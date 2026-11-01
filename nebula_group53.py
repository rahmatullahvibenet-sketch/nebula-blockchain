"""NEBULA group53 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. LiquidDemocracy  (orig. lines 82405-82469)
   2. TransactionCoalescer  (orig. lines 82476-82518)
   3. ChainSnapshotManager  (orig. lines 82525-82569)
   4. ValidatorRewardsV2  (orig. lines 82576-82624)
   5. ConsensusAnalytics  (orig. lines 82707-82736)
   6. WalletAnalytics  (orig. lines 82743-82779)
   7. YieldFarmV3  (orig. lines 82786-82840)
   8. YieldFarmRegistryV3  (orig. lines 82843-82876)
   9. DeFiSafetyModule  (orig. lines 82883-82938)
  10. TreasuryDiversification  (orig. lines 82945-82996)
  11. GovernanceForumV2  (orig. lines 83003-83072)
  12. NFTAuction  (orig. lines 83079-83124)
  13. NFTMarketplaceV3  (orig. lines 83126-83174)
  14. StakingInsurancePoolV2  (orig. lines 83181-83243)
  15. ChainPruning  (orig. lines 83250-83284)
  16. ExtendedTestSuiteV2  (orig. lines 83334-83485)
  17. BlockTemplateV2  (orig. lines 83492-83557)
  18. SwapAggregatorV2  (orig. lines 83564-83632)
  19. NFTRoyaltyDAO  (orig. lines 83639-83696)
  20. PredictionOracle  (orig. lines 83703-83759)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): AdvancedDEXV2, BlockHeader, GovernanceV3, MerkleTree, NBL721Registry, NEBULABlockchain, NEBULAWallet, OptionsProtocolV2, OracleV2, P2PKHScript, SyntheticAssetProtocol, Transaction, TransactionOutput, ZKRollupLayer
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

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

DIFFICULTY_WINDOW      = 2016                           # blocks per retarget

MAX_TARGET             = 0x0fffff * (256 ** ((0x1e if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d) - 3))   # [v10.24]   # bits_to_target(INITIAL_BITS) — max allowed PoW target

MAX_BLOCK_SIZE_BYTES   = 1_048_576                      # 1 MB

MAX_TX_PER_BLOCK       = 3000

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

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

def err(msg, code=None):
    """CLI: err("text") prints a red line.  REST API (v10.10 fix): err("text", 404) -> (404, body)."""
    if code is None:
        print(c(f"❌ {msg}", C.RED))
        return None
    return code, {"success": False, "error": str(msg)}

def info(msg):  print(c(f"ℹ️  {msg}", C.CYAN))

_routes: Dict[str, Dict[str, Callable]] = {}

def route(path: str, methods: List[str] = None):
    """Decorator to register an API endpoint."""
    def decorator(fn: Callable) -> Callable:
        for method in (methods or ["GET"]):
            _routes.setdefault(method.upper(), {})[path] = fn
        return fn
    return decorator

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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- LiquidDemocracy
class LiquidDemocracy:
    """
    Liquid democracy for NEBULA governance.
    Delegate votes to experts, or vote directly.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  governance: 'GovernanceEngine'):
        self._bc         = blockchain
        self._gov        = governance
        self._delegations: Dict[str, str] = {}   # delegator -> delegate
        self._topics:    Dict[str, Dict[str, str]] = {}  # topic -> {delegator: delegate}
        self._lock       = threading.RLock()

    def delegate(self, delegator: str,
                  delegate_to: str,
                  topic: str = "all") -> Tuple[bool, str]:
        with self._lock:
            if delegator == delegate_to:
                return False, "Cannot delegate to self"
            if topic == "all":
                self._delegations[delegator] = delegate_to
            else:
                if topic not in self._topics:
                    self._topics[topic] = {}
                self._topics[topic][delegator] = delegate_to
            return True, f"Delegated to {delegate_to[:8]} for topic '{topic}'"

    def undelegate(self, delegator: str,
                    topic: str = "all") -> bool:
        with self._lock:
            if topic == "all":
                return self._delegations.pop(delegator, None) is not None
            return self._topics.get(topic, {}).pop(delegator, None) is not None

    def resolve_vote(self, voter: str,
                      proposal_id: str) -> str:
        """Resolve who actually votes (may be a delegate)."""
        topic = "governance"
        if voter in self._topics.get(topic, {}):
            return self._topics[topic][voter]
        if voter in self._delegations:
            return self._delegations[voter]
        return voter

    def voting_power(self, address: str) -> dict:
        direct    = self._bc.utxo.balance(address)
        delegated = sum(
            self._bc.utxo.balance(d)
            for d, del_to in self._delegations.items()
            if del_to == address
        )
        return {
            "address":          address,
            "direct_nbl":       f"{direct/10**DECIMALS:.3f}",
            "delegated_nbl":    f"{delegated/10**DECIMALS:.3f}",
            "total_voting_nbl": f"{(direct+delegated)/10**DECIMALS:.3f}",
        }

    def democracy_stats(self) -> dict:
        return {
            "total_delegations":   len(self._delegations),
            "topic_delegations":   sum(len(v) for v in self._topics.values()),
            "active_delegates":    len(set(self._delegations.values())),
        }


