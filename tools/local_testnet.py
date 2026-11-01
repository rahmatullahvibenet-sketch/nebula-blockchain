#!/usr/bin/env python3
"""NEBULA local testnet - 3 REAL nodes (own chain, own P2P socket, TLS 1.3) on this machine talking to each other.

    python3 tools/local_testnet.py            # full run (mines 101 blocks for coinbase maturity, then a real payment)
    python3 tools/local_testnet.py --quick    # skips the payment part (a few minutes less)

What it checks (all with REAL mined blocks and REAL signed transactions, no mocks):
  1  3 nodes connect over TLS            2  a block mined on A reaches B and C
  3  mining 101 blocks keeps all in sync 4  a signed payment sent via B reaches A and C's mempool
  5  the payment is mined by C and every node agrees on balances
  6  a brand new node D syncs the whole chain from scratch
  7  fork + reorg: B is cut off and mines its own block, A mines more, B rejoins and switches to the longer chain
Uses the regtest network (easy difficulty); it refuses to run on mainnet difficulty. Nothing is written outside a temp folder.
"""
import os, sys, io, time, socket, ctypes, tempfile, shutil, contextlib, importlib.util

if os.environ.get("NEBULA_NETWORK", "regtest").strip().lower() != "regtest":
    sys.exit("local_testnet needs NEBULA_NETWORK=regtest (mainnet difficulty is far too high for a test).")
os.environ["NEBULA_NETWORK"] = "regtest"
os.environ.setdefault("NEBULA_ALLOW_DEV_MODE", "1")
os.environ["NEBULA_DISABLE_CHAIN"] = "1"
os.environ["NEBULA_P2P_TLS"] = "required"
TMP = tempfile.mkdtemp(prefix="nebula_lt_")
os.environ["NEBULA_P2P_TLS_DIR"] = os.path.join(TMP, "tls")
QUICK = "--quick" in sys.argv

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)
spec = importlib.util.spec_from_file_location("nb", os.path.join(root, "nebula_v10_24.py"))
m = importlib.util.module_from_spec(spec); sys.modules["nb"] = m
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    spec.loader.exec_module(m)

QUIET = lambda: contextlib.redirect_stdout(io.StringIO())
R = []
def chk(name, ok, info=""):
    R.append((name, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + name + (f"   [{info}]" if info and not ok else ""), flush=True)

def free_port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p

def wait(cond, t=40):
    t0 = time.time()
    while time.time() - t0 < t:
        try:
            if cond(): return True
        except Exception:
            pass
        time.sleep(0.3)
    return False

class Node:
    def __init__(self, name):
        self.name = name
        with QUIET(), contextlib.redirect_stderr(io.StringIO()):
            self.bc = m.NEBULABlockchain(); self.bc._dev_mode = True
            self.port = free_port()
            self.p2p = m.P2PNode(self.bc, host="127.0.0.1", port=self.port, data_dir=tempfile.mkdtemp(dir=TMP))
            self.p2p.on_new_block = lambda blk, _p=self.p2p: _p.broadcast_block(blk)   # same relay as the real NEBULANode
            self.p2p.start()
        time.sleep(0.5)
    def connect(self, other):
        with QUIET(), contextlib.redirect_stderr(io.StringIO()):
            return self.p2p.connect_peer("127.0.0.1", other.port)
    @property
    def tip(self): return self.bc.tip.hash
    @property
    def height(self): return self.bc.height
    def stop(self):
        with QUIET(), contextlib.redirect_stderr(io.StringIO()):
            try: self.p2p.stop()
            except Exception: pass

_ts = [int(time.time()) - 100000]
def solve(hdr):
    if getattr(m, "_NBL_ACCEL_OK", False):
        h76 = hdr.serialize()[:76]; tgt = m.bits_to_target(hdr.bits).to_bytes(32, "big")
        found = ctypes.c_uint32(0); hashes = ctypes.c_uint64(0); n = 0
        while n < 2 ** 32:
            end = min(n + 0xFFFFF, 2 ** 32 - 1)
            if m._NBL_C_MINE(h76, tgt, ctypes.c_uint32(n), ctypes.c_uint32(end), ctypes.byref(found), ctypes.byref(hashes)) == 1:
                hdr.nonce = found.value; break
            n = end + 1
    else:
        hdr.nonce = 0
        while not hdr.meets_target(): hdr.nonce += 1
    assert hdr.meets_target()

def build_block(bc, addr, txs=(), prev=None):
    prev = prev or bc.tip
    h = prev.height + 1
    fees = sum(t.fee(bc.utxo) for t in txs)
    cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h) + fees, miner_address=addr)
    allt = [cb] + list(txs)
    root_ = m.MerkleTree.compute_root([t.txid for t in allt])
    _ts[0] = max(_ts[0] + 1, prev.header.timestamp + 1)
    bits = bc.get_next_bits() if prev is bc.tip else prev.header.bits
    hdr = m.BlockHeader(1, prev.hash, root_, _ts[0], bits, 0, h)
    solve(hdr)
    return m.Block(hdr, allt)

