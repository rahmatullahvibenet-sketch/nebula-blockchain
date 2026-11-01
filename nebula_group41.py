"""NEBULA group41 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. OptionsContract  (orig. lines 67826-67864)
   2. OptionsMarket  (orig. lines 67866-67964)
   3. FuturesPosition  (orig. lines 67971-68000)
   4. PerpetualFuturesMarket  (orig. lines 68002-68087)
   5. ReferralProgram  (orig. lines 68094-68165)
   6. GrantStatus  (orig. lines 68172-68178)
   7. GrantProposal  (orig. lines 68180-68205)
   8. GovernanceTreasuryV2  (orig. lines 68207-68319)
   9. AIOracle  (orig. lines 68425-68497)
  10. SyncCheckpoint  (orig. lines 68592-68601)
  11. NodeSyncV2  (orig. lines 68603-68650)
  12. LiquidityMiningProgram  (orig. lines 68657-68732)
  13. NFTStakingPool  (orig. lines 68739-68784)
  14. NFTStakingManager  (orig. lines 68786-68822)
  15. CollateralType  (orig. lines 68829-68837)
  16. MultiCollateralStablecoin  (orig. lines 68839-68925)
  17. AirdropCampaign  (orig. lines 68932-68972)
  18. AirdropManager  (orig. lines 68974-69015)
  19. DeFiStrategy  (orig. lines 69022-69033)
  20. ArbitrageStrategy  (orig. lines 69036-69073)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): OptionType
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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- OptionsContract
@dataclass
class OptionsContract:
    contract_id:  str
    underlying:   str       # e.g. "NBL/USD"
    option_type:  OptionType
    strike_price: float
    expiry_block: int
    premium:      float
    size:         float     # contract size in NBL
    writer:       str
    buyer:        str = ""
    exercised:    bool = False
    expired:      bool = False

    def is_in_the_money(self, current_price: float) -> bool:
        if self.option_type == OptionType.CALL:
            return current_price > self.strike_price
        else:
            return current_price < self.strike_price

    def intrinsic_value(self, current_price: float) -> float:
        if self.option_type == OptionType.CALL:
            return max(0, current_price - self.strike_price) * self.size
        else:
            return max(0, self.strike_price - current_price) * self.size

    def to_dict(self) -> dict:
        return {
            "contract_id":  self.contract_id,
            "underlying":   self.underlying,
            "type":         self.option_type.value,
            "strike":       f"{self.strike_price:.4f}",
            "expiry_block": self.expiry_block,
            "premium":      f"{self.premium:.6f} NBL",
            "size":         f"{self.size:.4f} NBL",
            "writer":       self.writer,
            "buyer":        self.buyer,
            "exercised":    self.exercised,
        }


# ---- OptionsMarket
class OptionsMarket:
    """
    Decentralized options market for NEBULA.
    European-style options on NBL and other assets.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc        = blockchain
        self._oracle    = oracle
        self._contracts: Dict[str, OptionsContract] = {}
        self._lock      = threading.RLock()

    def write_option(self, writer: str, underlying: str,
                      option_type: OptionType,
                      strike: float, expiry_days: int,
                      premium: float, size: float) -> Tuple[bool, str]:
        with self._lock:
            collateral = int(size * 10**DECIMALS)
            if self._bc.utxo.balance(writer) < collateral:
                return False, "Insufficient collateral"
            expiry_block = self._bc.height + expiry_days * 144
            cid = hashlib.sha256(
                f"OPT:{writer}:{underlying}:{strike}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._contracts[cid] = OptionsContract(
                contract_id  = cid,
                underlying   = underlying,
                option_type  = option_type,
                strike_price = strike,
                expiry_block = expiry_block,
                premium      = premium,
                size         = size,
                writer       = writer,
            )
            return True, cid

    def buy_option(self, buyer: str,
                    contract_id: str) -> Tuple[bool, str]:
        with self._lock:
            opt = self._contracts.get(contract_id)
            if not opt or opt.buyer:
                return False, "Not available"
            if self._bc.height >= opt.expiry_block:
                opt.expired = True
                return False, "Option expired"
            premium_raw = int(opt.premium * 10**DECIMALS)
            if self._bc.utxo.balance(buyer) < premium_raw:
                return False, "Insufficient premium"
            opt.buyer = buyer
            return True, f"Bought {opt.option_type.value} option on {opt.underlying}"

    def exercise(self, buyer: str,
                  contract_id: str) -> Tuple[bool, float]:
        with self._lock:
            opt = self._contracts.get(contract_id)
            if not opt or opt.buyer != buyer:
                return False, 0.0
            if opt.exercised or opt.expired:
                return False, 0.0
            if self._bc.height >= opt.expiry_block:
                opt.expired = True
                return False, 0.0
            price = (self._oracle.price(opt.underlying)
                     if self._oracle else opt.strike_price) or opt.strike_price
            if not opt.is_in_the_money(price):
                return False, 0.0
            payout = opt.intrinsic_value(price)
            opt.exercised = True
            return True, payout

    def expire_contracts(self) -> int:
        cur     = self._bc.height
        expired = 0
        with self._lock:
            for opt in self._contracts.values():
                if not opt.expired and not opt.exercised and cur >= opt.expiry_block:
                    opt.expired = True
                    expired    += 1
        return expired

    def open_contracts(self) -> List[dict]:
        cur = self._bc.height
        return [opt.to_dict() for opt in self._contracts.values()
                if not opt.expired and not opt.exercised
                and cur < opt.expiry_block]

    def options_stats(self) -> dict:
        with self._lock:
            total     = len(self._contracts)
            open_c    = sum(1 for o in self._contracts.values()
                            if not o.expired and not o.exercised)
            exercised = sum(1 for o in self._contracts.values() if o.exercised)
        return {
            "total_contracts": total,
            "open":            open_c,
            "exercised":       exercised,
            "expired":         total - open_c - exercised,
        }