# ---- TransactionCoalescer
class TransactionCoalescer:
    """
    Coalesces multiple small transactions into batches.
    Reduces UTXO fragmentation and lowers fees.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._queue: Dict[str, List[dict]] = {}
        self._lock   = threading.RLock()

    def queue_transfer(self, sender: str, to: str,
                        amount: int) -> str:
        with self._lock:
            if sender not in self._queue:
                self._queue[sender] = []
            qid = hashlib.sha256(
                f"COAL:{sender}:{to}:{amount}:{time.time()}".encode()
            ).hexdigest()[:8]
            self._queue[sender].append({
                "qid":    qid,
                "to":     to,
                "amount": amount,
            })
            return qid

    def flush_queue(self, sender: str) -> Tuple[int, int]:
        """Flush all queued transfers for sender into one batch."""
        with self._lock:
            transfers = self._queue.pop(sender, [])
        if not transfers:
            return 0, 0
        total     = sum(t["amount"] for t in transfers)
        count     = len(transfers)
        return count, total

    def queue_stats(self) -> dict:
        with self._lock:
            total = sum(len(q) for q in self._queue.values())
        return {
            "senders":   len(self._queue),
            "total_queued": total,
        }


# ---- ChainSnapshotManager
class ChainSnapshotManager:
    """
    Manages chain snapshots for fast node sync and state backups.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._snapshots: Dict[int, dict] = {}
        self._lock       = threading.RLock()

    def take_snapshot(self) -> dict:
        with self._lock:
            h   = self._bc.height
            utxo_data = {}
            for addr in list(self._bc.utxo._addr_idx.keys())[:500]:
                bal = self._bc.utxo.balance(addr)
                if bal > 0:
                    utxo_data[addr] = bal
            snap = {
                "height":    h,
                "utxo_count": self._bc.utxo.size(),
                "supply":    self._bc.utxo.total_supply(),
                "top_utxos": utxo_data,
                "hash":      hashlib.sha256(
                    json.dumps(utxo_data, sort_keys=True).encode()
                ).hexdigest(),
                "ts":        time.time(),
            }
            self._snapshots[h] = snap
            return snap

    def restore_from(self, height: int) -> bool:
        return height in self._snapshots

    def list_snapshots(self) -> List[dict]:
        return [
            {"height": h, "hash": s["hash"][:16], "ts": s["ts"]}
            for h, s in sorted(self._snapshots.items())
        ]

    def snapshot_stats(self) -> dict:
        return {
            "snapshots":   len(self._snapshots),
            "latest":      max(self._snapshots.keys()) if self._snapshots else 0,
        }


# ---- ValidatorRewardsV2
class ValidatorRewardsV2:
    """
    Enhanced validator rewards with MEV and fee sharing.
    Validators earn: block reward + transaction fees + MEV tips.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._rewards: Dict[str, int] = {}
        self._mev:     Dict[str, int] = {}
        self._blocks:  Dict[str, int] = {}
        self._lock    = threading.RLock()

    def credit_block(self, validator: str, height: int):
        with self._lock:
            reward     = mining_reward(height)
            block_fees = sum(
                tx.byte_size() * MIN_TX_FEE
                for tx in list(self._bc.mempool._txs.values())[:10]
            )
            total = reward + block_fees
            self._rewards[validator] = self._rewards.get(validator, 0) + total
            self._blocks[validator]  = self._blocks.get(validator, 0) + 1

    def credit_mev(self, validator: str, amount: int):
        with self._lock:
            self._mev[validator] = self._mev.get(validator, 0) + amount

    def claim(self, validator: str) -> Tuple[bool, int]:
        with self._lock:
            reward = self._rewards.get(validator, 0)
            mev    = self._mev.get(validator, 0)
            total  = reward + mev
            if total == 0:
                return False, 0
            self._rewards.pop(validator, None)
            self._mev.pop(validator, None)
            return True, total

    def leaderboard(self, n: int = 10) -> List[dict]:
        with self._lock:
            combined = {v: self._rewards.get(v, 0) + self._mev.get(v, 0)
                        for v in set(list(self._rewards.keys()) + list(self._mev.keys()))}
        return [
            {"rank": i+1, "validator": v, "total": f"{t/10**DECIMALS:.6f}",
             "blocks": self._blocks.get(v, 0)}
            for i, (v, t) in enumerate(
                sorted(combined.items(), key=lambda x: -x[1])[:n])
        ]


# ---- ConsensusAnalytics
class ConsensusAnalytics:
    """Analytics for NEBULA consensus health and performance."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  consensus_metrics: 'ConsensusMetrics'):
        self._bc  = blockchain
        self._cm  = consensus_metrics

    def hash_rate_estimate(self) -> float:
        h    = self._bc.height
        bits = self._bc.tip.header.bits
        diff = MAX_TARGET / max(1, bits_to_target(bits))
        return diff * (2**32) / TARGET_BLOCK_TIME

    def security_score(self) -> dict:
        hr        = self.hash_rate_estimate()
        diff      = MAX_TARGET / max(1, bits_to_target(
            self._bc.tip.header.bits))
        health    = self._cm.consensus_health()
        score     = min(100, int(diff / 1000 + 50))
        return {
            "hash_rate_th":   f"{hr/1e12:.2f} TH/s (est)",
            "difficulty":     f"{diff:.2f}",
            "score":          score,
            "health":         health.get("health", "UNKNOWN"),
            "avg_block_time": health.get("avg_block_time_s", "N/A"),
        }

    def uncle_rate(self) -> float:
        return self._cm._orphan_count / max(1, self._bc.height)


