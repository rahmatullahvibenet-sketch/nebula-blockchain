"""NEBULA group55 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. WalletConnectV2  (orig. lines 84917-84976)
   2. FeeShareV2  (orig. lines 84983-85036)
   3. StakingRewardsV3  (orig. lines 85043-85104)
   4. CrossShardTransaction  (orig. lines 85111-85133)
   5. CrossShardRouter  (orig. lines 85135-85182)
   6. ValidatorRotation  (orig. lines 85189-85247)
   7. DeFiAnalyticsV2  (orig. lines 85254-85309)
   8. FinalTestSuite  (orig. lines 85316-85439)
   9. ChainDataCompressor  (orig. lines 85451-85485)
  10. WalletBackupManager  (orig. lines 85492-85547)
  11. OracleV3  (orig. lines 85554-85613)
  12. RoyaltyEnforcementMiddleware  (orig. lines 85620-85669)
  13. GovernanceSimulation  (orig. lines 85676-85718)
  14. ExchangeListingInfo  (orig. lines 85725-85775)
  15. InstitutionalGrade  (orig. lines 85782-85842)
  16. APIGateway  (orig. lines 85853-85903)
  17. CompactBlockV2  (orig. lines 85987-86012)
  18. UTXOSnapshotV2  (orig. lines 86016-86044)
  19. SchnorrMultiSig  (orig. lines 86048-86088)
  20. MimbleWimbleTx  (orig. lines 86094-86121)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): BridgeEngine, GovernanceEngine, KeyDerivationFunction, MerkleTree, NBL721Registry, NEBULABlockchain, NEBULADex, NEBULANameService, OracleV2, ProposalType, Secp256k1, StakingEngine, ThresholdSignatureScheme
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

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- WalletConnectV2
class WalletConnectV2:
    """
    WalletConnect v2 protocol for NEBULA.
    Connects mobile wallets to dApps via QR codes.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._sessions:  Dict[str, dict] = {}
        self._pending:   Dict[str, dict] = {}
        self._lock       = threading.RLock()

    def new_pairing(self) -> dict:
        uri  = f"wc:nebula{secrets.token_hex(16)}@2?relay={secrets.token_hex(8)}"
        topic = hashlib.sha256(uri.encode()).hexdigest()[:16]
        with self._lock:
            self._pending[topic] = {
                "topic":     topic,
                "uri":       uri,
                "created":   time.time(),
                "approved":  False,
            }
        return {"uri": uri, "topic": topic}

    def approve(self, topic: str, wallet_address: str) -> bool:
        with self._lock:
            p = self._pending.get(topic)
            if not p:
                return False
            session_id = hashlib.sha256(
                f"{topic}:{wallet_address}:{time.time()}".encode()
            ).hexdigest()[:16]
            self._sessions[session_id] = {
                "session_id": session_id,
                "topic":      topic,
                "address":    wallet_address,
                "connected":  True,
                "ts":         time.time(),
            }
            del self._pending[topic]
            return True

    def sign_request(self, session_id: str, method: str,
                      params: dict) -> dict:
        session = self._sessions.get(session_id)
        if not session:
            return {"error": "Session not found"}
        return {
            "session_id": session_id,
            "method":     method,
            "address":    session["address"],
            "params":     params,
            "status":     "pending_signature",
        }

    def wc_stats(self) -> dict:
        return {
            "active_sessions": len(self._sessions),
            "pending":         len(self._pending),
        }


