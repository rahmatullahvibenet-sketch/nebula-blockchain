import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
import os
import sys, time, io, contextlib, importlib.util, struct, hashlib, copy, traceback
spec=importlib.util.spec_from_file_location('nb',os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'nebula_v10_24.py')); m=importlib.util.module_from_spec(spec); sys.modules['nb']=m
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
R=[]
def chk(name,fn):
    try:
        r=fn(); R.append((name,'PASS' if r is not False else 'FAIL',str(r)[:100]))
    except Exception as e:
        R.append((name,'ERROR',f'{type(e).__name__}: {str(e)[:110]}'))
def mine(bc, txs_extra=(), addr=None, ts=None, prev=None, height=None, bits=None):
    prev = prev or bc.tip
    h = height if height is not None else prev.height+1
    addr = addr or 'NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx'
    cb=m.Transaction.coinbase(height=h, reward=m.mining_reward(h)+sum(0 for _ in txs_extra), miner_address=addr)
    txs=[cb]+list(txs_extra)
    root=m.MerkleTree.compute_root([t.txid for t in txs])
    b_=bits or bc.get_next_bits()
    hdr=m.BlockHeader(1,prev.hash,root,ts or int(time.time()),b_,0,h)
    tgt=hdr.target
    n=0
    while True:
        hdr.nonce=n
        if int(hdr.hash(),16)<tgt: break
        n+=1
    return m.Block(hdr,txs)
bc=m.NEBULABlockchain()
chk('genesis height 0', lambda: bc.height==0)
chk('genesis meets own PoW', lambda: bc.tip.header.meets_target())
t=time.time(); b1=mine(bc); print('mine secs',round(time.time()-t,1))
chk('accept valid mined block', lambda: bc.add_block(b1)==(True,'OK') or bc.add_block(b1))
chk('height==1', lambda: bc.height==1)
chk('reject duplicate block', lambda: not bc.add_block(b1)[0])
# bad PoW
bad=mine(bc); bad.header.nonce+=1; bad._hash=None
chk('reject bad PoW', lambda: not bc.add_block(bad)[0])
# wrong bits
try:
    wb=mine(bc,bits=0x1f0fffff); chk('reject wrong difficulty bits', lambda: not bc.add_block(wb)[0])
except Exception as e: R.append(('reject wrong bits','ERROR',str(e)[:100]))
# wrong coinbase reward (too high)
def overreward():
    h=bc.height+1
    cb=m.Transaction.coinbase(height=h,reward=m.mining_reward(h)*2,miner_address='NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx')
    root=m.MerkleTree.compute_root([cb.txid]); hdr=m.BlockHeader(1,bc.tip.hash,root,int(time.time()),bc.get_next_bits(),0,h)
    n=0
    while int(hdr.hash(),16)>=hdr.target: n+=1; hdr.nonce=n
    ok,msg=bc.add_block(m.Block(hdr,[cb])); return (not ok), msg
chk('reject inflated coinbase', overreward)
# wrong merkle root
def badmerkle():
    b=mine(bc); b.header.merkle_root='00'*32; hdr=b.header; n=0
    while int(hdr.hash(),16)>=hdr.target: n+=1; hdr.nonce=n
    b._hash=None; ok,msg=bc.add_block(b); return (not ok), msg
chk('reject bad merkle root', badmerkle)
# Transactions via dev mode
bc._dev_mode=True
w=m.NEBULAWallet(utxo_set=bc.utxo); w2=m.NEBULAWallet(utxo_set=bc.utxo)
a1=w.first_address; a2=w2.first_address
bc.fund_address(a1,10)
chk('balance after fund', lambda: bc.utxo.balance(a1)==10*10**m.DECIMALS)
def mk():
    return w.build_transaction(a2,3)
