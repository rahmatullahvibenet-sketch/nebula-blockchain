"""NEBULA group45 - install layer (wires the 20 group45 classes into a running node).

Design rules
------------
* nebula_v10_11.py is NEVER edited.  nebula_group45.py is NEVER edited.
* The layer is attached by wrapping NEBULAFullNode.__init__ (install / uninstall),
  exactly like group 5.  If the layer fails to build, the node still starts
  (the error is stored in node.group45_error).
* Every callback runs inside a guard: an exception is counted and logged, it is
  never raised into the chain.  The layer never rejects a block or a transaction.
* Consensus-sensitive classes (ConsensusMetrics, ValidatorRewardTracker) are
  REPORT-ONLY: they read blocks, they never change consensus rules.
* Host dependencies (dex, oracle, nft registry, ...) are found by class name on
  the node / blockchain object, or can be passed explicitly (deps={...}).

Usage
-----
    import nebula_v10_11 as host
    import nebula_group45_install as g45
    g45.install(host)              # patch NEBULAFullNode.__init__
    node = host.NEBULAFullNode(...)  # node.group45 is now the layer
    print(node.group45.status())
    print(node.group45.report())
    g45.uninstall(host)            # restore the original __init__

Manual attach (no patching):
    layer = g45.attach(node, deps={"dex": my_dex})
"""
from __future__ import annotations

import functools
import logging
import threading
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Callable, Deque, Dict, List, Optional, Tuple

import nebula_group45 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group45")

# --------------------------------------------------------------------------
# Host dependency roles -> host class names (matched against the MRO of the
# attributes found on the node and on node.bc).
# --------------------------------------------------------------------------
ROLE_TYPES: Dict[str, Tuple[str, ...]] = {
    "dex":           ("NEBULADex",),
    "oracle":        ("OracleV2",),
    "lending":       ("LendingProtocol",),
    "order_book":    ("OrderBookManager",),
    "nft_registry":  ("NBL721Registry",),
    "venbl":         ("VoteEscrowedNBL",),
    "governance":    ("GovernanceEngine",),
    "validator_set": ("ValidatorSetManager",),
    "api":           ("NodeRESTAPI",),
}


@dataclass
class Group45Config:
    confirmations: int = 6          # blocks a block must be buried before rewards are recorded
    snapshot_interval: int = 144    # ArchiveNode state snapshot every N blocks
    snapshot_cap: int = 1000        # max snapshots kept in RAM
    receipt_cap: int = 100_000      # max tx receipts kept in RAM
    error_log_cap: int = 200        # last N error records kept
    enabled: Optional[set] = None   # None = all parts; or a set of part names
    proposer_fn: Optional[Callable[[Any], Optional[str]]] = None  # custom block -> proposer address


@dataclass
class Spec:
    part: str                                   # attribute / key name on the layer
    cls: str                                    # class name inside nebula_group45
    required: Dict[str, str] = field(default_factory=dict)                 # ctor kwarg -> role
    optional: Dict[str, Tuple[str, str]] = field(default_factory=dict)     # ctor kwarg -> (role, private attr)
    nullable: Tuple[str, ...] = ()              # optional kwargs that must be passed as None when unresolved
    feeds: Tuple[str, ...] = ()                 # chain events this part consumes


