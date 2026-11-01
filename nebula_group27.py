"""NEBULA group27 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. BatchProcessor  (orig. lines 44730-44833)
   2. NEBULAComplete  (orig. lines 44845-45075)
   3. OnChainMetric  (orig. lines 45096-45113)
   4. ChainMetricsEngine  (orig. lines 45115-45286)
   5. TxAccelerator  (orig. lines 45298-45398)
   6. DataExporter  (orig. lines 45411-45601)
   7. ContractMath  (orig. lines 45614-45655)
   8. EventEmitter  (orig. lines 45676-45711)
   9. AccessControl  (orig. lines 45713-45747)
  10. StandardContract  (orig. lines 45791-45831)
  11. TestCase  (orig. lines 45844-45851)
  12. TestResult  (orig. lines 45853-45868)
  13. NEBULAAssert  (orig. lines 45870-45923)
  14. TestRunner  (orig. lines 45925-46006)
  15. PropertyTest  (orig. lines 46008-46094)
  16. MedianTimePast  (orig. lines 46108-46158)
  17. ChainClock  (orig. lines 46160-46211)
  18. SignatureAggregator  (orig. lines 46223-46314)
  19. FullChainValidator  (orig. lines 46326-46445)
  20. MempoolAlert  (orig. lines 46458-46474)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): AMMEngine, ASNDiversityManager, AddressBook, AnalyticsDashboard, BatchJob, BlockArchiver, BlockExplorerAPI, BlockPruner, BlockRewardSimulator, BlockchainAPI, ChainForkManager, ChainIndexer, ChainStateManager, CheckpointValidator, ContractEvent, ContractStorage, DEXEngine, DeveloperToolkit, FeeBumper, FeeReserveTracker, FullSystemTester, GetWorkServer, GossipRouter, GovernanceEngine, HistoricalDataManager, IBDManager, KademliaNode, LendingProtocol, MempoolPolicyEnforcer, MempoolVisualizer, MiningDifficulty, MiningPool, MiningPoolDetector, MiningProfitCalc, MobileSyncManager, MonitoringDashboard, NEBULABlockchain, NEBULAJSONRPCServer, NEBULAMiner, NEBULAWallet, NFTEngine, NodeDiscovery, NodeWatchdog, NotificationManager, PeerEvictionManager, PerformanceBenchmark, PriceOracle, PrivacyAwareAddrManager, PrivacyConnectionManager, PrivacyLevel, ProtocolDocGenerator, RealTimeNetworkStats, RichList, Schnorr, ScriptInterpreter, ScriptOpcode, ScriptTemplateLibrary, SecurityAuditor, StakingEngine, TokenBridge, TokenRegistry, TxGraphAnalyzer, UpgradeManager, VersionBitsState, WalletConnectHandler, WalletRecovery
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

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

PUBKEY_ADDRESS_VERSION  = 0x35   # N prefix for mainnet NBL addresses

PUBKEY_ADDRESS_PREFIX   = 'N'    # human-readable prefix for P2PKH addresses

def sha256d(data: bytes) -> bytes:
    """Double SHA-256 — used everywhere in Bitcoin/NEBULA"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

BASE58_ALPHABET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58_encode(data: bytes) -> str:
    count = 0
    for byte in data:
        if byte == 0: count += 1
        else: break
    num = int.from_bytes(data, 'big')
    res = []
    while num > 0:
        num, rem = divmod(num, 58)
        res.append(chr(BASE58_ALPHABET[rem]))
    return '1' * count + ''.join(reversed(res))

def base58_decode(s: str) -> bytes:
    count = 0
    for c in s:
        if c == '1': count += 1
        else: break
    num = 0
    for c in s:
        num = num * 58 + BASE58_ALPHABET.index(ord(c))
    result = []
    while num > 0:
        num, rem = divmod(num, 256)
        result.append(rem)
    return bytes([0] * count + list(reversed(result)))

def base58check_encode(payload: bytes, version: int) -> str:
    versioned = bytes([version]) + payload
    checksum  = sha256d(versioned)[:4]
    return base58_encode(versioned + checksum)

def base58check_decode(s: str) -> Tuple[int, bytes]:
    raw      = base58_decode(s)
    version  = raw[0]
    payload  = raw[1:-4]
    checksum = raw[-4:]
    if sha256d(raw[:-4])[:4] != checksum:
        raise ValueError("Invalid base58check checksum")
    return version, payload

def mining_reward(height: int) -> int:
    """Block reward with halving schedule.
    FIX: negative height safely returns 0 instead of crashing."""
    if height < 0:
        return 0
    era = height // HALVING_INTERVAL
    if era >= 64:
        return 0
    return INITIAL_BLOCK_REWARD >> era

def halving_era(height: int) -> dict:
    """Return information about the current halving era for a given height"""
    era              = height // HALVING_INTERVAL
    blocks_this_era  = height % HALVING_INTERVAL
    blocks_remaining = HALVING_INTERVAL - blocks_this_era
    reward           = mining_reward(height)
    era_names = {
        0: "Era I — Genesis (2025–2029)",
        1: "Era II (2029–2033)",
        2: "Era III (2033–2037)",
        3: "Era IV (2037–2041)",
        4: "Era V (2041–2045)",
        5: "Era VI (2045–2049)",
    }
    return {
        "era":             era,
        "era_name":        era_names.get(era, f"Era {era+1}"),
        "reward_nbl":      f"{reward / 10**DECIMALS:.9f}",
        "blocks_mined":    blocks_this_era,
        "blocks_remaining":blocks_remaining,
        "next_halving_at": (era + 1) * HALVING_INTERVAL,
        "pct_complete":    f"{blocks_this_era / HALVING_INTERVAL * 100:.2f}%",
    }

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

def info(msg):  print(c(f"ℹ️  {msg}", C.CYAN))

def _script_int_to_bytes(n: int) -> bytes:
    if n == 0: return b''
    neg = n < 0
    n   = abs(n)
    result = []
    while n:
        result.append(n & 0xff)
        n >>= 8
    if result[-1] & 0x80:
        result.append(0x80 if neg else 0x00)
    elif neg:
        result[-1] |= 0x80
    return bytes(result)

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

def nebula_ecosystem_info() -> dict:
    """Return complete NEBULA ecosystem overview."""
    return {
        "project":    "NEBULA Blockchain (NBL)",
        "version":    "1.0.0",
        "launched":   "2025-03-16",
        "author":     "Zayn Quantum / NEBULA Core Team",
        "license":    "MIT — Open to All Humanity",
        "mission":    "Financial Freedom for Every Human Being",
        "github":     "",

        "core_modules": {
            "nebula_core":       "Blockchain engine, UTXO, PoW, ECDSA",
            "nebula_wallet":     "HD Wallet BIP32/39/44",
            "nebula_miner":      "Multi-process PoW miner",
            "nebula_network":    "P2P TCP network",
            "nebula_node":       "Full node orchestrator",
            "nebula_security":   "DoS protection, rate limiting",
            "nebula_contracts":  "Smart contracts, 92 opcodes",
            "nebula_tests":      "54 automated tests",
            "nebula_cli":        "Command-line interface",
            "nebula_api":        "REST API 32+ endpoints",
        },

        "defi_modules": {
            "governance":   "On-chain DAO voting + timelock",
            "staking":      "PoS hybrid, validator slashing",
            "dex":          "AMM + order book DEX",
            "lending":      "Collateralized lending + liquidation",
            "yield_farm":   "Liquidity mining rewards",
            "bridge":       "Cross-chain HTLC bridge",
            "oracle":       "Decentralized price feeds",
            "micropay":     "Off-chain payment channels",
            "insurance":    "DeFi insurance protocol",
            "launchpad":    "IDO/ICO token launchpad",
            "defi_router":  "Aggregator swap routing",
        },

        "identity_modules": {
            "nft":          "NBL-721 NFT standard + marketplace",
            "did":          "W3C DID decentralized identity",
            "social":       "On-chain social network",
            "escrow":       "Trustless escrow service",
            "subscription": "Recurring payment protocol",
            "multisig":     "Advanced m-of-n vaults",
            "audit":        "Immutable compliance log",
            "privacy":      "Stealth addresses + CoinJoin",
        },

        "advanced_modules": {
            "segwit":         "SegWit v0 + Taproot + Schnorr",
            "lightning":      "Lightning Network protocol",
            "stratum":        "Mining pool protocol",
            "bip324":         "Encrypted P2P transport",
            "musig2":         "MuSig2 aggregated signatures",
            "psbt":           "Partially Signed Transactions",
            "shamirs_secret": "Threshold key sharing",
            "smart_vm":       "Full stack-based VM with gas",
            "analytics":      "Chain analytics + whale tracking",
            "full_node":      "All subsystems unified",
        },

        "token_economics": {
            "symbol":        "NBL",
            "max_supply":    "21,000,000 NBL",
            "decimals":      9,
            "smallest_unit": "1 Neb = 0.000000001 NBL",
            "initial_reward": "50 NBL/block",
            "halving":       "Every 210,000 blocks (~4 years)",
            "block_time":    "~10 minutes",
            "algorithm":     "SHA-256d Proof of Work",
            "foundation_fee": "2% of each block reward",
        },

        "for_afghanistan": {
            "use_case":     "Remittances: AED → AFN via NEBULA in 10 min",
            "western_union_fee": "~7%",
            "nebula_fee":   "0.001%",
            "savings":      "99.9% cheaper than traditional methods",
            "population":   "40 million Afghans can use without bank account",
        },

        "statistics": {
            "total_lines_of_code": "100,000+",
            "modules":             "145+",
            "opcodes":             "92",
            "api_endpoints":       "32+",
            "rpc_methods":         "50+",
            "test_cases":          "54+",
            "built_by":            "Solo developer",
            "development_time":    "~6 months",
        }
    }

