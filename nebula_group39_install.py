"""NEBULA group39 - install / uninstall wrapper (same pattern as group5).

Usage (after nebula_v10_11.py is importable):

    import nebula_v10_11 as host
    import nebula_group39_install as g39
    g39.install(host)        # every NEBULAFullNode created afterwards gets node.group39
    ...
    g39.uninstall(host)      # restores the original __init__

Nothing in nebula_v10_11.py or nebula_group39.py is edited.
A failure inside the layer is stored in ``node.group39_error`` / ``layer.errors``
and the node still starts normally.
"""
from __future__ import annotations

from typing import Any, Optional

from nebula_group39_chain import Group39Chain
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

_POS_ATTRS = ("pos_engine", "pos", "_pos", "pos_eng")
_TREASURY_ATTRS = ("treasury", "nebula_treasury", "_treasury")


def _first_attr(obj: Any, names) -> Optional[Any]:
    for name in names:
        value = getattr(obj, name, None)
        if value is not None:
            return value
    return None


class Layer39:
    """Blockchain listener that feeds the group39 chain.

    Listener contract (verified in the host according to the guide):
    ``bc.add_listener(layer)`` -> ``layer.on_connect(block)`` and
    ``layer.on_reorg(old, new, ancestor_height)``.
    """

    def __init__(self, node, report_only: bool = True):
        self.node = node
        self._extra_errors = 0
        self.chain = Group39Chain(
            node.bc,
            pos_engine=_first_attr(node, _POS_ATTRS),
            treasury=_first_attr(node, _TREASURY_ATTRS),
            report_only=report_only,
        )

    @property
    def errors(self) -> int:
        return self.chain.errors + self._extra_errors

    def on_connect(self, block) -> None:
        try:
            self.chain.on_block_connected(block)
        except Exception:  # noqa: BLE001 - never break block connection
            self._extra_errors += 1

    def on_reorg(self, old, new, ancestor_height) -> None:
        try:
            self.chain.on_block_reorged(old, new, ancestor_height)
        except Exception:  # noqa: BLE001
            self._extra_errors += 1

    def stats(self) -> dict:
        data = self.chain.stats()
        data["layer_errors"] = self._extra_errors
        return data

    def detach(self) -> None:
        try:
            self.node.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer39.detach", exc_info=True)


def install(host, report_only: bool = True) -> None:
    """Wrap NEBULAFullNode.__init__ so each new node gets ``node.group39``."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g39_orig", None):
        return
    orig = cls.__init__

    def patched(self, *args, **kwargs):
        orig(self, *args, **kwargs)
        try:
            self.group39 = Layer39(self, report_only=report_only)
            self.bc.add_listener(self.group39)
        except Exception as exc:  # noqa: BLE001 - the node must still start
            self.group39_error = exc

    cls._g39_orig = orig
    cls.__init__ = patched


def uninstall(host) -> None:
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g39_orig", None)
    if orig:
        cls.__init__ = orig
        del cls._g39_orig
