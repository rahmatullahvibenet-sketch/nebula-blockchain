"""NEBULA group46 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. CollateralManager  (orig. lines 74121-74169)
   2. NFTMetadataStandard  (orig. lines 74176-74244)
   3. CrossChainOracle  (orig. lines 74251-74312)
   4. StakingPoolV3  (orig. lines 74319-74366)
   5. DeFiScorecard  (orig. lines 74373-74424)
   6. NFTDropManager  (orig. lines 74431-74504)
   7. ProtocolComposer  (orig. lines 74511-74591)
   8. NEBULAAIAssistant  (orig. lines 74598-74680)
   9. ZKRollupBatch  (orig. lines 74692-74726)
  10. ZKRollupLayer  (orig. lines 74728-74790)
  11. DeFiAlertV2  (orig. lines 74797-74870)
  12. OnChainKVStore  (orig. lines 74877-74934)
  13. ProtocolConfig  (orig. lines 74941-75003)
  14. WalletSecurityManager  (orig. lines 75010-75071)
  15. EcosystemMetricsTracker  (orig. lines 75078-75133)
  16. TransactionAnalytics  (orig. lines 75140-75193)
  17. YieldAggregator  (orig. lines 75200-75266)
  18. TreasuryV3  (orig. lines 75273-75360)
  19. OnChainCoinFlip  (orig. lines 75367-75399)
  20. OnChainDice  (orig. lines 75401-75436)

Helpers/constants copied from the host (module-level) are in the section below the imports.
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

INITIAL_BITS           = 0x1e0fffff if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d0fffff   # [v10.24]

MAX_BLOCK_SIZE_BYTES   = 1_048_576                      # 1 MB

MAX_TX_PER_BLOCK       = 3000

COINBASE_MATURITY      = 100                            # blocks before coinbase spendable

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

DUST_THRESHOLD         = 546                            # min output amount in Neb

DEFAULT_PORT           = 8333

PROTOCOL_VERSION       = 70015

MAX_PEERS              = 125

MAGIC_BYTES            = 0x4E424C4D   # "NBLM" — NEBULA Mainnet magic integer

SEED_NODES = [
    # Asia Pacific
    ("seed1.nebula-nbl.io",  DEFAULT_PORT),
    ("seed2.nebula-nbl.io",  DEFAULT_PORT),
    ("seed3.nebula-nbl.io",  DEFAULT_PORT),
    # Europe
    ("seed4.nebula-nbl.io",  DEFAULT_PORT),
    ("seed5.nebula-nbl.io",  DEFAULT_PORT),
    # Americas
    ("seed6.nebula-nbl.io",  DEFAULT_PORT),
    ("seed7.nebula-nbl.io",  DEFAULT_PORT),
    # Africa & Middle East
    ("seed8.nebula-nbl.io",  DEFAULT_PORT),
    # Oceania
    ("seed9.nebula-nbl.io",  DEFAULT_PORT),
    ("seed10.nebula-nbl.io", DEFAULT_PORT),
]

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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- CollateralManager
class CollateralManager:
    """
    Manages collateral across multiple DeFi protocols.
    Shows unified collateral health dashboard.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc     = blockchain
        self._oracle = oracle
        self._positions: Dict[str, List[dict]] = {}   # addr -> [positions]
        self._lock   = threading.RLock()

    def add_collateral_position(self, address: str, protocol: str,
                                 collateral_asset: str, collateral_amount: int,
                                 debt_asset: str, debt_amount: int):
        with self._lock:
            if address not in self._positions:
                self._positions[address] = []
            self._positions[address].append({
                "protocol":          protocol,
                "collateral_asset":  collateral_asset,
                "collateral_amount": collateral_amount,
                "debt_asset":        debt_asset,
                "debt_amount":       debt_amount,
                "added_at":          time.time(),
            })

    def health_summary(self, address: str) -> dict:
        positions = self._positions.get(address, [])
        total_col  = 0.0
        total_debt = 0.0
        price      = (self._oracle.price("NBL/USD")
                      if self._oracle else 0.01) or 0.01
        for p in positions:
            col_usd  = p["collateral_amount"] / 10**DECIMALS * price
            debt_usd = p["debt_amount"] / 10**DECIMALS
            total_col  += col_usd
            total_debt += debt_usd
        hf = total_col * 0.8 / total_debt if total_debt > 0 else float('inf')
        return {
            "address":         address,
            "total_col_usd":   f"${total_col:.2f}",
            "total_debt_usd":  f"${total_debt:.2f}",
            "health_factor":   f"{hf:.4f}",
            "status":          ("SAFE" if hf > 1.5 else
                                "WARNING" if hf > 1.2 else "DANGER"),
            "positions":       len(positions),
        }


