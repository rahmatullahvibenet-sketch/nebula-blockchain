"""NEBULA group50 - wiring layer.

Connects the 20 classes of ``nebula_group50.py`` to a running NEBULA node WITHOUT editing the
host file (``nebula_v10_11.py``) and WITHOUT editing ``nebula_group50.py``.

Design rules
------------
1. Observe by default.  Everything that only *reads* chain data or keeps in-memory statistics is
   switched on.  Everything that mutates state, creates identity claims, resolves markets, relays
   transactions, runs keeper actions or mints dev coins is OFF until you enable it explicitly in
   ``Group50Config``.
2. Never break the node.  Every callback and every public method catches all exceptions, counts
   them in ``layer.errors`` and records them in ``layer.error_log``.  A failing component can never
   reject a block or a transaction.
3. Never touch consensus.  The layer is a chain *listener* (``on_connect`` / ``on_reorg``) plus an
   optional passive observer on ``Mempool.submit`` (the original method always runs first and its
   result is returned unchanged).
4. Fully reversible: ``uninstall(host)`` restores the original ``NEBULAFullNode.__init__`` and
   ``Mempool.submit`` and detaches every layer.
5. Bounded memory.  All growing lists and ledgers are capped.

Usage
-----
    import nebula_v10_11 as host
    import nebula_group50_install as g50
    g50.install(host)                 # patches NEBULAFullNode.__init__ -> node.group50 is created
    ...
    node = host.NEBULAFullNode(...)   # normal construction
    node.group50.status()             # which components are connected
    node.group50.stats()              # read-only statistics of every component

or, for a node that already exists:

    layer = g50.attach(node, host, g50.Group50Config(...))

Every public method returns ``(ok: bool, value_or_reason)``.
"""
from __future__ import annotations

import functools
import inspect
import json
import logging
import math
import threading
import time
import weakref
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple

import nebula_group50 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

__all__ = ["Group50Config", "Layer50", "install", "uninstall", "attach", "is_installed"]

_log = logging.getLogger("nebula.group50")

# Names the group50 classes look up as module globals.  When a host module is passed explicitly we
# bind these to THAT host's live classes (not to a second copy imported by nebula_group50 itself).
_HOST_DEPENDENCIES = ("Epoch", "ConcentratedLiquidityPool", "ContractFactory", "NEBULAWallet")

# Service discovery: role -> (candidate attribute names on node / blockchain, host class names that
# may be used to create a standalone instance when no live one exists).
_SERVICE_NAMES: Dict[str, Tuple[Tuple[str, ...], Tuple[str, ...]]] = {
    "validator_set":       (("validator_set", "validators", "validator_manager",
                             "validator_set_manager"), ("ValidatorSetManager",)),
    "rng":                 (("rng", "onchain_rng", "on_chain_rng"), ("OnChainRNG",)),
    "order_book_mgr":      (("order_book_mgr", "order_books", "orderbook_manager",
                             "order_book_manager"), ("OrderBookManager",)),
    "did_v2":              (("did_v2", "did_registry", "did"), ()),
    "reputation":          (("reputation", "reputation_engine"), ()),
    "compliance":          (("compliance", "compliance_engine"), ()),
    "oracle":              (("oracle", "oracle_v2", "price_oracle"), ()),
    "liquidation_engine":  (("liquidation_engine", "liquidations", "liquidation"), ()),
    "rewards_distributor": (("rewards_distributor", "rewards"), ()),
}


# ----------------------------------------------------------------------------------------------
# configuration
# ----------------------------------------------------------------------------------------------
@dataclass
class Group50Config:
    """All switches of the wiring layer.  Defaults are the safe 'observe only' profile."""

    # --- passive features (on by default) ---
    track_epoch_rewards: bool = True          # feed EpochSystem from connected blocks (reorg-safe)
    track_delegated_rewards: bool = True      # DelegatedStaking in-memory reward accounting
    track_mempool: bool = True                # passive Mempool.submit observer -> FeeOptimizer
    analytics_every_blocks: int = 144         # holder snapshot period (0 = never)

    # --- state-changing features (OFF by default) ---
    allow_identity_writes: bool = False       # IdentityHub.verify_identity (KYC claims)
    allow_relay: bool = False                 # GaslessRelay.relay_for (submits txs to mempool)
    run_keeper_actions: bool = False          # KeeperBot liquidations / distributions
    keeper_every_blocks: int = 0              # keeper period (0 = never automatic)
    keeper_address: Optional[str] = None      # address that receives keeper bonuses
    market_admins: Tuple[str, ...] = ()       # who may resolve prediction markets (empty = nobody)
    relayer_address: Optional[str] = None     # GaslessRelay relayer (None = class default)
    enable_dev_tools: bool = True             # still needs chain dev mode (see _enable_dev_mode)

    # --- explicit service injection: {"validator_set": obj, "oracle": obj, ...} ---
    services: Dict[str, Any] = field(default_factory=dict)
    create_missing_services: bool = True      # try host.<Class>(bc) when no live service is found

    # --- limits ---
    max_records: int = 1000                   # cap for every growing list
    ledger_depth: int = 5000                  # heights remembered for reorg rollback
    max_profiles: int = 100_000
    max_channels: int = 10_000
    max_markets: int = 10_000
    max_vaults: int = 10_000


class _Rejected(Exception):
    """Input validation failure (returned to the caller as (False, reason))."""


class _Unavailable(Exception):
    """Component is not connected (returned to the caller as (False, reason))."""


def _safe(fn: Callable) -> Callable:
    """Public-method decorator: never raise, always return (ok, value_or_reason)."""
    @functools.wraps(fn)
    def wrapper(self: "Layer50", *a, **k):
        try:
            res = fn(self, *a, **k)
        except (_Rejected, _Unavailable) as e:
            return False, str(e)
        except Exception as e:                                       # noqa: BLE001 - by design
            self._fail(fn.__name__, e)
            return False, f"{type(e).__name__}: {e}"
        if isinstance(res, tuple) and len(res) == 2 and isinstance(res[0], bool):
            return res
        return True, res
    return wrapper