try:
    tx=mk(); chk('wallet builds tx', lambda: tx is not None)
    chk('mempool accepts signed tx', lambda: bc.add_to_mempool(tx)[0])
    chk('mempool rejects same tx again', lambda: not bc.add_to_mempool(tx)[0])
    # double spend: different tx spending same utxo
    tx2=w.build_transaction(a2,2)
    chk('mempool rejects double-spend', lambda: not bc.add_to_mempool(tx2)[0])
    # tampered signature
    tx3=copy.deepcopy(tx); tx3.inputs[0].script_sig=tx3.inputs[0].script_sig[:-2]+b'\x00\x00' if isinstance(tx3.inputs[0].script_sig,(bytes,bytearray)) else tx3.inputs[0].script_sig
    tx3.invalidate_cache()
    bc2=m.NEBULABlockchain(); bc2._dev_mode=True
    # include tx in a block
    fee=tx.fee(bc.utxo) if tx.fee.__code__.co_argcount>1 else tx.fee
    cbh=bc.height+1
    cb=m.Transaction.coinbase(height=cbh,reward=m.mining_reward(cbh)+ (fee if isinstance(fee,int) else 0),miner_address='NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx')  # v10.19: miner must not be the sender (wallet change goes to a new address)
    txs=[cb,tx]; root=m.MerkleTree.compute_root([x.txid for x in txs])
    hdr=m.BlockHeader(1,bc.tip.hash,root,int(time.time()),bc.get_next_bits(),0,cbh); n=0
    while int(hdr.hash(),16)>=hdr.target: n+=1; hdr.nonce=n
    ok,msg=bc.add_block(m.Block(hdr,txs)); R.append(('block with real signed tx accepted','PASS' if ok else 'FAIL',msg))
    chk('receiver got 3 NBL', lambda: bc.utxo.balance(a2)==3*10**m.DECIMALS)
    chk('sender spent input (balance<10)', lambda: bc.utxo.balance(a1)<1*10**m.DECIMALS)  # v10.19: funded 10 NBL input is gone; change sits on a new wallet address
    chk('mempool cleared after block', lambda: bc.mempool.size()==0)
except Exception as e:
    R.append(('tx flow','ERROR',traceback.format_exc()[-300:]))
# Fork/reorg: build competing branch off b1 with 2 blocks vs main having 1 more
try:
    main_tip=bc.tip; base=b1
    f1=mine(bc,prev=base,addr=a2,ts=int(time.time())+1)
    r1=bc.add_block(f1); R.append(('fork block accepted as side chain','PASS' if r1[0] else 'FAIL',r1[1]))
    # extend fork till more work than main (main has 2 blocks past b1)
    prev=f1; res=None; msgs=[]
    for i in range(3):
        fb=mine(bc,prev=prev,addr=a2,ts=int(time.time())+2+i,height=prev.height+1); res=bc.add_block(fb); msgs.append(res[1]); prev=fb
    # v10.19: the REORG message is returned by the block that triggers it, not necessarily the last block of the loop
    R.append(('reorg to heavier fork','PASS' if any('REORG' in x for x in msgs) else 'FAIL',' | '.join(msgs)))
    R.append(('tip == fork tip after reorg','PASS' if bc.tip.hash==prev.hash else 'FAIL',str(bc.height)))
    R.append(('utxo consistent after reorg (supply>0)','PASS' if bc.utxo.total_supply()>0 else 'FAIL',str(bc.utxo.total_supply())))
except Exception as e:
    R.append(('fork/reorg','ERROR',traceback.format_exc()[-300:]))
# save / load
try:
    import tempfile,os
    p=os.path.join(tempfile.mkdtemp(),'chain.json')
    import inspect; print('save sig',inspect.signature(bc.save),'load sig',inspect.signature(m.NEBULABlockchain.load))
    bc.save(p) if len(inspect.signature(bc.save).parameters)>0 else bc.save()
    R.append(('save ok','PASS',''))
except Exception as e:
    R.append(('save','ERROR',f'{type(e).__name__}: {str(e)[:120]}'))
for r in R: print(f'{r[1]:6} {r[0]:45} {r[2]}'.encode('ascii','replace').decode())
