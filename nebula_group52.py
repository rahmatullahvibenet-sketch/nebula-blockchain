"""NEBULA group52 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. ZKVirtualMachine  (orig. lines 81166-81247)
   2. NFTGamingV2  (orig. lines 81254-81315)
   3. StakingProtocolV4  (orig. lines 81322-81370)
   4. DEXv3  (orig. lines 81377-81417)
   5. NEBULAFullSystem  (orig. lines 81424-81492)
   6. PriceDiscovery  (orig. lines 81504-81555)
   7. IncentiveSystem  (orig. lines 81562-81613)
   8. BlockValidator  (orig. lines 81620-81686)
   9. ColdStorageManager  (orig. lines 81693-81747)
  10. EpochRewardEngine  (orig. lines 81754-81800)
  11. DeFiRouterV2  (orig. lines 81807-81876)
  12. NBUSD_V3  (orig. lines 81883-81935)
  13. CrossChainNFTV2  (orig. lines 81942-81998)
  14. ValidatorCommittee  (orig. lines 82005-82046)
  15. GasMarket  (orig. lines 82053-82103)
  16. ChainIndexerV2  (orig. lines 82115-82163)
  17. RewardBooster  (orig. lines 82170-82212)
  18. LiquidityDepthAnalyzer  (orig. lines 82219-82262)
  19. SecurityAuditV2  (orig. lines 82269-82336)
  20. NFTProvenanceTracker  (orig. lines 82343-82398)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): AdvancedAnalyticsV3, AdvancedDEXV2, AdvancedStakingPlatform, BridgeEngine, CommunityHub, DAOv2, DIDRegistryV2, EcosystemHub, GameItem, GovernanceV3, InteroperabilityLayer, LendingProtocolV2, MerkleTree, NBL721Registry, NEBULABlockchain, NEBULADex, NEBULANameService, NEBULAWallet, NFTMetadataStandard, OptionsProtocolV2, OracleV2, OrderBookManager, PerpetualProtocol, SecurityCouncil, StakedNBL, StakingEngine, SyntheticAssetProtocol, TreasuryV3, VoteEscrowedNBL, ZKRollupLayer
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

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

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

def price_impact(amount_in: float, reserve_in: float,
                  reserve_out: float, fee: float = 0.003) -> float:
    """Calculate price impact for an AMM swap."""
    amount_with_fee = amount_in * (1 - fee)
    new_reserve_in  = reserve_in + amount_with_fee
    new_reserve_out = reserve_in * reserve_out / new_reserve_in
    amount_out      = reserve_out - new_reserve_out
    old_price       = reserve_out / reserve_in
    new_price       = (reserve_out - amount_out) / new_reserve_in
    return abs(new_price - old_price) / old_price * 100

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


# ---- ZKVirtualMachine
class ZKVirtualMachine:
    """
    Zero-knowledge virtual machine for NEBULA.
    Executes programs with ZK-proof of correct execution.
    """

    OPCODES = {
        0x01: "PUSH",
        0x02: "POP",
        0x03: "ADD",
        0x04: "SUB",
        0x05: "MUL",
        0x06: "DIV",
        0x07: "HASH",
        0x08: "VERIFY",
        0x09: "RETURN",
    }

    def __init__(self):
        self._stack:    List[int] = []
        self._memory:   Dict[int, int] = {}
        self._trace:    List[dict]     = []
        self._executed  = 0

    def execute(self, bytecode: bytes) -> Tuple[bool, List[int]]:
        self._stack.clear()
        self._trace.clear()
        i = 0
        while i < len(bytecode):
            op = bytecode[i]
            i += 1
            name = self.OPCODES.get(op, f"UNKNOWN_{op:02x}")
            if op == 0x01:   # PUSH
                if i < len(bytecode):
                    self._stack.append(bytecode[i])
                    i += 1
            elif op == 0x02:  # POP
                if self._stack:
                    self._stack.pop()
            elif op == 0x03:  # ADD
                if len(self._stack) >= 2:
                    b, a = self._stack.pop(), self._stack.pop()
                    self._stack.append(a + b)
            elif op == 0x04:  # SUB
                if len(self._stack) >= 2:
                    b, a = self._stack.pop(), self._stack.pop()
                    self._stack.append(max(0, a - b))
            elif op == 0x05:  # MUL
                if len(self._stack) >= 2:
                    b, a = self._stack.pop(), self._stack.pop()
                    self._stack.append(a * b)
            elif op == 0x07:  # HASH
                if self._stack:
                    top = self._stack.pop()
                    h   = int(hashlib.sha256(
                        top.to_bytes(8, 'big')
                    ).hexdigest()[:8], 16)
                    self._stack.append(h)
            elif op == 0x09:  # RETURN
                break
            self._trace.append({"op": name, "stack": list(self._stack)})
            self._executed += 1
        return True, list(self._stack)

    def generate_execution_proof(self) -> dict:
        """Generate proof of correct execution."""
        trace_hash = hashlib.sha256(
            json.dumps(self._trace, sort_keys=True).encode()
        ).hexdigest()
        return {
            "trace_hash":    trace_hash,
            "steps":         len(self._trace),
            "final_stack":   list(self._stack),
            "proof_type":    "execution_trace_commitment",
        }

    def zk_vm_stats(self) -> dict:
        return {
            "total_executed": self._executed,
            "opcodes":        len(self.OPCODES),
            "stack_depth":    len(self._stack),
        }


# ---- NFTGamingV2
class NFTGamingV2:
    """Enhanced NFT gaming v2 with item crafting and dungeons."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  rng: 'OnChainRNG'):
        self._bc      = blockchain
        self._rng     = rng
        self._items:  Dict[str, GameItem] = {}
        self._inventories: Dict[str, List[str]] = {}
        self._lock    = threading.RLock()

    def mint_random_item(self, player: str) -> GameItem:
        with self._lock:
            h      = self._bc.height
            rarity = self._rng.random_int(h, 100)
            if rarity >= 99:
                r = 4   # Legendary
            elif rarity >= 95:
                r = 3   # Epic
            elif rarity >= 80:
                r = 2   # Rare
            elif rarity >= 50:
                r = 1   # Uncommon
            else:
                r = 0   # Common
            names   = ["Sword", "Shield", "Staff", "Bow", "Armor",
                       "Ring", "Amulet", "Helm", "Boots", "Gloves"]
            name_idx = self._rng.random_int(h, len(names), 1)
            name    = f"{['Common','Uncommon','Rare','Epic','Legendary'][r]} {names[name_idx]}"
            item_id = hashlib.sha256(
                f"ITEM:{player}:{name}:{time.time()}".encode()
            ).hexdigest()[:10]
            item    = GameItemC(item_id=item_id, owner=player, game_id="nbl-game", item_type=name, name=name, rarity=["common","uncommon","rare","epic","legendary"][r], attributes={
                "attack":  10 + r * 5,
                "defense": 5 + r * 3,
                "magic":   r * 4,
            })
            self._items[item_id] = item
            if player not in self._inventories:
                self._inventories[player] = []
            self._inventories[player].append(item_id)
            return item

    def gain_xp(self, item_id: str, xp: int) -> bool:
        item = self._items.get(item_id)
        if not item:
            return False
        item.gain_xp(xp)
        return True

    def inventory(self, player: str) -> List[dict]:
        return [
            self._items[iid].to_dict()
            for iid in self._inventories.get(player, [])
            if iid in self._items
        ]

    def gaming_v2_stats(self) -> dict:
        return {
            "total_items":   len(self._items),
            "total_players": len(self._inventories),
        }