# ----------------------------------------------------------------------------------------------
# small validation helpers
# ----------------------------------------------------------------------------------------------
def _is_num(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _pos_int(x: Any, what: str) -> int:
    if not isinstance(x, int) or isinstance(x, bool) or x <= 0:
        raise _Rejected(f"{what} must be a positive integer")
    return x


def _pos_num(x: Any, what: str) -> float:
    if not _is_num(x) or x <= 0:
        raise _Rejected(f"{what} must be a positive finite number")
    return float(x)


def _addr(x: Any, what: str = "address") -> str:
    if not isinstance(x, str) or not (0 < len(x) <= 128) or not x.isprintable():
        raise _Rejected(f"{what} must be a printable string of 1-128 characters")
    return x


def _ident(x: Any, what: str) -> str:
    if not isinstance(x, str) or not (0 < len(x) <= 64) or not x.isprintable():
        raise _Rejected(f"{what} must be a printable string of 1-64 characters")
    return x


def _weights(targets: Any, what: str = "targets") -> Dict[str, float]:
    if not isinstance(targets, dict) or not (1 <= len(targets) <= 64):
        raise _Rejected(f"{what} must be a dict with 1-64 entries")
    out: Dict[str, float] = {}
    for k, v in targets.items():
        _ident(k, f"{what} key")
        if not _is_num(v) or v < 0:
            raise _Rejected(f"{what}['{k}'] must be a non-negative finite number")
        out[k] = float(v)
    if abs(sum(out.values()) - 1.0) > 0.001:
        raise _Rejected(f"{what} must sum to 1.0")
    return out


def _is_service(x: Any) -> bool:
    """True for a live object that can act as a service (not None / primitive / function / class)."""
    if x is None or isinstance(x, (str, bytes, int, float, bool, list, tuple, set, dict, type)):
        return False
    return not (inspect.isroutine(x) or inspect.isclass(x))


def _nonneg_int(x: Any, what: str) -> int:
    if not isinstance(x, int) or isinstance(x, bool) or x < 0:
        raise _Rejected(f"{what} must be a non-negative integer")
    return x


def _get(obj: Any, name: str, default: Any = None) -> Any:
    """getattr that also understands dict-like blocks / transactions."""
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _trim(seq: list, cap: int) -> None:
    if len(seq) > cap:
        del seq[: len(seq) - cap]


# ----------------------------------------------------------------------------------------------
# fallback Epoch (used ONLY when the host does not provide one)
# ----------------------------------------------------------------------------------------------
class _FallbackEpoch:
    """Minimal stand-in with the interface EpochSystem uses (number, start/end block, rewards)."""

    def __init__(self, number: int, start_block: int, duration: int):
        self.number = number
        self.start_block = start_block
        self.end_block = start_block + duration
        self.rewards_distributed = 0

    def progress(self, height: int) -> float:
        span = max(1, self.end_block - self.start_block)
        return max(0.0, min(1.0, (height - self.start_block) / span))

    def to_dict(self) -> dict:
        return {"number": self.number, "start_block": self.start_block,
                "end_block": self.end_block,
                "rewards_distributed": self.rewards_distributed}


# ----------------------------------------------------------------------------------------------
# the layer
# ----------------------------------------------------------------------------------------------
class Layer50:
    """Owns one instance of every group50 service and bridges it to the node."""

    def __init__(self, node: Any, host: Any = None, config: Optional[Group50Config] = None):
        self.node = node
        self.host = host
        self.cfg = config or Group50Config()
        self.bc = _get(node, "bc") or _get(node, "blockchain")
        if self.bc is None:
            raise ValueError("node has no 'bc' / 'blockchain' attribute")

        self._lock = threading.RLock()
        self.errors = 0
        self.error_log: deque = deque(maxlen=50)
        self.blocks_seen = 0
        self.reorgs_seen = 0
        self.last_height = -1
        self.mempool_seen = 0
        self.mempool_accepted = 0
        self.status_map: Dict[str, str] = {}
        self.notes: List[str] = []
        self.components: Dict[str, Any] = {}
        self.services: Dict[str, Any] = {}
        self.channels: Dict[str, Any] = {}
        self.markets: Dict[str, Any] = {}
        self.vaults: Dict[str, Any] = {}
        self.last_holder_snapshot: Optional[dict] = None
        # per-height ledger so a reorg can be rolled back exactly
        self._ledger: Dict[int, dict] = {}
        self._attached = False

        self._prepare_namespace()
        self._discover_services()
        self._build_components()

    # ------------------------------------------------------------------ setup
    def _prepare_namespace(self) -> None:
        """Bind host-provided classes into nebula_group50's globals (explicit host wins)."""
        host = self.host
        for name in _HOST_DEPENDENCIES:
            cls = getattr(host, name, None) if host is not None else None
            if cls is not None:
                setattr(g, name, cls)
        if not hasattr(g, "Epoch"):
            g.Epoch = _FallbackEpoch                                 # type: ignore[attr-defined]
            self.notes.append("host has no Epoch class: using built-in fallback Epoch")
        for name in _HOST_DEPENDENCIES[1:]:
            if not hasattr(g, name):
                self.notes.append(f"host class {name} not found: dependent methods will return "
                                  f"(False, reason) until it is available")

    def _discover_services(self) -> None:
        for role, (attr_names, class_names) in _SERVICE_NAMES.items():
            found = self.cfg.services.get(role)
            origin = "config" if found is not None else ""
            if found is None:
                for holder in (self.node, self.bc):
                    for n in attr_names:
                        cand = _get(holder, n)
                        if _is_service(cand):
                            found, origin = cand, f"{type(holder).__name__}.{n}"
                            break
                    if found is not None:
                        break
            if found is None and self.cfg.create_missing_services and self.host is not None:
                for cn in class_names:
                    cls = getattr(self.host, cn, None)
                    if cls is None:
                        continue
                    for args in ((self.bc,), ()):
                        try:
                            found, origin = cls(*args), f"standalone {cn}"
                            break
                        except Exception:                           # noqa: BLE001
                            continue
                    if found is not None:
                        break
            if found is not None:
                self.services[role] = found
                self.notes.append(f"service {role}: {origin}")

    def _build(self, name: str, factory: Callable[[], Any], needs: Iterable[str] = ()) -> None:
        missing = [n for n in needs if self.services.get(n) is None]
        if missing:
            self.status_map[name] = f"skipped: missing service(s) {missing}"
            return
        try:
            obj = factory()
        except PermissionError as e:
            self.status_map[name] = f"disabled (safe): {e}"
            return
        except Exception as e:                                       # noqa: BLE001
            self.status_map[name] = f"failed: {type(e).__name__}: {e}"
            self._fail(f"build:{name}", e)
            return
        self.components[name] = obj
        self.status_map[name] = "ok"

    def _build_components(self) -> None:
        bc, sv, cfg = self.bc, self.services, self.cfg
        b = self._build
        b("epoch_system",    lambda: g.EpochSystem(bc))
        b("identity_hub",    lambda: g.IdentityHub(bc, sv.get("did_v2"), sv.get("reputation"),
                                                   sv.get("compliance")))
        b("dex_v2",          lambda: g.AdvancedDEXV2(bc))
        b("orderbook",       lambda: g.OrderbookAggregator(sv["order_book_mgr"]),
          needs=("order_book_mgr",))
        b("fee_optimizer",   lambda: g.FeeOptimizer(bc))
        b("reward_schedule", lambda: g.BlockRewardSchedule(bc))
        b("validator_select", lambda: g.ValidatorSelectionAlgorithm(sv["validator_set"], sv["rng"]),
          needs=("validator_set", "rng"))
        b("xswap",           lambda: g.CrossChainSwapV2(bc))
        b("rebalancer",      lambda: g.PortfolioRebalancer(bc, sv.get("oracle")))
        b("analytics",       lambda: g.OnChainAnalyticsV2(bc))
        b("delegation",      lambda: g.DelegatedStaking(bc, sv["validator_set"]),
          needs=("validator_set",))
        b("launchpad",       lambda: g.LaunchpadV2(bc))
        relay_args = (cfg.relayer_address,) if cfg.relayer_address else ()
        b("relay",           lambda: g.GaslessRelay(bc, *relay_args, oracle=sv.get("oracle")))
        b("keeper",          lambda: g.KeeperBot(bc, cfg.keeper_address or "UNCONFIGURED_KEEPER"))
        if cfg.enable_dev_tools:
            b("dev_tools",   lambda: g.NEBULADevTools(bc))
        else:
            self.status_map["dev_tools"] = "disabled by config"
        b("community",       lambda: g.CommunityHub(bc))
        # per-entity classes are created on demand through the registries below
        self.status_map["state_channels"] = "ok (registry; channels created on demand)"
        self.status_map["prediction_markets"] = "ok (registry; markets created on demand)"
        self.status_map["vaults"] = "ok (registry; vaults created on demand)"
        self.status_map["ido_parameters"] = "ok (built by create_ido)"

    # ------------------------------------------------------------------ bookkeeping
    def _fail(self, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.error_log.append(f"{time.strftime('%H:%M:%S')} {where}: {type(exc).__name__}: {exc}")
        _log.warning("group50 %s failed: %s: %s", where, type(exc).__name__, exc)

    def _need(self, name: str) -> Any:
        comp = self.components.get(name)
        if comp is None:
            raise _Unavailable(f"component '{name}' is not connected "
                               f"({self.status_map.get(name, 'not built')})")
        return comp

    # ------------------------------------------------------------------ chain listener protocol
    def _block_height(self, block: Any) -> int:
        for holder in (block, _get(block, "header")):
            for n in ("height", "index", "number"):
                v = _get(holder, n)
                if isinstance(v, int) and not isinstance(v, bool):
                    return v
        return int(_get(self.bc, "height", 0) or 0)

    @staticmethod
    def _block_miner(block: Any) -> Optional[str]:
        for n in ("miner", "miner_address", "coinbase_address", "proposer", "validator"):
            v = _get(block, n)
            if isinstance(v, str) and v:
                return v
        txs = _get(block, "transactions") or _get(block, "txs") or []
        try:
            outs = _get(txs[0], "outputs") or []
            return _get(outs[0], "address") if outs else None
        except Exception:                                            # noqa: BLE001
            return None

    def on_connect(self, block: Any) -> None:
        """Chain listener: a block was connected to the best chain."""
        try:
            with self._lock:
                h = self._block_height(block)
                if h in self._ledger:                    # duplicate delivery: never double count
                    return
                entry: Dict[str, Any] = {"epoch": 0, "deleg": {}}
                if self.cfg.track_epoch_rewards:
                    self._epoch_credit(h, entry)
                if self.cfg.track_delegated_rewards:
                    self._delegation_credit(h, block, entry)
                self._ledger[h] = entry
                while len(self._ledger) > self.cfg.ledger_depth:
                    self._ledger.pop(min(self._ledger))
                self.blocks_seen += 1
                self.last_height = h
                self._periodic(h)
                self._enforce_caps()
        except Exception as e:                                       # noqa: BLE001
            self._fail("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        """Chain listener: blocks above ``ancestor_height`` were disconnected."""
        try:
            with self._lock:
                self.reorgs_seen += 1
                for h in sorted((x for x in self._ledger if x > ancestor_height), reverse=True):
                    entry = self._ledger.pop(h)
                    self._epoch_debit(h, entry.get("epoch", 0))
                    self._delegation_debit(entry.get("deleg", {}))
                self.last_height = min(self.last_height, int(ancestor_height))
        except Exception as e:                                       # noqa: BLE001
            self._fail("on_reorg", e)

    # --- epoch accounting
    def _epoch_credit(self, h: int, entry: dict) -> None:
        es = self.components.get("epoch_system")
        if es is None:
            return
        amount = int(g.mining_reward(h))
        if amount <= 0:
            return
        if int(_get(self.bc, "height", -1)) == h:
            es.record_reward(amount)                     # normal path: tip == this block
        else:
            self._epoch_for(es, h).rewards_distributed += amount
        entry["epoch"] = amount

    def _epoch_debit(self, h: int, amount: int) -> None:
        es = self.components.get("epoch_system")
        if es is None or not amount:
            return
        ep = self._epoch_for(es, h)
        ep.rewards_distributed = max(0, ep.rewards_distributed - amount)

    @staticmethod
    def _epoch_for(es: Any, h: int) -> Any:
        dur = es.EPOCH_DURATION
        num = h // dur
        with es._lock:
            ep = es._epochs.get(num)
            if ep is None:
                ep = g.Epoch(num, num * dur, dur)
                es._epochs[num] = ep
            return ep

    # --- delegated staking accounting (in-memory only, never moves coins)
    def _delegation_credit(self, h: int, block: Any, entry: dict) -> None:
        ds = self.components.get("delegation")
        miner = self._block_miner(block)
        if ds is None or not miner:
            return
        before = dict(ds._rewards)
        ds.distribute_block_rewards(int(g.mining_reward(h)), miner)
        entry["deleg"] = {k: v - before.get(k, 0) for k, v in ds._rewards.items()
                          if v - before.get(k, 0)}

    def _delegation_debit(self, deltas: Dict[str, int]) -> None:
        ds = self.components.get("delegation")
        if ds is None:
            return
        for k, v in deltas.items():
            left = ds._rewards.get(k, 0) - v
            if left > 0:
                ds._rewards[k] = left
            else:
                ds._rewards.pop(k, None)

    # --- periodic jobs
    def _periodic(self, h: int) -> None:
        n = self.cfg.analytics_every_blocks
        if n and h % n == 0 and "analytics" in self.components:
            try:
                self.last_holder_snapshot = self.components["analytics"] \
                    .holder_distribution_snapshot()
            except Exception as e:                                   # noqa: BLE001
                self._fail("analytics.snapshot", e)
        k = self.cfg.keeper_every_blocks
        if k and h % k == 0:
            self.run_keeper_once()

    def _enforce_caps(self) -> None:
        cap = self.cfg.max_records
        for name, attr in (("analytics", "_snapshots"), ("keeper", "_executions"),
                           ("relay", "_relayed"), ("fee_optimizer", "_history")):
            comp = self.components.get(name)
            if comp is not None:
                _trim(getattr(comp, attr, []), cap)

    # ------------------------------------------------------------------ mempool observer
    def observe_submit(self, tx: Any, result: Any) -> None:
        """Called by the passive Mempool.submit wrapper AFTER the original method returned."""
        try:
            with self._lock:
                self.mempool_seen += 1
                accepted = isinstance(result, tuple) and bool(result and result[0])
                if accepted:
                    self.mempool_accepted += 1
                fo = self.components.get("fee_optimizer")
                fee = _get(tx, "fee")
                if fo is not None and accepted and _is_num(fee):
                    size = 0
                    try:
                        size = int(tx.byte_size())
                    except Exception:                                # noqa: BLE001
                        _NB_SWALLOW_LOG.debug("swallowed Exception in Layer50.observe_submit", exc_info=True)
                    fo._history.append({"ts": time.time(), "fee": fee, "size": size})
                    _trim(fo._history, self.cfg.max_records)
        except Exception as e:                                       # noqa: BLE001
            self._fail("observe_submit", e)

    # ------------------------------------------------------------------ attach / detach
    def attach(self) -> None:
        if self._attached:
            return
        self.bc.add_listener(self)
        self._attached = True
        if self.cfg.track_mempool:
            mp = _get(self.bc, "mempool")
            try:
                mp._g50_observer = self.observe_submit
            except Exception as e:                                   # noqa: BLE001
                self.notes.append(f"mempool observer not attached: {e}")

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer50.detach", exc_info=True)
        mp = _get(self.bc, "mempool")
        try:
            if getattr(mp, "_g50_observer", None) == self.observe_submit:
                del mp._g50_observer
        except Exception:                                            # noqa: BLE001
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer50.detach", exc_info=True)
        self._attached = False

    # ================================================================== PUBLIC API (all guarded)
    # ---- reporting
    def status(self) -> dict:
        with self._lock:
            return {
                "attached": self._attached, "errors": self.errors,
                "blocks_seen": self.blocks_seen, "reorgs_seen": self.reorgs_seen,
                "last_height": self.last_height,
                "mempool_seen": self.mempool_seen, "mempool_accepted": self.mempool_accepted,
                "components": dict(self.status_map), "notes": list(self.notes),
                "recent_errors": list(self.error_log),
                "flags": {
                    "allow_identity_writes": self.cfg.allow_identity_writes,
                    "allow_relay": self.cfg.allow_relay,
                    "run_keeper_actions": self.cfg.run_keeper_actions,
                    "market_admins": len(self.cfg.market_admins),
                },
            }

    def stats(self) -> dict:
        """Read-only statistics of every connected component (JSON serialisable)."""
        out: Dict[str, Any] = {}
        calls = {
            "epoch_system": "epoch_stats", "identity_hub": "hub_stats", "dex_v2": "dex_v2_stats",
            "validator_select": "selection_stats", "xswap": "swap_stats",
            "delegation": "delegation_stats", "relay": "relay_stats", "keeper": "keeper_stats",
            "community": "community_stats", "reward_schedule": "reward_breakdown",
            "orderbook": "best_prices",
        }
        for name, method in calls.items():
            comp = self.components.get(name)
            if comp is None:
                continue
            try:
                out[name] = getattr(comp, method)()
            except Exception as e:                                   # noqa: BLE001
                self._fail(f"stats:{name}", e)
                out[name] = {"error": f"{type(e).__name__}: {e}"}
        out["state_channels"] = len(self.channels)
        out["prediction_markets"] = len(self.markets)
        out["vaults"] = len(self.vaults)
        out["holder_snapshot"] = self.last_holder_snapshot
        return json.loads(json.dumps(out, default=str))

    # ---- identity
    @_safe
    def identity_profile(self, address: str):
        hub = self._need("identity_hub")
        _addr(address)
        if address not in hub._hub_profiles and len(hub._hub_profiles) >= self.cfg.max_profiles:
            raise _Rejected("profile limit reached")
        return hub.full_identity(address)

    @_safe
    def set_kyc(self, address: str, kyc_level: int, evidence: str):
        if not self.cfg.allow_identity_writes:
            raise _Rejected("identity writes are disabled (Group50Config.allow_identity_writes)")
        hub = self._need("identity_hub")
        _addr(address)
        if not isinstance(kyc_level, int) or isinstance(kyc_level, bool) or not 0 <= kyc_level <= 5:
            raise _Rejected("kyc_level must be an integer 0-5")
        if not isinstance(evidence, str) or not evidence:
            raise _Rejected("evidence is required")
        return hub.verify_identity(address, kyc_level, evidence[:256])

    # ---- DEX v2
    @_safe
    def dex_create_pool(self, token_a: str, token_b: str, fee_tier: float = 0.003):
        dex = self._need("dex_v2")
        _ident(token_a, "token_a"); _ident(token_b, "token_b")
        if token_a == token_b:
            raise _Rejected("tokens must differ")
        if not _is_num(fee_tier) or not 0 < fee_tier < 0.1:
            raise _Rejected("fee_tier must be between 0 and 0.1")
        return dex.create_pool(token_a, token_b, fee_tier)

    @_safe
    def dex_add_liquidity(self, pool_id: str, lp: str, tick_lower: int, tick_upper: int,
                          liquidity: float):
        dex = self._need("dex_v2")
        _ident(pool_id, "pool_id"); _addr(lp, "lp")
        if not (isinstance(tick_lower, int) and isinstance(tick_upper, int)) \
                or tick_lower >= tick_upper:
            raise _Rejected("ticks must be integers with tick_lower < tick_upper")
        _pos_num(liquidity, "liquidity")
        return dex.add_liquidity(pool_id, lp, tick_lower, tick_upper, liquidity)

    @_safe
    def dex_swap(self, pool_id: str, trader: str, token_in: str, amount_in: float):
        dex = self._need("dex_v2")
        _ident(pool_id, "pool_id"); _addr(trader, "trader"); _ident(token_in, "token_in")
        _pos_num(amount_in, "amount_in")
        return dex.swap(pool_id, trader, token_in, amount_in)

    # ---- order book aggregator (read only)
    @_safe
    def orderbook_pairs(self):
        return self._need("orderbook").all_pairs()

    @_safe
    def orderbook_best_prices(self):
        return self._need("orderbook").best_prices()

    @_safe
    def orderbook_liquidity(self, pair: str, depth: int = 10):
        _ident(pair, "pair"); _pos_int(depth, "depth")
        return self._need("orderbook").aggregate_liquidity(pair, min(depth, 100))

    # ---- fees
    @_safe
    def fee_suggest(self, confirm_in_blocks: int = 6):
        _pos_int(confirm_in_blocks, "confirm_in_blocks")
        return self._need("fee_optimizer").suggested_fee(confirm_in_blocks)

    @_safe
    def fee_batch_estimate(self, tx_sizes: List[int], confirm_in: int = 6):
        if not isinstance(tx_sizes, list) or not 1 <= len(tx_sizes) <= 1000:
            raise _Rejected("tx_sizes must be a list of 1-1000 sizes")
        for s in tx_sizes:
            _pos_int(s, "tx size")
        _pos_int(confirm_in, "confirm_in")
        return self._need("fee_optimizer").batch_fee_estimate(tx_sizes, confirm_in)

    @_safe
    def fee_rbf_bump(self, current_fee: int, bump_pct: float = 1.25):
        _pos_int(current_fee, "current_fee")
        if not _is_num(bump_pct) or not 1.0 < bump_pct <= 10:
            raise _Rejected("bump_pct must be in (1, 10]")
        return self._need("fee_optimizer").rbf_bump(current_fee, bump_pct)

    @_safe
    def fee_tips(self):
        return self._need("fee_optimizer").fee_savings_tips()

    # ---- reward schedule
    @_safe
    def reward_breakdown(self, height: Optional[int] = None):
        if height is not None and (not isinstance(height, int) or isinstance(height, bool)
                                   or height < 0):
            raise _Rejected("height must be a non-negative integer")
        return self._need("reward_schedule").reward_breakdown(height)

    @_safe
    def reward_cumulative(self, from_h: int = 0, to_h: Optional[int] = None):
        for v in (from_h, to_h):
            if v is not None and (not isinstance(v, int) or isinstance(v, bool) or v < 0):
                raise _Rejected("heights must be non-negative integers")
        return self._need("reward_schedule").cumulative_rewards(from_h, to_h)

    @_safe
    def reward_future(self, years: int = 10):
        _pos_int(years, "years")
        if years > 100:
            raise _Rejected("years must be <= 100")
        return self._need("reward_schedule").future_rewards(years)

    # ---- validator selection (report only)
    @_safe
    def select_proposer(self, height: int):
        _nonneg_int(height, "height")
        return self._need("validator_select").select_proposer(height)

    @_safe
    def select_committee(self, height: int, size: int = 21):
        _nonneg_int(height, "height"); _pos_int(size, "size")
        return self._need("validator_select").select_committee(height, min(size, 1000))

    # ---- cross-chain swap
    @_safe
    def xswap_initiate(self, initiator: str, participant: str, chain_a: str, amount_a: float,
                       chain_b: str, amount_b: float):
        x = self._need("xswap")
        _addr(initiator, "initiator"); _addr(participant, "participant")
        _ident(chain_a, "chain_a"); _ident(chain_b, "chain_b")
        _pos_num(amount_a, "amount_a"); _pos_num(amount_b, "amount_b")
        if len(x._swaps) >= self.cfg.max_records * 10:
            raise _Rejected("swap registry is full")
        return True, x.initiate(initiator, participant, chain_a, amount_a, chain_b, amount_b)

    @_safe
    def xswap_complete(self, swap_id: str, preimage_hex: str):
        x = self._need("xswap")
        _ident(swap_id, "swap_id")
        try:
            bytes.fromhex(preimage_hex)
        except (ValueError, TypeError):
            raise _Rejected("preimage must be a hex string")
        return x.reveal_and_complete(swap_id, preimage_hex)

    @_safe
    def xswap_refund(self, swap_id: str, initiator: str):
        _ident(swap_id, "swap_id"); _addr(initiator, "initiator")
        return self._need("xswap").refund(swap_id, initiator)

    # ---- portfolio rebalancer
    @_safe
    def portfolio_set_target(self, owner: str, targets: Dict[str, float],
                             rebalance_threshold: float = 0.05):
        pr = self._need("rebalancer")
        _addr(owner, "owner")
        t = _weights(targets)
        if not _is_num(rebalance_threshold) or not 0 < rebalance_threshold < 1:
            raise _Rejected("rebalance_threshold must be in (0, 1)")
        pr.set_target(owner, t, rebalance_threshold)
        return True, "target stored"

    @staticmethod
    def _holdings(current: Any) -> Dict[str, float]:
        if not isinstance(current, dict) or not 1 <= len(current) <= 64:
            raise _Rejected("current must be a dict with 1-64 entries")
        for k, v in current.items():
            _ident(k, "asset")
            if not _is_num(v) or v < 0:
                raise _Rejected(f"current['{k}'] must be a non-negative finite number")
        return current

    @_safe
    def portfolio_drift(self, owner: str, current: Dict[str, float]):
        _addr(owner, "owner")
        return self._need("rebalancer").check_drift(owner, self._holdings(current))

    @_safe
    def portfolio_plan(self, owner: str, current: Dict[str, float]):
        _addr(owner, "owner")
        return self._need("rebalancer").rebalance_plan(owner, self._holdings(current))

    # ---- analytics (read only)
    @_safe
    def analytics_whales(self, min_nbl: float = 10_000):
        return self._need("analytics").whale_movements(_pos_num(min_nbl, "min_nbl"))

    @_safe
    def analytics_holders(self):
        snap = self._need("analytics").holder_distribution_snapshot()
        self.last_holder_snapshot = snap
        return snap

    @_safe
    def analytics_flow(self):
        return self._need("analytics").exchange_flow()

    # ---- delegated staking
    def _delegated_by(self, ds: Any, delegator: str) -> int:
        return sum(d.get(delegator, 0) for d in ds._delegations.values())

    @_safe
    def delegate(self, delegator: str, validator: str, amount: int):
        ds = self._need("delegation")
        _addr(delegator, "delegator"); _addr(validator, "validator"); _pos_int(amount, "amount")
        bal = self.bc.utxo.balance(delegator)
        if bal < self._delegated_by(ds, delegator) + amount:
            return False, "Insufficient balance (counting existing delegations)"
        return ds.delegate(delegator, validator, amount)

    @_safe
    def undelegate(self, delegator: str, validator: str, amount: Optional[int] = None):
        ds = self._need("delegation")
        _addr(delegator, "delegator"); _addr(validator, "validator")
        if amount is not None:
            _pos_int(amount, "amount")
        return ds.undelegate(delegator, validator, amount)

    @_safe
    def delegation_total(self, validator: str):
        return self._need("delegation").total_delegated(_addr(validator, "validator"))

    @_safe
    def delegation_info(self, delegator: str):
        return self._need("delegation").delegator_info(_addr(delegator, "delegator"))

    # ---- launchpad
    @_safe
    def create_ido(self, creator: str, token_symbol: str, total_raise: float, hard_cap: float,
                   price_per_token: float, min_buy: float, max_buy: float, start_block: int,
                   duration_blocks: int, vesting_days: int = 90):
        lp = self._need("launchpad")
        _addr(creator, "creator"); _ident(token_symbol, "token_symbol")
        _pos_num(total_raise, "total_raise"); _pos_num(hard_cap, "hard_cap")
        _pos_num(price_per_token, "price_per_token")
        _pos_num(min_buy, "min_buy"); _pos_num(max_buy, "max_buy")
        if min_buy > max_buy:
            raise _Rejected("min_buy must be <= max_buy")
        if hard_cap < total_raise:
            raise _Rejected("hard_cap must be >= total_raise")
        if not isinstance(start_block, int) or isinstance(start_block, bool) or start_block < 0:
            raise _Rejected("start_block must be a non-negative integer")
        _pos_int(duration_blocks, "duration_blocks")
        if not isinstance(vesting_days, int) or isinstance(vesting_days, bool) or vesting_days < 0:
            raise _Rejected("vesting_days must be a non-negative integer")
        if len(lp._idos) >= self.cfg.max_records:
            raise _Rejected("IDO registry is full")
        params = g.IDOParameters(token_symbol, total_raise, hard_cap, price_per_token, min_buy,
                                 max_buy, start_block, duration_blocks, vesting_days)
        return True, lp.create_ido(creator, params)

    @_safe
    def ido_participate(self, ido_id: str, participant: str, amount_nbl: float):
        _ident(ido_id, "ido_id"); _addr(participant, "participant")
        return self._need("launchpad").participate(ido_id, participant,
                                                   _pos_num(amount_nbl, "amount_nbl"))

    @_safe
    def ido_info(self, ido_id: str):
        info = self._need("launchpad").ido_info(_ident(ido_id, "ido_id"))
        return (True, info) if info is not None else (False, "IDO not found")

    # ---- gasless relay (gated)
    @_safe
    def relay_sponsor(self, dapp: str, budget_nbl: float):
        if not self.cfg.allow_relay:
            raise _Rejected("relay is disabled (Group50Config.allow_relay)")
        ok = self._need("relay").sponsor(_addr(dapp, "dapp"), _pos_num(budget_nbl, "budget_nbl"))
        return (True, "sponsored") if ok else (False, "dApp balance too low")

    @_safe
    def relay_transaction(self, user: str, dapp: str, tx: Any):
        if not self.cfg.allow_relay:
            raise _Rejected("relay is disabled (Group50Config.allow_relay)")
        _addr(user, "user"); _addr(dapp, "dapp")
        if tx is None or not hasattr(tx, "byte_size") or not hasattr(tx, "txid"):
            raise _Rejected("tx must provide byte_size() and txid")
        return self._need("relay").relay_for(user, dapp, tx)

    # ---- keeper (gated)
    @_safe
    def run_keeper_once(self):
        if not self.cfg.run_keeper_actions:
            raise _Rejected("keeper actions are disabled (Group50Config.run_keeper_actions)")
        if not self.cfg.keeper_address:
            raise _Rejected("keeper_address is not configured")
        keeper = self._need("keeper")
        liq = self.services.get("liquidation_engine")
        res = {"liquidations": 0, "distributions": 0, "oracle_updates": 0}
        if liq is not None:
            res["liquidations"] = keeper.run_liquidations(liq)
        rd = self.services.get("rewards_distributor")
        if rd is not None:
            res["distributions"] = keeper.run_reward_distributions(rd)
        orc = self.services.get("oracle")
        if orc is not None:
            res["oracle_updates"] = keeper.run_oracle_updates(orc)
        return res

    # ---- dev tools (needs chain dev mode; never enabled by this layer)
    @_safe
    def dev_inspect_address(self, address: str):
        return self._need("dev_tools").inspect_address(_addr(address))

    @_safe
    def dev_sdk_snippet(self, task: str):
        return self._need("dev_tools").sdk_snippet(_ident(task, "task"))

    @_safe
    def dev_create_test_wallet(self, fund_nbl: float = 1000):
        return self._need("dev_tools").create_test_wallet(_pos_num(fund_nbl, "fund_nbl"))

    # ---- community
    @_safe
    def community_register_ambassador(self, address: str, name: str, region: str,
                                      handles: Optional[dict] = None):
        hub = self._need("community")
        _addr(address); _ident(name, "name"); _ident(region, "region")
        if handles is not None and not isinstance(handles, dict):
            raise _Rejected("handles must be a dict")
        if len(hub._ambassadors) >= self.cfg.max_records * 10:
            raise _Rejected("ambassador registry is full")
        created = hub.register_ambassador(address, name, region, handles)
        return (True, "registered") if created else (False, "address is already registered")

    @_safe
    def community_add_event(self, title: str, event_type: str, date: str, organizer: str,
                            description: str = ""):
        hub = self._need("community")
        _ident(title, "title"); _ident(event_type, "event_type"); _ident(date, "date")
        _addr(organizer, "organizer")
        if len(hub._events) >= self.cfg.max_records:
            raise _Rejected("event list is full")
        return True, hub.add_event(title, event_type, date, organizer, str(description)[:500])

    @_safe
    def community_feedback(self, author: str, category: str, message: str):
        hub = self._need("community")
        _addr(author, "author"); _ident(category, "category")
        if not isinstance(message, str) or not message.strip():
            raise _Rejected("message must be a non-empty string")
        if len(hub._feedback) >= self.cfg.max_records:
            del hub._feedback[0]
        return True, hub.submit_feedback(author, category, message)

    # ---- state channels (registry of StateChannelV2)
    @staticmethod
    def _channel_id(alice: str, bob: str, nonce: int) -> str:
        return f"ch{nonce}:{alice[:8]}:{bob[:8]}"

    @_safe
    def channel_open(self, alice: str, bob: str, capacity: int):
        _addr(alice, "alice"); _addr(bob, "bob"); _pos_int(capacity, "capacity")
        if alice == bob:
            raise _Rejected("alice and bob must differ")
        with self._lock:
            if len(self.channels) >= self.cfg.max_channels:
                raise _Rejected("channel registry is full")
            if self.bc.utxo.balance(alice) < capacity:
                raise _Rejected("alice cannot fund this capacity")
            cid = self._channel_id(alice, bob, len(self.channels) + 1)
            self.channels[cid] = g.StateChannelV2(alice, bob, capacity, self.bc)
        return True, cid

    def _channel(self, channel_id: str) -> Any:
        ch = self.channels.get(_ident(channel_id, "channel_id"))
        if ch is None:
            raise _Rejected("channel not found")
        return ch

    @_safe
    def channel_pay(self, channel_id: str, payer: str, amount: int):
        ch = self._channel(channel_id)
        _pos_int(amount, "amount")
        if payer not in (ch.alice, ch.bob):
            raise _Rejected("payer is not a channel participant")
        return ch.pay(payer, amount)

    @_safe
    def channel_add_htlc(self, channel_id: str, payer: str, amount: int, hash_lock: str,
                         timeout: int):
        ch = self._channel(channel_id)
        _pos_int(amount, "amount"); _pos_int(timeout, "timeout")
        if payer not in (ch.alice, ch.bob):
            raise _Rejected("payer is not a channel participant")
        if not isinstance(hash_lock, str) or len(hash_lock) != 64:
            raise _Rejected("hash_lock must be a 64-char sha256 hex string")
        if len(ch.htlcs) >= self.cfg.max_records:
            raise _Rejected("too many HTLCs on this channel")
        return True, ch.add_htlc(payer, amount, hash_lock, timeout)

    @_safe
    def channel_settle_htlc(self, channel_id: str, htlc_id: str, preimage: str):
        ch = self._channel(channel_id)
        ok = ch.settle_htlc(_ident(htlc_id, "htlc_id"), str(preimage))
        return (True, "settled") if ok else (False, "HTLC not settled")

    @_safe
    def channel_close(self, channel_id: str):
        return True, self._channel(channel_id).close()

    @_safe
    def channel_info(self, channel_id: str):
        return True, self._channel(channel_id).channel_info()

    # ---- prediction markets (registry of PredictionMarketV2)
    @_safe
    def market_create(self, market_id: str, question: str, outcomes: List[str]):
        _ident(market_id, "market_id")
        if not isinstance(question, str) or not (0 < len(question) <= 500):
            raise _Rejected("question must be a string of 1-500 characters")
        if not isinstance(outcomes, list) or not 2 <= len(outcomes) <= 16:
            raise _Rejected("outcomes must be a list of 2-16 names")
        for o in outcomes:
            _ident(o, "outcome")
        if len(set(outcomes)) != len(outcomes):
            raise _Rejected("outcomes must be unique")
        with self._lock:
            if market_id in self.markets:
                raise _Rejected("market already exists")
            if len(self.markets) >= self.cfg.max_markets:
                raise _Rejected("market registry is full")
            self.markets[market_id] = g.PredictionMarketV2(market_id, question,
                                                           list(outcomes), self.bc)
        return True, market_id

    def _market(self, market_id: str) -> Any:
        m = self.markets.get(_ident(market_id, "market_id"))
        if m is None:
            raise _Rejected("market not found")
        return m

    @_safe
    def market_buy(self, market_id: str, trader: str, outcome: str, amount: int):
        m = self._market(market_id)
        _addr(trader, "trader"); _ident(outcome, "outcome"); _pos_int(amount, "amount")
        if m.resolved:
            raise _Rejected("market already resolved")
        return m.buy_shares(trader, outcome, amount)

    @_safe
    def market_price(self, market_id: str, outcome: str):
        m = self._market(market_id)
        if outcome not in m.outcomes:
            raise _Rejected("unknown outcome")
        return m.get_price(outcome)

    @_safe
    def market_resolve(self, market_id: str, caller: str, winning_outcome: str):
        m = self._market(market_id)
        if caller not in self.cfg.market_admins:
            raise _Rejected("caller is not in Group50Config.market_admins")
        if m.resolved:
            raise _Rejected("market already resolved")
        ok = m.resolve(winning_outcome)
        return (True, "resolved") if ok else (False, "unknown outcome")

    @_safe
    def market_claim(self, market_id: str, trader: str):
        return self._market(market_id).claim_winnings(_addr(trader, "trader"))

    @_safe
    def market_info(self, market_id: str):
        return True, self._market(market_id).market_info()

    # ---- auto-rebalancing vaults (registry of AutoRebalancingVault)
    @_safe
    def vault_create(self, vault_id: str, targets: Dict[str, float]):
        _ident(vault_id, "vault_id")
        t = _weights(targets)
        with self._lock:
            if vault_id in self.vaults:
                raise _Rejected("vault already exists")
            if len(self.vaults) >= self.cfg.max_vaults:
                raise _Rejected("vault registry is full")
            self.vaults[vault_id] = g.AutoRebalancingVault(vault_id, t, self.bc,
                                                           self.services.get("oracle"))
        return True, vault_id

    def _vault(self, vault_id: str) -> Any:
        v = self.vaults.get(_ident(vault_id, "vault_id"))
        if v is None:
            raise _Rejected("vault not found")
        return v

    @_safe
    def vault_deposit(self, vault_id: str, asset: str, amount: float):
        v = self._vault(vault_id)
        _ident(asset, "asset"); _pos_num(amount, "amount")
        ok = v.deposit(asset, amount)
        return (True, "deposited") if ok else (False, "asset is not part of the vault targets")

    @_safe
    def vault_rebalance(self, vault_id: str):
        return True, self._vault(vault_id).rebalance()

    @_safe
    def vault_info(self, vault_id: str):
        return True, self._vault(vault_id).vault_info()


# ----------------------------------------------------------------------------------------------
# install / uninstall / attach  (same pattern as group 5)
# ----------------------------------------------------------------------------------------------
_LAYERS: "weakref.WeakSet[Layer50]" = weakref.WeakSet()
_DEFAULT_CONFIG: Dict[str, Group50Config] = {}


def is_installed(host: Any) -> bool:
    cls = getattr(host, "NEBULAFullNode", None)
    return bool(cls is not None and getattr(cls, "_g50_orig", None))


def attach(node: Any, host: Any = None, config: Optional[Group50Config] = None) -> Layer50:
    """Create a layer for an EXISTING node and register it as a chain listener."""
    layer = Layer50(node, host, config)
    layer.attach()
    _LAYERS.add(layer)
    node.group50 = layer
    return layer


def _patch_mempool(host: Any) -> None:
    cls = getattr(host, "Mempool", None)
    if cls is None or not hasattr(cls, "submit") or getattr(cls, "_g50_submit_orig", None):
        return
    orig = cls.submit

    @functools.wraps(orig)
    def submit(self, *a, **k):
        result = orig(self, *a, **k)            # original ALWAYS runs first, result unchanged
        obs = getattr(self, "_g50_observer", None)
        if obs is not None and a:
            try:
                obs(a[0], result)
            except Exception:                   # noqa: BLE001 - observer must never affect submit
                _NB_SWALLOW_LOG.debug("swallowed Exception in _patch_mempool.submit", exc_info=True)
        return result

    cls._g50_submit_orig = orig
    cls.submit = submit


def install(host: Any, config: Optional[Group50Config] = None) -> None:
    """Patch ``host.NEBULAFullNode.__init__`` so every new node gets ``node.group50``."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g50_orig", None):
        return
    cfg = config or Group50Config()
    _DEFAULT_CONFIG["cfg"] = cfg
    orig = cls.__init__

    @functools.wraps(orig)
    def patched(self, *a, **k):
        orig(self, *a, **k)                      # the node must come up exactly as before
        try:
            layer = Layer50(self, host, _DEFAULT_CONFIG.get("cfg"))
            layer.attach()
            _LAYERS.add(layer)
            self.group50 = layer
        except Exception as e:                   # noqa: BLE001
            self.group50_error = e               # node still starts

    cls._g50_orig = orig
    cls.__init__ = patched
    if cfg.track_mempool:
        _patch_mempool(host)


def uninstall(host: Any) -> None:
    """Restore the host exactly as it was and detach every layer."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g50_orig", None)
    if orig:
        cls.__init__ = orig
        del cls._g50_orig
    mp = getattr(host, "Mempool", None)
    mp_orig = getattr(mp, "_g50_submit_orig", None) if mp is not None else None
    if mp_orig:
        mp.submit = mp_orig
        del mp._g50_submit_orig
    for layer in list(_LAYERS):
        layer.detach()
    _LAYERS.clear()
    _DEFAULT_CONFIG.clear()
