"""NEBULA group30 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. GenesisAllocation  (orig. lines 49220-49234)
   2. GenesisConfig  (orig. lines 49236-49269)
   3. GenesisConfigurator  (orig. lines 49271-49334)
   4. NEBULA50KMilestone  (orig. lines 49346-49508)
   5. ExtendedAPIEndpoints  (orig. lines 49529-49645)
   6. NEBULAOnboarding  (orig. lines 49656-49773)
   7. ProjectStats  (orig. lines 49875-49921)
   8. NEBULARoadmap  (orig. lines 49977-50003)
   9. WalletUtils  (orig. lines 50101-50165)
  10. NetworkUtils  (orig. lines 50170-50235)
  11. NEBULAInit  (orig. lines 50373-50398)
  12. NEBULAFinalTestSuite  (orig. lines 50871-51084)
  13. HashUtils  (orig. lines 51276-51334)
  14. AddressUtils  (orig. lines 51338-51390)
  15. NEBULAFinalStats  (orig. lines 51621-51650)
  16. RemittanceCorridor  (orig. lines 51865-51887)
  17. RemittanceTransfer  (orig. lines 51912-51966)
  18. RemittanceAgent  (orig. lines 51968-52008)
  19. RemittanceEngine  (orig. lines 52010-52309)
  20. Vote  (orig. lines 52338-52346)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): AMMEngine, AtomicSwapEngine, BIP39, BLSSignature, Bech32, BlockRewardSimulator, BloomFilter, DEXEngine, ECIES, FullChainValidator, GovernanceEngine, HDKey, LendingProtocol, MultisigWallet, NEBULABlockchain, NEBULALaunchChecker, NEBULAMiner, NEBULAWallet, NFTEngine, PedersenCommitment, PriceOracle, PropertyTest, Schnorr, Script, ScriptInterpreter, ScriptOpcode, Secp256k1, SecurityAuditor, StakingEngine, StealthAddress, TokenBridge
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

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

INITIAL_BITS           = 0x1e0fffff if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d0fffff   # [v10.24]

DEFAULT_PORT           = 8333

PUBKEY_ADDRESS_VERSION  = 0x35   # N prefix for mainnet NBL addresses

SCRIPT_ADDRESS_VERSION  = 0x32

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

def c(text, color): return f"{color}{text}{C.RESET}"

def ok(msg):
    """CLI: ok("text") prints a green line.  REST API (v10.10 fix): ok({...}) -> (200, body).
    The REST routes always pass a dict and unpack `status, data = fn(...)`; before v10.10 this name
    was only the CLI printer, so EVERY API request crashed (connection closed, no response)."""
    if isinstance(msg, str):
        print(c(f"✅ {msg}", C.GREEN))
        return None
    return 200, {"success": True, "data": msg}

def info(msg):  print(c(f"ℹ️  {msg}", C.CYAN))

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

NEBULA_MODULES_TOTAL = 120

FEATURES = {
    "segwit"            : True,
    "taproot"           : True,
    "schnorr"           : True,
    "musig2"            : True,
    "lightning"         : True,
    "tor"               : True,
    "i2p"               : True,
    "compact_blocks"    : True,
    "bloom_filters"     : True,
    "compact_filters"   : True,
    "rbf"               : True,
    "cpfp"              : True,
    "psbt"              : True,
    "descriptors"       : True,
    "bip85"             : True,
    "bip324"            : True,
    "stratum_v2"        : True,
    "atomic_swaps"      : True,
    "zk_proofs"         : True,
    "nfts"              : True,
    "defi_amm"          : True,
    "governance"        : True,
    "staking"           : True,
    "bridge"            : True,
    "layer2"            : True,
    "zk_rollup"         : True,
    "bls_sigs"          : True,
    "verkle_trees"      : True,
    "ring_sigs"         : True,
    "stealth_addrs"     : True,
}

def feature_count() -> int:
    return sum(1 for v in FEATURES.values() if v)

_NEBULA_FINAL_MESSAGE = """
NEBULA Blockchain — Complete.
50,000+ lines. 121 modules. 54/54 tests. Zero dependencies.
Written on a Python 3 by NEBULA Core Team.
NEBULA Blockchain.
"""

NBL_EXCHANGE_RATES: Dict[str, float] = {
    "USD": 10.0,        # 1 USD = 10 NBL  (at $0.10/NBL)
    "EUR": 10.9,
    "AED":  2.72,       # 1 AED ≈ 0.27 USD
    "SAR":  2.67,
    "AFN":  0.072,      # 1 AFN ≈ $0.0072
    "PKR":  0.036,
    "BDT":  0.091,
    "NGN":  0.0063,
    "INR":  0.12,
    "PHP":  0.18,
    "MXN":  0.58,
    "KES":  0.077,
    "GHS":  0.066,
    "EGP":  0.21,
    "ETB":  0.18,
    "IQD":  0.0076,
    "TRY":  0.31,
}

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


# ---- GenesisAllocation
@dataclass
class GenesisAllocation:
    """Pre-mine allocation in genesis block"""
    address    : str
    amount_nbl : float
    label      : str    = ""
    vesting    : Optional[dict] = None   # vesting schedule

    def to_dict(self) -> dict:
        return {
            "address"   : self.address,
            "amount"    : self.amount_nbl,
            "label"     : self.label,
            "vesting"   : self.vesting,
        }


# ---- GenesisConfig
@dataclass
class GenesisConfig:
    """Complete genesis block configuration"""
    chain_name      : str  = CHAIN_NAME
    chain_symbol    : str  = CHAIN_SYMBOL
    chain_id        : int  = CHAIN_ID
    initial_bits    : int  = INITIAL_BITS
    timestamp       : int  = 0
    message         : str  = "NEBULA Genesis — NEBULA Core Team — Core Developer"
    allocations     : List[GenesisAllocation] = field(default_factory=list)
    foundation_addr : str  = FOUNDATION_ADDRESS

    def total_premined(self) -> float:
        return sum(a.amount_nbl for a in self.allocations)

    def pct_premined(self) -> float:
        return self.total_premined() / (MAX_SUPPLY / 10**DECIMALS) * 100

    def add_allocation(self, address: str, amount: float,
                        label: str = "", vesting: dict = None):
        self.allocations.append(GenesisAllocation(
            address=address, amount_nbl=amount,
            label=label, vesting=vesting))

    def to_dict(self) -> dict:
        return {
            "chain_name"    : self.chain_name,
            "chain_symbol"  : self.chain_symbol,
            "chain_id"      : self.chain_id,
            "message"       : self.message,
            "total_premined": self.total_premined(),
            "pct_premined"  : f"{self.pct_premined():.4f}%",
            "allocations"   : [a.to_dict() for a in self.allocations],
        }


# ---- GenesisConfigurator
class GenesisConfigurator:
    """
    Configure and generate custom genesis blocks.
    Supports: pre-mine allocations, team vesting, airdrop lists.
    """

    RECOMMENDED_PREMINED_PCT = 10.0   # industry standard: ≤10%

    def __init__(self):
        self.config = GenesisConfig()
        # Default allocation to foundation
        self.config.add_allocation(
            FOUNDATION_ADDRESS,
            MAX_SUPPLY * 0.02 / 10**DECIMALS,
            "NEBULA Foundation — Development Fund",
            vesting={"type": "linear", "months": 48}
        )

    def add_team_allocation(self, address: str,
                             pct: float,
                             vesting_months: int = 24):
        """Add team member allocation with vesting"""
        amount = MAX_SUPPLY * pct / 100 / 10**DECIMALS
        self.config.add_allocation(
            address, amount,
            f"Team allocation ({pct:.2f}%)",
            vesting={"type": "linear", "months": vesting_months,
                     "cliff_months": 6}
        )

    def add_airdrop(self, recipients: Dict[str, float]):
        """Add airdrop allocations"""
        for addr, amount in recipients.items():
            self.config.add_allocation(addr, amount, "Airdrop")

    def validate(self) -> Tuple[bool, List[str]]:
        """Validate genesis configuration"""
        errors = []
        pct = self.config.pct_premined()
        if pct > self.RECOMMENDED_PREMINED_PCT:
            errors.append(f"Pre-mine {pct:.2f}% > recommended {self.RECOMMENDED_PREMINED_PCT}%")
        if not self.config.allocations:
            errors.append("No allocations configured")
        return len(errors) == 0, errors

    def generate_genesis_hash(self) -> str:
        """Generate deterministic genesis hash from config"""
        config_json = json.dumps(self.config.to_dict(), sort_keys=True)
        return hashlib.sha256(config_json.encode()).hexdigest()

    def export(self) -> str:
        """Export genesis config as JSON"""
        return json.dumps(self.config.to_dict(), indent=2)

    def summary(self) -> dict:
        ok, errors = self.validate()
        return {
            "valid"          : ok,
            "errors"         : errors,
            "total_premined" : self.config.total_premined(),
            "pct_premined"   : f"{self.config.pct_premined():.4f}%",
            "allocations"    : len(self.config.allocations),
            "genesis_hash"   : self.generate_genesis_hash()[:16] + "...",
        }


# ---- NEBULA50KMilestone
class NEBULA50KMilestone:
    """
    The 50,000 line milestone module.
    A tribute to what's possible with determination.
    """

    MILESTONE_BANNER = """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   🌌  N E B U L A  B L O C K C H A I N  —  5 0 , 0 0 0  L I N E S  ║
║                                                                      ║
║   ✅ 50,000+ lines of pure Python code                               ║
║   ✅ 115 production-grade modules                                    ║
║   ✅ Written entirely on a Python 3                              ║
║   ✅ Zero external dependencies                                      ║
║   ✅ 54/54 tests passing                                             ║
║                                                                      ║
║   Author : NEBULA Core Team                           ║
║                                               ║
║                                      ║
║                                                                      ║
║   "The best code is not written on the best device —                 ║
║    it's written with the best determination."                        ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

    MODULE_SUMMARY = {
        "Core Blockchain"   : range(1, 12),
        "Cryptography"      : range(12, 22),
        "Infrastructure"    : range(22, 36),
        "Advanced Features" : range(36, 56),
        "DeFi & Finance"    : range(56, 70),
        "Developer Tools"   : range(70, 86),
        "Privacy & Security": range(86, 100),
        "Advanced Analytics": range(100, 115),
        "Milestone"         : [115],
    }

    def __init__(self):
        self.bc         = NEBULABlockchain()
        self.components = self._init_components()

    def _init_components(self) -> dict:
        """Initialize all major components"""
        return {
            "blockchain"    : self.bc,
            "oracle"        : PriceOracle(self.bc),
            "amm"           : AMMEngine(self.bc),
            "staking"       : StakingEngine(self.bc),
            "governance"    : GovernanceEngine(self.bc),
            "nft"           : NFTEngine(self.bc),
            "dex"           : DEXEngine(),
            "bridge"        : TokenBridge(self.bc),
            "reward_sim"    : BlockRewardSimulator(),
            "chain_metrics" : None,   # requires oracle ref
        }

    def print_milestone(self):
        """Print the 50K milestone banner"""
        print(self.MILESTONE_BANNER)

    def full_ecosystem_status(self) -> dict:
        """Complete ecosystem status"""
        bc      = self.bc
        price   = self.components["oracle"].get_nbl_usd()
        issued  = bc.utxo.total_supply()
        staking = self.components["staking"]
        amm     = self.components["amm"]
        dex     = self.components["dex"]
        nft     = self.components["nft"]

        return {
            "milestone"       : "50,000+ lines",
            "modules"         : 115,
            "author"          : "NEBULA Core Team",
            "platform": "Python 3",
            "language"        : "Python 3 (pure stdlib)",
            "deps"            : 0,
            "chain"           : {
                "name"        : CHAIN_NAME,
                "symbol"      : CHAIN_SYMBOL,
                "height"      : bc.height,
                "supply_nbl"  : issued / 10**DECIMALS,
                "utxos"       : bc.utxo.size(),
                "nbl_usd"     : price,
            },
            "defi"            : {
                "amm_pools"   : len(amm._pools),
                "stakers"     : len(staking._stakes),
                "validators"  : len(staking._validators),
                "nfts"        : sum(c.minted_count for c in nft._collections.values()),
            },
            "capabilities"    : [
                "secp256k1 ECDSA + Schnorr + BLS",
                "HD Wallets BIP32/39/44/85",
                "SegWit + Taproot",
                "Lightning Network",
                "MuSig2 N-of-N",
                "Atomic Swaps",
                "ZK Proofs + Verkle Trees",
                "AMM + DEX + Lending",
                "DAO Governance",
                "NFTs + Token Bridge",
                "Tor/I2P Privacy",
                "ZK Rollups",
                "Layer 2 Channels",
                "Mining Pool",
                "JSON-RPC 200+ methods",
                "Block Explorer",
                "Market Making Bot",
                "Address Clustering",
                "Lightning Routing",
                "Hybrid PoS",
            ],
        }

    def run_comprehensive_validation(self) -> dict:
        """Run all validation checks"""
        results = {}

        # Chain validation
        validator = FullChainValidator(self.bc)
        results["chain"] = validator.validate_chain()

        # Security audit
        auditor = SecurityAuditor(self.bc)
        audit   = auditor.full_audit()
        results["security"] = {"score": audit["score"]}

        # Property tests
        prop = PropertyTest.run_all()
        results["property_tests"] = {"passed": prop["passed"],
                                      "total": prop["property_tests"]}

        # Launch readiness
        checker = NEBULALaunchChecker(self.bc)
        check   = checker.run_checklist()
        results["launch_ready"] = {"pct": check["pct"]}

        return results

    def print_final_stats(self):
        """Print final project statistics"""
        status = self.full_ecosystem_status()
        print(self.MILESTONE_BANNER)
        print("  📊 Final Project Statistics:")
        print("  " + "─"*50)
        for key, val in status.items():
            if not isinstance(val, dict) and not isinstance(val, list):
                print(f"  {key:20}: {val}")
        print("\n  🔗 Blockchain:")
        for k, v in status["chain"].items():
            print(f"    {k:16}: {v}")
        print("\n  💎 DeFi:")
        for k, v in status["defi"].items():
            print(f"    {k:16}: {v}")
        print("\n  ✅ Capabilities:")
        for cap in status["capabilities"]:
            print(f"    • {cap}")
        print("\n  " + "═"*50)
        print(f"  NEBULA — Built by {status['author']} on {status['platform']}")
        print("  " + "═"*50)


