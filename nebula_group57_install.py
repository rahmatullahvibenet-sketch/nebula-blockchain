"""NEBULA group57 - wiring layer (install / uninstall).

Connects the 20 formerly-dead classes of nebula_group57.py to a running
NEBULAFullNode WITHOUT editing nebula_v10_11.py and WITHOUT editing
nebula_group57.py (the 20 classes stay byte-for-byte as extracted).

Usage
-----
    import nebula_v10_11 as host
    import nebula_group57_install as g57
    g57.install(host)            # every NEBULAFullNode created afterwards gets node.group57
    ...
    node = host.NEBULAFullNode(...)
    node.group57.snapshot()      # read-only view of everything
    node.group57.api_get("/api/g57/health")
    g57.uninstall(host)          # restores the original __init__ and detaches live layers

Safety rules (from the group57 guide)
-------------------------------------
* Report-only: this layer never rejects a block, a transaction or a peer.
* Every callback is wrapped in try/except; failures only increment `errors`.
* A failure while building the layer never stops the node from starting
  (the error is stored in node.group57_error).
* All data kept in RAM is capped.
"""
from __future__ import annotations

import logging
import math
import threading
import time
import weakref
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group57 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group57")

# ---------------------------------------------------------------------------
# Tunables
# ---------------------------------------------------------------------------
SNAPSHOT_EVERY_N_BLOCKS = 144      # roughly one metrics snapshot per day at 10-minute blocks
MAX_SNAPSHOTS           = 365      # cap for DailyMetricsCollector history kept in RAM
MAX_QUERY_AMOUNT        = 1e15     # sanity cap for calculator inputs coming from REST
MAX_QUERY_DAYS          = 3650
API_PREFIX              = "/api/g57"

# Layers currently attached to live nodes (so uninstall() can detach them).
_LIVE_LAYERS: "weakref.WeakSet[Layer57]" = weakref.WeakSet()


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
class _BadRequest(ValueError):
    """Raised for invalid REST query parameters (maps to HTTP 400)."""


def _first(value: Any) -> Any:
    """Query values may be lists (parse_qs) or plain strings."""
    if isinstance(value, (list, tuple)):
        return value[0] if value else None
    return value


def _num(query: Dict[str, Any], key: str, default: Optional[float] = None,
         lo: float = 0.0, hi: float = MAX_QUERY_AMOUNT,
         lo_exclusive: bool = False) -> float:
    raw = _first(query.get(key))
    if raw is None or raw == "":
        if default is None:
            raise _BadRequest(f"missing parameter: {key}")
        return float(default)
    try:
        val = float(raw)
    except (TypeError, ValueError):
        raise _BadRequest(f"parameter '{key}' must be a number")
    if not math.isfinite(val):
        raise _BadRequest(f"parameter '{key}' must be finite")
    if val < lo or (lo_exclusive and val == lo) or val > hi:
        raise _BadRequest(f"parameter '{key}' out of range")
    return val


def _text(query: Dict[str, Any], key: str, default: Optional[str] = None,
          max_len: int = 128) -> str:
    raw = _first(query.get(key))
    if raw is None or raw == "":
        if default is None:
            raise _BadRequest(f"missing parameter: {key}")
        return default
    raw = str(raw)
    if len(raw) > max_len:
        raise _BadRequest(f"parameter '{key}' too long")
    return raw


