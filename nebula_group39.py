"""NEBULA group39 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. CoinMixPool  (orig. lines 65322-65388)
   2. PrivacyMixerManager  (orig. lines 65391-65411)
   3. TaprootScript  (orig. lines 65418-65482)
   4. StateProof  (orig. lines 65493-65561)
   5. NodeType  (orig. lines 65568-65574)
   6. NodeInfo  (orig. lines 65576-65602)
   7. NodeRegistry  (orig. lines 65604-65676)
   8. BridgeProtocol  (orig. lines 65683-65686)
   9. BridgeTransfer  (orig. lines 65688-65713)
  10. TokenBridgeV2  (orig. lines 65715-65793)
  11. TreasuryProposalType  (orig. lines 65800-65805)
  12. TreasuryProposal  (orig. lines 65807-65834)
  13. TreasuryGovernanceV2  (orig. lines 65836-65909)
  14. ContractStdLib  (orig. lines 66051-66131)
  15. AddressFormatter  (orig. lines 66138-66209)
  16. SupplyAnalytics  (orig. lines 66220-66296)
  17. SlashingCondition  (orig. lines 66303-66308)
  18. SlashingConditionsEngine  (orig. lines 66310-66377)
  19. ContractTemplate  (orig. lines 66384-66392)
  20. DeployedContract  (orig. lines 66394-66413)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): AddressType, KeyBlinding, MerkleTree, SlashingEvidence
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

def _v108_fallback(ftype):
    t = str(ftype)
    if t.startswith('Optional') or t.startswith('Any'):
        return None
    if t == 'str':
        return ''
    if t == 'int':
        return 0
    if t == 'float':
        return 0.0
    if t == 'bool':
        return False
    if t == 'bytes':
        return b''
    if t.startswith('Dict') or t.startswith('dict'):
        return {}
    if t.startswith('List') or t.startswith('list'):
        return []
    return None

def _make_compat(base, aliases=None, extra_defaults=None, post=None, name=None):
    """Subclass of dataclass `base` whose __init__ accepts the caller's field
    names (aliases -> real field names), fills every missing field with a
    default, and keeps any unknown keyword as a plain attribute."""
    aliases = dict(aliases or {})
    extra_defaults = dict(extra_defaults or {})
    flds = list(_v108_dc.fields(base))

    def __init__(self, *args, **kw):
        for k in list(kw):
            if k in aliases:
                real = aliases[k]
                v = kw.pop(k)
                kw.setdefault(real, v)
                kw.setdefault(k, v)          # keep the caller's own name too
        for f, v in zip(flds, args):
            kw.setdefault(f.name, v)
        for f in flds:
            if f.name in kw:
                continue
            if f.default is not _v108_dc.MISSING:
                kw[f.name] = f.default
            elif f.default_factory is not _v108_dc.MISSING:
                kw[f.name] = f.default_factory()
            elif f.name in extra_defaults:
                d = extra_defaults[f.name]
                kw[f.name] = d() if callable(d) else d
            else:
                kw[f.name] = _v108_fallback(f.type)
        for k, v in kw.items():
            setattr(self, k, v)
        if post:
            post(self)

    return type(name or (base.__name__ + 'C'), (base,), {'__init__': __init__})

def _v108_slash_post(o):
    o.condition = o.evidence_type

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- CoinMixPool
class CoinMixPool:
    """
    Privacy-preserving coin mixing pool.
    Users deposit equal amounts, receive back unlinked outputs.
    """

    FIXED_DENOMINATIONS = [
        1 * 10**DECIMALS,
        10 * 10**DECIMALS,
        100 * 10**DECIMALS,
        1000 * 10**DECIMALS,
    ]

    def __init__(self, blockchain: 'NEBULABlockchain',
                  denomination: int):
        self._bc           = blockchain
        self.denomination  = denomination
        self._participants: List[dict] = []
        self._outputs:      List[str]  = []   # output addresses
        self._lock         = threading.RLock()
        self._round        = 0
        self._status       = "waiting"

    def join(self, sender: str, output_address: str) -> Tuple[bool, str]:
        with self._lock:
            if self._status != "waiting":
                return False, "Round not accepting"
            bal = self._bc.utxo.balance(sender)
            if bal < self.denomination:
                return False, "Insufficient balance"
            self._participants.append({
                "sender":  sender,
                "amount":  self.denomination,
                "joined":  time.time(),
            })
            self._outputs.append(output_address)
            if len(self._participants) >= 5:
                self._status = "ready"
            return True, (f"Joined mix round {self._round}. "
                          f"Participants: {len(self._participants)}")

    def execute_mix(self) -> Tuple[bool, dict]:
        with self._lock:
            if len(self._participants) < 2:
                return False, {}
            import random
            shuffled = list(self._outputs)
            random.shuffle(shuffled)
            result = {
                "round":       self._round,
                "denomination": self.denomination,
                "outputs":     shuffled,
                "inputs":      len(self._participants),
            }
            self._round        += 1
            self._participants  = []
            self._outputs       = []
            self._status        = "waiting"
            return True, result

    def pool_info(self) -> dict:
        return {
            "denomination_nbl": f"{self.denomination/10**DECIMALS:.3f}",
            "participants":     len(self._participants),
            "status":           self._status,
            "round":            self._round,
        }


# ---- PrivacyMixerManager
class PrivacyMixerManager:
    """Manages multiple coin mixing pools for different denominations."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._pools: Dict[int, CoinMixPool] = {
            d: CoinMixPool(blockchain, d)
            for d in CoinMixPool.FIXED_DENOMINATIONS
        }

    def join_mix(self, sender: str, amount_nbl: float,
                  output_addr: str) -> Tuple[bool, str]:
        amount = int(amount_nbl * 10**DECIMALS)
        pool   = self._pools.get(amount)
        if not pool:
            denoms = [d/10**DECIMALS for d in CoinMixPool.FIXED_DENOMINATIONS]
            return False, f"Invalid denomination. Choose: {denoms}"
        return pool.join(sender, output_addr)

    def mixer_stats(self) -> List[dict]:
        return [p.pool_info() for p in self._pools.values()]