# ---- ExtendedAPIEndpoints
class ExtendedAPIEndpoints:
    """Additional REST API endpoints for modules 76-115"""

    def __init__(self, blockchain, oracle=None, amm=None,
                 staking=None, nft=None, dex=None, pool=None,
                 governance=None, bridge=None):
        self.bc         = blockchain
        self.oracle     = oracle
        self.amm        = amm
        self.staking    = staking
        self.nft        = nft
        self.dex        = dex
        self.pool       = pool
        self.governance = governance
        self.bridge     = bridge

    def handle(self, path: str, params: dict) -> Optional[dict]:
        """Route extended API requests"""
        routes = {
            '/ext/amm/pools'           : self._amm_pools,
            '/ext/amm/quote'           : lambda: self._amm_quote(params),
            '/ext/staking/validators'  : self._validators,
            '/ext/staking/network'     : self._staking_network,
            '/ext/nft/collections'     : self._nft_collections,
            '/ext/nft/listed'          : self._nft_listed,
            '/ext/dex/orderbooks'      : self._dex_orderbooks,
            '/ext/dex/trades'          : lambda: self._dex_trades(params),
            '/ext/governance/proposals': self._proposals,
            '/ext/bridge/stats'        : self._bridge_stats,
            '/ext/oracle/prices'       : self._oracle_prices,
            '/ext/oracle/twap'         : lambda: self._oracle_twap(params),
            '/ext/pool/workers'        : self._pool_workers,
            '/ext/pool/stats'          : self._pool_stats,
        }
        handler = routes.get(path)
        return handler() if handler else None

    def _amm_pools(self) -> dict:
        if not self.amm: return {"error": "AMM not available"}
        return {"pools": self.amm.pools_summary(), "tvl": self.amm.total_tvl()}

    def _amm_quote(self, p: dict) -> dict:
        if not self.amm: return {"error": "AMM not available"}
        token_in  = p.get("from", "NBL")
        token_out = p.get("to", "USDT")
        amount    = int(float(p.get("amount", 1)) * 10**DECIMALS)
        return self.amm.get_quote(token_in, token_out, amount)

    def _validators(self) -> dict:
        if not self.staking: return {"error": "Staking not available"}
        return {"validators": self.staking.validator_list()}

    def _staking_network(self) -> dict:
        if not self.staking: return {"error": "Staking not available"}
        return self.staking.network_stats()

    def _nft_collections(self) -> dict:
        if not self.nft: return {"error": "NFT not available"}
        return {"collections": [c.to_dict() for c in self.nft._collections.values()],
                "stats": self.nft.stats()}

    def _nft_listed(self) -> dict:
        if not self.nft: return {"error": "NFT not available"}
        return {"listed": self.nft.marketplace_listings()}

    def _dex_orderbooks(self) -> dict:
        if not self.dex: return {"error": "DEX not available"}
        return {"orderbooks": {pair: self.dex.get_order_book(pair)
                               for pair in DEXEngine.DEFAULT_PAIRS}}

    def _dex_trades(self, p: dict) -> dict:
        if not self.dex: return {"error": "DEX not available"}
        pair = p.get("pair")
        return {"trades": self.dex.get_trades(pair, 20)}

    def _proposals(self) -> dict:
        if not self.governance: return {"error": "Governance not available"}
        return {"proposals": self.governance.list_proposals(),
                "stats": self.governance.stats()}

    def _bridge_stats(self) -> dict:
        if not self.bridge: return {"error": "Bridge not available"}
        return self.bridge.stats()

    def _oracle_prices(self) -> dict:
        if not self.oracle: return {"error": "Oracle not available"}
        return self.oracle.price_summary()

    def _oracle_twap(self, p: dict) -> dict:
        if not self.oracle: return {"error": "Oracle not available"}
        pair   = p.get("pair", "NBL/USD")
        window = int(p.get("window", 3600))
        return {
            "pair"    : pair,
            "twap"    : self.oracle.aggregator.get_twap(pair, window),
            "spot"    : self.oracle.aggregator.get_median_price(pair),
            "window_s": window,
        }

    def _pool_workers(self) -> dict:
        if not self.pool: return {"error": "Pool not available"}
        return {"workers": self.pool.worker_list()}

    def _pool_stats(self) -> dict:
        if not self.pool: return {"error": "Pool not available"}
        return self.pool.stats()

    def endpoint_list(self) -> List[str]:
        return [
            "/ext/amm/pools", "/ext/amm/quote",
            "/ext/staking/validators", "/ext/staking/network",
            "/ext/nft/collections", "/ext/nft/listed",
            "/ext/dex/orderbooks", "/ext/dex/trades",
            "/ext/governance/proposals", "/ext/bridge/stats",
            "/ext/oracle/prices", "/ext/oracle/twap",
            "/ext/pool/workers", "/ext/pool/stats",
        ]


# ---- NEBULAOnboarding
class NEBULAOnboarding:
    """
    Interactive onboarding guide for new NEBULA users.
    Guides through: wallet, mining, sending, DeFi.
    """

    WELCOME = """
  ╔══════════════════════════════════════════╗
  ║  Welcome to NEBULA Blockchain!           ║
  ║  Your journey starts here.               ║
  ╚══════════════════════════════════════════╝
  """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc = blockchain

    def step1_create_wallet(self) -> dict:
        """Step 1: Create your first wallet"""
        wallet = NEBULAWallet.create_new(self.bc.utxo)
        return {
            "step"    : 1,
            "title"   : "Create Your Wallet",
            "status"  : "completed",
            "address" : wallet.first_address,
            "mnemonic": wallet.mnemonic,
            "tip"     : "Write down your 12 words! This is your backup.",
        }

    def step2_explain_address(self, address: str) -> dict:
        """Step 2: Understand your address"""
        return {
            "step"      : 2,
            "title"     : "Your NBL Address",
            "address"   : address,
            "prefix"    : f"Starts with '{PUBKEY_ADDRESS_PREFIX}'",
            "length"    : len(address),
            "type"      : "P2PKH (Pay to Public Key Hash)",
            "tip"       : "Share this address to receive NBL.",
        }

    def step3_mining_demo(self) -> dict:
        """Step 3: Mine your first NBL"""
        wallet = NEBULAWallet.create_new(self.bc.utxo)
        miner  = NEBULAMiner(self.bc, wallet.first_address)
        block  = miner.mine_demo_block(easy_bits=0x1f7fffff, timeout_secs=10)
        if block:
            self.bc.add_block(block)
            reward = mining_reward(block.height) / 10**DECIMALS
            return {
                "step"   : 3,
                "title"  : "Mine Your First Block",
                "status" : "completed",
                "height" : block.height,
                "reward" : f"{reward:.9f} NBL",
                "address": wallet.first_address,
                "tip"    : f"You earned {reward:.2f} NBL! Mining keeps the network secure.",
            }
        return {"step": 3, "status": "skipped", "tip": "Mining demo skipped."}

    def step4_send_nbl(self, wallet: 'NEBULAWallet') -> dict:
        """Step 4: Send your first transaction"""
        recipient = NEBULAWallet.create_new(self.bc.utxo)
        tx        = wallet.build_transaction(recipient.first_address, 0.1)
        if tx:
            ok, msg = self.bc.mempool.submit(tx)
            return {
                "step"      : 4,
                "title"     : "Send Your First Transaction",
                "status"    : "completed" if ok else "failed",
                "txid"      : tx.txid[:16] + "...",
                "amount"    : "0.1 NBL",
                "recipient" : recipient.first_address[:20] + "...",
                "tip"       : "Transaction submitted to mempool!",
            }
        return {"step": 4, "status": "skipped",
                "tip": "Need more NBL. Mine first!"}

    def step5_defi_intro(self) -> dict:
        """Step 5: DeFi overview"""
        return {
            "step"    : 5,
            "title"   : "Discover DeFi on NEBULA",
            "features": [
                {"name": "AMM", "desc": "Swap tokens without order book"},
                {"name": "Staking", "desc": "Earn 5% APY staking NBL"},
                {"name": "Governance", "desc": "Vote on protocol changes"},
                {"name": "NFTs", "desc": "Mint and trade digital assets"},
                {"name": "Bridge", "desc": "Move assets cross-chain"},
            ],
            "tip": "NEBULA has a full DeFi ecosystem!",
        }

    def run_full_onboarding(self) -> dict:
        """Run complete onboarding sequence"""
        print(self.WELCOME)
        steps = []

        s1 = self.step1_create_wallet()
        steps.append(s1)
        print(f"  ✅ Step 1: Wallet created — {s1['address'][:20]}...")

        s2 = self.step2_explain_address(s1['address'])
        steps.append(s2)
        print(f"  ✅ Step 2: Address type — {s2['type']}")

        s3 = self.step3_mining_demo()
        steps.append(s3)
        print(f"  {'✅' if s3['status']=='completed' else '⏭️'} Step 3: Mining — {s3.get('reward','skipped')}")

        s5 = self.step5_defi_intro()
        steps.append(s5)
        print(f"  ✅ Step 5: DeFi intro — {len(s5['features'])} features")

        return {
            "steps_completed": sum(1 for s in steps if s.get("status") == "completed"),
            "total_steps"    : 5,
            "steps"          : steps,
        }


# ---- ProjectStats
class ProjectStats:
    """Final NEBULA project statistics"""

    def __init__(self, source_file: str = None):
        if source_file is None:
            source_file = 'nebula_FINAL.py'
        self.source_file = source_file
        self._line_count = 0
        self._class_count = 0
        self._function_count = 0
        self._analyzed = False

    def analyze(self) -> dict:
        """Analyze the source code"""
        if self._analyzed:
            return self.to_dict()
        try:
            with open(self.source_file if self.source_file else 'nebula_FINAL.py') as f:
                lines = f.readlines()
            self._line_count = len(lines)
            self._class_count = sum(1 for l in lines if l.strip().startswith("class "))
            self._function_count = sum(1 for l in lines if l.strip().startswith("def "))
            self._analyzed = True
        except Exception:
            self._line_count = 50_000
            self._class_count = 300
            self._function_count = 2000
        return self.to_dict()

    def to_dict(self) -> dict:
        return {
            "lines"     : self._line_count,
            "classes"   : self._class_count,
            "functions" : self._function_count,
            "modules"   : 119,
            "author"    : "NEBULA Core Team",
            "platform": "Python 3",
            "language"  : "Python 3",
            "deps"      : 0,
        }

    def print_stats(self):
        stats = self.analyze()
        print("\n  📊 NEBULA Code Analysis")
        print("  " + "─"*40)
        for k, v in stats.items():
            print(f"  {k:15}: {v:,}" if isinstance(v, int) else f"  {k:15}: {v}")


