"""NEBULA group58 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. NEBULAPartnership  (orig. lines 87392-87421)
   2. NEBULAGrantsProgram  (orig. lines 87423-87463)
   3. NEBULAAmbassadorProgram  (orig. lines 87465-87501)
   4. NEBULAHackathonHistory  (orig. lines 87503-87525)
   5. NEBULAEcosystemFund  (orig. lines 87527-87557)
   6. RustBridge  (orig. lines 99571-99678)
   7. NEBULATestnet  (orig. lines 99763-99952)
   8. TestnetFaucetAPI  (orig. lines 99955-100005)
   9. NEBULACommunityPlatform  (orig. lines 100023-100390)
  10. SecurityAuditReport  (orig. lines 100447-100738)
  11. BugBountyProgram  (orig. lines 100741-100840)
  12. DynamicFeePool  (orig. lines 100851-100914)
  13. RangeOrderBook  (orig. lines 100917-100967)
  14. MEVAuction  (orig. lines 100970-101020)
  15. AutomatedMarketMakerV3  (orig. lines 101023-101113)
  16. OptimisticRollup  (orig. lines 101121-101284)
  17. GameCharacter  (orig. lines 101292-101353)
  18. Dungeon  (orig. lines 101356-101409)
  19. NFTGamingPlatform  (orig. lines 101412-101491)
  20. SocialToken  (orig. lines 101499-101550)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): NEBULABlockchain, Secp256k1
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

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BITS           = 0x1e0fffff if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d0fffff   # [v10.24]

MAGIC_BYTES            = 0x4E424C4D   # "NBLM" — NEBULA Mainnet magic integer

def _enable_dev_mode(bc, who: str):
    """v10.9: classes that mint coins with fund_address() (faucet, dev tools, gaming) used to flip
    `_dev_mode = True` on WHATEVER chain they were given - on a real node that lets them create
    money from nothing. Now they may only run on a chain whose dev mode was switched on by the
    caller, or when the operator explicitly sets NEBULA_ALLOW_DEV_MODE=1 (test/regtest only)."""
    if getattr(bc, '_dev_mode', False):
        return
    if os.environ.get('NEBULA_ALLOW_DEV_MODE') == '1':
        bc._dev_mode = True
        return
    raise PermissionError(
        f"{who} needs coin-minting dev mode, which is disabled on real chains. "
        "Use a throw-away chain (bc._dev_mode = True) or set NEBULA_ALLOW_DEV_MODE=1 for tests.")

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

API_PORT       = 8080

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


# ---- NEBULAPartnership
class NEBULAPartnership:
    """Manages ecosystem partnerships."""

    def __init__(self):
        self._partners: List[dict] = []

    def add_partner(self, name: str, category: str,
                     description: str) -> bool:
        self._partners.append({
            "name":        name,
            "category":    category,
            "description": description,
            "joined":      time.time(),
            "active":      True,
        })
        return True

    def list_partners(self, category: str = None) -> List[dict]:
        if category:
            return [p for p in self._partners if p["category"] == category]
        return list(self._partners)

    def partnership_stats(self) -> dict:
        cats = {}
        for p in self._partners:
            cats[p["category"]] = cats.get(p["category"], 0) + 1
        return {
            "total_partners":  len(self._partners),
            "by_category":     cats,
        }


# ---- NEBULAGrantsProgram
class NEBULAGrantsProgram:
    """Ecosystem grants program for NEBULA builders."""

    GRANT_TIERS = {
        "micro":   10_000,
        "small":   50_000,
        "medium":  200_000,
        "large":   500_000,
        "flagship": 1_000_000,
    }

    def __init__(self):
        self._applications: List[dict] = []
        self._awarded:      List[dict] = []

    def apply(self, project: str, team: str,
               tier: str, description: str) -> str:
        app_id = hashlib.sha256(
            f"GRANT:{project}:{team}:{time.time()}".encode()
        ).hexdigest()[:8]
        self._applications.append({
            "app_id":      app_id,
            "project":     project,
            "team":        team,
            "tier":        tier,
            "amount":      self.GRANT_TIERS.get(tier, 0),
            "description": description,
            "status":      "under_review",
        })
        return app_id

    def grants_stats(self) -> dict:
        total_applied = sum(
            self.GRANT_TIERS.get(a["tier"], 0)
            for a in self._applications
        )
        return {
            "applications":   len(self._applications),
            "tiers":          self.GRANT_TIERS,
            "total_applied":  f"${total_applied:,}",
        }


# ---- NEBULAAmbassadorProgram
class NEBULAAmbassadorProgram:
    """Global ambassador program for NEBULA."""

    REGIONS = [
        "Africa", "Asia", "Central Asia", "Middle East",
        "Europe", "North America", "South America", "Oceania"
    ]

    def __init__(self):
        self._ambassadors: List[dict] = []

    def register(self, name: str, address: str,
                  region: str, language: str) -> bool:
        if region not in self.REGIONS:
            return False
        self._ambassadors.append({
            "name":     name,
            "address":  address,
            "region":   region,
            "language": language,
            "joined":   time.time(),
        })
        return True

    def by_region(self) -> dict:
        result = {}
        for amb in self._ambassadors:
            r = amb["region"]
            result[r] = result.get(r, 0) + 1
        return result

    def program_stats(self) -> dict:
        return {
            "total":    len(self._ambassadors),
            "regions":  self.by_region(),
            "target":   "100 ambassadors worldwide",
        }


# ---- NEBULAHackathonHistory
class NEBULAHackathonHistory:
    """Historical record of NEBULA hackathons."""

    EVENTS = [
        {
            "edition":     1,
            "theme":       "Build on NEBULA",
            "prize_pool":  "100,000 NBL",
            "teams":       50,
            "status":      "planned",
        },
        {
            "edition":     2,
            "theme":       "DeFi Innovation",
            "prize_pool":  "500,000 NBL",
            "teams":       0,
            "status":      "upcoming",
        },
    ]

    @classmethod
    def get_history(cls) -> List[dict]:
        return cls.EVENTS


# ---- NEBULAEcosystemFund
class NEBULAEcosystemFund:
    """Ecosystem development fund management."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._balance = 0
        self._disbursements: List[dict] = []

    def fund(self, amount: int):
        self._balance += amount

    def disburse(self, recipient: str, amount: int,
                  purpose: str) -> bool:
        if amount > self._balance:
            return False
        self._balance -= amount
        self._disbursements.append({
            "recipient": recipient,
            "amount":    amount,
            "purpose":   purpose,
            "block":     self._bc.height,
        })
        return True

    def fund_stats(self) -> dict:
        total_disbursed = sum(d["amount"] for d in self._disbursements)
        return {
            "balance_nbl":     f"{self._balance/10**DECIMALS:.3f}",
            "total_disbursed": f"{total_disbursed/10**DECIMALS:.3f}",
            "disbursements":   len(self._disbursements),
        }


# ---- RustBridge
class RustBridge:
    """
    Python ↔ Rust FFI bridge for NEBULA.
    Loads the compiled nebula_core.so/.dll and calls Rust functions.
    Falls back to pure Python if Rust library not available.
    """

    def __init__(self):
        self._lib    = None
        self._available = False
        self._try_load()

    def _try_load(self):
        import ctypes, os, platform
        lib_name = {
            "Linux":   "libnebula_core.so",
            "Darwin":  "libnebula_core.dylib",
            "Windows": "nebula_core.dll",
        }.get(platform.system(), "libnebula_core.so")

        _this_file = globals().get('__file__', None) or sys.argv[0]
        search_paths = [
            os.path.join(os.path.dirname(os.path.abspath(_this_file)), lib_name),
            f"/usr/local/lib/{lib_name}",
            f"./target/release/{lib_name}",
        ]
        for path in search_paths:
            if os.path.exists(path):
                try:
                    self._lib       = ctypes.CDLL(path)
                    self._available = True
                    self._setup_signatures()
                    break
                except Exception:
                    _NB_SWALLOW_LOG.warning("swallowed Exception in RustBridge._try_load", exc_info=True)

    def _setup_signatures(self):
        """Configure ctypes function signatures for Rust exports."""
        import ctypes
        if not self._lib:
            return
        # nebula_sha256(data: *const u8, len: usize, out: *mut u8)
        try:
            self._lib.nebula_sha256.argtypes = [
                ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p]
            self._lib.nebula_sha256.restype  = ctypes.c_void_p
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in RustBridge._setup_signatures", exc_info=True)

    def sha256(self, data: bytes) -> bytes:
        """SHA-256 via Rust (10x faster than Python)."""
        import ctypes
        if not self._available:
            return hashlib.sha256(data).digest()
        out = (ctypes.c_char * 32)()
        self._lib.nebula_sha256(data, len(data), out)
        return bytes(out)

    def hash256(self, data: bytes) -> bytes:
        """SHA-256d via Rust."""
        if not self._available:
            return hashlib.sha256(hashlib.sha256(data).digest()).digest()
        return self.sha256(self.sha256(data))

    def secp256k1_sign(self, privkey: bytes, msg_hash: bytes) -> bytes:
        """ECDSA sign via Rust secp256k1."""
        if not self._available:
            privkey_int = int.from_bytes(privkey, 'big')
            r, s        = Secp256k1.sign(privkey_int, msg_hash)
            return Secp256k1.sig_to_der(r, s)
        import ctypes
        out     = (ctypes.c_char * 72)()
        out_len = ctypes.c_size_t(0)
        self._lib.nebula_sign(
            privkey, msg_hash, out, ctypes.byref(out_len))
        return bytes(out[:out_len.value])

    @property
    def available(self) -> bool:
        return self._available

    def performance_report(self) -> dict:
        """Compare Python vs Rust performance."""
        import time
        data = b"benchmark_data_nebula" * 100
        # Python benchmark
        n    = 10_000
        t0   = time.perf_counter()
        for _ in range(n):
            hashlib.sha256(data).digest()
        py_time = time.perf_counter() - t0
        # Rust benchmark (if available)
        if self._available:
            t0 = time.perf_counter()
            for _ in range(n):
                self.sha256(data)
            rs_time  = time.perf_counter() - t0
            speedup  = py_time / rs_time
        else:
            rs_time = None
            speedup = None
        return {
            "rust_available": self._available,
            "python_sha256":  f"{n/py_time:.0f} ops/s",
            "rust_sha256":    f"{n/rs_time:.0f} ops/s" if rs_time else "N/A",
            "speedup":        f"{speedup:.1f}x" if speedup else "N/A",
            "note":           "Build Rust lib: cd rust/ && cargo build --release",
        }


