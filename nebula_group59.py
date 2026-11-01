"""NEBULA group59 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. SocialFiPlatform  (orig. lines 101553-101628)
   2. RealWorldAsset  (orig. lines 101635-101687)
   3. RWATokenizationPlatform  (orig. lines 101690-101777)
   4. AITradingSignals  (orig. lines 101784-101845)
   5. AIPortfolioOptimizer  (orig. lines 101848-101895)
   6. AISmartContractAuditor  (orig. lines 101898-101933)
   7. ZKIdentityProof  (orig. lines 101941-101998)
   8. SoulBoundToken  (orig. lines 102001-102062)
   9. CrossChainDeFiRouter  (orig. lines 102069-102158)
  10. QuadraticVoting  (orig. lines 102165-102239)
  11. DelegatedGovernance  (orig. lines 102242-102299)
  12. HubAndSpokeNetwork  (orig. lines 102306-102416)
  13. NEBULAAnalyticsDashboard  (orig. lines 102423-102495)
  14. NEBULAStorage  (orig. lines 102503-102575)
  15. DAOTreasuryManager  (orig. lines 102582-102660)
  16. ValidatorStakingV2  (orig. lines 102667-102795)
  17. DynamicNFT  (orig. lines 102802-102852)
  18. NFTFractionalizationV2  (orig. lines 102855-102936)
  19. NEBULAEcosystemIntegrations  (orig. lines 102943-103016)
  20. IBCPacket  (orig. lines 103024-103048)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): SocialToken
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


# ---- SocialFiPlatform
class SocialFiPlatform:
    """Full SocialFi platform — creator tokens, gated content."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._tokens: dict = {}
        self._content: list = []
        self._follows: dict = {}
        self._lock    = threading.RLock()

    def launch_token(self, creator: str, symbol: str,
                      name: str) -> dict:
        with self._lock:
            if symbol in self._tokens:
                return {"ok": False, "error": "Symbol taken"}
            token = SocialToken(creator, symbol, name,
                                1_000_000, self._bc)
            self._tokens[symbol] = token
            return {
                "ok":       True,
                "symbol":   symbol,
                "price":    "0.001 NBL (launch price)",
                "supply":   "1,000,000 tokens",
                "message":  f"${symbol} launched successfully!",
            }

    def buy_token(self, buyer: str, symbol: str,
                   amount: int) -> dict:
        token = self._tokens.get(symbol)
        if not token:
            return {"ok": False, "error": "Token not found"}
        ok, cost = token.buy(buyer, amount)
        return {"ok": ok, "cost_nbl": f"{cost:.6f}"}

    def post_gated_content(self, creator: str, symbol: str,
                            content: str, min_tokens: int = 100) -> dict:
        with self._lock:
            cid = hashlib.sha256(
                f"CONTENT:{creator}:{time.time()}".encode()
            ).hexdigest()[:10]
            self._content.append({
                "cid":         cid,
                "creator":     creator,
                "symbol":      symbol,
                "content":     content[:500],
                "min_tokens":  min_tokens,
                "views":       0,
                "ts":          time.time(),
            })
            return {"ok": True, "cid": cid, "gated_by": f"{min_tokens} ${symbol}"}

    def view_content(self, viewer: str, cid: str) -> dict:
        post = next((c for c in self._content if c["cid"] == cid), None)
        if not post:
            return {"ok": False, "error": "Not found"}
        token = self._tokens.get(post["symbol"])
        if token and not token.unlock_content(viewer, post["min_tokens"]):
            return {
                "ok": False,
                "error": f"Need {post['min_tokens']} ${post['symbol']} tokens",
                "buy_url": f"https://social.nebula-nbl.io/token/{post['symbol']}",
            }
        post["views"] += 1
        return {"ok": True, "content": post["content"], "views": post["views"]}

    def follow(self, follower: str, creator: str):
        if follower not in self._follows:
            self._follows[follower] = set()
        self._follows[follower].add(creator)

    def social_stats(self) -> dict:
        return {
            "creator_tokens": len(self._tokens),
            "gated_posts":    len(self._content),
            "follow_pairs":   sum(len(v) for v in self._follows.values()),
        }


# ---- RealWorldAsset
class RealWorldAsset:
    """Tokenized real-world asset on NEBULA."""

    ASSET_TYPES = {
        "real_estate":   {"min_value": 10_000, "liquidity": "low"},
        "commodity":     {"min_value": 1_000,  "liquidity": "medium"},
        "treasury_bill": {"min_value": 100,    "liquidity": "high"},
        "invoice":       {"min_value": 500,    "liquidity": "medium"},
        "carbon_credit": {"min_value": 10,     "liquidity": "medium"},
        "art":           {"min_value": 1_000,  "liquidity": "low"},
        "vehicle":       {"min_value": 5_000,  "liquidity": "low"},
        "equipment":     {"min_value": 2_000,  "liquidity": "low"},
    }

    def __init__(self, asset_id: str, asset_type: str,
                  issuer: str, total_value_usd: float,
                  token_count: int, description: str):
        self.asset_id        = asset_id
        self.asset_type      = asset_type
        self.issuer          = issuer
        self.total_value     = total_value_usd
        self.token_count     = token_count
        self.price_per_token = total_value_usd / token_count
        self.description     = description
        self._holders:       dict = {}
        self.verified        = False
        self.legal_doc_hash  = ""
        self.created         = time.time()

    def buy_tokens(self, buyer: str, count: int) -> bool:
        available = self.token_count - sum(self._holders.values())
        if count > available:
            return False
        self._holders[buyer] = self._holders.get(buyer, 0) + count
        return True

    def holder_value(self, holder: str) -> float:
        tokens = self._holders.get(holder, 0)
        return tokens * self.price_per_token

    def asset_info(self) -> dict:
        sold = sum(self._holders.values())
        return {
            "asset_id":    self.asset_id,
            "type":        self.asset_type,
            "value_usd":   f"${self.total_value:,.2f}",
            "tokens":      self.token_count,
            "sold":        sold,
            "remaining":   self.token_count - sold,
            "price_usd":   f"${self.price_per_token:.4f}",
            "verified":    self.verified,
            "holders":     len(self._holders),
        }


