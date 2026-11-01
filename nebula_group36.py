"""NEBULA group36 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. LaunchpadStatus  (orig. lines 61360-61364)
   2. TokenLaunchpad  (orig. lines 61366-61467)
   3. FarmPool  (orig. lines 61474-61492)
   4. FarmPosition  (orig. lines 61494-61500)
   5. YieldFarmingV2  (orig. lines 61502-61608)
   6. DeFiInsurance  (orig. lines 61615-61706)
   7. LiquidityPosition  (orig. lines 61721-61753)
   8. ConcentratedLiquidityPool  (orig. lines 61756-61858)
   9. NFTRental  (orig. lines 61865-61932)
  10. NFTFractionalizer  (orig. lines 61935-61991)
  11. DAOTier  (orig. lines 61998-62002)
  12. DAOMember  (orig. lines 62004-62020)
  13. NEBULADao  (orig. lines 62022-62142)
  14. ChainAlertSystem  (orig. lines 62149-62165)
  15. NEBULAFullNodeV2  (orig. lines 62167-62342)
  16. CrossChainMessageType  (orig. lines 62356-62361)
  17. CrossChainMessage  (orig. lines 62363-62400)
  18. CrossChainRouter  (orig. lines 62402-62495)
  19. HDWalletV2  (orig. lines 62505-62594)
  20. PeerDiscoveryMethod  (orig. lines 62601-62606)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): APIv2Router, AddressType, AlertLevel, AlertSystem, AtomicSwapEngine, BIP39, BlockTemplateEngine, BloomFilter, BridgeEngine, ChainAnalytics, ChainArchiver, ChainParametersRegistry, CircuitBreaker, CompactBlockRelay, ConsensusRuleEngine, DIDRegistry, DataMarket, DecentralizedOracle, DynamicFeeModel, FeeFilter, FeeMarket, ForkChoiceRule, GovernanceEngine, HDKey, HDWalletExtended, InsurancePolicy, LaunchpadProject, LendingProtocol, MetricsCollector, NBL721Registry, NEBULABlockchain, NEBULADex, NEBULASocial, NEBULATreasury, NEBULAWallet, NetworkStatsCollector, OnChainLottery, OnChainRNG, PeerAddressBook, PredictionMarket, ReputationEngine, Secp256k1, ShardManager, SmartEscrowEngine, StakingEngine, StealthAddressScheme, SubscriptionManager, TransactionIndex, TransactionSpamFilter, ValidatorSetManager, VestingManager, WalletAccount, WalletConnectBridge
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

COIN_TYPE              = 2025         # BIP-44 coin type for NEBULA

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

GAP_LIMIT       = 20           # standard address gap limit

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


# ---- LaunchpadStatus
class LaunchpadStatus(_enum.Enum):
    DRAFT      = "draft"
    ACTIVE     = "active"
    COMPLETED  = "completed"
    CANCELLED  = "cancelled"


# ---- TokenLaunchpad
@dataclass
class TokenLaunchpad:
    """
    NEBULA token launchpad for IDO / ICO.
    Projects raise NBL in exchange for new tokens.
    """

    PLATFORM_FEE_PCT = 0.03   # 3% of raised amount

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._projects: Dict[str, LaunchpadProject] = {}
        self._contributions: Dict[str, Dict[str, int]] = {}  # pid -> {addr: amount}
        self._lock     = threading.RLock()

    def create_project(self, creator: str, token_name: str,
                        token_symbol: str, total_supply: float,
                        sale_pct: float, price: float,
                        soft_cap: float, hard_cap: float,
                        duration_days: int = 7) -> str:
        with self._lock:
            total  = int(total_supply * 10**DECIMALS)
            sale   = int(total * sale_pct)
            pid    = hashlib.sha256(
                f"LAUNCH:{creator}:{token_symbol}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._projects[pid] = LaunchpadProjectC(
                project_id      = pid,
                creator         = creator,
                token_name      = token_name,
                token_symbol    = token_symbol,
                total_supply    = total,
                sale_supply     = sale,
                price_per_token = price,
                soft_cap        = soft_cap,
                hard_cap        = hard_cap,
                start_block     = self._bc.height,
                end_block       = self._bc.height + duration_days * 144,
                status          = LaunchpadStatus.ACTIVE,
            )
            self._contributions[pid] = {}
            return pid

    def contribute(self, project_id: str, investor: str,
                    amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            proj = self._projects.get(project_id)
            if not proj:
                return False, "Project not found"
            if proj.status != LaunchpadStatus.ACTIVE:
                return False, f"Not active: {proj.status.value}"
            if self._bc.height > proj.end_block:
                return False, "Sale ended"

            amount    = int(amount_nbl * 10**DECIMALS)
            hard_cap  = int(proj.hard_cap * 10**DECIMALS)
            remaining = hard_cap - proj.raised

            if amount > remaining:
                amount = remaining
            if amount <= 0:
                return False, "Hard cap reached"

            proj.raised   += amount
            proj.participants.add(investor)
            self._contributions[project_id][investor] = (
                self._contributions[project_id].get(investor, 0) + amount)

            tokens = amount / (proj.price_per_token * 10**DECIMALS)
            if proj.raised >= hard_cap:
                proj.status = LaunchpadStatus.COMPLETED

            return True, f"Contributed {amount/10**DECIMALS:.3f} NBL → {tokens:.2f} {proj.token_symbol}"

    def finalize(self, project_id: str) -> Tuple[bool, str]:
        with self._lock:
            proj = self._projects.get(project_id)
            if not proj:
                return False, "Not found"
            soft = int(proj.soft_cap * 10**DECIMALS)
            if proj.raised < soft:
                proj.status = LaunchpadStatus.CANCELLED
                return False, f"Soft cap not met ({proj.raised/10**DECIMALS:.3f} < {proj.soft_cap})"
            if proj.status != LaunchpadStatus.COMPLETED:
                proj.status = LaunchpadStatus.COMPLETED
            fee = int(proj.raised * self.PLATFORM_FEE_PCT)
            return True, (f"Finalized! Raised {proj.raised/10**DECIMALS:.3f} NBL. "
                          f"Platform fee: {fee/10**DECIMALS:.3f}")

    def launchpad_stats(self) -> dict:
        with self._lock:
            active     = sum(1 for p in self._projects.values()
                             if p.status == LaunchpadStatus.ACTIVE)
            completed  = sum(1 for p in self._projects.values()
                             if p.status == LaunchpadStatus.COMPLETED)
            total_raised = sum(p.raised for p in self._projects.values())
        return {
            "total_projects": len(self._projects),
            "active":         active,
            "completed":      completed,
            "total_raised_nbl": f"{total_raised/10**DECIMALS:.3f}",
        }


# ---- FarmPool
@dataclass
class FarmPool:
    pool_id:       str
    lp_token:      str    # e.g. "NBL-USDT-LP"
    reward_token:  str    # "NBL"
    reward_per_block: int
    total_staked:  int = 0
    acc_reward_per_share: float = 0.0
    last_reward_block: int = 0
    allocation_points: int = 100

    def to_dict(self) -> dict:
        return {
            "pool_id":         self.pool_id,
            "lp_token":        self.lp_token,
            "reward_per_block": f"{self.reward_per_block/10**DECIMALS:.6f}",
            "total_staked":    f"{self.total_staked/10**DECIMALS:.3f}",
            "alloc_points":    self.allocation_points,
        }


# ---- FarmPosition
@dataclass
class FarmPosition:
    farmer:     str
    pool_id:    str
    amount:     int
    reward_debt: float = 0.0
    staked_at:  float = field(default_factory=time.time)


# ---- YieldFarmingV2
class YieldFarmingV2:
    """
    Advanced yield farming for NEBULA.
    Multiple pools, adjustable allocation points, compounding.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._pools:   Dict[str, FarmPool]     = {}
        self._positions: Dict[str, Dict[str, FarmPosition]] = {}  # pool -> addr -> pos
        self._lock     = threading.RLock()

    def add_pool(self, lp_token: str, reward_per_block: float,
                  alloc_points: int = 100) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"FARM:{lp_token}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._pools[pid] = FarmPool(
                pool_id          = pid,
                lp_token         = lp_token,
                reward_token     = "NBL",
                reward_per_block = int(reward_per_block * 10**DECIMALS),
                last_reward_block = self._bc.height,
                allocation_points = alloc_points,
            )
            self._positions[pid] = {}
            return pid

    def _update_pool(self, pool: FarmPool):
        cur = self._bc.height
        if cur <= pool.last_reward_block or pool.total_staked == 0:
            pool.last_reward_block = cur
            return
        blocks   = cur - pool.last_reward_block
        reward   = blocks * pool.reward_per_block
        pool.acc_reward_per_share += reward / pool.total_staked
        pool.last_reward_block     = cur

    def deposit(self, farmer: str, pool_id: str,
                 amount: float) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, "Pool not found"
            self._update_pool(pool)
            amount_raw = int(amount * 10**DECIMALS)
            pos = self._positions[pool_id].get(farmer)
            pending = 0
            if pos:
                pending = int(pos.amount * pool.acc_reward_per_share - pos.reward_debt)
                pos.amount += amount_raw
                pos.reward_debt = pos.amount * pool.acc_reward_per_share
            else:
                self._positions[pool_id][farmer] = FarmPosition(
                    farmer      = farmer,
                    pool_id     = pool_id,
                    amount      = amount_raw,
                    reward_debt = amount_raw * pool.acc_reward_per_share,
                )
            pool.total_staked += amount_raw
            msg = f"Deposited {amount:.3f} LP"
            if pending > 0:
                msg += f", claimed {pending/10**DECIMALS:.6f} NBL"
            return True, msg

    def withdraw(self, farmer: str, pool_id: str,
                  amount: float) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, "Pool not found"
            pos = self._positions[pool_id].get(farmer)
            if not pos:
                return False, "No position"
            self._update_pool(pool)
            amount_raw = int(amount * 10**DECIMALS)
            if pos.amount < amount_raw:
                return False, "Insufficient staked amount"
            pending = int(pos.amount * pool.acc_reward_per_share - pos.reward_debt)
            pos.amount      -= amount_raw
            pos.reward_debt  = pos.amount * pool.acc_reward_per_share
            pool.total_staked -= amount_raw
            return True, (f"Withdrew {amount:.3f} LP, "
                          f"claimed {pending/10**DECIMALS:.6f} NBL")

    def pending_rewards(self, farmer: str, pool_id: str) -> int:
        pool = self._pools.get(pool_id)
        pos  = self._positions.get(pool_id, {}).get(farmer)
        if not pool or not pos:
            return 0
        acc = pool.acc_reward_per_share
        cur = self._bc.height
        if cur > pool.last_reward_block and pool.total_staked > 0:
            blocks = cur - pool.last_reward_block
            acc   += blocks * pool.reward_per_block / pool.total_staked
        return int(pos.amount * acc - pos.reward_debt)

    def farm_stats(self) -> dict:
        with self._lock:
            total_staked = sum(p.total_staked for p in self._pools.values())
            total_farmers = sum(len(pos) for pos in self._positions.values())
        return {
            "total_pools":      len(self._pools),
            "total_staked_nbl": f"{total_staked/10**DECIMALS:.3f}",
            "total_farmers":    total_farmers,
        }


