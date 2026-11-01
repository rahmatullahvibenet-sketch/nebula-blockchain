"""NEBULA group40 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. ContractFactory  (orig. lines 66415-66481)
   2. EventLog  (orig. lines 66488-66571)
   3. NFTBridgeStatus  (orig. lines 66585-66591)
   4. CrossChainNFTTransfer  (orig. lines 66593-66616)
   5. CrossChainNFTBridge  (orig. lines 66618-66733)
   6. AdvancedStakingPlatform  (orig. lines 66740-66829)
   7. PortfolioEntry  (orig. lines 66836-66864)
   8. PortfolioTracker  (orig. lines 66866-66944)
   9. NodeRESTAPI  (orig. lines 66951-67197)
  10. ContractState  (orig. lines 67204-67228)
  11. SmartContractV2  (orig. lines 67231-67268)
  12. ERC20Contract  (orig. lines 67271-67362)
  13. DeFiDashboard  (orig. lines 67374-67451)
  14. NodeConfig  (orig. lines 67458-67501)
  15. NodeManager  (orig. lines 67503-67551)
  16. BridgeRequestV2  (orig. lines 67558-67584)
  17. UniversalTokenBridge  (orig. lines 67586-67672)
  18. MarginPosition  (orig. lines 67679-67730)
  19. MarginTradingEngine  (orig. lines 67732-67815)
  20. OptionType  (orig. lines 67822-67824)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BlockTemplateEngine, BridgeDirection, BridgeRequest, ContractEvent, ContractTemplate, DeployedContract, LockStakingPool, NEBULABlockchain, StakingPool, Transaction
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

FOUNDATION_RATE        = 0.02          # 2% per block to foundation

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

DIFFICULTY_WINDOW      = 2016                           # blocks per retarget

MAX_TARGET             = 0x0fffff * (256 ** ((0x1e if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d) - 3))   # [v10.24]   # bits_to_target(INITIAL_BITS) — max allowed PoW target

DEFAULT_PORT           = 8333

PROTOCOL_VERSION       = 70015

MAX_PEERS              = 125

MAGIC_BYTES            = 0x4E424C4D   # "NBLM" — NEBULA Mainnet magic integer

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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- ContractFactory
class ContractFactory:
    """
    Smart contract factory for NEBULA.
    Deploy standardized contract templates with custom parameters.
    """

    DEPLOY_FEE = 10 * 10**DECIMALS    # 10 NBL to deploy

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._contracts: Dict[str, DeployedContract] = {}
        self._lock      = threading.RLock()

    def deploy(self, deployer: str, template: ContractTemplate,
                params: dict) -> Tuple[bool, str]:
        with self._lock:
            if self._bc.utxo.balance(deployer) < self.DEPLOY_FEE:
                return False, "Insufficient balance for deployment fee"
            bytecode = self._generate_bytecode(template, params)
            bc_hash  = hashlib.sha256(bytecode.encode()).hexdigest()
            cid = hashlib.sha256(
                f"FACTORY:{deployer}:{template.value}:{bc_hash}:{time.time()}".encode()
            ).hexdigest()[:20]
            self._contracts[cid] = DeployedContract(
                contract_id   = cid,
                template      = template,
                deployer      = deployer,
                params        = params,
                deployed_at   = time.time(),
                block_height  = self._bc.height,
                bytecode_hash = bc_hash,
            )
            return True, cid

    def _generate_bytecode(self, template: ContractTemplate,
                             params: dict) -> str:
        """Generate (simulated) bytecode for a contract template."""
        return json.dumps({"template": template.value, "params": params})

    def verify_source(self, contract_id: str,
                       source_code: str) -> Tuple[bool, str]:
        """Verify contract source matches deployed bytecode."""
        with self._lock:
            contract = self._contracts.get(contract_id)
            if not contract:
                return False, "Contract not found"
            src_hash = hashlib.sha256(source_code.encode()).hexdigest()
            if src_hash == contract.bytecode_hash:
                contract.verified = True
                return True, "Source verified"
            return False, "Source hash mismatch"

    def contracts_by(self, deployer: str) -> List[dict]:
        return [c.to_dict() for c in self._contracts.values()
                if c.deployer == deployer]

    def factory_stats(self) -> dict:
        with self._lock:
            by_template = {}
            for c in self._contracts.values():
                t = c.template.value
                by_template[t] = by_template.get(t, 0) + 1
        return {
            "total_contracts": len(self._contracts),
            "by_template":     by_template,
            "deploy_fee_nbl":  f"{self.DEPLOY_FEE/10**DECIMALS:.0f}",
        }


# ---- EventLog
@dataclass
class EventLog:
    """
    On-chain event log system for NEBULA smart contracts.
    Allows contracts to emit searchable events.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._logs:  List[ContractEvent]          = []
        self._index: Dict[str, List[int]]          = {}  # topic -> [log indices]
        self._lock   = threading.RLock()

    def emit(self, contract_id: str, event_name: str,
              topics: List[str], data: dict,
              tx_index: int = 0) -> str:
        with self._lock:
            log_index = len(self._logs)
            eid = hashlib.sha256(
                f"EVT:{contract_id}:{event_name}:{log_index}:{time.time()}".encode()
            ).hexdigest()[:16]
            event = ContractEventC(
                event_id     = eid,
                contract_id  = contract_id,
                event_name   = event_name,
                topics       = topics,
                data         = data,
                block_height = self._bc.height,
                tx_index     = tx_index,
                log_index    = log_index,
                timestamp    = time.time(),
            )
            self._logs.append(event)
            # Index by topic
            for topic in topics:
                if topic not in self._index:
                    self._index[topic] = []
                self._index[topic].append(log_index)
            # Index by event name
            ename_key = f"event:{event_name}"
            if ename_key not in self._index:
                self._index[ename_key] = []
            self._index[ename_key].append(log_index)
            # Index by contract
            ckey = f"contract:{contract_id}"
            if ckey not in self._index:
                self._index[ckey] = []
            self._index[ckey].append(log_index)
            return eid

    def get_logs(self, contract_id: str = None,
                  event_name: str = None,
                  topic: str = None,
                  from_block: int = 0,
                  to_block: int = None,
                  limit: int = 100) -> List[dict]:
        to_b = to_block or self._bc.height
        with self._lock:
            if contract_id:
                indices = self._index.get(f"contract:{contract_id}", [])
            elif event_name:
                indices = self._index.get(f"event:{event_name}", [])
            elif topic:
                indices = self._index.get(topic, [])
            else:
                indices = list(range(len(self._logs)))
            results = []
            for i in indices[-limit:]:
                if 0 <= i < len(self._logs):
                    evt = self._logs[i]
                    if from_block <= evt.block_height <= to_b:
                        results.append(evt.to_dict())
        return results

    def event_log_stats(self) -> dict:
        with self._lock:
            unique_contracts = len(set(e.contract_id for e in self._logs))
            unique_events    = len(set(e.event_name for e in self._logs))
        return {
            "total_events":      len(self._logs),
            "unique_contracts":  unique_contracts,
            "unique_event_types": unique_events,
            "indexed_topics":    len(self._index),
        }