# ---- WalletAnalytics
class WalletAnalytics:
    """Advanced wallet analytics for NEBULA addresses."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def portfolio_health(self, address: str) -> dict:
        bal   = self._bc.utxo.balance(address)
        utxos = self._bc.utxo.get_by_address(address)  # FIX
        score = 0
        tips  = []
        if bal >= 100 * 10**DECIMALS:
            score += 30
        else:
            tips.append("Accumulate at least 100 NBL for basic staking")
        if len(utxos) <= 10:
            score += 20
        else:
            tips.append("Consolidate UTXOs to reduce fees")
        if bal >= 10_000 * 10**DECIMALS:
            score += 50
            tips.append("Consider locking for governance with veNBL")
        return {
            "address":      address,
            "health_score": score,
            "utxo_count":   len(utxos),
            "balance_nbl":  f"{bal/10**DECIMALS:.9f}",
            "tips":         tips,
        }

    def spending_pattern(self, address: str) -> dict:
        mp_txs = [tx for tx in self._bc.mempool._txs.values()
                  if any(out.address == address for out in tx.outputs)]
        return {
            "pending_inbound": len(mp_txs),
            "analysis":        "Pattern analysis requires full indexer",
        }


# ---- YieldFarmV3
class YieldFarmV3:
    """Yield farming v3 with dynamic emission schedules."""

    def __init__(self, farm_id: str, lp_token: str,
                  total_rewards: int, duration_blocks: int,
                  blockchain: 'NEBULABlockchain'):
        self.farm_id       = farm_id
        self.lp_token      = lp_token
        self.total_rewards = total_rewards
        self.duration      = duration_blocks
        self._bc           = blockchain
        self.start_block   = blockchain.height
        self._stakers:     Dict[str, dict] = {}
        self._total_lp     = 0

    def rewards_per_block(self) -> int:
        elapsed = self._bc.height - self.start_block
        if elapsed >= self.duration:
            return 0
        # Decaying emission: more rewards early
        remaining = self.duration - elapsed
        return int(self.total_rewards * 2 / (self.duration * (self.duration + 1))
                   * remaining)

    def stake(self, user: str, lp_amount: int) -> bool:
        self._stakers[user] = {
            "amount":   self._stakers.get(user, {}).get("amount", 0) + lp_amount,
            "entry":    self._bc.height,
            "pending":  0,
        }
        self._total_lp += lp_amount
        return True

    def unstake(self, user: str) -> Tuple[int, int]:
        info   = self._stakers.pop(user, {})
        amount = info.get("amount", 0)
        self._total_lp = max(0, self._total_lp - amount)
        # Calculate reward
        blocks = self._bc.height - info.get("entry", self._bc.height)
        rpb    = self.rewards_per_block()
        share  = amount / max(1, self._total_lp + amount)
        reward = int(rpb * blocks * share)
        return amount, reward

    def farm_info(self) -> dict:
        elapsed = self._bc.height - self.start_block
        pct     = min(100, elapsed / max(1, self.duration) * 100)
        return {
            "farm_id":    self.farm_id,
            "lp_token":   self.lp_token,
            "stakers":    len(self._stakers),
            "total_lp":   self._total_lp,
            "progress":   f"{pct:.1f}%",
            "rpb":        self.rewards_per_block(),
        }


# ---- YieldFarmRegistryV3
class YieldFarmRegistryV3:
    """Registry of v3 yield farms."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._farms: Dict[str, YieldFarmV3] = {}
        self._lock  = threading.RLock()

    def create_farm(self, lp_token: str,
                     total_rewards_nbl: float,
                     duration_days: int) -> str:
        with self._lock:
            fid = hashlib.sha256(
                f"FARMV3:{lp_token}:{time.time()}".encode()
            ).hexdigest()[:10]
            self._farms[fid] = YieldFarmV3(
                fid, lp_token,
                int(total_rewards_nbl * 10**DECIMALS),
                duration_days * 144,
                self._bc
            )
            return fid

    def stake(self, farm_id: str, user: str,
               lp_amount: int) -> Tuple[bool, str]:
        with self._lock:
            farm = self._farms.get(farm_id)
            if not farm:
                return False, "Farm not found"
            farm.stake(user, lp_amount)
            return True, f"Staked {lp_amount} LP in farm {farm_id}"

    def all_farms(self) -> List[dict]:
        return [f.farm_info() for f in self._farms.values()]


