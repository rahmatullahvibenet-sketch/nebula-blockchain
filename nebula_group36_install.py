"""
nebula_group36_install.py - wiring layer for the 20 group36 classes.

Design rules (same as group5):
  * NOTHING inside nebula_v10_11.py is edited.
  * NEBULAFullNode.__init__ is wrapped; the original always runs first.
  * Every callback is wrapped in try/except. A failure here can NEVER reject
    a block or a transaction. Failures are counted in layer.errors.
  * install(host) is idempotent, uninstall(host) restores the original methods.

What gets wired (all against the LIVE chain `node.bc`):
  Chain listener (on_connect / on_reorg):
      ChainAlertSystem           -> receives every connected block
      NEBULAFullNodeV2           -> opt-in only, receives every connected block
  Contract / economy services (kept on node.group36.<name>):
      YieldFarmingV2             -> .farming
      DeFiInsurance              -> .insurance
      TokenLaunchpad             -> .launchpad
      NEBULADao                  -> .dao
      ConcentratedLiquidityPool  -> .pools (registry, create with create_pool)
      NFTRental                  -> .nft_rental
      NFTFractionalizer          -> .nft_fractionalizer
  P2P observer (read-only, original handler always runs first):
      CrossChainRouter           -> .cross_chain  (+ message counters)
  Wallet side:
      HDWalletV2                 -> .get_hd_wallet()  (lazy; never exposes the mnemonic)
  Data types used by the services above (verified present by .verify()):
      LaunchpadStatus, FarmPool, FarmPosition, LiquidityPosition, DAOTier,
      DAOMember, CrossChainMessageType, CrossChainMessage, PeerDiscoveryMethod
"""
from __future__ import annotations

import threading
import time
import traceback
from collections import deque
from typing import Any, Callable, Dict, List, Optional

import nebula_group36 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

GROUP36_CLASSES = (
    "LaunchpadStatus", "TokenLaunchpad", "FarmPool", "FarmPosition",
    "YieldFarmingV2", "DeFiInsurance", "LiquidityPosition",
    "ConcentratedLiquidityPool", "NFTRental", "NFTFractionalizer",
    "DAOTier", "DAOMember", "NEBULADao", "ChainAlertSystem",
    "NEBULAFullNodeV2", "CrossChainMessageType", "CrossChainMessage",
    "CrossChainRouter", "HDWalletV2", "PeerDiscoveryMethod",
)

# Held while NEBULAFullNodeV2 is being built against the live chain.
_SHIM_LOCK = threading.Lock()


