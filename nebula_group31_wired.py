"""NEBULA group31 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. ValidatorInfo  (orig. lines 52361-52389)
   2. NEBULADex  (orig. lines 52517-52649)
   3. NBLNFTToken  (orig. lines 52664-52688)
   4. NBL721Registry  (orig. lines 52690-52942)
   5. BridgeRequest  (orig. lines 52957-52990)
   6. WrappedToken  (orig. lines 52992-53019)
   7. BridgeEngine  (orig. lines 53021-53262)
   8. TxBatcher  (orig. lines 53283-53367)
   9. StealthAddressScheme  (orig. lines 53378-53467)
  10. CoinJoinCoordinator  (orig. lines 53469-53558)
  11. OracleNode  (orig. lines 53572-53593)
  12. DecentralizedOracle  (orig. lines 53595-53714)
  13. LendingPool  (orig. lines 53724-53760)
  14. FarmingPool  (orig. lines 53762-53791)
  15. UserFarmInfo  (orig. lines 53793-53799)
  16. YieldFarm  (orig. lines 53801-53964)
  17. DIDDocument  (orig. lines 53979-54001)
  18. VerifiableCredential  (orig. lines 54003-54034)
  19. DIDRegistry  (orig. lines 54036-54210)
  20. ShamirSecretSharing  (orig. lines 54221-54286)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): AMMPool, BatchCoinSelector, C, FeeEstimator, LiquidityPool, LiquidityPoolC, NFTCollection, OrderBook, OutPoint, PriceFeed, Script, Secp256k1, Transaction, TxInput, TxOutput
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

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

DUST_THRESHOLD         = 546                            # min output amount in Neb

def sha256d(data: bytes) -> bytes:
    """Double SHA-256 — used everywhere in Bitcoin/NEBULA"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def hash160(data: bytes) -> bytes:
    """RIPEMD160(SHA256(data)) — used for addresses"""
    h = hashlib.new('ripemd160')
    h.update(hashlib.sha256(data).digest())
    return h.digest()

SIGHASH_ALL         = 0x01

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

BRIDGE_FEE_PCT     = 10   # 0.1% bridge fee

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

def _v108_nft_post(o):
    try:
        o.royalty_bps = int(float(getattr(o, 'royalty_pct', 0)) * 100)
    except Exception:
        _NB_SWALLOW_LOG.debug("swallowed Exception in _v108_nft_post", exc_info=True)

def _v108_sign_p2pkh(tx, selected_utxos, keys):
    """Sign every input of `tx` (P2PKH) using the key whose hash160 matches the
    spent output. `keys` = iterable of objects with .key (int) and .pubkey (point)."""
    by_h160 = {hash160(Secp256k1.pubkey_to_bytes(k.pubkey)): k for k in keys}
    for i, u in enumerate(selected_utxos):
        k = by_h160.get(u.script_pubkey[3:23])
        if k is None:
            return False
        sighash = tx.signature_hash(i, u.script_pubkey, SIGHASH_ALL)
        r, s_ = Secp256k1.sign(k.key, sighash)
        der = Secp256k1.sig_to_der(r, s_) + bytes([SIGHASH_ALL])
        tx.inputs[i].script_sig = Script.p2pkh_unlocking(der, Secp256k1.pubkey_to_bytes(k.pubkey))
        tx.invalidate_cache()
    return True

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- ValidatorInfo
@dataclass
@dataclass
class ValidatorInfo:
    address:       str
    total_stake:   int           # own + delegated
    delegators:    Dict[str,int] = field(default_factory=dict)
    blocks_signed: int = 0
    blocks_missed: int = 0
    commission:    float = 0.05  # 5% of delegator rewards
    is_jailed:     bool  = False
    jail_until:    int   = 0
    uptime_pct:    float = 100.0

    @property
    def reliability(self) -> float:
        total = self.blocks_signed + self.blocks_missed
        return self.blocks_signed / total if total > 0 else 1.0

    def to_dict(self) -> dict:
        return {
            "address":       self.address,
            "total_stake_nbl": f"{self.total_stake/10**DECIMALS:.3f}",
            "delegators":    len(self.delegators),
            "blocks_signed": self.blocks_signed,
            "blocks_missed": self.blocks_missed,
            "commission":    f"{self.commission*100:.1f}%",
            "is_jailed":     self.is_jailed,
            "uptime_pct":    f"{self.reliability*100:.2f}%",
        }


# ---- NEBULADex
class NEBULADex:
    """
    Top-level DEX combining order books and AMM pools.
    Hybrid: limit orders + AMM for passive liquidity.
    """

    DEX_FEE_PCT = 0.0005   # 0.05% protocol fee on AMM swaps

    def __init__(self, blockchain: 'NEBULABlockchain',
                 nbl20: 'NBL20Registry' = None):
        self._bc      = blockchain
        self._nbl20   = nbl20
        self._books:  Dict[str, OrderBook]   = {}
        self._pools:  Dict[str, LiquidityPool] = {}
        self._amms:   Dict[str, AMMPool]     = {}
        self._balances: Dict[str, Dict[str,int]] = {}  # addr -> token -> amount
        self._lock    = threading.RLock()
        self._fee_collector: Dict[str, int]  = {}

    def _pair_id(self, base: str, quote: str) -> str:
        return f"{base}:{quote}"

    def get_or_create_book(self, base: str, quote: str) -> OrderBook:
        pid = self._pair_id(base, quote)
        if pid not in self._books:
            self._books[pid] = OrderBook(pid)
        return self._books[pid]

    def create_pool(self, token_a: str, token_b: str,
                    fee_bps: int = 30) -> str:
        """Create a new AMM liquidity pool."""
        pid = self._pair_id(token_a, token_b)
        if pid in self._pools:
            return pid
        pool = LiquidityPoolC(
            pool_id = pid,
            token_a = token_a,
            token_b = token_b,
            fee_bps = fee_bps,
        )
        self._pools[pid] = pool
        self._amms[pid]  = AMMPool(pool)
        return pid

    def add_liquidity(self, provider: str, token_a: str, token_b: str,
                      amount_a: int, amount_b: int) -> Tuple[bool, str]:
        """Add liquidity to AMM pool."""
        with self._lock:
            pid  = self._pair_id(token_a, token_b)
            if pid not in self._amms:
                self.create_pool(token_a, token_b)
            amm  = self._amms[pid]
            a_used, b_used, lp = amm.add_liquidity(amount_a, amount_b)
            # Credit LP tokens
            lp_key = f"LP:{pid}"
            if provider not in self._balances:
                self._balances[provider] = {}
            self._balances[provider][lp_key] = (
                self._balances[provider].get(lp_key, 0) + lp)
            return True, (f"Added liquidity: {a_used} {token_a} + "
                          f"{b_used} {token_b} → {lp} LP tokens")

    def swap_amm(self, trader: str, token_in: str, token_out: str,
                 amount_in: int,
                 min_out: int = 0) -> Tuple[bool, str, int]:
        """Execute AMM swap."""
        with self._lock:
            pid       = self._pair_id(token_in, token_out)
            rev_pid   = self._pair_id(token_out, token_in)
            if pid in self._amms:
                amm        = self._amms[pid]
                is_a_to_b  = True
            elif rev_pid in self._amms:
                amm        = self._amms[rev_pid]
                is_a_to_b  = False
            else:
                return False, "No pool for this pair", 0

            impact = amm.price_impact(amount_in, is_a_to_b)
            if impact > 0.15:
                return False, f"Price impact too high: {impact*100:.1f}% > 15%", 0

            out, fee = amm.swap(amount_in, is_a_to_b)
            if out < min_out:
                return False, f"Slippage: got {out}, min {min_out}", 0

            # Protocol fee
            proto_fee = int(out * self.DEX_FEE_PCT)
            out      -= proto_fee
            self._fee_collector[token_out] = (
                self._fee_collector.get(token_out, 0) + proto_fee)

            return True, (f"Swapped {amount_in} {token_in} → "
                          f"{out} {token_out} (fee {fee})"), out

    def place_limit_order(self, maker: str, base: str, quote: str,
                          side: str, price: float,
                          amount: int) -> Tuple[str, List[dict]]:
        """Place limit order on order book."""
        with self._lock:
            book = self.get_or_create_book(base, quote)
            return book.place_order(maker, side, price, amount)

    def market_price(self, base: str, quote: str) -> float:
        """Best available price (AMM or order book)."""
        pid = self._pair_id(base, quote)
        if pid in self._pools:
            return self._pools[pid].price_a_in_b
        book = self._books.get(pid)
        if book and book._asks:
            return book._asks[0].price
        return 0.0

    def list_pools(self) -> List[dict]:
        return [p.to_dict() for p in self._pools.values()]

    def list_pairs(self) -> List[str]:
        return [f"{b.base}/{b.quote}" for b in self._books.values()]

    def dex_stats(self) -> dict:
        with self._lock:
            total_pools   = len(self._pools)
            total_pairs   = len(self._books)
            total_tvl     = sum(p.reserve_a + p.reserve_b
                                for p in self._pools.values())
            total_swaps   = sum(p.swaps_count for p in self._pools.values())
        return {
            "total_pools":   total_pools,
            "total_pairs":   total_pairs,
            "total_tvl_neb": total_tvl,
            "total_swaps":   total_swaps,
            "protocol_fee":  f"{self.DEX_FEE_PCT*100:.2f}%",
        }


# ---- NBLNFTToken
@dataclass
class NBLNFTToken:
    token_id:     int
    contract_id:  str
    owner:        str
    creator:      str
    metadata_uri: str
    metadata:     dict
    created_at:   float
    royalty_pct:  float = 0.05    # 5% royalty to creator
    is_burned:    bool  = False
    transfer_count: int = 0

    def to_dict(self) -> dict:
        return {
            "token_id":      self.token_id,
            "contract_id":   self.contract_id,
            "owner":         self.owner,
            "creator":       self.creator,
            "metadata_uri":  self.metadata_uri,
            "metadata":      self.metadata,
            "royalty_pct":   f"{self.royalty_pct*100:.1f}%",
            "is_burned":     self.is_burned,
            "transfers":     self.transfer_count,
        }


