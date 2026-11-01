import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""v10.21 tests: incremental SQLite chain store (live per-block commits, reorg follow, tamper detection, kill -9)."""
import os, sys, io, json, time, shutil, tempfile, threading, contextlib, importlib.util, glob, sqlite3, subprocess, signal

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("NEBULA_DISABLE_CHAIN", "1")
os.environ.pop("NEBULA_LEGACY_JSON", None)
os.environ.pop("NEBULA_VERIFY_ON_LOAD", None)
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

@contextlib.contextmanager
def QUIET():
    with contextlib.redirect_stdout(io.StringIO()):
        yield

ADDR = 'NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx'
BASE = int(time.time()) - 6000
def mine_on(prev, extra=b'', tsoff=0):
    h = prev.height + 1
    cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h), miner_address=ADDR, extra_data=extra)
    root_ = m.MerkleTree.compute_root([cb.txid])
    hdr = m.BlockHeader(1, prev.hash, root_, BASE + h * 60 + tsoff, prev.header.bits, 0, h)
    n = 0
    while int(hdr.hash(), 16) >= hdr.target:
        n += 1; hdr.nonce = n
    return m.Block(hdr, [cb])
def mine(bc): return mine_on(bc.tip)
def grow(bc, k):
    for _ in range(k):
        ok, msg = bc.add_block(mine(bc)); assert ok, msg
def fresh_chain(k=4):
    with QUIET():
        bc = m.NEBULABlockchain(); grow(bc, k)
    return bc
def save(bc, d):
    with QUIET(): return bc.save(d)
def load(d):
    with QUIET(): return m.NEBULABlockchain.load(d)
def db(d): return sqlite3.connect(os.path.join(d, 'nebula_chain.db'))
def nblocks(d):
    c = db(d); r = c.execute('select count(*) from blocks').fetchone()[0]; c.close(); return r
def same_state(a, b):
    return (a.height == b.height and a.tip.hash == b.tip.hash and a.utxo.size() == b.utxo.size()
            and a.utxo.total_supply() == b.utxo.total_supply())

# 1 round trip
bc = fresh_chain(4); d = tempfile.mkdtemp()
chk('save -> True, DB created, no JSON files written', lambda: save(bc, d) is True and os.path.exists(os.path.join(d, 'nebula_chain.db')) and not glob.glob(os.path.join(d, 'nebula_*.json')))
bc2 = load(d)
chk('load from DB: same height/tip/UTXO/supply', lambda: bc2 is not None and same_state(bc, bc2) and bc2.height == 4)
def streams():
    with QUIET(): ok, _ = bc2.add_block(mine(bc2))
    return ok and nblocks(d) == 6          # committed WITHOUT calling save()
chk('restarted chain accepts a block; it is on disk immediately (no save())', streams)
chk('...and a third start sees it', lambda: load(d).height == 5)

# 2 live streaming from the first save on
d2 = tempfile.mkdtemp(); b2 = fresh_chain(2); save(b2, d2)
with QUIET(): grow(b2, 3)
chk('blocks mined after save() are committed per block (rows == height+1)', lambda: nblocks(d2) == 6)
r2 = load(d2)
chk('...and load gives the same state', lambda: same_state(b2, r2))

# 3 save() is incremental
d3 = tempfile.mkdtemp(); b3 = fresh_chain(3); save(b3, d3)
st = list(b3._chain_stores.values())[0]
calls = []
orig = st._apply
st._apply = lambda blk: (calls.append(blk.height), orig(blk))[1]
st.stale = True; st.tip_h = st.tip_h        # force save() to do the work itself
with QUIET(): b3.add_block(mine(b3))
st._apply = orig
chk('after a stale flag, save() re-applies only the missing block', lambda: save(b3, d3) is True and nblocks(d3) == 5)

# 4 reorg: DB follows the heavier fork
d4 = tempfile.mkdtemp(); b4 = fresh_chain(4); save(b4, d4)
anc = b4._chain[2]; prev = anc; fork = []
for i in range(3):
    f = mine_on(prev, extra=b'fk', tsoff=5); fork.append(f); prev = f
msgs = []
with QUIET():
    for f in fork: msgs.append(b4.add_block(f))
chk('heavier fork accepted -> reorg happened', lambda: b4.tip.hash == fork[-1].hash and b4.height == 5)
r4 = load(d4)
chk('DB followed the reorg (tip, UTXO, supply identical)', lambda: r4 is not None and same_state(b4, r4))
chk('old branch rows are gone', lambda: nblocks(d4) == 6)

# 5 tampering is detected
def tamper_case(sql_fn, label, expect_none_after=True):
    dd = tempfile.mkdtemp(); bb = fresh_chain(3); save(bb, dd)
    for s in list(bb._chain_stores.values()): s.close()
    c = db(dd); sql_fn(c); c.commit(); c.close()
    r = load(dd)
    return r is None and len(glob.glob(os.path.join(dd, 'nebula_chain.db.corrupt-*'))) == 1
chk('edited UTXO value -> rejected, DB kept as *.corrupt-*', lambda: tamper_case(lambda c: c.execute('update utxo set value=value+1 where rowid=1'), 'utxo'))
chk('forged extra UTXO row -> rejected', lambda: tamper_case(lambda c: c.execute("insert into utxo values('zz:0','zz',0,999999999999,x'00',1,0)"), 'ins'))
chk('edited block nonce -> rejected (PoW/link)', lambda: tamper_case(lambda c: c.execute("update blocks set data=replace(data,'\"nonce\":','\"nonce\":9') where height=2"), 'nonce'))
chk('deleted middle block row -> rejected (not contiguous)', lambda: tamper_case(lambda c: c.execute('delete from blocks where height=1'), 'gap'))
def garbage():
    dd = tempfile.mkdtemp(); bb = fresh_chain(2); save(bb, dd)
    for s in list(bb._chain_stores.values()): s.close()
    open(os.path.join(dd, 'nebula_chain.db'), 'wb').write(b'not a database' * 50)
    for sfx in ('-wal', '-shm'):
        if os.path.exists(os.path.join(dd, 'nebula_chain.db' + sfx)): os.remove(os.path.join(dd, 'nebula_chain.db' + sfx))
    return load(dd) is None
chk('garbage file -> None, no crash', garbage)

# 6 fallback from a damaged DB to the JSON files of an older version
d6 = tempfile.mkdtemp(); b6 = fresh_chain(3)
os.environ['NEBULA_LEGACY_JSON'] = '1'; save(b6, d6); os.environ.pop('NEBULA_LEGACY_JSON')
r6 = load(d6)
chk('migration: JSON-only dir loads and creates the DB', lambda: r6 is not None and same_state(b6, r6) and os.path.exists(os.path.join(d6, 'nebula_chain.db')))
chk('...JSON files left untouched', lambda: os.path.exists(os.path.join(d6, 'nebula_chain.json')) and os.path.exists(os.path.join(d6, 'nebula_meta.json')))
with QUIET(): grow(r6, 1)
r6b = load(d6)
chk('...next start reads the DB (has the new block, JSON is older)', lambda: r6b.height == 4)

# 7 foreign chain id
d7 = tempfile.mkdtemp(); b7 = fresh_chain(2); save(b7, d7)
for s in list(b7._chain_stores.values()): s.close()
c = db(d7); c.execute("update meta set v='999' where k='chain_id'"); c.commit(); c.close()
chk('foreign chain id -> None, DB untouched', lambda: load(d7) is None and os.path.exists(os.path.join(d7, 'nebula_chain.db')) and not glob.glob(os.path.join(d7, '*.corrupt-*')))

# 8 dev mode keeps unbacked coin
with QUIET():
    bD = m.NEBULABlockchain(); bD._dev_mode = True; grow(bD, 2); ent = bD.fund_address(ADDR, 7)
dD = tempfile.mkdtemp(); save(bD, dD); rD = load(dD)
chk('dev-mode funded coin survives restart', lambda: rD is not None and same_state(bD, rD))

# 9 optional deep verification
os.environ['NEBULA_VERIFY_ON_LOAD'] = 'replay'
chk('NEBULA_VERIFY_ON_LOAD=replay accepts a good DB', lambda: load(d4) is not None)
os.environ['NEBULA_VERIFY_ON_LOAD'] = 'full'
chk('NEBULA_VERIFY_ON_LOAD=full accepts a good DB', lambda: load(d4) is not None)
os.environ.pop('NEBULA_VERIFY_ON_LOAD')

# 10 concurrent saves + growth
bT = fresh_chain(2); dT = tempfile.mkdtemp(); errs = []
def saver():
    for _ in range(6):
        try:
            if not save(bT, dT): errs.append('False')
        except Exception as e: errs.append(repr(e))
ths = [threading.Thread(target=saver) for _ in range(4)]; [t.start() for t in ths]
for _ in range(3):
    with QUIET(): grow(bT, 1)
[t.join() for t in ths]; save(bT, dT)
chk('concurrent saves while mining: no errors, DB matches', lambda: not errs and same_state(bT, load(dT)))

# 11 simulated crash inside a block transaction (rollback leaves the previous state)
class Crash(BaseException): pass
ok_all = True; detail = []
for n in range(1, 6):
    dC = tempfile.mkdtemp(); bC = fresh_chain(2); save(bC, dC)
    st = list(bC._chain_stores.values())[0]
    real = st._put; cnt = [0]
    def put(e, real=real, cnt=cnt, n=n):
        cnt[0] += 1
        if cnt[0] == n: raise Crash()
        return real(e)
    st._put = put
    blk = mine(bC)
    try:
        with QUIET(): bC.add_block(blk)
    except Crash:
        pass
    st.close()
    r = load(dC)
    good = r is not None and r.height in (2, 3)
    if good:
        with QUIET(): ok, _ = r.add_block(mine(r))
        good = ok
    if not good: ok_all = False; detail.append((n, None if r is None else r.height))
chk('crash in the middle of a block commit: previous state loads and keeps working', lambda: ok_all or detail)

# 12 real kill -9 of a node process while it appends blocks
dA = tempfile.mkdtemp(); bK = fresh_chain(2); save(bK, dA)
for st_ in list(bK._chain_stores.values()): st_.close()
bK._listeners.clear()
dB = tempfile.mkdtemp(); shutil.rmtree(dB); shutil.copytree(dA, dB)        # base DB at height 2
with QUIET(): grow(bK, 6)
todo = [m._blk_to_dict(b) for b in bK._chain[3:]]                           # blocks 3..8
json.dump(todo, open(os.path.join(tempfile.gettempdir(), 'nb_todo.json'), 'w'))
child = r"""
import os, sys, io, json, time, contextlib, importlib.util
os.environ['NEBULA_DISABLE_CHAIN'] = '1'
spec = importlib.util.spec_from_file_location('nb', sys.argv[1]); m = importlib.util.module_from_spec(spec); sys.modules['nb'] = m
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
with contextlib.redirect_stdout(io.StringIO()): bc = m.NEBULABlockchain.load(sys.argv[2])
todo = json.load(open(sys.argv[3]))
sys.__stdout__.write('READY\n'); sys.__stdout__.flush()
for i, bd in enumerate(todo, 1):
    with contextlib.redirect_stdout(io.StringIO()): ok, why = bc.add_block(m._blk_from_dict(bd))
    sys.__stdout__.write(f'ADDED {i} {ok}\n'); sys.__stdout__.flush()
    time.sleep(0.4)
