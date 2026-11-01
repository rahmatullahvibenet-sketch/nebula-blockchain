"""NEBULA group63 - wiring layer (report-only, safe by design).

Connects the four group63 classes to a NEBULAFullNode WITHOUT editing the host file:

    MicroChannelUpdate / StateChannelRound -> bounded in-memory registries (data holders)
    PurposeAccount                         -> wallet-side HD accounts (BIP44/49/84/86 style)
    StateTxBuilder                         -> builds + signs a state-carrying tx (never broadcasts)

Rules followed (from nebula_group63_guide.txt):
  * Nothing in nebula_v10_11.py is modified; the original __init__ always runs first.
  * No callback can ever reject a block/tx: every entry point is wrapped, failures
    are counted in layer.errors and stored in layer.last_error.
  * Consensus is not touched. Memory use is capped (deque / OrderedDict limits).
  * install(host) / uninstall(host) are idempotent and fully reversible.
"""
from __future__ import annotations

import threading
from collections import OrderedDict, deque
from functools import wraps
from typing import Any, Dict, List, Optional, Tuple

import nebula_group63 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

DEFAULT_MAX_ITEMS = 1000


def _safe(default=None):
    """Swallow every exception, count it, return `default`. Never raises."""
    def deco(fn):
        @wraps(fn)
        def inner(self, *a, **k):
            try:
                return fn(self, *a, **k)
            except Exception as e:  # noqa: BLE001 - layer must never break the node
                with self._lock:
                    self.errors += 1
                    self.last_error = f"{fn.__name__}: {type(e).__name__}: {e}"
                return default
        return inner
    return deco


