"""NEBULA hardening pack - fixes for real weaknesses found while auditing groups 46..63.

Apply once, AFTER the groups are installed (or before - it only patches classes):

    import nebula_hardening as hard
    report = hard.apply(host)          # host may be None
    print(report)

What is fixed here (all fixes are fail-closed and use only the standard library):

 1. ScriptEngine (group48)
      - OP_CHECKSIG used to push "valid" for ANY signature.  Now it needs a real
        verifier (context["verify_sig"] or ScriptEngine.signature_verifier) and
        fails closed when none is configured.
      - eval_p2pkh() set the stack and then execute() cleared it, so P2PKH never
        evaluated.  Fixed (stack is kept for eval_p2pkh).
      - Truncated pushes were silently ignored; now the script is invalid.
      - Added script-size and op-count limits (DoS protection).
 2. WalletBackupManager (group55)
      - Mnemonic was "encrypted" with a repeating XOR key (2048 PBKDF2 rounds, no
        authentication).  Now: PBKDF2-HMAC-SHA256 (600k rounds) + HMAC-SHA256
        counter-mode keystream + encrypt-then-MAC tag (constant-time compare).
        Version-1 backups can still be restored.
 3. ThresholdSignatureScheme (group51)
      - generate_shares() produced sha256(secret||i): shares could not recover the
        secret.  Now real Shamir secret sharing over GF(2**521 - 1).
        New: recover_secret(shares).
 4. PrivacyTransaction (group49)
      - random.shuffle (predictable) -> secrets.SystemRandom.
      - Decoys were always the first N addresses -> random sample.
      - Commitment was truncated mod 2**32 (destroyed binding) -> full values.
      - Key image depended on the amount (double spends with another amount were
        not linked) and was brute-forceable from the address list -> keyed HMAC of
        the sender only.
      - Input validation and a cap on stored transactions.
      NOTE: this is still NOT a real ring signature.  The result is labelled
      experimental so nobody relies on it for anonymity.
 5. OptimisticRollup (group58)
      - submit_fraud_proof() accepted ANY text and froze the batch (free griefing).
        Now it needs a configured verifier (OptimisticRollup.fraud_verifier) and
        rejects duplicates; with no verifier it fails closed.

Known weaknesses that are documented but NOT fixable without new cryptography
(see the audit report): ZKRollupLayer proof is a hash (not a ZK proof),
BLSAggregatedMultisig XOR aggregation, TaprootEngine 4-byte XOR tweak.
"""
from __future__ import annotations

import hashlib
import hmac
import importlib
import secrets
import threading
from typing import Any, Callable, Dict, List, Optional
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

# --------------------------------------------------------------------------- #
# 1. Script engine
# --------------------------------------------------------------------------- #
MAX_SCRIPT_BYTES = 10_000
MAX_SCRIPT_OPS = 201


