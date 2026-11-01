"""NEBULA group29 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. LNChannelGraph  (orig. lines 48013-48059)
   2. LightningRouter  (orig. lines 48061-48161)
   3. WhaleAlert  (orig. lines 48175-48194)
   4. WhaleTracker  (orig. lines 48196-48242)
   5. NetworkHealthIndex  (orig. lines 48244-48321)
   6. ExchangeFlowAnalyzer  (orig. lines 48323-48371)
   7. RollupBatch  (orig. lines 48384-48409)
   8. ZKRollupState  (orig. lines 48411-48451)
   9. ZKProver  (orig. lines 48453-48481)
  10. ZKRollupOperator  (orig. lines 48483-48578)
  11. MMConfig  (orig. lines 48591-48600)
  12. MMInventory  (orig. lines 48602-48615)
  13. MarketMakerBot  (orig. lines 48617-48747)
  14. ConsensusParams  (orig. lines 48762-48789)
  15. DifficultyCLI  (orig. lines 48791-48851)
  16. ConsensusManager  (orig. lines 48853-48911)
  17. ExplorerV2Handler  (orig. lines 48925-49043)
  18. BlockExplorerV2  (orig. lines 49045-49074)
  19. SimulationResult  (orig. lines 49087-49104)
  20. TxSimulator  (orig. lines 49106-49207)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): ChannelGraph, LNEdge, MockBlockchain
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

MAX_SUPPLY          = 21_000_000 * (10 ** DECIMALS)   # in Neb  (matches 50 NBL * 210,000 blocks * 2 geometric series)

FOUNDATION_RATE        = 0.02          # 2% per block to foundation

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

DIFFICULTY_WINDOW      = 2016                           # blocks per retarget

INITIAL_BITS           = 0x1e0fffff if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d0fffff   # [v10.24]

MAX_BLOCK_SIZE_BYTES   = 1_048_576                      # 1 MB

MAX_TX_PER_BLOCK       = 3000

COINBASE_MATURITY      = 100                            # blocks before coinbase spendable

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

DUST_THRESHOLD         = 546                            # min output amount in Neb

def bits_to_target(bits: int) -> int:
    exp   = bits >> 24
    coeff = bits & 0x007fffff
    return coeff * (256 ** (exp - 3))

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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- LNChannelGraph
class LNChannelGraph:
    """Lightning Network channel graph"""

    def __init__(self):
        self._edges     : Dict[str, LNEdge] = {}
        self._adj       : Dict[str, List[str]] = {}
        self._lock      = threading.RLock()

    def add_channel(self, edge: LNEdge):
        with self._lock:
            self._edges[edge.channel_id] = edge
            self._adj.setdefault(edge.node_a, []).append(edge.channel_id)
            self._adj.setdefault(edge.node_b, []).append(edge.channel_id)

    def remove_channel(self, channel_id: str):
        with self._lock:
            edge = self._edges.pop(channel_id, None)
            if edge:
                self._adj.get(edge.node_a, []).remove(channel_id)
                self._adj.get(edge.node_b, []).remove(channel_id)

    def neighbors(self, node: str) -> List[Tuple[str, LNEdge]]:
        """Get neighbors (node_id, edge) for a node"""
        with self._lock:
            result = []
            for cid in self._adj.get(node, []):
                edge = self._edges.get(cid)
                if edge and edge.is_active:
                    neighbor = edge.node_b if edge.node_a == node else edge.node_a
                    result.append((neighbor, edge))
            return result

    def node_count(self) -> int:
        return len(self._adj)

    def channel_count(self) -> int:
        return len(self._edges)

    def stats(self) -> dict:
        with self._lock:
            caps = [e.capacity for e in self._edges.values()]
            return {
                "nodes"          : len(self._adj),
                "channels"       : len(self._edges),
                "total_capacity" : sum(caps) / 10**DECIMALS,
                "avg_capacity"   : (sum(caps)//max(1,len(caps))) / 10**DECIMALS,
            }


# ---- LightningRouter
class LightningRouter:
    """
    Lightning Network pathfinder with fee optimization.
    Uses Dijkstra's algorithm with fee-weighted edges.
    Supports: multi-path payments (MPP), fee minimization.
    """

    MAX_HOPS = 20
    MAX_FEE_PCT = 1.0   # max 1% fee

    def __init__(self, graph: ChannelGraph):
        self.graph = graph

    def find_route(self, source: str, dest: str,
                    amount_msat: int,
                    max_fee_pct: float = None) -> Optional[List[LNEdge]]:
        """
        Find lowest-fee route from source to dest.
        Returns list of edges (hops) or None if no route.
        """
        max_fee = int(amount_msat * (max_fee_pct or self.MAX_FEE_PCT) / 100)

        # Dijkstra: (total_fee, hops, node, path)
        heap     = [(0, 0, source, [])]
        visited  : Set[str] = set()

        while heap:
            fee, hops, node, path = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)

            if node == dest:
                return path

            if hops >= self.MAX_HOPS:
                continue
            if fee > max_fee:
                continue

            for neighbor, edge in self.graph.neighbors(node):
                if neighbor not in visited and edge.can_route(amount_msat):
                    edge_fee = edge.fee_for_amount(amount_msat)
                    heapq.heappush(heap, (
                        fee + edge_fee,
                        hops + 1,
                        neighbor,
                        path + [edge]
                    ))

        return None   # No route found

    def find_multi_path(self, source: str, dest: str,
                         amount_msat: int,
                         n_paths: int = 3) -> List[List[LNEdge]]:
        """
        Multi-path payment (MPP) routing.
        Splits payment across multiple paths for better success.
        """
        paths    = []
        per_part = amount_msat // n_paths

        for _ in range(n_paths):
            route = self.find_route(source, dest, per_part)
            if route:
                paths.append(route)

        return paths

    def calculate_route_fee(self, route: List[LNEdge],
                              amount_msat: int) -> int:
        """Calculate total fee for a route"""
        total_fee = 0
        remaining = amount_msat
        for edge in reversed(route[:-1]):   # last hop is free
            total_fee += edge.fee_for_amount(remaining)
            remaining  = amount_msat + total_fee   # amount increases as we go back
        return total_fee

    def estimate_success_prob(self, route: List[LNEdge],
                               amount_msat: int) -> float:
        """Estimate probability of payment success"""
        prob = 1.0
        for edge in route:
            # Each hop: probability based on capacity vs amount
            cap_ratio = min(1.0, edge.capacity * 1000 / max(1, amount_msat))
            prob     *= 0.85 * cap_ratio   # simplified
        return round(prob, 4)

    def route_summary(self, route: List[LNEdge],
                       amount_msat: int) -> dict:
        fee = self.calculate_route_fee(route, amount_msat)
        return {
            "hops"           : len(route),
            "amount_msat"    : amount_msat,
            "total_fee_msat" : fee,
            "fee_pct"        : f"{fee/max(1,amount_msat)*100:.4f}%",
            "success_prob"   : self.estimate_success_prob(route, amount_msat),
            "path"           : [e.channel_id[:8] for e in route],
        }


# ---- WhaleAlert
@dataclass
class WhaleAlert:
    """Alert for large on-chain movement"""
    txid         : str
    amount_nbl   : float
    from_addr    : str
    to_addr      : str
    height       : int
    timestamp    : float = field(default_factory=time.time)
    category     : str   = "large_transfer"

    def to_dict(self) -> dict:
        return {
            "txid"      : self.txid[:16] + "...",
            "amount_nbl": f"{self.amount_nbl:.2f}",
            "from"      : self.from_addr[:16] + "...",
            "to"        : self.to_addr[:16] + "...",
            "height"    : self.height,
            "category"  : self.category,
        }


# ---- WhaleTracker
class WhaleTracker:
    """
    Track large NBL movements.
    Alerts when significant transactions occur.
    """

    MIN_WHALE_NBL = 1_000.0   # 1000 NBL minimum for whale alert

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc      = blockchain
        self._alerts : List[WhaleAlert] = []
        self._lock   = threading.Lock()

    def scan_block(self, block: 'Block'):
        """Scan block for whale movements"""
        for tx in block.transactions[1:]:   # skip coinbase
            total_out = tx.total_output() / 10**DECIMALS
            if total_out >= self.MIN_WHALE_NBL:
                from_addr = "unknown"
                to_addr   = (tx.outputs[0].address or "unknown"
                             if tx.outputs else "unknown")
                alert = WhaleAlert(
                    txid       = tx.txid,
                    amount_nbl = total_out,
                    from_addr  = from_addr,
                    to_addr    = to_addr,
                    height     = block.height,
                    category   = self._classify(total_out),
                )
                with self._lock:
                    self._alerts.append(alert)

    def _classify(self, amount: float) -> str:
        if amount >= 10_000:   return "mega_whale"
        if amount >= 1_000:    return "whale"
        if amount >= 100:      return "dolphin"
        return "fish"

    def recent_alerts(self, n: int = 20) -> List[dict]:
        with self._lock:
            return [a.to_dict() for a in self._alerts[-n:]]

    def total_whale_volume_24h(self) -> float:
        cutoff = time.time() - 86400
        with self._lock:
            return sum(a.amount_nbl for a in self._alerts
                       if a.timestamp >= cutoff)


# ---- NetworkHealthIndex
class NetworkHealthIndex:
    """
    Composite network health index (0-100).
    Weights: block time accuracy, hash rate stability,
    mempool size, active addresses, price stability.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 oracle: 'PriceOracle' = None):
        self.bc     = blockchain
        self.oracle = oracle
        self._history: List[Tuple[float, float]] = []

    def compute(self) -> dict:
        """Compute network health index"""
        score     = 100.0
        breakdown = {}

        # Block time score (max 25pts)
        chain = self.bc._chain
        if len(chain) >= 10:
            times = [chain[i].header.timestamp - chain[i-1].header.timestamp
                     for i in range(max(1,len(chain)-10), len(chain))]
            avg_bt  = statistics.mean(times) if times else TARGET_BLOCK_TIME
            dev_pct = abs(avg_bt - TARGET_BLOCK_TIME) / TARGET_BLOCK_TIME
            bt_score = max(0, 25 * (1 - dev_pct * 2))
        else:
            bt_score = 25
        breakdown["block_time"] = round(bt_score, 1)
        score    -= (25 - bt_score)

        # Mempool score (max 20pts)
        mp_size  = self.bc.mempool.size()
        mp_score = max(0, 20 * (1 - mp_size / 5000))
        breakdown["mempool"] = round(mp_score, 1)
        score   -= (20 - mp_score)

        # Supply health (max 20pts)
        issued   = self.bc.utxo.total_supply()
        pct_left = 1 - issued / MAX_SUPPLY
        s_score  = 20 * min(1.0, pct_left * 5)
        breakdown["supply"] = round(s_score, 1)
        score   -= (20 - s_score)

        # UTXO set health (max 20pts)
        utxo_score = min(20, 20 * self.bc.utxo.size() / max(1, 100))
        breakdown["utxo"] = round(utxo_score, 1)

        # Chain height (max 15pts)
        h_score = min(15, self.bc.height / 10)
        breakdown["height"] = round(h_score, 1)

        final = max(0, min(100, score))
        self._history.append((time.time(), final))
        if len(self._history) > 1440:
            self._history.pop(0)

        return {
            "index"        : round(final, 1),
            "grade"        : self._grade(final),
            "breakdown"    : breakdown,
            "trend"        : self._trend(),
        }

    def _grade(self, score: float) -> str:
        if score >= 90: return "A+"
        if score >= 80: return "A"
        if score >= 70: return "B"
        if score >= 60: return "C"
        if score >= 50: return "D"
        return "F"

    def _trend(self) -> str:
        if len(self._history) < 2: return "stable"
        recent = [v for _, v in self._history[-10:]]
        if recent[-1] > recent[0] + 2: return "improving"
        if recent[-1] < recent[0] - 2: return "declining"
        return "stable"


