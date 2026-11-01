"""nebula_group29_install.py - wiring layer for NEBULA group29 (20 classes).

Design rules (taken from nebula_group29_guide.txt):
  * nothing in nebula_v10_11.py is edited; everything is attached by wrappers
  * the layer NEVER rejects a block / tx / message: every callback is guarded,
    failures are counted in layer.errors and the host carries on
  * the original host method always runs first, its result is returned untouched
  * report-only for consensus-sensitive classes (ConsensusManager, DifficultyCLI)
  * anything with a thread or a socket (MarketMakerBot, BlockExplorerV2) is OFF
    until the caller starts it explicitly

Usage:
    import nebula_v10_11 as host
    import nebula_group29_install as inst
    inst.install(host)        # every NEBULAFullNode created afterwards gets node.group29
    ...
    inst.uninstall(host)      # host behaves exactly as before

How the 20 classes are used (see Layer29.registry() for the live table):
    chain listener : WhaleTracker (+WhaleAlert), NetworkHealthIndex,
                     DifficultyCLI, ConsensusManager (+ConsensusParams),
                     BlockExplorerV2 (+ExplorerV2Handler, opt-in)
    P2P observer   : LNChannelGraph, ExchangeFlowAnalyzer (on demand), counters
    security       : ZKRollupState, ZKProver, ZKRollupOperator (+RollupBatch)
    utility        : MarketMakerBot (+MMConfig, MMInventory), TxSimulator
                     (+SimulationResult)
    mempool hook   : LightningRouter lives next to the graph; the mempool hook
                     only counts accepted / rejected submissions
    REST (GET)     : /api/group29/* read-only endpoints
"""
from __future__ import annotations

import functools
import logging
import threading
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group29 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group29")

# --------------------------------------------------------------------------
# module level registry of live layers (used by the class level wrappers)
# --------------------------------------------------------------------------
_LAYERS: List["Layer29"] = []
_LAYERS_LOCK = threading.RLock()

ROUTE_PREFIX = "/api/group29"
ROUTE_NAMES = ("status", "whale", "health", "exchange_flows",
               "consensus", "difficulty", "zk", "ln")


def _live_layers() -> List["Layer29"]:
    with _LAYERS_LOCK:
        return list(_LAYERS)


def _msg_kind(msg: Any) -> str:
    """Best-effort message type name for counters (never raises)."""
    try:
        if isinstance(msg, dict):
            value = msg.get("type") or msg.get("command") or msg.get("cmd")
        else:
            value = (getattr(msg, "type", None) or getattr(msg, "command", None)
                     or getattr(msg, "cmd", None))
        if value is None:
            return type(msg).__name__
        return str(value)[:32]
    except Exception:
        return "unknown"


def _to_int(value: Any, default: int, lo: int, hi: int) -> int:
    try:
        return max(lo, min(hi, int(value)))
    except (TypeError, ValueError):
        return default


