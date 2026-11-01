#!/usr/bin/env python3
"""NEBULA - generate ONE foundation signing key. Run it on an OFFLINE computer (Wi-Fi/cable off), once per key,
on three DIFFERENT computers/people for a 2-of-3 foundation.
It prints the PUBLIC key (safe to share) and the PRIVATE key (secret: write it on paper, never photograph,
never send, never paste into any chat or cloud). Nothing is written to disk."""
import os, sys, importlib.util
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("NEBULA_DISABLE_CHAIN", "1")
import io, contextlib
spec = importlib.util.spec_from_file_location("nb", os.path.join(here, "nebula_v10_24.py"))
nb = importlib.util.module_from_spec(spec); sys.modules["nb"] = nb
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(nb)
priv, pub = nb.Secp256k1.generate_keypair()
pub_b = nb.Secp256k1.pubkey_to_bytes(pub)
assert len(pub_b) == 33 and pub_b[0] in (2, 3)
priv_hex = priv.to_bytes(32, "big").hex() if isinstance(priv, int) else bytes(priv).hex()
print("PUBLIC key  (send this to the person who builds the address):\n  " + pub_b.hex())
print("\nPRIVATE key (SECRET - paper only, keep 2 copies in 2 safe places):\n  " + priv_hex)
print("\nAfter writing it down, close this window. Do NOT re-run to 'check' - each run makes a NEW key.")
