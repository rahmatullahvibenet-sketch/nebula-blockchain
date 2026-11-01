"""NEBULA group49 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. YieldStrategy  (orig. lines 77664-77673)
   2. SingleStakingStrategy  (orig. lines 77675-77689)
   3. LPFarmingStrategy  (orig. lines 77691-77705)
   4. CompoundingStrategy  (orig. lines 77707-77722)
   5. ProtocolLimits  (orig. lines 77741-77788)
   6. XCMMessageType  (orig. lines 77846-77851)
   7. XCMMessage  (orig. lines 77853-77871)
   8. XCMRouterV2  (orig. lines 77873-77923)
   9. AdvancedGenesisConfig  (orig. lines 77930-78000)
  10. PrivacyTransaction  (orig. lines 78012-78059)
  11. LiquidityProvisionManager  (orig. lines 78066-78131)
  12. ContractAuditor  (orig. lines 78138-78183)
  13. EcosystemGrantProgram  (orig. lines 78190-78249)
  14. OrderBookV2  (orig. lines 78256-78327)
  15. ValidatorSlashingCondition  (orig. lines 78337-78341)
  16. SlashingEngine  (orig. lines 78343-78400)
  17. NotificationType  (orig. lines 78411-78418)
  18. Notification  (orig. lines 78420-78434)
  19. NotificationSystem  (orig. lines 78436-78492)
  20. Epoch  (orig. lines 78499-78527)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BlockHeader, MerkleTree, P2PKHScript, PedersenCommitment, Secp256k1, Transaction, TransactionOutput
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

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BITS           = 0x1e0fffff if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d0fffff   # [v10.24]

COINBASE_MATURITY      = 100                            # blocks before coinbase spendable

DEFAULT_PORT           = 8333

def _mk_block(header, txs, height=None):
    """Block(header, txs) -- height lives in the header, not in Block()."""
    if height is not None and not getattr(header, 'height', 0):
        header.height = height
    return Block(header, txs)

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

MAX_VALIDATORS           = 100

def impermanent_loss(initial_price: float,
                      current_price: float) -> float:
    """
    Calculate impermanent loss for a 50/50 AMM LP position.
    Returns IL as a percentage (negative means loss).
    """
    ratio = current_price / initial_price
    il    = 2 * ratio**0.5 / (1 + ratio) - 1
    return il * 100

MAX_MEMPOOL_BYTES       = 300 * 1024 * 1024   # 300 MB

MAX_MEMPOOL_ANCESTORS   = 25

MAX_MEMPOOL_DESCENDANTS = 25

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- YieldStrategy
class YieldStrategy:
    """Base class for yield strategies."""

    def __init__(self, name: str, apy: float, risk: int):
        self.name = name
        self.apy  = apy
        self.risk = risk   # 1=low, 5=high

    def execute(self, amount: float) -> dict:
        raise NotImplementedError


# ---- SingleStakingStrategy
class SingleStakingStrategy(YieldStrategy):
    def __init__(self, lock_days: int):
        apy_map = {0: 0.05, 30: 0.08, 90: 0.12, 180: 0.18, 365: 0.25}
        apy = apy_map.get(lock_days, 0.05)
        super().__init__(f"Staking {lock_days}d", apy, 1)
        self.lock_days = lock_days

    def execute(self, amount: float) -> dict:
        return {
            "strategy":  self.name,
            "amount":    amount,
            "annual":    amount * self.apy,
            "monthly":   amount * self.apy / 12,
            "daily":     amount * self.apy / 365,
        }


# ---- LPFarmingStrategy
class LPFarmingStrategy(YieldStrategy):
    def __init__(self, pair: str, apy: float):
        super().__init__(f"LP Farming {pair}", apy, 3)
        self.pair = pair

    def execute(self, amount: float) -> dict:
        il_est = amount * 0.02   # estimated IL
        net_yield = amount * self.apy - il_est
        return {
            "strategy":  self.name,
            "amount":    amount,
            "gross_apy": self.apy,
            "il_est":    il_est,
            "net_annual": net_yield,
        }


# ---- CompoundingStrategy
class CompoundingStrategy(YieldStrategy):
    def __init__(self, base_apy: float, freq: int = 365):
        effective = (1 + base_apy/freq) ** freq - 1
        super().__init__(f"Auto-Compound {freq}/yr", effective, 2)
        self.base_apy = base_apy
        self.freq     = freq

    def execute(self, amount: float) -> dict:
        final = amount * (1 + self.base_apy / self.freq) ** self.freq
        return {
            "strategy":    self.name,
            "principal":   amount,
            "final_year1": final,
            "net_gain":    final - amount,
            "effective_apy": f"{(final/amount-1)*100:.2f}%",
        }


# ---- ProtocolLimits
class ProtocolLimits:
    """All NEBULA protocol limits and constants."""

    # Transaction limits
    MAX_TX_SIZE_BYTES          = 100_000
    MAX_TX_INPUTS              = 10_000
    MAX_TX_OUTPUTS             = 10_000
    MAX_TX_SIGOPS              = 20_000
    MAX_SCRIPT_SIZE            = 10_000
    MAX_ELEMENT_SIZE           = 520

    # Block limits
    MAX_BLOCK_SIGOPS           = 80_000
    MAX_COINBASE_SIZE          = 100
    MATURITY_BLOCKS            = COINBASE_MATURITY

    # P2P limits
    MAX_INV_SIZE               = 50_000
    MAX_HEADERS_RESULTS        = 2000
    MAX_GETDATA_RESULTS        = 1000

    # Mempool limits
    MAX_MEMPOOL_BYTES          = 300 * 1024 * 1024   # 300 MB
    MAX_MEMPOOL_ANCESTORS      = 25
    MAX_MEMPOOL_DESCENDANTS    = 25
    MAX_MEMPOOL_ANCESTOR_SIZE  = 101 * 1024          # 101 KB

    # DeFi limits
    MAX_LIQUIDITY_POOLS        = 10_000
    MAX_VALIDATORS             = 1_000
    MAX_GOVERNANCE_PROPOSALS   = 10_000
    MAX_NFT_PER_COLLECTION     = 100_000

    @classmethod
    def all_limits(cls) -> dict:
        return {
            k: v for k, v in vars(cls).items()
            if not k.startswith('_') and not callable(v)
               and k == k.upper()
        }

    @classmethod
    def is_within_limits(cls, limit_name: str,
                           value: int) -> bool:
        limit = getattr(cls, limit_name, None)
        if limit is None:
            return True
        return value <= limit


# ---- XCMMessageType
class XCMMessageType(_enum.Enum):
    TRANSFER       = "transfer"
    CALL           = "call"
    QUERY          = "query"
    QUERY_RESPONSE = "query_response"
    TELEPORT       = "teleport"


# ---- XCMMessage
@dataclass
class XCMMessage:
    msg_id:      str
    msg_type:    XCMMessageType
    origin:      str   # chain
    destination: str   # chain
    payload:     dict
    fee:         int
    status:      str = "pending"

    def to_dict(self) -> dict:
        return {
            "msg_id":   self.msg_id,
            "type":     self.msg_type.value,
            "origin":   self.origin,
            "dest":     self.destination,
            "status":   self.status,
            "fee":      self.fee,
        }


# ---- XCMRouterV2
class XCMRouterV2:
    """Cross-Chain Message Router v2 for NEBULA."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._messages: Dict[str, XCMMessage] = {}
        self._channels: Dict[str, bool]       = {}   # "src:dst" -> open
        self._lock      = threading.RLock()

    def open_channel(self, src: str, dst: str) -> bool:
        with self._lock:
            self._channels[f"{src}:{dst}"] = True
            self._channels[f"{dst}:{src}"] = True
            return True

    def send_xcm(self, origin: str, destination: str,
                  msg_type: XCMMessageType,
                  payload: dict, fee: int) -> Tuple[bool, str]:
        with self._lock:
            if not self._channels.get(f"{origin}:{destination}", False):
                return False, "No open channel"
            mid = hashlib.sha256(
                f"XCM:{origin}:{destination}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._messages[mid] = XCMMessage(
                msg_id      = mid,
                msg_type    = msg_type,
                origin      = origin,
                destination = destination,
                payload     = payload,
                fee         = fee,
            )
            return True, mid

    def process_message(self, msg_id: str) -> Tuple[bool, str]:
        with self._lock:
            msg = self._messages.get(msg_id)
            if not msg or msg.status != "pending":
                return False, "Not found"
            msg.status = "processed"
            return True, f"XCM processed: {msg.msg_type.value}"

    def xcm_stats(self) -> dict:
        with self._lock:
            processed = sum(1 for m in self._messages.values()
                            if m.status == "processed")
        return {
            "messages":   len(self._messages),
            "processed":  processed,
            "channels":   len(self._channels) // 2,
        }


