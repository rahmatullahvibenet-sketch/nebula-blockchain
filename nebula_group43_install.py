"""nebula_group43_install.py
=====================================================================
NEBULA group43 - د ۲۰ مړو کلاسونو د وصلولو Layer (د ډلې ۵ په څېر).

اصول (د لارښود له مخې):
  * په nebula_v10_11.py کې هېڅ شی نه ایډیټیږي. ټول بدلونونه د install(host) له لارې
    په memory کې کېږي او uninstall(host) هرڅه لکه مخکې کوي.
  * Layer هېڅکله بلاک یا tx نه رد کوي. هر callback په try/except کې دی؛ تېروتنې په
    layer.errors کې شمېرل کیږي.
  * ډیفالټ حالت "observe" (یوازې کتل/شمېرل) دی. "active" یوازې هغه وخت چې تاسو
    په څرګنده ورکړئ: install(host, mode="active").
  * هغه کلاسونه چې کیلي/مندرجات جوړوي (MultiChainWallet, MobileSDK) په پیل کې نه
    جوړیږي؛ یوازې کله چې تاسو غوښتنه وکړئ (lazy).

کارول:
    import nebula_v10_11 as host            # یا: host = sys.modules['__main__']
    import nebula_group43_install as g43
    g43.install(host)                        # observe mode
    node = host.NEBULAFullNode(...)          # node.group43 اوس شته
    node.group43.status()                    # د ټولو برخو حالت
    g43.uninstall(host)                      # بیرته لکه مخکې
"""
from __future__ import annotations

import logging
import threading
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group43 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

_log = logging.getLogger("nebula.group43")

# هغه نومونه چې د group43 کلاسونه یې د host څخه غواړي. install پر مهال د ژوندي host
# څخه دلته بیا تړل کیږي، ترڅو د class identity سمه وي (مثلاً که host د __main__ په توګه چلیږي).
HOST_DEPENDENCIES = (
    "BIP39", "HDKey", "NEBULABlockchain", "NEBULAWallet", "Script", "Secp256k1",
    "TxBuilder", "ProtocolUpgrade", "ProtocolUpgradeC", "L2Type", "C",
)

# د هغو ځانګړتیاوو نومونه چې node کې د اختیاري سرچینو لپاره لټول کیږي.
_OPTIONAL_NODE_ATTRS = {
    "oracle":   ("oracle", "oracle_v2", "price_oracle"),
    "dex":      ("dex", "nebula_dex"),
    "registry": ("nft_registry", "nbl721_registry", "nbl721", "nft"),
    "venbl":    ("venbl", "ve_nbl"),
    "treasury": ("treasury", "nebula_treasury"),
    "ipfs":     ("ipfs", "ipfs_client"),
    "order_book_mgr": ("order_book_mgr", "orderbook", "order_books"),
    "aggregator": ("aggregator", "defi_aggregator"),
}


def _find(node: Any, key: str) -> Any:
    for name in _OPTIONAL_NODE_ATTRS.get(key, ()):
        val = getattr(node, name, None)
        if val is not None:
            return val
    return None


def bind_host(host: Any) -> Dict[str, bool]:
    """د ژوندي host نومونه په group43 ماډل کې وتړئ. بیرته: کوم نومونه وموندل شول."""
    found: Dict[str, bool] = {}
    for name in HOST_DEPENDENCIES:
        if hasattr(host, name):
            setattr(g, name, getattr(host, name))
            found[name] = True
        else:
            found[name] = hasattr(g, name)
    return found


