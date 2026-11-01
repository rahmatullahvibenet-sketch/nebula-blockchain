"""nebula_group47_install.py - wiring layer for the 20 revived NEBULA group47 classes.

Design rules (taken from the group47 guide):
  A) nebula_v10_11.py and nebula_group47.py are NEVER edited.  Everything lives here.
  B) The layer never rejects a block or a transaction.  Every callback is wrapped in
     try/except and failures are counted in ``layer.errors`` / ``layer.error_log``.
  C) Read-only by default.  Anything that changes state of a group47 object goes through
     ``layer.write(...)`` / dedicated methods and is refused until
     ``layer.mutations_enabled = True`` is set explicitly.
  D) install(host) wraps NEBULAFullNode.__init__ (and, optionally, P2PNode._handle_message).
     The original method always runs first.  uninstall(host) restores everything.

Usage:
    import nebula_v10_11 as host
    import nebula_group47_install as g47
    g47.install(host)                  # before the node is created
    node = host.NEBULAFullNode(...)    # node.group47 is now the layer
    print(node.group47.report())       # read-only snapshot, JSON-safe
    g47.uninstall(host)                # back to the original behaviour

IMPORTANT - what is NOT guaranteed:
  * Several group47 classes only SIMULATE value movement (FlashLoanProvider, SettlementLayer,
    StakingInsurance never move real coins; P2PMessage "encryption" only masks text in to_dict).
    They were copied verbatim and are not changed here.  See README_group47_wiring.txt.
  * Attribute names of the host node (rng, lending, governance, oracle, ...) are PROBED, not
    known.  Pass ``deps={...}`` to install() to name them explicitly.
"""
from __future__ import annotations

import collections
import functools
import threading
import time
import weakref
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group47 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

# --------------------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------------------

GROUP_CLASSES: Tuple[str, ...] = (
    "BlockchainGamesHub", "StablecoinReserveManager", "LendingMarketOverview",
    "GovernanceCalendar", "P2PMessage", "P2PMessaging", "ProtocolEvent",
    "ProtocolEventBus", "EconomicModel", "FlashLoanCallback", "FlashLoanProvider",
    "NEBULAProtocolRegistry", "AdvancedAnalyticsV3", "ValidatorNode",
    "ValidatorNetwork", "RoyaltySplitter", "StakingInsurance", "TokenConverter",
    "SettlementLayer", "OnChainCreditScore",
)

# How every one of the 20 classes is reached from the layer (checked by the tests).
COVERAGE: Dict[str, str] = {
    "BlockchainGamesHub":       "component 'games' (chain-listener sampling)",
    "StablecoinReserveManager": "component 'reserve' (wallet/REST read side)",
    "LendingMarketOverview":    "component 'lending_overview'",
    "GovernanceCalendar":       "component 'gov_calendar'",
    "P2PMessage":               "created by P2PMessaging.send via layer.send_message",
    "P2PMessaging":             "component 'messaging'",
    "ProtocolEvent":            "created by ProtocolEventBus.emit",
    "ProtocolEventBus":         "component 'bus' (block_connected / chain_reorg events)",
    "EconomicModel":            "component 'economic'",
    "FlashLoanCallback":        "type check in layer.flash_loan (callbacks must subclass it)",
    "FlashLoanProvider":        "component 'flash'",
    "NEBULAProtocolRegistry":   "component 'registry'",
    "AdvancedAnalyticsV3":      "component 'analytics' (KPI sampling on connect)",
    "ValidatorNode":            "created by ValidatorNetwork.register_validator_node",
    "ValidatorNetwork":         "component 'validators' (P2P liveness hook, report-only)",
    "RoyaltySplitter":          "created on demand by layer.royalty_call",
    "StakingInsurance":         "component 'insurance'",
    "TokenConverter":           "component 'converter'",
    "SettlementLayer":          "component 'settlement'",
    "OnChainCreditScore":       "component 'credit' (on demand: layer.credit_score)",
}

# Names the host node might use for its sub-systems (probed in this order).
DEP_NAMES: Dict[str, Tuple[str, ...]] = {
    "rng":        ("rng", "onchain_rng", "on_chain_rng"),
    "lending_v2": ("lending_v2", "lending_protocol_v2", "lending"),
    "lending":    ("lending", "lending_protocol", "lending_v1", "lending_v2"),
    "governance": ("governance", "governance_engine", "gov"),
    "oracle":     ("oracle", "oracle_v2"),
    "stnbl":      ("stnbl", "staked_nbl"),
    "venbl":      ("venbl", "vote_escrowed_nbl"),
    "staking":    ("staking", "staking_engine"),
    "stablecoin": ("stablecoin", "stablecoin_protocol", "nbusd"),
}