# ---- DeFiSafetyModule
class DeFiSafetyModule:
    """
    Safety module for NEBULA DeFi — circuit breakers and limits.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._circuit_open: Dict[str, bool] = {}
        self._daily_limits: Dict[str, int]  = {}
        self._daily_usage:  Dict[str, int]  = {}
        self._lock         = threading.RLock()

    def set_circuit_breaker(self, protocol: str,
                             threshold_pct: float = 0.20):
        with self._lock:
            self._circuit_open[protocol] = False

    def check_circuit(self, protocol: str) -> Tuple[bool, str]:
        if self._circuit_open.get(protocol, False):
            return False, f"Circuit breaker OPEN for {protocol}"
        return True, "OK"

    def trip_breaker(self, protocol: str, reason: str):
        with self._lock:
            self._circuit_open[protocol] = True

    def reset_breaker(self, guardian: str, protocol: str) -> bool:
        with self._lock:
            if protocol in self._circuit_open:
                self._circuit_open[protocol] = False
                return True
            return False

    def set_daily_limit(self, protocol: str, limit: int):
        with self._lock:
            self._daily_limits[protocol] = limit
            self._daily_usage[protocol]  = 0

    def check_and_use(self, protocol: str, amount: int) -> Tuple[bool, str]:
        with self._lock:
            limit = self._daily_limits.get(protocol)
            if limit is None:
                return True, "No limit"
            used  = self._daily_usage.get(protocol, 0)
            if used + amount > limit:
                return False, f"Daily limit reached: {limit/10**DECIMALS:.0f} NBL"
            self._daily_usage[protocol] = used + amount
            return True, "OK"

    def safety_stats(self) -> dict:
        open_circuits = [k for k, v in self._circuit_open.items() if v]
        return {
            "protocols_monitored": len(self._circuit_open),
            "open_circuits":       open_circuits,
            "with_limits":         len(self._daily_limits),
        }


# ---- TreasuryDiversification
class TreasuryDiversification:
    """
    Manages diversification of NEBULA treasury holdings.
    Prevents over-concentration in any single asset.
    """

    TARGET_ALLOCATION = {
        "NBL":  0.50,
        "BTC":  0.20,
        "ETH":  0.15,
        "USDT": 0.10,
        "OTHER": 0.05,
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc       = blockchain
        self._oracle   = oracle
        self._holdings: Dict[str, float] = {k: 0.0
                                             for k in self.TARGET_ALLOCATION}

    def update_holdings(self, asset: str, amount: float):
        self._holdings[asset] = self._holdings.get(asset, 0) + amount

    def allocation_drift(self) -> Dict[str, dict]:
        total = sum(self._holdings.values()) or 1
        drift = {}
        for asset, target in self.TARGET_ALLOCATION.items():
            actual = self._holdings.get(asset, 0) / total
            diff   = actual - target
            drift[asset] = {
                "target":  f"{target*100:.0f}%",
                "actual":  f"{actual*100:.1f}%",
                "drift":   f"{diff*100:+.1f}%",
                "action":  "reduce" if diff > 0.05 else
                            "increase" if diff < -0.05 else "hold",
            }
        return drift

    def rebalance_trades(self) -> List[dict]:
        total   = sum(self._holdings.values()) or 1
        trades  = []
        for asset, target in self.TARGET_ALLOCATION.items():
            actual    = self._holdings.get(asset, 0) / total
            diff      = target - actual
            if abs(diff) > 0.03:
                trades.append({
                    "asset":  asset,
                    "action": "buy" if diff > 0 else "sell",
                    "pct":    f"{abs(diff)*100:.1f}%",
                })
        return trades


# ---- GovernanceForumV2
class GovernanceForumV2:
    """Enhanced governance forum v2 with reputation and moderation."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._posts:   List[dict] = []
        self._tags:    Dict[str, List[int]] = {}
        self._reputation: Dict[str, int]   = {}
        self._mods:    Set[str]            = set()
        self._lock     = threading.RLock()

    def create_post(self, author: str, title: str,
                     body: str, tags: List[str] = None) -> int:
        with self._lock:
            post_id = len(self._posts)
            self._posts.append({
                "id":        post_id,
                "author":    author,
                "title":     title,
                "body":      body[:2000],
                "tags":      tags or [],
                "upvotes":   0,
                "downvotes": 0,
                "ts":        time.time(),
                "pinned":    False,
                "hidden":    False,
            })
            for tag in (tags or []):
                if tag not in self._tags:
                    self._tags[tag] = []
                self._tags[tag].append(post_id)
            self._reputation[author] = self._reputation.get(author, 0) + 1
            return post_id

    def upvote(self, voter: str, post_id: int):
        with self._lock:
            if post_id < len(self._posts):
                self._posts[post_id]["upvotes"] += 1
                author = self._posts[post_id]["author"]
                self._reputation[author] = (
                    self._reputation.get(author, 0) + 1)

    def pin(self, mod: str, post_id: int) -> bool:
        with self._lock:
            if mod not in self._mods:
                return False
            if post_id < len(self._posts):
                self._posts[post_id]["pinned"] = True
                return True
            return False

    def add_moderator(self, mod: str):
        self._mods.add(mod)

    def hot_posts(self, n: int = 10) -> List[dict]:
        with self._lock:
            posts = [p for p in self._posts if not p["hidden"]]
        return sorted(posts,
                      key=lambda p: p["upvotes"] - p["downvotes"],
                      reverse=True)[:n]

    def forum_v2_stats(self) -> dict:
        with self._lock:
            total_votes = sum(p["upvotes"] for p in self._posts)
        return {
            "posts":       len(self._posts),
            "total_votes": total_votes,
            "moderators":  len(self._mods),
            "tags":        len(self._tags),
        }


