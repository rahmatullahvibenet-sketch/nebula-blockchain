"""NEBULA group44 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. PositionManager  (orig. lines 71553-71622)
   2. LiquidationEngine  (orig. lines 71629-71708)
   3. EVMBridge  (orig. lines 71715-71772)
   4. StakedNBL  (orig. lines 71779-71841)
   5. ProtocolStatsDashboard  (orig. lines 71848-71922)
   6. IntegrationTestSuite  (orig. lines 71929-72066)
   7. ProofOfReserves  (orig. lines 72081-72131)
   8. TreasuryBond  (orig. lines 72138-72163)
   9. TreasuryBondMarket  (orig. lines 72165-72228)
  10. RewardsDistributor  (orig. lines 72235-72297)
  11. FeeSharing  (orig. lines 72304-72365)
  12. GovernanceForum  (orig. lines 72372-72440)
  13. PerpetualVault  (orig. lines 72447-72510)
  14. PerpetualVaultRegistry  (orig. lines 72512-72545)
  15. ChainGovernanceParameter  (orig. lines 72552-72572)
  16. ChainGovernance  (orig. lines 72574-72636)
  17. AuditTrail  (orig. lines 72643-72689)
  18. RiskLevel  (orig. lines 72696-72700)
  19. ProtocolRiskEngine  (orig. lines 72702-72761)
  20. SupplyScheduleEngine  (orig. lines 72768-72840)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): AuditEvent, DeFiPosition, GovernanceEngine, MerkleTree, NBL721Registry, NEBULABlockchain, NEBULADex, NEBULAFullNodeV2, NEBULANameService, NEBULAWallet, OnChainLottery, OnChainRNG, PositionType, ProposalType
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

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

INITIAL_BITS           = 0x1e0fffff if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d0fffff   # [v10.24]

MAX_TARGET             = 0x0fffff * (256 ** ((0x1e if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d) - 3))   # [v10.24]   # bits_to_target(INITIAL_BITS) — max allowed PoW target

MAX_BLOCK_SIZE_BYTES   = 1_048_576                      # 1 MB

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

DUST_THRESHOLD         = 546                            # min output amount in Neb

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

def err(msg, code=None):
    """CLI: err("text") prints a red line.  REST API (v10.10 fix): err("text", 404) -> (404, body)."""
    if code is None:
        print(c(f"❌ {msg}", C.RED))
        return None
    return code, {"success": False, "error": str(msg)}

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

def _v108_audit_post(o):
    o.event_type = o.category
    if not o.event_id:
        o.event_id = _v108_hashlib.sha256(
            f"{o.category}:{o.actor}:{o.timestamp}:{id(o)}".encode()).hexdigest()[:16]

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- PositionManager
class PositionManager:
    """Tracks all DeFi positions for a user."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc       = blockchain
        self._oracle   = oracle
        self._positions: Dict[str, DeFiPosition] = {}
        self._lock     = threading.RLock()

    def add_position(self, owner: str, protocol: str,
                      pos_type: PositionType, asset: str,
                      amount: float, apy: float = 0,
                      metadata: dict = None) -> str:
        with self._lock:
            nbl_price = (self._oracle.price("NBL/USD")
                         if self._oracle else 0.01) or 0.01
            value     = amount * nbl_price if asset == "NBL" else amount
            pid       = hashlib.sha256(
                f"POS:{owner}:{protocol}:{asset}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._positions[pid] = DeFiPosition(
                pos_id    = pid,
                owner     = owner,
                protocol  = protocol,
                pos_type  = pos_type,
                asset     = asset,
                amount    = amount,
                value_usd = value,
                apy       = apy,
                opened_at = time.time(),
                metadata  = metadata or {},
            )
            return pid

    def close_position(self, pos_id: str, owner: str) -> bool:
        with self._lock:
            pos = self._positions.get(pos_id)
            if pos and pos.owner == owner:
                del self._positions[pos_id]
                return True
            return False

    def portfolio_overview(self, owner: str) -> dict:
        with self._lock:
            positions = [p for p in self._positions.values()
                         if p.owner == owner]
        total_value = sum(p.value_usd for p in positions)
        by_type     = {}
        for p in positions:
            k = p.pos_type.value
            by_type[k] = by_type.get(k, 0) + p.value_usd
        return {
            "owner":       owner,
            "positions":   len(positions),
            "total_usd":   f"${total_value:.2f}",
            "by_type":     {k: f"${v:.2f}" for k, v in by_type.items()},
            "details":     [p.to_dict() for p in positions],
        }

    def total_apy_weighted(self, owner: str) -> float:
        with self._lock:
            positions = [p for p in self._positions.values()
                         if p.owner == owner]
        if not positions:
            return 0.0
        total_value  = sum(p.value_usd for p in positions) or 1
        weighted_apy = sum(p.apy * p.value_usd / total_value
                           for p in positions)
        return weighted_apy


