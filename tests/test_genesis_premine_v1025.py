"""v10.25: genesis premine (1,035,000 NBL to the founder wallet). Each network runs in its own subprocess."""
import os, sys, subprocess, json
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHILD = r'''
import os, sys, io, json, contextlib, importlib.util
os.environ["NEBULA_DISABLE_CHAIN"] = "1"
spec = importlib.util.spec_from_file_location("nb", os.path.join(sys.argv[1], "nebula_v10_24.py"))
m = importlib.util.module_from_spec(spec); sys.modules["nb"] = m
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(m)
    bc = m.NEBULABlockchain()
g = bc.tip
cb = g.transactions[0]
addr = m.GENESIS_PREMINE_ADDRESS
script = m.Script.p2pkh_locking_from_address(addr)
paid = sum(o.value for o in cb.outputs if o.script_pubkey == script)
out = dict(net=m.NEBULA_NETWORK, height=bc.height, hash=g.hash, const=m.GENESIS_HASH_HEX,
           meets=g.header.meets_target(), merkle_ok=g.verify_merkle(),
           paid=paid, want=m.GENESIS_PREMINE_AMOUNT, outs=len(cb.outputs),
           balance=bc.utxo.balance(addr), reward0=cb.outputs[0].value, is_cb=cb.is_coinbase,
           total=bc.utxo.total_supply())
print("JSON" + json.dumps(out))
'''
def run(net):
    env = dict(os.environ, NEBULA_NETWORK=net)
    r = subprocess.run([sys.executable, "-c", CHILD, here], env=env, capture_output=True, text=True, timeout=300)
    line = [l for l in r.stdout.splitlines() if l.startswith("JSON")]
    return json.loads(line[0][4:]) if line else {"error": r.stderr[-400:]}
R = []
def chk(n, c): R.append((n, bool(c)))
for net in ("mainnet", "regtest"):
    d = run(net)
    chk(f"{net}: chain builds (no error)", "error" not in d)
    chk(f"{net}: genesis hash == GENESIS_HASH_HEX", d.get("hash") == d.get("const"))
    chk(f"{net}: genesis meets its own proof of work", d.get("meets") is True)
    chk(f"{net}: genesis merkle root verifies", d.get("merkle_ok") is True)
    chk(f"{net}: genesis coinbase has exactly 2 outputs", d.get("outs") == 2)
    chk(f"{net}: premine output == 1,035,000 NBL", d.get("paid") == 1_035_000 * 10**9 == d.get("want"))
    chk(f"{net}: premine address balance == 1,035,000 NBL", d.get("balance") == 1_035_000 * 10**9)
    chk(f"{net}: normal 50 NBL genesis reward kept", d.get("reward0") == 50 * 10**9)
    chk(f"{net}: total supply at genesis == 1,035,050 NBL", d.get("total") == 1_035_050 * 10**9)
bad = [n for n, ok in R if not ok]
for n, ok in R: print(("PASS " if ok else "FAIL ") + n)
print(f"\n{len(R)-len(bad)}/{len(R)} passed")
sys.exit(1 if bad else 0)