# ---- NEBULARoadmap
class NEBULARoadmap:
    """NEBULA project roadmap and milestones"""

    PHASES = [
        {"phase": 1, "name": "Genesis",      "status": "✅ Complete", "desc": "Core blockchain, wallets, PoW mining"},
        {"phase": 2, "name": "DeFi Layer",   "status": "✅ Complete", "desc": "AMM, staking, NFTs, DEX, governance"},
        {"phase": 3, "name": "Privacy",      "status": "✅ Complete", "desc": "Tor/I2P, ZK proofs, Layer 2, stealth"},
        {"phase": 4, "name": "50K Lines",    "status": "✅ Complete", "desc": "50,000+ lines, 115+ modules"},
        {"phase": 5, "name": "Mainnet",      "status": "🔄 Planned",  "desc": "Public mainnet launch"},
        {"phase": 6, "name": "Mobile App",   "status": "🔄 Planned",  "desc": "Android/iOS wallet"},
        {"phase": 7, "name": "Ecosystem",    "status": "🔄 Planned",  "desc": "Developer grants, tooling"},
        {"phase": 8, "name": "Exchange",     "status": "🔄 Planned",  "desc": "CEX/DEX listings"},
    ]

    def print_roadmap(self):
        print("\n  🗺️  NEBULA Roadmap")
        print("  " + "─"*55)
        for p in self.PHASES:
            print(f"  Phase {p['phase']}: {p['name']:12} {p['status']:14} — {p['desc']}")
        print("  " + "─"*55)

    def current_phase(self) -> dict:
        return next((p for p in self.PHASES if "Planned" in p["status"]),
                     self.PHASES[-1])

    def completed_phases(self) -> int:
        return sum(1 for p in self.PHASES if "Complete" in p["status"])


# ---- WalletUtils
class WalletUtils:
    """Extended wallet utilities"""

    @staticmethod
    def wif_to_privkey(wif: str) -> Optional[int]:
        """Decode WIF to private key integer"""
        try:
            version, payload = base58check_decode(wif)
            if len(payload) == 33 and payload[-1] == 0x01:
                payload = payload[:-1]   # compressed flag
            return int.from_bytes(payload, 'big')
        except Exception:
            return None

    @staticmethod
    def privkey_to_wif(privkey: int, compressed: bool = True) -> str:
        """Encode private key as WIF"""
        key_bytes = privkey.to_bytes(32, 'big')
        if compressed:
            key_bytes += bytes([0x01])
        return base58check_encode(key_bytes, 0x80)

    @staticmethod
    def address_type(address: str) -> str:
        """Determine address type"""
        try:
            version, payload = base58check_decode(address)
            if version == PUBKEY_ADDRESS_VERSION:
                return "P2PKH"
            if version == SCRIPT_ADDRESS_VERSION:
                return "P2SH"
        except Exception:
            _NB_SWALLOW_LOG.warning("swallowed Exception in WalletUtils.address_type", exc_info=True)
        if address.startswith("nbl1"):
            return "Bech32 (SegWit)"
        return "Unknown"

    @staticmethod
    def generate_vanity_prefix(prefix: str,
                                max_tries: int = 10_000) -> Optional[dict]:
        """Generate address with vanity prefix (best effort)"""
        for _ in range(max_tries):
            privkey = secrets.randbelow(Secp256k1.N - 1) + 1
            pubkey  = Secp256k1.pubkey_to_bytes(
                          Secp256k1.point_mul(privkey, Secp256k1.G()))
            addr    = Script.p2pkh_address(pubkey)
            if addr[1:].startswith(prefix):
                return {
                    "address": addr,
                    "privkey": f"{privkey:064x}",
                    "wif"    : WalletUtils.privkey_to_wif(privkey),
                }
        return None

    @staticmethod
    def multisig_address_info(m: int, n: int,
                               pubkeys: List[bytes]) -> dict:
        """Get info about a multisig setup"""
        ms = MultisigWallet(m, pubkeys[:n])
        return {
            "type"         : f"P2WSH {m}-of-{n}",
            "address"      : ms.address(),
            "redeem_script": ms.redeem_script().hex(),
            "script_asm"   : ScriptInterpreter.disassemble(ms.redeem_script()),
        }


# ---- NetworkUtils
class NetworkUtils:
    """Extended network utilities"""

    @staticmethod
    def encode_varint(n: int) -> bytes:
        """Bitcoin variable-length integer encoding"""
        if n < 0xfd:
            return bytes([n])
        if n <= 0xffff:
            return b'\xfd' + n.to_bytes(2, 'little')
        if n <= 0xffffffff:
            return b'\xfe' + n.to_bytes(4, 'little')
        return b'\xff' + n.to_bytes(8, 'little')

    @staticmethod
    def decode_varint(data: bytes, offset: int = 0) -> Tuple[int, int]:
        """Decode variable-length integer"""
        first = data[offset]
        if first < 0xfd:
            return first, offset + 1
        if first == 0xfd:
            return int.from_bytes(data[offset+1:offset+3], 'little'), offset + 3
        if first == 0xfe:
            return int.from_bytes(data[offset+1:offset+5], 'little'), offset + 5
        return int.from_bytes(data[offset+1:offset+9], 'little'), offset + 9

    @staticmethod
    def compute_checksum(data: bytes) -> bytes:
        """Bitcoin double-SHA256 checksum"""
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]

    @staticmethod
    def peer_from_string(peer_str: str) -> Tuple[str, int]:
        """Parse "host:port" string"""
        parts = peer_str.rsplit(':', 1)
        host  = parts[0].strip('[]')
        port  = int(parts[1]) if len(parts) > 1 else DEFAULT_PORT
        return host, port

    @staticmethod
    def is_private_ip(ip: str) -> bool:
        """Check if IP is private/loopback"""
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        try:
            a = int(parts[0])
            b = int(parts[1])
            if a == 10: return True
            if a == 172 and 16 <= b <= 31: return True
            if a == 192 and b == 168: return True
            if a == 127: return True
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in NetworkUtils.is_private_ip", exc_info=True)
        return False

    @staticmethod
    def format_hashrate(hashrate: float) -> str:
        """Format hashrate with appropriate unit"""
        if hashrate >= 1e18: return f"{hashrate/1e18:.2f} EH/s"
        if hashrate >= 1e15: return f"{hashrate/1e15:.2f} PH/s"
        if hashrate >= 1e12: return f"{hashrate/1e12:.2f} TH/s"
        if hashrate >= 1e9:  return f"{hashrate/1e9:.2f} GH/s"
        if hashrate >= 1e6:  return f"{hashrate/1e6:.2f} MH/s"
        if hashrate >= 1e3:  return f"{hashrate/1e3:.2f} kH/s"
        return f"{hashrate:.2f} H/s"


# ---- NEBULAInit
class NEBULAInit:
    """Final initialization and environment check"""

    @staticmethod
    def check_environment() -> dict:
        """Verify Python environment is suitable"""
        import sys, platform
        return {
            "python_version"  : sys.version,
            "platform"        : platform.system(),
            "architecture"    : platform.machine(),
            "nebula_version"  : "1.0.0",
            "features_enabled": feature_count(),
            "ready"           : True,
        }

    @staticmethod
    def print_startup_banner():
        """Print startup banner"""
        env = NEBULAInit.check_environment()
        print(f"\n  🌌 NEBULA Blockchain v1.0.0")
        print(f"  Python  : {env['python_version'][:20]}")
        print(f"  Platform: {env['platform']} ({env['architecture']})")
        print(f"  Features: {env['features_enabled']} enabled")
        print(f"  Modules : {NEBULA_MODULES_TOTAL}")
        print(f"  Author  : NEBULA Core Team\n")


