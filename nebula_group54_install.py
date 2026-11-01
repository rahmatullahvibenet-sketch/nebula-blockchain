"""NEBULA group54 - wiring layer (install / uninstall).

Style follows the group5 pattern:
  * nothing inside nebula_v10_11.py is edited;
  * the layer NEVER rejects a block / tx - every callback is wrapped in try/except,
    failures are counted in layer.errors (details in layer.error_log);
  * the first day is "report-only": the layer only records counters/stats.

Usage (from a launcher, NOT by editing the host):

    import nebula_v10_11 as host
    import nebula_group54_install as g54
    g54.install(host)           # every NEBULAFullNode created afterwards gets node.group54
    ...
    g54.uninstall(host)         # restores the original __init__ and detaches live layers

Assumptions about the host (from the group54 guide; verify them against the real file):
  node.bc                      -> NEBULABlockchain
  bc.add_listener(obj)         -> obj.on_connect(block) / obj.on_reorg(old, new, ancestor_height)
  bc.height, bc.mempool.size(), bc.utxo.size()/total_supply()/balance(addr)
"""
from __future__ import annotations

import logging
import threading
import time
import weakref
from collections import deque
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

_log = logging.getLogger("nebula.group54")

# ---- tunables (report-only defaults) ---------------------------------------
SNAPSHOT_EVERY_BLOCKS = 6        # NetworkStatsV2.snapshot()
HEALTH_EVERY_BLOCKS = 10         # EcosystemHealthMonitor.auto_record()
LIQ_SCAN_EVERY_BLOCKS = 10       # LendingLiquidationBot.scan_positions()  (scan only)
STAKING_ACCRUE_EVERY = 144       # MultiAssetStaking.accrue_rewards(): its formula is "per day" (144 blocks)
CAP_SNAPSHOTS = 1000             # RAM caps for the unbounded lists inside the group classes
CAP_SIGNALS = 2000
CAP_EVENT_HISTORY = 5000
CAP_MESSAGES = 10000

# where to look for optional dependencies on the node (first non-None wins).
# These names are GUESSES - pass explicit objects with install(host, dex=..., ...) if yours differ.
_DEP_CANDIDATES = {
    "dex":     ("dex", "nebula_dex", "amm"),
    "oracle":  ("oracle", "oracle_v2", "price_oracle"),
    "lending": ("lending", "lending_protocol"),
    "staking": ("staking", "staking_engine"),
    "p2p":     ("p2p", "network", "net", "p2p_node"),
}

# stats method per service (used by report(), read-only)
_STATS = {
    "incentives":        "incentive_stats",
    "xchain":            "hub_stats",
    "delegation":        "delegation_v2_stats",
    "passport":          "passport_v2_stats",
    "storage":           "storage_v2_stats",
    "mining":            "mining_stats",
    "validator_metrics": "metrics_stats",
    "multi_staking":     "multi_staking_stats",
    "liq_bot":           "bot_stats",
    "composer":          "composability_v3_stats",
    "events":            "emitter_stats",
    "rewards":           "rewards_v3_stats",
    "revenue":           "revenue_report",
}


def _group():
    import nebula_group54 as g
    return g


def _bind_host(g, host) -> None:
    """Make group54 use the LIVE host classes for the 3 cross-group names
    (ContractState, NEBULAWallet, Secp256k1). Needed when the host runs as __main__ or was
    imported before group54, so group54 does not keep a second copy of them."""
    for name in ("ContractState", "NEBULAWallet", "Secp256k1"):
        if hasattr(host, name):
            setattr(g, name, getattr(host, name))


def _trim(lst, cap: int) -> None:
    if isinstance(lst, list) and len(lst) > cap:
        lst[:] = lst[-cap:]


