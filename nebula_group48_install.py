"""nebula_group48_install.py

Wires all 20 classes of nebula_group48.py into a running NEBULAFullNode as ONE
connected chain, without editing nebula_v10_11.py or nebula_group48.py.

Design rules (same as group 5):
  A) One separate Layer48 object per node, stored on  node.group48.
  B) The layer NEVER rejects a block, a transaction or a peer message.
     The original host method always runs first; the layer only observes.
     Every callback is wrapped in try/except and failures are counted in
     layer.errors (details in layer.error_log).
  C) install(host) / uninstall(host) wrap NEBULAFullNode.__init__ (reversible).

Wiring chain (in the order of the guide, step 4):

   1  ScriptOpCode              data type      -> used by ScriptEngine
   2  NetworkMessageType        data type      -> used by NetworkMessage / NetworkLayerV2
   3  NetworkMessage            data type      -> used by NetworkLayerV2
   4  MetaTransaction           utility        -> layer.new_meta_transaction()
   5  MetaTransactionRelayer    utility/p2p    -> layer.relay_meta_transaction()
   6  MempoolTransactionPool    Mempool.submit -> observed accepted-tx pool
   7  AdvancedMempoolV2         Mempool.submit -> tiered shadow mempool (observe only)
   8  BlockProducer             chain listener -> records blocks mined by our address
   9  ScriptEngine              utility/p2p    -> layer.run_script()
  10  WalletRecoveryEngine      wallet         -> layer.recover_wallet() & friends
  11  TaprootEngine             utility/p2p    -> layer.taproot_address()
  12  BLSAggregatedMultisig     wallet         -> layer.new_multisig()
  13  UTXOCommitment            chain listener -> periodic commitments
  14  BFTConsensus              chain listener -> report-only voting rounds
  15  NetworkLayerV2            P2PNode        -> peer / message observation
  16  ChainAnalysisTool         chain listener -> layer.chain_analysis (on demand)
  17  PositionHealthMonitor     monitor        -> periodic scan_all()
  18  CrossChainYieldAggregator chain listener -> layer.yield_report() (on demand)
  19  DIDDocumentV2             utility        -> used by DIDRegistryV2
  20  DIDRegistryV2             utility        -> layer.create_did() / resolve_did()

Usage:
    import nebula_v10_11 as host
    import nebula_group48_install as g48
    g48.install(host)          # every NEBULAFullNode created afterwards gets node.group48
    ...
    node.group48.status()      # wiring state of all 20 classes
    node.group48.stats()       # live counters of every component
    g48.uninstall(host)        # back to the original behaviour
"""
from __future__ import annotations

import functools
import threading
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group48 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

LAYER_ATTR = "group48"
LAYER_ERROR_ATTR = "group48_error"

# ----------------------------------------------------------------------------
# Tunables (all caps exist so the layer can never grow without bound)
# ----------------------------------------------------------------------------
COMMITMENT_INTERVAL_BLOCKS = 100     # UTXOCommitment is O(addresses): not every block
HEALTH_SCAN_INTERVAL_BLOCKS = 10     # PositionHealthMonitor.scan_all() cadence
HISTORY_CAP = 1000                   # commitments, BFT rounds, alerts kept
OBSERVED_POOL_CAP = 5000             # MempoolTransactionPool eviction is O(n)
PEER_CAP = 1000                      # peers mirrored into NetworkLayerV2
MESSAGE_TYPE_CAP = 64                # distinct message-type counters
ERROR_LOG_CAP = 100

# Candidate host method names for "peer disconnected" (only existing ones are wrapped).
_P2P_DISCONNECT_CANDIDATES = (
    "_remove_peer", "remove_peer", "_on_peer_disconnect",
    "_disconnect_peer", "disconnect_peer", "_drop_peer",
)
_P2P_MESSAGE_HOOKS = ("_handle_message", "_handle_block")

