"""NEBULA group35 wiring layer.

Connects the 20 previously dead classes of ``nebula_group35`` to the live node
WITHOUT editing ``nebula_v10_11.py``.

Design rules (taken from the group35 guide):
  * Report-only first: nothing here rejects a block, a transaction or a message.
  * Every callback runs inside try/except; failures are counted in ``layer.errors``.
  * The original host method always runs first; its result is returned untouched.
  * ``uninstall(host)`` restores every patched method and removes every route.

Public API:
  install(host)      -> dict report (idempotent)
  uninstall(host)    -> None
  attach(node)       -> Layer35 (for a node that was created before install)
  Layer35            -> the layer object, available as ``node.group35``

Wiring map:
  chain listener   : DynamicFeeModel, ConsensusRuleEngine (report-only),
                     MetricsCollector, PriorityFeeAuction, ForkChoiceRule,
                     ChainParametersRegistry, ChainArchiver, OnChainMetadata
  wallet side      : EmergencyMultiSig, WalletConnectBridge, KeyBlinding
  state / economy  : SmartEscrowEngine, SubscriptionManager (manual use only)
  utility          : CircuitBreaker, ExtendedTestSuite (on demand)
  Mempool.submit   : observe-only wrapper -> MetricsCollector
  P2PNode message  : observe-only wrapper -> NetworkStatsCollector
  REST (@route)    : read-only GET endpoints under /api/g35/
"""
from __future__ import annotations

import logging
import os
import threading
import time
from collections import deque
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group35 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group35")

_LOCK = threading.RLock()
_ACTIVE: List["Layer35"] = []                      # layers currently attached
_PATCHES: Dict[Tuple[Any, str], Any] = {}          # (class, method name) -> original
_ROUTES: Dict[str, Callable] = {}                  # path -> handler we registered

ROUTE_PREFIX = "/api/g35"


