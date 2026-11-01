"""NEBULA group34 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. DataListing  (orig. lines 57456-57490)
   2. DataMarket  (orig. lines 57492-57624)
   3. ReputationScore  (orig. lines 57634-57663)
   4. ReputationEngine  (orig. lines 57665-57754)
   5. APIv2Router  (orig. lines 57764-57924)
   6. MerkleProver  (orig. lines 57937-57965)
   7. TreasuryGrant  (orig. lines 57975-57994)
   8. NEBULATreasury  (orig. lines 57996-58090)
   9. ClusterNode  (orig. lines 58100-58142)
  10. NodeCluster  (orig. lines 58144-58240)
  11. ShardBlock  (orig. lines 58257-58274)
  12. CrossShardMessage  (orig. lines 58276-58285)
  13. ShardManager  (orig. lines 58287-58374)
  14. StateChannel  (orig. lines 58384-58470)
  15. Market  (orig. lines 58480-58521)
  16. Position  (orig. lines 58523-58530)
  17. PredictionMarket  (orig. lines 58532-58663)
  18. VRF  (orig. lines 58673-58707)
  19. OnChainRNG  (orig. lines 58710-58768)
  20. OnChainLottery  (orig. lines 58771-58839)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): ChannelState, MerkleTree, NEBULABlockchain, Secp256k1, StakingEngine, StateChannelRound
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
DECIMALS            = 9

FOUNDATION_RATE        = 0.02          # 2% per block to foundation

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

def sha256d(data: bytes) -> bytes:
    """Double SHA-256 — used everywhere in Bitcoin/NEBULA"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

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

SHARD_COUNT      = 8      # number of parallel shards

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- DataListing
@dataclass
class DataListing:
    listing_id:   str
    seller:       str
    title:        str
    description:  str
    category:     str
    data_hash:    str    # SHA256 of actual data
    ipfs_cid:     str    # content address (IPFS)
    price_nbl:    float
    size_bytes:   int
    schema:       dict   # data format description
    created_at:   float
    purchases:    int = 0
    rating_sum:   float = 0.0
    rating_count: int   = 0

    @property
    def avg_rating(self) -> float:
        return self.rating_sum / self.rating_count if self.rating_count > 0 else 0

    def to_dict(self) -> dict:
        return {
            "listing_id":  self.listing_id,
            "seller":      self.seller,
            "title":       self.title,
            "description": self.description,
            "category":    self.category,
            "data_hash":   self.data_hash,
            "ipfs_cid":    self.ipfs_cid,
            "price_nbl":   self.price_nbl,
            "size_bytes":  self.size_bytes,
            "purchases":   self.purchases,
            "avg_rating":  f"{self.avg_rating:.1f}/5.0",
        }


