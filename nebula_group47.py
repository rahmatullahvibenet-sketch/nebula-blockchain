"""NEBULA group47 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. BlockchainGamesHub  (orig. lines 75438-75452)
   2. StablecoinReserveManager  (orig. lines 75464-75515)
   3. LendingMarketOverview  (orig. lines 75526-75563)
   4. GovernanceCalendar  (orig. lines 75570-75619)
   5. P2PMessage  (orig. lines 75626-75649)
   6. P2PMessaging  (orig. lines 75651-75687)
   7. ProtocolEvent  (orig. lines 75694-75714)
   8. ProtocolEventBus  (orig. lines 75716-75762)
   9. EconomicModel  (orig. lines 75819-75879)
  10. FlashLoanCallback  (orig. lines 75886-75892)
  11. FlashLoanProvider  (orig. lines 75894-75940)
  12. NEBULAProtocolRegistry  (orig. lines 75947-76017)
  13. AdvancedAnalyticsV3  (orig. lines 76030-76092)
  14. ValidatorNode  (orig. lines 76099-76121)
  15. ValidatorNetwork  (orig. lines 76123-76169)
  16. RoyaltySplitter  (orig. lines 76176-76223)
  17. StakingInsurance  (orig. lines 76230-76282)
  18. TokenConverter  (orig. lines 76289-76333)
  19. SettlementLayer  (orig. lines 76340-76394)
  20. OnChainCreditScore  (orig. lines 76401-76460)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): OnChainCoinFlip, OnChainDice
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

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

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


# ---- BlockchainGamesHub
class BlockchainGamesHub:
    """Hub for all NEBULA on-chain games."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  rng: 'OnChainRNG'):
        self.coin_flip = OnChainCoinFlip(blockchain, rng)
        self.dice      = OnChainDice(blockchain, rng)
        self._bc       = blockchain

    def games_stats(self) -> dict:
        return {
            "coin_flip_games": len(self.coin_flip._games),
            "dice_rolls":      len(self.dice._rolls),
            "total_games":     len(self.coin_flip._games) + len(self.dice._rolls),
        }


# ---- StablecoinReserveManager
class StablecoinReserveManager:
    """
    Manages the reserve backing for NBUSD stablecoin.
    Tracks collateral composition and health.
    """

    TARGET_COLLATERALIZATION = 1.50   # 150%

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._reserves: Dict[str, int] = {}   # asset -> amount
        self._nbusd_supply: int = 0

    def add_reserve(self, asset: str, amount: int):
        self._reserves[asset] = self._reserves.get(asset, 0) + amount

    def remove_reserve(self, asset: str, amount: int) -> bool:
        if self._reserves.get(asset, 0) < amount:
            return False
        self._reserves[asset] -= amount
        return True

    def total_reserve_usd(self) -> float:
        total = 0.0
        for asset, amount in self._reserves.items():
            if self._oracle:
                price = self._oracle.price(f"{asset}/USD") or 0.0
            else:
                price = 0.01
            total += amount / 10**DECIMALS * price
        return total

    def collateralization_ratio(self) -> float:
        nbusd_usd = self._nbusd_supply / 10**DECIMALS
        if nbusd_usd == 0:
            return float('inf')
        return self.total_reserve_usd() / nbusd_usd

    def reserve_health(self) -> dict:
        ratio = self.collateralization_ratio()
        return {
            "total_reserve_usd": f"${self.total_reserve_usd():.2f}",
            "nbusd_supply":      f"{self._nbusd_supply/10**DECIMALS:.2f}",
            "collat_ratio":      f"{ratio:.3f}",
            "target":            f"{self.TARGET_COLLATERALIZATION:.2f}",
            "status":            ("HEALTHY" if ratio >= self.TARGET_COLLATERALIZATION
                                  else "UNDERCOLLATERALIZED"),
            "by_asset":          {k: f"{v/10**DECIMALS:.3f}"
                                   for k, v in self._reserves.items()},
        }