# ---- AdvancedGenesisConfig
class AdvancedGenesisConfig:
    """
    Advanced genesis configuration for NEBULA.
    Supports custom allocations, vesting, and initial parameters.
    """

    def __init__(self):
        self.allocations:    Dict[str, int]   = {}
        self.vesting_schedules: List[dict]    = []
        self.initial_validators: List[str]    = []
        self.chain_params:   dict             = {}
        self.timestamp      = int(time.time())

    def add_allocation(self, address: str, amount_nbl: float):
        self.allocations[address] = int(amount_nbl * 10**DECIMALS)

    def add_vesting(self, address: str, total: float,
                     cliff_days: int, duration_days: int):
        self.vesting_schedules.append({
            "address":      address,
            "total":        int(total * 10**DECIMALS),
            "cliff_blocks": cliff_days * 144,
            "duration":     duration_days * 144,
        })

    def add_validator(self, address: str):
        self.initial_validators.append(address)

    def to_genesis_block(self) -> 'Block':
        """Build genesis block from configuration."""
        txs = []
        for addr, amount in self.allocations.items():
            tx = Transaction(
                version = 1,
                inputs  = [],
                outputs = [TransactionOutput(
                    value   = amount,
                    address = addr,
                    script  = P2PKHScript.lock(addr),
                )],
            )
            txs.append(tx)
        merkle_root = MerkleTree.compute_root([t.txid for t in txs]) if txs else "0" * 64
        header = BlockHeader(
            version     = 1,
            prev_hash   = "0" * 64,
            merkle_root = merkle_root,
            timestamp   = self.timestamp,
            bits        = INITIAL_BITS,
            nonce       = 0,
        )
        return _mk_block(header, txs, 0)

    def default_mainnet(self) -> 'AdvancedGenesisConfig':
        """Build default mainnet genesis."""
        self.add_allocation(FOUNDATION_ADDRESS, 1_000_000)
        self.add_vesting(FOUNDATION_ADDRESS, 10_000_000, 365, 1460)
        for seed in SEED_NODES:
            if seed:
                self.add_validator(seed)
        return self

    def genesis_info(self) -> dict:
        total = sum(self.allocations.values())
        return {
            "allocations":  len(self.allocations),
            "total_genesis": f"{total/10**DECIMALS:.3f} NBL",
            "vestings":      len(self.vesting_schedules),
            "validators":    len(self.initial_validators),
            "timestamp":     self.timestamp,
        }