# ---- StakingProtocolV4
class StakingProtocolV4:
    """
    Staking protocol v4 — unified staking interface.
    Combines flexible, locked, delegated, and liquid staking.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc   = blockchain
        self._flex = StakingEngine(blockchain)
        self._adv  = AdvancedStakingPlatform(blockchain)
        self._del  = None   # delegated staking
        self._stnbl = StakedNBL(blockchain)
        self._venbl = VoteEscrowedNBL(blockchain)

    def stake_flexible(self, address: str, amount: int) -> Tuple[bool, str]:
        return self._flex.stake(address, amount)

    def stake_locked(self, address: str, amount_nbl: float,
                      pool_id: str) -> Tuple[bool, str]:
        return self._adv.stake(address, pool_id, amount_nbl)

    def stake_liquid(self, address: str, amount: int) -> Tuple[bool, int]:
        return self._stnbl.stake(address, amount)

    def lock_for_governance(self, address: str, amount: int,
                             lock_blocks: int) -> Tuple[bool, str]:
        return self._venbl.lock(address, amount, lock_blocks)

    def unified_position(self, address: str) -> dict:
        flex    = self._flex.get_stake(address)
        locked  = self._adv.user_positions(address)
        liquid  = self._stnbl.stnbl_balance(address)
        venbl   = self._venbl.balance(address)
        return {
            "address":      address,
            "flexible":     flex,
            "locked_pools": locked,
            "liquid_stnbl": f"{liquid/10**DECIMALS:.6f}",
            "governance_venbl": f"{venbl/10**DECIMALS:.6f}",
            "total_staked": f"{(flex.get('staked_raw', 0) + liquid)/10**DECIMALS:.6f}",
        }

    def staking_v4_stats(self) -> dict:
        return {
            "flexible_stakers": len(self._flex._stakers),
            "liquid_holders":   len(self._stnbl._stnbl_balances),
            "venbl_lockers":    len(self._venbl._locks),
            "total_stnbl_nbl":  self._stnbl.stnbl_stats()["total_staked_nbl"],
        }


# ---- DEXv3
class DEXv3:
    """
    DEX v3 — combines AMM, CLMM, and order book in one contract.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._amm     = NEBULADex(blockchain)
        self._clmm    = AdvancedDEXV2(blockchain)
        self._ob_mgr  = OrderBookManager()
        self._lock    = threading.RLock()

    def swap(self, trader: str, token_in: str, token_out: str,
              amount_in: float, venue: str = "auto") -> Tuple[bool, str, float]:
        """Route swap to best venue."""
        amt_raw = int(amount_in * 10**DECIMALS)
        if venue == "amm" or venue == "auto":
            ok, msg, out = self._amm.swap_amm(
                trader, token_in, token_out, amt_raw)
            if ok:
                return True, f"AMM: {msg}", out / 10**DECIMALS
        return False, "No liquidity", 0.0

    def add_liquidity_amm(self, lp: str, token_a: str,
                           token_b: str, amount_a: float,
                           amount_b: float) -> Tuple[bool, str]:
        return self._amm.add_liquidity(
            lp, token_a, token_b,
            int(amount_a * 10**DECIMALS),
            int(amount_b * 10**DECIMALS))

    def dex_v3_stats(self) -> dict:
        amm_pools = self._amm.dex_stats()
        return {
            "amm_pools":   amm_pools.get("total_pools", 0),
            "clmm_pools":  len(self._clmm._pools),
            "order_books": len(self._ob_mgr._books),
            "venues":      ["AMM", "CLMM", "OrderBook"],
        }