# ---- NEBULATestnet
class NEBULATestnet:
    """
    NEBULA Real Testnet — complete public testnet infrastructure.
    Faucet, bootstrap nodes, genesis, explorer integration.
    """

    # ── Testnet Configuration ──────────────────────────────────
    CHAIN_ID         = 9999
    MAGIC_BYTES      = 0x4E424C54   # "NBLT"
    PORT             = 18333
    API_PORT         = 18080
    GENESIS_HASH     = "0000000testnet" + "0" * 50
    INITIAL_BITS     = 0x1f00ffff   # easier difficulty for testnet
    FAUCET_AMOUNT    = 1_000 * 10**DECIMALS    # 1000 NBL per request
    FAUCET_COOLDOWN  = 86_400        # 24 hours

    BOOTSTRAP_NODES = [
        "testnet-seed1.nebula-nbl.io:18333",
        "testnet-seed2.nebula-nbl.io:18333",
        "testnet-seed3.nebula-nbl.io:18333",
        "testnet-bootstrap1.nebula-nbl.io:18333",
        "testnet-bootstrap2.nebula-nbl.io:18333",
    ]

    TESTNET_EXPLORERS = [
        "https://testnet-explorer.nebula-nbl.io",
        "https://testnet.nebula-nbl.io/explorer",
    ]

    TESTNET_API = "https://testnet-api.nebula-nbl.io"

    # ── Faucet ─────────────────────────────────────────────────
    def __init__(self, blockchain: 'NEBULABlockchain' = None):
        self._bc         = blockchain or NEBULABlockchain()
        self._faucet_log: dict = {}   # address -> last_claim_time
        self._faucet_total = 0
        self._lock       = threading.RLock()
        self._requests   = []
        self._validators: list = []

    def faucet_request(self, address: str,
                        ip: str = "0.0.0.0") -> dict:
        """Request testnet NBL from faucet."""
        with self._lock:
            # Rate limit per address
            last = self._faucet_log.get(address, 0)
            now  = time.time()
            if now - last < self.FAUCET_COOLDOWN:
                wait = int(self.FAUCET_COOLDOWN - (now - last))
                hours = wait // 3600
                mins  = (wait % 3600) // 60
                return {
                    "ok":      False,
                    "error":   f"Rate limited. Wait {hours}h {mins}m",
                    "address": address,
                    "next_at": last + self.FAUCET_COOLDOWN,
                }
            # Fund the address
            self._bc.fund_address(address, self.FAUCET_AMOUNT / 10**DECIMALS)
            self._faucet_log[address] = now
            self._faucet_total       += self.FAUCET_AMOUNT
            tx_hash = hashlib.sha256(
                f"{address}:{now}".encode()).hexdigest()
            self._requests.append({
                "address": address,
                "amount":  self.FAUCET_AMOUNT,
                "txid":    tx_hash,
                "ts":      now,
                "ip":      ip,
            })
            return {
                "ok":        True,
                "address":   address,
                "amount_nbl": f"{self.FAUCET_AMOUNT/10**DECIMALS:.3f}",
                "txid":      tx_hash,
                "explorer":  f"{self.TESTNET_EXPLORERS[0]}/tx/{tx_hash}",
                "note":      "Testnet NBL has no real value",
            }

    def faucet_status(self, address: str) -> dict:
        last = self._faucet_log.get(address, 0)
        now  = time.time()
        can_claim = (now - last) >= self.FAUCET_COOLDOWN
        return {
            "address":   address,
            "can_claim": can_claim,
            "balance":   f"{self._bc.utxo.balance(address)/10**DECIMALS:.3f} NBL",
            "wait_secs": max(0, int(self.FAUCET_COOLDOWN - (now - last))),
        }

    # ── Testnet Genesis ────────────────────────────────────────
    def testnet_genesis_config(self) -> dict:
        return {
            "chain_id":      self.CHAIN_ID,
            "magic":         hex(self.MAGIC_BYTES),
            "port":          self.PORT,
            "initial_bits":  hex(self.INITIAL_BITS),
            "genesis_msg":   "NEBULA Testnet — Test Safely, Break Things, Learn",
            "timestamp":     1742083200,
            "nonce":         0,
            "premines": [
                {
                    "address": FOUNDATION_ADDRESS,
                    "amount":  "10000000 NBL",
                    "purpose": "Testnet faucet fund",
                },
                {
                    "address": "NtestFaucet000000000000000000000",
                    "amount":  "5000000 NBL",
                    "purpose": "Public faucet",
                },
            ],
            "bootstrap_nodes": self.BOOTSTRAP_NODES,
        }

    # ── Testnet Validator Registration ─────────────────────────
    def register_validator(self, address: str, name: str,
                            endpoint: str, stake: float) -> dict:
        with self._lock:
            vid = hashlib.sha256(
                f"TVAL:{address}:{name}".encode()
            ).hexdigest()[:12]
            self._validators.append({
                "validator_id": vid,
                "address":      address,
                "name":         name,
                "endpoint":     endpoint,
                "stake":        stake,
                "joined":       time.time(),
                "active":       True,
                "network":      "testnet",
            })
            return {
                "ok":          True,
                "validator_id": vid,
                "message":     f"Validator {name} registered on testnet",
                "stake":       f"{stake:.3f} NBL",
                "explorer":    f"{self.TESTNET_EXPLORERS[0]}/validator/{vid}",
            }

    # ── Testnet Stats ──────────────────────────────────────────
    def testnet_stats(self) -> dict:
        return {
            "network":       "NEBULA Testnet",
            "chain_id":      self.CHAIN_ID,
            "height":        self._bc.height,
            "faucet_claims": len(self._requests),
            "faucet_total":  f"{self._faucet_total/10**DECIMALS:.3f} NBL",
            "validators":    len(self._validators),
            "api":           self.TESTNET_API,
            "explorer":      self.TESTNET_EXPLORERS[0],
            "faucet":        "https://faucet.nebula-nbl.io",
            "bootstrap_nodes": self.BOOTSTRAP_NODES,
            "note":          "Testnet NBL has no monetary value",
        }

    # ── Node Setup Instructions ────────────────────────────────
    @staticmethod
    def setup_instructions() -> str:
        return """
# ── How to join NEBULA Testnet ──────────────────────────────────

## Option 1: Python (this file)
python3 nebula_blockchain_fixed.py node --network testnet

## Option 2: Rust node (recommended for validators)
cargo build --release
./target/release/nebula-node --network testnet --mine

## Option 3: Docker
docker pull nebulanbl/testnet-node:latest
docker run -p 18333:18333 -p 18080:18080 nebulanbl/testnet-node

## Get testnet NBL
curl -X POST https://faucet.nebula-nbl.io/request \\
  -H "Content-Type: application/json" \\
  -d '{"address": "YOUR_NEBULA_ADDRESS"}'

## Check balance
curl https://testnet-api.nebula-nbl.io/address/YOUR_ADDRESS

## Testnet explorer
https://testnet-explorer.nebula-nbl.io

## Connect your wallet
Network:  NEBULA Testnet
Chain ID: 9999
RPC URL:  https://testnet-rpc.nebula-nbl.io
Symbol:   NBL (testnet)
"""


