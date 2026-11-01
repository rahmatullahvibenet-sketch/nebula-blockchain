"""NEBULA group46 wiring layer.

Connects the 20 revived classes of ``nebula_group46`` to a running NEBULA node
WITHOUT editing ``nebula_v10_11.py`` or ``nebula_group46.py``.

Design rules (taken from the group46 guide):
  * The layer never rejects a block, a transaction or a P2P message.
  * Every callback runs inside a guard; failures are counted in ``layer.errors``
    and stored in ``layer.error_log`` instead of propagating into the host.
  * Hooks are installed on the node INSTANCE (not on host classes) so that
    ``detach()`` / ``uninstall()`` restore the host exactly.
  * Mempool / P2P hooks call the original method first and only observe.
  * Everything is observe-only: none of the revived classes moves real funds.

Public API:
    install(host, config=None)        patch NEBULAFullNode.__init__
    uninstall(host)                   restore it and detach every layer
    install_on_node(node, config)     attach a layer to an already running node
    Layer46                           the layer itself (alias: Group46Layer)
    Group46Config                     tunables
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import threading
import time
import weakref
from collections import deque
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Callable, Deque, Dict, List, Optional

import nebula_group46 as g46
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group46")

# --------------------------------------------------------------------------
# Wiring map: class -> (guide wiring point, role in this layer)
# --------------------------------------------------------------------------
WIRING_MAP: Dict[str, str] = {
    "ProtocolConfig":          "shared read-only configuration (data type)",
    "CollateralManager":       "security/monitor service: node.group46.services",
    "NFTMetadataStandard":     "state/economy service: validator for NFT metadata",
    "CrossChainOracle":        "chain listener: fed from the host oracle on every block",
    "StakingPoolV3":           "miner side: attached to the miner as group46_staking_pool",
    "DeFiScorecard":           "state/economy service: static scorecard",
    "NFTDropManager":          "state/economy service: needs the host NFT registry",
    "ProtocolComposer":        "state/economy service: uses host dex/staking/farming if found",
    "NEBULAAIAssistant":       "utility service: pattern-based assistant",
    "ZKRollupBatch":           "internal: created by ZKRollupLayer",
    "ZKRollupLayer":           "mempool.submit observer + periodic batch/verify on blocks",
    "DeFiAlertV2":             "chain listener + P2P observer: rate-limited check_all()",
    "OnChainKVStore":          "chain-side service: capped on-chain key/value storage",
    "WalletSecurityManager":   "wallet side: attached to the wallet as group46_security",
    "EcosystemMetricsTracker": "storage: daily snapshots persisted atomically to data_dir",
    "TransactionAnalytics":    "chain listener: per-block analysis (bounded history)",
    "YieldAggregator":         "state/economy service: default protocols registered",
    "TreasuryV3":              "wallet side: attached to the wallet as group46_treasury",
    "OnChainCoinFlip":         "chain-side service: SIMULATION ONLY (no balance changes)",
    "OnChainDice":             "chain-side service: SIMULATION ONLY (no balance changes)",
}


@dataclass
class Group46Config:
    """Tunables for the layer. Defaults are conservative."""
    snapshot_every_blocks: int = 144        # metrics snapshot cadence
    rollup_every_blocks: int = 10           # ZKRollupLayer.PROOF_GEN_BLOCKS
    maintenance_every_blocks: int = 100     # cap trimming cadence
    alert_check_min_interval: float = 5.0   # seconds between DeFiAlertV2.check_all
    max_history: int = 1000                 # cap for in-RAM history lists
    max_rollup_batches: int = 100           # cap for stored rollup batches
    max_daily_records: int = 400            # cap for metrics daily records
    max_block_analysis: int = 200           # cap for analytics history
    persist_metrics: bool = True            # write metrics to <data_dir>/group46
    observe_mempool: bool = True            # wrap mempool.submit (observe only)
    observe_p2p: bool = True                # wrap p2p._handle_message (observe only)
    feed_rollup_from_mempool: bool = True   # record accepted txs in ZKRollupLayer


class _FallbackRNG:
    """Used only when the host has no OnChainRNG. Deterministic and therefore
    PREDICTABLE: fine for simulation, never for real money."""

    def random_int(self, height: int, n: int, nonce: int = 0) -> int:
        digest = hashlib.sha256(f"g46-rng:{height}:{nonce}:{n}".encode()).digest()
        return int.from_bytes(digest[:8], "big") % max(1, n)


_PRIMITIVES = (str, bytes, int, float, bool, type(None), dict, list, tuple, set,
               frozenset, deque)

# Every live layer, so that uninstall() can detach all of them.
_LIVE_LAYERS: "weakref.WeakSet[Layer46]" = weakref.WeakSet()


class Layer46:
    """Holds all group46 services and listens to the node."""

    def __init__(self, node: Any, config: Optional[Group46Config] = None):
        self.node = node
        self.cfg = config or Group46Config()
        self.errors = 0
        self.last_error: Optional[str] = None
        self.error_log: Deque[dict] = deque(maxlen=50)
        self.stats_: Dict[str, int] = {
            "blocks": 0, "reorgs": 0, "mempool_seen": 0, "mempool_fed": 0,
            "p2p_messages": 0, "snapshots": 0, "rollup_batches": 0,
            "maintenance_runs": 0,
        }
        self.services: Dict[str, Any] = {}
        self.skipped: Dict[str, str] = {}
        self.hooks: Dict[str, str] = {}          # hook name -> "attached" / reason
        self.block_analysis: Deque[dict] = deque(maxlen=self.cfg.max_block_analysis)
        self.detached = False
        self._lock = threading.RLock()
        self._undo: List[Callable[[], None]] = []
        self._found: Dict[str, Any] = {}
        self._warned: set = set()
        self._last_alert_check = 0.0
        self._metrics_path: Optional[Path] = self._resolve_metrics_path()

        self._build_services()
        self._load_metrics()
        self._attach_integrations()
        _LIVE_LAYERS.add(self)

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------
    @property
    def bc(self) -> Any:
        return self.node.bc

    def _record_error(self, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.last_error = f"{where}: {type(exc).__name__}: {exc}"
        self.error_log.append({"where": where, "error": self.last_error,
                               "ts": time.time()})
        level = logging.WARNING if where not in self._warned else logging.DEBUG
        self._warned.add(where)
        log.log(level, "group46 %s failed: %s", where, exc)

    def _guard(self, where: str, fn: Callable, *args, **kwargs):
        """Run fn; never raise. Returns (ok, value)."""
        try:
            return True, fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001 - isolation is the point
            self._record_error(where, exc)
            return False, None

    def find(self, class_name: str) -> Any:
        """Find a host service by class name.

        Looks at the attributes of the node and of the blockchain, then one
        level deeper (e.g. node.defi.oracle). Uses vars() only, so no property
        or method of the host is ever executed during discovery.
        """
        if class_name in self._found:
            return self._found[class_name]
        found = None
        seen = set()
        level = [self.node, getattr(self.node, "bc", None)]
        for _depth in range(2):
            next_level = []
            for holder in level:
                if holder is None or id(holder) in seen:
                    continue
                seen.add(id(holder))
                try:
                    values = list(vars(holder).values())
                except TypeError:
                    continue
                for value in values:
                    if value is self or isinstance(value, _PRIMITIVES):
                        continue
                    if class_name in [k.__name__ for k in type(value).__mro__]:
                        found = value
                        break
                    next_level.append(value)
                if found is not None:
                    break
            if found is not None:
                break
            level = next_level[:500]
        self._found[class_name] = found
        return found

    def _resolve_metrics_path(self) -> Optional[Path]:
        if not self.cfg.persist_metrics:
            return None
        data_dir = getattr(self.node, "data_dir", None)
        if data_dir is None:
            data_dir = getattr(getattr(self.node, "config", None), "data_dir", None)
        if not data_dir:
            return None
        return Path(str(data_dir)) / "group46" / "metrics.json"

    # ------------------------------------------------------------------
    # step 1: build services in the guide's dependency order
    # ------------------------------------------------------------------
    def _build_services(self) -> None:
        bc = self.bc

        def need(class_name: str) -> Any:
            obj = self.find(class_name)
            if obj is None:
                raise LookupError(f"host service {class_name} not found on node")
            return obj

        def build_yield() -> Any:
            agg = g46.YieldAggregator(bc)
            agg.initialize_defaults()
            return agg

        steps: List[tuple] = [
            ("ProtocolConfig",          lambda: g46.ProtocolConfig()),
            ("CollateralManager",       lambda: g46.CollateralManager(bc, self.find("OracleV2"))),
            ("NFTMetadataStandard",     lambda: g46.NFTMetadataStandard()),
            ("CrossChainOracle",        lambda: g46.CrossChainOracle()),
            ("StakingPoolV3",           lambda: g46.StakingPoolV3("group46-main", bc)),
            ("DeFiScorecard",           lambda: g46.DeFiScorecard()),
            ("NFTDropManager",          lambda: g46.NFTDropManager(need("NBL721Registry"), bc)),
            ("ProtocolComposer",        lambda: g46.ProtocolComposer(
                                            bc, dex=self.find("NEBULADex"),
                                            staking=self.find("StakingEngine"),
                                            farming=self.find("YieldFarmingV2"))),
            ("NEBULAAIAssistant",       lambda: g46.NEBULAAIAssistant(bc)),
            ("ZKRollupLayer",           lambda: g46.ZKRollupLayer(bc)),
            ("DeFiAlertV2",             lambda: g46.DeFiAlertV2(bc, self.find("OracleV2"))),
            ("OnChainKVStore",          lambda: g46.OnChainKVStore(bc)),
            ("WalletSecurityManager",   lambda: g46.WalletSecurityManager(bc)),
            ("EcosystemMetricsTracker", lambda: g46.EcosystemMetricsTracker(bc)),
            ("TransactionAnalytics",    lambda: g46.TransactionAnalytics(bc)),
            ("YieldAggregator",         build_yield),
            ("TreasuryV3",              lambda: g46.TreasuryV3(bc)),
            ("OnChainCoinFlip",         lambda: g46.OnChainCoinFlip(bc, self._rng())),
            ("OnChainDice",             lambda: g46.OnChainDice(bc, self._rng())),
        ]
        for name, factory in steps:
            try:
                self.services[name] = factory()
            except Exception as exc:  # noqa: BLE001
                self.skipped[name] = f"{type(exc).__name__}: {exc}"
                log.warning("group46: %s not built (%s)", name, exc)

    def _rng(self) -> Any:
        return self.find("OnChainRNG") or _FallbackRNG()

    def svc(self, name: str) -> Any:
        return self.services.get(name)

    # ------------------------------------------------------------------
    # step 2: attach to the node
    # ------------------------------------------------------------------
    def _attach_integrations(self) -> None:
        self._attach_chain_listener()
        self._attach_mempool_observer()
        self._attach_p2p_observer()
        self._attach_attribute("NEBULAWallet", "group46_security",
                               "WalletSecurityManager")
        self._attach_attribute("NEBULAWallet", "group46_treasury", "TreasuryV3")
        self._attach_attribute("NEBULAMiner", "group46_staking_pool",
                               "StakingPoolV3")

    def _attach_chain_listener(self) -> None:
        bc = self.bc
        if not hasattr(bc, "add_listener"):
            self.hooks["chain_listener"] = "host has no add_listener"
            return
        bc.add_listener(self)

        def undo() -> None:
            try:
                bc._listeners.remove(self)
            except (ValueError, AttributeError):
                _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer46._attach_chain_listener.undo", exc_info=True)
        self._undo.append(undo)
        self.hooks["chain_listener"] = "attached"

    def _wrap_instance_method(self, owner: Any, method: str,
                              make_wrapper: Callable[[Callable], Callable]) -> bool:
        original = getattr(owner, method)
        wrapper = make_wrapper(original)
        try:
            setattr(owner, method, wrapper)
        except (AttributeError, TypeError):
            return False

        def undo() -> None:
            try:
                if vars(owner).get(method) is wrapper:
                    delattr(owner, method)
            except (AttributeError, TypeError):
                _NB_SWALLOW_LOG.debug("swallowed (AttributeError, TypeError) in Layer46._wrap_instance_method.undo", exc_info=True)
        self._undo.append(undo)
        return True

    def _attach_mempool_observer(self) -> None:
        mempool = getattr(self.bc, "mempool", None)
        if not self.cfg.observe_mempool or mempool is None \
                or not hasattr(mempool, "submit"):
            self.hooks["mempool_observer"] = "disabled or unavailable"
            return
        layer = self

        def make(original: Callable) -> Callable:
            def submit(tx, *args, **kwargs):
                result = original(tx, *args, **kwargs)     # host first, always
                ok, _ = layer._guard("mempool_observer", layer._observe_submit,
                                     tx, result)
                return result
            return submit

        attached = self._wrap_instance_method(mempool, "submit", make)
        self.hooks["mempool_observer"] = "attached" if attached else "instance not patchable"

    def _attach_p2p_observer(self) -> None:
        p2p = self.find("P2PNode")
        if not self.cfg.observe_p2p or p2p is None \
                or not hasattr(p2p, "_handle_message"):
            self.hooks["p2p_observer"] = "disabled or unavailable"
            return
        layer = self

        def make(original: Callable) -> Callable:
            def handle(*args, **kwargs):
                result = original(*args, **kwargs)         # host first, always
                layer._guard("p2p_observer", layer._observe_p2p)
                return result
            return handle

        attached = self._wrap_instance_method(p2p, "_handle_message", make)
        self.hooks["p2p_observer"] = "attached" if attached else "instance not patchable"

    def _attach_attribute(self, host_class: str, attr: str, service: str) -> None:
        target = self.find(host_class)
        obj = self.svc(service)
        if target is None or obj is None:
            self.hooks[attr] = "host object or service missing"
            return
        try:
            setattr(target, attr, obj)
        except (AttributeError, TypeError):
            self.hooks[attr] = "not settable"
            return

        def undo() -> None:
            try:
                if getattr(target, attr, None) is obj:
                    delattr(target, attr)
            except (AttributeError, TypeError):
                _NB_SWALLOW_LOG.debug("swallowed (AttributeError, TypeError) in Layer46._attach_attribute.undo", exc_info=True)
        self._undo.append(undo)
        self.hooks[attr] = "attached"

    # ------------------------------------------------------------------
    # chain listener interface (called by NEBULABlockchain)
    # ------------------------------------------------------------------
    def on_connect(self, block: Any) -> None:
        with self._lock:
            if self.detached:
                return
            self.stats_["blocks"] += 1
            height = self._height_of(block)
            self._guard("oracle_feed", self._feed_oracle)
            self._guard("analytics", self._analyze_block, block)
            if self.stats_["blocks"] == 1 or height % max(1, self.cfg.snapshot_every_blocks) == 0:
                self._guard("metrics_snapshot", self._snapshot_metrics)
            self._guard("alerts", self._maybe_check_alerts)
            if height % max(1, self.cfg.rollup_every_blocks) == 0:
                self._guard("rollup", self._seal_rollup)
            if self.stats_["blocks"] % max(1, self.cfg.maintenance_every_blocks) == 0:
                self._guard("maintenance", self.run_maintenance)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        with self._lock:
            if self.detached:
                return
            self.stats_["reorgs"] += 1
            kept = [a for a in self.block_analysis
                    if int(a.get("height", 0)) <= int(ancestor_height)]
            self.block_analysis = deque(kept, maxlen=self.cfg.max_block_analysis)

    def _height_of(self, block: Any) -> int:
        h = getattr(block, "height", None)
        return int(h if h is not None else self.bc.height)

    # ------------------------------------------------------------------
    # handlers
    # ------------------------------------------------------------------
    def _feed_oracle(self) -> None:
        host_oracle = self.find("OracleV2")
        cross = self.svc("CrossChainOracle")
        if host_oracle is None or cross is None:
            return
        price = host_oracle.price("NBL/USD")
        if price:
            cross.ingest_chain_price("nebula", "NBL/USD", float(price), "nebula_oracle")

    def _analyze_block(self, block: Any) -> None:
        analytics = self.svc("TransactionAnalytics")
        if analytics is None:
            return
        result = analytics.analyze_block(block, self.bc.utxo)
        if result:
            self.block_analysis.append(result)

    def _snapshot_metrics(self) -> None:
        tracker = self.svc("EcosystemMetricsTracker")
        if tracker is None:
            return
        tracker.auto_snapshot()
        self.stats_["snapshots"] += 1
        self._persist_metrics()

    def _maybe_check_alerts(self) -> None:
        alerts = self.svc("DeFiAlertV2")
        now = time.time()
        if alerts is None or now - self._last_alert_check < self.cfg.alert_check_min_interval:
            return
        self._last_alert_check = now
        alerts.check_all()

    def _seal_rollup(self) -> None:
        rollup = self.svc("ZKRollupLayer")
        if rollup is None:
            return
        batch_id = rollup.force_batch()
        if batch_id:
            rollup.verify_batch(batch_id)
            self.stats_["rollup_batches"] += 1

    def _observe_submit(self, tx: Any, result: Any) -> None:
        accepted = result[0] if isinstance(result, tuple) and result else bool(result)
        if not accepted:
            return
        self.stats_["mempool_seen"] += 1
        rollup = self.svc("ZKRollupLayer")
        if self.cfg.feed_rollup_from_mempool and rollup is not None:
            rollup.submit_l2_tx({"txid": self._txid(tx), "ts": time.time()})
            self.stats_["mempool_fed"] += 1

    def _observe_p2p(self) -> None:
        self.stats_["p2p_messages"] += 1
        self._maybe_check_alerts()

    @staticmethod
    def _txid(tx: Any) -> str:
        value = getattr(tx, "txid", None)
        if callable(value):
            value = value()
        if value:
            return str(value)
        return hashlib.sha256(repr(tx).encode()).hexdigest()[:16]

    # ------------------------------------------------------------------
    # bounded memory
    # ------------------------------------------------------------------
    @staticmethod
    def _trim_list(obj: Any, attr: str, limit: int) -> None:
        items = getattr(obj, attr, None)
        if isinstance(items, list) and len(items) > limit:
            del items[:-limit]

    def run_maintenance(self) -> None:
        """Trim every in-RAM history to its configured cap."""
        cap = self.cfg.max_history
        self.stats_["maintenance_runs"] += 1
        for service, attr in (
            ("NEBULAAIAssistant", "_history"),
            ("ProtocolComposer", "_ops_log"),
            ("DeFiAlertV2", "_alerts"),
            ("OnChainCoinFlip", "_games"),
            ("OnChainDice", "_rolls"),
        ):
            obj = self.svc(service)
            if obj is not None:
                self._trim_list(obj, attr, cap)
        rollup = self.svc("ZKRollupLayer")
        if rollup is not None:
            with rollup._lock:
                extra = len(rollup._batches) - self.cfg.max_rollup_batches
                if extra > 0:
                    for key in sorted(rollup._batches)[:extra]:
                        del rollup._batches[key]
        tracker = self.svc("EcosystemMetricsTracker")
        if tracker is not None:
            with tracker._lock:
                extra = len(tracker._daily) - self.cfg.max_daily_records
                if extra > 0:
                    for key in sorted(tracker._daily)[:extra]:
                        del tracker._daily[key]

    # ------------------------------------------------------------------
    # storage: atomic metrics persistence (tmp + fsync + rename)
    # ------------------------------------------------------------------
    def _persist_metrics(self) -> None:
        tracker = self.svc("EcosystemMetricsTracker")
        path = self._metrics_path
        if tracker is None or path is None:
            return
        with tracker._lock:
            payload = {"version": 1, "daily": dict(tracker._daily)}
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_name(path.name + ".tmp")
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, sort_keys=True)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)

    def _load_metrics(self) -> None:
        tracker = self.svc("EcosystemMetricsTracker")
        path = self._metrics_path
        if tracker is None or path is None or not path.exists():
            return
        ok, _ = self._guard("metrics_load", self._load_metrics_unsafe, tracker, path)
        if not ok:
            log.warning("group46: metrics file ignored (unreadable): %s", path)

    @staticmethod
    def _load_metrics_unsafe(tracker: Any, path: Path) -> None:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        daily = data.get("daily", {})
        if data.get("version") != 1 or not isinstance(daily, dict):
            raise ValueError("unexpected metrics file layout")
        clean = {str(k): v for k, v in daily.items() if isinstance(v, dict)}
        with tracker._lock:
            tracker._daily.update(clean)

    # ------------------------------------------------------------------
    # reporting (read-only)
    # ------------------------------------------------------------------
    def wiring_report(self) -> Dict[str, dict]:
        report: Dict[str, dict] = {}
        for name, role in WIRING_MAP.items():
            if name in self.services:
                state = "wired"
            elif name == "ZKRollupBatch":
                state = "wired" if "ZKRollupLayer" in self.services else "skipped"
            else:
                state = "skipped"
            report[name] = {"state": state, "role": role}
            if name in self.skipped:
                report[name]["reason"] = self.skipped[name]
        return report

    def status(self) -> dict:
        rollup = self.svc("ZKRollupLayer")
        tracker = self.svc("EcosystemMetricsTracker")
        return {
            "errors": self.errors,
            "last_error": self.last_error,
            "detached": self.detached,
            "stats": dict(self.stats_),
            "hooks": dict(self.hooks),
            "skipped": dict(self.skipped),
            "services": sorted(self.services),
            "rollup": rollup.rollup_stats() if rollup else None,
            "metrics_days": len(tracker._daily) if tracker else 0,
            "analysis_history": len(self.block_analysis),
            "config": asdict(self.cfg),
        }

    def api_routes(self) -> Dict[str, Callable[[], dict]]:
        """Read-only routes the host REST layer may mount. All return plain dicts."""
        def latest_analysis() -> dict:
            return dict(self.block_analysis[-1]) if self.block_analysis else {}

        def safe(name: str, fn: Callable[[], Any]) -> Callable[[], dict]:
            def route() -> dict:
                ok, value = self._guard(f"api:{name}", fn)
                return value if ok and isinstance(value, dict) else {"error": "unavailable"}
            return route

        s = self.svc
        routes: Dict[str, Callable[[], dict]] = {
            "/g46/status":     lambda: self.status(),
            "/g46/wiring":     lambda: self.wiring_report(),
            "/g46/scorecard":  lambda: s("DeFiScorecard").get_scores(),
            "/g46/analytics":  latest_analysis,
            "/g46/oracle":     lambda: s("CrossChainOracle").oracle_health(),
            "/g46/rollup":     lambda: s("ZKRollupLayer").rollup_stats(),
            "/g46/treasury":   lambda: s("TreasuryV3").treasury_v3_stats(),
            "/g46/kv":         lambda: s("OnChainKVStore").kv_stats(),
            "/g46/alerts":     lambda: s("DeFiAlertV2").alert_stats(),
            "/g46/assistant":  lambda: s("NEBULAAIAssistant").assistant_stats(),
            "/g46/composer":   lambda: s("ProtocolComposer").composer_stats(),
            "/g46/protocol":   lambda: s("ProtocolConfig").to_dict(),
        }
        return {path: safe(path, fn) for path, fn in routes.items()}

    # ------------------------------------------------------------------
    # teardown
    # ------------------------------------------------------------------
    def detach(self) -> None:
        """Remove every hook this layer installed. Safe to call repeatedly."""
        with self._lock:
            if self.detached:
                return
            self.detached = True
            for undo in reversed(self._undo):
                try:
                    undo()
                except Exception as exc:  # noqa: BLE001
                    log.debug("group46 undo failed: %s", exc)
            self._undo.clear()
            self._guard("final_persist", self._persist_metrics)


Group46Layer = Layer46


# --------------------------------------------------------------------------
# install / uninstall
# --------------------------------------------------------------------------
def install_on_node(node: Any, config: Optional[Group46Config] = None) -> Layer46:
    """Attach a layer to an already running node (idempotent)."""
    existing = getattr(node, "group46", None)
    if isinstance(existing, Layer46) and not existing.detached:
        return existing
    layer = Layer46(node, config)
    node.group46 = layer
    return layer


def install(host: Any, config: Optional[Group46Config] = None) -> None:
    """Patch ``host.NEBULAFullNode.__init__`` so every new node gets a layer."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g46_orig", None):
        return
    original = cls.__init__

    def patched(self, *args, **kwargs):
        original(self, *args, **kwargs)
        try:                                   # the node must still start
            install_on_node(self, config)
        except Exception as exc:  # noqa: BLE001
            self.group46_error = exc
            log.warning("group46 install failed: %s", exc)

    cls._g46_orig = original
    cls.__init__ = patched


def uninstall(host: Any) -> None:
    """Restore NEBULAFullNode.__init__ and detach every live layer."""
    cls = host.NEBULAFullNode
    original = getattr(cls, "_g46_orig", None)
    if original:
        cls.__init__ = original
        del cls._g46_orig
    for layer in list(_LIVE_LAYERS):
        layer.detach()