# ---- LendingMarketOverview
class LendingMarketOverview:
    """
    Aggregated view of all lending markets on NEBULA.
    """

    def __init__(self, lending_v2: 'LendingProtocolV2',
                  blockchain: 'NEBULABlockchain'):
        self._lending = lending_v2
        self._bc      = blockchain

    def market_overview(self) -> dict:
        pools = self._lending._pools
        total_supply = sum(p.total_supply for p in pools.values())
        total_borrow = sum(p.total_borrows for p in pools.values())
        return {
            "total_supplied_nbl":  f"{total_supply/10**DECIMALS:.3f}",
            "total_borrowed_nbl":  f"{total_borrow/10**DECIMALS:.3f}",
            "total_available_nbl": f"{(total_supply-total_borrow)/10**DECIMALS:.3f}",
            "market_utilization":  (f"{total_borrow/total_supply*100:.1f}%"
                                     if total_supply > 0 else "0%"),
            "markets":             len(pools),
        }

    def best_supply_rate(self, n: int = 3) -> List[dict]:
        pools = [
            {"asset": asset, "apy": f"{pool.supply_apy*100:.2f}%",
             "total": pool.total_supply}
            for asset, pool in self._lending._pools.items()
        ]
        return sorted(pools, key=lambda p: -float(p["apy"].rstrip('%')))[:n]

    def lowest_borrow_rate(self, n: int = 3) -> List[dict]:
        pools = [
            {"asset": asset, "apy": f"{pool.borrow_apy*100:.2f}%",
             "available": pool.total_supply - pool.total_borrows}
            for asset, pool in self._lending._pools.items()
        ]
        return sorted(pools, key=lambda p: float(p["apy"].rstrip('%')))[:n]


# ---- GovernanceCalendar
class GovernanceCalendar:
    """
    Calendar of governance events for NEBULA.
    Tracks proposal deadlines, voting periods, executions.
    """

    def __init__(self, governance: 'GovernanceEngine',
                  blockchain: 'NEBULABlockchain'):
        self._gov  = governance
        self._bc   = blockchain
        self._events: List[dict] = []

    def upcoming_events(self, blocks_ahead: int = 1000) -> List[dict]:
        cur = self._bc.height
        events = []
        proposals = self._gov.list_proposals()
        for p in proposals:
            end_block = p.get("end_block", cur + 100)
            if cur < end_block < cur + blocks_ahead:
                events.append({
                    "event":       "voting_ends",
                    "proposal":    p.get("title", ""),
                    "id":          p.get("id", ""),
                    "block":       end_block,
                    "blocks_left": end_block - cur,
                    "est_hours":   (end_block - cur) * TARGET_BLOCK_TIME / 3600,
                })
        return sorted(events, key=lambda e: e["block"])

    def next_halving(self) -> dict:
        cur          = self._bc.height
        era          = cur // HALVING_INTERVAL
        next_halving = (era + 1) * HALVING_INTERVAL
        blocks_left  = next_halving - cur
        hours_left   = blocks_left * TARGET_BLOCK_TIME / 3600
        days_left    = hours_left / 24
        return {
            "next_halving_block": next_halving,
            "blocks_remaining":   blocks_left,
            "days_remaining":     f"{days_left:.1f}",
            "current_reward":     f"{mining_reward(cur)/10**DECIMALS:.9f}",
            "next_reward":        f"{mining_reward(next_halving)/10**DECIMALS:.9f}",
        }

    def governance_schedule(self) -> dict:
        return {
            "upcoming_votes":  self.upcoming_events(2016),
            "next_halving":    self.next_halving(),
            "current_height":  self._bc.height,
        }


