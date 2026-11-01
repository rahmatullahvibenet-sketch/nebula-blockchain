"""NEBULA group38 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. NFTMarketplaceV2  (orig. lines 63912-64028)
   2. SidechainBridge  (orig. lines 64035-64106)
   3. PoSValidator  (orig. lines 64113-64139)
   4. PoSEngine  (orig. lines 64141-64231)
   5. TxBuilderV2  (orig. lines 64238-64330)
   6. TestnetFaucet  (orig. lines 64457-64490)
   7. DevToolkit  (orig. lines 64493-64566)
   8. WebSocketSubscription  (orig. lines 64573-64593)
   9. WebSocketAPIServer  (orig. lines 64595-64699)
  10. OrderBookManager  (orig. lines 64711-64746)
  11. GameItem  (orig. lines 64753-64780)
  12. NFTGamingEngine  (orig. lines 64782-64895)
  13. CredentialType  (orig. lines 64902-64910)
  14. VerifiablePresentation  (orig. lines 64912-64930)
  15. DigitalIdentityV2  (orig. lines 64932-65062)
  16. ComplianceCheckType  (orig. lines 65069-65074)
  17. ComplianceRecord  (orig. lines 65076-65095)
  18. ComplianceEngine  (orig. lines 65097-65185)
  19. AnalyticsMetric  (orig. lines 65192-65200)
  20. AnalyticsV2  (orig. lines 65202-65311)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BIP39, Block, BlockHeader, HDKey, MerkleTree, NEBULABlockchain, NFTAuctionType, NFTListing, OrderBook, OutPoint, Script, Secp256k1, Transaction, TxInput, TxOutput
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

CHAIN_VERSION       = 1

DECIMALS            = 9

MAX_SUPPLY          = 21_000_000 * (10 ** DECIMALS)   # in Neb  (matches 50 NBL * 210,000 blocks * 2 geometric series)

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

INITIAL_BITS           = 0x1e0fffff if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d0fffff   # [v10.24]

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

DUST_THRESHOLD         = 546                            # min output amount in Neb

OP_RETURN       = 0x6a

TX_VERSION        = 1             # default transaction version

def mining_reward(height: int) -> int:
    """Block reward with halving schedule.
    FIX: negative height safely returns 0 instead of crashing."""
    if height < 0:
        return 0
    era = height // HALVING_INTERVAL
    if era >= 64:
        return 0
    return INITIAL_BLOCK_REWARD >> era

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

_routes: Dict[str, Dict[str, Callable]] = {}

def route(path: str, methods: List[str] = None):
    """Decorator to register an API endpoint."""
    def decorator(fn: Callable) -> Callable:
        for method in (methods or ["GET"]):
            _routes.setdefault(method.upper(), {})[path] = fn
        return fn
    return decorator

@route("/api/health")
def health(path, query, body):
    ok_count = sum(1 for m in STATE.module_status().values() if m["ok"])
    total    = len(STATE.module_status())
    return ok({
        "status"         : "healthy" if ok_count >= 5 else "degraded",
        "modules_loaded" : ok_count,
        "modules_total"  : total,
        "uptime_secs"    : int(time.time() - STATE._start),
        "height"         : STATE.height(),
        "mining"         : STATE._mining,
        "timestamp"      : time.time(),
    })

MIN_STAKE           = 100 * 10**DECIMALS    # 100 NBL minimum

SLASH_DOUBLE_SIGN   = 5_000                  # 5% slash for double sign

SLASH_DOWNTIME      = 100                    # 0.01% slash for downtime

MAX_VALIDATORS           = 100

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


# ---- NFTMarketplaceV2
class NFTMarketplaceV2:
    """
    Advanced NFT marketplace supporting multiple auction types.
    Fixed price, English auction, Dutch auction, sealed bid.
    """

    MARKET_FEE = 0.025    # 2.5%

    def __init__(self, blockchain: 'NEBULABlockchain',
                  nft_registry: 'NBL721Registry' = None):
        self._bc       = blockchain
        self._nft      = nft_registry
        self._listings: Dict[str, NFTListing] = {}
        self._sealed_bids: Dict[str, Dict[str, bytes]] = {}  # listing_id -> {bidder: sealed}
        self._lock      = threading.RLock()
        self._volume:   int = 0

    def list_fixed(self, collection_id: str, token_id: int,
                    seller: str, price: float) -> str:
        with self._lock:
            lid = hashlib.sha256(
                f"MKT:{collection_id}:{token_id}:{seller}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._listings[lid] = NFTListing(
                listing_id    = lid,
                collection_id = collection_id,
                token_id      = token_id,
                seller        = seller,
                auction_type  = NFTAuctionType.FIXED_PRICE,
                start_price   = int(price * 10**DECIMALS),
            )
            return lid

    def list_auction(self, collection_id: str, token_id: int,
                      seller: str, start_price: float,
                      reserve: float = 0, duration_blocks: int = 1000,
                      auction_type: NFTAuctionType = NFTAuctionType.ENGLISH) -> str:
        with self._lock:
            lid = hashlib.sha256(
                f"AUC:{collection_id}:{token_id}:{seller}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._listings[lid] = NFTListing(
                listing_id    = lid,
                collection_id = collection_id,
                token_id      = token_id,
                seller        = seller,
                auction_type  = auction_type,
                start_price   = int(start_price * 10**DECIMALS),
                reserve       = int(reserve * 10**DECIMALS),
                end_block     = self._bc.height + duration_blocks,
            )
            return lid

    def buy_now(self, listing_id: str, buyer: str) -> Tuple[bool, str]:
        with self._lock:
            listing = self._listings.get(listing_id)
            if not listing or listing.sold:
                return False, "Not available"
            if listing.auction_type != NFTAuctionType.FIXED_PRICE:
                return False, "Not a fixed-price listing"
            if self._bc.utxo.balance(buyer) < listing.start_price:
                return False, "Insufficient funds"
            listing.sold = True
            fee          = int(listing.start_price * self.MARKET_FEE)
            seller_gets  = listing.start_price - fee
            self._volume += listing.start_price
            return True, (f"Purchased #{listing.token_id} for "
                          f"{listing.start_price/10**DECIMALS:.3f} NBL")

    def place_bid(self, listing_id: str, bidder: str,
                   amount: float) -> Tuple[bool, str]:
        with self._lock:
            listing = self._listings.get(listing_id)
            if not listing or listing.sold:
                return False, "Not available"
            if listing.auction_type not in (
                    NFTAuctionType.ENGLISH, NFTAuctionType.DUTCH):
                return False, "Not an auction listing"
            if self._bc.height > listing.end_block:
                return False, "Auction ended"
            bid_raw = int(amount * 10**DECIMALS)
            if bid_raw <= listing.highest_bid:
                return False, f"Bid too low: must exceed {listing.highest_bid/10**DECIMALS:.3f}"
            if self._bc.utxo.balance(bidder) < bid_raw:
                return False, "Insufficient funds"
            listing.highest_bid    = bid_raw
            listing.highest_bidder = bidder
            listing.bids.append({"bidder": bidder, "amount": bid_raw,
                                  "block": self._bc.height})
            return True, f"Bid placed: {amount:.3f} NBL"

    def finalize_auction(self, listing_id: str) -> Tuple[bool, str]:
        with self._lock:
            listing = self._listings.get(listing_id)
            if not listing or listing.sold:
                return False, "Not found or sold"
            if self._bc.height <= listing.end_block:
                return False, f"Auction not ended yet (block {listing.end_block})"
            if listing.highest_bid == 0:
                return False, "No bids"
            if listing.highest_bid < listing.reserve:
                return False, f"Reserve not met: {listing.highest_bid} < {listing.reserve}"
            listing.sold = True
            self._volume += listing.highest_bid
            return True, (f"Auction won by {listing.highest_bidder} "
                          f"for {listing.highest_bid/10**DECIMALS:.3f} NBL")

    def marketplace_stats(self) -> dict:
        with self._lock:
            sold   = sum(1 for l in self._listings.values() if l.sold)
            active = len(self._listings) - sold
        return {
            "total_listings": len(self._listings),
            "active":         active,
            "sold":           sold,
            "volume_nbl":     f"{self._volume/10**DECIMALS:.3f}",
        }


# ---- SidechainBridge
class SidechainBridge:
    """
    Sidechain bridge — allows NBL to move to/from sidechains.
    Two-way peg: lock NBL on main chain, mint on sidechain.
    """

    def __init__(self, sidechain_name: str,
                  blockchain: 'NEBULABlockchain'):
        self.sidechain      = sidechain_name
        self._bc            = blockchain
        self._locked:       Dict[str, int] = {}   # addr -> locked NBL
        self._pegs:         List[dict]     = []
        self._lock          = threading.RLock()
        self._total_locked  = 0

    def peg_in(self, address: str,
                amount_nbl: float) -> Tuple[bool, str]:
        """Lock NBL on main chain to receive on sidechain."""
        with self._lock:
            amount = int(amount_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(address) < amount:
                return False, "Insufficient balance"
            self._locked[address] = self._locked.get(address, 0) + amount
            self._total_locked   += amount
            peg_id = hashlib.sha256(
                f"PEG_IN:{address}:{amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._pegs.append({
                "peg_id":     peg_id,
                "type":       "peg_in",
                "address":    address,
                "amount":     amount,
                "sidechain":  self.sidechain,
                "timestamp":  time.time(),
            })
            return True, (f"Pegged {amount_nbl} NBL to {self.sidechain}. "
                          f"PegID: {peg_id}")

    def peg_out(self, address: str,
                 amount_nbl: float,
                 proof: str = "") -> Tuple[bool, str]:
        """Unlock NBL on main chain from sidechain peg-out."""
        with self._lock:
            amount = int(amount_nbl * 10**DECIMALS)
            locked = self._locked.get(address, 0)
            if locked < amount:
                return False, f"Only {locked/10**DECIMALS} NBL locked for {address}"
            self._locked[address] -= amount
            self._total_locked    -= amount
            peg_id = hashlib.sha256(
                f"PEG_OUT:{address}:{amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._pegs.append({
                "peg_id":   peg_id,
                "type":     "peg_out",
                "address":  address,
                "amount":   amount,
                "proof":    proof,
                "timestamp": time.time(),
            })
            return True, f"Released {amount_nbl} NBL from {self.sidechain}"

    def locked_balance(self, address: str) -> int:
        return self._locked.get(address, 0)

    def bridge_stats(self) -> dict:
        return {
            "sidechain":      self.sidechain,
            "total_locked":   f"{self._total_locked/10**DECIMALS:.3f} NBL",
            "peg_operations": len(self._pegs),
            "locked_holders": sum(1 for v in self._locked.values() if v > 0),
        }


# ---- PoSValidator
class PoSValidator:
    """A PoS validator node."""

    def __init__(self, address: str, stake: int, commission: float):
        self.address     = address
        self.stake       = stake
        self.commission  = commission
        self.blocks_proposed = 0
        self.blocks_missed   = 0
        self.slashed         = False
        self.slash_count     = 0
        self.jail_until:  int = 0

    @property
    def uptime(self) -> float:
        total = self.blocks_proposed + self.blocks_missed
        return self.blocks_proposed / total if total > 0 else 1.0

    def to_dict(self) -> dict:
        return {
            "address":    self.address,
            "stake_nbl":  f"{self.stake/10**DECIMALS:.3f}",
            "commission": f"{self.commission*100:.1f}%",
            "uptime":     f"{self.uptime*100:.1f}%",
            "slashed":    self.slashed,
            "jail_until": self.jail_until,
        }


# ---- PoSEngine
class PoSEngine:
    """
    Proof of Stake consensus engine.
    Selects block proposers proportionally to stake.
    Slashes validators for double-signing or downtime.
    """

    MIN_STAKE          = 1_000 * 10**DECIMALS
    MAX_VALIDATORS     = 100
    SLASH_DOUBLE_SIGN  = 0.05    # 5% slash
    SLASH_DOWNTIME     = 0.01    # 1% slash
    JAIL_BLOCKS        = 1000

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._validators: Dict[str, PoSValidator] = {}
        self._round:      int = 0
        self._lock        = threading.RLock()

    def register(self, address: str, stake: int,
                  commission: float) -> Tuple[bool, str]:
        with self._lock:
            if stake < self.MIN_STAKE:
                return False, f"Min stake: {self.MIN_STAKE/10**DECIMALS:.0f} NBL"
            if address in self._validators:
                return False, "Already registered"
            if len(self._validators) >= self.MAX_VALIDATORS:
                return False, "Validator set full"
            self._validators[address] = PoSValidator(address, stake, commission)
            return True, f"Registered with {stake/10**DECIMALS:.0f} NBL stake"

    def select_proposer(self, block_height: int) -> Optional[str]:
        """Select block proposer using weighted random selection."""
        with self._lock:
            eligible = [
                v for v in self._validators.values()
                if not v.slashed and v.jail_until < block_height
            ]
            if not eligible:
                return None
            total_stake = sum(v.stake for v in eligible)
            if total_stake == 0:
                return eligible[0].address
            seed = hashlib.sha256(
                f"PROPOSER:{block_height}".encode()
            ).digest()
            r = int.from_bytes(seed[:4], 'big') % total_stake
            cum = 0
            for v in eligible:
                cum += v.stake
                if r < cum:
                    return v.address
            return eligible[-1].address

    def record_proposal(self, address: str, proposed: bool):
        with self._lock:
            v = self._validators.get(address)
            if v:
                if proposed:
                    v.blocks_proposed += 1
                else:
                    v.blocks_missed += 1
                    if v.uptime < 0.90:
                        self._slash_downtime(v)

    def _slash_downtime(self, v: PoSValidator):
        slash = int(v.stake * self.SLASH_DOWNTIME)
        v.stake      -= slash
        v.slash_count += 1
        v.jail_until  = self._bc.height + self.JAIL_BLOCKS

    def slash_double_sign(self, address: str) -> Tuple[bool, str]:
        with self._lock:
            v = self._validators.get(address)
            if not v:
                return False, "Not a validator"
            slash = int(v.stake * self.SLASH_DOUBLE_SIGN)
            v.stake   -= slash
            v.slashed  = True
            return True, f"Slashed {slash/10**DECIMALS:.3f} NBL for double-sign"

    def pos_stats(self) -> dict:
        with self._lock:
            active = sum(1 for v in self._validators.values()
                         if not v.slashed and v.jail_until < self._bc.height)
            total_stake = sum(v.stake for v in self._validators.values())
        return {
            "total_validators": len(self._validators),
            "active":           active,
            "total_stake_nbl":  f"{total_stake/10**DECIMALS:.3f}",
        }


# ---- TxBuilderV2
class TxBuilderV2:
    """
    High-level transaction builder for NEBULA v2.
    Handles UTXO selection, fee calculation, change outputs.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  wallet: 'HDWalletV2' = None):
        self._bc     = blockchain
        self._wallet = wallet

    def build_transfer(self, sender: str, recipient: str,
                        amount_nbl: float, fee_rate: int = None,
                        memo: str = "") -> Tuple[bool, Any, str]:
        """Build a simple transfer transaction."""
        amount   = int(amount_nbl * 10**DECIMALS)
        fee_rate = fee_rate or MIN_TX_FEE
        utxos    = self._bc.utxo.get_by_address(sender)  # FIX
        if not utxos:
            return False, None, "No UTXOs found"
        # Select UTXOs
        selected, total_in = self._select_utxos(utxos, amount + MIN_TX_FEE)
        if total_in < amount:
            return False, None, f"Insufficient funds: {total_in} < {amount}"
        # Build outputs
        outputs = [TxOutput(value=amount, script_pubkey=Script.p2pkh_script(recipient))]
        # Change
        estimated_fee = fee_rate * 250
        change = total_in - amount - estimated_fee
        if change >= DUST_THRESHOLD:
            outputs.append(
                TxOutput(value=change,
                          script_pubkey=Script.p2pkh_script(sender)))
        # Add memo as OP_RETURN if provided
        if memo:
            memo_data = memo[:80].encode()
            outputs.append(
                TxOutput(value=0,
                          script_pubkey=bytes([OP_RETURN]) + memo_data))
        # Build inputs
        inputs = [TxInput(
            outpoint=OutPoint(txid=u["txid"], index=u["index"]),  # Outpoint→OutPoint
            script_sig=b"",
            sequence=0xFFFFFFFF,
        ) for u in selected]
        tx = Transaction(inputs=inputs, outputs=outputs, version=TX_VERSION)
        return True, tx, "OK"

    def _select_utxos(self, utxos: List[dict],
                       target: int) -> Tuple[List[dict], int]:
        """Select UTXOs using smallest-first selection."""
        sorted_utxos = sorted(utxos, key=lambda u: u.get("value", 0))
        selected = []
        total    = 0
        for u in sorted_utxos:
            selected.append(u)
            total += u.get("value", 0)
            if total >= target:
                break
        return selected, total

    def build_batch(self, sender: str,
                     recipients: List[Tuple[str, float]]) -> Tuple[bool, Any, str]:
        """Build a batch transaction (one sender, many recipients)."""
        total_out = sum(int(a * 10**DECIMALS) for _, a in recipients)
        utxos     = self._bc.utxo.get_by_address(sender)  # FIX
        selected, total_in = self._select_utxos(utxos, total_out + MIN_TX_FEE * 2)
        if total_in < total_out:
            return False, None, "Insufficient balance for batch"
        outputs = []
        for addr, amount in recipients:
            outputs.append(
                TxOutput(value=int(amount * 10**DECIMALS),
                          script_pubkey=Script.p2pkh_script(addr)))
        change = total_in - total_out - MIN_TX_FEE * len(recipients)
        if change >= DUST_THRESHOLD:
            outputs.append(
                TxOutput(value=change,
                          script_pubkey=Script.p2pkh_script(sender)))
        inputs = [TxInput(
            outpoint=OutPoint(txid=u["txid"], index=u["index"]),  # Outpoint→OutPoint
            script_sig=b"",
            sequence=0xFFFFFFFF,
        ) for u in selected]
        tx = Transaction(inputs=inputs, outputs=outputs, version=TX_VERSION)
        return True, tx, f"Batch tx: {len(recipients)} recipients"

    def estimate_fee(self, n_inputs: int = 2,
                      n_outputs: int = 2,
                      fee_rate: int = None) -> int:
        rate = fee_rate or MIN_TX_FEE
        size = n_inputs * 148 + n_outputs * 34 + 10
        return rate * size


