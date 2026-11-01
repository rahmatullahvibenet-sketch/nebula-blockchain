"""nebula_group58_install.py - wires the 20 group58 classes into a NEBULA node.

Design rules (taken from nebula_group58_guide.txt):
  * nebula_v10_11.py (the host) is NEVER edited.  Everything happens by wrapping
    NEBULAFullNode.__init__ (install / uninstall), exactly like group 5.
  * The layer is OBSERVE-ONLY on day one: it counts blocks and reorgs, never
    rejects a block or a transaction, never mines, never changes consensus.
  * Every callback is wrapped in try/except; failures are counted in
    `layer.errors` and the node always keeps running.
  * Coin-minting classes (testnet faucet, NFT gaming platform) are built ONLY
    when the chain is in dev mode (bc._dev_mode) or NEBULA_ALLOW_DEV_MODE=1.
    On a real chain they are skipped with a clear reason (see `layer.skipped`).

Usage:
    import nebula_v10_11 as host
    import nebula_group58_install as g58
    g58.install(host)            # before the node is created
    node = host.NEBULAFullNode(...)
    node.group58.stats()         # observe
    g58.uninstall(host)          # back to the original behaviour
"""
from __future__ import annotations

import functools
import inspect
import logging
import os
import threading
import time
from collections import deque
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group58 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group58")

# --------------------------------------------------------------------------
# Configuration (all values are defaults; pass `config={...}` to install())
# --------------------------------------------------------------------------
DEFAULT_CONFIG: Dict[str, Any] = {
    # Pair used for the dynamic-fee pool (and the range-order book on top of it).
    "pool_token_a": "NBL",
    "pool_token_b": "NUSD",
    "pool_base_fee_bps": 30,
    # Names under which the host node may already hold an RNG / NFT registry.
    "rng_attrs": ("rng", "onchain_rng", "on_chain_rng"),
    "nft_attrs": ("nft", "nft_registry", "nbl721", "nbl721_registry"),
    # Host class names used when the node does not hold them already.
    "rng_class": "OnChainRNG",
    "nft_class": "NBL721Registry",
    # Memory cap: how many recent block heights the layer remembers.
    "recent_heights_cap": 1000,
    # Prefix of the read-only REST endpoints.
    "api_prefix": "/api/group58",
}

# Order = guide Step 4 (classes that need nothing first, dependents later).
BUILD_ORDER: Tuple[str, ...] = (
    "partnership", "grants", "ambassadors", "hackathons", "ecosystem_fund",
    "rust_bridge", "testnet", "faucet_api", "community", "security_audit",
    "bug_bounty", "fee_pool", "range_orders", "mev_auction", "amm_v3",
    "rollup", "dungeon", "gaming",
)
# GameCharacter (17) and SocialToken (20) are per-instance classes (one object
# per hero / per creator), so the layer exposes factories for them instead of a
# single shared instance: make_character() and make_social_token().

MINTING = ("testnet", "faucet_api", "gaming")   # these can create coins


def _mint_allowed(bc: Any) -> bool:
    """True only on throw-away chains (same rule as host _enable_dev_mode)."""
    return bool(getattr(bc, "_dev_mode", False)) or \
        os.environ.get("NEBULA_ALLOW_DEV_MODE") == "1"