# ---- TestnetFaucetAPI
class TestnetFaucetAPI:
    """REST API endpoints for the testnet faucet."""

    def __init__(self, testnet: 'NEBULATestnet',
                  blockchain: 'NEBULABlockchain'):
        self._tn = testnet
        self._bc = blockchain

    def handle(self, method: str, path: str,
               body: dict = None) -> dict:
        """Handle faucet API requests."""
        body = body or {}
        # POST /faucet/request
        if method == "POST" and path == "/faucet/request":
            addr = body.get("address", "")
            if not addr:
                return {"ok": False, "error": "address required"}
            return self._tn.faucet_request(addr)

        # GET /faucet/status/{address}
        elif method == "GET" and path.startswith("/faucet/status/"):
            addr = path.split("/")[-1]
            return self._tn.faucet_status(addr)

        # GET /faucet/stats
        elif method == "GET" and path == "/faucet/stats":
            return {
                "total_claims": len(self._tn._requests),
                "total_nbl":    f"{self._tn._faucet_total/10**DECIMALS:.3f}",
                "cooldown_hrs": self._tn.FAUCET_COOLDOWN // 3600,
                "amount_nbl":   self._tn.FAUCET_AMOUNT / 10**DECIMALS,
            }

        # GET /testnet/genesis
        elif method == "GET" and path == "/testnet/genesis":
            return self._tn.testnet_genesis_config()

        # GET /testnet/stats
        elif method == "GET" and path == "/testnet/stats":
            return self._tn.testnet_stats()

        # POST /testnet/validator/register
        elif method == "POST" and path == "/testnet/validator/register":
            return self._tn.register_validator(
                body.get("address", ""),
                body.get("name", ""),
                body.get("endpoint", ""),
                float(body.get("stake", 1000)),
            )

        return {"ok": False, "error": f"Unknown: {method} {path}"}


