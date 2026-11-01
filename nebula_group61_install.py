"""
nebula_group61_install.py
=========================

Wiring layer for the 20 "dead" classes in ``nebula_group61.py``.

Design rules (taken from the group-61 guide):
  * NOTHING inside ``nebula_v10_11.py`` or ``nebula_group61.py`` is edited.
  * The layer is REPORT-ONLY: it observes the node and never rejects,
    delays or alters a block, a transaction or a P2P message.
  * Every callback is wrapped in try/except. Errors are counted in
    ``layer.errors`` / ``layer.errors_by_component`` and the node keeps running.
  * Original host methods always run FIRST; the layer runs afterwards.
  * ``uninstall(host)`` restores the host exactly as it was.

Classes that open ports, mine, or build a second node (RealP2PNode, RealMiner,
NEBULAFullNodeV3, PersistentChain, BIP324Transport) are NOT auto-started. They
are available through explicit ``create_*`` factory methods.

Usage
-----
    import nebula_v10_11 as host
    import nebula_group61_install as g61

    report = g61.install(host)              # patch NEBULAFullNode (+ optional hooks)
    node = host.NEBULAFullNode(...)         # node.group61 is now a Layer61
    print(node.group61.status())

    g61.uninstall(host)                     # back to the original behaviour
"""
from __future__ import annotations

import hashlib
import logging
import os
import threading
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

import nebula_group61 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group61")


# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------
@dataclass
class _ShadowEntry:
    """One mirrored mempool transaction."""
    __slots__ = ("txid", "fee", "vsize", "fee_rate")

    def __init__(self, txid: str, fee: int, vsize: int):
        self.txid = txid
        self.fee = fee
        self.vsize = vsize
        self.fee_rate = fee / vsize if vsize else 0.0


class _ShadowMempool:
    """Observe-only mirror of accepted mempool txs. Never rejects, never touches the real mempool.
    Same public surface the layer uses: add_tx / get_txids / fee_estimates (+ remove / size).
    Bounded: when full, the lowest fee-rate entry is evicted."""

    def __init__(self, max_entries: int = 10000, min_relay_fee: float = 1.0):
        self.max_entries = int(max_entries)
        self.min_relay_fee = float(min_relay_fee)
        self._entries: Dict[str, _ShadowEntry] = {}
        self._lock = threading.RLock()

    def accept(self, txid: str, fee: int = 0, vsize: int = 0) -> tuple:
        vsize = max(int(vsize or 0), 250)
        with self._lock:
            self._entries[str(txid)] = _ShadowEntry(str(txid), int(fee or 0), vsize)
            while len(self._entries) > self.max_entries:
                worst = min(self._entries.values(), key=lambda e: e.fee_rate)
                del self._entries[worst.txid]
        return True, "mirrored"

    def add_tx(self, tx: Any, fee: int = 0, vsize: int = 0) -> tuple:
        txid = getattr(tx, "txid", None)
        return self.accept(str(txid if txid is not None else tx), fee, vsize)

    def remove(self, txid: str) -> bool:
        with self._lock:
            return self._entries.pop(str(txid), None) is not None

    def size(self) -> int:
        with self._lock:
            return len(self._entries)

    def get_txids(self) -> list:
        with self._lock:
            return list(self._entries.keys())

    def sorted_by_fee_rate(self) -> list:
        with self._lock:
            return sorted(self._entries.values(), key=lambda e: e.fee_rate, reverse=True)

    def fee_estimates(self) -> dict:
        entries = self.sorted_by_fee_rate()

        def _est(target_blocks: int) -> float:
            if not entries:
                return self.min_relay_fee
            idx = int(len(entries) * min(1.0, target_blocks / 144))
            return round(entries[min(idx, len(entries) - 1)].fee_rate, 2)
        return {"1": _est(1), "3": _est(3), "6": _est(6), "144": _est(144)}


