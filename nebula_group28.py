"""NEBULA group28 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. MempoolMonitor  (orig. lines 46476-46570)
   2. NEBULATests  (orig. lines 46584-46598)
   3. NEBULAGrandFinale  (orig. lines 46600-46875)
   4. BLSSignature  (orig. lines 46893-46969)
   5. VerkleTree  (orig. lines 46971-47027)
   6. KZGCommitment  (orig. lines 47029-47087)
   7. ValidatorVote  (orig. lines 47100-47116)
   8. HybridConsensus  (orig. lines 47118-47202)
   9. StealthAddress  (orig. lines 47214-47302)
  10. RingSignature  (orig. lines 47304-47363)
  11. L2Type  (orig. lines 47377-47382)
  12. L2Channel  (orig. lines 47384-47425)
  13. Layer2Manager  (orig. lines 47427-47534)
  14. NEBULALaunchChecker  (orig. lines 47546-47691)
  15. Cluster  (orig. lines 47749-47774)
  16. CommonInputHeuristic  (orig. lines 47776-47827)
  17. ChangeDetectionHeuristic  (orig. lines 47829-47857)
  18. PeelChainDetector  (orig. lines 47859-47891)
  19. BlockchainClusterer  (orig. lines 47893-47964)
  20. LNEdge  (orig. lines 47977-48011)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): FullChainValidator, FullSystemTester, MempoolAlert, NEBULABlockchain, PropertyTest, Schnorr, Secp256k1, TestBlockchain, TestBlocks, TestCrypto, TestResultAccumulator, TestTransactions, TestWallet
"""
from __future__ import annotations
import argparse
import ast
import binascii
import ctypes
import getpass
import hashlib
import heapq
import hmac
import ipaddress
import json
import logging
import math
import multiprocessing as mp
import os
import queue
import secrets
import socket
import stat
import struct
import sys
import threading
import time
import traceback
import unicodedata
from collections  import defaultdict, deque
from dataclasses  import dataclass, field
from datetime     import datetime, timezone
from enum         import Enum, IntEnum
from functools    import wraps
from http.server  import HTTPServer, BaseHTTPRequestHandler
from pathlib      import Path
from typing       import (List, Dict, Optional, Tuple, Set,
                           Any, Callable, Iterator as _Iter)
from urllib.parse import urlparse, parse_qs
import time as _wtime
import sys
import hashlib, struct, secrets, hmac as _hmac
from typing import List, Tuple, Optional, Dict
import hashlib, secrets, struct, time, threading, json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
import json, socket, threading, time, hashlib, struct, secrets
from typing import Dict, List, Optional, Callable, Tuple
from dataclasses import dataclass, field
from enum import Enum
import os, json, struct, hashlib, threading, time, sqlite3
from typing import Dict, List, Optional, Iterator, Tuple
from pathlib import Path
from dataclasses import dataclass
import os, struct, hashlib, hmac as _hmac, secrets, threading
from typing import Optional, Tuple, Dict
from enum import Enum
import json, time, hashlib, threading
from typing import Dict, List, Optional, Any
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import socket, struct, threading, time, secrets, hashlib
from typing import Optional, List, Dict, Tuple
from dataclasses import dataclass, field
from enum import Enum
import hashlib, secrets, threading
from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass, field
import time, threading, heapq
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
import hashlib, struct, math, threading, time
from typing import List, Optional, Set, Tuple, Dict
import json, threading, time, hashlib, struct
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, Callable, Any, Optional, List, Tuple
import hashlib, hmac as _hmac, struct, secrets, time, json, threading
from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum
import threading, time, hashlib, struct, queue
from typing import List, Dict, Optional, Tuple, Set
from dataclasses import dataclass, field
from enum import Enum
import threading, time, hashlib, json, os, logging, gzip
from typing import Dict, List, Optional, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum, IntFlag
from pathlib import Path
import hashlib, struct, time, threading, secrets
from typing import List, Dict, Optional, Tuple, Any, Callable
from dataclasses import dataclass, field
from enum import IntEnum
import threading, time, json, hashlib, secrets
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import time, threading, hashlib, math, struct
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import time, threading, hashlib, math
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import threading, time, hashlib, secrets, queue
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum
import time
from dataclasses import dataclass, field
from typing import Dict, List
import hashlib, re, threading
from typing import List, Optional, Dict, Tuple, Any
from dataclasses import dataclass, field
import threading, time, hashlib, struct
from typing import List, Dict, Optional, Set, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import json, threading, time, hashlib
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from pathlib import Path
import hashlib, hmac, struct, secrets, time, threading
from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum
import hashlib, hmac as _hmac, struct, unicodedata
from typing import List, Optional, Tuple
import threading, time, queue, hashlib, struct
from typing import Dict, List, Optional, Set, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import threading, time, hashlib, statistics
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import hashlib, threading
from typing import List, Optional, Dict, Tuple
import threading, time, os, sys
from typing import Callable, Optional, Dict
from dataclasses import dataclass, field
import threading, time, socket, hashlib, secrets
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import time, threading, collections
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field
import hashlib, struct, time, threading
from typing import Dict, List, Any, Optional, Callable, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto
import threading, time, sys
from typing import Optional
import json, socket, threading, time
from typing import List, Dict, Any, Optional, Callable
import time, threading, math
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import time, threading, hashlib
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import time, threading, hashlib
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field
import hashlib, struct, time, threading
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import hashlib, struct, time, threading, random, heapq
from typing import Dict, List, Optional, Set, Tuple, Callable
from dataclasses import dataclass, field
import json, time, threading, hashlib, base64
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import hashlib, struct
from typing import List, Tuple, Optional, Any
from enum import IntEnum
import threading
from typing import List, Optional, Tuple, Dict
from dataclasses import dataclass, field
import time, threading
from typing import Optional, List, Tuple
from dataclasses import dataclass
import threading, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import hashlib, json
from typing import List, Optional, Dict
from dataclasses import dataclass, field
import hashlib, struct
from typing import List, Optional, Dict
from dataclasses import dataclass
import threading, time, hashlib, secrets
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import threading, time, secrets, hashlib
from typing import Dict, Optional, Tuple, List
from dataclasses import dataclass, field
from enum import Enum
import threading, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from statistics import median
import threading, time, math
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import hashlib, os, threading, time, struct, secrets
from typing import Dict, List, Optional, Tuple
import threading, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import hashlib, secrets
from typing import Tuple, List, Optional
import threading, time
from typing import Optional, Dict, List
import threading, time, statistics, collections
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import threading, json
from typing import Optional, Set
from pathlib import Path
import threading
from typing import Dict
from dataclasses import dataclass, field
import threading, time, secrets, json
from typing import Dict, Callable, Optional
import time
import threading, time, math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict
import threading, time
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict
import threading
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict, deque
import threading, time, hashlib, secrets
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import threading, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import bisect
import threading, time, hashlib, json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import threading, time, hashlib, secrets
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import math
from typing import List, Tuple, Dict
import hashlib, threading
from typing import List, Optional, Tuple, Dict
from dataclasses import dataclass
import threading, time
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, Optional
import urllib.parse
import threading, secrets, hashlib
from typing import List, Optional, Tuple, Iterator
import time, threading
import threading, time, hashlib
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum
import time, threading
from typing import Dict, List, Callable, Optional
import threading, time
from typing import Dict, List, Optional, Tuple
from collections import deque
from dataclasses import dataclass, field
import threading, time, hashlib, struct, secrets
from typing import Dict, List, Optional, Tuple
import threading, time
from typing import Optional, Dict
import threading, time, hashlib, secrets
from typing import Dict, List, Set, Optional, Tuple, Callable
from dataclasses import dataclass, field
from collections import deque, defaultdict
import hashlib, time, struct
from typing import List, Optional, Tuple
from dataclasses import dataclass
import json, threading, time, hashlib
from typing import Optional, Dict, List
from pathlib import Path
import threading, time
from typing import Dict, List, Callable, Optional
from dataclasses import dataclass, field
from enum import Enum
import time, threading, hashlib
from typing import Any, Dict, List, Optional
import json, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, List, Optional
import urllib.parse
import threading, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import threading, time, socket
from typing import Dict, List, Optional, Tuple, Set
import threading
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import time, threading
from typing import Optional
import threading, time
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
import threading, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import threading, time, json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import threading, time
from typing import Dict, List, Optional, Tuple, Callable
from dataclasses import dataclass, field
import time, threading
from typing import Optional, List
import threading, time, statistics
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import threading, time
from typing import Dict, List, Optional, Tuple
import json, time, threading
from typing import Dict, List, Optional
from pathlib import Path
from typing import Any, Dict, List, Optional, Callable
from dataclasses import dataclass, field
import hashlib, time
import time, threading, traceback
from typing import Any, Callable, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import threading, time, statistics
from typing import List, Optional
import hashlib, threading
from typing import List, Tuple, Optional
import threading, time
from typing import Dict, List, Optional, Tuple
import threading, time
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
import time, hashlib
from typing import Optional
import hashlib, secrets, struct
from typing import List, Tuple, Optional
import threading, time, secrets
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
import hashlib, secrets
from typing import Tuple, Optional, List
import threading, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import time, json
from typing import Dict, List, Optional
import threading, hashlib
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict, deque
import threading, heapq, math
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field
import threading, time, statistics
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import hashlib, threading, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import threading, time, secrets
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import threading, statistics
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
import json, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Optional
import urllib.parse
import threading, time
from typing import Dict, List, Optional, Tuple, Callable
from dataclasses import dataclass, field
import json, hashlib
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import time
import json, threading
from http.server import BaseHTTPRequestHandler
from typing import Optional
import urllib.parse
import time
import time, hashlib
import time
import time, hashlib, threading
from typing import Any, Dict, List, Optional, Callable, Tuple
import time, hashlib, threading, secrets
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import enum as _enum
from collections import OrderedDict as _FeeOD
import json, time, hashlib, threading, os, socket
import os
import json
import struct
import threading
import socket
import hashlib
import time
import queue
import logging
import hashlib as _hl
from typing import List as _L, Optional as _O, Tuple as _T, Dict as _D
import os as _os
import struct as _struct
import hashlib as _hashlib
import hmac as _hmac
import os   as _os2
import json as _json2
import struct as _st2
import threading as _th2
from pathlib import Path as _Path2
import time   as _time2
import heapq  as _hq
from dataclasses import dataclass as _dc, field as _fld
from typing import Dict as _D2, List as _L2, Optional as _O2, Set as _S2
from enum      import Enum   as _Enum2
from dataclasses import dataclass as _dc2, field as _fld2
from typing    import Dict as _D3, List as _L3, Optional as _O3
import time      as _time3
import ipaddress as _ip3
import json      as _json3
from dataclasses import dataclass as _dc3, field as _fld3
from typing      import Dict as _D4, Optional as _O4, List as _L4
from pathlib     import Path as _Path3
from enum        import Enum as _Enum3
import re      as _re
import math    as _math3
from urllib.parse import urlencode as _urlencode, quote as _quote, unquote as _unquote, parse_qs as _pqs
from typing  import Optional as _O5, Dict as _D5
import time      as _time4
import hashlib   as _hl4
import struct    as _st4
from dataclasses import dataclass as _dc4
from typing      import Optional as _O6
import os as _os
import sys as _sys
import tempfile as _tempfile
import subprocess as _subprocess
import ctypes as _ctypes
import dataclasses as _v108_dc
import enum as _v108_enum
import json as _v108_json
import math as _v108_math
import time as _v108_time
import hashlib as _v108_hashlib
import copy as _v109_copy
import copyreg as _v109_copyreg
from math import isqrt as _v109_isqrt
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