# ==========================================================================
# Layer29
# ==========================================================================
class Layer29:
    """One layer instance per node. Lives at node.group29."""

    WHALE_ALERT_CAP = 5000      # keep RAM bounded
    HEALTH_EVERY = 10           # blocks between NetworkHealthIndex samples
    DIFFICULTY_EVERY = 10       # blocks between difficulty comparisons
    ZK_CHECK_EVERY = 10         # blocks between ZK self checks
    P2P_KINDS_CAP = 64          # distinct message kinds tracked
    CACHE_SECONDS = 60.0        # cache for chain-scanning reports

    def __init__(self, node: Any):
        self.node = node
        self.bc = getattr(node, "bc", None)
        self._lock = threading.RLock()

        # error accounting - must stay 0 in a healthy run
        self.errors = 0
        self.last_error: Optional[str] = None
        self.component_status: Dict[str, str] = {}

        # counters
        self.counters: Dict[str, int] = {
            "blocks_seen": 0, "reorgs_seen": 0,
            "p2p_messages": 0,
            "mempool_ok": 0, "mempool_rejected": 0,
        }
        self.p2p_kinds: Dict[str, int] = {}
        self.last_reorg: Optional[Dict[str, Any]] = None
        self.last_health: Optional[dict] = None
        self.last_difficulty: Optional[dict] = None
        self.last_zk_check: Optional[dict] = None
        self._cache: Dict[str, Tuple[float, Any]] = {}

        # components (None when construction failed - see component_status)
        self.ln_graph: Optional[g.LNChannelGraph] = None
        self.ln_router: Optional[g.LightningRouter] = None
        self.whale: Optional[g.WhaleTracker] = None
        self.health: Optional[g.NetworkHealthIndex] = None
        self.flows: Optional[g.ExchangeFlowAnalyzer] = None
        self.zk_operator: Optional[g.ZKRollupOperator] = None
        self.zk_state: Optional[g.ZKRollupState] = None
        self.zk_prover: Optional[g.ZKProver] = None
        self.difficulty: Optional[g.DifficultyCLI] = None
        self.consensus: Optional[g.ConsensusManager] = None
        self.explorer: Optional[g.BlockExplorerV2] = None
        self.market_maker: Optional[g.MarketMakerBot] = None
        self._simulator: Optional[g.TxSimulator] = None

        self._attached = False
        self._build()

    # ------------------------------------------------------------------
    # error handling helper
    # ------------------------------------------------------------------
    def _fail(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.last_error = f"{where}: {type(exc).__name__}: {exc}"
        log.warning("group29 %s failed: %s", where, exc)

    def _safe(self, where: str, fn: Callable, *args, **kwargs) -> Any:
        try:
            return fn(*args, **kwargs)
        except Exception as exc:          # never let the layer hurt the host
            self._fail(where, exc)
            return None

    def _count(self, key: str, n: int = 1) -> None:
        with self._lock:
            self.counters[key] = self.counters.get(key, 0) + n

    def _cached(self, key: str, producer: Callable[[], Any]) -> Any:
        now = time.time()
        with self._lock:
            hit = self._cache.get(key)
            if hit and now - hit[0] < self.CACHE_SECONDS:
                return hit[1]
        value = producer()
        with self._lock:
            self._cache[key] = (now, value)
        return value

    def _invalidate_cache(self) -> None:
        with self._lock:
            self._cache.clear()

    # ------------------------------------------------------------------
    # construction of the components (each one isolated)
    # ------------------------------------------------------------------
    def _build_one(self, name: str, factory: Callable[[], Any]) -> Any:
        try:
            obj = factory()
            self.component_status[name] = "ok"
            return obj
        except Exception as exc:
            self.component_status[name] = f"failed: {type(exc).__name__}: {exc}"
            self._fail(f"build {name}", exc)
            return None

    def _build(self) -> None:
        node, bc = self.node, self.bc
        b = self._build_one
        self.ln_graph = b("LNChannelGraph", lambda: g.LNChannelGraph())
        if self.ln_graph is not None:
            self.ln_router = b("LightningRouter",
                               lambda: g.LightningRouter(self.ln_graph))
        self.whale = b("WhaleTracker", lambda: g.WhaleTracker(bc))
        self.health = b("NetworkHealthIndex",
                        lambda: g.NetworkHealthIndex(bc, getattr(node, "oracle", None)))
        self.flows = b("ExchangeFlowAnalyzer", lambda: g.ExchangeFlowAnalyzer(bc))
        self.zk_prover = b("ZKProver", lambda: g.ZKProver())
        self.zk_operator = b("ZKRollupOperator", lambda: g.ZKRollupOperator(bc))
        if self.zk_operator is not None:
            self.zk_state = self.zk_operator.l2_state       # ZKRollupState
            self.component_status["ZKRollupState"] = "ok"
        self.difficulty = b("DifficultyCLI", lambda: g.DifficultyCLI())
        self.consensus = b("ConsensusManager",
                           lambda: g.ConsensusManager(bc, getattr(node, "governance", None)))

    # ------------------------------------------------------------------
    # attach / detach (chain listener)
    # ------------------------------------------------------------------
    def attach(self) -> None:
        if self._attached:
            return
        self.bc.add_listener(self)          # raises if host has no such API
        with _LAYERS_LOCK:
            _LAYERS.append(self)
        self._attached = True

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer29.detach", exc_info=True)
        with _LAYERS_LOCK:
            if self in _LAYERS:
                _LAYERS.remove(self)
        self._attached = False
        self.stop_explorer()
        self.stop_market_maker()

    # ------------------------------------------------------------------
    # chain listener callbacks
    # ------------------------------------------------------------------
    def on_connect(self, block: Any) -> None:
        try:
            self._count("blocks_seen")
            self._safe("whale.scan_block", self._scan_whales, block)
            height = getattr(block, "height", None)
            if isinstance(height, int):
                if self.HEALTH_EVERY and height % self.HEALTH_EVERY == 0:
                    self._safe("health.compute", self._sample_health)
                if self.DIFFICULTY_EVERY and height % self.DIFFICULTY_EVERY == 0:
                    self._safe("difficulty.report", self._sample_difficulty)
                if self.ZK_CHECK_EVERY and height % self.ZK_CHECK_EVERY == 0:
                    self._safe("zk.selfcheck", self._zk_self_check)
            self._invalidate_cache()
        except Exception as exc:
            self._fail("on_connect", exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        try:
            self._count("reorgs_seen")
            removed = 0
            if self.whale is not None and isinstance(ancestor_height, int):
                with self.whale._lock:
                    keep = [a for a in self.whale._alerts if a.height <= ancestor_height]
                    removed = len(self.whale._alerts) - len(keep)
                    self.whale._alerts[:] = keep
            with self._lock:
                self.last_reorg = {"ancestor_height": ancestor_height,
                                   "whale_alerts_dropped": removed,
                                   "at": time.time()}
            self._invalidate_cache()
        except Exception as exc:
            self._fail("on_reorg", exc)

    # ------------------------------------------------------------------
    # chain-listener work items
    # ------------------------------------------------------------------
    def _scan_whales(self, block: Any) -> None:
        if self.whale is None:
            return
        self.whale.scan_block(block)
        with self.whale._lock:
            extra = len(self.whale._alerts) - self.WHALE_ALERT_CAP
            if extra > 0:
                del self.whale._alerts[:extra]

    def _sample_health(self) -> None:
        if self.health is not None:
            self.last_health = self.health.compute()

    def _sample_difficulty(self) -> None:
        """Report-only: compare alternative algorithms, never apply them."""
        if self.difficulty is None or self.bc is None:
            return
        report = {
            "height": getattr(self.bc, "height", None),
            "simple_ema_bits": g.DifficultyCLI.simple_ema(self.bc),
            "zawy_lwma_bits": g.DifficultyCLI.zawy_lwma(self.bc),
            "at": time.time(),
        }
        getter = getattr(self.bc, "get_next_bits", None)
        if callable(getter):
            report["host_next_bits"] = getter()
        self.last_difficulty = report

    def _zk_self_check(self) -> None:
        """Security monitor: the prover must verify its own proofs and refuse tampered ones."""
        if self.zk_prover is None or self.zk_state is None:
            return
        before = self.zk_state.state_root()
        after = self.zk_state.state_root()
        txs: List[dict] = []
        proof = g.ZKProver.generate_proof(before, after, txs)
        valid_ok = g.ZKProver.verify_proof(before, after, txs, proof)
        tampered = bytes([proof[0] ^ 0xFF]) + proof[1:]
        tamper_rejected = not g.ZKProver.verify_proof(before, after, txs, tampered)
        batches_ok = True
        if self.zk_operator is not None:
            st = self.zk_operator.stats()
            batches_ok = st["verified_batches"] == st["batches_posted"]
        healthy = valid_ok and tamper_rejected and batches_ok
        self.last_zk_check = {"healthy": healthy, "valid_ok": valid_ok,
                              "tamper_rejected": tamper_rejected,
                              "all_batches_verified": batches_ok,
                              "at": time.time()}
        if not healthy:
            self._fail("zk.selfcheck", RuntimeError(f"unhealthy: {self.last_zk_check}"))

    # ------------------------------------------------------------------
    # observers used by the class level wrappers (P2P / mempool)
    # ------------------------------------------------------------------
    def note_p2p(self, peer: Any, msg: Any) -> None:
        kind = _msg_kind(msg)
        with self._lock:
            self.counters["p2p_messages"] += 1
            if kind not in self.p2p_kinds and len(self.p2p_kinds) >= self.P2P_KINDS_CAP:
                kind = "other"
            self.p2p_kinds[kind] = self.p2p_kinds.get(kind, 0) + 1

    def note_mempool_submit(self, tx: Any, result: Any) -> None:
        accepted = True
        if isinstance(result, tuple) and result:
            accepted = bool(result[0])
        elif isinstance(result, bool):
            accepted = result
        self._count("mempool_ok" if accepted else "mempool_rejected")

    # ------------------------------------------------------------------
    # utility classes (explicit, never automatic)
    # ------------------------------------------------------------------
    def get_simulator(self) -> Optional[g.TxSimulator]:
        """TxSimulator needs MockBlockchain from the host (group26)."""
        if self._simulator is None:
            self._simulator = self._build_one("TxSimulator",
                                              lambda: g.TxSimulator(self.bc))
        return self._simulator

    def create_market_maker(self, config: Optional[g.MMConfig] = None,
                            pair: str = "NBL/USDT") -> Optional[g.MarketMakerBot]:
        """Create (but do not start) a MarketMakerBot. Needs node.dex and node.oracle."""
        dex = getattr(self.node, "dex", None)
        oracle = getattr(self.node, "oracle", None)
        if dex is None or oracle is None:
            self.component_status["MarketMakerBot"] = "not created: node has no dex/oracle"
            return None
        cfg = config or g.MMConfig(pair=pair)
        self.market_maker = self._build_one(
            "MarketMakerBot", lambda: g.MarketMakerBot(dex, oracle, cfg))
        return self.market_maker

    def start_market_maker(self, interval: float = 30.0) -> bool:
        if self.market_maker is None and self.create_market_maker() is None:
            return False
        self.market_maker.start(interval)
        return True

    def stop_market_maker(self) -> None:
        if self.market_maker is not None:
            self.market_maker.stop()

    def start_explorer(self, host: str = "127.0.0.1", port: int = 8082) -> bool:
        """Start BlockExplorerV2 (HTTP). Binds to localhost unless told otherwise."""
        if self.explorer is not None:
            return False
        n = self.node
        try:
            explorer = g.BlockExplorerV2(
                self.bc,
                nft=getattr(n, "nft", None), staking=getattr(n, "staking", None),
                amm=getattr(n, "amm", None), dex=getattr(n, "dex", None),
                pool=getattr(n, "pool", None),
                token_registry=getattr(n, "token_registry", None),
                clusterer=getattr(n, "clusterer", None),
                metrics=getattr(n, "metrics", None),
                host=host, port=port)
            explorer.start()
        except Exception as exc:
            self.component_status["BlockExplorerV2"] = f"failed: {type(exc).__name__}: {exc}"
            self._fail("explorer.start", exc)
            return False
        self.explorer = explorer
        self.component_status["BlockExplorerV2"] = "ok"
        return True

    def stop_explorer(self) -> None:
        explorer, self.explorer = self.explorer, None
        if explorer is None:
            return
        try:
            explorer.stop()
            if explorer._server is not None:
                explorer._server.server_close()
        except Exception as exc:
            self._fail("explorer.stop", exc)

    # ------------------------------------------------------------------
    # reports (used by the REST routes and by humans)
    # ------------------------------------------------------------------
    def stats(self) -> dict:
        with self._lock:
            return {
                "errors": self.errors,
                "last_error": self.last_error,
                "counters": dict(self.counters),
                "p2p_kinds": dict(self.p2p_kinds),
                "components": dict(self.component_status),
                "last_reorg": self.last_reorg,
            }

    def report(self, name: str, params: Optional[dict] = None) -> dict:
        params = params or {}
        try:
            return getattr(self, f"_report_{name}")(params)
        except AttributeError:
            return {"error": f"unknown report '{name}'"}
        except Exception as exc:
            self._fail(f"report {name}", exc)
            return {"error": f"report '{name}' failed: {type(exc).__name__}"}

    def _report_status(self, p: dict) -> dict:
        return self.stats()

    def _report_whale(self, p: dict) -> dict:
        if self.whale is None:
            return {"error": "WhaleTracker unavailable"}
        n = _to_int(p.get("n"), 20, 1, 200)
        return {"alerts": self.whale.recent_alerts(n),
                "volume_24h_nbl": self.whale.total_whale_volume_24h()}

    def _report_health(self, p: dict) -> dict:
        if self.health is None:
            return {"error": "NetworkHealthIndex unavailable"}
        return self._cached("health", self.health.compute)

    def _report_exchange_flows(self, p: dict) -> dict:
        if self.flows is None:
            return {"error": "ExchangeFlowAnalyzer unavailable"}
        out = dict(self._cached("flows", self.flows.exchange_flows_24h))
        addr = p.get("addr")
        if isinstance(addr, str) and 0 < len(addr) <= 128:
            out["address"] = addr
            out["classification"] = self._cached(
                f"class:{addr}", lambda: self.flows.classify_address(addr))
        return out

    def _report_consensus(self, p: dict) -> dict:
        if self.consensus is None:
            return {"error": "ConsensusManager unavailable"}
        return {"report_only": True, "stats": self.consensus.stats(),
                "history": self.consensus.history()}

    def _report_difficulty(self, p: dict) -> dict:
        return {"report_only": True, "latest": self.last_difficulty}

    def _report_zk(self, p: dict) -> dict:
        if self.zk_operator is None:
            return {"error": "ZKRollupOperator unavailable"}
        return {"stats": self.zk_operator.stats(), "self_check": self.last_zk_check}

    def _report_ln(self, p: dict) -> dict:
        if self.ln_graph is None:
            return {"error": "LNChannelGraph unavailable"}
        return {"graph": self.ln_graph.stats()}

    # ------------------------------------------------------------------
    # live table of all 20 classes
    # ------------------------------------------------------------------
    def registry(self) -> List[Dict[str, Any]]:
        def row(cls: str, role: str, via: str, obj: Any) -> Dict[str, Any]:
            return {"class": cls, "role": role, "wired_via": via,
                    "instance": obj is not None}
        return [
            row("LNChannelGraph", "service", "P2P observer / node.group29.ln_graph", self.ln_graph),
            row("LightningRouter", "service", "mempool hook / node.group29.ln_router", self.ln_router),
            row("WhaleAlert", "data", "created by WhaleTracker", self.whale),
            row("WhaleTracker", "service", "chain listener on_connect/on_reorg", self.whale),
            row("NetworkHealthIndex", "service", "chain listener (every N blocks) + REST", self.health),
            row("ExchangeFlowAnalyzer", "service", "REST on demand (cached)", self.flows),
            row("RollupBatch", "data", "created by ZKRollupOperator", self.zk_operator),
            row("ZKRollupState", "service", "security monitor", self.zk_state),
            row("ZKProver", "service", "security monitor self-check", self.zk_prover),
            row("ZKRollupOperator", "service", "security monitor", self.zk_operator),
            row("MMConfig", "data", "used by create_market_maker", True),
            row("MMInventory", "data", "created by MarketMakerBot", True),
            row("MarketMakerBot", "service", "utility, explicit start only", self.market_maker or True),
            row("ConsensusParams", "data", "held by ConsensusManager", self.consensus),
            row("DifficultyCLI", "service", "chain listener, report-only", self.difficulty),
            row("ConsensusManager", "service", "chain listener, report-only", self.consensus),
            row("ExplorerV2Handler", "service", "used by BlockExplorerV2 (opt-in)", True),
            row("BlockExplorerV2", "service", "start_explorer(), localhost default", self.explorer or True),
            row("SimulationResult", "data", "returned by TxSimulator", True),
            row("TxSimulator", "service", "utility via get_simulator()", self._simulator or True),
        ]


# ==========================================================================
# REST helpers
# ==========================================================================
def _find_layer(args: tuple, kwargs: dict) -> Optional[Layer29]:
    for obj in list(args) + list(kwargs.values()):
        if isinstance(obj, Layer29):
            return obj
        for candidate in (obj, getattr(obj, "node", None)):
            layer = getattr(candidate, "group29", None)
            if isinstance(layer, Layer29):
                return layer
    live = _live_layers()
    return live[-1] if live else None


def _find_params(args: tuple, kwargs: dict) -> dict:
    p = kwargs.get("params") or kwargs.get("query")
    if isinstance(p, dict):
        return p
    for obj in args:
        if isinstance(obj, dict):
            return obj
    return {}


def _wrap_ok(host: Any, payload: dict) -> Any:
    fn = getattr(host, "ok", None)
    if callable(fn):
        try:
            result = fn(payload)
            if isinstance(result, tuple):
                return result
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _wrap_ok", exc_info=True)
    return 200, {"success": True, "data": payload}


def _make_route_handler(host: Any, name: str) -> Callable:
    def handler(*args, **kwargs):
        layer = _find_layer(args, kwargs)
        if layer is None:
            return _wrap_ok(host, {"error": "group29 layer not attached"})
        return _wrap_ok(host, layer.report(name, _find_params(args, kwargs)))
    handler.__name__ = f"group29_{name}"
    return handler


# ==========================================================================
# class level wrappers (original ALWAYS runs first, result returned untouched)
# ==========================================================================
def _wrap_p2p(orig: Callable) -> Callable:
    @functools.wraps(orig)
    def wrapper(self, *args, **kwargs):
        result = orig(self, *args, **kwargs)
        try:
            peer = args[0] if len(args) > 0 else kwargs.get("peer")
            msg = args[1] if len(args) > 1 else kwargs.get("msg")
            for layer in _live_layers():
                layer._safe("p2p.observe", layer.note_p2p, peer, msg)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _wrap_p2p.wrapper", exc_info=True)
        return result
    return wrapper


def _wrap_mempool_submit(orig: Callable) -> Callable:
    @functools.wraps(orig)
    def wrapper(self, *args, **kwargs):
        result = orig(self, *args, **kwargs)
        try:
            tx = args[0] if args else kwargs.get("tx")
            layers = _live_layers()
            mine = [l for l in layers if getattr(l.bc, "mempool", None) is self]
            for layer in (mine or layers):
                layer._safe("mempool.observe", layer.note_mempool_submit, tx, result)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _wrap_mempool_submit.wrapper", exc_info=True)
        return result
    return wrapper


# ==========================================================================
# install / uninstall
# ==========================================================================
def install(host: Any) -> Dict[str, Any]:
    """Attach group29 to the host module. Safe to call twice."""
    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is None:
        raise RuntimeError("host module has no NEBULAFullNode - cannot install group29")
    if getattr(node_cls, "_g29_orig", None):
        return {"already_installed": True}

    patched_parts: List[str] = []

    # 1) node constructor ------------------------------------------------
    orig_init = node_cls.__init__

    @functools.wraps(orig_init)
    def patched_init(self, *a, **k):
        orig_init(self, *a, **k)
        try:
            layer = Layer29(self)
            layer.attach()
            self.group29 = layer
        except Exception as exc:          # the node must still start
            self.group29_error = exc
            log.warning("group29 attach failed: %s", exc)

    node_cls._g29_orig = orig_init
    node_cls.__init__ = patched_init
    patched_parts.append("NEBULAFullNode.__init__")

    # 2) P2P message hook -------------------------------------------------
    p2p_cls = getattr(host, "P2PNode", None)
    if p2p_cls is not None and callable(getattr(p2p_cls, "_handle_message", None)):
        p2p_cls._g29_orig_handle = p2p_cls._handle_message
        p2p_cls._handle_message = _wrap_p2p(p2p_cls._handle_message)
        patched_parts.append("P2PNode._handle_message")

    # 3) Mempool.submit hook ---------------------------------------------
    mp_cls = getattr(host, "Mempool", None)
    if mp_cls is not None and callable(getattr(mp_cls, "submit", None)):
        mp_cls._g29_orig_submit = mp_cls.submit
        mp_cls.submit = _wrap_mempool_submit(mp_cls.submit)
        patched_parts.append("Mempool.submit")

    # 4) REST routes (GET, read-only) ------------------------------------
    route_fn = getattr(host, "route", None)
    registered: List[str] = []
    if callable(route_fn):
        for name in ROUTE_NAMES:
            path = f"{ROUTE_PREFIX}/{name}"
            route_fn(path)(_make_route_handler(host, name))
            registered.append(path)
        patched_parts.append("REST routes")
    node_cls._g29_routes = registered

    return {"already_installed": False, "patched": patched_parts, "routes": registered}


def uninstall(host: Any) -> bool:
    """Undo install(): host behaves like before. Returns True if something was undone."""
    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is None:
        return False
    orig_init = getattr(node_cls, "_g29_orig", None)
    if not orig_init:
        return False

    for layer in _live_layers():
        layer.detach()

    node_cls.__init__ = orig_init
    del node_cls._g29_orig

    p2p_cls = getattr(host, "P2PNode", None)
    if p2p_cls is not None and getattr(p2p_cls, "_g29_orig_handle", None):
        p2p_cls._handle_message = p2p_cls._g29_orig_handle
        del p2p_cls._g29_orig_handle

    mp_cls = getattr(host, "Mempool", None)
    if mp_cls is not None and getattr(mp_cls, "_g29_orig_submit", None):
        mp_cls.submit = mp_cls._g29_orig_submit
        del mp_cls._g29_orig_submit

    routes = getattr(host, "_routes", None)
    for path in getattr(node_cls, "_g29_routes", []):
        if isinstance(routes, dict):
            for table in routes.values():
                if isinstance(table, dict):
                    table.pop(path, None)
    if hasattr(node_cls, "_g29_routes"):
        del node_cls._g29_routes
    return True
