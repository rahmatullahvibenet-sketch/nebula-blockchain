"""nebula_group52_install.py - wiring layer for the 20 "dead" classes of nebula_group52.py.

Design rules (same philosophy as group 5):
  * Nothing in nebula_v10_11.py or nebula_group52.py is edited. Everything is attached from outside.
  * The layer NEVER rejects a block, a transaction or a P2P message. Every callback is wrapped in
    try/except; failures are counted in ``layer.errors`` / ``layer.error_log``.
  * Host wrappers (NEBULAFullNode.__init__, Mempool.submit, P2PNode._handle_message) call the ORIGINAL
    method first and return its result unchanged. The layer only observes afterwards.
  * Consensus-sensitive classes (BlockValidator, ValidatorCommittee, EpochRewardEngine, RewardBooster)
    are report-only. Mutating behaviour (rebase, incentives) is OFF unless enabled in Group52Config.
  * Every service is built in its own try/except. If one cannot be built (missing dependency in the
    host), it is listed in ``layer.failed`` and the node still starts.

Public API:
    install(host, **config)      patch NEBULAFullNode / Mempool / P2PNode for nodes created later
    uninstall(host)              restore everything (patched methods become pass-through)
    attach(node, host=None, **config)   wire an ALREADY created node
    Layer52                      the layer object, available as ``node.group52``
    Group52Config                all tunables
"""
from __future__ import annotations

import json
import logging
import os
import threading
import time
from collections import deque
from dataclasses import dataclass
from typing import Any, Callable, Deque, Dict, List, Optional, Tuple
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group52")

STATE_FILE_NAME = "group52_state.json"
STATE_VERSION = 1


# ----------------------------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------------------------
@dataclass
class Group52Config:
    """All tunables. Defaults are conservative (observe-only)."""
    data_dir: Optional[str] = None            # where group52_state.json is stored (None -> auto-detect, else RAM only)
    save_every_blocks: int = 50               # periodic atomic save
    health_every_blocks: int = 25             # NEBULAFullSystem.health_check cadence
    depth_every_blocks: int = 20              # LiquidityDepthAnalyzer snapshot cadence
    max_block_tx: int = 2000                  # denominator for block utilization fed to GasMarket
    max_events: int = 10_000                  # ChainIndexerV2 events cap
    max_addr_txs: int = 1_000                 # per-address tx list cap
    max_addresses: int = 100_000              # addresses tracked by ChainIndexerV2
    max_provenance_keys: int = 100_000        # NFTs tracked by NFTProvenanceTracker
    max_committees: int = 500                 # committees kept by ValidatorCommittee
    max_gas_history: int = 2_000              # GasMarket history cap
    price_pairs: Tuple[Tuple[str, str], ...] = (("NBL", "USDT"),)
    price_min_interval: float = 30.0          # seconds between PriceDiscovery.record_price sweeps
    reorg_alert_depth: int = 6                # reorgs at least this deep are flagged by the security monitor
    seen_heights_kept: int = 5_000            # idempotency / rollback window
    # --- behaviour switches (all OFF by default) ---
    auto_rebase_every: int = 0                # >0 -> NBUSD_V3.rebase() every N connected blocks
    auto_incentives: bool = False             # True -> "daily_active" reward for the coinbase recipient once per UTC day
    committee_every_block: bool = True        # report-only committee selection each block (needs a validator network)


# ----------------------------------------------------------------------------------------------
# Small helpers
# ----------------------------------------------------------------------------------------------
def _bhash(block: Any) -> Optional[str]:
    """Best-effort block hash (attribute or callable, on block or on block.header)."""
    for holder in (block, getattr(block, "header", None)):
        if holder is None:
            continue
        h = getattr(holder, "hash", None)
        if callable(h):
            try:
                h = h()
            except Exception:
                h = None
        if h:
            return str(h)
    return None


def _bheight(block: Any) -> Optional[int]:
    h = getattr(block, "height", None)
    if h is None:
        h = getattr(getattr(block, "header", None), "height", None)
    try:
        return int(h) if h is not None else None
    except (TypeError, ValueError):
        return None


def _txs(block: Any) -> List[Any]:
    t = getattr(block, "transactions", None)
    if t is None:
        t = getattr(block, "txs", None)
    try:
        return list(t or [])
    except TypeError:
        return []


def _data_dir_of(node: Any, cfg: Group52Config) -> Optional[str]:
    if cfg.data_dir:
        return cfg.data_dir
    env = os.environ.get("NEBULA_GROUP52_DIR")
    if env:
        return env
    holders = [node, getattr(node, "bc", None), getattr(node, "blockchain", None), getattr(node, "config", None)]
    for holder in holders:
        if holder is None:
            continue
        for name in ("data_dir", "datadir", "data_path"):
            v = getattr(holder, name, None)
            if isinstance(v, (str, os.PathLike)) and str(v):
                return str(v)
    return None