# ---- NFTMetadataStandard
class NFTMetadataStandard:
    """
    NEBULA NFT metadata standard (NIP-81 compliant).
    Validates and normalizes NFT metadata.
    """

    REQUIRED_FIELDS = ["name", "description", "image"]
    OPTIONAL_FIELDS = ["external_url", "animation_url",
                       "youtube_url", "background_color", "attributes"]

    ATTRIBUTE_TYPES = {"string", "number", "boost_number",
                       "boost_percentage", "date", "ranking"}

    @classmethod
    def validate(cls, metadata: dict) -> Tuple[bool, List[str]]:
        errors = []
        for field in cls.REQUIRED_FIELDS:
            if field not in metadata:
                errors.append(f"Missing required field: {field}")
        name = metadata.get("name", "")
        if len(name) > 100:
            errors.append("Name too long (max 100 chars)")
        desc = metadata.get("description", "")
        if len(desc) > 1000:
            errors.append("Description too long (max 1000 chars)")
        attrs = metadata.get("attributes", [])
        if isinstance(attrs, list):
            for i, attr in enumerate(attrs):
                if "trait_type" not in attr:
                    errors.append(f"Attribute {i} missing trait_type")
                if "value" not in attr:
                    errors.append(f"Attribute {i} missing value")
        return len(errors) == 0, errors

    @classmethod
    def normalize(cls, metadata: dict) -> dict:
        normalized = {}
        for field in cls.REQUIRED_FIELDS + cls.OPTIONAL_FIELDS:
            if field in metadata:
                normalized[field] = metadata[field]
        # Ensure attributes is a list
        if "attributes" not in normalized:
            normalized["attributes"] = []
        return normalized

    @classmethod
    def from_opensea_format(cls, os_meta: dict) -> dict:
        """Convert OpenSea metadata format to NIP-81."""
        return {
            "name":        os_meta.get("name", ""),
            "description": os_meta.get("description", ""),
            "image":       os_meta.get("image", ""),
            "attributes":  os_meta.get("attributes", []),
            "external_url": os_meta.get("external_url", ""),
        }

    @classmethod
    def generate_sample(cls, name: str, token_id: int) -> dict:
        return {
            "name":        f"{name} #{token_id}",
            "description": f"NEBULA NFT: {name} #{token_id}",
            "image":       f"ipfs://placeholder/{token_id}.png",
            "attributes":  [
                {"trait_type": "Token ID",  "value": token_id},
                {"trait_type": "Blockchain", "value": "NEBULA"},
                {"trait_type": "Standard",  "value": "NIP-81"},
            ],
            "external_url": f"https://nebula-nbl.io/nft/{token_id}",
        }