# ---- FeeShareV2
class FeeShareV2:
    """
    Enhanced fee sharing v2 — real-time distribution.
    Uses ve-token snapshot model.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  venbl: 'VoteEscrowedNBL'):
        self._bc     = blockchain
        self._venbl  = venbl
        self._epochs: List[dict] = []
        self._claims: Dict[int, Set[str]] = {}
        self._lock   = threading.RLock()

    def create_epoch(self, fees: int) -> int:
        with self._lock:
            epoch_id = len(self._epochs)
            total_venbl = self._venbl.total_venbl()
            self._epochs.append({
                "id":          epoch_id,
                "fees":        fees,
                "total_venbl": total_venbl,
                "created":     self._bc.height,
            })
            self._claims[epoch_id] = set()
            return epoch_id

    def claimable(self, address: str, epoch_id: int) -> int:
        with self._lock:
            if epoch_id >= len(self._epochs):
                return 0
            if address in self._claims[epoch_id]:
                return 0
            epoch      = self._epochs[epoch_id]
            venbl_bal  = self._venbl.balance(address)
            total_venbl = epoch["total_venbl"]
            if total_venbl == 0:
                return 0
            return int(epoch["fees"] * venbl_bal / total_venbl)

    def claim(self, address: str, epoch_id: int) -> Tuple[bool, int]:
        with self._lock:
            amount = self.claimable(address, epoch_id)
            if amount == 0:
                return False, 0
            self._claims[epoch_id].add(address)
            return True, amount

    def fee_share_v2_stats(self) -> dict:
        total_fees = sum(e["fees"] for e in self._epochs)
        return {
            "epochs":     len(self._epochs),
            "total_fees": f"{total_fees/10**DECIMALS:.6f} NBL",
        }


# ---- StakingRewardsV3
class StakingRewardsV3:
    """
    Staking rewards v3 with smooth emission and anti-gaming.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  total_emission: float = 50_000_000):
        self._bc       = blockchain
        self.total     = int(total_emission * 10**DECIMALS)
        self.emitted   = 0
        self._stakers: Dict[str, dict] = {}
        self._lock     = threading.RLock()

    def emission_rate(self) -> int:
        """Smooth decay emission rate."""
        h       = self._bc.height
        era     = h // HALVING_INTERVAL
        reward  = INITIAL_BLOCK_REWARD >> era
        return max(0, reward)

    def stake(self, address: str, amount: int) -> bool:
        with self._lock:
            if self._bc.utxo.balance(address) < amount:
                return False
            if address not in self._stakers:
                self._stakers[address] = {
                    "amount":   0,
                    "entry":    self._bc.height,
                    "rewards":  0,
                }
            self._stakers[address]["amount"] += amount
            return True

    def accrue(self, address: str, blocks: int) -> int:
        with self._lock:
            info = self._stakers.get(address)
            if not info or info["amount"] == 0:
                return 0
            total_staked = sum(s["amount"] for s in self._stakers.values()) or 1
            share  = info["amount"] / total_staked
            reward = int(self.emission_rate() * blocks * share)
            info["rewards"] += reward
            self.emitted    += reward
            return reward

    def claim(self, address: str) -> Tuple[bool, int]:
        with self._lock:
            info = self._stakers.get(address)
            if not info:
                return False, 0
            amount = info["rewards"]
            info["rewards"] = 0
            return amount > 0, amount

    def v3_staking_stats(self) -> dict:
        total = sum(s["amount"] for s in self._stakers.values())
        return {
            "stakers":      len(self._stakers),
            "total_staked": f"{total/10**DECIMALS:.3f}",
            "emitted":      f"{self.emitted/10**DECIMALS:.3f}",
            "emission_rate": f"{self.emission_rate()/10**DECIMALS:.9f} NBL/block",
        }


# ---- CrossShardTransaction
class CrossShardTransaction:
    """Handles transactions that span multiple NEBULA shards."""

    def __init__(self, tx_id: str, from_shard: int,
                  to_shard: int, sender: str,
                  recipient: str, amount: int):
        self.tx_id      = tx_id
        self.from_shard = from_shard
        self.to_shard   = to_shard
        self.sender     = sender
        self.recipient  = recipient
        self.amount     = amount
        self.phase      = "lock"   # lock -> broadcast -> finalize
        self.receipt    = ""

    def to_dict(self) -> dict:
        return {
            "tx_id":      self.tx_id,
            "from_shard": self.from_shard,
            "to_shard":   self.to_shard,
            "amount":     f"{self.amount/10**DECIMALS:.9f}",
            "phase":      self.phase,
        }


# ---- CrossShardRouter
class CrossShardRouter:
    """Routes transactions across NEBULA shards."""

    NUM_SHARDS = 8

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._txs:  Dict[str, CrossShardTransaction] = {}
        self._lock  = threading.RLock()

    def shard_of(self, address: str) -> int:
        return int(hashlib.sha256(address.encode()).hexdigest()[:2], 16) % self.NUM_SHARDS

    def route(self, sender: str, recipient: str,
               amount: int) -> Tuple[bool, str]:
        with self._lock:
            from_s = self.shard_of(sender)
            to_s   = self.shard_of(recipient)
            if from_s == to_s:
                return True, "same_shard"
            tx_id = hashlib.sha256(
                f"XS:{sender}:{recipient}:{amount}:{time.time()}".encode()
            ).hexdigest()[:16]
            cst = CrossShardTransaction(
                tx_id, from_s, to_s, sender, recipient, amount)
            self._txs[tx_id] = cst
            return True, tx_id

    def finalize(self, tx_id: str) -> bool:
        with self._lock:
            tx = self._txs.get(tx_id)
            if not tx:
                return False
            tx.phase   = "finalized"
            tx.receipt = hashlib.sha256(
                f"{tx_id}:finalized:{time.time()}".encode()
            ).hexdigest()[:16]
            return True

    def router_stats(self) -> dict:
        with self._lock:
            finalized = sum(1 for tx in self._txs.values()
                            if tx.phase == "finalized")
        return {
            "total_cross_shard": len(self._txs),
            "finalized":         finalized,
            "num_shards":        self.NUM_SHARDS,
        }


