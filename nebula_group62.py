"""NEBULA group62 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. Bip9PeriodCache  (orig. lines 107633-107637)
   2. Misbehavior  (orig. lines 107855-107877)
   3. PeerScoreEntry  (orig. lines 107886-107915)
   4. Bip21URI  (orig. lines 108200-108310)
   5. _QRCode  (orig. lines 108317-108502)
   6. NetworkParams  (orig. lines 108597-108624)
   7. NetworkConfig  (orig. lines 108744-108841)
   8. MiniscriptError  (orig. lines 108987-108988)
   9. MiniscriptType  (orig. lines 108990-109008)
  10. MiniscriptNode  (orig. lines 109011-109252)
  11. MiniscriptPolicy  (orig. lines 109288-109355)
  12. MiniscriptCompiler  (orig. lines 109358-109403)
  13. SilentPaymentError  (orig. lines 109535-109536)
  14. SilentPaymentReceiver  (orig. lines 109538-109633)
  15. SilentPaymentSender  (orig. lines 109636-109700)
  16. SilentPaymentWallet  (orig. lines 109744-109806)
  17. WalletConnectSessionC  (orig. lines 110780-110787)
  18. LockStakingPool  (orig. lines 110804-110850)
  19. BatchCoinSelector  (orig. lines 110853-110870)
  20. MicroChannel  (orig. lines 110873-110886)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): Bip9State, Secp256k1, WalletConnectSession
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

COINBASE_MATURITY      = 100                            # blocks before coinbase spendable

OP_DUP          = 0x76

OP_HASH160      = 0xa9

OP_EQUALVERIFY  = 0x88

OP_CHECKSIG     = 0xac

OP_EQUAL        = 0x87

OP_0            = 0x00

OP_CHECKMULTISIG = 0xae

def hash160(data: bytes) -> bytes:
    """RIPEMD160(SHA256(data)) — used for addresses"""
    h = hashlib.new('ripemd160')
    h.update(hashlib.sha256(data).digest())
    return h.digest()

def c(text, color): return f"{color}{text}{C.RESET}"

def info(msg):  print(c(f"ℹ️  {msg}", C.CYAN))

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

BAN_THRESHOLD       = 100

MAX_SCORE           = 100

SCORE_DECAY_HOURS   = 6      # score decays by 1 point per decay period

def _ms_push(data: bytes) -> bytes:
    """Minimal push opcode for data."""
    n = len(data)
    if n == 0:
        return bytes([0x00])
    if n <= 75:
        return bytes([n]) + data
    if n <= 255:
        return bytes([0x4c, n]) + data
    return bytes([0x4d]) + struct.pack('<H', n) + data

def _ms_push_int(n: int) -> bytes:
    """Minimal push for small integers (0-16)."""
    if n == 0:
        return bytes([0x00])
    if 1 <= n <= 16:
        return bytes([0x50 + n])
    # larger: encode as little-endian script integer
    raw = []
    neg = n < 0
    absn = abs(n)
    while absn:
        raw.append(absn & 0xff)
        absn >>= 8
    if raw[-1] & 0x80:
        raw.append(0x80 if neg else 0x00)
    elif neg:
        raw[-1] |= 0x80
    return _ms_push(bytes(raw))

def _bech32_encode(hrp: str, witver: int, witprog: bytes) -> str:
    """Minimal bech32/bech32m encoder (BIP173/350)."""
    CHARSET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'
    def _polymod(values):
        GEN = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]
        chk = 1
        for v in values:
            b = chk >> 25
            chk = (chk & 0x1ffffff) << 5 ^ v
            for i in range(5):
                chk ^= GEN[i] if ((b >> i) & 1) else 0
        return chk
    def _hrp_expand(h):
        return [ord(x) >> 5 for x in h] + [0] + [ord(x) & 31 for x in h]
    def _convertbits(data, frombits, tobits, pad=True):
        acc = 0; bits = 0; ret = []
        maxv = (1 << tobits) - 1
        for val in data:
            acc = ((acc << frombits) | val) & 0xffffffff
            bits += frombits
            while bits >= tobits:
                bits -= tobits
                ret.append((acc >> bits) & maxv)
        if pad and bits:
            ret.append((acc << (tobits - bits)) & maxv)
        return ret
    data   = [witver] + _convertbits(witprog, 8, 5)
    const  = 1 if witver == 0 else 0x2bc830a3
    values = _hrp_expand(hrp) + data
    chk    = _polymod(values + [0, 0, 0, 0, 0, 0]) ^ const
    return hrp + '1' + ''.join(CHARSET[d] for d in data) + \
           ''.join(CHARSET[(chk >> (5*(5-i))) & 31] for i in range(6))

def _sp_compress(point) -> str:
    """Compress secp256k1 point to 33-byte hex."""
    if point is None:
        raise SilentPaymentError("Point at infinity")
    x, y = point
    prefix = '02' if y % 2 == 0 else '03'
    return prefix + x.to_bytes(32, 'big').hex()

def _sp_decompress(hex_pub: str):
    """Decompress 33-byte hex pubkey to (x, y) point."""
    b      = bytes.fromhex(hex_pub)
    prefix = b[0]
    x      = int.from_bytes(b[1:], 'big')
    p      = Secp256k1.P
    y_sq   = (pow(x, 3, p) + 7) % p
    y      = pow(y_sq, (p + 1) // 4, p)
    if (y % 2) != (prefix & 1):
        y = p - y
    return (x, y)

def _sp_input_hash(outpoints: list, input_pubkeys: list) -> bytes:
    """
    BIP352 input hash:
    hash = SHA256( SHA256( lexicographically_sorted(outpoints) ) || sum_pubkeys )
    """
    # Encode outpoints as 36-byte (txid LE + vout LE)
    encoded = []
    for txid_hex, vout in outpoints:
        txid_bytes = bytes.fromhex(txid_hex)[::-1]   # LE
        encoded.append(txid_bytes + struct.pack('<I', vout))
    encoded.sort()
    outpoints_bytes = b''.join(encoded)
    # Append sum of compressed input pubkeys (concatenated, sorted)
    pks_sorted = sorted(input_pubkeys)
    pks_bytes  = b''.join(bytes.fromhex(pk) for pk in pks_sorted)
    preimage   = outpoints_bytes + pks_bytes
    return hashlib.sha256(hashlib.sha256(preimage).digest()).digest()

def _sp_decode_address(addr: str):
    """Decode BIP352 silent payment address → (scan_hex, spend_hex)."""
    # Minimal bech32 decode
    CHARSET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'
    addr    = addr.lower()
    pos     = addr.rfind('1')
    if pos < 1:
        raise SilentPaymentError("Invalid SP address")
    hrp     = addr[:pos]
    data_str= addr[pos+1:-6]   # strip hrp + separator + checksum
    data5   = [CHARSET.index(c) for c in data_str]
    # Convert 5-bit groups back to 8-bit bytes
    acc  = 0; bits = 0; out = []
    for val in data5[1:]:   # skip witness version byte
        acc  = (acc << 5) | val
        bits += 5
        while bits >= 8:
            bits -= 8
            out.append((acc >> bits) & 0xff)
    payload = bytes(out)
    scan_hex  = payload[:33].hex()
    spend_hex = payload[33:66].hex()
    return scan_hex, spend_hex

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- Bip9PeriodCache
@_dc2
class Bip9PeriodCache:
    period      : int
    signal_count: int = 0
    state       : Bip9State = Bip9State.DEFINED


# ---- Misbehavior
class Misbehavior(_Enum3):
    # Protocol violations
    INVALID_HEADER          = 20
    INVALID_BLOCK           = 100   # instant ban
    INVALID_TX              = 10
    INVALID_SIGNATURE       = 20
    DOUBLE_SPEND_ATTEMPT    = 50
    # P2P abuse
    GETDATA_SPAM            = 1
    INV_SPAM                = 1
    PING_SPAM               = 5
    ADDR_SPAM               = 10
    BAD_HANDSHAKE           = 20
    VERSION_MISMATCH        = 5
    WRONG_NETWORK           = 100   # instant ban
    # Data quality
    OVERSIZED_MESSAGE       = 20
    STALE_BLOCK             = 5
    ORPHAN_FLOOD            = 10
    BLOOM_FILTER_ABUSE      = 10
    # Resource exhaustion
    GETBLOCKS_SPAM          = 2
    TOO_MANY_CONNECTIONS    = 20


# ---- PeerScoreEntry
@_dc3
class PeerScoreEntry:
    ip          : str
    score       : int = 0
    last_updated: float = _fld3(default_factory=_time3.time)
    events      : list = _fld3(default_factory=list)   # recent log

    def add(self, points: int, reason: str):
        self.score = min(MAX_SCORE, self.score + points)
        self.last_updated = _time3.time()
        self.events.append({
            'time'  : self.last_updated,
            'points': points,
            'reason': reason,
        })
        if len(self.events) > 50:
            self.events = self.events[-50:]

    def decay(self):
        """Decay score by 1 point per SCORE_DECAY_HOURS elapsed."""
        elapsed_periods = int(
            (_time3.time() - self.last_updated) / (SCORE_DECAY_HOURS * 3600)
        )
        if elapsed_periods > 0:
            self.score = max(0, self.score - elapsed_periods)
            self.last_updated = _time3.time()

    @property
    def is_banned(self) -> bool:
        return self.score >= BAN_THRESHOLD


# ---- Bip21URI
class Bip21URI:
    """
    Build and parse BIP21 payment URIs for NEBULA (NBL).

    Examples:
        uri = Bip21URI("NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx",
                        amount=0.001, label="Alice", message="Coffee")
        print(uri)
        # nebula:NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx?amount=0.001&label=Alice&message=Coffee
    """

    SCHEME = "nebula"

    def __init__(self, address: str,
                  amount: float = None,
                  label: str = None,
                  message: str = None,
                  memo: str = None,
                  extras: dict = None):
        self.address = address
        self.amount  = amount     # in NBL (float)
        self.label   = label
        self.message = message
        self.memo    = memo
        self.extras  = extras or {}

    def __str__(self) -> str:
        return self.to_uri()

    def to_uri(self) -> str:
        """Encode as BIP21 URI string."""
        params = {}
        if self.amount is not None:
            # Format without trailing zeros, max 9 decimal places
            params['amount'] = f"{self.amount:.9f}".rstrip('0').rstrip('.')
        if self.label:
            params['label'] = self.label
        if self.message:
            params['message'] = self.message
        if self.memo:
            params['memo'] = self.memo
        for k, v in self.extras.items():
            params[k] = str(v)

        uri = f"{self.SCHEME}:{self.address}"
        if params:
            query = '&'.join(
                f"{_quote(str(k), safe='')}={_quote(str(v), safe='')}"
                for k, v in params.items()
            )
            uri += '?' + query
        return uri

    def to_dict(self) -> dict:
        """Return as plain dict."""
        return {
            'address' : self.address,
            'amount'  : self.amount,
            'label'   : self.label,
            'message' : self.message,
            'memo'    : self.memo,
            'extras'  : self.extras,
            'uri'     : self.to_uri(),
        }

    def amount_in_neb(self) -> int:
        """Return amount in smallest units (Neb = 10^-9 NBL)."""
        if self.amount is None:
            return 0
        return int(round(self.amount * (10 ** DECIMALS)))

    @classmethod
    def parse(cls, uri: str) -> 'Bip21URI':
        """Parse a BIP21 URI string."""
        scheme = cls.SCHEME + ':'
        if not uri.startswith(scheme):
            raise ValueError(f"Not a NEBULA URI (expected '{scheme}')")
        rest = uri[len(scheme):]
        if '?' in rest:
            address, query = rest.split('?', 1)
        else:
            address, query = rest, ''

        params = {}
        if query:
            for part in query.split('&'):
                if '=' in part:
                    k, v = part.split('=', 1)
                    params[_unquote(k)] = _unquote(v)

        amount  = float(params.pop('amount',  0)) if 'amount'  in params else None
        label   = params.pop('label',   None)
        message = params.pop('message', None)
        memo    = params.pop('memo',    None)
        return cls(address, amount=amount, label=label,
                   message=message, memo=memo, extras=params)

    @classmethod
    def validate(cls, uri: str) -> tuple:
        """Validate a URI. Returns (valid: bool, error: str)."""
        try:
            parsed = cls.parse(uri)
            if not parsed.address:
                return False, "Missing address"
            if len(parsed.address) < 26 or len(parsed.address) > 62:
                return False, f"Address length invalid: {len(parsed.address)}"
            if parsed.amount is not None and parsed.amount < 0:
                return False, "Negative amount"
            return True, "ok"
        except Exception as e:
            return False, str(e)


# ---- _QRCode
class _QRCode:
    """
    Pure-Python QR code generator.
    Supports alphanumeric + byte mode, EC level M.
    """

    # QR alphanumeric charset
    _ALNUM = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:'

    # Version 1-10 capacities (byte mode, EC level M)
    _CAPACITIES = [
        0, 14, 26, 42, 62, 84, 106, 122, 154, 180, 206
    ]

    # Reed-Solomon ECC codewords per block, version 1-10, level M
    _ECC_PER_BLOCK = [0,10,16,26,18,24,16,18,22,22,26]
    _BLOCKS        = [0, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5]

    def __init__(self, data: str):
        self._data    = data
        self._version = self._pick_version(data)
        self._size    = 4 * self._version + 17
        self._modules : list = []
        self._func    : list = []  # function pattern mask
        self._build()

    def _pick_version(self, data: str) -> int:
        n = len(data.encode('utf-8'))
        for v, cap in enumerate(self._CAPACITIES):
            if v > 0 and n <= cap:
                return v
        return 10  # max supported

    def _build(self):
        sz = self._size
        self._modules = [[False]*sz for _ in range(sz)]
        self._func    = [[False]*sz for _ in range(sz)]
        self._place_finders()
        self._place_timing()
        self._place_dark()
        self._encode_data()
        self._apply_mask()

    def _set(self, r, c, v, func=False):
        if 0 <= r < self._size and 0 <= c < self._size:
            self._modules[r][c] = v
            if func:
                self._func[r][c] = True

    def _place_finder(self, r, c):
        for dr in range(-1, 8):
            for dc in range(-1, 8):
                val = (0 <= dr <= 6 and 0 <= dc <= 6 and
                       (dr in (0,6) or dc in (0,6) or
                        (2 <= dr <= 4 and 2 <= dc <= 4)))
                self._set(r+dr, c+dc, val, func=True)

    def _place_finders(self):
        sz = self._size
        self._place_finder(0, 0)
        self._place_finder(0, sz-7)
        self._place_finder(sz-7, 0)

    def _place_timing(self):
        sz = self._size
        for i in range(8, sz-8):
            v = (i % 2 == 0)
            self._set(6, i, v, func=True)
            self._set(i, 6, v, func=True)

    def _place_dark(self):
        self._set(4*self._version+9, 8, True, func=True)

    def _encode_data(self):
        """Place data bits using byte mode."""
        data_bytes = self._data.encode('utf-8')
        # Build bit stream
        bits = []
        # Mode indicator: byte = 0100
        bits += [0,1,0,0]
        # Character count (8 bits for version 1-9)
        n = len(data_bytes)
        for i in range(7,-1,-1):
            bits.append((n >> i) & 1)
        # Data
        for byte in data_bytes:
            for i in range(7,-1,-1):
                bits.append((byte >> i) & 1)
        # Terminator
        bits += [0,0,0,0]
        # Pad to byte boundary
        while len(bits) % 8:
            bits.append(0)
        # Pad codewords
        pad_bytes = [0xEC, 0x11]
        max_bits = self._CAPACITIES[self._version] * 8
        pi = 0
        while len(bits) < max_bits:
            bits += [(pad_bytes[pi%2] >> i) & 1 for i in range(7,-1,-1)]
            pi += 1

        # Place bits in zigzag order
        bit_idx = 0
        sz = self._size
        col = sz - 1
        going_up = True
        while col >= 0:
            if col == 6:
                col -= 1
                continue
            for row_offset in range(sz):
                row = (sz-1-row_offset) if going_up else row_offset
                for c_offset in [0, -1]:
                    c = col + c_offset
                    if not self._func[row][c] and bit_idx < len(bits):
                        self._modules[row][c] = bool(bits[bit_idx])
                        bit_idx += 1
            going_up = not going_up
            col -= 2

    def _apply_mask(self):
        """Apply mask pattern 0: (row+col) % 2 == 0"""
        sz = self._size
        for r in range(sz):
            for c in range(sz):
                if not self._func[r][c]:
                    if (r + c) % 2 == 0:
                        self._modules[r][c] = not self._modules[r][c]

    def to_matrix(self) -> list:
        """Return list of lists of bool (True=dark)."""
        return [row[:] for row in self._modules]

    def to_ascii(self, border: int = 2) -> str:
        """Render as ASCII art using Unicode block chars."""
        matrix = self.to_matrix()
        sz = len(matrix)
        lines = []
        pad = '  ' * border
        top_bot = pad + '  ' * (sz + border * 2)
        for _ in range(border):
            lines.append(top_bot)
        for row in matrix:
            line = pad
            for cell in row:
                line += '██' if cell else '  '
            line += pad
            lines.append(line)
        for _ in range(border):
            lines.append(top_bot)
        return '\n'.join(lines)

    def to_svg(self, module_size: int = 6, border: int = 4) -> str:
        """Render as SVG string."""
        matrix = self.to_matrix()
        sz     = len(matrix)
        dim    = (sz + border * 2) * module_size
        rects  = []
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell:
                    x = (c + border) * module_size
                    y = (r + border) * module_size
                    rects.append(
                        f'<rect x="{x}" y="{y}" '
                        f'width="{module_size}" height="{module_size}" fill="#000"/>'
                    )
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{dim}" height="{dim}" viewBox="0 0 {dim} {dim}">'
            f'<rect width="{dim}" height="{dim}" fill="#fff"/>'
            + ''.join(rects) +
            '</svg>'
        )

    def to_html(self, title: str = '') -> str:
        """Return standalone HTML page with embedded QR."""
        svg = self.to_svg(module_size=8)
        return (
            f'<!DOCTYPE html><html><head><meta charset="utf-8">'
            f'<title>{title or "NEBULA QR"}</title></head>'
            f'<body style="font-family:monospace;text-align:center;padding:2em">'
            f'<h2>{title}</h2>{svg}'
            f'<p style="font-size:0.8em;color:#666">{self._data}</p>'
            f'</body></html>'
        )


# ---- NetworkParams
@_dc4
class NetworkParams:
    name               : str
    magic              : bytes
    default_port       : int
    # Address versions
    pubkey_addr_version: int
    script_addr_version: int
    wif_version        : int
    # Genesis
    genesis_timestamp  : int
    genesis_nonce      : int
    genesis_bits       : int
    genesis_message    : str
    genesis_hash       : str    # expected (computed at init)
    # Mining
    initial_bits       : int
    pow_limit          : int
    retarget_interval  : int
    target_block_time  : int
    # Chain rules
    coinbase_maturity  : int
    halving_interval   : int
    initial_reward     : int
    # Seeds
    dns_seeds          : list
    # Flags
    no_pow             : bool = False   # regtest: skip PoW


# ---- NetworkConfig
class NetworkConfig:
    """
    Runtime network configuration.
    Applies a NetworkParams to override global constants when
    running a non-mainnet node.

    Usage:
        cfg = NetworkConfig("testnet3")
        cfg.apply()   # patches module-level constants for this network
        # or use:
        cfg.address_version  → 0x6f
        cfg.magic            → b'\x0b\x11\x09\x07'
    """

    def __init__(self, network: str = "mainnet"):
        self.params = ALL_NETWORKS.get(network, MAINNET)
        self.name   = network

    @property
    def magic(self) -> bytes:
        return self.params.magic

    @property
    def port(self) -> int:
        return self.params.default_port

    @property
    def address_version(self) -> int:
        return self.params.pubkey_addr_version

    @property
    def script_version(self) -> int:
        return self.params.script_addr_version

    @property
    def wif_version(self) -> int:
        return self.params.wif_version

    @property
    def genesis_bits(self) -> int:
        return self.params.genesis_bits

    @property
    def initial_bits(self) -> int:
        return self.params.initial_bits

    @property
    def is_regtest(self) -> bool:
        return self.params.no_pow

    @property
    def is_testnet(self) -> bool:
        return self.name in ('testnet3', 'signet', 'regtest')

    def genesis_block_dict(self) -> dict:
        """Return genesis block parameters for this network."""
        p = self.params
        return {
            'network'   : p.name,
            'timestamp' : p.genesis_timestamp,
            'nonce'     : p.genesis_nonce,
            'bits'      : p.genesis_bits,
            'message'   : p.genesis_message,
            'height'    : 0,
        }

    def faucet_info(self) -> dict:
        """Testnet/regtest faucet information."""
        if self.name == 'mainnet':
            return {'available': False}
        return {
            'available' : True,
            'network'   : self.name,
            'url'       : f'https://faucet.nebula-nbl.io/{self.name}',
            'note'      : 'Test NBL have no real value',
        }

    def summary(self) -> dict:
        p = self.params
        return {
            'network'         : p.name,
            'magic'           : p.magic.hex(),
            'port'            : p.default_port,
            'addr_version'    : hex(p.pubkey_addr_version),
            'wif_version'     : hex(p.wif_version),
            'genesis_bits'    : hex(p.genesis_bits),
            'initial_bits'    : hex(p.initial_bits),
            'block_time_s'    : p.target_block_time,
            'retarget_blocks' : p.retarget_interval,
            'coinbase_maturity': p.coinbase_maturity,
            'halving_interval': p.halving_interval,
            'initial_reward_nbl': p.initial_reward / 10**9,
            'dns_seeds'       : p.dns_seeds,
            'no_pow'          : p.no_pow,
        }

    def __repr__(self) -> str:
        return f"NetworkConfig({self.name})"


# ---- MiniscriptError
class MiniscriptError(Exception):
    pass


# ---- MiniscriptType
class MiniscriptType:
    """
    Miniscript type system.
    Base types: B (base), V (verify), K (key), W (wrapped)
    Modifiers: z,o,n,d,u,e,f,s,x
    """
    BASE_TYPES = {'B', 'V', 'K', 'W'}

    def __init__(self, base: str, mods: str = ''):
        if base not in self.BASE_TYPES:
            raise MiniscriptError(f"Invalid base type: {base}")
        self.base = base
        self.mods = set(mods)

    def has(self, mod: str) -> bool:
        return mod in self.mods

    def __repr__(self):
        return self.base + ''.join(sorted(self.mods))


# ---- MiniscriptNode
class MiniscriptNode:
    """
    A single Miniscript AST node.
    tag   : fragment name (e.g. 'pk', 'and_v', 'thresh')
    args  : child MiniscriptNode list
    value : leaf value (pubkey hex, hash hex, timelock int)
    """
    __slots__ = ('tag', 'args', 'value', '_script', '_type')

    def __init__(self, tag: str, args=None, value=None):
        self.tag    = tag
        self.args   = args or []
        self.value  = value
        self._script = None
        self._type   = None

    # ── Type inference ──────────────────────────────────────
    def infer_type(self) -> MiniscriptType:
        if self._type:
            return self._type
        t = self.tag
        if t == 'pk_k':
            self._type = MiniscriptType('K', 'ndu')
        elif t in ('pk', 'pk_h'):
            self._type = MiniscriptType('B', 'ndu')
        elif t == 'multi':
            self._type = MiniscriptType('B', 'ndu')
        elif t == 'thresh':
            self._type = MiniscriptType('B', 'ndu')
        elif t in ('after', 'older'):
            self._type = MiniscriptType('B', 'z')
        elif t in ('sha256', 'hash256', 'hash160', 'ripemd160'):
            self._type = MiniscriptType('B', 'ndu')
        elif t == 'and_v':
            self._type = MiniscriptType('V', 'ndu')
        elif t == 'and_b':
            self._type = MiniscriptType('B', 'ndu')
        elif t in ('or_b', 'or_d', 'or_c', 'or_i'):
            self._type = MiniscriptType('B', 'du')
        elif t == 'andor':
            self._type = MiniscriptType('B', 'ndu')
        elif t == 'thresh_m':
            self._type = MiniscriptType('B', 'ndu')
        elif t == 'wrap_a':
            self._type = MiniscriptType('W', 'ndu')
        elif t == 'wrap_s':
            self._type = MiniscriptType('W', 'ndu')
        elif t == 'wrap_c':
            self._type = MiniscriptType('B', 'ndu')
        elif t == 'wrap_d':
            self._type = MiniscriptType('B', 'ndu')
        elif t == 'wrap_v':
            self._type = MiniscriptType('V', 'ndu')
        elif t == 'wrap_j':
            self._type = MiniscriptType('B', 'ndu')
        elif t == 'wrap_n':
            self._type = MiniscriptType('B', 'ndu')
        elif t == '1':
            self._type = MiniscriptType('B', 'zu')
        elif t == '0':
            self._type = MiniscriptType('B', 'zuf')
        else:
            self._type = MiniscriptType('B', '')
        return self._type

    # ── Script compilation ──────────────────────────────────
    def to_script(self) -> bytes:
        if self._script is not None:
            return self._script
        self._script = self._compile()
        return self._script

    def _compile(self) -> bytes:
        t = self.tag

        # ── Leaf fragments ──────────────────────────────────
        if t == 'pk_k':
            pk = bytes.fromhex(self.value)
            return _ms_push(pk)

        if t == 'pk':
            pk = bytes.fromhex(self.value)
            return _ms_push(pk) + bytes([OP_CHECKSIG])

        if t == 'pk_h':
            pkh = bytes.fromhex(self.value)
            return (bytes([OP_DUP, OP_HASH160]) +
                    _ms_push(pkh) +
                    bytes([OP_EQUALVERIFY, OP_CHECKSIG]))

        if t == 'multi':
            k   = self.value
            pks = self.args   # list of pubkey-hex strings
            out = _ms_push_int(k)
            for pk in pks:
                out += _ms_push(bytes.fromhex(pk))
            out += _ms_push_int(len(pks))
            out += bytes([OP_CHECKMULTISIG])
            return out

        if t == 'after':
            return _ms_push_int(self.value) + bytes([0xb1])   # OP_CHECKLOCKTIMEVERIFY

        if t == 'older':
            return _ms_push_int(self.value) + bytes([0xb2])   # OP_CHECKSEQUENCEVERIFY

        if t == 'sha256':
            h = bytes.fromhex(self.value)
            return (bytes([OP_0 + 8]) +   # OP_SIZE
                    _ms_push_int(32) +
                    bytes([OP_EQUALVERIFY, 0xa8]) +   # OP_SHA256
                    _ms_push(h) +
                    bytes([OP_EQUAL]))

        if t == 'hash256':
            h = bytes.fromhex(self.value)
            return (bytes([OP_0 + 8]) +
                    _ms_push_int(32) +
                    bytes([OP_EQUALVERIFY, 0xaa]) +   # OP_HASH256
                    _ms_push(h) +
                    bytes([OP_EQUAL]))

        if t == 'hash160':
            h = bytes.fromhex(self.value)
            return (bytes([OP_0 + 8]) +
                    _ms_push_int(20) +
                    bytes([OP_EQUALVERIFY, OP_HASH160]) +
                    _ms_push(h) +
                    bytes([OP_EQUAL]))

        if t == 'ripemd160':
            h = bytes.fromhex(self.value)
            return (bytes([OP_0 + 8]) +
                    _ms_push_int(20) +
                    bytes([OP_EQUALVERIFY, 0xa6]) +   # OP_RIPEMD160
                    _ms_push(h) +
                    bytes([OP_EQUAL]))

        if t == '1':
            return bytes([0x51])   # OP_1
        if t == '0':
            return bytes([0x00])   # OP_0

        # ── Connectives ─────────────────────────────────────
        if t == 'and_v':
            return self.args[0].to_script() + self.args[1].to_script()

        if t == 'and_b':
            return (self.args[0].to_script() +
                    self.args[1].to_script() +
                    bytes([0x84]))   # OP_BOOLAND

        if t == 'or_b':
            return (self.args[0].to_script() +
                    self.args[1].to_script() +
                    bytes([0x85]))   # OP_BOOLOR

        if t == 'or_d':
            return (self.args[0].to_script() +
                    bytes([0x73, 0x64]) +   # OP_IFDUP OP_IF
                    self.args[1].to_script() +
                    bytes([0x68]))           # OP_ENDIF

        if t == 'or_c':
            return (self.args[0].to_script() +
                    bytes([0x9b]) +           # OP_NOTIF
                    self.args[1].to_script() +
                    bytes([0x68]))

        if t == 'or_i':
            return (bytes([0x63]) +           # OP_IF
                    self.args[0].to_script() +
                    bytes([0x67]) +           # OP_ELSE
                    self.args[1].to_script() +
                    bytes([0x68]))            # OP_ENDIF

        if t == 'andor':
            # andor(X,Y,Z) = X OP_NOTIF Z OP_ELSE Y OP_ENDIF
            return (self.args[0].to_script() +
                    bytes([0x9b]) +
                    self.args[2].to_script() +
                    bytes([0x67]) +
                    self.args[1].to_script() +
                    bytes([0x68]))

        if t == 'thresh':
            k    = self.value
            subs = self.args
            out  = subs[0].to_script()
            for sub in subs[1:]:
                out += sub.to_script() + bytes([0x93])  # OP_ADD
            out += _ms_push_int(k) + bytes([OP_EQUAL])
            return out

        # ── Wrappers ─────────────────────────────────────────
        if t == 'wrap_a':
            return bytes([0x9b]) + self.args[0].to_script() + bytes([0x68])

        if t == 'wrap_s':
            return bytes([0xac]) + self.args[0].to_script()

        if t == 'wrap_c':
            return self.args[0].to_script() + bytes([OP_CHECKSIG])

        if t == 'wrap_d':
            return (bytes([0x76]) +            # OP_DUP
                    bytes([0x9b]) +            # OP_NOTIF
                    bytes([0x00]) +            # OP_0
                    bytes([0x67]) +            # OP_ELSE
                    self.args[0].to_script() +
                    bytes([0x68]))             # OP_ENDIF

        if t == 'wrap_v':
            inner = self.args[0].to_script()
            # append VERIFY or replace last byte
            if inner and inner[-1] == OP_EQUAL:
                return inner[:-1] + bytes([OP_EQUALVERIFY])
            if inner and inner[-1] == OP_CHECKSIG:
                return inner[:-1] + bytes([0xad])   # OP_CHECKSIGVERIFY
            return inner + bytes([0x69])             # OP_VERIFY

        if t == 'wrap_j':
            return (bytes([0x91]) +            # OP_SIZE
                    bytes([0x9b]) +            # OP_NOTIF
                    bytes([0x00]) +            # OP_0
                    bytes([0x67]) +            # OP_ELSE
                    self.args[0].to_script() +
                    bytes([0x68]))

        if t == 'wrap_n':
            return self.args[0].to_script() + bytes([0x91])  # OP_NOT

        raise MiniscriptError(f"Unknown fragment: {t}")

    def __repr__(self):
        if self.args and self.value is not None:
            return f"{self.tag}({self.value},{','.join(repr(a) for a in self.args)})"
        if self.args:
            return f"{self.tag}({','.join(repr(a) for a in self.args)})"
        if self.value is not None:
            return f"{self.tag}({self.value})"
        return self.tag


# ---- MiniscriptPolicy
class MiniscriptPolicy:
    """
    High-level spending policy that compiles to Miniscript.

    Supported policies:
      pk(KEY)
      pkh(KEY)
      multi(k, KEY1, KEY2, ...)
      after(LOCKTIME)
      older(SEQUENCE)
      sha256(HASH)
      hash256(HASH)
      hash160(HASH)
      ripemd160(HASH)
      and(POL1, POL2)
      or(POL1, POL2)
      thresh(k, POL1, POL2, ...)
    """

    @staticmethod
    def pk(pubkey_hex: str) -> MiniscriptNode:
        return MiniscriptNode('pk', value=pubkey_hex)

    @staticmethod
    def pkh(pubkey_hex: str) -> MiniscriptNode:
        """pk_h using HASH160 of the pubkey."""
        pkh = hash160(bytes.fromhex(pubkey_hex)).hex()
        return MiniscriptNode('pk_h', value=pkh)

    @staticmethod
    def multi(k: int, *pubkeys: str) -> MiniscriptNode:
        return MiniscriptNode('multi', args=list(pubkeys), value=k)

    @staticmethod
    def after(locktime: int) -> MiniscriptNode:
        return MiniscriptNode('after', value=locktime)

    @staticmethod
    def older(sequence: int) -> MiniscriptNode:
        return MiniscriptNode('older', value=sequence)

    @staticmethod
    def sha256(hash_hex: str) -> MiniscriptNode:
        return MiniscriptNode('sha256', value=hash_hex)

    @staticmethod
    def hash256(hash_hex: str) -> MiniscriptNode:
        return MiniscriptNode('hash256', value=hash_hex)

    @staticmethod
    def hash160(hash_hex: str) -> MiniscriptNode:
        return MiniscriptNode('hash160', value=hash_hex)

    @staticmethod
    def ripemd160(hash_hex: str) -> MiniscriptNode:
        return MiniscriptNode('ripemd160', value=hash_hex)

    @staticmethod
    def and_(left: MiniscriptNode, right: MiniscriptNode) -> MiniscriptNode:
        return MiniscriptNode('and_v', args=[left, right])

    @staticmethod
    def or_(left: MiniscriptNode, right: MiniscriptNode) -> MiniscriptNode:
        return MiniscriptNode('or_i', args=[left, right])

    @staticmethod
    def thresh(k: int, *subs: MiniscriptNode) -> MiniscriptNode:
        return MiniscriptNode('thresh', args=list(subs), value=k)


# ---- MiniscriptCompiler
class MiniscriptCompiler:
    """
    Compiles a MiniscriptNode policy into a locking script (bytes)
    and provides analysis utilities.
    """

    def compile(self, node: MiniscriptNode) -> bytes:
        """Return compiled Script bytes."""
        return node.to_script()

    def to_p2wsh_address(self, node: MiniscriptNode,
                          network: str = 'mainnet') -> str:
        """
        Wrap compiled script as P2WSH and return bech32 address.
        Uses NEBULA bech32 encoding.
        """
        script = self.compile(node)
        witness_program = hashlib.sha256(script).digest()
        # Encode as bech32 (version 0)
        hrp = 'nbl' if network == 'mainnet' else 'tnbl'
        return _bech32_encode(hrp, 0, witness_program)

    def analyze(self, node: MiniscriptNode) -> dict:
        """Return safety/correctness/malleability analysis."""
        script = self.compile(node)
        typ    = node.infer_type()
        return {
            'fragment'          : repr(node),
            'script_hex'        : script.hex(),
            'script_bytes'      : len(script),
            'type'              : str(typ),
            'is_valid'          : typ.base in MiniscriptType.BASE_TYPES,
            'non_malleable'     : 'n' in typ.mods,
            'unit'              : 'u' in typ.mods,
            'has_dissatisfaction': 'd' in typ.mods,
        }

    def descriptor(self, node: MiniscriptNode,
                    wrap: str = 'wsh') -> str:
        """Return output descriptor string."""
        inner = repr(node)
        if wrap == 'wsh':
            return f"wsh({inner})"
        if wrap == 'sh':
            return f"sh({inner})"
        return inner


# ---- SilentPaymentError
class SilentPaymentError(Exception):
    pass


# ---- SilentPaymentReceiver
class SilentPaymentReceiver:
    """
    A Silent Payment receiver identity.
    Holds scan key and spend key (private + public).
    """

    def __init__(self, b_scan: int = None, b_spend: int = None):
        """
        b_scan  : scan private key  (int) — used to find payments
        b_spend : spend private key (int) — used to spend payments
        If not provided, generates random keys.
        """
        curve = Secp256k1
        G     = (curve.Gx, curve.Gy)
        if b_scan is None:
            b_scan  = int.from_bytes(secrets.token_bytes(32), 'big') % curve.N
        if b_spend is None:
            b_spend = int.from_bytes(secrets.token_bytes(32), 'big') % curve.N

        self.b_scan  = b_scan
        self.b_spend = b_spend

        # Public keys
        self.B_scan  = curve.point_mul(b_scan,  G)
        self.B_spend = curve.point_mul(b_spend, G)

    @property
    def scan_pubkey_hex(self) -> str:
        return _sp_compress(self.B_scan)

    @property
    def spend_pubkey_hex(self) -> str:
        return _sp_compress(self.B_spend)

    def address(self, network: str = 'mainnet') -> str:
        """
        BIP352 silent payment address:
        bech32m encode of (B_scan || B_spend).
        HRP: 'sp'  for mainnet,  'tsp' for testnet.
        """
        payload = (bytes.fromhex(self.scan_pubkey_hex) +
                   bytes.fromhex(self.spend_pubkey_hex))
        hrp     = 'sp' if network == 'mainnet' else 'tsp'
        return _bech32_encode(hrp, 0, payload)

    def scan(self, tx_input_pubkeys: list,
              tx_outpoints: list,
              outputs: list,
              network: str = 'mainnet') -> list:
        """
        Scan a transaction for payments to this receiver.

        tx_input_pubkeys : list of hex-compressed pubkeys from tx inputs
        tx_outpoints     : list of (txid_hex, vout_int) tuples
        outputs          : list of output pubkey hex strings (x-only for Taproot)
        Returns          : list of (output_index, private_key_int) for matched outputs
        """
        curve = Secp256k1
        G     = (curve.Gx, curve.Gy)

        # Step 1: compute input_hash = hash(sorted outpoints)
        input_hash = _sp_input_hash(tx_outpoints, tx_input_pubkeys)

        # Step 2: sum input pubkeys
        A_sum = None
        for pk_hex in tx_input_pubkeys:
            pt = _sp_decompress(pk_hex)
            A_sum = curve.point_add(A_sum, pt)
        if A_sum is None:
            return []

        # Step 3: shared secret S = b_scan * input_hash * A_sum
        t_input = (int.from_bytes(input_hash, 'big') * self.b_scan) % curve.N
        S = curve.point_mul(t_input, A_sum)

        found = []
        for k in range(len(outputs)):
            # t_k = hash(S_bytes || k)
            S_bytes = bytes.fromhex(_sp_compress(S))
            t_k_bytes = hashlib.sha256(
                S_bytes + k.to_bytes(4, 'big')
            ).digest()
            t_k = int.from_bytes(t_k_bytes, 'big') % curve.N

            # Expected output pubkey: P_k = B_spend + t_k * G
            t_k_G   = curve.point_mul(t_k, G)
            P_k     = curve.point_add(self.B_spend, t_k_G)
            P_k_xonly = P_k[0].to_bytes(32, "big").hex()

            if P_k_xonly in outputs:
                idx = outputs.index(P_k_xonly)
                # private key for this output: p_k = b_spend + t_k
                p_k = (self.b_spend + t_k) % curve.N
                found.append((idx, p_k))

        return found


# ---- SilentPaymentSender
class SilentPaymentSender:
    """
    Constructs a silent payment output for a given receiver.
    """

    @staticmethod
    def create_output(receiver_scan_pubkey_hex: str,
                       receiver_spend_pubkey_hex: str,
                       sender_input_privkeys: list,
                       sender_outpoints: list,
                       k: int = 0) -> dict:
        """
        Create a P2TR output paying the receiver silently.

        receiver_scan_pubkey_hex  : hex-compressed B_scan
        receiver_spend_pubkey_hex : hex-compressed B_spend
        sender_input_privkeys     : list of int (private keys for inputs)
        sender_outpoints          : list of (txid_hex, vout_int)
        k                         : output index (for multiple outputs to same receiver)

        Returns {
            'output_pubkey_hex'  : x-only pubkey (32 bytes hex),
            'p2tr_script'        : P2TR locking script bytes,
            'p2tr_address'       : bech32m address,
        }
        """
        curve = Secp256k1
        G     = (curve.Gx, curve.Gy)

        B_scan  = _sp_decompress(receiver_scan_pubkey_hex)
        B_spend = _sp_decompress(receiver_spend_pubkey_hex)

        # Sum sender private keys
        a_sum = sum(sender_input_privkeys) % curve.N

        # input_hash = hash(sorted outpoints || sum(input_pubkeys))
        input_pubkeys = []
        for a in sender_input_privkeys:
            P = curve.point_mul(a, G)
            input_pubkeys.append(_sp_compress(P))
        input_hash = _sp_input_hash(sender_outpoints, input_pubkeys)

        # Shared secret S = a_sum * input_hash * B_scan
        t_input = (a_sum * int.from_bytes(input_hash, 'big')) % curve.N
        S = curve.point_mul(t_input, B_scan)

        # t_k = hash(S_bytes || k)
        S_bytes   = bytes.fromhex(_sp_compress(S))
        t_k_bytes = hashlib.sha256(S_bytes + k.to_bytes(4, 'big')).digest()
        t_k       = int.from_bytes(t_k_bytes, 'big') % curve.N

        # P_k = B_spend + t_k * G
        t_k_G    = curve.point_mul(t_k, G)
        P_k      = curve.point_add(B_spend, t_k_G)
        x_only   = P_k[0].to_bytes(32, 'big')  # x-only for Taproot

        # P2TR script: OP_1 <32-byte-x-only-pubkey>
        p2tr_script = bytes([0x51, 0x20]) + x_only

        return {
            'output_pubkey_hex' : x_only.hex(),
            'p2tr_script'       : p2tr_script,
            'p2tr_script_hex'   : p2tr_script.hex(),
            'p2tr_address'      : _bech32_encode('nbl', 1, x_only),
        }


# ---- SilentPaymentWallet
class SilentPaymentWallet:
    """
    Full BIP352 wallet that can:
    - Generate silent payment addresses
    - Scan transactions for incoming payments
    - Build outgoing silent payment transactions
    """

    def __init__(self, label: str = 'default'):
        self.label    = label
        self.receiver = SilentPaymentReceiver()
        self._received: list = []   # (outpoint, privkey, amount)

    @property
    def address(self) -> str:
        return self.receiver.address()

    def scan_tx(self, tx_input_pubkeys: list,
                 tx_outpoints: list,
                 outputs: list,
                 amounts: list = None) -> list:
        """
        Scan a transaction. Returns list of received payments.
        outputs : list of x-only pubkey hex strings
        amounts : optional list of amounts in Neb
        """
        found = self.receiver.scan(tx_input_pubkeys, tx_outpoints, outputs)
        result = []
        for idx, privkey in found:
            amt = amounts[idx] if amounts and idx < len(amounts) else 0
            entry = {
                'output_index' : idx,
                'privkey_int'  : privkey,
                'amount_neb'   : amt,
                'amount_nbl'   : amt / 10**DECIMALS,
            }
            self._received.append(entry)
            result.append(entry)
        return result

    def send(self, receiver_address: str,
              sender_privkeys: list,
              sender_outpoints: list,
              k: int = 0) -> dict:
        """
        Build a silent payment output to receiver_address.
        Returns the output dict from SilentPaymentSender.create_output.
        """
        # Decode address → scan + spend pubkeys
        scan_hex, spend_hex = _sp_decode_address(receiver_address)
        return SilentPaymentSender.create_output(
            receiver_scan_pubkey_hex  = scan_hex,
            receiver_spend_pubkey_hex = spend_hex,
            sender_input_privkeys     = sender_privkeys,
            sender_outpoints          = sender_outpoints,
            k                         = k,
        )

    def balance(self) -> int:
        return sum(e['amount_neb'] for e in self._received)

    def history(self) -> list:
        return list(self._received)


# ---- WalletConnectSessionC
class WalletConnectSessionC(WalletConnectSession):
    def __init__(self, dapp_name, dapp_url, session_id=None, wallet_address=None, **kw):
        super().__init__(dapp_name, dapp_url)
        if session_id:
            self.session_id = session_id
        self.wallet_address = wallet_address
        for k, v in kw.items():
            setattr(self, k, v)


# ---- LockStakingPool
class LockStakingPool:
    """Fixed-term staking pool used by AdvancedStakingPlatform."""
    BLOCKS_PER_DAY = 144

    def __init__(self, pool_id, name, lock_days, apy, min_stake_nbl):
        self.pool_id = pool_id
        self.name = name
        self.lock_days = lock_days
        self.apy = apy
        self.min_stake = int(min_stake_nbl * 10 ** DECIMALS)
        self.stakers = {}
        self.total_staked = 0

    def stake(self, address, amount, height):
        if amount <= 0:
            return False, "Invalid amount"
        info = self.stakers.get(address)
        if (info is None) and amount < self.min_stake:
            return False, f"Minimum stake: {self.min_stake / 10 ** DECIMALS:.3f} NBL"
        if info is None:
            info = {'amount': 0, 'rewards': 0, 'staked_at': height, 'unlock_block': height}
            self.stakers[address] = info
        info['amount'] += amount
        info['unlock_block'] = height + self.lock_days * self.BLOCKS_PER_DAY
        self.total_staked += amount
        return True, (f"Staked {amount / 10 ** DECIMALS:.3f} NBL in {self.name} "
                      f"(unlocks at block {info['unlock_block']})")

    def unstake(self, address, height):
        info = self.stakers.get(address)
        if not info:
            return False, 0
        if height < info['unlock_block']:
            return False, -(info['unlock_block'] - height)
        payout = info['amount'] + info['rewards']
        self.total_staked -= info['amount']
        del self.stakers[address]
        return True, payout

    def accrue_rewards(self, cur_height, last_height):
        blocks = max(0, cur_height - last_height)
        total = 0
        for info in self.stakers.values():
            r = int(info['amount'] * self.apy * blocks / (365 * self.BLOCKS_PER_DAY))
            info['rewards'] += r
            total += r
        return total


# ---- BatchCoinSelector
class BatchCoinSelector:
    """Greedy largest-first UTXO selection (skips immature coinbase)."""
    def __init__(self, blockchain):
        self._bc = blockchain

    def select_utxos(self, address, total_out, fee):
        need = total_out + fee
        h = self._bc.height
        cands = [u for u in self._bc.utxo.get_by_address(address)
                 if not (u.is_coinbase and h - u.height < COINBASE_MATURITY)]
        cands.sort(key=lambda u: u.value, reverse=True)
        sel, tot = [], 0
        for u in cands:
            sel.append(u)
            tot += u.value
            if tot >= need:
                return sel, tot - need
        return [], 0


# ---- MicroChannel
@dataclass
class MicroChannel:
    channel_id: str
    party_a: str
    party_b: str
    capacity: int
    balance_a: int
    balance_b: int
    opened_at: float = 0.0
    state: str = "open"
    sequence: int = 0
    total_payments: int = 0
    total_volume: int = 0
    closed_at: float = 0.0
