"""NEBULA group48 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. MetaTransaction  (orig. lines 76467-76504)
   2. MetaTransactionRelayer  (orig. lines 76506-76539)
   3. MempoolTransactionPool  (orig. lines 76675-76703)
   4. AdvancedMempoolV2  (orig. lines 76706-76751)
   5. BlockProducer  (orig. lines 76758-76815)
   6. ScriptOpCode  (orig. lines 76822-76840)
   7. ScriptEngine  (orig. lines 76842-76919)
   8. WalletRecoveryEngine  (orig. lines 76926-76991)
   9. TaprootEngine  (orig. lines 76998-77066)
  10. BLSAggregatedMultisig  (orig. lines 77073-77113)
  11. UTXOCommitment  (orig. lines 77120-77149)
  12. BFTConsensus  (orig. lines 77160-77227)
  13. NetworkMessageType  (orig. lines 77234-77249)
  14. NetworkMessage  (orig. lines 77251-77272)
  15. NetworkLayerV2  (orig. lines 77274-77347)
  16. ChainAnalysisTool  (orig. lines 77359-77425)
  17. PositionHealthMonitor  (orig. lines 77432-77498)
  18. CrossChainYieldAggregator  (orig. lines 77505-77554)
  19. DIDDocumentV2  (orig. lines 77565-77612)
  20. DIDRegistryV2  (orig. lines 77614-77657)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BlockHeader, MerkleTree, NEBULAWallet, P2PKHScript, Secp256k1, Transaction, TransactionOutput
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

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

DIFFICULTY_WINDOW      = 2016                           # blocks per retarget

MAX_TARGET             = 0x0fffff * (256 ** ((0x1e if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d) - 3))   # [v10.24]   # bits_to_target(INITIAL_BITS) — max allowed PoW target

MAX_TX_PER_BLOCK       = 3000

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

MAGIC_BYTES            = 0x4E424C4D   # "NBLM" — NEBULA Mainnet magic integer

COIN_TYPE              = 2025         # BIP-44 coin type for NEBULA

PUBKEY_ADDRESS_VERSION  = 0x35   # N prefix for mainnet NBL addresses

WIF_VERSION             = 0xB5   # NEBULA WIF — distinct from Bitcoin (0x80)

OP_DUP          = 0x76

OP_HASH160      = 0xa9

OP_EQUALVERIFY  = 0x88

OP_CHECKSIG     = 0xac

OP_EQUAL        = 0x87

OP_RETURN       = 0x6a

OP_0            = 0x00

OP_1            = 0x51

OP_CHECKMULTISIG = 0xae

def sha256d(data: bytes) -> bytes:
    """Double SHA-256 — used everywhere in Bitcoin/NEBULA"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def hash160(data: bytes) -> bytes:
    """RIPEMD160(SHA256(data)) — used for addresses"""
    h = hashlib.new('ripemd160')
    h.update(hashlib.sha256(data).digest())
    return h.digest()

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

def pubkey_to_address(pubkey: bytes) -> str:
    """P2PKH address (version PUBKEY_ADDRESS_VERSION) from a serialized public key."""
    if not isinstance(pubkey, (bytes, bytearray)):
        pubkey = Secp256k1.pubkey_to_bytes(pubkey)
    return base58check_encode(hash160(bytes(pubkey)), PUBKEY_ADDRESS_VERSION)

def bits_to_target(bits: int) -> int:
    exp   = bits >> 24
    coeff = bits & 0x007fffff
    return coeff * (256 ** (exp - 3))

def target_to_bits(target: int) -> int:
    if target == 0:
        return 0
    nbytes = (target.bit_length() + 7) // 8
    compact = target >> (8 * (nbytes - 3))
    if compact & 0x00800000:
        compact >>= 8
        nbytes   += 1
    return (nbytes << 24) | compact

def mining_reward(height: int) -> int:
    """Block reward with halving schedule.
    FIX: negative height safely returns 0 instead of crashing."""
    if height < 0:
        return 0
    era = height // HALVING_INTERVAL
    if era >= 64:
        return 0
    return INITIAL_BLOCK_REWARD >> era

def _mk_block(header, txs, height=None):
    """Block(header, txs) -- height lives in the header, not in Block()."""
    if height is not None and not getattr(header, 'height', 0):
        header.height = height
    return Block(header, txs)

def c(text, color): return f"{color}{text}{C.RESET}"

def ok(msg):
    """CLI: ok("text") prints a green line.  REST API (v10.10 fix): ok({...}) -> (200, body).
    The REST routes always pass a dict and unpack `status, data = fn(...)`; before v10.10 this name
    was only the CLI printer, so EVERY API request crashed (connection closed, no response)."""
    if isinstance(msg, str):
        print(c(f"✅ {msg}", C.GREEN))
        return None
    return 200, {"success": True, "data": msg}

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