# ---- TestnetFaucet
class TestnetFaucet:
    """
    NEBULA testnet faucet.
    Distributes test NBL to developers for testing.
    """

    FAUCET_AMOUNT      = int(100 * 10**DECIMALS)
    COOLDOWN_SECS      = 3600    # 1 request per hour

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        _enable_dev_mode(self._bc, 'TestnetFaucet')   # v10.9: fail-closed (was: forced _dev_mode=True)
        self._requests:   Dict[str, float] = {}
        self._total_sent: int = 0
        self._lock        = threading.RLock()

    def request(self, address: str) -> Tuple[bool, str]:
        with self._lock:
            last = self._requests.get(address, 0)
            if time.time() - last < self.COOLDOWN_SECS:
                remaining = int(self.COOLDOWN_SECS - (time.time() - last))
                return False, f"Cooldown: wait {remaining}s"
            self._requests[address] = time.time()
            self._total_sent       += self.FAUCET_AMOUNT
            return True, (f"Sent {self.FAUCET_AMOUNT/10**DECIMALS:.0f} test NBL "
                          f"to {address}")

    def faucet_stats(self) -> dict:
        return {
            "total_sent_nbl":   f"{self._total_sent/10**DECIMALS:.3f}",
            "unique_requests":  len(self._requests),
            "faucet_amount":    f"{self.FAUCET_AMOUNT/10**DECIMALS:.0f} NBL",
            "cooldown":         f"{self.COOLDOWN_SECS}s",
        }