# ----------------------------------------------------------------------------
# Wiring plan (order == guide step 4). Used by Layer48.status().
# ----------------------------------------------------------------------------
WIRING_PLAN: Tuple[Tuple[int, str, str, str], ...] = (
    (1,  "ScriptOpCode",              "data type",       "imported by ScriptEngine"),
    (2,  "NetworkMessageType",        "data type",       "imported by NetworkMessage / NetworkLayerV2"),
    (3,  "NetworkMessage",            "data type",       "imported by NetworkLayerV2"),
    (4,  "MetaTransaction",           "utility",         "layer.new_meta_transaction"),
    (5,  "MetaTransactionRelayer",    "p2p / utility",   "layer.relay_meta_transaction"),
    (6,  "MempoolTransactionPool",    "Mempool.submit",  "observed accepted-tx pool"),
    (7,  "AdvancedMempoolV2",         "Mempool.submit",  "tiered shadow mempool"),
    (8,  "BlockProducer",             "chain listener",  "on_connect: records own blocks"),
    (9,  "ScriptEngine",              "p2p / utility",   "layer.run_script"),
    (10, "WalletRecoveryEngine",      "wallet",          "layer.recover_wallet"),
    (11, "TaprootEngine",             "p2p / utility",   "layer.taproot_address"),
    (12, "BLSAggregatedMultisig",     "wallet",          "layer.new_multisig"),
    (13, "UTXOCommitment",            "chain listener",  "on_connect: periodic commitment"),
    (14, "BFTConsensus",              "chain listener",  "on_connect: report-only rounds"),
    (15, "NetworkLayerV2",            "P2PNode",         "message / peer observation"),
    (16, "ChainAnalysisTool",         "chain listener",  "layer.chain_analysis"),
    (17, "PositionHealthMonitor",     "monitor",         "on_connect: periodic scan_all"),
    (18, "CrossChainYieldAggregator", "chain listener",  "layer.yield_report"),
    (19, "DIDDocumentV2",             "utility",         "used by DIDRegistryV2"),
    (20, "DIDRegistryV2",             "utility",         "layer.create_did / resolve_did"),
)

# ----------------------------------------------------------------------------
# Small helpers
# ----------------------------------------------------------------------------
_LIVE_LAYERS: List["Layer48"] = []
_LIVE_LOCK = threading.RLock()
_P2P_ORIGINALS: Dict[str, Callable] = {}
_P2P_CLASS: Any = None


def _first_attr(obj: Any, names: Tuple[str, ...], default: Any = None) -> Any:
    for name in names:
        try:
            value = getattr(obj, name)
        except Exception:
            continue
        if value is not None:
            return value
    return default


def _block_height(block: Any) -> int:
    value = _first_attr(block, ("height",))
    if value is None:
        value = _first_attr(_first_attr(block, ("header",)), ("height",), 0)
    try:
        return int(value or 0)
    except Exception:
        return 0


def _block_hash(block: Any) -> str:
    value = _first_attr(block, ("hash", "block_hash"))
    if value is None:
        value = _first_attr(_first_attr(block, ("header",)), ("hash",), "")
    return str(value or "")


def _block_txs(block: Any) -> list:
    value = _first_attr(block, ("transactions", "txs", "tx", "vtx"), [])
    try:
        return list(value)
    except Exception:
        return []


def _peer_info(peer: Any) -> Tuple[str, str, int]:
    """Return (peer_id, ip, port) from whatever peer object the host uses."""
    ip = _first_attr(peer, ("ip", "host", "address"), "")
    port = _first_attr(peer, ("port",), 0)
    if isinstance(peer, tuple) and len(peer) >= 2:
        ip, port = peer[0], peer[1]
    peer_id = _first_attr(peer, ("peer_id", "id", "node_id", "addr"), None)
    if peer_id is None:
        peer_id = f"{ip}:{port}" if ip else str(peer)
    try:
        port = int(port or 0)
    except Exception:
        port = 0
    return str(peer_id), str(ip or ""), port