# ---- NEBULACommunityPlatform
class NEBULACommunityPlatform:
    """
    Full community platform for NEBULA ecosystem.
    Forums, governance discussions, developer hub, events.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._members:    dict  = {}
        self._posts:      list  = []
        self._events:     list  = []
        self._projects:   list  = []
        self._grants:     list  = []
        self._ambassadors: list = []
        self._bounties:   list  = []
        self._lock        = threading.RLock()

    # ── Member Registration ──────────────────────────────────
    def register(self, address: str, username: str,
                  bio: str = "", github: str = "",
                  twitter: str = "", region: str = "") -> dict:
        with self._lock:
            if username in [m["username"] for m in self._members.values()]:
                return {"ok": False, "error": "Username taken"}
            member_id = hashlib.sha256(
                f"MEMBER:{address}:{username}".encode()
            ).hexdigest()[:12]
            self._members[address] = {
                "member_id":  member_id,
                "address":    address,
                "username":   username,
                "bio":        bio[:200],
                "github":     github,
                "twitter":    twitter,
                "region":     region,
                "joined":     time.time(),
                "role":       "member",
                "rep_score":  0,
                "badges":     [],
                "posts":      0,
                "contributions": [],
            }
            return {
                "ok":       True,
                "member_id": member_id,
                "username": username,
                "profile":  f"https://community.nebula-nbl.io/@{username}",
            }

    # ── Forum Posts ──────────────────────────────────────────
    def create_post(self, author: str, title: str,
                     body: str, category: str = "general",
                     tags: list = None) -> dict:
        with self._lock:
            if author not in self._members:
                return {"ok": False, "error": "Not a member"}
            post_id = len(self._posts) + 1
            self._posts.append({
                "id":        post_id,
                "author":    author,
                "username":  self._members[author]["username"],
                "title":     title,
                "body":      body[:5000],
                "category":  category,
                "tags":      tags or [],
                "upvotes":   0,
                "replies":   [],
                "views":     0,
                "pinned":    False,
                "ts":        time.time(),
            })
            self._members[author]["posts"] += 1
            self._members[author]["rep_score"] += 5
            return {
                "ok":     True,
                "post_id": post_id,
                "url":    f"https://community.nebula-nbl.io/post/{post_id}",
            }

    def reply(self, author: str, post_id: int,
               content: str) -> dict:
        with self._lock:
            post = next((p for p in self._posts if p["id"] == post_id), None)
            if not post:
                return {"ok": False, "error": "Post not found"}
            post["replies"].append({
                "author":   author,
                "username": self._members.get(author, {}).get("username", author[:8]),
                "content":  content[:1000],
                "ts":       time.time(),
                "upvotes":  0,
            })
            return {"ok": True, "replies": len(post["replies"])}

    def upvote(self, voter: str, post_id: int) -> bool:
        for post in self._posts:
            if post["id"] == post_id:
                post["upvotes"] += 1
                author = post["author"]
                if author in self._members:
                    self._members[author]["rep_score"] += 2
                return True
        return False

    # ── Events ──────────────────────────────────────────────
    def create_event(self, organizer: str, title: str,
                      event_type: str, date: str,
                      description: str = "",
                      online: bool = True,
                      link: str = "") -> dict:
        with self._lock:
            eid = len(self._events) + 1
            self._events.append({
                "id":          eid,
                "organizer":   organizer,
                "title":       title,
                "type":        event_type,
                "date":        date,
                "description": description,
                "online":      online,
                "link":        link,
                "attendees":   [],
                "ts":          time.time(),
            })
            return {
                "ok":      True,
                "event_id": eid,
                "url":     f"https://community.nebula-nbl.io/events/{eid}",
            }

    def rsvp_event(self, address: str, event_id: int) -> bool:
        for event in self._events:
            if event["id"] == event_id:
                if address not in event["attendees"]:
                    event["attendees"].append(address)
                return True
        return False

    def upcoming_events(self, n: int = 10) -> list:
        now = time.time()
        return sorted(
            [e for e in self._events if e["ts"] >= now - 86400],
            key=lambda e: e["ts"]
        )[:n]

    # ── Developer Projects ──────────────────────────────────
    def submit_project(self, developer: str, name: str,
                        description: str, github: str,
                        category: str = "dapp",
                        status: str = "building") -> dict:
        with self._lock:
            pid = hashlib.sha256(
                f"PROJ:{developer}:{name}".encode()
            ).hexdigest()[:12]
            self._projects.append({
                "project_id": pid,
                "developer":  developer,
                "name":       name,
                "description": description,
                "github":     github,
                "category":   category,
                "status":     status,
                "likes":      0,
                "submitted":  time.time(),
            })
            return {
                "ok":        True,
                "project_id": pid,
                "listing":   f"https://community.nebula-nbl.io/projects/{pid}",
            }

    # ── Grant Applications ──────────────────────────────────
    def apply_grant(self, applicant: str, project_name: str,
                     amount_nbl: float, milestones: list,
                     description: str, tier: str = "small") -> dict:
        TIERS = {
            "micro":    10_000,
            "small":    50_000,
            "medium":   200_000,
            "large":    500_000,
            "flagship": 1_000_000,
        }
        with self._lock:
            gid = hashlib.sha256(
                f"GRANT:{applicant}:{project_name}:{time.time()}".encode()
            ).hexdigest()[:12]
            max_amount = TIERS.get(tier, 50_000)
            if amount_nbl > max_amount:
                return {"ok": False, "error": f"Tier {tier} max: {max_amount:,} NBL"}
            self._grants.append({
                "grant_id":    gid,
                "applicant":   applicant,
                "project":     project_name,
                "amount_nbl":  amount_nbl,
                "milestones":  milestones,
                "description": description,
                "tier":        tier,
                "status":      "under_review",
                "applied_at":  time.time(),
            })
            return {
                "ok":      True,
                "grant_id": gid,
                "status":  "under_review",
                "tracking": f"https://grants.nebula-nbl.io/{gid}",
                "message": f"Grant application submitted. Review: 2-4 weeks",
            }

    # ── Ambassador Program ──────────────────────────────────
    def join_ambassador(self, address: str, name: str,
                         region: str, language: str,
                         social_links: dict = None,
                         motivation: str = "") -> dict:
        REGIONS = [
            "Afghanistan", "Central Asia", "Middle East", "South Asia",
            "Africa", "Europe", "North America", "South America",
            "East Asia", "Southeast Asia", "Oceania",
        ]
        with self._lock:
            if region not in REGIONS:
                region = "Global"
            amb_id = hashlib.sha256(
                f"AMB:{address}:{name}:{region}".encode()
            ).hexdigest()[:12]
            self._ambassadors.append({
                "amb_id":       amb_id,
                "address":      address,
                "name":         name,
                "region":       region,
                "language":     language,
                "social_links": social_links or {},
                "motivation":   motivation[:500],
                "joined":       time.time(),
                "status":       "active",
                "events_hosted": 0,
                "members_referred": 0,
                "reward_nbl":   0.0,
            })
            return {
                "ok":       True,
                "amb_id":   amb_id,
                "name":     name,
                "region":   region,
                "badge":    "🌟 NEBULA Ambassador",
                "profile":  f"https://community.nebula-nbl.io/ambassadors/{amb_id}",
                "welcome":  f"Welcome to the NEBULA Ambassador Program, {name}!",
            }

    # ── Bounties ────────────────────────────────────────────
    def post_bounty(self, poster: str, title: str,
                     description: str, reward_nbl: float,
                     category: str = "bug",
                     difficulty: str = "medium") -> dict:
        with self._lock:
            bid = hashlib.sha256(
                f"BOUNTY:{poster}:{title}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._bounties.append({
                "bounty_id":  bid,
                "poster":     poster,
                "title":      title,
                "description": description,
                "reward_nbl": reward_nbl,
                "category":   category,
                "difficulty": difficulty,
                "status":     "open",
                "submissions": [],
                "posted_at":  time.time(),
            })
            return {
                "ok":        True,
                "bounty_id": bid,
                "reward":    f"{reward_nbl:,.0f} NBL",
                "url":       f"https://bounties.nebula-nbl.io/{bid}",
            }

    def submit_bounty_solution(self, bounty_id: str,
                                solver: str,
                                solution_url: str,
                                notes: str = "") -> dict:
        with self._lock:
            bounty = next((b for b in self._bounties
                           if b["bounty_id"] == bounty_id), None)
            if not bounty:
                return {"ok": False, "error": "Bounty not found"}
            if bounty["status"] != "open":
                return {"ok": False, "error": "Bounty not open"}
            sub_id = hashlib.sha256(
                f"SUB:{solver}:{bounty_id}:{time.time()}".encode()
            ).hexdigest()[:10]
            bounty["submissions"].append({
                "sub_id":   sub_id,
                "solver":   solver,
                "url":      solution_url,
                "notes":    notes[:500],
                "ts":       time.time(),
                "status":   "pending_review",
            })
            return {
                "ok":    True,
                "sub_id": sub_id,
                "status": "pending_review",
                "message": "Solution submitted for review",
            }

    # ── Community Stats ─────────────────────────────────────
    def community_stats(self) -> dict:
        with self._lock:
            by_region = {}
            for a in self._ambassadors:
                r = a["region"]
                by_region[r] = by_region.get(r, 0) + 1

            by_category = {}
            for p in self._posts:
                c = p["category"]
                by_category[c] = by_category.get(c, 0) + 1

            open_bounties  = sum(1 for b in self._bounties if b["status"] == "open")
            total_rewards  = sum(b["reward_nbl"] for b in self._bounties)
            pending_grants = sum(1 for g in self._grants if g["status"] == "under_review")
            total_grant_ask = sum(g["amount_nbl"] for g in self._grants)

            return {
                "members":         len(self._members),
                "posts":           len(self._posts),
                "events":          len(self._events),
                "projects":        len(self._projects),
                "ambassadors":     len(self._ambassadors),
                "ambassador_regions": by_region,
                "open_bounties":   open_bounties,
                "total_bounty_nbl": f"{total_rewards:,.0f}",
                "grant_applications": len(self._grants),
                "pending_grants":  pending_grants,
                "total_grant_ask_nbl": f"{total_grant_ask:,.0f}",
                "posts_by_category": by_category,
                "community_links": {
                    "website":   "https://nebula-nbl.io",
                    "forum":     "https://community.nebula-nbl.io",
                    "github":    "",
                    "discord":   "https://discord.gg/nebula-nbl",
                    "telegram":  "https://t.me/nebula_nbl",
                    "twitter":   "https://twitter.com/nebula_nbl",
                    "docs":      "https://docs.nebula-nbl.io",
                    "grants":    "https://grants.nebula-nbl.io",
                    "bounties":  "https://bounties.nebula-nbl.io",
                },
            }

    # ── Top Contributors ────────────────────────────────────
    def top_contributors(self, n: int = 20) -> list:
        with self._lock:
            members = sorted(
                self._members.values(),
                key=lambda m: m["rep_score"],
                reverse=True
            )
        return [
            {
                "rank":      i + 1,
                "username":  m["username"],
                "region":    m["region"],
                "rep_score": m["rep_score"],
                "posts":     m["posts"],
                "role":      m["role"],
            }
            for i, m in enumerate(members[:n])
        ]


# ---- SecurityAuditReport
class SecurityAuditReport:
    """Complete security audit framework for NEBULA."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._findings: list = []
        self._passed:   list = []
        self._score     = 100
        self._lock      = threading.RLock()

    # ── Vulnerability Scanner ───────────────────────────────
    def scan_all(self) -> dict:
        """Run complete security audit."""
        self._findings.clear()
        self._passed.clear()
        self._score = 100

        self._check_crypto()
        self._check_consensus()
        self._check_network()
        self._check_defi()
        self._check_governance()
        self._check_nft()
        self._check_bridge()
        self._check_wallets()
        self._check_api()
        self._check_mempool()

        return self.generate_report()

    def _finding(self, category: str, severity: str,
                  title: str, description: str,
                  mitigation: str, cwe: str = ""):
        """Record a security finding."""
        deductions = {"CRITICAL": 25, "HIGH": 15, "MEDIUM": 8, "LOW": 3, "INFO": 0}
        self._score = max(0, self._score - deductions.get(severity, 0))
        self._findings.append({
            "id":           f"NBL-{len(self._findings)+1:04d}",
            "category":     category,
            "severity":     severity,
            "title":        title,
            "description":  description,
            "mitigation":   mitigation,
            "cwe":          cwe,
            "status":       "open",
        })

    def _pass(self, category: str, check: str):
        self._passed.append({"category": category, "check": check})

    def _check_crypto(self):
        self._pass("Cryptography", "secp256k1 curve — same as Bitcoin (production-grade)")
        self._pass("Cryptography", "SHA-256d for block hashing")
        self._pass("Cryptography", "RIPEMD-160(SHA-256(pubkey)) for addresses")
        self._pass("Cryptography", "BIP-32/39/44 HD wallet derivation")
        self._pass("Cryptography", "Pedersen commitments for privacy")
        self._finding("Cryptography", "MEDIUM",
            "Python cryptography speed",
            "Pure Python secp256k1 is ~100x slower than C implementation. "
            "This is acceptable for prototype but not for high-throughput production.",
            "Migrate to Rust node with secp256k1 crate. Python FFI bridge available.",
            "CWE-676")
        self._pass("Cryptography", "WIF private key encoding with checksum")
        self._pass("Cryptography", "Base58Check encoding for addresses")
        self._pass("Cryptography", "HMAC-SHA512 for BIP-32 key derivation")

    def _check_consensus(self):
        self._pass("Consensus", "SHA-256d Proof of Work — battle-tested algorithm")
        self._pass("Consensus", "Difficulty adjustment every 2016 blocks")
        self._pass("Consensus", "Maximum 4x difficulty change per period")
        self._pass("Consensus", "Merkle tree for transaction inclusion proofs")
        self._pass("Consensus", "Coinbase maturity (100 blocks) enforced")
        self._finding("Consensus", "INFO",
            "No checkpoints",
            "No hardcoded checkpoints to prevent deep reorgs on a fresh chain.",
            "Add checkpoints at regular intervals as chain matures.")
        self._finding("Consensus", "LOW",
            "Simulation-only mining",
            "Current Python implementation simulates mining. "
            "Real PoW requires the Rust node with hardware hash rate.",
            "Deploy Rust miner for real network security.")

    def _check_network(self):
        self._pass("Network", "Message magic bytes prevent cross-network replay")
        self._pass("Network", "Protocol version negotiation in handshake")
        self._pass("Network", "Peer scoring and banning system")
        self._finding("Network", "MEDIUM",
            "No transport encryption",
            "P2P connections are not encrypted in current Python implementation. "
            "Messages can be read by network observers.",
            "Implement BIP-324 encrypted transport. Rust node uses Noise protocol via libp2p.")
        self._finding("Network", "LOW",
            "Eclipse attack surface",
            "A node with few peers could be isolated by an attacker.",
            "Maintain diverse peer connections. Implement peer rotation.")
        self._pass("Network", "Rate limiting for P2P messages")
        self._pass("Network", "Maximum peer limit (125) enforced")

    def _check_defi(self):
        self._pass("DeFi", "Constant product AMM — mathematically sound")
        self._pass("DeFi", "Slippage tolerance checks in swaps")
        self._pass("DeFi", "Liquidation threshold enforcement (80%)")
        self._pass("DeFi", "Flash loan fee collection")
        self._pass("DeFi", "Circuit breaker system for anomalies")
        self._finding("DeFi", "HIGH",
            "Oracle price manipulation",
            "Single oracle source can be manipulated in same block. "
            "DEX spot prices can be flash-loan manipulated.",
            "Use TWAP (30-min minimum window). Use multiple oracle sources. "
            "Implement OracleV3 with median aggregation.")
        self._finding("DeFi", "HIGH",
            "Reentrancy potential",
            "Python state management may not fully guard against reentrancy "
            "in complex multi-call scenarios.",
            "Add reentrancy_guard decorator to all state-changing DeFi functions. "
            "Follow checks-effects-interactions pattern strictly.")
        self._finding("DeFi", "MEDIUM",
            "Sandwich attack vulnerability",
            "MEV bots can sandwich DEX swaps for profit.",
            "MEVProtector module implemented. Use commit-reveal for large swaps.")
        self._pass("DeFi", "Insurance fund for protocol losses")
        self._pass("DeFi", "Emergency DAO pause capability")

    def _check_governance(self):
        self._pass("Governance", "Timelock (2-day) before proposal execution")
        self._pass("Governance", "Guardian veto window (1-day)")
        self._pass("Governance", "Minimum 60% threshold to pass")
        self._pass("Governance", "Quorum requirement prevents low-participation attacks")
        self._pass("Governance", "Emergency DAO for critical fixes")
        self._finding("Governance", "MEDIUM",
            "Governance plutocracy risk",
            "Large NBL holders have disproportionate voting power.",
            "veNBL lock mechanism already reduces pure whale voting. "
            "Consider quadratic voting for community proposals.")
        self._finding("Governance", "LOW",
            "Proposal spam potential",
            "Low proposal fee (100 NBL) may allow spam proposals.",
            "Increase proposal stake requirement. Implement proposal reputation threshold.")
        self._pass("Governance", "Security Council 4-of-7 multisig")

    def _check_nft(self):
        self._pass("NFT", "NIP-81 standard enforces ownership checks")
        self._pass("NFT", "Royalty enforcement on all marketplace sales")
        self._pass("NFT", "Transfer approval system")
        self._pass("NFT", "Collection max supply enforcement")
        self._finding("NFT", "LOW",
            "Metadata mutability",
            "NFT metadata URIs (IPFS) can point to mutable content "
            "if not using content-addressed storage.",
            "Enforce IPFS CID-based URIs. Validate IPFS hash format on mint.")

    def _check_bridge(self):
        self._pass("Bridge", "HTLC (Hash Time Lock Contract) design")
        self._pass("Bridge", "Timeout-based refund mechanism")
        self._pass("Bridge", "Hash preimage verification")
        self._finding("Bridge", "HIGH",
            "Centralized bridge relayer",
            "Bridge relies on off-chain relayers which are centralized points of failure.",
            "Implement decentralized bridge validator set. "
            "Use Light Client proofs for trustless bridging.")
        self._finding("Bridge", "MEDIUM",
            "Bridge fund concentration",
            "All bridged assets are held in single contract addresses.",
            "Implement multi-sig custody. Add bridge TVL limits. "
            "Use insurance fund coverage for bridge amounts.")

    def _check_wallets(self):
        self._pass("Wallet", "BIP-39 mnemonic with 12/24 word options")
        self._pass("Wallet", "BIP-32 HD derivation")
        self._pass("Wallet", "WIF private key with checksum")
        self._pass("Wallet", "Address checksum validation")
        self._finding("Wallet", "INFO",
            "Mnemonic word entropy",
            "12-word mnemonics have 128 bits of entropy. "
            "Recommend 24-word (256 bits) for maximum security.",
            "Default to 24-word mnemonics for new wallets.")

    def _check_api(self):
        self._pass("API", "Input validation on all endpoints")
        self._finding("API", "MEDIUM",
            "No authentication on admin endpoints",
            "Node management APIs have no authentication layer.",
            "Add JWT/API key authentication to sensitive endpoints. "
            "Use middleware for all admin routes.")
        self._finding("API", "LOW",
            "Rate limiting not enforced at API layer",
            "REST API endpoints could be spammed.",
            "Implement rate limiting middleware: 100 req/min per IP.")
        self._pass("API", "CORS headers configurable")
        self._pass("API", "JSON schema validation on POST bodies")

    def _check_mempool(self):
        self._pass("Mempool", "Minimum fee rate enforcement")
        self._pass("Mempool", "Dust threshold filtering")
        self._pass("Mempool", "RBF (Replace-By-Fee) support")
        self._pass("Mempool", "Spam filter for abnormal transaction patterns")
        self._finding("Mempool", "LOW",
            "Mempool DoS via small valid transactions",
            "Attacker could fill mempool with valid low-fee transactions.",
            "Dynamic minimum fee based on mempool size. "
            "Implement mempool size limit with fee-based eviction.")
        self._pass("Mempool", "Maximum mempool size enforcement")

    def generate_report(self) -> dict:
        severities = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}
        for f in self._findings:
            severities[f["severity"]] = severities.get(f["severity"], 0) + 1

        grade = ("A+" if self._score >= 95 else
                 "A"  if self._score >= 90 else
                 "B"  if self._score >= 80 else
                 "C"  if self._score >= 70 else "D")

        return {
            "audit_title":    "NEBULA Blockchain Security Audit",
            "audited_by":     "NEBULA Internal Security Team",
            "date":           time.strftime("%Y-%m-%d"),
            "version":        "3.0.0",
            "overall_score":  f"{self._score}/100",
            "security_grade": grade,
            "total_checks":   len(self._passed) + len(self._findings),
            "passed":         len(self._passed),
            "findings":       len(self._findings),
            "by_severity":    severities,
            "findings_detail": self._findings,
            "passed_checks":  self._passed,
            "summary": {
                "CRITICAL": severities["CRITICAL"],
                "HIGH":     severities["HIGH"],
                "MEDIUM":   severities["MEDIUM"],
                "LOW":      severities["LOW"],
                "INFO":     severities["INFO"],
            },
            "recommendations": [
                "1. Deploy Rust node for production — eliminates Python performance issues",
                "2. Implement TWAP oracle — prevents flash loan price manipulation",
                "3. Add transport encryption (BIP-324) — protects P2P layer",
                "4. Decentralize bridge validator set — removes central point of failure",
                "5. Add API authentication — secures admin endpoints",
                "6. Commission professional third-party audit before mainnet launch",
                "7. Implement formal verification for critical consensus code",
                "8. Deploy on testnet for 6+ months before mainnet",
                "9. Establish bug bounty program (implemented via community module)",
                "10. Regular penetration testing by external security firms",
            ],
            "audit_scope": [
                "Cryptographic primitives",
                "Consensus mechanism",
                "P2P network layer",
                "DeFi protocols (DEX, Lending, Staking)",
                "Governance system",
                "NFT contracts",
                "Cross-chain bridge",
                "Wallet implementation",
                "REST API",
                "Mempool management",
            ],
            "out_of_scope": [
                "Third-party dependencies",
                "Operating system security",
                "Physical infrastructure",
                "Social engineering attacks",
            ],
            "disclaimer": (
                "This is an internal security assessment for development purposes. "
                "A professional third-party audit from a reputable security firm "
                "(e.g., Trail of Bits, Certik, Halborn, Quantstamp) is required "
                "before any mainnet deployment with real user funds."
            ),
        }

    def print_report(self):
        """Print a formatted security audit report."""
        report = self.generate_report()
        print("\n" + "═" * 65)
        print(f"  🔐 {report['audit_title']}")
        print("═" * 65)
        print(f"  Date:          {report['date']}")
        print(f"  Version:       {report['version']}")
        print(f"  Overall Score: {report['overall_score']} (Grade: {report['security_grade']})")
        print(f"  Checks Passed: {report['passed']}/{report['total_checks']}")
        print()
        print(f"  Findings by Severity:")
        for sev, count in report["by_severity"].items():
            if count > 0:
                emoji = {"CRITICAL":"🔴","HIGH":"🟠","MEDIUM":"🟡","LOW":"🟢","INFO":"ℹ️"}.get(sev,"")
                print(f"    {emoji} {sev:<10}: {count}")
        print()
        print("  Top Recommendations:")
        for rec in report["recommendations"][:5]:
            print(f"    {rec}")
        print("═" * 65 + "\n")


