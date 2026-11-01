"""nebula_group62_install.py

Wires the 20 formerly-dead classes of nebula_group62.py into the NEBULA host
WITHOUT editing nebula_v10_11.py.

Design rules (from nebula_group62_guide.txt):
  * Report-only: the layer observes and counts; it never rejects a block,
    a transaction, a message or a peer.
  * Every callback / wrapper runs inside try/except. Failures only bump
    `layer.errors` and are kept in `layer.last_errors`.
  * The original host method ALWAYS runs first; its result is returned
    unchanged.
  * install(host) / uninstall(host) are idempotent and fully reversible.
  * Nothing here calls NetworkConfig.apply() (it patches host globals).

Usage:
    import nebula_v10_11 as host
    import nebula_group62_install as g62
    g62.install(host)            # before the node is created
    node = host.NEBULAFullNode(...)
    node.group62.report()        # observe stats
    g62.uninstall(host)          # back to the original behaviour
"""
from __future__ import annotations

import threading
import time
from collections import deque
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group62 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

# --------------------------------------------------------------------------
# Tunables (all observation-only)
# --------------------------------------------------------------------------
MSG_WINDOW_SECONDS = 10          # sliding window for per-peer message rate
MSG_RATE_FLAG = 200              # messages per window -> flagged as spam
MAX_TRACKED_PEERS = 2048         # cap for per-peer tables (RAM safety)
MAX_ERROR_LOG = 50               # cap for layer.last_errors
MAX_CHANNELS = 10_000            # cap for micro-channel registry
MAX_WC_SESSIONS = 1_000          # cap for WalletConnect sessions
MAX_BIP9_PERIODS = 256           # cap for Bip9PeriodCache entries

# Layers currently installed; class-level wrappers fan out to these.
_ACTIVE: List["Layer62"] = []
_ACTIVE_LOCK = threading.Lock()


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------
def _peer_key(peer: Any) -> str:
    """Best-effort stable identifier of a peer object (never raises)."""
    try:
        for attr in ("ip", "host", "addr", "address"):
            v = getattr(peer, attr, None)
            if v:
                if isinstance(v, tuple):
                    v = v[0]
                return str(v)
        if isinstance(peer, (tuple, list)) and peer:
            return str(peer[0])
        return str(peer)
    except Exception:
        return "unknown"


def _block_height(block: Any, fallback: int = 0) -> int:
    try:
        h = getattr(block, "height", None)
        if h is None and isinstance(block, dict):
            h = block.get("height")
        return int(h) if h is not None else fallback
    except Exception:
        return fallback