# ---- ExchangeFlowAnalyzer
class ExchangeFlowAnalyzer:
    """
    Analyze flows to/from exchanges.
    Exchange inflows = potential selling pressure.
    Exchange outflows = potential holding/accumulation.
    """

    KNOWN_EXCHANGES = {
        FOUNDATION_ADDRESS: "NEBULA Foundation",
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc = blockchain

    def classify_address(self, addr: str) -> str:
        """Classify an address as exchange/miner/whale/personal"""
        if addr in self.KNOWN_EXCHANGES:
            return f"Exchange: {self.KNOWN_EXCHANGES[addr]}"
        # Check if it's a miner (received coinbase)
        for blk in self.bc._chain:
            if blk.transactions:
                cb = blk.transactions[0]
                for out in cb.outputs:
                    if out.address == addr:
                        return "Miner"
        # Check balance for whale
        bal = self.bc.utxo.balance(addr) / 10**DECIMALS
        if bal >= 10_000: return "Mega Whale"
        if bal >= 1_000:  return "Whale"
        return "Personal"

    def exchange_flows_24h(self) -> dict:
        """Net exchange flows in last 24 hours"""
        cutoff = time.time() - 86400
        inflows  = 0
        outflows = 0
        for blk in self.bc._chain:
            if blk.header.timestamp < cutoff:
                continue
            for tx in blk.transactions[1:]:
                for out in tx.outputs:
                    if out.address in self.KNOWN_EXCHANGES:
                        inflows += out.value
        return {
            "inflows_nbl"  : inflows / 10**DECIMALS,
            "outflows_nbl" : outflows / 10**DECIMALS,
            "net_flow_nbl" : (inflows - outflows) / 10**DECIMALS,
            "pressure"     : "selling" if inflows > outflows else "buying",
        }


# ---- RollupBatch
@dataclass
class RollupBatch:
    """A batch of transactions to be rolled up"""
    batch_id       : str
    transactions   : List[dict]
    state_root_before: bytes
    state_root_after : bytes
    proof          : Optional[bytes]    = None
    height_posted  : Optional[int]      = None
    verified       : bool               = False
    created_at     : float = field(default_factory=time.time)

    @property
    def tx_count(self) -> int:
        return len(self.transactions)

    def to_dict(self) -> dict:
        return {
            "batch_id"    : self.batch_id,
            "tx_count"    : self.tx_count,
            "state_before": self.state_root_before.hex()[:16] + "...",
            "state_after" : self.state_root_after.hex()[:16] + "...",
            "has_proof"   : self.proof is not None,
            "verified"    : self.verified,
            "height"      : self.height_posted,
        }


# ---- ZKRollupState
class ZKRollupState:
    """State tree for ZK Rollup"""

    def __init__(self):
        self._balances : Dict[str, int] = {}
        self._nonces   : Dict[str, int] = {}
        self._version  = 0

    def get_balance(self, addr: str) -> int:
        return self._balances.get(addr, 0)

    def apply_transfer(self, from_addr: str, to_addr: str,
                        amount: int) -> bool:
        if self._balances.get(from_addr, 0) < amount:
            return False
        self._balances[from_addr] = self._balances.get(from_addr, 0) - amount
        self._balances[to_addr]   = self._balances.get(to_addr, 0) + amount
        self._nonces[from_addr]   = self._nonces.get(from_addr, 0) + 1
        return True

    def deposit(self, addr: str, amount: int):
        self._balances[addr] = self._balances.get(addr, 0) + amount

    def withdraw(self, addr: str, amount: int) -> bool:
        if self._balances.get(addr, 0) < amount:
            return False
        self._balances[addr] -= amount
        return True

    def state_root(self) -> bytes:
        """Compute Merkle root of current state"""
        items = sorted(
            f"{addr}:{bal}:{self._nonces.get(addr,0)}"
            for addr, bal in self._balances.items()
        )
        combined = hashlib.sha256("\n".join(items).encode()).digest()
        return combined

    @property
    def version(self) -> int:
        return self._version


# ---- ZKProver
class ZKProver:
    """
    Simplified ZK proof generation.
    Real implementation would use zk-SNARK/STARK library.
    This demonstrates the interface and data structures.
    """

    @staticmethod
    def generate_proof(state_before: bytes,
                        state_after: bytes,
                        transactions: List[dict]) -> bytes:
        """
        Generate validity proof for batch of transactions.
        Proof proves: given state_before and txs, state_after is correct.
        """
        # Simplified: hash everything together
        proof_input = (state_before + state_after +
                       hashlib.sha256(
                           str(transactions).encode()).digest())
        proof = hashlib.sha256(b"ZKP:" + proof_input).digest()
        # In production: use Groth16, PLONK, or STARK
        return proof

    @staticmethod
    def verify_proof(state_before: bytes, state_after: bytes,
                      transactions: List[dict], proof: bytes) -> bool:
        """Verify ZK proof"""
        expected = ZKProver.generate_proof(state_before, state_after, transactions)
        return proof == expected


# ---- ZKRollupOperator
class ZKRollupOperator:
    """
    ZK Rollup operator: batches transactions and posts proofs on-chain.
    Users can transact cheaply off-chain.
    Security: any invalid proof is rejected by L1 contract.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 max_batch_size: int = 1000):
        self.bc             = blockchain
        self.max_batch_size = max_batch_size
        self.l2_state       = ZKRollupState()
        self._pending_txs   : List[dict] = []
        self._batches       : List[RollupBatch] = []
        self._lock          = threading.RLock()
        self._total_gas_saved = 0

    def deposit(self, l1_addr: str, amount: int) -> bool:
        """Bridge NBL from L1 to L2"""
        l1_bal = self.bc.utxo.balance(l1_addr)
        if l1_bal < amount:
            return False
        self.l2_state.deposit(l1_addr, amount)
        return True

    def submit_tx(self, from_addr: str, to_addr: str,
                   amount: int, nonce: int) -> bool:
        """Submit L2 transaction"""
        tx = {
            "from"  : from_addr,
            "to"    : to_addr,
            "amount": amount,
            "nonce" : nonce,
        }
        with self._lock:
            self._pending_txs.append(tx)
            if len(self._pending_txs) >= self.max_batch_size:
                self._create_batch()
        return True

    def _create_batch(self):
        """Create and prove a batch"""
        if not self._pending_txs:
            return

        txs              = self._pending_txs[:self.max_batch_size]
        self._pending_txs = self._pending_txs[self.max_batch_size:]

        state_before = self.l2_state.state_root()

        # Apply transactions
        valid_txs = []
        for tx in txs:
            ok = self.l2_state.apply_transfer(
                tx["from"], tx["to"], tx["amount"])
            if ok:
                valid_txs.append(tx)

        state_after = self.l2_state.state_root()
        proof       = ZKProver.generate_proof(state_before, state_after, valid_txs)
        batch_id    = hashlib.sha256(proof).hexdigest()[:16]

        batch = RollupBatch(
            batch_id           = batch_id,
            transactions       = valid_txs,
            state_root_before  = state_before,
            state_root_after   = state_after,
            proof              = proof,
            verified           = ZKProver.verify_proof(
                                     state_before, state_after, valid_txs, proof),
            height_posted      = self.bc.height,
        )
        self._batches.append(batch)

        # Gas savings estimate: ~1 calldata byte per tx vs ~250 bytes L1
        self._total_gas_saved += len(valid_txs) * 250

    def flush(self) -> Optional[RollupBatch]:
        """Force flush pending txs into a batch"""
        with self._lock:
            if self._pending_txs:
                self._create_batch()
            return self._batches[-1] if self._batches else None

    def get_l2_balance(self, addr: str) -> float:
        return self.l2_state.get_balance(addr) / 10**DECIMALS

    def stats(self) -> dict:
        return {
            "l2_addresses"      : len(self.l2_state._balances),
            "pending_txs"       : len(self._pending_txs),
            "batches_posted"    : len(self._batches),
            "total_l2_txs"      : sum(b.tx_count for b in self._batches),
            "gas_saved_estimate": self._total_gas_saved,
            "verified_batches"  : sum(1 for b in self._batches if b.verified),
        }


# ---- MMConfig
@dataclass
class MMConfig:
    """Market maker configuration"""
    pair            : str
    spread_bps      : int   = 50      # 0.5% spread
    inventory_target: float = 0.5     # 50% of capital in base
    order_size_pct  : float = 0.05    # 5% of inventory per order
    max_position    : float = 10.0    # max position in NBL
    rebalance_every : int   = 10      # rebalance every N blocks
    min_profit_bps  : int   = 10      # min profit before trading


# ---- MMInventory
@dataclass
class MMInventory:
    """Market maker inventory tracking"""
    base_balance  : float = 0.0    # NBL
    quote_balance : float = 0.0    # USDT
    total_pnl     : float = 0.0
    trades_count  : int   = 0
    fees_earned   : float = 0.0

    def base_value(self, price: float) -> float:
        return self.base_balance * price

    def total_value(self, price: float) -> float:
        return self.base_value(price) + self.quote_balance


# ---- MarketMakerBot
class MarketMakerBot:
    """
    Automated market maker bot for NEBULA DEX.
    Provides two-sided liquidity (both bids and asks).
    Earns the spread between buy and sell orders.
    """

    def __init__(self, dex: 'DEXEngine',
                 oracle: 'PriceOracle',
                 config: MMConfig):
        self.dex         = dex
        self.oracle      = oracle
        self.config      = config
        self.inventory   = MMInventory(base_balance=config.max_position,
                                        quote_balance=config.max_position * 0.5)
        self._orders     : Dict[str, dict] = {}
        self._running    = False
        self._lock       = threading.Lock()
        self._pnl_history: List[float] = []

    def get_fair_value(self) -> Optional[float]:
        """Get fair value from oracle"""
        if "NBL" in self.config.pair:
            return self.oracle.get_nbl_usd()
        return None

    def compute_quotes(self, fair_value: float) -> Tuple[float, float]:
        """Compute bid/ask quotes around fair value"""
        half_spread = fair_value * self.config.spread_bps / 10_000 / 2
        bid = fair_value - half_spread
        ask = fair_value + half_spread
        return bid, ask

    def place_quotes(self) -> dict:
        """Place/update market making orders"""
        fv = self.get_fair_value()
        if not fv:
            return {"error": "No price feed"}

        bid, ask = self.compute_quotes(fv)
        size     = self.inventory.base_balance * self.config.order_size_pct
        size_nbl = int(size * 10**DECIMALS)

        placed   = []
        # Place buy (bid) order
        if self.inventory.quote_balance >= bid * size:
            oid, _ = self.dex.place_order(
                "mm_bot", self.config.pair, "buy", "limit", bid, size_nbl)
            placed.append({"side": "buy", "price": bid, "size": size})
            with self._lock:
                self._orders[oid] = {"side": "buy", "price": bid}

        # Place sell (ask) order
        if self.inventory.base_balance >= size:
            oid, _ = self.dex.place_order(
                "mm_bot", self.config.pair, "sell", "limit", ask, size_nbl)
            placed.append({"side": "sell", "price": ask, "size": size})
            with self._lock:
                self._orders[oid] = {"side": "sell", "price": ask}

        return {
            "fair_value": fv,
            "bid"       : bid,
            "ask"       : ask,
            "spread_pct": f"{(ask-bid)/fv*100:.3f}%",
            "placed"    : placed,
        }

    def rebalance(self):
        """Rebalance inventory toward target"""
        fv = self.get_fair_value()
        if not fv:
            return
        total  = self.inventory.total_value(fv)
        target = total * self.config.inventory_target
        current = self.inventory.base_value(fv)
        diff   = target - current
        if abs(diff) > total * 0.05:  # > 5% drift
            if diff > 0:
                # Need more base: buy
                qty = diff / fv
                self.inventory.base_balance  += qty
                self.inventory.quote_balance -= diff
            else:
                # Too much base: sell
                qty = abs(diff) / fv
                self.inventory.base_balance  -= qty
                self.inventory.quote_balance += abs(diff)

    def simulate_trade(self, side: str, price: float, amount: float):
        """Simulate a trade execution"""
        if side == "buy":
            self.inventory.base_balance  += amount
            self.inventory.quote_balance -= price * amount
        else:
            self.inventory.base_balance  -= amount
            self.inventory.quote_balance += price * amount
        self.inventory.trades_count += 1
        # Earn half the spread as fees
        fv = self.get_fair_value() or price
        fee = abs(price - fv) * amount
        self.inventory.fees_earned    += fee
        self.inventory.total_pnl      += fee

    def start(self, interval: float = 30.0):
        """Start market making"""
        self._running = True
        def _loop():
            while self._running:
                try:
                    self.place_quotes()
                except Exception:
                    _NB_SWALLOW_LOG.debug("swallowed Exception in MarketMakerBot.start._loop", exc_info=True)
                time.sleep(interval)
        threading.Thread(target=_loop, daemon=True, name="MarketMaker").start()
        print(f"  📈 Market Maker started: {self.config.pair}")

    def stop(self): self._running = False

    def pnl_report(self) -> dict:
        fv = self.get_fair_value() or 0.0
        return {
            "pair"           : self.config.pair,
            "base_balance"   : self.inventory.base_balance,
            "quote_balance"  : self.inventory.quote_balance,
            "total_value_usd": self.inventory.total_value(fv),
            "total_pnl"      : self.inventory.total_pnl,
            "fees_earned"    : self.inventory.fees_earned,
            "trades"         : self.inventory.trades_count,
            "spread_bps"     : self.config.spread_bps,
        }


# ---- ConsensusParams
@dataclass
class ConsensusParams:
    """Live consensus parameters (some adjustable by governance)"""
    target_block_time  : int   = TARGET_BLOCK_TIME
    max_block_size     : int   = MAX_BLOCK_SIZE_BYTES
    min_tx_fee         : int   = MIN_TX_FEE
    coinbase_maturity  : int   = COINBASE_MATURITY
    dust_threshold     : int   = DUST_THRESHOLD
    max_tx_per_block   : int   = MAX_TX_PER_BLOCK
    difficulty_window  : int   = DIFFICULTY_WINDOW
    foundation_rate    : float = FOUNDATION_RATE
    max_ancestors      : int   = 25
    max_descendants    : int   = 25
    enable_taproot     : bool  = True
    enable_segwit      : bool  = True

    def to_dict(self) -> dict:
        return {
            "target_block_time" : self.target_block_time,
            "max_block_size"    : self.max_block_size,
            "min_tx_fee"        : self.min_tx_fee,
            "coinbase_maturity" : self.coinbase_maturity,
            "dust_threshold"    : self.dust_threshold,
            "difficulty_window" : self.difficulty_window,
            "foundation_rate"   : self.foundation_rate,
            "enable_taproot"    : self.enable_taproot,
            "enable_segwit"     : self.enable_segwit,
        }


# ---- DifficultyCLI
class DifficultyCLI:
    """
    Alternative difficulty adjustment algorithms.
    NEBULA uses LWMA; alternatives for testing.
    """

    @staticmethod
    def simple_ema(blockchain: 'NEBULABlockchain',
                    alpha: float = 0.1) -> int:
        """
        Exponential Moving Average difficulty.
        Smooth response to hashrate changes.
        """
        chain = blockchain._chain
        if len(chain) < 2:
            return INITIAL_BITS
        times = [chain[i].header.timestamp - chain[i-1].header.timestamp
                 for i in range(max(1,len(chain)-20), len(chain))]
        if not times:
            return blockchain.get_next_bits()
        ema = times[0]
        for t in times[1:]:
            ema = alpha * t + (1-alpha) * ema
        ratio     = ema / TARGET_BLOCK_TIME
        target    = bits_to_target(chain[-1].header.bits)
        new_target= int(target * ratio)
        # Clamp
        max_t     = bits_to_target(INITIAL_BITS)
        new_target = max(1, min(max_t, new_target))
        # Convert back to bits
        nbytes   = (new_target.bit_length() + 7) // 8
        mantissa = new_target >> (8*(nbytes-3))
        return (nbytes << 24) | mantissa

    @staticmethod
    def zawy_lwma(blockchain: 'NEBULABlockchain',
                   n: int = 60) -> int:
        """
        Zawy's LWMA (Linear Weighted Moving Average).
        More responsive than Bitcoin's 2016-block window.
        Used in many altcoins.
        """
        chain = blockchain._chain
        if len(chain) < n + 1:
            return INITIAL_BITS
        window = chain[-(n+1):]
        L  = 0
        ST = 0
        for i in range(1, n+1):
            dt = max(1, window[i].header.timestamp - window[i-1].header.timestamp)
            L += i * dt
            ST += dt
        avg_target = sum(bits_to_target(window[i].header.bits)
                         for i in range(1, n+1)) / n
        k          = n*(n+1)//2 * TARGET_BLOCK_TIME
        new_target = int(avg_target * L / k)
        max_t      = bits_to_target(INITIAL_BITS)
        new_target = max(1, min(max_t * 4, new_target))
        nbytes     = (new_target.bit_length() + 7) // 8
        mantissa   = new_target >> (8*(nbytes-3))
        return (nbytes << 24) | mantissa


# ---- ConsensusManager
class ConsensusManager:
    """
    Manages consensus parameters and their updates.
    Parameters can be updated via governance votes.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                 governance: 'GovernanceEngine' = None):
        self.bc         = blockchain
        self.governance = governance
        self.params     = ConsensusParams()
        self._lock      = threading.Lock()
        self._history   : List[Tuple[int, str, object]] = []

    def update_param(self, param: str, value: object,
                      caller: str = "governance") -> bool:
        """Update a consensus parameter"""
        if not hasattr(self.params, param):
            return False
        with self._lock:
            old_val = getattr(self.params, param)
            setattr(self.params, param, value)
            self._history.append((self.bc.height, param, old_val))
            print(f"  📋 Consensus param '{param}' updated: {old_val} → {value}")
        return True

    def get_param(self, param: str) -> object:
        return getattr(self.params, param, None)

    def validate_update(self, param: str, value: object) -> Tuple[bool, str]:
        """Validate a proposed parameter update"""
        if param == "target_block_time":
            if not (30 <= value <= 3600):
                return False, "Block time must be 30-3600 seconds"
        elif param == "max_block_size":
            if not (100_000 <= value <= 4_000_000):
                return False, "Block size must be 100KB-4MB"
        elif param == "foundation_rate":
            if not (0.0 <= value <= 0.10):
                return False, "Foundation rate must be 0-10%"
        return True, "Valid"

    def best_difficulty_algo(self) -> str:
        """Recommend best difficulty algorithm for current chain"""
        if self.bc.height < 100:
            return "simple"
        return "zawy_lwma"

    def history(self) -> List[dict]:
        with self._lock:
            return [{"height": h, "param": p, "old_value": v}
                    for h, p, v in self._history[-20:]]

    def stats(self) -> dict:
        return {
            "params"          : self.params.to_dict(),
            "updates"         : len(self._history),
            "best_diff_algo"  : self.best_difficulty_algo(),
        }