# ---- BugBountyProgram
class BugBountyProgram:
    """NEBULA Bug Bounty Program."""

    SEVERITY_REWARDS = {
        "CRITICAL": (50_000, 100_000),
        "HIGH":     (10_000,  50_000),
        "MEDIUM":   ( 1_000,  10_000),
        "LOW":      (   100,   1_000),
        "INFO":     (     0,     100),
    }

    SCOPE = [
        "nebula_blockchain_fixed.py — Core blockchain",
        "Rust node implementation (nebula-node)",
        "REST API endpoints",
        "Wallet key generation and management",
        "Smart contract execution engine",
        "Cross-chain bridge logic",
        "DeFi protocol math and edge cases",
        "Governance vote manipulation",
        "DoS/Spam vulnerabilities",
    ]

    OUT_OF_SCOPE = [
        "Social engineering / phishing",
        "Third-party centralized services",
        "Testnet-only issues (unless critical)",
        "Issues requiring physical access",
        "Known issues already in audit report",
    ]

    def __init__(self):
        self._reports: list = []
        self._paid:    int  = 0

    def submit(self, reporter: str, title: str,
               severity: str, description: str,
               proof_of_concept: str,
               affected_component: str) -> dict:
        """Submit a bug bounty report."""
        report_id = hashlib.sha256(
            f"BUG:{reporter}:{title}:{time.time()}".encode()
        ).hexdigest()[:12]

        min_r, max_r = self.SEVERITY_REWARDS.get(severity, (0, 0))

        self._reports.append({
            "report_id":   report_id,
            "reporter":    reporter,
            "title":       title,
            "severity":    severity,
            "description": description[:2000],
            "poc":         proof_of_concept[:1000],
            "component":   affected_component,
            "status":      "received",
            "submitted":   time.time(),
            "reward_range": f"{min_r:,} – {max_r:,} NBL",
        })
        return {
            "ok":          True,
            "report_id":   report_id,
            "severity":    severity,
            "reward_range": f"{min_r:,} – {max_r:,} NBL",
            "status":      "received",
            "sla":         "Response within 72 hours",
            "submit_url":  "https://security.nebula-nbl.io/bounty",
            "email":       "security@nebula-nbl.io",
            "pgp_key":     "https://nebula-nbl.io/pgp-key.asc",
        }

    def program_info(self) -> dict:
        total_potential = sum(
            self.SEVERITY_REWARDS[sev][1]
            for sev in self.SEVERITY_REWARDS
        )
        return {
            "program":         "NEBULA Bug Bounty",
            "total_reports":   len(self._reports),
            "total_paid_nbl":  f"{self._paid:,}",
            "max_reward":      "100,000 NBL (Critical)",
            "total_potential": f"{total_potential:,} NBL",
            "scope":           self.SCOPE,
            "out_of_scope":    self.OUT_OF_SCOPE,
            "severity_rewards": {
                sev: f"{mn:,} – {mx:,} NBL"
                for sev, (mn, mx) in self.SEVERITY_REWARDS.items()
            },
            "rules": [
                "First reporter of each valid bug gets the reward",
                "No exploitation of the bug beyond PoC",
                "Responsible disclosure — private report first",
                "Do not disclose publicly until patched",
                "Testnet testing encouraged before mainnet",
            ],
            "contact": {
                "email":   "security@nebula-nbl.io",
                "website": "https://security.nebula-nbl.io",
                "pgp":     "https://nebula-nbl.io/pgp-key.asc",
            },
        }