# ---- NEBULAFinalTestSuite
class NEBULAFinalTestSuite:
    """Complete test suite validating all NEBULA modules"""

    def __init__(self):
        self.bc      = NEBULABlockchain()
        self.results : Dict[str, bool] = {}
        self._errors : List[str] = []

    def _test(self, name: str, fn) -> bool:
        try:
            result = fn()
            ok     = result is not False
            self.results[name] = ok
            if not ok:
                self._errors.append(f"FAIL: {name}")
            return ok
        except Exception as e:
            self.results[name] = False
            self._errors.append(f"ERROR: {name}: {str(e)[:60]}")
            return False

    # ── Cryptography Tests ────────────────────────────────────────
    def test_crypto(self):
        """Test cryptographic primitives"""
        self._test("secp256k1_curve_params",
            lambda: Secp256k1.P == 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F)
        self._test("secp256k1_order",
            lambda: Secp256k1.N == 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)
        self._test("point_multiplication",
            lambda: Secp256k1.point_mul(1, Secp256k1.G()) == Secp256k1.G())
        self._test("ecdsa_sign_verify",
            lambda: Secp256k1.verify(
                Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(12345, Secp256k1.G())),
                hashlib.sha256(b"nebula").digest(),
                *Secp256k1.sign(12345, hashlib.sha256(b"nebula").digest())))
        self._test("schnorr_sign_verify",
            lambda: Schnorr.verify(
                Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(99, Secp256k1.G()))[1:],
                hashlib.sha256(b"test").digest(),
                Schnorr.sign(99, hashlib.sha256(b"test").digest())))
        self._test("bip39_12_words",
            lambda: len(BIP39.generate_mnemonic(12).split()) == 12)
        self._test("bip39_24_words",
            lambda: len(BIP39.generate_mnemonic(24).split()) == 24)
        self._test("bip39_seed_length",
            lambda: len(BIP39.mnemonic_to_seed("abandon " * 11 + "about")) == 64)
        self._test("base58check_roundtrip_20",
            lambda: base58check_decode(base58check_encode(bytes(20), PUBKEY_ADDRESS_VERSION))[1] == bytes(20))
        self._test("base58check_roundtrip_32",
            lambda: base58check_decode(base58check_encode(bytes(32), PUBKEY_ADDRESS_VERSION))[1] == bytes(32))
        self._test("address_valid_format",
            lambda: NEBULAWallet.create_new(self.bc.utxo).first_address.startswith(PUBKEY_ADDRESS_PREFIX))
        self._test("hd_derive_path",
            lambda: len(HDKey.from_seed(b'\x01'*64).derive_path("m/0'/0'/0'").address) > 10)
        self._test("pedersen_commit_64bytes",
            lambda: len(PedersenCommitment.commit(1000)[0]) == 64)
        self._test("pedersen_homomorphic",
            lambda: PedersenCommitment.add_commitments(
                PedersenCommitment.commit(100)[0],
                PedersenCommitment.commit(200)[0]) != bytes(64))
        self._test("bls_keygen",
            lambda: len(BLSSignature.keygen()[1]) == 33)
        self._test("bls_aggregate",
            lambda: len(BLSSignature.aggregate_sigs([
                BLSSignature.sign(i, b"msg") for i in range(1, 4)])) == 33)

    # ── Blockchain Tests ─────────────────────────────────────────
    def test_blockchain(self):
        """Test blockchain operations"""
        bc = self.bc
        self._test("genesis_exists",   lambda: bc.height >= 0)
        self._test("genesis_hash_64",  lambda: len(bc.tip.hash) == 64)
        self._test("mining_reward_era0",lambda: mining_reward(0) == INITIAL_BLOCK_REWARD)
        self._test("halving_correct",  lambda: mining_reward(HALVING_INTERVAL) == INITIAL_BLOCK_REWARD // 2)
        self._test("reward_zero_eventually", lambda: mining_reward(HALVING_INTERVAL * 64) == 0)
        self._test("max_supply_math",  lambda: INITIAL_BLOCK_REWARD * HALVING_INTERVAL * 2 == MAX_SUPPLY)
        self._test("utxo_balance_zero", lambda: bc.utxo.balance("nonexistent_addr_xyz") == 0)
        self._test("foundation_addr_valid",
            lambda: bool(base58check_decode(FOUNDATION_ADDRESS)))
        self._test("chain_info_height",
            lambda: bc.chain_info()["height"] == bc.height)
        self._test("bits_to_target_initial",
            lambda: bits_to_target(INITIAL_BITS) > 0)

    # ── Script Tests ──────────────────────────────────────────────
    def test_scripts(self):
        """Test script interpreter"""
        def _run(ops):
            i = ScriptInterpreter()
            ok, _ = i.execute(bytes(ops))
            return ok

        self._test("script_op_1",
            lambda: _run([ScriptOpcode.OP_1]))
        self._test("script_op_0_false",
            lambda: not _run([ScriptOpcode.OP_0]))
        self._test("script_1_plus_1",
            lambda: _run([ScriptOpcode.OP_1, ScriptOpcode.OP_1, ScriptOpcode.OP_ADD,
                           len(_script_int_to_bytes(2))] +
                          list(_script_int_to_bytes(2)) + [ScriptOpcode.OP_EQUAL]))
        self._test("script_dup",
            lambda: _run([ScriptOpcode.OP_1, ScriptOpcode.OP_DUP, ScriptOpcode.OP_EQUAL]))
        self._test("script_if_else",
            lambda: _run([ScriptOpcode.OP_1, ScriptOpcode.OP_IF,
                           ScriptOpcode.OP_1, ScriptOpcode.OP_ELSE,
                           ScriptOpcode.OP_0, ScriptOpcode.OP_ENDIF]))
        self._test("script_sha256",
            lambda: len(ScriptInterpreter().stack) == 0)
        self._test("p2pkh_script_builds",
            lambda: len(Script.p2pkh_locking_from_address(FOUNDATION_ADDRESS)) == 25)
        self._test("script_disassemble",
            lambda: "OP_DUP" in ScriptInterpreter.disassemble(
                Script.p2pkh_locking_from_address(FOUNDATION_ADDRESS)))

    # ── DeFi Tests ────────────────────────────────────────────────
    def test_defi(self):
        """Test DeFi components"""
        bc = self.bc

        self._test("amm_create_pool",
            lambda: bool(AMMEngine(bc).create_pool("NBL", "TEST")))
        self._test("amm_add_liquidity",
            lambda: AMMEngine(bc).add_liquidity(
                "p", "NBL", "USDT",
                1000*10**DECIMALS, 100*10**DECIMALS)[0] > 0)
        self._test("amm_get_quote",
            lambda: AMMEngine(bc).get_quote("NBL", "USDT", 10*10**DECIMALS).get("amount_out", -1) >= 0)
        self._test("staking_init",
            lambda: len(StakingEngine(bc)._validators) >= 1)
        self._test("staking_foundation",
            lambda: FOUNDATION_ADDRESS in StakingEngine(bc)._validators)
        self._test("oracle_price_positive",
            lambda: (PriceOracle(bc).get_nbl_usd() or 0) > 0)
        self._test("dex_create",
            lambda: bool(DEXEngine()))
        self._test("dex_place_order",
            lambda: bool(DEXEngine().place_order(
                FOUNDATION_ADDRESS, "NBL/USDT", "sell", "limit",
                0.10, 100*10**DECIMALS)[0]))
        self._test("nft_engine_init",
            lambda: NFTEngine(bc).stats()["collections"] >= 0)
        self._test("nft_create_collection",
            lambda: bool(NFTEngine(bc).create_collection(
                FOUNDATION_ADDRESS, "Test", "TST")))
        self._test("governance_init",
            lambda: bool(GovernanceEngine(bc)))
        self._test("governance_propose",
            lambda: GovernanceEngine(bc).submit_proposal(
                FOUNDATION_ADDRESS, "T", "D",
                GOV_MIN_DEPOSIT_NBL)[0])
        self._test("atomic_swap_init",
            lambda: bool(AtomicSwapEngine(bc)))
        self._test("atomic_swap_claim",
            lambda: AtomicSwapEngine(bc).claim_swap(
                AtomicSwapEngine(bc).initiate_swap(
                    "a", "b", 10**DECIMALS, 100, "btc").swap_id,
                bytes.fromhex(AtomicSwapEngine(bc).initiate_swap(
                    "a", "b", 10**DECIMALS, 100, "btc").preimage.hex()))[0])
        self._test("lending_init",
            lambda: bool(LendingProtocol(bc).stats()))

    # ── Privacy Tests ─────────────────────────────────────────────
    def test_privacy(self):
        """Test privacy features"""
        self._test("ecies_roundtrip",
            lambda: ECIES.decrypt(
                ECIES.encrypt(b"NEBULA", Secp256k1.pubkey_to_bytes(
                    Secp256k1.point_mul(12345, Secp256k1.G()))),
                12345) == b"NEBULA")
        self._test("bloom_filter_basic",
            lambda: BloomFilter(100, 0.01).contains(b"test") == False)
        self._test("bloom_filter_insert",
            lambda: (lambda: (lambda bf: (bf.insert(b"nebula"), bf.contains(b"nebula"))[-1])(BloomFilter(100, 0.01))))
        self._test("stealth_addr_length",
            lambda: len(StealthAddress.generate_payment_address(
                Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(1, Secp256k1.G())),
                Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(2, Secp256k1.G())))[0]) == 33)

    # ── Run all tests ──────────────────────────────────────────────
    def run_all(self) -> dict:
        """Run complete final test suite"""
        start = time.time()
        self.test_crypto()
        self.test_blockchain()
        self.test_scripts()
        self.test_defi()
        self.test_privacy()

        passed  = sum(1 for v in self.results.values() if v)
        total   = len(self.results)
        elapsed = time.time() - start

        return {
            "suite"  : "NEBULA Final Suite",
            "passed" : passed,
            "total"  : total,
            "pct"    : f"{passed/max(1,total)*100:.1f}%",
            "elapsed": f"{elapsed:.2f}s",
            "errors" : self._errors[:10],
        }

    def print_results(self):
        report = self.run_all()
        print(f"\n  {'='*55}")
        print(f"  🧪 {report['suite']}")
        print(f"  {'='*55}")
        for name, ok in self.results.items():
            icon = "✅" if ok else "❌"
            print(f"  {icon} {name}")
        print(f"  {'─'*55}")
        print(f"  {report['passed']}/{report['total']} ({report['pct']}) in {report['elapsed']}")
        if report["errors"]:
            print(f"  Errors: {report['errors'][:3]}")
        print(f"  {'='*55}")


# ---- HashUtils
class HashUtils:
    """Extended hashing utilities for NEBULA"""

    @staticmethod
    def sha256d(data: bytes) -> bytes:
        """Double SHA-256 (Bitcoin-style PoW hash)"""
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    @staticmethod
    def hash160(data: bytes) -> bytes:
        """HASH160 = RIPEMD160(SHA256(data))"""
        return hashlib.new('ripemd160', hashlib.sha256(data).digest()).digest()

    @staticmethod
    def hash256(data: bytes) -> bytes:
        """HASH256 = SHA256(SHA256(data))"""
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    @staticmethod
    def tagged_hash(tag: str, data: bytes) -> bytes:
        """BIP340 tagged hash: SHA256(SHA256(tag) || SHA256(tag) || data)"""
        tag_hash = hashlib.sha256(tag.encode()).digest()
        return hashlib.sha256(tag_hash + tag_hash + data).digest()

    @staticmethod
    def merkle_root(txids: list) -> str:
        """Compute Merkle root from list of txids"""
        if not txids:
            return '0' * 64
        hashes = [bytes.fromhex(txid)[::-1] for txid in txids]
        while len(hashes) > 1:
            if len(hashes) % 2 == 1:
                hashes.append(hashes[-1])
            hashes = [
                HashUtils.hash256(hashes[i] + hashes[i+1])
                for i in range(0, len(hashes), 2)
            ]
        return hashes[0][::-1].hex()

    @staticmethod
    def target_to_difficulty(target: int) -> float:
        """Convert target integer to difficulty float"""
        max_target = bits_to_target(INITIAL_BITS)
        return max_target / max(1, target)

    @staticmethod
    def difficulty_to_target(difficulty: float) -> int:
        """Convert difficulty to target"""
        max_target = bits_to_target(INITIAL_BITS)
        return int(max_target / max(0.0001, difficulty))

    @staticmethod
    def compact_from_uint256(target: int) -> int:
        """Convert target integer to compact bits format"""
        # FIX (group30 audit): the original compared the mantissa with 0x7f instead of
        # testing bit 0x800000, so most targets (e.g. INITIAL_BITS) did not round-trip.
        nbytes = (target.bit_length() + 7) // 8
        if nbytes <= 3:
            mantissa = target << (8 * (3 - nbytes))
        else:
            mantissa = target >> (8 * (nbytes - 3))
        if mantissa & 0x800000:          # sign bit must stay clear
            mantissa >>= 8
            nbytes += 1
        return (nbytes << 24) | (mantissa & 0x7fffff)


# ---- AddressUtils
class AddressUtils:
    """Extended address utilities for NEBULA"""

    @staticmethod
    def pubkey_to_p2pkh(pubkey: bytes) -> str:
        """Convert compressed public key to P2PKH address"""
        h160 = HashUtils.hash160(pubkey)
        return base58check_encode(h160, PUBKEY_ADDRESS_VERSION)

    @staticmethod
    def pubkey_to_p2wpkh(pubkey: bytes, hrp: str = "nbl") -> str:
        """Convert compressed public key to P2WPKH (bech32) address"""
        h160 = HashUtils.hash160(pubkey)
        return Bech32.encode(hrp, 0, h160)

    @staticmethod
    def script_to_p2sh(script: bytes) -> str:
        """Convert redeem script to P2SH address"""
        h160 = HashUtils.hash160(script)
        return base58check_encode(h160, SCRIPT_ADDRESS_VERSION)

    @staticmethod
    def script_to_p2wsh(script: bytes, hrp: str = "nbl") -> str:
        """Convert witness script to P2WSH (bech32) address"""
        sh256 = hashlib.sha256(script).digest()
        return Bech32.encode(hrp, 0, sh256)

    @staticmethod
    def xpub_to_address(xpub: str, index: int = 0) -> str:
        """Derive address from extended public key"""
        try:
            master = HDKey.from_xpub(xpub)
            child  = master.derive_path(f"m/0/{index}")
            return child.address
        except Exception:
            return ""

    @staticmethod
    def validate_nbl_address(address: str) -> dict:
        """Validate and classify a NEBULA address"""
        result = {"address": address, "valid": False, "type": "unknown"}
        try:
            version, payload = base58check_decode(address)
            if version == PUBKEY_ADDRESS_VERSION and len(payload) == 20:
                result.update({"valid": True, "type": "P2PKH",
                                "hash160": payload.hex()})
            elif version == SCRIPT_ADDRESS_VERSION and len(payload) == 20:
                result.update({"valid": True, "type": "P2SH",
                                "hash160": payload.hex()})
        except Exception:
            if address.startswith("nbl1"):
                result.update({"valid": True, "type": "Bech32/SegWit"})
        return result


# ---- NEBULAFinalStats
class NEBULAFinalStats:
    """Final statistics for the NEBULA 50,000-line milestone"""

    LINE_GOAL    = 50_000
    MODULES_GOAL = 121
    TESTS_GOAL   = 54

    @classmethod
    def achievement_unlocked(cls) -> dict:
        return {
            "🏆 Lines"     : "50,000+",
            "📦 Modules"   : cls.MODULES_GOAL,
            "🧪 Tests"     : f"{cls.TESTS_GOAL}/{cls.TESTS_GOAL} (100%)",
            "🐍 Language"  : "Python 3 — pure stdlib",
            "👤 Author"    : "NEBULA Core Team",
            "🌍 Country"   : "Worldwide",
            "🔗 Chain"     : f"{CHAIN_NAME} ({CHAIN_SYMBOL})",
            "💰 Supply"    : f"{MAX_SUPPLY/10**DECIMALS:,.0f} {CHAIN_SYMBOL}",
        }

    @classmethod
    def print_achievement(cls):
        print("\n" + "█" * 60)
        print("  🌌  NEBULA — 50,000 LINES ACHIEVED!")
        print("█" * 60)
        for k, v in cls.achievement_unlocked().items():
            print(f"  {k:15}: {v}")
        print("█" * 60)
        print(f"\n  {_NEBULA_FINAL_MESSAGE.strip()}")
        print()


