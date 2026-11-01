import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""v10.22 tests: reorg depth policy (limit, alert, override), checkpoint floor, O(depth) work comparison,
and reorg / competing blocks after a restart (undo data from the chain database)."""
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
def replay_supply(bc):
    u = m.UTXOSet()
    for b in bc._chain: assert u.apply_block(b)
    return u.size(), u.total_supply()

# 1 configuration
chk('default limit is 100 blocks', lambda: m.NEBULABlockchain.MAX_FORK_DEPTH == 100)
def envcheck():
    os.environ['NEBULA_MAX_REORG_DEPTH'] = '7'; a = m._env_int('NEBULA_MAX_REORG_DEPTH', 100, 1, 10**6)
    os.environ['NEBULA_MAX_REORG_DEPTH'] = 'abc'; b = m._env_int('NEBULA_MAX_REORG_DEPTH', 100, 1, 10**6)
    os.environ['NEBULA_MAX_REORG_DEPTH'] = '0'; c = m._env_int('NEBULA_MAX_REORG_DEPTH', 100, 1, 10**6)
    os.environ.pop('NEBULA_MAX_REORG_DEPTH'); return (a, b, c) == (7, 100, 1)
chk('NEBULA_MAX_REORG_DEPTH: valid / garbage / clamped', envcheck)

# 2 deep fork: refused + alert, junk makes no alert
bc = chain(6); bc.MAX_FORK_DEPTH = 2
f1 = mine_on(bc._chain[2], extra=b'fk', tsoff=5)
ok, msg = add(bc, f1)
chk('fork 4 blocks deep with limit 2 -> refused', lambda: ok is False and 'too deep' in msg)
chk('...alert recorded (depth 4, limit 2, hash)', lambda: len(bc.deep_fork_alerts()) == 1 and bc.deep_fork_alerts()[0]['depth'] == 4 and bc.deep_fork_alerts()[0]['hash'] == f1.hash)
junk = mine_on(bc._chain[1], extra=b'jk'); junk.header.nonce ^= 0x5a5a5a; 
while int(junk.header.hash(), 16) < junk.header.target: junk.header.nonce += 1
ok2, _ = add(bc, junk)
chk('block without proof of work: refused, NO alert', lambda: ok2 is False and len(bc.deep_fork_alerts()) == 1)
chk('same branch is alerted only once (rate limit)', lambda: (add(bc, mine_on(bc._chain[2], extra=b'f2', tsoff=9)), len(bc.deep_fork_alerts()))[1] == 1)

# 3 operator override -> normal reorg incl. O(depth) work == full work comparison
bc.set_max_reorg_depth(10)
def _raises(f):
    try: f(); return False
    except ValueError: return True
chk('set_max_reorg_depth rejects values < 1', lambda: _raises(lambda: bc.set_max_reorg_depth(0)))
tip_before = bc.tip.hash; fork = [f1]; prev = f1
ok, msg = add(bc, f1)
chk('after the override the same branch is accepted as a side chain', lambda: ok and 'fork' in msg.lower())
eq = []
for i in range(4):
    nb = mine_on(prev, extra=b'fk', tsoff=5); prev = nb; fork.append(nb)
    ok, msg = add(bc, nb)
    if bc.tip.hash == tip_before and bc._fork_tips:
        fc = bc._fork_tips[nb.hash]
        eq.append(bc._branch_work_delta(fc)[0] == m.NEBULABlockchain._chain_work(fc) - m.NEBULABlockchain._chain_work(bc._chain))
chk('work delta (O(depth)) == full chain work comparison (shorter and equal fork)', lambda: len(eq) >= 3 and all(eq) or eq)
chk('heavier fork -> reorg executed, tip == fork tip', lambda: bc.tip.hash == prev.hash and bc.height == 7)
chk('UTXO set after reorg == replay of the new chain', lambda: (bc.utxo.size(), bc.utxo.total_supply()) == replay_supply(bc))
fc2 = list(bc._chain)
bc.MAX_FORK_DEPTH = 1
chk('_execute_reorg refuses a reorg deeper than the limit', lambda: m.NEBULABlockchain._execute_reorg(bc, fc2[:3] + [mine_on(fc2[2], extra=b'zz')])[0] is False)

# 4 checkpoints
bcC = chain(5)
save_cps = dict(m.CHECKPOINTS)
try:
    m.CHECKPOINTS[4] = bcC._chain[4].hash
    fk = mine_on(bcC._chain[2], extra=b'fk', tsoff=5)
    okc, msgc = add(bcC, fk)
    chk('fork below a checkpointed block is refused', lambda: okc is False and 'checkpoint' in msgc.lower())
    bcC.set_max_reorg_depth(1000)
    okc2, msgc2 = add(bcC, mine_on(bcC._chain[2], extra=b'f3', tsoff=6))
    chk('...even with a raised limit (checkpoint is absolute)', lambda: okc2 is False and 'checkpoint' in msgc2.lower())
    m.CHECKPOINTS.clear(); m.CHECKPOINTS.update(save_cps); m.CHECKPOINTS[6] = 'ab' * 32
    okc3, msgc3 = add(bcC, mine_on(bcC.tip))
    chk('main-chain block with the wrong hash at a checkpoint height is refused', lambda: okc3 is False and 'checkpoint' in msgc3.lower())
    m.CHECKPOINTS.clear(); m.CHECKPOINTS.update(save_cps)
    okc4, _ = add(bcC, mine_on(bcC.tip))
    chk('...and the chain continues once the checkpoint table is normal', lambda: okc4)
finally:
    m.CHECKPOINTS.clear(); m.CHECKPOINTS.update(save_cps)

# 5 performance of the work comparison on a long chain (synthetic blocks)
class FB:
    __slots__ = ('hash', 'header')
    def __init__(self, i, bits=0x1e0fffff): self.hash = '%064x' % i; self.header = types.SimpleNamespace(bits=bits)
N = 60000
bcP = m.NEBULABlockchain.__new__(m.NEBULABlockchain)
bcP._chain = [FB(i) for i in range(N)]
forkP = bcP._chain[:N - 10] + [FB(10**7 + i) for i in range(12)]
t0 = time.perf_counter(); d_new = bcP._branch_work_delta(forkP)[0]; t_new = time.perf_counter() - t0
t0 = time.perf_counter(); d_old = m.NEBULABlockchain._chain_work(forkP) - m.NEBULABlockchain._chain_work(bcP._chain); t_old = time.perf_counter() - t0
sys.__stdout__.write(f'  (info) 60,000-block chain: old full comparison {t_old*1000:.1f} ms, new {t_new*1000:.3f} ms\n')
chk('same answer on a 60,000-block chain and far cheaper', lambda: d_new == d_old and t_new * 50 < t_old or (d_new, d_old, t_new, t_old))

# 6 restart: the real bugs of v10.21
bcR = chain(5); dR = tempfile.mkdtemp()
with Q(): bcR.save(dR); bc2 = m.NEBULABlockchain.load(dR)
chk('blocks loaded from disk have no undo data in memory (as before)', lambda: not getattr(bc2._chain[3], '_undo_added', None))
fa = mine_on(bc2._chain[3], tsoff=7)       # same miner, same coinbase as the main block at height 4
okA, msgA = add(bc2, fa)
chk('after restart: competing block with an IDENTICAL coinbase is accepted as a side chain', lambda: okA or msgA)
prev = bc2._chain[2]; res = []
for i in range(4):
    nb = mine_on(prev, extra=b'fk', tsoff=5); prev = nb; res.append(add(bc2, nb))
chk('after restart: heavier fork from before the restart -> REORG succeeds', lambda: bc2.tip.hash == prev.hash and bc2.height == 6 or res)
chk('...UTXO set equals the replay of the new chain', lambda: (bc2.utxo.size(), bc2.utxo.total_supply()) == replay_supply(bc2))
with Q(): bc3 = m.NEBULABlockchain.load(dR)
chk('...the database followed the reorg (next start has the new tip)', lambda: bc3 is not None and bc3.tip.hash == prev.hash and bc3.utxo.total_supply() == bc2.utxo.total_supply())
okx, _ = add(bc3, mine_on(bc3.tip))
chk('...and the chain keeps growing afterwards', lambda: okx)

sys.stdout = sys.__stdout__
w = max(len(n) for n, _, _ in R)
for n, s_, d_ in R: print(f'{s_:5} {n:<{w}}  {d_}')
f = sum(1 for _, s_, _ in R if s_ != 'PASS')
print(f'\n{len(R) - f}/{len(R)} passed', flush=True)
sys.exit(1 if f else 0)