# ---- NFTBridgeStatus
class NFTBridgeStatus(_enum.Enum):
    INITIATED  = "initiated"
    LOCKED     = "locked"
    MINTED     = "minted"
    BURNED     = "burned"
    RELEASED   = "released"
    FAILED     = "failed"


# ---- CrossChainNFTTransfer
@dataclass
class CrossChainNFTTransfer:
    transfer_id:   str
    collection_id: str
    token_id:      int
    owner:         str
    source_chain:  str
    dest_chain:    str
    dest_address:  str
    status:        NFTBridgeStatus
    metadata_cid:  str
    created_at:    float
    completed_at:  Optional[float] = None

    def to_dict(self) -> dict:
        return {
            "transfer_id":   self.transfer_id,
            "collection":    self.collection_id,
            "token_id":      self.token_id,
            "owner":         self.owner,
            "from":          self.source_chain,
            "to":            self.dest_chain,
            "status":        self.status.value,
        }


# ---- CrossChainNFTBridge
class CrossChainNFTBridge:
    """
    Bridge NFTs between NEBULA and other chains.
    Lock-and-mint: lock on source, mint wrapped on destination.
    """

    SUPPORTED_CHAINS = ["nebula", "ethereum", "polygon", "solana", "bnb_chain"]

    def __init__(self, blockchain: 'NEBULABlockchain',
                  nft_registry: 'NBL721Registry' = None):
        self._bc         = blockchain
        self._nft        = nft_registry
        self._transfers: Dict[str, CrossChainNFTTransfer] = {}
        self._locked_nfts: Dict[str, Set[int]] = {}   # collection_id -> {token_ids}
        self._wrapped:     Dict[str, dict]     = {}   # chain -> {wrapped collections}
        self._lock        = threading.RLock()

    def bridge_out(self, collection_id: str, token_id: int,
                    owner: str, dest_chain: str,
                    dest_address: str) -> Tuple[bool, str]:
        """Lock NFT on NEBULA and initiate bridge to destination chain."""
        with self._lock:
            if dest_chain not in self.SUPPORTED_CHAINS:
                return False, f"Unsupported chain: {dest_chain}"
            if self._nft:
                current = self._nft.owner_of(collection_id, token_id)
                if current != owner:
                    return False, "Not the NFT owner"
            tid = hashlib.sha256(
                f"NFTBRIDGE:{collection_id}:{token_id}:{owner}:{time.time()}".encode()
            ).hexdigest()[:16]
            if collection_id not in self._locked_nfts:
                self._locked_nfts[collection_id] = set()
            self._locked_nfts[collection_id].add(token_id)
            metadata_cid = f"Qm{hashlib.sha256(f'{collection_id}:{token_id}'.encode()).hexdigest()[:44]}"
            self._transfers[tid] = CrossChainNFTTransfer(
                transfer_id   = tid,
                collection_id = collection_id,
                token_id      = token_id,
                owner         = owner,
                source_chain  = "nebula",
                dest_chain    = dest_chain,
                dest_address  = dest_address,
                status        = NFTBridgeStatus.LOCKED,
                metadata_cid  = metadata_cid,
                created_at    = time.time(),
            )
            return True, tid

    def bridge_in(self, collection_id: str, token_id: int,
                   owner: str, source_chain: str,
                   proof: str = "") -> Tuple[bool, str]:
        """Receive NFT from another chain and mint on NEBULA."""
        with self._lock:
            if collection_id in self._locked_nfts and \
               token_id in self._locked_nfts[collection_id]:
                # Release locked NFT
                self._locked_nfts[collection_id].discard(token_id)
                tid = hashlib.sha256(
                    f"NFTBRIDGE_IN:{collection_id}:{token_id}:{owner}:{time.time()}".encode()
                ).hexdigest()[:16]
                self._transfers[tid] = CrossChainNFTTransfer(
                    transfer_id   = tid,
                    collection_id = collection_id,
                    token_id      = token_id,
                    owner         = owner,
                    source_chain  = source_chain,
                    dest_chain    = "nebula",
                    dest_address  = owner,
                    status        = NFTBridgeStatus.RELEASED,
                    metadata_cid  = "",
                    created_at    = time.time(),
                    completed_at  = time.time(),
                )
                return True, tid
            else:
                # Mint wrapped NFT
                tid = hashlib.sha256(
                    f"WRAPPED_NFT:{source_chain}:{collection_id}:{token_id}:{time.time()}".encode()
                ).hexdigest()[:16]
                self._transfers[tid] = CrossChainNFTTransfer(
                    transfer_id   = tid,
                    collection_id = f"w{collection_id[:8]}_{source_chain}",
                    token_id      = token_id,
                    owner         = owner,
                    source_chain  = source_chain,
                    dest_chain    = "nebula",
                    dest_address  = owner,
                    status        = NFTBridgeStatus.MINTED,
                    metadata_cid  = "",
                    created_at    = time.time(),
                    completed_at  = time.time(),
                )
                return True, tid

    def is_locked(self, collection_id: str, token_id: int) -> bool:
        return token_id in self._locked_nfts.get(collection_id, set())

    def transfer_history(self, owner: str = None) -> List[dict]:
        transfers = list(self._transfers.values())
        if owner:
            transfers = [t for t in transfers if t.owner == owner]
        return [t.to_dict() for t in transfers]

    def bridge_stats(self) -> dict:
        with self._lock:
            total_locked = sum(len(s) for s in self._locked_nfts.values())
            by_status    = {}
            for t in self._transfers.values():
                k = t.status.value
                by_status[k] = by_status.get(k, 0) + 1
        return {
            "total_transfers": len(self._transfers),
            "locked_nfts":     total_locked,
            "by_status":       by_status,
        }