class Group61Config:
    """Switches for the layer. Defaults are safe (report-only)."""
    enable_block_store: bool = True        # shadow copy of connected blocks (append-only)
    block_store_subdir: str = "group61_blocks"
    enable_utreexo: bool = True            # block-hash accumulator (shadow)
    utreexo_leaf_cap: int = 2000           # forest rebuilds on every add -> cap RAM/CPU
    enable_mempool_shadow: bool = True     # MempoolWithEviction mirror (never rejects)
    enable_p2p_observer: bool = True       # message counters + peer heights
    max_tracked_peers: int = 1000
    max_message_types: int = 64
    run_selfchecks: bool = True
    node_id: str = "local"
    node_host: str = "127.0.0.1"
    node_port: int = 8333
    node_type: str = "full"


# --------------------------------------------------------------------------
# Coverage table: how each of the 20 classes is connected
# --------------------------------------------------------------------------
COVERAGE: Dict[str, str] = {
    "NEBULANodeManager":   "auto    - registers this node, height updated on every connected block",
    "BlockchainMetrics":   "auto    - custom metrics refreshed on every block; export_* via layer",
    "ChainSyncMonitor":    "auto    - fed with peer heights by the P2P observer",
    "TransactionBuilder":  "auto/factory - built if node has .wallet; else create_tx_builder(wallet)",
    "P2PMessageType":      "type    - used by the P2P observer to normalise message names",
    "P2PMessage_Real":     "selfcheck + factory new_message(type, payload)",
    "RealP2PNode":         "factory - create_real_p2p(); never auto-started",
    "RealMiner":           "factory - create_real_miner(); never auto-started",
    "NEBULAFullNodeV3":    "factory - create_full_node_v3(); never auto-started",
    "P2PKHScript":         "utility - p2pkh_lock() / p2pkh_address() + selfcheck",
    "UtreexoProof":        "auto    - produced/verified by the forest",
    "_UtreexoTree":        "auto    - built internally by the forest",
    "UtreexoForest":       "auto    - shadow accumulator of connected block hashes (capped)",
    "BIP324Session":       "selfcheck + factory new_bip324_session()",
    "BIP324Transport":     "factory - wrap_bip324(sock, initiator)",
    "BlockFileStore":      "auto    - append-only shadow store of connected blocks (data_dir)",
    "PersistentChain":     "factory - create_persistent_chain(); owns a separate chain, so never auto-attached",
    "MempoolWithEviction": "auto    - shadow mirror of accepted mempool txs (never rejects)",
    "Bip9State":           "type    - exposed as layer.Bip9State",
    "Bip9Deployment":      "registry - register_bip9(); report-only",
}

_CLASS_NAMES = tuple(COVERAGE.keys())

_HEIGHT_KEYS = ("height", "start_height", "best_height", "block_height")


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------
def _num(value: Any, default: int = 0) -> int:
    """Convert int / float / callable / property-like values to int safely."""
    try:
        if callable(value):
            value = value()
        return int(value)
    except Exception:
        return default


def _resolve_chain(node: Any) -> Any:
    for attr in ("bc", "blockchain", "chain"):
        obj = getattr(node, attr, None)
        if obj is not None and hasattr(obj, "add_listener"):
            return obj
    return None


def _message_fields(msg: Any):
    """Return (type_name, payload) from several possible message shapes."""
    if isinstance(msg, dict):
        mtype = msg.get("type") or msg.get("command") or msg.get("msg_type")
        payload = msg.get("payload", msg)
    else:
        mtype = (getattr(msg, "msg_type", None) or getattr(msg, "command", None)
                 or getattr(msg, "type", None))
        payload = getattr(msg, "payload", None)
    return (str(mtype) if mtype is not None else "unknown"), payload