def _make_execute(module: Any) -> Callable:
    Op = module.ScriptOpCode
    hash160 = module.hash160

    def execute(self, script: bytes, context: dict = None, keep_stack: bool = False) -> bool:
        context = context or {}
        if not isinstance(script, (bytes, bytearray)) or len(script) > MAX_SCRIPT_BYTES:
            return False
        if not keep_stack:
            self._stack.clear()
        ops = 0
        i = 0
        n = len(script)
        while i < n:
            op = script[i]
            i += 1
            ops += 1
            if ops > MAX_SCRIPT_OPS:
                return False
            if 0x01 <= op <= 0x4B:                    # direct data push (includes 0x14)
                if i + op > n:
                    return False                       # truncated push => invalid
                self._stack.append(bytes(script[i:i + op]))
                i += op
            elif op == Op.OP_DUP:
                if not self._stack:
                    return False
                self._stack.append(self._stack[-1])
            elif op == Op.OP_HASH160:
                if not self._stack:
                    return False
                self._stack.append(hash160(self._stack.pop()))
            elif op == Op.OP_EQUALVERIFY:
                if len(self._stack) < 2:
                    return False
                a, b = self._stack.pop(), self._stack.pop()
                if not hmac.compare_digest(a, b):
                    return False
            elif op == Op.OP_EQUAL:
                if len(self._stack) < 2:
                    return False
                a, b = self._stack.pop(), self._stack.pop()
                self._stack.append(b"\x01" if hmac.compare_digest(a, b) else b"\x00")
            elif op == Op.OP_CHECKSIG:
                if len(self._stack) < 2:
                    return False
                pubkey = self._stack.pop()
                sig = self._stack.pop()
                verifier = context.get("verify_sig") or getattr(self, "signature_verifier", None)
                if verifier is None:
                    return False                       # fail closed: never "always valid"
                try:
                    ok = bool(verifier(sig, pubkey, context.get("sighash")))
                except Exception:
                    ok = False
                self._stack.append(b"\x01" if ok else b"\x00")
            elif op == Op.OP_DROP:
                if not self._stack:
                    return False
                self._stack.pop()
            elif op == Op.OP_RETURN:
                return False
            else:
                return False                           # unknown opcode => invalid
            self._ops_executed += 1
        return bool(self._stack and self._stack[-1] not in (b"", b"\x00"))

    return execute


def _make_eval_p2pkh(module: Any) -> Callable:
    Op = module.ScriptOpCode

    def eval_p2pkh(self, pubkey_hash: bytes, pubkey: bytes, sig: bytes,
                   context: dict = None) -> bool:
        if len(pubkey_hash) != 20:
            return False
        script = (bytes([Op.OP_DUP, Op.OP_HASH160, 0x14]) + pubkey_hash +
                  bytes([Op.OP_EQUALVERIFY, Op.OP_CHECKSIG]))
        self._stack = [sig, pubkey]
        return self.execute(script, context, keep_stack=True)

    return eval_p2pkh


# --------------------------------------------------------------------------- #
# 2. Encrypted wallet backup
# --------------------------------------------------------------------------- #
BACKUP_PBKDF2_ROUNDS = 600_000


def _keystream(key: bytes, nonce: bytes, length: int) -> bytes:
    out = bytearray()
    counter = 0
    while len(out) < length:
        out += hmac.new(key, nonce + counter.to_bytes(8, "big"), hashlib.sha256).digest()
        counter += 1
    return bytes(out[:length])


def _derive_keys(passphrase: str, salt: bytes, rounds: int):
    material = hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt, rounds, dklen=64)
    return material[:32], material[32:]


def encrypt_secret(data: bytes, passphrase: str) -> dict:
    salt = secrets.token_bytes(32)
    nonce = secrets.token_bytes(16)
    enc_key, mac_key = _derive_keys(passphrase, salt, BACKUP_PBKDF2_ROUNDS)
    ks = _keystream(enc_key, nonce, len(data))
    ct = bytes(a ^ b for a, b in zip(data, ks))
    tag = hmac.new(mac_key, b"NBLBK2" + salt + nonce + ct, hashlib.sha256).digest()
    return {"version": 2, "kdf": "pbkdf2-sha256", "rounds": BACKUP_PBKDF2_ROUNDS,
            "salt": salt.hex(), "nonce": nonce.hex(), "encrypted": ct.hex(), "tag": tag.hex()}


def decrypt_secret(backup: dict, passphrase: str) -> Optional[bytes]:
    try:
        if backup.get("version") != 2:
            return None
        rounds = int(backup["rounds"])
        if not (100_000 <= rounds <= 5_000_000):
            return None
        salt = bytes.fromhex(backup["salt"])
        nonce = bytes.fromhex(backup["nonce"])
        ct = bytes.fromhex(backup["encrypted"])
        tag = bytes.fromhex(backup["tag"])
        enc_key, mac_key = _derive_keys(passphrase, salt, rounds)
        expect = hmac.new(mac_key, b"NBLBK2" + salt + nonce + ct, hashlib.sha256).digest()
        if not hmac.compare_digest(expect, tag):
            return None                                # wrong passphrase OR tampered
        ks = _keystream(enc_key, nonce, len(ct))
        return bytes(a ^ b for a, b in zip(ct, ks))
    except Exception:
        return None


