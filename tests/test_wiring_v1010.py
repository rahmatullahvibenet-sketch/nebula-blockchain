import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""NEBULA v10.10 - wiring tests: TransactionIndex (TxIndexLayer) + OrphanPool (P2PNode).
Run from the folder that contains nebula_v10_24.py:   python3 tests/test_wiring_v1010.py
Everything uses REAL signed transactions inside REAL mined blocks."""
import sys, os, io, time, ctypes, tempfile, contextlib, importlib.util, traceback, types
os.environ.setdefault('NEBULA_ALLOW_DEV_MODE', '1')      # tests only: throw-away chains

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
    R.append((name, bool(cond), str(info)[:140]))

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

def mk_block(bc, txs=(), prev=None, addr=MINER, ts=None, extra_reward=0):
    prev = prev or bc.tip
    h = prev.height + 1
    fees = sum(t.fee(bc.utxo) for t in txs)
    cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h) + fees + extra_reward, miner_address=addr)
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
    def tx(self, bc, payload):
        t = m.StateTxBuilder.build(bc, self.w, self.a, payload)
        assert t is not None, "could not build tx"
        return t

def world():
    with QUIET():
        bc = m.NEBULABlockchain()
        bc._dev_mode = True
    return bc

A = m.StateActions
def snap(layer):
    ix = layer.index
    return (dict(ix._txid_to_block), {a: sorted(v) for a, v in ix._addr_to_txids.items()})

try:
    # ═══════════════════  TRANSACTION INDEX  ═══════════════════
    bc = world()
    idx = m.TxIndexLayer.for_chain(bc)
    chk('index registered as bc._tx_index and as listener', bc._tx_index is idx and idx in bc._listeners)
    chk('for_chain is idempotent', m.TxIndexLayer.for_chain(bc) is idx and bc._listeners.count(idx) == 1)
    gtx = bc._chain[0].transactions[0].txid
    chk('genesis coinbase is indexed', idx.locate(gtx) == (0, 0), idx.locate(gtx))

    u1, u2 = User(bc), User(bc)
    t1 = u1.tx(bc, A.token_create('IDX', 8, 1000 * U))
    mine(bc, [t1])
    loc = idx.locate(t1.txid)
    chk('mined tx found with (height, position)', loc == (bc.height, 1), loc)
    chk('get() returns the real Transaction', idx.get(t1.txid) is not None and idx.get(t1.txid).txid == t1.txid)
    chk('unknown txid -> None', idx.get('00' * 32) is None and idx.locate('11' * 32) is None)
    chk('sender side is in the address history', t1.txid in idx.address_txids(u1.a))
    chk('coinbase paid to miner is in the miner history', len(idx.address_txids(MINER)) >= 1)
    info = bc.get_address_info(u1.a)
    chk('get_address_info: real tx_count + recent_txids', info['tx_count'] == idx.address_tx_count(u1.a) >= 1
        and t1.txid in info['recent_txids'], (info['tx_count'], info.get('recent_txids')))

    # a transaction OLDER than 100 blocks (BlockExplorer used to scan only the last 100)
    for _ in range(105):
        mine(bc)
    ex = m.BlockExplorer(bc)
    d = ex.tx_info(t1.txid)
    chk('BlockExplorer finds a tx older than 100 blocks', d is not None and d['block_height'] == loc[0]
        and d['confirmations'] == bc.height - loc[0] + 1, d and d.get('block_height'))
    saved_ix = bc._tx_index
    bc._tx_index = None
    chk('...and without the index it could not (the old behaviour)', ex.tx_info(t1.txid) is None)
    bc._tx_index = saved_ix

    # REST API
    old_chain = m.STATE.chain
    try:
        m.STATE.chain = bc
        st, body = m.tx_detail('/api/tx/' + t1.txid, {}, {})
        data = body.get('data', body) if isinstance(body, dict) else body
        chk('API /api/tx/<txid> returns a confirmed tx (was: always 404)', st == 200 and
            (data.get('status') == 'confirmed') and data.get('block_height') == loc[0], (st, str(body)[:120]))
        t_mp = u2.tx(bc, A.token_create('MEMP', 8, 5 * U))
        okm, msgm = bc.add_to_mempool(t_mp)
        st2, body2 = m.tx_detail('/api/tx/' + t_mp.txid, {}, {})
        data2 = body2.get('data', body2) if isinstance(body2, dict) else body2
        chk('API finds an unconfirmed tx in the mempool (_txs)', okm and st2 == 200 and data2.get('status') == 'mempool', (okm, msgm, st2, str(body2)[:100]))
        st3, body3 = m.tx_detail('/api/tx/' + 'ab' * 32, {}, {})
        chk('API 404 for an unknown tx', st3 == 404, st3)
        # real HTTP round-trip (before v10.10 every request dropped the connection: ok()/err() were CLI printers)
        import urllib.request, urllib.error, json as _json
        srv = m.NEBULAAPIServer(host='127.0.0.1', port=18771, ws_port=18772)
        with QUIET():
            srv.start()
        time.sleep(0.5)
        def http(path):
            try:
                r = urllib.request.urlopen('http://127.0.0.1:18771' + path, timeout=10)
                return r.status, _json.loads(r.read())
            except urllib.error.HTTPError as e:
                return e.code, _json.loads(e.read())
        hs, hb = http('/api/tx/' + t1.txid)
        chk('HTTP GET /api/tx/<txid> -> 200 success + confirmed + block_height',
            hs == 200 and hb.get('success') and hb['data'].get('status') == 'confirmed'
            and hb['data'].get('block_height') == loc[0], (hs, str(hb)[:120]))
        hs, hb = http('/api/tx/' + 'cd' * 32)
        chk('HTTP 404 body is JSON with success=false', hs == 404 and hb.get('success') is False, (hs, hb))
        hs, hb = http('/api/address/' + u1.a)
        chk('HTTP /api/address/<addr> has tx_count + recent_txids',
            hs == 200 and hb['data'].get('tx_count', 0) >= 1 and t1.txid in hb['data'].get('recent_txids', []), (hs, str(hb)[:140]))
        hs, hb = http('/api/status')
        chk('HTTP /api/status answers', hs == 200 and hb.get('success'), (hs, str(hb)[:100]))
        try:
            srv.stop()
        except Exception:
            pass
    finally:
        m.STATE.chain = old_chain
    mine(bc, [t_mp])
    chk('mempool tx becomes confirmed in the index', idx.locate(t_mp.txid) == (bc.height, 1))

    fresh = m.TxIndexLayer(bc); fresh.rebuild()
    chk('live index == fresh replay of the chain', snap(fresh) == snap(idx))

    # ── reorg ──
    bcR = world(); ixR = m.TxIndexLayer.for_chain(bcR)
    v1, v2 = User(bcR), User(bcR)
    mine(bcR, [v1.tx(bcR, A.token_create('FORK', 8, 1000 * U))])
    base = bcR.tip
    tx_a = v1.tx(bcR, A.token_transfer(1, v2.a, 100 * U))
    tx_b = v1.tx(bcR, A.token_transfer(1, v2.a, 7 * U))      # conflicting alternative (same inputs)
    mine(bcR, [tx_a]); mine(bcR)
    chk('main branch: tx_a indexed', ixR.locate(tx_a.txid) is not None and ixR.locate(tx_b.txid) is None)
    prev = base; msgs = []
    for i in range(4):
        blk = mk_block(bcR, [tx_b] if i == 0 else [], prev=prev, ts=_ts[0] + 50 + i)
        with QUIET():
            msgs.append(bcR.add_block(blk)[1])
        prev = blk
    chk('reorg happened', any('REORG' in x for x in msgs), msgs)
    chk('after reorg: tx_a gone from the index, tx_b indexed', ixR.locate(tx_a.txid) is None
        and ixR.locate(tx_b.txid) == (base.height + 1, 1), (ixR.locate(tx_a.txid), ixR.locate(tx_b.txid)))
    chk('after reorg: orphaned tx_a no longer in sender history', tx_a.txid not in ixR.address_txids(v1.a))
    freshR = m.TxIndexLayer(bcR); freshR.rebuild()
    chk('after reorg: live index == fresh replay', snap(freshR) == snap(ixR))
    chk('after reorg the layer did not need a rebuild', ixR._stale is False)

    # ── isolation / self-heal ──
    orig = idx._add
    idx._add = lambda b: (_ for _ in ()).throw(RuntimeError('boom'))
    h0 = bc.height
    with QUIET():
        okb, msgb = bc.add_block(mk_block(bc))
    idx._add = orig
    chk('index crash does NOT affect block acceptance', okb and bc.height == h0 + 1, msgb)
    chk('stale index heals itself on the next query', idx.locate(t1.txid) == loc and idx._stale is False)
    freshS = m.TxIndexLayer(bc); freshS.rebuild()
    chk('healed index == fresh replay', snap(freshS) == snap(idx))

    # ── save / load (restart) ──
    d_ = tempfile.mkdtemp()
    with QUIET():
        bc.save(d_)
        bc2 = m.NEBULABlockchain.load(d_)
    ix2 = m.TxIndexLayer.for_chain(bc2)
    chk('after restart the index finds old transactions', ix2.locate(t1.txid) == loc and ix2.get(t_mp.txid) is not None)
    with QUIET():
        okr, msgr = bc2.add_block(mk_block(bc2))
    chk('restarted chain accepts a block and the index follows', okr and ix2._height == bc2.height, msgr)

    # ── full node wiring ──
    with QUIET():
        node = m.NEBULAFullNode(data_dir=tempfile.mkdtemp(), port=18999)
    chk('NEBULAFullNode attaches the index', isinstance(node.tx_index, m.TxIndexLayer) and node.bc._tx_index is node.tx_index)
    chk('FullNode P2P owns an OrphanPool', isinstance(node.p2p.orphan_pool, m.OrphanPool))

    # ═══════════════════  ORPHAN POOL  ═══════════════════
    class FakePeer:
        def __init__(self):
            self.sent = []
            self.info = types.SimpleNamespace(addr='9.9.9.9:1', state=None)
        def send(self, msg): self.sent.append(msg)

    def feed(node, peer, blk):
        node._handle_block(peer, {"blocks": [blk.to_dict()]})

    chainA = world()
    blocks = []
    for _ in range(4):
        mine(chainA); blocks.append(chainA.tip)
    b1, b2, b3, b4 = blocks

    chainB = world()
    with QUIET():
        nodeB = m.P2PNode(chainB, port=18998)
    got = []
    nodeB.on_new_block = lambda b: got.append(b.height)
    peer = FakePeer()
    with QUIET():
        for blk in (b4, b3, b2):
            feed(nodeB, peer, blk)
    chk('out-of-order blocks are kept, chain unchanged', chainB.height == 0 and nodeB.orphan_pool.size() == 3,
        (chainB.height, nodeB.orphan_pool.size()))
    chk('orphan hash stays re-processable (not stuck in _known_invs)', b4.hash not in nodeB._known_invs)
    chk('missing history is requested from the peer (rate-limited to once)',
        len([x for x in peer.sent if getattr(x, 'type', getattr(x, 'msg_type', None)) in (m.MsgType.GETBLOCKS, 'getblocks')]) == 1
        or len(peer.sent) == 1, len(peer.sent))
    with QUIET():
        feed(nodeB, peer, b1)
    chk('when the parent arrives every stored orphan connects', chainB.height == 4 and chainB.tip.hash == b4.hash
        and nodeB.orphan_pool.size() == 0, (chainB.height, nodeB.orphan_pool.size()))
    chk('on_new_block fired for parent AND adopted children, in order', got == [1, 2, 3, 4], got)
    chk('adopted chain is identical to the source chain', [b.hash for b in chainB._chain] == [b.hash for b in chainA._chain])

    # junk (no proof of work) is never stored
    chainC = world()
    with QUIET():
        nodeC = m.P2PNode(chainC, port=18997)
    junk = mk_block(chainA, prev=b2)
    junk.header.nonce = (junk.header.nonce + 1) & 0xFFFFFFFF
    junk._hash = None
    if junk.header.meets_target():
        junk.header.nonce = (junk.header.nonce + 7) & 0xFFFFFFFF
    with QUIET():
        feed(nodeC, FakePeer(), junk)
    chk('block without valid PoW is NOT stored (anti-spam)', nodeC.orphan_pool.size() == 0, nodeC.orphan_pool.size())

    # an orphan with real PoW but INVALID content is rejected when it is finally connected
    chainD = world()
    with QUIET():
        nodeD = m.P2PNode(chainD, port=18996)
    bad2 = mk_block(chainA, prev=b1, extra_reward=1)      # coinbase pays 1 neb too much; PoW is real
    with QUIET():
        feed(nodeD, FakePeer(), bad2)
        stored = nodeD.orphan_pool.size()
        feed(nodeD, FakePeer(), b1)
    chk('invalid orphan was stored (PoW ok) ...', stored == 1, stored)
    chk('... but consensus rejects it on connect: chain stops at the valid parent, pool emptied',
        chainD.height == 1 and chainD.tip.hash == b1.hash and nodeD.orphan_pool.size() == 0, (chainD.height, nodeD.orphan_pool.size()))

    # siblings: two blocks on the same parent are both kept and both tried
    chainE = world()
    with QUIET():
        nodeE = m.P2PNode(chainE, port=18995)
    sib_a = mk_block(chainA, prev=b1, ts=_ts[0] + 11)
    sib_b = mk_block(chainA, prev=b1, ts=_ts[0] + 12, addr='NLfMw4STiuDo9pMixgNnXZapH3sXasYVk5')
    with QUIET():
        feed(nodeE, FakePeer(), sib_a); feed(nodeE, FakePeer(), sib_b)
    chk('siblings with the same parent are both stored', len(nodeE.orphan_pool.get_children(b1.hash)) == 2)
    with QUIET():
        feed(nodeE, FakePeer(), b1)
    chk('both siblings were tried; pool empty; best chain valid', nodeE.orphan_pool.size() == 0 and chainE.height == 2,
        (nodeE.orphan_pool.size(), chainE.height))

    # pool unit behaviour
    pool = m.OrphanPool()
    c1 = mk_block(chainA, prev=b2, ts=_ts[0] + 21)
    c2 = mk_block(chainA, prev=b2, ts=_ts[0] + 22, addr='NLfMw4STiuDo9pMixgNnXZapH3sXasYVk5')
    pool.add(c1); pool.add(c2)
    pool.remove(c1.hash)
    chk('remove(sibling) keeps the other sibling reachable',
        [b.hash for b in pool.get_children(b2.hash)] == [c2.hash] and pool.get_by_prev(b2.hash).hash == c2.hash)
    chk('adding the same block twice does not duplicate', pool.add(c2) and pool.size() == 1)
    pool._times[c2.hash] = time.time() - m.OrphanPool.ORPHAN_TTL - 5
    pool.add(c1)
    chk('expired orphans are purged on add()', c2.hash not in pool and c1.hash in pool and pool.size() == 1)
    small = m.OrphanPool(); small.MAX_ORPHANS = 3
    for i in range(6):
        small.add(mk_block(chainA, prev=b2, ts=_ts[0] + 40 + i, addr=MINER))
    chk('pool stays bounded', small.size() <= 3, small.size())

except Exception:
    R.append(('UNEXPECTED ERROR', False, traceback.format_exc()[-400:]))

bad = 0
for n, ok, info in R:
    if not ok:
        bad += 1
    print(('PASS  ' if ok else 'FAIL  ') + n + ('' if ok or not info else '   -> ' + info))
print(f"\n{len(R) - bad}/{len(R)} passed")
sys.exit(1 if bad else 0)