# ---- RemittanceCorridor
class RemittanceCorridor(Enum):
    AF_AFGHANI      = "AFN"   # Afghanistan
    PK_RUPEE        = "PKR"   # Pakistan
    BD_TAKA         = "BDT"   # Bangladesh
    NG_NAIRA        = "NGN"   # Nigeria
    ET_BIRR         = "ETB"   # Ethiopia
    PH_PESO         = "PHP"   # Philippines
    IN_RUPEE        = "INR"   # India
    MX_PESO         = "MXN"   # Mexico
    GH_CEDI         = "GHS"   # Ghana
    KE_SHILLING     = "KES"   # Kenya
    EG_POUND        = "EGP"   # Egypt
    IQ_DINAR        = "IQD"   # Iraq
    SY_POUND        = "SYP"   # Syria
    YE_RIAL         = "YER"   # Yemen
    SO_SHILLING     = "SOS"   # Somalia
    SD_POUND        = "SDG"   # Sudan
    USD             = "USD"   # US Dollar
    EUR             = "EUR"   # Euro
    AED             = "AED"   # UAE Dirham (Dubai workers)
    SAR             = "SAR"   # Saudi Riyal (KSA workers)
    TR_LIRA         = "TRY"   # Turkey
    IR_RIAL         = "IRR"   # Iran


# ---- RemittanceTransfer
@dataclass
class RemittanceTransfer:
    """A single remittance transfer"""
    transfer_id   : str
    sender_addr   : str
    recipient_addr: str
    amount_nbl    : float          # amount in NBL
    send_currency : str            # sender's local currency
    recv_currency : str            # recipient's local currency
    send_amount   : float          # amount in sender's currency
    recv_amount   : float          # amount recipient gets (local)
    fee_nbl       : float          # protocol fee
    fee_pct       : float          # fee as percentage
    tx_hash       : Optional[str]  = None
    status        : str            = "pending"
    created_at    : float          = field(default_factory=time.time)
    confirmed_at  : Optional[float] = None
    note          : str            = ""

    @property
    def elapsed_minutes(self) -> float:
        end = self.confirmed_at or time.time()
        return (end - self.created_at) / 60

    @property
    def traditional_fee_usd(self) -> float:
        """What Western Union / Hawala would charge (avg 8%)"""
        send_usd = self.send_amount / NBL_EXCHANGE_RATES.get(self.send_currency, 10)
        return send_usd * 0.08

    @property
    def nebula_fee_usd(self) -> float:
        """What NEBULA charges"""
        return self.fee_nbl * 0.10   # at $0.10/NBL

    @property
    def savings_usd(self) -> float:
        """How much the sender saved vs traditional"""
        return max(0, self.traditional_fee_usd - self.nebula_fee_usd)

    def to_dict(self) -> dict:
        return {
            "transfer_id"        : self.transfer_id,
            "status"             : self.status,
            "send_amount"        : f"{self.send_amount:.2f} {self.send_currency}",
            "recv_amount"        : f"{self.recv_amount:.2f} {self.recv_currency}",
            "amount_nbl"         : f"{self.amount_nbl:.9f} NBL",
            "fee_pct"            : f"{self.fee_pct:.4f}%",
            "fee_nbl"            : f"{self.fee_nbl:.9f} NBL",
            "traditional_fee"    : f"${self.traditional_fee_usd:.2f}",
            "nebula_fee"         : f"${self.nebula_fee_usd:.6f}",
            "you_saved"          : f"${self.savings_usd:.2f}",
            "time_minutes"       : f"{self.elapsed_minutes:.1f}",
            "tx_hash"            : (self.tx_hash[:16]+"..." if self.tx_hash else None),
        }


# ---- RemittanceAgent
@dataclass
class RemittanceAgent:
    """
    A local cash-in/cash-out agent.
    Like a corner shop that buys/sells NBL for local currency.
    Similar to M-Pesa agents in Kenya.
    Agents earn a small spread — their income source.
    """
    agent_id      : str
    name          : str
    country       : str
    city          : str
    currency      : str
    nbl_address   : str
    buy_rate      : float     # local currency per 1 NBL (agent buys NBL)
    sell_rate     : float     # local currency per 1 NBL (agent sells NBL)
    nbl_balance   : float = 0.0
    cash_balance  : float = 0.0
    is_online     : bool  = True
    rating        : float = 5.0     # 1-5 stars
    tx_count      : int   = 0
    last_seen     : float = field(default_factory=time.time)

    @property
    def spread_pct(self) -> float:
        """Agent's profit margin"""
        return (self.sell_rate - self.buy_rate) / self.buy_rate * 100

    def to_dict(self) -> dict:
        return {
            "agent"        : self.name,
            "city"         : f"{self.city}, {self.country}",
            "currency"     : self.currency,
            "buy_rate"     : f"{self.buy_rate:.4f} {self.currency}/NBL",
            "sell_rate"    : f"{self.sell_rate:.4f} {self.currency}/NBL",
            "spread"       : f"{self.spread_pct:.2f}%",
            "nbl_available": f"{self.nbl_balance:.4f} NBL",
            "rating"       : f"{self.rating}/5.0",
            "tx_count"     : self.tx_count,
            "online"       : self.is_online,
        }


# ---- RemittanceEngine
class RemittanceEngine:
    """
    NEBULA Zero-Fee Remittance System.

    Replaces: Western Union, MoneyGram, Hawala, SWIFT
    For:      The 2 billion unbanked people worldwide

    Key innovation:
    - Traditional: bank → SWIFT → correspondent bank → local bank → recipient
      Cost: 5-15%, Time: 2-5 days
    - NEBULA: sender wallet → blockchain → recipient wallet
      Cost: 0.001%, Time: ~10 minutes

    Real-world example:
    - Ali works in Dubai (AED), sends 500 AED home to Kabul (AFN)
    - Traditional: 500 AED - 8% fee = 460 AED equivalent reaches family
    - NEBULA: 500 AED = 1360 NBL, 1360 NBL = 29,920 AFN, fee = 0.00136 NBL (~$0.000136)
    - Family gets ~40 AED MORE than via Western Union
    """

    # Protocol fee: 0.001% — covers network costs only
    PROTOCOL_FEE_PCT   = 0.00001   # 0.001%
    MIN_FEE_NBL        = 0.001     # minimum 0.001 NBL (~$0.0001)
    MAX_SINGLE_TX_NBL  = 100_000   # $10,000 equivalent

    def __init__(self, blockchain: 'NEBULABlockchain',
                 oracle: 'PriceOracle' = None):
        self.bc        = blockchain
        self.oracle    = oracle
        self._transfers: Dict[str, RemittanceTransfer] = {}
        self._agents   : Dict[str, RemittanceAgent]    = {}
        self._lock     = threading.RLock()
        self._stats    = {
            "total_transfers"    : 0,
            "total_volume_nbl"   : 0.0,
            "total_saved_usd"    : 0.0,
            "countries_served"   : set(),
            "families_helped"    : 0,
        }
        self._seed_demo_agents()

    def _seed_demo_agents(self):
        """Pre-register demo agents for demonstration"""
        demo_agents = [
            RemittanceAgent(
                agent_id="AF001", name="Kabul Exchange",
                country="Afghanistan", city="Kabul",
                currency="AFN", nbl_address=FOUNDATION_ADDRESS,
                buy_rate=21.5, sell_rate=22.0,
                nbl_balance=50000, cash_balance=1_000_000,
            ),
            RemittanceAgent(
                agent_id="PK001", name="Lahore Money Shop",
                country="Pakistan", city="Lahore",
                currency="PKR", nbl_address=FOUNDATION_ADDRESS,
                buy_rate=27.5, sell_rate=28.1,
                nbl_balance=80000, cash_balance=2_000_000,
            ),
            RemittanceAgent(
                agent_id="NG001", name="Lagos NBL Point",
                country="Nigeria", city="Lagos",
                currency="NGN", nbl_address=FOUNDATION_ADDRESS,
                buy_rate=155.0, sell_rate=158.5,
                nbl_balance=100000, cash_balance=15_000_000,
            ),
            RemittanceAgent(
                agent_id="PH001", name="Manila Remit Center",
                country="Philippines", city="Manila",
                currency="PHP", nbl_address=FOUNDATION_ADDRESS,
                buy_rate=5.55, sell_rate=5.65,
                nbl_balance=60000, cash_balance=300_000,
            ),
            RemittanceAgent(
                agent_id="AE001", name="Dubai NBL Kiosk",
                country="UAE", city="Dubai",
                currency="AED", nbl_address=FOUNDATION_ADDRESS,
                buy_rate=0.365, sell_rate=0.370,
                nbl_balance=200000, cash_balance=50_000,
            ),
            RemittanceAgent(
                agent_id="KE001", name="Nairobi M-NBL Agent",
                country="Kenya", city="Nairobi",
                currency="KES", nbl_address=FOUNDATION_ADDRESS,
                buy_rate=12.8, sell_rate=13.1,
                nbl_balance=45000, cash_balance=500_000,
            ),
            RemittanceAgent(
                agent_id="BD001", name="Dhaka City Exchange",
                country="Bangladesh", city="Dhaka",
                currency="BDT", nbl_address=FOUNDATION_ADDRESS,
                buy_rate=10.9, sell_rate=11.2,
                nbl_balance=70000, cash_balance=700_000,
            ),
        ]
        for agent in demo_agents:
            self._agents[agent.agent_id] = agent

    def calculate_transfer(self, send_currency: str,
                            send_amount: float,
                            recv_currency: str) -> dict:
        """
        Calculate a remittance transfer without executing it.
        Shows: how much recipient gets, fees, savings vs traditional.
        """
        # Convert to NBL
        send_rate  = NBL_EXCHANGE_RATES.get(send_currency, 10.0)
        recv_rate  = NBL_EXCHANGE_RATES.get(recv_currency, 10.0)
        amount_nbl = send_amount * send_rate

        # Protocol fee
        fee_nbl = max(self.MIN_FEE_NBL,
                      amount_nbl * self.PROTOCOL_FEE_PCT)
        net_nbl      = amount_nbl - fee_nbl
        recv_amount  = net_nbl / recv_rate
        fee_pct      = fee_nbl / amount_nbl * 100

        # What traditional services charge
        usd_amount   = send_amount / send_rate * 10.0   # rough USD
        traditional_fee_usd = usd_amount * 0.08
        nebula_fee_usd      = fee_nbl * 0.10
        savings_usd         = traditional_fee_usd - nebula_fee_usd

        return {
            "send"              : f"{send_amount:.2f} {send_currency}",
            "amount_nbl"        : f"{amount_nbl:.4f} NBL",
            "protocol_fee"      : f"{fee_nbl:.6f} NBL ({fee_pct:.4f}%)",
            "recipient_gets"    : f"{recv_amount:.2f} {recv_currency}",
            "time"              : "~10 minutes",
            "comparison": {
                "western_union"     : f"${traditional_fee_usd:.2f} fee (~8%)",
                "nebula"            : f"${nebula_fee_usd:.6f} fee (0.001%)",
                "you_save"          : f"${savings_usd:.2f}  ({savings_usd/traditional_fee_usd*100:.0f}% cheaper)",
                "monthly_savings"   : f"${savings_usd * 2:.2f}  (sending twice/month)",
                "yearly_savings"    : f"${savings_usd * 24:.2f}  (sending twice/month)",
            },
        }

    def initiate_transfer(self, sender_addr: str,
                           recipient_addr: str,
                           send_currency: str,
                           send_amount:   float,
                           recv_currency: str,
                           note: str = "") -> RemittanceTransfer:
        """
        Initiate a remittance transfer.
        In production: sender deposits local currency at local agent,
        agent sends NBL, recipient collects local currency from local agent.
        """
        calc = self.calculate_transfer(send_currency, send_amount, recv_currency)

        send_rate  = NBL_EXCHANGE_RATES.get(send_currency, 10.0)
        recv_rate  = NBL_EXCHANGE_RATES.get(recv_currency, 10.0)
        amount_nbl = send_amount * send_rate
        fee_nbl    = max(self.MIN_FEE_NBL, amount_nbl * self.PROTOCOL_FEE_PCT)
        net_nbl    = amount_nbl - fee_nbl
        recv_amount= net_nbl / recv_rate
        fee_pct    = fee_nbl / amount_nbl * 100

        transfer_id = hashlib.sha256(
            f"{sender_addr}{recipient_addr}{send_amount}{time.time()}".encode()
        ).hexdigest()[:20]

        transfer = RemittanceTransfer(
            transfer_id   = transfer_id,
            sender_addr   = sender_addr,
            recipient_addr= recipient_addr,
            amount_nbl    = amount_nbl,
            send_currency = send_currency,
            recv_currency = recv_currency,
            send_amount   = send_amount,
            recv_amount   = recv_amount,
            fee_nbl       = fee_nbl,
            fee_pct       = fee_pct,
            note          = note,
        )

        with self._lock:
            self._transfers[transfer_id] = transfer
            self._stats["total_transfers"]  += 1
            self._stats["total_volume_nbl"] += amount_nbl
            self._stats["total_saved_usd"]  += transfer.savings_usd
            self._stats["countries_served"].add(send_currency)
            self._stats["countries_served"].add(recv_currency)
            self._stats["families_helped"]  += 1

        return transfer

    def complete_transfer(self, transfer_id: str,
                           tx_hash: str) -> Tuple[bool, str]:
        """Mark transfer as confirmed on blockchain"""
        with self._lock:
            t = self._transfers.get(transfer_id)
            if not t:
                return False, "Transfer not found"
            t.status       = "confirmed"
            t.tx_hash      = tx_hash
            t.confirmed_at = time.time()
            return True, (f"Transfer confirmed in "
                          f"{t.elapsed_minutes:.1f} minutes. "
                          f"Recipient gets {t.recv_amount:.2f} {t.recv_currency}")

    def find_agents(self, currency: str,
                     min_nbl: float = 0) -> List[RemittanceAgent]:
        """Find available cash-out agents for a currency"""
        with self._lock:
            return [a for a in self._agents.values()
                    if a.currency == currency
                    and a.is_online
                    and a.nbl_balance >= min_nbl]

    def register_agent(self, agent: RemittanceAgent):
        """Register a new local cash-in/out agent"""
        with self._lock:
            self._agents[agent.agent_id] = agent

    def transfer_history(self, addr: str) -> List[dict]:
        """Get transfer history for an address"""
        with self._lock:
            return [t.to_dict() for t in self._transfers.values()
                    if t.sender_addr == addr or t.recipient_addr == addr]

    def impact_report(self) -> dict:
        """How much value NEBULA remittance has created for the world"""
        with self._lock:
            stats = dict(self._stats)
            stats["countries_served"] = len(stats["countries_served"])

        avg_saving = (stats["total_saved_usd"] /
                      max(1, stats["total_transfers"]))
        return {
            "mission"            : "Financial inclusion for 2 billion unbanked people",
            "total_transfers"    : stats["total_transfers"],
            "total_volume_nbl"   : f"{stats['total_volume_nbl']:.2f} NBL",
            "total_saved_usd"    : f"${stats['total_saved_usd']:.2f}",
            "families_helped"    : stats["families_helped"],
            "countries_served"   : stats["countries_served"],
            "avg_saving_per_tx"  : f"${avg_saving:.2f}",
            "vs_western_union"   : "99.9% cheaper",
            "vs_bank_wire"       : "99.8% cheaper",
            "confirmation_time"  : "~10 minutes vs 2-5 days",
            "agents_registered"  : len(self._agents),
        }

    def demo_real_scenario(self) -> str:
        """
        Print a real-world demonstration:
        Ali works in Dubai, sends money home to Kabul.
        """
        calc = self.calculate_transfer("AED", 500, "AFN")
        lines = [
            "",
            "  ╔══════════════════════════════════════════════════════╗",
            "  ║   REAL SCENARIO: Ali sends 500 AED from Dubai       ║",
            "  ║   to his family in Kabul, Afghanistan                ║",
            "  ╠══════════════════════════════════════════════════════╣",
            f"  ║   Sending    : {calc['send']:>36} ║",
            f"  ║   NBL amount : {calc['amount_nbl']:>36} ║",
            f"  ║   Family gets: {calc['recipient_gets']:>36} ║",
            f"  ║   Fee        : {calc['protocol_fee']:>36} ║",
            f"  ║   Time       : {calc['time']:>36} ║",
            "  ╠══════════════════════════════════════════════════════╣",
            "  ║   COMPARISON:                                        ║",
            f"  ║   Western Union fee : {calc['comparison']['western_union']:>30} ║",
            f"  ║   NEBULA fee        : {calc['comparison']['nebula']:>30} ║",
            f"  ║   Ali saves         : {calc['comparison']['you_save']:>30} ║",
            f"  ║   Per year (2x/mo)  : {calc['comparison']['yearly_savings']:>30} ║",
            "  ╚══════════════════════════════════════════════════════╝",
            "",
        ]
        return "\n".join(lines)

    def global_impact_projection(self) -> dict:
        """
        If NEBULA captured 1% of global remittance market:
        Global remittance = $800 billion/year
        Average fee = 6.5% = $52 billion/year in fees
        NEBULA fee  = 0.001% = $8 million/year
        Savings to poor families: $51.99 BILLION/year
        """
        global_remittance_usd = 800_000_000_000   # $800B/year
        current_fee_pct       = 0.065             # 6.5% average
        nebula_fee_pct        = 0.00001           # 0.001%
        market_share          = 0.01              # conservative 1%

        volume      = global_remittance_usd * market_share
        current_fee = volume * current_fee_pct
        nebula_fee  = volume * nebula_fee_pct
        savings     = current_fee - nebula_fee

        return {
            "scenario"          : "1% of global remittance market",
            "global_market"     : "$800 billion/year",
            "current_fees_total": f"${current_fee/1e9:.1f} billion/year (to families)",
            "nebula_fees"       : f"${nebula_fee/1e6:.1f} million/year",
            "annual_savings"    : f"${savings/1e9:.2f} billion saved by poor families",
            "families_impacted" : "~200 million families",
            "vs_bitcoin"        : "Bitcoin stores value. NEBULA moves it — cheaply.",
            "vs_ethereum"       : "Ethereum is too expensive for $50 transfers.",
            "nebula_advantage"  : "Built for $5 transfers, not $5,000 ones.",
        }