# ---- NFTAuction
class NFTAuction:
    """NFT auction with time-based bidding."""

    def __init__(self, auction_id: str, collection_id: str,
                  token_id: int, seller: str,
                  reserve_price: int, duration_blocks: int,
                  blockchain: 'NEBULABlockchain'):
        self.auction_id    = auction_id
        self.collection_id = collection_id
        self.token_id      = token_id
        self.seller        = seller
        self.reserve_price = reserve_price
        self.end_block     = blockchain.height + duration_blocks
        self._bc           = blockchain
        self.bids:         List[Tuple[str, int]] = []
        self.settled       = False

    @property
    def highest_bid(self) -> Tuple[Optional[str], int]:
        if not self.bids:
            return None, 0
        return max(self.bids, key=lambda b: b[1])

    def place_bid(self, bidder: str, amount: int) -> Tuple[bool, str]:
        if self._bc.height > self.end_block:
            return False, "Auction ended"
        _, current_high = self.highest_bid
        if amount <= current_high:
            return False, f"Bid must exceed {current_high}"
        if amount < self.reserve_price:
            return False, f"Below reserve: {self.reserve_price}"
        self.bids.append((bidder, amount))
        return True, f"Bid placed: {amount/10**DECIMALS:.6f} NBL"

    def settle(self) -> Tuple[bool, dict]:
        if self.settled:
            return False, {}
        if self._bc.height < self.end_block:
            return False, {}
        winner, amount = self.highest_bid
        self.settled = True
        return True, {
            "winner":   winner,
            "amount":   amount,
            "token_id": self.token_id,
        }


