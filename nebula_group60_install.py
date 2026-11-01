"""NEBULA group60 wiring layer.

Connects the 20 formerly-dead classes of ``nebula_group60.py`` to a running
``NEBULAFullNode`` WITHOUT editing ``nebula_v10_11.py``.

Design rules (taken from nebula_group60_guide.txt):
  * Observe-only: nothing here ever rejects a block, a transaction or a peer.
  * Every callback is wrapped in try/except; failures only increase
    ``layer.errors`` and are kept (bounded) in ``layer.last_errors``.
  * A component that cannot be built (missing host dependency) is *skipped*
    and reported in ``layer.skipped``; it never stops the node.
  * Reversible: ``uninstall(host)`` restores the original behaviour.

Public API
----------
    install(host, config=None)    patch NEBULAFullNode.__init__ (+ Mempool.submit)
    uninstall(host)               undo install()
    Layer60(node, module=None, config=None)
"""
from __future__ import annotations

import json
import logging
import os
import secrets
import threading
import time
from collections import deque
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group60")

# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

_ORACLE_NAMES = ("oracle_v2", "oracle", "price_oracle")
_STNBL_NAMES = ("stnbl", "staked_nbl", "liquid_staking", "staking_v2")
_NFT_NAMES = ("nft", "nbl721", "nft_registry")
_DATA_DIR_NAMES = ("data_dir", "datadir", "_data_dir")


def _find_attr(obj: Any, names: Tuple[str, ...],
               check: Callable[[Any], bool]) -> Any:
    """Return the first attribute of *obj* in *names* that passes *check*."""
    for name in names:
        try:
            value = getattr(obj, name, None)
        except Exception:
            continue
        if value is None:
            continue
        try:
            if check(value):
                return value
        except Exception:
            continue
    return None