# ---- NBL721Registry
@dataclass
class NBL721Registry:
    """
    NBL-721 NFT standard registry.
    Manages collections, tokens, approvals, marketplace listings.
    """

    def __init__(self):
        self._collections: Dict[str, NFTCollection]      = {}
        self._tokens:      Dict[str, Dict[int, NBLNFTToken]] = {}  # cid -> {tid -> token}
        self._approvals:   Dict[str, Dict[int, str]]     = {}  # cid -> {tid -> approved_addr}
        self._operators:   Dict[str, Dict[str, bool]]    = {}  # owner -> {operator -> approved}
        self._listings:    Dict[str, Dict[int, dict]]    = {}  # cid -> {tid -> listing}
        self._lock         = threading.RLock()
        self._next_id:     Dict[str, int]                = {}  # cid -> next token id

    # ── Collection management ─────────────────────────────────────

    def create_collection(self, owner: str, name: str, symbol: str,
                           description: str = "",
                           max_supply: int = 0,
                           royalty_pct: float = 0.05) -> str:
        """Deploy a new NFT collection."""
        with self._lock:
            if not (0.0 <= royalty_pct <= 0.15):
                raise ValueError("Royalty must be 0%-15%")
            cid = hashlib.sha256(
                f"NBL721:{owner}:{name}:{symbol}:{time.time()}".encode()
            ).hexdigest()[:24]
            self._collections[cid] = NFTCollectionC(
                contract_id  = cid,
                name         = name,
                symbol       = symbol,
                owner        = owner,
                description  = description,
                max_supply   = max_supply,
                royalty_pct  = royalty_pct,
            )
            self._tokens[cid]   = {}
            self._approvals[cid]= {}
            self._listings[cid] = {}
            self._next_id[cid]  = 1
            return cid

    # ── Minting ───────────────────────────────────────────────────

    def mint(self, contract_id: str, to: str,
             metadata_uri: str = "",
             metadata: dict = None,
             caller: str = "") -> Tuple[int, str]:
        """Mint a new NFT. Returns (token_id, status)."""
        with self._lock:
            col = self._collections.get(contract_id)
            if not col:
                raise ValueError("Collection not found")
            if col.is_paused:
                raise ValueError("Collection is paused")
            if caller and caller != col.owner:
                raise PermissionError("Only collection owner can mint")
            if col.max_supply > 0 and col.total_minted >= col.max_supply:
                raise ValueError("Max supply reached")

            tid   = self._next_id[contract_id]
            token = NBLNFTToken(
                token_id     = tid,
                contract_id  = contract_id,
                owner        = to,
                creator      = col.owner,
                metadata_uri = metadata_uri,
                metadata     = metadata or {},
                created_at   = time.time(),
                royalty_pct  = col.royalty_pct,
            )
            self._tokens[contract_id][tid] = token
            self._next_id[contract_id]     = tid + 1
            col.total_minted              += 1
            return tid, f"Minted #{tid} to {to}"

    def batch_mint(self, contract_id: str, to: str, count: int,
                   base_uri: str = "", caller: str = "") -> List[int]:
        """Mint multiple tokens at once."""
        ids = []
        for i in range(count):
            uri = f"{base_uri}/{i}" if base_uri else ""
            tid, _ = self.mint(contract_id, to, uri, {}, caller)
            ids.append(tid)
        return ids

    # ── Transfer ──────────────────────────────────────────────────

    def transfer(self, contract_id: str, from_addr: str,
                 to_addr: str, token_id: int) -> Tuple[bool, str]:
        """Transfer NFT ownership."""
        with self._lock:
            token = self._tokens.get(contract_id, {}).get(token_id)
            if not token:
                return False, "Token not found"
            if token.is_burned:
                return False, "Token is burned"
            if token.owner != from_addr:
                # Check approval
                approved = self._approvals.get(contract_id, {}).get(token_id)
                ops      = self._operators.get(token.owner, {})
                if from_addr != approved and not ops.get(from_addr, False):
                    return False, "Not authorized"
            token.owner = to_addr
            token.transfer_count += 1
            # Clear approval on transfer
            if contract_id in self._approvals:
                self._approvals[contract_id].pop(token_id, None)
            return True, f"Token #{token_id} transferred to {to_addr}"

    def approve(self, contract_id: str, owner: str,
                approved_addr: str, token_id: int) -> Tuple[bool, str]:
        """Approve address to transfer specific token."""
        with self._lock:
            token = self._tokens.get(contract_id, {}).get(token_id)
            if not token or token.owner != owner:
                return False, "Not owner"
            if contract_id not in self._approvals:
                self._approvals[contract_id] = {}
            self._approvals[contract_id][token_id] = approved_addr
            return True, f"Approved {approved_addr} for token #{token_id}"

    def set_approval_for_all(self, owner: str, operator: str,
                              approved: bool) -> Tuple[bool, str]:
        """Grant/revoke operator rights for all owner's tokens."""
        with self._lock:
            if owner not in self._operators:
                self._operators[owner] = {}
            self._operators[owner][operator] = approved
            status = "granted" if approved else "revoked"
            return True, f"Operator {status} for {operator}"

    def burn(self, contract_id: str, owner: str,
             token_id: int) -> Tuple[bool, str]:
        """Burn (destroy) an NFT."""
        with self._lock:
            token = self._tokens.get(contract_id, {}).get(token_id)
            if not token:
                return False, "Not found"
            if token.owner != owner:
                return False, "Not owner"
            token.is_burned = True
            col = self._collections.get(contract_id)
            if col:
                col.total_burned += 1
            return True, f"Token #{token_id} burned"

    # ── Marketplace ───────────────────────────────────────────────

    def list_for_sale(self, contract_id: str, owner: str,
                      token_id: int, price_neb: int) -> Tuple[bool, str]:
        """List NFT for sale."""
        with self._lock:
            token = self._tokens.get(contract_id, {}).get(token_id)
            if not token or token.owner != owner:
                return False, "Not owner"
            if contract_id not in self._listings:
                self._listings[contract_id] = {}
            self._listings[contract_id][token_id] = {
                "seller":    owner,
                "price_neb": price_neb,
                "listed_at": time.time(),
            }
            return True, f"Listed #{token_id} for {price_neb/10**DECIMALS:.4f} NBL"

    def buy(self, contract_id: str, buyer: str,
            token_id: int) -> Tuple[bool, str, dict]:
        """Buy a listed NFT. Returns royalty breakdown."""
        with self._lock:
            listing = self._listings.get(contract_id, {}).get(token_id)
            if not listing:
                return False, "Not listed", {}
            token  = self._tokens.get(contract_id, {}).get(token_id)
            if not token:
                return False, "Token not found", {}

            price   = listing["price_neb"]
            royalty = int(price * token.royalty_pct)
            seller_get = price - royalty

            # Transfer token
            ok, msg = self.transfer(contract_id, token.owner, buyer, token_id)
            if not ok:
                return False, msg, {}

            # Remove listing
            self._listings[contract_id].pop(token_id, None)

            return True, f"Bought #{token_id} for {price/10**DECIMALS:.4f} NBL", {
                "price_neb":   price,
                "seller_gets": seller_get,
                "royalty_neb": royalty,
                "royalty_to":  token.creator,
            }

    def delist(self, contract_id: str, owner: str,
               token_id: int) -> Tuple[bool, str]:
        """Remove listing."""
        with self._lock:
            if self._listings.get(contract_id, {}).get(token_id, {}).get("seller") != owner:
                return False, "Not your listing"
            self._listings.get(contract_id, {}).pop(token_id, None)
            return True, "Delisted"

    # ── Queries ───────────────────────────────────────────────────

    def owner_of(self, contract_id: str, token_id: int) -> Optional[str]:
        t = self._tokens.get(contract_id, {}).get(token_id)
        return t.owner if t and not t.is_burned else None

    def tokens_of(self, contract_id: str, owner: str) -> List[int]:
        tokens = self._tokens.get(contract_id, {})
        return [tid for tid, t in tokens.items()
                if t.owner == owner and not t.is_burned]

    def token_info(self, contract_id: str, token_id: int) -> Optional[dict]:
        t = self._tokens.get(contract_id, {}).get(token_id)
        return t.to_dict() if t else None

    def collection_info(self, contract_id: str) -> Optional[dict]:
        c = self._collections.get(contract_id)
        return c.to_dict() if c else None

    def marketplace_listings(self, contract_id: str = None) -> List[dict]:
        result = []
        for cid, listings in self._listings.items():
            if contract_id and cid != contract_id:
                continue
            for tid, listing in listings.items():
                t = self._tokens.get(cid, {}).get(tid)
                result.append({
                    "contract_id": cid,
                    "token_id":    tid,
                    "metadata":    t.metadata if t else {},
                    **listing,
                })
        return result

    def nft_stats(self) -> dict:
        with self._lock:
            total_cols    = len(self._collections)
            total_tokens  = sum(len(t) for t in self._tokens.values())
            total_listed  = sum(len(l) for l in self._listings.values())
            total_burned  = sum(c.total_burned for c in self._collections.values())
        return {
            "total_collections": total_cols,
            "total_tokens":      total_tokens,
            "total_listed":      total_listed,
            "total_burned":      total_burned,
            "active_tokens":     total_tokens - total_burned,
        }


# ---- BridgeRequest
@dataclass
class BridgeRequest:
    request_id:    str
    user:          str
    direction:     str         # "nbl_to_eth" / "eth_to_nbl" / "nbl_to_btc" etc.
    source_chain:  str
    dest_chain:    str
    token:         str
    amount:        int
    dest_address:  str
    secret_hash:   str         # SHA256 of secret (for HTLC)
    secret:        str = ""    # revealed on claim
    status:        str = "pending"   # pending/locked/claimed/refunded/expired
    created_at:    float = 0.0
    lock_height:   int = 0
    expire_height: int = 0
    tx_hash_src:   str = ""
    tx_hash_dst:   str = ""
    fee_paid:      int = 0

    def to_dict(self) -> dict:
        return {
            "request_id":   self.request_id,
            "user":         self.user,
            "direction":    self.direction,
            "from":         self.source_chain,
            "to":           self.dest_chain,
            "token":        self.token,
            "amount":       self.amount,
            "dest_address": self.dest_address,
            "status":       self.status,
            "created_at":   self.created_at,
            "expires_at":   self.expire_height,
        }


# ---- WrappedToken
@dataclass
class WrappedToken:
    """Represents a bridged asset on NEBULA (e.g. wBTC, wETH)."""
    contract_id:   str
    original_chain: str
    original_token: str     # contract address or "native"
    symbol:        str
    name:          str
    decimals:      int
    total_minted:  int = 0
    total_burned:  int = 0
    custodian:     str = ""  # multisig address holding original asset

    @property
    def circulating(self) -> int:
        return self.total_minted - self.total_burned

    def to_dict(self) -> dict:
        return {
            "contract_id":     self.contract_id,
            "original_chain":  self.original_chain,
            "original_token":  self.original_token,
            "symbol":          self.symbol,
            "name":            self.name,
            "decimals":        self.decimals,
            "circulating":     self.circulating,
            "total_minted":    self.total_minted,
        }


