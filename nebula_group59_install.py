"""NEBULA group59 wiring layer.

Connects the 20 previously dead classes of ``nebula_group59.py`` to a running
``NEBULAFullNode`` WITHOUT editing ``nebula_v10_11.py`` or ``nebula_group59.py``.

Usage
-----
    import nebula_v10_11 as host
    import nebula_group59_install as g59
    g59.install(host)        # every node created afterwards gets node.group59
    ...
    g59.uninstall(host)      # restores the host exactly as before

Design rules (taken from the group59 guide)
-------------------------------------------
* The layer NEVER rejects a block or a transaction. Every callback is wrapped
  in try/except and failures are only counted in ``layer.errors``.
* None of the 20 classes moves real funds: they only READ chain state
  (balances, height, supply). ValidatorStakingV2 is therefore report-only; the
  automatic block-reward accounting stays OFF unless ``observe_only=False``.
* In-memory lists are capped (``MAX_LIST``) so RAM cannot grow without limit.
* Persistent state is written atomically (tmp file + fsync + rename).
* Small guards in the layer protect against input problems of the verbatim
  classes (see the ``# GUARD`` comments) without editing those classes.
"""
from __future__ import annotations

import json
import os
import threading
import time
from collections import Counter, deque
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import nebula_group59 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

__all__ = ["Layer59", "install", "uninstall", "WIRING", "active_layers"]

# ---------------------------------------------------------------------------
# Wiring table: (no, class name, attribute on the layer, suggested hook, mode)
# ---------------------------------------------------------------------------
WIRING = [
    (1,  "SocialFiPlatform",           "social_fi",           "contract_economy", "instance"),
    (2,  "RealWorldAsset",             "rwa_platform",        "contract_economy", "created_by:rwa_platform"),
    (3,  "RWATokenizationPlatform",    "rwa_platform",        "contract_economy", "instance"),
    (4,  "AITradingSignals",           "trading_signals",     "chain_listener",   "instance"),
    (5,  "AIPortfolioOptimizer",       "portfolio_optimizer", "utility",          "instance"),
    (6,  "AISmartContractAuditor",     "contract_auditor",    "contract_economy", "instance"),
    (7,  "ZKIdentityProof",            "zk_proofs",           "security_monitor", "per_address_registry"),
    (8,  "SoulBoundToken",             "sbt",                 "contract_economy", "instance"),
    (9,  "CrossChainDeFiRouter",       "cross_chain",         "contract_economy", "instance"),
    (10, "QuadraticVoting",            "quadratic_voting",    "contract_economy", "instance"),
    (11, "DelegatedGovernance",        "delegated_gov",       "contract_economy", "instance"),
    (12, "HubAndSpokeNetwork",         "hub_network",         "p2p_peer",         "instance"),
    (13, "NEBULAAnalyticsDashboard",   "analytics",           "rest_rpc",         "instance"),
    (14, "NEBULAStorage",              "storage",             "storage_backup",   "instance"),
    (15, "DAOTreasuryManager",         "treasury",            "contract_economy", "instance"),
    (16, "ValidatorStakingV2",         "staking",             "chain_listener",   "instance_report_only"),
    (17, "DynamicNFT",                 "dynamic_nfts",        "contract_economy", "registry"),
    (18, "NFTFractionalizationV2",     "nft_frac",            "contract_economy", "instance"),
    (19, "NEBULAEcosystemIntegrations", "ecosystem",          "utility",          "class_level"),
    (20, "IBCPacket",                  "ibc_packets",         "utility",          "factory"),
]

_ACTIVE: List["Layer59"] = []          # layers created by the patched __init__
_ROUTE_PATHS = ("/api/g59/stats", "/api/g59/dashboard",
                "/api/g59/ecosystem", "/api/g59/storage",
                "/api/g59/validators", "/api/g59/wiring")


def active_layers() -> List["Layer59"]:
    return list(_ACTIVE)


def _first_attr(obj: Any, names) -> Any:
    """Return the first non-None attribute of ``obj`` out of ``names``."""
    for n in names:
        v = getattr(obj, n, None)
        if v is not None:
            return v
    return None


def _block_height(block: Any) -> Optional[int]:
    h = getattr(block, "height", None)
    if h is None:
        h = getattr(getattr(block, "header", None), "height", None)
    return h if isinstance(h, int) else None


