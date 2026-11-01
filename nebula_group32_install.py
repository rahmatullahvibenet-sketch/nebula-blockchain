"""NEBULA group32 - wiring layer (install / uninstall).

This module connects the 20 formerly dead classes of ``nebula_group32.py`` to the
running node WITHOUT editing the host file (nebula_v10_xx.py).

Design rules (taken from the group32 guide):
  * The layer is OBSERVER-ONLY. It never rejects a block or a transaction and it
    never changes consensus state.
  * Every callback is wrapped in try/except. Problems are counted in
    ``layer.errors`` and stored in ``layer.last_error``; they never propagate
    into the node.
  * ``install(host)`` patches ``NEBULAFullNode.__init__`` once (idempotent) and
    ``uninstall(host)`` restores the original constructor exactly.

Where each class lives after wiring (``node.group32`` is the Layer32 object):

    node.group32.vaults          MultisigVaultManager      (wallet side)
    node.group32.subscriptions   SubscriptionProtocol      (wallet side)
    node.group32.audit           AuditLogger               (security / monitoring)
    node.group32.vm              NEBULASmartContractVM     (contracts and economy)
    node.group32.escrow          EscrowService             (contracts and economy)
    node.group32.router          DeFiRouter                (contracts and economy, needs a DEX)
    node.group32.social          NEBULASocial              (social layer)
    node.group32.micropay        MicroPaymentNetwork       (off-chain channels)

Data classes, the enum and the exceptions (MultisigVault, AuditSeverity,
AuditEvent, VMError, VMGasExhausted, GasCosts, VMState, Subscription,
EscrowContract, SocialProfile, SocialPost, InsurancePolicy) are used by the
services above and are re-exported on the layer as ``layer.types``.
"""
from __future__ import annotations

import threading
import weakref
from typing import Any, Dict, List, Optional

import nebula_group32 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

__all__ = ["Layer32", "install", "uninstall", "bind_host", "SERVICE_CLASS_NAMES",
           "TYPE_CLASS_NAMES"]

# Classes that run as services and are instantiated by the layer.
SERVICE_CLASS_NAMES = (
    "MultisigVaultManager",
    "AuditLogger",
    "MicroPaymentNetwork",
    "NEBULASmartContractVM",
    "DeFiRouter",
    "SubscriptionProtocol",
    "EscrowService",
    "NEBULASocial",
)

# Classes that are data types / enum / exceptions used by the services.
TYPE_CLASS_NAMES = (
    "MultisigVault",
    "AuditSeverity",
    "AuditEvent",
    "VMError",
    "VMGasExhausted",
    "GasCosts",
    "VMState",
    "Subscription",
    "EscrowContract",
    "SocialProfile",
    "SocialPost",
    "InsurancePolicy",
)

# Live layers, so that an optional Mempool wrapper can notify all of them.
_LIVE_LAYERS: "weakref.WeakSet[Layer32]" = weakref.WeakSet()


def bind_host(host: Any) -> List[str]:
    """Copy names that the host defines and group32 lacks into the group32 module.

    group32 needs classes from other groups (ChannelUpdate, DecentralizedOracle,
    MicroChannel, MicroChannelUpdate, NEBULADex, PaymentChannel). Importing the
    host module is not enough when the host has a different module name than the
    one hard-coded in nebula_group32.py, so this function fills the gap for the
    host that is actually running. Names group32 already defines are never
    overwritten. Returns the list of names that were added.
    """
    added: List[str] = []
    namespace = vars(g)
    for name, value in vars(host).items():
        if name.startswith("__") or name in namespace:
            continue
        namespace[name] = value
        added.append(name)
    return added


