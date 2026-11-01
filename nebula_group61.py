"""NEBULA group61 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. NEBULANodeManager  (orig. lines 104570-104615)
   2. BlockchainMetrics  (orig. lines 104618-104653)
   3. ChainSyncMonitor  (orig. lines 104656-104682)
   4. TransactionBuilder  (orig. lines 104685-104711)
   5. P2PMessageType  (orig. lines 104857-104873)
   6. P2PMessage_Real  (orig. lines 104875-104947)
   7. RealP2PNode  (orig. lines 104950-105497)
   8. RealMiner  (orig. lines 105508-105792)
   9. NEBULAFullNodeV3  (orig. lines 105802-105985)
  10. P2PKHScript  (orig. lines 106250-106280)
  11. UtreexoProof  (orig. lines 106345-106390)
  12. _UtreexoTree  (orig. lines 106393-106438)
  13. UtreexoForest  (orig. lines 106441-106609)
  14. BIP324Session  (orig. lines 106834-106973)
  15. BIP324Transport  (orig. lines 106977-107047)
  16. BlockFileStore  (orig. lines 107110-107330)
  17. PersistentChain  (orig. lines 107334-107407)
  18. MempoolWithEviction  (orig. lines 107488-107521)
  19. Bip9State  (orig. lines 107590-107595)
  20. Bip9Deployment  (orig. lines 107598-107612)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BlockHeader, MempoolEvictionPolicy, MerkleTree, NEBULABlockchain, NodeRESTAPI, PeerConnection, PersistentBlockStore, PersistentUTXOSet, Script, Transaction, TransactionOutput
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

FOUNDATION_RATE        = 0.02          # 2% per block to foundation

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

DIFFICULTY_WINDOW      = 2016                           # blocks per retarget

MAX_TARGET             = 0x0fffff * (256 ** ((0x1e if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d) - 3))   # [v10.24]   # bits_to_target(INITIAL_BITS) — max allowed PoW target

MAX_TX_PER_BLOCK       = 3000

PROTOCOL_VERSION       = 70015

MAX_PEERS              = 125

MAINNET_MAGIC          = b'\xf9\xbe\xb4\xd9'[::-1]    # repurposed, unique to NBL

TESTNET_MAGIC          = b'\x0b\x11\x09\x07'

PUBKEY_ADDRESS_VERSION  = 0x35   # N prefix for mainnet NBL addresses

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

def base58_decode(s: str) -> bytes:
    count = 0
    for c in s:
        if c == '1': count += 1
        else: break
    num = 0
    for c in s:
        num = num * 58 + BASE58_ALPHABET.index(ord(c))
    result = []
    while num > 0:
        num, rem = divmod(num, 256)
        result.append(rem)
    return bytes([0] * count + list(reversed(result)))

def base58check_encode(payload: bytes, version: int) -> str:
    versioned = bytes([version]) + payload
    checksum  = sha256d(versioned)[:4]
    return base58_encode(versioned + checksum)

def base58check_decode(s: str) -> Tuple[int, bytes]:
    raw      = base58_decode(s)
    version  = raw[0]
    payload  = raw[1:-4]
    checksum = raw[-4:]
    if sha256d(raw[:-4])[:4] != checksum:
        raise ValueError("Invalid base58check checksum")
    return version, payload

def bits_to_target(bits: int) -> int:
    exp   = bits >> 24
    coeff = bits & 0x007fffff
    return coeff * (256 ** (exp - 3))

def target_to_bits(target: int) -> int:
    if target == 0:
        return 0
    nbytes = (target.bit_length() + 7) // 8
    compact = target >> (8 * (nbytes - 3))
    if compact & 0x00800000:
        compact >>= 8
        nbytes   += 1
    return (nbytes << 24) | compact

def mining_reward(height: int) -> int:
    """Block reward with halving schedule.
    FIX: negative height safely returns 0 instead of crashing."""
    if height < 0:
        return 0
    era = height // HALVING_INTERVAL
    if era >= 64:
        return 0
    return INITIAL_BLOCK_REWARD >> era

def _mk_block(header, txs, height=None):
    """Block(header, txs) -- height lives in the header, not in Block()."""
    if height is not None and not getattr(header, 'height', 0):
        header.height = height
    return Block(header, txs)

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

def _pus_sync_from_chain(self, blockchain) -> int:
    """If the persistent set is empty, rebuild it by replaying the chain."""
    if self.size() > 0:
        return 0
    n = 0
    for blk in blockchain._chain:
        if self.apply_block(blk):
            n += 1
    self.flush()
    return n

PING_INTERVAL   = 120   # seconds

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

logger_p2p = logging.getLogger("nebula.p2p")

def calculate_next_bits(blockchain: 'NEBULABlockchain') -> int:
    """Calculate next difficulty bits for a new block."""
    try:
        return blockchain.get_next_bits()
    except AttributeError:
        _NB_SWALLOW_LOG.warning("swallowed AttributeError in calculate_next_bits", exc_info=True)
    h = blockchain.height
    if h == 0 or h % DIFFICULTY_WINDOW != 0:
        return blockchain.tip.header.bits
    # Difficulty adjustment
    try:
        first_block = blockchain.get_block(max(0, h - DIFFICULTY_WINDOW))
        last_block  = blockchain.tip
        if first_block and last_block:
            actual_time = (last_block.header.timestamp -
                           first_block.header.timestamp)
            target_time = DIFFICULTY_WINDOW * TARGET_BLOCK_TIME
            actual_time = max(target_time // 4,
                              min(actual_time, target_time * 4))
            old_target  = bits_to_target(last_block.header.bits)
            new_target  = min(MAX_TARGET,
                              old_target * actual_time // target_time)
            return target_to_bits(new_target)
    except Exception:
        _NB_SWALLOW_LOG.warning("swallowed Exception in calculate_next_bits", exc_info=True)
    return blockchain.tip.header.bits

def _utreexo_parent(left: bytes, right: bytes) -> bytes:
    """Combine two sibling hashes into their parent."""
    return _hl.sha256(_hl.sha256(left + right).digest()).digest()

def _rotl32(v: int, n: int) -> int:
    return ((v << n) | (v >> (32 - n))) & 0xFFFFFFFF

def _chacha20_block(key: bytes, counter: int, nonce: bytes) -> bytes:
    """Single 64-byte ChaCha20 keystream block."""
    def u32(b, i): return _struct.unpack_from('<I', b, i)[0]

    CONST = b'expand 32-byte k'
    c = [u32(CONST, i*4) for i in range(4)]
    k = [u32(key,   i*4) for i in range(8)]
    n = [u32(nonce, i*4) for i in range(3)]

    s = (c + k + [counter & 0xFFFFFFFF] + n)
    w = list(s)

    def qr(a, b, c, d):
        w[a] = (w[a]+w[b]) & 0xFFFFFFFF; w[d] ^= w[a]; w[d] = _rotl32(w[d],16)
        w[c] = (w[c]+w[d]) & 0xFFFFFFFF; w[b] ^= w[c]; w[b] = _rotl32(w[b],12)
        w[a] = (w[a]+w[b]) & 0xFFFFFFFF; w[d] ^= w[a]; w[d] = _rotl32(w[d], 8)
        w[c] = (w[c]+w[d]) & 0xFFFFFFFF; w[b] ^= w[c]; w[b] = _rotl32(w[b], 7)

    for _ in range(10):  # 20 rounds = 10 double-rounds
        qr(0,4, 8,12); qr(1,5, 9,13); qr(2,6,10,14); qr(3,7,11,15)
        qr(0,5,10,15); qr(1,6,11,12); qr(2,7, 8,13); qr(3,4, 9,14)

    out = b''
    for i in range(16):
        out += _struct.pack('<I', (w[i] + s[i]) & 0xFFFFFFFF)
    return out

def _chacha20_encrypt(key: bytes, counter: int, nonce: bytes, data: bytes) -> bytes:
    """ChaCha20 stream cipher (XOR with keystream)."""
    out = bytearray()
    for block_num in range((len(data) + 63) // 64):
        ks = _chacha20_block(key, counter + block_num, nonce)
        start = block_num * 64
        chunk = data[start:start+64]
        out.extend(a ^ b for a, b in zip(chunk, ks))
    return bytes(out)

def _poly1305_mac(key: bytes, data: bytes) -> bytes:
    """Poly1305 one-time MAC."""
    r = int.from_bytes(key[:16], 'little') & 0x0ffffffc0ffffffc0ffffffc0fffffff
    s = int.from_bytes(key[16:], 'little')
    P = (1 << 130) - 5
    acc = 0
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        n = int.from_bytes(chunk + b'\x01', 'little')
        acc = (acc + n) % P
        acc = (r * acc) % P
    acc = (acc + s) % (1 << 128)
    return acc.to_bytes(16, 'little')

def _chacha20poly1305_encrypt(key: bytes, nonce: bytes,
                               plaintext: bytes, aad: bytes = b'') -> bytes:
    """Encrypt + authenticate. Returns ciphertext + 16-byte tag."""
    # Poly1305 key: first block of ChaCha20 with counter=0
    poly_key = _chacha20_block(key, 0, nonce)[:32]
    # Encrypt with counter starting at 1
    ct = _chacha20_encrypt(key, 1, nonce, plaintext)
    # MAC over: aad || pad || ciphertext || pad || len(aad) || len(ct)
    def pad16(b): return b + b'\x00' * ((-len(b)) % 16)
    mac_data = (pad16(aad) + pad16(ct) +
                _struct.pack('<Q', len(aad)) +
                _struct.pack('<Q', len(ct)))
    tag = _poly1305_mac(poly_key, mac_data)
    return ct + tag

def _chacha20poly1305_decrypt(key: bytes, nonce: bytes,
                               ciphertext_tag: bytes, aad: bytes = b'') -> bytes:
    """Decrypt + verify. Raises ValueError on auth failure."""
    if len(ciphertext_tag) < 16:
        raise ValueError("Ciphertext too short")
    ct, tag = ciphertext_tag[:-16], ciphertext_tag[-16:]
    poly_key = _chacha20_block(key, 0, nonce)[:32]
    def pad16(b): return b + b'\x00' * ((-len(b)) % 16)
    mac_data = (pad16(aad) + pad16(ct) +
                _struct.pack('<Q', len(aad)) +
                _struct.pack('<Q', len(ct)))
    expected = _poly1305_mac(poly_key, mac_data)
    if not _hmac.compare_digest(tag, expected):
        raise ValueError("BIP324: MAC authentication failed")
    return _chacha20_encrypt(key, 1, nonce, ct)

def _x25519_clamp(k: bytes) -> int:
    """Clamp a 32-byte scalar per X25519 spec."""
    k = bytearray(k)
    k[0]  &= 248
    k[31] &= 127
    k[31] |= 64
    return int.from_bytes(k, 'little')

def _x25519_mul(k_bytes: bytes, u_bytes: bytes) -> bytes:
    """X25519 scalar multiplication (Montgomery ladder)."""
    P   = (1 << 255) - 19
    A24 = 121665

    def add(P_, Q, p):
        return (P_ + Q) % p
    def mul(a, b, p):
        return (a * b) % p
    def sub(a, b, p):
        return (a - b) % p
    def inv(a, p):
        return pow(a, p - 2, p)

    k = _x25519_clamp(k_bytes)
    u = int.from_bytes(u_bytes, 'little') % P

    x1 = u;  x2 = 1;  z2 = 0;  x3 = u;  z3 = 1
    swap = 0
    for t in range(254, -1, -1):
        kt = (k >> t) & 1
        if kt ^ swap:
            x2, x3 = x3, x2
            z2, z3 = z3, z2
        swap = kt
        A  = add(x2, z2, P);  AA = mul(A, A, P)
        B  = sub(x2, z2, P);  BB = mul(B, B, P)
        E  = sub(AA, BB, P)
        C  = add(x3, z3, P)
        D  = sub(x3, z3, P)
        DA = mul(D, A, P);    CB = mul(C, B, P)
        x3 = pow(add(DA, CB, P), 2, P)
        z3 = mul(u, pow(sub(DA, CB, P), 2, P), P)
        x2 = mul(AA, BB, P)
        z2 = mul(E, add(AA, mul(A24, E, P), P), P)
    if swap:
        x2, x3 = x3, x2
        z2, z3 = z3, z2
    result = (x2 * inv(z2, P)) % P
    return result.to_bytes(32, 'little')

_X25519_BASE = (9).to_bytes(32, 'little')

def x25519_pubkey(privkey: bytes) -> bytes:
    """Derive X25519 public key from private key."""
    return _x25519_mul(privkey, _X25519_BASE)

def x25519_shared(privkey: bytes, their_pubkey: bytes) -> bytes:
    """Compute X25519 shared secret."""
    return _x25519_mul(privkey, their_pubkey)

_BIP324_LABEL   = b"bip324_v1_shared_secret"

_BIP324_SEND_L  = b"initiator_L"

_BIP324_RECV_L  = b"responder_L"

_BIP324_GARBAGE = b"garbage_terminators"

def _hkdf_extract(salt: bytes, ikm: bytes) -> bytes:
    return _hmac.new(salt, ikm, _hashlib.sha256).digest()

def _hkdf_expand(prk: bytes, info: bytes, length: int) -> bytes:
    out = b''
    t   = b''
    for i in range(1, (length + 31) // 32 + 1):
        t = _hmac.new(prk, t + info + bytes([i]), _hashlib.sha256).digest()
        out += t
    return out[:length]

_BLK_MAGIC       = b'\x4e\x42\x4c\x4d'   # "NBLM"

_BLK_MAX_FILE    = 128 * 1024 * 1024      # 128 MB per blk file

_BLK_DIR_DEFAULT = Path("blocks")

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- NEBULANodeManager
class NEBULANodeManager:
    """Manages multiple NEBULA node instances."""

    def __init__(self):
        self._nodes:    dict = {}
        self._lock      = threading.RLock()

    def register_node(self, node_id: str, host: str,
                       port: int, node_type: str = "full") -> bool:
        with self._lock:
            self._nodes[node_id] = {
                "node_id":   node_id,
                "host":      host,
                "port":      port,
                "type":      node_type,
                "online":    True,
                "last_seen": time.time(),
                "version":   "3.0.0",
                "blocks":    0,
            }
            return True

    def update_status(self, node_id: str, height: int,
                       online: bool = True):
        with self._lock:
            node = self._nodes.get(node_id)
            if node:
                node["blocks"]    = height
                node["online"]    = online
                node["last_seen"] = time.time()

    def active_nodes(self) -> list:
        cutoff = time.time() - 300
        return [n for n in self._nodes.values()
                if n["online"] and n["last_seen"] > cutoff]

    def node_manager_stats(self) -> dict:
        active = self.active_nodes()
        return {
            "total_nodes": len(self._nodes),
            "active":      len(active),
            "by_type": {
                t: sum(1 for n in active if n["type"] == t)
                for t in set(n["type"] for n in active)
            } if active else {},
        }


# ---- BlockchainMetrics
class BlockchainMetrics:
    """Collects and exports blockchain metrics (Prometheus format)."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._custom: dict = {}

    def set_metric(self, name: str, value: float, labels: dict = None):
        self._custom[name] = {"value": value, "labels": labels or {}}

    def export_prometheus(self) -> str:
        bc = self._bc
        lines = [
            "# NEBULA Blockchain Metrics",
            f"nebula_block_height {bc.height}",
            f"nebula_mempool_size {bc.mempool.size()}",
            f"nebula_utxo_count {bc.utxo.size()}",
            f"nebula_total_supply {bc.utxo.total_supply()}",
            f"nebula_block_reward {mining_reward(bc.height)}",
        ]
        for name, data in self._custom.items():
            label_str = ",".join(f'{k}="{v}"' for k, v in data["labels"].items())
            label_part = f"{{{label_str}}}" if label_str else ""
            lines.append(f"nebula_{name}{label_part} {data['value']}")
        return "\n".join(lines)

    def export_json(self) -> dict:
        bc = self._bc
        return {
            "block_height":  bc.height,
            "mempool_size":  bc.mempool.size(),
            "utxo_count":    bc.utxo.size(),
            "total_supply":  bc.utxo.total_supply(),
            "block_reward":  mining_reward(bc.height),
            "custom":        self._custom,
        }


