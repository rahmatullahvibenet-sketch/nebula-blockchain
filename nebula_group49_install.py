"""NEBULA group49 install layer.

Wires the 20 dead classes of nebula_group49.py into a running NEBULAFullNode
WITHOUT editing nebula_v10_11.py or nebula_group49.py.

Design rules (same as the earlier groups):
  * Nothing here can reject a block, a transaction or a peer message.
  * Every callback runs inside try/except; failures only increment
    layer.errors and are kept in layer.error_log.
  * The original method always runs first (P2P wrapper), and its exceptions
    are never swallowed.
  * Everything that touches consensus-sensitive state is report-only:
    SlashingEngine works on a read-only COPY of validator data, so it can
    record slashes but can never change a real stake.
  * Every in-memory collection that grows with chain or peer activity is capped.
  * install(host) / uninstall(host) are idempotent and fully reversible.

Usage:
    import nebula_v10_11 as host
    import nebula_group49_install as g49
    g49.install(host)          # before creating NEBULAFullNode instances
    node = host.NEBULAFullNode(...)
    node.group49.stats()       # inspect
    g49.uninstall(host)        # node behaves as before
"""
from __future__ import annotations

import collections
import functools
import threading
import time
import weakref
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple

import nebula_group49 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

__all__ = ["Layer49", "install", "uninstall", "install_default"]

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------
LAYER_ATTR = "group49"
ERROR_ATTR = "group49_error"

INIT_BACKUP_ATTR = "_g49_orig"
INIT_OWNED_ATTR = "_g49_orig_owned"
P2P_BACKUP_ATTR = "_g49_orig_handle_message"
P2P_OWNED_ATTR = "_g49_orig_handle_message_owned"
P2P_LAYER_ATTR = "_g49_layer"

EPOCH_LENGTH = 2016                 # default duration of g.Epoch
EPOCH_HISTORY_MAX = 64
ERROR_LOG_MAX = 50
LIMIT_EVENTS_MAX = 50
P2P_COMMAND_KEYS_MAX = 64

MAX_NOTIFICATIONS_PER_USER = 1_000
MAX_AUDIT_HISTORY = 500
MAX_AUDIT_SOURCE_CHARS = 1_000_000
MAX_SLASH_RECORDS = 10_000
MAX_ORDER_BOOKS = 256
MAX_ORDERS_PER_BOOK = 10_000
MAX_FILLS_PER_BOOK = 10_000
MAX_STRATEGIES = 256
MAX_XCM_MESSAGES = 10_000
MAX_XCM_PAYLOAD_CHARS = 16_384
MAX_TEXT_TITLE = 200
MAX_TEXT_MESSAGE = 1_000

STAKING_LOCK_TIERS = (0, 30, 90, 180, 365)   # the tiers SingleStakingStrategy knows

EXPECTED_CLASSES = (
    "XCMMessageType", "XCMMessage", "ValidatorSlashingCondition",
    "NotificationType", "Notification", "YieldStrategy",
    "SingleStakingStrategy", "LPFarmingStrategy", "CompoundingStrategy",
    "ProtocolLimits", "XCMRouterV2", "AdvancedGenesisConfig",
    "PrivacyTransaction", "LiquidityProvisionManager", "ContractAuditor",
    "EcosystemGrantProgram", "OrderBookV2", "SlashingEngine",
    "NotificationSystem", "Epoch",
)

# class name -> (kind, where it is wired inside the layer)
COVERAGE_TABLE: Dict[str, Tuple[str, str]] = {
    "XCMMessageType":             ("enum",    "send_xcm() / inbound 'xcm' P2P messages"),
    "XCMMessage":                 ("data",    "created by router.send_xcm()"),
    "ValidatorSlashingCondition": ("enum",    "slash_report()"),
    "NotificationType":           ("enum",    "subscribe() / notify() / on_connect()"),
    "Notification":               ("data",    "created by notifications.push()"),
    "YieldStrategy":              ("service", "strategies (base of the three strategy classes)"),
    "SingleStakingStrategy":      ("service", "strategies (one per lock tier)"),
    "LPFarmingStrategy":          ("service", "add_strategy('lp_farming', ...)"),
    "CompoundingStrategy":        ("service", "add_strategy('compounding', ...)"),
    "ProtocolLimits":             ("service", "limits (checked on every connected block)"),
    "XCMRouterV2":                ("service", "router (fed by the P2PNode._handle_message hook)"),
    "AdvancedGenesisConfig":      ("service", "genesis_config + genesis_report() (chain listener)"),
    "PrivacyTransaction":         ("service", "privacy / create_private_tx()"),
    "LiquidityProvisionManager":  ("service", "lp_manager"),
    "ContractAuditor":            ("service", "auditor / audit_contract()"),
    "EcosystemGrantProgram":      ("service", "grants"),
    "OrderBookV2":                ("service", "order_books / place_limit()"),
    "SlashingEngine":             ("service", "slashing (report-only, read-only validator view)"),
    "NotificationSystem":         ("service", "notifications (fed by on_connect)"),
    "Epoch":                      ("service", "epoch / epoch_history (tracked by on_connect / on_reorg)"),
}

