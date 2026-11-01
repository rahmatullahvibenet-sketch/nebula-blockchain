import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
import os
import sys, time, io, contextlib, importlib.util, traceback, signal, inspect
spec=importlib.util.spec_from_file_location('nb',os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'nebula_v10_24.py')); m=importlib.util.module_from_spec(spec); sys.modules['nb']=m
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
bc=m.NEBULABlockchain(); bc._dev_mode=True
A='NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx'
def mk(c,*a,**k):
    return getattr(m,c)(*a,**k)
R=[]
class TO(Exception): pass
signal.signal(signal.SIGALRM,lambda s,f:(_ for _ in ()).throw(TO()))
def T(name,fn):
    signal.alarm(90)
    try:
        with contextlib.redirect_stdout(io.StringIO()): r=fn()
        R.append((name,'PASS' if r is not False else 'FAIL',repr(r)[:90]))
    except TO: R.append((name,'TIMEOUT',''))
    except BaseException as e:
        R.append((name,'ERROR',f'{type(e).__name__}: {str(e)[:100]} @ '+traceback.extract_tb(e.__traceback__)[-1].name+':'+str(traceback.extract_tb(e.__traceback__)[-1].lineno)))
    finally: signal.alarm(0)
T('MultiAccountWallet.get_address', lambda: (lambda w:(w.get_address(0), w.get_segwit_address(0), w.get_taproot_address(1)))(m.MultiAccountWallet.from_mnemonic(m.BIP39.generate_mnemonic(12))))
T('GovernanceSystem.create_proposal', lambda: (lambda g:g.create_proposal('t','d',A,'max_block_size','2000000'))(mk('GovernanceSystem',bc)))
def ev20():
    t=mk('NBL20TokenAdv',*[]) if False else None
T('NBL20TokenAdv._emit', lambda: (lambda t:(t._emit('Transfer',[A,5],1),len(t._events)))(m.NBL20TokenAdv('T','T',8,1000,A)))
T('NBL721Token._emit', lambda: (lambda t:(t._emit('Transfer',[A,5],1),len(t._events)))(m.NBL721Token('N','N','ipfs://',A)))
def tok(cls):
    try: sig=inspect.signature(cls); 
    except: sig=None
    return sig
print('sigs', tok(m.NBL20TokenAdv), tok(m.NBL721Token), file=sys.stderr)
T('NEBULADex.book+pool', lambda: (lambda d:(d.get_or_create_book('NBL','USDT'),d.create_pool('NBL','USDT')))(mk('NEBULADex',bc)))
def dexpool():
    d=mk('NEBULADex',bc); pid=d.create_pool('NBL','USDT'); return d.add_liquidity(A,'NBL','USDT',1000000,2000000)
T('NEBULADex.add_liquidity', dexpool)
T('NBL721Registry.create_collection', lambda: (lambda r:r.create_collection(A,'Art','ART','d',100,0.05))(mk('NBL721Registry')))
T('MicroPaymentNetwork open/pay/close', lambda: (lambda n:(lambda ok,cid:(n.pay(cid,'a',500),n.cooperative_close(cid),n.channel_stats()))(*n.open_channel('a','b',10_000,5_000)))(mk('MicroPaymentNetwork',bc)))
T('PeerAddressBook.add/get_random', lambda: (lambda b:(b.add('1.2.3.4',8333,1),b.get_random(3),b._evict()))(mk('PeerAddressBook')))
def sc():
    c=m.StateChannel('c1',['a','b'],{'a':10,'b':5}); k=12345
    st=c.propose_state('a',{'n':1},{'a':9,'b':6},k); ok=c.countersign(st,'b',k); fin=c.close(k,'a'); return ok, c.channel_info()['round'], fin.final
T('StateChannel flow', sc)
T('WalletConnectBridge.create_session', lambda: (lambda b:b.create_session('dapp','https://x',A))(mk('WalletConnectBridge')))
T('SubscriptionManager.create', lambda: (lambda s:s.create(A,'merchant',1.0,30))(mk('SubscriptionManager',bc)))
T('TokenLaunchpad.create_project', lambda: (lambda l:l.create_project(A,'Tok','TK',1_000_000,0.5,0.01,100,1000,30))(mk('TokenLaunchpad',bc)))
T('DeFiInsurance.buy_policy', lambda: (lambda d:d.buy_policy(A,'smart_contract','dex',10.0,30))(mk('DeFiInsurance',bc)))
T('OracleV2.update_price', lambda: (lambda o:(o.update_price('NBL/USD',1.5,'rep'),o.price('NBL/USD')))(mk('OracleV2',bc)))
T('SlashingConditionsEngine.submit_evidence', lambda: (lambda s:s.submit_evidence('rep','val',list(m.SlashingCondition)[0],{'h':1}))(mk('SlashingConditionsEngine',bc)))
T('EventLog.emit', lambda: (lambda e:e.emit('c1','Transfer',['t'],{'a':1}))(mk('EventLog',bc)))
def adv():
    p=mk('AdvancedStakingPlatform',bc); bc.fund_address(A,100000)
    s=p.stake(A,'30day',500.0); u1=p.unstake(A,'30day'); r=p.process_rewards(); return s,u1,r,p.user_positions(A)
T('AdvancedStakingPlatform stake/unstake', adv)
T('ProtocolUpgradeManager.propose_upgrade', lambda: (lambda p:p.propose_upgrade(A,'segwit2','d','1.0','BIP-X'))(mk('ProtocolUpgradeManager',bc)))
T('AuditTrail.log/query', lambda: (lambda a:(a.log('login',A,'x',{}),a.query()))(mk('AuditTrail',bc)))
import random
T('NFTGamingV2.mint_random_item', lambda: (lambda g:g.mint_random_item(A))(mk('NFTGamingV2',bc,m.OnChainRNG(bc))))
def ban():
    b=mk('BanManager'); r=b._do_ban('1.2.3.4',1,'spam'); return r.is_expired if hasattr(r,'is_expired') else r
T('BanManager._do_ban', ban)
for r in R: print(f'{r[1]:7} {r[0]:44} {r[2]}'.encode('ascii','replace').decode())
