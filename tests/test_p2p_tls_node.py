import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""NEBULA v10.19 - two real P2PNode instances talking over TLS 1.3 (loopback)."""
import os, sys, io, time, socket, tempfile, contextlib, importlib.util
os.environ['NEBULA_ALLOW_DEV_MODE'] = '1'; os.environ['NEBULA_DISABLE_CHAIN'] = '1'
os.environ['NEBULA_P2P_TLS'] = 'required'; os.environ['NEBULA_P2P_TLS_DIR'] = tempfile.mkdtemp()
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, root)
spec = importlib.util.spec_from_file_location('nb', os.path.join(root, 'nebula_v10_24.py'))
m = importlib.util.module_from_spec(spec); sys.modules['nb'] = m
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    spec.loader.exec_module(m)
import nebula_p2p_secure as S
R = []
def chk(n, fn):
    try:
        r = fn(); R.append((n, 'PASS' if r is not False else 'FAIL', str(r)[:90]))
    except Exception as e: R.append((n, 'ERROR', f'{type(e).__name__}: {str(e)[:100]}'))
def free():
    s = socket.socket(); s.bind(('127.0.0.1', 0)); p = s.getsockname()[1]; s.close(); return p
def wait(cond, t=12):
    t0 = time.time()
    while time.time() - t0 < t:
        if cond(): return True
        time.sleep(0.2)
    return False
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    bcA = m.NEBULABlockchain(); bcA._dev_mode = True
    bcB = m.NEBULABlockchain(); bcB._dev_mode = True
    pa = free(); A = m.P2PNode(bcA, host='127.0.0.1', port=pa, data_dir=tempfile.mkdtemp())
    pb = free(); B = m.P2PNode(bcB, host='127.0.0.1', port=pb, data_dir=tempfile.mkdtemp())
    A.start(); B.start(); time.sleep(1.0)
    ok = B.connect_peer('127.0.0.1', pa)
chk('node B dials node A (mode=required)', lambda: ok)
chk('node A has the inbound peer', lambda: wait(lambda: len(A._peers) == 1))
chk('node B has the outbound peer', lambda: wait(lambda: len(B._peers) == 1))
def got_version():
    return wait(lambda: any(getattr(p.info, 'version', 0) for p in list(A._peers.values())) and any(getattr(p.info, 'version', 0) for p in list(B._peers.values())))
chk('version handshake completed over TLS both ways', got_version)
def socks():
    pb_ = list(B._peers.values())[0]; pa_ = list(A._peers.values())[0]
    out_tls = pb_._sock.version(); inb = pa_._sock._active.version()
    return out_tls == 'TLSv1.3' and inb == 'TLSv1.3', (out_tls, inb)
chk('both sockets negotiated TLS 1.3', lambda: socks()[0])
st = S.get_security().status()
chk('stats: tls_in>=1 tls_out>=1 plain=0', lambda: st['stats']['tls_in'] >= 1 and st['stats']['tls_out'] >= 1 and st['stats']['plain_in'] == 0 and st['stats']['plain_out'] == 0)
chk('node key stored in the TLS dir', lambda: os.path.exists(os.path.join(st['dir'], 'node.key')))
def plain_refused():
    s = socket.socket(); s.settimeout(5); s.connect(('127.0.0.1', pa)); s.sendall(b'\x00' * 24)
    try: d = s.recv(64)
    except Exception: d = b''
    s.close(); return d == b''
chk('old plaintext peer is refused in required mode', plain_refused)
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    for n in (A, B):
        try: n.stop()
        except Exception: pass
for n, r, d in R: print(f'{r:5} {n:52} {d}')
ok_ = sum(1 for _, r, _d in R if r == 'PASS'); print(f'{ok_}/{len(R)}'); sys.exit(0 if ok_ == len(R) else 1)