class Layer32:
    """Observer layer that owns every group32 service for one node."""

    CHECKPOINT_INTERVAL = 144   # blocks between audit checkpoints

    def __init__(self, node: Any, enable_subscription_processing: bool = False):
        self.node = node
        self.errors = 0
        self.last_error: Optional[BaseException] = None
        self.init_errors: Dict[str, BaseException] = {}
        self.enable_subscription_processing = bool(enable_subscription_processing)
        self._lock = threading.RLock()
        self.stats_: Dict[str, int] = {
            "blocks_seen": 0,
            "reorgs_seen": 0,
            "checkpoints": 0,
            "audit_integrity_failures": 0,
            "subscriptions_processed": 0,
            "submits_seen": 0,
            "submits_accepted": 0,
        }
        self.types = {name: getattr(g, name) for name in TYPE_CLASS_NAMES}

        chain = getattr(node, "bc", None)
        self.vaults = self._build("MultisigVaultManager")
        self.audit = self._build("AuditLogger", chain)
        self.micropay = self._build("MicroPaymentNetwork", chain)
        self.vm = self._build("NEBULASmartContractVM")
        self.subscriptions = self._build("SubscriptionProtocol", chain)
        self.escrow = self._build("EscrowService", chain)
        self.social = self._build("NEBULASocial", chain)

        # DeFiRouter needs a DEX (and optionally an oracle) from another group.
        self.router = None
        dex = getattr(node, "dex", None)
        if dex is not None:
            self.attach_dex(dex, getattr(node, "oracle", None))

        _LIVE_LAYERS.add(self)

    # ------------------------------------------------------------------ helpers
    def _build(self, class_name: str, *args: Any) -> Any:
        """Instantiate one group32 class. A failure is recorded, never raised."""
        try:
            return getattr(g, class_name)(*args)
        except Exception as exc:  # noqa: BLE001 - the node must keep running
            self.init_errors[class_name] = exc
            self._record_error(exc)
            return None

    def _record_error(self, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.last_error = exc

    def attach_dex(self, dex: Any, oracle: Any = None) -> bool:
        """Create the DeFiRouter once a DEX object is available."""
        try:
            self.router = g.DeFiRouter(dex, oracle)
            return True
        except Exception as exc:  # noqa: BLE001
            self.init_errors["DeFiRouter"] = exc
            self._record_error(exc)
            return False

    def _audit(self, severity_name: str, category: str, action: str,
               details: Optional[dict] = None) -> None:
        """Write one audit event if the audit logger exists."""
        if self.audit is None:
            return
        severity = getattr(g.AuditSeverity, severity_name)
        self.audit.log(severity, category, "layer32", action, details or {})

    # ----------------------------------------------------------- chain listener
    def on_connect(self, block: Any) -> None:
        """Called by the chain after a block is connected."""
        try:
            with self._lock:
                self.stats_["blocks_seen"] += 1
                seen = self.stats_["blocks_seen"]
            height = getattr(getattr(self.node, "bc", None), "height", None)
            if height is None:
                height = getattr(block, "height", None)

            if self.enable_subscription_processing and self.subscriptions is not None:
                done = self.subscriptions.process_due()
                with self._lock:
                    self.stats_["subscriptions_processed"] += len(done)

            if height is not None and height % self.CHECKPOINT_INTERVAL == 0:
                self._checkpoint(height, seen)
        except Exception as exc:  # noqa: BLE001
            self._record_error(exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        """Called by the chain after a reorganisation."""
        try:
            with self._lock:
                self.stats_["reorgs_seen"] += 1
            self._audit("WARNING", "chain", "reorg", {
                "ancestor_height": ancestor_height,
                "old_length": _safe_len(old),
                "new_length": _safe_len(new),
            })
        except Exception as exc:  # noqa: BLE001
            self._record_error(exc)

    def _checkpoint(self, height: int, blocks_seen: int) -> None:
        ok, message = (True, "audit logger missing")
        if self.audit is not None:
            ok, message = self.audit.verify_integrity()
        with self._lock:
            self.stats_["checkpoints"] += 1
            if not ok:
                self.stats_["audit_integrity_failures"] += 1
        severity = "INFO" if ok else "CRITICAL"
        self._audit(severity, "chain", "checkpoint", {
            "height": height,
            "blocks_seen": blocks_seen,
            "audit_integrity": message,
        })

    # --------------------------------------------------------- mempool recording
    def record_submit(self, accepted: bool) -> None:
        """Record-only hook for Mempool.submit (never changes the result)."""
        try:
            with self._lock:
                self.stats_["submits_seen"] += 1
                if accepted:
                    self.stats_["submits_accepted"] += 1
        except Exception as exc:  # noqa: BLE001
            self._record_error(exc)

    # ------------------------------------------------------------------- status
    def stats(self) -> Dict[str, Any]:
        """Small status report for dashboards and tests."""
        services = {
            "vaults": self.vaults, "audit": self.audit, "micropay": self.micropay,
            "vm": self.vm, "subscriptions": self.subscriptions,
            "escrow": self.escrow, "social": self.social, "router": self.router,
        }
        report: Dict[str, Any] = dict(self.stats_)
        report["errors"] = self.errors
        report["services_up"] = sorted(k for k, v in services.items() if v is not None)
        report["services_down"] = sorted(k for k, v in services.items() if v is None)
        return report

    def detach(self) -> None:
        """Remove this layer from the chain's listener list."""
        try:
            self.node.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer32.detach", exc_info=True)
        _LIVE_LAYERS.discard(self)


def _safe_len(value: Any) -> Optional[int]:
    try:
        return len(value)
    except TypeError:
        return None


def _register_listener(node: Any, layer: Layer32) -> None:
    chain = node.bc
    add = getattr(chain, "add_listener", None)
    if callable(add):
        add(layer)
    else:
        chain._listeners.append(layer)


def install(host: Any, enable_subscription_processing: bool = False,
            wrap_mempool: bool = False) -> None:
    """Patch NEBULAFullNode.__init__ so every new node gets a Layer32.

    Safe to call twice. The node still starts when the layer fails; the failure
    is stored in ``node.group32_error``.
    """
    bind_host(host)
    node_class = host.NEBULAFullNode
    if getattr(node_class, "_g32_orig", None):
        return
    original_init = node_class.__init__

    def patched_init(self, *args: Any, **kwargs: Any) -> None:
        original_init(self, *args, **kwargs)
        try:
            self.group32 = Layer32(
                self, enable_subscription_processing=enable_subscription_processing)
            _register_listener(self, self.group32)
        except Exception as exc:  # noqa: BLE001 - the node must still start
            self.group32_error = exc

    node_class._g32_orig = original_init
    node_class.__init__ = patched_init

    if wrap_mempool:
        _wrap_mempool_submit(host)


def _wrap_mempool_submit(host: Any) -> None:
    """Optional record-only wrapper around Mempool.submit(tx) -> (ok, reason)."""
    mempool_class = getattr(host, "Mempool", None)
    if mempool_class is None or getattr(mempool_class, "_g32_submit_orig", None):
        return
    original_submit = mempool_class.submit

    def patched_submit(self, *args: Any, **kwargs: Any):
        result = original_submit(self, *args, **kwargs)
        try:
            accepted = bool(result[0]) if isinstance(result, tuple) else bool(result)
            for layer in list(_LIVE_LAYERS):
                layer.record_submit(accepted)
        except Exception:  # noqa: BLE001 - recording must never alter the result
            _NB_SWALLOW_LOG.debug("swallowed Exception in _wrap_mempool_submit.patched_submit", exc_info=True)
        return result

    mempool_class._g32_submit_orig = original_submit
    mempool_class.submit = patched_submit


def uninstall(host: Any) -> None:
    """Restore the original constructors. Existing nodes keep their layer."""
    node_class = host.NEBULAFullNode
    original_init = getattr(node_class, "_g32_orig", None)
    if original_init:
        node_class.__init__ = original_init
        del node_class._g32_orig

    mempool_class = getattr(host, "Mempool", None)
    original_submit = getattr(mempool_class, "_g32_submit_orig", None) if mempool_class else None
    if original_submit:
        mempool_class.submit = original_submit
        del mempool_class._g32_submit_orig