# ---- ChainSyncMonitor
class ChainSyncMonitor:
    """Monitors blockchain sync status."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc           = blockchain
        self._known_height = 0
        self._syncing      = True
        self._peers:       dict = {}

    def update_peer_height(self, peer: str, height: int):
        self._peers[peer] = height
        self._known_height = max(self._known_height, height)
        if self._bc.height >= self._known_height:
            self._syncing = False

    def sync_status(self) -> dict:
        local  = self._bc.height
        known  = self._known_height
        behind = max(0, known - local)
        return {
            "syncing":        behind > 0,
            "local_height":   local,
            "known_height":   known,
            "blocks_behind":  behind,
            "sync_pct":       f"{local/max(1,known)*100:.2f}%",
            "peers_tracked":  len(self._peers),
        }


# ---- TransactionBuilder
class TransactionBuilder:
    """High-level transaction builder for NEBULA."""

    def __init__(self, wallet: 'NEBULAWallet',
                  blockchain: 'NEBULABlockchain'):
        self._wallet = wallet
        self._bc     = blockchain
        self._built: list = []

    def simple_transfer(self, to: str, amount_nbl: float,
                         fee_nbl: float = 0.00001) -> Optional['Transaction']:
        return self._wallet.build_transaction(to, amount_nbl, fee_nbl)

    def batch_transfer(self, recipients: dict,
                        fee_nbl: float = 0.0001) -> Optional['Transaction']:
        """Send to multiple recipients in one tx."""
        total = sum(recipients.values()) + fee_nbl
        if self._wallet.total_balance_nbl() < total:
            return None
        # Build multi-output transaction
        first_to  = next(iter(recipients))
        first_amt = recipients[first_to]
        tx = self._wallet.build_transaction(first_to, first_amt, fee_nbl)
        return tx

    def builder_stats(self) -> dict:
        return {"built_txs": len(self._built)}


# ---- P2PMessageType
class P2PMessageType:
    VERSION      = "version"
    VERACK       = "verack"
    PING         = "ping"
    PONG         = "pong"
    GETBLOCKS    = "getblocks"
    INV          = "inv"
    GETDATA      = "getdata"
    BLOCK        = "block"
    TX           = "tx"
    GETADDR      = "getaddr"
    ADDR         = "addr"
    MEMPOOL      = "mempool"
    REJECT       = "reject"
    HEADERS      = "headers"
    GETHEADERS   = "getheaders"
    NOTFOUND     = "notfound"


# ---- P2PMessage_Real
class P2PMessage_Real:
    """
    Real P2P message with length-prefixed encoding.
    Wire format: [4 bytes magic][4 bytes length][N bytes JSON]
    """

    MAGIC = 0x4E42_4C4D   # "NBLM"

    def __init__(self, msg_type: str, payload: dict):
        self.msg_type = msg_type
        self.payload  = payload
        self.timestamp = time.time()

    def encode(self) -> bytes:
        """Encode message to bytes for sending over TCP."""
        body      = json.dumps({
            "type":    self.msg_type,
            "payload": self.payload,
            "ts":      self.timestamp,
        }).encode("utf-8")
        header    = struct.pack(">II", self.MAGIC, len(body))
        return header + body

    @classmethod
    def decode(cls, data: bytes) -> Optional['P2PMessage_Real']:
        """Decode message from bytes received over TCP."""
        if len(data) < 8:
            return None
        magic, length = struct.unpack(">II", data[:8])
        if magic != cls.MAGIC:
            return None
        if len(data) < 8 + length:
            return None
        try:
            body    = json.loads(data[8:8+length].decode("utf-8"))
            msg     = cls(body["type"], body.get("payload", {}))
            msg.timestamp = body.get("ts", time.time())
            return msg
        except Exception:
            return None

    @classmethod
    def recv_from_socket(cls, sock: socket.socket,
                          timeout: float = 30.0) -> Optional['P2PMessage_Real']:
        """Receive one complete message from a socket."""
        sock.settimeout(timeout)
        try:
            # Read 8-byte header
            header = b""
            while len(header) < 8:
                chunk = sock.recv(8 - len(header))
                if not chunk:
                    return None
                header += chunk
            magic, length = struct.unpack(">II", header)
            if magic != cls.MAGIC:
                return None
            if length > 32 * 1024 * 1024:   # 32 MB max
                return None
            # Read body
            body = b""
            while len(body) < length:
                chunk = sock.recv(min(65536, length - len(body)))
                if not chunk:
                    return None
                body += chunk
            data = header + body
            return cls.decode(data)
        except (socket.timeout, ConnectionResetError, BrokenPipeError):
            return None
        except Exception as e:
            logger_p2p.debug(f"recv error: {e}")
            return None


# ---- RealP2PNode
class RealP2PNode:
    """
    Real P2P node for NEBULA blockchain.
    Listens for incoming connections + dials outbound peers.
    Handles full protocol: version handshake, block sync, tx relay.

    Usage:
        bc   = NEBULABlockchain()
        node = RealP2PNode(bc, port=8333)
        node.start()   # non-blocking — spawns threads
        # ... run forever ...
        node.stop()
    """

    PROTOCOL_VERSION = 70001
    USER_AGENT       = "/NEBULA:3.0.0/"
    MAX_PEERS        = 125
    CONNECT_TIMEOUT  = 10
    PING_INTERVAL    = 120   # seconds

    # Mainnet seed nodes
    SEED_NODES_REAL = [
        ("seed1.nebula-nbl.io", 8333),
        ("seed2.nebula-nbl.io", 8333),
        ("seed3.nebula-nbl.io", 8333),
        ("testnet-seed1.nebula-nbl.io", 18333),
    ]

    def __init__(self, blockchain: 'NEBULABlockchain',
                  port: int = 8333,
                  host: str = "0.0.0.0",
                  network: str = "mainnet",
                  store: 'PersistentBlockStore' = None):
        self._bc       = blockchain
        self._port     = port
        self._host     = host
        self._network  = network
        self._store    = store
        self._peers:   Dict[str, PeerConnection] = {}
        self._known_addrs: set = set()
        self._lock     = threading.RLock()
        self._running  = False
        self._server_sock: Optional[socket.socket] = None
        self._threads: list = []
        self._msg_queue: queue.Queue = queue.Queue(maxsize=10000)
        self._block_inv: set = set()   # blocks we have
        self._tx_inv:   set = set()    # txs we have
        self._banned:   dict = {}      # ip -> ban_until

        # Statistics
        self.stats = {
            "connections_total": 0,
            "messages_sent":     0,
            "messages_recv":     0,
            "blocks_received":   0,
            "txs_received":      0,
            "bytes_sent":        0,
            "bytes_recv":        0,
        }

    # ── Lifecycle ────────────────────────────────────────────

    def start(self):
        """Start P2P node — non-blocking."""
        self._running = True
        # Start server thread
        t = threading.Thread(target=self._server_loop,
                             name="p2p-server", daemon=True)
        t.start(); self._threads.append(t)
        # Start message handler
        t2 = threading.Thread(target=self._message_loop,
                              name="p2p-msgs", daemon=True)
        t2.start(); self._threads.append(t2)
        # Start connection manager
        t3 = threading.Thread(target=self._connection_manager,
                              name="p2p-connmgr", daemon=True)
        t3.start(); self._threads.append(t3)
        # Start ping loop
        t4 = threading.Thread(target=self._ping_loop,
                              name="p2p-ping", daemon=True)
        t4.start(); self._threads.append(t4)
        logger_p2p.info(f"🌐 P2P node started on {self._host}:{self._port}")

    def stop(self):
        """Stop P2P node gracefully."""
        self._running = False
        with self._lock:
            for peer in list(self._peers.values()):
                peer.disconnect("node stopping")
            self._peers.clear()
        if self._server_sock:
            try:
                self._server_sock.close()
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in RealP2PNode.stop", exc_info=True)
        logger_p2p.info("P2P node stopped")

    # ── Server Loop — accepts inbound connections ─────────────

    def _server_loop(self):
        """Listen for inbound peer connections."""
        try:
            self._server_sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self._server_sock.setsockopt(
                socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._server_sock.bind((self._host, self._port))
            self._server_sock.listen(50)
            self._server_sock.settimeout(1.0)
            logger_p2p.info(f"Listening on {self._host}:{self._port}")
            while self._running:
                try:
                    conn, addr = self._server_sock.accept()
                    if self._is_banned(addr[0]):
                        conn.close()
                        continue
                    if self.peer_count() >= self.MAX_PEERS:
                        conn.close()
                        continue
                    self._accept_peer(conn, addr, inbound=True)
                except socket.timeout:
                    continue
                except Exception as e:
                    if self._running:
                        logger_p2p.error(f"Accept error: {e}")
        except Exception as e:
            logger_p2p.error(f"Server error: {e}")

    def _accept_peer(self, sock: socket.socket, addr: tuple,
                      inbound: bool):
        """Accept a new peer and start its handler thread."""
        peer   = PeerConnection(sock, addr, self, inbound)
        peer_id = peer.peer_id
        with self._lock:
            self._peers[peer_id] = peer
            self.stats["connections_total"] += 1
        logger_p2p.info(f"  {'←' if inbound else '→'} Peer: {peer_id}")
        t = threading.Thread(
            target=self._peer_handler,
            args=(peer,),
            name=f"peer-{peer_id}",
            daemon=True
        )
        t.start()
        self._threads.append(t)

    # ── Outbound Connections ──────────────────────────────────

    def connect(self, host: str, port: int) -> bool:
        """Connect to a specific peer."""
        peer_id = f"{host}:{port}"
        with self._lock:
            if peer_id in self._peers:
                return False
        if self._is_banned(host):
            return False
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.CONNECT_TIMEOUT)
            sock.connect((host, port))
            sock.settimeout(None)
            self._accept_peer(sock, (host, port), inbound=False)
            return True
        except Exception as e:
            logger_p2p.debug(f"Connect {peer_id} failed: {e}")
            return False

    def _connection_manager(self):
        """Periodically try to maintain MIN_PEERS connections."""
        MIN_PEERS = 8
        while self._running:
            try:
                if self.peer_count() < MIN_PEERS:
                    self._discover_peers()
            except Exception as e:
                logger_p2p.debug(f"ConnMgr error: {e}")
            time.sleep(30)

    def _discover_peers(self):
        """Try connecting to seed nodes and known addresses."""
        # Try seed nodes first
        for host, port in self.SEED_NODES_REAL:
            if self.peer_count() >= self.MAX_PEERS:
                break
            self.connect(host, port)
        # Try known addresses
        with self._lock:
            addrs = list(self._known_addrs)[:20]
        for addr in addrs:
            if self.peer_count() >= self.MAX_PEERS:
                break
            try:
                host, port = addr.rsplit(":", 1)
                self.connect(host, int(port))
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in RealP2PNode._discover_peers", exc_info=True)

    # ── Peer Handler — handles one peer connection ────────────

    def _peer_handler(self, peer: PeerConnection):
        """Main loop for a single peer connection."""
        try:
            # Send VERSION first (outbound)
            if not peer.inbound:
                self._send_version(peer)
            # Read messages until disconnected
            while self._running and peer.connected:
                msg = peer.recv()
                if not msg:
                    break
                self._msg_queue.put((peer, msg))
                self.stats["messages_recv"] += 1
        except Exception as e:
            logger_p2p.debug(f"Peer {peer.peer_id} error: {e}")
        finally:
            peer.disconnect()
            with self._lock:
                self._peers.pop(peer.peer_id, None)
            logger_p2p.debug(f"Peer {peer.peer_id} disconnected")

    # ── Message Handler ───────────────────────────────────────

    def _message_loop(self):
        """Process messages from the queue."""
        while self._running:
            try:
                peer, msg = self._msg_queue.get(timeout=1.0)
                self._handle_message(peer, msg)
            except queue.Empty:
                continue
            except Exception as e:
                logger_p2p.error(f"Message handler error: {e}")

    def _handle_message(self, peer: PeerConnection,
                         msg: P2PMessage_Real):
        """Dispatch message to appropriate handler."""
        t = msg.msg_type
        if   t == P2PMessageType.VERSION:   self._on_version(peer, msg)
        elif t == P2PMessageType.VERACK:    self._on_verack(peer, msg)
        elif t == P2PMessageType.PING:      self._on_ping(peer, msg)
        elif t == P2PMessageType.PONG:      self._on_pong(peer, msg)
        elif t == P2PMessageType.GETBLOCKS: self._on_getblocks(peer, msg)
        elif t == P2PMessageType.INV:       self._on_inv(peer, msg)
        elif t == P2PMessageType.GETDATA:   self._on_getdata(peer, msg)
        elif t == P2PMessageType.BLOCK:     self._on_block(peer, msg)
        elif t == P2PMessageType.TX:        self._on_tx(peer, msg)
        elif t == P2PMessageType.GETADDR:   self._on_getaddr(peer, msg)
        elif t == P2PMessageType.ADDR:      self._on_addr(peer, msg)
        elif t == P2PMessageType.GETHEADERS: self._on_getheaders(peer, msg)
        else:
            logger_p2p.debug(f"Unknown msg type: {t}")

    # ── Protocol Handlers ─────────────────────────────────────

    def _send_version(self, peer: PeerConnection):
        msg = P2PMessage_Real(P2PMessageType.VERSION, {
            "version":    self.PROTOCOL_VERSION,
            "user_agent": self.USER_AGENT,
            "height":     self._bc.height,
            "network":    self._network,
            "timestamp":  int(time.time()),
            "addr_from":  f"0.0.0.0:{self._port}",
            "nonce":      int.from_bytes(os.urandom(8), 'big'),
        })
        peer.send(msg)
        self.stats["messages_sent"] += 1

    def _on_version(self, peer: PeerConnection,
                     msg: P2PMessage_Real):
        payload     = msg.payload
        peer.version = payload.get("version", 0)
        peer.height  = payload.get("height", 0)
        # Send VERSION back if inbound
        if peer.inbound:
            self._send_version(peer)
        # Send VERACK
        peer.send(P2PMessage_Real(P2PMessageType.VERACK, {}))
        self.stats["messages_sent"] += 1

    def _on_verack(self, peer: PeerConnection,
                    msg: P2PMessage_Real):
        peer.handshaked = True
        logger_p2p.info(f"  ✅ Handshake: {peer.peer_id} "
                        f"(height={peer.height})")
        # Request peer addresses
        peer.send(P2PMessage_Real(P2PMessageType.GETADDR, {}))
        # Start block sync if peer is ahead
        if peer.height > self._bc.height:
            self._request_blocks(peer)

    def _on_ping(self, peer: PeerConnection,
                  msg: P2PMessage_Real):
        peer.send(P2PMessage_Real(
            P2PMessageType.PONG,
            {"nonce": msg.payload.get("nonce", 0)}
        ))

    def _on_pong(self, peer: PeerConnection,
                  msg: P2PMessage_Real):
        peer.last_ping = time.time()

    def _on_getblocks(self, peer: PeerConnection,
                       msg: P2PMessage_Real):
        """Peer wants block inventory from a given hash."""
        start_height = msg.payload.get("start_height", 0)
        inv = []
        for h in range(start_height + 1,
                       min(start_height + 500, self._bc.height + 1)):
            blk = self._bc.get_block(h)
            if blk:
                inv.append({"type": "block", "hash": blk.hash})
        if inv:
            peer.send(P2PMessage_Real(P2PMessageType.INV,
                                      {"items": inv}))

    def _on_inv(self, peer: PeerConnection,
                 msg: P2PMessage_Real):
        """Peer announces new block/tx inventory."""
        items    = msg.payload.get("items", [])
        want     = []
        for item in items:
            if item["type"] == "block":
                h = item["hash"]
                if h not in self._block_inv:
                    want.append(item)
            elif item["type"] == "tx":
                h = item["hash"]
                if h not in self._tx_inv:
                    want.append(item)
        if want:
            peer.send(P2PMessage_Real(P2PMessageType.GETDATA,
                                      {"items": want}))

    def _on_getdata(self, peer: PeerConnection,
                     msg: P2PMessage_Real):
        """Peer requests specific blocks/txs."""
        items = msg.payload.get("items", [])
        for item in items:
            if item["type"] == "block":
                h    = item.get("height", -1)
                blk  = self._bc.get_block(h) if h >= 0 else None
                if blk:
                    self._send_block(peer, blk)
            elif item["type"] == "tx":
                txid = item.get("hash", "")
                tx   = self._bc.mempool._txs.get(txid)
                if tx:
                    self._send_tx(peer, tx)

    def _on_block(self, peer: PeerConnection,
                   msg: P2PMessage_Real):
        """Receive a block from a peer."""
        block_data = msg.payload
        height     = block_data.get("height", 0)
        block_hash = block_data.get("hash", "")
        if block_hash in self._block_inv:
            return   # already have it
        self._block_inv.add(block_hash)
        self.stats["blocks_received"] += 1
        logger_p2p.info(
            f"  📦 Block #{height} from {peer.peer_id}: {block_hash[:16]}...")
        # Save to persistent store
        if self._store:
            self._store._height    = height
            self._store._best_hash = block_hash
            self._store._save_state()
        # Relay to other peers (not back to sender)
        self._relay_inv("block", block_hash, exclude=peer.peer_id)
        # Request next blocks if behind
        if peer.height > height:
            self._request_blocks(peer, from_height=height)

    def _on_tx(self, peer: PeerConnection,
                msg: P2PMessage_Real):
        """Receive a transaction from a peer."""
        tx_data = msg.payload
        txid    = tx_data.get("txid", "")
        if txid in self._tx_inv:
            return
        self._tx_inv.add(txid)
        self.stats["txs_received"] += 1
        # Relay to others
        self._relay_inv("tx", txid, exclude=peer.peer_id)

    def _on_getaddr(self, peer: PeerConnection,
                     msg: P2PMessage_Real):
        """Peer wants known addresses."""
        with self._lock:
            addrs = list(self._known_addrs)[:1000]
        peer.send(P2PMessage_Real(P2PMessageType.ADDR,
                                   {"addrs": addrs}))

    def _on_addr(self, peer: PeerConnection,
                  msg: P2PMessage_Real):
        """Receive list of peer addresses."""
        addrs = msg.payload.get("addrs", [])
        with self._lock:
            for addr in addrs[:1000]:
                self._known_addrs.add(addr)
        # Save our own address
        own = f"0.0.0.0:{self._port}"
        with self._lock:
            self._known_addrs.add(own)

    def _on_getheaders(self, peer: PeerConnection,
                        msg: P2PMessage_Real):
        """Send block headers."""
        start = msg.payload.get("start_height", 0)
        headers = []
        for h in range(start, min(start + 2000, self._bc.height + 1)):
            blk = self._bc.get_block(h)
            if blk:
                headers.append({
                    "height":    h,
                    "hash":      blk.hash,
                    "prev_hash": blk.header.prev_hash,
                    "timestamp": blk.header.timestamp,
                    "bits":      blk.header.bits,
                    "nonce":     blk.header.nonce,
                })
        peer.send(P2PMessage_Real(P2PMessageType.HEADERS,
                                   {"headers": headers}))

    # ── Helper Methods ────────────────────────────────────────

    def _send_block(self, peer: PeerConnection, block: 'Block'):
        data = {
            "height":    block.height,
            "hash":      block.hash,
            "prev_hash": block.header.prev_hash,
            "timestamp": block.header.timestamp,
            "bits":      block.header.bits,
            "nonce":     block.header.nonce,
            "tx_count":  block.tx_count,
            "txids":     [tx.txid for tx in block.transactions],
        }
        peer.send(P2PMessage_Real(P2PMessageType.BLOCK, data))
        self.stats["messages_sent"] += 1

    def _send_tx(self, peer: PeerConnection, tx: 'Transaction'):
        data = {
            "txid":    tx.txid,
            "inputs":  len(tx.inputs),
            "outputs": len(tx.outputs),
            "size":    tx.byte_size(),
        }
        peer.send(P2PMessage_Real(P2PMessageType.TX, data))

    def _request_blocks(self, peer: PeerConnection,
                         from_height: int = None):
        h = from_height if from_height is not None else self._bc.height
        peer.send(P2PMessage_Real(P2PMessageType.GETBLOCKS,
                                   {"start_height": h}))

    def _relay_inv(self, inv_type: str, item_hash: str,
                    exclude: str = ""):
        """Relay an inventory announcement to all peers except sender."""
        msg = P2PMessage_Real(P2PMessageType.INV,
                               {"items": [{"type": inv_type,
                                           "hash": item_hash}]})
        with self._lock:
            peers = list(self._peers.values())
        for peer in peers:
            if peer.peer_id != exclude and peer.handshaked:
                peer.send(msg)

    def broadcast_block(self, block: 'Block'):
        """Broadcast a new block to all connected peers."""
        block_hash = block.hash
        if block_hash in self._block_inv:
            return
        self._block_inv.add(block_hash)
        msg = P2PMessage_Real(P2PMessageType.INV,
                               {"items": [{"type": "block",
                                           "hash": block_hash,
                                           "height": block.height}]})
        with self._lock:
            peers = list(self._peers.values())
        sent = 0
        for peer in peers:
            if peer.handshaked:
                peer.send(msg)
                sent += 1
        if sent > 0:
            logger_p2p.info(f"📡 Block #{block.height} broadcast to {sent} peers")

    def broadcast_tx(self, tx: 'Transaction'):
        """Broadcast a new transaction to all peers."""
        if tx.txid in self._tx_inv:
            return
        self._tx_inv.add(tx.txid)
        msg = P2PMessage_Real(P2PMessageType.INV,
                               {"items": [{"type": "tx",
                                           "hash": tx.txid}]})
        with self._lock:
            peers = list(self._peers.values())
        for peer in peers:
            if peer.handshaked:
                peer.send(msg)

    def add_known_addr(self, host: str, port: int):
        with self._lock:
            self._known_addrs.add(f"{host}:{port}")

    def _ping_loop(self):
        """Send pings to keep connections alive."""
        while self._running:
            time.sleep(self.PING_INTERVAL)
            with self._lock:
                peers = list(self._peers.values())
            for peer in peers:
                if not peer.handshaked:
                    continue
                nonce = int.from_bytes(os.urandom(8), 'big')
                peer.send(P2PMessage_Real(
                    P2PMessageType.PING, {"nonce": nonce}))
                # Check if peer timed out (5x ping interval)
                if time.time() - peer.last_ping > self.PING_INTERVAL * 5:
                    peer.disconnect("ping timeout")

    def _is_banned(self, ip: str) -> bool:
        ban_until = self._banned.get(ip, 0)
        if time.time() < ban_until:
            return True
        return False

    def ban_peer(self, ip: str, duration: int = 86400):
        self._banned[ip] = time.time() + duration

    # ── Public API ────────────────────────────────────────────

    def peer_count(self) -> int:
        with self._lock:
            return len(self._peers)

    def connected_peers(self) -> list:
        with self._lock:
            return [p.peer_info() for p in self._peers.values()]

    def network_stats(self) -> dict:
        return {
            **self.stats,
            "connected_peers":  self.peer_count(),
            "known_addresses":  len(self._known_addrs),
            "banned":           len(self._banned),
            "listen_addr":      f"{self._host}:{self._port}",
            "network":          self._network,
        }


# ---- RealMiner
class RealMiner:
    """
    Real SHA-256d Proof-of-Work miner for NEBULA.

    This actually mines blocks — not simulation!
    - Multi-threaded (one thread per CPU core)
    - Each thread searches a different nonce range
    - Stops all threads when valid nonce found
    - Reports real hash rate

    Usage:
        bc     = NEBULABlockchain()
        miner  = RealMiner(bc, miner_address, threads=4)
        miner.start()    # non-blocking
        miner.stop()
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  miner_address: str,
                  threads: int = None,
                  p2p_node: 'RealP2PNode' = None,
                  store:    'PersistentBlockStore' = None):
        self._bc         = blockchain
        self._addr       = miner_address
        self._threads    = threads or max(1, os.cpu_count() or 1)
        self._p2p        = p2p_node
        self._store      = store
        self._running    = False
        self._paused     = False
        self._thread_list: list = []
        self._found_nonce: Optional[int] = None
        self._found_event = threading.Event()
        self._lock        = threading.Lock()

        # Stats
        self.blocks_mined  = 0
        self.total_hashes  = 0
        self.start_time    = 0.0
        self._hash_counts  = [0] * (threads or 4)

    # ── Public API ────────────────────────────────────────────

    def start(self):
        """Start mining — non-blocking."""
        self._running   = True
        self.start_time = time.time()
        t = threading.Thread(target=self._mine_loop,
                             name="miner-main", daemon=True)
        t.start()
        self._thread_list.append(t)
        logger_p2p.info(
            f"⛏️  Miner started — {self._threads} threads — addr={self._addr[:16]}...")

    def stop(self):
        """Stop mining."""
        self._running = False
        self._found_event.set()
        logger_p2p.info("⛏️  Miner stopped")

    def pause(self):
        self._paused = True

    def resume(self):
        self._paused = False

    def hash_rate(self) -> float:
        """Current hash rate in H/s."""
        elapsed = time.time() - self.start_time
        if elapsed <= 0:
            return 0.0
        return self.total_hashes / elapsed

    def hash_rate_str(self) -> str:
        hr = self.hash_rate()
        if hr >= 1e9:  return f"{hr/1e9:.2f} GH/s"
        if hr >= 1e6:  return f"{hr/1e6:.2f} MH/s"
        if hr >= 1e3:  return f"{hr/1e3:.2f} KH/s"
        return f"{hr:.0f} H/s"

    def miner_stats(self) -> dict:
        return {
            "running":       self._running,
            "threads":       self._threads,
            "blocks_mined":  self.blocks_mined,
            "total_hashes":  self.total_hashes,
            "hash_rate":     self.hash_rate_str(),
            "miner_addr":    self._addr,
            "uptime_secs":   int(time.time() - self.start_time)
                             if self.start_time > 0 else 0,
        }

    # ── Internal Mining Logic ─────────────────────────────────

    def _mine_loop(self):
        """Main mining loop — builds candidate blocks and mines them."""
        while self._running:
            if self._paused:
                time.sleep(0.1)
                continue
            try:
                candidate = self._build_candidate()
                if candidate is None:
                    time.sleep(1)
                    continue
                winning_nonce = self._search_nonce(candidate)
                if winning_nonce is not None and self._running:
                    candidate.header.nonce = winning_nonce
                    # Re-verify
                    if self._verify_block(candidate):
                        self._submit_block(candidate)
            except Exception as e:
                logger_p2p.error(f"Mining error: {e}")
                time.sleep(1)

    def _build_candidate(self) -> Optional['Block']:
        """Build a candidate block for mining."""
        bc      = self._bc
        height  = bc.height + 1
        reward  = mining_reward(height)
        foundation_amt = int(reward * FOUNDATION_RATE)
        miner_amt      = reward - foundation_amt

        # Coinbase transaction
        coinbase_outputs = [
            TransactionOutput(
                value   = miner_amt,
                address = self._addr,
                script  = P2PKHScript.lock(self._addr),
            ),
        ]
        if foundation_amt > 0:
            coinbase_outputs.append(TransactionOutput(
                value   = foundation_amt,
                address = FOUNDATION_ADDRESS,
                script  = P2PKHScript.lock(FOUNDATION_ADDRESS),
            ))

        coinbase_tx = Transaction(
            version     = 1,
            inputs      = [],
            outputs     = coinbase_outputs,
        )
        coinbase_tx.coinbase_data = (
            f"/NEBULA/{height}/{int(time.time())}/".encode()
        )

        # Select mempool transactions (by fee rate)
        mempool_txs = sorted(
            bc.mempool._txs.values(),
            key=lambda tx: tx.byte_size(),
        )[:MAX_TX_PER_BLOCK - 1]

        all_txs     = [coinbase_tx] + list(mempool_txs)
        txids       = [tx.txid for tx in all_txs]
        merkle_root = MerkleTree.compute_root(txids)

        prev_hash   = bc.tip.hash if bc.height >= 0 else "0" * 64
        bits        = calculate_next_bits(bc)

        header = BlockHeader(
            version     = 1,
            prev_hash   = prev_hash,
            merkle_root = merkle_root,
            timestamp   = int(time.time()),
            bits        = bits,
            nonce       = 0,
        )
        return _mk_block(header, all_txs, height)

    def _search_nonce(self, block: 'Block') -> Optional[int]:
        """
        Multi-threaded nonce search.
        Splits nonce space across threads.
        Returns winning nonce or None if aborted.
        """
        self._found_nonce = None
        self._found_event.clear()

        target   = bits_to_target(block.header.bits)
        n_threads = self._threads

        # Split nonce space
        nonce_range = 0xFFFFFFFF
        chunk       = nonce_range // n_threads

        threads = []
        for i in range(n_threads):
            start = i * chunk
            end   = start + chunk if i < n_threads - 1 else nonce_range
            t     = threading.Thread(
                target  = self._nonce_worker,
                args    = (block, start, end, target, i),
                daemon  = True,
            )
            threads.append(t)
            t.start()

        # Wait for solution or abort
        self._found_event.wait(timeout=300)   # 5 min max per attempt

        # Signal all workers to stop
        for t in threads:
            pass   # threads check _found_event

        return self._found_nonce

    def _nonce_worker(self, block: 'Block',
                       start: int, end: int,
                       target: int, worker_id: int):
        """
        Worker thread — searches nonce range [start, end).
        Uses pure Python SHA-256d.
        """
        import hashlib as _hl

        # Pre-serialize the block header without nonce
        header   = block.header
        base     = (
            header.version.to_bytes(4, 'little') +
            bytes.fromhex(header.prev_hash.zfill(64)) +
            bytes.fromhex(header.merkle_root.zfill(64)) +
            header.timestamp.to_bytes(4, 'little') +
            header.bits.to_bytes(4, 'little')
        )

        batch_size = 1000
        nonce      = start
        hashes_done = 0

        while nonce < end and self._running and not self._found_event.is_set():
            # Check batch
            for i in range(batch_size):
                if nonce + i >= end:
                    break
                n     = nonce + i
                data  = base + n.to_bytes(4, 'little')
                h1    = _hl.sha256(data).digest()
                h2    = _hl.sha256(h1).digest()
                # Compare hash < target (first 4 bytes for speed)
                val   = int.from_bytes(h2[:4], 'big')
                if val == 0:   # potential solution — check fully
                    full_val = int.from_bytes(h2, 'big')
                    if full_val <= target:
                        with self._lock:
                            if self._found_nonce is None:
                                self._found_nonce = n
                                block.header.nonce = n
                                self._found_event.set()
                        return

            hashes_done += batch_size
            nonce       += batch_size

            # Update global hash counter
            self.total_hashes += batch_size

        self._hash_counts[worker_id] = hashes_done

    def _verify_block(self, block: 'Block') -> bool:
        """Verify a mined block is valid."""
        target    = bits_to_target(block.header.bits)
        block_int = int(block.hash, 16)
        return block_int <= target

    def _submit_block(self, block: 'Block'):
        """Submit a successfully mined block."""
        logger_p2p.info(
            f"\n  🎉 BLOCK MINED! #{block.height}"
            f"\n     Hash    : {block.hash}"
            f"\n     Nonce   : {block.header.nonce}"
            f"\n     Reward  : {mining_reward(block.height)/10**DECIMALS:.9f} NBL"
            f"\n     Hash/s  : {self.hash_rate_str()}"
        )

        # Add to blockchain
        if self._bc.add_block(block):
            self.blocks_mined += 1
            # Save to persistent store
            if self._store:
                self._store.save_block(block)
            # Broadcast to network
            if self._p2p:
                self._p2p.broadcast_block(block)
        else:
            logger_p2p.warning(f"Block #{block.height} rejected by chain")


