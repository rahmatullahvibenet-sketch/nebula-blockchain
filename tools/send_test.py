#!/usr/bin/env python3
"""NEBULA - verify your 12 words and send a TEST payment from the genesis premine (regtest only).

    python3 tools/send_test.py --check-only      # ONLY check that your 12 words give the premine address
    python3 tools/send_test.py                   # check, then send 1,000 test NBL to a throwaway address
    python3 tools/send_test.py --amount=250      # other amount (NBL)
    python3 tools/send_test.py --expect=<ADDR>   # compare with another address (default: GENESIS_PREMINE_ADDRESS)
    python3 tools/send_test.py --dir=~/nebula_testnet

What it does
  1. Asks for the 12 words ONE AT A TIME with HIDDEN input (nothing is echoed, nothing is written to a file). After each
     word it prints "word N accepted (K letters)" so you can see that typing works. Old one-line mode: --single-line.
  2. Derives the first address (m/44'/2025'/0'/0/0) and compares it with the expected premine address.
     If it is different, the tool stops: your words do NOT control the premine. Do NOT launch the mainnet.
  3. (not with --check-only) Builds and signs a real transaction from the premine, mines one test block that contains it
     and shows the balances before and after.

Safety
  * Test network only. The chain lives in ~/nebula_testnet (nothing is sent over the internet).
  * For --check-only no chain is needed at all and no file is touched.
  * Turn off Wi-Fi/mobile data and use a keyboard WITHOUT ads / cloud features while typing the words.
    The words stay in memory only until this program exits.
"""
import os, sys, io, time, ctypes, getpass, contextlib, importlib.util

if os.environ.get("NEBULA_NETWORK", "regtest").strip().lower() != "regtest":
    sys.exit("This tool is for the TEST network only (NEBULA_NETWORK=regtest).")
os.environ["NEBULA_NETWORK"] = "regtest"
os.environ["NEBULA_DISABLE_CHAIN"] = "1"

flags = [a for a in sys.argv[1:] if a.startswith("--")]
if any(a in ("-h", "--help") for a in sys.argv[1:]):
    sys.exit(__doc__)
CHECK_ONLY = "--check-only" in flags
DATA = os.path.expanduser("~/nebula_testnet")
AMOUNT_NBL = 1000.0
EXPECT = None
for f in flags:
    if f.startswith("--dir="):
        DATA = os.path.expanduser(f.split("=", 1)[1])
    elif f.startswith("--amount="):
        AMOUNT_NBL = float(f.split("=", 1)[1])
    elif f.startswith("--expect="):
        EXPECT = f.split("=", 1)[1].strip()

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("nb", os.path.join(root, "nebula_v10_24.py"))
m = importlib.util.module_from_spec(spec)
sys.modules["nb"] = m
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    spec.loader.exec_module(m)

EXPECT = EXPECT or m.GENESIS_PREMINE_ADDRESS


def QUIET():
    return contextlib.redirect_stdout(io.StringIO())


def nbl(x):
    return x / 10 ** m.DECIMALS


# ---------------------------------------------------------------- step 1: read and check the 12 words
print("NEBULA wallet check (TEST network)")
print(f"Expected address : {EXPECT}")
try:
    m.base58check_decode(EXPECT)
except Exception:
    sys.exit("The expected address has a bad checksum. Copy it as text, never retype it.")

WORDSET = set(m.BIP39_WORDLIST)


def read_words_one_by_one(total=12):
    """Ask for the words ONE AT A TIME (hidden input). After each word the tool prints a confirmation that never
    contains the word itself (only its number and length), so you can see that typing works."""
    got = []
    print(f"\nType word 1 to {total}, ONE word per prompt, then press Enter. Nothing you type is shown.")
    print("Lower-case English letters only. Do not use the keyboard's suggestion bar.\n")
    i = 1
    while i <= total:
        w = getpass.getpass(f"Word {i}/{total}: ").strip().lower()
        if not w:
            print("   ✗ nothing was received (empty line). Type the word first, then press Enter.")
            continue
        if len(w.split()) > 1:
            print("   ✗ that looks like several words. Type only ONE word, then Enter.")
            continue
        if w not in WORDSET:
            print(f"   ✗ a {len(w)}-letter entry is not in the BIP39 word list (typo or autocorrect). Try this word again.")
            continue
        print(f"   ✓ word {i} accepted ({len(w)} letters)")
        got.append(w)
        i += 1
    return " ".join(got)


if "--single-line" in flags:
    words = getpass.getpass("Type your 12 words separated by spaces (input is hidden), then Enter: ")
    words = " ".join(words.lower().split())
else:
    words = read_words_one_by_one(12)
count = len(words.split())
if count not in (12, 15, 18, 21, 24):
    sys.exit(f"You typed {count} words; a NEBULA wallet phrase has 12 (or 15/18/21/24). Nothing was done.")
if not m.BIP39.validate(words):
    sys.exit("At least one word is not in the BIP39 word list (typo?). Check spelling word by word. Nothing was done.")

