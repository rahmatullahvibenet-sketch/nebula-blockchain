"""NEBULA group33 - wiring layer.

Connects the 20 group33 classes (nebula_group33.py) to a running NEBULA node
WITHOUT editing nebula_v10_11.py.  Same pattern as group 5:

    import nebula_v10_11 as host
    import nebula_group33_install as g33
    g33.install(host)           # patch once, before the node is created
    node = host.NEBULAFullNode(...)
    node.group33.stats()        # everything the layer knows
    g33.uninstall(host)         # restore the host exactly as it was

Safety rules (from the guide):
  * Observe-only by default.  Nothing here ever rejects a block, a transaction
    or a peer message.  Every callback runs inside try/except; failures are
    counted in ``layer.errors`` and kept (bounded) in ``layer.error_log``.
  * Original host methods always run FIRST; the layer only looks at the result.
  * Consensus-sensitive classes (ValidatorSetManager, ChainSynchronizer) are
    report-only: their output never feeds back into block validation.
  * Secrets (mnemonics, WIF, private keys) are never written to stats or logs.

State kept by the service classes (insurance, launchpad, vesting, validators)
lives in RAM only and is NOT persisted by this layer.
"""
from __future__ import annotations

import functools
import logging
import threading
import time
from collections import deque
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group33 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group33")

__all__ = ["Layer33", "Layer33Config", "install", "uninstall", "is_installed"]


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
@dataclass
class Layer33Config:
    """Switches for the layer.  Defaults are the safe observe-only profile."""

    miner_address: str = ""            # BlockTemplateEngine payout address ("" = class default)
    prune_depth: int = 1000            # PrunedChainStorage: blocks to keep
    track_pruning: bool = True         # call prune_old_blocks on connect (bookkeeping counter only)
    rotate_validator_epochs: bool = True   # call ValidatorSetManager.rotate_epoch on connect (internal state only)
    enforce_eviction: bool = False     # True = really evict low-fee txs from the mempool
    evict_check_every: int = 50        # run the eviction check every N accepted submits
    max_error_log: int = 50            # bounded error history (RAM cap)
    p2p_attr_names: Tuple[str, ...] = ("p2p", "network", "p2p_node", "net", "peer_manager")


# ---------------------------------------------------------------------------
# Module-level registries used by the patched host methods
# ---------------------------------------------------------------------------
_MEMPOOL_LAYERS: Dict[int, "Layer33"] = {}
_P2P_LAYERS: Dict[int, "Layer33"] = {}
_LIVE_LAYERS: List["Layer33"] = []
_REGISTRY_LOCK = threading.RLock()

_KNOWN_MSG_TYPES = frozenset(
    v for k, v in vars(g.NetMsgType).items()
    if not k.startswith("_") and isinstance(v, str)
)


def _msg_type(msg: Any) -> str:
    """Best-effort extraction of the P2P message type from an unknown message shape."""
    raw: Any = None
    if isinstance(msg, dict):
        raw = msg.get("type") or msg.get("command") or msg.get("cmd")
    elif isinstance(msg, str):
        raw = msg
    else:
        for name in ("type", "command", "cmd", "msg_type"):
            raw = getattr(msg, name, None)
            if raw:
                break
    if isinstance(raw, bytes):
        raw = raw.decode("ascii", "ignore")
    raw = str(raw).strip().lower() if raw else ""
    return raw if raw in _KNOWN_MSG_TYPES else "other"


