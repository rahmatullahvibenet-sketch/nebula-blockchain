"""nebula_group41_install.py - wires the 20 group41 classes into a running NEBULA node.

Design rules (same as group 5):
  * nebula_v10_11.py is NEVER edited.  Everything is attached at runtime by install(host)
    and removed again by uninstall(host).
  * The layer NEVER rejects a block or a transaction.  Every callback is wrapped; failures
    are counted in layer.errors and the node keeps running.
  * The original method of every patched host method ALWAYS runs first.
  * Economic classes are REPORT-ONLY for consensus: nothing here moves UTXO funds.
    The layer keeps its own bookkeeping and exposes it through stats() and the REST route.
  * nebula_group41.py stays verbatim.  Input validation and the logic fixes below live in
    the guarded facade methods of Layer41 (see the "Known issues handled" list in
    CHANGES_group41.txt).

Hook map (class -> attach point):
  OptionsMarket, GovernanceTreasuryV2, AIOracle, NFTStakingManager, AirdropManager,
  DeFiStrategy                -> chain listener (on_connect / on_reorg) + facade methods
  PerpetualFuturesMarket,
  ArbitrageStrategy           -> chain listener tick (funding) / utility scan
  ReferralProgram             -> Mempool.submit wrapper + block-connect commit + reorg reverse
  NodeSyncV2                  -> P2PNode._handle_message / peer-disconnect wrapper + checkpoints
  LiquidityMiningProgram      -> NEBULAMiner / StratumV1Server attribute (data only)
  MultiCollateralStablecoin   -> NEBULAWallet attribute + REST route (read-only)
"""
from __future__ import annotations

import functools
import logging
import math
import threading
import time
from collections import OrderedDict, deque
from typing import Any, Callable, Deque, Dict, List, Optional, Tuple

import nebula_group41 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group41")

# --------------------------------------------------------------------------------------
# Static class map (used by the coverage test and by stats()).
# --------------------------------------------------------------------------------------
CLASS_ROLES: Dict[str, str] = {
    "OptionsContract":           "data used by OptionsMarket",
    "OptionsMarket":             "layer.options (chain listener: expiry, reorg)",
    "FuturesPosition":           "data used by PerpetualFuturesMarket",
    "PerpetualFuturesMarket":    "layer.perps (chain listener: funding)",
    "ReferralProgram":           "layer.referrals (Mempool.submit + block commit)",
    "GrantStatus":               "enum used by GovernanceTreasuryV2",
    "GrantProposal":             "data used by GovernanceTreasuryV2",
    "GovernanceTreasuryV2":      "layer.treasury (guarded facade)",
    "AIOracle":                  "layer.ai_oracle (fed every block)",
    "SyncCheckpoint":            "data used by NodeSyncV2",
    "NodeSyncV2":                "layer.sync (P2P wrapper + checkpoint verify)",
    "LiquidityMiningProgram":    "layer.lp_mining (miner attribute, data only)",
    "NFTStakingPool":            "data used by NFTStakingManager",
    "NFTStakingManager":         "layer.nft_staking (guarded facade)",
    "CollateralType":            "data used by MultiCollateralStablecoin",
    "MultiCollateralStablecoin": "layer.stablecoin (wallet attribute + REST)",
    "AirdropCampaign":           "data used by AirdropManager",
    "AirdropManager":            "layer.airdrops (guarded facade)",
    "DeFiStrategy":              "layer.register_strategy base type",
    "ArbitrageStrategy":         "layer.strategies['arbitrage']",
}

ROUTE_PATH = "/api/group41/stats"


# --------------------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------------------
class _Reject(Exception):
    """Validation failure (not an internal error)."""


def _num(value: Any, name: str, *, positive: bool = True) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise _Reject(f"{name} must be a number")
    if not math.isfinite(value):
        raise _Reject(f"{name} must be finite")
    if positive and value <= 0:
        raise _Reject(f"{name} must be > 0")
    if not positive and value < 0:
        raise _Reject(f"{name} must be >= 0")
    return value


def _int(value: Any, name: str, *, positive: bool = True) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise _Reject(f"{name} must be an integer")
    if positive and value <= 0:
        raise _Reject(f"{name} must be > 0")
    if not positive and value < 0:
        raise _Reject(f"{name} must be >= 0")
    return value


def _text(value: Any, name: str, max_len: int = 256) -> str:
    if not isinstance(value, str) or not value.strip():
        raise _Reject(f"{name} must be a non-empty string")
    if len(value) > max_len:
        raise _Reject(f"{name} too long")
    return value