# ---------------------------------------------------------------------------
# The layer
# ---------------------------------------------------------------------------
class Layer57:
    """Holds every group57 component for one node and listens to its chain.

    Build order (each stage only depends on earlier ones):
      1. static utilities          - need nothing
      2. stand-alone instances     - need nothing
      3. host-dependent instances  - need classes from other groups
      4. chain-bound instances     - need node.bc
      5. lazy instances            - need extra arguments (factory, miner)
    """

    def __init__(self, node: Any, snapshot_every: int = SNAPSHOT_EVERY_N_BLOCKS):
        self.node = node
        self.bc = node.bc
        self.errors = 0
        self.last_error: Optional[str] = None
        self.component_errors: Dict[str, str] = {}
        self.stats_: Dict[str, Any] = {
            "blocks_seen": 0,
            "reorgs": 0,
            "snapshots": 0,
            "last_snapshot_height": None,
            "last_reorg_ancestor": None,
        }
        self._snapshot_every = max(1, int(snapshot_every))
        self._lock = threading.RLock()
        self._attached = False
        self._build_all()
        _LIVE_LAYERS.add(self)

    # ------------------------------------------------------------------ build
    def _build(self, name: str, factory: Callable[[], Any]) -> Any:
        try:
            return factory()
        except Exception as exc:  # a missing dependency must never stop the node
            self.component_errors[name] = f"{type(exc).__name__}: {exc}"
            log.warning("group57 component '%s' unavailable: %s", name, exc)
            return None

    def _build_all(self) -> None:
        # Stage 1 - static utilities (classes with only static/class methods).
        self.pool_math = g.LiquidityPoolMath
        self.defi_math = g.DeFiMath
        self.yield_math = g.YieldMath
        self.contract_abi = g.NEBULAContractABI
        self.js_sdk_doc = g.NEBULAJavascriptSDKDoc
        self.whitepaper = g.NEBULAWhitepaper
        self.testnet_config = g.NEBULATestnetConfig
        self.mainnet_config = g.NEBULAMainnetConfig

        # Stage 2 - stand-alone instances.
        self.staking = self._build("staking", g.StakingCalculator)
        self.community = self._build("community", g.NEBULACommunityStats)
        self.topology = self._build("topology", g.NetworkTopologyMap)

        # Stage 3 - needs InterestRateCalculator (group56) resolved through the host.
        self.lending = self._build("lending", g.LendingCalculator)

        # Stage 4 - chain-bound components.
        bc = self.bc
        self.collector = self._build("collector", lambda: g.DailyMetricsCollector(bc))
        self.kpi = self._build("kpi", lambda: g.ProtocolKPITracker(bc))
        self.tokenomics = self._build("tokenomics", lambda: g.TokenomicsAnalysis(bc))
        self.health = self._build("health", lambda: g.NEBULAHealthScore(bc))
        self.status_page = self._build("status_page", lambda: g.NEBULAStatusPage(bc))
        self.sdk = self._build("sdk", self._make_sdk)

        # Stage 5 - lazy (need extra arguments); see contract_sdk() / block_template().
        self._contract_sdk: Any = None

    def _make_sdk(self) -> Any:
        """NebulaSDKPython.__init__ creates a brand-new NEBULABlockchain(), which
        would be a second, disconnected chain (and possibly a second database).
        Build the object without running __init__ and bind it to the node's chain."""
        sdk = g.NebulaSDKPython.__new__(g.NebulaSDKPython)
        sdk.rpc_url = g.NEBULAMainnetConfig.RPC_URL
        sdk._bc = self.bc
        return sdk

    # --------------------------------------------------------- lazy components
    def contract_sdk(self) -> Any:
        """NebulaContractSDK needs the node's ContractFactory. It is located by
        duck-typing on the node (deploy_erc20 + call_contract + get_contract)."""
        if self._contract_sdk is not None:
            return self._contract_sdk
        factory = self._find_contract_factory()
        if factory is None:
            self.component_errors["contract_sdk"] = "no ContractFactory found on node"
            return None
        self._contract_sdk = self._build(
            "contract_sdk", lambda: g.NebulaContractSDK(self.bc, factory))
        return self._contract_sdk

    def _find_contract_factory(self) -> Any:
        def looks_like_factory(obj: Any) -> bool:
            return all(callable(getattr(obj, m, None))
                       for m in ("deploy_erc20", "call_contract", "get_contract"))

        for name in ("contract_factory", "factory", "contracts"):
            obj = getattr(self.node, name, None)
            if obj is not None and looks_like_factory(obj):
                return obj
        try:
            for obj in vars(self.node).values():
                if looks_like_factory(obj):
                    return obj
        except TypeError:
            _NB_SWALLOW_LOG.debug("swallowed TypeError in Layer57._find_contract_factory", exc_info=True)
        return None

    def block_template(self, miner: str) -> dict:
        return g.EnhancedBlockTemplate(self.bc, miner).optimal_template()

    # ------------------------------------------------------- listener callbacks
    def on_connect(self, block: Any) -> None:
        """Called by the chain for every connected block. Report-only."""
        try:
            with self._lock:
                self.stats_["blocks_seen"] += 1
                seen = self.stats_["blocks_seen"]
                if seen == 1 or seen % self._snapshot_every == 0:
                    self.collect_snapshot()
        except Exception as exc:
            self._fail(exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        """Called on a chain reorganisation. Drops metric snapshots that belong
        to the abandoned branch so history stays consistent."""
        try:
            with self._lock:
                self.stats_["reorgs"] += 1
                self.stats_["last_reorg_ancestor"] = ancestor_height
                if self.collector is not None:
                    self.collector._data[:] = [
                        d for d in self.collector._data
                        if d.get("height", 0) <= ancestor_height
                    ]
        except Exception as exc:
            self._fail(exc)

    def _fail(self, exc: BaseException) -> None:
        self.errors += 1
        self.last_error = f"{type(exc).__name__}: {exc}"
        log.warning("group57 listener error: %s", exc)

    # --------------------------------------------------------------- snapshots
    def collect_snapshot(self) -> Optional[dict]:
        """Collect one metrics snapshot and feed the KPI tracker."""
        with self._lock:
            if self.collector is None:
                return None
            data = self.collector.collect()
            if len(self.collector._data) > MAX_SNAPSHOTS:
                del self.collector._data[:len(self.collector._data) - MAX_SNAPSHOTS]
            if self.kpi is not None:
                self.kpi.record("height", float(data["height"]))
                self.kpi.record("mempool", float(data["mempool"]))
                self.kpi.record("utxos", float(data["utxos"]))
                self.kpi.record("supply_nbl", float(data["supply"]) / 10 ** g.DECIMALS)
            self.stats_["snapshots"] += 1
            self.stats_["last_snapshot_height"] = data["height"]
            return data

    def _safe(self, fn: Callable[[], Any]) -> Any:
        try:
            return fn()
        except Exception as exc:
            self.errors += 1
            self.last_error = f"{type(exc).__name__}: {exc}"
            return {"error": self.last_error}

    def snapshot(self) -> dict:
        """Read-only view of all components. Never raises."""
        s = self._safe
        out: Dict[str, Any] = {
            "layer": {
                "errors": self.errors,
                "last_error": self.last_error,
                "component_errors": dict(self.component_errors),
                "stats": dict(self.stats_),
            },
            "mainnet_config": s(self.mainnet_config.to_dict),
            "testnet_config": s(self.testnet_config.to_dict),
        }
        if self.health:
            out["health"] = s(self.health.score)
        if self.tokenomics:
            out["tokenomics"] = s(self.tokenomics.scarcity_metrics)
        if self.status_page:
            out["status"] = s(self.status_page.status)
        if self.collector:
            out["metrics"] = list(self.collector._data[-7:])
            out["metrics_trend_height_pct"] = s(lambda: self.collector.trend("height"))
        if self.kpi:
            out["kpi"] = s(self.kpi.summary)
        if self.community:
            out["community"] = s(self.community.community_stats)
        if self.topology:
            out["topology"] = s(self.topology.topology_summary)
        if self.sdk:
            out["sdk"] = s(self.sdk.sdk_info)
        return out

    # ------------------------------------------------------------- REST (read-only)
    def api_get(self, path: str, query: Optional[Dict[str, Any]] = None) -> Tuple[int, dict]:
        """Read-only dispatcher: returns (http_status, json_dict). GET only.
        Hook it to the host's @route decorator or NEBULARPCHandler if you want it public."""
        query = query or {}
        try:
            handler = self._routes().get(path.rstrip("/") or "/")
            if handler is None:
                return 404, {"error": "unknown endpoint", "endpoints": sorted(self._routes())}
            return 200, handler(query)
        except _BadRequest as exc:
            return 400, {"error": str(exc)}
        except _Unavailable as exc:
            return 503, {"error": str(exc)}
        except ZeroDivisionError:
            return 400, {"error": "invalid combination of parameters"}
        except Exception as exc:
            self._fail(exc)
            return 500, {"error": "internal error"}

    def _need(self, obj: Any, name: str) -> Any:
        if obj is None:
            raise _Unavailable(f"component unavailable: {name}")
        return obj

    def _routes(self) -> Dict[str, Callable[[Dict[str, Any]], dict]]:
        P = API_PREFIX
        return {
            f"{P}/snapshot":      lambda q: self.snapshot(),
            f"{P}/health":        lambda q: self._need(self.health, "health").score(),
            f"{P}/tokenomics":    lambda q: self._need(self.tokenomics, "tokenomics").scarcity_metrics(),
            f"{P}/status":        self._r_status,
            f"{P}/metrics":       self._r_metrics,
            f"{P}/kpi":           lambda q: self._need(self.kpi, "kpi").summary(),
            f"{P}/community":     lambda q: self._need(self.community, "community").community_stats(),
            f"{P}/topology":      lambda q: self._need(self.topology, "topology").topology_summary(),
            f"{P}/sdk":           lambda q: self._need(self.sdk, "sdk").sdk_info(),
            f"{P}/config/mainnet": lambda q: self.mainnet_config.to_dict(),
            f"{P}/config/testnet": lambda q: self.testnet_config.to_dict(),
            f"{P}/whitepaper":    lambda q: {"abstract": self.whitepaper.get_abstract(),
                                             "citations": self.whitepaper.citations()},
            f"{P}/abi/erc20":     lambda q: {"abi": self.contract_abi.erc20_abi()},
            f"{P}/abi/staking":   lambda q: {"abi": self.contract_abi.staking_abi()},
            f"{P}/sdk/js-examples": lambda q: self.js_sdk_doc.usage_examples(),
            f"{P}/staking":       self._r_staking,
            f"{P}/staking/tiers": self._r_staking_tiers,
            f"{P}/lending/borrow": self._r_borrow,
            f"{P}/lending/supply": self._r_supply,
            f"{P}/pool/swap":     self._r_swap,
            f"{P}/pool/impermanent-loss": self._r_il,
            f"{P}/defi/health-factor": self._r_health_factor,
            f"{P}/yield":         self._r_yield,
            f"{P}/block-template": self._r_template,
        }

    # -- individual REST handlers -------------------------------------------
    def _r_status(self, q: Dict[str, Any]) -> dict:
        out = dict(self._need(self.status_page, "status_page").status())
        # The original class reports fixed values for these two fields.
        out["note"] = "services and uptime are static placeholders, not live measurements"
        return out

    def _r_metrics(self, q: Dict[str, Any]) -> dict:
        col = self._need(self.collector, "collector")
        with self._lock:
            return {"count": len(col._data), "latest": list(col._data[-30:]),
                    "trend_height_pct": col.trend("height"),
                    "trend_supply_pct": col.trend("supply")}

    def _r_staking(self, q: Dict[str, Any]) -> dict:
        calc = self._need(self.staking, "staking")
        amount = _num(q, "amount", lo=0.0, lo_exclusive=True)
        tier = _text(q, "tier", "90d", 16)
        if tier not in calc.APY_TIERS:
            raise _BadRequest("unknown tier; use one of: " + ", ".join(sorted(calc.APY_TIERS)))
        days = int(_num(q, "days", 90, lo=1, hi=MAX_QUERY_DAYS))
        return calc.calculate(amount, tier, days)

    def _r_staking_tiers(self, q: Dict[str, Any]) -> dict:
        calc = self._need(self.staking, "staking")
        amount = _num(q, "amount", 1000, lo=0.0, lo_exclusive=True)
        return {"tiers": calc.compare_tiers(amount)}

    def _r_borrow(self, q: Dict[str, Any]) -> dict:
        calc = self._need(self.lending, "lending")
        return calc.estimate_borrow_cost(
            _num(q, "amount", lo=0.0, lo_exclusive=True),
            _text(q, "asset", "NBL", 16),
            _num(q, "utilization", lo=0.0, hi=1.0),
            int(_num(q, "days", 30, lo=1, hi=MAX_QUERY_DAYS)))

    def _r_supply(self, q: Dict[str, Any]) -> dict:
        calc = self._need(self.lending, "lending")
        return calc.supply_yield_estimate(
            _num(q, "amount", lo=0.0, lo_exclusive=True),
            _num(q, "utilization", lo=0.0, hi=1.0),
            int(_num(q, "days", 30, lo=1, hi=MAX_QUERY_DAYS)))

    def _r_swap(self, q: Dict[str, Any]) -> dict:
        reserve_in = _num(q, "reserve_in", lo=0.0, lo_exclusive=True)
        reserve_out = _num(q, "reserve_out", lo=0.0, lo_exclusive=True)
        fee = _num(q, "fee", 0.003, lo=0.0, hi=0.5)
        out: Dict[str, Any] = {"k": self.pool_math.k_value(reserve_in, reserve_out)}
        if q.get("amount_in") is not None:
            amount_in = _num(q, "amount_in", lo=0.0, lo_exclusive=True)
            out["amount_out"] = self.pool_math.output_given_input(
                amount_in, reserve_in, reserve_out, fee)
        elif q.get("amount_out") is not None:
            amount_out = _num(q, "amount_out", lo=0.0, lo_exclusive=True)
            if amount_out >= reserve_out:
                raise _BadRequest("amount_out must be smaller than reserve_out")
            out["amount_in"] = self.pool_math.input_given_output(
                amount_out, reserve_in, reserve_out, fee)
        else:
            raise _BadRequest("provide amount_in or amount_out")
        return out

    def _r_il(self, q: Dict[str, Any]) -> dict:
        ratio = _num(q, "price_ratio", lo=0.0, lo_exclusive=True)
        return {"price_ratio": ratio,
                "impermanent_loss": self.pool_math.il_formula(ratio)}

    def _r_health_factor(self, q: Dict[str, Any]) -> dict:
        collateral = _num(q, "collateral_usd", lo=0.0)
        debt = _num(q, "debt_usd", lo=0.0)
        threshold = _num(q, "threshold", 0.8, lo=0.0, hi=1.0)
        hf = self.defi_math.health_factor(collateral, debt, threshold)
        return {"health_factor": None if math.isinf(hf) else hf,
                "no_debt": math.isinf(hf)}

    def _r_yield(self, q: Dict[str, Any]) -> dict:
        principal = _num(q, "principal", lo=0.0, lo_exclusive=True)
        apy = _num(q, "apy", lo=0.0, hi=100.0)
        fee = _num(q, "fee_pct", 0.02, lo=0.0, hi=1.0)
        ttd = self.yield_math.time_to_double(apy)
        return {
            "daily": self.yield_math.daily_yield(principal, apy),
            "weekly": self.yield_math.weekly_yield(principal, apy),
            "monthly": self.yield_math.monthly_yield(principal, apy),
            "years_to_double": None if math.isinf(ttd) else ttd,
            "effective_apy_with_fees": self.yield_math.effective_apy_with_fees(apy, fee),
        }

    def _r_template(self, q: Dict[str, Any]) -> dict:
        out = dict(self.block_template(_text(q, "miner")))
        # The original class sums transaction OUTPUTS, not real fees.
        out["note"] = "'fees' sums transaction outputs (original behaviour), not true fees"
        return out

    # ------------------------------------------------------------------ detach
    def detach(self) -> None:
        """Remove this layer from the chain's listener list."""
        try:
            remover = getattr(self.bc, "remove_listener", None)
            if callable(remover):
                remover(self)
            else:
                self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer57.detach", exc_info=True)
        self._attached = False
        _LIVE_LAYERS.discard(self)


class _Unavailable(RuntimeError):
    """A component could not be built (maps to HTTP 503)."""


# ---------------------------------------------------------------------------
# install / uninstall  (wrapper around NEBULAFullNode.__init__)
# ---------------------------------------------------------------------------
def install(host: Any, snapshot_every: int = SNAPSHOT_EVERY_N_BLOCKS) -> bool:
    """Patch host.NEBULAFullNode so every new node gets `node.group57`.
    Safe to call twice. Returns True if it patched, False if already installed."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g57_orig", None) is not None:
        return False
    orig = cls.__init__

    def patched(self, *args, **kwargs):
        orig(self, *args, **kwargs)           # the original node always starts first
        try:
            layer = Layer57(self, snapshot_every=snapshot_every)
            self.bc.add_listener(layer)
            layer._attached = True
            self.group57 = layer
        except Exception as exc:              # the node must still start
            self.group57_error = exc
            log.warning("group57 install failed on node: %s", exc)

    patched.__wrapped__ = orig
    patched.__name__ = getattr(orig, "__name__", "__init__")
    patched.__doc__ = getattr(orig, "__doc__", None)
    cls._g57_orig = orig
    cls.__init__ = patched
    return True


def uninstall(host: Any) -> bool:
    """Restore the original __init__ and detach layers from live nodes."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g57_orig", None)
    if orig is None:
        return False
    cls.__init__ = orig
    del cls._g57_orig
    for layer in list(_LIVE_LAYERS):
        layer.detach()
    return True