class Layer54:
    """Holds one instance of every group54 service class and feeds them from chain callbacks."""

    NAME = "group54"

    def __init__(self, node, group=None, **deps):
        self.node = node
        self.bc = node.bc
        self.g = group or _group()
        self._lock = threading.RLock()
        self.errors = 0
        self.error_log = deque(maxlen=50)
        self.detached = False
        self.blocks_seen = 0
        self.reorgs_seen = 0
        self.last_height = -1
        self.last_health = None
        self.last_liq_scan = []
        self._last_accrue_height = 0
        self.init_errors = {}      # service -> repr(exception) if its constructor failed
        self.skipped = {}          # service -> reason (missing dependency)
        self.contracts = {}        # contract_id -> SmartContractV3

        # optional dependencies: explicit > auto-detected on the node
        self.deps = {}
        for key, names in _DEP_CANDIDATES.items():
            obj = deps.get(key)
            if obj is None:
                for n in names:
                    obj = getattr(node, n, None)
                    if obj is not None:
                        break
            self.deps[key] = obj

        self._build()

    # ------------------------------------------------------------------ build
    def _make(self, attr, factory, needs=()):
        setattr(self, attr, None)
        missing = [n for n in needs if self.deps.get(n) is None]
        if missing:
            self.skipped[attr] = "missing dependency: " + ",".join(missing)
            return
        try:
            setattr(self, attr, factory())
        except Exception as e:                       # node must still start
            self.init_errors[attr] = repr(e)
            _log.warning("group54: %s failed to build: %r", attr, e)

    def _build(self):
        g, bc, d = self.g, self.bc, self.deps
        miner_addr = (getattr(self.node, "miner_address", None)
                      or getattr(self.node, "address", None) or "unassigned")
        self._make("incentives",        lambda: g.LiquidityIncentiveProgram(bc, d["dex"]), ("dex",))
        self._make("xchain",            lambda: g.CrossChainMessageHub(bc))
        self._make("delegation",        lambda: g.ValidatorDelegationV2(bc))
        self._make("passport",          lambda: g.DeFiPassportV2(bc))
        self._make("storage",           lambda: g.OnChainStorageV2(bc))
        self._make("mining",            lambda: g.AdvancedMiningEngine(bc, str(miner_addr)))
        self._make("netstats",          lambda: g.NetworkStatsV2(bc, d["p2p"]))
        self._make("defi_positions",    lambda: g.DeFiPositionsV2(bc, d["oracle"]))
        self._make("validator_metrics", lambda: g.ValidatorMetrics(bc))
        self._make("multi_staking",     lambda: g.MultiAssetStaking(bc, d["oracle"]))
        self._make("benchmark",         lambda: g.ProtocolBenchmark(bc))
        self._make("liq_bot",           lambda: g.LendingLiquidationBot(bc, d["lending"], d["oracle"]))
        self._make("composer",          lambda: g.ComposabilityEngineV3(bc))
        self._make("health",            lambda: g.EcosystemHealthMonitor(bc))
        self._make("events",            lambda: g.ChainEventEmitterV2(bc))
        self._make("rewards",           lambda: g.RewardsEngineV3(bc))
        self._make("revenue",           lambda: g.ProtocolRevenue(bc))

    # ----------------------------------------------------------------- guards
    def _fail(self, where, exc):
        self.errors += 1
        self.error_log.append((time.time(), where, repr(exc)))
        _log.warning("group54 %s failed: %r", where, exc)

    def _guard(self, where, fn, *a, **k):
        try:
            return fn(*a, **k)
        except Exception as e:
            self._fail(where, e)
            return None

    def _height(self):
        return int(getattr(self.bc, "height", 0))

    # -------------------------------------------------------------- listeners
    def on_connect(self, block):
        if self.detached:
            return
        try:
            with self._lock:
                self._on_connect(block)
        except Exception as e:                       # never propagate into the host
            self._fail("on_connect", e)

    def _on_connect(self, block):
        h = self._height()
        self.blocks_seen += 1
        self.last_height = h
        g = self.g

        if self.events:
            self._guard("events.emit", self.events.emit, g.ChainEvent.BLOCK_MINED,
                        {"height": h, "hash": self._block_hash(block)})
            self._guard("events.special", self.events.check_special_events)

        if self.netstats and h % SNAPSHOT_EVERY_BLOCKS == 0:
            self._guard("netstats.snapshot", self.netstats.snapshot)

        if self.health and h % HEALTH_EVERY_BLOCKS == 0:
            self.last_health = self._guard("health.auto_record", self.health.auto_record)

        if self.liq_bot and h % LIQ_SCAN_EVERY_BLOCKS == 0:
            # scan only. execute_liquidations() in group54 just bumps counters (it liquidates nothing),
            # so it is deliberately NOT called automatically.
            r = self._guard("liq_bot.scan", self.liq_bot.scan_positions)
            if r is not None:
                self.last_liq_scan = r

        if self.multi_staking and h > 0 and h % STAKING_ACCRUE_EVERY == 0 \
                and h > self._last_accrue_height:
            self._guard("multi_staking.accrue", self.multi_staking.accrue_rewards)
            self._last_accrue_height = h

        if self.incentives:
            self._guard("incentives.allocate", self.incentives.allocate_weekly)

        if self.validator_metrics:
            self._guard("validator_metrics.feed", self._feed_validator_metrics, block)

        self._trim_all()

    def on_reorg(self, old, new, ancestor_height):
        if self.detached:
            return
        try:
            with self._lock:
                self.reorgs_seen += 1
                try:
                    anc = int(ancestor_height)
                except Exception:
                    anc = self._height()
                self._last_accrue_height = min(self._last_accrue_height, anc)
                if self.incentives is not None:      # keep the weekly window valid after height went back
                    ws = getattr(self.incentives, "_week_start", None)
                    if isinstance(ws, int) and ws > anc:
                        self._guard("incentives.reorg", setattr, self.incentives, "_week_start", anc)
        except Exception as e:
            self._fail("on_reorg", e)

    # ---------------------------------------------------------------- helpers
    @staticmethod
    def _block_hash(block):
        for attr in ("hash", "block_hash"):
            v = getattr(block, attr, None)
            if callable(v):
                try:
                    v = v()
                except Exception:
                    v = None
            if v is not None:
                return v.hex() if isinstance(v, (bytes, bytearray)) else str(v)
        return None

    def _feed_validator_metrics(self, block):
        """Only if the block exposes a miner address (PoW chains often do not)."""
        miner = None
        for attr in ("miner", "miner_address", "coinbase_address"):
            miner = getattr(block, attr, None) or getattr(getattr(block, "header", None), attr, None)
            if miner:
                break
        if not miner:
            return
        size = 0
        ser = getattr(block, "serialize", None)
        if callable(ser):
            try:
                size = len(ser())
            except Exception:
                size = 0
        ts = getattr(getattr(block, "header", None), "timestamp", None)
        lat = 0.0
        if isinstance(ts, (int, float)):
            lat = min(max(0.0, (time.time() - ts) * 1000.0), 600_000.0)
        self.validator_metrics.record_block(str(miner), lat, size)

    def _trim_all(self):
        if self.netstats:
            _trim(getattr(self.netstats, "_snapshots", None), CAP_SNAPSHOTS)
        if self.health:
            _trim(getattr(self.health, "_signals", None), CAP_SIGNALS)
        if self.events:
            _trim(getattr(self.events, "_history", None), CAP_EVENT_HISTORY)
        if self.xchain:
            _trim(getattr(self.xchain, "_inbox", None), CAP_MESSAGES)
            _trim(getattr(self.xchain, "_outbox", None), CAP_MESSAGES)
        if self.revenue:
            _trim(getattr(self.revenue, "_history", None), CAP_EVENT_HISTORY)

    # ------------------------------------------------------- on-demand helpers
    def deploy_contract(self, contract_id, owner):
        """SmartContractV3 is per-contract; this keeps them in layer.contracts."""
        with self._lock:
            if contract_id in self.contracts:
                return self.contracts[contract_id]
            c = self.g.SmartContractV3(contract_id, owner, self.bc)
            self.contracts[contract_id] = c
            return c

    def run_strategy(self, user, strategy, amount_nbl):
        if not self.composer:
            return {"ok": False, "error": "composer not available"}
        return self.composer.execute_strategy(user, strategy, amount_nbl,
                                              dex=self.deps.get("dex"),
                                              staking=self.deps.get("staking"))

    def run_benchmark(self):
        """Heavy + prints to stdout: never called automatically."""
        if not self.benchmark:
            return {}
        return self._guard("benchmark", self.benchmark.run_all_benchmarks) or {}

    # ----------------------------------------------------------------- report
    def report(self):
        """Read-only status snapshot."""
        out = {
            "errors": self.errors,
            "blocks_seen": self.blocks_seen,
            "reorgs_seen": self.reorgs_seen,
            "last_height": self.last_height,
            "last_health": self.last_health,
            "contracts": len(self.contracts),
            "skipped": dict(self.skipped),
            "init_errors": dict(self.init_errors),
            "deps_found": {k: v is not None for k, v in self.deps.items()},
            "services": {},
        }
        for attr, meth in _STATS.items():
            svc = getattr(self, attr, None)
            if svc is not None:
                out["services"][attr] = self._guard("report." + attr, getattr(svc, meth))
        return out

    def detach(self):
        self.detached = True
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer54.detach", exc_info=True)
        rm = getattr(self.bc, "remove_listener", None)
        if callable(rm):
            try:
                rm(self)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in Layer54.detach", exc_info=True)


# ------------------------------------------------------------------ install
_LIVE = weakref.WeakSet()


def install(host, **deps):
    """Wrap NEBULAFullNode.__init__ so each new node gets node.group54 (idempotent)."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g54_orig", None):
        return
    g = _group()
    _bind_host(g, host)
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)                          # the original always runs first
        try:
            layer = Layer54(self, group=g, **deps)
            self.group54 = layer
            self.bc.add_listener(layer)
            _LIVE.add(layer)
        except Exception as e:                       # the node must still start
            self.group54_error = e
            _log.warning("group54 install failed for node: %r", e)

    patched.__wrapped__ = orig
    cls._g54_orig = orig
    cls.__init__ = patched


def uninstall(host):
    cls = host.NEBULAFullNode
    o = getattr(cls, "_g54_orig", None)
    for layer in list(_LIVE):
        try:
            layer.detach()
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in uninstall", exc_info=True)
    if o:
        cls.__init__ = o
        del cls._g54_orig
