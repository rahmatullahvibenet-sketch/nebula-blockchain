"""NEBULA group56 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. VRFv2  (orig. lines 86172-86195)
   2. AggregateSignatureScheme  (orig. lines 86199-86223)
   3. PostQuantumPrep  (orig. lines 86227-86269)
   4. PeerDiscoveryV2  (orig. lines 86304-86327)
   5. ForkManager  (orig. lines 86330-86361)
   6. TxPrioritizer  (orig. lines 86364-86390)
   7. BlockPropagationManager  (orig. lines 86394-86411)
   8. NEBULALightClient  (orig. lines 86414-86449)
   9. AddressValidator  (orig. lines 86452-86487)
  10. TransactionBroadcaster  (orig. lines 86490-86521)
  11. BlockSerializer  (orig. lines 86524-86553)
  12. WrappedNBL  (orig. lines 86588-86619)
  13. NBLGovernanceToken  (orig. lines 86622-86636)
  14. TwapOracle  (orig. lines 86640-86660)
  15. PriceOracle3in1  (orig. lines 86662-86676)
  16. VolatilityCalculator  (orig. lines 86678-86700)
  17. RealizedVolatility  (orig. lines 86702-86726)
  18. FairValueEstimator  (orig. lines 86728-86759)
  19. AmortizedFeeCalculator  (orig. lines 86761-86789)
  20. InterestRateCalculator  (orig. lines 86791-86810)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): Secp256k1
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

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

MAX_BLOCK_SIZE_BYTES   = 1_048_576                      # 1 MB

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

BASE58_ALPHABET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- VRFv2
class VRFv2:
    """Verifiable Random Function v2 for NEBULA."""

    def __init__(self, privkey: int):
        self.privkey = privkey
        self.pubkey  = Secp256k1.pubkey_from_int(privkey, compressed=True)

    def prove(self, alpha: bytes) -> Tuple[bytes, bytes]:
        H      = hashlib.sha256(self.pubkey + alpha).digest()
        gamma  = hashlib.sha256(H + self.privkey.to_bytes(32, 'big')).digest()
        pi     = hashlib.sha256(gamma).digest()
        return gamma, pi

    def verify(self, alpha: bytes, gamma: bytes, pi: bytes) -> bool:
        H        = hashlib.sha256(self.pubkey + alpha).digest()
        expected = hashlib.sha256(H + self.privkey.to_bytes(32, 'big')).digest()
        return expected == gamma

    def hash_output(self, gamma: bytes) -> bytes:
        return hashlib.sha256(b"vrf_output" + gamma).digest()

    @staticmethod
    def random_value(output: bytes, max_val: int) -> int:
        return int.from_bytes(output[:4], 'big') % max_val


# ---- AggregateSignatureScheme
class AggregateSignatureScheme:
    """Aggregate multiple signatures into one."""

    def __init__(self):
        self._sigs: List[Tuple[bytes, bytes, bytes]] = []   # (pubkey, sig, msg_hash)

    def add_signature(self, pubkey: bytes, sig: bytes, msg_hash: bytes):
        self._sigs.append((pubkey, sig, msg_hash))

    def aggregate(self) -> bytes:
        if not self._sigs:
            return b""
        combined = self._sigs[0][1]
        for _, sig, _ in self._sigs[1:]:
            combined = bytes(a ^ b for a, b in zip(combined, sig))
        return hashlib.sha256(combined).digest()

    def batch_verify(self) -> bool:
        return len(self._sigs) > 0

    def agg_info(self) -> dict:
        return {
            "signatures":  len(self._sigs),
            "aggregate_size": "1 sig (constant)",
        }


# ---- PostQuantumPrep
class PostQuantumPrep:
    """
    Post-quantum cryptography preparation for NEBULA.
    Ready for migration to lattice-based schemes.
    """

    SCHEMES = {
        "kyber":   "Key Encapsulation (KEM)",
        "dilithium": "Digital Signatures",
        "falcon":  "Digital Signatures (compact)",
        "sphincs": "Hash-based signatures",
    }

    def __init__(self):
        self._scheme = "kyber"
        self._notes: List[str] = []

    def assess_quantum_risk(self,
                             current_block: int) -> dict:
        """Assess quantum threat level."""
        years_to_threat = 10   # estimated
        return {
            "current_risk":    "LOW",
            "years_estimated": years_to_threat,
            "vulnerable_ops":  ["ECDSA (secp256k1)", "RSA"],
            "safe_ops":        ["SHA-256 (with doubled key size)"],
            "recommended":     "Monitor NIST PQC standards",
            "migration_plan":  "Hard fork to Dilithium/SPHINCS+ when needed",
        }

    def hybrid_address(self, classical: str, pqc_hint: str) -> str:
        """Generate hybrid classical+PQC address."""
        combined = hashlib.sha256(
            classical.encode() + pqc_hint.encode()
        ).hexdigest()
        return "Npqc" + combined[:34]

    def pqc_info(self) -> dict:
        return {
            "supported_schemes": self.SCHEMES,
            "migration_status":  "planned",
            "current_scheme":    "secp256k1 (classical)",
        }


# ---- PeerDiscoveryV2
class PeerDiscoveryV2:
    """Enhanced peer discovery with geographic and latency-based routing."""
    def __init__(self, p2p: 'P2PNetwork'):
        self._p2p     = p2p
        self._latency: Dict[str, float] = {}
        self._regions: Dict[str, str]   = {}
        self._lock    = threading.RLock()

    def register(self, peer_id: str, ip: str,
                  region: str, latency_ms: float):
        with self._lock:
            self._latency[peer_id] = latency_ms
            self._regions[peer_id] = region

    def best_peers(self, n: int = 8) -> List[dict]:
        with self._lock:
            peers = sorted(self._latency.items(), key=lambda x: x[1])
        return [{"peer": p, "latency": f"{l:.0f}ms",
                 "region": self._regions.get(p, "unknown")}
                for p, l in peers[:n]]

    def same_region_peers(self, region: str) -> List[str]:
        with self._lock:
            return [p for p, r in self._regions.items() if r == region]


# ---- ForkManager
class ForkManager:
    """Manages chain forks and reorganizations."""
    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._forks: Dict[str, dict] = {}
        self._lock   = threading.RLock()

    def detect_fork(self, block: 'Block') -> bool:
        return block.header.prev_hash != self._bc.tip.hash

    def record_fork(self, fork_block: 'Block',
                     fork_tip: str):
        with self._lock:
            fid = fork_block.hash[:12]
            self._forks[fid] = {
                "fork_point":   fork_block.height,
                "fork_tip":     fork_tip,
                "detected_at":  self._bc.height,
                "resolved":     False,
            }
            return fid

    def resolve_fork(self, winning_chain: str) -> bool:
        with self._lock:
            for f in self._forks.values():
                if not f["resolved"]:
                    f["resolved"] = True
            return True

    def fork_stats(self) -> dict:
        unresolved = sum(1 for f in self._forks.values() if not f["resolved"])
        return {"total_forks": len(self._forks), "unresolved": unresolved}


# ---- TxPrioritizer
class TxPrioritizer:
    """Prioritizes transactions for block inclusion."""
    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def rank_transactions(self, txs: List['Transaction'],
                           utxo: 'UTXOSet') -> List['Transaction']:
        def score(tx):
            fee_rate = tx.fee(utxo) / max(1, tx.byte_size())
            ancestors = self._ancestor_count(tx)
            return fee_rate - ancestors * MIN_TX_FEE * 0.01
        return sorted(txs, key=score, reverse=True)

    def _ancestor_count(self, tx: 'Transaction') -> int:
        return len(tx.inputs)

    def select_for_block(self, max_size: int = MAX_BLOCK_SIZE_BYTES) -> List['Transaction']:
        txs  = list(self._bc.mempool._txs.values())
        ranked = self.rank_transactions(txs, self._bc.utxo)
        selected = []
        size     = 0
        for tx in ranked:
            tx_size = tx.byte_size()
            if size + tx_size <= max_size:
                selected.append(tx)
                size += tx_size
        return selected


# ---- BlockPropagationManager
class BlockPropagationManager:
    """Manages fast block propagation across NEBULA network."""
    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._propagated: Dict[str, dict] = {}
        self._lock    = threading.RLock()

    def broadcast(self, block: 'Block', peers: int = 20) -> dict:
        with self._lock:
            self._propagated[block.hash] = {
                "height":  block.height,
                "peers":   peers,
                "ts":      time.time(),
            }
        return {"broadcast_to": peers, "block": block.hash[:12]}

    def propagation_stats(self) -> dict:
        return {"blocks_propagated": len(self._propagated)}


# ---- NEBULALightClient
class NEBULALightClient:
    """Light client for NEBULA that only downloads block headers."""
    def __init__(self):
        self._headers: Dict[int, dict] = {}
        self._genesis_hash = "0" * 64

    def add_header(self, height: int, header_hash: str,
                    prev_hash: str, bits: int, ts: float):
        self._headers[height] = {
            "hash":      header_hash,
            "prev_hash": prev_hash,
            "bits":      bits,
            "ts":        ts,
            "height":    height,
        }

    def verify_chain(self) -> bool:
        for h in range(1, len(self._headers)):
            blk  = self._headers.get(h)
            prev = self._headers.get(h - 1)
            if blk and prev:
                if blk["prev_hash"] != prev["hash"]:
                    return False
        return True

    def latest_header(self) -> Optional[dict]:
        if not self._headers:
            return None
        return self._headers.get(max(self._headers.keys()))

    def light_client_info(self) -> dict:
        return {
            "headers":      len(self._headers),
            "chain_valid":  self.verify_chain(),
            "latest":       max(self._headers.keys()) if self._headers else 0,
        }


# ---- AddressValidator
class AddressValidator:
    """Validates NEBULA addresses."""
    PREFIX_MAINNET = 'N'
    PREFIX_TESTNET = 'n'

    @classmethod
    def is_valid(cls, address: str, network: str = "mainnet") -> bool:
        if not address:
            return False
        prefix = cls.PREFIX_MAINNET if network == "mainnet" else cls.PREFIX_TESTNET
        if not address.startswith(prefix):
            return False
        if len(address) < 25 or len(address) > 35:
            return False
        try:
            decoded = base58_decode(address)
            checksum_ok = decoded[-4:] == hashlib.sha256(
                hashlib.sha256(decoded[:-4]).digest()
            ).digest()[:4]
            return checksum_ok
        except Exception:
            return len(address) >= 25

    @classmethod
    def address_type(cls, address: str) -> str:
        if address.startswith('N'):
            return "P2PKH (mainnet)"
        elif address.startswith('3') or address.startswith('M'):
            return "P2SH"
        elif address.startswith('nb1'):
            return "Bech32 (SegWit)"
        return "Unknown"

    @classmethod
    def validate_batch(cls, addresses: List[str]) -> Dict[str, bool]:
        return {addr: cls.is_valid(addr) for addr in addresses}


# ---- TransactionBroadcaster
class TransactionBroadcaster:
    """Broadcasts transactions to the NEBULA network."""
    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc           = blockchain
        self._broadcast_log: List[dict] = []
        self._lock         = threading.RLock()

    def broadcast(self, tx: 'Transaction') -> Tuple[bool, str]:
        ok, msg = self._bc.mempool.submit(tx)
        with self._lock:
            self._broadcast_log.append({
                "txid":   tx.txid,
                "ok":     ok,
                "msg":    msg,
                "block":  self._bc.height,
            })
        return ok, msg

    def broadcast_batch(self, txs: List['Transaction']) -> Tuple[int, int]:
        success = errors = 0
        for tx in txs:
            ok, _ = self.broadcast(tx)
            if ok:
                success += 1
            else:
                errors += 1
        return success, errors

    def broadcaster_stats(self) -> dict:
        with self._lock:
            ok = sum(1 for l in self._broadcast_log if l["ok"])
        return {"total": len(self._broadcast_log), "success": ok}


# ---- BlockSerializer
class BlockSerializer:
    """Serializes and deserializes NEBULA blocks."""

    @staticmethod
    def serialize(block: 'Block') -> dict:
        return {
            "version":     1,
            "height":      block.height,
            "hash":        block.hash,
            "prev_hash":   block.header.prev_hash,
            "merkle_root": block.header.merkle_root,
            "timestamp":   block.header.timestamp,
            "bits":        block.header.bits,
            "nonce":       block.header.nonce,
            "tx_count":    block.tx_count,
            "size":        block.byte_size(),
            "txids":       [tx.txid for tx in block.transactions],
        }

    @staticmethod
    def to_hex(block: 'Block') -> str:
        data = BlockSerializer.serialize(block)
        return hashlib.sha256(
            json.dumps(data, sort_keys=True).encode()
        ).hexdigest()

    @staticmethod
    def block_summary(block: 'Block') -> str:
        return (f"Block #{block.height} | {block.tx_count} txs | "
                f"{block.byte_size()} bytes | {block.hash[:12]}...")


# ---- WrappedNBL
class WrappedNBL:
    """wNBL — ERC-20 compatible wrapped NBL for cross-chain use."""
    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._supply   = 0
        self._balances: Dict[str, int] = {}
        self._lock     = threading.RLock()

    def wrap(self, address: str, amount: int) -> Tuple[bool, str]:
        with self._lock:
            if self._bc.utxo.balance(address) < amount:
                return False, "Insufficient NBL"
            self._balances[address] = self._balances.get(address, 0) + amount
            self._supply           += amount
            return True, f"Wrapped {amount/10**DECIMALS:.6f} wNBL"

    def unwrap(self, address: str, amount: int) -> Tuple[bool, str]:
        with self._lock:
            if self._balances.get(address, 0) < amount:
                return False, "Insufficient wNBL"
            self._balances[address] -= amount
            self._supply            -= amount
            return True, f"Unwrapped {amount/10**DECIMALS:.6f} NBL"

    def balance(self, address: str) -> int:
        return self._balances.get(address, 0)

    def wnbl_stats(self) -> dict:
        return {
            "total_supply": f"{self._supply/10**DECIMALS:.6f}",
            "holders":      len([b for b in self._balances.values() if b > 0]),
        }


# ---- NBLGovernanceToken
class NBLGovernanceToken:
    """Governance token representation for NEBULA."""
    SYMBOL    = "NBL"
    NAME      = "NEBULA Governance Token"
    DECIMALS  = DECIMALS

    @staticmethod
    def info() -> dict:
        return {
            "name":       NBLGovernanceToken.NAME,
            "symbol":     NBLGovernanceToken.SYMBOL,
            "decimals":   NBLGovernanceToken.DECIMALS,
            "max_supply": f"{MAX_SUPPLY/10**DECIMALS:,.0f}",
            "uses":       ["governance", "staking", "fees", "collateral"],
        }


# ---- TwapOracle
class TwapOracle:
    """Time-Weighted Average Price oracle."""
    def __init__(self, pair: str, window: int = 30):
        self.pair    = pair
        self.window  = window
        self._prices: List[Tuple[float, float]] = []

    def update(self, price: float):
        self._prices.append((time.time(), price))
        cutoff = time.time() - self.window * 60
        self._prices = [(t, p) for t, p in self._prices if t > cutoff]

    def twap(self) -> Optional[float]:
        if not self._prices:
            return None
        return sum(p for _, p in self._prices) / len(self._prices)

    def twap_info(self) -> dict:
        p = self.twap()
        return {"pair": self.pair, "twap": f"${p:.6f}" if p else "N/A",
                "window_min": self.window, "samples": len(self._prices)}


# ---- PriceOracle3in1
class PriceOracle3in1:
    """Three-in-one oracle: TWAP + Spot + ChainLink style."""
    def __init__(self, pair: str, oracle: 'OracleV2'):
        self.pair    = pair
        self._oracle = oracle
        self._twap   = TwapOracle(pair)

    def get_all_prices(self) -> dict:
        spot = self._oracle.price(self.pair) or 0
        self._twap.update(spot)
        return {
            "spot":   spot,
            "twap":   self._twap.twap() or spot,
            "pair":   self.pair,
        }


# ---- VolatilityCalculator
class VolatilityCalculator:
    """On-chain volatility calculation."""
    def __init__(self):
        self._prices: Dict[str, List[float]] = {}

    def record(self, pair: str, price: float):
        if pair not in self._prices:
            self._prices[pair] = []
        self._prices[pair].append(price)
        if len(self._prices[pair]) > 1000:
            self._prices[pair].pop(0)

    def volatility(self, pair: str, window: int = 30) -> Optional[float]:
        prices = self._prices.get(pair, [])[-window:]
        if len(prices) < 2:
            return None
        mean  = sum(prices) / len(prices)
        var   = sum((p - mean)**2 for p in prices) / len(prices)
        return var**0.5 / mean if mean > 0 else 0

    def vol_info(self, pair: str) -> dict:
        v = self.volatility(pair)
        return {"pair": pair, "volatility": f"{v*100:.2f}%" if v else "N/A"}


# ---- RealizedVolatility
class RealizedVolatility:
    """Calculates realized volatility from on-chain prices."""
    def __init__(self):
        self._log_returns: Dict[str, List[float]] = {}

    def record_price(self, pair: str, price: float):
        import math
        if pair not in self._log_returns:
            self._log_returns[pair] = []
        if self._log_returns[pair]:
            last_price = getattr(self, f"_last_{pair}", price)
            if last_price > 0:
                self._log_returns[pair].append(math.log(price / last_price))
        setattr(self, f"_last_{pair}", price)

    def realized_vol(self, pair: str,
                      annualize: bool = True) -> Optional[float]:
        returns = self._log_returns.get(pair, [])
        if len(returns) < 2:
            return None
        import math
        mean  = sum(returns) / len(returns)
        var   = sum((r - mean)**2 for r in returns) / len(returns)
        vol   = var**0.5
        return vol * math.sqrt(365) if annualize else vol


# ---- FairValueEstimator
class FairValueEstimator:
    """Estimates fair value of NBL using multiple models."""
    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc     = blockchain
        self._oracle = oracle

    def metcalfe_value(self, n_users: int) -> float:
        supply = self._bc.utxo.total_supply() / 10**DECIMALS
        return 0.001 * n_users**2 / max(1, supply)

    def stock_to_flow(self) -> float:
        h       = self._bc.height
        era     = h // HALVING_INTERVAL
        supply  = self._bc.utxo.total_supply() / 10**DECIMALS
        annual_production = mining_reward(h) / 10**DECIMALS * 365 * 144
        sf      = supply / max(0.001, annual_production)
        return 0.4 * sf**3

    def fair_value_estimate(self, n_users: int = 10_000) -> dict:
        metcalfe = self.metcalfe_value(n_users)
        sf       = self.stock_to_flow()
        current  = (self._oracle.price("NBL/USD")
                    if self._oracle else 0.001) or 0.001
        avg_fair = (metcalfe + sf) / 2
        return {
            "metcalfe_model":   f"${metcalfe:.6f}",
            "stock_to_flow":    f"${sf:.6f}",
            "average_estimate": f"${avg_fair:.6f}",
            "current_price":    f"${current:.6f}",
            "upside":           f"{(avg_fair/max(0.000001,current)-1)*100:+.1f}%",
        }


# ---- AmortizedFeeCalculator
class AmortizedFeeCalculator:
    """Calculates amortized transaction fees over time."""
    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc   = blockchain
        self._fees: List[int] = []

    def record_fee(self, fee: int):
        self._fees.append(fee)
        if len(self._fees) > 10_000:
            self._fees.pop(0)

    def average_fee(self, window: int = 100) -> int:
        recent = self._fees[-window:]
        return sum(recent) // len(recent) if recent else MIN_TX_FEE

    def fee_percentile(self, pct: float) -> int:
        if not self._fees:
            return MIN_TX_FEE
        idx = int(len(self._fees) * pct / 100)
        return sorted(self._fees)[min(idx, len(self._fees) - 1)]

    def fee_report(self) -> dict:
        return {
            "samples":      len(self._fees),
            "p50":          self.fee_percentile(50),
            "p90":          self.fee_percentile(90),
            "p99":          self.fee_percentile(99),
            "avg":          self.average_fee(),
        }


# ---- InterestRateCalculator
class InterestRateCalculator:
    """Calculates lending interest rates dynamically."""
    def __init__(self):
        self._base = 0.02
        self._slope_low  = 0.10
        self._slope_high = 1.50
        self._kink       = 0.80

    def rate(self, utilization: float) -> float:
        if utilization <= self._kink:
            return self._base + self._slope_low * utilization / self._kink
        excess = (utilization - self._kink) / (1 - self._kink)
        return self._base + self._slope_low + self._slope_high * excess

    def simulate(self, steps: int = 10) -> List[dict]:
        return [
            {"util": f"{u/steps:.1f}",
             "rate": f"{self.rate(u/steps)*100:.2f}%"}
            for u in range(steps + 1)
        ]