class Layer43:
    """د group43 ټول کلاسونه په یوه ځای کې، د node.group43 په توګه."""

    MODE_OBSERVE = "observe"
    MODE_ACTIVE = "active"

    def __init__(self, node: Any, mode: str = MODE_OBSERVE):
        if mode not in (self.MODE_OBSERVE, self.MODE_ACTIVE):
            raise ValueError("mode must be 'observe' or 'active'")
        self.node = node
        self.bc = getattr(node, "bc", None)
        self.mode = mode
        self._lock = threading.RLock()

        # شمېرنې
        self.errors = 0
        self.last_error: Optional[str] = None
        self.blocks_seen = 0
        self.reorgs_seen = 0
        self.txs_seen = 0
        self.fees_counted = 0
        self.last_height: Optional[int] = None

        # برخې
        self.components: Dict[str, Any] = {}
        self.component_errors: Dict[str, str] = {}
        self.skipped: Dict[str, str] = {}

        # lazy
        self.mobile_sdk: Optional[Any] = None
        self.multichain_wallet: Optional[Any] = None

        # ثابت ډولونه (Enum / dataclass / config) - جلا نه وصلیږي، یوازې د کارونې لپاره
        self.types = {
            "TriggerCondition": g.TriggerCondition,
            "AutomatedAction": g.AutomatedAction,
            "UpgradeStatus": g.UpgradeStatus,
            "ChainConfig": g.ChainConfig,
            "PositionType": g.PositionType,
            "DeFiPosition": g.DeFiPosition,
            "TraderProfile": g.TraderProfile,
        }

        self._build_components()

    # ---------------------------------------------------------------- errors
    def _err(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.last_error = f"{where}: {type(exc).__name__}: {exc}"
        _log.warning("group43 %s failed: %s", where, exc)

    # ------------------------------------------------------------ components
    def _build_components(self) -> None:
        bc = self.bc
        node = self.node

        def need_bc() -> Any:
            if bc is None:
                raise RuntimeError("node has no .bc (blockchain)")
            return bc

        def l2_bridge() -> Any:
            return g.Layer2Bridge("nebula-l2", g.Layer2Bridge.L2Type.OPTIMISTIC, need_bc())

        def nft() -> Any:
            reg = _find(node, "registry")
            if reg is None:
                raise LookupError("no NFT registry on node")
            return g.NFTCollectionAnalytics(reg)

        def router() -> Any:
            dex = _find(node, "dex")
            if dex is None:
                raise LookupError("no DEX on node")
            return g.SwapRouter(dex, _find(node, "order_book_mgr"), _find(node, "aggregator"))

        # (نوم، جوړونکی) - د لارښود د ګام ۴ ترتیب سره
        specs: List[Tuple[str, Callable[[], Any]]] = [
            ("social_trading",  lambda: g.SocialTradingPlatform(need_bc())),
            ("grant_dao",       lambda: g.GrantDAO(need_bc())),
            ("token_locker",    lambda: g.TokenLocker(need_bc())),
            ("defi_automation", lambda: g.DeFiAutomation(need_bc(), _find(node, "oracle"))),
            ("nft_analytics",   nft),
            ("swap_router",     router),
            ("fee_distributor", lambda: g.ProtocolFeeDistributor(
                need_bc(), _find(node, "venbl"), _find(node, "treasury"))),
            ("da_layer",        lambda: g.DataAvailabilityLayer(need_bc(), _find(node, "ipfs"))),
            ("l2_bridge",       l2_bridge),
            ("upgrade_manager", lambda: g.ProtocolUpgradeManager(need_bc())),
            ("emergency_dao",   lambda: g.EmergencyDAO(need_bc())),
        ]
        for name, factory in specs:
            try:
                self.components[name] = factory()
            except LookupError as e:          # د اختیاري سرچینې نشتوالی تېروتنه نه ده
                self.skipped[name] = str(e)
            except Exception as e:            # یو کلاس ماتیږي، نور دوام کوي
                self.component_errors[name] = f"{type(e).__name__}: {e}"
                self._err(f"build {name}", e)

    def __getattr__(self, name: str) -> Any:
        # layer.grant_dao  ->  layer.components["grant_dao"]
        comps = self.__dict__.get("components")
        if comps is not None and name in comps:
            return comps[name]
        raise AttributeError(name)

    # ------------------------------------------------------------ lazy parts
    def get_mobile_sdk(self, network: str = "mainnet") -> Any:
        """MobileSDK یوازې د غوښتنې پر مهال جوړیږي (کیف پول جوړولی شي)."""
        with self._lock:
            if self.mobile_sdk is None:
                self.mobile_sdk = g.MobileSDK(blockchain=self.bc, network=network)
            return self.mobile_sdk

    def new_multichain_wallet(self, mnemonic: Optional[str] = None) -> Any:
        """MultiChainWallet یوازې د غوښتنې پر مهال. mnemonic هېڅ ځای نه ساتل کیږي."""
        return g.MultiChainWallet(mnemonic)

    # --------------------------------------------------- chain listener hooks
    def on_connect(self, block: Any) -> None:
        try:
            h = getattr(block, "height", None)
            if h is None and self.bc is not None:
                h = getattr(self.bc, "height", None)
            with self._lock:
                self.blocks_seen += 1
                self.last_height = h
            if self.mode == self.MODE_ACTIVE:
                self._active_tick()
        except Exception as e:
            self._err("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        try:
            with self._lock:
                self.reorgs_seen += 1
        except Exception as e:
            self._err("on_reorg", e)

    def _active_tick(self) -> None:
        """یوازې active mode کې: هغه دوره یي کتنې چې کلاسونه یې لري."""
        auto = self.components.get("defi_automation")
        if auto is not None:
            try:
                auto.check_and_execute()
            except Exception as e:
                self._err("defi_automation.check_and_execute", e)
        upg = self.components.get("upgrade_manager")
        if upg is not None:
            try:
                upg.check_activations()
            except Exception as e:
                self._err("upgrade_manager.check_activations", e)

    # ---------------------------------------------------------- mempool hook
    def observe_tx(self, tx: Any, result: Any) -> None:
        """د Mempool.submit وروسته؛ پایله هېڅکله نه بدلوي."""
        try:
            accepted = bool(result[0]) if isinstance(result, tuple) and result else bool(result)
            with self._lock:
                self.txs_seen += 1
            if not accepted:
                return
            fee = getattr(tx, "fee", 0)
            if callable(fee):
                fee = fee()
            fee = int(fee or 0)
            dist = self.components.get("fee_distributor")
            if dist is not None and fee > 0:
                dist.accumulate_fees(fee)
                with self._lock:
                    self.fees_counted += fee
        except Exception as e:
            self._err("observe_tx", e)

    # ----------------------------------------------------------------- status
    _STATS = (
        ("social_trading",  "social_trading_stats"),
        ("grant_dao",       "dao_stats"),
        ("token_locker",    "locker_stats"),
        ("defi_automation", "automation_stats"),
        ("swap_router",     "router_stats"),
        ("fee_distributor", "fee_stats"),
        ("da_layer",        "da_stats"),
        ("l2_bridge",       "l2_stats"),
        ("upgrade_manager", "upgrade_stats"),
        ("emergency_dao",   "active_proposals"),
    )

    def status(self) -> dict:
        stats: Dict[str, Any] = {}
        for comp, method in self._STATS:
            obj = self.components.get(comp)
            if obj is None:
                continue
            try:
                stats[comp] = getattr(obj, method)()
            except Exception as e:
                stats[comp] = f"error: {type(e).__name__}: {e}"
        nft = self.components.get("nft_analytics")
        if nft is not None:
            stats["nft_analytics"] = "ready (use .collection_stats(collection_id))"
        with self._lock:
            return {
                "mode": self.mode,
                "errors": self.errors,
                "last_error": self.last_error,
                "blocks_seen": self.blocks_seen,
                "reorgs_seen": self.reorgs_seen,
                "last_height": self.last_height,
                "txs_seen": self.txs_seen,
                "fees_counted": self.fees_counted,
                "components": sorted(self.components),
                "component_errors": dict(self.component_errors),
                "skipped": dict(self.skipped),
                "stats": stats,
            }

    # ----------------------------------------------------------------- detach
    def detach(self) -> None:
        try:
            self.node.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer43.detach", exc_info=True)
        try:
            _LAYERS.remove(self)
        except ValueError:
            _NB_SWALLOW_LOG.debug("swallowed ValueError in Layer43.detach", exc_info=True)


# د Mempool hook لپاره ژوندي layers
_LAYERS: List[Layer43] = []
_LAYERS_LOCK = threading.Lock()


def install(host: Any, mode: str = Layer43.MODE_OBSERVE) -> Dict[str, Any]:
    """Layer د NEBULAFullNode.__init__ او Mempool.submit له لارې وصل کړئ.

    د ډیرو ځلونو چلول بې ضرره دي (دوهم ځل هېڅ نه کوي).
    """
    report: Dict[str, Any] = {"installed": False, "mempool_hook": False, "deps": {}}
    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is None:
        raise RuntimeError("host has no NEBULAFullNode")
    if getattr(node_cls, "_g43_orig", None):
        report["installed"] = True
        report["note"] = "already installed"
        return report

    report["deps"] = bind_host(host)

    orig_init = node_cls.__init__

    def patched_init(self, *a, **k):
        orig_init(self, *a, **k)
        try:
            layer = Layer43(self, mode)
            self.group43 = layer
            if getattr(self, "bc", None) is not None:
                self.bc.add_listener(layer)
            with _LAYERS_LOCK:
                _LAYERS.append(layer)
        except Exception as e:                      # نود باید لا هم پیل شي
            self.group43_error = e
            _log.warning("group43 install failed on node: %s", e)

    node_cls._g43_orig = orig_init
    node_cls.__init__ = patched_init
    report["installed"] = True

    # Mempool.submit(tx) -> (ok, reason): یوازې کتل، پایله نه بدلیږي
    mp = getattr(host, "Mempool", None)
    submit = getattr(mp, "submit", None) if mp is not None else None
    if submit is not None and not getattr(mp, "_g43_submit_orig", None):
        def patched_submit(self, tx, *a, **k):
            result = submit(self, tx, *a, **k)
            try:
                with _LAYERS_LOCK:
                    layers = list(_LAYERS)
                for layer in layers:
                    layer.observe_tx(tx, result)
            except Exception:                        # هېڅکله tx نه رد کوو
                _NB_SWALLOW_LOG.debug("swallowed Exception in install.patched_submit", exc_info=True)
            return result

        mp._g43_submit_orig = submit
        mp.submit = patched_submit
        report["mempool_hook"] = True
    return report


def uninstall(host: Any) -> bool:
    """هرڅه لکه مخکې. بیرته: ریښتیا که څه بدل شوي وو."""
    changed = False
    node_cls = getattr(host, "NEBULAFullNode", None)
    orig = getattr(node_cls, "_g43_orig", None) if node_cls is not None else None
    if orig:
        node_cls.__init__ = orig
        del node_cls._g43_orig
        changed = True
    mp = getattr(host, "Mempool", None)
    msub = getattr(mp, "_g43_submit_orig", None) if mp is not None else None
    if msub:
        mp.submit = msub
        del mp._g43_submit_orig
        changed = True
    with _LAYERS_LOCK:
        layers = list(_LAYERS)
        _LAYERS.clear()
    for layer in layers:
        try:
            layer.node.bc._listeners.remove(layer)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in uninstall", exc_info=True)
    return changed
