"""NEBULA group50 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. EpochSystem  (orig. lines 78529-78562)
   2. IdentityHub  (orig. lines 78569-78626)
   3. AdvancedDEXV2  (orig. lines 78639-78680)
   4. StateChannelV2  (orig. lines 78687-78764)
   5. PredictionMarketV2  (orig. lines 78771-78848)
   6. OrderbookAggregator  (orig. lines 78855-78894)
   7. FeeOptimizer  (orig. lines 78901-78949)
   8. BlockRewardSchedule  (orig. lines 78956-78997)
   9. ValidatorSelectionAlgorithm  (orig. lines 79004-79048)
  10. CrossChainSwapV2  (orig. lines 79055-79128)
  11. PortfolioRebalancer  (orig. lines 79135-79194)
  12. OnChainAnalyticsV2  (orig. lines 79201-79265)
  13. DelegatedStaking  (orig. lines 79278-79351)
  14. IDOParameters  (orig. lines 79358-79374)
  15. LaunchpadV2  (orig. lines 79376-79441)
  16. GaslessRelay  (orig. lines 79448-79497)
  17. AutoRebalancingVault  (orig. lines 79504-79573)
  18. KeeperBot  (orig. lines 79580-79635)
  19. NEBULADevTools  (orig. lines 79642-79700)
  20. CommunityHub  (orig. lines 79756-79820)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): ConcentratedLiquidityPool, ContractFactory, Epoch, NEBULAWallet
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

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

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

log = logging.getLogger("nebula.api")

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


# ---- EpochSystem
class EpochSystem:
    """Manages NEBULA epochs for staking reward distribution."""

    EPOCH_DURATION = 2016   # ~2 weeks

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._epochs: Dict[int, Epoch] = {}
        self._lock   = threading.RLock()
        self._ensure_current_epoch()

    def _ensure_current_epoch(self):
        epoch_num = self._bc.height // self.EPOCH_DURATION
        if epoch_num not in self._epochs:
            start = epoch_num * self.EPOCH_DURATION
            self._epochs[epoch_num] = Epoch(epoch_num, start,
                                             self.EPOCH_DURATION)

    def current_epoch(self) -> Epoch:
        self._ensure_current_epoch()
        epoch_num = self._bc.height // self.EPOCH_DURATION
        return self._epochs[epoch_num]

    def record_reward(self, amount: int):
        epoch = self.current_epoch()
        epoch.rewards_distributed += amount

    def epoch_stats(self) -> dict:
        epoch = self.current_epoch()
        return {
            **epoch.to_dict(),
            "progress":   f"{epoch.progress(self._bc.height)*100:.1f}%",
            "blocks_left": epoch.end_block - self._bc.height,
        }


# ---- IdentityHub
class IdentityHub:
    """
    Central identity hub for NEBULA.
    Aggregates DID, KYC, reputation, and credentials.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  did_v2: 'DIDRegistryV2' = None,
                  reputation: 'ReputationEngine' = None,
                  compliance: 'ComplianceEngine' = None):
        self._bc         = blockchain
        self._did        = did_v2
        self._rep        = reputation
        self._compliance = compliance
        self._hub_profiles: Dict[str, dict] = {}
        self._lock       = threading.RLock()

    def get_or_create_profile(self, address: str) -> dict:
        with self._lock:
            if address not in self._hub_profiles:
                self._hub_profiles[address] = {
                    "address":    address,
                    "did":        f"did:nebula:{address}",
                    "kyc_level":  0,
                    "verified":   False,
                    "joined_at":  time.time(),
                }
            return self._hub_profiles[address]

    def full_identity(self, address: str) -> dict:
        profile = self.get_or_create_profile(address)
        bal     = self._bc.utxo.balance(address)
        result  = {
            **profile,
            "balance_nbl": f"{bal/10**DECIMALS:.9f}",
        }
        if self._rep:
            result["reputation"] = self._rep.get_score(address)
        if self._compliance:
            result["compliance"] = self._compliance.compliance_report(address)
        return result

    def verify_identity(self, address: str,
                         kyc_level: int, evidence: str) -> bool:
        with self._lock:
            profile = self.get_or_create_profile(address)
            profile["kyc_level"] = kyc_level
            profile["verified"]  = kyc_level >= 1
            return True

    def hub_stats(self) -> dict:
        with self._lock:
            verified = sum(1 for p in self._hub_profiles.values()
                           if p["verified"])
        return {
            "total_profiles": len(self._hub_profiles),
            "verified":       verified,
        }


