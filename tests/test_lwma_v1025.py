"""v10.25e: per-block LWMA difficulty + easier PoW limit (mainnet). Unit tests with fake chains + a real-PoW regtest chain."""
import os, sys, subprocess, json, types
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CHILD_UNIT = r'''
import os, sys, io, json, contextlib, importlib.util, types
os.environ["NEBULA_DISABLE_CHAIN"] = "1"
spec = importlib.util.spec_from_file_location("nb", os.path.join(sys.argv[1], "nebula_v10_24.py"))
m = importlib.util.module_from_spec(spec); sys.modules["nb"] = m
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(m)
T = m.TARGET_BLOCK_TIME
def mk(h, ts, bits): return types.SimpleNamespace(height=h, hash=f"h{h}", header=types.SimpleNamespace(timestamp=ts, bits=bits))
def run(n, st_fn, start_bits=None):
    bits = start_bits or m.GENESIS_BITS
    ch = [mk(0, 1742083200, bits)]
    ts = 1742083200
    for h in range(1, n + 1):
        nb_ = m.lwma_next_bits(ch, h - 1) if h > 1 else ch[0].header.bits
        ts += st_fn(h)
        ch.append(mk(h, ts, nb_))
    return ch
out = {"algo": m.DIFF_ALGO, "net": m.NEBULA_NETWORK, "max_ok": m.bits_to_target(m.GENESIS_BITS) <= m.MAX_TARGET,
       "max_is_2e20": m.MAX_TARGET == m.bits_to_target(0x1e0fffff)}
g = m.bits_to_target(m.GENESIS_BITS)
# 1 steady
ch = run(200, lambda h: T)
t = m.bits_to_target(m.lwma_next_bits(ch, 200))
out["steady_ratio"] = t / g
# 2 fast blocks (60s) -> harder
ch = run(150, lambda h: 60)
out["fast_ratio"] = m.bits_to_target(m.lwma_next_bits(ch, 150)) / g
# 3 slow blocks -> easier, bounded by MAX_TARGET
ch = run(400, lambda h: 6 * T)
t = m.bits_to_target(m.lwma_next_bits(ch, 400))
out["slow_at_max"] = t <= m.MAX_TARGET and t > g
out["slow_ratio_vs_max"] = t / m.MAX_TARGET
# 4 never more than 2x per block
worst = 0
for stf in (lambda h: 1, lambda h: 6 * T, lambda h: T if h % 2 else 1, lambda h: 10 if h % 7 else 6 * T):
    ch = run(200, stf)
    for h in range(2, 201):
        a = m.bits_to_target(ch[h - 1].header.bits); b = m.bits_to_target(ch[h].header.bits)
        worst = max(worst, a / b, b / a)
out["worst_step"] = worst
# 5 weird timestamps (negative solvetime) do not crash / stay in range
ch = run(80, lambda h: -5000 if h % 3 == 0 else T)
t = m.bits_to_target(m.lwma_next_bits(ch, 80))
out["neg_ok"] = 0 < t <= m.MAX_TARGET
# 6 validator.expected_bits == lwma on a fake chain, None on wrong ancestry, tolerant w/o chain
ch = run(100, lambda h: T)
v = m.ChainValidator(None)
out["val_match"] = v.expected_bits(ch[100], ch) == m.lwma_next_bits(ch, 100)
bad = mk(100, 0, 0); bad.hash = "other"
out["val_none"] = v.expected_bits(bad, ch) is None
out["val_nochain"] = v.expected_bits(ch[100], None) == ch[100].header.bits
out["val_genesis"] = v.expected_bits(ch[0], ch) == ch[0].header.bits
# 7 determinism
out["det"] = m.lwma_next_bits(ch, 100) == m.lwma_next_bits(list(ch), 100)
print("JSON" + json.dumps(out))
'''

def run_unit(net, extra_env=None):
    env = dict(os.environ, NEBULA_NETWORK=net); env.update(extra_env or {})
    r = subprocess.run([sys.executable, "-c", CHILD_UNIT, here], env=env, capture_output=True, text=True, timeout=300)
    l = [x for x in r.stdout.splitlines() if x.startswith("JSON")]
    return json.loads(l[0][4:]) if l else {"error": r.stderr[-600:]}