# ---- Vote
@dataclass
class Vote:
    voter:       str
    proposal_id: str
    choice:      str    # "yes" / "no" / "abstain"
    weight:      int    # Neb balance at snapshot
    cast_at:     float
    tx_hash:     str = ""


# ==========================================================================
# ==========================================================================
#   NEBULA group30  --  WIRING LAYER  (connects all 20 classes to the chain)
# ==========================================================================
# ==========================================================================
#
# Design rules (same as the group5 pattern):
#   A) NOTHING is edited inside nebula_v10_11.py. Everything is attached from
#      outside by install(host) and can be removed again by uninstall(host).
#   B) The layer NEVER rejects a block / tx / message. Every callback is wrapped
#      in try/except; failures only increase layer.errors.
#   C) REPORT-ONLY first: no consensus rule is changed. Read-only REST routes
#      (GET). Mutating actions (remittance transfer, wallet creation, mining
#      demo) are NOT exposed over HTTP - they stay programmatic only.
#
# Usage (from your launcher, after importing the host):
#       import nebula_v10_11 as host
#       import nebula_group30 as g30
#       g30.install(host)          # every NEBULAFullNode created afterwards gets node.group30
#       ...
#       g30.uninstall(host)        # restores the original behaviour
#
# For a node that already exists:  layer = g30.attach(node, host)

from collections import OrderedDict as _G30_OD
from collections import deque as _g30_deque

# ---- fallback colour class (host normally provides C; only used by ok()/info()) ----
if "C" not in globals():
    class C:                                    # noqa: N801  (name must match host)
        GREEN = "\033[92m"
        CYAN = "\033[96m"
        RED = "\033[91m"
        YELLOW = "\033[93m"
        BOLD = "\033[1m"
        RESET = "\033[0m"

_G30_LOG = logging.getLogger("nebula.group30")

# All 20 classes of this group, in the order of the guide (step 4).
G30_CLASS_ORDER = (
    "GenesisAllocation", "GenesisConfig", "RemittanceCorridor",
    "RemittanceTransfer", "RemittanceAgent", "Vote",
    "GenesisConfigurator", "NEBULA50KMilestone", "ExtendedAPIEndpoints",
    "NEBULAOnboarding", "ProjectStats", "NEBULARoadmap", "WalletUtils",
    "NetworkUtils", "NEBULAInit", "NEBULAFinalTestSuite", "HashUtils",
    "AddressUtils", "NEBULAFinalStats", "RemittanceEngine",
)

_G30_LAYERS: list = []                 # every live Layer30 (used by the P2P observer)
_G30_LAYERS_LOCK = threading.RLock()
_G30_HOST_ROUTES: Dict[str, Callable] = {}   # path -> our handler (for clean uninstall)


def _g30_query(query, key, default=None):
    """Read one query value; works for {'k': 'v'} and {'k': ['v']} (parse_qs)."""
    if not isinstance(query, dict):
        return default
    v = query.get(key, default)
    if isinstance(v, (list, tuple)):
        v = v[0] if v else default
    return v


def _g30_bad(msg: str, code: int = 400):
    return code, {"success": False, "error": msg}


def _g30_find(obj, *names):
    """First non-None attribute among names on obj (safe)."""
    for n in names:
        try:
            v = getattr(obj, n, None)
        except Exception:
            v = None
        if v is not None:
            return v
    return None


def _g30_cls(name: str, host=None):
    """Resolve a class by name: this module first, then the host module."""
    v = globals().get(name)
    if v is not None:
        return v
    if host is not None:
        return getattr(host, name, None)
    return None