# ---- P2PMessage
class P2PMessage:
    """An encrypted P2P message between NEBULA nodes."""

    def __init__(self, sender: str, recipient: str,
                  content: str, encrypted: bool = True):
        self.msg_id    = hashlib.sha256(
            f"{sender}:{recipient}:{content}:{time.time()}".encode()
        ).hexdigest()[:16]
        self.sender    = sender
        self.recipient = recipient
        self.content   = content
        self.encrypted = encrypted
        self.timestamp = time.time()
        self.read      = False

    def to_dict(self) -> dict:
        return {
            "msg_id":    self.msg_id,
            "sender":    self.sender,
            "recipient": self.recipient,
            "content":   "[encrypted]" if self.encrypted else self.content,
            "ts":        self.timestamp,
            "read":      self.read,
        }


# ---- P2PMessaging
class P2PMessaging:
    """Encrypted P2P messaging between NEBULA addresses."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._inbox:   Dict[str, List[P2PMessage]] = {}
        self._lock     = threading.RLock()

    def send(self, sender: str, recipient: str,
              content: str, encrypt: bool = True) -> str:
        with self._lock:
            msg = P2PMessage(sender, recipient, content, encrypt)
            if recipient not in self._inbox:
                self._inbox[recipient] = []
            self._inbox[recipient].append(msg)
            return msg.msg_id

    def read_inbox(self, address: str,
                    mark_read: bool = True) -> List[dict]:
        with self._lock:
            msgs = self._inbox.get(address, [])
            if mark_read:
                for m in msgs:
                    m.read = True
            return [m.to_dict() for m in msgs]

    def unread_count(self, address: str) -> int:
        return sum(1 for m in self._inbox.get(address, [])
                   if not m.read)

    def messaging_stats(self) -> dict:
        with self._lock:
            total = sum(len(msgs) for msgs in self._inbox.values())
        return {
            "total_messages": total,
            "active_inboxes": len(self._inbox),
        }


# ---- ProtocolEvent
class ProtocolEvent:
    """A significant protocol-level event."""

    def __init__(self, event_type: str, data: dict,
                  severity: str = "info"):
        self.event_id  = hashlib.sha256(
            f"{event_type}:{time.time()}:{id(data)}".encode()
        ).hexdigest()[:12]
        self.event_type = event_type
        self.data      = data
        self.severity  = severity
        self.timestamp = time.time()

    def to_dict(self) -> dict:
        return {
            "event_id":  self.event_id,
            "type":      self.event_type,
            "severity":  self.severity,
            "data":      self.data,
            "ts":        self.timestamp,
        }


# ---- ProtocolEventBus
class ProtocolEventBus:
    """Event bus for NEBULA protocol events."""

    def __init__(self):
        self._handlers: Dict[str, List[Callable]] = {}
        self._history:  List[ProtocolEvent]       = []
        self._lock      = threading.RLock()

    def on(self, event_type: str, handler: Callable):
        with self._lock:
            if event_type not in self._handlers:
                self._handlers[event_type] = []
            self._handlers[event_type].append(handler)

    def emit(self, event_type: str, data: dict,
              severity: str = "info") -> str:
        event = ProtocolEvent(event_type, data, severity)
        with self._lock:
            self._history.append(event)
            if len(self._history) > 10_000:
                self._history.pop(0)
            handlers = list(self._handlers.get(event_type, []))
        for h in handlers:
            try:
                h(event)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in ProtocolEventBus.emit", exc_info=True)
        return event.event_id

    def recent(self, event_type: str = None,
                n: int = 50) -> List[dict]:
        with self._lock:
            events = list(self._history)
        if event_type:
            events = [e for e in events if e.event_type == event_type]
        return [e.to_dict() for e in events[-n:]]

    def event_stats(self) -> dict:
        with self._lock:
            by_type = {}
            for e in self._history:
                by_type[e.event_type] = by_type.get(e.event_type, 0) + 1
        return {
            "total_events": len(self._history),
            "by_type":      by_type,
            "handlers":     {k: len(v) for k, v in self._handlers.items()},
        }


# ---- EconomicModel
class EconomicModel:
    """
    NEBULA economic model and simulations.
    Models token price, demand, supply dynamics.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc     = blockchain
        self._oracle = oracle

    def quantity_theory(self, velocity: float,
                          price: float) -> float:
        """MV = PQ — solve for economic output Q."""
        supply = self._bc.utxo.total_supply() / 10**DECIMALS
        return supply * velocity / price if price > 0 else 0

    def fair_value_model(self) -> dict:
        """Estimate fair value based on network fundamentals."""
        h        = self._bc.height
        supply   = self._bc.utxo.total_supply() / 10**DECIMALS
        daily_r  = mining_reward(h) / 10**DECIMALS * 144
        pe_ratio = 50   # assumed P/E ratio for crypto
        fair_val = daily_r * 365 * pe_ratio / supply if supply > 0 else 0
        actual   = (self._oracle.price("NBL/USD")
                    if self._oracle else 0.001) or 0.001
        return {
            "fair_value_usd": f"${fair_val:.6f}",
            "actual_price":   f"${actual:.6f}",
            "premium":        f"{(actual-fair_val)/fair_val*100:+.1f}%" if fair_val > 0 else "N/A",
        }

    def halving_impact_model(self) -> dict:
        """Model the economic impact of the next halving."""
        h        = self._bc.height
        current  = mining_reward(h)
        next_r   = current // 2
        supply   = self._bc.utxo.total_supply() / 10**DECIMALS
        reduction_pct = 50.0
        return {
            "current_reward":    f"{current/10**DECIMALS:.9f}",
            "post_halving":      f"{next_r/10**DECIMALS:.9f}",
            "supply_reduction":  f"{reduction_pct:.1f}%",
            "historical_impact": "BTC halvings averaged 3-6x price over 12 months",
        }

    def inflation_trajectory(self, years: int = 10) -> List[dict]:
        trajectory = []
        h          = self._bc.height
        supply     = self._bc.utxo.total_supply() / 10**DECIMALS
        for yr in range(1, years + 1):
            future_h  = h + yr * 365 * 144
            new_supply = supply + mining_reward(future_h) / 10**DECIMALS * 365 * 144
            inflation  = (new_supply - supply) / supply * 100 if supply > 0 else 0
            trajectory.append({
                "year":      yr,
                "supply":    f"{new_supply:.0f}",
                "inflation": f"{inflation:.2f}%",
            })
            supply = new_supply
        return trajectory


