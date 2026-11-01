"""v10.24: mainnet/regtest split, genesis, checkpoints, P2SH address locking, bind/RPC defaults.
Runs each network in its OWN subprocess (the network is fixed at import time)."""
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
g = bc.chain[0].header if hasattr(bc, "chain") and bc.chain else bc.tip.header
out = dict(net=m.NEBULA_NETWORK, bits=hex(m.GENESIS_BITS), init=hex(m.INITIAL_BITS),
           genesis=g.hash(), meets=g.meets_target(), const=m.GENESIS_HASH_HEX,
           cp0=m.CHECKPOINTS[0], cp1=m.NEBULA_CHECKPOINTS[0],
           limit_eq=(m.bits_to_target(m.INITIAL_BITS) == m.MAX_TARGET),
           bind=m._nbl_default_bind(),
           msc=m.Script.p2pkh_locking_from_address(m.base58check_encode(b"\x22"*20, m.SCRIPT_ADDRESS_VERSION)).hex(),
           orphan=type(m.P2PNode(bc).orphan_pool).__name__)
print("JSON" + json.dumps(out))
'''
def run(net):
    env = dict(os.environ, NEBULA_NETWORK=net); env.pop("NEBULA_BIND", None)
    r = subprocess.run([sys.executable, "-c", CHILD, here], env=env, capture_output=True, text=True, timeout=300)
    line = [l for l in r.stdout.splitlines() if l.startswith("JSON")]
    return json.loads(line[0][4:]) if line else {"error": r.stderr[-300:]}
R = []
def chk(n, c): R.append((n, bool(c)))
main, reg = run("mainnet"), run("regtest")
unk = run("garbage-value")
chk("mainnet: default network is mainnet", main.get("net") == "mainnet")
chk("mainnet: unknown NEBULA_NETWORK value fails closed to mainnet", unk.get("net") == "mainnet")
chk("mainnet: launch difficulty 0x1d0fffff", main.get("bits") == "0x1d0fffff" and main.get("init") == "0x1d0fffff")
chk("mainnet: genesis block meets its own PoW", main.get("meets") is True)
chk("mainnet: built genesis hash == GENESIS_HASH_HEX", main.get("genesis") == main.get("const"))
chk("mainnet: both checkpoint tables hold the genesis hash", main.get("cp0") == main.get("const") == main.get("cp1"))
chk("mainnet: PoW limit == launch difficulty", main.get("limit_eq") is True)
chk("regtest: old difficulty and genesis kept", reg.get("bits") == "0x1e0fffff" and reg.get("genesis") == reg.get("const"))
chk("networks have different genesis hashes", main.get("genesis") != reg.get("genesis"))
chk("P2SH ('M...') address gets an OP_HASH160 locking script", main.get("msc") == "a914" + "22"*20 + "87")
chk("OrphanPool no longer raises NameError in P2PNode", main.get("orphan") == "OrphanPool")
chk("non-P2P servers bind to loopback by default", main.get("bind") == "127.0.0.1")
bad = 0
for n, ok in R:
    print(("PASS  " if ok else "FAIL  ") + n); bad += (not ok)
print(f"{len(R)-bad}/{len(R)}")
if bad: print(main, reg)
sys.exit(1 if bad else 0)