_SERVICE_ATTRS = {
    "YieldStrategy": None,          # base class, checked through the strategies dict
    "SingleStakingStrategy": None,
    "LPFarmingStrategy": None,
    "CompoundingStrategy": None,
    "ProtocolLimits": "limits",
    "XCMRouterV2": "router",
    "AdvancedGenesisConfig": "genesis_config",
    "PrivacyTransaction": "privacy",
    "LiquidityProvisionManager": "lp_manager",
    "ContractAuditor": "auditor",
    "EcosystemGrantProgram": "grants",
    "OrderBookV2": None,            # created on demand per pair
    "SlashingEngine": "slashing",
    "NotificationSystem": "notifications",
    "Epoch": "epoch",
}

# Module-level registry of live layers (needed by uninstall) and the P2P class.
_LAYERS: "weakref.WeakSet[Layer49]" = weakref.WeakSet()
_LAYERS_LOCK = threading.RLock()
_P2P_CLASS: Optional[type] = None


# --------------------------------------------------------------------------
# Small defensive helpers (the host object shapes are only partly known)
# --------------------------------------------------------------------------
def _first_attr(obj: Any, names: Iterable[str], default: Any = None) -> Any:
    for name in names:
        try:
            value = getattr(obj, name)
        except Exception:
            continue
        if value is not None:
            return value
    return default


def _block_height(block: Any) -> Optional[int]:
    header = getattr(block, "header", None)
    for source in (header, block):
        if source is None:
            continue
        value = getattr(source, "height", None)
        if isinstance(value, int) and not isinstance(value, bool):
            return value
    return None


def _block_txs(block: Any) -> List[Any]:
    for name in ("transactions", "txs", "tx_list", "vtx"):
        value = getattr(block, name, None)
        if isinstance(value, (list, tuple)):
            return list(value)
    return []


def _tx_list(tx: Any, name: str) -> List[Any]:
    value = getattr(tx, name, None)
    if isinstance(value, (list, tuple)):
        return list(value)
    return []


def _coinbase_total(txs: List[Any]) -> int:
    if not txs:
        return 0
    total = 0
    for out in _tx_list(txs[0], "outputs"):
        value = getattr(out, "value", 0)
        if isinstance(value, int) and not isinstance(value, bool):
            total += value
    return total


def _enum_lookup(enum_cls: Any, key: Any) -> Any:
    """Return the enum member for a member, a value string or a member name."""
    if isinstance(key, enum_cls):
        return key
    if not isinstance(key, str):
        return None
    for member in enum_cls:
        if member.value == key or member.name.lower() == key.lower():
            return member
    return None


def _find_instance(owner: Any, cls: Optional[type], names: Iterable[str]) -> Any:
    """Find an attribute of owner that is an instance of cls (names first, then a 2-level scan)."""
    if cls is None:
        return None
    for name in names:
        value = _first_attr(owner, (name,))
        if isinstance(value, cls):
            return value
    try:
        first_level = list(vars(owner).values())
    except TypeError:
        return None
    for value in first_level:
        if isinstance(value, cls):
            return value
    for value in first_level:
        if value is None or isinstance(value, (str, bytes, int, float, bool, list, tuple, dict, set)):
            continue
        try:
            nested = list(vars(value).values())
        except TypeError:
            continue
        for inner in nested:
            if isinstance(inner, cls):
                return inner
    return None


def _find_by_capability(owner: Any, names: Iterable[str], needs: Callable[[Any], bool]) -> Any:
    """Find an attribute of owner that satisfies a duck-typing predicate."""
    for name in names:
        value = _first_attr(owner, (name,))
        if value is not None:
            try:
                if needs(value):
                    return value
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in _find_by_capability", exc_info=True)
    try:
        values = list(vars(owner).values())
    except TypeError:
        return None
    for value in values:
        if value is None or isinstance(value, (str, bytes, int, float, bool, list, tuple, dict, set)):
            continue
        try:
            if needs(value):
                return value
        except Exception:
            continue
    return None