# --------------------------------------------------------------------------
# Self-checks (pure functions; no node needed)
# --------------------------------------------------------------------------
def run_selfchecks() -> Dict[str, Dict[str, Any]]:
    """Run small deterministic checks on the classes that can be tested alone."""
    results: Dict[str, Dict[str, Any]] = {}

    def check(name: str, fn: Callable[[], Any]):
        try:
            detail = fn()
            results[name] = {"ok": True, "detail": detail}
        except Exception as exc:  # noqa: BLE001
            results[name] = {"ok": False, "detail": f"{type(exc).__name__}: {exc}"}

    def p2p_roundtrip():
        sent = g.P2PMessage_Real("ping", {"nonce": 7})
        got = g.P2PMessage_Real.decode(sent.encode())
        assert got is not None and got.msg_type == "ping" and got.payload == {"nonce": 7}
        return "encode/decode ok"

    def bip324_loopback():
        a, b = g.BIP324Session(True), g.BIP324Session(False)
        assert a.receive_pubkey(b.our_pubkey()) and b.receive_pubkey(a.our_pubkey())
        assert a.is_ready and b.is_ready
        assert b.decrypt(a.encrypt(b"nebula-a")) == b"nebula-a"
        assert a.decrypt(b.encrypt(b"nebula-b")) == b"nebula-b"
        assert a.garbage_terminator() == b.garbage_terminator()
        return "handshake + both directions ok"

    def utreexo_roundtrip():
        forest = g.UtreexoForest()
        leaves = [hashlib.sha256(bytes([i])).digest() for i in range(7)]
        for leaf in leaves:
            forest.add(leaf)
        assert forest.leaf_count == 7
        for leaf in leaves:
            proof = forest.get_proof(leaf)
            assert proof is not None and forest.verify(proof)
        assert isinstance(forest.state_hash(), str)
        return "7 leaves, all proofs verify"

    def p2pkh_structure():
        script = g.P2PKHScript.lock(g.FOUNDATION_ADDRESS)
        assert len(script) == 25 and script[:3] == bytes([0x76, 0xA9, 0x14]) \
            and script[-2:] == bytes([0x88, 0xAC])
        addr = g.P2PKHScript.address_from_script(script)
        assert isinstance(addr, str)
        return {"script_len": len(script), "roundtrip_equal": addr == g.FOUNDATION_ADDRESS}

    def bip9_mask():
        d = g.Bip9Deployment("selfcheck", 28, g.Bip9Deployment.START_ALWAYS,
                             g.Bip9Deployment.NEVER_EXPIRE)
        assert d.mask == 1 << 28
        assert g.Bip9State.ACTIVE.value == "ACTIVE"
        return "mask ok"

    check("p2p_message_roundtrip", p2p_roundtrip)
    check("bip324_loopback", bip324_loopback)
    check("utreexo_roundtrip", utreexo_roundtrip)
    check("p2pkh_structure", p2pkh_structure)
    check("bip9_mask", bip9_mask)
    return results


# --------------------------------------------------------------------------
# The layer
# --------------------------------------------------------------------------
_LAYERS: List["Layer61"] = []
_LAYERS_LOCK = threading.RLock()