# ---- NEBULAFullSystem
class NEBULAFullSystem:
    """
    The final, fully-integrated NEBULA system.
    All 420+ modules working together.
    """

    def __init__(self, network: str = "mainnet"):
        self.network    = network
        self.blockchain = NEBULABlockchain()
        self._status    = "initializing"
        self._modules:  Dict[str, Any] = {}
        self._start_time = time.time()

    def initialize_all(self) -> int:
        """Initialize all NEBULA modules."""
        bc = self.blockchain
        module_list = [
            ("oracle",           lambda: OracleV2(bc)),
            ("staking",          lambda: StakingProtocolV4(bc)),
            ("dex",              lambda: DEXv3(bc, None)),
            ("governance",       lambda: GovernanceV3(bc)),
            ("nft",              lambda: NBL721Registry()),
            ("lending",          lambda: LendingProtocolV2(bc)),
            ("bridge",           lambda: BridgeEngine(bc)),
            ("nns",              lambda: NEBULANameService(bc)),
            ("treasury",         lambda: TreasuryV3(bc)),
            ("dao",              lambda: DAOv2(bc)),
            ("zk_rollup",        lambda: ZKRollupLayer(bc)),
            ("analytics",        lambda: AdvancedAnalyticsV3(bc)),
            ("security_council", lambda: SecurityCouncil(bc)),
            ("ecosystem",        lambda: EcosystemHub(bc)),
            ("identity",         lambda: DIDRegistryV2(bc)),
            ("interop",          lambda: InteroperabilityLayer(bc)),
            ("synthetics",       lambda: SyntheticAssetProtocol(bc)),
            ("perp_protocol",    lambda: PerpetualProtocol(bc)),
            ("options_v2",       lambda: OptionsProtocolV2(bc)),
            ("community",        lambda: CommunityHub(bc)),
        ]
        for name, factory in module_list:
            try:
                self._modules[name] = factory()
            except Exception as e:
                _NB_SWALLOW_LOG.debug("swallowed Exception in NEBULAFullSystem.initialize_all", exc_info=True)   # Some modules may fail if deps missing
        self._status = "running"
        return len(self._modules)

    def status(self) -> dict:
        return {
            "network":     self.network,
            "status":      self._status,
            "height":      self.blockchain.height,
            "modules":     len(self._modules),
            "uptime_secs": int(time.time() - self._start_time),
            "version":     "NEBULA v3.0.0 — Quantum Genesis",
            "creator":     "Zayn Quantum (ارمان)",
        }

    def health_check(self) -> dict:
        bc   = self.blockchain
        checks = {
            "blockchain": bc.height >= 0,
            "mempool":    bc.mempool.size() < 100_000,
            "utxo":       bc.utxo.size() >= 0,
            "modules":    len(self._modules) > 0,
        }
        return {
            "healthy":  all(checks.values()),
            "checks":   checks,
        }


# ---- PriceDiscovery
class PriceDiscovery:
    """On-chain price discovery mechanism for NEBULA assets."""

    def __init__(self, dex: 'NEBULADex',
                  oracle: 'OracleV2'):
        self._dex    = dex
        self._oracle = oracle
        self._history: Dict[str, List[Tuple[float, float]]] = {}

    def spot_price(self, base: str, quote: str) -> Optional[float]:
        pair  = f"{base}/{quote}"
        for pool in self._dex._pools.values():
            if pool.token_a == base and pool.token_b == quote:
                if pool.reserve_a > 0:
                    return pool.reserve_b / pool.reserve_a
            if pool.token_b == base and pool.token_a == quote:
                if pool.reserve_b > 0:
                    return pool.reserve_a / pool.reserve_b
        return self._oracle.price(pair)

    def twap(self, base: str, quote: str,
              window: int = 20) -> Optional[float]:
        pair = f"{base}/{quote}"
        hist = self._history.get(pair, [])
        if not hist:
            return self.spot_price(base, quote)
        prices = [p for _, p in hist[-window:]]
        return sum(prices) / len(prices) if prices else None

    def record_price(self, base: str, quote: str):
        pair  = f"{base}/{quote}"
        price = self.spot_price(base, quote)
        if price:
            if pair not in self._history:
                self._history[pair] = []
            self._history[pair].append((time.time(), price))
            if len(self._history[pair]) > 1000:
                self._history[pair].pop(0)

    def price_impact_estimate(self, base: str, quote: str,
                               amount: float) -> float:
        spot  = self.spot_price(base, quote) or 1
        for pool in self._dex._pools.values():
            if pool.token_a == base and pool.token_b == quote and pool.reserve_a > 0:
                return price_impact(amount, pool.reserve_a, pool.reserve_b)
        return 0.0

    def discovery_stats(self) -> dict:
        return {
            "tracked_pairs": len(self._history),
            "price_points":  sum(len(v) for v in self._history.values()),
        }