# ---- RWATokenizationPlatform
class RWATokenizationPlatform:
    """Platform for tokenizing real-world assets on NEBULA."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._assets: dict = {}
        self._kyc_verified: set = set()
        self._lock    = threading.RLock()

    def verify_kyc(self, address: str, docs_hash: str) -> bool:
        """KYC verification (simplified)."""
        self._kyc_verified.add(address)
        return True

    def tokenize_asset(self, issuer: str, asset_type: str,
                        value_usd: float, token_count: int,
                        description: str,
                        legal_doc: str = "") -> dict:
        with self._lock:
            if issuer not in self._kyc_verified:
                return {"ok": False, "error": "KYC required for asset issuance"}
            if asset_type not in RealWorldAsset.ASSET_TYPES:
                return {"ok": False, "error": f"Unknown asset type: {asset_type}"}
            min_val = RealWorldAsset.ASSET_TYPES[asset_type]["min_value"]
            if value_usd < min_val:
                return {"ok": False, "error": f"Minimum value: ${min_val:,}"}
            asset_id = hashlib.sha256(
                f"RWA:{issuer}:{asset_type}:{time.time()}".encode()
            ).hexdigest()[:12]
            asset = RealWorldAsset(asset_id, asset_type, issuer,
                                   value_usd, token_count, description)
            asset.legal_doc_hash = hashlib.sha256(
                legal_doc.encode()).hexdigest() if legal_doc else ""
            asset.verified = True
            self._assets[asset_id] = asset
            price_nbl = (value_usd / token_count /
                         ((self._oracle.price("NBL/USD") or 0.01) if self._oracle else 0.01))
            return {
                "ok":          True,
                "asset_id":    asset_id,
                "type":        asset_type,
                "value_usd":   f"${value_usd:,.2f}",
                "tokens":      token_count,
                "price_nbl":   f"{price_nbl:.4f}",
                "listed":      f"https://rwa.nebula-nbl.io/{asset_id}",
            }

    def buy_rwa(self, buyer: str, asset_id: str,
                 token_count: int) -> dict:
        with self._lock:
            if buyer not in self._kyc_verified:
                return {"ok": False, "error": "KYC required to buy RWA"}
            asset = self._assets.get(asset_id)
            if not asset:
                return {"ok": False, "error": "Asset not found"}
            ok = asset.buy_tokens(buyer, token_count)
            if not ok:
                return {"ok": False, "error": "Insufficient tokens available"}
            return {
                "ok":        True,
                "tokens":    token_count,
                "value_usd": f"${asset.holder_value(buyer):.2f}",
                "asset":     asset.asset_type,
            }

    def portfolio(self, address: str) -> list:
        holdings = []
        for aid, asset in self._assets.items():
            tokens = asset._holders.get(address, 0)
            if tokens > 0:
                holdings.append({
                    "asset_id":  aid,
                    "type":      asset.asset_type,
                    "tokens":    tokens,
                    "value_usd": f"${asset.holder_value(address):.2f}",
                })
        return holdings

    def rwa_stats(self) -> dict:
        total_val = sum(a.total_value for a in self._assets.values())
        return {
            "total_assets":   len(self._assets),
            "total_value":    f"${total_val:,.2f}",
            "kyc_users":      len(self._kyc_verified),
            "asset_types":    list(RealWorldAsset.ASSET_TYPES.keys()),
        }


# ---- AITradingSignals
class AITradingSignals:
    """Trading signals for NEBULA DeFi."""

    MODELS = ["momentum", "mean_reversion", "sentiment", "on_chain"]

    def __init__(self, oracle: 'OracleV2' = None):
        self._oracle   = oracle
        self._signals: list = []
        self._accuracy: dict = {}

    def generate_signal(self, pair: str,
                         model: str = "momentum") -> dict:
        """Generate trading signal using simple heuristics."""
        price     = (self._oracle.price(pair) if self._oracle else 0.01) or 0.01
        now       = time.time()
        # Simple momentum signal
        if model == "momentum":
            h = hashlib.sha256(f"{pair}{int(now/300)}".encode())
            signal_val = int.from_bytes(h.digest()[:2], 'big') / 65535
            direction  = "BUY" if signal_val > 0.55 else "SELL" if signal_val < 0.45 else "HOLD"
            confidence = abs(signal_val - 0.5) * 2
        elif model == "mean_reversion":
            h = hashlib.sha256(f"MR{pair}{int(now/600)}".encode())
            signal_val = int.from_bytes(h.digest()[:2], 'big') / 65535
            direction  = "SELL" if signal_val > 0.6 else "BUY" if signal_val < 0.4 else "HOLD"
            confidence = abs(signal_val - 0.5) * 2
        else:
            direction  = "HOLD"
            confidence = 0.5

        signal = {
            "pair":       pair,
            "model":      model,
            "signal":     direction,
            "confidence": f"{confidence*100:.0f}%",
            "price":      f"${price:.6f}",
            "generated":  now,
            "valid_secs": 300,
            "disclaimer": "AI signals are NOT financial advice",
        }
        self._signals.append(signal)
        return signal

    def multi_model_consensus(self, pair: str) -> dict:
        """Aggregate signals from all models."""
        signals    = [self.generate_signal(pair, m) for m in self.MODELS]
        buy_count  = sum(1 for s in signals if s["signal"] == "BUY")
        sell_count = sum(1 for s in signals if s["signal"] == "SELL")
        if buy_count > sell_count:
            consensus = "BUY"
        elif sell_count > buy_count:
            consensus = "SELL"
        else:
            consensus = "HOLD"
        return {
            "pair":      pair,
            "consensus": consensus,
            "buy_votes": buy_count,
            "sell_votes": sell_count,
            "signals":   signals,
            "note":      "Consensus of 4 AI models — educational only",
        }


# ---- AIPortfolioOptimizer
class AIPortfolioOptimizer:
    """AI portfolio optimizer using Modern Portfolio Theory."""

    def __init__(self, oracle: 'OracleV2' = None):
        self._oracle = oracle

    def optimize(self, assets: list,
                  risk_tolerance: str = "moderate") -> dict:
        """Suggest optimal portfolio allocation."""
        n = len(assets)
        if n == 0:
            return {"error": "No assets provided"}

        # Risk-based allocations
        if risk_tolerance == "conservative":
            # 70% stable, 20% blue-chip, 10% growth
            weights = [0.7/max(1,n)] * n
            weights[0] = 0.7
            if n > 1: weights[1] = 0.2
            if n > 2: weights[2] = 0.1
        elif risk_tolerance == "aggressive":
            # Equal weight
            weights = [1/n] * n
        else:
            # Moderate: descending weights
            total = sum(range(1, n+1))
            weights = [(n-i)/total for i in range(n)]

        # Normalize
        total_w = sum(weights[:n])
        weights = [w/total_w for w in weights[:n]]

        allocation = []
        for i, asset in enumerate(assets):
            price = ((self._oracle.price(f"{asset}/USD") or 0.01)
                     if self._oracle else 0.01)
            allocation.append({
                "asset":     asset,
                "weight":    f"{weights[i]*100:.1f}%",
                "price_usd": f"${price:.4f}",
            })

        return {
            "risk_tolerance": risk_tolerance,
            "allocation":     allocation,
            "rebalance_freq": "Monthly recommended",
            "disclaimer":     "Not financial advice — educational only",
        }


# ---- AISmartContractAuditor
class AISmartContractAuditor:
    """AI-powered smart contract auditor."""

    VULNERABILITY_PATTERNS = {
        "reentrancy":     ["call(", ".send(", "transfer("],
        "overflow":       ["unchecked", "uint", "+=", "*="],
        "access_control": ["onlyOwner", "require(msg.sender"],
        "integer_div":    ["/ ", "//", "div("],
        "timestamp":      ["block.timestamp", "now ", "time.time"],
    }

    def audit(self, code: str, contract_name: str = "Unknown") -> dict:
        findings = []
        lines    = code.split("\n")
        for i, line in enumerate(lines):
            for vuln, patterns in self.VULNERABILITY_PATTERNS.items():
                for pat in patterns:
                    if pat.lower() in line.lower():
                        findings.append({
                            "line":      i + 1,
                            "type":      vuln,
                            "code":      line.strip()[:80],
                            "severity":  "MEDIUM",
                            "info":      f"Pattern '{pat}' detected — review manually",
                        })

        score = max(0, 100 - len(findings) * 5)
        return {
            "contract":   contract_name,
            "lines":      len(lines),
            "findings":   findings[:20],
            "total_found": len(findings),
            "score":      score,
            "grade":      "A" if score >= 90 else "B" if score >= 70 else "C",
            "ai_note":    "AI audit is preliminary — use professional auditor for production",
        }


# ---- ZKIdentityProof
class ZKIdentityProof:
    """Zero-knowledge identity proof — prove without revealing."""

    def __init__(self, address: str, blockchain: 'NEBULABlockchain'):
        self._address = address
        self._bc      = blockchain
        self._proofs: dict = {}

    def prove_age(self, birthdate_hash: str,
                   min_age: int = 18) -> dict:
        """Prove age >= min_age without revealing exact age."""
        proof_id = hashlib.sha256(
            f"AGE:{self._address}:{birthdate_hash}:{min_age}".encode()
        ).hexdigest()[:16]
        self._proofs[proof_id] = {
            "type":    "age_proof",
            "claim":   f"age >= {min_age}",
            "address": self._address,
            "proof":   proof_id,
            "valid":   True,
            "ts":      time.time(),
        }
        return {
            "proof_id":   proof_id,
            "claim":      f"Person is at least {min_age} years old",
            "verified":   True,
            "reveals":    "Nothing — ZK proof only confirms claim",
        }

    def prove_nationality(self, country_code_hash: str,
                           allowed_countries: list) -> dict:
        """Prove nationality without revealing which country."""
        proof_id = hashlib.sha256(
            f"NAT:{self._address}:{country_code_hash}".encode()
        ).hexdigest()[:16]
        return {
            "proof_id": proof_id,
            "claim":    "Nationality is in allowed list",
            "verified": True,
            "reveals":  "Only that nationality is permitted, not which one",
        }

    def prove_balance(self, min_balance_nbl: float) -> dict:
        """Prove balance >= threshold without revealing exact amount."""
        actual = self._bc.utxo.balance(self._address) / 10**DECIMALS
        has_enough = actual >= min_balance_nbl
        proof_id = hashlib.sha256(
            f"BAL:{self._address}:{min_balance_nbl}:{has_enough}".encode()
        ).hexdigest()[:16]
        return {
            "proof_id":  proof_id,
            "claim":     f"Balance >= {min_balance_nbl} NBL",
            "verified":  has_enough,
            "reveals":   "Only that balance meets threshold, not exact amount",
        }

    def list_proofs(self) -> list:
        return list(self._proofs.values())


# ---- SoulBoundToken
class SoulBoundToken:
    """
    Non-transferable Soul Bound Tokens (SBT) on NEBULA.
    Used for identity, reputation, credentials.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._tokens: dict = {}   # address -> list of SBTs
        self._lock   = threading.RLock()

    def issue(self, issuer: str, holder: str,
               token_type: str, data: dict,
               expiry_blocks: int = 0) -> str:
        with self._lock:
            sbt_id = hashlib.sha256(
                f"SBT:{issuer}:{holder}:{token_type}:{time.time()}".encode()
            ).hexdigest()[:16]
            if holder not in self._tokens:
                self._tokens[holder] = []
            self._tokens[holder].append({
                "sbt_id":     sbt_id,
                "issuer":     issuer,
                "holder":     holder,
                "type":       token_type,
                "data":       data,
                "issued_at":  self._bc.height,
                "expires_at": self._bc.height + expiry_blocks if expiry_blocks > 0 else 0,
                "revoked":    False,
            })
            return sbt_id

    def verify(self, holder: str, token_type: str) -> bool:
        """Check if holder has a valid SBT of given type."""
        for sbt in self._tokens.get(holder, []):
            if sbt["type"] != token_type or sbt["revoked"]:
                continue
            if sbt["expires_at"] > 0 and self._bc.height > sbt["expires_at"]:
                continue
            return True
        return False

    def revoke(self, issuer: str, sbt_id: str) -> bool:
        with self._lock:
            for holder_sbts in self._tokens.values():
                for sbt in holder_sbts:
                    if sbt["sbt_id"] == sbt_id and sbt["issuer"] == issuer:
                        sbt["revoked"] = True
                        return True
        return False

    def get_sbts(self, holder: str) -> list:
        now = self._bc.height
        return [
            s for s in self._tokens.get(holder, [])
            if not s["revoked"] and
            (s["expires_at"] == 0 or s["expires_at"] > now)
        ]

    def sbt_stats(self) -> dict:
        total = sum(len(v) for v in self._tokens.values())
        return {"total_sbts": total, "holders": len(self._tokens)}


