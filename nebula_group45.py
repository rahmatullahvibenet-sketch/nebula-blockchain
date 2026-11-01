"""NEBULA group45 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. ConsensusMetrics  (orig. lines 72852-72909)
   2. SmartOrderRouter  (orig. lines 72916-72975)
   3. TokenEconomicsV2  (orig. lines 72982-73037)
   4. LiquidityAggregator  (orig. lines 73044-73093)
   5. GasStation  (orig. lines 73100-73150)
   6. DeFiPassport  (orig. lines 73157-73199)
   7. DeFiPassportRegistry  (orig. lines 73201-73238)
   8. InsuranceFund  (orig. lines 73245-73301)
   9. HackathonEvent  (orig. lines 73308-73391)
  10. RoyaltyEngine  (orig. lines 73480-73529)
  11. MerkleAirdrop  (orig. lines 73536-73591)
  12. StakingBoost  (orig. lines 73598-73643)
  13. TransactionMixer  (orig. lines 73650-73701)
  14. EconomicSecurityAnalyzer  (orig. lines 73712-73750)
  15. ArchiveNode  (orig. lines 73757-73808)
  16. GovernanceAnalytics  (orig. lines 73815-73860)
  17. NodeHealthCheck  (orig. lines 73867-73918)
  18. FeeHistoryAnalyzer  (orig. lines 73925-73988)
  19. ValidatorRewardTracker  (orig. lines 74000-74053)
  20. CrossDEXArbitrage  (orig. lines 74060-74114)

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
DECIMALS            = 9

MAX_SUPPLY          = 21_000_000 * (10 ** DECIMALS)   # in Neb  (matches 50 NBL * 210,000 blocks * 2 geometric series)

FOUNDATION_ADDRESS     = "NdoZxCWQfYDy4412S1Zqh8AWj9T5aKqmkx"  # NEBULA Core Team

INITIAL_BLOCK_REWARD   = 50 * (10 ** DECIMALS)        # 50 NBL

HALVING_INTERVAL       = 210_000                        # blocks

TARGET_BLOCK_TIME      = 600                            # 10 minutes (like Bitcoin)

MAX_TARGET             = 0x0fffff * (256 ** ((0x1e if __import__('os').environ.get('NEBULA_NETWORK','mainnet').strip().lower() == 'regtest' else 0x1d) - 3))   # [v10.24]   # bits_to_target(INITIAL_BITS) — max allowed PoW target

MIN_TX_FEE             = 1_000                          # 0.000001 NBL minimum fee

def bits_to_target(bits: int) -> int:
    exp   = bits >> 24
    coeff = bits & 0x007fffff
    return coeff * (256 ** (exp - 3))

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


# ---- ConsensusMetrics
class ConsensusMetrics:
    """Track and analyze NEBULA consensus health."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc            = blockchain
        self._block_times:  List[float] = []
        self._orphan_count  = 0
        self._reorg_count   = 0
        self._reorg_depths: List[int] = []
        self._lock          = threading.RLock()

    def record_block(self, block: 'Block', prev_timestamp: float):
        with self._lock:
            interval = block.header.timestamp - prev_timestamp
            if interval > 0:
                self._block_times.append(interval)
            if len(self._block_times) > 2016:
                self._block_times.pop(0)

    def record_orphan(self):
        with self._lock:
            self._orphan_count += 1

    def record_reorg(self, depth: int):
        with self._lock:
            self._reorg_count += 1
            self._reorg_depths.append(depth)

    def avg_block_time(self, window: int = 144) -> float:
        with self._lock:
            recent = self._block_times[-window:]
        return sum(recent) / len(recent) if recent else TARGET_BLOCK_TIME

    def block_time_std(self) -> float:
        bt   = self.avg_block_time()
        with self._lock:
            recent = self._block_times[-144:]
        if len(recent) < 2:
            return 0.0
        var = sum((t - bt) ** 2 for t in recent) / len(recent)
        return var ** 0.5

    def consensus_health(self) -> dict:
        avg_bt = self.avg_block_time()
        dev    = abs(avg_bt - TARGET_BLOCK_TIME) / TARGET_BLOCK_TIME * 100
        return {
            "avg_block_time_s":  f"{avg_bt:.1f}",
            "target_s":          TARGET_BLOCK_TIME,
            "deviation_pct":     f"{dev:.1f}%",
            "block_time_std":    f"{self.block_time_std():.1f}s",
            "orphan_count":      self._orphan_count,
            "reorg_count":       self._reorg_count,
            "avg_reorg_depth":   (sum(self._reorg_depths) /
                                   len(self._reorg_depths)
                                   if self._reorg_depths else 0),
            "health":            "GOOD" if dev < 10 else
                                 "WARNING" if dev < 25 else "CRITICAL",
        }