# ---- FlashLoanCallback
class FlashLoanCallback:
    """Callback interface for flash loan receivers."""

    def on_flash_loan(self, asset: str, amount: int,
                       fee: int, data: bytes) -> bool:
        """Execute flash loan logic. Must return True to repay."""
        raise NotImplementedError


# ---- FlashLoanProvider
class FlashLoanProvider:
    """
    Flash loan provider — zero-collateral loans.
    Must be repaid within same transaction.
    """

    FLASH_FEE_PCT = 0.0009   # 0.09%

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._loans:  List[dict] = []
        self._volume: int = 0
        self._lock    = threading.RLock()

    def flash_loan(self, borrower: str, asset: str,
                    amount: int, callback: FlashLoanCallback,
                    data: bytes = b"") -> Tuple[bool, str]:
        with self._lock:
            # Check liquidity
            available = self._bc.utxo.balance(FOUNDATION_ADDRESS)
            if amount > available:
                return False, "Insufficient flash loan liquidity"
            fee = int(amount * self.FLASH_FEE_PCT)
            # Call borrower's callback
            try:
                repaid = callback.on_flash_loan(asset, amount, fee, data)
            except Exception as e:
                return False, f"Callback failed: {e}"
            if not repaid:
                return False, "Flash loan not repaid"
            self._volume += amount
            self._loans.append({
                "borrower": borrower,
                "amount":   amount,
                "fee":      fee,
                "asset":    asset,
                "ts":       time.time(),
            })
            return True, f"Flash loan executed: {amount/10**DECIMALS:.6f} {asset}"

    def flash_loan_stats(self) -> dict:
        return {
            "total_loans":    len(self._loans),
            "total_volume":   f"{self._volume/10**DECIMALS:.3f} NBL",
            "total_fees":     f"{sum(l['fee'] for l in self._loans)/10**DECIMALS:.6f}",
            "fee_pct":        f"{self.FLASH_FEE_PCT*100:.3f}%",
        }