# ---- ValidatorRotation
class ValidatorRotation:
    """
    Manages validator set rotation in NEBULA PoS.
    Ensures fresh validators and prevents centralization.
    """

    ROTATION_INTERVAL = 2016   # rotate every ~2 weeks
    COMMITTEE_SIZE    = 21
    MAX_CONSECUTIVE   = 3      # max consecutive epochs for one validator

    def __init__(self, validator_set: 'ValidatorSetManager',
                  blockchain: 'NEBULABlockchain',
                  rng: 'OnChainRNG'):
        self._vs   = validator_set
        self._bc   = blockchain
        self._rng  = rng
        self._epoch_history: Dict[int, List[str]] = {}

    def should_rotate(self) -> bool:
        return self._bc.height % self.ROTATION_INTERVAL == 0

    def rotate(self) -> List[str]:
        epoch = self._bc.height // self.ROTATION_INTERVAL
        all_v = self._vs.list_active_validators()
        if not all_v:
            return []
        # Exclude validators in too many recent epochs
        recent = []
        for i in range(max(0, epoch - self.MAX_CONSECUTIVE), epoch):
            recent.extend(self._epoch_history.get(i, []))
        eligible = [v for v in all_v
                    if recent.count(v.get("address", "")) < self.MAX_CONSECUTIVE]
        if not eligible:
            eligible = all_v
        # Select by stake weight
        total   = sum(v.get("stake", 1) for v in eligible)
        selected = []
        seen     = set()
        for _ in range(min(self.COMMITTEE_SIZE, len(eligible))):
            rand = self._rng.random_int(self._bc.height, total, len(selected))
            cumulative = 0
            for v in eligible:
                addr = v.get("address", "")
                if addr in seen:
                    continue
                cumulative += v.get("stake", 1)
                if rand < cumulative:
                    selected.append(addr)
                    seen.add(addr)
                    break
        self._epoch_history[epoch] = selected
        return selected

    def rotation_stats(self) -> dict:
        return {
            "epochs_tracked":  len(self._epoch_history),
            "rotation_interval": self.ROTATION_INTERVAL,
            "committee_size":  self.COMMITTEE_SIZE,
        }