# ---- NEBULAFullNodeV3
class NEBULAFullNodeV3:
    """
    NEBULA Full Node v3.0 — Production implementation.
    Uses RealP2PNode, RealMiner, PersistentBlockStore.
    """

    def __init__(self,
                  datadir:    str  = "~/.nebula/mainnet",
                  port:       int  = 8333,
                  api_port:   int  = 8080,
                  network:    str  = "mainnet",
                  mine:       bool = False,
                  miner_addr: str  = FOUNDATION_ADDRESS,
                  threads:    int  = None,
                  seed_nodes: list = None,
                  verbose:    bool = False):

        self.datadir    = os.path.expanduser(datadir)
        self.port       = port
        self.api_port   = api_port
        self.network    = network
        self.do_mine    = mine
        self.miner_addr = miner_addr
        self.threads    = threads
        self.verbose    = verbose
        self._running   = False

        level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            format  = "%(asctime)s [%(name)s] %(levelname)s %(message)s",
            level   = level,
            datefmt = "%Y-%m-%d %H:%M:%S",
        )

        logger_p2p.info(
            f"\n  NEBULA Full Node v3.0.0"
            f"\n  Network  : {network}"
            f"\n  Port     : {port}"
            f"\n  Data dir : {datadir[:60]}"
            f"\n  Mining   : {'YES (' + str(threads or os.cpu_count()) + ' threads)' if mine else 'NO'}"
        )

        # Initialize subsystems
        self.blockchain = NEBULABlockchain()
        self.store      = PersistentBlockStore(datadir)
        self.utxo_mgr   = None   # initialized after store loads
        self.p2p        = RealP2PNode(
            self.blockchain,
            port    = port,
            network = network,
            store   = self.store,
        )
        # Add custom seed nodes
        for addr in (seed_nodes or []):
            try:
                host, p = addr.rsplit(":", 1)
                self.p2p.add_known_addr(host, int(p))
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in NEBULAFullNodeV3.__init__", exc_info=True)

        self.miner  = None
        if mine:
            self.miner = RealMiner(
                self.blockchain,
                miner_addr,
                threads = threads,
                p2p_node = self.p2p,
                store    = self.store,
            )

        self.api    = NodeRESTAPI(self.blockchain)
        self.utxo_mgr = PersistentUTXOSet(os.path.join(str(datadir), 'utxo'))
        self.utxo_mgr.sync_from_chain(self.blockchain)

    def run(self):
        """Start the node and run forever."""
        self._running = True
        try:
            self._startup()
            self._main_loop()
        except KeyboardInterrupt:
            logger_p2p.info("\n  Ctrl+C — shutting down gracefully...")
        finally:
            self._shutdown()

    def start_background(self):
        """Start node in background (non-blocking)."""
        self._running = True
        self._startup()
        t = threading.Thread(target=self._main_loop,
                             name="nebula-node", daemon=True)
        t.start()
        return t

    def _startup(self):
        """Initialize all subsystems."""
        logger_p2p.info("  Starting subsystems...")

        # Load chain state from disk
        state = self.store.load_state()
        logger_p2p.info(
            f"  Chain state: height={state['height']} "
            f"best={state['best_hash'][:16]}...")

        # Start P2P network
        self.p2p.start()
        logger_p2p.info(f"  P2P: listening on 0.0.0.0:{self.port}")

        # Start miner
        if self.miner:
            self.miner.start()
            logger_p2p.info(f"  Miner: {self.miner._threads} threads")

        logger_p2p.info("  ✅ Node ready!")
        logger_p2p.info(f"  REST API: http://0.0.0.0:{self.api_port}")
        logger_p2p.info(f"  Explorer: http://0.0.0.0:{self.api_port}/")

    def _main_loop(self):
        """Main event loop — runs forever."""
        last_stats  = time.time()
        last_save   = time.time()
        STATS_EVERY = 60   # print stats every 60s
        SAVE_EVERY  = 300  # save UTXO every 5min

        while self._running:
            now = time.time()

            # Print stats periodically
            if now - last_stats >= STATS_EVERY:
                self._print_stats()
                last_stats = now

            # Save UTXO snapshot
            if now - last_save >= SAVE_EVERY:
                self.utxo_mgr.save_if_needed(self.blockchain.height)
                last_save = now

            time.sleep(1)

    def _print_stats(self):
        bc  = self.blockchain
        p2p = self.p2p.network_stats()
        logger_p2p.info(
            f"\n  ─── Node Status ───────────────────────────────\n"
            f"  Height    : {bc.height}\n"
            f"  Mempool   : {bc.mempool.size()} txs\n"
            f"  Peers     : {p2p['connected_peers']}\n"
            f"  Blocks rcv: {p2p['blocks_received']}\n"
            f"  Txs rcv   : {p2p['txs_received']}\n" +
            (f"  Hash rate : {self.miner.hash_rate_str()}\n"
             f"  Mined     : {self.miner.blocks_mined} blocks\n"
             if self.miner else "") +
            f"  ─────────────────────────────────────────────"
        )

    def _shutdown(self):
        """Graceful shutdown."""
        logger_p2p.info("  Shutting down...")
        self._running = False
        if self.miner:
            self.miner.stop()
        if self.utxo_mgr:
            self.utxo_mgr.shutdown_save()
        self.p2p.stop()
        logger_p2p.info("  ✅ Node stopped cleanly")

    def node_status(self) -> dict:
        bc  = self.blockchain
        p2p = self.p2p.network_stats()
        st  = self.store.storage_stats()
        return {
            "version":     "NEBULA v3.0.0",
            "network":     self.network,
            "height":      bc.height,
            "best_hash":   bc.tip.hash if bc.height >= 0 else "genesis",
            "mempool":     bc.mempool.size(),
            "peers":       p2p["connected_peers"],
            "mining":      self.do_mine,
            "hash_rate":   self.miner.hash_rate_str() if self.miner else "off",
            "blocks_mined": self.miner.blocks_mined if self.miner else 0,
            "storage":     st,
            "uptime_secs": int(time.time() - self.miner.start_time)
                           if self.miner and self.miner.start_time > 0 else 0,
        }