# ---- AdvancedDEXV2
class AdvancedDEXV2:
    """Advanced DEX v2 with concentrated liquidity pools."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._pools: Dict[str, ConcentratedLiquidityPool] = {}
        self._lock  = threading.RLock()

    def create_pool(self, token_a: str, token_b: str,
                     fee_tier: float = 0.003) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"CLMM:{token_a}:{token_b}:{fee_tier}".encode()
            ).hexdigest()[:10]
            self._pools[pid] = ConcentratedLiquidityPool(
                pid, token_a, token_b, fee_tier)
            return pid

    def add_liquidity(self, pool_id: str, lp: str,
                       tick_lower: int, tick_upper: int,
                       liquidity: float) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, "Pool not found"
            pos_id = pool.add_position(lp, tick_lower, tick_upper, liquidity)
            return True, pos_id

    def swap(self, pool_id: str, trader: str,
              token_in: str, amount_in: float) -> Tuple[bool, float]:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, 0.0
            out = pool.swap(token_in, amount_in)
            return out > 0, out

    def dex_v2_stats(self) -> dict:
        return {
            "total_pools": len(self._pools),
            "pool_types":  "Concentrated Liquidity (CLMM)",
        }


# ---- StateChannelV2
class StateChannelV2:
    """
    Payment channel v2 with multi-hop routing and HTLCs.
    """

    def __init__(self, alice: str, bob: str,
                  capacity: int, blockchain: 'NEBULABlockchain'):
        self.alice      = alice
        self.bob        = bob
        self.capacity   = capacity
        self._bc        = blockchain
        self.balance_a  = capacity
        self.balance_b  = 0
        self.state_num  = 0
        self.open       = True
        self.htlcs:     List[dict] = []

    def pay(self, payer: str, amount: int) -> Tuple[bool, str]:
        if not self.open:
            return False, "Channel closed"
        if payer == self.alice:
            if self.balance_a < amount:
                return False, "Insufficient balance"
            self.balance_a -= amount
            self.balance_b += amount
        else:
            if self.balance_b < amount:
                return False, "Insufficient balance"
            self.balance_b -= amount
            self.balance_a += amount
        self.state_num += 1
        return True, f"Payment {amount/10**DECIMALS:.6f} NBL (state #{self.state_num})"

    def add_htlc(self, payer: str, amount: int,
                  hash_lock: str, timeout: int) -> str:
        htlc_id = hashlib.sha256(
            f"HTLC:{payer}:{amount}:{hash_lock}".encode()
        ).hexdigest()[:12]
        self.htlcs.append({
            "id":       htlc_id,
            "payer":    payer,
            "amount":   amount,
            "hashlock": hash_lock,
            "timeout":  timeout,
            "settled":  False,
        })
        return htlc_id

    def settle_htlc(self, htlc_id: str, preimage: str) -> bool:
        htlc = next((h for h in self.htlcs if h["id"] == htlc_id), None)
        if not htlc or htlc["settled"]:
            return False
        if hashlib.sha256(preimage.encode()).hexdigest() != htlc["hashlock"]:
            return False
        htlc["settled"] = True
        ok, _ = self.pay(htlc["payer"], htlc["amount"])
        return ok

    def close(self) -> dict:
        self.open = False
        return {
            "channel_id": f"{self.alice[:8]}:{self.bob[:8]}",
            "final_a":    f"{self.balance_a/10**DECIMALS:.9f}",
            "final_b":    f"{self.balance_b/10**DECIMALS:.9f}",
            "states":     self.state_num,
        }

    def channel_info(self) -> dict:
        return {
            "alice":      self.alice,
            "bob":        self.bob,
            "capacity":   f"{self.capacity/10**DECIMALS:.9f}",
            "balance_a":  f"{self.balance_a/10**DECIMALS:.9f}",
            "balance_b":  f"{self.balance_b/10**DECIMALS:.9f}",
            "state":      self.state_num,
            "open":       self.open,
            "htlcs":      len(self.htlcs),
        }


# ---- PredictionMarketV2
class PredictionMarketV2:
    """
    Enhanced prediction market with LMSR pricing.
    Logarithmic Market Scoring Rule for automated market making.
    """

    LMSR_B = 100.0   # LMSR liquidity parameter

    def __init__(self, market_id: str, question: str,
                  outcomes: List[str],
                  blockchain: 'NEBULABlockchain'):
        self.market_id = market_id
        self.question  = question
        self.outcomes  = outcomes
        self._bc       = blockchain
        self._qtys:    Dict[str, float] = {o: 0.0 for o in outcomes}
        self._shares:  Dict[str, Dict[str, float]] = {}  # trader -> {outcome: shares}
        self.resolved  = False
        self.result    = None

    def _lmsr_cost(self, qtys: Dict[str, float]) -> float:
        import math
        return self.LMSR_B * math.log(
            sum(math.exp(q / self.LMSR_B) for q in qtys.values()))

    def buy_shares(self, trader: str, outcome: str,
                    amount: int) -> Tuple[bool, float]:
        if outcome not in self.outcomes:
            return False, 0.0
        if self._bc.utxo.balance(trader) < amount:
            return False, 0.0
        import math
        old_cost   = self._lmsr_cost(self._qtys)
        new_qtys   = dict(self._qtys)
        new_qtys[outcome] += amount / 10**DECIMALS
        new_cost   = self._lmsr_cost(new_qtys)
        price_paid = (new_cost - old_cost) * 10**DECIMALS
        if price_paid > amount:
            return False, 0.0
        self._qtys = new_qtys
        shares     = amount / (10**DECIMALS)
        if trader not in self._shares:
            self._shares[trader] = {}
        self._shares[trader][outcome] = (
            self._shares[trader].get(outcome, 0) + shares)
        return True, shares

    def get_price(self, outcome: str) -> float:
        import math
        total_exp = sum(math.exp(q / self.LMSR_B) for q in self._qtys.values())
        return math.exp(self._qtys[outcome] / self.LMSR_B) / total_exp

    def resolve(self, winning_outcome: str) -> bool:
        if winning_outcome not in self.outcomes:
            return False
        self.resolved = True
        self.result   = winning_outcome
        return True

    def claim_winnings(self, trader: str) -> Tuple[bool, int]:
        if not self.resolved:
            return False, 0
        shares = self._shares.get(trader, {}).get(self.result, 0)
        if shares <= 0:
            return False, 0
        payout = int(shares * 10**DECIMALS)
        del self._shares[trader][self.result]
        return True, payout

    def market_info(self) -> dict:
        prices = {o: f"{self.get_price(o)*100:.1f}%" for o in self.outcomes}
        return {
            "market_id": self.market_id,
            "question":  self.question,
            "prices":    prices,
            "resolved":  self.resolved,
            "result":    self.result,
        }


# ---- OrderbookAggregator
class OrderbookAggregator:
    """
    Aggregates order books across all NEBULA trading pairs.
    Provides unified liquidity view.
    """

    def __init__(self, order_book_mgr: 'OrderBookManager'):
        self._mgr = order_book_mgr

    def all_pairs(self) -> List[str]:
        return list(self._mgr._books.keys())

    def best_prices(self) -> List[dict]:
        results = []
        for pair, book in self._mgr._books.items():
            bid = book.best_bid()
            ask = book.best_ask()
            if bid or ask:
                results.append({
                    "pair":   pair,
                    "bid":    f"{bid:.6f}" if bid else "N/A",
                    "ask":    f"{ask:.6f}" if ask else "N/A",
                    "spread": f"{ask-bid:.6f}" if bid and ask else "N/A",
                })
        return results

    def aggregate_liquidity(self, pair: str,
                             depth: int = 10) -> dict:
        book = self._mgr._books.get(pair)
        if not book:
            return {}
        bids = book._bids[:depth]
        asks = book._asks[:depth]
        return {
            "pair":       pair,
            "bid_depth":  [{"price": b[0], "qty": b[1]} for b in bids],
            "ask_depth":  [{"price": a[0], "qty": a[1]} for a in asks],
            "total_bid":  sum(b[1] for b in bids),
            "total_ask":  sum(a[1] for a in asks),
        }


# ---- FeeOptimizer
class FeeOptimizer:
    """
    Optimizes transaction fees for NEBULA users.
    Suggests optimal fee for desired confirmation time.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._history: List[dict] = []

    def suggested_fee(self, confirm_in_blocks: int = 6) -> int:
        mp_size = self._bc.mempool.size()
        if confirm_in_blocks <= 1:
            return MIN_TX_FEE * 10
        elif confirm_in_blocks <= 3:
            return MIN_TX_FEE * 5
        elif confirm_in_blocks <= 6:
            return MIN_TX_FEE * 3
        else:
            return MIN_TX_FEE

    def batch_fee_estimate(self, tx_sizes: List[int],
                            confirm_in: int = 6) -> dict:
        rate    = self.suggested_fee(confirm_in)
        totals  = [rate * s for s in tx_sizes]
        return {
            "fee_rate":    f"{rate} Neb/byte",
            "per_tx":      [f"{f/10**DECIMALS:.9f}" for f in totals],
            "total":       f"{sum(totals)/10**DECIMALS:.9f} NBL",
            "confirm_in":  f"~{confirm_in} blocks ({confirm_in * TARGET_BLOCK_TIME // 60}m)",
        }

    def rbf_bump(self, current_fee: int,
                  bump_pct: float = 1.25) -> int:
        """Calculate RBF (Replace-By-Fee) bump amount."""
        return int(current_fee * bump_pct)

    def fee_savings_tips(self) -> List[str]:
        tips = [
            "Use SegWit addresses for 40% lower transaction size",
            "Batch multiple sends into one transaction",
            "Transact during off-peak hours (low mempool)",
            "Use fee estimation for optimal rate",
            "Consolidate UTXOs during low-fee periods",
        ]
        mp = self._bc.mempool.size()
        if mp > 5000:
            tips.insert(0, "⚠️ Mempool congested — consider waiting or using high fee")
        return tips