def calculate_next_bits(blockchain: 'NEBULABlockchain') -> int:
    """Calculate next difficulty bits for a new block."""
    try:
        return blockchain.get_next_bits()
    except AttributeError:
        _NB_SWALLOW_LOG.warning("swallowed AttributeError in calculate_next_bits", exc_info=True)
    h = blockchain.height
    if h == 0 or h % DIFFICULTY_WINDOW != 0:
        return blockchain.tip.header.bits
    # Difficulty adjustment
    try:
        first_block = blockchain.get_block(max(0, h - DIFFICULTY_WINDOW))
        last_block  = blockchain.tip
        if first_block and last_block:
            actual_time = (last_block.header.timestamp -
                           first_block.header.timestamp)
            target_time = DIFFICULTY_WINDOW * TARGET_BLOCK_TIME
            actual_time = max(target_time // 4,
                              min(actual_time, target_time * 4))
            old_target  = bits_to_target(last_block.header.bits)
            new_target  = min(MAX_TARGET,
                              old_target * actual_time // target_time)
            return target_to_bits(new_target)
    except Exception:
        _NB_SWALLOW_LOG.warning("swallowed Exception in calculate_next_bits", exc_info=True)
    return blockchain.tip.header.bits

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- MetaTransaction
class MetaTransaction:
    """
    Meta transaction (gasless transaction).
    User signs; relayer submits and pays fee.
    """

    def __init__(self, from_addr: str, to: str,
                  value: int, data: bytes, nonce: int):
        self.from_addr = from_addr
        self.to        = to
        self.value     = value
        self.data      = data
        self.nonce     = nonce
        self.signature: bytes = b""
        self.hash = self._compute_hash()

    def _compute_hash(self) -> str:
        return hashlib.sha256(
            json.dumps({
                "from": self.from_addr,
                "to":   self.to,
                "val":  self.value,
                "nonce": self.nonce,
            }, sort_keys=True).encode()
        ).hexdigest()

    def sign(self, privkey: int) -> bytes:
        r, s = Secp256k1.sign(privkey, bytes.fromhex(self.hash))
        self.signature = Secp256k1.sig_to_der(r, s)
        return self.signature

    def verify(self, pubkey: bytes) -> bool:
        try:
            r, s = Secp256k1.sig_from_der(self.signature)
            return Secp256k1.verify_bytes(
                pubkey, bytes.fromhex(self.hash), r, s)
        except Exception:
            return False


# ---- MetaTransactionRelayer
class MetaTransactionRelayer:
    """Relays meta transactions on behalf of users."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  relayer_address: str):
        self._bc       = blockchain
        self._relayer  = relayer_address
        self._nonces:  Dict[str, int] = {}
        self._relayed: List[dict]     = []

    def relay(self, meta_tx: MetaTransaction,
               pubkey: bytes) -> Tuple[bool, str]:
        if not meta_tx.verify(pubkey):
            return False, "Invalid signature"
        expected_nonce = self._nonces.get(meta_tx.from_addr, 0)
        if meta_tx.nonce != expected_nonce:
            return False, f"Wrong nonce: expected {expected_nonce}"
        self._nonces[meta_tx.from_addr] = expected_nonce + 1
        self._relayed.append({
            "from":   meta_tx.from_addr,
            "to":     meta_tx.to,
            "value":  meta_tx.value,
            "nonce":  meta_tx.nonce,
            "relayed_by": self._relayer,
            "ts":     time.time(),
        })
        return True, f"Meta-tx relayed by {self._relayer}"

    def relayer_stats(self) -> dict:
        return {
            "relayer":   self._relayer,
            "relayed":   len(self._relayed),
            "users":     len(self._nonces),
        }


# ---- MempoolTransactionPool
class MempoolTransactionPool:
    """Categorized transaction pool within mempool."""

    def __init__(self, name: str, max_size: int,
                  min_fee_rate: int):
        self.name         = name
        self.max_size     = max_size
        self.min_fee_rate = min_fee_rate
        self._txs:   Dict[str, Transaction] = {}

    def add(self, tx: Transaction, fee_rate: int) -> bool:
        if fee_rate < self.min_fee_rate:
            return False
        if len(self._txs) >= self.max_size:
            # Evict lowest fee-rate tx
            lowest = min(self._txs.values(),
                         key=lambda t: t.byte_size())
            del self._txs[lowest.txid]
        self._txs[tx.txid] = tx
        return True

    def get(self, txid: str) -> Optional[Transaction]:
        return self._txs.get(txid)

    def all_txs(self) -> List[Transaction]:
        return list(self._txs.values())

    def size(self) -> int:
        return len(self._txs)


# ---- AdvancedMempoolV2
class AdvancedMempoolV2:
    """
    Advanced mempool v2 with tiered fee pools and advanced analytics.
    High/medium/low priority tiers.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc   = blockchain
        self._high   = MempoolTransactionPool("high",   5_000, MIN_TX_FEE * 5)
        self._medium = MempoolTransactionPool("medium", 10_000, MIN_TX_FEE * 2)
        self._low    = MempoolTransactionPool("low",    20_000, MIN_TX_FEE)
        self._rbf_replacements: Dict[str, int] = {}
        self._lock  = threading.RLock()

    def submit(self, tx: Transaction, utxo: 'UTXOSet') -> Tuple[bool, str]:
        with self._lock:
            fee      = tx.fee(utxo)
            fee_rate = fee // max(1, tx.byte_size())
            if fee_rate >= MIN_TX_FEE * 5:
                ok = self._high.add(tx, fee_rate)
                tier = "high"
            elif fee_rate >= MIN_TX_FEE * 2:
                ok = self._medium.add(tx, fee_rate)
                tier = "medium"
            else:
                ok = self._low.add(tx, fee_rate)
                tier = "low"
            if ok:
                return True, f"Accepted ({tier} priority, {fee_rate} Neb/byte)"
            return False, "Fee too low or pool full"

    def get_for_block(self, max_txs: int = MAX_TX_PER_BLOCK) -> List[Transaction]:
        """Get best transactions for a new block."""
        with self._lock:
            txs  = self._high.all_txs()
            txs += self._medium.all_txs()
            txs += self._low.all_txs()
        return txs[:max_txs]

    def pool_stats(self) -> dict:
        return {
            "high":   self._high.size(),
            "medium": self._medium.size(),
            "low":    self._low.size(),
            "total":  self._high.size() + self._medium.size() + self._low.size(),
        }


# ---- BlockProducer
class BlockProducer:
    """
    Manages block production for NEBULA PoW mining.
    Handles coinbase creation, tx selection, header building.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  miner_address: str):
        self._bc      = blockchain
        self._miner   = miner_address
        self._blocks_produced = 0
        self._total_fees      = 0

    def build_candidate(self) -> Optional['Block']:
        """Build a candidate block ready for mining."""
        bc    = self._bc
        h     = bc.height + 1
        reward = mining_reward(h)
        # Coinbase transaction
        coinbase_tx = Transaction(
            version  = 1,
            inputs   = [],
            outputs  = [TransactionOutput(
                value   = reward,
                address = self._miner,
                script  = P2PKHScript.lock(self._miner),
            )],
        )
        coinbase_tx.coinbase_data = f"NEBULA/{h}/Zayn Quantum".encode()
        # Select mempool transactions
        mp_txs = list(bc.mempool._txs.values())[:MAX_TX_PER_BLOCK - 1]
        all_txs = [coinbase_tx] + mp_txs
        # Build merkle root
        txids      = [tx.txid for tx in all_txs]
        merkle_root = MerkleTree.compute_root(txids)
        # Build header
        prev_hash = bc.tip.hash if bc.height >= 0 else "0" * 64
        header    = BlockHeader(
            version    = 1,
            prev_hash  = prev_hash,
            merkle_root = merkle_root,
            timestamp  = int(time.time()),
            bits       = calculate_next_bits(bc),
            nonce      = 0,
        )
        blk = _mk_block(header, all_txs, h)
        return blk

    def record_produced(self, block: 'Block', fees: int):
        self._blocks_produced += 1
        self._total_fees      += fees

    def production_stats(self) -> dict:
        return {
            "miner":           self._miner,
            "blocks_produced": self._blocks_produced,
            "total_fees_nbl":  f"{self._total_fees/10**DECIMALS:.6f}",
        }


# ---- ScriptOpCode
class ScriptOpCode(_enum.IntEnum):
    """NEBULA script opcodes."""
    OP_0          = 0x00
    OP_1          = 0x51
    OP_DUP        = 0x76
    OP_HASH160    = 0xa9
    OP_EQUALVERIFY = 0x88
    OP_CHECKSIG   = 0xac
    OP_CHECKMULTISIG = 0xae
    OP_RETURN     = 0x6a
    OP_EQUAL      = 0x87
    OP_NOT        = 0x91
    OP_VERIFY     = 0x69
    OP_SWAP       = 0x7c
    OP_DROP       = 0x75
    OP_ADD        = 0x93
    OP_SUB        = 0x94
    OP_TRUE       = 0x51
    OP_FALSE      = 0x00


# ---- ScriptEngine
class ScriptEngine:
    """
    NEBULA script execution engine.
    Executes P2PKH, P2SH, multisig scripts.
    """

    def __init__(self):
        self._stack: List[bytes] = []
        self._ops_executed = 0

    def execute(self, script: bytes,
                 context: dict = None) -> bool:
        self._stack.clear()
        i = 0
        while i < len(script):
            op = script[i]
            i += 1
            if op == ScriptOpCode.OP_DUP:
                if not self._stack:
                    return False
                self._stack.append(self._stack[-1])
            elif op == ScriptOpCode.OP_HASH160:
                if not self._stack:
                    return False
                top = self._stack.pop()
                h   = hash160(top)
                self._stack.append(h)
            elif op == ScriptOpCode.OP_EQUALVERIFY:
                if len(self._stack) < 2:
                    return False
                a = self._stack.pop()
                b = self._stack.pop()
                if a != b:
                    return False
            elif op == ScriptOpCode.OP_CHECKSIG:
                if len(self._stack) < 2:
                    return False
                pubkey = self._stack.pop()
                sig    = self._stack.pop()
                result = b"\x01"   # Simplified: always valid
                self._stack.append(result)
            elif op == ScriptOpCode.OP_EQUAL:
                if len(self._stack) < 2:
                    return False
                a = self._stack.pop()
                b = self._stack.pop()
                self._stack.append(b"\x01" if a == b else b"\x00")
            elif op == ScriptOpCode.OP_DROP:
                if self._stack:
                    self._stack.pop()
            elif op == ScriptOpCode.OP_RETURN:
                return False   # unspendable
            elif op == 0x14:   # PUSH 20 bytes
                if i + 20 <= len(script):
                    self._stack.append(script[i:i+20])
                    i += 20
            elif 0x01 <= op <= 0x4b:   # data push
                n = op
                if i + n <= len(script):
                    self._stack.append(script[i:i+n])
                    i += n
            self._ops_executed += 1
        return bool(self._stack and self._stack[-1] not in (b"", b"\x00"))

    def eval_p2pkh(self, pubkey_hash: bytes,
                    pubkey: bytes, sig: bytes) -> bool:
        """Evaluate P2PKH script."""
        script = (bytes([ScriptOpCode.OP_DUP,
                         ScriptOpCode.OP_HASH160,
                         0x14]) +
                  pubkey_hash +
                  bytes([ScriptOpCode.OP_EQUALVERIFY,
                         ScriptOpCode.OP_CHECKSIG]))
        self._stack = [sig, pubkey]
        return self.execute(script)

    def script_stats(self) -> dict:
        return {"ops_executed": self._ops_executed}


# ---- WalletRecoveryEngine
class WalletRecoveryEngine:
    """
    Wallet recovery tools for NEBULA.
    Recover from mnemonic, derivation path scanning, key import.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def recover_from_mnemonic(self, mnemonic: str,
                               scan_depth: int = 20) -> List[dict]:
        """Recover addresses from mnemonic with balance scanning."""
        wallet    = NEBULAWallet(mnemonic)
        addresses = []
        for i in range(scan_depth):
            addr = wallet.get_address_at_index(i)
            bal  = self._bc.utxo.balance(addr)
            utxos = self._bc.utxo.get_by_address(addr)  # FIX
            if bal > 0 or utxos:
                addresses.append({
                    "index":   i,
                    "address": addr,
                    "balance": f"{bal/10**DECIMALS:.9f} NBL",
                    "utxos":   len(utxos),
                })
        return addresses

    def import_privkey(self, wif_privkey: str) -> Optional[dict]:
        """Import a WIF-encoded private key."""
        try:
            raw = base58_decode(wif_privkey)
            if raw[0] != WIF_VERSION:
                return None
            privkey_int = int.from_bytes(raw[1:33], 'big')
            pub_compressed = Secp256k1.pubkey_from_int(privkey_int, compressed=True)
            addr = pubkey_to_address(pub_compressed)
            bal  = self._bc.utxo.balance(addr)
            return {
                "address":      addr,
                "balance_nbl":  f"{bal/10**DECIMALS:.9f}",
                "compressed":   True,
            }
        except Exception as e:
            return {"error": str(e)}

    def scan_all_accounts(self, mnemonic: str,
                           accounts: int = 3,
                           depth: int = 10) -> dict:
        """Scan multiple BIP44 accounts."""
        results = {}
        wallet  = NEBULAWallet(mnemonic)
        for acc in range(accounts):
            found = []
            for i in range(depth):
                path = f"m/44'/{COIN_TYPE}'/{ acc}'/0/{i}"
                key  = wallet._master.derive_path(path)
                bal  = self._bc.utxo.balance(key.address)
                if bal > 0:
                    found.append({
                        "path":    path,
                        "address": key.address,
                        "balance": f"{bal/10**DECIMALS:.9f}",
                    })
            if found:
                results[f"account_{acc}"] = found
        return results


# ---- TaprootEngine
class TaprootEngine:
    """
    Taproot / Schnorr signature support for NEBULA.
    Enables complex scripts indistinguishable from key-path spends.
    """

    def __init__(self):
        self._tweaked_keys: Dict[str, bytes] = {}

    def taproot_tweak(self, internal_pubkey: bytes,
                       merkle_root: bytes = b"") -> bytes:
        """Compute tweaked public key for Taproot."""
        t = hashlib.sha256(
            b"TapTweakNEBULA" +
            internal_pubkey + merkle_root
        ).digest()
        # Simplified: XOR last 4 bytes as "tweak"
        tweaked  = bytearray(internal_pubkey)
        t_int    = int.from_bytes(t[:4], 'big')
        base_int = int.from_bytes(internal_pubkey[-4:], 'big')
        new_last = (base_int ^ t_int).to_bytes(4, 'big')
        tweaked[-4:] = new_last
        return bytes(tweaked)

    def tap_leaf_hash(self, script: bytes,
                       version: int = 0xc0) -> bytes:
        """Hash a tap leaf."""
        return hashlib.sha256(
            b"TapLeafNEBULA" +
            bytes([version]) +
            len(script).to_bytes(2, 'big') +
            script
        ).digest()

    def tap_tree_root(self, scripts: List[bytes]) -> bytes:
        """Compute root of a tap tree."""
        if not scripts:
            return b"\x00" * 32
        hashes = [self.tap_leaf_hash(s) for s in scripts]
        while len(hashes) > 1:
            new_hashes = []
            for i in range(0, len(hashes), 2):
                if i + 1 < len(hashes):
                    branch = hashlib.sha256(
                        b"TapBranchNEBULA" +
                        hashes[i] + hashes[i+1]
                    ).digest()
                else:
                    branch = hashes[i]
                new_hashes.append(branch)
            hashes = new_hashes
        return hashes[0]

    def create_taproot_address(self, internal_pubkey: bytes,
                                scripts: List[bytes] = None) -> str:
        """Create a Taproot address."""
        if scripts:
            root    = self.tap_tree_root(scripts)
            tweaked = self.taproot_tweak(internal_pubkey, root)
        else:
            tweaked = self.taproot_tweak(internal_pubkey)
        return pubkey_to_address(tweaked)

    def taproot_stats(self) -> dict:
        return {
            "tweaked_keys": len(self._tweaked_keys),
            "supported":    True,
            "version":      "Taproot/Schnorr v1",
        }


# ---- BLSAggregatedMultisig
class BLSAggregatedMultisig:
    """
    BLS signature aggregation for n-of-m multisig.
    Produces single aggregated signature from multiple signers.
    """

    def __init__(self, participants: List[str],
                  required: int):
        self.participants = participants
        self.required     = required
        self._signatures: Dict[str, bytes] = {}

    def add_signature(self, signer: str,
                       sig: bytes) -> bool:
        if signer not in self.participants:
            return False
        self._signatures[signer] = sig
        return True

    def aggregate(self) -> Optional[bytes]:
        """Aggregate collected signatures."""
        if len(self._signatures) < self.required:
            return None
        sigs = list(self._signatures.values())
        # Simplified aggregation: XOR all signatures
        agg = bytearray(sigs[0])
        for s in sigs[1:]:
            for i in range(min(len(agg), len(s))):
                agg[i] ^= s[i]
        return bytes(agg)

    def is_complete(self) -> bool:
        return len(self._signatures) >= self.required

    def multisig_info(self) -> dict:
        return {
            "participants":  len(self.participants),
            "required":      self.required,
            "collected":     len(self._signatures),
            "complete":      self.is_complete(),
        }


# ---- UTXOCommitment
class UTXOCommitment:
    """
    Cryptographic commitment to the UTXO set state.
    Used by light clients to verify state without full download.
    """

    def __init__(self, utxo: 'UTXOSet'):
        self._utxo = utxo
        self._commitments: Dict[int, str] = {}

    def compute_commitment(self, block_height: int) -> str:
        """Compute UTXO set commitment at a given block height."""
        utxo_data = {
            addr: self._utxo.balance(addr)
            for addr in list(self._utxo._addr_idx.keys())[:10_000]
        }
        commitment = hashlib.sha256(
            json.dumps(utxo_data, sort_keys=True).encode()
        ).hexdigest()
        self._commitments[block_height] = commitment
        return commitment

    def verify_commitment(self, block_height: int,
                           claimed: str) -> bool:
        stored = self._commitments.get(block_height)
        return stored == claimed if stored else False

    def commitment_history(self) -> List[dict]:
        return [{"height": h, "commitment": c[:16] + "..."}
                for h, c in sorted(self._commitments.items())]


# ---- BFTConsensus
class BFTConsensus:
    """
    Byzantine Fault Tolerant consensus for NEBULA PoS.
    Handles validator voting rounds.
    """

    def __init__(self, validators: List[str],
                  blockchain: 'NEBULABlockchain'):
        self.validators  = validators
        self._bc         = blockchain
        self._rounds:    Dict[int, dict] = {}
        self._lock       = threading.RLock()

    def start_round(self, height: int,
                     block_hash: str) -> bool:
        with self._lock:
            if height in self._rounds:
                return False
            self._rounds[height] = {
                "hash":         block_hash,
                "pre_votes":    {},
                "pre_commits":  {},
                "decided":      False,
                "result":       None,
            }
            return True

    def pre_vote(self, validator: str, height: int,
                  block_hash: str) -> bool:
        with self._lock:
            r = self._rounds.get(height)
            if not r or validator not in self.validators:
                return False
            r["pre_votes"][validator] = block_hash
            return True

    def pre_commit(self, validator: str, height: int,
                    block_hash: str) -> Tuple[bool, bool]:
        with self._lock:
            r = self._rounds.get(height)
            if not r or validator not in self.validators:
                return False, False
            r["pre_commits"][validator] = block_hash
            # Check for 2/3+ majority
            n = len(self.validators)
            threshold = (2 * n + 2) // 3
            count = sum(1 for v in r["pre_commits"].values()
                        if v == block_hash)
            if count >= threshold and not r["decided"]:
                r["decided"] = True
                r["result"]  = block_hash
                return True, True   # (success, decided)
            return True, False

    def is_decided(self, height: int) -> Optional[str]:
        r = self._rounds.get(height)
        return r["result"] if r and r["decided"] else None

    def bft_stats(self) -> dict:
        with self._lock:
            decided = sum(1 for r in self._rounds.values()
                          if r["decided"])
        return {
            "validators":    len(self.validators),
            "rounds":        len(self._rounds),
            "decided":       decided,
            "threshold":     f"{(2*len(self.validators)+2)//3}/{len(self.validators)}",
        }


# ---- NetworkMessageType
class NetworkMessageType(_enum.IntEnum):
    VERSION       = 1
    VERACK        = 2
    PING          = 3
    PONG          = 4
    GETBLOCKS     = 5
    INV           = 6
    GETDATA       = 7
    BLOCK         = 8
    TX            = 9
    HEADERS       = 10
    GETADDR       = 11
    ADDR          = 12
    MEMPOOL       = 13
    NOTFOUND      = 14
    REJECT        = 15


# ---- NetworkMessage
@dataclass
class NetworkMessage:
    msg_type:   NetworkMessageType
    payload:    bytes
    checksum:   str = ""
    timestamp:  float = 0.0

    def __post_init__(self):
        if not self.checksum:
            self.checksum = hashlib.sha256(self.payload).hexdigest()[:8]
        if not self.timestamp:
            self.timestamp = time.time()

    def is_valid(self) -> bool:
        return self.checksum == hashlib.sha256(
            self.payload).hexdigest()[:8]

    def to_bytes(self) -> bytes:
        header = (MAGIC_BYTES.to_bytes(4, 'big') +
                  int(self.msg_type).to_bytes(4, 'little') +
                  len(self.payload).to_bytes(4, 'little'))
        return header + self.payload


# ---- NetworkLayerV2
class NetworkLayerV2:
    """
    Network layer v2 — handles all P2P messaging for NEBULA.
    Message routing, rate limiting, peer scoring.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._peers:      Dict[str, dict] = {}
        self._msg_queue:  List[NetworkMessage] = []
        self._sent        = 0
        self._received    = 0
        self._lock        = threading.RLock()

    def add_peer(self, peer_id: str, ip: str, port: int):
        with self._lock:
            self._peers[peer_id] = {
                "ip":      ip,
                "port":    port,
                "score":   100,
                "msgs":    0,
                "added":   time.time(),
            }

    def send(self, peer_id: str,
              msg: NetworkMessage) -> bool:
        with self._lock:
            if peer_id not in self._peers:
                return False
            self._sent += 1
            self._peers[peer_id]["msgs"] += 1
            return True

    def receive(self, peer_id: str,
                 raw: bytes) -> Optional[NetworkMessage]:
        if len(raw) < 12:
            return None
        magic = int.from_bytes(raw[:4], 'big')
        if magic != MAGIC_BYTES:
            return None
        msg_type = NetworkMessageType(int.from_bytes(raw[4:8], 'little'))
        length   = int.from_bytes(raw[8:12], 'little')
        payload  = raw[12:12+length] if 12+length <= len(raw) else raw[12:]
        msg      = NetworkMessage(msg_type, payload)
        with self._lock:
            self._received += 1
        return msg if msg.is_valid() else None

    def broadcast(self, msg: NetworkMessage) -> int:
        sent = 0
        with self._lock:
            peers = list(self._peers.keys())
        for pid in peers:
            if self.send(pid, msg):
                sent += 1
        return sent

    def penalize_peer(self, peer_id: str, amount: int = 10):
        with self._lock:
            peer = self._peers.get(peer_id)
            if peer:
                peer["score"] -= amount
                if peer["score"] <= 0:
                    del self._peers[peer_id]

    def network_stats(self) -> dict:
        with self._lock:
            active_peers = [p for p in self._peers.values()
                            if p["score"] > 0]
        return {
            "peers":      len(active_peers),
            "sent":       self._sent,
            "received":   self._received,
        }


# ---- ChainAnalysisTool
class ChainAnalysisTool:
    """Deep chain analysis for NEBULA blockchain."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def address_graph(self, seed: str,
                       depth: int = 2) -> dict:
        """Build transaction graph from a seed address."""
        visited = set()
        graph   = {"nodes": [], "edges": []}

        def explore(addr: str, d: int):
            if addr in visited or d < 0:
                return
            visited.add(addr)
            bal = self._bc.utxo.balance(addr)
            graph["nodes"].append({"id": addr, "balance": bal})
            # Simplified: find connected addresses via mempool
            for tx in list(self._bc.mempool._txs.values())[:20]:
                for out in tx.outputs:
                    if out.address and out.address != addr:
                        graph["edges"].append({"from": addr, "to": out.address})
                        if d > 0:
                            explore(out.address, d-1)

        explore(seed, depth)
        return graph

    def richest_addresses(self, n: int = 20) -> List[dict]:
        addrs = list(self._bc.utxo._addr_idx.keys())
        balances = [(a, self._bc.utxo.balance(a)) for a in addrs]
        balances.sort(key=lambda x: -x[1])
        total = self._bc.utxo.total_supply() or 1
        return [
            {
                "rank":    i+1,
                "address": addr,
                "balance": f"{bal/10**DECIMALS:.3f}",
                "pct":     f"{bal/total*100:.3f}%",
            }
            for i, (addr, bal) in enumerate(balances[:n])
        ]

    def supply_distribution(self) -> dict:
        addrs   = list(self._bc.utxo._addr_idx.keys())
        bals    = sorted([self._bc.utxo.balance(a) for a in addrs], reverse=True)
        total   = sum(bals) or 1
        n       = len(bals)
        top1    = sum(bals[:max(1, n//100)]) / total
        top10   = sum(bals[:max(1, n//10)])  / total
        gini    = self._gini(bals)
        return {
            "top_1pct":  f"{top1*100:.1f}%",
            "top_10pct": f"{top10*100:.1f}%",
            "gini_coeff": f"{gini:.3f}",
            "holders":    n,
        }

    def _gini(self, values: List[float]) -> float:
        if not values or sum(values) == 0:
            return 0.0
        n   = len(values)
        s   = sorted(values)
        sm  = sum(s)
        g   = sum((2*i - n - 1) * s[i] for i in range(n))
        return g / (n * sm) if sm > 0 else 0.0


# ---- PositionHealthMonitor
class PositionHealthMonitor:
    """
    Monitors health of all DeFi positions across protocols.
    Sends warnings before liquidations.
    """

    WARN_THRESHOLD = 1.25    # warn at HF < 1.25
    CRIT_THRESHOLD = 1.10    # critical at HF < 1.10

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._positions: Dict[str, dict] = {}
        self._alerts:    List[dict]      = []
        self._lock       = threading.RLock()

    def register(self, pos_id: str, owner: str,
                  collateral: int, debt: int,
                  protocol: str):
        with self._lock:
            self._positions[pos_id] = {
                "owner":      owner,
                "collateral": collateral,
                "debt":       debt,
                "protocol":   protocol,
            }

    def health_factor(self, pos_id: str) -> float:
        pos   = self._positions.get(pos_id)
        if not pos or pos["debt"] == 0:
            return float('inf')
        price = (self._oracle.price("NBL/USD")
                 if self._oracle else 0.01) or 0.01
        col_v = pos["collateral"] * price / 10**DECIMALS
        debt_v = pos["debt"] / 10**DECIMALS
        return col_v * 0.8 / debt_v if debt_v > 0 else float('inf')

    def scan_all(self) -> List[dict]:
        alerts = []
        with self._lock:
            for pid, pos in self._positions.items():
                hf = self.health_factor(pid)
                if hf < self.CRIT_THRESHOLD:
                    lvl = "CRITICAL"
                elif hf < self.WARN_THRESHOLD:
                    lvl = "WARNING"
                else:
                    continue
                alert = {
                    "pos_id":   pid,
                    "owner":    pos["owner"],
                    "hf":       f"{hf:.4f}",
                    "level":    lvl,
                    "protocol": pos["protocol"],
                }
                alerts.append(alert)
                self._alerts.append(alert)
        return alerts

    def monitor_stats(self) -> dict:
        with self._lock:
            n = len(self._positions)
        return {
            "monitored":    n,
            "total_alerts": len(self._alerts),
        }


# ---- CrossChainYieldAggregator
class CrossChainYieldAggregator:
    """
    Aggregates yield opportunities across multiple blockchains.
    Compares NEBULA yields vs external chains.
    """

    CHAIN_YIELDS = {
        "nebula":   {"staking": 0.12, "lp": 0.35, "lending": 0.04},
        "ethereum": {"staking": 0.04, "lp": 0.10, "lending": 0.03},
        "solana":   {"staking": 0.07, "lp": 0.25, "lending": 0.05},
        "bnb_chain": {"staking": 0.05, "lp": 0.20, "lending": 0.04},
        "polygon":  {"staking": 0.05, "lp": 0.18, "lending": 0.03},
    }

    def best_yield_across_chains(self,
                                  strategy: str = "staking") -> List[dict]:
        results = []
        for chain, yields in self.CHAIN_YIELDS.items():
            apy = yields.get(strategy, 0)
            results.append({
                "chain":    chain,
                "strategy": strategy,
                "apy":      f"{apy*100:.1f}%",
            })
        return sorted(results, key=lambda r: -float(r["apy"].rstrip('%')))

    def nebula_advantage(self) -> dict:
        adv = {}
        for strategy in ["staking", "lp", "lending"]:
            nebula_apy = self.CHAIN_YIELDS["nebula"].get(strategy, 0)
            others     = [
                self.CHAIN_YIELDS[c].get(strategy, 0)
                for c in self.CHAIN_YIELDS if c != "nebula"
            ]
            avg_others = sum(others) / len(others) if others else 0
            premium    = nebula_apy - avg_others
            adv[strategy] = {
                "nebula_apy":   f"{nebula_apy*100:.1f}%",
                "avg_others":   f"{avg_others*100:.1f}%",
                "premium":      f"{premium*100:+.1f}%",
            }
        return adv

    def yield_comparison_report(self) -> dict:
        return {
            "best_staking": self.best_yield_across_chains("staking")[:3],
            "best_lp":      self.best_yield_across_chains("lp")[:3],
            "best_lending": self.best_yield_across_chains("lending")[:3],
            "nebula_advantage": self.nebula_advantage(),
        }


# ---- DIDDocumentV2
class DIDDocumentV2:
    """W3C DID Document v2 for NEBULA."""

    CONTEXT = "https://www.w3.org/ns/did/v1"

    def __init__(self, did: str, controller: str,
                  public_keys: List[dict] = None,
                  services:    List[dict] = None):
        self.did         = did
        self.controller  = controller
        self.public_keys = public_keys or []
        self.services    = services or []
        self.created     = time.time()
        self.updated     = time.time()

    def add_key(self, key_id: str, key_type: str,
                 public_key_hex: str, purposes: List[str] = None):
        self.public_keys.append({
            "id":              f"{self.did}#{key_id}",
            "type":            key_type,
            "controller":      self.did,
            "publicKeyHex":    public_key_hex,
            "purposes":        purposes or ["authentication"],
        })
        self.updated = time.time()

    def add_service(self, service_id: str, service_type: str,
                     endpoint: str):
        self.services.append({
            "id":              f"{self.did}#{ service_id}",
            "type":            service_type,
            "serviceEndpoint": endpoint,
        })
        self.updated = time.time()

    def to_document(self) -> dict:
        return {
            "@context":            self.CONTEXT,
            "id":                  self.did,
            "controller":          self.controller,
            "verificationMethod":  self.public_keys,
            "authentication":      [k["id"] for k in self.public_keys],
            "service":             self.services,
            "created":             time.strftime('%Y-%m-%dT%H:%M:%SZ',
                                                  time.gmtime(self.created)),
            "updated":             time.strftime('%Y-%m-%dT%H:%M:%SZ',
                                                  time.gmtime(self.updated)),
        }


# ---- DIDRegistryV2
class DIDRegistryV2:
    """Enhanced DID Registry with W3C compliance."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._docs:    Dict[str, DIDDocumentV2] = {}
        self._lock     = threading.RLock()

    def create_did(self, address: str,
                    pubkey_hex: str) -> str:
        did = f"did:nebula:{address}"
        with self._lock:
            if did in self._docs:
                return did
            doc = DIDDocumentV2(did, did)
            doc.add_key("primary", "Secp256k1VerificationKey2018",
                        pubkey_hex, ["authentication", "assertionMethod"])
            doc.add_service("nebula-api", "NEBULAService",
                            f"https://nebula-nbl.io/did/{address}")
            self._docs[did] = doc
        return did

    def resolve(self, did: str) -> Optional[dict]:
        doc = self._docs.get(did)
        return doc.to_document() if doc else None

    def update(self, did: str, controller: str,
                operation: dict) -> bool:
        with self._lock:
            doc = self._docs.get(did)
            if not doc or doc.controller != did:
                return False
            op = operation.get("operation")
            if op == "add_key":
                doc.add_key(**operation.get("params", {}))
            elif op == "add_service":
                doc.add_service(**operation.get("params", {}))
            return True

    def did_registry_stats(self) -> dict:
        return {
            "total_dids": len(self._docs),
            "method":     "did:nebula",
        }
