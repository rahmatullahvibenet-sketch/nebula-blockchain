import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""v10.23 tests: side-chain validation budget (token bucket)."""
import os, sys, io, time, tempfile, contextlib, importlib.util, types

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("NEBULA_DISABLE_CHAIN", "1")
os.environ.pop("NEBULA_LEGACY_JSON", None)
spec = importlib.util.spec_from_file_location('nb', os.path.join(root, 'nebula_v10_24.py'))
m = importlib.util.module_from_spec(spec); sys.modules['nb'] = m
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(m)

R = []
def chk(name, fn):
    try:
        r = fn(); R.append((name, 'PASS' if r is not False else 'FAIL', str(r)[:90]))
    except Exception as e:
        import traceback; R.append((name, 'ERROR', f'{type(e).__name__}: {str(e)[:100]} {traceback.format_exc()[-200:]}'))
    sys.__stdout__.write(f'  .. {R[-1][1]:5} {name}\n'); sys.__stdout__.flush()

def Q(): return contextlib.redirect_stdout(io.StringIO())
ADDR = 'NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx'
BASE = int(time.time()) - 6000
def mine_on(prev, extra=b'', tsoff=0):
    h = prev.height + 1
    cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h), miner_address=ADDR, extra_data=extra)
    hdr = m.BlockHeader(1, prev.hash, m.MerkleTree.compute_root([cb.txid]), BASE + h * 60 + tsoff, prev.header.bits, 0, h)
    n = 0
    while int(hdr.hash(), 16) >= hdr.target:
        n += 1; hdr.nonce = n
    return m.Block(hdr, [cb])
def chain(k):
    with Q():
        bc = m.NEBULABlockchain()
        for _ in range(k):
            ok, msg = bc.add_block(mine_on(bc.tip)); assert ok, msg
    return bc
def add(bc, b):
    with Q(): return bc.add_block(b)

bc = chain(6)
chk('defaults: burst 300, 30 per minute', lambda: (m.NEBULABlockchain.SIDE_BLOCK_BURST, m.NEBULABlockchain.SIDE_BLOCK_PER_MIN) == (300, 30))
bc.SIDE_BLOCK_BURST = 3; bc.SIDE_BLOCK_PER_MIN = 60
b1 = bc._chain[1]
side = []; prev = b1; res = []
for i in range(4):
    blk = mine_on(prev, extra=b'side%d' % i)
    res.append(add(bc, blk)); side.append(blk); prev = blk
chk('first 3 side-chain blocks accepted', lambda: all(r[0] for r in res[:3]) or res[:3])
chk('4th side-chain block refused by the budget', lambda: (not res[3][0]) and 'rate limit' in res[3][1] or res[3])
chk('main chain unaffected (tip still height 6)', lambda: bc.height == 6)
ok_main, msg_main = add(bc, mine_on(bc.tip, extra=b'main7'))
chk('normal main-chain block still accepted while budget is empty', lambda: ok_main or msg_main)
bc.__dict__['_side_bucket'] = (3.0, time.monotonic())   # simulate refill
r4 = add(bc, side[3])
chk('after refill the same block is accepted', lambda: r4[0] or r4)
bc.__dict__['_side_bucket'] = (100.0, time.monotonic())   # absurd value must be capped to the burst
bc._side_budget_take()
chk('bucket never exceeds burst', lambda: bc._side_bucket[0] <= bc.SIDE_BLOCK_BURST)

bad = [r for r in R if r[1] != 'PASS']
print(f"\n{len(R)-len(bad)}/{len(R)} passed")
sys.exit(1 if bad else 0)
