"""
nebula_group28_install.py
=========================

Wiring layer for the 20 "dead" classes of nebula_group28.py.

Design rules (taken from nebula_group28_guide.txt):
  * nebula_v10_11.py is NEVER edited.  We only wrap NEBULAFullNode.__init__.
  * The layer NEVER rejects a block / transaction.  Every callback is wrapped
    in try/except; failures are counted in ``layer.errors`` and kept in
    ``layer.error_log`` (bounded).
  * Report-only: nothing here changes consensus (HybridConsensus is created
    but never votes by itself; nothing is fed back into validation).
  * Every service is created independently.  If one cannot be created
    (missing dependency, unexpected host shape) it is listed in
    ``layer.skipped`` and the rest keep working.
  * Memory is bounded (see ``Layer28.MAX_INDEXED_OUTPUTS``).

Usage:
    import nebula_v10_11 as host
    import nebula_group28_install as g28
    g28.install(host)                  # patches NEBULAFullNode.__init__
    node = host.NEBULAFullNode(...)    # node.group28 now exists
    node.group28.status()
    g28.uninstall(host)                # restores the original __init__

Honest notes about the wrapped classes (see README_wiring_ps.txt):
  * BLSSignature.verify / aggregate_verify, RingSignature.verify are
    length/field checks only -> NOT real cryptographic verification.
  * NEBULALaunchChecker.CHECKLIST is hard-coded True -> not a real audit.
  * PeelChainDetector._follow_chain returns only the start tx.
  They are exposed as "experimental" and are never used for any decision.
"""
from __future__ import annotations

import threading
import time
from collections import deque
from types import SimpleNamespace
from typing import Any, Callable, Dict, List, Optional

import nebula_group28 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
class _OutputIndex:
    """
    Minimal 'UTXOSet-like' adapter for CommonInputHeuristic.

    CommonInputHeuristic.process_transaction() calls ``utxo.get(txid, index)``
    and reads ``.address``.  The real UTXO set has ALREADY spent those inputs
    when a block is connected, so we keep our own (txid, index) -> address map,
    filled from every connected block.
    """

    def __init__(self, max_entries: int):
        self._map: Dict[tuple, str] = {}
        self.max_entries = max_entries
        self.overflowed = False
        self.unresolved_outputs = 0

    def __len__(self) -> int:
        return len(self._map)

    def clear(self) -> None:
        self._map.clear()
        self.overflowed = False
        self.unresolved_outputs = 0

    def add_output(self, txid: str, index: int, address: Optional[str]) -> None:
        if not address:
            self.unresolved_outputs += 1
            return
        if len(self._map) >= self.max_entries:
            self.overflowed = True
            return
        self._map[(txid, index)] = address

    # UTXOSet-compatible read API used by CommonInputHeuristic
    def get(self, txid: str, index: int):
        addr = self._map.get((txid, index))
        return SimpleNamespace(address=addr) if addr else None


class _ChainProxy:
    """
    Passed to BlockchainClusterer so its own chain loop is a no-op (we feed the
    heuristic incrementally) while balances still come from the REAL UTXO set.
    """

    def __init__(self, real_bc: Any):
        self._chain: list = []
        self.utxo = getattr(real_bc, "utxo", None)