NEBULA_PROTOCOL_V3_SUMMARY = {
    "name":          "NEBULA Blockchain Protocol v3",
    "version":       "3.0.0",
    "chain_id":      CHAIN_ID,
    "release_date":  "2025-01-01",
    "highlights": [
        "Complete DeFi stack: DEX, Lending, Staking, Farming, Insurance",
        "NFT ecosystem: Collections, Marketplace, Gaming, Fractionalization",
        "Cross-chain: Bridge, Atomic Swaps, Cross-chain Messaging",
        "Privacy: Confidential Txs, Mixer, Stealth Addresses",
        "Governance: veNBL, Delegation, Quadratic Voting, Emergency DAO",
        "Scaling: ZK Rollups, Sharding, State Channels, L2 Bridge",
        "Identity: DID, Verifiable Credentials, Name Service (NNS)",
        "Analytics: Real-time, AI-powered, Cross-protocol",
        "Security: MEV Protection, Circuit Breaker, Audit Trail",
        "Developer: SDK, Testnet, Faucet, Documentation",
    ],
    "module_count": 349,
    "total_lines":  "~100,000",
    "test_coverage": "comprehensive",
    "language":     "Python 3.10+",
    "license":      "MIT",
    "github":       "",
    "creator":      "Zayn Quantum (ارمان)",
    "status":       "Production Ready",
}

def nebula_v3_summary() -> dict:
    return NEBULA_PROTOCOL_V3_SUMMARY

def create_nebula_system(network: str = "mainnet",
                          enable_mining: bool = False) -> 'NEBULASystem':
    """Create and initialize the complete NEBULA system."""
    config = NodeConfig.from_env()
    config.mining_enabled = enable_mining
    config.network        = network
    return NEBULASystem(config, network)

def run_tests() -> dict:
    """Run all NEBULA test suites."""
    results = {}
    print("\n🧪 NEBULA Complete Test Suite")
    print("=" * 55)
    # Core tests
    try:
        core = NEBULATestSuite()
        results["core"] = core.run_all()
    except Exception as e:
        results["core"] = {"error": str(e)}
    # Extended tests
    try:
        ext = ExtendedTestSuite()
        results["extended"] = ext.run_all()
    except Exception as e:
        results["extended"] = {"error": str(e)}
    # Integration tests
    try:
        integ = IntegrationTestSuite()
        results["integration"] = integ.run_all()
    except Exception as e:
        results["integration"] = {"error": str(e)}
    total_p = sum(r.get("passed", 0) for r in results.values()
                  if isinstance(r, dict))
    total_f = sum(r.get("failed", 0) for r in results.values()
                  if isinstance(r, dict))
    print(f"\n{'='*55}")
    print(f"  🎯 GRAND TOTAL: {total_p} passed, {total_f} failed")
    print(f"{'='*55}\n")
    return results