# ---- DevToolkit
class DevToolkit:
    """
    Developer toolkit for NEBULA development and testing.
    Provides utilities for rapid development and testing.
    """

    def __init__(self, blockchain: 'NEBULABlockchain' = None):
        self._bc = blockchain or NEBULABlockchain()

    def generate_test_wallets(self, n: int = 10) -> List[dict]:
        wallets = []
        for i in range(n):
            mnemonic = BIP39.generate_mnemonic()
            seed     = BIP39.mnemonic_to_seed(mnemonic)
            master   = HDKey.from_seed(seed)
            key      = master.derive_path(f"m/44'/2025'/0'/0/{i}")
            wallets.append({
                "index":    i,
                "mnemonic": mnemonic,
                "address":  key.address,
                "path":     f"m/44'/2025'/0'/0/{i}",
            })
        return wallets

    def mine_test_blocks(self, n: int = 10,
                          miner: str = None) -> int:
        """Mine n test blocks quickly."""
        miner   = miner or FOUNDATION_ADDRESS
        mined   = 0
        for _ in range(n):
            bc      = self._bc
            height  = bc.height + 1
            reward  = mining_reward(height)
            coinbase = Transaction.coinbase(height, reward, miner)
            blk = Block(
                header=BlockHeader(
                    version     = CHAIN_VERSION,
                    prev_hash   = bc.tip.hash,
                    merkle_root = MerkleTree.compute_root([coinbase.txid]),
                    timestamp   = int(time.time()),
                    bits        = INITIAL_BITS,
                    nonce       = 0,
                    height      = height,
                ),
                transactions = [coinbase]
            )
            blk.header.nonce = 0
            ok, msg = bc.add_block(blk)
            if ok:
                mined += 1
        return mined

    def decode_transaction(self, tx_hex: str) -> dict:
        """Decode a raw transaction hex."""
        try:
            raw   = bytes.fromhex(tx_hex)
            tx    = Transaction.deserialize(raw)
            return tx.to_dict()
        except Exception as e:
            return {"error": str(e)}

    def simulate_network_load(self, n_txs: int = 100) -> dict:
        """Simulate network load by generating random transactions."""
        generated = 0
        for i in range(n_txs):
            priv, pub = Secp256k1.generate_keypair()
            pub_b     = Secp256k1.pubkey_to_bytes(pub)
            addr      = Script.p2pkh_address(pub_b)
            generated += 1
        return {
            "txs_generated":  generated,
            "mempool_before": 0,
            "mempool_after":  generated,
        }


