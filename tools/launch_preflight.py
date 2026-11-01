#!/usr/bin/env python3
"""NEBULA launch preflight - run on the machine that will be a mainnet node:  python3 tools/launch_preflight.py
Exit code 0 only if every FAIL item is cleared. WARN items need a human decision. Nothing here changes any file."""
import os, sys, io, socket, contextlib, importlib.util
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV0 = dict(os.environ)   # snapshot BEFORE the module can auto-generate keys
os.environ.setdefault("NEBULA_DISABLE_CHAIN", "1")
spec = importlib.util.spec_from_file_location("nb", os.path.join(here, "nebula_v10_24.py"))
nb = importlib.util.module_from_spec(spec); sys.modules["nb"] = nb
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(nb)
res = []
def add(level, name, detail=""): res.append((level, name, detail))
add("PASS" if nb.NEBULA_NETWORK == "mainnet" else "FAIL", "network is mainnet", nb.NEBULA_NETWORK)
with contextlib.redirect_stdout(io.StringIO()):
    bc = nb.NEBULABlockchain()
g = bc.tip.header if bc.height == 0 else bc.chain[0].header
add("PASS" if g.hash() == nb.GENESIS_HASH_HEX and g.meets_target() else "FAIL", "genesis hash/PoW consistent", g.hash())
hashes = 2 ** 256 // nb.bits_to_target(nb.GENESIS_BITS)
add("WARN", "launch difficulty vs expected hashrate", f"~{hashes:,} hashes/block. At 1 GH/s that is {hashes/1e9:.2f}s per block; "
    "choose it from the hashrate you can really expect, re-mine genesis if you change it")
extra = [h for h in nb.NEBULA_CHECKPOINTS if h > 0]
add("PASS" if extra else "FAIL", "checkpoints beyond genesis", f"{len(extra)} (only possible after blocks exist; add before announcing)")
ver, _ = nb.base58check_decode(nb.FOUNDATION_ADDRESS)
add("PASS" if ver == nb.SCRIPT_ADDRESS_VERSION else "FAIL", "foundation address is a multisig (P2SH)", nb.FOUNDATION_ADDRESS)
ok = []
for h in nb.DNS_SEEDS:
    try: socket.getaddrinfo(h, nb.DEFAULT_PORT); ok.append(h)
    except Exception: pass
add("PASS" if ok else "FAIL", "at least one DNS seed resolves", f"{len(ok)}/{len(nb.DNS_SEEDS)} resolve (an offline machine always shows 0)")
add("PASS" if os.environ.get("NEBULA_P2P_TLS", "required").lower() == "required" else "FAIL", "P2P TLS required", os.environ.get("NEBULA_P2P_TLS", "required (default)"))
add("PASS" if ENV0.get("NEBULA_RPC_PASSWORD") else "WARN", "NEBULA_RPC_PASSWORD set", "else a random one is used per start")
add("PASS" if ENV0.get("NEBULA_API_KEY") else "WARN", "NEBULA_API_KEY set", "else a random key is printed at start")
add("PASS" if os.environ.get("NEBULA_BIND", "127.0.0.1") == "127.0.0.1" else "WARN", "HTTP/RPC servers on loopback", os.environ.get("NEBULA_BIND", "127.0.0.1"))
try:
    import coincurve; add("PASS", "coincurve (libsecp256k1) installed")
except Exception:
    add("FAIL", "coincurve installed", "pure-Python ECDSA is slow and not constant-time: pip install coincurve")
add("FAIL", "public testnet ran long enough", "needs a human: run a testnet with independent miners for weeks")
add("FAIL", "external security audit done", "needs a human: independent auditors")
bad = 0
for lv, n, d in res:
    print(f"{lv:5} {n}" + (f"  - {d}" if d else "")); bad += (lv == "FAIL")
print(f"\n{bad} blocking item(s)."); sys.exit(1 if bad else 0)