# ---- CrossChainOracle
class CrossChainOracle:
    """
    Aggregates price data from multiple blockchains.
    Provides unified price feeds for cross-chain DeFi.
    """

    CHAIN_SOURCES = {
        "ethereum":  ["chainlink", "uniswap_twap"],
        "solana":    ["pyth", "switchboard"],
        "cosmos":    ["band_protocol"],
        "nebula":    ["nebula_oracle"],
    }

    def __init__(self):
        self._prices:    Dict[str, Dict[str, float]] = {}  # chain -> {pair: price}
        self._consensus: Dict[str, float]            = {}   # pair -> consensus price
        self._lock       = threading.RLock()

    def ingest_chain_price(self, chain: str, pair: str,
                            price: float, source: str = ""):
        with self._lock:
            if chain not in self._prices:
                self._prices[chain] = {}
            self._prices[chain][pair] = price
            self._update_consensus(pair)

    def _update_consensus(self, pair: str):
        prices = []
        for chain_data in self._prices.values():
            if pair in chain_data:
                prices.append(chain_data[pair])
        if not prices:
            return
        prices.sort()
        self._consensus[pair] = prices[len(prices)//2]

    def consensus_price(self, pair: str) -> Optional[float]:
        return self._consensus.get(pair)

    def price_divergence(self, pair: str) -> dict:
        prices = {
            chain: data.get(pair)
            for chain, data in self._prices.items()
            if pair in data
        }
        if len(prices) < 2:
            return {"pair": pair, "divergence": "N/A"}
        vals = list(prices.values())
        max_div = (max(vals) - min(vals)) / min(vals) * 100 if min(vals) > 0 else 0
        return {
            "pair":        pair,
            "by_chain":    {k: f"${v:.6f}" for k, v in prices.items()},
            "consensus":   f"${self.consensus_price(pair):.6f}",
            "max_divergence": f"{max_div:.3f}%",
        }

    def oracle_health(self) -> dict:
        return {
            "chains_tracked": len(self._prices),
            "pairs_tracked":  len(self._consensus),
            "sources":        self.CHAIN_SOURCES,
        }


# ---- StakingPoolV3
class StakingPoolV3:
    """
    Staking pool v3 with dynamic APY based on TVL.
    Higher TVL = lower APY (prevents over-staking).
    """

    TARGET_STAKING_RATIO = 0.67    # target 67% of supply staked
    BASE_APY             = 0.10    # 10% base APY

    def __init__(self, pool_id: str,
                  blockchain: 'NEBULABlockchain'):
        self.pool_id      = pool_id
        self._bc          = blockchain
        self.total_staked = 0
        self._stakers:    Dict[str, dict] = {}

    @property
    def current_apy(self) -> float:
        supply        = self._bc.utxo.total_supply()
        staking_ratio = self.total_staked / supply if supply > 0 else 0
        # Adjust APY based on staking ratio
        if staking_ratio < self.TARGET_STAKING_RATIO:
            multiplier = 1 + (self.TARGET_STAKING_RATIO - staking_ratio) * 2
        else:
            multiplier = max(0.5, 1 - (staking_ratio - self.TARGET_STAKING_RATIO) * 2)
        return self.BASE_APY * multiplier

    def stake(self, address: str, amount: int) -> bool:
        self._stakers[address] = {
            "amount":    self._stakers.get(address, {}).get("amount", 0) + amount,
            "staked_at": self._bc.height,
        }
        self.total_staked += amount
        return True

    def unstake(self, address: str) -> int:
        info = self._stakers.pop(address, {})
        amount = info.get("amount", 0)
        self.total_staked -= amount
        return amount

    def pool_info_v3(self) -> dict:
        return {
            "pool_id":     self.pool_id,
            "total_staked": f"{self.total_staked/10**DECIMALS:.3f}",
            "dynamic_apy": f"{self.current_apy*100:.2f}%",
            "stakers":     len(self._stakers),
        }


# ---- DeFiScorecard
class DeFiScorecard:
    """
    DeFi protocol scorecard — rates protocols on key metrics.
    Used by users to evaluate risk/reward of each protocol.
    """

    METRICS = [
        "security", "decentralization", "liquidity",
        "yield", "transparency", "user_experience",
    ]

    SCORES = {
        "NEBULA Staking":     [9, 9, 8, 7, 10, 9],
        "NEBULA DEX":         [8, 8, 7, 8, 9, 8],
        "NEBULA Lending":     [8, 7, 7, 7, 9, 8],
        "NEBULA NFT Market":  [8, 9, 6, 5, 9, 9],
        "NEBULA Governance":  [9, 10, 8, 6, 10, 8],
        "NEBULA Bridge":      [7, 7, 7, 6, 8, 7],
        "NEBULA Insurance":   [8, 8, 6, 7, 9, 7],
    }

    @classmethod
    def get_scores(cls, protocol: str = None) -> dict:
        if protocol:
            scores = cls.SCORES.get(protocol)
            if not scores:
                return {}
            return {
                "protocol":    protocol,
                "total":       sum(scores),
                "average":     f"{sum(scores)/len(scores):.1f}/10",
                "breakdown":   dict(zip(cls.METRICS, scores)),
            }
        return {
            p: {
                "total":   sum(s),
                "avg":     f"{sum(s)/len(s):.1f}",
                "scores":  dict(zip(cls.METRICS, s)),
            }
            for p, s in cls.SCORES.items()
        }

    @classmethod
    def best_protocols(cls, metric: str,
                        n: int = 3) -> List[Tuple[str, int]]:
        if metric not in cls.METRICS:
            return []
        idx = cls.METRICS.index(metric)
        return sorted(
            [(p, s[idx]) for p, s in cls.SCORES.items()],
            key=lambda x: -x[1]
        )[:n]


# ---- NFTDropManager
class NFTDropManager:
    """
    Tools for launching NFT collection drops on NEBULA.
    Handles allowlists, Dutch auctions, reveals.
    """

    def __init__(self, nft: 'NBL721Registry',
                  blockchain: 'NEBULABlockchain'):
        self._nft   = nft
        self._bc    = blockchain
        self._drops: Dict[str, dict] = {}
        self._lock  = threading.RLock()

    def create_drop(self, collection_id: str,
                     drop_type: str,
                     price: float,
                     max_per_wallet: int,
                     start_block: int,
                     allowlist: List[str] = None) -> str:
        with self._lock:
            did = hashlib.sha256(
                f"DROP:{collection_id}:{start_block}".encode()
            ).hexdigest()[:12]
            self._drops[did] = {
                "drop_id":       did,
                "collection_id": collection_id,
                "drop_type":     drop_type,
                "price":         int(price * 10**DECIMALS),
                "max_per_wallet": max_per_wallet,
                "start_block":   start_block,
                "allowlist":     set(allowlist or []),
                "minted_count":  0,
                "wallet_counts": {},
            }
            return did

    def mint_from_drop(self, drop_id: str, minter: str,
                        quantity: int = 1) -> Tuple[bool, List[int]]:
        with self._lock:
            drop = self._drops.get(drop_id)
            if not drop:
                return False, []
            if self._bc.height < drop["start_block"]:
                return False, []
            if drop["allowlist"] and minter not in drop["allowlist"]:
                return False, []
            wallet_count = drop["wallet_counts"].get(minter, 0)
            if wallet_count + quantity > drop["max_per_wallet"]:
                quantity = drop["max_per_wallet"] - wallet_count
            if quantity <= 0:
                return False, []
            token_ids = []
            for _ in range(quantity):
                tid, msg = self._nft.mint(
                    drop["collection_id"], minter,
                    f"ipfs://drop/{drop['drop_id']}/{drop['minted_count']}",
                    NFTMetadataStandard.generate_sample(
                        drop["collection_id"], drop["minted_count"]+1),
                    caller=minter
                )
                token_ids.append(tid)
                drop["minted_count"] += 1
            drop["wallet_counts"][minter] = wallet_count + quantity
            return True, token_ids

    def drop_stats(self, drop_id: str) -> Optional[dict]:
        drop = self._drops.get(drop_id)
        if not drop:
            return None
        return {
            **{k: v for k, v in drop.items() if k != "allowlist"},
            "allowlist_size":   len(drop["allowlist"]),
            "unique_minters":   len(drop["wallet_counts"]),
        }


# ---- ProtocolComposer
class ProtocolComposer:
    """
    Composes multiple NEBULA protocols in single transactions.
    e.g. swap → stake → farm in one operation.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  dex: 'NEBULADex' = None,
                  staking: 'StakingEngine' = None,
                  farming: 'YieldFarmingV2' = None):
        self._bc      = blockchain
        self._dex     = dex
        self._staking = staking
        self._farming = farming
        self._ops_log: List[dict] = []

    def swap_and_stake(self, user: str, token_in: str,
                        amount_in: float) -> Tuple[bool, str]:
        """Swap a token to NBL and immediately stake it."""
        steps = []
        # Step 1: Swap
        if self._dex and token_in != "NBL":
            ok, msg, out = self._dex.swap_amm(
                user, token_in, "NBL",
                int(amount_in * 10**DECIMALS))
            if not ok:
                return False, f"Swap failed: {msg}"
            steps.append(f"Swapped {amount_in} {token_in} → {out/10**DECIMALS:.6f} NBL")
            nbl_amount = out / 10**DECIMALS
        else:
            nbl_amount = amount_in
        # Step 2: Stake
        if self._staking:
            ok2, msg2 = self._staking.stake(user, int(nbl_amount * 10**DECIMALS))
            steps.append(f"Staked {nbl_amount:.6f} NBL: {msg2}")
        result = " | ".join(steps)
        self._ops_log.append({"user": user, "op": "swap_and_stake",
                               "result": result, "ts": time.time()})
        return True, result

    def add_liquidity_and_farm(self, user: str,
                                token_a: str, token_b: str,
                                amount_a: float, amount_b: float,
                                pool_id: str,
                                farm_pool_id: str) -> Tuple[bool, str]:
        """Add liquidity to DEX and farm the LP tokens."""
        steps = []
        if self._dex:
            ok, msg = self._dex.add_liquidity(
                user, token_a, token_b,
                int(amount_a * 10**DECIMALS),
                int(amount_b * 10**DECIMALS))
            steps.append(f"Added liquidity: {msg}")
        if self._farming:
            ok2, msg2 = self._farming.deposit(
                user, farm_pool_id, amount_a)
            steps.append(f"Farming: {msg2}")
        result = " | ".join(steps)
        self._ops_log.append({"user": user, "op": "lp_and_farm",
                               "result": result, "ts": time.time()})
        return True, result

    def harvest_and_compound(self, user: str,
                              pool_id: str) -> Tuple[bool, str]:
        """Harvest farming rewards and restake them."""
        if not self._farming or not self._staking:
            return False, "Required protocols not configured"
        ok, harvested = self._farming.claim_rewards(user, pool_id)
        if not ok or harvested == 0:
            return False, "No rewards to harvest"
        ok2, msg2 = self._staking.stake(user, harvested)
        result = f"Harvested {harvested/10**DECIMALS:.6f} NBL → {msg2}"
        self._ops_log.append({"user": user, "op": "harvest_compound",
                               "result": result, "ts": time.time()})
        return True, result

    def composer_stats(self) -> dict:
        return {
            "operations": len(self._ops_log),
            "op_types":   list(set(o["op"] for o in self._ops_log)),
        }


# ---- NEBULAAIAssistant
class NEBULAAIAssistant:
    """
    AI-powered assistant for NEBULA protocol queries.
    Generates responses for user queries.
    Note: Requires API key in production.
    """

    SYSTEM_PROMPT = """You are NEBULA AI — the intelligent assistant for the 
NEBULA blockchain ecosystem. You help users understand DeFi, trading, 
staking, governance, NFTs, and all NEBULA protocol features. 
Be concise, accurate, and helpful."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._history:    List[dict] = []
        self._queries:    int = 0

    def ask(self, question: str) -> str:
        """Ask the AI assistant a question about NEBULA."""
        self._queries += 1
        self._history.append({
            "role":    "user",
            "content": question,
        })
        # Response generation hook
        # For now: pattern-based responses
        q_lower = question.lower()
        if "price" in q_lower or "value" in q_lower:
            return ("NBL price can be found on the NEBULA DEX or via the oracle. "
                    "Use oracle.price('NBL/USD') to query the current price.")
        elif "stake" in q_lower or "staking" in q_lower:
            return ("NEBULA offers flexible and time-locked staking pools. "
                    "APY ranges from 5% (flexible) to 25% (1-year lock). "
                    "Use StakingEngine.stake() to begin staking.")
        elif "nft" in q_lower:
            return ("NEBULA NFTs follow the NIP-81 standard. "
                    "You can mint, trade, and stake NFTs on the platform. "
                    "Royalties are automatically enforced on-chain.")
        elif "governance" in q_lower or "vote" in q_lower:
            return ("NEBULA governance uses veNBL for weighted voting. "
                    "Lock NBL for up to 4 years to maximize voting power. "
                    "Submit proposals via GovernanceEngine.propose().")
        elif "swap" in q_lower or "dex" in q_lower:
            return ("The NEBULA DEX offers both AMM pools and an order book. "
                    "Swap any NBL-20 token with minimal slippage. "
                    "SmartOrderRouter finds the best execution path.")
        elif "security" in q_lower or "safe" in q_lower:
            return ("NEBULA uses battle-tested cryptography (secp256k1 ECDSA). "
                    "The circuit breaker system can pause protocols if anomalies detected. "
                    "Multi-sig governance controls all admin functions.")
        else:
            return (f"I understand you're asking about: {question[:100]}. "
                    "NEBULA offers a complete DeFi ecosystem including DEX, "
                    "staking, lending, NFTs, and governance. "
                    "For detailed help, check the docs at nebula-nbl.io.")

    def portfolio_advice(self, address: str,
                          risk_tolerance: str = "moderate") -> str:
        bc  = self._bc
        bal = bc.utxo.balance(address) / 10**DECIMALS
        if risk_tolerance == "conservative":
            return (f"With {bal:.3f} NBL, consider: "
                    "70% flexible staking (5% APY), "
                    "20% 30-day staking (8% APY), "
                    "10% lending supply (4% APY).")
        elif risk_tolerance == "aggressive":
            return (f"With {bal:.3f} NBL, consider: "
                    "30% 1-year staking (25% APY), "
                    "40% LP farming (65% APY), "
                    "20% options/futures, "
                    "10% cash buffer.")
        else:
            return (f"With {bal:.3f} NBL, consider: "
                    "40% 90-day staking (12% APY), "
                    "30% DEX liquidity (35% APY), "
                    "20% lending (4% APY), "
                    "10% flexible reserve.")

    def assistant_stats(self) -> dict:
        return {
            "queries":      self._queries,
            "history_len":  len(self._history),
        }


# ---- ZKRollupBatch
class ZKRollupBatch:
    """A batch of transactions rolled up with ZK proof."""

    def __init__(self, batch_id: int):
        self.batch_id    = batch_id
        self.txs:        List[dict] = []
        self.state_root  = ""
        self.zk_proof    = ""
        self.submitted   = False
        self.verified    = False

    def add_tx(self, tx: dict):
        self.txs.append(tx)

    def compute_state_root(self) -> str:
        data = json.dumps([t.get("txid", "") for t in self.txs],
                          sort_keys=True).encode()
        self.state_root = hashlib.sha256(data).hexdigest()
        return self.state_root

    def generate_proof(self) -> str:
        """Generate ZK proof (simplified simulation)."""
        self.zk_proof = hashlib.sha256(
            (self.state_root + str(len(self.txs))).encode()
        ).hexdigest()
        return self.zk_proof

    def to_dict(self) -> dict:
        return {
            "batch_id":   self.batch_id,
            "tx_count":   len(self.txs),
            "state_root": self.state_root,
            "verified":   self.verified,
            "submitted":  self.submitted,
        }


# ---- ZKRollupLayer
class ZKRollupLayer:
    """
    ZK Rollup layer for NEBULA scalability.
    Batches thousands of transactions, submits one ZK proof.
    """

    MAX_BATCH_SIZE    = 1000
    PROOF_GEN_BLOCKS  = 10

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._pending: List[dict] = []
        self._batches: Dict[int, ZKRollupBatch] = {}
        self._batch_counter = 0
        self._lock    = threading.RLock()

    def submit_l2_tx(self, tx: dict) -> bool:
        with self._lock:
            self._pending.append(tx)
            if len(self._pending) >= self.MAX_BATCH_SIZE:
                self._create_batch()
            return True

    def _create_batch(self) -> int:
        self._batch_counter += 1
        batch = ZKRollupBatch(self._batch_counter)
        for tx in self._pending:
            batch.add_tx(tx)
        self._pending.clear()
        batch.compute_state_root()
        batch.generate_proof()
        self._batches[self._batch_counter] = batch
        return self._batch_counter

    def force_batch(self) -> Optional[int]:
        with self._lock:
            if not self._pending:
                return None
            return self._create_batch()

    def verify_batch(self, batch_id: int) -> bool:
        with self._lock:
            batch = self._batches.get(batch_id)
            if not batch:
                return False
            # Simplified verification
            expected = hashlib.sha256(
                (batch.state_root + str(len(batch.txs))).encode()
            ).hexdigest()
            batch.verified = (expected == batch.zk_proof)
            return batch.verified

    def rollup_stats(self) -> dict:
        with self._lock:
            total_txs   = sum(len(b.txs) for b in self._batches.values())
            verified    = sum(1 for b in self._batches.values() if b.verified)
        return {
            "total_batches":  len(self._batches),
            "verified":       verified,
            "total_l2_txs":   total_txs,
            "pending":        len(self._pending),
            "compression":    f"{total_txs}/{len(self._batches)} (txs/batch)",
        }


# ---- DeFiAlertV2
class DeFiAlertV2:
    """Advanced DeFi alerting with webhooks and notifications."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc       = blockchain
        self._oracle   = oracle
        self._watchers: Dict[str, dict] = {}
        self._alerts:   List[dict]      = []
        self._lock      = threading.RLock()

    def watch_address(self, watcher: str, address: str,
                       min_amount: float = 100.0,
                       alert_types: List[str] = None):
        with self._lock:
            key = f"{watcher}:{address}"
            self._watchers[key] = {
                "watcher":    watcher,
                "address":    address,
                "min_amount": min_amount,
                "types":      alert_types or ["inbound", "outbound"],
                "active":     True,
            }

    def watch_price(self, watcher: str, pair: str,
                     above: float = None, below: float = None):
        with self._lock:
            key = f"{watcher}:price:{pair}"
            self._watchers[key] = {
                "watcher":  watcher,
                "pair":     pair,
                "above":    above,
                "below":    below,
                "active":   True,
                "type":     "price",
            }

    def check_all(self) -> List[dict]:
        triggered = []
        with self._lock:
            for key, watcher in self._watchers.items():
                if not watcher.get("active"):
                    continue
                if watcher.get("type") == "price" and self._oracle:
                    price = self._oracle.price(watcher["pair"])
                    if price:
                        if watcher.get("above") and price >= watcher["above"]:
                            alert = {"watcher": watcher["watcher"],
                                     "type": "price_above",
                                     "pair": watcher["pair"],
                                     "price": price}
                            triggered.append(alert)
                            self._alerts.append(alert)
                        if watcher.get("below") and price <= watcher["below"]:
                            alert = {"watcher": watcher["watcher"],
                                     "type": "price_below",
                                     "pair": watcher["pair"],
                                     "price": price}
                            triggered.append(alert)
                            self._alerts.append(alert)
        return triggered

    def alert_history(self, watcher: str = None,
                       n: int = 50) -> List[dict]:
        alerts = list(self._alerts)
        if watcher:
            alerts = [a for a in alerts if a.get("watcher") == watcher]
        return alerts[-n:]

    def alert_stats(self) -> dict:
        return {
            "watchers":    len(self._watchers),
            "total_alerts": len(self._alerts),
        }


# ---- OnChainKVStore
class OnChainKVStore:
    """
    General-purpose on-chain key-value storage.
    Smart contracts can use this for persistent storage.
    """

    MAX_KEY_LEN   = 256
    MAX_VAL_LEN   = 4096
    STORAGE_FEE   = MIN_TX_FEE   # per byte stored

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._store: Dict[str, Dict[str, Any]] = {}   # owner -> {key: val}
        self._lock   = threading.RLock()

    def set(self, owner: str, key: str, value: Any,
             namespace: str = "default") -> Tuple[bool, str]:
        with self._lock:
            full_key = f"{namespace}:{key}"
            if len(full_key) > self.MAX_KEY_LEN:
                return False, f"Key too long (max {self.MAX_KEY_LEN})"
            val_str = json.dumps(value) if not isinstance(value, str) else value
            if len(val_str) > self.MAX_VAL_LEN:
                return False, f"Value too long (max {self.MAX_VAL_LEN})"
            fee = len(val_str) * self.STORAGE_FEE // 100
            if self._bc.utxo.balance(owner) < fee:
                return False, "Insufficient balance for storage fee"
            if owner not in self._store:
                self._store[owner] = {}
            self._store[owner][full_key] = value
            return True, f"Stored at {full_key}"

    def get(self, owner: str, key: str,
             namespace: str = "default") -> Optional[Any]:
        full_key = f"{namespace}:{key}"
        return self._store.get(owner, {}).get(full_key)

    def delete(self, owner: str, key: str,
                namespace: str = "default") -> bool:
        with self._lock:
            full_key = f"{namespace}:{key}"
            if owner in self._store and full_key in self._store[owner]:
                del self._store[owner][full_key]
                return True
            return False

    def list_keys(self, owner: str,
                   namespace: str = "default") -> List[str]:
        prefix = f"{namespace}:"
        return [k[len(prefix):] for k in self._store.get(owner, {})
                if k.startswith(prefix)]

    def kv_stats(self) -> dict:
        total_keys = sum(len(v) for v in self._store.values())
        return {
            "owners":     len(self._store),
            "total_keys": total_keys,
        }


# ---- ProtocolConfig
@dataclass
class ProtocolConfig:
    """Runtime protocol configuration."""

    # Network
    chain_id:           int   = CHAIN_ID
    protocol_version:   int   = PROTOCOL_VERSION
    network_name:       str   = "NEBULA Mainnet"
    magic_bytes:        int   = MAGIC_BYTES
    default_port:       int   = DEFAULT_PORT
    seed_nodes:         List[str] = field(default_factory=lambda: SEED_NODES)

    # Block parameters
    max_block_size:     int   = MAX_BLOCK_SIZE_BYTES
    target_block_time:  int   = TARGET_BLOCK_TIME
    max_tx_per_block:   int   = MAX_TX_PER_BLOCK
    difficulty_window:  int   = DIFFICULTY_WINDOW

    # Fee parameters
    min_tx_fee:         int   = MIN_TX_FEE
    dust_threshold:     int   = DUST_THRESHOLD
    foundation_rate:    float = FOUNDATION_RATE

    # Consensus
    initial_bits:       int   = INITIAL_BITS
    coinbase_maturity:  int   = COINBASE_MATURITY
    halving_interval:   int   = HALVING_INTERVAL
    initial_reward:     int   = INITIAL_BLOCK_REWARD

    # P2P
    max_peers:          int   = MAX_PEERS
    handshake_timeout:  int   = 30
    ping_interval:      int   = 120

    def to_dict(self) -> dict:
        return {
            "network":        self.network_name,
            "chain_id":       self.chain_id,
            "version":        self.protocol_version,
            "block_time":     f"{self.target_block_time}s",
            "max_block_kb":   f"{self.max_block_size//1024}KB",
            "min_fee":        self.min_tx_fee,
            "halving_int":    self.halving_interval,
            "max_peers":      self.max_peers,
        }

    @classmethod
    def testnet(cls) -> 'ProtocolConfig':
        return cls(
            chain_id         = 9999,
            network_name     = "NEBULA Testnet",
            magic_bytes      = 0x4E424C54,
            initial_bits     = 0x1F00FFFF,
        )

    @classmethod
    def regtest(cls) -> 'ProtocolConfig':
        return cls(
            chain_id         = 9998,
            network_name     = "NEBULA Regtest",
            initial_bits     = 0x207FFFFF,
            target_block_time = 1,
        )


# ---- WalletSecurityManager
class WalletSecurityManager:
    """
    Security tools for NEBULA wallets.
    Spending limits, whitelist, multi-factor.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._limits:    Dict[str, dict] = {}
        self._whitelists: Dict[str, Set[str]] = {}
        self._blacklists: Dict[str, Set[str]] = {}
        self._2fa:       Dict[str, str]       = {}
        self._lock       = threading.RLock()

    def set_spending_limit(self, address: str,
                            daily_limit: float,
                            per_tx_limit: float):
        with self._lock:
            self._limits[address] = {
                "daily":     int(daily_limit * 10**DECIMALS),
                "per_tx":    int(per_tx_limit * 10**DECIMALS),
                "spent_today": 0,
                "reset_block": self._bc.height + 144,
            }

    def check_spend(self, address: str, amount: int) -> Tuple[bool, str]:
        with self._lock:
            limits = self._limits.get(address)
            if not limits:
                return True, "No limits set"
            if self._bc.height >= limits["reset_block"]:
                limits["spent_today"] = 0
                limits["reset_block"] = self._bc.height + 144
            if amount > limits["per_tx"]:
                return False, f"Exceeds per-tx limit: {limits['per_tx']/10**DECIMALS:.3f} NBL"
            if limits["spent_today"] + amount > limits["daily"]:
                return False, f"Exceeds daily limit"
            limits["spent_today"] += amount
            return True, "OK"

    def add_to_whitelist(self, owner: str, address: str):
        with self._lock:
            if owner not in self._whitelists:
                self._whitelists[owner] = set()
            self._whitelists[owner].add(address)

    def is_whitelisted(self, owner: str, address: str) -> bool:
        return address in self._whitelists.get(owner, set())

    def setup_2fa(self, address: str) -> str:
        """Setup 2FA for wallet (returns TOTP secret)."""
        secret = secrets.token_hex(20)
        self._2fa[address] = secret
        return secret

    def security_report(self, address: str) -> dict:
        return {
            "has_spending_limit": address in self._limits,
            "whitelist_size":     len(self._whitelists.get(address, set())),
            "blacklist_size":     len(self._blacklists.get(address, set())),
            "2fa_enabled":        address in self._2fa,
        }


# ---- EcosystemMetricsTracker
class EcosystemMetricsTracker:
    """
    Tracks comprehensive NEBULA ecosystem metrics over time.
    DAU, TVL, volume, user growth, protocol health.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._daily:     Dict[str, dict] = {}
        self._weekly:    Dict[str, dict] = {}
        self._lock       = threading.RLock()

    def record_daily(self, metrics: dict):
        key = time.strftime('%Y-%m-%d')
        with self._lock:
            self._daily[key] = {**metrics, "recorded_at": time.time()}

    def auto_snapshot(self) -> dict:
        bc = self._bc
        snap = {
            "block_height":  bc.height,
            "mempool_txs":   bc.mempool.size(),
            "utxo_count":    bc.utxo.size(),
            "total_supply":  bc.utxo.total_supply() / 10**DECIMALS,
            "foundation_bal": bc.utxo.balance(FOUNDATION_ADDRESS) / 10**DECIMALS,
        }
        self.record_daily(snap)
        return snap

    def week_over_week(self) -> dict:
        keys = sorted(self._daily.keys())
        if len(keys) < 8:
            return {"note": "Insufficient data"}
        last7  = keys[-7:]
        prev7  = keys[-14:-7]
        def avg(days, field):
            vals = [self._daily[d].get(field, 0) for d in days
                    if d in self._daily]
            return sum(vals) / len(vals) if vals else 0
        txs_now  = avg(last7, "mempool_txs")
        txs_prev = avg(prev7, "mempool_txs")
        return {
            "txs_wow_change": f"{(txs_now-txs_prev)/max(1,txs_prev)*100:+.1f}%",
            "data_points":    len(self._daily),
        }

    def growth_metrics(self) -> dict:
        keys = sorted(self._daily.keys())
        if len(keys) < 2:
            return {"note": "Insufficient data for growth metrics"}
        first = self._daily[keys[0]]
        last  = self._daily[keys[-1]]
        return {
            "days_tracked":  len(keys),
            "supply_growth": f"{last.get('total_supply',0)-first.get('total_supply',0):.3f} NBL",
        }


# ---- TransactionAnalytics
class TransactionAnalytics:
    """
    Analytics engine for NEBULA transaction patterns.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._stats: Dict[str, Any] = {}

    def analyze_block(self, block: 'Block',
                       utxo: 'UTXOSet') -> dict:
        txs  = block.transactions
        if not txs:
            return {}
        fees      = [tx.fee(utxo) for tx in txs[1:]]
        sizes     = [tx.byte_size() for tx in txs]
        outputs   = [len(tx.outputs) for tx in txs]
        inputs    = [len(tx.inputs) for tx in txs]
        total_out = sum(tx.total_output() for tx in txs)
        return {
            "height":           block.height,
            "tx_count":         len(txs),
            "total_volume_nbl": f"{total_out/10**DECIMALS:.6f}",
            "total_fees_nbl":   f"{sum(fees)/10**DECIMALS:.6f}",
            "avg_fee":          f"{sum(fees)//max(1,len(fees))/10**DECIMALS:.9f}",
            "avg_tx_size":      f"{sum(sizes)//max(1,len(sizes))} bytes",
            "avg_outputs":      f"{sum(outputs)/max(1,len(outputs)):.1f}",
            "avg_inputs":       f"{sum(inputs)/max(1,len(inputs)):.1f}",
        }

    def mempool_analytics(self) -> dict:
        mp   = self._bc.mempool
        txs  = list(mp._txs.values())
        if not txs:
            return {"empty": True}
        sizes  = [tx.byte_size() for tx in txs]
        return {
            "count":        len(txs),
            "total_kb":     f"{sum(sizes)/1024:.1f}",
            "avg_size":     f"{sum(sizes)//len(sizes)} bytes",
            "median_size":  f"{sorted(sizes)[len(sizes)//2]} bytes",
        }

    def whale_detection(self, threshold_nbl: float = 10000) -> List[dict]:
        threshold = int(threshold_nbl * 10**DECIMALS)
        txs = [
            {
                "txid": txid,
                "volume": tx.total_output(),
            }
            for txid, tx in self._bc.mempool._txs.items()
            if tx.total_output() >= threshold
        ]
        return sorted(txs, key=lambda t: -t["volume"])[:10]


# ---- YieldAggregator
class YieldAggregator:
    """
    Aggregates yield opportunities across all NEBULA protocols.
    Auto-allocates funds to maximize risk-adjusted yield.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._protocols:  List[dict] = []
        self._allocations: Dict[str, float] = {}

    def register_protocol(self, name: str, apy: float,
                            risk: float, min_amount: float = 0):
        self._protocols.append({
            "name":       name,
            "apy":        apy,
            "risk":       risk,      # 0 (safe) to 1 (risky)
            "min":        min_amount,
        })

    def initialize_defaults(self):
        defaults = [
            ("NEBULA Staking (Flex)",   0.05, 0.1,  0),
            ("NEBULA Staking (90d)",    0.12, 0.15, 1000),
            ("NEBULA Staking (365d)",   0.25, 0.20, 10000),
            ("NEBULA DEX LP",           0.35, 0.35, 500),
            ("NEBULA Lending Supply",   0.04, 0.10, 0),
            ("NEBULA Farming",          0.65, 0.55, 1000),
            ("NEBULA Insurance Pool",   0.15, 0.25, 5000),
            ("NEBULA Vault (Balanced)", 0.18, 0.20, 100),
        ]
        for name, apy, risk, min_a in defaults:
            self.register_protocol(name, apy, risk, min_a)

    def optimal_allocation(self, amount_nbl: float,
                            max_risk: float = 0.35) -> List[dict]:
        eligible = [p for p in self._protocols
                    if p["risk"] <= max_risk and p["min"] <= amount_nbl]
        if not eligible:
            return []
        eligible.sort(key=lambda p: -p["apy"])
        allocation = []
        remaining  = amount_nbl
        for p in eligible[:3]:
            share    = remaining / min(3, len(eligible))
            allocation.append({
                "protocol": p["name"],
                "amount":   f"{share:.2f} NBL",
                "apy":      f"{p['apy']*100:.1f}%",
                "risk":     f"{p['risk']*100:.0f}/100",
            })
            remaining -= share
        return allocation

    def projected_yield(self, allocation: List[dict]) -> dict:
        total_nbl   = 0.0
        total_yield = 0.0
        for item in allocation:
            amt = float(item["amount"].split()[0])
            apy = float(item["apy"].rstrip('%')) / 100
            total_nbl   += amt
            total_yield += amt * apy
        return {
            "total_invested": f"{total_nbl:.2f} NBL",
            "annual_yield":   f"{total_yield:.2f} NBL",
            "blended_apy":    f"{total_yield/max(1,total_nbl)*100:.2f}%",
        }


# ---- TreasuryV3
class TreasuryV3:
    """
    Protocol treasury v3 with automatic allocation.
    Multi-sig controlled, diversified portfolio.
    """

    ALLOCATION = {
        "development": 0.35,
        "security":    0.20,
        "community":   0.15,
        "marketing":   0.10,
        "research":    0.10,
        "reserves":    0.10,
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._balance: int = 0
        self._signers: List[str] = []
        self._required: int = 3
        self._txs:     List[dict] = []
        self._sigs:    Dict[str, Set[str]] = {}
        self._lock     = threading.RLock()

    def add_signer(self, signer: str):
        with self._lock:
            self._signers.append(signer)

    def deposit(self, amount: int):
        with self._lock:
            self._balance += amount

    def propose_spend(self, proposer: str, recipient: str,
                       amount: int, category: str,
                       description: str) -> Tuple[bool, str]:
        with self._lock:
            if proposer not in self._signers:
                return False, "Not a signer"
            if amount > self._balance:
                return False, "Insufficient treasury balance"
            txid = hashlib.sha256(
                f"TREAS:{recipient}:{amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._txs.append({
                "id":          txid,
                "proposer":    proposer,
                "recipient":   recipient,
                "amount":      amount,
                "category":    category,
                "description": description,
                "status":      "pending",
            })
            self._sigs[txid] = {proposer}
            return True, txid

    def sign_and_execute(self, signer: str,
                          tx_id: str) -> Tuple[bool, str]:
        with self._lock:
            if signer not in self._signers:
                return False, "Not a signer"
            tx = next((t for t in self._txs if t["id"] == tx_id), None)
            if not tx or tx["status"] != "pending":
                return False, "Not found"
            self._sigs[tx_id].add(signer)
            if len(self._sigs[tx_id]) >= self._required:
                self._balance -= tx["amount"]
                tx["status"] = "executed"
                return True, f"Executed: {tx['amount']/10**DECIMALS:.3f} NBL to {tx['recipient']}"
            return True, f"Signed ({len(self._sigs[tx_id])}/{self._required})"

    def treasury_v3_stats(self) -> dict:
        with self._lock:
            executed = sum(1 for t in self._txs if t["status"] == "executed")
        allocations = {
            cat: {
                "pct":     f"{pct*100:.0f}%",
                "amount":  f"{int(self._balance*pct)/10**DECIMALS:.3f} NBL",
            }
            for cat, pct in self.ALLOCATION.items()
        }
        return {
            "balance_nbl":  f"{self._balance/10**DECIMALS:.3f}",
            "signers":      len(self._signers),
            "required":     self._required,
            "txs":          len(self._txs),
            "executed":     executed,
            "allocations":  allocations,
        }


# ---- OnChainCoinFlip
class OnChainCoinFlip:
    """Provably fair on-chain coin flip game."""

    HOUSE_EDGE = 0.02   # 2%

    def __init__(self, blockchain: 'NEBULABlockchain',
                  rng: 'OnChainRNG'):
        self._bc     = blockchain
        self._rng    = rng
        self._games: List[dict] = []

    def flip(self, player: str, bet_nbl: float,
              choice: str) -> dict:
        if choice not in ("heads", "tails"):
            return {"error": "Choose heads or tails"}
        bet    = int(bet_nbl * 10**DECIMALS)
        if self._bc.utxo.balance(player) < bet:
            return {"error": "Insufficient balance"}
        rand   = self._rng.random_int(self._bc.height, 2)
        result = "heads" if rand == 0 else "tails"
        win    = result == choice
        payout = int(bet * (2 - self.HOUSE_EDGE)) if win else 0
        game   = {
            "player":   player,
            "bet":      bet,
            "choice":   choice,
            "result":   result,
            "won":      win,
            "payout":   payout,
            "block":    self._bc.height,
        }
        self._games.append(game)
        return game


# ---- OnChainDice
class OnChainDice:
    """Provably fair dice game."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  rng: 'OnChainRNG'):
        self._bc    = blockchain
        self._rng   = rng
        self._rolls: List[dict] = []

    def roll(self, player: str, bet_nbl: float,
              target: int, over: bool = True) -> dict:
        """Roll 1-100, win if result > target (or < target if over=False)."""
        if not 1 <= target <= 99:
            return {"error": "Target must be 1-99"}
        bet    = int(bet_nbl * 10**DECIMALS)
        result = self._rng.random_int(self._bc.height, 100, nonce=len(self._rolls)) + 1
        if over:
            win     = result > target
            win_pct = (100 - target) / 100
        else:
            win     = result < target
            win_pct = target / 100
        multiplier = (1 - 0.02) / win_pct if win_pct > 0 else 0
        payout     = int(bet * multiplier) if win else 0
        roll_data  = {
            "player":     player,
            "bet":        bet,
            "target":     target,
            "over":       over,
            "result":     result,
            "won":        win,
            "multiplier": f"{multiplier:.2f}x",
            "payout":     payout,
        }
        self._rolls.append(roll_data)
        return roll_data