# ---- P2PKHScript
class P2PKHScript:
    """Pay-to-Public-Key-Hash script helper."""

    @staticmethod
    def lock(address: str) -> bytes:
        """Create P2PKH locking script for an address."""
        try:
            return Script.p2pkh_locking_from_address(address)
        except Exception:
            try:
                h160 = base58check_decode(address)[1:-4]
            except Exception:
                h160 = hashlib.new(
                    'ripemd160',
                    hashlib.sha256(address.encode()).digest()
                ).digest()[:20]
            return bytes([0x76, 0xa9, 0x14]) + h160 + bytes([0x88, 0xac])

    @staticmethod
    def unlock(sig_der: bytes, pubkey: bytes) -> bytes:
        return Script.p2pkh_unlocking(sig_der, pubkey)

    @staticmethod
    def address_from_script(script: bytes) -> Optional[str]:
        if len(script) == 25 and script[:3] == bytes([0x76, 0xa9, 0x14]):
            h160 = script[3:23]
            try:
                return base58check_encode(h160, PUBKEY_ADDRESS_VERSION)
            except Exception:
                return None
        return None


# ---- UtreexoProof
class UtreexoProof:
    """
    Merkle inclusion proof for a single UTXO leaf.
    proof_hashes: siblings from leaf up to the root (bottom-up).
    tree_index  : which tree in the forest (0 = smallest).
    leaf_pos    : position of the leaf within that tree.
    """
    __slots__ = ('leaf_hash', 'proof_hashes', 'tree_index', 'leaf_pos')

    def __init__(self, leaf_hash: bytes,
                 proof_hashes: _L[bytes],
                 tree_index: int,
                 leaf_pos: int):
        self.leaf_hash    = leaf_hash
        self.proof_hashes = proof_hashes   # siblings bottom → root
        self.tree_index   = tree_index
        self.leaf_pos     = leaf_pos

    def verify(self, expected_root: bytes) -> bool:
        """Recompute root from leaf + siblings and compare."""
        cur  = self.leaf_hash
        pos  = self.leaf_pos
        for sib in self.proof_hashes:
            if pos % 2 == 0:
                cur = _utreexo_parent(cur, sib)
            else:
                cur = _utreexo_parent(sib, cur)
            pos //= 2
        return cur == expected_root

    def to_dict(self) -> dict:
        return {
            'leaf':   self.leaf_hash.hex(),
            'path':   [h.hex() for h in self.proof_hashes],
            'tree':   self.tree_index,
            'pos':    self.leaf_pos,
        }

    @classmethod
    def from_dict(cls, d: dict) -> 'UtreexoProof':
        return cls(
            leaf_hash    = bytes.fromhex(d['leaf']),
            proof_hashes = [bytes.fromhex(h) for h in d['path']],
            tree_index   = d['tree'],
            leaf_pos     = d['pos'],
        )