# ----------------------------------------------------------------------------
# The layer
# ----------------------------------------------------------------------------
class Layer48:
    """Connects all 20 group48 classes to one node. Never rejects anything."""

    def __init__(self, node: Any, host: Any = None,
                 miner_address: Optional[str] = None,
                 validators: Optional[List[str]] = None):
        self.node = node
        self.host = host
        self.errors = 0
        self.error_log: List[str] = []
        self.stats_: Dict[str, Any] = {
            "blocks_seen": 0, "reorgs": 0, "last_height": -1,
            "mempool_accepted": 0, "mempool_rejected_seen": 0,
            "p2p_messages": 0, "p2p_peers_seen": 0, "p2p_peers_gone": 0,
            "own_blocks": 0, "commitments": 0, "bft_rounds": 0, "health_scans": 0,
            "message_types": {},
        }
        self._lock = threading.RLock()
        self._plan_state: Dict[str, Dict[str, Any]] = {}
        self._mempool_obj: Any = None
        self._known_peers: set = set()
        self.p2p: Any = None

        self.bc = _first_attr(node, ("bc", "blockchain"))
        self.miner_address = str(miner_address or self._probe_miner_address() or "")
        self.validators = list(validators) if validators is not None else self._probe_validators()
        self.oracle = self._probe_oracle()

        # components (None until built successfully)
        self.mempool_pool = None
        self.advanced_mempool = None
        self.block_producer = None
        self.relayer = None
        self.script_engine = None
        self.wallet_recovery = None
        self.taproot = None
        self.utxo_commitment = None
        self.bft = None
        self.network = None
        self.chain_analysis = None
        self.health_monitor = None
        self.yield_aggregator = None
        self.did_registry = None

        self._build_all()
        self._attach_mempool_hook()
        self.p2p = self._probe_p2p()

    # -- error accounting ----------------------------------------------------
    def _count_error(self, where: str, exc: Optional[BaseException] = None) -> None:
        with self._lock:
            self.errors += 1
            if len(self.error_log) < ERROR_LOG_CAP:
                detail = f"{type(exc).__name__}: {exc}" if exc else ""
                self.error_log.append(f"{where} {detail}".strip())

    def _guard(self, where: str, fn: Callable, *args, **kwargs) -> Any:
        try:
            return fn(*args, **kwargs)
        except Exception as exc:
            self._count_error(where, exc)
            return None

    # -- probes (the host is never modified; we only look) ------------------
    def _probe_miner_address(self) -> str:
        for holder in (self.node, _first_attr(self.node, ("wallet", "miner_wallet"))):
            if holder is None:
                continue
            value = _first_attr(holder, ("miner_address", "mining_address", "address"))
            if isinstance(value, str) and value:
                return value
        return ""

    def _probe_validators(self) -> List[str]:
        for holder in (self.bc, self.node):
            raw = _first_attr(holder, ("validators",)) if holder is not None else None
            if raw is None:
                continue
            try:
                return [str(v) for v in raw]
            except Exception:
                continue
        return []

    def _probe_oracle(self) -> Any:
        oracle_cls = getattr(self.host, "OracleV2", None)
        if oracle_cls is None:
            return None
        try:
            for value in vars(self.node).values():
                if isinstance(value, oracle_cls):
                    return value
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer48._probe_oracle", exc_info=True)
        return None

    def _probe_p2p(self) -> Any:
        p2p_cls = getattr(self.host, "P2PNode", None)
        if p2p_cls is None:
            return None
        try:
            for value in vars(self.node).values():
                if isinstance(value, p2p_cls):
                    return value
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer48._probe_p2p", exc_info=True)
        return None

    # -- build, in guide order ----------------------------------------------
    def _plan(self, order: int, name: str, ok: bool, error: str = "") -> None:
        role, hook = next((r, h) for o, n, r, h in WIRING_PLAN if n == name)
        self._plan_state[name] = {"order": order, "role": role, "hook": hook,
                                  "attached": bool(ok), "error": error}

    def _build(self, order: int, name: str, attr: Optional[str], factory: Callable) -> None:
        try:
            obj = factory()
            if attr:
                setattr(self, attr, obj)
            self._plan(order, name, True)
        except Exception as exc:
            self._count_error(f"build {name}", exc)
            self._plan(order, name, False, f"{type(exc).__name__}: {exc}")

    def _build_all(self) -> None:
        bc = self.bc
        utxo = _first_attr(bc, ("utxo",))

        def check_script_opcode():
            assert len(g.ScriptOpCode) > 0
        def check_message_type():
            assert g.NetworkMessageType.PING == 3
        def check_message():
            assert g.NetworkMessage(g.NetworkMessageType.PING, b"").is_valid()
        def check_meta_tx():
            g.MetaTransaction("probe", "probe", 0, b"", 0)
        def check_multisig():
            g.BLSAggregatedMultisig(["a", "b"], 2)
        def check_did_doc():
            assert g.DIDDocumentV2("did:nebula:probe", "did:nebula:probe").to_document()

        self._build(1,  "ScriptOpCode", None, check_script_opcode)
        self._build(2,  "NetworkMessageType", None, check_message_type)
        self._build(3,  "NetworkMessage", None, check_message)
        self._build(4,  "MetaTransaction", None, check_meta_tx)
        self._build(5,  "MetaTransactionRelayer", "relayer",
                    lambda: g.MetaTransactionRelayer(bc, self.miner_address))
        self._build(6,  "MempoolTransactionPool", "mempool_pool",
                    lambda: g.MempoolTransactionPool("observed", OBSERVED_POOL_CAP, 0))
        self._build(7,  "AdvancedMempoolV2", "advanced_mempool",
                    lambda: g.AdvancedMempoolV2(bc))
        self._build(8,  "BlockProducer", "block_producer",
                    lambda: g.BlockProducer(bc, self.miner_address))
        self._build(9,  "ScriptEngine", "script_engine", g.ScriptEngine)
        self._build(10, "WalletRecoveryEngine", "wallet_recovery",
                    lambda: g.WalletRecoveryEngine(bc))
        self._build(11, "TaprootEngine", "taproot", g.TaprootEngine)
        self._build(12, "BLSAggregatedMultisig", None, check_multisig)
        self._build(13, "UTXOCommitment", "utxo_commitment",
                    lambda: g.UTXOCommitment(utxo))
        self._build(14, "BFTConsensus", "bft",
                    lambda: g.BFTConsensus(self.validators, bc))
        self._build(15, "NetworkLayerV2", "network",
                    lambda: g.NetworkLayerV2(bc))
        self._build(16, "ChainAnalysisTool", "chain_analysis",
                    lambda: g.ChainAnalysisTool(bc))
        self._build(17, "PositionHealthMonitor", "health_monitor",
                    lambda: g.PositionHealthMonitor(bc, self.oracle))
        self._build(18, "CrossChainYieldAggregator", "yield_aggregator",
                    g.CrossChainYieldAggregator)
        self._build(19, "DIDDocumentV2", None, check_did_doc)
        self._build(20, "DIDRegistryV2", "did_registry",
                    lambda: g.DIDRegistryV2(bc))

    # ------------------------------------------------------------------------
    # Chain listener  (bc.add_listener(layer))
    # ------------------------------------------------------------------------
    def on_connect(self, block: Any) -> None:
        try:
            height = _block_height(block)
            block_hash = _block_hash(block)
            txs = _block_txs(block)
            with self._lock:
                self.stats_["blocks_seen"] += 1
                self.stats_["last_height"] = height
            self._guard("on_connect/mempool-prune", self._prune_mempool_shadow, txs)
            self._guard("on_connect/block-producer", self._record_own_block, block, height, txs)
            if height % COMMITMENT_INTERVAL_BLOCKS == 0:
                self._guard("on_connect/commitment", self._record_commitment, height)
            self._guard("on_connect/bft", self._record_bft_round, height, block_hash)
            if height % HEALTH_SCAN_INTERVAL_BLOCKS == 0:
                self._guard("on_connect/health", self._scan_positions)
        except Exception as exc:
            self._count_error("on_connect", exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        try:
            with self._lock:
                self.stats_["reorgs"] += 1
            self._guard("on_reorg/commitments", self._drop_above, ancestor_height)
        except Exception as exc:
            self._count_error("on_reorg", exc)

    def detach(self) -> None:
        """Remove every hook this layer installed on its node."""
        bc = self.bc
        try:
            if hasattr(bc, "remove_listener"):
                bc.remove_listener(self)
            else:
                bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer48.detach", exc_info=True)
        mp = self._mempool_obj
        if mp is not None:
            try:
                vars(mp).pop("submit", None)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in Layer48.detach", exc_info=True)
            self._mempool_obj = None
        with _LIVE_LOCK:
            if self in _LIVE_LAYERS:
                _LIVE_LAYERS.remove(self)

    # -- listener steps -------------------------------------------------------
    def _prune_mempool_shadow(self, txs: list) -> None:
        for tx in txs:
            txid = _first_attr(tx, ("txid",))
            if txid is None:
                continue
            for pool in (self.mempool_pool,
                         getattr(self.advanced_mempool, "_high", None),
                         getattr(self.advanced_mempool, "_medium", None),
                         getattr(self.advanced_mempool, "_low", None)):
                if pool is not None:
                    pool._txs.pop(txid, None)

    def _record_own_block(self, block: Any, height: int, txs: list) -> None:
        if not self.miner_address or self.block_producer is None or not txs:
            return
        outputs = list(_first_attr(txs[0], ("outputs",), []))
        paid_to_us = [o for o in outputs if _first_attr(o, ("address",)) == self.miner_address]
        if not paid_to_us:
            return
        total = sum(int(_first_attr(o, ("value",), 0) or 0) for o in outputs)
        fees = max(0, total - int(g.mining_reward(height)))
        self.block_producer.record_produced(block, fees)
        with self._lock:
            self.stats_["own_blocks"] += 1

    def _record_commitment(self, height: int) -> None:
        if self.utxo_commitment is None:
            return
        self.utxo_commitment.compute_commitment(height)
        store = self.utxo_commitment._commitments
        while len(store) > HISTORY_CAP:
            store.pop(min(store))
        with self._lock:
            self.stats_["commitments"] += 1

    def _record_bft_round(self, height: int, block_hash: str) -> None:
        if self.bft is None:
            return
        # Report-only: a round is opened for statistics; no vote ever decides anything.
        if self.bft.start_round(height, block_hash):
            with self._lock:
                self.stats_["bft_rounds"] += 1
        rounds = self.bft._rounds
        while len(rounds) > HISTORY_CAP:
            rounds.pop(min(rounds))

    def _scan_positions(self) -> None:
        if self.health_monitor is None:
            return
        self.health_monitor.scan_all()
        alerts = self.health_monitor._alerts
        if len(alerts) > HISTORY_CAP:
            del alerts[:len(alerts) - HISTORY_CAP]
        with self._lock:
            self.stats_["health_scans"] += 1

    def _drop_above(self, ancestor_height: int) -> None:
        if self.utxo_commitment is not None:
            store = self.utxo_commitment._commitments
            for h in [h for h in store if h > ancestor_height]:
                store.pop(h, None)
        if self.bft is not None:
            rounds = self.bft._rounds
            for h in [h for h in rounds if h > ancestor_height]:
                rounds.pop(h, None)

    # ------------------------------------------------------------------------
    # Mempool.submit hook (instance level, original always runs first)
    # ------------------------------------------------------------------------
    def _attach_mempool_hook(self) -> None:
        mempool = _first_attr(self.bc, ("mempool",))
        if mempool is None or not hasattr(mempool, "submit"):
            self._count_error("mempool hook: bc.mempool.submit not found")
            return
        original = mempool.submit
        layer = self

        @functools.wraps(original)
        def submit_with_observer(tx, *args, **kwargs):
            result = original(tx, *args, **kwargs)      # host decision, untouched
            try:
                layer._observe_submit(tx, result)
            except Exception as exc:
                layer._count_error("mempool observe", exc)
            return result

        try:
            mempool.submit = submit_with_observer
            self._mempool_obj = mempool
        except Exception as exc:
            self._count_error("mempool hook install", exc)

    def _observe_submit(self, tx: Any, result: Any) -> None:
        accepted = result[0] if isinstance(result, tuple) and result else bool(result)
        if not accepted:
            with self._lock:
                self.stats_["mempool_rejected_seen"] += 1
            return
        with self._lock:
            self.stats_["mempool_accepted"] += 1
        utxo = _first_attr(self.bc, ("utxo",))
        if self.advanced_mempool is not None:
            self._guard("shadow mempool", self.advanced_mempool.submit, tx, utxo)
        if self.mempool_pool is not None:
            self._guard("observed pool", self._add_observed, tx, utxo)

    def _add_observed(self, tx: Any, utxo: Any) -> None:
        fee_rate = int(tx.fee(utxo)) // max(1, int(tx.byte_size()))
        self.mempool_pool.add(tx, fee_rate)

    # ------------------------------------------------------------------------
    # P2P observation (called by the class-level P2PNode wrappers)
    # ------------------------------------------------------------------------
    def observe_message(self, peer: Any, msg: Any) -> None:
        if self.network is None:
            return
        self._register_peer(peer)
        kind = str(_first_attr(msg, ("msg_type", "type", "command"), "unknown"))
        with self._lock:
            self.stats_["p2p_messages"] += 1
            kinds = self.stats_["message_types"]
            if kind in kinds or len(kinds) < MESSAGE_TYPE_CAP:
                kinds[kind] = kinds.get(kind, 0) + 1

    def observe_block(self, peer: Any) -> None:
        if self.network is not None:
            self._register_peer(peer)

    def observe_disconnect(self, peer: Any) -> None:
        if self.network is None:
            return
        peer_id, _, _ = _peer_info(peer)
        if peer_id in self._known_peers:
            self._known_peers.discard(peer_id)
            self.network.penalize_peer(peer_id, 100)    # score 100 -> 0 removes the peer
            with self._lock:
                self.stats_["p2p_peers_gone"] += 1

    def _register_peer(self, peer: Any) -> None:
        peer_id, ip, port = _peer_info(peer)
        if peer_id in self._known_peers or len(self._known_peers) >= PEER_CAP:
            return
        self._known_peers.add(peer_id)
        self.network.add_peer(peer_id, ip, port)
        with self._lock:
            self.stats_["p2p_peers_seen"] += 1

    # ------------------------------------------------------------------------
    # Public on-demand API (utility / wallet classes)
    # ------------------------------------------------------------------------
    def new_meta_transaction(self, from_addr: str, to: str, value: int,
                             data: bytes, nonce: int) -> "g.MetaTransaction":
        return g.MetaTransaction(from_addr, to, value, data, nonce)

    def relay_meta_transaction(self, meta_tx: "g.MetaTransaction",
                               pubkey: bytes) -> Tuple[bool, str]:
        if self.relayer is None:
            return False, "relayer unavailable"
        return self.relayer.relay(meta_tx, pubkey)

    def run_script(self, script: bytes, context: Optional[dict] = None) -> bool:
        if self.script_engine is None:
            return False
        return self.script_engine.execute(script, context)

    def taproot_address(self, internal_pubkey: bytes,
                        scripts: Optional[List[bytes]] = None) -> str:
        return self.taproot.create_taproot_address(internal_pubkey, scripts)

    def new_multisig(self, participants: List[str], required: int) -> "g.BLSAggregatedMultisig":
        return g.BLSAggregatedMultisig(participants, required)

    def recover_wallet(self, mnemonic: str, scan_depth: int = 20) -> List[dict]:
        return self.wallet_recovery.recover_from_mnemonic(mnemonic, scan_depth)

    def import_private_key(self, wif_privkey: str) -> Optional[dict]:
        return self.wallet_recovery.import_privkey(wif_privkey)

    def scan_accounts(self, mnemonic: str, accounts: int = 3, depth: int = 10) -> dict:
        return self.wallet_recovery.scan_all_accounts(mnemonic, accounts, depth)

    def create_did(self, address: str, pubkey_hex: str) -> str:
        return self.did_registry.create_did(address, pubkey_hex)

    def resolve_did(self, did: str) -> Optional[dict]:
        return self.did_registry.resolve(did)

    def register_position(self, pos_id: str, owner: str, collateral: int,
                          debt: int, protocol: str) -> None:
        self.health_monitor.register(pos_id, owner, collateral, debt, protocol)

    def yield_report(self) -> dict:
        return self.yield_aggregator.yield_comparison_report()

    # ------------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------------
    def status(self) -> Dict[str, Any]:
        """Wiring state of all 20 classes, in guide order."""
        rows = [dict(name=name, **self._plan_state.get(name, {"attached": False}))
                for _, name, _, _ in WIRING_PLAN]
        return {
            "classes_total": len(rows),
            "classes_attached": sum(1 for r in rows if r.get("attached")),
            "errors": self.errors,
            "mempool_hooked": self._mempool_obj is not None,
            "p2p_found": self.p2p is not None,
            "miner_address_known": bool(self.miner_address),
            "rows": rows,
        }

    def healthy(self) -> bool:
        s = self.status()
        return s["errors"] == 0 and s["classes_attached"] == s["classes_total"]

    def stats(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {"layer": dict(self.stats_), "errors": self.errors}
        sources = (
            ("mempool_shadow", self.advanced_mempool, "pool_stats"),
            ("observed_pool", self.mempool_pool, "size"),
            ("block_producer", self.block_producer, "production_stats"),
            ("relayer", self.relayer, "relayer_stats"),
            ("script_engine", self.script_engine, "script_stats"),
            ("taproot", self.taproot, "taproot_stats"),
            ("bft", self.bft, "bft_stats"),
            ("network", self.network, "network_stats"),
            ("health_monitor", self.health_monitor, "monitor_stats"),
            ("did_registry", self.did_registry, "did_registry_stats"),
            ("commitments", self.utxo_commitment, "commitment_history"),
        )
        for key, obj, method in sources:
            if obj is None:
                continue
            value = self._guard(f"stats/{key}", getattr(obj, method))
            out[key] = len(value) if key == "commitments" and value is not None else value
        return out


# ----------------------------------------------------------------------------
# Class-level P2PNode wrappers (dispatch to the layer that owns that P2PNode)
# ----------------------------------------------------------------------------
def _layer_for(p2p_obj: Any) -> Optional[Layer48]:
    with _LIVE_LOCK:
        layers = list(_LIVE_LAYERS)
    for layer in layers:
        if layer.p2p is p2p_obj:
            return layer
    # Layer built before the P2PNode existed: late binding if there is exactly one candidate.
    unbound = [l for l in layers if l.p2p is None]
    if len(unbound) == 1 and len(layers) == 1:
        unbound[0].p2p = p2p_obj
        return unbound[0]
    return None


def _make_p2p_wrapper(name: str, original: Callable) -> Callable:
    @functools.wraps(original)
    def wrapper(self, *args, **kwargs):
        result = original(self, *args, **kwargs)        # host behaviour first, always
        layer = _layer_for(self)
        if layer is not None:
            peer = args[0] if args else None
            try:
                if name == "_handle_message":
                    layer.observe_message(peer, args[1] if len(args) > 1 else None)
                elif name == "_handle_block":
                    layer.observe_block(peer)
                else:
                    layer.observe_disconnect(peer)
            except Exception as exc:
                layer._count_error(f"p2p {name}", exc)
        return result
    wrapper._g48_wrapped = True
    return wrapper


def _install_p2p_wrappers(host: Any) -> None:
    global _P2P_CLASS
    cls = getattr(host, "P2PNode", None)
    if cls is None or _P2P_ORIGINALS:
        return
    _P2P_CLASS = cls
    for name in _P2P_MESSAGE_HOOKS + _P2P_DISCONNECT_CANDIDATES:
        original = getattr(cls, name, None)
        if original is None or getattr(original, "_g48_wrapped", False):
            continue
        _P2P_ORIGINALS[name] = original
        setattr(cls, name, _make_p2p_wrapper(name, original))


def _uninstall_p2p_wrappers() -> None:
    global _P2P_CLASS
    if _P2P_CLASS is not None:
        for name, original in _P2P_ORIGINALS.items():
            setattr(_P2P_CLASS, name, original)
    _P2P_ORIGINALS.clear()
    _P2P_CLASS = None


# ----------------------------------------------------------------------------
# install / uninstall
# ----------------------------------------------------------------------------
def install(host: Any = None) -> bool:
    """Wrap NEBULAFullNode.__init__ so every new node gets node.group48."""
    if host is None:
        import nebula_v10_11 as host            # noqa: F811
    cls = host.NEBULAFullNode
    if getattr(cls, "_g48_orig", None):
        return False                            # already installed
    original = cls.__init__
    _install_p2p_wrappers(host)

    @functools.wraps(original)
    def patched(self, *args, **kwargs):
        original(self, *args, **kwargs)         # node must start exactly as before
        layer = None
        try:
            layer = Layer48(self, host)
            with _LIVE_LOCK:
                _LIVE_LAYERS.append(layer)
            setattr(self, LAYER_ATTR, layer)
            self.bc.add_listener(layer)
        except Exception as exc:                # the node must still start
            setattr(self, LAYER_ERROR_ATTR, exc)
            if layer is not None:
                layer.detach()

    cls._g48_orig = original
    cls.__init__ = patched
    return True


def uninstall(host: Any = None) -> bool:
    """Restore NEBULAFullNode.__init__, unwrap P2PNode and detach live layers."""
    if host is None:
        import nebula_v10_11 as host            # noqa: F811
    cls = host.NEBULAFullNode
    original = getattr(cls, "_g48_orig", None)
    if not original:
        return False
    cls.__init__ = original
    del cls._g48_orig
    _uninstall_p2p_wrappers()
    with _LIVE_LOCK:
        layers = list(_LIVE_LAYERS)
    for layer in layers:
        layer.detach()
    return True
