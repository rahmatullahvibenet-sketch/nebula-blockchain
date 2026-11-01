"""NEBULA group42 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. YieldOptimizer  (orig. lines 69076-69100)
   2. DollarCostAverager  (orig. lines 69103-69133)
   3. ConfidentialTransaction  (orig. lines 69147-69184)
   4. PrivacyPoolV2  (orig. lines 69186-69247)
   5. NBLDomain  (orig. lines 69254-69275)
   6. NEBULANameService  (orig. lines 69277-69376)
   7. EcosystemHub  (orig. lines 69383-69462)
   8. VoteEscrowedNBL  (orig. lines 69524-69592)
   9. MEVProtector  (orig. lines 69599-69660)
  10. CrossMarginAccount  (orig. lines 69667-69699)
  11. CrossMarginEngine  (orig. lines 69701-69765)
  12. InterestRateModel  (orig. lines 69772-69792)
  13. LendingPoolV2  (orig. lines 69794-69851)
  14. LendingProtocolV2  (orig. lines 69853-69891)
  15. VaultStrategy  (orig. lines 69898-69950)
  16. VaultManager  (orig. lines 69952-70015)
  17. FractionalNFTDex  (orig. lines 70022-70100)
  18. TokenomicsEngine  (orig. lines 70107-70192)
  19. SybilResistanceScore  (orig. lines 70199-70245)
  20. BlockchainIndexer  (orig. lines 70252-70329)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): DeFiStrategy, NEBULABlockchain, PedersenCommitment
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


# ---- YieldOptimizer
class YieldOptimizer(DeFiStrategy):
    """Moves funds to highest-yielding protocol."""

    def __init__(self):
        super().__init__(
            "Yield Optimizer",
            "Automatically moves funds to highest yield"
        )

    def find_best_yield(self) -> List[dict]:
        options = [
            {"protocol": "NEBULA Staking 365d", "apy": 0.25, "risk": "low"},
            {"protocol": "NEBULA DEX LP",       "apy": 0.35, "risk": "medium"},
            {"protocol": "NEBULA Farming",       "apy": 0.65, "risk": "high"},
            {"protocol": "NEBULA Lending",       "apy": 0.04, "risk": "low"},
            {"protocol": "NEBULA Insurance",     "apy": 0.15, "risk": "medium"},
        ]
        return sorted(options, key=lambda o: -o["apy"])

    def risk_adjusted_yield(self, max_risk: str = "medium") -> List[dict]:
        all_opts  = self.find_best_yield()
        risk_rank = {"low": 0, "medium": 1, "high": 2}
        max_rank  = risk_rank.get(max_risk, 1)
        return [o for o in all_opts
                if risk_rank.get(o["risk"], 2) <= max_rank]


# ---- DollarCostAverager
class DollarCostAverager(DeFiStrategy):
    """Dollar-cost averaging strategy for NBL accumulation."""

    def __init__(self, interval_blocks: int = 144,
                  amount_per_period: float = 100.0):
        super().__init__(
            "DCA Strategy",
            f"Buy {amount_per_period} NBL worth every {interval_blocks} blocks"
        )
        self.interval    = interval_blocks
        self.amount      = amount_per_period
        self._last_block = 0
        self._total_bought = 0.0

    def should_execute(self, current_block: int) -> bool:
        return current_block - self._last_block >= self.interval

    def record_execution(self, current_block: int,
                          price: float):
        self._last_block   = current_block
        self._total_bought += self.amount / price
        self.executions   += 1

    def dca_stats(self) -> dict:
        return {
            "strategy":       "DCA",
            "total_executions": self.executions,
            "total_bought":   f"{self._total_bought:.4f} NBL",
            "interval":       f"{self.interval} blocks",
            "per_period":     f"{self.amount:.2f} USD equivalent",
        }


# ---- ConfidentialTransaction
class ConfidentialTransaction:
    """
    Confidential transaction with hidden amounts.
    Uses Pedersen commitments for amount hiding.
    """

    def __init__(self, sender: str, recipient: str,
                  amount: int, blinding_factor: int):
        self.sender     = sender
        self.recipient  = recipient
        self.commitment = PedersenCommitment.commit(amount, blinding_factor)
        self.blinding   = blinding_factor
        self._amount    = amount   # Only known to sender/recipient
        self.tx_id      = hashlib.sha256(
            f"CT:{sender}:{recipient}:{self.commitment[0]}".encode()
        ).hexdigest()

    def reveal_to(self, recipient_address: str) -> Optional[int]:
        """Reveal amount to authorized recipient."""
        if recipient_address == self.recipient:
            return self._amount
        return None

    def verify_sum(self, other: 'ConfidentialTransaction') -> bool:
        """Verify sum of commitments for balance proof."""
        combined = PedersenCommitment.add(
            self.commitment, other.commitment)
        return combined is not None

    def to_dict(self) -> dict:
        return {
            "tx_id":      self.tx_id,
            "sender":     self.sender,
            "recipient":  self.recipient,
            "commitment": [self.commitment[0] % (2**32),
                           self.commitment[1] % (2**32)],
            "amount":     "hidden",
        }


# ---- PrivacyPoolV2
class PrivacyPoolV2:
    """
    Privacy pool v2 for anonymous transfers.
    Mix funds with ZK proofs of membership.
    """

    DENOMINATIONS = [
        10**DECIMALS,       # 1 NBL
        10 * 10**DECIMALS,  # 10 NBL
        100 * 10**DECIMALS, # 100 NBL
        1000 * 10**DECIMALS,# 1000 NBL
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._deposits: Dict[int, List[dict]] = {d: [] for d in self.DENOMINATIONS}
        self._used:     Set[str]              = set()
        self._lock      = threading.RLock()

    def deposit(self, sender: str, denomination: int,
                 nullifier: str) -> Tuple[bool, str]:
        with self._lock:
            if denomination not in self.DENOMINATIONS:
                return False, f"Invalid denomination. Use: {self.DENOMINATIONS}"
            if self._bc.utxo.balance(sender) < denomination:
                return False, "Insufficient balance"
            commitment = hashlib.sha256(
                nullifier.encode() + denomination.to_bytes(8, 'big')
            ).hexdigest()
            self._deposits[denomination].append({
                "commitment":  commitment,
                "deposited_at": self._bc.height,
            })
            return True, commitment

    def withdraw(self, recipient: str, denomination: int,
                  nullifier: str, proof: str) -> Tuple[bool, str]:
        with self._lock:
            if nullifier in self._used:
                return False, "Nullifier already used (double spend)"
            commitment = hashlib.sha256(
                nullifier.encode() + denomination.to_bytes(8, 'big')
            ).hexdigest()
            deposits = self._deposits.get(denomination, [])
            if not any(d["commitment"] == commitment for d in deposits):
                return False, "Commitment not found"
            self._used.add(nullifier)
            return True, f"Withdrew {denomination/10**DECIMALS:.0f} NBL anonymously"

    def pool_stats(self) -> dict:
        with self._lock:
            total_deposits = sum(len(d) for d in self._deposits.values())
            total_value    = sum(
                denom * len(deps)
                for denom, deps in self._deposits.items()
            )
        return {
            "total_deposits": total_deposits,
            "total_value_nbl": f"{total_value/10**DECIMALS:.3f}",
            "used_nullifiers": len(self._used),
            "denominations":   [f"{d/10**DECIMALS:.0f}" for d in self.DENOMINATIONS],
        }


# ---- NBLDomain
@dataclass
class NBLDomain:
    domain:     str      # e.g. "zayn.nbl"
    owner:      str
    resolver:   str      # resolved address
    expiry:     float
    records:    Dict[str, str] = field(default_factory=dict)
    subdomains: List[str]      = field(default_factory=list)

    @property
    def is_expired(self) -> bool:
        return time.time() > self.expiry

    def to_dict(self) -> dict:
        return {
            "domain":   self.domain,
            "owner":    self.owner,
            "resolver": self.resolver,
            "expiry":   time.strftime('%Y-%m-%d', time.localtime(self.expiry)),
            "expired":  self.is_expired,
            "records":  self.records,
        }


# ---- NEBULANameService
class NEBULANameService:
    """
    NEBULA Name Service (NNS) — human-readable addresses.
    e.g. "zayn.nbl" → "NbL1234...abc"
    """

    TLD           = ".nbl"
    REGISTRATION_FEE_PER_YEAR = int(10 * 10**DECIMALS)   # 10 NBL/year

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._domains: Dict[str, NBLDomain] = {}
        self._reverse: Dict[str, str]       = {}   # address -> domain
        self._lock    = threading.RLock()

    def register(self, label: str, owner: str,
                  years: int = 1) -> Tuple[bool, str]:
        with self._lock:
            domain = f"{label.lower()}{self.TLD}"
            if domain in self._domains and not self._domains[domain].is_expired:
                return False, f"Domain {domain} already registered"
            fee = self.REGISTRATION_FEE_PER_YEAR * years
            if self._bc.utxo.balance(owner) < fee:
                return False, f"Insufficient balance. Need {fee/10**DECIMALS:.0f} NBL"
            self._domains[domain] = NBLDomain(
                domain   = domain,
                owner    = owner,
                resolver = owner,
                expiry   = time.time() + years * 365 * 86400,
            )
            self._reverse[owner] = domain
            return True, domain

    def resolve(self, domain: str) -> Optional[str]:
        """Resolve domain to address."""
        if not domain.endswith(self.TLD):
            domain = domain + self.TLD
        d = self._domains.get(domain.lower())
        if d and not d.is_expired:
            return d.resolver
        return None

    def reverse_resolve(self, address: str) -> Optional[str]:
        """Resolve address to domain."""
        return self._reverse.get(address)

    def set_record(self, domain: str, key: str,
                    value: str, owner: str) -> Tuple[bool, str]:
        with self._lock:
            d = self._domains.get(domain.lower())
            if not d or d.owner != owner:
                return False, "Not found or not owner"
            if d.is_expired:
                return False, "Domain expired"
            d.records[key] = value
            return True, f"Set {domain} {key} = {value}"

    def set_subdomain(self, parent: str, label: str,
                       owner: str, resolver: str) -> Tuple[bool, str]:
        with self._lock:
            parent_d = self._domains.get(parent.lower())
            if not parent_d or parent_d.owner != owner:
                return False, "Parent domain not found or not owner"
            sub = f"{label}.{parent}"
            self._domains[sub] = NBLDomain(
                domain   = sub,
                owner    = owner,
                resolver = resolver,
                expiry   = parent_d.expiry,
            )
            parent_d.subdomains.append(sub)
            return True, sub

    def transfer(self, domain: str, new_owner: str,
                  current_owner: str) -> Tuple[bool, str]:
        with self._lock:
            d = self._domains.get(domain.lower())
            if not d or d.owner != current_owner:
                return False, "Not found or not owner"
            old_owner = d.owner
            d.owner   = new_owner
            if self._reverse.get(old_owner) == domain:
                del self._reverse[old_owner]
            self._reverse[new_owner] = domain
            return True, f"Transferred {domain} to {new_owner}"

    def search(self, query: str) -> List[dict]:
        q = query.lower()
        return [d.to_dict() for d in self._domains.values()
                if q in d.domain and not d.is_expired]

    def nns_stats(self) -> dict:
        with self._lock:
            active = sum(1 for d in self._domains.values() if not d.is_expired)
        return {
            "total_domains":  len(self._domains),
            "active":         active,
            "tld":            self.TLD,
            "fee_per_year":   f"{self.REGISTRATION_FEE_PER_YEAR/10**DECIMALS:.0f} NBL",
        }


# ---- EcosystemHub
class EcosystemHub:
    """
    Central hub for the entire NEBULA ecosystem.
    Aggregates stats, routes requests, manages integrations.
    """

    def __init__(self, blockchain: 'NEBULABlockchain' = None):
        self._bc = blockchain or NEBULABlockchain()
        self._dapps:     List[dict]        = []
        self._partners:  List[dict]        = []
        self._events:    List[dict]        = []

    def register_dapp(self, name: str, url: str,
                       category: str, description: str) -> str:
        did = hashlib.sha256(f"DAPP:{name}:{time.time()}".encode()).hexdigest()[:8]
        self._dapps.append({
            "id":          did,
            "name":        name,
            "url":         url,
            "category":    category,
            "description": description,
            "registered":  time.time(),
        })
        return did

    def register_partner(self, name: str, category: str,
                          website: str) -> str:
        pid = hashlib.sha256(f"PARTNER:{name}:{time.time()}".encode()).hexdigest()[:8]
        self._partners.append({
            "id":       pid,
            "name":     name,
            "category": category,
            "website":  website,
        })
        return pid

    def emit_ecosystem_event(self, event_type: str,
                              title: str, data: dict = None):
        self._events.append({
            "type":      event_type,
            "title":     title,
            "data":      data or {},
            "timestamp": time.time(),
        })

    def full_ecosystem_stats(self) -> dict:
        bc = self._bc
        return {
            "network": {
                "chain_height":  bc.height,
                "total_supply":  f"{bc.utxo.total_supply()/10**DECIMALS:.3f} NBL",
                "mempool_txs":   bc.mempool.size(),
                "utxo_entries":  bc.utxo.size(),
            },
            "ecosystem": {
                "registered_dapps":    len(self._dapps),
                "partners":            len(self._partners),
                "total_events":        len(self._events),
            },
            "protocol": {
                "chain_id":      CHAIN_ID,
                "decimals":      DECIMALS,
                "block_time":    f"{TARGET_BLOCK_TIME}s",
                "halving_int":   f"{HALVING_INTERVAL:,} blocks",
                "max_supply":    f"{MAX_SUPPLY/10**DECIMALS:,.0f} NBL",
            },
            "categories": [
                "defi", "nft", "gaming", "social",
                "identity", "governance", "bridge",
                "data_market", "insurance", "analytics",
            ],
        }

    def dapps_by_category(self, category: str = None) -> List[dict]:
        if category:
            return [d for d in self._dapps if d["category"] == category]
        return list(self._dapps)

    def recent_events(self, n: int = 20) -> List[dict]:
        return sorted(self._events, key=lambda e: -e["timestamp"])[:n]


# ---- VoteEscrowedNBL
class VoteEscrowedNBL:
    """
    veNBL: Vote-Escrowed NBL (like veCRV).
    Lock NBL for up to 4 years to get boosted voting power.
    Longer lock = more veNBL = more governance power.
    """

    MAX_LOCK_BLOCKS = 4 * 365 * 144   # 4 years

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._locks: Dict[str, dict] = {}
        self._lock  = threading.RLock()

    def lock(self, address: str, amount: int,
              lock_blocks: int) -> Tuple[bool, str]:
        with self._lock:
            if lock_blocks > self.MAX_LOCK_BLOCKS:
                return False, f"Max lock: {self.MAX_LOCK_BLOCKS} blocks"
            if self._bc.utxo.balance(address) < amount:
                return False, "Insufficient balance"
            if address in self._locks:
                existing = self._locks[address]
                new_unlock = max(existing["unlock_block"],
                                  self._bc.height + lock_blocks)
                self._locks[address]["amount"]       += amount
                self._locks[address]["unlock_block"]  = new_unlock
            else:
                self._locks[address] = {
                    "amount":       amount,
                    "lock_blocks":  lock_blocks,
                    "locked_at":    self._bc.height,
                    "unlock_block": self._bc.height + lock_blocks,
                }
            venbl = self.balance(address)
            return True, f"Locked {amount/10**DECIMALS:.3f} NBL → {venbl/10**DECIMALS:.3f} veNBL"

    def balance(self, address: str) -> int:
        """veNBL balance = NBL * (remaining_lock / max_lock)."""
        lock = self._locks.get(address)
        if not lock:
            return 0
        remaining = max(0, lock["unlock_block"] - self._bc.height)
        ratio = remaining / self.MAX_LOCK_BLOCKS
        return int(lock["amount"] * ratio)

    def unlock(self, address: str) -> Tuple[bool, int]:
        with self._lock:
            lock = self._locks.get(address)
            if not lock:
                return False, 0
            if self._bc.height < lock["unlock_block"]:
                return False, lock["unlock_block"] - self._bc.height
            amount = lock["amount"]
            del self._locks[address]
            return True, amount

    def total_venbl(self) -> int:
        return sum(self.balance(addr) for addr in self._locks)

    def venbl_stats(self) -> dict:
        total_locked = sum(l["amount"] for l in self._locks.values())
        total_venbl  = self.total_venbl()
        return {
            "total_locked_nbl":  f"{total_locked/10**DECIMALS:.3f}",
            "total_venbl":       f"{total_venbl/10**DECIMALS:.3f}",
            "lock_count":        len(self._locks),
            "max_lock_years":    4,
        }


# ---- MEVProtector
class MEVProtector:
    """
    MEV (Miner/Maximal Extractable Value) protection for NEBULA.
    Commit-reveal scheme, private mempool, fair ordering.
    """

    def __init__(self, mempool: 'Mempool',
                  blockchain: 'NEBULABlockchain'):
        self._mp  = mempool
        self._bc  = blockchain
        self._committed: Dict[str, dict] = {}   # commitment -> tx info
        self._lock = threading.RLock()

    def commit(self, tx_hash: bytes,
                secret: bytes) -> str:
        """Commit to a transaction without revealing it."""
        commitment = hashlib.sha256(tx_hash + secret).hexdigest()
        with self._lock:
            self._committed[commitment] = {
                "committed_at": self._bc.height,
                "revealed":     False,
            }
        return commitment

    def reveal(self, commitment: str, tx: 'Transaction',
                secret: bytes) -> Tuple[bool, str]:
        """Reveal a committed transaction."""
        with self._lock:
            info = self._committed.get(commitment)
            if not info:
                return False, "Commitment not found"
            if info["revealed"]:
                return False, "Already revealed"
            check = hashlib.sha256(bytes.fromhex(tx.txid) + secret).hexdigest()
            if check != commitment:
                return False, "Commitment mismatch"
            info["revealed"] = True
        ok, msg = self._mp.submit(tx)
        return ok, msg

    def detect_sandwich(self, tx: 'Transaction') -> bool:
        """Detect potential sandwich attack pattern."""
        # Simple heuristic: large tx with high fee may be front-run target
        fee   = tx.fee(self._mp._utxo) if hasattr(self._mp, '_utxo') else 0
        size  = tx.total_output()
        if size > 100_000 * 10**DECIMALS and fee > MIN_TX_FEE * 10:
            return True
        return False

    def fairness_ordering(self, txs: List['Transaction']) -> List['Transaction']:
        """Order transactions fairly (arrival time, not fee)."""
        return txs   # In practice: sort by arrival time

    def mev_stats(self) -> dict:
        with self._lock:
            revealed = sum(1 for c in self._committed.values()
                           if c["revealed"])
        return {
            "total_commitments": len(self._committed),
            "revealed":          revealed,
            "pending":           len(self._committed) - revealed,
        }


# ---- CrossMarginAccount
class CrossMarginAccount:
    """Cross-margin account using single collateral pool."""

    def __init__(self, address: str, collateral: int):
        self.address    = address
        self.collateral = collateral
        self.positions: List[dict] = []
        self.total_pnl  = 0.0

    @property
    def margin_used(self) -> float:
        return sum(p.get("margin", 0) for p in self.positions)

    @property
    def free_margin(self) -> float:
        return self.collateral / 10**DECIMALS - self.margin_used + self.total_pnl

    @property
    def margin_level(self) -> float:
        if self.margin_used == 0:
            return float('inf')
        return (self.collateral / 10**DECIMALS + self.total_pnl) / self.margin_used

    def to_dict(self) -> dict:
        return {
            "address":     self.address,
            "collateral":  f"{self.collateral/10**DECIMALS:.3f} NBL",
            "margin_used": f"{self.margin_used:.3f}",
            "free_margin": f"{self.free_margin:.3f}",
            "margin_level": f"{self.margin_level:.2f}",
            "positions":   len(self.positions),
            "total_pnl":   f"{self.total_pnl:.4f}",
        }


# ---- CrossMarginEngine
class CrossMarginEngine:
    """Cross-margin trading engine for NEBULA."""

    MARGIN_CALL_LEVEL = 1.2    # margin call at 120%
    LIQUIDATION_LEVEL = 1.0    # liquidate at 100%

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc       = blockchain
        self._oracle   = oracle
        self._accounts: Dict[str, CrossMarginAccount] = {}
        self._lock      = threading.RLock()

    def open_account(self, address: str,
                      collateral_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            if address in self._accounts:
                return False, "Account already exists"
            collateral = int(collateral_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(address) < collateral:
                return False, "Insufficient balance"
            self._accounts[address] = CrossMarginAccount(address, collateral)
            return True, f"Account opened with {collateral_nbl} NBL collateral"

    def deposit_collateral(self, address: str,
                            amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            acct = self._accounts.get(address)
            if not acct:
                return False, "Account not found"
            amount = int(amount_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(address) < amount:
                return False, "Insufficient balance"
            acct.collateral += amount
            return True, f"Deposited {amount_nbl} NBL"

    def check_margin_calls(self) -> List[str]:
        calls = []
        with self._lock:
            for addr, acct in self._accounts.items():
                ml = acct.margin_level
                if ml < self.MARGIN_CALL_LEVEL:
                    calls.append(addr)
        return calls

    def liquidate_account(self, address: str) -> Tuple[bool, str]:
        with self._lock:
            acct = self._accounts.get(address)
            if not acct:
                return False, "Not found"
            if acct.margin_level > self.LIQUIDATION_LEVEL:
                return False, "Not at liquidation level"
            acct.positions.clear()
            return True, f"Account {address} liquidated"

    def cross_margin_stats(self) -> dict:
        with self._lock:
            total_col   = sum(a.collateral for a in self._accounts.values())
            margin_calls = [a for a in self._accounts.values()
                            if a.margin_level < self.MARGIN_CALL_LEVEL]
        return {
            "accounts":         len(self._accounts),
            "total_collateral": f"{total_col/10**DECIMALS:.3f} NBL",
            "margin_calls":     len(margin_calls),
        }


# ---- InterestRateModel
class InterestRateModel:
    """Interest rate model for lending protocol."""

    def __init__(self, base_rate: float = 0.02,
                  optimal_util: float = 0.80,
                  slope1: float = 0.10,
                  slope2: float = 1.00):
        self.base_rate    = base_rate
        self.optimal_util = optimal_util
        self.slope1       = slope1
        self.slope2       = slope2

    def borrow_rate(self, utilization: float) -> float:
        if utilization <= self.optimal_util:
            return self.base_rate + utilization / self.optimal_util * self.slope1
        excess = (utilization - self.optimal_util) / (1 - self.optimal_util)
        return self.base_rate + self.slope1 + excess * self.slope2

    def supply_rate(self, utilization: float,
                     reserve_factor: float = 0.10) -> float:
        return self.borrow_rate(utilization) * utilization * (1 - reserve_factor)


# ---- LendingPoolV2
class LendingPoolV2:
    """Enhanced lending pool with variable interest rates."""

    def __init__(self, asset: str, irm: InterestRateModel):
        self.asset         = asset
        self.irm           = irm
        self.total_supply  = 0
        self.total_borrows = 0
        self.reserve_factor = 0.10
        self._deposits:    Dict[str, dict] = {}
        self._loans:       Dict[str, dict] = {}
        self._collateral:  Dict[str, dict] = {}

    @property
    def utilization(self) -> float:
        if self.total_supply == 0:
            return 0.0
        return min(1.0, self.total_borrows / self.total_supply)

    @property
    def borrow_apy(self) -> float:
        return self.irm.borrow_rate(self.utilization)

    @property
    def supply_apy(self) -> float:
        return self.irm.supply_rate(self.utilization, self.reserve_factor)

    def deposit(self, address: str, amount: int) -> bool:
        self.total_supply += amount
        if address not in self._deposits:
            self._deposits[address] = {"amount": 0, "deposited_at": time.time()}
        self._deposits[address]["amount"] += amount
        return True

    def borrow(self, address: str, amount: int,
                collateral: int) -> Tuple[bool, str]:
        min_col = int(amount * 1.5)
        if collateral < min_col:
            return False, f"Need {min_col} collateral"
        if amount > self.total_supply - self.total_borrows:
            return False, "Insufficient liquidity"
        self.total_borrows += amount
        self._loans[address] = {
            "amount":      amount,
            "collateral":  collateral,
            "borrowed_at": time.time(),
        }
        return True, f"Borrowed {amount} {self.asset}"

    def pool_info(self) -> dict:
        return {
            "asset":         self.asset,
            "total_supply":  f"{self.total_supply/10**DECIMALS:.3f}",
            "total_borrows": f"{self.total_borrows/10**DECIMALS:.3f}",
            "utilization":   f"{self.utilization*100:.1f}%",
            "borrow_apy":    f"{self.borrow_apy*100:.2f}%",
            "supply_apy":    f"{self.supply_apy*100:.2f}%",
        }


# ---- LendingProtocolV2
class LendingProtocolV2:
    """Lending protocol v2 with dynamic interest rates."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._pools: Dict[str, LendingPoolV2] = {}
        self._irm   = InterestRateModel()
        self._lock  = threading.RLock()

    def create_pool(self, asset: str) -> str:
        with self._lock:
            irm = InterestRateModel()
            self._pools[asset] = LendingPoolV2(asset, irm)
            return asset

    def deposit(self, address: str, asset: str,
                 amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(asset)
            if not pool:
                return False, "Pool not found"
            return pool.deposit(address, int(amount_nbl * 10**DECIMALS)), "Deposited"

    def borrow(self, address: str, asset: str,
                amount_nbl: float, collateral_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(asset)
            if not pool:
                return False, "Pool not found"
            return pool.borrow(
                address,
                int(amount_nbl * 10**DECIMALS),
                int(collateral_nbl * 10**DECIMALS)
            )

    def protocol_stats_v2(self) -> dict:
        with self._lock:
            pools = [p.pool_info() for p in self._pools.values()]
        return {"pools": pools, "total_pools": len(self._pools)}


# ---- VaultStrategy
class VaultStrategy:
    """Automated vault strategy that compounds yield."""

    def __init__(self, vault_id: str, name: str,
                  strategy_type: str):
        self.vault_id      = vault_id
        self.name          = name
        self.strategy_type = strategy_type
        self.total_assets  = 0
        self.shares:       Dict[str, int] = {}
        self.total_shares  = 0
        self._harvested    = 0

    def deposit(self, depositor: str, amount: int) -> int:
        if self.total_assets == 0 or self.total_shares == 0:
            shares = amount
        else:
            shares = amount * self.total_shares // self.total_assets
        self.shares[depositor]  = self.shares.get(depositor, 0) + shares
        self.total_shares      += shares
        self.total_assets      += amount
        return shares

    def withdraw(self, depositor: str, shares: int) -> int:
        owned = self.shares.get(depositor, 0)
        if owned < shares:
            return 0
        amount = shares * self.total_assets // max(1, self.total_shares)
        self.shares[depositor] -= shares
        self.total_shares      -= shares
        self.total_assets      -= amount
        return amount

    def harvest(self, yield_amount: int):
        """Compound yield into the vault."""
        self.total_assets += yield_amount
        self._harvested   += yield_amount

    def share_price(self) -> float:
        if self.total_shares == 0:
            return 1.0
        return self.total_assets / self.total_shares

    def vault_info(self) -> dict:
        return {
            "vault_id":    self.vault_id,
            "name":        self.name,
            "strategy":    self.strategy_type,
            "total_assets": f"{self.total_assets/10**DECIMALS:.3f}",
            "share_price": f"{self.share_price():.6f}",
            "depositors":  len(self.shares),
            "harvested":   f"{self._harvested/10**DECIMALS:.6f}",
        }


# ---- VaultManager
class VaultManager:
    """Manages automated yield vaults."""

    STRATEGIES = [
        ("nbl_staking_180d", "NBL 180-Day Staking", "staking"),
        ("nbl_usdt_lp",      "NBL-USDT LP Farming", "farming"),
        ("nbl_compound",     "NBL Auto-Compound",   "compound"),
        ("nbl_defi_blend",   "DeFi Blend",          "blend"),
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._vaults: Dict[str, VaultStrategy] = {}
        self._lock   = threading.RLock()
        for vid, name, stype in self.STRATEGIES:
            self._vaults[vid] = VaultStrategy(vid, name, stype)

    def deposit(self, vault_id: str, depositor: str,
                 amount_nbl: float) -> Tuple[bool, int]:
        with self._lock:
            vault = self._vaults.get(vault_id)
            if not vault:
                return False, 0
            amount = int(amount_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(depositor) < amount:
                return False, 0
            shares = vault.deposit(depositor, amount)
            return True, shares

    def withdraw(self, vault_id: str, depositor: str,
                  shares: int) -> Tuple[bool, int]:
        with self._lock:
            vault = self._vaults.get(vault_id)
            if not vault:
                return False, 0
            amount = vault.withdraw(depositor, shares)
            return amount > 0, amount

    def harvest_all(self) -> dict:
        results = {}
        with self._lock:
            for vid, vault in self._vaults.items():
                simulated_yield = int(vault.total_assets * 0.0001)
                vault.harvest(simulated_yield)
                results[vid] = simulated_yield
        return results

    def all_vaults(self) -> List[dict]:
        return [v.vault_info() for v in self._vaults.values()]

    def user_positions(self, address: str) -> List[dict]:
        positions = []
        for v in self._vaults.values():
            shares = v.shares.get(address, 0)
            if shares > 0:
                value = int(shares * v.share_price())
                positions.append({
                    "vault_id":    v.vault_id,
                    "name":        v.name,
                    "shares":      shares,
                    "value_nbl":   f"{value/10**DECIMALS:.6f}",
                    "share_price": f"{v.share_price():.6f}",
                })
        return positions


# ---- FractionalNFTDex
class FractionalNFTDex:
    """
    DEX for trading fractionalized NFT tokens.
    Each fractional NFT becomes tradeable like a fungible token.
    """

    def __init__(self, fractionalizer: 'NFTFractionalizer',
                  blockchain: 'NEBULABlockchain'):
        self._frac     = fractionalizer
        self._bc       = blockchain
        self._listings: Dict[str, dict] = {}   # vault_id -> listing info
        self._trades:   List[dict]      = []
        self._lock      = threading.RLock()

    def list_fractions(self, vault_id: str, seller: str,
                        amount: int, price_per_fraction: float) -> Tuple[bool, str]:
        with self._lock:
            vault = self._frac._vaults.get(vault_id)
            if not vault:
                return False, "Vault not found"
            if vault["holders"].get(seller, 0) < amount:
                return False, "Insufficient fractions"
            lid = hashlib.sha256(
                f"FRACDEX:{vault_id}:{seller}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._listings[lid] = {
                "listing_id": lid,
                "vault_id":   vault_id,
                "seller":     seller,
                "amount":     amount,
                "price":      price_per_fraction,
                "filled":     0,
            }
            return True, lid

    def buy_fractions(self, buyer: str, listing_id: str,
                       amount: int) -> Tuple[bool, str]:
        with self._lock:
            listing = self._listings.get(listing_id)
            if not listing:
                return False, "Listing not found"
            available = listing["amount"] - listing["filled"]
            if amount > available:
                return False, f"Only {available} fractions available"
            cost = int(amount * listing["price"] * 10**DECIMALS)
            if self._bc.utxo.balance(buyer) < cost:
                return False, "Insufficient funds"
            ok, msg = self._frac.transfer_fractions(
                listing["vault_id"],
                listing["seller"],
                buyer,
                amount
            )
            if ok:
                listing["filled"] += amount
                self._trades.append({
                    "vault_id": listing["vault_id"],
                    "buyer":    buyer,
                    "seller":   listing["seller"],
                    "amount":   amount,
                    "price":    listing["price"],
                    "ts":       time.time(),
                })
            return ok, msg

    def market_data(self, vault_id: str) -> dict:
        relevant = [t for t in self._trades if t["vault_id"] == vault_id]
        if not relevant:
            return {"vault_id": vault_id, "trades": 0}
        prices  = [t["price"] for t in relevant]
        volumes = sum(t["amount"] for t in relevant)
        return {
            "vault_id":   vault_id,
            "last_price": f"{prices[-1]:.4f}",
            "high":       f"{max(prices):.4f}",
            "low":        f"{min(prices):.4f}",
            "volume":     volumes,
            "trades":     len(relevant),
        }


# ---- TokenomicsEngine
class TokenomicsEngine:
    """
    NEBULA tokenomics engine.
    Models supply, demand, inflation, burn mechanics.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._burns: List[dict] = []
        self._lock   = threading.RLock()

    def circulating_supply(self) -> int:
        return self._bc.utxo.total_supply()

    def inflation_rate(self) -> float:
        """Current annual inflation rate."""
        h         = self._bc.height
        reward    = mining_reward(h)
        annual    = reward * 365 * 144
        supply    = self.circulating_supply()
        if supply == 0:
            return 0.0
        return annual / supply

    def halving_schedule(self) -> List[dict]:
        """Full halving schedule."""
        schedule = []
        reward   = INITIAL_BLOCK_REWARD
        for era in range(34):   # ~134 years
            h_start = era * HALVING_INTERVAL
            h_end   = (era + 1) * HALVING_INTERVAL
            era_supply = reward * HALVING_INTERVAL
            schedule.append({
                "era":         era + 1,
                "start_block": h_start,
                "end_block":   h_end,
                "reward_nbl":  f"{reward/10**DECIMALS:.9f}",
                "era_supply":  f"{era_supply/10**DECIMALS:.3f}",
            })
            reward = reward // 2
            if reward == 0:
                break
        return schedule

    def total_ever_issued(self) -> int:
        """Total NBL that will ever be mined."""
        total  = 0
        reward = INITIAL_BLOCK_REWARD
        while reward > 0:
            total  += reward * HALVING_INTERVAL
            reward  = reward // 2
        return total

    def burn_tokens(self, amount: int, reason: str = "") -> bool:
        """Permanently burn tokens (deflationary)."""
        with self._lock:
            self._burns.append({
                "amount": amount,
                "reason": reason,
                "block":  self._bc.height,
                "ts":     time.time(),
            })
            return True

    def total_burned(self) -> int:
        return sum(b["amount"] for b in self._burns)

    def effective_supply(self) -> int:
        return self.circulating_supply() - self.total_burned()

    def tokenomics_report(self) -> dict:
        h       = self._bc.height
        reward  = mining_reward(h)
        circ    = self.circulating_supply()
        burned  = self.total_burned()
        return {
            "circulating_supply":  f"{circ/10**DECIMALS:.3f}",
            "max_supply":          f"{MAX_SUPPLY/10**DECIMALS:.0f}",
            "total_burned":        f"{burned/10**DECIMALS:.3f}",
            "effective_supply":    f"{(circ-burned)/10**DECIMALS:.3f}",
            "current_reward":      f"{reward/10**DECIMALS:.9f} NBL",
            "annual_inflation":    f"{self.inflation_rate()*100:.2f}%",
            "supply_issued_pct":   f"{circ/MAX_SUPPLY*100:.4f}%",
            "halvings_completed":  h // HALVING_INTERVAL,
            "next_halving_block":  (h // HALVING_INTERVAL + 1) * HALVING_INTERVAL,
        }


# ---- SybilResistanceScore
class SybilResistanceScore:
    """Measures how likely an address is a unique human."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._scores:  Dict[str, dict] = {}
        self._verified: Set[str]       = set()

    def compute(self, address: str) -> dict:
        score       = 0
        reasons     = []
        # Balance check
        bal = self._bc.utxo.balance(address)
        if bal > 100 * 10**DECIMALS:
            score += 20
            reasons.append("holds_nbl")
        # Transaction history
        utxos = self._bc.utxo.get_by_address(address)  # FIX
        if len(utxos) > 3:
            score += 20
            reasons.append("active_wallet")
        # Verified identity
        if address in self._verified:
            score += 50
            reasons.append("identity_verified")
        # Age heuristic
        if bal > 1000 * 10**DECIMALS:
            score += 10
            reasons.append("significant_holder")
        return {
            "address":    address,
            "score":      score,
            "max_score":  100,
            "human_prob": f"{score}%",
            "reasons":    reasons,
            "verified":   address in self._verified,
        }

    def verify_identity(self, address: str,
                         did_proof: str = "") -> bool:
        self._verified.add(address)
        return True

    def is_likely_sybil(self, address: str,
                          threshold: int = 20) -> bool:
        result = self.compute(address)
        return result["score"] < threshold


# ---- BlockchainIndexer
class BlockchainIndexer:
    """
    Full blockchain indexer for NEBULA.
    Indexes all events, transfers, swaps, governance actions.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc           = blockchain
        self._tx_index:    Dict[str, dict]        = {}
        self._addr_index:  Dict[str, List[str]]   = {}
        self._event_index: Dict[str, List[dict]]  = {}
        self._block_index: Dict[int, dict]        = {}
        self._lock         = threading.RLock()
        self._last_indexed = -1

    def index_block(self, block: 'Block'):
        with self._lock:
            block_data = {
                "height":    block.height,
                "hash":      block.hash,
                "timestamp": block.header.timestamp,
                "tx_count":  block.tx_count,
                "size":      block.byte_size(),
            }
            self._block_index[block.height] = block_data
            for i, tx in enumerate(block.transactions):
                self._tx_index[tx.txid] = {
                    "txid":   tx.txid,
                    "block":  block.height,
                    "pos":    i,
                    "time":   block.header.timestamp,
                }
                for out in tx.outputs:
                    addr = out.address
                    if addr:
                        if addr not in self._addr_index:
                            self._addr_index[addr] = []
                        if tx.txid not in self._addr_index[addr]:
                            self._addr_index[addr].append(tx.txid)
            self._last_indexed = block.height

    def index_all(self) -> int:
        count = 0
        for h in range(self._last_indexed + 1, self._bc.height + 1):
            blk = self._bc.get_block(h)
            if blk:
                self.index_block(blk)
                count += 1
        return count

    def query_address(self, address: str,
                       limit: int = 50) -> dict:
        txids = self._addr_index.get(address, [])
        txs   = []
        for txid in txids[-limit:]:
            info = self._tx_index.get(txid)
            if info:
                txs.append(info)
        return {
            "address":   address,
            "tx_count":  len(txids),
            "balance":   f"{self._bc.utxo.balance(address)/10**DECIMALS:.9f}",
            "txs":       txs,
        }

    def query_block(self, height: int) -> Optional[dict]:
        return self._block_index.get(height)

    def query_tx(self, txid: str) -> Optional[dict]:
        return self._tx_index.get(txid)

    def index_stats(self) -> dict:
        return {
            "indexed_blocks":  len(self._block_index),
            "indexed_txs":     len(self._tx_index),
            "indexed_addrs":   len(self._addr_index),
            "last_indexed":    self._last_indexed,
        }