def _guarded(default_factory: Optional[Callable[[], Any]] = None):
    """Method decorator: never raise, count the failure, return a safe default."""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(self, *args, **kwargs):
            try:
                return fn(self, *args, **kwargs)
            except Exception as exc:
                self._record_error(fn.__name__, exc)
                return default_factory() if default_factory else None
        return wrapper
    return decorator


# --------------------------------------------------------------------------
# Null / read-only stand-ins used when the host does not expose a dependency
# --------------------------------------------------------------------------
class _NullDex:
    """Used when the node has no DEX object; LiquidityProvisionManager then sees zero pools."""
    def __init__(self):
        self._pools: Dict[str, Any] = {}


class _NullValidatorSet:
    def get_validator(self, address: str) -> None:
        return None


class _ValidatorSetView:
    """Read-only view: always returns a COPY so SlashingEngine can never change real validator data."""

    def __init__(self, inner: Any):
        self._inner = inner

    def get_validator(self, address: str) -> Optional[dict]:
        try:
            info = self._inner.get_validator(address)
        except Exception:
            return None
        if info is None:
            return None
        if isinstance(info, dict):
            return dict(info)
        stake = getattr(info, "stake", 0)
        if not isinstance(stake, (int, float)) or isinstance(stake, bool):
            stake = 0
        return {"stake": stake}