# --------------------------------------------------------------------------- #
# the layer
# --------------------------------------------------------------------------- #
class Layer28:
    """Holds one instance of every service class of group28 and the chain hooks."""

    MAX_INDEXED_OUTPUTS = 2_000_000     # RAM cap for the output->address index
    MAX_ERROR_LOG = 100
    STAKING_ATTRS = ("staking", "staking_engine", "stake_engine", "staker")

    def __init__(self, node: Any, *, start_mempool_thread: bool = False,
                 mempool_interval: float = 30.0,
                 max_indexed_outputs: Optional[int] = None):
        self.node = node
        self.bc = getattr(node, "bc", None)
        self.errors = 0
        self.error_log: deque = deque(maxlen=self.MAX_ERROR_LOG)
        self.skipped: Dict[str, str] = {}
        self.blocks_seen = 0
        self.reorgs_seen = 0
        self.last_height: Optional[int] = None
        self._lock = threading.RLock()
        self._attached = False
        self._clusters_dirty = True
        self._started_mempool = False
        self._replayed = False

        # services (None until successfully created)
        self.mempool_monitor = None
        self.core_tests = None
        self.grand_finale = None
        self.hybrid_consensus = None
        self.layer2 = None
        self.launch_checker = None
        self.verkle = None
        self.kzg = None
        self.clusterer = None
        self.change_detector = None
        self.peel_detector = None
        # stateless classmethod-only classes: the CLASS itself is the service
        self.bls = g.BLSSignature
        self.stealth = g.StealthAddress
        self.ring = g.RingSignature

        # clustering state (incremental feed)
        self._out_index = _OutputIndex(max_indexed_outputs or self.MAX_INDEXED_OUTPUTS)
        self._heuristic = g.CommonInputHeuristic()

        self._build_services(start_mempool_thread, mempool_interval)

    # ---------------- internal utilities ---------------- #
    def _record_error(self, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.error_log.append(f"{time.strftime('%H:%M:%S')} {where}: "
                              f"{type(exc).__name__}: {exc}")

    def _guard(self, where: str, fn: Callable, *a, **k):
        """Run fn; never raise. Returns (ok, value)."""
        try:
            return True, fn(*a, **k)
        except Exception as e:                       # noqa: BLE001
            self._record_error(where, e)
            return False, None

    def _find_staking(self):
        for name in self.STAKING_ATTRS:
            obj = getattr(self.node, name, None)
            if obj is not None and hasattr(obj, "_validators") \
                    and hasattr(obj, "_total_staked"):
                return obj
        return None

    def _make(self, name: str, factory: Callable, requires: tuple = ()):
        """Create one service; on any problem record it in self.skipped."""
        missing = [r for r in requires if not hasattr(g, r)]
        if missing:
            self.skipped[name] = "missing host classes: " + ", ".join(missing)
            return None
        try:
            return factory()
        except Exception as e:                       # noqa: BLE001
            self.skipped[name] = f"{type(e).__name__}: {e}"
            return None

    def _build_services(self, start_thread: bool, interval: float) -> None:
        bc = self.bc
        if bc is None:
            for n in ("mempool_monitor", "core_tests", "hybrid_consensus",
                      "layer2", "launch_checker", "clusterer"):
                self.skipped[n] = "node has no .bc"

        # --- ledger-bound services (need bc) ---
        if bc is not None:
            self.mempool_monitor = self._make(
                "mempool_monitor", lambda: g.MempoolMonitor(bc),
                requires=("MempoolAlert",))
            self.core_tests = self._make(
                "core_tests", lambda: g.NEBULATests(bc),
                requires=("TestResultAccumulator", "TestCrypto", "TestTransactions",
                          "TestBlocks", "TestBlockchain", "TestWallet"))
            self.layer2 = self._make("layer2", lambda: g.Layer2Manager(bc))
            self.launch_checker = self._make(
                "launch_checker", lambda: g.NEBULALaunchChecker(bc))   # pass bc: avoids creating a 2nd chain
            self.clusterer = self._make(
                "clusterer", self._new_clusterer)

            staking = self._find_staking()
            if staking is None:
                self.skipped["hybrid_consensus"] = \
                    "no staking engine found on node (tried: %s)" % ", ".join(self.STAKING_ATTRS)
            else:
                self.hybrid_consensus = self._make(
                    "hybrid_consensus", lambda: g.HybridConsensus(bc, staking),
                    requires=("Secp256k1",))

        # --- standalone services ---
        self.grand_finale = self._make(
            "grand_finale", lambda: g.NEBULAGrandFinale())
        self.verkle = self._make("verkle", lambda: g.VerkleTree())
        self.kzg = self._make("kzg", lambda: g.KZGCommitment())
        self.change_detector = self._make(
            "change_detector", lambda: g.ChangeDetectionHeuristic())
        self.peel_detector = self._make(
            "peel_detector", lambda: g.PeelChainDetector())

        if start_thread and self.mempool_monitor is not None:
            self._guard("mempool.start", self.mempool_monitor.start, interval)
            self._started_mempool = True

    def _new_clusterer(self):
        c = g.BlockchainClusterer(_ChainProxy(self.bc))
        c.common_input = self._heuristic      # share our incrementally-fed heuristic
        return c

    # ---------------- chain-listener interface ---------------- #
    def attach(self) -> bool:
        """Register on bc as listener. Returns True on success."""
        try:
            self.bc.add_listener(self)
            self._attached = True
            return True
        except Exception as e:                       # noqa: BLE001
            self._record_error("attach", e)
            return False

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer28.detach", exc_info=True)
        self._attached = False
        if self._started_mempool and self.mempool_monitor is not None:
            self._guard("mempool.stop", self.mempool_monitor.stop)
            self._started_mempool = False

    def on_connect(self, block) -> None:
        try:
            with self._lock:
                self.blocks_seen += 1
                self.last_height = getattr(block, "height",
                                           getattr(getattr(block, "header", None),
                                                   "height", self.last_height))
                self._feed_block(block)
                self._clusters_dirty = True
            if self.mempool_monitor is not None:
                self._guard("mempool.check", self.mempool_monitor.check)
        except Exception as e:                       # noqa: BLE001
            self._record_error("on_connect", e)

    def on_reorg(self, old, new, ancestor_height) -> None:
        """Union-find cannot undo merges -> drop clustering state, rebuild lazily."""
        try:
            with self._lock:
                self.reorgs_seen += 1
                self._out_index.clear()
                self._heuristic = g.CommonInputHeuristic()
                self._clusters_dirty = True
                self._replayed = False
        except Exception as e:                       # noqa: BLE001
            self._record_error("on_reorg", e)

    # ---------------- clustering ---------------- #
    def _feed_block(self, block) -> None:
        for tx in getattr(block, "transactions", []) or []:
            txid = getattr(tx, "txid", None)
            # 1) heuristic first (inputs refer to OLDER outputs)
            self._guard("cluster.tx", self._heuristic.process_transaction,
                        tx, self._out_index)
            # 2) then register this tx's outputs
            for i, out in enumerate(getattr(tx, "outputs", []) or []):
                self._out_index.add_output(txid, i, getattr(out, "address", None))

    def replay_chain(self) -> int:
        """Rebuild clustering state from bc._chain (after reorg or late install)."""
        n = 0
        with self._lock:
            self._out_index.clear()
            self._heuristic = g.CommonInputHeuristic()
            for blk in list(getattr(self.bc, "_chain", []) or []):
                self._feed_block(blk)
                n += 1
            self._clusters_dirty = True
            self._replayed = True
        return n

    def rebuild_clusters(self) -> int:
        """Return number of clusters. Fresh BlockchainClusterer every time
        (its cluster_blockchain() appends, so re-running it would duplicate)."""
        if self.bc is None:
            return 0
        with self._lock:
            if not self._replayed and self.blocks_seen == 0:
                self.replay_chain()
            ok, c = self._guard("cluster.new", self._new_clusterer)
            if not ok:
                return 0
            ok, n = self._guard("cluster.build", c.cluster_blockchain)
            if ok:
                self.clusterer = c
                self._clusters_dirty = False
                return n
            return 0

    def top_clusters(self, n: int = 10) -> List[dict]:
        if self._clusters_dirty:
            self.rebuild_clusters()
        return self.clusterer.top_clusters(n) if self.clusterer else []

    def cluster_for(self, address: str):
        if self._clusters_dirty:
            self.rebuild_clusters()
        return self.clusterer.get_cluster_for_address(address) if self.clusterer else None

    # ---------------- on-demand tools ---------------- #
    def run_core_tests(self):
        """(passed, total) from NEBULATests; (None, None) on failure."""
        if not self.core_tests:
            return None, None
        ok, v = self._guard("core_tests", self.core_tests.run_basic_tests)
        return v if ok else (None, None)

    def detect_peel_chains(self, min_length: int = 1) -> List[List[str]]:
        """NOTE: upstream _follow_chain returns only the first tx, so any
        min_length >= 2 yields nothing. Default 1 lists candidate start txs."""
        if not (self.peel_detector and self.bc):
            return []
        ok, v = self._guard("peel.detect", self.peel_detector.detect, self.bc, min_length)
        return v if ok and v else []

    def launch_report(self) -> Optional[dict]:
        """NOTE: upstream checklist is hard-coded True (not a real audit)."""
        if not self.launch_checker:
            return None
        ok, v = self._guard("launch.run", self.launch_checker.run_checklist)
        if ok and isinstance(v, dict):
            v = dict(v)
            v["warning"] = "hard-coded checklist; not an actual verification"
        return v if ok else None

    def finalized_height(self) -> Optional[int]:
        if not self.hybrid_consensus:
            return None
        ok, v = self._guard("hybrid.finalized_height", self.hybrid_consensus.finalized_height)
        return v if ok else None

    # ---------------- status ---------------- #
    def status(self) -> dict:
        services = {
            "mempool_monitor": self.mempool_monitor, "core_tests": self.core_tests,
            "grand_finale": self.grand_finale, "hybrid_consensus": self.hybrid_consensus,
            "layer2": self.layer2, "launch_checker": self.launch_checker,
            "verkle": self.verkle, "kzg": self.kzg, "clusterer": self.clusterer,
            "change_detector": self.change_detector, "peel_detector": self.peel_detector,
        }
        return {
            "attached": self._attached,
            "errors": self.errors,
            "last_errors": list(self.error_log)[-5:],
            "blocks_seen": self.blocks_seen,
            "reorgs_seen": self.reorgs_seen,
            "last_height": self.last_height,
            "services_ok": sorted(k for k, v in services.items() if v is not None),
            "skipped": dict(self.skipped),
            "indexed_outputs": len(self._out_index),
            "index_overflowed": self._out_index.overflowed,
            "unresolved_outputs": self._out_index.unresolved_outputs,
            "cluster_stats": self.clusterer.stats() if self.clusterer else None,
            "mempool_trend": (self.mempool_monitor.trend()
                              if self.mempool_monitor else None),
            "layer2_stats": self.layer2.stats() if self.layer2 else None,
            "experimental_only": ["BLSSignature", "RingSignature", "KZGCommitment",
                                   "VerkleTree", "StealthAddress"],
        }


# --------------------------------------------------------------------------- #
# install / uninstall (wrap NEBULAFullNode.__init__, as in group 5)
# --------------------------------------------------------------------------- #
def install(host, **layer_kwargs) -> bool:
    """Patch host.NEBULAFullNode.__init__. Idempotent. Returns True if patched now."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g28_orig", None):
        return False
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)                      # original always runs first; its errors propagate as before
        try:
            layer = Layer28(self, **layer_kwargs)
            self.group28 = layer
            layer.attach()
        except Exception as e:                   # noqa: BLE001  node must still start
            self.group28_error = e

    patched.__wrapped__ = orig
    cls._g28_orig = orig
    cls.__init__ = patched
    return True


def uninstall(host, nodes: tuple = ()) -> bool:
    """Restore the original __init__; optionally detach layers of given live nodes."""
    for n in nodes:
        lay = getattr(n, "group28", None)
        if lay is not None:
            lay.detach()
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g28_orig", None)
    if not orig:
        return False
    cls.__init__ = orig
    del cls._g28_orig
    return True