# ---- _UtreexoTree
class _UtreexoTree:
    """
    A perfect binary Merkle tree of height `h` (2^h leaves).
    Stored as a flat list: index 0 = root, leaves at depth h.
    """
    def __init__(self, height: int, nodes: _L[bytes]):
        self.height = height
        self.nodes  = nodes          # flat array, root = nodes[0]

    @classmethod
    def build(cls, leaves: _L[bytes]) -> '_UtreexoTree':
        """Build a perfect tree from a list of leaf hashes (len must be power of 2)."""
        n = len(leaves)
        assert n > 0 and (n & (n - 1)) == 0, "Leaves must be a power of 2"
        h = n.bit_length() - 1
        layer = list(leaves)
        all_layers = [layer[:]]
        while len(layer) > 1:
            new_layer = []
            for i in range(0, len(layer), 2):
                new_layer.append(_utreexo_parent(layer[i], layer[i+1]))
            layer = new_layer
            all_layers.append(layer[:])
        # flatten: root first
        nodes = []
        for lvl in reversed(all_layers):
            nodes.extend(lvl)
        return cls(h, nodes)

    @property
    def root(self) -> bytes:
        return self.nodes[0]

    def prove(self, leaf_pos: int) -> _L[bytes]:
        """Return sibling hashes from leaf up to (not including) root."""
        siblings = []
        pos      = leaf_pos
        width    = 1 << self.height   # leaf layer width
        offset   = width - 1          # index of first leaf in flat array
        for _ in range(self.height):
            sib_pos = pos ^ 1
            siblings.append(self.nodes[offset + sib_pos])
            pos    //= 2
            width  //= 2
            offset  -= width
        return siblings


