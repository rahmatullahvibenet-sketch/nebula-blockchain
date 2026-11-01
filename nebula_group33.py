"""NEBULA group33 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. InsuranceProtocol  (orig. lines 55645-55750)
   2. LaunchpadProject  (orig. lines 55760-55794)
   3. Launchpad  (orig. lines 55796-55899)
   4. RBFPolicy  (orig. lines 56016-56063)
   5. CPFPAccelerator  (orig. lines 56066-56133)
   6. MempoolEvictionPolicy  (orig. lines 56136-56179)
   7. StratumJob  (orig. lines 56266-56293)
   8. BlockTemplateEngine  (orig. lines 56295-56431)
   9. ChainSynchronizer  (orig. lines 56501-56646)
  10. PrunedChainStorage  (orig. lines 56649-56686)
  11. FastSyncManager  (orig. lines 56689-56735)
  12. MnemonicRecoveryTool  (orig. lines 56748-56824)
  13. PaperWalletImporter  (orig. lines 56827-56879)
  14. WalletMigrationTool  (orig. lines 56882-56921)
  15. NetMsgType  (orig. lines 56931-56961)
  16. RejectCode  (orig. lines 56963-56972)
  17. VestingSchedule  (orig. lines 57198-57245)
  18. VestingManager  (orig. lines 57247-57329)
  19. ValidatorCandidate  (orig. lines 57341-57358)
  20. ValidatorSetManager  (orig. lines 57360-57446)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BIP39, BlockHeader, HDKey, InsurancePolicy, MerkleTree, Script, Secp256k1, SyncState, Transaction
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
CHAIN_VERSION       = 1

DECIMALS            = 9

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

INITIAL_BITS           = 0x1e0fffff if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d0fffff   # [v10.24]

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

WIF_VERSION             = 0xB5   # NEBULA WIF — distinct from Bitcoin (0x80)

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

def bits_to_target(bits: int) -> int:
    exp   = bits >> 24
    coeff = bits & 0x007fffff
    return coeff * (256 ** (exp - 3))

def mining_reward(height: int) -> int:
    """Block reward with halving schedule.
    FIX: negative height safely returns 0 instead of crashing."""
    if height < 0:
        return 0
    era = height // HALVING_INTERVAL
    if era >= 64:
        return 0
    return INITIAL_BLOCK_REWARD >> era

def _encrypt_mnemonic(mnemonic: str, password: str) -> dict:
    """
    Encrypt mnemonic with PBKDF2-HMAC-SHA256 + XOR stream cipher.
    No external dependencies — uses only standard library.
    Format: {"salt": hex, "iv": hex, "ct": hex, "mac": hex}
    """
    salt    = secrets.token_bytes(16)
    iv      = secrets.token_bytes(16)
    # Derive 64-byte key via PBKDF2
    key     = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 200_000, dklen=64)
    enc_key = key[:32]
    mac_key = key[32:]
    # XOR-stream encryption (deterministic, secure with random IV)
    data    = mnemonic.encode('utf-8')
    pad     = hashlib.pbkdf2_hmac('sha256', enc_key, iv, 1, dklen=len(data))
    ct      = bytes(a ^ b for a, b in zip(data, pad))
    # HMAC authentication tag
    mac     = hmac.new(mac_key, salt + iv + ct, hashlib.sha256).digest()
    return {
        "salt": salt.hex(),
        "iv":   iv.hex(),
        "ct":   ct.hex(),
        "mac":  mac.hex(),
        "kdf":  "pbkdf2-sha256-200000",
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

_routes: Dict[str, Dict[str, Callable]] = {}

def route(path: str, methods: List[str] = None):
    """Decorator to register an API endpoint."""
    def decorator(fn: Callable) -> Callable:
        for method in (methods or ["GET"]):
            _routes.setdefault(method.upper(), {})[path] = fn
        return fn
    return decorator

@route("/api/status")
def status(path, query, body):
    return ok({
        "online"        : True,
        "height"        : STATE.height(),
        "tip_hash"      : STATE.tip_hash(),
        "mining"        : STATE._mining,
        "hashrate"      : (getattr(getattr(STATE.miner, "stats", None), "hashrate", 0) if STATE.miner else STATE._mock_hashrate),
        "peers"         : (STATE.network.peer_count() if STATE.network else len(STATE._mock_peers)),
        "mempool_txs"   : (len(STATE.chain.mempool._pool) if STATE.chain and hasattr(STATE.chain, "mempool") and hasattr(STATE.chain.mempool, "_pool") else len(STATE._mock_txpool)),
        "uptime_secs"   : int(time.time() - STATE._start),
        "modules"       : {k: v["ok"] for k,v in STATE.module_status().items()},
        "genesis_date"  : "2025-03-16",
        "block_reward"  : 50.0,
        "halving_era"   : 1,
    })

MAX_VALIDATORS           = 100

EPOCH_BLOCKS = 2016   # validator set rotates every 2016 blocks

MAX_MEMPOOL_BYTES       = 300 * 1024 * 1024   # 300 MB

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- InsuranceProtocol
class InsuranceProtocol:
    """
    NEBULA DeFi insurance protocol.
    Users pay premiums to get coverage against smart contract hacks.
    Claims assessed by governance vote.
    """

    BASE_PREMIUM_RATE  = 0.005    # 0.5% of coverage per year
    MIN_COVERAGE       = 100 * 10**DECIMALS
    MAX_COVERAGE_RATIO = 0.10     # max 10% of pool can be paid out

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._policies:  Dict[str, InsurancePolicy] = {}
        self._pools:     Dict[str, int]             = {}  # coverage_type -> pool_size
        self._claims:    List[dict]                 = []
        self._lock       = threading.RLock()

    def add_to_pool(self, coverage_type: str, amount: int):
        """Underwriters add capital to coverage pool."""
        with self._lock:
            self._pools[coverage_type] = (
                self._pools.get(coverage_type, 0) + amount)

    def buy_policy(self, holder: str, coverage_type: str,
                    covered_protocol: str,
                    coverage_nbl: float,
                    duration_days: int = 30) -> Tuple[bool, str]:
        with self._lock:
            coverage   = int(coverage_nbl * 10**DECIMALS)
            pool_size  = self._pools.get(coverage_type, 0)
            if coverage > pool_size * self.MAX_COVERAGE_RATIO:
                return False, "Coverage exceeds pool capacity"
            if coverage < self.MIN_COVERAGE:
                return False, f"Minimum coverage: {self.MIN_COVERAGE/10**DECIMALS:.0f} NBL"

            # Premium = coverage * rate * (days / 365)
            premium    = int(coverage * self.BASE_PREMIUM_RATE * duration_days / 365)
            valid_until = self._bc.height + duration_days * 144

            pid = hashlib.sha256(
                f"INS:{holder}:{coverage_type}:{time.time()}".encode()
            ).hexdigest()[:16]

            self._policies[pid] = InsurancePolicy(
                policy_id        = pid,
                holder           = holder,
                coverage_type    = coverage_type,
                covered_protocol = covered_protocol,
                coverage_amount  = coverage,
                premium_paid     = premium,
                valid_until      = valid_until,
            )
            self._pools[coverage_type] = max(0, pool_size - int(coverage * 0.1))
            return True, pid

    def file_claim(self, policy_id: str, holder: str,
                    description: str) -> Tuple[bool, str]:
        with self._lock:
            pol = self._policies.get(policy_id)
            if not pol or pol.holder != holder:
                return False, "Policy not found"
            if not pol.active:
                return False, "Policy not active"
            if pol.claimed:
                return False, "Already claimed"
            if self._bc.height > pol.valid_until:
                return False, "Policy expired"

            claim = {
                "claim_id":   secrets.token_hex(8),
                "policy_id":  policy_id,
                "holder":     holder,
                "amount":     pol.coverage_amount,
                "description": description,
                "status":     "pending",
                "filed_at":   time.time(),
            }
            self._claims.append(claim)
            return True, claim["claim_id"]

    def approve_claim(self, claim_id: str) -> Tuple[bool, str]:
        with self._lock:
            claim = next((c for c in self._claims if c["claim_id"] == claim_id), None)
            if not claim:
                return False, "Not found"
            claim["status"] = "approved"
            pol = self._policies.get(claim["policy_id"])
            if pol:
                pol.claimed = True
                pol.active  = False
            return True, f"Claim approved: {claim['amount']/10**DECIMALS:.3f} NBL payout"

    def insurance_stats(self) -> dict:
        with self._lock:
            total_policies  = len(self._policies)
            active_policies = sum(1 for p in self._policies.values() if p.active)
            total_pool      = sum(self._pools.values())
            total_claims    = len(self._claims)
        return {
            "total_policies":  total_policies,
            "active_policies": active_policies,
            "total_pool_nbl":  f"{total_pool/10**DECIMALS:.3f}",
            "total_claims":    total_claims,
            "coverage_types":  list(self._pools.keys()),
        }


# ---- LaunchpadProject
@dataclass
class LaunchpadProject:
    project_id:    str
    name:          str
    symbol:        str
    team:          str
    description:   str
    token_price:   float     # NBL per token
    hard_cap:      int       # max raise in NBL Neb
    soft_cap:      int       # min raise to proceed
    total_tokens:  int       # tokens being sold
    start_block:   int
    end_block:     int
    raised:        int = 0
    participants:  int = 0
    status:        str = "upcoming"   # upcoming/active/filled/failed/distributed
    contributions: dict = field(default_factory=dict)   # addr -> amount

    def fill_pct(self) -> float:
        return self.raised / self.hard_cap if self.hard_cap > 0 else 0

    def to_dict(self) -> dict:
        return {
            "project_id":   self.project_id,
            "name":         self.name,
            "symbol":       self.symbol,
            "team":         self.team,
            "token_price":  self.token_price,
            "hard_cap_nbl": f"{self.hard_cap/10**DECIMALS:.0f}",
            "soft_cap_nbl": f"{self.soft_cap/10**DECIMALS:.0f}",
            "raised_nbl":   f"{self.raised/10**DECIMALS:.3f}",
            "fill_pct":     f"{self.fill_pct()*100:.1f}%",
            "participants": self.participants,
            "status":       self.status,
        }


# ---- Launchpad
class Launchpad:
    """NEBULA project launchpad for IDO/ICO fundraising."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                 nbl20: 'NBL20Registry' = None):
        self._bc       = blockchain
        self._nbl20    = nbl20
        self._projects: Dict[str, LaunchpadProject] = {}
        self._lock     = threading.RLock()

    def list_project(self, team: str, name: str, symbol: str,
                      description: str, token_price: float,
                      hard_cap_nbl: float, soft_cap_nbl: float,
                      total_tokens: int, duration_days: int = 7) -> str:
        with self._lock:
            hard_cap   = int(hard_cap_nbl * 10**DECIMALS)
            soft_cap   = int(soft_cap_nbl * 10**DECIMALS)
            start      = self._bc.height + 1
            end        = start + duration_days * 144
            pid = hashlib.sha256(
                f"IDO:{team}:{name}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._projects[pid] = LaunchpadProject(
                project_id   = pid,
                name         = name,
                symbol       = symbol,
                team         = team,
                description  = description,
                token_price  = token_price,
                hard_cap     = hard_cap,
                soft_cap     = soft_cap,
                total_tokens = total_tokens,
                start_block  = start,
                end_block    = end,
                status       = "upcoming",
            )
            return pid

    def contribute(self, project_id: str, contributor: str,
                    amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            proj = self._projects.get(project_id)
            if not proj:
                return False, "Project not found"
            cur = self._bc.height
            if cur < proj.start_block:
                return False, "Not started yet"
            if cur > proj.end_block:
                proj.status = "failed" if proj.raised < proj.soft_cap else proj.status
                return False, "IDO ended"
            amount = int(amount_nbl * 10**DECIMALS)
            if proj.raised + amount > proj.hard_cap:
                amount = proj.hard_cap - proj.raised
            if amount <= 0:
                return False, "Hard cap reached"
            proj.contributions[contributor] = (
                proj.contributions.get(contributor, 0) + amount)
            if contributor not in proj.contributions or amount == int(amount_nbl * 10**DECIMALS):
                proj.participants += 1
            proj.raised += amount
            if proj.raised >= proj.hard_cap:
                proj.status = "filled"
            else:
                proj.status = "active"
            return True, (f"Contributed {amount/10**DECIMALS:.3f} NBL. "
                          f"You get {amount/10**DECIMALS/proj.token_price:.2f} {proj.symbol}")

    def finalize(self, project_id: str) -> Tuple[bool, str]:
        with self._lock:
            proj = self._projects.get(project_id)
            if not proj:
                return False, "Not found"
            if self._bc.height < proj.end_block and proj.status != "filled":
                return False, "IDO still active"
            if proj.raised < proj.soft_cap:
                proj.status = "failed"
                return False, f"Soft cap not reached ({proj.raised/10**DECIMALS:.0f} < {proj.soft_cap/10**DECIMALS:.0f} NBL)"
            proj.status = "distributed"
            return True, (f"IDO successful! Raised {proj.raised/10**DECIMALS:.0f} NBL "
                          f"from {proj.participants} participants")

    def refund(self, project_id: str, contributor: str) -> Tuple[bool, int]:
        with self._lock:
            proj = self._projects.get(project_id)
            if not proj or proj.status != "failed":
                return False, 0
            amount = proj.contributions.pop(contributor, 0)
            if amount == 0:
                return False, 0
            return True, amount

    def launchpad_stats(self) -> dict:
        with self._lock:
            total   = len(self._projects)
            active  = sum(1 for p in self._projects.values() if p.status == "active")
            success = sum(1 for p in self._projects.values() if p.status == "distributed")
            total_raised = sum(p.raised for p in self._projects.values()
                               if p.status == "distributed")
        return {
            "total_projects":   total,
            "active_projects":  active,
            "successful":       success,
            "total_raised_nbl": f"{total_raised/10**DECIMALS:.0f}",
        }


# ---- RBFPolicy
class RBFPolicy:
    """
    Replace-By-Fee policy for NEBULA mempool.
    Allows users to bump fees on unconfirmed transactions.
    """
    MIN_FEE_BUMP_PCT = 0.10   # new fee must be at least 10% higher

    def __init__(self, mempool: 'Mempool'):
        self._mp   = mempool
        self._rbf_map: Dict[str, str] = {}   # old_txid -> new_txid
        self._lock = threading.RLock()

    def can_replace(self, old_txid: str, new_tx: 'Transaction') -> Tuple[bool, str]:
        """Check if new_tx can replace old_txid under RBF rules."""
        with self._lock:
            old_tx = self._mp._txs.get(old_txid)
            if not old_tx:
                return False, "Original tx not in mempool"
            old_fee = old_tx.fee(self._mp._utxo)
            new_fee = new_tx.fee(self._mp._utxo)
            min_new = int(old_fee * (1 + self.MIN_FEE_BUMP_PCT))
            if new_fee < min_new:
                return False, (f"Fee too low for RBF: need {min_new}, "
                               f"got {new_fee}")
            # Must spend at least one same input
            old_inputs = {f"{i.outpoint.txid}:{i.outpoint.index}"
                          for i in old_tx.inputs}
            new_inputs = {f"{i.outpoint.txid}:{i.outpoint.index}"
                          for i in new_tx.inputs}
            if not old_inputs & new_inputs:
                return False, "No overlapping inputs — not an RBF"
            return True, "RBF eligible"

    def replace(self, old_txid: str,
                new_tx: 'Transaction') -> Tuple[bool, str]:
        """Replace old tx with new tx if RBF rules satisfied."""
        ok, msg = self.can_replace(old_txid, new_tx)
        if not ok:
            return False, msg
        with self._lock:
            self._mp.remove(old_txid)
            ok2, msg2 = self._mp.submit(new_tx)
            if ok2:
                self._rbf_map[old_txid] = new_tx.txid
            return ok2, msg2

    def replacement_of(self, old_txid: str) -> Optional[str]:
        return self._rbf_map.get(old_txid)


# ---- CPFPAccelerator
class CPFPAccelerator:
    """
    Child-Pays-For-Parent (CPFP) fee bumping.
    If parent tx has low fee, child tx with high fee
    incentivizes miner to include both.
    """

    def __init__(self, mempool: 'Mempool',
                 blockchain: 'NEBULABlockchain'):
        self._mp  = mempool
        self._bc  = blockchain

    def get_package_fee_rate(self, child_txid: str) -> float:
        """Calculate effective fee rate for parent+child package."""
        child = self._mp._txs.get(child_txid)
        if not child:
            return 0.0
        # Find parent txs in mempool
        parent_txids = set()
        for inp in child.inputs:
            if inp.outpoint.txid in self._mp._txs:
                parent_txids.add(inp.outpoint.txid)

        total_fee  = child.fee(self._bc.utxo)
        total_size = child.byte_size()

        for ptxid in parent_txids:
            parent = self._mp._txs.get(ptxid)
            if parent:
                total_fee  += parent.fee(self._bc.utxo)
                total_size += parent.byte_size()

        return total_fee / total_size if total_size > 0 else 0.0

    def suggest_child_fee(self, parent_txid: str,
                           target_rate: int) -> int:
        """
        Suggest fee for child tx to accelerate a stuck parent.
        target_rate = desired fee rate in Neb/byte
        """
        parent = self._mp._txs.get(parent_txid)
        if not parent:
            return MIN_TX_FEE
        parent_fee    = parent.fee(self._bc.utxo)
        parent_size   = parent.byte_size()
        parent_rate   = parent_fee / parent_size if parent_size > 0 else 0

        child_size    = 200   # estimated child tx size
        package_size  = parent_size + child_size
        total_needed  = target_rate * package_size
        child_fee     = max(int(total_needed - parent_fee), MIN_TX_FEE)
        return child_fee

    def find_stuck_parents(self, min_age_blocks: int = 6) -> List[dict]:
        """Find transactions stuck in mempool for too long."""
        cur = self._bc.height
        stuck = []
        for txid, tx in self._mp._txs.items():
            fee_rate = tx.fee(self._bc.utxo) // max(1, tx.byte_size())
            if fee_rate < MIN_TX_FEE * 2:
                stuck.append({
                    "txid":      txid,
                    "fee_rate":  fee_rate,
                    "size":      tx.byte_size(),
                    "fee":       tx.fee(self._bc.utxo),
                    "suggested_child_fee": self.suggest_child_fee(txid, MIN_TX_FEE * 5),
                })
        return stuck


# ---- MempoolEvictionPolicy
class MempoolEvictionPolicy:
    """
    Evict low-fee transactions when mempool is full.
    Keeps mempool bounded in memory.
    """

    MAX_MEMPOOL_BYTES  = 300 * 1024 * 1024   # 300 MB
    MIN_EVICT_FEE_RATE = MIN_TX_FEE          # below this = first to go

    def __init__(self, mempool: 'Mempool'):
        self._mp = mempool

    def current_size_bytes(self) -> int:
        return sum(tx.byte_size() for tx in self._mp._txs.values())

    def evict_if_needed(self) -> int:
        """Evict lowest-fee txs if mempool is too large. Returns count evicted."""
        if self.current_size_bytes() <= self.MAX_MEMPOOL_BYTES:
            return 0
        evicted = 0
        # Sort by fee rate ascending (cheapest first)
        by_fee = sorted(
            self._mp._txs.items(),
            key=lambda x: x[1].fee(self._mp._utxo) //
                          max(1, x[1].byte_size())
        )
        for txid, tx in by_fee:
            if self.current_size_bytes() <= self.MAX_MEMPOOL_BYTES * 0.9:
                break
            self._mp.remove(txid)
            evicted += 1
        return evicted

    def mempool_health(self) -> dict:
        size_bytes = self.current_size_bytes()
        pct        = size_bytes / self.MAX_MEMPOOL_BYTES * 100
        return {
            "size_mb":      f"{size_bytes/1024/1024:.2f}",
            "max_mb":       f"{self.MAX_MEMPOOL_BYTES/1024/1024:.0f}",
            "usage_pct":    f"{pct:.1f}%",
            "tx_count":     self._mp.size(),
            "total_fees":   f"{self._mp.total_fees()/10**DECIMALS:.6f} NBL",
            "health":       "OK" if pct < 80 else "WARNING" if pct < 95 else "FULL",
        }


# ---- StratumJob
@dataclass
class StratumJob:
    job_id:        str
    prev_hash:     str
    coinbase1:     str    # hex — first part of coinbase
    coinbase2:     str    # hex — second part (after extranonce)
    merkle_branch: List[str]
    version:       str
    nbits:         str
    ntime:         str
    clean_jobs:    bool = False

    def to_stratum(self) -> dict:
        return {
            "id":     None,
            "method": "mining.notify",
            "params": [
                self.job_id,
                self.prev_hash,
                self.coinbase1,
                self.coinbase2,
                self.merkle_branch,
                self.version,
                self.nbits,
                self.ntime,
                self.clean_jobs,
            ]
        }


# ---- BlockTemplateEngine
class BlockTemplateEngine:
    """
    Builds optimal block templates for miners.
    Selects transactions to maximize fee revenue.
    Supports extra nonce for pool mining.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 miner_address: str = ""):
        self._bc           = blockchain
        self._miner_address = miner_address or FOUNDATION_ADDRESS
        self._current_template: Optional[dict] = None
        self._template_height: int = -1
        self._lock         = threading.RLock()
        self._job_counter  = 0

    def build_template(self, extra_data: bytes = b'') -> dict:
        """Build a complete block template."""
        with self._lock:
            bc    = self._bc
            tip   = bc.tip
            height = bc.height + 1
            bits   = bc.get_next_bits()
            reward = mining_reward(height)

            # Select transactions from mempool
            selected_txs = bc.mempool.get_for_block()
            total_fees   = sum(tx.fee(bc.utxo) for tx in selected_txs)

            # Build coinbase
            coinbase = Transaction.coinbase(
                height        = height,
                reward        = reward + total_fees,
                miner_address = self._miner_address,
                extra_data    = extra_data,
            )

            all_txs    = [coinbase] + selected_txs
            merkle_root = MerkleTree.compute_root([tx.txid for tx in all_txs])

            template = {
                "version":      CHAIN_VERSION,
                "prev_hash":    tip.hash,
                "merkle_root":  merkle_root,
                "timestamp":    int(time.time()),
                "bits":         bits,
                "height":       height,
                "reward":       reward,
                "fees":         total_fees,
                "tx_count":     len(all_txs),
                "coinbase_txid": coinbase.txid,
                "transactions": all_txs,
                "target":       hex(bits_to_target(bits)),
            }
            self._current_template = template
            self._template_height  = height
            return template

    def to_stratum_job(self, clean: bool = False) -> StratumJob:
        """Convert template to Stratum mining job."""
        t = self._current_template
        if not t:
            t = self.build_template()

        self._job_counter += 1
        job_id = f"{self._job_counter:08x}"

        # Build coinbase hex parts
        cb_tx  = t["transactions"][0]
        cb_raw = cb_tx.serialize()
        # Split after script_sig for extranonce insertion
        split  = 42   # approximate split point
        cb1    = cb_raw[:split].hex()
        cb2    = cb_raw[split:].hex()

        # Merkle branch (all tx hashes except coinbase)
        branch = [tx.txid for tx in t["transactions"][1:]]

        return StratumJob(
            job_id        = job_id,
            prev_hash     = t["prev_hash"],
            coinbase1     = cb1,
            coinbase2     = cb2,
            merkle_branch = branch,
            version       = f"{t['version']:08x}",
            nbits         = f"{t['bits']:08x}",
            ntime         = f"{t['timestamp']:08x}",
            clean_jobs    = clean,
        )

    def validate_share(self, job_id: str,
                        extranonce2: str,
                        ntime: str,
                        nonce: str,
                        difficulty: int) -> Tuple[bool, str]:
        """Validate a share submitted by a pool worker."""
        if not self._current_template:
            return False, "No active job"
        try:
            nonce_int = int(nonce, 16)
            ntime_int = int(ntime, 16)
            bits      = self._current_template["bits"]
            prev      = self._current_template["prev_hash"]
            merkle    = self._current_template["merkle_root"]

            header = BlockHeader(
                version     = CHAIN_VERSION,
                prev_hash   = prev,
                merkle_root = merkle,
                timestamp   = ntime_int,
                bits        = bits,
                nonce       = nonce_int,
                height      = self._current_template["height"],
            )

            h = int(header.hash(), 16)

            # Check share difficulty
            share_target = bits_to_target(bits) * difficulty
            if h > share_target:
                return False, "Share below difficulty"

            # Check if it's a full block solution
            if header.meets_target():
                return True, "BLOCK_FOUND"

            return True, "SHARE_ACCEPTED"
        except Exception as e:
            return False, f"Share validation error: {e}"

    def template_age_blocks(self) -> int:
        return self._bc.height - self._template_height + 1

    def needs_refresh(self) -> bool:
        return (self._current_template is None or
                self._bc.height >= self._template_height or
                time.time() - self._current_template.get("timestamp", 0) > 60)


# ---- ChainSynchronizer
@dataclass
class ChainSynchronizer:
    """
    Headers-first chain synchronization.
    1. Download all headers (fast, no validation).
    2. Validate headers (difficulty, timestamps).
    3. Download+validate blocks in parallel.
    4. Handle forks and reorgs.
    """

    HEADERS_BATCH  = 2000
    BLOCKS_BATCH   = 128
    MAX_ORPHANS    = 200

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._state     = SyncState()
        self._orphans:  Dict[str, 'Block']    = {}
        self._pending_headers: List[dict]     = []
        self._checkpoints: Dict[int, str]     = self._default_checkpoints()
        self._lock      = threading.RLock()

    def _default_checkpoints(self) -> Dict[int, str]:
        """Known-good block hashes at specific heights."""
        return {
            0: self._bc.get_block(0).hash if self._bc.height >= 0 else "0"*64,
        }

    def add_checkpoint(self, height: int, block_hash: str):
        """Add a trusted checkpoint."""
        with self._lock:
            self._checkpoints[height] = block_hash

    def verify_checkpoint(self, height: int, block_hash: str) -> bool:
        """Verify block matches checkpoint if one exists."""
        expected = self._checkpoints.get(height)
        if expected is None:
            return True   # no checkpoint at this height
        return expected == block_hash

    def process_headers(self, headers: List[dict]) -> Tuple[int, List[str]]:
        """
        Process a batch of block headers.
        Returns (accepted_count, error_list).
        """
        accepted = 0
        errors   = []
        for hdr in headers:
            ok, err = self._validate_header(hdr)
            if ok:
                self._pending_headers.append(hdr)
                self._state.best_header = max(
                    self._state.best_header, hdr.get("height", 0))
                accepted += 1
            else:
                errors.append(err)
        return accepted, errors

    def _validate_header(self, hdr: dict) -> Tuple[bool, str]:
        """Validate a header without downloading the full block."""
        try:
            height = hdr.get("height", 0)
            bits   = hdr.get("bits", INITIAL_BITS)
            prev   = hdr.get("prev_hash", "0"*64)
            ts     = hdr.get("timestamp", 0)

            # Timestamp check
            now = int(time.time())
            if ts > now + 7200:
                return False, f"Future timestamp: {ts}"

            # Checkpoint check
            h = hdr.get("hash", "")
            if not self.verify_checkpoint(height, h):
                return False, f"Checkpoint mismatch at height {height}"

            # Basic PoW check
            if bits > INITIAL_BITS:
                return False, "bits exceeds minimum difficulty"

            return True, "OK"
        except Exception as e:
            return False, str(e)

    def handle_orphan(self, block: 'Block'):
        """Store orphan block for later processing."""
        with self._lock:
            if len(self._orphans) >= self.MAX_ORPHANS:
                oldest = min(self._orphans.keys(),
                             key=lambda h: self._orphans[h].height)
                del self._orphans[oldest]
            self._orphans[block.hash] = block

    def process_orphans(self) -> int:
        """Try to attach orphan blocks to main chain."""
        processed = 0
        with self._lock:
            for h, blk in list(self._orphans.items()):
                if blk.header.prev_hash == self._bc.tip.hash:
                    ok, msg = self._bc.add_block(blk)
                    if ok:
                        del self._orphans[h]
                        processed += 1
        return processed

    def detect_reorg(self, new_tip_hash: str,
                      new_tip_height: int) -> bool:
        """Detect if we need to reorganize the chain."""
        our_tip = self._bc.tip
        if new_tip_height <= our_tip.height:
            return False
        if self._bc.get_block_by_hash(new_tip_hash):
            return False   # already have this block
        return True

    def reorg_to(self, new_chain: List['Block']) -> Tuple[bool, str]:
        """
        Reorganize chain to new_chain if it has more PoW.
        Rolls back current chain to common ancestor, then applies new blocks.
        """
        if not new_chain:
            return False, "Empty chain"

        # Find common ancestor
        common_height = 0
        for i, blk in enumerate(new_chain):
            if self._bc.get_block_by_hash(blk.header.prev_hash):
                common_height = self._bc.get_block_by_hash(
                    blk.header.prev_hash).height
                break

        # Verify new chain has more cumulative work
        new_work = sum(bits_to_target(b.header.bits) for b in new_chain)
        cur_work = sum(
            bits_to_target(self._bc.get_block(h).header.bits)
            for h in range(common_height + 1, self._bc.height + 1)
            if self._bc.get_block(h)
        )

        if new_work >= cur_work:
            return False, "New chain does not have more work"

        return True, f"Reorg: {len(new_chain)} blocks from height {common_height+1}"

    def sync_status(self) -> dict:
        return self._state.to_dict()


# ---- PrunedChainStorage
class PrunedChainStorage:
    """
    Pruned node storage — keeps only recent blocks.
    Saves disk space while maintaining UTXO set integrity.
    Pruned nodes cannot serve old blocks to peers.
    """

    DEFAULT_PRUNE_HEIGHT = 1000   # keep last N blocks

    def __init__(self, blockchain: 'NEBULABlockchain',
                 prune_depth: int = DEFAULT_PRUNE_HEIGHT):
        self._bc          = blockchain
        self._prune_depth = prune_depth
        self._pruned_up_to: int = 0

    def prune_old_blocks(self) -> int:
        """Remove block data older than prune_depth. Returns pruned count."""
        cur       = self._bc.height
        prune_to  = cur - self._prune_depth
        if prune_to <= self._pruned_up_to:
            return 0
        # In real implementation, remove raw block data from disk.
        # UTXO set and headers are kept.
        pruned = prune_to - self._pruned_up_to
        self._pruned_up_to = prune_to
        return pruned

    def can_serve_block(self, height: int) -> bool:
        return height > self._pruned_up_to

    def storage_info(self) -> dict:
        cur = self._bc.height
        return {
            "pruned_up_to":   self._pruned_up_to,
            "blocks_kept":    max(0, cur - self._pruned_up_to),
            "prune_depth":    self._prune_depth,
            "is_pruned_node": self._pruned_up_to > 0,
        }


# ---- FastSyncManager
class FastSyncManager:
    """
    Fast sync using UTXO snapshot (assume-UTXO).
    Download a trusted UTXO snapshot and sync headers only,
    then verify from snapshot forward.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._snapshots: Dict[int, dict] = {}   # height -> snapshot info

    def register_snapshot(self, height: int,
                           utxo_hash: str,
                           block_hash: str):
        """Register a trusted UTXO snapshot."""
        self._snapshots[height] = {
            "height":      height,
            "utxo_hash":   utxo_hash,
            "block_hash":  block_hash,
            "trusted":     True,
        }

    def best_snapshot(self) -> Optional[dict]:
        """Return the most recent trusted snapshot."""
        if not self._snapshots:
            return None
        return self._snapshots[max(self._snapshots.keys())]

    def verify_snapshot(self, height: int) -> Tuple[bool, str]:
        """Verify current UTXO set matches snapshot at height."""
        snap = self._snapshots.get(height)
        if not snap:
            return False, "No snapshot at this height"
        blk = self._bc.get_block(height)
        if not blk:
            return False, "Block not found"
        if blk.hash != snap["block_hash"]:
            return False, "Block hash mismatch"
        # Compute UTXO hash
        utxo_data = json.dumps(
            {k: v.value for k, v in self._bc.utxo._utxos.items()},
            sort_keys=True
        ).encode()
        computed = hashlib.sha256(utxo_data).hexdigest()
        if computed != snap["utxo_hash"]:
            return False, "UTXO hash mismatch — snapshot invalid"
        return True, f"Snapshot at height {height} verified"


# ---- MnemonicRecoveryTool
class MnemonicRecoveryTool:
    """
    Tools for recovering wallets from partial mnemonics.
    Useful when some words are unknown or misspelled.
    """

    def __init__(self):
        self._wordlist = BIP39._wordlist if hasattr(BIP39, '_wordlist') else []

    def check_mnemonic(self, mnemonic: str) -> Tuple[bool, str]:
        """Validate a mnemonic phrase."""
        words = mnemonic.strip().split()
        if len(words) not in (12, 15, 18, 21, 24):
            return False, f"Wrong word count: {len(words)}"
        try:
            BIP39.mnemonic_to_seed(mnemonic)
            return True, "Valid mnemonic"
        except Exception as e:
            return False, str(e)

    def normalize_mnemonic(self, mnemonic: str) -> str:
        """Normalize mnemonic: lowercase, strip extra spaces."""
        return ' '.join(mnemonic.lower().strip().split())

    def derive_addresses(self, mnemonic: str,
                          count: int = 20,
                          path_prefix: str = "m/44'/2025'/0'/0") -> List[dict]:
        """Derive first N addresses from a mnemonic."""
        seed   = BIP39.mnemonic_to_seed(mnemonic)
        master = HDKey.from_seed(seed)
        result = []
        for i in range(count):
            key  = master.derive_path(f"{path_prefix}/{i}")
            result.append({
                "index":   i,
                "path":    f"{path_prefix}/{i}",
                "address": key.address,
                "wif":     key.wif,
            })
        return result

    def find_address_index(self, mnemonic: str,
                            target_address: str,
                            search_depth: int = 1000) -> Optional[int]:
        """Find which index generated a specific address."""
        seed   = BIP39.mnemonic_to_seed(mnemonic)
        master = HDKey.from_seed(seed)
        for i in range(search_depth):
            for path in [
                f"m/44'/2025'/0'/0/{i}",
                f"m/44'/2025'/0'/1/{i}",   # change addresses
            ]:
                try:
                    key = master.derive_path(path)
                    if key.address == target_address:
                        return i
                except Exception:
                    continue
        return None

    def recover_from_seed_hex(self, seed_hex: str) -> dict:
        """Recover wallet from raw seed hex (64 bytes)."""
        try:
            seed   = bytes.fromhex(seed_hex)
            if len(seed) != 64:
                return {"error": "Seed must be 64 bytes (128 hex chars)"}
            master = HDKey.from_seed(seed)
            addrs  = []
            for i in range(5):
                key = master.derive_path(f"m/44'/2025'/0'/0/{i}")
                addrs.append(key.address)
            return {
                "master_xpub": master.xpub() if hasattr(master, 'xpub') else "",
                "first_5_addresses": addrs,
            }
        except Exception as e:
            return {"error": str(e)}


# ---- PaperWalletImporter
class PaperWalletImporter:
    """Import keys from paper wallets (WIF, hex, address)."""

    def from_wif(self, wif: str) -> Tuple[bool, dict]:
        """Import private key from WIF format."""
        try:
            version, payload = base58check_decode(wif)
            if version not in (WIF_VERSION, 0x80):
                return False, {"error": f"Wrong WIF version: {version:#x}"}
            if len(payload) == 33 and payload[-1] == 0x01:
                privkey_bytes = payload[:-1]   # compressed
            else:
                privkey_bytes = payload
            privkey = int.from_bytes(privkey_bytes, 'big')
            pubkey  = Secp256k1.point_mul(privkey, Secp256k1.G())
            pub_b   = Secp256k1.pubkey_to_bytes(pubkey)
            address = Script.p2pkh_address(pub_b)
            return True, {
                "privkey_hex": privkey_bytes.hex(),
                "pubkey_hex":  pub_b.hex(),
                "address":     address,
                "wif":         wif,
            }
        except Exception as e:
            return False, {"error": str(e)}

    def from_privkey_hex(self, hex_key: str) -> Tuple[bool, dict]:
        """Import from raw private key hex."""
        try:
            privkey = int(hex_key, 16)
            if not (1 <= privkey < Secp256k1.N):
                return False, {"error": "Invalid private key range"}
            pubkey  = Secp256k1.point_mul(privkey, Secp256k1.G())
            pub_b   = Secp256k1.pubkey_to_bytes(pubkey)
            address = Script.p2pkh_address(pub_b)
            return True, {"address": address, "pubkey": pub_b.hex()}
        except Exception as e:
            return False, {"error": str(e)}

    def generate_paper_wallet(self) -> dict:
        """Generate a new paper wallet (offline-safe)."""
        privkey, pubkey = Secp256k1.generate_keypair()
        pub_b   = Secp256k1.pubkey_to_bytes(pubkey)
        address = Script.p2pkh_address(pub_b)
        wif_bytes = bytes([WIF_VERSION]) + privkey.to_bytes(32, 'big') + b'\x01'
        wif     = base58check_encode(privkey.to_bytes(32, 'big') + b'\x01', WIF_VERSION)
        return {
            "address":     address,
            "wif":         wif,
            "privkey_hex": privkey.to_bytes(32, 'big').hex(),
            "pubkey_hex":  pub_b.hex(),
            "warning":     "Store securely — never share private key!",
        }


# ---- WalletMigrationTool
class WalletMigrationTool:
    """Migrate wallets between formats and versions."""

    def export_watch_only(self, wallet: 'NEBULAWallet') -> dict:
        """Export wallet as watch-only (no private keys)."""
        addrs = [wallet.get_address(i) for i in range(20)]
        return {
            "type":      "watch_only",
            "addresses": addrs,
            "first":     addrs[0] if addrs else "",
            "exported":  time.time(),
        }

    def export_encrypted(self, wallet: 'NEBULAWallet',
                          password: str) -> dict:
        """Export wallet with encrypted mnemonic."""
        enc = _encrypt_mnemonic(wallet.mnemonic, password)
        return {
            "version":   2,
            "encrypted": enc,
            "hint":      "NEBULA HD Wallet v2",
            "exported":  time.time(),
        }

    def backup_summary(self, wallet: 'NEBULAWallet') -> str:
        """Generate human-readable backup summary."""
        lines = [
            "═" * 50,
            "  NEBULA WALLET BACKUP",
            "═" * 50,
            f"  Address: {wallet.first_address}",
            f"  Created: {time.strftime('%Y-%m-%d')}",
            "",
            "  SEED PHRASE (Keep Secret!):",
            "  " + wallet.mnemonic,
            "",
            "  BIP44 Path: m/44'/2025'/0'/0/x",
            "═" * 50,
        ]
        return "\n".join(lines)


# ---- NetMsgType
class NetMsgType:
    """All NEBULA P2P message type constants."""
    VERSION      = "version"
    VERACK       = "verack"
    PING         = "ping"
    PONG         = "pong"
    GETADDR      = "getaddr"
    ADDR         = "addr"
    INV          = "inv"
    GETDATA      = "getdata"
    NOTFOUND     = "notfound"
    GETBLOCKS    = "getblocks"
    GETHEADERS   = "getheaders"
    HEADERS      = "headers"
    BLOCK        = "block"
    TX           = "tx"
    MEMPOOL      = "mempool"
    FILTERLOAD   = "filterload"
    FILTERADD    = "filteradd"
    FILTERCLEAR  = "filterclear"
    MERKLEBLOCK  = "merkleblock"
    SENDHEADERS  = "sendheaders"
    FEEFILTER    = "feefilter"
    SENDCMPCT    = "sendcmpct"
    CMPCTBLOCK   = "cmpctblock"
    GETBLOCKTXN  = "getblocktxn"
    BLOCKTXN     = "blocktxn"
    REJECT       = "reject"
    ALERT        = "alert"
    GETINFO      = "getinfo"
    INFO         = "info"


# ---- RejectCode
class RejectCode:
    """Reason codes for REJECT messages."""
    MALFORMED    = 0x01
    INVALID      = 0x10
    OBSOLETE     = 0x11
    DUPLICATE    = 0x12
    NONSTANDARD  = 0x40
    DUST         = 0x41
    INSUFFICIENTFEE = 0x42
    CHECKPOINT   = 0x43


# ---- VestingSchedule
@dataclass
class VestingSchedule:
    schedule_id:  str
    beneficiary:  str
    token:        str       # "NBL" or NBL-20 contract_id
    total_amount: int
    cliff_blocks: int       # no tokens before cliff
    vest_blocks:  int       # linear vesting period after cliff
    start_block:  int
    claimed:      int = 0
    revocable:    bool = True
    revoked:      bool = False
    grantor:      str  = ""

    @property
    def end_block(self) -> int:
        return self.start_block + self.cliff_blocks + self.vest_blocks

    def vested_at(self, block_height: int) -> int:
        """Calculate vested amount at given block height."""
        if self.revoked:
            return self.claimed
        elapsed = block_height - self.start_block
        if elapsed < self.cliff_blocks:
            return 0   # before cliff
        vest_elapsed = min(elapsed - self.cliff_blocks, self.vest_blocks)
        if self.vest_blocks == 0:
            return self.total_amount
        vested = int(self.total_amount * vest_elapsed / self.vest_blocks)
        return min(vested, self.total_amount)

    def claimable_at(self, block_height: int) -> int:
        return max(0, self.vested_at(block_height) - self.claimed)

    def to_dict(self) -> dict:
        return {
            "schedule_id":  self.schedule_id,
            "beneficiary":  self.beneficiary,
            "token":        self.token,
            "total":        self.total_amount,
            "cliff_blocks": self.cliff_blocks,
            "vest_blocks":  self.vest_blocks,
            "start_block":  self.start_block,
            "end_block":    self.end_block,
            "claimed":      self.claimed,
            "revocable":    self.revocable,
            "revoked":      self.revoked,
        }


# ---- VestingManager
class VestingManager:
    """Manages token vesting schedules on NEBULA."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._schedules: Dict[str, VestingSchedule] = {}
        self._lock      = threading.RLock()

    def create_schedule(self, grantor: str, beneficiary: str,
                         token: str, total_nbl: float,
                         cliff_days: int = 90,
                         vest_days: int  = 365,
                         revocable: bool = True) -> str:
        with self._lock:
            total        = int(total_nbl * 10**DECIMALS)
            cliff_blocks = cliff_days * 144
            vest_blocks  = vest_days * 144
            sid = hashlib.sha256(
                f"VEST:{grantor}:{beneficiary}:{token}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._schedules[sid] = VestingSchedule(
                schedule_id  = sid,
                beneficiary  = beneficiary,
                token        = token,
                total_amount = total,
                cliff_blocks = cliff_blocks,
                vest_blocks  = vest_blocks,
                start_block  = self._bc.height,
                revocable    = revocable,
                grantor      = grantor,
            )
            return sid

    def claim(self, schedule_id: str,
               beneficiary: str) -> Tuple[bool, int]:
        with self._lock:
            s = self._schedules.get(schedule_id)
            if not s or s.beneficiary != beneficiary:
                return False, 0
            if s.revoked:
                return False, 0
            claimable = s.claimable_at(self._bc.height)
            if claimable <= 0:
                return False, 0
            s.claimed += claimable
            return True, claimable

    def revoke(self, schedule_id: str, grantor: str) -> Tuple[bool, str]:
        with self._lock:
            s = self._schedules.get(schedule_id)
            if not s or s.grantor != grantor:
                return False, "Not found or not grantor"
            if not s.revocable:
                return False, "Not revocable"
            if s.revoked:
                return False, "Already revoked"
            s.revoked = True
            unvested  = s.total_amount - s.vested_at(self._bc.height)
            return True, f"Revoked. {unvested/10**DECIMALS:.3f} tokens returned to grantor"

    def beneficiary_schedules(self, address: str) -> List[dict]:
        cur = self._bc.height
        result = []
        for s in self._schedules.values():
            if s.beneficiary == address:
                d = s.to_dict()
                d["vested"]    = s.vested_at(cur)
                d["claimable"] = s.claimable_at(cur)
                result.append(d)
        return result

    def vesting_stats(self) -> dict:
        with self._lock:
            total      = len(self._schedules)
            active     = sum(1 for s in self._schedules.values() if not s.revoked)
            total_vest = sum(s.total_amount for s in self._schedules.values())
            total_clmd = sum(s.claimed for s in self._schedules.values())
        return {
            "total_schedules": total,
            "active":          active,
            "total_vesting_nbl": f"{total_vest/10**DECIMALS:.3f}",
            "total_claimed_nbl": f"{total_clmd/10**DECIMALS:.3f}",
        }


# ---- ValidatorCandidate
@dataclass
class ValidatorCandidate:
    address:      str
    stake:        int
    pubkey:       bytes
    commission:   float
    joined_epoch: int
    votes:        int = 0
    performance:  float = 1.0   # 0.0 - 1.0

    def to_dict(self) -> dict:
        return {
            "address":     self.address,
            "stake_nbl":   f"{self.stake/10**DECIMALS:.3f}",
            "commission":  f"{self.commission*100:.1f}%",
            "performance": f"{self.performance*100:.1f}%",
            "votes":       self.votes,
        }


# ---- ValidatorSetManager
class ValidatorSetManager:
    """Manages the active validator set for NEBULA hybrid consensus."""

    MAX_VALIDATORS    = 100
    MIN_STAKE_TO_JOIN = 1_000 * 10**DECIMALS

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._candidates: Dict[str, ValidatorCandidate] = {}
        self._active_set: List[str] = []
        self._current_epoch: int    = 0
        self._epoch_history: List[dict] = []
        self._lock = threading.RLock()

    def current_epoch(self) -> int:
        return self._bc.height // EPOCH_BLOCKS

    def register(self, address: str, stake: int,
                  pubkey: bytes, commission: float) -> Tuple[bool, str]:
        with self._lock:
            if stake < self.MIN_STAKE_TO_JOIN:
                return False, f"Minimum stake: {self.MIN_STAKE_TO_JOIN/10**DECIMALS:.0f} NBL"
            if not (0.0 <= commission <= 0.20):
                return False, "Commission 0%-20% only"
            self._candidates[address] = ValidatorCandidate(
                address      = address,
                stake        = stake,
                pubkey       = pubkey,
                commission   = commission,
                joined_epoch = self.current_epoch(),
            )
            return True, f"Registered as validator candidate"

    def vote_for(self, voter: str, candidate: str,
                  weight: int) -> Tuple[bool, str]:
        with self._lock:
            c = self._candidates.get(candidate)
            if not c:
                return False, "Candidate not found"
            c.votes += weight
            return True, f"Voted for {candidate}"

    def rotate_epoch(self) -> List[str]:
        """Rotate validator set at epoch boundary."""
        with self._lock:
            epoch = self.current_epoch()
            if epoch <= self._current_epoch:
                return self._active_set

            # Sort by stake * votes * performance
            scored = sorted(
                self._candidates.values(),
                key=lambda v: v.stake * max(v.votes, 1) * v.performance,
                reverse=True
            )
            new_set = [v.address for v in scored[:self.MAX_VALIDATORS]]

            self._epoch_history.append({
                "epoch":      self._current_epoch,
                "validators": len(self._active_set),
                "rotated_at": self._bc.height,
            })
            self._active_set    = new_set
            self._current_epoch = epoch
            return new_set

    def is_active_validator(self, address: str) -> bool:
        return address in self._active_set

    def record_performance(self, address: str, signed: bool):
        with self._lock:
            c = self._candidates.get(address)
            if c:
                if signed:
                    c.performance = min(1.0, c.performance + 0.001)
                else:
                    c.performance = max(0.0, c.performance - 0.01)

    def validator_set_info(self) -> dict:
        return {
            "epoch":           self.current_epoch(),
            "active_count":    len(self._active_set),
            "candidate_count": len(self._candidates),
            "max_validators":  self.MAX_VALIDATORS,
            "epoch_blocks":    EPOCH_BLOCKS,
            "active_set":      self._active_set[:10],
        }
