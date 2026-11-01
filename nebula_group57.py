"""NEBULA group57 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. DailyMetricsCollector  (orig. lines 86863-86888)
   2. ProtocolKPITracker  (orig. lines 86890-86908)
   3. NebulaSDKPython  (orig. lines 86912-86943)
   4. NebulaContractSDK  (orig. lines 86945-86965)
   5. NEBULAJavascriptSDKDoc  (orig. lines 86967-86978)
   6. NEBULAContractABI  (orig. lines 86980-86998)
   7. NEBULATestnetConfig  (orig. lines 87000-87015)
   8. NEBULAMainnetConfig  (orig. lines 87017-87033)
   9. EnhancedBlockTemplate  (orig. lines 87047-87071)
  10. NetworkTopologyMap  (orig. lines 87074-87099)
  11. LiquidityPoolMath  (orig. lines 87103-87133)
  12. DeFiMath  (orig. lines 87135-87161)
  13. YieldMath  (orig. lines 87163-87185)
  14. StakingCalculator  (orig. lines 87187-87218)
  15. LendingCalculator  (orig. lines 87220-87252)
  16. TokenomicsAnalysis  (orig. lines 87254-87282)
  17. NEBULAHealthScore  (orig. lines 87286-87305)
  18. NEBULAStatusPage  (orig. lines 87307-87330)
  19. NEBULAWhitepaper  (orig. lines 87332-87362)
  20. NEBULACommunityStats  (orig. lines 87364-87390)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): InterestRateCalculator, NEBULABlockchain, NEBULAWallet
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

MAX_TX_PER_BLOCK       = 3000

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

MAGIC_BYTES            = 0x4E424C4D   # "NBLM" — NEBULA Mainnet magic integer

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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- DailyMetricsCollector
class DailyMetricsCollector:
    """Collects daily on-chain metrics."""
    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc   = blockchain
        self._data: List[dict] = []

    def collect(self) -> dict:
        data = {
            "date":    time.strftime('%Y-%m-%d'),
            "height":  self._bc.height,
            "supply":  self._bc.utxo.total_supply(),
            "mempool": self._bc.mempool.size(),
            "utxos":   self._bc.utxo.size(),
        }
        self._data.append(data)
        return data

    def trend(self, metric: str, days: int = 7) -> Optional[float]:
        if len(self._data) < 2:
            return None
        recent = self._data[-days:]
        if len(recent) < 2:
            return None
        first = recent[0].get(metric, 0)
        last  = recent[-1].get(metric, 0)
        return (last - first) / max(1, first) * 100


# ---- ProtocolKPITracker
class ProtocolKPITracker:
    """Tracks key performance indicators over time."""
    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc   = blockchain
        self._kpis: Dict[str, List[float]] = {}

    def record(self, kpi: str, value: float):
        if kpi not in self._kpis:
            self._kpis[kpi] = []
        self._kpis[kpi].append(value)
        if len(self._kpis[kpi]) > 365:
            self._kpis[kpi].pop(0)

    def avg(self, kpi: str) -> Optional[float]:
        vals = self._kpis.get(kpi, [])
        return sum(vals) / len(vals) if vals else None

    def summary(self) -> dict:
        return {k: f"{self.avg(k):.4f}" for k in self._kpis}


# ---- NebulaSDKPython
class NebulaSDKPython:
    """Python SDK for building on NEBULA."""
    VERSION = "1.0.0"

    def __init__(self, rpc_url: str = "https://rpc.nebula-nbl.io"):
        self.rpc_url  = rpc_url
        self._bc      = NEBULABlockchain()

    def new_wallet(self) -> dict:
        w = NEBULAWallet.generate()
        return {"address": w.first_address, "mnemonic": w.mnemonic}

    def get_balance(self, address: str) -> float:
        return self._bc.utxo.balance(address) / 10**DECIMALS

    def build_transfer_tx(self, from_addr: str,
                           to_addr: str,
                           amount_nbl: float) -> dict:
        amount = int(amount_nbl * 10**DECIMALS)
        return {
            "from":   from_addr,
            "to":     to_addr,
            "amount": amount,
            "fee":    MIN_TX_FEE * 250,
        }

    def sdk_info(self) -> dict:
        return {
            "version":  self.VERSION,
            "language": "Python",
            "chain_id": CHAIN_ID,
        }


# ---- NebulaContractSDK
class NebulaContractSDK:
    """SDK for interacting with NEBULA smart contracts."""
    def __init__(self, blockchain: 'NEBULABlockchain',
                  factory: 'ContractFactory'):
        self._bc      = blockchain
        self._factory = factory

    def deploy(self, deployer: str, name: str,
                symbol: str, supply: float) -> str:
        return self._factory.deploy_erc20(
            deployer, name, symbol, 18, supply)

    def call(self, contract_id: str, caller: str,
              fn: str, args: dict = None) -> Any:
        result, events = self._factory.call_contract(
            contract_id, caller, fn, args)
        return result

    def events(self, contract_id: str) -> List[dict]:
        contract = self._factory.get_contract(contract_id)
        return contract.state._events if contract else []


# ---- NEBULAJavascriptSDKDoc
class NEBULAJavascriptSDKDoc:
    """Documentation for NEBULA JavaScript SDK."""
    @staticmethod
    def usage_examples() -> dict:
        return {
            "install":    "npm install @nebula-nbl/sdk",
            "connect":    "const nbl = new NEBULAClient('mainnet')",
            "balance":    "await nbl.getBalance(address)",
            "transfer":   "await nbl.transfer(to, amount)",
            "stake":      "await nbl.stake(amount, pool_id)",
            "swap":       "await nbl.dex.swap('NBL', 'USDT', amount)",
        }


# ---- NEBULAContractABI
class NEBULAContractABI:
    """Generates ABI for NEBULA smart contracts."""
    @staticmethod
    def erc20_abi() -> List[dict]:
        functions = [
            "balanceOf(address)", "transfer(address,uint256)",
            "approve(address,uint256)", "transferFrom(address,address,uint256)",
            "totalSupply()", "allowance(address,address)",
        ]
        return [{"name": f.split("(")[0], "signature": f, "type": "function"}
                for f in functions]

    @staticmethod
    def staking_abi() -> List[dict]:
        return [
            {"name": "stake",   "signature": "stake(uint256,string)", "type": "function"},
            {"name": "unstake", "signature": "unstake(string)", "type": "function"},
            {"name": "claim",   "signature": "claimRewards()", "type": "function"},
        ]


# ---- NEBULATestnetConfig
class NEBULATestnetConfig:
    """Testnet configuration for NEBULA."""
    CHAIN_ID    = 9999
    RPC_URL     = "https://testnet-rpc.nebula-nbl.io"
    FAUCET_URL  = "https://faucet.nebula-nbl.io"
    EXPLORER    = "https://testnet-explorer.nebula-nbl.io"
    MAGIC_BYTES = 0x4E424C54

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "chain_id":   cls.CHAIN_ID,
            "rpc":        cls.RPC_URL,
            "faucet":     cls.FAUCET_URL,
            "explorer":   cls.EXPLORER,
        }


# ---- NEBULAMainnetConfig
class NEBULAMainnetConfig:
    """Mainnet configuration for NEBULA."""
    CHAIN_ID    = CHAIN_ID
    RPC_URL     = "https://rpc.nebula-nbl.io"
    WS_URL      = "wss://ws.nebula-nbl.io"
    EXPLORER    = "https://explorer.nebula-nbl.io"
    GITHUB      = ""

    @classmethod
    def to_dict(cls) -> dict:
        return {
            "chain_id":  cls.CHAIN_ID,
            "rpc":       cls.RPC_URL,
            "ws":        cls.WS_URL,
            "explorer":  cls.EXPLORER,
            "github":    cls.GITHUB,
        }


# ---- EnhancedBlockTemplate
class EnhancedBlockTemplate:
    """Block template with advanced fee optimization."""
    def __init__(self, bc: 'NEBULABlockchain', miner: str):
        self._bc    = bc
        self._miner = miner

    def optimal_template(self) -> dict:
        h     = self._bc.height + 1
        txs   = sorted(
            self._bc.mempool._txs.values(),
            key=lambda tx: tx.byte_size()
        )[:MAX_TX_PER_BLOCK - 1]
        reward = mining_reward(h)
        fees   = sum(
            tx.total_output() for tx in txs
            if not tx.coinbase_data
        )
        return {
            "height":    h,
            "reward":    f"{reward/10**DECIMALS:.9f} NBL",
            "fees":      f"{fees/10**DECIMALS:.9f} NBL",
            "total":     f"{(reward+fees)/10**DECIMALS:.9f} NBL",
            "tx_count":  len(txs) + 1,
            "miner":     self._miner,
        }


# ---- NetworkTopologyMap
class NetworkTopologyMap:
    """Visual topology map of the NEBULA network."""
    def __init__(self):
        self._nodes: List[dict] = []
        self._connections: List[Tuple[str, str]] = []

    def add_node(self, node_id: str, lat: float,
                  lon: float, region: str):
        self._nodes.append({
            "id":     node_id,
            "lat":    lat,
            "lon":    lon,
            "region": region,
        })

    def add_connection(self, n1: str, n2: str):
        self._connections.append((n1, n2))

    def topology_summary(self) -> dict:
        regions = list(set(n["region"] for n in self._nodes))
        return {
            "total_nodes":     len(self._nodes),
            "connections":     len(self._connections),
            "regions":         regions,
            "avg_connections": len(self._connections) / max(1, len(self._nodes)),
        }


# ---- LiquidityPoolMath
class LiquidityPoolMath:
    """Mathematical utilities for liquidity pool calculations."""

    @staticmethod
    def k_value(reserve_a: float, reserve_b: float) -> float:
        return reserve_a * reserve_b

    @staticmethod
    def output_given_input(amount_in: float, reserve_in: float,
                            reserve_out: float, fee: float = 0.003) -> float:
        amount_with_fee = amount_in * (1 - fee)
        return (amount_with_fee * reserve_out) / (reserve_in + amount_with_fee)

    @staticmethod
    def input_given_output(amount_out: float, reserve_in: float,
                            reserve_out: float, fee: float = 0.003) -> float:
        return (reserve_in * amount_out) / ((reserve_out - amount_out) * (1 - fee))

    @staticmethod
    def lp_tokens_for_deposit(amount_a: float, total_reserve_a: float,
                               total_lp: float) -> float:
        if total_reserve_a == 0:
            return amount_a
        return amount_a / total_reserve_a * total_lp

    @staticmethod
    def il_formula(price_ratio: float) -> float:
        """Impermanent loss formula: 2*sqrt(r)/(1+r) - 1"""
        import math
        r = price_ratio
        return 2 * math.sqrt(r) / (1 + r) - 1


# ---- DeFiMath
class DeFiMath:
    """General DeFi mathematical utilities."""

    @staticmethod
    def apy_to_apr(apy: float, compounds: int = 365) -> float:
        return compounds * ((1 + apy) ** (1 / compounds) - 1)

    @staticmethod
    def apr_to_apy(apr: float, compounds: int = 365) -> float:
        return (1 + apr / compounds) ** compounds - 1

    @staticmethod
    def compound_interest(principal: float, rate: float,
                           periods: int) -> float:
        return principal * (1 + rate) ** periods

    @staticmethod
    def liquidation_price(collateral: float, debt: float,
                           liquidation_threshold: float = 0.8) -> float:
        return debt / (collateral * liquidation_threshold) if collateral > 0 else 0

    @staticmethod
    def health_factor(collateral_usd: float, debt_usd: float,
                       threshold: float = 0.8) -> float:
        if debt_usd <= 0:
            return float('inf')
        return collateral_usd * threshold / debt_usd


# ---- YieldMath
class YieldMath:
    """Yield calculation utilities."""

    @staticmethod
    def daily_yield(principal: float, apy: float) -> float:
        return principal * apy / 365

    @staticmethod
    def weekly_yield(principal: float, apy: float) -> float:
        return principal * apy / 52

    @staticmethod
    def monthly_yield(principal: float, apy: float) -> float:
        return principal * apy / 12

    @staticmethod
    def time_to_double(apy: float) -> float:
        """Rule of 72 — years to double investment."""
        return 72 / (apy * 100) if apy > 0 else float('inf')

    @staticmethod
    def effective_apy_with_fees(gross_apy: float, fee_pct: float = 0.02) -> float:
        return gross_apy * (1 - fee_pct)


# ---- StakingCalculator
class StakingCalculator:
    """Staking reward calculator for users."""

    APY_TIERS = {
        "flexible":  0.05,
        "30d":       0.08,
        "90d":       0.12,
        "180d":      0.18,
        "365d":      0.25,
    }

    def calculate(self, amount_nbl: float,
                   tier: str = "90d",
                   period_days: int = 90) -> dict:
        apy      = self.APY_TIERS.get(tier, 0.12)
        rewards  = amount_nbl * apy * period_days / 365
        compound = DeFiMath.compound_interest(amount_nbl, apy/365, period_days)
        return {
            "principal":      f"{amount_nbl:.3f} NBL",
            "tier":           tier,
            "apy":            f"{apy*100:.0f}%",
            "period":         f"{period_days} days",
            "simple_rewards": f"{rewards:.6f} NBL",
            "compound_total": f"{compound:.6f} NBL",
            "effective_apy":  f"{(compound/amount_nbl-1)*365/period_days*100:.2f}%",
        }

    def compare_tiers(self, amount_nbl: float = 1000) -> List[dict]:
        return [
            self.calculate(amount_nbl, tier, int(tier.rstrip('d')) if 'd' in tier else 30)
            for tier in ["30d", "90d", "180d", "365d"]
        ]


# ---- LendingCalculator
class LendingCalculator:
    """Lending rate calculator for NEBULA."""

    def __init__(self):
        self._rate_model = InterestRateCalculator()

    def estimate_borrow_cost(self, amount: float,
                              asset: str,
                              utilization: float,
                              days: int) -> dict:
        rate   = self._rate_model.rate(utilization)
        cost   = amount * rate * days / 365
        return {
            "asset":        asset,
            "amount":       f"{amount:.4f}",
            "utilization":  f"{utilization*100:.0f}%",
            "borrow_rate":  f"{rate*100:.2f}% APR",
            "daily_cost":   f"{cost/days:.6f}",
            "total_cost":   f"{cost:.6f}",
            "repay_total":  f"{amount+cost:.6f}",
        }

    def supply_yield_estimate(self, amount: float,
                               utilization: float,
                               days: int) -> dict:
        borrow_rate = self._rate_model.rate(utilization)
        supply_rate = borrow_rate * utilization * 0.90
        yield_amt   = amount * supply_rate * days / 365
        return {
            "supply_amount": f"{amount:.4f}",
            "supply_rate":   f"{supply_rate*100:.2f}% APY",
            "yield":         f"{yield_amt:.6f}",
        }


# ---- TokenomicsAnalysis
class TokenomicsAnalysis:
    """Analyzes NEBULA tokenomics comprehensively."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def circulating_supply(self) -> float:
        return self._bc.utxo.total_supply() / 10**DECIMALS

    def inflation_rate(self) -> float:
        h       = self._bc.height
        annual  = mining_reward(h) * 365 * 144
        supply  = self._bc.utxo.total_supply()
        return annual / max(1, supply)

    def scarcity_metrics(self) -> dict:
        supply   = self.circulating_supply()
        max_s    = MAX_SUPPLY / 10**DECIMALS
        pct_left = (max_s - supply) / max_s * 100
        h        = self._bc.height
        next_h   = ((h // HALVING_INTERVAL) + 1) * HALVING_INTERVAL
        return {
            "circulating":   f"{supply:,.3f} NBL",
            "max_supply":    f"{max_s:,.0f} NBL",
            "mined_pct":     f"{supply/max_s*100:.4f}%",
            "remaining_pct": f"{pct_left:.4f}%",
            "blocks_to_halving": next_h - h,
            "inflation_rate": f"{self.inflation_rate()*100:.4f}%/year",
        }


# ---- NEBULAHealthScore
class NEBULAHealthScore:
    """Computes an overall health score for the NEBULA ecosystem."""

    def __init__(self, bc: 'NEBULABlockchain'):
        self._bc = bc

    def score(self) -> dict:
        components = {
            "block_production": 100 if self._bc.height > 0 else 50,
            "mempool_health":   max(0, 100 - self._bc.mempool.size() // 100),
            "utxo_diversity":   min(100, self._bc.utxo.size() // 10),
            "supply_health":    min(100, int(self._bc.utxo.total_supply() / MAX_SUPPLY * 10000)),
        }
        total  = sum(components.values()) / len(components)
        grade  = "A+" if total >= 95 else "A" if total >= 90 else "B" if total >= 80 else "C"
        return {
            "overall_score": f"{total:.1f}/100",
            "grade":         grade,
            "components":    components,
        }


# ---- NEBULAStatusPage
class NEBULAStatusPage:
    """Public status page for NEBULA services."""

    SERVICES = [
        "Mainnet RPC",
        "Block Explorer",
        "DEX Frontend",
        "Staking Dashboard",
        "NFT Marketplace",
        "Bridge Interface",
        "Governance Portal",
        "API Gateway",
    ]

    def __init__(self, bc: 'NEBULABlockchain'):
        self._bc = bc

    def status(self) -> dict:
        return {
            "services":    {s: "operational" for s in self.SERVICES},
            "chain_height": self._bc.height,
            "uptime":       "99.9%",
            "last_updated": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        }


# ---- NEBULAWhitepaper
class NEBULAWhitepaper:
    """Abstract of the NEBULA whitepaper."""

    ABSTRACT = (
        "NEBULA is a next-generation Layer-1 blockchain built entirely in Python "
        "by a solo developer. "
        "It combines Bitcoin-style UTXO accounting with a complete DeFi "
        "ecosystem including an AMM DEX, lending protocol, staking engine, "
        "NFT marketplace, cross-chain bridge, and ZK rollup scaling solution. "
        "The native token NBL (NEBULA) has a hard cap of 21 billion units "
        "(with 9 decimal places), distributed via SHA-256 Proof-of-Work mining "
        "with 4-year halving cycles. NEBULA's governance is managed via "
        "vote-escrowed NBL (veNBL), enabling decentralized protocol upgrades. "
        "This project demonstrates that world-class blockchain infrastructure "
        "can be built from anywhere in the world with nothing but determination "
        "and dedication."
    )

    @classmethod
    def get_abstract(cls) -> str:
        return cls.ABSTRACT

    @classmethod
    def citations(cls) -> List[str]:
        return [
            "Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System",
            "Buterin, V. (2014). Ethereum: A Next-Generation Smart Contract Platform",
            "Curve Finance (2020). StableSwap Invariant",
            "Uniswap (2021). Concentrated Liquidity",
            "Curve Finance (2020). Vote-Escrow Governance",
        ]


# ---- NEBULACommunityStats
class NEBULACommunityStats:
    """Tracks community growth metrics."""

    def __init__(self):
        self._members:  Dict[str, dict] = {}
        self._channels: Dict[str, int]  = {
            "github":   0,
            "twitter":  0,
            "telegram": 0,
            "discord":  0,
        }

    def join(self, address: str, channel: str = "web"):
        self._members[address] = {
            "joined": time.time(),
            "channel": channel,
            "active": True,
        }
        if channel in self._channels:
            self._channels[channel] += 1

    def community_stats(self) -> dict:
        return {
            "total_members":  len(self._members),
            "by_channel":     self._channels,
            "growth_target":  "10,000 members",
        }