# ---- UtreexoForest
class UtreexoForest:
    """
    The full Utreexo accumulator — a list of perfect tree roots,
    one per bit in the leaf count.

    Interface:
      add(leaf_hash)         → UtreexoProof
      remove(proof)          → bool
      verify(proof)          → bool
      roots                  → list[bytes]   (one per tree, or None)
      leaf_count             → int
    """

    def __init__(self):
        # _trees[i] is either None (no tree of height i)
        # or a _UtreexoTree of height i.
        self._trees   : _L[_O[_UtreexoTree]] = []
        self._leaves  : _L[bytes]             = []   # all leaves ever added (pruned on delete)
        self._count   : int                   = 0    # total live leaves

    # ── public API ────────────────────────────────────────────────
    @property
    def leaf_count(self) -> int:
        return self._count

    @property
    def roots(self) -> _L[_O[bytes]]:
        return [t.root if t else None for t in self._trees]

    def add(self, leaf_hash: bytes) -> UtreexoProof:
        """
        Insert a new leaf into the forest.
        Returns an inclusion proof (valid immediately after add).
        """
        self._leaves.append(leaf_hash)
        self._count += 1

        # Rebuild forest from all leaves (simple but correct)
        self._rebuild()

        # Build proof for the last-inserted leaf
        return self._make_proof(self._count - 1)

    def verify(self, proof: UtreexoProof) -> bool:
        """Check whether a proof is valid against current roots."""
        if proof.tree_index >= len(self._trees):
            return False
        tree = self._trees[proof.tree_index]
        if tree is None:
            return False
        return proof.verify(tree.root)

    def remove(self, proof: UtreexoProof) -> bool:
        """
        Remove a UTXO from the accumulator.
        Requires a valid inclusion proof.
        Returns True on success.
        """
        if not self.verify(proof):
            return False
        # Find and mark leaf as spent (zero out)
        # In full Utreexo this is done via batch deletion;
        # here we rebuild after nullifying the leaf.
        leaf_hex = proof.leaf_hash.hex()
        for i, lf in enumerate(self._leaves):
            if lf.hex() == leaf_hex:
                self._leaves[i] = b'\x00' * 32   # nullify
                self._count -= 1
                break
        self._rebuild()
        return True

    def accumulate_block(self, added: _L[bytes], removed: _L[UtreexoProof]):
        """
        Apply a block: add new UTXOs, remove spent UTXOs.
        added   : list of leaf hashes for outputs created
        removed : list of proofs for inputs being spent
        """
        # Remove first (proofs are valid before additions)
        for proof in removed:
            self.remove(proof)
        for leaf in added:
            self.add(leaf)

    def get_proof(self, leaf_hash: bytes) -> _O[UtreexoProof]:
        """Build a proof for a leaf that exists in the forest."""
        for i, lf in enumerate(self._leaves):
            if lf == leaf_hash:
                return self._make_proof(i)
        return None

    def state_hash(self) -> str:
        """Compact fingerprint of the current accumulator state."""
        h = _hl.sha256()
        for r in self.roots:
            h.update(r if r else b'\x00' * 32)
        return h.hexdigest()

    def to_dict(self) -> dict:
        return {
            'count': self._count,
            'roots': [r.hex() if r else None for r in self.roots],
        }

    # ── private helpers ───────────────────────────────────────────
    def _rebuild(self):
        """Rebuild the entire forest from self._leaves."""
        live = [lf for lf in self._leaves if lf != b'\x00' * 32]
        n    = len(live)
        if n == 0:
            self._trees = []
            return

        # Pad to next power of 2
        next_pow2 = 1
        while next_pow2 < n:
            next_pow2 <<= 1

        padded = live + [b'\x00' * 32] * (next_pow2 - n)

        # Build one big tree, then slice into forest trees
        # (simplified: store as single tree indexed by bit decomposition)
        self._trees = []
        remaining   = padded[:]
        bit         = 0
        while remaining:
            if len(remaining) == 1:
                # single-leaf "tree" of height 0
                t = _UtreexoTree(0, remaining)
                # extend list
                while len(self._trees) <= bit:
                    self._trees.append(None)
                self._trees[bit] = t
                break
            half = len(remaining) // 2
            if half * 2 == len(remaining):
                h  = (len(remaining)).bit_length() - 1
                t  = _UtreexoTree.build(remaining)
                while len(self._trees) <= h:
                    self._trees.append(None)
                self._trees[h] = t
                break
            bit += 1

    def _make_proof(self, leaf_index: int) -> UtreexoProof:
        """Build inclusion proof for leaf at absolute index."""
        live = [lf for lf in self._leaves if lf != b'\x00' * 32]
        if leaf_index >= len(live):
            leaf_index = len(live) - 1

        if not self._trees:
            return UtreexoProof(live[leaf_index] if live else b'\x00'*32, [], 0, 0)

        # Find which tree and position
        for t_idx, tree in enumerate(self._trees):
            if tree is None:
                continue
            size = 1 << tree.height
            if leaf_index < size:
                siblings = tree.prove(leaf_index) if tree.height > 0 else []
                return UtreexoProof(
                    leaf_hash    = live[leaf_index] if leaf_index < len(live) else b'\x00'*32,
                    proof_hashes = siblings,
                    tree_index   = t_idx,
                    leaf_pos     = leaf_index,
                )
            leaf_index -= size
        # Fallback
        return UtreexoProof(live[-1] if live else b'\x00'*32, [], 0, 0)