# ---- SmartOrderRouter
class SmartOrderRouter:
    """
    Intelligent order routing across all NEBULA liquidity sources.
    Splits orders for best execution price.
    """

    def __init__(self, dex: 'NEBULADex',
                  order_book: 'OrderBookManager' = None):
        self._dex = dex
        self._ob  = order_book

    def get_quotes(self, token_in: str, token_out: str,
                    amount: int) -> List[dict]:
        quotes = []
        # AMM quote
        amm_out = self._dex.quote_amm(token_in, token_out, amount)
        if amm_out > 0:
            quotes.append({
                "source":    "AMM",
                "out":       amm_out,
                "price":     amm_out / amount if amount > 0 else 0,
            })
        return quotes

    def optimal_split(self, token_in: str, token_out: str,
                       amount: int, n_splits: int = 3) -> dict:
        """Split order across sources for best execution."""
        if n_splits < 1:
            n_splits = 1
        part_size = amount // n_splits
        total_out = 0
        splits    = []
        for i in range(n_splits):
            part = part_size if i < n_splits - 1 else amount - part_size * (n_splits - 1)
            quotes = self.get_quotes(token_in, token_out, part)
            if quotes:
                best = max(quotes, key=lambda q: q["out"])
                total_out += best["out"]
                splits.append({"amount": part, "source": best["source"],
                                "out": best["out"]})
        return {
            "token_in":    token_in,
            "token_out":   token_out,
            "total_in":    amount,
            "total_out":   total_out,
            "splits":      splits,
            "avg_price":   total_out / amount if amount > 0 else 0,
        }

    def execute_split_order(self, trader: str, token_in: str,
                             token_out: str, amount: int) -> Tuple[bool, int]:
        plan   = self.optimal_split(token_in, token_out, amount)
        total  = 0
        for split in plan["splits"]:
            if split["source"] == "AMM":
                ok, _, out = self._dex.swap_amm(
                    trader, token_in, token_out, split["amount"])
                if ok:
                    total += out
        return total > 0, total


