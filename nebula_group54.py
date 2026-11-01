"""NEBULA group54 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. LiquidityIncentiveProgram  (orig. lines 83766-83813)
   2. CrossChainMessageHub  (orig. lines 83820-83875)
   3. ValidatorDelegationV2  (orig. lines 83882-83926)
   4. DeFiPassportV2  (orig. lines 83933-84005)
   5. OnChainStorageV2  (orig. lines 84012-84083)
   6. AdvancedMiningEngine  (orig. lines 84096-84176)
   7. NetworkStatsV2  (orig. lines 84183-84221)
   8. SmartContractV3  (orig. lines 84228-84287)
   9. DeFiPositionsV2  (orig. lines 84294-84349)
  10. ValidatorMetrics  (orig. lines 84356-84410)
  11. MultiAssetStaking  (orig. lines 84417-84480)
  12. ProtocolBenchmark  (orig. lines 84487-84546)
  13. LendingLiquidationBot  (orig. lines 84553-84610)
  14. ComposableTransaction  (orig. lines 84617-84647)
  15. ComposabilityEngineV3  (orig. lines 84650-84684)
  16. EcosystemHealthMonitor  (orig. lines 84691-84745)
  17. ChainEvent  (orig. lines 84758-84765)
  18. ChainEventEmitterV2  (orig. lines 84767-84811)
  19. RewardsEngineV3  (orig. lines 84818-84862)
  20. ProtocolRevenue  (orig. lines 84869-84910)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): ContractState, NEBULAWallet, Secp256k1
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

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

DIFFICULTY_WINDOW      = 2016                           # blocks per retarget

MAX_TARGET             = 0x0fffff * (256 ** ((0x1e if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d) - 3))   # [v10.24]   # bits_to_target(INITIAL_BITS) — max allowed PoW target

MAX_TX_PER_BLOCK       = 3000

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

PUBKEY_ADDRESS_VERSION  = 0x35   # N prefix for mainnet NBL addresses

def sha256d(data: bytes) -> bytes:
    """Double SHA-256 — used everywhere in Bitcoin/NEBULA"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def hash160(data: bytes) -> bytes:
    """RIPEMD160(SHA256(data)) — used for addresses"""
    h = hashlib.new('ripemd160')
    h.update(hashlib.sha256(data).digest())
    return h.digest()

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

def pubkey_to_address(pubkey: bytes) -> str:
    """P2PKH address (version PUBKEY_ADDRESS_VERSION) from a serialized public key."""
    if not isinstance(pubkey, (bytes, bytearray)):
        pubkey = Secp256k1.pubkey_to_bytes(pubkey)
    return base58check_encode(hash160(bytes(pubkey)), PUBKEY_ADDRESS_VERSION)

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


