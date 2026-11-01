"""NEBULA group37 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. DiscoveredPeer  (orig. lines 62608-62634)
   2. LightningChannel  (orig. lines 62743-62770)
   3. LightningNetworkV2  (orig. lines 62772-62918)
   4. VotingMechanism  (orig. lines 62928-62933)
   5. Delegation  (orig. lines 62935-62940)
   6. GovernanceV2  (orig. lines 62942-63107)
   7. OracleFeedType  (orig. lines 63118-63124)
   8. OracleReport  (orig. lines 63126-63142)
   9. OracleFeed  (orig. lines 63144-63165)
  10. OracleV2  (orig. lines 63167-63296)
  11. StablecoinMechanism  (orig. lines 63303-63305)
  12. StablecoinProtocol  (orig. lines 63307-63414)
  13. MultisigPolicy  (orig. lines 63421-63425)
  14. MultisigWalletV2  (orig. lines 63427-63451)
  15. MultisigManagerV2  (orig. lines 63453-63563)
  16. SwapRoute  (orig. lines 63570-63587)
  17. DeFiAggregatorV2  (orig. lines 63589-63702)
  18. BlockExplorerBackend  (orig. lines 63709-63851)
  19. NFTAuctionType  (orig. lines 63866-63870)
  20. NFTListing  (orig. lines 63872-63910)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): Secp256k1
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
CHAIN_ID            = 2025

DECIMALS            = 9

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

PROTOCOL_VERSION       = 70015

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

def base58check_encode(payload: bytes, version: int) -> str:
    versioned = bytes([version]) + payload
    checksum  = sha256d(versioned)[:4]
    return base58_encode(versioned + checksum)

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

def info(msg):  print(c(f"ℹ️  {msg}", C.CYAN))

_routes: Dict[str, Dict[str, Callable]] = {}

def route(path: str, methods: List[str] = None):
    """Decorator to register an API endpoint."""
    def decorator(fn: Callable) -> Callable:
        for method in (methods or ["GET"]):
            _routes.setdefault(method.upper(), {})[path] = fn
        return fn
    return decorator

def payment_hash(preimage: bytes) -> bytes:
    """SHA256 of preimage = payment hash (R-hash)"""
    return hashlib.sha256(preimage).digest()

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

def _v108_feed_post(o):
    if not o.name:
        o.name = o.feed_id

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- DiscoveredPeer
@dataclass
class DiscoveredPeer:
    ip:            str
    port:          int
    services:      int = 1
    last_seen:     float = 0.0
    version:       int = PROTOCOL_VERSION
    user_agent:    str = ""
    height:        int = 0
    latency_ms:    float = 0.0
    success_rate:  float = 1.0
    discovery:     str = "unknown"

    def score(self) -> float:
        age_penalty = max(0, (time.time() - self.last_seen) / 86400)
        return self.success_rate * 100 - age_penalty

    def to_dict(self) -> dict:
        return {
            "ip":          self.ip,
            "port":        self.port,
            "version":     self.version,
            "height":      self.height,
            "latency_ms":  f"{self.latency_ms:.1f}",
            "score":       f"{self.score():.1f}",
            "discovery":   self.discovery,
        }


# ---- LightningChannel
@dataclass
class LightningChannel:
    channel_id:   str
    party_a:      str
    party_b:      str
    capacity:     int
    balance_a:    int
    balance_b:    int
    state_num:    int = 0
    open:         bool = True
    htlcs:        List[dict] = field(default_factory=list)

    @property
    def balance_a_pct(self) -> float:
        return self.balance_a / self.capacity * 100 if self.capacity > 0 else 0

    def to_dict(self) -> dict:
        return {
            "channel_id": self.channel_id,
            "party_a":    self.party_a,
            "party_b":    self.party_b,
            "capacity_nbl": f"{self.capacity/10**DECIMALS:.3f}",
            "balance_a":    f"{self.balance_a/10**DECIMALS:.6f}",
            "balance_b":    f"{self.balance_b/10**DECIMALS:.6f}",
            "state_num":    self.state_num,
            "open":         self.open,
            "htlcs":        len(self.htlcs),
        }


# ---- LightningNetworkV2
class LightningNetworkV2:
    """
    NEBULA Lightning Network v2 — off-chain payment channels.
    Near-instant payments with on-chain settlement.
    Supports multi-hop routing via HTLCs.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._channels: Dict[str, LightningChannel] = {}
        self._routes:   Dict[str, List[str]]        = {}  # (a,b) -> path
        self._lock      = threading.RLock()

    def open_channel(self, party_a: str, party_b: str,
                      capacity_nbl: float,
                      initial_push: float = 0.0) -> Tuple[bool, str]:
        with self._lock:
            capacity = int(capacity_nbl * 10**DECIMALS)
            push     = int(initial_push * 10**DECIMALS)
            if self._bc.utxo.balance(party_a) < capacity:
                return False, "Insufficient balance for channel"
            cid = hashlib.sha256(
                f"LN:{party_a}:{party_b}:{capacity}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._channels[cid] = LightningChannel(
                channel_id = cid,
                party_a    = party_a,
                party_b    = party_b,
                capacity   = capacity,
                balance_a  = capacity - push,
                balance_b  = push,
            )
            return True, cid

    def send_payment(self, channel_id: str, sender: str,
                      amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            ch = self._channels.get(channel_id)
            if not ch or not ch.open:
                return False, "Channel not found or closed"
            amount = int(amount_nbl * 10**DECIMALS)
            if ch.party_a == sender:
                if ch.balance_a < amount:
                    return False, "Insufficient channel balance"
                ch.balance_a -= amount
                ch.balance_b += amount
            elif ch.party_b == sender:
                if ch.balance_b < amount:
                    return False, "Insufficient channel balance"
                ch.balance_b -= amount
                ch.balance_a += amount
            else:
                return False, "Not a channel participant"
            ch.state_num += 1
            return True, (f"Sent {amount_nbl:.6f} NBL off-chain. "
                          f"State #{ch.state_num}")

    def add_htlc(self, channel_id: str, sender: str,
                  amount: int, payment_hash: str,
                  timelock: int) -> Tuple[bool, str]:
        with self._lock:
            ch = self._channels.get(channel_id)
            if not ch or not ch.open:
                return False, "Channel unavailable"
            htlc = {
                "id":           secrets.token_hex(8),
                "sender":       sender,
                "amount":       amount,
                "payment_hash": payment_hash,
                "timelock":     timelock,
                "status":       "pending",
            }
            ch.htlcs.append(htlc)
            return True, htlc["id"]

    def settle_htlc(self, channel_id: str, htlc_id: str,
                     preimage: bytes) -> Tuple[bool, str]:
        with self._lock:
            ch = self._channels.get(channel_id)
            if not ch:
                return False, "Channel not found"
            for htlc in ch.htlcs:
                if htlc["id"] == htlc_id:
                    h = hashlib.sha256(preimage).hexdigest()
                    if h == htlc["payment_hash"]:
                        htlc["status"] = "settled"
                        return True, "HTLC settled"
                    return False, "Wrong preimage"
            return False, "HTLC not found"

    def close_channel(self, channel_id: str,
                       requester: str) -> Tuple[bool, dict]:
        with self._lock:
            ch = self._channels.get(channel_id)
            if not ch or not ch.open:
                return False, {}
            if requester not in (ch.party_a, ch.party_b):
                return False, {}
            ch.open = False
            return True, {
                "channel_id":    channel_id,
                "final_a":       f"{ch.balance_a/10**DECIMALS:.9f}",
                "final_b":       f"{ch.balance_b/10**DECIMALS:.9f}",
                "state_updates": ch.state_num,
            }

    def find_route(self, source: str, dest: str,
                    amount: int) -> Optional[List[str]]:
        """Find a payment route through the channel network."""
        # Simple BFS route finding
        graph: Dict[str, List[Tuple[str, str]]] = {}
        for cid, ch in self._channels.items():
            if not ch.open:
                continue
            if ch.party_a not in graph:
                graph[ch.party_a] = []
            if ch.party_b not in graph:
                graph[ch.party_b] = []
            graph[ch.party_a].append((ch.party_b, cid))
            graph[ch.party_b].append((ch.party_a, cid))

        visited  = {source}
        queue    = [(source, [source])]
        while queue:
            node, path = queue.pop(0)
            for neighbor, cid in graph.get(node, []):
                ch = self._channels[cid]
                bal = ch.balance_a if ch.party_a == node else ch.balance_b
                if bal < amount:
                    continue
                new_path = path + [neighbor]
                if neighbor == dest:
                    return new_path
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, new_path))
        return None

    def network_stats(self) -> dict:
        with self._lock:
            open_ch   = [c for c in self._channels.values() if c.open]
            total_cap = sum(c.capacity for c in open_ch)
        return {
            "total_channels":   len(self._channels),
            "open_channels":    len(open_ch),
            "total_capacity":   f"{total_cap/10**DECIMALS:.3f} NBL",
        }