def _block_proposer(block: Any) -> Optional[str]:
    for holder in (block, getattr(block, "header", None)):
        if holder is None:
            continue
        for n in ("proposer", "miner", "miner_address", "coinbase_address"):
            v = getattr(holder, n, None)
            if isinstance(v, str) and v:
                return v
    return None


class Layer59:
    """Owns one instance (or registry) of every group59 class for one node."""

    MAX_LIST = 10_000          # cap for every in-memory history list
    MAX_REGISTRY = 5_000       # cap for per-address / per-token registries
    PERSIST_EVERY = 100        # blocks between state saves
    STATE_FILE = "group59_state.json"

    def __init__(self, node: Any, observe_only: bool = True,
                 snapshot_every: int = 10, persist: bool = True):
        self.node = node
        self.bc = getattr(node, "bc", None)
        self.observe_only = observe_only
        self.snapshot_every = max(1, int(snapshot_every))
        self.errors = 0
        self.last_error: str = ""
        self.build_errors: Dict[str, str] = {}
        self.connected_blocks = 0
        self.reorgs = 0
        self.last_height: Optional[int] = None
        self.p2p_counts: Counter = Counter()
        self._lock = threading.RLock()
        self._p2p_orig: Dict[str, Any] = {}
        self._attached = False

        oracle = _first_attr(node, ("oracle", "oracle_v2", "price_oracle"))
        nft = _first_attr(node, ("nft", "nft_registry", "nbl721", "nbl721_registry"))
        bridge = _first_attr(node, ("bridge", "bridge_engine"))
        data_dir = _first_attr(node, ("data_dir", "datadir"))
        self.oracle, self.nft_registry, self.bridge = oracle, nft, bridge
        self.state_path: Optional[Path] = None
        if persist and data_dir:
            try:
                self.state_path = Path(str(data_dir)) / self.STATE_FILE
            except Exception:
                self.state_path = None

        # registries / factories
        self.zk_proofs: Dict[str, Any] = {}
        self.dynamic_nfts: Dict[str, Any] = {}
        self.ibc_packets: deque = deque(maxlen=self.MAX_LIST)

        # Build in the order of the guide (independent classes first).
        bc = self.bc
        self.social_fi = self._build("SocialFiPlatform", lambda: g.SocialFiPlatform(bc))
        self.rwa_platform = self._build("RWATokenizationPlatform",
                                        lambda: g.RWATokenizationPlatform(bc, oracle))
        self.trading_signals = self._build("AITradingSignals",
                                           lambda: g.AITradingSignals(oracle))
        self.portfolio_optimizer = self._build("AIPortfolioOptimizer",
                                               lambda: g.AIPortfolioOptimizer(oracle))
        self.contract_auditor = self._build("AISmartContractAuditor",
                                            lambda: g.AISmartContractAuditor())
        self.sbt = self._build("SoulBoundToken", lambda: g.SoulBoundToken(bc))
        self.cross_chain = self._build("CrossChainDeFiRouter",
                                       lambda: g.CrossChainDeFiRouter(bc, bridge))
        self.quadratic_voting = self._build("QuadraticVoting",
                                            lambda: g.QuadraticVoting(bc))
        self.delegated_gov = self._build("DelegatedGovernance",
                                         lambda: g.DelegatedGovernance(bc))
        self.hub_network = self._build("HubAndSpokeNetwork",
                                       lambda: g.HubAndSpokeNetwork(bc))
        self.analytics = self._build("NEBULAAnalyticsDashboard",
                                     lambda: g.NEBULAAnalyticsDashboard(bc, oracle))
        self.storage = self._build("NEBULAStorage", lambda: g.NEBULAStorage(bc))
        self.treasury = self._build("DAOTreasuryManager",
                                    lambda: g.DAOTreasuryManager(bc, oracle))
        self.staking = self._build("ValidatorStakingV2",
                                   lambda: g.ValidatorStakingV2(bc))
        if nft is not None:
            self.nft_frac = self._build("NFTFractionalizationV2",
                                        lambda: g.NFTFractionalizationV2(nft, bc))
        else:
            self.nft_frac = None
            self.build_errors["NFTFractionalizationV2"] = \
                "node has no NBL721 registry attribute (nft / nft_registry / nbl721)"
        self.ecosystem = g.NEBULAEcosystemIntegrations      # class-level registry

        self._load_state()

    # ------------------------------------------------------------------ utils
    def _build(self, name: str, factory: Callable[[], Any]) -> Any:
        try:
            return factory()
        except Exception as e:              # one failure must not block the others
            self.build_errors[name] = f"{type(e).__name__}: {e}"
            return None

    def _fail(self, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.last_error = f"{where}: {type(exc).__name__}: {exc}"

    def safe(self, where: str, fn: Callable, *a, **k) -> Dict[str, Any]:
        """Call ``fn``; never raise. Returns the result or an error dict."""
        try:
            return fn(*a, **k)
        except Exception as e:
            self._fail(where, e)
            return {"ok": False, "error": f"{type(e).__name__}: {e}"}

    # ------------------------------------------------------- chain listener
    def on_connect(self, block: Any) -> None:
        try:
            with self._lock:
                self.connected_blocks += 1
                h = _block_height(block)
                if h is None and self.bc is not None:
                    h = getattr(self.bc, "height", None)
                self.last_height = h

                # 1. periodic analytics snapshot
                if self.analytics and self.connected_blocks % self.snapshot_every == 0:
                    try:
                        self.analytics.snapshot()
                    except Exception as e:
                        self._fail("analytics.snapshot", e)

                # 2. dynamic NFTs evolve from chain height
                for key, nft in list(self.dynamic_nfts.items()):
                    try:
                        nft.check_evolution()
                    except Exception as e:
                        self._fail(f"dynamic_nft[{key}]", e)

                # 3. optional reward accounting (OFF by default, report-only)
                if not self.observe_only and self.staking and h is not None:
                    proposer = _block_proposer(block)
                    if proposer:
                        try:
                            self.staking.distribute_block_reward(
                                proposer, g.mining_reward(h))
                        except Exception as e:
                            self._fail("staking.distribute_block_reward", e)

                # 4. bounded memory and periodic persistence
                self._trim()
                if self.connected_blocks % self.PERSIST_EVERY == 0:
                    self.save_state()
        except Exception as e:              # never propagate into the chain
            self._fail("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        try:
            with self._lock:
                self.reorgs += 1
                if self.analytics is not None:
                    hist = self.analytics._metrics_history
                    hist[:] = [m for m in hist
                               if m.get("block", 0) <= ancestor_height]
                self.last_height = ancestor_height
        except Exception as e:
            self._fail("on_reorg", e)

    # ----------------------------------------------------------- P2P observer
    def attach_p2p(self) -> bool:
        """Observe P2P messages. The original handler ALWAYS runs first."""
        p2p = _first_attr(self.node, ("p2p", "p2p_node", "network"))
        if p2p is None or not callable(getattr(p2p, "_handle_message", None)):
            return False
        if "_handle_message" in self._p2p_orig:
            return True
        orig = p2p._handle_message
        layer = self

        def wrapped(peer, msg, *a, **k):
            result = orig(peer, msg, *a, **k)       # original first, always
            try:
                layer.on_p2p_message(peer, msg)
            except Exception as e:
                layer._fail("p2p_observer", e)
            return result

        self._p2p_orig["_handle_message"] = orig
        self._p2p_target = p2p
        p2p._handle_message = wrapped
        return True

    def on_p2p_message(self, peer: Any, msg: Any) -> None:
        kind = "unknown"
        if isinstance(msg, dict):
            kind = str(msg.get("type") or msg.get("cmd") or "unknown")[:32]
        with self._lock:
            if kind in self.p2p_counts or len(self.p2p_counts) < 256:
                self.p2p_counts[kind] += 1

    def detach(self) -> None:
        try:
            self.save_state()
        except Exception as e:
            self._fail("detach.save_state", e)
        try:
            if self.bc is not None:
                self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer59.detach", exc_info=True)
        orig = self._p2p_orig.pop("_handle_message", None)
        target = getattr(self, "_p2p_target", None)
        if orig is not None and target is not None:
            try:
                # remove the instance override; the class method is used again
                if "_handle_message" in vars(target):
                    del target._handle_message
                    if getattr(target, "_handle_message", None) != orig:
                        target._handle_message = orig
            except Exception as e:
                self._fail("detach.p2p", e)
        self._attached = False

    # ---------------------------------------------------------- memory caps
    def _trim(self) -> None:
        cap = self.MAX_LIST
        pairs = [
            (self.trading_signals, "_signals"),
            (self.hub_network, "_payments"),
            (self.cross_chain, "_routes"),
            (self.social_fi, "_content"),
            (self.analytics, "_metrics_history"),
            (self.staking, "_slashes"),
            (self.treasury, "_txs"),
            (self.delegated_gov, "_votes"),
        ]
        for obj, attr in pairs:
            lst = getattr(obj, attr, None) if obj is not None else None
            if isinstance(lst, list) and len(lst) > cap:
                del lst[: len(lst) - cap]

    # ------------------------------------------------------------ factories
    def zk_for(self, address: str) -> Optional[Any]:
        """Per-address ZKIdentityProof (created on first use, capped)."""
        with self._lock:
            obj = self.zk_proofs.get(address)
            if obj is None:
                if len(self.zk_proofs) >= self.MAX_REGISTRY:
                    return None
                obj = g.ZKIdentityProof(address, self.bc)
                self.zk_proofs[address] = obj
            return obj

    def make_dynamic_nft(self, token_id: int, collection_id: str,
                         owner: str, base_uri: str) -> Optional[Any]:
        key = f"{collection_id}:{token_id}"
        with self._lock:
            if key in self.dynamic_nfts:
                return self.dynamic_nfts[key]
            if len(self.dynamic_nfts) >= self.MAX_REGISTRY:
                return None
            obj = g.DynamicNFT(token_id, collection_id, owner, base_uri, self.bc)
            self.dynamic_nfts[key] = obj
            return obj

    def make_ibc_packet(self, sequence: int, src_port: str, src_channel: str,
                        dst_port: str, dst_channel: str, data: bytes,
                        timeout_height: int) -> Any:
        pkt = g.IBCPacket(sequence, src_port, src_channel, dst_port,
                          dst_channel, data, timeout_height)
        self.ibc_packets.append(pkt)
        return pkt

    # ------------------------------------------------- guarded facade methods
    # GUARD: the verbatim classes trust their inputs; these wrappers validate.
    def tokenize_asset(self, issuer: str, asset_type: str, value_usd: float,
                       token_count: int, description: str,
                       legal_doc: str = "") -> Dict[str, Any]:
        # GUARD: RealWorldAsset divides by token_count -> must be > 0.
        if not isinstance(token_count, int) or token_count <= 0:
            return {"ok": False, "error": "token_count must be a positive integer"}
        if not isinstance(value_usd, (int, float)) or value_usd <= 0:
            return {"ok": False, "error": "value_usd must be positive"}
        return self.safe("rwa.tokenize_asset", self.rwa_platform.tokenize_asset,
                         issuer, asset_type, value_usd, token_count,
                         description, legal_doc)

    def qv_vote(self, voter: str, pid: str, option: str,
                voice_credits: int) -> Dict[str, Any]:
        # GUARD: QuadraticVoting adds to the tally on every call, so a repeat
        # vote by the same voter would be counted twice. One vote per voter.
        if not isinstance(voice_credits, int) or voice_credits <= 0:
            return {"ok": False, "error": "voice_credits must be a positive integer"}
        with self._lock:
            prop = self.quadratic_voting._proposals.get(pid)
            if prop and voter in prop["voters"]:
                return {"ok": False, "error": "Already voted on this proposal"}
            return self.safe("qv.vote", self.quadratic_voting.vote,
                             voter, pid, option, voice_credits)

    def fractionalize(self, owner: str, collection_id: str, token_id: int,
                      shares: int, reserve_price_nbl: float) -> Dict[str, Any]:
        # GUARD: vault ids are deterministic, so a second call would overwrite
        # (reset) an existing vault. Refuse if the NFT already has a vault.
        if not isinstance(shares, int) or shares <= 0:
            return {"ok": False, "error": "shares must be a positive integer"}
        if reserve_price_nbl < 0:
            return {"ok": False, "error": "reserve price must not be negative"}
        if self.nft_frac is None:
            return {"ok": False, "error": "NFT registry not available on this node"}
        with self._lock:
            for v in self.nft_frac._vaults.values():
                if v["collection"] == collection_id and v["token_id"] == token_id:
                    return {"ok": False, "error": "NFT already fractionalized"}
            return self.safe("nft_frac.fractionalize", self.nft_frac.fractionalize,
                             owner, collection_id, token_id, shares,
                             reserve_price_nbl)

    def hub_send_payment(self, sender: str, receiver: str,
                         amount_nbl: float) -> Dict[str, Any]:
        # GUARD: hub-routed payments in HubAndSpokeNetwork do not move any
        # balance, so only direct channels (which do) are allowed here.
        if not isinstance(amount_nbl, (int, float)) or amount_nbl <= 0:
            return {"ok": False, "error": "amount must be positive"}
        with self._lock:
            route = self.hub_network.find_route(sender, receiver, amount_nbl)
            if not route or route[0].get("type") != "direct":
                return {"ok": False,
                        "error": "No direct channel with enough balance "
                                 "(hub routing is simulated only)"}
            return self.safe("hub.send_payment", self.hub_network.send_payment,
                             sender, receiver, amount_nbl)

    # ---------------------------------------------------------------- reports
    def stats(self) -> Dict[str, Any]:
        """One read-only summary of every wired class."""
        def s(obj, meth):
            if obj is None:
                return None
            try:
                return getattr(obj, meth)()
            except Exception as e:
                self._fail(f"stats.{meth}", e)
                return {"error": str(e)}
        return {
            "layer": {
                "errors": self.errors, "last_error": self.last_error,
                "blocks_seen": self.connected_blocks, "reorgs": self.reorgs,
                "last_height": self.last_height,
                "observe_only": self.observe_only,
                "build_errors": dict(self.build_errors),
                "p2p_messages": dict(self.p2p_counts),
            },
            "social_fi": s(self.social_fi, "social_stats"),
            "rwa": s(self.rwa_platform, "rwa_stats"),
            "sbt": s(self.sbt, "sbt_stats"),
            "cross_chain": s(self.cross_chain, "router_stats"),
            "quadratic_voting": s(self.quadratic_voting, "qv_stats"),
            "delegated_governance": s(self.delegated_gov, "governance_stats"),
            "hub_network": s(self.hub_network, "network_stats"),
            "storage": s(self.storage, "storage_stats"),
            "treasury": s(self.treasury, "treasury_report"),
            "validators": s(self.staking, "validator_set_stats"),
            "nft_fractions": s(self.nft_frac, "frac_stats"),
            "dynamic_nfts": len(self.dynamic_nfts),
            "zk_identities": len(self.zk_proofs),
            "ibc_packets": len(self.ibc_packets),
        }

    def wiring_report(self) -> List[Dict[str, Any]]:
        """Per-class status; used by the tests to prove all 20 are wired."""
        rows = []
        for no, cls_name, attr, hook, mode in WIRING:
            target = getattr(self, attr, None)
            if mode == "created_by:rwa_platform":
                ready = self.rwa_platform is not None
            elif mode in ("registry", "per_address_registry", "factory",
                          "class_level"):
                ready = target is not None
            else:
                ready = target is not None
            rows.append({"no": no, "class": cls_name, "attr": attr,
                         "hook": hook, "mode": mode, "ready": bool(ready),
                         "issue": self.build_errors.get(cls_name, "")})
        return rows

    def dependency_report(self) -> Dict[str, bool]:
        """Names the group59 classes need from other groups / the host."""
        return {"SocialToken (group58)": hasattr(g, "SocialToken"),
                "NBL721 registry on node": self.nft_registry is not None,
                "oracle on node": self.oracle is not None}

    # -------------------------------------------------------- persistence
    def save_state(self) -> bool:
        """Atomic write: tmp file + fsync + rename (+ best-effort dir fsync)."""
        if self.state_path is None:
            return False
        try:
            with self._lock:
                payload = {
                    "version": 1,
                    "saved_at": time.time(),
                    "storage_files": getattr(self.storage, "_files", {}),
                    "storage_pins": getattr(self.storage, "_pins", {}),
                    "sbt_tokens": getattr(self.sbt, "_tokens", {}),
                    "kyc_verified": sorted(
                        getattr(self.rwa_platform, "_kyc_verified", set())),
                }
                text = json.dumps(payload, default=str)
            self.state_path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.state_path.with_suffix(".tmp")
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(text)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, self.state_path)
            try:
                dfd = os.open(str(self.state_path.parent), os.O_RDONLY)
                try:
                    os.fsync(dfd)
                finally:
                    os.close(dfd)
            except OSError:
                _NB_SWALLOW_LOG.warning("swallowed OSError in Layer59.save_state", exc_info=True)
            return True
        except Exception as e:
            self._fail("save_state", e)
            return False

    def _load_state(self) -> None:
        if self.state_path is None or not self.state_path.exists():
            return
        try:
            data = json.loads(self.state_path.read_text(encoding="utf-8"))
            if self.storage is not None:
                self.storage._files.update(data.get("storage_files", {}))
                self.storage._pins.update(data.get("storage_pins", {}))
            if self.sbt is not None:
                self.sbt._tokens.update(data.get("sbt_tokens", {}))
            if self.rwa_platform is not None:
                self.rwa_platform._kyc_verified.update(data.get("kyc_verified", []))
        except Exception as e:              # a corrupt file must not stop the node
            self._fail("load_state", e)


# ---------------------------------------------------------------------------
# REST (read-only GET) endpoints
# ---------------------------------------------------------------------------
def _register_routes(host: Any) -> None:
    route = getattr(host, "route", None)
    if route is None:
        return
    ok_fn = getattr(host, "ok", None)

    def reply(data: Dict[str, Any]):
        if callable(ok_fn):
            try:
                return ok_fn(data)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in _register_routes.reply", exc_info=True)
        return 200, {"success": True, "data": data}

    def layer() -> Optional[Layer59]:
        return _ACTIVE[-1] if _ACTIVE else None

    def make(fn: Callable[[Layer59], Any]):
        def handler(*args, **kwargs):
            lay = layer()
            if lay is None:
                return reply({"error": "group59 layer not active"})
            try:
                return reply(fn(lay))
            except Exception as e:
                lay._fail("rest", e)
                return reply({"error": f"{type(e).__name__}: {e}"})
        return handler

    table = {
        "/api/g59/stats":      lambda l: l.stats(),
        "/api/g59/dashboard":  lambda l: l.analytics.full_dashboard(),
        "/api/g59/ecosystem":  lambda l: l.ecosystem.all(),
        "/api/g59/storage":    lambda l: l.storage.storage_stats(),
        "/api/g59/validators": lambda l: l.staking.validator_set_stats(),
        "/api/g59/wiring":     lambda l: l.wiring_report(),
    }
    existing = getattr(host, "_routes", {}).get("GET", {})
    for path, fn in table.items():
        if path not in existing:            # never override a host route
            route(path, ["GET"])(make(fn))


def _unregister_routes(host: Any) -> None:
    get_routes = getattr(host, "_routes", {}).get("GET", {})
    for path in _ROUTE_PATHS:
        get_routes.pop(path, None)


# ---------------------------------------------------------------------------
# install / uninstall (same pattern as group 5)
# ---------------------------------------------------------------------------
def install(host: Any, observe_only: bool = True, snapshot_every: int = 10,
            persist: bool = True) -> bool:
    """Patch ``NEBULAFullNode.__init__``. Safe to call twice."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g59_orig", None):
        return False
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)                 # the host always initialises first
        try:
            lay = Layer59(self, observe_only=observe_only,
                          snapshot_every=snapshot_every, persist=persist)
            self.group59 = lay
            if getattr(self, "bc", None) is not None:
                self.bc.add_listener(lay)
                lay._attached = True
            lay.attach_p2p()
            _ACTIVE.append(lay)
        except Exception as e:              # the node must still start
            self.group59_error = e

    cls._g59_orig = orig
    cls.__init__ = patched
    try:
        _register_routes(host)
    except Exception:
        _NB_SWALLOW_LOG.debug("swallowed Exception in install", exc_info=True)
    return True


def uninstall(host: Any) -> bool:
    """Restore the host exactly as before and detach every live layer."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g59_orig", None)
    if not orig:
        return False
    cls.__init__ = orig
    del cls._g59_orig
    for lay in list(_ACTIVE):
        lay.detach()
    _ACTIVE.clear()
    try:
        _unregister_routes(host)
    except Exception:
        _NB_SWALLOW_LOG.debug("swallowed Exception in uninstall", exc_info=True)
    return True