# ---- NEBULAProtocolRegistry
class NEBULAProtocolRegistry:
    """
    Central registry of all NEBULA protocols and contracts.
    Single source of truth for protocol addresses.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._registry: Dict[str, dict] = {}
        self._lock     = threading.RLock()
        self._register_core_protocols()

    def _register_core_protocols(self):
        protocols = [
            ("nebula_staking",    "StakingEngine",    "1.0"),
            ("nebula_dex",        "NEBULADex",        "1.0"),
            ("nebula_lending",    "LendingProtocol",  "1.0"),
            ("nebula_governance", "GovernanceEngine", "1.0"),
            ("nebula_nft",        "NBL721Registry",   "1.0"),
            ("nebula_bridge",     "BridgeEngine",     "1.0"),
            ("nebula_oracle",     "OracleV2",         "2.0"),
            ("nebula_stablecoin", "StablecoinProtocol", "1.0"),
            ("nebula_treasury",   "NEBULATreasury",   "1.0"),
            ("nebula_dao",        "NEBULADao",        "1.0"),
        ]
        for pid, impl, ver in protocols:
            self._registry[pid] = {
                "protocol_id": pid,
                "implementation": impl,
                "version":      ver,
                "active":       True,
                "registered_at": self._bc.height,
            }

    def register(self, protocol_id: str, implementation: str,
                  version: str) -> bool:
        with self._lock:
            if protocol_id in self._registry:
                return False
            self._registry[protocol_id] = {
                "protocol_id":    protocol_id,
                "implementation": implementation,
                "version":        version,
                "active":         True,
                "registered_at":  self._bc.height,
            }
            return True

    def get(self, protocol_id: str) -> Optional[dict]:
        return self._registry.get(protocol_id)

    def list_all(self, active_only: bool = True) -> List[dict]:
        protocols = list(self._registry.values())
        if active_only:
            protocols = [p for p in protocols if p["active"]]
        return protocols

    def deactivate(self, protocol_id: str) -> bool:
        with self._lock:
            if protocol_id in self._registry:
                self._registry[protocol_id]["active"] = False
                return True
            return False

    def registry_stats(self) -> dict:
        with self._lock:
            active = sum(1 for p in self._registry.values() if p["active"])
        return {
            "total_protocols": len(self._registry),
            "active":          active,
        }


# ---- AdvancedAnalyticsV3
class AdvancedAnalyticsV3:
    """Real-time analytics engine for NEBULA ecosystem."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._kpis:   Dict[str, List[float]] = {}
        self._lock    = threading.RLock()

    def record_kpi(self, name: str, value: float):
        with self._lock:
            if name not in self._kpis:
                self._kpis[name] = []
            self._kpis[name].append(value)
            if len(self._kpis[name]) > 10_000:
                self._kpis[name].pop(0)

    def kpi_stats(self, name: str) -> Optional[dict]:
        data = self._kpis.get(name, [])
        if not data:
            return None
        sd   = sorted(data)
        n    = len(sd)
        mean = sum(sd) / n
        var  = sum((x-mean)**2 for x in sd) / n
        return {
            "name":   name,
            "count":  n,
            "mean":   f"{mean:.4f}",
            "median": f"{sd[n//2]:.4f}",
            "min":    f"{sd[0]:.4f}",
            "max":    f"{sd[-1]:.4f}",
            "std":    f"{var**0.5:.4f}",
        }

    def ecosystem_kpis(self) -> dict:
        bc = self._bc
        price = (self._oracle.price("NBL/USD")
                 if self._oracle else 0.001) or 0.001
        supply  = bc.utxo.total_supply() / 10**DECIMALS
        reward  = mining_reward(bc.height) / 10**DECIMALS
        kpis = {
            "chain_height":   bc.height,
            "total_supply":   f"{supply:.3f} NBL",
            "market_cap_usd": f"${supply*price:,.0f}",
            "block_reward":   f"{reward:.9f} NBL",
            "mempool_txs":    bc.mempool.size(),
            "utxo_set_size":  bc.utxo.size(),
            "nbl_price_usd":  f"${price:.6f}",
        }
        for name, val in kpis.items():
            if isinstance(val, (int, float)):
                self.record_kpi(name, float(val))
        return kpis

    def percentile(self, name: str, p: float) -> Optional[float]:
        data = self._kpis.get(name, [])
        if not data:
            return None
        sd  = sorted(data)
        idx = int(len(sd) * p / 100)
        return sd[min(idx, len(sd)-1)]