def _make_backup_methods(module: Any):
    kdf = getattr(module, "KeyDerivationFunction", None)

    def create_encrypted_backup(self, wallet, passphrase: str) -> dict:
        if not isinstance(passphrase, str) or len(passphrase) < 8:
            raise ValueError("passphrase must be at least 8 characters")
        backup = encrypt_secret(wallet.mnemonic.encode("utf-8"), passphrase)
        backup["address"] = wallet.first_address
        self._backups[wallet.first_address] = backup
        return backup

    def restore_from_backup(self, backup: dict, passphrase: str) -> Optional[str]:
        if backup.get("version") == 2:
            raw = decrypt_secret(backup, passphrase)
            return raw.decode("utf-8") if raw is not None else None
        # legacy version 1 (weak XOR format) - restore only, never create
        try:
            salt = bytes.fromhex(backup["salt"])
            enc = bytes.fromhex(backup["encrypted"])
            if kdf is None:
                return None
            key = kdf.pbkdf2(passphrase.encode(), salt, 2048, 32)
            return bytes(a ^ b for a, b in zip(enc, (key * (len(enc) // 32 + 1))[:len(enc)])).decode()
        except Exception:
            return None

    return create_encrypted_backup, restore_from_backup


# --------------------------------------------------------------------------- #
# 3. Real Shamir secret sharing
# --------------------------------------------------------------------------- #
_PRIME = 2 ** 521 - 1
_CHUNK = 32          # bytes of secret per polynomial
_YLEN = 66           # bytes needed for a value < 2**521


def _eval_poly(coeffs: List[int], x: int) -> int:
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % _PRIME
    return acc


def shamir_split(secret: bytes, t: int, n: int) -> Dict[int, bytes]:
    if not (1 <= t <= n <= 255):
        raise ValueError("need 1 <= t <= n <= 255")
    chunks = [secret[i:i + _CHUNK] for i in range(0, len(secret), _CHUNK)] or [b""]
    header = len(secret).to_bytes(4, "big") + bytes([t])
    shares = {x: bytearray(header) for x in range(1, n + 1)}
    for chunk in chunks:
        coeffs = [int.from_bytes(chunk.ljust(_CHUNK, b"\x00"), "big")]
        coeffs += [secrets.randbelow(_PRIME) for _ in range(t - 1)]
        for x in range(1, n + 1):
            shares[x] += _eval_poly(coeffs, x).to_bytes(_YLEN, "big")
    return {x: bytes(v) for x, v in shares.items()}


def shamir_recover(shares: Dict[int, bytes]) -> bytes:
    if not shares:
        raise ValueError("no shares")
    items = sorted(shares.items())
    first = items[0][1]
    length = int.from_bytes(first[:4], "big")
    t = first[4]
    if len(items) < t:
        raise ValueError(f"need at least {t} shares")
    for _, s in items:
        if s[:5] != first[:5] or (len(s) - 5) % _YLEN != 0 or len(s) != len(first):
            raise ValueError("inconsistent shares")
    items = items[:t]
    xs = [x for x, _ in items]
    if len(set(xs)) != len(xs):
        raise ValueError("duplicate share index")
    n_chunks = (len(first) - 5) // _YLEN
    out = bytearray()
    for c in range(n_chunks):
        ys = [int.from_bytes(s[5 + c * _YLEN: 5 + (c + 1) * _YLEN], "big") for _, s in items]
        secret_int = 0
        for j, xj in enumerate(xs):
            num, den = 1, 1
            for m, xm in enumerate(xs):
                if m != j:
                    num = (num * (-xm)) % _PRIME
                    den = (den * (xj - xm)) % _PRIME
            secret_int = (secret_int + ys[j] * num * pow(den, -1, _PRIME)) % _PRIME
        out += secret_int.to_bytes(_CHUNK, "big")
    return bytes(out[:length])


def _make_tss_methods():
    def generate_shares(self, secret: bytes) -> Dict[int, bytes]:
        shares = shamir_split(bytes(secret), self.t, self.n)
        self._shares = dict(shares)
        return shares

    def recover_secret(self, shares: Dict[int, bytes]) -> bytes:
        return shamir_recover(shares)

    return generate_shares, recover_secret


# --------------------------------------------------------------------------- #
# 4. Privacy (ring) transaction
# --------------------------------------------------------------------------- #
_RING_TX_CAP = 10_000
_KEY_IMAGE_SECRET = secrets.token_bytes(32)      # node-local, never leaves the process


def _make_ring_method(module: Any):
    import time
    sysrand = secrets.SystemRandom()

    def create_ring_tx(self, sender: str, recipient: str, amount: int, ring_size: int = 11) -> dict:
        if not isinstance(sender, str) or not sender or not isinstance(recipient, str) or not recipient:
            raise ValueError("sender and recipient must be non-empty strings")
        if not isinstance(amount, int) or isinstance(amount, bool) or not (0 < amount < 2 ** 63):
            raise ValueError("amount must be a positive integer")
        if not (2 <= ring_size <= 64):
            raise ValueError("ring_size must be between 2 and 64")
        pool = [a for a in list(self._bc.utxo._addr_idx.keys()) if a != sender]
        decoys = sysrand.sample(pool, min(ring_size - 1, len(pool)))
        ring = decoys + [sender]
        sysrand.shuffle(ring)
        blinding = secrets.randbelow(module.Secp256k1.ORDER)
        commitment = module.PedersenCommitment.commit(amount, blinding)
        key_image = hmac.new(_KEY_IMAGE_SECRET, sender.encode(), hashlib.sha256).hexdigest()
        tx_id = hashlib.sha256(secrets.token_bytes(16) + f"{sender}{recipient}{amount}{time.time()}".encode()).hexdigest()[:16]
        tx = {
            "tx_id": tx_id,
            "ring": ring,
            "ring_size": len(ring),
            "commitment": [format(int(c), "x") for c in commitment],
            "key_image": key_image,
            "recipient": hashlib.sha256(recipient.encode()).hexdigest()[:16],
            "amount": "hidden",
            "experimental": True,
            "anonymity": "NOT guaranteed - no real ring signature yet",
        }
        with self._lock:
            self._ring_txs.append(tx)
            if len(self._ring_txs) > _RING_TX_CAP:
                del self._ring_txs[: len(self._ring_txs) - _RING_TX_CAP]
        return tx

    return create_ring_tx


# --------------------------------------------------------------------------- #
# 5. Optimistic rollup fraud proofs
# --------------------------------------------------------------------------- #
def _make_fraud_method():
    def submit_fraud_proof(self, challenger: str, batch_id: int, proof: str) -> dict:
        if not isinstance(proof, str) or len(proof) < 32:
            return {"ok": False, "error": "Proof too short"}
        verifier = getattr(self, "fraud_verifier", None)
        if verifier is None:
            return {"ok": False, "error": "No fraud-proof verifier configured (fail closed)"}
        with self._lock:
            batch = next((b for b in self._batches if b["batch_id"] == batch_id), None)
            if not batch:
                return {"ok": False, "error": "Batch not found"}
            if self._bc.height > batch["challenge_until"]:
                return {"ok": False, "error": "Challenge period expired"}
            if any(c["batch_id"] == batch_id and c["challenger"] == challenger for c in self._challenges):
                return {"ok": False, "error": "Already challenged by this address"}
            try:
                valid = bool(verifier(batch, proof))
            except Exception:
                valid = False
            if not valid:
                return {"ok": False, "error": "Fraud proof rejected"}
            batch["challenged"] = True
            self._challenges.append({"challenger": challenger, "batch_id": batch_id,
                                     "proof": proof[:100], "block": self._bc.height,
                                     "resolved": False})
            return {"ok": True, "message": f"Fraud proof accepted for batch {batch_id}"}

    return submit_fraud_proof


# --------------------------------------------------------------------------- #
# Applying the patches
# --------------------------------------------------------------------------- #
_APPLIED: List[tuple] = []
_LOCK = threading.RLock()


def _targets(group_no: int, host: Any, cls_name: str):
    """Yield (module_name, class) for the group module and the host, if present."""
    try:
        mod = importlib.import_module(f"nebula_group{group_no}")
    except Exception:
        mod = None
    if mod is not None and hasattr(mod, cls_name):
        yield mod, getattr(mod, cls_name)
    if host is not None and hasattr(host, cls_name):
        yield host, getattr(host, cls_name)


def _patch(cls: Any, name: str, fn: Callable) -> None:
    _APPLIED.append((cls, name, cls.__dict__.get(name)))
    setattr(cls, name, fn)


def apply(host: Any = None) -> Dict[str, Any]:
    """Apply every fix. Idempotent. Returns {"patched": [...], "skipped": {...}}."""
    report: Dict[str, Any] = {"patched": [], "skipped": {}}
    with _LOCK:
        plan = [
            (48, "ScriptEngine"), (55, "WalletBackupManager"),
            (51, "ThresholdSignatureScheme"), (49, "PrivacyTransaction"),
            (58, "OptimisticRollup"),
        ]
        for group_no, cls_name in plan:
            found = False
            for owner, cls in _targets(group_no, host, cls_name):
                found = True
                if getattr(cls, "_nbl_hardened", False):
                    continue
                try:
                    if cls_name == "ScriptEngine":
                        _patch(cls, "execute", _make_execute(owner))
                        _patch(cls, "eval_p2pkh", _make_eval_p2pkh(owner))
                        if not hasattr(cls, "signature_verifier"):
                            cls.signature_verifier = None
                    elif cls_name == "WalletBackupManager":
                        c, r = _make_backup_methods(owner)
                        _patch(cls, "create_encrypted_backup", c)
                        _patch(cls, "restore_from_backup", r)
                    elif cls_name == "ThresholdSignatureScheme":
                        g, r = _make_tss_methods()
                        _patch(cls, "generate_shares", g)
                        _patch(cls, "recover_secret", r)
                    elif cls_name == "PrivacyTransaction":
                        _patch(cls, "create_ring_tx", _make_ring_method(owner))
                    elif cls_name == "OptimisticRollup":
                        _patch(cls, "submit_fraud_proof", _make_fraud_method())
                        if not hasattr(cls, "fraud_verifier"):
                            cls.fraud_verifier = None
                    cls._nbl_hardened = True
                    report["patched"].append(f"group{group_no}.{cls_name}")
                except Exception as exc:
                    report["skipped"][f"group{group_no}.{cls_name}"] = f"{type(exc).__name__}: {exc}"
            if not found:
                report["skipped"][f"group{group_no}.{cls_name}"] = "class not found"
    return report


def revert() -> int:
    """Undo every patch made by apply() (newest first). Returns number reverted."""
    count = 0
    with _LOCK:
        while _APPLIED:
            cls, name, original = _APPLIED.pop()
            if original is None:
                try:
                    delattr(cls, name)
                except AttributeError:
                    _NB_SWALLOW_LOG.debug("swallowed AttributeError in revert", exc_info=True)
            else:
                setattr(cls, name, original)
            if getattr(cls, "_nbl_hardened", False):
                try:
                    del cls._nbl_hardened
                except AttributeError:
                    _NB_SWALLOW_LOG.debug("swallowed AttributeError in revert", exc_info=True)
            count += 1
    return count