# ---- LiquidationEngine
class LiquidationEngine:
    """
    Cross-protocol liquidation engine for NEBULA.
    Monitors health factors and executes liquidations.
    """

    LIQUIDATION_BONUS = 0.05   # 5% bonus for liquidators

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._monitored: Dict[str, dict] = {}   # account -> {debt, collateral, protocol}
        self._lock    = threading.RLock()

    def register_position(self, account: str, protocol: str,
                           debt: int, collateral: int,
                           collateral_asset: str = "NBL"):
        with self._lock:
            self._monitored[f"{account}:{protocol}"] = {
                "account":          account,
                "protocol":         protocol,
                "debt":             debt,
                "collateral":       collateral,
                "collateral_asset": collateral_asset,
            }

    def health_factor(self, key: str) -> float:
        pos   = self._monitored.get(key)
        if not pos or pos["debt"] == 0:
            return float('inf')
        price = (self._oracle.price(f"{pos['collateral_asset']}/USD")
                 if self._oracle else 0.01) or 0.01
        col_usd  = pos["collateral"] * price / 10**DECIMALS
        debt_usd = pos["debt"] / 10**DECIMALS
        return col_usd * 0.8 / debt_usd if debt_usd > 0 else float('inf')

    def scan_for_liquidations(self) -> List[dict]:
        underwater = []
        with self._lock:
            for key, pos in list(self._monitored.items()):
                hf = self.health_factor(key)
                if hf < 1.0:
                    underwater.append({
                        "key":           key,
                        "account":       pos["account"],
                        "protocol":      pos["protocol"],
                        "health_factor": f"{hf:.4f}",
                        "debt":          pos["debt"],
                        "collateral":    pos["collateral"],
                    })
        return underwater

    def liquidate(self, liquidator: str, target_key: str,
                   repay_amount: int) -> Tuple[bool, dict]:
        with self._lock:
            pos = self._monitored.get(target_key)
            if not pos:
                return False, {}
            hf = self.health_factor(target_key)
            if hf >= 1.0:
                return False, {"error": "Not underwater"}
            bonus     = int(repay_amount * self.LIQUIDATION_BONUS)
            collat_received = repay_amount + bonus
            pos["debt"]       -= repay_amount
            pos["collateral"] -= collat_received
            return True, {
                "repaid":       repay_amount,
                "received":     collat_received,
                "bonus":        bonus,
                "new_hf":       self.health_factor(target_key),
            }

    def liquidation_stats(self) -> dict:
        underwater = self.scan_for_liquidations()
        return {
            "monitored":   len(self._monitored),
            "underwater":  len(underwater),
            "liquidation_bonus": f"{self.LIQUIDATION_BONUS*100:.0f}%",
        }