CHILD_CHAIN = r'''
import os, sys, io, json, time, ctypes, contextlib, importlib.util
os.environ["NEBULA_DISABLE_CHAIN"] = "1"; os.environ["NEBULA_NETWORK"] = "regtest"; os.environ["NEBULA_DIFF_ALGO"] = "lwma"
spec = importlib.util.spec_from_file_location("nb", os.path.join(sys.argv[1], "nebula_v10_24.py"))
m = importlib.util.module_from_spec(spec); sys.modules["nb"] = m
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    spec.loader.exec_module(m)
    bc = m.NEBULABlockchain()
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
addr = "NYeuFNDnykFEhKWQnCCPeyFQFEKX2qs1oh"
def mine(spacing, count, wrong_bits=False):
    res = []
    for _ in range(count):
        prev = bc.tip; h = prev.height + 1
        bits = bc.get_next_bits()
        if wrong_bits: bits = m.target_to_bits(m.bits_to_target(bits) * 3)
        cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h), miner_address=addr)
        root = m.MerkleTree.compute_root([cb.txid])
        ts = prev.header.timestamp + spacing
        hdr = m.BlockHeader(1, prev.hash, root, ts, bits, 0, h)
        solve(hdr)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            ok, msg = bc.add_block(m.Block(hdr, [cb]))
        res.append((ok, msg, bits))
        if not ok: break
    return res
g = m.bits_to_target(m.GENESIS_BITS)
r1 = mine(600, 25)
t_steady = m.bits_to_target(bc.get_next_bits()) / g
r2 = mine(150, 8)                       # blocks 4x faster than target -> difficulty must rise
t_fast = m.bits_to_target(bc.get_next_bits()) / g
h_before = bc.height
r3 = mine(600, 1, wrong_bits=True)      # block with a wrong difficulty must be rejected
print("JSON" + json.dumps(dict(ok1=all(x[0] for x in r1), n1=len(r1), t_steady=t_steady,
      ok2=all(x[0] for x in r2), t_fast=t_fast, wrong_rejected=(not r3[0][0]), wrong_msg=str(r3[0][1])[:80],
      height_unchanged=(bc.height == h_before), height=bc.height)))
'''

def run_chain():
    r = subprocess.run([sys.executable, "-c", CHILD_CHAIN, here], capture_output=True, text=True, timeout=600)
    l = [x for x in r.stdout.splitlines() if x.startswith("JSON")]
    return json.loads(l[0][4:]) if l else {"error": r.stderr[-800:]}

R = []
def chk(n, c): R.append((n, bool(c)))
u = run_unit("mainnet")
chk("mainnet: unit run ok", "error" not in u)
chk("mainnet uses the LWMA algorithm", u.get("algo") == "lwma")
chk("mainnet: genesis difficulty is within the PoW limit", u.get("max_ok"))
chk("mainnet: PoW limit is the easy 2^20 level (miners can never get stuck)", u.get("max_is_2e20"))
chk("steady 10-minute blocks keep difficulty stable (+-5%)", 0.95 < u.get("steady_ratio", 0) < 1.05)
chk("blocks 10x too fast make the next block much harder", u.get("fast_ratio", 9) < 0.2)
chk("blocks too slow make it easier and it stops at the PoW limit", u.get("slow_at_max") and u.get("slow_ratio_vs_max") > 0.99)
chk("difficulty never changes more than 2x in one block", u.get("worst_step", 99) <= 2.001)   # tolerance = compact-bits rounding
chk("negative/odd timestamps are clamped (no crash, in range)", u.get("neg_ok"))
chk("validator expected_bits == lwma_next_bits", u.get("val_match"))
chk("validator: unknown ancestry -> None", u.get("val_none"))
chk("validator: no chain -> previous bits (like before)", u.get("val_nochain"))
chk("validator: genesis -> genesis bits", u.get("val_genesis"))
chk("deterministic", u.get("det"))
u2 = run_unit("mainnet", {"NEBULA_DIFF_ALGO": "legacy"})
chk("mainnet cannot be switched to legacy by an env var", u2.get("algo") == "lwma")
u3 = run_unit("regtest")
chk("regtest keeps the legacy retarget by default (fast dev chains)", u3.get("algo") == "legacy")
c = run_chain()
chk("real chain: no error", "error" not in c)
chk("real chain: 25 blocks at 600 s all accepted", c.get("ok1") and c.get("n1") == 25)
chk("real chain: difficulty stays ~stable at 600 s spacing", 0.9 < c.get("t_steady", 0) < 1.1)
chk("real chain: 8 blocks at 150 s all accepted", c.get("ok2"))
chk("real chain: difficulty rose after fast blocks", c.get("t_fast", 9) < 0.95)
chk("real chain: block with wrong bits is rejected", c.get("wrong_rejected") and c.get("height_unchanged"))
bad = [n for n, ok in R if not ok]
for n, ok in R: print(("PASS " if ok else "FAIL ") + n)
print(f"\n{len(R)-len(bad)}/{len(R)} passed")
if "error" in c: print(c["error"])
sys.exit(1 if bad else 0)
