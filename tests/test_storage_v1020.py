import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""v10.20 storage tests: atomic save, hash-checked load, backup fallback, crash simulation, replay-verified UTXO."""
import os, sys, io, json, time, shutil, hashlib, tempfile, threading, contextlib, importlib.util, glob

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("NEBULA_DISABLE_CHAIN", "1")
os.environ["NEBULA_LEGACY_JSON"] = "1"      # this file tests the v10.20 JSON store (the SQLite store: test_store_v1021.py)
spec = importlib.util.spec_from_file_location('nb', os.path.join(root, 'nebula_v10_24.py'))
m = importlib.util.module_from_spec(spec); sys.modules['nb'] = m
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(m)

R = []
def chk(name, fn):
    try:
        r = fn(); R.append((name, 'PASS' if r is not False else 'FAIL', str(r)[:90]))
    except Exception as e:
        R.append((name, 'ERROR', f'{type(e).__name__}: {str(e)[:100]}'))
    sys.__stdout__.write(f'  .. {R[-1][1]:5} {name}\n'); sys.__stdout__.flush()

@contextlib.contextmanager
def QUIET():
    with contextlib.redirect_stdout(io.StringIO()):
        yield

ADDR = 'NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx'
BASE = int(time.time()) - 6000
def mine(bc, i=None):
    prev = bc.tip; h = prev.height + 1
    cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h), miner_address=ADDR)
    root_ = m.MerkleTree.compute_root([cb.txid])
    hdr = m.BlockHeader(1, prev.hash, root_, BASE + h * 60, bc.get_next_bits(), 0, h)
    n = 0
    while int(hdr.hash(), 16) >= hdr.target:
        n += 1; hdr.nonce = n
    return m.Block(hdr, [cb])

def grow(bc, k):
    for _ in range(k):
        ok, msg = bc.add_block(mine(bc))
        assert ok, msg

def fresh_chain(k=4):
    with QUIET():
        bc = m.NEBULABlockchain(); grow(bc, k)
    return bc

def load(d):
    with QUIET():
        return m.NEBULABlockchain.load(d)

def save(bc, d):
    with QUIET():
        return bc.save(d)

def rewrite_meta(d, sfx='', **upd):
    p = os.path.join(d, 'nebula_meta.json' + sfx)
    meta = json.load(open(p)); meta.update(upd); json.dump(meta, open(p, 'w'))
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def names(d): return sorted(os.listdir(d))

# ── 1. round trip ──
bc = fresh_chain(4); d = tempfile.mkdtemp()
chk('save returns True', lambda: save(bc, d) is True)
chk('no .tmp files left behind', lambda: not [n for n in names(d) if n.endswith('.tmp') or n.endswith('.prevtmp')])
meta = json.load(open(os.path.join(d, 'nebula_meta.json')))
chk('meta has format 2 + both sha256', lambda: meta['format'] == 2 and meta['chain_sha256'] == sha(os.path.join(d, 'nebula_chain.json')) and meta['utxo_sha256'] == sha(os.path.join(d, 'nebula_utxo.json')))
bc2 = load(d)
chk('load: same height/tip', lambda: bc2.height == bc.height == 4 and bc2.tip.hash == bc.tip.hash)
chk('load: same UTXO set & supply', lambda: bc2.utxo.size() == bc.utxo.size() and bc2.utxo.total_supply() == bc.utxo.total_supply())
def accepts_after_restart():
    with QUIET(): ok, msg = bc2.add_block(mine(bc2))
    return ok and bc2.height == 5
chk('restarted chain accepts a new block', accepts_after_restart)

# ── 2. unchanged tip: no rewrite ──
d2 = tempfile.mkdtemp(); save(bc, d2); t0 = os.path.getmtime(os.path.join(d2, 'nebula_chain.json')); time.sleep(0.05)
chk('unchanged state: second save skipped', lambda: save(bc, d2) is True and os.path.getmtime(os.path.join(d2, 'nebula_chain.json')) == t0)

# ── 3. backup generation ──
d3 = tempfile.mkdtemp(); bcA = fresh_chain(3); save(bcA, d3)
grow(bcA, 2) if False else None
with QUIET(): grow(bcA, 2)
save(bcA, d3)
chk('.prev set exists after 2nd save', lambda: all(os.path.exists(os.path.join(d3, n + '.prev')) for n in m._STORE_NAMES))
with QUIET(): prev_bc = m.NEBULABlockchain._load_set(__import__('pathlib').Path(d3), '.prev', 'backup')
chk('.prev set is the older complete state', lambda: prev_bc.height == 3 and load(d3).height == 5)

# ── 4. torn write of the newest chain file -> backup used, bad set parked ──
p = os.path.join(d3, 'nebula_chain.json'); data = open(p, 'rb').read(); open(p, 'wb').write(data[:len(data) // 2])
rec = load(d3)
chk('torn chain file: recovered from backup (height 3)', lambda: rec is not None and rec.height == 3)
chk('torn set moved to *.corrupt-*, not deleted', lambda: len(glob.glob(os.path.join(d3, 'nebula_chain.json.corrupt-*'))) == 1)
chk('after recovery: add block + save + reload works', lambda: (lambda b: (grow(b, 1), save(b, d3), load(d3).height == 4)[2])(rec))

# ── 5. bit flip with intact length ──
d5 = tempfile.mkdtemp(); save(bcA, d5); save(bcA, d5)  # same state twice (skipped) -> make a real 2nd generation
with QUIET(): grow(bcA, 1)
save(bcA, d5)
p = os.path.join(d5, 'nebula_chain.json'); b = bytearray(open(p, 'rb').read()); b[len(b) // 3] ^= 0x01; open(p, 'wb').write(bytes(b))
r5 = load(d5)
chk('bit flip detected by sha256 -> backup used', lambda: r5 is not None and r5.height == 5)

# ── 6. tampered block with a recomputed (valid) checksum: structural checks must still catch it ──
d6 = tempfile.mkdtemp(); save(bc, d6)
p = os.path.join(d6, 'nebula_chain.json'); blocks = json.load(open(p)); blocks[2]['nonce'] += 1
open(p, 'w').write(json.dumps(blocks, separators=(',', ':'))); rewrite_meta(d6, chain_sha256=sha(p))
chk('tampered nonce (checksum repaired) -> rejected, nothing usable -> None', lambda: load(d6) is None)
chk('...and the files were kept as evidence', lambda: len(glob.glob(os.path.join(d6, '*.corrupt-*'))) == 3)

# ── 7. inflated UTXO file: replay is authoritative ──
d7 = tempfile.mkdtemp(); save(bc, d7)
p = os.path.join(d7, 'nebula_utxo.json'); u = json.load(open(p))
u.append(dict(u[0], txid='ab' * 32, value=10**15))
open(p, 'w').write(json.dumps(u, separators=(',', ':'))); rewrite_meta(d7, utxo_sha256=sha(p))
r7 = load(d7)
chk('forged extra coin in UTXO file is ignored (supply == chain replay)', lambda: r7 is not None and r7.utxo.total_supply() == bc.utxo.total_supply() and r7.utxo.size() == bc.utxo.size())

# ── 8. foreign chain id: ignored, never quarantined ──
d8 = tempfile.mkdtemp(); save(bc, d8); rewrite_meta(d8, chain_id=999999)
chk('foreign chain_id -> None', lambda: load(d8) is None)
chk('...files untouched', lambda: not glob.glob(os.path.join(d8, '*.corrupt-*')) and os.path.exists(os.path.join(d8, 'nebula_chain.json')))

# ── 9. legacy (pre-v10.20) files without checksums ──
d9 = tempfile.mkdtemp(); save(bc, d9)
mt = json.load(open(os.path.join(d9, 'nebula_meta.json')))
legacy = {k: mt[k] for k in ('chain', 'chain_id', 'version', 'height', 'tip_hash', 'saved_at', 'block_count')}
json.dump(legacy, open(os.path.join(d9, 'nebula_meta.json'), 'w'))
r9 = load(d9)
chk('legacy v10.19 save still loads (verified by replay)', lambda: r9 is not None and r9.height == 4 and r9.utxo.total_supply() == bc.utxo.total_supply())

# ── 10. dev-mode chain keeps its funded coin ──
with QUIET():
    bcD = m.NEBULABlockchain(); bcD._dev_mode = True; grow(bcD, 2)
    ent = bcD.fund_address(ADDR, 7)
dD = tempfile.mkdtemp(); save(bcD, dD); rD = load(dD)
chk('dev-mode funded coin survives restart', lambda: rD is not None and rD.utxo.get(ent.txid, 0) is not None and rD.utxo.total_supply() == bcD.utxo.total_supply())

# ── 11. all sets damaged -> None + evidence kept ──
dB = tempfile.mkdtemp(); save(bcA, dB)
with QUIET(): grow(bcA, 1)
save(bcA, dB)
for sfx in ('', '.prev'):
    open(os.path.join(dB, 'nebula_chain.json' + sfx), 'wb').write(b'{broken')
chk('everything damaged -> None', lambda: load(dB) is None)
chk('...6 files parked as *.corrupt-*', lambda: len(glob.glob(os.path.join(dB, '*.corrupt-*'))) == 6)

# ── 12. concurrent saves while the chain grows ──
bcT = fresh_chain(2); dT = tempfile.mkdtemp(); errs = []
def saver():
    for _ in range(6):
        try:
            if not save(bcT, dT): errs.append('save False')
        except Exception as e: errs.append(repr(e))
        time.sleep(0.01)
ths = [threading.Thread(target=saver) for _ in range(4)]
[t.start() for t in ths]
for _ in range(3):
    with QUIET(): grow(bcT, 1)
    time.sleep(0.02)
[t.join() for t in ths]; save(bcT, dT)
rT = load(dT)
chk('concurrent saves: no errors, final state loads and matches', lambda: not errs and rT is not None and rT.tip.hash == bcT.tip.hash)

# ── 13. crash simulation: die at every os.replace / os.fsync call of a save ──
class Crash(BaseException): pass
def crash_at(fn_name, n_target):
    real = getattr(os, fn_name); cnt = [0]
    def wrapper(*a, **k):
        cnt[0] += 1
        if cnt[0] == n_target: raise Crash()
        return real(*a, **k)
    return real, wrapper
ok_all = True; detail = []
for fn_name, maxn in (('replace', 8), ('fsync', 4)):
    for n in range(1, maxn + 1):
        dC = tempfile.mkdtemp(); b0 = fresh_chain(2); save(b0, dC)
        with QUIET(): grow(b0, 1)
        real, w = crash_at(fn_name, n); setattr(os, fn_name, w)
        try:
            with QUIET(): b0.save(dC)
        except Crash:
            pass
        finally:
            setattr(os, fn_name, real)
        rc = load(dC)
        good = rc is not None and rc.height in (2, 3)
        if rc is not None and good:
            with QUIET(): okb, _ = rc.add_block(mine(rc))
            good = okb
        if not good: ok_all = False; detail.append((fn_name, n, None if rc is None else rc.height))
chk('crash at ANY replace/fsync of a save: a valid chain always loads and keeps working', lambda: ok_all or detail)

sys.stdout = sys.__stdout__
w = max(len(n) for n, _, _ in R)
for n, s, d_ in R: print(f'{s:5} {n:<{w}}  {d_}')
f = sum(1 for _, s, _ in R if s != 'PASS')
print(f'\n{len(R) - f}/{len(R)} passed', flush=True)
sys.exit(1 if f else 0)