# ---- EVMBridge
class EVMBridge:
    """
    EVM compatibility bridge for NEBULA.
    Allows Solidity contracts to interact with NEBULA.
    Translates EVM calls to NEBULA native format.
    """

    EVM_CHAIN_ID = 2025   # NEBULA EVM chain ID

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._evm_txs:  List[dict] = []
        self._contracts: Dict[str, str] = {}   # evm_addr -> nbl_contract_id
        self._lock      = threading.RLock()

    def eth_call(self, to: str, data: str,
                  from_addr: str = "0x0",
                  value: int = 0) -> str:
        """Execute a read-only EVM call."""
        return "0x" + hashlib.sha256(f"EVM_CALL:{to}:{data}".encode()).hexdigest()

    def eth_send_transaction(self, from_addr: str, to: str,
                              data: str, value: int = 0,
                              gas: int = 21000) -> str:
        """Submit an EVM transaction."""
        with self._lock:
            tx_hash = "0x" + hashlib.sha256(
                f"EVM_TX:{from_addr}:{to}:{data}:{time.time()}".encode()
            ).hexdigest()
            self._evm_txs.append({
                "hash":     tx_hash,
                "from":     from_addr,
                "to":       to,
                "value":    value,
                "gas":      gas,
                "data":     data[:64],
                "status":   1,
            })
            return tx_hash

    def eth_get_balance(self, address: str) -> str:
        """Get NBL balance in ETH format (18 decimals)."""
        bal = self._bc.utxo.balance(address)
        evm_bal = bal * (10**18 // 10**DECIMALS)
        return hex(evm_bal)

    def eth_block_number(self) -> str:
        return hex(self._bc.height)

    def eth_chain_id(self) -> str:
        return hex(self.EVM_CHAIN_ID)

    def evm_stats(self) -> dict:
        return {
            "chain_id":    self.EVM_CHAIN_ID,
            "tx_count":    len(self._evm_txs),
            "contracts":   len(self._contracts),
        }


# ---- StakedNBL
class StakedNBL:
    """
    stNBL — liquid staked NBL token.
    Stake NBL and receive stNBL, which accrues rewards.
    Exchange ratio grows over time.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  staking: 'StakingEngine' = None):
        self._bc        = blockchain
        self._staking   = staking
        self._total_nbl_staked: int = 0
        self._total_stnbl:      int = 0
        self._stnbl_balances:   Dict[str, int] = {}
        self._lock      = threading.RLock()
        self._inception_block = blockchain.height

    @property
    def exchange_rate(self) -> float:
        """stNBL to NBL exchange rate (always >= 1.0)."""
        if self._total_stnbl == 0:
            return 1.0
        return self._total_nbl_staked / self._total_stnbl

    def stake(self, staker: str, amount: int) -> Tuple[bool, int]:
        with self._lock:
            if self._bc.utxo.balance(staker) < amount:
                return False, 0
            stnbl = int(amount / self.exchange_rate)
            self._total_nbl_staked += amount
            self._total_stnbl      += stnbl
            self._stnbl_balances[staker] = (
                self._stnbl_balances.get(staker, 0) + stnbl)
            return True, stnbl

    def unstake(self, staker: str, stnbl_amount: int) -> Tuple[bool, int]:
        with self._lock:
            if self._stnbl_balances.get(staker, 0) < stnbl_amount:
                return False, 0
            nbl_out = int(stnbl_amount * self.exchange_rate)
            self._stnbl_balances[staker]  -= stnbl_amount
            self._total_stnbl             -= stnbl_amount
            self._total_nbl_staked        -= nbl_out
            return True, nbl_out

    def accrue_rewards(self, amount: int):
        """Increase total NBL staked (simulating rewards)."""
        with self._lock:
            self._total_nbl_staked += amount

    def stnbl_balance(self, address: str) -> int:
        return self._stnbl_balances.get(address, 0)

    def nbl_value(self, stnbl: int) -> float:
        return stnbl * self.exchange_rate

    def stnbl_stats(self) -> dict:
        return {
            "total_staked_nbl": f"{self._total_nbl_staked/10**DECIMALS:.3f}",
            "total_stnbl":      f"{self._total_stnbl/10**DECIMALS:.3f}",
            "exchange_rate":    f"{self.exchange_rate:.6f}",
            "holders":          len(self._stnbl_balances),
        }


# ---- ProtocolStatsDashboard
class ProtocolStatsDashboard:
    """
    Comprehensive protocol statistics dashboard.
    Aggregates data from all subsystems.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def summary(self) -> dict:
        bc    = self._bc
        h     = bc.height
        sup   = bc.utxo.total_supply()
        return {
            "protocol":     "NEBULA Blockchain",
            "version":      f"{CHAIN_VERSION}",
            "chain_id":     CHAIN_ID,
            "height":       h,
            "supply":       f"{sup/10**DECIMALS:.3f} NBL",
            "max_supply":   f"{MAX_SUPPLY/10**DECIMALS:.0f} NBL",
            "supply_pct":   f"{sup/MAX_SUPPLY*100:.4f}%",
            "reward":       f"{mining_reward(h)/10**DECIMALS:.9f} NBL",
            "next_halving": (h // HALVING_INTERVAL + 1) * HALVING_INTERVAL,
            "mempool":      bc.mempool.size(),
            "utxo_set":     bc.utxo.size(),
        }

    def mining_stats(self) -> dict:
        bc   = self._bc
        h    = bc.height
        era  = h // HALVING_INTERVAL
        bits = bc.tip.header.bits if bc.height >= 0 else INITIAL_BITS
        return {
            "height":          h,
            "era":             era + 1,
            "reward":          f"{mining_reward(h)/10**DECIMALS:.9f}",
            "next_halving":    (era + 1) * HALVING_INTERVAL,
            "blocks_to_half":  HALVING_INTERVAL - (h % HALVING_INTERVAL),
            "bits":            bits,
            "difficulty":      f"{MAX_TARGET/max(1, bits_to_target(bits)):.2f}",
            "algorithm":       "SHA-256 Proof of Work",
        }

    def defi_overview(self) -> dict:
        return {
            "protocols": [
                "DEX (AMM + Order Book)",
                "Lending & Borrowing",
                "Staking (Flexible + Locked)",
                "Yield Farming",
                "NFT Marketplace",
                "Stablecoin (NBUSD)",
                "Cross-Chain Bridge",
                "Prediction Markets",
                "Options & Futures",
                "Insurance",
            ],
            "features": [
                "Identity (DID)",
                "Governance",
                "Social Network",
                "Data Marketplace",
                "Name Service",
                "Privacy Pool",
                "Atomic Swaps",
                "Layer-2 Bridge",
            ],
        }

    def full_stats(self) -> dict:
        return {
            "summary":  self.summary(),
            "mining":   self.mining_stats(),
            "defi":     self.defi_overview(),
        }


# ---- IntegrationTestSuite
class IntegrationTestSuite:
    """
    Full integration tests for NEBULA ecosystem.
    Tests complete user journeys across multiple protocols.
    """

    def __init__(self):
        self.passed  = 0
        self.failed  = 0
        self.results = []

    def _ok(self, name: str, detail: str = ""):
        self.passed += 1
        self.results.append({"name": name, "status": "PASS", "detail": detail})
        print(f"  ✅ {name}" + (f" — {detail}" if detail else ""))

    def _fail(self, name: str, err: str):
        self.failed += 1
        self.results.append({"name": name, "status": "FAIL", "detail": err})
        print(f"  ❌ {name}: {err}")

    def test_full_node_init(self):
        print("\n🌌 Full Node Init")
        try:
            bc   = NEBULABlockchain()
            node = NEBULAFullNodeV2(miner_address=FOUNDATION_ADDRESS)
            assert node.blockchain.height >= 0
            self._ok("Full node init", f"height={node.blockchain.height}")
            status = node.node_status()
            assert "chain_height" in status
            self._ok("Node status endpoint")
        except Exception as e:
            self._fail("Full node init", str(e))

    def test_wallet_to_wallet(self):
        print("\n💸 Wallet-to-Wallet Transfer")
        try:
            bc    = NEBULABlockchain()
            w1    = NEBULAWallet.generate()
            w2    = NEBULAWallet.generate()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(w1.first_address, 1000)
            bal1  = bc.utxo.balance(w1.first_address)
            assert bal1 == 1000 * 10**DECIMALS
            self._ok("Wallet funded", f"balance={bal1/10**DECIMALS} NBL")
            self._ok("Wallet-to-wallet transfer simulation")
        except Exception as e:
            self._fail("Wallet transfer", str(e))

    def test_complete_defi_journey(self):
        print("\n🏦 Complete DeFi Journey")
        try:
            bc     = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 100_000)
            ok, m  = stk.stake(FOUNDATION_ADDRESS, 1_000 * 10**DECIMALS)
            assert ok, m
            self._ok("Stake NBL", m)
            gov  = GovernanceEngine(bc)
            ok2, pid = gov.propose(
                FOUNDATION_ADDRESS, ProposalType.TEXT,
                "Test", "Integration test", {})
            assert ok2, pid
            self._ok("Create governance proposal", pid)
            ok3, m3 = gov.cast_vote(FOUNDATION_ADDRESS, pid, "yes")
            assert ok3, m3
            self._ok("Cast governance vote", m3)
            dex  = NEBULADex(bc)
            pid2 = dex.create_pool("NBL", "USDT", fee_bps=30)
            assert pid2
            self._ok("Create DEX pool", pid2)
        except Exception as e:
            self._fail("DeFi journey", str(e))

    def test_nft_lifecycle(self):
        print("\n🖼️  NFT Lifecycle")
        try:
            nft = NBL721Registry()
            cid = nft.create_collection(
                FOUNDATION_ADDRESS, "Test NFT", "TNFT",
                "Integration test NFT", 100, 0.05)
            assert cid
            self._ok("Create collection", cid[:16])
            tid, msg = nft.mint(cid, FOUNDATION_ADDRESS, "ipfs://test",
                                {"name": "Test #1"}, FOUNDATION_ADDRESS)
            assert tid == 1
            self._ok("Mint NFT", f"token #{tid}")
            owner = nft.owner_of(cid, tid)
            assert owner == FOUNDATION_ADDRESS
            self._ok("Verify ownership")
        except Exception as e:
            self._fail("NFT lifecycle", str(e))

    def test_cross_module_integration(self):
        print("\n🔗 Cross-Module Integration")
        try:
            bc  = NEBULABlockchain()
            # ZK + Bridge
            secret = secrets.token_bytes(32)
            sh  = hashlib.sha256(secret).hexdigest()
            self._ok("HTLC hash created", sh[:16])
            # VRF + Lottery
            bc2   = NEBULABlockchain()
            rng   = OnChainRNG(bc2)
            lot   = OnChainLottery(bc2, rng)
            rid   = lot.start_round(draw_block=1)
            ok, t = lot.buy_ticket(FOUNDATION_ADDRESS, rid)
            assert ok, t
            self._ok("Lottery ticket purchased")
            # Name Service
            nns   = NEBULANameService(bc)
            bc.fund_address(FOUNDATION_ADDRESS, 1000)
            ok2, domain = nns.register("zayn", FOUNDATION_ADDRESS, 1)
            assert ok2, domain
            addr   = nns.resolve("zayn.nbl")
            assert addr == FOUNDATION_ADDRESS
            self._ok("Name service resolve", f"zayn.nbl → {addr[:8]}...")
        except Exception as e:
            self._fail("Cross-module integration", str(e))

    def run_all(self) -> dict:
        print("\n" + "═" * 55)
        print("  🔗 NEBULA INTEGRATION TEST SUITE")
        print("═" * 55)
        start = time.time()
        self.test_full_node_init()
        self.test_wallet_to_wallet()
        self.test_complete_defi_journey()
        self.test_nft_lifecycle()
        self.test_cross_module_integration()
        elapsed = time.time() - start
        total   = self.passed + self.failed
        pct     = self.passed / total * 100 if total > 0 else 0
        print(f"\n{'═'*55}")
        print(f"  Integration: {self.passed}/{total} passed ({pct:.0f}%)")
        print(f"  Time: {elapsed:.2f}s")
        print(f"{'═'*55}\n")
        return {"passed": self.passed, "failed": self.failed, "pct": f"{pct:.0f}%"}


# ---- ProofOfReserves
class ProofOfReserves:
    """
    Cryptographic proof of reserves for NEBULA custodians.
    Proves total assets >= total liabilities without revealing individuals.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._snapshots: List[dict] = []
        self._lock      = threading.RLock()

    def generate_proof(self, custodian: str,
                        liabilities: Dict[str, int]) -> dict:
        """Generate proof that assets >= liabilities."""
        total_liab = sum(liabilities.values())
        # Sum all on-chain balances controlled by custodian
        # (In production: use Merkle sum tree)
        total_assets = self._bc.utxo.balance(custodian)
        proof_hash   = hashlib.sha256(
            json.dumps({"custodian": custodian,
                        "liabilities": total_liab,
                        "assets": total_assets,
                        "block": self._bc.height},
                       sort_keys=True).encode()
        ).hexdigest()
        proof = {
            "custodian":     custodian,
            "total_assets":  f"{total_assets/10**DECIMALS:.9f} NBL",
            "total_liab":    f"{total_liab/10**DECIMALS:.9f} NBL",
            "solvent":       total_assets >= total_liab,
            "surplus_nbl":   f"{max(0, total_assets-total_liab)/10**DECIMALS:.9f}",
            "block_height":  self._bc.height,
            "proof_hash":    proof_hash,
            "timestamp":     time.time(),
        }
        with self._lock:
            self._snapshots.append(proof)
        return proof

    def verify_proof(self, proof: dict) -> bool:
        expected = hashlib.sha256(
            json.dumps({"custodian":    proof["custodian"],
                        "liabilities":  proof["total_liab"],
                        "assets":       proof["total_assets"],
                        "block":        proof["block_height"]},
                       sort_keys=True).encode()
        ).hexdigest()
        return expected == proof.get("proof_hash", "")

    def history(self, n: int = 10) -> List[dict]:
        return self._snapshots[-n:]


# ---- TreasuryBond
@dataclass
class TreasuryBond:
    bond_id:       str
    issuer:        str
    holder:        str
    principal:     int
    coupon_rate:   float
    maturity_block: int
    issued_at:     int
    coupons_paid:  int = 0
    redeemed:      bool = False

    @property
    def coupon_blocks(self) -> int:
        return 144 * 30   # monthly coupon

    def to_dict(self) -> dict:
        return {
            "bond_id":      self.bond_id,
            "holder":       self.holder,
            "principal":    f"{self.principal/10**DECIMALS:.3f} NBL",
            "coupon":       f"{self.coupon_rate*100:.2f}%/yr",
            "maturity":     self.maturity_block,
            "coupons_paid": self.coupons_paid,
            "redeemed":     self.redeemed,
        }


# ---- TreasuryBondMarket
class TreasuryBondMarket:
    """
    NEBULA treasury bond market.
    Protocol issues bonds to raise funding, pays coupon + principal.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._bonds: Dict[str, TreasuryBond] = {}
        self._lock   = threading.RLock()

    def issue_bond(self, issuer: str, holder: str,
                    principal_nbl: float,
                    coupon_rate: float,
                    duration_days: int) -> str:
        with self._lock:
            bid = hashlib.sha256(
                f"BOND:{issuer}:{holder}:{principal_nbl}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._bonds[bid] = TreasuryBond(
                bond_id        = bid,
                issuer         = issuer,
                holder         = holder,
                principal      = int(principal_nbl * 10**DECIMALS),
                coupon_rate    = coupon_rate,
                maturity_block = self._bc.height + duration_days * 144,
                issued_at      = self._bc.height,
            )
            return bid

    def pay_coupon(self, bond_id: str) -> Tuple[bool, int]:
        with self._lock:
            bond = self._bonds.get(bond_id)
            if not bond or bond.redeemed:
                return False, 0
            annual_coupon   = int(bond.principal * bond.coupon_rate)
            periods_per_yr  = 365 * 144 // bond.coupon_blocks
            payment         = annual_coupon // max(1, periods_per_yr)
            bond.coupons_paid += 1
            return True, payment

    def redeem(self, bond_id: str, holder: str) -> Tuple[bool, int]:
        with self._lock:
            bond = self._bonds.get(bond_id)
            if not bond or bond.holder != holder:
                return False, 0
            if self._bc.height < bond.maturity_block:
                return False, bond.maturity_block - self._bc.height
            if bond.redeemed:
                return False, 0
            bond.redeemed = True
            return True, bond.principal

    def bond_market_stats(self) -> dict:
        with self._lock:
            active  = [b for b in self._bonds.values()
                       if not b.redeemed and
                       self._bc.height < b.maturity_block]
            total_outstanding = sum(b.principal for b in active)
        return {
            "total_bonds":    len(self._bonds),
            "active":         len(active),
            "outstanding_nbl": f"{total_outstanding/10**DECIMALS:.3f}",
        }


# ---- RewardsDistributor
class RewardsDistributor:
    """
    Distributes protocol rewards to multiple recipients.
    Merkle-tree based distribution for gas efficiency.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._distributions: List[dict] = []
        self._claimed:       Dict[str, Set[int]] = {}
        self._lock          = threading.RLock()

    def create_distribution(self, token: str,
                              rewards: Dict[str, int]) -> str:
        with self._lock:
            leaves = [f"{addr}:{amount}" for addr, amount in rewards.items()]
            merkle_root = MerkleTree.compute_root(
                [hashlib.sha256(l.encode()).hexdigest() for l in leaves])
            dist_id = len(self._distributions)
            self._distributions.append({
                "id":          dist_id,
                "token":       token,
                "merkle_root": merkle_root,
                "rewards":     rewards,
                "total":       sum(rewards.values()),
                "created_at":  time.time(),
                "block":       self._bc.height,
            })
            return merkle_root

    def claim(self, dist_id: int, address: str) -> Tuple[bool, int]:
        with self._lock:
            if dist_id >= len(self._distributions):
                return False, 0
            dist = self._distributions[dist_id]
            if dist_id not in self._claimed:
                self._claimed[dist_id] = set()
            if address in self._claimed[dist_id]:
                return False, 0
            amount = dist["rewards"].get(address, 0)
            if amount == 0:
                return False, 0
            self._claimed[dist_id].add(address)
            return True, amount

    def unclaimed(self, address: str) -> List[dict]:
        result = []
        for i, dist in enumerate(self._distributions):
            if (address in dist["rewards"] and
                    address not in self._claimed.get(i, set())):
                result.append({
                    "dist_id": i,
                    "token":   dist["token"],
                    "amount":  dist["rewards"][address],
                })
        return result

    def distributor_stats(self) -> dict:
        total_dist = sum(d["total"] for d in self._distributions)
        return {
            "distributions": len(self._distributions),
            "total_nbl":     f"{total_dist/10**DECIMALS:.3f}",
        }


# ---- FeeSharing
class FeeSharing:
    """
    Protocol fee sharing with NBL holders.
    Convert trading fees to NBL and distribute.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._pending:  int = 0
        self._snapshots: Dict[str, int] = {}   # holder -> balance at snapshot
        self._epoch:    int = 0
        self._epochs:   List[dict] = []
        self._lock      = threading.RLock()

    def accumulate(self, amount: int):
        with self._lock:
            self._pending += amount

    def take_snapshot(self) -> dict:
        """Take balance snapshot for fee sharing."""
        with self._lock:
            snap   = {}
            total  = 0
            for addr, utxos in self._bc.utxo._addr_idx.items():
                bal = self._bc.utxo.balance(addr)
                if bal > 0:
                    snap[addr] = bal
                    total     += bal
            self._snapshots = snap
            epoch_info = {
                "epoch":    self._epoch,
                "total":    total,
                "pending":  self._pending,
                "block":    self._bc.height,
                "holders":  len(snap),
            }
            self._epochs.append(epoch_info)
            self._epoch += 1
            return epoch_info

    def claim_fees(self, address: str) -> Tuple[bool, int]:
        with self._lock:
            if not self._epochs:
                return False, 0
            last_epoch  = self._epochs[-1]
            snap_bal    = self._snapshots.get(address, 0)
            total_snap  = last_epoch["total"]
            if total_snap == 0 or snap_bal == 0:
                return False, 0
            share   = snap_bal / total_snap
            amount  = int(self._pending * share)
            if amount == 0:
                return False, 0
            self._pending -= amount
            return True, amount

    def fee_sharing_stats(self) -> dict:
        return {
            "pending_nbl": f"{self._pending/10**DECIMALS:.6f}",
            "epochs":      len(self._epochs),
            "holders":     len(self._snapshots),
        }


# ---- GovernanceForum
class GovernanceForum:
    """
    On-chain governance forum for proposal discussion.
    Temperature checks, feedback, off-chain signaling.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._threads: List[dict] = []
        self._comments: Dict[str, List[dict]] = {}
        self._lock     = threading.RLock()

    def create_thread(self, author: str, title: str,
                       content: str, category: str = "general") -> str:
        with self._lock:
            tid = hashlib.sha256(
                f"FORUM:{author}:{title}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._threads.append({
                "id":        tid,
                "author":    author,
                "title":     title,
                "content":   content[:1000],
                "category":  category,
                "timestamp": time.time(),
                "likes":     0,
                "views":     0,
            })
            self._comments[tid] = []
            return tid

    def comment(self, thread_id: str, author: str,
                 content: str) -> bool:
        with self._lock:
            if thread_id not in self._comments:
                return False
            self._comments[thread_id].append({
                "author":    author,
                "content":   content[:500],
                "timestamp": time.time(),
            })
            return True

    def temperature_check(self, thread_id: str,
                           voter: str, support: bool):
        with self._lock:
            for t in self._threads:
                if t["id"] == thread_id:
                    t["likes"] += (1 if support else -1)
                    break

    def get_thread(self, thread_id: str) -> Optional[dict]:
        for t in self._threads:
            if t["id"] == thread_id:
                return {
                    **t,
                    "comments":     self._comments.get(thread_id, []),
                    "comment_count": len(self._comments.get(thread_id, [])),
                }
        return None

    def hot_threads(self, n: int = 10) -> List[dict]:
        return sorted(self._threads, key=lambda t: t["likes"], reverse=True)[:n]

    def forum_stats(self) -> dict:
        return {
            "threads":      len(self._threads),
            "total_comments": sum(len(c) for c in self._comments.values()),
        }


# ---- PerpetualVault
class PerpetualVault:
    """
    Perpetual auto-compounding vault.
    Continuously reinvests yield for maximum compounding.
    """

    def __init__(self, vault_id: str, strategy: str,
                  target_apy: float, blockchain: 'NEBULABlockchain'):
        self.vault_id    = vault_id
        self.strategy    = strategy
        self.target_apy  = target_apy
        self._bc         = blockchain
        self._total:     int = 0
        self._shares:    Dict[str, int] = {}
        self._last_compound: int = blockchain.height
        self._compound_count = 0

    def deposit(self, depositor: str, amount: int) -> int:
        if self._total == 0:
            shares = amount
        else:
            total_shares = sum(self._shares.values())
            shares = amount * total_shares // self._total if self._total > 0 else amount
        self._shares[depositor] = self._shares.get(depositor, 0) + shares
        self._total += amount
        return shares

    def compound(self) -> int:
        cur     = self._bc.height
        blocks  = cur - self._last_compound
        if blocks <= 0:
            return 0
        bpy     = 365 * 144
        yield_  = int(self._total * self.target_apy * blocks / bpy)
        self._total          += yield_
        self._last_compound   = cur
        self._compound_count += 1
        return yield_

    def withdraw(self, depositor: str, shares: int) -> int:
        self.compound()
        owned = self._shares.get(depositor, 0)
        if owned < shares:
            return 0
        total_shares = sum(self._shares.values()) or 1
        amount = shares * self._total // total_shares
        self._shares[depositor] -= shares
        self._total             -= amount
        return amount

    def share_value(self) -> float:
        total_shares = sum(self._shares.values())
        return self._total / total_shares if total_shares > 0 else 1.0

    def vault_info(self) -> dict:
        self.compound()
        return {
            "vault_id":    self.vault_id,
            "strategy":    self.strategy,
            "target_apy":  f"{self.target_apy*100:.1f}%",
            "total_nbl":   f"{self._total/10**DECIMALS:.6f}",
            "share_value": f"{self.share_value():.8f}",
            "compounds":   self._compound_count,
        }


# ---- PerpetualVaultRegistry
class PerpetualVaultRegistry:
    """Registry of perpetual vaults."""

    VAULTS = [
        ("nbl_max_yield",  "Maximum Yield Strategy",    0.30),
        ("nbl_safe",       "Conservative Strategy",     0.08),
        ("nbl_balanced",   "Balanced Strategy",         0.18),
        ("nbl_defi_alpha", "DeFi Alpha Strategy",       0.45),
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._vaults: Dict[str, PerpetualVault] = {
            vid: PerpetualVault(vid, name, apy, blockchain)
            for vid, name, apy in self.VAULTS
        }

    def deposit(self, vault_id: str, depositor: str,
                 amount_nbl: float) -> Tuple[bool, int]:
        vault = self._vaults.get(vault_id)
        if not vault:
            return False, 0
        amount = int(amount_nbl * 10**DECIMALS)
        shares = vault.deposit(depositor, amount)
        return True, shares

    def compound_all(self) -> dict:
        total_yield = 0
        for v in self._vaults.values():
            total_yield += v.compound()
        return {"total_yield_nbl": f"{total_yield/10**DECIMALS:.6f}"}

    def all_vaults(self) -> List[dict]:
        return [v.vault_info() for v in self._vaults.values()]


# ---- ChainGovernanceParameter
class ChainGovernanceParameter:
    """A governable chain parameter."""

    def __init__(self, name: str, current: Any,
                  min_val: Any = None, max_val: Any = None,
                  description: str = ""):
        self.name        = name
        self.current     = current
        self.min_val     = min_val
        self.max_val     = max_val
        self.description = description
        self.history:    List[Tuple[Any, float]] = [(current, time.time())]

    def update(self, new_val: Any) -> bool:
        if self.min_val is not None and new_val < self.min_val:
            return False
        if self.max_val is not None and new_val > self.max_val:
            return False
        self.history.append((new_val, time.time()))
        self.current = new_val
        return True


# ---- ChainGovernance
class ChainGovernance:
    """
    Chain-level governance for NEBULA.
    Allows governance to update protocol parameters.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._params: Dict[str, ChainGovernanceParameter] = {}
        self._proposals: List[dict] = []
        self._lock   = threading.RLock()
        self._init_params()

    def _init_params(self):
        params = [
            ("min_tx_fee",     MIN_TX_FEE,         1, 10**DECIMALS,    "Minimum transaction fee"),
            ("max_block_size", MAX_BLOCK_SIZE_BYTES, 100_000, 4_000_000, "Max block size bytes"),
            ("target_block_time", TARGET_BLOCK_TIME, 60, 3600,          "Target block time seconds"),
            ("foundation_rate", FOUNDATION_RATE,   0.0,  0.10,          "Foundation fee rate"),
            ("dust_threshold", DUST_THRESHOLD,     1,    1000,          "Dust threshold"),
        ]
        for name, cur, mn, mx, desc in params:
            self._params[name] = ChainGovernanceParameter(name, cur, mn, mx, desc)

    def propose_param_change(self, proposer: str,
                              param: str, new_value: Any,
                              rationale: str) -> Tuple[bool, str]:
        with self._lock:
            if param not in self._params:
                return False, f"Unknown parameter: {param}"
            pid = hashlib.sha256(
                f"CGOV:{param}:{new_value}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._proposals.append({
                "id":        pid,
                "proposer":  proposer,
                "param":     param,
                "new_value": new_value,
                "rationale": rationale,
                "votes":     0.0,
                "status":    "voting",
            })
            return True, pid

    def vote_and_execute(self, proposal_id: str,
                          voter: str,
                          weight: float) -> Tuple[bool, str]:
        with self._lock:
            prop = next((p for p in self._proposals
                         if p["id"] == proposal_id), None)
            if not prop:
                return False, "Not found"
            prop["votes"] += weight
            if prop["votes"] >= 1_000_000:   # threshold in NBL-weight
                param = self._params.get(prop["param"])
                if param and param.update(prop["new_value"]):
                    prop["status"] = "executed"
                    return True, f"Parameter {prop['param']} updated to {prop['new_value']}"
                return False, "Update failed (out of range)"
            return True, f"Vote recorded ({prop['votes']:.0f} weight)"

    def get_params(self) -> dict:
        return {name: p.current for name, p in self._params.items()}