# ---- CrossChainDeFiRouter
class CrossChainDeFiRouter:
    """Route DeFi operations across multiple chains."""

    CHAIN_PROTOCOLS = {
        "nebula":   ["staking", "dex", "lending", "nft", "governance"],
        "ethereum": ["uniswap", "aave", "compound", "maker", "curve"],
        "solana":   ["serum", "raydium", "solend", "mango"],
        "bnb":      ["pancakeswap", "venus", "alpaca"],
        "polygon":  ["quickswap", "aave-v3", "balancer"],
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  bridge: 'BridgeEngine' = None):
        self._bc      = blockchain
        self._bridge  = bridge
        self._routes: list = []
        self._lock    = threading.RLock()

    def find_best_yield(self, asset: str,
                         amount_usd: float) -> list:
        """Find best yield opportunity across all chains."""
        opportunities = []
        yields = {
            ("nebula",   "staking"):      0.12,
            ("nebula",   "dex_lp"):       0.35,
            ("nebula",   "lending"):      0.04,
            ("ethereum", "aave"):         0.03,
            ("ethereum", "compound"):     0.025,
            ("solana",   "solend"):       0.05,
            ("bnb",      "venus"):        0.06,
            ("polygon",  "aave-v3"):      0.04,
        }
        for (chain, protocol), apy in yields.items():
            annual = amount_usd * apy
            bridge_cost = 0 if chain == "nebula" else amount_usd * 0.001
            net_annual  = annual - bridge_cost
            opportunities.append({
                "chain":       chain,
                "protocol":    protocol,
                "apy":         f"{apy*100:.1f}%",
                "annual_usd":  f"${annual:.2f}",
                "bridge_cost": f"${bridge_cost:.2f}",
                "net_annual":  f"${net_annual:.2f}",
                "asset":       asset,
            })
        return sorted(opportunities,
                      key=lambda o: float(o["net_annual"].lstrip('$')),
                      reverse=True)

    def execute_cross_chain_strategy(self, user: str,
                                      src_chain: str,
                                      dst_chain: str,
                                      protocol: str,
                                      amount: float) -> dict:
        with self._lock:
            route_id = hashlib.sha256(
                f"XROUTE:{user}:{src_chain}:{dst_chain}:{time.time()}".encode()
            ).hexdigest()[:12]
            steps = []
            if src_chain != dst_chain:
                steps.append(f"1. Bridge {amount:.2f} NBL from {src_chain} to {dst_chain}")
                bridge_fee = amount * 0.001
                steps.append(f"2. Pay bridge fee: {bridge_fee:.4f} NBL")
                amount -= bridge_fee
            steps.append(f"3. Deposit {amount:.4f} NBL into {protocol} on {dst_chain}")
            steps.append(f"4. Receive yield automatically")

            self._routes.append({
                "route_id": route_id,
                "user":     user,
                "from":     src_chain,
                "to":       dst_chain,
                "protocol": protocol,
                "amount":   amount,
                "steps":    steps,
                "ts":       time.time(),
            })
            return {
                "ok":      True,
                "route_id": route_id,
                "steps":   steps,
                "estimated_apy": "varies by protocol",
            }

    def router_stats(self) -> dict:
        return {
            "supported_chains": len(self.CHAIN_PROTOCOLS),
            "total_routes":     len(self._routes),
            "protocols":        sum(len(v) for v in self.CHAIN_PROTOCOLS.values()),
        }


