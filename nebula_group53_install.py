"""nebula_group53_install.py - wiring layer for the 20 group53 classes.

Usage (from inside nebula_v10_11.py, after NEBULAFullNode is defined, or from a launcher):

    import nebula_group53_install as g53
    g53.install(host_module)             # patches NEBULAFullNode.__init__ (idempotent)
    ...
    node = NEBULAFullNode(...)           # node.group53 is now a Layer53
    node.group53.status()                # what is wired, what was skipped and why
    g53.uninstall(host_module)           # restores the original __init__

Design rules (same as group5):
  * nebula_v10_11.py is never edited; nebula_group53.py (verbatim classes) is never edited.
  * The layer NEVER rejects a block / tx. Every callback runs inside try/except; failures are
    counted in layer.errors and kept in layer.error_log. A failing layer must not stop the node.
  * Observe-only by default: the only chain-driven work is (a) crediting block rewards into
    ValidatorRewardsV2 (its own in-memory ledger) and (b) periodic ChainSnapshotManager snapshots.
    Anything that mutates host state (ChainPruning) is OFF unless allow_state_mutation=True.
  * Reorg-safe: rewards credited and snapshots taken for blocks that were reorged away are rolled back.
"""
from __future__ import annotations

import collections
import importlib
import json
import logging
import sys
import threading
import time
from typing import Any, Callable, Dict, List, Optional, Tuple
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

HOST_MODULE_NAME = "nebula_v10_11"
GROUP_MODULE_NAME = "nebula_group53"

log = logging.getLogger("nebula.group53")

# Host classes the group relies on (from the guide). Used by `--check` and by status().
HOST_CLASSES_NEEDED = (
    "BlockHeader", "MerkleTree", "NEBULABlockchain", "NEBULAWallet", "Transaction",   # live host classes
    "TransactionOutput", "NBL721Registry", "OracleV2", "ZKRollupLayer", "AdvancedDEXV2",
    "GovernanceV3", "OptionsProtocolV2", "SyntheticAssetProtocol", "P2PKHScript",     # other groups
)

DEFAULT_CONFIG: Dict[str, Any] = {
    "snapshot_interval": 144,        # take a chain snapshot every N blocks (0 = never)
    "max_snapshots": 50,             # keep at most this many snapshots in RAM
    "max_reward_log": 5000,          # blocks remembered for reorg rollback of rewards
    "allow_state_mutation": False,   # ChainPruning touches host UTXO index -> off by default
    "prune_interval": 0,             # with allow_state_mutation: prune every N blocks (0 = never)
    "create_missing_deps": True,     # build own OracleV2/NBL721Registry/... if the node has none
    "register_routes": True,         # add read-only GET /api/group53/* routes to the host REST table
    "miner_address": None,           # for BlockTemplateV2; auto-detected from node/wallet if None
    "deps": {},                      # explicit overrides: {"oracle": obj, "nft": obj, "dex": obj, ...}
    "disable": (),                   # component names to skip entirely
}

# ---------------------------------------------------------------------------------------------
# Dependency discovery (duck-typed, because the exact attribute names of NEBULAFullNode are not
# part of the group files). Order: explicit override -> node attrs -> chain attrs -> any attr that
# quacks right -> (optional) own instance built from the host classes.
# ---------------------------------------------------------------------------------------------
_DEP_NAMES: Dict[str, Tuple[str, ...]] = {
    "governance":        ("governance_v3", "governance", "gov", "governance_engine"),
    "oracle":            ("oracle_v2", "oracle", "price_oracle"),
    "nft":               ("nft", "nft_registry", "nbl721", "nbl721_registry"),
    "consensus_metrics": ("consensus_metrics", "metrics", "cm"),
    "dex":               ("dex", "nebula_dex", "dex_amm"),
    "dex_v3":            ("dex_v3", "dexv3"),
}


def _has(obj: Any, *names: str) -> bool:
    return all(callable(getattr(obj, n, None)) for n in names)


_DEP_QUACKS: Dict[str, Callable[[Any], bool]] = {
    "governance":        lambda o: _has(o, "propose", "vote"),
    "oracle":            lambda o: _has(o, "price", "update_price"),
    "nft":               lambda o: _has(o, "create_collection", "mint"),
    "consensus_metrics": lambda o: _has(o, "consensus_health"),
    "dex":               lambda o: _has(o, "quote_amm", "swap_amm"),
    "dex_v3":            lambda o: _has(o, "swap") and _has(o, "create_pool"),
}