# ---- BlockRewardSchedule
class BlockRewardSchedule:
    """
    Comprehensive block reward schedule for NEBULA.
    Foundation allocation, validator rewards, etc.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def reward_breakdown(self, height: int = None) -> dict:
        h      = height or self._bc.height
        reward = mining_reward(h)
        found  = int(reward * FOUNDATION_RATE)
        miner  = reward - found
        return {
            "total_reward":     f"{reward/10**DECIMALS:.9f} NBL",
            "miner_reward":     f"{miner/10**DECIMALS:.9f} NBL",
            "foundation_alloc": f"{found/10**DECIMALS:.9f} NBL",
            "foundation_rate":  f"{FOUNDATION_RATE*100:.0f}%",
            "height":           h,
        }

    def cumulative_rewards(self, from_h: int = 0,
                            to_h: int = None) -> int:
        end   = to_h or self._bc.height
        total = 0
        h     = from_h
        while h <= end:
            total   += mining_reward(h)
            next_era = (h // HALVING_INTERVAL + 1) * HALVING_INTERVAL
            h        = min(next_era, end + 1)
        return total

    def future_rewards(self, years: int = 10) -> dict:
        cur     = self._bc.height
        future  = cur + years * 365 * 144
        cum     = self.cumulative_rewards(cur, future)
        return {
            "period":        f"{years} years",
            "future_rewards": f"{cum/10**DECIMALS:.3f} NBL",
            "daily_avg":     f"{cum/(years*365)/10**DECIMALS:.6f} NBL",
        }


# ---- ValidatorSelectionAlgorithm
class ValidatorSelectionAlgorithm:
    """
    Selects validators for block production in NEBULA PoS.
    Uses stake-weighted random selection with VRF.
    """

    def __init__(self, validator_set: 'ValidatorSetManager',
                  rng: 'OnChainRNG'):
        self._vs  = validator_set
        self._rng = rng

    def select_proposer(self, height: int) -> Optional[str]:
        """Select block proposer via stake-weighted VRF."""
        validators = self._vs.list_active_validators()
        if not validators:
            return None
        total_stake = sum(v.get("stake", 0) for v in validators)
        if total_stake == 0:
            return validators[0].get("address") if validators else None
        rand_val    = self._rng.random_int(height, total_stake)
        cumulative  = 0
        for v in validators:
            cumulative += v.get("stake", 0)
            if rand_val < cumulative:
                return v.get("address")
        return validators[-1].get("address")

    def select_committee(self, height: int,
                          size: int = 21) -> List[str]:
        """Select validator committee for a block."""
        validators = self._vs.list_active_validators()
        selected   = []
        for i in range(min(size, len(validators))):
            rand = self._rng.random_int(height, len(validators), i)
            idx  = rand % len(validators)
            addr = validators[idx].get("address", "")
            if addr and addr not in selected:
                selected.append(addr)
        return selected

    def selection_stats(self) -> dict:
        return {
            "active_validators": len(self._vs.list_active_validators()),
            "algorithm":         "Stake-Weighted VRF",
        }


# ---- CrossChainSwapV2
class CrossChainSwapV2:
    """
    Cross-chain atomic swaps v2 with improved UX.
    Supports NEBULA ↔ BTC, ETH, SOL, BNB.
    """

    TIMEOUT_BLOCKS = {
        "nebula":   200,
        "bitcoin":  6,
        "ethereum": 50,
        "solana":   100,
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._swaps: Dict[str, dict] = {}
        self._lock  = threading.RLock()

    def initiate(self, initiator: str, participant: str,
                  chain_a: str, amount_a: float,
                  chain_b: str, amount_b: float) -> str:
        with self._lock:
            secret     = secrets.token_bytes(32)
            hash_lock  = hashlib.sha256(secret).hexdigest()
            swap_id    = hashlib.sha256(
                f"XCS:{initiator}:{participant}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._swaps[swap_id] = {
                "swap_id":    swap_id,
                "initiator":  initiator,
                "participant": participant,
                "chain_a":    chain_a,
                "amount_a":   amount_a,
                "chain_b":    chain_b,
                "amount_b":   amount_b,
                "hash_lock":  hash_lock,
                "_secret":    secret.hex(),
                "status":     "initiated",
                "timeout":    self._bc.height +
                               self.TIMEOUT_BLOCKS.get(chain_a, 200),
            }
            return swap_id

    def reveal_and_complete(self, swap_id: str,
                             preimage: str) -> Tuple[bool, str]:
        with self._lock:
            swap = self._swaps.get(swap_id)
            if not swap:
                return False, "Swap not found"
            if hashlib.sha256(bytes.fromhex(preimage)).hexdigest() != swap["hash_lock"]:
                return False, "Invalid preimage"
            if self._bc.height > swap["timeout"]:
                swap["status"] = "expired"
                return False, "Swap expired"
            swap["status"] = "completed"
            return True, f"Swap completed: {swap['amount_a']} {swap['chain_a']} ↔ {swap['amount_b']} {swap['chain_b']}"

    def refund(self, swap_id: str, initiator: str) -> Tuple[bool, str]:
        with self._lock:
            swap = self._swaps.get(swap_id)
            if not swap or swap["initiator"] != initiator:
                return False, "Not found"
            if self._bc.height <= swap["timeout"]:
                return False, "Timeout not reached"
            swap["status"] = "refunded"
            return True, "Refunded"

    def swap_stats(self) -> dict:
        with self._lock:
            by_status = {}
            for s in self._swaps.values():
                k = s["status"]
                by_status[k] = by_status.get(k, 0) + 1
        return {"swaps": len(self._swaps), "by_status": by_status}


# ---- PortfolioRebalancer
class PortfolioRebalancer:
    """
    Automated portfolio rebalancer for NEBULA DeFi positions.
    Keeps target allocation ratios within threshold.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc         = blockchain
        self._oracle     = oracle
        self._portfolios: Dict[str, dict] = {}

    def set_target(self, owner: str,
                    targets: Dict[str, float],
                    rebalance_threshold: float = 0.05):
        """Set target allocation. targets = {'staking': 0.5, 'lp': 0.3, ...}"""
        assert abs(sum(targets.values()) - 1.0) < 0.001, "Must sum to 1"
        self._portfolios[owner] = {
            "targets":    targets,
            "threshold":  rebalance_threshold,
        }

    def check_drift(self, owner: str,
                     current: Dict[str, float]) -> List[dict]:
        """Check which allocations have drifted beyond threshold."""
        portfolio = self._portfolios.get(owner)
        if not portfolio:
            return []
        total = sum(current.values()) or 1
        drifts = []
        for asset, target in portfolio["targets"].items():
            actual = current.get(asset, 0) / total
            drift  = actual - target
            if abs(drift) > portfolio["threshold"]:
                drifts.append({
                    "asset":  asset,
                    "target": f"{target*100:.0f}%",
                    "actual": f"{actual*100:.1f}%",
                    "drift":  f"{drift*100:+.1f}%",
                    "action": "reduce" if drift > 0 else "increase",
                })
        return drifts

    def rebalance_plan(self, owner: str,
                        current: Dict[str, float]) -> List[dict]:
        """Generate rebalance action plan."""
        total  = sum(current.values()) or 1
        drifts = self.check_drift(owner, current)
        plan   = []
        for d in drifts:
            asset      = d["asset"]
            target_pct = float(d["target"].rstrip('%')) / 100
            actual_pct = float(d["actual"].rstrip('%')) / 100
            diff       = (target_pct - actual_pct) * total
            plan.append({
                "asset":  asset,
                "action": d["action"],
                "amount": f"{abs(diff):.4f}",
            })
        return plan