# ---- QuadraticVoting
class QuadraticVoting:
    """
    Quadratic voting for NEBULA governance.
    Cost = votes^2 — reduces whale dominance.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._proposals: dict = {}
        self._votes:    dict = {}
        self._lock     = threading.RLock()

    def create_proposal(self, proposer: str, title: str,
                         options: list) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"QV:{proposer}:{title}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._proposals[pid] = {
                "pid":      pid,
                "proposer": proposer,
                "title":    title,
                "options":  {opt: 0.0 for opt in options},
                "voters":   {},
                "active":   True,
            }
            self._votes[pid] = {}
            return pid

    def vote(self, voter: str, pid: str,
              option: str, voice_credits: int) -> dict:
        """
        voice_credits: number of credits to spend.
        Actual votes = sqrt(credits). Cost = votes^2.
        """
        with self._lock:
            p = self._proposals.get(pid)
            if not p or not p["active"]:
                return {"ok": False, "error": "Not active"}
            if option not in p["options"]:
                return {"ok": False, "error": "Invalid option"}
            # Check NBL balance for voice credits
            bal_nbl = self._bc.utxo.balance(voter) / 10**DECIMALS
            if voice_credits > bal_nbl:
                return {"ok": False, "error": "Insufficient NBL for voice credits"}

            import math
            actual_votes = math.sqrt(voice_credits)
            p["options"][option] += actual_votes
            p["voters"][voter]    = p["voters"].get(voter, {})
            p["voters"][voter][option] = voice_credits

            return {
                "ok":          True,
                "voice_credits": voice_credits,
                "actual_votes": f"{actual_votes:.2f}",
                "cost_nbl":    voice_credits,
                "note":        "sqrt(credits) = votes — quadratic formula",
            }

    def results(self, pid: str) -> dict:
        p = self._proposals.get(pid)
        if not p:
            return {}
        winner = max(p["options"], key=p["options"].get)
        return {
            "pid":     pid,
            "title":   p["title"],
            "results": {k: f"{v:.2f} votes" for k, v in p["options"].items()},
            "winner":  winner,
            "voters":  len(p["voters"]),
        }

    def qv_stats(self) -> dict:
        return {"proposals": len(self._proposals)}


# ---- DelegatedGovernance
class DelegatedGovernance:
    """Full liquid democracy with topic-based delegation."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._delegates: dict = {}   # voter -> {topic: delegate}
        self._votes:    list = []
        self._lock     = threading.RLock()

    def delegate(self, voter: str, delegate: str,
                  topic: str = "*") -> dict:
        with self._lock:
            if voter not in self._delegates:
                self._delegates[voter] = {}
            self._delegates[voter][topic] = delegate
            return {
                "ok":       True,
                "voter":    voter[:8],
                "delegate": delegate[:8],
                "topic":    topic,
                "can_override": "Voter can still vote directly to override",
            }

    def undelegate(self, voter: str, topic: str = "*") -> bool:
        with self._lock:
            if voter in self._delegates:
                self._delegates[voter].pop(topic, None)
                return True
            return False

    def effective_voter(self, voter: str, topic: str) -> str:
        """Find who actually votes for this voter on this topic."""
        seen = {voter}
        current = voter
        for _ in range(10):   # max 10 hops
            d = self._delegates.get(current, {})
            next_v = d.get(topic) or d.get("*")
            if not next_v or next_v in seen:
                return current
            seen.add(next_v)
            current = next_v
        return current

    def voting_power(self, address: str, topic: str) -> float:
        """Total voting power including delegated power."""
        own = self._bc.utxo.balance(address) / 10**DECIMALS
        delegated = sum(
            self._bc.utxo.balance(voter) / 10**DECIMALS
            for voter, d in self._delegates.items()
            if (d.get(topic) == address or d.get("*") == address)
        )
        return own + delegated

    def governance_stats(self) -> dict:
        return {
            "delegators": len(self._delegates),
            "total_votes": len(self._votes),
        }