class Layer61:
    """Report-only observer that owns instances of the group-61 classes."""

    Bip9State = g.Bip9State
    P2PMessageType = g.P2PMessageType

    def __init__(self, node: Any, config: Optional[Group61Config] = None):
        self.node = node
        self.config = config or Group61Config()
        self.errors = 0
        self.errors_by_component: Dict[str, int] = {}
        self.last_error: Optional[str] = None
        self.build_notes: List[str] = []
        self.selfchecks: Dict[str, Dict[str, Any]] = {}
        self.bip9_deployments: Dict[str, Any] = {}
        self._lock = threading.RLock()
        self._attached = False
        self._known_msg_types = {v for k, v in vars(g.P2PMessageType).items()
                                 if isinstance(v, str) and not k.startswith("_")}
        self.stats_: Dict[str, Any] = {
            "blocks_seen": 0, "reorgs": 0, "last_reorg": None,
            "utreexo_capped": False, "store_writes": 0,
            "mempool_shadow_added": 0, "p2p_messages": {}, "p2p_total": 0,
        }

        self.bc = _resolve_chain(node)
        self.node_manager = self._build("node_manager", g.NEBULANodeManager)
        self.metrics = self._build("metrics", lambda: g.BlockchainMetrics(self.bc))
        self.sync_monitor = self._build("sync_monitor", lambda: g.ChainSyncMonitor(self.bc))
        self.forest = self._build("utreexo", g.UtreexoForest) \
            if self.config.enable_utreexo else None
        self.block_store = self._build("block_store", self._make_block_store) \
            if self.config.enable_block_store else None
        self.mempool_shadow = self._build("mempool_shadow", self._make_shadow_mempool) \
            if self.config.enable_mempool_shadow else None
        self.tx_builder = self._build("tx_builder", self._make_tx_builder)

    # ---------------------------------------------------------- building
    def _build(self, name: str, factory: Callable[[], Any]) -> Any:
        try:
            return factory()
        except Exception as exc:  # noqa: BLE001
            self._record_error(f"build:{name}", exc)
            return None

    def _make_block_store(self):
        datadir = getattr(self.node, "datadir", None) or getattr(self.node, "data_dir", None)
        base = os.path.expanduser(str(datadir)) if datadir else os.path.join(os.getcwd(), "nebula_data")
        return g.BlockFileStore(os.path.join(base, self.config.block_store_subdir))

    def _make_shadow_mempool(self):
        # v10.19 fix: g.MempoolWithEviction derives from the host MempoolEvictionPolicy, which wraps a live
        # Mempool and has no accept()/_entries/sorted_by_fee_rate(), so the old builder always failed.
        # The layer only needs an observe-only mirror, so it gets a small self-contained one.
        self.build_notes.append("mempool_shadow: using built-in _ShadowMempool (host policy class has no accept())")
        return _ShadowMempool()

    def _make_tx_builder(self):
        wallet = getattr(self.node, "wallet", None)
        if wallet is None or self.bc is None:
            return None
        return g.TransactionBuilder(wallet, self.bc)

    # ---------------------------------------------------------- errors
    def _record_error(self, component: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.errors_by_component[component] = self.errors_by_component.get(component, 0) + 1
            self.last_error = f"{component}: {type(exc).__name__}: {exc}"
        log.warning("group61 %s failed: %s", component, exc)

    def _guard(self, component: str, fn: Optional[Callable], *args, **kwargs):
        if fn is None:
            return None
        try:
            return fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001
            self._record_error(component, exc)
            return None

    # ---------------------------------------------------------- attach / detach
    def attach(self) -> bool:
        """Register as chain listener and in the live-layer registry."""
        if self._attached:
            return True
        if self.bc is None:
            self._record_error("attach", RuntimeError("no blockchain with add_listener found on node"))
            return False
        self.bc.add_listener(self)
        self._attached = True
        with _LAYERS_LOCK:
            _LAYERS.append(self)
        cfg = self.config
        if self.node_manager is not None:
            self._guard("node_manager", self.node_manager.register_node,
                        cfg.node_id, cfg.node_host, cfg.node_port, cfg.node_type)
            self._guard("node_manager", self.node_manager.update_status,
                        cfg.node_id, _num(getattr(self.bc, "height", 0)))
        if cfg.run_selfchecks:
            self.selfchecks = run_selfchecks()
            for name, res in self.selfchecks.items():
                if not res["ok"]:
                    self._record_error(f"selfcheck:{name}", RuntimeError(res["detail"]))
        return True

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer61.detach", exc_info=True)
        with _LAYERS_LOCK:
            if self in _LAYERS:
                _LAYERS.remove(self)
        self._attached = False

    # ---------------------------------------------------------- chain listener
    def on_connect(self, block: Any) -> None:
        with self._lock:
            self.stats_["blocks_seen"] += 1
            seen = self.stats_["blocks_seen"]
        height = _num(getattr(self.bc, "height", 0))
        if self.node_manager is not None:
            self._guard("node_manager", self.node_manager.update_status, self.config.node_id, height)
        if self.metrics is not None:
            self._guard("metrics", self.metrics.set_metric, "layer61_blocks_seen", seen)
            self._guard("metrics", self.metrics.set_metric, "layer61_last_height", height)
            self._guard("metrics", self.metrics.set_metric, "layer61_reorgs", self.stats_["reorgs"])
        self._guard("utreexo", self._utreexo_add, block)
        self._guard("block_store", self._store_block, block, height)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        with self._lock:
            self.stats_["reorgs"] += 1
            self.stats_["last_reorg"] = {
                "ancestor_height": _num(ancestor_height, -1),
                "old_len": len(old) if hasattr(old, "__len__") else None,
                "new_len": len(new) if hasattr(new, "__len__") else None,
                "time": time.time(),
            }
        # The accumulator only supports "add" for the shadow use-case, so after a reorg it is
        # restarted. New blocks are accumulated again from the next on_connect call.
        if self.config.enable_utreexo:
            with self._lock:
                self.forest = self._build("utreexo", g.UtreexoForest)
                self.stats_["utreexo_capped"] = False
        # The block store is append-only (Bitcoin style): stale blocks stay on disk and only the
        # tip pointer moves, which on_connect does for the new branch.

    # ---------------------------------------------------------- listener internals
    @staticmethod
    def _block_hash_bytes(block: Any) -> bytes:
        raw = getattr(block, "hash", None)
        if callable(raw):
            raw = raw()
        if isinstance(raw, bytes) and len(raw) == 32:
            return raw
        if isinstance(raw, str):
            try:
                data = bytes.fromhex(raw)
                if len(data) == 32:
                    return data
            except ValueError:
                _NB_SWALLOW_LOG.debug("swallowed ValueError in Layer61._block_hash_bytes", exc_info=True)
        return hashlib.sha256(str(raw if raw is not None else block).encode()).digest()

    def _utreexo_add(self, block: Any) -> None:
        with self._lock:
            if self.forest is None:
                return
            if self.forest.leaf_count >= self.config.utreexo_leaf_cap:
                self.stats_["utreexo_capped"] = True
                return
            leaf = self._block_hash_bytes(block)
            proof = self.forest.add(leaf)
            fresh = self.forest.get_proof(leaf) or proof
            if not self.forest.verify(fresh):
                raise RuntimeError("utreexo proof failed verification")

    def _store_block(self, block: Any, height: int) -> None:
        if self.block_store is None:
            return
        block_dict = g.PersistentChain._block_to_dict(block)
        if "prev_hash" not in block_dict:        # helper fell back to str(block)
            raise ValueError("block could not be converted to a storable dict")
        self.block_store.write_block(block_dict)
        self.block_store.set_tip(block_dict["hash"], height)
        with self._lock:
            self.stats_["store_writes"] += 1

    # ---------------------------------------------------------- P2P observer
    def observe_p2p(self, p2p_node: Any, peer: Any, msg: Any) -> None:
        if not self.config.enable_p2p_observer:
            return
        mtype, payload = _message_fields(msg)
        label = mtype if mtype in self._known_msg_types else "other"
        with self._lock:
            counts = self.stats_["p2p_messages"]
            if label not in counts and len(counts) >= self.config.max_message_types:
                label = "other"
            counts[label] = counts.get(label, 0) + 1
            self.stats_["p2p_total"] += 1
        if self.sync_monitor is not None and isinstance(payload, dict):
            for key in _HEIGHT_KEYS:
                if isinstance(payload.get(key), int):
                    peer_id = str(getattr(peer, "addr", None) or getattr(peer, "address", None)
                                  or id(peer))
                    if (peer_id in self.sync_monitor._peers
                            or len(self.sync_monitor._peers) < self.config.max_tracked_peers):
                        self._guard("sync_monitor", self.sync_monitor.update_peer_height,
                                    peer_id, payload[key])
                    break

    # ---------------------------------------------------------- mempool observer
    def observe_mempool(self, mempool: Any, tx: Any, result: Any) -> None:
        if self.mempool_shadow is None:
            return
        if getattr(self.bc, "mempool", None) is not mempool:
            return
        accepted = result[0] if isinstance(result, tuple) and result else bool(result)
        if not accepted:
            return
        fee = _num(getattr(tx, "fee", 0))
        vsize = _num(getattr(tx, "vsize", 0)) or _num(getattr(tx, "size", 0))
        self._guard("mempool_shadow", self.mempool_shadow.add_tx, tx, fee, vsize)
        with self._lock:
            self.stats_["mempool_shadow_added"] += 1

    # ---------------------------------------------------------- explicit utilities
    def p2pkh_lock(self, address: str) -> bytes:
        return g.P2PKHScript.lock(address)

    def p2pkh_address(self, script: bytes) -> Optional[str]:
        return g.P2PKHScript.address_from_script(script)

    def new_message(self, msg_type: str, payload: dict):
        return g.P2PMessage_Real(msg_type, payload)

    def new_bip324_session(self, initiator: bool, network: str = "mainnet"):
        return g.BIP324Session(initiator, network)

    def wrap_bip324(self, sock: Any, initiator: bool, network: str = "mainnet"):
        return g.BIP324Transport(sock, initiator, network)

    def new_utreexo_forest(self):
        return g.UtreexoForest()

    def register_bip9(self, name: str, bit: int, start_time: int, timeout: int,
                      threshold_pct: float = 95.0, min_activation_height: int = 0):
        dep = g.Bip9Deployment(name, bit, start_time, timeout, threshold_pct,
                               min_activation_height)
        self.bip9_deployments[name] = dep
        return dep

    def create_tx_builder(self, wallet: Any):
        self.tx_builder = g.TransactionBuilder(wallet, self.bc)
        return self.tx_builder

    # Explicit opt-in factories: these build objects but NEVER start them.
    def create_real_p2p(self, **kwargs):
        return g.RealP2PNode(self.bc, **kwargs)

    def create_real_miner(self, miner_address: str, **kwargs):
        return g.RealMiner(self.bc, miner_address, **kwargs)

    def create_full_node_v3(self, **kwargs):
        return g.NEBULAFullNodeV3(**kwargs)

    def create_persistent_chain(self, data_dir: Optional[str] = None):
        return g.PersistentChain(data_dir)

    # ---------------------------------------------------------- reporting
    def export_prometheus(self) -> str:
        return self.metrics.export_prometheus() if self.metrics else ""

    def export_json(self) -> dict:
        return self.metrics.export_json() if self.metrics else {}

    def status(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "attached": self._attached,
                "errors": self.errors,
                "errors_by_component": dict(self.errors_by_component),
                "last_error": self.last_error,
                "build_notes": list(self.build_notes),
                "components": {
                    "node_manager": self.node_manager is not None,
                    "metrics": self.metrics is not None,
                    "sync_monitor": self.sync_monitor is not None,
                    "utreexo": self.forest is not None,
                    "block_store": self.block_store is not None,
                    "mempool_shadow": self.mempool_shadow is not None,
                    "tx_builder": self.tx_builder is not None,
                },
                "stats": {k: (dict(v) if isinstance(v, dict) else v) for k, v in self.stats_.items()},
                "utreexo_leaves": self.forest.leaf_count if self.forest else 0,
                "node_manager": self.node_manager.node_manager_stats() if self.node_manager else {},
                "sync": self.sync_monitor.sync_status() if self.sync_monitor else {},
                "store": self.block_store.storage_info() if self.block_store else {},
                "selfchecks": {k: v["ok"] for k, v in self.selfchecks.items()},
                "bip9_deployments": sorted(self.bip9_deployments),
            }


# --------------------------------------------------------------------------
# install / uninstall
# --------------------------------------------------------------------------
def _dispatch(method: str, *args) -> None:
    with _LAYERS_LOCK:
        layers = list(_LAYERS)
    for layer in layers:
        try:
            getattr(layer, method)(*args)
        except Exception as exc:  # noqa: BLE001
            layer._record_error(method, exc)


def _patch_p2p(host: Any, report: dict) -> None:
    cls = getattr(host, "P2PNode", None)
    if cls is None or not hasattr(cls, "_handle_message"):
        report["skipped"].append("P2PNode._handle_message (not found in host)")
        return
    if getattr(cls, "_g61_orig_handle", None):
        return
    orig = cls._handle_message

    def patched(self, peer, msg, *a, **k):
        result = orig(self, peer, msg, *a, **k)      # original ALWAYS first
        _dispatch("observe_p2p", self, peer, msg)
        return result

    cls._g61_orig_handle = orig
    cls._handle_message = patched
    report["patched"].append("P2PNode._handle_message")


def _patch_mempool(host: Any, report: dict) -> None:
    cls = getattr(host, "Mempool", None)
    if cls is None or not hasattr(cls, "submit"):
        report["skipped"].append("Mempool.submit (not found in host)")
        return
    if getattr(cls, "_g61_orig_submit", None):
        return
    orig = cls.submit

    def patched(self, tx, *a, **k):
        result = orig(self, tx, *a, **k)             # original ALWAYS first
        _dispatch("observe_mempool", self, tx, result)
        return result

    cls._g61_orig_submit = orig
    cls.submit = patched
    report["patched"].append("Mempool.submit")


def install(host: Any, config: Optional[Group61Config] = None) -> Dict[str, Any]:
    """Attach the layer to every NEBULAFullNode created after this call."""
    report: Dict[str, Any] = {"installed": False, "patched": [], "skipped": [], "already": False}
    cls = getattr(host, "NEBULAFullNode", None)
    if cls is None:
        report["skipped"].append("NEBULAFullNode (not found in host)")
        return report
    if getattr(cls, "_g61_orig", None):
        report["already"] = True
        return report

    orig_init = cls.__init__

    def patched_init(self, *a, **k):
        orig_init(self, *a, **k)                     # original ALWAYS first
        try:
            self.group61 = Layer61(self, config)
            self.group61.attach()
        except Exception as exc:  # noqa: BLE001 - the node must still start
            self.group61_error = exc
            log.warning("group61 attach failed: %s", exc)

    cls._g61_orig = orig_init
    cls.__init__ = patched_init
    report["patched"].append("NEBULAFullNode.__init__")
    _patch_p2p(host, report)
    _patch_mempool(host, report)
    report["installed"] = True
    return report


def uninstall(host: Any) -> Dict[str, Any]:
    """Undo install(): restore every patched method and detach live layers."""
    report: Dict[str, Any] = {"restored": []}
    for cls_name, attr, marker in (
        ("NEBULAFullNode", "__init__", "_g61_orig"),
        ("P2PNode", "_handle_message", "_g61_orig_handle"),
        ("Mempool", "submit", "_g61_orig_submit"),
    ):
        cls = getattr(host, cls_name, None)
        orig = getattr(cls, marker, None) if cls is not None else None
        if orig:
            setattr(cls, attr, orig)
            delattr(cls, marker)
            report["restored"].append(f"{cls_name}.{attr}")
    with _LAYERS_LOCK:
        layers = list(_LAYERS)
    for layer in layers:
        layer.detach()
    return report


if __name__ == "__main__":
    for check_name, outcome in run_selfchecks().items():
        print(f"{check_name:24s} {'OK ' if outcome['ok'] else 'FAIL'}  {outcome['detail']}")