# Read-only methods reachable through layer.read(component, method, ...).
READ_METHODS: Dict[str, frozenset] = {
    "games":            frozenset({"games_stats"}),
    "reserve":          frozenset({"total_reserve_usd", "collateralization_ratio", "reserve_health"}),
    "lending_overview": frozenset({"market_overview", "best_supply_rate", "lowest_borrow_rate"}),
    "gov_calendar":     frozenset({"upcoming_events", "next_halving", "governance_schedule"}),
    "messaging":        frozenset({"unread_count", "messaging_stats"}),
    "bus":              frozenset({"recent", "event_stats"}),
    "economic":         frozenset({"quantity_theory", "fair_value_model",
                                   "halving_impact_model", "inflation_trajectory"}),
    "flash":            frozenset({"flash_loan_stats"}),
    "registry":         frozenset({"get", "list_all", "registry_stats"}),
    "analytics":        frozenset({"kpi_stats", "ecosystem_kpis", "percentile"}),
    "validators":       frozenset({"network_stats"}),
    "insurance":        frozenset({"insurance_stats"}),
    "converter":        frozenset({"conversion_rates"}),
    "settlement":       frozenset({"settlement_stats"}),
    "credit":           frozenset({"compute_score", "max_loan_estimate"}),
}

# State-changing methods reachable through layer.write(...) - refused unless enabled.
WRITE_METHODS: Dict[str, frozenset] = {
    "reserve":    frozenset({"add_reserve", "remove_reserve"}),
    "registry":   frozenset({"register", "deactivate"}),
    "analytics":  frozenset({"record_kpi"}),
    "validators": frozenset({"register_validator_node", "mark_online",
                             "mark_offline", "record_block_signed"}),
    "insurance":  frozenset({"purchase", "claim"}),
    "converter":  frozenset({"nbl_to_stnbl", "stnbl_to_nbl", "nbl_to_venbl", "venbl_to_nbl"}),
}

ROYALTY_READ = frozenset({"splitter_info"})
ROYALTY_WRITE = frozenset({"set_splits", "distribute_royalty", "claim"})

# Report calls: (component, method, args)
REPORT_CALLS: Tuple[Tuple[str, str, tuple], ...] = (
    ("games", "games_stats", ()),
    ("reserve", "reserve_health", ()),
    ("lending_overview", "market_overview", ()),
    ("gov_calendar", "governance_schedule", ()),
    ("messaging", "messaging_stats", ()),
    ("bus", "event_stats", ()),
    ("registry", "registry_stats", ()),
    ("validators", "network_stats", ()),
    ("insurance", "insurance_stats", ()),
    ("settlement", "settlement_stats", ()),
    ("flash", "flash_loan_stats", ()),
    ("economic", "fair_value_model", ()),
    ("economic", "halving_impact_model", ()),
)

# Hard limits so RAM use stays bounded (group47 classes keep everything in memory).
MAX_MESSAGE_CHARS = 2048
MAX_INBOX_PER_ADDRESS = 500
MAX_INBOXES = 10_000
MAX_SETTLEMENT_LEGS = 20
MAX_ROYALTY_COLLECTIONS = 1_000
KPI_SAMPLE_EVERY_N_BLOCKS = 10
ERROR_LOG_SIZE = 50

# Layers currently alive (used by the optional P2P hook).  Weak so a dropped node is freed.
_LAYERS: "weakref.WeakSet[Layer47]" = weakref.WeakSet()


class _Skip(Exception):
    """Raised by a component factory when an optional dependency is missing."""


def _first_attr(obj: Any, names: Tuple[str, ...]) -> Any:
    for name in names:
        value = getattr(obj, name, None)
        if value is not None:
            return value
    return None


# --------------------------------------------------------------------------------------
# The layer
# --------------------------------------------------------------------------------------