# ---------------------------------------------------------------------------
# The layer
# ---------------------------------------------------------------------------
class Layer33:
    """One object that owns every group33 service and the chain-listener hooks."""

    # (attribute name, factory(layer) -> instance).  Order matters: independent
    # services first, then the ones that need a mempool.
    def _service_table(self) -> List[Tuple[str, Callable[[], Any]]]:
        bc, mp, cfg = self.bc, self.mempool, self.config
        return [
            ("insurance",  lambda: g.InsuranceProtocol(bc)),
            ("launchpad",  lambda: g.Launchpad(bc)),
            ("vesting",    lambda: g.VestingManager(bc)),
            ("validators", lambda: g.ValidatorSetManager(bc)),
            ("template",   lambda: g.BlockTemplateEngine(bc, cfg.miner_address)),
            ("pruning",    lambda: g.PrunedChainStorage(bc, cfg.prune_depth)),
            ("fast_sync",  lambda: g.FastSyncManager(bc)),
            ("synchronizer", lambda: g.ChainSynchronizer(bc)),
            ("rbf",        lambda: g.RBFPolicy(self._need(mp, "mempool"))),
            ("cpfp",       lambda: g.CPFPAccelerator(self._need(mp, "mempool"), bc)),
            ("eviction",   lambda: g.MempoolEvictionPolicy(self._need(mp, "mempool"))),
            ("mnemonic_tool", lambda: g.MnemonicRecoveryTool()),
            ("paper_wallet",  lambda: g.PaperWalletImporter()),
            ("wallet_migration", lambda: g.WalletMigrationTool()),
        ]

    # (service attr, method, key in stats()) - read-only probes
    _PROBES: Tuple[Tuple[str, str, str], ...] = (
        ("insurance",  "insurance_stats",   "insurance"),
        ("launchpad",  "launchpad_stats",   "launchpad"),
        ("vesting",    "vesting_stats",     "vesting"),
        ("validators", "validator_set_info", "validators"),
        ("pruning",    "storage_info",      "pruning"),
        ("eviction",   "mempool_health",    "mempool_health"),
        ("synchronizer", "sync_status",     "sync"),
        ("fast_sync",  "best_snapshot",     "best_snapshot"),
    )

    def __init__(self, node: Any, config: Optional[Layer33Config] = None):
        self.node = node
        self.config = config or Layer33Config()
        self.errors = 0
        self.stats_: Dict[str, int] = {}
        self.error_log: deque = deque(maxlen=max(1, self.config.max_error_log))
        self.build_errors: Dict[str, str] = {}
        self.services: Dict[str, Any] = {}
        self.p2p_msgs: Dict[str, int] = {}
        self.template_stale = True
        self.last_connected_height: Optional[int] = None
        self.last_reorg: Optional[dict] = None
        self._lock = threading.RLock()
        self._p2p_ids: List[int] = []
        self._detached = False

        self.bc = getattr(node, "bc", None)
        self.mempool = getattr(self.bc, "mempool", None) or getattr(node, "mempool", None)

        # Services default to None so attribute access never raises.
        for name, _ in self._service_table():
            setattr(self, name, None)
        if self.bc is None:
            self._record_error("init", AttributeError("node has no .bc (blockchain)"))
            return
        self._build_services()
        self._register_hooks()

    # ----- internals -------------------------------------------------------
    @staticmethod
    def _need(obj: Any, what: str) -> Any:
        if obj is None:
            raise RuntimeError(f"{what} is not available on this node")
        return obj

    def _count(self, key: str, n: int = 1) -> None:
        with self._lock:
            self.stats_[key] = self.stats_.get(key, 0) + n

    def _record_error(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.error_log.append({"where": where, "error": f"{type(exc).__name__}: {exc}",
                                   "at": time.time()})
        log.warning("group33 %s failed: %s", where, exc)

    def _guard(self, where: str, fn: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
        """Run fn; never raise.  Failures are counted and logged."""
        try:
            return fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001 - the layer must never break the host
            self._record_error(where, exc)
            return default

    def _build_services(self) -> None:
        for name, factory in self._service_table():
            try:
                inst = factory()
            except Exception as exc:  # noqa: BLE001
                self.build_errors[name] = f"{type(exc).__name__}: {exc}"
                log.warning("group33 service %s not built: %s", name, exc)
                continue
            self.services[name] = inst
            setattr(self, name, inst)

    def _register_hooks(self) -> None:
        with _REGISTRY_LOCK:
            if self.mempool is not None:
                _MEMPOOL_LAYERS[id(self.mempool)] = self
            _LIVE_LAYERS.append(self)

    def register_p2p(self, p2p: Any) -> bool:
        """Attach a P2P object so patched message handlers can report to this layer."""
        if p2p is None or not hasattr(p2p, "_handle_message"):
            return False
        with _REGISTRY_LOCK:
            _P2P_LAYERS[id(p2p)] = self
            self._p2p_ids.append(id(p2p))
        return True

    def discover_p2p(self) -> int:
        """Look for a P2P object on the node using the configured attribute names."""
        found = 0
        for attr in self.config.p2p_attr_names:
            if self.register_p2p(getattr(self.node, attr, None)):
                found += 1
        return found

    # ----- chain listener interface (bc.add_listener(layer)) ---------------
    def on_connect(self, block: Any) -> None:
        self._count("blocks_connected")
        self.last_connected_height = getattr(block, "height", self.last_connected_height)
        self.template_stale = True
        if self.config.track_pruning and self.pruning is not None:
            pruned = self._guard("pruning.prune_old_blocks", self.pruning.prune_old_blocks, default=0)
            if pruned:
                self._count("blocks_marked_pruned", int(pruned))
        if self.config.rotate_validator_epochs and self.validators is not None:
            before = list(getattr(self.validators, "_active_set", []))
            after = self._guard("validators.rotate_epoch", self.validators.rotate_epoch, default=before)
            if after is not None and list(after) != before:
                self._count("validator_rotations")

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        self._count("reorgs_seen")
        self.template_stale = True
        self.last_reorg = {
            "ancestor_height": ancestor_height,
            "old_len": self._safe_len(old),
            "new_len": self._safe_len(new),
            "at": time.time(),
        }

    @staticmethod
    def _safe_len(obj: Any) -> int:
        try:
            return len(obj)
        except Exception:  # noqa: BLE001
            return -1

    # ----- hooks called from the patched host methods ----------------------
    def observe_submit(self, result: Any) -> None:
        ok = bool(result[0]) if isinstance(result, (tuple, list)) and result else bool(result)
        self._count("mempool_submit_total")
        self._count("mempool_submit_accepted" if ok else "mempool_submit_rejected")
        if not ok or not self.config.enforce_eviction or self.eviction is None:
            return
        every = max(1, self.config.evict_check_every)
        if self.stats_.get("mempool_submit_accepted", 0) % every == 0:
            evicted = self._guard("eviction.evict_if_needed", self.eviction.evict_if_needed, default=0)
            if evicted:
                self._count("mempool_evicted", int(evicted))

    def observe_p2p(self, peer: Any, msg: Any) -> None:
        kind = _msg_type(msg)
        with self._lock:
            self.p2p_msgs[kind] = self.p2p_msgs.get(kind, 0) + 1

    # ----- mining helpers ---------------------------------------------------
    def get_template(self, extra_data: bytes = b"") -> Optional[dict]:
        """Build (or rebuild when stale) a block template.  Returns None on failure."""
        if self.template is None:
            return None
        if self.template_stale or extra_data:
            tpl = self._guard("template.build_template", self.template.build_template, extra_data)
            if tpl is not None:
                self.template_stale = False
            return tpl
        return self._guard("template.current", lambda: self.template._current_template)

    def get_stratum_job(self, clean: bool = False) -> Optional[Any]:
        if self.template is None:
            return None
        if self.template_stale and self.get_template() is None:
            return None
        return self._guard("template.to_stratum_job", self.template.to_stratum_job, clean)

    # ----- wallet-side helpers (secrets are returned to the caller only) ----
    def check_mnemonic(self, mnemonic: str) -> Tuple[bool, str]:
        if self.mnemonic_tool is None:
            return False, "mnemonic tool unavailable"
        return self._guard("mnemonic_tool.check_mnemonic", self.mnemonic_tool.check_mnemonic,
                           mnemonic, default=(False, "internal error"))

    def derive_addresses(self, mnemonic: str, count: int = 20) -> List[dict]:
        if self.mnemonic_tool is None:
            return []
        rows = self._guard("mnemonic_tool.derive_addresses", self.mnemonic_tool.derive_addresses,
                           mnemonic, count, default=[])
        return rows or []

    def import_wif(self, wif: str) -> Tuple[bool, dict]:
        if self.paper_wallet is None:
            return False, {"error": "paper wallet importer unavailable"}
        return self._guard("paper_wallet.from_wif", self.paper_wallet.from_wif, wif,
                           default=(False, {"error": "internal error"}))

    def import_privkey_hex(self, hex_key: str) -> Tuple[bool, dict]:
        if self.paper_wallet is None:
            return False, {"error": "paper wallet importer unavailable"}
        return self._guard("paper_wallet.from_privkey_hex", self.paper_wallet.from_privkey_hex,
                           hex_key, default=(False, {"error": "internal error"}))

    def new_paper_wallet(self) -> Optional[dict]:
        if self.paper_wallet is None:
            return None
        return self._guard("paper_wallet.generate_paper_wallet", self.paper_wallet.generate_paper_wallet)

    def export_watch_only(self, wallet: Any) -> Optional[dict]:
        if self.wallet_migration is None:
            return None
        return self._guard("wallet_migration.export_watch_only",
                           self.wallet_migration.export_watch_only, wallet)

    def export_encrypted(self, wallet: Any, password: str) -> Optional[dict]:
        if self.wallet_migration is None:
            return None
        return self._guard("wallet_migration.export_encrypted",
                           self.wallet_migration.export_encrypted, wallet, password)

    # ----- reporting --------------------------------------------------------
    def stats(self) -> dict:
        """Read-only snapshot.  Never contains keys, mnemonics or other secrets."""
        with self._lock:
            out: Dict[str, Any] = {
                "errors": self.errors,
                "counters": dict(self.stats_),
                "p2p_messages": dict(self.p2p_msgs),
                "services": sorted(self.services),
                "build_errors": dict(self.build_errors),
                "last_connected_height": self.last_connected_height,
                "last_reorg": dict(self.last_reorg) if self.last_reorg else None,
                "template_stale": self.template_stale,
                "enforce_eviction": self.config.enforce_eviction,
            }
        for attr, method, key in self._PROBES:
            svc = self.services.get(attr)
            if svc is not None:
                out[key] = self._guard(f"{attr}.{method}", getattr(svc, method))
        return out

    def detach(self) -> None:
        """Remove this layer from the chain and from every registry."""
        if self._detached:
            return
        self._detached = True
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer33.detach", exc_info=True)
        with _REGISTRY_LOCK:
            if self.mempool is not None and _MEMPOOL_LAYERS.get(id(self.mempool)) is self:
                del _MEMPOOL_LAYERS[id(self.mempool)]
            for pid in self._p2p_ids:
                if _P2P_LAYERS.get(pid) is self:
                    del _P2P_LAYERS[pid]
            self._p2p_ids.clear()
            if self in _LIVE_LAYERS:
                _LIVE_LAYERS.remove(self)


# ---------------------------------------------------------------------------
# install / uninstall
# ---------------------------------------------------------------------------
def is_installed(host: Any) -> bool:
    cls = getattr(host, "NEBULAFullNode", None)
    return bool(cls is not None and getattr(cls, "_g33_orig", None))


def _patch_method(cls: Any, name: str, make_wrapper: Callable[[Callable], Callable]) -> None:
    """Replace cls.<name> with a wrapper; the original is kept on the class."""
    stash = f"_g33_orig_{name}"
    if cls is None or not hasattr(cls, name) or getattr(cls, stash, None):
        return
    orig = getattr(cls, name)
    setattr(cls, stash, orig)
    setattr(cls, name, make_wrapper(orig))


def _unpatch_method(cls: Any, name: str) -> None:
    stash = f"_g33_orig_{name}"
    orig = getattr(cls, stash, None) if cls is not None else None
    if orig is not None:
        setattr(cls, name, orig)
        delattr(cls, stash)


def install(host: Any, config: Optional[Layer33Config] = None) -> bool:
    """Patch the host module.  Safe to call twice.  Returns True when active."""
    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is None:
        log.error("group33 install: host has no NEBULAFullNode")
        return False
    if getattr(node_cls, "_g33_orig", None):
        return True

    orig_init = node_cls.__init__

    @functools.wraps(orig_init)
    def patched_init(self: Any, *a: Any, **k: Any) -> None:
        orig_init(self, *a, **k)                       # the host always starts first
        try:
            layer = Layer33(self, config)
            self.group33 = layer
            bc = getattr(self, "bc", None)
            if bc is not None and hasattr(bc, "add_listener"):
                bc.add_listener(layer)
            layer.discover_p2p()
        except Exception as exc:  # noqa: BLE001 - the node must still start
            self.group33_error = exc
            log.warning("group33 layer failed to attach: %s", exc)

    node_cls._g33_orig = orig_init
    node_cls.__init__ = patched_init

    def wrap_submit(orig: Callable) -> Callable:
        @functools.wraps(orig)
        def submit(self: Any, *a: Any, **k: Any) -> Any:
            result = orig(self, *a, **k)               # original first; its exceptions propagate
            layer = _MEMPOOL_LAYERS.get(id(self))
            if layer is not None:
                layer._guard("observe_submit", layer.observe_submit, result)
            return result
        return submit

    def wrap_handle_message(orig: Callable) -> Callable:
        @functools.wraps(orig)
        def handle(self: Any, peer: Any, msg: Any, *a: Any, **k: Any) -> Any:
            result = orig(self, peer, msg, *a, **k)
            layer = _P2P_LAYERS.get(id(self))
            if layer is not None:
                layer._guard("observe_p2p", layer.observe_p2p, peer, msg)
            return result
        return handle

    _patch_method(getattr(host, "Mempool", None), "submit", wrap_submit)
    _patch_method(getattr(host, "P2PNode", None), "_handle_message", wrap_handle_message)
    return True


def uninstall(host: Any) -> None:
    """Restore the host exactly as before and detach every live layer."""
    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is not None:
        orig = getattr(node_cls, "_g33_orig", None)
        if orig is not None:
            node_cls.__init__ = orig
            del node_cls._g33_orig
    _unpatch_method(getattr(host, "Mempool", None), "submit")
    _unpatch_method(getattr(host, "P2PNode", None), "_handle_message")
    with _REGISTRY_LOCK:
        layers = list(_LIVE_LAYERS)
    for layer in layers:
        layer.detach()
    with _REGISTRY_LOCK:
        _MEMPOOL_LAYERS.clear()
        _P2P_LAYERS.clear()