def _atomic_write_json(path: Path, payload: dict) -> None:
    """Crash-safe write: tmp file + fsync + rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    data = json.dumps(payload, indent=2, sort_keys=True, default=str)
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


class OracleAdapter:
    """Gives ``ChainlinkStyleOracle`` the ``price(pair)`` API that the DeFi
    classes expect from the host's ``OracleV2``.

    Returns a float (answer / 10**decimals) or ``None`` when the feed has no
    data yet - the DeFi classes already fall back to a default in that case.
    """

    def __init__(self, oracle: Any):
        self._oracle = oracle

    def price(self, pair: str) -> Optional[float]:
        answer = self._oracle.latest_answer(pair)
        if answer is None:
            return None
        feed = self._oracle._feeds.get(pair, {})
        return answer / (10 ** int(feed.get("decimals", 8)))


# ---------------------------------------------------------------------------
# The layer
# ---------------------------------------------------------------------------

class Layer60:
    """Holds one instance of every group60 class and observes the chain."""

    #: refresh cached stats + write snapshot every N connected blocks
    SNAPSHOT_INTERVAL = 144
    #: hard cap for the shadow mempool (RAM protection)
    SHADOW_POOL_CAP = 5000
    #: how many recent errors are remembered
    ERROR_LOG_SIZE = 50

    #: (attribute name, class name, stats method) in dependency order
    STATS_METHODS: Tuple[Tuple[str, str], ...] = (
        ("oracle", "oracle_stats"),
        ("ibc", "ibc_stats"),
        ("restaking", "restaking_stats"),
        ("perp", "perp_v2_stats"),
        ("options_vault", "vault_stats"),
        ("isolated_market", "market_stats"),
        ("lending_v3", "protocol_v3_stats"),
        ("launchpad", None),            # needs a project id -> skipped
        ("ve", "ve_stats"),
        ("vesting_manager", "vesting_stats"),
        ("risk", "risk_stats"),
        ("ecosystem", "ecosystem_v2_stats"),
        ("multisig_dao", "dao_stats"),
        ("grants_dao", "grants_stats"),
        ("swap_aggregator", "agg_stats"),
        ("portfolio", "tracker_stats"),
        ("hw_wallet", "hw_stats"),
        ("shadow_mempool", "mempool_stats"),
    )

    def __init__(self, node: Any, module: Any = None,
                 config: Optional[dict] = None):
        if module is None:
            import nebula_group60 as module  # type: ignore
        self.g = module
        self.node = node
        self.bc = node.bc
        self.config = dict(config or {})

        self.errors = 0
        self.last_errors: deque = deque(maxlen=self.ERROR_LOG_SIZE)
        self.skipped: Dict[str, str] = {}
        self.built: List[str] = []
        self.stats_: Dict[str, Any] = {}
        self.counters = {
            "blocks_seen": 0, "reorgs_seen": 0, "txs_shadowed": 0,
            "snapshots_written": 0,
        }
        self.last_height: Optional[int] = None
        self.last_block_hash: Optional[str] = None
        self.last_reorg: Optional[dict] = None
        self._lock = threading.RLock()
        self.attached = False

        # ---- build the 20 classes -----------------------------------------
        self._build_all()

    # ------------------------------------------------------------------ errors
    def _fail(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.last_errors.append(
                {"where": where, "error": repr(exc), "ts": time.time()})
        log.warning("group60 %s failed: %r", where, exc)

    def _guard(self, where: str, fn: Callable[[], Any], default: Any = None):
        try:
            return fn()
        except Exception as exc:      # never propagate into the node
            self._fail(where, exc)
            return default

    # ------------------------------------------------------------------ build
    def _build(self, attr: str, factory: Callable[[], Any],
               requires: Optional[Dict[str, Any]] = None) -> None:
        """Construct one component; record skip / failure instead of raising."""
        for dep_name, dep in (requires or {}).items():
            if dep is None:
                self.skipped[attr] = f"missing host dependency: {dep_name}"
                setattr(self, attr, None)
                return
        try:
            setattr(self, attr, factory())
            self.built.append(attr)
        except Exception as exc:
            setattr(self, attr, None)
            self.skipped[attr] = f"construction failed: {exc!r}"
            self._fail(f"build:{attr}", exc)

    def _build_all(self) -> None:
        g, bc, cfg = self.g, self.bc, self.config

        host_oracle = _find_attr(self.node, _ORACLE_NAMES,
                                 lambda o: callable(getattr(o, "price", None)))
        stnbl = _find_attr(self.node, _STNBL_NAMES,
                           lambda o: callable(getattr(o, "stnbl_balance", None)))
        nft = _find_attr(self.node, _NFT_NAMES,
                         lambda o: callable(getattr(o, "create_collection", None)))

        # 1) oracle first (others depend on it). Prefer the host oracle.
        self._build("oracle", lambda: g.ChainlinkStyleOracle())
        if host_oracle is not None:
            self.price_source = host_oracle
            self.price_source_name = "host"
        elif self.oracle is not None:
            self.price_source = OracleAdapter(self.oracle)
            self.price_source_name = "group60-feed"
        else:
            self.price_source = None
            self.price_source_name = "none"
        orc = self.price_source

        # 2) independent / utility
        self._build("ibc", lambda: g.IBCProtocol(bc))
        self._build("restaking",
                    lambda: g.LiquidRestaking(bc, stnbl),
                    {"stnbl (node.stnbl / node.staked_nbl)": stnbl})
        self._build("perp",
                    lambda: g.PerpetualV2(cfg.get("perp_pair", "NBL/USD"), bc, orc))
        self._build("options_vault",
                    lambda: g.OptionsVault(cfg.get("vault_asset", "NBL"), bc, orc))
        self._build("isolated_market",
                    lambda: g.IsolatedMarket(
                        cfg.get("market_collateral", "NBL"),
                        cfg.get("market_borrow", "USD"),
                        cfg.get("market_ltv", 0.75),
                        cfg.get("market_liq_threshold", 0.80), bc, orc))
        self._build("lending_v3", lambda: g.LendingProtocolV3(bc, orc))

        # 3) NFT
        self._build("mint_phase",
                    lambda: g.NFTMintPhase(
                        cfg.get("phase_name", "public"),
                        cfg.get("phase_start", 0),
                        cfg.get("phase_end", 2 ** 31 - 1),
                        cfg.get("phase_price_nbl", 0.0),
                        cfg.get("phase_max_per_wallet", 5),
                        cfg.get("phase_allowlist")))
        self._build("launchpad",
                    lambda: g.NFTLaunchpadV2(nft, bc),
                    {"nft registry (node.nft / node.nbl721)": nft})

        # 4) economics
        self._build("ve", lambda: g.VeTokenomics(bc))
        self._build("vesting_schedule",
                    lambda: g.VestingScheduleV2(
                        cfg.get("vesting_beneficiary", "unassigned"),
                        cfg.get("vesting_total", 0),
                        cfg.get("vesting_cliff_blocks", 0),
                        cfg.get("vesting_blocks", 1),
                        bc, cfg.get("vesting_type", "linear")))
        self._build("vesting_manager", lambda: g.TokenVestingManager(bc))
        self._build("risk", lambda: g.RiskManagementSystem(bc, orc))
        self._build("ecosystem", lambda: g.NEBULAEcosystemV2(bc))
        self._build("multisig_dao",
                    lambda: g.MultiSigDAO(
                        list(cfg.get("dao_members", [])),
                        int(cfg.get("dao_threshold", 1)), bc))
        self._build("grants_dao",
                    lambda: g.OnChainGrantsDAO(
                        bc, cfg.get("grants_treasury_nbl", 1_000_000)))
        self._build("swap_aggregator", lambda: g.SwapAggregatorV3(bc))
        self._build("portfolio", lambda: g.PortfolioTrackerV2(bc, orc))

        # 5) wallet side - EPHEMERAL seed, never persisted, never the user's key
        self._build("hw_wallet",
                    lambda: g.HardwareWalletSimulator(
                        cfg.get("hw_seed") or secrets.token_bytes(32)))

        # 6) shadow mempool (observe only)
        self._build("shadow_mempool", lambda: g.NEBULAMemoryPool(bc))

    # -------------------------------------------------------- chain listener
    def on_connect(self, block: Any) -> None:
        """Called by the chain for every connected block. Never raises."""
        try:
            with self._lock:
                self.counters["blocks_seen"] += 1
                self.last_height = getattr(block, "height", None)
                if self.last_height is None:
                    self.last_height = getattr(self.bc, "height", None)
                bh = getattr(block, "hash", None)
                if callable(bh):
                    bh = bh()
                self.last_block_hash = None if bh is None else str(bh)
            self._guard("on_connect:prune_shadow",
                        lambda: self._prune_shadow_pool(block))
            h = self.last_height
            if isinstance(h, int) and h % self.SNAPSHOT_INTERVAL == 0:
                self._guard("on_connect:snapshot", self.save_snapshot)
        except Exception as exc:
            self._fail("on_connect", exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        """Called on a chain reorganisation. Never raises."""
        try:
            with self._lock:
                self.counters["reorgs_seen"] += 1
                self.last_reorg = {
                    "ancestor_height": ancestor_height,
                    "old_len": self._safe_len(old),
                    "new_len": self._safe_len(new),
                    "ts": time.time(),
                }
        except Exception as exc:
            self._fail("on_reorg", exc)

    @staticmethod
    def _safe_len(x: Any) -> Optional[int]:
        try:
            return len(x)
        except Exception:
            return None

    # --------------------------------------------------------- shadow mempool
    def observe_tx(self, tx: Any, fee_rate: int = 0) -> bool:
        """Record an ACCEPTED transaction in the shadow mempool (bounded).

        Never affects the host's own mempool. Returns True if recorded.
        """
        pool = self.shadow_mempool
        if pool is None:
            return False
        try:
            if not hasattr(tx, "txid") or not hasattr(tx, "byte_size"):
                return False
            with pool._lock:
                if len(pool._pool) >= self.SHADOW_POOL_CAP:
                    # evict the lowest fee-rate entry
                    victim = min(pool._pool.items(),
                                 key=lambda kv: kv[1]["fee_rate"])[0]
                    del pool._pool[victim]
            ok, _ = pool.submit_tx(tx, int(fee_rate or 0),
                                   getattr(self.bc, "utxo", None))
            if ok:
                with self._lock:
                    self.counters["txs_shadowed"] += 1
            return bool(ok)
        except Exception as exc:
            self._fail("observe_tx", exc)
            return False

    def _prune_shadow_pool(self, block: Any) -> None:
        """Drop txs from the shadow pool that are now confirmed in *block*."""
        pool = self.shadow_mempool
        txs = getattr(block, "transactions", None) or getattr(block, "txs", None)
        if pool is None or not txs:
            return
        with pool._lock:
            for tx in txs:
                txid = getattr(tx, "txid", None)
                if txid is not None:
                    pool._pool.pop(txid, None)

    # ------------------------------------------------------------ stats / API
    def refresh_stats(self) -> Dict[str, Any]:
        """Call every component's read-only stats method (each guarded)."""
        out: Dict[str, Any] = {}
        for attr, method in self.STATS_METHODS:
            obj = getattr(self, attr, None)
            if obj is None or method is None:
                continue
            out[attr] = self._guard(
                f"stats:{attr}", lambda o=obj, m=method: getattr(o, m)(),
                default={"error": "stats failed"})
        # extras that live on the layer itself
        if getattr(self, "mint_phase", None) is not None:
            out["mint_phase"] = {
                "name": self.mint_phase.name,
                "start_block": self.mint_phase.start_block,
                "end_block": self.mint_phase.end_block,
                "wallets_minted": len(self.mint_phase.minted),
            }
        if getattr(self, "vesting_schedule", None) is not None:
            out["vesting_schedule"] = self._guard(
                "stats:vesting_schedule", self.vesting_schedule.vesting_info,
                default={"error": "stats failed"})
        if getattr(self, "risk", None) is not None:
            out["risk_score"] = self._guard(
                "stats:risk_score", self.risk.global_risk_score,
                default={"error": "stats failed"})
        with self._lock:
            self.stats_ = out
        return out

    def snapshot(self) -> Dict[str, Any]:
        """JSON-serialisable view of the whole layer (used by REST / disk)."""
        stats = self.refresh_stats()
        with self._lock:
            return {
                "layer": "group60",
                "attached": self.attached,
                "price_source": self.price_source_name,
                "built": list(self.built),
                "skipped": dict(self.skipped),
                "errors": self.errors,
                "last_errors": list(self.last_errors)[-10:],
                "counters": dict(self.counters),
                "last_height": self.last_height,
                "last_block_hash": self.last_block_hash,
                "last_reorg": self.last_reorg,
                "stats": stats,
                "ts": time.time(),
            }

    def api_get(self, path: str = "/api/group60/stats") -> Tuple[int, str]:
        """Read-only (GET) helper any REST/RPC layer can call.

        Returns ``(http_status, json_text)``.
        """
        try:
            return 200, json.dumps(self.snapshot(), default=str)
        except Exception as exc:
            self._fail("api_get", exc)
            return 500, json.dumps({"error": "snapshot failed"})

    # --------------------------------------------------------------- storage
    def data_dir(self) -> Optional[Path]:
        for name in _DATA_DIR_NAMES:
            value = getattr(self.node, name, None)
            if value:
                try:
                    return Path(value)
                except Exception:
                    continue
        return None

    def save_snapshot(self) -> Optional[Path]:
        """Atomically write the snapshot to <data_dir>/group60_snapshot.json."""
        base = self.data_dir()
        if base is None:
            return None
        path = base / "group60_snapshot.json"
        _atomic_write_json(path, self.snapshot())
        with self._lock:
            self.counters["snapshots_written"] += 1
        return path

    # ----------------------------------------------------------- attach/detach
    def attach(self) -> None:
        self.bc.add_listener(self)
        self.attached = True

    def detach(self) -> None:
        """Remove this layer from the chain's listener list."""
        try:
            remover = getattr(self.bc, "remove_listener", None)
            if callable(remover):
                remover(self)
            else:
                self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer60.detach", exc_info=True)
        self.attached = False


