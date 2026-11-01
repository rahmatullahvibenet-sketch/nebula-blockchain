"""NEBULA group55 wiring layer.

Connects the 20 group55 classes to a live NEBULAFullNode WITHOUT editing
nebula_v10_11.py.  Same pattern as group5:

    import nebula_v10_11 as host
    import nebula_group55_install as g55
    g55.install(host)          # every NEBULAFullNode created afterwards gets node.group55
    ...
    g55.uninstall(host)        # node behaves exactly as before

Safety rules (all enforced in code):
  * Layer55 never rejects a block or a transaction. Every callback is wrapped in
    try/except; failures are counted in layer.errors and stored in layer.last_error.
  * Observe-only: no consensus decision is taken from group55. StakingRewardsV3 and
    ValidatorRotation (consensus-sensitive names) are created but NEVER called
    automatically.
  * Services that need objects this file cannot be sure exist (VoteEscrowedNBL,
    ValidatorSetManager, OnChainRNG, NBL721Registry, RoyaltyEngine, NodeRESTAPI,
    ComplianceEngine, OracleV2) are built only when you pass them in `deps=` or when
    the node already has them under the exact attribute names listed in DEP_ATTRS AND
    the object has the methods the service calls. Otherwise they are listed in
    layer.skipped with the reason.
  * Memory is capped (max_blocks) and rolled back on reorg.
"""
from __future__ import annotations

import sys
import threading
import weakref
from typing import Any, Callable, Dict, List, Optional
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

__all__ = ["Layer55", "install", "uninstall", "DEP_ATTRS"]

# dependency name -> (exact node attribute names to look for, methods the object must have)
DEP_ATTRS: Dict[str, tuple] = {
    "oracle":          (("oracle", "oracle_v2"),              ("price",)),
    "compliance":      (("compliance",),                      ()),
    "venbl":           (("venbl",),                           ("total_venbl", "balance")),
    "validator_set":   (("validator_set",),                   ("list_active_validators",)),
    "rng":             (("rng", "onchain_rng"),               ("random_int",)),
    "nft":             (("nft", "nbl721"),                    ()),
    "royalty_engine":  (("royalty_engine",),                  ("process_sale",)),
    "rest_api":        (("rest_api",),                        ("handle",)),
}

_LIVE: "weakref.WeakSet[Layer55]" = weakref.WeakSet()


def _group_module():
    """Import nebula_group55 lazily (it pulls in the big host file by name)."""
    import nebula_group55 as g
    return g


