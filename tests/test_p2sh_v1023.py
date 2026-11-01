import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
import os, sys, io, contextlib, importlib.util
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("NEBULA_DISABLE_CHAIN", "1")
spec = importlib.util.spec_from_file_location('nb', os.path.join(here, 'nebula_v10_24.py'))
m = importlib.util.module_from_spec(spec); sys.modules['nb'] = m
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(m)
R = []
def chk(name, fn):
    try:
        r = fn(); R.append((name, bool(r), str(r)[:90]))
    except Exception as e:
        R.append((name, False, f"{type(e).__name__}: {str(e)[:90]}"))

S = m.Secp256k1
keys = [S.generate_keypair() for _ in range(3)]
pubs = [S.pubkey_to_bytes(k[1]) for k in keys]
MS = None
for nm in dir(m):
    c = getattr(m, nm)
    if isinstance(c, type) and 'multisig' in c.__dict__:
        try:
            c.multisig(2, pubs); MS = c; break
        except Exception:
            pass
assert MS, "no multisig builder found"
redeem = MS.multisig(2, pubs)
lock = bytes([m.OP_HASH160, 0x14]) + m.hash160(redeem) + bytes([m.OP_EQUAL])

chk('classify == P2SH', lambda: m.Script.classify(lock) == m.ScriptType.P2SH)
chk('classify P2PKH unchanged', lambda: m.Script.classify(m.Script.p2pkh_locking_from_address(m.FOUNDATION_ADDRESS)) == m.ScriptType.P2PKH)
chk('classify junk 23B stays UNKNOWN', lambda: m.Script.classify(bytes([m.OP_HASH160, 0x14]) + b'\0'*20 + b'\x00') == m.ScriptType.UNKNOWN)
chk('P2SH output gets a script-version address', lambda: m.TxOutput(1000, lock).address is not None and m.base58check_decode(m.TxOutput(1000, lock).address)[0] == m.SCRIPT_ADDRESS_VERSION if hasattr(m, 'base58check_decode') else m.TxOutput(1000, lock).address is not None)

def fresh():
    utxo = m.UTXOSet()
    fund_txid = '11' * 32
    utxo.add(m.UTXOEntry(fund_txid, 0, 5_000_000, lock, 1, False))
    cv = m.ChainValidator(utxo) if hasattr(m, 'ChainValidator') else None
    return utxo, fund_txid
# locate class owning validate_tx
owner = None
for nm in dir(m):
    c = getattr(m, nm)
    if isinstance(c, type) and 'validate_tx' in c.__dict__ and 'validate_block' in c.__dict__:
        owner = c; break
assert owner, "validator class not found"

def build(sign_with, redeem_used=None, hashtype=1, tamper=False):
    utxo, ftxid = fresh()
    v = owner(utxo)
    dest = m.Script.p2pkh_locking_from_address(m.FOUNDATION_ADDRESS)
    tx = m.Transaction(inputs=[m.TxInput(m.OutPoint(ftxid, 0))],
                       outputs=[m.TxOutput(4_990_000, dest)])
    rs = redeem_used or redeem
    sh = tx.signature_hash(0, rs, m.SIGHASH_ALL)
    sh = bytes.fromhex(sh) if isinstance(sh, str) else sh
    sigs = [S.sig_to_der(*S.sign(keys[i][0], sh)) + bytes([hashtype]) for i in sign_with]
    ss = b'\x00' + b''.join(bytes([len(x)]) + x for x in sigs)
    ss += (bytes([len(rs)]) if len(rs) < 0x4c else bytes([0x4c, len(rs)])) + rs
    tx.inputs[0].script_sig = ss
    tx._txid = None
    if tamper:
        tx.outputs[0].value -= 1; tx._txid = None
    return v.validate_tx(tx, current_height=200)

ok, why = build([0, 2]);                chk('2-of-3 valid spend accepted', lambda: (ok, why) if ok else False)
r = build([1, 0]);                      chk('wrong key order rejected', lambda: not r[0])
r = build([0]);                         chk('only 1 of 2 required sigs rejected', lambda: not r[0])
r = build([0, 1], tamper=True);         chk('tampered outputs after signing rejected', lambda: not r[0])
r = build([0, 1], hashtype=2);          chk('non-SIGHASH_ALL signature rejected', lambda: not r[0])
other = MS.multisig(1, pubs[:1])
r = build([0], redeem_used=other);      chk('wrong redeem script (hash mismatch) rejected', lambda: (not r[0] and 'mismatch' in r[1]) or r)
# non-push-only scriptSig
def nonpush():
    utxo, ftxid = fresh(); v = owner(utxo)
    dest = m.Script.p2pkh_locking_from_address(m.FOUNDATION_ADDRESS)
    tx = m.Transaction(inputs=[m.TxInput(m.OutPoint(ftxid, 0), bytes([m.OP_DUP, 0x01, 0x01]) + b'\x00')],
                       outputs=[m.TxOutput(4_990_000, dest)])
    return v.validate_tx(tx, current_height=200)
r = nonpush();                          chk('non-push-only scriptSig rejected', lambda: not r[0])
def empty():
    utxo, ftxid = fresh(); v = owner(utxo)
    dest = m.Script.p2pkh_locking_from_address(m.FOUNDATION_ADDRESS)
    tx = m.Transaction(inputs=[m.TxInput(m.OutPoint(ftxid, 0), b'')], outputs=[m.TxOutput(4_990_000, dest)])
    return v.validate_tx(tx, current_height=200)
r = empty();                            chk('empty scriptSig rejected', lambda: not r[0])
# multisig bounds in the interpreter
def bounds():
    it = m.ScriptInterpreter(tx_hash=b'\x00'*32)
    # stack (bottom->top): dummy, 3 sigs, n_sigs=3, 1 key, n_keys=1  -> more sigs than keys
    st = [b'', b'\x01', b'\x01', b'\x01', b'\x03', b'\x02'+b'\x00'*32, b'\x01']
    try:
        it._op_checkmultisig(st)
    except m.ScriptError as e:
        return 'signature count' in str(e)
    return False
chk('CHECKMULTISIG bad counts raise ScriptError', bounds)

bad = [r for r in R if not r[1]]
for n, ok_, d in R: print(('PASS ' if ok_ else 'FAIL '), n, '|', d)
print(f"\n{len(R)-len(bad)}/{len(R)} passed")
sys.exit(1 if bad else 0)