# --------------------------------------------------------------------------
# Layer
# --------------------------------------------------------------------------
class Layer35:
    """Holds one instance of every group35 service for a single node."""

    def __init__(self, node: Any, archive_dir: Optional[str] = None):
        self.node = node
        self.bc = getattr(node, "bc", None)
        self.errors = 0
        self.last_error = ""
        self.stats_: Dict[str, int] = {
            "blocks_seen": 0,
            "reorgs_seen": 0,
            "rule_failures": 0,
            "txs_seen": 0,
            "txs_accepted": 0,
            "txs_rejected": 0,
            "messages_seen": 0,
        }
        self.build_errors: Dict[str, str] = {}
        self.recent_rule_failures: deque = deque(maxlen=50)
        self.last_rule_report: Optional[dict] = None
        self._lock = threading.RLock()

        self.circuit: Optional[Any] = None
        self.multisig: Optional[Any] = None
        self.fee_model: Optional[Any] = None
        self.fee_auction: Optional[Any] = None
        self.rules: Optional[Any] = None
        self.wc_bridge: Optional[Any] = None
        self.ipfs: Optional[Any] = None
        self.onchain_meta: Optional[Any] = None
        self.key_blinding: Any = g.KeyBlinding            # static helpers, no instance needed
        self.net_stats: Optional[Any] = None
        self.params: Optional[Any] = None
        self.fork_choice: Optional[Any] = None
        self.archiver: Optional[Any] = None
        self.metrics: Optional[Any] = None
        self.subscriptions: Optional[Any] = None
        self.escrow: Optional[Any] = None

        self._archive_dir = archive_dir or os.environ.get(
            "NEBULA_G35_ARCHIVE_DIR", "./nebula_archive")
        self._build()

    # ---- construction ---------------------------------------------------
    def _make(self, attr: str, factory: Callable[[], Any]) -> None:
        try:
            setattr(self, attr, factory())
        except Exception as exc:  # a failed service must never stop the node
            self.build_errors[attr] = f"{type(exc).__name__}: {exc}"
            log.warning("group35: could not build %s: %s", attr, exc)

    def _build(self) -> None:
        bc = self.bc
        guardians = [x.strip() for x in
                     os.environ.get("NEBULA_G35_GUARDIANS", "").split(",") if x.strip()]
        try:
            required = max(1, int(os.environ.get("NEBULA_G35_REQUIRED", "2")))
        except ValueError:
            required = 2

        self._make("circuit", lambda: g.CircuitBreaker())
        self._make("multisig", lambda: g.EmergencyMultiSig(guardians, required))
        self._make("wc_bridge", lambda: g.WalletConnectBridge())
        self._make("ipfs", lambda: g.IPFSClient())            # no network call at construction
        self._make("net_stats", lambda: g.NetworkStatsCollector())
        self._make("params", lambda: g.ChainParametersRegistry())

        if bc is None:
            self.build_errors["chain"] = "node has no 'bc' attribute; chain services skipped"
            return

        self._make("fee_model", lambda: g.DynamicFeeModel(bc))
        self._make("rules", lambda: g.ConsensusRuleEngine(bc))
        self._make("fork_choice", lambda: g.ForkChoiceRule(bc))
        self._make("archiver", lambda: g.ChainArchiver(bc, self._archive_dir))
        self._make("metrics", lambda: g.MetricsCollector(bc))
        self._make("subscriptions", lambda: g.SubscriptionManager(bc))
        self._make("escrow", lambda: g.SmartEscrowEngine(bc))
        if self.fee_model is not None:
            self._make("fee_auction",
                       lambda: g.PriorityFeeAuction(bc.mempool, self.fee_model))
        if self.ipfs is not None:
            self._make("onchain_meta", lambda: g.OnChainMetadata(bc, self.ipfs))

    # ---- safety wrapper -------------------------------------------------
    def _safe(self, where: str, fn: Callable, *args, **kwargs) -> Any:
        try:
            return fn(*args, **kwargs)
        except Exception as exc:
            with self._lock:
                self.errors += 1
                self.last_error = f"{where}: {type(exc).__name__}: {exc}"
            log.warning("group35 %s failed: %s", where, exc)
            return None

    def _bump(self, key: str, n: int = 1) -> None:
        with self._lock:
            self.stats_[key] = self.stats_.get(key, 0) + n

    # ---- chain listener interface --------------------------------------
    def on_connect(self, block: Any) -> None:
        self._bump("blocks_seen")
        if self.fee_model is not None:
            self._safe("fee_model.update_base_fee", self.fee_model.update_base_fee, block)
        if self.rules is not None:
            result = self._safe("rules.validate", self.rules.validate, block)
            if result is not None:
                ok_flag, problems = result
                report = {"height": getattr(block, "height", None),
                          "ok": bool(ok_flag), "errors": list(problems)}
                with self._lock:
                    self.last_rule_report = report
                if not ok_flag:
                    self._bump("rule_failures")
                    with self._lock:
                        self.recent_rule_failures.append(report)
        if self.metrics is not None:
            self._safe("metrics.blocks", self.metrics.inc, "nebula_g35_blocks_connected_total")
            self._safe("metrics.size", self._observe_block, block)

    def _observe_block(self, block: Any) -> None:
        self.metrics.observe("nebula_g35_block_size_bytes", float(block.byte_size()))
        self.metrics.observe("nebula_g35_block_tx_count", float(len(block.transactions)))

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        self._bump("reorgs_seen")
        if self.metrics is not None:
            self._safe("metrics.reorg", self.metrics.inc, "nebula_g35_reorgs_total")

    # ---- observe-only hooks (called by the install wrappers) -----------
    def on_submit(self, tx: Any, result: Any) -> None:
        self._bump("txs_seen")
        accepted = bool(result[0]) if isinstance(result, tuple) and result else bool(result)
        self._bump("txs_accepted" if accepted else "txs_rejected")
        if self.metrics is not None:
            self._safe("metrics.submit", self.metrics.inc,
                       "nebula_g35_mempool_submit_total",
                       1.0, {"accepted": "true" if accepted else "false"})

    def on_message(self, peer: Any, msg: Any) -> None:
        self._bump("messages_seen")
        if self.net_stats is not None:
            self._safe("net_stats.record", self._record_message, peer, msg)

    def _record_message(self, peer: Any, msg: Any) -> None:
        self.net_stats.record_message(_peer_id(peer), _msg_type(msg), _msg_size(msg), "recv")

    # ---- on-demand helpers (never called automatically) ----------------
    def run_extended_tests(self) -> dict:
        """Run the extended test suite. Slow; call it manually."""
        return g.ExtendedTestSuite().run_all()

    def process_subscriptions(self) -> list:
        """Move due subscription payments. Changes state, so manual only."""
        if self.subscriptions is None:
            return []
        return self.subscriptions.process_due()

    def component_paused(self, component: str) -> bool:
        """True when the circuit breaker has paused the named component."""
        return bool(self.circuit and self.circuit.is_paused(component))

    def snapshot(self) -> dict:
        with self._lock:
            stats = dict(self.stats_)
            last_error = self.last_error
            errors = self.errors
            last_rules = self.last_rule_report
        return {
            "errors": errors,
            "last_error": last_error,
            "stats": stats,
            "build_errors": dict(self.build_errors),
            "services": {name: getattr(self, name) is not None for name in _SERVICE_NAMES},
            "base_fee": self.fee_model.current_base_fee() if self.fee_model else None,
            "last_rule_report": last_rules,
        }

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer35.detach", exc_info=True)
        with _LOCK:
            if self in _ACTIVE:
                _ACTIVE.remove(self)