class Layer36:
    """Holds every group36 object and receives chain / P2P events."""

    MAX_ERROR_LOG = 50

    def __init__(self, node: Any, enable_full_node_v2: bool = False):
        self.node = node
        self.bc = getattr(node, "bc", None) or getattr(node, "blockchain", None)
        self.errors = 0
        self.error_log: deque = deque(maxlen=self.MAX_ERROR_LOG)
        self.stats_: Dict[str, Any] = {
            "blocks_seen": 0,
            "reorgs": 0,
            "last_height": None,
            "p2p_messages": 0,
            "p2p_by_kind": {},
            "installed_at": time.time(),
        }
        self._lock = threading.RLock()
        self.attached = False
        self._hd_wallet = None
        self.pools: Dict[str, Any] = {}
        self.full_node_v2 = None

        if self.bc is None:
            self._record_error("init", RuntimeError("node has no .bc / .blockchain"))

        # Services that need the live blockchain
        self.farming = self._build("YieldFarmingV2", lambda: g.YieldFarmingV2(self.bc), True)
        self.insurance = self._build("DeFiInsurance", lambda: g.DeFiInsurance(self.bc), True)
        self.launchpad = self._build("TokenLaunchpad", lambda: g.TokenLaunchpad(self.bc), True)
        self.dao = self._build("NEBULADao",
                               lambda: g.NEBULADao(self.bc, self._live_treasury()), True)
        self.cross_chain = self._build("CrossChainRouter", lambda: g.CrossChainRouter(self.bc), True)
        self.alerts = self._build("ChainAlertSystem", lambda: g.ChainAlertSystem(self.bc), False)

        # Standalone services
        self.nft_rental = self._build("NFTRental", lambda: g.NFTRental(), False)
        self.nft_fractionalizer = self._build("NFTFractionalizer", lambda: g.NFTFractionalizer(), False)

        if enable_full_node_v2:
            self.build_full_node_v2()

    # ------------------------------------------------------------------ helpers
    def _live_treasury(self) -> Optional[Any]:
        """Return node.treasury only if it is a real NEBULATreasury, else None."""
        t = getattr(self.node, "treasury", None)
        cls = getattr(g, "NEBULATreasury", None)
        return t if (t is not None and isinstance(cls, type) and isinstance(t, cls)) else None

    def _record_error(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.error_log.append({
                "where": where,
                "error": f"{type(exc).__name__}: {exc}",
                "at": time.time(),
                "trace": traceback.format_exc(limit=4),
            })

    def _build(self, name: str, factory: Callable[[], Any], needs_chain: bool) -> Any:
        if needs_chain and self.bc is None:
            self._record_error(f"build:{name}", RuntimeError("no blockchain available"))
            return None
        try:
            return factory()
        except Exception as e:
            self._record_error(f"build:{name}", e)
            return None

    # ------------------------------------------------------------ attach/detach
    def attach(self) -> bool:
        """Register on the chain listener list and tag P2P objects."""
        if self.attached:
            return True
        ok = False
        try:
            if self.bc is not None and hasattr(self.bc, "add_listener"):
                self.bc.add_listener(self)
                ok = True
            else:
                raise AttributeError("blockchain has no add_listener")
        except Exception as e:
            self._record_error("attach:listener", e)
        self._tag_p2p_objects()
        self.attached = ok
        return ok

    def _tag_p2p_objects(self) -> None:
        """Mark every P2PNode held by the node so the P2P observer can find us."""
        try:
            import sys
            host = None
            for mod_name in ("nebula_v10_11", "__main__"):
                m = sys.modules.get(mod_name)
                if m is not None and hasattr(m, "P2PNode"):
                    host = m
                    break
            p2p_cls = getattr(host, "P2PNode", None) if host else None
            if p2p_cls is None:
                return
            for value in list(vars(self.node).values()):
                if isinstance(value, p2p_cls):
                    value._g36_layer = self
        except Exception as e:
            self._record_error("attach:p2p", e)

    def detach(self) -> None:
        try:
            if self.bc is not None:
                if hasattr(self.bc, "remove_listener"):
                    self.bc.remove_listener(self)
                else:
                    self.bc._listeners.remove(self)
        except ValueError:
            _NB_SWALLOW_LOG.debug("swallowed ValueError in Layer36.detach", exc_info=True)
        except Exception as e:
            self._record_error("detach", e)
        self.attached = False

    # --------------------------------------------------------- chain listener
    def on_connect(self, block: Any) -> None:
        try:
            with self._lock:
                self.stats_["blocks_seen"] += 1
                self.stats_["last_height"] = getattr(block, "height", None)
        except Exception as e:
            self._record_error("on_connect:stats", e)

        if self.alerts is not None:
            try:
                self.alerts.on_new_block(block)
            except Exception as e:
                self._record_error("on_connect:alerts", e)

        if self.full_node_v2 is not None:
            try:
                self.full_node_v2.on_new_block(block)
            except Exception as e:
                self._record_error("on_connect:full_node_v2", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        try:
            with self._lock:
                self.stats_["reorgs"] += 1
        except Exception as e:
            self._record_error("on_reorg:stats", e)
        if self.alerts is None:
            return
        try:
            level = getattr(g.AlertLevel, "WARNING")
            try:
                depth = len(old)
            except Exception:
                depth = None
            self.alerts.alert(level, f"Chain reorg above height {ancestor_height}",
                              {"ancestor_height": ancestor_height, "old_depth": depth})
        except Exception as e:
            self._record_error("on_reorg:alerts", e)

    # ------------------------------------------------------------ P2P observer
    def on_p2p_message(self, peer: Any, msg: Any) -> None:
        """Read-only observer. The original handler has already finished."""
        try:
            kind = "unknown"
            if isinstance(msg, dict):
                kind = str(msg.get("type") or msg.get("cmd") or msg.get("command") or "unknown")
            else:
                kind = str(getattr(msg, "type", None) or getattr(msg, "cmd", None)
                           or type(msg).__name__)
            with self._lock:
                self.stats_["p2p_messages"] += 1
                by_kind = self.stats_["p2p_by_kind"]
                if kind in by_kind or len(by_kind) < 64:   # hard cap on label count
                    by_kind[kind] = by_kind.get(kind, 0) + 1
        except Exception as e:
            self._record_error("on_p2p_message", e)

    # --------------------------------------------------------------- services
    def create_pool(self, pool_id: str, token_a: str, token_b: str,
                    initial_price: float, **kwargs: Any) -> Optional[Any]:
        """Create and register a ConcentratedLiquidityPool (kwargs: fee_bps)."""
        with self._lock:
            if pool_id in self.pools:
                return self.pools[pool_id]
            try:
                pool = g.ConcentratedLiquidityPool(pool_id, token_a, token_b,
                                                   initial_price, **kwargs)
            except Exception as e:
                self._record_error("create_pool", e)
                return None
            self.pools[pool_id] = pool
            return pool

    def get_hd_wallet(self, mnemonic: Optional[str] = None) -> Optional[Any]:
        """
        Lazy HDWalletV2. With no mnemonic a fresh random one is generated.
        The node's own wallet mnemonic is NEVER used implicitly.
        """
        with self._lock:
            if self._hd_wallet is None:
                try:
                    self._hd_wallet = g.HDWalletV2(mnemonic)
                except Exception as e:
                    self._record_error("get_hd_wallet", e)
                    return None
            return self._hd_wallet

    def build_full_node_v2(self, miner_address: str = "") -> Optional[Any]:
        """
        OPT-IN. Builds NEBULAFullNodeV2 on top of the LIVE chain and wallet.
        The class normally creates its own NEBULABlockchain and wallet; while it
        is constructed those two module names inside nebula_group36 are
        temporarily pointed at the live objects (restored in `finally`).
        Services this layer already owns are re-used, so state is not duplicated.
        """
        if self.full_node_v2 is not None:
            return self.full_node_v2
        live_bc = self.bc
        live_wallet = getattr(self.node, "wallet", None)
        if live_bc is None or live_wallet is None:
            self._record_error("build_full_node_v2",
                               RuntimeError("node needs .bc and .wallet"))
            return None

        class _WalletShim:
            @staticmethod
            def generate():
                return live_wallet

        with _SHIM_LOCK:
            saved_bc = g.__dict__.get("NEBULABlockchain")
            saved_wallet = g.__dict__.get("NEBULAWallet")
            g.NEBULABlockchain = lambda *a, **k: live_bc
            g.NEBULAWallet = _WalletShim
            try:
                nv2 = g.NEBULAFullNodeV2(miner_address=miner_address,
                                         enable_mining=False, enable_api=False)
            except Exception as e:
                self._record_error("build_full_node_v2", e)
                return None
            finally:
                g.NEBULABlockchain = saved_bc
                g.NEBULAWallet = saved_wallet

        # Single source of truth: reuse this layer's services.
        for attr, svc in (("yield_farming", self.farming), ("insurance", self.insurance),
                          ("launchpad", self.launchpad), ("dao", self.dao),
                          ("alerts", self.alerts)):
            if svc is not None:
                setattr(nv2, attr, svc)
        self.full_node_v2 = nv2
        return nv2

    # ----------------------------------------------------------------- reports
    def verify(self) -> Dict[str, bool]:
        """True for every one of the 20 classes that is importable from group36."""
        return {name: hasattr(g, name) for name in GROUP36_CLASSES}

    def snapshot(self) -> Dict[str, Any]:
        """Read-only statistics; each section is isolated so one failure is harmless."""
        out: Dict[str, Any] = {}
        sections = (
            ("farming", self.farming, "farm_stats"),
            ("insurance", self.insurance, "insurance_stats"),
            ("launchpad", self.launchpad, "launchpad_stats"),
            ("dao", self.dao, "dao_stats"),
            ("cross_chain", self.cross_chain, "router_stats"),
            ("nft_rental", self.nft_rental, "rental_stats"),
        )
        for key, svc, method in sections:
            if svc is None:
                out[key] = None
                continue
            try:
                out[key] = getattr(svc, method)()
            except Exception as e:
                self._record_error(f"snapshot:{key}", e)
                out[key] = None
        try:
            out["pools"] = {pid: p.pool_info() for pid, p in list(self.pools.items())}
        except Exception as e:
            self._record_error("snapshot:pools", e)
            out["pools"] = None
        with self._lock:
            out["layer"] = dict(self.stats_, errors=self.errors,
                                attached=self.attached,
                                full_node_v2=self.full_node_v2 is not None)
        return out


# ------------------------------------------------------------------- install
def _wrap_node_init(host: Any, enable_full_node_v2: bool) -> bool:
    cls = getattr(host, "NEBULAFullNode", None)
    if cls is None:
        return False
    if getattr(cls, "_g36_orig", None):
        return True
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)          # the original always runs first
        try:
            layer = Layer36(self, enable_full_node_v2=enable_full_node_v2)
            self.group36 = layer
            layer.attach()
        except Exception as e:       # the node must still start
            self.group36_error = e

    cls._g36_orig = orig
    cls.__init__ = patched
    return True


def _wrap_p2p(host: Any) -> bool:
    cls = getattr(host, "P2PNode", None)
    if cls is None or not hasattr(cls, "_handle_message"):
        return False
    if getattr(cls, "_g36_orig_handle", None):
        return True
    orig = cls._handle_message

    def patched(self, peer, msg, *a, **k):
        result = orig(self, peer, msg, *a, **k)   # original first, result untouched
        try:
            layer = getattr(self, "_g36_layer", None)
            if layer is not None:
                layer.on_p2p_message(peer, msg)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _wrap_p2p.patched", exc_info=True)
        return result

    cls._g36_orig_handle = orig
    cls._handle_message = patched
    return True


def install(host: Any, enable_full_node_v2: bool = False) -> Dict[str, bool]:
    """Wrap the host classes. Returns which hooks were installed."""
    return {
        "node_init": _wrap_node_init(host, enable_full_node_v2),
        "p2p_observer": _wrap_p2p(host),
    }


def uninstall(host: Any) -> None:
    cls = getattr(host, "NEBULAFullNode", None)
    if cls is not None:
        orig = getattr(cls, "_g36_orig", None)
        if orig:
            cls.__init__ = orig
            del cls._g36_orig
    p2p = getattr(host, "P2PNode", None)
    if p2p is not None:
        orig = getattr(p2p, "_g36_orig_handle", None)
        if orig:
            p2p._handle_message = orig
            del p2p._g36_orig_handle
