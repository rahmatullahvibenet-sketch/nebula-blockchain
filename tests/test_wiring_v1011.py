import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""NEBULA v10.11 - wiring tests: FeeEstimator (FeeLayer) + PeerAddressBook (P2PNode).
Run from the folder that contains nebula_v10_24.py:   python3 tests/test_wiring_v1011.py
Real signed transactions inside real mined blocks; real sockets for the P2P parts."""
import sys, os, io, time, ctypes, tempfile, contextlib, importlib.util, traceback, types, threading, socket, json

os.environ.setdefault('NEBULA_ALLOW_DEV_MODE', '1')      # tests only: throw-away chains
os.environ.pop('NEBULA_ALLOW_PRIVATE_PEERS', None)       # default policy must hold

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
    R.append((name, bool(cond), str(info)[:160]))

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
close = lambda a, b, tol=0.06: abs(a - b) <= tol

try:
    # ═══════════════════  FEE ESTIMATOR (unit)  ═══════════════════
    fe = m.FeeEstimator()
    for r in [2.0, 5.0, 20.0, 100.0] * 50:
        fe.record_confirmed(r, 1)
    est = fe.estimate_fee(1)
    chk('estimate_fee returns the LOWEST sufficient bucket (v10.10 returned the highest: 100)',
        est is not None and est < 3.0, est)

    fe = m.FeeEstimator()
    for _ in range(40): fe.record_confirmed(100.0, 1)
    for _ in range(40): fe.record_unconfirmed(3.0, 1)       # cheap txs still waiting after 1 block
    e1 = fe.estimate_fee(1)
    chk('cheap txs that miss the target push the estimate up to what really confirms',
        e1 is not None and 50 <= e1 <= 100.0, e1)

    fe = m.FeeEstimator()
    for _ in range(40): fe.record_confirmed(5.0, 8)         # rate 5 needs ~8 blocks
    chk('target 1 has no evidence from txs that took 8 blocks', fe.estimate_fee(1) is None, fe.estimate_fee(1))
    chk('target 12 does (txs paying 5 confirm within 12)', fe.estimate_fee(12) is not None
        and fe.estimate_fee(12) <= 5.0, fe.estimate_fee(12))

    fe = m.FeeEstimator()
    fe.record_confirmed(5.0, 1); fe.record_confirmed(10.0, 2)
    chk('too little data -> None (not a made-up number)', fe.estimate_fee(6) is None)
    chk('legacy smart_fee still >= 1 (built-in test)', fe.smart_fee(6) >= 1)
    fe.record_unconfirmed(5.0)                                # legacy one-argument call
    chk('legacy record_unconfirmed(rate) still works', True)
    fe2 = m.FeeEstimator()
    for _ in range(30): fe2.record_confirmed(50.0, 1)
    s0 = fe2.samples(1)
    for _ in range(1000): fe2.decay_all()
    chk('old observations decay away', fe2.samples(1) < s0 * 0.2, (s0, fe2.samples(1)))
    chk('fee_table() still works', set(fe2.fee_table()) == {f"{b} blocks" for b in m.FEE_ESTIMATION_BLOCKS})

    # ═══════════════════  FEE LAYER (real chain)  ═══════════════════
    bc = world()
    fl = m.FeeLayer.for_chain(bc)
    chk('layer registered as listener + bc._fee_layer', bc._fee_layer is fl and fl in bc._listeners)
    chk('for_chain idempotent', m.FeeLayer.for_chain(bc) is fl and bc._listeners.count(fl) == 1)
    chk('old mempool.fee_estimates() consumers now get real data', set(bc.mempool.fee_estimates())
        == {f"{b} blocks" for b in m.FEE_ESTIMATION_BLOCKS})
    r0 = fl.estimate(6, 250)
    chk('no data yet -> source "default", fee == protocol minimum (honest)',
        r0['source'] == 'default' and r0['fee'] == m.MIN_TX_FEE, r0)

    # exact fee of a confirmed tx (inputs from undo data)
    uA = User(bc)
    txA = uA.tx(bc, A.token_create('FEE1', 8, 10 * U), fee=12_345)
    fee_before = txA.fee(bc.utxo)
    mine(bc, [txA])
    rows = fl._block_fees(bc.tip)
    chk('exact per-tx fee recovered from the connected block', rows is not None and len(rows) == 1
        and rows[0][0] == txA.txid and rows[0][2] == 12_345 == fee_before, rows)
    chk('fee rate uses the mempool definition (fee // size)', rows[0][1] == float(12_345 // txA.byte_size())
        and rows[0][3] == txA.byte_size(), rows[0])
    cb = bc.tip.transactions[0]
    chk('sum of per-tx fees == coinbase minus subsidy', sum(r[2] for r in rows)
        == sum(o.value for o in cb.outputs) - m.mining_reward(bc.height))
    chk('layer recorded it', fl.stats()['txs_recorded'] == 1 and fl.stats()['height'] == bc.height, fl.stats())

    # waited-blocks accounting
    bcW = world(); flW = m.FeeLayer.for_chain(bcW); e = flW.estimator
    uW = User(bcW)
    tW = uW.tx(bcW, A.token_create('WAIT', 8, 10 * U))
    okm, msgm = bcW.add_to_mempool(tW)
    rate = float(bcW.mempool._meta[tW.txid][0]); ix = e._bucket_index(rate)
    tot0 = {t: e._tgt_tot[t][ix] for t in e._tgt_tot}; ok0 = {t: e._tgt_ok[t][ix] for t in e._tgt_ok}
    mine(bcW); mine(bcW)                                    # two blocks without it
    d1 = e._tgt_tot[1][ix] - tot0[1]; d2 = e._tgt_tot[2][ix] - tot0[2]
    chk('pending after 1 block = a miss for target 1; after 2 = a miss for target 2',
        okm and close(d1, 1) and close(d2, 1) and close(e._tgt_tot[3][ix] - tot0[3], 0), (okm, msgm, d1, d2))
    mine(bcW, [tW])                                         # confirmed on the 3rd block
    dok = {t: round(e._tgt_ok[t][ix] - ok0[t], 2) for t in (1, 2, 3, 6)}
    dtot = {t: round(e._tgt_tot[t][ix] - tot0[t], 2) for t in (1, 2, 3, 6)}
    chk('confirmed after 3 blocks: success only for targets >= 3',
        close(dok[1], 0) and close(dok[2], 0) and close(dok[3], 1) and close(dok[6], 1), dok)
    chk('...and no double counting of the earlier misses',
        close(dtot[1], 1) and close(dtot[2], 1) and close(dtot[3], 1) and close(dtot[6], 1), dtot)
    chk('stamps of confirmed txs are forgotten', tW.txid not in flW._first_seen and flW.stats()['pending_tracked'] == 0)

    uN = User(bcW)
    tN = uN.tx(bcW, A.token_create('NEVER', 8, 10 * U))
    rN = bcW.mempool  # never submitted to this node's mempool: first seen inside its block
    rate_n = float((m.FeeLayer._block_fees.__func__ if hasattr(m.FeeLayer._block_fees, '__func__') else m.FeeLayer._block_fees)) if False else None
    ixn = None
    before = {t: e._tgt_ok[t][:] for t in e._tgt_ok}
    mine(bcW, [tN])
    gained = [t for t in (1, 2, 3, 6, 12) if sum(e._tgt_ok[t]) > sum(before[t]) * 0.998 + 0.5]
    chk('a tx first seen inside its block waited exactly 1 block (success for every target)',
        gained == [1, 2, 3, 6, 12], gained)

    # market-like data: cheap txs never confirm, expensive ones do
    bcM = world(); flM = m.FeeLayer.for_chain(bcM)
    hi_users = [User(bcM) for _ in range(4)]
    lo_rate = hi_rate = None
    for rnd in range(4):
        hi = [u.tx(bcM, A.token_create(f'H{rnd}{i}', 8, U), fee=40_000) for i, u in enumerate(hi_users)]
        lo_users = [User(bcM) for _ in range(4)]
        lo = [u.tx(bcM, A.token_create(f'L{rnd}{i}', 8, U), fee=1_000) for i, u in enumerate(lo_users)]
        for t in hi + lo:
            okx, msgx = bcM.add_to_mempool(t)
            assert okx, msgx
        lo_rate = lo[0].fee(bcM.utxo) // lo[0].byte_size(); hi_rate = hi[0].fee(bcM.utxo) // hi[0].byte_size()
        mine(bcM, hi)
    r1 = flM.estimate(1, 250)
    chk('market data: estimate sits between the cheap rate (never confirms) and the paying rate',
        r1['source'] == 'data' and lo_rate < r1['fee_rate'] <= hi_rate, (r1, lo_rate, hi_rate))
    chk('estimate() fee >= MIN_TX_FEE and scales with size',
        r1['fee'] >= m.MIN_TX_FEE and flM.estimate(1, 500)['fee'] >= flM.estimate(1, 250)['fee'])
    chk('conservative adds a margin', flM.estimate(1, 250, True)['fee_rate'] > r1['fee_rate'])
    tb = flM.table()
    chk('table() covers all standard targets', list(tb) == [f"{b} blocks" for b in m.FEE_ESTIMATION_BLOCKS])
    chk('simple_table() gives ints >= 1', all(isinstance(v, int) and v >= 1 for v in flM.simple_table().values()))

    # reorg
    bcR = world(); flR = m.FeeLayer.for_chain(bcR)
    v1 = User(bcR)
    mine(bcR, [v1.tx(bcR, A.token_create('FORK', 8, 1000 * U))])
    base = bcR.tip
    tx_a = v1.tx(bcR, A.token_transfer(1, v1.a, 1 * U), fee=10_000)
    tx_b = v1.tx(bcR, A.token_transfer(1, v1.a, 2 * U), fee=30_000)      # conflicting twin, different fee
    mine(bcR, [tx_a]); mine(bcR)
    n_before = flR.stats()['txs_recorded']
    prev = base; msgs = []
    for i in range(4):
        blk = mk_block(bcR, [tx_b] if i == 0 else [], prev=prev, ts=_ts[0] + 50 + i)
        with QUIET():
            msgs.append(bcR.add_block(blk)[1])
        prev = blk
    st = flR.stats()
    chk('reorg handled by on_reorg without a gap or crash', any('REORG' in x for x in msgs)
        and st['reorgs'] == 1 and st['gaps'] == 0 and st['height'] == bcR.height, (msgs[-1:], st))
    chk('the tx that only exists on the new branch was recorded (once)',
        tx_b.txid in flR._recorded and st['txs_recorded'] == n_before + 1, (st, n_before))

    # isolation
    orig = fl._process
    fl._process = lambda *a, **k: (_ for _ in ()).throw(RuntimeError('boom'))
    h0 = bc.height
    with QUIET():
        okb, msgb = bc.add_block(mk_block(bc))
    fl._process = orig
    chk('a fee-layer crash can NOT affect block acceptance', okb and bc.height == h0 + 1, msgb)
    mine(bc)
    chk('the layer recovers on the next block (gap noticed, state consistent)',
        fl.stats()['height'] == bc.height and fl.stats()['gaps'] == 1, fl.stats())

    # save / load (restart): undo data is not persisted -> must not crash, must say so honestly
    d_ = tempfile.mkdtemp()
    with QUIET():
        bc.save(d_)
        bc2 = m.NEBULABlockchain.load(d_)
    fl2 = m.FeeLayer.for_chain(bc2)
    chk('after restart the layer attaches without crashing', fl2._height == bc2.height)
    chk('...old blocks without undo data are skipped, not guessed',
        m.FeeLayer._block_fees(bc2._chain[txA_h := 1]) is None and fl2.stats()['blocks_skipped'] >= 1, fl2.stats())
    with QUIET():
        okr, msgr = bc2.add_block(mk_block(bc2))
    chk('restarted chain accepts a block and the layer follows', okr and fl2.stats()['height'] == bc2.height, msgr)

    # ═══════════════════  PEER ADDRESS BOOK (unit)  ═══════════════════
    bk = m.PeerAddressBook()
    bad = [('127.0.0.1', 8333), ('10.0.0.5', 8333), ('192.168.1.2', 8333), ('0.0.0.0', 8333),
           ('224.0.0.1', 8333), ('169.254.1.1', 8333), ('8.8.8.8', 0), ('8.8.8.8', 70000), ('8.8.8.8', True),
           ('8.8.8.8', '8333'), (None, 8333), (123, 8333), ('localhost', 8333), ('x' * 300, 8333),
           ('bad host', 8333), ('..evil', 8333), ('-x.com', 8333), ('::1', 8333)]
    chk('gossiped junk / private / loopback / bad ports are all rejected',
        not any(bk.add(h, p, source='gossip') for h, p in bad) and bk.size() == 0, [x for x in bad if bk.add(*x)])
    chk('public IPv4/IPv6/DNS names accepted',
        bk.add('8.8.8.8', 8333, source='gossip') and bk.add('2606:4700::1111', 8333, source='gossip')
        and bk.add('node.example.org', 8333, source='gossip') and bk.size() == 3)
    chk('trusted (operator/seed/outbound) private address allowed', bk.add('127.0.0.1', 9, trusted=True))
    priv = m.PeerAddressBook(allow_private=True)
    chk('allow_private (LAN testnet) accepts gossiped private addresses', priv.add('10.1.2.3', 8333, source='gossip'))
    chk('add() is True only when NEW', not bk.add('8.8.8.8', 8333) and bk.add('9.9.9.9', 8333))
    bk.mark_attempt('8.8.8.8', 8333); bk.mark_attempt('8.8.8.8', 8333)
    bk.add('8.8.8.8', 8333)
    chk('re-adding a known address keeps attempts (v10.10 erased them)', bk._addrs['8.8.8.8:8333'].attempts == 2)
    bk.mark_good('8.8.8.8', 8333)
    for _ in range(10): bk.mark_attempt('8.8.8.8', 8333)
    chk('a verified address survives failures', '8.8.8.8:8333' in bk._addrs)
    for _ in range(m.PeerAddressBook.MAX_FAILS): bk.mark_attempt('9.9.9.9', 8333)
    chk('a never-successful address is dropped after MAX_FAILS', '9.9.9.9:8333' not in bk._addrs)

    small = m.PeerAddressBook(); small.MAX_ADDRS = 5
    for i in range(40):
        small.add(f'20.0.0.{i + 1}', 8333, source='gossip')
    chk('the book is bounded (v10.10 grew without limit when nothing was stale)', small.size() <= 5, small.size())
    small2 = m.PeerAddressBook(); small2.MAX_ADDRS = 3
    for i in range(3):
        small2.add(f'21.0.0.{i + 1}', 8333, source='gossip')
    small2.mark_good('21.0.0.2', 8333)
    for i in range(10):
        small2.add(f'22.0.0.{i + 1}', 8333, source='gossip')
    chk('when full, the verified address is the last to go', '21.0.0.2:8333' in small2._addrs and small2.size() <= 3)

    cb_ = m.PeerAddressBook()
    for i, ip in enumerate(['30.0.0.1', '30.0.0.2', '30.0.0.3', '30.0.0.4']):
        cb_.add(ip, 8333, source='gossip'); time.sleep(0.002)
    cb_.mark_good('30.0.0.2', 8333); time.sleep(0.002); cb_.mark_good('30.0.0.1', 8333)
    cb_.mark_attempt('30.0.0.3', 8333)
    for _ in range(m.PeerAddressBook.MAX_FAILS - 1): cb_.mark_attempt('30.0.0.4', 8333)
    cands = cb_.candidates(10, exclude={'30.0.0.3:8333'})
    chk('candidates: verified first (most recent first), exclusions honoured',
        cands[0] == ('30.0.0.1', 8333) and cands[1] == ('30.0.0.2', 8333) and ('30.0.0.3', 8333) not in cands, cands)
    cb_.mark_attempt('30.0.0.4', 8333)
    chk('candidates: failed addresses are skipped', ('30.0.0.4', 8333) not in cb_.candidates(10))
    g = cb_.gossip_list(10)
    chk('gossip_list: only addresses WE verified recently', {(a['host']) for a in g} == {'30.0.0.1', '30.0.0.2'}, g)
    cb_._addrs['30.0.0.1:8333'].last_success = time.time() - m.PeerAddressBook.GOOD_WINDOW - 10
    chk('gossip_list: stale verification not advertised', [a['host'] for a in cb_.gossip_list(10)] == ['30.0.0.2'])

    pth = os.path.join(tempfile.mkdtemp(), 'peers.json')
    chk('save() ok, atomic (no .tmp left)', cb_.save(pth) and not os.path.exists(pth + '.tmp'))
    cb3 = m.PeerAddressBook()
    n3 = cb3.load(pth)
    chk('load() restores addresses with their history', n3 == cb_.size() and
        cb3._addrs['30.0.0.2:8333'].last_success == cb_._addrs['30.0.0.2:8333'].last_success
        and cb3._addrs['30.0.0.3:8333'].attempts == cb_._addrs['30.0.0.3:8333'].attempts == 1, (n3, cb_.size()))
    open(pth, 'w').write('{not json')
    chk('corrupt file -> 0 loaded, no crash', m.PeerAddressBook().load(pth) == 0)
    open(pth, 'w').write(json.dumps({"addrs": [{"host": "127.0.0.1", "port": 1, "source": "gossip"}, 5, "x",
                                               {"host": "8.8.4.4", "port": "bad"}, {"host": "8.8.4.4", "port": 53}]}))
    cb4 = m.PeerAddressBook()
    chk('bad rows are skipped, good rows kept (saved rows count as trusted)', cb4.load(pth) == 2 and cb4.size() == 2)
    chk('missing file -> 0', m.PeerAddressBook().load(pth + '.nope') == 0)

    # ═══════════════════  P2PNode wiring  ═══════════════════
    class FakePeer:
        def __init__(self, host='9.9.9.9', port=8333, inbound=False, connected=True):
            self.sent = []; self.inbound = inbound; self.disconnected = False
            self.info = types.SimpleNamespace(host=host, port=port, addr=f'{host}:{port}', version=0, chain_id=0,
                                              height=0, user_agent='', state=m.PeerState.CONNECTED if connected
                                              else m.PeerState.CONNECTING, last_seen=time.time())
        def send(self, msg): self.sent.append(msg)
        def disconnect(self): self.disconnected = True

    bcP = world()
    node = m.P2PNode(bcP, host='127.0.0.1', port=18981, data_dir=tempfile.mkdtemp())
    chk('P2PNode owns a PeerAddressBook', isinstance(node.addr_book, m.PeerAddressBook))
    calls = []
    node.connect_peer = lambda h, p: calls.append((h, p)) or True
    payload = {"addrs": [{"host": "40.0.0.1", "port": 8333}, {"host": "127.0.0.1", "port": 8333},
                         {"host": "10.9.9.9", "port": 8333}, "junk", {"host": "40.0.0.2"},
                         {"host": "40.0.0.1", "port": 8333}, {"host": None, "port": 1}, 7]}
    node._handle_message(FakePeer(), m.Message(m.MsgType.ADDR, payload))
    time.sleep(0.3)
    chk('ADDR: only valid NEW addresses remembered and dialled (loopback/private/junk/dup ignored)',
        sorted(calls) == [('40.0.0.1', 8333), ('40.0.0.2', m.DEFAULT_PORT)] and node.addr_book.size() == 2, (calls, node.addr_book.size()))
    calls.clear()
    node._handle_message(FakePeer(), m.Message(m.MsgType.ADDR, payload)); time.sleep(0.2)
    chk('ADDR: an address already known is not dialled again', calls == [])
    node._handle_message(FakePeer(), m.Message(m.MsgType.ADDR, {"addrs": "not a list"}))
    node._handle_message(FakePeer(), m.Message(m.MsgType.ADDR, {"addrs": {"host": "1.1.1.1"}}))
    chk('ADDR: malformed payload ignored (no crash)', node.addr_book.size() == 2)
    flood = {"addrs": [{"host": f"50.{i // 250}.{i % 250 + 1}.9", "port": 8333} for i in range(5000)]}
    calls.clear()
    node._handle_message(FakePeer(), m.Message(m.MsgType.ADDR, flood)); time.sleep(0.5)
    chk('ADDR: at most 100 addresses taken per message, at most 20 dialled', node.addr_book.size() <= 2 + 100 and len(calls) <= 20,
        (node.addr_book.size(), len(calls)))

    # GETADDR
    node2 = m.P2PNode(bcP, host='127.0.0.1', port=18982)
    out_p = FakePeer('60.0.0.1', 8333, inbound=False); in_p = FakePeer('70.0.0.1', 51234, inbound=True)
    node2._peers = {out_p.info.addr: out_p, in_p.info.addr: in_p}
    node2.addr_book.add('61.0.0.1', 8333, source='gossip'); node2.addr_book.add('62.0.0.1', 8333, source='gossip')
    node2.addr_book.mark_good('62.0.0.1', 8333)
    asker = FakePeer()
    node2._handle_message(asker, m.Message(m.MsgType.GETADDR))
    got = {(a['host'], a['port']) for a in asker.sent[-1].payload['addrs']}
    chk('GETADDR: outbound peers + verified book entries; NOT inbound ephemeral ports, NOT unverified gossip',
        got == {('60.0.0.1', 8333), ('62.0.0.1', 8333)}, got)

    # VERSION handshake bookkeeping
    node3 = m.P2PNode(bcP, host='127.0.0.1', port=18983)
    node3.addr_book.add('63.0.0.1', 8333, source='gossip')
    good = FakePeer('63.0.0.1', 8333, connected=False)
    node3._handle_message(good, m.Message(m.MsgType.VERSION, {"version": 1, "chain_id": m.CHAIN_ID, "height": 0}))
    chk('VERSION (right chain, outbound) marks the address verified', node3.addr_book._addrs['63.0.0.1:8333'].last_success > 0)
    node3.addr_book.add('64.0.0.1', 8333, source='gossip')
    wrong = FakePeer('64.0.0.1', 8333, connected=False)
    node3._handle_message(wrong, m.Message(m.MsgType.VERSION, {"version": 1, "chain_id": m.CHAIN_ID + 1, "height": 0}))
    chk('VERSION (wrong chain) forgets the address and disconnects', '64.0.0.1:8333' not in node3.addr_book._addrs and wrong.disconnected)
    node3.addr_book.add('65.0.0.1', 8333, source='gossip')
    inb = FakePeer('65.0.0.1', 8333, inbound=True, connected=False)
    node3._handle_message(inb, m.Message(m.MsgType.VERSION, {"version": 1, "chain_id": m.CHAIN_ID, "height": 0}))
    chk('VERSION on an INBOUND connection does not verify a book entry', node3.addr_book._addrs['65.0.0.1:8333'].last_success == 0)

    # connect_peer: failure counted, success remembered (real sockets)
    s_closed = socket.socket(); s_closed.bind(('127.0.0.1', 0)); dead_port = s_closed.getsockname()[1]; s_closed.close()
    node4 = m.P2PNode(bcP, host='127.0.0.1', port=18984)
    node4.addr_book.add('127.0.0.1', dead_port, trusted=True)
    r_ = node4.connect_peer('127.0.0.1', dead_port)
    chk('connect_peer failure -> attempt counted', r_ is False and node4.addr_book._addrs[f'127.0.0.1:{dead_port}'].attempts == 1)

    # ── real two-node handshake: restart + reconnect from peers.json ──
    dirA, dirB = tempfile.mkdtemp(), tempfile.mkdtemp()
    nodeA = m.P2PNode(world(), host='127.0.0.1', port=18991, data_dir=dirA)
    nodeA._running = True
    threading.Thread(target=nodeA._listen, daemon=True).start()
    time.sleep(0.4)
    nodeB = m.P2PNode(world(), host='127.0.0.1', port=18992, data_dir=dirB)
    nodeB.addr_book.add('127.0.0.1', 18991, trusted=True)            # as if remembered from an earlier run
    nodeB._running = True
    with QUIET():
        nodeB.stop()                                                  # writes peers.json (shutdown)
    chk('stop() persists peers.json', os.path.exists(os.path.join(dirB, 'peers.json')))
    nodeB2 = m.P2PNode(world(), host='127.0.0.1', port=18992, data_dir=dirB)   # "restart"
    chk('restart: address book reloaded from peers.json', nodeB2.addr_book.size() == 1)
    nodeB2._running = True
    with QUIET():
        tried = nodeB2._connect_from_book(4)
    time.sleep(1.5)
    ent = nodeB2.addr_book._addrs.get('127.0.0.1:18991')
    chk('restart: node redials the remembered peer', tried == 1 and '127.0.0.1:18991' in nodeB2._peers, (tried, list(nodeB2._peers)))
    chk('real handshake verified the entry (mark_good) and A saw an inbound peer',
        ent is not None and ent.last_success > 0 and nodeA.peer_count() >= 1, (ent and ent.last_success, nodeA.peer_count()))
    chk('network_info exposes the book', nodeB2.network_info()['addr_book']['verified'] == 1, nodeB2.network_info())
    for n_ in (nodeA, nodeB2):
        n_._running = False
        with QUIET():
            for p_ in list(n_._peers.values()):
                p_.disconnect()

    # ═══════════════════  FULL NODE + API  ═══════════════════
    dN = tempfile.mkdtemp()
    with QUIET():
        fn = m.NEBULAFullNode(data_dir=dN, port=18995)
    chk('NEBULAFullNode attaches FeeLayer', isinstance(fn.fee_layer, m.FeeLayer) and fn.bc._fee_layer is fn.fee_layer)
    chk('FullNode P2P gets data_dir (peers.json) and a book', fn.p2p._addr_file == os.path.join(dN, 'peers.json'))

    old_chain, old_net = m.STATE.chain, m.STATE.network
    try:
        m.STATE.chain = bcM; m.STATE.network = node2
        st, body = m.fee_estimates_api('/api/fees', {}, {})
        d = body['data']
        chk('API /api/fees: table with source/samples/min_fee', st == 200 and len(d['estimates']) == len(m.FEE_ESTIMATION_BLOCKS)
            and d['estimates']['1 blocks']['source'] == 'data' and d['min_fee'] == m.MIN_TX_FEE, (st, str(body)[:140]))
        st, body = m.fee_estimates_api('/api/fees', {'target': ['6'], 'size': ['400']}, {})
        chk('API /api/fees?target&size', st == 200 and body['data']['estimate']['target_blocks'] == 6
            and body['data']['estimate']['tx_size'] == 400, str(body)[:120])
        st, body = m.fee_estimates_api('/api/fees', {'target': ['abc']}, {})
        chk('API /api/fees bad input -> 400', st == 400, (st, body))
        st, body = m.network_info('/api/network', {}, {})
        chk('API /api/network peers_known = real address book size', body['data']['peers_known'] == node2.addr_book.size(), body['data'])
        import urllib.request, urllib.error
        srv = m.NEBULAAPIServer(host='127.0.0.1', port=18781, ws_port=18782)
        with QUIET():
            srv.start()
        time.sleep(0.5)
        try:
            r = urllib.request.urlopen('http://127.0.0.1:18781/api/fees?target=3&size=300', timeout=10)
            hb = json.loads(r.read())
            chk('HTTP GET /api/fees -> 200 success', r.status == 200 and hb.get('success')
                and hb['data']['estimate']['target_blocks'] == 3, str(hb)[:140])
        except Exception as ex:
            chk('HTTP GET /api/fees -> 200 success', False, ex)
        try:
            srv.stop()
        except Exception:
            pass
    finally:
        m.STATE.chain, m.STATE.network = old_chain, old_net

except Exception:
    R.append(('UNEXPECTED ERROR', False, traceback.format_exc()[-700:]))

bad = 0
for n, ok, info in R:
    if not ok:
        bad += 1
    print(('PASS  ' if ok else 'FAIL  ') + n + ('' if ok or not info else '   -> ' + info))
print(f"\n{len(R) - bad}/{len(R)} passed")
sys.exit(1 if bad else 0)