def _block_hash(block: Any) -> Optional[str]:
    for src in (block, getattr(block, "header", None)):
        if src is None:
            continue
        h = getattr(src, "hash", None)
        if callable(h):
            try:
                h = h()
            except Exception:
                h = None
        if isinstance(h, str) and h:
            return h
    return None


def _jsonable(obj: Any) -> Any:
    return json.loads(json.dumps(obj, default=str))


# ---------------------------------------------------------------------------------------------
# The layer
# ---------------------------------------------------------------------------------------------
class Layer53:
    """Owns one instance of every group53 service and reacts to chain events."""

    # (component attr, class name, role) in wiring order (guide step 4 order)
    PLAN: Tuple[Tuple[str, str, str], ...] = (
        ("liquid_democracy",   "LiquidDemocracy",        "contract/economy"),
        ("tx_coalescer",       "TransactionCoalescer",   "utility"),
        ("snapshot_manager",   "ChainSnapshotManager",   "storage/backup (chain-driven)"),
        ("validator_rewards",  "ValidatorRewardsV2",     "chain listener (report-only)"),
        ("consensus_analytics", "ConsensusAnalytics",    "pull-based report (report-only)"),
        ("wallet_analytics",   "WalletAnalytics",        "wallet/REST"),
        ("yield_farm_v3",      "YieldFarmV3",            "per-farm object (made by registry)"),
        ("farm_registry",      "YieldFarmRegistryV3",    "contract/economy"),
        ("safety_module",      "DeFiSafetyModule",       "contract/economy"),
        ("treasury",           "TreasuryDiversification", "contract/economy"),
        ("forum",              "GovernanceForumV2",      "contract/economy"),
        ("nft_auction",        "NFTAuction",             "per-auction object (made by marketplace)"),
        ("nft_marketplace",    "NFTMarketplaceV3",       "contract/economy"),
        ("insurance_pool",     "StakingInsurancePoolV2", "contract/economy"),
        ("chain_pruning",      "ChainPruning",           "maintenance (mutating, gated)"),
        ("test_suite",         "ExtendedTestSuiteV2",    "manual test runner"),
        ("block_template",     "BlockTemplateV2",        "mining helper (lazy, needs miner address)"),
        ("swap_aggregator",    "SwapAggregatorV2",       "contract/economy"),
        ("royalty_dao",        "NFTRoyaltyDAO",          "contract/economy"),
        ("prediction_oracle",  "PredictionOracle",       "oracle helper"),
    )

    def __init__(self, node: Any, host: Any = None, group: Any = None, **config: Any):
        unknown = set(config) - set(DEFAULT_CONFIG)
        if unknown:
            raise TypeError(f"unknown Layer53 option(s): {sorted(unknown)}")
        self.node = node
        self.host = host
        self.g = group if group is not None else _load_group(host)
        self.bc = node.bc
        self.cfg: Dict[str, Any] = {**DEFAULT_CONFIG, **config}
        self.cfg["deps"] = dict(self.cfg.get("deps") or {})
        self.errors = 0
        self.query_errors = 0
        self.error_log: collections.deque = collections.deque(maxlen=50)
        self.stats_: Dict[str, int] = collections.defaultdict(int)
        self.components: Dict[str, Any] = {}
        self.component_status: Dict[str, Dict[str, str]] = {}
        self.dep_sources: Dict[str, str] = {}
        self._deps: Dict[str, Any] = {}
        self._lock = threading.RLock()
        self._reward_log: "collections.OrderedDict[str, Tuple[int, str, int, int]]" = collections.OrderedDict()
        self._snap_meta: Dict[str, int] = {}          # block-hash (or "height:N") -> snapshot height
        self._detached = False
        self._build_components()

    # -- attribute access to components: layer.forum, layer.validator_rewards, ... ---------------
    def __getattr__(self, name: str) -> Any:
        comps = self.__dict__.get("components")
        if comps is not None and name in comps:
            return comps[name]
        raise AttributeError(name)

    # ===========================================================================================
    # construction
    # ===========================================================================================
    def _dep(self, kind: str) -> Any:
        if kind in self._deps:
            return self._deps[kind]
        obj, src = self._discover(kind)
        self._deps[kind] = obj
        if obj is not None:
            self.dep_sources[kind] = src
        return obj

    def _discover(self, kind: str) -> Tuple[Any, str]:
        quack = _DEP_QUACKS[kind]
        explicit = self.cfg["deps"].get(kind)
        if explicit is not None:
            return explicit, "explicit"
        for label, src in (("node", self.node), ("bc", self.bc)):
            for n in _DEP_NAMES[kind]:
                try:
                    obj = getattr(src, n, None)
                except Exception:
                    obj = None
                if obj is not None and quack(obj):
                    return obj, f"{label}.{n}"
        try:
            items = list(vars(self.node).items())
        except TypeError:
            items = []
        for n, obj in items:
            if obj is not None and obj is not self and not n.startswith("__"):
                try:
                    if quack(obj):
                        return obj, f"node.{n} (duck-typed)"
                except Exception:
                    continue
        if self.cfg["create_missing_deps"] and self.host is not None:
            made = self._own_instance(kind)
            if made is not None:
                return made, "own instance (fallback - NOT shared with the node)"
        return None, ""

    def _own_instance(self, kind: str) -> Any:
        h, bc = self.host, self.bc
        tries: Dict[str, List[Callable[[], Any]]] = {
            "oracle":            [lambda: h.OracleV2(bc)],
            "nft":               [lambda: h.NBL721Registry()],
            "governance":        [lambda: h.GovernanceV3(bc)],
            "consensus_metrics": [lambda: h.ConsensusMetrics(bc), lambda: h.ConsensusMetrics()],
        }
        for t in tries.get(kind, []):
            try:
                obj = t()
                if _DEP_QUACKS[kind](obj):
                    return obj
            except Exception:
                continue
        return None

    def _miner_address(self) -> Optional[str]:
        if self.cfg.get("miner_address"):
            return self.cfg["miner_address"]
        n = self.node
        for name in ("miner_address", "mining_address", "miner_addr"):
            v = getattr(n, name, None)
            if isinstance(v, str) and v:
                return v
        for holder in ("wallet", "miner"):
            w = getattr(n, holder, None)
            if w is None:
                continue
            for name in ("first_address", "address", "miner_address"):
                v = getattr(w, name, None)
                if isinstance(v, str) and v:
                    return v
        return None

    def _set_status(self, attr: str, cls_name: str, role: str, state: str, detail: str = "") -> None:
        self.component_status[attr] = {"class": cls_name, "role": role, "state": state, "detail": detail}

    def _make(self, attr: str, cls_name: str, role: str,
              factory: Callable[[Any, Dict[str, Any]], Any],
              required: Tuple[str, ...] = (), optional: Tuple[str, ...] = ()) -> None:
        if attr in self.cfg["disable"]:
            self._set_status(attr, cls_name, role, "disabled", "disabled by config")
            return
        cls = getattr(self.g, cls_name, None)
        if cls is None:
            self._set_status(attr, cls_name, role, "failed", f"{cls_name} not found in {GROUP_MODULE_NAME}")
            return
        deps: Dict[str, Any] = {}
        for kind in required:
            obj = self._dep(kind)
            if obj is None:
                self._set_status(attr, cls_name, role, "skipped", f"missing required dependency: {kind}")
                return
            deps[kind] = obj
        for kind in optional:
            deps[kind] = self._dep(kind)
        try:
            inst = factory(cls, deps)
        except Exception as e:  # constructor failure must never stop the node
            self.errors += 1
            self._remember_error(f"construct {cls_name}", e)
            self._set_status(attr, cls_name, role, "failed", f"{type(e).__name__}: {e}")
            return
        self.components[attr] = inst
        used = ", ".join(f"{k}<-{self.dep_sources.get(k, 'none')}" for k in (*required, *optional) if deps.get(k) is not None)
        self._set_status(attr, cls_name, role, "ok", used)

    def _build_components(self) -> None:
        bc = self.bc
        self._make("liquid_democracy", "LiquidDemocracy", self.PLAN[0][2],
                   lambda C, d: C(bc, d["governance"]), optional=("governance",))
        self._make("tx_coalescer", "TransactionCoalescer", self.PLAN[1][2], lambda C, d: C(bc))
        self._make("snapshot_manager", "ChainSnapshotManager", self.PLAN[2][2], lambda C, d: C(bc))
        self._make("validator_rewards", "ValidatorRewardsV2", self.PLAN[3][2], lambda C, d: C(bc))
        self._make("consensus_analytics", "ConsensusAnalytics", self.PLAN[4][2],
                   lambda C, d: C(bc, d["consensus_metrics"]), required=("consensus_metrics",))
        self._make("wallet_analytics", "WalletAnalytics", self.PLAN[5][2], lambda C, d: C(bc))
        # YieldFarmV3 objects are created by YieldFarmRegistryV3 / new_farm(); the registry goes first.
        self._make("farm_registry", "YieldFarmRegistryV3", self.PLAN[7][2], lambda C, d: C(bc))
        self._via_parent("yield_farm_v3", "YieldFarmV3", self.PLAN[6][2], "farm_registry")
        self._make("safety_module", "DeFiSafetyModule", self.PLAN[8][2], lambda C, d: C(bc))
        self._make("treasury", "TreasuryDiversification", self.PLAN[9][2],
                   lambda C, d: C(bc, d["oracle"]), optional=("oracle",))
        self._make("forum", "GovernanceForumV2", self.PLAN[10][2], lambda C, d: C(bc))
        self._make("nft_marketplace", "NFTMarketplaceV3", self.PLAN[12][2],
                   lambda C, d: C(d["nft"], bc), required=("nft",))
        self._via_parent("nft_auction", "NFTAuction", self.PLAN[11][2], "nft_marketplace")
        self._make("insurance_pool", "StakingInsurancePoolV2", self.PLAN[13][2], lambda C, d: C(bc))
        self._make("chain_pruning", "ChainPruning", self.PLAN[14][2], lambda C, d: C(bc))
        self._make("test_suite", "ExtendedTestSuiteV2", self.PLAN[15][2], lambda C, d: C())
        self._build_block_template()
        self._make("swap_aggregator", "SwapAggregatorV2", self.PLAN[17][2],
                   lambda C, d: C(d["dex"], d["dex_v3"], d["oracle"]),
                   required=("dex",), optional=("dex_v3", "oracle"))
        self._make("royalty_dao", "NFTRoyaltyDAO", self.PLAN[18][2],
                   lambda C, d: C(bc, d["nft"]), required=("nft",))
        self._make("prediction_oracle", "PredictionOracle", self.PLAN[19][2],
                   lambda C, d: C(d["oracle"]), required=("oracle",))

    def _via_parent(self, attr: str, cls_name: str, role: str, parent: str) -> None:
        if self.component_status.get(parent, {}).get("state") == "ok" and getattr(self.g, cls_name, None):
            self._set_status(attr, cls_name, role, "ok", f"created through {parent}")
        else:
            self._set_status(attr, cls_name, role, "skipped", f"parent {parent} not available")

    def _build_block_template(self) -> None:
        attr, cls_name, role = "block_template", "BlockTemplateV2", self.PLAN[16][2]
        addr = self._miner_address()
        if not addr:
            self._set_status(attr, cls_name, role, "deferred",
                             "no miner address found; call layer.build_block_template(miner=...)")
            return
        self.dep_sources["miner"] = "configured/auto-detected"
        self._make(attr, cls_name, role, lambda C, d: C(self.bc, addr))

    # ===========================================================================================
    # error handling
    # ===========================================================================================
    def _remember_error(self, where: str, exc: BaseException) -> None:
        self.error_log.append({"where": where, "error": f"{type(exc).__name__}: {exc}", "ts": time.time()})
        log.warning("group53 %s failed: %s: %s", where, type(exc).__name__, exc)

    def _guard(self, where: str, fn: Callable[..., Any], *args: Any) -> Any:
        try:
            return fn(*args)
        except Exception as e:  # a layer failure must never reach the node
            self.errors += 1
            self._remember_error(where, e)
            return None

    @property
    def last_error(self) -> Optional[Dict[str, Any]]:
        return self.error_log[-1] if self.error_log else None

    # ===========================================================================================
    # chain listener protocol:  bc.add_listener(layer) -> on_connect(block) / on_reorg(old, new, h)
    # ===========================================================================================
    def on_connect(self, block: Any) -> None:
        try:
            with self._lock:
                if self._detached:
                    return
                self.stats_["blocks_seen"] += 1
                height = self._block_height(block)
                bhash = _block_hash(block)
                self._guard("rewards.credit", self._hook_rewards, block, height, bhash)
                self._guard("snapshot", self._hook_snapshot, height, bhash)
                self._guard("pruning", self._hook_pruning, height)
        except Exception as e:  # defensive: even lock/stat failures stay inside the layer
            self.errors += 1
            self._remember_error("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        try:
            with self._lock:
                if self._detached:
                    return
                self.stats_["reorgs_seen"] += 1
                try:
                    anc = int(ancestor_height)
                except (TypeError, ValueError):
                    anc = -1
                self._guard("rewards.rollback", self._rollback_rewards, old, new, anc)
                self._guard("snapshot.rollback", self._rollback_snapshots, old, new, anc)
        except Exception as e:
            self.errors += 1
            self._remember_error("on_reorg", e)

    def detach(self) -> None:
        self._detached = True
        try:
            rm = getattr(self.bc, "remove_listener", None)
            if callable(rm):
                rm(self)
            else:
                self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer53.detach", exc_info=True)

    # -- helpers -----------------------------------------------------------------------------
    def _block_height(self, block: Any) -> int:
        tip = getattr(self.bc, "tip", None)
        bh = _block_hash(block)
        if bh is not None and tip is not None and _block_hash(tip) == bh:
            return int(self.bc.height)
        for src in (block, getattr(block, "header", None)):
            v = getattr(src, "height", None) if src is not None else None
            if isinstance(v, int) and not isinstance(v, bool) and v > 0:
                return v
        return int(self.bc.height)

    def _coinbase_address(self, block: Any) -> Optional[str]:
        txs = getattr(block, "txs", None) or getattr(block, "transactions", None) or []
        if not txs:
            return None
        foundation = getattr(self.g, "FOUNDATION_ADDRESS", None)
        addrs = [a for a in (getattr(o, "address", None) for o in (getattr(txs[0], "outputs", None) or []))
                 if isinstance(a, str) and a]
        for a in addrs:
            if a != foundation:
                return a
        return addrs[0] if addrs else None

    @staticmethod
    def _hash_set(seq: Any) -> set:
        if seq is None:
            return set()
        if isinstance(seq, str) or hasattr(seq, "header"):
            seq = [seq]
        try:
            items = list(seq)
        except TypeError:
            return set()
        out = set()
        for it in items:
            h = it if isinstance(it, str) else _block_hash(it)
            if h:
                out.add(h)
        return out

    @staticmethod
    def _stale_keys(known: Dict[str, int], old: Any, new: Any, ancestor: int) -> List[str]:
        """Keys (block hashes) that belong to the abandoned branch.

        Works whether the host notifies the reorg before or after the new branch was connected:
        a key is stale if it is in `old` and not in `new`; if `old` cannot be parsed we fall back to
        'height above the common ancestor and not part of the new branch'."""
        old_h, new_h = Layer53._hash_set(old), Layer53._hash_set(new)
        stale = []
        for key, height in known.items():
            if key in new_h:
                continue
            if key in old_h:
                stale.append(key)
            elif (key.startswith("height:") or not old_h) and height > ancestor:
                stale.append(key)
        return stale

    # -- ValidatorRewardsV2 -------------------------------------------------------------------
    def _hook_rewards(self, block: Any, height: int, bhash: Optional[str]) -> None:
        vr = self.components.get("validator_rewards")
        if vr is None:
            return
        addr = self._coinbase_address(block)
        if not addr:
            self.stats_["blocks_without_coinbase_address"] += 1
            return
        key = bhash or f"height:{height}"
        if key in self._reward_log:        # same block delivered twice: never double-credit
            return
        with vr._lock:
            before_r, before_b = vr._rewards.get(addr, 0), vr._blocks.get(addr, 0)
        vr.credit_block(addr, height)
        with vr._lock:
            d_r = vr._rewards.get(addr, 0) - before_r
            d_b = vr._blocks.get(addr, 0) - before_b
        self._reward_log[key] = (height, addr, d_r, d_b)
        while len(self._reward_log) > int(self.cfg["max_reward_log"]):
            self._reward_log.popitem(last=False)
        self.stats_["rewards_credited"] += 1

    def _rollback_rewards(self, old: Any, new: Any, ancestor: int) -> None:
        vr = self.components.get("validator_rewards")
        if vr is None or not self._reward_log:
            return
        known = {k: v[0] for k, v in self._reward_log.items()}
        for key in self._stale_keys(known, old, new, ancestor):
            _h, addr, d_r, d_b = self._reward_log.pop(key)
            with vr._lock:
                left = max(0, vr._rewards.get(addr, 0) - d_r)
                blocks = max(0, vr._blocks.get(addr, 0) - d_b)
                if left or addr in vr._mev:
                    vr._rewards[addr] = left
                else:
                    vr._rewards.pop(addr, None)
                if blocks:
                    vr._blocks[addr] = blocks
                else:
                    vr._blocks.pop(addr, None)
            self.stats_["rewards_rolled_back"] += 1

    # -- ChainSnapshotManager -----------------------------------------------------------------
    def _hook_snapshot(self, height: int, bhash: Optional[str]) -> None:
        sm = self.components.get("snapshot_manager")
        interval = int(self.cfg["snapshot_interval"])
        if sm is None or interval <= 0 or height <= 0 or height % interval:
            return
        snap = sm.take_snapshot()
        snap_h = int(snap.get("height", height)) if isinstance(snap, dict) else height
        # take_snapshot() is keyed by height and overwrites an older snapshot of the same height
        # (e.g. one taken on a branch that has since been reorged away) -> forget the old owner.
        for k in [k for k, v in self._snap_meta.items() if v == snap_h]:
            self._snap_meta.pop(k, None)
        self._snap_meta[bhash or f"height:{snap_h}"] = snap_h
        self.stats_["snapshots_taken"] += 1
        self._trim_snapshots(sm)

    def _trim_snapshots(self, sm: Any) -> None:
        limit = int(self.cfg["max_snapshots"])
        with sm._lock:
            while len(sm._snapshots) > max(1, limit):
                oldest = min(sm._snapshots)
                sm._snapshots.pop(oldest, None)
                for k in [k for k, v in self._snap_meta.items() if v == oldest]:
                    self._snap_meta.pop(k, None)

    def _rollback_snapshots(self, old: Any, new: Any, ancestor: int) -> None:
        sm = self.components.get("snapshot_manager")
        if sm is None or not self._snap_meta:
            return
        for key in self._stale_keys(dict(self._snap_meta), old, new, ancestor):
            height = self._snap_meta.pop(key)
            if height in self._snap_meta.values():      # a live snapshot already replaced it
                continue
            with sm._lock:
                sm._snapshots.pop(height, None)
            self.stats_["snapshots_rolled_back"] += 1

    # -- ChainPruning (gated) -------------------------------------------------------------------
    def _hook_pruning(self, height: int) -> None:
        interval = int(self.cfg["prune_interval"])
        if not self.cfg["allow_state_mutation"] or interval <= 0 or height <= 0 or height % interval:
            return
        self.run_pruning()

    def run_pruning(self) -> Optional[int]:
        """Run ChainPruning.prune_spent_utxos(); refuses unless allow_state_mutation=True."""
        cp = self.components.get("chain_pruning")
        if cp is None:
            return None
        if not self.cfg["allow_state_mutation"]:
            raise PermissionError("ChainPruning mutates the host UTXO index; start with allow_state_mutation=True")
        n = cp.prune_spent_utxos()
        self.stats_["prune_runs"] += 1
        return n

    # ===========================================================================================
    # on-demand API (what REST routes / CLI / other code call)
    # ===========================================================================================
    def new_farm(self, lp_token: str, total_rewards_nbl: float, duration_days: int) -> Optional[str]:
        fr = self.components.get("farm_registry")
        return fr.create_farm(lp_token, total_rewards_nbl, duration_days) if fr else None

    def build_block_template(self, miner: Optional[str] = None, max_size: Optional[int] = None) -> dict:
        """Lazy BlockTemplateV2 (builds the component on first use if no miner address was known)."""
        bt = self.components.get("block_template")
        if bt is None or (miner and getattr(bt, "_miner", None) != miner):
            addr = miner or self._miner_address()
            if not addr:
                raise ValueError("miner address required")
            bt = self.g.BlockTemplateV2(self.bc, addr)
            self.components["block_template"] = bt
            self._set_status("block_template", "BlockTemplateV2", self.PLAN[16][2], "ok", f"miner={addr[:12]}")
        return bt.build_template(max_size) if max_size else bt.build_template()

    def run_extended_tests(self) -> dict:
        """Run ExtendedTestSuiteV2 (creates throw-away NEBULABlockchain objects - never on a live node)."""
        ts = self.components.get("test_suite")
        if ts is None:
            raise RuntimeError("ExtendedTestSuiteV2 not available")
        return ts.run_all()

    def validators(self, n: int = 10) -> List[dict]:
        vr = self.components.get("validator_rewards")
        return vr.leaderboard(n) if vr else []

    def snapshots(self) -> List[dict]:
        sm = self.components.get("snapshot_manager")
        return sm.list_snapshots() if sm else []

    def security(self) -> dict:
        ca = self.components.get("consensus_analytics")
        if ca is None:
            return {}
        return {"security_score": ca.security_score(), "uncle_rate": ca.uncle_rate()}

    _STATS_CALLS: Tuple[Tuple[str, str], ...] = (
        ("liquid_democracy", "democracy_stats"), ("tx_coalescer", "queue_stats"),
        ("snapshot_manager", "snapshot_stats"), ("safety_module", "safety_stats"),
        ("forum", "forum_v2_stats"), ("nft_marketplace", "marketplace_v3_stats"),
        ("insurance_pool", "pool_stats"), ("chain_pruning", "pruning_stats"),
        ("swap_aggregator", "aggregator_v2_stats"), ("royalty_dao", "dao_stats"),
        ("farm_registry", "all_farms"),
    )

    def all_stats(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        for comp, method in self._STATS_CALLS:
            obj = self.components.get(comp)
            if obj is None:
                continue
            try:
                out[comp] = getattr(obj, method)()
            except Exception as e:
                self.query_errors += 1
                out[comp] = {"error": f"{type(e).__name__}: {e}"}
        return out

    def status(self) -> Dict[str, Any]:
        states = [v["state"] for v in self.component_status.values()]
        return {
            "layer": "group53",
            "attached": not self._detached,
            "coverage": f"{states.count('ok')}/{len(self.PLAN)} classes wired",
            "errors": self.errors,
            "last_error": self.last_error,
            "counters": dict(self.stats_),
            "config": {k: v for k, v in self.cfg.items() if k != "deps"},
            "dependency_sources": dict(self.dep_sources),
            "components": {k: dict(v) for k, v in self.component_status.items()},
        }

    def report(self) -> str:
        s = self.status()
        lines = [f"group53: {s['coverage']} | errors={s['errors']} | counters={s['counters']}"]
        for name, _cls, _role in self.PLAN:
            c = self.component_status.get(name, {"state": "?", "class": _cls, "detail": ""})
            lines.append(f"  [{c['state']:<8}] {c['class']:<24} {c['detail']}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------------------------
# host / group loading
# ---------------------------------------------------------------------------------------------
def _resolve_host(host: Any = None) -> Any:
    if host is None:
        host = sys.modules.get(HOST_MODULE_NAME)
        if host is None:
            main = sys.modules.get("__main__")
            host = main if hasattr(main, "NEBULAFullNode") else importlib.import_module(HOST_MODULE_NAME)
    elif isinstance(host, str):
        host = importlib.import_module(host)
    if not hasattr(host, "NEBULAFullNode"):
        raise AttributeError("host module has no NEBULAFullNode")
    return host


def _load_group(host: Any = None) -> Any:
    """Import nebula_group53 once and make sure it sees the *running* host classes.

    If the host runs as a script (module name __main__), nebula_group53's own optional
    `import nebula_v10_11` would execute the whole host file a second time. We alias the running
    module under its canonical name first, so that import returns the live module instead."""
    if host is not None and sys.modules.get(HOST_MODULE_NAME) is None:
        sys.modules[HOST_MODULE_NAME] = host
    g = importlib.import_module(GROUP_MODULE_NAME)
    if host is not None:
        for k, v in vars(host).items():          # names defined in the host after group53 was first imported
            if not k.startswith("__") and k not in vars(g):
                setattr(g, k, v)
    return g


# ---------------------------------------------------------------------------------------------
# REST routes (read-only GETs, added to the host's own route table)
# ---------------------------------------------------------------------------------------------
_ACTIVE: Optional[Layer53] = None
_ROUTE_PATHS = ("/api/group53/status", "/api/group53/stats", "/api/group53/validators",
                "/api/group53/snapshots", "/api/group53/security")


def _api(fn: Callable[[Layer53, Any], Any]) -> Callable[[Any, Any, Any], Tuple[int, dict]]:
    def handler(path: Any, query: Any, body: Any) -> Tuple[int, dict]:
        layer = _ACTIVE
        if layer is None:
            return 503, {"success": False, "error": "group53 layer not attached"}
        try:
            return 200, {"success": True, "data": _jsonable(fn(layer, query))}
        except Exception as e:
            layer.query_errors += 1
            return 500, {"success": False, "error": f"{type(e).__name__}: {e}"}
    return handler


def _top_n(query: Any) -> int:
    try:
        return max(1, min(100, int((query or {}).get("n", [10])[0])))
    except (TypeError, ValueError, IndexError, AttributeError):
        return 10


_HANDLERS: Dict[str, Callable] = {
    "/api/group53/status":     _api(lambda l, q: l.status()),
    "/api/group53/stats":      _api(lambda l, q: l.all_stats()),
    "/api/group53/validators": _api(lambda l, q: l.validators(_top_n(q))),
    "/api/group53/snapshots":  _api(lambda l, q: l.snapshots()),
    "/api/group53/security":   _api(lambda l, q: l.security()),
}


def _register_routes(host: Any) -> List[str]:
    table = getattr(host, "_routes", None)
    if not isinstance(table, dict):
        return []
    get = table.setdefault("GET", {})
    added = []
    for path, fn in _HANDLERS.items():
        if path not in get:
            get[path] = fn
            added.append(path)
    return added


def _unregister_routes(host: Any) -> None:
    table = getattr(host, "_routes", None)
    if isinstance(table, dict):
        for path, fn in _HANDLERS.items():
            if table.get("GET", {}).get(path) is fn:
                del table["GET"][path]


# ---------------------------------------------------------------------------------------------
# install / uninstall (wrapper around NEBULAFullNode.__init__, same pattern as group5)
# ---------------------------------------------------------------------------------------------
def attach(node: Any, host: Any = None, **options: Any) -> Layer53:
    """Attach a Layer53 to an already-built node (what the patched __init__ does)."""
    global _ACTIVE
    try:
        host = _resolve_host(host)
    except Exception:
        host = None                                 # no host module: own-instance fallbacks are disabled
    layer = Layer53(node, host=host, **options)
    node.bc.add_listener(layer)
    node.group53 = layer
    _ACTIVE = layer
    return layer


def install(host: Any = None, **options: Any) -> Any:
    """Patch host.NEBULAFullNode.__init__ so every new node gets `node.group53`. Idempotent."""
    host = _resolve_host(host)
    _load_group(host)
    cls = host.NEBULAFullNode
    if getattr(cls, "_g53_orig", None):
        return host
    orig = cls.__init__
    register = bool(options.get("register_routes", DEFAULT_CONFIG["register_routes"]))

    def patched(self: Any, *a: Any, **k: Any) -> None:
        orig(self, *a, **k)
        try:
            attach(self, host=host, **options)
        except Exception as e:                      # the node must still start
            self.group53_error = e
            log.warning("group53 attach failed: %s: %s", type(e).__name__, e)

    patched.__wrapped__ = orig                      # type: ignore[attr-defined]
    cls._g53_orig = orig
    cls._g53_routes = _register_routes(host) if register else []
    cls.__init__ = patched
    return host


def uninstall(host: Any = None) -> None:
    """Undo install(): restore __init__, drop routes, detach the layer from already-built nodes."""
    global _ACTIVE
    host = _resolve_host(host)
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g53_orig", None)
    if _ACTIVE is not None:
        _ACTIVE.detach()
        _ACTIVE = None
    _unregister_routes(host)
    if orig:
        cls.__init__ = orig
        del cls._g53_orig
        if hasattr(cls, "_g53_routes"):
            del cls._g53_routes


# ---------------------------------------------------------------------------------------------
# CLI:  python3 nebula_group53_install.py --check      (needs nebula_v10_11.py next to this file)
# ---------------------------------------------------------------------------------------------
def _check() -> int:
    print("importing host ...")
    try:
        host = importlib.import_module(HOST_MODULE_NAME)
    except Exception as e:
        print(f"FAIL: cannot import {HOST_MODULE_NAME}: {type(e).__name__}: {e}")
        return 2
    g = _load_group(host)
    missing = [n for n in HOST_CLASSES_NEEDED if not hasattr(host, n) and not hasattr(g, n)]
    print("host classes needed by group53:", "all present" if not missing else f"MISSING {missing}")
    print("NEBULAFullNode:", "present" if hasattr(host, "NEBULAFullNode") else "MISSING")
    gm = [n for _, n, _ in Layer53.PLAN if not hasattr(g, n)]
    print("group53 classes:", "all 20 present" if not gm else f"MISSING {gm}")
    return 1 if (missing or gm or not hasattr(host, "NEBULAFullNode")) else 0


if __name__ == "__main__":
    sys.exit(_check())
