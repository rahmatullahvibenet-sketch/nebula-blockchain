import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
import os
import sys, io, contextlib, importlib.util, traceback, signal
spec=importlib.util.spec_from_file_location('nb',os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'nebula_v10_24.py')); m=importlib.util.module_from_spec(spec); sys.modules['nb']=m
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
R=[]
def T(name,fn):
    try:
        with contextlib.redirect_stdout(io.StringIO()): r=fn()
        R.append((name,'PASS' if r is not False else 'FAIL',repr(r)[:110]))
    except BaseException as e:
        tb=traceback.extract_tb(e.__traceback__)[-1]
        R.append((name,'ERROR',f'{type(e).__name__}: {str(e)[:90]} @{tb.name}:{tb.lineno}'))
bc=m.NEBULABlockchain(); bc._dev_mode=True
w=m.NEBULAWallet(utxo_set=bc.utxo); a=w.first_address; b=m.NEBULAWallet(utxo_set=bc.utxo).first_address
bc.fund_address(a,50)
import random
T('NFTGamingV2.mint_random_item', lambda: m.NFTGamingV2(bc,m.OnChainRNG(bc)).mint_random_item(a).rarity)
# TxBatcher
def batch():
    tb=m.TxBatcher(w,bc); tb.add_payment(b,2*10**8); tb.add_payment(b,1*10**8)
    tx=tb.build(a); ok=bc.add_to_mempool(tx) if tx else None; return tx is not None, ok
T('TxBatcher.build -> mempool accepts', batch)
# FeeBumper RBF
def rbf():
    bc2=m.NEBULABlockchain(); bc2._dev_mode=True
    w2=m.NEBULAWallet(utxo_set=bc2.utxo); a2=w2.first_address; bc2.fund_address(a2,50)
    b2=m.NEBULAWallet(utxo_set=bc2.utxo).first_address
    tx=w2.build_transaction(b2,5,fee_nbl=0.0001); r=bc2.add_to_mempool(tx)
    priv=w2._keys[a2].key
    nb=m.FeeBumper(bc2).rbf_bump(tx.txid,priv,50,change_address=w2.change_address(0))
    bc2.mempool.remove(tx.txid) if hasattr(bc2.mempool,'remove') else None
    return r, nb is not None, (bc2.add_to_mempool(nb) if nb else None), (nb.fee(bc2.utxo)>tx.fee(bc2.utxo)) if nb else None
T('FeeBumper.rbf_bump', rbf)
# MobileSDK send with memo: must not duplicate outputs
def sdk():
    sd=m.MobileSDK(bc); import inspect; return str(inspect.signature(sd.send))+' '+str([n for n in dir(sd) if not n.startswith('_')])
T('MobileSDK api', sdk)
# BanManager save/load roundtrip
def ban():
    import tempfile,os
    bm=m.BanManager(); bm.ban('9.9.9.9',1,'spam'); p=os.path.join(tempfile.mkdtemp(),'b.json'); bm.save(p)
    b2=m.BanManager(); n=b2.load(p); return n, len(b2.banlist()), b2.is_banned('9.9.9.9')
T('BanManager save/load/banlist', ban)
def ins():
    d=m.DeFiInsurance(bc); d.deposit_capital(a,40.0); return d.buy_policy(a,'smart_contract','dex',10.0,30)
T('DeFiInsurance deposit+buy', ins)
for r in R: print(f'{r[1]:7} {r[0]:40} {r[2]}'.encode('ascii','replace').decode())
def sdkmemo():
    sd=m.MobileSDK(bc)
    import inspect
    src=inspect.getsource(m.MobileSDK.send); return 'memo' in src