SPECS: List[Spec] = [
    # ---- chain listeners (fed from on_connect / on_reorg) ----
    Spec("consensus_metrics", "ConsensusMetrics",
         required={"blockchain": "blockchain"}, feeds=("connect", "reorg")),
    Spec("fee_history", "FeeHistoryAnalyzer",
         required={"blockchain": "blockchain"}, feeds=("connect",)),
    Spec("validator_rewards", "ValidatorRewardTracker",
         required={"blockchain": "blockchain"},
         optional={"validator_set": ("validator_set", "_vs")},
         nullable=("validator_set",), feeds=("connect", "reorg")),
    Spec("archive", "ArchiveNode",
         required={"blockchain": "blockchain"}, feeds=("connect", "reorg")),
    # ---- services (called by node code / API, no chain feed) ----
    Spec("order_router", "SmartOrderRouter",
         required={"dex": "dex"}, optional={"order_book": ("order_book", "_ob")}),
    Spec("token_economics", "TokenEconomicsV2",
         required={"blockchain": "blockchain"}, optional={"oracle": ("oracle", "_oracle")}),
    Spec("liquidity", "LiquidityAggregator",
         required={"dex": "dex"}, optional={"lending": ("lending", "_lending")}),
    Spec("gas_station", "GasStation",
         required={"blockchain": "blockchain"}, optional={"oracle": ("oracle", "_oracle")}),
    Spec("passport_registry", "DeFiPassportRegistry",
         required={"blockchain": "blockchain"}),
    Spec("insurance_fund", "InsuranceFund",
         required={"blockchain": "blockchain"}),
    Spec("royalty_engine", "RoyaltyEngine",
         required={"nft_registry": "nft_registry", "blockchain": "blockchain"}),
    Spec("staking_boost", "StakingBoost",
         required={"venbl": "venbl", "nft": "nft_registry"}),
    Spec("tx_mixer", "TransactionMixer",
         required={"blockchain": "blockchain"}),
    Spec("security_analyzer", "EconomicSecurityAnalyzer",
         required={"blockchain": "blockchain"}, optional={"oracle": ("oracle", "_oracle")}),
    Spec("governance_analytics", "GovernanceAnalytics",
         required={"governance": "governance", "blockchain": "blockchain"}),
    Spec("health_check", "NodeHealthCheck",
         required={"blockchain": "blockchain"}, optional={"api": ("api", "_api")}),
    Spec("cross_dex_arbitrage", "CrossDEXArbitrage",
         required={"dex1": "dex"}, optional={"order_book": ("order_book", "_ob")}),
]

# Stats method of each part used by Layer45.report()
STAT_METHODS: Dict[str, str] = {
    "consensus_metrics":    "consensus_health",
    "fee_history":          "fee_history_summary",
    "validator_rewards":    "reward_stats",
    "archive":              "archive_stats",
    "token_economics":      "economics_report",
    "gas_station":          "gas_station_stats",
    "passport_registry":    "registry_stats",
    "insurance_fund":       "insurance_fund_stats",
    "royalty_engine":       "royalty_stats",
    "tx_mixer":             "pool_sizes",
    "security_analyzer":    "security_budget",
    "governance_analytics": "governance_summary",
    "health_check":         "run_all",
    "cross_dex_arbitrage":  "arb_stats",
    "liquidity":            "liquidity_map",
}

_PROPOSER_ATTRS = ("proposer", "miner", "validator", "coinbase_address")
_OUTPUT_ADDR_ATTRS = ("address", "addr", "recipient", "to")