# ---- BridgeEngine
class BridgeEngine:
    """
    NEBULA cross-chain bridge.

    How it works:
    1. User locks assets on source chain + generates secret.
    2. Bridge relayer sees the lock, mints wrapped tokens on NEBULA.
    3. User reveals secret to claim tokens.
    4. If timeout, user gets refund.

    Supported chains: Bitcoin, Ethereum, BNB Chain, Polygon.
    """

    BRIDGE_FEE_PCT   = 0.001     # 0.1% bridge fee
    LOCK_PERIOD      = 144       # ~24 hours in blocks
    MIN_AMOUNT       = 1_000     # minimum bridge amount in Neb
    SUPPORTED_CHAINS = ["bitcoin", "ethereum", "bnb", "polygon", "solana"]

    def __init__(self, blockchain: 'NEBULABlockchain',
                 nbl20: 'NBL20Registry' = None):
        self._bc        = blockchain
        self._nbl20     = nbl20
        self._requests: Dict[str, BridgeRequest]  = {}
        self._wrapped:  Dict[str, WrappedToken]   = {}   # symbol -> token
        self._relayers: set                        = set()
        self._lock      = threading.RLock()
        self._total_bridged_in:  int = 0
        self._total_bridged_out: int = 0

    # ── Wrapped token management ──────────────────────────────────

    def register_wrapped(self, original_chain: str, original_token: str,
                          symbol: str, name: str,
                          decimals: int, custodian: str = "") -> str:
        """Register a new wrapped asset type."""
        with self._lock:
            cid = hashlib.sha256(
                f"BRIDGE:{original_chain}:{original_token}:{symbol}".encode()
            ).hexdigest()[:20]
            self._wrapped[symbol] = WrappedToken(
                contract_id    = cid,
                original_chain = original_chain,
                original_token = original_token,
                symbol         = symbol,
                name           = name,
                decimals       = decimals,
                custodian      = custodian,
            )
            return cid

    # ── Bridge IN (external → NEBULA) ─────────────────────────────

    def initiate_bridge_in(self, user: str, source_chain: str,
                            token: str, amount: int,
                            dest_address: str,
                            secret: bytes) -> Tuple[bool, str]:
        """
        User wants to bring assets into NEBULA.
        User locks assets on source chain and calls this.
        """
        with self._lock:
            if source_chain not in self.SUPPORTED_CHAINS:
                return False, f"Unsupported chain: {source_chain}"
            if amount < self.MIN_AMOUNT:
                return False, f"Amount below minimum: {self.MIN_AMOUNT}"

            secret_hash = hashlib.sha256(secret).hexdigest()
            expire_h    = self._bc.height + self.LOCK_PERIOD
            fee         = int(amount * self.BRIDGE_FEE_PCT)
            net_amount  = amount - fee

            rid = hashlib.sha256(
                f"{user}{source_chain}{token}{amount}{time.time()}".encode()
            ).hexdigest()[:16]

            req = BridgeRequest(
                request_id    = rid,
                user          = user,
                direction     = f"{source_chain}_to_nbl",
                source_chain  = source_chain,
                dest_chain    = "nebula",
                token         = token,
                amount        = net_amount,
                dest_address  = dest_address,
                secret_hash   = secret_hash,
                status        = "pending",
                created_at    = time.time(),
                lock_height   = self._bc.height,
                expire_height = expire_h,
                fee_paid      = fee,
            )
            self._requests[rid] = req
            return True, rid

    def confirm_bridge_in(self, request_id: str,
                           relayer: str,
                           source_tx: str) -> Tuple[bool, str]:
        """
        Relayer confirms source chain lock — mints wrapped tokens on NEBULA.
        """
        with self._lock:
            req = self._requests.get(request_id)
            if not req:
                return False, "Request not found"
            if req.status != "pending":
                return False, f"Wrong status: {req.status}"
            if self._bc.height > req.expire_height:
                req.status = "expired"
                return False, "Request expired"

            req.status      = "locked"
            req.tx_hash_src = source_tx

            # Mint wrapped tokens
            wrapped = self._wrapped.get(req.token)
            if wrapped and self._nbl20:
                self._nbl20._balances.setdefault(
                    wrapped.contract_id, {})[req.dest_address] = (
                    self._nbl20._balances.get(wrapped.contract_id, {}).get(
                        req.dest_address, 0) + req.amount)
                wrapped.total_minted += req.amount
            self._total_bridged_in += req.amount
            return True, f"Minted {req.amount} wrapped {req.token} to {req.dest_address}"

    def claim_bridge_in(self, request_id: str,
                         secret: bytes) -> Tuple[bool, str]:
        """User reveals secret to finalize bridge-in."""
        with self._lock:
            req = self._requests.get(request_id)
            if not req or req.status != "locked":
                return False, "Not found or wrong status"
            if hashlib.sha256(secret).hexdigest() != req.secret_hash:
                return False, "Wrong secret"
            req.status = "claimed"
            req.secret = secret.hex()
            return True, f"Bridge-in complete: {req.amount} {req.token}"

    # ── Bridge OUT (NEBULA → external) ────────────────────────────

    def initiate_bridge_out(self, user: str, dest_chain: str,
                             token: str, amount: int,
                             dest_address: str) -> Tuple[bool, str]:
        """User wants to withdraw assets from NEBULA to external chain."""
        with self._lock:
            if dest_chain not in self.SUPPORTED_CHAINS:
                return False, f"Unsupported chain: {dest_chain}"
            if amount < self.MIN_AMOUNT:
                return False, f"Below minimum: {self.MIN_AMOUNT}"

            fee        = int(amount * self.BRIDGE_FEE_PCT)
            net_amount = amount - fee

            # Burn wrapped tokens
            wrapped = self._wrapped.get(token)
            if wrapped and self._nbl20:
                bal = self._nbl20._balances.get(wrapped.contract_id, {}).get(user, 0)
                if bal < amount:
                    return False, f"Insufficient wrapped balance: {bal}"
                self._nbl20._balances[wrapped.contract_id][user] -= amount
                wrapped.total_burned += amount

            rid = hashlib.sha256(
                f"OUT:{user}{dest_chain}{token}{amount}{time.time()}".encode()
            ).hexdigest()[:16]

            req = BridgeRequest(
                request_id    = rid,
                user          = user,
                direction     = f"nbl_to_{dest_chain}",
                source_chain  = "nebula",
                dest_chain    = dest_chain,
                token         = token,
                amount        = net_amount,
                dest_address  = dest_address,
                secret_hash   = "",
                status        = "locked",
                created_at    = time.time(),
                expire_height = self._bc.height + self.LOCK_PERIOD,
                fee_paid      = fee,
            )
            self._requests[rid] = req
            self._total_bridged_out += amount
            return True, rid

    def complete_bridge_out(self, request_id: str,
                             relayer: str,
                             dest_tx: str) -> Tuple[bool, str]:
        """Relayer confirms release on destination chain."""
        with self._lock:
            req = self._requests.get(request_id)
            if not req or req.status != "locked":
                return False, "Not found or wrong status"
            req.status      = "claimed"
            req.tx_hash_dst = dest_tx
            return True, f"Bridge-out complete tx {dest_tx}"

    def refund(self, request_id: str) -> Tuple[bool, str]:
        """Refund expired bridge request."""
        with self._lock:
            req = self._requests.get(request_id)
            if not req:
                return False, "Not found"
            if req.status not in ("pending", "locked"):
                return False, f"Cannot refund: {req.status}"
            if self._bc.height <= req.expire_height:
                return False, "Not expired yet"
            req.status = "refunded"
            # Re-mint burned tokens on refund
            if req.direction.startswith("nbl_to_"):
                wrapped = self._wrapped.get(req.token)
                if wrapped and self._nbl20:
                    self._nbl20._balances.setdefault(
                        wrapped.contract_id, {})[req.user] = (
                        self._nbl20._balances.get(
                            wrapped.contract_id, {}).get(req.user, 0) + req.amount)
                    wrapped.total_burned -= req.amount
            return True, f"Refunded {req.amount} {req.token} to {req.user}"

    # ── Queries ───────────────────────────────────────────────────

    def get_request(self, request_id: str) -> Optional[dict]:
        r = self._requests.get(request_id)
        return r.to_dict() if r else None

    def list_wrapped(self) -> List[dict]:
        return [w.to_dict() for w in self._wrapped.values()]

    def bridge_stats(self) -> dict:
        with self._lock:
            total   = len(self._requests)
            by_status = {}
            for r in self._requests.values():
                by_status[r.status] = by_status.get(r.status, 0) + 1
        return {
            "total_requests":    total,
            "by_status":         by_status,
            "total_bridged_in":  f"{self._total_bridged_in/10**DECIMALS:.4f} NBL",
            "total_bridged_out": f"{self._total_bridged_out/10**DECIMALS:.4f} NBL",
            "supported_chains":  self.SUPPORTED_CHAINS,
            "bridge_fee":        f"{self.BRIDGE_FEE_PCT*100:.1f}%",
            "wrapped_assets":    len(self._wrapped),
        }