# ---- DeFiInsurance
@dataclass
class DeFiInsurance:
    """
    Decentralized insurance protocol for NEBULA DeFi.
    Users buy coverage; capital providers earn premiums.
    """

    PREMIUM_RATES = {
        "smart_contract": 0.02,   # 2% annual
        "bridge":         0.05,
        "staking":        0.01,
        "dex":            0.03,
    }
    COVERAGE_RATIO = 0.80   # pays 80% of covered amount

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._policies: Dict[str, InsurancePolicy] = {}
        self._capital_pool: int = 0
        self._claims_paid:  int = 0
        self._premiums_collected: int = 0
        self._lock     = threading.RLock()

    def deposit_capital(self, provider: str,
                         amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            amount = int(amount_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(provider) < amount:
                return False, "Insufficient balance"
            self._capital_pool += amount
            return True, f"Deposited {amount_nbl} NBL to insurance pool"

    def buy_policy(self, holder: str, coverage_type: str,
                    protocol: str, coverage_nbl: float,
                    duration_days: int = 30) -> Tuple[bool, str]:
        with self._lock:
            rate = self.PREMIUM_RATES.get(coverage_type, 0.03)
            coverage_amount = int(coverage_nbl * 10**DECIMALS)
            annual_premium  = int(coverage_amount * rate)
            premium         = int(annual_premium * duration_days / 365)
            if coverage_amount > self._capital_pool:
                return False, "Insufficient pool capital"
            pid = hashlib.sha256(
                f"INS:{holder}:{protocol}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._policies[pid] = InsurancePolicyC(
                policy_id       = pid,
                holder          = holder,
                coverage        = coverage_type,
                covered_protocol = protocol,
                coverage_amount = coverage_amount,
                premium_paid    = premium,
                start_block     = self._bc.height,
                end_block       = self._bc.height + duration_days * 144,
            )
            self._premiums_collected += premium
            return True, (f"Policy {pid}: {coverage_nbl} NBL coverage "
                          f"for {duration_days}d, premium: {premium/10**DECIMALS:.6f} NBL")

    def file_claim(self, policy_id: str,
                    holder: str,
                    evidence: str = "") -> Tuple[bool, int]:
        with self._lock:
            pol = self._policies.get(policy_id)
            if not pol or pol.holder != holder:
                return False, 0
            if pol.claimed:
                return False, 0
            if not pol.is_active(self._bc.height):
                return False, 0
            payout = int(pol.coverage_amount * self.COVERAGE_RATIO)
            if payout > self._capital_pool:
                payout = self._capital_pool
            pol.claimed = True
            pol.active  = False
            self._capital_pool -= payout
            self._claims_paid  += payout
            return True, payout

    def insurance_stats(self) -> dict:
        with self._lock:
            active = sum(1 for p in self._policies.values()
                         if p.is_active(self._bc.height))
            total_coverage = sum(p.coverage_amount for p in self._policies.values())
        return {
            "active_policies":     active,
            "total_policies":      len(self._policies),
            "capital_pool_nbl":    f"{self._capital_pool/10**DECIMALS:.3f}",
            "premiums_collected":  f"{self._premiums_collected/10**DECIMALS:.3f}",
            "claims_paid":         f"{self._claims_paid/10**DECIMALS:.3f}",
            "total_coverage_nbl":  f"{total_coverage/10**DECIMALS:.3f}",
        }


# ---- LiquidityPosition
@dataclass
class LiquidityPosition:
    pos_id:       str
    owner:        str
    pool_id:      str
    token_a:      str
    token_b:      str
    amount_a:     int
    amount_b:     int
    tick_lower:   float   # price lower bound
    tick_upper:   float   # price upper bound
    liquidity:    float
    fee_earned_a: int = 0
    fee_earned_b: int = 0
    created_at:   float = 0.0

    def in_range(self, current_price: float) -> bool:
        return self.tick_lower <= current_price <= self.tick_upper

    def to_dict(self) -> dict:
        return {
            "pos_id":     self.pos_id,
            "owner":      self.owner,
            "pool":       self.pool_id,
            "tokens":     f"{self.token_a}/{self.token_b}",
            "amount_a":   f"{self.amount_a/10**DECIMALS:.6f}",
            "amount_b":   f"{self.amount_b/10**DECIMALS:.6f}",
            "price_range": f"[{self.tick_lower:.4f}, {self.tick_upper:.4f}]",
            "in_range":   self.in_range(
                (self.tick_lower + self.tick_upper) / 2),
            "fee_a":      f"{self.fee_earned_a/10**DECIMALS:.9f}",
            "fee_b":      f"{self.fee_earned_b/10**DECIMALS:.9f}",
        }


# ---- ConcentratedLiquidityPool
class ConcentratedLiquidityPool:
    """
    Concentrated liquidity pool (Uniswap v3 style).
    LPs deposit in specific price ranges, earning more fees
    when price stays in their range.
    """

    FEE_TIER_BIPS = [5, 30, 100]    # 0.05%, 0.30%, 1.00%

    def __init__(self, pool_id: str, token_a: str, token_b: str,
                  initial_price: float, fee_bps: int = 30):
        self.pool_id       = pool_id
        self.token_a       = token_a
        self.token_b       = token_b
        self.current_price = initial_price
        self.fee_bps       = fee_bps
        self._positions:   Dict[str, LiquidityPosition] = {}
        self._volume:      int = 0
        self._fees_a:      int = 0
        self._fees_b:      int = 0

    def add_position(self, owner: str, amount_a: float, amount_b: float,
                      price_low: float, price_high: float) -> str:
        pos_id   = hashlib.sha256(
            f"CLM:{owner}:{self.pool_id}:{time.time()}".encode()
        ).hexdigest()[:16]
        liq_a    = int(amount_a * 10**DECIMALS)
        liq_b    = int(amount_b * 10**DECIMALS)
        liq      = (liq_a * liq_b) ** 0.5
        pos = LiquidityPosition(
            pos_id     = pos_id,
            owner      = owner,
            pool_id    = self.pool_id,
            token_a    = self.token_a,
            token_b    = self.token_b,
            amount_a   = liq_a,
            amount_b   = liq_b,
            tick_lower = price_low,
            tick_upper = price_high,
            liquidity  = liq,
            created_at = time.time(),
        )
        self._positions[pos_id] = pos
        return pos_id

    def swap(self, token_in: str, amount_in: int) -> Tuple[int, float]:
        """Execute a swap. Returns (amount_out, price_impact_pct)."""
        fee        = int(amount_in * self.fee_bps / 10_000)
        amount_net = amount_in - fee
        # Active liquidity: only positions in range
        active_liq = sum(
            p.liquidity for p in self._positions.values()
            if p.in_range(self.current_price)
        )
        if active_liq == 0:
            return 0, 0.0
        k          = active_liq * active_liq
        # Constant product formula
        reserve_in = amount_net
        amount_out = int(k / (active_liq + amount_net) * 0.997)
        old_price  = self.current_price
        # Update price
        if token_in == self.token_a:
            self.current_price *= (1 + amount_net / active_liq)
            self._fees_a += fee
        else:
            self.current_price /= (1 + amount_net / active_liq)
            self._fees_b += fee
        self._volume += amount_in
        impact = abs(self.current_price - old_price) / old_price * 100
        return amount_out, impact

    def collect_fees(self, pos_id: str) -> Tuple[int, int]:
        """Collect accumulated fees for a position."""
        pos = self._positions.get(pos_id)
        if not pos or not pos.in_range(self.current_price):
            return 0, 0
        if self._fees_a == 0 and self._fees_b == 0:
            return 0, 0
        # Distribute proportional to liquidity
        total_liq = sum(p.liquidity for p in self._positions.values()
                        if p.in_range(self.current_price)) or 1
        share  = pos.liquidity / total_liq
        fee_a  = int(self._fees_a * share)
        fee_b  = int(self._fees_b * share)
        self._fees_a -= fee_a
        self._fees_b -= fee_b
        pos.fee_earned_a += fee_a
        pos.fee_earned_b += fee_b
        return fee_a, fee_b

    def pool_info(self) -> dict:
        active_pos = sum(1 for p in self._positions.values()
                         if p.in_range(self.current_price))
        return {
            "pool_id":       self.pool_id,
            "pair":          f"{self.token_a}/{self.token_b}",
            "price":         f"{self.current_price:.6f}",
            "fee_bps":       self.fee_bps,
            "positions":     len(self._positions),
            "active_positions": active_pos,
            "volume_nbl":    f"{self._volume/10**DECIMALS:.3f}",
        }


# ---- NFTRental
class NFTRental:
    """NFT rental system — rent NFTs for a period of time."""

    def __init__(self):
        self._rentals: Dict[str, dict] = {}   # nft_key -> rental info
        self._lock    = threading.RLock()

    def list_for_rent(self, collection_id: str, token_id: int,
                       owner: str, price_per_day: float,
                       max_days: int = 30) -> str:
        key = f"{collection_id}:{token_id}"
        with self._lock:
            rid = hashlib.sha256(f"RENT:{key}:{time.time()}".encode()).hexdigest()[:12]
            self._rentals[rid] = {
                "rental_id":     rid,
                "collection_id": collection_id,
                "token_id":      token_id,
                "owner":         owner,
                "renter":        None,
                "price_per_day": price_per_day,
                "max_days":      max_days,
                "end_time":      None,
                "active":        True,
            }
            return rid

    def rent(self, rental_id: str, renter: str,
              days: int) -> Tuple[bool, str]:
        with self._lock:
            r = self._rentals.get(rental_id)
            if not r or not r["active"]:
                return False, "Not available"
            if r["renter"] is not None:
                return False, "Already rented"
            if days > r["max_days"]:
                return False, f"Max {r['max_days']} days"
            cost = r["price_per_day"] * days
            r["renter"]   = renter
            r["end_time"] = time.time() + days * 86400
            return True, f"Rented for {days} days, cost {cost:.3f} NBL"

    def end_rental(self, rental_id: str) -> bool:
        with self._lock:
            r = self._rentals.get(rental_id)
            if not r:
                return False
            r["renter"]   = None
            r["end_time"] = None
            return True

    def current_renter(self, rental_id: str) -> Optional[str]:
        r = self._rentals.get(rental_id)
        if not r or r["renter"] is None:
            return None
        if time.time() > r.get("end_time", 0):
            self.end_rental(rental_id)
            return None
        return r["renter"]

    def rental_stats(self) -> dict:
        active_rentals = sum(
            1 for r in self._rentals.values()
            if r["renter"] and time.time() < r.get("end_time", 0)
        )
        return {
            "total_listings": len(self._rentals),
            "active_rentals": active_rentals,
        }


# ---- NFTFractionalizer
class NFTFractionalizer:
    """Fractionalize an NFT into ERC-20 style tokens."""

    def __init__(self):
        self._vaults: Dict[str, dict] = {}
        self._lock   = threading.RLock()

    def fractionalize(self, collection_id: str, token_id: int,
                       owner: str, n_fractions: int,
                       initial_price: float) -> str:
        with self._lock:
            vid = hashlib.sha256(
                f"FRAC:{collection_id}:{token_id}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._vaults[vid] = {
                "vault_id":      vid,
                "collection_id": collection_id,
                "token_id":      token_id,
                "owner":         owner,
                "n_fractions":   n_fractions,
                "price":         initial_price,
                "holders":       {owner: n_fractions},
                "active":        True,
                "buyout_price":  initial_price * n_fractions * 1.1,
            }
            return vid

    def transfer_fractions(self, vault_id: str, sender: str,
                            recipient: str, amount: int) -> Tuple[bool, str]:
        with self._lock:
            vault = self._vaults.get(vault_id)
            if not vault:
                return False, "Vault not found"
            holders = vault["holders"]
            if holders.get(sender, 0) < amount:
                return False, "Insufficient fractions"
            holders[sender]    -= amount
            holders[recipient]  = holders.get(recipient, 0) + amount
            return True, f"Transferred {amount} fractions"

    def buyout(self, vault_id: str, buyer: str) -> Tuple[bool, str]:
        with self._lock:
            vault = self._vaults.get(vault_id)
            if not vault or not vault["active"]:
                return False, "Vault not active"
            vault["active"] = False
            return True, (f"Buyout successful! {buyer} acquires "
                          f"{vault['collection_id']}#{vault['token_id']}")

    def vault_info(self, vault_id: str) -> Optional[dict]:
        v = self._vaults.get(vault_id)
        if not v:
            return None
        return {
            **v,
            "holder_count": len([h for h in v["holders"] if v["holders"][h] > 0]),
        }


# ---- DAOTier
class DAOTier(_enum.Enum):
    COMMUNITY   = "community"
    GUARDIAN    = "guardian"
    COUNCIL     = "council"
    CORE        = "core"


# ---- DAOMember
@dataclass
class DAOMember:
    address:    str
    tier:       DAOTier
    voting_power: float
    joined_at:  float
    proposals_created: int = 0
    votes_cast: int = 0

    def to_dict(self) -> dict:
        return {
            "address":        self.address,
            "tier":           self.tier.value,
            "voting_power":   f"{self.voting_power:.4f}",
            "proposals":      self.proposals_created,
            "votes":          self.votes_cast,
        }


# ---- NEBULADao
class NEBULADao:
    """
    NEBULA DAO governance system.
    Tiered membership, weighted voting, treasury spending.
    """

    MIN_STAKE_FOR_COMMUNITY = 100 * 10**DECIMALS
    MIN_STAKE_FOR_GUARDIAN  = 10_000 * 10**DECIMALS
    MIN_STAKE_FOR_COUNCIL   = 100_000 * 10**DECIMALS

    def __init__(self, blockchain: 'NEBULABlockchain',
                  treasury: 'NEBULATreasury' = None):
        self._bc       = blockchain
        self._treasury = treasury
        self._members: Dict[str, DAOMember] = {}
        self._proposals: List[dict] = []
        self._lock     = threading.RLock()

    def join(self, address: str) -> Tuple[bool, str]:
        with self._lock:
            balance = self._bc.utxo.balance(address)
            if balance >= self.MIN_STAKE_FOR_COUNCIL:
                tier = DAOTier.COUNCIL
                power = 10.0
            elif balance >= self.MIN_STAKE_FOR_GUARDIAN:
                tier = DAOTier.GUARDIAN
                power = 3.0
            elif balance >= self.MIN_STAKE_FOR_COMMUNITY:
                tier = DAOTier.COMMUNITY
                power = 1.0
            else:
                return False, f"Need {self.MIN_STAKE_FOR_COMMUNITY/10**DECIMALS:.0f} NBL to join"
            self._members[address] = DAOMember(
                address      = address,
                tier         = tier,
                voting_power = power,
                joined_at    = time.time(),
            )
            return True, f"Joined DAO as {tier.value} (voting power: {power}x)"

    def create_proposal(self, creator: str,
                          title: str, description: str,
                          action: str, params: dict = None) -> Tuple[bool, str]:
        with self._lock:
            member = self._members.get(creator)
            if not member:
                return False, "Not a DAO member"
            if member.tier == DAOTier.COMMUNITY and member.proposals_created >= 3:
                return False, "Community members limited to 3 proposals"
            pid = hashlib.sha256(
                f"DAO:{creator}:{title}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._proposals.append({
                "id":          pid,
                "creator":     creator,
                "title":       title,
                "description": description,
                "action":      action,
                "params":      params or {},
                "votes_for":   0.0,
                "votes_against": 0.0,
                "voters":      {},
                "created_at":  time.time(),
                "status":      "active",
            })
            member.proposals_created += 1
            return True, pid

    def vote(self, voter: str, proposal_id: str,
              support: bool) -> Tuple[bool, str]:
        with self._lock:
            member = self._members.get(voter)
            if not member:
                return False, "Not a DAO member"
            prop = next((p for p in self._proposals if p["id"] == proposal_id), None)
            if not prop or prop["status"] != "active":
                return False, "Proposal not found or not active"
            if voter in prop["voters"]:
                return False, "Already voted"
            power = member.voting_power
            if support:
                prop["votes_for"] += power
            else:
                prop["votes_against"] += power
            prop["voters"][voter] = "yes" if support else "no"
            member.votes_cast += 1
            total = prop["votes_for"] + prop["votes_against"]
            pct   = prop["votes_for"] / total * 100 if total > 0 else 0
            return True, f"Vote recorded. Current: {pct:.1f}% support"

    def execute_proposal(self, proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            prop = next((p for p in self._proposals if p["id"] == proposal_id), None)
            if not prop:
                return False, "Not found"
            if prop["status"] != "active":
                return False, "Already executed/failed"
            total = prop["votes_for"] + prop["votes_against"]
            if total < 10:
                return False, "Insufficient participation"
            pct = prop["votes_for"] / total if total > 0 else 0
            if pct >= 0.60:
                prop["status"] = "passed"
                return True, f"Proposal passed ({pct*100:.1f}% support). Executing: {prop['action']}"
            else:
                prop["status"] = "failed"
                return False, f"Proposal failed ({pct*100:.1f}% support)"

    def dao_stats(self) -> dict:
        with self._lock:
            tiers = {}
            for m in self._members.values():
                tiers[m.tier.value] = tiers.get(m.tier.value, 0) + 1
            passed  = sum(1 for p in self._proposals if p["status"] == "passed")
            failed  = sum(1 for p in self._proposals if p["status"] == "failed")
            active  = sum(1 for p in self._proposals if p["status"] == "active")
        return {
            "members":    len(self._members),
            "by_tier":    tiers,
            "proposals":  {"active": active, "passed": passed, "failed": failed},
        }


# ---- ChainAlertSystem
class ChainAlertSystem(AlertSystem):
    """AlertSystem bound to a blockchain: raises alerts from new blocks."""

    def __init__(self, blockchain=None):
        super().__init__()
        self.blockchain  = blockchain
        self._last_ts    = None
        self.blocks_seen = 0

    def on_new_block(self, block: 'Block'):
        self.blocks_seen += 1
        ts = block.header.timestamp
        if self._last_ts is not None and ts - self._last_ts > 2 * 3600:
            self.alert(AlertLevel.WARNING,
                       f"Long gap before block {block.height}: {ts - self._last_ts}s",
                       {"height": block.height})
        self._last_ts = ts


# ---- NEBULAFullNodeV2
class NEBULAFullNodeV2:
    """
    NEBULA Full Node v2 — complete integration of all subsystems.
    Single class that wires together every protocol component.
    The production-ready node implementation.
    """

    NODE_VERSION = "2.0.0"

    def __init__(self, miner_address: str = "",
                  enable_mining: bool = False,
                  enable_api: bool    = True):
        self.blockchain      = NEBULABlockchain()
        self.miner_address   = miner_address or FOUNDATION_ADDRESS
        self.enable_mining   = enable_mining
        self.enable_api      = enable_api

        # Core protocol
        self.mempool         = self.blockchain.mempool
        self.utxo            = self.blockchain.utxo

        # Consensus
        self.consensus_rules = ConsensusRuleEngine(self.blockchain)
        self.fork_choice     = ForkChoiceRule(self.blockchain)

        # Wallet
        self.wallet          = NEBULAWallet.generate()
        self.hd_wallet       = HDWalletExtended(self.wallet.mnemonic)

        # P2P
        self.address_book    = PeerAddressBook()
        self.compact_relay   = CompactBlockRelay(self.mempool)
        self.fee_filter      = FeeFilter()
        self.net_stats       = NetworkStatsCollector()

        # DeFi
        self.governance      = GovernanceEngine(self.blockchain)
        self.staking         = StakingEngine(self.blockchain)
        self.dex             = NEBULADex(self.blockchain)
        self.nft             = NBL721Registry()
        self.bridge          = BridgeEngine(self.blockchain)
        self.lending         = LendingProtocol(DecentralizedOracle())
        self.yield_farming   = YieldFarmingV2(self.blockchain)
        self.insurance       = DeFiInsurance(self.blockchain)
        self.atomic_swaps    = AtomicSwapEngine(self.blockchain)
        self.prediction_mkt  = PredictionMarket(self.blockchain)

        # Identity & Social
        self.did_registry    = DIDRegistry()
        self.social          = NEBULASocial(self.blockchain)
        self.reputation      = ReputationEngine(
                                 self.blockchain, self.staking, self.social)

        # Infrastructure
        self.vesting         = VestingManager(self.blockchain)
        self.validator_set   = ValidatorSetManager(self.blockchain)
        self.data_market     = DataMarket(self.blockchain)
        self.launchpad       = TokenLaunchpad(self.blockchain)
        self.subscriptions   = SubscriptionManager(self.blockchain)
        self.escrow          = SmartEscrowEngine(self.blockchain)
        self.lottery         = OnChainLottery(self.blockchain,
                                OnChainRNG(self.blockchain))

        # Analytics & Monitoring
        self.analytics       = ChainAnalytics(self.blockchain)
        self.alerts          = ChainAlertSystem(self.blockchain)
        self.metrics         = MetricsCollector(self.blockchain)
        self.tx_index        = TransactionIndex()
        self.bloom_filter    = BloomFilter(n_elements=10_000)
        self.spam_filter     = TransactionSpamFilter()

        # Mining
        self.block_template  = BlockTemplateEngine(
                                 self.blockchain, self.miner_address)
        self.fee_market      = FeeMarket(self.blockchain)
        self.dynamic_fees    = DynamicFeeModel(self.blockchain)

        # Scaling
        self.shard_manager   = ShardManager()
        self.chain_archiver  = ChainArchiver(self.blockchain)
        self.circuit_breaker = CircuitBreaker()

        # APIs
        self.api_v2          = APIv2Router(self)
        self.walletconnect   = WalletConnectBridge()

        # DAO
        self.dao             = NEBULADao(self.blockchain)
        self.treasury        = NEBULATreasury(self.blockchain)

        # Chain parameters
        self.params_registry = ChainParametersRegistry()

        # Privacy
        self.privacy         = StealthAddressScheme()

        print(f"  🌌 NEBULA Full Node v{self.NODE_VERSION} initialized")
        print(f"  ⛓️  Chain height: {self.blockchain.height}")
        print(f"  🔑 Node address: {self.miner_address[:16]}...")
        print(f"  📦 Subsystems: {self._subsystem_count()} active")

    def _subsystem_count(self) -> int:
        return len([v for v in self.__dict__.values()
                    if not isinstance(v, (str, bool, int, type(None)))])

    def on_new_block(self, block: 'Block'):
        """Called when a new block is added to the chain."""
        self.tx_index.index_block(block)
        self.fee_market.record_block(block)
        self.dynamic_fees.update_base_fee(block)
        self.alerts.on_new_block(block)
        self.metrics.inc("nebula_blocks_total")
        self.metrics.inc("nebula_txs_total", len(block.transactions))
        self.shard_manager.process_orphans() if hasattr(
            self.shard_manager, 'process_orphans') else None
        self.subscriptions.process_due()

    def submit_transaction(self, tx: 'Transaction') -> Tuple[bool, str]:
        """Submit a transaction through all validation layers."""
        # Spam filter
        for inp in tx.inputs:
            addr = inp.outpoint.address if hasattr(inp.outpoint, 'address') else ""
            if addr:
                ok, msg = self.spam_filter.check_rate_limit(addr)
                if not ok:
                    return False, f"Rate limited: {msg}"

        ok, msg = self.spam_filter.check_tx(tx)
        if not ok:
            return False, f"Spam filter: {msg}"

        # Fee filter
        fee_rate = tx.fee(self.utxo) // max(1, tx.byte_size())
        min_rate = self.fee_filter.min_fee_rate
        if fee_rate < min_rate:
            return False, f"Fee too low: {fee_rate} < {min_rate}"

        # Mempool submission
        return self.mempool.submit(tx)

    def node_status(self) -> dict:
        bc = self.blockchain
        return {
            "node_version":     self.NODE_VERSION,
            "chain_height":     bc.height,
            "best_block":       bc.tip.hash[:16] + "...",
            "mempool_size":     self.mempool.size(),
            "utxo_set_size":    self.utxo.size(),
            "peers":            self.address_book.size(),
            "mining":           self.enable_mining,
            "miner_address":    self.miner_address[:16] + "...",
            "subsystems":       self._subsystem_count(),
            "api_v2_routes":    len(self.api_v2.list_routes()),
        }

    def ecosystem_report(self) -> dict:
        """Generate a comprehensive ecosystem report."""
        return {
            "node":          self.node_status(),
            "staking":       self.staking.staking_stats(),
            "dex":           self.dex.dex_stats(),
            "nft":           self.nft.nft_stats(),
            "governance":    self.governance.governance_stats(),
            "bridge":        self.bridge.bridge_stats(),
            "social":        self.social.social_stats(),
            "data_market":   self.data_market.market_stats(),
            "launchpad":     self.launchpad.launchpad_stats(),
            "insurance":     self.insurance.insurance_stats(),
            "farming":       self.yield_farming.farm_stats(),
            "dao":           self.dao.dao_stats(),
            "treasury":      self.treasury.budget_report(),
            "prediction_mkt": self.prediction_mkt.market_stats(),
            "chain_archiver": self.chain_archiver.archive_stats(),
            "circuit_breaker": self.circuit_breaker.status(),
            "metrics":       self.metrics.prometheus_format()[:500],
        }


# ---- CrossChainMessageType
class CrossChainMessageType(_enum.Enum):
    ASSET_TRANSFER   = "asset_transfer"
    CONTRACT_CALL    = "contract_call"
    DATA_PAYLOAD     = "data_payload"
    GOVERNANCE_VOTE  = "governance_vote"
    NFT_TRANSFER     = "nft_transfer"


# ---- CrossChainMessage
@dataclass
class CrossChainMessage:
    msg_id:       str
    source_chain: str
    dest_chain:   str
    msg_type:     CrossChainMessageType
    sender:       str
    recipient:    str
    payload:      dict
    nonce:        int
    fee:          int
    timestamp:    float
    status:       str = "pending"   # pending/relayed/delivered/failed
    relayer:      str = ""
    proof:        str = ""

    def hash(self) -> str:
        data = json.dumps({
            "source": self.source_chain,
            "dest":   self.dest_chain,
            "type":   self.msg_type.value,
            "sender": self.sender,
            "nonce":  self.nonce,
            "payload": self.payload,
        }, sort_keys=True).encode()
        return hashlib.sha256(data).hexdigest()

    def to_dict(self) -> dict:
        return {
            "msg_id":     self.msg_id,
            "from":       self.source_chain,
            "to":         self.dest_chain,
            "type":       self.msg_type.value,
            "sender":     self.sender,
            "recipient":  self.recipient,
            "status":     self.status,
            "fee_nbl":    f"{self.fee/10**DECIMALS:.6f}",
        }


# ---- CrossChainRouter
class CrossChainRouter:
    """
    Routes messages between NEBULA and other chains.
    Uses relayers to deliver messages cross-chain.
    """

    SUPPORTED_CHAINS = [
        "nebula", "ethereum", "bitcoin", "bnb_chain",
        "polygon", "avalanche", "solana", "cosmos"
    ]

    BASE_FEE_PER_MSG = 1 * 10**DECIMALS    # 1 NBL per message

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._messages: Dict[str, CrossChainMessage] = {}
        self._nonces:   Dict[str, int]               = {}  # sender -> nonce
        self._relayers: Set[str]                     = set()
        self._lock      = threading.RLock()

    def register_relayer(self, relayer_addr: str) -> bool:
        with self._lock:
            self._relayers.add(relayer_addr)
            return True

    def send_message(self, sender: str, dest_chain: str,
                      recipient: str, msg_type: CrossChainMessageType,
                      payload: dict) -> Tuple[bool, str]:
        with self._lock:
            if dest_chain not in self.SUPPORTED_CHAINS:
                return False, f"Unsupported chain: {dest_chain}"
            bal = self._bc.utxo.balance(sender)
            if bal < self.BASE_FEE_PER_MSG:
                return False, "Insufficient fee"
            nonce = self._nonces.get(sender, 0) + 1
            self._nonces[sender] = nonce
            mid = hashlib.sha256(
                f"CCM:{sender}:{dest_chain}:{nonce}:{time.time()}".encode()
            ).hexdigest()[:16]
            msg = CrossChainMessage(
                msg_id       = mid,
                source_chain = "nebula",
                dest_chain   = dest_chain,
                msg_type     = msg_type,
                sender       = sender,
                recipient    = recipient,
                payload      = payload,
                nonce        = nonce,
                fee          = self.BASE_FEE_PER_MSG,
                timestamp    = time.time(),
            )
            msg.proof = msg.hash()
            self._messages[mid] = msg
            return True, mid

    def relay_message(self, relayer: str, msg_id: str) -> Tuple[bool, str]:
        with self._lock:
            if relayer not in self._relayers:
                return False, "Not a registered relayer"
            msg = self._messages.get(msg_id)
            if not msg or msg.status != "pending":
                return False, "Message not found or not pending"
            msg.status  = "relayed"
            msg.relayer = relayer
            return True, f"Relayed to {msg.dest_chain}"

    def confirm_delivery(self, msg_id: str,
                          receipt_hash: str) -> Tuple[bool, str]:
        with self._lock:
            msg = self._messages.get(msg_id)
            if not msg:
                return False, "Not found"
            if msg.status != "relayed":
                return False, f"Wrong status: {msg.status}"
            msg.status = "delivered"
            return True, f"Message delivered to {msg.dest_chain}"

    def messages_for(self, address: str) -> List[dict]:
        return [m.to_dict() for m in self._messages.values()
                if m.sender == address or m.recipient == address]

    def router_stats(self) -> dict:
        with self._lock:
            by_chain   = {}
            by_status  = {}
            for m in self._messages.values():
                by_chain[m.dest_chain]  = by_chain.get(m.dest_chain, 0) + 1
                by_status[m.status]     = by_status.get(m.status, 0) + 1
        return {
            "total_messages":  len(self._messages),
            "by_chain":        by_chain,
            "by_status":       by_status,
            "relayers":        len(self._relayers),
        }


# ---- HDWalletV2
class HDWalletV2:
    """
    HD Wallet v2 with multi-account support.
    BIP-44: m/purpose'/coin'/account'/change/index
    NEBULA coin type: 2025'
    """

    COIN_TYPE = 2025

    def __init__(self, mnemonic: str = None):
        if mnemonic is None:
            mnemonic = BIP39.generate_mnemonic()
        self.mnemonic    = mnemonic
        self._seed       = BIP39.mnemonic_to_seed(mnemonic)
        self._master     = HDKey.from_seed(self._seed)
        self._accounts:  Dict[int, WalletAccount] = {}
        self._labels:    Dict[str, str]           = {}  # addr -> label
        self.create_account(0)   # default account

    def create_account(self, account_idx: int = None) -> WalletAccount:
        if account_idx is None:
            account_idx = max(self._accounts.keys(), default=-1) + 1
        path     = f"m/44'/{self.COIN_TYPE}'/{account_idx}'"
        acct_key = self._master.derive_path(path)
        ext_keys = [acct_key.derive_path(f"0/{i}") for i in range(GAP_LIMIT)]
        int_keys = [acct_key.derive_path(f"1/{i}") for i in range(GAP_LIMIT)]
        xpub     = base58check_encode(
            Secp256k1.pubkey_to_bytes(acct_key.pubkey) + account_idx.to_bytes(4, 'big'), 0x04)
        acct = WalletAccount(
            account_index = account_idx,
            addr_type     = AddressType.P2PKH,
            xpub          = xpub,
            external_keys = ext_keys,
            internal_keys = int_keys,
            label         = f"Account {account_idx}",
        )
        self._accounts[account_idx] = acct
        return acct

    def account(self, idx: int = 0) -> Optional[WalletAccount]:
        return self._accounts.get(idx)

    def receive_address(self, account_idx: int = 0) -> str:
        acct = self._accounts.get(account_idx)
        return acct.get_receive_address() if acct else ""

    def change_address(self, account_idx: int = 0) -> str:
        acct = self._accounts.get(account_idx)
        return acct.get_change_address() if acct else ""

    def label_address(self, address: str, label: str):
        self._labels[address] = label

    def get_label(self, address: str) -> str:
        return self._labels.get(address, "")

    def all_addresses(self) -> List[str]:
        addrs = []
        for acct in self._accounts.values():
            addrs.extend(acct.all_addresses())
        return addrs

    def wallet_summary(self, utxo: 'UTXOSet') -> dict:
        addrs = self.all_addresses()
        total = sum(utxo.balance(a) for a in addrs)
        return {
            "accounts":       len(self._accounts),
            "total_addresses": len(addrs),
            "total_balance":   f"{total/10**DECIMALS:.9f} NBL",
            "mnemonic_words":  len(self.mnemonic.split()),
        }

    def export_xpub(self, account_idx: int = 0) -> str:
        """Export account extended public key (watch-only)."""
        path  = f"m/44'/{self.COIN_TYPE}'/{account_idx}'"
        key   = self._master.derive_path(path)
        data  = Secp256k1.pubkey_to_bytes(key.pubkey) + account_idx.to_bytes(4, 'big')
        return base58check_encode(data, 0x04)

    def sign_message(self, account_idx: int, addr_idx: int,
                      message: str) -> str:
        """Sign an arbitrary message with a wallet key."""
        path    = f"m/44'/{self.COIN_TYPE}'/{account_idx}'/0/{addr_idx}"
        key     = self._master.derive_path(path)
        msg_h   = hashlib.sha256(
            b"\x18NEBULA Signed Message:\n" + message.encode()
        ).digest()
        r, s    = Secp256k1.sign(key.key, sha256d(msg_h))
        sig_der = Secp256k1.sig_to_der(r, s)
        return sig_der.hex()


# ---- PeerDiscoveryMethod
class PeerDiscoveryMethod(_enum.Enum):
    DNS_SEED     = "dns_seed"
    HARDCODED    = "hardcoded"
    PEER_GOSSIP  = "peer_gossip"
    LOCAL_NET    = "local_net"
    TOR          = "tor"