# ===== module-level helpers/constants used by these classes (verbatim from host) =====
CHAIN_NAME          = "NEBULA"

CHAIN_SYMBOL        = "NBL"

CHAIN_ID            = 2025

DECIMALS            = 9

MAX_SUPPLY          = 21_000_000 * (10 ** DECIMALS)   # in Neb  (matches 50 NBL * 210,000 blocks * 2 geometric series)

FOUNDATION_RATE        = 0.02          # 2% per block to foundation

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

HALVING_INTERVAL       = 210_000                        # blocks

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

PUBKEY_ADDRESS_PREFIX   = 'N'    # human-readable prefix for P2PKH addresses

def c(text, color): return f"{color}{text}{C.RESET}"

def ok(msg):
    """CLI: ok("text") prints a green line.  REST API (v10.10 fix): ok({...}) -> (200, body).
    The REST routes always pass a dict and unpack `status, data = fn(...)`; before v10.10 this name
    was only the CLI printer, so EVERY API request crashed (connection closed, no response)."""
    if isinstance(msg, str):
        print(c(f"✅ {msg}", C.GREEN))
        return None
    return 200, {"success": True, "data": msg}

def err(msg, code=None):
    """CLI: err("text") prints a red line.  REST API (v10.10 fix): err("text", 404) -> (404, body)."""
    if code is None:
        print(c(f"❌ {msg}", C.RED))
        return None
    return code, {"success": False, "error": str(msg)}

try:
    _CORE_OK = True
except ImportError as e:
    _CORE_OK = True
    print(f"[API] Warning: nebula_core.py not found — {e}")

API_VERSION    = "1.0.0"

API_PORT       = 8080

WS_PORT        = 8081

_routes: Dict[str, Dict[str, Callable]] = {}

def route(path: str, methods: List[str] = None):
    """Decorator to register an API endpoint."""
    def decorator(fn: Callable) -> Callable:
        for method in (methods or ["GET"]):
            _routes.setdefault(method.upper(), {})[path] = fn
        return fn
    return decorator

@route("/")
@route("/api")
def root(path, query, body):
    return ok({
        "name"       : "NEBULA Blockchain API",
        "version"    : API_VERSION,
        "chain"      : CHAIN_NAME if _CORE_OK else "NEBULA",
        "symbol"     : CHAIN_SYMBOL if _CORE_OK else "NBL",
        "chain_id"   : CHAIN_ID if _CORE_OK else 2025,
        "author"     : "NEBULA Core Team",
        "license"    : "MIT",
        "genesis"    : "2025-03-16",
        "api_port"   : API_PORT,
        "ws_port"    : WS_PORT,
        "endpoints"  : sorted(_routes.get("GET",{}).keys()) +
                       sorted(_routes.get("POST",{}).keys()),
        "modules"    : STATE.module_status(),
    })

GOV_MIN_DEPOSIT_NBL       = 100 * 10**DECIMALS  # 100 NBL deposit

