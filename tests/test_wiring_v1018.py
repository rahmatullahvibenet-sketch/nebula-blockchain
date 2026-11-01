import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
"""python3 tests/test_wiring_v1018.py   - group 5 on a REAL NEBULAFullNode (built into nebula_v10_24.py)"""
import sys, os, io, time, tempfile, contextlib, importlib.util
os.environ.setdefault('NEBULA_ALLOW_DEV_MODE', '1')
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('nb', os.path.join(os.path.dirname(HERE), 'nebula_v10_24.py'))
m = importlib.util.module_from_spec(spec); sys.modules['nb'] = m
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    spec.loader.exec_module(m)
R = []
def chk(n, c): R.append(bool(c)); print(('PASS ' if c else 'FAIL ') + n)
Q = lambda: contextlib.redirect_stdout(io.StringIO())

# the 20 classes: exactly one definition each, and all are in the module
C20 = ("SegWitBlockValidator BlockUtils SparseMerkleTree PatriciaTrie TransactionUtils WalletHistory WalletLabelManager "
       "TimeOracle PeerSyncManager PeerDiscoveryEngine AddrRelayManager SmartMessageRouter StakingRewardsCalculator "
       "PriceFeedAggregator WatchOnlyWalletAdv MempoolUtils CoinControlAdv StateAccumulator ContractStorageAdv "
       "ExtraNonceManager").split()
import ast
t = ast.parse(open(spec.origin, encoding='utf-8').read())
for c in C20:
    n = sum(1 for x in ast.walk(t) if isinstance(x, ast.ClassDef) and x.name == c)
    chk('one definition of ' + c, n == 1 and hasattr(m, c))

with Q(): node = m.NEBULAFullNode(data_dir=tempfile.mkdtemp(), port=0, mine=False)
chk('no group5 attach error', node.group5_error is None)
chk('groups 1-4 still attached', node.groups is not None and node.groups.g1 is not None and node.groups.g4 is not None)
chk('node.group5 + group5_net + group5_extra exist', all(hasattr(node, a) for a in ('group5', 'group5_net', 'group5_extra', 'group5_api')))
chk('p2p wrapped by Group5Net', getattr(node.p2p, '_group5_net', None) is node.group5_net)
chk('chain listeners attached', node.group5 in node.bc._listeners and node.group5_extra in node.bc._listeners)
chk('weight limit = host consensus', node.group5.max_block_weight == 4 * m.MAX_BLOCK_SIZE_BYTES)
for p in ('/api/group5', '/api/group5/staking', '/api/group5/price', '/api/group5/watch', '/api/group5/mempool',
          '/api/group5/storage', '/api/group5/accumulator'):
    chk('REST route ' + p, p in m._routes['GET'])
m.STATE.chain = node.bc
s, d = m._routes['GET']['/api/group5']('/api/group5', {}, None)
chk('REST /api/group5 returns layer+net', s == 200 and 'layer' in d['data'] and 'net' in d['data'])

# real mined blocks through BOTH the old live layers and group 5
node.bc._dev_mode = True
user = m.NEBULAWallet(utxo_set=node.bc.utxo); a = user.first_address
node.group5.watch(a, 'test-wallet')
MINER = a
_ts = [int(time.time()) - 100000]
def solve(h):
    h.nonce = 0
    while not h.meets_target(): h.nonce += 1
def mk(bc):
    prev = bc.tip; h = prev.height + 1
    cb = m.Transaction.coinbase(height=h, reward=m.mining_reward(h), miner_address=MINER)
    root = m.MerkleTree.compute_root([cb.txid]); _ts[0] = max(_ts[0] + 1, prev.header.timestamp + 1)
    hd = m.BlockHeader(1, prev.hash, root, _ts[0], bc.get_next_bits(), 0, h); solve(hd); return m.Block(hd, [cb])
h0 = node.bc.height
with Q():
    for _ in range(3):
        okb, msg = node.bc.add_block(mk(node.bc)); assert okb, msg
chk('3 real blocks mined and accepted', node.bc.height == h0 + 3)
node.group5_extra.flush()
st = node.group5.stats()
chk('group5 layer follows the chain height', st['height'] == node.bc._chain[-1].height == h0 + 3)
chk('watched wallet saw the 3 rewards', st['wallet_hits'] >= 3 and st['received'] > 0)
chk('accumulator + kv saw every tx', node.group5_extra.stats()['elements'] >= 3 and node.group5_extra.stats()['acc_height'] == h0 + 3)
chk('smt/trie roots present', len(st['smt_root']) == 64 and len(st['trie_root']) == 64)
chk('tip stored in key-value store', node.group5_extra.kv.get('tip') == node.bc._chain[-1].hash)
chk('layer not stale, no group errors', not st['stale'] and not node.groups.errors)
s, d = m._routes['GET']['/api/group5/accumulator']('/x', {}, None)
chk('REST /accumulator 200', s == 200 and d['data']['elements'] >= 1)
s, d = m._routes['GET']['/api/group5/storage']('/x', {'key': ['tip']}, None)
chk('REST /storage tip 200', s == 200)
chk('group5_net no errors', node.group5_net.errors == 0)

with Q(): srv = m.StratumV1Server(node.bc, port=0)
chk('every Stratum server gets Group5Pool', hasattr(srv, 'group5_pool') and not getattr(srv, 'group5_error', None))

with Q(): node.stop()
chk('stop(): group5 net restored', getattr(node.p2p, '_group5_net', None) is None)
chk('stop(): listeners removed', node.group5 not in node.bc._listeners and node.group5_extra not in node.bc._listeners)
print('%d/%d' % (sum(R), len(R))); sys.exit(0 if all(R) else 1)