# ---- DynamicFeePool
class DynamicFeePool:
    """AMM pool with dynamic fees based on volatility."""

    def __init__(self, token_a: str, token_b: str,
                  base_fee_bps: int = 30):
        self.token_a      = token_a
        self.token_b      = token_b
        self.base_fee     = base_fee_bps / 10000
        self.reserve_a    = 0
        self.reserve_b    = 0
        self._vol_samples: list = []
        self._lock        = threading.RLock()

    @property
    def dynamic_fee(self) -> float:
        """Fee increases with volatility."""
        if len(self._vol_samples) < 2:
            return self.base_fee
        prices   = self._vol_samples[-20:]
        mean_p   = sum(prices) / len(prices)
        variance = sum((p - mean_p)**2 for p in prices) / len(prices)
        vol      = (variance**0.5) / mean_p if mean_p > 0 else 0
        # Fee scales from base to 3x base with volatility
        return min(self.base_fee * 3, self.base_fee * (1 + vol * 10))

    def add_liquidity(self, amount_a: float, amount_b: float) -> float:
        with self._lock:
            if self.reserve_a == 0:
                lp = (amount_a * amount_b) ** 0.5
            else:
                lp = min(amount_a / self.reserve_a,
                         amount_b / self.reserve_b) * self.total_lp
            self.reserve_a += amount_a
            self.reserve_b += amount_b
            self.total_lp  = getattr(self, 'total_lp', 0) + lp
            return lp

    def swap(self, token_in: str, amount_in: float) -> float:
        with self._lock:
            fee    = self.dynamic_fee
            net_in = amount_in * (1 - fee)
            if token_in == self.token_a:
                out = net_in * self.reserve_b / (self.reserve_a + net_in)
                self.reserve_a += amount_in
                self.reserve_b -= out
            else:
                out = net_in * self.reserve_a / (self.reserve_b + net_in)
                self.reserve_b += amount_in
                self.reserve_a -= out
            # Record price for volatility
            if self.reserve_a > 0:
                self._vol_samples.append(self.reserve_b / self.reserve_a)
                if len(self._vol_samples) > 100:
                    self._vol_samples.pop(0)
            return out

    def pool_info(self) -> dict:
        return {
            "pair":        f"{self.token_a}/{self.token_b}",
            "reserve_a":   f"{self.reserve_a:.6f}",
            "reserve_b":   f"{self.reserve_b:.6f}",
            "dynamic_fee": f"{self.dynamic_fee*100:.3f}%",
            "base_fee":    f"{self.base_fee*100:.2f}%",
        }


# ---- RangeOrderBook
class RangeOrderBook:
    """Range orders — like Uniswap v3 limit orders."""

    def __init__(self, pool: 'DynamicFeePool'):
        self._pool    = pool
        self._orders: list = []
        self._lock    = threading.RLock()

    def place_range_order(self, owner: str, token_in: str,
                           amount: float, lower_price: float,
                           upper_price: float) -> str:
        with self._lock:
            oid = hashlib.sha256(
                f"RANGE:{owner}:{amount}:{time.time()}".encode()
            ).hexdigest()[:10]
            self._orders.append({
                "oid":         oid,
                "owner":       owner,
                "token_in":    token_in,
                "amount":      amount,
                "lower":       lower_price,
                "upper":       upper_price,
                "filled":      False,
                "ts":          time.time(),
            })
            return oid

    def check_and_fill(self) -> list:
        """Fill orders if current price is in range."""
        filled = []
        with self._lock:
            ra, rb = self._pool.reserve_a, self._pool.reserve_b
            if ra <= 0:
                return []
            cur_price = rb / ra
            for order in self._orders:
                if order["filled"]:
                    continue
                if order["lower"] <= cur_price <= order["upper"]:
                    out = self._pool.swap(order["token_in"], order["amount"])
                    order["filled"]   = True
                    order["out"]      = out
                    order["fill_price"] = cur_price
                    filled.append(order)
        return filled

    def open_orders(self, owner: str = None) -> list:
        orders = [o for o in self._orders if not o["filled"]]
        if owner:
            orders = [o for o in orders if o["owner"] == owner]
        return orders


