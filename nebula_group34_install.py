"""NEBULA group34 wiring layer.

Connects the 20 revived classes of nebula_group34.py to the live chain WITHOUT editing the host file:

    install(host)   -> wraps host.NEBULAFullNode.__init__; every node gets `node.group34` (a Layer34)
    uninstall(host) -> restores the original __init__, detaches listeners, removes REST routes

What the layer does (all of it is report-only: it never rejects a block or a transaction):

    * chain listener  : bc.add_listener(layer) -> on_connect(block) / on_reorg(old, new, ancestor_height)
    * ShardManager    : routes every confirmed tx, builds one ShardBlock per shard per block, runs the
                        two-block cross-shard receipt protocol, rolls everything back on reorg
    * MerkleProver    : bounded txid -> block index; inclusion proofs on demand (light-client style)
    * ReputationEngine: fed with live activity (tx count / first-seen height) collected from blocks
    * OnChainRNG/VRF  : verified VRF entropy submission; randomness for any mined height
    * OnChainLottery  : rounds are drawn automatically once the seed block exists, undone on reorg
    * REST            : read-only GET endpoints under /api/v2 (via the host's @route decorator)
    * DataMarket, PredictionMarket, NEBULATreasury, StateChannel, NodeCluster: constructed, owned by
      the layer and exposed read-only over REST; mutations go through the Python API
      (node.group34.markets.buy(...), ...). They are in-memory ledgers - they do NOT move UTXOs.

Every assumption about the shape of host objects (block / transaction fields) lives in HostAdapter below.
If your host uses other field names, that is the ONLY place that needs to change.
"""
from __future__ import annotations

import hashlib
import json
import threading
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group34 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

__all__ = ["Group34Config", "HostAdapter", "Layer34", "install", "uninstall"]


# ====================================================================================================
# Configuration
# ====================================================================================================
@dataclass
class Group34Config:
    """Tunables. Every cache is bounded so the layer cannot grow without limit on a small server."""
    backfill_blocks:       int  = 144      # blocks replayed from the tip at start-up (0 = none)
    tx_index_blocks:       int  = 1008     # blocks kept in the tx index / reorg-rollback window
    shard_keep_blocks:     int  = 288      # shard blocks kept per shard
    n_shards:              int  = g.SHARD_COUNT
    cross_finality_blocks: int  = 2        # receipt protocol latency (matches throughput_estimate note)
    cross_keep:            int  = 10_000   # finalized cross-shard messages kept
    auto_draw_lottery:     bool = True
    lottery_winners:       int  = 3
    max_entropy_per_height: int = 64
    max_channels:          int  = 1_000
    register_routes:       bool = True
    cluster_nodes_max:     int  = 10
    # NodeCluster builds one blockchain object per simulated node. The default chain constructor of
    # the host might open the production data dir, so a factory must be given explicitly (or the
    # opt-in flag set) before a cluster can be created.
    cluster_blockchain_factory:        Optional[Callable[[], Any]] = None
    allow_default_cluster_blockchain:  bool = False