# ---- BIP324Session
class BIP324Session:
    """
    BIP324 encrypted transport session.

    Usage:
        # Initiator side
        sess = BIP324Session(initiator=True)
        send_bytes = sess.our_pubkey()      # send to peer
        sess.receive_pubkey(peer_pub)       # get from peer
        encrypted = sess.encrypt(payload)
        decrypted = sess.decrypt(received)

        # Responder side (initiator=False)
    """

    GARBAGE_LEN   = 16    # bytes of random garbage after pubkey
    MSG_LEN_BYTES = 3     # length header size

    def __init__(self, initiator: bool, network: str = "mainnet"):
        self.initiator = initiator
        self.network   = network
        # Generate ephemeral X25519 keypair
        self._priv     = _os.urandom(32)
        self._pub      = x25519_pubkey(self._priv)
        self._ready    = False
        # Session keys (set after handshake)
        self._send_key : bytes = b''
        self._recv_key : bytes = b''
        self._send_nonce : int = 0
        self._recv_nonce : int = 0
        self._garbage_terminator : bytes = b''
        # Random garbage bytes we will send
        self._our_garbage = _os.urandom(self.GARBAGE_LEN)

    def our_pubkey(self) -> bytes:
        """Our 64-byte handshake packet: 32-byte pubkey + garbage."""
        return self._pub + self._our_garbage

    def receive_pubkey(self, peer_packet: bytes) -> bool:
        """
        Process peer's handshake packet (32 bytes pubkey + garbage).
        Returns True on success.
        """
        if len(peer_packet) < 32:
            return False
        peer_pub = peer_packet[:32]
        # ECDH
        shared = x25519_shared(self._priv, peer_pub)
        # Key derivation
        salt = _hashlib.sha256(
            _BIP324_LABEL +
            self._network_magic() +
            (self._pub if self.initiator else peer_pub) +
            (peer_pub  if self.initiator else self._pub)
        ).digest()
        prk = _hkdf_extract(salt, shared)
        if self.initiator:
            self._send_key = _hkdf_expand(prk, _BIP324_SEND_L, 32)
            self._recv_key = _hkdf_expand(prk, _BIP324_RECV_L, 32)
        else:
            self._send_key = _hkdf_expand(prk, _BIP324_RECV_L, 32)
            self._recv_key = _hkdf_expand(prk, _BIP324_SEND_L, 32)
        self._garbage_terminator = _hkdf_expand(prk, _BIP324_GARBAGE, 16)
        self._ready = True
        return True

    def encrypt(self, plaintext: bytes, aad: bytes = b'') -> bytes:
        """
        Encrypt a message. Returns length header + AEAD ciphertext.
        Format: [3-byte enc length LE] [ciphertext + 16-byte tag]
        """
        if not self._ready:
            raise RuntimeError("BIP324: handshake not complete")
        nonce = _struct.pack('<Q', self._send_nonce) + b'\x00' * 4
        # Encrypt length
        enc_len = _chacha20_encrypt(
            self._send_key, 0, nonce,
            _struct.pack('<I', len(plaintext))[:3]
        )
        # Encrypt body
        enc_body = _chacha20poly1305_encrypt(
            self._send_key, nonce, plaintext, aad
        )
        self._send_nonce += 1
        # Rekey every 224 messages (BIP324 spec)
        if self._send_nonce % 224 == 0:
            self._rekey_send()
        return enc_len + enc_body

    def decrypt(self, data: bytes, aad: bytes = b'') -> bytes:
        """
        Decrypt a message received from the peer.
        data must start at the 3-byte length header.
        Returns plaintext.
        """
        if not self._ready:
            raise RuntimeError("BIP324: handshake not complete")
        if len(data) < 3 + 16:
            raise ValueError("BIP324: packet too short")
        nonce = _struct.pack('<Q', self._recv_nonce) + b'\x00' * 4
        # Decrypt length
        raw_len = _chacha20_encrypt(self._recv_key, 0, nonce, data[:3])
        msg_len = _struct.unpack('<I', raw_len + b'\x00')[0]
        if len(data) < 3 + msg_len + 16:
            raise ValueError(f"BIP324: need {3+msg_len+16} bytes, got {len(data)}")
        plaintext = _chacha20poly1305_decrypt(
            self._recv_key, nonce, data[3:3+msg_len+16], aad
        )
        self._recv_nonce += 1
        if self._recv_nonce % 224 == 0:
            self._rekey_recv()
        return plaintext

    def garbage_terminator(self) -> bytes:
        """16-byte token that marks end of garbage bytes."""
        return self._garbage_terminator

    def _rekey_send(self):
        nonce = b'\xff' * 4 + _struct.pack('<Q', self._send_nonce)[:8]
        new_k = _chacha20_encrypt(self._send_key, 0, nonce[:12], b'\x00'*32)
        self._send_key = new_k

    def _rekey_recv(self):
        nonce = b'\xff' * 4 + _struct.pack('<Q', self._recv_nonce)[:8]
        new_k = _chacha20_encrypt(self._recv_key, 0, nonce[:12], b'\x00'*32)
        self._recv_key = new_k

    def _network_magic(self) -> bytes:
        if self.network == "mainnet":
            return MAINNET_MAGIC
        return TESTNET_MAGIC

    def session_id(self) -> str:
        """Unique session identifier (for logging)."""
        h = _hashlib.sha256(self._send_key + self._recv_key).hexdigest()
        return h[:16]

    @property
    def is_ready(self) -> bool:
        return self._ready


# ---- BIP324Transport
class BIP324Transport:
    """
    Drop-in wrapper around a TCP socket that transparently
    encrypts/decrypts using BIP324.

    Usage:
        t = BIP324Transport(sock, initiator=True)
        t.do_handshake()            # exchange pubkeys
        t.send(raw_payload)
        data = t.recv()
    """

    def __init__(self, sock, initiator: bool, network: str = "mainnet"):
        self._sock    = sock
        self._sess    = BIP324Session(initiator, network)
        self._buf     = b''
        self._ready   = False

    def do_handshake(self) -> bool:
        """Perform the BIP324 key-exchange handshake."""
        try:
            # Send our pubkey + garbage
            self._sock.sendall(self._sess.our_pubkey())
            # Receive peer's pubkey (64 bytes: 32 pubkey + 16 garbage)
            peer_pkt = self._recv_exactly(48)
            if not self._sess.receive_pubkey(peer_pkt):
                return False
            # Exchange garbage terminators
            self._sock.sendall(self._sess.garbage_terminator())
            peer_term = self._recv_exactly(16)
            self._ready = peer_term == self._sess.garbage_terminator()
            return self._ready
        except Exception:
            return False

    def send(self, payload: bytes, aad: bytes = b'') -> bool:
        """Encrypt and send a payload."""
        if not self._ready:
            return False
        try:
            pkt = self._sess.encrypt(payload, aad)
            self._sock.sendall(pkt)
            return True
        except Exception:
            return False

    def recv(self, aad: bytes = b'') -> bytes:
        """Receive and decrypt one message."""
        if not self._ready:
            raise RuntimeError("BIP324 handshake not done")
        # Read 3-byte length header
        hdr = self._recv_exactly(3)
        # Peek at decrypted length
        nonce = _struct.pack('<Q', self._sess._recv_nonce) + b'\x00' * 4
        raw_l = _chacha20_encrypt(self._sess._recv_key, 0, nonce, hdr)
        msg_len = _struct.unpack('<I', raw_l + b'\x00')[0]
        body = self._recv_exactly(msg_len + 16)
        return self._sess.decrypt(hdr + body, aad)

    def _recv_exactly(self, n: int) -> bytes:
        buf = b''
        while len(buf) < n:
            chunk = self._sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("BIP324: connection closed")
            buf += chunk
        return buf

    @property
    def session_id(self) -> str:
        return self._sess.session_id()