# ---- OnChainAnalyticsV2
class OnChainAnalyticsV2:
    """
    Advanced on-chain analytics for NEBULA.
    Whale tracking, flow analysis, sentiment indicators.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._snapshots: List[dict] = []

    def whale_movements(self, min_nbl: float = 10_000) -> List[dict]:
        """Detect large wallet movements."""
        threshold = int(min_nbl * 10**DECIMALS)
        whales    = []
        for txid, tx in list(self._bc.mempool._txs.items())[:500]:
            if tx.total_output() >= threshold:
                whales.append({
                    "txid":    txid,
                    "volume":  f"{tx.total_output()/10**DECIMALS:.3f} NBL",
                    "outputs": len(tx.outputs),
                })
        return sorted(whales, key=lambda w: -float(w["volume"].split()[0]))[:20]

    def holder_distribution_snapshot(self) -> dict:
        addrs = list(self._bc.utxo._addr_idx.keys())
        bals  = sorted([self._bc.utxo.balance(a) for a in addrs], reverse=True)
        total = sum(bals) or 1
        buckets = {
            "whale (>100k NBL)":  sum(1 for b in bals if b >= 100_000*10**DECIMALS),
            "large (10k-100k)":   sum(1 for b in bals if 10_000*10**DECIMALS <= b < 100_000*10**DECIMALS),
            "medium (1k-10k)":    sum(1 for b in bals if 1_000*10**DECIMALS <= b < 10_000*10**DECIMALS),
            "small (100-1k)":     sum(1 for b in bals if 100*10**DECIMALS <= b < 1_000*10**DECIMALS),
            "micro (<100 NBL)":   sum(1 for b in bals if 0 < b < 100*10**DECIMALS),
        }
        snap = {
            "height":       self._bc.height,
            "total_holders": len([b for b in bals if b > 0]),
            "buckets":      buckets,
            "gini":         self._gini(bals),
        }
        self._snapshots.append(snap)
        return snap

    def _gini(self, vals: List[float]) -> float:
        if not vals or sum(vals) == 0:
            return 0
        n   = len(vals)
        s   = sorted(vals)
        sm  = sum(s)
        g   = sum((2*i - n - 1) * s[i] for i in range(n))
        return round(g / (n * sm), 4) if sm > 0 else 0

    def exchange_flow(self) -> dict:
        """Estimate net exchange inflow/outflow."""
        mempool_txs = list(self._bc.mempool._txs.values())[:200]
        inflow  = sum(tx.total_output() for tx in mempool_txs
                      if len(tx.outputs) == 1)
        outflow = sum(tx.total_output() for tx in mempool_txs
                      if len(tx.outputs) > 3)
        return {
            "estimated_inflow":  f"{inflow/10**DECIMALS:.3f} NBL",
            "estimated_outflow": f"{outflow/10**DECIMALS:.3f} NBL",
            "net_flow":          f"{(inflow-outflow)/10**DECIMALS:+.3f} NBL",
            "sentiment":         "bullish" if inflow > outflow else "bearish",
        }


# ---- DelegatedStaking
class DelegatedStaking:
    """
    Delegated Proof-of-Stake for NEBULA.
    Token holders delegate to validators without losing custody.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  validator_set: 'ValidatorSetManager'):
        self._bc     = blockchain
        self._vs     = validator_set
        self._delegations: Dict[str, Dict[str, int]] = {}  # validator -> {delegator: amount}
        self._rewards:     Dict[str, int]             = {}
        self._lock   = threading.RLock()

    def delegate(self, delegator: str, validator: str,
                  amount: int) -> Tuple[bool, str]:
        with self._lock:
            if not self._vs.get_validator(validator):
                return False, "Validator not found"
            if self._bc.utxo.balance(delegator) < amount:
                return False, "Insufficient balance"
            if validator not in self._delegations:
                self._delegations[validator] = {}
            self._delegations[validator][delegator] = (
                self._delegations[validator].get(delegator, 0) + amount)
            return True, f"Delegated {amount/10**DECIMALS:.6f} NBL to {validator[:8]}"

    def undelegate(self, delegator: str,
                    validator: str,
                    amount: int = None) -> Tuple[bool, int]:
        with self._lock:
            d = self._delegations.get(validator, {})
            staked = d.get(delegator, 0)
            if staked == 0:
                return False, 0
            withdraw = amount or staked
            withdraw = min(withdraw, staked)
            d[delegator] = staked - withdraw
            if d[delegator] == 0:
                del d[delegator]
            return True, withdraw

    def total_delegated(self, validator: str) -> int:
        return sum(self._delegations.get(validator, {}).values())

    def delegator_info(self, delegator: str) -> List[dict]:
        result = []
        for val, d in self._delegations.items():
            if delegator in d:
                result.append({
                    "validator": val,
                    "amount":    f"{d[delegator]/10**DECIMALS:.6f} NBL",
                    "rewards":   f"{self._rewards.get(delegator, 0)/10**DECIMALS:.6f}",
                })
        return result

    def distribute_block_rewards(self, block_reward: int,
                                   proposer: str):
        total_del = self.total_delegated(proposer)
        if total_del == 0:
            return
        for delegator, amount in self._delegations.get(proposer, {}).items():
            share = int(block_reward * 0.7 * amount / total_del)
            self._rewards[delegator] = self._rewards.get(delegator, 0) + share

    def delegation_stats(self) -> dict:
        total = sum(
            sum(d.values())
            for d in self._delegations.values()
        )
        return {
            "total_delegated_nbl": f"{total/10**DECIMALS:.3f}",
            "validators_with_delegations": len(self._delegations),
        }