# ---- LiquidityIncentiveProgram
class LiquidityIncentiveProgram:
    """
    Incentivizes liquidity provision in NEBULA DEX.
    LPs earn extra NBL rewards on top of trading fees.
    """

    WEEKLY_BUDGET = 10_000 * 10**DECIMALS   # 10,000 NBL per week

    def __init__(self, blockchain: 'NEBULABlockchain',
                  dex: 'NEBULADex'):
        self._bc      = blockchain
        self._dex     = dex
        self._week_start = blockchain.height
        self._lp_rewards: Dict[str, int] = {}
        self._lock     = threading.RLock()

    def allocate_weekly(self) -> dict:
        """Allocate weekly rewards proportional to LP share."""
        with self._lock:
            cur = self._bc.height
            if cur - self._week_start < 144 * 7:
                return {"allocated": False}
            # Each pool gets share based on volume (simplified)
            pools      = list(self._dex._pools.values())
            n          = len(pools) or 1
            per_pool   = self.WEEKLY_BUDGET // n
            allocated  = {}
            for pool in pools:
                lps = list(pool.lp_shares.keys()) if hasattr(pool, 'lp_shares') else []
                for lp in lps:
                    self._lp_rewards[lp] = (
                        self._lp_rewards.get(lp, 0) + per_pool // max(1, len(lps)))
                allocated[pool.pool_id] = per_pool
            self._week_start = cur
            return {"allocated": True, "breakdown": allocated}

    def claim_rewards(self, lp: str) -> Tuple[bool, int]:
        with self._lock:
            amount = self._lp_rewards.pop(lp, 0)
            return amount > 0, amount

    def incentive_stats(self) -> dict:
        total_pending = sum(self._lp_rewards.values())
        return {
            "weekly_budget":  f"{self.WEEKLY_BUDGET/10**DECIMALS:.0f} NBL",
            "pending_claims": f"{total_pending/10**DECIMALS:.3f}",
            "lp_recipients":  len(self._lp_rewards),
        }


# ---- CrossChainMessageHub
class CrossChainMessageHub:
    """
    Central hub for all cross-chain messages on NEBULA.
    Routes messages to appropriate handlers.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._handlers: Dict[str, Callable] = {}
        self._inbox:    List[dict]          = []
        self._outbox:   List[dict]          = []
        self._lock      = threading.RLock()

    def register_handler(self, msg_type: str,
                           handler: Callable):
        self._handlers[msg_type] = handler

    def receive(self, src_chain: str, msg_type: str,
                 payload: dict) -> Tuple[bool, Any]:
        with self._lock:
            self._inbox.append({
                "src":     src_chain,
                "type":    msg_type,
                "payload": payload,
                "ts":      time.time(),
            })
        handler = self._handlers.get(msg_type)
        if handler:
            try:
                result = handler(src_chain, payload)
                return True, result
            except Exception as e:
                return False, str(e)
        return False, "No handler"

    def send(self, dest_chain: str, msg_type: str,
              payload: dict) -> str:
        with self._lock:
            mid = hashlib.sha256(
                f"XCM:{dest_chain}:{msg_type}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._outbox.append({
                "id":   mid,
                "dest": dest_chain,
                "type": msg_type,
                "payload": payload,
                "status":  "queued",
            })
            return mid

    def hub_stats(self) -> dict:
        return {
            "inbox":    len(self._inbox),
            "outbox":   len(self._outbox),
            "handlers": len(self._handlers),
        }


# ---- ValidatorDelegationV2
class ValidatorDelegationV2:
    """Enhanced validator delegation with rewards tracking."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._dels:    Dict[str, Dict[str, int]] = {}  # validator -> {delegator: amount}
        self._rewards: Dict[str, int]            = {}
        self._lock     = threading.RLock()

    def delegate(self, delegator: str, validator: str,
                  amount: int) -> Tuple[bool, str]:
        with self._lock:
            if self._bc.utxo.balance(delegator) < amount:
                return False, "Insufficient balance"
            if validator not in self._dels:
                self._dels[validator] = {}
            self._dels[validator][delegator] = (
                self._dels[validator].get(delegator, 0) + amount)
            return True, f"Delegated {amount/10**DECIMALS:.6f} NBL"

    def redelegate(self, delegator: str, from_v: str,
                    to_v: str, amount: int) -> Tuple[bool, str]:
        with self._lock:
            current = self._dels.get(from_v, {}).get(delegator, 0)
            if current < amount:
                return False, "Insufficient delegation"
            self._dels[from_v][delegator] -= amount
            if self._dels[from_v][delegator] == 0:
                del self._dels[from_v][delegator]
            if to_v not in self._dels:
                self._dels[to_v] = {}
            self._dels[to_v][delegator] = (
                self._dels[to_v].get(delegator, 0) + amount)
            return True, f"Redelegated from {from_v[:8]} to {to_v[:8]}"

    def total_delegated(self, validator: str) -> int:
        return sum(self._dels.get(validator, {}).values())

    def delegation_v2_stats(self) -> dict:
        total = sum(
            sum(d.values()) for d in self._dels.values())
        return {
            "total_delegated_nbl": f"{total/10**DECIMALS:.3f}",
            "validators":          len(self._dels),
        }


# ---- DeFiPassportV2
class DeFiPassportV2:
    """
    DeFi Passport v2 with on-chain reputation and achievements.
    Non-transferable soul-bound NFT representing DeFi activity.
    """

    ACHIEVEMENTS = {
        "first_swap":      "Completed first DEX swap",
        "diamond_hands":   "Held NBL for 1 year",
        "governance_guru": "Voted on 10+ proposals",
        "lp_provider":     "Provided $10k+ liquidity",
        "nft_collector":   "Owns 10+ NFTs",
        "bridge_pioneer":  "Used cross-chain bridge",
        "staking_master":  "Staked for 180+ days",
        "defi_veteran":    "Used 5+ protocols",
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._passports: Dict[str, dict] = {}
        self._lock     = threading.RLock()

    def get_passport(self, address: str) -> dict:
        with self._lock:
            if address not in self._passports:
                self._passports[address] = {
                    "address":      address,
                    "achievements": [],
                    "score":        0,
                    "level":        1,
                    "created":      time.time(),
                }
            return self._passports[address]

    def award_achievement(self, address: str,
                           achievement: str) -> bool:
        with self._lock:
            if achievement not in self.ACHIEVEMENTS:
                return False
            pp = self.get_passport(address)
            if achievement in pp["achievements"]:
                return False
            pp["achievements"].append(achievement)
            pp["score"] += 100
            pp["level"]  = 1 + pp["score"] // 500
            return True

    def check_auto_achievements(self, address: str) -> List[str]:
        awarded = []
        bal     = self._bc.utxo.balance(address)
        if bal > 0:
            if self.award_achievement(address, "diamond_hands"):
                awarded.append("diamond_hands")
        return awarded

    def leaderboard(self, n: int = 10) -> List[dict]:
        with self._lock:
            sorted_pp = sorted(
                self._passports.values(),
                key=lambda p: -p["score"])[:n]
        return [{"rank": i+1, "address": p["address"],
                 "score": p["score"], "level": p["level"],
                 "achievements": len(p["achievements"])}
                for i, p in enumerate(sorted_pp)]

    def passport_v2_stats(self) -> dict:
        with self._lock:
            total_achiev = sum(len(p["achievements"])
                               for p in self._passports.values())
        return {
            "passports":   len(self._passports),
            "achievements": total_achiev,
        }


# ---- OnChainStorageV2
class OnChainStorageV2:
    """
    On-chain storage v2 with access control and namespacing.
    Supports public/private data with encryption hints.
    """

    MAX_ENTRY_SIZE  = 10_240   # 10KB
    STORAGE_FEE_PER_KB = MIN_TX_FEE

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._public: Dict[str, dict]            = {}   # key -> {value, owner, ts}
        self._private: Dict[str, Dict[str, Any]] = {}   # owner -> {key: value}
        self._acl:    Dict[str, Set[str]]        = {}   # key -> allowed addresses
        self._lock    = threading.RLock()

    def write_public(self, owner: str, key: str,
                      value: Any, ttl_blocks: int = 0) -> Tuple[bool, str]:
        with self._lock:
            val_bytes = json.dumps(value).encode()
            if len(val_bytes) > self.MAX_ENTRY_SIZE:
                return False, "Value too large"
            fee = len(val_bytes) * self.STORAGE_FEE_PER_KB // 1024
            self._public[key] = {
                "value":   value,
                "owner":   owner,
                "ts":      time.time(),
                "expires": (self._bc.height + ttl_blocks
                             if ttl_blocks > 0 else 0),
                "size":    len(val_bytes),
            }
            return True, f"Stored {len(val_bytes)} bytes at '{key}'"

    def read_public(self, key: str) -> Optional[Any]:
        entry = self._public.get(key)
        if not entry:
            return None
        if entry["expires"] > 0 and self._bc.height > entry["expires"]:
            del self._public[key]
            return None
        return entry["value"]

    def write_private(self, owner: str, key: str,
                       value: Any) -> bool:
        with self._lock:
            if owner not in self._private:
                self._private[owner] = {}
            self._private[owner][key] = value
            return True

    def read_private(self, accessor: str, owner: str,
                      key: str) -> Optional[Any]:
        if accessor != owner:
            allowed = self._acl.get(f"{owner}:{key}", set())
            if accessor not in allowed:
                return None
        return self._private.get(owner, {}).get(key)

    def grant_access(self, owner: str, key: str, accessor: str):
        with self._lock:
            acl_key = f"{owner}:{key}"
            if acl_key not in self._acl:
                self._acl[acl_key] = set()
            self._acl[acl_key].add(accessor)

    def storage_v2_stats(self) -> dict:
        total_size = sum(e.get("size", 0) for e in self._public.values())
        return {
            "public_entries":  len(self._public),
            "private_owners":  len(self._private),
            "total_size_kb":   f"{total_size/1024:.2f}",
        }


# ---- AdvancedMiningEngine
class AdvancedMiningEngine:
    """
    Advanced mining engine with hardware abstraction.
    Supports CPU, GPU, ASIC simulation.
    """

    class HardwareType(_enum.Enum):
        CPU  = "cpu"
        GPU  = "gpu"
        ASIC = "asic"

    HASH_RATES = {
        HardwareType.CPU:  10_000,       # 10 KH/s
        HardwareType.GPU:  500_000,      # 500 KH/s
        HardwareType.ASIC: 100_000_000,  # 100 MH/s
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  miner_address: str):
        self._bc      = blockchain
        self._miner   = miner_address
        self._hardware: List[dict] = []
        self._total_blocks = 0
        self._total_rewards = 0

    def add_hardware(self, hw_type: HardwareType,
                      count: int = 1):
        self._hardware.append({
            "type":      hw_type.value,
            "count":     count,
            "hash_rate": self.HASH_RATES[hw_type] * count,
        })

    def total_hash_rate(self) -> int:
        return sum(h["hash_rate"] for h in self._hardware)

    def simulate_mine(self, blocks: int = 1) -> List[dict]:
        """Simulate mining blocks."""
        results = []
        for _ in range(blocks):
            h       = self._bc.height + 1
            reward  = mining_reward(h)
            self._total_blocks  += 1
            self._total_rewards += reward
            results.append({
                "height":  h,
                "reward":  f"{reward/10**DECIMALS:.9f} NBL",
                "miner":   self._miner,
            })
        return results

    def profitability(self, nbl_price_usd: float,
                       power_cost_kwh: float = 0.05) -> dict:
        hr      = self.total_hash_rate()
        h       = self._bc.height
        diff    = MAX_TARGET / max(1, bits_to_target(self._bc.tip.header.bits))
        daily_nbl = hr * 86400 / (diff * 2**32) * mining_reward(h) / 10**DECIMALS
        revenue = daily_nbl * nbl_price_usd
        # Estimate power (simplified)
        power_w = sum(
            h["count"] * (100 if h["type"] == "cpu" else
                          300 if h["type"] == "gpu" else 1500)
            for h in self._hardware
        )
        cost    = power_w / 1000 * 24 * power_cost_kwh
        return {
            "hash_rate":     f"{hr/1e6:.2f} MH/s",
            "daily_nbl":     f"{daily_nbl:.6f}",
            "daily_revenue": f"${revenue:.2f}",
            "daily_cost":    f"${cost:.2f}",
            "daily_profit":  f"${revenue-cost:.2f}",
        }

    def mining_stats(self) -> dict:
        return {
            "miner":         self._miner,
            "blocks":        self._total_blocks,
            "rewards_nbl":   f"{self._total_rewards/10**DECIMALS:.6f}",
            "hardware":      self._hardware,
            "hash_rate_mhs": f"{self.total_hash_rate()/1e6:.2f}",
        }


# ---- NetworkStatsV2
class NetworkStatsV2:
    """Enhanced network statistics for NEBULA."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  p2p: 'P2PNetwork' = None):
        self._bc  = blockchain
        self._p2p = p2p
        self._snapshots: List[dict] = []

    def snapshot(self) -> dict:
        bc = self._bc
        snap = {
            "ts":        time.time(),
            "height":    bc.height,
            "supply":    bc.utxo.total_supply() / 10**DECIMALS,
            "mempool":   bc.mempool.size(),
            "utxos":     bc.utxo.size(),
        }
        self._snapshots.append(snap)
        return snap

    def tps_estimate(self, window_secs: int = 600) -> float:
        """Estimate TPS from mempool."""
        mp_size = self._bc.mempool.size()
        return mp_size / max(1, TARGET_BLOCK_TIME) * MAX_TX_PER_BLOCK / 1000

    def network_utilization(self) -> float:
        mp_size  = self._bc.mempool.size()
        capacity = MAX_TX_PER_BLOCK * (1000 / TARGET_BLOCK_TIME)
        return min(1.0, mp_size / max(1, capacity))

    def full_network_stats(self) -> dict:
        snap = self.snapshot()
        return {
            **snap,
            "tps_estimate":  f"{self.tps_estimate():.2f}",
            "utilization":   f"{self.network_utilization()*100:.1f}%",
            "avg_block_time": f"{TARGET_BLOCK_TIME}s",
        }


# ---- SmartContractV3
class SmartContractV3:
    """
    Smart contract v3 — event-driven with upgradeable proxy pattern.
    """

    def __init__(self, contract_id: str, owner: str,
                  blockchain: 'NEBULABlockchain'):
        self.contract_id = contract_id
        self.owner       = owner
        self._bc         = blockchain
        self._state      = ContractState()
        self._events:    List[dict] = []
        self._version    = 1
        self._paused     = False
        self._abi:       Dict[str, Callable] = {}

    def register(self, fn_name: str, fn: Callable):
        self._abi[fn_name] = fn

    def call(self, caller: str, fn_name: str,
              args: dict = None, value: int = 0) -> Tuple[Any, List[dict]]:
        if self._paused:
            raise RuntimeError("Contract is paused")
        fn = self._abi.get(fn_name)
        if not fn:
            raise ValueError(f"Function not found: {fn_name}")
        prev_n = len(self._state._events)
        result = fn(caller, args or {}, value)
        new_events = self._state._events[prev_n:]
        self._events.extend(new_events)
        return result, new_events

    def upgrade(self, new_owner: str,
                 new_version: int) -> bool:
        if new_owner != self.owner:
            return False
        self._version += 1
        return True

    def pause(self, caller: str) -> bool:
        if caller != self.owner:
            return False
        self._paused = True
        return True

    def unpause(self, caller: str) -> bool:
        if caller != self.owner:
            return False
        self._paused = False
        return True

    def contract_v3_info(self) -> dict:
        return {
            "contract_id": self.contract_id,
            "owner":       self.owner,
            "version":     self._version,
            "paused":      self._paused,
            "functions":   list(self._abi.keys()),
            "events":      len(self._events),
        }


# ---- DeFiPositionsV2
class DeFiPositionsV2:
    """Enhanced DeFi position tracker v2."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._positions: Dict[str, List[dict]] = {}
        self._lock    = threading.RLock()

    def add(self, owner: str, protocol: str,
             pos_type: str, asset: str,
             amount: float, apy: float = 0,
             metadata: dict = None) -> str:
        with self._lock:
            pos_id = hashlib.sha256(
                f"POS2:{owner}:{protocol}:{asset}:{time.time()}".encode()
            ).hexdigest()[:12]
            if owner not in self._positions:
                self._positions[owner] = []
            price = (self._oracle.price(f"{asset}/USD")
                     if self._oracle else 0.01) or 0.01
            self._positions[owner].append({
                "pos_id":   pos_id,
                "protocol": protocol,
                "type":     pos_type,
                "asset":    asset,
                "amount":   amount,
                "apy":      apy,
                "value_usd": amount * price,
                "metadata": metadata or {},
                "added":    time.time(),
            })
            return pos_id

    def summary(self, owner: str) -> dict:
        with self._lock:
            positions = self._positions.get(owner, [])
        total_usd  = sum(p["value_usd"] for p in positions)
        annual_usd = sum(p["value_usd"] * p["apy"] for p in positions)
        return {
            "owner":        owner,
            "positions":    len(positions),
            "total_usd":    f"${total_usd:.2f}",
            "annual_yield": f"${annual_usd:.2f}",
            "blended_apy":  f"{annual_usd/max(0.01, total_usd)*100:.2f}%",
        }

    def remove(self, owner: str, pos_id: str) -> bool:
        with self._lock:
            positions = self._positions.get(owner, [])
            for i, p in enumerate(positions):
                if p["pos_id"] == pos_id:
                    positions.pop(i)
                    return True
            return False


# ---- ValidatorMetrics
class ValidatorMetrics:
    """Comprehensive metrics for NEBULA validators."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._metrics:   Dict[str, dict] = {}
        self._lock        = threading.RLock()

    def record_block(self, validator: str, latency_ms: float,
                      block_size: int):
        with self._lock:
            if validator not in self._metrics:
                self._metrics[validator] = {
                    "blocks":     0,
                    "total_lat":  0.0,
                    "total_size": 0,
                    "uptime":     1.0,
                    "slashes":    0,
                }
            m = self._metrics[validator]
            m["blocks"]     += 1
            m["total_lat"]  += latency_ms
            m["total_size"] += block_size

    def slash(self, validator: str):
        with self._lock:
            if validator in self._metrics:
                self._metrics[validator]["slashes"] += 1
                self._metrics[validator]["uptime"] *= 0.95

    def score(self, validator: str) -> float:
        m = self._metrics.get(validator)
        if not m:
            return 0.0
        lat_score  = max(0, 100 - m["total_lat"] / max(1, m["blocks"]))
        slash_pen  = m["slashes"] * 10
        return max(0, m["uptime"] * 100 * lat_score / 100 - slash_pen)

    def leaderboard(self, n: int = 10) -> List[dict]:
        with self._lock:
            vals = [(v, self.score(v)) for v in self._metrics]
        return [
            {"rank": i+1, "validator": v[:12], "score": f"{s:.1f}",
             "blocks": self._metrics[v]["blocks"]}
            for i, (v, s) in enumerate(
                sorted(vals, key=lambda x: -x[1])[:n])
        ]

    def metrics_stats(self) -> dict:
        with self._lock:
            total_blocks = sum(m["blocks"] for m in self._metrics.values())
        return {
            "validators":    len(self._metrics),
            "total_blocks":  total_blocks,
        }


# ---- MultiAssetStaking
class MultiAssetStaking:
    """
    Stake multiple assets to earn NBL rewards.
    Weighted basket staking.
    """

    ACCEPTED_ASSETS = {
        "NBL":  1.0,   # base weight
        "USDT": 0.3,
        "WBTC": 2.0,
        "WETH": 1.5,
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._stakes: Dict[str, Dict[str, float]] = {}
        self._rewards: Dict[str, int]             = {}
        self._lock    = threading.RLock()

    def stake_asset(self, staker: str, asset: str,
                     amount: float) -> Tuple[bool, str]:
        with self._lock:
            if asset not in self.ACCEPTED_ASSETS:
                return False, f"Asset {asset} not accepted"
            if staker not in self._stakes:
                self._stakes[staker] = {}
            self._stakes[staker][asset] = (
                self._stakes[staker].get(asset, 0) + amount)
            return True, f"Staked {amount:.4f} {asset}"

    def weighted_value(self, staker: str) -> float:
        total = 0.0
        for asset, amount in self._stakes.get(staker, {}).items():
            weight = self.ACCEPTED_ASSETS.get(asset, 0)
            price  = (self._oracle.price(f"{asset}/USD")
                      if self._oracle else 1.0) or 1.0
            total += amount * weight * price
        return total

    def accrue_rewards(self, apy: float = 0.12) -> dict:
        total_accrued = 0
        with self._lock:
            for staker in self._stakes:
                val    = self.weighted_value(staker)
                reward = int(val * apy / (365 * 144) * 10**DECIMALS)
                self._rewards[staker] = (
                    self._rewards.get(staker, 0) + reward)
                total_accrued += reward
        return {"accrued_nbl": f"{total_accrued/10**DECIMALS:.6f}"}

    def claim(self, staker: str) -> Tuple[bool, int]:
        with self._lock:
            amount = self._rewards.pop(staker, 0)
            return amount > 0, amount

    def multi_staking_stats(self) -> dict:
        total_val = sum(self.weighted_value(s) for s in self._stakes)
        return {
            "stakers":        len(self._stakes),
            "total_weighted": f"${total_val:.2f}",
            "assets":         list(self.ACCEPTED_ASSETS.keys()),
        }


# ---- ProtocolBenchmark
class ProtocolBenchmark:
    """Benchmarks NEBULA protocol performance."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._results: Dict[str, dict] = {}

    def bench_wallet_generation(self, n: int = 100) -> dict:
        start = time.time()
        addrs = [NEBULAWallet.generate().first_address for _ in range(n)]
        elapsed = time.time() - start
        result  = {
            "operation":  "wallet_generation",
            "count":      n,
            "total_ms":   f"{elapsed*1000:.1f}",
            "per_ms":     f"{elapsed*1000/n:.2f}",
            "per_sec":    f"{n/elapsed:.0f}",
        }
        self._results["wallet_gen"] = result
        return result

    def bench_hash_operations(self, n: int = 10_000) -> dict:
        start = time.time()
        for i in range(n):
            hashlib.sha256(i.to_bytes(8, 'big')).hexdigest()
        elapsed = time.time() - start
        result  = {
            "operation": "sha256",
            "count":     n,
            "total_ms":  f"{elapsed*1000:.1f}",
            "per_sec":   f"{n/elapsed:.0f} ops/s",
        }
        self._results["sha256"] = result
        return result

    def bench_address_generation(self, n: int = 1000) -> dict:
        start = time.time()
        for i in range(n):
            priv  = secrets.randbelow(Secp256k1.ORDER - 1) + 1
            pub   = Secp256k1.pubkey_from_int(priv, compressed=True)
            addr  = pubkey_to_address(pub)
        elapsed = time.time() - start
        result  = {
            "operation": "address_generation",
            "count":     n,
            "total_ms":  f"{elapsed*1000:.1f}",
            "per_sec":   f"{n/elapsed:.0f}",
        }
        self._results["addr_gen"] = result
        return result

    def run_all_benchmarks(self) -> dict:
        print("\n⚡ Running NEBULA benchmarks...")
        r1 = self.bench_hash_operations(50_000)
        print(f"  SHA-256: {r1['per_sec']}")
        r2 = self.bench_wallet_generation(50)
        print(f"  Wallet gen: {r2['per_sec']} wallets/s")
        r3 = self.bench_address_generation(100)
        print(f"  Addr gen: {r3['per_sec']} addrs/s")
        return self._results


# ---- LendingLiquidationBot
class LendingLiquidationBot:
    """
    Automated liquidation bot for NEBULA lending protocols.
    Monitors positions and executes profitable liquidations.
    """

    LIQUIDATION_BONUS = 0.05
    MIN_PROFIT_NBL    = 1.0

    def __init__(self, blockchain: 'NEBULABlockchain',
                  lending: 'LendingProtocol' = None,
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._lending = lending
        self._oracle  = oracle
        self._liq_count = 0
        self._profit    = 0.0

    def scan_positions(self) -> List[dict]:
        """Find liquidatable positions."""
        if not self._lending:
            return []
        underwater = []
        for addr, loan in self._lending._loans.items():
            if not loan.get("active"):
                continue
            price = (self._oracle.price("NBL/USD")
                     if self._oracle else 0.01) or 0.01
            col_usd  = loan.get("collateral", 0) / 10**DECIMALS * price
            debt_usd = loan.get("amount", 0) / 10**DECIMALS
            hf = col_usd * 0.8 / debt_usd if debt_usd > 0 else 999
            if hf < 1.0:
                profit = loan.get("collateral", 0) * self.LIQUIDATION_BONUS / 10**DECIMALS
                underwater.append({
                    "borrower": addr,
                    "hf":       hf,
                    "debt":     loan.get("amount", 0),
                    "collateral": loan.get("collateral", 0),
                    "profit":   profit,
                })
        return sorted(underwater, key=lambda x: -x["profit"])

    def execute_liquidations(self) -> int:
        positions = self.scan_positions()
        executed  = 0
        for pos in positions:
            if pos["profit"] >= self.MIN_PROFIT_NBL:
                self._liq_count += 1
                self._profit    += pos["profit"]
                executed        += 1
        return executed

    def bot_stats(self) -> dict:
        return {
            "liquidations":   self._liq_count,
            "total_profit":   f"{self._profit:.3f} NBL",
            "bonus_rate":     f"{self.LIQUIDATION_BONUS*100:.0f}%",
        }


# ---- ComposableTransaction
class ComposableTransaction:
    """
    A composable transaction that chains multiple DeFi operations.
    Atomic execution — all succeed or all fail.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc   = blockchain
        self._ops: List[Tuple[str, Callable, dict]] = []
        self._executed = False

    def add_op(self, name: str, fn: Callable, args: dict = None):
        self._ops.append((name, fn, args or {}))
        return self   # fluent interface

    def execute(self) -> Tuple[bool, List[dict]]:
        if self._executed:
            return False, [{"error": "Already executed"}]
        results = []
        for name, fn, args in self._ops:
            try:
                result = fn(**args)
                results.append({"op": name, "result": result, "ok": True})
            except Exception as e:
                results.append({"op": name, "error": str(e), "ok": False})
                return False, results
        self._executed = True
        return True, results

    def ops_count(self) -> int:
        return len(self._ops)


# ---- ComposabilityEngineV3
class ComposabilityEngineV3:
    """Execute complex multi-step DeFi strategies atomically."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._txs:  List[ComposableTransaction] = []
        self._lock  = threading.RLock()

    def new_tx(self) -> ComposableTransaction:
        tx = ComposableTransaction(self._bc)
        with self._lock:
            self._txs.append(tx)
        return tx

    def execute_strategy(self, user: str, strategy: str,
                          amount_nbl: float,
                          dex: 'NEBULADex' = None,
                          staking: 'StakingEngine' = None) -> dict:
        """Execute a named strategy atomically."""
        tx     = self.new_tx()
        amount = int(amount_nbl * 10**DECIMALS)
        if strategy == "swap_and_stake" and dex and staking:
            tx.add_op("swap", lambda: dex.swap_amm(
                user, "USDT", "NBL", amount))
            tx.add_op("stake", lambda: staking.stake(user, amount // 2))
        elif strategy == "full_liquid_stake" and staking:
            tx.add_op("stake", lambda: staking.stake(user, amount))
        ok, results = tx.execute()
        return {"strategy": strategy, "ok": ok, "steps": len(results)}

    def composability_v3_stats(self) -> dict:
        return {
            "total_txs":   len(self._txs),
            "executed":    sum(1 for tx in self._txs if tx._executed),
        }


# ---- EcosystemHealthMonitor
class EcosystemHealthMonitor:
    """
    Monitors the overall health of the NEBULA ecosystem.
    Aggregates signals from all protocols.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._signals:  List[dict] = []
        self._lock      = threading.RLock()

    def record_signal(self, source: str, metric: str,
                       value: float, good_threshold: float,
                       bad_threshold: float):
        with self._lock:
            status = ("good" if value >= good_threshold else
                      "bad"  if value <= bad_threshold  else "neutral")
            self._signals.append({
                "source":  source,
                "metric":  metric,
                "value":   value,
                "status":  status,
                "ts":      time.time(),
            })

    def auto_record(self) -> dict:
        bc   = self._bc
        sigs = [
            ("chain",      "height",    bc.height,          100,    0),
            ("mempool",    "size",       bc.mempool.size(),  0,      50_000),
            ("utxo",       "size",       bc.utxo.size(),     100,    0),
            ("supply",     "pct_mined",  bc.utxo.total_supply()/max(1,MAX_SUPPLY)*100, 0, 99),
        ]
        for source, metric, val, good, bad in sigs:
            self.record_signal(source, metric, val, good, bad)
        recent = self._signals[-20:]
        good   = sum(1 for s in recent if s["status"] == "good")
        bad    = sum(1 for s in recent if s["status"] == "bad")
        health = "EXCELLENT" if bad == 0 else \
                 "GOOD" if bad <= 2 else \
                 "DEGRADED" if bad <= 5 else "CRITICAL"
        return {
            "health":       health,
            "good_signals": good,
            "bad_signals":  bad,
            "total":        len(recent),
        }

    def health_report(self) -> dict:
        status = self.auto_record()
        return {
            **status,
            "chain_height": self._bc.height,
            "timestamp":    time.time(),
        }


# ---- ChainEvent
class ChainEvent(_enum.Enum):
    BLOCK_MINED       = "block_mined"
    TX_CONFIRMED      = "tx_confirmed"
    HALVING           = "halving"
    DIFFICULTY_ADJ    = "difficulty_adj"
    LARGE_TX          = "large_tx"
    ADDR_ACTIVATED    = "address_activated"
    CONTRACT_DEPLOYED = "contract_deployed"


# ---- ChainEventEmitterV2
class ChainEventEmitterV2:
    """Emits and handles chain-level events."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._handlers: Dict[ChainEvent, List[Callable]] = {}
        self._history:  List[dict] = []
        self._lock      = threading.RLock()

    def on(self, event: ChainEvent, handler: Callable):
        with self._lock:
            if event not in self._handlers:
                self._handlers[event] = []
            self._handlers[event].append(handler)

    def emit(self, event: ChainEvent, data: dict = None):
        record = {"event": event.value, "data": data or {},
                  "block": self._bc.height, "ts": time.time()}
        with self._lock:
            self._history.append(record)
            handlers = list(self._handlers.get(event, []))
        for h in handlers:
            try:
                h(data or {})
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in ChainEventEmitterV2.emit", exc_info=True)

    def check_special_events(self):
        h = self._bc.height
        if h > 0 and h % HALVING_INTERVAL == 0:
            self.emit(ChainEvent.HALVING, {"height": h, "era": h // HALVING_INTERVAL})
        if h > 0 and h % DIFFICULTY_WINDOW == 0:
            self.emit(ChainEvent.DIFFICULTY_ADJ, {"height": h})

    def event_history(self, event_type: str = None, n: int = 50) -> List[dict]:
        events = list(self._history)
        if event_type:
            events = [e for e in events if e["event"] == event_type]
        return events[-n:]

    def emitter_stats(self) -> dict:
        return {
            "total_events": len(self._history),
            "handlers":     sum(len(v) for v in self._handlers.values()),
        }


# ---- RewardsEngineV3
class RewardsEngineV3:
    """
    Comprehensive rewards engine v3 for NEBULA.
    Combines staking, liquidity, governance, and referral rewards.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._balances: Dict[str, Dict[str, int]] = {}
        self._lock     = threading.RLock()

    def credit(self, address: str, source: str, amount: int):
        with self._lock:
            if address not in self._balances:
                self._balances[address] = {}
            self._balances[address][source] = (
                self._balances[address].get(source, 0) + amount)

    def total_pending(self, address: str) -> int:
        return sum(self._balances.get(address, {}).values())

    def pending_by_source(self, address: str) -> dict:
        return {
            source: f"{amt/10**DECIMALS:.6f}"
            for source, amt in self._balances.get(address, {}).items()
        }

    def claim(self, address: str,
               source: str = None) -> Tuple[bool, int]:
        with self._lock:
            bal = self._balances.get(address, {})
            if source:
                amount = bal.pop(source, 0)
            else:
                amount = sum(bal.values())
                bal.clear()
            return amount > 0, amount

    def rewards_v3_stats(self) -> dict:
        total = sum(
            sum(b.values()) for b in self._balances.values())
        return {
            "participants": len(self._balances),
            "total_pending": f"{total/10**DECIMALS:.6f} NBL",
        }


# ---- ProtocolRevenue
class ProtocolRevenue:
    """
    Tracks and manages NEBULA protocol revenue.
    Revenue from trading fees, interest, liquidations, etc.
    """

    REVENUE_SOURCES = [
        "dex_fees", "lending_interest", "liquidation_fees",
        "bridge_fees", "nft_royalties", "stablecoin_fees",
        "options_premiums", "futures_funding",
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._revenue: Dict[str, int] = {s: 0 for s in self.REVENUE_SOURCES}
        self._history: List[dict]     = []
        self._lock     = threading.RLock()

    def record_revenue(self, source: str, amount: int):
        with self._lock:
            self._revenue[source] = self._revenue.get(source, 0) + amount
            self._history.append({
                "source": source,
                "amount": amount,
                "block":  self._bc.height,
                "ts":     time.time(),
            })

    def total_revenue(self) -> int:
        return sum(self._revenue.values())

    def revenue_by_source(self) -> dict:
        return {k: f"{v/10**DECIMALS:.6f}" for k, v in self._revenue.items()}

    def revenue_report(self) -> dict:
        total = self.total_revenue()
        return {
            "total_revenue_nbl": f"{total/10**DECIMALS:.6f}",
            "by_source":         self.revenue_by_source(),
            "largest_source":    max(self._revenue, key=self._revenue.get)
                                 if self._revenue else "none",
        }