# ---- ExplorerV2Handler
class ExplorerV2Handler(BaseHTTPRequestHandler):
    """Enhanced block explorer with DeFi/NFT data"""
    explorer2 = None

    def log_message(self, fmt, *args): pass

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path   = parsed.path.rstrip('/')
        params = dict(urllib.parse.parse_qsl(parsed.query))

        routes = {
            '/v2/address_full' : lambda: self._address_full(params),
            '/v2/nft_gallery'  : lambda: self._nft_gallery(params),
            '/v2/defi_pos'     : lambda: self._defi_positions(params),
            '/v2/staking'      : lambda: self._staking_info(params),
            '/v2/token_list'   : self._token_list,
            '/v2/chain_metrics': self._chain_metrics,
            '/v2/dex_summary'  : self._dex_summary,
            '/v2/pool_stats'   : self._pool_stats,
        }
        handler = routes.get(path)
        if handler:
            try:
                self._json(200, handler())
            except Exception as e:
                self._json(500, {"error": str(e)})
        else:
            self._json(404, {"error": "Not found"})

    def _address_full(self, p: dict) -> dict:
        addr = p.get("addr", "")
        ex   = self.explorer2
        bc   = ex.bc

        result = {
            "address"    : addr,
            "balance_nbl": bc.utxo.balance(addr) / 10**DECIMALS,
            "utxo_count" : len(bc.utxo.get_by_address(addr)),
        }

        # NFTs
        if ex.nft:
            result["nfts"] = ex.nft.get_owner_nfts(addr)

        # Staking
        if ex.staking:
            result["staking"] = ex.staking.get_staker_info(addr, bc.height)

        # Cluster
        if ex.clusterer:
            cluster = ex.clusterer.get_cluster_for_address(addr)
            if cluster:
                result["cluster"] = cluster.to_dict()

        return result

    def _nft_gallery(self, p: dict) -> dict:
        addr = p.get("addr", "")
        ex   = self.explorer2
        nfts = ex.nft.get_owner_nfts(addr) if ex.nft else []
        return {"address": addr, "nfts": nfts, "count": len(nfts)}

    def _defi_positions(self, p: dict) -> dict:
        addr = p.get("addr", "")
        ex   = self.explorer2
        result = {"address": addr}
        if ex.amm:
            positions = []
            for pid, pool in ex.amm._pools.items():
                share = pool.lp_share(addr)
                if share > 0:
                    positions.append({
                        "pool"  : pid,
                        "share" : f"{share*100:.4f}%",
                        "value" : pool.total_value * share / 10**DECIMALS,
                    })
            result["amm_positions"] = positions
        return result

    def _staking_info(self, p: dict) -> dict:
        addr = p.get("addr", "")
        ex   = self.explorer2
        if ex.staking:
            return ex.staking.get_staker_info(addr, ex.bc.height)
        return {"error": "Staking not available"}

    def _token_list(self) -> dict:
        ex = self.explorer2
        if ex.token_registry:
            return {"tokens": ex.token_registry.list_tokens()}
        return {"tokens": []}

    def _chain_metrics(self) -> dict:
        ex = self.explorer2
        if ex.metrics:
            return {"metrics": ex.metrics.compute_all()}
        return {"error": "Metrics not available"}

    def _dex_summary(self) -> dict:
        ex = self.explorer2
        if ex.dex:
            return {"summary": ex.dex.market_summary(), "stats": ex.dex.stats()}
        return {"error": "DEX not available"}

    def _pool_stats(self) -> dict:
        ex = self.explorer2
        if ex.pool:
            return ex.pool.stats()
        return {"error": "Pool not available"}

    def _json(self, code: int, data: dict):
        body = json.dumps(data, default=str).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)


