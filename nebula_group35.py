"""NEBULA group35 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. CircuitBreaker  (orig. lines 58849-58935)
   2. EmergencyMultiSig  (orig. lines 58938-59004)
   3. DynamicFeeModel  (orig. lines 59014-59079)
   4. PriorityFeeAuction  (orig. lines 59082-59123)
   5. ConsensusRuleEngine  (orig. lines 59130-59212)
   6. WalletConnectBridge  (orig. lines 59219-59281)
   7. IPFSClient  (orig. lines 59292-59585)
   8. OnChainMetadata  (orig. lines 59588-59629)
   9. ExtendedTestSuite  (orig. lines 59636-60122)
  10. KeyBlinding  (orig. lines 60133-60151)
  11. NetworkStatsCollector  (orig. lines 60595-60663)
  12. ChainParametersRegistry  (orig. lines 60741-60811)
  13. ForkChoiceRule  (orig. lines 60818-60867)
  14. ChainArchiver  (orig. lines 60955-61018)
  15. MetricsCollector  (orig. lines 61025-61099)
  16. SubscriptionManager  (orig. lines 61111-61189)
  17. EscrowStatus  (orig. lines 61196-61202)
  18. Escrow  (orig. lines 61204-61228)
  19. SmartEscrowEngine  (orig. lines 61230-61327)
  20. Post  (orig. lines 61334-61354)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BridgeEngine, C, DIDRegistry, DecentralizedOracle, GovernanceEngine, LendingProtocol, NBL721Registry, NEBULABlockchain, NEBULADex, NEBULASmartContractVM, PedersenCommitment, PredictionMarket, ProposalType, RangeProof, Script, Secp256k1, ShamirSecretSharing, StakingEngine, Subscription, VRF, WalletConnectSession, WalletConnectSessionC
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

MAX_SUPPLY          = 21_000_000 * (10 ** DECIMALS)   # in Neb  (matches 50 NBL * 210,000 blocks * 2 geometric series)

FOUNDATION_RATE        = 0.02          # 2% per block to foundation

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

DIFFICULTY_WINDOW      = 2016                           # blocks per retarget

MAX_BLOCK_SIZE_BYTES   = 1_048_576                      # 1 MB

MAX_TX_PER_BLOCK       = 3000

COINBASE_MATURITY      = 100                            # blocks before coinbase spendable

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

DUST_THRESHOLD         = 546                            # min output amount in Neb

PROTOCOL_VERSION       = 70015

MAX_PEERS              = 125

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

log = logging.getLogger("nebula.api")

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


# ---- CircuitBreaker
class CircuitBreaker:
    """
    Emergency circuit breaker for NEBULA protocol.
    Can pause specific components if anomaly detected.
    Requires multi-sig to activate/deactivate.
    """

    class State(_enum.Enum):
        OPEN    = "open"      # normal operation
        TRIPPED = "tripped"   # partially halted
        CLOSED  = "closed"    # fully halted

    TRIP_THRESHOLD  = 3   # consecutive anomalies before tripping
    COOLDOWN_BLOCKS = 144  # ~1 day before auto-reset

    def __init__(self):
        self._components: Dict[str, dict] = {}
        self._anomaly_count: Dict[str, int] = {}
        self._lock = threading.RLock()
        self._register_defaults()

    def _register_defaults(self):
        for comp in ["bridge", "dex", "lending", "staking",
                     "withdrawals", "deposits", "governance"]:
            self._components[comp] = {
                "state":    self.State.OPEN.value,
                "trips":    0,
                "last_trip": 0.0,
                "reason":   "",
            }
            self._anomaly_count[comp] = 0

    def record_anomaly(self, component: str, reason: str):
        """Record an anomaly. Trip breaker if threshold reached."""
        with self._lock:
            if component not in self._anomaly_count:
                self._anomaly_count[component] = 0
            self._anomaly_count[component] += 1
            if self._anomaly_count[component] >= self.TRIP_THRESHOLD:
                self._trip(component, reason)

    def _trip(self, component: str, reason: str):
        c = self._components.get(component)
        if c:
            c["state"]    = self.State.TRIPPED.value
            c["trips"]   += 1
            c["last_trip"] = time.time()
            c["reason"]   = reason
            self._anomaly_count[component] = 0

    def reset(self, component: str, admin: str) -> Tuple[bool, str]:
        """Reset a tripped circuit breaker (admin action)."""
        with self._lock:
            c = self._components.get(component)
            if not c:
                return False, "Component not found"
            c["state"]  = self.State.OPEN.value
            c["reason"] = ""
            return True, f"Circuit breaker reset for {component} by {admin}"

    def emergency_pause(self, components: List[str],
                         reason: str,
                         admin: str) -> List[str]:
        """Emergency pause multiple components."""
        paused = []
        with self._lock:
            for comp in components:
                if comp in self._components:
                    self._components[comp]["state"]  = self.State.CLOSED.value
                    self._components[comp]["reason"] = reason
                    paused.append(comp)
        return paused

    def is_paused(self, component: str) -> bool:
        c = self._components.get(component)
        return c and c["state"] != self.State.OPEN.value

    def status(self) -> dict:
        with self._lock:
            return {
                comp: {
                    "state":  c["state"],
                    "trips":  c["trips"],
                    "reason": c["reason"],
                }
                for comp, c in self._components.items()
            }


# ---- EmergencyMultiSig
class EmergencyMultiSig:
    """
    Emergency multi-sig for critical protocol actions.
    Requires M-of-N guardian signatures for execution.
    """

    def __init__(self, guardians: List[str], required: int):
        self.guardians = guardians
        self.required  = required
        self._pending: Dict[str, dict] = {}
        self._lock     = threading.RLock()

    def propose_emergency(self, proposer: str,
                           action: str,
                           params: dict) -> Tuple[bool, str]:
        with self._lock:
            if proposer not in self.guardians:
                return False, "Not a guardian"
            eid = hashlib.sha256(
                f"EMRG:{action}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._pending[eid] = {
                "action":     action,
                "params":     params,
                "proposer":   proposer,
                "signatures": {proposer},
                "created_at": time.time(),
                "executed":   False,
            }
            return True, eid

    def sign(self, guardian: str, proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            p = self._pending.get(proposal_id)
            if not p:
                return False, "Not found"
            if guardian not in self.guardians:
                return False, "Not a guardian"
            p["signatures"].add(guardian)
            if len(p["signatures"]) >= self.required:
                return True, f"THRESHOLD_MET — ready to execute"
            return True, f"Signed ({len(p['signatures'])}/{self.required})"

    def execute(self, proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            p = self._pending.get(proposal_id)
            if not p:
                return False, "Not found"
            if p["executed"]:
                return False, "Already executed"
            if len(p["signatures"]) < self.required:
                return False, f"Need {self.required} sigs, have {len(p['signatures'])}"
            p["executed"] = True
            return True, f"Emergency action '{p['action']}' executed"

    def active_proposals(self) -> List[dict]:
        return [
            {
                "id":       eid,
                "action":   p["action"],
                "sigs":     len(p["signatures"]),
                "required": self.required,
                "executed": p["executed"],
            }
            for eid, p in self._pending.items()
            if not p["executed"]
        ]


# ---- DynamicFeeModel
class DynamicFeeModel:
    """
    EIP-1559 style fee model for NEBULA.
    Base fee adjusts automatically based on block fullness.
    """

    TARGET_BLOCK_UTIL = 0.50     # 50% target utilization
    MAX_BASE_FEE_CHANGE = 0.125  # 12.5% per block max change
    INITIAL_BASE_FEE    = MIN_TX_FEE * 10

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._base_fee  = self.INITIAL_BASE_FEE
        self._fee_history: List[int] = []
        self._lock      = threading.RLock()

    def update_base_fee(self, block: 'Block') -> int:
        """Update base fee after each block."""
        with self._lock:
            block_size   = block.byte_size()
            target_size  = MAX_BLOCK_SIZE_BYTES * self.TARGET_BLOCK_UTIL
            util         = block_size / MAX_BLOCK_SIZE_BYTES

            if util > self.TARGET_BLOCK_UTIL:
                # Increase fee
                delta = self._base_fee * self.MAX_BASE_FEE_CHANGE * \
                        (util - self.TARGET_BLOCK_UTIL) / self.TARGET_BLOCK_UTIL
                self._base_fee = int(self._base_fee + delta)
            else:
                # Decrease fee
                delta = self._base_fee * self.MAX_BASE_FEE_CHANGE * \
                        (self.TARGET_BLOCK_UTIL - util) / self.TARGET_BLOCK_UTIL
                self._base_fee = max(MIN_TX_FEE,
                                     int(self._base_fee - delta))

            self._fee_history.append(self._base_fee)
            if len(self._fee_history) > 2016:
                self._fee_history.pop(0)
            return self._base_fee

    def current_base_fee(self) -> int:
        return self._base_fee

    def suggested_fee(self, priority: str = "normal") -> int:
        bf = self._base_fee
        tips = {"slow": 0, "normal": MIN_TX_FEE, "fast": MIN_TX_FEE * 3}
        return bf + tips.get(priority, MIN_TX_FEE)

    def fee_history_percentiles(self) -> dict:
        if not self._fee_history:
            return {}
        h = sorted(self._fee_history)
        n = len(h)
        return {
            "min":  h[0],
            "p25":  h[n//4],
            "p50":  h[n//2],
            "p75":  h[3*n//4],
            "max":  h[-1],
            "current": self._base_fee,
        }

    def burn_estimate(self, block: 'Block') -> int:
        """In EIP-1559, base fee is burned. Estimate NBL burned."""
        tx_count = len(block.transactions)
        return self._base_fee * tx_count * 200  # ~200 bytes avg tx


# ---- PriorityFeeAuction
class PriorityFeeAuction:
    """
    First-price sealed-bid auction for block space.
    Miners include highest-fee transactions first.
    """

    def __init__(self, mempool: 'Mempool',
                 base_fee_model: DynamicFeeModel):
        self._mp  = mempool
        self._bfm = base_fee_model

    def rank_transactions(self) -> List[Tuple[str, int, int]]:
        """
        Rank txs by effective fee rate (fee - base_fee).
        Returns [(txid, fee_rate, priority_fee)].
        """
        base_fee = self._bfm.current_base_fee()
        ranked   = []
        for txid, tx in self._mp._txs.items():
            fee       = tx.fee(self._mp._utxo)
            size      = max(1, tx.byte_size())
            fee_rate  = fee // size
            priority  = max(0, fee_rate - base_fee)
            ranked.append((txid, fee_rate, priority))
        ranked.sort(key=lambda x: x[2], reverse=True)
        return ranked

    def optimal_block(self, max_bytes: int = MAX_BLOCK_SIZE_BYTES) -> List[str]:
        """Select optimal set of transactions for a block."""
        ranked = self.rank_transactions()
        total  = 0
        result = []
        for txid, _, priority in ranked:
            tx = self._mp._txs.get(txid)
            if not tx:
                continue
            sz = tx.byte_size()
            if total + sz > max_bytes:
                continue
            result.append(txid)
            total += sz
        return result


# ---- ConsensusRuleEngine
class ConsensusRuleEngine:
    """
    Pluggable consensus rule engine for NEBULA.
    Validates blocks against all active consensus rules.
    Rules can be added/removed via governance.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._rules: List[dict] = []
        self._load_default_rules()

    def _load_default_rules(self):
        self._rules = [
            {"name": "max_block_size",    "active": True, "priority": 1},
            {"name": "min_difficulty",    "active": True, "priority": 2},
            {"name": "timestamp_range",   "active": True, "priority": 3},
            {"name": "coinbase_maturity", "active": True, "priority": 4},
            {"name": "double_spend",      "active": True, "priority": 5},
            {"name": "merkle_root",       "active": True, "priority": 6},
            {"name": "script_validity",   "active": True, "priority": 7},
            {"name": "dust_threshold",    "active": True, "priority": 8},
            {"name": "max_tx_count",      "active": True, "priority": 9},
            {"name": "coinbase_reward",   "active": True, "priority": 10},
        ]

    def validate(self, block: 'Block') -> Tuple[bool, List[str]]:
        """Run all active consensus rules against a block."""
        errors = []
        active = sorted([r for r in self._rules if r["active"]],
                        key=lambda r: r["priority"])
        for rule in active:
            ok, err = self._apply_rule(rule["name"], block)
            if not ok:
                errors.append(f"[{rule['name']}] {err}")
        return len(errors) == 0, errors

    def _apply_rule(self, rule_name: str,
                     block: 'Block') -> Tuple[bool, str]:
        if rule_name == "max_block_size":
            sz = block.byte_size()
            if sz > MAX_BLOCK_SIZE_BYTES:
                return False, f"Block too large: {sz} > {MAX_BLOCK_SIZE_BYTES}"
        elif rule_name == "max_tx_count":
            n = len(block.transactions)
            if n > MAX_TX_PER_BLOCK:
                return False, f"Too many txs: {n}"
        elif rule_name == "merkle_root":
            if not block.verify_merkle():
                return False, "Merkle root mismatch"
        elif rule_name == "min_difficulty":
            if not block.header.meets_target():
                return False, "Insufficient PoW"
        elif rule_name == "timestamp_range":
            now = int(time.time())
            if block.header.timestamp > now + 7200:
                return False, "Timestamp too far in future"
        elif rule_name == "dust_threshold":
            for tx in block.transactions:
                for out in tx.outputs:
                    if out.value < DUST_THRESHOLD:
                        return False, f"Output below dust: {out.value}"
        return True, "OK"

    def add_rule(self, name: str, priority: int = 100) -> bool:
        if any(r["name"] == name for r in self._rules):
            return False
        self._rules.append({"name": name, "active": True, "priority": priority})
        return True

    def disable_rule(self, name: str) -> bool:
        for r in self._rules:
            if r["name"] == name:
                r["active"] = False
                return True
        return False

    def rules_summary(self) -> dict:
        return {
            "total_rules":  len(self._rules),
            "active_rules": sum(1 for r in self._rules if r["active"]),
            "rules":        self._rules,
        }