_SERVICE_NAMES = (
    "circuit", "multisig", "fee_model", "fee_auction", "rules", "wc_bridge",
    "ipfs", "onchain_meta", "net_stats", "params", "fork_choice", "archiver",
    "metrics", "subscriptions", "escrow",
)


# --------------------------------------------------------------------------
# Small defensive helpers for message parsing
# --------------------------------------------------------------------------
def _peer_id(peer: Any) -> str:
    for attr in ("addr", "address", "id", "peer_id"):
        value = getattr(peer, attr, None)
        if value:
            return str(value)
    return str(peer)


def _msg_type(msg: Any) -> str:
    if isinstance(msg, dict):
        return str(msg.get("type") or msg.get("command") or "unknown")
    for attr in ("command", "type", "msg_type"):
        value = getattr(msg, attr, None)
        if value:
            return str(value)
    return type(msg).__name__


def _msg_size(msg: Any) -> int:
    if isinstance(msg, (bytes, bytearray)):
        return len(msg)
    payload = msg.get("payload") if isinstance(msg, dict) else getattr(msg, "payload", None)
    if isinstance(payload, (bytes, bytearray, str)):
        return len(payload)
    return 0


# --------------------------------------------------------------------------
# Patching helpers
# --------------------------------------------------------------------------
def _patch(cls: Any, name: str, make_wrapper: Callable[[Callable], Callable]) -> bool:
    key = (cls, name)
    if key in _PATCHES:
        return False
    original = getattr(cls, name, None)
    if original is None or not callable(original):
        return False
    _PATCHES[key] = original
    setattr(cls, name, make_wrapper(original))
    return True


def _unpatch_all() -> None:
    for (cls, name), original in list(_PATCHES.items()):
        setattr(cls, name, original)
    _PATCHES.clear()


def _layers_matching(attr_names: Tuple[str, ...], target: Any) -> List[Layer35]:
    """Layers whose node holds ``target`` under one of ``attr_names``.
    Falls back to the only active layer when no attribute matches."""
    with _LOCK:
        layers = list(_ACTIVE)
    hits = [layer for layer in layers
            if any(getattr(layer.node, a, None) is target for a in attr_names)]
    if hits:
        return hits
    return layers if len(layers) == 1 else []