# ---- BlockExplorerV2
class BlockExplorerV2:
    """Enhanced block explorer with DeFi + NFT integration"""

    def __init__(self, bc, nft=None, staking=None, amm=None,
                 dex=None, pool=None, token_registry=None,
                 clusterer=None, metrics=None,
                 host="0.0.0.0", port=8082):
        self.bc             = bc
        self.nft            = nft
        self.staking        = staking
        self.amm            = amm
        self.dex            = dex
        self.pool           = pool
        self.token_registry = token_registry
        self.clusterer      = clusterer
        self.metrics        = metrics
        self.host           = host
        self.port           = port
        self._server        = None

    def start(self):
        ExplorerV2Handler.explorer2 = self
        self._server = HTTPServer((self.host, self.port), ExplorerV2Handler)
        threading.Thread(target=self._server.serve_forever,
                          daemon=True, name="ExplorerV2").start()
        print(f"🔍 Explorer v2: http://{self.host}:{self.port}/v2/chain_metrics")

    def stop(self):
        if self._server:
            self._server.shutdown()


# ---- SimulationResult
@dataclass
class SimulationResult:
    """Result of a transaction simulation"""
    scenario   : str
    tx_count   : int
    total_fees : float
    success    : bool
    elapsed_ms : float
    details    : List[dict] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "scenario"  : self.scenario,
            "tx_count"  : self.tx_count,
            "total_fees": self.total_fees,
            "success"   : self.success,
            "elapsed_ms": round(self.elapsed_ms, 2),
        }