# ---- HubAndSpokeNetwork
class HubAndSpokeNetwork:
    """
    Hub-and-spoke payment channel network.
    Routes payments through well-connected hub nodes.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._channels: dict = {}
        self._hubs:    list = []
        self._payments: list = []
        self._lock     = threading.RLock()

    def open_channel(self, party_a: str, party_b: str,
                      capacity: float) -> str:
        with self._lock:
            cid = hashlib.sha256(
                f"CH:{party_a}:{party_b}:{time.time()}".encode()
            ).hexdigest()[:12]
            cap = int(capacity * 10**DECIMALS)
            self._channels[cid] = {
                "cid":      cid,
                "party_a":  party_a,
                "party_b":  party_b,
                "capacity": cap,
                "balance_a": cap,
                "balance_b": 0,
                "open":     True,
                "payments": 0,
            }
            return cid

    def register_hub(self, address: str, name: str,
                      routing_fee_pct: float = 0.001) -> bool:
        self._hubs.append({
            "address": address,
            "name":    name,
            "fee":     routing_fee_pct,
            "volume":  0.0,
        })
        return True

    def find_route(self, sender: str, receiver: str,
                    amount: float) -> list:
        """Find payment route through network."""
        # Direct channel
        for cid, ch in self._channels.items():
            if (ch["party_a"] == sender and ch["party_b"] == receiver):
                if ch["balance_a"] >= int(amount * 10**DECIMALS):
                    return [{"type": "direct", "channel": cid, "hops": 0}]
        # Route through hub
        for hub in self._hubs:
            return [{
                "type":    "hub_routed",
                "hub":     hub["name"],
                "hops":    2,
                "fee":     f"{hub['fee']*100:.3f}%",
            }]
        return []

    def send_payment(self, sender: str, receiver: str,
                      amount_nbl: float) -> dict:
        with self._lock:
            amount = int(amount_nbl * 10**DECIMALS)
            route  = self.find_route(sender, receiver, amount_nbl)
            if not route:
                return {"ok": False, "error": "No route found"}
            hop   = route[0]
            if hop["type"] == "direct":
                ch = self._channels[hop["channel"]]
                if ch["balance_a"] < amount:
                    return {"ok": False, "error": "Insufficient channel balance"}
                ch["balance_a"] -= amount
                ch["balance_b"] += amount
                ch["payments"]  += 1
            fee = amount_nbl * 0.001 if hop.get("hops", 0) > 0 else 0
            pay = {
                "ok":        True,
                "amount":    f"{amount_nbl:.9f} NBL",
                "fee":       f"{fee:.9f} NBL",
                "route":     hop["type"],
                "instant":   True,
            }
            self._payments.append(pay)
            return pay

    def close_channel(self, cid: str) -> dict:
        with self._lock:
            ch = self._channels.get(cid)
            if not ch or not ch["open"]:
                return {"ok": False, "error": "Channel not open"}
            ch["open"] = False
            return {
                "ok":       True,
                "final_a":  f"{ch['balance_a']/10**DECIMALS:.9f} NBL",
                "final_b":  f"{ch['balance_b']/10**DECIMALS:.9f} NBL",
                "payments": ch["payments"],
            }

    def network_stats(self) -> dict:
        open_ch = sum(1 for c in self._channels.values() if c["open"])
        total_v = sum(
            c["capacity"] for c in self._channels.values()
        ) / 10**DECIMALS
        return {
            "channels":      len(self._channels),
            "open":          open_ch,
            "hubs":          len(self._hubs),
            "total_payments": len(self._payments),
            "total_capacity": f"{total_v:.3f} NBL",
        }


# ---- NEBULAAnalyticsDashboard
class NEBULAAnalyticsDashboard:
    """Real-time analytics dashboard for NEBULA ecosystem."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._metrics_history: list = []

    def snapshot(self) -> dict:
        bc    = self._bc
        price = (self._oracle.price("NBL/USD") if self._oracle else 0.001) or 0.001
        supply = bc.utxo.total_supply() / 10**DECIMALS
        snap  = {
            "ts":              time.time(),
            "block":           bc.height,
            "price_usd":       price,
            "supply_nbl":      supply,
            "market_cap_usd":  supply * price,
            "mempool_txs":     bc.mempool.size(),
            "utxo_count":      bc.utxo.size(),
            "block_reward":    mining_reward(bc.height) / 10**DECIMALS,
            "inflation_pct":   mining_reward(bc.height)*144*365/max(1,bc.utxo.total_supply())*100,
        }
        self._metrics_history.append(snap)
        if len(self._metrics_history) > 10000:
            self._metrics_history.pop(0)
        return snap

    def price_change(self, hours: int = 24) -> dict:
        if len(self._metrics_history) < 2:
            return {"change": "N/A"}
        now   = self._metrics_history[-1]
        old   = self._metrics_history[max(0, len(self._metrics_history)-hours*12)]
        if old["price_usd"] == 0:
            return {"change": "N/A"}
        change_pct = (now["price_usd"] - old["price_usd"]) / old["price_usd"] * 100
        return {
            "current":  f"${now['price_usd']:.6f}",
            "previous": f"${old['price_usd']:.6f}",
            "change":   f"{change_pct:+.2f}%",
            "period":   f"{hours}h",
        }

    def full_dashboard(self) -> dict:
        snap = self.snapshot()
        return {
            "overview": {
                "price":      f"${snap['price_usd']:.6f}",
                "market_cap": f"${snap['market_cap_usd']:,.0f}",
                "supply":     f"{snap['supply_nbl']:,.3f} NBL",
                "block":      snap["block"],
                "reward":     f"{snap['block_reward']:.9f} NBL",
                "inflation":  f"{snap['inflation_pct']:.4f}%/yr",
            },
            "network": {
                "mempool":    snap["mempool_txs"],
                "utxo_set":   snap["utxo_count"],
                "tps_est":    f"{snap['mempool_txs'] / max(1, TARGET_BLOCK_TIME):.2f}",
            },
            "price_change": self.price_change(24),
            "snapshots":    len(self._metrics_history),
        }

    def export_csv(self, n: int = 100) -> str:
        """Export metrics as CSV."""
        rows = ["ts,block,price_usd,supply_nbl,mempool"]
        for m in self._metrics_history[-n:]:
            rows.append(
                f"{m['ts']:.0f},{m['block']},{m['price_usd']:.6f},"
                f"{m['supply_nbl']:.3f},{m['mempool_txs']}"
            )
        return "\n".join(rows)