# ---- TxBatcher
class TxBatcher:
    """
    Batch multiple payments into a single transaction.
    Reduces fees and improves privacy.
    """

    def __init__(self, wallet: 'NEBULAWallet',
                 blockchain: 'NEBULABlockchain',
                 fee_estimator: FeeEstimator = None):
        self._wallet    = wallet
        self._bc        = blockchain
        self._fee_est   = fee_estimator
        self._outputs:  List[Tuple[str, int]] = []   # (address, amount)

    def add_payment(self, address: str, amount_neb: int):
        """Add a payment to the batch."""
        if amount_neb < DUST_THRESHOLD:
            raise ValueError(f"Amount below dust: {amount_neb}")
        self._outputs.append((address, amount_neb))

    def clear(self):
        self._outputs.clear()

    def total_output(self) -> int:
        return sum(amt for _, amt in self._outputs)

    def estimated_fee(self) -> int:
        n_out = len(self._outputs) + 1  # +1 for change
        n_in  = max(1, self.total_output() // (10 * 10**DECIMALS))  # rough estimate
        if self._fee_est:
            return self._fee_est.estimate_tx_fee(n_in, n_out)
        return MIN_TX_FEE * n_in

    def build(self, sender_address: str,
               change_address: str = None) -> Optional['Transaction']:
        """Build the batched transaction."""
        if not self._outputs:
            return None
        change_address = change_address or sender_address
        total_out = self.total_output()
        fee       = self.estimated_fee()
        total_needed = total_out + fee

        # Select UTXOs
        cc = BatchCoinSelector(self._bc)
        selected, change = cc.select_utxos(sender_address, total_out, fee)
        if not selected:
            return None

        # Build inputs
        inputs = [
            TxInput(OutPoint(txid=u.txid, index=u.index))
            for u in selected
        ]

        # Build outputs
        outputs = [
            TxOutput(value=amt,
                     script_pubkey=Script.p2pkh_locking_from_address(addr))
            for addr, amt in self._outputs
        ]

        # Change output
        if change >= DUST_THRESHOLD:
            outputs.append(TxOutput(
                value=change,
                script_pubkey=Script.p2pkh_locking_from_address(change_address)
            ))

        tx = Transaction(inputs=inputs, outputs=outputs)
        # v10.8: the batched tx used to be returned UNSIGNED (mempool rejected it)
        if not _v108_sign_p2pkh(tx, selected, self._wallet._keys.values()):
            return None
        return tx

    def summary(self) -> dict:
        return {
            "payments":        len(self._outputs),
            "total_output_nbl": f"{self.total_output()/10**DECIMALS:.9f}",
            "estimated_fee":   f"{self.estimated_fee()/10**DECIMALS:.9f}",
            "outputs":         [
                {"to": addr, "nbl": f"{amt/10**DECIMALS:.9f}"}
                for addr, amt in self._outputs
            ],
        }


# ---- StealthAddressScheme
class StealthAddressScheme:
    """
    Stealth addresses for NEBULA (ECDH-based).
    Sender generates one-time address from recipient's scan/spend keys.
    Only recipient can find their payments by scanning the chain.

    Usage:
        1. Receiver publishes (scan_pub, spend_pub) as their stealth address.
        2. Sender derives ephemeral key R and sends to P = spend_pub + hash(r*scan_pub)*G
        3. Receiver scans by checking if hash(scan_priv * R) * G + spend_pub == P
    """

    @staticmethod
    def generate_stealth_keys() -> Tuple[int, int, bytes, bytes]:
        """Generate scan + spend key pair for receiver."""
        scan_priv  = secrets.randbelow(Secp256k1.N - 1) + 1
        spend_priv = secrets.randbelow(Secp256k1.N - 1) + 1
        scan_pub   = Secp256k1.pubkey_to_bytes(
                       Secp256k1.point_mul(scan_priv, Secp256k1.G()))
        spend_pub  = Secp256k1.pubkey_to_bytes(
                       Secp256k1.point_mul(spend_priv, Secp256k1.G()))
        return scan_priv, spend_priv, scan_pub, spend_pub

    @staticmethod
    def derive_payment_address(scan_pub_bytes: bytes,
                                spend_pub_bytes: bytes) -> Tuple[str, bytes]:
        """
        Sender: derive one-time payment address.
        Returns (nbl_address, ephemeral_pubkey).
        """
        r      = secrets.randbelow(Secp256k1.N - 1) + 1
        R      = Secp256k1.pubkey_to_bytes(
                   Secp256k1.point_mul(r, Secp256k1.G()))

        # Decode scan pubkey
        scan_x   = int.from_bytes(scan_pub_bytes[1:], 'big')
        scan_yq  = (pow(scan_x, 3, Secp256k1.P) + 7) % Secp256k1.P
        scan_y   = pow(scan_yq, (Secp256k1.P+1)//4, Secp256k1.P)
        if (scan_y % 2 == 0) != (scan_pub_bytes[0] == 0x02):
            scan_y = Secp256k1.P - scan_y
        scan_point = (scan_x, scan_y)

        shared = Secp256k1.point_mul(r, scan_point)
        h      = int.from_bytes(
                    hashlib.sha256(
                        Secp256k1.pubkey_to_bytes(shared)
                    ).digest(), 'big') % Secp256k1.N

        # Decode spend pubkey
        sp_x   = int.from_bytes(spend_pub_bytes[1:], 'big')
        sp_yq  = (pow(sp_x, 3, Secp256k1.P) + 7) % Secp256k1.P
        sp_y   = pow(sp_yq, (Secp256k1.P+1)//4, Secp256k1.P)
        if (sp_y % 2 == 0) != (spend_pub_bytes[0] == 0x02):
            sp_y = Secp256k1.P - sp_y
        spend_point = (sp_x, sp_y)

        # P = spend_pub + h*G
        hG     = Secp256k1.point_mul(h, Secp256k1.G())
        P      = Secp256k1.point_add(spend_point, hG)
        addr   = Script.p2pkh_address(Secp256k1.pubkey_to_bytes(P))
        return addr, R

    @staticmethod
    def check_payment(scan_priv: int, spend_priv: int,
                       R_bytes: bytes, address: str) -> Tuple[bool, Optional[int]]:
        """
        Receiver: check if a payment is theirs.
        Returns (is_mine, spending_key) if found.
        """
        R_x = int.from_bytes(R_bytes[1:], 'big')
        R_yq = (pow(R_x, 3, Secp256k1.P) + 7) % Secp256k1.P
        R_y  = pow(R_yq, (Secp256k1.P+1)//4, Secp256k1.P)
        if (R_y % 2 == 0) != (R_bytes[0] == 0x02):
            R_y = Secp256k1.P - R_y
        R_point = (R_x, R_y)

        shared = Secp256k1.point_mul(scan_priv, R_point)
        h      = int.from_bytes(
                    hashlib.sha256(
                        Secp256k1.pubkey_to_bytes(shared)
                    ).digest(), 'big') % Secp256k1.N

        priv_key = (spend_priv + h) % Secp256k1.N
        pub      = Secp256k1.pubkey_to_bytes(
                     Secp256k1.point_mul(priv_key, Secp256k1.G()))
        derived_addr = Script.p2pkh_address(pub)

        if derived_addr == address:
            return True, priv_key
        return False, None


# ---- CoinJoinCoordinator
class CoinJoinCoordinator:
    """
    CoinJoin coordinator for privacy.
    Combines multiple users' transactions into one
    to obscure the link between inputs and outputs.
    """

    MIN_PARTICIPANTS = 3
    STANDARD_AMOUNT  = 100 * 10**DECIMALS  # 100 NBL standard denomination

    def __init__(self):
        self._sessions: Dict[str, dict] = {}
        self._lock      = threading.RLock()

    def new_session(self, denomination: int = None) -> str:
        """Create a new CoinJoin session."""
        sid  = secrets.token_hex(16)
        denom = denomination or self.STANDARD_AMOUNT
        with self._lock:
            self._sessions[sid] = {
                "session_id":   sid,
                "denomination": denom,
                "participants": {},
                "status":       "open",
                "created_at":   time.time(),
                "inputs":       [],
                "outputs":      [],
            }
        return sid

    def join(self, session_id: str, participant: str,
              input_utxos: List[dict],
              output_address: str) -> Tuple[bool, str]:
        """Join a CoinJoin session."""
        with self._lock:
            s = self._sessions.get(session_id)
            if not s:
                return False, "Session not found"
            if s["status"] != "open":
                return False, f"Session is {s['status']}"
            if participant in s["participants"]:
                return False, "Already joined"

            s["participants"][participant] = {
                "inputs":  input_utxos,
                "output":  output_address,
                "joined":  time.time(),
            }
            s["inputs"].extend(input_utxos)
            s["outputs"].append({
                "address": output_address,
                "amount":  s["denomination"],
            })

            # Auto-start when enough participants
            if len(s["participants"]) >= self.MIN_PARTICIPANTS:
                s["status"] = "mixing"
                import random
                random.shuffle(s["outputs"])

            return True, f"Joined session {session_id}"

    def build_coinjoin_tx(self, session_id: str) -> Optional[dict]:
        """Build the combined CoinJoin transaction."""
        with self._lock:
            s = self._sessions.get(session_id)
            if not s or s["status"] != "mixing":
                return None
            tx_desc = {
                "session_id":    session_id,
                "inputs":        s["inputs"],
                "outputs":       s["outputs"],
                "participants":  len(s["participants"]),
                "denomination":  s["denomination"],
                "privacy_score": len(s["participants"]) * 10,
            }
            s["status"] = "complete"
            return tx_desc

    def session_info(self, session_id: str) -> Optional[dict]:
        s = self._sessions.get(session_id)
        if not s:
            return None
        return {
            "session_id":   session_id,
            "denomination": f"{s['denomination']/10**DECIMALS:.3f} NBL",
            "participants": len(s["participants"]),
            "status":       s["status"],
            "min_needed":   self.MIN_PARTICIPANTS,
        }


# ---- OracleNode
@dataclass
class OracleNode:
    """Single oracle data provider."""

    def __init__(self, node_id: str, address: str):
        self.node_id  = node_id
        self.address  = address
        self.reports: Dict[str, PriceFeed] = {}
        self.stake    = 0
        self.reputation = 1.0   # 0.0 - 1.0
        self.reports_count = 0
        self.slashes   = 0

    def report(self, pair: str, price: float):
        self.reports[pair] = PriceFeed(
            pair      = pair,
            price     = price,
            timestamp = time.time(),
            source    = self.node_id,
            confidence= self.reputation,
        )
        self.reports_count += 1


# ---- DecentralizedOracle
class DecentralizedOracle:
    """
    Aggregates price reports from multiple oracle nodes.
    Uses stake-weighted median to resist manipulation.
    Slashes nodes that report outlier prices.
    """

    OUTLIER_THRESHOLD = 0.10    # 10% deviation = outlier
    MIN_REPORTERS     = 3
    STALE_THRESHOLD   = 300     # 5 minutes

    def __init__(self):
        self._nodes:  Dict[str, OracleNode] = {}
        self._prices: Dict[str, float]      = {}   # pair -> aggregated price
        self._history: Dict[str, List[Tuple[float,float]]] = {}  # pair -> [(ts, price)]
        self._lock    = threading.RLock()

    def register_node(self, node_id: str, address: str,
                       stake: int) -> bool:
        with self._lock:
            if node_id in self._nodes:
                return False
            node = OracleNode(node_id, address)
            node.stake = stake
            self._nodes[node_id] = node
            return True

    def submit_price(self, node_id: str, pair: str,
                     price: float) -> Tuple[bool, str]:
        with self._lock:
            node = self._nodes.get(node_id)
            if not node:
                return False, "Node not registered"
            if price <= 0:
                return False, "Price must be positive"
            node.report(pair, price)
            self._aggregate(pair)
            return True, f"Reported {pair} = {price}"

    def _aggregate(self, pair: str):
        """Compute stake-weighted median price."""
        reports = [
            (n.reports[pair].price, n.stake * n.reputation)
            for n in self._nodes.values()
            if pair in n.reports and not n.reports[pair].is_stale()
        ]
        if len(reports) < self.MIN_REPORTERS:
            return

        total_weight = sum(w for _, w in reports)
        if total_weight == 0:
            return

        # Weighted median
        reports.sort(key=lambda x: x[0])
        cumulative = 0.0
        median_price = reports[0][0]
        for price, weight in reports:
            cumulative += weight / total_weight
            if cumulative >= 0.5:
                median_price = price
                break

        self._prices[pair] = median_price
        if pair not in self._history:
            self._history[pair] = []
        self._history[pair].append((time.time(), median_price))
        if len(self._history[pair]) > 1440:
            self._history[pair].pop(0)

        # Slash outliers
        for n in self._nodes.values():
            if pair not in n.reports:
                continue
            reported = n.reports[pair].price
            deviation = abs(reported - median_price) / median_price
            if deviation > self.OUTLIER_THRESHOLD:
                n.reputation = max(0.1, n.reputation - 0.05)
                n.slashes   += 1

    def get_price(self, pair: str) -> Optional[float]:
        return self._prices.get(pair)

    def get_feed(self, pair: str) -> Optional[dict]:
        price = self._prices.get(pair)
        if price is None:
            return None
        history = self._history.get(pair, [])
        day_ago = time.time() - 86400
        day_hist = [(t, p) for t, p in history if t >= day_ago]
        if day_hist:
            prices = [p for _, p in day_hist]
            high   = max(prices)
            low    = min(prices)
            first  = day_hist[0][1]
            chg    = (price - first) / first if first > 0 else 0
        else:
            high = low = price
            chg  = 0
        return {
            "pair":        pair,
            "price":       price,
            "24h_high":    high,
            "24h_low":     low,
            "24h_change":  f"{chg*100:+.2f}%",
            "reporters":   len([n for n in self._nodes.values()
                                if pair in n.reports]),
        }

    def oracle_stats(self) -> dict:
        with self._lock:
            nodes  = len(self._nodes)
            active = sum(1 for n in self._nodes.values()
                         if n.reports_count > 0)
        return {
            "total_nodes":  nodes,
            "active_nodes": active,
            "tracked_pairs": list(self._prices.keys()),
            "min_reporters": self.MIN_REPORTERS,
        }


# ---- LendingPool
@dataclass
class LendingPool:
    asset:           str
    total_supplied:  int = 0
    total_borrowed:  int = 0
    supply_rate:     float = 0.03   # 3% APY base
    borrow_rate:     float = 0.06   # 6% APY base
    utilization_optimal: float = 0.80
    last_update:     float = field(default_factory=time.time)

    @property
    def utilization(self) -> float:
        return self.total_borrowed / self.total_supplied if self.total_supplied > 0 else 0

    @property
    def available(self) -> int:
        return self.total_supplied - self.total_borrowed

    def dynamic_borrow_rate(self) -> float:
        """Higher utilization = higher borrow rate (kink model)."""
        u = self.utilization
        if u <= self.utilization_optimal:
            return self.borrow_rate * (u / self.utilization_optimal)
        else:
            excess = (u - self.utilization_optimal) / (1 - self.utilization_optimal)
            return self.borrow_rate + excess * 0.50   # steep rise above optimal

    def to_dict(self) -> dict:
        return {
            "asset":           self.asset,
            "total_supplied":  self.total_supplied,
            "total_borrowed":  self.total_borrowed,
            "available":       self.available,
            "utilization_pct": f"{self.utilization*100:.2f}%",
            "supply_apy":      f"{self.supply_rate*100:.2f}%",
            "borrow_apy":      f"{self.dynamic_borrow_rate()*100:.2f}%",
        }


# ---- FarmingPool
@dataclass
# ================================================================
# MODULE 133  nebula_yield.py — Yield Farming & Liquidity Mining
# ================================================================
# NBL rewards for liquidity providers.
# Farming pools, reward multipliers, vesting.
# ================================================================

@dataclass
class FarmingPool:
    pool_id:       str
    lp_token:      str      # LP token contract ID
    reward_token:  str      # NBL or other token
    reward_per_block: int   # reward distributed per block
    total_staked:  int = 0
    acc_reward_per_share: int = 0    # accumulated reward * 1e12 / total_staked
    last_reward_block: int = 0
    multiplier:    float = 1.0
    start_block:   int = 0
    end_block:     int = 0

    def to_dict(self) -> dict:
        return {
            "pool_id":         self.pool_id,
            "lp_token":        self.lp_token,
            "reward_token":    self.reward_token,
            "reward_per_block": self.reward_per_block,
            "total_staked":    self.total_staked,
            "multiplier":      self.multiplier,
        }


# ---- UserFarmInfo
@dataclass
class UserFarmInfo:
    user:          str
    pool_id:       str
    staked_amount: int = 0
    reward_debt:   int = 0    # prevents double-claiming
    pending_rewards: int = 0


# ---- YieldFarm
class YieldFarm:
    """
    NEBULA yield farming protocol.
    Users stake LP tokens to earn NBL rewards.
    Reward rate decreases over time (emission schedule).
    """

    PRECISION = 10**12

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._pools: Dict[str, FarmingPool]         = {}
        self._users: Dict[str, Dict[str, UserFarmInfo]] = {}  # user -> pool_id -> info
        self._total_rewards_distributed: int = 0
        self._lock   = threading.RLock()

    def add_pool(self, lp_token: str, reward_token: str,
                 reward_per_block: int,
                 multiplier: float = 1.0,
                 start_block: int = 0,
                 end_block: int = 0) -> str:
        """Add a new farming pool."""
        with self._lock:
            pid = hashlib.sha256(
                f"FARM:{lp_token}:{reward_token}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._pools[pid] = FarmingPool(
                pool_id           = pid,
                lp_token          = lp_token,
                reward_token      = reward_token,
                reward_per_block  = reward_per_block,
                multiplier        = multiplier,
                start_block       = start_block or self._bc.height,
                end_block         = end_block,
                last_reward_block = self._bc.height,
            )
            return pid

    def _update_pool(self, pool: FarmingPool):
        """Update accumulated rewards per share."""
        cur = self._bc.height
        if cur <= pool.last_reward_block:
            return
        if pool.total_staked == 0:
            pool.last_reward_block = cur
            return
        if pool.end_block > 0 and cur > pool.end_block:
            blocks = pool.end_block - pool.last_reward_block
        else:
            blocks = cur - pool.last_reward_block
        if blocks <= 0:
            return
        reward = int(blocks * pool.reward_per_block * pool.multiplier)
        pool.acc_reward_per_share += reward * self.PRECISION // pool.total_staked
        pool.last_reward_block     = cur
        self._total_rewards_distributed += reward

    def stake(self, user: str, pool_id: str,
              amount: int) -> Tuple[bool, str]:
        """Stake LP tokens into farming pool."""
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, "Pool not found"
            self._update_pool(pool)

            if user not in self._users:
                self._users[user] = {}
            if pool_id not in self._users[user]:
                self._users[user][pool_id] = UserFarmInfo(
                    user=user, pool_id=pool_id)

            info = self._users[user][pool_id]

            # Claim pending before updating
            pending = self._calc_pending(info, pool)
            info.pending_rewards += pending

            info.staked_amount += amount
            pool.total_staked  += amount
            info.reward_debt    = (info.staked_amount *
                                   pool.acc_reward_per_share // self.PRECISION)
            return True, f"Staked {amount} LP tokens in pool {pool_id}"

    def unstake(self, user: str, pool_id: str,
                amount: int) -> Tuple[bool, str]:
        """Unstake LP tokens."""
        with self._lock:
            pool = self._pools.get(pool_id)
            info = self._users.get(user, {}).get(pool_id)
            if not pool or not info:
                return False, "Not found"
            if amount > info.staked_amount:
                return False, "Insufficient staked amount"
            self._update_pool(pool)

            pending = self._calc_pending(info, pool)
            info.pending_rewards += pending

            info.staked_amount -= amount
            pool.total_staked  -= amount
            info.reward_debt    = (info.staked_amount *
                                   pool.acc_reward_per_share // self.PRECISION)
            return True, f"Unstaked {amount} LP tokens"

    def harvest(self, user: str, pool_id: str) -> Tuple[bool, int]:
        """Claim accumulated rewards."""
        with self._lock:
            pool = self._pools.get(pool_id)
            info = self._users.get(user, {}).get(pool_id)
            if not pool or not info:
                return False, 0
            self._update_pool(pool)
            pending  = self._calc_pending(info, pool)
            total    = info.pending_rewards + pending
            if total == 0:
                return False, 0
            info.pending_rewards = 0
            info.reward_debt     = (info.staked_amount *
                                    pool.acc_reward_per_share // self.PRECISION)
            return True, total

    def _calc_pending(self, info: UserFarmInfo,
                       pool: FarmingPool) -> int:
        if info.staked_amount == 0:
            return 0
        return (info.staked_amount * pool.acc_reward_per_share //
                self.PRECISION - info.reward_debt)

    def pending_rewards(self, user: str, pool_id: str) -> int:
        with self._lock:
            pool = self._pools.get(pool_id)
            info = self._users.get(user, {}).get(pool_id)
            if not pool or not info:
                return 0
            self._update_pool(pool)
            return info.pending_rewards + self._calc_pending(info, pool)

    def user_info(self, user: str) -> List[dict]:
        with self._lock:
            pools_info = self._users.get(user, {})
        result = []
        for pid, info in pools_info.items():
            pool = self._pools.get(pid)
            if pool:
                pend = self.pending_rewards(user, pid)
                result.append({
                    "pool_id":       pid,
                    "lp_token":      pool.lp_token,
                    "staked":        info.staked_amount,
                    "pending_rewards": pend,
                })
        return result

    def farm_stats(self) -> dict:
        with self._lock:
            total_pools = len(self._pools)
            total_tvl   = sum(p.total_staked for p in self._pools.values())
        return {
            "total_pools":       total_pools,
            "total_tvl":         total_tvl,
            "total_distributed": f"{self._total_rewards_distributed/10**DECIMALS:.3f} NBL",
            "pools":             [p.to_dict() for p in self._pools.values()],
        }


# ---- DIDDocument
@dataclass
class DIDDocument:
    did:             str          # e.g. "did:nbl:NxAbc123..."
    controller:      str          # NBL address controlling this DID
    public_keys:     List[dict]
    authentication:  List[str]
    services:        List[dict]
    created:         float
    updated:         float
    deactivated:     bool = False

    def to_dict(self) -> dict:
        return {
            "@context":      "https://www.w3.org/ns/did/v1",
            "id":            self.did,
            "controller":    self.controller,
            "verificationMethod": self.public_keys,
            "authentication":    self.authentication,
            "service":           self.services,
            "created":           self.created,
            "updated":           self.updated,
            "deactivated":       self.deactivated,
        }


# ---- VerifiableCredential
@dataclass
class VerifiableCredential:
    credential_id:  str
    issuer_did:     str
    subject_did:    str
    claim_type:     str      # e.g. "AgeVerification", "KYC", "Membership"
    claims:         dict
    issued_at:      float
    expires_at:     float
    proof:          dict     # cryptographic proof
    is_revoked:     bool = False

    @property
    def is_expired(self) -> bool:
        return time.time() > self.expires_at

    @property
    def is_valid(self) -> bool:
        return not self.is_revoked and not self.is_expired

    def to_dict(self) -> dict:
        return {
            "@context":          ["https://www.w3.org/2018/credentials/v1"],
            "id":                self.credential_id,
            "type":              ["VerifiableCredential", self.claim_type],
            "issuer":            self.issuer_did,
            "credentialSubject": {"id": self.subject_did, **self.claims},
            "issuanceDate":      self.issued_at,
            "expirationDate":    self.expires_at,
            "proof":             self.proof,
            "isRevoked":         self.is_revoked,
        }


# ---- DIDRegistry
class DIDRegistry:
    """
    NEBULA Decentralized Identity Registry.
    Anyone can create a DID for free.
    Identity is self-sovereign — no central authority.
    """

    DID_METHOD = "nbl"

    def __init__(self):
        self._dids:        Dict[str, DIDDocument]          = {}
        self._credentials: Dict[str, VerifiableCredential] = {}
        self._revoked:     Set[str]                        = set()
        self._lock         = threading.RLock()

    def create_did(self, address: str,
                   public_key_bytes: bytes,
                   services: List[dict] = None) -> str:
        """Create a new DID for an address."""
        with self._lock:
            did = f"did:{self.DID_METHOD}:{address}"
            if did in self._dids:
                return did   # already exists

            key_id = f"{did}#key-1"
            doc = DIDDocument(
                did         = did,
                controller  = address,
                public_keys = [{
                    "id":              key_id,
                    "type":            "EcdsaSecp256k1VerificationKey2019",
                    "controller":      did,
                    "publicKeyHex":    public_key_bytes.hex(),
                }],
                authentication = [key_id],
                services    = services or [],
                created     = time.time(),
                updated     = time.time(),
            )
            self._dids[did] = doc
            return did

    def resolve(self, did: str) -> Optional[dict]:
        """Resolve a DID to its document."""
        doc = self._dids.get(did)
        return doc.to_dict() if doc and not doc.deactivated else None

    def update_did(self, did: str, controller: str,
                   services: List[dict] = None,
                   new_key: bytes = None) -> Tuple[bool, str]:
        """Update DID document."""
        with self._lock:
            doc = self._dids.get(did)
            if not doc:
                return False, "DID not found"
            if doc.controller != controller:
                return False, "Not controller"
            if doc.deactivated:
                return False, "DID deactivated"
            if services is not None:
                doc.services = services
            if new_key is not None:
                key_id = f"{did}#key-{len(doc.public_keys)+1}"
                doc.public_keys.append({
                    "id":           key_id,
                    "type":         "EcdsaSecp256k1VerificationKey2019",
                    "controller":   did,
                    "publicKeyHex": new_key.hex(),
                })
                doc.authentication.append(key_id)
            doc.updated = time.time()
            return True, "Updated"

    def deactivate(self, did: str, controller: str) -> Tuple[bool, str]:
        """Deactivate a DID permanently."""
        with self._lock:
            doc = self._dids.get(did)
            if not doc or doc.controller != controller:
                return False, "Not found or not controller"
            doc.deactivated = True
            doc.updated     = time.time()
            return True, f"DID {did} deactivated"

    def issue_credential(self, issuer_did: str, subject_did: str,
                          claim_type: str, claims: dict,
                          validity_days: int = 365,
                          issuer_privkey: int = None) -> str:
        """Issue a verifiable credential."""
        with self._lock:
            if issuer_did not in self._dids:
                raise ValueError("Issuer DID not found")
            if subject_did not in self._dids:
                raise ValueError("Subject DID not found")

            cid = hashlib.sha256(
                f"{issuer_did}{subject_did}{claim_type}{time.time()}".encode()
            ).hexdigest()[:24]

            proof_data = json.dumps({
                "id": cid, "issuer": issuer_did,
                "subject": subject_did, "claims": claims,
            }, sort_keys=True).encode()

            if issuer_privkey:
                r, s = Secp256k1.sign(issuer_privkey, sha256d(proof_data))
                proof = {
                    "type":             "EcdsaSecp256k1Signature2019",
                    "proofPurpose":     "assertionMethod",
                    "verificationMethod": f"{issuer_did}#key-1",
                    "jws":              Secp256k1.sig_to_der(r, s).hex(),
                }
            else:
                proof = {
                    "type":  "EcdsaSecp256k1Signature2019",
                    "jws":   hashlib.sha256(proof_data).hexdigest(),
                }

            vc = VerifiableCredential(
                credential_id = cid,
                issuer_did    = issuer_did,
                subject_did   = subject_did,
                claim_type    = claim_type,
                claims        = claims,
                issued_at     = time.time(),
                expires_at    = time.time() + validity_days * 86400,
                proof         = proof,
            )
            self._credentials[cid] = vc
            return cid

    def verify_credential(self, credential_id: str) -> Tuple[bool, str]:
        """Verify a credential is valid and not revoked."""
        vc = self._credentials.get(credential_id)
        if not vc:
            return False, "Credential not found"
        if vc.is_revoked:
            return False, "Revoked"
        if vc.is_expired:
            return False, f"Expired at {vc.expires_at}"
        issuer_doc = self._dids.get(vc.issuer_did)
        if not issuer_doc or issuer_doc.deactivated:
            return False, "Issuer DID invalid"
        return True, "Valid"

    def revoke_credential(self, credential_id: str,
                           issuer_did: str) -> Tuple[bool, str]:
        """Revoke an issued credential."""
        with self._lock:
            vc = self._credentials.get(credential_id)
            if not vc:
                return False, "Not found"
            if vc.issuer_did != issuer_did:
                return False, "Not issuer"
            vc.is_revoked = True
            self._revoked.add(credential_id)
            return True, "Revoked"

    def get_credentials(self, subject_did: str) -> List[dict]:
        """Get all credentials for a subject."""
        return [vc.to_dict() for vc in self._credentials.values()
                if vc.subject_did == subject_did and not vc.is_revoked]

    def did_stats(self) -> dict:
        with self._lock:
            total_dids   = len(self._dids)
            active_dids  = sum(1 for d in self._dids.values() if not d.deactivated)
            total_creds  = len(self._credentials)
            valid_creds  = sum(1 for c in self._credentials.values() if c.is_valid)
        return {
            "total_dids":    total_dids,
            "active_dids":   active_dids,
            "total_creds":   total_creds,
            "valid_creds":   valid_creds,
            "revoked_creds": len(self._revoked),
        }


# ---- ShamirSecretSharing
class ShamirSecretSharing:
    """
    Shamir's Secret Sharing Scheme.
    Split a secret into n shares, require k to reconstruct.
    Used for distributed key management.
    """

    PRIME = Secp256k1.N   # Use curve order as field prime

    @classmethod
    def split(cls, secret: int, k: int, n: int) -> List[Tuple[int, int]]:
        """
        Split secret into n shares, k needed to reconstruct.
        Returns list of (x, y) share pairs.
        """
        if k > n:
            raise ValueError(f"k ({k}) must be <= n ({n})")
        if k < 2:
            raise ValueError("k must be >= 2")

        # Generate k-1 random coefficients for polynomial
        coeffs = [secret] + [secrets.randbelow(cls.PRIME) for _ in range(k-1)]

        def poly_eval(x: int) -> int:
            result = 0
            for i, c in enumerate(coeffs):
                result = (result + c * pow(x, i, cls.PRIME)) % cls.PRIME
            return result

        return [(i+1, poly_eval(i+1)) for i in range(n)]

    @classmethod
    def reconstruct(cls, shares: List[Tuple[int, int]]) -> int:
        """Reconstruct secret from k shares using Lagrange interpolation."""
        def lagrange_basis(i: int, x_vals: List[int]) -> int:
            xi = x_vals[i]
            num = den = 1
            for j, xj in enumerate(x_vals):
                if j == i:
                    continue
                num = num * (-xj) % cls.PRIME
                den = den * (xi - xj) % cls.PRIME
            return num * pow(den, cls.PRIME - 2, cls.PRIME) % cls.PRIME

        x_vals = [s[0] for s in shares]
        y_vals = [s[1] for s in shares]
        secret = 0
        for i in range(len(shares)):
            secret = (secret + y_vals[i] * lagrange_basis(i, x_vals)) % cls.PRIME
        return secret

    @classmethod
    def verify_share(cls, share: Tuple[int, int],
                      commitments: List[Tuple[int, int]]) -> bool:
        """
        Feldman VSS: verify share against public commitments.
        commitments = [coeff_i * G for each coefficient]
        """
        x, y = share
        lhs  = Secp256k1.point_mul(y, Secp256k1.G())
        rhs  = None
        for i, C in enumerate(commitments):
            xi_power = pow(x, i, Secp256k1.N)
            term     = Secp256k1.point_mul(xi_power, C)
            rhs      = Secp256k1.point_add(rhs, term)
        return lhs == rhs


# ======================================================================
# ======================================================================
#  GROUP31 WIRING SECTION
#  Everything ABOVE this banner is the verbatim group31 code taken from
#  nebula_v10_11.py.  Everything BELOW is new glue code that connects all
#  20 classes to the chain WITHOUT editing nebula_v10_11.py.
#
#  Design rules (from nebula_group31_guide.txt):
#    A) one separate Layer that owns the 20 classes
#    B) the Layer NEVER rejects a block or a transaction; every callback
#       is wrapped in try/except and failures are only counted in .errors
#    C) hooks are installed by wrapping host methods; uninstall() restores
#       every original method exactly
#    D) report-only: nothing here changes consensus rules
#
#  Usage (no edit of the host file is needed):
#       import nebula_v10_11 as host
#       import nebula_group31_wired as g31
#       g31.install(host)          # patch hooks
#       node = host.NEBULAFullNode(...)      # node.group31 is now a Layer31
#       print(node.group31.report())
#       g31.uninstall(host)        # restore everything
# ======================================================================
# ======================================================================

import collections as _g31_collections
import functools as _g31_functools
import sys as _g31_sys
import threading as _g31_threading
import time as _g31_time

GROUP31_CLASS_NAMES = (
    "ValidatorInfo", "NBLNFTToken", "NBL721Registry", "BridgeRequest",
    "WrappedToken", "OracleNode", "LendingPool", "FarmingPool",
    "UserFarmInfo", "DIDDocument", "VerifiableCredential", "NEBULADex",
    "BridgeEngine", "TxBatcher", "StealthAddressScheme",
    "CoinJoinCoordinator", "DecentralizedOracle", "YieldFarm",
    "DIDRegistry", "ShamirSecretSharing",
)

_G31_LOCK = _g31_threading.RLock()
_G31_ACTIVE: list = []                 # every live Layer31 (newest last)
_G31_SHARED = {"coinjoin": None}       # one CoinJoin coordinator per process
_G31_ROUTES: dict = {}                 # path -> handler we registered


def _g31_shared_coinjoin():
    """One CoinJoinCoordinator shared by the node layer and every wallet."""
    with _G31_LOCK:
        if _G31_SHARED["coinjoin"] is None:
            _G31_SHARED["coinjoin"] = CoinJoinCoordinator()
        return _G31_SHARED["coinjoin"]


def _g31_active_layer():
    with _G31_LOCK:
        return _G31_ACTIVE[-1] if _G31_ACTIVE else None


# ----------------------------------------------------------------------
#  Layer31  -  node side (chain listener + services)
# ----------------------------------------------------------------------
class Layer31:
    """
    Owns every group31 service.  Attached to the node as `node.group31`
    and registered as a chain listener (on_connect / on_reorg).

    Class -> where it lives:
      NEBULADex            -> self.dex
      BridgeEngine         -> self.bridge          (BridgeRequest, WrappedToken inside)
      DecentralizedOracle  -> self.oracle          (OracleNode inside)
      YieldFarm            -> self.farm            (FarmingPool, UserFarmInfo inside)
      NBL721Registry       -> self.nft             (NBLNFTToken inside)
      DIDRegistry          -> self.dids            (DIDDocument, VerifiableCredential inside)
      CoinJoinCoordinator  -> self.coinjoin        (shared with wallets)
      StealthAddressScheme -> self.stealth         (static helpers)
      ShamirSecretSharing  -> self.shamir          (class helpers)
      TxBatcher            -> self.new_batcher(wallet)
      LendingPool          -> self.lending         (dict asset -> LendingPool)
      ValidatorInfo        -> self.validators      (dict address -> ValidatorInfo)
    """

    EVENT_CAP   = 1000     # RAM cap for the event log
    SIGNER_CAP  = 5000     # RAM cap for height -> block-signer memory
    POOL_CAP    = 256      # max lending pools created through the layer

    def __init__(self, node):
        self.node    = node
        self.errors  = 0
        self.last_error = ""
        self._lock   = _g31_threading.RLock()
        self.events  = _g31_collections.deque(maxlen=self.EVENT_CAP)
        self.stats_  = {
            "blocks_connected": 0,
            "reorgs":           0,
            "txs_seen":         0,
            "txs_accepted":     0,
            "batch_like_txs":   0,
            "last_height":      0,
        }
        self.bc = (getattr(node, "bc", None)
                   or getattr(node, "blockchain", None)
                   or getattr(node, "chain", None))

        # ---- services (each one is a real group31 class) ----
        self.dex       = NEBULADex(self.bc)
        self.bridge    = BridgeEngine(self.bc)
        self.oracle    = DecentralizedOracle()
        self.farm      = YieldFarm(self.bc)
        self.nft       = NBL721Registry()
        self.dids      = DIDRegistry()
        self.coinjoin  = _g31_shared_coinjoin()
        self.stealth   = StealthAddressScheme
        self.shamir    = ShamirSecretSharing

        # ---- data-type holders ----
        self.lending:    dict = {}     # asset   -> LendingPool
        self.validators: dict = {}     # address -> ValidatorInfo
        self._signer_by_height: "_g31_collections.OrderedDict[int, str]" = \
            _g31_collections.OrderedDict()

    # ------------------------------------------------------------ utils
    def _fail(self, where: str, exc: Exception):
        self.errors += 1
        self.last_error = f"{where}: {type(exc).__name__}: {exc}"
        try:
            self.events.append(("error", _g31_time.time(), self.last_error))
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer31._fail", exc_info=True)

    def _height_of(self, block):
        for owner in (block, getattr(block, "header", None)):
            if owner is None:
                continue
            h = getattr(owner, "height", None)
            if isinstance(h, int):
                return h
        h = getattr(self.bc, "height", None)
        if callable(h):
            try:
                h = h()
            except Exception:
                h = None
        return h if isinstance(h, int) else 0

    @staticmethod
    def _signer_of(block):
        for owner in (block, getattr(block, "header", None)):
            if owner is None:
                continue
            for attr in ("miner", "miner_address", "coinbase_address",
                         "validator", "proposer"):
                v = getattr(owner, attr, None)
                if isinstance(v, str) and v:
                    return v
        return None

    # ------------------------------------------------- chain listener API
    def on_connect(self, block):
        """Called for every connected block.  Report-only, never raises."""
        try:
            h = self._height_of(block)
            with self._lock:
                self.stats_["blocks_connected"] += 1
                self.stats_["last_height"] = h
                signer = self._signer_of(block)
                if signer:
                    self._record_signer(h, signer)
                self.events.append(("block", _g31_time.time(), h))
        except Exception as e:
            self._fail("on_connect", e)

    def on_reorg(self, old, new, ancestor_height):
        """Chain reorganised: undo the per-height validator counters."""
        try:
            with self._lock:
                self.stats_["reorgs"] += 1
                for h in [x for x in self._signer_by_height
                          if x > ancestor_height]:
                    addr = self._signer_by_height.pop(h)
                    v = self.validators.get(addr)
                    if v is not None and v.blocks_signed > 0:
                        v.blocks_signed -= 1
                self.events.append(("reorg", _g31_time.time(), ancestor_height))
        except Exception as e:
            self._fail("on_reorg", e)

    def _record_signer(self, height: int, address: str):
        v = self.validators.get(address)
        if v is None:
            v = ValidatorInfo(address=address, total_stake=0)
            self.validators[address] = v
        v.blocks_signed += 1
        self._signer_by_height[height] = address
        while len(self._signer_by_height) > self.SIGNER_CAP:
            self._signer_by_height.popitem(last=False)

    def detach(self):
        try:
            bc = self.bc
            if bc is not None and hasattr(bc, "remove_listener"):
                bc.remove_listener(self)
            elif bc is not None and hasattr(bc, "_listeners"):
                bc._listeners.remove(self)
        except ValueError:
            _NB_SWALLOW_LOG.debug("swallowed ValueError in Layer31.detach", exc_info=True)
        except Exception as e:
            self._fail("detach", e)
        with _G31_LOCK:
            if self in _G31_ACTIVE:
                _G31_ACTIVE.remove(self)

    # -------------------------------------------------- mempool counter
    def on_tx_submitted(self, tx, result):
        """Called after Mempool.submit(tx).  Counts only, never rejects."""
        try:
            with self._lock:
                self.stats_["txs_seen"] += 1
                accepted = result[0] if isinstance(result, tuple) and result else bool(result)
                if accepted:
                    self.stats_["txs_accepted"] += 1
                outs = getattr(tx, "outputs", None)
                if outs is not None and len(outs) >= 3:
                    self.stats_["batch_like_txs"] += 1
        except Exception as e:
            self._fail("on_tx_submitted", e)

    # --------------------------------------------------------- factories
    def new_batcher(self, wallet, fee_estimator=None):
        """TxBatcher bound to this node's blockchain."""
        return TxBatcher(wallet, self.bc, fee_estimator)

    def get_lending_pool(self, asset: str, create: bool = True):
        with self._lock:
            p = self.lending.get(asset)
            if p is None and create:
                if len(self.lending) >= self.POOL_CAP:
                    raise ValueError("lending pool cap reached")
                p = LendingPool(asset=asset)
                self.lending[asset] = p
            return p

    def track_validator(self, address: str, total_stake: int, **kw):
        """Create / update a ValidatorInfo (report-only, no consensus effect)."""
        with self._lock:
            v = self.validators.get(address)
            if v is None:
                v = ValidatorInfo(address=address, total_stake=total_stake, **kw)
                self.validators[address] = v
            else:
                v.total_stake = total_stake
                for k, val in kw.items():
                    if hasattr(v, k):
                        setattr(v, k, val)
            return v

    # ----------------------------------------------------------- reports
    def _safe_report(self, label, fn):
        try:
            return fn()
        except Exception as e:
            self._fail(f"report:{label}", e)
            return {"error": f"{type(e).__name__}: {e}"}

    def report(self) -> dict:
        with self._lock:
            stats = dict(self.stats_)
        return {
            "errors":     self.errors,
            "last_error": self.last_error,
            "stats":      stats,
            "dex":        self._safe_report("dex",    self.dex.dex_stats),
            "bridge":     self._safe_report("bridge", self.bridge.bridge_stats),
            "oracle":     self._safe_report("oracle", self.oracle.oracle_stats),
            "farm":       self._safe_report("farm",   self.farm.farm_stats),
            "nft":        self._safe_report("nft",    self.nft.nft_stats),
            "did":        self._safe_report("did",    self.dids.did_stats),
            "coinjoin":   {"sessions": len(self.coinjoin._sessions)},
            "lending":    [p.to_dict() for p in list(self.lending.values())],
            "validators": [v.to_dict() for v in list(self.validators.values())],
        }

    def connected_classes(self) -> dict:
        """Proof table: class name -> how the Layer reaches it."""
        return {
            "ValidatorInfo":        "Layer31.validators / track_validator()",
            "NBLNFTToken":          "Layer31.nft (NBL721Registry.mint)",
            "NBL721Registry":       "Layer31.nft",
            "BridgeRequest":        "Layer31.bridge (BridgeEngine.initiate_bridge_in)",
            "WrappedToken":         "Layer31.bridge (BridgeEngine.register_wrapped)",
            "OracleNode":           "Layer31.oracle (DecentralizedOracle.register_node)",
            "LendingPool":          "Layer31.lending / get_lending_pool()",
            "FarmingPool":          "Layer31.farm (YieldFarm.add_pool)",
            "UserFarmInfo":         "Layer31.farm (YieldFarm.stake)",
            "DIDDocument":          "Layer31.dids (DIDRegistry.create_did)",
            "VerifiableCredential": "Layer31.dids (DIDRegistry.issue_credential)",
            "NEBULADex":            "Layer31.dex",
            "BridgeEngine":         "Layer31.bridge",
            "TxBatcher":            "Layer31.new_batcher() / wallet.group31.batcher()",
            "StealthAddressScheme": "Layer31.stealth / wallet.group31.stealth_*",
            "CoinJoinCoordinator":  "Layer31.coinjoin (shared with wallets)",
            "DecentralizedOracle":  "Layer31.oracle",
            "YieldFarm":            "Layer31.farm",
            "DIDRegistry":          "Layer31.dids",
            "ShamirSecretSharing":  "Layer31.shamir / wallet.group31.split_secret()",
        }


# ----------------------------------------------------------------------
#  WalletServices31  -  wallet side (wallet.group31)
# ----------------------------------------------------------------------
class WalletServices31:
    """Wallet-side services: batching, stealth addresses, CoinJoin, Shamir."""

    def __init__(self, wallet):
        self.wallet = wallet
        self.errors = 0

    def batcher(self, blockchain=None, fee_estimator=None):
        if blockchain is None:
            layer = _g31_active_layer()
            blockchain = layer.bc if layer is not None else None
        return TxBatcher(self.wallet, blockchain, fee_estimator)

    # --- stealth ---
    def stealth_keys(self):
        return StealthAddressScheme.generate_stealth_keys()

    def stealth_pay_address(self, scan_pub: bytes, spend_pub: bytes):
        return StealthAddressScheme.derive_payment_address(scan_pub, spend_pub)

    def stealth_check(self, scan_priv: int, spend_priv: int,
                      R_bytes: bytes, address: str):
        return StealthAddressScheme.check_payment(scan_priv, spend_priv,
                                                  R_bytes, address)

    # --- coinjoin (shared coordinator) ---
    def coinjoin(self):
        return _g31_shared_coinjoin()

    # --- shamir ---
    def split_secret(self, secret: int, k: int, n: int):
        return ShamirSecretSharing.split(secret, k, n)

    def recover_secret(self, shares):
        return ShamirSecretSharing.reconstruct(shares)


# ----------------------------------------------------------------------
#  REST routes (read-only GET) - registered into the host's _routes table
# ----------------------------------------------------------------------
def _g31_reply(fn):
    def handler(path, query, body):
        layer = _g31_active_layer()
        if layer is None:
            return 503, {"success": False, "error": "group31 not installed"}
        try:
            return 200, {"success": True, "data": fn(layer, query or {})}
        except Exception as e:
            layer._fail(f"route:{path}", e)
            return 500, {"success": False, "error": f"{type(e).__name__}: {e}"}
    return handler


def _g31_q(query, key, default=None):
    v = query.get(key, default) if isinstance(query, dict) else default
    if isinstance(v, (list, tuple)):
        return v[0] if v else default
    return v


def _g31_route_table():
    return {
        "/api/group31/status":     lambda L, q: L.report(),
        "/api/group31/classes":    lambda L, q: L.connected_classes(),
        "/api/group31/dex":        lambda L, q: {"stats": L.dex.dex_stats(),
                                                 "pools": L.dex.list_pools(),
                                                 "pairs": L.dex.list_pairs()},
        "/api/group31/bridge":     lambda L, q: {"stats": L.bridge.bridge_stats(),
                                                 "wrapped": L.bridge.list_wrapped()},
        "/api/group31/oracle":     lambda L, q: ({"feed": L.oracle.get_feed(_g31_q(q, "pair"))}
                                                 if _g31_q(q, "pair") else L.oracle.oracle_stats()),
        "/api/group31/farm":       lambda L, q: L.farm.farm_stats(),
        "/api/group31/nft":        lambda L, q: {"stats": L.nft.nft_stats(),
                                                 "listings": L.nft.marketplace_listings()},
        "/api/group31/did":        lambda L, q: L.dids.did_stats(),
        "/api/group31/lending":    lambda L, q: [p.to_dict() for p in list(L.lending.values())],
        "/api/group31/validators": lambda L, q: [v.to_dict() for v in list(L.validators.values())],
        "/api/group31/coinjoin":   lambda L, q: {"sessions": len(L.coinjoin._sessions)},
    }


# ----------------------------------------------------------------------
#  install / uninstall
# ----------------------------------------------------------------------
def _g31_resolve_host(host=None):
    if host is not None:
        return host
    m = _g31_sys.modules.get("__main__")
    if m is not None and hasattr(m, "NEBULAFullNode"):
        return m
    m = _g31_sys.modules.get("nebula_v10_11")
    if m is not None:
        return m
    import nebula_v10_11 as m          # may take several seconds
    return m


def install(host=None) -> dict:
    """Patch the host.  Safe to call twice.  Returns what was patched."""
    host = _g31_resolve_host(host)
    done = {"node_init": False, "mempool_submit": False,
            "wallet_init": False, "routes": 0}

    # --- 1) NEBULAFullNode.__init__  ->  node.group31 = Layer31(node)
    node_cls = getattr(host, "NEBULAFullNode", None)
    if node_cls is None:
        raise RuntimeError("host has no NEBULAFullNode")
    if not getattr(node_cls, "_g31_orig_init", None):
        orig_init = node_cls.__init__

        @_g31_functools.wraps(orig_init)
        def patched_init(self, *a, **k):
            orig_init(self, *a, **k)
            try:
                layer = Layer31(self)
                self.group31 = layer
                with _G31_LOCK:
                    _G31_ACTIVE.append(layer)
                if layer.bc is not None and hasattr(layer.bc, "add_listener"):
                    layer.bc.add_listener(layer)
            except Exception as e:                      # node must still start
                self.group31_error = e

        node_cls._g31_orig_init = orig_init
        node_cls.__init__ = patched_init
        done["node_init"] = True

    # --- 2) Mempool.submit  ->  count only, result unchanged
    mp_cls = getattr(host, "Mempool", None)
    if mp_cls is not None and hasattr(mp_cls, "submit") \
            and not getattr(mp_cls, "_g31_orig_submit", None):
        orig_submit = mp_cls.submit

        @_g31_functools.wraps(orig_submit)
        def patched_submit(self, *a, **k):
            res = orig_submit(self, *a, **k)
            try:
                tx = a[0] if a else k.get("tx")
                with _G31_LOCK:
                    layers = list(_G31_ACTIVE)
                for layer in layers:
                    mp = getattr(layer.bc, "mempool", None)
                    if mp is not None and mp is not self:
                        continue
                    layer.on_tx_submitted(tx, res)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in install.patched_submit", exc_info=True)
            return res                                  # never altered

        mp_cls._g31_orig_submit = orig_submit
        mp_cls.submit = patched_submit
        done["mempool_submit"] = True

    # --- 3) NEBULAWallet.__init__  ->  wallet.group31 = WalletServices31
    w_cls = getattr(host, "NEBULAWallet", None)
    if w_cls is not None and not getattr(w_cls, "_g31_orig_init", None):
        orig_w = w_cls.__init__

        @_g31_functools.wraps(orig_w)
        def patched_w(self, *a, **k):
            orig_w(self, *a, **k)
            try:
                self.group31 = WalletServices31(self)
            except Exception as e:
                self.group31_error = e

        w_cls._g31_orig_init = orig_w
        w_cls.__init__ = patched_w
        done["wallet_init"] = True

    # --- 4) REST routes (read-only GET)
    routes = getattr(host, "_routes", None)
    if isinstance(routes, dict):
        table = routes.setdefault("GET", {})
        for path, fn in _g31_route_table().items():
            if path in table and path not in _G31_ROUTES:
                continue                                # never override host routes
            h = _g31_reply(fn)
            table[path] = h
            _G31_ROUTES[path] = h
            done["routes"] += 1
    return done


def uninstall(host=None) -> dict:
    """Restore every original host method and remove our routes."""
    host = _g31_resolve_host(host)
    undone = {"node_init": False, "mempool_submit": False,
              "wallet_init": False, "routes": 0}

    node_cls = getattr(host, "NEBULAFullNode", None)
    o = getattr(node_cls, "_g31_orig_init", None) if node_cls else None
    if o:
        node_cls.__init__ = o
        del node_cls._g31_orig_init
        undone["node_init"] = True

    mp_cls = getattr(host, "Mempool", None)
    o = getattr(mp_cls, "_g31_orig_submit", None) if mp_cls else None
    if o:
        mp_cls.submit = o
        del mp_cls._g31_orig_submit
        undone["mempool_submit"] = True

    w_cls = getattr(host, "NEBULAWallet", None)
    o = getattr(w_cls, "_g31_orig_init", None) if w_cls else None
    if o:
        w_cls.__init__ = o
        del w_cls._g31_orig_init
        undone["wallet_init"] = True

    routes = getattr(host, "_routes", None)
    if isinstance(routes, dict):
        table = routes.get("GET", {})
        for path, h in list(_G31_ROUTES.items()):
            if table.get(path) is h:
                del table[path]
                undone["routes"] += 1
    _G31_ROUTES.clear()

    with _G31_LOCK:
        layers = list(_G31_ACTIVE)
    for layer in layers:
        layer.detach()
    return undone


# ----------------------------------------------------------------------
#  Self check (python3 nebula_group31_wired.py)
# ----------------------------------------------------------------------
def self_check() -> dict:
    """True for every group31 class that exists in this module."""
    g = globals()
    return {name: isinstance(g.get(name), type) for name in GROUP31_CLASS_NAMES}


if __name__ == "__main__":
    res = self_check()
    bad = [k for k, v in res.items() if not v]
    print(f"group31 classes present: {sum(res.values())}/{len(res)}")
    if bad:
        print("MISSING:", ", ".join(bad))
        raise SystemExit(1)
    print("OK - now call install(host) from your launcher.")