# ---- IDOParameters
class IDOParameters:
    """Parameters for an Initial DEX Offering."""

    def __init__(self, token_symbol: str, total_raise: float,
                  hard_cap: float, price_per_token: float,
                  min_buy: float, max_buy: float,
                  start_block: int, duration_blocks: int,
                  vesting_days: int = 90):
        self.token_symbol    = token_symbol
        self.total_raise     = total_raise
        self.hard_cap        = hard_cap
        self.price_per_token = price_per_token
        self.min_buy         = int(min_buy * 10**DECIMALS)
        self.max_buy         = int(max_buy * 10**DECIMALS)
        self.start_block     = start_block
        self.end_block       = start_block + duration_blocks
        self.vesting_days    = vesting_days


# ---- LaunchpadV2
class LaunchpadV2:
    """Token launchpad v2 with whitelist, vesting, and fair launch."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._idos: Dict[str, dict] = {}
        self._lock  = threading.RLock()

    def create_ido(self, creator: str,
                    params: IDOParameters) -> str:
        with self._lock:
            ido_id = hashlib.sha256(
                f"IDO:{creator}:{params.token_symbol}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._idos[ido_id] = {
                "id":         ido_id,
                "creator":    creator,
                "symbol":     params.token_symbol,
                "hard_cap":   params.hard_cap,
                "price":      params.price_per_token,
                "min_buy":    params.min_buy,
                "max_buy":    params.max_buy,
                "start":      params.start_block,
                "end":        params.end_block,
                "vesting_d":  params.vesting_days,
                "raised":     0.0,
                "participants": {},
                "status":     "upcoming",
            }
            return ido_id

    def participate(self, ido_id: str, participant: str,
                     amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            ido = self._idos.get(ido_id)
            if not ido:
                return False, "IDO not found"
            h = self._bc.height
            if h < ido["start"]:
                return False, "IDO not started"
            if h > ido["end"]:
                return False, "IDO ended"
            amount = int(amount_nbl * 10**DECIMALS)
            if amount < ido["min_buy"]:
                return False, "Below minimum buy"
            current = ido["participants"].get(participant, 0)
            if current + amount > ido["max_buy"]:
                return False, "Exceeds maximum allocation"
            if ido["raised"] + amount_nbl > ido["hard_cap"]:
                return False, "Hard cap reached"
            if self._bc.utxo.balance(participant) < amount:
                return False, "Insufficient balance"
            ido["participants"][participant] = current + amount
            ido["raised"] += amount_nbl
            tokens = amount_nbl / ido["price"]
            return True, f"Participated: {tokens:.4f} {ido['symbol']} allocated"

    def ido_info(self, ido_id: str) -> Optional[dict]:
        ido = self._idos.get(ido_id)
        if not ido:
            return None
        return {
            **{k: v for k, v in ido.items() if k != "participants"},
            "participants": len(ido["participants"]),
            "fill_pct":     f"{ido['raised']/max(1,ido['hard_cap'])*100:.1f}%",
        }


# ---- GaslessRelay
class GaslessRelay:
    """
    Gasless transaction relay — users never need NBL for fees.
    Protocol or dApp pays fees, users just sign.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  relayer: str = FOUNDATION_ADDRESS,
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._relayer = relayer
        self._oracle  = oracle
        self._relayed: List[dict] = []
        self._sponsored: Dict[str, int] = {}   # dapp -> total sponsored

    def sponsor(self, dapp: str,
                 budget_nbl: float) -> bool:
        budget = int(budget_nbl * 10**DECIMALS)
        if self._bc.utxo.balance(dapp) < budget:
            return False
        self._sponsored[dapp] = self._sponsored.get(dapp, 0) + budget
        return True

    def relay_for(self, user: str, dapp: str,
                   tx: 'Transaction') -> Tuple[bool, str]:
        """Relay a transaction, billing the dApp."""
        fee = MIN_TX_FEE * tx.byte_size()
        if self._sponsored.get(dapp, 0) < fee:
            return False, "Insufficient dApp sponsorship"
        self._sponsored[dapp] -= fee
        self._relayed.append({
            "user":   user,
            "dapp":   dapp,
            "txid":   tx.txid,
            "fee":    fee,
            "ts":     time.time(),
        })
        ok, msg = self._bc.mempool.submit(tx)
        return ok, f"Gasless relay: {msg}"

    def relay_stats(self) -> dict:
        total_sponsored = sum(self._sponsored.values())
        total_relayed   = len(self._relayed)
        total_fees_paid = sum(r["fee"] for r in self._relayed)
        return {
            "total_relayed":   total_relayed,
            "total_fees_paid": f"{total_fees_paid/10**DECIMALS:.6f} NBL",
            "dapps":           len(self._sponsored),
            "remaining_budget": f"{total_sponsored/10**DECIMALS:.3f}",
        }