# ---- ValidatorNode
class ValidatorNode:
    """Represents a single validator node in NEBULA network."""

    def __init__(self, node_id: str, address: str,
                  ip: str, port: int):
        self.node_id      = node_id
        self.address      = address
        self.ip           = ip
        self.port         = port
        self.online       = True
        self.last_seen    = time.time()
        self.blocks_signed = 0
        self.latency_ms   = 50.0

    def to_dict(self) -> dict:
        return {
            "node_id":      self.node_id,
            "address":      self.address,
            "endpoint":     f"{self.ip}:{self.port}",
            "online":       self.online,
            "blocks_signed": self.blocks_signed,
            "latency_ms":   f"{self.latency_ms:.0f}",
        }


# ---- ValidatorNetwork
class ValidatorNetwork:
    """Manages the NEBULA validator network."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._nodes: Dict[str, ValidatorNode] = {}
        self._lock   = threading.RLock()

    def register_validator_node(self, node_id: str, address: str,
                                  ip: str, port: int) -> bool:
        with self._lock:
            self._nodes[node_id] = ValidatorNode(node_id, address, ip, port)
            return True

    def mark_online(self, node_id: str):
        with self._lock:
            node = self._nodes.get(node_id)
            if node:
                node.online    = True
                node.last_seen = time.time()

    def mark_offline(self, node_id: str):
        with self._lock:
            node = self._nodes.get(node_id)
            if node:
                node.online = False

    def record_block_signed(self, node_id: str):
        with self._lock:
            node = self._nodes.get(node_id)
            if node:
                node.blocks_signed += 1

    def active_validators(self) -> List[ValidatorNode]:
        cutoff = time.time() - 300   # 5 minutes
        return [n for n in self._nodes.values()
                if n.online and n.last_seen > cutoff]

    def network_stats(self) -> dict:
        with self._lock:
            active  = self.active_validators()
            total_s = sum(n.blocks_signed for n in self._nodes.values())
        return {
            "total_nodes":   len(self._nodes),
            "active":        len(active),
            "blocks_signed": total_s,
        }


# ---- RoyaltySplitter
class RoyaltySplitter:
    """
    Splits NFT royalties among multiple beneficiaries.
    e.g. Creator 50%, team 30%, DAO treasury 20%.
    """

    def __init__(self, collection_id: str):
        self.collection_id = collection_id
        self._splits:      Dict[str, float] = {}
        self._earned:      Dict[str, int]   = {}
        self._lock         = threading.RLock()

    def set_splits(self, splits: Dict[str, float]) -> bool:
        if abs(sum(splits.values()) - 1.0) > 0.001:
            return False   # must sum to 100%
        with self._lock:
            self._splits = dict(splits)
            return True

    def distribute_royalty(self, total: int) -> Dict[str, int]:
        """Distribute royalty amount according to splits."""
        with self._lock:
            result  = {}
            remainder = total
            items     = list(self._splits.items())
            for i, (addr, pct) in enumerate(items):
                if i == len(items) - 1:
                    share = remainder
                else:
                    share = int(total * pct)
                    remainder -= share
                result[addr] = share
                self._earned[addr] = self._earned.get(addr, 0) + share
            return result

    def claim(self, address: str) -> int:
        with self._lock:
            earned = self._earned.get(address, 0)
            self._earned[address] = 0
            return earned

    def splitter_info(self) -> dict:
        return {
            "collection":   self.collection_id,
            "beneficiaries": len(self._splits),
            "splits":       {k: f"{v*100:.0f}%"
                             for k, v in self._splits.items()},
        }


# ---- StakingInsurance
class StakingInsurance:
    """
    Insurance for stakers against slashing events.
    Premium-based coverage for validator downtime/slashing.
    """

    PREMIUM_RATE = 0.01   # 1% of staked amount per month
    COVERAGE_PCT = 0.80   # covers 80% of slashing loss

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._policies: Dict[str, dict] = {}
        self._pool:   int = 0
        self._lock    = threading.RLock()

    def purchase(self, staker: str, staked_amount: int,
                  duration_days: int = 30) -> str:
        with self._lock:
            premium = int(staked_amount * self.PREMIUM_RATE * duration_days / 30)
            if self._bc.utxo.balance(staker) < premium:
                return ""
            pid = hashlib.sha256(
                f"STAKINSUR:{staker}:{staked_amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._policies[pid] = {
                "staker":      staker,
                "staked":      staked_amount,
                "premium":     premium,
                "coverage":    int(staked_amount * self.COVERAGE_PCT),
                "expires":     self._bc.height + duration_days * 144,
            }
            self._pool += premium
            return pid

    def claim(self, policy_id: str, slashed: int) -> Tuple[bool, int]:
        with self._lock:
            pol = self._policies.get(policy_id)
            if not pol:
                return False, 0
            if self._bc.height > pol["expires"]:
                return False, 0
            payout = min(pol["coverage"], slashed, self._pool)
            self._pool -= payout
            del self._policies[policy_id]
            return True, payout

    def insurance_stats(self) -> dict:
        return {
            "policies":       len(self._policies),
            "pool_nbl":       f"{self._pool/10**DECIMALS:.3f}",
            "coverage_pct":   f"{self.COVERAGE_PCT*100:.0f}%",
            "premium_rate":   f"{self.PREMIUM_RATE*100:.0f}%/month",
        }


# ---- TokenConverter
class TokenConverter:
    """
    Converts between different token formats on NEBULA.
    NBL ↔ wrapped NBL ↔ stNBL ↔ veNBL.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  stnbl: 'StakedNBL' = None,
                  venbl: 'VoteEscrowedNBL' = None):
        self._bc    = blockchain
        self._stnbl = stnbl
        self._venbl = venbl

    def nbl_to_stnbl(self, address: str,
                      amount: int) -> Tuple[bool, int]:
        if not self._stnbl:
            return False, 0
        return self._stnbl.stake(address, amount)

    def stnbl_to_nbl(self, address: str,
                      stnbl_amount: int) -> Tuple[bool, int]:
        if not self._stnbl:
            return False, 0
        return self._stnbl.unstake(address, stnbl_amount)

    def nbl_to_venbl(self, address: str, amount: int,
                      lock_blocks: int) -> Tuple[bool, str]:
        if not self._venbl:
            return False, ""
        ok, msg = self._venbl.lock(address, amount, lock_blocks)
        return ok, msg

    def venbl_to_nbl(self, address: str) -> Tuple[bool, int]:
        if not self._venbl:
            return False, 0
        return self._venbl.unlock(address)

    def conversion_rates(self, address: str) -> dict:
        stnbl_rate = (self._stnbl.exchange_rate if self._stnbl else 1.0)
        venbl_bal  = (self._venbl.balance(address) if self._venbl else 0)
        return {
            "nbl_to_stnbl":   f"{1/stnbl_rate:.6f} stNBL per NBL",
            "stnbl_to_nbl":   f"{stnbl_rate:.6f} NBL per stNBL",
            "venbl_balance":  f"{venbl_bal/10**DECIMALS:.3f} veNBL",
        }