# ---- TaprootScript
class TaprootScript:
    """
    Taproot-style script commitments for NEBULA.
    MAST (Merklized Alternative Script Trees) — reveals only
    the executed branch; other branches stay private.
    """

    def __init__(self):
        self._trees: Dict[str, dict] = {}

    def build_mast(self, scripts: List[bytes]) -> Tuple[str, str]:
        """Build a Merklized script tree. Returns (root_hash, taproot_pubkey)."""
        leaf_hashes = [
            hashlib.sha256(b"MAST_LEAF:" + s).hexdigest()
            for s in scripts
        ]
        root   = MerkleTree.compute_root(leaf_hashes)
        tapkey = hashlib.sha256(root.encode()).hexdigest()[:64]
        tree_id = tapkey[:16]
        self._trees[tree_id] = {
            "root":    root,
            "tapkey":  tapkey,
            "scripts": [s.hex() for s in scripts],
            "leaves":  leaf_hashes,
        }
        return root, tapkey

    def create_spend_proof(self, tree_id: str,
                            script_index: int) -> Optional[dict]:
        """Create Merkle proof to spend a specific script branch."""
        tree = self._trees.get(tree_id)
        if not tree:
            return None
        if script_index >= len(tree["leaves"]):
            return None
        proof = MerkleTree.build_proof(tree["leaves"], tree["leaves"][script_index])
        return {
            "tree_id":      tree_id,
            "script_index": script_index,
            "script":       tree["scripts"][script_index],
            "proof":        proof,
            "root":         tree["root"],
        }

    def verify_spend_proof(self, spend_proof: dict) -> bool:
        """Verify a MAST spend proof."""
        try:
            leaf  = tree_id = spend_proof["script"]
            proof = spend_proof["proof"]
            root  = spend_proof["root"]
            leaf_hash = hashlib.sha256(
                b"MAST_LEAF:" + bytes.fromhex(leaf)
            ).hexdigest()
            return MerkleTree.verify_proof(root, leaf_hash, proof)
        except Exception:
            return False

    def taproot_address(self, internal_key: bytes,
                         mast_root: str) -> str:
        """Compute taproot address from internal key and MAST root."""
        tweak  = hashlib.sha256(internal_key + mast_root.encode()).digest()
        tweaked = KeyBlinding.tweak_privkey(
            int.from_bytes(internal_key[:32], 'big'), tweak)
        tweaked_bytes = tweaked.to_bytes(32, 'big')
        return hashlib.sha256(b"TAPROOT:" + tweaked_bytes).hexdigest()[:40]