class Layer45:
    """Holds the 20 group45 classes and feeds the chain-driven ones.

    Never raises into the chain; never rejects a block or a transaction.
    """

    def __init__(self, node: Any, config: Optional[Group45Config] = None,
                 deps: Optional[Dict[str, Any]] = None):
        self.node = node
        self.cfg = config or Group45Config()
        self._explicit: Dict[str, Any] = dict(deps or {})
        self.errors = 0
        self.error_log: Deque[dict] = deque(maxlen=self.cfg.error_log_cap)
        self.part_errors: Dict[str, int] = {}
        self.part_calls: Dict[str, int] = {}
        self.parts: Dict[str, Any] = {}
        self.skipped: Dict[str, str] = {}
        self.airdrops: Dict[str, Any] = {}
        self.hackathons: Dict[str, Any] = {}
        self.blocks_seen = 0
        self.reorgs_seen = 0
        self.detached = False
        self.started_at = time.time()
        self._lock = threading.RLock()
        self._prev_ts: Optional[float] = None
        self._pending_rewards: Deque[Any] = deque()
        self._last_rewarded_height = -1
        self._build_all()

    # ------------------------------------------------------------------
    # building
    # ------------------------------------------------------------------
    def _wanted(self, part: str) -> bool:
        return self.cfg.enabled is None or part in self.cfg.enabled

    def _resolve(self, role: str) -> Any:
        if role in self._explicit:
            return self._explicit[role]
        if role == "blockchain":
            return getattr(self.node, "bc", None)
        names = ROLE_TYPES.get(role, ())
        for holder in (self.node, getattr(self.node, "bc", None)):
            if holder is None:
                continue
            try:
                values = list(vars(holder).values())
            except TypeError:
                continue
            for v in values:
                if v is self:
                    continue
                if any(k.__name__ in names for k in type(v).__mro__):
                    return v
        return None

    def _build_all(self) -> None:
        for spec in SPECS:
            if not self._wanted(spec.part):
                self.skipped[spec.part] = "disabled by config"
                continue
            self._build_part(spec)

    def _build_part(self, spec: Spec) -> Optional[Any]:
        kwargs: Dict[str, Any] = {}
        for kw, role in spec.required.items():
            obj = self._resolve(role)
            if obj is None:
                self.skipped[spec.part] = f"missing host dependency: {role}"
                return None
            kwargs[kw] = obj
        for kw, (role, _attr) in spec.optional.items():
            obj = self._resolve(role)
            if obj is not None:
                kwargs[kw] = obj
            elif kw in spec.nullable:
                kwargs[kw] = None
        try:
            inst = getattr(g, spec.cls)(**kwargs)
        except Exception as e:  # construction failure must not stop the node
            self.skipped[spec.part] = f"constructor failed: {type(e).__name__}: {e}"
            self._record_error(spec.part, "build", e)
            return None
        self.parts[spec.part] = inst
        self.skipped.pop(spec.part, None)
        return inst

    def rebind_optional(self) -> Dict[str, List[str]]:
        """Late binding: fill optional dependencies (oracle, api, lending, ...) that were
        not available when the node was built.  Existing state is kept.  Parts that were
        skipped because a REQUIRED dependency was missing are built now if it appeared."""
        bound: Dict[str, List[str]] = {}
        for spec in SPECS:
            if not self._wanted(spec.part):
                continue
            inst = self.parts.get(spec.part)
            if inst is None:
                if self._build_part(spec) is not None:
                    bound.setdefault(spec.part, []).append("built")
                continue
            for kw, (role, attr) in spec.optional.items():
                if getattr(inst, attr, None) is None:
                    obj = self._resolve(role)
                    if obj is not None:
                        setattr(inst, attr, obj)
                        bound.setdefault(spec.part, []).append(role)
        return bound

    # ------------------------------------------------------------------
    # factories for classes that need their own arguments
    # ------------------------------------------------------------------
    def create_airdrop(self, key: str, token: str, merkle_root: str):
        """MerkleAirdrop needs a token and a merkle root, so it is created on demand."""
        bc = self._resolve("blockchain")
        if bc is None:
            raise RuntimeError("blockchain not available")
        with self._lock:
            if key in self.airdrops:
                raise KeyError(f"airdrop '{key}' already exists")
            obj = g.MerkleAirdrop(token, merkle_root, bc)
            self.airdrops[key] = obj
            return obj

    def create_hackathon(self, key: str, name: str, prize_pool: float,
                         start_block: int, end_block: int):
        """HackathonEvent needs event parameters, so it is created on demand."""
        bc = self._resolve("blockchain")
        if bc is None:
            raise RuntimeError("blockchain not available")
        with self._lock:
            if key in self.hackathons:
                raise KeyError(f"hackathon '{key}' already exists")
            obj = g.HackathonEvent(name, prize_pool, start_block, end_block, bc)
            self.hackathons[key] = obj
            return obj

    def new_passport(self, address: str):
        """DeFiPassport is a plain dataclass; the registry is the normal way to create it."""
        reg = self.parts.get("passport_registry")
        return reg.get_or_create(address) if reg else g.DeFiPassport(address=address, created_at=time.time())

    # ------------------------------------------------------------------
    # guard
    # ------------------------------------------------------------------
    def _record_error(self, part: str, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.part_errors[part] = self.part_errors.get(part, 0) + 1
        self.error_log.append({
            "ts": time.time(), "part": part, "where": where,
            "error": f"{type(exc).__name__}: {exc}",
        })
        log.warning("group45 %s/%s failed: %s", part, where, exc)

    def _guard(self, part: str, where: str, fn: Callable, *a, **k) -> Any:
        self.part_calls[part] = self.part_calls.get(part, 0) + 1
        try:
            return fn(*a, **k)
        except Exception as e:
            self._record_error(part, where, e)
            return None

    # ------------------------------------------------------------------
    # chain listener interface (called by NEBULABlockchain)
    # ------------------------------------------------------------------
    def on_connect(self, block: Any) -> None:
        if self.detached:
            return
        with self._lock:
            self.blocks_seen += 1
            self._guard("consensus_metrics", "connect", self._feed_consensus, block)
            self._guard("fee_history", "connect", self._feed_fees, block)
            self._guard("validator_rewards", "connect", self._feed_rewards, block)
            self._guard("archive", "connect", self._feed_archive, block)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        if self.detached:
            return
        with self._lock:
            self.reorgs_seen += 1
            self._guard("consensus_metrics", "reorg", self._reorg_consensus, old)
            self._guard("validator_rewards", "reorg", self._reorg_rewards, ancestor_height)
            self._guard("archive", "reorg", self._reorg_archive, old, ancestor_height)

    def detach(self) -> None:
        self.detached = True
        try:
            self.node.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer45.detach", exc_info=True)

    # ---- ConsensusMetrics ----
    def _feed_consensus(self, block: Any) -> None:
        part = self.parts.get("consensus_metrics")
        if part is None:
            return
        ts = block.header.timestamp
        if self._prev_ts is not None:
            part.record_block(block, self._prev_ts)
        self._prev_ts = ts

    @staticmethod
    def _depth(old: Any) -> int:
        try:
            return max(1, len(old))
        except TypeError:
            return 1

    def _reorg_consensus(self, old: Any) -> None:
        part = self.parts.get("consensus_metrics")
        if part is not None:
            part.record_reorg(self._depth(old))
        self._prev_ts = None   # intervals across a reorg boundary are meaningless

    # ---- FeeHistoryAnalyzer ----
    def _feed_fees(self, block: Any) -> None:
        part = self.parts.get("fee_history")
        if part is not None:
            part.record_block_fees(block, self.node.bc.utxo)

    # ---- ValidatorRewardTracker (report-only, reorg-safe via confirmations) ----
    def _proposer_of(self, block: Any) -> Optional[str]:
        if self.cfg.proposer_fn is not None:
            return self.cfg.proposer_fn(block)
        for holder in (block, getattr(block, "header", None)):
            if holder is None:
                continue
            for a in _PROPOSER_ATTRS:
                v = getattr(holder, a, None)
                if isinstance(v, str) and v:
                    return v
        txs = getattr(block, "transactions", None) or []
        if txs:
            cb = txs[0]
            outs = getattr(cb, "outputs", None) or getattr(cb, "vout", None) or []
            if outs:
                o = outs[0]
                for a in _OUTPUT_ADDR_ATTRS:
                    v = o.get(a) if isinstance(o, dict) else getattr(o, a, None)
                    if isinstance(v, str) and v:
                        return v
        return None

    def _feed_rewards(self, block: Any) -> None:
        part = self.parts.get("validator_rewards")
        if part is None:
            return
        self._pending_rewards.append(block)
        limit = block.height - self.cfg.confirmations
        while self._pending_rewards and self._pending_rewards[0].height <= limit:
            b = self._pending_rewards.popleft()
            if b.height <= self._last_rewarded_height:
                continue
            proposer = self._proposer_of(b)
            if proposer:
                part.record_block(b, proposer)
                self._last_rewarded_height = b.height

    def _reorg_rewards(self, ancestor_height: int) -> None:
        self._pending_rewards = deque(
            b for b in self._pending_rewards if b.height <= ancestor_height)

    # ---- ArchiveNode ----
    def _feed_archive(self, block: Any) -> None:
        part = self.parts.get("archive")
        if part is None:
            return
        for i, tx in enumerate(getattr(block, "transactions", []) or []):
            part.add_receipt(tx.txid, {"height": block.height,
                                       "block_hash": block.hash, "index": i})
        with part._lock:
            while len(part._tx_receipts) > self.cfg.receipt_cap:
                part._tx_receipts.pop(next(iter(part._tx_receipts)))
        if self.cfg.snapshot_interval > 0 and block.height % self.cfg.snapshot_interval == 0:
            part.snapshot_state(block.height)
            with part._lock:
                while len(part._state_snapshots) > self.cfg.snapshot_cap:
                    part._state_snapshots.pop(min(part._state_snapshots))

    def _reorg_archive(self, old: Any, ancestor_height: int) -> None:
        part = self.parts.get("archive")
        if part is None:
            return
        with part._lock:
            for h in [h for h in part._state_snapshots if h > ancestor_height]:
                del part._state_snapshots[h]
            try:
                for b in old:
                    for tx in getattr(b, "transactions", []) or []:
                        part._tx_receipts.pop(tx.txid, None)
            except TypeError:
                _NB_SWALLOW_LOG.warning("swallowed TypeError in Layer45._reorg_archive", exc_info=True)

    # ------------------------------------------------------------------
    # reporting
    # ------------------------------------------------------------------
    def get(self, part: str) -> Any:
        return self.parts.get(part)

    def status(self) -> dict:
        return {
            "built":        sorted(self.parts),
            "skipped":      dict(self.skipped),
            "errors":       self.errors,
            "part_errors":  dict(self.part_errors),
            "blocks_seen":  self.blocks_seen,
            "reorgs_seen":  self.reorgs_seen,
            "airdrops":     sorted(self.airdrops),
            "hackathons":   sorted(self.hackathons),
            "detached":     self.detached,
            "uptime_s":     round(time.time() - self.started_at, 1),
        }

    def report(self) -> dict:
        out: Dict[str, Any] = {}
        for part, method in STAT_METHODS.items():
            inst = self.parts.get(part)
            if inst is None:
                continue
            try:
                out[part] = {"ok": True, "data": getattr(inst, method)()}
            except Exception as e:
                out[part] = {"ok": False, "error": f"{type(e).__name__}: {e}"}
        for k, a in self.airdrops.items():
            out[f"airdrop:{k}"] = {"ok": True, "data": a.airdrop_stats()}
        for k, h in self.hackathons.items():
            out[f"hackathon:{k}"] = {"ok": True, "data": h.hackathon_info()}
        return out


# --------------------------------------------------------------------------
# install / uninstall
# --------------------------------------------------------------------------
def check_host(host: Any) -> List[str]:
    """Return a list of problems; an empty list means the host has the interface we need."""
    problems: List[str] = []
    if not hasattr(host, "NEBULAFullNode"):
        problems.append("host has no NEBULAFullNode")
    bc = getattr(host, "NEBULABlockchain", None)
    if bc is None:
        problems.append("host has no NEBULABlockchain")
    else:
        for m in ("add_listener", "_notify_connect", "_notify_reorg"):
            if not hasattr(bc, m):
                problems.append(f"NEBULABlockchain.{m} missing")
    return problems


def attach(node: Any, config: Optional[Group45Config] = None,
           deps: Optional[Dict[str, Any]] = None) -> Layer45:
    """Build the layer for one node and register it as a chain listener."""
    layer = Layer45(node, config, deps)
    node.bc.add_listener(layer)
    node.group45 = layer
    return layer


def install(host: Any, config: Optional[Group45Config] = None,
            deps: Optional[Dict[str, Any]] = None) -> bool:
    """Patch host.NEBULAFullNode.__init__.  Returns False if already installed."""
    problems = check_host(host)
    if problems:
        raise RuntimeError("group45 install refused: " + "; ".join(problems))
    cls = host.NEBULAFullNode
    if getattr(cls, "_g45_orig", None):
        return False
    orig = cls.__init__

    @functools.wraps(orig)
    def patched(self, *a, **k):
        orig(self, *a, **k)
        try:
            attach(self, config, deps)
        except Exception as e:      # the node must still start
            self.group45_error = e
            log.error("group45 attach failed: %s", e)

    cls._g45_orig = orig
    cls.__init__ = patched
    return True


def uninstall(host: Any) -> bool:
    """Restore the original __init__.  Layers of already running nodes: node.group45.detach()."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g45_orig", None)
    if not orig:
        return False
    cls.__init__ = orig
    del cls._g45_orig
    return True