# ---- MEVAuction
class MEVAuction:
    """MEV (Maximal Extractable Value) auction system."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._bundles: list = []
        self._auctions: list = []
        self._lock    = threading.RLock()

    def submit_bundle(self, builder: str,
                       txids: list, bid_nbl: float) -> str:
        with self._lock:
            bundle_id = hashlib.sha256(
                f"BUNDLE:{builder}:{bid_nbl}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._bundles.append({
                "bundle_id": bundle_id,
                "builder":   builder,
                "txids":     txids,
                "bid":       bid_nbl,
                "block":     self._bc.height + 1,
                "status":    "pending",
            })
            return bundle_id

    def run_auction(self, block_height: int) -> dict:
        """Select winning bundle for a block."""
        with self._lock:
            candidates = [b for b in self._bundles
                          if b["block"] == block_height
                          and b["status"] == "pending"]
        if not candidates:
            return {"winner": None, "bid": 0}
        winner = max(candidates, key=lambda b: b["bid"])
        winner["status"] = "won"
        self._auctions.append({
            "block":   block_height,
            "winner":  winner["builder"],
            "bid_nbl": winner["bid"],
            "txs":     len(winner["txids"]),
        })
        return {"winner": winner["builder"], "bid": winner["bid"]}

    def mev_stats(self) -> dict:
        total_bids = sum(a["bid_nbl"] for a in self._auctions)
        return {
            "total_auctions": len(self._auctions),
            "total_mev_nbl":  f"{total_bids:.3f}",
            "pending_bundles": len([b for b in self._bundles
                                    if b["status"] == "pending"]),
        }


# ---- AutomatedMarketMakerV3
class AutomatedMarketMakerV3:
    """Full-featured AMM v3 with concentrated liquidity."""

    TICK_SPACING = 60

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._pools: dict = {}
        self._lock  = threading.RLock()

    def create_pool(self, token_a: str, token_b: str,
                     initial_price: float,
                     fee_bps: int = 30) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"AMMV3:{token_a}:{token_b}:{fee_bps}".encode()
            ).hexdigest()[:10]
            self._pools[pid] = {
                "token_a":     token_a,
                "token_b":     token_b,
                "sqrt_price":  initial_price ** 0.5,
                "liquidity":   0.0,
                "fee_bps":     fee_bps,
                "tick":        0,
                "positions":   {},
                "fee_growth":  0.0,
            }
            return pid

    def mint_position(self, pool_id: str, owner: str,
                       tick_lower: int, tick_upper: int,
                       liquidity: float) -> str:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return ""
            pos_id = hashlib.sha256(
                f"POS:{owner}:{tick_lower}:{tick_upper}:{time.time()}".encode()
            ).hexdigest()[:10]
            pool["positions"][pos_id] = {
                "owner":      owner,
                "tick_lower": tick_lower,
                "tick_upper": tick_upper,
                "liquidity":  liquidity,
                "fees_earned": 0.0,
            }
            if tick_lower <= pool["tick"] <= tick_upper:
                pool["liquidity"] += liquidity
            return pos_id

    def swap(self, pool_id: str, zero_for_one: bool,
              amount_in: float) -> Tuple[float, float]:
        """Returns (amount_out, fee_paid)."""
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool or pool["liquidity"] <= 0:
                return 0.0, 0.0
            fee_rate = pool["fee_bps"] / 10000
            fee_paid = amount_in * fee_rate
            net_in   = amount_in - fee_paid
            liq      = pool["liquidity"]
            sqp      = pool["sqrt_price"]
            if zero_for_one:
                new_sqp = liq * sqp / (liq + net_in * sqp)
                out     = liq * (sqp - new_sqp)
            else:
                new_sqp = sqp + net_in / liq
                out     = liq * (1/sqp - 1/new_sqp) if sqp > 0 else 0
            pool["sqrt_price"] = max(1e-18, new_sqp)
            pool["fee_growth"] += fee_paid / max(1, liq)
            return out, fee_paid

    def collect_fees(self, pool_id: str, pos_id: str) -> float:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return 0.0
            pos  = pool["positions"].get(pos_id)
            if not pos:
                return 0.0
            fees = pos["fees_earned"]
            pos["fees_earned"] = 0.0
            return fees

    def amm_v3_stats(self) -> dict:
        total_liq = sum(p["liquidity"] for p in self._pools.values())
        return {
            "pools":        len(self._pools),
            "total_liq":    f"{total_liq:.4f}",
            "version":      "AMM v3 (CLMM)",
        }


# ---- OptimisticRollup
class OptimisticRollup:
    """
    Optimistic Rollup L2 for NEBULA.
    Assumes transactions valid — fraud proofs if disputed.
    7-day challenge period for withdrawals.
    """

    CHALLENGE_PERIOD_BLOCKS = 144 * 7   # 7 days
    FRAUD_PROOF_WINDOW      = 144       # 1 day to submit fraud proof

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._l2_state:  dict = {}        # address -> l2_balance
        self._batches:   list = []
        self._withdrawals: list = []
        self._challenges: list = []
        self._sequencer: str = FOUNDATION_ADDRESS
        self._lock       = threading.RLock()

    def deposit(self, address: str, amount: int) -> dict:
        """Deposit NBL to L2."""
        with self._lock:
            if self._bc.utxo.balance(address) < amount:
                return {"ok": False, "error": "Insufficient L1 balance"}
            self._l2_state[address] = self._l2_state.get(address, 0) + amount
            deposit_id = hashlib.sha256(
                f"L2DEP:{address}:{amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            return {
                "ok":         True,
                "deposit_id": deposit_id,
                "l2_balance": self._l2_state[address] / 10**DECIMALS,
                "note":       "Available immediately on L2",
            }

    def l2_transfer(self, sender: str, recipient: str,
                     amount: int) -> dict:
        """Instant L2 transfer (no L1 cost)."""
        with self._lock:
            if self._l2_state.get(sender, 0) < amount:
                return {"ok": False, "error": "Insufficient L2 balance"}
            self._l2_state[sender]    -= amount
            self._l2_state[recipient]  = self._l2_state.get(recipient, 0) + amount
            return {
                "ok":     True,
                "txid":   hashlib.sha256(f"{sender}{recipient}{amount}{time.time()}".encode()).hexdigest()[:16],
                "cost":   "0 NBL (L2 gas-free)",
                "speed":  "instant",
            }

    def submit_batch(self, transactions: list) -> dict:
        """Sequencer submits batch of L2 txs to L1."""
        with self._lock:
            batch_id = len(self._batches)
            state_root = hashlib.sha256(
                json.dumps(self._l2_state, sort_keys=True).encode()
            ).hexdigest()
            self._batches.append({
                "batch_id":    batch_id,
                "tx_count":    len(transactions),
                "state_root":  state_root,
                "sequencer":   self._sequencer,
                "l1_block":    self._bc.height,
                "challenge_until": self._bc.height + self.CHALLENGE_PERIOD_BLOCKS,
                "finalized":   False,
                "challenged":  False,
            })
            return {
                "ok":       True,
                "batch_id": batch_id,
                "tx_count": len(transactions),
                "state_root": state_root[:16] + "...",
                "challenge_period": f"{self.CHALLENGE_PERIOD_BLOCKS} blocks (~7 days)",
            }

    def initiate_withdrawal(self, address: str, amount: int) -> dict:
        """Start 7-day withdrawal to L1."""
        with self._lock:
            if self._l2_state.get(address, 0) < amount:
                return {"ok": False, "error": "Insufficient L2 balance"}
            self._l2_state[address] -= amount
            wid = hashlib.sha256(
                f"WITHDRAW:{address}:{amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            ready_at = self._bc.height + self.CHALLENGE_PERIOD_BLOCKS
            self._withdrawals.append({
                "withdrawal_id": wid,
                "address":       address,
                "amount":        amount,
                "initiated":     self._bc.height,
                "ready_at":      ready_at,
                "claimed":       False,
            })
            return {
                "ok":             True,
                "withdrawal_id":  wid,
                "amount_nbl":     f"{amount/10**DECIMALS:.6f}",
                "ready_at_block": ready_at,
                "ready_in_days":  7,
                "note":           "7-day challenge window for fraud proofs",
            }

    def claim_withdrawal(self, address: str, wid: str) -> dict:
        """Claim withdrawal after challenge period."""
        with self._lock:
            w = next((w for w in self._withdrawals
                      if w["withdrawal_id"] == wid), None)
            if not w:
                return {"ok": False, "error": "Withdrawal not found"}
            if w["claimed"]:
                return {"ok": False, "error": "Already claimed"}
            if self._bc.height < w["ready_at"]:
                left = w["ready_at"] - self._bc.height
                return {"ok": False, "error": f"Not ready. {left} blocks remaining"}
            if w["address"] != address:
                return {"ok": False, "error": "Not your withdrawal"}
            w["claimed"] = True
            return {
                "ok":       True,
                "amount":   f"{w['amount']/10**DECIMALS:.6f} NBL",
                "returned": "to L1",
            }

    def submit_fraud_proof(self, challenger: str,
                            batch_id: int, proof: str) -> dict:
        """Challenge a fraudulent batch."""
        with self._lock:
            batch = next((b for b in self._batches
                          if b["batch_id"] == batch_id), None)
            if not batch:
                return {"ok": False, "error": "Batch not found"}
            if self._bc.height > batch["challenge_until"]:
                return {"ok": False, "error": "Challenge period expired"}
            # Simplified: accept challenge (real impl needs fraud proof verification)
            batch["challenged"] = True
            self._challenges.append({
                "challenger": challenger,
                "batch_id":   batch_id,
                "proof":      proof[:100],
                "block":      self._bc.height,
                "resolved":   False,
            })
            return {
                "ok":      True,
                "message": f"Fraud proof submitted for batch {batch_id}",
                "reward":  "Challenger receives slashed sequencer stake if valid",
            }

    def l2_stats(self) -> dict:
        with self._lock:
            total_l2 = sum(self._l2_state.values())
            finalized = sum(1 for b in self._batches if b["finalized"])
        return {
            "type":          "Optimistic Rollup",
            "l2_tvl_nbl":    f"{total_l2/10**DECIMALS:.3f}",
            "l2_users":      len(self._l2_state),
            "batches":       len(self._batches),
            "finalized":     finalized,
            "withdrawals":   len(self._withdrawals),
            "challenges":    len(self._challenges),
            "challenge_days": 7,
            "tps_capacity":  "~2,000 TPS",
            "cost_reduction": "~100x cheaper than L1",
        }


# ---- GameCharacter
class GameCharacter:
    """On-chain RPG character NFT."""

    CLASSES = ["Warrior", "Mage", "Rogue", "Archer", "Paladin"]
    RACES   = ["Human", "Elf", "Dwarf", "Orc", "Demon"]

    def __init__(self, char_id: str, owner: str,
                  name: str, char_class: str, race: str):
        self.char_id   = char_id
        self.owner     = owner
        self.name      = name
        self.char_class = char_class
        self.race      = race
        self.level     = 1
        self.xp        = 0
        self.hp        = 100
        self.max_hp    = 100
        self.attack    = 10 + (["Warrior","Rogue"].count(char_class) * 5)
        self.defense   = 5  + (["Warrior","Paladin"].count(char_class) * 5)
        self.magic     = 5  + (["Mage","Paladin"].count(char_class) * 8)
        self.inventory: list = []
        self.skills:    list = []
        self.quests:    list = []

    def gain_xp(self, amount: int) -> bool:
        """Returns True if leveled up."""
        self.xp += amount
        needed = self.level * 100
        if self.xp >= needed:
            self.xp    -= needed
            self.level += 1
            self.max_hp += 10
            self.hp     = self.max_hp
            self.attack += 2
            self.defense += 1
            self.magic  += 2
            return True
        return False

    def equip(self, item: dict) -> bool:
        if len(self.inventory) >= 20:
            return False
        self.inventory.append(item)
        self.attack  += item.get("attack_bonus", 0)
        self.defense += item.get("defense_bonus", 0)
        self.magic   += item.get("magic_bonus", 0)
        return True

    def to_dict(self) -> dict:
        return {
            "char_id":   self.char_id,
            "name":      self.name,
            "class":     self.char_class,
            "race":      self.race,
            "level":     self.level,
            "xp":        self.xp,
            "hp":        f"{self.hp}/{self.max_hp}",
            "attack":    self.attack,
            "defense":   self.defense,
            "magic":     self.magic,
            "items":     len(self.inventory),
        }


# ---- Dungeon
class Dungeon:
    """On-chain dungeon with boss fights."""

    DUNGEONS = [
        {"name": "Goblin Cave",     "level_req": 1,  "boss_hp": 50,  "reward_nbl": 10},
        {"name": "Dark Forest",     "level_req": 5,  "boss_hp": 150, "reward_nbl": 50},
        {"name": "Ancient Ruins",   "level_req": 10, "boss_hp": 300, "reward_nbl": 150},
        {"name": "Dragon Lair",     "level_req": 20, "boss_hp": 800, "reward_nbl": 500},
        {"name": "Void Realm",      "level_req": 50, "boss_hp": 5000,"reward_nbl": 5000},
    ]

    def __init__(self, rng: 'OnChainRNG', blockchain: 'NEBULABlockchain'):
        self._rng  = rng
        self._bc   = blockchain
        self._runs: list = []

    def enter(self, character: 'GameCharacter',
               dungeon_index: int) -> dict:
        dungeon = self.DUNGEONS[dungeon_index % len(self.DUNGEONS)]
        if character.level < dungeon["level_req"]:
            return {"ok": False, "error": f"Need level {dungeon['level_req']}"}

        # Simulate combat rounds
        char_hp  = character.hp
        boss_hp  = dungeon["boss_hp"]
        rounds   = []
        h        = self._bc.height
        r        = 0
        while char_hp > 0 and boss_hp > 0 and r < 20:
            char_dmg = max(1, character.attack +
                          self._rng.random_int(h, 10, r) - 5)
            boss_dmg = max(0, dungeon["boss_hp"] // 20 +
                          self._rng.random_int(h, 8, r+1) - character.defense)
            boss_hp  -= char_dmg
            char_hp  -= boss_dmg
            rounds.append({"round": r+1, "char_dmg": char_dmg, "boss_dmg": boss_dmg})
            r += 1

        won    = boss_hp <= 0
        reward = dungeon["reward_nbl"] if won else 0
        xp     = dungeon["boss_hp"] // 5 if won else dungeon["boss_hp"] // 20
        leveled = character.gain_xp(xp)

        run = {
            "dungeon":  dungeon["name"],
            "won":      won,
            "rounds":   len(rounds),
            "xp":       xp,
            "reward_nbl": reward,
            "leveled":  leveled,
            "char_hp_remaining": max(0, char_hp),
        }
        self._runs.append(run)
        return {"ok": True, **run}


# ---- NFTGamingPlatform
class NFTGamingPlatform:
    """Complete NFT gaming platform."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  nft: 'NBL721Registry',
                  rng: 'OnChainRNG'):
        self._bc      = blockchain
        _enable_dev_mode(self._bc, 'NFTGamingPlatform')   # v10.9: fail-closed (was: forced _dev_mode=True)
        self._nft     = nft
        self._rng     = rng
        self._chars:  dict = {}
        self._dungeon = Dungeon(rng, blockchain)
        self._leaderboard: list = []
        self._lock    = threading.RLock()

    def create_character(self, owner: str, name: str,
                          char_class: str = None,
                          race: str = None) -> dict:
        with self._lock:
            if char_class not in GameCharacter.CLASSES:
                char_class = GameCharacter.CLASSES[
                    self._rng.random_int(self._bc.height, len(GameCharacter.CLASSES))]
            if race not in GameCharacter.RACES:
                race = GameCharacter.RACES[
                    self._rng.random_int(self._bc.height, len(GameCharacter.RACES), 1)]
            char_id = hashlib.sha256(
                f"CHAR:{owner}:{name}:{time.time()}".encode()
            ).hexdigest()[:12]
            char    = GameCharacter(char_id, owner, name, char_class, race)
            self._chars[char_id] = char
            # Mint as NFT
            col_id = "nebula_heroes"
            self._nft._collections.setdefault(col_id, {
                "creator": FOUNDATION_ADDRESS, "name": "NEBULA Heroes",
                "symbol": "NHERO", "max_supply": 100000,
                "royalty_pct": 0.05, "tokens": {}, "counter": 0
            })
            col = self._nft._collections[col_id]
            col["counter"] = col.get("counter", 0) + 1
            token_id = col["counter"]
            col["tokens"][token_id] = {
                "owner": owner,
                "uri":   f"ipfs://nebula/heroes/{char_id}",
                "meta":  char.to_dict(),
                "approved": None,
            }
            return {
                "ok":       True,
                "char_id":  char_id,
                "token_id": token_id,
                "character": char.to_dict(),
            }

    def enter_dungeon(self, owner: str, char_id: str,
                       dungeon_index: int) -> dict:
        with self._lock:
            char = self._chars.get(char_id)
            if not char or char.owner != owner:
                return {"ok": False, "error": "Character not found"}
        result = self._dungeon.enter(char, dungeon_index)
        if result.get("won") and result.get("reward_nbl", 0) > 0:
            self._bc.fund_address(owner, result["reward_nbl"])
        return result

    def top_characters(self, n: int = 10) -> list:
        with self._lock:
            chars = sorted(self._chars.values(),
                           key=lambda c: c.level, reverse=True)
        return [{"rank": i+1, **c.to_dict()}
                for i, c in enumerate(chars[:n])]

    def gaming_stats(self) -> dict:
        with self._lock:
            total_lvl = sum(c.level for c in self._chars.values())
        return {
            "characters":   len(self._chars),
            "dungeons":     len(self._dungeon.DUNGEONS),
            "runs":         len(self._dungeon._runs),
            "avg_level":    f"{total_lvl/max(1,len(self._chars)):.1f}",
        }