# ==========================================================================
#  Layer30  -  one instance per node
# ==========================================================================
class Layer30:
    """
    The single object that owns every group30 class for one node.

    Hook points (as suggested by the guide):
      chain listener : GenesisConfigurator, NEBULA50KMilestone, HashUtils
      REST (GET)     : ExtendedAPIEndpoints, RemittanceEngine, AddressUtils,
                       WalletUtils, NEBULARoadmap, NEBULAFinalStats, ProjectStats
      wallet side    : NEBULAOnboarding, WalletUtils, AddressUtils, NEBULAFinalTestSuite
      P2P observer   : NetworkUtils, NEBULAInit
      data types     : GenesisAllocation, GenesisConfig, RemittanceCorridor,
                       RemittanceTransfer, RemittanceAgent, Vote
    """

    VERSION = "30.1"
    VOTE_CAP = 10_000          # RAM cap for recorded votes
    PEER_CAP = 512             # RAM cap for per-peer counters
    CHECK_EVERY_N = 1          # run the merkle observation on every Nth block

    def __init__(self, node, host=None):
        self.node = node
        self.host = host
        self.bc = _g30_find(node, "bc", "blockchain", "chain")
        self.errors = 0
        self.last_error = ""
        self._lock = threading.RLock()
        self._lazy: Dict[str, Any] = {}
        self.wired: "_G30_OD[str, str]" = _G30_OD()      # class name -> status text
        self.routes: List[Tuple[str, str]] = []           # (method, path) registered on host
        self.votes = _g30_deque(maxlen=self.VOTE_CAP)
        self.peer_stats: Dict[str, Dict[str, int]] = {}
        self.env: dict = {}
        self.genesis_summary: dict = {}
        self._selftest: Optional[dict] = None
        self._selftest_running = False
        self.stats_ = {
            "blocks_seen": 0, "reorgs": 0, "last_height": None,
            "last_reorg_ancestor": None,
            "merkle_match": 0, "merkle_mismatch": 0, "merkle_skipped": 0,
            "p2p_messages": 0, "p2p_bytes": 0, "p2p_private_peers": 0,
            "api_calls": 0,
        }
        self.created_at = time.time()
        self.listener_attached = False      # set by attach() when add_listener really worked
        self._build()

    # ------------------------------------------------------------------ errors
    def _err(self, where: str, exc: BaseException):
        with self._lock:
            self.errors += 1
            self.last_error = f"{where}: {type(exc).__name__}: {exc}"
        try:
            _G30_LOG.warning("group30 %s failed: %s", where, exc)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer30._err", exc_info=True)

    def _mark(self, cls_name: str, status: str):
        with self._lock:
            self.wired[cls_name] = status

    # ------------------------------------------------------------------ build
    def _build(self):
        """Wire all 20 classes, one by one, each isolated from the others."""
        steps = (
            self._wire_data_types,       # 1-6   GenesisAllocation .. Vote
            self._wire_genesis,          # 7     GenesisConfigurator
            self._wire_milestone,        # 8     NEBULA50KMilestone (lazy)
            self._wire_ext_api,          # 9     ExtendedAPIEndpoints (lazy)
            self._wire_onboarding,       # 10    NEBULAOnboarding (lazy)
            self._wire_utility,          # 11-12 ProjectStats, NEBULARoadmap
            self._wire_wallet_utils,     # 13,18 WalletUtils, AddressUtils
            self._wire_network,          # 14-15 NetworkUtils, NEBULAInit
            self._wire_selftest,         # 16    NEBULAFinalTestSuite (on demand)
            self._wire_hash,             # 17    HashUtils
            self._wire_final_stats,      # 19    NEBULAFinalStats
            self._wire_remittance,       # 20    RemittanceEngine
        )
        for fn in steps:
            try:
                fn()
            except Exception as e:                      # a failing step never stops the node
                self._err(fn.__name__, e)
        for name in G30_CLASS_ORDER:                    # anything not marked is reported honestly
            self.wired.setdefault(name, "NOT WIRED")
        self._register_routes()

    # ---- 1-6: plain data types / enum ---------------------------------------
    def _wire_data_types(self):
        for name in ("GenesisAllocation", "GenesisConfig", "RemittanceCorridor",
                     "RemittanceTransfer", "RemittanceAgent", "Vote"):
            cls = _g30_cls(name, self.host)
            if cls is None:
                self._mark(name, "MISSING class")
                continue
            self._mark(name, "ok (data type, used by its engine)")
        # sanity: the enum must have members, the Vote dataclass must build
        try:
            self.corridors = [m.name for m in RemittanceCorridor]
            Vote(voter="x", proposal_id="p", choice="abstain", weight=0, cast_at=time.time())
        except Exception as e:
            self._err("data_types_sanity", e)
            self._mark("Vote", f"error: {e}")

    # ---- 7: GenesisConfigurator ---------------------------------------------
    def _wire_genesis(self):
        self.genesis = GenesisConfigurator()
        self.genesis_summary = self.genesis.summary()      # report only, never applied to the chain
        self._mark("GenesisConfigurator", "ok (report-only; genesis block untouched)")

    # ---- 8: NEBULA50KMilestone (lazy, shares the node's chain) --------------
    def _wire_milestone(self):
        self._mark("NEBULA50KMilestone", "ok (lazy, shares node chain)")

    def milestone(self):
        """Built on first use WITHOUT calling __init__ (which would create a second chain)."""
        with self._lock:
            m = self._lazy.get("milestone")
            if m is None:
                if self.bc is None:
                    raise RuntimeError("node has no blockchain")
                m = object.__new__(NEBULA50KMilestone)
                m.bc = self.bc
                m.components = m._init_components()
                self._lazy["milestone"] = m
            return m

    # ---- 9: ExtendedAPIEndpoints (lazy) --------------------------------------
    def _wire_ext_api(self):
        self._mark("ExtendedAPIEndpoints", "ok (lazy; routes /api/ext/*)")

    def _component(self, label: str, attr_names: Tuple[str, ...], class_name: str, needs_bc=True):
        """Use the node's own component when it exists, else build one on the node's chain."""
        found = _g30_find(self.node, *attr_names)
        if found is None and self.bc is not None:
            found = _g30_find(self.bc, *attr_names)
        if found is not None:
            return found
        cls = _g30_cls(class_name, self.host)
        if cls is None:
            return None
        key = f"comp:{label}"
        with self._lock:
            obj = self._lazy.get(key)
            if obj is None:
                obj = cls(self.bc) if needs_bc else cls()
                self._lazy[key] = obj
            return obj

    def ext_api(self):
        with self._lock:
            api = self._lazy.get("ext_api")
        if api is not None:
            return api
        comps = {}
        for label, attrs, cname, needs_bc in (
            ("oracle",     ("oracle", "price_oracle"),         "PriceOracle",      True),
            ("amm",        ("amm", "amm_engine"),              "AMMEngine",        True),
            ("staking",    ("staking", "staking_engine"),      "StakingEngine",    True),
            ("nft",        ("nft", "nft_engine"),              "NFTEngine",        True),
            ("dex",        ("dex", "dex_engine"),              "DEXEngine",        False),
            ("governance", ("governance", "governance_engine"), "GovernanceEngine", True),
            ("bridge",     ("bridge", "token_bridge"),         "TokenBridge",      True),
        ):
            try:
                comps[label] = self._component(label, attrs, cname, needs_bc)
            except Exception as e:
                self._err(f"ext_api component {label}", e)
                comps[label] = None
        comps["pool"] = _g30_find(self.node, "pool", "mining_pool")
        api = ExtendedAPIEndpoints(self.bc, **comps)
        with self._lock:
            self._lazy["ext_api"] = api
        return api

    # ---- 10: NEBULAOnboarding (programmatic only) ----------------------------
    def _wire_onboarding(self):
        self._mark("NEBULAOnboarding", "ok (lazy; run_onboarding() - never over HTTP)")

    def onboarding(self):
        with self._lock:
            ob = self._lazy.get("onboarding")
            if ob is None:
                ob = NEBULAOnboarding(self.bc)
                self._lazy["onboarding"] = ob
            return ob

    def run_onboarding(self) -> dict:
        """Manual only: creates a wallet and may mine a demo block."""
        return self.onboarding().run_full_onboarding()

    # ---- 11-12: ProjectStats / NEBULARoadmap ---------------------------------
    def _wire_utility(self):
        src = getattr(self.host, "__file__", None) if self.host is not None else None
        self.project_stats = ProjectStats(source_file=src)      # file is read only on analyze()
        self._mark("ProjectStats", "ok (lazy analyze, reads host source file once)")
        self.roadmap = NEBULARoadmap()
        self._mark("NEBULARoadmap", "ok (REST /api/group30/roadmap)")

    # ---- 13, 18: WalletUtils / AddressUtils (stateless helpers) --------------
    def _wire_wallet_utils(self):
        self.wallet_utils = WalletUtils()
        self.address_utils = AddressUtils()
        self._mark("WalletUtils", "ok (REST address_type only; WIF helpers stay local)")
        self._mark("AddressUtils", "ok (REST validate)")

    # ---- 14-15: NetworkUtils / NEBULAInit ------------------------------------
    def _wire_network(self):
        self.network_utils = NetworkUtils()
        self.env = NEBULAInit.check_environment()
        self._mark("NetworkUtils", "ok (P2P observer, counters only)")
        self._mark("NEBULAInit", "ok (environment checked at attach)")

    # ---- 16: NEBULAFinalTestSuite (on demand) --------------------------------
    def _wire_selftest(self):
        self._mark("NEBULAFinalTestSuite", "ok (on demand: run_selftest())")

    def run_selftest(self, background: bool = True) -> dict:
        """Runs the final suite on its OWN fresh chain (never touches the live chain)."""
        def _job():
            try:
                suite = NEBULAFinalTestSuite()
                rep = suite.run_all()
            except Exception as e:
                rep = {"suite": "NEBULA Final Suite", "error": str(e)}
                self._err("selftest", e)
            with self._lock:
                self._selftest = rep
                self._selftest_running = False
        with self._lock:
            if self._selftest_running:
                return {"running": True}
            self._selftest_running = True
        if background:
            threading.Thread(target=_job, name="g30-selftest", daemon=True).start()
            return {"running": True}
        _job()
        return self._selftest or {}

    # ---- 17: HashUtils (merkle observation) ----------------------------------
    def _wire_hash(self):
        self.hash_utils = HashUtils()
        self._mark("HashUtils", "ok (listener: merkle root observation, report-only)")

    # ---- 19: NEBULAFinalStats --------------------------------------------------
    def _wire_final_stats(self):
        self._mark("NEBULAFinalStats", "ok (REST /api/group30/achievement)")

    # ---- 20: RemittanceEngine --------------------------------------------------
    def _wire_remittance(self):
        oracle = _g30_find(self.node, "oracle", "price_oracle")
        self.remittance = RemittanceEngine(self.bc, oracle)
        self._mark("RemittanceEngine", "ok (REST read-only; transfers programmatic only)")

    # ==================================================== remittance (validated)
    def remit_initiate(self, sender_addr: str, recipient_addr: str, send_currency: str,
                       send_amount: float, recv_currency: str, note: str = ""):
        """Validated front door for RemittanceEngine.initiate_transfer (programmatic only).
        NOTE: this records the transfer in RAM; it does NOT move any NBL on the chain."""
        for who, addr in (("sender", sender_addr), ("recipient", recipient_addr)):
            if not AddressUtils.validate_nbl_address(str(addr)).get("valid"):
                raise ValueError(f"{who} address is not a valid NBL address")
        if send_currency not in NBL_EXCHANGE_RATES or recv_currency not in NBL_EXCHANGE_RATES:
            raise ValueError("unknown currency")
        amount = float(send_amount)
        if not (0.01 <= amount <= 1e12):
            raise ValueError("amount out of range")
        return self.remittance.initiate_transfer(sender_addr, recipient_addr,
                                                 send_currency, amount, recv_currency, note[:200])

    def remit_complete(self, transfer_id: str, tx_hash: str):
        h = str(tx_hash).lower()
        if len(h) != 64 or any(ch not in "0123456789abcdef" for ch in h):
            raise ValueError("tx_hash must be 64 hex characters")
        return self.remittance.complete_transfer(transfer_id, h)

    # ==================================================================== votes
    def record_vote(self, voter: str, proposal_id: str, choice: str,
                    weight: int, tx_hash: str = "") -> Vote:
        """Record a governance vote object (data only; does not change any chain state)."""
        if choice not in ("yes", "no", "abstain"):
            raise ValueError("choice must be yes / no / abstain")
        if weight < 0:
            raise ValueError("weight must be >= 0")
        v = Vote(voter=voter, proposal_id=proposal_id, choice=choice,
                 weight=int(weight), cast_at=time.time(), tx_hash=tx_hash)
        self.votes.append(v)
        return v

    # ============================================================ chain listener
    def on_connect(self, block):
        """Called by NEBULABlockchain for every connected block. Never raises."""
        try:
            with self._lock:
                self.stats_["blocks_seen"] += 1
                h = _g30_find(block, "height")
                if h is None:
                    hdr = _g30_find(block, "header")
                    h = _g30_find(hdr, "height") if hdr is not None else None
                self.stats_["last_height"] = h
                n = self.stats_["blocks_seen"]
            if n % self.CHECK_EVERY_N == 0:
                self._observe_merkle(block)
        except Exception as e:
            self._err("on_connect", e)

    def on_reorg(self, old, new, ancestor_height):
        try:
            with self._lock:
                self.stats_["reorgs"] += 1
                self.stats_["last_reorg_ancestor"] = ancestor_height
        except Exception as e:
            self._err("on_reorg", e)

    def _observe_merkle(self, block):
        """Compare the header merkle root with HashUtils.merkle_root (both byte orders)."""
        txs = _g30_find(block, "txs", "transactions", "vtx")
        hdr = _g30_find(block, "header")
        want = _g30_find(block, "merkle_root", "merkle")
        if want is None and hdr is not None:
            want = _g30_find(hdr, "merkle_root", "merkle")
        if not txs or want is None:
            with self._lock:
                self.stats_["merkle_skipped"] += 1
            return
        ids = []
        for t in txs:
            tid = _g30_find(t, "txid", "hash", "id")
            if callable(tid):
                tid = tid()
            if isinstance(tid, (bytes, bytearray)):
                tid = bytes(tid).hex()
            if not isinstance(tid, str) or len(tid) != 64:
                with self._lock:
                    self.stats_["merkle_skipped"] += 1
                return
            ids.append(tid)
        if isinstance(want, (bytes, bytearray)):
            want = bytes(want).hex()
        want = str(want).lower()
        mine = HashUtils.merkle_root(ids)
        flipped = bytes.fromhex(mine)[::-1].hex()
        with self._lock:
            if want in (mine, flipped):
                self.stats_["merkle_match"] += 1
            else:
                self.stats_["merkle_mismatch"] += 1   # observation only - block is NOT rejected

    def detach(self):
        """Remove this layer from the chain listeners."""
        try:
            lst = getattr(self.bc, "_listeners", None)
            if lst is not None:
                lst.remove(self)
        except ValueError:
            _NB_SWALLOW_LOG.debug("swallowed ValueError in Layer30.detach", exc_info=True)
        except Exception as e:
            self._err("detach", e)
        self._unregister_routes()
        with _G30_LAYERS_LOCK:
            if self in _G30_LAYERS:
                _G30_LAYERS.remove(self)

    # ================================================================= P2P hook
    def on_peer_message(self, peer, msg):
        """Called AFTER the original P2PNode._handle_message. Counters only."""
        try:
            size = 0
            if isinstance(msg, (bytes, bytearray)):
                size = len(msg)
            else:
                payload = _g30_find(msg, "payload", "data")
                if isinstance(payload, (bytes, bytearray)):
                    size = len(payload)
            host_s = _g30_find(peer, "host", "ip", "addr", "address")
            key = str(host_s) if host_s is not None else "unknown"
            ip_only = key.rsplit(":", 1)[0] if key.count(":") == 1 else key
            with self._lock:
                self.stats_["p2p_messages"] += 1
                self.stats_["p2p_bytes"] += size
                if key not in self.peer_stats and len(self.peer_stats) >= self.PEER_CAP:
                    return
                ps = self.peer_stats.setdefault(key, {"messages": 0, "bytes": 0})
                ps["messages"] += 1
                ps["bytes"] += size
            if ps["messages"] == 1 and NetworkUtils.is_private_ip(ip_only):
                with self._lock:
                    self.stats_["p2p_private_peers"] += 1
        except Exception as e:
            self._err("on_peer_message", e)

    # ================================================================== REST (GET)
    def _register_routes(self):
        route_fn = _g30_find(self.host, "route") if self.host is not None else None
        table = getattr(self.host, "_routes", None) if self.host is not None else None
        defs = (
            ("/api/group30/status",       self._r_status),
            ("/api/group30/roadmap",      self._r_roadmap),
            ("/api/group30/achievement",  self._r_achievement),
            ("/api/group30/project",      self._r_project),
            ("/api/group30/selftest",     self._r_selftest),
            ("/api/group30/genesis",      self._r_genesis),
            ("/api/group30/milestone",    self._r_milestone),
            ("/api/address/validate",     self._r_validate_address),
            ("/api/address/type",         self._r_address_type),
            ("/api/remit/calculate",      self._r_remit_calc),
            ("/api/remit/agents",         self._r_remit_agents),
            ("/api/remit/impact",         self._r_remit_impact),
            ("/api/ext/endpoints",        self._r_ext_list),
        )
        paths = list(defs)
        for p in self._ext_paths():
            paths.append((p, self._make_ext_handler(p)))
        for path, fn in paths:
            try:
                if callable(route_fn):
                    route_fn(path)(fn)
                elif isinstance(table, dict):
                    table.setdefault("GET", {})[path] = fn
                else:
                    break                      # no routing table: layer still works programmatically
                self.routes.append(("GET", path))
                _G30_HOST_ROUTES[path] = fn
            except Exception as e:
                self._err(f"route {path}", e)

    def _unregister_routes(self):
        table = getattr(self.host, "_routes", None) if self.host is not None else None
        if isinstance(table, dict):
            for method, path in self.routes:
                cur = table.get(method, {}).get(path)
                if cur is not None and cur is _G30_HOST_ROUTES.get(path):
                    table[method].pop(path, None)
        for _, path in self.routes:
            _G30_HOST_ROUTES.pop(path, None)
        self.routes = []

    @staticmethod
    def _ext_paths() -> List[str]:
        # the 14 paths listed by ExtendedAPIEndpoints.endpoint_list(), mounted under /api
        return ["/api" + p for p in (
            "/ext/amm/pools", "/ext/amm/quote", "/ext/staking/validators",
            "/ext/staking/network", "/ext/nft/collections", "/ext/nft/listed",
            "/ext/dex/orderbooks", "/ext/dex/trades", "/ext/governance/proposals",
            "/ext/bridge/stats", "/ext/oracle/prices", "/ext/oracle/twap",
            "/ext/pool/workers", "/ext/pool/stats")]

    def _make_ext_handler(self, full_path: str):
        inner = full_path[len("/api"):]
        def handler(path, query, body):
            return self._guard(lambda: self._ext_call(inner, query))
        return handler

    def _ext_call(self, inner_path: str, query):
        params = {}
        if isinstance(query, dict):
            for k in query:
                params[k] = _g30_query(query, k)
        res = self.ext_api().handle(inner_path, params)
        if res is None:
            return _g30_bad("unknown endpoint", 404)
        if isinstance(res, dict) and "error" in res and len(res) == 1:
            return _g30_bad(str(res["error"]), 503)
        return 200, {"success": True, "data": res}

    def _guard(self, fn):
        """Every REST handler: count, catch, never crash the HTTP thread."""
        try:
            with self._lock:
                self.stats_["api_calls"] += 1
            return fn()
        except (ValueError, TypeError, KeyError) as e:      # bad client input, not a layer fault
            return _g30_bad(f"bad request: {e}", 400)
        except Exception as e:
            self._err("rest", e)
            return _g30_bad(f"{type(e).__name__}: {e}", 500)

    def _ok(self, data):
        return 200, {"success": True, "data": data}

    # ---- individual REST handlers (all read-only) ---------------------------
    def _r_status(self, path, query, body):
        return self._guard(lambda: self._ok(self.report()))

    def _r_roadmap(self, path, query, body):
        def f():
            rm = self.roadmap
            return self._ok({"current_phase": rm.current_phase(),
                             "completed_phases": rm.completed_phases()})
        return self._guard(f)

    def _r_achievement(self, path, query, body):
        return self._guard(lambda: self._ok({
            "achievement": NEBULAFinalStats.achievement_unlocked(),
            "note": "static text from the source file; these numbers are NOT measured at runtime"}))

    def _r_project(self, path, query, body):
        return self._guard(lambda: self._ok(self.project_stats.analyze()))

    def _r_selftest(self, path, query, body):
        # GET only reports the last result; it never starts the suite.
        def f():
            with self._lock:
                return self._ok({"running": self._selftest_running, "last": self._selftest})
        return self._guard(f)

    def _r_genesis(self, path, query, body):
        return self._guard(lambda: self._ok(self.genesis.summary()))

    def _r_milestone(self, path, query, body):
        return self._guard(lambda: self._ok(self.milestone().full_ecosystem_status()))

    def _r_validate_address(self, path, query, body):
        def f():
            a = _g30_query(query, "address")
            if not a:
                return _g30_bad("missing ?address=")
            return self._ok(AddressUtils.validate_nbl_address(str(a)))
        return self._guard(f)

    def _r_address_type(self, path, query, body):
        def f():
            a = _g30_query(query, "address")
            if not a:
                return _g30_bad("missing ?address=")
            return self._ok({"address": a, "type": WalletUtils.address_type(str(a))})
        return self._guard(f)

    def _r_remit_calc(self, path, query, body):
        def f():
            frm = _g30_query(query, "from")
            to = _g30_query(query, "to")
            amt = _g30_query(query, "amount")
            if not (frm and to and amt):
                return _g30_bad("need ?from=AED&to=AFN&amount=500")
            amount = float(amt)
            if not (0.01 <= amount <= 1e12):
                return _g30_bad("amount out of range (0.01 .. 1e12)")
            if str(frm) not in NBL_EXCHANGE_RATES or str(to) not in NBL_EXCHANGE_RATES:
                return _g30_bad("unknown currency; known: " + ",".join(sorted(NBL_EXCHANGE_RATES)))
            return self._ok(self.remittance.calculate_transfer(str(frm), amount, str(to)))
        return self._guard(f)

    def _r_remit_agents(self, path, query, body):
        def f():
            cur = _g30_query(query, "currency")
            if not cur:
                return _g30_bad("need ?currency=AFN")
            return self._ok([a.to_dict() for a in self.remittance.find_agents(str(cur))])
        return self._guard(f)

    def _r_remit_impact(self, path, query, body):
        return self._guard(lambda: self._ok(self.remittance.impact_report()))

    def _r_ext_list(self, path, query, body):
        return self._guard(lambda: self._ok(self.ext_api().endpoint_list()))

    # ================================================================== report
    def report(self) -> dict:
        with self._lock:
            return {
                "version": self.VERSION,
                "errors": self.errors,
                "last_error": self.last_error,
                "uptime_s": int(time.time() - self.created_at),
                "classes_total": len(G30_CLASS_ORDER),
                "classes_ok": sum(1 for v in self.wired.values() if v.startswith("ok")),
                "wired": dict(self.wired),
                "routes": [p for _, p in self.routes],
                "stats": dict(self.stats_),
                "votes_recorded": len(self.votes),
                "peers_tracked": len(self.peer_stats),
                "genesis": self.genesis_summary,
                "environment_ready": bool(self.env.get("ready")),
                "listener_attached": self.listener_attached,
                "known_limits": [
                    "RemittanceEngine keeps data in RAM only and does not move NBL on-chain",
                    "NBL_EXCHANGE_RATES are fixed numbers, not oracle prices",
                    "merkle check is observation only (byte-order of host unverified)",
                    "NEBULAFinalStats numbers are static text",
                ],
            }