def _pick(obj: Any, names: Tuple[str, ...]) -> Any:
    """Return the first present attribute / dict key from `names` (calls it if callable)."""
    for n in names:
        val = None
        if isinstance(obj, dict):
            val = obj.get(n)
        else:
            val = getattr(obj, n, None)
        if val is None:
            continue
        if callable(val):
            try:
                val = val()
            except Exception:
                continue
        if val is not None:
            return val
    return None


def _facade(fail: Callable[[str], Any]):
    """Guard decorator: validation errors -> fail(msg); internal errors are counted."""
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(self, *a, **k):
            try:
                return fn(self, *a, **k)
            except _Reject as r:
                return fail(str(r))
            except Exception as e:                      # never propagate into the node
                self._record_error(fn.__name__, e)
                return fail("internal error")
        return wrapper
    return deco


_FAIL_BOOL_STR = lambda m: (False, m)        # noqa: E731
_FAIL_BOOL_NUM = lambda m: (False, 0)        # noqa: E731
_FAIL_STR = lambda m: ""                     # noqa: E731
_FAIL_NONE = lambda m: None                  # noqa: E731


class OracleAdapter:
    """Gives the group41 classes the two names they use (price / latest) on top of whatever
    the host oracle really offers.  Invalid values (None, NaN, <= 0) become None, so the
    classes fall back to their own defaults instead of using garbage."""

    PRICE_NAMES = ("price", "latest", "get_price", "latest_price", "get")

    def __init__(self, oracle: Any):
        self._oracle = oracle

    def _read(self, pair: str) -> Optional[float]:
        if self._oracle is None:
            return None
        for name in self.PRICE_NAMES:
            fn = getattr(self._oracle, name, None)
            if not callable(fn):
                continue
            try:
                val = fn(pair)
            except Exception:
                continue
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                continue
            if math.isfinite(val) and val > 0:
                return float(val)
        return None

    def price(self, pair: str) -> Optional[float]:
        return self._read(pair)

    def latest(self, pair: str) -> Optional[float]:
        return self._read(pair)


