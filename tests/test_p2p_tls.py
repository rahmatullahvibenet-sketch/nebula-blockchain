import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""NEBULA v10.19 - P2P TLS transport tests (module level, loopback sockets)."""
import os, sys, socket, ssl, tempfile, threading, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import nebula_p2p_secure as S

R = []
def chk(name, fn):
    try:
        r = fn(); R.append((name, 'PASS' if r is not False else 'FAIL', str(r)[:90]))
    except Exception as e:
        R.append((name, 'ERROR', f'{type(e).__name__}: {str(e)[:100]}'))

def server(sec, handler, n=1):
    """Listen on a free loopback port; run handler(conn) for n connections. Returns (port, thread, errors)."""
    ls = socket.socket(); ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ls.bind(('127.0.0.1', 0)); ls.listen(8); ls.settimeout(8)
    port = ls.getsockname()[1]; errs = []
    def run():
        for _ in range(n):
            try:
                c, _a = ls.accept()
                c = sec.wrap_inbound(c)
                if c is None: continue
                handler(c)
            except Exception as e:
                errs.append(type(e).__name__)
        ls.close()
    t = threading.Thread(target=run, daemon=True); t.start()
    return port, t, errs

def echo(c):
    c.settimeout(5)
    d = c.recv(64); c.sendall(b'echo:' + d); c.close()

def dial(sec, port, payload=b'hello', plain=False):
    s = socket.socket(); s.settimeout(5); s.connect(('127.0.0.1', port))
    if not plain: s = sec.wrap_outbound(s, '127.0.0.1', port)
    s.sendall(payload); out = s.recv(64); return s, out

d1, d2, d3 = tempfile.mkdtemp(), tempfile.mkdtemp(), tempfile.mkdtemp()
A = S.P2PTransportSecurity(d1, mode='required'); B = S.P2PTransportSecurity(d2, mode='required')

chk('certificate generated + node id', lambda: A.available and len(A.node_id) == 64)
chk('node id stable after reload', lambda: S.P2PTransportSecurity(d1, mode='required').node_id == A.node_id)
chk('private key file mode 0600', lambda: oct(os.stat(os.path.join(d1, 'node.key')).st_mode & 0o777) == '0o600')

port, t, errs = server(B, echo)
def rt():
    s, out = dial(A, port); v = s.version(); c = s.cipher()[0]; s.close(); t.join(5)
    return out == b'echo:hello' and v == 'TLSv1.3', (out, v, c)
chk('required<->required TLS 1.3 round trip', lambda: rt()[0])
chk('client pinned the server on first use', lambda: A.status()['pinned_peers'] == 1 and A.status()['stats']['pin_new'] == 1)

port2, t2, _ = server(B, echo, n=2)
def second():
    s, out = dial(A, port2); s.close(); return out == b'echo:hello'
chk('second connection to same peer accepted', second)

# pin mismatch: new identity listening on the SAME host:port string is simulated by swapping the pin
A._pins['127.0.0.1:%d' % port2] = 'ab' * 32
def mism():
    try: dial(A, port2); return False
    except S.PinMismatch: return True
chk('PIN MISMATCH refused (possible MITM)', mism)
chk('pin_mismatch counted', lambda: A.status()['stats']['pin_mismatch'] == 1)
chk('forget_peer clears the pin', lambda: A.forget_peer('127.0.0.1:%d' % port2) is True)
t2.join(8)

# required server vs plaintext client
port3, t3, _ = server(B, echo)
def plain_to_required():
    s = socket.socket(); s.settimeout(4); s.connect(('127.0.0.1', port3)); s.sendall(b'hi')
    try: d = s.recv(64)
    except Exception: d = b''
    s.close(); return d == b''
chk('required server rejects plaintext client', plain_to_required)
t3.join(8)
chk('rejected_in counted', lambda: B.status()['stats']['rejected_in'] >= 1)

# optional server accepts both
O = S.P2PTransportSecurity(d3, mode='optional')
port4, t4, _ = server(O, echo, n=2)
def opt_plain():
    s = socket.socket(); s.settimeout(6); s.connect(('127.0.0.1', port4)); s.sendall(b'hello'); out = s.recv(64); s.close(); return out == b'echo:hello'
def opt_tls():
    s, out = dial(A, port4); s.close(); return out == b'echo:hello'
chk('optional server accepts a plaintext peer', opt_plain)
chk('optional server accepts a TLS peer', opt_tls)
t4.join(8)
chk('plain_in and tls_in both counted', lambda: O.status()['stats']['plain_in'] == 1 and O.status()['stats']['tls_in'] == 1)

# optional client -> plaintext-only server falls back; required client refuses
OFF = S.P2PTransportSecurity(tempfile.mkdtemp(), mode='off')
port5, t5, _ = server(OFF, echo, n=2)
def opt_fallback():
    s, out = dial(O, port5); s.close(); return out == b'echo:hello'
chk('optional client falls back to plaintext server', opt_fallback)
def req_refuses():
    try: dial(A, port5); return False
    except (ssl.SSLError, OSError): return True
chk('required client refuses plaintext server', req_refuses)
t5.join(10)
chk('plain_fallback counted', lambda: O.status()['stats']['plain_fallback'] == 1)

# silent client must not hang the server thread forever (optional mode sniff timeout)
def silent():
    port6, t6, _ = server(O, lambda c: (c.settimeout(2), c.recv(8), c.close()), n=1)
    s = socket.socket(); s.connect(('127.0.0.1', port6)); t0 = time.time(); t6.join(10); s.close()
    return (not t6.is_alive()), round(time.time() - t0, 1)
chk('silent client does not hang the server', lambda: silent()[0])

# unavailable TLS + required = fail closed
BROKEN = S.P2PTransportSecurity(tempfile.mkdtemp(), mode='required'); BROKEN.available = False; BROKEN.error = 'simulated'
def fail_closed():
    a, b = socket.socketpair()
    try: BROKEN.wrap_outbound(a, 'x', 1); return False
    except S.TLSUnavailable: pass
    c, d = socket.socketpair()
    return BROKEN.wrap_inbound(c) is None
chk('required + TLS unavailable fails closed', fail_closed)
chk('mode off is a pass-through', lambda: (lambda a: OFF.wrap_inbound(a) is a and OFF.wrap_outbound(a, 'x', 1) is a)(socket.socket()))

# [v10.23] default mode is fail-closed
import os as _os
_os.environ.pop('NEBULA_P2P_TLS', None)
chk('default mode is required', lambda: S.P2PTransportSecurity(tempfile.mkdtemp()).mode == 'required')
_os.environ['NEBULA_P2P_TLS'] = 'garbage'
chk('invalid mode value fails closed to required', lambda: S.P2PTransportSecurity(tempfile.mkdtemp()).mode == 'required')
_os.environ.pop('NEBULA_P2P_TLS', None)

for n, r, d in R: print(f'{r:5} {n:52} {d}')
ok = sum(1 for _, r, _d in R if r == 'PASS'); print(f'{ok}/{len(R)}')
sys.exit(0 if ok == len(R) else 1)