# ---- TokenEconomicsV2
class TokenEconomicsV2:
    """
    Advanced token economics model for NEBULA.
    Models supply/demand dynamics, velocity, market cap.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc     = blockchain
        self._oracle = oracle

    def velocity(self, period_blocks: int = 144) -> float:
        """Token velocity = transaction volume / supply."""
        supply = self._bc.utxo.total_supply()
        if supply == 0:
            return 0.0
        mempool_volume = sum(
            tx.total_output()
            for tx in list(self._bc.mempool._txs.values())[:100]
        )
        return mempool_volume / supply

    def market_cap(self) -> dict:
        price  = (self._oracle.price("NBL/USD")
                  if self._oracle else 0.001) or 0.001
        supply = self._bc.utxo.total_supply() / 10**DECIMALS
        mc     = supply * price
        fdv    = MAX_SUPPLY / 10**DECIMALS * price
        return {
            "price_usd":      f"${price:.6f}",
            "circulating":    f"{supply:.3f} NBL",
            "market_cap":     f"${mc:,.0f}",
            "fdv":            f"${fdv:,.0f}",
            "mc_to_fdv":      f"{mc/fdv*100:.2f}%" if fdv > 0 else "0%",
        }

    def nvt_ratio(self) -> float:
        """Network Value to Transactions ratio."""
        price    = (self._oracle.price("NBL/USD")
                    if self._oracle else 0.001) or 0.001
        supply   = self._bc.utxo.total_supply() / 10**DECIMALS
        mc       = supply * price
        tx_vol   = self.velocity() * supply * price * 144   # daily
        return mc / tx_vol if tx_vol > 0 else 0

    def economics_report(self) -> dict:
        mc   = self.market_cap()
        vel  = self.velocity()
        nvt  = self.nvt_ratio()
        return {
            "market_cap":   mc,
            "velocity":     f"{vel:.6f}",
            "nvt_ratio":    f"{nvt:.2f}",
            "signal":       "undervalued" if nvt < 15 else
                            "fairly valued" if nvt < 50 else "overvalued",
        }


# ---- LiquidityAggregator
class LiquidityAggregator:
    """
    Aggregates liquidity across all NEBULA DeFi pools.
    Shows total available liquidity per token.
    """

    def __init__(self, dex: 'NEBULADex',
                  lending: 'LendingProtocol' = None):
        self._dex     = dex
        self._lending = lending

    def total_liquidity(self, token: str) -> dict:
        """Get total available liquidity for a token."""
        dex_liq     = 0
        lending_liq = 0
        # DEX liquidity
        for pool in self._dex._pools.values():
            if pool.token_a == token:
                dex_liq += pool.reserve_a
            elif pool.token_b == token:
                dex_liq += pool.reserve_b
        # Lending liquidity
        if self._lending:
            for asset, pool_data in self._lending._pools.items():
                if asset == token:
                    supply  = pool_data.get("total_supply", 0)
                    borrows = pool_data.get("total_borrows", 0)
                    lending_liq += supply - borrows
        return {
            "token":        token,
            "dex_liq":      f"{dex_liq/10**DECIMALS:.3f}",
            "lending_liq":  f"{lending_liq/10**DECIMALS:.3f}",
            "total":        f"{(dex_liq+lending_liq)/10**DECIMALS:.3f}",
        }

    def liquidity_map(self) -> dict:
        tokens = {"NBL", "USDT", "WBTC", "WETH", "USDC"}
        for pool in self._dex._pools.values():
            tokens.add(pool.token_a)
            tokens.add(pool.token_b)
        return {t: self.total_liquidity(t) for t in sorted(tokens)}

    def slippage_estimate(self, token: str,
                           trade_size: float) -> str:
        total = self.total_liquidity(token)
        total_f = float(total["total"].split()[0])
        if total_f == 0:
            return "∞"
        slippage = trade_size / total_f * 100
        return f"{slippage:.3f}%"


# ---- GasStation
class GasStation:
    """
    Gas station for NEBULA — allows users to pay fees in any token.
    Relayer pays NBL fees and gets reimbursed in user's token.
    """

    SUPPORTED_FEE_TOKENS = ["USDT", "USDC", "WBTC", "WETH"]
    FEE_MARGIN = 1.10   # 10% margin for relayer

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None,
                  relayer: str = FOUNDATION_ADDRESS):
        self._bc      = blockchain
        self._oracle  = oracle
        self._relayer = relayer
        self._relayed: List[dict] = []

    def estimate_fee_in_token(self, token: str,
                               tx_size_bytes: int = 250) -> float:
        nbl_fee   = MIN_TX_FEE * tx_size_bytes / 10**DECIMALS
        nbl_price = (self._oracle.price("NBL/USD")
                     if self._oracle else 0.01) or 0.01
        tok_price = 1.0   # assume $1 for stable coins
        if token == "WBTC":
            tok_price = (self._oracle.price("BTC/USD")
                         if self._oracle else 30000) or 30000
        nbl_usd   = nbl_fee * nbl_price * self.FEE_MARGIN
        return nbl_usd / tok_price

    def relay_transaction(self, user: str, token: str,
                           tx: 'Transaction') -> Tuple[bool, str]:
        if token not in self.SUPPORTED_FEE_TOKENS:
            return False, f"Token {token} not supported"
        fee_in_token = self.estimate_fee_in_token(token, tx.byte_size())
        ok, msg = self._bc.mempool.submit(tx)
        if ok:
            self._relayed.append({
                "user":     user,
                "token":    token,
                "fee":      fee_in_token,
                "txid":     tx.txid,
                "ts":       time.time(),
            })
        return ok, msg

    def gas_station_stats(self) -> dict:
        return {
            "relayer":       self._relayer,
            "relayed_txs":   len(self._relayed),
            "fee_tokens":    self.SUPPORTED_FEE_TOKENS,
        }


# ---- DeFiPassport
@dataclass
class DeFiPassport:
    """Cross-protocol DeFi reputation passport."""
    address:       str
    created_at:    float
    total_volume:  float = 0.0
    protocols:     Set[str]   = field(default_factory=set)
    badges:        List[str]  = field(default_factory=list)
    score:         int = 0

    BADGE_THRESHOLDS = {
        "First Trade":       ("volume", 1.0),
        "Volume 1000 NBL":   ("volume", 1000.0),
        "Volume 10000 NBL":  ("volume", 10000.0),
        "Multi-Protocol":    ("protocols", 3),
        "DeFi Veteran":      ("protocols", 5),
    }

    def update_volume(self, amount: float):
        self.total_volume += amount
        self._award_badges()

    def add_protocol(self, protocol: str):
        self.protocols.add(protocol)
        self._award_badges()

    def _award_badges(self):
        for badge, (metric, threshold) in self.BADGE_THRESHOLDS.items():
            if badge in self.badges:
                continue
            val = self.total_volume if metric == "volume" else len(self.protocols)
            if val >= threshold:
                self.badges.append(badge)
        self.score = len(self.badges) * 10 + int(self.total_volume / 100)

    def to_dict(self) -> dict:
        return {
            "address":      self.address,
            "score":        self.score,
            "protocols":    len(self.protocols),
            "badges":       self.badges,
            "volume_nbl":   f"{self.total_volume:.3f}",
        }


# ---- DeFiPassportRegistry
class DeFiPassportRegistry:
    """Registry of DeFi passports."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._passports: Dict[str, DeFiPassport] = {}
        self._lock      = threading.RLock()

    def get_or_create(self, address: str) -> DeFiPassport:
        with self._lock:
            if address not in self._passports:
                self._passports[address] = DeFiPassport(
                    address=address, created_at=time.time())
            return self._passports[address]

    def record_activity(self, address: str, protocol: str,
                         volume_nbl: float):
        pp = self.get_or_create(address)
        pp.update_volume(volume_nbl)
        pp.add_protocol(protocol)

    def leaderboard(self, n: int = 20) -> List[dict]:
        with self._lock:
            sorted_pp = sorted(
                self._passports.values(),
                key=lambda p: p.score,
                reverse=True
            )
        return [{"rank": i+1, **p.to_dict()}
                for i, p in enumerate(sorted_pp[:n])]

    def registry_stats(self) -> dict:
        with self._lock:
            total_vol = sum(p.total_volume for p in self._passports.values())
        return {
            "total_passports": len(self._passports),
            "total_volume_nbl": f"{total_vol:.3f}",
        }