# ---- StateProof
class StateProof:
    """
    Compact state proofs for light clients.
    Proves that a specific state exists without full data.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def prove_balance(self, address: str,
                       block_height: int) -> dict:
        """Prove an address had a specific balance at a block height."""
        blk     = self._bc.get_block(block_height)
        balance = self._bc.utxo.balance(address)
        proof_data = {
            "address":      address,
            "balance":      balance,
            "block_height": block_height,
            "block_hash":   blk.hash if blk else "0"*64,
        }
        proof_hash = hashlib.sha256(
            json.dumps(proof_data, sort_keys=True).encode()
        ).hexdigest()
        return {
            **proof_data,
            "proof_hash": proof_hash,
            "proved_at":  time.time(),
        }

    def prove_utxo_existence(self, txid: str, vout: int) -> dict:
        """Prove a UTXO exists in the UTXO set."""
        key  = f"{txid}:{vout}"
        utxo = self._bc.utxo._utxos.get(key)
        if not utxo:
            return {"exists": False, "key": key}
        return {
            "exists":  True,
            "key":     key,
            "value":   utxo.value,
            "address": utxo.address,
        }

    def prove_transaction(self, txid: str,
                           block_height: int) -> dict:
        """Prove a transaction was included in a block."""
        blk = self._bc.get_block(block_height)
        if not blk:
            return {"included": False}
        tx_ids = [tx.txid for tx in blk.transactions]
        if txid not in tx_ids:
            return {"included": False}
        proof = MerkleTree.build_proof(tx_ids, txid)
        return {
            "included":     True,
            "txid":         txid,
            "block_height": block_height,
            "block_hash":   blk.hash,
            "merkle_proof": proof,
            "merkle_root":  blk.header.merkle_root,
        }

    def verify_tx_proof(self, proof: dict) -> bool:
        if not proof.get("included"):
            return False
        return MerkleTree.verify_proof(
            proof["merkle_root"],
            proof["txid"],
            proof["merkle_proof"]
        )


# ---- NodeType
class NodeType(_enum.Enum):
    FULL_NODE    = "full_node"
    LIGHT_NODE   = "light_node"
    MINING_NODE  = "mining_node"
    ARCHIVE_NODE = "archive_node"
    SEED_NODE    = "seed_node"
    VALIDATOR    = "validator"


# ---- NodeInfo
@dataclass
class NodeInfo:
    node_id:    str
    operator:   str
    node_type:  NodeType
    ip:         str
    port:       int
    version:    str
    height:     int
    uptime:     float
    services:   List[str]
    registered: float = 0.0
    last_ping:  float = 0.0
    score:      float = 1.0

    def to_dict(self) -> dict:
        return {
            "node_id":  self.node_id,
            "operator": self.operator,
            "type":     self.node_type.value,
            "ip":       self.ip,
            "port":     self.port,
            "version":  self.version,
            "height":   self.height,
            "services": self.services,
            "score":    f"{self.score:.2f}",
        }


# ---- NodeRegistry
class NodeRegistry:
    """
    On-chain node registry for NEBULA network participants.
    Operators register their nodes for discoverability.
    """

    MIN_STAKE_TO_REGISTER = 100 * 10**DECIMALS

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._nodes: Dict[str, NodeInfo] = {}
        self._lock  = threading.RLock()

    def register(self, operator: str, node_type: NodeType,
                  ip: str, port: int, version: str,
                  services: List[str]) -> Tuple[bool, str]:
        with self._lock:
            if self._bc.utxo.balance(operator) < self.MIN_STAKE_TO_REGISTER:
                return False, "Insufficient stake to register"
            nid = hashlib.sha256(
                f"NODE:{operator}:{ip}:{port}".encode()
            ).hexdigest()[:16]
            self._nodes[nid] = NodeInfo(
                node_id    = nid,
                operator   = operator,
                node_type  = node_type,
                ip         = ip,
                port       = port,
                version    = version,
                height     = self._bc.height,
                uptime     = 100.0,
                services   = services,
                registered = time.time(),
                last_ping  = time.time(),
            )
            return True, nid

    def ping(self, node_id: str, height: int) -> bool:
        with self._lock:
            node = self._nodes.get(node_id)
            if node:
                node.last_ping = time.time()
                node.height    = height
                return True
            return False

    def deregister(self, node_id: str, operator: str) -> bool:
        with self._lock:
            node = self._nodes.get(node_id)
            if node and node.operator == operator:
                del self._nodes[node_id]
                return True
            return False

    def get_active_nodes(self, node_type: NodeType = None,
                          max_age_secs: int = 3600) -> List[dict]:
        cutoff = time.time() - max_age_secs
        nodes  = [n for n in self._nodes.values()
                  if n.last_ping >= cutoff]
        if node_type:
            nodes = [n for n in nodes if n.node_type == node_type]
        return [n.to_dict() for n in nodes]

    def registry_stats(self) -> dict:
        with self._lock:
            by_type = {}
            for n in self._nodes.values():
                t = n.node_type.value
                by_type[t] = by_type.get(t, 0) + 1
        return {
            "total_registered": len(self._nodes),
            "by_type":          by_type,
        }


# ---- BridgeProtocol
class BridgeProtocol(_enum.Enum):
    LOCK_MINT   = "lock_mint"    # lock on source, mint on dest
    BURN_MINT   = "burn_mint"    # burn on source, mint on dest
    LIQUIDITY   = "liquidity"    # use liquidity pools on both sides


# ---- BridgeTransfer
@dataclass
class BridgeTransfer:
    transfer_id: str
    protocol:    BridgeProtocol
    source:      str
    dest:        str
    token:       str
    amount:      int
    sender:      str
    recipient:   str
    fee:         int
    status:      str = "pending"
    proof:       str = ""
    created_at:  float = 0.0
    completed_at: float = 0.0

    def to_dict(self) -> dict:
        return {
            "transfer_id": self.transfer_id,
            "from":        self.source,
            "to":          self.dest,
            "token":       self.token,
            "amount":      f"{self.amount/10**DECIMALS:.6f}",
            "status":      self.status,
            "fee":         f"{self.fee/10**DECIMALS:.6f}",
        }


# ---- TokenBridgeV2
class TokenBridgeV2:
    """
    NEBULA Token Bridge v2 — multi-protocol, multi-chain.
    Supports lock/mint, burn/mint, and liquidity-based bridging.
    """

    BRIDGE_FEE_BPS = 10    # 0.10%
    SUPPORTED      = {
        "ethereum": {"chain_id": 1,   "symbol": "ETH"},
        "bnb_chain": {"chain_id": 56,  "symbol": "BNB"},
        "polygon":  {"chain_id": 137, "symbol": "MATIC"},
        "avalanche": {"chain_id": 43114, "symbol": "AVAX"},
        "arbitrum": {"chain_id": 42161, "symbol": "ARB"},
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._transfers: Dict[str, BridgeTransfer] = {}
        self._liquidity: Dict[str, int]            = {}  # chain -> NBL liquidity
        self._lock      = threading.RLock()
        self._volume:   int = 0

    def initiate(self, sender: str, dest_chain: str,
                  recipient: str, amount_nbl: float,
                  token: str = "NBL",
                  protocol: BridgeProtocol = BridgeProtocol.LOCK_MINT) -> Tuple[bool, str]:
        with self._lock:
            if dest_chain not in self.SUPPORTED:
                return False, f"Unsupported chain: {dest_chain}"
            amount = int(amount_nbl * 10**DECIMALS)
            fee    = amount * self.BRIDGE_FEE_BPS // 10_000
            if self._bc.utxo.balance(sender) < amount:
                return False, "Insufficient balance"
            tid = hashlib.sha256(
                f"BRIDGE2:{sender}:{dest_chain}:{amount}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._transfers[tid] = BridgeTransfer(
                transfer_id = tid,
                protocol    = protocol,
                source      = "nebula",
                dest        = dest_chain,
                token       = token,
                amount      = amount - fee,
                sender      = sender,
                recipient   = recipient,
                fee         = fee,
                created_at  = time.time(),
            )
            return True, tid

    def complete(self, transfer_id: str,
                  relay_proof: str) -> Tuple[bool, str]:
        with self._lock:
            t = self._transfers.get(transfer_id)
            if not t or t.status != "pending":
                return False, "Not found or not pending"
            t.status       = "completed"
            t.proof        = relay_proof
            t.completed_at = time.time()
            self._volume  += t.amount
            return True, f"Bridge transfer complete: {t.amount/10**DECIMALS:.6f} {t.token}"

    def add_liquidity(self, chain: str, amount: int):
        with self._lock:
            self._liquidity[chain] = self._liquidity.get(chain, 0) + amount

    def bridge_stats(self) -> dict:
        with self._lock:
            pending   = sum(1 for t in self._transfers.values()
                            if t.status == "pending")
            completed = sum(1 for t in self._transfers.values()
                            if t.status == "completed")
        return {
            "total_transfers": len(self._transfers),
            "pending":         pending,
            "completed":       completed,
            "volume_nbl":      f"{self._volume/10**DECIMALS:.3f}",
            "supported_chains": list(self.SUPPORTED.keys()),
        }


# ---- TreasuryProposalType
class TreasuryProposalType(_enum.Enum):
    GRANT        = "grant"
    BUYBACK      = "buyback"
    BURN         = "burn"
    INVEST       = "invest"
    PARTNERSHIP  = "partnership"


# ---- TreasuryProposal
@dataclass
class TreasuryProposal:
    proposal_id:  str
    proposer:     str
    ptype:        TreasuryProposalType
    amount:       int
    recipient:    str
    description:  str
    votes_for:    float = 0.0
    votes_against: float = 0.0
    voters:       Dict[str, str] = field(default_factory=dict)
    status:       str = "active"
    created_at:   float = 0.0
    executed_at:  float = 0.0

    def to_dict(self) -> dict:
        total = self.votes_for + self.votes_against
        yes_pct = self.votes_for / total * 100 if total > 0 else 0
        return {
            "proposal_id": self.proposal_id,
            "type":        self.ptype.value,
            "amount_nbl":  f"{self.amount/10**DECIMALS:.3f}",
            "recipient":   self.recipient,
            "description": self.description,
            "yes_pct":     f"{yes_pct:.1f}%",
            "voters":      len(self.voters),
            "status":      self.status,
        }


# ---- TreasuryGovernanceV2
class TreasuryGovernanceV2:
    """Treasury governance v2 with token-weighted voting."""

    QUORUM_PCT    = 0.10    # 10% of supply
    PASS_PCT      = 0.60    # 60% yes

    def __init__(self, blockchain: 'NEBULABlockchain',
                  treasury: 'NEBULATreasury'):
        self._bc       = blockchain
        self._treasury = treasury
        self._proposals: Dict[str, TreasuryProposal] = {}
        self._lock     = threading.RLock()

    def propose(self, proposer: str, ptype: TreasuryProposalType,
                 amount_nbl: float, recipient: str,
                 description: str) -> Tuple[bool, str]:
        with self._lock:
            amount = int(amount_nbl * 10**DECIMALS)
            if amount > self._treasury.balance():
                return False, "Amount exceeds treasury balance"
            pid = hashlib.sha256(
                f"TGOV2:{proposer}:{ptype.value}:{amount}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._proposals[pid] = TreasuryProposal(
                proposal_id = pid,
                proposer    = proposer,
                ptype       = ptype,
                amount      = amount,
                recipient   = recipient,
                description = description,
                created_at  = time.time(),
            )
            return True, pid

    def vote(self, voter: str, proposal_id: str,
              support: bool) -> Tuple[bool, str]:
        with self._lock:
            prop = self._proposals.get(proposal_id)
            if not prop or prop.status != "active":
                return False, "Not active"
            if voter in prop.voters:
                return False, "Already voted"
            weight = self._bc.utxo.balance(voter) / 10**DECIMALS
            if support:
                prop.votes_for += weight
            else:
                prop.votes_against += weight
            prop.voters[voter] = "yes" if support else "no"
            return True, f"Voted (weight: {weight:.2f})"

    def execute(self, proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            prop = self._proposals.get(proposal_id)
            if not prop or prop.status != "active":
                return False, "Not found or not active"
            total_supply = self._bc.utxo.total_supply() / 10**DECIMALS
            total_votes  = prop.votes_for + prop.votes_against
            if total_votes < total_supply * self.QUORUM_PCT:
                return False, f"Quorum not met ({total_votes:.0f} < {total_supply * self.QUORUM_PCT:.0f})"
            if prop.votes_for / total_votes < self.PASS_PCT:
                prop.status = "failed"
                return False, "Did not pass"
            prop.status      = "executed"
            prop.executed_at = time.time()
            return True, f"Treasury proposal executed: {prop.ptype.value}"

    def treasury_governance_stats(self) -> dict:
        by_status = {}
        for p in self._proposals.values():
            by_status[p.status] = by_status.get(p.status, 0) + 1
        return {
            "total_proposals": len(self._proposals),
            "by_status":       by_status,
        }


# ---- ContractStdLib
class ContractStdLib:
    """
    Standard library functions available to NEBULA smart contracts.
    Provides common utilities: math, string ops, crypto.
    """

    @staticmethod
    def safe_add(a: int, b: int) -> int:
        result = a + b
        if result < a:
            raise OverflowError("Safe add overflow")
        return result

    @staticmethod
    def safe_sub(a: int, b: int) -> int:
        if b > a:
            raise ValueError("Safe sub underflow")
        return a - b

    @staticmethod
    def safe_mul(a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        result = a * b
        if result // a != b:
            raise OverflowError("Safe mul overflow")
        return result

    @staticmethod
    def safe_div(a: int, b: int) -> int:
        if b == 0:
            raise ZeroDivisionError("Safe div by zero")
        return a // b

    @staticmethod
    def percentage(amount: int, pct_bps: int) -> int:
        """Calculate percentage in basis points (100 bps = 1%)."""
        return amount * pct_bps // 10_000

    @staticmethod
    def now_block(blockchain: 'NEBULABlockchain') -> int:
        return blockchain.height

    @staticmethod
    def block_timestamp(blockchain: 'NEBULABlockchain') -> float:
        return blockchain.tip.header.timestamp

    @staticmethod
    def address_valid(address: str) -> bool:
        try:
            version, payload = base58check_decode(address)
            return len(payload) == 20 and version in (0x00, 0x05, WIF_VERSION)
        except Exception:
            return False

    @staticmethod
    def keccak256(data: bytes) -> bytes:
        """SHA3-256 (approximation of keccak256)."""
        import hashlib
        return hashlib.sha3_256(data).digest()

    @staticmethod
    def min_val(a: int, b: int) -> int:
        return a if a < b else b

    @staticmethod
    def max_val(a: int, b: int) -> int:
        return a if a > b else b

    @staticmethod
    def clamp(value: int, min_val: int, max_val: int) -> int:
        return max(min_val, min(max_val, value))

    @staticmethod
    def linear_interpolate(start: int, end: int,
                            current: int, total: int) -> int:
        """Linear interpolation between start and end over total steps."""
        if total <= 0:
            return end
        pct = min(current, total) / total
        return int(start + (end - start) * pct)


# ---- AddressFormatter
class AddressFormatter:
    """
    NEBULA address formatting and validation utilities.
    Supports multiple address types and formats.
    """

    VERSION_BYTES = {
        AddressType.P2PKH:   0x00,
        AddressType.P2SH:    0x05,
        AddressType.P2WPKH:  0x06,
        AddressType.P2WSH:   0x07,
        AddressType.TAPROOT: 0x08,
    }

    @classmethod
    def encode_p2pkh(cls, pubkey_hash: bytes) -> str:
        return base58check_encode(pubkey_hash,
                                   cls.VERSION_BYTES[AddressType.P2PKH])

    @classmethod
    def encode_p2sh(cls, script_hash: bytes) -> str:
        return base58check_encode(script_hash,
                                   cls.VERSION_BYTES[AddressType.P2SH])

    @classmethod
    def decode(cls, address: str) -> Tuple[AddressType, bytes]:
        version, payload = base58check_decode(address)
        for atype, vbyte in cls.VERSION_BYTES.items():
            if vbyte == version:
                return atype, payload
        raise ValueError(f"Unknown address version: {version:#x}")

    @classmethod
    def detect_type(cls, address: str) -> Optional[AddressType]:
        try:
            atype, _ = cls.decode(address)
            return atype
        except Exception:
            return None

    @classmethod
    def is_valid(cls, address: str) -> bool:
        return cls.detect_type(address) is not None

    @classmethod
    def pubkey_to_all_formats(cls, pubkey: bytes) -> dict:
        """Generate all address formats from a public key."""
        pkh    = hashlib.new('ripemd160',
                              hashlib.sha256(pubkey).digest()).digest()
        p2pkh  = cls.encode_p2pkh(pkh)
        # P2SH-P2WPKH: script = OP_0 <pubkey_hash>
        rs     = bytes([0x00, 0x14]) + pkh
        rs_h   = hashlib.new('ripemd160',
                               hashlib.sha256(rs).digest()).digest()
        p2sh   = cls.encode_p2sh(rs_h)
        return {
            "p2pkh":  p2pkh,
            "p2sh":   p2sh,
            "pubkey": pubkey.hex(),
        }

    @staticmethod
    def checksum(address: str) -> str:
        """EIP-55 style mixed-case checksum for NEBULA addresses."""
        h = hashlib.sha256(address.lower().encode()).hexdigest()
        result = ""
        for i, c in enumerate(address):
            if c.isalpha():
                result += c.upper() if int(h[i % 64], 16) >= 8 else c.lower()
            else:
                result += c
        return result


# ---- SupplyAnalytics
class SupplyAnalytics:
    """
    Analyzes NBL token supply distribution.
    Rich list, Gini coefficient, supply concentration.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def rich_list(self, n: int = 100) -> List[dict]:
        """Top N addresses by NBL balance."""
        utxo    = self._bc.utxo
        addrs   = list(utxo._addr_idx.keys())
        balances = [(a, utxo.balance(a)) for a in addrs if utxo.balance(a) > 0]
        balances.sort(key=lambda x: -x[1])
        total   = utxo.total_supply()
        result  = []
        cum_pct  = 0.0
        for rank, (addr, bal) in enumerate(balances[:n], 1):
            pct      = bal / total * 100 if total > 0 else 0
            cum_pct += pct
            result.append({
                "rank":       rank,
                "address":    addr,
                "balance":    f"{bal/10**DECIMALS:.6f}",
                "pct":        f"{pct:.4f}%",
                "cumulative": f"{cum_pct:.2f}%",
            })
        return result

    def gini_coefficient(self) -> float:
        """Calculate Gini coefficient of NBL distribution (0=equal, 1=unequal)."""
        utxo     = self._bc.utxo
        addrs    = list(utxo._addr_idx.keys())
        balances = sorted([utxo.balance(a) for a in addrs if utxo.balance(a) > 0])
        if not balances:
            return 0.0
        n     = len(balances)
        total = sum(balances)
        if total == 0:
            return 0.0
        gini  = 0.0
        for i, b in enumerate(balances):
            gini += (2 * (i + 1) - n - 1) * b
        return gini / (n * total)

    def supply_distribution(self) -> dict:
        utxo    = self._bc.utxo
        addrs   = list(utxo._addr_idx.keys())
        balances = sorted([utxo.balance(a) for a in addrs if utxo.balance(a) > 0], reverse=True)
        total    = utxo.total_supply()
        if not balances or total == 0:
            return {}
        top1   = sum(balances[:1]) / total * 100
        top10  = sum(balances[:10]) / total * 100
        top100 = sum(balances[:100]) / total * 100
        return {
            "total_supply":    f"{total/10**DECIMALS:.3f}",
            "holders":         len(balances),
            "top_1_pct":       f"{top1:.2f}%",
            "top_10_pct":      f"{top10:.2f}%",
            "top_100_pct":     f"{top100:.2f}%",
            "gini":            f"{self.gini_coefficient():.4f}",
        }

    def circulating_supply(self, locked_addresses: List[str] = None) -> int:
        utxo    = self._bc.utxo
        locked  = sum(utxo.balance(a) for a in (locked_addresses or []))
        return utxo.total_supply() - locked

    def inflation_rate(self) -> float:
        """Estimate annual inflation rate based on block rewards."""
        height   = self._bc.height
        reward   = mining_reward(height)
        annual   = reward * 365 * 144   # blocks per year
        supply   = self._bc.utxo.total_supply()
        return annual / supply * 100 if supply > 0 else 0.0