# ====================================================================================================
# Host adapter - the single place that knows field names of host blocks / transactions
# ====================================================================================================
class HostAdapter:
    """Defensive accessors for host block/tx objects (attribute or dict style)."""

    ADDR_ATTRS  = ("address", "addr", "recipient", "script_address", "to_address")
    VALUE_ATTRS = ("value", "amount", "nvalue")

    @staticmethod
    def _get(obj: Any, name: str) -> Any:
        if obj is None:
            return None
        if isinstance(obj, dict):
            return obj.get(name)
        v = getattr(obj, name, None)
        return v() if callable(v) else v

    @classmethod
    def _first(cls, obj: Any, names: Tuple[str, ...], default: Any = None) -> Any:
        for n in names:
            v = cls._get(obj, n)
            if v is not None:
                return v
        return default

    @classmethod
    def block_height(cls, block: Any) -> int:
        h = cls._first(block, ("height",))
        if h is None:
            raise ValueError("block has no height")
        return int(h)

    @classmethod
    def block_hash(cls, block: Any) -> str:
        h = cls._first(block, ("hash", "block_hash"))
        if h is None:
            raise ValueError("block has no hash")
        return h if isinstance(h, str) else (h.hex() if isinstance(h, (bytes, bytearray)) else str(h))

    @classmethod
    def block_txs(cls, block: Any) -> List[Any]:
        return list(cls._first(block, ("transactions", "txs"), []) or [])

    @classmethod
    def block_time(cls, block: Any) -> float:
        hdr = cls._get(block, "header")
        ts = cls._first(hdr, ("timestamp", "time")) if hdr is not None else None
        if ts is None:
            ts = cls._first(block, ("timestamp", "time"))
        try:
            return float(ts)
        except (TypeError, ValueError):
            return time.time()

    @classmethod
    def tx_id(cls, tx: Any) -> str:
        t = cls._first(tx, ("txid", "hash", "id"))
        if t is None:
            return ""
        return t if isinstance(t, str) else (t.hex() if isinstance(t, (bytes, bytearray)) else str(t))

    @classmethod
    def tx_outputs(cls, tx: Any) -> List[Tuple[str, int]]:
        outs = cls._first(tx, ("outputs", "vout", "outs"), []) or []
        result: List[Tuple[str, int]] = []
        for o in outs:
            addr = cls._first(o, cls.ADDR_ATTRS)
            if not addr:
                continue
            try:
                amt = int(cls._first(o, cls.VALUE_ATTRS, 0) or 0)
            except (TypeError, ValueError):
                amt = 0
            result.append((str(addr), amt))
        return result

    @classmethod
    def tx_input_addrs(cls, tx: Any) -> List[str]:
        ins = cls._first(tx, ("inputs", "vin", "ins"), []) or []
        addrs = []
        for i in ins:
            a = cls._first(i, cls.ADDR_ATTRS)
            if a:
                addrs.append(str(a))
        return addrs

    @classmethod
    def is_coinbase(cls, tx: Any) -> bool:
        v = cls._get(tx, "is_coinbase")
        if v is not None:
            return bool(v)
        ins = cls._first(tx, ("inputs", "vin", "ins"), []) or []
        if not ins:
            return True
        prev = cls._first(ins[0], ("prev_txid", "prev_hash", "txid"))
        return isinstance(prev, str) and prev != "" and set(prev) <= {"0"}


# ====================================================================================================
# Small helpers
# ====================================================================================================
class _BadRequest(ValueError):
    pass


class _NotFound(LookupError):
    pass


def _jsonable(x: Any) -> Any:
    """Make proofs / dicts safe for json.dumps (bytes -> hex, tuples/sets -> lists)."""
    if isinstance(x, (bytes, bytearray)):
        return bytes(x).hex()
    if isinstance(x, dict):
        return {str(k): _jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple, set)):
        return [_jsonable(v) for v in x]
    return x


def _flatten(query: Any) -> Dict[str, Any]:
    """parse_qs style {k: [v]} or plain {k: v} -> {k: v}."""
    out: Dict[str, Any] = {}
    for k, v in (query or {}).items():
        out[str(k)] = v[0] if isinstance(v, (list, tuple)) and v else v
    return out


def _p_str(p: dict, key: str, required: bool = True, maxlen: int = 200) -> str:
    v = p.get(key, "")
    v = "" if v is None else str(v)
    if required and not v:
        raise _BadRequest(f"bad request: '{key}' is required")
    if len(v) > maxlen:
        raise _BadRequest(f"bad request: '{key}' too long")
    return v


def _p_int(p: dict, key: str, default: Optional[int], lo: int, hi: int) -> int:
    if key not in p or p[key] in (None, ""):
        if default is None:
            raise _BadRequest(f"bad request: '{key}' is required")
        return default
    try:
        v = int(p[key])
    except (TypeError, ValueError):
        raise _BadRequest(f"bad request: '{key}' must be an integer")
    if not (lo <= v <= hi):
        raise _BadRequest(f"bad request: '{key}' must be between {lo} and {hi}")
    return v