# --------------------------------------------------------------------------
# The layer
# --------------------------------------------------------------------------
class Layer49:
    """Owns one instance of every group49 service and connects them to the node."""

    def __init__(self, node: Any):
        self.node = node
        self.errors = 0
        self.error_log: "collections.deque" = collections.deque(maxlen=ERROR_LOG_MAX)
        self.build_failures: Dict[str, str] = {}
        self.report_only = True
        self.listening = False
        self.p2p_attached = False
        self._lock = threading.RLock()
        self._p2p_node: Any = None

        self.stats_: Dict[str, int] = collections.defaultdict(int)
        self.p2p_commands: Dict[str, int] = {}
        self.limit_events: "collections.deque" = collections.deque(maxlen=LIMIT_EVENTS_MAX)
        self.limit_counters: Dict[str, int] = collections.defaultdict(int)
        self.genesis_observed: Optional[dict] = None

        self.bc = _first_attr(node, ("bc", "blockchain", "chain"))
        self.dex = _find_by_capability(
            node, ("dex", "nebula_dex", "dex_engine"),
            lambda v: isinstance(getattr(v, "_pools", None), dict))
        validator_source = _find_by_capability(
            node, ("validator_set", "validators", "validator_manager", "vs"),
            lambda v: callable(getattr(v, "get_validator", None)))
        if validator_source is None and self.bc is not None:
            validator_source = _find_by_capability(
                self.bc, ("validator_set", "validators", "validator_manager", "vs"),
                lambda v: callable(getattr(v, "get_validator", None)))
        self.validator_set_attached = validator_source is not None
        self.dex_attached = self.dex is not None

        # ---- services (each build is isolated; one failure never blocks the others)
        self.limits = self._build("limits", lambda: g.ProtocolLimits())
        self.genesis_config = self._build("genesis_config", lambda: g.AdvancedGenesisConfig())
        self.router = self._build("router", lambda: g.XCMRouterV2(self.bc))
        self.privacy = self._build("privacy", lambda: g.PrivacyTransaction(self.bc))
        self.lp_manager = self._build(
            "lp_manager", lambda: g.LiquidityProvisionManager(self.dex if self.dex is not None else _NullDex()))
        self.auditor = self._build("auditor", lambda: g.ContractAuditor())
        self.grants = self._build("grants", lambda: g.EcosystemGrantProgram(self.bc))
        self.slashing = self._build(
            "slashing",
            lambda: g.SlashingEngine(
                self.bc,
                _ValidatorSetView(validator_source) if validator_source is not None else _NullValidatorSet()))
        self.notifications = self._build("notifications", lambda: g.NotificationSystem(self.bc))

        self.order_books: Dict[str, Any] = {}
        self.strategies: Dict[str, Any] = {}
        for lock_days in STAKING_LOCK_TIERS:
            self._build("strategy_staking_%d" % lock_days,
                        lambda d=lock_days: self._register_strategy(g.SingleStakingStrategy(d)))

        self.epoch_length = EPOCH_LENGTH
        self.epoch: Any = None
        self.epoch_history: "collections.deque" = collections.deque(maxlen=EPOCH_HISTORY_MAX)
        self._build("initial_epoch", self._start_initial_epoch)

    def _start_initial_epoch(self) -> None:
        """Start tracking at the chain's current height so the Epoch service is live before the first new block."""
        height = _first_attr(self.bc, ("height",))
        if callable(height):
            height = height()
        if not isinstance(height, int) or isinstance(height, bool) or height < 0:
            height = 0
        number = height // self.epoch_length
        epoch = g.Epoch(number, number * self.epoch_length, self.epoch_length)
        self.epoch = epoch
        self.epoch_history.append(epoch)

    # ------------------------------------------------------------------ plumbing
    def _build(self, name: str, factory: Callable[[], Any]) -> Any:
        try:
            return factory()
        except Exception as exc:
            self.build_failures[name] = "%s: %s" % (type(exc).__name__, exc)
            self._record_error("build." + name, exc)
            return None

    def _record_error(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.error_log.append((time.time(), where, "%s: %s" % (type(exc).__name__, exc)))

    def _step(self, name: str, fn: Callable[..., Any], *args: Any) -> None:
        try:
            fn(*args)
        except Exception as exc:
            self._record_error(name, exc)

    def _register_strategy(self, strategy: Any) -> Any:
        if len(self.strategies) >= MAX_STRATEGIES:
            raise RuntimeError("strategy registry full")
        self.strategies[strategy.name] = strategy
        return strategy

    # ------------------------------------------------------------------ attach / detach
    def attach(self) -> None:
        """Register as chain listener and hook the node's P2PNode (if any). Never raises."""
        try:
            add = getattr(self.bc, "add_listener", None)
            if callable(add):
                add(self)
                self.listening = True
            else:
                self._record_error("attach.chain", RuntimeError("blockchain has no add_listener"))
        except Exception as exc:
            self._record_error("attach.chain", exc)
        try:
            p2p = _find_instance(self.node, _P2P_CLASS, ("p2p", "network", "p2p_node", "node"))
            if p2p is not None:
                setattr(p2p, P2P_LAYER_ATTR, self)
                self._p2p_node = p2p
                self.p2p_attached = True
        except Exception as exc:
            self._record_error("attach.p2p", exc)

    def detach(self) -> None:
        try:
            listeners = getattr(self.bc, "_listeners", None)
            if isinstance(listeners, list):
                try:
                    listeners.remove(self)
                except ValueError:
                    _NB_SWALLOW_LOG.debug("swallowed ValueError in Layer49.detach", exc_info=True)
            else:
                remove = getattr(self.bc, "remove_listener", None)
                if callable(remove):
                    remove(self)
        except Exception as exc:
            self._record_error("detach.chain", exc)
        self.listening = False
        try:
            if self._p2p_node is not None and getattr(self._p2p_node, P2P_LAYER_ATTR, None) is self:
                delattr(self._p2p_node, P2P_LAYER_ATTR)
        except Exception as exc:
            self._record_error("detach.p2p", exc)
        self._p2p_node = None
        self.p2p_attached = False

    # ------------------------------------------------------------------ chain listener
    @_guarded()
    def on_connect(self, block: Any) -> None:
        with self._lock:
            self.stats_["blocks_seen"] += 1
        height = _block_height(block)
        txs = _block_txs(block)
        self._step("on_connect.epoch", self._track_epoch, height, txs)
        self._step("on_connect.limits", self._check_limits, height, txs)
        self._step("on_connect.notify", self._notify_receivers, height, txs)
        self._step("on_connect.genesis", self._capture_genesis, height, txs)

    @_guarded()
    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        with self._lock:
            self.stats_["reorgs_seen"] += 1
        self._step("on_reorg.epoch", self._rewind_epochs, old, ancestor_height)

    def _track_epoch(self, height: Optional[int], txs: List[Any]) -> None:
        if height is None:
            return
        with self._lock:
            epoch = self.epoch
            if epoch is None or not epoch.is_active(height):
                number = height // self.epoch_length
                epoch = g.Epoch(number, number * self.epoch_length, self.epoch_length)
                self.epoch = epoch
                self.epoch_history.append(epoch)
                self.stats_["epochs_started"] += 1
            epoch.txs_processed += len(txs)
            # "rewards" here means total coinbase output value (subsidy + fees) of the block.
            epoch.rewards_distributed += _coinbase_total(txs)

    def _rewind_epochs(self, old: Any, ancestor_height: Any) -> None:
        if not isinstance(ancestor_height, int):
            return
        with self._lock:
            # Subtract the disconnected blocks (only when `old` is a list of block-like objects).
            if isinstance(old, (list, tuple)):
                for blk in old:
                    h = _block_height(blk)
                    if h is None:
                        continue
                    txs = _block_txs(blk)
                    for ep in self.epoch_history:
                        if ep.is_active(h):
                            ep.txs_processed = max(0, ep.txs_processed - len(txs))
                            ep.rewards_distributed = max(0, ep.rewards_distributed - _coinbase_total(txs))
                            break
            # Drop epochs that start after the common ancestor.
            while self.epoch_history and self.epoch_history[-1].start_block > ancestor_height:
                self.epoch_history.pop()
            last = self.epoch_history[-1] if self.epoch_history else None
            self.epoch = last if (last is not None and last.is_active(ancestor_height)) else None

    def _check_limits(self, height: Optional[int], txs: List[Any]) -> None:
        if self.limits is None:
            return
        for tx in txs:
            checks = (("MAX_TX_INPUTS", len(_tx_list(tx, "inputs"))),
                      ("MAX_TX_OUTPUTS", len(_tx_list(tx, "outputs"))))
            for name, count in checks:
                if not self.limits.is_within_limits(name, count):
                    with self._lock:
                        self.limit_counters[name] += 1
                        self.limit_events.append({
                            "height": height,
                            "txid": str(getattr(tx, "txid", "?"))[:64],
                            "limit": name,
                            "value": count,
                        })

    def subscribed_users(self) -> set:
        notif = self.notifications
        if notif is None:
            return set()
        with notif._lock:
            return set(notif._prefs.keys())

    def _notify_receivers(self, height: Optional[int], txs: List[Any]) -> None:
        notif = self.notifications
        if notif is None:
            return
        users = self.subscribed_users()
        if not users:
            return
        for tx in txs:
            for out in _tx_list(tx, "outputs"):
                address = getattr(out, "address", None)
                if address not in users:
                    continue
                value = getattr(out, "value", 0)
                amount = (value / 10 ** g.DECIMALS) if isinstance(value, (int, float)) else 0.0
                if notif.push(address, g.NotificationType.TX_RECEIVED, "Funds received",
                              "%.3f NBL in block %s" % (amount, height)):
                    with self._lock:
                        self.stats_["notifications_pushed"] += 1
                    self._trim_notifications(address)

    def _trim_notifications(self, user: str) -> None:
        notif = self.notifications
        with notif._lock:
            items = notif._notifs.get(user)
            if items is not None and len(items) > MAX_NOTIFICATIONS_PER_USER:
                del items[:len(items) - MAX_NOTIFICATIONS_PER_USER]

    def _capture_genesis(self, height: Optional[int], txs: List[Any]) -> None:
        if height != 0 or self.genesis_observed is not None:
            return
        total = 0
        for tx in txs:
            for out in _tx_list(tx, "outputs"):
                value = getattr(out, "value", 0)
                if isinstance(value, int) and not isinstance(value, bool):
                    total += value
        self.genesis_observed = {"height": 0, "tx_count": len(txs), "output_total": total}

    # ------------------------------------------------------------------ P2P observer
    def on_p2p_message(self, peer: Any, msg: Any) -> None:
        """Called AFTER the original P2PNode._handle_message. Observe only; never raises."""
        try:
            command = None
            if isinstance(msg, dict):
                command = msg.get("command") or msg.get("type") or msg.get("cmd")
            else:
                command = _first_attr(msg, ("command", "type", "cmd"))
            command = command if isinstance(command, str) else "other"
            with self._lock:
                self.stats_["p2p_messages"] += 1
                if command in self.p2p_commands or len(self.p2p_commands) < P2P_COMMAND_KEYS_MAX:
                    self.p2p_commands[command] = self.p2p_commands.get(command, 0) + 1
                else:
                    self.p2p_commands["other"] = self.p2p_commands.get("other", 0) + 1
            if command.lower() == "xcm":
                payload = msg.get("payload") if isinstance(msg, dict) else getattr(msg, "payload", None)
                self._route_inbound_xcm(payload)
        except Exception as exc:
            self._record_error("on_p2p_message", exc)

    def _route_inbound_xcm(self, payload: Any) -> None:
        """Inbound XCM: expects a dict with origin, destination, type, payload, fee.
        Only works for channels the operator opened; messages stay 'pending' (never auto-processed)."""
        if not isinstance(payload, dict):
            self._bump("xcm_inbound_rejected")
            return
        ok, _ = self.send_xcm(payload.get("origin"), payload.get("destination"),
                              payload.get("type"), payload.get("payload"), payload.get("fee"))
        self._bump("xcm_inbound_accepted" if ok else "xcm_inbound_rejected")

    def _bump(self, key: str) -> None:
        with self._lock:
            self.stats_[key] += 1

    # ------------------------------------------------------------------ strategies
    @_guarded(lambda: None)
    def add_strategy(self, kind: str, **params: Any) -> Optional[str]:
        """kind: 'staking' (lock_days), 'lp_farming' (pair, apy), 'compounding' (base_apy, freq=365)."""
        factories = {
            "staking": g.SingleStakingStrategy,
            "lp_farming": g.LPFarmingStrategy,
            "compounding": g.CompoundingStrategy,
        }
        factory = factories.get(kind)
        if factory is None:
            return None
        strategy = factory(**params)
        with self._lock:
            self._register_strategy(strategy)
        return strategy.name

    @_guarded(lambda: None)
    def strategy_quote(self, name: str, amount: float) -> Optional[dict]:
        strategy = self.strategies.get(name)
        if strategy is None or not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            return None
        return strategy.execute(float(amount))

    def strategy_names(self) -> List[str]:
        return sorted(self.strategies)

    # ------------------------------------------------------------------ order books
    @_guarded(lambda: None)
    def order_book(self, pair: str) -> Any:
        if not isinstance(pair, str) or not pair or len(pair) > 64:
            return None
        with self._lock:
            book = self.order_books.get(pair)
            if book is None:
                if len(self.order_books) >= MAX_ORDER_BOOKS:
                    return None
                book = g.OrderBookV2(pair)
                self.order_books[pair] = book
            return book

    @_guarded(lambda: None)
    def place_limit(self, pair: str, side: str, price: float, qty: float, trader: str) -> Optional[str]:
        valid_number = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0
        if side not in ("buy", "sell") or not valid_number(price) or not valid_number(qty):
            return None
        book = self.order_book(pair)
        if book is None:
            return None
        with book._lock:
            if len(book._bids) + len(book._asks) >= MAX_ORDERS_PER_BOOK:
                return None
        order_id = book.place_limit(side, float(price), float(qty), str(trader))
        with book._lock:
            if len(book._fills) > MAX_FILLS_PER_BOOK:
                del book._fills[:len(book._fills) - MAX_FILLS_PER_BOOK]
        return order_id

    # ------------------------------------------------------------------ liquidity provision
    @_guarded(lambda: None)
    def lp_add_position(self, owner: str, pool_id: str, token_a: str, token_b: str,
                        amount_a: float, amount_b: float, lp_tokens: float) -> Optional[str]:
        return self.lp_manager.add_lp_position(owner, pool_id, token_a, token_b, amount_a, amount_b, lp_tokens)

    @_guarded(lambda: [])
    def lp_positions(self, owner: str) -> List[dict]:
        return self.lp_manager.all_positions(owner)

    # ------------------------------------------------------------------ contract audit
    @_guarded(lambda: None)
    def audit_contract(self, name: str, source_code: str) -> Optional[dict]:
        if not isinstance(source_code, str) or len(source_code) > MAX_AUDIT_SOURCE_CHARS:
            return None
        result = self.auditor.audit_code(str(name)[:128], source_code)
        if len(self.auditor._audits) > MAX_AUDIT_HISTORY:
            del self.auditor._audits[:len(self.auditor._audits) - MAX_AUDIT_HISTORY]
        return result

    # ------------------------------------------------------------------ notifications
    @_guarded(lambda: 0)
    def subscribe(self, user: str, type_names: List[Any]) -> int:
        members = []
        for key in type_names or []:
            member = _enum_lookup(g.NotificationType, key)
            if member is not None:
                members.append(member)
        if not members:
            return 0
        self.notifications.subscribe(user, members)
        return len(members)

    @_guarded(lambda: False)
    def notify(self, user: str, type_name: Any, title: str, message: str) -> bool:
        member = _enum_lookup(g.NotificationType, type_name)
        if member is None:
            return False
        pushed = self.notifications.push(user, member, str(title)[:MAX_TEXT_TITLE], str(message)[:MAX_TEXT_MESSAGE])
        if pushed:
            self._trim_notifications(user)
        return bool(pushed)

    # ------------------------------------------------------------------ slashing (report-only)
    @_guarded(lambda: (False, 0))
    def slash_report(self, validator: str, condition: Any, evidence: str = "") -> Tuple[bool, int]:
        """Records a slashing report. Real stakes are never changed (the engine only sees a copy)."""
        member = _enum_lookup(g.ValidatorSlashingCondition, condition)
        if member is None:
            return False, 0
        result = self.slashing.slash(validator, member, str(evidence)[:MAX_TEXT_MESSAGE])
        if len(self.slashing._slashes) > MAX_SLASH_RECORDS:
            del self.slashing._slashes[:len(self.slashing._slashes) - MAX_SLASH_RECORDS]
        return result

    # ------------------------------------------------------------------ cross-chain messages
    @_guarded(lambda: False)
    def open_xcm_channel(self, src: str, dst: str) -> bool:
        if not isinstance(src, str) or not isinstance(dst, str) or not src or not dst:
            return False
        return bool(self.router.open_channel(src, dst))

    @_guarded(lambda: (False, "error"))
    def send_xcm(self, origin: Any, destination: Any, type_name: Any, payload: Any, fee: Any) -> Tuple[bool, str]:
        member = _enum_lookup(g.XCMMessageType, type_name)
        if member is None:
            return False, "Unknown message type"
        if not isinstance(origin, str) or not isinstance(destination, str) or not origin or not destination:
            return False, "Bad origin/destination"
        if not isinstance(payload, dict) or len(repr(payload)) > MAX_XCM_PAYLOAD_CHARS:
            return False, "Bad payload"
        if not isinstance(fee, int) or isinstance(fee, bool) or fee < 0:
            return False, "Bad fee"
        with self.router._lock:
            if len(self.router._messages) >= MAX_XCM_MESSAGES:
                return False, "Router full"
        return self.router.send_xcm(origin, destination, member, payload, fee)

    @_guarded(lambda: (False, "error"))
    def process_xcm(self, msg_id: str) -> Tuple[bool, str]:
        return self.router.process_message(msg_id)

    # ------------------------------------------------------------------ privacy
    @_guarded(lambda: None)
    def create_private_tx(self, sender: str, recipient: str, amount: int, ring_size: int = 11) -> Optional[dict]:
        if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
            return None
        if not isinstance(ring_size, int) or not (2 <= ring_size <= 64):
            return None
        return self.privacy.create_ring_tx(sender, recipient, amount, ring_size)

    # ------------------------------------------------------------------ genesis
    @_guarded(lambda: {})
    def genesis_report(self) -> dict:
        """Summary of the default mainnet genesis config next to what the chain actually produced at height 0."""
        preview = g.AdvancedGenesisConfig().default_mainnet()
        return {"config": preview.genesis_info(), "observed": self.genesis_observed}

    @_guarded(lambda: None)
    def genesis_preview_block(self) -> Any:
        """Builds (never installs) the genesis block of the live genesis_config."""
        return self.genesis_config.to_genesis_block()

    # ------------------------------------------------------------------ reporting
    def coverage(self) -> Dict[str, dict]:
        """For each of the 20 classes: kind, where it is wired, how it becomes live, and whether it is usable now.

        mode 'always'    : an instance exists as soon as the node starts
        mode 'on_demand' : created by a layer method (add_strategy / place_limit); usable now, instance later
        mode 'data'      : enum or data class, used through the layer methods that create or look up members
        """
        on_demand = {"LPFarmingStrategy": "add_strategy", "CompoundingStrategy": "add_strategy",
                     "OrderBookV2": "place_limit"}
        report: Dict[str, dict] = {}
        for name in EXPECTED_CLASSES:
            kind, where = COVERAGE_TABLE[name]
            cls = getattr(g, name, None)
            attr = _SERVICE_ATTRS.get(name)
            if name in on_demand:
                mode = "on_demand"
                live = cls is not None and callable(getattr(self, on_demand[name], None))
            elif attr is not None:
                mode = "always"
                live = cls is not None and isinstance(getattr(self, attr, None), cls)
            elif kind == "service":
                mode = "always"      # YieldStrategy family: instances sit in self.strategies
                live = cls is not None and any(isinstance(s, cls) for s in self.strategies.values())
            else:
                mode = "data"
                live = cls is not None
            report[name] = {"kind": kind, "mode": mode, "wired_via": where,
                            "available": cls is not None, "live": live}
        return report

    def stats(self) -> dict:
        def safe(fn: Callable[[], Any]) -> Any:
            try:
                return fn()
            except Exception as exc:
                self._record_error("stats", exc)
                return None

        with self._lock:
            counters = dict(self.stats_)
            commands = dict(self.p2p_commands)
            limit_counters = dict(self.limit_counters)
            epoch_info = self.epoch.to_dict() if self.epoch is not None else None
        return {
            "errors": self.errors,
            "build_failures": dict(self.build_failures),
            "report_only": self.report_only,
            "listening": self.listening,
            "p2p_attached": self.p2p_attached,
            "dex_attached": self.dex_attached,
            "validator_set_attached": self.validator_set_attached,
            "counters": counters,
            "p2p_commands": commands,
            "limit_violations": limit_counters,
            "epoch": epoch_info,
            "epochs_tracked": len(self.epoch_history),
            "xcm": safe(lambda: self.router.xcm_stats()),
            "notifications": safe(lambda: self.notifications.notif_stats()),
            "slashing": safe(lambda: self.slashing.slashing_stats()),
            "grants": safe(lambda: self.grants.program_stats()),
            "privacy": safe(lambda: self.privacy.privacy_stats()),
            "audits": safe(lambda: len(self.auditor.audit_history())),
            "strategies": self.strategy_names(),
            "order_books": {pair: safe(book.ob_stats) for pair, book in list(self.order_books.items())},
            "all_limits": safe(lambda: self.limits.all_limits()),
        }


# --------------------------------------------------------------------------
# Class patching helpers (reversible; handles inherited methods correctly)
# --------------------------------------------------------------------------
def _patch_method(cls: type, name: str, new_fn: Callable[..., Any], backup_attr: str, owned_attr: str) -> None:
    owned = name in vars(cls)
    original = getattr(cls, name)
    setattr(cls, backup_attr, original)
    setattr(cls, owned_attr, owned)
    setattr(cls, name, new_fn)


def _unpatch_method(cls: type, name: str, backup_attr: str, owned_attr: str) -> None:
    original = getattr(cls, backup_attr, None)
    if original is None:
        return
    if getattr(cls, owned_attr, True):
        setattr(cls, name, original)
    else:
        try:
            delattr(cls, name)
        except AttributeError:
            _NB_SWALLOW_LOG.debug("swallowed AttributeError in _unpatch_method", exc_info=True)
    for attr in (backup_attr, owned_attr):
        try:
            delattr(cls, attr)
        except AttributeError:
            _NB_SWALLOW_LOG.debug("swallowed AttributeError in _unpatch_method", exc_info=True)


def install(host: Any) -> None:
    """Wrap NEBULAFullNode.__init__ (and P2PNode._handle_message when present). Idempotent."""
    global _P2P_CLASS
    node_cls = host.NEBULAFullNode
    p2p_cls = getattr(host, "P2PNode", None)
    if isinstance(p2p_cls, type):
        _P2P_CLASS = p2p_cls

    if not getattr(node_cls, INIT_BACKUP_ATTR, None):
        original_init = node_cls.__init__

        @functools.wraps(original_init)
        def patched_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            try:
                layer = Layer49(self)
                layer.attach()
                setattr(self, LAYER_ATTR, layer)
                with _LAYERS_LOCK:
                    _LAYERS.add(layer)
            except Exception as exc:                 # the node must still start
                setattr(self, ERROR_ATTR, exc)

        _patch_method(node_cls, "__init__", patched_init, INIT_BACKUP_ATTR, INIT_OWNED_ATTR)

    if (isinstance(p2p_cls, type) and callable(getattr(p2p_cls, "_handle_message", None))
            and not getattr(p2p_cls, P2P_BACKUP_ATTR, None)):
        original_handler = p2p_cls._handle_message

        @functools.wraps(original_handler)
        def patched_handler(self, *args, **kwargs):
            result = original_handler(self, *args, **kwargs)      # original always first, errors propagate
            layer = getattr(self, P2P_LAYER_ATTR, None)
            if layer is not None:
                peer = args[0] if len(args) > 0 else kwargs.get("peer")
                msg = args[1] if len(args) > 1 else kwargs.get("msg")
                layer.on_p2p_message(peer, msg)                   # never raises
            return result

        _patch_method(p2p_cls, "_handle_message", patched_handler, P2P_BACKUP_ATTR, P2P_OWNED_ATTR)


def uninstall(host: Any) -> None:
    """Detach every live layer and restore the original methods."""
    global _P2P_CLASS
    with _LAYERS_LOCK:
        layers = list(_LAYERS)
        _LAYERS.clear()
    for layer in layers:
        layer.detach()
        try:
            if getattr(layer.node, LAYER_ATTR, None) is layer:
                delattr(layer.node, LAYER_ATTR)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in uninstall", exc_info=True)
    _unpatch_method(host.NEBULAFullNode, "__init__", INIT_BACKUP_ATTR, INIT_OWNED_ATTR)
    p2p_cls = getattr(host, "P2PNode", None)
    if isinstance(p2p_cls, type):
        _unpatch_method(p2p_cls, "_handle_message", P2P_BACKUP_ATTR, P2P_OWNED_ATTR)
    _P2P_CLASS = None


def install_default() -> Any:
    """Import the real host module and install the layer on it."""
    import nebula_v10_11 as host
    install(host)
    return host