# ---- NFTMarketplaceV3
class NFTMarketplaceV3:
    """NFT Marketplace v3 with auctions, offers, bundles."""

    def __init__(self, nft: 'NBL721Registry',
                  blockchain: 'NEBULABlockchain'):
        self._nft     = nft
        self._bc      = blockchain
        self._auctions: Dict[str, NFTAuction] = {}
        self._offers:   Dict[str, dict]       = {}
        self._lock     = threading.RLock()

    def create_auction(self, seller: str, collection_id: str,
                        token_id: int, reserve_nbl: float,
                        duration_days: int) -> str:
        with self._lock:
            aid = hashlib.sha256(
                f"AUCT3:{seller}:{collection_id}:{token_id}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._auctions[aid] = NFTAuction(
                aid, collection_id, token_id, seller,
                int(reserve_nbl * 10**DECIMALS),
                duration_days * 144, self._bc)
            return aid

    def bid(self, auction_id: str, bidder: str,
             amount_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            auc = self._auctions.get(auction_id)
            if not auc:
                return False, "Auction not found"
            return auc.place_bid(bidder, int(amount_nbl * 10**DECIMALS))

    def settle_auction(self, auction_id: str) -> Tuple[bool, dict]:
        with self._lock:
            auc = self._auctions.get(auction_id)
            if not auc:
                return False, {}
            return auc.settle()

    def marketplace_v3_stats(self) -> dict:
        with self._lock:
            active = sum(1 for a in self._auctions.values()
                         if not a.settled and
                         self._bc.height <= a.end_block)
        return {
            "total_auctions": len(self._auctions),
            "active":         active,
            "total_offers":   len(self._offers),
        }


# ---- StakingInsurancePoolV2
class StakingInsurancePoolV2:
    """
    Decentralized staking insurance pool v2.
    Underwriters earn premium, pay claims on slash events.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._underwriters: Dict[str, int] = {}
        self._policies:   Dict[str, dict] = {}
        self._pool:       int = 0
        self._total_premium = 0
        self._lock = threading.RLock()

    def underwrite(self, underwriter: str,
                    amount: int) -> bool:
        with self._lock:
            if self._bc.utxo.balance(underwriter) < amount:
                return False
            self._underwriters[underwriter] = (
                self._underwriters.get(underwriter, 0) + amount)
            self._pool += amount
            return True

    def insure(self, staker: str, staked: int,
                premium_rate: float = 0.01) -> str:
        with self._lock:
            premium = int(staked * premium_rate)
            policy_id = hashlib.sha256(
                f"SIP2:{staker}:{staked}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._policies[policy_id] = {
                "staker":  staker,
                "staked":  staked,
                "premium": premium,
                "coverage": int(staked * 0.80),
                "active":  True,
            }
            self._total_premium += premium
            return policy_id

    def claim(self, policy_id: str,
               slashed: int) -> Tuple[bool, int]:
        with self._lock:
            pol = self._policies.get(policy_id)
            if not pol or not pol["active"]:
                return False, 0
            payout = min(pol["coverage"], slashed, self._pool)
            self._pool -= payout
            pol["active"] = False
            return True, payout

    def underwriter_share(self, underwriter: str) -> float:
        total = sum(self._underwriters.values()) or 1
        return self._underwriters.get(underwriter, 0) / total

    def pool_stats(self) -> dict:
        return {
            "pool_nbl":        f"{self._pool/10**DECIMALS:.3f}",
            "underwriters":    len(self._underwriters),
            "policies":        len(self._policies),
            "total_premium":   f"{self._total_premium/10**DECIMALS:.6f}",
        }


# ---- ChainPruning
class ChainPruning:
    """
    Selective chain pruning for NEBULA nodes.
    Prunes spent UTXOs and old block data to save storage.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc           = blockchain
        self._pruned_blocks = 0
        self._pruned_utxos  = 0
        self._lock          = threading.RLock()

    def prune_spent_utxos(self) -> int:
        """Remove spent UTXOs from the UTXO set."""
        with self._lock:
            before = self._bc.utxo.size()
            empty  = [addr for addr in list(self._bc.utxo._addr_idx.keys())
                      if self._bc.utxo.balance(addr) == 0]
            for addr in empty:
                self._bc.utxo._addr_idx.pop(addr, None)
            pruned = before - self._bc.utxo.size()
            self._pruned_utxos += pruned
            return pruned

    def prune_blocks_before(self, height: int) -> int:
        """Prune block data before a given height (full node keeps headers)."""
        return 0   # Simplified: just log intent

    def pruning_stats(self) -> dict:
        return {
            "pruned_utxos":  self._pruned_utxos,
            "pruned_blocks": self._pruned_blocks,
            "current_utxos": self._bc.utxo.size(),
            "mode":          "full (no pruning)" if self._pruned_blocks == 0 else "pruned",
        }


# ---- ExtendedTestSuiteV2
class ExtendedTestSuiteV2:
    """Second extended test suite covering advanced modules."""

    def __init__(self):
        self.passed  = 0
        self.failed  = 0
        self.results = []

    def _ok(self, name: str, detail: str = ""):
        self.passed += 1
        self.results.append({"test": name, "status": "PASS"})
        print(f"  ✅ {name}" + (f" — {detail}" if detail else ""))

    def _fail(self, name: str, err: str):
        self.failed += 1
        self.results.append({"test": name, "status": "FAIL", "err": err})
        print(f"  ❌ {name}: {err}")

    def test_zk_rollup(self):
        print("\n🔐 ZK Rollup")
        try:
            bc      = NEBULABlockchain()
            rollup  = ZKRollupLayer(bc)
            for i in range(10):
                rollup.submit_l2_tx({"txid": f"l2tx{i}", "amount": i*100})
            bid = rollup.force_batch()
            assert bid is not None
            self._ok("ZK batch created", f"batch #{bid}")
            ok = rollup.verify_batch(bid)
            assert ok
            self._ok("ZK batch verified")
        except Exception as e:
            self._fail("ZK rollup", str(e))

    def test_options_pricing(self):
        print("\n📊 Options Pricing")
        try:
            bc  = NEBULABlockchain()
            opt = OptionsProtocolV2(bc)
            p   = opt.price_option("NBL", 0.01, 30, call=True)
            assert "bs_price" in p
            self._ok("Black-Scholes call pricing", p["bs_price"])
            p2  = opt.price_option("NBL", 0.01, 30, call=False)
            self._ok("Black-Scholes put pricing", p2["bs_price"])
        except Exception as e:
            self._fail("Options pricing", str(e))

    def test_concentrated_liquidity(self):
        print("\n💧 CLMM Pool")
        try:
            bc   = NEBULABlockchain()
            dex  = AdvancedDEXV2(bc)
            pid  = dex.create_pool("NBL", "USDT", 0.003)
            assert pid
            ok, pos_id = dex.add_liquidity(pid, FOUNDATION_ADDRESS,
                                            -1000, 1000, 10_000)
            assert ok, pos_id
            self._ok("CLMM pool created and funded", pos_id[:8])
            ok2, out = dex.swap(pid, FOUNDATION_ADDRESS, "NBL", 100.0)
            self._ok("CLMM swap executed")
        except Exception as e:
            self._fail("CLMM pool", str(e))

    def test_staking_v4(self):
        print("\n🔒 Staking v4")
        try:
            bc  = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 50_000)
            ok, msg = stk.stake_flexible(FOUNDATION_ADDRESS,
                                          1000 * 10**DECIMALS)
            assert ok, msg
            self._ok("Flexible staking", msg)
            ok2, shares = stk.stake_liquid(FOUNDATION_ADDRESS,
                                            500 * 10**DECIMALS)
            assert ok2
            self._ok("Liquid staking (stNBL)", f"{shares/10**DECIMALS:.4f} stNBL")
        except Exception as e:
            self._fail("Staking v4", str(e))

    def test_governance_v3(self):
        print("\n🗳️  Governance v3")
        try:
            bc  = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 10_000)
            gov = GovernanceV3(bc)
            gov.add_guardian(FOUNDATION_ADDRESS)
            pid = gov.propose(FOUNDATION_ADDRESS, "Test Upgrade v3",
                               [{"action": "update_param", "value": 100}])
            ok, msg = gov.vote(FOUNDATION_ADDRESS, pid, True)
            assert ok, msg
            self._ok("Governance v3 vote", msg)
        except Exception as e:
            self._fail("Governance v3", str(e))

    def test_synthetic_assets(self):
        print("\n📈 Synthetic Assets")
        try:
            bc   = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 100_000)
            ora  = OracleV2(bc)
            ora.update_price("TSLA/USD", 200.0, FOUNDATION_ADDRESS)
            ora.update_price("NBL/USD", 0.01, FOUNDATION_ADDRESS)
            synth = SyntheticAssetProtocol(bc, ora)
            ok, msg = synth.mint(FOUNDATION_ADDRESS, "sTSLA",
                                  1.0, 40_000.0)
            self._ok("Synthetic asset mint attempt", msg)
        except Exception as e:
            self._fail("Synthetic assets", str(e))

    def test_nft_auction(self):
        print("\n🎨 NFT Auction v3")
        try:
            bc  = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 50_000)
            nft = NBL721Registry()
            cid = nft.create_collection(FOUNDATION_ADDRESS, "AuctionNFT",
                                         "ANFT", "Test", 10, 0.0)
            tid, _ = nft.mint(cid, FOUNDATION_ADDRESS, "ipfs://test",
                               {"name": "Auction Item"}, FOUNDATION_ADDRESS)
            mkt = NFTMarketplaceV3(nft, bc)
            aid = mkt.create_auction(FOUNDATION_ADDRESS, cid, tid, 100.0, 7)
            w2  = NEBULAWallet.generate()
            bc.fund_address(w2.first_address, 1_000)
            ok, msg = mkt.bid(aid, w2.first_address, 150.0)
            self._ok("NFT auction bid", msg)
        except Exception as e:
            self._fail("NFT auction", str(e))

    def run_all(self) -> dict:
        print("\n" + "═"*55)
        print("  🧪 NEBULA EXTENDED TEST SUITE v2")
        print("═"*55)
        import time as _t; start = _t.time()
        self.test_zk_rollup()
        self.test_options_pricing()
        self.test_concentrated_liquidity()
        self.test_staking_v4()
        self.test_governance_v3()
        self.test_synthetic_assets()
        self.test_nft_auction()
        elapsed = _t.time() - start
        total   = self.passed + self.failed
        pct     = self.passed / total * 100 if total > 0 else 0
        print(f"\n{'═'*55}")
        print(f"  Extended v2: {self.passed}/{total} passed ({pct:.0f}%)")
        print(f"  Time: {elapsed:.2f}s")
        print(f"{'═'*55}\n")
        return {"passed": self.passed, "failed": self.failed}