# ---- WebSocketSubscription
class WebSocketSubscription:
    """A WebSocket subscription for real-time updates."""

    def __init__(self, sub_id: str, client_id: str,
                  sub_type: str, filter_params: dict = None):
        self.sub_id       = sub_id
        self.client_id    = client_id
        self.sub_type     = sub_type
        self.filter_params = filter_params or {}
        self.created_at   = time.time()
        self.messages_sent = 0
        self.active       = True

    def to_dict(self) -> dict:
        return {
            "sub_id":   self.sub_id,
            "client":   self.client_id,
            "type":     self.sub_type,
            "active":   self.active,
            "messages": self.messages_sent,
        }


# ---- WebSocketAPIServer
class WebSocketAPIServer:
    """
    WebSocket API server for NEBULA real-time data.
    Supports subscriptions for blocks, txs, addresses, prices.
    """

    SUBSCRIPTION_TYPES = [
        "new_block",
        "new_transaction",
        "address_activity",
        "mempool_update",
        "price_update",
        "governance_event",
        "nft_sale",
        "dex_trade",
    ]

    def __init__(self, blockchain: 'NEBULABlockchain',
                  alert_system: 'AlertSystem' = None):
        self._bc          = blockchain
        self._alerts      = alert_system
        self._clients:    Dict[str, dict]                    = {}
        self._subs:       Dict[str, WebSocketSubscription]   = {}
        self._lock        = threading.RLock()

    def connect(self, client_id: str,
                 ip: str = "unknown") -> dict:
        with self._lock:
            self._clients[client_id] = {
                "client_id":   client_id,
                "ip":          ip,
                "connected_at": time.time(),
                "sub_count":   0,
            }
        return {"status": "connected", "client_id": client_id}

    def disconnect(self, client_id: str):
        with self._lock:
            # Remove all subscriptions for this client
            to_remove = [sid for sid, sub in self._subs.items()
                         if sub.client_id == client_id]
            for sid in to_remove:
                del self._subs[sid]
            self._clients.pop(client_id, None)

    def subscribe(self, client_id: str, sub_type: str,
                   filter_params: dict = None) -> Tuple[bool, str]:
        with self._lock:
            if sub_type not in self.SUBSCRIPTION_TYPES:
                return False, f"Unknown subscription type: {sub_type}"
            if client_id not in self._clients:
                return False, "Client not connected"
            sid = hashlib.sha256(
                f"WS:{client_id}:{sub_type}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._subs[sid] = WebSocketSubscription(
                sub_id       = sid,
                client_id    = client_id,
                sub_type     = sub_type,
                filter_params = filter_params or {},
            )
            self._clients[client_id]["sub_count"] += 1
            return True, sid

    def unsubscribe(self, sub_id: str) -> bool:
        with self._lock:
            sub = self._subs.pop(sub_id, None)
            if sub and sub.client_id in self._clients:
                self._clients[sub.client_id]["sub_count"] = max(
                    0, self._clients[sub.client_id]["sub_count"] - 1)
            return sub is not None

    def broadcast_event(self, event_type: str, data: dict) -> int:
        """Broadcast event to all relevant subscribers."""
        sent = 0
        with self._lock:
            matching = [sub for sub in self._subs.values()
                        if sub.sub_type == event_type and sub.active]
        for sub in matching:
            sub.messages_sent += 1
            sent += 1
        return sent

    def on_new_block(self, block: 'Block') -> int:
        return self.broadcast_event("new_block", {
            "height": block.height,
            "hash":   block.hash,
            "txs":    block.tx_count,
        })

    def on_new_tx(self, tx: 'Transaction') -> int:
        return self.broadcast_event("new_transaction", {
            "txid":  tx.txid,
            "size":  tx.byte_size(),
        })

    def ws_stats(self) -> dict:
        with self._lock:
            total_msgs = sum(s.messages_sent for s in self._subs.values())
        return {
            "connected_clients": len(self._clients),
            "active_subs":       len(self._subs),
            "sub_types":         self.SUBSCRIPTION_TYPES,
            "total_messages":    total_msgs,
        }