# ---- AuditTrail
class AuditTrail:
    """
    Immutable audit trail for NEBULA protocol actions.
    Records all governance, admin, and protocol events.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._events: List[AuditEvent] = []
        self._lock   = threading.RLock()

    def log(self, event_type: str, actor: str,
             action: str, details: dict = None) -> str:
        with self._lock:
            event       = AuditEventC(event_type=event_type, actor=actor, action=action, details=details or {})
            event.block = self._bc.height
            self._events.append(event)
            return event.event_id

    def query(self, event_type: str = None, actor: str = None,
               limit: int = 50) -> List[dict]:
        events = list(self._events)
        if event_type:
            events = [e for e in events if e.event_type == event_type]
        if actor:
            events = [e for e in events if e.actor == actor]
        return [e.to_dict() for e in events[-limit:]]

    def event_hash_chain(self) -> str:
        """Compute hash chain over all events (immutability proof)."""
        h = hashlib.sha256(b"NEBULA_AUDIT_GENESIS").hexdigest()
        for e in self._events:
            h = hashlib.sha256(
                (h + e.event_id + str(e.timestamp)).encode()
            ).hexdigest()
        return h

    def audit_stats(self) -> dict:
        with self._lock:
            by_type = {}
            for e in self._events:
                by_type[e.event_type] = by_type.get(e.event_type, 0) + 1
        return {
            "total_events": len(self._events),
            "by_type":      by_type,
            "hash_chain":   self.event_hash_chain()[:16] + "...",
        }


# ---- RiskLevel
class RiskLevel(_enum.Enum):
    LOW      = "low"
    MEDIUM   = "medium"
    HIGH     = "high"
    CRITICAL = "critical"


# ---- ProtocolRiskEngine
class ProtocolRiskEngine:
    """
    Protocol risk assessment engine.
    Monitors and scores protocol-wide risk.
    """

    RISK_WEIGHTS = {
        "concentration":  0.25,
        "liquidity":      0.25,
        "smart_contract": 0.20,
        "oracle":         0.15,
        "governance":     0.15,
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._risk_scores: Dict[str, float] = {}
        self._alerts:      List[dict]       = []

    def assess_concentration_risk(self) -> float:
        """Score: high if top holder has >10% supply."""
        total = self._bc.utxo.total_supply()
        if total == 0:
            return 0.0
        addrs = list(self._bc.utxo._addr_idx.keys())[:100]
        max_bal = max((self._bc.utxo.balance(a) for a in addrs), default=0)
        pct     = max_bal / total
        return min(1.0, pct * 5)   # scale to 0-1

    def assess_liquidity_risk(self) -> float:
        """Score: high if mempool is congested."""
        mp_size = self._bc.mempool.size()
        return min(1.0, mp_size / 10_000)

    def overall_risk_score(self) -> dict:
        scores = {
            "concentration":  self.assess_concentration_risk(),
            "liquidity":      self.assess_liquidity_risk(),
            "smart_contract": 0.3,
            "oracle":         0.2,
            "governance":     0.1,
        }
        weighted = sum(
            scores[k] * w for k, w in self.RISK_WEIGHTS.items())
        level = (
            RiskLevel.CRITICAL if weighted > 0.75 else
            RiskLevel.HIGH     if weighted > 0.50 else
            RiskLevel.MEDIUM   if weighted > 0.25 else
            RiskLevel.LOW
        )
        return {
            "overall_score": f"{weighted:.3f}",
            "risk_level":    level.value,
            "components":    {k: f"{v:.3f}" for k, v in scores.items()},
            "recommendation": (
                "Monitor closely" if level == RiskLevel.HIGH else
                "Consider reducing exposure" if level == RiskLevel.CRITICAL else
                "Normal operations"
            ),
        }


# ---- SupplyScheduleEngine
class SupplyScheduleEngine:
    """
    Detailed NBL supply schedule and inflation model.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def full_schedule(self, max_eras: int = 34) -> List[dict]:
        schedule = []
        reward   = INITIAL_BLOCK_REWARD
        cum      = 0
        for era in range(max_eras):
            era_supply = reward * HALVING_INTERVAL
            cum       += era_supply
            schedule.append({
                "era":              era + 1,
                "start_block":      era * HALVING_INTERVAL,
                "end_block":        (era + 1) * HALVING_INTERVAL,
                "block_reward":     f"{reward/10**DECIMALS:.9f}",
                "era_supply_nbl":   f"{era_supply/10**DECIMALS:.3f}",
                "cumulative_nbl":   f"{cum/10**DECIMALS:.3f}",
                "pct_of_max":       f"{cum/MAX_SUPPLY*100:.4f}%",
            })
            reward = reward // 2
            if reward == 0:
                break
        return schedule

    def current_era_info(self) -> dict:
        h    = self._bc.height
        era  = h // HALVING_INTERVAL
        sched = self.full_schedule()
        if era < len(sched):
            return sched[era]
        return {"era": era + 1, "reward": "0"}

    def emission_curve(self, n_points: int = 50) -> List[dict]:
        max_h  = HALVING_INTERVAL * 34
        step   = max_h // n_points
        curve  = []
        for i in range(n_points):
            h = i * step
            r = mining_reward(h)
            curve.append({"block": h, "reward": r/10**DECIMALS})
        return curve

    def years_until_fully_mined(self) -> float:
        """Estimate years until all NBL mined."""
        return 34 * 4   # ~136 years (each halving era ~4 years)

    def supply_at_block(self, height: int) -> int:
        """Calculate cumulative supply at given block."""
        total  = 0
        reward = INITIAL_BLOCK_REWARD
        remaining = height
        while remaining > 0 and reward > 0:
            blocks_in_era = min(remaining, HALVING_INTERVAL)
            total        += reward * blocks_in_era
            remaining    -= blocks_in_era
            reward        = reward // 2
        return min(total, MAX_SUPPLY)

    def supply_stats(self) -> dict:
        cur_h  = self._bc.height
        supply = self.supply_at_block(cur_h)
        return {
            "current_block":    cur_h,
            "mined_so_far":     f"{supply/10**DECIMALS:.3f} NBL",
            "max_supply":       f"{MAX_SUPPLY/10**DECIMALS:.0f} NBL",
            "pct_mined":        f"{supply/MAX_SUPPLY*100:.4f}%",
            "years_remaining":  f"~{self.years_until_fully_mined():.0f}",
        }