def mine_on(node, addr, txs=()):
    blk = build_block(node.bc, addr, txs)
    with QUIET(), contextlib.redirect_stderr(io.StringIO()):
        ok, msg = node.bc.add_block(blk)
        if ok: node.p2p.broadcast_block(blk)
    assert ok, msg
    return blk

def same_tip(*nodes, t=40):
    return wait(lambda: len({n.tip for n in nodes}) == 1, t)

def main():
    t_start = time.time()
    A, B, C = Node("A"), Node("B"), Node("C")
    wallet_miner = m.NEBULAWallet(utxo_set=A.bc.utxo); MINER = wallet_miner.first_address
    wallet_dest = m.NEBULAWallet(utxo_set=A.bc.utxo); DEST = wallet_dest.first_address
    nodes = [A, B, C]
    try:
        # 1 - connect (star around A)
        chk("1  B and C connect to A over TLS 1.3", B.connect(A) and C.connect(A) and wait(lambda: len(A.p2p._peers) == 2 and len(B.p2p._peers) >= 1 and len(C.p2p._peers) >= 1))
        chk("1b genesis is identical on all nodes", len({n.bc._chain[0].hash for n in nodes}) == 1)
        # 2 - one block
        mine_on(A, MINER)
        chk("2  a block mined on A reaches B and C", same_tip(A, B, C) and B.height == 1, (A.height, B.height, C.height))
        # 3 - many blocks
        n_blocks = 4 if QUICK else m.COINBASE_MATURITY + 1
        for _ in range(n_blocks):
            mine_on(A, MINER)
        chk(f"3  {n_blocks} more blocks mined on A: all three nodes stay in sync", same_tip(A, B, C, t=120) and A.height == B.height == C.height == n_blocks + 1, (A.height, B.height, C.height))
        chk("3b UTXO totals agree on all nodes", len({n.bc.utxo.balance(MINER) for n in nodes}) == 1)
        if not QUICK:
            # 4 - a real signed payment, injected at B
            tx = wallet_miner.build_transaction(DEST, 12.5, fee_nbl=0.001)
            ok_tx, msg_tx = (tx is not None, "wallet could not build tx") if tx is None else B.bc.add_to_mempool(tx)
            chk("4  signed payment accepted by B's mempool", ok_tx, msg_tx)
            if ok_tx:
                with QUIET(), contextlib.redirect_stderr(io.StringIO()):
                    B.p2p.broadcast_tx(tx)
                chk("4b the payment reaches A's and C's mempool", wait(lambda: tx.txid in A.bc.mempool._txs and tx.txid in C.bc.mempool._txs, 30))
                # 5 - mined by C
                mine_on(C, MINER, [tx])
                chk("5  C mines the payment; all nodes agree", same_tip(A, B, C))
                bals = {n.bc.utxo.balance(DEST) for n in nodes}
                chk("5b receiver balance is exactly 12.5 NBL on every node", bals == {int(12.5 * 10 ** m.DECIMALS)}, bals)
                chk("5c mempools are empty after the block", wait(lambda: A.bc.mempool.size() == 0 and B.bc.mempool.size() == 0 and C.bc.mempool.size() == 0, 15))
        # 6 - brand-new node syncs everything
        D = Node("D"); nodes.append(D)
        chk("6  new node D connects", D.connect(A))
        chk("6b D syncs the whole chain from scratch", same_tip(A, D, t=180) and D.height == A.height, (A.height, D.height))
        # 7 - fork and reorg
        B.stop()
        mine_on(B, MINER)                            # B mines alone: its own 1-block branch
        b_tip_alone = B.tip
        for _ in range(3): mine_on(A, MINER)         # the rest of the network goes 3 blocks further
        chk("7  while cut off, B and A really have different tips", B.tip != A.tip and B.tip == b_tip_alone)
        B2 = Node("B2"); B2.bc = B.bc
        with QUIET(), contextlib.redirect_stderr(io.StringIO()):
            B2.p2p = m.P2PNode(B.bc, host="127.0.0.1", port=B2.port, data_dir=tempfile.mkdtemp(dir=TMP))
            B2.p2p.on_new_block = lambda blk, _p=B2.p2p: _p.broadcast_block(blk); B2.p2p.start()
        time.sleep(0.5); nodes.append(B2)
        B2.connect(A)
        chk("7b B rejoins and reorgs to the longer chain", same_tip(A, B2, C, D, t=120), (A.height, B.height, C.height, D.height))
        chk("7c all four views of the chain are identical", len({n.tip for n in (A, B2, C, D)}) == 1 and len({n.bc.utxo.balance(MINER) for n in (A, B2, C, D)}) == 1)
    finally:
        for n in nodes: n.stop()
        shutil.rmtree(TMP, ignore_errors=True)
    bad = sum(1 for _, ok in R if not ok)
    print(f"\n{len(R)-bad}/{len(R)} passed  ({time.time()-t_start:.0f}s)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