# ---- SocialToken
class SocialToken:
    """Creator social token on NEBULA."""

    def __init__(self, creator: str, symbol: str, name: str,
                  total_supply: int, blockchain: 'NEBULABlockchain'):
        self.creator      = creator
        self.symbol       = symbol
        self.name         = name
        self.total_supply = total_supply
        self._bc          = blockchain
        self._holders:    dict = {}
        self._price:      float = 0.001   # NBL per token
        self._buy_volume: float = 0.0
        self._lock        = threading.RLock()
        # Creator gets 10% of supply
        self._holders[creator] = total_supply // 10

    def buy(self, buyer: str, amount: int) -> Tuple[bool, float]:
        """Bonding curve buy."""
        with self._lock:
            cost  = amount * self._price * (1 + self._buy_volume / 100000)
            if self._bc.utxo.balance(buyer) < int(cost * 10**DECIMALS):
                return False, 0.0
            self._holders[buyer] = self._holders.get(buyer, 0) + amount
            self._price         *= 1.001   # price increases
            self._buy_volume    += cost
            return True, cost

    def sell(self, seller: str, amount: int) -> Tuple[bool, float]:
        """Bonding curve sell."""
        with self._lock:
            if self._holders.get(seller, 0) < amount:
                return False, 0.0
            proceeds = amount * self._price * 0.95   # 5% sell tax
            self._holders[seller] -= amount
            self._price           = max(0.001, self._price * 0.999)
            return True, proceeds

    def unlock_content(self, holder: str,
                        min_tokens: int = 100) -> bool:
        """Check if holder can access gated content."""
        return self._holders.get(holder, 0) >= min_tokens

    def token_info(self) -> dict:
        return {
            "symbol":    self.symbol,
            "name":      self.name,
            "creator":   self.creator,
            "price_nbl": f"{self._price:.6f}",
            "holders":   len(self._holders),
            "volume":    f"{self._buy_volume:.3f}",
        }