def _atomic_write_json(path: str, payload: dict) -> None:
    """Crash-safe write: tmp file + flush + fsync + rename (+ best-effort directory fsync)."""
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    tmp = f"{path}.tmp.{os.getpid()}.{threading.get_ident()}"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, separators=(",", ":"), default=str)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)
    try:
        fd = os.open(directory, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
    except OSError:
        _NB_SWALLOW_LOG.debug("swallowed OSError in _atomic_write_json", exc_info=True)  # directory fsync is not supported everywhere (e.g. Windows)


def _discover(node: Any, cls: Optional[type], skip_layer: Any = None) -> Any:
    """Find an already existing instance of ``cls`` on the node or on any other ``group*`` layer.

    This lets the layer SHARE state with other groups instead of silently creating a second copy.
    """
    if cls is None or not isinstance(cls, type):
        return None
    try:
        attrs = dict(vars(node))
    except TypeError:
        return None
    for name, value in attrs.items():
        if value is skip_layer:
            continue
        if isinstance(value, cls):
            return value
    for name, layer in attrs.items():
        if layer is skip_layer or not str(name).startswith("group"):
            continue
        try:
            inner = dict(vars(layer))
        except TypeError:
            continue
        candidates = list(inner.values())
        services = inner.get("services")
        if isinstance(services, dict):
            candidates.extend(services.values())
        for value in candidates:
            if isinstance(value, cls):
                return value
    return None


# ----------------------------------------------------------------------------------------------
# Security monitor (backs SecurityAuditV2 / "security & monitoring" integration point)
# ----------------------------------------------------------------------------------------------
class SecurityMonitor:
    """Passive monitor. Collects facts; never blocks anything."""

    def __init__(self, audit: Any, reorg_alert_depth: int = 6):
        self._audit = audit
        self._alert_depth = reorg_alert_depth
        self._lock = threading.RLock()
        self.reorgs: Deque[dict] = deque(maxlen=200)
        self.alerts: Deque[dict] = deque(maxlen=500)
        self.validator_disagreements: Deque[dict] = deque(maxlen=200)
        self.p2p_messages: Dict[str, int] = {}
        self.mempool = {"seen": 0, "accepted": 0, "rejected": 0, "below_base_fee": 0}
        self._audit_cache: Optional[dict] = None

    def alert(self, kind: str, **data: Any) -> None:
        with self._lock:
            self.alerts.append({"kind": kind, "ts": time.time(), **data})

    def record_reorg(self, depth: int, ancestor_height: Any) -> None:
        with self._lock:
            self.reorgs.append({"depth": depth, "ancestor": ancestor_height, "ts": time.time()})
        if depth >= self._alert_depth:
            self.alert("deep_reorg", depth=depth, ancestor=ancestor_height)

    def record_disagreement(self, height: Any, message: str) -> None:
        with self._lock:
            self.validator_disagreements.append({"height": height, "message": message, "ts": time.time()})
        self.alert("validator_disagreement", height=height, message=message)

    def full_audit(self, refresh: bool = False) -> Optional[dict]:
        """Run SecurityAuditV2.nebula_full_audit() lazily and cache it (it is a static report)."""
        if self._audit is None:
            return None
        with self._lock:
            if self._audit_cache is None or refresh:
                self._audit_cache = self._audit.nebula_full_audit()
            return self._audit_cache

    def summary(self) -> dict:
        with self._lock:
            return {
                "reorgs_seen": len(self.reorgs),
                "deepest_reorg": max((r["depth"] for r in self.reorgs), default=0),
                "alerts": len(self.alerts),
                "validator_disagreements": len(self.validator_disagreements),
                "p2p_messages": dict(self.p2p_messages),
                "mempool": dict(self.mempool),
                "audit_cached": self._audit_cache is not None,
            }


# ----------------------------------------------------------------------------------------------
# The layer
# ----------------------------------------------------------------------------------------------
class Layer52:
    """Owns the 20 group52 objects and feeds them with real chain / mempool / P2P data."""

    # ---- construction -------------------------------------------------------------------
    def __init__(self, node: Any, g: Any, host: Any = None, config: Optional[Group52Config] = None):
        self.node = node
        self.g = g                      # the nebula_group52 module
        self.host = host                # the nebula_v10_11 module (may be None)
        self.cfg = config or Group52Config()
        self.errors = 0
        self.error_log: Deque[dict] = deque(maxlen=50)
        self.failed: Dict[str, str] = {}        # service -> reason it could not be built
        self.borrowed: Dict[str, bool] = {}     # service -> True if an existing shared instance was reused
        self.services: Dict[str, Any] = {}
        self.attached = False
        self.blocks_processed = 0
        self.last_health: Optional[dict] = None
        self.last_depth: Optional[dict] = None
        self.last_committee: Optional[dict] = None
        self.last_state_save: Optional[float] = None
        self.state_path: Optional[str] = None

        self._lock = threading.RLock()
        self._seen: Dict[int, str] = {}                 # height -> block hash (idempotency + rollback window)
        self._undo_index: Dict[int, List[Tuple[str, str]]] = {}   # height -> [(address, txid)] added to the indexer
        self._incentive_days: set = set()
        self._last_price_sweep = 0.0
        self._rebase_counter = 0
        self._dirty = False

        self._ensure_compat_names()
        self._build_services()
        self._load_state()

    # ---- error handling ------------------------------------------------------------------
    def _err(self, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.error_log.append({"where": where, "error": f"{type(exc).__name__}: {exc}", "ts": time.time()})
        log.warning("group52 %s failed: %s", where, exc)

    def _guard(self, where: str, fn: Callable[[], Any]) -> Any:
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 - a layer must never break the host
            self._err(where, exc)
            return None

    # ---- host lookups ----------------------------------------------------------------------
    def _cls(self, name: str) -> Optional[type]:
        for mod in (self.host, self.g):
            c = getattr(mod, name, None)
            if isinstance(c, type):
                return c
        return None

    def _ensure_compat_names(self) -> None:
        """nebula_group52.NFTGamingV2 references the name ``GameItemC`` which lives in the host.

        If the host does not export it, build it the same way the host does (``_make_compat``).
        This only adds a missing module-level name; no class source is changed.
        """
        try:
            if not hasattr(self.g, "GameItemC"):
                base = self._cls("GameItem")
                maker = getattr(self.g, "_make_compat", None)
                if base is not None and maker is not None:
                    self.g.GameItemC = maker(base, name="GameItemC")
        except Exception as exc:  # noqa: BLE001
            self._err("ensure_compat_names", exc)

    @property
    def bc(self) -> Any:
        return getattr(self.node, "bc", None) or getattr(self.node, "blockchain", None)

    # ---- service construction -----------------------------------------------------------------
    def _build(self, key: str, factory: Callable[[], Any]) -> Any:
        try:
            obj = factory()
            if obj is None:
                raise RuntimeError("factory returned None")
            self.services[key] = obj
            setattr(self, key, obj)
            return obj
        except Exception as exc:  # noqa: BLE001
            self.failed[key] = f"{type(exc).__name__}: {exc}"
            setattr(self, key, None)
            log.warning("group52 service %s not built: %s", key, exc)
            return None

    def _borrow_or_make(self, key: str, class_name: str, make: Callable[[type], Any]) -> Any:
        """Reuse an instance another group already created; otherwise construct one."""
        cls = self._cls(class_name)
        if cls is None:
            self.failed[key] = f"host class {class_name} not available"
            setattr(self, key, None)
            return None
        found = _discover(self.node, cls, skip_layer=self)
        if found is not None:
            self.borrowed[key] = True
            self.services[key] = found
            setattr(self, key, found)
            return found
        self.borrowed[key] = False
        return self._build(key, lambda: make(cls))

    def _build_services(self) -> None:
        g, bc = self.g, self.bc
        if bc is None:
            self.failed["blockchain"] = "node has no .bc / .blockchain"
            return

        # -- shared host-side dependencies (borrowed from other groups when they exist) --------
        oracle = self._borrow_or_make("oracle", "OracleV2", lambda c: c(bc))
        nft_registry = self._borrow_or_make("nft_registry", "NBL721Registry", lambda c: c())
        epoch_system = self._borrow_or_make("epoch_system", "EpochSystem", lambda c: self._try_ctor(c, (bc,), ()))
        validator_network = self._borrow_or_make(
            "validator_network", "ValidatorNetwork", lambda c: self._try_ctor(c, (bc,), ()))
        lending = _discover(self.node, self._cls("LendingProtocolV2"), skip_layer=self)
        rng = self._borrow_or_make("rng", "OnChainRNG", lambda c: self._try_ctor(c, (bc,), ()))

        # -- the 20 group52 classes ------------------------------------------------------------
        self._build("zk_vm", lambda: g.ZKVirtualMachine())
        self._build("gaming", lambda: self._need(rng, "OnChainRNG") and g.NFTGamingV2(bc, rng))
        self._build("staking_v4", lambda: g.StakingProtocolV4(bc))
        self._build("dex_v3", lambda: self._make_dex_v3(bc, oracle))
        self._build("price_discovery", lambda: g.PriceDiscovery(self._amm(), self._need(oracle, "OracleV2")))
        self._build("incentives", lambda: g.IncentiveSystem(bc))
        self._build("block_validator", lambda: g.BlockValidator(bc))
        self._build("cold_storage", lambda: g.ColdStorageManager(bc))
        self._build("epoch_rewards", lambda: g.EpochRewardEngine(bc, self._need(epoch_system, "EpochSystem")))
        self._build("defi_router", lambda: g.DeFiRouterV2(bc, self.services.get("staking_v4"),
                                                          self.services.get("dex_v3"), lending))
        self._build("nbusd", lambda: g.NBUSD_V3(bc, oracle))
        self._build("xc_nft", lambda: g.CrossChainNFTV2(self._need(nft_registry, "NBL721Registry"), bc))
        self._build("committee", lambda: g.ValidatorCommittee(self._need(validator_network, "ValidatorNetwork"), bc))
        self._build("gas_market", lambda: g.GasMarket(bc))
        self._build("indexer", lambda: g.ChainIndexerV2(bc))
        self._build("reward_booster", lambda: g.RewardBooster(bc))
        self._build("depth_analyzer", lambda: g.LiquidityDepthAnalyzer(self._amm()))
        self._build("audit", lambda: g.SecurityAuditV2())
        self._build("provenance", lambda: g.NFTProvenanceTracker(bc))
        self._build("full_system", self._make_full_system)

        self.security = SecurityMonitor(self.services.get("audit"), self.cfg.reorg_alert_depth)
        self.services["security"] = self.security

    @staticmethod
    def _need(value: Any, what: str) -> Any:
        if value is None:
            raise RuntimeError(f"dependency {what} is not available")
        return value

    @staticmethod
    def _try_ctor(cls: type, *arg_sets: tuple) -> Any:
        last: Optional[BaseException] = None
        for args in arg_sets:
            try:
                return cls(*args)
            except TypeError as exc:
                last = exc
        raise RuntimeError(f"cannot construct {cls.__name__}: {last}")

    def _amm(self) -> Any:
        dex = self.services.get("dex_v3")
        if dex is None:
            raise RuntimeError("DEXv3 is not available")
        return dex._amm

    def _make_dex_v3(self, bc: Any, oracle: Any) -> Any:
        dex = self.g.DEXv3(bc, oracle)
        shared = _discover(self.node, self._cls("NEBULADex"), skip_layer=self)
        if shared is not None and shared is not dex._amm:
            dex._amm = shared           # share the pools other groups already use
            self.borrowed["amm"] = True
        return dex

    def _make_full_system(self) -> Any:
        """NEBULAFullSystem() would create a SECOND NEBULABlockchain. Build it on THIS node's chain instead
        and fill its module table with the instances that really exist (no duplicates, no new threads)."""
        cls = self.g.NEBULAFullSystem
        fs = cls.__new__(cls)
        fs.network = getattr(self.bc, "network", None) or getattr(self.node, "network", None) or "mainnet"
        fs.blockchain = self.bc
        fs._status = "running"
        fs._start_time = time.time()
        modules: Dict[str, Any] = {}
        mine = {"oracle": "oracle", "staking": "staking_v4", "dex": "dex_v3", "nft": "nft_registry"}
        for name, key in mine.items():
            if self.services.get(key) is not None:
                modules[name] = self.services[key]
        others = {
            "governance": "GovernanceV3", "lending": "LendingProtocolV2", "bridge": "BridgeEngine",
            "nns": "NEBULANameService", "treasury": "TreasuryV3", "dao": "DAOv2", "zk_rollup": "ZKRollupLayer",
            "analytics": "AdvancedAnalyticsV3", "security_council": "SecurityCouncil",
            "ecosystem": "EcosystemHub", "identity": "DIDRegistryV2", "interop": "InteroperabilityLayer",
            "synthetics": "SyntheticAssetProtocol", "perp_protocol": "PerpetualProtocol",
            "options_v2": "OptionsProtocolV2", "community": "CommunityHub",
        }
        for name, cname in others.items():
            found = _discover(self.node, self._cls(cname), skip_layer=self)
            if found is not None:
                modules[name] = found
        fs._modules = modules
        return fs

    # ---- chain listener ---------------------------------------------------------------------------
    def on_connect(self, block: Any) -> None:
        try:
            with self._lock:
                self._process_block(block)
        except Exception as exc:  # noqa: BLE001
            self._err("on_connect", exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        try:
            with self._lock:
                old_blocks = [b for b in (old or []) if _bheight(b) is not None]
                new_blocks = [b for b in (new or []) if _bheight(b) is not None]
                depth = len(list(old or []))
                self.security.record_reorg(depth, ancestor_height)
                old_hashes = {h for h in (_bhash(b) for b in old_blocks) if h}
                self._rollback_above(ancestor_height, old_hashes)
                for blk in new_blocks:                   # idempotent: skipped if already processed
                    self._process_block(blk)
        except Exception as exc:  # noqa: BLE001
            self._err("on_reorg", exc)

    def _process_block(self, block: Any) -> None:
        height = _bheight(block)
        if height is None:
            return
        bh = _bhash(block) or f"h{height}"
        prev_seen = self._seen.get(height)
        if prev_seen == bh:
            return                                       # already processed (host may notify twice)
        if prev_seen is not None and prev_seen != bh:
            self._rollback_heights([height])             # a different block replaced this height
        self._seen[height] = bh
        self.blocks_processed += 1
        self._dirty = True

        txs = _txs(block)
        self._guard("indexer", lambda: self._index_block(height, txs))
        self._guard("gas_market", lambda: self._update_gas(len(txs)))
        self._guard("price_discovery", self._maybe_record_price)
        self._guard("committee", lambda: self._report_committee(height))
        self._guard("block_validator", lambda: self._report_validation(block, height))
        self._guard("incentives", lambda: self._auto_incentive(block, txs))
        self._guard("nbusd", self._auto_rebase)
        self._guard("health", self._maybe_health)
        self._guard("depth", self._maybe_depth)
        self._guard("trim", self._trim_caps)
        if self.cfg.save_every_blocks and self.blocks_processed % self.cfg.save_every_blocks == 0:
            self._guard("save_state", self.save_state)

    # -- per-service chain steps --
    def _index_block(self, height: int, txs: List[Any]) -> None:
        idx = self.services.get("indexer")
        if idx is None:
            return
        added: List[Tuple[str, str]] = []
        for tx in txs:
            txid = getattr(tx, "txid", None)
            if txid is None:
                continue
            for out in getattr(tx, "outputs", None) or []:
                addr = getattr(out, "address", None)
                if addr and txid not in idx._tx_by_addr.get(addr, ()):
                    added.append((addr, txid))
            idx.index_transaction(tx, height)
        self._undo_index[height] = added

    def _update_gas(self, tx_count: int) -> None:
        gm = self.services.get("gas_market")
        if gm is None:
            return
        utilization = min(1.0, tx_count / float(max(1, self.cfg.max_block_tx)))
        gm.update_base_fee(utilization)

    def _maybe_record_price(self, force: bool = False) -> None:
        pdisc = self.services.get("price_discovery")
        if pdisc is None:
            return
        now = time.time()
        if not force and now - self._last_price_sweep < self.cfg.price_min_interval:
            return
        self._last_price_sweep = now
        for base, quote in self.cfg.price_pairs:
            self._guard(f"record_price {base}/{quote}", lambda b=base, q=quote: pdisc.record_price(b, q))

    def _report_committee(self, height: int) -> None:
        com = self.services.get("committee")
        if com is None or not self.cfg.committee_every_block:
            return
        members = com.select_committee(height)
        self.last_committee = {"height": height, "size": len(members)}
        if len(com._committees) > self.cfg.max_committees:
            for h in sorted(com._committees)[: len(com._committees) - self.cfg.max_committees]:
                com._committees.pop(h, None)

    def _prev_block(self, block: Any, height: int) -> Any:
        bc = self.bc
        prev_hash = getattr(getattr(block, "header", None), "prev_hash", None)
        for name, arg in (("get_block_by_hash", prev_hash), ("get_block", height - 1), ("block_at", height - 1)):
            fn = getattr(bc, name, None)
            if callable(fn) and arg is not None:
                try:
                    res = fn(arg)
                except Exception:  # noqa: BLE001
                    continue
                if res is not None:
                    return res
        chain = getattr(bc, "chain", None) or getattr(bc, "blocks", None)
        try:
            if chain is not None and 0 <= height - 1 < len(chain):
                return chain[height - 1]
        except Exception:  # noqa: BLE001
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer52._prev_block", exc_info=True)
        return None

    def _report_validation(self, block: Any, height: int) -> None:
        """REPORT-ONLY header check. The block is already accepted by the host; a disagreement is logged.

        Full validate_block()/validate_transaction() are intentionally NOT run here: they recompute fees from
        the UTXO set, but after a block is connected its inputs are already spent, so they would report
        false errors.
        """
        val = self.services.get("block_validator")
        if val is None or height <= 0:
            return
        prev = self._prev_block(block, height)
        if prev is None:
            return
        ok, msg = val.validate_block_header(block.header, prev)
        if not ok:
            self.security.record_disagreement(height, msg)

    def _auto_incentive(self, block: Any, txs: List[Any]) -> None:
        inc = self.services.get("incentives")
        if inc is None or not self.cfg.auto_incentives or not txs:
            return
        outs = getattr(txs[0], "outputs", None) or []
        addr = getattr(outs[0], "address", None) if outs else None
        if not addr:
            return
        day = int(time.time() // 86400)
        key = (addr, day)
        if key in self._incentive_days:
            return
        self._incentive_days.add(key)
        if len(self._incentive_days) > 50_000:
            self._incentive_days = {k for k in self._incentive_days if k[1] == day}
        inc.earn_reward(addr, "daily_active")

    def _auto_rebase(self) -> None:
        coin = self.services.get("nbusd")
        every = self.cfg.auto_rebase_every
        if coin is None or every <= 0:
            return
        self._rebase_counter += 1
        if self._rebase_counter % every == 0:
            coin.rebase()

    def _maybe_health(self) -> None:
        fs = self.services.get("full_system")
        every = self.cfg.health_every_blocks
        if fs is not None and every and self.blocks_processed % every == 0:
            self.last_health = fs.health_check()

    def _maybe_depth(self) -> None:
        da = self.services.get("depth_analyzer")
        every = self.cfg.depth_every_blocks
        if da is not None and every and self.blocks_processed % every == 0:
            self.last_depth = {"ts": time.time(), "top_pools": da.most_liquid_pools(3)}

    # -- rollback / caps --
    def _rollback_above(self, ancestor_height: Any, old_hashes: set) -> None:
        try:
            anc = int(ancestor_height)
        except (TypeError, ValueError):
            anc = -1
        heights = []
        for h, bh in list(self._seen.items()):
            if h <= anc:
                continue
            if old_hashes and bh not in old_hashes:
                continue                                  # this height already holds a NEW block: keep it
            heights.append(h)
        self._rollback_heights(heights)

    def _rollback_heights(self, heights: List[int]) -> None:
        if not heights:
            return
        idx = self.services.get("indexer")
        for h in heights:
            for addr, txid in self._undo_index.pop(h, []):
                if idx is not None:
                    lst = idx._tx_by_addr.get(addr)
                    if lst and txid in lst:
                        lst.remove(txid)
                        if not lst:
                            idx._tx_by_addr.pop(addr, None)
            self._seen.pop(h, None)
        gm = self.services.get("gas_market")
        if gm is not None and heights:
            lowest = min(heights)
            with gm._lock:
                while gm._history and gm._history[-1].get("height", -1) >= lowest:
                    gm._history.pop()
                gm._base_fee = gm._history[-1]["base_fee"] if gm._history else gm.MIN_BASE_FEE
        self._dirty = True

    def _trim_caps(self) -> None:
        cfg = self.cfg
        idx = self.services.get("indexer")
        if idx is not None:
            with idx._lock:
                if len(idx._events) > cfg.max_events:
                    del idx._events[: len(idx._events) - cfg.max_events]
                while len(idx._tx_by_addr) > cfg.max_addresses:
                    idx._tx_by_addr.pop(next(iter(idx._tx_by_addr)))
                for addr, lst in idx._tx_by_addr.items():
                    if len(lst) > cfg.max_addr_txs:
                        del lst[: len(lst) - cfg.max_addr_txs]
        gm = self.services.get("gas_market")
        if gm is not None:
            with gm._lock:
                if len(gm._history) > cfg.max_gas_history:
                    del gm._history[: len(gm._history) - cfg.max_gas_history]
        pv = self.services.get("provenance")
        if pv is not None:
            with pv._lock:
                while len(pv._history) > cfg.max_provenance_keys:
                    pv._history.pop(next(iter(pv._history)))
        if len(self._seen) > cfg.seen_heights_kept:
            for h in sorted(self._seen)[: len(self._seen) - cfg.seen_heights_kept]:
                self._seen.pop(h, None)
                self._undo_index.pop(h, None)

    # ---- mempool / P2P observers (called by the host wrappers, AFTER the original method ran) ----------
    def on_mempool_submit(self, tx: Any, result: Any) -> None:
        try:
            m = self.security.mempool
            m["seen"] += 1
            accepted = bool(result[0]) if isinstance(result, tuple) and result else bool(result)
            m["accepted" if accepted else "rejected"] += 1
            gm = self.services.get("gas_market")
            bc = self.bc
            if gm is not None and accepted and bc is not None:
                fee_fn = getattr(tx, "fee", None)
                size_fn = getattr(tx, "byte_size", None)
                if callable(fee_fn) and callable(size_fn):
                    try:
                        fee = fee_fn(bc.utxo)
                        size = max(1, int(size_fn()))
                    except Exception:  # noqa: BLE001 - fee needs the UTXO set; just skip when unavailable
                        return
                    if fee * 1000 // size < gm._base_fee:
                        m["below_base_fee"] += 1
        except Exception as exc:  # noqa: BLE001
            self._err("on_mempool_submit", exc)

    def on_p2p_message(self, peer: Any, msg: Any) -> None:
        try:
            kind = "unknown"
            if isinstance(msg, dict):
                kind = str(msg.get("type") or msg.get("cmd") or msg.get("command") or "unknown")
            else:
                kind = str(getattr(msg, "type", None) or getattr(msg, "cmd", None) or type(msg).__name__)
            counts = self.security.p2p_messages
            if kind in counts or len(counts) < 64:        # bounded label set
                counts[kind] = counts.get(kind, 0) + 1
            self._maybe_record_price()
        except Exception as exc:  # noqa: BLE001
            self._err("on_p2p_message", exc)

    # ---- manual (explicit) actions: never run automatically -----------------------------------------------
    def run_epoch_rewards(self) -> Optional[dict]:
        """EpochRewardEngine mutates the EpochSystem (record_reward). Call it yourself when you are ready."""
        eng = self.services.get("epoch_rewards")
        if eng is None:
            raise RuntimeError("EpochRewardEngine is not available: " + self.failed.get("epoch_rewards", "?"))
        return eng.distribute_epoch_rewards()

    def run_rebase(self) -> Optional[dict]:
        coin = self.services.get("nbusd")
        if coin is None:
            raise RuntimeError("NBUSD_V3 is not available")
        return coin.rebase()

    # ---- persistence ----------------------------------------------------------------------------------------------
    def _state_path(self) -> Optional[str]:
        if self.state_path:
            return self.state_path
        d = _data_dir_of(self.node, self.cfg)
        if d:
            self.state_path = os.path.join(d, STATE_FILE_NAME)
        return self.state_path

    def snapshot_state(self) -> dict:
        s = self.services
        out: Dict[str, Any] = {"version": STATE_VERSION, "saved_at": time.time(), "blocks_processed": self.blocks_processed}
        if s.get("indexer"):
            i = s["indexer"]
            with i._lock:
                out["indexer"] = {"tx_by_addr": {a: list(v) for a, v in i._tx_by_addr.items()},
                                  "events": list(i._events)}
        if s.get("gas_market"):
            gm = s["gas_market"]
            with gm._lock:
                out["gas_market"] = {"base_fee": gm._base_fee, "history": list(gm._history)}
        if s.get("incentives"):
            inc = s["incentives"]
            with inc._lock:
                out["incentives"] = {"earned": dict(inc._earned),
                                     "claimed": {a: sorted(v) for a, v in inc._claimed.items()}}
        if s.get("provenance"):
            pv = s["provenance"]
            with pv._lock:
                out["provenance"] = {k: list(v) for k, v in pv._history.items()}
        if s.get("price_discovery"):
            out["price_history"] = {k: [list(p) for p in v] for k, v in s["price_discovery"]._history.items()}
        if s.get("reward_booster"):
            out["boosts"] = dict(s["reward_booster"]._boosts)
        if s.get("epoch_rewards"):
            out["epoch_distributed"] = list(s["epoch_rewards"]._distributed)
        if s.get("nbusd"):
            n = s["nbusd"]
            with n._lock:
                out["nbusd"] = {"supply": n._supply, "balances": dict(n._balances), "factor": n._rebase_factor}
        if s.get("xc_nft"):
            x = s["xc_nft"]
            with x._lock:
                out["xc_nft"] = {"locked": {c: sorted(t) for c, t in x._locked_nfts.items()},
                                 "bridges": dict(x._bridges)}
        return out

    def save_state(self) -> bool:
        path = self._state_path()
        if not path:
            return False
        with self._lock:
            payload = self.snapshot_state()
        _atomic_write_json(path, payload)
        self.last_state_save = time.time()
        self._dirty = False
        return True

    def _load_state(self) -> None:
        path = self._state_path()
        if not path or not os.path.isfile(path):
            return
        try:
            with open(path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            if not isinstance(data, dict) or data.get("version") != STATE_VERSION:
                raise ValueError("unsupported state file version")
            self._apply_state(data)
        except Exception as exc:  # noqa: BLE001
            self._err("load_state", exc)
            try:
                os.replace(path, f"{path}.corrupt.{int(time.time())}")   # keep it for inspection, start clean
            except OSError:
                _NB_SWALLOW_LOG.warning("swallowed OSError in Layer52._load_state", exc_info=True)

    def _apply_state(self, d: dict) -> None:
        s = self.services
        if s.get("indexer") and "indexer" in d:
            i = s["indexer"]
            with i._lock:
                i._tx_by_addr = {a: list(v) for a, v in d["indexer"].get("tx_by_addr", {}).items()}
                i._events = list(d["indexer"].get("events", []))
        if s.get("gas_market") and "gas_market" in d:
            gm = s["gas_market"]
            with gm._lock:
                gm._base_fee = int(d["gas_market"].get("base_fee", gm._base_fee))
                gm._history = list(d["gas_market"].get("history", []))
        if s.get("incentives") and "incentives" in d:
            inc = s["incentives"]
            with inc._lock:
                inc._earned = {a: int(v) for a, v in d["incentives"].get("earned", {}).items()}
                inc._claimed = {a: set(v) for a, v in d["incentives"].get("claimed", {}).items()}
        if s.get("provenance") and "provenance" in d:
            pv = s["provenance"]
            with pv._lock:
                pv._history = {k: list(v) for k, v in d["provenance"].items()}
        if s.get("price_discovery") and "price_history" in d:
            s["price_discovery"]._history = {k: [(float(p[0]), float(p[1])) for p in v]
                                             for k, v in d["price_history"].items()}
        if s.get("reward_booster") and "boosts" in d:
            s["reward_booster"]._boosts = {a: float(v) for a, v in d["boosts"].items()}
        if s.get("epoch_rewards") and "epoch_distributed" in d:
            s["epoch_rewards"]._distributed = list(d["epoch_distributed"])
        if s.get("nbusd") and "nbusd" in d:
            n = s["nbusd"]
            with n._lock:
                n._supply = int(d["nbusd"].get("supply", 0))
                n._balances = {a: int(v) for a, v in d["nbusd"].get("balances", {}).items()}
                n._rebase_factor = float(d["nbusd"].get("factor", 1.0))
        if s.get("xc_nft") and "xc_nft" in d:
            x = s["xc_nft"]
            with x._lock:
                x._locked_nfts = {c: set(int(t) for t in toks) for c, toks in d["xc_nft"].get("locked", {}).items()}
                x._bridges = {p: int(v) for p, v in d["xc_nft"].get("bridges", {}).items()}

    # ---- reporting ------------------------------------------------------------------------------------------------------
    _STAT_METHODS = {
        "zk_vm": "zk_vm_stats", "gaming": "gaming_v2_stats", "staking_v4": "staking_v4_stats",
        "dex_v3": "dex_v3_stats", "full_system": "status", "price_discovery": "discovery_stats",
        "incentives": "incentive_stats", "block_validator": "validator_stats",
        "epoch_rewards": "epoch_reward_stats", "defi_router": "router_v2_stats", "nbusd": "nbusd_v3_stats",
        "xc_nft": "xcnft_v2_stats", "gas_market": "gas_market_stats", "indexer": "indexer_v2_stats",
        "provenance": "provenance_stats",
    }

    def stats(self) -> dict:
        """One call that shows the health of the whole layer. Secrets (mnemonics etc.) are never included."""
        out: Dict[str, Any] = {
            "errors": self.errors,
            "blocks_processed": self.blocks_processed,
            "services_built": sorted(self.services),
            "services_failed": dict(self.failed),
            "borrowed_shared": sorted(k for k, v in self.borrowed.items() if v),
            "state_file": self._state_path(),
            "last_state_save": self.last_state_save,
            "last_health": self.last_health,
            "last_committee": self.last_committee,
            "security": self.security.summary() if getattr(self, "security", None) else None,
        }
        per: Dict[str, Any] = {}
        for key, method in self._STAT_METHODS.items():
            obj = self.services.get(key)
            if obj is not None:
                per[key] = self._guard(f"stats.{key}", getattr(obj, method))
        out["services"] = per
        return out

    # ---- lifecycle ----------------------------------------------------------------------------------------------------------
    def detach(self) -> None:
        """Remove the listener and flush state. Never raises."""
        bc = self.bc
        try:
            remover = getattr(bc, "remove_listener", None)
            if callable(remover):
                remover(self)
            else:
                bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer52.detach", exc_info=True)
        except Exception as exc:  # noqa: BLE001
            self._err("detach", exc)
        if self._dirty:
            self._guard("save_state", self.save_state)
        self.attached = False
        _unregister(self)


# ----------------------------------------------------------------------------------------------
# Host patching (NEBULAFullNode.__init__, Mempool.submit, P2PNode._handle_message)
# ----------------------------------------------------------------------------------------------
_LAYERS: List[Layer52] = []
_LAYERS_LOCK = threading.RLock()
_ENABLED = {"on": False}


def _register(layer: Layer52) -> None:
    with _LAYERS_LOCK:
        if layer not in _LAYERS:
            _LAYERS.append(layer)


def _unregister(layer: Layer52) -> None:
    with _LAYERS_LOCK:
        if layer in _LAYERS:
            _LAYERS.remove(layer)


def _layers_owning(obj: Any, kind: str) -> List[Layer52]:
    with _LAYERS_LOCK:
        layers = list(_LAYERS)
    owners = []
    for layer in layers:
        try:
            node = layer.node
            if kind == "mempool":
                if getattr(layer.bc, "mempool", None) is obj:
                    owners.append(layer)
            elif any(v is obj for v in vars(node).values()):
                owners.append(layer)
        except Exception:  # noqa: BLE001
            continue
    return owners


def _import_group52() -> Any:
    import nebula_group52 as g  # imported lazily so this file can be read without the host present
    return g


def attach(node: Any, host: Any = None, **config: Any) -> Layer52:
    """Wire an already created node. Returns the layer (also stored as ``node.group52``)."""
    g = _import_group52()
    if host is None:
        host = getattr(g, "_host", None)
    cfg = Group52Config(**config)
    layer = Layer52(node, g, host, cfg)
    bc = layer.bc
    if bc is None:
        raise RuntimeError("node has no blockchain (.bc / .blockchain)")
    bc.add_listener(layer)
    layer.attached = True
    node.group52 = layer
    _register(layer)
    return layer


def install(host: Any, **config: Any) -> bool:
    """Patch the host so every NEBULAFullNode created afterwards gets ``node.group52``."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g52_orig", None):
        return False                                        # already installed
    orig_init = cls.__init__

    def patched_init(self, *a, **k):                      # noqa: ANN001
        orig_init(self, *a, **k)                            # the original always runs first
        if not _ENABLED["on"]:
            return
        try:
            attach(self, host, **config)
        except Exception as exc:  # noqa: BLE001 - the node must still start
            self.group52_error = exc
            log.warning("group52 attach failed: %s", exc)

    cls._g52_orig = orig_init
    cls._g52_wrapper = patched_init
    cls.__init__ = patched_init

    _patch_method(getattr(host, "Mempool", None), "submit", "mempool")
    _patch_method(getattr(host, "P2PNode", None), "_handle_message", "p2p")
    _ENABLED["on"] = True
    return True


def _patch_method(cls: Any, name: str, kind: str) -> None:
    if cls is None or not hasattr(cls, name):
        return
    marker = f"_g52_orig_{name}"
    if cls.__dict__.get(marker):
        return
    orig = getattr(cls, name)

    if kind == "mempool":
        def wrapper(self, tx, *a, **k):                    # noqa: ANN001
            result = orig(self, tx, *a, **k)                # original first, result returned untouched
            if _ENABLED["on"]:
                for layer in _layers_owning(self, "mempool"):
                    layer.on_mempool_submit(tx, result)
            return result
    else:
        def wrapper(self, peer, msg, *a, **k):             # noqa: ANN001
            result = orig(self, peer, msg, *a, **k)
            if _ENABLED["on"]:
                for layer in _layers_owning(self, "p2p"):
                    layer.on_p2p_message(peer, msg)
            return result

    wrapper.__wrapped__ = orig
    wrapper.__name__ = getattr(orig, "__name__", name)
    wrapper.__doc__ = getattr(orig, "__doc__", None)
    setattr(cls, marker, orig)
    setattr(cls, f"_g52_wrapper_{name}", wrapper)
    setattr(cls, name, wrapper)


def _restore_method(cls: Any, name: str) -> None:
    if cls is None:
        return
    marker = f"_g52_orig_{name}"
    orig = cls.__dict__.get(marker)
    if not orig:
        return
    if cls.__dict__.get(name) is cls.__dict__.get(f"_g52_wrapper_{name}"):
        setattr(cls, name, orig)                            # nobody wrapped on top of us: fully restore
    # else: another layer wrapped after us. Leave the chain intact; our wrapper is a pass-through once disabled.
    for attr in (marker, f"_g52_wrapper_{name}"):
        try:
            delattr(cls, attr)
        except AttributeError:
            _NB_SWALLOW_LOG.warning("swallowed AttributeError in _restore_method", exc_info=True)


def uninstall(host: Any) -> None:
    """Disable the layer, detach it from every node and restore the host classes."""
    _ENABLED["on"] = False
    with _LAYERS_LOCK:
        layers = list(_LAYERS)
    for layer in layers:
        layer.detach()
        try:
            if getattr(layer.node, "group52", None) is layer:
                del layer.node.group52
        except AttributeError:
            _NB_SWALLOW_LOG.debug("swallowed AttributeError in uninstall", exc_info=True)
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g52_orig", None)
    if orig:
        if cls.__dict__.get("__init__") is getattr(cls, "_g52_wrapper", None):
            cls.__init__ = orig
        del cls._g52_orig
        if hasattr(cls, "_g52_wrapper"):
            del cls._g52_wrapper
    _restore_method(getattr(host, "Mempool", None), "submit")
    _restore_method(getattr(host, "P2PNode", None), "_handle_message")