# ---- AutoRebalancingVault
class AutoRebalancingVault:
    """
    Vault that automatically rebalances between assets.
    Maintains target allocation through periodic rebalancing.
    """

    def __init__(self, vault_id: str,
                  targets: Dict[str, float],
                  blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self.vault_id    = vault_id
        self.targets     = targets
        self._bc         = blockchain
        self._oracle     = oracle
        self._holdings:  Dict[str, float] = {k: 0.0 for k in targets}
        self._rebalances: int = 0
        self._lock       = threading.RLock()

    def deposit(self, asset: str, amount: float) -> bool:
        with self._lock:
            if asset not in self.targets:
                return False
            self._holdings[asset] = self._holdings.get(asset, 0) + amount
            return True

    def total_value_nbl(self) -> float:
        total = 0.0
        for asset, amount in self._holdings.items():
            price = (self._oracle.price(f"{asset}/NBL")
                     if self._oracle and asset != "NBL" else 1.0) or 1.0
            total += amount * price
        return total

    def current_weights(self) -> Dict[str, float]:
        total = self.total_value_nbl() or 1
        price = lambda a: (self._oracle.price(f"{a}/NBL")
                            if self._oracle and a != "NBL" else 1.0) or 1.0
        return {
            asset: (amount * price(asset)) / total
            for asset, amount in self._holdings.items()
        }

    def rebalance(self) -> List[dict]:
        with self._lock:
            current = self.current_weights()
            trades  = []
            total   = self.total_value_nbl()
            for asset, target in self.targets.items():
                actual = current.get(asset, 0)
                diff   = target - actual
                if abs(diff) > 0.02:
                    trade_val = diff * total
                    trades.append({
                        "asset":  asset,
                        "action": "buy" if diff > 0 else "sell",
                        "amount": f"{abs(trade_val):.4f} NBL worth",
                    })
            self._rebalances += 1
            return trades

    def vault_info(self) -> dict:
        with self._lock:
            weights = self.current_weights()
        return {
            "vault_id":    self.vault_id,
            "total_value": f"{self.total_value_nbl():.4f} NBL",
            "targets":     {k: f"{v*100:.0f}%" for k, v in self.targets.items()},
            "current":     {k: f"{v*100:.1f}%" for k, v in weights.items()},
            "rebalances":  self._rebalances,
        }


# ---- KeeperBot
class KeeperBot:
    """
    Keeper bot for NEBULA protocol maintenance.
    Executes liquidations, distributions, and rebalancing.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  address: str):
        self._bc       = blockchain
        self.address   = address
        self._executions: List[dict] = []

    def run_liquidations(self, liquidation_engine: 'LiquidationEngine') -> int:
        underwater = liquidation_engine.scan_for_liquidations()
        count = 0
        for pos in underwater:
            ok, result = liquidation_engine.liquidate(
                self.address, pos["key"], pos["debt"])
            if ok:
                count += 1
                self._executions.append({
                    "type":   "liquidation",
                    "target": pos["key"],
                    "profit": result.get("bonus", 0),
                    "block":  self._bc.height,
                })
        return count

    def run_reward_distributions(self,
                                  distributor: 'RewardsDistributor') -> int:
        return 0   # Simplified

    def run_oracle_updates(self,
                            oracle: 'OracleV2') -> int:
        # / previously raised NotImplementedError which crashed
        #   the entire keeper process if this method was called.
        #   Now logs a clear warning and returns 0 (no updates performed) so the keeper
        #   loop continues safely.  Replace this body with a real price-feed integration
        #   (on-chain TWAP, Chainlink-style oracle, or CEX API) before mainnet launch.
        log.warning(
            "run_oracle_updates(): no real price feed configured — "
            "oracle prices NOT updated this cycle. "
            "Integrate a real feed (TWAP / Chainlink / CEX API) before mainnet."
        )
        return 0

    def keeper_stats(self) -> dict:
        by_type = {}
        for e in self._executions:
            t = e["type"]
            by_type[t] = by_type.get(t, 0) + 1
        return {
            "keeper":     self.address,
            "executions": len(self._executions),
            "by_type":    by_type,
        }


# ---- NEBULADevTools
class NEBULADevTools:
    """
    Developer toolbox for building on NEBULA.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        _enable_dev_mode(self._bc, 'NEBULADevTools')   # v10.9: fail-closed (was: forced _dev_mode=True)

    def create_test_wallet(self, fund_nbl: float = 1000) -> dict:
        """Create and fund a test wallet."""
        wallet = NEBULAWallet.generate()
        self._bc.fund_address(wallet.first_address, fund_nbl)
        return {
            "address":     wallet.first_address,
            "mnemonic":    wallet.mnemonic,
            "balance":     f"{fund_nbl} NBL (test funds)",
        }

    def deploy_test_contract(self, deployer: str,
                              contract_type: str = "erc20") -> dict:
        """Deploy a test contract."""
        factory = ContractFactory(self._bc)
        if contract_type == "erc20":
            cid = factory.deploy_erc20(
                deployer, "TestToken", "TEST", 18, 1_000_000)
            return {"contract_id": cid, "type": "ERC20"}
        return {"error": "Unknown contract type"}

    def simulate_transactions(self, n: int = 10) -> dict:
        """Generate sample transactions for testing."""
        w = NEBULAWallet.generate()
        self._bc.fund_address(w.first_address, n * 100)
        txids = []
        for _ in range(n):
            dest = NEBULAWallet.generate().first_address
            txid = "test_" + secrets.token_hex(16)
            txids.append(txid)
        return {"generated": n, "txids": txids[:5]}

    def inspect_address(self, address: str) -> dict:
        bal   = self._bc.utxo.balance(address)
        utxos = self._bc.utxo.get_by_address(address)  # FIX
        return {
            "address":     address,
            "balance_raw": bal,
            "balance_nbl": f"{bal/10**DECIMALS:.9f}",
            "utxo_count":  len(utxos),
            "utxos":       utxos[:5],
        }

    def sdk_snippet(self, task: str) -> str:
        snippets = {
            "wallet": "wallet = NEBULAWallet.generate()\nprint(wallet.first_address)",
            "stake":  "engine = StakingEngine(bc)\nok, msg = engine.stake(addr, 100*10**9)",
            "swap":   "dex = NEBULADex(bc)\nok, msg, out = dex.swap_amm(addr, 'NBL', 'USDT', 100)",
            "nft":    "nft = NBL721Registry()\ncid = nft.create_collection(creator, 'Name', 'SYM', 'Desc')",
        }
        return snippets.get(task, "# See docs at https://nebula-nbl.io/docs")


# ---- CommunityHub
class CommunityHub:
    """NEBULA community hub — forums, ambassadors, grants, events."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._ambassadors: Dict[str, dict] = {}
        self._events:      List[dict]      = []
        self._feedback:    List[dict]      = []
        self._lock         = threading.RLock()

    def register_ambassador(self, address: str, name: str,
                              region: str, handles: dict = None) -> bool:
        with self._lock:
            if address in self._ambassadors:
                return False
            self._ambassadors[address] = {
                "address":  address,
                "name":     name,
                "region":   region,
                "handles":  handles or {},
                "joined":   time.time(),
                "points":   0,
            }
            return True

    def add_event(self, title: str, event_type: str,
                   date: str, organizer: str,
                   description: str = "") -> str:
        with self._lock:
            eid = hashlib.sha256(
                f"EVENT:{title}:{date}:{time.time()}".encode()
            ).hexdigest()[:8]
            self._events.append({
                "id":          eid,
                "title":       title,
                "type":        event_type,
                "date":        date,
                "organizer":   organizer,
                "description": description,
            })
            return eid

    def submit_feedback(self, author: str, category: str,
                         message: str) -> str:
        with self._lock:
            fid = hashlib.sha256(
                f"FB:{author}:{time.time()}".encode()
            ).hexdigest()[:8]
            self._feedback.append({
                "id":       fid,
                "author":   author,
                "category": category,
                "message":  message[:500],
                "ts":       time.time(),
            })
            return fid

    def community_stats(self) -> dict:
        return {
            "ambassadors": len(self._ambassadors),
            "events":      len(self._events),
            "feedback":    len(self._feedback),
            "regions":     list(set(a["region"]
                               for a in self._ambassadors.values())),
        }