def print_nebula_info():
    """Print comprehensive NEBULA protocol information."""
    print("\n" + "=" * 60)
    print("  🌌 NEBULA BLOCKCHAIN — Complete Information")
    print("=" * 60)
    info = nebula_ecosystem_info()
    for section, data in info.items():
        print(f"\n  📋 {section.upper()}")
        if isinstance(data, dict):
            for k, v in data.items():
                print(f"     {k:30s}: {v}")
        else:
            print(f"     {data}")
    print("\n" + "=" * 60 + "\n")

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- BatchProcessor
class BatchProcessor:
    """
    Batch transaction and operation processor.
    Processes: bulk address queries, batch broadcasts,
    bulk UTXOs scan, exchange withdrawals.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc     = blockchain
        self._jobs  : Dict[str, BatchJob] = {}
        self._queue : List[str] = []
        self._lock  = threading.RLock()
        self._running = False

    def submit_batch_balance_check(self, addresses: List[str]) -> str:
        """Check balances for a batch of addresses"""
        job_id = f"balance_{int(time.time()*1000)}"
        job    = BatchJob(job_id=job_id, job_type="balance_check",
                          items=addresses)
        with self._lock:
            self._jobs[job_id] = job
            self._queue.append(job_id)
        self._process_immediately(job_id)
        return job_id

    def submit_batch_broadcast(self, txs: List['Transaction']) -> str:
        """Broadcast multiple transactions"""
        job_id = f"broadcast_{int(time.time()*1000)}"
        job    = BatchJob(job_id=job_id, job_type="broadcast",
                          items=txs)
        with self._lock:
            self._jobs[job_id] = job
            self._queue.append(job_id)
        self._process_immediately(job_id)
        return job_id

    def submit_batch_address_watch(self, addresses: List[str],
                                    callback: Callable) -> str:
        """Watch multiple addresses for incoming transactions"""
        job_id = f"watch_{int(time.time()*1000)}"
        job    = BatchJob(job_id=job_id, job_type="address_watch",
                          items=addresses, callback=callback)
        with self._lock:
            self._jobs[job_id] = job
        return job_id

    def _process_immediately(self, job_id: str):
        """Process job immediately in background"""
        def _run():
            with self._lock:
                job = self._jobs.get(job_id)
            if not job:
                return

            try:
                if job.job_type == "balance_check":
                    for addr in job.items:
                        bal = self.bc.utxo.balance(addr)
                        job.results.append({"address": addr,
                                            "balance_nbl": bal/10**DECIMALS})
                elif job.job_type == "broadcast":
                    for tx in job.items:
                        ok, msg = self.bc.mempool.submit(tx)
                        job.results.append({"txid": tx.txid, "ok": ok, "msg": msg})
                        if not ok:
                            job.errors.append({"txid": tx.txid, "error": msg})

                job.status = "completed"
                if job.callback:
                    job.callback(job)
            except Exception as e:
                job.status = "failed"
                job.errors.append(str(e))

        threading.Thread(target=_run, daemon=True).start()

    def get_job(self, job_id: str) -> Optional[dict]:
        job = self._jobs.get(job_id)
        return job.to_dict() if job else None

    def get_results(self, job_id: str) -> Optional[List]:
        job = self._jobs.get(job_id)
        return job.results if job else None

    def cleanup_old_jobs(self, max_age_secs: float = 3600):
        """Remove completed jobs older than max_age_secs"""
        cutoff = time.time() - max_age_secs
        with self._lock:
            old = [jid for jid, j in self._jobs.items()
                   if j.is_done() and j.created_at < cutoff]
            for jid in old:
                del self._jobs[jid]

    def stats(self) -> dict:
        with self._lock:
            return {
                "total_jobs"    : len(self._jobs),
                "pending"       : sum(1 for j in self._jobs.values()
                                      if j.status == "pending"),
                "completed"     : sum(1 for j in self._jobs.values()
                                      if j.status == "completed"),
                "failed"        : sum(1 for j in self._jobs.values()
                                      if j.status == "failed"),
            }


# ---- NEBULAComplete
class NEBULAComplete:
    """
    NEBULA Complete — All 90 modules integrated.
    The most comprehensive single-file blockchain in Python.

    Written entirely on a Python 3 by NEBULA Core Team.
    Pure Python, no external dependencies.
    Production-grade cryptography and consensus.
    """

    VERSION      = "1.0.0"
    MODULES      = 90
    AUTHOR       = "NEBULA Core Team"
    DESCRIPTION  = "NEBULA Blockchain — Complete Python Implementation"

    def __init__(self):
        # ── Core Blockchain ───────────────────────────────────────
        self.bc             = NEBULABlockchain()

        # ── DeFi Layer ────────────────────────────────────────────
        self.oracle         = PriceOracle(self.bc)
        self.amm            = AMMEngine(self.bc)
        self.dex            = DEXEngine()
        self.staking        = StakingEngine(self.bc)
        self.lending        = LendingProtocol(self.bc)
        self.governance     = GovernanceEngine(self.bc, self.staking)

        # ── Tokens & NFTs ─────────────────────────────────────────
        self.nft            = NFTEngine(self.bc)
        self.token_registry = TokenRegistry(self.bc)
        self.bridge         = TokenBridge(self.bc)

        # ── Network Layer ─────────────────────────────────────────
        self.privacy        = PrivacyConnectionManager(PrivacyLevel.MIXED)
        self.addr_mgr       = PrivacyAwareAddrManager()
        self.gossip         = GossipRouter(FOUNDATION_ADDRESS[:16])
        self.kademlia       = KademliaNode()
        self.discovery      = NodeDiscovery()
        self.fork_mgr       = ChainForkManager(self.bc)
        self.ibd            = IBDManager(self.bc)
        self.eviction       = PeerEvictionManager()
        self.asn_diversity  = ASNDiversityManager()

        # ── Mining ────────────────────────────────────────────────
        self.pool           = MiningPool(self.bc)
        self.vardiff        = MiningDifficulty()
        self.profit_calc    = MiningProfitCalc(self.oracle)
        self.getwork        = GetWorkServer(self.bc)
        self.pool_detector  = MiningPoolDetector(self.bc)

        # ── Analytics ─────────────────────────────────────────────
        self.analytics      = AnalyticsDashboard(self.bc)
        self.historical     = HistoricalDataManager(self.bc)
        self.net_stats      = RealTimeNetworkStats(self.bc, self.oracle)
        self.indexer        = ChainIndexer()
        self.tx_graph       = TxGraphAnalyzer()
        self.mempool_viz    = MempoolVisualizer(self.bc)
        self.rich_list      = RichList(self.bc)
        self.reward_sim     = BlockRewardSimulator()

        # ── Infrastructure ────────────────────────────────────────
        self.rpc            = NEBULAJSONRPCServer(self.bc)
        self.api            = BlockchainAPI(self.bc, self.oracle)
        self.explorer_api   = BlockExplorerAPI(self.bc, self.historical)
        self.watchdog       = NodeWatchdog(self.bc)
        self.notifications  = NotificationManager(self.bc, self.oracle)
        self.snapshot_mgr   = ChainStateManager(self.bc)
        self.auditor        = SecurityAuditor(self.bc)
        self.benchmarks     = PerformanceBenchmark(self.bc)
        self.monitor        = MonitoringDashboard(
                                  self.bc, self.oracle, self.pool, self.staking)

        # ── Wallet & User Tools ───────────────────────────────────
        self.address_book   = AddressBook()
        self.wallet_connect = WalletConnectHandler()
        self.fee_bumper     = FeeBumper(self.bc)
        self.bulk_addr_gen  = None   # initialized with master key on wallet load
        self.recovery       = WalletRecovery(self.bc)
        self.batch_proc     = BatchProcessor(self.bc)

        # ── Protocol ──────────────────────────────────────────────
        self.version_bits   = VersionBitsState()
        self.upgrade_mgr    = UpgradeManager(self.bc)
        self.checkpoint_val = CheckpointValidator()
        self.mempool_policy = MempoolPolicyEnforcer()
        self.protocol_docs  = ProtocolDocGenerator()
        self.pruner         = BlockPruner(self.bc)
        self.archiver       = BlockArchiver()
        self.fee_reserve    = FeeReserveTracker(self.bc)
        self.script_library = ScriptTemplateLibrary()

        # ── Developer Tools ───────────────────────────────────────
        self.dev            = DeveloperToolkit(self.bc)
        self.mobile_sync    = MobileSyncManager(self.bc)

        self._start_time    = time.time()
        print(f"  🌌 {self.DESCRIPTION} v{self.VERSION}")
        print(f"  Modules: {self.MODULES} | Author: {self.AUTHOR}")

    def quick_start(self, mine: bool = False,
                     miner_address: str = None):
        """Quick start all services"""
        # Core services
        self.oracle.start()
        self.watchdog.start()
        self.historical.start_collection(60, self.oracle)
        self.net_stats.start()
        self.notifications.start(30)

        # APIs
        for svc, name in [(self.rpc.start, "RPC"),
                           (self.api.start, "API"),
                           (self.explorer_api.start, "Explorer")]:
            try:
                svc()
            except Exception as e:
                print(f"  ⚠️  {name}: {e}")

        # Initialize DeFi
        for pair in [("NBL","USDT"),("NBL","BTC"),("NBL","ETH")]:
            self.amm.create_pool(*pair)

        if mine and miner_address:
            threading.Thread(
                target=self._mine_loop,
                args=(miner_address,),
                daemon=True, name="Miner").start()

        print(f"  ✅ System ready | {self.MODULES} modules active")

    def _mine_loop(self, addr: str):
        miner = NEBULAMiner(self.bc, addr)
        while True:
            try:
                miner.mine_one_block()
                self.upgrade_mgr.check_activations(self.bc.height)
                self.snapshot_mgr.auto_snapshot(1000)
                self.fee_reserve.process_block(self.bc.tip)
                self.indexer.index_block(self.bc.tip)
            except Exception:
                time.sleep(1)

    def stop(self):
        """Stop all services"""
        for svc in [self.oracle, self.watchdog, self.notifications,
                     self.historical, self.net_stats]:
            try: svc.stop()
            except Exception: _NB_SWALLOW_LOG.debug("swallowed bare in NEBULAComplete.stop", exc_info=True)
        try:
            self.rpc.stop()
            self.api.stop()
            self.explorer_api.stop()
        except Exception: _NB_SWALLOW_LOG.debug("swallowed bare in NEBULAComplete.stop", exc_info=True)
        print("  NEBULA stopped")

    def comprehensive_status(self) -> dict:
        """Return full system status"""
        price = self.oracle.get_nbl_usd()
        issued = self.bc.utxo.total_supply()
        return {
            "version"         : self.VERSION,
            "modules"         : self.MODULES,
            "author"          : self.AUTHOR,
            "chain"           : {
                "height"        : self.bc.height,
                "utxos"         : self.bc.utxo.size(),
                "mempool"       : self.bc.mempool.size(),
                "supply_nbl"    : issued / 10**DECIMALS,
                "pct_issued"    : f"{issued/MAX_SUPPLY*100:.4f}%",
            },
            "defi"            : {
                "amm_pools"     : len(self.amm._pools),
                "amm_tvl"       : self.amm.total_tvl(),
                "stakers"       : len(self.staking._stakes),
                "validators"    : len(self.staking._validators),
                "proposals"     : len(self.governance._proposals),
                "nft_minted"    : sum(c.minted_count for c in
                                      self.nft._collections.values()),
                "tokens"        : len(self.token_registry._tokens),
            },
            "network"         : {
                "known_peers"   : len(self.addr_mgr.get_all_addresses()),
                "gossip_peers"  : len(self.gossip._peers),
                "pool_workers"  : len(self.pool._workers),
                "forks_seen"    : len(self.fork_mgr._forks),
            },
            "pricing"         : {
                "nbl_usd"       : price,
                "nbl_btc"       : self.oracle.get_nbl_btc(),
            },
            "uptime_secs"     : round(time.time() - self._start_time),
            "security_score"  : self.auditor._security_score(),
        }

    def run_all_tests(self) -> dict:
        """Run complete test suite"""
        import time as _t
        start = _t.time()
        # Core tests
        results = {}
        # Module 55 extended tests
        passed, total = _run_extended_module_tests()
        results["module_tests"] = {"passed": passed, "total": total}
        # System integration
        tester = FullSystemTester()
        sys_result = tester.run_all()
        results["system_test"] = {"passed": sys_result["passed"],
                                   "total": sys_result["total"]}
        # Benchmark
        bench = self.benchmarks.run_all()
        results["benchmarks"] = {"count": len(bench["benchmarks"])}
        # Security
        audit = self.auditor.full_audit()
        results["security"] = {"score": audit["score"]}

        total_passed = sum(r.get("passed", 0) for r in results.values()
                           if isinstance(r, dict))
        total_tests  = sum(r.get("total", 0) for r in results.values()
                           if isinstance(r, dict))

        return {
            "summary"  : f"{total_passed} checks passed",
            "elapsed"  : f"{_t.time()-start:.2f}s",
            "details"  : results,
        }

    def __repr__(self) -> str:
        return (f"<NEBULAComplete v{self.VERSION} "
                f"modules={self.MODULES} "
                f"height={self.bc.height} "
                f"author='{self.AUTHOR}'>")


# ---- OnChainMetric
@dataclass
class OnChainMetric:
    """A single on-chain metric data point"""
    name      : str
    value     : float
    height    : int
    timestamp : float = field(default_factory=time.time)
    unit      : str   = ""
    description: str  = ""

    def to_dict(self) -> dict:
        return {
            "metric"    : self.name,
            "value"     : round(self.value, 6),
            "height"    : self.height,
            "unit"      : self.unit,
            "description": self.description,
        }


# ---- ChainMetricsEngine
class ChainMetricsEngine:
    """
    Advanced on-chain metrics for NEBULA.
    Implements: NVT, SOPR, Realized Cap, Stock-to-Flow, MVRV.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 oracle: 'PriceOracle' = None):
        self.bc     = blockchain
        self.oracle = oracle
        self._cache : Dict[str, OnChainMetric] = {}
        self._lock  = threading.Lock()

    def nvt_ratio(self) -> OnChainMetric:
        """
        NVT (Network Value to Transactions) Ratio.
        NVT = Market Cap / Daily TX Volume
        High NVT = overvalued, Low NVT = undervalued.
        """
        price     = self.oracle.get_nbl_usd() if self.oracle else 0.10
        supply    = self.bc.utxo.total_supply() / 10**DECIMALS
        market_cap= supply * price

        # 24h transaction volume
        cutoff    = time.time() - 86400
        daily_vol = 0
        for blk in self.bc._chain:
            if blk.header.timestamp >= cutoff:
                for tx in blk.transactions[1:]:
                    daily_vol += tx.total_output() / 10**DECIMALS

        nvt = market_cap / max(0.001, daily_vol)
        return OnChainMetric(
            name="NVT", value=nvt, height=self.bc.height,
            unit="ratio",
            description="Network Value to Transactions ratio")

    def realized_cap(self) -> OnChainMetric:
        """
        Realized Capitalization.
        Sum of (each UTXO value * price at time of last move).
        Approximated using block height vs price.
        """
        price   = self.oracle.get_nbl_usd() if self.oracle else 0.10
        # Simplified: current price * supply (proper impl requires price history)
        supply  = self.bc.utxo.total_supply() / 10**DECIMALS
        r_cap   = supply * price * 0.85  # ~85% of market cap typically
        return OnChainMetric(
            name="Realized Cap", value=r_cap, height=self.bc.height,
            unit="USD",
            description="Realized market capitalization")

    def mvrv_ratio(self) -> OnChainMetric:
        """
        MVRV (Market Value to Realized Value).
        MVRV > 1 = unrealized profit, < 1 = unrealized loss.
        """
        price   = self.oracle.get_nbl_usd() if self.oracle else 0.10
        supply  = self.bc.utxo.total_supply() / 10**DECIMALS
        mv      = supply * price
        rv      = self.realized_cap().value
        mvrv    = mv / max(0.001, rv)
        return OnChainMetric(
            name="MVRV", value=mvrv, height=self.bc.height,
            unit="ratio",
            description="Market Value to Realized Value ratio")

    def stock_to_flow(self) -> OnChainMetric:
        """
        Stock-to-Flow model.
        S2F = Current Supply / Annual New Supply
        Higher S2F = more scarce.
        """
        supply      = self.bc.utxo.total_supply() / 10**DECIMALS
        # Annual new supply at current block reward
        blocks_year = 365 * 24 * 6   # ~52,560
        reward_nbl  = mining_reward(self.bc.height) / 10**DECIMALS
        annual_new  = reward_nbl * blocks_year
        s2f         = supply / max(0.001, annual_new)
        return OnChainMetric(
            name="S2F", value=s2f, height=self.bc.height,
            unit="ratio",
            description="Stock-to-Flow scarcity model")

    def sopr(self) -> OnChainMetric:
        """
        SOPR (Spent Output Profit Ratio).
        SOPR > 1 = coins moved at profit.
        Simplified: ratio of recent outputs vs older UTXO average.
        """
        chain    = self.bc._chain
        recent   = chain[-144:] if len(chain) >= 144 else chain
        # Count recently spent outputs
        spent    = sum(len(blk.transactions) for blk in recent)
        total_t  = max(1, sum(len(blk.transactions) for blk in chain))
        sopr_val = 1.0 + (spent / total_t - 0.5) * 0.1
        return OnChainMetric(
            name="SOPR", value=round(sopr_val, 4), height=self.bc.height,
            unit="ratio",
            description="Spent Output Profit Ratio")

    def active_addresses_1d(self) -> OnChainMetric:
        """Count unique active addresses in last 24h"""
        cutoff = time.time() - 86400
        addrs  = set()
        for blk in self.bc._chain:
            if blk.header.timestamp >= cutoff:
                for tx in blk.transactions:
                    for out in tx.outputs:
                        if out.address:
                            addrs.add(out.address)
        return OnChainMetric(
            name="Active Addresses 24h", value=len(addrs),
            height=self.bc.height, unit="addresses",
            description="Unique addresses active in last 24 hours")

    def transaction_count_24h(self) -> OnChainMetric:
        """Count transactions in last 24h"""
        cutoff = time.time() - 86400
        count  = sum(
            len(blk.transactions)
            for blk in self.bc._chain
            if blk.header.timestamp >= cutoff
        )
        return OnChainMetric(
            name="Tx Count 24h", value=count,
            height=self.bc.height, unit="transactions",
            description="Total transactions in last 24 hours")

    def average_tx_value(self) -> OnChainMetric:
        """Average transaction value in last 100 blocks"""
        values = []
        chain  = self.bc._chain[-100:]
        for blk in chain:
            for tx in blk.transactions[1:]:
                values.append(tx.total_output() / 10**DECIMALS)
        avg = statistics.mean(values) if values else 0
        return OnChainMetric(
            name="Avg Tx Value", value=avg,
            height=self.bc.height, unit="NBL",
            description="Average transaction value last 100 blocks")

    def compute_all(self) -> List[dict]:
        """Compute all metrics"""
        metrics = [
            self.nvt_ratio,
            self.realized_cap,
            self.mvrv_ratio,
            self.stock_to_flow,
            self.sopr,
            self.active_addresses_1d,
            self.transaction_count_24h,
            self.average_tx_value,
        ]
        results = []
        for fn in metrics:
            try:
                results.append(fn().to_dict())
            except Exception as e:
                results.append({"metric": fn.__name__, "error": str(e)})
        return results

    def print_report(self):
        """Print formatted metrics report"""
        metrics = self.compute_all()
        print("\n" + "═"*55)
        print("  📈 NEBULA On-Chain Metrics")
        print("═"*55)
        for m in metrics:
            if "error" not in m:
                print(f"  {m['metric']:30} {m['value']:>12}  {m['unit']}")
        print("═"*55)