# ---------------------------------------------------------------------------
# install / uninstall  (same pattern as group 5)
# ---------------------------------------------------------------------------

def _wrap_mempool_submit(host: Any) -> None:
    """Shadow-record accepted transactions; the host's result is returned
    UNCHANGED and any shadow error is swallowed."""
    cls = getattr(host, "Mempool", None)
    if cls is None or not hasattr(cls, "submit"):
        return
    if getattr(cls, "_g60_submit_orig", None):
        return
    orig = cls.submit

    def patched(self, *args, **kwargs):
        result = orig(self, *args, **kwargs)
        try:
            ok = result[0] if isinstance(result, tuple) else bool(result)
            layer = _LAYER_BY_MEMPOOL.get(id(self))
            if ok and layer is not None and args:
                tx = args[0]
                fee_rate = getattr(tx, "fee_rate", 0)
                layer.observe_tx(tx, fee_rate if isinstance(fee_rate, int) else 0)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _wrap_mempool_submit.patched", exc_info=True)
        return result

    cls._g60_submit_orig = orig
    cls.submit = patched


def _unwrap_mempool_submit(host: Any) -> None:
    cls = getattr(host, "Mempool", None)
    orig = getattr(cls, "_g60_submit_orig", None) if cls is not None else None
    if orig:
        cls.submit = orig
        del cls._g60_submit_orig


