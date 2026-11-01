#!/usr/bin/env python3
"""NEBULA - mine TEST blocks on your own phone/PC and pay the reward to YOUR wallet address.

    python3 tools/mine_to_address.py <ADDRESS> [BLOCKS]       # default 20 blocks
    python3 tools/mine_to_address.py <ADDRESS> --balance      # only show the balance

* Runs on the regtest (test) network only. These coins have NO real value and exist only in the chain folder
  (~/nebula_testnet by default, override with --dir). Nothing is sent over the internet.
* The chain is saved after every block, so you can stop with Ctrl+C and continue later.
* Only the PUBLIC address is needed - never type your 12 words here.
* A reward only becomes spendable after 100 more blocks (coinbase maturity); both numbers are shown.
"""
import os, sys, io, time, ctypes, contextlib, importlib.util

if os.environ.get("NEBULA_NETWORK", "regtest").strip().lower() != "regtest":
    sys.exit("This tool is for the TEST network only (NEBULA_NETWORK=regtest).")
os.environ["NEBULA_NETWORK"] = "regtest"
os.environ["NEBULA_DISABLE_CHAIN"] = "1"

args = [a for a in sys.argv[1:] if not a.startswith("--")]
flags = [a for a in sys.argv[1:] if a.startswith("--")]
if not args:
    sys.exit(__doc__)
ADDR = args[0]
BLOCKS = int(args[1]) if len(args) > 1 else 20
DATA = os.path.expanduser("~/nebula_testnet")
for f in flags:
    if f.startswith("--dir="): DATA = os.path.expanduser(f.split("=", 1)[1])

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("nb", os.path.join(root, "nebula_v10_24.py"))
m = importlib.util.module_from_spec(spec); sys.modules["nb"] = m
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    spec.loader.exec_module(m)

# --- the address must be a valid NEBULA address (checksum catches a mistyped / mis-read character) ---
try:
    ver, payload = m.base58check_decode(ADDR)
    assert len(payload) == 20 and ver == m.PUBKEY_ADDRESS_VERSION
except Exception:
    sys.exit("This is not a valid NEBULA address (check every character; copy it as text, never retype it).")

def QUIET(): return contextlib.redirect_stdout(io.StringIO())

os.makedirs(DATA, exist_ok=True)
with QUIET(), contextlib.redirect_stderr(io.StringIO()):
    if os.path.exists(os.path.join(DATA, "nebula_chain.db")):
        bc = m.NEBULABlockchain.load(DATA)
    else:
        bc = m.NEBULABlockchain()

def nbl(x): return x / 10 ** m.DECIMALS

def show():
    h = bc.height
    total = bc.utxo.balance(ADDR)
    mature = sum(u.value for u in bc.utxo.get_by_address(ADDR)
                 if not (u.is_coinbase and h - u.height < m.COINBASE_MATURITY))
    print(f"  height {h} | balance {nbl(total):,.2f} NBL | spendable now {nbl(mature):,.2f} NBL")

def solve(hdr):
    if getattr(m, "_NBL_ACCEL_OK", False):
        h76 = hdr.serialize()[:76]; tgt = m.bits_to_target(hdr.bits).to_bytes(32, "big")
        found = ctypes.c_uint32(0); hashes = ctypes.c_uint64(0); n = 0
        while n < 2 ** 32:
            end = min(n + 0xFFFFF, 2 ** 32 - 1)
            if m._NBL_C_MINE(h76, tgt, ctypes.c_uint32(n), ctypes.c_uint32(end), ctypes.byref(found), ctypes.byref(hashes)) == 1:
                hdr.nonce = found.value; return
            n = end + 1
    else:
        hdr.nonce = 0
        while not hdr.meets_target(): hdr.nonce += 1

def mine_one():
    prev = bc.tip; h = prev.height + 1
    cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h), miner_address=ADDR)
    root_ = m.MerkleTree.compute_root([cb.txid])
    ts = max(int(time.time()) - 60, prev.header.timestamp + 1)
    hdr = m.BlockHeader(1, prev.hash, root_, ts, bc.get_next_bits(), 0, h)
    solve(hdr)
    blk = m.Block(hdr, [cb])
    with QUIET(), contextlib.redirect_stderr(io.StringIO()):
        ok, msg = bc.add_block(blk)
        if ok: bc.save(DATA)
    if not ok: sys.exit(f"block rejected: {msg}")

print(f"NEBULA test chain: {DATA}\nAddress: {ADDR}")
show()
if "--balance" in flags:
    sys.exit(0)
t0 = time.time()
try:
    for i in range(1, BLOCKS + 1):
        mine_one()
        if i % 5 == 0 or i == BLOCKS:
            print(f"  mined {i}/{BLOCKS}  ({(time.time()-t0)/i:.1f}s per block)", flush=True)
except KeyboardInterrupt:
    print("\nstopped - everything mined so far is saved.")
show()