# ---- DataMarket
class DataMarket:
    """
    Decentralized data marketplace on NEBULA.
    Sellers list datasets; buyers pay NBL to access.
    """

    MARKET_FEE_PCT = 0.025   # 2.5% platform fee

    CATEGORIES = [
        "financial", "weather", "satellite", "social",
        "medical", "traffic", "energy", "agricultural",
        "sports", "scientific", "other"
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._listings: Dict[str, DataListing] = {}
        self._purchases: Dict[str, Set[str]]   = {}  # listing_id -> {buyers}
        self._access:    Dict[str, Dict[str, str]] = {}  # buyer -> lid -> decryption_key
        self._lock      = threading.RLock()
        self._revenue:  int = 0

    def list_data(self, seller: str, title: str, description: str,
                   category: str, data_hash: str, ipfs_cid: str,
                   price_nbl: float, size_bytes: int,
                   schema: dict = None) -> str:
        with self._lock:
            # G34 FIX: validate inputs (a negative price produced a negative platform fee).
            if not seller:
                raise ValueError("seller is required")
            if (isinstance(price_nbl, bool) or not isinstance(price_nbl, (int, float))
                    or not math.isfinite(price_nbl) or price_nbl < 0):
                raise ValueError("price_nbl must be a finite number >= 0")
            if size_bytes < 0:
                raise ValueError("size_bytes must be >= 0")
            if category not in self.CATEGORIES:
                raise ValueError(f"Invalid category. Choose from {self.CATEGORIES}")
            lid = hashlib.sha256(
                f"DATA:{seller}:{data_hash}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._listings[lid] = DataListing(
                listing_id  = lid,
                seller      = seller,
                title       = title,
                description = description,
                category    = category,
                data_hash   = data_hash,
                ipfs_cid    = ipfs_cid,
                price_nbl   = price_nbl,
                size_bytes  = size_bytes,
                schema      = schema or {},
                created_at  = time.time(),
            )
            self._purchases[lid] = set()
            return lid

    def purchase(self, buyer: str, listing_id: str,
                  decryption_key: str = "") -> Tuple[bool, str]:
        with self._lock:
            listing = self._listings.get(listing_id)
            if not listing:
                return False, "Listing not found"
            if buyer in self._purchases.get(listing_id, set()):
                return False, "Already purchased"

            price  = int(listing.price_nbl * 10**DECIMALS)
            fee    = int(price * self.MARKET_FEE_PCT)
            seller_gets = price - fee

            self._purchases[listing_id].add(buyer)
            listing.purchases += 1
            self._revenue     += fee

            if buyer not in self._access:
                self._access[buyer] = {}
            self._access[buyer][listing_id] = decryption_key or listing.ipfs_cid

            return True, (f"Access granted. IPFS: {listing.ipfs_cid} | "
                          f"Seller gets {seller_gets/10**DECIMALS:.3f} NBL")

    def has_access(self, buyer: str, listing_id: str) -> bool:
        return buyer in self._purchases.get(listing_id, set())

    def rate(self, buyer: str, listing_id: str,
              rating: float, review: str = "") -> Tuple[bool, str]:
        with self._lock:
            if not self.has_access(buyer, listing_id):
                return False, "Must purchase before rating"
            listing = self._listings.get(listing_id)
            if not listing:
                return False, "Not found"
            if not (1.0 <= rating <= 5.0):
                return False, "Rating must be 1-5"
            listing.rating_sum   += rating
            listing.rating_count += 1
            return True, f"Rated {rating}/5"

    def search(self, query: str = "", category: str = "",
                max_price: float = 0, min_rating: float = 0) -> List[dict]:
        results = list(self._listings.values())
        if query:
            q = query.lower()
            results = [l for l in results
                       if q in l.title.lower() or q in l.description.lower()]
        if category:
            results = [l for l in results if l.category == category]
        if max_price > 0:
            results = [l for l in results if l.price_nbl <= max_price]
        if min_rating > 0:
            results = [l for l in results if l.avg_rating >= min_rating]
        results.sort(key=lambda l: l.purchases, reverse=True)
        return [l.to_dict() for l in results]

    def seller_stats(self, seller: str) -> dict:
        listings = [l for l in self._listings.values() if l.seller == seller]
        total_earned = sum(
            int(l.price_nbl * 10**DECIMALS) * l.purchases * (1 - self.MARKET_FEE_PCT)
            for l in listings
        )
        return {
            "total_listings": len(listings),
            "total_sales":    sum(l.purchases for l in listings),
            "total_earned_nbl": f"{total_earned/10**DECIMALS:.3f}",
            "avg_rating":     f"{sum(l.avg_rating for l in listings)/len(listings):.1f}" if listings else "0",
        }

    def market_stats(self) -> dict:
        with self._lock:
            total_listings = len(self._listings)
            total_purchases = sum(len(b) for b in self._purchases.values())
            total_volume = sum(
                int(l.price_nbl * 10**DECIMALS) * l.purchases
                for l in self._listings.values()
            )
        return {
            "total_listings":   total_listings,
            "total_purchases":  total_purchases,
            "total_volume_nbl": f"{total_volume/10**DECIMALS:.3f}",
            "platform_revenue": f"{self._revenue/10**DECIMALS:.3f} NBL",
            "categories":       self.CATEGORIES,
        }


# ---- ReputationScore
@dataclass
class ReputationScore:
    address:        str
    score:          float    # 0.0 - 1000.0
    transactions:   int
    total_volume:   int
    age_blocks:     int
    stake_weight:   float
    social_weight:  float
    penalty_count:  int = 0
    last_updated:   float = field(default_factory=time.time)

    @property
    def tier(self) -> str:
        if self.score >= 900:   return "DIAMOND"
        elif self.score >= 700: return "PLATINUM"
        elif self.score >= 500: return "GOLD"
        elif self.score >= 300: return "SILVER"
        elif self.score >= 100: return "BRONZE"
        else:                   return "NEWCOMER"

    def to_dict(self) -> dict:
        return {
            "address":      self.address,
            "score":        f"{self.score:.1f}",
            "tier":         self.tier,
            "transactions": self.transactions,
            "age_blocks":   self.age_blocks,
            "penalty_count": self.penalty_count,
        }


# ---- ReputationEngine
class ReputationEngine:
    """
    On-chain reputation scoring for NEBULA addresses.
    Score based on: tx history, stake, age, social, penalties.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 staking:   StakingEngine   = None,
                 social:    'NEBULASocial'  = None):
        self._bc      = blockchain
        self._staking = staking
        self._social  = social
        self._scores: Dict[str, ReputationScore] = {}
        self._penalties: Dict[str, List[dict]]   = {}
        self._lock    = threading.RLock()
        # G34: optional callable(address) -> (tx_count:int, first_seen_height:Optional[int]).
        # The wiring layer sets it so the age/tx components (hard-coded to 0 originally) are live.
        self.activity_provider = None

    SCORE_CACHE_MAX = 10_000

    def _activity(self, address: str):
        prov = self.activity_provider
        if prov is None:
            return 0, None
        try:
            tx_count, first = prov(address)
            return int(tx_count), (None if first is None else int(first))
        except Exception:
            return 0, None

    def _stake_points(self, address: str) -> float:
        if not self._staking:
            return 0.0
        try:
            stk    = self._staking.get_stake(address)
            staked = float(str(stk.get("total_staked", "0 NBL")).split()[0])
            return max(0.0, min(200.0, staked / 100))
        except Exception:
            return 0.0

    def _social_points(self, address: str) -> float:
        if not self._social:
            return 0.0
        try:
            profile = self._social.profile(address)
            if profile:
                return max(0.0, min(100.0, profile.get("followers", 0) * 2))
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in ReputationEngine._social_points", exc_info=True)
        return 0.0

    def _components(self, address: str) -> dict:
        tx_count, first = self._activity(address)
        age     = max(0, self._bc.height - first) if first is not None else 0
        balance = self._bc.utxo.balance(address)
        penalties = self._penalties.get(address, [])
        return {
            "age_blocks": age,
            "tx_count":   tx_count,
            "balance":    balance,
            "age_pt":     min(200, age / 10),               # max 200 pts
            "tx_pt":      min(200, tx_count * 2),           # max 200 pts
            "vol_pt":     min(200, balance / 10**DECIMALS), # max 200 pts
            "stake_pt":   self._stake_points(address),      # max 200 pts
            "social_pt":  self._social_points(address),     # max 100 pts
            "penalty":    min(500, len(penalties) * 50),
            "penalty_count": len(penalties),
        }

    def compute_score(self, address: str) -> float:
        """Compute reputation score (0-1000) for an address."""
        c = self._components(address)
        total = (c["age_pt"] + c["tx_pt"] + c["vol_pt"] + c["stake_pt"]
                 + c["social_pt"] - c["penalty"])
        return max(0.0, min(1000.0, total))

    def get_score(self, address: str) -> ReputationScore:
        with self._lock:
            c     = self._components(address)
            score = max(0.0, min(1000.0, c["age_pt"] + c["tx_pt"] + c["vol_pt"]
                                 + c["stake_pt"] + c["social_pt"] - c["penalty"]))
            rs    = ReputationScore(
                address       = address,
                score         = score,
                transactions  = c["tx_count"],
                total_volume  = c["balance"],
                age_blocks    = c["age_blocks"],
                stake_weight  = c["stake_pt"],
                social_weight = c["social_pt"],
                penalty_count = c["penalty_count"],
            )
            self._scores[address] = rs
            # G34 FIX: bound the cache (it is reachable from the public API).
            while len(self._scores) > self.SCORE_CACHE_MAX:
                self._scores.pop(next(iter(self._scores)))
            return rs

    def add_penalty(self, address: str, reason: str,
                     severity: float = 1.0):
        with self._lock:
            if address not in self._penalties:
                self._penalties[address] = []
            self._penalties[address].append({
                "reason":   reason,
                "severity": severity,
                "ts":       time.time(),
            })

    def trust_level(self, address: str) -> str:
        return self.get_score(address).tier

    def leaderboard(self, n: int = 20) -> List[dict]:
        n = max(1, min(int(n), 100))
        # G34 FIX: islice instead of list(all addresses) on every call (O(n) on big chains).
        import itertools
        addrs = list(itertools.islice(self._bc.utxo._addr_idx.keys(), 100))
        scores = [(a, self.compute_score(a)) for a in addrs]
        scores.sort(key=lambda x: -x[1])
        return [{"rank": i+1, "address": a, "score": f"{s:.1f}",
                 "tier": ReputationScore(a,s,0,0,0,0,0).tier}
                for i, (a, s) in enumerate(scores[:n])]


# ---- APIv2Router
class APIv2Router:
    """
    Extended API router for NEBULA v2 endpoints.
    Mounts on top of existing REST API.
    """

    PREFIX = "/api/v2"

    def __init__(self, full_node: 'NEBULAFullNode' = None):
        self._node = full_node
        self._routes: Dict[str, Callable] = {}
        self._register_routes()

    def _register_routes(self):
        """Register all v2 API routes."""
        r = self._routes

        # Governance
        r["/governance/proposals"]       = self._list_proposals
        r["/governance/stats"]           = self._governance_stats

        # Staking
        r["/staking/stats"]              = self._staking_stats
        r["/staking/validators"]         = self._top_validators

        # DEX
        r["/dex/stats"]                  = self._dex_stats
        r["/dex/pools"]                  = self._list_pools

        # NFT
        r["/nft/stats"]                  = self._nft_stats
        r["/nft/marketplace"]            = self._nft_listings

        # Identity
        r["/did/stats"]                  = self._did_stats

        # Analytics
        r["/analytics/rich-list"]        = self._rich_list
        r["/analytics/summary"]          = self._analytics_summary

        # Social
        r["/social/stats"]               = self._social_stats
        r["/social/trending"]            = self._trending

        # Bridge
        r["/bridge/stats"]               = self._bridge_stats

        # Ecosystem
        r["/ecosystem"]                  = self._ecosystem_info

    def handle(self, path: str,
                params: dict = None) -> dict:
        """Route a request to the appropriate handler."""
        # Strip prefix
        # G34 FIX: the original sliced blindly; any path was accepted and a trailing slash broke matching.
        if not isinstance(path, str) or not path.startswith(self.PREFIX):
            return {"ok": False, "error": f"Route not found: {path}"}
        rel = path[len(self.PREFIX):].rstrip("/") or "/"
        handler = self._routes.get(rel)
        if handler:
            try:
                return {"ok": True, "data": handler(params or {})}
            except Exception as e:
                return {"ok": False, "error": str(e)}
        return {"ok": False, "error": f"Route not found: {path}"}

    def _list_proposals(self, p: dict) -> list:
        if self._node:
            return self._node.governance.list_proposals(p.get("status"))
        return []

    def _governance_stats(self, p: dict) -> dict:
        if self._node:
            return self._node.governance.governance_stats()
        return {}

    def _staking_stats(self, p: dict) -> dict:
        if self._node:
            return self._node.staking.staking_stats()
        return {}

    def _top_validators(self, p: dict) -> list:
        if self._node:
            return self._node.staking.top_validators(int(p.get("n", 10)))
        return []

    def _dex_stats(self, p: dict) -> dict:
        if self._node:
            return self._node.dex.dex_stats()
        return {}

    def _list_pools(self, p: dict) -> list:
        if self._node:
            return self._node.dex.list_pools()
        return []

    def _nft_stats(self, p: dict) -> dict:
        if self._node:
            return self._node.nft.nft_stats()
        return {}

    def _nft_listings(self, p: dict) -> list:
        if self._node:
            return self._node.nft.marketplace_listings()
        return []

    def _did_stats(self, p: dict) -> dict:
        if self._node:
            return self._node.did_registry.did_stats()
        return {}

    def _rich_list(self, p: dict) -> list:
        if self._node:
            return self._node.analytics.rich_list(int(p.get("n", 20)))
        return []

    def _analytics_summary(self, p: dict) -> dict:
        if self._node:
            return self._node.analytics.summary()
        return {}

    def _social_stats(self, p: dict) -> dict:
        return {}

    def _trending(self, p: dict) -> list:
        return []

    def _bridge_stats(self, p: dict) -> dict:
        if self._node:
            return self._node.bridge.bridge_stats()
        return {}

    def _ecosystem_info(self, p: dict) -> dict:
        return nebula_ecosystem_info()

    def register(self, rel_path: str, handler: Callable) -> None:
        """G34: add an endpoint under /api/v2 (rel_path starts with '/'; handler(params: dict) -> data)."""
        if not rel_path.startswith("/") or not callable(handler):
            raise ValueError("rel_path must start with '/' and handler must be callable")
        self._routes[rel_path] = handler

    def list_routes(self) -> List[str]:
        return [f"{self.PREFIX}{r}" for r in self._routes.keys()]

    def openapi_spec(self) -> dict:
        """Generate OpenAPI 3.0 specification."""
        paths = {}
        for route in self._routes:
            full = f"{self.PREFIX}{route}"
            paths[full] = {
                "get": {
                    "summary":     f"NEBULA {route.strip('/').replace('/', ' ').title()}",
                    "operationId": route.strip('/').replace('/', '_'),
                    "responses": {
                        "200": {"description": "Success",
                                "content": {"application/json": {}}},
                        "500": {"description": "Error"},
                    }
                }
            }
        return {
            "openapi":  "3.0.0",
            "info": {
                "title":   "NEBULA Blockchain API v2",
                "version": "2.0.0",
                "description": "Complete DeFi + NFT + Governance REST API",
            },
            "servers": [{"url": "http://localhost:8080"}],
            "paths":   paths,
        }


# ---- MerkleProver
class MerkleProver:
    """
    Merkle inclusion proofs for transaction verification.
    Light clients can verify tx without full block data.
    """

    @staticmethod
    def prove_inclusion(txid: str, block: 'Block') -> Optional[dict]:
        """Generate Merkle proof that txid is in block."""
        if block is None:
            return None
        txids = [tx.txid for tx in block.transactions]
        if txid not in txids:
            return None
        proof = MerkleTree.build_proof(txids, txid)
        return {
            "txid":       txid,
            "block_hash": block.hash,
            "height":     block.height,
            "merkle_root": block.header.merkle_root,
            "proof":      proof,
        }

    @staticmethod
    def verify_inclusion(proof_dict: dict) -> bool:
        """Verify a Merkle inclusion proof."""
        try:
            return bool(MerkleTree.verify_proof(
                proof_dict["merkle_root"],
                proof_dict["txid"],
                proof_dict["proof"]
            ))
        except Exception:      # G34 FIX: malformed proof -> False instead of an exception
            return False


# ---- TreasuryGrant
@dataclass
class TreasuryGrant:
    grant_id:    str
    recipient:   str
    amount:      int
    purpose:     str
    milestone:   str
    approved_by: str    # governance proposal id
    paid:        bool = False
    paid_at:     float = 0.0

    def to_dict(self) -> dict:
        return {
            "grant_id":  self.grant_id,
            "recipient": self.recipient,
            "amount_nbl": f"{self.amount/10**DECIMALS:.3f}",
            "purpose":   self.purpose,
            "milestone": self.milestone,
            "paid":      self.paid,
        }


# ---- NEBULATreasury
class NEBULATreasury:
    """
    NEBULA Protocol Treasury.
    Receives 2% of every block reward.
    Distributes via governance-approved grants.
    """

    CATEGORIES = [
        "core_development", "security_audit", "community",
        "marketing", "research", "infrastructure", "grants",
        "bug_bounty", "liquidity", "other"
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._grants: Dict[str, TreasuryGrant] = {}
        self._budget_allocations: Dict[str, float] = {
            "core_development": 0.40,
            "security_audit":   0.15,
            "community":        0.15,
            "marketing":        0.10,
            "research":         0.10,
            "infrastructure":   0.05,
            "grants":           0.05,
        }
        self._lock    = threading.RLock()
        self._spent:  int = 0

    def balance(self) -> int:
        return self._bc.utxo.balance(FOUNDATION_ADDRESS)

    def total_received(self) -> int:
        """Sum of foundation shares of all rewards up to the tip.
        G34 FIX: closed form over the (max 64) halving eras instead of one loop iteration per block;
        the result is identical because the reward is constant inside an era."""
        height = self._bc.height
        if height < 0:
            return 0
        total = 0
        for era in range(64):
            first = era * HALVING_INTERVAL
            if first > height:
                break
            last   = min(height, first + HALVING_INTERVAL - 1)
            blocks = last - first + 1
            total += blocks * int(mining_reward(first) * FOUNDATION_RATE)
        return total

    def committed(self) -> int:
        """Total of grants that were created but not yet paid."""
        return sum(g.amount for g in self._grants.values() if not g.paid)

    def available(self) -> int:
        """Balance that is neither already paid out nor promised to an open grant."""
        return self.balance() - self._spent - self.committed()

    def create_grant(self, recipient: str, amount_nbl: float,
                      purpose: str, milestone: str,
                      governance_proposal_id: str = "") -> str:
        with self._lock:
            if not recipient:
                raise ValueError("recipient is required")
            amount = int(amount_nbl * 10**DECIMALS)
            if amount <= 0:
                raise ValueError("amount must be positive")
            # G34 FIX: grants could previously over-commit the same balance any number of times.
            if amount > self.available():
                raise ValueError("Insufficient treasury balance")
            gid = hashlib.sha256(
                f"GRANT:{recipient}:{amount}:{time.time()}:{len(self._grants)}".encode()
            ).hexdigest()[:16]
            self._grants[gid] = TreasuryGrant(
                grant_id    = gid,
                recipient   = recipient,
                amount      = amount,
                purpose     = purpose,
                milestone   = milestone,
                approved_by = governance_proposal_id,
            )
            return gid

    def pay_grant(self, grant_id: str) -> Tuple[bool, str]:
        """Mark a grant as paid. NOTE: this is a LEDGER entry only - it does not broadcast a
        transaction. Moving real funds needs the foundation key and a governance decision."""
        with self._lock:
            grant = self._grants.get(grant_id)
            if not grant:
                return False, "Grant not found"
            if grant.paid:
                return False, "Already paid"
            if grant.amount > self.balance() - self._spent:
                return False, "Insufficient treasury balance"
            grant.paid    = True
            grant.paid_at = time.time()
            self._spent  += grant.amount
            return True, (f"Paid {grant.amount/10**DECIMALS:.3f} NBL "
                          f"to {grant.recipient}")

    def budget_report(self) -> dict:
        balance   = self.balance()
        received  = self.total_received()
        allocations = {
            cat: {
                "pct":    f"{pct*100:.0f}%",
                "amount": f"{balance*pct/10**DECIMALS:.3f} NBL",
            }
            for cat, pct in self._budget_allocations.items()
        }
        return {
            "balance_nbl":   f"{balance/10**DECIMALS:.3f}",
            "total_received": f"{received/10**DECIMALS:.3f}",
            "total_spent":   f"{self._spent/10**DECIMALS:.3f}",
            "grants":        len(self._grants),
            "paid_grants":   sum(1 for g in self._grants.values() if g.paid),
            "allocations":   allocations,
        }

    def grant_history(self) -> List[dict]:
        return [g.to_dict() for g in self._grants.values()]


# ---- ClusterNode
# G34 FIX: the original had two stray @dataclass decorators here. The class has no class-level
# fields, so @dataclass generated an __eq__ comparing empty tuples (every ClusterNode equal to
# every other) and set __hash__ = None (unhashable). Decorators removed.
class ClusterNode:
    """A single node in a test cluster."""

    def __init__(self, node_id: str, blockchain=None):
        self.node_id    = node_id
        # G34 FIX: allow an injected (e.g. in-memory) chain so a test cluster can never open the
        # production data directory by accident. Default behaviour is unchanged.
        self.blockchain = blockchain if blockchain is not None else NEBULABlockchain()
        self.peers:     Set[str] = set()
        self.messages:  List[dict] = []
        self.latency_ms: float = 10.0   # simulated network latency

    def connect_to(self, other_id: str):
        self.peers.add(other_id)

    def send(self, other: 'ClusterNode', msg: dict):
        """Simulate sending a message to another node."""
        msg["from"]  = self.node_id
        msg["delay"] = self.latency_ms
        other.messages.append(msg)

    def receive_all(self, cluster: 'NodeCluster'):
        """Process all pending messages."""
        for msg in self.messages:
            self._handle(msg, cluster)
        self.messages.clear()

    def _handle(self, msg: dict, cluster: 'NodeCluster'):
        pass   # Override for specific handling


# ---- NodeCluster
class NodeCluster:
    """
    Simulated multi-node NEBULA network cluster.
    Used for testing network propagation, fork resolution, etc.
    """

    def __init__(self, n_nodes: int = 5, blockchain_factory: Optional[Callable] = None):
        if n_nodes < 1:
            raise ValueError("n_nodes must be >= 1")
        self.nodes: Dict[str, ClusterNode] = {}
        self._factory = blockchain_factory
        self._create_nodes(n_nodes)
        self._connect_mesh()

    def _create_nodes(self, n: int):
        for i in range(n):
            nid = f"node_{i}"
            chain = self._factory() if self._factory else None
            self.nodes[nid] = ClusterNode(nid, chain)

    def _connect_mesh(self):
        """Connect all nodes to each other (full mesh)."""
        ids = list(self.nodes.keys())
        for i, nid in enumerate(ids):
            for other in ids[i+1:]:
                self.nodes[nid].connect_to(other)
                self.nodes[other].connect_to(nid)

    def broadcast(self, sender_id: str, msg: dict):
        """Broadcast a message from one node to all peers."""
        sender = self.nodes.get(sender_id)
        if not sender:
            return
        for peer_id in sender.peers:
            peer = self.nodes.get(peer_id)
            if peer:
                sender.send(peer, dict(msg))

    def propagation_test(self, msg: dict) -> dict:
        """Test how fast a message propagates through the cluster."""
        origin   = list(self.nodes.keys())[0]
        received = {origin: 0.0}
        queue    = [(origin, 0.0)]

        while queue:
            current_id, delay = queue.pop(0)
            current = self.nodes[current_id]
            for peer_id in current.peers:
                if peer_id not in received:
                    peer = self.nodes[peer_id]
                    propagation_delay = delay + peer.latency_ms
                    received[peer_id] = propagation_delay
                    queue.append((peer_id, propagation_delay))

        max_delay = max(received.values()) if received else 0
        return {
            "nodes_reached":  len(received),
            "total_nodes":    len(self.nodes),
            "max_delay_ms":   max_delay,
            "avg_delay_ms":   sum(received.values()) / len(received) if received else 0,
            "coverage_pct":   f"{len(received)/len(self.nodes)*100:.0f}%",
        }

    def simulate_fork(self) -> dict:
        """Simulate a chain fork and observe resolution."""
        ids      = list(self.nodes.keys())
        group_a  = ids[:len(ids)//2]
        group_b  = ids[len(ids)//2:]

        # Mine one block on each group
        blocks_a = []
        blocks_b = []

        for nid in group_a:
            node = self.nodes[nid]
            h    = node.blockchain.height + 1
            blocks_a.append(f"block_A_{h}")

        for nid in group_b:
            node = self.nodes[nid]
            h    = node.blockchain.height + 1
            blocks_b.append(f"block_B_{h}")

        return {
            "fork_detected":   True,
            "group_a":         group_a,
            "group_b":         group_b,
            "blocks_a":        blocks_a,
            "blocks_b":        blocks_b,
            "resolution":      "Longest chain wins (most cumulative PoW)",
        }

    def cluster_health(self) -> dict:
        heights = [n.blockchain.height for n in self.nodes.values()]
        return {
            "node_count":    len(self.nodes),
            "min_height":    min(heights) if heights else 0,
            "max_height":    max(heights) if heights else 0,
            "in_sync":       len(set(heights)) == 1,
            "topology":      "full_mesh",
        }


# ---- ShardBlock
@dataclass
class ShardBlock:
    shard_id:    int
    height:      int
    prev_hash:   str
    txs:         List[str]   # tx hashes
    state_root:  str
    timestamp:   float
    proposer:    str

    def to_dict(self) -> dict:
        return {
            "shard_id":   self.shard_id,
            "height":     self.height,
            "tx_count":   len(self.txs),
            "state_root": self.state_root,
            "proposer":   self.proposer,
        }


# ---- CrossShardMessage
@dataclass
class CrossShardMessage:
    msg_id:      str
    from_shard:  int
    to_shard:    int
    sender:      str
    recipient:   str
    amount:      int
    nonce:       int
    status:      str = "pending"  # pending/included/finalized


# ---- ShardManager
class ShardManager:
    """
    NEBULA sharding coordinator.
    Routes transactions to appropriate shards based on address prefix.
    Handles cross-shard transfers via receipt-based protocol.
    """

    def __init__(self, n_shards: int = SHARD_COUNT):
        self.n_shards      = n_shards
        self._shards:      Dict[int, List[ShardBlock]] = {i: [] for i in range(n_shards)}
        self._cross_msgs:  List[CrossShardMessage]     = []
        self._pending:     Dict[int, List[str]]        = {i: [] for i in range(n_shards)}
        self._lock         = threading.RLock()
        self._seq          = 0      # G34: monotonic cross-shard nonce (len() of a trimmed list repeats)

    def address_to_shard(self, address: str) -> int:
        """Deterministically assign address to shard."""
        h = int(hashlib.sha256(address.encode()).hexdigest()[:4], 16)
        return h % self.n_shards

    def route_tx(self, txid: str, sender: str, recipient: str) -> Tuple[int, bool]:
        """
        Route a transaction to the appropriate shard.
        Returns (shard_id, is_cross_shard).
        """
        src_shard = self.address_to_shard(sender)
        dst_shard = self.address_to_shard(recipient)
        if src_shard == dst_shard:
            with self._lock:
                self._pending[src_shard].append(txid)
            return src_shard, False
        else:
            return src_shard, True   # cross-shard

    def initiate_cross_shard(self, sender: str, recipient: str,
                              amount: int) -> str:
        """Start a cross-shard transfer."""
        with self._lock:
            from_shard = self.address_to_shard(sender)
            to_shard   = self.address_to_shard(recipient)
            # G34 FIX: the id now includes a monotonic nonce, so two identical transfers created
            # within the clock resolution can no longer collide on the same msg_id.
            nonce = self._seq
            self._seq += 1
            mid = hashlib.sha256(
                f"XSHARD:{sender}:{recipient}:{amount}:{nonce}:{time.time()}".encode()
            ).hexdigest()[:16]
            msg = CrossShardMessage(
                msg_id     = mid,
                from_shard = from_shard,
                to_shard   = to_shard,
                sender     = sender,
                recipient  = recipient,
                amount     = amount,
                nonce      = nonce,
            )
            self._cross_msgs.append(msg)
            return mid

    def finalize_cross_shard(self, msg_id: str) -> Tuple[bool, str]:
        """Finalize a cross-shard transfer on destination shard."""
        with self._lock:
            msg = next((m for m in self._cross_msgs if m.msg_id == msg_id), None)
            if not msg:
                return False, "Message not found"
            if msg.status != "pending":
                return False, f"Wrong status: {msg.status}"
            msg.status = "finalized"
            return True, f"Cross-shard transfer finalized on shard {msg.to_shard}"

    # ---- G34 additions: bookkeeping hooks used by the chain-listener layer ----
    def add_shard_block(self, block: ShardBlock, keep: int = 5000) -> None:
        """Append a shard block and keep only the newest `keep` blocks of that shard."""
        with self._lock:
            chain = self._shards.get(block.shard_id)
            if chain is None:
                raise ValueError(f"unknown shard {block.shard_id}")
            chain.append(block)
            if len(chain) > keep:
                del chain[:len(chain) - keep]

    def shard_tip(self, shard_id: int) -> Optional[ShardBlock]:
        with self._lock:
            chain = self._shards.get(shard_id)
            return chain[-1] if chain else None

    def rollback_above(self, height: int) -> int:
        """Drop shard blocks above `height` (chain reorg). Returns how many were removed."""
        removed = 0
        with self._lock:
            for chain in self._shards.values():
                while chain and chain[-1].height > height:
                    chain.pop()
                    removed += 1
        return removed

    def discard_pending(self, txid: str, shard_id: int) -> None:
        """Remove a confirmed tx from the shard's pending queue."""
        with self._lock:
            q = self._pending.get(shard_id)
            if q and txid in q:
                q.remove(txid)

    def drop_cross_messages(self, msg_ids) -> int:
        """Remove cross-shard messages (their source block was reorganised away)."""
        ids = set(msg_ids)
        with self._lock:
            before = len(self._cross_msgs)
            self._cross_msgs = [m for m in self._cross_msgs if m.msg_id not in ids]
            return before - len(self._cross_msgs)

    def trim_finalized(self, keep: int = 10000) -> int:
        """Keep at most `keep` finalized cross-shard messages (pending ones are never trimmed)."""
        with self._lock:
            fin = [m for m in self._cross_msgs if m.status == "finalized"]
            extra = len(fin) - keep
            if extra <= 0:
                return 0
            drop = {m.msg_id for m in fin[:extra]}
            self._cross_msgs = [m for m in self._cross_msgs if m.msg_id not in drop]
            return extra

    def shard_stats(self) -> dict:
        with self._lock:
            # G34: height = tip height of the shard chain (len() saturates once old blocks are trimmed)
            shard_heights = {i: (s[-1].height if s else 0) for i, s in self._shards.items()}
            pending       = {i: len(p) for i, p in self._pending.items()}
            cross_pending = sum(1 for m in self._cross_msgs if m.status == "pending")
        return {
            "n_shards":          self.n_shards,
            "shard_heights":     shard_heights,
            "pending_per_shard": pending,
            "cross_shard_msgs":  len(self._cross_msgs),
            "cross_pending":     cross_pending,
        }

    def throughput_estimate(self) -> dict:
        """Estimate theoretical throughput with sharding."""
        base_tps   = 7       # Bitcoin-like base TPS
        shard_tps  = base_tps * self.n_shards
        return {
            "base_tps":       base_tps,
            "shard_tps":      shard_tps,
            "n_shards":       self.n_shards,
            "note":           "Cross-shard txs have 2-block latency",
        }


# ---- StateChannel
# G34 FIX: removed @dataclass (custom __init__, no fields -> all channels compared equal, unhashable)
class StateChannel:
    """
    Generalized state channel between 2+ participants.
    Any off-chain logic can run in the channel.
    On-chain settlement only when channel closes.
    """

    def __init__(self, channel_id: str, participants: List[str],
                  deposits: Dict[str, int]):
        if len(participants) < 2 or len(set(participants)) != len(participants):
            raise ValueError("A channel needs at least 2 distinct participants")
        if set(deposits) - set(participants) or any(v < 0 for v in deposits.values()):
            raise ValueError("Deposits must be non-negative and belong to participants")
        self.channel_id   = channel_id
        self.participants = participants
        self.deposits     = deposits
        self._states:     List[ChannelState] = []
        self._lock        = threading.RLock()

        # Initial state
        initial = StateChannelRound(
            channel_id = channel_id,
            round_num  = 0,
            state_data = {"status": "open"},
            balances   = dict(deposits),
        )
        self._states.append(initial)

    @property
    def current_state(self) -> ChannelState:
        return self._states[-1]

    def propose_state(self, proposer: str,
                       new_state_data: dict,
                       new_balances: Dict[str, int],
                       privkey: int) -> ChannelState:
        """Propose a new channel state (binding only once every participant countersigned)."""
        with self._lock:
            cur = self.current_state
            if getattr(cur, "final", False):
                raise ValueError("Channel is closed")
            if proposer not in self.participants:
                raise ValueError("Proposer is not a channel participant")
            # G34 FIX: a state may never create or destroy value inside the channel.
            if (set(new_balances) - set(self.participants)
                    or any(v < 0 for v in new_balances.values())
                    or sum(new_balances.values()) != sum(self.deposits.values())):
                raise ValueError("Balances must be non-negative, belong to participants "
                                 "and conserve the total deposit")
            state = StateChannelRound(
                channel_id = self.channel_id,
                round_num  = cur.round_num + 1,
                state_data = new_state_data,
                balances   = new_balances,
            )
            h     = state.hash().encode()
            r, s  = Secp256k1.sign(privkey, sha256d(h))
            state.sigs[proposer] = Secp256k1.sig_to_der(r, s)
            return state

    def countersign(self, state: ChannelState,
                     signer: str, privkey: int) -> bool:
        """Countersign a proposed state; returns True once all participants signed and it is accepted."""
        with self._lock:
            cur = self.current_state
            # G34 FIX: reject closed channels, outsiders, foreign/stale/replayed rounds.
            if getattr(cur, "final", False):
                return False
            if signer not in self.participants:
                return False
            if getattr(state, "channel_id", None) != self.channel_id:
                return False
            if state.round_num != cur.round_num + 1:
                return False
            h    = state.hash().encode()
            r, s = Secp256k1.sign(privkey, sha256d(h))
            state.sigs[signer] = Secp256k1.sig_to_der(r, s)
            if set(state.sigs.keys()) >= set(self.participants):
                self._states.append(state)
                return True
            return False

    def close(self, privkey: int,
               closer: str) -> ChannelState:
        """Close the channel with the current state (idempotent once closed)."""
        with self._lock:
            cur = self.current_state
            if getattr(cur, "final", False):
                return cur
            if closer not in self.participants:
                raise ValueError("Closer is not a channel participant")
            final = StateChannelRound(
                channel_id = self.channel_id,
                round_num  = cur.round_num + 1,
                state_data = {"status": "closed"},
                balances   = dict(cur.balances),
                final      = True,
            )
            h    = final.hash().encode()
            r, s = Secp256k1.sign(privkey, sha256d(h))
            final.sigs[closer] = Secp256k1.sig_to_der(r, s)
            self._states.append(final)
            return final

    def channel_info(self) -> dict:
        cs = self.current_state
        return {
            "channel_id":   self.channel_id,
            "participants": self.participants,
            "round":        cs.round_num,
            "state":        cs.state_data,
            "balances":     cs.balances,
            "is_closed":    cs.final,
            "total_rounds": len(self._states),
        }


# ---- Market
@dataclass
class Market:
    market_id:   str
    creator:     str
    question:    str
    category:    str
    end_block:   int
    resolution:  Optional[bool] = None   # True=YES, False=NO, None=open
    yes_pool:    int = 0
    no_pool:     int = 0
    fee_pct:     float = 0.02   # 2%
    resolved_at: float = 0.0
    oracle:      str = ""

    @property
    def total_pool(self) -> int:
        return self.yes_pool + self.no_pool

    @property
    def yes_price(self) -> float:
        """Price of YES share (0.0-1.0)."""
        if self.total_pool == 0:
            return 0.5
        return self.yes_pool / self.total_pool

    @property
    def no_price(self) -> float:
        return 1.0 - self.yes_price

    def to_dict(self) -> dict:
        return {
            "market_id":  self.market_id,
            "question":   self.question,
            "category":   self.category,
            "yes_price":  f"{self.yes_price:.4f}",
            "no_price":   f"{self.no_price:.4f}",
            "yes_pool_nbl": f"{self.yes_pool/10**DECIMALS:.3f}",
            "no_pool_nbl":  f"{self.no_pool/10**DECIMALS:.3f}",
            "total_pool": f"{self.total_pool/10**DECIMALS:.3f}",
            "resolution": self.resolution,
            "end_block":  self.end_block,
        }


# ---- Position
@dataclass
class Position:
    trader:    str
    market_id: str
    outcome:   str   # "yes" or "no"
    amount:    int   # NBL staked
    shares:    float
    entry_price: float


# ---- PredictionMarket
class PredictionMarket:
    """
    NEBULA decentralized prediction market.
    AMM-based: price determined by pool ratio.

    NOTE (G34): this is an in-memory LEDGER. buy()/claim() do not move UTXOs; settlement on chain
    is a separate, consensus-relevant step that this class does not perform.
    """

    MIN_PRICE = 0.01     # G34: price clamp - a 0.0 price used to mint zero shares for real money
    MAX_PRICE = 0.99

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._markets: Dict[str, Market]   = {}
        self._positions: Dict[str, List[Position]] = {}  # market_id -> positions
        self._lock     = threading.RLock()
        self._claimed: Set[Tuple[str, str]] = set()      # G34: (trader, market_id) already paid
        self._fees: int = 0                              # G34: fees were silently dropped before

    def create_market(self, creator: str, question: str,
                       category: str, duration_days: int = 7,
                       oracle: str = "") -> str:
        with self._lock:
            if not creator or not question:
                raise ValueError("creator and question are required")
            if duration_days < 1:
                raise ValueError("duration_days must be >= 1")
            end_block = self._bc.height + duration_days * 144
            mid = hashlib.sha256(
                f"PM:{creator}:{question}:{time.time()}:{len(self._markets)}".encode()
            ).hexdigest()[:16]
            self._markets[mid] = Market(
                market_id = mid,
                creator   = creator,
                question  = question,
                category  = category,
                end_block = end_block,
                oracle    = oracle,
            )
            self._positions[mid] = []
            return mid

    def buy(self, trader: str, market_id: str,
             outcome: str, amount: int) -> Tuple[bool, str]:
        """Buy YES or NO shares."""
        with self._lock:
            mkt = self._markets.get(market_id)
            if not mkt:
                return False, "Market not found"
            if mkt.resolution is not None:
                return False, "Market resolved"
            if self._bc.height > mkt.end_block:
                return False, "Market closed"
            if outcome not in ("yes", "no"):
                return False, "outcome must be 'yes' or 'no'"
            # G34 FIX: a negative amount used to shrink the pool and create negative shares.
            if isinstance(amount, bool) or not isinstance(amount, int) or amount <= 0:
                return False, "amount must be a positive integer (in Neb)"
            if not trader:
                return False, "trader is required"

            fee    = int(amount * mkt.fee_pct)
            net    = amount - fee
            raw    = mkt.yes_price if outcome == "yes" else mkt.no_price
            price  = min(self.MAX_PRICE, max(self.MIN_PRICE, raw))
            shares = net / (price * 10**DECIMALS)

            if outcome == "yes":
                mkt.yes_pool += net
            else:
                mkt.no_pool  += net
            self._fees += fee

            pos = Position(
                trader      = trader,
                market_id   = market_id,
                outcome     = outcome,
                amount      = amount,
                shares      = shares,
                entry_price = price,
            )
            self._positions[market_id].append(pos)
            return True, (f"Bought {shares:.4f} {outcome.upper()} shares "
                          f"at {price:.4f} for {amount/10**DECIMALS:.4f} NBL")

    def resolve(self, market_id: str, oracle: str,
                 outcome: bool) -> Tuple[bool, str]:
        """Resolve market outcome (True=YES wins, False=NO wins)."""
        with self._lock:
            mkt = self._markets.get(market_id)
            if not mkt:
                return False, "Not found"
            if mkt.resolution is not None:
                return False, "Already resolved"
            # G34 FIX: the old check was skipped when oracle == "" so anyone could resolve.
            # The designated oracle (or, if none was set, the market creator) must be the caller.
            allowed = mkt.oracle or mkt.creator
            if oracle != allowed:
                return False, "Not the designated oracle"
            if not isinstance(outcome, bool):
                return False, "outcome must be True (YES) or False (NO)"
            mkt.resolution  = outcome
            mkt.resolved_at = time.time()
            winner          = "YES" if outcome else "NO"
            return True, f"Market resolved: {winner} wins"

    def claim(self, trader: str, market_id: str) -> Tuple[bool, int]:
        """Claim winnings after market resolution (once per trader per market)."""
        with self._lock:
            mkt = self._markets.get(market_id)
            if not mkt or mkt.resolution is None:
                return False, 0
            # G34 FIX: claim() could be called repeatedly and returned the full payout each time.
            if (trader, market_id) in self._claimed:
                return False, 0

            winning_outcome = "yes" if mkt.resolution else "no"
            total_pool      = mkt.total_pool

            positions = [p for p in self._positions.get(market_id, [])
                         if p.trader == trader and p.outcome == winning_outcome]
            if not positions:
                return False, 0

            trader_shares  = sum(p.shares for p in positions)
            total_shares   = sum(p.shares for p in self._positions[market_id]
                                 if p.outcome == winning_outcome)
            if total_shares == 0:
                return False, 0

            payout = int(total_pool * trader_shares / total_shares)
            self._claimed.add((trader, market_id))
            return True, payout

    def market_info(self, market_id: str) -> Optional[dict]:
        m = self._markets.get(market_id)
        return m.to_dict() if m else None

    def list_markets(self, open_only: bool = True) -> List[dict]:
        with self._lock:
            mkts = list(self._markets.values())
        if open_only:
            cur  = self._bc.height
            mkts = [m for m in mkts
                    if m.resolution is None and cur <= m.end_block]
        return [m.to_dict() for m in mkts]

    def market_stats(self) -> dict:
        with self._lock:
            total    = len(self._markets)
            resolved = sum(1 for m in self._markets.values() if m.resolution is not None)
            total_vol = sum(m.total_pool for m in self._markets.values())
            fees      = self._fees
        return {
            "total_markets":   total,
            "open_markets":    total - resolved,
            "resolved":        resolved,
            "total_volume_nbl": f"{total_vol/10**DECIMALS:.3f}",
            "fees_collected_nbl": f"{fees/10**DECIMALS:.3f}",
        }


# ---- VRF
class VRF:
    """
    Simplified VRF (Verifiable Random Function) using ECDSA.
    In production use: ECVRF-SECP256K1-SHA256-TAI (RFC 9381).
    """

    @staticmethod
    def prove(privkey: int, message: bytes) -> Tuple[bytes, bytes]:
        """
        Generate VRF proof and output.
        Returns (vrf_output, proof).
        """
        r, s     = Secp256k1.sign(privkey, sha256d(message))
        proof    = Secp256k1.sig_to_der(r, s)
        vrf_out  = hashlib.sha256(proof + message).digest()
        return vrf_out, proof

    @staticmethod
    def verify(pubkey_bytes: bytes, message: bytes,
               vrf_output: bytes, proof: bytes) -> bool:
        """Verify a VRF proof."""
        try:
            r, s    = Secp256k1.sig_from_der(proof)
            expected = hashlib.sha256(proof + message).digest()
            if expected != vrf_output:
                return False
            return Secp256k1.verify_bytes(pubkey_bytes, sha256d(message), r, s)
        except Exception:
            return False

    @staticmethod
    def output_to_int(vrf_output: bytes, max_val: int) -> int:
        """Convert VRF output to integer in [0, max_val)."""
        n = int.from_bytes(vrf_output, 'big')
        return n % max_val


# ---- OnChainRNG
class OnChainRNG:
    """
    On-chain random number generator using VRF + block data.
    Combines validator VRF proofs with block hashes for randomness.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._entropy: Dict[int, List[bytes]] = {}   # height -> [vrf_outputs]
        self._lock    = threading.RLock()

    def drop_entropy_above(self, height: int) -> int:
        """G34: forget contributions made for blocks above `height` (reorg). Returns count removed."""
        with self._lock:
            stale = [h for h in self._entropy if h > height]
            for h in stale:
                del self._entropy[h]
            return len(stale)

    def contribute_entropy(self, height: int,
                            vrf_output: bytes):
        """Validator contributes VRF entropy for a block."""
        with self._lock:
            if height not in self._entropy:
                self._entropy[height] = []
            self._entropy[height].append(vrf_output)

    def get_randomness(self, height: int,
                        nonce: int = 0) -> bytes:
        """
        Get verifiable randomness for a block height.
        Combines all validator contributions + block hash.
        """
        # G34 FIX: for a height that does not exist yet the old code silently used the constant
        # b"genesis", which makes the "random" value predictable. Refuse instead.
        if height > self._bc.height:
            raise ValueError(f"block {height} is not mined yet (tip {self._bc.height})")
        blk = self._bc.get_block(height)
        block_hash = blk.hash.encode() if blk else b"genesis"

        contributions = self._entropy.get(height, [])
        combined = block_hash + b"".join(contributions) + nonce.to_bytes(8, 'big')
        return hashlib.sha256(combined).digest()

    def random_int(self, height: int, max_val: int,
                    nonce: int = 0) -> int:
        """Get a random integer in [0, max_val) for given block."""
        rand = self.get_randomness(height, nonce)
        return int.from_bytes(rand, 'big') % max_val

    def random_sample(self, height: int,
                       population: List[Any],
                       k: int) -> List[Any]:
        """Randomly sample k items from population using on-chain randomness."""
        rand    = self.get_randomness(height)
        indices = []
        pop     = list(population)
        for i in range(min(k, len(pop))):
            r   = int.from_bytes(hashlib.sha256(rand + i.to_bytes(4,'big')).digest(), 'big')
            idx = r % len(pop)
            indices.append(pop.pop(idx))
        return indices

    def lottery_draw(self, tickets: List[str],
                      n_winners: int,
                      block_height: int) -> List[str]:
        """Draw lottery winners using verifiable on-chain randomness."""
        if not tickets or n_winners <= 0:
            return []
        winners = self.random_sample(block_height, tickets, n_winners)
        return winners


# ---- OnChainLottery
class OnChainLottery:
    """
    Decentralized lottery using VRF randomness.

    G34 NOTES:
    - Randomness is taken from the block DRAW_CONFIRMATIONS blocks AFTER draw_block, so the miner of
      draw_block can no longer pick the winner by withholding/choosing a block.
    - A draw is remembered together with the hash of the seed block; if a reorg replaces that block,
      reset_if_reorged() undoes the draw so it is recomputed from the new chain.
    - Tickets are an in-memory LEDGER (TICKET_PRICE is not collected on chain by this class).
    """

    TICKET_PRICE        = 10 * 10**DECIMALS   # 10 NBL per ticket
    DRAW_CONFIRMATIONS  = 6

    def __init__(self, blockchain: 'NEBULABlockchain',
                 rng: OnChainRNG):
        self._bc      = blockchain
        self._rng     = rng
        self._rounds: Dict[int, dict] = {}   # round_id -> info
        self._lock    = threading.RLock()

    def seed_block(self, round_id: int) -> Optional[int]:
        r = self._rounds.get(round_id)
        return None if r is None else r["draw_block"] + self.DRAW_CONFIRMATIONS

    def start_round(self, draw_block: int) -> int:
        with self._lock:
            if draw_block <= self._bc.height:
                raise ValueError("draw_block must be in the future")
            rid = max(self._rounds.keys(), default=0) + 1
            self._rounds[rid] = {
                "round_id":   rid,
                "draw_block": draw_block,
                "tickets":    [],
                "prize_pool": 0,
                "winners":    [],
                "drawn":      False,
                "seed_hash":  "",
            }
            return rid

    def buy_ticket(self, buyer: str,
                    round_id: int) -> Tuple[bool, str]:
        with self._lock:
            r = self._rounds.get(round_id)
            if not r:
                return False, "Round not found"
            if not buyer:
                return False, "buyer is required"
            if r["drawn"]:
                return False, "Round already drawn"
            if self._bc.height >= r["draw_block"]:
                return False, "Round closed for new tickets"
            r["tickets"].append(buyer)
            r["prize_pool"] += self.TICKET_PRICE
            ticket_num = len(r["tickets"])
            return True, f"Ticket #{ticket_num} purchased"

    def due_rounds(self) -> List[int]:
        """Round ids that are not drawn yet and whose seed block exists."""
        with self._lock:
            tip = self._bc.height
            return [rid for rid, r in sorted(self._rounds.items())
                    if not r["drawn"] and tip >= r["draw_block"] + self.DRAW_CONFIRMATIONS]

    def draw(self, round_id: int,
              n_winners: int = 3) -> Tuple[bool, List[str]]:
        with self._lock:
            r = self._rounds.get(round_id)
            if not r:
                return False, []
            if r["drawn"]:
                return False, r["winners"]
            seed = r["draw_block"] + self.DRAW_CONFIRMATIONS
            if self._bc.height < seed:
                return False, []
            if n_winners < 1:
                return False, []

            winners = self._rng.lottery_draw(r["tickets"], n_winners, seed)
            blk     = self._bc.get_block(seed)
            r["seed_hash"] = blk.hash if blk else ""
            r["winners"] = winners
            r["drawn"]   = True
            return True, winners

    def reset_if_reorged(self) -> List[int]:
        """Undo draws whose seed block is gone or changed. Returns the reset round ids."""
        reset: List[int] = []
        with self._lock:
            tip = self._bc.height
            for rid, r in self._rounds.items():
                if not r["drawn"]:
                    continue
                seed = r["draw_block"] + self.DRAW_CONFIRMATIONS
                blk  = self._bc.get_block(seed) if seed <= tip else None
                if blk is None or (r["seed_hash"] and blk.hash != r["seed_hash"]):
                    r["drawn"]     = False
                    r["winners"]   = []
                    r["seed_hash"] = ""
                    reset.append(rid)
        return reset

    def round_info(self, round_id: int) -> Optional[dict]:
        r = self._rounds.get(round_id)
        if not r:
            return None
        return {
            **r,
            "ticket_count": len(r["tickets"]),
            "prize_pool_nbl": f"{r['prize_pool']/10**DECIMALS:.3f}",
            "seed_block": r["draw_block"] + self.DRAW_CONFIRMATIONS,
        }