# ---- OrderBookManager
@dataclass
@dataclass
class OrderBookManager:
    """Manages order books for multiple trading pairs."""

    PAIRS = [
        "NBL/USDT", "NBL/BTC", "NBL/ETH",
        "NBL/BNB", "NBL/SOL", "NBL/MATIC",
    ]

    def __init__(self):
        self._books: Dict[str, OrderBook] = {
            pair: OrderBook(pair) for pair in self.PAIRS
        }

    def get_book(self, pair: str) -> Optional[OrderBook]:
        return self._books.get(pair)

    def add_pair(self, pair: str) -> OrderBook:
        if pair not in self._books:
            self._books[pair] = OrderBook(pair)
        return self._books[pair]

    def all_stats(self) -> List[dict]:
        return [book.order_book_stats() for book in self._books.values()]

    def market_summary(self) -> dict:
        total_volume = sum(
            b._vol_24h for b in self._books.values()
        )
        return {
            "pairs":        len(self._books),
            "total_vol_24h": f"{total_volume:.3f}",
            "active_pairs": [p for p, b in self._books.items()
                             if b._last_price > 0],
        }


# ---- GameItem
@dataclass
class GameItem:
    item_id:    str
    owner:      str
    game_id:    str
    item_type:  str
    attributes: dict
    rarity:     str   # common/uncommon/rare/epic/legendary
    level:      int = 1
    experience: int = 0
    tradeable:  bool = True

    RARITY_WEIGHTS = {
        "common": 60, "uncommon": 25, "rare": 10,
        "epic": 4, "legendary": 1
    }

    def to_dict(self) -> dict:
        return {
            "item_id":    self.item_id,
            "owner":      self.owner,
            "game_id":    self.game_id,
            "type":       self.item_type,
            "rarity":     self.rarity,
            "level":      self.level,
            "attributes": self.attributes,
            "tradeable":  self.tradeable,
        }