# ---- InsuranceFund
class InsuranceFund:
    """
    Protocol-wide insurance fund.
    Auto-grows from protocol fees, pays out on hacks.
    """

    TARGET_COVERAGE_PCT = 0.10   # target 10% of TVL

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._fund:  int = 0
        self._claims: List[dict] = []
        self._lock   = threading.RLock()

    def deposit(self, amount: int):
        with self._lock:
            self._fund += amount

    def file_claim(self, claimant: str, amount: int,
                    evidence: str, incident: str) -> str:
        with self._lock:
            cid = hashlib.sha256(
                f"INSCLAIM:{claimant}:{amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._claims.append({
                "claim_id": cid,
                "claimant": claimant,
                "amount":   amount,
                "evidence": evidence,
                "incident": incident,
                "status":   "pending",
                "filed_at": time.time(),
            })
            return cid

    def approve_claim(self, claim_id: str,
                       approver: str) -> Tuple[bool, int]:
        with self._lock:
            claim = next((c for c in self._claims
                          if c["claim_id"] == claim_id), None)
            if not claim or claim["status"] != "pending":
                return False, 0
            payout = min(claim["amount"], self._fund)
            self._fund  -= payout
            claim["status"] = "paid"
            return True, payout

    def insurance_fund_stats(self) -> dict:
        with self._lock:
            pending = sum(1 for c in self._claims if c["status"] == "pending")
            paid    = sum(c["amount"] for c in self._claims if c["status"] == "paid")
        return {
            "fund_balance_nbl": f"{self._fund/10**DECIMALS:.3f}",
            "total_claims":     len(self._claims),
            "pending_claims":   pending,
            "total_paid_nbl":   f"{paid/10**DECIMALS:.3f}",
        }


# ---- HackathonEvent
class HackathonEvent:
    """NEBULA hackathon event management."""

    def __init__(self, name: str, prize_pool: float,
                  start_block: int, end_block: int,
                  blockchain: 'NEBULABlockchain'):
        self.name        = name
        self.prize_pool  = int(prize_pool * 10**DECIMALS)
        self.start_block = start_block
        self.end_block   = end_block
        self._bc         = blockchain
        self.submissions: Dict[str, dict] = {}
        self.judges:      List[str]       = []
        self.scores:      Dict[str, float] = {}

    def register_team(self, team_name: str, members: List[str],
                       project: str) -> bool:
        if team_name in self.submissions:
            return False
        self.submissions[team_name] = {
            "members":    members,
            "project":    project,
            "repo":       "",
            "score":      0.0,
            "submitted":  False,
        }
        return True

    def submit(self, team: str, repo_url: str,
                demo_url: str) -> bool:
        s = self.submissions.get(team)
        if not s:
            return False
        if self._bc.height > self.end_block:
            return False
        s["repo"]      = repo_url
        s["demo"]      = demo_url
        s["submitted"] = True
        return True

    def judge_score(self, judge: str, team: str,
                     score: float) -> bool:
        if judge not in self.judges:
            return False
        key = f"{judge}:{team}"
        self.scores[key] = score
        team_scores = [self.scores[f"{j}:{team}"]
                       for j in self.judges
                       if f"{j}:{team}" in self.scores]
        if team_scores:
            self.submissions[team]["score"] = sum(team_scores) / len(team_scores)
        return True

    def winners(self, top_n: int = 3) -> List[dict]:
        submitted = [(t, s) for t, s in self.submissions.items()
                     if s["submitted"]]
        sorted_t  = sorted(submitted, key=lambda x: -x[1]["score"])
        prizes    = [0.50, 0.30, 0.20]   # 50/30/20% distribution
        result    = []
        for i, (team, info) in enumerate(sorted_t[:top_n]):
            pct   = prizes[i] if i < len(prizes) else 0
            prize = int(self.prize_pool * pct)
            result.append({
                "rank":    i + 1,
                "team":    team,
                "project": info["project"],
                "score":   info["score"],
                "prize":   f"{prize/10**DECIMALS:.3f} NBL",
            })
        return result

    def hackathon_info(self) -> dict:
        cur = self._bc.height
        return {
            "name":         self.name,
            "prize_pool":   f"{self.prize_pool/10**DECIMALS:.3f} NBL",
            "start":        self.start_block,
            "end":          self.end_block,
            "status":       ("upcoming" if cur < self.start_block else
                             "active" if cur <= self.end_block else "ended"),
            "teams":        len(self.submissions),
            "submitted":    sum(1 for s in self.submissions.values()
                                if s["submitted"]),
        }


