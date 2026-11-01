import os as _o; _o.environ.setdefault("NEBULA_NETWORK","regtest")  # v10.24: tests mine blocks, so they use the regtest difficulty
import os; os.environ.setdefault('NEBULA_ALLOW_DEV_MODE','1')
import sys, inspect, time, importlib.util, io, contextlib, signal, json, traceback
spec=importlib.util.spec_from_file_location('nb',os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'nebula_v10_24.py')); m=importlib.util.module_from_spec(spec)
sys.modules['nb']=m
t=time.time()
buf=io.StringIO()
with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
    spec.loader.exec_module(m)
print('import secs',round(time.time()-t,1))
classes=[(n,c) for n,c in vars(m).items() if inspect.isclass(c) and c.__module__=='nb']
print('classes',len(classes))
class TO(Exception): pass
def h(s,f): raise TO()
signal.signal(signal.SIGALRM,h)
res={'ok':[], 'needs_args':[], 'crash':[], 'timeout':[], 'abstract_or_enum':[]}
import enum, abc
for n,c in classes:
    if issubclass(c,enum.Enum) or issubclass(c,BaseException) or inspect.isabstract(c):
        res['abstract_or_enum'].append(n); continue
    try:
        sig=inspect.signature(c)
    except Exception: sig=None
    req=[p for p in (sig.parameters.values() if sig else []) if p.default is p.empty and p.kind in (p.POSITIONAL_OR_KEYWORD,p.POSITIONAL_ONLY,p.KEYWORD_ONLY)]
    if req:
        res['needs_args'].append((n,[p.name for p in req])); continue
    signal.alarm(8)
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            c()
        res['ok'].append(n)
    except TO: res['timeout'].append(n)
    except BaseException as e: res['crash'].append((n,type(e).__name__,str(e)[:90]))
    finally: signal.alarm(0)
for k,v in res.items(): print(k,len(v))
json.dump(res,open('scan.json','w'),default=str)