# maps id(host mempool object) -> Layer60 (so the class-level wrapper can find
# the layer of the node that owns that mempool)
_LAYER_BY_MEMPOOL: Dict[int, Layer60] = {}


def install(host: Any, config: Optional[dict] = None) -> None:
    """Patch ``host.NEBULAFullNode.__init__`` so every new node gets
    ``node.group60``. Idempotent."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g60_orig", None):
        return
    orig_init = cls.__init__

    def patched(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)          # the node starts as before
        try:
            layer = Layer60(self, config=config)
            layer.attach()
            self.group60 = layer
            mp = getattr(getattr(self, "bc", None), "mempool", None)
            if mp is not None:
                _LAYER_BY_MEMPOOL[id(mp)] = layer
        except Exception as exc:                   # node must still start
            self.group60_error = exc
            log.warning("group60 install failed: %r", exc)

    cls._g60_orig = orig_init
    cls.__init__ = patched
    _wrap_mempool_submit(host)


def uninstall(host: Any) -> None:
    """Undo ``install``. Existing nodes keep working; new nodes are plain."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g60_orig", None)
    if orig:
        cls.__init__ = orig
        del cls._g60_orig
    _unwrap_mempool_submit(host)
    _LAYER_BY_MEMPOOL.clear()


def detach_node(node: Any) -> None:
    """Detach the layer from one already-running node."""
    layer = getattr(node, "group60", None)
    if layer is not None:
        layer.detach()
        mp = getattr(getattr(node, "bc", None), "mempool", None)
        if mp is not None:
            _LAYER_BY_MEMPOOL.pop(id(mp), None)
