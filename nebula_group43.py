"""NEBULA group43 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. TraderProfile  (orig. lines 70341-70369)
   2. SocialTradingPlatform  (orig. lines 70371-70437)
   3. GrantDAO  (orig. lines 70444-70526)
   4. TokenLocker  (orig. lines 70533-70583)
   5. TriggerCondition  (orig. lines 70594-70600)
   6. AutomatedAction  (orig. lines 70602-70622)
   7. DeFiAutomation  (orig. lines 70624-70703)
   8. NFTCollectionAnalytics  (orig. lines 70710-70771)
   9. SwapRouter  (orig. lines 70778-70850)
  10. ProtocolFeeDistributor  (orig. lines 70857-70907)
  11. DataAvailabilityLayer  (orig. lines 70914-70965)
  12. Layer2Bridge  (orig. lines 70972-71055)
  13. UpgradeStatus  (orig. lines 71067-71072)
  14. ProtocolUpgradeManager  (orig. lines 71074-71146)
  15. EmergencyDAO  (orig. lines 71153-71240)
  16. ChainConfig  (orig. lines 71247-71256)
  17. MultiChainWallet  (orig. lines 71258-71300)
  18. MobileSDK  (orig. lines 71307-71512)
  19. PositionType  (orig. lines 71519-71527)
  20. DeFiPosition  (orig. lines 71529-71551)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BIP39, HDKey, L2Type, NEBULABlockchain, NEBULAWallet, ProtocolUpgrade, Script, Secp256k1, TxBuilder
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

def sha256d(data: bytes) -> bytes:
    """Double SHA-256 — used everywhere in Bitcoin/NEBULA"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

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

log = logging.getLogger("nebula.api")

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

def _v108_upg_post(o):
    o.name = o.title

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- TraderProfile
class TraderProfile:
    """Public trading profile for copy trading."""

    def __init__(self, address: str, display_name: str):
        self.address      = address
        self.display_name = display_name
        self.followers:   Set[str]    = set()
        self.trades:      List[dict]  = []
        self.win_rate:    float       = 0.0
        self.total_pnl:   float       = 0.0
        self.aum:         float       = 0.0    # assets under management

    def add_trade(self, trade: dict):
        self.trades.append(trade)
        wins  = sum(1 for t in self.trades if t.get("pnl", 0) > 0)
        total = len(self.trades)
        self.win_rate  = wins / total if total > 0 else 0
        self.total_pnl = sum(t.get("pnl", 0) for t in self.trades)

    def to_dict(self) -> dict:
        return {
            "address":      self.address,
            "name":         self.display_name,
            "followers":    len(self.followers),
            "trades":       len(self.trades),
            "win_rate":     f"{self.win_rate*100:.1f}%",
            "total_pnl":    f"{self.total_pnl:.4f}",
            "aum":          f"{self.aum:.3f} NBL",
        }


# ---- SocialTradingPlatform
class SocialTradingPlatform:
    """
    Social trading platform for NEBULA.
    Follow top traders and auto-copy their positions.
    """

    COPY_FEE_PCT = 0.05   # 5% of profits to copied trader

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._traders:  Dict[str, TraderProfile] = {}
        self._copies:   Dict[str, str]           = {}   # follower -> trader
        self._lock      = threading.RLock()

    def create_profile(self, address: str,
                        name: str) -> bool:
        with self._lock:
            if address in self._traders:
                return False
            self._traders[address] = TraderProfile(address, name)
            return True

    def follow(self, follower: str,
                trader: str) -> Tuple[bool, str]:
        with self._lock:
            prof = self._traders.get(trader)
            if not prof:
                return False, "Trader not found"
            prof.followers.add(follower)
            return True, f"Following {prof.display_name}"

    def copy_trade(self, follower: str,
                    trader: str) -> Tuple[bool, str]:
        with self._lock:
            if follower not in self._traders.get(trader, TraderProfile("", "")).followers:
                return False, "Must follow trader first"
            self._copies[follower] = trader
            prof = self._traders.get(trader)
            if prof:
                prof.aum += self._bc.utxo.balance(follower) / 10**DECIMALS * 0.1
            return True, f"Now copying {self._traders[trader].display_name}"

    def stop_copy(self, follower: str) -> bool:
        return self._copies.pop(follower, None) is not None

    def record_trade(self, trader: str, trade_data: dict):
        with self._lock:
            prof = self._traders.get(trader)
            if prof:
                prof.add_trade(trade_data)

    def leaderboard(self, n: int = 10) -> List[dict]:
        traders = sorted(
            self._traders.values(),
            key=lambda t: t.total_pnl,
            reverse=True
        )
        return [t.to_dict() for t in traders[:n]]

    def social_trading_stats(self) -> dict:
        with self._lock:
            total_aum = sum(t.aum for t in self._traders.values())
        return {
            "traders":    len(self._traders),
            "copy_pairs": len(self._copies),
            "total_aum":  f"{total_aum:.3f} NBL",
        }