# ---- RoyaltyEngine
class RoyaltyEngine:
    """
    On-chain royalty enforcement for NFTs.
    Automatically distributes royalties on every sale.
    """

    def __init__(self, nft_registry: 'NBL721Registry',
                  blockchain: 'NEBULABlockchain'):
        self._nft    = nft_registry
        self._bc     = blockchain
        self._royalties_paid: Dict[str, int] = {}   # collection -> total paid
        self._lock   = threading.RLock()

    def calculate_royalty(self, collection_id: str,
                           sale_price: int) -> Tuple[str, int]:
        """Returns (creator_address, royalty_amount)."""
        col = self._nft._collections.get(collection_id)
        if not col:
            return "", 0
        creator  = col.get("creator", "")
        rate     = col.get("royalty_pct", 0.0)
        royalty  = int(sale_price * rate)
        return creator, royalty

    def process_sale(self, collection_id: str, token_id: int,
                      buyer: str, seller: str,
                      sale_price: int) -> Tuple[bool, dict]:
        with self._lock:
            creator, royalty = self.calculate_royalty(collection_id, sale_price)
            seller_amount = sale_price - royalty
            self._royalties_paid[collection_id] = (
                self._royalties_paid.get(collection_id, 0) + royalty)
            return True, {
                "sale_price":    f"{sale_price/10**DECIMALS:.6f}",
                "royalty":       f"{royalty/10**DECIMALS:.6f}",
                "seller_gets":   f"{seller_amount/10**DECIMALS:.6f}",
                "creator":       creator,
                "royalty_pct":   self._nft._collections.get(
                                   collection_id, {}).get("royalty_pct", 0),
            }

    def royalty_stats(self, collection_id: str = None) -> dict:
        with self._lock:
            if collection_id:
                paid = self._royalties_paid.get(collection_id, 0)
                return {"collection": collection_id,
                        "total_paid": f"{paid/10**DECIMALS:.6f}"}
            total = sum(self._royalties_paid.values())
            return {"total_royalties_paid": f"{total/10**DECIMALS:.6f}",
                    "collections":          len(self._royalties_paid)}


# ---- MerkleAirdrop
class MerkleAirdrop:
    """
    Merkle-tree based airdrop — gas-efficient claims.
    Stores only root on-chain; users provide their own proof.
    """

    def __init__(self, token: str, merkle_root: str,
                  blockchain: 'NEBULABlockchain'):
        self.token       = token
        self.merkle_root = merkle_root
        self._bc         = blockchain
        self._claimed:   Set[str] = set()
        self._allocations: Dict[str, int] = {}   # addr -> amount
        self._lock       = threading.RLock()

    def set_allocations(self, allocations: Dict[str, int]):
        with self._lock:
            self._allocations = dict(allocations)

    def claim(self, address: str,
               amount: int, proof: List[str]) -> Tuple[bool, str]:
        with self._lock:
            if address in self._claimed:
                return False, "Already claimed"
            if self._allocations.get(address, 0) != amount:
                return False, "Invalid allocation amount"
            # Verify Merkle proof
            leaf = hashlib.sha256(
                f"{address}:{amount}".encode()
            ).hexdigest()
            computed = leaf
            for p in proof:
                if computed < p:
                    combined = computed + p
                else:
                    combined = p + computed
                computed = hashlib.sha256(combined.encode()).hexdigest()
            if computed != self.merkle_root:
                return False, "Invalid Merkle proof"
            self._claimed.add(address)
            return True, f"Claimed {amount/10**DECIMALS:.6f} {self.token}"

    def claimable(self, address: str) -> bool:
        return (address in self._allocations and
                address not in self._claimed)

    def airdrop_stats(self) -> dict:
        total     = sum(self._allocations.values())
        claimed   = sum(self._allocations.get(a, 0) for a in self._claimed)
        return {
            "total_allocations": len(self._allocations),
            "claimed":           len(self._claimed),
            "total_amount":      f"{total/10**DECIMALS:.3f}",
            "claimed_amount":    f"{claimed/10**DECIMALS:.3f}",
            "remaining":         f"{(total-claimed)/10**DECIMALS:.3f}",
        }


# ---- StakingBoost
class StakingBoost:
    """
    Boost staking rewards based on veNBL holdings and NFT ownership.
    Incentivizes long-term alignment.
    """

    BASE_BOOST         = 1.0
    MAX_VENBL_BOOST    = 2.5   # up to 2.5x for max veNBL
    NFT_HOLDER_BONUS   = 0.10  # +10% for NFT holders

    def __init__(self, venbl: 'VoteEscrowedNBL',
                  nft: 'NBL721Registry'):
        self._venbl = venbl
        self._nft   = nft

    def compute_boost(self, address: str,
                       staked_amount: int) -> float:
        """Compute staking boost multiplier for an address."""
        boost = self.BASE_BOOST
        # veNBL boost (linear)
        venbl_bal = self._venbl.balance(address)
        if venbl_bal > 0 and staked_amount > 0:
            venbl_ratio = venbl_bal / staked_amount
            venbl_boost = min(self.MAX_VENBL_BOOST - 1, venbl_ratio)
            boost       += venbl_boost
        # NFT holder bonus
        owned_nfts  = self._nft.tokens_of(address)
        if owned_nfts:
            boost += self.NFT_HOLDER_BONUS * min(5, len(owned_nfts))
        return min(boost, self.MAX_VENBL_BOOST + 5 * self.NFT_HOLDER_BONUS)

    def boosted_reward(self, address: str, staked: int,
                        base_reward: int) -> int:
        boost = self.compute_boost(address, staked)
        return int(base_reward * boost)

    def boost_breakdown(self, address: str, staked: int) -> dict:
        boost    = self.compute_boost(address, staked)
        venbl    = self._venbl.balance(address)
        nfts     = len(self._nft.tokens_of(address))
        return {
            "total_multiplier": f"{boost:.2f}x",
            "venbl_balance":    f"{venbl/10**DECIMALS:.3f}",
            "nft_count":        nfts,
            "nft_bonus":        f"{min(5,nfts)*self.NFT_HOLDER_BONUS*100:.0f}%",
        }