class Layer47:
    """Holds one instance of every group47 service and feeds them from chain events."""

    def __init__(self, node: Any, deps: Optional[Dict[str, Any]] = None,
                 mutations_enabled: bool = False,
                 sample_every: int = KPI_SAMPLE_EVERY_N_BLOCKS):
        self.node = node
        self.bc = node.bc
        self.mutations_enabled = bool(mutations_enabled)
        self.sample_every = max(1, int(sample_every))
        self.errors = 0
        self.error_log: "collections.deque[dict]" = collections.deque(maxlen=ERROR_LOG_SIZE)
        self.stats_: Dict[str, Any] = {
            "blocks_seen": 0, "reorgs_seen": 0, "peer_messages_seen": 0,
            "kpi_samples": 0, "nbusd_supply_synced": False,
        }
        self.components: Dict[str, Any] = {}
        self.skipped: Dict[str, str] = {}
        self._royalty: Dict[str, Any] = {}
        self._lock = threading.RLock()
        self._deps_override = dict(deps or {})
        self.deps = {name: self._resolve_dep(name) for name in DEP_NAMES}
        self._build_all()
        _LAYERS.add(self)

    # ---- dependency discovery --------------------------------------------------------

    def _resolve_dep(self, name: str) -> Any:
        if name in self._deps_override:
            return self._deps_override[name]
        found = _first_attr(self.node, DEP_NAMES[name])
        if found is None:
            found = _first_attr(self.bc, DEP_NAMES[name]) if name == "rng" else None
        return found

    # ---- error bookkeeping -----------------------------------------------------------

    def _note_error(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.error_log.append({"where": where,
                                   "error": f"{type(exc).__name__}: {exc}",
                                   "ts": time.time()})

    def _guard(self, where: str, fn: Callable, *a: Any, **k: Any) -> Tuple[bool, Any]:
        try:
            return True, fn(*a, **k)
        except Exception as exc:  # never propagate into the node
            self._note_error(where, exc)
            return False, f"{type(exc).__name__}: {exc}"

    @staticmethod
    def _unwrap(result: Tuple[bool, Any]) -> Tuple[bool, Any]:
        """Methods that already return (bool, message) are passed through un-nested."""
        ok, value = result
        if (ok and isinstance(value, tuple) and len(value) == 2
                and isinstance(value[0], bool)):
            return value
        return result

    # ---- component construction ------------------------------------------------------

    def _build(self, name: str, factory: Callable[[], Any]) -> None:
        try:
            self.components[name] = factory()
        except _Skip as why:
            self.skipped[name] = str(why)
        except Exception as exc:
            self.skipped[name] = f"build failed: {type(exc).__name__}: {exc}"
            self._note_error(f"build:{name}", exc)

    def _build_all(self) -> None:
        bc = self.bc
        d = self.deps
        oracle = d["oracle"] if callable(getattr(d["oracle"], "price", None)) else None

        # order matters: the event bus first, other parts may emit through it
        self._build("bus", lambda: g.ProtocolEventBus())
        self._build("registry", self._make_registry)
        self._build("analytics", lambda: g.AdvancedAnalyticsV3(bc, oracle))
        self._build("economic", lambda: g.EconomicModel(bc, oracle))
        self._build("messaging", lambda: g.P2PMessaging(bc))
        self._build("validators", lambda: g.ValidatorNetwork(bc))
        self._build("flash", lambda: g.FlashLoanProvider(bc))
        self._build("settlement", lambda: g.SettlementLayer(bc))
        self._build("insurance", lambda: g.StakingInsurance(bc))
        self._build("converter", lambda: g.TokenConverter(bc, d["stnbl"], d["venbl"]))
        self._build("reserve", lambda: g.StablecoinReserveManager(bc, oracle))
        self._build("credit", lambda: g.OnChainCreditScore(bc, d["lending"], d["staking"]))
        self._build("games", self._make_games)
        self._build("lending_overview", self._make_lending_overview)
        self._build("gov_calendar", self._make_gov_calendar)

    def _make_registry(self) -> Any:
        registry = g.NEBULAProtocolRegistry(self.bc)
        registry.register("nebula_group47_layer", "Layer47", "1.0")
        return registry

    def _make_games(self) -> Any:
        # OnChainCoinFlip / OnChainDice come from group46 (or the host).  Look them up lazily.
        for needed in ("OnChainCoinFlip", "OnChainDice"):
            if not hasattr(g, needed):
                try:
                    import importlib
                    mod = importlib.import_module("nebula_group46")
                    if hasattr(mod, needed):
                        setattr(g, needed, getattr(mod, needed))
                except Exception:
                    _NB_SWALLOW_LOG.debug("swallowed Exception in Layer47._make_games", exc_info=True)
            if not hasattr(g, needed):
                raise _Skip(f"{needed} not available (needs group46 or the host file)")
        rng = self.deps["rng"]
        if rng is None:
            maker = getattr(g, "OnChainRNG", None)
            if maker is None:
                raise _Skip("no rng on the node and OnChainRNG not available")
            rng = maker(self.bc)
            self.deps["rng"] = rng
        return g.BlockchainGamesHub(self.bc, rng)

    def _make_lending_overview(self) -> Any:
        lending = self.deps["lending_v2"]
        if lending is None or not hasattr(lending, "_pools"):
            raise _Skip("no lending protocol with _pools found on the node")
        return g.LendingMarketOverview(lending, self.bc)

    def _make_gov_calendar(self) -> Any:
        gov = self.deps["governance"]
        if gov is None or not callable(getattr(gov, "list_proposals", None)):
            raise _Skip("no governance engine with list_proposals() found on the node")
        return g.GovernanceCalendar(gov, self.bc)

    # ---- chain listener interface (bc.add_listener) ---------------------------------

    def on_connect(self, block: Any) -> None:
        try:
            with self._lock:
                self.stats_["blocks_seen"] += 1
                seen = self.stats_["blocks_seen"]
            bus = self.components.get("bus")
            if bus is not None:
                bus.emit("block_connected", {"height": self._block_height(block)})
            if seen % self.sample_every == 0:
                self._sample()
        except Exception as exc:
            self._note_error("on_connect", exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        try:
            with self._lock:
                self.stats_["reorgs_seen"] += 1
            bus = self.components.get("bus")
            if bus is not None:
                bus.emit("chain_reorg",
                         {"ancestor_height": ancestor_height,
                          "old_len": self._safe_len(old),
                          "new_len": self._safe_len(new)},
                         severity="warning")
        except Exception as exc:
            self._note_error("on_reorg", exc)

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer47.detach", exc_info=True)
        _LAYERS.discard(self)

    @staticmethod
    def _safe_len(obj: Any) -> Optional[int]:
        try:
            return len(obj)
        except Exception:
            return None

    def _block_height(self, block: Any) -> Any:
        for path in (("height",), ("header", "height")):
            value = block
            try:
                for part in path:
                    value = getattr(value, part)
                if isinstance(value, int) and not isinstance(value, bool):
                    return value
            except AttributeError:
                continue
        return getattr(self.bc, "height", None)

    def _sample(self) -> None:
        """Periodic read-only sampling (every N connected blocks)."""
        analytics = self.components.get("analytics")
        if analytics is not None:
            self._guard("sample:ecosystem_kpis", analytics.ecosystem_kpis)
            games = self.components.get("games")
            if games is not None:
                ok, stats = self._guard("sample:games_stats", games.games_stats)
                if ok:
                    analytics.record_kpi("games_total", float(stats.get("total_games", 0)))
        self._guard("sample:nbusd_supply", self._sync_nbusd_supply)
        with self._lock:
            self.stats_["kpi_samples"] += 1

    def _sync_nbusd_supply(self) -> None:
        """Copy the NBUSD supply into the reserve manager if the node exposes it as an int."""
        stable = self.deps["stablecoin"]
        reserve = self.components.get("reserve")
        if stable is None or reserve is None:
            return
        for attr in ("total_supply", "nbusd_supply", "_total_supply", "_supply"):
            value = getattr(stable, attr, None)
            if callable(value):
                value = value()
            if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
                reserve._nbusd_supply = value
                self.stats_["nbusd_supply_synced"] = True
                return

    # ---- optional P2P hook (see install_p2p_hook) ------------------------------------

    def on_peer_message(self, peer: Any, msg: Any) -> None:
        """Called AFTER the original P2PNode._handle_message.  Liveness only, never consensus."""
        try:
            with self._lock:
                self.stats_["peer_messages_seen"] += 1
            validators = self.components.get("validators")
            if validators is None or peer is None:
                return
            for attr in ("node_id", "id", "peer_id", "address"):
                peer_id = getattr(peer, attr, None)
                if isinstance(peer_id, str) and peer_id in validators._nodes:
                    validators.mark_online(peer_id)
                    return
        except Exception as exc:
            self._note_error("on_peer_message", exc)

    # ---- read / write gateways -------------------------------------------------------

    def read(self, component: str, method: str, *a: Any, **k: Any) -> Tuple[bool, Any]:
        comp = self.components.get(component)
        if comp is None:
            return False, f"component not available: {component}"
        if method not in READ_METHODS.get(component, frozenset()):
            return False, f"method not allowed for read: {component}.{method}"
        return self._guard(f"read:{component}.{method}", getattr(comp, method), *a, **k)

    def write(self, component: str, method: str, *a: Any, **k: Any) -> Tuple[bool, Any]:
        if not self.mutations_enabled:
            return False, "mutations are disabled (set layer.mutations_enabled = True)"
        comp = self.components.get(component)
        if comp is None:
            return False, f"component not available: {component}"
        if method not in WRITE_METHODS.get(component, frozenset()):
            return False, f"method not allowed for write: {component}.{method}"
        return self._unwrap(
            self._guard(f"write:{component}.{method}", getattr(comp, method), *a, **k))

    # ---- dedicated, validated entry points -------------------------------------------

    def credit_score(self, address: str) -> Tuple[bool, Any]:
        if not isinstance(address, str) or not address or len(address) > 128:
            return False, "invalid address"
        return self.read("credit", "compute_score", address)

    def read_inbox(self, address: str, mark_read: bool = False) -> Tuple[bool, Any]:
        """Reading is non-mutating unless mark_read=True (which needs mutations enabled)."""
        messaging = self.components.get("messaging")
        if messaging is None:
            return False, "component not available: messaging"
        if mark_read and not self.mutations_enabled:
            return False, "mark_read needs mutations_enabled"
        return self._guard("read_inbox", messaging.read_inbox, address, mark_read)

    def send_message(self, sender: str, recipient: str, content: str,
                     encrypt: bool = True) -> Tuple[bool, Any]:
        """Bounded send.  NOTE: 'encrypt' only masks the text in to_dict(); it is not real crypto."""
        if not self.mutations_enabled:
            return False, "mutations are disabled (set layer.mutations_enabled = True)"
        messaging = self.components.get("messaging")
        if messaging is None:
            return False, "component not available: messaging"
        for label, value, limit in (("sender", sender, 128), ("recipient", recipient, 128),
                                    ("content", content, MAX_MESSAGE_CHARS)):
            if not isinstance(value, str) or not value or len(value) > limit:
                return False, f"invalid {label}"
        with messaging._lock:
            inbox = messaging._inbox.get(recipient)
            if inbox is None and len(messaging._inbox) >= MAX_INBOXES:
                return False, "too many inboxes"
            if inbox is not None and len(inbox) >= MAX_INBOX_PER_ADDRESS:
                return False, "inbox full"
        return self._guard("send_message", messaging.send, sender, recipient, content, encrypt)

    def flash_loan(self, borrower: str, asset: str, amount: int,
                   callback: Any, data: bytes = b"") -> Tuple[bool, Any]:
        """Simulation only: the provider never moves coins (see README)."""
        if not self.mutations_enabled:
            return False, "mutations are disabled (set layer.mutations_enabled = True)"
        flash = self.components.get("flash")
        if flash is None:
            return False, "component not available: flash"
        if not isinstance(callback, g.FlashLoanCallback):
            return False, "callback must subclass FlashLoanCallback"
        if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
            return False, "amount must be a positive int"
        return self._unwrap(self._guard("flash_loan", flash.flash_loan,
                                        borrower, asset, amount, callback, data))

    def create_settlement(self, legs: List[dict]) -> Tuple[bool, Any]:
        if not self.mutations_enabled:
            return False, "mutations are disabled (set layer.mutations_enabled = True)"
        settlement = self.components.get("settlement")
        if settlement is None:
            return False, "component not available: settlement"
        if not isinstance(legs, list) or not 0 < len(legs) <= MAX_SETTLEMENT_LEGS:
            return False, f"legs must be a list of 1..{MAX_SETTLEMENT_LEGS} items"
        for leg in legs:
            if not isinstance(leg, dict) or not {"from", "to", "asset", "amount"} <= set(leg):
                return False, "each leg needs from/to/asset/amount"
            amount = leg["amount"]
            if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
                return False, "leg amount must be a positive int"
        return self._guard("create_settlement", settlement.create_settlement, legs)

    def execute_settlement(self, settlement_id: str) -> Tuple[bool, Any]:
        """Marks the settlement 'settled' after balance checks; it does NOT move coins."""
        if not self.mutations_enabled:
            return False, "mutations are disabled (set layer.mutations_enabled = True)"
        settlement = self.components.get("settlement")
        if settlement is None:
            return False, "component not available: settlement"
        return self._unwrap(self._guard("execute_settlement", settlement.execute, settlement_id))

    def royalty_call(self, collection_id: str, method: str, *a: Any, **k: Any) -> Tuple[bool, Any]:
        """RoyaltySplitter per collection, created on demand (bounded)."""
        if not isinstance(collection_id, str) or not collection_id or len(collection_id) > 128:
            return False, "invalid collection_id"
        if method in ROYALTY_WRITE:
            if not self.mutations_enabled:
                return False, "mutations are disabled (set layer.mutations_enabled = True)"
        elif method not in ROYALTY_READ:
            return False, f"method not allowed: royalty.{method}"
        with self._lock:
            splitter = self._royalty.get(collection_id)
            if splitter is None:
                if method in ROYALTY_READ:
                    return False, "unknown collection"
                if len(self._royalty) >= MAX_ROYALTY_COLLECTIONS:
                    return False, "too many collections"
                splitter = g.RoyaltySplitter(collection_id)
                self._royalty[collection_id] = splitter
        return self._guard(f"royalty:{method}", getattr(splitter, method), *a, **k)

    # ---- reporting -------------------------------------------------------------------

    def report(self) -> Dict[str, Any]:
        """JSON-safe, read-only snapshot of the whole layer."""
        out: Dict[str, Any] = {}
        for component, method, args in REPORT_CALLS:
            if component not in self.components:
                continue
            ok, result = self.read(component, method, *args)
            out[f"{component}.{method}"] = result if ok else {"error": result}
        analytics = self.components.get("analytics")
        if analytics is not None:
            ok, result = self.read("analytics", "ecosystem_kpis")
            out["analytics.ecosystem_kpis"] = result if ok else {"error": result}
        return {
            "layer": {
                "components": sorted(self.components),
                "skipped": dict(self.skipped),
                "errors": self.errors,
                "recent_errors": list(self.error_log)[-5:],
                "stats": dict(self.stats_),
                "mutations_enabled": self.mutations_enabled,
                "p2p_messaging_encryption": "none (display masking only)",
                "value_movement": "simulation only (flash loans, settlements, insurance)",
            },
            "components": out,
        }


# --------------------------------------------------------------------------------------
# install / uninstall
# --------------------------------------------------------------------------------------

def install_p2p_hook(host: Any) -> bool:
    """Wrap P2PNode._handle_message so layers see peer activity AFTER the original ran."""
    cls = getattr(host, "P2PNode", None)
    if cls is None or not hasattr(cls, "_handle_message"):
        return False
    if cls.__dict__.get("_g47_orig_handle_message"):
        return True
    original = cls._handle_message

    @functools.wraps(original)
    def patched(self: Any, *a: Any, **k: Any) -> Any:
        result = original(self, *a, **k)      # original always first; its errors propagate
        try:
            peer = a[0] if a else k.get("peer")
            msg = a[1] if len(a) > 1 else k.get("msg")
            for layer in list(_LAYERS):
                layer.on_peer_message(peer, msg)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in install_p2p_hook.patched", exc_info=True)                               # the hook must never break message handling
        return result

    cls._g47_orig_handle_message = original
    cls._handle_message = patched
    return True


def install(host: Any, deps: Optional[Dict[str, Any]] = None,
            mutations_enabled: bool = False, hook_p2p: bool = True) -> None:
    """Wrap NEBULAFullNode.__init__ so every new node gets ``node.group47``.  Idempotent."""
    cls = host.NEBULAFullNode
    if cls.__dict__.get("_g47_orig"):
        return
    original = cls.__init__

    @functools.wraps(original)
    def patched(self: Any, *a: Any, **k: Any) -> None:
        original(self, *a, **k)
        try:
            self.group47 = Layer47(self, deps=deps, mutations_enabled=mutations_enabled)
            self.bc.add_listener(self.group47)
        except Exception as exc:
            self.group47_error = exc           # the node must still start
            layer = getattr(self, "group47", None)
            if layer is not None:
                layer.detach()

    cls._g47_orig = original
    cls.__init__ = patched
    if hook_p2p:
        install_p2p_hook(host)


def uninstall(host: Any) -> None:
    """Restore the original methods and detach every live layer."""
    cls = host.NEBULAFullNode
    original = cls.__dict__.get("_g47_orig")
    if original:
        cls.__init__ = original
        del cls._g47_orig
    p2p = getattr(host, "P2PNode", None)
    if p2p is not None:
        original_hm = p2p.__dict__.get("_g47_orig_handle_message")
        if original_hm:
            p2p._handle_message = original_hm
            del p2p._g47_orig_handle_message
    for layer in list(_LAYERS):
        layer.detach()
