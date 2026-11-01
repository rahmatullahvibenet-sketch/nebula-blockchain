#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nebula_group27_install.py
=========================

Wiring layer for the 20 previously-dead classes in ``nebula_group27.py``.

NOTHING inside ``nebula_v10_11.py`` is edited.  Everything is attached from
the outside, exactly like the group-5 installer:

    import nebula_v10_11 as host
    import nebula_group27_install as g27
    g27.install(host)          # patches NEBULAFullNode.__init__ (+ Mempool.submit, observe-only)
    ...
    g27.uninstall(host)        # restores the original behaviour completely

Safety contract (the same one the guide demands)
------------------------------------------------
* The layer NEVER rejects a block or a transaction.
* Every callback is wrapped in try/except; failures are counted in
  ``layer.errors`` and described in ``layer.error_log``.
* Validation / clock / signature code is REPORT-ONLY (findings, no vetoes).
* All growing collections are capped (no unbounded RAM growth).
* Heavy work (on-chain metrics, exports, full-chain validation, self-tests)
  runs only ON DEMAND, never inside the block-connect hot path.

Where each of the 20 classes is wired
-------------------------------------
    #   class                role in Layer27                      attribute
    --  -------------------  -----------------------------------  ----------------
     1  BatchProcessor       service (+ periodic job cleanup)     layer.batch
     2  NEBULAComplete       LAZY, opt-in facade (see warning)    layer.facade()
     3  OnChainMetric        data type produced by #4             layer.metrics()
     4  ChainMetricsEngine   on-demand metrics (TTL cached)       layer.metrics_engine
     5  TxAccelerator        service + Mempool.submit observer    layer.accelerator
     6  DataExporter         on-demand exports                    layer.exporter
     7  ContractMath         contract utility                     layer.math
     8  EventEmitter         receives BlockConnected/Reorg events layer.events
     9  AccessControl        roles for the layer's system contract layer.access
    10  StandardContract     system contract (events + roles)     layer.contract
    11  TestCase             data type used by #14                layer.tests
    12  TestResult           data type produced by #14            layer.tests
    13  NEBULAAssert         assertion helpers for self-tests     layer.asserts
    14  TestRunner           self-test runner                     layer.tests
    15  PropertyTest         property tests (on demand)           layer.properties
    16  MedianTimePast       BIP113 helper (used by #17)          layer.mtp
    17  ChainClock           per-block timestamp check (report)   layer.clock
    18  SignatureAggregator  security helper (report-only)        layer.sig_aggregator
    19  FullChainValidator   per-block header/merkle/reward check layer.validator
    20  MempoolAlert         data type for mempool alerts         layer.mempool_alerts

WARNINGS (read these)
---------------------
1. ``NEBULAComplete.__init__`` builds a SECOND ``NEBULABlockchain`` plus ~60
   services, and ``quick_start`` opens RPC/API/Explorer ports and a mining
   loop.  That would collide with the running node, so it is NOT created
   automatically.  ``layer.facade()`` creates it only when
   ``Layer27Config.allow_complete_facade`` is True.
2. ``SignatureAggregator.verify_half_aggregate`` always returns True (the
   original code is a stub: "simplified; full impl would check point
   equation").  It must never be used as a security decision.  The layer only
   exposes ``batch_verify`` (real, sequential Schnorr.verify) and the size
   estimator, and never uses them to accept or reject anything.
3. ``MedianTimePast.validate_sequence`` (time-based branch) is documented as
   "simplified" in the original code; it is not used by the layer's hooks.
"""
from __future__ import annotations

import argparse
import functools
import importlib
import logging
import sys
import threading
import time
import weakref
from collections import deque
from dataclasses import dataclass
from typing import Any, Callable, Deque, Dict, List, Optional, Tuple
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group27")

# --------------------------------------------------------------------------
# Lazy loader for the group module (so the offline self-test can inject a
# stub host before nebula_group27 imports it).
# --------------------------------------------------------------------------
_GROUP_MODULE = None


def _load_group():
    """Import nebula_group27 once and return the module."""
    global _GROUP_MODULE
    if _GROUP_MODULE is None:
        _GROUP_MODULE = importlib.import_module("nebula_group27")
    return _GROUP_MODULE


# --------------------------------------------------------------------------
# Registry of live layers (so uninstall() can detach every one of them).
# --------------------------------------------------------------------------
_LIVE_LAYERS: "weakref.WeakSet[Layer27]" = weakref.WeakSet()


# --------------------------------------------------------------------------
# The 20 classes and how each is wired (used by coverage()).
#   kind:  "instance" -> layer.<attr> must be an instance of the class
#          "static"   -> layer.<attr> holds the class (all-static helper)
#          "data"     -> plain data type; proven by the producing component
#          "lazy"     -> intentionally NOT created automatically
# --------------------------------------------------------------------------
CLASS_ROLES: Dict[str, Tuple[str, Optional[str], str]] = {
    "BatchProcessor":      ("instance", "batch",           "service + periodic cleanup"),
    "NEBULAComplete":      ("lazy",     None,              "opt-in facade via layer.facade()"),
    "OnChainMetric":       ("data",     "metrics_engine",  "produced by ChainMetricsEngine"),
    "ChainMetricsEngine":  ("instance", "metrics_engine",  "on-demand metrics"),
    "TxAccelerator":       ("instance", "accelerator",     "service + submit observer"),
    "DataExporter":        ("instance", "exporter",        "on-demand exports"),
    "ContractMath":        ("instance", "math",            "contract utility"),
    "EventEmitter":        ("instance", "events",          "block/reorg events"),
    "AccessControl":       ("instance", "access",          "layer-level roles"),
    "StandardContract":    ("instance", "contract",        "system contract"),
    "TestCase":            ("data",     "tests",           "registered in TestRunner"),
    "TestResult":          ("data",     "tests",           "produced by TestRunner"),
    "NEBULAAssert":        ("static",   "asserts",         "self-test assertions"),
    "TestRunner":          ("instance", "tests",           "self-test runner"),
    "PropertyTest":        ("static",   "properties",      "on-demand property tests"),
    "MedianTimePast":      ("static",   "mtp",             "BIP113 helper"),
    "ChainClock":          ("instance", "clock",           "timestamp checks (report-only)"),
    "SignatureAggregator": ("static",   "sig_aggregator",  "security helper (report-only)"),
    "FullChainValidator":  ("instance", "validator",       "block checks (report-only)"),
    "MempoolAlert":        ("data",     "mempool_alerts",  "mempool alert records"),
}


# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------
@dataclass
class Layer27Config:
    """All tunables of the layer.  Defaults are conservative / observe-only."""

    # --- per-block checks (all report-only) ---
    check_clock: bool = True                 # ChainClock + MedianTimePast per block
    check_blocks: bool = True                # FullChainValidator header/merkle/reward per block
    validate_every: int = 1                  # run block checks every N blocks (1 = every block)

    # --- housekeeping ---
    cleanup_every_blocks: int = 100          # BatchProcessor.cleanup_old_jobs cadence
    job_max_age_secs: float = 3600.0         # age limit for finished batch jobs

    # --- mempool monitoring (MempoolAlert) ---
    mempool_alert_size: int = 5000           # alert when mempool holds more txs than this
    mempool_alert_cooldown_secs: float = 300.0

    # --- caps (memory safety) ---
    max_events: int = 1000                   # EventEmitter history length
    max_findings: int = 500                  # clock / validation findings kept
    max_mempool_alerts: int = 200
    max_error_log: int = 100
    max_validator_errors: int = 1000         # FullChainValidator._errors / _warnings length

    # --- on-demand metrics ---
    metrics_ttl_secs: float = 60.0           # cache lifetime of layer.metrics()

    # --- contract identity (not consensus data) ---
    contract_owner: Optional[str] = None     # default: group27.FOUNDATION_ADDRESS
    contract_address: str = "NEBULA_LAYER27_SYSTEM"

    # --- dangerous opt-ins ---
    allow_complete_facade: bool = False      # permit layer.facade() (builds a 2nd blockchain!)
    observe_mempool: bool = True             # wrap Mempool.submit (observe-only)


# --------------------------------------------------------------------------
# Small helper: a read-only view of a chain that looks like a blockchain to
# MedianTimePast / ChainClock (they only read ``_chain``).
# --------------------------------------------------------------------------
class _ChainView:
    """Minimal blockchain look-alike exposing ``_chain`` (and height/tip)."""

    def __init__(self, blocks: List[Any]):
        self._chain = blocks

    @property
    def height(self) -> int:
        return len(self._chain) - 1

    @property
    def tip(self) -> Any:
        return self._chain[-1]


# ==========================================================================
#                                Layer27
# ==========================================================================
class Layer27:
    """
    Chain listener + service container for the 20 group-27 classes.

    The blockchain calls (see guide, step 3):
        layer.on_connect(block)
        layer.on_reorg(old, new, ancestor_height)
    """

    def __init__(self, node: Any, config: Optional[Layer27Config] = None,
                 group_module: Any = None):
        self.node = node
        self.bc = getattr(node, "bc", None)
        if self.bc is None:
            raise RuntimeError("Layer27: node has no .bc (blockchain) attribute")
        self.cfg = config or Layer27Config()
        self.g = group_module or _load_group()

        # ---- bookkeeping ----
        self._lock = threading.RLock()
        self.started_at = time.time()
        self.errors = 0
        self.error_log: Deque[str] = deque(maxlen=self.cfg.max_error_log)
        self.build_errors: Dict[str, str] = {}
        self.findings: Deque[dict] = deque(maxlen=self.cfg.max_findings)
        self.mempool_alerts: Deque[Any] = deque(maxlen=self.cfg.max_mempool_alerts)
        self._last_mempool_alert = 0.0

        self.blocks_seen = 0
        self.reorgs_seen = 0
        self.last_height = -1
        self.last_reorg: Optional[dict] = None
        self.clock_violations = 0
        self.block_check_failures = 0
        self.submit_calls = 0
        self.submit_accepted = 0
        self.submit_rejected = 0

        self._metrics_cache: Optional[Tuple[float, List[dict]]] = None
        self._metrics_objects: Dict[str, Any] = {}
        self._facade = None
        self._attached_mempool = None
        self._detached = False

        # ---- components ----
        self.batch = None
        self.metrics_engine = None
        self.accelerator = None
        self.exporter = None
        self.math = None
        self.events = None
        self.access = None
        self.contract = None
        self.tests = None
        self.clock = None
        self.validator = None
        self.asserts = None
        self.properties = None
        self.mtp = None
        self.sig_aggregator = None
        self._build_components()
        self._register_self_tests()
        self._attach_mempool()
        _LIVE_LAYERS.add(self)

    # ------------------------------------------------------------------
    # internal helpers
    # ------------------------------------------------------------------
    def _fail(self, where: str, exc: BaseException) -> None:
        """Record a failure.  Never raises."""
        try:
            with self._lock:
                self.errors += 1
                self.error_log.append(f"{where}: {type(exc).__name__}: {exc}")
            log.warning("group27 %s failed: %s: %s", where, type(exc).__name__, exc)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer27._fail", exc_info=True)

    def _finding(self, kind: str, height: int, message: str) -> None:
        with self._lock:
            self.findings.append({
                "kind": kind, "height": height,
                "message": message, "time": time.time(),
            })

    def _make(self, attr: str, factory: Callable[[], Any]) -> None:
        """Build one component; on failure keep the node alive and record why."""
        try:
            setattr(self, attr, factory())
        except Exception as exc:
            setattr(self, attr, None)
            self.build_errors[attr] = f"{type(exc).__name__}: {exc}"
            self._fail(f"build:{attr}", exc)

    # ------------------------------------------------------------------
    # component construction (guide step 4 order: independent ones first)
    # ------------------------------------------------------------------
    def _build_components(self) -> None:
        g, bc, node, cfg = self.g, self.bc, self.node, self.cfg
        oracle = getattr(node, "oracle", None)
        fee_bumper = getattr(node, "fee_bumper", None)
        owner = cfg.contract_owner or getattr(g, "FOUNDATION_ADDRESS", "NEBULA_OWNER")

        # -- 1) static helpers / data holders (no node access needed) --
        self._make("math", lambda: g.ContractMath())
        self._make("asserts", lambda: g.NEBULAAssert)
        self._make("properties", lambda: g.PropertyTest)
        self._make("mtp", lambda: g.MedianTimePast)
        self._make("sig_aggregator", lambda: g.SignatureAggregator)
        self._make("events", lambda: g.EventEmitter())
        self._make("access", lambda: g.AccessControl(owner))
        self._make("contract", lambda: g.StandardContract(cfg.contract_address, owner))
        self._make("tests", lambda: g.TestRunner("NEBULA group27 self-tests"))

        # -- 2) blockchain-bound services --
        self._make("clock", lambda: g.ChainClock(bc))
        self._make("validator", lambda: g.FullChainValidator(bc))
        self._make("metrics_engine", lambda: g.ChainMetricsEngine(bc, oracle))
        self._make("exporter", lambda: g.DataExporter(bc, oracle))
        self._make("accelerator", lambda: g.TxAccelerator(bc, fee_bumper))
        self._make("batch", lambda: g.BatchProcessor(bc))

        # The system contract owner may pause/unpause its own contract.
        if self.access is not None:
            try:
                self.access.grant_role(self.g.AccessControl.PAUSER_ROLE, owner, owner)
            except Exception as exc:
                self._fail("build:pauser_role", exc)

    # ------------------------------------------------------------------
    # Mempool observation (data comes from Mempool.submit wrapper)
    # ------------------------------------------------------------------
    def _attach_mempool(self) -> None:
        if not self.cfg.observe_mempool:
            return
        try:
            mp = getattr(self.bc, "mempool", None)
            if mp is not None:
                mp._g27_layer = self          # read by the Mempool.submit wrapper
                self._attached_mempool = mp
        except Exception as exc:
            self._fail("attach_mempool", exc)

    def observe_submit(self, result: Any) -> None:
        """Called by the Mempool.submit wrapper AFTER the original ran."""
        try:
            ok = bool(result[0]) if isinstance(result, tuple) and result else bool(result)
            with self._lock:
                self.submit_calls += 1
                if ok:
                    self.submit_accepted += 1
                else:
                    self.submit_rejected += 1
        except Exception as exc:
            self._fail("observe_submit", exc)

    # ------------------------------------------------------------------
    # CHAIN LISTENER API
    # ------------------------------------------------------------------
    def on_connect(self, block: Any) -> None:
        """A block was connected.  Never raises, never vetoes."""
        height = getattr(block, "height", -1)
        with self._lock:
            self.blocks_seen += 1
            self.last_height = height
            seen = self.blocks_seen

        self._step(self._emit_connect_event, block, height, name="emit_connect_event")

        if seen % max(1, self.cfg.validate_every) == 0:
            if self.cfg.check_clock:
                self._step(self._check_clock, block, height, name="check_clock")
            if self.cfg.check_blocks:
                self._step(self._check_block, block, height, name="check_block")

        self._step(self._check_mempool, height, name="check_mempool")

        if seen % max(1, self.cfg.cleanup_every_blocks) == 0:
            self._step(self._housekeeping, name="housekeeping")

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        """A reorg happened.  Never raises."""
        try:
            n_old = len(old) if old is not None else 0
            n_new = len(new) if new is not None else 0
        except Exception:
            n_old = n_new = -1
        with self._lock:
            self.reorgs_seen += 1
            self.last_reorg = {
                "ancestor_height": ancestor_height,
                "old_blocks": n_old, "new_blocks": n_new,
                "time": time.time(),
            }
        self._step(self._emit_reorg_event, ancestor_height, n_old, n_new,
                   name="emit_reorg_event")
        # The old error list described blocks that may no longer exist.
        self._step(self._reset_validator_errors, name="reset_validator_errors")

    def detach(self) -> None:
        """Remove this layer from the blockchain's listener list."""
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer27.detach", exc_info=True)
        try:
            if self._attached_mempool is not None and \
                    getattr(self._attached_mempool, "_g27_layer", None) is self:
                del self._attached_mempool._g27_layer
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer27.detach", exc_info=True)
        self._attached_mempool = None
        self._detached = True

    def _step(self, fn: Callable, *args, name: str = "step") -> None:
        """Run one hook step; contain every exception."""
        try:
            fn(*args)
        except Exception as exc:
            self._fail(name, exc)

    # ------------------------------------------------------------------
    # per-block steps
    # ------------------------------------------------------------------
    def _emit_connect_event(self, block: Any, height: int) -> None:
        if self.events is None:
            return
        self.events.emit(self.cfg.contract_address, "BlockConnected",
                         {"height": height,
                          "txs": len(getattr(block, "transactions", []) or [])},
                         height=height, tx_hash=str(getattr(block, "hash", "")))
        self._trim_events()

    def _emit_reorg_event(self, ancestor: int, n_old: int, n_new: int) -> None:
        if self.events is None:
            return
        self.events.emit(self.cfg.contract_address, "Reorg",
                         {"ancestor_height": ancestor,
                          "old_blocks": n_old, "new_blocks": n_new},
                         height=ancestor)
        self._trim_events()

    def _trim_events(self) -> None:
        cap = self.cfg.max_events
        with self._lock:
            ev = self.events._events
            if len(ev) > cap:
                del ev[:-cap]

    def _check_clock(self, block: Any, height: int) -> None:
        """
        ChainClock.validate_timestamp compares against the MTP of
        ``bc._chain``.  The new block is already inside the chain here, so
        we evaluate it against a view WITHOUT the new block (otherwise the
        block would be judged against itself).
        """
        if self.clock is None:
            return
        chain = list(self.bc._chain[-13:])
        if len(chain) < 2:
            return
        if getattr(chain[-1], "hash", None) != getattr(block, "hash", None):
            return                                # tip moved on; skip safely
        previous = chain[:-1]
        ts = int(block.header.timestamp)
        prev_ts = int(previous[-1].header.timestamp)
        ok, msg = self.g.ChainClock(_ChainView(previous)).validate_timestamp(ts, prev_ts)
        if not ok:
            with self._lock:
                self.clock_violations += 1
            self._finding("clock", height, msg)

    def _check_block(self, block: Any, height: int) -> None:
        """Report-only header / merkle / reward checks via FullChainValidator."""
        v = self.validator
        if v is None:
            return
        problems: List[str] = []
        for fn in (v.validate_header, v.validate_merkle_root, v.validate_reward):
            ok, msg = fn(block)
            if not ok:
                problems.append(msg)
        if problems:
            with self._lock:
                self.block_check_failures += 1
            for msg in problems:
                self._finding("block", height, msg)
        self._trim_validator()

    def _trim_validator(self) -> None:
        v, cap = self.validator, self.cfg.max_validator_errors
        if v is None:
            return
        with v._lock:
            if len(v._errors) > cap:
                del v._errors[:-cap]
            if len(v._warnings) > cap:
                del v._warnings[:-cap]

    def _reset_validator_errors(self) -> None:
        v = self.validator
        if v is None:
            return
        with v._lock:
            v._errors.clear()
            v._warnings.clear()

    def _check_mempool(self, height: int) -> None:
        mp = getattr(self.bc, "mempool", None)
        if mp is None:
            return
        size = mp.size()
        if size <= self.cfg.mempool_alert_size:
            return
        now = time.time()
        with self._lock:
            if now - self._last_mempool_alert < self.cfg.mempool_alert_cooldown_secs:
                return
            self._last_mempool_alert = now
            self.mempool_alerts.append(self.g.MempoolAlert(
                alert_type="size", severity="warning",
                message=f"Mempool holds {size} txs at height {height}",
                value=float(size)))

    def _housekeeping(self) -> None:
        if self.batch is not None:
            self.batch.cleanup_old_jobs(self.cfg.job_max_age_secs)

    # ------------------------------------------------------------------
    # ON-DEMAND API (never called from the hot path)
    # ------------------------------------------------------------------
    def metrics(self, force: bool = False) -> List[dict]:
        """
        All on-chain metrics as dicts (TTL cached).  Also keeps the
        OnChainMetric objects in ``layer.metric_objects`` and fills the
        engine's own ``_cache``.  Walks the whole chain: call it rarely.
        """
        eng = self.metrics_engine
        if eng is None:
            return []
        with self._lock:
            cached = self._metrics_cache
            if (not force and cached is not None and
                    time.time() - cached[0] < self.cfg.metrics_ttl_secs):
                return list(cached[1])
        fns = [eng.nvt_ratio, eng.realized_cap, eng.mvrv_ratio, eng.stock_to_flow,
               eng.sopr, eng.active_addresses_1d, eng.transaction_count_24h,
               eng.average_tx_value]
        rows: List[dict] = []
        objs: Dict[str, Any] = {}
        for fn in fns:
            try:
                m = fn()                                  # -> OnChainMetric
                objs[m.name] = m
                rows.append(m.to_dict())
            except Exception as exc:
                rows.append({"metric": fn.__name__, "error": str(exc)})
        with eng._lock:
            eng._cache.update(objs)
        with self._lock:
            self._metrics_objects = objs
            self._metrics_cache = (time.time(), rows)
        return list(rows)

    @property
    def metric_objects(self) -> Dict[str, Any]:
        """Latest OnChainMetric objects produced by metrics()."""
        with self._lock:
            return dict(self._metrics_objects)

    def validate_chain(self, start: int = 0, end: Optional[int] = None) -> dict:
        """Full range validation (report-only, O(blocks))."""
        if self.validator is None:
            return {"error": "validator not available"}
        result = self.validator.validate_chain(start, end)
        self._trim_validator()
        return result

    def verify_signatures(self, triples: List[Tuple[bytes, bytes, bytes]]) -> bool:
        """Real sequential Schnorr batch check.  Informational only."""
        return self.g.SignatureAggregator.batch_verify(triples)

    def estimate_signature_saving(self, n_sigs: int) -> dict:
        return self.g.SignatureAggregator.estimate_size_saving(n_sigs)

    def median_time_past(self) -> int:
        return self.g.MedianTimePast.compute(self.bc)

    def export_snapshot(self, path: Optional[str] = None) -> str:
        return self.exporter.export_chain_snapshot(path)

    def facade(self) -> Any:
        """
        Lazily build NEBULAComplete.  DANGEROUS: it creates a second
        NEBULABlockchain and ~60 services.  Disabled unless
        ``Layer27Config.allow_complete_facade`` is True.  This method never
        calls quick_start() for you.
        """
        if not self.cfg.allow_complete_facade:
            raise RuntimeError(
                "NEBULAComplete builds a second blockchain; enable it explicitly "
                "with Layer27Config(allow_complete_facade=True)")
        with self._lock:
            if self._facade is None:
                self._facade = self.g.NEBULAComplete()
            return self._facade

    # ------------------------------------------------------------------
    # self-tests (TestRunner + NEBULAAssert + PropertyTest)
    # ------------------------------------------------------------------
    def _register_self_tests(self) -> None:
        if self.tests is None:
            return
        g, A = self.g, self.g.NEBULAAssert
        T = self.tests

        # ---------- unit tests: pure logic, no chain needed ----------
        def t_math_overflow():
            A.raises(OverflowError, g.ContractMath.safe_add, g.ContractMath.MAX, 1)
            A.raises(ValueError, g.ContractMath.safe_sub, 1, 2)
            A.raises(ZeroDivisionError, g.ContractMath.safe_div, 1, 0)
            A.equal(g.ContractMath.percentage(1000, 250), 25)

        def t_events_roundtrip():
            em, seen = g.EventEmitter(), []
            em.on_all(seen.append)
            em.emit("c", "n", {"k": 1}, height=3)
            A.equal(len(seen), 1)
            A.equal(len(em.get_events("c", "n")), 1)

        def t_access_roles():
            ac = g.AccessControl("owner")
            A.false(ac.grant_role("MINTER", "bob", caller="mallory"))
            A.true(ac.grant_role("MINTER", "bob", caller="owner"))
            A.true(ac.has_role("MINTER", "bob"))
            A.raises(PermissionError, ac.require_role, "MINTER", "eve")

        def t_system_contract():
            sc = g.StandardContract("addr", "owner")
            sc.access.grant_role(g.AccessControl.PAUSER_ROLE, "owner", "owner")
            sc.pause("owner")
            A.raises(RuntimeError, sc.require_not_paused)
            sc.unpause("owner")
            sc.require_not_paused()
            A.true(sc.info()["events"] >= 2)

        def t_mtp_median():
            ts = [100, 90, 110, 105, 95, 120, 130, 80, 85, 140, 150]
            view = _ChainView([_FakeBlk(t) for t in ts])
            A.equal(g.MedianTimePast.compute(view), sorted(ts)[5])

        def t_locktime_height():
            view = _ChainView([_FakeBlk(1)] * 6)          # height 5
            A.true(g.MedianTimePast.validate_locktime(5, view))
            A.false(g.MedianTimePast.validate_locktime(6, view))

        def t_clock_future():
            blocks = [_FakeBlk(1_000 + i) for i in range(12)]
            clk = g.ChainClock(_ChainView(blocks))
            A.false(clk.validate_timestamp(int(time.time()) + 10_000, 1_011)[0])
            A.false(clk.validate_timestamp(1_005, 1_011)[0])       # not after MTP

        def t_sig_size():
            r = g.SignatureAggregator.estimate_size_saving(10)
            A.equal(r["saving_bytes"], 10 * 64 - (10 * 32 + 32))
            A.true(g.SignatureAggregator.batch_verify([]))

        def t_base58_roundtrip():
            A.true(g.PropertyTest.test_base58check_roundtrip(10))

        def t_reward_monotone():
            A.true(g.PropertyTest.test_mining_reward_monotone_decrease())

        def t_testcase_types():
            tc = g.TestCase(name="x", fn=lambda: None)
            A.equal(tc.timeout, 30.0)
            r = g.TestResult(name="x", passed=True, duration=0.0)
            A.equal(r.to_dict()["passed"], True)
            A.equal(g.OnChainMetric("m", 1.0, 1).to_dict()["metric"], "m")
            A.equal(g.MempoolAlert("a", "info", "m", 1.0).to_dict()["type"], "a")

        for name, fn in [
            ("math_overflow", t_math_overflow), ("events_roundtrip", t_events_roundtrip),
            ("access_roles", t_access_roles), ("system_contract", t_system_contract),
            ("mtp_median", t_mtp_median), ("locktime_height", t_locktime_height),
            ("clock_future", t_clock_future), ("signature_size", t_sig_size),
            ("base58_roundtrip", t_base58_roundtrip), ("reward_monotone", t_reward_monotone),
            ("data_types", t_testcase_types),
        ]:
            T.add_test(name, fn, tags=["unit"])

        # ---------- chain tests: need the live blockchain ----------
        def t_metrics_all():
            rows = self.metrics(force=True)
            A.true(len(rows) == 8, f"expected 8 metric rows, got {len(rows)}")
            bad = [r for r in rows if "error" in r]
            A.false(bad, f"metric errors: {bad}")

        def t_validator_tip():
            if len(self.bc._chain) == 0:
                return
            A.true(isinstance(self.validator.quick_validate(), bool))

        def t_clock_stats():
            A.true("mtp" in self.clock.stats())

        for name, fn in [("metrics_all", t_metrics_all), ("validator_tip", t_validator_tip),
                         ("clock_stats", t_clock_stats)]:
            T.add_test(name, fn, tags=["chain"])

        # ---------- property tests: need real host wallet / script engine ----------
        def prop(fn_name: str):
            def _run():
                A.true(getattr(g.PropertyTest, fn_name)(), f"{fn_name} returned False")
            return _run

        for fn_name in ("test_wallet_address_invariant", "test_script_arithmetic_consistency"):
            T.add_test(fn_name, prop(fn_name), tags=["property"])

    def run_self_tests(self, tag: Optional[str] = None) -> dict:
        """Run registered tests.  tag in {'unit', 'chain', 'property', None=all}."""
        if self.tests is None:
            return {"error": "TestRunner not available"}
        return self.tests.run(tag_filter=tag)

    # ------------------------------------------------------------------
    # introspection
    # ------------------------------------------------------------------
    def coverage(self) -> Dict[str, dict]:
        """For each of the 20 classes: is it wired, and how."""
        out: Dict[str, dict] = {}
        for cls_name, (kind, attr, role) in CLASS_ROLES.items():
            cls = getattr(self.g, cls_name, None)
            if kind == "lazy":
                wired = cls is not None
                state = "lazy-available" if wired else "class-missing"
            elif kind == "data":
                wired = cls is not None and attr is not None and getattr(self, attr, None) is not None
                state = "wired" if wired else "producer-missing"
            elif kind == "static":
                wired = cls is not None and getattr(self, attr, None) is cls
                state = "wired" if wired else "missing"
            else:
                obj = getattr(self, attr, None) if attr else None
                wired = cls is not None and isinstance(obj, cls)
                state = "wired" if wired else "missing"
            out[cls_name] = {"kind": kind, "attr": attr, "role": role,
                             "wired": wired, "state": state}
        return out

    def problems(self) -> List[str]:
        """Human-readable list of everything that is not wired correctly."""
        res = [f"{n}: {d['state']}" for n, d in self.coverage().items() if not d["wired"]]
        res += [f"build:{k}: {v}" for k, v in self.build_errors.items()]
        return res

    def status(self) -> dict:
        with self._lock:
            return {
                "uptime_secs": round(time.time() - self.started_at, 1),
                "errors": self.errors,
                "last_errors": list(self.error_log)[-5:],
                "blocks_seen": self.blocks_seen,
                "last_height": self.last_height,
                "reorgs_seen": self.reorgs_seen,
                "last_reorg": self.last_reorg,
                "clock_violations": self.clock_violations,
                "block_check_failures": self.block_check_failures,
                "findings": len(self.findings),
                "mempool_alerts": len(self.mempool_alerts),
                "submit": {"calls": self.submit_calls,
                           "accepted": self.submit_accepted,
                           "rejected": self.submit_rejected},
                "events_kept": len(self.events._events) if self.events else 0,
                "batch": self.batch.stats() if self.batch else None,
                "build_errors": dict(self.build_errors),
                "detached": self._detached,
            }


class _FakeBlk:
    """Tiny block stand-in used by the built-in unit tests (timestamp only)."""

    class _H:
        def __init__(self, ts: int):
            self.timestamp = ts

    def __init__(self, ts: int):
        self.header = _FakeBlk._H(ts)


# ==========================================================================
#                         install / uninstall
# ==========================================================================
def install(host: Any, config: Optional[Layer27Config] = None) -> dict:
    """
    Attach Layer27 to every NEBULAFullNode created AFTER this call and
    (optionally) observe Mempool.submit.  Idempotent.
    """
    report: Dict[str, Any] = {"node_patched": False, "mempool_observed": False,
                              "already_installed": False, "notes": []}
    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is None:
        raise RuntimeError("install(): host has no NEBULAFullNode")

    if getattr(node_cls, "_g27_orig", None):
        report["already_installed"] = True
        return report

    orig_init = node_cls.__init__

    @functools.wraps(orig_init)
    def patched_init(self, *a, **k):
        orig_init(self, *a, **k)                     # the original ALWAYS runs first
        try:
            layer = Layer27(self, config=config)
            self.group27 = layer
            self.bc.add_listener(layer)
        except Exception as exc:                     # the node must still start
            self.group27_error = exc
            log.error("group27 layer failed to attach: %s", exc)

    node_cls._g27_orig = orig_init
    node_cls.__init__ = patched_init
    report["node_patched"] = True

    cfg = config or Layer27Config()
    mem_cls = getattr(host, "Mempool", None)
    if cfg.observe_mempool and mem_cls is not None and hasattr(mem_cls, "submit") \
            and not getattr(mem_cls, "_g27_submit_orig", None):
        orig_submit = mem_cls.submit

        @functools.wraps(orig_submit)
        def patched_submit(self, *a, **k):
            result = orig_submit(self, *a, **k)      # original first, result untouched
            try:
                layer = getattr(self, "_g27_layer", None)
                if layer is not None:
                    layer.observe_submit(result)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in install.patched_submit", exc_info=True)
            return result

        mem_cls._g27_submit_orig = orig_submit
        mem_cls.submit = patched_submit
        report["mempool_observed"] = True
    elif cfg.observe_mempool and mem_cls is None:
        report["notes"].append("host has no Mempool class; submit observation skipped")
    return report


def uninstall(host: Any) -> dict:
    """Restore the host exactly as it was and detach every live layer."""
    report = {"node_restored": False, "mempool_restored": False, "detached": 0}
    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is not None:
        orig = getattr(node_cls, "_g27_orig", None)
        if orig:
            node_cls.__init__ = orig
            del node_cls._g27_orig
            report["node_restored"] = True
    mem_cls = getattr(host, "Mempool", None)
    if mem_cls is not None:
        orig_submit = getattr(mem_cls, "_g27_submit_orig", None)
        if orig_submit:
            mem_cls.submit = orig_submit
            del mem_cls._g27_submit_orig
            report["mempool_restored"] = True
    for layer in list(_LIVE_LAYERS):
        layer.detach()
        report["detached"] += 1
    return report


def install_from_import(config: Optional[Layer27Config] = None) -> Any:
    """Convenience: import nebula_v10_11 and install.  Returns the host module."""
    host = importlib.import_module("nebula_v10_11")
    install(host, config)
    return host


# ==========================================================================
#            OFFLINE SELF-TEST  (python nebula_group27_install.py --selftest)
#
# Runs against a small STUB host (the real nebula_v10_11.py is NOT needed).
# It proves the layer logic: listener wiring, report-only behaviour, error
# containment, caps, Mempool observation and a clean uninstall.
# It does NOT prove anything about the real host - see the --live notes.
# ==========================================================================
def _build_stub_host():
    import types
    from dataclasses import dataclass, field

    m = types.ModuleType("nebula_v10_11")

    @dataclass
    class ContractEvent:
        contract: str
        name: str
        data: dict
        height: int = 0
        tx_hash: str = ""

        def to_dict(self):
            return {"contract": self.contract, "name": self.name, "data": self.data,
                    "height": self.height, "tx_hash": self.tx_hash}

    class ContractStorage:
        def __init__(self):
            self._d = {}

        def size(self):
            return len(self._d)

    @dataclass
    class BatchJob:
        job_id: str
        job_type: str
        items: list
        callback: object = None
        status: str = "pending"
        results: list = field(default_factory=list)
        errors: list = field(default_factory=list)
        created_at: float = field(default_factory=time.time)

        def is_done(self):
            return self.status in ("completed", "failed")

        def to_dict(self):
            return {"job_id": self.job_id, "status": self.status}

    class FeeBumper:
        def __init__(self, bc):
            self.bc = bc

    class Schnorr:
        N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

        @staticmethod
        def verify(pub, msg, sig):
            return True

    class ScriptOpcode:
        OP_ADD, OP_EQUAL = 0x93, 0x87

    class ScriptInterpreter:
        def execute(self, script):
            return True, ""

    class Header:
        def __init__(self, ts, merkle="m"):
            self.timestamp, self.merkle_root = ts, merkle

        def meets_target(self):
            return True

    class Out:
        def __init__(self, value, address):
            self.value, self.address = value, address

    class Tx:
        def __init__(self, txid, outs, coinbase=False):
            self.txid, self.outputs, self.is_coinbase = txid, outs, coinbase

        def total_output(self):
            return sum(o.value for o in self.outputs)

    class Block:
        def __init__(self, height, ts, merkle_ok=True):
            self.height = height
            self.hash = f"{height:064x}"
            self.header = Header(ts, "m" if merkle_ok else "BAD")
            self.transactions = [Tx(f"cb{height}", [Out(50 * 10**9, "Nminer")], True),
                                 Tx(f"tx{height}", [Out(10**9, "Nbob")])]

        def compute_merkle_root(self):
            return "m"

        def byte_size(self):
            return 300

    class Utxo:
        def balance(self, addr):
            return 0

        def total_supply(self):
            return 1000 * 10**9

        def size(self):
            return 10

    class Mempool:
        def __init__(self):
            self._txs = {}

        def submit(self, tx):
            if tx == "bad":
                return False, "rejected"
            self._txs[tx] = 1
            return True, "ok"

        def size(self):
            return len(self._txs)

        def smart_fee(self, n):
            return 10

    class NEBULABlockchain:
        def __init__(self):
            self._chain, self._listeners = [], []
            self.utxo, self.mempool = Utxo(), Mempool()

        @property
        def height(self):
            return len(self._chain) - 1

        @property
        def tip(self):
            return self._chain[-1]

        def get_block(self, h):
            return self._chain[h] if 0 <= h < len(self._chain) else None

        def add_listener(self, l):
            self._listeners.append(l)

        def connect(self, blk):
            self._chain.append(blk)
            for l in list(self._listeners):
                try:
                    l.on_connect(blk)
                except Exception:
                    _NB_SWALLOW_LOG.debug("swallowed Exception in _build_stub_host.NEBULABlockchain.connect", exc_info=True)                      # host semantic: listener errors never veto

        def reorg(self, old, new, anc):
            for l in list(self._listeners):
                l.on_reorg(old, new, anc)

    class NEBULAFullNode:
        def __init__(self):
            self.bc = NEBULABlockchain()
            self.started = True

    for obj in (ContractEvent, ContractStorage, BatchJob, FeeBumper, Schnorr, ScriptOpcode,
                ScriptInterpreter, Block, Mempool, NEBULABlockchain, NEBULAFullNode):
        setattr(m, obj.__name__, obj)
    return m


def selftest(verbose: bool = True) -> bool:
    """Offline logic test against a stub host.  Returns True on success."""
    import os

    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)
    if "nebula_group27" in sys.modules or "nebula_v10_11" in sys.modules:
        print("selftest must run in a fresh interpreter (modules already imported)")
        return False

    host = _build_stub_host()
    sys.modules["nebula_v10_11"] = host          # nebula_group27 will pick this up
    failures: List[str] = []

    def check(cond: bool, label: str) -> None:
        if verbose:
            print(("  PASS  " if cond else "  FAIL  ") + label)
        if not cond:
            failures.append(label)

    try:
        # 1. install --------------------------------------------------------
        rep = install(host)
        check(rep["node_patched"] and rep["mempool_observed"], "install patches node + mempool")
        check(install(host)["already_installed"], "install is idempotent")

        node = host.NEBULAFullNode()
        layer = getattr(node, "group27", None)
        check(layer is not None and not hasattr(node, "group27_error"), "layer attached to node")
        check(layer in node.bc._listeners, "layer registered as chain listener")
        check(node.started, "original __init__ still ran")

        # 2. all 20 classes accounted for ------------------------------------
        check(len(CLASS_ROLES) == 20, "CLASS_ROLES lists exactly 20 classes")
        check(layer.problems() == [], f"all 20 classes wired (problems={layer.problems()})")

        # 3. normal blocks ----------------------------------------------------
        base = int(time.time()) - 1000
        for i in range(15):
            node.bc.connect(host.Block(i, base + i * 10))
        st = layer.status()
        check(st["blocks_seen"] == 15 and st["last_height"] == 14, "15 blocks observed")
        check(st["errors"] == 0, f"no errors on normal blocks ({st['last_errors']})")
        check(st["findings"] == 0, "no false positives on normal blocks")
        check(st["events_kept"] == 15, "one BlockConnected event per block")

        # 4. anomalies are REPORTED, never rejected ----------------------------
        node.bc.connect(host.Block(15, int(time.time()) + 10_000))
        check(node.bc.height == 15, "future-timestamp block was NOT rejected")
        check(layer.clock_violations == 1, "clock violation reported")
        node.bc.connect(host.Block(16, base + 200, merkle_ok=False))
        check(node.bc.height == 16, "bad-merkle block was NOT rejected")
        check(layer.block_check_failures == 1, "merkle failure reported")

        # 5. mempool observation ------------------------------------------------
        r1, r2 = node.bc.mempool.submit("a"), node.bc.mempool.submit("bad")
        check(r1 == (True, "ok") and r2 == (False, "rejected"), "Mempool.submit results unchanged")
        s = layer.status()["submit"]
        check(s == {"calls": 2, "accepted": 1, "rejected": 1}, f"submit counters {s}")

        # 6. reorg ---------------------------------------------------------------
        node.bc.reorg([1, 2], [3], 10)
        check(layer.reorgs_seen == 1 and layer.last_reorg["old_blocks"] == 2, "reorg recorded")

        # 7. mempool alert -------------------------------------------------------
        layer.cfg.mempool_alert_size = 0
        node.bc.connect(host.Block(17, base + 210))
        check(len(layer.mempool_alerts) == 1, "MempoolAlert created when mempool is large")
        check(layer.mempool_alerts[0].to_dict()["type"] == "size", "MempoolAlert content ok")

        # 8. error containment ---------------------------------------------------
        before = layer.errors
        saved = layer.validator
        layer.validator = object()                      # will blow up inside _check_block
        node.bc.connect(host.Block(18, base + 220))
        layer.validator = saved
        check(node.bc.height == 18, "block connected despite layer failure")
        check(layer.errors > before, "layer failure was counted, not raised")

        # 9. on-demand API ---------------------------------------------------------
        rows = layer.metrics(force=True)
        check(len(rows) == 8 and not [r for r in rows if "error" in r], f"8 metrics computed {rows[:1]}")
        check(len(layer.metric_objects) == 8, "OnChainMetric objects retained")
        check(len(layer.metrics_engine._cache) == 8, "engine _cache filled")
        check(layer.metrics() == layer.metrics(), "metrics TTL cache works")
        vr = layer.validate_chain()
        check(isinstance(vr, dict) and "blocks_checked" in vr, "validate_chain works")
        check(isinstance(layer.median_time_past(), int), "median_time_past works")
        check(layer.estimate_signature_saving(4)["saving_bytes"] == 4 * 64 - (4 * 32 + 32),
              "signature saving estimate")
        try:
            layer.facade()
            check(False, "facade refused by default")
        except RuntimeError:
            check(True, "facade refused by default")

        # 10. built-in self tests ---------------------------------------------------
        res = layer.run_self_tests("unit")
        check(res["failed"] == 0, f"unit self-tests {res['passed']}/{res['total']} "
                                  f"{[r for r in res['results'] if not r['passed']]}")
        res = layer.run_self_tests("chain")
        check(res["failed"] == 0, f"chain self-tests {res['passed']}/{res['total']} "
                                  f"{[r for r in res['results'] if not r['passed']]}")

        # 11. caps -------------------------------------------------------------------
        layer.cfg.max_events = 5
        node.bc.connect(host.Block(19, base + 230))
        check(len(layer.events._events) <= 5, "event history capped")

        # 12. uninstall ---------------------------------------------------------------
        ur = uninstall(host)
        check(ur["node_restored"] and ur["mempool_restored"], "uninstall restores both patches")
        check(layer not in node.bc._listeners, "layer detached from listeners")
        node2 = host.NEBULAFullNode()
        check(not hasattr(node2, "group27"), "new nodes no longer get a layer")
        check(host.Mempool.submit(node2.bc.mempool, "z") == (True, "ok"), "original Mempool.submit back")
        check(layer.status()["detached"], "layer flagged detached")
    except Exception as exc:                            # a crash is a failure too
        import traceback
        traceback.print_exc()
        failures.append(f"CRASH: {exc}")
    finally:
        sys.modules.pop("nebula_v10_11", None)

    print()
    print("RESULT:", "ALL CHECKS PASSED" if not failures else f"{len(failures)} FAILED: {failures}")
    return not failures


# ==========================================================================
#                                  CLI
# ==========================================================================
def _main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="NEBULA group27 wiring layer")
    ap.add_argument("--selftest", action="store_true",
                    help="offline logic test against a stub host (no nebula_v10_11.py needed)")
    args = ap.parse_args(argv)
    if args.selftest:
        return 0 if selftest() else 1
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(_main())