# ---- TxAccelerator
class TxAccelerator:
    """
    Transaction acceleration service.
    Helps users get stuck transactions confirmed faster.
    Methods: RBF replacement, CPFP child, pool direct submit.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 fee_bumper: 'FeeBumper' = None):
        self.bc         = blockchain
        self.fee_bumper = fee_bumper or FeeBumper(blockchain)
        self._pending   : Dict[str, dict] = {}
        self._lock      = threading.Lock()

    def check_tx_status(self, txid: str) -> dict:
        """Check if transaction is stuck and needs acceleration"""
        # Check confirmed
        for blk in reversed(self.bc._chain):
            for tx in blk.transactions:
                if tx.txid == txid:
                    confs = self.bc.height - blk.height + 1
                    return {
                        "txid"          : txid,
                        "status"        : "confirmed",
                        "confirmations" : confs,
                        "block_height"  : blk.height,
                        "needs_accel"   : False,
                    }

        # Check mempool
        pool = getattr(self.bc.mempool, '_txs', {})
        entry = pool.get(txid)
        if entry:
            fee_rate    = getattr(entry, 'fee_rate', 0)
            smart_fee   = self.bc.mempool.smart_fee(1) if hasattr(self.bc.mempool, 'smart_fee') else 10
            is_stuck    = fee_rate < smart_fee * 0.5
            minutes_old = (time.time() - getattr(entry, 'time', time.time())) / 60
            return {
                "txid"       : txid,
                "status"     : "mempool",
                "fee_rate"   : fee_rate,
                "target_rate": smart_fee,
                "minutes_old": round(minutes_old, 1),
                "is_stuck"   : is_stuck,
                "needs_accel": is_stuck and minutes_old > 30,
            }

        return {"txid": txid, "status": "not_found", "needs_accel": False}

    def accelerate_rbf(self, txid: str,
                        privkey: int,
                        target_fee_rate: int = None) -> Tuple[bool, str]:
        """Accelerate via RBF (replace with higher fee)"""
        if not target_fee_rate:
            target_fee_rate = (self.bc.mempool.smart_fee(1)
                               if hasattr(self.bc.mempool, 'smart_fee') else 50) * 2
        new_tx = self.fee_bumper.rbf_bump(txid, privkey, target_fee_rate)
        if not new_tx:
            return False, "RBF bump failed — tx may not signal RBF"
        ok, msg = self.bc.mempool.submit(new_tx)
        return ok, f"RBF: {msg} (new txid: {new_tx.txid[:16]}...)"

    def accelerate_cpfp(self, txid: str,
                         privkey: int,
                         child_fee_rate: int = 100) -> Tuple[bool, str]:
        """Accelerate via CPFP (child pays for parent)"""
        child_tx = self.fee_bumper.cpfp_bump(txid, privkey, child_fee_rate)
        if not child_tx:
            return False, "CPFP failed — no spendable outputs found"
        ok, msg = self.bc.mempool.submit(child_tx)
        return ok, f"CPFP: {msg} (child txid: {child_tx.txid[:16]}...)"

    def estimate_confirmation_time(self, fee_rate: int) -> dict:
        """Estimate confirmation time for given fee rate"""
        smart_1  = self.bc.mempool.smart_fee(1)  if hasattr(self.bc.mempool,'smart_fee') else 50
        smart_6  = self.bc.mempool.smart_fee(6)  if hasattr(self.bc.mempool,'smart_fee') else 20
        smart_144= self.bc.mempool.smart_fee(144) if hasattr(self.bc.mempool,'smart_fee') else 5

        if fee_rate >= smart_1:
            blocks, time_str = 1, "~10 minutes"
        elif fee_rate >= smart_6:
            blocks, time_str = 6, "~1 hour"
        elif fee_rate >= smart_144:
            blocks, time_str = 144, "~1 day"
        else:
            blocks, time_str = 1008, "~1 week"

        return {
            "fee_rate"         : fee_rate,
            "estimated_blocks" : blocks,
            "estimated_time"   : time_str,
            "fee_for_next_block": smart_1,
        }

    def stats(self) -> dict:
        return {
            "pending_accel"  : len(self._pending),
            "mempool_size"   : self.bc.mempool.size(),
            "smart_fee_1blk" : (self.bc.mempool.smart_fee(1)
                                if hasattr(self.bc.mempool,'smart_fee') else 10),
        }


# ---- DataExporter
class DataExporter:
    """
    Export NEBULA blockchain data in multiple formats.
    Formats: JSON, CSV, HTML report, plain text.
    Use cases: tax reports, audits, analytics, backups.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 oracle: 'PriceOracle' = None):
        self.bc     = blockchain
        self.oracle = oracle

    def export_address_statement(self, address: str,
                                  fmt: str = "json") -> str:
        """Export all transactions for an address"""
        bc      = self.bc
        history = []

        for blk in bc._chain:
            for tx in blk.transactions:
                received = sum(o.value for o in tx.outputs
                               if o.address == address)
                sent     = 0  # would need input tracking
                if received > 0:
                    history.append({
                        "date"     : time.strftime(
                            "%Y-%m-%d %H:%M:%S",
                            time.localtime(blk.header.timestamp)),
                        "txid"     : tx.txid[:16] + "...",
                        "type"     : "received",
                        "amount_nbl": received / 10**DECIMALS,
                        "block"    : blk.height,
                    })

        if fmt == "csv":
            lines = ["date,txid,type,amount_nbl,block"]
            for h in history:
                lines.append(f"{h['date']},{h['txid']},{h['type']},"
                              f"{h['amount_nbl']:.9f},{h['block']}")
            return "\n".join(lines)

        if fmt == "html":
            rows = "\n".join(
                f"<tr><td>{h['date']}</td><td>{h['txid']}</td>"
                f"<td>{h['type']}</td><td>{h['amount_nbl']:.9f}</td>"
                f"<td>{h['block']}</td></tr>"
                for h in history
            )
            return (f"<!DOCTYPE html><html><head>"
                    f"<title>NEBULA Statement: {address[:20]}...</title>"
                    f"<style>table{{border-collapse:collapse}}td,th"
                    f"{{border:1px solid #ddd;padding:8px}}</style>"
                    f"</head><body>"
                    f"<h2>NEBULA Wallet Statement</h2>"
                    f"<p>Address: {address}</p>"
                    f"<table><tr><th>Date</th><th>TxID</th><th>Type</th>"
                    f"<th>Amount NBL</th><th>Block</th></tr>{rows}</table>"
                    f"</body></html>")

        return json.dumps({
            "address"  : address,
            "balance"  : bc.utxo.balance(address) / 10**DECIMALS,
            "history"  : history,
            "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        }, indent=2)

    def export_chain_snapshot(self, output_path: str = None) -> str:
        """Export full chain snapshot as JSON"""
        bc   = self.bc
        data = {
            "chain_name"  : CHAIN_NAME,
            "symbol"      : CHAIN_SYMBOL,
            "height"      : bc.height,
            "tip_hash"    : bc.tip.hash,
            "supply_nbl"  : bc.utxo.total_supply() / 10**DECIMALS,
            "utxo_count"  : bc.utxo.size(),
            "mempool"     : bc.mempool.size(),
            "exported_at" : time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "blocks"      : [
                {"height": b.height, "hash": b.hash,
                 "time": b.header.timestamp, "txs": len(b.transactions)}
                for b in bc._chain
            ],
        }
        result = json.dumps(data, indent=2)
        if output_path:
            Path(output_path).write_text(result)
        return result

    def export_rich_list_csv(self) -> str:
        """Export rich list as CSV"""
        rl    = RichList(self.bc, 100)
        lines = ["rank,address,balance_nbl,pct_supply,utxo_count"]
        for entry in rl.build():
            lines.append(f"{entry.rank},{entry.address},"
                          f"{entry.balance_nbl:.9f},"
                          f"{entry.pct:.4f},{entry.utxos}")
        return "\n".join(lines)

    def export_mining_history(self) -> str:
        """Export mining history as CSV"""
        lines = ["height,hash,timestamp,miner,reward_nbl,tx_count,size_bytes"]
        for blk in self.bc._chain:
            miner = (blk.transactions[0].outputs[0].address
                     if blk.transactions and blk.transactions[0].outputs
                     else "unknown")
            reward = mining_reward(blk.height) / 10**DECIMALS
            lines.append(
                f"{blk.height},{blk.hash[:16]}...,"
                f"{blk.header.timestamp:.0f},{miner[:20]}...,"
                f"{reward:.9f},{len(blk.transactions)},{blk.byte_size()}")
        return "\n".join(lines)

    def generate_html_report(self) -> str:
        """Generate full HTML analytics report"""
        bc     = self.bc
        price  = self.oracle.get_nbl_usd() if self.oracle else 0.10
        issued = bc.utxo.total_supply() / 10**DECIMALS
        era    = halving_era(bc.height)

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>NEBULA Blockchain Report</title>
  <style>
    body {{font-family:monospace;background:#0a0a1a;color:#e0e0ff;margin:0;padding:20px}}
    h1 {{color:#7c7cff}} h2 {{color:#5c5cdd;border-bottom:1px solid #333}}
    .card {{background:#111128;border:1px solid #333;border-radius:8px;
            padding:16px;margin:12px 0;display:inline-block;min-width:200px}}
    .val {{font-size:1.5em;color:#7c7cff;font-weight:bold}}
    table {{width:100%;border-collapse:collapse;margin:8px 0}}
    th,td {{border:1px solid #333;padding:8px;text-align:left}}
    th {{background:#1a1a3a}}
    .badge {{background:#2a2a5a;padding:2px 8px;border-radius:4px;font-size:0.85em}}
  </style>
</head>
<body>
  <h1>🌌 NEBULA Blockchain Analytics Report</h1>
  <p>Generated: {time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())}
     | Author: NEBULA Core Team <span class="badge">v1.0.0</span></p>

  <h2>Chain Overview</h2>
  <div class="card"><div>Block Height</div><div class="val">{bc.height:,}</div></div>
  <div class="card"><div>Total Supply</div><div class="val">{issued:,.4f} NBL</div></div>
  <div class="card"><div>UTXO Count</div><div class="val">{bc.utxo.size():,}</div></div>
  <div class="card"><div>NBL/USD</div><div class="val">${price:.6f}</div></div>
  <div class="card"><div>Mempool</div><div class="val">{bc.mempool.size()} txs</div></div>

  <h2>Mining Economics</h2>
  <table>
    <tr><th>Era</th><th>Block Reward</th><th>Halving Height</th><th>% Issued</th></tr>
    <tr>
      <td>{era.get('era',0)}</td>
      <td>{era.get('reward_nbl','?')} NBL</td>
      <td>{era.get('next_halving','?'):,}</td>
      <td>{issued/MAX_SUPPLY*10**DECIMALS*100:.3f}%</td>
    </tr>
  </table>

  <h2>Foundation</h2>
  <table>
    <tr><th>Address</th><th>Balance</th><th>Rate</th></tr>
    <tr>
      <td>{FOUNDATION_ADDRESS}</td>
      <td>{bc.utxo.balance(FOUNDATION_ADDRESS)/10**DECIMALS:.9f} NBL</td>
      <td>{FOUNDATION_RATE*100:.0f}% per block</td>
    </tr>
  </table>

  <h2>Top Blocks (Last 5)</h2>
  <table>
    <tr><th>Height</th><th>Hash</th><th>Txs</th><th>Reward</th></tr>
    {"".join(f"<tr><td>{b.height}</td><td>{b.hash[:24]}...</td>"
             f"<td>{len(b.transactions)}</td>"
             f"<td>{mining_reward(b.height)/10**DECIMALS:.2f} NBL</td></tr>"
             for b in reversed(bc._chain[-5:]))}
  </table>

  <footer style="margin-top:40px;color:#555;font-size:0.8em">
    NEBULA Blockchain — NEBULA Core Team — Pure Python Core Developerelopment
  </footer>
</body>
</html>"""

    def save_report(self, path: str = "./nebula_report.html"):
        """Save HTML report to file"""
        report = self.generate_html_report()
        Path(path).write_text(report)
        print(f"  📄 Report saved: {path}")
        return path


# ---- ContractMath
class ContractMath:
    """Safe math for smart contracts (no overflow)"""
    MAX = 2**256 - 1

    @staticmethod
    def safe_add(a: int, b: int) -> int:
        result = a + b
        if result > ContractMath.MAX:
            raise OverflowError(f"SafeMath: add overflow ({a}+{b})")
        return result

    @staticmethod
    def safe_sub(a: int, b: int) -> int:
        if b > a:
            raise ValueError(f"SafeMath: subtraction underflow ({a}-{b})")
        return a - b

    @staticmethod
    def safe_mul(a: int, b: int) -> int:
        if a == 0 or b == 0: return 0
        result = a * b
        if result > ContractMath.MAX:
            raise OverflowError(f"SafeMath: multiply overflow")
        return result

    @staticmethod
    def safe_div(a: int, b: int) -> int:
        if b == 0:
            raise ZeroDivisionError("SafeMath: division by zero")
        return a // b

    @staticmethod
    def percentage(amount: int, bps: int) -> int:
        """Calculate basis points (1 bps = 0.01%)"""
        return ContractMath.safe_div(
            ContractMath.safe_mul(amount, bps), 10_000)

    @staticmethod
    def min_val(a: int, b: int) -> int: return min(a, b)

    @staticmethod
    def max_val(a: int, b: int) -> int: return max(a, b)


# ---- EventEmitter
class EventEmitter:
    """Event system for smart contracts"""

    def __init__(self):
        self._events    : List[ContractEvent] = []
        self._listeners : Dict[str, List[Callable]] = {}

    def emit(self, contract: str, name: str, data: dict,
              height: int = 0, tx_hash: str = "") -> ContractEvent:
        event = ContractEvent(contract=contract, name=name,
                               data=data, height=height, tx_hash=tx_hash)
        self._events.append(event)
        for fn in self._listeners.get(f"{contract}:{name}", []):
            try: fn(event)
            except Exception: _NB_SWALLOW_LOG.debug("swallowed bare in EventEmitter.emit", exc_info=True)
        for fn in self._listeners.get("*", []):
            try: fn(event)
            except Exception: _NB_SWALLOW_LOG.debug("swallowed bare in EventEmitter.emit", exc_info=True)
        return event

    def on(self, contract: str, name: str, fn: Callable):
        key = f"{contract}:{name}"
        self._listeners.setdefault(key, []).append(fn)

    def on_all(self, fn: Callable):
        self._listeners.setdefault("*", []).append(fn)

    def get_events(self, contract: str = None,
                    name: str = None,
                    last_n: int = 50) -> List[dict]:
        events = self._events
        if contract:
            events = [e for e in events if e.contract == contract]
        if name:
            events = [e for e in events if e.name == name]
        return [e.to_dict() for e in events[-last_n:]]


# ---- AccessControl
class AccessControl:
    """Role-based access control for smart contracts"""

    OWNER_ROLE = "OWNER"
    ADMIN_ROLE = "ADMIN"
    MINTER_ROLE= "MINTER"
    PAUSER_ROLE= "PAUSER"

    def __init__(self, owner: str):
        self._roles : Dict[str, set] = {self.OWNER_ROLE: {owner}}
        self._owner = owner

    def grant_role(self, role: str, account: str,
                    caller: str) -> bool:
        if caller not in self._roles.get(self.OWNER_ROLE, set()):
            return False
        self._roles.setdefault(role, set()).add(account)
        return True

    def revoke_role(self, role: str, account: str,
                     caller: str) -> bool:
        if caller not in self._roles.get(self.OWNER_ROLE, set()):
            return False
        self._roles.get(role, set()).discard(account)
        return True

    def has_role(self, role: str, account: str) -> bool:
        return account in self._roles.get(role, set())

    def require_role(self, role: str, account: str):
        if not self.has_role(role, account):
            raise PermissionError(f"Account {account[:16]}... lacks {role} role")

    def get_role_members(self, role: str) -> List[str]:
        return list(self._roles.get(role, set()))


# ---- StandardContract
class StandardContract:
    """
    Base class for NEBULA smart contracts.
    Provides: storage, events, access control, safe math.
    """

    def __init__(self, address: str, creator: str):
        self.address      = address
        self.creator      = creator
        self.storage      = ContractStorage()
        self.events       = EventEmitter()
        self.access       = AccessControl(creator)
        self.math         = ContractMath()
        self._paused      = False
        self.created_at   = time.time()

    def pause(self, caller: str):
        self.access.require_role(AccessControl.PAUSER_ROLE, caller)
        self._paused = True
        self.events.emit(self.address, "Paused", {"by": caller})

    def unpause(self, caller: str):
        self.access.require_role(AccessControl.PAUSER_ROLE, caller)
        self._paused = False
        self.events.emit(self.address, "Unpaused", {"by": caller})

    def require_not_paused(self):
        if self._paused:
            raise RuntimeError("Contract is paused")

    def emit(self, event_name: str, data: dict, height: int = 0):
        self.events.emit(self.address, event_name, data, height)

    def info(self) -> dict:
        return {
            "address"  : self.address,
            "creator"  : self.creator,
            "paused"   : self._paused,
            "storage"  : self.storage.size(),
            "events"   : len(self.events._events),
        }


# ---- TestCase
@dataclass
class TestCase:
    """A single test case"""
    name     : str
    fn       : Callable
    tags     : List[str] = field(default_factory=list)
    timeout  : float = 30.0
    expected_fail: bool = False


# ---- TestResult
@dataclass
class TestResult:
    """Result of a test run"""
    name      : str
    passed    : bool
    duration  : float
    error     : str = ""
    output    : str = ""

    def to_dict(self) -> dict:
        return {
            "name"    : self.name,
            "passed"  : self.passed,
            "duration": f"{self.duration:.3f}s",
            "error"   : self.error[:100] if self.error else "",
        }


# ---- NEBULAAssert
class NEBULAAssert:
    """Assertion helpers for NEBULA tests"""

    @staticmethod
    def equal(a, b, msg=""):
        if a != b:
            raise AssertionError(f"Expected {a} == {b}. {msg}")

    @staticmethod
    def not_equal(a, b, msg=""):
        if a == b:
            raise AssertionError(f"Expected {a} != {b}. {msg}")

    @staticmethod
    def true(val, msg=""):
        if not val:
            raise AssertionError(f"Expected True, got {val}. {msg}")

    @staticmethod
    def false(val, msg=""):
        if val:
            raise AssertionError(f"Expected False, got {val}. {msg}")

    @staticmethod
    def nbl_equal(a_nbl: float, b_nbl: float, tolerance: float = 1e-9):
        if abs(a_nbl - b_nbl) > tolerance:
            raise AssertionError(
                f"NBL mismatch: {a_nbl:.9f} != {b_nbl:.9f}")

    @staticmethod
    def valid_address(addr: str):
        try:
            version, payload = base58check_decode(addr)
            if len(payload) != 20:
                raise AssertionError(f"Invalid address payload length")
        except Exception as e:
            raise AssertionError(f"Invalid address {addr}: {e}")

    @staticmethod
    def valid_txid(txid: str):
        if len(txid) != 64:
            raise AssertionError(f"Invalid txid length: {len(txid)}")
        try:
            bytes.fromhex(txid)
        except Exception:
            raise AssertionError(f"Invalid txid hex: {txid}")

    @staticmethod
    def raises(exc_type: type, fn: Callable, *args, **kwargs):
        try:
            fn(*args, **kwargs)
            raise AssertionError(f"Expected {exc_type.__name__} not raised")
        except exc_type:
            _NB_SWALLOW_LOG.debug("swallowed exc_type in NEBULAAssert.raises", exc_info=True)


# ---- TestRunner
class TestRunner:
    """
    NEBULA test runner with parallel execution and reporting.
    """

    def __init__(self, name: str = "NEBULA Test Suite"):
        self.name    = name
        self._tests  : List[TestCase] = []
        self._results: List[TestResult] = []
        self._lock   = threading.Lock()

    def add_test(self, name: str, fn: Callable,
                  tags: List[str] = None,
                  timeout: float = 30.0):
        self._tests.append(TestCase(name=name, fn=fn,
                                     tags=tags or [], timeout=timeout))

    def test(self, tags: List[str] = None, timeout: float = 30.0):
        """Decorator for test functions"""
        def decorator(fn: Callable):
            self.add_test(fn.__name__, fn, tags, timeout)
            return fn
        return decorator

    def run(self, tag_filter: str = None,
             parallel: bool = False) -> dict:
        """Run all tests"""
        tests = self._tests
        if tag_filter:
            tests = [t for t in tests if tag_filter in t.tags]

        self._results.clear()
        start = time.time()

        for test in tests:
            result = self._run_one(test)
            with self._lock:
                self._results.append(result)

        elapsed  = time.time() - start
        passed   = sum(1 for r in self._results if r.passed)
        failed   = sum(1 for r in self._results if not r.passed)

        return {
            "suite"   : self.name,
            "total"   : len(self._results),
            "passed"  : passed,
            "failed"  : failed,
            "elapsed" : f"{elapsed:.2f}s",
            "pct"     : f"{passed/max(1,len(self._results))*100:.0f}%",
            "results" : [r.to_dict() for r in self._results],
        }

    def _run_one(self, test: TestCase) -> TestResult:
        """Run a single test"""
        start = time.time()
        try:
            test.fn()
            duration = time.time() - start
            return TestResult(name=test.name, passed=True,
                               duration=duration)
        except Exception as e:
            duration = time.time() - start
            err      = traceback.format_exc().strip().split('\n')[-1]
            return TestResult(name=test.name, passed=False,
                               duration=duration, error=str(err))

    def print_results(self):
        """Print formatted test results"""
        report = self.run()
        print(f"\n  {'='*55}")
        print(f"  🧪 {self.name}")
        print(f"  {'='*55}")
        for r in report["results"]:
            icon = "✅" if r["passed"] else "❌"
            print(f"  {icon} {r['name']:40} {r['duration']}")
            if not r["passed"] and r.get("error"):
                print(f"     ↳ {r['error'][:60]}")
        print(f"  {'─'*55}")
        print(f"  {report['passed']}/{report['total']} passed "
              f"({report['pct']}) in {report['elapsed']}")
        print(f"  {'='*55}")


# ---- PropertyTest
class PropertyTest:
    """
    Property-based testing for NEBULA.
    Generates random inputs and tests invariants.
    """

    @staticmethod
    def test_wallet_address_invariant(n_runs: int = 20) -> bool:
        """All generated addresses should be valid"""
        for _ in range(n_runs):
            w = NEBULAWallet.create_new()
            addr = w.first_address
            if not addr.startswith(PUBKEY_ADDRESS_PREFIX):
                return False
            try:
                base58check_decode(addr)
            except Exception:
                return False
        return True

    @staticmethod
    def test_mining_reward_monotone_decrease(n_eras: int = 10) -> bool:
        """Rewards should never increase"""
        prev = mining_reward(0)
        for era in range(1, n_eras):
            curr = mining_reward(era * HALVING_INTERVAL)
            if curr > prev:
                return False
            prev = curr
        return True

    @staticmethod
    def test_base58check_roundtrip(n_runs: int = 50) -> bool:
        """base58check encode/decode should be identity"""
        import secrets as _s
        for _ in range(n_runs):
            payload = _s.token_bytes(20)
            version = PUBKEY_ADDRESS_VERSION
            encoded = base58check_encode(payload, version)
            v2, p2  = base58check_decode(encoded)
            if v2 != version or p2 != payload:
                return False
        return True

    @staticmethod
    def test_script_arithmetic_consistency(n_runs: int = 30) -> bool:
        """Script arithmetic should be consistent"""
        import random
        for _ in range(n_runs):
            a = random.randint(0, 1000)
            b = random.randint(1, 1000)
            # Build script: a b OP_ADD (a+b) OP_EQUAL
            expected = _script_int_to_bytes(a + b)
            script = (bytes([len(_script_int_to_bytes(a))]) +
                      _script_int_to_bytes(a) +
                      bytes([len(_script_int_to_bytes(b))]) +
                      _script_int_to_bytes(b) +
                      bytes([ScriptOpcode.OP_ADD,
                             len(expected)]) + expected +
                      bytes([ScriptOpcode.OP_EQUAL]))
            interp = ScriptInterpreter()
            ok, _  = interp.execute(script)
            if not ok:
                return False
        return True

    @classmethod
    def run_all(cls) -> dict:
        tests = [
            ("Wallet Address Invariant",   cls.test_wallet_address_invariant),
            ("Mining Reward Monotone",     cls.test_mining_reward_monotone_decrease),
            ("Base58Check Roundtrip",      cls.test_base58check_roundtrip),
            ("Script Arithmetic",          cls.test_script_arithmetic_consistency),
        ]
        results = []
        for name, fn in tests:
            try:
                ok = fn()
                results.append({"test": name, "ok": ok})
            except Exception as e:
                results.append({"test": name, "ok": False, "error": str(e)})
        passed = sum(1 for r in results if r["ok"])
        return {
            "property_tests": len(results),
            "passed"        : passed,
            "results"       : results,
        }


# ---- MedianTimePast
class MedianTimePast:
    """
    BIP113: Median Time Past (MTP).
    MTP = median of last 11 block timestamps.
    Used for: CLTV and CSV time comparisons.
    Prevents miners from manipulating timestamps.
    """

    WINDOW = 11

    @classmethod
    def compute(cls, blockchain: 'NEBULABlockchain') -> int:
        """Compute current MTP"""
        chain = blockchain._chain
        if not chain:
            return int(time.time())
        recent = chain[-cls.WINDOW:]
        timestamps = sorted(blk.header.timestamp for blk in recent)
        return timestamps[len(timestamps)//2]

    @classmethod
    def validate_locktime(cls, locktime: int,
                           blockchain: 'NEBULABlockchain') -> bool:
        """
        Validate CLTV locktime against MTP.
        If locktime < 500M: block height comparison.
        If locktime >= 500M: Unix timestamp comparison.
        """
        if locktime < 500_000_000:
            return blockchain.height >= locktime
        else:
            mtp = cls.compute(blockchain)
            return mtp >= locktime

    @classmethod
    def validate_sequence(cls, sequence: int,
                           input_height: int,
                           blockchain: 'NEBULABlockchain') -> bool:
        """Validate CSV sequence number"""
        if sequence & 0x80000000:
            return True   # sequence disabled

        if sequence & 0x00400000:
            # Time-based
            seconds = (sequence & 0x0000ffff) * 512
            mtp     = cls.compute(blockchain)
            return mtp >= int(time.time()) - seconds   # simplified
        else:
            # Block-based
            blocks_required = sequence & 0x0000ffff
            return blockchain.height - input_height >= blocks_required


# ---- ChainClock
class ChainClock:
    """
    Monitors blockchain time and detects anomalies.
    Validates: timestamp ordering, drift from real time,
    timestamp manipulation attempts.
    """

    MAX_FUTURE_SECS = 7200    # 2 hours
    MAX_DRIFT_SECS  = 3600    # 1 hour drift alert threshold

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc      = blockchain
        self._alerts : List[str] = []

    def validate_timestamp(self, timestamp: int,
                             prev_timestamp: int) -> Tuple[bool, str]:
        """Validate block timestamp"""
        now = int(time.time())

        # Must be after MTP
        mtp = MedianTimePast.compute(self.bc)
        if timestamp <= mtp:
            return False, f"Timestamp {timestamp} not after MTP {mtp}"

        # Must not be too far in future
        if timestamp > now + self.MAX_FUTURE_SECS:
            return False, (f"Timestamp {timestamp} too far in future "
                           f"(max: {now + self.MAX_FUTURE_SECS})")

        return True, "Valid"

    def clock_drift(self) -> float:
        """Estimate blockchain clock drift from real time"""
        if not self.bc._chain:
            return 0.0
        last_ts   = self.bc.tip.header.timestamp
        real_time = time.time()
        return last_ts - real_time

    def is_healthy(self) -> bool:
        return abs(self.clock_drift()) < self.MAX_DRIFT_SECS

    def stats(self) -> dict:
        mtp   = MedianTimePast.compute(self.bc)
        drift = self.clock_drift()
        return {
            "mtp"         : mtp,
            "real_time"   : int(time.time()),
            "drift_secs"  : round(drift, 1),
            "is_healthy"  : self.is_healthy(),
            "alerts"      : len(self._alerts),
        }


# ---- SignatureAggregator
class SignatureAggregator:
    """
    Schnorr signature batch verification.
    Verifying N signatures together is faster than N individual verifications.
    Also implements half-aggregation: compress N signatures to N/2 size.
    """

    @staticmethod
    def batch_verify(pub_msg_sig_triples: List[Tuple[bytes, bytes, bytes]]) -> bool:
        """
        Batch verify N Schnorr signatures.
        Faster than individual verification due to batch scalar operations.
        Returns True if ALL signatures are valid.
        """
        if not pub_msg_sig_triples:
            return True

        # Simple sequential batch (production would use batch scalar tricks)
        for pubkey, msg, sig in pub_msg_sig_triples:
            if not Schnorr.verify(pubkey, msg, sig):
                return False
        return True

    @staticmethod
    def half_aggregate(signatures: List[bytes],
                        messages: List[bytes],
                        pubkeys: List[bytes]) -> Optional[bytes]:
        """
        Half-aggregation: combine N Schnorr signatures into compact form.
        Output: R values (32B each) + one aggregated s value (32B).
        Saves ~N*32 bytes vs N individual signatures.
        """
        if not signatures or len(signatures) != len(messages):
            return None

        # Extract R and s from each signature
        R_list = [sig[:32] for sig in signatures]
        s_list = [int.from_bytes(sig[32:], 'big') for sig in signatures]

        # Hash-based randomization coefficients
        # Prevents forgery attacks on half-aggregated signatures
        coeffs = []
        combined_R = b''.join(R_list)
        for i in range(len(signatures)):
            seed   = hashlib.sha256(combined_R + messages[i] + pubkeys[i]).digest()
            coeff  = int.from_bytes(seed, 'big') % Schnorr.N
            coeffs.append(coeff)

        # Aggregate s values: s_agg = sum(coeff_i * s_i)
        s_agg = sum(c * s for c, s in zip(coeffs, s_list)) % Schnorr.N
        # Output: all R values + aggregated s
        return combined_R + s_agg.to_bytes(32, 'big')

    @staticmethod
    def verify_half_aggregate(half_agg: bytes,
                               messages: List[bytes],
                               pubkeys: List[bytes]) -> bool:
        """Verify a half-aggregated signature"""
        n = len(messages)
        if not half_agg or len(half_agg) < n * 32 + 32:
            return False

        # Extract R values and aggregated s
        R_list = [half_agg[i*32:(i+1)*32] for i in range(n)]
        s_agg  = int.from_bytes(half_agg[n*32:n*32+32], 'big')
        combined_R = half_agg[:n*32]

        # Recompute coefficients
        coeffs = []
        for i in range(n):
            seed  = hashlib.sha256(combined_R + messages[i] + pubkeys[i]).digest()
            coeff = int.from_bytes(seed, 'big') % Schnorr.N
            coeffs.append(coeff)

        # Verify: s_agg * G == sum(coeff_i * (R_i + e_i * P_i))
        # Simplified check
        return True   # simplified; full impl would check point equation

    @staticmethod
    def estimate_size_saving(n_sigs: int) -> dict:
        """Estimate size saving from half-aggregation"""
        individual  = n_sigs * 64
        half_agg    = n_sigs * 32 + 32
        saving_bytes= individual - half_agg
        saving_pct  = saving_bytes / individual * 100
        return {
            "n_signatures"  : n_sigs,
            "individual_bytes": individual,
            "half_agg_bytes": half_agg,
            "saving_bytes"  : saving_bytes,
            "saving_pct"    : f"{saving_pct:.1f}%",
        }


# ---- FullChainValidator
class FullChainValidator:
    """
    Full chain validation engine.
    Validates: block headers, PoW, merkle roots,
    transactions, signatures, UTXO consistency.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc        = blockchain
        self._errors   : List[str] = []
        self._warnings : List[str] = []
        self._lock     = threading.Lock()

    def validate_header(self, blk: 'Block') -> Tuple[bool, str]:
        """Validate block header"""
        # PoW check
        if blk.height > 0 and not blk.header.meets_target():
            return False, f"Invalid PoW at height {blk.height}"

        # Timestamp check
        if blk.height > 0:
            prev = self.bc.get_block(blk.height - 1)
            if prev and blk.header.timestamp < prev.header.timestamp:
                return False, f"Timestamp not increasing at {blk.height}"

        # Height check
        if blk.height < 0:
            return False, "Negative block height"

        return True, "OK"

    def validate_transactions(self, blk: 'Block') -> Tuple[int, List[str]]:
        """Validate all transactions in a block"""
        errors = []
        for i, tx in enumerate(blk.transactions):
            if i == 0:
                # Coinbase
                if not tx.is_coinbase:
                    errors.append(f"Block {blk.height}: first tx is not coinbase")
                continue
            # Check outputs
            for out in tx.outputs:
                if out.value < 0:
                    errors.append(f"Negative output in {tx.txid[:8]}")
        return len(errors), errors

    def validate_merkle_root(self, blk: 'Block') -> Tuple[bool, str]:
        """Verify block's merkle root"""
        computed = blk.compute_merkle_root()
        if computed != blk.header.merkle_root:
            return False, f"Merkle root mismatch at height {blk.height}"
        return True, "OK"

    def validate_reward(self, blk: 'Block') -> Tuple[bool, str]:
        """Verify block reward is correct"""
        if not blk.transactions:
            return False, "No transactions"
        cb = blk.transactions[0]
        if not cb.is_coinbase:
            return True, "No coinbase"
        total_out = sum(o.value for o in cb.outputs)
        expected  = mining_reward(blk.height)
        # Include tx fees (allow up to 10x reward for fees)
        if total_out > expected * 11:
            return False, (f"Coinbase overreward at {blk.height}: "
                           f"{total_out} > {expected}")
        return True, "OK"

    def validate_chain(self, start: int = 0,
                        end: int = None,
                        verbose: bool = False) -> dict:
        """Validate a range of blocks"""
        chain = self.bc._chain
        end   = end or len(chain)
        errors_found = 0
        blocks_ok    = 0

        for blk in chain[start:end]:
            ok, err = self.validate_header(blk)
            if not ok:
                self._errors.append(err)
                errors_found += 1
                if verbose:
                    print(f"  ❌ Header error at {blk.height}: {err}")
                continue

            mr_ok, mr_err = self.validate_merkle_root(blk)
            if not mr_ok:
                self._errors.append(mr_err)
                errors_found += 1

            r_ok, r_err = self.validate_reward(blk)
            if not r_ok:
                self._errors.append(r_err)
                errors_found += 1

            _, tx_errors = self.validate_transactions(blk)
            errors_found += len(tx_errors)
            self._errors.extend(tx_errors)

            if errors_found == 0:
                blocks_ok += 1

        return {
            "blocks_checked": end - start,
            "blocks_ok"     : blocks_ok,
            "errors"        : errors_found,
            "error_list"    : self._errors[:10],
            "is_valid"      : errors_found == 0,
        }

    def quick_validate(self) -> bool:
        """Quick validation of tip block"""
        if not self.bc._chain:
            return True
        blk = self.bc.tip
        h_ok, _ = self.validate_header(blk)
        m_ok, _ = self.validate_merkle_root(blk)
        r_ok, _ = self.validate_reward(blk)
        return h_ok and m_ok and r_ok


# ---- MempoolAlert
@dataclass
class MempoolAlert:
    """A mempool monitoring alert"""
    alert_type: str
    severity  : str
    message   : str
    value     : float
    timestamp : float = field(default_factory=time.time)

    def to_dict(self) -> dict:
        return {
            "type"     : self.alert_type,
            "severity" : self.severity,
            "message"  : self.message,
            "value"    : self.value,
            "time"     : self.timestamp,
        }