# ---- VotingMechanism
class VotingMechanism(_enum.Enum):
    SIMPLE_MAJORITY  = "simple_majority"
    SUPERMAJORITY    = "supermajority"     # 67%
    QUADRATIC        = "quadratic"
    TOKEN_WEIGHTED   = "token_weighted"
    ONE_PERSON_ONE   = "one_person_one"


# ---- Delegation
@dataclass
class Delegation:
    delegator:  str
    delegate:   str
    scope:      str = "all"   # "all" or specific proposal type
    expires:    Optional[float] = None


# ---- GovernanceV2
class GovernanceV2:
    """
    NEBULA Governance v2 with advanced features.
    Vote delegation, quadratic voting, proposal templates,
    emergency veto by guardian council.
    """

    PROPOSAL_TEMPLATES = {
        "parameter_change": {
            "required_fields": ["param_name", "new_value", "reason"],
            "quorum": 0.10,
            "threshold": 0.50,
            "mechanism": VotingMechanism.TOKEN_WEIGHTED,
        },
        "treasury_spend": {
            "required_fields": ["recipient", "amount", "purpose"],
            "quorum": 0.15,
            "threshold": 0.60,
            "mechanism": VotingMechanism.TOKEN_WEIGHTED,
        },
        "protocol_upgrade": {
            "required_fields": ["upgrade_description", "activation_block"],
            "quorum": 0.20,
            "threshold": 0.67,
            "mechanism": VotingMechanism.SUPERMAJORITY,
        },
        "text_proposal": {
            "required_fields": ["text"],
            "quorum": 0.05,
            "threshold": 0.50,
            "mechanism": VotingMechanism.SIMPLE_MAJORITY,
        },
    }

    GUARDIAN_VETO_THRESHOLD = 5   # 5 guardians needed for veto

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc           = blockchain
        self._proposals:   Dict[str, dict]        = {}
        self._delegations: Dict[str, Delegation]  = {}
        self._guardians:   Set[str]               = set()
        self._vetos:       Dict[str, Set[str]]    = {}  # pid -> {vetoing guardians}
        self._lock         = threading.RLock()

    def add_guardian(self, address: str):
        with self._lock:
            self._guardians.add(address)

    def delegate_vote(self, delegator: str, delegate: str,
                       scope: str = "all",
                       expires_days: int = 30) -> bool:
        with self._lock:
            key = f"{delegator}:{scope}"
            self._delegations[key] = Delegation(
                delegator = delegator,
                delegate  = delegate,
                scope     = scope,
                expires   = time.time() + expires_days * 86400,
            )
            return True

    def effective_voter(self, address: str, scope: str = "all") -> str:
        """Get the effective voter (may be a delegate)."""
        key = f"{address}:{scope}"
        d   = self._delegations.get(key)
        if d and (d.expires is None or time.time() < d.expires):
            return self.effective_voter(d.delegate, scope)  # chain
        return address

    def create_proposal(self, creator: str, template: str,
                          title: str, fields: dict) -> Tuple[bool, str]:
        with self._lock:
            tmpl = self.PROPOSAL_TEMPLATES.get(template)
            if not tmpl:
                return False, f"Unknown template: {template}"
            for req in tmpl["required_fields"]:
                if req not in fields:
                    return False, f"Missing field: {req}"
            pid = hashlib.sha256(
                f"GOVV2:{creator}:{template}:{title}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._proposals[pid] = {
                "id":         pid,
                "creator":    creator,
                "template":   template,
                "title":      title,
                "fields":     fields,
                "quorum":     tmpl["quorum"],
                "threshold":  tmpl["threshold"],
                "mechanism":  tmpl["mechanism"].value,
                "votes_yes":  0.0,
                "votes_no":   0.0,
                "voters":     {},
                "vetoed":     False,
                "status":     "active",
                "created_at": time.time(),
            }
            self._vetos[pid] = set()
            return True, pid

    def vote(self, voter: str, proposal_id: str,
              support: bool) -> Tuple[bool, str]:
        with self._lock:
            eff_voter = self.effective_voter(voter)
            prop = self._proposals.get(proposal_id)
            if not prop or prop["status"] != "active":
                return False, "Not active"
            if eff_voter in prop["voters"]:
                return False, "Already voted (or delegated voter already voted)"
            weight = self._bc.utxo.balance(eff_voter) / 10**DECIMALS
            if prop["mechanism"] == VotingMechanism.QUADRATIC.value:
                weight = weight ** 0.5   # quadratic
            elif prop["mechanism"] == VotingMechanism.ONE_PERSON_ONE.value:
                weight = 1.0
            if support:
                prop["votes_yes"] += weight
            else:
                prop["votes_no"]  += weight
            prop["voters"][eff_voter] = "yes" if support else "no"
            return True, f"Vote recorded (weight: {weight:.2f})"

    def guardian_veto(self, guardian: str,
                       proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            if guardian not in self._guardians:
                return False, "Not a guardian"
            prop = self._proposals.get(proposal_id)
            if not prop:
                return False, "Not found"
            self._vetos[proposal_id].add(guardian)
            if len(self._vetos[proposal_id]) >= self.GUARDIAN_VETO_THRESHOLD:
                prop["vetoed"] = True
                prop["status"] = "vetoed"
                return True, f"Proposal VETOED by guardian council"
            return True, (f"Veto vote recorded "
                          f"({len(self._vetos[proposal_id])}/{self.GUARDIAN_VETO_THRESHOLD})")

    def tally(self, proposal_id: str) -> dict:
        prop = self._proposals.get(proposal_id)
        if not prop:
            return {}
        total = prop["votes_yes"] + prop["votes_no"]
        yes_pct = prop["votes_yes"] / total * 100 if total > 0 else 0
        return {
            "proposal_id": proposal_id,
            "votes_yes":   f"{prop['votes_yes']:.2f}",
            "votes_no":    f"{prop['votes_no']:.2f}",
            "yes_pct":     f"{yes_pct:.1f}%",
            "quorum_met":  total >= prop["quorum"] * 1000,
            "passing":     yes_pct / 100 >= prop["threshold"],
            "vetoed":      prop["vetoed"],
            "status":      prop["status"],
        }

    def governance_v2_stats(self) -> dict:
        with self._lock:
            by_status = {}
            for p in self._proposals.values():
                s = p["status"]
                by_status[s] = by_status.get(s, 0) + 1
        return {
            "total_proposals": len(self._proposals),
            "by_status":       by_status,
            "guardians":       len(self._guardians),
            "delegations":     len(self._delegations),
        }


# ---- OracleFeedType
class OracleFeedType(_enum.Enum):
    PRICE        = "price"
    WEATHER      = "weather"
    SPORT        = "sport"
    ELECTION     = "election"
    RANDOM       = "random"
    CUSTOM       = "custom"


# ---- OracleReport
@dataclass
class OracleReport:
    feed_id:    str
    reporter:   str
    value:      Any
    timestamp:  float
    signature:  bytes
    confidence: float = 1.0

    def to_dict(self) -> dict:
        return {
            "feed_id":    self.feed_id,
            "reporter":   self.reporter,
            "value":      self.value,
            "timestamp":  self.timestamp,
            "confidence": self.confidence,
        }


# ---- OracleFeed
@dataclass
class OracleFeed:
    feed_id:      str
    name:         str
    feed_type:    OracleFeedType
    description:  str
    decimals:     int = 8
    heartbeat:    int = 3600    # seconds
    deviation_pct: float = 0.5
    reports:      List[OracleReport] = field(default_factory=list)
    aggregated:   Any = None
    last_update:  float = 0.0

    def to_dict(self) -> dict:
        return {
            "feed_id":    self.feed_id,
            "name":       self.name,
            "type":       self.feed_type.value,
            "value":      self.aggregated,
            "last_update": self.last_update,
            "reporters":  len(self.reports),
        }


# ---- OracleV2
class OracleV2:
    """
    NEBULA Oracle v2 — decentralized multi-feed oracle.
    Supports price, weather, sports, elections.
    Stake-weighted aggregation with outlier rejection.
    """

    OUTLIER_ZSCORE = 2.0    # reject reports >2 std deviations away

    def __init__(self, blockchain: 'NEBULABlockchain' = None):
        self._bc      = blockchain
        self._feeds:  Dict[str, OracleFeed]     = {}
        self._reporters: Dict[str, dict]        = {}   # addr -> {stake, reputation}
        self._lock    = threading.RLock()
        self._init_default_feeds()

    def _init_default_feeds(self):
        defaults = [
            ("NBL/USD",  "NBL Price in USD",  OracleFeedType.PRICE),
            ("NBL/BTC",  "NBL Price in BTC",  OracleFeedType.PRICE),
            ("BTC/USD",  "Bitcoin Price",     OracleFeedType.PRICE),
            ("ETH/USD",  "Ethereum Price",    OracleFeedType.PRICE),
            ("GAS_PRICE","Network Gas Price", OracleFeedType.PRICE),
        ]
        for fid, name, ftype in defaults:
            self.create_feed(fid, name, ftype)

    def create_feed(self, feed_id: str, name: str,
                     feed_type: OracleFeedType,
                     description: str = "") -> str:
        with self._lock:
            self._feeds[feed_id] = OracleFeed(
                feed_id     = feed_id,
                name        = name,
                feed_type   = feed_type,
                description = description,
            )
            return feed_id

    def register_reporter(self, address: str, stake: int):
        with self._lock:
            self._reporters[address] = {
                "stake":      stake,
                "reputation": 1.0,
                "reports":    0,
                "correct":    0,
            }

    def report(self, reporter: str, feed_id: str,
                value: Any, privkey: int) -> Tuple[bool, str]:
        with self._lock:
            if reporter not in self._reporters:
                return False, "Not a registered reporter"
            feed = self._feeds.get(feed_id)
            if not feed:
                return False, "Feed not found"
            msg_bytes = json.dumps(
                {"feed": feed_id, "value": str(value), "ts": time.time()}
            ).encode()
            r, s    = Secp256k1.sign(privkey, hashlib.sha256(msg_bytes).digest())
            sig     = Secp256k1.sig_to_der(r, s)
            report  = OracleReport(
                feed_id    = feed_id,
                reporter   = reporter,
                value      = value,
                timestamp  = time.time(),
                signature  = sig,
                confidence = self._reporters[reporter]["reputation"],
            )
            feed.reports.append(report)
            if len(feed.reports) > 100:
                feed.reports.pop(0)
            self._reporters[reporter]["reports"] += 1
            self._aggregate_feed(feed)
            return True, f"Report accepted for {feed_id}"

    def _aggregate_feed(self, feed: OracleFeed):
        """Aggregate reports using stake-weighted median."""
        recent   = [r for r in feed.reports
                    if time.time() - r.timestamp < 3600]
        if not recent:
            return
        try:
            values = [float(r.value) for r in recent]
            weights = [self._reporters.get(r.reporter, {}).get("stake", 1) *
                       r.confidence for r in recent]
            if not values:
                return
            # Weighted median
            pairs   = sorted(zip(values, weights))
            total_w = sum(w for _, w in pairs)
            cum     = 0.0
            for v, w in pairs:
                cum += w
                if cum >= total_w / 2:
                    feed.aggregated = v
                    break
            feed.last_update = time.time()
        except (ValueError, TypeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, TypeError) in OracleV2._aggregate_feed", exc_info=True)

    def latest(self, feed_id: str) -> Optional[Any]:
        feed = self._feeds.get(feed_id)
        return feed.aggregated if feed else None

    def update_price(self, pair: str, price: float,
                      reporter: str = "") -> bool:
        """Convenience: set price directly (testing/internal use)."""
        with self._lock:
            if pair not in self._feeds:
                self._feeds[pair] = OracleFeedC(feed_id=pair)
            self._feeds[pair].aggregated = price
            self._feeds[pair].last_update = time.time()
            return True

    def price(self, pair: str) -> Optional[float]:
        return self.latest(pair)

    def oracle_stats(self) -> dict:
        with self._lock:
            active_feeds = sum(
                1 for f in self._feeds.values()
                if f.last_update > time.time() - 3600
            )
        return {
            "total_feeds":   len(self._feeds),
            "active_feeds":  active_feeds,
            "reporters":     len(self._reporters),
            "feed_ids":      list(self._feeds.keys()),
        }


# ---- StablecoinMechanism
class StablecoinMechanism(_enum.Enum):
    COLLATERAL = "collateral"   # backed by NBL collateral
    ALGORITHMIC = "algorithmic" # expands/contracts supply


# ---- StablecoinProtocol
class StablecoinProtocol:
    """
    NEBULA algorithmic stablecoin (NBUSD).
    Soft-peg to USD via collateral-backed minting.
    CDP (Collateralized Debt Position) system.
    """

    SYMBOL          = "NBUSD"
    TARGET_PRICE    = 1.0        # $1.00 USD
    MIN_COLLAT_RATIO = 1.5       # 150% minimum collateralization
    LIQUIDATION_RATIO = 1.2      # liquidate below 120%
    STABILITY_FEE   = 0.02       # 2% annual
    LIQUIDATION_PEN = 0.13       # 13% liquidation penalty

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2'):
        self._bc      = blockchain
        self._oracle  = oracle
        self._cdps:   Dict[str, dict]   = {}   # cdp_id -> CDP data
        self._supply: int               = 0    # total NBUSD minted
        self._lock    = threading.RLock()

    def open_cdp(self, owner: str, collateral_nbl: float) -> Tuple[bool, str]:
        """Open a Collateralized Debt Position."""
        with self._lock:
            collat  = int(collateral_nbl * 10**DECIMALS)
            bal     = self._bc.utxo.balance(owner)
            if bal < collat:
                return False, "Insufficient NBL"
            cdp_id  = hashlib.sha256(
                f"CDP:{owner}:{collat}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._cdps[cdp_id] = {
                "cdp_id":        cdp_id,
                "owner":         owner,
                "collateral":    collat,
                "debt":          0,
                "opened_at":     time.time(),
                "last_fee_calc": time.time(),
                "liquidated":    False,
            }
            return True, cdp_id

    def mint_nbusd(self, cdp_id: str, amount: float) -> Tuple[bool, str]:
        """Mint NBUSD against CDP collateral."""
        with self._lock:
            cdp = self._cdps.get(cdp_id)
            if not cdp or cdp["liquidated"]:
                return False, "CDP not found or liquidated"
            nbl_price = self._oracle.price("NBL/USD") or 0.01
            max_debt  = int(cdp["collateral"] * nbl_price / self.MIN_COLLAT_RATIO)
            mint_raw  = int(amount * 10**DECIMALS)
            if cdp["debt"] + mint_raw > max_debt:
                return False, (f"Exceeds max debt. Max: "
                               f"{max_debt/10**DECIMALS:.2f} NBUSD")
            cdp["debt"]  += mint_raw
            self._supply += mint_raw
            return True, f"Minted {amount:.2f} NBUSD"

    def repay(self, cdp_id: str, amount: float) -> Tuple[bool, str]:
        with self._lock:
            cdp = self._cdps.get(cdp_id)
            if not cdp:
                return False, "CDP not found"
            repay_raw = min(int(amount * 10**DECIMALS), cdp["debt"])
            cdp["debt"]  -= repay_raw
            self._supply -= repay_raw
            return True, f"Repaid {repay_raw/10**DECIMALS:.2f} NBUSD"

    def get_collateral_ratio(self, cdp_id: str) -> float:
        cdp = self._cdps.get(cdp_id)
        if not cdp or cdp["debt"] == 0:
            return float('inf')
        nbl_price = self._oracle.price("NBL/USD") or 0.01
        collat_usd = cdp["collateral"] * nbl_price / 10**DECIMALS
        debt_usd   = cdp["debt"] / 10**DECIMALS
        return collat_usd / debt_usd

    def check_liquidations(self) -> List[str]:
        """Check all CDPs for liquidation eligibility."""
        liquidated = []
        with self._lock:
            for cdp_id, cdp in self._cdps.items():
                if cdp["liquidated"] or cdp["debt"] == 0:
                    continue
                ratio = self.get_collateral_ratio(cdp_id)
                if ratio < self.LIQUIDATION_RATIO:
                    cdp["liquidated"] = True
                    penalty = int(cdp["collateral"] * self.LIQUIDATION_PEN)
                    self._supply -= cdp["debt"]
                    liquidated.append(cdp_id)
        return liquidated

    def stablecoin_stats(self) -> dict:
        with self._lock:
            active_cdps = sum(1 for c in self._cdps.values()
                              if not c["liquidated"])
            total_collat = sum(c["collateral"] for c in self._cdps.values()
                               if not c["liquidated"])
            nbl_price = self._oracle.price("NBL/USD") or 0.0
        return {
            "symbol":             self.SYMBOL,
            "total_supply":       f"{self._supply/10**DECIMALS:.2f}",
            "active_cdps":        active_cdps,
            "total_collateral":   f"{total_collat/10**DECIMALS:.3f} NBL",
            "nbl_price_usd":      f"${nbl_price:.4f}",
            "min_collat_ratio":   f"{self.MIN_COLLAT_RATIO*100:.0f}%",
        }


# ---- MultisigPolicy
class MultisigPolicy(_enum.Enum):
    SIMPLE      = "m_of_n"
    TIMELOCK    = "timelock"
    HIERARCHICAL = "hierarchical"
    SOCIAL_RECOVERY = "social_recovery"


# ---- MultisigWalletV2
@dataclass
class MultisigWalletV2:
    wallet_id:    str
    signers:      List[str]
    required:     int
    policy:       MultisigPolicy
    timelock:     int = 0         # blocks for timelock policy
    created_at:   float = 0.0
    spent:        int = 0

    @property
    def address(self) -> str:
        data = f"MULTISIG2:{':'.join(sorted(self.signers))}:{self.required}"
        h    = hashlib.sha256(data.encode()).hexdigest()
        return base58check_encode(bytes.fromhex(h[:40]), 0x05)[:34]

    def to_dict(self) -> dict:
        return {
            "wallet_id": self.wallet_id,
            "address":   self.address,
            "signers":   len(self.signers),
            "required":  self.required,
            "policy":    self.policy.value,
            "timelock":  self.timelock,
        }


# ---- MultisigManagerV2
class MultisigManagerV2:
    """
    Advanced multisig wallet manager.
    Supports timelock, hierarchical, social recovery policies.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._wallets: Dict[str, MultisigWalletV2]      = {}
        self._pending: Dict[str, dict]                   = {}  # tx proposals
        self._lock     = threading.RLock()

    def create_wallet(self, signers: List[str],
                       required: int,
                       policy: MultisigPolicy = MultisigPolicy.SIMPLE,
                       timelock_blocks: int = 0) -> Tuple[bool, str]:
        with self._lock:
            if required < 1 or required > len(signers):
                return False, f"Invalid m ({required}) for {len(signers)} signers"
            wid = hashlib.sha256(
                f"MSV2:{':'.join(sorted(signers))}:{required}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._wallets[wid] = MultisigWalletV2(
                wallet_id  = wid,
                signers    = signers,
                required   = required,
                policy     = policy,
                timelock   = timelock_blocks,
                created_at = time.time(),
            )
            return True, wid

    def propose_tx(self, wallet_id: str, proposer: str,
                    recipient: str, amount: int,
                    memo: str = "") -> Tuple[bool, str]:
        with self._lock:
            wallet = self._wallets.get(wallet_id)
            if not wallet:
                return False, "Wallet not found"
            if proposer not in wallet.signers:
                return False, "Not a signer"
            pid = hashlib.sha256(
                f"MSTX:{wallet_id}:{recipient}:{amount}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._pending[pid] = {
                "proposal_id":    pid,
                "wallet_id":      wallet_id,
                "proposer":       proposer,
                "recipient":      recipient,
                "amount":         amount,
                "memo":           memo,
                "signatures":     {proposer},
                "created_at":     time.time(),
                "execute_after":  (self._bc.height + wallet.timelock
                                   if wallet.timelock else 0),
                "executed":       False,
            }
            return True, pid

    def sign_proposal(self, proposal_id: str,
                       signer: str) -> Tuple[bool, str]:
        with self._lock:
            prop   = self._pending.get(proposal_id)
            if not prop:
                return False, "Proposal not found"
            wallet = self._wallets.get(prop["wallet_id"])
            if signer not in wallet.signers:
                return False, "Not a signer"
            prop["signatures"].add(signer)
            n = len(prop["signatures"])
            r = wallet.required
            if n >= r:
                return True, f"THRESHOLD_MET ({n}/{r}) — ready to execute"
            return True, f"Signed ({n}/{r})"

    def execute_proposal(self, proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            prop   = self._pending.get(proposal_id)
            if not prop or prop["executed"]:
                return False, "Not found or already executed"
            wallet = self._wallets.get(prop["wallet_id"])
            if len(prop["signatures"]) < wallet.required:
                return False, f"Need {wallet.required} signatures"
            if (wallet.timelock > 0 and
                    self._bc.height < prop["execute_after"]):
                return False, f"Timelock: wait until block {prop['execute_after']}"
            prop["executed"] = True
            wallet.spent    += prop["amount"]
            return True, (f"Executed: {prop['amount']/10**DECIMALS:.6f} NBL → "
                          f"{prop['recipient']}")

    def wallet_info(self, wallet_id: str) -> Optional[dict]:
        w = self._wallets.get(wallet_id)
        if not w:
            return None
        bal = self._bc.utxo.balance(w.address)
        return {
            **w.to_dict(),
            "balance_nbl": f"{bal/10**DECIMALS:.6f}",
            "pending_txs": sum(
                1 for p in self._pending.values()
                if p["wallet_id"] == wallet_id and not p["executed"]
            ),
        }

    def multisig_stats(self) -> dict:
        return {
            "total_wallets":  len(self._wallets),
            "pending_tx":     sum(1 for p in self._pending.values()
                                  if not p["executed"]),
        }


# ---- SwapRoute
class SwapRoute:
    """A multi-hop swap route through DEX pools."""

    def __init__(self, path: List[str], pools: List[str]):
        self.path   = path      # [token_A, token_B, token_C]
        self.pools  = pools     # [pool_AB, pool_BC]
        self.estimated_out: int = 0
        self.price_impact: float = 0.0
        self.fees_total: int     = 0

    def to_dict(self) -> dict:
        return {
            "path":         " → ".join(self.path),
            "hops":         len(self.pools),
            "estimated_out": f"{self.estimated_out/10**DECIMALS:.6f}",
            "price_impact": f"{self.price_impact:.3f}%",
            "fees":         f"{self.fees_total/10**DECIMALS:.9f}",
        }


# ---- DeFiAggregatorV2
class DeFiAggregatorV2:
    """
    DeFi aggregator v2 — finds best swap routes across all DEX pools.
    Splits orders for minimal slippage.
    Supports any token pair via multi-hop routing.
    """

    MAX_HOPS     = 3
    SPLIT_PARTS  = 5    # split order into 5 parts for min slippage

    def __init__(self, dex: 'NEBULADex',
                  blockchain: 'NEBULABlockchain'):
        self._dex = dex
        self._bc  = blockchain
        self._swap_history: List[dict] = []

    def find_best_route(self, token_in: str, token_out: str,
                         amount_in: int) -> Optional[SwapRoute]:
        """Find best swap route (direct or multi-hop)."""
        # Try direct
        direct = self._try_route([token_in, token_out], amount_in)
        if direct:
            return direct

        # Try 2-hop via NBL
        via_nbl = self._try_route([token_in, "NBL", token_out], amount_in)
        return via_nbl

    def _try_route(self, path: List[str],
                    amount_in: int) -> Optional[SwapRoute]:
        route     = SwapRoute(path, [])
        cur_amount = amount_in
        for i in range(len(path) - 1):
            ta = path[i]
            tb = path[i+1]
            # Find pool
            pool = next(
                (p for pid, p in self._dex._pools.items()
                 if (p.token_a == ta and p.token_b == tb) or
                    (p.token_a == tb and p.token_b == ta)),
                None
            )
            if not pool:
                return None
            route.pools.append(pool.pool_id)
            fee        = cur_amount * pool.fee_bps // 10_000
            route.fees_total += fee
            net_amount = cur_amount - fee
            out = int(net_amount * 0.998)  # 0.2% slippage estimate
            cur_amount = out
        route.estimated_out = cur_amount
        return route

    def split_swap(self, token_in: str, token_out: str,
                    total_amount: int,
                    n_parts: int = None) -> Tuple[bool, int]:
        """
        Split a large swap to minimize price impact.
        Returns (success, total_out).
        """
        parts    = n_parts or self.SPLIT_PARTS
        per_part = total_amount // parts
        total_out = 0
        for i in range(parts):
            amt   = per_part if i < parts - 1 else total_amount - per_part * (parts - 1)
            route = self.find_best_route(token_in, token_out, amt)
            if route:
                total_out += route.estimated_out
        return total_out > 0, total_out

    def quote(self, token_in: str, token_out: str,
               amount_in: float) -> dict:
        """Get swap quote."""
        raw    = int(amount_in * 10**DECIMALS)
        route  = self.find_best_route(token_in, token_out, raw)
        if not route:
            return {"error": f"No route found: {token_in} → {token_out}"}
        return {
            "token_in":      token_in,
            "token_out":     token_out,
            "amount_in":     f"{amount_in:.6f}",
            "amount_out":    f"{route.estimated_out/10**DECIMALS:.6f}",
            "route":         route.to_dict(),
            "price_ratio":   f"{route.estimated_out/raw:.4f}" if raw > 0 else "0",
        }

    def swap(self, trader: str, token_in: str, token_out: str,
              amount_in: float, slippage_pct: float = 0.5) -> Tuple[bool, str]:
        """Execute a swap via aggregator."""
        raw    = int(amount_in * 10**DECIMALS)
        route  = self.find_best_route(token_in, token_out, raw)
        if not route:
            return False, f"No route for {token_in} → {token_out}"
        min_out = int(route.estimated_out * (1 - slippage_pct / 100))
        if route.estimated_out < min_out:
            return False, f"Slippage exceeded: got {route.estimated_out} < min {min_out}"
        self._swap_history.append({
            "trader":     trader,
            "token_in":   token_in,
            "token_out":  token_out,
            "amount_in":  raw,
            "amount_out": route.estimated_out,
            "timestamp":  time.time(),
        })
        return True, (f"Swapped {amount_in} {token_in} → "
                      f"{route.estimated_out/10**DECIMALS:.6f} {token_out} "
                      f"via {' → '.join(route.path)}")

    def aggregator_stats(self) -> dict:
        total_vol = sum(s["amount_in"] for s in self._swap_history)
        return {
            "total_swaps": len(self._swap_history),
            "total_volume_nbl": f"{total_vol/10**DECIMALS:.3f}",
        }


# ---- BlockExplorerBackend
class BlockExplorerBackend:
    """
    Block explorer backend for NEBULA.
    Powers web-based block explorers.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  tx_index: 'TransactionIndex' = None,
                  analytics: 'ChainAnalytics'  = None):
        self._bc        = blockchain
        self._tx_index  = tx_index
        self._analytics = analytics

    def get_block(self, height_or_hash: str) -> Optional[dict]:
        """Get block info by height or hash."""
        try:
            height = int(height_or_hash)
            blk    = self._bc.get_block(height)
        except ValueError:
            blk = self._bc.get_block_by_hash(height_or_hash)
        if not blk:
            return None
        return {
            "height":     blk.height,
            "hash":       blk.hash,
            "prev_hash":  blk.header.prev_hash,
            "timestamp":  blk.header.timestamp,
            "tx_count":   blk.tx_count,
            "size_bytes": blk.byte_size(),
            "miner":      blk.transactions[0].outputs[0].address
                          if blk.transactions else "",
            "reward":     f"{mining_reward(blk.height)/10**DECIMALS:.9f}",
            "difficulty": blk.header.bits,
            "merkle_root": blk.header.merkle_root,
        }

    def get_transaction(self, txid: str) -> Optional[dict]:
        """Get transaction info by txid."""
        bc  = self._bc
        tx  = bc.mempool._txs.get(txid)
        if tx:
            return {
                **tx.to_dict(),
                "confirmations": 0,
                "in_mempool":    True,
            }
        if self._tx_index:
            loc = self._tx_index.get_tx_location(txid)
            if loc:
                height, pos = loc
                blk = bc.get_block(height)
                if blk and pos < len(blk.transactions):
                    tx = blk.transactions[pos]
                    return {
                        **tx.to_dict(),
                        "block_height":  height,
                        "block_hash":    blk.hash,
                        "confirmations": bc.height - height + 1,
                        "in_mempool":    False,
                    }
        return None

    def get_address(self, address: str) -> dict:
        """Get address info."""
        balance = self._bc.utxo.balance(address)
        utxos   = self._bc.utxo.get_by_address(address)  # FIX
        tx_ids  = []
        if self._tx_index:
            tx_ids = self._tx_index.get_address_txids(address)
        return {
            "address":       address,
            "balance_nbl":   f"{balance/10**DECIMALS:.9f}",
            "utxo_count":    len(utxos),
            "tx_count":      len(tx_ids),
            "recent_txids":  tx_ids[-10:],
        }

    def latest_blocks(self, n: int = 10) -> List[dict]:
        blocks = []
        for h in range(max(0, self._bc.height - n + 1), self._bc.height + 1):
            blk = self._bc.get_block(h)
            if blk:
                blocks.append({
                    "height":    blk.height,
                    "hash":      blk.hash[:16] + "...",
                    "tx_count":  blk.tx_count,
                    "timestamp": blk.header.timestamp,
                    "size":      blk.byte_size(),
                })
        blocks.reverse()
        return blocks

    def mempool_snapshot(self) -> dict:
        txs = []
        for txid, tx in list(self._bc.mempool._txs.items())[:20]:
            txs.append({
                "txid":    txid[:16] + "...",
                "size":    tx.byte_size(),
                "fee":     tx.fee(self._bc.utxo),
                "inputs":  len(tx.inputs),
                "outputs": len(tx.outputs),
            })
        return {
            "mempool_count": self._bc.mempool.size(),
            "transactions":  txs,
        }

    def search(self, query: str) -> dict:
        """Search by block height, txid, or address."""
        query = query.strip()
        # Try block height
        try:
            h = int(query)
            blk = self.get_block(str(h))
            if blk:
                return {"type": "block", "data": blk}
        except ValueError:
            _NB_SWALLOW_LOG.debug("swallowed ValueError in BlockExplorerBackend.search", exc_info=True)
        # Try txid
        if len(query) == 64:
            tx = self.get_transaction(query)
            if tx:
                return {"type": "transaction", "data": tx}
            blk = self.get_block(query)
            if blk:
                return {"type": "block", "data": blk}
        # Try address
        addr_info = self.get_address(query)
        if addr_info["utxo_count"] > 0 or addr_info["tx_count"] > 0:
            return {"type": "address", "data": addr_info}
        return {"type": "not_found", "query": query}

    def explorer_stats(self) -> dict:
        bc = self._bc
        tip = bc.tip
        return {
            "chain_height":  bc.height,
            "best_block":    tip.hash,
            "total_supply":  f"{bc.utxo.total_supply()/10**DECIMALS:.3f} NBL",
            "mempool_txs":   bc.mempool.size(),
            "utxo_set":      bc.utxo.size(),
            "avg_block_time": f"{TARGET_BLOCK_TIME}s target",
        }