# ---- AdvancedStakingPlatform
class AdvancedStakingPlatform:
    """
    Multi-pool staking platform for NEBULA.
    Different pools offer different lock periods and APY rates.
    Auto-compound feature available.
    """

    POOL_CONFIGS = [
        ("flexible",  "Flexible",     0,   0.05,   100),
        ("30day",     "30-Day Lock",  30,  0.08,   500),
        ("90day",     "90-Day Lock",  90,  0.12,  1000),
        ("180day",    "180-Day Lock", 180, 0.18,  5000),
        ("365day",    "1-Year Lock",  365, 0.25, 10000),
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._pools: Dict[str, StakingPool] = {}
        self._auto_compound: Set[str]       = set()
        self._last_reward_block: int        = 0
        self._lock   = threading.RLock()
        for pid, name, days, apy, min_s in self.POOL_CONFIGS:
            self._pools[pid] = LockStakingPool(pid, name, days, apy, min_s)

    def stake(self, address: str, pool_id: str,
               amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, f"Pool not found: {pool_id}"
            amount = int(amount_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(address) < amount:
                return False, "Insufficient balance"
            return pool.stake(address, amount, self._bc.height)

    def unstake(self, address: str, pool_id: str) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, "Pool not found"
            ok, result = pool.unstake(address, self._bc.height)
            if not ok:
                if result < 0:
                    return False, f"Locked: {-result} blocks remaining"
                return False, "No stake found"
            return True, f"Unstaked {result/10**DECIMALS:.3f} NBL"

    def enable_auto_compound(self, address: str):
        self._auto_compound.add(address)

    def process_rewards(self) -> dict:
        """Process staking rewards for all pools."""
        cur   = self._bc.height
        last  = self._last_reward_block
        if cur <= last:
            return {"rewards_distributed": 0}
        total = 0
        with self._lock:
            for pool in self._pools.values():
                total += pool.accrue_rewards(cur, last)
            self._last_reward_block = cur
        return {"rewards_distributed": f"{total/10**DECIMALS:.6f} NBL"}

    def user_positions(self, address: str) -> List[dict]:
        positions = []
        for pool in self._pools.values():
            info = pool.stakers.get(address)
            if info:
                positions.append({
                    "pool_id":     pool.pool_id,
                    "pool_name":   pool.name,
                    "amount":      f"{info['amount']/10**DECIMALS:.3f} NBL",
                    "rewards":     f"{info['rewards']/10**DECIMALS:.6f} NBL",
                    "unlock_block": info["unlock_block"],
                    "apy":         f"{pool.apy*100:.1f}%",
                    "auto_compound": address in self._auto_compound,
                })
        return positions

    def staking_platform_stats(self) -> dict:
        with self._lock:
            total_staked = sum(p.total_staked for p in self._pools.values())
            total_stakers = sum(len(p.stakers) for p in self._pools.values())
            pools = [p.pool_info() for p in self._pools.values()]
        return {
            "total_staked_nbl": f"{total_staked/10**DECIMALS:.3f}",
            "unique_stakers":   total_stakers,
            "pools":            pools,
            "auto_compound":    len(self._auto_compound),
        }


# ---- PortfolioEntry
class PortfolioEntry:
    """A single asset in a portfolio."""

    def __init__(self, asset: str, amount: float, avg_cost: float):
        self.asset     = asset
        self.amount    = amount
        self.avg_cost  = avg_cost   # cost basis
        self.txs:      List[dict] = []

    def add_position(self, amount: float, price: float):
        total_cost  = self.avg_cost * self.amount + price * amount
        self.amount += amount
        self.avg_cost = total_cost / self.amount if self.amount > 0 else 0

    def unrealized_pnl(self, current_price: float) -> float:
        return (current_price - self.avg_cost) * self.amount

    def to_dict(self, current_price: float = 0) -> dict:
        pnl  = self.unrealized_pnl(current_price) if current_price else 0
        pct  = pnl / (self.avg_cost * self.amount) * 100 if self.avg_cost > 0 else 0
        return {
            "asset":       self.asset,
            "amount":      f"{self.amount:.4f}",
            "avg_cost":    f"${self.avg_cost:.4f}",
            "current":     f"${current_price:.4f}",
            "value":       f"${self.amount * current_price:.2f}",
            "pnl":         f"${pnl:.2f}",
            "pnl_pct":     f"{pct:+.2f}%",
        }


# ---- PortfolioTracker
class PortfolioTracker:
    """
    On-chain portfolio tracker for NEBULA wallets.
    Tracks positions, P&L, performance metrics.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc          = blockchain
        self._oracle      = oracle
        self._portfolios: Dict[str, Dict[str, PortfolioEntry]] = {}
        self._lock        = threading.RLock()

    def create_portfolio(self, owner: str) -> bool:
        with self._lock:
            if owner not in self._portfolios:
                self._portfolios[owner] = {}
            return True

    def record_buy(self, owner: str, asset: str,
                    amount: float, price: float) -> bool:
        with self._lock:
            if owner not in self._portfolios:
                self._portfolios[owner] = {}
            p = self._portfolios[owner]
            if asset in p:
                p[asset].add_position(amount, price)
            else:
                p[asset] = PortfolioEntry(asset, amount, price)
            p[asset].txs.append({
                "type": "buy", "amount": amount,
                "price": price, "ts": time.time()
            })
            return True

    def record_sell(self, owner: str, asset: str,
                     amount: float, price: float) -> Tuple[bool, float]:
        with self._lock:
            p     = self._portfolios.get(owner, {})
            entry = p.get(asset)
            if not entry or entry.amount < amount:
                return False, 0.0
            realized_pnl = (price - entry.avg_cost) * amount
            entry.amount -= amount
            if entry.amount <= 0:
                del p[asset]
            else:
                entry.txs.append({
                    "type": "sell", "amount": amount,
                    "price": price, "ts": time.time()
                })
            return True, realized_pnl

    def portfolio_value(self, owner: str) -> dict:
        with self._lock:
            p = self._portfolios.get(owner, {})
        if not p:
            return {"total_usd": "0.00", "assets": []}
        assets = []
        total  = 0.0
        nbl_price = (self._oracle.price("NBL/USD")
                     if self._oracle else 0.01)
        for asset, entry in p.items():
            price = nbl_price if asset == "NBL" else 1.0
            d = entry.to_dict(price)
            assets.append(d)
            total += entry.amount * price
        return {
            "owner":     owner,
            "total_usd": f"${total:.2f}",
            "assets":    assets,
            "n_assets":  len(assets),
        }

    def global_stats(self) -> dict:
        return {
            "tracked_portfolios": len(self._portfolios),
            "total_assets":       sum(len(p) for p in self._portfolios.values()),
        }


# ---- NodeRESTAPI
class NodeRESTAPI:
    """
    Complete REST API for NEBULA node.
    Handles all HTTP endpoints for external clients.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._routes: Dict[str, Callable] = {}
        self._register_routes()
        self._request_count  = 0
        self._error_count    = 0

    def _register_routes(self):
        r = self._routes
        # Chain info
        r["GET /"] = self._root
        r["GET /info"] = self._info
        r["GET /status"] = self._status
        r["GET /health"] = self._health
        # Blocks
        r["GET /blocks"] = self._latest_blocks
        r["GET /block/{id}"] = self._get_block
        # Transactions
        r["GET /tx/{txid}"] = self._get_tx
        r["POST /tx"] = self._submit_tx
        r["GET /mempool"] = self._mempool
        # Addresses
        r["GET /address/{addr}"] = self._get_address
        r["GET /address/{addr}/utxos"] = self._get_utxos
        r["GET /address/{addr}/txs"] = self._get_addr_txs
        # Mining
        r["GET /mining/template"] = self._block_template
        r["GET /mining/difficulty"] = self._difficulty
        r["GET /mining/reward"] = self._current_reward
        # Network
        r["GET /peers"] = self._peers
        r["GET /network"] = self._network_info
        # Utilities
        r["GET /decode/{hex}"] = self._decode_tx
        r["GET /validate/{addr}"] = self._validate_address
        r["GET /supply"] = self._supply_info

    def handle(self, method: str, path: str,
                body: dict = None) -> dict:
        """Route a request."""
        self._request_count += 1
        key     = f"{method} {path}"
        # Try exact match first
        handler = self._routes.get(key)
        if not handler:
            # Try pattern match
            handler = self._pattern_match(method, path)
        if handler:
            try:
                return {"ok": True, "result": handler(path, body or {})}
            except Exception as e:
                self._error_count += 1
                return {"ok": False, "error": str(e)}
        self._error_count += 1
        return {"ok": False, "error": f"404 Not Found: {path}"}

    def _pattern_match(self, method: str, path: str) -> Optional[Callable]:
        for route, handler in self._routes.items():
            rm, rp = route.split(" ", 1)
            if rm != method:
                continue
            parts   = rp.split("/")
            inparts = path.split("/")
            if len(parts) != len(inparts):
                continue
            if all(p == i or p.startswith("{") for p, i in zip(parts, inparts)):
                return handler
        return None

    def _root(self, path, body) -> dict:
        return {"name": "NEBULA Node", "version": CHAIN_VERSION,
                "chain_id": CHAIN_ID}

    def _info(self, path, body) -> dict:
        return nebula_ecosystem_info()

    def _status(self, path, body) -> dict:
        bc = self._bc
        return {
            "height":     bc.height,
            "best_block": bc.tip.hash,
            "mempool":    bc.mempool.size(),
            "utxo_set":   bc.utxo.size(),
        }

    def _health(self, path, body) -> dict:
        return {"status": "ok", "timestamp": time.time()}

    def _latest_blocks(self, path, body) -> list:
        bc = self._bc
        result = []
        for h in range(max(0, bc.height - 9), bc.height + 1):
            blk = bc.get_block(h)
            if blk:
                result.append({
                    "height":    blk.height,
                    "hash":      blk.hash,
                    "tx_count":  blk.tx_count,
                    "timestamp": blk.header.timestamp,
                    "size":      blk.byte_size(),
                })
        return list(reversed(result))

    def _get_block(self, path, body) -> Optional[dict]:
        parts = path.strip("/").split("/")
        bid   = parts[-1] if parts else "0"
        try:
            h   = int(bid)
            blk = self._bc.get_block(h)
        except ValueError:
            blk = self._bc.get_block_by_hash(bid)
        if not blk:
            return None
        return {
            "height":    blk.height,
            "hash":      blk.hash,
            "prev_hash": blk.header.prev_hash,
            "timestamp": blk.header.timestamp,
            "tx_count":  blk.tx_count,
            "merkle_root": blk.header.merkle_root,
            "bits":      blk.header.bits,
            "nonce":     blk.header.nonce,
            "size":      blk.byte_size(),
            "reward":    f"{mining_reward(blk.height)/10**DECIMALS:.9f}",
        }

    def _get_tx(self, path, body) -> Optional[dict]:
        parts = path.strip("/").split("/")
        txid  = parts[-1] if parts else ""
        tx    = self._bc.mempool._txs.get(txid)
        if tx:
            return {**tx.to_dict(), "confirmations": 0}
        return None

    def _submit_tx(self, path, body) -> dict:
        tx_hex = body.get("tx_hex", "")
        if not tx_hex:
            return {"error": "tx_hex required"}
        try:
            raw = bytes.fromhex(tx_hex)
            tx  = Transaction.deserialize(raw)
            ok, msg = self._bc.mempool.submit(tx)
            return {"accepted": ok, "txid": tx.txid, "msg": msg}
        except Exception as e:
            return {"error": str(e)}

    def _mempool(self, path, body) -> dict:
        mp = self._bc.mempool
        txs = list(mp._txs.keys())[:50]
        return {
            "size":    mp.size(),
            "txids":   txs,
            "total_fees": f"{mp.total_fees()/10**DECIMALS:.6f} NBL",
        }

    def _get_address(self, path, body) -> dict:
        parts = path.strip("/").split("/")
        addr  = parts[-1] if parts else ""
        bal   = self._bc.utxo.balance(addr)
        return {
            "address": addr,
            "balance": f"{bal/10**DECIMALS:.9f} NBL",
            "balance_raw": bal,
        }

    def _get_utxos(self, path, body) -> list:
        parts = path.strip("/").split("/")
        addr  = parts[-2] if len(parts) >= 2 else ""
        return self._bc.utxo.get_by_address(addr)  # FIX

    def _get_addr_txs(self, path, body) -> list:
        return []

    def _block_template(self, path, body) -> dict:
        addr = body.get("miner", FOUNDATION_ADDRESS)
        tmpl = BlockTemplateEngine(self._bc, addr)
        return tmpl.build_template()

    def _difficulty(self, path, body) -> dict:
        bc = self._bc
        return {
            "bits":         bc.tip.header.bits,
            "difficulty":   f"{MAX_TARGET / bits_to_target(bc.tip.header.bits):.2f}",
            "target":       hex(bits_to_target(bc.tip.header.bits)),
            "next_adjust":  DIFFICULTY_WINDOW - (bc.height % DIFFICULTY_WINDOW),
        }

    def _current_reward(self, path, body) -> dict:
        h = self._bc.height
        r = mining_reward(h)
        return {
            "height":       h,
            "reward_nbl":   f"{r/10**DECIMALS:.9f}",
            "foundation":   f"{int(r*FOUNDATION_RATE)/10**DECIMALS:.9f}",
            "next_halving": (h // HALVING_INTERVAL + 1) * HALVING_INTERVAL,
        }

    def _peers(self, path, body) -> list:
        return []

    def _network_info(self, path, body) -> dict:
        return {
            "chain_id":        CHAIN_ID,
            "protocol":        PROTOCOL_VERSION,
            "default_port":    DEFAULT_PORT,
            "magic_bytes":     hex(MAGIC_BYTES),
        }

    def _decode_tx(self, path, body) -> dict:
        parts = path.strip("/").split("/")
        hex_s = parts[-1] if parts else ""
        try:
            raw = bytes.fromhex(hex_s)
            tx  = Transaction.deserialize(raw)
            return tx.to_dict()
        except Exception as e:
            return {"error": str(e)}

    def _validate_address(self, path, body) -> dict:
        parts = path.strip("/").split("/")
        addr  = parts[-1] if parts else ""
        valid = len(addr) >= 25 and addr[0] in ('N', '1', '3')
        return {"address": addr, "valid": valid}

    def _supply_info(self, path, body) -> dict:
        bc = self._bc
        supply = bc.utxo.total_supply()
        return {
            "total_supply_nbl":   f"{supply/10**DECIMALS:.3f}",
            "max_supply_nbl":     f"{MAX_SUPPLY/10**DECIMALS:.0f}",
            "circulating_pct":    f"{supply/MAX_SUPPLY*100:.4f}%",
            "foundation_reserve": f"{bc.utxo.balance(FOUNDATION_ADDRESS)/10**DECIMALS:.3f}",
        }

    def api_stats(self) -> dict:
        return {
            "total_requests": self._request_count,
            "errors":         self._error_count,
            "routes":         len(self._routes),
            "error_rate":     f"{self._error_count/max(1,self._request_count)*100:.1f}%",
        }


# ---- ContractState
class ContractState:
    """Persisted state for a smart contract."""

    def __init__(self):
        self._storage: Dict[str, Any] = {}
        self._events:  List[dict]     = []

    def get(self, key: str, default: Any = None) -> Any:
        return self._storage.get(key, default)

    def set(self, key: str, value: Any):
        self._storage[key] = value

    def delete(self, key: str):
        self._storage.pop(key, None)

    def emit_event(self, name: str, data: dict):
        self._events.append({
            "event":     name,
            "data":      data,
            "timestamp": time.time(),
        })

    def snapshot(self) -> dict:
        return dict(self._storage)


# ---- SmartContractV2
class SmartContractV2:
    """
    Smart contract v2 with persistent state and events.
    Contracts are Python classes that inherit this base.
    """

    def __init__(self, contract_id: str, owner: str,
                  blockchain: 'NEBULABlockchain'):
        self.contract_id = contract_id
        self.owner       = owner
        self.blockchain  = blockchain
        self.state       = ContractState()
        self.deployed_at = blockchain.height
        self._abi:       Dict[str, Callable] = {}

    def register_function(self, name: str, fn: Callable):
        self._abi[name] = fn

    def call(self, caller: str, fn_name: str,
              args: dict = None, value: int = 0) -> Tuple[Any, List[dict]]:
        """Call a contract function."""
        fn = self._abi.get(fn_name)
        if not fn:
            raise ValueError(f"Function not found: {fn_name}")
        prev_events = len(self.state._events)
        result = fn(caller, args or {}, value)
        new_events = self.state._events[prev_events:]
        return result, new_events

    def contract_info(self) -> dict:
        return {
            "contract_id": self.contract_id,
            "owner":       self.owner,
            "deployed_at": self.deployed_at,
            "functions":   list(self._abi.keys()),
            "storage_keys": list(self.state._storage.keys()),
            "events":      len(self.state._events),
        }


# ---- ERC20Contract
class ERC20Contract(SmartContractV2):
    """
    Example NBL-20 contract implemented using SmartContractV2.
    Fully featured fungible token contract.
    """

    def __init__(self, contract_id: str, owner: str,
                  blockchain: 'NEBULABlockchain',
                  name: str, symbol: str,
                  decimals: int, total_supply: float):
        super().__init__(contract_id, owner, blockchain)
        # Initialize state
        self.state.set("name", name)
        self.state.set("symbol", symbol)
        self.state.set("decimals", decimals)
        supply = int(total_supply * 10**decimals)
        self.state.set("total_supply", supply)
        self.state.set(f"balance:{owner}", supply)
        # Register functions
        self.register_function("transfer",     self._transfer)
        self.register_function("approve",      self._approve)
        self.register_function("transferFrom", self._transfer_from)
        self.register_function("mint",         self._mint)
        self.register_function("burn",         self._burn)
        self.register_function("balanceOf",    self._balance_of)
        self.register_function("totalSupply",  self._total_supply)

    def _balance_of(self, caller: str, args: dict, value: int) -> int:
        return self.state.get(f"balance:{args.get('account', caller)}", 0)

    def _total_supply(self, caller: str, args: dict, value: int) -> int:
        return self.state.get("total_supply", 0)

    def _transfer(self, caller: str, args: dict, value: int) -> bool:
        to     = args.get("to", "")
        amount = args.get("amount", 0)
        bal    = self.state.get(f"balance:{caller}", 0)
        if bal < amount:
            raise ValueError("Insufficient balance")
        self.state.set(f"balance:{caller}", bal - amount)
        self.state.set(f"balance:{to}",
                        self.state.get(f"balance:{to}", 0) + amount)
        self.state.emit_event("Transfer",
                              {"from": caller, "to": to, "amount": amount})
        return True

    def _approve(self, caller: str, args: dict, value: int) -> bool:
        spender = args.get("spender", "")
        amount  = args.get("amount", 0)
        self.state.set(f"allowance:{caller}:{spender}", amount)
        self.state.emit_event("Approval",
                              {"owner": caller, "spender": spender, "amount": amount})
        return True

    def _transfer_from(self, caller: str, args: dict, value: int) -> bool:
        owner   = args.get("owner", "")
        to      = args.get("to", "")
        amount  = args.get("amount", 0)
        allowed = self.state.get(f"allowance:{owner}:{caller}", 0)
        if allowed < amount:
            raise ValueError("Insufficient allowance")
        self.state.set(f"allowance:{owner}:{caller}", allowed - amount)
        bal = self.state.get(f"balance:{owner}", 0)
        if bal < amount:
            raise ValueError("Insufficient balance")
        self.state.set(f"balance:{owner}", bal - amount)
        self.state.set(f"balance:{to}",
                        self.state.get(f"balance:{to}", 0) + amount)
        return True

    def _mint(self, caller: str, args: dict, value: int) -> bool:
        if caller != self.owner:
            raise ValueError("Only owner")
        to     = args.get("to", caller)
        amount = args.get("amount", 0)
        self.state.set(f"balance:{to}",
                        self.state.get(f"balance:{to}", 0) + amount)
        self.state.set("total_supply",
                        self.state.get("total_supply", 0) + amount)
        self.state.emit_event("Mint", {"to": to, "amount": amount})
        return True

    def _burn(self, caller: str, args: dict, value: int) -> bool:
        amount = args.get("amount", 0)
        bal    = self.state.get(f"balance:{caller}", 0)
        if bal < amount:
            raise ValueError("Insufficient balance to burn")
        self.state.set(f"balance:{caller}", bal - amount)
        self.state.set("total_supply",
                        self.state.get("total_supply", 0) - amount)
        self.state.emit_event("Burn", {"from": caller, "amount": amount})
        return True


# ---- DeFiDashboard
class DeFiDashboard:
    """
    Aggregated DeFi dashboard for NEBULA ecosystem.
    Real-time TVL, yields, positions, alerts.
    """

    def __init__(self, full_node: 'NEBULAFullNodeV2' = None,
                  blockchain: 'NEBULABlockchain'     = None):
        self._node = full_node
        self._bc   = blockchain or (full_node.blockchain if full_node else NEBULABlockchain())

    def user_dashboard(self, address: str) -> dict:
        """Complete user dashboard for a single address."""
        bc  = self._bc
        bal = bc.utxo.balance(address)
        dashboard = {
            "address":      address,
            "nbl_balance":  f"{bal/10**DECIMALS:.9f}",
            "usd_value":    "N/A",
            "defi":         {},
        }
        if self._node:
            # Staking positions
            stk   = self._node.staking.get_stake(address)
            dashboard["defi"]["staking"] = stk
            # NFT holdings
            nfts  = self._node.nft.tokens_of(address)
            dashboard["defi"]["nfts"] = {"count": len(nfts)}
            # Governance votes
            gov   = self._node.governance.votes_by(address)
            dashboard["defi"]["governance"] = {"votes": len(gov)}
        return dashboard

    def ecosystem_snapshot(self) -> dict:
        """Snapshot of the entire NEBULA DeFi ecosystem."""
        bc = self._bc
        snap = {
            "timestamp":    time.time(),
            "chain_height": bc.height,
            "total_supply": f"{bc.utxo.total_supply()/10**DECIMALS:.3f} NBL",
            "mempool":      bc.mempool.size(),
            "utxo_set":     bc.utxo.size(),
        }
        if self._node:
            snap["staking"]    = self._node.staking.staking_stats()
            snap["dex"]        = self._node.dex.dex_stats()
            snap["nft"]        = self._node.nft.nft_stats()
            snap["governance"] = self._node.governance.governance_stats()
            snap["bridge"]     = self._node.bridge.bridge_stats()
            snap["social"]     = self._node.social.social_stats()
        return snap

    def yield_opportunities(self) -> List[dict]:
        """List current yield opportunities."""
        opportunities = [
            {"protocol": "NEBULA Staking (Flexible)",   "apy": "5%",  "risk": "low",    "tvl": "N/A"},
            {"protocol": "NEBULA Staking (30-Day Lock)", "apy": "8%",  "risk": "low",    "tvl": "N/A"},
            {"protocol": "NEBULA Staking (90-Day Lock)", "apy": "12%", "risk": "low",    "tvl": "N/A"},
            {"protocol": "NEBULA DEX LP (NBL/USDT)",     "apy": "35%", "risk": "medium", "tvl": "N/A"},
            {"protocol": "NEBULA DEX LP (NBL/BTC)",      "apy": "28%", "risk": "medium", "tvl": "N/A"},
            {"protocol": "NEBULA Lending (Supply NBL)",  "apy": "4%",  "risk": "low",    "tvl": "N/A"},
            {"protocol": "NEBULA Farming (NBL-USDT-LP)", "apy": "65%", "risk": "high",   "tvl": "N/A"},
            {"protocol": "NEBULA Insurance Pool",        "apy": "15%", "risk": "medium", "tvl": "N/A"},
        ]
        return opportunities

    def risk_metrics(self) -> dict:
        """Protocol-wide risk metrics."""
        bc = self._bc
        supply = bc.utxo.total_supply()
        return {
            "circulating_supply_pct": f"{supply/MAX_SUPPLY*100:.4f}%",
            "concentration_risk":     "N/A",
            "smart_contract_risk":    "MEDIUM",
            "bridge_risk":            "MEDIUM",
            "oracle_risk":            "LOW",
            "liquidity_risk":         "LOW",
        }


# ---- NodeConfig
class NodeConfig:
    """Node configuration parameters."""

    def __init__(self):
        self.node_id          = secrets.token_hex(8)
        self.listen_ip        = "0.0.0.0"
        self.listen_port      = DEFAULT_PORT
        self.max_peers        = MAX_PEERS
        self.rpc_port         = 8545
        self.api_port         = 8080
        self.ws_port          = 8546
        self.miner_address    = FOUNDATION_ADDRESS
        self.mining_enabled   = False
        self.prune_depth      = 0          # 0 = full node
        self.log_level        = "INFO"
        self.data_dir         = "./nebula_data"
        self.network          = "mainnet"

    def to_dict(self) -> dict:
        return {
            "node_id":       self.node_id,
            "listen":        f"{self.listen_ip}:{self.listen_port}",
            "api_port":      self.api_port,
            "rpc_port":      self.rpc_port,
            "ws_port":       self.ws_port,
            "max_peers":     self.max_peers,
            "mining":        self.mining_enabled,
            "network":       self.network,
            "log_level":     self.log_level,
            "data_dir":      self.data_dir,
        }

    @classmethod
    def from_env(cls) -> 'NodeConfig':
        """Create config from environment variables."""
        import os
        cfg = cls()
        cfg.miner_address  = os.environ.get("NBL_MINER", FOUNDATION_ADDRESS)
        cfg.mining_enabled = os.environ.get("NBL_MINING", "0") == "1"
        cfg.api_port       = int(os.environ.get("NBL_API_PORT", "8080"))
        cfg.listen_port    = int(os.environ.get("NBL_P2P_PORT", str(DEFAULT_PORT)))
        cfg.log_level      = os.environ.get("NBL_LOG_LEVEL", "INFO")
        cfg.network        = os.environ.get("NBL_NETWORK", "mainnet")
        return cfg


# ---- NodeManager
class NodeManager:
    """
    Manages node lifecycle: start, stop, restart, config.
    Coordinates all node subsystems.
    """

    def __init__(self, config: NodeConfig = None):
        self.config      = config or NodeConfig.from_env()
        self.blockchain  = NEBULABlockchain()
        self.running     = False
        self._threads:   List[threading.Thread] = []
        self._start_time = 0.0

    def start(self) -> bool:
        """Start all node subsystems."""
        if self.running:
            return False
        self.running    = True
        self._start_time = time.time()
        print(f"🌌 NEBULA Node starting...")
        print(f"   Network:  {self.config.network}")
        print(f"   Node ID:  {self.config.node_id}")
        print(f"   API port: {self.config.api_port}")
        print(f"   P2P port: {self.config.listen_port}")
        print(f"   Mining:   {'enabled' if self.config.mining_enabled else 'disabled'}")
        return True

    def stop(self):
        """Gracefully stop the node."""
        self.running = False
        for t in self._threads:
            if t.is_alive():
                t.join(timeout=5)
        print("🔴 NEBULA Node stopped")

    def restart(self):
        self.stop()
        self.start()

    def uptime(self) -> float:
        return time.time() - self._start_time if self.running else 0

    def node_info(self) -> dict:
        return {
            "config":      self.config.to_dict(),
            "running":     self.running,
            "uptime_secs": f"{self.uptime():.0f}",
            "chain_height": self.blockchain.height,
        }


# ---- BridgeRequestV2
@dataclass
class BridgeRequestV2:
    request_id:   str
    direction:    BridgeDirection
    asset:        str
    amount:       int
    sender:       str
    receiver:     str
    src_chain:    str
    dst_chain:    str
    status:       str = "pending"
    tx_hash:      str = ""
    created_at:   float = 0.0
    completed_at: Optional[float] = None

    def to_dict(self) -> dict:
        return {
            "request_id":  self.request_id,
            "direction":   self.direction.value,
            "asset":       self.asset,
            "amount":      f"{self.amount/10**DECIMALS:.6f}",
            "sender":      self.sender,
            "receiver":    self.receiver,
            "src_chain":   self.src_chain,
            "dst_chain":   self.dst_chain,
            "status":      self.status,
        }


# ---- UniversalTokenBridge
class UniversalTokenBridge:
    """
    Universal bridge supporting any NBL-20 token.
    Validators confirm cross-chain transfers.
    """

    VALIDATOR_THRESHOLD = 3    # require 3 validators
    MAX_DAILY_LIMIT     = 1_000_000 * 10**DECIMALS

    def __init__(self, blockchain: 'NEBULABlockchain',
                  nbl20_registry: 'NBL20Registry' = None):
        self._bc        = blockchain
        self._registry  = nbl20_registry
        self._requests: Dict[str, BridgeRequest]      = {}
        self._validator_sigs: Dict[str, Set[str]]     = {}
        self._validators: Set[str]                    = set()
        self._daily_volume: Dict[str, int]            = {}
        self._lock      = threading.RLock()

    def add_validator(self, address: str):
        with self._lock:
            self._validators.add(address)

    def submit_bridge_request(self, sender: str, asset: str,
                               amount_raw: int, receiver: str,
                               dst_chain: str) -> Tuple[bool, str]:
        with self._lock:
            today = time.strftime('%Y-%m-%d')
            daily = self._daily_volume.get(today, 0)
            if daily + amount_raw > self.MAX_DAILY_LIMIT:
                return False, "Daily bridge limit exceeded"
            rid = hashlib.sha256(
                f"BRIDGE:{sender}:{asset}:{amount_raw}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._requests[rid] = BridgeRequestV2(
                request_id  = rid,
                direction   = BridgeDirection.FROM_NEBULA,
                asset       = asset,
                amount      = amount_raw,
                sender      = sender,
                receiver    = receiver,
                src_chain   = "nebula",
                dst_chain   = dst_chain,
                created_at  = time.time(),
            )
            self._validator_sigs[rid] = set()
            self._daily_volume[today] = daily + amount_raw
            return True, rid

    def validator_sign(self, validator: str,
                        request_id: str) -> Tuple[bool, str]:
        with self._lock:
            if validator not in self._validators:
                return False, "Not a validator"
            req = self._requests.get(request_id)
            if not req:
                return False, "Request not found"
            self._validator_sigs[request_id].add(validator)
            n = len(self._validator_sigs[request_id])
            if n >= self.VALIDATOR_THRESHOLD:
                req.status       = "approved"
                req.completed_at = time.time()
                return True, f"APPROVED ({n}/{self.VALIDATOR_THRESHOLD} validators)"
            return True, f"Signed ({n}/{self.VALIDATOR_THRESHOLD})"

    def get_status(self, request_id: str) -> Optional[dict]:
        req = self._requests.get(request_id)
        if not req:
            return None
        return {
            **req.to_dict(),
            "validator_sigs": len(self._validator_sigs.get(request_id, set())),
            "threshold":      self.VALIDATOR_THRESHOLD,
        }

    def bridge_stats(self) -> dict:
        with self._lock:
            by_status = {}
            for r in self._requests.values():
                by_status[r.status] = by_status.get(r.status, 0) + 1
            today_vol = self._daily_volume.get(time.strftime('%Y-%m-%d'), 0)
        return {
            "total_requests": len(self._requests),
            "by_status":      by_status,
            "validators":     len(self._validators),
            "today_volume":   f"{today_vol/10**DECIMALS:.3f} NBL",
        }


# ---- MarginPosition
class MarginPosition:
    """A leveraged trading position."""

    def __init__(self, pos_id: str, trader: str,
                  pair: str, side: str, size: float,
                  leverage: float, entry_price: float,
                  collateral: float):
        self.pos_id      = pos_id
        self.trader      = trader
        self.pair        = pair
        self.side        = side       # "long" or "short"
        self.size        = size
        self.leverage    = leverage
        self.entry_price = entry_price
        self.collateral  = collateral
        self.margin_used = size / leverage
        self.liquidation_price = self._calc_liq_price()
        self.open        = True
        self.pnl         = 0.0

    def _calc_liq_price(self) -> float:
        if self.side == "long":
            return self.entry_price * (1 - 1/self.leverage + 0.005)
        else:
            return self.entry_price * (1 + 1/self.leverage - 0.005)

    def update_pnl(self, current_price: float):
        if self.side == "long":
            self.pnl = (current_price - self.entry_price) * self.size
        else:
            self.pnl = (self.entry_price - current_price) * self.size

    def is_liquidatable(self, current_price: float) -> bool:
        if self.side == "long":
            return current_price <= self.liquidation_price
        return current_price >= self.liquidation_price

    def to_dict(self, current_price: float = 0) -> dict:
        if current_price:
            self.update_pnl(current_price)
        return {
            "pos_id":      self.pos_id,
            "trader":      self.trader,
            "pair":        self.pair,
            "side":        self.side,
            "size":        f"{self.size:.4f}",
            "leverage":    f"{self.leverage}x",
            "entry":       f"{self.entry_price:.4f}",
            "liq_price":   f"{self.liquidation_price:.4f}",
            "pnl":         f"{self.pnl:.4f}",
            "open":        self.open,
        }


# ---- MarginTradingEngine
class MarginTradingEngine:
    """
    Margin trading with up to 10x leverage on NEBULA DEX.
    Long/short positions with automatic liquidation.
    """

    MAX_LEVERAGE     = 10
    MAINTENANCE_MARGIN = 0.05   # 5% maintenance margin
    LIQUIDATION_FEE  = 0.015    # 1.5% liquidation fee

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc         = blockchain
        self._oracle     = oracle
        self._positions: Dict[str, MarginPosition] = {}
        self._lock       = threading.RLock()

    def open_position(self, trader: str, pair: str,
                       side: str, size_nbl: float,
                       leverage: float) -> Tuple[bool, str]:
        with self._lock:
            if leverage > self.MAX_LEVERAGE:
                return False, f"Max leverage: {self.MAX_LEVERAGE}x"
            if side not in ("long", "short"):
                return False, "Side must be 'long' or 'short'"
            collateral = size_nbl / leverage
            if self._bc.utxo.balance(trader) < int(collateral * 10**DECIMALS):
                return False, "Insufficient collateral"
            price = (self._oracle.price(pair) if self._oracle else 1.0) or 1.0
            pid   = hashlib.sha256(
                f"MARGIN:{trader}:{pair}:{side}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._positions[pid] = MarginPosition(
                pos_id      = pid,
                trader      = trader,
                pair        = pair,
                side        = side,
                size        = size_nbl,
                leverage    = leverage,
                entry_price = price,
                collateral  = collateral,
            )
            return True, pid

    def close_position(self, pos_id: str,
                        trader: str) -> Tuple[bool, float]:
        with self._lock:
            pos = self._positions.get(pos_id)
            if not pos or pos.trader != trader or not pos.open:
                return False, 0.0
            price = (self._oracle.price(pos.pair)
                     if self._oracle else pos.entry_price) or pos.entry_price
            pos.update_pnl(price)
            pos.open = False
            return True, pos.pnl

    def check_liquidations(self) -> List[str]:
        liquidated = []
        with self._lock:
            for pid, pos in list(self._positions.items()):
                if not pos.open:
                    continue
                price = (self._oracle.price(pos.pair)
                         if self._oracle else pos.entry_price) or pos.entry_price
                if pos.is_liquidatable(price):
                    pos.open = False
                    liquidated.append(pid)
        return liquidated

    def trader_positions(self, trader: str) -> List[dict]:
        price_fn = lambda p: (self._oracle.price(p.pair)
                               if self._oracle else 0) or 0
        return [p.to_dict(price_fn(p)) for p in self._positions.values()
                if p.trader == trader and p.open]

    def margin_stats(self) -> dict:
        with self._lock:
            open_pos    = sum(1 for p in self._positions.values() if p.open)
            total_size  = sum(p.size for p in self._positions.values() if p.open)
        return {
            "open_positions":  open_pos,
            "total_size_nbl":  f"{total_size:.3f}",
            "max_leverage":    f"{self.MAX_LEVERAGE}x",
        }


# ---- OptionType
class OptionType(_enum.Enum):
    CALL = "call"
    PUT  = "put"
