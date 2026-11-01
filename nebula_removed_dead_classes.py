"""NEBULA v10.19 - ARCHIVE of removed dead classes that have NO identical live copy.

Nothing here is imported by the node. Kept verbatim (from nebula_v10_18.py) so no work is lost.
Kind C = no live copy anywhere; kind B = the group module holds a different (improved) version.
"""

# ---- HashUtils  (kind B, v10.18 lines 56464-56522) ----
class HashUtils:
    """Extended hashing utilities for NEBULA"""

    @staticmethod
    def sha256d(data: bytes) -> bytes:
        """Double SHA-256 (Bitcoin-style PoW hash)"""
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    @staticmethod
    def hash160(data: bytes) -> bytes:
        """HASH160 = RIPEMD160(SHA256(data))"""
        return hashlib.new('ripemd160', hashlib.sha256(data).digest()).digest()

    @staticmethod
    def hash256(data: bytes) -> bytes:
        """HASH256 = SHA256(SHA256(data))"""
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    @staticmethod
    def tagged_hash(tag: str, data: bytes) -> bytes:
        """BIP340 tagged hash: SHA256(SHA256(tag) || SHA256(tag) || data)"""
        tag_hash = hashlib.sha256(tag.encode()).digest()
        return hashlib.sha256(tag_hash + tag_hash + data).digest()

    @staticmethod
    def merkle_root(txids: list) -> str:
        """Compute Merkle root from list of txids"""
        if not txids:
            return '0' * 64
        hashes = [bytes.fromhex(txid)[::-1] for txid in txids]
        while len(hashes) > 1:
            if len(hashes) % 2 == 1:
                hashes.append(hashes[-1])
            hashes = [
                HashUtils.hash256(hashes[i] + hashes[i+1])
                for i in range(0, len(hashes), 2)
            ]
        return hashes[0][::-1].hex()

    @staticmethod
    def target_to_difficulty(target: int) -> float:
        """Convert target integer to difficulty float"""
        max_target = bits_to_target(INITIAL_BITS)
        return max_target / max(1, target)

    @staticmethod
    def difficulty_to_target(difficulty: float) -> int:
        """Convert difficulty to target"""
        max_target = bits_to_target(INITIAL_BITS)
        return int(max_target / max(0.0001, difficulty))

    @staticmethod
    def compact_from_uint256(target: int) -> int:
        """Convert target integer to compact bits format"""
        nbytes = (target.bit_length() + 7) // 8
        if target >> (8 * (nbytes - 3)) > 0x7f:
            nbytes += 1
        mantissa = target >> (8 * (nbytes - 3))
        return (nbytes << 24) | (mantissa & 0x7fffff)

# ---- MerkleProver  (kind B, v10.18 lines 62866-62894) ----
class MerkleProver:
    """
    Merkle inclusion proofs for transaction verification.
    Light clients can verify tx without full block data.
    """

    @staticmethod
    def prove_inclusion(txid: str, block: 'Block') -> Optional[dict]:
        """Generate Merkle proof that txid is in block."""
        txids = [tx.txid for tx in block.transactions]
        if txid not in txids:
            return None
        proof = MerkleTree.build_proof(txids, txid)
        return {
            "txid":       txid,
            "block_hash": block.hash,
            "height":     block.height,
            "merkle_root": block.header.merkle_root,
            "proof":      proof,
        }

    @staticmethod
    def verify_inclusion(proof_dict: dict) -> bool:
        """Verify a Merkle inclusion proof."""
        return MerkleTree.verify_proof(
            proof_dict["merkle_root"],
            proof_dict["txid"],
            proof_dict["proof"]
        )

# ---- ClusterNode  (kind B, v10.18 lines 63029-63071) ----
@dataclass
# ================================================================
# MODULE 159  nebula_alerts.py — Blockchain Alert System
# ================================================================
# Real-time alerts for significant on-chain events.
# Price alerts, whale movements, governance, security.
# ================================================================

@dataclass
# ================================================================
# MODULE 160  nebula_node_cluster.py — Multi-Node Cluster
# ================================================================
# Run multiple NEBULA nodes in a simulated cluster.
# Network topology, message propagation testing, fork simulation.
# ================================================================

class ClusterNode:
    """A single node in a test cluster."""

    def __init__(self, node_id: str):
        self.node_id    = node_id
        self.blockchain = NEBULABlockchain()
        self.peers:     Set[str] = set()
        self.messages:  List[dict] = []
        self.latency_ms: float = 10.0   # simulated network latency

    def connect_to(self, other_id: str):
        self.peers.add(other_id)

    def send(self, other: 'ClusterNode', msg: dict):
        """Simulate sending a message to another node."""
        msg["from"]  = self.node_id
        msg["delay"] = self.latency_ms
        other.messages.append(msg)

    def receive_all(self, cluster: 'NodeCluster'):
        """Process all pending messages."""
        for msg in self.messages:
            self._handle(msg, cluster)
        self.messages.clear()

    def _handle(self, msg: dict, cluster: 'NodeCluster'):
        pass   # Override for specific handling

# ---- NodeCluster  (kind B, v10.18 lines 63073-63169) ----
class NodeCluster:
    """
    Simulated multi-node NEBULA network cluster.
    Used for testing network propagation, fork resolution, etc.
    """

    def __init__(self, n_nodes: int = 5):
        self.nodes: Dict[str, ClusterNode] = {}
        self._create_nodes(n_nodes)
        self._connect_mesh()

    def _create_nodes(self, n: int):
        for i in range(n):
            nid = f"node_{i}"
            self.nodes[nid] = ClusterNode(nid)

    def _connect_mesh(self):
        """Connect all nodes to each other (full mesh)."""
        ids = list(self.nodes.keys())
        for i, nid in enumerate(ids):
            for other in ids[i+1:]:
                self.nodes[nid].connect_to(other)
                self.nodes[other].connect_to(nid)

    def broadcast(self, sender_id: str, msg: dict):
        """Broadcast a message from one node to all peers."""
        sender = self.nodes.get(sender_id)
        if not sender:
            return
        for peer_id in sender.peers:
            peer = self.nodes.get(peer_id)
            if peer:
                sender.send(peer, dict(msg))

    def propagation_test(self, msg: dict) -> dict:
        """Test how fast a message propagates through the cluster."""
        origin   = list(self.nodes.keys())[0]
        received = {origin: 0.0}
        queue    = [(origin, 0.0)]

        while queue:
            current_id, delay = queue.pop(0)
            current = self.nodes[current_id]
            for peer_id in current.peers:
                if peer_id not in received:
                    peer = self.nodes[peer_id]
                    propagation_delay = delay + peer.latency_ms
                    received[peer_id] = propagation_delay
                    queue.append((peer_id, propagation_delay))

        max_delay = max(received.values()) if received else 0
        return {
            "nodes_reached":  len(received),
            "total_nodes":    len(self.nodes),
            "max_delay_ms":   max_delay,
            "avg_delay_ms":   sum(received.values()) / len(received) if received else 0,
            "coverage_pct":   f"{len(received)/len(self.nodes)*100:.0f}%",
        }

    def simulate_fork(self) -> dict:
        """Simulate a chain fork and observe resolution."""
        ids      = list(self.nodes.keys())
        group_a  = ids[:len(ids)//2]
        group_b  = ids[len(ids)//2:]

        # Mine one block on each group
        blocks_a = []
        blocks_b = []

        for nid in group_a:
            node = self.nodes[nid]
            h    = node.blockchain.height + 1
            blocks_a.append(f"block_A_{h}")

        for nid in group_b:
            node = self.nodes[nid]
            h    = node.blockchain.height + 1
            blocks_b.append(f"block_B_{h}")

        return {
            "fork_detected":   True,
            "group_a":         group_a,
            "group_b":         group_b,
            "blocks_a":        blocks_a,
            "blocks_b":        blocks_b,
            "resolution":      "Longest chain wins (most cumulative PoW)",
        }

    def cluster_health(self) -> dict:
        heights = [n.blockchain.height for n in self.nodes.values()]
        return {
            "node_count":    len(self.nodes),
            "min_height":    min(heights) if heights else 0,
            "max_height":    max(heights) if heights else 0,
            "in_sync":       len(set(heights)) == 1,
            "topology":      "full_mesh",
        }

# ---- StateChannel  (kind B, v10.18 lines 63313-63399) ----
@dataclass
class StateChannel:
    """
    Generalized state channel between 2+ participants.
    Any off-chain logic can run in the channel.
    On-chain settlement only when channel closes.
    """

    def __init__(self, channel_id: str, participants: List[str],
                  deposits: Dict[str, int]):
        self.channel_id   = channel_id
        self.participants = participants
        self.deposits     = deposits
        self._states:     List[ChannelState] = []
        self._lock        = threading.RLock()

        # Initial state
        initial = StateChannelRound(
            channel_id = channel_id,
            round_num  = 0,
            state_data = {"status": "open"},
            balances   = dict(deposits),
        )
        self._states.append(initial)

    @property
    def current_state(self) -> ChannelState:
        return self._states[-1]

    def propose_state(self, proposer: str,
                       new_state_data: dict,
                       new_balances: Dict[str, int],
                       privkey: int) -> ChannelState:
        """Propose a new channel state."""
        with self._lock:
            cur   = self.current_state
            state = StateChannelRound(
                channel_id = self.channel_id,
                round_num  = cur.round_num + 1,
                state_data = new_state_data,
                balances   = new_balances,
            )
            h     = state.hash().encode()
            r, s  = Secp256k1.sign(privkey, sha256d(h))
            state.sigs[proposer] = Secp256k1.sig_to_der(r, s)
            return state

    def countersign(self, state: ChannelState,
                     signer: str, privkey: int) -> bool:
        """Countersign a proposed state."""
        h    = state.hash().encode()
        r, s = Secp256k1.sign(privkey, sha256d(h))
        state.sigs[signer] = Secp256k1.sig_to_der(r, s)
        if set(state.sigs.keys()) >= set(self.participants):
            with self._lock:
                self._states.append(state)
            return True
        return False

    def close(self, privkey: int,
               closer: str) -> ChannelState:
        """Close the channel with current state."""
        with self._lock:
            final = StateChannelRound(
                channel_id = self.channel_id,
                round_num  = self.current_state.round_num + 1,
                state_data = {"status": "closed"},
                balances   = dict(self.current_state.balances),
                final      = True,
            )
            h    = final.hash().encode()
            r, s = Secp256k1.sign(privkey, sha256d(h))
            final.sigs[closer] = Secp256k1.sig_to_der(r, s)
            self._states.append(final)
            return final

    def channel_info(self) -> dict:
        cs = self.current_state
        return {
            "channel_id":   self.channel_id,
            "participants": self.participants,
            "round":        cs.round_num,
            "state":        cs.state_data,
            "balances":     cs.balances,
            "is_closed":    cs.final,
            "total_rounds": len(self._states),
        }

# ---- NEBULAFullNodeV3  (kind B, v10.18 lines 112603-112786) ----
class NEBULAFullNodeV3:
    """
    NEBULA Full Node v3.0 — Production implementation.
    Uses RealP2PNode, RealMiner, PersistentBlockStore.
    """

    def __init__(self,
                  datadir:    str  = "~/.nebula/mainnet",
                  port:       int  = 8333,
                  api_port:   int  = 8080,
                  network:    str  = "mainnet",
                  mine:       bool = False,
                  miner_addr: str  = FOUNDATION_ADDRESS,
                  threads:    int  = None,
                  seed_nodes: list = None,
                  verbose:    bool = False):

        self.datadir    = os.path.expanduser(datadir)
        self.port       = port
        self.api_port   = api_port
        self.network    = network
        self.do_mine    = mine
        self.miner_addr = miner_addr
        self.threads    = threads
        self.verbose    = verbose
        self._running   = False

        level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            format  = "%(asctime)s [%(name)s] %(levelname)s %(message)s",
            level   = level,
            datefmt = "%Y-%m-%d %H:%M:%S",
        )

        logger_p2p.info(
            f"\n  NEBULA Full Node v3.0.0"
            f"\n  Network  : {network}"
            f"\n  Port     : {port}"
            f"\n  Data dir : {datadir[:60]}"
            f"\n  Mining   : {'YES (' + str(threads or os.cpu_count()) + ' threads)' if mine else 'NO'}"
        )

        # Initialize subsystems
        self.blockchain = NEBULABlockchain()
        self.store      = PersistentBlockStoreLegacy(datadir)
        self.utxo_mgr   = None   # initialized after store loads
        self.p2p        = RealP2PNode(
            self.blockchain,
            port    = port,
            network = network,
            store   = self.store,
        )
        # Add custom seed nodes
        for addr in (seed_nodes or []):
            try:
                host, p = addr.rsplit(":", 1)
                self.p2p.add_known_addr(host, int(p))
            except Exception:
                pass

        self.miner  = None
        if mine:
            self.miner = RealMiner(
                self.blockchain,
                miner_addr,
                threads = threads,
                p2p_node = self.p2p,
                store    = self.store,
            )

        self.api    = NodeRESTAPI(self.blockchain)
        self.utxo_mgr = PersistentUTXOSetLegacy(os.path.join(str(datadir), 'utxo'))
        self.utxo_mgr.sync_from_chain(self.blockchain)

    def run(self):
        """Start the node and run forever."""
        self._running = True
        try:
            self._startup()
            self._main_loop()
        except KeyboardInterrupt:
            logger_p2p.info("\n  Ctrl+C — shutting down gracefully...")
        finally:
            self._shutdown()

    def start_background(self):
        """Start node in background (non-blocking)."""
        self._running = True
        self._startup()
        t = threading.Thread(target=self._main_loop,
                             name="nebula-node", daemon=True)
        t.start()
        return t

    def _startup(self):
        """Initialize all subsystems."""
        logger_p2p.info("  Starting subsystems...")

        # Load chain state from disk
        state = self.store.load_state()
        logger_p2p.info(
            f"  Chain state: height={state['height']} "
            f"best={state['best_hash'][:16]}...")

        # Start P2P network
        self.p2p.start()
        logger_p2p.info(f"  P2P: listening on 0.0.0.0:{self.port}")

        # Start miner
        if self.miner:
            self.miner.start()
            logger_p2p.info(f"  Miner: {self.miner._threads} threads")

        logger_p2p.info("  ✅ Node ready!")
        logger_p2p.info(f"  REST API: http://0.0.0.0:{self.api_port}")
        logger_p2p.info(f"  Explorer: http://0.0.0.0:{self.api_port}/")

    def _main_loop(self):
        """Main event loop — runs forever."""
        last_stats  = time.time()
        last_save   = time.time()
        STATS_EVERY = 60   # print stats every 60s
        SAVE_EVERY  = 300  # save UTXO every 5min

        while self._running:
            now = time.time()

            # Print stats periodically
            if now - last_stats >= STATS_EVERY:
                self._print_stats()
                last_stats = now

            # Save UTXO snapshot
            if now - last_save >= SAVE_EVERY:
                self.utxo_mgr.save_if_needed(self.blockchain.height)
                last_save = now

            time.sleep(1)

    def _print_stats(self):
        bc  = self.blockchain
        p2p = self.p2p.network_stats()
        logger_p2p.info(
            f"\n  ─── Node Status ───────────────────────────────\n"
            f"  Height    : {bc.height}\n"
            f"  Mempool   : {bc.mempool.size()} txs\n"
            f"  Peers     : {p2p['connected_peers']}\n"
            f"  Blocks rcv: {p2p['blocks_received']}\n"
            f"  Txs rcv   : {p2p['txs_received']}\n" +
            (f"  Hash rate : {self.miner.hash_rate_str()}\n"
             f"  Mined     : {self.miner.blocks_mined} blocks\n"
             if self.miner else "") +
            f"  ─────────────────────────────────────────────"
        )

    def _shutdown(self):
        """Graceful shutdown."""
        logger_p2p.info("  Shutting down...")
        self._running = False
        if self.miner:
            self.miner.stop()
        if self.utxo_mgr:
            self.utxo_mgr.shutdown_save()
        self.p2p.stop()
        logger_p2p.info("  ✅ Node stopped cleanly")

    def node_status(self) -> dict:
        bc  = self.blockchain
        p2p = self.p2p.network_stats()
        st  = self.store.storage_stats()
        return {
            "version":     "NEBULA v3.0.0",
            "network":     self.network,
            "height":      bc.height,
            "best_hash":   bc.tip.hash if bc.height >= 0 else "genesis",
            "mempool":     bc.mempool.size(),
            "peers":       p2p["connected_peers"],
            "mining":      self.do_mine,
            "hash_rate":   self.miner.hash_rate_str() if self.miner else "off",
            "blocks_mined": self.miner.blocks_mined if self.miner else 0,
            "storage":     st,
            "uptime_secs": int(time.time() - self.miner.start_time)
                           if self.miner and self.miner.start_time > 0 else 0,
        }

# ---- GenesisVerifier  (kind C, v10.18 lines 2619-2655) ----
class GenesisVerifier:
    """Verify that the stored genesis block matches hard-coded parameters."""

    GENESIS_HASH    = "00000b74d5624d41e2a590950aaab23747bfc929f08192967b74a233a800f1b1"
    GENESIS_NONCE   = 819391
    GENESIS_BITS    = 0x1e0fffff
    GENESIS_TS      = 1_742_083_200
    GENESIS_REWARD  = 50 * 10**DECIMALS
    GENESIS_MSG     = "NEBULA — Financial Freedom for All Humanity — 2025/03/16"
    GENESIS_ADDR    = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"

    @classmethod
    def verify(cls, block: "Block") -> tuple:
        errors = []
        bh = block.header.hash()
        if bh != cls.GENESIS_HASH:
            errors.append(f"Hash mismatch: {bh} != {cls.GENESIS_HASH}")
        if block.header.nonce != cls.GENESIS_NONCE:
            errors.append(f"Nonce mismatch: {block.header.nonce} != {cls.GENESIS_NONCE}")
        if block.header.bits != cls.GENESIS_BITS:
            errors.append(f"Bits mismatch")
        if block.header.timestamp != cls.GENESIS_TS:
            errors.append(f"Timestamp mismatch")
        if len(block.transactions) < 1:
            errors.append("No transactions in genesis block")
        else:
            cb = block.transactions[0]
            if cb.outputs[0].value != cls.GENESIS_REWARD:
                errors.append(f"Coinbase reward mismatch")
        return len(errors) == 0, errors

    @classmethod
    def report(cls, block: "Block") -> str:
        ok, errors = cls.verify(block)
        if ok:
            return f"Genesis block verified ✅\n  Hash : {cls.GENESIS_HASH}\n  Nonce: {cls.GENESIS_NONCE}\n  Date : 2025-03-16"
        return "Genesis FAILED:\n" + "\n".join(f"  ✗ {e}" for e in errors)

# ---- StandardScriptChecker  (kind C, v10.18 lines 2661-2693) ----
class StandardScriptChecker:
    """
    Determine if a script is 'standard' (relay policy).
    Non-standard scripts are not relayed by default.
    Standard: P2PKH, P2PK, bare-multisig (≤3-of-3), OP_RETURN (≤80B), P2SH
    """

    MAX_OP_RETURN = 80

    @classmethod
    def is_standard(cls, script: bytes) -> tuple:
        if not script:
            return False, "empty"
        # P2PKH: 25 bytes OP_DUP OP_HASH160 <20> OP_EQUALVERIFY OP_CHECKSIG
        if (len(script)==25 and script[0]==0x76 and script[1]==0xa9
                and script[2]==0x14 and script[-2]==0x88 and script[-1]==0xac):
            return True, "P2PKH"
        # P2PK: <33|65> OP_CHECKSIG
        if len(script) in (35,67) and script[-1]==0xac:
            return True, "P2PK"
        # OP_RETURN
        if script[0]==0x6a:
            if len(script)-1 <= cls.MAX_OP_RETURN:
                return True, "OP_RETURN"
            return False, f"OP_RETURN too large ({len(script)-1}>{cls.MAX_OP_RETURN})"
        # P2SH: OP_HASH160 <20> OP_EQUAL
        if (len(script)==23 and script[0]==0xa9 and script[1]==0x14
                and script[-1]==0x87):
            return True, "P2SH"
        # Bare multisig (≤3-of-3)
        if len(script) > 3 and script[-1]==0xae:
            return True, "MULTISIG"
        return False, "non-standard"

# ---- CoinSelectorOriginal  (kind C, v10.18 lines 3436-3493) ----
class CoinSelectorOriginal:
    """
    UTXO coin selection algorithms.
    Chooses which UTXOs to spend for a given target amount.

    Algorithms:
      1. BnB  — Branch and Bound (minimize change output)
      2. FIFO — First In First Out (spend oldest first)
      3. Rand — Random selection
    """

    @staticmethod
    def bnb(utxos, target: int, fee_per_byte: int = 1,
            input_size: int = 148) -> _WOpt[_WList]:
        """Branch and Bound — tries to find exact match first."""
        # Sort by value descending
        sorted_utxos = sorted(utxos, key=lambda u: u.value, reverse=True)
        # Try exact match within tolerance
        tolerance = fee_per_byte * input_size * 2
        for utxo in sorted_utxos:
            if abs(utxo.value - target) <= tolerance:
                return [utxo]
        # Fall back to accumulation
        return CoinSelector.accumulate(sorted_utxos, target, fee_per_byte, input_size)

    @staticmethod
    def fifo(utxos, target: int, fee_per_byte: int = 1,
             input_size: int = 148) -> _WOpt[_WList]:
        """FIFO — spend oldest UTXOs first."""
        sorted_utxos = sorted(utxos, key=lambda u: u.height)
        return CoinSelector.accumulate(sorted_utxos, target, fee_per_byte, input_size)

    @staticmethod
    def accumulate(utxos, target: int, fee_per_byte: int,
                   input_size: int) -> _WOpt[_WList]:
        """Accumulate UTXOs until target is met.
        Final check was `total >= 0` which incorrectly returned
        a selection even when total < target (e.g. 0 <= total < target),
        producing underfunded transactions. Corrected to `total >= target`."""
        selected = []
        total    = 0
        for utxo in utxos:
            if total >= target:
                break
            selected.append(utxo)
            total += utxo.value
            # Subtract per-input fee cost
            total -= fee_per_byte * input_size
        if total >= target:   # was `>= 0` — must verify target is covered
            return selected
        return None

    @staticmethod
    def estimate_fee(n_inputs: int, n_outputs: int,
                     fee_rate: int = 1) -> int:
        """Estimate TX fee: 10 + 148*inputs + 34*outputs bytes."""
        size = 10 + 148 * n_inputs + 34 * n_outputs
        return size * fee_rate

# ---- MultiSigWallet  (kind C, v10.18 lines 3496-3534) ----
class MultiSigWallet:
    """
    m-of-n multi-signature wallet.
    Supports 2-of-3 for treasury/escrow use cases.
    """

    def __init__(self, m: int, n: int, public_keys: _WList[bytes]):
        if not (1 <= m <= n <= 16):
            raise ValueError(f"Invalid m-of-n: {m}/{n}")
        if len(public_keys) != n:
            raise ValueError(f"Expected {n} keys, got {len(public_keys)}")
        self.m           = m
        self.n           = n
        self.public_keys = public_keys

    def redeem_script(self) -> bytes:
        """OP_m [pubkeys] OP_n OP_CHECKMULTISIG"""
        script  = bytes([0x50 + self.m])  # OP_m
        for pk in self.public_keys:
            script += bytes([len(pk)]) + pk
        script += bytes([0x50 + self.n])  # OP_n
        script += bytes([0xae])           # OP_CHECKMULTISIG
        return script

    def p2sh_address(self) -> str:
        """P2SH address for NEBULA — base58check encoded."""
        rs   = self.redeem_script()
        h160 = hashlib.new('ripemd160', hashlib.sha256(rs).digest()).digest()
        return base58check_encode(h160, SCRIPT_ADDRESS_VERSION)

    def info(self) -> dict:
        return {
            "type"         : f"{self.m}-of-{self.n} multisig",
            "m"            : self.m,
            "n"            : self.n,
            "redeem_script": self.redeem_script().hex(),
            "address"      : self.p2sh_address(),
            "signers_needed": self.m,
        }

# ---- WatchOnlyWallet  (kind C, v10.18 lines 3537-3559) ----
class WatchOnlyWallet:
    """
    Watch-only wallet — tracks addresses without private keys.
    Used for read-only monitoring (e.g. on an online node).
    """

    def __init__(self):
        self._addrs : _WDict[str, dict] = {}

    def add(self, address: str, label: str = ""):
        self._addrs[address] = {"label": label, "added": _wtime.time()}

    def remove(self, address: str):
        self._addrs.pop(address, None)

    def is_watching(self, address: str) -> bool:
        return address in self._addrs

    def list_addresses(self) -> _WList[dict]:
        return [{"address": a, **info} for a, info in self._addrs.items()]

    def count(self) -> int:
        return len(self._addrs)

# ---- SighashTaproot  (kind C, v10.18 lines 19279-19343) ----
class SighashTaproot:
    """
    BIP341 sighash for Taproot (SegWit v1) inputs.
    Covers ALL outputs (not just one) improving hardware wallet security.
    Supports keypath and scriptpath spending.
    """

    @staticmethod
    def compute(tx, input_index: int,
                prevouts: List[Tuple[int, bytes]],
                sighash_type: int = 0,
                ext_flag: int = 0) -> bytes:
        """
        BIP341 Taproot sighash.
        prevouts: list of (value, script_pubkey) for all inputs
        sighash_type: 0=DEFAULT(all), 1=ALL, 2=NONE, 3=SINGLE
        Returns 32-byte hash.
        """
        def _varint(n):
            if n < 0xfd: return bytes([n])
            elif n <= 0xffff: return b'\xfd' + struct.pack('<H', n)
            else: return b'\xfe' + struct.pack('<I', n)

        def sha_tag(tag, data):
            return _tagged_hash(f"TapSighash/{tag}" if '/' not in tag else tag, data)

        epoch      = bytes([0])   # BIP341 epoch
        sht_byte   = bytes([sighash_type])
        version    = struct.pack('<i', tx.version)
        locktime   = struct.pack('<I', tx.locktime)

        # sha_prevouts, sha_amounts, sha_scriptpubkeys, sha_sequences
        prevout_buf  = b''.join(bytes.fromhex(i.outpoint.txid)[::-1] +
                                struct.pack('<I', i.outpoint.index)
                                for i in tx.inputs)
        amounts_buf  = b''.join(struct.pack('<q', v) for v, _ in prevouts)
        scripts_buf  = b''.join(_varint(len(s)) + s for _, s in prevouts)
        seq_buf      = b''.join(struct.pack('<I', i.sequence) for i in tx.inputs)

        sha_prevouts   = _tagged_hash("TapSighash", prevout_buf)
        sha_amounts    = _tagged_hash("TapSighash", amounts_buf)
        sha_scripts    = _tagged_hash("TapSighash", scripts_buf)
        sha_sequences  = _tagged_hash("TapSighash", seq_buf)

        def _ser_out(o):
            return struct.pack('<q', o.value) + _varint(len(o.script_pubkey)) + o.script_pubkey
        out_buf = b''.join(_ser_out(o) for o in tx.outputs)
        sha_outputs = _tagged_hash("TapSighash", out_buf)

        spend_type = bytes([ext_flag * 2 + (0 if sighash_type in (0,1) else 0)])

        inp = tx.inputs[input_index]
        inp_value, inp_script = prevouts[input_index]
        outpoint = bytes.fromhex(inp.outpoint.txid)[::-1] + struct.pack('<I', inp.outpoint.index)

        preimage = (
            epoch + sht_byte + version + locktime +
            sha_prevouts + sha_amounts + sha_scripts + sha_sequences +
            sha_outputs + spend_type +
            outpoint +
            struct.pack('<q', inp_value) +
            _varint(len(inp_script)) + inp_script +
            struct.pack('<I', inp.sequence)
        )
        return _tagged_hash("TapSighash", preimage)

# ---- TaprootSpender  (kind C, v10.18 lines 19346-19390) ----
class TaprootSpender:
    """
    High-level Taproot keypath spending.
    Signs Taproot inputs using Schnorr signatures.
    """

    @staticmethod
    def sign_input(tx, input_index: int,
                   privkey: int,
                   prevouts: List[Tuple[int, bytes]],
                   sighash_type: int = 0) -> bytes:
        """
        Sign a Taproot keypath input.
        Returns 64 or 65-byte Schnorr witness element.
        """
        # Tweak the private key
        P = Schnorr._point_mul(privkey, Schnorr._G())
        if P[1] % 2 != 0:
            privkey = Schnorr.N - privkey
        xonly_pub = P[0].to_bytes(32, 'big')
        tweak     = _tagged_hash("TapTweak", xonly_pub)
        t         = int.from_bytes(tweak, 'big')
        sk_tweaked = (privkey + t) % Schnorr.N

        msg = SighashTaproot.compute(tx, input_index, prevouts, sighash_type)
        sig = Schnorr.sign(sk_tweaked, msg)
        # Append sighash type byte if not DEFAULT(0)
        if sighash_type != 0:
            sig += bytes([sighash_type])
        return sig

    @staticmethod
    def verify_input(tx, input_index: int,
                     xonly_pubkey: bytes,
                     prevouts: List[Tuple[int, bytes]],
                     sig: bytes) -> bool:
        """Verify a Taproot keypath input."""
        sighash_type = 0
        if len(sig) == 65:
            sighash_type = sig[-1]
            sig = sig[:64]
        elif len(sig) != 64:
            return False
        msg = SighashTaproot.compute(tx, input_index, prevouts, sighash_type)
        return Schnorr.verify(xonly_pubkey, msg, sig)

# ---- WitnessSerializer  (kind C, v10.18 lines 19393-19433) ----
class WitnessSerializer:
    """
    Serialize / deserialize segregated witness data.
    Witness data is NOT included in txid computation (malleability fix).
    Format: [num_items][len][item]... per input
    """

    @staticmethod
    def serialize(witnesses: List[List[bytes]]) -> bytes:
        """Serialize witness stack for all inputs"""
        out = b''
        for stack in witnesses:
            out += _encode_varint_sw(len(stack))
            for item in stack:
                out += _encode_varint_sw(len(item)) + item
        return out

    @staticmethod
    def deserialize(data: bytes, num_inputs: int) -> Tuple[List[List[bytes]], int]:
        """Deserialize witness stacks. Returns (witnesses, bytes_consumed)"""
        witnesses = []
        offset = 0
        for _ in range(num_inputs):
            count, offset = _decode_varint_sw(data, offset)
            stack = []
            for _ in range(count):
                length, offset = _decode_varint_sw(data, offset)
                stack.append(data[offset:offset+length])
                offset += length
            witnesses.append(stack)
        return witnesses, offset

    @staticmethod
    def weight(witnesses: List[List[bytes]]) -> int:
        """Calculate witness weight (1 WU per witness byte)"""
        total = 2  # segwit marker + flag
        for stack in witnesses:
            total += 1  # stack item count
            for item in stack:
                total += 1 + len(item)  # varint + data
        return total

# ---- SegWitTxBuilder  (kind C, v10.18 lines 19447-19521) ----
class SegWitTxBuilder:
    """
    Build SegWit-aware transactions.
    Handles P2WPKH, P2WSH, P2TR inputs/outputs.
    Computes correct weight and virtual bytes (vbytes).
    """

    def __init__(self, tx, witnesses: List[List[bytes]] = None):
        self.tx        = tx
        self.witnesses = witnesses or [[] for _ in tx.inputs]

    def add_witness(self, input_index: int, stack: List[bytes]):
        """Set witness stack for an input"""
        while len(self.witnesses) <= input_index:
            self.witnesses.append([])
        self.witnesses[input_index] = stack

    def sign_p2wpkh(self, input_index: int, privkey: int,
                    value: int, sighash_type: int = 1):
        """Sign a P2WPKH input. Witness = [sig, pubkey]"""
        pub_bytes  = Secp256k1.pubkey_to_bytes(
                        Secp256k1.point_mul(privkey, Secp256k1.G()))
        h160       = hashlib.new('ripemd160', hashlib.sha256(pub_bytes).digest()).digest()
        # P2PKH script code for BIP143
        script_code = (bytes([0x76, 0xa9, 0x14]) + h160 +
                       bytes([0x88, 0xac]))
        sighash = SighashSegWitV0.compute(
                    self.tx, input_index, script_code, value, sighash_type)
        r, s    = Secp256k1.sign(privkey, sighash)
        der     = Secp256k1.sig_to_der(r, s) + bytes([sighash_type])
        self.add_witness(input_index, [der, pub_bytes])

    def sign_p2tr(self, input_index: int, privkey: int,
                  prevouts: List[Tuple[int, bytes]],
                  sighash_type: int = 0):
        """Sign a P2TR keypath input. Witness = [schnorr_sig]"""
        sig = TaprootSpender.sign_input(
                self.tx, input_index, privkey, prevouts, sighash_type)
        self.add_witness(input_index, [sig])

    def serialize_segwit(self) -> bytes:
        """Serialize transaction with witness data (BIP144 format)"""
        tx  = self.tx
        out = struct.pack('<i', tx.version)
        out += b'\x00\x01'   # segwit marker + flag
        out += _encode_varint_sw(len(tx.inputs))
        for inp in tx.inputs:
            out += inp.serialize()
        out += _encode_varint_sw(len(tx.outputs))
        for txout in tx.outputs:
            out += txout.serialize()
        out += WitnessSerializer.serialize(self.witnesses)
        out += struct.pack('<I', tx.locktime)
        return out

    def weight(self) -> int:
        """Transaction weight in weight units (WU)"""
        # Base weight (non-witness * 4) + witness weight * 1
        base_size = len(self.tx.serialize())
        wit_size  = WitnessSerializer.weight(self.witnesses)
        return base_size * 4 + wit_size

    def vbytes(self) -> int:
        """Virtual bytes = ceil(weight / 4)"""
        return (self.weight() + 3) // 4

    def txid(self) -> str:
        """txid = double-sha256 of base serialization (no witness)"""
        raw = self.tx.serialize()
        return hashlib.sha256(hashlib.sha256(raw).digest()).digest()[::-1].hex()

    def wtxid(self) -> str:
        """wtxid = double-sha256 of full witness serialization"""
        raw = self.serialize_segwit()
        return hashlib.sha256(hashlib.sha256(raw).digest()).digest()[::-1].hex()

# ---- SegWitAddressRegistry  (kind C, v10.18 lines 19624-19665) ----
class SegWitAddressRegistry:
    """
    Registry mapping SegWit addresses to their type and program.
    Used by wallet and node to track P2WPKH / P2TR outputs.
    """

    def __init__(self, hrp: str = "nbl"):
        self.hrp   = hrp
        self._keys : Dict[str, dict] = {}   # address -> info

    def register_p2wpkh(self, privkey: int) -> str:
        """Register a P2WPKH address and return it"""
        pub = Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(privkey, Secp256k1.G()))
        addr = SegWitScript.p2wpkh_address(pub, self.hrp)
        self._keys[addr] = {
            "type"    : "P2WPKH",
            "privkey" : privkey,
            "pubkey"  : pub,
            "script"  : SegWitScript.p2wpkh(pub),
        }
        return addr

    def register_p2tr(self, privkey: int) -> str:
        """Register a P2TR address and return it"""
        xonly, script = SegWitScript.p2tr_from_privkey(privkey)
        addr = SegWitScript.p2tr_address(xonly, self.hrp)
        self._keys[addr] = {
            "type"    : "P2TR",
            "privkey" : privkey,
            "xonly"   : xonly,
            "script"  : script,
        }
        return addr

    def get(self, address: str) -> Optional[dict]:
        return self._keys.get(address)

    def list_addresses(self) -> List[dict]:
        return [{"address": a, **info} for a, info in self._keys.items()]

    def address_count(self) -> int:
        return len(self._keys)

# ---- TaprootTree  (kind C, v10.18 lines 19694-19764) ----
class TaprootTree:
    """
    Build a Taproot script tree.
    Computes the Merkle root (tweak) for key path + script path spending.
    """

    def __init__(self, leaves: List[TapLeaf] = None):
        self.leaves = leaves or []
        self._root  = None

    def add_leaf(self, script: bytes, leaf_version: int = TapLeaf.TAPSCRIPT_LEAF_VERSION):
        self.leaves.append(TapLeaf(script, leaf_version))
        self._root = None

    def root(self) -> Optional[bytes]:
        """Compute Merkle root of the script tree"""
        if not self.leaves:
            return None
        if self._root is None:
            nodes = list(self.leaves)
            while len(nodes) > 1:
                if len(nodes) % 2 == 1:
                    nodes.append(nodes[-1])
                nodes = [TapBranch(nodes[i], nodes[i+1])
                         for i in range(0, len(nodes), 2)]
            self._root = nodes[0].hash()
        return self._root

    def tweaked_key(self, internal_key: bytes) -> bytes:
        """
        Compute tweaked x-only output key.
        output_key = internal_key + H_TapTweak(internal_key || merkle_root) * G
        """
        root = self.root()
        if root:
            tweak = _tagged_hash("TapTweak", internal_key + root)
        else:
            tweak = _tagged_hash("TapTweak", internal_key)
        t  = int.from_bytes(tweak, 'big')
        Px = int.from_bytes(internal_key, 'big')
        P  = Schnorr._lift_x(Px)
        if P is None: raise ValueError("Invalid internal key")
        Q  = Schnorr._point_add(P, Schnorr._point_mul(t, Schnorr._G()))
        if Q is None: raise ValueError("Tweaked key is point at infinity")
        return Q[0].to_bytes(32, 'big')

    def control_block(self, leaf: TapLeaf, internal_key: bytes) -> bytes:
        """
        Build control block for script path spending.
        Required to spend a tapscript leaf.
        """
        # Find sibling hashes (Merkle proof)
        leaf_hash = leaf.hash()
        nodes     = list(self.leaves)
        proof     = []
        idx       = next((i for i,l in enumerate(nodes) if l.hash() == leaf_hash), None)
        if idx is None:
            raise ValueError("Leaf not in tree")

        while len(nodes) > 1:
            if len(nodes) % 2 == 1:
                nodes.append(nodes[-1])
            sibling_idx = idx ^ 1
            proof.append(nodes[sibling_idx].hash())
            nodes = [TapBranch(nodes[i], nodes[i+1])
                     for i in range(0, len(nodes), 2)]
            idx //= 2

        parity    = 0   # simplified: assume even y output key
        cb_byte   = bytes([leaf.leaf_version | parity])
        return cb_byte + internal_key + b''.join(proof)

# ---- SegWitStats  (kind C, v10.18 lines 19770-19803) ----
class SegWitStats:
    """Track SegWit adoption statistics"""

    def __init__(self):
        self.total_txs    = 0
        self.segwit_txs   = 0
        self.taproot_txs  = 0
        self.p2wpkh_txs   = 0
        self.p2wsh_txs    = 0
        self.total_weight = 0
        self.total_vbytes = 0

    def record_tx(self, tx_type: str, weight: int):
        self.total_txs += 1
        vb = (weight + 3) // 4
        self.total_weight += weight
        self.total_vbytes += vb
        if tx_type in ("P2WPKH","P2WSH","P2TR"):
            self.segwit_txs += 1
        if tx_type == "P2TR":  self.taproot_txs += 1
        if tx_type == "P2WPKH": self.p2wpkh_txs += 1
        if tx_type == "P2WSH":  self.p2wsh_txs  += 1

    def adoption_rate(self) -> float:
        return self.segwit_txs / max(1, self.total_txs)

    def to_dict(self) -> dict:
        return {
            "total_txs"      : self.total_txs,
            "segwit_txs"     : self.segwit_txs,
            "taproot_txs"    : self.taproot_txs,
            "segwit_adoption": f"{self.adoption_rate()*100:.1f}%",
            "avg_vbytes"     : self.total_vbytes // max(1, self.total_txs),
        }

# ---- OnionPacket  (kind C, v10.18 lines 20268-20338) ----
class OnionPacket:
    """
    BOLT #4 Sphinx onion routing.
    Each hop can only see its own layer — source-routed, privacy-preserving.
    Packet size: 1366 bytes regardless of route length.
    """
    VERSION         = 0
    HMAC_SIZE       = 32
    PUBKEY_SIZE     = 33
    HOP_DATA_SIZE   = 65
    MAX_HOPS        = 20
    PACKET_SIZE     = 1 + PUBKEY_SIZE + MAX_HOPS * HOP_DATA_SIZE + HMAC_SIZE

    @staticmethod
    def _ecdh(privkey: int, pubkey_bytes: bytes) -> bytes:
        """ECDH shared secret"""
        x = int.from_bytes(pubkey_bytes[1:33], 'big')
        prefix = pubkey_bytes[0]
        P_sq = Secp256k1.P
        y_sq = (pow(x, 3, P_sq) + 7) % P_sq
        y    = pow(y_sq, (P_sq+1)//4, P_sq)
        if (y % 2 == 0) != (prefix == 0x02):
            y = P_sq - y
        point = Secp256k1.point_mul(privkey, (x, y))
        return hashlib.sha256(Secp256k1.pubkey_to_bytes((point[0], point[1]))).digest()

    @classmethod
    def build(cls, hops: List[dict], session_key: int) -> bytes:
        """
        Build onion packet for a route.
        hops: list of {"pubkey": bytes, "payload": bytes}
        Returns PACKET_SIZE bytes.
        """
        if len(hops) > cls.MAX_HOPS:
            raise ValueError(f"Too many hops: {len(hops)} > {cls.MAX_HOPS}")

        session_pub = Secp256k1.pubkey_to_bytes(
            Secp256k1.point_mul(session_key, Secp256k1.G()))

        # Build routing info (simplified — production uses Sphinx)
        routing_info = b'\x00' * (cls.MAX_HOPS * cls.HOP_DATA_SIZE)
        hmac         = b'\x00' * cls.HMAC_SIZE

        # Encrypt each hop (simplified representation)
        for i, hop in enumerate(reversed(hops)):
            shared   = cls._ecdh(session_key, hop["pubkey"])
            rho      = hashlib.sha256(b"rho" + shared).digest()
            payload  = hop.get("payload", b'\x00' * cls.HOP_DATA_SIZE)[:cls.HOP_DATA_SIZE]
            # XOR-stream encryption (simplified)
            stream   = hashlib.sha256(rho + bytes([i])).digest() * 3
            encrypted = bytes(a^b for a,b in zip(
                payload + hmac, stream[:len(payload)+cls.HMAC_SIZE]))
            hmac     = encrypted[-cls.HMAC_SIZE:]

        return (bytes([cls.VERSION]) + session_pub +
                routing_info + hmac)

    @classmethod
    def peel(cls, privkey: int, session_pub: bytes,
             routing_info: bytes) -> Tuple[bytes, bytes, bytes]:
        """
        Peel one layer of the onion.
        Returns (payload, next_routing_info, next_hmac).
        """
        shared = cls._ecdh(privkey, session_pub)
        rho    = hashlib.sha256(b"rho" + shared).digest()
        # Simplified decryption
        payload     = routing_info[:cls.HOP_DATA_SIZE]
        next_info   = routing_info[cls.HOP_DATA_SIZE:] + b'\x00' * cls.HOP_DATA_SIZE
        next_hmac   = hashlib.sha256(rho + next_info).digest()
        return payload, next_info, next_hmac

# ---- LightningInvoice  (kind C, v10.18 lines 20446-20503) ----
@dataclass
class LightningInvoice:
    """
    BOLT #11 Lightning invoice.
    Encodes payment request: amount, payee, description, expiry.
    """
    payment_hash  : bytes
    preimage      : bytes
    amount_msat   : int
    description   : str
    payee_node_id : bytes
    expiry_secs   : int   = 3600
    cltv_expiry   : int   = CLTV_EXPIRY_DELTA
    created_at    : float = field(default_factory=time.time)
    paid          : bool  = False
    paid_at       : Optional[float] = None

    @classmethod
    def create(cls, amount_msat: int, description: str,
               node_id: bytes) -> 'LightningInvoice':
        """Create a new payment invoice"""
        preimage = generate_payment_preimage()
        phash    = payment_hash(preimage)
        return cls(
            payment_hash  = phash,
            preimage      = preimage,
            amount_msat   = amount_msat,
            description   = description,
            payee_node_id = node_id,
        )

    def is_expired(self) -> bool:
        return time.time() > self.created_at + self.expiry_secs

    def mark_paid(self):
        self.paid    = True
        self.paid_at = time.time()

    def encode(self) -> str:
        """
        Simplified bech32-encoded invoice string.
        Real BOLT#11 uses full bech32 with TLV fields.
        """
        prefix = f"lnnbl{self.amount_msat}m"
        data   = self.payment_hash.hex()[:20]
        return f"{prefix}1{data}..."

    def to_dict(self) -> dict:
        return {
            "payment_hash"  : self.payment_hash.hex(),
            "amount_msat"   : self.amount_msat,
            "amount_nbl"    : f"{self.amount_msat/1000/10**DECIMALS:.9f}",
            "description"   : self.description,
            "expiry_secs"   : self.expiry_secs,
            "created_at"    : self.created_at,
            "is_expired"    : self.is_expired(),
            "paid"          : self.paid,
        }

# ---- LightningNode  (kind C, v10.18 lines 20506-20646) ----
class LightningNode:
    """
    Full Lightning Network node.
    Manages channels, invoices, routing, and payments.
    Integrates with NEBULA blockchain for on-chain operations.
    """

    def __init__(self, node_id: bytes, blockchain: 'NEBULABlockchain' = None):
        self.node_id    = node_id
        self.blockchain = blockchain
        self.channels   : Dict[bytes, PaymentChannel] = {}
        self.invoices   : Dict[bytes, LightningInvoice] = {}
        self.graph      = ChannelGraph()
        self._lock      = threading.RLock()
        self._running   = False

    # ── Channel management ───────────────────────────────────────
    def open_channel(self, remote_node_id: bytes,
                     capacity_sat: int,
                     push_msat: int = 0) -> Tuple[bool, str, Optional[PaymentChannel]]:
        """Open a new payment channel with remote node"""
        with self._lock:
            seed    = secrets.token_bytes(32)
            lk      = ChannelKeys.from_seed(seed)
            rk      = ChannelKeys.from_seed(secrets.token_bytes(32))
            chan_id = secrets.token_bytes(8)

            channel = PaymentChannel(
                channel_id     = chan_id,
                local_node_id  = self.node_id,
                remote_node_id = remote_node_id,
                local_keys     = lk,
                remote_keys    = rk,
                capacity_sat   = capacity_sat,
                is_initiator   = True,
            )
            channel.local_msats  = capacity_sat * 1000 - push_msat
            channel.remote_msats = push_msat
            self.channels[chan_id] = channel
            return True, "Channel opened (pending funding)", channel

    def close_channel(self, channel_id: bytes,
                      force: bool = False) -> Tuple[bool, str]:
        """Close a payment channel"""
        with self._lock:
            ch = self.channels.get(channel_id)
            if ch is None:
                return False, "Channel not found"
            if force:
                commitment = ch.force_close()
                return True, f"Force closed: {json.dumps(commitment)[:80]}..."
            else:
                return ch.initiate_close()

    # ── Payments ─────────────────────────────────────────────────
    def create_invoice(self, amount_msat: int,
                       description: str) -> LightningInvoice:
        """Create a payment invoice"""
        inv = LightningInvoice.create(amount_msat, description, self.node_id)
        with self._lock:
            self.invoices[inv.payment_hash] = inv
        return inv

    def pay_invoice(self, invoice: LightningInvoice) -> Tuple[bool, str]:
        """
        Pay a Lightning invoice.
        Finds route, sends payment through channel network.
        """
        with self._lock:
            if invoice.is_expired():
                return False, "Invoice expired"

            # Find a channel with sufficient balance
            best_channel = None
            for ch in self.channels.values():
                if (ch.state == ChannelState.NORMAL and
                    ch.remote_node_id == invoice.payee_node_id and
                    ch.local_msats - ch.pending_outgoing_msat() >= invoice.amount_msat):
                    best_channel = ch
                    break

            if best_channel is None:
                # Try routing through channel graph
                route = self.graph.find_route(
                    self.node_id, invoice.payee_node_id, invoice.amount_msat)
                if not route:
                    return False, "No route to destination"
                return True, f"Routed via {len(route)} hops (pending)"

            ok, reason, htlc = best_channel.offer_htlc(
                invoice.amount_msat, invoice.payment_hash,
                int(time.time() // 600) + CLTV_EXPIRY_DELTA)

            if not ok:
                return False, reason

            # Simulate immediate settlement (same-node payment)
            if best_channel.remote_node_id == self.node_id:
                best_channel.settle_htlc(htlc.htlc_id, invoice.preimage)
                invoice.mark_paid()

            return True, f"Payment sent: {htlc.htlc_id}"

    def receive_payment(self, payment_hash_hex: str,
                        preimage_hex: str) -> Tuple[bool, str]:
        """Receive payment by revealing preimage"""
        phash    = bytes.fromhex(payment_hash_hex)
        preimage = bytes.fromhex(preimage_hex)
        if not verify_preimage(preimage, phash):
            return False, "Invalid preimage"
        with self._lock:
            inv = self.invoices.get(phash)
            if inv:
                inv.mark_paid()
            return True, "Payment received"

    # ── Stats ────────────────────────────────────────────────────
    def get_stats(self) -> dict:
        channels = list(self.channels.values())
        total_local  = sum(c.local_msats  for c in channels) // 1000
        total_remote = sum(c.remote_msats for c in channels) // 1000
        return {
            "node_id"          : self.node_id.hex(),
            "channels_total"   : len(channels),
            "channels_active"  : sum(1 for c in channels
                                     if c.state == ChannelState.NORMAL),
            "local_balance_sat": total_local,
            "remote_balance_sat":total_remote,
            "local_balance_nbl": f"{total_local/10**DECIMALS:.9f}",
            "pending_htlcs"    : sum(len(c.pending_htlcs) for c in channels),
            "invoices"         : len(self.invoices),
            "invoices_paid"    : sum(1 for i in self.invoices.values() if i.paid),
            "graph_nodes"      : self.graph.node_count(),
            "graph_channels"   : self.graph.channel_count(),
        }

    def list_channels(self) -> List[dict]:
        return [ch.to_dict() for ch in self.channels.values()]

    def list_invoices(self) -> List[dict]:
        return [inv.to_dict() for inv in self.invoices.values()]

# ---- StratumV2Message  (kind C, v10.18 lines 21197-21244) ----
class StratumV2Message:
    """
    Stratum v2 binary message format.
    Fixed header: extension_type(2) + msg_type(1) + channel_id(4) + length(3)
    More efficient than V1 JSON: ~30% bandwidth reduction.
    """
    HEADER_SIZE = 6

    # Message types
    SETUP_CONNECTION         = 0x00
    SETUP_CONNECTION_SUCCESS = 0x01
    SETUP_CONNECTION_ERROR   = 0x02
    NEW_MINING_JOB          = 0x1f
    SET_NEW_PREV_HASH        = 0x20
    SUBMIT_SHARES_STANDARD  = 0x1e
    SUBMIT_SHARES_SUCCESS   = 0x1c
    SUBMIT_SHARES_ERROR     = 0x1d
    SET_DIFFICULTY           = 0x02
    OPEN_STANDARD_MINING_CHANNEL = 0x10
    OPEN_STANDARD_MINING_CHANNEL_SUCCESS = 0x11

    def __init__(self, msg_type: int, channel_id: int = 0, payload: bytes = b''):
        self.extension_type = 0
        self.msg_type   = msg_type
        self.channel_id = channel_id
        self.payload    = payload

    def encode(self) -> bytes:
        length = len(self.payload)
        header = (struct.pack('<H', self.extension_type) +
                  struct.pack('<B', self.msg_type) +
                  struct.pack('<I', self.channel_id) +
                  struct.pack('<I', length)[:3])
        return header + self.payload

    @classmethod
    def decode(cls, data: bytes) -> Optional['StratumV2Message']:
        if len(data) < cls.HEADER_SIZE:
            return None
        ext_type   = struct.unpack_from('<H', data, 0)[0]
        msg_type   = data[2]
        channel_id = struct.unpack_from('<I', data[3:7]+b'\x00')[0]
        length     = struct.unpack_from('<I', data[3:7]+b'\x00')[0] & 0xFFFFFF
        if len(data) < cls.HEADER_SIZE + length:
            return None
        payload = data[cls.HEADER_SIZE:cls.HEADER_SIZE+length]
        msg = cls(msg_type, channel_id, payload)
        return msg

# ---- StratumV2Server  (kind C, v10.18 lines 21246-21351) ----
class StratumV2Server:
    """
    Stratum v2 mining pool server.
    Binary protocol, more efficient than v1.
    Supports: setup, channel open, job distribution, share submission.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 host: str = "0.0.0.0",
                 port: int = DEFAULT_POOL_PORT + 1):
        self.blockchain = blockchain
        self.host       = host
        self.port       = port
        self._running   = False
        self._stats     = PoolStats()
        self._workers   : Dict[int, PoolWorker] = {}
        self._chan_counter = 0
        self._lock      = threading.RLock()

    def start(self):
        self._running = True
        threading.Thread(target=self._listen, daemon=True,
                         name="StratumV2-Listen").start()
        print(f"⛏️  Stratum v2 Pool on {self.host}:{self.port}")

    def stop(self):
        self._running = False

    def _listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))
        sock.listen(1024)
        while self._running:
            try:
                conn, addr = sock.accept()
                threading.Thread(
                    target=self._handle_connection,
                    args=(conn,), daemon=True).start()
            except Exception:
                break

    def _handle_connection(self, conn: socket.socket):
        with self._lock:
            self._chan_counter += 1
            chan_id = self._chan_counter
            worker  = PoolWorker(
                worker_id   = str(chan_id),
                worker_name = f"worker-{chan_id}",
                address     = "",
                extranonce1 = secrets.token_bytes(EXTRANONCE1_SIZE),
            )
            self._workers[chan_id] = worker
            self._stats.active_workers = len(self._workers)
        try:
            buf = b''
            while self._running:
                data = conn.recv(4096)
                if not data: break
                buf += data
                while len(buf) >= StratumV2Message.HEADER_SIZE:
                    msg = StratumV2Message.decode(buf)
                    if msg is None: break
                    consumed = StratumV2Message.HEADER_SIZE + len(msg.payload)
                    buf = buf[consumed:]
                    resp = self._dispatch(msg, worker)
                    if resp:
                        conn.sendall(resp.encode())
        except Exception:
            pass
        finally:
            conn.close()
            with self._lock:
                self._workers.pop(chan_id, None)
                self._stats.active_workers = len(self._workers)

    def _dispatch(self, msg: StratumV2Message,
                  worker: PoolWorker) -> Optional[StratumV2Message]:
        if msg.msg_type == StratumV2Message.SETUP_CONNECTION:
            return StratumV2Message(
                StratumV2Message.SETUP_CONNECTION_SUCCESS,
                payload=struct.pack('<H', 0))

        elif msg.msg_type == StratumV2Message.OPEN_STANDARD_MINING_CHANNEL:
            worker.authorized = True
            return StratumV2Message(
                StratumV2Message.OPEN_STANDARD_MINING_CHANNEL_SUCCESS,
                channel_id=int(worker.worker_id),
                payload=(struct.pack('<I', int(worker.worker_id)) +
                         worker.extranonce1 +
                         struct.pack('<I', EXTRANONCE2_SIZE) +
                         struct.pack('<Q', int(worker.difficulty))))

        elif msg.msg_type == StratumV2Message.SUBMIT_SHARES_STANDARD:
            with self._lock:
                self._stats.shares_submitted += 1
                self._stats.shares_accepted  += 1
                worker.shares_accepted += 1
            return StratumV2Message(
                StratumV2Message.SUBMIT_SHARES_SUCCESS,
                channel_id=int(worker.worker_id),
                payload=struct.pack('<II', worker.shares_accepted, 0))
        return None

    def get_stats(self) -> dict:
        return self._stats.to_dict()

# ---- MiningPoolManager  (kind C, v10.18 lines 21354-21445) ----
class MiningPoolManager:
    """
    High-level mining pool manager.
    Runs both Stratum v1 and v2 servers.
    Handles reward distribution (PPLNS / PPS / FPPS).
    """

    class PayoutScheme(Enum):
        PPLNS = "pay_per_last_n_shares"
        PPS   = "pay_per_share"
        FPPS  = "full_pay_per_share"
        SOLO  = "solo"

    def __init__(self, blockchain: 'NEBULABlockchain',
                 pool_address: str = FOUNDATION_ADDRESS,
                 scheme: 'MiningPoolManager.PayoutScheme' = None):
        self.blockchain   = blockchain
        self.pool_address = pool_address
        self.scheme       = scheme or self.PayoutScheme.PPLNS

        self.v1 = StratumV1Server(blockchain,
                                   pool_address=pool_address)
        self.v2 = StratumV2Server(blockchain)

        self._payout_queue  : List[dict] = []
        self._total_paid    : int = 0
        self._lock          = threading.RLock()

        # Wire up block-found callback
        self.v1.on_block_found = self._on_block_found

    def start(self):
        self.v1.start()
        self.v2.start()
        threading.Thread(target=self._payout_loop,
                         daemon=True, name="Pool-Payout").start()
        print(f"🏊 Mining Pool Manager started")
        print(f"   Payout scheme: {self.scheme.value}")
        print(f"   Pool address : {self.pool_address}")

    def stop(self):
        self.v1.stop()
        self.v2.stop()

    def _on_block_found(self, worker: PoolWorker, block_hash: str):
        """Called when a worker finds a valid block"""
        with self._lock:
            reward = mining_reward(self.blockchain.height + 1)
            self._distribute_reward(reward, block_hash)

    def _distribute_reward(self, reward_neb: int, block_hash: str):
        """Distribute block reward among workers by contribution"""
        workers = list(self.v1._workers.values())
        if not workers:
            return

        if self.scheme == self.PayoutScheme.PPLNS:
            total_shares = sum(w.shares_accepted for w in workers)
            if total_shares == 0: return
            for w in workers:
                share   = w.shares_accepted / total_shares
                payout  = int(reward_neb * share * (1 - self.v1.pool_fee_pct / 100))
                if payout > DUST_THRESHOLD:
                    self._payout_queue.append({
                        "address": w.address or self.pool_address,
                        "amount" : payout,
                        "block"  : block_hash,
                        "worker" : w.worker_name,
                    })
        elif self.scheme == self.PayoutScheme.SOLO:
            # All reward to the worker who found the block
            pass

    def _payout_loop(self):
        """Process pending payouts"""
        while True:
            time.sleep(30)
            with self._lock:
                if self._payout_queue:
                    print(f"💰 Processing {len(self._payout_queue)} payouts...")
                    self._payout_queue.clear()

    def get_stats(self) -> dict:
        v1s = self.v1.get_stats()
        v2s = self.v2.get_stats()
        return {
            "v1"           : v1s,
            "v2"           : v2s,
            "pool_address" : self.pool_address,
            "payout_scheme": self.scheme.value,
            "total_workers": v1s["active_workers"] + v2s["active_workers"],
        }

# ---- EllSwift  (kind C, v10.18 lines 22133-22171) ----
class EllSwift:
    """
    ElligatorSwift key encoding (BIP324).
    Encodes secp256k1 public keys as 64-byte uniform random-looking strings.
    Makes encryption indistinguishable from random traffic.
    """

    @staticmethod
    def encode(pubkey_bytes: bytes) -> bytes:
        """
        Encode 33-byte compressed public key as 64-byte ElligatorSwift.
        Simplified: pad with deterministic nonce. Full impl uses sqrt.
        """
        assert len(pubkey_bytes) == 33
        x_bytes = pubkey_bytes[1:]   # 32-byte x-coord
        # ElligatorSwift: u || t where decode(u,t) = (x,y)
        # Simplified: u = x, t = hash(prefix || x)
        t = hashlib.sha256(b"ellswift_prefix" + x_bytes).digest()
        return x_bytes + t

    @staticmethod
    def decode(ellswift: bytes) -> bytes:
        """
        Decode 64-byte ElligatorSwift to 33-byte compressed pubkey.
        Simplified: recover x from first 32 bytes.
        """
        assert len(ellswift) == 64
        x_bytes = ellswift[:32]
        x       = int.from_bytes(x_bytes, 'big')
        P       = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
        y_sq    = (pow(x, 3, P) + 7) % P
        y       = pow(y_sq, (P+1)//4, P)
        if y * y % P != y_sq:
            # Try x+1 if invalid
            x = (x + 1) % P
            y_sq = (pow(x, 3, P) + 7) % P
            y    = pow(y_sq, (P+1)//4, P)
        prefix  = b'\x02' if y % 2 == 0 else b'\x03'
        return prefix + x_bytes

# ---- ChaCha20Poly1305  (kind C, v10.18 lines 22174-22269) ----
class ChaCha20Poly1305:
    """
    ChaCha20-Poly1305 AEAD cipher (RFC 8439).
    Used for all BIP324 encrypted packets.
    Authenticated encryption with associated data (AEAD).
    """

    @staticmethod
    def _chacha20_block(key: bytes, counter: int, nonce: bytes) -> bytes:
        """ChaCha20 block function (RFC 8439 §2.1)"""
        def rotl32(v, n): return ((v << n) | (v >> (32-n))) & 0xFFFFFFFF

        def quarter_round(a,b,c,d,s):
            s[a] = (s[a]+s[b]) & 0xFFFFFFFF; s[d] ^= s[a]; s[d] = rotl32(s[d],16)
            s[c] = (s[c]+s[d]) & 0xFFFFFFFF; s[b] ^= s[c]; s[b] = rotl32(s[b],12)
            s[a] = (s[a]+s[b]) & 0xFFFFFFFF; s[d] ^= s[a]; s[d] = rotl32(s[d], 8)
            s[c] = (s[c]+s[d]) & 0xFFFFFFFF; s[b] ^= s[c]; s[b] = rotl32(s[b], 7)

        c = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574]
        k = list(struct.unpack('<8I', key))
        n = list(struct.unpack('<3I', nonce))
        state = c + k + [counter] + n
        work  = list(state)

        for _ in range(10):
            quarter_round(0,4,8,12,work)
            quarter_round(1,5,9,13,work)
            quarter_round(2,6,10,14,work)
            quarter_round(3,7,11,15,work)
            quarter_round(0,5,10,15,work)
            quarter_round(1,6,11,12,work)
            quarter_round(2,7,8,13,work)
            quarter_round(3,4,9,14,work)

        return struct.pack('<16I',
                           *[(work[i]+state[i])&0xFFFFFFFF for i in range(16)])

    @classmethod
    def _keystream(cls, key: bytes, counter: int, nonce: bytes, length: int) -> bytes:
        stream = b''
        block_idx = 0
        while len(stream) < length:
            stream += cls._chacha20_block(key, counter + block_idx, nonce)
            block_idx += 1
        return stream[:length]

    @classmethod
    def _poly1305_mac(cls, key: bytes, msg: bytes) -> bytes:
        """Poly1305 MAC (simplified — uses HMAC-SHA256 as secure approximation)"""
        return _hmac.new(key, msg, hashlib.sha256).digest()[:16]

    @classmethod
    def encrypt(cls, key: bytes, nonce: bytes,
                plaintext: bytes, aad: bytes = b'') -> bytes:
        """
        Encrypt and authenticate. Returns ciphertext + 16-byte tag.
        """
        assert len(key) == 32 and len(nonce) == 12

        # Derive Poly1305 key from first keystream block
        otk    = cls._keystream(key, 0, nonce, 32)
        # Encrypt starting at counter=1
        stream = cls._keystream(key, 1, nonce, len(plaintext))
        ct     = bytes(a^b for a,b in zip(plaintext, stream))

        # Build mac data (RFC 8439 §2.8)
        def pad16(b): return b + b'\x00' * ((-len(b)) % 16)
        mac_data = (pad16(aad) + pad16(ct) +
                    struct.pack('<Q', len(aad)) +
                    struct.pack('<Q', len(ct)))
        tag = cls._poly1305_mac(otk, mac_data)
        return ct + tag

    @classmethod
    def decrypt(cls, key: bytes, nonce: bytes,
                ciphertext: bytes, aad: bytes = b'') -> Optional[bytes]:
        """
        Decrypt and verify. Returns plaintext or None if authentication fails.
        """
        if len(ciphertext) < POLY1305_TAG_SIZE:
            return None
        ct  = ciphertext[:-POLY1305_TAG_SIZE]
        tag = ciphertext[-POLY1305_TAG_SIZE:]

        otk = cls._keystream(key, 0, nonce, 32)
        def pad16(b): return b + b'\x00' * ((-len(b)) % 16)
        mac_data = (pad16(aad) + pad16(ct) +
                    struct.pack('<Q', len(aad)) +
                    struct.pack('<Q', len(ct)))
        expected_tag = cls._poly1305_mac(otk, mac_data)

        if not _hmac.compare_digest(tag, expected_tag):
            return None   # Authentication failed

        stream = cls._keystream(key, 1, nonce, len(ct))
        return bytes(a^b for a,b in zip(ct, stream))

# ---- BIP324Handshake  (kind C, v10.18 lines 22273-22350) ----
class BIP324Handshake:
    """
    BIP324 v2 P2P encrypted handshake.
    Flow:
      Initiator → Responder: ElligatorSwift(pubkey) + garbage(0-4095 bytes)
      Responder → Initiator: ElligatorSwift(pubkey) + garbage + garbage_terminator
      Both: derive session keys via ECDH
      Both: send version packet (version negotiation)
    """

    def __init__(self, privkey: int, initiator: bool):
        self.privkey   = privkey
        self.initiator = initiator
        self._state    = "initial"
        self._session  : Optional[BIP324Session] = None

        # Generate local ephemeral ElligatorSwift key
        pub_bytes      = Secp256k1.pubkey_to_bytes(
                            Secp256k1.point_mul(privkey, Secp256k1.G()))
        self._ellswift_local = EllSwift.encode(pub_bytes)
        self._garbage  = secrets.token_bytes(secrets.randbelow(GARBAGE_LEN_MAX + 1))

    def build_client_hello(self) -> bytes:
        """Build initiator → responder opening message"""
        return self._ellswift_local + self._garbage

    def build_server_hello(self) -> bytes:
        """Build responder → initiator opening message"""
        return self._ellswift_local + self._garbage

    def process_peer_hello(self, data: bytes) -> Tuple[bool, str]:
        """
        Process peer's opening message and derive session keys.
        Returns (success, reason).
        """
        if len(data) < ELLSWIFT_SIZE:
            return False, "Message too short"

        peer_ellswift = data[:ELLSWIFT_SIZE]
        # garbage and garbage terminator follow (variable length)

        try:
            peer_pub  = EllSwift.decode(peer_ellswift)
            peer_x    = int.from_bytes(peer_pub[1:33], 'big')
            P         = Secp256k1.P
            y_sq      = (pow(peer_x, 3, P) + 7) % P
            y         = pow(y_sq, (P+1)//4, P)
            if y * y % P != y_sq:
                return False, "Invalid peer public key"
            if peer_pub[0] == b'\x03'[0]: y = P - y
            peer_point = (peer_x, y)

            shared_point = Secp256k1.point_mul(self.privkey, peer_point)
            if shared_point is None:
                return False, "ECDH failed"

            shared_secret = hashlib.sha256(
                Secp256k1.pubkey_to_bytes(shared_point)).digest()

            self._session = BIP324Session(shared_secret, self.initiator)
            self._state   = "ready"
            return True, "Handshake complete"
        except Exception as e:
            return False, f"Handshake error: {e}"

    @property
    def session(self) -> Optional[BIP324Session]:
        return self._session

    @property
    def is_complete(self) -> bool:
        return self._state == "ready"

    @property
    def session_id(self) -> Optional[bytes]:
        if self._session:
            return self._session.session_id
        return None

# ---- EncryptedPeerConnection  (kind C, v10.18 lines 22353-22449) ----
class EncryptedPeerConnection:
    """
    BIP324 encrypted P2P peer connection.
    Wraps a TCP socket with transparent BIP324 encryption.
    Negotiates v2 protocol on connect; falls back to v1 if peer doesn't support.
    """

    def __init__(self, host: str, port: int,
                 node: 'P2PNode', sock=None, inbound: bool = False):
        self.host      = host
        self.port      = port
        self.node      = node
        self._sock     = sock
        self.inbound   = inbound

        # Generate ephemeral session key
        self._privkey  = secrets.randbelow(Secp256k1.N - 1) + 1
        self._handshake= BIP324Handshake(self._privkey, initiator=not inbound)
        self._session  : Optional[BIP324Session] = None
        self._v2       = False    # True once BIP324 negotiated
        self._lock     = threading.Lock()
        self._buf      = b''
        self._running  = False
        self._send_nonce = 0
        self._recv_nonce = 0

    def connect(self) -> bool:
        import socket as _socket
        try:
            self._sock = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
            self._sock.settimeout(10)
            self._sock.connect((self.host, self.port))
            self._sock.settimeout(None)
            return self._do_handshake()
        except Exception:
            return False

    def _do_handshake(self) -> bool:
        """Perform BIP324 handshake or fall back to v1"""
        try:
            hello = self._handshake.build_client_hello()
            self._sock.sendall(hello)
            resp = self._sock.recv(ELLSWIFT_SIZE + GARBAGE_LEN_MAX + 100)
            ok, reason = self._handshake.process_peer_hello(resp)
            if ok:
                self._session = self._handshake.session
                self._v2      = True
                return True
            return False
        except Exception:
            return False   # Fall back to v1

    def send_message(self, msg: 'Message') -> bool:
        """Send an encrypted message"""
        try:
            raw = msg.encode()
            if self._v2 and self._session:
                encrypted = self._session.encrypt_packet(raw)
                with self._lock:
                    self._sock.sendall(encrypted)
            else:
                with self._lock:
                    self._sock.sendall(raw)
            return True
        except Exception:
            return False

    def send_decoy(self, size: int = 32) -> bool:
        """Send a decoy packet to frustrate traffic analysis"""
        if not (self._v2 and self._session):
            return False
        try:
            payload   = secrets.token_bytes(size)
            encrypted = self._session.encrypt_packet(payload, decoy=True)
            with self._lock:
                self._sock.sendall(encrypted)
            return True
        except Exception:
            return False

    def is_encrypted(self) -> bool:
        return self._v2 and self._session is not None

    def session_id_hex(self) -> Optional[str]:
        if self._session:
            return self._session.session_id.hex()
        return None

    def to_dict(self) -> dict:
        return {
            "host"       : self.host,
            "port"       : self.port,
            "encrypted"  : self.is_encrypted(),
            "protocol"   : "BIP324 v2" if self._v2 else "v1 plaintext",
            "session_id" : (self.session_id_hex() or "")[:16] + "..." if self._session else None,
            "inbound"    : self.inbound,
        }

# ---- PrivacyDNSSeeder  (kind C, v10.18 lines 23863-23922) ----
class PrivacyDNSSeeder:
    """
    DNS seed resolver with Tor support.
    When Tor is available, resolves DNS seeds through Tor to prevent
    ISP from learning which blockchain network you're joining.
    """

    # NEBULA onion seed nodes
    ONION_SEEDS = [
        PeerAddress("nebulanbl3seed1aaabbbccc", DEFAULT_PORT, NetworkType.ONION, source="onion_seed"),
        PeerAddress("nebulanbl3seed2dddeeefff", DEFAULT_PORT, NetworkType.ONION, source="onion_seed"),
        PeerAddress("nebulanbl3seed3ggghhh111", DEFAULT_PORT, NetworkType.ONION, source="onion_seed"),
    ]

    # NEBULA I2P seed nodes
    I2P_SEEDS = [
        PeerAddress("nebulanbl1aaabbbcccdddeee", DEFAULT_PORT, NetworkType.I2P, source="i2p_seed"),
        PeerAddress("nebulanbl2fffggghhh111222", DEFAULT_PORT, NetworkType.I2P, source="i2p_seed"),
    ]

    def __init__(self, privacy_mgr: PrivacyConnectionManager):
        self.privacy = privacy_mgr

    def get_seeds(self) -> List[PeerAddress]:
        """Resolve DNS seeds + return onion/I2P seeds"""
        result = []

        # Add static onion seeds if Tor available
        if self.privacy._tor_available:
            result.extend(self.ONION_SEEDS)

        # Add static I2P seeds if I2P available
        if self.privacy._i2p_available:
            result.extend(self.I2P_SEEDS)

        # Resolve clearnet DNS seeds (through Tor if available)
        for hostname in DNS_SEEDS:
            try:
                if self.privacy._tor_available:
                    # Use Tor for DNS resolution
                    sock = self.privacy.tor.connect(hostname, DEFAULT_PORT)
                    if sock:
                        sock.close()
                        result.append(PeerAddress(
                            hostname, DEFAULT_PORT, NetworkType.IPV4,
                            source=f"dns:{hostname}"))
                else:
                    import socket as _sock
                    infos = _sock.getaddrinfo(hostname, DEFAULT_PORT,
                                              _sock.AF_UNSPEC, _sock.SOCK_STREAM)
                    for info in infos:
                        ip   = info[4][0]
                        port = info[4][1]
                        net  = (NetworkType.IPV6 if ':' in ip else NetworkType.IPV4)
                        result.append(PeerAddress(ip, port, net,
                                                   source=f"dns:{hostname}"))
            except Exception:
                continue

        return result

# ---- TrafficAnalysisResistance  (kind C, v10.18 lines 23925-23975) ----
class TrafficAnalysisResistance:
    """
    Techniques to resist traffic analysis and deanonymization.
    - Random delay injection between messages
    - Decoy traffic generation
    - Message batching
    - Connection timing randomization
    """

    def __init__(self, session: 'BIP324Session' = None):
        self.session     = session
        self._running    = False
        self._decoy_rate = 0.1   # decoy packets per second
        self._min_delay  = 0.05  # minimum inter-message delay (seconds)
        self._max_delay  = 0.5   # maximum inter-message delay (seconds)

    def random_delay(self):
        """Add random delay before sending to obscure timing patterns"""
        import random
        delay = random.uniform(self._min_delay, self._max_delay)
        time.sleep(delay)

    def should_send_decoy(self) -> bool:
        """Probabilistically decide whether to send a decoy packet"""
        import random
        return random.random() < self._decoy_rate

    def start_decoy_loop(self, send_func):
        """Start background decoy packet sender"""
        self._running = True
        def _loop():
            while self._running:
                time.sleep(1.0 / max(0.01, self._decoy_rate))
                try:
                    send_func(size=secrets.randbelow(256) + 32)
                except Exception:
                    pass
        threading.Thread(target=_loop, daemon=True,
                         name="Decoy-Sender").start()

    def stop(self):
        self._running = False

    def set_decoy_rate(self, rate: float):
        """Set decoy packet rate (packets per second)"""
        self._decoy_rate = max(0.0, min(100.0, rate))

    def set_delay_range(self, min_s: float, max_s: float):
        """Set inter-message delay range"""
        self._min_delay = max(0, min_s)
        self._max_delay = max(self._min_delay, max_s)

# ---- MuSig2Nonce  (kind C, v10.18 lines 24082-24121) ----
@dataclass
class MuSig2Nonce:
    """
    MuSig2 nonce pair (R1, R2) for one signer.
    MUST be generated fresh for every signing session.
    Reusing nonces leaks private key — same as ECDSA.
    """
    k1    : int    # secret nonce 1
    k2    : int    # secret nonce 2
    R1    : bytes  # public nonce 1 (33 bytes compressed)
    R2    : bytes  # public nonce 2 (33 bytes compressed)
    used  : bool = False

    @classmethod
    def generate(cls, privkey: int, msg: bytes = b'',
                 extra_rand: bytes = None) -> 'MuSig2Nonce':
        """
        Generate fresh nonce pair deterministically.
        BIP327: nonces derived from privkey + msg + random bytes.
        """
        rand  = extra_rand or secrets.token_bytes(32)
        seed1 = _musig2_hash("MuSig/nonce",
                              privkey.to_bytes(32,'big') + msg + rand + b'\x00')
        seed2 = _musig2_hash("MuSig/nonce",
                              privkey.to_bytes(32,'big') + msg + rand + b'\x01')
        k1 = int.from_bytes(seed1, 'big') % Schnorr.N
        k2 = int.from_bytes(seed2, 'big') % Schnorr.N
        if k1 == 0 or k2 == 0:
            raise ValueError("Zero nonce — retry")

        def _to_pub(k):
            P = Schnorr._point_mul(k, Schnorr._G())
            return Secp256k1.pubkey_to_bytes(P)

        return cls(k1=k1, k2=k2, R1=_to_pub(k1), R2=_to_pub(k2))

    @property
    def public_nonce(self) -> bytes:
        """66-byte public nonce = R1 || R2"""
        return self.R1 + self.R2

# ---- MuSig2Session  (kind C, v10.18 lines 24124-24314) ----
class MuSig2Session:
    """
    MuSig2 interactive signing session (BIP327).
    Coordinates multi-party signing:
      Round 1: each signer generates and shares nonce
      Round 2: each signer computes partial signature
      Combine: partial sigs combined into final Schnorr sig
    """

    def __init__(self, signer_index: int,
                 all_pubkeys: List[bytes],
                 privkey: int,
                 msg32: bytes):
        if len(msg32) != 32:
            raise ValueError("Message must be 32 bytes")

        self.signer_index  = signer_index
        self.all_pubkeys   = sorted(all_pubkeys)
        self.privkey       = privkey
        self.msg32         = msg32
        self.n_signers     = len(all_pubkeys)

        # Aggregate public key
        self.agg_pubkey, self.coeffs = MuSig2KeyAgg.aggregate(all_pubkeys)
        self.agg_coeff = self.coeffs[
            self.all_pubkeys.index(
                Secp256k1.pubkey_to_bytes(
                    Secp256k1.point_mul(privkey, Secp256k1.G())))]

        # Our nonce
        self.nonce          = MuSig2Nonce.generate(privkey, msg32)
        self._peer_nonces   : Dict[int, bytes] = {}
        self._partial_sigs  : Dict[int, int]   = {}
        self._state         = "round1"
        self._lock          = threading.Lock()

    # ── Round 1: Nonce exchange ───────────────────────────────────
    def get_public_nonce(self) -> bytes:
        """Return our 66-byte public nonce to share with peers"""
        return self.nonce.public_nonce

    def receive_nonce(self, signer_idx: int, pub_nonce: bytes):
        """Receive peer's public nonce"""
        if len(pub_nonce) != 66:
            raise ValueError(f"Invalid nonce size: {len(pub_nonce)}")
        with self._lock:
            self._peer_nonces[signer_idx] = pub_nonce

    def nonces_complete(self) -> bool:
        """True when we have nonces from all signers"""
        return len(self._peer_nonces) == self.n_signers - 1

    # ── Round 2: Partial signature ────────────────────────────────
    def compute_partial_sig(self) -> int:
        """
        Compute our partial signature.
        Must only be called after all nonces received.
        Returns partial signature as integer.
        """
        if not self.nonces_complete():
            raise RuntimeError("Not all nonces received")
        if self.nonce.used:
            raise RuntimeError("Nonce already used — create new session")

        with self._lock:
            self.nonce.used = True

            # Collect all nonces in order
            all_nonces = {}
            all_nonces[self.signer_index] = self.nonce.public_nonce
            all_nonces.update(self._peer_nonces)

            # Compute combined nonce R = R1 + b*R2
            b_data = b''.join(all_nonces[i] for i in sorted(all_nonces))
            b_hash = _musig2_hash("MuSig/nonceblinding",
                                   b_data + self.agg_pubkey + self.msg32)
            b = int.from_bytes(b_hash, 'big') % Schnorr.N

            # Compute R = sum(R1_i + b*R2_i)
            R = None
            for idx in sorted(all_nonces):
                nonce_bytes = all_nonces[idx]
                R1i = nonce_bytes[:33]
                R2i = nonce_bytes[33:]

                def _decode_pub(pb):
                    x = int.from_bytes(pb[1:], 'big')
                    P = Schnorr.P
                    ys = (pow(x,3,P)+7)%P
                    y  = pow(ys,(P+1)//4,P)
                    if (y%2==0) != (pb[0]==0x02): y=P-y
                    return (x,y)

                p1 = _decode_pub(R1i)
                p2 = _decode_pub(R2i)
                bR2 = Schnorr._point_mul(b, p2)
                Ri  = Schnorr._point_add(p1, bR2)
                R   = Schnorr._point_add(R, Ri)

            if R is None:
                raise ValueError("Combined nonce is point at infinity")

            # Negate if R.y is odd (BIP340)
            if R[1] % 2 != 0:
                k1_eff = Schnorr.N - self.nonce.k1
                k2_eff = Schnorr.N - self.nonce.k2
            else:
                k1_eff = self.nonce.k1
                k2_eff = self.nonce.k2

            # Effective private key (negate if agg key y is odd)
            agg_x = int.from_bytes(self.agg_pubkey, 'big')
            agg_P = Schnorr._lift_x(agg_x)
            if agg_P and agg_P[1] % 2 != 0:
                privkey_eff = Schnorr.N - self.privkey
            else:
                privkey_eff = self.privkey

            # Challenge e = H(R.x || agg_pubkey || msg)
            e_data = (R[0].to_bytes(32,'big') + self.agg_pubkey + self.msg32)
            e = int.from_bytes(_musig2_hash("BIP0340/challenge", e_data), 'big') % Schnorr.N

            # Partial sig: s_i = k1_i + b*k2_i + e * a_i * privkey_i
            s_i = (k1_eff + b * k2_eff + e * self.agg_coeff * privkey_eff) % Schnorr.N
            self._partial_sigs[self.signer_index] = s_i
            return s_i

    def receive_partial_sig(self, signer_idx: int, partial_sig: int):
        """Receive partial signature from peer"""
        with self._lock:
            self._partial_sigs[signer_idx] = partial_sig

    def sigs_complete(self) -> bool:
        return len(self._partial_sigs) == self.n_signers

    def aggregate_signatures(self) -> bytes:
        """
        Combine all partial signatures into final 64-byte Schnorr signature.
        Only call after all partial sigs received.
        """
        if not self.sigs_complete():
            raise RuntimeError("Not all partial signatures received")

        # Sum partial sigs
        s = sum(self._partial_sigs.values()) % Schnorr.N

        # Get R.x for the signature
        all_nonces = {self.signer_index: self.nonce.public_nonce}
        all_nonces.update(self._peer_nonces)

        b_data = b''.join(all_nonces[i] for i in sorted(all_nonces))
        b_hash = _musig2_hash("MuSig/nonceblinding",
                               b_data + self.agg_pubkey + self.msg32)
        b = int.from_bytes(b_hash, 'big') % Schnorr.N

        R = None
        for idx in sorted(all_nonces):
            nb  = all_nonces[idx]
            def _dec(pb):
                x = int.from_bytes(pb[1:],'big')
                P_ = Schnorr.P
                ys = (pow(x,3,P_)+7)%P_
                y  = pow(ys,(P_+1)//4,P_)
                if (y%2==0)!=(pb[0]==0x02): y=P_-y
                return (x,y)
            p1  = _dec(nb[:33])
            p2  = _dec(nb[33:])
            bR2 = Schnorr._point_mul(b, p2)
            Ri  = Schnorr._point_add(p1, bR2)
            R   = Schnorr._point_add(R, Ri)

        if R is None:
            raise ValueError("Final nonce is infinity")

        R_x = R[0].to_bytes(32, 'big')
        sig  = R_x + s.to_bytes(32, 'big')
        return sig

    def verify_final(self, sig: bytes) -> bool:
        """Verify the final aggregated Schnorr signature"""
        return Schnorr.verify(self.agg_pubkey, self.msg32, sig)

    def to_dict(self) -> dict:
        return {
            "signer_index"      : self.signer_index,
            "n_signers"         : self.n_signers,
            "agg_pubkey"        : self.agg_pubkey.hex(),
            "nonces_received"   : len(self._peer_nonces),
            "partial_sigs"      : len(self._partial_sigs),
            "state"             : self._state,
        }

# ---- MuSig2Coordinator  (kind C, v10.18 lines 24317-24379) ----
class MuSig2Coordinator:
    """
    Coordinates MuSig2 signing across multiple parties.
    Can run locally (all keys on same device) or distributed.
    Useful for: NEBULA Lightning funding, threshold wallets, DAOs.
    """

    def __init__(self, privkeys: List[int], msg32: bytes):
        """
        Local MuSig2: all private keys on same machine.
        For distributed, create sessions on separate devices and
        exchange nonces + partial sigs manually.
        """
        if len(msg32) != 32:
            raise ValueError("msg32 must be 32 bytes")
        self.msg32    = msg32
        self.privkeys = privkeys
        self.pubkeys  = [
            Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(sk, Secp256k1.G()))
            for sk in privkeys
        ]
        self.n        = len(privkeys)
        self.sessions : List[MuSig2Session] = []

    def sign(self) -> Tuple[bytes, bytes]:
        """
        Run full local MuSig2 signing protocol.
        Returns (aggregated_xonly_pubkey, final_schnorr_signature).
        """
        # Create sessions
        self.sessions = [
            MuSig2Session(i, self.pubkeys, sk, self.msg32)
            for i, sk in enumerate(self.privkeys)
        ]

        # Round 1: exchange nonces
        nonces = [s.get_public_nonce() for s in self.sessions]
        for i, sess in enumerate(self.sessions):
            for j, nonce in enumerate(nonces):
                if j != i:
                    sess.receive_nonce(j, nonce)

        # Round 2: compute and exchange partial sigs
        partial_sigs = [s.compute_partial_sig() for s in self.sessions]
        for i, sess in enumerate(self.sessions):
            for j, psig in enumerate(partial_sigs):
                if j != i:
                    sess.receive_partial_sig(j, psig)

        # Aggregate signatures
        final_sig = self.sessions[0].aggregate_signatures()
        agg_pubkey, _ = MuSig2KeyAgg.aggregate(self.pubkeys)

        # Verify
        if not Schnorr.verify(agg_pubkey, self.msg32, final_sig):
            raise RuntimeError("Final signature verification failed")

        return agg_pubkey, final_sig

    def aggregated_address(self, hrp: str = "nbl") -> str:
        """Get the P2TR address for the aggregated key"""
        agg_pubkey, _ = MuSig2KeyAgg.aggregate(self.pubkeys)
        return SegWitScript.p2tr_address(agg_pubkey, hrp)

# ---- ThresholdSig  (kind C, v10.18 lines 24382-24428) ----
class ThresholdSig:
    """
    t-of-n threshold signature using MuSig2 + Tapscript fallback.
    For N-of-N: use pure MuSig2 (most efficient, single key on-chain).
    For t-of-N: use MuSig2 for online signers + Tapscript for recovery.
    """

    def __init__(self, threshold: int, pubkeys: List[bytes]):
        if threshold > len(pubkeys):
            raise ValueError(f"threshold {threshold} > n_keys {len(pubkeys)}")
        self.threshold = threshold
        self.pubkeys   = sorted(pubkeys)
        self.n         = len(pubkeys)

    @property
    def is_n_of_n(self) -> bool:
        return self.threshold == self.n

    def aggregated_key(self) -> bytes:
        """Aggregate all N public keys"""
        key, _ = MuSig2KeyAgg.aggregate(self.pubkeys)
        return key

    def build_tapscript_fallback(self) -> List[bytes]:
        """
        Build Tapscript leaves for t-of-n spending.
        Each subset of t keys gets a Tapscript leaf.
        For small n, enumerate all combinations.
        """
        from itertools import combinations
        scripts = []
        for combo in combinations(self.pubkeys, self.threshold):
            # CHECKMULTISIG-like using CHECKSIGADD (BIP342)
            script = b''
            for pk in combo:
                xonly = pk[1:] if len(pk) == 33 else pk
                script += bytes([0x20]) + xonly + bytes([0xac])  # CHECKSIG
            scripts.append(script)
        return scripts

    def to_dict(self) -> dict:
        return {
            "threshold"    : self.threshold,
            "n_keys"       : self.n,
            "type"         : "N-of-N MuSig2" if self.is_n_of_n else f"{self.threshold}-of-{self.n}",
            "agg_pubkey"   : self.aggregated_key().hex(),
        }

# ---- MerkleBlockProof  (kind C, v10.18 lines 25134-25219) ----
class MerkleBlockProof:
    """
    BIP37 merkleblock message.
    Proves a set of transactions are in a block using a partial Merkle tree.
    SPV clients use this to verify transactions without downloading full blocks.
    """

    def __init__(self, block: 'Block', tx_filter: BloomFilter = None):
        self.header      = block.header
        self.total_txs   = len(block.transactions)
        self.matched_txids : List[str] = []
        self.hashes      : List[bytes] = []
        self.flags_bits  : bytearray  = bytearray()

        if tx_filter:
            self._build(block, tx_filter)

    def _build(self, block: 'Block', bloom: BloomFilter):
        """Build partial Merkle tree for matched transactions"""
        n        = len(block.transactions)
        matched  = [bloom.matches_tx(tx) for tx in block.transactions]

        self.matched_txids = [
            tx.txid for tx, m in zip(block.transactions, matched) if m]

        txids = [bytes.fromhex(tx.txid)[::-1] for tx in block.transactions]
        self.hashes, flags = self._traverse(txids, matched, 0, n)
        # Pack flags into bytes
        self.flags_bits = bytearray(
            (len(flags) + 7) // 8)
        for i, f in enumerate(flags):
            if f:
                self.flags_bits[i >> 3] |= 1 << (i & 7)

    def _traverse(self, txids: List[bytes], matched: List[bool],
                   start: int, end: int) -> Tuple[List[bytes], List[bool]]:
        """Traverse Merkle tree, collecting hashes and flag bits"""
        def dsha(b): return hashlib.sha256(hashlib.sha256(b).digest()).digest()

        hashes = []
        flags  = []

        def _build(start, end):
            width = end - start
            if width == 1:
                flags.append(matched[start])
                if matched[start]:
                    flags.append(True)
                    hashes.append(txids[start])
                else:
                    hashes.append(txids[start])
                return txids[start]

            # Check if any in range matched
            any_matched = any(matched[start:end])
            flags.append(any_matched)
            if not any_matched:
                # Hash the subtree
                h = dsha(txids[start])   # simplified
                hashes.append(h)
                return h

            mid  = (start + end) // 2
            left  = _build(start, mid)
            right = _build(mid, end) if mid < end else left
            return dsha(left + right)

        _build(start, end)
        return hashes, flags

    def verify(self) -> Tuple[bool, str]:
        """Verify this merkle proof against the block header"""
        if not self.matched_txids:
            return True, "No matched transactions"
        computed_root = self.header.merkle_root
        return True, f"Proof valid for {len(self.matched_txids)} txs"

    def to_dict(self) -> dict:
        return {
            "block_hash"    : self.header.hash(),
            "block_height"  : self.header.height,
            "total_txs"     : self.total_txs,
            "matched_txs"   : len(self.matched_txids),
            "matched_txids" : self.matched_txids,
            "proof_hashes"  : len(self.hashes),
        }

# ---- SPVClient  (kind C, v10.18 lines 25222-25333) ----
class SPVClient:
    """
    Full SPV (Simplified Payment Verification) client.
    Downloads and verifies block headers only.
    Uses bloom filters to receive relevant transactions from peers.
    Verifies payments using merkle proofs.
    """

    def __init__(self, addresses: List[str] = None,
                 txids: List[str] = None):
        self.addresses    = addresses or []
        self.txids        = txids or []
        self._headers     : List['BlockHeader'] = []
        self._bloom       : Optional[BloomFilter] = None
        self._verified_txs: Dict[str, dict] = {}
        self._lock        = threading.RLock()

        # Initialize bloom filter
        n = max(10, len(self.addresses) + len(self.txids)) * 2
        self._bloom = BloomFilterLegacy(n, fp_rate=0.0001,
                                   tweak=secrets.randbelow(0xFFFFFFFF))
        for addr in self.addresses:
            self._bloom.insert_address(addr)
        for txid in self.txids:
            self._bloom.insert_txid(txid)

    def add_address(self, address: str):
        """Watch an additional address"""
        with self._lock:
            self.addresses.append(address)
            self._bloom.insert_address(address)

    def process_headers(self, headers: List['BlockHeader']) -> int:
        """
        Process and validate a batch of block headers.
        Returns number of valid headers added.
        """
        added = 0
        with self._lock:
            for hdr in headers:
                if not self._validate_header(hdr):
                    break
                self._headers.append(hdr)
                added += 1
        return added

    def _validate_header(self, hdr: 'BlockHeader') -> bool:
        """Validate PoW and chain linkage"""
        # Check PoW
        if not hdr.meets_target():
            return False
        # Check prev_hash linkage
        if self._headers:
            if hdr.prev_hash != self._headers[-1].hash():
                return False
        return True

    def process_merkle_block(self, proof: MerkleBlockProof) -> List[str]:
        """
        Process a merkleblock message.
        Returns list of verified transaction IDs.
        """
        ok, reason = proof.verify()
        if not ok:
            return []

        with self._lock:
            for txid in proof.matched_txids:
                self._verified_txs[txid] = {
                    "block_hash"   : proof.header.hash(),
                    "block_height" : proof.header.height,
                    "confirmed"    : True,
                    "verified_at"  : time.time(),
                }
        return proof.matched_txids

    def verify_payment(self, txid: str, address: str,
                       amount_neb: int) -> Tuple[bool, str]:
        """
        Verify a payment to address for amount.
        Returns (verified, reason).
        """
        with self._lock:
            if txid not in self._verified_txs:
                return False, "Transaction not verified"
            tx_info = self._verified_txs[txid]
            return True, (f"Payment verified in block #{tx_info['block_height']}")

    @property
    def chain_height(self) -> int:
        return len(self._headers) - 1

    @property
    def bloom_filter(self) -> Optional[BloomFilter]:
        return self._bloom

    def get_filter_payload(self) -> Optional[bytes]:
        """Get serialized bloom filter for sending to full node"""
        if self._bloom:
            return self._bloom.serialize()
        return None

    def stats(self) -> dict:
        with self._lock:
            return {
                "chain_height"  : self.chain_height,
                "headers"       : len(self._headers),
                "watched_addrs" : len(self.addresses),
                "watched_txids" : len(self.txids),
                "verified_txs"  : len(self._verified_txs),
                "bloom"         : self._bloom.stats() if self._bloom else None,
            }

# ---- CompactFilterIndex  (kind C, v10.18 lines 25459-25494) ----
class CompactFilterIndex:
    """
    Index of compact block filters for fast light client queries.
    Allows SPV-like functionality without bloom filter privacy issues.
    """

    def __init__(self):
        self._filters : Dict[int, CompactBlockFilter] = {}
        self._lock    = threading.RLock()

    def add_block(self, block: 'Block'):
        with self._lock:
            f = CompactBlockFilter.build_basic(block)
            self._filters[block.height] = f

    def get_filter(self, height: int) -> Optional[CompactBlockFilter]:
        return self._filters.get(height)

    def find_blocks_matching(self, address: str,
                              start_height: int = 0,
                              end_height: int = None) -> List[int]:
        """Find block heights that might contain transactions for address"""
        matching = []
        with self._lock:
            max_h = end_height or max(self._filters.keys(), default=0)
            for h in range(start_height, max_h + 1):
                f = self._filters.get(h)
                if f and f.match(address):
                    matching.append(h)
        return matching

    def stats(self) -> dict:
        return {
            "indexed_blocks" : len(self._filters),
            "max_height"     : max(self._filters.keys(), default=-1),
        }

# ---- HDAccountAdv  (kind C, v10.18 lines 26792-26908) ----
@dataclass
class HDAccountAdv:
    """
    Single HD wallet account (BIP44 account level).
    Manages external (receive) and internal (change) address chains.
    Supports multiple script types via purpose field.
    """
    index       : int
    purpose     : int           # 44/49/84/86
    master_key  : 'HDKey'
    label       : str = ""
    gap_limit   : int = 20
    created_at  : float = field(default_factory=time.time)
    last_used   : float = field(default_factory=time.time)

    # Address derivation state
    _external_index : int = field(default=0, init=False)
    _internal_index : int = field(default=0, init=False)
    _used_external  : set = field(default_factory=set, init=False)
    _used_internal  : set = field(default_factory=set, init=False)
    _lock           : threading.RLock = field(default_factory=threading.RLock, init=False)

    @property
    def coin_type(self) -> int:
        return CHAIN_ID   # 2025 for NEBULA

    @property
    def base_path(self) -> str:
        return f"m/{self.purpose}'/{self.coin_type}'/{self.index}'"

    def _derive_address(self, change: int, idx: int) -> str:
        """Derive address at path: base/change/idx"""
        path = f"{self.base_path}/{change}/{idx}"
        key  = self.master_key.derive_path(path)
        if self.purpose == PURPOSE_TAPROOT:
            xonly, script = SegWitScript.p2tr_from_privkey(key.key)
            return SegWitScript.p2tr_address(xonly)
        elif self.purpose == PURPOSE_NATIVE:
            pub = Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(key.key, Secp256k1.G()))
            return SegWitScript.p2wpkh_address(pub)
        else:
            return key.address

    def get_receive_address(self) -> str:
        """Get next unused external (receive) address"""
        with self._lock:
            addr = self._derive_address(0, self._external_index)
            self._external_index += 1
            self.last_used = time.time()
            return addr

    def get_change_address(self) -> str:
        """Get next unused internal (change) address"""
        with self._lock:
            addr = self._derive_address(1, self._internal_index)
            self._internal_index += 1
            return addr

    def mark_used(self, address: str, is_change: bool = False):
        """Mark address as used"""
        with self._lock:
            if is_change:
                self._used_internal.add(address)
            else:
                self._used_external.add(address)
            self.last_used = time.time()

    def get_all_addresses(self, look_ahead: int = None) -> List[str]:
        """Get all derived addresses (including gap limit look-ahead)"""
        ahead = look_ahead or self.gap_limit
        with self._lock:
            addrs = []
            for i in range(self._external_index + ahead):
                addrs.append(self._derive_address(0, i))
            return addrs

    def scan_for_used(self, utxo_set: 'UTXOSet') -> int:
        """Scan UTXO set to find which addresses have been used"""
        found = 0
        for i in range(self._external_index + self.gap_limit):
            addr = self._derive_address(0, i)
            if utxo_set.balance(addr) > 0:
                self.mark_used(addr)
                self._external_index = max(self._external_index, i + 1)
                found += 1
        return found

    def xpub(self) -> str:
        """Return xpub for this account"""
        key = self.master_key.derive_path(self.base_path)
        pub = Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(key.key, Secp256k1.G()))
        return pub.hex()

    def descriptor(self) -> OutputDescriptor:
        """Get output descriptor for this account"""
        xpub = self.xpub()
        if self.purpose == PURPOSE_TAPROOT:
            return OutputDescriptor.for_taproot(xpub, "00000000", self.index)
        elif self.purpose == PURPOSE_NATIVE:
            return OutputDescriptor.for_wpkh(xpub, "00000000", self.index)
        else:
            return OutputDescriptor.for_pkh(xpub, "00000000",
                                             f"{self.purpose}'/0'", self.index)

    def to_dict(self) -> dict:
        with self._lock:
            return {
                "index"           : self.index,
                "purpose"         : self.purpose,
                "label"           : self.label,
                "base_path"       : self.base_path,
                "external_index"  : self._external_index,
                "internal_index"  : self._internal_index,
                "used_addresses"  : len(self._used_external) + len(self._used_internal),
                "descriptor"      : self.descriptor().full(),
                "created_at"      : self.created_at,
            }

# ---- HardwareWalletInterface  (kind C, v10.18 lines 27283-27335) ----
class HardwareWalletInterface:
    """
    Hardware wallet integration interface.
    Compatible with Ledger, Trezor, Coldcard via PSBT flow.
    Actual device communication via HID/USB/NFC (device-specific).
    """

    class DeviceType(Enum):
        LEDGER   = "ledger"
        TREZOR   = "trezor"
        COLDCARD = "coldcard"
        BITBOX   = "bitbox"
        UNKNOWN  = "unknown"

    def __init__(self, device_type: 'HardwareWalletInterface.DeviceType' = None):
        self.device_type = device_type or self.DeviceType.UNKNOWN
        self._connected  = False
        self._xpub       : Optional[str] = None

    def connect(self) -> bool:
        """Connect to hardware wallet (device-specific)"""
        # In production: use hidapi/libusb for actual device communication
        self._connected = False
        return False

    def get_xpub(self, path: str) -> Optional[str]:
        """Get xpub from hardware wallet for given derivation path"""
        if not self._connected:
            return None
        return None   # would call device API

    def sign_psbt(self, psbt: PSBT) -> Optional[PSBT]:
        """Send PSBT to hardware wallet for signing"""
        if not self._connected:
            return None
        return None   # would send to device

    def display_address(self, address: str) -> bool:
        """Display address on hardware wallet screen for verification"""
        if not self._connected:
            return False
        return False

    @property
    def is_connected(self) -> bool:
        return self._connected

    def get_device_info(self) -> dict:
        return {
            "device_type" : self.device_type.value,
            "connected"   : self._connected,
            "xpub"        : self._xpub,
        }

# ---- CoinControl  (kind C, v10.18 lines 27338-27392) ----
class CoinControl:
    """
    Manual UTXO selection (coin control).
    Allows user to choose exactly which UTXOs to spend.
    Important for privacy and fee optimization.
    """

    def __init__(self):
        self._selected   : List['UTXOEntry'] = []
        self._change_addr: Optional[str]     = None
        self._fee_rate   : Optional[int]     = None
        self._subtract_fee_from_amount = False
        self._rbf        = True   # opt into RBF by default

    def select(self, utxo: 'UTXOEntry'):
        """Manually select a UTXO"""
        if utxo not in self._selected:
            self._selected.append(utxo)

    def deselect(self, txid: str, vout: int):
        """Deselect a UTXO"""
        self._selected = [u for u in self._selected
                          if not (u.txid == txid and u.index == vout)]

    def clear(self):
        """Clear all selections"""
        self._selected.clear()

    def set_change_address(self, address: str):
        self._change_addr = address

    def set_fee_rate(self, sat_per_vbyte: int):
        self._fee_rate = sat_per_vbyte

    @property
    def selected_utxos(self) -> List['UTXOEntry']:
        return list(self._selected)

    @property
    def selected_value(self) -> int:
        return sum(u.value for u in self._selected)

    def effective_fee(self, n_outputs: int = 2) -> int:
        rate = self._fee_rate or (MIN_TX_FEE // 100)
        size = 10 + 148 * len(self._selected) + 34 * n_outputs
        return rate * size

    def to_dict(self) -> dict:
        return {
            "selected_utxos"  : len(self._selected),
            "selected_value"  : self.selected_value,
            "change_address"  : self._change_addr,
            "fee_rate"        : self._fee_rate,
            "rbf"             : self._rbf,
        }

# ---- DLCOracle  (kind C, v10.18 lines 29054-29099) ----
class DLCOracle:
    """
    Discreet Log Contract oracle.
    An oracle commits to future event outcomes using Schnorr signatures.
    DLC parties pre-compute adaptor signatures for all outcomes.
    When oracle reveals outcome, one party can claim the funds.
    """

    def __init__(self, oracle_privkey: int):
        self.privkey    = oracle_privkey
        self.pubkey     = Schnorr.xonly_pubkey(oracle_privkey)
        self._nonces    : Dict[str, Tuple[int, bytes]] = {}   # event_id -> (k, R)

    def announce_event(self, event_id: str) -> bytes:
        """
        Announce an event and commit to a nonce.
        Returns the public nonce R (32 bytes) for this event.
        """
        k = secrets.randbelow(Schnorr.N - 1) + 1
        R = Schnorr._point_mul(k, Schnorr._G())
        R_bytes = R[0].to_bytes(32, 'big')
        self._nonces[event_id] = (k, R_bytes)
        return R_bytes

    def attest(self, event_id: str, outcome: str) -> bytes:
        """
        Attest to an outcome.
        Returns oracle signature for this (event, outcome) pair.
        """
        if event_id not in self._nonces:
            raise ValueError(f"Event {event_id} not announced")

        k, R_bytes = self._nonces[event_id]
        msg    = hashlib.sha256(outcome.encode()).digest()
        sig    = Schnorr.sign(self.privkey, msg)
        return sig

    def get_announcement(self, event_id: str) -> Optional[dict]:
        if event_id not in self._nonces:
            return None
        _, R_bytes = self._nonces[event_id]
        return {
            "event_id"    : event_id,
            "oracle_pubkey": self.pubkey.hex(),
            "nonce_R"     : R_bytes.hex(),
        }

# ---- BIP47PaymentCode  (kind C, v10.18 lines 29725-29818) ----
class BIP47PaymentCode:
    """
    BIP47 Reusable Payment Codes.
    Share one static payment code — receiver derives new address per sender.
    Solves address reuse without requiring per-payment interaction.
    Format: P || x || chain || 0x00 * 13 (80 bytes)
    Encoded as base58check with version byte 0x47.
    """

    VERSION = 0x47

    def __init__(self, privkey: int):
        self.privkey  = privkey
        self.pubkey   = Secp256k1.pubkey_to_bytes(
            Secp256k1.point_mul(privkey, Secp256k1.G()))
        # Generate notification address
        self._chain   = hashlib.sha256(self.pubkey).digest()[:32]

    def payment_code(self) -> bytes:
        """
        Serialize payment code (80 bytes).
        Format: 0x01 || 0x00 || pubkey(33) || chain(32) || 0x00*13
        """
        return (bytes([0x01, 0x00]) +
                self.pubkey +
                self._chain +
                bytes(13))

    def payment_code_b58(self) -> str:
        """Base58Check encoded payment code"""
        return base58check_encode(self.payment_code(), self.VERSION)

    def derive_address_for_sender(self, sender_pubkey: bytes,
                                   index: int = 0) -> str:
        """
        Derive a receive address for a specific sender.
        Receiver: knows their privkey + sender pubkey → derives same address as sender.
        """
        # ECDH shared secret
        sx    = int.from_bytes(sender_pubkey[1:33], 'big')
        P     = Secp256k1.P
        ys    = (pow(sx,3,P)+7) % P
        y     = pow(ys,(P+1)//4,P)
        if (y%2==0) != (sender_pubkey[0]==0x02): y = P-y
        point = Secp256k1.point_mul(self.privkey, (sx, y))
        secret= hashlib.sha256(Secp256k1.pubkey_to_bytes(point)).digest()

        # Derive child key
        child_privkey = (self.privkey + int.from_bytes(secret, 'big')) % Secp256k1.N
        child_pub     = Secp256k1.pubkey_to_bytes(
            Secp256k1.point_mul(child_privkey, Secp256k1.G()))
        return Script.p2pkh_address(child_pub)

    def derive_payment_address(self, recipient_payment_code: bytes,
                                 index: int = 0) -> str:
        """
        Derive payment address for a recipient given their payment code.
        Sender: knows their privkey + recipient payment code → derives address.
        """
        # Extract recipient's pubkey and chain from payment code
        if len(recipient_payment_code) < 35:
            raise ValueError("Invalid payment code")
        rec_pub = recipient_payment_code[2:35]

        # ECDH
        rx    = int.from_bytes(rec_pub[1:], 'big')
        P     = Secp256k1.P
        ys    = (pow(rx,3,P)+7) % P
        y     = pow(ys,(P+1)//4,P)
        if (y%2==0) != (rec_pub[0]==0x02): y = P-y
        point = Secp256k1.point_mul(self.privkey, (rx, y))
        secret = hashlib.sha256(Secp256k1.pubkey_to_bytes(point)).digest()

        # Tweak recipient's pubkey
        t      = int.from_bytes(secret, 'big') % Secp256k1.N
        tG     = Secp256k1.point_mul(t, Secp256k1.G())
        rec_pt = (rx, y)
        pay_pt = Secp256k1.point_add(rec_pt, tG)
        if pay_pt is None:
            raise ValueError("Key derivation failed")
        pay_pub = Secp256k1.pubkey_to_bytes(pay_pt)
        return Script.p2pkh_address(pay_pub)

    def notification_address(self) -> str:
        """BIP47 notification address (for announcing payment code to recipient)"""
        h160 = hash160(self.pubkey)
        return base58check_encode(h160, PUBKEY_ADDRESS_VERSION)

    def to_dict(self) -> dict:
        return {
            "payment_code"         : self.payment_code_b58(),
            "notification_address" : self.notification_address(),
            "version"              : "BIP47 v1",
        }

# ---- AddressGenerator  (kind C, v10.18 lines 29925-29960) ----
class AddressGenerator:
    """
    Generates fresh addresses with gap limit tracking.
    Prevents address reuse, supports all script types.
    """

    def __init__(self, wallet: MultiAccountWallet,
                 address_book: AddressBook):
        self.wallet  = wallet
        self.book    = address_book

    def fresh_receive_address(self, purpose: int = PURPOSE_LEGACY,
                               label: str = "") -> str:
        """Get a fresh receive address"""
        addr = self.wallet.get_address(purpose=purpose)
        if label:
            self.book.set_address_label(addr, label)
        return addr

    def fresh_taproot_address(self, label: str = "") -> str:
        """Get a fresh Taproot (P2TR) receive address"""
        return self.fresh_receive_address(PURPOSE_TAPROOT, label)

    def fresh_segwit_address(self, label: str = "") -> str:
        """Get a fresh native SegWit (P2WPKH) receive address"""
        return self.fresh_receive_address(PURPOSE_NATIVE, label)

    def batch_addresses(self, count: int = 10,
                         purpose: int = PURPOSE_LEGACY) -> List[str]:
        """Generate multiple fresh addresses"""
        return [self.wallet.get_address(purpose=purpose) for _ in range(count)]

    def verify_fresh(self, address: str) -> bool:
        """Verify an address has not been used before"""
        reused, _ = self.book.check_reuse(address)
        return not reused

# ---- DandelionPhase  (kind C, v10.18 lines 30868-30870) ----
class DandelionPhase(Enum):
    STEM  = "stem"    # relay to one peer (anonymous routing)
    FLUFF = "fluff"   # broadcast to all peers

# ---- DandelionRouter  (kind C, v10.18 lines 30872-30991) ----
class DandelionRouter:
    """
    Dandelion++ transaction routing (BIP156).
    Two-phase relay to improve transaction source privacy:
    Phase 1 (Stem): Route tx through random path of nodes.
    Phase 2 (Fluff): Broadcast normally once fluff phase starts.
    
    Prevents IP-to-transaction linkage attacks.
    """

    STEM_PROBABILITY   = 0.9    # probability of continuing stem phase
    STEM_TIMEOUT_SECS  = 30     # max time in stem before forced fluff
    STEM_MAX_HOPS      = 10     # max hops in stem phase

    def __init__(self, node_id: bytes):
        self.node_id      = node_id
        self._stem_peers  : Dict[bytes, bytes] = {}   # source -> relay peer
        self._stem_txs    : Dict[str, dict]    = {}   # txid -> stem info
        self._lock        = threading.RLock()
        self._fluff_queue : queue.Queue = queue.Queue()

        # Rotate stem peers every 10 minutes
        threading.Thread(target=self._rotation_loop,
                         daemon=True, name="Dandelion-Rotate").start()
        # Timeout stem transactions
        threading.Thread(target=self._timeout_loop,
                         daemon=True, name="Dandelion-Timeout").start()

    def route_transaction(self, txid: str,
                           source_peer: Optional[bytes] = None) -> Tuple[DandelionPhase, Optional[bytes]]:
        """
        Determine routing for a transaction.
        Returns (phase, relay_peer_id).
        relay_peer_id is None for fluff phase.
        """
        with self._lock:
            # Check if already tracking
            if txid in self._stem_txs:
                return DandelionPhase.STEM, self._stem_txs[txid].get("relay_to")

            # Decide phase
            import random
            if random.random() < self.STEM_PROBABILITY:
                # Stem phase: pick relay peer
                relay = self._get_stem_relay(source_peer)
                if relay:
                    self._stem_txs[txid] = {
                        "phase"    : DandelionPhase.STEM,
                        "relay_to" : relay,
                        "hops"     : 1,
                        "entered"  : time.time(),
                    }
                    return DandelionPhase.STEM, relay

            # Fluff phase: broadcast normally
            self._fluff_queue.put(txid)
            return DandelionPhase.FLUFF, None

    def _get_stem_relay(self, exclude: Optional[bytes]) -> Optional[bytes]:
        """Get a stem relay peer (excluding source)"""
        candidates = [p for p in self._stem_peers.values() if p != exclude]
        if candidates:
            return secrets.choice(candidates)
        return None

    def register_peer(self, peer_id: bytes):
        """Register a peer for potential stem relaying"""
        with self._lock:
            # Each peer gets a deterministic stem peer assignment
            h = int(hashlib.sha256(self.node_id + peer_id).hexdigest(), 16)
            self._stem_peers[peer_id] = peer_id   # simplified

    def unregister_peer(self, peer_id: bytes):
        with self._lock:
            self._stem_peers.pop(peer_id, None)

    def get_fluff_queue(self) -> List[str]:
        """Get all transactions ready for fluff broadcast"""
        txids = []
        while not self._fluff_queue.empty():
            try:
                txids.append(self._fluff_queue.get_nowait())
            except Exception:
                break
        return txids

    def _rotation_loop(self):
        """Rotate stem peer assignments every 10 minutes"""
        while True:
            time.sleep(600)
            with self._lock:
                # Re-assign random stem peers
                peers = list(self._stem_peers.keys())
                import random
                random.shuffle(peers)
                self._stem_peers = {p: peers[(i+1)%len(peers)]
                                    for i, p in enumerate(peers)}

    def _timeout_loop(self):
        """Force fluff any stem txs that have timed out"""
        while True:
            time.sleep(5)
            now = time.time()
            with self._lock:
                timed_out = [
                    txid for txid, info in self._stem_txs.items()
                    if (now - info["entered"] > self.STEM_TIMEOUT_SECS or
                        info["hops"] >= self.STEM_MAX_HOPS)
                ]
                for txid in timed_out:
                    self._fluff_queue.put(txid)
                    del self._stem_txs[txid]

    def stats(self) -> dict:
        with self._lock:
            return {
                "stem_txs"   : len(self._stem_txs),
                "stem_peers" : len(self._stem_peers),
                "fluff_queue": self._fluff_queue.qsize(),
            }

# ---- CompactBlockLegacy  (kind C, v10.18 lines 30994-31101) ----
class CompactBlockLegacy:
    """[v10.17] OLD implementation kept ONLY for old stand-alone callers (their API differs from the live CompactBlock)."""
    """
    BIP152 compact block representation.
    Instead of full block, sends:
    - Block header
    - Short transaction IDs (6 bytes each)
    - Prefilled transactions (coinbase + predicted unknown txs)
    
    Reduces bandwidth by ~98% for nodes with full mempools.
    """

    SHORT_ID_BYTES = 6

    def __init__(self, block: 'Block', nonce: int = None):
        self.header     = block.header
        self.nonce      = nonce or secrets.randbelow(2**64)
        self.prefilled  : List[Tuple[int,'Transaction']] = []
        self.short_ids  : List[int] = []

        self._build(block)

    def _siphash(self, key: bytes, data: bytes) -> int:
        """SipHash for short ID computation"""
        k0 = int.from_bytes(key[:8],  'little')
        k1 = int.from_bytes(key[8:16],'little') if len(key) >= 16 else 0
        h  = hashlib.sha256(key + data).digest()
        return int.from_bytes(h[:8], 'little') & 0xFFFFFFFFFFFFFFFF

    def _short_id(self, txid: str) -> int:
        """Compute 6-byte short transaction ID"""
        header_hash = bytes.fromhex(self.header.hash())
        key         = hashlib.sha256(
            header_hash + self.nonce.to_bytes(8, 'little')
        ).digest()[:16]
        tx_hash = bytes.fromhex(txid)[::-1]
        return self._siphash(key, tx_hash) & ((1 << 48) - 1)

    def _build(self, block: 'Block'):
        """Build compact block from full block"""
        for i, tx in enumerate(block.transactions):
            if tx.is_coinbase or i < 3:
                # Prefill coinbase and first few txs
                self.prefilled.append((i, tx))
            else:
                self.short_ids.append(self._short_id(tx.txid))

    def reconstruct(self, mempool: Dict[str, 'Transaction'],
                     extra_txs: List['Transaction'] = None) -> Optional['Block']:
        """
        Reconstruct full block from compact block + mempool.
        Returns None if any transactions are missing.
        """
        # Build short_id -> tx mapping from mempool
        header_hash = bytes.fromhex(self.header.hash())
        key         = hashlib.sha256(
            header_hash + self.nonce.to_bytes(8, 'little')
        ).digest()[:16]

        short_id_map : Dict[int, 'Transaction'] = {}
        for tx in mempool.values():
            sid = self._short_id(tx.txid)
            short_id_map[sid] = tx

        if extra_txs:
            for tx in extra_txs:
                sid = self._short_id(tx.txid)
                short_id_map[sid] = tx

        # Reconstruct transaction list
        prefill_map = {idx: tx for idx, tx in self.prefilled}
        txs         = []
        short_idx   = 0

        for i in range(len(self.prefilled) + len(self.short_ids)):
            if i in prefill_map:
                txs.append(prefill_map[i])
            else:
                if short_idx >= len(self.short_ids):
                    return None
                sid = self.short_ids[short_idx]
                short_idx += 1
                if sid not in short_id_map:
                    return None   # Request full block
                txs.append(short_id_map[sid])

        return Block(header=self.header, transactions=txs)

    def size_bytes(self) -> int:
        """Approximate compact block size"""
        return (80 +  # header
                8 +   # nonce
                len(self.short_ids) * self.SHORT_ID_BYTES +
                sum(tx.byte_size() + 4 for _, tx in self.prefilled))

    def compression_ratio(self, full_block_size: int) -> float:
        """How much smaller compact block is vs full block"""
        return self.size_bytes() / max(1, full_block_size)

    def to_dict(self) -> dict:
        return {
            "block_hash"       : self.header.hash(),
            "block_height"     : self.header.height,
            "nonce"            : self.nonce,
            "prefilled_txs"    : len(self.prefilled),
            "short_ids"        : len(self.short_ids),
            "compact_size"     : self.size_bytes(),
        }

# ---- EclipseDefense  (kind C, v10.18 lines 31104-31191) ----
class EclipseDefense:
    """
    Eclipse attack detection and prevention.
    Eclipse attack: adversary surrounds node with malicious peers,
    feeding false chain data.
    
    Defenses:
    - Minimum required outbound connections
    - Peer diversity (multiple /16 subnets)
    - Anchor connections (persistent trusted peers)
    - Periodic peer rotation
    - Outbound peer source diversity
    """

    MIN_OUTBOUND    = 8
    MIN_SUBNETS     = 4     # require peers from N different /16 subnets
    MAX_PER_SUBNET  = 2     # max peers from same /16
    ANCHOR_COUNT    = 2     # persistent anchor connections

    def __init__(self):
        self._anchors      : List[str] = []    # anchor peer addresses
        self._peer_subnets : Dict[str, str] = {}   # peer -> /16 subnet
        self._subnet_count : Dict[str, int] = {}   # subnet -> peer count
        self._lock         = threading.RLock()

    def register_peer(self, peer_addr: str) -> bool:
        """Register peer, check eclipse risk. Returns False if should reject."""
        with self._lock:
            subnet = self._get_subnet(peer_addr)
            if subnet:
                count = self._subnet_count.get(subnet, 0)
                if count >= self.MAX_PER_SUBNET and peer_addr not in self._anchors:
                    return False   # too many peers from same subnet
                self._peer_subnets[peer_addr] = subnet
                self._subnet_count[subnet]    = count + 1
            return True

    def unregister_peer(self, peer_addr: str):
        with self._lock:
            subnet = self._peer_subnets.pop(peer_addr, None)
            if subnet and subnet in self._subnet_count:
                self._subnet_count[subnet] = max(0, self._subnet_count[subnet] - 1)

    def _get_subnet(self, addr: str) -> Optional[str]:
        """Get /16 subnet from IPv4 address"""
        try:
            parts = addr.split(':')[0].split('.')
            if len(parts) >= 2:
                return f"{parts[0]}.{parts[1]}"
        except Exception:
            pass
        return None

    def add_anchor(self, peer_addr: str):
        """Add a trusted anchor peer (always maintain connection)"""
        if peer_addr not in self._anchors:
            self._anchors.append(peer_addr)

    def is_anchor(self, peer_addr: str) -> bool:
        return peer_addr in self._anchors

    def subnet_diversity(self) -> int:
        """Count distinct /16 subnets"""
        return len(self._subnet_count)

    def eclipse_risk(self) -> dict:
        """Assess current eclipse attack risk"""
        subnet_div  = self.subnet_diversity()
        peer_count  = len(self._peer_subnets)
        risk_level  = "low"

        if subnet_div < self.MIN_SUBNETS:
            risk_level = "high"
        elif peer_count < self.MIN_OUTBOUND:
            risk_level = "medium"

        return {
            "risk_level"      : risk_level,
            "peer_count"      : peer_count,
            "subnet_diversity": subnet_div,
            "min_required"    : self.MIN_SUBNETS,
            "anchors"         : len(self._anchors),
            "recommendation"  : (
                "Increase outbound connections" if peer_count < self.MIN_OUTBOUND
                else "Connect to more diverse subnets" if subnet_div < self.MIN_SUBNETS
                else "Node is well-protected"
            ),
        }

# ---- AdvancedP2PNode  (kind C, v10.18 lines 31259-31300) ----
class AdvancedP2PNode(P2PNode):
    """
    Extended P2P node with Dandelion++, compact blocks,
    eclipse defense, and topology analysis.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 host: str = "0.0.0.0", port: int = DEFAULT_PORT):
        super().__init__(blockchain, host, port)

        node_id            = secrets.token_bytes(32)
        self.dandelion     = DandelionRouter(node_id)
        self.eclipse       = EclipseDefense()
        self.topology      = NetworkTopologyAnalyzer()
        self._compact_mode = True

    def broadcast_tx_dandelion(self, tx: 'Transaction',
                                source_peer: Optional[bytes] = None):
        """Broadcast transaction using Dandelion++ routing"""
        phase, relay = self.dandelion.route_transaction(tx.txid, source_peer)
        if phase == DandelionPhase.FLUFF:
            # Normal broadcast
            self.broadcast(Message(MsgType.TX, {"txid": tx.txid}))
        else:
            # Stem: route to one peer only
            if relay:
                peer = self._peers.get(relay.decode() if isinstance(relay, bytes) else relay)
                if peer:
                    peer.send(Message(MsgType.TX, {"txid": tx.txid}))

    def get_compact_block(self, block: 'Block') -> CompactBlock:
        """Build compact block for relay"""
        return CompactBlockLegacy(block)

    def advanced_stats(self) -> dict:
        base = {
            "dandelion"  : self.dandelion.stats(),
            "eclipse"    : self.eclipse.eclipse_risk(),
            "topology"   : self.topology.topology_stats(),
            "compact"    : {"enabled": self._compact_mode},
        }
        return base

# ---- GovernanceProposalLegacy  (kind C, v10.18 lines 31384-31432) ----
@dataclass
class GovernanceProposalLegacy:
    """On-chain governance proposal"""
    proposal_id  : str
    title        : str
    description  : str
    proposer     : str
    parameter    : str   # which parameter to change
    new_value    : str   # proposed new value
    start_height : int
    end_height   : int
    yes_votes    : int   = 0
    no_votes     : int   = 0
    abstain      : int   = 0
    created_at   : float = field(default_factory=time.time)
    status       : str   = "active"

    @property
    def total_votes(self) -> int:
        return self.yes_votes + self.no_votes + self.abstain

    @property
    def approval_pct(self) -> float:
        return self.yes_votes / max(1, self.total_votes) * 100

    def is_passed(self, threshold_pct: float = 67.0) -> bool:
        return (self.approval_pct >= threshold_pct and
                self.total_votes >= 10)

    def is_expired(self, current_height: int) -> bool:
        return current_height > self.end_height

    def to_dict(self) -> dict:
        return {
            "proposal_id"  : self.proposal_id,
            "title"        : self.title,
            "description"  : self.description,
            "proposer"     : self.proposer,
            "parameter"    : self.parameter,
            "new_value"    : self.new_value,
            "start_height" : self.start_height,
            "end_height"   : self.end_height,
            "yes_votes"    : self.yes_votes,
            "no_votes"     : self.no_votes,
            "abstain"      : self.abstain,
            "total_votes"  : self.total_votes,
            "approval_pct" : f"{self.approval_pct:.1f}%",
            "status"       : self.status,
        }

# ---- DescriptorType  (kind C, v10.18 lines 31668-31679) ----
class DescriptorType:
    PK      = "pk"
    PKH     = "pkh"
    WPKH    = "wpkh"
    SH      = "sh"
    WSH     = "wsh"
    TR      = "tr"
    MULTI   = "multi"
    SORTEDMULTI = "sortedmulti"
    RAW     = "raw"
    ADDR    = "addr"
    COMBO   = "combo"

# ---- DescriptorKey  (kind C, v10.18 lines 31739-31810) ----
@dataclass
class DescriptorKey:
    """A key expression in a descriptor"""
    raw_key     : str              # original key string
    xpub        : Optional[str] = None
    xprv        : Optional[str] = None
    fingerprint : str = "00000000"
    path        : str = ""         # derivation path e.g. m/44'/2025'/0'
    child       : str = ""         # child key range e.g. /0/*, /1/*
    is_range    : bool = False
    pubkey_bytes: Optional[bytes] = None

    @classmethod
    def parse(cls, key_str: str) -> 'DescriptorKey':
        """Parse key expression from descriptor"""
        k = cls(raw_key=key_str)
        # Check for origin [fingerprint/path]
        if key_str.startswith('['):
            end = key_str.index(']')
            origin = key_str[1:end]
            key_str = key_str[end+1:]
            parts = origin.split('/', 1)
            k.fingerprint = parts[0]
            if len(parts) > 1:
                k.path = 'm/' + parts[1]
        # Check for derivation suffix
        if '/' in key_str:
            idx = key_str.rindex('/')
            base = key_str[:idx]
            child_part = key_str[idx:]
            k.child    = child_part
            k.is_range = '*' in child_part
            key_str    = base
        # Is it xpub/xprv?
        if key_str.startswith('xpub') or key_str.startswith('tpub'):
            k.xpub = key_str
        elif key_str.startswith('xprv') or key_str.startswith('tprv'):
            k.xprv = key_str
        else:
            # Assume raw hex pubkey
            try:
                k.pubkey_bytes = bytes.fromhex(key_str)
            except Exception:
                pass
        return k

    def derive_address(self, index: int = 0, hrp: str = "nbl") -> Optional[str]:
        """Derive address for given index"""
        if self.pubkey_bytes:
            return Script.p2pkh_address(self.pubkey_bytes)
        if self.xpub:
            try:
                master = HDKey.from_xpub(self.xpub)
                path   = self.child.replace('*', str(index)).lstrip('/')
                if path:
                    key = master.derive_path('m/' + path)
                else:
                    key = master
                return key.address
            except Exception:
                pass
        return None

    def to_dict(self) -> dict:
        return {
            "raw"        : self.raw_key,
            "fingerprint": self.fingerprint,
            "path"       : self.path,
            "child"      : self.child,
            "is_range"   : self.is_range,
            "xpub"       : self.xpub,
        }

# ---- OutputDescriptorAlt  (kind C, v10.18 lines 31813-31943) ----
@dataclass
class OutputDescriptorAlt:
    """
    BIP380 Output Script Descriptor.
    Describes exactly what scripts and addresses a wallet manages.
    Standard format for wallet backup and import/export.
    """
    desc_type    : str
    keys         : List[DescriptorKey] = field(default_factory=list)
    threshold    : int  = 1
    inner        : Optional['OutputDescriptor'] = None   # for sh(wpkh(...))
    raw_script   : Optional[bytes] = None
    address      : Optional[str]   = None
    checksum     : str = ""
    is_range     : bool = False

    @classmethod
    def parse(cls, descriptor: str) -> 'OutputDescriptor':
        """Parse a descriptor string"""
        # Strip checksum
        if '#' in descriptor:
            descriptor, chk = descriptor.split('#', 1)
        else:
            chk = ""

        d = cls(desc_type="unknown", checksum=chk)

        # Match function name
        m = re.match(r'^(\w+)\((.+)\)$', descriptor.strip(), re.DOTALL)
        if not m:
            return d

        func   = m.group(1).lower()
        inner  = m.group(2)
        d.desc_type = func

        if func in (DescriptorType.PK, DescriptorType.PKH, DescriptorType.WPKH):
            d.keys = [DescriptorKey.parse(inner)]
            d.is_range = d.keys[0].is_range

        elif func in (DescriptorType.SH, DescriptorType.WSH):
            d.inner = OutputDescriptor.parse(inner)
            d.is_range = d.inner.is_range

        elif func in (DescriptorType.MULTI, DescriptorType.SORTEDMULTI):
            parts = inner.split(',')
            d.threshold = int(parts[0])
            d.keys = [DescriptorKey.parse(k.strip()) for k in parts[1:]]
            d.is_range = any(k.is_range for k in d.keys)

        elif func == DescriptorType.TR:
            d.keys = [DescriptorKey.parse(inner.split(',')[0])]
            d.is_range = d.keys[0].is_range

        elif func == DescriptorType.ADDR:
            d.address = inner
        elif func == DescriptorType.RAW:
            try: d.raw_script = bytes.fromhex(inner)
            except Exception: pass

        return d

    def derive_scripts(self, index: int = 0) -> List[bytes]:
        """Derive output scripts for given index"""
        scripts = []
        if self.desc_type == DescriptorType.PKH:
            for key in self.keys:
                addr = key.derive_address(index)
                if addr:
                    scripts.append(Script.p2pkh_locking_from_address(addr))

        elif self.desc_type == DescriptorType.WPKH:
            for key in self.keys:
                if key.pubkey_bytes:
                    scripts.append(SegWitScript.p2wpkh(key.pubkey_bytes))

        elif self.desc_type == DescriptorType.TR:
            for key in self.keys:
                if key.pubkey_bytes and len(key.pubkey_bytes) == 33:
                    _, script = SegWitScript.p2tr_from_privkey(
                        int.from_bytes(key.pubkey_bytes[1:], 'big'))
                    scripts.append(script)

        elif self.desc_type == DescriptorType.ADDR:
            if self.address:
                scripts.append(Script.p2pkh_locking_from_address(self.address))

        elif self.desc_type == DescriptorType.RAW:
            if self.raw_script:
                scripts.append(self.raw_script)

        return scripts

    def derive_addresses(self, start: int = 0, count: int = 10) -> List[str]:
        """Derive a range of addresses"""
        addrs = []
        for i in range(start, start + count):
            for key in self.keys:
                addr = key.derive_address(i)
                if addr:
                    addrs.append(addr)
        return list(dict.fromkeys(addrs))   # deduplicate

    def to_string(self, add_checksum: bool = True) -> str:
        """Serialize descriptor to string"""
        if self.desc_type == DescriptorType.PKH and self.keys:
            s = f"pkh({self.keys[0].raw_key})"
        elif self.desc_type == DescriptorType.WPKH and self.keys:
            s = f"wpkh({self.keys[0].raw_key})"
        elif self.desc_type == DescriptorType.TR and self.keys:
            s = f"tr({self.keys[0].raw_key})"
        elif self.desc_type == DescriptorType.MULTI:
            keys_str = ','.join(k.raw_key for k in self.keys)
            s = f"multi({self.threshold},{keys_str})"
        elif self.desc_type == DescriptorType.ADDR and self.address:
            s = f"addr({self.address})"
        elif self.desc_type == DescriptorType.RAW and self.raw_script:
            s = f"raw({self.raw_script.hex()})"
        else:
            s = f"{self.desc_type}(...)"
        return DescriptorChecksum.add_checksum(s) if add_checksum else s

    def to_dict(self) -> dict:
        return {
            "type"      : self.desc_type,
            "is_range"  : self.is_range,
            "threshold" : self.threshold,
            "keys"      : [k.to_dict() for k in self.keys],
            "checksum"  : self.checksum,
            "descriptor": self.to_string(),
        }

# ---- DescriptorWallet  (kind C, v10.18 lines 31946-32080) ----
class DescriptorWallet:
    """
    BIP380-style descriptor-based wallet.
    Manages multiple descriptors for receive + change addresses.
    Supports: P2PKH, P2WPKH, P2TR, multisig.
    """

    def __init__(self, name: str = "default"):
        self.name         = name
        self._descriptors : List[Tuple[OutputDescriptor, str]] = []
        self._utxo        : Optional['UTXOSet'] = None
        self._next_index  : Dict[str, int] = {}
        self._lock        = threading.RLock()
        self._labels      : Dict[str, str] = {}   # address → label

    def add_descriptor(self, descriptor: str,
                        purpose: str = "receive") -> bool:
        """Add a descriptor to the wallet"""
        desc = OutputDescriptor.parse(descriptor)
        if desc.desc_type == "unknown":
            return False
        with self._lock:
            self._descriptors.append((desc, purpose))
            key = f"{purpose}_{len(self._descriptors)}"
            self._next_index[key] = 0
        return True

    @classmethod
    def from_seed(cls, seed: bytes, name: str = "default") -> 'DescriptorWallet':
        """Create wallet from BIP32 seed with standard descriptors"""
        master = HDKey.from_seed(seed)
        wallet = cls(name)

        # P2PKH receive/change
        pkh_receive = f"pkh([{master.fingerprint()}/{NBL_BIP44_PATH[2:]}/0/*])"
        pkh_change  = f"pkh([{master.fingerprint()}/{NBL_BIP44_PATH[2:]}/1/*])"
        wallet.add_descriptor(pkh_receive, "receive")
        wallet.add_descriptor(pkh_change,  "change")

        # P2WPKH receive/change
        wpkh_path   = "m/84'/2025'/0'"
        wpkh_recv   = f"wpkh([{master.fingerprint()}/{wpkh_path[2:]}/0/*])"
        wpkh_chng   = f"wpkh([{master.fingerprint()}/{wpkh_path[2:]}/1/*])"
        wallet.add_descriptor(wpkh_recv, "receive")
        wallet.add_descriptor(wpkh_chng, "change")

        # P2TR (Taproot)
        tr_path     = "m/86'/2025'/0'"
        tr_recv     = f"tr([{master.fingerprint()}/{tr_path[2:]}/0/*])"
        tr_chng     = f"tr([{master.fingerprint()}/{tr_path[2:]}/1/*])"
        wallet.add_descriptor(tr_recv, "receive")
        wallet.add_descriptor(tr_chng, "change")

        return wallet

    def get_receive_address(self, script_type: str = "pkh") -> Optional[str]:
        """Get next unused receive address"""
        with self._lock:
            for i, (desc, purpose) in enumerate(self._descriptors):
                if purpose == "receive" and desc.desc_type == script_type:
                    key   = f"receive_{i+1}"
                    idx   = self._next_index.get(key, 0)
                    addrs = desc.derive_addresses(idx, 1)
                    if addrs:
                        return addrs[0]
        return None

    def get_change_address(self, script_type: str = "pkh") -> Optional[str]:
        """Get next change address"""
        with self._lock:
            for i, (desc, purpose) in enumerate(self._descriptors):
                if purpose == "change" and desc.desc_type == script_type:
                    key   = f"change_{i+1}"
                    idx   = self._next_index.get(key, 0)
                    addrs = desc.derive_addresses(idx, 1)
                    if addrs:
                        return addrs[0]
        return None

    def get_all_addresses(self, count: int = 20) -> List[dict]:
        """Get all watched addresses with labels"""
        result = []
        with self._lock:
            for i, (desc, purpose) in enumerate(self._descriptors):
                addrs = desc.derive_addresses(0, count)
                for addr in addrs:
                    result.append({
                        "address"  : addr,
                        "purpose"  : purpose,
                        "type"     : desc.desc_type,
                        "label"    : self._labels.get(addr, ""),
                    })
        return result

    def label_address(self, address: str, label: str):
        """Label an address"""
        with self._lock:
            self._labels[address] = label

    def export_descriptors(self) -> List[dict]:
        """Export all descriptors"""
        with self._lock:
            return [{"descriptor": desc.to_string(),
                     "purpose"   : purpose,
                     "type"      : desc.desc_type,
                     "is_range"  : desc.is_range}
                    for desc, purpose in self._descriptors]

    def to_json(self) -> str:
        """Serialize wallet to JSON"""
        import json
        return json.dumps({
            "name"       : self.name,
            "descriptors": self.export_descriptors(),
            "labels"     : self._labels,
            "version"    : 1,
        }, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'DescriptorWallet':
        """Deserialize wallet from JSON"""
        import json
        data   = json.loads(json_str)
        wallet = cls(data.get("name", "default"))
        for d in data.get("descriptors", []):
            wallet.add_descriptor(d["descriptor"], d.get("purpose", "receive"))
        wallet._labels = data.get("labels", {})
        return wallet

    def stats(self) -> dict:
        return {
            "name"        : self.name,
            "descriptors" : len(self._descriptors),
            "labels"      : len(self._labels),
        }

# ---- WalletManager  (kind C, v10.18 lines 32083-32190) ----
class WalletManager:
    """
    Multi-wallet support — manage multiple wallets simultaneously.
    Each wallet is independent with its own descriptors and UTXOs.
    Supports: create, load, unload, list, switch active wallet.
    """

    def __init__(self, data_dir: str = "./nebula_wallets"):
        self.data_dir   = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self._wallets   : Dict[str, DescriptorWallet] = {}
        self._active    : Optional[str] = None
        self._lock      = threading.RLock()

    def create_wallet(self, name: str,
                       mnemonic: str = None,
                       passphrase: str = "") -> DescriptorWallet:
        """Create a new descriptor wallet"""
        with self._lock:
            if name in self._wallets:
                raise ValueError(f"Wallet '{name}' already exists")

            if mnemonic is None:
                mnemonic = BIP39.generate_mnemonic(12)

            seed   = BIP39.mnemonic_to_seed(mnemonic, passphrase)
            wallet = DescriptorWallet.from_seed(seed, name)
            self._wallets[name] = wallet

            # Save to disk
            wallet_path = self.data_dir / f"{name}.json"
            wallet_path.write_text(wallet.to_json())

            if self._active is None:
                self._active = name

            return wallet

    def load_wallet(self, name: str) -> Optional[DescriptorWallet]:
        """Load wallet from disk"""
        with self._lock:
            wallet_path = self.data_dir / f"{name}.json"
            if not wallet_path.exists():
                return None
            wallet = DescriptorWallet.from_json(wallet_path.read_text())
            self._wallets[name] = wallet
            return wallet

    def unload_wallet(self, name: str):
        """Unload wallet from memory"""
        with self._lock:
            if name in self._wallets:
                # Save first
                wallet_path = self.data_dir / f"{name}.json"
                wallet_path.write_text(self._wallets[name].to_json())
                del self._wallets[name]
            if self._active == name:
                self._active = next(iter(self._wallets), None)

    def get_wallet(self, name: str = None) -> Optional[DescriptorWallet]:
        """Get wallet by name or active wallet"""
        with self._lock:
            target = name or self._active
            return self._wallets.get(target)

    def set_active(self, name: str) -> bool:
        with self._lock:
            if name in self._wallets:
                self._active = name
                return True
            return False

    def list_wallets(self) -> List[dict]:
        """List all loaded and on-disk wallets"""
        result = []
        # Loaded wallets
        with self._lock:
            for name, wallet in self._wallets.items():
                result.append({
                    "name"    : name,
                    "loaded"  : True,
                    "active"  : name == self._active,
                    "stats"   : wallet.stats(),
                })
            # On-disk wallets not loaded
            for f in self.data_dir.glob("*.json"):
                name = f.stem
                if name not in self._wallets:
                    result.append({
                        "name"  : name,
                        "loaded": False,
                        "active": False,
                    })
        return result

    def save_all(self):
        """Save all loaded wallets to disk"""
        with self._lock:
            for name, wallet in self._wallets.items():
                wallet_path = self.data_dir / f"{name}.json"
                wallet_path.write_text(wallet.to_json())

    def stats(self) -> dict:
        return {
            "loaded_wallets": len(self._wallets),
            "active"        : self._active,
            "data_dir"      : str(self.data_dir),
        }

# ---- SyncStateV2  (kind C, v10.18 lines 32222-32228) ----
class SyncStateV2(Enum):
    IDLE         = "idle"
    HEADERS_SYNC = "headers_sync"
    BLOCK_SYNC   = "block_sync"
    SYNCED       = "synced"
    STALLED      = "stalled"
    REORGING     = "reorging"

# ---- SyncMonitor  (kind C, v10.18 lines 32720-32775) ----
class SyncMonitor:
    """
    Real-time sync progress monitoring.
    Tracks sync speed, ETA, stall detection.
    """

    def __init__(self, ibd: IBDManager):
        self.ibd         = ibd
        self._samples    : List[Tuple[float, int]] = []
        self._max_samples = 60
        self._lock       = threading.Lock()

    def sample(self):
        """Take a height sample for speed calculation"""
        with self._lock:
            self._samples.append((time.time(), self.ibd.bc.height))
            if len(self._samples) > self._max_samples:
                self._samples.pop(0)

    def blocks_per_second(self) -> float:
        """Calculate recent sync speed"""
        with self._lock:
            if len(self._samples) < 2:
                return 0.0
            dt     = self._samples[-1][0] - self._samples[0][0]
            dblocks = self._samples[-1][1] - self._samples[0][1]
            return dblocks / max(1, dt)

    def eta_seconds(self) -> Optional[float]:
        """Estimated time to complete sync"""
        speed   = self.blocks_per_second()
        remaining = max(0, self.ibd._best_height_seen - self.ibd.bc.height)
        if speed <= 0:
            return None
        return remaining / speed

    def is_stalled(self) -> bool:
        """True if sync appears stalled"""
        with self._lock:
            if len(self._samples) < 2:
                return False
            dt = self._samples[-1][0] - self._samples[0][0]
            dh = self._samples[-1][1] - self._samples[0][1]
            return dt > STALL_TIMEOUT_SECS and dh == 0

    def status(self) -> dict:
        eta = self.eta_seconds()
        return {
            "synced"        : self.ibd.is_synced(),
            "progress_pct"  : f"{self.ibd.sync_progress()*100:.2f}%",
            "blocks_per_sec": round(self.blocks_per_second(), 2),
            "eta_secs"      : round(eta) if eta else None,
            "stalled"       : self.is_stalled(),
            "current_height": self.ibd.bc.height,
            "target_height" : self.ibd._best_height_seen,
        }

# ---- AddressBookEntry  (kind C, v10.18 lines 32793-32834) ----
@dataclass
class AddressBookEntry:
    """A single entry in the address book"""
    address     : str
    label       : str
    category    : str  = "personal"    # personal/exchange/mining/contract/foundation
    note        : str  = ""
    is_mine     : bool = False
    is_watch_only: bool = False
    created_at  : float = field(default_factory=time.time)
    last_used   : float = 0.0
    use_count   : int   = 0
    tags        : List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "address"      : self.address,
            "label"        : self.label,
            "category"     : self.category,
            "note"         : self.note,
            "is_mine"      : self.is_mine,
            "is_watch_only": self.is_watch_only,
            "created_at"   : self.created_at,
            "last_used"    : self.last_used,
            "use_count"    : self.use_count,
            "tags"         : self.tags,
        }

    @classmethod
    def from_dict(cls, d: dict) -> 'AddressBookEntry':
        return cls(
            address      = d["address"],
            label        = d.get("label", ""),
            category     = d.get("category", "personal"),
            note         = d.get("note", ""),
            is_mine      = d.get("is_mine", False),
            is_watch_only= d.get("is_watch_only", False),
            created_at   = d.get("created_at", time.time()),
            last_used    = d.get("last_used", 0.0),
            use_count    = d.get("use_count", 0),
            tags         = d.get("tags", []),
        )

# ---- TransactionNote  (kind C, v10.18 lines 32837-32855) ----
@dataclass
class TransactionNote:
    """User note attached to a transaction"""
    txid      : str
    note      : str
    amount_nbl: float
    direction : str    # "sent" / "received"
    timestamp : float = field(default_factory=time.time)
    tags      : List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "txid"      : self.txid,
            "note"      : self.note,
            "amount_nbl": self.amount_nbl,
            "direction" : self.direction,
            "timestamp" : self.timestamp,
            "tags"      : self.tags,
        }

# ---- WatchOnlyWalletV2  (kind C, v10.18 lines 32858-32954) ----
class WatchOnlyWalletV2:
    """
    Watch-only wallet: tracks addresses without private keys.
    Used for cold storage monitoring, exchange addresses, multisig.
    Can verify received payments without ability to spend.
    """

    def __init__(self, name: str, blockchain: 'NEBULABlockchain' = None):
        self.name       = name
        self.bc         = blockchain
        self._addresses : Set[str] = set()
        self._lock      = threading.RLock()

    def add_address(self, address: str) -> bool:
        """Add address to watch list"""
        try:
            base58check_decode(address)
            with self._lock:
                self._addresses.add(address)
            return True
        except Exception:
            return False

    def add_addresses(self, addresses: List[str]) -> int:
        """Bulk add addresses. Returns count added."""
        count = 0
        for addr in addresses:
            if self.add_address(addr):
                count += 1
        return count

    def remove_address(self, address: str):
        with self._lock:
            self._addresses.discard(address)

    def get_balance(self, address: str) -> float:
        """Get balance for watched address"""
        if address not in self._addresses:
            return 0.0
        if self.bc:
            return self.bc.utxo.balance(address) / 10**DECIMALS
        return 0.0

    def get_total_balance(self) -> float:
        """Total balance across all watched addresses"""
        if not self.bc:
            return 0.0
        with self._lock:
            return sum(self.bc.utxo.balance(a) for a in self._addresses) / 10**DECIMALS

    def get_utxos(self, address: str) -> List[dict]:
        """Get UTXOs for watched address"""
        if not self.bc or address not in self._addresses:
            return []
        utxos = self.bc.utxo.get_by_address(address)
        return [{"txid": u.txid, "vout": u.index,
                 "value_nbl": u.value / 10**DECIMALS,
                 "height": u.height,
                 "matured": (self.bc.height - u.height >= COINBASE_MATURITY
                             if u.is_coinbase else True)}
                for u in utxos]

    def has_received(self, address: str) -> bool:
        """True if address has ever received funds"""
        if not self.bc or address not in self._addresses:
            return False
        return self.bc.utxo.balance(address) > 0

    def scan_blockchain(self) -> dict:
        """Scan blockchain for transactions to watched addresses"""
        results = {}
        if not self.bc:
            return results
        with self._lock:
            for addr in self._addresses:
                bal = self.bc.utxo.balance(addr)
                if bal > 0:
                    results[addr] = {
                        "balance_nbl": bal / 10**DECIMALS,
                        "utxos"      : len(self.bc.utxo.get_by_address(addr)),
                    }
        return results

    def addresses(self) -> List[str]:
        with self._lock:
            return list(self._addresses)

    def count(self) -> int:
        return len(self._addresses)

    def to_dict(self) -> dict:
        return {
            "name"      : self.name,
            "addresses" : self.addresses(),
            "count"     : self.count(),
            "balance"   : self.get_total_balance(),
        }

# ---- AddressBookLabels  (kind C, v10.18 lines 32957-33112) ----
class AddressBookLabels:
    """
    Full address book with labels, categories, search, and persistence.
    """

    CATEGORIES = ["personal", "exchange", "mining", "contract", "foundation",
                   "merchant", "donation", "cold_storage", "other"]

    def __init__(self, data_path: str = "./nebula_address_book.json"):
        self.data_path = Path(data_path)
        self._entries  : Dict[str, AddressBookEntry] = {}
        self._tx_notes : Dict[str, TransactionNote]  = {}
        self._lock     = threading.RLock()

        # Pre-populate with foundation address
        self.add(FOUNDATION_ADDRESS, "NEBULA Foundation",
                 category="foundation",
                 note="NEBULA development fund — 2% of all block rewards")

        self.load()

    def add(self, address: str, label: str,
            category: str = "personal",
            note: str = "",
            tags: List[str] = None) -> bool:
        """Add or update address book entry"""
        with self._lock:
            self._entries[address] = AddressBookEntry(
                address   = address,
                label     = label,
                category  = category,
                note      = note,
                tags      = tags or [],
            )
            return True

    def remove(self, address: str) -> bool:
        with self._lock:
            if address in self._entries:
                del self._entries[address]
                return True
            return False

    def get(self, address: str) -> Optional[AddressBookEntry]:
        return self._entries.get(address)

    def label(self, address: str) -> str:
        """Get label for address, or shortened address if not found"""
        entry = self._entries.get(address)
        if entry:
            return entry.label
        return address[:12] + "..."

    def search(self, query: str) -> List[AddressBookEntry]:
        """Search by address, label, note, or tag"""
        q = query.lower()
        with self._lock:
            return [e for e in self._entries.values()
                    if (q in e.address.lower() or
                        q in e.label.lower() or
                        q in e.note.lower() or
                        any(q in tag.lower() for tag in e.tags))]

    def by_category(self, category: str) -> List[AddressBookEntry]:
        with self._lock:
            return [e for e in self._entries.values()
                    if e.category == category]

    def mark_used(self, address: str):
        """Mark address as recently used"""
        with self._lock:
            entry = self._entries.get(address)
            if entry:
                entry.last_used = time.time()
                entry.use_count += 1

    def recently_used(self, count: int = 10) -> List[AddressBookEntry]:
        """Get most recently used addresses"""
        with self._lock:
            used = [e for e in self._entries.values() if e.last_used > 0]
            return sorted(used, key=lambda e: e.last_used, reverse=True)[:count]

    # ── Transaction notes ─────────────────────────────────────────
    def add_tx_note(self, txid: str, note: str,
                    amount_nbl: float = 0.0,
                    direction: str = "received",
                    tags: List[str] = None):
        with self._lock:
            self._tx_notes[txid] = TransactionNote(
                txid       = txid,
                note       = note,
                amount_nbl = amount_nbl,
                direction  = direction,
                tags       = tags or [],
            )

    def get_tx_note(self, txid: str) -> Optional[TransactionNote]:
        return self._tx_notes.get(txid)

    def search_tx_notes(self, query: str) -> List[TransactionNote]:
        q = query.lower()
        with self._lock:
            return [n for n in self._tx_notes.values()
                    if q in n.note.lower() or
                    any(q in tag.lower() for tag in n.tags)]

    # ── Persistence ───────────────────────────────────────────────
    def save(self) -> bool:
        try:
            with self._lock:
                data = {
                    "version"  : 1,
                    "entries"  : {a: e.to_dict()
                                  for a, e in self._entries.items()},
                    "tx_notes" : {t: n.to_dict()
                                  for t, n in self._tx_notes.items()},
                }
            self.data_path.write_text(json.dumps(data, indent=2))
            return True
        except Exception:
            return False

    def load(self) -> bool:
        if not self.data_path.exists():
            return False
        try:
            data = json.loads(self.data_path.read_text())
            with self._lock:
                for addr, d in data.get("entries", {}).items():
                    self._entries[addr] = AddressBookEntry.from_dict(d)
                for txid, d in data.get("tx_notes", {}).items():
                    self._tx_notes[txid] = TransactionNote(**d)
            return True
        except Exception:
            return False

    def export_csv(self) -> str:
        """Export address book as CSV"""
        lines = ["address,label,category,note,use_count,created_at"]
        with self._lock:
            for e in self._entries.values():
                lines.append(f'"{e.address}","{e.label}","{e.category}",'
                             f'"{e.note}",{e.use_count},{e.created_at:.0f}')
        return "\n".join(lines)

    def stats(self) -> dict:
        with self._lock:
            by_cat = {}
            for e in self._entries.values():
                by_cat[e.category] = by_cat.get(e.category, 0) + 1
            return {
                "total"       : len(self._entries),
                "tx_notes"    : len(self._tx_notes),
                "by_category" : by_cat,
                "has_file"    : self.data_path.exists(),
            }

# ---- QRCodeGenerator  (kind C, v10.18 lines 33115-33170) ----
class QRCodeGenerator:
    """
    ASCII QR code generator for NBL addresses.
    Displays payment QR codes in terminal.
    Format: nebula:<address>?amount=<nbl>
    """

    @staticmethod
    def payment_uri(address: str, amount_nbl: float = 0,
                    label: str = "", message: str = "") -> str:
        """Generate BIP21-style payment URI"""
        params = []
        if amount_nbl > 0:
            params.append(f"amount={amount_nbl:.9f}")
        if label:
            params.append(f"label={label.replace(' ', '+')}")
        if message:
            params.append(f"message={message.replace(' ', '+')}")
        uri = f"nebula:{address}"
        if params:
            uri += "?" + "&".join(params)
        return uri

    @staticmethod
    def ascii_qr(data: str, size: int = 21) -> str:
        """
        Generate simple ASCII art QR placeholder.
        Full QR requires qrcode library — this provides a visual placeholder.
        """
        # Deterministic pattern based on data hash
        h = hashlib.sha256(data.encode()).digest()
        lines = ["┌" + "─" * (size * 2) + "┐"]
        for row in range(size):
            line = "│"
            for col in range(size):
                bit = (h[(row * size + col) % len(h)] >>
                       ((row * size + col) % 8)) & 1
                line += "██" if bit else "  "
            line += "│"
            lines.append(line)
        lines.append("└" + "─" * (size * 2) + "┘")
        lines.append(f"  {data[:40]}{'...' if len(data) > 40 else ''}")
        return "\n".join(lines)

    @classmethod
    def display_payment(cls, address: str, amount_nbl: float = 0,
                         label: str = ""):
        """Print payment QR to terminal"""
        uri = cls.payment_uri(address, amount_nbl, label)
        print(cls.ascii_qr(uri))
        print(f"\nAddress : {address}")
        if amount_nbl > 0:
            print(f"Amount  : {amount_nbl:.9f} NBL")
        if label:
            print(f"Label   : {label}")
        print(f"URI     : {uri}")

# ---- ContactManager  (kind C, v10.18 lines 33173-33244) ----
class ContactManager:
    """
    High-level contact management combining address book + watch-only wallets.
    Each contact can have multiple addresses across different networks.
    """

    @dataclass
    class ContactAdv:
        name        : str
        addresses   : Dict[str, str] = field(default_factory=dict)  # label→address
        email       : str = ""
        note        : str = ""
        created_at  : float = field(default_factory=time.time)
        tags        : List[str] = field(default_factory=list)

        def to_dict(self) -> dict:
            return {
                "name"      : self.name,
                "addresses" : self.addresses,
                "email"     : self.email,
                "note"      : self.note,
                "created_at": self.created_at,
                "tags"      : self.tags,
            }

    def __init__(self, address_book: AddressBook):
        self.book     = address_book
        self._contacts: Dict[str, 'ContactManager.Contact'] = {}
        self._lock    = threading.RLock()

    def add_contact(self, name: str, addresses: Dict[str, str] = None,
                     email: str = "", note: str = "",
                     tags: List[str] = None) -> 'ContactManager.Contact':
        """Add a new contact"""
        with self._lock:
            contact = self.Contact(
                name      = name,
                addresses = addresses or {},
                email     = email,
                note      = note,
                tags      = tags or [],
            )
            self._contacts[name] = contact
            # Register all addresses in address book
            for label, addr in (addresses or {}).items():
                self.book.add(addr, f"{name} ({label})",
                              note=f"Contact: {name}")
            return contact

    def get_contact(self, name: str) -> Optional['ContactManager.Contact']:
        return self._contacts.get(name)

    def search_contacts(self, query: str) -> List['ContactManager.Contact']:
        q = query.lower()
        with self._lock:
            return [c for c in self._contacts.values()
                    if q in c.name.lower() or q in c.email.lower() or
                    any(q in addr.lower() for addr in c.addresses.values())]

    def list_contacts(self) -> List[dict]:
        with self._lock:
            return [c.to_dict() for c in self._contacts.values()]

    def delete_contact(self, name: str) -> bool:
        with self._lock:
            if name in self._contacts:
                del self._contacts[name]
                return True
            return False

    def count(self) -> int:
        return len(self._contacts)

# ---- KeyOrigin  (kind C, v10.18 lines 33280-33282) ----
class KeyOrigin(Enum):
    INTERNAL = 0   # change address
    EXTERNAL = 1   # receive address

# ---- BIP39Wallet  (kind C, v10.18 lines 33446-33525) ----
class BIP39Wallet:
    """
    BIP39 mnemonic generation and seed derivation.
    Supports 12, 15, 18, 21, 24 word mnemonics.
    Built-in English wordlist (2048 words).
    """

    # Abbreviated wordlist — first 200 words for demonstration
    # Full 2048-word list would be embedded in production
    WORDLIST_SAMPLE = [
        "abandon","ability","able","about","above","absent","absorb","abstract",
        "absurd","abuse","access","accident","account","accuse","achieve","acid",
        "acoustic","acquire","across","act","action","actor","actress","actual",
        "adapt","add","addict","address","adjust","admit","adult","advance",
        "advice","aerobic","afford","afraid","again","agent","agree","ahead",
        "aim","air","airport","aisle","alarm","album","alcohol","alert","alien",
        "all","alley","allow","almost","alone","alpha","already","also","alter",
        "always","amateur","amazing","among","amount","amused","analyst","anchor",
        "ancient","anger","angle","angry","animal","ankle","announce","annual",
        "another","answer","antenna","antique","anxiety","any","apart","apology",
        "appear","apple","approve","april","arch","arctic","area","arena","argue",
        "arm","armed","armor","army","around","arrange","arrest","arrive","arrow",
        "art","artefact","artist","artwork","ask","aspect","assault","asset",
        "assist","assume","asthma","athlete","atom","attack","attend","attitude",
        "attract","auction","audit","august","aunt","author","auto","autumn",
        "average","avocado","avoid","awake","aware","away","awesome","awful",
        "awkward","axis","baby","balance","bamboo","banner","barely","bargain",
        "barrel","base","basic","basket","battle","beach","bean","beauty",
        "become","beef","before","begin","behave","behind","believe","below",
        "belt","bench","benefit","best","betray","better","between","beyond",
        "bicycle","bid","bike","bind","biology","bird","birth","bitter","black",
        "blade","blame","blanket","blast","bleak","bless","blind","blood","blossom",
        "blouse","blue","blur","blush","board","boat","body","boil","bomb","bone",
        "book","boost","border","boring","borrow","boss","bottom","bounce","box",
        "boy","bracket","brain","brand","brave","breeze","brick","bridge","brief",
        "bright","bring","brisk","broccoli","broken","bronze","broom","brother",
        "brown","brush","bubble","buddy","budget","buffalo","build","bulb","bulk",
        "bullet","bundle","bunker","burden","burger","burst","bus","business",
        "busy","butter","buyer","buzz","cabbage","cabin","cable","cactus","cage",
    ]

    @classmethod
    def generate(cls, strength: int = 128) -> str:
        """
        Generate BIP39 mnemonic.
        strength: 128=12 words, 160=15, 192=18, 224=21, 256=24
        """
        if strength not in (128, 160, 192, 224, 256):
            raise ValueError("strength must be 128/160/192/224/256")

        entropy   = secrets.token_bytes(strength // 8)
        h         = hashlib.sha256(entropy).digest()
        checksum  = bin(h[0])[2:].zfill(8)[:strength // 32]
        bits      = bin(int.from_bytes(entropy, 'big'))[2:].zfill(strength) + checksum

        words = []
        for i in range(0, len(bits), 11):
            idx = int(bits[i:i+11], 2)
            words.append(cls.WORDLIST_SAMPLE[idx % len(cls.WORDLIST_SAMPLE)])

        return ' '.join(words)

    @classmethod
    def to_seed(cls, mnemonic: str, passphrase: str = "") -> bytes:
        """Derive 64-byte seed from mnemonic (BIP39 PBKDF2)"""
        import unicodedata
        mnemonic   = unicodedata.normalize('NFKD', mnemonic)
        passphrase = unicodedata.normalize('NFKD', "mnemonic" + passphrase)
        return hashlib.pbkdf2_hmac(
            'sha512',
            mnemonic.encode('utf-8'),
            passphrase.encode('utf-8'),
            2048
        )

    @classmethod
    def validate(cls, mnemonic: str) -> bool:
        """Validate mnemonic word count"""
        words = mnemonic.strip().split()
        return len(words) in (12, 15, 18, 21, 24)

# ---- OutputDescriptorUtil  (kind C, v10.18 lines 33528-33591) ----
class OutputDescriptorUtil:
    """
    Bitcoin output descriptors (BIP380/381/382/383/384/385/386).
    Portable wallet backup format — describes exactly how to
    derive addresses and scripts from a set of keys.
    """

    SUPPORTED = {"pk", "pkh", "wpkh", "sh", "wsh", "tr", "multi", "sortedmulti",
                 "combo", "addr", "raw"}

    @staticmethod
    def from_xpub(xpub: str, path: str = "0/*",
                  addr_type: AddressType = AddressType.P2PKH) -> str:
        """Create descriptor from xpub"""
        key_expr = f"[{xpub}/{path}]"
        if addr_type == AddressType.P2PKH:
            return f"pkh({key_expr})"
        elif addr_type == AddressType.P2WPKH:
            return f"wpkh({key_expr})"
        elif addr_type == AddressType.P2TR:
            return f"tr({key_expr})"
        else:
            return f"sh(wpkh({key_expr}))"

    @staticmethod
    def multisig(m: int, xpubs: List[str], sorted_keys: bool = True) -> str:
        """Create m-of-n multisig descriptor"""
        func = "sortedmulti" if sorted_keys else "multi"
        keys = ",".join(xpubs)
        return f"sh({func}({m},{keys}))"

    @staticmethod
    def checksum(descriptor: str) -> str:
        """Add descriptor checksum"""
        CHARSET = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
        c = 1
        cls_val = 0
        for ch in descriptor:
            cls_val = ord(ch) >> 5
            c = c * 32 ^ cls_val
            for i in range(5):
                c = (c >> 1) ^ (0xf5dee51989 if c & 1 else 0)
            c ^= ord(ch) & 31
        for i in range(8):
            c ^= 0
            c = (c >> 5) ^ (0xf5dee51989 if c & 1 else 0)
        c ^= 1
        checksum = ''
        for i in range(8):
            checksum = CHARSET[(c >> (5 * (7 - i))) & 31] + checksum
        return f"{descriptor}#{checksum}"

    @staticmethod
    def parse(descriptor: str) -> dict:
        """Parse descriptor into components"""
        descriptor = descriptor.split('#')[0].strip()
        for func in ["wpkh", "pkh", "tr", "sh", "wsh", "multi", "sortedmulti"]:
            if descriptor.startswith(func + "("):
                return {
                    "type"   : func,
                    "inner"  : descriptor[len(func)+1:-1],
                    "raw"    : descriptor,
                }
        return {"type": "unknown", "raw": descriptor}

# ---- UTXOSelector  (kind C, v10.18 lines 33597-33723) ----
class UTXOSelector:
    """
    Automatic UTXO selection algorithms.
    Branch and Bound (BnB) — Bitcoin Core's default.
    Knapsack — fallback algorithm.
    Largest First — simple, high fee.
    Smallest First — consolidation.
    """

    @staticmethod
    def branch_and_bound(utxos: list, target: int,
                          cost_per_input: int = 68) -> Optional[List]:
        """
        Branch and Bound coin selection (BIP 0000).
        Finds exact change-free solution when possible.
        Falls back to knapsack.
        """
        # Filter UTXOs that are large enough to be useful
        available = [u for u in utxos
                     if u.value > cost_per_input]
        available.sort(key=lambda u: u.value, reverse=True)

        best         = None
        best_waste   = float('inf')
        current_val  = 0
        current_sel  = []

        def _bnb(idx: int):
            nonlocal best, best_waste, current_val

            if abs(current_val - target) < 546:   # dust threshold
                waste = abs(current_val - target)
                if waste < best_waste:
                    best_waste = waste
                    best = current_sel[:]
                return

            if idx >= len(available):
                return

            remaining = sum(u.value for u in available[idx:])
            if current_val + remaining < target:
                return

            # Include branch
            current_sel.append(available[idx])
            current_val += available[idx].value
            _bnb(idx + 1)
            current_sel.pop()
            current_val -= available[idx].value

            # Exclude branch
            _bnb(idx + 1)

        try:
            _bnb(0)
        except RecursionError:
            pass

        if best is not None:
            return best

        return UTXOSelector.knapsack(utxos, target, cost_per_input)

    @staticmethod
    def knapsack(utxos: list, target: int,
                 cost_per_input: int = 68) -> Optional[List]:
        """Greedy knapsack coin selection"""
        available = sorted(utxos, key=lambda u: u.value, reverse=True)
        selected  = []
        total     = 0

        for utxo in available:
            if total >= target:
                break
            selected.append(utxo)
            total += utxo.value

        return selected if total >= target else None

    @staticmethod
    def smallest_first(utxos: list, target: int) -> Optional[List]:
        """Select smallest UTXOs first (UTXO consolidation)"""
        available = sorted(utxos, key=lambda u: u.value)
        selected  = []
        total     = 0
        for utxo in available:
            selected.append(utxo)
            total += utxo.value
            if total >= target:
                return selected
        return None

    @staticmethod
    def largest_first(utxos: list, target: int) -> Optional[List]:
        """Select largest UTXOs first (minimal inputs)"""
        available = sorted(utxos, key=lambda u: u.value, reverse=True)
        selected  = []
        total     = 0
        for utxo in available:
            selected.append(utxo)
            total += utxo.value
            if total >= target:
                return selected
        return None

    @staticmethod
    def privacy_optimized(utxos: list, target: int) -> Optional[List]:
        """
        Privacy-optimized selection.
        Avoids mixing UTXOs from different addresses when possible.
        Groups UTXOs by address, prefers single-address spending.
        """
        # Group by address
        by_addr: Dict[str, list] = {}
        for u in utxos:
            by_addr.setdefault(u.address, []).append(u)

        # Try to find single-address solution first
        for addr, addr_utxos in by_addr.items():
            total = sum(u.value for u in addr_utxos)
            if total >= target:
                sel = UTXOSelector.knapsack(addr_utxos, target)
                if sel: return sel

        # Fall back to knapsack across all UTXOs
        return UTXOSelector.knapsack(utxos, target)

# ---- AddressBookSimple  (kind C, v10.18 lines 33726-33848) ----
class AddressBookSimple:
    """
    Persistent address labels and contact management.
    Labels persist to disk as JSON.
    """

    def __init__(self):
        self._labels  : Dict[str, dict] = {}
        self._lock    = threading.Lock()

    def set_label(self, address: str, label: str,
                   category: str = "personal", note: str = ""):
        with self._lock:
            self._labels[address] = {
                "label"    : label,
                "category" : category,
                "note"     : note,
                "added"    : time.time(),
            }

    def get_label(self, address: str) -> Optional[str]:
        entry = self._labels.get(address)
        return entry["label"] if entry else None

    def get_entry(self, address: str) -> Optional[dict]:
        return self._labels.get(address)

    def remove(self, address: str):
        with self._lock:
            self._labels.pop(address, None)

    def search(self, query: str) -> List[dict]:
        results = []
        q = query.lower()
        for addr, entry in self._labels.items():
            if (q in addr.lower() or
                q in entry.get("label","").lower() or
                q in entry.get("note","").lower()):
                results.append({"address": addr, **entry})
        return results

    def by_category(self, category: str) -> List[dict]:
        return [{"address": a, **e}
                for a, e in self._labels.items()
                if e.get("category") == category]

    def categories(self) -> List[str]:
        return list(set(e.get("category","") for e in self._labels.values()))

    def export(self) -> dict:
        return dict(self._labels)

    def import_data(self, data: dict):
        with self._lock:
            self._labels.update(data)

    def add(self, address: str, label: str,
             category: str = "personal",
             note: str = "",
             tags: list = None) -> bool:
        """Add or update an address entry (compatibility method)"""
        self.set_label(address, label)
        if address not in self._entries:
            from dataclasses import field as _field
            import time as _time
            self._entries[address] = type('Entry', (), {
                'address': address, 'label': label,
                'category': category, 'note': note,
                'tags': tags or [], 'last_used': 0.0,
                'use_count': 0, 'is_mine': False,
                'created_at': _time.time()
            })()
        return True

    def get(self, address: str):
        """Get address entry (compatibility method)"""
        return self._entries.get(address)

    def mark_used(self, address: str):
        """Mark address as recently used"""
        entry = self._entries.get(address)
        if entry:
            import time as _time
            entry.last_used = _time.time()
            entry.use_count = getattr(entry, 'use_count', 0) + 1

    def add_tx_note(self, txid: str, note: str,
                     amount: float = 0.0, direction: str = "received",
                     tags: list = None):
        """Record a transaction note"""
        self._tx_notes = getattr(self, '_tx_notes', {})
        self._tx_notes[txid] = {
            'txid': txid, 'note': note,
            'amount_nbl': amount, 'direction': direction,
            'tags': tags or []
        }

    def get_tx_note(self, txid: str):
        """Get a transaction note"""
        self._tx_notes = getattr(self, '_tx_notes', {})
        return self._tx_notes.get(txid)

    def total(self) -> int:
        """Return total number of entries"""
        return len(self._entries)

    def save(self) -> bool:
        """Save to disk (stub)"""
        return True

    def load(self) -> bool:
        """Load from disk (stub)"""
        return False

    def stats(self) -> dict:
        """Return statistics"""
        return {
            "total"    : len(self._entries),
            "tx_notes" : len(getattr(self, '_tx_notes', {})),
        }

    def __len__(self) -> int:
        return len(self._labels)

# ---- MultiAccountWalletAdv  (kind C, v10.18 lines 33889-34072) ----
class MultiAccountWalletAdv:
    """
    BIP44/49/84/86 multi-account HD wallet.
    Supports unlimited accounts, multiple address types,
    watch-only mode, coin control, and address book.
    """

    def __init__(self, mnemonic: str = None,
                 passphrase: str = "",
                 seed: bytes = None):
        if seed is None:
            if mnemonic is None:
                mnemonic = BIP39.generate_mnemonic(12)
            self.mnemonic  = mnemonic
            seed           = BIP39.mnemonic_to_seed(mnemonic, passphrase)
        else:
            self.mnemonic  = None

        self.master       = ExtendedKey.from_seed(seed)
        self._accounts    : Dict[int, WalletAccount] = {}
        self.address_book = AddressBook()
        self.coin_control = CoinControl()
        self._lock        = threading.RLock()

        # Create default account 0
        self._create_account(0, AddressType.P2PKH)

    def _account_path(self, account: int,
                       addr_type: AddressType) -> str:
        purposes = {
            AddressType.P2PKH : 44,
            AddressType.P2SH  : 49,
            AddressType.P2WPKH: 84,
            AddressType.P2TR  : 86,
        }
        purpose = purposes.get(addr_type, 44)
        return f"m/{purpose}'/2025'/{account}'"

    def _create_account(self, index: int,
                         addr_type: AddressType = AddressType.P2PKH,
                         label: str = "") -> WalletAccount:
        path = self._account_path(index, addr_type)
        acct_key = self.master.derive_path(path)

        # Derive first GAP_LIMIT external addresses
        ext_keys = [acct_key.derive_path(f"0/{i}") for i in range(GAP_LIMIT)]
        int_keys = [acct_key.derive_path(f"1/{i}") for i in range(GAP_LIMIT)]

        acct = WalletAccount(
            account_index = index,
            addr_type     = addr_type,
            xpub          = acct_key.to_xpub(),
            external_keys = ext_keys,
            internal_keys = int_keys,
            label         = label or f"Account {index}",
        )
        with self._lock:
            self._accounts[index] = acct
        return acct

    def create_account(self, label: str = "",
                        addr_type: AddressType = AddressType.P2PKH) -> WalletAccount:
        idx = max(self._accounts.keys(), default=-1) + 1
        return self._create_account(idx, addr_type, label)

    def get_account(self, index: int = 0) -> Optional[WalletAccount]:
        return self._accounts.get(index)

    def all_accounts(self) -> List[WalletAccount]:
        return list(self._accounts.values())

    def get_receive_address(self, account: int = 0) -> str:
        acct = self.get_account(account)
        return acct.get_receive_address() if acct else ""

    def get_change_address(self, account: int = 0) -> str:
        acct = self.get_account(account)
        return acct.get_change_address() if acct else ""

    def all_addresses(self) -> List[str]:
        result = []
        for acct in self._accounts.values():
            result.extend(acct.all_addresses())
        return result

    def total_balance(self, utxo_set: 'UTXOSet') -> int:
        return sum(utxo_set.balance(addr) for addr in self.all_addresses())

    def build_transaction(self, to_address: str, amount_nbl: float,
                           utxo_set: 'UTXOSet',
                           account: int = 0,
                           fee_rate: int = 2,
                           selection: str = "bnb") -> Optional['Transaction']:
        """
        Build and sign transaction.
        selection: 'bnb', 'knapsack', 'largest', 'smallest', 'privacy'
        """
        amount = int(amount_nbl * 10**DECIMALS)
        acct   = self.get_account(account)
        if not acct: return None

        # Collect available UTXOs
        all_utxos = []
        for addr in acct.all_addresses():
            all_utxos.extend(utxo_set.get_by_address(addr))

        if not all_utxos: return None

        # Estimate fee: ~148 bytes per input + 34 per output + 10 overhead
        estimated_fee = max(MIN_TX_FEE, fee_rate * (148 + 34 * 2 + 10))
        target        = amount + estimated_fee

        # Select UTXOs
        selectors = {
            "bnb"      : UTXOSelector.branch_and_bound,
            "knapsack" : UTXOSelector.knapsack,
            "largest"  : UTXOSelector.largest_first,
            "smallest" : UTXOSelector.smallest_first,
            "privacy"  : UTXOSelector.privacy_optimized,
        }
        selector  = selectors.get(selection, UTXOSelector.knapsack)
        selected  = selector(all_utxos, target)
        if selected is None: return None

        total_in = sum(u.value for u in selected)
        change   = total_in - amount - estimated_fee

        # Build inputs
        inputs = []
        for u in selected:
            seq = 0xFFFFFFFD if self.coin_control._rbf else 0xFFFFFFFF
            inputs.append(TxInput(OutPoint(u.txid, u.index), b'', sequence=seq))

        # Build outputs
        outputs = [TxOutput(amount, Script.p2pkh_locking_from_address(to_address))]
        if change > DUST_THRESHOLD:
            change_addr = self.coin_control._change_addr or acct.get_change_address()
            outputs.append(TxOutput(change, Script.p2pkh_locking_from_address(change_addr)))

        tx = Transaction(inputs=inputs, outputs=outputs)

        # Sign all inputs
        key_map = {}
        for k in acct.external_keys + acct.internal_keys:
            key_map[k.address] = k

        for i, (inp, utxo) in enumerate(zip(inputs, selected)):
            addr = utxo.address
            key  = key_map.get(addr)
            if key and key.is_private:
                sig_hash = tx.signature_hash(i, utxo.script_pubkey)
                sig      = ECDSA.sign(sig_hash, key.private_key_int)
                pubkey   = key.public_key_bytes
                inp.script_sig = (bytes([len(sig)+1]) + sig + bytes([SIGHASH_ALL]) +
                                  bytes([len(pubkey)]) + pubkey)

        return tx

    def export_descriptor(self, account: int = 0,
                           chain: int = 0) -> str:
        """Export wallet as output descriptor"""
        acct = self.get_account(account)
        if not acct: return ""
        return OutputDescriptor.checksum(
            OutputDescriptor.from_xpub(acct.xpub, f"{chain}/*", acct.addr_type))

    def backup(self) -> dict:
        """Export wallet backup data"""
        return {
            "mnemonic"  : self.mnemonic,
            "accounts"  : [a.to_dict() for a in self.all_accounts()],
            "labels"    : self.address_book.export(),
            "version"   : 1,
            "chain"     : CHAIN_NAME,
            "created"   : time.time(),
        }

    def stats(self) -> dict:
        return {
            "accounts"  : len(self._accounts),
            "addresses" : len(self.all_addresses()),
            "labels"    : len(self.address_book),
            "has_mnemonic": self.mnemonic is not None,
        }

# ---- BIP85Wallet  (kind C, v10.18 lines 34075-34127) ----
class BIP85Wallet:
    """
    BIP85: Deterministic Entropy from BIP32 Keychains.
    Derive child seeds from master — all from one mnemonic.
    Use cases: separate wallets, app-specific keys, backups.
    """

    APP_MNEMONIC = 39     # Derive BIP39 mnemonic
    APP_WIF      = 2      # Derive WIF key
    APP_XPRV     = 32     # Derive xprv
    APP_HEX      = 128169 # Derive hex entropy

    @staticmethod
    def derive_entropy(master: ExtendedKey, app: int,
                        params: List[int]) -> bytes:
        """
        Derive entropy for application `app` with `params`.
        Path: m/83696968'/app'/params...
        """
        path = f"m/83696968'/{app}'"
        for p in params:
            path += f"/{p}'"
        child = master.derive_path(path)

        # HMAC-SHA512 of child private key
        I = hmac.new(b"bip-entropy-from-k",
                      child.key, hashlib.sha512).digest()
        return I

    @classmethod
    def derive_mnemonic(cls, master: ExtendedKey,
                         word_count: int = 12,
                         index: int = 0) -> str:
        """Derive child BIP39 mnemonic"""
        entropy_bits = {12: 16, 15: 20, 18: 24, 21: 28, 24: 32}
        n_bytes = entropy_bits.get(word_count, 16)
        entropy = cls.derive_entropy(master, cls.APP_MNEMONIC,
                                      [2048, word_count, index])[:n_bytes]
        return BIP39.generate.__func__(BIP39, n_bytes * 8) if True else "fallback"

    @classmethod
    def derive_wif(cls, master: ExtendedKey, index: int = 0) -> str:
        """Derive child WIF private key"""
        entropy = cls.derive_entropy(master, cls.APP_WIF, [index])[:32]
        return base58check_encode(entropy + b'\x01', 0x80)

    @classmethod
    def derive_hex(cls, master: ExtendedKey,
                    num_bytes: int = 32, index: int = 0) -> str:
        """Derive hex entropy string"""
        entropy = cls.derive_entropy(master, cls.APP_HEX,
                                      [num_bytes, index])[:num_bytes]
        return entropy.hex()

# ---- BIP85App  (kind C, v10.18 lines 34150-34160) ----
class BIP85App:
    ENTROPY       = 0       # raw entropy
    WIF           = 2       # WIF private key
    XPRV          = 32      # extended private key
    HEX           = 128169  # hex entropy
    MNEMONIC_12   = 39      # BIP39 12-word mnemonic
    MNEMONIC_18   = 39      # BIP39 18-word mnemonic
    MNEMONIC_24   = 39      # BIP39 24-word mnemonic
    PWD_BASE64    = 707764  # base64 password
    PWD_BASE85    = 707785  # base85 password
    DICE_ROLL     = 89101   # dice rolling

# ---- SyncStateV3  (kind C, v10.18 lines 34421-34426) ----
class SyncStateV3(Enum):
    IDLE               = "idle"
    HEADERS_SYNC       = "headers_sync"
    BLOCK_DOWNLOAD     = "block_download"
    SYNCED             = "synced"
    REORG              = "reorg"

# ---- BlockRequest  (kind C, v10.18 lines 34442-34452) ----
@dataclass
class BlockRequest:
    height   : int
    hash     : str
    peer_id  : str
    requested: float = field(default_factory=time.time)
    retries  : int = 0

    @property
    def is_stale(self) -> bool:
        return time.time() - self.requested > STALE_BLOCK_TIMEOUT

# ---- PeerSyncStateAdv  (kind C, v10.18 lines 34455-34470) ----
@dataclass
class PeerSyncStateAdv:
    peer_id        : str
    known_height   : int = 0
    known_hash     : str = ""
    in_flight      : int = 0
    max_in_flight  : int = MAX_BLOCKS_PER_PEER
    last_headers   : float = 0.0
    last_block     : float = 0.0
    stall_count    : int = 0
    bytes_received : int = 0
    is_preferred   : bool = False

    @property
    def can_accept_more(self) -> bool:
        return self.in_flight < self.max_in_flight

# ---- ReorgHandlerAdv  (kind C, v10.18 lines 34473-34554) ----
class ReorgHandlerAdv:
    """
    Handles blockchain reorganizations.
    Detects forks, finds common ancestor, rolls back and re-applies.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc   = blockchain
        self._log : List[dict] = []

    def find_common_ancestor(self, fork_chain: List['Block']) -> Optional[int]:
        """
        Find common ancestor between main chain and fork.
        Returns height of last common block, or None if no ancestor found.
        """
        for fork_block in reversed(fork_chain):
            for i, main_block in enumerate(self.bc._chain):
                if main_block.hash == fork_block.hash:
                    return main_block.height
        return None

    def execute_reorg(self, new_chain: List['Block'],
                       common_height: int) -> Tuple[bool, str]:
        """
        Execute a chain reorganization.
        1. Disconnect blocks from tip to common ancestor.
        2. Connect new fork blocks.
        3. Update UTXO set, mempool.
        Returns (success, reason).
        """
        if not new_chain:
            return False, "Empty new chain"

        new_work  = len(new_chain)
        old_work  = self.bc.height - common_height

        if new_work <= old_work:
            return False, f"Fork has less work: {new_work} <= {old_work}"

        # Validate all blocks in new chain
        for blk in new_chain:
            if not self._validate_block_header(blk):
                return False, f"Invalid block at height {blk.height}"

        # Log reorg event
        self._log.append({
            "time"          : time.time(),
            "common_height" : common_height,
            "old_tip_height": self.bc.height,
            "new_tip_height": new_chain[-1].height,
            "disconnected"  : old_work,
            "connected"     : new_work,
        })

        # Disconnect old blocks (add txs back to mempool)
        disconnected_txs = []
        while self.bc.height > common_height:
            tip_block = self.bc.tip
            for tx in tip_block.transactions[1:]:  # skip coinbase
                disconnected_txs.append(tx)
            self.bc._chain.pop()

        # Reconnect new blocks
        for blk in new_chain:
            ok, reason = self.bc.connect_block(blk)
            if not ok:
                return False, f"Failed to connect block {blk.height}: {reason}"

        # Re-add disconnected txs to mempool
        for tx in disconnected_txs:
            self.bc.mempool.submit(tx)

        return True, f"Reorg: -{old_work}/+{new_work} at height {common_height}"

    def _validate_block_header(self, blk: 'Block') -> bool:
        try:
            return blk.header.meets_target()
        except Exception:
            return False

    def reorg_history(self) -> List[dict]:
        return list(self._log)

# ---- HeadersFirstSyncLegacy  (kind C, v10.18 lines 34557-34743) ----
class HeadersFirstSyncLegacy:
    """[v10.17] OLD implementation kept ONLY for old stand-alone callers (their API differs from the live HeadersFirstSync)."""
    """
    Bitcoin-style headers-first synchronization.
    Phase 1: Download all headers (fast, ~50MB for 800k blocks).
    Phase 2: Download blocks in parallel using multiple peers.
    Validates PoW for all headers before downloading blocks.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc            = blockchain
        self._state        = SyncState.IDLE
        self._headers      : List[dict] = []
        self._peer_states  : Dict[str, PeerSyncStateAdv] = {}
        self._in_flight    : Dict[str, BlockRequest]  = {}
        self._pending_blocks: Dict[int, 'Block'] = {}
        self._lock         = threading.RLock()
        self._block_queue  = queue.PriorityQueue()
        self._reorg_handler = ReorgHandler(blockchain)
        self._callbacks    : Dict[str, Callable] = {}
        self._progress     = SyncProgress()

    def register_peer(self, peer_id: str, height: int, tip_hash: str):
        """Register a new peer for sync"""
        with self._lock:
            self._peer_states[peer_id] = PeerSyncStateAdv(
                peer_id      = peer_id,
                known_height = height,
                known_hash   = tip_hash,
            )
            # Mark highest peer as preferred
            best = max(self._peer_states.values(),
                       key=lambda p: p.known_height)
            for ps in self._peer_states.values():
                ps.is_preferred = (ps.peer_id == best.peer_id)

    def remove_peer(self, peer_id: str):
        """Remove peer and reschedule its in-flight requests"""
        with self._lock:
            self._peer_states.pop(peer_id, None)
            # Reschedule stale requests
            to_reschedule = [r for r in self._in_flight.values()
                             if r.peer_id == peer_id]
            for req in to_reschedule:
                del self._in_flight[req.hash]

    def best_known_height(self) -> int:
        if not self._peer_states: return 0
        return max(ps.known_height for ps in self._peer_states.values())

    def is_ibd(self) -> bool:
        """Are we in Initial Block Download?"""
        if not self.bc._chain or len(self.bc._chain) == 0:
            return True
        tip_time = self.bc.tip.header.timestamp
        return (time.time() - tip_time) > IBD_THRESHOLD

    def process_headers(self, peer_id: str,
                         headers: List[dict]) -> Tuple[int, str]:
        """
        Process received headers from peer.
        Validates chain connection and PoW.
        Returns (accepted_count, status).
        """
        if not headers:
            return 0, "empty"

        accepted = 0
        with self._lock:
            for hdr in headers:
                height = hdr.get("height", 0)
                block_hash = hdr.get("hash", "")

                # Checkpoint validation
                if not verify_checkpoint(height, block_hash):
                    return accepted, f"checkpoint_fail at {height}"

                self._headers.append(hdr)
                accepted += 1

            ps = self._peer_states.get(peer_id)
            if ps:
                ps.last_headers = time.time()
                ps.known_height = max(ps.known_height,
                                      headers[-1].get("height", 0))

        self._progress.headers_synced = len(self._headers)
        self._state = SyncState.HEADERS_SYNC
        return accepted, "ok"

    def process_block(self, peer_id: str,
                       block: 'Block') -> Tuple[bool, str]:
        """
        Process a received block.
        Queues in-order blocks for chain connection.
        """
        with self._lock:
            # Remove from in-flight
            req = self._in_flight.pop(block.hash, None)
            if req:
                ps = self._peer_states.get(peer_id)
                if ps:
                    ps.in_flight     -= 1
                    ps.last_block     = time.time()
                    ps.bytes_received += block.byte_size()

            # Buffer out-of-order blocks
            self._pending_blocks[block.height] = block

            # Connect all consecutive blocks we have
            connected = 0
            next_height = self.bc.height + 1
            while next_height in self._pending_blocks:
                blk = self._pending_blocks.pop(next_height)

                # Check for reorg
                if (self.bc._chain and
                    blk.header.prev_hash != self.bc.tip.hash):
                    # Fork detected
                    ok, reason = self._reorg_handler.execute_reorg(
                        [blk], self.bc.height - 1)
                    if not ok:
                        return False, f"Reorg failed: {reason}"
                else:
                    ok, reason = self.bc.connect_block(blk)
                    if not ok:
                        return False, reason

                connected    += 1
                next_height  += 1
                self._progress.blocks_synced += 1

        if self.bc.height >= self.best_known_height():
            self._state = SyncState.SYNCED
            self._progress.complete = True

        return True, f"connected {connected} blocks"

    def next_download_requests(self, peer_id: str,
                                n: int = 4) -> List[str]:
        """
        Get next block hashes to request from peer.
        Returns up to n block hashes.
        """
        ps = self._peer_states.get(peer_id)
        if not ps or not ps.can_accept_more:
            return []

        requests = []
        with self._lock:
            for hdr in self._headers:
                if len(requests) >= n: break
                h     = hdr.get("hash","")
                height= hdr.get("height",0)
                if (height > self.bc.height and
                    h not in self._in_flight and
                    height not in self._pending_blocks):
                    self._in_flight[h] = BlockRequest(height, h, peer_id)
                    requests.append(h)
                    ps.in_flight += 1

        return requests

    def check_stall(self) -> List[str]:
        """Check for stalled requests and return their hashes"""
        stalled = []
        with self._lock:
            for h, req in list(self._in_flight.items()):
                if req.is_stale:
                    del self._in_flight[h]
                    stalled.append(h)
        return stalled

    def progress(self) -> dict:
        best = self.best_known_height()
        return {
            "state"          : self._state.value,
            "our_height"     : self.bc.height,
            "best_height"    : best,
            "headers_synced" : len(self._headers),
            "blocks_synced"  : self._progress.blocks_synced,
            "in_flight"      : len(self._in_flight),
            "pending"        : len(self._pending_blocks),
            "pct_complete"   : f"{self.bc.height/max(1,best)*100:.1f}%",
            "is_ibd"         : self.is_ibd(),
            "peers"          : len(self._peer_states),
        }

# ---- SyncProgressAdv  (kind C, v10.18 lines 34745-34754) ----
@dataclass
class SyncProgressAdv:
    headers_synced : int   = 0
    blocks_synced  : int   = 0
    complete       : bool  = False
    start_time     : float = field(default_factory=time.time)

    @property
    def elapsed(self) -> float:
        return time.time() - self.start_time

# ---- ParallelBlockFetcher  (kind C, v10.18 lines 34757-34813) ----
class ParallelBlockFetcher:
    """
    Downloads blocks in parallel from multiple peers.
    Distributes load across peers, retries on timeout.
    Target: download blocks at maximum network speed.
    """

    def __init__(self, sync: HeadersFirstSync, max_parallel: int = 8):
        self.sync        = sync
        self.max_parallel= max_parallel
        self._workers    : List[threading.Thread] = []
        self._running    = False
        self._stats      = FetcherStats()

    def start(self, send_getblocks_func: Callable):
        """Start parallel download"""
        self._running = True
        self._send    = send_getblocks_func

        for i in range(self.max_parallel):
            t = threading.Thread(
                target=self._worker_loop,
                args=(i,),
                daemon=True,
                name=f"BlockFetcher-{i}")
            t.start()
            self._workers.append(t)

    def _worker_loop(self, worker_id: int):
        while self._running:
            # Check for stalled requests
            stalled = self.sync.check_stall()
            if stalled:
                self._stats.stalls += len(stalled)

            # Request blocks from best peer
            for peer_id, ps in self.sync._peer_states.items():
                if ps.can_accept_more:
                    hashes = self.sync.next_download_requests(peer_id, 4)
                    if hashes and self._send:
                        try:
                            self._send(peer_id, hashes)
                            self._stats.requests += len(hashes)
                        except Exception:
                            self.sync.remove_peer(peer_id)

            time.sleep(0.1)

    def stop(self):
        self._running = False

    def stats(self) -> dict:
        return {
            "requests"  : self._stats.requests,
            "stalls"    : self._stats.stalls,
            "workers"   : len(self._workers),
        }

# ---- FetcherStats  (kind C, v10.18 lines 34815-34818) ----
@dataclass
class FetcherStats:
    requests : int = 0
    stalls   : int = 0

# ---- SyncAntiDoS  (kind C, v10.18 lines 34821-34878) ----
class SyncAntiDoS:
    """
    Anti-DoS measures for sync process.
    Bans peers who send invalid data.
    Rate-limits block requests per peer.
    """

    def __init__(self):
        self._misbehaving : Dict[str, int]   = {}   # peer_id -> score
        self._banned      : Dict[str, float] = {}   # peer_id -> ban_expiry
        self._rates       : Dict[str, List[float]] = {}
        self._lock        = threading.Lock()
        self.ban_threshold = 100
        self.ban_duration  = 86400   # 24 hours

    def misbehaving(self, peer_id: str, score: int, reason: str = ""):
        """Add misbehavior score to peer"""
        with self._lock:
            self._misbehaving[peer_id] = self._misbehaving.get(peer_id, 0) + score
            if self._misbehaving[peer_id] >= self.ban_threshold:
                self._banned[peer_id] = time.time() + self.ban_duration

    def is_banned(self, peer_id: str) -> bool:
        expiry = self._banned.get(peer_id, 0)
        if time.time() > expiry:
            self._banned.pop(peer_id, None)
            return False
        return True

    def ban(self, peer_id: str, duration: float = None):
        dur = duration or self.ban_duration
        with self._lock:
            self._banned[peer_id] = time.time() + dur

    def unban(self, peer_id: str):
        with self._lock:
            self._banned.pop(peer_id, None)
            self._misbehaving.pop(peer_id, None)

    def check_rate(self, peer_id: str, action: str,
                    max_per_sec: float = 10.0) -> bool:
        """Check if peer is within rate limit for action"""
        key = f"{peer_id}:{action}"
        now = time.time()
        with self._lock:
            times = [t for t in self._rates.get(key,[]) if now-t < 1.0]
            if len(times) >= max_per_sec:
                self.misbehaving(peer_id, 5, f"rate_limit:{action}")
                return False
            times.append(now)
            self._rates[key] = times
        return True

    def stats(self) -> dict:
        return {
            "misbehaving" : len(self._misbehaving),
            "banned"      : len(self._banned),
        }

# ---- OrphanBlockPool  (kind C, v10.18 lines 34881-34918) ----
class OrphanBlockPool:
    """
    Pool for orphan blocks (received before parent).
    When a block arrives whose parent we don't have,
    it's stored here until the parent arrives.
    """

    MAX_ORPHANS = 750

    def __init__(self):
        self._pool : Dict[str, 'Block'] = {}   # hash -> block
        self._lock = threading.Lock()

    def add(self, block: 'Block'):
        with self._lock:
            if len(self._pool) >= self.MAX_ORPHANS:
                # Evict oldest
                oldest = min(self._pool.values(),
                             key=lambda b: b.header.timestamp)
                del self._pool[oldest.hash]
            self._pool[block.hash] = block

    def get_children(self, parent_hash: str) -> List['Block']:
        """Get orphans whose parent is parent_hash"""
        with self._lock:
            return [b for b in self._pool.values()
                    if b.header.prev_hash == parent_hash]

    def remove(self, block_hash: str):
        with self._lock:
            self._pool.pop(block_hash, None)

    def __len__(self) -> int:
        return len(self._pool)

    def stats(self) -> dict:
        return {"orphans": len(self._pool),
                "max"    : self.MAX_ORPHANS}

# ---- ChainManager  (kind C, v10.18 lines 34921-34988) ----
class ChainManager:
    """
    Top-level chain management:
    - Coordinates sync, reorg, orphan handling
    - Manages chainwork and best chain selection
    - Provides chain state to all other modules
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc       = blockchain
        self.sync     = HeadersFirstSyncLegacy(blockchain)
        self.orphans  = OrphanBlockPool()
        self.antidos  = SyncAntiDoS()
        self._lock    = threading.RLock()
        self._tip_callbacks: List[Callable] = []

    def on_new_tip(self, callback: Callable):
        """Register callback for new chain tip"""
        self._tip_callbacks.append(callback)

    def receive_block(self, peer_id: str,
                       block: 'Block') -> Tuple[bool, str]:
        """Main entry point for new blocks"""
        if self.antidos.is_banned(peer_id):
            return False, "peer banned"

        if not self.antidos.check_rate(peer_id, "block"):
            return False, "rate limited"

        # Check if we need parent first
        if (block.header.prev_hash != self.bc.tip.hash and
            block.height > self.bc.height + 1):
            self.orphans.add(block)
            return True, "orphaned — queued"

        ok, reason = self.sync.process_block(peer_id, block)

        if ok:
            # Check for orphans we can now connect
            children = self.orphans.get_children(block.hash)
            for child in children:
                self.orphans.remove(child.hash)
                self.receive_block(peer_id, child)

            # Fire tip callbacks
            for cb in self._tip_callbacks:
                try: cb(block)
                except Exception: pass

        else:
            self.antidos.misbehaving(peer_id, 20, reason)

        return ok, reason

    def receive_headers(self, peer_id: str,
                         headers: List[dict]) -> Tuple[int, str]:
        if self.antidos.is_banned(peer_id):
            return 0, "banned"
        return self.sync.process_headers(peer_id, headers)

    def chain_status(self) -> dict:
        return {
            "height"   : self.bc.height,
            "tip"      : self.bc.tip.hash,
            "sync"     : self.sync.progress(),
            "orphans"  : self.orphans.stats(),
            "antidos"  : self.antidos.stats(),
        }

# ---- PeerScoreAdv  (kind C, v10.18 lines 35739-35783) ----
@dataclass
class PeerScoreAdv:
    """
    Misbehavior scoring for a peer (like Bitcoin Core).
    Score 0-100: at 100 → ban for 24 hours.
    """
    peer_id      : str
    score        : int   = 0
    bans         : int   = 0
    last_ban     : float = 0.0
    services     : int   = 0
    version      : int   = 0
    user_agent   : str   = ""
    connected_at : float = field(default_factory=time.time)
    last_seen    : float = field(default_factory=time.time)
    blocks_sent  : int   = 0
    txs_relayed  : int   = 0
    latency_ms   : float = 0.0

    def punish(self, points: int, reason: str = "") -> bool:
        """Add misbehavior score. Returns True if should be banned."""
        self.score = min(100, self.score + points)
        if self.score >= 100:
            self.bans    += 1
            self.last_ban = time.time()
            return True
        return False

    def reward(self, points: int = 1):
        """Good behavior reduces score"""
        self.score = max(0, self.score - points)

    def to_dict(self) -> dict:
        return {
            "peer_id"    : self.peer_id,
            "score"      : self.score,
            "bans"       : self.bans,
            "services"   : self.services,
            "version"    : self.version,
            "user_agent" : self.user_agent,
            "latency_ms" : round(self.latency_ms, 1),
            "blocks_sent": self.blocks_sent,
            "txs_relayed": self.txs_relayed,
            "uptime_secs": round(time.time() - self.connected_at),
        }

# ---- CompactBlockAdv  (kind C, v10.18 lines 35786-35885) ----
class CompactBlockAdv:
    """
    BIP152 Compact Block relay.
    Sends block header + short transaction IDs.
    Receiving node reconstructs block from mempool (fast) or
    requests missing transactions (slow mode).
    Reduces block propagation time significantly.
    """

    SHORT_ID_LENGTH = 6   # bytes

    def __init__(self, block: 'Block', nonce: int = None):
        self.block   = block
        self.nonce   = nonce or secrets.randbelow(2**64)
        self._key    = self._compute_key()
        self.short_ids = self._compute_short_ids()
        self.prefilled : List[Tuple[int, 'Transaction']] = []
        # Always prefill coinbase
        if block.transactions:
            self.prefilled = [(0, block.transactions[0])]

    def _compute_key(self) -> bytes:
        """SipHash key derived from header hash + nonce"""
        header_hash = bytes.fromhex(self.block.hash)
        nonce_bytes = self.nonce.to_bytes(8, 'little')
        return hashlib.sha256(header_hash + nonce_bytes).digest()[:16]

    def _siphash_short(self, txid: str) -> bytes:
        """Compute 6-byte short txid"""
        tx_bytes = bytes.fromhex(txid)[::-1]
        h = hashlib.sha256(self._key + tx_bytes).digest()
        return h[:self.SHORT_ID_LENGTH]

    def _compute_short_ids(self) -> List[bytes]:
        """Compute short IDs for all non-prefilled transactions"""
        prefill_indices = {idx for idx, _ in self.prefilled}
        ids = []
        for i, tx in enumerate(self.block.transactions):
            if i not in prefill_indices:
                ids.append(self._siphash_short(tx.txid))
        return ids

    def reconstruct(self, mempool_txs: Dict[str, 'Transaction']) -> Optional['Block']:
        """
        Reconstruct block using mempool transactions.
        Returns Block if successful, None if transactions missing.
        """
        txs = [None] * len(self.block.transactions)

        # Place prefilled transactions
        for idx, tx in self.prefilled:
            if idx < len(txs):
                txs[idx] = tx

        # Match short IDs to mempool
        mempool_list = list(mempool_txs.values())
        short_idx    = 0
        for i in range(len(txs)):
            if txs[i] is not None:
                continue
            if short_idx >= len(self.short_ids):
                break
            short_id = self.short_ids[short_idx]
            short_idx += 1
            # Find matching tx in mempool
            for tx in mempool_list:
                if self._siphash_short(tx.txid) == short_id:
                    txs[i] = tx
                    break

        if any(t is None for t in txs):
            return None

        return Block(header=self.block.header, transactions=txs)

    def missing_tx_indices(self, mempool_txs: Dict[str, 'Transaction']) -> List[int]:
        """Return indices of transactions not found in mempool"""
        missing      = []
        short_map    = {self._siphash_short(tx.txid): tx for tx in mempool_txs.values()}
        prefill_idxs = {idx for idx, _ in self.prefilled}
        short_idx    = 0
        offset       = 0
        for i in range(len(self.block.transactions)):
            if i in prefill_idxs:
                continue
            if short_idx < len(self.short_ids):
                if self.short_ids[short_idx] not in short_map:
                    missing.append(i)
                short_idx += 1
        return missing

    def to_dict(self) -> dict:
        return {
            "block_hash"   : self.block.hash,
            "height"       : self.block.height,
            "nonce"        : self.nonce,
            "short_ids"    : len(self.short_ids),
            "prefilled"    : len(self.prefilled),
            "total_txs"    : len(self.block.transactions),
        }

# ---- UTXOAgeBandAdv  (kind C, v10.18 lines 35979-35990) ----
@dataclass
class UTXOAgeBandAdv:
    """Classifies UTXOs by age (Bitcoin HODL wave style)"""
    label     : str
    min_blocks: int
    max_blocks: int
    count     : int = 0
    value_nbl : float = 0.0

    @property
    def pct_count(self) -> str:
        return f"{self.count} UTXOs"

# ---- AddressClusterer  (kind C, v10.18 lines 36004-36065) ----
class AddressClusterer:
    """
    Heuristic address clustering (common-input-ownership).
    Groups addresses likely controlled by same entity.
    Heuristic: all inputs to a tx share same owner.
    """

    def __init__(self):
        self._parent : Dict[str, str] = {}   # union-find
        self._lock   = threading.Lock()

    def _find(self, x: str) -> str:
        if x not in self._parent:
            self._parent[x] = x
        if self._parent[x] != x:
            self._parent[x] = self._find(self._parent[x])
        return self._parent[x]

    def _union(self, x: str, y: str):
        px, py = self._find(x), self._find(y)
        if px != py:
            self._parent[px] = py

    def process_transaction(self, tx: 'Transaction',
                              utxo: 'UTXOSet'):
        """Apply common-input heuristic to transaction"""
        if tx.is_coinbase or len(tx.inputs) < 2:
            return
        with self._lock:
            addrs = []
            for inp in tx.inputs:
                u = utxo.get(inp.outpoint.txid, inp.outpoint.index)
                if u and u.address:
                    addrs.append(u.address)
            for i in range(1, len(addrs)):
                self._union(addrs[0], addrs[i])

    def process_block(self, block: 'Block', utxo: 'UTXOSet'):
        for tx in block.transactions:
            self.process_transaction(tx, utxo)

    def get_cluster(self, address: str) -> str:
        """Get cluster ID (root address) for address"""
        with self._lock:
            return self._find(address)

    def cluster_members(self, address: str) -> List[str]:
        """Get all addresses in same cluster"""
        root = self.get_cluster(address)
        with self._lock:
            return [a for a, p in self._parent.items()
                    if self._find(a) == root]

    def cluster_count(self) -> int:
        roots = set(self._find(a) for a in self._parent)
        return len(roots)

    def stats(self) -> dict:
        return {
            "total_addresses" : len(self._parent),
            "clusters"        : self.cluster_count(),
        }

# ---- RichListAdv  (kind C, v10.18 lines 36068-36104) ----
class RichListAdv:
    """
    Top N wallets by balance.
    Updated on each new block.
    """

    def __init__(self, top_n: int = 100):
        self.top_n    = top_n
        self._entries : List[Tuple[str, int]] = []  # (address, balance)
        self._lock    = threading.Lock()

    def rebuild(self, utxo: 'UTXOSet'):
        """Rebuild rich list from UTXO set"""
        balances: Dict[str, int] = {}
        for u in utxo.all_utxos():
            if u.address:
                balances[u.address] = balances.get(u.address, 0) + u.value

        sorted_list = sorted(balances.items(), key=lambda x: x[1], reverse=True)
        with self._lock:
            self._entries = sorted_list[:self.top_n]

    def get(self) -> List[dict]:
        with self._lock:
            return [
                {
                    "rank"    : i + 1,
                    "address" : addr,
                    "balance" : bal / 10**DECIMALS,
                    "is_whale": bal / 10**DECIMALS >= WHALE_THRESHOLD_NBL,
                }
                for i, (addr, bal) in enumerate(self._entries)
            ]

    def whale_count(self) -> int:
        return sum(1 for _, bal in self._entries
                   if bal / 10**DECIMALS >= WHALE_THRESHOLD_NBL)

# ---- NetworkHealthMonitorAdv  (kind C, v10.18 lines 36183-36281) ----
class NetworkHealthMonitorAdv:
    """
    Monitors overall NEBULA network health:
    hashrate, mempool health, block time variance,
    orphan rate, peer diversity.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc           = blockchain
        self._hashrate_history: List[Tuple[float,float]] = []
        self._orphan_count: int = 0
        self._lock        = threading.Lock()

    def estimated_hashrate(self) -> float:
        """
        Estimate current network hashrate from recent blocks.
        hashrate = difficulty * 2^32 / block_time
        """
        chain = self.bc._chain
        if len(chain) < 2:
            return 0.0

        recent = chain[-min(144, len(chain)):]
        if len(recent) < 2:
            return 0.0

        time_span = recent[-1].header.timestamp - recent[0].header.timestamp
        if time_span <= 0:
            return 0.0

        total_work = sum(bits_to_target(b.header.bits) for b in recent)
        return total_work / max(1, time_span)

    def block_time_variance(self) -> dict:
        chain = self.bc._chain
        if len(chain) < 10:
            return {}

        times = [chain[i].header.timestamp - chain[i-1].header.timestamp
                 for i in range(1, min(144, len(chain)))]
        avg = sum(times) / len(times)
        variance = sum((t - avg)**2 for t in times) / len(times)
        import math
        return {
            "target_seconds" : TARGET_BLOCK_TIME,
            "actual_avg"     : round(avg, 1),
            "std_dev"        : round(math.sqrt(variance), 1),
            "min"            : min(times),
            "max"            : max(times),
            "samples"        : len(times),
        }

    def mempool_health(self) -> dict:
        mp = self.bc.mempool
        return {
            "size"       : mp.size(),
            "healthy"    : mp.size() < 5000,
            "congested"  : mp.size() > 10000,
        }

    def health_score(self) -> dict:
        bv    = self.block_time_variance()
        mph   = self.mempool_health()
        score = 100

        # Penalize for poor block times
        if bv:
            deviation = abs(bv.get("actual_avg", TARGET_BLOCK_TIME) - TARGET_BLOCK_TIME)
            score    -= min(30, int(deviation / 60))

        # Penalize for mempool congestion
        if mph["congested"]:
            score -= 20

        return {
            "score"          : max(0, score),
            "grade"          : "A" if score>=90 else "B" if score>=80 else "C" if score>=70 else "D",
            "block_times"    : bv,
            "mempool"        : mph,
            "hashrate"       : self.estimated_hashrate(),
        }

    def miner_revenue(self) -> dict:
        """Calculate miner revenue stats for recent blocks"""
        chain = self.bc._chain
        if not chain: return {}
        recent = chain[-144:]
        revenues = []
        for blk in recent:
            reward = mining_reward(blk.height)
            # simplified — no fee tracking here
            revenues.append(reward)
        total = sum(revenues)
        return {
            "blocks_analyzed" : len(revenues),
            "total_reward_nbl": total / 10**DECIMALS,
            "avg_per_block"   : (total / max(1,len(revenues))) / 10**DECIMALS,
            "annualized_nbl"  : total / 10**DECIMALS * (525600 / max(1,len(revenues))),
        }

# ---- TransactionGraph  (kind C, v10.18 lines 36284-36339) ----
class TransactionGraph:
    """
    Build and analyze transaction graphs.
    Tracks fund flows, detects mixing, peeling chains.
    """

    def __init__(self):
        self._edges   : List[Tuple[str,str,int]] = []  # (from_addr, to_addr, value)
        self._lock    = threading.Lock()

    def add_transaction(self, tx: 'Transaction', utxo: 'UTXOSet'):
        """Add transaction edges to graph"""
        if tx.is_coinbase: return
        with self._lock:
            in_addrs = []
            for inp in tx.inputs:
                u = utxo.get(inp.outpoint.txid, inp.outpoint.index)
                if u and u.address:
                    in_addrs.append(u.address)

            for out in tx.outputs:
                if out.address:
                    for from_addr in in_addrs:
                        self._edges.append((from_addr, out.address, out.value))

    def outgoing(self, address: str) -> List[Tuple[str,int]]:
        """Get outgoing flows from address"""
        return [(to, val) for fr, to, val in self._edges if fr == address]

    def incoming(self, address: str) -> List[Tuple[str,int]]:
        """Get incoming flows to address"""
        return [(fr, val) for fr, to, val in self._edges if to == address]

    def is_peeling_chain(self, address: str,
                          depth: int = 5) -> bool:
        """
        Detect peel chain pattern (common privacy technique).
        Each step: one output is large, one is small change.
        """
        current = address
        for _ in range(depth):
            outs = self.outgoing(current)
            if len(outs) != 2: return False
            # Check if one output is significantly larger (>90% of total)
            total = sum(v for _, v in outs)
            large = max(v for _, v in outs)
            if large / max(1, total) > 0.9:
                # Follow the large output
                current = next((a for a, v in outs if v == large), None)
                if not current: return False
            else:
                return False
        return True

    def stats(self) -> dict:
        return {"edges": len(self._edges)}

# ---- NEBULAAnalyticsEngine  (kind C, v10.18 lines 36342-36452) ----
class NEBULAAnalyticsEngine:
    """
    Central analytics engine combining all analytics components.
    Auto-updates on each new block.
    Provides dashboards, alerts, and API endpoints.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc         = blockchain
        self.clusterer  = AddressClusterer()
        self.rich_list  = RichList(100)
        self.fee_market = FeeMarketAnalytics()
        self.health     = NetworkHealthMonitor(blockchain)
        self.tx_graph   = TransactionGraph()
        self._cache     : dict = {}
        self._cache_time: float = 0
        self._lock      = threading.Lock()
        self._alerts    : List[dict] = []

    def on_new_block(self, block: 'Block'):
        """Called when a new block is added"""
        # Update all analytics
        self.clusterer.process_block(block, self.bc.utxo)
        self.fee_market.add_block(block, self.bc.utxo)
        for tx in block.transactions:
            self.tx_graph.add_transaction(tx, self.bc.utxo)

        # Rebuild rich list every 10 blocks
        if block.height % 10 == 0:
            self.rich_list.rebuild(self.bc.utxo)

        # Generate alerts
        self._check_alerts(block)
        self._cache_time = 0  # invalidate cache

    def _check_alerts(self, block: 'Block'):
        """Generate alerts for large transactions, whale activity"""
        for tx in block.transactions:
            out_total = sum(o.value for o in tx.outputs)
            if out_total >= WHALE_THRESHOLD_NBL * 10**DECIMALS:
                self._alerts.append({
                    "type"     : "whale_tx",
                    "txid"     : tx.txid,
                    "amount"   : out_total / 10**DECIMALS,
                    "block"    : block.height,
                    "time"     : time.time(),
                })
        if len(self._alerts) > 1000:
            self._alerts = self._alerts[-1000:]

    def dashboard(self) -> dict:
        """Full analytics dashboard"""
        if time.time() - self._cache_time < ANALYTICS_CACHE_TTL:
            return self._cache

        data = {
            "chain_height"    : self.bc.height,
            "health"          : self.health.health_score(),
            "fee_market"      : self.fee_market.summary(),
            "rich_list_top10" : self.rich_list.get()[:10],
            "whale_count"     : self.rich_list.whale_count(),
            "clustering"      : self.clusterer.stats(),
            "miner_revenue"   : self.health.miner_revenue(),
            "recent_alerts"   : self._alerts[-10:],
            "utxo_stats"      : self._utxo_age_analysis(),
        }
        self._cache      = data
        self._cache_time = time.time()
        return data

    def _utxo_age_analysis(self) -> dict:
        bands = [UTXOAgeBand(b.label, b.min_blocks, b.max_blocks)
                 for b in UTXO_AGE_BANDS]
        current_h = self.bc.height
        for u in self.bc.utxo.all_utxos():
            age = current_h - u.height
            for band in bands:
                if band.min_blocks <= age < band.max_blocks:
                    band.count     += 1
                    band.value_nbl += u.value / 10**DECIMALS
                    break
        return {b.label: {"count": b.count, "value_nbl": round(b.value_nbl, 4)}
                for b in bands}

    def address_report(self, address: str) -> dict:
        utxos   = self.bc.utxo.get_by_address(address)
        balance = sum(u.value for u in utxos)
        return {
            "address"     : address,
            "balance_nbl" : balance / 10**DECIMALS,
            "utxos"       : len(utxos),
            "cluster"     : self.clusterer.get_cluster(address),
            "cluster_size": len(self.clusterer.cluster_members(address)),
            "incoming"    : len(self.tx_graph.incoming(address)),
            "outgoing"    : len(self.tx_graph.outgoing(address)),
            "is_whale"    : balance / 10**DECIMALS >= WHALE_THRESHOLD_NBL,
            "is_peel"     : self.tx_graph.is_peeling_chain(address),
        }

    def export_csv(self, data_type: str = "rich_list") -> str:
        """Export analytics data as CSV"""
        if data_type == "rich_list":
            rows = self.rich_list.get()
            lines = ["rank,address,balance_nbl,is_whale"]
            for r in rows:
                lines.append(f"{r['rank']},{r['address']},{r['balance']},{r['is_whale']}")
            return "\n".join(lines)
        return "unknown data type"

    def alerts(self, limit: int = 50) -> List[dict]:
        return self._alerts[-limit:]

# ---- Opcode  (kind C, v10.18 lines 36492-36630) ----
class Opcode(Enum):
    STOP        = 0x00
    ADD         = 0x01
    MUL         = 0x02
    SUB         = 0x03
    DIV         = 0x04
    SDIV        = 0x05
    MOD         = 0x06
    SMOD        = 0x07
    ADDMOD      = 0x08
    MULMOD      = 0x09
    EXP         = 0x0a
    SIGNEXTEND  = 0x0b
    LT          = 0x10
    GT          = 0x11
    SLT         = 0x12
    SGT         = 0x13
    EQ          = 0x14
    ISZERO      = 0x15
    AND         = 0x16
    OR          = 0x17
    XOR         = 0x18
    NOT         = 0x19
    BYTE        = 0x1a
    SHL         = 0x1b
    SHR         = 0x1c
    SAR         = 0x1d
    SHA3        = 0x20
    ADDRESS     = 0x30
    BALANCE     = 0x31
    ORIGIN      = 0x32
    CALLER      = 0x33
    CALLVALUE   = 0x34
    CALLDATALOAD= 0x35
    CALLDATASIZE= 0x36
    CALLDATACOPY= 0x37
    CODESIZE    = 0x38
    CODECOPY    = 0x39
    GASPRICE    = 0x3a
    EXTCODESIZE = 0x3b
    EXTCODECOPY = 0x3c
    BLOCKHASH   = 0x40
    COINBASE    = 0x41
    TIMESTAMP   = 0x42
    NUMBER      = 0x43
    DIFFICULTY  = 0x44
    GASLIMIT    = 0x45
    CHAINID     = 0x46
    SELFBALANCE = 0x47
    POP         = 0x50
    MLOAD       = 0x51
    MSTORE      = 0x52
    MSTORE8     = 0x53
    SLOAD       = 0x54
    SSTORE      = 0x55
    JUMP        = 0x56
    JUMPI       = 0x57
    PC          = 0x58
    MSIZE       = 0x59
    GAS         = 0x5a
    JUMPDEST    = 0x5b
    PUSH1       = 0x60
    PUSH2       = 0x61
    PUSH3       = 0x62
    PUSH4       = 0x63
    PUSH5       = 0x64
    PUSH6       = 0x65
    PUSH7       = 0x66
    PUSH8       = 0x67
    PUSH9       = 0x68
    PUSH10      = 0x69
    PUSH11      = 0x6a
    PUSH12      = 0x6b
    PUSH13      = 0x6c
    PUSH14      = 0x6d
    PUSH15      = 0x6e
    PUSH16      = 0x6f
    PUSH17      = 0x70
    PUSH18      = 0x71
    PUSH19      = 0x72
    PUSH20      = 0x73
    PUSH21      = 0x74
    PUSH22      = 0x75
    PUSH23      = 0x76
    PUSH24      = 0x77
    PUSH25      = 0x78
    PUSH26      = 0x79
    PUSH27      = 0x7a
    PUSH28      = 0x7b
    PUSH29      = 0x7c
    PUSH30      = 0x7d
    PUSH31      = 0x7e
    PUSH32      = 0x7f
    DUP1        = 0x80
    DUP2        = 0x81
    DUP3        = 0x82
    DUP4        = 0x83
    DUP5        = 0x84
    DUP6        = 0x85
    DUP7        = 0x86
    DUP8        = 0x87
    DUP9        = 0x88
    DUP10       = 0x89
    DUP11       = 0x8a
    DUP12       = 0x8b
    DUP13       = 0x8c
    DUP14       = 0x8d
    DUP15       = 0x8e
    DUP16       = 0x8f
    SWAP1       = 0x90
    SWAP2       = 0x91
    SWAP3       = 0x92
    SWAP4       = 0x93
    SWAP5       = 0x94
    SWAP6       = 0x95
    SWAP7       = 0x96
    SWAP8       = 0x97
    SWAP9       = 0x98
    SWAP10      = 0x99
    SWAP11      = 0x9a
    SWAP12      = 0x9b
    SWAP13      = 0x9c
    SWAP14      = 0x9d
    SWAP15      = 0x9e
    SWAP16      = 0x9f
    LOG0        = 0xa0
    LOG1        = 0xa1
    LOG2        = 0xa2
    LOG3        = 0xa3
    LOG4        = 0xa4
    CREATE      = 0xf0
    CALL        = 0xf1
    CALLCODE    = 0xf2
    RETURN      = 0xf3
    DELEGATECALL= 0xf4
    CREATE2     = 0xf5
    STATICCALL  = 0xfa
    REVERT      = 0xfd
    SELFDESTRUCT= 0xff

# ---- ContractEventLegacy  (kind C, v10.18 lines 36704-36728) ----
@dataclass
class ContractEventLegacy:
    contract_addr : str
    event_name    : str
    topics        : List[bytes]
    data          : bytes
    block_height  : int
    tx_index      : int
    log_index     : int
    timestamp     : float = field(default_factory=time.time)

    @property
    def topic0(self) -> Optional[bytes]:
        return self.topics[0] if self.topics else None

    def to_dict(self) -> dict:
        return {
            "address"      : self.contract_addr,
            "event"        : self.event_name,
            "topics"       : [t.hex() for t in self.topics],
            "data"         : self.data.hex(),
            "block"        : self.block_height,
            "tx_index"     : self.tx_index,
            "log_index"    : self.log_index,
        }

# ---- GasMeter  (kind C, v10.18 lines 36736-36768) ----
class GasMeter:
    """Precise EVM-compatible gas metering"""

    def __init__(self, gas_limit: int = MAX_GAS_PER_TX):
        self.limit   = gas_limit
        self.used    = 0
        self.refund  = 0

    def consume(self, amount: int, operation: str = "") -> bool:
        if self.used + amount > self.limit:
            raise ContractError(f"Out of gas at {operation}: used={self.used}, need={amount}, limit={self.limit}")
        self.used += amount
        return True

    def refund_gas(self, amount: int):
        self.refund += amount

    @property
    def remaining(self) -> int:
        return self.limit - self.used

    @property
    def net_used(self) -> int:
        return max(0, self.used - self.refund // 2)

    def to_dict(self) -> dict:
        return {
            "limit"    : self.limit,
            "used"     : self.used,
            "refund"   : self.refund,
            "net_used" : self.net_used,
            "remaining": self.remaining,
        }

# ---- ExecutionContext  (kind C, v10.18 lines 36771-36786) ----
@dataclass
class ExecutionContext:
    """Context passed to contract during execution"""
    caller        : str
    contract_addr : str
    value         : int   = 0
    data          : bytes = b''
    block_height  : int   = 0
    block_time    : int   = 0
    gas_limit     : int   = MAX_GAS_PER_TX
    chain_id      : int   = CHAIN_ID
    origin        : str   = ""

    def __post_init__(self):
        if not self.origin:
            self.origin = self.caller

# ---- TerminalWalletUI  (kind C, v10.18 lines 37155-37314) ----
class TerminalWalletUI:
    """Full-featured terminal wallet interface with menus"""

    TITLE = """
╔══════════════════════════════════════════════════════════╗
║         🌌 NEBULA WALLET — Command Line Interface        ║
║            Author: NEBULA Core Team  |  v1.0.0              ║
╚══════════════════════════════════════════════════════════╝"""

    MENU = """
  ┌─────────────────────────────────────────┐
  │  1.  Create new wallet                  │
  │  2.  Restore from mnemonic              │
  │  3.  Check balance                      │
  │  4.  Send NBL                           │
  │  5.  Receive (show address + QR)        │
  │  6.  Transaction history                │
  │  7.  Address book                       │
  │  8.  Export private keys                │
  │  9.  Security settings                  │
  │  10. Analytics dashboard                │
  │  0.  Exit                               │
  └─────────────────────────────────────────┘"""

    def __init__(self, blockchain: 'NEBULABlockchain',
                 wallet: 'NEBULAWallet' = None):
        self.bc          = blockchain
        self.wallet      = wallet
        self.address_book= AddressBook()
        self.analytics   = AnalyticsDashboard(blockchain)
        self._running    = False

    def run(self):
        print(self.TITLE)
        self._running = True
        while self._running:
            print(self.MENU)
            choice = input("  Choice: ").strip()
            self._dispatch(choice)

    def _dispatch(self, choice: str):
        actions = {
            "1": self._create_wallet,
            "2": self._restore_wallet,
            "3": self._show_balance,
            "4": self._send_nbl,
            "5": self._show_receive,
            "6": self._show_history,
            "7": self._address_book_menu,
            "8": self._export_keys,
            "9": self._security_menu,
            "10": self._show_analytics,
            "0": self._exit,
        }
        action = actions.get(choice)
        if action:
            try:
                action()
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print(f"  ❌ Error: {e}")
        else:
            print("  Invalid choice")

    def _create_wallet(self):
        print("\n  Creating new HD wallet...")
        self.wallet = NEBULAWallet.create_new(self.bc.utxo)
        print(f"\n  ✅ Wallet created!")
        print(f"  Address  : {self.wallet.first_address}")
        print(f"\n  ⚠️  WRITE DOWN YOUR 12-WORD MNEMONIC:")
        print(f"  {self.wallet.mnemonic}")
        input("\n  Press Enter when you have written it down...")

    def _restore_wallet(self):
        phrase = input("\n  Enter mnemonic (12 words): ").strip()
        try:
            self.wallet = NEBULAWallet.from_mnemonic(phrase, utxo_set=self.bc.utxo)
            print(f"  ✅ Wallet restored: {self.wallet.first_address}")
        except Exception as e:
            print(f"  ❌ Invalid mnemonic: {e}")

    def _show_balance(self):
        if not self.wallet:
            addr = input("\n  Enter address: ").strip()
        else:
            addr = self.wallet.first_address
        info = self.bc.get_balance(addr)
        print(f"\n  Address  : {addr}")
        print(f"  Balance  : {info['balance_nbl']:.9f} NBL")
        print(f"  UTXOs    : {info['utxo_count']}")

    def _send_nbl(self):
        if not self.wallet:
            print("  ❌ No wallet loaded"); return
        to_addr = input("\n  Recipient address: ").strip()
        amount  = float(input("  Amount (NBL): "))
        label   = self.address_book.label(to_addr)
        print(f"  Sending {amount:.9f} NBL to {label}...")
        tx = self.wallet.build_transaction(to_addr, amount)
        if tx:
            ok, msg = self.bc.mempool.submit(tx)
            print(f"  {'✅' if ok else '❌'} {msg}: {tx.txid[:20]}...")
            if ok:
                self.address_book.mark_used(to_addr)
                self.address_book.add_tx_note(
                    tx.txid, f"Sent to {label}", amount, "sent")
        else:
            print("  ❌ Insufficient balance")

    def _show_receive(self):
        if not self.wallet:
            print("  ❌ No wallet loaded"); return
        addr = self.wallet.first_address
        print(f"\n  Your address: {addr}")
        QRCodeGenerator.display_payment(addr)

    def _show_history(self):
        if not self.wallet:
            print("  ❌ No wallet loaded"); return
        addr  = self.wallet.first_address
        utxos = self.bc.utxo.get_by_address(addr)
        print(f"\n  Last {min(5, len(utxos))} UTXOs:")
        for u in utxos[-5:]:
            print(f"  • {u.txid[:20]}... | {u.value/10**DECIMALS:.9f} NBL | block #{u.height}")

    def _address_book_menu(self):
        print(f"\n  Address book: {self.address_book.stats()['total']} entries")
        q = input("  Search (or Enter to list all): ").strip()
        results = self.address_book.search(q) if q else list(self.address_book._entries.values())
        for e in results[:10]:
            print(f"  • {e.label[:25]:25} | {e.address[:20]}...")

    def _export_keys(self):
        if not self.wallet:
            print("  ❌ No wallet loaded"); return
        confirm = input("  ⚠️  Are you sure? This shows private keys (yes/no): ")
        if confirm.lower() == 'yes':
            key = self.wallet.master.derive_path(NBL_BIP44_PATH + "/0/0")
            print(f"  WIF: {key.wif}")
            print(f"  ⚠️  NEVER share this with anyone!")

    def _security_menu(self):
        print("""
  Security Options:
  1. Change wallet password
  2. Verify wallet backup
  3. Show security status""")
        choice = input("  Choice: ").strip()
        if choice == "3":
            print("  ✅ ECDSA: secp256k1 (production grade)")
            print("  ✅ Wallet: AES-256 encrypted (PBKDF2)")
            print("  ✅ BIP39: 12-word mnemonic backup")

    def _show_analytics(self):
        self.analytics.print_dashboard()

    def _exit(self):
        print("\n  Goodbye! 🌌")
        self._running = False

# ---- NetworkSimulator  (kind C, v10.18 lines 37523-37568) ----
class NetworkSimulator:
    """
    Multi-node NEBULA network simulator.
    Used for testing consensus, mining, and propagation.
    Creates N independent blockchain instances and simulates messages.
    """

    def __init__(self, num_nodes: int = 3):
        self.nodes : List['SimNode'] = []
        for i in range(num_nodes):
            self.nodes.append(SimNode(node_id=i))
        self._lock = threading.Lock()

    def mine_block(self, node_idx: int = 0,
                    broadcast: bool = True) -> Optional['Block']:
        """Mine a block on node and optionally broadcast"""
        node  = self.nodes[node_idx]
        miner = NEBULAMiner(node.bc, node.miner_address)
        blk   = miner.mine_demo_block(easy_bits=0x1f7fffff, timeout_secs=10)
        if blk:
            ok, _ = node.bc.add_block(blk)
            if ok and broadcast:
                self._broadcast(blk, source=node_idx)
        return blk

    def _broadcast(self, block: 'Block', source: int):
        """Broadcast block to all other nodes"""
        for i, node in enumerate(self.nodes):
            if i != source:
                node.bc.add_block(block)

    def get_heights(self) -> List[int]:
        return [n.bc.height for n in self.nodes]

    def is_consensus(self) -> bool:
        """True if all nodes agree on tip"""
        tips = [n.bc.tip.hash for n in self.nodes]
        return len(set(tips)) == 1

    def stats(self) -> dict:
        return {
            "node_count" : len(self.nodes),
            "heights"    : self.get_heights(),
            "in_consensus": self.is_consensus(),
            "tips"       : [n.bc.tip.hash[:16]+"..." for n in self.nodes],
        }

# ---- SimNode  (kind C, v10.18 lines 37570-37583) ----
@dataclass
class SimNode:
    """Single simulated node"""
    node_id       : int
    bc            : 'NEBULABlockchain' = field(default_factory=NEBULABlockchain)
    miner_address : str = ""

    def __post_init__(self):
        # Create deterministic miner address
        seed    = f"sim_node_{self.node_id}".encode()
        privkey = int(hashlib.sha256(seed).hexdigest(), 16) % Secp256k1.N
        pub     = Secp256k1.pubkey_to_bytes(
                      Secp256k1.point_mul(privkey, Secp256k1.G()))
        self.miner_address = Script.p2pkh_address(pub)

# ---- OrderBookSimple  (kind C, v10.18 lines 37846-37977) ----
class OrderBookSimple:
    """
    On-chain limit order book for NEBULA DEX.
    Supports: limit orders, market orders, cancel, partial fill.
    Orders are stored in blockchain state (contract storage).
    """

    @dataclass
    class OrderAdv:
        order_id  : int
        maker     : str
        pair      : str
        side      : str   # "buy" or "sell"
        price     : int   # in smallest units (neb per token unit)
        amount    : int   # token amount remaining
        filled    : int = 0
        timestamp : float = field(default_factory=time.time)
        is_active : bool = True

        @property
        def remaining(self) -> int:
            return self.amount - self.filled

        def to_dict(self) -> dict:
            return {
                "id"        : self.order_id,
                "maker"     : self.maker,
                "pair"      : self.pair,
                "side"      : self.side,
                "price"     : self.price,
                "amount"    : self.amount,
                "filled"    : self.filled,
                "remaining" : self.remaining,
                "active"    : self.is_active,
            }

    def __init__(self, pair: str):
        self.pair       = pair
        self._bids      : List['OrderBook.Order'] = []   # buy orders
        self._asks      : List['OrderBook.Order'] = []   # sell orders
        self._next_id   = 1
        self._trades    : List[dict] = []
        self._lock      = threading.RLock()

    def place_limit(self, maker: str, side: str,
                     price: int, amount: int) -> 'OrderBook.Order':
        """Place limit order"""
        with self._lock:
            order = self.Order(
                order_id = self._next_id,
                maker    = maker,
                pair     = self.pair,
                side     = side,
                price    = price,
                amount   = amount,
            )
            self._next_id += 1

            if side == "buy":
                self._bids.append(order)
                self._bids.sort(key=lambda o: (-o.price, o.timestamp))
            else:
                self._asks.append(order)
                self._asks.sort(key=lambda o: (o.price, o.timestamp))

            # Try to match
            self._match()
            return order

    def _match(self):
        """Attempt order matching"""
        while self._bids and self._asks:
            best_bid = self._bids[0]
            best_ask = self._asks[0]
            if best_bid.price < best_ask.price:
                break

            trade_price  = best_ask.price   # taker gets maker's price
            trade_amount = min(best_bid.remaining, best_ask.remaining)

            best_bid.filled += trade_amount
            best_ask.filled += trade_amount

            self._trades.append({
                "pair"   : self.pair,
                "price"  : trade_price,
                "amount" : trade_amount,
                "buyer"  : best_bid.maker,
                "seller" : best_ask.maker,
                "time"   : time.time(),
            })

            if best_bid.remaining == 0:
                best_bid.is_active = False
                self._bids.pop(0)
            if best_ask.remaining == 0:
                best_ask.is_active = False
                self._asks.pop(0)

    def cancel(self, maker: str, order_id: int) -> bool:
        with self._lock:
            for pool in [self._bids, self._asks]:
                for order in pool:
                    if order.order_id == order_id and order.maker == maker:
                        order.is_active = False
                        pool.remove(order)
                        return True
        return False

    def best_bid(self) -> Optional[int]:
        return self._bids[0].price if self._bids else None

    def best_ask(self) -> Optional[int]:
        return self._asks[0].price if self._asks else None

    def spread(self) -> Optional[float]:
        bb, ba = self.best_bid(), self.best_ask()
        if bb and ba and ba > 0:
            return (ba - bb) / ba * 100
        return None

    def depth(self, levels: int = 10) -> dict:
        return {
            "bids": [{"price": o.price, "amount": o.remaining}
                     for o in self._bids[:levels]],
            "asks": [{"price": o.price, "amount": o.remaining}
                     for o in self._asks[:levels]],
            "spread_pct": self.spread(),
        }

    def recent_trades(self, n: int = 20) -> List[dict]:
        return self._trades[-n:]

# ---- DAOTreasury  (kind C, v10.18 lines 38350-38400) ----
class DAOTreasury:
    """
    NEBULA DAO treasury management.
    Receives 2% foundation allocation.
    Funds can only be spent via governance proposals.
    Supports multi-token treasury (NBL + tokens).
    """

    def __init__(self, address: str = FOUNDATION_ADDRESS):
        self.address      = address
        self._balances    : Dict[str, int] = {}  # token -> balance
        self._expenditures: List[dict] = []
        self._lock        = threading.Lock()

    def receive(self, token: str, amount: int, from_addr: str = ""):
        with self._lock:
            self._balances[token] = self._balances.get(token, 0) + amount

    def spend(self, token: str, amount: int, to: str,
               proposal_id: int, description: str = "") -> bool:
        with self._lock:
            if self._balances.get(token, 0) < amount:
                return False
            self._balances[token] -= amount
            self._expenditures.append({
                "token"       : token,
                "amount"      : amount,
                "to"          : to,
                "proposal_id" : proposal_id,
                "description" : description,
                "time"        : time.time(),
            })
        return True

    def balance(self, token: str = "NBL") -> int:
        return self._balances.get(token, 0)

    def total_spent(self, token: str = "NBL") -> int:
        return sum(e["amount"] for e in self._expenditures
                   if e["token"] == token)

    def expenditure_history(self) -> List[dict]:
        return list(self._expenditures)

    def to_dict(self) -> dict:
        return {
            "address"    : self.address,
            "balances"   : {k: v/10**DECIMALS for k, v in self._balances.items()},
            "total_spent": self.total_spent() / 10**DECIMALS,
            "grants"     : len(self._expenditures),
        }

# ---- NEBULAGovernance  (kind C, v10.18 lines 38403-38590) ----
class NEBULAGovernance:
    """
    Full on-chain governance for NEBULA.
    Inspired by Compound Governor Bravo + OpenZeppelin.
    Parameters are upgradeable via proposals.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc          = blockchain
        self.treasury    = DAOTreasury()
        self.timelock    = Timelock()
        self._proposals  : Dict[int, Proposal] = {}
        self._next_id    = 1
        self._params     : Dict[str, Any] = {
            "block_reward"      : INITIAL_BLOCK_REWARD,
            "min_tx_fee"        : MIN_TX_FEE,
            "max_block_size"    : MAX_BLOCK_SIZE_BYTES,
            "halving_interval"  : HALVING_INTERVAL,
            "target_block_time" : TARGET_BLOCK_TIME,
        }
        self._lock       = threading.RLock()
        self._emergency_keys: List[str] = []
        self._emergency_sigs: Dict[str, List[str]] = {}

    def propose(self, proposer: str, title: str, description: str,
                 proposal_type: ProposalType,
                 calldata: bytes = b'') -> Tuple[int, str]:
        """Submit a governance proposal"""
        with self._lock:
            # Check bond
            balance = self.bc.utxo.balance(proposer)
            if balance < PROPOSAL_BOND:
                return -1, f"Insufficient bond: {balance/10**DECIMALS} < {PROPOSAL_BOND/10**DECIMALS} NBL"

            # Check active proposal limit
            active = sum(1 for p in self._proposals.values()
                         if p.state in (ProposalState.PENDING, ProposalState.ACTIVE))
            if active >= MAX_ACTIVE_PROPOSALS:
                return -1, "Too many active proposals"

            pid        = self._next_id
            self._next_id += 1
            start      = self.bc.height + 1
            end        = start + PROPOSAL_DURATION

            proposal = Proposal(
                proposal_id  = pid,
                proposer     = proposer,
                title        = title,
                description  = description,
                proposal_type= proposal_type,
                calldata     = calldata,
                start_block  = start,
                end_block    = end,
                state        = ProposalState.ACTIVE,
            )
            self._proposals[pid] = proposal
        return pid, "Proposal created"

    def vote(self, voter: str, proposal_id: int,
              choice: VoteChoice) -> Tuple[bool, str]:
        """Cast vote on a proposal"""
        with self._lock:
            p = self._proposals.get(proposal_id)
            if p is None:
                return False, "Proposal not found"
            if p.state != ProposalState.ACTIVE:
                return False, f"Proposal is {p.state.value}"
            if self.bc.height < p.start_block or self.bc.height > p.end_block:
                return False, "Not in voting period"
            if p.has_voted(voter):
                return False, "Already voted"

            # Voting weight = NBL balance at snapshot
            weight = self.bc.utxo.balance(voter)
            if weight == 0:
                return False, "No voting power"

            p.record_vote(voter, choice, weight)
        return True, f"Voted {choice.name} with weight {weight/10**DECIMALS:.4f} NBL"

    def finalize(self, proposal_id: int) -> Tuple[bool, str]:
        """Finalize proposal after voting period"""
        with self._lock:
            p = self._proposals.get(proposal_id)
            if p is None:
                return False, "Not found"
            if self.bc.height <= p.end_block:
                return False, "Voting still active"
            if p.state != ProposalState.ACTIVE:
                return False, f"Already {p.state.value}"

            # Check quorum
            total_supply = self.bc.utxo.total_supply()
            quorum_needed = total_supply * QUORUM_PERCENT // 100
            if p.total_votes < quorum_needed:
                p.state = ProposalState.DEFEATED
                return True, f"Defeated (quorum: {p.total_votes} < {quorum_needed})"

            # Check majority
            if p.approval_pct >= MAJORITY_PERCENT:
                p.state = ProposalState.SUCCEEDED
                # Queue in timelock
                eta = self.bc.height + TIMELOCK_DELAY
                p.eta = eta
                tx_hash = hashlib.sha256(p.calldata + p.proposal_id.to_bytes(4,'big')).digest()
                self.timelock.queue_tx(tx_hash, "nebula", p.calldata, eta)
                p.state = ProposalState.QUEUED
                return True, f"Queued for execution at block {eta}"
            else:
                p.state = ProposalState.DEFEATED
                return True, f"Defeated ({p.approval_pct:.1f}% < {MAJORITY_PERCENT}%)"

    def execute(self, proposal_id: int) -> Tuple[bool, str]:
        """Execute a queued proposal"""
        with self._lock:
            p = self._proposals.get(proposal_id)
            if p is None:
                return False, "Not found"
            if p.state != ProposalState.QUEUED:
                return False, f"Not queued: {p.state.value}"

            tx_hash = hashlib.sha256(
                p.calldata + p.proposal_id.to_bytes(4,'big')).digest()
            ok, reason = self.timelock.execute_tx(tx_hash, self.bc.height)
            if not ok:
                return False, reason

            # Execute action
            self._apply_proposal(p)
            p.state      = ProposalState.EXECUTED
            p.executed_at = time.time()
        return True, "Executed"

    def _apply_proposal(self, p: Proposal):
        """Apply proposal effects (parameter changes, treasury spends)"""
        if p.proposal_type == ProposalType.PARAMETER_CHANGE:
            # Calldata: key (32 bytes) + value (32 bytes)
            if len(p.calldata) >= 64:
                key   = p.calldata[:32].rstrip(b'\x00').decode(errors='replace')
                value = int.from_bytes(p.calldata[32:64], 'big')
                if key in self._params:
                    self._params[key] = value

        elif p.proposal_type == ProposalType.TREASURY_SPEND:
            # Calldata: to (32 bytes) + amount (32 bytes)
            if len(p.calldata) >= 64:
                to     = p.calldata[:32].rstrip(b'\x00').decode(errors='replace')
                amount = int.from_bytes(p.calldata[32:64], 'big')
                self.treasury.spend("NBL", amount, to, p.proposal_id)

    def cancel(self, proposal_id: int, caller: str) -> Tuple[bool, str]:
        with self._lock:
            p = self._proposals.get(proposal_id)
            if p is None: return False, "Not found"
            if p.state not in (ProposalState.PENDING, ProposalState.ACTIVE,
                                ProposalState.QUEUED):
                return False, "Cannot cancel"
            if caller != p.proposer and caller not in self._emergency_keys:
                return False, "Not authorized"
            p.state    = ProposalState.CANCELLED
            p.canceller = caller
        return True, "Cancelled"

    def get_proposal(self, pid: int) -> Optional[dict]:
        p = self._proposals.get(pid)
        return p.to_dict() if p else None

    def all_proposals(self, state: ProposalState = None) -> List[dict]:
        proposals = self._proposals.values()
        if state:
            proposals = [p for p in proposals if p.state == state]
        return [p.to_dict() for p in proposals]

    def set_parameter(self, key: str) -> Any:
        return self._params.get(key)

    def governance_stats(self) -> dict:
        return {
            "total_proposals"  : len(self._proposals),
            "active"           : sum(1 for p in self._proposals.values()
                                    if p.state == ProposalState.ACTIVE),
            "executed"         : sum(1 for p in self._proposals.values()
                                    if p.state == ProposalState.EXECUTED),
            "treasury"         : self.treasury.to_dict(),
            "timelock_pending" : len(self.timelock.pending()),
            "parameters"       : self._params,
        }

# ---- ValidatorRecord  (kind C, v10.18 lines 38635-38701) ----
@dataclass
class ValidatorRecord:
    address       : str
    pubkey        : bytes
    moniker       : str          # name
    commission    : int          # basis points (1000 = 10%)
    min_self_del  : int          # minimum self-delegation
    stake         : int = 0      # total bonded stake
    self_stake    : int = 0      # validator's own stake
    delegated     : int = 0      # delegated from others
    status        : ValidatorStatus = ValidatorStatus.INACTIVE
    jailed_until  : int = 0      # block height
    tombstoned    : bool = False
    slash_count   : int = 0
    uptime        : float = 1.0  # 0.0 - 1.0
    last_block    : int = 0
    created_at    : float = field(default_factory=time.time)
    rewards_acc   : int = 0      # accumulated rewards
    _delegators   : Dict[str, int] = field(default_factory=dict)

    @property
    def voting_power(self) -> int:
        return self.stake if self.status == ValidatorStatus.ACTIVE else 0

    @property
    def commission_rate(self) -> float:
        return self.commission / 10000

    def delegate(self, delegator: str, amount: int):
        self._delegators[delegator] = self._delegators.get(delegator, 0) + amount
        self.delegated += amount
        self.stake     += amount

    def undelegate(self, delegator: str, amount: int) -> bool:
        if self._delegators.get(delegator, 0) < amount:
            return False
        self._delegators[delegator] -= amount
        if self._delegators[delegator] == 0:
            del self._delegators[delegator]
        self.delegated -= amount
        self.stake     -= amount
        return True

    def delegator_share(self, delegator: str) -> float:
        if self.stake == 0: return 0
        return self._delegators.get(delegator, 0) / self.stake

    def slash(self, slash_factor: int):
        """slash_factor in basis points (5000 = 50%)"""
        slashed = self.stake * slash_factor // 10000
        self.stake     -= slashed
        self.slash_count += 1
        return slashed

    def to_dict(self) -> dict:
        return {
            "address"      : self.address,
            "moniker"      : self.moniker,
            "stake_nbl"    : self.stake / 10**DECIMALS,
            "self_stake"   : self.self_stake / 10**DECIMALS,
            "delegated"    : self.delegated / 10**DECIMALS,
            "status"       : self.status.value,
            "commission"   : f"{self.commission/100:.1f}%",
            "uptime"       : f"{self.uptime*100:.1f}%",
            "delegators"   : len(self._delegators),
            "voting_power" : self.voting_power,
        }

# ---- BridgeChain  (kind C, v10.18 lines 38992-38997) ----
class BridgeChain(Enum):
    NEBULA  = "nebula"
    BITCOIN = "bitcoin"
    ETHEREUM= "ethereum"
    SOLANA  = "solana"
    BNB     = "bnb"

# ---- BridgeTx  (kind C, v10.18 lines 39007-39054) ----
@dataclass
class BridgeTx:
    bridge_id   : str
    source_chain: BridgeChain
    dest_chain  : BridgeChain
    sender      : str
    receiver    : str
    token       : str
    amount      : int
    fee         : int
    nonce       : int
    created_at  : int         # source chain block height
    expires_at  : int
    status      : BridgeTxStatus = BridgeTxStatus.PENDING
    source_txid : str = ""
    dest_txid   : str = ""
    relay_sigs  : List[bytes] = field(default_factory=list)
    proof       : bytes = b''

    @property
    def bridge_hash(self) -> bytes:
        data = (self.bridge_id.encode() +
                self.sender.encode() +
                self.receiver.encode() +
                self.amount.to_bytes(16,'big') +
                self.nonce.to_bytes(8,'big'))
        return hashlib.sha256(data).digest()

    @property
    def net_amount(self) -> int:
        return self.amount - self.fee

    def is_expired(self, current_height: int) -> bool:
        return current_height > self.expires_at

    def to_dict(self) -> dict:
        return {
            "bridge_id"    : self.bridge_id,
            "from"         : f"{self.source_chain.value}:{self.sender}",
            "to"           : f"{self.dest_chain.value}:{self.receiver}",
            "token"        : self.token,
            "amount"       : self.amount / 10**DECIMALS,
            "fee"          : self.fee / 10**DECIMALS,
            "net_amount"   : self.net_amount / 10**DECIMALS,
            "status"       : self.status.value,
            "signatures"   : len(self.relay_sigs),
            "required_sigs": REQUIRED_RELAYERS,
        }

# ---- BridgeProofVerifier  (kind C, v10.18 lines 39068-39097) ----
class BridgeProofVerifier:
    """
    Verifies cryptographic proofs of cross-chain events.
    Supports Merkle proofs, SPV proofs, light client proofs.
    """

    @staticmethod
    def verify_bitcoin_spv(proof: bytes, tx_hash: bytes,
                            block_header: bytes) -> bool:
        """Verify Bitcoin SPV proof"""
        # Simplified — full implementation would verify actual Bitcoin headers
        if len(proof) < 32 or len(block_header) < 80:
            return False
        return proof[:32] == hashlib.sha256(tx_hash).digest()[:32]

    @staticmethod
    def verify_ethereum_receipt(proof: bytes,
                                  receipt_root: bytes) -> bool:
        """Verify Ethereum receipt Merkle proof"""
        # Simplified RLP + Merkle verification
        if not proof: return False
        h = hashlib.sha256(proof).digest()
        return h[:4] == receipt_root[:4]

    @staticmethod
    def verify_nebula_proof(proof: bytes,
                              tx_hash: bytes) -> bool:
        """Verify NEBULA Merkle proof"""
        if not proof or len(proof) < 32: return False
        return proof[:32] == hashlib.sha256(tx_hash).digest()

# ---- NEBULACrossChainBridge  (kind C, v10.18 lines 39100-39265) ----
class NEBULACrossChainBridge:
    """
    Cross-chain bridge for NEBULA.
    Inspired by IBC (Inter-Blockchain Communication Protocol).
    Supports: lock-and-mint, burn-and-release, atomic swaps.
    Multi-sig relayers validate cross-chain events.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc          = blockchain
        self._relayers   : Dict[str, Relayer] = {}
        self._txs        : Dict[str, BridgeTx] = {}
        self._nonce      = 0
        self._locked     : Dict[str, int] = {}   # token -> locked amount
        self._minted     : Dict[str, int] = {}   # wrapped_token -> minted
        self._lock       = threading.RLock()
        self._total_volume = 0
        self._verifier   = BridgeProofVerifier()

    def add_relayer(self, relayer: Relayer) -> bool:
        with self._lock:
            if len(self._relayers) >= MAX_RELAYERS:
                return False
            self._relayers[relayer.address] = relayer
        return True

    def initiate_outbound(self, sender: str,
                           dest_chain: BridgeChain,
                           receiver: str,
                           amount: int,
                           token: str = "NBL") -> Tuple[str, str]:
        """
        Initiate outbound bridge transfer.
        Locks NBL on NEBULA, relayers mint wrapped token on dest chain.
        """
        with self._lock:
            if amount < MIN_BRIDGE_AMOUNT:
                return "", f"Below min: {MIN_BRIDGE_AMOUNT/10**DECIMALS} NBL"
            if amount > MAX_BRIDGE_AMOUNT:
                return "", f"Above max: {MAX_BRIDGE_AMOUNT/10**DECIMALS} NBL"

            bal = self.bc.utxo.balance(sender)
            if bal < amount:
                return "", f"Insufficient balance: {bal/10**DECIMALS}"

            fee       = amount * BRIDGE_FEE_PCT // 10000
            self._nonce += 1
            bid       = hashlib.sha256(
                sender.encode() + receiver.encode() +
                self._nonce.to_bytes(8,'big') +
                struct.pack('>Q', int(time.time()))).hexdigest()[:16]

            btx = BridgeTx(
                bridge_id    = bid,
                source_chain = BridgeChain.NEBULA,
                dest_chain   = dest_chain,
                sender       = sender,
                receiver     = receiver,
                token        = token,
                amount       = amount,
                fee          = fee,
                nonce        = self._nonce,
                created_at   = self.bc.height,
                expires_at   = self.bc.height + BRIDGE_TIMEOUT,
            )
            self._txs[bid] = btx
            self._locked[token] = self._locked.get(token, 0) + amount

        return bid, "Initiated"

    def relay_inbound(self, relayer_addr: str,
                       bridge_id: str,
                       proof: bytes,
                       signature: bytes) -> Tuple[bool, str]:
        """
        Relayer submits proof of dest chain event.
        When REQUIRED_RELAYERS have signed, bridge tx is finalized.
        """
        with self._lock:
            btx = self._txs.get(bridge_id)
            if btx is None:
                return False, "Bridge tx not found"
            if btx.is_expired(self.bc.height):
                btx.status = BridgeTxStatus.FAILED
                return False, "Expired"
            if relayer_addr not in self._relayers:
                return False, "Unknown relayer"

            # Verify signature
            r = self._relayers[relayer_addr]
            if not r.is_active:
                return False, "Relayer inactive"

            btx.relay_sigs.append(signature)
            btx.proof = proof
            r.txs_relayed += 1

            # Finalize if enough signatures
            if len(btx.relay_sigs) >= REQUIRED_RELAYERS:
                # Verify proof
                proof_ok = self._verifier.verify_nebula_proof(
                    proof, btx.bridge_hash)
                if not proof_ok:
                    btx.status = BridgeTxStatus.FAILED
                    return False, "Proof verification failed"

                btx.status = BridgeTxStatus.FINALIZED
                self._total_volume += btx.amount

                # Distribute fee to relayers
                fee_per_relayer = btx.fee // len(self._relayers)
                for rel in self._relayers.values():
                    rel.rewards += fee_per_relayer

        return True, "Finalized"

    def process_inbound(self, source_chain: BridgeChain,
                          receiver: str, amount: int,
                          token: str, proof: bytes) -> Tuple[bool, str]:
        """
        Process inbound bridge (mint wrapped tokens or release locked NBL).
        """
        with self._lock:
            # Simplified proof check
            if not proof:
                return False, "No proof"

            wrapped_key = f"w{token}.{source_chain.value}"
            self._minted[wrapped_key] = self._minted.get(wrapped_key, 0) + amount

        return True, f"Minted {amount/10**DECIMALS} {wrapped_key} to {receiver}"

    def refund(self, bridge_id: str) -> Tuple[bool, str]:
        """Refund expired bridge transactions"""
        with self._lock:
            btx = self._txs.get(bridge_id)
            if btx is None: return False, "Not found"
            if not btx.is_expired(self.bc.height):
                return False, "Not yet expired"
            if btx.status == BridgeTxStatus.FINALIZED:
                return False, "Already finalized"
            btx.status = BridgeTxStatus.REFUNDED
            self._locked[btx.token] = max(0,
                self._locked.get(btx.token, 0) - btx.amount)
        return True, "Refunded"

    def bridge_stats(self) -> dict:
        return {
            "total_txs"       : len(self._txs),
            "finalized"       : sum(1 for t in self._txs.values()
                                    if t.status == BridgeTxStatus.FINALIZED),
            "pending"         : sum(1 for t in self._txs.values()
                                    if t.status == BridgeTxStatus.PENDING),
            "total_locked"    : {k: v/10**DECIMALS for k,v in self._locked.items()},
            "total_minted"    : {k: v/10**DECIMALS for k,v in self._minted.items()},
            "total_volume_nbl": self._total_volume / 10**DECIMALS,
            "relayers"        : len(self._relayers),
        }

    def get_tx(self, bridge_id: str) -> Optional[dict]:
        t = self._txs.get(bridge_id)
        return t.to_dict() if t else None

    def pending_txs(self) -> List[dict]:
        return [t.to_dict() for t in self._txs.values()
                if t.status == BridgeTxStatus.PENDING]

# ---- NodeID  (kind C, v10.18 lines 39293-39323) ----
class NodeID:
    """256-bit Kademlia-style node identifier"""

    def __init__(self, value: bytes = None):
        if value is None:
            import secrets
            value = secrets.token_bytes(32)
        self.value = value[:32].ljust(32, b'\x00')

    @classmethod
    def from_address(cls, host: str, port: int) -> 'NodeID':
        data = f"{host}:{port}".encode()
        return cls(hashlib.sha256(data).digest())

    def distance(self, other: 'NodeID') -> int:
        """XOR distance metric"""
        a = int.from_bytes(self.value, 'big')
        b = int.from_bytes(other.value, 'big')
        return a ^ b

    def __eq__(self, other): return self.value == other.value
    def __hash__(self): return hash(self.value)
    def __str__(self): return self.value.hex()[:16]

    @property
    def leading_zeros(self) -> int:
        for i, byte in enumerate(self.value):
            for bit in range(7, -1, -1):
                if byte & (1 << bit):
                    return i * 8 + (7 - bit)
        return 256

# ---- DHTNode  (kind C, v10.18 lines 39326-39347) ----
@dataclass
class DHTNode:
    node_id    : NodeID
    host       : str
    port       : int
    last_seen  : float = field(default_factory=time.time)
    failures   : int = 0
    rtt_ms     : float = 0.0

    @property
    def is_good(self) -> bool:
        return (self.failures < 3 and
                time.time() - self.last_seen < 3600)

    def to_dict(self) -> dict:
        return {
            "id"      : str(self.node_id),
            "host"    : self.host,
            "port"    : self.port,
            "last_seen": self.last_seen,
            "good"    : self.is_good,
        }

# ---- KBucket  (kind C, v10.18 lines 39350-39397) ----
class KBucket:
    """Kademlia k-bucket for routing table"""

    def __init__(self, k: int = DHT_K):
        self.k     = k
        self.nodes : List[DHTNode] = []
        self.cache : List[DHTNode] = []   # replacement cache
        self._lock = threading.Lock()

    def add(self, node: DHTNode) -> bool:
        with self._lock:
            # Check if already exists
            for existing in self.nodes:
                if existing.node_id == node.node_id:
                    # Move to tail (most recently seen)
                    self.nodes.remove(existing)
                    existing.last_seen = time.time()
                    self.nodes.append(existing)
                    return True

            if len(self.nodes) < self.k:
                self.nodes.append(node)
                return True
            else:
                # Bucket full — check if head is alive
                head = self.nodes[0]
                if not head.is_good:
                    self.nodes.pop(0)
                    self.nodes.append(node)
                    return True
                else:
                    # Add to replacement cache
                    if len(self.cache) < self.k:
                        self.cache.append(node)
                    return False

    def remove(self, node_id: NodeID):
        with self._lock:
            self.nodes = [n for n in self.nodes if n.node_id != node_id]
            # Promote from cache
            if self.cache:
                self.nodes.append(self.cache.pop(0))

    def get_nodes(self) -> List[DHTNode]:
        return list(self.nodes)

    def __len__(self) -> int:
        return len(self.nodes)

# ---- KademliaRoutingTable  (kind C, v10.18 lines 39400-39445) ----
class KademliaRoutingTable:
    """
    Full Kademlia routing table.
    256 k-buckets for 256-bit node IDs.
    """

    def __init__(self, local_id: NodeID):
        self.local_id = local_id
        self.buckets  = [KBucket() for _ in range(DHT_BITS)]
        self._lock    = threading.RLock()

    def _bucket_index(self, node_id: NodeID) -> int:
        dist = self.local_id.distance(node_id)
        if dist == 0: return 0
        return DHT_BITS - 1 - (dist.bit_length() - 1)

    def add(self, node: DHTNode) -> bool:
        if node.node_id == self.local_id: return False
        idx = self._bucket_index(node.node_id)
        return self.buckets[idx].add(node)

    def remove(self, node_id: NodeID):
        idx = self._bucket_index(node_id)
        self.buckets[idx].remove(node_id)

    def find_closest(self, target_id: NodeID, k: int = DHT_K) -> List[DHTNode]:
        """Find k closest nodes to target"""
        all_nodes = []
        for bucket in self.buckets:
            all_nodes.extend(bucket.get_nodes())

        all_nodes.sort(key=lambda n: n.node_id.distance(target_id))
        return all_nodes[:k]

    def all_nodes(self) -> List[DHTNode]:
        nodes = []
        for bucket in self.buckets:
            nodes.extend(bucket.get_nodes())
        return nodes

    def bucket_sizes(self) -> dict:
        non_empty = {i: len(b) for i, b in enumerate(self.buckets) if len(b) > 0}
        return {
            "total_nodes"   : sum(non_empty.values()),
            "non_empty_buckets": len(non_empty),
        }

# ---- InventoryManager  (kind C, v10.18 lines 39448-39549) ----
class InventoryManager:
    """
    P2P inventory management.
    Tracks announced transactions/blocks.
    Implements Erlay reconciliation for bandwidth efficiency.
    """

    def __init__(self, node_id: NodeID):
        self.node_id      = node_id
        self._known_txs   : Set[str] = set()
        self._known_blocks: Set[str] = set()
        self._peer_invs   : Dict[str, Set[str]] = {}  # peer -> announced inv
        self._pending_req : Dict[str, float] = {}
        self._lock        = threading.Lock()
        self._inv_sketch  : Dict[str, Set[str]] = {}

    def announce_tx(self, txid: str):
        with self._lock:
            self._known_txs.add(txid)

    def announce_block(self, block_hash: str):
        with self._lock:
            self._known_blocks.add(block_hash)

    def receive_inv(self, peer_id: str, items: List[Tuple[str,str]]) -> List[Tuple[str,str]]:
        """
        Process received inventory from peer.
        Returns items we need to request.
        """
        needed = []
        with self._lock:
            for item_type, item_hash in items:
                if item_type == "tx" and item_hash not in self._known_txs:
                    needed.append((item_type, item_hash))
                elif item_type == "block" and item_hash not in self._known_blocks:
                    needed.append((item_type, item_hash))
            self._peer_invs.setdefault(peer_id, set()).update(
                h for _, h in items)
        return needed

    def get_items_for_peer(self, peer_id: str) -> List[Tuple[str,str]]:
        """Get inventory items peer doesn't know about"""
        with self._lock:
            peer_known = self._peer_invs.get(peer_id, set())
            inv = []
            for txid in self._known_txs:
                if txid not in peer_known:
                    inv.append(("tx", txid))
            for bh in self._known_blocks:
                if bh not in peer_known:
                    inv.append(("block", bh))
            return inv[:INV_BATCH_SIZE]

    def erlay_sketch(self, peer_id: str) -> bytes:
        """
        Erlay: create set reconciliation sketch.
        IBLT-inspired compact representation of known txids.
        """
        known_for_peer = self.get_items_for_peer(peer_id)
        sketch_data = b''
        for _, item_hash in known_for_peer[:64]:
            h = hashlib.sha256(item_hash.encode()).digest()[:4]
            sketch_data += h
        return sketch_data

    def reconcile(self, peer_id: str,
                   peer_sketch: bytes) -> List[str]:
        """Reconcile differences using Erlay sketch"""
        local_sketch = self.erlay_sketch(peer_id)
        # Simplified XOR reconciliation
        needed = []
        if len(peer_sketch) == len(local_sketch):
            diff = bytes(a ^ b for a, b in zip(peer_sketch, local_sketch))
            if any(diff):
                # Some items differ — request full diff
                items = self.get_items_for_peer(peer_id)
                needed = [h for _, h in items[:8]]
        return needed

    def mark_received(self, item_hash: str, item_type: str):
        with self._lock:
            if item_type == "tx":
                self._known_txs.add(item_hash)
            else:
                self._known_blocks.add(item_hash)
            self._pending_req.pop(item_hash, None)

    def cleanup(self, max_size: int = 10000):
        """Trim old inventory to prevent memory growth"""
        with self._lock:
            if len(self._known_txs) > max_size:
                excess = len(self._known_txs) - max_size
                items  = list(self._known_txs)[:excess]
                for item in items:
                    self._known_txs.discard(item)

    def stats(self) -> dict:
        return {
            "known_txs"     : len(self._known_txs),
            "known_blocks"  : len(self._known_blocks),
            "peers_tracked" : len(self._peer_invs),
        }

# ---- GossipProtocol  (kind C, v10.18 lines 39552-39632) ----
class GossipProtocol:
    """
    Gossip-based message propagation for NEBULA.
    Flood-fill with deduplication (like Bitcoin).
    Optional: Dandelion++ stem phase for tx privacy.
    """

    def __init__(self, node_id: NodeID, fanout: int = GOSSIP_FANOUT):
        self.node_id     = node_id
        self.fanout      = fanout
        self._seen       : Dict[str, float] = {}
        self._peers      : List[str] = []
        self._lock       = threading.Lock()
        self._callbacks  : Dict[str, List[Callable]] = {}
        self._stats      = GossipStats()

    def add_peer(self, peer_id: str):
        with self._lock:
            if peer_id not in self._peers:
                self._peers.append(peer_id)

    def remove_peer(self, peer_id: str):
        with self._lock:
            if peer_id in self._peers:
                self._peers.remove(peer_id)

    def receive(self, msg_id: str, msg_type: str,
                 data: bytes, from_peer: str) -> Tuple[bool, List[str]]:
        """
        Receive a gossip message.
        Returns (is_new, list_of_peers_to_forward_to).
        """
        with self._lock:
            if msg_id in self._seen:
                self._stats.duplicates += 1
                return False, []

            self._seen[msg_id]    = time.time()
            self._stats.received += 1

            # Select fanout peers (exclude source)
            eligible = [p for p in self._peers if p != from_peer]
            random.shuffle(eligible)
            forward_to = eligible[:self.fanout]

            self._stats.forwarded += len(forward_to)

        # Fire callbacks
        for cb in self._callbacks.get(msg_type, []):
            try: cb(msg_id, data)
            except Exception: pass

        return True, forward_to

    def broadcast(self, msg_id: str, msg_type: str,
                   data: bytes) -> List[str]:
        """Broadcast a new message to all peers"""
        with self._lock:
            self._seen[msg_id] = time.time()
            forward_to = list(self._peers)[:self.fanout * 2]
            self._stats.broadcast += 1
        return forward_to

    def on(self, msg_type: str, callback: Callable):
        """Register handler for message type"""
        self._callbacks.setdefault(msg_type, []).append(callback)

    def prune_seen(self, max_age: float = 3600):
        cutoff = time.time() - max_age
        with self._lock:
            self._seen = {k: v for k, v in self._seen.items() if v > cutoff}

    def stats(self) -> dict:
        return {
            "peers"      : len(self._peers),
            "seen"       : len(self._seen),
            "received"   : self._stats.received,
            "forwarded"  : self._stats.forwarded,
            "duplicates" : self._stats.duplicates,
            "broadcast"  : self._stats.broadcast,
        }

# ---- GossipStats  (kind C, v10.18 lines 39634-39639) ----
@dataclass
class GossipStats:
    received   : int = 0
    forwarded  : int = 0
    duplicates : int = 0
    broadcast  : int = 0

# ---- PaymentURI  (kind C, v10.18 lines 39728-39777) ----
class PaymentURI:
    """
    NEBULA payment URI (BIP21-style).
    Format: nebula:<address>?amount=<NBL>&label=<str>&message=<str>
    """

    SCHEME = "nebula"

    @staticmethod
    def encode(address: str, amount_nbl: float = 0,
                label: str = "", message: str = "",
                req_params: Dict[str, str] = None) -> str:
        """Encode payment URI"""
        uri = f"{PaymentURI.SCHEME}:{address}"
        params = []
        if amount_nbl > 0:
            params.append(f"amount={amount_nbl:.9f}")
        if label:
            params.append(f"label={label.replace(' ','%20')}")
        if message:
            params.append(f"message={message.replace(' ','%20')}")
        if req_params:
            for k, v in req_params.items():
                params.append(f"req-{k}={v}")
        if params:
            uri += "?" + "&".join(params)
        return uri

    @staticmethod
    def decode(uri: str) -> dict:
        """Decode payment URI"""
        uri = uri.strip()
        if not uri.startswith(PaymentURI.SCHEME + ":"):
            raise ValueError("Not a NEBULA payment URI")
        rest    = uri[len(PaymentURI.SCHEME)+1:]
        parts   = rest.split("?", 1)
        address = parts[0]
        params  = {}
        if len(parts) > 1:
            for param in parts[1].split("&"):
                if "=" in param:
                    k, v = param.split("=", 1)
                    params[k] = v.replace('%20', ' ')
        return {
            "address": address,
            "amount" : float(params.get("amount", 0)),
            "label"  : params.get("label", ""),
            "message": params.get("message", ""),
            "params" : params,
        }

# ---- QRCodeGeneratorAdv  (kind C, v10.18 lines 39780-39804) ----
class QRCodeGeneratorAdv:
    """
    Simple QR code data generator.
    Returns QR code as ASCII art or raw matrix.
    """

    @staticmethod
    def generate_ascii(data: str, size: int = 21) -> str:
        """Generate ASCII QR code (placeholder — actual QR needs qrcode library)"""
        h = hashlib.sha256(data.encode()).hexdigest()
        lines = ["▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"]
        lines.append(f"█ NEBULA QR Code █")
        lines.append(f"█ {data[:16]}{'...' if len(data)>16 else ''} █")
        lines.append(f"█ {h[:8]} █")
        lines.append("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
        return "\n".join(lines)

    @staticmethod
    def payment_qr(address: str, amount_nbl: float = 0) -> str:
        uri = PaymentURI.encode(address, amount_nbl)
        return QRCodeGenerator.generate_ascii(uri)

    @staticmethod
    def address_qr(address: str) -> str:
        return QRCodeGenerator.generate_ascii(address)

# ---- WalletNotification  (kind C, v10.18 lines 39807-39832) ----
@dataclass
class WalletNotification:
    """Wallet push notification"""
    notification_id: str
    address        : str
    event_type     : str   # "received", "sent", "confirmed", "new_block"
    title          : str
    body           : str
    amount_nbl     : float = 0
    txid           : str = ""
    block_height   : int = 0
    timestamp      : float = 0.0
    is_read        : bool = False

    def to_dict(self) -> dict:
        return {
            "id"          : self.notification_id,
            "type"        : self.event_type,
            "title"       : self.title,
            "body"        : self.body,
            "amount"      : self.amount_nbl,
            "txid"        : self.txid,
            "block"       : self.block_height,
            "time"        : self.timestamp,
            "read"        : self.is_read,
        }

# ---- MobileWalletAPI  (kind C, v10.18 lines 39838-40028) ----
class MobileWalletAPI:
    """
    Lightweight REST API for mobile wallets.
    Endpoints optimized for mobile: small payloads, fast response.
    Handles: balance, send, receive, history, notifications.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 wallet: 'MultiAccountWallet' = None):
        self.bc             = blockchain
        self.wallet         = wallet
        self._notifications : Dict[str, List[WalletNotification]] = {}
        self._watch_wallets : Dict[str, WatchOnlyWallet] = {}
        self._sessions      : Dict[str, dict] = {}
        self._lock          = threading.RLock()

    def get_balance(self, address: str) -> dict:
        """GET /api/v1/balance/:address"""
        balance   = self.bc.utxo.balance(address)
        utxos     = self.bc.utxo.get_by_address(address)
        confirmed = sum(u.value for u in utxos
                        if self.bc.height - u.height >= 6)
        unconfirmed = balance - confirmed

        return {
            "address"      : address,
            "balance"      : balance / 10**DECIMALS,
            "confirmed"    : confirmed / 10**DECIMALS,
            "unconfirmed"  : unconfirmed / 10**DECIMALS,
            "utxo_count"   : len(utxos),
            "block_height" : self.bc.height,
        }

    def get_transactions(self, address: str,
                          page: int = 1, per_page: int = 20) -> dict:
        """GET /api/v1/txs/:address"""
        txs = []
        for blk in reversed(self.bc._chain[-500:]):
            for tx in blk.transactions:
                for out in tx.outputs:
                    if out.address == address:
                        txs.append({
                            "txid"     : tx.txid,
                            "type"     : "received",
                            "amount"   : out.value / 10**DECIMALS,
                            "block"    : blk.height,
                            "time"     : blk.header.timestamp,
                            "confirms" : self.bc.height - blk.height,
                        })
                for inp in tx.inputs:
                    u = self.bc.utxo.get(inp.outpoint.txid, inp.outpoint.index)
                    if u and u.address == address:
                        txs.append({
                            "txid"     : tx.txid,
                            "type"     : "sent",
                            "amount"   : u.value / 10**DECIMALS,
                            "block"    : blk.height,
                            "time"     : blk.header.timestamp,
                            "confirms" : self.bc.height - blk.height,
                        })

        start  = (page - 1) * per_page
        end    = start + per_page
        return {
            "address"  : address,
            "txs"      : txs[start:end],
            "total"    : len(txs),
            "page"     : page,
            "pages"    : (len(txs) + per_page - 1) // per_page,
        }

    def build_send_request(self, from_address: str,
                            to_address: str,
                            amount_nbl: float) -> dict:
        """POST /api/v1/send — builds unsigned tx for wallet to sign"""
        amount = int(amount_nbl * 10**DECIMALS)
        utxos  = self.bc.utxo.get_by_address(from_address)
        if not utxos:
            return {"error": "No UTXOs"}

        fee = MIN_TX_FEE * 2
        selected = UTXOSelector.knapsack(utxos, amount + fee)
        if selected is None:
            return {"error": "Insufficient balance"}

        total_in = sum(u.value for u in selected)
        change   = total_in - amount - fee

        tx_data = {
            "inputs"  : [{"txid": u.txid, "vout": u.index,
                          "amount": u.value/10**DECIMALS} for u in selected],
            "outputs" : [{"address": to_address, "amount": amount_nbl}],
            "fee"     : fee / 10**DECIMALS,
        }
        if change > DUST_THRESHOLD:
            tx_data["outputs"].append({
                "address": from_address,
                "amount" : change / 10**DECIMALS,
            })

        return {"unsigned_tx": tx_data}

    def get_payment_request(self, address: str,
                             amount_nbl: float = 0,
                             label: str = "",
                             message: str = "") -> dict:
        """GET /api/v1/payment_request"""
        uri = PaymentURI.encode(address, amount_nbl, label, message)
        qr  = QRCodeGenerator.payment_qr(address, amount_nbl)
        return {
            "address"    : address,
            "amount"     : amount_nbl,
            "uri"        : uri,
            "qr_ascii"   : qr,
            "label"      : label,
            "message"    : message,
        }

    def get_notifications(self, address: str,
                           since: float = 0) -> List[dict]:
        """GET /api/v1/notifications/:address"""
        notifs = self._notifications.get(address, [])
        return [n.to_dict() for n in notifs
                if n.timestamp > since]

    def register_address_watch(self, address: str):
        """Register address for notification watching"""
        with self._lock:
            if address not in self._notifications:
                self._notifications[address] = []

    def emit_notification(self, address: str,
                           event_type: str,
                           title: str, body: str,
                           **kwargs):
        """Emit notification for watched address"""
        nid = hashlib.sha256(
            address.encode() + event_type.encode() +
            str(time.time()).encode()).hexdigest()[:12]

        notif = WalletNotification(
            notification_id = nid,
            address         = address,
            event_type      = event_type,
            title           = title,
            body            = body,
            timestamp       = time.time(),
            **kwargs
        )
        with self._lock:
            if address in self._notifications:
                self._notifications[address].append(notif)
                if len(self._notifications[address]) > 100:
                    self._notifications[address] = \
                        self._notifications[address][-100:]

    def on_new_block(self, block: 'Block'):
        """Called on each new block — send relevant notifications"""
        for tx in block.transactions:
            for out in tx.outputs:
                if out.address and out.address in self._notifications:
                    self.emit_notification(
                        out.address, "received",
                        "NBL Received",
                        f"You received {out.value/10**DECIMALS:.4f} NBL",
                        amount_nbl = out.value / 10**DECIMALS,
                        txid       = tx.txid,
                        block_height = block.height,
                    )

    def fee_recommendation(self) -> dict:
        """GET /api/v1/fees"""
        return {
            "economy" : MIN_TX_FEE / 10**DECIMALS,
            "standard": MIN_TX_FEE * 2 / 10**DECIMALS,
            "fast"    : MIN_TX_FEE * 5 / 10**DECIMALS,
            "unit"    : "NBL/tx",
        }

    def network_status(self) -> dict:
        """GET /api/v1/status"""
        return {
            "chain"       : CHAIN_NAME,
            "symbol"      : CHAIN_SYMBOL,
            "height"      : self.bc.height,
            "tip_hash"    : self.bc.tip.hash,
            "mempool_size": self.bc.mempool.size(),
            "block_reward": mining_reward(self.bc.height) / 10**DECIMALS,
            "supply_pct"  : self.bc.utxo.total_supply() / MAX_SUPPLY * 100,
            "synced"      : True,
        }

# ---- ScriptErrorAdv  (kind C, v10.18 lines 40044-40045) ----
class ScriptErrorAdv(Exception):
    pass

# ---- ScriptInterpreterAdv  (kind C, v10.18 lines 40189-40572) ----
class ScriptInterpreterAdv:
    """
    Full Bitcoin Script interpreter.
    Implements all enabled opcodes per BIP141/BIP342.
    Used for transaction validation and smart contract execution.
    """

    MAX_STACK_SIZE  = 1000
    MAX_SCRIPT_SIZE = 10_000
    MAX_OPS         = 201
    MAX_ELEMENT_SIZE= 520

    def __init__(self, flags: int = 0):
        self.flags     = flags
        self.stack     : List[bytes] = []
        self.altstack  : List[bytes] = []
        self._op_count = 0

    def _pop(self) -> bytes:
        if not self.stack:
            raise ScriptError("Stack underflow")
        return self.stack.pop()

    def _peek(self) -> bytes:
        if not self.stack:
            raise ScriptError("Stack empty")
        return self.stack[-1]

    def _push(self, val: bytes):
        if len(self.stack) >= self.MAX_STACK_SIZE:
            raise ScriptError("Stack overflow")
        self.stack.append(val)

    def _bool(self, val: bytes) -> bool:
        for i, b in enumerate(val):
            if b != 0:
                if i == len(val) - 1 and b == 0x80:
                    return False
                return True
        return False

    def _true(self): self._push(b'\x01')
    def _false(self): self._push(b'')

    def execute(self, script: bytes,
                 sig_checker=None) -> Tuple[bool, str]:
        """
        Execute a Bitcoin script.
        Returns (success, error_message).
        """
        self.stack.clear()
        self.altstack.clear()
        self._op_count = 0

        if len(script) > self.MAX_SCRIPT_SIZE:
            return False, "Script too large"

        i = 0
        exec_stack = []   # for IF/ELSE/ENDIF

        while i < len(script):
            op = script[i]
            i += 1

            # Should we execute? (inside false IF branch)
            executing = all(exec_stack)

            # Data push
            if 0x01 <= op <= 0x4b:
                data = script[i:i+op]
                i += op
                if executing:
                    self._push(data)
                continue

            if op == ScriptOpcode.OP_PUSHDATA1:
                n    = script[i]; i += 1
                data = script[i:i+n]; i += n
                if executing: self._push(data)
                continue

            if op == ScriptOpcode.OP_PUSHDATA2:
                n    = struct.unpack_from('<H', script, i)[0]; i += 2
                data = script[i:i+n]; i += n
                if executing: self._push(data)
                continue

            if op == ScriptOpcode.OP_PUSHDATA4:
                n    = struct.unpack_from('<I', script, i)[0]; i += 4
                data = script[i:i+n]; i += n
                if executing: self._push(data)
                continue

            # OP_0
            if op == ScriptOpcode.OP_0:
                if executing: self._push(b'')
                continue

            # OP_1 through OP_16
            if 0x51 <= op <= 0x60:
                if executing: self._push(_script_int_to_bytes(op - 0x50))
                continue

            if op == ScriptOpcode.OP_1NEGATE:
                if executing: self._push(_script_int_to_bytes(-1))
                continue

            # Flow control
            if op == ScriptOpcode.OP_IF:
                if executing:
                    val = self._pop()
                    exec_stack.append(self._bool(val))
                else:
                    exec_stack.append(False)
                continue

            if op == ScriptOpcode.OP_NOTIF:
                if executing:
                    val = self._pop()
                    exec_stack.append(not self._bool(val))
                else:
                    exec_stack.append(False)
                continue

            if op == ScriptOpcode.OP_ELSE:
                if exec_stack:
                    exec_stack[-1] = not exec_stack[-1]
                continue

            if op == ScriptOpcode.OP_ENDIF:
                if exec_stack: exec_stack.pop()
                continue

            if not executing:
                continue

            self._op_count += 1
            if self._op_count > self.MAX_OPS:
                return False, "Too many opcodes"

            # Stack ops
            if op == ScriptOpcode.OP_NOP: pass
            elif op == ScriptOpcode.OP_VERIFY:
                if not self._bool(self._pop()):
                    return False, "OP_VERIFY failed"
            elif op == ScriptOpcode.OP_RETURN:
                return False, "OP_RETURN"
            elif op == ScriptOpcode.OP_DROP:   self._pop()
            elif op == ScriptOpcode.OP_2DROP:  self._pop(); self._pop()
            elif op == ScriptOpcode.OP_DUP:    self._push(self._peek())
            elif op == ScriptOpcode.OP_2DUP:
                b = self._pop(); a = self._pop()
                self._push(a); self._push(b)
                self._push(a); self._push(b)
            elif op == ScriptOpcode.OP_3DUP:
                c = self._pop(); b = self._pop(); a = self._pop()
                for x in [a,b,c,a,b,c]: self._push(x)
            elif op == ScriptOpcode.OP_OVER:
                b = self._pop(); a = self._peek()
                self._push(b); self._push(a)
            elif op == ScriptOpcode.OP_SWAP:
                b = self._pop(); a = self._pop()
                self._push(b); self._push(a)
            elif op == ScriptOpcode.OP_ROT:
                c=self._pop(); b=self._pop(); a=self._pop()
                self._push(b); self._push(c); self._push(a)
            elif op == ScriptOpcode.OP_TUCK:
                b=self._pop(); a=self._pop()
                self._push(b); self._push(a); self._push(b)
            elif op == ScriptOpcode.OP_NIP:
                b=self._pop(); self._pop(); self._push(b)
            elif op == ScriptOpcode.OP_IFDUP:
                if self._bool(self._peek()): self._push(self._peek())
            elif op == ScriptOpcode.OP_DEPTH:
                self._push(_script_int_to_bytes(len(self.stack)))
            elif op == ScriptOpcode.OP_TOALTSTACK:
                self.altstack.append(self._pop())
            elif op == ScriptOpcode.OP_FROMALTSTACK:
                if not self.altstack: return False, "Alt stack empty"
                self._push(self.altstack.pop())
            elif op == ScriptOpcode.OP_SIZE:
                self._push(_script_int_to_bytes(len(self._peek())))
            elif op == ScriptOpcode.OP_PICK:
                n = _bytes_to_script_int(self._pop())
                if n < 0 or n >= len(self.stack):
                    return False, "OP_PICK: invalid index"
                self._push(self.stack[-(n+1)])
            elif op == ScriptOpcode.OP_ROLL:
                n = _bytes_to_script_int(self._pop())
                if n < 0 or n >= len(self.stack):
                    return False, "OP_ROLL: invalid index"
                self._push(self.stack.pop(-(n+1)))

            # Bitwise
            elif op == ScriptOpcode.OP_EQUAL:
                b=self._pop(); a=self._pop()
                self._true() if a==b else self._false()
            elif op == ScriptOpcode.OP_EQUALVERIFY:
                b=self._pop(); a=self._pop()
                if a != b: return False, "OP_EQUALVERIFY failed"

            # Arithmetic
            elif op == ScriptOpcode.OP_ADD:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(a+b))
            elif op == ScriptOpcode.OP_SUB:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(a-b))
            elif op == ScriptOpcode.OP_MUL:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(a*b))
            elif op == ScriptOpcode.OP_DIV:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                if b == 0: return False, "Division by zero"
                self._push(_script_int_to_bytes(int(a/b)))
            elif op == ScriptOpcode.OP_MOD:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                if b == 0: return False, "Modulo by zero"
                self._push(_script_int_to_bytes(a%b))
            elif op == ScriptOpcode.OP_NEGATE:
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(-a))
            elif op == ScriptOpcode.OP_ABS:
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(abs(a)))
            elif op == ScriptOpcode.OP_NOT:
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(1 if a==0 else 0))
            elif op == ScriptOpcode.OP_0NOTEQUAL:
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(0 if a==0 else 1))
            elif op == ScriptOpcode.OP_1ADD:
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(a+1))
            elif op == ScriptOpcode.OP_1SUB:
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(a-1))
            elif op == ScriptOpcode.OP_MIN:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(min(a,b)))
            elif op == ScriptOpcode.OP_MAX:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(max(a,b)))
            elif op == ScriptOpcode.OP_WITHIN:
                mx=_bytes_to_script_int(self._pop())
                mn=_bytes_to_script_int(self._pop())
                x=_bytes_to_script_int(self._pop())
                self._true() if mn<=x<mx else self._false()
            elif op == ScriptOpcode.OP_BOOLAND:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(1 if a!=0 and b!=0 else 0))
            elif op == ScriptOpcode.OP_BOOLOR:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._push(_script_int_to_bytes(1 if a!=0 or b!=0 else 0))
            elif op == ScriptOpcode.OP_NUMEQUAL:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._true() if a==b else self._false()
            elif op == ScriptOpcode.OP_NUMEQUALVERIFY:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                if a != b: return False, "OP_NUMEQUALVERIFY failed"
            elif op == ScriptOpcode.OP_NUMNOTEQUAL:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._true() if a!=b else self._false()
            elif op == ScriptOpcode.OP_LESSTHAN:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._true() if a<b else self._false()
            elif op == ScriptOpcode.OP_GREATERTHAN:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._true() if a>b else self._false()
            elif op == ScriptOpcode.OP_LESSTHANOREQUAL:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._true() if a<=b else self._false()
            elif op == ScriptOpcode.OP_GREATERTHANOREQUAL:
                b=_bytes_to_script_int(self._pop())
                a=_bytes_to_script_int(self._pop())
                self._true() if a>=b else self._false()

            # Crypto
            elif op == ScriptOpcode.OP_RIPEMD160:
                self._push(hashlib.new('ripemd160', self._pop()).digest())
            elif op == ScriptOpcode.OP_SHA1:
                self._push(hashlib.sha1(self._pop()).digest())
            elif op == ScriptOpcode.OP_SHA256:
                self._push(hashlib.sha256(self._pop()).digest())
            elif op == ScriptOpcode.OP_HASH160:
                d = hashlib.new('ripemd160', hashlib.sha256(self._pop()).digest()).digest()
                self._push(d)
            elif op == ScriptOpcode.OP_HASH256:
                self._push(hashlib.sha256(hashlib.sha256(self._pop()).digest()).digest())
            elif op == ScriptOpcode.OP_CHECKSIG:
                pubkey = self._pop()
                sig    = self._pop()
                if sig_checker:
                    ok = sig_checker.check_sig(sig, pubkey)
                    self._true() if ok else self._false()
                else:
                    self._true()   # no checker = assume valid
            elif op == ScriptOpcode.OP_CHECKSIGVERIFY:
                pubkey = self._pop()
                sig    = self._pop()
                if sig_checker and not sig_checker.check_sig(sig, pubkey):
                    return False, "OP_CHECKSIGVERIFY failed"
            elif op == ScriptOpcode.OP_CHECKMULTISIG:
                n = _bytes_to_script_int(self._pop())
                if n < 0 or n > 20: return False, "Invalid n"
                pubkeys = [self._pop() for _ in range(n)]
                m = _bytes_to_script_int(self._pop())
                if m < 0 or m > n: return False, "Invalid m"
                sigs    = [self._pop() for _ in range(m)]
                self._pop()   # dummy (CHECKMULTISIG bug)
                self._true()  # simplified: assume valid
            elif op == ScriptOpcode.OP_CHECKSIGADD:
                n      = _bytes_to_script_int(self._pop())
                pubkey = self._pop()
                sig    = self._pop()
                if sig:
                    self._push(_script_int_to_bytes(n + 1))
                else:
                    self._push(_script_int_to_bytes(n))
            elif op == ScriptOpcode.OP_CHECKLOCKTIMEVERIFY:
                pass   # simplified: always pass
            elif op == ScriptOpcode.OP_CHECKSEQUENCEVERIFY:
                pass   # simplified: always pass
            elif 0xb0 <= op <= 0xb9:
                pass   # NOP4-NOP10: ignore
            elif op == ScriptOpcode.OP_CODESEPARATOR:
                pass   # no-op for now
            else:
                return False, f"Unknown opcode: 0x{op:02x}"

        if exec_stack:
            return False, "Unbalanced IF"

        if not self.stack:
            return False, "Empty stack"

        return self._bool(self._peek()), ""

    def verify_p2pkh(self, script_sig: bytes,
                      script_pubkey: bytes,
                      sig_checker=None) -> Tuple[bool, str]:
        """Verify P2PKH: run scriptSig then scriptPubKey"""
        interp = ScriptInterpreter(self.flags)
        ok, err = interp.execute(script_sig, sig_checker)
        if not ok and err:
            return False, f"scriptSig: {err}"
        # Transfer stack
        self.stack = interp.stack[:]
        return self.execute(script_pubkey, sig_checker)

    @staticmethod
    def disassemble(script: bytes) -> str:
        """Convert script bytes to human-readable ASM"""
        parts = []
        i = 0
        opnames = {v.value: v.name for v in ScriptOpcode}
        while i < len(script):
            op = script[i]; i += 1
            if 0x01 <= op <= 0x4b:
                data = script[i:i+op]; i += op
                parts.append(data.hex())
            elif op == 0x4c:
                n=script[i]; i+=1; data=script[i:i+n]; i+=n
                parts.append(f"OP_PUSHDATA1({data.hex()})")
            elif op in opnames:
                parts.append(opnames[op])
            else:
                parts.append(f"0x{op:02x}")
        return " ".join(parts)

# ---- TimelockParams  (kind C, v10.18 lines 40886-40906) ----
@dataclass
class TimelockParams:
    """Parameters for a timelock"""
    locktime     : int    # block height or Unix timestamp
    is_timestamp : bool = False   # False = block height, True = timestamp
    sequence     : int  = 0       # for CSV

    @property
    def is_block_height(self) -> bool:
        return not self.is_timestamp and self.locktime < 500_000_000

    def is_mature(self, current_height: int,
                   current_time: int = None) -> bool:
        if self.is_timestamp:
            return (current_time or int(time.time())) >= self.locktime
        return current_height >= self.locktime

    def blocks_remaining(self, current_height: int) -> int:
        if self.is_block_height:
            return max(0, self.locktime - current_height)
        return 0

# ---- VaultWallet  (kind C, v10.18 lines 41012-41070) ----
class VaultWallet:
    """
    Vault wallet implementation using timelocked scripts.
    Funds can only be spent after a delay (prevents theft).
    Use cases: cold storage, inheritance, corporate treasury.
    """

    def __init__(self, owner_privkey: int, heir_privkey: int,
                  delay_blocks: int = 144):  # 144 blocks ≈ 1 day
        self.owner_pk   = Secp256k1.pubkey_to_bytes(
                              Secp256k1.point_mul(owner_privkey, Secp256k1.G()))
        self.heir_pk    = Secp256k1.pubkey_to_bytes(
                              Secp256k1.point_mul(heir_privkey, Secp256k1.G()))
        self.owner_privkey = owner_privkey
        self.heir_privkey  = heir_privkey
        self.delay_blocks  = delay_blocks
        self.vault_script  = TimelockScript.vault_script(
                                 self.owner_pk, self.heir_pk, delay_blocks)

    def vault_address(self) -> str:
        """P2SH address for the vault"""
        h160 = hashlib.new('ripemd160',
               hashlib.sha256(self.vault_script).digest()).digest()
        return base58check_encode(h160, SCRIPT_ADDRESS_VERSION)

    def owner_spend_scriptsig(self, tx: 'Transaction',
                               input_idx: int) -> bytes:
        """Build scriptSig for owner spending"""
        sighash = tx.signature_hash(input_idx, self.vault_script, SIGHASH_ALL)
        r, s    = Secp256k1.sign(self.owner_privkey, sighash)
        sig     = Secp256k1.sig_to_der(r, s) + bytes([SIGHASH_ALL])
        # OP_IF path: <sig> <pubkey> OP_1 <redeem_script>
        return (bytes([len(sig)]) + sig +
                bytes([len(self.owner_pk)]) + self.owner_pk +
                bytes([0x51]) +   # OP_1 = true for IF
                bytes([0x4c, len(self.vault_script)]) + self.vault_script)

    def heir_spend_scriptsig(self, tx: 'Transaction',
                              input_idx: int) -> bytes:
        """Build scriptSig for heir spending (after delay)"""
        sighash = tx.signature_hash(input_idx, self.vault_script, SIGHASH_ALL)
        r, s    = Secp256k1.sign(self.heir_privkey, sighash)
        sig     = Secp256k1.sig_to_der(r, s) + bytes([SIGHASH_ALL])
        # OP_ELSE path: <sig> <pubkey> OP_0 <redeem_script>
        return (bytes([len(sig)]) + sig +
                bytes([len(self.heir_pk)]) + self.heir_pk +
                bytes([0x00]) +   # OP_0 = false for IF → ELSE path
                bytes([0x4c, len(self.vault_script)]) + self.vault_script)

    def info(self) -> dict:
        return {
            "vault_address"  : self.vault_address(),
            "delay_blocks"   : self.delay_blocks,
            "delay_days"     : self.delay_blocks * TARGET_BLOCK_TIME / 86400,
            "owner_address"  : Script.p2pkh_address(self.owner_pk),
            "heir_address"   : Script.p2pkh_address(self.heir_pk),
            "script_hex"     : self.vault_script.hex(),
            "script_asm"     : ScriptInterpreter.disassemble(self.vault_script),
        }

# ---- HTLCManager  (kind C, v10.18 lines 41072-41121) ----
class HTLCManager:
    """
    Manages HTLC contracts for atomic swaps and Lightning channels.
    """

    def __init__(self):
        self._htlcs    : Dict[str, dict] = {}
        self._lock     = threading.Lock()

    def create_htlc(self, sender_privkey: int,
                     receiver_pk: bytes,
                     amount_nbl: float,
                     timeout_blocks: int = 144) -> dict:
        """Create a new HTLC"""
        # Generate random preimage
        preimage     = secrets.token_bytes(32)
        payment_hash = hashlib.sha256(preimage).digest()

        sender_pk = Secp256k1.pubkey_to_bytes(
                         Secp256k1.point_mul(sender_privkey, Secp256k1.G()))
        script    = TimelockScript.htlc_script(
                         sender_pk, receiver_pk, preimage, timeout_blocks)

        htlc_id = payment_hash.hex()
        htlc    = {
            "id"            : htlc_id,
            "preimage"      : preimage.hex(),
            "payment_hash"  : payment_hash.hex(),
            "amount_nbl"    : amount_nbl,
            "timeout_blocks": timeout_blocks,
            "script_hex"    : script.hex(),
            "status"        : "pending",
            "created_at"    : time.time(),
        }
        with self._lock:
            self._htlcs[htlc_id] = htlc
        return htlc

    def reveal_preimage(self, htlc_id: str) -> Optional[bytes]:
        """Reveal preimage to claim payment"""
        with self._lock:
            htlc = self._htlcs.get(htlc_id)
            if htlc:
                htlc["status"] = "claimed"
                return bytes.fromhex(htlc["preimage"])
        return None

    def list_htlcs(self) -> List[dict]:
        with self._lock:
            return list(self._htlcs.values())

# ---- PSBTRole  (kind C, v10.18 lines 41372-41378) ----
class PSBTRole:
    CREATOR  = "creator"
    UPDATER  = "updater"
    SIGNER   = "signer"
    COMBINER = "combiner"
    FINALIZER= "finalizer"
    EXTRACTOR= "extractor"

# ---- PSBTInput  (kind C, v10.18 lines 41380-41411) ----
@dataclass
class PSBTInput:
    """PSBT input with partial signing info"""
    outpoint      : 'OutPoint'
    sequence      : int   = 0xFFFFFFFF
    utxo          : Optional['UTXOEntry'] = None
    witness_utxo  : Optional['TxOutput']  = None
    partial_sigs  : Dict[bytes, bytes] = field(default_factory=dict)
    sighash_type  : int = SIGHASH_ALL
    redeem_script : Optional[bytes] = None
    witness_script: Optional[bytes] = None
    bip32_derivation: Dict[bytes, str] = field(default_factory=dict)
    final_scriptsig: Optional[bytes]  = None
    final_witness  : Optional[List[bytes]] = None
    is_finalized  : bool = False

    def add_partial_sig(self, pubkey: bytes, sig: bytes):
        self.partial_sigs[pubkey] = sig

    def finalize(self, script_sig: bytes = None,
                  witness: List[bytes] = None):
        self.final_scriptsig = script_sig
        self.final_witness   = witness
        self.is_finalized    = True

    def to_dict(self) -> dict:
        return {
            "outpoint"     : f"{self.outpoint.txid}:{self.outpoint.index}",
            "partial_sigs" : {pk.hex(): sig.hex()
                              for pk, sig in self.partial_sigs.items()},
            "is_finalized" : self.is_finalized,
        }

# ---- PSBTOutput  (kind C, v10.18 lines 41413-41420) ----
@dataclass
class PSBTOutput:
    """PSBT output"""
    amount           : int
    script_pubkey    : bytes
    redeem_script    : Optional[bytes] = None
    witness_script   : Optional[bytes] = None
    bip32_derivation : Dict[bytes, str] = field(default_factory=dict)

# ---- PartiallySignedTransaction  (kind C, v10.18 lines 41422-41555) ----
class PartiallySignedTransaction:
    """
    PSBT (BIP174) implementation.
    Enables: hardware wallet signing, multi-party signing, air-gapped signing.
    Flow: Creator → Updater → Signer × N → Combiner → Finalizer → Extractor
    """

    MAGIC = b"psbt\xff"

    def __init__(self, tx: Optional['Transaction'] = None):
        self.tx      = tx
        self.inputs  : List[PSBTInput]  = []
        self.outputs : List[PSBTOutput] = []
        self.metadata: Dict = {"version": 0}

        if tx:
            for inp in tx.inputs:
                self.inputs.append(PSBTInput(outpoint=inp.outpoint,
                                              sequence=inp.sequence))
            for out in tx.outputs:
                self.outputs.append(PSBTOutput(amount=out.value,
                                                script_pubkey=out.script_pubkey))

    # ── Creator role ─────────────────────────────────────────────
    @classmethod
    def create(cls, inputs: List['OutPoint'],
                outputs: List[Tuple[str, int]],
                locktime: int = 0) -> 'PartiallySignedTransaction':
        """Create unsigned PSBT"""
        tx_inputs  = [TxInput(op, b'', sequence=0xFFFFFFFD) for op in inputs]
        tx_outputs = [TxOutput(amt, Script.p2pkh_locking_from_address(addr))
                      for addr, amt in outputs]
        tx = Transaction(inputs=tx_inputs, outputs=tx_outputs,
                          locktime=locktime)
        return cls(tx)

    # ── Updater role ─────────────────────────────────────────────
    def add_utxo(self, input_idx: int, utxo: 'UTXOEntry'):
        """Add UTXO info to input (needed for signing)"""
        if input_idx < len(self.inputs):
            self.inputs[input_idx].utxo = utxo

    def add_bip32_derivation(self, input_idx: int,
                              pubkey: bytes, path: str):
        """Add BIP32 derivation path for a key"""
        if input_idx < len(self.inputs):
            self.inputs[input_idx].bip32_derivation[pubkey] = path

    # ── Signer role ──────────────────────────────────────────────
    def sign(self, privkey: int, input_idx: int) -> bool:
        """Sign one input"""
        if input_idx >= len(self.inputs):
            return False
        psbt_in = self.inputs[input_idx]
        if psbt_in.is_finalized:
            return False

        utxo = psbt_in.utxo
        if not utxo:
            return False

        sighash = self.tx.signature_hash(
            input_idx, utxo.script_pubkey, psbt_in.sighash_type)
        r, s    = Secp256k1.sign(privkey, sighash)
        sig_der = Secp256k1.sig_to_der(r, s) + bytes([psbt_in.sighash_type])
        pub     = Secp256k1.pubkey_to_bytes(
                      Secp256k1.point_mul(privkey, Secp256k1.G()))
        psbt_in.add_partial_sig(pub, sig_der)
        return True

    def sign_all(self, privkey: int) -> int:
        """Sign all inputs with given key. Returns signed count."""
        count = 0
        for i in range(len(self.inputs)):
            if self.sign(privkey, i):
                count += 1
        return count

    # ── Combiner role ────────────────────────────────────────────
    def combine(self, other: 'PartiallySignedTransaction') -> bool:
        """Merge partial signatures from another PSBT"""
        if len(self.inputs) != len(other.inputs):
            return False
        for i, (inp, other_inp) in enumerate(zip(self.inputs, other.inputs)):
            inp.partial_sigs.update(other_inp.partial_sigs)
        return True

    # ── Finalizer role ───────────────────────────────────────────
    def finalize(self) -> bool:
        """Finalize all inputs"""
        for i, inp in enumerate(self.inputs):
            if not inp.partial_sigs:
                return False
            # Use first sig (P2PKH)
            pub, sig = next(iter(inp.partial_sigs.items()))
            script_sig = bytes([len(sig)]) + sig + bytes([len(pub)]) + pub
            inp.finalize(script_sig)
        return True

    # ── Extractor role ───────────────────────────────────────────
    def extract(self) -> Optional['Transaction']:
        """Extract final signed transaction"""
        if not all(inp.is_finalized for inp in self.inputs):
            return None
        for i, inp in enumerate(self.inputs):
            if inp.final_scriptsig:
                self.tx.inputs[i].script_sig = inp.final_scriptsig
        return self.tx

    # ── Serialization ────────────────────────────────────────────
    def to_dict(self) -> dict:
        return {
            "inputs"     : [inp.to_dict() for inp in self.inputs],
            "outputs"    : len(self.outputs),
            "finalized"  : all(i.is_finalized for i in self.inputs),
            "signed_inputs": sum(1 for i in self.inputs if i.partial_sigs),
        }

    def to_base64(self) -> str:
        """Serialize to base64 for QR/transport"""
        import base64
        data = json.dumps(self.to_dict(), default=str)
        return base64.b64encode(data.encode()).decode()

    @classmethod
    def from_base64(cls, b64: str) -> Optional['PartiallySignedTransaction']:
        """Deserialize from base64"""
        import base64
        try:
            data = json.loads(base64.b64decode(b64))
            psbt = cls()
            return psbt
        except Exception:
            return None

# ---- AirGappedSigner  (kind C, v10.18 lines 41558-41597) ----
class AirGappedSigner:
    """
    Air-gapped signing workflow.
    Hot wallet creates PSBT → transfer to offline device (USB/QR) →
    cold wallet signs → transfer back → broadcast.
    """

    def __init__(self, privkeys: List[int]):
        self.privkeys = privkeys

    def sign_psbt(self, psbt: PartiallySignedTransaction) -> int:
        """Sign all inputs we have keys for"""
        count = 0
        for privkey in self.privkeys:
            count += psbt.sign_all(privkey)
        return count

    def sign_from_base64(self, psbt_b64: str) -> str:
        """Sign PSBT from base64, return signed base64"""
        psbt = PartiallySignedTransaction.from_base64(psbt_b64)
        if psbt:
            self.sign_psbt(psbt)
            return psbt.to_base64()
        return psbt_b64

    @staticmethod
    def workflow_example() -> str:
        """Show air-gapped signing workflow"""
        return """
Air-Gapped Signing Workflow:
  1. Online device  → Create PSBT (unsigned tx)
  2. Online device  → Export PSBT as QR or USB file
  3. Offline device → Import PSBT
  4. Offline device → Sign PSBT with cold keys
  5. Offline device → Export signed PSBT as QR or USB
  6. Online device  → Import signed PSBT
  7. Online device  → Finalize + Broadcast

Security: Private keys NEVER touch internet-connected device.
        """

# ---- CoinPool  (kind C, v10.18 lines 41682-41728) ----
@dataclass
class CoinPool:
    """
    CTV-based Coin Pool (payment pool).
    Allows N users to share a UTXO and make payments atomically.
    More efficient than individual transactions.
    Uses a tree of CTV-locked transactions.
    """
    participants : List[str]   # addresses
    balances     : Dict[str, int]  # address → balance
    pool_script  : Optional[bytes] = None
    pool_address : Optional[str]   = None

    @classmethod
    def create(cls, participants: List[str],
                balances: Dict[str, int]) -> 'CoinPool':
        """Create a new coin pool"""
        pool = cls(participants=participants, balances=balances)
        # Pool address is a simple P2SH for now (CTV pending activation)
        pool_script = Script.p2pkh_locking_from_address(participants[0])
        pool.pool_script  = pool_script
        pool.pool_address = participants[0] if participants else ""
        return pool

    def total_balance(self) -> int:
        return sum(self.balances.values())

    def get_balance(self, address: str) -> int:
        return self.balances.get(address, 0)

    def pay(self, from_addr: str, to_addr: str,
             amount: int) -> bool:
        """Internal pool payment (off-chain)"""
        if self.balances.get(from_addr, 0) < amount:
            return False
        self.balances[from_addr] -= amount
        self.balances[to_addr]    = self.balances.get(to_addr, 0) + amount
        return True

    def to_dict(self) -> dict:
        return {
            "participants" : len(self.participants),
            "total_balance": self.total_balance() / 10**DECIMALS,
            "pool_address" : self.pool_address,
            "balances"     : {addr[:12]+"...": bal/10**DECIMALS
                              for addr, bal in self.balances.items()},
        }

# ---- InheritanceVault  (kind C, v10.18 lines 41730-41769) ----
class InheritanceVault:
    """
    CTV-based inheritance vault.
    Owner has immediate access. Heir gets access after delay.
    Uses CTV to pre-commit the inheritance transaction structure.
    """

    def __init__(self, owner_addr: str, heir_addr: str,
                  amount: int, delay_blocks: int = 26_280):  # 
        self.owner_addr   = owner_addr
        self.heir_addr    = heir_addr
        self.amount       = amount
        self.delay_blocks = delay_blocks

    def create_inheritance_tx(self) -> 'Transaction':
        """Pre-create the inheritance transaction (to be locked in CTV)"""
        heir_script = Script.p2pkh_locking_from_address(self.heir_addr)
        # This tx sends to heir after delay (via CSV in a second covenant)
        outputs = [TxOutput(self.amount - MIN_TX_FEE, heir_script)]
        return Transaction(
            inputs=[TxInput(OutPoint("0"*64, 0), b'', sequence=self.delay_blocks)],
            outputs=outputs)

    def vault_address(self) -> str:
        """Address that locks funds under this covenant"""
        inherit_tx  = self.create_inheritance_tx()
        covenant    = CheckTemplateVerify.create_covenant(inherit_tx, 0)
        h160        = hashlib.new('ripemd160',
                          hashlib.sha256(covenant).digest()).digest()
        return base58check_encode(h160, SCRIPT_ADDRESS_VERSION)

    def to_dict(self) -> dict:
        return {
            "owner"         : self.owner_addr,
            "heir"          : self.heir_addr,
            "amount_nbl"    : self.amount / 10**DECIMALS,
            "delay_blocks"  : self.delay_blocks,
            "delay_days"    : self.delay_blocks * TARGET_BLOCK_TIME / 86400,
            "vault_address" : self.vault_address(),
        }

# ---- BlockchainMessage  (kind C, v10.18 lines 42991-43035) ----
class BlockchainMessage:
    """Message stored on NEBULA blockchain via OP_RETURN"""

    MAX_SIZE = 80   # OP_RETURN data limit in bytes

    def __init__(self, sender: str, recipient_pubkey: bytes,
                  content: str, timestamp: float = None):
        self.sender          = sender
        self.recipient_pubkey= recipient_pubkey
        self.content         = content
        self.timestamp       = timestamp or time.time()
        self._encrypted      : Optional[bytes] = None

    def encrypt(self) -> bytes:
        """Encrypt message for recipient"""
        self._encrypted = ECIES.encrypt(
            self.content.encode('utf-8'), self.recipient_pubkey)
        return self._encrypted

    def to_op_return(self) -> bytes:
        """Pack message into OP_RETURN data"""
        enc = self.encrypt()
        # Prefix with message type + truncate to MAX_SIZE
        return b'NBL\x01' + enc[:self.MAX_SIZE - 4]

    @classmethod
    def from_op_return(cls, data: bytes, privkey: int) -> Optional[str]:
        """Decode message from OP_RETURN"""
        if not data.startswith(b'NBL\x01'):
            return None
        payload = data[4:]
        try:
            decrypted = ECIES.decrypt(payload, privkey)
            return decrypted.decode('utf-8') if decrypted else None
        except Exception:
            return None

    def to_dict(self) -> dict:
        return {
            "sender"     : self.sender,
            "recipient"  : self.recipient_pubkey.hex()[:20] + "...",
            "preview"    : self.content[:40] + "..." if len(self.content) > 40 else self.content,
            "timestamp"  : self.timestamp,
            "encrypted"  : self._encrypted is not None,
        }

# ---- P2PMessenger  (kind C, v10.18 lines 43037-43094) ----
class P2PMessenger:
    """
    NEBULA P2P encrypted messaging system.
    Messages stored on-chain (OP_RETURN) or off-chain (direct P2P).
    """

    def __init__(self, blockchain: 'NEBULABlockchain', privkey: int):
        self.bc        = blockchain
        self.privkey   = privkey
        self.pubkey    = Secp256k1.pubkey_to_bytes(
                             Secp256k1.point_mul(privkey, Secp256k1.G()))
        self._inbox    : List[dict] = []
        self._outbox   : List[dict] = []
        self._lock     = threading.RLock()

    def send(self, recipient_pubkey: bytes,
              message: str) -> Tuple[bool, str]:
        """Send encrypted message"""
        msg = BlockchainMessage(
            sender          = Script.p2pkh_address(self.pubkey),
            recipient_pubkey= recipient_pubkey,
            content         = message,
        )
        op_return_data = msg.to_op_return()

        with self._lock:
            self._outbox.append({
                "to"        : recipient_pubkey.hex()[:20] + "...",
                "preview"   : message[:40],
                "timestamp" : time.time(),
                "status"    : "sent",
                "op_return" : op_return_data.hex(),
            })
        return True, f"Message queued ({len(op_return_data)} bytes)"

    def scan_inbox(self) -> List[dict]:
        """Scan blockchain for messages to our address"""
        for blk in self.bc._chain:
            for tx in blk.transactions:
                for out in tx.outputs:
                    if out.script_pubkey and out.script_pubkey[:2] == b'\x6a\x4c':
                        data    = out.script_pubkey[3:]
                        decoded = BlockchainMessage.from_op_return(data, self.privkey)
                        if decoded:
                            with self._lock:
                                self._inbox.append({
                                    "content"  : decoded,
                                    "block"    : blk.height,
                                    "txid"     : tx.txid[:16] + "...",
                                    "timestamp": blk.header.timestamp,
                                })
        return self._inbox

    def inbox(self) -> List[dict]:
        return list(self._inbox)

    def outbox(self) -> List[dict]:
        return list(self._outbox)

# ---- ConfidentialTx  (kind C, v10.18 lines 43462-43510) ----
class ConfidentialTx:
    """
    Confidential transaction: hides amounts using Pedersen commitments.
    Verifiers can check that inputs = outputs (no inflation) without
    learning any specific amounts.
    """

    def __init__(self):
        self.input_commitments  : List[bytes] = []
        self.output_commitments : List[bytes] = []
        self.input_blindings    : List[int]   = []
        self.output_blindings   : List[int]   = []
        self.range_proofs       : List[dict]  = []

    def add_input(self, amount: int) -> bytes:
        """Add input with commitment"""
        c, r = PedersenCommitment.commit(amount)
        self.input_commitments.append(c)
        self.input_blindings.append(r)
        return c

    def add_output(self, amount: int) -> bytes:
        """Add output with commitment and range proof"""
        c, r = PedersenCommitment.commit(amount)
        self.output_commitments.append(c)
        self.output_blindings.append(r)
        # Range proof: amount is non-negative and fits in 64 bits
        rp = RangeProof(64).prove(amount, r)
        self.range_proofs.append(rp)
        return c

    def balance_check(self) -> bool:
        """Verify inputs = outputs (no new coins)"""
        excess = (sum(self.input_blindings) -
                  sum(self.output_blindings)) % Secp256k1.N
        return PedersenCommitment.verify_sum(
            self.input_commitments,
            self.output_commitments,
            excess)

    def verify_range_proofs(self) -> bool:
        """Verify all output range proofs"""
        return all(
            RangeProof(64).verify(rp, bytes.fromhex(rp["commitment"]))
            for rp in self.range_proofs
        )

    def is_valid(self) -> bool:
        return self.balance_check() and self.verify_range_proofs()

# ---- NEBULANodeEnhanced  (kind C, v10.18 lines 43522-43687) ----
class NEBULANodeEnhanced:
    """
    Enhanced NEBULA Full Node.
    Integrates all 50 modules into a unified node.
    """

    VERSION     = "1.0.0"
    CODENAME    = "NEBULA Genesis"

    def __init__(self, data_dir: str = "./nebula_data",
                 rpc_port: int = RPC_DEFAULT_PORT,
                 p2p_port: int = DEFAULT_PORT,
                 privacy_level: str = "mixed"):
        print(f"\n{'='*60}")
        print(f"  🌌 NEBULA Enhanced Node v{self.VERSION}")
        print(f"  Codename: {self.CODENAME}")
        print(f"  Author  : NEBULA Core Team")
        print(f"{'='*60}\n")

        # Core blockchain
        self.bc             = NEBULABlockchain()
        self.data_dir       = data_dir

        # Modules
        self.mempool        = AdvancedMempool(self.bc.utxo)
        self.ibd            = IBDManager(self.bc)
        self.checkpoints    = CheckpointValidator()
        self.filter_index   = CompactFilterIndex()
        self.version_bits   = VersionBitsState()
        self.staking        = StakingEngine(self.bc)
        self.governance     = GovernanceEngine(self.bc, self.staking)
        self.amm            = AMMEngine(self.bc)
        self.oracle         = PriceOracle(self.bc)
        self.analytics      = AnalyticsDashboard(self.bc)
        self.address_book   = AddressBook(f"{data_dir}/addresses.json")
        self.watchdog       = NodeWatchdog(self.bc)
        self.privacy_mgr    = PrivacyConnectionManager(
                                  PrivacyLevel.MIXED)
        self.addr_mgr       = PrivacyAwareAddrManager()
        self.eviction_mgr   = PeerEvictionManager()
        self.asn_diversity  = ASNDiversityManager()
        self.filter_mgr     = CompactFilterIndex()
        self.rpc_server     = NEBULAJSONRPCServerLegacy(
                                  self.bc, port=rpc_port)
        self.htlc_manager   = HTLCManager()
        self.swap_engine    = AtomicSwapEngine(self.bc)
        self.wallet_mgr     = None    # initialized on demand
        self._running       = False
        self._start_time    = time.time()
        self._threads       : List[threading.Thread] = []

    def start(self, mine: bool = False,
               miner_address: str = None):
        """Start the enhanced node"""
        self._running = True
        print("  📂 Loading blockchain...")
        try:
            self.bc.load(self.data_dir)
        except Exception:
            pass

        # Start subsystems
        self.oracle.start()
        self.watchdog.start()

        # Start RPC server
        try:
            self.rpc_server.start()
        except Exception as e:
            print(f"  ⚠️  RPC: {e}")

        # Optionally start miner
        if mine and miner_address:
            self._start_miner(miner_address)

        print(f"\n  ✅ NEBULA Node started!")
        print(f"  Chain height : {self.bc.height}")
        print(f"  UTXOs        : {self.bc.utxo.size():,}")
        print(f"  RPC          : http://127.0.0.1:{self.rpc_server.port}")
        print(f"  Data dir     : {self.data_dir}")
        print(f"\n  Modules loaded: 50")
        print(f"  {'─'*40}")
        self._print_module_list()

    def _print_module_list(self):
        modules = [
            "nebula_core", "nebula_wallet", "nebula_miner",
            "nebula_network", "nebula_node", "nebula_security",
            "nebula_contracts", "nebula_tests", "nebula_cli",
            "nebula_api", "nebula_server", "nebula_segwit",
            "nebula_lightning", "nebula_stratum", "nebula_storage",
            "nebula_bip324", "nebula_explorer", "nebula_privacy",
            "nebula_musig2", "nebula_mempool_adv", "nebula_spv",
            "nebula_jsonrpc", "nebula_descriptor", "nebula_ibd",
            "nebula_addrbook", "nebula_bip85", "nebula_analytics",
            "nebula_multisig", "nebula_watchdog", "nebula_p2p_adv",
            "nebula_wallet_ui", "nebula_rpc_client", "nebula_adaptor",
            "nebula_utxo_snap", "nebula_simulator", "nebula_script",
            "nebula_txbuilder", "nebula_timelock", "nebula_upgrades",
            "nebula_feebumper", "nebula_cold_storage","nebula_covenant",
            "nebula_staking", "nebula_crosschain", "nebula_oracle",
            "nebula_defi", "nebula_messaging", "nebula_governance",
            "nebula_zkproofs", "nebula_enhanced",
        ]
        for i, m in enumerate(modules, 1):
            print(f"  [{i:>2}] {m}")

    def _start_miner(self, address: str):
        """Start background miner"""
        def _mine():
            miner = NEBULAMiner(self.bc, address)
            while self._running:
                try:
                    miner.mine_one_block()
                except Exception:
                    time.sleep(1)
        t = threading.Thread(target=_mine, daemon=True, name="Miner")
        t.start()
        self._threads.append(t)

    def stop(self):
        """Stop all subsystems"""
        self._running = False
        self.oracle.stop()
        self.watchdog.stop()
        self.rpc_server.stop()
        try:
            self.bc.save(self.data_dir)
            print("  💾 Blockchain saved")
        except Exception:
            pass
        print("  👋 Node stopped")

    def status(self) -> dict:
        """Full node status"""
        uptime = time.time() - self._start_time
        nbl_price = self.oracle.get_nbl_usd()
        return {
            "version"      : self.VERSION,
            "codename"     : self.CODENAME,
            "height"       : self.bc.height,
            "utxos"        : self.bc.utxo.size(),
            "mempool_txs"  : self.bc.mempool.size(),
            "stakers"      : len(self.staking._stakes),
            "validators"   : len(self.staking._validators),
            "amm_pools"    : len(self.amm._pools),
            "amm_tvl"      : self.amm.total_tvl(),
            "proposals"    : len(self.governance._proposals),
            "nbl_usd"      : nbl_price,
            "uptime_secs"  : round(uptime),
            "uptime_human" : f"{uptime//3600:.0f}h {(uptime%3600)//60:.0f}m",
            "modules"      : 50,
            "rpc_port"     : self.rpc_server.port,
            "watchdog"     : self.watchdog.health_report(),
        }

    def defi_stats(self) -> dict:
        return {
            "amm"      : {"pools": len(self.amm._pools), "tvl": self.amm.total_tvl()},
            "staking"  : self.staking.network_stats(),
            "lending"  : {},
            "oracle"   : {pair: self.oracle.aggregator.get_price_report(pair)
                          for pair in ["NBL/USD", "NBL/BTC"]},
            "swaps"    : self.swap_engine.stats(),
            "governance": self.governance.stats(),
        }

# ---- BridgeTxStatusV2  (kind C, v10.18 lines 45575-45580) ----
class BridgeTxStatusV2(Enum):
    PENDING     = "pending"
    CONFIRMED   = "confirmed"
    COMPLETED   = "completed"
    FAILED      = "failed"
    REFUNDED    = "refunded"

# ---- SpendingRule  (kind C, v10.18 lines 46164-46186) ----
@dataclass
class SpendingRule:
    """A spending rule for smart wallet"""
    daily_limit     : int        # max spend per day in Neb
    per_tx_limit    : int        # max per transaction
    whitelist       : Set[str]   = field(default_factory=set)
    blacklist       : Set[str]   = field(default_factory=set)
    require_2fa     : bool       = False
    freeze_until    : float      = 0.0   # timestamp

    def can_spend(self, amount: int, to_addr: str,
                   current_spent_today: int) -> Tuple[bool, str]:
        if time.time() < self.freeze_until:
            return False, f"Wallet frozen until {self.freeze_until:.0f}"
        if self.blacklist and to_addr in self.blacklist:
            return False, f"Address blacklisted"
        if self.whitelist and to_addr not in self.whitelist:
            return False, f"Address not whitelisted"
        if amount > self.per_tx_limit:
            return False, f"Exceeds per-tx limit: {self.per_tx_limit/10**DECIMALS}"
        if current_spent_today + amount > self.daily_limit:
            return False, f"Exceeds daily limit: {self.daily_limit/10**DECIMALS}"
        return True, "OK"

# ---- SmartWallet  (kind C, v10.18 lines 46188-46309) ----
class SmartWallet:
    """
    Smart Wallet with account abstraction features.
    Guardian-based social recovery, spending limits,
    transaction batching, auto-approve whitelist.
    """

    def __init__(self, owner_privkey: int,
                  blockchain: 'NEBULABlockchain'):
        self.privkey    = owner_privkey
        self.pubkey     = Secp256k1.pubkey_to_bytes(
                              Secp256k1.point_mul(owner_privkey, Secp256k1.G()))
        self.address    = Script.p2pkh_address(self.pubkey)
        self.bc         = blockchain
        self.guardians  : List[str] = []   # guardian addresses
        self.rules      = SpendingRule(
            daily_limit  = 1000 * 10**DECIMALS,
            per_tx_limit = 100  * 10**DECIMALS,
        )
        self._daily_spent   = 0
        self._last_reset    = time.time()
        self._pending_batch : List[Tuple[str, int]] = []
        self._lock          = threading.RLock()

    def add_guardian(self, guardian_addr: str) -> bool:
        """Add a social recovery guardian"""
        if len(self.guardians) >= 5:
            return False
        self.guardians.append(guardian_addr)
        return True

    def remove_guardian(self, guardian_addr: str) -> bool:
        if guardian_addr in self.guardians:
            self.guardians.remove(guardian_addr)
            return True
        return False

    def set_daily_limit(self, limit_nbl: float):
        """Set daily spending limit"""
        self.rules.daily_limit = int(limit_nbl * 10**DECIMALS)

    def whitelist_address(self, address: str):
        """Add address to whitelist (no limit checks)"""
        self.rules.whitelist.add(address)

    def freeze(self, hours: float):
        """Freeze wallet for N hours"""
        self.rules.freeze_until = time.time() + hours * 3600

    def _reset_daily_if_needed(self):
        """Reset daily spending counter if new day"""
        if time.time() - self._last_reset > 86400:
            self._daily_spent = 0
            self._last_reset  = time.time()

    def send(self, to_addr: str, amount_nbl: float) -> Tuple[bool, str]:
        """Send NBL with smart wallet rules enforced"""
        amount = int(amount_nbl * 10**DECIMALS)
        with self._lock:
            self._reset_daily_if_needed()
            ok, reason = self.rules.can_spend(amount, to_addr, self._daily_spent)
            if not ok:
                return False, f"Rule violation: {reason}"

            builder = TxBuilder(self.bc.utxo)
            builder.add_output(to_addr, amount_nbl)
            builder.set_change_address(self.address)
            tx = builder.build(self.address, self.privkey)
            if not tx:
                return False, "Insufficient balance"

            ok2, msg = self.bc.mempool.submit(tx)
            if ok2:
                self._daily_spent += amount
            return ok2, msg

    def batch_send(self, outputs: List[Tuple[str, float]]) -> Tuple[bool, str]:
        """Send to multiple addresses in one transaction"""
        total = sum(int(a * 10**DECIMALS) for _, a in outputs)
        with self._lock:
            self._reset_daily_if_needed()
            if total > self.rules.daily_limit - self._daily_spent:
                return False, "Batch exceeds daily limit"

            builder = TxBuilder(self.bc.utxo)
            for addr, amt in outputs:
                builder.add_output(addr, amt)
            builder.set_change_address(self.address)
            tx = builder.build(self.address, self.privkey)
            if not tx:
                return False, "Insufficient balance"

            ok, msg = self.bc.mempool.submit(tx)
            if ok:
                self._daily_spent += total
            return ok, msg

    def initiate_recovery(self, new_owner_addr: str,
                           approving_guardians: List[str]) -> Tuple[bool, str]:
        """
        Social recovery: requires majority of guardians to approve.
        """
        if not self.guardians:
            return False, "No guardians configured"
        threshold  = len(self.guardians) // 2 + 1
        approvals  = sum(1 for g in approving_guardians if g in self.guardians)
        if approvals < threshold:
            return False, f"Need {threshold} guardians, got {approvals}"
        return True, f"Recovery initiated. New owner: {new_owner_addr}"

    def status(self) -> dict:
        self._reset_daily_if_needed()
        return {
            "address"          : self.address,
            "balance_nbl"      : self.bc.utxo.balance(self.address) / 10**DECIMALS,
            "daily_limit_nbl"  : self.rules.daily_limit / 10**DECIMALS,
            "daily_spent_nbl"  : self._daily_spent / 10**DECIMALS,
            "remaining_today"  : (self.rules.daily_limit - self._daily_spent) / 10**DECIMALS,
            "guardians"        : len(self.guardians),
            "whitelisted"      : len(self.rules.whitelist),
            "frozen"           : time.time() < self.rules.freeze_until,
        }

# ---- MempoolRPCExtensions  (kind C, v10.18 lines 46319-46396) ----
class MempoolRPCExtensions:
    """
    Extended mempool RPC methods for wallets and tools.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 fee_bumper: 'FeeBumper' = None):
        self.bc          = blockchain
        self.fee_bumper  = fee_bumper
        self.visualizer  = MempoolVisualizer(blockchain)

    def get_fee_estimates(self) -> dict:
        """Get fee estimates for various confirmation targets"""
        mempool = self.bc.mempool
        if hasattr(mempool, 'fee_estimates'):
            estimates = mempool.fee_estimates()
        else:
            estimates = {f"{n} blocks": MIN_TX_FEE // 10**DECIMALS
                         for n in [1, 3, 6, 12, 24, 48, 144, 504, 1008]}

        return {
            "estimates"      : estimates,
            "unit"           : "NBL/byte",
            "mempool_min"    : MIN_TX_FEE / 10**DECIMALS,
            "congestion"     : self.visualizer.congestion_level(),
            "next_block"     : self.visualizer.next_block_estimate(),
        }

    def get_mempool_heatmap(self) -> dict:
        return self.visualizer.full_report()

    def test_replace_by_fee(self, txid: str,
                             new_fee_rate: int) -> dict:
        """Check if a tx can be replaced by fee"""
        entry = (self.bc.mempool._txs.get(txid)
                 if hasattr(self.bc.mempool, '_txs') else None)
        if not entry:
            return {"can_rbf": False, "reason": "Not in mempool"}

        signals_rbf = getattr(entry, 'is_rbf', False)
        current_rate = getattr(entry, 'fee_rate', 0)

        return {
            "txid"         : txid,
            "signals_rbf"  : signals_rbf,
            "current_rate" : current_rate,
            "proposed_rate": new_fee_rate,
            "can_rbf"      : signals_rbf and new_fee_rate > current_rate * 1.1,
            "min_new_fee"  : current_rate * 1.1,
        }

    def package_relay_info(self) -> dict:
        """Info about package relay support"""
        return {
            "supported"         : True,
            "max_package_count" : MAX_PACKAGE_COUNT if 'MAX_PACKAGE_COUNT' in dir() else 25,
            "max_package_size"  : MAX_PACKAGE_SIZE if 'MAX_PACKAGE_SIZE' in dir() else 101000,
            "cpfp_supported"    : True,
            "rbf_supported"     : True,
        }

    def estimate_vsize(self, n_inputs: int = 1,
                        n_outputs: int = 2,
                        script_type: str = "p2pkh") -> dict:
        """Estimate transaction virtual size"""
        overhead = 10
        input_sizes  = {"p2pkh": 148, "p2wpkh": 68, "p2sh": 92, "p2tr": 58}
        output_sizes = {"p2pkh": 34,  "p2wpkh": 31, "p2sh": 32, "p2tr": 43}
        in_size  = input_sizes.get(script_type, 148)
        out_size = output_sizes.get(script_type, 34)
        vsize    = overhead + n_inputs * in_size + n_outputs * out_size
        return {
            "vsize"          : vsize,
            "weight"         : vsize * 4,
            "fee_at_1sat"    : vsize,
            "fee_at_10sat"   : vsize * 10,
            "fee_at_100sat"  : vsize * 100,
        }

# ---- BulkAddressGenerator  (kind C, v10.18 lines 46612-46717) ----
class BulkAddressGenerator:
    """
    Generate large batches of NEBULA addresses efficiently.
    Used by: exchanges, payment processors, airdrop tools.
    """

    def __init__(self, master_key: 'HDKey'):
        self.master = master_key

    def generate_sequential(self, account: int = 0,
                              start: int = 0,
                              count: int = 100,
                              change: bool = False) -> List[dict]:
        """Generate sequential BIP44 addresses"""
        chain  = 1 if change else 0
        result = []
        for i in range(start, start + count):
            path = f"{NBL_BIP44_PATH}/{account}'/{chain}/{i}"
            try:
                child = self.master.derive_path(path)
                result.append({
                    "index"  : i,
                    "path"   : path,
                    "address": child.address,
                    "pubkey" : Secp256k1.pubkey_to_bytes(
                                   Secp256k1.point_mul(child.privkey,
                                   Secp256k1.G())).hex()[:20] + "...",
                })
            except Exception:
                pass
        return result

    def generate_random(self, count: int = 10) -> List[dict]:
        """Generate random addresses (for testing)"""
        result = []
        for _ in range(count):
            privkey = int.from_bytes(secrets.token_bytes(32), 'big') % Secp256k1.N
            pubkey  = Secp256k1.pubkey_to_bytes(
                          Secp256k1.point_mul(privkey, Secp256k1.G()))
            result.append({
                "address": Script.p2pkh_address(pubkey),
                "wif"    : HDKey(privkey, b'\x00'*32, None).wif,
            })
        return result

    def vanity_address(self, prefix: str, max_attempts: int = 100_000,
                        timeout_secs: float = 30.0) -> Optional[dict]:
        """
        Find address starting with given prefix.
        WARNING: exponential time — max 6 chars practical.
        """
        import time
        start = time.time()
        for attempt in range(max_attempts):
            if time.time() - start > timeout_secs:
                break
            privkey = int.from_bytes(secrets.token_bytes(32), 'big') % Secp256k1.N
            pubkey  = Secp256k1.pubkey_to_bytes(
                          Secp256k1.point_mul(privkey, Secp256k1.G()))
            addr    = Script.p2pkh_address(pubkey)
            if addr[1:].startswith(prefix):   # skip version byte prefix
                return {
                    "address"  : addr,
                    "prefix"   : prefix,
                    "attempts" : attempt + 1,
                    "wif"      : HDKey(privkey, b'\x00'*32, None).wif,
                }
        return None

    def generate_multisig_addresses(self, n_keys: int = 3,
                                     threshold: int = 2,
                                     count: int = 10) -> List[dict]:
        """Generate threshold multisig addresses"""
        result = []
        for i in range(count):
            privkeys = [
                self.master.derive_path(f"{NBL_BIP44_PATH}/0'/{j}/{i}").privkey
                for j in range(n_keys)
            ]
            pubkeys  = [Secp256k1.pubkey_to_bytes(
                            Secp256k1.point_mul(pk, Secp256k1.G()))
                        for pk in privkeys]
            ms  = MultisigWallet(threshold, pubkeys)
            result.append({
                "index"     : i,
                "type"      : f"{threshold}-of-{n_keys}",
                "address"   : ms.address(),
                "pubkeys"   : [pk.hex()[:16]+"..." for pk in pubkeys],
            })
        return result

    @staticmethod
    def validate_address(address: str) -> dict:
        """Validate a NEBULA address"""
        try:
            version, payload = base58check_decode(address)
            valid  = version == PUBKEY_ADDRESS_VERSION and len(payload) == 20
            return {
                "address"  : address,
                "valid"    : valid,
                "version"  : version,
                "type"     : "P2PKH" if version == PUBKEY_ADDRESS_VERSION else "P2SH",
                "hash160"  : payload.hex() if valid else "",
            }
        except Exception as e:
            return {"address": address, "valid": False, "error": str(e)}


# ======== Second removal pass: 8 classes judged redundant with wired live classes ========
# ---- ContractError  (kind D, lines 31099-31101 before this pass) ----
class ContractError(Exception):
    """Base exception for smart contract execution errors (out of gas, slippage, etc.)"""
    pass

# ---- TokenPair  (kind D, lines 31712-31724 before this pass) ----
@dataclass
class TokenPair:
    token0  : str    # contract address or "NBL" for native
    token1  : str
    fee_tier: int = DEX_FEE_RATE   # basis points * 100

    @property
    def pair_id(self) -> str:
        t0, t1 = sorted([self.token0, self.token1])
        return f"{t0}/{t1}"

    def __hash__(self):
        return hash(self.pair_id)

# ---- LiquidityPoolSimple  (kind D, lines 31727-31947 before this pass) ----
class LiquidityPoolSimple:
    """
    Uniswap v2-style constant product AMM (x * y = k).
    Supports: add/remove liquidity, swap, price queries.
    Tracks TWAP oracle for resistance to price manipulation.
    """

    def __init__(self, pair: TokenPair,
                 registry: 'ContractRegistry' = None):
        self.pair       = pair
        self.registry   = registry
        self.address    = contract_address(pair.token0, hash(pair.pair_id) % 10**6)
        self.reserve0   = 0      # token0 reserve
        self.reserve1   = 0      # token1 reserve
        self.total_lp   = 0      # total LP tokens
        self._lp_balances: Dict[str, int] = {}
        self._fee_acc0  = 0      # accumulated fees token0
        self._fee_acc1  = 0      # accumulated fees token1
        self._lock      = threading.Lock()
        self._price_cumulative0 = 0
        self._price_cumulative1 = 0
        self._last_block_time   = 0
        self._price_history     : List[Tuple[float, float, float]] = []  # (time, p0, p1)
        self._swap_count        = 0
        self._volume0           = 0
        self._volume1           = 0

    @property
    def k(self) -> int:
        """Constant product invariant"""
        return self.reserve0 * self.reserve1

    def price_token0_in_token1(self) -> float:
        """Current spot price of token0 denominated in token1"""
        if self.reserve0 == 0: return 0
        return self.reserve1 / self.reserve0

    def price_token1_in_token0(self) -> float:
        if self.reserve1 == 0: return 0
        return self.reserve0 / self.reserve1

    def get_amount_out(self, amount_in: int,
                        reserve_in: int, reserve_out: int) -> int:
        """
        Constant product formula with fee.
        amount_out = (amount_in * (10000 - fee) * reserve_out) /
                     (reserve_in * 10000 + amount_in * (10000 - fee))
        """
        if amount_in <= 0 or reserve_in <= 0 or reserve_out <= 0:
            return 0
        fee      = self.pair.fee_tier
        amount_in_with_fee = amount_in * (10000 - fee)
        numerator   = amount_in_with_fee * reserve_out
        denominator = reserve_in * 10000 + amount_in_with_fee
        return numerator // denominator

    def get_amount_in(self, amount_out: int,
                       reserve_in: int, reserve_out: int) -> int:
        """Calculate required input for desired output"""
        if amount_out <= 0 or reserve_out <= amount_out:
            return 0
        fee = self.pair.fee_tier
        numerator   = reserve_in * amount_out * 10000
        denominator = (reserve_out - amount_out) * (10000 - fee)
        return numerator // denominator + 1

    def add_liquidity(self, provider: str,
                       amount0_desired: int,
                       amount1_desired: int,
                       min0: int = 0, min1: int = 0) -> Tuple[int, int, int]:
        """
        Add liquidity to pool.
        Returns (actual_amount0, actual_amount1, lp_tokens_minted).
        """
        with self._lock:
            if self.total_lp == 0:
                # First liquidity — geometric mean
                lp = int(math.sqrt(amount0_desired * amount1_desired)) - MIN_LIQUIDITY
                if lp <= 0:
                    raise ContractError("Insufficient initial liquidity")
                actual0, actual1 = amount0_desired, amount1_desired
                # Lock MIN_LIQUIDITY permanently
                self._lp_balances["0x000000"] = MIN_LIQUIDITY
                self.total_lp = MIN_LIQUIDITY
            else:
                # Maintain ratio
                amount1_optimal = amount0_desired * self.reserve1 // self.reserve0
                if amount1_optimal <= amount1_desired:
                    actual0, actual1 = amount0_desired, amount1_optimal
                else:
                    amount0_optimal = amount1_desired * self.reserve0 // self.reserve1
                    actual0, actual1 = amount0_optimal, amount1_desired

                if actual0 < min0 or actual1 < min1:
                    raise ContractError("Slippage exceeded")

                lp = min(
                    actual0 * self.total_lp // self.reserve0,
                    actual1 * self.total_lp // self.reserve1
                )

            self.reserve0 += actual0
            self.reserve1 += actual1
            self.total_lp += lp
            self._lp_balances[provider] = self._lp_balances.get(provider, 0) + lp
            return actual0, actual1, lp

    def remove_liquidity(self, provider: str,
                          lp_amount: int,
                          min0: int = 0, min1: int = 0) -> Tuple[int, int]:
        """
        Remove liquidity from pool.
        Returns (amount0, amount1) returned to provider.
        """
        with self._lock:
            if self._lp_balances.get(provider, 0) < lp_amount:
                raise ContractError("Insufficient LP tokens")
            if self.total_lp == 0:
                return 0, 0

            amount0 = lp_amount * self.reserve0 // self.total_lp
            amount1 = lp_amount * self.reserve1 // self.total_lp

            if amount0 < min0 or amount1 < min1:
                raise ContractError("Slippage exceeded")

            self.reserve0                 -= amount0
            self.reserve1                 -= amount1
            self.total_lp                 -= lp_amount
            self._lp_balances[provider]   -= lp_amount
            return amount0, amount1

    def swap(self, caller: str, token_in: str, amount_in: int,
              min_out: int = 0) -> Tuple[int, str]:
        """
        Execute a swap.
        Returns (amount_out, token_out).
        """
        with self._lock:
            is_0_to_1 = (token_in == self.pair.token0)
            if is_0_to_1:
                amount_out = self.get_amount_out(amount_in, self.reserve0, self.reserve1)
                token_out  = self.pair.token1
            else:
                amount_out = self.get_amount_out(amount_in, self.reserve1, self.reserve0)
                token_out  = self.pair.token0

            if amount_out < min_out:
                raise ContractError(f"Slippage: {amount_out} < {min_out}")

            # Price impact check
            if amount_in > 0:
                impact = amount_in * 10000 // (self.reserve0 if is_0_to_1 else self.reserve1)
                if impact > MAX_PRICE_IMPACT:
                    raise ContractError(f"Price impact too high: {impact/100:.1f}%")

            # Update reserves
            if is_0_to_1:
                self.reserve0 += amount_in
                self.reserve1 -= amount_out
                self._volume0 += amount_in
            else:
                self.reserve1 += amount_in
                self.reserve0 -= amount_out
                self._volume1 += amount_in

            # Accumulate fees
            fee_amount = amount_in * DEX_FEE_RATE // 10000
            if is_0_to_1:
                self._fee_acc0 += fee_amount
            else:
                self._fee_acc1 += fee_amount

            self._swap_count += 1

            # Update price oracle
            now = time.time()
            self._price_history.append((now,
                                         self.price_token0_in_token1(),
                                         self.price_token1_in_token0()))
            if len(self._price_history) > 1000:
                self._price_history.pop(0)

            return amount_out, token_out

    def twap(self, window_seconds: float = ORACLE_WINDOW) -> Tuple[float, float]:
        """
        Time-Weighted Average Price over window.
        Returns (twap_0_in_1, twap_1_in_0).
        """
        cutoff = time.time() - window_seconds
        points = [(t, p0, p1) for t, p0, p1 in self._price_history
                  if t >= cutoff]
        if not points:
            return self.price_token0_in_token1(), self.price_token1_in_token0()
        avg0 = sum(p[1] for p in points) / len(points)
        avg1 = sum(p[2] for p in points) / len(points)
        return avg0, avg1

    def lp_balance(self, provider: str) -> int:
        return self._lp_balances.get(provider, 0)

    def pool_share(self, provider: str) -> float:
        if self.total_lp == 0: return 0
        return self._lp_balances.get(provider, 0) / self.total_lp

    def to_dict(self) -> dict:
        return {
            "pair"           : self.pair.pair_id,
            "address"        : self.address,
            "reserve0"       : self.reserve0,
            "reserve1"       : self.reserve1,
            "total_lp"       : self.total_lp,
            "price0"         : self.price_token0_in_token1(),
            "price1"         : self.price_token1_in_token0(),
            "volume0"        : self._volume0,
            "volume1"        : self._volume1,
            "swap_count"     : self._swap_count,
            "fee_tier_pct"   : self.pair.fee_tier / 100,
            "k"              : self.k,
        }

# ---- AtomicSwapProtocol  (kind D, lines 31953-32056 before this pass) ----
class AtomicSwapProtocol:
    """
    Hash Time Lock Contract (HTLC) atomic swap.
    Enables trustless cross-chain swaps.
    Party A locks funds with hash(secret).
    Party B locks funds with same hash.
    A reveals secret to claim B's funds.
    B uses revealed secret to claim A's funds.
    """

    @dataclass
    class HTLCContract:
        swap_id    : str
        initiator  : str
        participant: str
        token      : str
        amount     : int
        hash_lock  : bytes   # sha256 of secret
        time_lock  : float   # unix timestamp expiry
        is_claimed : bool = False
        is_refunded: bool = False
        secret     : Optional[bytes] = None

        @property
        def is_expired(self) -> bool:
            return time.time() > self.time_lock

        def to_dict(self) -> dict:
            return {
                "swap_id"     : self.swap_id,
                "initiator"   : self.initiator,
                "participant" : self.participant,
                "amount"      : self.amount,
                "hash_lock"   : self.hash_lock.hex(),
                "time_lock"   : self.time_lock,
                "is_claimed"  : self.is_claimed,
                "is_refunded" : self.is_refunded,
                "is_expired"  : self.is_expired,
            }

    def __init__(self):
        self._contracts : Dict[str, AtomicSwap.HTLCContract] = {}
        self._lock      = threading.Lock()

    def initiate(self, initiator: str, participant: str,
                  token: str, amount: int,
                  secret_hash: bytes,
                  time_lock_seconds: int = 3600) -> str:
        """Initiate HTLC. Returns swap_id."""
        swap_id = hashlib.sha256(
            initiator.encode() + participant.encode() +
            secret_hash + struct.pack('>I', int(time.time()))
        ).hexdigest()[:16]

        with self._lock:
            self._contracts[swap_id] = self.HTLCContract(
                swap_id    = swap_id,
                initiator  = initiator,
                participant= participant,
                token      = token,
                amount     = amount,
                hash_lock  = secret_hash,
                time_lock  = time.time() + time_lock_seconds,
            )
        return swap_id

    def claim(self, swap_id: str, claimer: str,
               secret: bytes) -> Tuple[bool, str]:
        """Claim HTLC using secret."""
        with self._lock:
            htlc = self._contracts.get(swap_id)
            if htlc is None:
                return False, "Swap not found"
            if htlc.is_claimed:
                return False, "Already claimed"
            if htlc.is_expired:
                return False, "Expired"
            if claimer != htlc.participant:
                return False, "Not participant"
            if hashlib.sha256(secret).digest() != htlc.hash_lock:
                return False, "Invalid secret"

            htlc.is_claimed = True
            htlc.secret     = secret
        return True, "Claimed"

    def refund(self, swap_id: str, initiator: str) -> Tuple[bool, str]:
        """Refund expired HTLC."""
        with self._lock:
            htlc = self._contracts.get(swap_id)
            if htlc is None: return False, "Not found"
            if htlc.is_claimed: return False, "Already claimed"
            if not htlc.is_expired: return False, "Not yet expired"
            if initiator != htlc.initiator: return False, "Not initiator"
            htlc.is_refunded = True
        return True, "Refunded"

    def get_swap(self, swap_id: str) -> Optional[dict]:
        htlc = self._contracts.get(swap_id)
        return htlc.to_dict() if htlc else None

    def active_swaps(self) -> List[dict]:
        return [h.to_dict() for h in self._contracts.values()
                if not h.is_claimed and not h.is_refunded]

# ---- DEXRouter  (kind D, lines 32059-32166 before this pass) ----
class DEXRouter:
    """
    Multi-hop DEX routing.
    Finds best path across multiple liquidity pools.
    Executes multi-hop swaps in a single transaction.
    """

    def __init__(self):
        self._pools      : Dict[str, LiquidityPool] = {}
        self._order_books: Dict[str, OrderBook]      = {}
        self._atomic     = AtomicSwapProtocol()
        self._lock       = threading.RLock()
        self._total_volume = 0
        self._total_fees   = 0
        self._swap_count   = 0

    def add_pool(self, pool: LiquidityPool):
        with self._lock:
            self._pools[pool.pair.pair_id] = pool

    def add_order_book(self, pair: str) -> OrderBook:
        ob = OrderBook(pair)
        with self._lock:
            self._order_books[pair] = ob
        return ob

    def get_pool(self, token0: str, token1: str) -> Optional[LiquidityPool]:
        pair_id = TokenPair(token0, token1).pair_id
        return self._pools.get(pair_id)

    def quote(self, token_in: str, token_out: str,
               amount_in: int) -> Tuple[int, List[str]]:
        """
        Get best quote for swap, possibly via multi-hop.
        Returns (amount_out, path).
        """
        # Direct route
        pool = self.get_pool(token_in, token_out)
        if pool:
            is_01 = (token_in == pool.pair.token0)
            res_in  = pool.reserve0 if is_01 else pool.reserve1
            res_out = pool.reserve1 if is_01 else pool.reserve0
            direct_out = pool.get_amount_out(amount_in, res_in, res_out)
            if direct_out > 0:
                return direct_out, [token_in, token_out]

        # Try NBL as intermediate
        if token_in != "NBL" and token_out != "NBL":
            pool_in  = self.get_pool(token_in, "NBL")
            pool_out = self.get_pool("NBL", token_out)
            if pool_in and pool_out:
                mid, _  = self.quote(token_in, "NBL", amount_in)
                if mid > 0:
                    final, _ = self.quote("NBL", token_out, mid)
                    if final > 0:
                        return final, [token_in, "NBL", token_out]

        return 0, []

    def swap_exact_in(self, caller: str, path: List[str],
                       amount_in: int, min_out: int = 0) -> Tuple[int, str]:
        """Execute multi-hop swap with exact input"""
        current_amount = amount_in
        current_token  = path[0]

        with self._lock:
            for i in range(1, len(path)):
                next_token = path[i]
                pool = self.get_pool(current_token, next_token)
                if pool is None:
                    return 0, f"No pool for {current_token}/{next_token}"

                out, tok_out = pool.swap(caller, current_token, current_amount, 0)
                current_amount = out
                current_token  = tok_out

            if current_amount < min_out:
                return 0, f"Slippage: {current_amount} < {min_out}"

            self._total_volume += amount_in
            self._swap_count   += 1

        return current_amount, "OK"

    def add_liquidity(self, provider: str,
                       token0: str, token1: str,
                       amount0: int, amount1: int) -> Tuple[int, int, int]:
        """Add liquidity, creating pool if needed"""
        pair = TokenPair(token0, token1)
        pool = self.get_pool(token0, token1)
        if pool is None:
            pool = LiquidityPoolSimple(pair)
            self.add_pool(pool)
        if token0 != pool.pair.token0:
            amount0, amount1 = amount1, amount0
        return pool.add_liquidity(provider, amount0, amount1)

    def all_pools(self) -> List[dict]:
        return [p.to_dict() for p in self._pools.values()]

    def dex_stats(self) -> dict:
        return {
            "pools"         : len(self._pools),
            "order_books"   : len(self._order_books),
            "total_swaps"   : self._swap_count,
            "total_volume"  : self._total_volume,
            "active_swaps"  : len(self._atomic.active_swaps()),
        }

# ---- ValidatorStatus  (kind D, lines 32353-32357 before this pass) ----
class ValidatorStatus(Enum):
    INACTIVE    = "inactive"
    ACTIVE      = "active"
    JAILED      = "jailed"
    TOMBSTONED  = "tombstoned"  # permanently removed

# ---- UnbondingEntry  (kind D, lines 32374-32381 before this pass) ----
@dataclass
class UnbondingEntry:
    delegator     : str
    validator     : str
    amount        : int
    completion_height: int
    start_height  : int
    created_at    : float = field(default_factory=time.time)

# ---- NEBULAStaking  (kind D, lines 32426-32640 before this pass) ----
class NEBULAStaking:
    """
    Full proof-of-stake layer for NEBULA.
    Validators register, delegators bond NBL to validators.
    Rewards distributed every epoch (100 blocks).
    Slashing for misbehavior.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc             = blockchain
        self._validators    : Dict[str, Validator] = {}
        self._pools         : Dict[str, StakingPool] = {}
        self._unbonding     : List[UnbondingEntry] = []
        self._evidences     : List[SlashingEvidence] = []
        self._total_staked  = 0
        self._epoch         = 0
        self._lock          = threading.RLock()

    def register_validator(self, address: str, pubkey: bytes,
                             moniker: str, commission: int,
                             self_stake: int) -> Tuple[bool, str]:
        """Register as a validator"""
        with self._lock:
            if address in self._validators:
                return False, "Already registered"
            bal = self.bc.utxo.balance(address)
            if bal < max(MIN_STAKE, self_stake):
                return False, f"Insufficient balance: {bal/10**DECIMALS} NBL"
            if self_stake < MIN_STAKE:
                return False, f"Min self-stake: {MIN_STAKE/10**DECIMALS} NBL"

            v = ValidatorC(
                address    = address,
                pubkey     = pubkey,
                moniker    = moniker,
                commission = commission,
                min_self_del = self_stake,
                stake      = self_stake,
                self_stake = self_stake,
                status     = ValidatorStatus.INACTIVE,
            )
            self._validators[address] = v
            self._pools[address]      = StakingPool(v)
            self._total_staked       += self_stake

            # Auto-activate if under max_validators
            if self._active_count() < MAX_VALIDATORS:
                v.status = ValidatorStatus.ACTIVE

        return True, "Registered"

    def _active_count(self) -> int:
        return sum(1 for v in self._validators.values()
                   if v.status == ValidatorStatus.ACTIVE)

    def delegate(self, delegator: str, validator_addr: str,
                  amount: int) -> Tuple[bool, str]:
        """Delegate NBL to a validator"""
        with self._lock:
            v = self._validators.get(validator_addr)
            if v is None: return False, "Validator not found"
            if v.status == ValidatorStatus.JAILED:
                return False, "Validator is jailed"
            if v.tombstoned:
                return False, "Validator is tombstoned"
            if amount < MIN_STAKE:
                return False, f"Min delegation: {MIN_STAKE/10**DECIMALS} NBL"
            if len(v._delegators) >= MAX_DELEGATORS:
                return False, "Validator at max delegators"
            bal = self.bc.utxo.balance(delegator)
            if bal < amount:
                return False, f"Insufficient balance: {bal/10**DECIMALS}"

            v.delegate(delegator, amount)
            self._total_staked += amount
        return True, f"Delegated {amount/10**DECIMALS} NBL to {v.moniker}"

    def undelegate(self, delegator: str, validator_addr: str,
                    amount: int) -> Tuple[bool, str]:
        """Begin undelegation (unbonding period applies)"""
        with self._lock:
            v = self._validators.get(validator_addr)
            if v is None: return False, "Validator not found"
            ok = v.undelegate(delegator, amount)
            if not ok: return False, "Insufficient delegation"

            # Queue unbonding
            entry = UnbondingEntry(
                delegator         = delegator,
                validator         = validator_addr,
                amount            = amount,
                completion_height = self.bc.height + UNBONDING_PERIOD,
                start_height      = self.bc.height,
            )
            self._unbonding.append(entry)
            self._total_staked -= amount
        return True, f"Unbonding {amount/10**DECIMALS} NBL (available in {UNBONDING_PERIOD} blocks)"

    def claim_rewards(self, delegator: str) -> int:
        """Claim all pending staking rewards"""
        total = 0
        with self._lock:
            for pool in self._pools.values():
                total += pool.claim_rewards(delegator)
        return total

    def process_epoch(self):
        """Called every EPOCH_LENGTH blocks to distribute rewards"""
        with self._lock:
            self._epoch += 1
            total_stake = max(1, self._total_staked)

            # Calculate epoch reward (annualized / epochs_per_year)
            epochs_per_year = 525600 / EPOCH_LENGTH  # blocks/min * min/year
            annual_reward   = total_stake * STAKING_REWARD_PCT // 100
            epoch_reward    = int(annual_reward / epochs_per_year)

            # Distribute to active validators proportionally
            for addr, pool in self._pools.items():
                v = pool.validator
                if v.status != ValidatorStatus.ACTIVE: continue
                v_share = epoch_reward * v.stake // total_stake
                pool.distribute_rewards(v_share, self._epoch)

    def process_block(self, height: int):
        """Called on each new block"""
        if height % EPOCH_LENGTH == 0:
            self.process_epoch()

        # Process completed unbondings
        with self._lock:
            completed = [e for e in self._unbonding
                         if e.completion_height <= height]
            for e in completed:
                self._unbonding.remove(e)
                # Funds returned automatically (in production: UTXO created)

    def submit_evidence(self, evidence: SlashingEvidence) -> Tuple[bool, str]:
        """Submit slashing evidence"""
        with self._lock:
            v = self._validators.get(evidence.validator)
            if v is None: return False, "Validator not found"

            self._evidences.append(evidence)

            if evidence.evidence_type == "double_sign":
                slash_amount = v.slash(SLASH_DOUBLE_SIGN)
                v.status     = ValidatorStatus.TOMBSTONED
                v.tombstoned = True
                return True, f"Slashed {slash_amount/10**DECIMALS} NBL and tombstoned"

            elif evidence.evidence_type == "downtime":
                slash_amount = v.slash(SLASH_DOWNTIME)
                v.status     = ValidatorStatus.JAILED
                v.jailed_until = self.bc.height + 28_800  # 2 days
                return True, f"Jailed and slashed {slash_amount/10**DECIMALS} NBL"

        return False, "Unknown evidence type"

    def unjail(self, validator_addr: str) -> Tuple[bool, str]:
        """Unjail a validator after jailing period"""
        with self._lock:
            v = self._validators.get(validator_addr)
            if v is None: return False, "Not found"
            if v.tombstoned: return False, "Tombstoned — cannot unjail"
            if v.status != ValidatorStatus.JAILED:
                return False, "Not jailed"
            if self.bc.height < v.jailed_until:
                return False, f"{v.jailed_until - self.bc.height} blocks until unjail"
            v.status = ValidatorStatus.ACTIVE
        return True, "Unjailed"

    def active_validators(self) -> List[dict]:
        return [v.to_dict() for v in self._validators.values()
                if v.status == ValidatorStatus.ACTIVE]

    def top_validators(self, n: int = 10) -> List[dict]:
        sorted_v = sorted(self._validators.values(),
                           key=lambda v: v.stake, reverse=True)
        return [v.to_dict() for v in sorted_v[:n]]

    def staking_stats(self) -> dict:
        active = self._active_count()
        return {
            "total_validators"   : len(self._validators),
            "active_validators"  : active,
            "total_staked_nbl"   : self._total_staked / 10**DECIMALS,
            "unbonding_entries"  : len(self._unbonding),
            "current_epoch"      : self._epoch,
            "slash_events"       : len(self._evidences),
            "min_stake_nbl"      : MIN_STAKE / 10**DECIMALS,
        }

    def delegator_summary(self, address: str) -> dict:
        delegations = {}
        total_del   = 0
        total_rewards = 0
        for addr, v in self._validators.items():
            del_amount = v._delegators.get(address, 0)
            if del_amount > 0:
                delegations[addr] = {
                    "validator"   : v.moniker,
                    "amount_nbl"  : del_amount / 10**DECIMALS,
                    "rewards_nbl" : self._pools[addr].pending_rewards(address) / 10**DECIMALS,
                    "status"      : v.status.value,
                }
                total_del     += del_amount
                total_rewards += self._pools[addr].pending_rewards(address)
        return {
            "address"       : address,
            "delegations"   : delegations,
            "total_del_nbl" : total_del / 10**DECIMALS,
            "total_rewards" : total_rewards / 10**DECIMALS,
            "unbonding"     : len([e for e in self._unbonding if e.delegator == address]),
        }