class Layer55:
    """Holds every group55 service for one node and listens to chain events."""

    def __init__(self, node: Any, deps: Optional[Dict[str, Any]] = None,
                 max_blocks: int = 2000, count_mempool: bool = True):
        self.node = node
        self.bc = node.bc
        self.errors = 0
        self.last_error: Optional[str] = None
        self.max_blocks = int(max_blocks)
        self.services: Dict[str, Any] = {}
        self.skipped: Dict[str, str] = {}
        self.counters: Dict[str, int] = {
            "blocks_seen": 0, "reorgs_seen": 0,
            "mempool_accepted": 0, "mempool_rejected": 0,
        }
        self.last_height = -1
        self._lock = threading.RLock()
        self._mp_target: Any = None
        self._mp_had_own = False
        self._mp_orig: Any = None
        self._g = _group_module()
        self.deps = self._resolve_deps(deps or {})
        self._build_services()
        if count_mempool:
            self._wrap_mempool()
        _LIVE.add(self)

    # ------------------------------------------------------------------ helpers
    def _fail(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.last_error = f"{where}: {type(exc).__name__}: {exc}"

    def _resolve_deps(self, given: Dict[str, Any]) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        for name, (attrs, methods) in DEP_ATTRS.items():
            if name in given and given[name] is not None:
                out[name] = given[name]          # explicit always wins
                continue
            for a in attrs:
                obj = getattr(self.node, a, None)
                if obj is not None and all(callable(getattr(obj, m, None)) for m in methods):
                    out[name] = obj
                    break
        return out

    def _make(self, name: str, factory: Callable[[], Any]) -> None:
        try:
            self.services[name] = factory()
        except Exception as e:                    # never stop the node
            self.skipped[name] = f"{type(e).__name__}: {e}"
            self._fail(f"build:{name}", e)

    def _need(self, name: str, *dep_names: str) -> Optional[List[Any]]:
        missing = [d for d in dep_names if d not in self.deps]
        if missing:
            self.skipped[name] = "missing dependency: " + ", ".join(missing)
            return None
        return [self.deps[d] for d in dep_names]

    # ----------------------------------------------------------------- building
    def _build_services(self) -> None:
        g, bc = self._g, self.bc
        # self-contained (only need the chain)
        self._make("wallet_connect",   lambda: g.WalletConnectV2(bc))
        self._make("cross_shard",      lambda: g.CrossShardRouter(bc))
        self._make("compressor",       lambda: g.ChainDataCompressor(bc))
        self._make("wallet_backup",    lambda: g.WalletBackupManager(bc))
        self._make("oracle_v3",        lambda: g.OracleV3(bc))
        self._make("gov_simulation",   lambda: g.GovernanceSimulation(bc))
        self._make("exchange_info",    lambda: g.ExchangeListingInfo())
        # consensus-sensitive name: created, report-only, never called by the layer
        self._make("staking_v3",       lambda: g.StakingRewardsV3(bc))
        # optional dependency
        self._make("defi_analytics",   lambda: g.DeFiAnalyticsV2(bc, self.deps.get("oracle")))
        self._make("institutional",    lambda: g.InstitutionalGrade(bc, self.deps.get("compliance")))
        # need extra objects
        d = self._need("fee_share", "venbl")
        if d:
            self._make("fee_share", lambda: g.FeeShareV2(bc, d[0]))
        d = self._need("validator_rotation", "validator_set", "rng")
        if d:   # consensus-sensitive name: report-only
            self._make("validator_rotation", lambda: g.ValidatorRotation(d[0], bc, d[1]))
        d = self._need("royalty_middleware", "nft", "royalty_engine")
        if d:
            self._make("royalty_middleware",
                       lambda: g.RoyaltyEnforcementMiddleware(d[0], d[1], bc))
        d = self._need("api_gateway", "rest_api")
        if d:
            self._make("api_gateway", lambda: g.APIGateway(d[0], bc))

    def _wrap_mempool(self) -> None:
        """Count Mempool.submit results. The original result is returned unchanged."""
        try:
            mp = self.bc.mempool
            orig = mp.submit
            self._mp_had_own = "submit" in getattr(mp, "__dict__", {})
            layer_ref = weakref.ref(self)

            def submit_counted(*a, **k):
                res = orig(*a, **k)               # original behaviour first; exceptions propagate as before
                layer = layer_ref()
                if layer is not None:
                    try:
                        accepted = bool(res[0]) if isinstance(res, tuple) else bool(res)
                        with layer._lock:
                            layer.counters["mempool_accepted" if accepted else "mempool_rejected"] += 1
                    except Exception as e:
                        layer._fail("mempool.count", e)
                return res

            self._mp_orig = orig
            mp.submit = submit_counted
            self._mp_target = mp
        except Exception as e:
            self.skipped["mempool_counter"] = f"{type(e).__name__}: {e}"
            self._fail("wrap_mempool", e)

    # ----------------------------------------------------- per-use object factories
    def compact_block(self, block: Any):
        return self._g.CompactBlockV2(block)

    def utxo_snapshot(self, height: Optional[int] = None):
        h = self.bc.height if height is None else height
        return self._g.UTXOSnapshotV2(self.bc.utxo, h)

    def new_multisig(self, participants: List[bytes]):
        return self._g.SchnorrMultiSig(participants)

    def new_cross_shard_tx(self, *args, **kw):
        return self._g.CrossShardTransaction(*args, **kw)

    def new_mimblewimble_tx(self, inputs: List[int], outputs: List[int], kernel_excess: int):
        return self._g.MimbleWimbleTx(inputs, outputs, kernel_excess)

    def run_final_tests(self) -> dict:
        """On demand only. FinalTestSuite builds its OWN fresh chains; it never touches this node."""
        return self._g.FinalTestSuite().run_all()

    # ----------------------------------------------------------- chain listener API
    def on_connect(self, block: Any) -> None:
        try:
            with self._lock:
                self.counters["blocks_seen"] += 1
                self.last_height = getattr(block, "height", self.last_height)
            comp = self.services.get("compressor")
            if comp is not None:
                comp.store_compressed(block)
                self._trim(comp)
        except Exception as e:
            self._fail("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        try:
            with self._lock:
                self.counters["reorgs_seen"] += 1
            comp = self.services.get("compressor")
            if comp is not None:
                for h in [h for h in list(comp._compressed) if h > ancestor_height]:
                    comp._compressed.pop(h, None)
        except Exception as e:
            self._fail("on_reorg", e)

    def _trim(self, comp: Any) -> None:
        extra = len(comp._compressed) - self.max_blocks
        if extra > 0:
            for h in sorted(comp._compressed)[:extra]:
                comp._compressed.pop(h, None)

    # ----------------------------------------------------------------- reporting
    _STATS = {
        "wallet_connect": "wc_stats", "fee_share": "fee_share_v2_stats",
        "staking_v3": "v3_staking_stats", "cross_shard": "router_stats",
        "validator_rotation": "rotation_stats", "compressor": "compression_stats",
        "wallet_backup": "backup_stats", "oracle_v3": "oracle_v3_stats",
        "royalty_middleware": "enforcement_stats", "institutional": "institutional_stats",
        "api_gateway": "gateway_stats",
    }

    def stats(self) -> dict:
        out: Dict[str, Any] = {
            "errors": self.errors, "last_error": self.last_error,
            "last_height": self.last_height, "counters": dict(self.counters),
            "active": sorted(self.services), "skipped": dict(self.skipped),
        }
        for name, meth in self._STATS.items():
            svc = self.services.get(name)
            if svc is None:
                continue
            try:
                out[name] = getattr(svc, meth)()
            except Exception as e:
                self._fail(f"stats:{name}", e)
        return out

    # ------------------------------------------------------------------- detaching
    def detach(self) -> None:
        try:
            self.node.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer55.detach", exc_info=True)
        mp = self._mp_target
        if mp is not None:
            try:
                if self._mp_had_own:
                    mp.submit = self._mp_orig
                else:
                    del mp.submit                 # falls back to the class method
            except Exception as e:
                self._fail("detach_mempool", e)
            self._mp_target = None


# ---------------------------------------------------------------------- install
def install(host: Any, deps: Optional[Dict[str, Any]] = None, max_blocks: int = 2000) -> None:
    """Patch host.NEBULAFullNode.__init__ so each new node gets node.group55."""
    # If the host runs as a script (__main__), make group55's `import nebula_v10_11`
    # resolve to the SAME module instead of loading a second copy.
    if getattr(host, "__name__", "") == "__main__" and "nebula_v10_11" not in sys.modules:
        sys.modules["nebula_v10_11"] = host
    cls = host.NEBULAFullNode
    if getattr(cls, "_g55_orig", None):
        return
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)
        try:
            layer = Layer55(self, deps=deps, max_blocks=max_blocks)
            self.group55 = layer
            self.bc.add_listener(layer)
        except Exception as e:                    # node must still start
            self.group55_error = e

    patched.__wrapped__ = orig
    cls._g55_orig = orig
    cls.__init__ = patched


def uninstall(host: Any, detach_live: bool = True) -> None:
    cls = host.NEBULAFullNode
    o = getattr(cls, "_g55_orig", None)
    if o:
        cls.__init__ = o
        del cls._g55_orig
    if detach_live:
        for layer in list(_LIVE):
            layer.detach()
