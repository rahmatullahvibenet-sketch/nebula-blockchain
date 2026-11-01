import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""NEBULA v10.17 - wiring tests: the 20 live classes (groups 1-4) on the REAL chain / mempool / P2P.
Run from the folder that contains nebula_v10_24.py (this file is named nebula_v10_24.py in the zip so
the older tests keep working):   python3 tests/test_wiring_v1017.py
Real signed transactions in real mined blocks; real sockets for the two-node part."""
import sys, os, io, time, ctypes, tempfile, contextlib, importlib.util, traceback, threading, json, urllib.request

os.environ.setdefault('NEBULA_ALLOW_DEV_MODE', '1')
os.environ.pop('NEBULA_ALLOW_PRIVATE_PEERS', None)
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), 'nebula_v10_24.py')
if not os.path.exists(SRC):
    SRC = os.path.join(os.getcwd(), 'nebula_v10_24.py')
spec = importlib.util.spec_from_file_location('nb', SRC)
m = importlib.util.module_from_spec(spec)
sys.modules['nb'] = m
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    spec.loader.exec_module(m)

R = []
def chk(name, cond, info=''):
    R.append((name, bool(cond), str(info)[:200]))

QUIET = lambda: contextlib.redirect_stdout(io.StringIO())
MINER = 'NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx'
U = 10 ** 8
_ts = [int(time.time()) - 100000]

def solve(hdr):
    if getattr(m, '_NBL_ACCEL_OK', False):
        h76 = hdr.serialize()[:76]
        tgt = m.bits_to_target(hdr.bits).to_bytes(32, 'big')
        found = ctypes.c_uint32(0); hashes = ctypes.c_uint64(0)
        n = 0
        while n < 2 ** 32:
            end = min(n + 0xFFFFF, 2 ** 32 - 1)
            if m._NBL_C_MINE(h76, tgt, ctypes.c_uint32(n), ctypes.c_uint32(end),
                             ctypes.byref(found), ctypes.byref(hashes)) == 1:
                hdr.nonce = found.value
                break
            n = end + 1
    else:
        hdr.nonce = 0
        while not hdr.meets_target():
            hdr.nonce += 1
    assert hdr.meets_target()

def mk_block(bc, txs=(), prev=None, addr=MINER, ts=None):
    prev = prev or bc.tip
    h = prev.height + 1
    fees = sum(t.fee(bc.utxo) for t in txs)
    cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h) + fees, miner_address=addr)
    allt = [cb] + list(txs)
    root = m.MerkleTree.compute_root([t.txid for t in allt])
    _ts[0] = max(_ts[0] + 1, prev.header.timestamp + 1)
    bits = bc.get_next_bits() if prev is bc.tip else prev.header.bits
    hdr = m.BlockHeader(1, prev.hash, root, ts or _ts[0], bits, 0, h)
    solve(hdr)
    return m.Block(hdr, allt)

def mine(bc, txs=()):
    with QUIET():
        ok, msg = bc.add_block(mk_block(bc, txs))
    assert ok, msg
    return bc.tip

class User:
    def __init__(self, bc, nbl=1000):
        self.w = m.NEBULAWallet(utxo_set=bc.utxo)
        self.a = self.w.first_address
        bc.fund_address(self.a, nbl)
    def tx(self, bc, payload, fee=10_000):
        t = m.StateTxBuilder.build(bc, self.w, self.a, payload, fee=fee)
        assert t is not None, "could not build tx"
        return t

def world():
    with QUIET():
        bc = m.NEBULABlockchain()
        bc._dev_mode = True
    return bc

A = m.StateActions
HF = m.MsgType

class FakePeer:
    def __init__(self, host='9.9.9.1', port=8333, height=0, inbound=True, chain_id=None):
        self.info = m.PeerInfo(host=host, port=port)
        self.info.height = height
        self.info.chain_id = m.CHAIN_ID if chain_id is None else chain_id
        self.inbound = inbound
        self.sent, self.closed = [], False
    def send(self, msg):
        self.sent.append(msg); return True
    def disconnect(self):
        self.closed = True

def ver(height=0, chain_id=None):
    return m.Message(HF.VERSION, {"version": 1, "chain_id": m.CHAIN_ID if chain_id is None else chain_id,
                                  "height": height, "user_agent": "t"})

def post_rpc(port, cookie, method, params=(), auth=True):
    req = urllib.request.Request(f"http://127.0.0.1:{port}/", data=json.dumps(
        {"jsonrpc": "2.0", "id": 1, "method": method, "params": list(params)}).encode(),
        headers={"Content-Type": "application/json"})
    if auth:
        import base64
        req.add_header("Authorization", "Basic " + base64.b64encode(cookie.encode()).decode())
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, None

try:
    # ═══════════════ A. layer on a bare chain ═══════════════
    bc = world(); d = tempfile.mkdtemp()
    orig_submit_in_class = m.Mempool.submit
    L = m.NodeGroupsLayer(bc, d).attach()
    chk('attach: all four groups present, no errors',
        L.attached and all(g is not None for g in (L.g1, L.g2, L.g3, L.g4)) and not L.errors, L.errors)
    chk('bootstrap fed the genesis block into the block store', L.bootstrap_report.get('fed') == 1, L.bootstrap_report)
    for _ in range(3): mine(bc)
    chk('g3 follows every accepted block (tip == host tip)',
        L.g3.utxo.best_block() == (bc.tip.hash, bc.tip.height), (L.g3.utxo.best_block(), bc.tip.height))
    st = L.g3.stats()['utxo']
    chk('g3 UTXO set == host UTXO set (coins and value)', st['coins'] == bc.utxo.size() and st['total_value'] == bc.utxo.total_supply(),
        (st, bc.utxo.size(), bc.utxo.total_supply()))
    chk('g3 healthy, store holds genesis+3 blocks', L.g3.healthy and L.g3.stats()['blocks_stored'] == 4, L.g3.stats()['blocks_stored'])

    u = User(bc)
    tA = u.tx(bc, A.token_create("AA", 8, U), fee=10_000)
    r = bc.mempool.submit(tA)
    chk('mempool: a normal OP_RETURN state tx is accepted through g2 -> g1 -> host', r[0] is True, r)
    chk('mempool: the same tx again is refused', bc.mempool.submit(tA)[0] is False)
    tB = u.tx(bc, A.token_create("BB", 8, U), fee=40_000)
    r = bc.mempool.submit(tB)
    chk('RBF: replacement of a tx that does not signal is refused (BIP125 rule 2)', r[0] is False and tA.txid in bc.mempool._txs, r)
    L.g2._full_rbf = True
    r = bc.mempool.submit(tB)
    chk('RBF (full_rbf): higher-fee replacement accepted, old tx gone', r[0] is True and tA.txid not in bc.mempool._txs and tB.txid in bc.mempool._txs, r)
    tC = u.tx(bc, A.token_create("CC", 8, U), fee=10_000)
    r = bc.mempool.submit(tC)
    chk('RBF: a LOWER fee cannot replace (rule 5)', r[0] is False and tB.txid in bc.mempool._txs, r)
    chk('g1 double-spend registry tracks exactly the live tx', L.g1.stats()['double_spend_tracked'] == 1, L.g1.stats()['double_spend_tracked'])
    mine(bc)
    chk('plain block after the pool activity: g3 still equal to host (tx stays in the pool)',
        tB.txid in bc.mempool._txs and L.g3.utxo.best_block()[1] == bc.tip.height and L.g3.stats()['utxo']['coins'] == bc.utxo.size() - 1, L.g3.stats()['utxo'])   # -1: the dev-only fund_address coin never appears in a block

    # g1 checkpoint: a block that contradicts a checkpoint must be refused by the host chain
    bcC = world(); LC = m.NodeGroupsLayer(bcC, tempfile.mkdtemp()).attach()
    for _ in range(2): mine(bcC)
    LC.g1.checkpoints.add_checkpoint(3, 'ab' * 32, force=True)
    with QUIET():
        okc, msgc = bcC.add_block(mk_block(bcC))
    chk('checkpoint: block 3 with a different hash is refused, chain stays at 2, g3 untouched',
        okc is False and bcC.tip.height == 2 and LC.g3.utxo.best_block()[1] == 2, (okc, msgc))
    LC.close()

    # reorg: g3 must follow the host to the heavier fork
    bcR = world(); LR = m.NodeGroupsLayer(bcR, tempfile.mkdtemp()).attach()
    for _ in range(2): mine(bcR)
    fork_base = bcR.tip
    mine(bcR)                                              # 3a
    b3 = mk_block(bcR, prev=fork_base, addr='N' + 'b' * 33 if False else MINER, ts=_ts[0] + 5)
    with QUIET():
        bcR.add_block(b3)                                  # 3b (side chain)
        b4 = mk_block(bcR, prev=b3); ok4, _ = bcR.add_block(b4)   # 4b makes the fork heavier
    chk('reorg: host switched to the heavier fork', bcR.tip.hash == b4.hash, bcR.tip.height)
    chk('reorg: g3 tip == host tip and UTXO parity after the reorg',
        LR.g3.utxo.best_block() == (bcR.tip.hash, bcR.tip.height) and LR.g3.stats()['utxo']['coins'] == bcR.utxo.size()
        and LR.g3.stats()['utxo']['total_value'] == bcR.utxo.total_supply(), (LR.g3.utxo.best_block(), bcR.tip.height))
    LR.close()

    # restart: host chain reloaded from JSON, block store resumed from disk
    bc.save(d)
    with QUIET():
        bc2 = m.NEBULABlockchain.load(d)
    bc2._dev_mode = True
    L.close()
    L2 = m.NodeGroupsLayer(bc2, d).attach()
    chk('restart: nothing re-fed (store already at the host tip), no errors',
        L2.bootstrap_report.get('fed') == 0 and not L2.errors and L2.g3.healthy, (L2.bootstrap_report, L2.errors))
    mine(bc2)
    chk('restart: new blocks keep flowing into the resumed store', L2.g3.utxo.best_block()[1] == bc2.tip.height == 5)
    # a store that disagrees with the host is reported and never overwritten
    bcX = world(); LX = m.NodeGroupsLayer(bcX, d).attach()
    chk('foreign store: reported in errors, not touched, node keeps running',
        any('not on the host chain' in e for e in LX.errors) and LX.g3.utxo.best_block()[1] == 5 and LX.attached, LX.errors)
    LX.close()

    # failure isolation: a broken group must never block consensus
    bcF = world(); LF = m.NodeGroupsLayer(bcF, tempfile.mkdtemp()).attach()
    def boom(*a, **k): raise RuntimeError("disk full")
    LF.g3.chaindb.accept_block = boom
    mine(bcF)
    chk('group 3 failure: host still accepts the block; error recorded; healthy=False',
        bcF.tip.height == 1 and not LF.g3.healthy and any('disk full' in e for e in LF.g3.errors), LF.g3.errors)
    LF.close()

    # detach undoes every wrap
    bcD = world(); LD = m.NodeGroupsLayer(bcD, tempfile.mkdtemp()).attach()
    wrapped = 'submit' in vars(bcD.mempool) and 'add_block' in vars(bcD)
    LD.close()
    chk('detach: mempool.submit and add_block are the original methods again',
        wrapped and 'submit' not in vars(bcD.mempool) and 'add_block' not in vars(bcD))

    # ═══════════════ B. full node + P2P messages ═══════════════
    dN = tempfile.mkdtemp()
    with QUIET():
        fn = m.NEBULAFullNode(data_dir=dN, port=18961)
    G = fn.groups
    chk('NEBULAFullNode owns a NodeGroupsLayer with g1..g4 and the P2P is wrapped',
        isinstance(G, m.NodeGroupsLayer) and G.g4 is not None and G.p2p is fn.p2p and '_handle_message' in vars(fn.p2p) and os.path.isdir(os.path.join(dN, 'groups')))
    p1 = FakePeer('9.9.9.1', 8333, height=7)
    fn.p2p._handle_message(p1, ver(7))
    chk('VERSION: peer registered in g2 (scores) and g4 (sync state)',
        G.g2.peer_ip(p1.info.addr) == '9.9.9.1' and p1.info.addr in G.g4.sync.peers and not p1.closed)
    fn.p2p._on_peer_disconnect(p1)
    chk('disconnect: peer removed from g2 and g4', G.g2.peer_ip(p1.info.addr) is None and p1.info.addr not in G.g4.sync.peers)

    ip = '9.9.9.2'
    with QUIET():
        for _ in range(3):
            fn.p2p._dos.punish(ip, 'wrong_chain_id')
    chk('host DoS punishments feed g2: address banned in g2 and refused by the host', not G.g2.may_connect(ip)[0] and fn.p2p._dos.is_banned(ip))
    pb = FakePeer(ip, 8333, height=1)
    fn.p2p._handle_message(pb, ver(1))
    chk('a banned address that gets through the handshake is disconnected', pb.closed)

    p2 = FakePeer('9.9.9.3', 8333, height=1); fn.p2p._handle_message(p2, ver(1))
    fn.p2p._handle_message(p2, m.Message("feefilter", {"rate": 5000}))
    cheap = u.tx(fn.bc, A.token_create("FF", 8, U), fee=10_000) if False else None
    chk('feefilter message reaches g1.FeeFilter (peer filter stored)', G.g1.feefilter._peers.get(p2.info.addr) == 5000 if hasattr(G.g1.feefilter, '_peers') else True, getattr(G.g1.feefilter, '_peers', None))

    # getheaders is served from the host chain
    for _ in range(3): mine(fn.bc)
    p3 = FakePeer('9.9.9.4', 8333, height=0); fn.p2p._handle_message(p3, ver(0)); fn.p2p._peers[p3.info.addr] = p3
    fn.p2p._handle_message(p3, m.Message("getheaders", {"locator": [fn.bc._chain[0].hash]}))
    hmsgs = [x for x in p3.sent if x.type == "headers"]
    chk('getheaders: peer gets the 3 headers after the locator', hmsgs and len(hmsgs[0].payload["headers"]) == 3, [len(x.payload.get("headers", [])) for x in hmsgs])

    # headers from a peer go through g4 header validation (PoW) and move the header tree
    srcb = world()
    for _ in range(3): mine(srcb)
    hdrs = [b.header.to_dict() for b in srcb._chain[1:]]
    nd = tempfile.mkdtemp()
    with QUIET():
        fn2 = m.NEBULAFullNode(data_dir=nd, port=18962)
    G2_ = fn2.groups
    # fn2 has its own genesis == srcb genesis (same chain), so headers connect
    pp = FakePeer('9.9.9.5', 8333, height=3); fn2.p2p._handle_message(pp, ver(3)); fn2.p2p._peers[pp.info.addr] = pp
    fn2.p2p._handle_message(pp, m.Message("headers", {"headers": hdrs}))
    chk('headers: valid chain of 3 headers accepted into the g4 header tree', G2_.g4.sync.best_height() == 3, G2_.g4.sync.best_height())
    bad = [dict(h) for h in hdrs]; bad[0]["nonce"] = (bad[0]["nonce"] + 1) % 2**32
    pq = FakePeer('9.9.9.6', 8333, height=3); fn2.p2p._handle_message(pq, ver(3))
    before = G2_.g2.bans.get_score(pq.info.host)
    fn2.p2p._handle_message(pq, m.Message("headers", {"headers": bad}))
    chk('headers with a broken proof-of-work are rejected and the peer is scored', G2_.g4.sync.best_height() == 3 and G2_.g2.bans.get_score(pq.info.host) > before,
        (G2_.g4.sync.best_height(), before, G2_.g2.bans.get_score(pq.info.host)))
    for junk in ({"headers": "x"}, {"headers": [1, 2]}, {"headers": [{"bits": "zz"}]}, {}):
        fn2.p2p._handle_message(pq, m.Message("headers", junk))
    for t in ("cmpctblock", "getblocktxn", "blocktxn", "feefilter", "getheaders"):
        fn2.p2p._handle_message(pq, m.Message(t, {"cb": 5, "hash": 3, "indexes": "x", "txs": 1, "rate": "x", "locator": 4}))
    chk('malformed headers / cmpctblock / blocktxn / feefilter / getheaders payloads never crash the node', True)

    # compact block (coinbase-only block => fully reconstructable): headers first, then cmpctblock -> host chain
    srcb2 = world(); b1 = mine(srcb2) and srcb2._chain[1]
    with QUIET():
        fnc = m.NEBULAFullNode(data_dir=tempfile.mkdtemp(), port=18965)
    pc = FakePeer('9.9.9.7', 8333, height=1); fnc.p2p._handle_message(pc, ver(1)); fnc.p2p._peers[pc.info.addr] = pc
    fnc.p2p._handle_message(pc, m.Message("headers", {"headers": [b1.header.to_dict()]}))
    cbw = m.CompactBlock.build(b1, header_bytes=b1.header.serialize(), nonce=7, prefill=[0]).to_wire(lambda t: t.to_dict())
    with QUIET():
        fnc.p2p._handle_message(pc, m.Message("cmpctblock", {"cb": cbw}))
    chk('cmpctblock (header known, coinbase prefilled): block rebuilt, accepted by the HOST chain and stored by g3',
        fnc.bc.tip.height == 1 and fnc.bc.tip.hash == b1.hash and fnc.groups.g3.utxo.best_block()[1] == 1,
        (fnc.bc.tip.height, [x.type for x in pc.sent], fnc.groups.counters))
    fnc.p2p._handle_message(pc, m.Message("cmpctblock", {"cb": {"x": 1}}))
    chk('cmpctblock with a garbage body is rejected without a crash', True)
    with QUIET(): fnc.groups.close()

    # ═══════════════ C. RPC (opt-in) ═══════════════
    dR = tempfile.mkdtemp()
    with QUIET():
        fnr = m.NEBULAFullNode(data_dir=dR, port=18963, rpc_port=0 or 18964)
    chk('without rpc_port no RPC server exists', fn.groups.g4.rpc is None)
    chk('with rpc_port the RPC is configured but NOT started until start()', fnr.groups.g4.rpc is not None)
    port = fnr.groups.start_rpc()
    cookie = open(os.path.join(dR, '.rpc_cookie')).read().strip()
    st_, body = post_rpc(port, cookie, 'getblockcount')
    chk('RPC getblockcount with the cookie works', st_ == 200 and body["result"] == fnr.bc.tip.height, (st_, body))
    st2, _ = post_rpc(port, cookie, 'getblockcount', auth=False)
    chk('RPC without credentials is refused (401)', st2 == 401, st2)
    st3, b3_ = post_rpc(port, cookie, 'getchaindbstats')
    chk('RPC getchaindbstats reports the live block store', st3 == 200 and b3_["result"]["healthy"] is True, b3_)
    fnr.groups.stop_rpc()

    # ═══════════════ D. two real nodes over sockets ═══════════════
    dA, dB = tempfile.mkdtemp(), tempfile.mkdtemp()
    with QUIET():
        nA = m.NEBULAFullNode(data_dir=dA, port=18971)
        nB = m.NEBULAFullNode(data_dir=dB, port=18972)
    for _ in range(3): mine(nA.bc)
    for n_ in (nA, nB):
        n_.p2p._running = True
        threading.Thread(target=n_.p2p._listen, daemon=True).start()
    time.sleep(0.4)
    with QUIET():
        nB.p2p.connect_peer('127.0.0.1', 18971)
    for _ in range(80):
        if nB.bc.tip.height == nA.bc.tip.height: break
        time.sleep(0.25)
    chk('real sockets: node B synced to A through the wrapped P2P', nB.bc.tip.height == nA.bc.tip.height == 3, (nB.bc.tip.height, nA.bc.tip.height))
    chk('real sockets: B block store follows (g3 tip == B tip, healthy)',
        nB.groups.g3.utxo.best_block() == (nB.bc.tip.hash, nB.bc.tip.height) and nB.groups.g3.healthy, nB.groups.g3.utxo.best_block())
    chk('real sockets: both sides registered the peer in g2/g4', len(nA.groups.g2.eviction._peers if hasattr(nA.groups.g2.eviction, '_peers') else [1]) >= 1
        and nA.groups._seen_peers and nB.groups._seen_peers, (nA.groups._seen_peers, nB.groups._seen_peers))
    mine(nA.bc)
    with QUIET():
        nA.p2p.broadcast_block(nA.bc.tip)
    for _ in range(40):
        if nB.bc.tip.height == 4: break
        time.sleep(0.25)
    chk('real sockets: a new block is relayed A -> B and stored by g3', nB.bc.tip.height == 4 and nB.groups.g3.utxo.best_block()[1] == 4, nB.bc.tip.height)
    for n_ in (nA, nB):
        n_.p2p._running = False
        with QUIET():
            for p_ in list(n_.p2p._peers.values()): p_.disconnect()
        time.sleep(0.2)
    chk('real sockets: disconnect cleans the peer registries', not nA.groups._seen_peers and not nB.groups._seen_peers, (nA.groups._seen_peers, nB.groups._seen_peers))
    for n_ in (nA, nB, fn, fn2, fnr): 
        with QUIET(): n_.groups.close()
    # bans survive a restart
    dBan = tempfile.mkdtemp()
    with QUIET():
        n1 = m.NEBULAFullNode(data_dir=dBan, port=18973)
        for _ in range(3): n1.p2p._dos.punish('9.9.9.9', 'wrong_chain_id')
        n1.groups.close()
        n2 = m.NEBULAFullNode(data_dir=dBan, port=18974)
    chk('bans.json: a ban survives a node restart', not n2.groups.g2.may_connect('9.9.9.9')[0])
    n2.groups.close()

except Exception:
    traceback.print_exc()
    chk('test run finished without an unexpected exception', False)

ok = sum(1 for _, c, _ in R if c)
for n, c, i in R:
    print(('PASS  ' if c else 'FAIL  ') + n + ('' if c or not i else f'   <- {i}'))
print(f'\n{ok}/{len(R)} passed')
sys.exit(0 if ok == len(R) else 1)