# ---- NFTGamingEngine
class NFTGamingEngine:
    """
    NFT-based gaming infrastructure for NEBULA.
    On-chain items, crafting, battles, achievements.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  rng: 'OnChainRNG'):
        self._bc    = blockchain
        self._rng   = rng
        self._items: Dict[str, GameItem]  = {}
        self._games: Dict[str, dict]      = {}
        self._achievements: Dict[str, List[str]] = {}
        self._lock  = threading.RLock()

    def register_game(self, game_id: str, name: str,
                       developer: str,
                       item_types: List[str]) -> bool:
        with self._lock:
            self._games[game_id] = {
                "name":       name,
                "developer":  developer,
                "item_types": item_types,
                "created_at": time.time(),
            }
            return True

    def mint_item(self, game_id: str, owner: str,
                   item_type: str,
                   block_height: int = 0) -> Tuple[bool, str]:
        with self._lock:
            game = self._games.get(game_id)
            if not game:
                return False, "Game not registered"
            if item_type not in game["item_types"]:
                return False, f"Invalid item type: {item_type}"
            # Determine rarity using VRF
            rand_val = self._rng.random_int(block_height or 1, 100)
            cum = 0
            rarity = "common"
            for r, w in GameItem.RARITY_WEIGHTS.items():
                cum += w
                if rand_val < cum:
                    rarity = r
                    break
            item_id = hashlib.sha256(
                f"ITEM:{game_id}:{owner}:{item_type}:{time.time()}".encode()
            ).hexdigest()[:16]
            attrs = self._generate_attributes(item_type, rarity, rand_val)
            self._items[item_id] = GameItem(
                item_id    = item_id,
                owner      = owner,
                game_id    = game_id,
                item_type  = item_type,
                attributes = attrs,
                rarity     = rarity,
            )
            return True, item_id

    def _generate_attributes(self, item_type: str,
                              rarity: str, seed: int) -> dict:
        rarity_mult = {"common": 1, "uncommon": 1.5, "rare": 2,
                       "epic": 3, "legendary": 5}.get(rarity, 1)
        base = seed % 50 + 10
        return {
            "power":     int(base * rarity_mult),
            "speed":     int((base + 5) * rarity_mult),
            "defense":   int((base + 3) * rarity_mult),
            "item_type": item_type,
        }

    def level_up(self, item_id: str, xp_gained: int) -> Tuple[bool, str]:
        with self._lock:
            item = self._items.get(item_id)
            if not item:
                return False, "Item not found"
            item.experience += xp_gained
            xp_per_level = 1000
            while item.experience >= item.level * xp_per_level:
                item.experience -= item.level * xp_per_level
                item.level      += 1
                for attr in ("power", "speed", "defense"):
                    if attr in item.attributes:
                        item.attributes[attr] = int(item.attributes[attr] * 1.1)
            return True, f"Item level: {item.level}"

    def transfer_item(self, item_id: str, sender: str,
                       recipient: str) -> Tuple[bool, str]:
        with self._lock:
            item = self._items.get(item_id)
            if not item or item.owner != sender:
                return False, "Not found or not owner"
            if not item.tradeable:
                return False, "Item is not tradeable"
            item.owner = recipient
            return True, f"Transferred {item.item_type} to {recipient}"

    def player_items(self, owner: str,
                      game_id: str = None) -> List[dict]:
        items = [i for i in self._items.values() if i.owner == owner]
        if game_id:
            items = [i for i in items if i.game_id == game_id]
        return [i.to_dict() for i in items]

    def gaming_stats(self) -> dict:
        with self._lock:
            by_rarity = {}
            for item in self._items.values():
                by_rarity[item.rarity] = by_rarity.get(item.rarity, 0) + 1
        return {
            "total_items":  len(self._items),
            "total_games":  len(self._games),
            "by_rarity":    by_rarity,
        }


# ---- CredentialType
class CredentialType(_enum.Enum):
    KYC              = "kyc"
    AGE_VERIFICATION = "age_verification"
    ACCREDITED_INVESTOR = "accredited_investor"
    PROFESSIONAL     = "professional"
    ORGANIZATION     = "organization"
    GOVERNMENT_ID    = "government_id"
    ACADEMIC         = "academic"
    SOCIAL_MEDIA     = "social_media"


# ---- VerifiablePresentation
@dataclass
class VerifiablePresentation:
    vp_id:        str
    holder:       str
    credentials:  List[str]   # credential IDs
    purpose:      str
    challenge:    str         # nonce from verifier
    signature:    bytes
    created_at:   float
    expires:      Optional[float] = None

    def to_dict(self) -> dict:
        return {
            "vp_id":       self.vp_id,
            "holder":      self.holder,
            "credentials": len(self.credentials),
            "purpose":     self.purpose,
            "expires":     self.expires,
        }


# ---- DigitalIdentityV2
class DigitalIdentityV2:
    """
    Advanced digital identity system for NEBULA.
    W3C DID v1.1 compliant with verifiable credentials.
    Selective disclosure, zero-knowledge proofs.
    """

    def __init__(self):
        self._dids:         Dict[str, dict]                    = {}
        self._credentials:  Dict[str, dict]                    = {}
        self._presentations: Dict[str, VerifiablePresentation] = {}
        self._issuers:      Dict[str, dict]                    = {}
        self._lock          = threading.RLock()

    def register_issuer(self, did: str, name: str,
                          credential_types: List[CredentialType]) -> bool:
        with self._lock:
            self._issuers[did] = {
                "did":   did,
                "name":  name,
                "types": [t.value for t in credential_types],
                "issued_count": 0,
            }
            return True

    def issue_credential(self, issuer_did: str,
                          holder_did: str,
                          cred_type: CredentialType,
                          claims: dict,
                          expiry_days: int = 365) -> str:
        with self._lock:
            issuer = self._issuers.get(issuer_did)
            if not issuer:
                raise ValueError("Issuer not registered")
            if cred_type.value not in issuer["types"]:
                raise ValueError(f"Issuer not authorized for {cred_type.value}")
            cid = hashlib.sha256(
                f"CRED:{issuer_did}:{holder_did}:{cred_type.value}:{time.time()}".encode()
            ).hexdigest()[:20]
            self._credentials[cid] = {
                "credential_id": cid,
                "type":          cred_type.value,
                "issuer":        issuer_did,
                "holder":        holder_did,
                "claims":        claims,
                "issued_at":     time.time(),
                "expires":       time.time() + expiry_days * 86400,
                "revoked":       False,
                "schema":        f"https://schema.nebula-nbl.io/{cred_type.value}",
            }
            issuer["issued_count"] += 1
            return cid

    def create_presentation(self, holder: str,
                              credential_ids: List[str],
                              purpose: str, challenge: str,
                              privkey: int,
                              selective_claims: Dict[str, List[str]] = None) -> str:
        """Create a Verifiable Presentation (optionally with selective disclosure)."""
        with self._lock:
            for cid in credential_ids:
                cred = self._credentials.get(cid)
                if not cred or cred["holder"] != holder:
                    raise ValueError(f"Credential {cid} not found for holder")
            # Selective disclosure — only expose specified claims
            disclosed_creds = []
            for cid in credential_ids:
                cred = dict(self._credentials[cid])
                if selective_claims and cid in selective_claims:
                    allowed  = set(selective_claims[cid])
                    cred["claims"] = {
                        k: v for k, v in cred["claims"].items()
                        if k in allowed
                    }
                disclosed_creds.append(cred)
            vp_data = json.dumps({
                "holder":      holder,
                "credentials": disclosed_creds,
                "purpose":     purpose,
                "challenge":   challenge,
            }, sort_keys=True).encode()
            r, s = Secp256k1.sign(privkey, hashlib.sha256(vp_data).digest())
            sig  = Secp256k1.sig_to_der(r, s)
            vpid = hashlib.sha256(vp_data).hexdigest()[:16]
            self._presentations[vpid] = VerifiablePresentation(
                vp_id       = vpid,
                holder      = holder,
                credentials = credential_ids,
                purpose     = purpose,
                challenge   = challenge,
                signature   = sig,
                created_at  = time.time(),
            )
            return vpid

    def revoke_credential(self, cred_id: str,
                           issuer_did: str) -> Tuple[bool, str]:
        with self._lock:
            cred = self._credentials.get(cred_id)
            if not cred or cred["issuer"] != issuer_did:
                return False, "Not found or not issuer"
            cred["revoked"] = True
            return True, f"Credential {cred_id} revoked"

    def verify_presentation(self, vp_id: str,
                              expected_challenge: str) -> Tuple[bool, str]:
        vp = self._presentations.get(vp_id)
        if not vp:
            return False, "Presentation not found"
        if vp.challenge != expected_challenge:
            return False, "Challenge mismatch"
        for cid in vp.credentials:
            cred = self._credentials.get(cid)
            if not cred:
                return False, f"Credential {cid} not found"
            if cred["revoked"]:
                return False, f"Credential {cid} revoked"
            if cred["expires"] < time.time():
                return False, f"Credential {cid} expired"
        return True, "Presentation valid"

    def identity_stats(self) -> dict:
        with self._lock:
            valid   = sum(1 for c in self._credentials.values()
                          if not c["revoked"] and c["expires"] > time.time())
        return {
            "total_credentials": len(self._credentials),
            "valid":             valid,
            "presentations":     len(self._presentations),
            "registered_issuers": len(self._issuers),
        }


# ---- ComplianceCheckType
class ComplianceCheckType(_enum.Enum):
    AML   = "aml"              # Anti-Money Laundering
    KYC   = "kyc"              # Know Your Customer
    OFAC  = "ofac"             # OFAC sanctions check
    FATF  = "fatf"             # FATF travel rule
    PEP   = "pep"              # Politically Exposed Person


# ---- ComplianceRecord
@dataclass
class ComplianceRecord:
    address:    str
    checks:     Dict[str, bool]
    risk_score: float          # 0.0 (clean) - 1.0 (high risk)
    flags:      List[str]
    last_check: float
    kyc_level:  int = 0        # 0=none, 1=basic, 2=enhanced

    def to_dict(self) -> dict:
        return {
            "address":     self.address,
            "risk_score":  f"{self.risk_score:.2f}",
            "risk_level":  "HIGH" if self.risk_score > 0.7
                           else "MEDIUM" if self.risk_score > 0.3
                           else "LOW",
            "flags":       self.flags,
            "kyc_level":   self.kyc_level,
            "last_check":  self.last_check,
        }


# ---- ComplianceEngine
class ComplianceEngine:
    """
    Optional compliance layer for NEBULA.
    Provides AML/KYC tools for regulated applications.
    Note: Decentralized by default — compliance is opt-in.
    """

    HIGH_RISK_AMOUNT = 10_000 * 10**DECIMALS   # flag large txs

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._records: Dict[str, ComplianceRecord] = {}
        self._blacklist: Set[str]                  = set()
        self._whitelist: Set[str]                  = set()
        self._lock     = threading.RLock()

    def run_aml_check(self, address: str) -> ComplianceRecord:
        with self._lock:
            risk   = 0.0
            flags  = []
            # Check blacklist
            if address in self._blacklist:
                risk  = 1.0
                flags.append("BLACKLISTED")
            # Check balance (heuristic: very high balance may indicate mixing)
            bal = self._bc.utxo.balance(address)
            if bal > 1_000_000 * 10**DECIMALS:
                risk   += 0.1
                flags.append("HIGH_BALANCE")
            # Check if whitelisted
            if address in self._whitelist:
                risk   = max(0, risk - 0.3)
                flags.append("WHITELISTED")
            record = ComplianceRecord(
                address    = address,
                checks     = {"aml": risk < 0.7, "blacklist": address not in self._blacklist},
                risk_score = min(1.0, risk),
                flags      = flags,
                last_check = time.time(),
            )
            self._records[address] = record
            return record

    def add_to_blacklist(self, address: str, reason: str = ""):
        with self._lock:
            self._blacklist.add(address)
            if address in self._whitelist:
                self._whitelist.discard(address)

    def add_to_whitelist(self, address: str):
        with self._lock:
            self._whitelist.add(address)
            if address in self._blacklist:
                self._blacklist.discard(address)

    def transaction_check(self, tx: 'Transaction') -> Tuple[bool, str]:
        """Check a transaction for compliance red flags."""
        for out in tx.outputs:
            if out.address and out.address in self._blacklist:
                return False, f"Output to blacklisted address: {out.address}"
        total = sum(o.value for o in tx.outputs)
        if total > self.HIGH_RISK_AMOUNT:
            return True, f"FLAGGED: Large transaction ({total/10**DECIMALS:.0f} NBL)"
        return True, "PASS"

    def travel_rule_check(self, sender: str, recipient: str,
                           amount: int) -> dict:
        """FATF Travel Rule — required for large transfers."""
        threshold = 1000 * 10**DECIMALS   # $1000 equivalent
        if amount < threshold:
            return {"required": False, "amount": amount}
        return {
            "required":  True,
            "amount":    amount,
            "sender":    sender,
            "recipient": recipient,
            "note":      "Travel Rule applies — sender/recipient info required",
        }

    def compliance_stats(self) -> dict:
        with self._lock:
            high_risk = sum(1 for r in self._records.values()
                            if r.risk_score > 0.7)
        return {
            "records_checked": len(self._records),
            "blacklisted":     len(self._blacklist),
            "whitelisted":     len(self._whitelist),
            "high_risk":       high_risk,
        }


# ---- AnalyticsMetric
class AnalyticsMetric(_enum.Enum):
    TVL          = "tvl"
    DAILY_ACTIVE = "dau"
    DAILY_TXS    = "dtx"
    FEES_24H     = "fees_24h"
    GAS_USED     = "gas_used"
    BRIDGE_VOLUME = "bridge_volume"
    DEX_VOLUME   = "dex_volume"
    NFT_VOLUME   = "nft_volume"


# ---- AnalyticsV2
class AnalyticsV2:
    """
    Advanced analytics engine for NEBULA ecosystem.
    Tracks TVL, DAU, DEX volume, NFT metrics, DeFi health.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc       = blockchain
        self._oracle   = oracle
        self._daily_data: Dict[str, Dict[str, float]] = {}   # date -> metrics
        self._lock      = threading.RLock()

    def record_daily_snapshot(self):
        """Take a daily snapshot of all key metrics."""
        today = time.strftime('%Y-%m-%d')
        bc    = self._bc
        nbl_price = (self._oracle.price("NBL/USD")
                     if self._oracle else 0.01)
        with self._lock:
            self._daily_data[today] = {
                "height":      bc.height,
                "mempool_txs": bc.mempool.size(),
                "utxo_count":  bc.utxo.size(),
                "total_supply": bc.utxo.total_supply() / 10**DECIMALS,
                "nbl_price_usd": nbl_price,
                "market_cap":  bc.utxo.total_supply() / 10**DECIMALS * nbl_price,
                "timestamp":   time.time(),
            }

    def tvl_estimate(self, staking: 'StakingEngine' = None,
                      dex: 'NEBULADex' = None,
                      lending: 'LendingProtocol' = None) -> dict:
        """Estimate Total Value Locked across protocols."""
        nbl_price = (self._oracle.price("NBL/USD")
                     if self._oracle else 0.01)
        tvl_nbl = 0.0
        breakdown = {}
        if staking:
            stk_stats = staking.staking_stats()
            stk_nbl   = float(stk_stats.get("total_staked_nbl", "0 NBL").split()[0])
            tvl_nbl  += stk_nbl
            breakdown["staking"] = f"${stk_nbl * nbl_price:,.0f}"
        if dex:
            dex_stats = dex.dex_stats()
            liq_nbl   = float(dex_stats.get("total_liquidity_nbl", "0").split()[0])
            tvl_nbl  += liq_nbl
            breakdown["dex"] = f"${liq_nbl * nbl_price:,.0f}"
        tvl_usd = tvl_nbl * nbl_price
        return {
            "total_nbl":    f"{tvl_nbl:,.3f}",
            "total_usd":    f"${tvl_usd:,.0f}",
            "breakdown":    breakdown,
            "nbl_price":    f"${nbl_price:.4f}",
        }

    def protocol_health(self) -> dict:
        """Overall protocol health score (0-100)."""
        bc     = self._bc
        score  = 0.0
        checks = {}
        # Chain liveness (0-30)
        chain_score = min(30, bc.height / 1000 * 30)
        score      += chain_score
        checks["chain_activity"] = f"{chain_score:.0f}/30"
        # Mempool health (0-20)
        mp     = bc.mempool.size()
        mp_score = 20 if mp < 1000 else max(0, 20 - (mp - 1000) / 500)
        score += mp_score
        checks["mempool"] = f"{mp_score:.0f}/20"
        # UTXO set (0-20)
        utxo_score = min(20, bc.utxo.size() / 100)
        score      += utxo_score
        checks["utxo_set"] = f"{utxo_score:.0f}/20"
        # Supply health (0-30)
        supply = bc.utxo.total_supply() / MAX_SUPPLY * 100
        supply_score = 30 if supply < 50 else max(0, 30 - (supply - 50))
        score += supply_score
        checks["supply_dist"] = f"{supply_score:.0f}/30"
        return {
            "score":     f"{score:.0f}/100",
            "grade":     "A" if score >= 80 else "B" if score >= 60
                         else "C" if score >= 40 else "D",
            "checks":    checks,
        }

    def growth_metrics(self) -> dict:
        """Calculate growth metrics from daily snapshots."""
        with self._lock:
            days = sorted(self._daily_data.keys())
        if len(days) < 2:
            return {"note": "Insufficient data for growth metrics"}
        first = self._daily_data[days[0]]
        last  = self._daily_data[days[-1]]
        return {
            "days_tracked":   len(days),
            "block_growth":   last["height"] - first["height"],
            "supply_growth":  f"{last['total_supply'] - first['total_supply']:.3f} NBL",
        }

    def analytics_summary(self) -> dict:
        self.record_daily_snapshot()
        today = time.strftime('%Y-%m-%d')
        snap  = self._daily_data.get(today, {})
        health = self.protocol_health()
        return {
            "snapshot":       snap,
            "health_score":   health["score"],
            "health_grade":   health["grade"],
        }