# ---- WalletConnectBridge
class WalletConnectBridge:
    """
    WalletConnect bridge for NEBULA.
    Allows dApps to connect to NBL wallets via QR code.
    """

    def __init__(self):
        self._sessions: Dict[str, WalletConnectSession] = {}
        self._lock = threading.RLock()

    def create_session(self, dapp_name: str,
                        dapp_url: str,
                        wallet_address: str) -> Tuple[str, str]:
        """Create session. Returns (session_id, qr_uri)."""
        with self._lock:
            sid = secrets.token_hex(16)
            session = WalletConnectSessionC(
                session_id     = sid,
                dapp_name      = dapp_name,
                dapp_url       = dapp_url,
                wallet_address = wallet_address,
            )
            self._sessions[sid] = session
            qr_uri = f"nbl:wc:{sid}@1?bridge=wss://bridge.nebula-nbl.io&key={secrets.token_hex(16)}"
            return sid, qr_uri

    def approve_request(self, session_id: str,
                         request_id: str,
                         result: Any) -> Tuple[bool, str]:
        with self._lock:
            session = self._sessions.get(session_id)
            if not session or not session.active:
                return False, "Session not found"
            session.pending_requests = [
                r for r in session.pending_requests
                if r.get("id") != request_id
            ]
            session.last_activity = time.time()
            return True, "Request approved"

    def reject_request(self, session_id: str,
                        request_id: str) -> Tuple[bool, str]:
        with self._lock:
            session = self._sessions.get(session_id)
            if not session:
                return False, "Not found"
            session.pending_requests = [
                r for r in session.pending_requests
                if r.get("id") != request_id
            ]
            return True, "Rejected"

    def disconnect(self, session_id: str) -> bool:
        with self._lock:
            session = self._sessions.get(session_id)
            if session:
                session.active = False
                return True
            return False

    def active_sessions(self) -> List[dict]:
        return [s.to_dict() for s in self._sessions.values()
                if s.active]