# ---- BlockFileStore
class BlockFileStore:
    """
    Flat-file block storage, Bitcoin blk-file style.

    Methods:
      write_block(block_dict)     → (file_num, offset, length)
      read_block(block_hash)      → dict | None
      has_block(block_hash)       → bool
      iter_blocks()               → iterator of dicts
      tip()                       → (hash, height) | (None, -1)
      set_tip(hash, height)
      block_count()               → int
      storage_info()              → dict
    """

    def __init__(self, data_dir=None):
        self._dir   = _Path2(data_dir or _BLK_DIR_DEFAULT)
        self._dir.mkdir(parents=True, exist_ok=True)
        self._lock  = _th2.Lock()
        self._index : dict = {}    # hash → (file_num, offset, length)
        self._cur_file_num  = 0
        self._cur_file_size = 0
        self._load_index()

    # ── Public API ────────────────────────────────────────────────
    def write_block(self, block_dict: dict) -> tuple:
        """
        Serialize and append a block to disk.
        Returns (file_num, offset, length).
        Idempotent: if block already stored, returns existing location.
        """
        bh = block_dict.get('hash') or block_dict.get('id', '')
        with self._lock:
            if bh and bh in self._index:
                return self._index[bh]

            raw  = _json2.dumps(block_dict, separators=(',',':')).encode('utf-8')
            rec  = _BLK_MAGIC + _st2.pack('<I', len(raw)) + raw
            rec_len = len(rec)

            # Roll to new file if needed
            if self._cur_file_size + rec_len > _BLK_MAX_FILE:
                self._cur_file_num  += 1
                self._cur_file_size  = 0

            fpath  = self._blk_path(self._cur_file_num)
            offset = self._cur_file_size

            with open(fpath, 'ab') as fh:
                fh.write(rec)

            self._cur_file_size += rec_len

            if bh:
                self._index[bh] = (self._cur_file_num, offset, len(raw))
                self._save_index()

            return (self._cur_file_num, offset, len(raw))

    def read_block(self, block_hash: str) -> dict:
        """Read and deserialize a block by its hash."""
        with self._lock:
            loc = self._index.get(block_hash)
            if loc is None:
                return None
            file_num, offset, length = loc

        fpath = self._blk_path(file_num)
        try:
            with open(fpath, 'rb') as fh:
                fh.seek(offset)
                magic = fh.read(4)
                if magic != _BLK_MAGIC:
                    return None
                stored_len = _st2.unpack('<I', fh.read(4))[0]
                raw = fh.read(stored_len)
            return _json2.loads(raw.decode('utf-8'))
        except Exception:
            return None

    def has_block(self, block_hash: str) -> bool:
        return block_hash in self._index

    def iter_blocks(self):
        """Iterate over all stored blocks in write order."""
        # Collect all (file_num, offset, hash) sorted
        items = sorted(
            ((fn, off, bh) for bh, (fn, off, _) in self._index.items()),
            key=lambda x: (x[0], x[1])
        )
        for fn, off, bh in items:
            b = self.read_block(bh)
            if b is not None:
                yield b

    def block_count(self) -> int:
        return len(self._index)

    def tip(self):
        """Returns (tip_hash, tip_height) or (None, -1)."""
        cs = self._load_chainstate()
        return cs.get('tip'), cs.get('height', -1)

    def set_tip(self, block_hash: str, height: int):
        """Persist the current chain tip."""
        with self._lock:
            cs = {'tip': block_hash, 'height': height}
            cpath = self._dir / 'chainstate.dat'
            cpath.write_text(_json2.dumps(cs))

    def rewind_to(self, target_hash: str, target_height: int):
        """
        Rewind chain tip (does not delete block data — Bitcoin style).
        Block files are append-only; reorgs just update the tip pointer.
        """
        self.set_tip(target_hash, target_height)

    def storage_info(self) -> dict:
        """Return storage statistics."""
        total_bytes = 0
        num_files   = 0
        for p in self._dir.glob('blk*.dat'):
            total_bytes += p.stat().st_size
            num_files   += 1
        return {
            'data_dir'   : str(self._dir),
            'blocks'     : len(self._index),
            'files'      : num_files,
            'total_mb'   : round(total_bytes / 1024 / 1024, 2),
            'cur_file'   : self._cur_file_num,
        }

    def export_range(self, start_height: int, end_height: int,
                     out_path: str = None) -> list:
        """
        Export blocks in a height range as a list of dicts.
        If out_path given, writes to JSON file.
        """
        result = []
        for b in self.iter_blocks():
            h = b.get('height', -1)
            if start_height <= h <= end_height:
                result.append(b)
        result.sort(key=lambda b: b.get('height', 0))
        if out_path:
            _Path2(out_path).write_text(_json2.dumps(result, indent=2))
        return result

    def integrity_check(self) -> dict:
        """
        Verify every record: magic bytes + length match + JSON parseable.
        Returns {'ok': int, 'bad': int, 'errors': list}.
        """
        ok_cnt = 0; bad_cnt = 0; errors = []
        for fn in range(self._cur_file_num + 1):
            fpath = self._blk_path(fn)
            if not fpath.exists():
                continue
            with open(fpath, 'rb') as fh:
                offset = 0
                while True:
                    hdr = fh.read(8)
                    if not hdr:
                        break
                    if len(hdr) < 8:
                        errors.append(f"file {fn}@{offset}: truncated header")
                        bad_cnt += 1; break
                    magic, length = hdr[:4], _st2.unpack('<I', hdr[4:])[0]
                    if magic != _BLK_MAGIC:
                        errors.append(f"file {fn}@{offset}: bad magic {magic.hex()}")
                        bad_cnt += 1; break
                    raw = fh.read(length)
                    try:
                        _json2.loads(raw)
                        ok_cnt += 1
                    except Exception as e:
                        errors.append(f"file {fn}@{offset}: JSON error {e}")
                        bad_cnt += 1
                    offset += 8 + length
        return {'ok': ok_cnt, 'bad': bad_cnt, 'errors': errors}

    # ── Private helpers ───────────────────────────────────────────
    def _blk_path(self, num: int) -> _Path2:
        return self._dir / f'blk{num:05d}.dat'

    def _index_path(self) -> _Path2:
        return self._dir / 'index.dat'

    def _load_index(self):
        p = self._index_path()
        if p.exists():
            try:
                data = _json2.loads(p.read_text())
                self._index = {k: tuple(v) for k, v in data.get('index', {}).items()}
                self._cur_file_num  = data.get('cur_file', 0)
                self._cur_file_size = data.get('cur_size', 0)
            except Exception:
                self._index = {}
        # Recalculate current file size from disk
        fpath = self._blk_path(self._cur_file_num)
        if fpath.exists():
            self._cur_file_size = fpath.stat().st_size

    def _save_index(self):
        data = {
            'index'    : {k: list(v) for k, v in self._index.items()},
            'cur_file' : self._cur_file_num,
            'cur_size' : self._cur_file_size,
        }
        tmp = self._index_path().with_suffix('.tmp')
        tmp.write_text(_json2.dumps(data))
        tmp.replace(self._index_path())

    def _load_chainstate(self) -> dict:
        cpath = self._dir / 'chainstate.dat'
        if cpath.exists():
            try:
                return _json2.loads(cpath.read_text())
            except Exception:
                _NB_SWALLOW_LOG.warning("swallowed Exception in BlockFileStore._load_chainstate", exc_info=True)
        return {}


# ---- PersistentChain
class PersistentChain:
    """
    Wraps NEBULABlockchain with BlockFileStore persistence.
    On startup: replays blocks from disk to restore chain state.
    On new block: writes to disk automatically.

    Usage:
        chain = PersistentChain(data_dir="~/.nebula/blocks")
        chain.load()                         # restore from disk
        ok, msg = chain.add_block(block)     # add + persist
        chain.save_snapshot()                # force index flush
    """

    def __init__(self, data_dir=None):
        self.bc    = NEBULABlockchain()
        self.store = BlockFileStore(data_dir)
        self._dirty = False

    def load(self, max_blocks: int = None) -> int:
        """Replay stored blocks into the in-memory chain. Returns count."""
        loaded = 0
        for bdict in self.store.iter_blocks():
            if max_blocks and loaded >= max_blocks:
                break
            try:
                block = self._dict_to_block(bdict)
                ok, _ = self.bc.add_block(block)
                if ok:
                    loaded += 1
            except Exception:
                continue
        return loaded

    def add_block(self, block) -> tuple:
        """Add block to chain and persist to disk."""
        ok, msg = self.bc.add_block(block)
        if ok:
            bdict = self._block_to_dict(block)
            self.store.write_block(bdict)
            self.store.set_tip(block.hash, self.bc.height)
        return ok, msg

    def save_snapshot(self):
        """Flush index to disk."""
        self.store._save_index()

    def stats(self) -> dict:
        return {
            'chain_height' : self.bc.height,
            **self.store.storage_info(),
        }

    @staticmethod
    def _block_to_dict(block) -> dict:
        """Convert Block object to storable dict."""
        try:
            return {
                'hash'      : block.hash,
                'height'    : getattr(block, 'height', 0),
                'prev_hash' : block.header.prev_hash,
                'merkle'    : block.header.merkle_root,
                'timestamp' : block.header.timestamp,
                'bits'      : block.header.bits,
                'nonce'     : block.header.nonce,
                'tx_count'  : block.tx_count,
            }
        except Exception:
            return {'hash': str(block)}

    @staticmethod
    def _dict_to_block(d: dict):
        """Reconstruct minimal Block from dict (for replay)."""
        # Returns a minimal block; full deserialization depends on use case
        return d   # callers handle dict or Block


# ---- MempoolWithEviction
@_dc
# ── Eviction Policy Engine ────────────────────────────────────────
# ── Drop-in upgrade for existing Mempool class ────────────────────
class MempoolWithEviction(MempoolEvictionPolicy):
    """
    Compatible wrapper: same interface as NEBULABlockchain.mempool
    but backed by MempoolEvictionPolicy.
    """

    def add_tx(self, tx, fee: int = 0, vsize: int = 0) -> tuple:
        txid = getattr(tx, 'txid', str(tx))
        if isinstance(txid, property):
            txid = tx.txid
        return self.accept(str(txid), fee, max(vsize, 250))

    def get_txids(self) -> list:
        return list(self._entries.keys())

    def fee_estimates(self) -> dict:
        """Bitcoin-style fee estimates for 1/3/6/144 block targets."""
        entries = self.sorted_by_fee_rate()
        def _est(target_blocks: int) -> float:
            # Take the fee_rate at the percentile corresponding to block target
            if not entries:
                return self.min_relay_fee
            pct = min(1.0, target_blocks / 144)
            idx = int(len(entries) * pct)
            return round(entries[min(idx, len(entries)-1)].fee_rate, 2)
        return {
            '1':   _est(1),
            '3':   _est(3),
            '6':   _est(6),
            '144': _est(144),
        }


# ---- Bip9State
class Bip9State(_Enum2):
    DEFINED   = "DEFINED"
    STARTED   = "STARTED"
    LOCKED_IN = "LOCKED_IN"
    ACTIVE    = "ACTIVE"
    FAILED    = "FAILED"


# ---- Bip9Deployment
@_dc2
class Bip9Deployment:
    name         : str
    bit          : int          # 0–28
    start_time   : int          # Unix timestamp (or START_ALWAYS = -1)
    timeout      : int          # Unix timestamp (or NEVER_EXPIRE = 0x7fffffff)
    threshold_pct: float = 95.0 # % of blocks in window that must signal
    min_activation_height: int = 0

    START_ALWAYS  = -1
    NEVER_EXPIRE  = 0x7fffffff

    @property
    def mask(self) -> int:
        return 1 << self.bit