# ---- GrantDAO
class GrantDAO:
    """
    Community grant DAO for funding NEBULA ecosystem projects.
    Small grants funded by community, large grants by treasury.
    """

    MICRO_GRANT_MAX  = 500.0    # NBL
    SMALL_GRANT_MAX  = 5_000.0
    LARGE_GRANT_MAX  = 50_000.0

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._grants: List[dict] = []
        self._pot:    int = 0
        self._lock    = threading.RLock()

    def contribute_to_pot(self, contributor: str,
                           amount_nbl: float) -> bool:
        with self._lock:
            amount = int(amount_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(contributor) < amount:
                return False
            self._pot += amount
            return True

    def apply(self, applicant: str, title: str,
               amount_nbl: float, category: str,
               description: str) -> str:
        with self._lock:
            gid = hashlib.sha256(
                f"GDAO:{applicant}:{title}:{time.time()}".encode()
            ).hexdigest()[:12]
            tier = (
                "micro"  if amount_nbl <= self.MICRO_GRANT_MAX else
                "small"  if amount_nbl <= self.SMALL_GRANT_MAX else
                "large"
            )
            self._grants.append({
                "id":          gid,
                "applicant":   applicant,
                "title":       title,
                "amount":      amount_nbl,
                "category":    category,
                "description": description,
                "tier":        tier,
                "votes":       0,
                "status":      "voting",
                "created_at":  time.time(),
            })
            return gid

    def vote(self, grant_id: str, voter: str,
              support: bool) -> bool:
        with self._lock:
            grant = next((g for g in self._grants if g["id"] == grant_id), None)
            if not grant:
                return False
            weight = self._bc.utxo.balance(voter) / 10**DECIMALS
            grant["votes"] += weight if support else -weight
            return True

    def distribute_grants(self) -> List[dict]:
        distributed = []
        with self._lock:
            for grant in self._grants:
                if grant["status"] != "voting":
                    continue
                if grant["votes"] > 100:
                    amount = int(grant["amount"] * 10**DECIMALS)
                    if amount <= self._pot:
                        self._pot -= amount
                        grant["status"] = "funded"
                        distributed.append(grant)
        return distributed

    def dao_stats(self) -> dict:
        with self._lock:
            funded = sum(1 for g in self._grants if g["status"] == "funded")
        return {
            "pot_nbl":       f"{self._pot/10**DECIMALS:.3f}",
            "total_grants":  len(self._grants),
            "funded":        funded,
        }


# ---- TokenLocker
class TokenLocker:
    """Lock tokens for a period — used for project commitments."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._locks: Dict[str, dict] = {}
        self._lock   = threading.RLock()

    def lock_tokens(self, owner: str, amount_nbl: float,
                     unlock_date_days: int,
                     reason: str = "") -> str:
        with self._lock:
            lid = hashlib.sha256(
                f"LOCK:{owner}:{amount_nbl}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._locks[lid] = {
                "lock_id":      lid,
                "owner":        owner,
                "amount":       int(amount_nbl * 10**DECIMALS),
                "unlock_block": self._bc.height + unlock_date_days * 144,
                "reason":       reason,
                "unlocked":     False,
            }
            return lid

    def unlock(self, lock_id: str, owner: str) -> Tuple[bool, int]:
        with self._lock:
            lock = self._locks.get(lock_id)
            if not lock or lock["owner"] != owner:
                return False, 0
            if lock["unlocked"]:
                return False, 0
            if self._bc.height < lock["unlock_block"]:
                remaining = lock["unlock_block"] - self._bc.height
                return False, -remaining
            lock["unlocked"] = True
            return True, lock["amount"]

    def active_locks(self, owner: str = None) -> List[dict]:
        locks = [l for l in self._locks.values() if not l["unlocked"]]
        if owner:
            locks = [l for l in locks if l["owner"] == owner]
        return locks

    def locker_stats(self) -> dict:
        active = [l for l in self._locks.values() if not l["unlocked"]]
        total  = sum(l["amount"] for l in active)
        return {
            "active_locks":    len(active),
            "total_locked_nbl": f"{total/10**DECIMALS:.3f}",
        }


# ---- TriggerCondition
class TriggerCondition(_enum.Enum):
    PRICE_ABOVE   = "price_above"
    PRICE_BELOW   = "price_below"
    BALANCE_BELOW = "balance_below"
    TIME_ELAPSED  = "time_elapsed"
    BLOCK_REACHED = "block_reached"
    HEALTH_BELOW  = "health_below"


# ---- AutomatedAction
@dataclass
class AutomatedAction:
    action_id:   str
    owner:       str
    trigger:     TriggerCondition
    threshold:   float
    action_type: str    # "swap", "repay", "add_collateral", "harvest"
    action_data: dict
    active:      bool = True
    executions:  int  = 0

    def to_dict(self) -> dict:
        return {
            "id":         self.action_id,
            "owner":      self.owner,
            "trigger":    self.trigger.value,
            "threshold":  self.threshold,
            "action":     self.action_type,
            "active":     self.active,
            "executions": self.executions,
        }


# ---- DeFiAutomation
class DeFiAutomation:
    """
    Automated DeFi actions triggered by on-chain conditions.
    Stop-loss, take-profit, auto-compound, auto-repay.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._actions: Dict[str, AutomatedAction] = {}
        self._lock    = threading.RLock()

    def register_action(self, owner: str,
                          trigger: TriggerCondition,
                          threshold: float,
                          action_type: str,
                          action_data: dict) -> str:
        with self._lock:
            aid = hashlib.sha256(
                f"AUTO:{owner}:{trigger.value}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._actions[aid] = AutomatedAction(
                action_id   = aid,
                owner       = owner,
                trigger     = trigger,
                threshold   = threshold,
                action_type = action_type,
                action_data = action_data,
            )
            return aid

    def check_and_execute(self) -> List[str]:
        """Check all conditions and execute triggered actions."""
        triggered = []
        with self._lock:
            for aid, action in list(self._actions.items()):
                if not action.active:
                    continue
                if self._is_triggered(action):
                    self._execute_action(action)
                    triggered.append(aid)
        return triggered

    def _is_triggered(self, action: AutomatedAction) -> bool:
        t = action.trigger
        if t == TriggerCondition.PRICE_ABOVE:
            price = (self._oracle.price("NBL/USD")
                     if self._oracle else 0) or 0
            return price >= action.threshold
        elif t == TriggerCondition.PRICE_BELOW:
            price = (self._oracle.price("NBL/USD")
                     if self._oracle else 0) or 0
            return price <= action.threshold
        elif t == TriggerCondition.BALANCE_BELOW:
            bal = self._bc.utxo.balance(action.owner) / 10**DECIMALS
            return bal <= action.threshold
        elif t == TriggerCondition.BLOCK_REACHED:
            return self._bc.height >= action.threshold
        return False

    def _execute_action(self, action: AutomatedAction):
        action.executions += 1

    def cancel_action(self, action_id: str, owner: str) -> bool:
        with self._lock:
            a = self._actions.get(action_id)
            if a and a.owner == owner:
                a.active = False
                return True
            return False

    def automation_stats(self) -> dict:
        with self._lock:
            active = sum(1 for a in self._actions.values() if a.active)
        return {
            "total_actions": len(self._actions),
            "active":        active,
            "types":         [t.value for t in TriggerCondition],
        }


# ---- NFTCollectionAnalytics
class NFTCollectionAnalytics:
    """Analytics for NFT collections on NEBULA."""

    def __init__(self, registry: 'NBL721Registry'):
        self._registry = registry

    def floor_price(self, collection_id: str) -> Optional[float]:
        if not hasattr(self._registry, '_marketplace_listings'):
            return None
        listings = [
            l for l in getattr(self._registry, '_marketplace_listings', {}).values()
            if l.get("collection_id") == collection_id and not l.get("sold")
        ]
        if not listings:
            return None
        prices = [l.get("price", float('inf')) for l in listings]
        return min(prices)

    def rarity_scores(self, collection_id: str) -> Dict[int, float]:
        col = self._registry._collections.get(collection_id)
        if not col:
            return {}
        tokens = col.get("tokens", {})
        # Count trait frequencies
        trait_counts: Dict[str, Dict[str, int]] = {}
        for token_id, meta in tokens.items():
            attrs = meta.get("metadata", {}).get("attributes", [])
            if isinstance(attrs, list):
                for attr in attrs:
                    key = attr.get("trait_type", "")
                    val = str(attr.get("value", ""))
                    if key not in trait_counts:
                        trait_counts[key] = {}
                    trait_counts[key][val] = trait_counts[key].get(val, 0) + 1
        # Score = sum of -log(frequency)
        n      = len(tokens)
        scores = {}
        for token_id, meta in tokens.items():
            score = 0.0
            attrs = meta.get("metadata", {}).get("attributes", [])
            if isinstance(attrs, list):
                for attr in attrs:
                    key  = attr.get("trait_type", "")
                    val  = str(attr.get("value", ""))
                    freq = trait_counts.get(key, {}).get(val, 1)
                    score += n / freq
            scores[int(token_id)] = score
        return scores

    def collection_stats(self, collection_id: str) -> dict:
        col = self._registry._collections.get(collection_id)
        if not col:
            return {}
        tokens = col.get("tokens", {})
        owners = set(meta.get("owner") for meta in tokens.values())
        return {
            "collection_id": collection_id,
            "name":          col.get("name", ""),
            "total_tokens":  len(tokens),
            "unique_owners": len(owners),
            "floor_price":   self.floor_price(collection_id),
        }


# ---- SwapRouter
class SwapRouter:
    """
    Universal swap router for NEBULA DEX ecosystem.
    Routes through AMM pools, order books, and aggregators.
    """

    def __init__(self, dex: 'NEBULADex',
                  order_book_mgr: 'OrderBookManager' = None,
                  aggregator: 'DeFiAggregatorV2' = None):
        self._dex    = dex
        self._ob     = order_book_mgr
        self._agg    = aggregator
        self._routes_used: Dict[str, int] = {}

    def best_execution(self, token_in: str, token_out: str,
                        amount_in: float) -> dict:
        """Find best execution path for a swap."""
        options = []
        # AMM quote
        amm_out = self._dex.quote_amm(token_in, token_out,
                                       int(amount_in * 10**DECIMALS))
        if amm_out > 0:
            options.append({
                "venue": "AMM",
                "out":   amm_out,
                "path":  f"{token_in} → {token_out} (AMM)",
            })
        # Aggregator quote
        if self._agg:
            q = self._agg.quote(token_in, token_out, amount_in)
            if "error" not in q:
                out = float(q.get("amount_out", "0"))
                options.append({
                    "venue": "Aggregator",
                    "out":   int(out * 10**DECIMALS),
                    "path":  q.get("route", {}).get("path", ""),
                })
        if not options:
            return {"error": "No liquidity found"}
        best = max(options, key=lambda o: o["out"])
        return {
            "token_in":   token_in,
            "token_out":  token_out,
            "amount_in":  amount_in,
            "best_venue": best["venue"],
            "amount_out": f"{best['out']/10**DECIMALS:.6f}",
            "path":       best["path"],
            "all_quotes": options,
        }

    def execute_swap(self, trader: str, token_in: str,
                      token_out: str, amount_in: float,
                      min_out: float = 0) -> Tuple[bool, str]:
        """Execute swap via best route."""
        result = self.best_execution(token_in, token_out, amount_in)
        if "error" in result:
            return False, result["error"]
        venue = result["best_venue"]
        self._routes_used[venue] = self._routes_used.get(venue, 0) + 1
        if venue == "AMM":
            ok, msg, out = self._dex.swap_amm(
                trader, token_in, token_out,
                int(amount_in * 10**DECIMALS))
            return ok, msg
        elif self._agg and venue == "Aggregator":
            return self._agg.swap(trader, token_in, token_out, amount_in)
        return False, "No venue available"

    def router_stats(self) -> dict:
        return {
            "routes_used": self._routes_used,
            "total_swaps": sum(self._routes_used.values()),
        }


# ---- ProtocolFeeDistributor
class ProtocolFeeDistributor:
    """
    Distributes protocol fees to stakeholders:
    - veNBL holders get buy-back and burn
    - Treasury gets development fund
    - LPs get fee boost
    """

    DISTRIBUTION = {
        "venbl_holders":  0.40,
        "treasury":       0.30,
        "lp_boost":       0.20,
        "burn":           0.10,
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  venbl: 'VoteEscrowedNBL' = None,
                  treasury: 'NEBULATreasury' = None):
        self._bc      = blockchain
        self._venbl   = venbl
        self._treasury = treasury
        self._accumulated: int = 0
        self._distributed: Dict[str, int] = {k: 0 for k in self.DISTRIBUTION}
        self._lock    = threading.RLock()

    def accumulate_fees(self, amount: int):
        with self._lock:
            self._accumulated += amount

    def distribute(self) -> dict:
        with self._lock:
            if self._accumulated == 0:
                return {"distributed": 0}
            total  = self._accumulated
            result = {}
            for dest, pct in self.DISTRIBUTION.items():
                share = int(total * pct)
                self._distributed[dest] += share
                result[dest] = f"{share/10**DECIMALS:.6f} NBL"
            self._accumulated = 0
            return {"distributed": f"{total/10**DECIMALS:.6f} NBL", "breakdown": result}

    def fee_stats(self) -> dict:
        with self._lock:
            total_dist = sum(self._distributed.values())
        return {
            "accumulated":  f"{self._accumulated/10**DECIMALS:.6f} NBL",
            "total_distributed": f"{total_dist/10**DECIMALS:.6f}",
            "breakdown":    {k: f"{v/10**DECIMALS:.6f}"
                             for k, v in self._distributed.items()},
        }


# ---- DataAvailabilityLayer
class DataAvailabilityLayer:
    """
    Data availability (DA) layer for NEBULA Layer-2 solutions.
    Ensures transaction data is available for fraud proofs.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  ipfs: 'IPFSClient' = None):
        self._bc    = blockchain
        self._ipfs  = ipfs
        self._da_headers: Dict[int, dict] = {}   # block -> DA header
        self._blobs: Dict[str, bytes]     = {}   # blob_id -> data
        self._lock  = threading.RLock()

    def submit_blob(self, submitter: str,
                     data: bytes,
                     namespace: str = "default") -> str:
        with self._lock:
            blob_id = hashlib.sha256(data).hexdigest()
            self._blobs[blob_id] = data
            if self._ipfs:
                self._ipfs.add(data, f"blob_{blob_id[:8]}")
            return blob_id

    def get_blob(self, blob_id: str) -> Optional[bytes]:
        return self._blobs.get(blob_id)

    def verify_blob_availability(self, blob_id: str) -> bool:
        return blob_id in self._blobs

    def post_da_header(self, block_height: int,
                        blob_ids: List[str]) -> str:
        with self._lock:
            header = {
                "height":   block_height,
                "blobs":    blob_ids,
                "root":     hashlib.sha256(
                    b"".join(b.encode() for b in blob_ids)
                ).hexdigest(),
                "posted_at": time.time(),
            }
            self._da_headers[block_height] = header
            return header["root"]

    def da_stats(self) -> dict:
        with self._lock:
            total_size = sum(len(b) for b in self._blobs.values())
        return {
            "total_blobs":   len(self._blobs),
            "total_size_kb": f"{total_size/1024:.1f}",
            "da_headers":    len(self._da_headers),
        }


# ---- Layer2Bridge
class Layer2Bridge:
    """
    Bridge between NEBULA L1 and Layer-2 solutions.
    Supports optimistic rollups and ZK rollups.
    """

    class L2Type(_enum.Enum):
        OPTIMISTIC = "optimistic"
        ZK_ROLLUP  = "zk_rollup"
        VALIDIUM   = "validium"

    CHALLENGE_PERIOD_BLOCKS = 1000   # 7 days for optimistic

    def __init__(self, l2_name: str, l2_type: L2Type,
                  blockchain: 'NEBULABlockchain'):
        self.l2_name     = l2_name
        self.l2_type     = l2_type
        self._bc         = blockchain
        self._deposits:  Dict[str, int]  = {}
        self._withdrawals: Dict[str, dict] = {}
        self._state_roots: Dict[int, str] = {}
        self._lock       = threading.RLock()

    def deposit_to_l2(self, address: str,
                       amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            amount = int(amount_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(address) < amount:
                return False, "Insufficient balance"
            self._deposits[address] = self._deposits.get(address, 0) + amount
            tx_hash = hashlib.sha256(
                f"L2DEP:{address}:{amount}:{time.time()}".encode()
            ).hexdigest()[:16]
            return True, f"Deposited to {self.l2_name}: tx {tx_hash}"

    def initiate_withdrawal(self, address: str,
                             amount_nbl: float,
                             l2_proof: str = "") -> Tuple[bool, str]:
        with self._lock:
            amount  = int(amount_nbl * 10**DECIMALS)
            wid     = hashlib.sha256(
                f"L2WD:{address}:{amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            finalize = self._bc.height + (
                self.CHALLENGE_PERIOD_BLOCKS
                if self.l2_type == self.L2Type.OPTIMISTIC else 0)
            self._withdrawals[wid] = {
                "wid":      wid,
                "address":  address,
                "amount":   amount,
                "status":   "pending",
                "finalize_block": finalize,
                "proof":    l2_proof,
            }
            return True, wid

    def finalize_withdrawal(self, wid: str) -> Tuple[bool, int]:
        with self._lock:
            w = self._withdrawals.get(wid)
            if not w or w["status"] != "pending":
                return False, 0
            if self._bc.height < w["finalize_block"]:
                remaining = w["finalize_block"] - self._bc.height
                return False, -remaining
            w["status"] = "finalized"
            return True, w["amount"]

    def post_state_root(self, block_number: int,
                         state_root: str):
        with self._lock:
            self._state_roots[block_number] = state_root

    def l2_stats(self) -> dict:
        with self._lock:
            total_dep = sum(self._deposits.values())
            pending_w = sum(1 for w in self._withdrawals.values()
                            if w["status"] == "pending")
        return {
            "l2_name":      self.l2_name,
            "l2_type":      self.l2_type.value,
            "total_deposited": f"{total_dep/10**DECIMALS:.3f} NBL",
            "pending_withdrawals": pending_w,
            "state_roots":  len(self._state_roots),
        }


# ---- UpgradeStatus
class UpgradeStatus(_enum.Enum):
    PROPOSED  = "proposed"
    SIGNALING = "signaling"
    LOCKED_IN = "locked_in"
    ACTIVE    = "active"
    FAILED    = "failed"


# ---- ProtocolUpgradeManager
@dataclass
class ProtocolUpgradeManager:
    """
    Manages protocol upgrades via miner signaling.
    Uses BIP 9-style soft fork activation.
    """

    SIGNAL_THRESHOLD = 0.90    # 90% of miners must signal
    SIGNAL_WINDOW    = 2016    # 2 weeks of blocks
    MIN_ACTIVATION_DELAY = 1008  # 1 week delay after lock-in

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._upgrades: Dict[str, ProtocolUpgrade] = {}
        self._miner_signals: Dict[str, Set[str]]   = {}
        self._lock     = threading.RLock()

    def propose_upgrade(self, proposer: str, name: str,
                         description: str, version: str,
                         bip: str) -> str:
        with self._lock:
            uid = hashlib.sha256(
                f"UPGRADE:{name}:{version}:{time.time()}".encode()
            ).hexdigest()[:12]
            activation = self._bc.height + self.SIGNAL_WINDOW + self.MIN_ACTIVATION_DELAY
            self._upgrades[uid] = ProtocolUpgradeC(
                upgrade_id       = uid,
                name             = name,
                description      = description,
                version          = version,
                activation_block = activation,
                bip              = bip,
                status           = UpgradeStatus.SIGNALING,
                created_at       = time.time(),
            )
            self._miner_signals[uid] = set()
            return uid

    def signal_readiness(self, miner: str,
                          upgrade_id: str) -> Tuple[bool, str]:
        with self._lock:
            upgrade = self._upgrades.get(upgrade_id)
            if not upgrade or upgrade.status != UpgradeStatus.SIGNALING:
                return False, "Not in signaling phase"
            self._miner_signals[upgrade_id].add(miner)
            signals = len(self._miner_signals[upgrade_id])
            pct     = signals / max(1, self._bc.height % self.SIGNAL_WINDOW) * 100
            if pct >= self.SIGNAL_THRESHOLD * 100:
                upgrade.status = UpgradeStatus.LOCKED_IN
                return True, f"LOCKED IN — activates block {upgrade.activation_block}"
            return True, f"Signal recorded ({signals} miners)"

    def check_activations(self) -> List[str]:
        activated = []
        with self._lock:
            cur = self._bc.height
            for uid, upgrade in self._upgrades.items():
                if (upgrade.status == UpgradeStatus.LOCKED_IN and
                        cur >= upgrade.activation_block):
                    upgrade.status = UpgradeStatus.ACTIVE
                    activated.append(uid)
        return activated

    def upgrade_stats(self) -> dict:
        with self._lock:
            by_status = {}
            for u in self._upgrades.values():
                s = u.status.value
                by_status[s] = by_status.get(s, 0) + 1
        return {
            "total_upgrades": len(self._upgrades),
            "by_status":      by_status,
        }


# ---- EmergencyDAO
class EmergencyDAO:
    """
    Emergency DAO for rapid response to protocol threats.
    Fast governance with 24-hour voting period.
    """

    VOTE_PERIOD_BLOCKS = 144    # ~24 hours
    QUORUM_PCT         = 0.05   # 5% quorum required
    THRESHOLD          = 0.75   # 75% yes to pass

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._proposals:  List[dict] = []
        self._lock        = threading.RLock()

    def emergency_propose(self, proposer: str,
                           title: str, action: str,
                           params: dict = None) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"EDAO:{proposer}:{title}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._proposals.append({
                "id":          pid,
                "proposer":    proposer,
                "title":       title,
                "action":      action,
                "params":      params or {},
                "votes_yes":   0.0,
                "votes_no":    0.0,
                "voters":      set(),
                "created_at":  self._bc.height,
                "expires_at":  self._bc.height + self.VOTE_PERIOD_BLOCKS,
                "executed":    False,
                "status":      "active",
            })
            return pid

    def vote(self, voter: str, proposal_id: str,
              yes: bool) -> Tuple[bool, str]:
        with self._lock:
            prop = next((p for p in self._proposals if p["id"] == proposal_id), None)
            if not prop or prop["status"] != "active":
                return False, "Not found or not active"
            if self._bc.height > prop["expires_at"]:
                prop["status"] = "expired"
                return False, "Voting period ended"
            if voter in prop["voters"]:
                return False, "Already voted"
            weight = self._bc.utxo.balance(voter) / 10**DECIMALS
            if yes:
                prop["votes_yes"] += weight
            else:
                prop["votes_no"]  += weight
            prop["voters"].add(voter)
            return True, "Vote recorded"

    def try_execute(self, proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            prop = next((p for p in self._proposals if p["id"] == proposal_id), None)
            if not prop:
                return False, "Not found"
            if prop["executed"]:
                return False, "Already executed"
            total = prop["votes_yes"] + prop["votes_no"]
            if total == 0:
                return False, "No votes"
            pct = prop["votes_yes"] / total
            if pct < self.THRESHOLD:
                prop["status"] = "failed"
                return False, f"Failed: {pct*100:.1f}% yes (need {self.THRESHOLD*100:.0f}%)"
            prop["executed"] = True
            prop["status"]   = "executed"
            return True, f"Emergency action executed: {prop['action']}"

    def active_proposals(self) -> List[dict]:
        cur = self._bc.height
        return [
            {
                "id":       p["id"],
                "title":    p["title"],
                "votes_yes": p["votes_yes"],
                "votes_no":  p["votes_no"],
                "expires_in": p["expires_at"] - cur,
            }
            for p in self._proposals
            if p["status"] == "active"
        ]


# ---- ChainConfig
class ChainConfig:
    """Configuration for a supported chain."""

    CHAINS = {
        "nebula":   {"chain_id": 2025, "native": "NBL",  "decimals": 9},
        "ethereum": {"chain_id": 1,    "native": "ETH",  "decimals": 18},
        "bitcoin":  {"chain_id": 0,    "native": "BTC",  "decimals": 8},
        "bnb_chain":{"chain_id": 56,   "native": "BNB",  "decimals": 18},
        "polygon":  {"chain_id": 137,  "native": "MATIC","decimals": 18},
    }


# ---- MultiChainWallet
class MultiChainWallet:
    """
    Multi-chain HD wallet supporting NEBULA and other chains.
    Single seed phrase, multiple chains.
    """

    COIN_TYPES = {
        "nebula":   2025,
        "bitcoin":  0,
        "ethereum": 60,
        "bnb_chain": 714,
        "polygon":  60,
    }

    def __init__(self, mnemonic: str = None):
        self.mnemonic = mnemonic or BIP39.generate_mnemonic()
        self._seed    = BIP39.mnemonic_to_seed(self.mnemonic)
        self._master  = HDKey.from_seed(self._seed)
        self._addresses: Dict[str, Dict[int, str]] = {}

    def get_address(self, chain: str, index: int = 0) -> str:
        coin_type = self.COIN_TYPES.get(chain, 60)
        path      = f"m/44'/{coin_type}'/0'/0/{index}"
        key       = self._master.derive_path(path)
        if chain not in self._addresses:
            self._addresses[chain] = {}
        self._addresses[chain][index] = key.address
        return key.address

    def get_all_addresses(self,
                           n_per_chain: int = 3) -> Dict[str, List[str]]:
        result = {}
        for chain in self.COIN_TYPES:
            result[chain] = [self.get_address(chain, i)
                              for i in range(n_per_chain)]
        return result

    def wallet_summary(self) -> dict:
        return {
            "chains_supported":  list(self.COIN_TYPES.keys()),
            "mnemonic_words":    len(self.mnemonic.split()),
            "derivation_standard": "BIP-44",
        }


# ---- MobileSDK
class MobileSDK:
    """
    NEBULA Mobile SDK — simplified API for mobile apps.
    Handles wallet operations, transactions, DeFi.
    """

    def __init__(self, blockchain: 'NEBULABlockchain' = None,
                  network: str = "mainnet"):
        self._bc      = blockchain or NEBULABlockchain()
        self.network  = network
        self._wallet: Optional[NEBULAWallet] = None
        self._cache:  Dict[str, Any] = {}

    def create_wallet(self) -> dict:
        """Create a new wallet."""
        self._wallet = NEBULAWallet.generate()
        return {
            "address":  self._wallet.first_address,
            "mnemonic": self._wallet.mnemonic,
            "warning":  "Save your mnemonic phrase securely!",
        }

    def import_wallet(self, mnemonic: str) -> dict:
        """Import wallet from mnemonic."""
        try:
            self._wallet = NEBULAWallet(mnemonic)
            return {"address": self._wallet.first_address, "ok": True}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def get_balance(self, address: str = None) -> dict:
        addr = address or (self._wallet.first_address if self._wallet else "")
        bal  = self._bc.utxo.balance(addr)
        return {
            "address": addr,
            "balance": f"{bal/10**DECIMALS:.9f}",
            "raw":     bal,
        }

    def send(self, to: str, amount_nbl: float,
              memo: str = "") -> dict:
        """
        Build, sign and submit a real P2PKH transaction.
        Uses TxBuilder → UTXO selection → Secp256k1 signing → mempool.
        """
        if not self._wallet:
            return {"ok": False, "error": "No wallet loaded"}
        if not to or not (to.startswith("N") or to.startswith("3")):
            return {"ok": False, "error": "Invalid destination address"}
        try:
            amount_f = float(amount_nbl)
        except (TypeError, ValueError):
            return {"ok": False, "error": "amount must be a number"}
        if amount_f <= 0:
            return {"ok": False, "error": "Amount must be positive"}

        # Derive signing key + from-address
        from_addr = self._wallet.first_address
        # HDKey for first receiving address lives in _wallet._keys
        hd_key = self._wallet._keys.get(from_addr)
        if hd_key is None:
            # ensure derivation has run
            self._wallet._derive_address(0, 0)
            hd_key = self._wallet._keys.get(from_addr)
        if hd_key is None or hd_key.key is None:
            return {"ok": False, "error": "Cannot access signing key"}

        privkey_int: int = hd_key.key

        # Build transaction via TxBuilder
        builder = TxBuilder(self._bc.utxo)
        try:
            builder.add_output(to, amount_f)
        except ValueError as e:
            return {"ok": False, "error": str(e)}
        builder.set_change_address(from_addr)

        # Optional OP_RETURN memo (max 80 bytes)
        if memo:
            memo_bytes = memo.encode()[:80]
            op_ret_script = (
                bytes([0x6A]) +                  # OP_RETURN
                bytes([len(memo_bytes)]) +
                memo_bytes
            )
            pass  # v10.8: memo/OP_RETURN output not supported by TxBuilder; old code duplicated the last output instead

        tx = builder.build(from_addr, privkey_int)
        if tx is None:
            bal = self._bc.utxo.balance(from_addr)
            return {
                "ok":    False,
                "error": (
                    f"Insufficient balance — "
                    f"address {from_addr} holds "
                    f"{bal/10**DECIMALS:.9f} NBL"
                ),
            }

        # Submit to mempool
        ok2, msg = self._bc.add_to_mempool(tx)
        if not ok2:
            return {"ok": False, "error": f"Mempool rejected: {msg}"}

        log.info(f"MobileSDK.send: {amount_f} NBL → {to} txid={tx.txid}")
        return {
            "ok":     True,
            "txid":   tx.txid,
            "from":   from_addr,
            "to":     to,
            "amount": amount_f,
            "fee":    (sum(u.value for u in builder._inputs) -
                       sum(o.value for o in tx.outputs)) / 10**DECIMALS
                      if builder._inputs else 0.0,
            "size":   tx.byte_size() if hasattr(tx, "byte_size") else len(tx.serialize()),
            "memo":   memo[:80] if memo else "",
        }

    def get_transactions(self, address: str = None,
                          limit: int = 20) -> List[dict]:
        """
        Return recent transactions for an address by scanning
        the blockchain's UTXO spent/unspent records.
        """
        addr = address or (self._wallet.first_address if self._wallet else "")
        if not addr:
            return []
        results: List[dict] = []

        # Walk blocks newest → oldest
        try:
            chain_height = self._bc.height
            for h in range(chain_height, max(-1, chain_height - 10000), -1):
                bhash = self._bc._height_index.get(h)
                if not bhash:
                    continue
                block = self._bc._blocks.get(bhash)
                if not block:
                    continue
                for tx in block.transactions:
                    involved = False
                    record: dict = {
                        "txid":          tx.txid,
                        "height":        h,
                        "confirmations": chain_height - h + 1,
                        "inputs":        [],
                        "outputs":       [],
                        "type":          "unknown",
                        "amount":        0.0,
                    }
                    # Check outputs (received)
                    for idx, out in enumerate(tx.outputs):
                        out_addr = Script.address_from_script(
                            out.script_pubkey
                        ) if hasattr(Script, "address_from_script") else ""
                        if out_addr == addr:
                            involved = True
                            record["outputs"].append({
                                "index": idx,
                                "value": out.value / 10**DECIMALS,
                            })
                    # Check inputs (sent) — match via UTXO
                    for inp in tx.inputs:
                        spent_entry = self._bc.utxo._spent.get(
                            (inp.outpoint.txid, inp.outpoint.index)
                        ) if hasattr(self._bc.utxo, "_spent") else None
                        if spent_entry:
                            inp_addr = Script.address_from_script(
                                spent_entry.script_pubkey
                            ) if hasattr(Script, "address_from_script") else ""
                            if inp_addr == addr:
                                involved = True
                                record["inputs"].append({
                                    "txid":  inp.outpoint.txid,
                                    "index": inp.outpoint.index,
                                    "value": spent_entry.value / 10**DECIMALS,
                                })
                    if involved:
                        sent_val = sum(i["value"] for i in record["inputs"])
                        recv_val = sum(o["value"] for o in record["outputs"])
                        record["type"]   = "sent" if sent_val > 0 else "received"
                        record["amount"] = recv_val - sent_val
                        results.append(record)
                        if len(results) >= limit:
                            return results
        except Exception as e:
            log.warning(f"get_transactions scan error: {e}")
        return results

    def sign_message(self, message: str) -> Optional[str]:
        if not self._wallet:
            return None
        msg_h = hashlib.sha256(
            b"\x18NEBULA Signed Message:\n" + message.encode()
        ).digest()
        priv  = self._wallet.private_key_int
        r, s  = Secp256k1.sign(priv, sha256d(msg_h))
        return Secp256k1.sig_to_der(r, s).hex()

    def sdk_info(self) -> dict:
        return {
            "version":  "1.0.0",
            "network":  self.network,
            "chain_id": CHAIN_ID,
            "has_wallet": self._wallet is not None,
        }


# ---- PositionType
class PositionType(_enum.Enum):
    STAKING     = "staking"
    LIQUIDITY   = "liquidity"
    LENDING     = "lending"
    BORROWING   = "borrowing"
    FARMING     = "farming"
    VAULT       = "vault"
    OPTIONS     = "options"
    FUTURES     = "futures"


# ---- DeFiPosition
@dataclass
class DeFiPosition:
    pos_id:     str
    owner:      str
    protocol:   str
    pos_type:   PositionType
    asset:      str
    amount:     float
    value_usd:  float
    apy:        float
    opened_at:  float
    metadata:   dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "pos_id":    self.pos_id,
            "protocol":  self.protocol,
            "type":      self.pos_type.value,
            "asset":     self.asset,
            "amount":    f"{self.amount:.4f}",
            "value_usd": f"${self.value_usd:.2f}",
            "apy":       f"{self.apy*100:.2f}%",
        }
