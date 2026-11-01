#!/usr/bin/env python3
"""Mine the genesis nonce for the CURRENT network (set NEBULA_NETWORK=regtest or leave unset for mainnet).

Usage:
    python3 tools/mine_genesis_v1025.py            # mainnet
    NEBULA_NETWORK=regtest python3 tools/mine_genesis_v1025.py

Run it again whenever GENESIS_PREMINE_ADDRESS, GENESIS_PREMINE_AMOUNT, GENESIS_TIMESTAMP or GENESIS_MESSAGE
change. Then paste the printed GENESIS_NONCE and genesis hash into nebula_v10_24.py (GENESIS_NONCE / GENESIS_HASH_HEX).
"""
import os, sys, io, contextlib, importlib.util

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("NEBULA_DISABLE_CHAIN", "1")
spec = importlib.util.spec_from_file_location("nb", os.path.join(here, "nebula_v10_24.py"))
nb = importlib.util.module_from_spec(spec)
sys.modules["nb"] = nb
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(nb)

print(f"Network        : {nb.NEBULA_NETWORK}")
print(f"Premine        : {nb.GENESIS_PREMINE_AMOUNT / 10 ** nb.DECIMALS:,.0f} NBL -> {nb.GENESIS_PREMINE_ADDRESS}")
print(f"Accelerated C  : {getattr(nb, '_NBL_ACCEL_OK', False)}")
nonce, ghash = nb.mine_genesis(nb.GENESIS_BITS)
print("\nPaste into nebula_v10_24.py for this network:")
print(f"    GENESIS_NONCE    = {nonce}")
print(f'    GENESIS_HASH_HEX = "{ghash}"')