with QUIET(), contextlib.redirect_stderr(io.StringIO()):
    wallet = m.NEBULAWallet(mnemonic=words)
words = None   # drop our copy; the wallet object still holds it until exit
derived = wallet.first_address
print(f"Derived address  : {derived}")
if derived != EXPECT:
    print("\n❌ MISMATCH - these words do NOT give the premine address.")
    print("   Do not launch. Check each word and its order, and any passphrase you may have used.")
    sys.exit(2)
print("✅ MATCH - your 12 words control the premine address.")
if CHECK_ONLY:
    sys.exit(0)

# ---------------------------------------------------------------- step 2: test payment
if not os.path.exists(os.path.join(DATA, "nebula_chain.db")):
    sys.exit(f"No test chain found in {DATA}. First run: python3 tools/mine_to_address.py {EXPECT} 100")
with QUIET(), contextlib.redirect_stderr(io.StringIO()):
    bc = m.NEBULABlockchain.load(DATA)
if bc is None:
    sys.exit(f"Could not load the chain in {DATA} (wrong genesis? delete it and start again).")
wallet._utxo = bc.utxo

tip = bc.height
spendable = sum(u.value for u in wallet.spendable_utxos(lambda: bc.height))
print(f"\nChain height {tip} | spendable now {nbl(spendable):,.2f} NBL")
if spendable < int((AMOUNT_NBL + 0.001) * 10 ** m.DECIMALS):
    sys.exit("Not enough spendable coins. Mine 100+ blocks to the premine address first (tools/mine_to_address.py).")

# a throwaway destination: its words are never shown or stored (test coins only)
with QUIET(), contextlib.redirect_stderr(io.StringIO()):
    dest_wallet = m.NEBULAWallet(utxo_set=bc.utxo)
DEST = dest_wallet.first_address
before_src = sum(bc.utxo.balance(a) for a in list(wallet._keys))
before_dst = bc.utxo.balance(DEST)

FEE_NBL = 0.001
with QUIET(), contextlib.redirect_stderr(io.StringIO()):
    tx = wallet.build_transaction(DEST, AMOUNT_NBL, fee_nbl=FEE_NBL)
if tx is None:
    sys.exit("The wallet could not build the transaction.")
with QUIET(), contextlib.redirect_stderr(io.StringIO()):
    ok, msg = bc.add_to_mempool(tx)
print(f"Transaction      : {tx.txid}")
print(f"Mempool          : {'accepted' if ok else 'REJECTED - ' + str(msg)}")
if not ok:
    sys.exit(3)


def solve(hdr):
    if getattr(m, "_NBL_ACCEL_OK", False):
        h76 = hdr.serialize()[:76]
        tgt = m.bits_to_target(hdr.bits).to_bytes(32, "big")
        found = ctypes.c_uint32(0)
        hashes = ctypes.c_uint64(0)
        n = 0
        while n < 2 ** 32:
            end = min(n + 0xFFFFF, 2 ** 32 - 1)
            if m._NBL_C_MINE(h76, tgt, ctypes.c_uint32(n), ctypes.c_uint32(end),
                             ctypes.byref(found), ctypes.byref(hashes)) == 1:
                hdr.nonce = found.value
                return
            n = end + 1
    else:
        hdr.nonce = 0
        while not hdr.meets_target():
            hdr.nonce += 1


# mine ONE test block that contains the payment (the reward goes back to the premine wallet)
prev = bc.tip
h = prev.height + 1
fees = tx.fee(bc.utxo)
cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h) + fees, miner_address=derived)
allt = [cb, tx]
root_ = m.MerkleTree.compute_root([t.txid for t in allt])
ts = max(int(time.time()) - 60, prev.header.timestamp + 1)
hdr = m.BlockHeader(1, prev.hash, root_, ts, bc.get_next_bits(), 0, h)
solve(hdr)
blk = m.Block(hdr, allt)
with QUIET(), contextlib.redirect_stderr(io.StringIO()):
    ok, msg = bc.add_block(blk)
    if ok:
        bc.save(DATA)
print(f"Block {h}        : {'accepted' if ok else 'REJECTED - ' + str(msg)}")
if not ok:
    sys.exit(4)

after_src = sum(bc.utxo.balance(a) for a in list(wallet._keys))
after_dst = bc.utxo.balance(DEST)
print(f"\nDestination      : {DEST}")
print(f"  received       : {nbl(after_dst - before_dst):,.4f} NBL")
print(f"Premine wallet (incl. change) before: {nbl(before_src):,.2f} NBL, after: {nbl(after_src):,.2f} NBL")
print(f"Fee paid to the miner of that block: {FEE_NBL} NBL")
good = (after_dst - before_dst) == int(AMOUNT_NBL * 10 ** m.DECIMALS)
print("\n✅ TEST PAYMENT WORKS - the premine can be spent with your 12 words." if good
      else "\n⚠️ The destination did not receive the expected amount - send me this output.")
sys.exit(0 if good else 5)