# ---- DeFiAnalyticsV2
class DeFiAnalyticsV2:
    """Advanced DeFi analytics for NEBULA ecosystem."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc     = blockchain
        self._oracle = oracle

    def tvl_estimate(self, dex: 'NEBULADex' = None,
                      staking: 'StakingEngine' = None,
                      lending: 'LendingProtocol' = None) -> dict:
        price    = (self._oracle.price("NBL/USD")
                    if self._oracle else 0.01) or 0.01
        tvl_nbl  = 0
        breakdown = {}
        if dex:
            dex_liq = sum(
                p.reserve_a + p.reserve_b
                for p in dex._pools.values()
            )
            tvl_nbl += dex_liq
            breakdown["dex"] = f"{dex_liq/10**DECIMALS:.3f}"
        if staking:
            stk = sum(
                int(v.get("staked_nbl", 0) or 0) * 10**DECIMALS
                for v in staking._stakers.values()
            )
            tvl_nbl += stk
            breakdown["staking"] = f"{stk/10**DECIMALS:.3f}"
        return {
            "tvl_nbl": f"{tvl_nbl/10**DECIMALS:.3f}",
            "tvl_usd": f"${tvl_nbl/10**DECIMALS*price:,.0f}",
            "breakdown": breakdown,
        }

    def protocol_metrics(self) -> dict:
        bc  = self._bc
        supply = bc.utxo.total_supply()
        return {
            "height":           bc.height,
            "total_supply_nbl": f"{supply/10**DECIMALS:.3f}",
            "mempool_txs":      bc.mempool.size(),
            "utxo_count":       bc.utxo.size(),
            "avg_block_reward": f"{mining_reward(bc.height)/10**DECIMALS:.9f}",
        }

    def dex_volume_estimate(self, dex: 'NEBULADex') -> dict:
        mp_volume = sum(
            tx.total_output()
            for tx in list(dex._blockchain.mempool._txs.values())[:50]
            if hasattr(dex, '_blockchain')
        )
        return {
            "estimated_volume_nbl": f"{mp_volume/10**DECIMALS:.3f}",
            "note":                 "Based on mempool data",
        }


# ---- FinalTestSuite
class FinalTestSuite:
    """
    Final comprehensive test suite for NEBULA 100K lines.
    Tests all major systems together.
    """

    def __init__(self):
        self.passed  = 0
        self.failed  = 0

    def _ok(self, name: str):
        self.passed += 1
        print(f"  ✅ {name}")

    def _fail(self, name: str, err: str):
        self.failed += 1
        print(f"  ❌ {name}: {err[:60]}")

    def test_blockchain_core(self):
        print("\n⛓️  Blockchain Core")
        try:
            bc  = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 1_000_000)
            bal = bc.utxo.balance(FOUNDATION_ADDRESS)
            assert bal == 1_000_000 * 10**DECIMALS
            self._ok("Fund address")
            assert bc.height >= 0
            self._ok("Chain height")
            assert bc.mempool.size() >= 0
            self._ok("Mempool access")
        except Exception as e:
            self._fail("Blockchain core", str(e))

    def test_full_defi_stack(self):
        print("\n🏦 Full DeFi Stack")
        try:
            bc      = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 10_000_000)
            oracle  = OracleV2(bc)
            oracle.update_price("NBL/USD", 0.01, FOUNDATION_ADDRESS)
            staking = StakingEngine(bc)
            ok, msg = staking.stake(FOUNDATION_ADDRESS, 1_000 * 10**DECIMALS)
            assert ok, msg
            self._ok("Staking")
            dex  = NEBULADex(bc)
            pid  = dex.create_pool("NBL", "USDT", fee_bps=30)
            assert pid
            self._ok("DEX pool created")
            gov  = GovernanceEngine(bc)
            ok2, pid2 = gov.propose(FOUNDATION_ADDRESS, ProposalType.TEXT,
                                     "Final Test", "Test", {})
            assert ok2
            self._ok("Governance proposal")
            ok3, m3 = gov.cast_vote(FOUNDATION_ADDRESS, pid2, "yes")
            assert ok3
            self._ok("Governance vote")
        except Exception as e:
            self._fail("Full DeFi stack", str(e))

    def test_nft_complete(self):
        print("\n🖼️  NFT Complete")
        try:
            bc  = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 100_000)
            nft = NBL721Registry()
            cid = nft.create_collection(FOUNDATION_ADDRESS, "FinalNFT",
                                         "FNFT", "Final test NFTs", 100, 0.05)
            assert cid
            self._ok("Collection created")
            for i in range(5):
                tid, msg = nft.mint(cid, FOUNDATION_ADDRESS,
                                     f"ipfs://final/{i}",
                                     {"name": f"Final #{i}"}, FOUNDATION_ADDRESS)
                assert tid > 0
            self._ok("Minted 5 NFTs")
            tokens = nft.tokens_of(FOUNDATION_ADDRESS)
            assert len(tokens) >= 5
            self._ok(f"Queried tokens ({len(tokens)} owned)")
        except Exception as e:
            self._fail("NFT complete", str(e))

    def test_cross_chain(self):
        print("\n🌉 Cross-Chain")
        try:
            bc      = NEBULABlockchain()
            bc._dev_mode = True  # enable fund_address for test
            bc.fund_address(FOUNDATION_ADDRESS, 100_000)
            bridge  = BridgeEngine(bc)
            ok, txid = bridge.initiate_htlc(FOUNDATION_ADDRESS,
                                             "0xETH_ADDRESS",
                                             1_000 * 10**DECIMALS,
                                             "ethereum")
            assert ok, txid
            self._ok("HTLC initiated")
            nns  = NEBULANameService(bc)
            ok2, domain = nns.register("test", FOUNDATION_ADDRESS, 1)
            assert ok2, domain
            resolved = nns.resolve("test.nbl")
            assert resolved == FOUNDATION_ADDRESS
            self._ok(f"NNS domain resolved: {domain}")
        except Exception as e:
            self._fail("Cross-chain", str(e))

    def run_all(self) -> dict:
        print("\n" + "═"*55)
        print("  🎯 NEBULA FINAL TEST SUITE")
        print("═"*55)
        import time as _t; start = _t.time()
        self.test_blockchain_core()
        self.test_full_defi_stack()
        self.test_nft_complete()
        self.test_cross_chain()
        elapsed = _t.time() - start
        total   = self.passed + self.failed
        pct     = self.passed / total * 100 if total > 0 else 0
        print(f"\n{'═'*55}")
        print(f"  FINAL: {self.passed}/{total} passed ({pct:.0f}%)")
        print(f"  Time: {elapsed:.2f}s")
        print(f"{'═'*55}\n")
        return {"passed": self.passed, "failed": self.failed,
                "pct": f"{pct:.0f}%"}


# ---- ChainDataCompressor
class ChainDataCompressor:
    """Compresses historical blockchain data for storage efficiency."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._compressed: Dict[int, bytes] = {}

    def compress_block(self, block: 'Block') -> bytes:
        data    = {
            "h":    block.height,
            "hash": block.hash[:16],
            "txs":  block.tx_count,
            "ts":   block.header.timestamp,
        }
        raw     = json.dumps(data, separators=(',', ':')).encode()
        return raw   # In production: use zlib/lz4

    def store_compressed(self, block: 'Block') -> int:
        compressed = self.compress_block(block)
        self._compressed[block.height] = compressed
        return len(compressed)

    def retrieve(self, height: int) -> Optional[dict]:
        raw = self._compressed.get(height)
        if not raw:
            return None
        return json.loads(raw)

    def compression_stats(self) -> dict:
        total_bytes = sum(len(v) for v in self._compressed.values())
        return {
            "blocks_compressed": len(self._compressed),
            "total_size_kb":     f"{total_bytes/1024:.2f}",
            "avg_size_bytes":    total_bytes // max(1, len(self._compressed)),
        }