def _p_float(p: dict, key: str, default: float) -> float:
    if key not in p or p[key] in (None, ""):
        return default
    try:
        v = float(p[key])
    except (TypeError, ValueError):
        raise _BadRequest(f"bad request: '{key}' must be a number")
    if v != v or v in (float("inf"), float("-inf")):
        raise _BadRequest(f"bad request: '{key}' must be finite")
    return v


def _shard_block_hash(sb: "g.ShardBlock") -> str:
    payload = json.dumps([sb.shard_id, sb.height, sb.prev_hash, sorted(sb.txs),
                          sb.state_root, sb.proposer], separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


@dataclass
class _BlockRecord:
    height:     int
    block_hash: str
    txids:      List[str]
    touched:    List[str]     # addresses credited with one activity point each (for rollback)
    cross_ids:  List[str]     # cross-shard message ids created for this block


# ====================================================================================================
# The layer
# ====================================================================================================
class Layer34:
    """Owns the group34 services for one node and listens to its chain."""

    def __init__(self, node: Any, config: Optional[Group34Config] = None, host: Any = None):
        self.node   = node
        self.host   = host
        self.cfg    = config or Group34Config()
        self.bc     = getattr(node, "bc", None) or getattr(node, "blockchain", None)
        if self.bc is None:
            raise RuntimeError("group34: node has no blockchain attribute (expected node.bc)")

        self.errors      = 0
        self.last_error  = ""
        self.stats_: Dict[str, int] = {
            "blocks_processed": 0, "blocks_skipped": 0, "reorgs": 0, "rollback_window_exceeded": 0,
            "txs_seen": 0, "cross_shard_txs": 0, "cross_finalized": 0,
            "lottery_draws": 0, "lottery_resets": 0, "entropy_accepted": 0, "entropy_rejected": 0,
        }
        self._lock      = threading.RLock()
        self._attached  = False
        self._registered: List[Tuple[str, str, Callable]] = []   # (method, path, handler)
        self.routes_skipped: List[str] = []

        # ---- services (the 20 classes) ----
        staking = getattr(node, "staking", None)
        social  = getattr(node, "social", None)
        self.data_market = g.DataMarket(self.bc)
        self.reputation  = g.ReputationEngine(self.bc, staking, social)
        self.reputation.activity_provider = self._activity_of
        self.api_v2      = g.APIv2Router(node)
        self.prover      = g.MerkleProver
        self.treasury    = g.NEBULATreasury(self.bc)
        self.shards      = g.ShardManager(self.cfg.n_shards)
        self.markets     = g.PredictionMarket(self.bc)
        self.vrf         = g.VRF
        self.rng         = g.OnChainRNG(self.bc)
        self.lottery     = g.OnChainLottery(self.bc, self.rng)
        self.channels: "OrderedDict[str, g.StateChannel]" = OrderedDict()
        self.cluster: Optional[g.NodeCluster] = None

        # ---- derived chain state (rebuilt from blocks; rolled back on reorg) ----
        self.tip_height: Optional[int] = None
        self._records:       "OrderedDict[int, _BlockRecord]" = OrderedDict()
        self._tx_index:      Dict[str, int]       = {}      # txid -> height
        self._activity:      Dict[str, List[int]] = {}      # address -> [tx_count, first_height]
        self._pending_cross: Dict[str, int]       = {}      # cross msg id -> creation height
        self._entropy_keys:  Dict[int, set]       = {}      # height -> {pubkey hex} already used

        self._register_endpoints()

    # ------------------------------------------------------------------ plumbing
    def _fail(self, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.last_error = f"{where}: {type(exc).__name__}: {exc}"

    def attach(self) -> None:
        """Backfill recent blocks, subscribe to the chain, then bind REST routes."""
        if self._attached:
            return
        try:
            self.backfill(self.cfg.backfill_blocks)
        except Exception as e:
            self._fail("backfill", e)
        try:
            self.bc.add_listener(self)
            self._attached = True
        except Exception as e:
            self._fail("add_listener", e)
        try:
            self._catch_up()
        except Exception as e:
            self._fail("catch_up", e)
        if self.cfg.register_routes and self.host is not None:
            try:
                self.bind_routes(self.host)
            except Exception as e:
                self._fail("bind_routes", e)

    def detach(self) -> None:
        try:
            remover = getattr(self.bc, "remove_listener", None)
            if callable(remover):
                remover(self)
            else:
                self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer34.detach", exc_info=True)
        self._attached = False
        self.unbind_routes()

    def backfill(self, n_blocks: int) -> int:
        """Replay up to n_blocks blocks ending at the tip, oldest first."""
        if n_blocks <= 0:
            return 0
        tip = int(self.bc.height)
        done = 0
        for h in range(max(0, tip - n_blocks + 1), tip + 1):
            blk = self.bc.get_block(h)
            if blk is not None and self._process_block(blk):
                done += 1
        return done

    def _catch_up(self) -> None:
        tip = int(self.bc.height)
        start = (self.tip_height + 1) if self.tip_height is not None else tip
        for h in range(start, tip + 1):
            blk = self.bc.get_block(h)
            if blk is not None:
                self._process_block(blk)

    # ------------------------------------------------------------------ chain listener API
    def on_connect(self, block: Any) -> None:
        """Called by the chain for every block added to the best chain. Never raises."""
        try:
            self._process_block(block)
        except Exception as e:
            self._fail("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        """Called by the chain when the best chain switches. Never raises."""
        try:
            with self._lock:
                self.stats_["reorgs"] += 1
                self._rollback_to(int(ancestor_height))
                # Some hosts also call on_connect for every new block; _process_block is idempotent
                # per (height, hash), so replaying `new` here is safe either way.
                try:
                    blocks = sorted(list(new or []), key=HostAdapter.block_height)
                except Exception:
                    blocks = []
                for blk in blocks:
                    self._process_block(blk)
        except Exception as e:
            self._fail("on_reorg", e)

    # ------------------------------------------------------------------ block processing
    def _bump_activity(self, address: str, height: int) -> None:
        st = self._activity.get(address)
        if st is None:
            self._activity[address] = [1, height]
        else:
            st[0] += 1

    def _activity_of(self, address: str) -> Tuple[int, Optional[int]]:
        with self._lock:
            st = self._activity.get(address)
            return (st[0], st[1]) if st else (0, None)

    def _process_block(self, block: Any) -> bool:
        """Index one block. Returns False when it was already known (idempotent)."""
        height = HostAdapter.block_height(block)
        bhash  = HostAdapter.block_hash(block)
        with self._lock:
            rec = self._records.get(height)
            if rec is not None:
                if rec.block_hash == bhash:
                    return False
                self._rollback_to(height - 1)                  # different block at a known height
            elif self._records and height <= max(self._records):
                if height < min(self._records):
                    self.stats_["blocks_skipped"] += 1          # older than the window
                    return False
                self._rollback_to(height - 1)

            txs        = HostAdapter.block_txs(block)
            ts         = HostAdapter.block_time(block)
            proposer   = ""
            txids:     List[str] = []
            touched:   List[str] = []
            cross_ids: List[str] = []
            per_shard: Dict[int, List[str]] = {i: [] for i in range(self.shards.n_shards)}

            for tx in txs:
                txid = HostAdapter.tx_id(tx)
                if not txid:
                    continue
                txids.append(txid)
                outs      = HostAdapter.tx_outputs(tx)
                coinbase  = HostAdapter.is_coinbase(tx)
                senders   = [] if coinbase else HostAdapter.tx_input_addrs(tx)
                if coinbase and outs and not proposer:
                    proposer = outs[0][0]

                for a in dict.fromkeys(senders + [o[0] for o in outs]):
                    self._bump_activity(a, height)
                    touched.append(a)

                sender = senders[0] if senders else None
                target = next((o for o in outs if o[0] != sender), outs[0] if outs else None)
                if target is None:
                    continue
                recipient, amount = target
                shard, is_cross = self.shards.route_tx(txid, sender or recipient, recipient)
                self.shards.discard_pending(txid, shard)        # it is confirmed, not pending
                per_shard[shard].append(txid)
                if is_cross and sender:
                    mid = self.shards.initiate_cross_shard(sender, recipient, amount)
                    cross_ids.append(mid)
                    self._pending_cross[mid] = height
                    self.stats_["cross_shard_txs"] += 1

            self.stats_["txs_seen"] += len(txids)
            self._build_shard_blocks(height, ts, proposer, per_shard)

            for mid, created in list(self._pending_cross.items()):    # receipt protocol: finalize
                if height - created >= self.cfg.cross_finality_blocks:
                    ok_, _ = self.shards.finalize_cross_shard(mid)
                    del self._pending_cross[mid]
                    if ok_:
                        self.stats_["cross_finalized"] += 1
            self.shards.trim_finalized(self.cfg.cross_keep)

            for t in txids:
                self._tx_index[t] = height
            self._records[height] = _BlockRecord(height, bhash, txids, touched, cross_ids)
            self.tip_height = max(self._records)
            self._trim_window()
            self.stats_["blocks_processed"] += 1

            if self.cfg.auto_draw_lottery:
                self._auto_draw()
            return True

    def _build_shard_blocks(self, height: int, ts: float, proposer: str,
                            per_shard: Dict[int, List[str]]) -> None:
        for sid in range(self.shards.n_shards):
            tip   = self.shards.shard_tip(sid)
            prev  = _shard_block_hash(tip) if tip else "0" * 64
            # "state_root" here is a rolling commitment over the shard's confirmed txids.
            commit = hashlib.sha256(
                ((tip.state_root if tip else "") + "".join(sorted(per_shard[sid]))).encode()
            ).hexdigest()
            self.shards.add_shard_block(
                g.ShardBlock(shard_id=sid, height=height, prev_hash=prev, txs=list(per_shard[sid]),
                             state_root=commit, timestamp=ts, proposer=proposer),
                keep=self.cfg.shard_keep_blocks)

    def _trim_window(self) -> None:
        while len(self._records) > self.cfg.tx_index_blocks:
            _, old = self._records.popitem(last=False)
            for t in old.txids:
                self._tx_index.pop(t, None)
            self._entropy_keys.pop(old.height, None)

    def _auto_draw(self) -> None:
        for rid in self.lottery.due_rounds():
            ok_, _ = self.lottery.draw(rid, self.cfg.lottery_winners)
            if ok_:
                self.stats_["lottery_draws"] += 1

    def _rollback_to(self, height: int) -> None:
        """Undo every derived effect of blocks above `height`."""
        with self._lock:
            if self._records and height < min(self._records) - 1:
                self.stats_["rollback_window_exceeded"] += 1
            dropped_cross: List[str] = []
            for h in sorted((h for h in self._records if h > height), reverse=True):
                rec = self._records.pop(h)
                for t in rec.txids:
                    self._tx_index.pop(t, None)
                for a in rec.touched:
                    st = self._activity.get(a)
                    if st:
                        st[0] -= 1
                        if st[0] <= 0:
                            del self._activity[a]
                for mid in rec.cross_ids:
                    self._pending_cross.pop(mid, None)
                dropped_cross.extend(rec.cross_ids)
                self._entropy_keys.pop(h, None)
            self.shards.rollback_above(height)
            if dropped_cross:
                self.shards.drop_cross_messages(dropped_cross)
            self.rng.drop_entropy_above(height)
            self.stats_["lottery_resets"] += len(self.lottery.reset_if_reorged())
            self.tip_height = max(self._records) if self._records else None

    # ------------------------------------------------------------------ public helpers
    def prove_tx(self, txid: str) -> dict:
        """Merkle inclusion proof for an indexed transaction (verified before it is returned)."""
        with self._lock:
            height = self._tx_index.get(txid)
            rec    = self._records.get(height) if height is not None else None
        if height is None or rec is None:
            raise _NotFound("not found: txid is not in the indexed window")
        block = self.bc.get_block(height)
        if block is None or HostAdapter.block_hash(block) != rec.block_hash:
            raise _NotFound("not found: block was reorganised away")
        proof = self.prover.prove_inclusion(txid, block)
        if proof is None:
            raise _NotFound("not found: txid is not in that block")
        proof["verified"] = self.prover.verify_inclusion(proof)
        return _jsonable(proof)

    def _rng_message(self, height: int) -> bytes:
        blk = self.bc.get_block(height)
        if blk is None:
            raise _BadRequest("bad request: block not found")
        return hashlib.sha256(b"G34-RNG" + height.to_bytes(8, "big")
                              + HostAdapter.block_hash(blk).encode()).digest()

    def vrf_prove(self, privkey: int, height: int) -> Tuple[bytes, bytes]:
        """Validator side: produce (vrf_output, proof) for `height` (to submit with submit_entropy)."""
        return self.vrf.prove(privkey, self._rng_message(height))

    def submit_entropy(self, height: int, pubkey: bytes, vrf_output: bytes, proof: bytes) -> bool:
        """Accept a VRF contribution only if its proof verifies for this block (one per key/height)."""
        with self._lock:
            try:
                if height < 0 or height > int(self.bc.height):
                    raise _BadRequest("bad request: height not mined yet")
                keys = self._entropy_keys.setdefault(height, set())
                pk   = bytes(pubkey).hex()
                if pk in keys or len(keys) >= self.cfg.max_entropy_per_height:
                    raise _BadRequest("bad request: duplicate key or height is full")
                if not self.vrf.verify(pubkey, self._rng_message(height), vrf_output, proof):
                    raise _BadRequest("bad request: invalid VRF proof")
            except _BadRequest:
                self.stats_["entropy_rejected"] += 1
                return False
            keys.add(pk)
            self.rng.contribute_entropy(height, vrf_output)
            self.stats_["entropy_accepted"] += 1
            return True

    def open_channel(self, participants: List[str], deposits: Dict[str, int]) -> str:
        """Create and register a StateChannel (bounded registry; closed channels are evicted first)."""
        with self._lock:
            if len(self.channels) >= self.cfg.max_channels:
                victim = next((cid for cid, ch in self.channels.items()
                               if getattr(ch.current_state, "final", False)), None)
                if victim is None:
                    raise RuntimeError("channel registry is full")
                del self.channels[victim]
            cid = hashlib.sha256(
                f"CH:{','.join(participants)}:{time.time()}:{len(self.channels)}".encode()
            ).hexdigest()[:16]
            self.channels[cid] = g.StateChannel(cid, list(participants), dict(deposits))
            return cid

    def get_cluster(self, n_nodes: int = 5, factory: Optional[Callable[[], Any]] = None) -> "g.NodeCluster":
        """Create (once) the simulated NodeCluster. Needs an explicit chain factory - see Group34Config."""
        with self._lock:
            if self.cluster is not None:
                return self.cluster
            factory = factory or self.cfg.cluster_blockchain_factory
            if factory is None and not self.cfg.allow_default_cluster_blockchain:
                raise RuntimeError(
                    "NodeCluster needs an in-memory chain factory (Group34Config.cluster_blockchain_factory) "
                    "or allow_default_cluster_blockchain=True")
            self.cluster = g.NodeCluster(max(1, min(int(n_nodes), self.cfg.cluster_nodes_max)),
                                         blockchain_factory=factory)
            return self.cluster

    def status(self) -> dict:
        with self._lock:
            return {
                "attached":          self._attached,
                "tip_height":        self.tip_height,
                "errors":            self.errors,
                "last_error":        self.last_error,
                "stats":             dict(self.stats_),
                "txs_indexed":       len(self._tx_index),
                "addresses_tracked": len(self._activity),
                "routes_registered": len(self._registered),
                "routes_skipped":    list(self.routes_skipped),
                "shards":            self.shards.shard_stats(),
                "data_market":       self.data_market.market_stats(),
                "markets":           self.markets.market_stats(),
                "lottery_rounds":    len(self.lottery._rounds),
                "channels":          len(self.channels),
                "cluster":           self.cluster is not None,
            }

    # ------------------------------------------------------------------ REST (read-only GET)
    def _register_endpoints(self) -> None:
        r = self.api_v2.register

        r("/g34/status",              lambda p: self.status())
        r("/g34/data/search",         self._h_data_search)
        r("/g34/data/stats",          lambda p: self.data_market.market_stats())
        r("/g34/reputation",          self._h_reputation)
        r("/g34/reputation/leaderboard",
          lambda p: self.reputation.leaderboard(_p_int(p, "n", 20, 1, 100)))
        r("/g34/treasury",            lambda p: self.treasury.budget_report())
        r("/g34/treasury/grants",     lambda p: self.treasury.grant_history())
        r("/g34/shards",              lambda p: self.shards.shard_stats())
        r("/g34/shards/throughput",   lambda p: self.shards.throughput_estimate())
        r("/g34/shards/address",      self._h_shard_of)
        r("/g34/markets",             lambda p: self.markets.list_markets(str(p.get("open", "1")) != "0"))
        r("/g34/markets/stats",       lambda p: self.markets.market_stats())
        r("/g34/market",              self._h_market)
        r("/g34/lottery/round",       self._h_lottery_round)
        r("/g34/merkle/proof",        lambda p: self.prove_tx(_p_str(p, "txid", maxlen=128)))
        r("/g34/merkle/verify",       self._h_merkle_verify)
        r("/g34/rng",                 self._h_rng)
        r("/g34/channels",            lambda p: [self._channel_row(c) for c in list(self.channels.values())[-100:]])
        r("/g34/channel",             self._h_channel)
        r("/g34/cluster/health",      self._h_cluster_health)
        r("/g34/cluster/propagation", self._h_cluster_propagation)

    @staticmethod
    def _channel_row(ch: "g.StateChannel") -> dict:
        return ch.channel_info()

    def _h_data_search(self, p: dict) -> list:
        res = self.data_market.search(
            query=_p_str(p, "query", required=False), category=_p_str(p, "category", required=False, maxlen=40),
            max_price=_p_float(p, "max_price", 0.0), min_rating=_p_float(p, "min_rating", 0.0))
        return res[:_p_int(p, "limit", 50, 1, 200)]

    def _h_reputation(self, p: dict) -> dict:
        return self.reputation.get_score(_p_str(p, "address", maxlen=100)).to_dict()

    def _h_shard_of(self, p: dict) -> dict:
        a = _p_str(p, "address", maxlen=100)
        return {"address": a, "shard": self.shards.address_to_shard(a)}

    def _h_market(self, p: dict) -> dict:
        info = self.markets.market_info(_p_str(p, "market_id", maxlen=64))
        if info is None:
            raise _NotFound("not found: market")
        return info

    def _h_lottery_round(self, p: dict) -> dict:
        info = self.lottery.round_info(_p_int(p, "round_id", None, 1, 10**9))
        if info is None:
            raise _NotFound("not found: round")
        return _jsonable(info)

    def _h_merkle_verify(self, p: dict) -> dict:
        try:
            proof = json.loads(_p_str(p, "proof", maxlen=20000))
        except ValueError:
            raise _BadRequest("bad request: 'proof' must be JSON")
        if not isinstance(proof, dict):
            raise _BadRequest("bad request: 'proof' must be a JSON object")
        return {"valid": self.prover.verify_inclusion(proof)}

    def _h_rng(self, p: dict) -> dict:
        height = _p_int(p, "height", None, 0, 10**9)
        nonce  = _p_int(p, "nonce", 0, 0, 2**63 - 1)
        max_v  = _p_int(p, "max", 1_000_000, 1, 2**63 - 1)
        try:
            raw = self.rng.get_randomness(height, nonce)
        except ValueError as e:
            raise _BadRequest(f"bad request: {e}")
        return {"height": height, "nonce": nonce, "randomness": raw.hex(),
                "random_int": int.from_bytes(raw, "big") % max_v, "max": max_v}

    def _h_channel(self, p: dict) -> dict:
        ch = self.channels.get(_p_str(p, "channel_id", maxlen=64))
        if ch is None:
            raise _NotFound("not found: channel")
        return ch.channel_info()

    def _h_cluster_health(self, p: dict) -> dict:
        if self.cluster is None:
            raise _NotFound("not found: no cluster created")
        return self.cluster.cluster_health()

    def _h_cluster_propagation(self, p: dict) -> dict:
        if self.cluster is None:
            raise _NotFound("not found: no cluster created")
        return self.cluster.propagation_test({"type": "ping"})

    # ---- binding to the host's route registry
    def _reply(self, res: dict) -> Tuple[int, dict]:
        if res.get("ok"):
            data = res.get("data")
            ok_fn = getattr(self.host, "ok", None)
            if callable(ok_fn):
                try:
                    out = ok_fn(data if data is not None else {})
                    if isinstance(out, tuple):
                        return out
                except Exception:
                    _NB_SWALLOW_LOG.debug("swallowed Exception in Layer34._reply", exc_info=True)
            return 200, {"success": True, "data": data}
        msg = str(res.get("error", "error"))
        if msg.startswith("Route not found") or msg.startswith("not found"):
            code = 404
        elif msg.startswith("bad request"):
            code = 400
        elif "has no attribute" in msg:
            code = 503          # a subsystem this node does not have (e.g. node.governance missing)
        else:
            code = 500
        return code, {"success": False, "error": msg}

    def _make_handler(self, full_path: str) -> Callable:
        def handler(path, query, body):
            try:
                return self._reply(self.api_v2.handle(full_path, _flatten(query)))
            except Exception as e:          # never let an exception escape into the HTTP thread
                self._fail("rest", e)
                return 500, {"success": False, "error": "internal error"}
        handler._g34 = True
        return handler

    def bind_routes(self, host: Any) -> int:
        """Register every /api/v2 route (the router's own and the g34 ones) as GET endpoints."""
        reg = getattr(host, "route", None)
        table = getattr(host, "_routes", None)
        if not callable(reg) or table is None:
            raise RuntimeError("host has no route()/_routes registry")
        existing = table.get("GET", {})
        count = 0
        for full in self.api_v2.list_routes():
            if full in existing:
                self.routes_skipped.append(full)       # never override a route the host already has
                continue
            handler = self._make_handler(full)
            reg(full, ["GET"])(handler)
            self._registered.append(("GET", full, handler))
            count += 1
        return count

    def unbind_routes(self) -> None:
        table = getattr(self.host, "_routes", None) if self.host is not None else None
        if table is not None:
            for method, path, handler in self._registered:
                if table.get(method, {}).get(path) is handler:
                    del table[method][path]
        self._registered.clear()


# ====================================================================================================
# install / uninstall  (same pattern as the group 5 wrapper)
# ====================================================================================================
def install(host: Any, config: Optional[Group34Config] = None) -> None:
    """Wrap host.NEBULAFullNode.__init__ so each node gets a Layer34 as `node.group34`."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g34_orig", None):
        return
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)                      # the original constructor always runs first
        try:
            layer = Layer34(self, config=config, host=host)
            self.group34 = layer
            layer.attach()
        except Exception as e:                   # the node must still start if the layer fails
            self.group34_error = e

    cls._g34_orig = orig
    cls.__init__ = patched


def uninstall(host: Any) -> None:
    """Restore the original constructor. Existing nodes keep their layer until detach() is called.
    If other groups also wrapped __init__ after this one, uninstall them first (LIFO order)."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g34_orig", None)
    if orig:
        cls.__init__ = orig
        del cls._g34_orig