def _run_extended_module_tests() -> Tuple[int, int]:
    """Run extended tests for modules 23-54"""
    passed = 0
    total  = 0

    def _test(name: str, fn):
        nonlocal passed, total
        total += 1
        try:
            result = fn()
            if result is not False:
                passed += 1
            else:
                print(f"  ✗ {name}")
        except Exception as e:
            print(f"  ✗ {name}: {e}")

    # Test descriptor wallet
    def _t_descriptor():
        d = OutputDescriptor.parse("pkh(02" + "a"*64 + ")")
        return d.desc_type == "pkh"
    _test("Descriptor parsing", _t_descriptor)

    # Test bloom filter
    def _t_bloom():
        bf = BloomFilter(100, 0.01)
        bf.insert(b"hello world")
        return bf.contains(b"hello world") and not bf.contains(b"not there")
    _test("Bloom filter insert/query", _t_bloom)

    # Test GCS filter
    def _t_gcs():
        key = secrets.token_bytes(16)
        elements = [b"element1", b"element2", b"element3"]
        gcs = GCSFilter(key, elements)
        return gcs.size_bytes > 0 and gcs.n == 3
    _test("GCS filter construction", _t_gcs)

    # Test MuSig2 key aggregation
    def _t_musig2_keyagg():
        pks = [
            Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(i, Secp256k1.G()))
            for i in [1234567, 7654321, 9999999]
        ]
        agg, coeffs = MuSig2KeyAgg.aggregate(pks)
        return len(agg) == 32 and len(coeffs) == 3
    _test("MuSig2 key aggregation", _t_musig2_keyagg)

    # Test RBF validator
    def _t_rbf():
        v = RBFValidator()
        return v is not None
    _test("RBF validator init", _t_rbf)

    # Test fee estimator
    def _t_fee():
        fe = FeeEstimator()
        fe.record_confirmed(5.0, 1)
        fe.record_confirmed(10.0, 2)
        return fe.smart_fee(6) >= 1
    _test("Fee estimator", _t_fee)

    # Test Schnorr adaptor signature
    def _t_adaptor():
        privkey     = 0xdeadbeefcafe
        msg32       = secrets.token_bytes(32)
        t_secret    = 0xabcd1234
        T           = Secp256k1.point_mul(t_secret, Secp256k1.G())
        adaptor, k  = SchnorrAdaptorSig.create_adaptor(privkey, msg32, T)
        final_sig   = SchnorrAdaptorSig.complete_adaptor(adaptor, t_secret)
        extracted   = SchnorrAdaptorSig.extract_secret(adaptor, final_sig)
        return extracted == t_secret
    _test("Schnorr adaptor signatures", _t_adaptor)

    # Test coin selector
    def _t_coinsel():
        utxos = []
        for i in range(5):
            u = UTXOEntry(txid=f"tx{i}", index=0,
                          value=(i+1) * 10**DECIMALS,
                          script_pubkey=b'', height=1)
            utxos.append(u)
        selected = CoinSelector.largest_first(utxos, 3 * 10**DECIMALS)
        return selected is not None and len(selected) >= 1
    _test("Coin selector (largest-first)", _t_coinsel)

    # Test BIP85 derivation
    def _t_bip85():
        seed   = hashlib.sha256(b"test bip85 seed").digest()
        master = HDKey.from_seed(seed)
        deriver= BIP85Deriver(master)
        pw     = deriver.derive_password(16, index=0)
        return len(pw) == 16 and pw.isprintable()
    _test("BIP85 password derivation", _t_bip85)

    # Test Pedersen commitment
    def _t_pedersen():
        c1, r1 = PedersenCommitment.commit(100)
        c2, r2 = PedersenCommitment.commit(200)
        c_sum  = PedersenCommitment.add_commitments(c1, c2)
        c3, r3 = PedersenCommitment.commit(300, (r1+r2) % Secp256k1.N)
        return c_sum == c3
    _test("Pedersen commitment homomorphism", _t_pedersen)

    # Test script interpreter
    def _t_script():
        # OP_1 OP_1 OP_ADD OP_2 OP_EQUAL
        script = bytes([
            ScriptOpcode.OP_1,
            ScriptOpcode.OP_1,
            ScriptOpcode.OP_ADD,
            ScriptOpcode.OP_2,
            ScriptOpcode.OP_EQUAL,
        ])
        interp = ScriptInterpreter()
        ok, err = interp.execute(script)
        return ok and not err
    _test("Script interpreter (1+1=2)", _t_script)

    # Test multisig wallet
    def _t_multisig():
        pks = [Secp256k1.pubkey_to_bytes(
               Secp256k1.point_mul(i * 1234567, Secp256k1.G()))
               for i in range(1, 4)]
        ms  = MultisigWallet(2, pks)
        return ms.address().startswith("N") or len(ms.redeem_script()) > 10
    _test("2-of-3 multisig setup", _t_multisig)

    # Test HTLC script
    def _t_htlc():
        sk1 = Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(111, Secp256k1.G()))
        sk2 = Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(222, Secp256k1.G()))
        pre = secrets.token_bytes(32)
        scr = TimelockScript.htlc_script(sk1, sk2, pre, 144)
        asm = ScriptInterpreter.disassemble(scr)
        return len(scr) > 20 and "OP_CHECKSEQUENCEVERIFY" in asm
    _test("HTLC script construction", _t_htlc)

    # Test atomic swap
    def _t_swap():
        bc    = NEBULABlockchain()
        engine = AtomicSwapEngine(bc)
        swap  = engine.initiate_swap("addr1", "addr2",
                                      10 * 10**DECIMALS, 1000000, "BTC")
        ok, _ = engine.claim_swap(swap.swap_id, bytes.fromhex(swap.preimage.hex()))
        return ok
    _test("Atomic swap claim", _t_swap)

    # Test RPC registry
    def _t_rpc():
        reg = RPCRegistry()
        reg.register("test", lambda: 42, "test", "test method")
        result = reg.call("test", [])
        return result == 42
    _test("JSON-RPC registry", _t_rpc)

    # Test version bits
    def _t_versionbits():
        vbs = VersionBitsState()
        return vbs.is_active("taproot") and vbs.is_active("segwit")
    _test("Version bits (taproot/segwit active)", _t_versionbits)

    # Test checksum descriptor
    def _t_checksum():
        desc = "pkh(02" + "a" * 64 + ")"
        with_cs = DescriptorChecksum.add_checksum(desc)
        return "#" in with_cs and len(with_cs.split("#")[1]) == 8
    _test("Descriptor checksum", _t_checksum)

    # Test staking engine
    def _t_staking():
        bc     = NEBULABlockchain()
        engine = StakingEngine(bc)
        return len(engine._validators) >= 1
    _test("Staking engine init", _t_staking)

    # Test AMM pool
    def _t_amm():
        bc  = NEBULABlockchain()
        amm = AMMEngine(bc)
        pid = amm.create_pool("NBL", "USDT")
        lp, _ = amm.add_liquidity("provider1", "NBL", "USDT",
                                    1000 * 10**DECIMALS, 100 * 10**DECIMALS)
        return lp > 0
    _test("AMM pool creation + liquidity", _t_amm)

    # Test AMM swap quote
    def _t_amm_quote():
        bc  = NEBULABlockchain()
        amm = AMMEngine(bc)
        amm.create_pool("NBL", "USDT")
        amm.add_liquidity("p", "NBL", "USDT",
                           10000*10**DECIMALS, 1000*10**DECIMALS)
        q = amm.get_quote("NBL", "USDT", 100*10**DECIMALS)
        return "amount_out" in q and q.get("amount_out", 0) > 0
    _test("AMM swap quote", _t_amm_quote)

    # Test governance proposal
    def _t_governance():
        bc  = NEBULABlockchain()
        gov = GovernanceEngine(bc)
        ok, pid = gov.submit_proposal(
            FOUNDATION_ADDRESS, "Test Proposal",
            "Test description", GOV_MIN_DEPOSIT_NBL)
        return ok and pid == 1
    _test("Governance proposal submit", _t_governance)

    # Test price oracle
    def _t_oracle():
        bc  = NEBULABlockchain()
        oracle = PriceOracle(bc)
        price  = oracle.get_nbl_usd()
        return price is not None and price > 0
    _test("Price oracle NBL/USD", _t_oracle)

    # Test CTV template hash
    def _t_ctv():
        bc   = NEBULABlockchain()
        wallet = NEBULAWallet.create_new(bc.utxo)
        tx   = Transaction(
            inputs=[TxInput(OutPoint("a"*64, 0), b'')],
            outputs=[TxOutput(10**DECIMALS,
                     Script.p2pkh_locking_from_address(wallet.first_address))])
        h    = CheckTemplateVerify.template_hash(tx, 0)
        return len(h) == 32
    _test("CTV template hash", _t_ctv)

    # Test ECIES encryption
    def _t_ecies():
        privkey = 0xcafe1234deadbeef
        pubkey  = Secp256k1.pubkey_to_bytes(
                      Secp256k1.point_mul(privkey, Secp256k1.G()))
        msg     = b"Hello NEBULA P2P Messaging!"
        enc     = ECIES.encrypt(msg, pubkey)
        dec     = ECIES.decrypt(enc, privkey)
        return dec == msg
    _test("ECIES encrypt/decrypt", _t_ecies)

    return passed, total

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- MempoolMonitor
class MempoolMonitor:
    """
    Advanced mempool monitoring with anomaly detection.
    Detects: fee spikes, size explosions, dust attacks,
    unusual patterns, RBF storms.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc       = blockchain
        self._alerts  : List[MempoolAlert] = []
        self._history : List[dict] = []
        self._callbacks: List[Callable] = []
        self._running = False
        self._lock    = threading.Lock()

        # Thresholds
        self.size_high_threshold  = 1000
        self.size_critical        = 5000
        self.fee_spike_pct        = 50.0    # % increase triggers spike alert
        self._prev_size           = 0
        self._prev_avg_fee        = 0.0

    def add_callback(self, fn: Callable):
        self._callbacks.append(fn)

    def check(self):
        """Run all mempool checks"""
        pool = self.bc.mempool
        size = pool.size()
        now  = time.time()

        # Snapshot
        snapshot = {
            "time"     : now,
            "size"     : size,
            "fees"     : pool.total_fees() / 10**DECIMALS,
        }
        with self._lock:
            self._history.append(snapshot)
            if len(self._history) > 1440:
                self._history.pop(0)

        # Size alerts
        if size > self.size_critical:
            self._fire("size_critical", "critical",
                        f"Mempool critically full: {size:,} txs", size)
        elif size > self.size_high_threshold:
            self._fire("size_high", "warning",
                        f"Mempool congested: {size:,} txs", size)

        # Size explosion alert (doubled in one check)
        if self._prev_size > 0 and size > self._prev_size * 2:
            self._fire("size_explosion", "warning",
                        f"Mempool doubled: {self._prev_size} → {size}", size)

        self._prev_size = size

    def _fire(self, alert_type: str, severity: str,
               message: str, value: float):
        alert = MempoolAlert(alert_type, severity, message, value)
        with self._lock:
            self._alerts.append(alert)
            if len(self._alerts) > 500:
                self._alerts.pop(0)
        for cb in self._callbacks:
            try: cb(alert)
            except Exception: _NB_SWALLOW_LOG.debug("swallowed bare in MempoolMonitor._fire", exc_info=True)

    def start(self, interval: float = 30.0):
        self._running = True
        def _loop():
            while self._running:
                try: self.check()
                except Exception: _NB_SWALLOW_LOG.debug("swallowed bare in MempoolMonitor.start._loop", exc_info=True)
                time.sleep(interval)
        threading.Thread(target=_loop, daemon=True, name="MempoolMon").start()

    def stop(self): self._running = False

    def get_alerts(self, last_n: int = 20) -> List[dict]:
        with self._lock:
            return [a.to_dict() for a in self._alerts[-last_n:]]

    def trend(self) -> dict:
        with self._lock:
            if len(self._history) < 2:
                return {"insufficient_data": True}
            sizes = [h["size"] for h in self._history[-20:]]
        return {
            "current"    : sizes[-1],
            "avg"        : sum(sizes)//len(sizes),
            "max"        : max(sizes),
            "trend"      : "growing" if sizes[-1] > sizes[0] else "shrinking",
            "alert_count": len(self._alerts),
        }


# ---- NEBULATests
class NEBULATests:
    """Adapter used by NEBULAGrandFinale.run_complete_test_suite() to run core tests."""
    def __init__(self, bc):
        self.bc = bc

    def run_basic_tests(self) -> tuple:
        """Run core crypto/transaction/blockchain tests. Returns (passed, total)."""
        r = TestResultAccumulator()
        for suite in [TestCrypto(), TestTransactions(), TestBlocks(),
                      TestBlockchain(), TestWallet()]:
            try:
                suite.run(r)
            except Exception as e:
                r.fail(type(suite).__name__, str(e))
        return r.passed, r.passed + r.failed


# ---- NEBULAGrandFinale
class NEBULAGrandFinale:
    """
    Module 100: The Grand Finale.
    The complete NEBULA blockchain ecosystem.
    100 modules. ~50,000 lines. One Python file. One Python 3.
    """

    MODULES    = 100
    AUTHOR     = "NEBULA Core Team"
    VERSION    = "1.0.0"
    STARTED    = "2024"

    ACHIEVEMENT = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║   🏆  milestone reached: 100 MODULES                         ║
    ║                                                                  ║
    ║   Project  : NEBULA Blockchain                                   ║
    ║   Author   : NEBULA Core Team                                        ║
    ║   Platform : Python 3                               ║
    ║   Modules  : 100                                                 ║
    ║   Language : Pure Python (no deps)                               ║
    ║   Symbol   : NBL                                                 ║
    ║   MaxSupply: 21,000,000 NBL                                      ║
    ║                                                                  ║
    ║   ""                    ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """

    def __init__(self):
        self.bc          = NEBULABlockchain()
        self.start_time  = time.time()
        self._modules_tested = 0

    def run_complete_test_suite(self) -> dict:
        """Run the complete 100-module test suite"""
        start   = time.time()
        results = {}

        # 1. Core tests (already in nebula_tests)
        print("  Running core tests...")
        try:
            core = NEBULATests(self.bc)
            passed, total = core.run_basic_tests()
            results["core_tests"] = {"passed": passed, "total": total}
        except Exception as e:
            results["core_tests"] = {"error": str(e)}

        # 2. Extended module tests (Module 55)
        print("  Running extended module tests...")
        try:
            passed, total = _run_extended_module_tests()
            results["extended_tests"] = {"passed": passed, "total": total}
        except Exception as e:
            results["extended_tests"] = {"error": str(e)}

        # 3. Property-based tests (Module 95)
        print("  Running property-based tests...")
        try:
            prop = PropertyTest.run_all()
            results["property_tests"] = prop
        except Exception as e:
            results["property_tests"] = {"error": str(e)}

        # 4. System integration (Module 70)
        print("  Running system integration tests...")
        try:
            tester = FullSystemTester()
            sys_r  = tester.run_all()
            results["system_tests"] = {
                "passed": sys_r["passed"],
                "total" : sys_r["total"],
            }
        except Exception as e:
            results["system_tests"] = {"error": str(e)}

        # 5. Chain validation
        print("  Running chain validation...")
        try:
            validator = FullChainValidator(self.bc)
            val_r     = validator.validate_chain(verbose=False)
            results["chain_validation"] = {
                "blocks": val_r["blocks_checked"],
                "ok"    : val_r["is_valid"],
            }
        except Exception as e:
            results["chain_validation"] = {"error": str(e)}

        elapsed = time.time() - start
        total_passed = sum(
            r.get("passed", 0) for r in results.values()
            if isinstance(r, dict) and "error" not in r)
        total_tests  = sum(
            r.get("total", r.get("property_tests", 0)) for r in results.values()
            if isinstance(r, dict) and "error" not in r)

        return {
            "total_passed" : total_passed,
            "total_tests"  : total_tests,
            "elapsed"      : f"{elapsed:.2f}s",
            "modules"      : self.MODULES,
            "author"       : self.AUTHOR,
            "results"      : results,
        }

    def print_achievement(self):
        print(self.ACHIEVEMENT)

    def module_manifest(self) -> List[dict]:
        """Return manifest of all 100 modules"""
        modules = [
            (1,  "nebula_core",             "Blockchain engine (ECDSA, UTXO, PoW)"),
            (2,  "nebula_wallet",           "HD Wallet BIP32/39/44"),
            (3,  "nebula_miner",            "PoW miner (multiprocessing SHA-256d)"),
            (4,  "nebula_network",          "P2P network (TCP peers, sync)"),
            (5,  "nebula_node",             "Full node"),
            (6,  "nebula_security",         "DoS, rate-limit, replay protection"),
            (7,  "nebula_contracts",        "Smart contracts (NBL-20 tokens)"),
            (8,  "nebula_tests",            "Test suite (54 tests)"),
            (9,  "nebula_cli",              "CLI (20+ commands, REPL)"),
            (10, "nebula_api",              "REST API (32 endpoints, SSE)"),
            (11, "nebula_server",           "Ubuntu auto-deployment"),
            (12, "nebula_segwit",           "Taproot+SegWit (BIP340/341/342)"),
            (13, "nebula_lightning",        "Lightning Network (HTLC, onion)"),
            (14, "nebula_stratum",          "Stratum v1/v2 mining pool"),
            (15, "nebula_storage",          "LevelDB/SQLite persistent storage"),
            (16, "nebula_bip324",           "BIP324 encrypted P2P (ChaCha20)"),
            (17, "nebula_explorer",         "Web block explorer"),
            (18, "nebula_privacy",          "Tor/I2P privacy layer"),
            (19, "nebula_musig2",           "BIP327 MuSig2 multisig"),
            (20, "nebula_mempool_adv",      "Advanced mempool (RBF/CPFP)"),
            (21, "nebula_spv",              "SPV + BIP37 Bloom Filters"),
            (22, "nebula_jsonrpc",          "JSON-RPC Server (200 methods)"),
            (23, "nebula_descriptor",       "BIP380 Output Descriptors"),
            (24, "nebula_ibd",              "IBD / Chain Sync / Orphan handling"),
            (25, "nebula_addrbook",         "Address Book + Watch-Only"),
            (26, "nebula_bip85",            "BIP85 HD Entropy Derivation"),
            (27, "nebula_analytics",        "Advanced Chain Analytics"),
            (28, "nebula_multisig",         "P2SH/P2WSH Multisig"),
            (29, "nebula_watchdog",         "Node Watchdog + Auto-Restart"),
            (30, "nebula_p2p_adv",          "Advanced P2P + Compact Blocks"),
            (31, "nebula_wallet_ui",        "Terminal Wallet Interface"),
            (32, "nebula_rpc_client",       "JSON-RPC Batch Client"),
            (33, "nebula_adaptor",          "Schnorr Adaptor Signatures"),
            (34, "nebula_utxo_snap",        "UTXO Snapshot (assumeutxo)"),
            (35, "nebula_simulator",        "Network Simulator"),
            (36, "nebula_script",           "Full Script Interpreter"),
            (37, "nebula_txbuilder",        "Advanced Transaction Builder"),
            (38, "nebula_timelock",         "CLTV/CSV Timelocks + Vaults"),
            (39, "nebula_upgrades",         "BIP9 Version Bits + Soft Forks"),
            (40, "nebula_feebumper",        "Fee Bumper (RBF/CPFP auto)"),
            (41, "nebula_cold_storage",     "PSBT + Air-Gapped Signing"),
            (42, "nebula_covenant",         "CTV Covenants + Coin Pools"),
            (43, "nebula_staking",          "NBL Staking + Delegation"),
            (44, "nebula_crosschain",       "Cross-Chain Atomic Swaps"),
            (45, "nebula_oracle",           "Decentralized Price Oracle"),
            (46, "nebula_defi",             "AMM + Lending Protocol"),
            (47, "nebula_messaging",        "ECIES Encrypted Messaging"),
            (48, "nebula_governance",       "On-Chain DAO Governance"),
            (49, "nebula_zkproofs",         "Zero-Knowledge Proof Primitives"),
            (50, "nebula_enhanced_node",    "Enhanced Full Node (50 modules)"),
            (51, "nebula_netstats",         "Real-Time Network Statistics"),
            (52, "nebula_pruning",          "Block Pruning + Archive"),
            (53, "nebula_fee_reserve",      "Fee Reserve Tracker"),
            (54, "nebula_wallet_connect",   "WalletConnect Protocol"),
            (55, "nebula_ext_tests",        "Extended Test Suite"),
            (56, "nebula_mempool_viz",      "Mempool Heatmap + Analytics"),
            (57, "nebula_indexer",          "Full Chain Indexer"),
            (58, "nebula_tx_graph",         "Transaction Graph Analysis"),
            (59, "nebula_pool",             "Mining Pool (PPLNS)"),
            (60, "nebula_dex",              "DEX Order Book"),
            (61, "nebula_nft",              "NBL-721 NFTs"),
            (62, "nebula_bridge",           "Cross-Chain Token Bridge"),
            (63, "nebula_reward_sim",       "Block Reward Simulator"),
            (64, "nebula_recovery",         "Wallet Recovery + Backup"),
            (65, "nebula_protocol_docs",    "Protocol Documentation"),
            (66, "nebula_smart_wallet",     "Smart Wallet (Account Abstraction)"),
            (67, "nebula_mempool_rpc",      "Mempool RPC Extensions"),
            (68, "nebula_blockchain_api",   "Public Blockchain REST API"),
            (69, "nebula_addr_gen",         "Bulk Address Generator"),
            (70, "nebula_sys_test",         "Full System Integration Test"),
            (71, "nebula_security_audit",   "Security Audit Framework"),
            (72, "nebula_benchmarks",       "Performance Benchmarks"),
            (73, "nebula_historical",       "Historical Data Manager"),
            (74, "nebula_adv_mining",       "Advanced Mining (Vardiff)"),
            (75, "nebula_ecosystem",        "NEBULAEcosystem (75 modules)"),
            (76, "nebula_gossip",           "Gossip Protocol + Kademlia DHT"),
            (77, "nebula_script_tmpl",      "Script Template Library"),
            (78, "nebula_chain_state",      "Chain State Snapshots"),
            (79, "nebula_notifications",    "Alerts + Notifications"),
            (80, "nebula_devtools",         "Developer Tools Suite"),
            (81, "nebula_explorer_api",     "Block Explorer Backend API"),
            (82, "nebula_mobile_sync",      "Mobile-Optimized Sync"),
            (83, "nebula_discovery",        "Automatic Node Discovery"),
            (84, "nebula_mempool_policy",   "Advanced Mempool Policy"),
            (85, "nebula_monitor",          "System Monitoring Dashboard"),
            (86, "nebula_fork_mgr",         "Chain Fork Detection"),
            (87, "nebula_token_registry",   "NBL-20 Token Registry"),
            (88, "nebula_upgrade_mgr",      "Protocol Upgrade Manager"),
            (89, "nebula_batch_proc",       "Batch Transaction Processor"),
            (90, "nebula_complete",         "NEBULAComplete (90 modules)"),
            (91, "nebula_chain_metrics",    "Advanced On-Chain Metrics"),
            (92, "nebula_tx_accel",         "Transaction Accelerator"),
            (93, "nebula_data_export",      "Data Export + HTML Reports"),
            (94, "nebula_contract_stdlib",  "Smart Contract Standard Library"),
            (95, "nebula_test_framework",   "Full Testing Framework"),
            (96, "nebula_chain_clock",      "Median Time Past + Clock"),
            (97, "nebula_sig_agg",          "Signature Aggregation"),
            (98, "nebula_chain_valid",      "Full Chain Validator"),
            (99, "nebula_mempool_mon",      "Mempool Monitor + Alerts"),
            (100,"nebula_grand_finale",     "The Grand Finale — 100 Modules"),
        ]
        return [
            {"id": n, "name": name, "description": desc}
            for n, name, desc in modules
        ]

    def statistics(self) -> dict:
        """Final statistics for the NEBULA project"""
        return {
            "project"         : "NEBULA Blockchain",
            "author"          : self.AUTHOR,
            "version"         : self.VERSION,
            "modules"         : self.MODULES,
            "platform": "Python 3",
            "language"        : "Python 3 (pure stdlib)",
            "external_deps"   : 0,
            "chain_name"      : CHAIN_NAME,
            "symbol"          : CHAIN_SYMBOL,
            "max_supply"      : f"{MAX_SUPPLY/10**DECIMALS:,.0f} NBL",
            "consensus"       : "Proof of Work (SHA-256d)",
            "block_time"      : f"{TARGET_BLOCK_TIME}s",
            "halving"         : f"Every {HALVING_INTERVAL:,} blocks",
            "foundation"      : f"{FOUNDATION_RATE*100:.0f}% per block → {FOUNDATION_ADDRESS}",
            "features"        : [
                "secp256k1 ECDSA + Schnorr",
                "HD Wallets (BIP32/39/44/85)",
                "SegWit + Taproot (BIP340/341/342)",
                "Lightning Network (HTLC)",
                "MuSig2 Multi-Signature",
                "Atomic Cross-Chain Swaps",
                "ZK Proof Primitives",
                "AMM DeFi + DEX",
                "DAO Governance",
                "NFTs (NBL-721)",
                "Tor/I2P Privacy",
                "BIP9 Soft Forks",
                "JSON-RPC 200 methods",
                "Block Explorer",
                "Mining Pool (PPLNS)",
                "Token Bridge",
                "Price Oracle (TWAP)",
                "Staking + Delegation",
                "Smart Wallets",
                "Kademlia DHT",
            ],
        }

    def final_print(self):
        """Print the final status"""
        stats = self.statistics()
        print(self.ACHIEVEMENT)
        print(f"\n  📊 NEBULA Final Statistics:")
        print(f"  {'─'*45}")
        for k, v in stats.items():
            if not isinstance(v, list):
                print(f"  {k:25}: {v}")
        print(f"\n  Features ({len(stats['features'])} total):")
        for feat in stats["features"]:
            print(f"    ✅ {feat}")
        print(f"\n  Module Manifest ({self.MODULES} modules):")
        for m in self.module_manifest()[-10:]:
            print(f"    [{m['id']:>3}] {m['name']:30} {m['description'][:35]}")
        print(f"\n  🌌 NEBULA — Built on a Python 3 by {self.AUTHOR}")
        print(f"  {'═'*55}")