# ---- SlashingCondition
class SlashingCondition(_enum.Enum):
    DOUBLE_VOTE       = "double_vote"
    SURROUND_VOTE     = "surround_vote"
    PROPOSER_SLASHING = "proposer_slashing"
    OFFLINE           = "offline"
    INVALID_BLOCK     = "invalid_block"


# ---- SlashingConditionsEngine
@dataclass
class SlashingConditionsEngine:
    """
    Detects and processes validator slashing conditions.
    Evidence can be submitted by any network participant.
    """

    SLASH_RATES = {
        SlashingCondition.DOUBLE_VOTE:       0.05,
        SlashingCondition.SURROUND_VOTE:     0.02,
        SlashingCondition.PROPOSER_SLASHING: 0.10,
        SlashingCondition.OFFLINE:           0.01,
        SlashingCondition.INVALID_BLOCK:     0.05,
    }
    REPORTER_REWARD_PCT = 0.05   # 5% of slash goes to reporter

    def __init__(self, pos_engine: 'PoSEngine' = None,
                  blockchain: 'NEBULABlockchain' = None):
        self._pos   = pos_engine
        self._bc    = blockchain
        self._evidences: Dict[str, SlashingEvidence] = {}
        self._lock  = threading.RLock()

    def submit_evidence(self, reporter: str,
                         validator: str,
                         condition: SlashingCondition,
                         evidence_data: dict) -> Tuple[bool, str]:
        with self._lock:
            eid = hashlib.sha256(
                f"SLASH:{validator}:{condition.value}:{time.time()}".encode()
            ).hexdigest()[:16]
            height = self._bc.height if self._bc else 0
            self._evidences[eid] = SlashingEvidenceC(
                evidence_id   = eid,
                validator     = validator,
                condition     = condition,
                block_height  = height,
                evidence_data = evidence_data,
                submitted_by  = reporter,
                timestamp     = time.time(),
            )
            return True, eid

    def process_evidence(self, evidence_id: str) -> Tuple[bool, str]:
        with self._lock:
            ev = self._evidences.get(evidence_id)
            if not ev or ev.processed:
                return False, "Not found or already processed"
            rate       = self.SLASH_RATES.get(ev.condition, 0.01)
            stake      = 10_000 * 10**DECIMALS   # placeholder
            slash_amt  = int(stake * rate)
            ev.slash_amount = slash_amt
            ev.processed    = True
            reporter_reward = int(slash_amt * self.REPORTER_REWARD_PCT)
            if self._pos:
                self._pos.slash_double_sign(ev.validator)
            return True, (f"Slashed {slash_amt/10**DECIMALS:.3f} NBL from {ev.validator}. "
                          f"Reporter reward: {reporter_reward/10**DECIMALS:.3f} NBL")

    def slashing_stats(self) -> dict:
        with self._lock:
            processed = sum(1 for e in self._evidences.values() if e.processed)
            total_slash = sum(e.slash_amount for e in self._evidences.values())
        return {
            "total_evidence":   len(self._evidences),
            "processed":        processed,
            "total_slashed_nbl": f"{total_slash/10**DECIMALS:.3f}",
        }


# ---- ContractTemplate
class ContractTemplate(_enum.Enum):
    ERC20         = "erc20"
    ERC721        = "erc721"
    MULTISIG      = "multisig"
    VESTING       = "vesting"
    ESCROW        = "escrow"
    LIQUIDITY_POOL = "liquidity_pool"
    STAKING       = "staking"
    DAO           = "dao"


# ---- DeployedContract
@dataclass
class DeployedContract:
    contract_id:  str
    template:     ContractTemplate
    deployer:     str
    params:       dict
    deployed_at:  float
    block_height: int
    bytecode_hash: str
    verified:     bool = False

    def to_dict(self) -> dict:
        return {
            "contract_id":   self.contract_id,
            "template":      self.template.value,
            "deployer":      self.deployer,
            "deployed_at":   self.deployed_at,
            "block_height":  self.block_height,
            "verified":      self.verified,
        }