# ---- BlockTemplateV2
class BlockTemplateV2:
    """Enhanced block template with miner hints and priority."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  miner: str):
        self._bc    = blockchain
        self._miner = miner

    def build_template(self, max_size: int = MAX_BLOCK_SIZE_BYTES) -> dict:
        bc     = self._bc
        height = bc.height + 1
        reward = mining_reward(height)
        foundation = int(reward * FOUNDATION_RATE)
        miner_r    = reward - foundation
        # Select highest-fee transactions
        txs = sorted(
            bc.mempool._txs.values(),
            key=lambda tx: tx.byte_size(),
            reverse=False
        )[:MAX_TX_PER_BLOCK - 1]
        txids      = [tx.txid for tx in txs]
        fee_total  = sum(tx.total_output() for tx in txs
                         if not tx.coinbase_data)
        merkle     = MerkleTree.compute_root(txids) if txids else "0"*64
        bits       = calculate_next_bits(bc)
        target     = bits_to_target(bits)
        return {
            "height":          height,
            "prev_hash":       bc.tip.hash,
            "merkle_root":     merkle,
            "bits":            bits,
            "target":          hex(target),
            "timestamp":       int(time.time()),
            "tx_count":        len(txids) + 1,
            "coinbase_value":  miner_r,
            "foundation_fee":  foundation,
            "tx_fees":         fee_total,
            "miner":           self._miner,
            "txids":           txids[:10],
        }

    def submit_solution(self, nonce: int,
                         extra_nonce: int = 0) -> Optional['Block']:
        tmpl   = self.build_template()
        header = BlockHeader(
            version      = 1,
            prev_hash    = tmpl["prev_hash"],
            merkle_root  = tmpl["merkle_root"],
            timestamp    = tmpl["timestamp"],
            bits         = tmpl["bits"],
            nonce        = nonce,
        )
        if int(header.hash, 16) <= bits_to_target(tmpl["bits"]):
            # Valid solution
            cb_tx = Transaction(
                version = 1,
                inputs  = [],
                outputs = [TransactionOutput(
                    value   = tmpl["coinbase_value"],
                    address = self._miner,
                    script  = P2PKHScript.lock(self._miner),
                )],
            )
            blk = _mk_block(header, [cb_tx], tmpl["height"])
            return blk
        return None


# ---- SwapAggregatorV2
class SwapAggregatorV2:
    """
    Swap aggregator v2 — finds best price across all venues.
    Supports multi-hop routing.
    """

    def __init__(self, dex: 'NEBULADex',
                  dex_v3: 'DEXv3' = None,
                  oracle: 'OracleV2' = None):
        self._dex    = dex
        self._dex_v3 = dex_v3
        self._oracle = oracle
        self._swaps: List[dict] = []

    def quote_all(self, token_in: str, token_out: str,
                   amount_in: float) -> List[dict]:
        """Get quotes from all available venues."""
        quotes   = []
        amt_raw  = int(amount_in * 10**DECIMALS)
        # AMM quote
        amm_out  = self._dex.quote_amm(token_in, token_out, amt_raw)
        if amm_out > 0:
            quotes.append({
                "venue":    "AMM",
                "out":      amm_out / 10**DECIMALS,
                "price":    amm_out / max(1, amt_raw),
                "slippage": f"{price_impact(amount_in, 10000, 10000):.3f}%",
            })
        # Oracle-based estimate
        if self._oracle:
            in_usd  = (self._oracle.price(f"{token_in}/USD") or 0.01) * amount_in
            out_usd = self._oracle.price(f"{token_out}/USD") or 1.0
            oracle_out = in_usd / out_usd if out_usd > 0 else 0
            if oracle_out > 0:
                quotes.append({
                    "venue":    "Oracle",
                    "out":      oracle_out,
                    "price":    oracle_out / amount_in if amount_in > 0 else 0,
                    "slippage": "N/A",
                })
        return sorted(quotes, key=lambda q: -q["out"])

    def best_swap(self, trader: str, token_in: str,
                   token_out: str, amount_in: float) -> Tuple[bool, str, float]:
        quotes = self.quote_all(token_in, token_out, amount_in)
        if not quotes:
            return False, "No liquidity", 0.0
        best = quotes[0]
        # Execute via best venue
        if best["venue"] == "AMM":
            ok, msg, out = self._dex.swap_amm(
                trader, token_in, token_out,
                int(amount_in * 10**DECIMALS))
            if ok:
                self._swaps.append({
                    "trader":  trader,
                    "in":      token_in,
                    "out":     token_out,
                    "amount":  amount_in,
                    "venue":   "AMM",
                })
            return ok, msg, out / 10**DECIMALS
        return False, "Best venue unavailable", 0.0

    def aggregator_v2_stats(self) -> dict:
        return {
            "swaps_routed": len(self._swaps),
            "venues":       ["AMM", "Oracle"],
        }


# ---- NFTRoyaltyDAO
class NFTRoyaltyDAO:
    """
    DAO governing NFT royalty rates and distribution.
    NFT holders vote on royalty parameters.
    """

    DEFAULT_ROYALTY = 0.05

    def __init__(self, blockchain: 'NEBULABlockchain',
                  nft: 'NBL721Registry'):
        self._bc         = blockchain
        self._nft        = nft
        self._royalties: Dict[str, float] = {}
        self._proposals: List[dict]       = []
        self._lock       = threading.RLock()

    def propose_rate_change(self, proposer: str,
                             collection_id: str,
                             new_rate: float) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"ROYALTYDAO:{collection_id}:{new_rate}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._proposals.append({
                "id":          pid,
                "collection":  collection_id,
                "new_rate":    new_rate,
                "proposer":    proposer,
                "votes":       0.0,
                "status":      "voting",
            })
            return pid

    def vote(self, voter: str, proposal_id: str,
              support: bool) -> bool:
        with self._lock:
            p = next((p for p in self._proposals
                      if p["id"] == proposal_id), None)
            if not p or p["status"] != "voting":
                return False
            weight = self._bc.utxo.balance(voter) / 10**DECIMALS
            p["votes"] += weight if support else -weight
            if abs(p["votes"]) >= 10_000:
                if p["votes"] > 0:
                    self._royalties[p["collection"]] = p["new_rate"]
                    p["status"] = "passed"
                else:
                    p["status"] = "rejected"
            return True

    def get_royalty_rate(self, collection_id: str) -> float:
        return self._royalties.get(collection_id, self.DEFAULT_ROYALTY)

    def dao_stats(self) -> dict:
        return {
            "managed_collections": len(self._royalties),
            "proposals":           len(self._proposals),
        }


# ---- PredictionOracle
class PredictionOracle:
    """
    Oracle that aggregates prediction market probabilities.
    Uses wisdom-of-crowd for price forecasting.
    """

    def __init__(self, oracle: 'OracleV2'):
        self._oracle     = oracle
        self._predictions: Dict[str, List[dict]] = {}
        self._resolved:    Dict[str, float]      = {}

    def submit_prediction(self, predictor: str, pair: str,
                           target_price: float, target_date: str,
                           confidence: float = 0.5):
        if pair not in self._predictions:
            self._predictions[pair] = []
        self._predictions[pair].append({
            "predictor":   predictor,
            "target":      target_price,
            "date":        target_date,
            "confidence":  confidence,
            "ts":          time.time(),
        })

    def consensus_forecast(self, pair: str) -> dict:
        preds = self._predictions.get(pair, [])
        if not preds:
            current = self._oracle.price(pair) or 0
            return {"pair": pair, "forecast": current, "consensus": "low"}
        prices  = [p["target"] * p["confidence"] for p in preds]
        weights = [p["confidence"] for p in preds]
        total_w = sum(weights) or 1
        forecast = sum(prices) / total_w
        return {
            "pair":        pair,
            "forecast":    f"${forecast:.6f}",
            "current":     f"${self._oracle.price(pair) or 0:.6f}",
            "predictors":  len(preds),
            "consensus":   "high" if len(preds) > 5 else "medium",
        }

    def accuracy_score(self, predictor: str) -> dict:
        total  = 0
        errors = 0
        for pair, preds in self._predictions.items():
            actual = self._oracle.price(pair) or 0
            for p in preds:
                if p["predictor"] == predictor and actual > 0:
                    err = abs(p["target"] - actual) / actual
                    errors += err
                    total  += 1
        mae = errors / total if total > 0 else None
        return {
            "predictor": predictor,
            "predictions": total,
            "mae": f"{mae*100:.2f}%" if mae else "N/A",
        }