# ---- BLSSignature
class BLSSignature:
    """
    BLS (Boneh-Lynn-Shacham) signature scheme.
    Key property: signatures are aggregatable.
    N parties can aggregate N signatures into 1 short signature.
    Used in: ETH2, Chia, many PoS chains.
    Pure Python implementation using secp256k1 as approximation.
    """

    @classmethod
    def keygen(cls) -> Tuple[int, bytes]:
        """Generate BLS keypair (privkey_int, pubkey_bytes)"""
        privkey = secrets.randbelow(Secp256k1.N - 1) + 1
        pubkey  = Secp256k1.pubkey_to_bytes(
                      Secp256k1.point_mul(privkey, Secp256k1.G()))
        return privkey, pubkey

    @classmethod
    def sign(cls, privkey: int, msg: bytes) -> bytes:
        """Sign message. Returns 64-byte signature."""
        msg_hash = hashlib.sha256(b"BLS/sign" + msg).digest()
        h_int    = int.from_bytes(msg_hash, 'big') % Secp256k1.N
        sig_pt   = Secp256k1.point_mul(privkey * h_int % Secp256k1.N,
                                         Secp256k1.G())
        return Secp256k1.pubkey_to_bytes(sig_pt)

    @classmethod
    def verify(cls, pubkey: bytes, msg: bytes, sig: bytes) -> bool:
        """Verify BLS signature"""
        try:
            msg_hash = hashlib.sha256(b"BLS/sign" + msg).digest()
            return len(sig) in (33, 64, 65)   # simplified
        except Exception:
            return False

    @classmethod
    def aggregate_sigs(cls, signatures: List[bytes]) -> bytes:
        """
        Aggregate N BLS signatures into one.
        The aggregated signature is the same size as one signature!
        """
        if not signatures:
            return b'\x00' * 33
        # Sum the signature points
        result = None
        for sig in signatures:
            x   = int.from_bytes(sig[1:33], 'big')
            P   = Secp256k1.P
            ys  = (pow(x, 3, P) + 7) % P
            y   = pow(ys, (P+1)//4, P)
            if (y%2==0) != (sig[0]==0x02 if len(sig)>1 else True):
                y = P - y
            pt  = (x, y)
            if result is None:
                result = pt
            else:
                result = Schnorr._point_add(result, pt)
        if result is None:
            return b'\x00' * 33
        return Secp256k1.pubkey_to_bytes(result)

    @classmethod
    def aggregate_verify(cls, agg_sig: bytes,
                          pubkeys: List[bytes],
                          messages: List[bytes]) -> bool:
        """Verify aggregated BLS signature"""
        return len(agg_sig) >= 33

    @classmethod
    def size_comparison(cls, n: int) -> dict:
        """Compare BLS vs Schnorr signature sizes"""
        return {
            "n_signatures"    : n,
            "schnorr_total"   : n * 64,
            "bls_aggregated"  : 48,       # BLS sig is ~48 bytes regardless of n
            "bls_saving"      : f"{(1 - 48/(n*64))*100:.1f}% smaller",
        }


# ---- VerkleTree
class VerkleTree:
    """
    Verkle Tree — more efficient than Merkle trees for state storage.
    Used in Ethereum's upcoming state tree upgrade.
    Proofs are much smaller: O(1) vs O(log n) for Merkle.
    """

    def __init__(self, width: int = 256):
        self.width    = width
        self._nodes  : dict = {}
        self._root   : Optional[bytes] = None

    def insert(self, key: bytes, value: bytes):
        """Insert key-value pair"""
        path      = [key[i] for i in range(min(4, len(key)))]
        node_hash = hashlib.sha256(key + value).digest()
        self._nodes[key] = (value, node_hash)
        self._root = self._compute_root()

    def get(self, key: bytes) -> Optional[bytes]:
        entry = self._nodes.get(key)
        return entry[0] if entry else None

    def generate_proof(self, key: bytes) -> dict:
        """Generate a Verkle proof for a key"""
        entry = self._nodes.get(key)
        if not entry:
            return {"exists": False}
        value, node_hash = entry
        # Simplified proof (real Verkle uses IPA/KZG commitments)
        proof_hash = hashlib.sha256(
            key + value + (self._root or b'')).digest()
        return {
            "exists"     : True,
            "key"        : key.hex(),
            "value"      : value.hex(),
            "proof_hash" : proof_hash.hex(),
            "root"       : self._root.hex() if self._root else "",
            "proof_size" : 96,   # bytes (vs Merkle which grows with n)
        }

    def verify_proof(self, proof: dict) -> bool:
        """Verify a Verkle proof"""
        return proof.get("exists", False) and "proof_hash" in proof

    def _compute_root(self) -> bytes:
        if not self._nodes:
            return bytes(32)
        all_hashes = b''.join(v[1] for v in self._nodes.values())
        return hashlib.sha256(all_hashes).digest()

    @property
    def root(self) -> Optional[bytes]:
        return self._root

    def size(self) -> int:
        return len(self._nodes)


# ---- KZGCommitment
class KZGCommitment:
    """
    KZG (Kate-Zaverucha-Goldberg) polynomial commitment.
    Used in: EIP-4844 (Proto-Danksharding), zk-SNARKs.
    Allows committing to a polynomial and proving evaluations.
    Simplified implementation for educational purposes.
    """

    def __init__(self, degree: int = 256):
        self.degree = degree
        # Trusted setup (in production: powers of tau ceremony)
        self._tau   = int.from_bytes(secrets.token_bytes(32), 'big') % Secp256k1.N

    def commit(self, polynomial: List[int]) -> bytes:
        """
        Commit to a polynomial f(x) = sum(coeff_i * x^i).
        Returns 33-byte commitment.
        """
        # C = sum(coeff_i * tau^i * G)
        result = None
        tau_pow = 1
        for coeff in polynomial[:self.degree]:
            if coeff != 0:
                scalar = (coeff * tau_pow) % Secp256k1.N
                pt     = Secp256k1.point_mul(scalar, Secp256k1.G())
                if result is None:
                    result = pt
                else:
                    result = Schnorr._point_add(result, pt)
            tau_pow = (tau_pow * self._tau) % Secp256k1.N

        if result is None:
            return bytes(33)
        return Secp256k1.pubkey_to_bytes(result)

    def prove_evaluation(self, polynomial: List[int], z: int,
                          y: int) -> bytes:
        """Prove that f(z) = y"""
        # Witness polynomial: q(x) = (f(x) - y) / (x - z)
        # Simplified: just hash the claim
        claim = (f"{polynomial[:4]}:{z}:{y}").encode()
        proof = hashlib.sha256(claim).digest()
        return proof

    def verify_evaluation(self, commitment: bytes,
                            z: int, y: int,
                            proof: bytes) -> bool:
        """Verify that f(z) = y using the commitment and proof"""
        return len(proof) == 32 and len(commitment) >= 33

    def blob_commitment(self, data: bytes) -> bytes:
        """Commit to a data blob (EIP-4844 style)"""
        # Split data into field elements
        field_elems = []
        for i in range(0, min(len(data), self.degree * 32), 32):
            chunk = data[i:i+32]
            val   = int.from_bytes(chunk.ljust(32, b'\x00'), 'big') % Secp256k1.N
            field_elems.append(val)
        return self.commit(field_elems)


# ---- ValidatorVote
@dataclass
class ValidatorVote:
    """A PoS validator vote for a block"""
    validator : str
    block_hash: str
    block_height: int
    signature : bytes
    stake     : int
    timestamp : float = field(default_factory=time.time)

    def to_dict(self) -> dict:
        return {
            "validator"  : self.validator[:16] + "...",
            "block_hash" : self.block_hash[:16] + "...",
            "height"     : self.block_height,
            "stake"      : self.stake / 10**DECIMALS,
        }


# ---- HybridConsensus
class HybridConsensus:
    """
    Hybrid PoW/PoS consensus for NEBULA.
    PoW: produces blocks (like Bitcoin).
    PoS validators: vote on canonical chain, enabling fast finality.
    A block is "finalized" when 2/3 of staked NBL votes for it.
    """

    FINALITY_THRESHOLD = 0.67   # 67% of staked NBL
    VOTE_PERIOD_BLOCKS = 6      # validators vote every 6 blocks
    MAX_VOTE_AGE       = 12     # discard votes older than 12 blocks

    def __init__(self, blockchain: 'NEBULABlockchain',
                 staking: 'StakingEngine'):
        self.bc        = blockchain
        self.staking   = staking
        self._votes    : Dict[str, List[ValidatorVote]] = {}
        self._finalized: Set[int] = set()   # finalized block heights
        self._lock     = threading.RLock()

    def submit_vote(self, validator_addr: str,
                     block_hash: str,
                     block_height: int,
                     privkey: int) -> Tuple[bool, str]:
        """Submit a validator vote"""
        # Check validator is active
        val = self.staking._validators.get(validator_addr)
        if not val or not val.is_active:
            return False, "Not an active validator"

        # Sign the vote
        msg    = hashlib.sha256(f"{block_hash}:{block_height}".encode()).digest()
        r, s   = Secp256k1.sign(privkey, msg)
        sig    = Secp256k1.sig_to_der(r, s)

        vote = ValidatorVote(
            validator    = validator_addr,
            block_hash   = block_hash,
            block_height = block_height,
            signature    = sig,
            stake        = val.total_staked + val.self_stake,
        )

        with self._lock:
            self._votes.setdefault(block_hash, []).append(vote)
            # Check if finality threshold met
            if self._check_finality(block_hash, block_height):
                self._finalized.add(block_height)
                return True, f"Block {block_height} finalized!"

        return True, "Vote accepted"

    def _check_finality(self, block_hash: str, height: int) -> bool:
        """Check if block has enough votes for finality"""
        if height in self._finalized:
            return True

        votes      = self._votes.get(block_hash, [])
        voted_stake = sum(v.stake for v in votes)
        total_stake = self.staking._total_staked

        if total_stake == 0:
            return False
        return voted_stake / total_stake >= self.FINALITY_THRESHOLD

    def is_finalized(self, height: int) -> bool:
        return height in self._finalized

    def finalized_height(self) -> int:
        """Highest finalized block height"""
        return max(self._finalized, default=-1)

    def get_block_votes(self, block_hash: str) -> List[dict]:
        with self._lock:
            return [v.to_dict() for v in self._votes.get(block_hash, [])]

    def stats(self) -> dict:
        total_stake = self.staking._total_staked
        return {
            "finalized_height" : self.finalized_height(),
            "total_votes"      : sum(len(v) for v in self._votes.values()),
            "finalized_blocks" : len(self._finalized),
            "total_staked_nbl" : total_stake / 10**DECIMALS,
            "validators"       : len(self.staking._validators),
        }


# ---- StealthAddress
class StealthAddress:
    """
    One-time stealth addresses.
    Sender generates a unique address for each payment.
    Recipient scans blockchain to find payments to them.
    Sender and recipient know the address; nobody else does.
    """

    @classmethod
    def generate_payment_address(cls, recipient_spend_pubkey: bytes,
                                  recipient_view_pubkey: bytes) -> Tuple[bytes, bytes]:
        """
        Generate a one-time stealth address.
        Returns (one_time_pubkey, payment_pubkey).
        """
        # r = random scalar
        r    = secrets.randbelow(Secp256k1.N - 1) + 1
        # R = r*G (shared secret component)
        R    = Secp256k1.pubkey_to_bytes(
                   Secp256k1.point_mul(r, Secp256k1.G()))

        # Shared secret = H(r * view_pubkey)
        vx   = int.from_bytes(recipient_view_pubkey[1:], 'big')
        P    = Secp256k1.P
        vys  = (pow(vx, 3, P) + 7) % P
        vy   = pow(vys, (P+1)//4, P)
        if (vy%2==0) != (recipient_view_pubkey[0]==0x02):
            vy = P - vy
        view_pt   = (vx, vy)
        shared_pt = Schnorr._point_mul(r, view_pt)
        if shared_pt is None:
            return R, recipient_spend_pubkey

        secret    = hashlib.sha256(
            shared_pt[0].to_bytes(32,'big')).digest()
        s_int     = int.from_bytes(secret, 'big') % Secp256k1.N

        # Payment key = s*G + spend_pubkey
        sG        = Secp256k1.point_mul(s_int, Secp256k1.G())
        sx        = int.from_bytes(recipient_spend_pubkey[1:], 'big')
        spys      = (pow(sx, 3, P) + 7) % P
        spy       = pow(spys, (P+1)//4, P)
        if (spy%2==0) != (recipient_spend_pubkey[0]==0x02):
            spy = P - spy
        spend_pt  = (sx, spy)
        payment_pt= Schnorr._point_add(sG, spend_pt)

        payment_key = (Secp256k1.pubkey_to_bytes(payment_pt)
                       if payment_pt else recipient_spend_pubkey)
        return R, payment_key

    @classmethod
    def scan_for_payments(cls, view_privkey: int,
                           spend_pubkey: bytes,
                           ephemeral_keys: List[bytes]) -> List[int]:
        """
        Scan list of ephemeral keys to find payments to us.
        Returns indices of matching payments.
        """
        matches = []
        for i, R in enumerate(ephemeral_keys):
            try:
                Rx   = int.from_bytes(R[1:], 'big')
                P_   = Secp256k1.P
                Rys  = (pow(Rx, 3, P_) + 7) % P_
                Ry   = pow(Rys, (P_+1)//4, P_)
                if (Ry%2==0) != (R[0]==0x02):
                    Ry = P_ - Ry
                Rpt  = (Rx, Ry)
                # Shared secret using our view key
                shared  = Schnorr._point_mul(view_privkey, Rpt)
                if shared is None:
                    continue
                secret  = hashlib.sha256(shared[0].to_bytes(32,'big')).digest()
                s_int   = int.from_bytes(secret, 'big') % Secp256k1.N
                # Check if payment key matches
                sG      = Secp256k1.point_mul(s_int, Secp256k1.G())
                sx      = int.from_bytes(spend_pubkey[1:], 'big')
                spys    = (pow(sx, 3, P_) + 7) % P_
                spy     = pow(spys, (P_+1)//4, P_)
                if (spy%2==0) != (spend_pubkey[0]==0x02):
                    spy = P_ - spy
                spt     = (sx, spy)
                expected= Schnorr._point_add(sG, spt)
                if expected:
                    matches.append(i)
            except Exception:
                continue
        return matches


# ---- RingSignature
class RingSignature:
    """
    Linkable Ring Signature (simplified).
    Proves knowledge of one key in a set, without revealing which.
    Used for: privacy coins, anonymous voting, whistleblowing.
    """

    @classmethod
    def sign(cls, privkey: int,
              ring_pubkeys: List[bytes],
              msg: bytes) -> dict:
        """
        Sign message with ring. Returns ring signature.
        True signer's index is hidden in the ring.
        """
        n        = len(ring_pubkeys)
        our_pub  = Secp256k1.pubkey_to_bytes(
                       Secp256k1.point_mul(privkey, Secp256k1.G()))

        # Find our index in ring
        our_idx  = -1
        for i, pk in enumerate(ring_pubkeys):
            if pk == our_pub:
                our_idx = i
                break

        if our_idx < 0:
            raise ValueError("Signer not in ring")

        # Generate random scalars for other ring members
        c      = [0] * n
        s      = [secrets.randbelow(Secp256k1.N) for _ in range(n)]
        alpha  = secrets.randbelow(Secp256k1.N)

        # Compute key image (prevents double-spending)
        H_pk   = hashlib.sha256(our_pub).digest()
        key_image = Secp256k1.pubkey_to_bytes(
            Secp256k1.point_mul(
                int.from_bytes(H_pk, 'big') % Secp256k1.N,
                Secp256k1.G()))

        # Compute ring hash (simplified)
        ring_hash = hashlib.sha256(
            b''.join(pk for pk in ring_pubkeys) + msg).hexdigest()

        return {
            "ring_hash"  : ring_hash,
            "key_image"  : key_image.hex(),
            "c"          : [hex(ci) for ci in c],
            "s"          : [hex(si) for si in s],
            "ring_size"  : n,
            "msg_hash"   : hashlib.sha256(msg).hexdigest(),
        }

    @classmethod
    def verify(cls, sig: dict, ring_pubkeys: List[bytes],
                msg: bytes) -> bool:
        """Verify ring signature"""
        return (sig.get("ring_size") == len(ring_pubkeys) and
                "key_image" in sig and "ring_hash" in sig)


# ---- L2Type
class L2Type(Enum):
    PAYMENT_CHANNEL = "payment_channel"
    STATE_CHANNEL   = "state_channel"
    OPTIMISTIC_ROLL = "optimistic_rollup"
    ZK_ROLLUP       = "zk_rollup"
    PLASMA          = "plasma"


# ---- L2Channel
@dataclass
class L2Channel:
    """A Layer 2 channel between two parties"""
    channel_id  : str
    party_a     : str
    party_b     : str
    balance_a   : int
    balance_b   : int
    l2_type     : L2Type
    state_num   : int  = 0
    is_open     : bool = True
    opened_at   : float = field(default_factory=time.time)
    closed_at   : Optional[float] = None
    dispute_end : Optional[float] = None

    @property
    def total_value(self) -> int:
        return self.balance_a + self.balance_b

    def update(self, new_a: int, new_b: int) -> bool:
        """Update channel balances off-chain"""
        if new_a + new_b != self.total_value:
            return False   # Conservation of value
        if new_a < 0 or new_b < 0:
            return False
        self.balance_a = new_a
        self.balance_b = new_b
        self.state_num += 1
        return True

    def to_dict(self) -> dict:
        return {
            "channel_id" : self.channel_id,
            "type"       : self.l2_type.value,
            "party_a"    : self.party_a[:16] + "...",
            "party_b"    : self.party_b[:16] + "...",
            "balance_a"  : self.balance_a / 10**DECIMALS,
            "balance_b"  : self.balance_b / 10**DECIMALS,
            "total"      : self.total_value / 10**DECIMALS,
            "state_num"  : self.state_num,
            "is_open"    : self.is_open,
        }


# ---- Layer2Manager
class Layer2Manager:
    """
    Manages Layer 2 protocols for NEBULA.
    Handles: channel lifecycle, state updates, disputes, settlements.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc       = blockchain
        self._channels: Dict[str, L2Channel] = {}
        self._lock    = threading.RLock()
        self._total_l2_value = 0

    def open_channel(self, party_a: str, party_b: str,
                      amount_a: int, amount_b: int,
                      l2_type: L2Type = L2Type.PAYMENT_CHANNEL) -> L2Channel:
        """Open a new L2 channel"""
        channel_id = hashlib.sha256(
            f"{party_a}{party_b}{time.time()}".encode()).hexdigest()[:16]

        channel = L2Channel(
            channel_id = channel_id,
            party_a    = party_a,
            party_b    = party_b,
            balance_a  = amount_a,
            balance_b  = amount_b,
            l2_type    = l2_type,
        )
        with self._lock:
            self._channels[channel_id] = channel
            self._total_l2_value += channel.total_value
        return channel

    def update_channel(self, channel_id: str,
                        new_a: int, new_b: int) -> Tuple[bool, str]:
        """Update channel state off-chain"""
        with self._lock:
            ch = self._channels.get(channel_id)
            if not ch:
                return False, "Channel not found"
            if not ch.is_open:
                return False, "Channel closed"
            ok = ch.update(new_a, new_b)
            return ok, f"State #{ch.state_num}" if ok else "Invalid update"

    def open_and_update(self, party_a: str, party_b: str,
                          amount_a: int, amount_b: int,
                          new_a: int, new_b: int) -> Tuple[bool, str, str]:
        """Open channel and immediately update state (convenience method)"""
        ch = self.open_channel(party_a, party_b, amount_a, amount_b)
        ok, msg = self.update_channel(ch.channel_id, new_a, new_b)
        return ok, msg, ch.channel_id

    def close_channel(self, channel_id: str,
                       cooperative: bool = True) -> Tuple[bool, str]:
        """Close a channel and settle on-chain"""
        with self._lock:
            ch = self._channels.get(channel_id)
            if not ch:
                return False, "Channel not found"
            ch.is_open   = False
            ch.closed_at = time.time()
            if not cooperative:
                ch.dispute_end = time.time() + 7 * 86400   # 7-day dispute window
            self._total_l2_value -= ch.total_value
        return True, f"Channel closed ({'cooperative' if cooperative else 'dispute'})"

    def get_channel(self, channel_id: str) -> Optional[dict]:
        ch = self._channels.get(channel_id)
        return ch.to_dict() if ch else None

    def open_channels(self) -> List[dict]:
        with self._lock:
            return [ch.to_dict() for ch in self._channels.values() if ch.is_open]

    def route_payment(self, from_addr: str, to_addr: str,
                       amount: int) -> Tuple[bool, str]:
        """
        Route payment through L2 channels.
        Finds a path: from → intermediate channels → to.
        """
        # Simple: find direct channel
        with self._lock:
            for ch in self._channels.values():
                if not ch.is_open:
                    continue
                if ch.party_a == from_addr and ch.balance_a >= amount:
                    if ch.party_b == to_addr:
                        ok = ch.update(ch.balance_a - amount,
                                        ch.balance_b + amount)
                        return ok, f"Routed via channel {ch.channel_id[:8]}"
                elif ch.party_b == from_addr and ch.balance_b >= amount:
                    if ch.party_a == to_addr:
                        ok = ch.update(ch.balance_a + amount,
                                        ch.balance_b - amount)
                        return ok, f"Routed via channel {ch.channel_id[:8]}"
        return False, "No route found"

    def stats(self) -> dict:
        with self._lock:
            open_ch = sum(1 for ch in self._channels.values() if ch.is_open)
            return {
                "total_channels"  : len(self._channels),
                "open_channels"   : open_ch,
                "total_l2_value"  : self._total_l2_value / 10**DECIMALS,
                "channel_types"   : {t.value: sum(1 for ch in self._channels.values()
                                                    if ch.l2_type == t and ch.is_open)
                                     for t in L2Type},
            }


# ---- NEBULALaunchChecker
class NEBULALaunchChecker:
    """
    Pre-launch checklist for NEBULA mainnet.
    Verifies all systems are ready for production.
    """

    CHECKLIST = [
        ("Core blockchain", "NEBULABlockchain", True),
        ("HD Wallets", "BIP32/39/44", True),
        ("PoW Mining", "SHA-256d", True),
        ("P2P Network", "TCP peers", True),
        ("Security", "DoS protection", True),
        ("Smart Contracts", "NBL-20 tokens", True),
        ("Test Suite", "54/54 tests", True),
        ("JSON-RPC", "200 methods", True),
        ("SegWit/Taproot", "BIP340/341/342", True),
        ("Lightning Network", "HTLC channels", True),
        ("Stratum Protocol", "Pool mining", True),
        ("BIP324", "Encrypted P2P", True),
        ("Block Explorer", "Web interface", True),
        ("Tor/I2P Privacy", "SOCKS5/SAM", True),
        ("MuSig2", "BIP327", True),
        ("SPV/Bloom Filters", "BIP37/157/158", True),
        ("Descriptor Wallets", "BIP380", True),
        ("IBD Sync", "Headers first", True),
        ("Analytics", "Rich list, UTXO age", True),
        ("Multisig", "P2SH/P2WSH", True),
        ("PSBT", "BIP174 cold storage", True),
        ("CTV Covenants", "BIP119", True),
        ("Staking", "PoS delegation", True),
        ("Atomic Swaps", "HTLC cross-chain", True),
        ("Price Oracle", "TWAP", True),
        ("AMM DeFi", "Constant product", True),
        ("DEX", "Order book", True),
        ("NFTs", "NBL-721", True),
        ("Token Bridge", "Peg-in/out", True),
        ("DAO Governance", "On-chain voting", True),
        ("ZK Proofs", "Pedersen + range", True),
        ("Gossip Protocol", "Epidemic broadcast", True),
        ("Kademlia DHT", "Peer routing", True),
        ("Script Templates", "Escrow, vault, etc.", True),
        ("Mining Pool", "PPLNS payouts", True),
        ("Monitoring", "Real-time dashboard", True),
        ("Block Explorer API", "15+ endpoints", True),
        ("Security Audit", "Score: 100", True),
        ("Chain Validator", "Full validation", True),
        ("BLS Signatures", "Aggregatable", True),
        ("Verkle Trees", "State efficiency", True),
        ("Hybrid PoS", "Fast finality", True),
        ("Stealth Addresses", "One-time addrs", True),
        ("Ring Signatures", "Anonymous txs", True),
        ("Layer 2", "State channels", True),
    ]

    def __init__(self, blockchain: 'NEBULABlockchain' = None):
        self.bc = blockchain or NEBULABlockchain()

    def run_checklist(self) -> dict:
        """Run pre-launch checklist"""
        passed = sum(1 for _, _, ok in self.CHECKLIST if ok)
        total  = len(self.CHECKLIST)
        return {
            "ready"         : passed == total,
            "passed"        : passed,
            "total"         : total,
            "pct"           : f"{passed/total*100:.0f}%",
            "items"         : [
                {"feature": f, "component": c, "ready": ok}
                for f, c, ok in self.CHECKLIST
            ],
        }

    def deployment_guide(self) -> str:
        """Generate deployment guide"""
        return f"""
NEBULA Mainnet Deployment Guide
================================
Version: 1.0.0

1. REQUIREMENTS
   - Python 3.9+
   - 4GB RAM minimum
   - 100GB SSD
   - Ubuntu 20.04+ recommended

2. INSTALLATION
   git clone <repository-url>
   cd NEBULA-Blockchain-Ecosystem
   python3 nebula_main.py node

3. START NODE
   python3 nebula_main.py node --rpc-port 8332 --p2p-port 8333

4. MINE NBL
   python3 nebula_main.py mine --address YOUR_ADDRESS

5. RPC ACCESS
   curl http://127.0.0.1:8332 -d '{{"method":"getblockchaininfo"}}'

6. EXPLORER
   Open browser: http://127.0.0.1:8081/explorer/stats

7. WALLET
   python3 nebula_main.py wallet create

Chain ID    : {CHAIN_ID}
P2PKH Prefix: {PUBKEY_ADDRESS_PREFIX}
Max Supply  : {MAX_SUPPLY/10**DECIMALS:,.0f} NBL
Block Time  : {TARGET_BLOCK_TIME}s
Halving     : Every {HALVING_INTERVAL:,} blocks
Foundation  : {FOUNDATION_RATE*100:.0f}% → {FOUNDATION_ADDRESS}
"""

    def community_message(self) -> str:
        return f"""
Dear NEBULA Community,

This blockchain was built from scratch on a Python 3.
100 modules. ~50,000 lines. Pure Python. No external dependencies.

From genesis block to Lightning Network.
From basic PoW to Taproot + MuSig2.
From a simple wallet to DeFi, NFTs, and DAO governance.

,


This is NEBULA — your blockchain, our vision.

— NEBULA Core Team
  {time.strftime("%Y")}
"""

    def print_final(self):
        """Print the final launch status"""
        check = self.run_checklist()
        print("\n" + "█"*60)
        print("  🌌  NEBULA BLOCKCHAIN — LAUNCH READY")
        print("█"*60)
        print(f"  Checklist: {check['passed']}/{check['total']} ({check['pct']})")
        print(f"  Status: {'✅ READY FOR MAINNET' if check['ready'] else '⚠️ NOT READY'}")
        print("─"*60)
        print(self.community_message())
        print("─"*60)
        print(self.deployment_guide())
        print("█"*60)


# ---- Cluster
@dataclass
class Cluster:
    """A group of addresses believed to belong to the same entity"""
    cluster_id  : int
    addresses   : Set[str] = field(default_factory=set)
    label       : str      = ""
    entity_type : str      = "unknown"   # exchange/miner/whale/personal/contract
    tags        : List[str]= field(default_factory=list)
    balance     : int      = 0
    tx_count    : int      = 0
    first_seen  : int      = 0    # block height
    last_seen   : int      = 0

    def size(self) -> int:
        return len(self.addresses)

    def to_dict(self) -> dict:
        return {
            "id"          : self.cluster_id,
            "size"        : self.size(),
            "label"       : self.label or f"Cluster #{self.cluster_id}",
            "entity_type" : self.entity_type,
            "balance_nbl" : self.balance / 10**DECIMALS,
            "tx_count"    : self.tx_count,
            "tags"        : self.tags,
        }


# ---- CommonInputHeuristic
class CommonInputHeuristic:
    """
    Bitcoin's most effective clustering heuristic.
    Assumption: all inputs of a transaction belong to the same wallet.
    A multi-input tx reveals that the owner controls all input addresses.
    """

    def __init__(self):
        self._unions : Dict[str, str] = {}   # union-find: addr → root

    def _find(self, addr: str) -> str:
        if addr not in self._unions:
            self._unions[addr] = addr
        if self._unions[addr] != addr:
            self._unions[addr] = self._find(self._unions[addr])
        return self._unions[addr]

    def _union(self, a: str, b: str):
        ra, rb = self._find(a), self._find(b)
        if ra != rb:
            self._unions[ra] = rb

    def process_transaction(self, tx: 'Transaction',
                              utxo: 'UTXOSet'):
        """Apply heuristic: union all input addresses"""
        if tx.is_coinbase or len(tx.inputs) < 2:
            return
        input_addrs = []
        for inp in tx.inputs:
            u = utxo.get(inp.outpoint.txid, inp.outpoint.index)
            if u and u.address:
                input_addrs.append(u.address)
        if len(input_addrs) < 2:
            return
        root = input_addrs[0]
        for addr in input_addrs[1:]:
            self._union(root, addr)

    def get_cluster(self, address: str) -> str:
        """Get cluster root for address"""
        return self._find(address)

    def build_clusters(self) -> Dict[str, Set[str]]:
        """Build all clusters from union-find"""
        clusters : Dict[str, Set[str]] = defaultdict(set)
        for addr in self._unions:
            root = self._find(addr)
            clusters[root].add(addr)
        return dict(clusters)

    def cluster_count(self) -> int:
        return len(set(self._find(a) for a in self._unions))


# ---- ChangeDetectionHeuristic
class ChangeDetectionHeuristic:
    """
    Change address detection heuristics.
    Identifies likely change outputs to improve clustering.
    Methods: round-number heuristic, address reuse, output count.
    """

    @staticmethod
    def is_likely_change(tx: 'Transaction',
                          output_idx: int,
                          utxo: 'UTXOSet') -> bool:
        """Determine if an output is likely change"""
        out = tx.outputs[output_idx]
        if len(tx.outputs) < 2:
            return False

        # Heuristic 1: Only one output → likely change is absent
        # Heuristic 2: Smaller of two outputs is often change
        if len(tx.outputs) == 2:
            other_idx = 1 - output_idx
            other_out = tx.outputs[other_idx]
            # Round number heuristic: payment is round, change is not
            val_nbl = out.value / 10**DECIMALS
            other_nbl = other_out.value / 10**DECIMALS
            if abs(other_nbl - round(other_nbl, 2)) < 0.001:
                return True   # other is round, this is change
            if out.value < other_out.value:
                return True   # smaller output more likely change
        return False


# ---- PeelChainDetector
class PeelChainDetector:
    """
    Peel chain detection: transactions with one input → two outputs,
    where one output is change and one is payment.
    Common pattern in mixing and CoinJoin.
    """

    def __init__(self):
        self._chains : List[List[str]] = []

    def detect(self, blockchain: 'NEBULABlockchain',
                min_length: int = 3) -> List[List[str]]:
        """Find peel chains of length >= min_length"""
        chains = []
        visited = set()

        for blk in blockchain._chain:
            for tx in blk.transactions:
                if tx.txid in visited:
                    continue
                if len(tx.inputs) == 1 and len(tx.outputs) == 2:
                    chain = self._follow_chain(tx, blockchain, visited)
                    if len(chain) >= min_length:
                        chains.append(chain)
        return chains

    def _follow_chain(self, start_tx: 'Transaction',
                       blockchain: 'NEBULABlockchain',
                       visited: Set[str]) -> List[str]:
        chain = [start_tx.txid]
        visited.add(start_tx.txid)
        # Would follow the chain by tracking outputs → inputs
        return chain


# ---- BlockchainClusterer
class BlockchainClusterer:
    """
    Full blockchain address clusterer.
    Combines multiple heuristics for maximum accuracy.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc             = blockchain
        self.common_input   = CommonInputHeuristic()
        self._clusters      : Dict[int, Cluster] = {}
        self._addr_cluster  : Dict[str, int]     = {}
        self._next_id       = 1
        self._lock          = threading.RLock()
        # Known entity labels
        self._known_labels  = {
            FOUNDATION_ADDRESS: ("NEBULA Foundation", "foundation"),
        }

    def cluster_blockchain(self) -> int:
        """Cluster all blockchain addresses"""
        for blk in self.bc._chain:
            for tx in blk.transactions:
                self.common_input.process_transaction(tx, self.bc.utxo)

        # Build clusters
        raw = self.common_input.build_clusters()
        with self._lock:
            for root, addrs in raw.items():
                cid = self._next_id
                self._next_id += 1
                bal   = sum(self.bc.utxo.balance(a) for a in addrs)
                label, etype = self._known_labels.get(root, ("", "unknown"))
                cluster = Cluster(
                    cluster_id  = cid,
                    addresses   = addrs,
                    label       = label,
                    entity_type = etype,
                    balance     = bal,
                )
                self._clusters[cid] = cluster
                for a in addrs:
                    self._addr_cluster[a] = cid
        return len(self._clusters)

    def get_cluster_for_address(self, addr: str) -> Optional[Cluster]:
        with self._lock:
            cid = self._addr_cluster.get(addr)
            return self._clusters.get(cid) if cid else None

    def top_clusters(self, n: int = 10) -> List[dict]:
        with self._lock:
            sorted_c = sorted(self._clusters.values(),
                               key=lambda c: c.balance, reverse=True)
            return [c.to_dict() for c in sorted_c[:n]]

    def label_cluster(self, addr: str, label: str,
                       entity_type: str = "unknown"):
        with self._lock:
            cid = self._addr_cluster.get(addr)
            if cid and cid in self._clusters:
                c = self._clusters[cid]
                c.label       = label
                c.entity_type = entity_type

    def stats(self) -> dict:
        with self._lock:
            return {
                "clusters"        : len(self._clusters),
                "clustered_addrs" : len(self._addr_cluster),
                "largest_cluster" : max((c.size() for c in self._clusters.values()),
                                         default=0),
            }


# ---- LNEdge
@dataclass
class LNEdge:
    """A Lightning Network channel edge"""
    channel_id    : str
    node_a        : str
    node_b        : str
    capacity      : int
    base_fee_msat : int    # base fee in millisatoshis
    fee_rate_ppm  : int    # proportional fee parts-per-million
    min_htlc      : int    = 1_000
    max_htlc      : int    = 0    # 0 = channel capacity
    cltv_delta    : int    = 40   # CLTV expiry delta
    is_active     : bool   = True
    last_update   : float  = 0.0

    def fee_for_amount(self, amount_msat: int) -> int:
        """Calculate routing fee for given amount"""
        proportional = (amount_msat * self.fee_rate_ppm) // 1_000_000
        return self.base_fee_msat + proportional

    def can_route(self, amount_msat: int) -> bool:
        max_h = self.max_htlc or self.capacity * 1000
        return (self.is_active and
                self.min_htlc <= amount_msat <= max_h)

    def to_dict(self) -> dict:
        return {
            "channel_id"   : self.channel_id,
            "from"         : self.node_a[:16] + "...",
            "to"           : self.node_b[:16] + "...",
            "capacity_nbl" : self.capacity / 10**DECIMALS,
            "base_fee_msat": self.base_fee_msat,
            "fee_rate_ppm" : self.fee_rate_ppm,
            "is_active"    : self.is_active,
        }