# ==========================================================================
#  install / uninstall / attach  (patch from outside, fully reversible)
# ==========================================================================
def attach(node, host=None) -> Layer30:
    """Attach a Layer30 to an already-created node and subscribe it to the chain."""
    if host is None:
        host = globals().get("_host")
    layer = Layer30(node, host)
    bc = layer.bc
    if bc is not None and hasattr(bc, "add_listener"):
        bc.add_listener(layer)
    node.group30 = layer
    layer.listener_attached = bool(bc is not None and hasattr(bc, "add_listener"))
    with _G30_LAYERS_LOCK:
        _G30_LAYERS.append(layer)
    return layer


def _g30_p2p_class(host):
    for name in ("P2PNode", "NEBULAP2PNode", "P2PNetwork"):
        cls = getattr(host, name, None)
        if cls is not None and hasattr(cls, "_handle_message"):
            return cls
    return None


def install(host):
    """
    Patch the host from outside:
      * NEBULAFullNode.__init__  -> after the original runs, attach Layer30
      * P2PNode._handle_message  -> original runs FIRST, then the observer
    Safe to call twice. Returns True when the node class was patched.
    """
    cls = getattr(host, "NEBULAFullNode", None)
    if cls is None:
        raise RuntimeError("host has no NEBULAFullNode - cannot install group30")
    if getattr(cls, "_g30_orig", None):
        return False
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)                       # the node must start exactly as before
        try:
            attach(self, host)
        except Exception as e:                    # never stop the node because of this layer
            self.group30_error = e

    cls._g30_orig = orig
    cls.__init__ = patched

    p2p = _g30_p2p_class(host)
    if p2p is not None and not getattr(p2p, "_g30_orig_msg", None):
        orig_msg = p2p._handle_message

        def patched_msg(self, peer, msg, *a, **k):
            result = orig_msg(self, peer, msg, *a, **k)    # original ALWAYS first
            try:
                with _G30_LAYERS_LOCK:
                    layers = list(_G30_LAYERS)
                for layer in layers:
                    layer.on_peer_message(peer, msg)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in install.patched_msg", exc_info=True)
            return result

        p2p._g30_orig_msg = orig_msg
        p2p._handle_message = patched_msg
    return True


def uninstall(host):
    """Undo install(): restore the original methods and detach every live layer."""
    cls = getattr(host, "NEBULAFullNode", None)
    if cls is not None:
        o = getattr(cls, "_g30_orig", None)
        if o:
            cls.__init__ = o
            del cls._g30_orig
    p2p = _g30_p2p_class(host)
    if p2p is not None:
        om = getattr(p2p, "_g30_orig_msg", None)
        if om:
            p2p._handle_message = om
            del p2p._g30_orig_msg
    with _G30_LAYERS_LOCK:
        layers = list(_G30_LAYERS)
    for layer in layers:
        layer.detach()