def _wrap_node_init(original: Callable) -> Callable:
    @wraps(original)
    def patched(self, *args, **kwargs):
        original(self, *args, **kwargs)
        try:
            attach(self)
        except Exception as exc:               # the node must still start
            self.group35_error = exc
            log.warning("group35 attach failed: %s", exc)
    return patched


def _wrap_mempool_submit(original: Callable) -> Callable:
    @wraps(original)
    def patched(self, *args, **kwargs):
        result = original(self, *args, **kwargs)     # original first; exceptions propagate
        try:
            tx = args[0] if args else kwargs.get("tx")
            with _LOCK:
                layers = [l for l in _ACTIVE
                          if getattr(l.bc, "mempool", None) is self]
            for layer in layers:
                layer.on_submit(tx, result)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _wrap_mempool_submit.patched", exc_info=True)
        return result
    return patched


def _wrap_p2p_message(original: Callable) -> Callable:
    @wraps(original)
    def patched(self, *args, **kwargs):
        result = original(self, *args, **kwargs)
        try:
            if len(args) >= 2:
                peer, msg = args[0], args[1]
                for layer in _layers_matching(("network", "p2p", "node", "net"), self):
                    layer.on_message(peer, msg)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _wrap_p2p_message.patched", exc_info=True)
        return result
    return patched


# --------------------------------------------------------------------------
# REST routes (read-only GET)
# --------------------------------------------------------------------------
def _current_layer() -> Optional[Layer35]:
    with _LOCK:
        return _ACTIVE[-1] if _ACTIVE else None


def _reply(host: Any, data: Any, code: int = 200):
    if code == 200:
        fn = getattr(host, "ok", None)
        if callable(fn):
            try:
                return fn(data)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in _reply", exc_info=True)
        return 200, {"success": True, "data": data}
    fn = getattr(host, "err", None)
    if callable(fn):
        try:
            return fn(str(data), code)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _reply", exc_info=True)
    return code, {"success": False, "error": str(data)}


def _make_routes(host: Any) -> Dict[str, Callable]:
    def guarded(builder: Callable[[Layer35], Any]) -> Callable:
        def handler(path, query, body):
            layer = _current_layer()
            if layer is None:
                return _reply(host, "group35 layer is not attached", 503)
            try:
                return _reply(host, builder(layer))
            except Exception as exc:
                with layer._lock:
                    layer.errors += 1
                    layer.last_error = f"route{path}: {type(exc).__name__}: {exc}"
                return _reply(host, f"{type(exc).__name__}: {exc}", 500)
        return handler

    def fees(layer: Layer35) -> dict:
        if layer.fee_model is None:
            raise RuntimeError("fee model unavailable")
        return {
            "base_fee": layer.fee_model.current_base_fee(),
            "suggested": {p: layer.fee_model.suggested_fee(p) for p in ("slow", "normal", "fast")},
            "history": layer.fee_model.fee_history_percentiles(),
        }

    def forkchoice(layer: Layer35) -> dict:
        if layer.fork_choice is None:
            raise RuntimeError("fork choice unavailable")
        height = getattr(layer.bc, "height", 0) or 0
        if height > 100_000:                      # cumulative_work walks the whole chain
            return {"skipped": "chain too long for an on-request walk", "height": height}
        return layer.fork_choice.fork_choice_info()

    def require(layer: Layer35, attr: str) -> Any:
        obj = getattr(layer, attr)
        if obj is None:
            raise RuntimeError(f"{attr} unavailable")
        return obj

    return {
        f"{ROUTE_PREFIX}/status": guarded(lambda l: l.snapshot()),
        f"{ROUTE_PREFIX}/fees": guarded(fees),
        f"{ROUTE_PREFIX}/circuit": guarded(lambda l: require(l, "circuit").status()),
        f"{ROUTE_PREFIX}/params": guarded(lambda l: require(l, "params").all_params()),
        f"{ROUTE_PREFIX}/rules": guarded(lambda l: {
            "summary": require(l, "rules").rules_summary(),
            "recent_failures": list(l.recent_rule_failures)}),
        f"{ROUTE_PREFIX}/forkchoice": guarded(forkchoice),
        f"{ROUTE_PREFIX}/network": guarded(lambda l: {
            "bandwidth": require(l, "net_stats").bandwidth_summary(),
            "distribution": l.net_stats.message_distribution(),
            "health": l.net_stats.network_health_score()}),
        f"{ROUTE_PREFIX}/metrics": guarded(lambda l: require(l, "metrics").metrics_endpoint_handler()),
    }


