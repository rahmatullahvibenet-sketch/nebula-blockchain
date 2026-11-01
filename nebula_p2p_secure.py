"""
nebula_p2p_secure.py - TLS 1.3 transport security for the NEBULA P2P layer (v10.19)
===================================================================================

What it gives you
-----------------
* Encryption + integrity of every P2P byte (TLS 1.3 only, ECDSA P-256 node certificate).
* Trust-on-first-use pinning of the peers you DIAL: the first time you connect to host:port the
  certificate fingerprint is stored in <dir>/known_peers.json; a different certificate later is a
  possible man-in-the-middle and the connection is refused (PinMismatch).
* A stable node id (sha256 of the node certificate).

What it does NOT give you (be honest with yourself before launch)
-----------------------------------------------------------------
* Inbound peers are anonymous (as in Bitcoin) - no client certificates, no reputation, no Sybil defence.
* TOFU cannot protect the very first connection to a peer.
* mode "optional" accepts / falls back to plaintext, so an active attacker can strip TLS.
  For mainnet set  NEBULA_P2P_TLS=required .

Configuration (environment)
---------------------------
NEBULA_P2P_TLS      off | optional | required      (default: required since v10.23; use optional for old plaintext nodes)
NEBULA_P2P_TLS_PIN  tofu | off                      (default: tofu)
NEBULA_P2P_TLS_DIR  directory for node.key / node.crt / known_peers.json
                    (default: ./nebula_data/p2p_tls)

The module never raises on import and never touches consensus code. The host calls only
get_security().wrap_inbound(conn) and get_security().wrap_outbound(sock, host, port).
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import socket
import ssl
import subprocess
import threading
import time
from typing import Any, Dict, Optional

log = logging.getLogger("nebula.p2p_tls")

MODES = ("off", "optional", "required")
HANDSHAKE_TIMEOUT = 10.0     # seconds for a TLS handshake
SNIFF_TIMEOUT = 3.0          # seconds to wait for a peer's first byte in "optional" mode
TLS_RECORD_HANDSHAKE = 0x16  # first byte of every TLS ClientHello


class TLSUnavailable(OSError):
    """TLS is required but cannot be provided (no certificate / ssl problem)."""


class PinMismatch(ssl.SSLError):
    """The peer presented a different certificate than the one pinned for host:port."""


# --------------------------------------------------------------------------- certificate creation
def _gen_cert_cryptography(key_path: str, crt_path: str, days: int = 3650) -> None:
    import datetime
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.x509.oid import NameOID

    key = ec.generate_private_key(ec.SECP256R1())
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "nebula-node")])
    now = datetime.datetime.now(datetime.timezone.utc)
    cert = (x509.CertificateBuilder()
            .subject_name(name).issuer_name(name)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now - datetime.timedelta(days=1))
            .not_valid_after(now + datetime.timedelta(days=days))
            .sign(key, hashes.SHA256()))
    with open(key_path, "wb") as f:
        f.write(key.private_bytes(serialization.Encoding.PEM,
                                  serialization.PrivateFormat.PKCS8,
                                  serialization.NoEncryption()))
    with open(crt_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))


def _gen_cert_openssl(key_path: str, crt_path: str, days: int = 3650) -> None:
    subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "ec", "-pkeyopt", "ec_paramgen_curve:prime256v1",
         "-nodes", "-keyout", key_path, "-out", crt_path, "-days", str(days), "-subj", "/CN=nebula-node"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)


def _fingerprint(der: bytes) -> str:
    return hashlib.sha256(der).hexdigest()


# --------------------------------------------------------------------------- lazy server-side socket
class _LazyServerSocket:
    """Server-side socket proxy: the TLS handshake (or plaintext sniffing) is done on the FIRST I/O call,
    in the peer's own thread, so a slow or silent client can never stall the accept loop."""

    _IO = frozenset(("recv", "recv_into", "send", "sendall", "makefile", "read", "write"))

    def __init__(self, sec: "P2PTransportSecurity", raw: socket.socket):
        self._sec = sec
        self._raw = raw
        self._active: Optional[socket.socket] = None
        self._timeout = raw.gettimeout()
        self._failed: Optional[BaseException] = None
        self._lock = threading.RLock()

    def _ensure(self) -> socket.socket:
        with self._lock:
            if self._active is not None:
                return self._active
            if self._failed is not None:
                raise self._failed
            sec, raw = self._sec, self._raw
            try:
                if sec.mode == "optional":
                    raw.settimeout(SNIFF_TIMEOUT)
                    try:
                        first = raw.recv(1, socket.MSG_PEEK)
                    except socket.timeout:
                        first = None                      # TLS clients always speak first -> plaintext peer
                    if first is None or (first and first[0] != TLS_RECORD_HANDSHAKE):
                        sec._count("plain_in")
                        raw.settimeout(self._timeout)
                        self._active = raw
                        return raw
                    if first == b"":                      # closed before sending anything
                        raw.settimeout(self._timeout)
                        self._active = raw
                        return raw
                raw.settimeout(HANDSHAKE_TIMEOUT)
                tls = sec._srv_ctx.wrap_socket(raw, server_side=True)
                tls.settimeout(self._timeout)
                sec._count("tls_in")
                self._active = tls
                return tls
            except BaseException as exc:
                sec._count("rejected_in")
                self._failed = exc
                try:
                    raw.close()
                except Exception:
                    pass
                raise

    # explicit fast paths
    def settimeout(self, t):
        with self._lock:
            self._timeout = t
            (self._active or self._raw).settimeout(t)

    def gettimeout(self):
        return self._timeout

    def close(self):
        with self._lock:
            target = self._active or self._raw
        try:
            target.close()
        except Exception:
            pass

    def __getattr__(self, name):
        if name in self._IO:
            return getattr(self._ensure(), name)
        return getattr(self._active or self._raw, name)