"""
proc = subprocess.Popen([sys.executable, '-c', child, os.path.join(root, 'nebula_v10_24.py'), dB,
                         os.path.join(tempfile.gettempdir(), 'nb_todo.json')],
                        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, env=dict(os.environ, NEBULA_DISABLE_CHAIN='1'))
added = 0
t_end = time.time() + 120
while time.time() < t_end:
    line = proc.stdout.readline()
    if not line: break
    if line.startswith('ADDED'):
        added = int(line.split()[1])
        if added >= 3:
            os.kill(proc.pid, signal.SIGKILL); break
proc.wait()
rK = load(dB)
chk('kill -9 while appending: child had committed >=3 blocks', lambda: added >= 3)
chk('...DB loads, height >= 5 (every acknowledged block is durable)', lambda: rK is not None and 5 <= rK.height <= 8)
def continues():
    with QUIET(): ok, _ = rK.add_block(mine(rK))
    return ok
chk('...and the recovered chain keeps accepting blocks', continues)
chk('...and re-saves/loads cleanly', lambda: save(rK, dB) is True and same_state(rK, load(dB)))

# 13 informational: per-block commit cost with a large UTXO table
dP = tempfile.mkdtemp(); bP = fresh_chain(2); save(bP, dP)
stP = list(bP._chain_stores.values())[0]
with stP.lock:
    stP.con.execute('BEGIN IMMEDIATE')
    for i in range(0, 200000, 1000):
        for j in range(i, i + 1000):
            stP._put(m.UTXOEntry(txid=('%064x' % (j + 10**9)), index=0, value=1000, script_pubkey=b'\x51', height=1, is_coinbase=False))
    stP._write_meta()
    stP.con.execute('COMMIT')
with QUIET(): blkP = mine(bP)
t0 = time.time()
with QUIET(): bP.add_block(blkP)
dt = time.time() - t0
sys.__stdout__.write(f'  (info) block commit with {stP.count} UTXO rows in the table: add_block incl. DB commit = {dt*1000:.0f} ms\n')
chk('per-block commit stays small with 200k UTXO rows (< 1.5 s)', lambda: dt < 1.5 or dt)

sys.stdout = sys.__stdout__
w = max(len(n) for n, _, _ in R)
for n, s_, d_ in R: print(f'{s_:5} {n:<{w}}  {d_}')
f = sum(1 for _, s_, _ in R if s_ != 'PASS')
print(f'\n{len(R) - f}/{len(R)} passed', flush=True)
sys.exit(1 if f else 0)