def _construct(cls: Any, bc: Any) -> Any:
    """Build a host helper class when it needs no args or only the chain."""
    params = [p for p in inspect.signature(cls).parameters.values()
              if p.default is inspect.Parameter.empty
              and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
    if not params:
        return cls()
    if len(params) == 1 and params[0].name in ("bc", "blockchain", "chain"):
        return cls(bc)
    raise TypeError(
        f"{getattr(cls, '__name__', cls)} needs "
        f"{[p.name for p in params]}; attach it to the node by hand")


class Layer58:
    """Holds one instance of every group58 service and listens to the chain."""

    def __init__(self, node: Any, host: Any = None,
                 config: Optional[dict] = None):
        self.node = node
        self.host = host
        self.cfg = {**DEFAULT_CONFIG, **(config or {})}
        self.bc = getattr(node, "bc", None)
        self._lock = threading.RLock()

        self.errors = 0
        self.last_error: Optional[str] = None
        self.built: List[str] = []
        self.skipped: Dict[str, str] = {}
        self.blocks_seen = 0
        self.reorgs = 0
        self.last_height: Optional[int] = None
        self.recent_heights: deque = deque(maxlen=self.cfg["recent_heights_cap"])
        self.started_at = time.time()
        self.attached = False
        self.mint_allowed = _mint_allowed(self.bc)

        self.social_tokens: Dict[str, Any] = {}
        self.characters: Dict[str, Any] = {}
        self._security_cache: Optional[dict] = None
        self._rng = None
        self._nft = None

        self._build_all()

    # ------------------------------------------------------------------ build
    def _record_error(self, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.last_error = f"{where}: {type(exc).__name__}: {exc}"
        log.warning("group58 %s failed: %s", where, exc)

    def _need(self, name: str, *deps: str) -> None:
        for d in deps:
            if getattr(self, d, None) is None:
                raise LookupError(f"needs '{d}' which is not available")
        if name in MINTING and not self.mint_allowed:
            raise PermissionError(
                "can mint coins; chain is not in dev mode "
                "(set bc._dev_mode or NEBULA_ALLOW_DEV_MODE=1 on a test chain)")

    def _make(self, name: str, factory: Callable[[], Any],
              deps: Tuple[str, ...] = ()) -> None:
        setattr(self, name, None)
        try:
            self._need(name, *deps)
            setattr(self, name, factory())
            self.built.append(name)
        except (PermissionError, LookupError) as e:      # expected skips
            self.skipped[name] = str(e)
        except Exception as e:                           # real faults
            self.skipped[name] = f"error: {type(e).__name__}: {e}"
            self._record_error(f"build {name}", e)

    def _resolve_helper(self, attrs: Tuple[str, ...], cls_name: str) -> Any:
        for a in attrs:                                  # 1) node already has it
            v = getattr(self.node, a, None)
            if v is not None:
                return v
        cls = getattr(self.host, cls_name, None) or getattr(g, cls_name, None)
        if cls is None:
            return None
        return _construct(cls, self.bc)                  # 2) build a fresh one

    def _build_all(self) -> None:
        bc, cfg = self.bc, self.cfg
        if bc is None:
            self.skipped["*"] = "node has no .bc (blockchain) attribute"
            return

        # helpers needed by the game classes (never fatal)
        try:
            self._rng = self._resolve_helper(cfg["rng_attrs"], cfg["rng_class"])
        except Exception as e:
            self.skipped["_rng"] = f"{type(e).__name__}: {e}"
        try:
            self._nft = self._resolve_helper(cfg["nft_attrs"], cfg["nft_class"])
        except Exception as e:
            self.skipped["_nft"] = f"{type(e).__name__}: {e}"

        m = self._make
        m("partnership",    lambda: g.NEBULAPartnership())
        m("grants",         lambda: g.NEBULAGrantsProgram())
        m("ambassadors",    lambda: g.NEBULAAmbassadorProgram())
        m("hackathons",     lambda: g.NEBULAHackathonHistory())
        m("ecosystem_fund", lambda: g.NEBULAEcosystemFund(bc))
        m("rust_bridge",    lambda: g.RustBridge())
        m("testnet",        lambda: g.NEBULATestnet(bc))
        m("faucet_api",     lambda: g.TestnetFaucetAPI(self.testnet, bc),
          deps=("testnet",))
        m("community",      lambda: g.NEBULACommunityPlatform(bc))
        m("security_audit", lambda: g.SecurityAuditReport(bc))
        m("bug_bounty",     lambda: g.BugBountyProgram())
        m("fee_pool",       lambda: g.DynamicFeePool(
            cfg["pool_token_a"], cfg["pool_token_b"], cfg["pool_base_fee_bps"]))
        m("range_orders",   lambda: g.RangeOrderBook(self.fee_pool),
          deps=("fee_pool",))
        m("mev_auction",    lambda: g.MEVAuction(bc))
        m("amm_v3",         lambda: g.AutomatedMarketMakerV3(bc))
        m("rollup",         lambda: g.OptimisticRollup(bc))
        m("dungeon",        lambda: g.Dungeon(self._rng, bc), deps=("_rng",))
        m("gaming",         lambda: g.NFTGamingPlatform(bc, self._nft, self._rng),
          deps=("_rng", "_nft"))

    # ------------------------------------------------------------ factories
    def make_character(self, char_id: str, owner: str, name: str,
                       char_class: str, race: str) -> Any:
        """GameCharacter (class 17) - one object per hero."""
        ch = g.GameCharacter(char_id, owner, name, char_class, race)
        with self._lock:
            self.characters[char_id] = ch
        return ch

    def make_social_token(self, creator: str, symbol: str, name: str,
                          total_supply: int) -> Any:
        """SocialToken (class 20) - one object per creator token."""
        tok = g.SocialToken(creator, symbol, name, total_supply, self.bc)
        with self._lock:
            self.social_tokens[symbol] = tok
        return tok

    # ----------------------------------------------- chain listener (observe)
    def on_connect(self, block: Any) -> None:
        try:
            h = getattr(block, "height", None)
            if h is None and isinstance(block, dict):
                h = block.get("height")
            if h is None:
                h = getattr(self.bc, "height", None)
            with self._lock:
                self.blocks_seen += 1
                self.last_height = h
                self.recent_heights.append(h)
        except Exception as e:
            self._record_error("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        try:
            with self._lock:
                self.reorgs += 1
        except Exception as e:
            self._record_error("on_reorg", e)

    def detach(self) -> None:
        try:
            self.node.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer58.detach", exc_info=True)
        self.attached = False

    # ---------------------------------------------------------------- stats
    def _safe(self, label: str, fn: Callable[[], Any]) -> Any:
        try:
            return fn()
        except Exception as e:
            self._record_error(f"stats {label}", e)
            return {"error": f"{type(e).__name__}: {e}"}

    def stats(self) -> dict:
        """Read-only summary of the layer and of every built service."""
        s = self._safe
        out: Dict[str, Any] = {
            "layer": {
                "built": list(self.built),
                "skipped": dict(self.skipped),
                "errors": self.errors,
                "last_error": self.last_error,
                "blocks_seen": self.blocks_seen,
                "reorgs": self.reorgs,
                "last_height": self.last_height,
                "mint_allowed": self.mint_allowed,
                "uptime_secs": int(time.time() - self.started_at),
            }
        }
        probes = {
            "partnership":    lambda: self.partnership.partnership_stats(),
            "grants":         lambda: self.grants.grants_stats(),
            "ambassadors":    lambda: self.ambassadors.program_stats(),
            "ecosystem_fund": lambda: self.ecosystem_fund.fund_stats(),
            "rust_bridge":    lambda: {"rust_available": self.rust_bridge.available},
            "testnet":        lambda: self.testnet.testnet_stats(),
            "bug_bounty":     lambda: self.bug_bounty.program_info(),
            "fee_pool":       lambda: self.fee_pool.pool_info(),
            "mev_auction":    lambda: self.mev_auction.mev_stats(),
            "amm_v3":         lambda: self.amm_v3.amm_v3_stats(),
            "rollup":         lambda: self.rollup.l2_stats(),
            "gaming":         lambda: self.gaming.gaming_stats(),
        }
        for name, fn in probes.items():
            if getattr(self, name, None) is not None:
                out[name] = s(name, fn)
        out["social_tokens"] = [t.token_info() for t in self.social_tokens.values()]
        return out

    def security_report(self) -> Optional[dict]:
        """Run the audit once, cache it (scan_all resets its own state)."""
        if self.security_audit is None:
            return None
        if self._security_cache is None:
            self._security_cache = self._safe(
                "security_audit", lambda: self.security_audit.scan_all())
        return self._security_cache


# --------------------------------------------------------------------------
# Read-only REST endpoints (GET only; nothing here can move coins)
# --------------------------------------------------------------------------
_LIVE: List[Layer58] = []
_LIVE_LOCK = threading.RLock()
_ROUTE_PATHS: List[str] = []


def _active() -> Optional[Layer58]:
    with _LIVE_LOCK:
        return _LIVE[-1] if _LIVE else None


def _json_ok(host: Any, data: Any):
    ok = getattr(host, "ok", None)
    if callable(ok):
        return ok(data)
    return 200, {"success": True, "data": data}


def _make_routes(host: Any, prefix: str) -> Dict[str, Callable]:
    def need_layer():
        return _active()

    def unavailable():
        return 503, {"success": False, "error": "group58 layer not active"}

    def stats(path, query, body):
        L = need_layer()
        return _json_ok(host, L.stats()) if L else unavailable()

    def ecosystem(path, query, body):
        L = need_layer()
        if not L:
            return unavailable()
        return _json_ok(host, {
            "partners":   L.partnership.partnership_stats() if L.partnership else None,
            "grants":     L.grants.grants_stats() if L.grants else None,
            "ambassadors": L.ambassadors.program_stats() if L.ambassadors else None,
            "hackathons": L.hackathons.get_history() if L.hackathons else None,
            "bug_bounty": L.bug_bounty.program_info() if L.bug_bounty else None,
        })

    def defi(path, query, body):
        L = need_layer()
        if not L:
            return unavailable()
        return _json_ok(host, {
            "fee_pool": L.fee_pool.pool_info() if L.fee_pool else None,
            "amm_v3":   L.amm_v3.amm_v3_stats() if L.amm_v3 else None,
            "mev":      L.mev_auction.mev_stats() if L.mev_auction else None,
            "rollup":   L.rollup.l2_stats() if L.rollup else None,
        })

    def gaming(path, query, body):
        L = need_layer()
        if not L:
            return unavailable()
        if L.gaming is None:
            return _json_ok(host, {"enabled": False,
                                   "reason": L.skipped.get("gaming", "not built")})
        return _json_ok(host, {"enabled": True, **L.gaming.gaming_stats()})

    def security(path, query, body):
        L = need_layer()
        if not L:
            return unavailable()
        rep = L.security_report()
        return _json_ok(host, rep) if rep is not None else \
            (404, {"success": False, "error": "security audit not built"})

    return {
        f"{prefix}/stats": stats, f"{prefix}/ecosystem": ecosystem,
        f"{prefix}/defi": defi, f"{prefix}/gaming": gaming,
        f"{prefix}/security": security,
    }


def _register_routes(host: Any, prefix: str) -> None:
    routes = _make_routes(host, prefix)
    table = getattr(host, "_routes", None)
    if table is None:
        return
    for path, fn in routes.items():
        table.setdefault("GET", {})[path] = fn
        _ROUTE_PATHS.append(path)


def _unregister_routes(host: Any) -> None:
    table = getattr(host, "_routes", None) or {}
    for path in _ROUTE_PATHS:
        table.get("GET", {}).pop(path, None)
    _ROUTE_PATHS.clear()


# --------------------------------------------------------------------------
# install / uninstall  (wrapper around NEBULAFullNode.__init__)
# --------------------------------------------------------------------------
def install(host: Any, config: Optional[dict] = None) -> None:
    cls = host.NEBULAFullNode
    if getattr(cls, "_g58_orig", None):
        return                                           # already installed
    cfg = {**DEFAULT_CONFIG, **(config or {})}
    orig = cls.__init__

    @functools.wraps(orig)
    def patched(self, *a, **k):
        orig(self, *a, **k)                              # original runs first
        try:
            layer = Layer58(self, host=host, config=cfg)
            self.group58 = layer
            self.bc.add_listener(layer)
            layer.attached = True
            with _LIVE_LOCK:
                _LIVE.append(layer)
        except Exception as e:                           # node must still start
            self.group58_error = e
            log.warning("group58 install failed: %s", e)

    cls._g58_orig = orig
    cls.__init__ = patched
    _register_routes(host, cfg["api_prefix"])


def uninstall(host: Any) -> None:
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g58_orig", None)
    if not orig:
        return
    cls.__init__ = orig
    del cls._g58_orig
    with _LIVE_LOCK:
        layers = list(_LIVE)
        _LIVE.clear()
    for layer in layers:
        layer.detach()
    _unregister_routes(host)