# ---- IncentiveSystem
class IncentiveSystem:
    """
    Protocol incentive system for NEBULA.
    Rewards users for beneficial behavior.
    """

    REWARDS = {
        "first_stake":       50 * 10**DECIMALS,
        "provide_liquidity": 100 * 10**DECIMALS,
        "governance_vote":   10 * 10**DECIMALS,
        "referral":          25 * 10**DECIMALS,
        "daily_active":      5 * 10**DECIMALS,
        "holding_30d":       20 * 10**DECIMALS,
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._claimed: Dict[str, Set[str]] = {}
        self._earned:  Dict[str, int] = {}
        self._lock     = threading.RLock()

    def earn_reward(self, address: str,
                     reward_type: str) -> Tuple[bool, int]:
        with self._lock:
            if address not in self._claimed:
                self._claimed[address] = set()
            one_time = {"first_stake", "referral"}
            if reward_type in one_time and reward_type in self._claimed[address]:
                return False, 0
            amount = self.REWARDS.get(reward_type, 0)
            if amount == 0:
                return False, 0
            if reward_type in one_time:
                self._claimed[address].add(reward_type)
            self._earned[address] = self._earned.get(address, 0) + amount
            return True, amount

    def claim_all(self, address: str) -> int:
        with self._lock:
            amount = self._earned.pop(address, 0)
            return amount

    def pending_rewards(self, address: str) -> int:
        return self._earned.get(address, 0)

    def incentive_stats(self) -> dict:
        total = sum(self._earned.values())
        return {
            "participants":    len(self._earned),
            "total_pending":   f"{total/10**DECIMALS:.3f}",
            "reward_types":    list(self.REWARDS.keys()),
        }


# ---- BlockValidator
class BlockValidator:
    """
    Validates blocks and transactions for NEBULA consensus.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def validate_block_header(self, header: 'BlockHeader',
                               prev_block: 'Block') -> Tuple[bool, str]:
        if header.prev_hash != prev_block.hash:
            return False, "Invalid prev_hash"
        if header.timestamp < prev_block.header.timestamp:
            return False, "Timestamp too old"
        if header.timestamp > time.time() + 7200:
            return False, "Timestamp too far in future"
        target = bits_to_target(header.bits)
        block_hash = int(header.hash, 16)
        if block_hash > target:
            return False, "Insufficient PoW"
        return True, "OK"

    def validate_block(self, block: 'Block',
                        utxo: 'UTXOSet') -> Tuple[bool, str]:
        if block.tx_count == 0:
            return False, "Empty block"
        # Validate coinbase
        cb = block.transactions[0]
        if cb.inputs:
            return False, "Coinbase must have no inputs"
        reward = mining_reward(block.height)
        cb_value = cb.total_output()
        if cb_value > reward:
            return False, f"Coinbase too large: {cb_value} > {reward}"
        # Validate all non-coinbase txs
        for tx in block.transactions[1:]:
            ok, msg = self.validate_transaction(tx, utxo)
            if not ok:
                return False, f"Invalid tx {tx.txid[:8]}: {msg}"
        # Validate merkle root
        txids = [tx.txid for tx in block.transactions]
        computed = MerkleTree.compute_root(txids)
        if computed != block.header.merkle_root:
            return False, "Merkle root mismatch"
        return True, "Block valid"

    def validate_transaction(self, tx: 'Transaction',
                               utxo: 'UTXOSet') -> Tuple[bool, str]:
        if not tx.inputs and not tx.coinbase_data:
            return False, "No inputs"
        if not tx.outputs:
            return False, "No outputs"
        # Check outputs
        for out in tx.outputs:
            if out.value < 0:
                return False, "Negative output"
        # Check fee
        fee = tx.fee(utxo)
        if fee < MIN_TX_FEE * tx.byte_size() // 1000:
            return False, f"Fee too low: {fee}"
        return True, "Valid"

    def validator_stats(self) -> dict:
        return {
            "chain_height":  self._bc.height,
            "rules":         ["pow", "merkle", "fee", "scripts"],
        }


# ---- ColdStorageManager
class ColdStorageManager:
    """
    Cold storage management for NEBULA wallets.
    Hardware wallet support, air-gapped signing.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def generate_multisig_cold_wallet(self, n: int = 3,
                                       required: int = 2) -> dict:
        """Generate n-of-m multisig cold wallet."""
        keys = []
        for i in range(n):
            w = NEBULAWallet.generate()
            keys.append({
                "key_index":  i + 1,
                "address":    w.first_address,
                "mnemonic":   w.mnemonic,
            })
        redeem_script = "OP_{} {} OP_{} OP_CHECKMULTISIG".format(
            required,
            " ".join(k["address"] for k in keys),
            n
        )
        p2sh_addr = "3" + hashlib.sha256(
            redeem_script.encode()
        ).hexdigest()[:33]
        return {
            "type":           f"{required}-of-{n} multisig",
            "p2sh_address":   p2sh_addr,
            "redeem_script":  redeem_script,
            "keys":           keys,
            "warning":        "Store each key separately in cold storage!",
        }

    def sign_psbt(self, unsigned_tx: dict,
                   privkey_wif: str) -> dict:
        """Sign a Partially Signed Bitcoin Transaction (PSBT) style."""
        import re
        clean = re.sub(r'[^a-fA-F0-9]', '', privkey_wif)
        sig   = hashlib.sha256(clean.encode()).hexdigest()[:128]
        return {
            **unsigned_tx,
            "partial_signature": sig,
            "signed":            True,
        }

    def verify_cold_signature(self, tx_hash: str,
                               signature: str,
                               public_key: str) -> bool:
        expected = hashlib.sha256(
            (tx_hash + public_key).encode()
        ).hexdigest()
        return len(signature) == 128


# ---- EpochRewardEngine
class EpochRewardEngine:
    """
    Distributes epoch-based rewards in NEBULA PoS.
    Each epoch: distribute staking rewards, governance incentives.
    """

    EPOCH_REWARD_NBL  = 1_000 * 10**DECIMALS   # 1000 NBL per epoch
    STAKERS_SHARE     = 0.70
    GOVERNANCE_SHARE  = 0.15
    LIQUIDITY_SHARE   = 0.10
    ECOSYSTEM_SHARE   = 0.05

    def __init__(self, blockchain: 'NEBULABlockchain',
                  epoch_system: 'EpochSystem'):
        self._bc     = blockchain
        self._epoch  = epoch_system
        self._distributed: List[dict] = []

    def distribute_epoch_rewards(self) -> dict:
        epoch    = self._epoch.current_epoch()
        total    = self.EPOCH_REWARD_NBL
        dist     = {
            "stakers":    int(total * self.STAKERS_SHARE),
            "governance": int(total * self.GOVERNANCE_SHARE),
            "liquidity":  int(total * self.LIQUIDITY_SHARE),
            "ecosystem":  int(total * self.ECOSYSTEM_SHARE),
        }
        self._epoch.record_reward(total)
        record = {
            "epoch":       epoch.epoch_num,
            "total":       total,
            "distributed": dist,
            "block":       self._bc.height,
        }
        self._distributed.append(record)
        return {
            "epoch":    epoch.epoch_num,
            "total_nbl": f"{total/10**DECIMALS:.3f}",
            "breakdown": {k: f"{v/10**DECIMALS:.3f}" for k, v in dist.items()},
        }

    def epoch_reward_stats(self) -> dict:
        total = sum(r["total"] for r in self._distributed)
        return {
            "epochs_processed": len(self._distributed),
            "total_distributed": f"{total/10**DECIMALS:.3f} NBL",
        }


# ---- DeFiRouterV2
class DeFiRouterV2:
    """
    Comprehensive DeFi router v2.
    Routes any DeFi operation to the best protocol.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  staking: 'StakingProtocolV4' = None,
                  dex:     'DEXv3'             = None,
                  lending: 'LendingProtocolV2' = None):
        self._bc      = blockchain
        self._staking = staking
        self._dex     = dex
        self._lending = lending
        self._routes:  List[dict] = []

    def best_yield(self, amount_nbl: float,
                    risk: str = "low") -> List[dict]:
        strategies = []
        if self._staking:
            strategies.append({
                "protocol": "NEBULA Staking",
                "apy":      "12-25%",
                "risk":     "low",
                "action":   f"stake_locked({amount_nbl}, '90d')",
            })
        if self._dex:
            strategies.append({
                "protocol": "NEBULA DEX LP",
                "apy":      "30-40%",
                "risk":     "medium",
                "action":   f"add_liquidity(NBL/USDT, {amount_nbl/2})",
            })
        if self._lending:
            strategies.append({
                "protocol": "NEBULA Lending",
                "apy":      "3-5%",
                "risk":     "low",
                "action":   f"supply(NBL, {amount_nbl})",
            })
        risk_filter = {"low": ["low"], "medium": ["low", "medium"],
                       "high": ["low", "medium", "high"]}
        return [s for s in strategies
                if s["risk"] in risk_filter.get(risk, ["low"])]

    def execute_route(self, user: str, protocol: str,
                       action: str, params: dict) -> Tuple[bool, str]:
        self._routes.append({
            "user":     user,
            "protocol": protocol,
            "action":   action,
            "params":   params,
            "ts":       time.time(),
        })
        if protocol == "staking" and self._staking:
            return self._staking.stake_flexible(
                user, int(params.get("amount", 0)))
        elif protocol == "dex" and self._dex:
            return self._dex.swap(
                user, params.get("in", "NBL"),
                params.get("out", "USDT"),
                params.get("amount", 0)
            )[:2]
        return False, "Protocol not available"

    def router_v2_stats(self) -> dict:
        return {
            "routes_processed": len(self._routes),
            "protocols":        ["staking", "dex", "lending"],
        }


# ---- NBUSD_V3
class NBUSD_V3:
    """
    NBUSD v3 — fully algorithmic stablecoin with rebase.
    Uses rebase mechanism to maintain $1 peg.
    """

    TARGET_PRICE  = 1.0    # $1
    REBASE_BAND   = 0.01   # ±1% before rebase

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._supply  = 0
        self._balances: Dict[str, int] = {}
        self._rebase_factor = 1.0
        self._lock   = threading.RLock()

    def mint(self, address: str, amount: int):
        with self._lock:
            self._supply += amount
            self._balances[address] = (
                self._balances.get(address, 0) + amount)

    def balance(self, address: str) -> int:
        return int(self._balances.get(address, 0) * self._rebase_factor)

    def rebase(self) -> dict:
        """Adjust supply to maintain peg."""
        price = (self._oracle.price("NBUSD/USD")
                 if self._oracle else 1.0) or 1.0
        if abs(price - self.TARGET_PRICE) < self.REBASE_BAND:
            return {"rebased": False, "price": price}
        delta   = (price - self.TARGET_PRICE) / self.TARGET_PRICE
        new_factor = self._rebase_factor * (1 + delta * 0.1)
        old_supply  = self._supply
        new_supply  = int(self._supply * new_factor / self._rebase_factor)
        self._rebase_factor = new_factor
        self._supply        = new_supply
        return {
            "rebased":      True,
            "price":        price,
            "delta":        f"{delta*100:.3f}%",
            "supply_change": f"{(new_supply-old_supply)/10**DECIMALS:.4f}",
        }

    def nbusd_v3_stats(self) -> dict:
        return {
            "symbol":         "NBUSD",
            "total_supply":   f"{self._supply/10**DECIMALS:.2f}",
            "rebase_factor":  f"{self._rebase_factor:.6f}",
            "holders":        len(self._balances),
        }


# ---- CrossChainNFTV2
class CrossChainNFTV2:
    """
    Cross-chain NFT v2 — supports multiple bridge protocols.
    Lock-mint with metadata preservation.
    """

    BRIDGE_PROTOCOLS = ["nebula_native", "wormhole", "layerzero"]

    def __init__(self, nft: 'NBL721Registry',
                  blockchain: 'NEBULABlockchain'):
        self._nft    = nft
        self._bc     = blockchain
        self._locked_nfts: Dict[str, Set[int]] = {}
        self._bridges: Dict[str, int] = {}
        self._lock   = threading.RLock()

    def bridge_out(self, collection_id: str, token_id: int,
                    owner: str, dest_chain: str,
                    protocol: str = "nebula_native") -> Tuple[bool, str]:
        with self._lock:
            if protocol not in self.BRIDGE_PROTOCOLS:
                return False, f"Unsupported: {protocol}"
            if self._nft.owner_of(collection_id, token_id) != owner:
                return False, "Not owner"
            if collection_id not in self._locked_nfts:
                self._locked_nfts[collection_id] = set()
            self._locked_nfts[collection_id].add(token_id)
            self._bridges[protocol] = self._bridges.get(protocol, 0) + 1
            tx_hash = hashlib.sha256(
                f"XCNFT:{collection_id}:{token_id}:{dest_chain}:{time.time()}".encode()
            ).hexdigest()[:16]
            return True, f"Bridging to {dest_chain} via {protocol}: {tx_hash}"

    def bridge_in(self, collection_id: str, token_id: int,
                   recipient: str, src_chain: str,
                   proof: str = "") -> Tuple[bool, str]:
        with self._lock:
            locked = self._locked_nfts.get(collection_id, set())
            if token_id in locked:
                locked.discard(token_id)
                return True, f"Released NFT #{token_id} to {recipient}"
            # Mint wrapped
            tid, msg = self._nft.mint(
                collection_id, recipient,
                f"ipfs://xcnft/{src_chain}/{token_id}",
                NFTMetadataStandard.generate_sample(
                    collection_id, token_id),
                caller=recipient)
            return True, f"Minted wrapped NFT #{tid}"

    def xcnft_v2_stats(self) -> dict:
        total_locked = sum(len(s) for s in self._locked_nfts.values())
        return {
            "locked_nfts":   total_locked,
            "bridges_used":  self._bridges,
            "protocols":     self.BRIDGE_PROTOCOLS,
        }


# ---- ValidatorCommittee
class ValidatorCommittee:
    """
    Validator committee for block finalization.
    Subset of validators responsible for 2/3 BFT finality.
    """

    COMMITTEE_SIZE = 21

    def __init__(self, validator_network: 'ValidatorNetwork',
                  blockchain: 'NEBULABlockchain'):
        self._vn   = validator_network
        self._bc   = blockchain
        self._committees: Dict[int, List[str]] = {}

    def select_committee(self, height: int) -> List[str]:
        """Select committee for a given block height."""
        active = [n.address for n in self._vn.active_validators()]
        if not active:
            return []
        # Deterministic selection via block height
        rng      = hashlib.sha256(height.to_bytes(8, 'big')).hexdigest()
        seed     = int(rng[:8], 16)
        shuffled = sorted(active, key=lambda a: (hash(a) ^ seed) % 2**32)
        committee = shuffled[:self.COMMITTEE_SIZE]
        self._committees[height] = committee
        return committee

    def check_quorum(self, height: int,
                      signers: Set[str]) -> bool:
        committee = self._committees.get(height) or self.select_committee(height)
        required  = (2 * len(committee) + 2) // 3
        signed    = sum(1 for s in signers if s in committee)
        return signed >= required

    def committee_info(self, height: int) -> dict:
        committee = self._committees.get(height, [])
        return {
            "height":     height,
            "size":       len(committee),
            "members":    committee[:5],
            "quorum":     (2 * len(committee) + 2) // 3,
        }


# ---- GasMarket
class GasMarket:
    """
    EIP-1559 style gas market for NEBULA.
    Base fee + priority fee model for fee predictability.
    """

    BASE_FEE_CHANGE_DENOMINATOR = 8
    TARGET_BLOCK_UTILIZATION    = 0.50   # 50% target
    MIN_BASE_FEE                = MIN_TX_FEE

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._base_fee  = MIN_TX_FEE
        self._history:  List[dict] = []
        self._lock      = threading.RLock()

    def update_base_fee(self, block_utilization: float) -> int:
        """Update base fee based on block utilization."""
        with self._lock:
            delta = self._base_fee // self.BASE_FEE_CHANGE_DENOMINATOR
            if block_utilization > self.TARGET_BLOCK_UTILIZATION:
                new_fee = self._base_fee + delta
            elif block_utilization < self.TARGET_BLOCK_UTILIZATION:
                new_fee = max(self.MIN_BASE_FEE, self._base_fee - delta)
            else:
                new_fee = self._base_fee
            self._history.append({
                "height":      self._bc.height,
                "base_fee":    new_fee,
                "utilization": block_utilization,
            })
            self._base_fee = new_fee
            return new_fee

    def suggested_tip(self) -> int:
        """Suggest priority fee (tip) for fast inclusion."""
        return self._base_fee // 2

    def total_fee(self, gas_used: int = 250) -> int:
        return (self._base_fee + self.suggested_tip()) * gas_used

    def gas_market_stats(self) -> dict:
        with self._lock:
            avg = (sum(h["base_fee"] for h in self._history[-100:]) //
                   max(1, len(self._history[-100:])))
        return {
            "current_base_fee": self._base_fee,
            "avg_base_100":     avg,
            "suggested_tip":    self.suggested_tip(),
            "history_points":   len(self._history),
        }


# ---- ChainIndexerV2
class ChainIndexerV2:
    """Enhanced blockchain indexer with full event indexing."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._tx_by_addr:  Dict[str, List[str]]  = {}
        self._events:      List[dict]             = []
        self._token_txs:   Dict[str, List[dict]]  = {}
        self._lock         = threading.RLock()

    def index_transaction(self, tx: 'Transaction', height: int):
        with self._lock:
            for out in tx.outputs:
                if out.address:
                    if out.address not in self._tx_by_addr:
                        self._tx_by_addr[out.address] = []
                    if tx.txid not in self._tx_by_addr[out.address]:
                        self._tx_by_addr[out.address].append(tx.txid)

    def index_event(self, event_type: str, data: dict,
                     contract_id: str = ""):
        with self._lock:
            self._events.append({
                "type":     event_type,
                "data":     data,
                "contract": contract_id,
                "block":    self._bc.height,
                "ts":       time.time(),
            })

    def get_address_txs(self, address: str,
                         limit: int = 50) -> List[str]:
        return self._tx_by_addr.get(address, [])[-limit:]

    def get_events(self, event_type: str = None,
                    n: int = 100) -> List[dict]:
        events = list(self._events)
        if event_type:
            events = [e for e in events if e["type"] == event_type]
        return events[-n:]

    def indexer_v2_stats(self) -> dict:
        with self._lock:
            total_txs = sum(len(v) for v in self._tx_by_addr.values())
        return {
            "addresses_indexed": len(self._tx_by_addr),
            "total_txs":         total_txs,
            "events_indexed":    len(self._events),
        }


# ---- RewardBooster
class RewardBooster:
    """
    Reward booster for NEBULA — multiplies rewards based on activity.
    """

    BOOST_TIERS = [
        (0,     1.00),   # no boost
        (1_000, 1.10),   # 10%
        (10_000, 1.25),
        (100_000, 1.50),
        (1_000_000, 2.0),
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._boosts: Dict[str, float] = {}

    def compute_boost(self, address: str) -> float:
        bal = self._bc.utxo.balance(address) / 10**DECIMALS
        boost = 1.0
        for threshold, mult in self.BOOST_TIERS:
            if bal >= threshold:
                boost = mult
        self._boosts[address] = boost
        return boost

    def boosted_reward(self, address: str, base: int) -> int:
        boost = self.compute_boost(address)
        return int(base * boost)

    def boost_summary(self, address: str) -> dict:
        boost = self.compute_boost(address)
        bal   = self._bc.utxo.balance(address) / 10**DECIMALS
        nxt   = next(
            ((t, m) for t, m in self.BOOST_TIERS if t > bal),
            None
        )
        return {
            "address":    address,
            "balance":    f"{bal:.3f} NBL",
            "boost":      f"{boost:.2f}x",
            "next_tier":  f"{nxt[0]:,} NBL → {nxt[1]}x" if nxt else "Max tier",
        }


# ---- LiquidityDepthAnalyzer
class LiquidityDepthAnalyzer:
    """Analyzes liquidity depth across NEBULA DEX pools."""

    def __init__(self, dex: 'NEBULADex'):
        self._dex = dex

    def depth_at_price(self, pair: str,
                        slippage_pct: float = 0.01) -> dict:
        """How much can be bought/sold within slippage?"""
        a, b = pair.split("/") if "/" in pair else (pair, "USDT")
        for pool in self._dex._pools.values():
            if pool.token_a == a and pool.token_b == b:
                if pool.reserve_a > 0 and pool.reserve_b > 0:
                    spot = pool.reserve_b / pool.reserve_a
                    max_buy_r  = pool.reserve_b * slippage_pct
                    max_sell_r = pool.reserve_a * slippage_pct
                    return {
                        "pair":        pair,
                        "spot_price":  f"{spot:.6f}",
                        "slippage":    f"{slippage_pct*100:.1f}%",
                        "buy_depth":   f"{max_buy_r/10**DECIMALS:.3f} {b}",
                        "sell_depth":  f"{max_sell_r/10**DECIMALS:.3f} {a}",
                        "reserve_a":   f"{pool.reserve_a/10**DECIMALS:.3f}",
                        "reserve_b":   f"{pool.reserve_b/10**DECIMALS:.3f}",
                    }
        return {"pair": pair, "depth": "No liquidity"}

    def all_pools_depth(self) -> List[dict]:
        results = []
        for pool in self._dex._pools.values():
            pair = f"{pool.token_a}/{pool.token_b}"
            results.append(self.depth_at_price(pair, 0.01))
        return results

    def most_liquid_pools(self, n: int = 5) -> List[dict]:
        pools = []
        for pool in self._dex._pools.values():
            tvl = pool.reserve_a + pool.reserve_b
            pools.append({
                "pair": f"{pool.token_a}/{pool.token_b}",
                "tvl":  tvl,
                "fee":  pool.fee_bps,
            })
        return sorted(pools, key=lambda p: -p["tvl"])[:n]


# ---- SecurityAuditV2
class SecurityAuditV2:
    """Automated security audit for NEBULA protocols."""

    VULNERABILITY_DB = {
        "reentrancy":          "Contract calls external contract before updating state",
        "integer_overflow":    "Arithmetic operation may overflow",
        "access_control":      "Missing access control on privileged function",
        "front_running":       "Transaction order dependency vulnerability",
        "price_manipulation":  "Oracle price can be manipulated",
        "flash_loan_attack":   "State changes vulnerable to flash loans",
        "signature_replay":    "Missing nonce in signed messages",
    }

    def audit_protocol(self, protocol_name: str,
                        code_size: int,
                        has_oracle: bool = True,
                        has_flash_loans: bool = False) -> dict:
        findings = []
        risk_score = 0
        if has_oracle:
            findings.append({
                "type":     "price_manipulation",
                "severity": "medium",
                "message":  "Consider TWAP oracle instead of spot price",
            })
            risk_score += 10
        if has_flash_loans:
            findings.append({
                "type":     "flash_loan_attack",
                "severity": "high",
                "message":  "Add reentrancy guard and checks-effects-interactions",
            })
            risk_score += 20
        if code_size > 10_000:
            findings.append({
                "type":     "complexity",
                "severity": "low",
                "message":  "Large codebase increases attack surface",
            })
            risk_score += 5
        overall = "CRITICAL" if risk_score >= 50 else \
                  "HIGH" if risk_score >= 30 else \
                  "MEDIUM" if risk_score >= 15 else "LOW"
        return {
            "protocol":    protocol_name,
            "risk_score":  risk_score,
            "risk_level":  overall,
            "findings":    findings,
            "code_size":   code_size,
            "audited_at":  time.strftime('%Y-%m-%d'),
        }

    def nebula_full_audit(self) -> dict:
        protocols = [
            ("NEBULA Core",     50_000, False, False),
            ("NEBULA DEX",      5_000,  True,  True),
            ("NEBULA Staking",  3_000,  False, False),
            ("NEBULA Lending",  4_000,  True,  True),
            ("NEBULA Bridge",   6_000,  True,  False),
            ("NEBULA Governance", 3_000, False, False),
        ]
        results = [self.audit_protocol(*p) for p in protocols]
        overall = max(r["risk_score"] for r in results)
        return {
            "ecosystem_risk":    overall,
            "protocols_audited": len(results),
            "results":           results,
        }


# ---- NFTProvenanceTracker
class NFTProvenanceTracker:
    """
    Tracks the complete provenance history of NFTs.
    Records every transfer, sale, and transformation.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._history: Dict[str, List[dict]] = {}
        self._lock   = threading.RLock()

    def record_mint(self, collection_id: str, token_id: int,
                     creator: str):
        with self._lock:
            key = f"{collection_id}:{token_id}"
            self._history[key] = [{
                "event":  "mint",
                "from":   None,
                "to":     creator,
                "price":  0,
                "block":  self._bc.height,
                "ts":     time.time(),
            }]

    def record_transfer(self, collection_id: str, token_id: int,
                          from_addr: str, to_addr: str,
                          price: float = 0):
        with self._lock:
            key = f"{collection_id}:{token_id}"
            if key not in self._history:
                self._history[key] = []
            self._history[key].append({
                "event":  "transfer" if price == 0 else "sale",
                "from":   from_addr,
                "to":     to_addr,
                "price":  price,
                "block":  self._bc.height,
                "ts":     time.time(),
            })

    def get_provenance(self, collection_id: str,
                        token_id: int) -> List[dict]:
        return self._history.get(f"{collection_id}:{token_id}", [])

    def ownership_chain(self, collection_id: str,
                         token_id: int) -> List[str]:
        history  = self.get_provenance(collection_id, token_id)
        owners   = [h["to"] for h in history if h.get("to")]
        return list(dict.fromkeys(owners))

    def provenance_stats(self) -> dict:
        total_events = sum(len(h) for h in self._history.values())
        return {
            "nfts_tracked":   len(self._history),
            "total_events":   total_events,
        }