# ---- TxSimulator
class TxSimulator:
    """
    Simulate complex transaction scenarios without broadcasting.
    Useful for: testing strategies, estimating fees, stress testing.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self.bc     = blockchain
        self._mock  = MockBlockchain()

    def simulate_dca(self, buyer_addr: str,
                      target_addr: str,
                      weekly_amount: float,
                      weeks: int = 52) -> SimulationResult:
        """Simulate Dollar-Cost Averaging over N weeks"""
        start    = time.time()
        self._mock.fund_address(buyer_addr, weekly_amount * weeks * 2)
        success  = 0
        details  = []
        fee_per_tx = MIN_TX_FEE / 10**DECIMALS

        for week in range(weeks):
            ok, _ = self._mock.mock_send(buyer_addr, target_addr, weekly_amount)
            if ok:
                success += 1
            details.append({"week": week+1, "amount": weekly_amount, "ok": ok})

        elapsed = (time.time() - start) * 1000
        return SimulationResult(
            scenario  = f"DCA {weeks}w @ {weekly_amount} NBL",
            tx_count  = weeks,
            total_fees= fee_per_tx * weeks,
            success   = success == weeks,
            elapsed_ms= elapsed,
            details   = details[:5],
        )

    def simulate_grid_trading(self, wallet: str,
                               low: float, high: float,
                               grid_levels: int = 10,
                               amount_per_grid: float = 1.0) -> SimulationResult:
        """Simulate grid trading strategy"""
        start  = time.time()
        prices = [low + (high-low)*i/(grid_levels-1) for i in range(grid_levels)]
        trades = []

        self._mock.fund_address(wallet, amount_per_grid * grid_levels * 2)

        for i, price in enumerate(prices):
            # Buy below midpoint, sell above
            mid = (low + high) / 2
            if price < mid:
                ok, _ = self._mock.mock_send(wallet, f"grid_buy_{i}", amount_per_grid)
                trades.append({"type": "buy", "price": price, "ok": ok})
            else:
                ok, _ = self._mock.mock_send(f"grid_buy_{i}", wallet, amount_per_grid * price / mid)
                trades.append({"type": "sell", "price": price, "ok": ok})

        elapsed = (time.time() - start) * 1000
        total_fees = MIN_TX_FEE / 10**DECIMALS * len(trades)
        return SimulationResult(
            scenario  = f"Grid {grid_levels} levels {low:.2f}-{high:.2f}",
            tx_count  = len(trades),
            total_fees= total_fees,
            success   = True,
            elapsed_ms= elapsed,
            details   = trades[:5],
        )

    def simulate_batch_send(self, sender: str,
                             recipients: List[str],
                             amount_each: float) -> SimulationResult:
        """Simulate sending to many recipients"""
        start  = time.time()
        total  = amount_each * len(recipients)
        self._mock.fund_address(sender, total * 1.1)
        ok_count = 0
        for addr in recipients:
            ok, _ = self._mock.mock_send(sender, addr, amount_each)
            if ok: ok_count += 1
        elapsed = (time.time() - start) * 1000
        return SimulationResult(
            scenario  = f"Batch send to {len(recipients)} addresses",
            tx_count  = len(recipients),
            total_fees= MIN_TX_FEE/10**DECIMALS * len(recipients),
            success   = ok_count == len(recipients),
            elapsed_ms= elapsed,
        )

    def estimate_scenario_cost(self, scenario: str,
                                tx_count: int,
                                avg_tx_size: int = 250) -> dict:
        """Estimate cost for a scenario"""
        fee_per_tx  = avg_tx_size * MIN_TX_FEE / 1000 / 10**DECIMALS
        total_fee   = fee_per_tx * tx_count
        return {
            "scenario"       : scenario,
            "tx_count"       : tx_count,
            "fee_per_tx"     : fee_per_tx,
            "total_fee_nbl"  : total_fee,
            "at_1_usd"       : f"${total_fee:.4f} USD",
        }