# --------------------------------------------------------------------------------------
# The layer
# --------------------------------------------------------------------------------------
class Layer41:
    MAX_PENDING_FEES = 10_000
    MAX_COMMITTED_FEES = 5_000
    PENDING_TTL_SECS = 3_600
    MAX_SYNC_PEERS = 1_000
    MAX_ALERTS = 100
    MAX_AIRDROP_ELIGIBLE = 100_000

    def __init__(self, node: Any, oracle: Any = None, dex: Any = None,
                 track_pairs: Tuple[str, ...] = ("NBL/USD",),
                 lp_total_rewards: float = 0.0, lp_duration_blocks: int = 0,
                 nft_owner_check: Optional[Callable[[str, str, int], bool]] = None):
        self.node = node
        self.bc = node.bc
        self.errors = 0
        self.last_error = ""
        self.stats_: Dict[str, int] = {
            "blocks": 0, "reorgs": 0, "fees_pending": 0, "fees_committed": 0,
            "fees_reversed": 0, "fees_skipped": 0, "checkpoint_mismatches": 0,
            "peer_messages": 0, "liquidation_candidates": 0, "options_expired": 0,
        }
        self._lock = threading.RLock()
        self._track_pairs = tuple(track_pairs)
        self._nft_owner_check = nft_owner_check
        self._dex = dex

        oracle = oracle if oracle is not None else (
            getattr(node, "oracle", None) or getattr(self.bc, "oracle", None))
        self.oracle = OracleAdapter(oracle)

        # ---- the services -------------------------------------------------------------
        self.options = g.OptionsMarket(self.bc, self.oracle)
        self.perps = g.PerpetualFuturesMarket(self.bc, self.oracle)
        self.referrals = g.ReferralProgram(self.bc)
        self.treasury = g.GovernanceTreasuryV2(self.bc)
        self.ai_oracle = g.AIOracle(self.oracle)
        self.sync = g.NodeSyncV2(self.bc)
        self.nft_staking = g.NFTStakingManager(self.bc)
        self.stablecoin = g.MultiCollateralStablecoin(self.bc, self.oracle)
        self.airdrops = g.AirdropManager(self.bc)
        self.strategies: Dict[str, g.DeFiStrategy] = {}
        self.register_strategy("arbitrage", g.ArbitrageStrategy())

        self.lp_mining: Optional[g.LiquidityMiningProgram] = None
        if lp_total_rewards and lp_duration_blocks:
            self.start_lp_program(lp_total_rewards, lp_duration_blocks)

        # ---- bookkeeping ----------------------------------------------------------------
        self._expired_by_tick: set = set()
        self._pending_fees: "OrderedDict[str, Tuple[str, int, float]]" = OrderedDict()
        self._committed_fees: "OrderedDict[str, Tuple[int, str, int]]" = OrderedDict()
        self._released_milestones: set = set()
        self.checkpoint_alerts: Deque[str] = deque(maxlen=self.MAX_ALERTS)

    # ------------------------------------------------------------------ error accounting
    def _record_error(self, where: str, exc: BaseException) -> None:
        self.errors += 1
        self.last_error = f"{where}: {type(exc).__name__}: {exc}"
        log.warning("group41 %s", self.last_error)

    def _safe(self, where: str, fn: Callable, *a, **k):
        try:
            return fn(*a, **k)
        except Exception as e:
            self._record_error(where, e)
            return None

    # ================================================================== chain listener
    def on_connect(self, block: Any) -> None:
        try:
            with self._lock:
                self.stats_["blocks"] += 1
                height = _pick(block, ("height",))
                height = height if isinstance(height, int) else self.bc.height
                self._safe("options.expire", self._tick_options)
                self._safe("perps.funding", self.perps.process_funding)
                self._safe("stablecoin.scan", self._scan_liquidations)
                self._safe("ai_oracle.feed", self._feed_ai_oracle)
                self._safe("fees.commit", self._commit_block_fees, block, height)
                self._safe("sync.verify", self._verify_checkpoint, height)
        except Exception as e:                               # absolute last line of defence
            self._record_error("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        try:
            with self._lock:
                self.stats_["reorgs"] += 1
                self._safe("reorg.options", self._reorg_options, ancestor_height)
                self._safe("reorg.perps", self._reorg_perps, ancestor_height)
                self._safe("reorg.fees", self._reorg_fees, ancestor_height)
        except Exception as e:
            self._record_error("on_reorg", e)

    def detach(self) -> None:
        try:
            self.node.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer41.detach", exc_info=True)

    # ---- per-block work -------------------------------------------------------------
    def _tick_options(self) -> None:
        opts = self.options
        with opts._lock:
            before = {cid for cid, o in opts._contracts.items() if not o.expired and not o.exercised}
            n = opts.expire_contracts()
            after = {cid for cid in before if opts._contracts[cid].expired}
        self._expired_by_tick |= after
        self.stats_["options_expired"] += n

    def _scan_liquidations(self) -> None:
        """READ-ONLY liquidation scan.  MultiCollateralStablecoin.check_all_liquidations()
        zeroes the debt without seizing collateral, so it is never called automatically."""
        sc = self.stablecoin
        count = 0
        with sc._lock:
            for v in sc._vaults.values():
                debt = v.get("debt", 0)
                if not debt or debt <= 0:
                    continue
                spec = g.CollateralType.TYPES.get(v.get("collateral_type"), {})
                price = self.oracle.price(spec.get("oracle", "NBL/USD")) or 0.01
                if v["collateral"] * price / debt < sc.LIQ_RATIO:
                    count += 1
        self.stats_["liquidation_candidates"] = count

    def _feed_ai_oracle(self) -> None:
        for pair in self._track_pairs:
            price = self.oracle.latest(pair)
            if price is not None:
                self.ai_oracle.record_price(pair, price)

    def _verify_checkpoint(self, height: int) -> None:
        if height not in self.sync._checkpoints:
            return
        ok, msg = self.sync.verify_at_height(height)
        if not ok:                                           # report-only, never reject
            self.stats_["checkpoint_mismatches"] += 1
            self.checkpoint_alerts.append(msg)
            log.error("group41 checkpoint alert: %s", msg)

    # ---- fees: mempool accept -> pending, block connect -> commit, reorg -> reverse ---
    def note_submitted(self, tx: Any, accepted: bool) -> None:
        if not accepted:
            return
        try:
            txid = _pick(tx, ("txid", "tx_id", "hash", "id"))
            payer = _pick(tx, ("sender", "from_addr", "from_address", "from", "payer"))
            fee = _pick(tx, ("fee", "fees"))
            if (txid is None or not isinstance(payer, str)
                    or isinstance(fee, bool) or not isinstance(fee, int) or fee < 0):
                self.stats_["fees_skipped"] += 1
                return
            with self._lock:
                txid = str(txid)
                if txid in self._pending_fees or txid in self._committed_fees:
                    return
                self._pending_fees[txid] = (payer, fee, time.time())
                while len(self._pending_fees) > self.MAX_PENDING_FEES:
                    self._pending_fees.popitem(last=False)
                self.stats_["fees_pending"] = len(self._pending_fees)
        except Exception as e:
            self._record_error("note_submitted", e)

    def _commit_block_fees(self, block: Any, height: int) -> None:
        now = time.time()
        for txid in [t for t, (_, _, ts) in self._pending_fees.items()
                     if now - ts > self.PENDING_TTL_SECS]:
            del self._pending_fees[txid]
        txs = _pick(block, ("transactions", "txs", "tx")) or []
        for tx in txs:
            txid = _pick(tx, ("txid", "tx_id", "hash", "id"))
            if txid is None:
                continue
            entry = self._pending_fees.pop(str(txid), None)
            if entry is None:
                continue
            payer, fee, _ = entry
            self.referrals.record_fee(payer, fee)
            self._committed_fees[str(txid)] = (height, payer, fee)
            while len(self._committed_fees) > self.MAX_COMMITTED_FEES:
                self._committed_fees.popitem(last=False)
            self.stats_["fees_committed"] += 1
        self.stats_["fees_pending"] = len(self._pending_fees)

    def _reverse_fee(self, payer: str, fee: int) -> None:
        """Exact inverse of ReferralProgram.record_fee (clamped at zero if already claimed)."""
        rp = self.referrals
        with rp._lock:
            referrer, depth, rate = rp._referrals.get(payer), 0, rp.REFERRAL_PCT
            while referrer and depth < rp.MAX_DEPTH:
                commission = int(fee * rate)
                rp._earnings[referrer] = max(0, rp._earnings.get(referrer, 0) - commission)
                referrer = rp._referrals.get(referrer)
                depth += 1
                rate *= 0.5

    def _reorg_fees(self, ancestor_height: int) -> None:
        for txid, (h, payer, fee) in list(self._committed_fees.items()):
            if h > ancestor_height:
                self._reverse_fee(payer, fee)
                del self._committed_fees[txid]
                self._pending_fees[txid] = (payer, fee, time.time())   # may re-confirm
                self.stats_["fees_reversed"] += 1
        self.stats_["fees_pending"] = len(self._pending_fees)

    def _reorg_options(self, ancestor_height: int) -> None:
        opts = self.options
        with opts._lock:
            for cid in list(self._expired_by_tick):
                o = opts._contracts.get(cid)
                if o is None or o.exercised:
                    self._expired_by_tick.discard(cid)
                elif o.expiry_block > ancestor_height:
                    o.expired = False                 # the next connected block re-evaluates it
                    self._expired_by_tick.discard(cid)

    def _reorg_perps(self, ancestor_height: int) -> None:
        with self.perps._lock:
            self.perps._last_funding_block = min(self.perps._last_funding_block, ancestor_height)

    # ================================================================== network hooks
    @staticmethod
    def _peer_id(peer: Any) -> Optional[str]:
        val = peer if isinstance(peer, str) else _pick(peer, ("addr", "address", "peer_id", "id", "host"))
        return str(val) if val is not None else None

    def on_peer_message(self, peer: Any, msg: Any = None) -> None:
        try:
            pid = self._peer_id(peer)
            with self._lock:
                self.stats_["peer_messages"] += 1
                if pid and pid not in self.sync._sync_peers:
                    if len(self.sync._sync_peers) >= self.MAX_SYNC_PEERS:
                        self.sync._sync_peers.pop(0)
                    self.sync._sync_peers.append(pid)
        except Exception as e:
            self._record_error("on_peer_message", e)

    def on_peer_gone(self, peer: Any) -> None:
        try:
            pid = self._peer_id(peer)
            with self._lock:
                if pid in self.sync._sync_peers:
                    self.sync._sync_peers.remove(pid)
        except Exception as e:
            self._record_error("on_peer_gone", e)

    # ================================================================== guarded facade
    # ---- options ---------------------------------------------------------------------
    @_facade(_FAIL_BOOL_STR)
    def write_option(self, writer: str, underlying: str, option_type: Any, strike: float,
                     expiry_days: int, premium: float, size: float) -> Tuple[bool, str]:
        _text(writer, "writer"); _text(underlying, "underlying")
        if not isinstance(option_type, g.OptionType):
            raise _Reject("option_type must be an OptionType")
        _num(strike, "strike"); _int(expiry_days, "expiry_days"); _num(premium, "premium", positive=False)
        _num(size, "size")
        return self.options.write_option(writer, underlying, option_type, strike, expiry_days, premium, size)

    @_facade(_FAIL_BOOL_STR)
    def buy_option(self, buyer: str, contract_id: str) -> Tuple[bool, str]:
        _text(buyer, "buyer"); _text(contract_id, "contract_id")
        opt = self.options._contracts.get(contract_id)
        if opt is not None and opt.writer == buyer:
            raise _Reject("writer cannot buy own option")
        return self.options.buy_option(buyer, contract_id)

    @_facade(_FAIL_BOOL_NUM)
    def exercise_option(self, buyer: str, contract_id: str) -> Tuple[bool, float]:
        _text(buyer, "buyer"); _text(contract_id, "contract_id")
        return self.options.exercise(buyer, contract_id)

    # ---- perpetual futures -------------------------------------------------------------
    @_facade(_FAIL_BOOL_STR)
    def open_position(self, trader: str, pair: str, side: str, size: float,
                      leverage: float, collateral_nbl: float) -> Tuple[bool, str]:
        _text(trader, "trader"); _text(pair, "pair")
        if side not in ("long", "short"):
            raise _Reject("side must be 'long' or 'short'")
        _num(size, "size"); _num(leverage, "leverage"); _num(collateral_nbl, "collateral_nbl")
        return self.perps.open(trader, pair, side, size, leverage, collateral_nbl)

    @_facade(_FAIL_BOOL_NUM)
    def close_position(self, pos_id: str, trader: str) -> Tuple[bool, float]:
        _text(pos_id, "pos_id"); _text(trader, "trader")
        return self.perps.close(pos_id, trader)

    # ---- referrals ---------------------------------------------------------------------
    @_facade(_FAIL_BOOL_STR)
    def register_referral(self, referee: str, referrer: str) -> Tuple[bool, str]:
        _text(referee, "referee"); _text(referrer, "referrer")
        with self.referrals._lock:
            cur, hops = referrer, 0
            while cur is not None and hops <= 64:          # refuse referral cycles
                if cur == referee:
                    raise _Reject("referral cycle")
                cur = self.referrals._referrals.get(cur)
                hops += 1
        return self.referrals.register(referee, referrer)

    # ---- treasury ----------------------------------------------------------------------
    @_facade(_FAIL_BOOL_STR)
    def submit_grant(self, applicant: str, title: str, description: str, amount_nbl: float,
                     category: str, milestones: List[dict]) -> Tuple[bool, str]:
        _text(applicant, "applicant"); _text(title, "title"); _text(description, "description", 4096)
        _num(amount_nbl, "amount_nbl")
        if not isinstance(milestones, list) or not milestones or len(milestones) > 50:
            raise _Reject("milestones must be a list of 1..50 items")
        total = 0.0
        for ms in milestones:
            if not isinstance(ms, dict):
                raise _Reject("each milestone must be a dict")
            total += _num(ms.get("amount"), "milestone amount")
        if total > amount_nbl + 1e-9:
            raise _Reject("milestones exceed grant amount")
        return self.treasury.submit_grant(applicant, title, description, amount_nbl, category, milestones)

    @_facade(_FAIL_BOOL_STR)
    def vote_grant(self, voter: str, grant_id: str, support: bool) -> Tuple[bool, str]:
        _text(voter, "voter"); _text(grant_id, "grant_id")
        if not isinstance(support, bool):
            raise _Reject("support must be bool")
        return self.treasury.vote_on_grant(voter, grant_id, support)

    @_facade(_FAIL_BOOL_STR)
    def finalize_grant(self, grant_id: str) -> Tuple[bool, str]:
        """Only a grant that is still in the voting phase can be finalised (the raw class
        would flip COMPLETED/REJECTED grants back to APPROVED on a repeat call)."""
        _text(grant_id, "grant_id")
        grant = self.treasury._grants.get(grant_id)
        if grant is not None and grant.status != g.GrantStatus.PROPOSED:
            raise _Reject("grant is not in voting phase")
        return self.treasury.finalize_vote(grant_id)

    @_facade(_FAIL_BOOL_NUM)
    def release_milestone(self, grant_id: str, milestone_idx: int) -> Tuple[bool, float]:
        """Fixes two raw-class bugs: a second milestone could never be paid (status became
        MILESTONED and release required APPROVED) and the same milestone could be re-paid."""
        _text(grant_id, "grant_id"); _int(milestone_idx, "milestone_idx", positive=False)
        key = (grant_id, milestone_idx)
        with self.treasury._lock:
            grant = self.treasury._grants.get(grant_id)
            if grant is None or key in self._released_milestones:
                return False, 0
            if grant.status not in (g.GrantStatus.APPROVED, g.GrantStatus.MILESTONED):
                return False, 0
            if milestone_idx >= len(grant.milestones):
                return False, 0
            amount = float(grant.milestones[milestone_idx].get("amount", 0))
            if grant.paid + amount > grant.amount_nbl + 1e-9:
                return False, 0
            previous = grant.status
            grant.status = g.GrantStatus.APPROVED          # temporary, restored below
            try:
                ok, paid = self.treasury.release_milestone(grant_id, milestone_idx)
            finally:
                if grant.status == g.GrantStatus.APPROVED:
                    grant.status = previous               # call refused: restore
            if ok:
                self._released_milestones.add(key)
            return ok, paid

    # ---- liquidity mining -------------------------------------------------------------
    @_facade(_FAIL_BOOL_STR)
    def start_lp_program(self, total_rewards: float, duration_blocks: int) -> Tuple[bool, str]:
        if self.lp_mining is not None:
            raise _Reject("LP program already running")
        _num(total_rewards, "total_rewards"); _int(duration_blocks, "duration_blocks")
        self.lp_mining = g.LiquidityMiningProgram(self.bc, total_rewards, duration_blocks)
        return True, "LP program started"

    def _lp(self) -> g.LiquidityMiningProgram:
        if self.lp_mining is None:
            raise _Reject("no LP program")
        return self.lp_mining

    @_facade(_FAIL_BOOL_STR)
    def stake_lp(self, address: str, lp_amount: int) -> Tuple[bool, str]:
        """Settles pending rewards BEFORE adding stake (the raw class resets the claim
        block on every stake and silently loses the pending reward)."""
        _text(address, "address"); _int(lp_amount, "lp_amount")
        lp = self._lp()
        lp._claim_pending(address)
        return lp.stake_lp(address, lp_amount)

    @_facade(_FAIL_BOOL_STR)
    def unstake_lp(self, address: str, lp_amount: int) -> Tuple[bool, str]:
        _text(address, "address"); _int(lp_amount, "lp_amount")
        return self._lp().unstake_lp(address, lp_amount)

    @_facade(_FAIL_BOOL_NUM)
    def claim_lp_rewards(self, address: str) -> Tuple[bool, int]:
        _text(address, "address")
        return self._lp().claim_rewards(address)

    # ---- NFT staking --------------------------------------------------------------------
    @_facade(_FAIL_STR)
    def create_nft_pool(self, collection_id: str, reward_per_block: float) -> str:
        _text(collection_id, "collection_id"); _num(reward_per_block, "reward_per_block")
        return self.nft_staking.create_pool(collection_id, reward_per_block)

    @_facade(_FAIL_BOOL_STR)
    def stake_nft(self, pool_id: str, owner: str, token_id: int) -> Tuple[bool, str]:
        _text(pool_id, "pool_id"); _text(owner, "owner"); _int(token_id, "token_id", positive=False)
        with self.nft_staking._lock:
            pool = self.nft_staking._pools.get(pool_id)
            if pool is None:
                raise _Reject("Pool not found")
            if any(tid == token_id for lst in pool._staked.values() for tid, _ in lst):
                raise _Reject("token already staked")
            if self._nft_owner_check is not None and not self._nft_owner_check(
                    owner, pool.collection_id, token_id):
                raise _Reject("owner check failed")
        return self.nft_staking.stake(pool_id, owner, token_id)

    @_facade(_FAIL_BOOL_NUM)
    def unstake_nft(self, pool_id: str, owner: str, token_id: int) -> Tuple[bool, int]:
        _text(pool_id, "pool_id"); _text(owner, "owner"); _int(token_id, "token_id", positive=False)
        return self.nft_staking.unstake(pool_id, owner, token_id)

    # ---- stablecoin --------------------------------------------------------------------
    @_facade(_FAIL_BOOL_STR)
    def open_vault(self, owner: str, collateral_type: str, collateral_amount: float) -> Tuple[bool, str]:
        _text(owner, "owner"); _text(collateral_type, "collateral_type"); _num(collateral_amount, "collateral_amount")
        return self.stablecoin.open_vault(owner, collateral_type, collateral_amount)

    @_facade(_FAIL_BOOL_STR)
    def mint_nbusd(self, vault_id: str, amount: float) -> Tuple[bool, str]:
        _text(vault_id, "vault_id"); _num(amount, "amount")
        return self.stablecoin.mint(vault_id, amount)

    @_facade(_FAIL_BOOL_STR)
    def repay_nbusd(self, vault_id: str, amount: float) -> Tuple[bool, str]:
        _text(vault_id, "vault_id"); _num(amount, "amount")
        return self.stablecoin.repay(vault_id, amount)

    def liquidation_candidates(self) -> List[str]:
        """Vault ids below the liquidation ratio (read-only, nothing is changed)."""
        out: List[str] = []
        try:
            sc = self.stablecoin
            with sc._lock:
                for vid, v in sc._vaults.items():
                    if v.get("debt", 0) > 0:
                        spec = g.CollateralType.TYPES.get(v["collateral_type"], {})
                        price = self.oracle.price(spec.get("oracle", "NBL/USD")) or 0.01
                        if v["collateral"] * price / v["debt"] < sc.LIQ_RATIO:
                            out.append(vid)
        except Exception as e:
            self._record_error("liquidation_candidates", e)
        return out

    # ---- airdrops ----------------------------------------------------------------------
    @_facade(_FAIL_STR)
    def create_airdrop(self, creator: str, token: str, total_nbl: float,
                       eligible: List[str], per_address_nbl: float) -> str:
        _text(creator, "creator"); _text(token, "token"); _num(total_nbl, "total_nbl")
        _num(per_address_nbl, "per_address_nbl")
        if per_address_nbl > total_nbl:
            raise _Reject("per_address_nbl exceeds total")
        if (not isinstance(eligible, list) or not eligible
                or len(eligible) > self.MAX_AIRDROP_ELIGIBLE
                or not all(isinstance(a, str) and a for a in eligible)):
            raise _Reject("invalid eligible list")
        needed = int(total_nbl * 10 ** g.DECIMALS)
        if self.bc.utxo.balance(creator) < needed:
            raise _Reject("creator balance too low")
        return self.airdrops.create_campaign(creator, token, total_nbl, eligible, per_address_nbl)

    @_facade(_FAIL_BOOL_NUM)
    def claim_airdrop(self, campaign_id: str, address: str) -> Tuple[bool, int]:
        _text(campaign_id, "campaign_id"); _text(address, "address")
        return self.airdrops.claim(campaign_id, address)

    # ---- strategies --------------------------------------------------------------------
    @_facade(_FAIL_BOOL_STR)
    def register_strategy(self, key: str, strategy: Any) -> Tuple[bool, str]:
        _text(key, "key")
        if not isinstance(strategy, g.DeFiStrategy):
            raise _Reject("strategy must derive from DeFiStrategy")
        self.strategies[key] = strategy
        return True, "registered"

    @_facade(_FAIL_NONE)
    def scan_arbitrage(self, pair: str, dex: Any = None) -> Optional[dict]:
        _text(pair, "pair")
        dex = dex or self._dex or getattr(self.node, "dex", None)
        if dex is None:
            raise _Reject("no DEX available")
        return self.strategies["arbitrage"].find_opportunity(dex, pair)

    @_facade(_FAIL_NONE)
    def run_strategy(self, key: str, *a, **k) -> Optional[dict]:
        strategy = self.strategies.get(key)
        if strategy is None or not strategy.active:
            raise _Reject("unknown or inactive strategy")
        try:
            result = strategy.execute(*a, **k)
        except NotImplementedError:
            raise _Reject("strategy has no execute()")     # ArbitrageStrategy: scan only
        strategy.executions += 1
        return result

    # ---- sync checkpoints --------------------------------------------------------------
    @_facade(_FAIL_BOOL_STR)
    def add_checkpoint(self, height: int, hash_: str, utxo_hash: str) -> Tuple[bool, str]:
        _int(height, "height", positive=False); _text(hash_, "hash_", 128); _text(utxo_hash, "utxo_hash", 128)
        self.sync.add_checkpoint(height, hash_, utxo_hash)
        return True, "checkpoint added"

    # ================================================================== reporting
    def stats(self) -> dict:
        out: Dict[str, Any] = {
            "errors": self.errors, "last_error": self.last_error, "layer": dict(self.stats_),
            "options": self._safe("stats.options", self.options.options_stats),
            "futures": self._safe("stats.futures", self.perps.futures_stats),
            "referrals": self._safe("stats.referrals", self.referrals.stats),
            "treasury": self._safe("stats.treasury", self.treasury.treasury_v2_stats),
            "ai_oracle": self._safe("stats.ai", self.ai_oracle.price_prediction_summary),
            "sync": self._safe("stats.sync", self.sync.sync_status),
            "nft_pools": self._safe("stats.nft", self.nft_staking.all_pools),
            "stablecoin": self._safe("stats.stablecoin", self.stablecoin.stablecoin_stats),
            "airdrops": self._safe("stats.airdrops", self.airdrops.airdrop_stats),
            "strategies": {k: {"active": s.active, "executions": s.executions}
                           for k, s in self.strategies.items()},
            "checkpoint_alerts": list(self.checkpoint_alerts),
        }
        if self.lp_mining is not None:
            out["lp_mining"] = self._safe("stats.lp", self.lp_mining.program_stats)
        return out


# --------------------------------------------------------------------------------------
# install / uninstall
# --------------------------------------------------------------------------------------
_ATTACH_NAMES = {
    "mempool": ("mempool",),
    "p2p":     ("p2p", "network", "p2p_node", "net"),
    "miner":   ("miner", "stratum", "stratum_server"),
    "wallet":  ("wallet",),
}
_DISCONNECT_NAMES = ("_on_disconnect", "remove_peer", "_remove_peer", "disconnect_peer", "_handle_disconnect")
_ACTIVE: Dict[str, Optional[Layer41]] = {"layer": None}
_ALL_LAYERS: List[Layer41] = []              # every layer created by install(), for clean uninstall


def _find(node: Any, key: str) -> Any:
    for name in _ATTACH_NAMES[key]:
        obj = getattr(node, name, None)
        if obj is None and key == "mempool":
            obj = getattr(getattr(node, "bc", None), "mempool", None)
        if obj is not None:
            return obj
    return None


def _tag(obj: Any, layer: Optional[Layer41]) -> None:
    if obj is None:
        return
    try:
        if layer is None:
            if hasattr(obj, "group41_layer"):
                delattr(obj, "group41_layer")
        else:
            obj.group41_layer = layer
    except Exception:
        _NB_SWALLOW_LOG.debug("swallowed Exception in _tag", exc_info=True)                                    # __slots__ objects: that hook is simply skipped


def _wrap_method(cls: Any, name: str, after: Callable[[Any, tuple, dict, Any], None]) -> None:
    orig = getattr(cls, name, None)
    if orig is None or getattr(orig, "_g41_wrapped", False):
        return

    @functools.wraps(orig)
    def patched(self, *a, **k):
        result = orig(self, *a, **k)                 # the original ALWAYS runs first
        layer = getattr(self, "group41_layer", None)
        if layer is not None:
            try:
                after(layer, a, k, result)
            except Exception as e:
                layer._record_error(f"{cls.__name__}.{name}", e)
        return result

    patched._g41_wrapped = True
    patched._g41_orig = orig
    setattr(cls, name, patched)


def _unwrap_method(cls: Any, name: str) -> None:
    cur = getattr(cls, name, None)
    if cur is not None and getattr(cur, "_g41_wrapped", False):
        setattr(cls, name, cur._g41_orig)


def _route_handler(path, query, body):
    layer = _ACTIVE["layer"]
    if layer is None:
        return 503, {"success": False, "error": "group41 not installed"}
    return 200, {"success": True, "data": layer.stats()}


def install(host: Any, **layer_kwargs: Any) -> None:
    """Attach the layer to host.NEBULAFullNode (idempotent)."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g41_orig", None):
        return
    orig_init = cls.__init__

    @functools.wraps(orig_init)
    def patched(self, *a, **k):
        orig_init(self, *a, **k)
        try:
            layer = Layer41(self, **layer_kwargs)
            self.group41 = layer
            self.bc.add_listener(layer)
            _ACTIVE["layer"] = layer
            _ALL_LAYERS.append(layer)
            for key in ("mempool", "p2p", "miner", "wallet"):
                _tag(_find(self, key), layer)
        except Exception as e:                       # the node must start regardless
            self.group41_error = e
            log.error("group41 install failed: %s", e)

    cls._g41_orig = orig_init
    cls.__init__ = patched

    if hasattr(host, "Mempool"):
        _wrap_method(host.Mempool, "submit", lambda layer, a, k, res: layer.note_submitted(
            a[0] if a else k.get("tx"),
            bool(res[0]) if isinstance(res, tuple) and res else bool(res)))
    if hasattr(host, "P2PNode"):
        _wrap_method(host.P2PNode, "_handle_message", lambda layer, a, k, res: layer.on_peer_message(
            a[0] if a else k.get("peer"), a[1] if len(a) > 1 else k.get("msg")))
        for name in _DISCONNECT_NAMES:
            _wrap_method(host.P2PNode, name, lambda layer, a, k, res: layer.on_peer_gone(
                a[0] if a else None))
    routes = getattr(host, "_routes", None)
    if isinstance(routes, dict):
        routes.setdefault("GET", {})[ROUTE_PATH] = _route_handler


def uninstall(host: Any) -> None:
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g41_orig", None)
    if not orig:
        return
    cls.__init__ = orig
    del cls._g41_orig
    if hasattr(host, "Mempool"):
        _unwrap_method(host.Mempool, "submit")
    if hasattr(host, "P2PNode"):
        for name in ("_handle_message",) + _DISCONNECT_NAMES:
            _unwrap_method(host.P2PNode, name)
    routes = getattr(host, "_routes", None)
    if isinstance(routes, dict):
        routes.get("GET", {}).pop(ROUTE_PATH, None)
    for layer in _ALL_LAYERS:
        layer.detach()
        for key in ("mempool", "p2p", "miner", "wallet"):
            _tag(_find(layer.node, key), None)
    _ALL_LAYERS.clear()
    _ACTIVE["layer"] = None