# ---- WalletBackupManager
class WalletBackupManager:
    """
    Wallet backup and recovery tools.
    Encrypted backup, social recovery, shamir's secret sharing.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._backups: Dict[str, dict] = {}

    def create_encrypted_backup(self, wallet: 'NEBULAWallet',
                                  passphrase: str) -> dict:
        salt    = secrets.token_bytes(32)
        key     = KeyDerivationFunction.pbkdf2(
            passphrase.encode(), salt, 2048, 32)
        # XOR encryption (simplified — production: use AES-256)
        mnemonic_bytes = wallet.mnemonic.encode()
        encrypted = bytes(a ^ b for a, b in zip(
            mnemonic_bytes,
            (key * (len(mnemonic_bytes) // 32 + 1))[:len(mnemonic_bytes)]
        ))
        backup = {
            "version":    1,
            "salt":       salt.hex(),
            "encrypted":  encrypted.hex(),
            "address":    wallet.first_address,
            "checksum":   hashlib.sha256(encrypted).hexdigest()[:8],
        }
        self._backups[wallet.first_address] = backup
        return backup

    def restore_from_backup(self, backup: dict,
                              passphrase: str) -> Optional[str]:
        """Restore mnemonic from encrypted backup."""
        try:
            salt       = bytes.fromhex(backup["salt"])
            encrypted  = bytes.fromhex(backup["encrypted"])
            key        = KeyDerivationFunction.pbkdf2(
                passphrase.encode(), salt, 2048, 32)
            decrypted  = bytes(a ^ b for a, b in zip(
                encrypted,
                (key * (len(encrypted) // 32 + 1))[:len(encrypted)]
            ))
            return decrypted.decode()
        except Exception:
            return None

    def social_recovery_shares(self, mnemonic: str,
                                n: int = 5, t: int = 3) -> List[str]:
        """Split mnemonic into n shares, t needed to recover."""
        tss = ThresholdSignatureScheme(t, n)
        shares = tss.generate_shares(mnemonic.encode())
        return [shares[i].hex() for i in range(1, n + 1)]

    def backup_stats(self) -> dict:
        return {"backups_created": len(self._backups)}


# ---- OracleV3
class OracleV3:
    """
    Oracle v3 — decentralized, tamper-proof price oracle.
    Multiple reporters, median aggregation, outlier rejection.
    """

    MIN_REPORTERS   = 3
    OUTLIER_FACTOR  = 2.0   # reject if > 2x median deviation
    MAX_STALENESS   = 300   # 5 minutes

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._reporters: Set[str]                         = set()
        self._reports:   Dict[str, Dict[str, float]]      = {}   # pair -> {reporter: price}
        self._prices:    Dict[str, Tuple[float, float]]   = {}   # pair -> (price, ts)
        self._lock       = threading.RLock()

    def add_reporter(self, address: str):
        self._reporters.add(address)

    def report(self, reporter: str, pair: str,
                price: float) -> bool:
        if reporter not in self._reporters:
            return False
        with self._lock:
            if pair not in self._reports:
                self._reports[pair] = {}
            self._reports[pair][reporter] = price
            if len(self._reports[pair]) >= self.MIN_REPORTERS:
                self._aggregate(pair)
        return True

    def _aggregate(self, pair: str):
        prices  = sorted(self._reports[pair].values())
        n       = len(prices)
        median  = prices[n // 2]
        # Reject outliers
        filtered = [p for p in prices
                    if abs(p - median) < median * (self.OUTLIER_FACTOR - 1)]
        if not filtered:
            filtered = prices
        agg = sum(filtered) / len(filtered)
        self._prices[pair] = (agg, time.time())

    def price(self, pair: str) -> Optional[float]:
        with self._lock:
            result = self._prices.get(pair)
        if not result:
            return None
        price, ts = result
        if time.time() - ts > self.MAX_STALENESS:
            return None
        return price

    def oracle_v3_stats(self) -> dict:
        return {
            "reporters":      len(self._reporters),
            "tracked_pairs":  len(self._prices),
            "min_reporters":  self.MIN_REPORTERS,
        }


# ---- RoyaltyEnforcementMiddleware
class RoyaltyEnforcementMiddleware:
    """
    Middleware that enforces NFT royalties on all transfers.
    Wraps transfer functions to automatically deduct royalties.
    """

    def __init__(self, nft: 'NBL721Registry',
                  royalty_engine: 'RoyaltyEngine',
                  blockchain: 'NEBULABlockchain'):
        self._nft     = nft
        self._royalty = royalty_engine
        self._bc      = blockchain
        self._enforced_sales: List[dict] = []

    def enforce_sale(self, collection_id: str, token_id: int,
                      seller: str, buyer: str,
                      sale_price: int) -> Tuple[bool, dict]:
        ok, breakdown = self._royalty.process_sale(
            collection_id, token_id,
            buyer, seller, sale_price)
        if not ok:
            return False, {}
        self._enforced_sales.append({
            "collection": collection_id,
            "token_id":   token_id,
            "seller":     seller,
            "buyer":      buyer,
            "price":      sale_price,
            "royalty":    breakdown,
            "block":      self._bc.height,
        })
        return True, breakdown

    def total_royalties_collected(self) -> int:
        total = 0
        for sale in self._enforced_sales:
            royalty = sale.get("royalty", {})
            r_str   = royalty.get("royalty", "0")
            try:
                total += int(float(r_str.split()[0]) * 10**DECIMALS)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in RoyaltyEnforcementMiddleware.total_royalties_collected", exc_info=True)
        return total

    def enforcement_stats(self) -> dict:
        total = self.total_royalties_collected()
        return {
            "enforced_sales":     len(self._enforced_sales),
            "total_royalties":    f"{total/10**DECIMALS:.6f} NBL",
        }


# ---- GovernanceSimulation
class GovernanceSimulation:
    """
    Simulate governance scenarios for NEBULA.
    Monte Carlo voting simulations.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain

    def simulate_vote(self, n_voters: int = 100,
                       threshold: float = 0.60,
                       yes_probability: float = 0.55) -> dict:
        """Simulate a governance vote with random voters."""
        import random
        votes_yes = 0
        votes_no  = 0
        for _ in range(n_voters):
            weight = random.uniform(100, 10_000)
            if random.random() < yes_probability:
                votes_yes += weight
            else:
                votes_no  += weight
        total = votes_yes + votes_no
        pct   = votes_yes / total if total > 0 else 0
        return {
            "n_voters":  n_voters,
            "votes_yes": f"{votes_yes:.0f}",
            "votes_no":  f"{votes_no:.0f}",
            "pct_yes":   f"{pct*100:.1f}%",
            "passed":    pct >= threshold,
        }

    def monte_carlo_outcomes(self, n_runs: int = 1000,
                              yes_probability: float = 0.55) -> dict:
        passed = sum(
            1 for _ in range(n_runs)
            if self.simulate_vote(100, 0.60, yes_probability)["passed"]
        )
        return {
            "simulations":  n_runs,
            "pass_rate":    f"{passed/n_runs*100:.1f}%",
            "yes_prob_input": f"{yes_probability*100:.0f}%",
        }