class Layer63:
    """Holds group63 objects for one node. Report-only: observes, never decides."""

    def __init__(self, node, max_items: int = DEFAULT_MAX_ITEMS):
        self.node = node
        self.max_items = max(1, int(max_items))
        self.errors = 0
        self.last_error: Optional[str] = None
        self._lock = threading.RLock()
        self.stats_: Dict[str, int] = {
            "blocks_connected": 0, "reorgs": 0,
            "micro_updates": 0, "micro_rejected": 0,
            "channel_rounds": 0,
            "accounts_opened": 0, "addresses_issued": 0,
            "state_txs_built": 0, "state_tx_failures": 0,
        }
        # data-holder registries (bounded)
        self.micro_updates: deque = deque(maxlen=self.max_items)
        self.rounds: deque = deque(maxlen=self.max_items)
        self.latest_micro: "OrderedDict[str, g.MicroChannelUpdate]" = OrderedDict()
        self.latest_round: "OrderedDict[str, g.StateChannelRound]" = OrderedDict()
        # wallet side
        self.accounts: Dict[Tuple[int, int], g.PurposeAccount] = {}

    # ------------------------------------------------------------------ chain listener
    @_safe()
    def on_connect(self, block) -> None:
        with self._lock:
            self.stats_["blocks_connected"] += 1

    @_safe()
    def on_reorg(self, old, new, ancestor_height) -> None:
        with self._lock:
            self.stats_["reorgs"] += 1

    # ------------------------------------------------------------------ 1. MicroChannelUpdate
    @_safe()
    def record_micro_update(self, channel_id: str, sequence: int,
                            balance_a: int, balance_b: int) -> Optional["g.MicroChannelUpdate"]:
        """Store an update. Stale (non-increasing) sequence numbers are counted and ignored."""
        upd = g.MicroChannelUpdate(channel_id, sequence, balance_a, balance_b)
        with self._lock:
            prev = self.latest_micro.get(channel_id)
            if prev is not None and sequence <= prev.sequence:
                self.stats_["micro_rejected"] += 1
                return None
            self.micro_updates.append(upd)
            self.latest_micro[channel_id] = upd
            self.latest_micro.move_to_end(channel_id)
            while len(self.latest_micro) > self.max_items:
                self.latest_micro.popitem(last=False)
            self.stats_["micro_updates"] += 1
        return upd

    # ------------------------------------------------------------------ 2. StateChannelRound
    @_safe()
    def record_round(self, channel_id: str, round_num: int, state_data: dict,
                     balances: dict, final: bool = False,
                     sigs: Optional[dict] = None) -> Optional["g.StateChannelRound"]:
        rnd = g.StateChannelRound(channel_id, round_num, state_data, balances,
                                  final=final, sigs=dict(sigs or {}))
        with self._lock:
            self.rounds.append(rnd)
            self.latest_round[channel_id] = rnd
            self.latest_round.move_to_end(channel_id)
            while len(self.latest_round) > self.max_items:
                self.latest_round.popitem(last=False)
            self.stats_["channel_rounds"] += 1
        return rnd

    @_safe(default="")
    def round_hash(self, channel_id: str) -> str:
        with self._lock:
            rnd = self.latest_round.get(channel_id)
        return rnd.hash() if rnd else ""

    # ------------------------------------------------------------------ 3. PurposeAccount
    @_safe()
    def open_account(self, index: int, purpose: int, master_key=None) -> Optional["g.PurposeAccount"]:
        """Open (or return the already opened) account. master_key defaults to the node wallet's."""
        key = (int(index), int(purpose))
        with self._lock:
            acct = self.accounts.get(key)
            if acct is not None:
                return acct
        if master_key is None:
            wallet = getattr(self.node, "wallet", None)
            master_key = getattr(wallet, "master_key", None) or getattr(wallet, "master", None)
        if master_key is None:
            raise ValueError("no master_key supplied and node.wallet has none")
        acct = g.PurposeAccount(index, purpose, master_key)
        with self._lock:
            self.accounts[key] = acct
            self.stats_["accounts_opened"] += 1
        return acct

    @_safe()
    def new_receive_address(self, index: int, purpose: int) -> Optional[str]:
        acct = self.accounts.get((int(index), int(purpose)))
        if acct is None:
            raise KeyError(f"account ({index}, {purpose}) is not open")
        addr = acct.get_receive_address()
        with self._lock:
            self.stats_["addresses_issued"] += 1
        return addr

    @_safe()
    def new_change_address(self, index: int, purpose: int) -> Optional[str]:
        acct = self.accounts.get((int(index), int(purpose)))
        if acct is None:
            raise KeyError(f"account ({index}, {purpose}) is not open")
        addr = acct.get_change_address()
        with self._lock:
            self.stats_["addresses_issued"] += 1
        return addr

    # ------------------------------------------------------------------ 4. StateTxBuilder
    def build_state_tx(self, sender: str, payload: bytes, fee: int = 10_000,
                       pay: Optional[List[Tuple[str, int]]] = None, wallet=None):
        """Build + sign a tx carrying `payload`. Returns Transaction or None.
        Never broadcasts - the caller decides what to do with the result."""
        try:
            wallet = wallet or getattr(self.node, "wallet", None)
            blockchain = getattr(self.node, "bc", None)
            if wallet is None or blockchain is None:
                raise RuntimeError("node has no wallet/bc")
            tx = g.StateTxBuilder.build(blockchain, wallet, sender, payload, fee=fee, pay=pay)
        except Exception as e:  # noqa: BLE001
            with self._lock:
                self.errors += 1
                self.last_error = f"build_state_tx: {type(e).__name__}: {e}"
                self.stats_["state_tx_failures"] += 1
            return None
        with self._lock:
            self.stats_["state_txs_built" if tx is not None else "state_tx_failures"] += 1
        return tx

    # ------------------------------------------------------------------ housekeeping
    def snapshot(self) -> Dict[str, Any]:
        with self._lock:
            return {"errors": self.errors, "last_error": self.last_error,
                    "stats": dict(self.stats_), "accounts": len(self.accounts),
                    "channels_micro": len(self.latest_micro),
                    "channels_rounds": len(self.latest_round)}

    def detach(self) -> None:
        listeners = getattr(getattr(self.node, "bc", None), "_listeners", None)
        if listeners is not None:
            try:
                listeners.remove(self)
            except ValueError:
                _NB_SWALLOW_LOG.debug("swallowed ValueError in Layer63.detach", exc_info=True)


def get_layer(node) -> Optional[Layer63]:
    return getattr(node, "group63", None)


def install(host) -> bool:
    """Wrap host.NEBULAFullNode.__init__. Returns True if newly installed."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g63_orig", None):
        return False
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)  # original always runs first
        try:
            self.group63 = Layer63(self)
            self.bc.add_listener(self.group63)
        except Exception as e:  # noqa: BLE001 - node must still start
            self.group63_error = e

    patched.__wrapped__ = orig
    cls._g63_orig = orig
    cls.__init__ = patched
    return True


def uninstall(host) -> bool:
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g63_orig", None)
    if not orig:
        return False
    cls.__init__ = orig
    del cls._g63_orig
    return True