# ---- PrivacyTransaction
class PrivacyTransaction:
    """
    Enhanced privacy transaction using RingCT-inspired approach.
    Hides sender, receiver, and amount simultaneously.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._ring_txs: List[dict] = []
        self._lock   = threading.RLock()

    def create_ring_tx(self, sender: str, recipient: str,
                        amount: int, ring_size: int = 11) -> dict:
        """Create a ring-signature style private transaction."""
        # Decoys from UTXO set (simplified)
        all_addrs  = list(self._bc.utxo._addr_idx.keys())
        decoys     = [a for a in all_addrs
                      if a != sender][:ring_size - 1]
        ring       = decoys + [sender]
        import random; random.shuffle(ring)
        # Pedersen commitment to amount
        blinding   = secrets.randbelow(Secp256k1.ORDER)
        commitment = PedersenCommitment.commit(amount, blinding)
        # Key image (one-time) to prevent double-spend
        key_image  = hashlib.sha256(
            sender.encode() + amount.to_bytes(8, 'big')
        ).hexdigest()
        tx = {
            "tx_id":      hashlib.sha256(
                f"{sender}{recipient}{amount}{time.time()}".encode()
            ).hexdigest()[:16],
            "ring":       ring,
            "ring_size":  len(ring),
            "commitment": [c % (2**32) for c in commitment],
            "key_image":  key_image,
            "recipient":  hashlib.sha256(recipient.encode()).hexdigest()[:16],
            "amount":     "hidden",
        }
        with self._lock:
            self._ring_txs.append(tx)
        return tx

    def privacy_stats(self) -> dict:
        return {
            "ring_txs":    len(self._ring_txs),
            "default_ring_size": 11,
            "privacy_level": "HIGH",
        }


# ---- LiquidityProvisionManager
class LiquidityProvisionManager:
    """
    Manages LP positions across all NEBULA pools.
    Tracks impermanent loss, fees earned, optimal entry.
    """

    def __init__(self, dex: 'NEBULADex',
                  oracle: 'OracleV2' = None):
        self._dex    = dex
        self._oracle = oracle
        self._positions: Dict[str, List[dict]] = {}
        self._lock   = threading.RLock()

    def add_lp_position(self, owner: str, pool_id: str,
                         token_a: str, token_b: str,
                         amount_a: float, amount_b: float,
                         lp_tokens: float) -> str:
        with self._lock:
            pool = self._dex._pools.get(pool_id)
            entry_price = (pool.reserve_b / pool.reserve_a
                           if pool and pool.reserve_a > 0 else 1.0)
            pid = hashlib.sha256(
                f"LP:{owner}:{pool_id}:{time.time()}".encode()
            ).hexdigest()[:12]
            if owner not in self._positions:
                self._positions[owner] = []
            self._positions[owner].append({
                "pos_id":      pid,
                "pool_id":     pool_id,
                "token_a":     token_a,
                "token_b":     token_b,
                "amount_a":    amount_a,
                "amount_b":    amount_b,
                "lp_tokens":   lp_tokens,
                "entry_price": entry_price,
                "entered_at":  time.time(),
            })
            return pid

    def il_for_position(self, owner: str, pos_id: str) -> dict:
        with self._lock:
            positions = self._positions.get(owner, [])
        pos = next((p for p in positions if p["pos_id"] == pos_id), None)
        if not pos:
            return {}
        pool = self._dex._pools.get(pos["pool_id"])
        if not pool or pool.reserve_a == 0:
            return {"il": "N/A"}
        current_price = pool.reserve_b / pool.reserve_a
        entry_price   = pos["entry_price"]
        il = impermanent_loss(entry_price, current_price)
        return {
            "pos_id":        pos_id,
            "entry_price":   f"{entry_price:.6f}",
            "current_price": f"{current_price:.6f}",
            "il_pct":        f"{il:.4f}%",
        }

    def all_positions(self, owner: str) -> List[dict]:
        with self._lock:
            positions = self._positions.get(owner, [])
        results = []
        for pos in positions:
            il = self.il_for_position(owner, pos["pos_id"])
            results.append({**pos, "il": il.get("il_pct", "N/A")})
        return results


# ---- ContractAuditor
class ContractAuditor:
    """
    Static analysis and audit tool for NEBULA smart contracts.
    """

    VULNERABILITY_PATTERNS = {
        "reentrancy":      ["call", "send", "transfer"],
        "overflow":        ["__add__", "__mul__", "+", "*"],
        "unchecked_return": ["ok, _"],
        "hardcoded_addr":  ["FOUNDATION_ADDRESS", "0x"],
    }

    def __init__(self):
        self._audits: List[dict] = []

    def audit_code(self, contract_name: str,
                    source_code: str) -> dict:
        findings = []
        lines    = source_code.split("\n")
        for i, line in enumerate(lines):
            for vuln, patterns in self.VULNERABILITY_PATTERNS.items():
                for pat in patterns:
                    if pat in line:
                        findings.append({
                            "line":        i + 1,
                            "severity":    "INFO",
                            "type":        vuln,
                            "description": f"Pattern '{pat}' found",
                            "code":        line.strip()[:100],
                        })
        score = max(0, 100 - len(findings) * 5)
        audit = {
            "contract":   contract_name,
            "score":      score,
            "grade":      ("A" if score >= 90 else "B" if score >= 80
                           else "C" if score >= 70 else "D"),
            "findings":   findings,
            "lines":      len(lines),
            "audited_at": time.time(),
        }
        self._audits.append(audit)
        return audit

    def audit_history(self) -> List[dict]:
        return [{"contract": a["contract"], "score": a["score"],
                 "grade": a["grade"]} for a in self._audits]


# ---- EcosystemGrantProgram
class EcosystemGrantProgram:
    """
    NEBULA foundation ecosystem grant program.
    Funds projects building on NEBULA.
    """

    GRANT_ROUNDS: List[dict] = [
        {"round": 1, "budget": 100_000, "focus": "Infrastructure"},
        {"round": 2, "budget": 200_000, "focus": "DeFi Applications"},
        {"round": 3, "budget": 150_000, "focus": "NFT & Gaming"},
        {"round": 4, "budget": 250_000, "focus": "Layer-2 Solutions"},
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._grantees: List[dict] = []
        self._round     = 1
        self._lock      = threading.RLock()

    def apply(self, applicant: str, project_name: str,
               category: str, amount_nbl: float,
               description: str, milestones: List[str]) -> str:
        with self._lock:
            gid = hashlib.sha256(
                f"GRANT:{applicant}:{project_name}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._grantees.append({
                "grant_id":   gid,
                "applicant":  applicant,
                "project":    project_name,
                "category":   category,
                "amount":     amount_nbl,
                "description": description,
                "milestones": milestones,
                "round":      self._round,
                "status":     "reviewing",
            })
            return gid

    def approve(self, grant_id: str) -> bool:
        with self._lock:
            g = next((g for g in self._grantees
                      if g["grant_id"] == grant_id), None)
            if g:
                g["status"] = "approved"
                return True
            return False

    def program_stats(self) -> dict:
        with self._lock:
            approved = sum(1 for g in self._grantees if g["status"] == "approved")
            total_nbl = sum(g["amount"] for g in self._grantees
                            if g["status"] == "approved")
        return {
            "total_applications": len(self._grantees),
            "approved":           approved,
            "total_funded_nbl":   f"{total_nbl:.3f}",
            "current_round":      self._round,
            "rounds":             self.GRANT_ROUNDS,
        }


# ---- OrderBookV2
class OrderBookV2:
    """
    Enhanced order book v2 with partial fills and order matching.
    """

    def __init__(self, pair: str):
        self.pair    = pair
        self._bids: List[Tuple[float, float, str]] = []  # (price, qty, order_id)
        self._asks: List[Tuple[float, float, str]] = []
        self._fills: List[dict] = []
        self._lock  = threading.RLock()

    def place_limit(self, side: str, price: float,
                     qty: float, trader: str) -> str:
        with self._lock:
            oid = hashlib.sha256(
                f"OBV2:{side}:{price}:{qty}:{time.time()}".encode()
            ).hexdigest()[:10]
            entry = (price, qty, oid)
            if side == "buy":
                self._bids.append(entry)
                self._bids.sort(key=lambda x: -x[0])
            else:
                self._asks.append(entry)
                self._asks.sort(key=lambda x: x[0])
            self._try_match()
            return oid

    def _try_match(self):
        while self._bids and self._asks:
            b_price, b_qty, b_id = self._bids[0]
            a_price, a_qty, a_id = self._asks[0]
            if b_price < a_price:
                break
            fill_qty = min(b_qty, a_qty)
            fill_price = (b_price + a_price) / 2
            self._fills.append({
                "bid_id":    b_id,
                "ask_id":    a_id,
                "price":     fill_price,
                "qty":       fill_qty,
                "ts":        time.time(),
            })
            if b_qty <= a_qty:
                self._bids.pop(0)
            else:
                self._bids[0] = (b_price, b_qty - fill_qty, b_id)
            if a_qty <= b_qty:
                self._asks.pop(0)
            else:
                self._asks[0] = (a_price, a_qty - fill_qty, a_id)

    def best_bid(self) -> Optional[float]:
        return self._bids[0][0] if self._bids else None

    def best_ask(self) -> Optional[float]:
        return self._asks[0][0] if self._asks else None

    def spread(self) -> Optional[float]:
        b, a = self.best_bid(), self.best_ask()
        return a - b if b and a else None

    def ob_stats(self) -> dict:
        with self._lock:
            return {
                "pair":    self.pair,
                "bids":    len(self._bids),
                "asks":    len(self._asks),
                "fills":   len(self._fills),
                "spread":  f"{self.spread():.6f}" if self.spread() else "N/A",
                "mid":     f"{((self.best_bid() or 0)+(self.best_ask() or 0))/2:.6f}",
            }


# ---- ValidatorSlashingCondition
class ValidatorSlashingCondition(_enum.Enum):
    DOUBLE_SIGN   = "double_sign"
    DOWNTIME      = "downtime"
    INVALID_BLOCK = "invalid_block"
    EQUIVOCATION  = "equivocation"


# ---- SlashingEngine
class SlashingEngine:
    """Slashes misbehaving validators in NEBULA PoS."""

    SLASH_RATES = {
        ValidatorSlashingCondition.DOUBLE_SIGN:   0.50,   # 50% stake slashed
        ValidatorSlashingCondition.DOWNTIME:      0.01,   # 1%
        ValidatorSlashingCondition.INVALID_BLOCK: 0.30,
        ValidatorSlashingCondition.EQUIVOCATION:  0.05,
    }
    JAILBREAK_BLOCKS = 10_000

    def __init__(self, blockchain: 'NEBULABlockchain',
                  validator_set: 'ValidatorSetManager'):
        self._bc      = blockchain
        self._vs      = validator_set
        self._slashes: List[dict] = []
        self._jailed:  Dict[str, int] = {}
        self._lock     = threading.RLock()

    def slash(self, validator: str,
               condition: ValidatorSlashingCondition,
               evidence: str = "") -> Tuple[bool, int]:
        with self._lock:
            info = self._vs.get_validator(validator)
            if not info:
                return False, 0
            rate    = self.SLASH_RATES.get(condition, 0.01)
            stake   = info.get("stake", 0)
            slashed = int(stake * rate)
            self._slashes.append({
                "validator": validator,
                "condition": condition.value,
                "slashed":   slashed,
                "block":     self._bc.height,
                "evidence":  evidence,
            })
            self._jailed[validator] = (
                self._bc.height + self.JAILBREAK_BLOCKS)
            return True, slashed

    def is_jailed(self, validator: str) -> bool:
        return (self._bc.height < self._jailed.get(validator, 0))

    def unjail(self, validator: str) -> bool:
        with self._lock:
            if not self.is_jailed(validator):
                return False
            del self._jailed[validator]
            return True

    def slashing_stats(self) -> dict:
        with self._lock:
            total_slashed = sum(s["slashed"] for s in self._slashes)
        return {
            "total_slashes":   len(self._slashes),
            "jailed":          len(self._jailed),
            "total_slashed_nbl": f"{total_slashed/10**DECIMALS:.3f}",
        }


# ---- NotificationType
class NotificationType(_enum.Enum):
    TX_RECEIVED      = "tx_received"
    TX_CONFIRMED     = "tx_confirmed"
    PRICE_ALERT      = "price_alert"
    GOVERNANCE_VOTE  = "governance_vote"
    LIQUIDATION_WARN = "liquidation_warning"
    STAKING_REWARD   = "staking_reward"
    BRIDGE_COMPLETE  = "bridge_complete"


# ---- Notification
@dataclass
class Notification:
    notif_id:  str
    user:      str
    notif_type: NotificationType
    title:     str
    message:   str
    read:      bool = False
    ts:        float = 0.0

    def __post_init__(self):
        if not self.ts:
            self.ts = time.time()
        if not self.notif_id:
            self.notif_id = secrets.token_hex(8)


# ---- NotificationSystem
class NotificationSystem:
    """Push notification system for NEBULA users."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._notifs: Dict[str, List[Notification]] = {}
        self._prefs:  Dict[str, Set[NotificationType]] = {}
        self._lock    = threading.RLock()

    def subscribe(self, user: str,
                   notif_types: List[NotificationType]):
        with self._lock:
            self._prefs[user] = set(notif_types)

    def push(self, user: str,
              notif_type: NotificationType,
              title: str, message: str) -> bool:
        with self._lock:
            if user in self._prefs and \
               notif_type not in self._prefs[user]:
                return False
            if user not in self._notifs:
                self._notifs[user] = []
            notif = Notification(
                notif_id   = secrets.token_hex(8),
                user       = user,
                notif_type = notif_type,
                title      = title,
                message    = message,
            )
            self._notifs[user].append(notif)
            return True

    def get_unread(self, user: str) -> List[dict]:
        with self._lock:
            notifs = self._notifs.get(user, [])
        return [
            {"id": n.notif_id, "type": n.notif_type.value,
             "title": n.title, "message": n.message, "ts": n.ts}
            for n in notifs if not n.read
        ]

    def mark_read(self, user: str, notif_id: str) -> bool:
        with self._lock:
            for n in self._notifs.get(user, []):
                if n.notif_id == notif_id:
                    n.read = True
                    return True
            return False

    def notif_stats(self) -> dict:
        with self._lock:
            total = sum(len(v) for v in self._notifs.values())
        return {
            "users":       len(self._notifs),
            "total_notifs": total,
        }


# ---- Epoch
class Epoch:
    """Represents a NEBULA epoch (period of blocks)."""

    def __init__(self, epoch_num: int, start_block: int,
                  duration: int = 2016):
        self.epoch_num   = epoch_num
        self.start_block = start_block
        self.end_block   = start_block + duration - 1
        self.duration    = duration
        self.rewards_distributed = 0
        self.txs_processed      = 0
        self.started_at          = time.time()

    def is_active(self, height: int) -> bool:
        return self.start_block <= height <= self.end_block

    def progress(self, height: int) -> float:
        if height < self.start_block:
            return 0.0
        return min(1.0, (height - self.start_block + 1) / self.duration)

    def to_dict(self) -> dict:
        return {
            "epoch":       self.epoch_num,
            "start":       self.start_block,
            "end":         self.end_block,
            "duration":    self.duration,
            "rewards_nbl": f"{self.rewards_distributed/10**DECIMALS:.3f}",
        }