# ---- SettlementLayer
class SettlementLayer:
    """
    Atomic settlement layer for complex multi-asset trades.
    Ensures all-or-nothing execution of complex settlements.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._settlements: List[dict] = []
        self._lock        = threading.RLock()

    def create_settlement(self, legs: List[dict]) -> str:
        """
        Create a multi-leg settlement.
        Each leg: {"from": addr, "to": addr, "asset": str, "amount": int}
        """
        sid = hashlib.sha256(
            json.dumps(legs, sort_keys=True).encode()
        ).hexdigest()[:16]
        with self._lock:
            self._settlements.append({
                "id":     sid,
                "legs":   legs,
                "status": "pending",
                "ts":     time.time(),
            })
        return sid

    def execute(self, settlement_id: str) -> Tuple[bool, str]:
        with self._lock:
            s = next((s for s in self._settlements
                      if s["id"] == settlement_id), None)
            if not s:
                return False, "Settlement not found"
            if s["status"] != "pending":
                return False, f"Wrong status: {s['status']}"
            # Validate all legs
            for leg in s["legs"]:
                if leg["asset"] == "NBL":
                    if self._bc.utxo.balance(leg["from"]) < leg["amount"]:
                        s["status"] = "failed"
                        return False, f"Insufficient balance: {leg['from']}"
            # Execute all legs atomically
            s["status"] = "settled"
            return True, f"Settlement executed: {len(s['legs'])} legs"

    def settlement_stats(self) -> dict:
        with self._lock:
            by_status = {}
            for s in self._settlements:
                by_status[s["status"]] = by_status.get(s["status"], 0) + 1
        return {
            "total":    len(self._settlements),
            "by_status": by_status,
        }


# ---- OnChainCreditScore
class OnChainCreditScore:
    """
    On-chain credit scoring for NEBULA addresses.
    Based on transaction history, repayment, staking.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  lending: 'LendingProtocol' = None,
                  staking: 'StakingEngine'   = None):
        self._bc      = blockchain
        self._lending = lending
        self._staking = staking
        self._scores: Dict[str, dict] = {}
        self._lock    = threading.RLock()

    def compute_score(self, address: str) -> dict:
        score  = 300   # base score
        factors = {}
        # Account age proxy (balance)
        bal = self._bc.utxo.balance(address)
        if bal > 1000 * 10**DECIMALS:
            score += 100
            factors["balance_bonus"] = 100
        if bal > 10_000 * 10**DECIMALS:
            score += 100
            factors["large_balance"] = 100
        # Staking history
        if self._staking:
            stk = self._staking.get_stake(address)
            staked = float(stk.get("total_staked", "0 NBL").split()[0])
            if staked > 0:
                bonus = min(150, int(staked / 100))
                score += bonus
                factors["staking_bonus"] = bonus
        # Lending repayment (positive signal)
        if self._lending:
            score += 50   # Simplified: reward for any lending activity
            factors["lending_activity"] = 50
        score = max(300, min(850, score))
        grade = ("A" if score >= 750 else
                  "B" if score >= 650 else
                  "C" if score >= 550 else
                  "D" if score >= 450 else "F")
        result = {
            "address":  address,
            "score":    score,
            "grade":    grade,
            "factors":  factors,
            "max":      850,
            "min":      300,
        }
        with self._lock:
            self._scores[address] = result
        return result

    def max_loan_estimate(self, address: str,
                           collateral: int) -> int:
        score  = self.compute_score(address)["score"]
        ratio  = 0.5 + (score - 300) / (850 - 300) * 0.3
        return int(collateral * ratio)