# ---- NFTAuctionType
class NFTAuctionType(_enum.Enum):
    FIXED_PRICE  = "fixed_price"
    ENGLISH      = "english_auction"
    DUTCH        = "dutch_auction"
    SEALED_BID   = "sealed_bid"


# ---- NFTListing
@dataclass
class NFTListing:
    listing_id:   str
    collection_id: str
    token_id:     int
    seller:       str
    auction_type: NFTAuctionType
    start_price:  int
    reserve:      int = 0
    end_block:    int = 0
    highest_bid:  int = 0
    highest_bidder: str = ""
    bids:         List[dict] = field(default_factory=list)
    sold:         bool = False
    dutch_end_price: int = 0
    dutch_blocks:    int = 0

    def current_dutch_price(self, current_block: int,
                             start_block: int) -> int:
        if self.auction_type != NFTAuctionType.DUTCH:
            return self.start_price
        elapsed  = current_block - start_block
        total    = self.dutch_blocks or 1
        pct      = min(elapsed / total, 1.0)
        discount = int((self.start_price - self.dutch_end_price) * pct)
        return max(self.start_price - discount, self.dutch_end_price)

    def to_dict(self) -> dict:
        return {
            "listing_id":    self.listing_id,
            "collection":    self.collection_id,
            "token":         self.token_id,
            "seller":        self.seller,
            "auction_type":  self.auction_type.value,
            "start_price":   f"{self.start_price/10**DECIMALS:.3f} NBL",
            "highest_bid":   f"{self.highest_bid/10**DECIMALS:.3f} NBL",
            "bids":          len(self.bids),
            "sold":          self.sold,
        }