# ---- TransactionMixer
class TransactionMixer:
    """
    Privacy mixer for NEBULA.
    Mixes transactions to break the transaction graph.
    Note: For educational/research purposes.
    """

    POOL_DENOMINATIONS = [
        1 * 10**DECIMALS,
        10 * 10**DECIMALS,
        100 * 10**DECIMALS,
    ]

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._pools: Dict[int, List[dict]] = {d: [] for d in self.POOL_DENOMINATIONS}
        self._lock   = threading.RLock()

    def enter_pool(self, denomination: int,
                    sender: str,
                    commitment: str) -> Tuple[bool, str]:
        with self._lock:
            if denomination not in self._pools:
                return False, "Invalid denomination"
            if self._bc.utxo.balance(sender) < denomination:
                return False, "Insufficient balance"
            ticket = hashlib.sha256(
                f"MIX:{sender}:{commitment}:{time.time()}".encode()
            ).hexdigest()
            self._pools[denomination].append({
                "ticket":     ticket,
                "commitment": commitment,
                "entered_at": self._bc.height,
            })
            return True, ticket

    def exit_pool(self, denomination: int,
                   ticket: str, recipient: str,
                   nullifier: str) -> Tuple[bool, str]:
        with self._lock:
            pool = self._pools.get(denomination, [])
            entry = next((e for e in pool if e["ticket"] == ticket), None)
            if not entry:
                return False, "Ticket not found"
            pool.remove(entry)
            return True, f"Mixed {denomination/10**DECIMALS:.0f} NBL sent to {recipient}"

    def pool_sizes(self) -> dict:
        return {
            f"{d/10**DECIMALS:.0f} NBL": len(p)
            for d, p in self._pools.items()
        }


# ---- EconomicSecurityAnalyzer
class EconomicSecurityAnalyzer:
    """
    Analyzes NEBULA's economic security.
    Models cost of 51% attack, security budget.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc     = blockchain
        self._oracle = oracle

    def attack_cost_estimate(self) -> dict:
        """Estimate cost of a 51% attack."""
        h         = self._bc.height
        bits      = self._bc.tip.header.bits
        difficulty = MAX_TARGET / max(1, bits_to_target(bits))
        price     = (self._oracle.price("NBL/USD")
                     if self._oracle else 0.001) or 0.001
        reward    = mining_reward(h) * price / 10**DECIMALS
        daily_rewards = reward * 144   # blocks per day
        attack_cost   = daily_rewards * 0.51   # need >51% of revenue
        return {
            "difficulty":      f"{difficulty:.2f}",
            "daily_rewards":   f"${daily_rewards:.2f}",
            "attack_cost_usd": f"${attack_cost:.2f}/day",
            "security_note":   "Actual cost much higher with hardware",
        }

    def security_budget(self) -> dict:
        h       = self._bc.height
        reward  = mining_reward(h)
        price   = (self._oracle.price("NBL/USD")
                   if self._oracle else 0.001) or 0.001
        usd_val = reward * price / 10**DECIMALS * 144
        return {
            "block_reward_nbl": f"{reward/10**DECIMALS:.9f}",
            "daily_usd":        f"${usd_val:.2f}",
            "annual_usd":       f"${usd_val*365:.2f}",
        }


# ---- ArchiveNode
class ArchiveNode:
    """
    Archive node — stores complete chain history.
    Never prunes. Serves historical queries.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._state_snapshots: Dict[int, dict] = {}
        self._tx_receipts: Dict[str, dict]     = {}
        self._lock         = threading.RLock()

    def snapshot_state(self, block_height: int) -> str:
        """Take a state snapshot at a given height."""
        with self._lock:
            utxo_data    = {
                k: self._bc.utxo.balance(k)
                for k in list(self._bc.utxo._addr_idx.keys())[:1000]
            }
            snap         = {
                "height":       block_height,
                "utxo_count":   self._bc.utxo.size(),
                "total_supply": self._bc.utxo.total_supply(),
                "top_balances": dict(sorted(
                    utxo_data.items(), key=lambda x: -x[1])[:20]),
            }
            self._state_snapshots[block_height] = snap
            return hashlib.sha256(
                json.dumps(snap, sort_keys=True).encode()
            ).hexdigest()

    def add_receipt(self, txid: str, receipt: dict):
        with self._lock:
            self._tx_receipts[txid] = {
                **receipt,
                "txid":      txid,
                "archived":  time.time(),
            }

    def get_state_at(self, height: int) -> Optional[dict]:
        closest = min(
            (h for h in self._state_snapshots if h <= height),
            default=None
        )
        return self._state_snapshots.get(closest) if closest else None

    def archive_stats(self) -> dict:
        return {
            "snapshots":   len(self._state_snapshots),
            "tx_receipts": len(self._tx_receipts),
            "is_archive":  True,
        }