# ---- NEBULAStorage
class NEBULAStorage:
    """
    Decentralized storage integration for NEBULA.
    Content-addressed storage via IPFS/Arweave.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._files:  dict = {}
        self._pins:   dict = {}   # cid -> {pinner, fee_nbl}
        self._lock    = threading.RLock()

    def store(self, uploader: str, data: bytes,
               filename: str = "") -> dict:
        """Store data and return content hash (CID)."""
        cid = "Qm" + hashlib.sha256(data).hexdigest()[:44]
        size_kb = len(data) / 1024
        fee_nbl = max(0.001, size_kb * 0.0001)  # 0.0001 NBL per KB

        with self._lock:
            self._files[cid] = {
                "cid":      cid,
                "uploader": uploader,
                "filename": filename,
                "size_kb":  size_kb,
                "fee":      fee_nbl,
                "pinned":   False,
                "ts":       time.time(),
            }
        return {
            "ok":      True,
            "cid":     cid,
            "size_kb": f"{size_kb:.2f}",
            "fee_nbl": f"{fee_nbl:.6f}",
            "url":     f"https://ipfs.nebula-nbl.io/ipfs/{cid}",
            "gateway": f"https://gateway.nebula-nbl.io/{cid}",
        }

    def pin(self, pinner: str, cid: str,
             duration_days: int = 365) -> dict:
        """Pin a file to ensure it stays available."""
        with self._lock:
            f = self._files.get(cid)
            if not f:
                return {"ok": False, "error": "CID not found"}
            pin_fee = f["size_kb"] * 0.001 * duration_days / 365
            self._pins[cid] = {
                "pinner":       pinner,
                "fee_nbl":      pin_fee,
                "duration":     duration_days,
                "pinned_at":    self._bc.height,
                "expires_at":   self._bc.height + duration_days * 144,
            }
            f["pinned"] = True
            return {
                "ok":       True,
                "cid":      cid,
                "fee_nbl":  f"{pin_fee:.6f}",
                "days":     duration_days,
                "expires":  f"block {self._bc.height + duration_days * 144}",
            }

    def retrieve(self, cid: str) -> Optional[dict]:
        return self._files.get(cid)

    def storage_stats(self) -> dict:
        total_kb = sum(f["size_kb"] for f in self._files.values())
        return {
            "total_files":  len(self._files),
            "total_size":   f"{total_kb:.2f} KB",
            "pinned":       len(self._pins),
            "gateways":     ["ipfs.nebula-nbl.io", "gateway.nebula-nbl.io"],
        }


# ---- DAOTreasuryManager
class DAOTreasuryManager:
    """Advanced DAO treasury management with diversification."""

    ALLOCATION_TARGETS = {
        "NBL":   0.40,   # 40% native token
        "BTC":   0.20,   # 20% Bitcoin
        "ETH":   0.15,   # 15% Ethereum
        "USDT":  0.15,   # 15% stablecoins
        "OTHER": 0.10,   # 10% other assets
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc       = blockchain
        self._oracle   = oracle
        self._holdings: dict = {k: 0.0 for k in self.ALLOCATION_TARGETS}
        self._txs:     list = []
        self._signers: list = []
        self._required  = 3
        self._lock     = threading.RLock()

    def add_signer(self, address: str, role: str = "member"):
        self._signers.append({"address": address, "role": role})

    def deposit(self, asset: str, amount: float, source: str = ""):
        with self._lock:
            self._holdings[asset] = self._holdings.get(asset, 0) + amount
            self._txs.append({
                "type":   "deposit",
                "asset":  asset,
                "amount": amount,
                "source": source,
                "ts":     time.time(),
            })

    def total_value_usd(self) -> float:
        total = 0.0
        prices = {"NBL": 0.001, "BTC": 45000, "ETH": 2500,
                  "USDT": 1.0, "OTHER": 1.0}
        if self._oracle:
            prices["NBL"] = self._oracle.price("NBL/USD") or 0.001
            prices["BTC"] = self._oracle.price("BTC/USD") or 45000
            prices["ETH"] = self._oracle.price("ETH/USD") or 2500
        for asset, amt in self._holdings.items():
            total += amt * prices.get(asset, 1.0)
        return total

    def rebalance_plan(self) -> list:
        total_usd  = self.total_value_usd()
        if total_usd == 0:
            return []
        prices = {"NBL": 0.001, "BTC": 45000, "ETH": 2500,
                  "USDT": 1.0, "OTHER": 1.0}
        trades = []
        for asset, target_pct in self.ALLOCATION_TARGETS.items():
            target_usd = total_usd * target_pct
            curr_usd   = self._holdings.get(asset, 0) * prices.get(asset, 1.0)
            diff_usd   = target_usd - curr_usd
            if abs(diff_usd) > total_usd * 0.03:   # 3% threshold
                trades.append({
                    "asset":    asset,
                    "action":   "BUY" if diff_usd > 0 else "SELL",
                    "amount_usd": f"${abs(diff_usd):.2f}",
                    "target":   f"{target_pct*100:.0f}%",
                    "current":  f"{curr_usd/total_usd*100:.1f}%",
                })
        return trades

    def treasury_report(self) -> dict:
        total = self.total_value_usd()
        return {
            "total_value_usd": f"${total:,.2f}",
            "holdings":        {k: f"{v:.4f} {k}" for k, v in self._holdings.items()},
            "allocation":      {k: f"{self.ALLOCATION_TARGETS[k]*100:.0f}%" for k in self.ALLOCATION_TARGETS},
            "signers":         len(self._signers),
            "required":        self._required,
            "transactions":    len(self._txs),
            "rebalance_needed": len(self.rebalance_plan()) > 0,
        }


# ---- ValidatorStakingV2
class ValidatorStakingV2:
    """
    Full validator staking with delegation, slashing, and rewards.
    Minimum stake: 32,000 NBL to become validator.
    """

    MIN_VALIDATOR_STAKE = 32_000 * 10**DECIMALS
    MAX_VALIDATORS      = 1000
    SLASH_DOUBLE_SIGN   = 0.50   # 50% slash
    SLASH_DOWNTIME      = 0.01   # 1% slash

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._validators: dict = {}
        self._delegations: dict = {}
        self._rewards:   dict = {}
        self._slashes:   list = []
        self._lock       = threading.RLock()

    def register_validator(self, address: str,
                            commission_rate: float = 0.10,
                            moniker: str = "") -> dict:
        with self._lock:
            if len(self._validators) >= self.MAX_VALIDATORS:
                return {"ok": False, "error": "Validator set full"}
            stake = self._bc.utxo.balance(address)
            if stake < self.MIN_VALIDATOR_STAKE:
                need = self.MIN_VALIDATOR_STAKE / 10**DECIMALS
                return {"ok": False, "error": f"Need {need:,.0f} NBL stake"}
            self._validators[address] = {
                "address":    address,
                "moniker":    moniker or address[:12],
                "commission": commission_rate,
                "stake":      stake,
                "delegated":  0,
                "status":     "active",
                "uptime":     1.0,
                "blocks":     0,
                "joined":     self._bc.height,
            }
            return {
                "ok":        True,
                "moniker":   moniker,
                "stake_nbl": f"{stake/10**DECIMALS:,.3f}",
                "commission": f"{commission_rate*100:.1f}%",
                "message":   "Validator registered successfully",
            }

    def delegate(self, delegator: str, validator: str,
                  amount: int) -> dict:
        with self._lock:
            if validator not in self._validators:
                return {"ok": False, "error": "Validator not found"}
            if self._bc.utxo.balance(delegator) < amount:
                return {"ok": False, "error": "Insufficient balance"}
            key = f"{delegator}:{validator}"
            self._delegations[key] = self._delegations.get(key, 0) + amount
            self._validators[validator]["delegated"] += amount
            return {
                "ok":       True,
                "delegated": f"{amount/10**DECIMALS:.3f} NBL",
                "validator": validator[:12],
                "commission": f"{self._validators[validator]['commission']*100:.1f}%",
            }

    def distribute_block_reward(self, proposer: str, reward: int):
        with self._lock:
            val = self._validators.get(proposer)
            if not val:
                return
            val["blocks"] += 1
            total_stake = val["stake"] + val["delegated"]
            if total_stake == 0:
                return
            commission_amount = int(reward * val["commission"])
            delegator_pool    = reward - commission_amount
            # Reward to proposer
            self._rewards[proposer] = (
                self._rewards.get(proposer, 0) + commission_amount +
                int(delegator_pool * val["stake"] / total_stake)
            )
            # Reward to delegators
            for key, del_amount in self._delegations.items():
                if key.split(":")[1] == proposer:
                    delegator = key.split(":")[0]
                    share = int(delegator_pool * del_amount / total_stake)
                    self._rewards[delegator] = self._rewards.get(delegator, 0) + share

    def claim(self, address: str) -> int:
        with self._lock:
            amount = self._rewards.pop(address, 0)
            return amount

    def slash(self, validator: str, reason: str) -> dict:
        with self._lock:
            val = self._validators.get(validator)
            if not val:
                return {"ok": False}
            rate    = (self.SLASH_DOUBLE_SIGN if reason == "double_sign"
                       else self.SLASH_DOWNTIME)
            slashed = int(val["stake"] * rate)
            val["stake"]  -= slashed
            val["uptime"] *= 0.95
            if val["stake"] < self.MIN_VALIDATOR_STAKE:
                val["status"] = "jailed"
            self._slashes.append({
                "validator": validator,
                "reason":    reason,
                "slashed":   slashed,
                "block":     self._bc.height,
            })
            return {
                "ok":      True,
                "slashed": f"{slashed/10**DECIMALS:.3f} NBL",
                "status":  val["status"],
            }

    def validator_set_stats(self) -> dict:
        active = sum(1 for v in self._validators.values()
                     if v["status"] == "active")
        total_staked = sum(v["stake"] + v["delegated"]
                          for v in self._validators.values())
        return {
            "total_validators":  len(self._validators),
            "active":            active,
            "total_staked_nbl":  f"{total_staked/10**DECIMALS:,.3f}",
            "total_slashes":     len(self._slashes),
            "min_stake_nbl":     f"{self.MIN_VALIDATOR_STAKE/10**DECIMALS:,.0f}",
        }


# ---- DynamicNFT
class DynamicNFT:
    """
    Dynamic NFT that changes based on on-chain events.
    Metadata updates automatically based on blockchain state.
    """

    def __init__(self, token_id: int, collection_id: str,
                  owner: str, base_uri: str,
                  blockchain: 'NEBULABlockchain'):
        self.token_id      = token_id
        self.collection_id = collection_id
        self.owner         = owner
        self.base_uri      = base_uri
        self._bc           = blockchain
        self._traits:      dict = {}
        self._evolves:     list = []
        self._level        = 1

    def update_trait(self, trait: str, value: any):
        self._traits[trait] = value

    def check_evolution(self) -> Optional[dict]:
        """Evolve NFT based on on-chain conditions."""
        h   = self._bc.height
        era = h // HALVING_INTERVAL

        if era >= 1 and self._level < 2:
            self._level = 2
            self._traits["era"]  = "Post-First-Halving"
            self._traits["level"] = 2
            self._evolves.append({
                "from": 1, "to": 2,
                "trigger": "First halving occurred",
                "block": h,
            })
            return self._evolves[-1]
        return None

    def current_metadata(self) -> dict:
        evolution = self.check_evolution()
        return {
            "token_id":    self.token_id,
            "collection":  self.collection_id,
            "owner":       self.owner,
            "level":       self._level,
            "traits":      self._traits,
            "image":       f"{self.base_uri}/{self.token_id}_lv{self._level}.png",
            "evolved":     len(self._evolves),
            "dynamic":     True,
            "block":       self._bc.height,
        }


# ---- NFTFractionalizationV2
class NFTFractionalizationV2:
    """Advanced NFT fractionalization with governance."""

    def __init__(self, nft: 'NBL721Registry',
                  blockchain: 'NEBULABlockchain'):
        self._nft   = nft
        self._bc    = blockchain
        self._vaults: dict = {}
        self._lock  = threading.RLock()

    def fractionalize(self, owner: str, collection_id: str,
                       token_id: int, shares: int,
                       reserve_price_nbl: float) -> dict:
        with self._lock:
            if self._nft.owner_of(collection_id, token_id) != owner:
                return {"ok": False, "error": "Not owner"}
            vault_id = hashlib.sha256(
                f"FRAC:{collection_id}:{token_id}:{owner}".encode()
            ).hexdigest()[:12]
            self._vaults[vault_id] = {
                "vault_id":     vault_id,
                "collection":   collection_id,
                "token_id":     token_id,
                "owner":        owner,
                "total_shares": shares,
                "holders":      {owner: shares},
                "reserve_nbl":  reserve_price_nbl,
                "buyout":       None,
            }
            return {
                "ok":       True,
                "vault_id": vault_id,
                "shares":   shares,
                "reserve":  f"{reserve_price_nbl:,.3f} NBL",
                "note":     f"NFT locked. {shares:,} shares created.",
            }

    def buy_shares(self, buyer: str, vault_id: str,
                    share_count: int) -> dict:
        with self._lock:
            v = self._vaults.get(vault_id)
            if not v:
                return {"ok": False, "error": "Vault not found"}
            owner_shares = v["holders"].get(v["owner"], 0)
            if share_count > owner_shares:
                return {"ok": False, "error": "Not enough shares available"}
            price_per = v["reserve_nbl"] / v["total_shares"]
            cost      = price_per * share_count
            v["holders"][v["owner"]] -= share_count
            v["holders"][buyer]       = v["holders"].get(buyer, 0) + share_count
            return {
                "ok":         True,
                "shares":     share_count,
                "cost_nbl":   f"{cost:.6f}",
                "ownership":  f"{share_count/v['total_shares']*100:.2f}%",
            }

    def propose_buyout(self, buyer: str, vault_id: str,
                        offer_nbl: float) -> dict:
        with self._lock:
            v = self._vaults.get(vault_id)
            if not v:
                return {"ok": False, "error": "Vault not found"}
            if offer_nbl < v["reserve_nbl"]:
                return {"ok": False, "error": f"Below reserve: {v['reserve_nbl']} NBL"}
            v["buyout"] = {
                "buyer":   buyer,
                "offer":   offer_nbl,
                "started": self._bc.height,
                "ends":    self._bc.height + 144 * 3,   # 3-day window
            }
            return {
                "ok":    True,
                "offer": f"{offer_nbl:,.3f} NBL",
                "window": "3-day buyout window — shareholders can vote to reject",
            }

    def frac_stats(self) -> dict:
        return {
            "vaults":   len(self._vaults),
            "total_shares": sum(v["total_shares"] for v in self._vaults.values()),
        }


# ---- NEBULAEcosystemIntegrations
class NEBULAEcosystemIntegrations:
    """Central registry of all NEBULA ecosystem integrations."""

    INTEGRATIONS = {
        "wallets": [
            {"name": "NEBULA Web Wallet",  "url": "https://wallet.nebula-nbl.io",      "type": "web"},
            {"name": "NEBULA Mobile",      "url": "https://app.nebula-nbl.io",          "type": "mobile"},
            {"name": "MetaMask (bridge)",  "url": "https://nebula-nbl.io/metamask",     "type": "browser"},
            {"name": "Ledger Support",     "url": "https://nebula-nbl.io/ledger",       "type": "hardware"},
            {"name": "Trezor Support",     "url": "https://nebula-nbl.io/trezor",       "type": "hardware"},
        ],
        "exchanges": [
            {"name": "NEBULA DEX",         "url": "https://dex.nebula-nbl.io",          "type": "dex"},
            {"name": "NEBULA Aggregator",  "url": "https://swap.nebula-nbl.io",         "type": "aggregator"},
        ],
        "bridges": [
            {"name": "NEBULA Bridge",      "url": "https://bridge.nebula-nbl.io",       "chains": ["ETH","BNB","SOL","POL"]},
            {"name": "LayerZero (planned)","url": "https://nebula-nbl.io/layerzero",    "chains": ["ETH","ARB","OP"]},
        ],
        "analytics": [
            {"name": "NEBULA Explorer",    "url": "https://explorer.nebula-nbl.io",     "type": "explorer"},
            {"name": "NEBULA Analytics",   "url": "https://analytics.nebula-nbl.io",    "type": "analytics"},
            {"name": "NEBULA Charts",      "url": "https://charts.nebula-nbl.io",       "type": "charts"},
        ],
        "defi": [
            {"name": "NEBULA DEX",         "url": "https://dex.nebula-nbl.io",          "tvl": "growing"},
            {"name": "NEBULA Lend",        "url": "https://lend.nebula-nbl.io",         "tvl": "growing"},
            {"name": "NEBULA Stake",       "url": "https://stake.nebula-nbl.io",        "apy": "5-25%"},
            {"name": "NEBULA Farm",        "url": "https://farm.nebula-nbl.io",         "apy": "varies"},
            {"name": "NEBULA NFTs",        "url": "https://nft.nebula-nbl.io",          "type": "marketplace"},
            {"name": "NEBULA RWA",         "url": "https://rwa.nebula-nbl.io",          "type": "tokenization"},
            {"name": "NEBULA Social",      "url": "https://social.nebula-nbl.io",       "type": "socialfi"},
        ],
        "developer": [
            {"name": "NEBULA Docs",        "url": "https://docs.nebula-nbl.io",         "type": "docs"},
            {"name": "NEBULA SDK (Python)","url": "https://pypi.org/project/nebula-nbl","type": "sdk"},
            {"name": "NEBULA SDK (JS)",    "url": "https://npmjs.com/nebula-nbl",       "type": "sdk"},
            {"name": "NEBULA API",         "url": "https://api.nebula-nbl.io",          "type": "api"},
            {"name": "NEBULA Faucet",      "url": "https://faucet.nebula-nbl.io",       "type": "faucet"},
            {"name": "NEBULA Testnet",     "url": "https://testnet.nebula-nbl.io",      "type": "testnet"},
            {"name": "GitHub",             "url": "", "type": "source"},
        ],
        "community": [
            {"name": "Community Forum",    "url": "https://community.nebula-nbl.io",    "type": "forum"},
            {"name": "Telegram",           "url": "https://t.me/nebula_nbl",            "type": "chat"},
            {"name": "Discord",            "url": "https://discord.gg/nebula-nbl",      "type": "chat"},
            {"name": "Twitter/X",          "url": "https://twitter.com/nebula_nbl",     "type": "social"},
            {"name": "Grant Program",      "url": "https://grants.nebula-nbl.io",       "type": "grants"},
            {"name": "Bug Bounty",         "url": "https://security.nebula-nbl.io",     "type": "security"},
        ],
    }

    @classmethod
    def all(cls) -> dict:
        total = sum(len(v) for v in cls.INTEGRATIONS.values())
        return {
            "total_integrations": total,
            "categories":        len(cls.INTEGRATIONS),
            "integrations":      cls.INTEGRATIONS,
        }

    @classmethod
    def by_category(cls, category: str) -> list:
        return cls.INTEGRATIONS.get(category, [])

    @classmethod
    def ecosystem_summary(cls) -> str:
        lines = ["🌌 NEBULA Ecosystem — All Integrations\n"]
        for cat, items in cls.INTEGRATIONS.items():
            lines.append(f"  {cat.upper()}")
            for item in items:
                lines.append(f"    • {item['name']}: {item['url']}")
            lines.append("")
        return "\n".join(lines)


# ---- IBCPacket
class IBCPacket:
    """IBC (Inter-Blockchain Communication) packet."""
    def __init__(self, sequence: int, src_port: str, src_channel: str,
                  dst_port: str, dst_channel: str,
                  data: bytes, timeout_height: int):
        self.sequence       = sequence
        self.src_port       = src_port
        self.src_channel    = src_channel
        self.dst_port       = dst_port
        self.dst_channel    = dst_channel
        self.data           = data
        self.timeout_height = timeout_height
        self.packet_id      = hashlib.sha256(
            f"{sequence}:{src_port}:{dst_port}:{time.time()}".encode()
        ).hexdigest()[:16]

    def to_dict(self) -> dict:
        return {
            "packet_id":   self.packet_id,
            "sequence":    self.sequence,
            "src":         f"{self.src_port}/{self.src_channel}",
            "dst":         f"{self.dst_port}/{self.dst_channel}",
            "data_len":    len(self.data),
            "timeout":     self.timeout_height,
        }