# ---- IPFSClient
class IPFSClient:
    """
    NEBULA IPFS integration for off-chain data storage.
    Store large data off-chain; put content hash on-chain.

    Strategy (in order):
      1. Local IPFS daemon  — http://localhost:5001/api/v0/add
      2. Pinata cloud API   — requires PINATA_JWT env var
      3. web3.storage API   — requires WEB3_STORAGE_TOKEN env var
      If all three unavailable, raises RuntimeError (no silent fakes).
    """

    IPFS_GATEWAYS = [
        "https://ipfs.io/ipfs/",
        "https://cloudflare-ipfs.com/ipfs/",
        "https://gateway.pinata.cloud/ipfs/",
    ]

    _PINATA_UPLOAD   = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    _PINATA_UNPIN    = "https://api.pinata.cloud/pinning/unpin/{cid}"
    _PINATA_LIST     = "https://api.pinata.cloud/data/pinList?status=pinned"
    _W3S_UPLOAD      = "https://api.web3.storage/upload"

    def __init__(self, api_url: str = "http://localhost:5001"):
        import os
        self.api_url          = api_url.rstrip("/")
        self._pinned:  Dict[str, dict] = {}
        self._pinata_jwt      = os.environ.get("PINATA_JWT", "")
        self._w3s_token       = os.environ.get("WEB3_STORAGE_TOKEN", "")
        self._local_available : Optional[bool] = None   # checked lazily

    # ── internal helpers ──────────────────────────────────────────

    def _check_local(self) -> bool:
        """Return True if local IPFS daemon responds."""
        if self._local_available is not None:
            return self._local_available
        import urllib.request
        try:
            urllib.request.urlopen(
                f"{self.api_url}/api/v0/id", timeout=2
            )
            self._local_available = True
        except Exception:
            self._local_available = False
        return self._local_available

    def _add_local(self, data: bytes, name: str) -> str:
        """Upload to local IPFS daemon via multipart/form-data."""
        import urllib.request
        boundary = "----NEBULAIPFSBoundary" + secrets.token_hex(8)
        ctype    = f"multipart/form-data; boundary={boundary}"
        fname    = name.encode() or b"nebula_data"
        body = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{name or "nebula_data"}"\r\n'
            f"Content-Type: application/octet-stream\r\n\r\n"
        ).encode() + data + f"\r\n--{boundary}--\r\n".encode()

        req = urllib.request.Request(
            f"{self.api_url}/api/v0/add?pin=true",
            data=body,
            headers={"Content-Type": ctype},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
        cid = result["Hash"]
        return cid

    def _add_pinata(self, data: bytes, name: str) -> str:
        """Upload to Pinata cloud pinning service."""
        import urllib.request
        boundary = "----NEBULAPinataBoundary" + secrets.token_hex(8)
        ctype    = f"multipart/form-data; boundary={boundary}"
        body = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{name or "nebula_data"}"\r\n'
            f"Content-Type: application/octet-stream\r\n\r\n"
        ).encode() + data + f"\r\n--{boundary}--\r\n".encode()

        req = urllib.request.Request(
            self._PINATA_UPLOAD,
            data=body,
            headers={
                "Content-Type": ctype,
                "Authorization": f"Bearer {self._pinata_jwt}",
            },
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
        return result["IpfsHash"]

    def _add_w3s(self, data: bytes, name: str) -> str:
        """Upload to web3.storage."""
        import urllib.request
        req = urllib.request.Request(
            self._W3S_UPLOAD,
            data=data,
            headers={
                "Authorization": f"Bearer {self._w3s_token}",
                "X-NAME": name or "nebula_data",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
        return result["cid"]

    # ── public API ────────────────────────────────────────────────

    def add(self, data: bytes, name: str = "") -> str:
        """
        Upload data to IPFS. Tries local daemon → Pinata → web3.storage.
        Returns a real CID that is resolvable via any IPFS gateway.
        Raises RuntimeError if no backend is available.
        """
        last_err = None

        # 1. Local daemon
        if self._check_local():
            try:
                cid = self._add_local(data, name)
                self._pinned[cid] = {
                    "name": name, "size": len(data),
                    "cid": cid, "added_at": time.time(),
                    "backend": "local",
                }
                log.info(f"IPFS add via local daemon: {cid}")
                return cid
            except Exception as e:
                last_err = e
                log.warning(f"IPFS local add failed: {e}")

        # 2. Pinata
        if self._pinata_jwt:
            try:
                cid = self._add_pinata(data, name)
                self._pinned[cid] = {
                    "name": name, "size": len(data),
                    "cid": cid, "added_at": time.time(),
                    "backend": "pinata",
                }
                log.info(f"IPFS add via Pinata: {cid}")
                return cid
            except Exception as e:
                last_err = e
                log.warning(f"IPFS Pinata add failed: {e}")

        # 3. web3.storage
        if self._w3s_token:
            try:
                cid = self._add_w3s(data, name)
                self._pinned[cid] = {
                    "name": name, "size": len(data),
                    "cid": cid, "added_at": time.time(),
                    "backend": "web3.storage",
                }
                log.info(f"IPFS add via web3.storage: {cid}")
                return cid
            except Exception as e:
                last_err = e
                log.warning(f"IPFS web3.storage add failed: {e}")

        raise RuntimeError(
            "IPFS upload failed — no backend available. "
            "Run a local IPFS daemon, or set PINATA_JWT / WEB3_STORAGE_TOKEN. "
            f"Last error: {last_err}"
        )

    def add_json(self, obj: dict, name: str = "") -> str:
        """Add JSON object to IPFS."""
        data = json.dumps(obj, separators=(',', ':')).encode()
        return self.add(data, name)

    def get(self, cid: str) -> Optional[bytes]:
        """
        Retrieve data by CID.
        Tries local daemon first, then public gateways.
        """
        import urllib.request

        # 1. Local daemon cat
        if self._check_local():
            try:
                url = f"{self.api_url}/api/v0/cat?arg={cid}"
                req = urllib.request.Request(url, method="POST")
                with urllib.request.urlopen(req, timeout=10) as resp:
                    return resp.read()
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in IPFSClient.get", exc_info=True)

        # 2. Public gateways
        for gateway in self.IPFS_GATEWAYS:
            try:
                with urllib.request.urlopen(
                    gateway + cid, timeout=15
                ) as resp:
                    return resp.read()
            except Exception:
                continue
        return None

    def get_json(self, cid: str) -> Optional[dict]:
        data = self.get(cid)
        if data:
            try:
                return json.loads(data)
            except Exception:
                return None
        return None

    def pin(self, cid: str) -> bool:
        """Pin a CID on local daemon."""
        import urllib.request
        if self._check_local():
            try:
                req = urllib.request.Request(
                    f"{self.api_url}/api/v0/pin/add?arg={cid}", method="POST"
                )
                urllib.request.urlopen(req, timeout=30)
                self._pinned.setdefault(cid, {"cid": cid})["pinned"] = True
                return True
            except Exception as e:
                log.warning(f"IPFS pin failed: {e}")
        if cid in self._pinned:
            self._pinned[cid]["pinned"] = True
            return True
        return False

    def unpin(self, cid: str) -> bool:
        """Unpin a CID from local daemon."""
        import urllib.request
        if self._check_local():
            try:
                req = urllib.request.Request(
                    f"{self.api_url}/api/v0/pin/rm?arg={cid}", method="POST"
                )
                urllib.request.urlopen(req, timeout=10)
                if cid in self._pinned:
                    self._pinned[cid]["pinned"] = False
                return True
            except Exception as e:
                log.warning(f"IPFS unpin failed: {e}")
        if cid in self._pinned:
            self._pinned[cid]["pinned"] = False
        return False

    def gateway_url(self, cid: str, gateway_idx: int = 0) -> str:
        return self.IPFS_GATEWAYS[gateway_idx % len(self.IPFS_GATEWAYS)] + cid

    def pinned_list(self) -> List[dict]:
        """List pinned CIDs from local daemon or local cache."""
        import urllib.request
        if self._check_local():
            try:
                req = urllib.request.Request(
                    f"{self.api_url}/api/v0/pin/ls?type=recursive",
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=10) as resp:
                    result = json.loads(resp.read())
                return [
                    {"cid": cid, "type": info.get("Type", "recursive")}
                    for cid, info in result.get("Keys", {}).items()
                ]
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in IPFSClient.pinned_list", exc_info=True)
        return [v for v in self._pinned.values() if v.get("pinned", True)]

    def storage_stats(self) -> dict:
        """Repo stats from local daemon or cached counts."""
        import urllib.request
        if self._check_local():
            try:
                req = urllib.request.Request(
                    f"{self.api_url}/api/v0/repo/stat", method="POST"
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    s = json.loads(resp.read())
                return {
                    "backend":       "local",
                    "repo_size_kb":  f"{s.get('RepoSize',0)/1024:.1f}",
                    "num_objects":   s.get("NumObjects", 0),
                    "pinned_local":  len(self._pinned),
                    "gateways":      len(self.IPFS_GATEWAYS),
                }
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in IPFSClient.storage_stats", exc_info=True)
        return {
            "backend":      "none" if not (self._pinata_jwt or self._w3s_token) else
                             "pinata" if self._pinata_jwt else "web3.storage",
            "pinned_cache": len(self._pinned),
            "gateways":     len(self.IPFS_GATEWAYS),
        }


# ---- OnChainMetadata
class OnChainMetadata:
    """
    Manages on-chain metadata pointers to IPFS content.
    Stores IPFS CIDs on-chain; actual data lives on IPFS.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  ipfs: IPFSClient):
        self._bc    = blockchain
        self._ipfs  = ipfs
        self._index: Dict[str, dict] = {}   # key -> {cid, block, type}
        self._lock  = threading.RLock()

    def store(self, key: str, data: dict,
               data_type: str = "json") -> str:
        """Store data on IPFS and record CID on-chain."""
        with self._lock:
            cid = self._ipfs.add_json(data)
            self._index[key] = {
                "cid":    cid,
                "block":  self._bc.height,
                "type":   data_type,
                "key":    key,
            }
            return cid

    def retrieve(self, key: str) -> Optional[dict]:
        """Retrieve data by key."""
        entry = self._index.get(key)
        if not entry:
            return None
        return self._ipfs.get_json(entry["cid"])

    def lookup_cid(self, key: str) -> Optional[str]:
        entry = self._index.get(key)
        return entry["cid"] if entry else None

    def metadata_stats(self) -> dict:
        return {
            "total_entries": len(self._index),
            "ipfs_stats":    self._ipfs.storage_stats(),
        }


# ---- ExtendedTestSuite
class ExtendedTestSuite:
    """
    Extended automated test suite for NEBULA v2 modules.
    Tests all new DeFi, identity, and governance modules.
    """

    def __init__(self):
        self.results: List[dict] = []
        self.passed  = 0
        self.failed  = 0

    def _ok(self, name: str, msg: str = ""):
        self.results.append({"name": name, "status": "PASS", "msg": msg})
        self.passed += 1
        print(f"  ✅ {name}" + (f" — {msg}" if msg else ""))

    def _fail(self, name: str, err: str):
        self.results.append({"name": name, "status": "FAIL", "msg": err})
        self.failed += 1
        print(f"  ❌ {name}: {err}")

    def test_governance(self):
        print("\n🗳️  Governance Tests")
        try:
            bc   = NEBULABlockchain()
            gov  = GovernanceEngine(bc)
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 10_000)
            ok, pid = gov.propose(
                FOUNDATION_ADDRESS,
                ProposalType.TEXT,
                "Test Proposal",
                "A test governance proposal",
                {"text": "hello"}
            )
            assert ok, f"Propose failed: {pid}"
            self._ok("Governance propose", f"pid={pid}")

            ok2, msg2 = gov.cast_vote(FOUNDATION_ADDRESS, pid, "yes")
            assert ok2, f"Vote failed: {msg2}"
            self._ok("Governance vote", msg2)

            info = gov.get_proposal(pid)
            assert info is not None
            self._ok("Governance proposal info")

            stats = gov.governance_stats()
            assert stats["total_proposals"] >= 1
            self._ok("Governance stats", f"{stats['total_proposals']} proposals")
        except Exception as e:
            self._fail("Governance", str(e))

    def test_staking(self):
        print("\n💎 Staking Tests")
        try:
            bc     = NEBULABlockchain()
            stk    = StakingEngine(bc)
            addr   = FOUNDATION_ADDRESS
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(addr, 5_000)

            ok, msg = stk.stake(addr, 1_000 * 10**DECIMALS)
            assert ok, f"Stake failed: {msg}"
            self._ok("Stake NBL", msg)

            info = stk.get_stake(addr)
            assert "1000" in info["total_staked"]
            self._ok("Stake balance check")

            stats = stk.staking_stats()
            assert stats["total_staked_nbl"] != "0.000"
            self._ok("Staking stats", stats["staked_pct"])

            apy = stk.apy_estimate(1_000 * 10**DECIMALS)
            self._ok("APY estimate", apy["effective_apy"])
        except Exception as e:
            self._fail("Staking", str(e))

    def test_dex(self):
        print("\n📊 DEX Tests")
        try:
            bc  = NEBULABlockchain()
            dex = NEBULADex(bc)

            pid = dex.create_pool("NBL", "USDT", fee_bps=30)
            assert pid
            self._ok("Create AMM pool", pid)

            ok, msg = dex.add_liquidity(
                "liquidity_provider",
                "NBL", "USDT",
                10_000 * 10**DECIMALS,
                10_000 * 10**DECIMALS
            )
            assert ok, msg
            self._ok("Add liquidity", msg)

            ok2, msg2, out = dex.swap_amm(
                "trader", "NBL", "USDT",
                100 * 10**DECIMALS
            )
            assert ok2, msg2
            self._ok("AMM swap", f"got {out} USDT")

            stats = dex.dex_stats()
            assert stats["total_pools"] >= 1
            self._ok("DEX stats")
        except Exception as e:
            self._fail("DEX", str(e))

    def test_nft(self):
        print("\n🖼️  NFT Tests")
        try:
            nft = NBL721Registry()
            cid = nft.create_collection(
                FOUNDATION_ADDRESS, "NEBULA Art", "NART",
                "NEBULA genesis art collection",
                max_supply=1000, royalty_pct=0.05
            )
            assert cid
            self._ok("Create NFT collection", cid[:16])

            tid, msg = nft.mint(cid, FOUNDATION_ADDRESS,
                                "ipfs://Qm...", {"name": "NFT #1"},
                                caller=FOUNDATION_ADDRESS)
            assert tid == 1
            self._ok("Mint NFT", f"token #{tid}")

            owner = nft.owner_of(cid, tid)
            assert owner == FOUNDATION_ADDRESS
            self._ok("NFT owner check")

            ok, msg2 = nft.list_for_sale(
                cid, FOUNDATION_ADDRESS, tid, 100 * 10**DECIMALS)
            assert ok
            self._ok("List NFT for sale")

            stats = nft.nft_stats()
            assert stats["total_tokens"] >= 1
            self._ok("NFT stats", f"{stats['total_tokens']} tokens")
        except Exception as e:
            self._fail("NFT", str(e))

    def test_did(self):
        print("\n🪪  DID Identity Tests")
        try:
            did_reg = DIDRegistry()
            priv, pub = Secp256k1.generate_keypair()
            pub_b     = Secp256k1.pubkey_to_bytes(pub)
            addr      = Script.p2pkh_address(pub_b)

            did = did_reg.create_did(addr, pub_b)
            assert did.startswith("did:nbl:")
            self._ok("Create DID", did[:24])

            doc = did_reg.resolve(did)
            assert doc is not None
            self._ok("Resolve DID")

            issuer_priv, _ = Secp256k1.generate_keypair()
            issuer_pub_b   = Secp256k1.pubkey_to_bytes(
                               Secp256k1.point_mul(issuer_priv, Secp256k1.G()))
            issuer_addr    = Script.p2pkh_address(issuer_pub_b)
            issuer_did     = did_reg.create_did(issuer_addr, issuer_pub_b)

            cred_id = did_reg.issue_credential(
                issuer_did, did,
                "AgeVerification",
                {"age_over_18": True},
                validity_days=365
            )
            assert cred_id
            self._ok("Issue credential", cred_id[:16])

            ok, msg = did_reg.verify_credential(cred_id)
            assert ok, msg
            self._ok("Verify credential", msg)

            stats = did_reg.did_stats()
            assert stats["total_dids"] >= 2
            self._ok("DID stats", f"{stats['total_dids']} DIDs")
        except Exception as e:
            self._fail("DID", str(e))

    def test_lending(self):
        print("\n🏦 Lending Tests")
        try:
            bc      = NEBULABlockchain()
            oracle  = DecentralizedOracle()
            lending = LendingProtocol(oracle)

            lending.create_pool("NBL")
            ok, msg = lending.supply(
                FOUNDATION_ADDRESS, "NBL", 10_000 * 10**DECIMALS)
            assert ok, msg
            self._ok("Supply to lending pool", msg)

            ok2, msg2 = lending.borrow(
                "borrower", "NBL", 5_000 * 10**DECIMALS,
                "NBL", 3_000 * 10**DECIMALS
            )
            assert ok2, msg2
            self._ok("Borrow from pool", msg2)

            stats = lending.protocol_stats()
            assert stats["total_positions"] >= 1
            self._ok("Lending stats")
        except Exception as e:
            self._fail("Lending", str(e))

    def test_bridge(self):
        print("\n🌉 Bridge Tests")
        try:
            bc     = NEBULABlockchain()
            bridge = BridgeEngine(bc)

            cid = bridge.register_wrapped(
                "ethereum", "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                "wUSDT", "Wrapped USDT", 6)
            assert cid
            self._ok("Register wrapped token", cid[:16])

            secret = secrets.token_bytes(32)
            ok, rid = bridge.initiate_bridge_in(
                FOUNDATION_ADDRESS, "ethereum",
                "wUSDT", 1_000 * 10**6,
                FOUNDATION_ADDRESS, secret
            )
            assert ok, rid
            self._ok("Initiate bridge-in", rid)

            stats = bridge.bridge_stats()
            assert stats["wrapped_assets"] >= 1
            self._ok("Bridge stats", f"{stats['wrapped_assets']} wrapped assets")
        except Exception as e:
            self._fail("Bridge", str(e))

    def test_zk_proofs(self):
        print("\n🔐 ZK Proof Tests")
        try:
            value    = 1_000
            blinding = secrets.randbelow(Secp256k1.N)
            C        = PedersenCommitment.commit(value, blinding)
            assert C is not None
            self._ok("Pedersen commitment")

            # Homomorphic addition
            v1, b1 = 300, secrets.randbelow(Secp256k1.N)
            v2, b2 = 700, secrets.randbelow(Secp256k1.N)
            C1 = PedersenCommitment.commit(v1, b1)
            C2 = PedersenCommitment.commit(v2, b2)
            C_sum = PedersenCommitment.add(C1, C2)
            C_expected = PedersenCommitment.commit(v1+v2, (b1+b2) % Secp256k1.N)
            assert C_sum == C_expected
            self._ok("Homomorphic commitment addition")

            proof = RangeProof.prove(1_000, blinding)
            assert proof["valid"]
            self._ok("Range proof generation")

            ok = RangeProof.verify(proof)
            assert ok
            self._ok("Range proof verification")
        except Exception as e:
            self._fail("ZK Proofs", str(e))

    def test_atomic_swap(self):
        print("\n⚡ Atomic Swap Tests")
        try:
            bc     = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 10_000)
            secret = secrets.token_bytes(32)

            ok, sid = swaps.initiate(
                FOUNDATION_ADDRESS, "counterparty",
                100.0, "ethereum", 0.05, secret
            )
            assert ok, sid
            self._ok("Initiate atomic swap", sid)

            ok2, msg2 = swaps.fund(sid, "counterparty")
            assert ok2, msg2
            self._ok("Fund atomic swap")

            ok3, msg3 = swaps.redeem(sid, secret)
            assert ok3, msg3
            self._ok("Redeem atomic swap", msg3[:40])

            stats = swaps.swap_stats()
            assert stats["total_swaps"] >= 1
            self._ok("Atomic swap stats")
        except Exception as e:
            self._fail("Atomic Swaps", str(e))

    def test_vrf_randomness(self):
        print("\n🎲 VRF Randomness Tests")
        try:
            priv, pub = Secp256k1.generate_keypair()
            pub_b     = Secp256k1.pubkey_to_bytes(pub)
            msg       = b"NEBULA VRF TEST MESSAGE 2025"

            vrf_out, proof = VRF.prove(priv, msg)
            assert len(vrf_out) == 32
            self._ok("VRF prove", vrf_out.hex()[:16])

            ok = VRF.verify(pub_b, msg, vrf_out, proof)
            assert ok
            self._ok("VRF verify")

            # Wrong message should fail
            ok2 = VRF.verify(pub_b, b"wrong message", vrf_out, proof)
            assert not ok2
            self._ok("VRF reject wrong message")

            n = VRF.output_to_int(vrf_out, 100)
            assert 0 <= n < 100
            self._ok("VRF to int", f"random int: {n}")
        except Exception as e:
            self._fail("VRF", str(e))

    def test_prediction_market(self):
        print("\n📈 Prediction Market Tests")
        try:
            bc  = NEBULABlockchain()
            pm  = PredictionMarket(bc)
            mid = pm.create_market(
                FOUNDATION_ADDRESS,
                "Will NEBULA reach 1M users by 2026?",
                "crypto", duration_days=7
            )
            assert mid
            self._ok("Create prediction market", mid)

            ok, msg = pm.buy(
                "trader1", mid, "yes", 1_000 * 10**DECIMALS)
            assert ok, msg
            self._ok("Buy YES shares", msg[:40])

            ok2, msg2 = pm.buy(
                "trader2", mid, "no", 500 * 10**DECIMALS)
            assert ok2, msg2
            self._ok("Buy NO shares")

            ok3, msg3 = pm.resolve(mid, "", True)
            assert ok3, msg3
            self._ok("Resolve market", msg3)

            ok4, payout = pm.claim("trader1", mid)
            assert ok4
            self._ok("Claim winnings", f"{payout/10**DECIMALS:.3f} NBL")
        except Exception as e:
            self._fail("Prediction Markets", str(e))

    def test_circuit_breaker(self):
        print("\n🔴 Circuit Breaker Tests")
        try:
            cb = CircuitBreaker()

            assert not cb.is_paused("bridge")
            self._ok("Circuit breaker initial state")

            for _ in range(3):
                cb.record_anomaly("bridge", "test anomaly")
            assert cb.is_paused("bridge")
            self._ok("Circuit breaker trip on anomaly")

            ok, msg = cb.reset("bridge", FOUNDATION_ADDRESS)
            assert ok
            assert not cb.is_paused("bridge")
            self._ok("Circuit breaker reset")

            paused = cb.emergency_pause(["dex", "lending"], "test", FOUNDATION_ADDRESS)
            assert "dex" in paused and "lending" in paused
            self._ok("Emergency pause", f"paused: {paused}")
        except Exception as e:
            self._fail("Circuit Breaker", str(e))

    def test_shamir_secret(self):
        print("\n🔑 Shamir Secret Sharing Tests")
        try:
            secret  = secrets.randbelow(Secp256k1.N)
            shares  = ShamirSecretSharing.split(secret, 3, 5)
            assert len(shares) == 5
            self._ok("Split secret into 5 shares (3-of-5)")

            rec = ShamirSecretSharing.reconstruct(shares[:3])
            assert rec == secret
            self._ok("Reconstruct from 3 shares")

            rec2 = ShamirSecretSharing.reconstruct(shares[1:4])
            assert rec2 == secret
            self._ok("Reconstruct from different 3 shares")

            rec3 = ShamirSecretSharing.reconstruct(shares[:2])
            assert rec3 != secret
            self._ok("Cannot reconstruct from 2 shares (correct)")
        except Exception as e:
            self._fail("Shamir Secret Sharing", str(e))

    def test_vm(self):
        print("\n🖥️  Smart Contract VM Tests")
        try:
            vm = NEBULASmartContractVM(gas_limit=2_000_000)

            # Test: 10 + 32 = 42
            bytecode = [
                ("PUSH", 10),
                ("PUSH", 32),
                ("ADD", None),
                ("RETURN", None),
            ]
            result = vm.execute_bytecode(bytecode, {})
            assert result == 42, f"Expected 42, got {result}"
            self._ok("VM arithmetic (10+32=42)")

            # Test: storage
            vm2 = NEBULASmartContractVM(gas_limit=2_000_000)
            bc2 = [
                ("PUSH", "my_key"),
                ("PUSH", 999),
                ("MSTORE", None),
                ("PUSH", "my_key"),
                ("MLOAD", None),
                ("RETURN", None),
            ]
            r2 = vm2.execute_bytecode(bc2, {})
            assert r2 == 999
            self._ok("VM memory store/load")

            # Test: event emit
            vm3 = NEBULASmartContractVM(gas_limit=2_000_000)
            bc3 = [
                ("PUSH", "Transfer"),
                ("PUSH", {"amount": 100}),
                ("LOG", None),
                ("PUSH", 1),
                ("RETURN", None),
            ]
            r3 = vm3.execute_bytecode(bc3, {})
            assert len(vm3.events) == 1
            self._ok("VM event emit")

            report = vm.gas_report()
            self._ok("VM gas report", f"used={report['gas_used']}")
        except Exception as e:
            self._fail("Smart Contract VM", str(e))

    def run_all(self) -> dict:
        print("\n" + "═"*55)
        print("  🧪 NEBULA v2 EXTENDED TEST SUITE")
        print("═"*55)
        start = time.time()

        self.test_governance()
        self.test_staking()
        self.test_dex()
        self.test_nft()
        self.test_did()
        self.test_lending()
        self.test_bridge()
        self.test_zk_proofs()
        self.test_atomic_swap()
        self.test_vrf_randomness()
        self.test_prediction_market()
        self.test_circuit_breaker()
        self.test_shamir_secret()
        self.test_vm()

        elapsed = time.time() - start
        total   = self.passed + self.failed
        pct     = self.passed / total * 100 if total > 0 else 0

        print(f"\n{'═'*55}")
        print(f"  Results: {self.passed}/{total} passed ({pct:.0f}%)")
        print(f"  Time: {elapsed:.2f}s")
        if self.failed > 0:
            print(f"  Failed: {self.failed}")
        print(f"{'═'*55}\n")

        return {
            "passed":  self.passed,
            "failed":  self.failed,
            "total":   total,
            "pct":     f"{pct:.1f}%",
            "elapsed": f"{elapsed:.2f}s",
        }


# ---- KeyBlinding
class KeyBlinding:
    """Key blinding for privacy-preserving protocols."""

    @staticmethod
    def tweak_privkey(privkey: int, tweak: bytes) -> int:
        t = int.from_bytes(hashlib.sha256(tweak).digest(), 'big') % Secp256k1.N
        return (privkey + t) % Secp256k1.N

    @staticmethod
    def tweak_pubkey(pubkey: Tuple[int,int], tweak: bytes) -> Tuple[int,int]:
        t  = int.from_bytes(hashlib.sha256(tweak).digest(), 'big') % Secp256k1.N
        tG = Secp256k1.point_mul(t, Secp256k1.G())
        return Secp256k1.point_add(pubkey, tG)

    @staticmethod
    def generate_one_time_key() -> Tuple[int, bytes, str]:
        priv = secrets.randbelow(Secp256k1.N - 1) + 1
        pub  = Secp256k1.pubkey_to_bytes(Secp256k1.point_mul(priv, Secp256k1.G()))
        return priv, pub, Script.p2pkh_address(pub)


# ---- NetworkStatsCollector
class NetworkStatsCollector:
    """
    Collects and analyzes NEBULA network statistics.
    Tracks peer behavior, message rates, bandwidth usage.
    """

    def __init__(self):
        self._peer_stats:  Dict[str, dict] = {}
        self._msg_counts:  Dict[str, int]  = {}
        self._bandwidth:   Dict[str, int]  = {}
        self._start_time   = time.time()
        self._lock         = threading.RLock()

    def record_message(self, peer: str, msg_type: str,
                        size_bytes: int, direction: str = 'recv'):
        with self._lock:
            if peer not in self._peer_stats:
                self._peer_stats[peer] = {
                    'bytes_recv': 0, 'bytes_sent': 0,
                    'msgs_recv': 0, 'msgs_sent': 0,
                    'first_seen': time.time(), 'last_seen': time.time(),
                }
            p = self._peer_stats[peer]
            p[f'bytes_{direction}'] += size_bytes
            p[f'msgs_{direction}']  += 1
            p['last_seen']           = time.time()
            self._msg_counts[msg_type] = self._msg_counts.get(msg_type, 0) + 1
            self._bandwidth[direction] = (
                self._bandwidth.get(direction, 0) + size_bytes)

    def peer_report(self, peer: str) -> Optional[dict]:
        return self._peer_stats.get(peer)

    def top_peers_by_bandwidth(self, n: int = 10) -> List[dict]:
        peers = [
            {"peer": p, **stats,
             "total_bytes": stats['bytes_recv'] + stats['bytes_sent']}
            for p, stats in self._peer_stats.items()
        ]
        return sorted(peers, key=lambda x: -x['total_bytes'])[:n]

    def message_distribution(self) -> dict:
        total = sum(self._msg_counts.values()) or 1
        return {
            msg: {"count": cnt, "pct": f"{cnt/total*100:.1f}%"}
            for msg, cnt in sorted(self._msg_counts.items(),
                                    key=lambda x: -x[1])
        }

    def bandwidth_summary(self) -> dict:
        elapsed = max(1, time.time() - self._start_time)
        recv    = self._bandwidth.get('recv', 0)
        sent    = self._bandwidth.get('sent', 0)
        return {
            "total_recv_mb":  f"{recv/1024/1024:.2f}",
            "total_sent_mb":  f"{sent/1024/1024:.2f}",
            "recv_rate_kbps": f"{recv/elapsed/1024:.1f}",
            "sent_rate_kbps": f"{sent/elapsed/1024:.1f}",
            "active_peers":   len(self._peer_stats),
            "uptime_hrs":     f"{elapsed/3600:.2f}",
        }

    def network_health_score(self) -> float:
        """Score 0.0-100.0 based on connectivity and activity."""
        n_peers   = len(self._peer_stats)
        peer_score = min(50, n_peers * 5)
        msg_rate   = sum(self._msg_counts.values()) / max(1, time.time() - self._start_time)
        msg_score  = min(50, msg_rate * 2)
        return peer_score + msg_score


# ---- ChainParametersRegistry
class ChainParametersRegistry:
    """
    Registry of all NEBULA chain parameters.
    Allows governance to update parameters on-chain.
    All changes are logged and time-locked.
    """

    IMMUTABLE_PARAMS = {
        "MAX_SUPPLY", "GENESIS_TIMESTAMP", "GENESIS_NONCE",
        "HALVING_INTERVAL", "GENESIS_BITS",
    }

    def __init__(self):
        self._params: Dict[str, Any] = {
            "MAX_SUPPLY":          MAX_SUPPLY,
            "INITIAL_BLOCK_REWARD": INITIAL_BLOCK_REWARD,
            "HALVING_INTERVAL":    HALVING_INTERVAL,
            "TARGET_BLOCK_TIME":   TARGET_BLOCK_TIME,
            "DIFFICULTY_WINDOW":   DIFFICULTY_WINDOW,
            "MAX_BLOCK_SIZE":      MAX_BLOCK_SIZE_BYTES,
            "MAX_TX_PER_BLOCK":    MAX_TX_PER_BLOCK,
            "MIN_TX_FEE":          MIN_TX_FEE,
            "DUST_THRESHOLD":      DUST_THRESHOLD,
            "COINBASE_MATURITY":   COINBASE_MATURITY,
            "FOUNDATION_RATE":     FOUNDATION_RATE,
            "MAX_PEERS":           MAX_PEERS,
            "CHAIN_ID":            CHAIN_ID,
            "PROTOCOL_VERSION":    PROTOCOL_VERSION,
        }
        self._history: List[dict] = []
        self._lock    = threading.RLock()

    def get(self, key: str) -> Any:
        return self._params.get(key)

    def set(self, key: str, value: Any,
             proposer: str = "",
             governance_id: str = "") -> Tuple[bool, str]:
        if key in self.IMMUTABLE_PARAMS:
            return False, f"Parameter '{key}' is immutable"
        with self._lock:
            old = self._params.get(key)
            self._params[key] = value
            self._history.append({
                "key":           key,
                "old_value":     old,
                "new_value":     value,
                "changed_by":    proposer,
                "governance_id": governance_id,
                "changed_at":    time.time(),
            })
            return True, f"Parameter '{key}' updated: {old} → {value}"

    def all_params(self) -> dict:
        return dict(self._params)

    def param_history(self, key: str = None) -> List[dict]:
        if key:
            return [h for h in self._history if h["key"] == key]
        return list(self._history)

    def validate_all(self) -> List[str]:
        """Validate parameter consistency."""
        errors = []
        if self._params.get("MIN_TX_FEE", 0) < 0:
            errors.append("MIN_TX_FEE cannot be negative")
        if self._params.get("MAX_BLOCK_SIZE", 0) < 100_000:
            errors.append("MAX_BLOCK_SIZE too small")
        if self._params.get("TARGET_BLOCK_TIME", 0) < 60:
            errors.append("TARGET_BLOCK_TIME must be >= 60 seconds")
        return errors


# ---- ForkChoiceRule
class ForkChoiceRule:
    """
    NEBULA fork choice: heaviest chain (most cumulative PoW).
    In case of same PoW: first-seen wins.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def cumulative_work(self, tip_hash: str) -> int:
        """Calculate total work in chain ending at tip_hash."""
        blk = self._bc.get_block_by_hash(tip_hash)
        if not blk:
            blk = self._bc.tip
        total = 0
        h     = blk.height
        while h >= 0:
            b = self._bc.get_block(h)
            if not b:
                break
            # Work = 2^256 / target
            target = bits_to_target(b.header.bits)
            if target > 0:
                total += (2**256) // target
            h -= 1
        return total

    def choose_best_tip(self, candidates: List[str]) -> Optional[str]:
        """Choose the best chain tip from candidates."""
        if not candidates:
            return None
        scores = {}
        for tip_hash in candidates:
            scores[tip_hash] = self.cumulative_work(tip_hash)
        return max(scores, key=scores.get)

    def should_reorg(self, new_tip_hash: str) -> bool:
        """Determine if we should reorganize to a new tip."""
        our_work = self.cumulative_work(self._bc.tip.hash)
        new_work = self.cumulative_work(new_tip_hash)
        return new_work > our_work

    def fork_choice_info(self) -> dict:
        tip = self._bc.tip
        return {
            "current_tip":       tip.hash[:16] + "...",
            "height":            tip.height,
            "cumulative_work":   str(self.cumulative_work(tip.hash))[:20] + "...",
            "rule":              "heaviest_chain_pow",
        }


# ---- ChainArchiver
class ChainArchiver:
    """
    Archives old blockchain data for long-term storage.
    Compresses and exports block ranges.
    """

    ARCHIVE_CHUNK_SIZE = 1000    # blocks per archive file

    def __init__(self, blockchain: 'NEBULABlockchain',
                  archive_dir: str = "./nebula_archive"):
        self._bc          = blockchain
        self._archive_dir = archive_dir
        self._archived:   Dict[int, str] = {}   # chunk_id -> filename
        self._lock        = threading.RLock()

    def archive_range(self, start_height: int,
                       end_height: int) -> dict:
        """Archive a range of blocks."""
        blocks = []
        for h in range(start_height, min(end_height + 1, self._bc.height + 1)):
            blk = self._bc.get_block(h)
            if blk:
                blocks.append({
                    "height":    blk.height,
                    "hash":      blk.hash,
                    "timestamp": blk.header.timestamp,
                    "tx_count":  blk.tx_count,
                    "size":      blk.byte_size(),
                })
        checksum = hashlib.sha256(
            json.dumps(blocks, sort_keys=True).encode()
        ).hexdigest()
        archive = {
            "start_height": start_height,
            "end_height":   end_height,
            "block_count":  len(blocks),
            "checksum":     checksum,
            "blocks":       blocks,
            "archived_at":  time.time(),
        }
        chunk_id = start_height // self.ARCHIVE_CHUNK_SIZE
        filename = f"nebula_archive_{chunk_id:06d}.json"
        with self._lock:
            self._archived[chunk_id] = filename
        return archive

    def verify_archive(self, archive: dict) -> bool:
        """Verify archive checksum."""
        blocks   = archive.get("blocks", [])
        expected = archive.get("checksum", "")
        computed = hashlib.sha256(
            json.dumps(blocks, sort_keys=True).encode()
        ).hexdigest()
        return computed == expected

    def archive_stats(self) -> dict:
        with self._lock:
            n_chunks = len(self._archived)
        return {
            "archived_chunks": n_chunks,
            "blocks_archived": n_chunks * self.ARCHIVE_CHUNK_SIZE,
            "chunk_size":      self.ARCHIVE_CHUNK_SIZE,
            "archive_dir":     self._archive_dir,
        }


# ---- MetricsCollector
class MetricsCollector:
    """
    Prometheus-compatible metrics for NEBULA node monitoring.
    Exposes metrics in text format for Prometheus scraping.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._counters: Dict[str, float] = {}
        self._gauges:   Dict[str, float] = {}
        self._histograms: Dict[str, List[float]] = {}
        self._start_time = time.time()

    def inc(self, name: str, value: float = 1.0, labels: dict = None):
        key = self._key(name, labels)
        self._counters[key] = self._counters.get(key, 0) + value

    def set(self, name: str, value: float, labels: dict = None):
        key = self._key(name, labels)
        self._gauges[key] = value

    def observe(self, name: str, value: float):
        if name not in self._histograms:
            self._histograms[name] = []
        self._histograms[name].append(value)
        if len(self._histograms[name]) > 10_000:
            self._histograms[name].pop(0)

    def _key(self, name: str, labels: dict = None) -> str:
        if not labels:
            return name
        label_str = ','.join(f'{k}="{v}"' for k, v in sorted(labels.items()))
        return f"{name}{{{label_str}}}"

    def collect_blockchain_metrics(self):
        """Collect current blockchain metrics."""
        bc = self._bc
        self.set("nebula_block_height",          bc.height)
        self.set("nebula_utxo_set_size",         bc.utxo.size())
        self.set("nebula_mempool_size",           bc.mempool.size())
        self.set("nebula_total_supply",           bc.utxo.total_supply())
        self.set("nebula_mining_reward",          mining_reward(bc.height))
        self.set("nebula_uptime_seconds",         time.time() - self._start_time)

    def prometheus_format(self) -> str:
        """Export metrics in Prometheus text format."""
        self.collect_blockchain_metrics()
        lines = []
        for key, val in self._gauges.items():
            name = key.split('{')[0]
            lines.append(f"# TYPE {name} gauge")
            lines.append(f"{key} {val}")
        for key, val in self._counters.items():
            name = key.split('{')[0]
            lines.append(f"# TYPE {name} counter")
            lines.append(f"{key} {val}")
        for name, values in self._histograms.items():
            if not values:
                continue
            sv = sorted(values)
            n  = len(sv)
            lines.append(f"# TYPE {name} histogram")
            lines.append(f"{name}_count {n}")
            lines.append(f"{name}_sum {sum(sv):.4f}")
            for p in [50, 90, 99]:
                idx = min(int(n * p / 100), n - 1)
                lines.append(f'{name}{{quantile="{p/100}"}} {sv[idx]:.4f}')
        return '\n'.join(lines)

    def metrics_endpoint_handler(self) -> dict:
        """Handle /metrics HTTP endpoint."""
        return {
            "content_type": "text/plain; version=0.0.4",
            "body":         self.prometheus_format(),
        }


# ---- SubscriptionManager
@dataclass
class SubscriptionManager:
    """Recurring payment subscriptions on NEBULA."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc   = blockchain
        self._subs: Dict[str, Subscription] = {}
        self._lock = threading.RLock()

    def create(self, subscriber: str, merchant: str,
                amount_nbl: float, interval_days: int,
                description: str = "", max_payments: int = 0) -> str:
        with self._lock:
            sid = hashlib.sha256(
                f"SUB:{subscriber}:{merchant}:{time.time()}".encode()
            ).hexdigest()[:16]
            interval_blocks = interval_days * 144
            self._subs[sid] = SubscriptionC(
                sub_id           = sid,
                subscriber       = subscriber,
                merchant         = merchant,
                amount           = int(amount_nbl * 10**DECIMALS),
                interval_blocks  = interval_blocks,
                next_due_block   = self._bc.height + interval_blocks,
                max_payments     = max_payments,
                description      = description,
            )
            return sid

    def process_due(self) -> List[dict]:
        """Process all due subscriptions. Returns processed list."""
        cur     = self._bc.height
        results = []
        with self._lock:
            for sub in self._subs.values():
                if not sub.is_due(cur):
                    continue
                bal = self._bc.utxo.balance(sub.subscriber)
                if bal >= sub.amount:
                    sub.payments_made   += 1
                    sub.next_due_block  += sub.interval_blocks
                    if sub.max_payments > 0 and sub.payments_made >= sub.max_payments:
                        sub.active = False
                    results.append({
                        "sub_id":  sub.sub_id,
                        "status":  "processed",
                        "amount":  sub.amount,
                    })
                else:
                    sub.active = False
                    results.append({
                        "sub_id":  sub.sub_id,
                        "status":  "cancelled_insufficient_funds",
                    })
        return results

    def cancel(self, sub_id: str, caller: str) -> Tuple[bool, str]:
        with self._lock:
            sub = self._subs.get(sub_id)
            if not sub:
                return False, "Not found"
            if caller not in (sub.subscriber, sub.merchant):
                return False, "Not authorized"
            sub.active = False
            return True, "Cancelled"

    def list_for(self, address: str) -> List[dict]:
        return [s.to_dict() for s in self._subs.values()
                if address in (s.subscriber, s.merchant)]

    def subscription_stats(self) -> dict:
        with self._lock:
            active = sum(1 for s in self._subs.values() if s.active)
            total_vol = sum(s.amount * s.payments_made for s in self._subs.values())
        return {
            "total_subscriptions": len(self._subs),
            "active":              active,
            "total_volume_nbl":    f"{total_vol/10**DECIMALS:.3f}",
        }


# ---- EscrowStatus
class EscrowStatus(_enum.Enum):
    PENDING    = "pending"
    FUNDED     = "funded"
    RELEASED   = "released"
    REFUNDED   = "refunded"
    DISPUTED   = "disputed"
    RESOLVED   = "resolved"


# ---- Escrow
@dataclass
class Escrow:
    escrow_id:    str
    buyer:        str
    seller:       str
    arbiter:      str
    amount:       int
    description:  str
    deadline_block: int
    status:       EscrowStatus = EscrowStatus.PENDING
    release_code: str = ""   # buyer uses this to release
    created_at:   float = 0.0
    resolved_by:  str = ""

    def to_dict(self) -> dict:
        return {
            "escrow_id":    self.escrow_id,
            "buyer":        self.buyer,
            "seller":       self.seller,
            "arbiter":      self.arbiter,
            "amount_nbl":   f"{self.amount/10**DECIMALS:.6f}",
            "status":       self.status.value,
            "deadline":     self.deadline_block,
            "description":  self.description,
        }


# ---- SmartEscrowEngine
class SmartEscrowEngine:
    """
    Trustless smart escrow for NEBULA.
    Buyer deposits funds; seller delivers; buyer releases.
    Arbiter resolves disputes.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._escrows: Dict[str, Escrow] = {}
        self._lock    = threading.RLock()

    def create(self, buyer: str, seller: str, arbiter: str,
                amount_nbl: float, description: str,
                deadline_days: int = 30) -> Tuple[bool, str]:
        with self._lock:
            amount = int(amount_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(buyer) < amount:
                return False, "Insufficient buyer balance"
            eid = hashlib.sha256(
                f"ESCROW:{buyer}:{seller}:{amount}:{time.time()}".encode()
            ).hexdigest()[:16]
            release_code = secrets.token_hex(8)
            self._escrows[eid] = Escrow(
                escrow_id     = eid,
                buyer         = buyer,
                seller        = seller,
                arbiter       = arbiter,
                amount        = amount,
                description   = description,
                deadline_block = self._bc.height + deadline_days * 144,
                status        = EscrowStatus.FUNDED,
                release_code  = release_code,
                created_at    = time.time(),
            )
            return True, eid

    def release(self, escrow_id: str, buyer: str,
                 code: str) -> Tuple[bool, str]:
        with self._lock:
            esc = self._escrows.get(escrow_id)
            if not esc or esc.buyer != buyer:
                return False, "Not found or not buyer"
            if esc.status != EscrowStatus.FUNDED:
                return False, f"Wrong status: {esc.status.value}"
            if code != esc.release_code:
                return False, "Wrong release code"
            esc.status = EscrowStatus.RELEASED
            return True, f"Released {esc.amount/10**DECIMALS:.6f} NBL to {esc.seller}"

    def refund(self, escrow_id: str) -> Tuple[bool, str]:
        with self._lock:
            esc = self._escrows.get(escrow_id)
            if not esc:
                return False, "Not found"
            if esc.status != EscrowStatus.FUNDED:
                return False, f"Wrong status: {esc.status.value}"
            if self._bc.height <= esc.deadline_block:
                return False, f"Deadline not passed (block {esc.deadline_block})"
            esc.status = EscrowStatus.REFUNDED
            return True, f"Refunded {esc.amount/10**DECIMALS:.6f} NBL to {esc.buyer}"

    def dispute(self, escrow_id: str, caller: str) -> Tuple[bool, str]:
        with self._lock:
            esc = self._escrows.get(escrow_id)
            if not esc or caller not in (esc.buyer, esc.seller):
                return False, "Not found or not party"
            if esc.status != EscrowStatus.FUNDED:
                return False, "Cannot dispute"
            esc.status = EscrowStatus.DISPUTED
            return True, f"Dispute opened. Arbiter: {esc.arbiter}"

    def resolve(self, escrow_id: str, arbiter: str,
                 release_to_seller: bool) -> Tuple[bool, str]:
        with self._lock:
            esc = self._escrows.get(escrow_id)
            if not esc or esc.arbiter != arbiter:
                return False, "Not arbiter"
            if esc.status != EscrowStatus.DISPUTED:
                return False, "Not disputed"
            esc.status      = EscrowStatus.RESOLVED
            esc.resolved_by = arbiter
            winner = esc.seller if release_to_seller else esc.buyer
            return True, f"Resolved: {esc.amount/10**DECIMALS:.6f} NBL sent to {winner}"

    def escrow_stats(self) -> dict:
        with self._lock:
            by_status = {}
            for e in self._escrows.values():
                k = e.status.value
                by_status[k] = by_status.get(k, 0) + 1
            total_locked = sum(e.amount for e in self._escrows.values()
                               if e.status == EscrowStatus.FUNDED)
        return {
            "total_escrows":  len(self._escrows),
            "by_status":      by_status,
            "total_locked_nbl": f"{total_locked/10**DECIMALS:.3f}",
        }


# ---- Post
@dataclass
class Post:
    post_id:   str
    author:    str
    content:   str
    ipfs_cid:  str
    timestamp: float
    likes:     int = 0
    tips:      int = 0
    replies:   List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "post_id":  self.post_id,
            "author":   self.author,
            "content":  self.content[:280],
            "timestamp": self.timestamp,
            "likes":    self.likes,
            "tips_nbl": f"{self.tips/10**DECIMALS:.6f}",
            "replies":  len(self.replies),
        }
