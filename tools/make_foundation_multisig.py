#!/usr/bin/env python3
"""NEBULA - build the foundation M-of-N multisig (P2SH) address from PUBLIC keys only.
Usage: NEBULA_NETWORK=regtest python3 tools/make_foundation_multisig.py 2 <pubkey1_hex> <pubkey2_hex> <pubkey3_hex> ...
Each pubkey = 33-byte compressed key (66 hex chars), generated on a DIFFERENT device (ideally hardware wallets).
Never type a private key here. Put the printed address into FOUNDATION_ADDRESS BEFORE re-mining the genesis."""
import os, sys, importlib.util
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("NEBULA_DISABLE_CHAIN", "1")
spec = importlib.util.spec_from_file_location("nb", os.path.join(here, "nebula_v10_24.py"))
nb = importlib.util.module_from_spec(spec); sys.modules["nb"] = nb; spec.loader.exec_module(nb)
if len(sys.argv) < 4: sys.exit(__doc__)
m = int(sys.argv[1]); keys = [bytes.fromhex(k) for k in sys.argv[2:]]
n = len(keys)
assert 1 <= m <= n <= 15, "need 1 <= M <= N <= 15"
for k in keys: assert len(k) == 33 and k[0] in (2, 3), "compressed pubkeys only"
redeem = bytes([0x50 + m]) + b"".join(bytes([33]) + k for k in keys) + bytes([0x50 + n, nb.OP_CHECKMULTISIG])
assert len(redeem) <= 520
addr = nb.base58check_encode(nb.hash160(redeem), nb.SCRIPT_ADDRESS_VERSION)
print(f"{m}-of-{n} foundation address : {addr}")
print(f"redeem script (KEEP A COPY)   : {redeem.hex()}")