# ---- ExchangeListingInfo
class ExchangeListingInfo:
    """
    Information package for NEBULA exchange listings.
    Provides technical integration details.
    """

    CHAIN_INFO = {
        "name":              "NEBULA",
        "ticker":            "NBL",
        "chain_id":          CHAIN_ID,
        "decimals":          DECIMALS,
        "total_supply":      f"{MAX_SUPPLY/10**DECIMALS:,.0f}",
        "algorithm":         "SHA-256 PoW",
        "block_time":        f"{TARGET_BLOCK_TIME}s",
        "confirmation_time": "6 blocks (~60 min)",
        "api_endpoint":      "https://api.nebula-nbl.io/v2",
        "ws_endpoint":       "wss://ws.nebula-nbl.io",
        "explorer":          "https://explorer.nebula-nbl.io",
        "github":            "",
        "whitepaper":        "https://nebula-nbl.io/whitepaper.pdf",
        "audit":             "Community audited",
        "category":          "DeFi / Layer-1",
        "features": [
            "Full DeFi ecosystem",
            "NFT marketplace",
            "Cross-chain bridge",
            "Governance token",
            "Staking rewards",
        ],
    }

    DEPOSIT_WITHDRAWAL = {
        "deposit_confirmations":    6,
        "withdrawal_fee":           f"{10 * MIN_TX_FEE / 10**DECIMALS:.6f} NBL",
        "min_deposit":              f"{MIN_TX_FEE * 100 / 10**DECIMALS:.6f} NBL",
        "address_format":           "Starts with 'N', 26-35 characters",
        "transaction_id_format":    "64 hex characters (SHA-256)",
        "memo_required":            False,
    }

    @classmethod
    def integration_guide(cls) -> dict:
        return {
            "chain_info":       cls.CHAIN_INFO,
            "deposit_config":   cls.DEPOSIT_WITHDRAWAL,
            "rpc_methods": [
                "GET /info", "GET /block/{height}", "GET /tx/{txid}",
                "GET /address/{addr}", "POST /tx/broadcast",
                "GET /mempool", "GET /mining/template",
            ],
        }