# --------------------------------------------------------------------------
# The layer
# --------------------------------------------------------------------------
class Layer62:
    """Holds every group62 service for one node."""

    def __init__(self, node: Any):
        self.node = node
        self.errors = 0
        self.last_errors: deque = deque(maxlen=MAX_ERROR_LOG)
        self.stats: Dict[str, int] = {
            "blocks_connected": 0, "reorgs": 0,
            "p2p_messages": 0, "p2p_flagged_peers": 0,
            "mempool_submits": 0, "mempool_accepted": 0,
            "staking_accruals": 0,
        }
        self._lock = threading.RLock()
        self._last_height = self._safe_height()

        # ---- 1. chain / network -------------------------------------------
        self.network_name = str(getattr(node, "network", None)
                                or getattr(getattr(node, "config", None),
                                           "network", None) or "mainnet")
        self.net_config = self._guard(lambda: g.NetworkConfig(self.network_name))
        # NetworkParams is a plain dataclass used by NetworkConfig; exposed
        # for callers that want to build custom network descriptions.
        self.NetworkParams = g.NetworkParams

        # ---- 2. BIP9 period cache (data holder, filled by callers/tests) ---
        self.bip9_periods: Dict[int, Any] = {}

        # ---- 3. P2P peer scoring (observe-only) ----------------------------
        self.peer_scores: Dict[str, Any] = {}
        self._peer_msgs: Dict[str, deque] = {}

        # ---- 4. wallet side utilities -------------------------------------
        self.miniscript_policy = g.MiniscriptPolicy()
        self.miniscript_compiler = g.MiniscriptCompiler()
        self.sp_wallet = self._guard(g.SilentPaymentWallet)   # BIP352
        self.sp_scan_extractor: Optional[Callable] = None     # opt-in, see below
        self.wc_sessions: Dict[str, Any] = {}

        # ---- 5. staking / coin selection / channels -----------------------
        self.staking_pools: Dict[Any, Any] = {}
        self.coin_selector = self._guard(
            lambda: g.BatchCoinSelector(getattr(node, "bc", None)))
        self.channels: Dict[str, Any] = {}

    # ------------------------------------------------------------------ core
    def _safe_height(self) -> int:
        try:
            return int(getattr(getattr(self.node, "bc", None), "height", 0) or 0)
        except Exception:
            return 0

    def _fail(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.last_errors.append((time.time(), where, repr(exc)))

    def _guard(self, fn: Callable, default: Any = None) -> Any:
        try:
            return fn()
        except Exception as e:      # construction failures must not stop the node
            self._fail(getattr(fn, "__name__", "guard"), e)
            return default

    # --------------------------------------------------- chain listener API
    def on_connect(self, block: Any) -> None:
        try:
            h = _block_height(block, self._safe_height())
            with self._lock:
                self.stats["blocks_connected"] += 1
                last, self._last_height = self._last_height, h
            # Staking rewards accrue in memory only (no consensus effect).
            if h > last:
                for pool in list(self.staking_pools.values()):
                    try:
                        pool.accrue_rewards(h, last)
                        self.stats["staking_accruals"] += 1
                    except Exception as e:
                        self._fail("staking.accrue", e)
            self._maybe_scan_silent_payments(block)
        except Exception as e:
            self._fail("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        try:
            with self._lock:
                self.stats["reorgs"] += 1
                # Staking accrual is monotonic and in-memory; after a reorg
                # we only rewind the height marker so no block is counted
                # twice when the new branch is connected.
                self._last_height = int(ancestor_height)
        except Exception as e:
            self._fail("on_reorg", e)

    def detach(self) -> None:
        try:
            self.node.bc._listeners.remove(self)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer62.detach", exc_info=True)

    # ------------------------------------------------- P2P (observe-only)
    def observe_message(self, peer: Any, msg: Any) -> None:
        """Called after the original _handle_message ran."""
        try:
            key = _peer_key(peer)
            now = time.time()
            with self._lock:
                self.stats["p2p_messages"] += 1
                if key not in self.peer_scores:
                    if len(self.peer_scores) >= MAX_TRACKED_PEERS:
                        self._evict_oldest_peer()
                    self.peer_scores[key] = g.PeerScoreEntry(ip=key)
                    self._peer_msgs[key] = deque()
                q = self._peer_msgs[key]
                q.append(now)
                while q and now - q[0] > MSG_WINDOW_SECONDS:
                    q.popleft()
                if len(q) == MSG_RATE_FLAG:          # flag once per burst
                    self.peer_scores[key].add(
                        g.Misbehavior.GETDATA_SPAM.value, "msg-rate (observed)")
                    self.stats["p2p_flagged_peers"] += 1
        except Exception as e:
            self._fail("observe_message", e)

    def _evict_oldest_peer(self) -> None:
        oldest = min(self.peer_scores,
                     key=lambda k: self.peer_scores[k].last_updated)
        self.peer_scores.pop(oldest, None)
        self._peer_msgs.pop(oldest, None)

    def report_misbehavior(self, peer: Any, kind: "g.Misbehavior",
                           note: str = "") -> int:
        """Record (never enforce) a misbehavior event. Returns the new score."""
        try:
            key = _peer_key(peer)
            with self._lock:
                e = self.peer_scores.setdefault(key, g.PeerScoreEntry(ip=key))
                e.decay()
                e.add(kind.value, f"{kind.name} {note}".strip())
                return e.score
        except Exception as ex:
            self._fail("report_misbehavior", ex)
            return 0

    def would_ban(self, peer: Any) -> bool:
        """Advisory only: would this peer be banned by the score table?"""
        e = self.peer_scores.get(_peer_key(peer))
        return bool(e and e.is_banned)

    # ------------------------------------------------ Mempool (count-only)
    def observe_submit(self, tx: Any, result: Any) -> None:
        try:
            with self._lock:
                self.stats["mempool_submits"] += 1
                if isinstance(result, tuple) and result and result[0]:
                    self.stats["mempool_accepted"] += 1
        except Exception as e:
            self._fail("observe_submit", e)

    # ------------------------------------------------ payment URI / QR
    def payment_uri(self, address: str, amount: Optional[float] = None,
                    label: str = "", message: str = "") -> str:
        kw: Dict[str, Any] = {}
        if amount is not None:
            kw["amount"] = amount
        if label:
            kw["label"] = label
        if message:
            kw["message"] = message
        return g.Bip21URI(address, **kw).to_uri()

    def parse_payment_uri(self, uri: str) -> "g.Bip21URI":
        return g.Bip21URI.parse(uri)

    def validate_payment_uri(self, uri: str) -> tuple:
        return g.Bip21URI.validate(uri)

    def qr_for(self, data: str) -> "g._QRCode":
        return g._QRCode(data)

    def qr_for_address(self, address: str, **kw) -> "g._QRCode":
        return g._QRCode(self.payment_uri(address, **kw))

    # ------------------------------------------------- Miniscript helpers
    def compile_policy(self, node_: "g.MiniscriptNode") -> Dict[str, Any]:
        """Compile a Miniscript node into script bytes + analysis."""
        try:
            return {
                "ok": True,
                "script_hex": self.miniscript_compiler.compile(node_).hex(),
                "analysis": self.miniscript_compiler.analyze(node_),
            }
        except g.MiniscriptError as e:
            return {"ok": False, "error": str(e)}
        except Exception as e:
            self._fail("compile_policy", e)
            return {"ok": False, "error": repr(e)}

    # ------------------------------------------------- Silent payments
    def enable_silent_payment_scanning(self, extractor: Callable) -> None:
        """Opt-in. `extractor(block)` must yield tuples
        (input_pubkeys, outpoints, output_xonly_hex_list, amounts_or_None)
        per transaction. It is host-format specific, so it is supplied by
        the integrator instead of being guessed here."""
        self.sp_scan_extractor = extractor

    def _maybe_scan_silent_payments(self, block: Any) -> None:
        if not (self.sp_scan_extractor and self.sp_wallet):
            return
        try:
            for item in self.sp_scan_extractor(block) or ():
                pubs, outpoints, outputs, amounts = item
                try:
                    self.sp_wallet.scan_tx(pubs, outpoints, outputs, amounts)
                except g.SilentPaymentError as e:
                    self._fail("sp.scan_tx", e)
        except Exception as e:
            self._fail("sp.extractor", e)

    # ------------------------------------------------- WalletConnect
    def open_wc_session(self, dapp_name: str, dapp_url: str,
                        wallet_address: Optional[str] = None,
                        **extra) -> Optional["g.WalletConnectSessionC"]:
        try:
            with self._lock:
                if len(self.wc_sessions) >= MAX_WC_SESSIONS:
                    raise RuntimeError("too many WalletConnect sessions")
                s = g.WalletConnectSessionC(dapp_name, dapp_url,
                                            wallet_address=wallet_address,
                                            **extra)
                self.wc_sessions[s.session_id] = s
                return s
        except Exception as e:
            self._fail("open_wc_session", e)
            return None

    def close_wc_session(self, session_id: str) -> bool:
        with self._lock:
            return self.wc_sessions.pop(session_id, None) is not None

    # ------------------------------------------------- Staking pools
    def add_staking_pool(self, pool_id: Any, name: str, lock_days: int,
                         apy: float, min_stake_nbl: float) -> "g.LockStakingPool":
        with self._lock:
            if pool_id in self.staking_pools:
                raise ValueError(f"pool {pool_id!r} already exists")
            p = g.LockStakingPool(pool_id, name, lock_days, apy, min_stake_nbl)
            self.staking_pools[pool_id] = p
            return p

    # ------------------------------------------------- Coin selection
    def select_coins(self, address: str, total_out: int, fee: int):
        if not self.coin_selector:
            return [], 0
        return self.coin_selector.select_utxos(address, total_out, fee)

    # ------------------------------------------------- Micro channels
    def open_channel(self, channel_id: str, party_a: str, party_b: str,
                     balance_a: int, balance_b: int) -> "g.MicroChannel":
        with self._lock:
            if channel_id in self.channels:
                raise ValueError("channel exists")
            if len(self.channels) >= MAX_CHANNELS:
                raise RuntimeError("too many channels")
            if balance_a < 0 or balance_b < 0:
                raise ValueError("negative balance")
            ch = g.MicroChannel(channel_id, party_a, party_b,
                                balance_a + balance_b, balance_a, balance_b,
                                opened_at=time.time())
            self.channels[channel_id] = ch
            return ch

    def channel_pay(self, channel_id: str, from_party: str, amount: int) -> bool:
        with self._lock:
            ch = self.channels.get(channel_id)
            if not ch or ch.state != "open" or amount <= 0:
                return False
            if from_party == ch.party_a and ch.balance_a >= amount:
                ch.balance_a -= amount; ch.balance_b += amount
            elif from_party == ch.party_b and ch.balance_b >= amount:
                ch.balance_b -= amount; ch.balance_a += amount
            else:
                return False
            ch.sequence += 1
            ch.total_payments += 1
            ch.total_volume += amount
            return True

    def close_channel(self, channel_id: str) -> Optional["g.MicroChannel"]:
        with self._lock:
            ch = self.channels.get(channel_id)
            if not ch or ch.state != "open":
                return None
            ch.state = "closed"
            ch.closed_at = time.time()
            return ch

    # ------------------------------------------------- BIP9 cache
    def bip9_period(self, period: int) -> "g.Bip9PeriodCache":
        with self._lock:
            c = self.bip9_periods.get(period)
            if c is None:
                if len(self.bip9_periods) >= MAX_BIP9_PERIODS:
                    self.bip9_periods.pop(min(self.bip9_periods))
                c = g.Bip9PeriodCache(period=period)
                self.bip9_periods[period] = c
            return c

    # ------------------------------------------------- reporting
    def report(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "errors": self.errors,
                "stats": dict(self.stats),
                "network": self.network_name,
                "peers_tracked": len(self.peer_scores),
                "peers_over_ban_threshold": sum(
                    1 for e in self.peer_scores.values() if e.is_banned),
                "staking_pools": len(self.staking_pools),
                "channels_open": sum(1 for c in self.channels.values()
                                     if c.state == "open"),
                "wc_sessions": len(self.wc_sessions),
            }


# --------------------------------------------------------------------------
# Install / uninstall (class-level wrappers; original always runs first)
# --------------------------------------------------------------------------
def _active_layers() -> List[Layer62]:
    with _ACTIVE_LOCK:
        return list(_ACTIVE)


def _wrap_node_init(host) -> None:
    cls = host.NEBULAFullNode
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)
        try:
            layer = Layer62(self)
            self.group62 = layer
            self.bc.add_listener(layer)
            with _ACTIVE_LOCK:
                _ACTIVE.append(layer)
        except Exception as e:                    # node must still start
            self.group62_error = e

    patched.__wrapped__ = orig
    cls._g62_orig_init = orig
    cls.__init__ = patched


def _wrap_p2p(host) -> None:
    cls = getattr(host, "P2PNode", None)
    if cls is None or not hasattr(cls, "_handle_message"):
        return
    orig = cls._handle_message

    def patched(self, peer, msg, *a, **k):
        result = orig(self, peer, msg, *a, **k)   # original first, unchanged
        for layer in _active_layers():
            layer.observe_message(peer, msg)
        return result

    patched.__wrapped__ = orig
    cls._g62_orig_handle_message = orig
    cls._handle_message = patched


def _wrap_mempool(host) -> None:
    cls = getattr(host, "Mempool", None)
    if cls is None or not hasattr(cls, "submit"):
        return
    orig = cls.submit

    def patched(self, tx, *a, **k):
        result = orig(self, tx, *a, **k)          # original first, unchanged
        for layer in _active_layers():
            layer.observe_submit(tx, result)
        return result

    patched.__wrapped__ = orig
    cls._g62_orig_submit = orig
    cls.submit = patched


def install(host) -> bool:
    """Install the layer. Returns False if already installed."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g62_orig_init", None):
        return False
    _wrap_node_init(host)
    _wrap_p2p(host)
    _wrap_mempool(host)
    return True


def uninstall(host) -> bool:
    """Restore every patched method and detach all layers."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g62_orig_init", None)
    if not orig:
        return False
    cls.__init__ = orig
    del cls._g62_orig_init
    for name, attr, owner in (
            ("_handle_message", "_g62_orig_handle_message", "P2PNode"),
            ("submit", "_g62_orig_submit", "Mempool")):
        oc = getattr(host, owner, None)
        o = getattr(oc, attr, None) if oc else None
        if o:
            setattr(oc, name, o)
            delattr(oc, attr)
    with _ACTIVE_LOCK:
        for layer in _ACTIVE:
            layer.detach()
        _ACTIVE.clear()
    return True