# ---- GovernanceAnalytics
class GovernanceAnalytics:
    """Analytics and insights for NEBULA governance."""

    def __init__(self, governance: 'GovernanceEngine',
                  blockchain: 'NEBULABlockchain'):
        self._gov = governance
        self._bc  = blockchain

    def voter_participation(self) -> dict:
        total_voters  = set()
        proposals     = self._gov.list_proposals()
        for p in proposals:
            voters = p.get("voters", {})
            total_voters.update(voters.keys() if isinstance(voters, dict) else [])
        return {
            "unique_voters": len(total_voters),
            "total_proposals": len(proposals),
            "avg_participation": f"{len(total_voters)/max(1,len(proposals)):.1f} voters/proposal",
        }

    def pass_rate(self) -> dict:
        proposals = self._gov.list_proposals()
        passed    = sum(1 for p in proposals if p.get("status") == "passed")
        failed    = sum(1 for p in proposals if p.get("status") == "failed")
        total     = len(proposals)
        return {
            "total":   total,
            "passed":  passed,
            "failed":  failed,
            "pass_pct": f"{passed/max(1,total)*100:.1f}%",
        }

    def proposal_type_breakdown(self) -> dict:
        proposals = self._gov.list_proposals()
        by_type   = {}
        for p in proposals:
            pt = p.get("type", "unknown")
            by_type[pt] = by_type.get(pt, 0) + 1
        return by_type

    def governance_summary(self) -> dict:
        return {
            "participation": self.voter_participation(),
            "pass_rate":     self.pass_rate(),
            "by_type":       self.proposal_type_breakdown(),
        }


# ---- NodeHealthCheck
class NodeHealthCheck:
    """Comprehensive health check for NEBULA nodes."""

    CHECKS = {
        "chain_sync":   lambda self: self._check_chain(),
        "mempool":      lambda self: self._check_mempool(),
        "disk_usage":   lambda self: self._check_disk(),
        "peer_count":   lambda self: self._check_peers(),
        "api_response": lambda self: self._check_api(),
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  api: 'NodeRESTAPI' = None):
        self._bc  = blockchain
        self._api = api

    def _check_chain(self) -> dict:
        h   = self._bc.height
        tip = self._bc.tip
        ok  = h >= 0 and tip is not None
        return {"ok": ok, "height": h, "tip": tip.hash[:12] if tip else "none"}

    def _check_mempool(self) -> dict:
        size = self._bc.mempool.size()
        ok   = size < 50_000
        return {"ok": ok, "size": size, "status": "normal" if ok else "congested"}

    def _check_disk(self) -> dict:
        return {"ok": True, "note": "disk check simulated"}

    def _check_peers(self) -> dict:
        return {"ok": True, "peers": 0, "note": "peer check simulated"}

    def _check_api(self) -> dict:
        if not self._api:
            return {"ok": False, "note": "API not configured"}
        result = self._api.handle("GET", "/health")
        return {"ok": result.get("ok", False)}

    def run_all(self) -> dict:
        results = {}
        for name, fn in self.CHECKS.items():
            try:
                results[name] = fn(self)
            except Exception as e:
                results[name] = {"ok": False, "error": str(e)}
        all_ok = all(r.get("ok", False) for r in results.values())
        return {
            "healthy":  all_ok,
            "status":   "UP" if all_ok else "DEGRADED",
            "checks":   results,
        }