# --------------------------------------------------------------------------- the security object
class P2PTransportSecurity:
    def __init__(self, directory: Optional[str] = None, mode: Optional[str] = None, pin: Optional[str] = None):
        mode = (mode or os.environ.get("NEBULA_P2P_TLS", "required")).strip().lower()
        if mode not in MODES:
            log.warning("NEBULA_P2P_TLS=%r is not one of %s - using 'required' (fail closed)", mode, MODES)
            mode = "required"
        self.mode = mode
        self.pin = (pin or os.environ.get("NEBULA_P2P_TLS_PIN", "tofu")).strip().lower()
        self.dir = os.path.abspath(directory or os.environ.get("NEBULA_P2P_TLS_DIR")
                                   or os.path.join(os.getcwd(), "nebula_data", "p2p_tls"))
        self.available = False
        self.error: Optional[str] = None
        self.node_id: Optional[str] = None
        self._srv_ctx: Optional[ssl.SSLContext] = None
        self._cli_ctx: Optional[ssl.SSLContext] = None
        self._lock = threading.RLock()
        self._pins: Dict[str, str] = {}
        self._stats: Dict[str, int] = {k: 0 for k in (
            "tls_in", "tls_out", "plain_in", "plain_out", "plain_fallback",
            "rejected_in", "pin_new", "pin_mismatch", "failed_out")}
        if self.mode != "off":
            self._init_tls()

    # ----- setup
    def _init_tls(self) -> None:
        try:
            os.makedirs(self.dir, mode=0o700, exist_ok=True)
            key_path = os.path.join(self.dir, "node.key")
            crt_path = os.path.join(self.dir, "node.crt")
            if not (os.path.exists(key_path) and os.path.exists(crt_path)):
                try:
                    _gen_cert_cryptography(key_path, crt_path)
                except Exception as exc:
                    log.info("cryptography cert generation unavailable (%s) - trying openssl CLI", exc)
                    _gen_cert_openssl(key_path, crt_path)
            try:
                os.chmod(key_path, 0o600)
            except OSError:
                pass
            srv = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            srv.minimum_version = ssl.TLSVersion.TLSv1_3
            srv.load_cert_chain(crt_path, key_path)
            cli = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            cli.minimum_version = ssl.TLSVersion.TLSv1_3
            cli.check_hostname = False
            cli.verify_mode = ssl.CERT_NONE            # identity is checked by fingerprint pinning
            with open(crt_path, "r", encoding="ascii") as f:
                self.node_id = _fingerprint(ssl.PEM_cert_to_DER_cert(f.read()))
            self._srv_ctx, self._cli_ctx = srv, cli
            self._load_pins()
            self.available = True
            log.info("P2P TLS ready (mode=%s, pin=%s, node_id=%s...)", self.mode, self.pin, self.node_id[:16])
        except Exception as exc:
            self.error = "%s: %s" % (type(exc).__name__, exc)
            log.error("P2P TLS could not be initialised: %s", self.error)

    def _pins_path(self) -> str:
        return os.path.join(self.dir, "known_peers.json")

    def _load_pins(self) -> None:
        try:
            with open(self._pins_path(), "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                self._pins = {str(k): str(v) for k, v in data.items()}
        except FileNotFoundError:
            self._pins = {}
        except Exception:
            log.error("known_peers.json unreadable - starting with no pins", exc_info=True)
            self._pins = {}

    def _save_pins(self) -> None:
        tmp = self._pins_path() + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(self._pins, f, indent=1, sort_keys=True)
        os.replace(tmp, self._pins_path())

    def _count(self, key: str) -> None:
        with self._lock:
            self._stats[key] = self._stats.get(key, 0) + 1

    # ----- public API
    def wrap_inbound(self, conn: socket.socket):
        """Return a socket to use for an accepted connection, or None to refuse it."""
        if self.mode == "off":
            return conn
        if not self.available:
            if self.mode == "required":
                self._count("rejected_in")
                _safe_close(conn)
                return None
            self._count("plain_in")
            return conn
        return _LazyServerSocket(self, conn)

    def wrap_outbound(self, sock: socket.socket, host: str, port: int):
        """Return a connected socket (TLS if possible). Raises OSError when the connection must not be used."""
        if self.mode == "off":
            return sock
        if not self.available:
            if self.mode == "required":
                _safe_close(sock)
                raise TLSUnavailable("TLS required but unavailable: %s" % self.error)
            self._count("plain_out")
            return sock
        timeout = sock.gettimeout()
        try:
            tls = self._cli_ctx.wrap_socket(sock, server_hostname=None)
            der = tls.getpeercert(binary_form=True)
            if not der:
                raise ssl.SSLError("peer sent no certificate")
            self._check_pin("%s:%s" % (host, port), _fingerprint(der), tls)
            self._count("tls_out")
            return tls
        except PinMismatch:
            raise
        except (ssl.SSLError, OSError, socket.timeout) as exc:
            _safe_close(sock)
            if self.mode == "required":
                self._count("failed_out")
                raise
            log.warning("TLS to %s:%s failed (%s) - falling back to plaintext (mode=optional)", host, port, exc)
            plain = socket.create_connection((host, port), timeout=timeout or HANDSHAKE_TIMEOUT)
            plain.settimeout(timeout)
            self._count("plain_out")
            self._count("plain_fallback")
            return plain

    def _check_pin(self, addr: str, fp: str, tls: ssl.SSLSocket) -> None:
        if self.pin != "tofu":
            return
        with self._lock:
            known = self._pins.get(addr)
            if known is None:
                self._pins[addr] = fp
                self._count("pin_new")
                try:
                    self._save_pins()
                except Exception:
                    log.error("could not save known_peers.json", exc_info=True)
                log.info("pinned %s -> %s...", addr, fp[:16])
                return
            if known != fp:
                self._count("pin_mismatch")
                _safe_close(tls)
                log.error("CERTIFICATE CHANGED for %s (pinned %s..., got %s...) - possible MITM, refusing",
                          addr, known[:16], fp[:16])
                raise PinMismatch("certificate for %s does not match the pinned one" % addr)

    def forget_peer(self, addr: str) -> bool:
        """Operator action: drop the pin for host:port (after a legitimate re-key)."""
        with self._lock:
            had = self._pins.pop(addr, None) is not None
            if had:
                self._save_pins()
            return had

    def status(self) -> Dict[str, Any]:
        with self._lock:
            return {"mode": self.mode, "pin": self.pin, "available": self.available, "error": self.error,
                    "node_id": self.node_id, "pinned_peers": len(self._pins), "dir": self.dir,
                    "stats": dict(self._stats)}


def _safe_close(s) -> None:
    try:
        s.close()
    except Exception:
        pass


# --------------------------------------------------------------------------- process-wide instance
_INSTANCE: Optional[P2PTransportSecurity] = None
_INSTANCE_LOCK = threading.Lock()


def get_security() -> P2PTransportSecurity:
    global _INSTANCE
    with _INSTANCE_LOCK:
        if _INSTANCE is None:
            _INSTANCE = P2PTransportSecurity()
        return _INSTANCE


def set_security(sec: Optional[P2PTransportSecurity]) -> None:
    """Replace (or clear) the process-wide instance - used by tests and by operators who want a custom dir."""
    global _INSTANCE
    with _INSTANCE_LOCK:
        _INSTANCE = sec


def configure(directory: str) -> None:
    """Choose the key/pin directory once, before the first connection. An explicit NEBULA_P2P_TLS_DIR
    environment variable wins; an instance that already exists is never replaced."""
    global _INSTANCE
    with _INSTANCE_LOCK:
        if _INSTANCE is None and not os.environ.get("NEBULA_P2P_TLS_DIR"):
            _INSTANCE = P2PTransportSecurity(directory)