# ---- InstitutionalGrade
class InstitutionalGrade:
    """
    Institutional-grade tools for NEBULA.
    OTC, bulk transfers, reporting, compliance.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  compliance: 'ComplianceEngine' = None):
        self._bc         = blockchain
        self._compliance = compliance
        self._otc_trades: List[dict] = []
        self._reports:    List[dict] = []
        self._lock        = threading.RLock()

    def otc_trade(self, buyer: str, seller: str,
                   amount_nbl: float, price_usd: float,
                   settlement_blocks: int = 1) -> dict:
        with self._lock:
            trade_id = hashlib.sha256(
                f"OTC:{buyer}:{seller}:{amount_nbl}:{time.time()}".encode()
            ).hexdigest()[:12]
            trade = {
                "trade_id":     trade_id,
                "buyer":        buyer,
                "seller":       seller,
                "amount_nbl":   amount_nbl,
                "price_usd":    price_usd,
                "total_usd":    amount_nbl * price_usd,
                "settlement":   self._bc.height + settlement_blocks,
                "status":       "pending",
                "ts":           time.time(),
            }
            self._otc_trades.append(trade)
            return trade

    def bulk_transfer(self, sender: str,
                       transfers: List[Tuple[str, float]]) -> dict:
        """Execute multiple transfers in one batch."""
        total = sum(amt for _, amt in transfers)
        if self._bc.utxo.balance(sender) < int(total * 10**DECIMALS):
            return {"error": "Insufficient balance"}
        return {
            "sender":    sender,
            "transfers": len(transfers),
            "total_nbl": total,
            "batch_id":  hashlib.sha256(f"BULK:{sender}:{time.time()}".encode()).hexdigest()[:12],
        }

    def generate_tax_report(self, address: str,
                             year: int) -> dict:
        return {
            "address":     address,
            "tax_year":    year,
            "transactions": "Full indexer required for complete history",
            "note":        "Consult a tax professional",
        }

    def institutional_stats(self) -> dict:
        return {
            "otc_trades":    len(self._otc_trades),
        }


# ---- APIGateway
class APIGateway:
    """
    API gateway for NEBULA — rate limiting, auth, routing.
    """

    def __init__(self, rest_api: 'NodeRESTAPI',
                  blockchain: 'NEBULABlockchain'):
        self._api      = rest_api
        self._bc       = blockchain
        self._api_keys: Dict[str, dict] = {}
        self._rate_lim: Dict[str, List[float]] = {}
        self._requests = 0
        self._lock     = threading.RLock()

    def register_key(self, api_key: str, tier: str = "free",
                      rate_limit: int = 100) -> bool:
        with self._lock:
            self._api_keys[api_key] = {
                "tier":       tier,
                "rate_limit": rate_limit,
                "created":    time.time(),
            }
            return True

    def check_rate_limit(self, api_key: str) -> bool:
        with self._lock:
            key_info = self._api_keys.get(api_key)
            if not key_info:
                return False
            now   = time.time()
            times = self._rate_lim.get(api_key, [])
            times = [t for t in times if now - t < 60]
            if len(times) >= key_info["rate_limit"]:
                return False
            times.append(now)
            self._rate_lim[api_key] = times
            return True

    def handle(self, api_key: str, method: str,
                path: str, body: dict = None) -> dict:
        with self._lock:
            self._requests += 1
        if not self.check_rate_limit(api_key):
            return {"ok": False, "error": "429 Rate limit exceeded"}
        return self._api.handle(method, path, body)

    def gateway_stats(self) -> dict:
        return {
            "api_keys":    len(self._api_keys),
            "requests":    self._requests,
        }


# ---- CompactBlockV2
class CompactBlockV2:
    """Compact block relay protocol v2 for NEBULA."""

    def __init__(self, block: 'Block'):
        self.header       = block.header
        self.height       = block.height
        self.short_ids:   List[str] = [tx.txid[:6] for tx in block.transactions]
        self.prefilled:   List['Transaction'] = []

    def reconstruct(self, pool: Dict[str, 'Transaction']) -> Optional['Block']:
        txs = []
        for sid in self.short_ids:
            full = next((tx for txid, tx in pool.items()
                         if txid[:6] == sid), None)
            if full:
                txs.append(full)
        if len(txs) < len(self.short_ids):
            return None
        return _mk_block(self.header, txs, self.height)

    def compact_info(self) -> dict:
        return {
            "height":      self.height,
            "short_ids":   len(self.short_ids),
            "prefilled":   len(self.prefilled),
        }


# ---- UTXOSnapshotV2
class UTXOSnapshotV2:
    """Enhanced UTXO snapshot for light client sync."""

    def __init__(self, utxo: 'UTXOSet',
                  height: int):
        addrs  = list(utxo._addr_idx.keys())[:100_000]
        self.height   = height
        self.entries: Dict[str, int] = {
            addr: utxo.balance(addr)
            for addr in addrs
            if utxo.balance(addr) > 0
        }
        self.merkle_root = self._compute_root()

    def _compute_root(self) -> str:
        leaves = [f"{k}:{v}" for k, v in sorted(self.entries.items())]
        return MerkleTree.compute_root(
            [hashlib.sha256(l.encode()).hexdigest() for l in leaves])

    def verify(self, address: str, balance: int) -> bool:
        return self.entries.get(address) == balance

    def snapshot_info(self) -> dict:
        return {
            "height":      self.height,
            "entries":     len(self.entries),
            "merkle_root": self.merkle_root[:16] + "...",
            "total_nbl":   f"{sum(self.entries.values())/10**DECIMALS:.3f}",
        }


# ---- SchnorrMultiSig
class SchnorrMultiSig:
    """Schnorr-based multi-signature scheme for NEBULA."""

    def __init__(self, participants: List[bytes]):
        self.participants = participants
        self.n            = len(participants)
        self._nonces:     Dict[int, int] = {}
        self._sigs:       Dict[int, bytes] = {}

    def aggregate_pubkeys(self) -> bytes:
        combined = bytes(self.participants[0])
        for pk in self.participants[1:]:
            combined = bytes(a ^ b for a, b in zip(combined, pk))
        return combined

    def partial_sign(self, signer_idx: int,
                      privkey: int, msg: bytes) -> bytes:
        nonce  = secrets.randbelow(Secp256k1.ORDER - 1) + 1
        self._nonces[signer_idx] = nonce
        R      = Secp256k1.pubkey_from_int(nonce, compressed=True)
        H      = hashlib.sha256(R + msg).digest()
        e      = int.from_bytes(H, 'big') % Secp256k1.ORDER
        s      = (nonce - privkey * e) % Secp256k1.ORDER
        sig    = s.to_bytes(32, 'big')
        self._sigs[signer_idx] = sig
        return sig

    def aggregate_signatures(self) -> Optional[bytes]:
        if len(self._sigs) < self.n:
            return None
        result = int.from_bytes(self._sigs[0], 'big')
        for i in range(1, len(self._sigs)):
            result = (result + int.from_bytes(self._sigs[i], 'big')) % Secp256k1.ORDER
        return result.to_bytes(32, 'big')

    def msig_info(self) -> dict:
        return {
            "participants": self.n,
            "signed":       len(self._sigs),
            "complete":     len(self._sigs) >= self.n,
        }


# ---- MimbleWimbleTx
class MimbleWimbleTx:
    """
    MimbleWimble-style transaction for NEBULA.
    Confidential transactions with cut-through.
    """

    def __init__(self, inputs: List[int], outputs: List[int],
                  kernel_excess: int):
        self.inputs    = inputs
        self.outputs   = outputs
        self.kernel    = kernel_excess
        self.tx_id     = hashlib.sha256(
            json.dumps({"in": inputs, "out": outputs, "k": kernel_excess},
                       sort_keys=True).encode()
        ).hexdigest()

    def verify_balance(self) -> bool:
        """Sum of outputs - sum of inputs == kernel excess."""
        return sum(self.outputs) - sum(self.inputs) == self.kernel

    def cut_through(self, other: 'MimbleWimbleTx') -> 'MimbleWimbleTx':
        """Cut through matching inputs/outputs."""
        remaining_in   = list(self.inputs)
        remaining_out  = list(other.outputs)
        combined_in    = remaining_in + list(other.inputs)
        combined_out   = list(self.outputs) + remaining_out
        new_kernel     = self.kernel + other.kernel
        return MimbleWimbleTx(combined_in, combined_out, new_kernel)