# ---- FeeHistoryAnalyzer
class FeeHistoryAnalyzer:
    """
    Analyzes NEBULA fee market history.
    Provides fee recommendations and congestion analysis.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc          = blockchain
        self._fee_samples: List[dict] = []
        self._lock         = threading.RLock()

    def record_block_fees(self, block: 'Block',
                           utxo: 'UTXOSet'):
        with self._lock:
            fees     = [tx.fee(utxo) for tx in block.transactions[1:]]
            sizes    = [tx.byte_size() for tx in block.transactions[1:]]
            fee_rates = [f//max(1,s) for f,s in zip(fees, sizes)]
            if fee_rates:
                self._fee_samples.append({
                    "height":  block.height,
                    "min":     min(fee_rates),
                    "max":     max(fee_rates),
                    "avg":     sum(fee_rates) // len(fee_rates),
                    "median":  sorted(fee_rates)[len(fee_rates)//2],
                    "count":   len(fee_rates),
                })
                if len(self._fee_samples) > 2016:
                    self._fee_samples.pop(0)

    def fee_recommendations(self) -> dict:
        with self._lock:
            recent = self._fee_samples[-10:] if self._fee_samples else []
        if not recent:
            return {"fast": MIN_TX_FEE*3,
                    "normal": MIN_TX_FEE*2,
                    "slow": MIN_TX_FEE}
        medians = [s["median"] for s in recent]
        avg_med = sum(medians) // len(medians)
        return {
            "fast":   int(avg_med * 1.5),
            "normal": avg_med,
            "slow":   int(avg_med * 0.7),
            "unit":   "Neb/byte",
        }

    def congestion_level(self) -> str:
        mp_size = self._bc.mempool.size()
        if mp_size > 10_000:
            return "HIGH"
        elif mp_size > 1_000:
            return "MEDIUM"
        return "LOW"

    def fee_history_summary(self) -> dict:
        with self._lock:
            n = len(self._fee_samples)
        recs = self.fee_recommendations()
        return {
            "samples_recorded":  n,
            "congestion":        self.congestion_level(),
            "recommended_fast":  f"{recs['fast']} Neb/byte",
            "recommended_norm":  f"{recs['normal']} Neb/byte",
            "recommended_slow":  f"{recs['slow']} Neb/byte",
        }


# ---- ValidatorRewardTracker
class ValidatorRewardTracker:
    """Tracks and distributes rewards to PoS validators."""

    VALIDATOR_REWARD_PCT = 0.60   # 60% of block rewards to validators
    DELEGATOR_SHARE      = 0.80   # 80% to delegators, 20% to validator

    def __init__(self, blockchain: 'NEBULABlockchain',
                  validator_set: 'ValidatorSetManager'):
        self._bc   = blockchain
        self._vs   = validator_set
        self._rewards:     Dict[str, int] = {}
        self._delegations: Dict[str, Dict[str, int]] = {}  # validator -> {delegator: amount}
        self._lock  = threading.RLock()

    def record_block(self, block: 'Block', proposer: str):
        with self._lock:
            reward      = mining_reward(block.height)
            val_reward  = int(reward * self.VALIDATOR_REWARD_PCT)
            deleg_share = int(val_reward * self.DELEGATOR_SHARE)
            val_share   = val_reward - deleg_share
            self._rewards[proposer] = (
                self._rewards.get(proposer, 0) + val_share)
            delegates = self._delegations.get(proposer, {})
            total_del = sum(delegates.values()) or 1
            for delegator, amount in delegates.items():
                share = int(deleg_share * amount / total_del)
                self._rewards[delegator] = (
                    self._rewards.get(delegator, 0) + share)

    def delegate(self, delegator: str, validator: str, amount: int):
        with self._lock:
            if validator not in self._delegations:
                self._delegations[validator] = {}
            self._delegations[validator][delegator] = (
                self._delegations[validator].get(delegator, 0) + amount)

    def claim(self, address: str) -> Tuple[bool, int]:
        with self._lock:
            reward = self._rewards.get(address, 0)
            if reward == 0:
                return False, 0
            self._rewards[address] = 0
            return True, reward

    def pending(self, address: str) -> int:
        return self._rewards.get(address, 0)

    def reward_stats(self) -> dict:
        with self._lock:
            total = sum(self._rewards.values())
        return {
            "pending_total_nbl": f"{total/10**DECIMALS:.6f}",
            "validators_tracked": len(self._rewards),
        }


# ---- CrossDEXArbitrage
class CrossDEXArbitrage:
    """
    Cross-DEX arbitrage detector and executor for NEBULA.
    Identifies profitable arbitrage opportunities.
    """

    MIN_PROFIT_NBL = 1.0 * 10**DECIMALS

    def __init__(self, dex1: 'NEBULADex',
                  dex2: 'NEBULADex' = None,
                  order_book: 'OrderBookManager' = None):
        self._dex1 = dex1
        self._dex2 = dex2
        self._ob   = order_book
        self._opps: List[dict] = []

    def find_opportunities(self, token_a: str,
                            token_b: str,
                            test_amount: int = 1000 * 10**DECIMALS) -> List[dict]:
        opportunities = []
        # AMM vs AMM
        if self._dex2:
            out1 = self._dex1.quote_amm(token_a, token_b, test_amount)
            out2 = self._dex2.quote_amm(token_b, token_a, out1) if out1 > 0 else 0
            profit = out2 - test_amount
            if profit >= self.MIN_PROFIT_NBL:
                opportunities.append({
                    "type":    "AMM-AMM",
                    "route":   f"{token_a} → {token_b} (DEX1) → {token_a} (DEX2)",
                    "profit":  f"{profit/10**DECIMALS:.6f} {token_a}",
                    "pct":     f"{profit/test_amount*100:.3f}%",
                })
        # AMM vs Order Book
        if self._ob:
            amm_out = self._dex1.quote_amm(token_a, token_b, test_amount)
            book    = self._ob.get_book(f"{token_a}/{token_b}")
            if book and book.best_ask():
                ob_price = book.best_ask()
                if ob_price and amm_out > 0:
                    amm_price = test_amount / amm_out if amm_out > 0 else 0
                    spread    = (ob_price - amm_price) / amm_price * 100
                    if abs(spread) > 0.5:
                        opportunities.append({
                            "type":   "AMM-OrderBook",
                            "spread": f"{spread:+.3f}%",
                            "route":  f"{token_a}/{token_b}",
                        })
        self._opps.extend(opportunities)
        return opportunities

    def arb_stats(self) -> dict:
        return {
            "opportunities_found": len(self._opps),
            "min_profit":         f"{self.MIN_PROFIT_NBL/10**DECIMALS:.1f} NBL",
        }