def _register_routes(host: Any) -> int:
    table = getattr(host, "_routes", None)
    if not isinstance(table, dict):
        return 0
    get_routes = table.setdefault("GET", {})
    count = 0
    for path, handler in _make_routes(host).items():
        if path in get_routes:                 # never override an existing route
            continue
        get_routes[path] = handler
        _ROUTES[path] = handler
        count += 1
    return count


def _unregister_routes(host: Any) -> None:
    table = getattr(host, "_routes", None)
    if isinstance(table, dict):
        get_routes = table.get("GET", {})
        for path, handler in list(_ROUTES.items()):
            if get_routes.get(path) is handler:
                del get_routes[path]
    _ROUTES.clear()


# --------------------------------------------------------------------------
# Public entry points
# --------------------------------------------------------------------------
def _sync_globals(host: Any) -> None:
    """Make host names (Block, Secp256k1, Script, ...) visible inside nebula_group35,
    exactly like the optional shim at the top of that file does."""
    for key, value in vars(host).items():
        if not key.startswith("__") and key not in g.__dict__:
            g.__dict__[key] = value


def attach(node: Any) -> Layer35:
    """Create a layer for ``node`` and register it as a chain listener."""
    existing = getattr(node, "group35", None)
    if isinstance(existing, Layer35):
        return existing
    layer = Layer35(node)
    node.group35 = layer
    bc = getattr(node, "bc", None)
    if bc is not None and hasattr(bc, "add_listener"):
        bc.add_listener(layer)
    else:
        layer.build_errors["listener"] = "chain has no add_listener; running without block events"
    with _LOCK:
        _ACTIVE.append(layer)
    return layer


def install(host: Any) -> dict:
    """Patch the host. Safe to call twice."""
    report = {"installed": False, "patched": [], "routes": 0, "skipped": []}
    if getattr(host, "_g35_installed", False):
        report["installed"] = True
        report["skipped"].append("already installed")
        return report

    _sync_globals(host)

    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is None or not _patch(node_cls, "__init__", _wrap_node_init):
        report["skipped"].append("NEBULAFullNode.__init__ (required) not patched")
        return report
    report["patched"].append("NEBULAFullNode.__init__")

    mempool_cls = getattr(host, "Mempool", None)
    if mempool_cls is not None and _patch(mempool_cls, "submit", _wrap_mempool_submit):
        report["patched"].append("Mempool.submit")
    else:
        report["skipped"].append("Mempool.submit")

    p2p_cls = getattr(host, "P2PNode", None)
    if p2p_cls is not None and _patch(p2p_cls, "_handle_message", _wrap_p2p_message):
        report["patched"].append("P2PNode._handle_message")
    else:
        report["skipped"].append("P2PNode._handle_message")

    report["routes"] = _register_routes(host)
    host._g35_installed = True
    report["installed"] = True
    return report


def uninstall(host: Any) -> None:
    """Restore the host to its original behaviour."""
    with _LOCK:
        layers = list(_ACTIVE)
    for layer in layers:
        layer.detach()
        try:
            layer.node.group35 = None
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in uninstall", exc_info=True)
    _unpatch_all()
    _unregister_routes(host)
    if hasattr(host, "_g35_installed"):
        host._g35_installed = False