# ---- FuturesPosition
@dataclass
class FuturesPosition:
    pos_id:       str
    trader:       str
    pair:         str
    side:         str        # "long" or "short"
    size:         float
    entry_price:  float
    funding_rate: float = 0.001   # 0.1% per 8 hours
    collateral:   float = 0.0
    unrealized_pnl: float = 0.0
    open:         bool = True

    def update(self, mark_price: float, funding_payment: float = 0):
        if self.side == "long":
            self.unrealized_pnl = (mark_price - self.entry_price) * self.size - funding_payment
        else:
            self.unrealized_pnl = (self.entry_price - mark_price) * self.size - funding_payment

    def to_dict(self) -> dict:
        return {
            "pos_id":    self.pos_id,
            "trader":    self.trader,
            "pair":      self.pair,
            "side":      self.side,
            "size":      f"{self.size:.4f}",
            "entry":     f"{self.entry_price:.4f}",
            "pnl":       f"{self.unrealized_pnl:.4f}",
            "open":      self.open,
        }


# ---- PerpetualFuturesMarket
class PerpetualFuturesMarket:
    """
    Perpetual futures market for NEBULA.
    No expiry — uses funding rate to anchor to spot price.
    """

    FUNDING_INTERVAL_BLOCKS = 1200    # ~8 hours (1200 * 400s)
    MAX_LEVERAGE = 20

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc        = blockchain
        self._oracle    = oracle
        self._positions: Dict[str, FuturesPosition] = {}
        self._mark_prices: Dict[str, float]         = {}
        self._last_funding_block: int               = 0
        self._lock      = threading.RLock()

    def open(self, trader: str, pair: str, side: str,
              size: float, leverage: float,
              collateral_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            if leverage > self.MAX_LEVERAGE:
                return False, f"Max leverage: {self.MAX_LEVERAGE}x"
            collateral_raw = int(collateral_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(trader) < collateral_raw:
                return False, "Insufficient collateral"
            mark_price = (self._oracle.price(pair)
                          if self._oracle else 1.0) or 1.0
            pid = hashlib.sha256(
                f"PERP:{trader}:{pair}:{side}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._positions[pid] = FuturesPosition(
                pos_id      = pid,
                trader      = trader,
                pair        = pair,
                side        = side,
                size        = size,
                entry_price = mark_price,
                collateral  = collateral_nbl,
            )
            return True, pid

    def close(self, pos_id: str, trader: str) -> Tuple[bool, float]:
        with self._lock:
            pos = self._positions.get(pos_id)
            if not pos or pos.trader != trader or not pos.open:
                return False, 0.0
            mark = (self._oracle.price(pos.pair)
                    if self._oracle else pos.entry_price) or pos.entry_price
            pos.update(mark)
            pos.open = False
            return True, pos.unrealized_pnl

    def process_funding(self) -> dict:
        """Process funding payments for all open positions."""
        cur = self._bc.height
        if cur - self._last_funding_block < self.FUNDING_INTERVAL_BLOCKS:
            return {"funding_processed": False}
        payments = {}
        with self._lock:
            for pid, pos in self._positions.items():
                if not pos.open:
                    continue
                mark  = (self._oracle.price(pos.pair)
                         if self._oracle else pos.entry_price) or pos.entry_price
                fund  = pos.size * pos.entry_price * pos.funding_rate
                fund  = fund if pos.side == "long" else -fund
                pos.update(mark, fund)
                payments[pid] = fund
            self._last_funding_block = cur
        return {"funding_processed": True, "payments": len(payments)}

    def futures_stats(self) -> dict:
        with self._lock:
            open_p   = sum(1 for p in self._positions.values() if p.open)
            oi_long  = sum(p.size * p.entry_price for p in self._positions.values()
                           if p.open and p.side == "long")
            oi_short = sum(p.size * p.entry_price for p in self._positions.values()
                           if p.open and p.side == "short")
        return {
            "open_positions": open_p,
            "oi_long":        f"{oi_long:.3f}",
            "oi_short":       f"{oi_short:.3f}",
            "funding_rate":   "0.1%/8h",
        }


# ---- ReferralProgram
class ReferralProgram:
    """
    On-chain referral program for NEBULA ecosystem.
    Earn commissions by referring new users.
    """

    REFERRAL_PCT   = 0.10    # 10% of referee's fees
    MAX_DEPTH      = 3       # 3-level referral tree

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._referrals:  Dict[str, str]      = {}   # referee -> referrer
        self._earnings:   Dict[str, int]      = {}   # referrer -> total earned
        self._tree:       Dict[str, List[str]] = {}  # referrer -> [referees]
        self._lock        = threading.RLock()

    def register(self, referee: str,
                  referrer: str) -> Tuple[bool, str]:
        with self._lock:
            if referee in self._referrals:
                return False, "Already referred"
            if referee == referrer:
                return False, "Cannot refer yourself"
            self._referrals[referee] = referrer
            if referrer not in self._tree:
                self._tree[referrer] = []
            self._tree[referrer].append(referee)
            return True, f"Registered referral: {referee} → {referrer}"

    def record_fee(self, payer: str, fee: int):
        """Record a fee payment and distribute referral commissions."""
        with self._lock:
            referrer = self._referrals.get(payer)
            depth    = 0
            rate     = self.REFERRAL_PCT
            while referrer and depth < self.MAX_DEPTH:
                commission = int(fee * rate)
                self._earnings[referrer] = (
                    self._earnings.get(referrer, 0) + commission)
                referrer = self._referrals.get(referrer)
                depth   += 1
                rate    *= 0.5   # halve at each level

    def claim(self, referrer: str) -> Tuple[bool, int]:
        with self._lock:
            earned = self._earnings.get(referrer, 0)
            if earned == 0:
                return False, 0
            self._earnings[referrer] = 0
            return True, earned

    def referral_tree(self, referrer: str,
                       depth: int = 0) -> dict:
        referees = self._tree.get(referrer, [])
        return {
            "address":  referrer,
            "referees": len(referees),
            "earned":   f"{self._earnings.get(referrer, 0)/10**DECIMALS:.6f} NBL",
            "sub_tree": [self.referral_tree(r, depth+1)
                          for r in referees[:5]]  # limit to 5 to avoid deep recursion
            if depth < 2 else [],
        }

    def stats(self) -> dict:
        with self._lock:
            total_refs   = len(self._referrals)
            total_earned = sum(self._earnings.values())
        return {
            "total_referrals": total_refs,
            "total_earned_nbl": f"{total_earned/10**DECIMALS:.6f}",
            "referral_pct":    f"{self.REFERRAL_PCT*100:.0f}%",
        }


# ---- GrantStatus
class GrantStatus(_enum.Enum):
    PROPOSED   = "proposed"
    APPROVED   = "approved"
    FUNDED     = "funded"
    MILESTONED = "milestoned"
    COMPLETED  = "completed"
    REJECTED   = "rejected"


# ---- GrantProposal
@dataclass
class GrantProposal:
    proposal_id: str
    applicant:   str
    title:       str
    description: str
    amount_nbl:  float
    milestones:  List[dict]
    category:    str
    status:      GrantStatus = GrantStatus.PROPOSED
    votes_yes:   float = 0.0
    votes_no:    float = 0.0
    paid:        float = 0.0

    def to_dict(self) -> dict:
        return {
            "id":          self.proposal_id,
            "title":       self.title,
            "applicant":   self.applicant,
            "amount_nbl":  self.amount_nbl,
            "status":      self.status.value,
            "milestones":  len(self.milestones),
            "category":    self.category,
            "yes_votes":   f"{self.votes_yes:.1f}",
            "no_votes":    f"{self.votes_no:.1f}",
        }


# ---- GovernanceTreasuryV2
class GovernanceTreasuryV2:
    """
    Enhanced governance-controlled treasury v2.
    Milestone-based grant disbursement, multi-category budgets.
    """

    CATEGORIES = {
        "development":   0.35,
        "marketing":     0.15,
        "community":     0.15,
        "security":      0.15,
        "research":      0.10,
        "infrastructure": 0.10,
    }
    GRANT_QUORUM    = 0.10
    GRANT_THRESHOLD = 0.60

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._grants:  Dict[str, GrantProposal] = {}
        self._voters:  Dict[str, Set[str]]      = {}   # grant_id -> {voters}
        self._balance: int = 0
        self._lock     = threading.RLock()

    def deposit(self, amount: int):
        with self._lock:
            self._balance += amount

    def submit_grant(self, applicant: str, title: str,
                      description: str, amount_nbl: float,
                      category: str,
                      milestones: List[dict]) -> Tuple[bool, str]:
        with self._lock:
            if category not in self.CATEGORIES:
                return False, f"Invalid category. Use: {list(self.CATEGORIES.keys())}"
            gid = hashlib.sha256(
                f"GRANT_V2:{applicant}:{title}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._grants[gid] = GrantProposal(
                proposal_id = gid,
                applicant   = applicant,
                title       = title,
                description = description,
                amount_nbl  = amount_nbl,
                milestones  = milestones,
                category    = category,
            )
            self._voters[gid] = set()
            return True, gid

    def vote_on_grant(self, voter: str, grant_id: str,
                       support: bool) -> Tuple[bool, str]:
        with self._lock:
            grant = self._grants.get(grant_id)
            if not grant or grant.status != GrantStatus.PROPOSED:
                return False, "Not in voting phase"
            if voter in self._voters[grant_id]:
                return False, "Already voted"
            weight = self._bc.utxo.balance(voter) / 10**DECIMALS
            if support:
                grant.votes_yes += weight
            else:
                grant.votes_no  += weight
            self._voters[grant_id].add(voter)
            return True, f"Voted {'yes' if support else 'no'} (weight: {weight:.2f})"

    def finalize_vote(self, grant_id: str) -> Tuple[bool, str]:
        with self._lock:
            grant = self._grants.get(grant_id)
            if not grant:
                return False, "Not found"
            total = grant.votes_yes + grant.votes_no
            pct   = grant.votes_yes / total if total > 0 else 0
            if pct >= self.GRANT_THRESHOLD:
                grant.status = GrantStatus.APPROVED
                return True, f"Grant APPROVED ({pct*100:.1f}% yes)"
            else:
                grant.status = GrantStatus.REJECTED
                return False, f"Grant REJECTED ({pct*100:.1f}% yes)"

    def release_milestone(self, grant_id: str,
                           milestone_idx: int) -> Tuple[bool, float]:
        with self._lock:
            grant = self._grants.get(grant_id)
            if not grant or grant.status != GrantStatus.APPROVED:
                return False, 0.0
            if milestone_idx >= len(grant.milestones):
                return False, 0.0
            ms     = grant.milestones[milestone_idx]
            amount = float(ms.get("amount", 0))
            if amount > self._balance / 10**DECIMALS:
                return False, 0.0
            self._balance -= int(amount * 10**DECIMALS)
            grant.paid    += amount
            grant.status   = (GrantStatus.COMPLETED
                               if grant.paid >= grant.amount_nbl
                               else GrantStatus.MILESTONED)
            return True, amount

    def treasury_v2_stats(self) -> dict:
        with self._lock:
            by_status = {}
            for g in self._grants.values():
                k = g.status.value
                by_status[k] = by_status.get(k, 0) + 1
            total_requested = sum(g.amount_nbl for g in self._grants.values())
        return {
            "balance_nbl":      f"{self._balance/10**DECIMALS:.3f}",
            "grants":           len(self._grants),
            "by_status":        by_status,
            "total_requested":  f"{total_requested:.3f} NBL",
            "categories":       self.CATEGORIES,
        }


# ---- AIOracle
class AIOracle:
    """
    AI-enhanced oracle for NEBULA.
    Combines multiple data sources with ML-based outlier detection.
    Provides sentiment analysis, trend prediction.
    """

    def __init__(self, oracle: 'OracleV2'):
        self._oracle    = oracle
        self._price_history: Dict[str, List[float]] = {}
        self._sentiment: Dict[str, float]           = {}   # 1 to +1
        self._predictions: Dict[str, dict]          = {}

    def record_price(self, pair: str, price: float):
        if pair not in self._price_history:
            self._price_history[pair] = []
        self._price_history[pair].append(price)
        if len(self._price_history[pair]) > 1000:
            self._price_history[pair].pop(0)
        self._update_prediction(pair)

    def _update_prediction(self, pair: str):
        history = self._price_history.get(pair, [])
        if len(history) < 10:
            return
        recent  = history[-10:]
        trend   = (recent[-1] - recent[0]) / recent[0] if recent[0] > 0 else 0
        vol     = self._std_dev(recent) / self._mean(recent) if recent else 0
        self._predictions[pair] = {
            "trend":      f"{trend*100:+.2f}%",
            "volatility": f"{vol*100:.2f}%",
            "direction":  "up" if trend > 0.01 else "down" if trend < -0.01 else "sideways",
            "confidence": min(100, len(history) / 10),
        }

    def _mean(self, data: List[float]) -> float:
        return sum(data) / len(data) if data else 0

    def _std_dev(self, data: List[float]) -> float:
        if len(data) < 2:
            return 0
        m   = self._mean(data)
        var = sum((x - m) ** 2 for x in data) / len(data)
        return var ** 0.5

    def update_sentiment(self, pair: str,
                          sentiment: float):
        """Update sentiment score (-1=bearish, +1=bullish)."""
        self._sentiment[pair] = max(-1.0, min(1.0, sentiment))

    def get_signal(self, pair: str) -> dict:
        """Get composite trading signal."""
        pred  = self._predictions.get(pair, {})
        sent  = self._sentiment.get(pair, 0.0)
        price = self._oracle.latest(pair) or 0
        signal = "NEUTRAL"
        if sent > 0.3 and pred.get("direction") == "up":
            signal = "BUY"
        elif sent < -0.3 and pred.get("direction") == "down":
            signal = "SELL"
        return {
            "pair":       pair,
            "price":      price,
            "signal":     signal,
            "sentiment":  f"{sent:+.2f}",
            "prediction": pred,
        }

    def price_prediction_summary(self) -> dict:
        return {
            "pairs_tracked": len(self._price_history),
            "predictions":   self._predictions,
        }


# ---- SyncCheckpoint
class SyncCheckpoint:
    """A trusted sync checkpoint."""

    def __init__(self, height: int, hash_: str,
                  utxo_hash: str, trusted: bool = True):
        self.height    = height
        self.hash      = hash_
        self.utxo_hash = utxo_hash
        self.trusted   = trusted
        self.added_at  = time.time()


# ---- NodeSyncV2
class NodeSyncV2:
    """
    Advanced node synchronization with snapshot sync.
    Supports fast sync via trusted checkpoints.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._checkpoints: Dict[int, SyncCheckpoint] = {}
        self._sync_peers:  List[str]                 = []
        self._sync_start  = time.time()
        self._synced      = False

    def add_checkpoint(self, height: int, hash_: str,
                        utxo_hash: str):
        self._checkpoints[height] = SyncCheckpoint(height, hash_, utxo_hash)

    def verify_at_height(self, height: int) -> Tuple[bool, str]:
        cp = self._checkpoints.get(height)
        if not cp:
            return True, "No checkpoint"
        blk = self._bc.get_block(height)
        if not blk:
            return False, f"Block {height} not found"
        if blk.hash != cp.hash:
            return False, f"Block hash mismatch at {height}"
        return True, f"Checkpoint {height} verified"

    def sync_status(self) -> dict:
        return {
            "synced":       self._synced,
            "height":       self._bc.height,
            "checkpoints":  len(self._checkpoints),
            "sync_peers":   len(self._sync_peers),
            "elapsed_secs": f"{time.time()-self._sync_start:.0f}",
        }

    def estimate_sync_time(self, blocks_remaining: int,
                            sync_rate_bps: float = 100) -> str:
        if sync_rate_bps <= 0:
            return "unknown"
        secs = blocks_remaining / sync_rate_bps
        if secs < 60:
            return f"{secs:.0f}s"
        elif secs < 3600:
            return f"{secs/60:.0f}m"
        else:
            return f"{secs/3600:.1f}h"


# ---- LiquidityMiningProgram
class LiquidityMiningProgram:
    """
    Liquidity mining program — rewards LPs with NBL tokens.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  total_rewards: float,
                  duration_blocks: int):
        self._bc              = blockchain
        self.total_rewards    = int(total_rewards * 10**DECIMALS)
        self.duration_blocks  = duration_blocks
        self.start_block      = blockchain.height
        self.end_block        = blockchain.height + duration_blocks
        self.rewards_per_block = self.total_rewards // duration_blocks
        self._lp_stakes:  Dict[str, int]   = {}   # addr -> LP tokens staked
        self._claimed:    Dict[str, int]   = {}   # addr -> rewards claimed
        self._last_block: Dict[str, int]   = {}   # addr -> last claim block
        self._total_lp    = 0

    def stake_lp(self, address: str,
                  lp_amount: int) -> Tuple[bool, str]:
        self._lp_stakes[address]  = self._lp_stakes.get(address, 0) + lp_amount
        self._total_lp           += lp_amount
        self._last_block[address] = self._bc.height
        return True, f"Staked {lp_amount} LP tokens"

    def unstake_lp(self, address: str,
                    lp_amount: int) -> Tuple[bool, str]:
        staked = self._lp_stakes.get(address, 0)
        if staked < lp_amount:
            return False, "Insufficient staked LP"
        # Auto-claim pending rewards
        self._claim_pending(address)
        self._lp_stakes[address] -= lp_amount
        self._total_lp           -= lp_amount
        return True, f"Unstaked {lp_amount} LP tokens"

    def _claim_pending(self, address: str) -> int:
        cur       = min(self._bc.height, self.end_block)
        last      = self._last_block.get(address, self.start_block)
        blocks    = cur - last
        staked    = self._lp_stakes.get(address, 0)
        if blocks <= 0 or staked == 0 or self._total_lp == 0:
            return 0
        share   = staked / self._total_lp
        reward  = int(blocks * self.rewards_per_block * share)
        self._claimed[address]    = self._claimed.get(address, 0) + reward
        self._last_block[address] = cur
        return reward

    def claim_rewards(self, address: str) -> Tuple[bool, int]:
        reward = self._claim_pending(address)
        if reward == 0:
            return False, 0
        return True, reward

    def pending_rewards(self, address: str) -> int:
        cur    = min(self._bc.height, self.end_block)
        last   = self._last_block.get(address, self.start_block)
        blocks = cur - last
        staked = self._lp_stakes.get(address, 0)
        if blocks <= 0 or staked == 0 or self._total_lp == 0:
            return 0
        return int(blocks * self.rewards_per_block * staked / self._total_lp)

    def program_stats(self) -> dict:
        cur = self._bc.height
        pct = min(100, (cur - self.start_block) / max(1, self.duration_blocks) * 100)
        return {
            "start_block":   self.start_block,
            "end_block":     self.end_block,
            "progress":      f"{pct:.1f}%",
            "total_rewards": f"{self.total_rewards/10**DECIMALS:.3f} NBL",
            "lp_stakers":    len(self._lp_stakes),
            "total_lp":      self._total_lp,
        }


# ---- NFTStakingPool
class NFTStakingPool:
    """Stake NFTs to earn NBL rewards."""

    def __init__(self, pool_id: str, collection_id: str,
                  reward_per_block: float):
        self.pool_id          = pool_id
        self.collection_id    = collection_id
        self.reward_per_block = int(reward_per_block * 10**DECIMALS)
        self._staked:  Dict[str, List[Tuple[int, int]]] = {}  # owner -> [(token_id, staked_block)]
        self._rewards: Dict[str, int]                   = {}

    def stake(self, owner: str, token_id: int,
               current_block: int) -> bool:
        if owner not in self._staked:
            self._staked[owner] = []
        self._staked[owner].append((token_id, current_block))
        return True

    def unstake(self, owner: str, token_id: int,
                 current_block: int) -> Tuple[bool, int]:
        if owner not in self._staked:
            return False, 0
        for i, (tid, stk_block) in enumerate(self._staked[owner]):
            if tid == token_id:
                blocks  = current_block - stk_block
                reward  = blocks * self.reward_per_block
                self._staked[owner].pop(i)
                self._rewards[owner] = self._rewards.get(owner, 0) + reward
                return True, reward
        return False, 0

    def pending(self, owner: str, current_block: int) -> int:
        total = 0
        for _, stk_block in self._staked.get(owner, []):
            total += (current_block - stk_block) * self.reward_per_block
        return total + self._rewards.get(owner, 0)

    def pool_info(self) -> dict:
        total_staked = sum(len(nfts) for nfts in self._staked.values())
        return {
            "pool_id":        self.pool_id,
            "collection_id":  self.collection_id,
            "reward_per_block": f"{self.reward_per_block/10**DECIMALS:.6f}",
            "total_staked":   total_staked,
            "stakers":        len(self._staked),
        }


# ---- NFTStakingManager
class NFTStakingManager:
    """Manages multiple NFT staking pools."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._pools: Dict[str, NFTStakingPool] = {}
        self._lock  = threading.RLock()

    def create_pool(self, collection_id: str,
                     reward_per_block: float) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"NFTSTK:{collection_id}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._pools[pid] = NFTStakingPool(
                pid, collection_id, reward_per_block)
            return pid

    def stake(self, pool_id: str, owner: str,
               token_id: int) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, "Pool not found"
            ok = pool.stake(owner, token_id, self._bc.height)
            return ok, f"Staked NFT #{token_id}"

    def unstake(self, pool_id: str, owner: str,
                 token_id: int) -> Tuple[bool, int]:
        with self._lock:
            pool = self._pools.get(pool_id)
            if not pool:
                return False, 0
            return pool.unstake(owner, token_id, self._bc.height)

    def all_pools(self) -> List[dict]:
        return [p.pool_info() for p in self._pools.values()]


# ---- CollateralType
class CollateralType:
    """Supported collateral for NBUSD minting."""

    TYPES = {
        "NBL":   {"ratio": 1.50, "oracle": "NBL/USD"},
        "WBTC":  {"ratio": 1.30, "oracle": "BTC/USD"},
        "WETH":  {"ratio": 1.35, "oracle": "ETH/USD"},
        "NBL_LP": {"ratio": 1.80, "oracle": "NBL/USD"},
    }


# ---- MultiCollateralStablecoin
class MultiCollateralStablecoin:
    """
    Multi-collateral NBUSD stablecoin.
    Accepts NBL, WBTC, WETH as collateral.
    """

    SYMBOL     = "NBUSD"
    TARGET     = 1.0       # $1.00 peg
    LIQ_RATIO  = 1.15      # liquidate below 115%
    STAB_FEE   = 0.015     # 1.5% annual stability fee

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._vaults: Dict[str, dict] = {}
        self._supply  = 0
        self._lock    = threading.RLock()

    def open_vault(self, owner: str, collateral_type: str,
                    collateral_amount: float) -> Tuple[bool, str]:
        with self._lock:
            if collateral_type not in CollateralType.TYPES:
                return False, f"Unsupported collateral: {collateral_type}"
            vid = hashlib.sha256(
                f"VAULT:{owner}:{collateral_type}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._vaults[vid] = {
                "vault_id":   vid,
                "owner":      owner,
                "collateral_type": collateral_type,
                "collateral": collateral_amount,
                "debt":       0.0,
                "opened_at":  time.time(),
            }
            return True, vid

    def mint(self, vault_id: str, amount_nbusd: float) -> Tuple[bool, str]:
        with self._lock:
            v = self._vaults.get(vault_id)
            if not v:
                return False, "Vault not found"
            ct     = CollateralType.TYPES.get(v["collateral_type"], {})
            okey   = ct.get("oracle", "NBL/USD")
            price  = (self._oracle.price(okey) if self._oracle else 0.01) or 0.01
            ratio  = ct.get("ratio", 1.5)
            max_d  = v["collateral"] * price / ratio
            if v["debt"] + amount_nbusd > max_d:
                return False, f"Exceeds max debt: {max_d:.2f} NBUSD"
            v["debt"]    += amount_nbusd
            self._supply += int(amount_nbusd * 10**DECIMALS)
            return True, f"Minted {amount_nbusd:.2f} NBUSD"

    def repay(self, vault_id: str, amount: float) -> Tuple[bool, str]:
        with self._lock:
            v = self._vaults.get(vault_id)
            if not v:
                return False, "Vault not found"
            repay  = min(amount, v["debt"])
            v["debt"]    -= repay
            self._supply -= int(repay * 10**DECIMALS)
            return True, f"Repaid {repay:.2f} NBUSD"

    def check_all_liquidations(self) -> List[str]:
        liquidated = []
        with self._lock:
            for vid, v in list(self._vaults.items()):
                if v["debt"] == 0:
                    continue
                ct    = CollateralType.TYPES.get(v["collateral_type"], {})
                price = (self._oracle.price(ct.get("oracle", "NBL/USD"))
                         if self._oracle else 0.01) or 0.01
                ratio = v["collateral"] * price / v["debt"] if v["debt"] > 0 else 999
                if ratio < self.LIQ_RATIO:
                    liquidated.append(vid)
                    v["debt"] = 0
        return liquidated

    def stablecoin_stats(self) -> dict:
        with self._lock:
            active = sum(1 for v in self._vaults.values() if v["debt"] > 0)
        return {
            "symbol":       self.SYMBOL,
            "total_supply": f"{self._supply/10**DECIMALS:.2f}",
            "active_vaults": active,
            "total_vaults": len(self._vaults),
        }


# ---- AirdropCampaign
class AirdropCampaign:
    """A token airdrop campaign."""

    def __init__(self, campaign_id: str, creator: str,
                  token: str, total_amount: int,
                  eligible_addresses: List[str],
                  per_address: int):
        self.campaign_id = campaign_id
        self.creator     = creator
        self.token       = token
        self.total       = total_amount
        self.eligible    = set(eligible_addresses)
        self.per_address = per_address
        self.claimed:    Set[str] = set()
        self.active      = True

    @property
    def total_claimed(self) -> int:
        return len(self.claimed) * self.per_address

    def claim(self, address: str) -> Tuple[bool, int]:
        if not self.active:
            return False, 0
        if address not in self.eligible:
            return False, 0
        if address in self.claimed:
            return False, 0
        if self.total_claimed + self.per_address > self.total:
            return False, 0
        self.claimed.add(address)
        return True, self.per_address

    def to_dict(self) -> dict:
        return {
            "campaign_id": self.campaign_id,
            "token":       self.token,
            "total":       f"{self.total/10**DECIMALS:.3f}",
            "claimed":     len(self.claimed),
            "eligible":    len(self.eligible),
            "active":      self.active,
        }


# ---- AirdropManager
class AirdropManager:
    """Manages multiple airdrop campaigns."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._campaigns: Dict[str, AirdropCampaign] = {}
        self._lock      = threading.RLock()

    def create_campaign(self, creator: str, token: str,
                         total_nbl: float,
                         eligible: List[str],
                         per_address_nbl: float) -> str:
        with self._lock:
            cid = hashlib.sha256(
                f"AIRDROP:{creator}:{token}:{time.time()}".encode()
            ).hexdigest()[:12]
            total  = int(total_nbl * 10**DECIMALS)
            per    = int(per_address_nbl * 10**DECIMALS)
            self._campaigns[cid] = AirdropCampaign(
                cid, creator, token, total, eligible, per)
            return cid

    def claim(self, campaign_id: str,
               address: str) -> Tuple[bool, int]:
        with self._lock:
            camp = self._campaigns.get(campaign_id)
            if not camp:
                return False, 0
            return camp.claim(address)

    def eligible_for(self, address: str) -> List[str]:
        return [cid for cid, c in self._campaigns.items()
                if address in c.eligible and address not in c.claimed]

    def airdrop_stats(self) -> dict:
        with self._lock:
            total_claimed = sum(
                c.total_claimed for c in self._campaigns.values())
        return {
            "total_campaigns": len(self._campaigns),
            "total_claimed_nbl": f"{total_claimed/10**DECIMALS:.3f}",
        }


# ---- DeFiStrategy
class DeFiStrategy:
    """Base class for automated DeFi strategies."""

    def __init__(self, name: str, description: str):
        self.name        = name
        self.description = description
        self.active      = True
        self.executions  = 0
        self.pnl         = 0.0

    def execute(self, *args, **kwargs) -> dict:
        raise NotImplementedError


# ---- ArbitrageStrategy
class ArbitrageStrategy(DeFiStrategy):
    """Simple AMM arbitrage strategy."""

    def __init__(self):
        super().__init__(
            "AMM Arbitrage",
            "Profits from price discrepancies between DEX pools"
        )

    def find_opportunity(self, dex: 'NEBULADex',
                          pair: str) -> Optional[dict]:
        """Find arbitrage opportunity across pools for a pair."""
        pools = [p for p in dex._pools.values()
                 if p.token_a == pair.split('/')[0] or
                    p.token_b == pair.split('/')[0]]
        if len(pools) < 2:
            return None
        prices = []
        for p in pools:
            if p.reserve_a > 0 and p.reserve_b > 0:
                price = p.reserve_b / p.reserve_a
                prices.append((p.pool_id, price))
        if len(prices) < 2:
            return None
        prices.sort(key=lambda x: x[1])
        low_pool, low_price   = prices[0]
        high_pool, high_price = prices[-1]
        spread = (high_price - low_price) / low_price * 100
        if spread > 0.5:   # >0.5% spread after fees
            return {
                "opportunity": True,
                "buy_pool":    low_pool,
                "sell_pool":   high_pool,
                "buy_price":   low_price,
                "sell_price":  high_price,
                "spread_pct":  f"{spread:.2f}%",
            }
        return None
