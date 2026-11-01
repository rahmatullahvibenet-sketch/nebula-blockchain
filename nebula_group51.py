"""NEBULA group51 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. ComplianceRuleV2  (orig. lines 79827-79842)
   2. ComplianceV2  (orig. lines 79844-79913)
   3. DataFeedRegistry  (orig. lines 79981-80037)
   4. PerpetualProtocol  (orig. lines 80044-80122)
   5. OptionsProtocolV2  (orig. lines 80129-80209)
   6. TreasuryYieldStrategy  (orig. lines 80216-80274)
   7. GovernanceV3  (orig. lines 80281-80396)
   8. SyntheticAsset  (orig. lines 80403-80414)
   9. SyntheticAssetProtocol  (orig. lines 80416-80485)
  10. CrossChainGovernance  (orig. lines 80492-80549)
  11. SecurityCouncil  (orig. lines 80556-80635)
  12. EcosystemTracker  (orig. lines 80642-80679)
  13. InteroperabilityLayer  (orig. lines 80686-80741)
  14. ThresholdSignatureScheme  (orig. lines 80753-80797)
  15. KeyDerivationFunction  (orig. lines 80800-80820)
  16. NFTLoanOffer  (orig. lines 80831-80844)
  17. NFTLending  (orig. lines 80846-80925)
  18. DAOv2  (orig. lines 80932-81015)
  19. MultisigTreasury  (orig. lines 81022-81084)
  20. RecursiveZKProof  (orig. lines 81091-81159)

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

def hmac_sha256(key: bytes, data: bytes) -> bytes:
    import hmac as _hmac
    return _hmac.new(key, data, 'sha256').digest()

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- ComplianceRuleV2
class ComplianceRuleV2:
    """A compliance rule for NEBULA."""

    def __init__(self, rule_id: str, name: str,
                  check_fn: Callable, severity: str = "warning"):
        self.rule_id  = rule_id
        self.name     = name
        self.check_fn = check_fn
        self.severity = severity

    def evaluate(self, address: str, context: dict) -> Tuple[bool, str]:
        try:
            result = self.check_fn(address, context)
            return result
        except Exception as e:
            return True, f"Error evaluating rule: {e}"


# ---- ComplianceV2
class ComplianceV2:
    """
    Enhanced compliance engine v2 for NEBULA.
    Pluggable rule system for regulatory compliance.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._rules: Dict[str, ComplianceRuleV2] = {}
        self._reports: List[dict] = []
        self._lock   = threading.RLock()
        self._init_default_rules()

    def _init_default_rules(self):
        # Large transaction reporting
        def large_tx_check(addr: str, ctx: dict) -> Tuple[bool, str]:
            bal = ctx.get("amount", 0)
            if bal > 10_000 * 10**DECIMALS:
                return False, "Transaction >10,000 NBL requires review"
            return True, "OK"
        self.add_rule("large_tx", "Large Transaction",
                      large_tx_check, "info")

        # Velocity check
        def velocity_check(addr: str, ctx: dict) -> Tuple[bool, str]:
            tx_count = ctx.get("tx_count_24h", 0)
            if tx_count > 1000:
                return False, "High velocity detected"
            return True, "OK"
        self.add_rule("velocity", "Transaction Velocity",
                      velocity_check, "warning")

    def add_rule(self, rule_id: str, name: str,
                  check_fn: Callable, severity: str = "warning"):
        with self._lock:
            self._rules[rule_id] = ComplianceRuleV2(
                rule_id, name, check_fn, severity)

    def check_address(self, address: str,
                       context: dict = None) -> dict:
        context = context or {}
        results = []
        for rule in self._rules.values():
            ok, msg = rule.evaluate(address, context)
            results.append({
                "rule":    rule.rule_id,
                "name":    rule.name,
                "passed":  ok,
                "message": msg,
                "severity": rule.severity,
            })
        passed_all = all(r["passed"] for r in results)
        report = {
            "address":    address,
            "compliant":  passed_all,
            "rules":      results,
            "checked_at": time.time(),
        }
        with self._lock:
            self._reports.append(report)
        return report

    def compliance_v2_stats(self) -> dict:
        with self._lock:
            compliant = sum(1 for r in self._reports if r["compliant"])
        return {
            "rules":    len(self._rules),
            "reports":  len(self._reports),
            "pass_rate": f"{compliant/max(1,len(self._reports))*100:.1f}%",
        }


# ---- DataFeedRegistry
class DataFeedRegistry:
    """Registry of on-chain data feeds for NEBULA smart contracts."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._feeds: Dict[str, dict] = {}
        self._lock  = threading.RLock()

    def register_feed(self, feed_id: str, description: str,
                       data_type: str, provider: str) -> bool:
        with self._lock:
            if feed_id in self._feeds:
                return False
            self._feeds[feed_id] = {
                "feed_id":     feed_id,
                "description": description,
                "data_type":   data_type,
                "provider":    provider,
                "rounds":      [],
                "latest":      None,
            }
            return True

    def update_feed(self, feed_id: str, value: Any,
                     provider: str = "") -> bool:
        with self._lock:
            feed = self._feeds.get(feed_id)
            if not feed:
                return False
            round_data = {
                "round":     len(feed["rounds"]) + 1,
                "value":     value,
                "block":     self._bc.height,
                "provider":  provider,
                "ts":        time.time(),
            }
            feed["rounds"].append(round_data)
            feed["latest"] = round_data
            if len(feed["rounds"]) > 1000:
                feed["rounds"].pop(0)
            return True

    def get_latest(self, feed_id: str) -> Optional[dict]:
        feed = self._feeds.get(feed_id)
        return feed["latest"] if feed else None

    def feed_history(self, feed_id: str, n: int = 10) -> List[dict]:
        feed = self._feeds.get(feed_id)
        if not feed:
            return []
        return feed["rounds"][-n:]

    def feed_registry_stats(self) -> dict:
        return {
            "feeds":       len(self._feeds),
            "total_rounds": sum(len(f["rounds"]) for f in self._feeds.values()),
        }


# ---- PerpetualProtocol
class PerpetualProtocol:
    """
    Full perpetual trading protocol for NEBULA.
    Virtual AMM (vAMM) based perpetuals with funding.
    """

    VIRTUAL_BASE    = 1_000_000   # virtual liquidity base
    FUNDING_PERIOD  = 28_800      # 8 hours in seconds

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc       = blockchain
        self._oracle   = oracle
        self._markets: Dict[str, dict] = {}
        self._positions: Dict[str, List[dict]] = {}
        self._lock     = threading.RLock()

    def create_market(self, base: str, quote: str = "USD",
                       init_price: float = 1.0) -> str:
        with self._lock:
            market_id = f"{base}/{quote}"
            k         = self.VIRTUAL_BASE * init_price * self.VIRTUAL_BASE
            self._markets[market_id] = {
                "base":       base,
                "quote":      quote,
                "vBase":      float(self.VIRTUAL_BASE),
                "vQuote":     float(self.VIRTUAL_BASE) * init_price,
                "k":          k,
                "funding":    0.0,
                "open_int":   0.0,
                "last_fund":  time.time(),
            }
            return market_id

    def open_position(self, trader: str, market_id: str,
                       long: bool, notional: float,
                       leverage: float) -> Tuple[bool, str]:
        with self._lock:
            mkt = self._markets.get(market_id)
            if not mkt:
                return False, "Market not found"
            margin = notional / leverage
            if self._bc.utxo.balance(trader) < int(margin * 10**DECIMALS):
                return False, "Insufficient margin"
            # vAMM swap
            if long:
                new_vQuote = mkt["vQuote"] + notional
                new_vBase  = mkt["k"] / new_vQuote
                size       = mkt["vBase"] - new_vBase
            else:
                new_vBase  = mkt["vBase"] + notional / (mkt["vQuote"]/mkt["vBase"])
                new_vQuote = mkt["k"] / new_vBase
                size       = -(new_vBase - mkt["vBase"])
            mkt["vBase"]  = new_vBase
            mkt["vQuote"] = new_vQuote
            mkt["open_int"] += abs(size)
            if trader not in self._positions:
                self._positions[trader] = []
            self._positions[trader].append({
                "market":   market_id,
                "long":     long,
                "size":     size,
                "margin":   margin,
                "notional": notional,
                "entry_price": mkt["vQuote"] / mkt["vBase"],
            })
            return True, f"{'Long' if long else 'Short'} {abs(size):.4f} {mkt['base']}"

    def mark_price(self, market_id: str) -> float:
        mkt = self._markets.get(market_id)
        if not mkt:
            return 0.0
        return mkt["vQuote"] / mkt["vBase"]

    def perp_protocol_stats(self) -> dict:
        return {
            "markets":   len(self._markets),
            "positions": sum(len(p) for p in self._positions.values()),
        }


# ---- OptionsProtocolV2
class OptionsProtocolV2:
    """
    Full options protocol v2 with Greeks calculation.
    Black-Scholes model for option pricing.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._options: Dict[str, dict] = {}
        self._lock    = threading.RLock()

    def _black_scholes_approx(self, S: float, K: float,
                                T: float, r: float = 0.05,
                                sigma: float = 0.8,
                                call: bool = True) -> float:
        """Simplified Black-Scholes approximation."""
        import math
        if T <= 0 or S <= 0 or K <= 0:
            return max(0, S - K) if call else max(0, K - S)
        d1  = (math.log(S/K) + (r + sigma**2/2)*T) / (sigma * math.sqrt(T))
        d2  = d1 - sigma * math.sqrt(T)
        # Normal CDF approximation
        def N(x):
            return 0.5 * (1 + math.erf(x / math.sqrt(2)))
        if call:
            return S * N(d1) - K * math.exp(-r*T) * N(d2)
        else:
            return K * math.exp(-r*T) * N(-d2) - S * N(-d1)

    def price_option(self, underlying: str, strike: float,
                      expiry_days: float,
                      call: bool = True) -> dict:
        S     = (self._oracle.price(f"{underlying}/USD")
                 if self._oracle else 0.01) or 0.01
        T     = expiry_days / 365
        price = self._black_scholes_approx(S, strike, T, call=call)
        return {
            "underlying":  underlying,
            "spot":        f"${S:.4f}",
            "strike":      f"${strike:.4f}",
            "expiry_days": expiry_days,
            "type":        "call" if call else "put",
            "bs_price":    f"${price:.6f}",
            "itm":         S > strike if call else S < strike,
        }

    def write_option_v2(self, writer: str, underlying: str,
                         strike: float, expiry_days: int,
                         call: bool, amount: float) -> str:
        with self._lock:
            pricing = self.price_option(underlying, strike,
                                         expiry_days, call)
            oid     = hashlib.sha256(
                f"OPT2:{writer}:{underlying}:{strike}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._options[oid] = {
                "id":          oid,
                "writer":      writer,
                "underlying":  underlying,
                "strike":      strike,
                "expiry_days": expiry_days,
                "call":        call,
                "amount":      amount,
                "premium":     float(pricing["bs_price"].lstrip('$')),
                "buyer":       None,
                "exercised":   False,
            }
            return oid

    def options_v2_stats(self) -> dict:
        with self._lock:
            calls  = sum(1 for o in self._options.values() if o["call"])
            puts   = len(self._options) - calls
        return {
            "total":     len(self._options),
            "calls":     calls,
            "puts":      puts,
            "model":     "Black-Scholes",
        }


# ---- TreasuryYieldStrategy
class TreasuryYieldStrategy:
    """
    Manages yield generation from NEBULA treasury funds.
    Invests treasury into DeFi protocols for additional yield.
    """

    YIELD_ALLOCATION = {
        "staking_365d": 0.40,
        "dex_lp":       0.30,
        "lending":      0.20,
        "reserves":     0.10,
    }

    def __init__(self, treasury: 'NEBULATreasury',
                  blockchain: 'NEBULABlockchain'):
        self._treasury = treasury
        self._bc       = blockchain
        self._deployed: Dict[str, float] = {}
        self._yields:   Dict[str, float] = {}

    def deploy_capital(self, amount_nbl: float) -> dict:
        """Deploy treasury capital to yield strategies."""
        deployed = {}
        for strategy, pct in self.YIELD_ALLOCATION.items():
            allocation = amount_nbl * pct
            self._deployed[strategy] = (
                self._deployed.get(strategy, 0) + allocation)
            deployed[strategy] = allocation
        return deployed

    def estimate_yield(self, period_days: int = 365) -> dict:
        """Estimate yield from deployed capital."""
        apys = {
            "staking_365d": 0.25,
            "dex_lp":       0.35,
            "lending":      0.04,
            "reserves":     0.00,
        }
        total_yield = 0.0
        breakdown   = {}
        for strategy, amount in self._deployed.items():
            apy    = apys.get(strategy, 0)
            yield_ = amount * apy * period_days / 365
            breakdown[strategy] = f"{yield_:.3f} NBL"
            total_yield += yield_
        return {
            "period_days":  period_days,
            "total_yield":  f"{total_yield:.3f} NBL",
            "blended_apy":  f"{total_yield/max(0.001,sum(self._deployed.values()))*100:.2f}%",
            "breakdown":    breakdown,
        }

    def treasury_yield_stats(self) -> dict:
        total = sum(self._deployed.values())
        return {
            "total_deployed": f"{total:.3f} NBL",
            "strategies":     self.YIELD_ALLOCATION,
            "annual_estimate": self.estimate_yield(365),
        }


# ---- GovernanceV3
class GovernanceV3:
    """
    Governance v3 — multi-sig weighted, time-locked execution.
    Fully on-chain with timelock and guardian veto.
    """

    TIMELOCK_BLOCKS   = 144 * 2    # 2-day timelock
    GUARDIAN_VETO_BLOCKS = 144     # 1-day guardian window

    def __init__(self, blockchain: 'NEBULABlockchain',
                  venbl: 'VoteEscrowedNBL' = None):
        self._bc       = blockchain
        self._venbl    = venbl
        self._proposals: List[dict] = []
        self._guardians: Set[str]   = set()
        self._vetoed:    Set[str]   = set()
        self._lock      = threading.RLock()

    def add_guardian(self, guardian: str):
        self._guardians.add(guardian)

    def propose(self, proposer: str, title: str,
                 actions: List[dict],
                 description: str = "") -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"GOVV3:{proposer}:{title}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._proposals.append({
                "id":          pid,
                "proposer":    proposer,
                "title":       title,
                "actions":     actions,
                "description": description,
                "votes_yes":   0.0,
                "votes_no":    0.0,
                "voters":      {},
                "status":      "voting",
                "timelock":    None,
                "created":     self._bc.height,
            })
            return pid

    def vote(self, voter: str, proposal_id: str,
              support: bool) -> Tuple[bool, str]:
        with self._lock:
            p = next((p for p in self._proposals
                      if p["id"] == proposal_id), None)
            if not p or p["status"] != "voting":
                return False, "Not voteable"
            if voter in p["voters"]:
                return False, "Already voted"
            weight = (self._venbl.balance(voter) / 10**DECIMALS
                      if self._venbl else
                      self._bc.utxo.balance(voter) / 10**DECIMALS)
            if support:
                p["votes_yes"] += weight
            else:
                p["votes_no"]  += weight
            p["voters"][voter] = support
            return True, f"Voted ({'yes' if support else 'no'}), weight={weight:.2f}"

    def queue(self, proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            p = next((p for p in self._proposals
                      if p["id"] == proposal_id), None)
            if not p:
                return False, "Not found"
            total = p["votes_yes"] + p["votes_no"]
            pct   = p["votes_yes"] / total if total > 0 else 0
            if pct < 0.60:
                p["status"] = "failed"
                return False, f"Failed: {pct*100:.1f}% yes"
            p["status"]   = "queued"
            p["timelock"]  = self._bc.height + self.TIMELOCK_BLOCKS
            return True, f"Queued. Executes at block {p['timelock']}"

    def guardian_veto(self, guardian: str,
                       proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            if guardian not in self._guardians:
                return False, "Not a guardian"
            p = next((p for p in self._proposals
                      if p["id"] == proposal_id), None)
            if not p or p["status"] != "queued":
                return False, "Not queued"
            self._vetoed.add(proposal_id)
            p["status"] = "vetoed"
            return True, "Proposal vetoed by guardian"

    def execute(self, proposal_id: str) -> Tuple[bool, str]:
        with self._lock:
            p = next((p for p in self._proposals
                      if p["id"] == proposal_id), None)
            if not p or p["status"] != "queued":
                return False, "Not queued"
            if proposal_id in self._vetoed:
                return False, "Vetoed"
            if self._bc.height < p["timelock"]:
                left = p["timelock"] - self._bc.height
                return False, f"Timelock: {left} blocks remaining"
            p["status"] = "executed"
            return True, f"Executed {len(p['actions'])} actions"

    def gov_v3_stats(self) -> dict:
        with self._lock:
            by_status = {}
            for p in self._proposals:
                s = p["status"]
                by_status[s] = by_status.get(s, 0) + 1
        return {
            "proposals":  len(self._proposals),
            "guardians":  len(self._guardians),
            "by_status":  by_status,
            "timelock":   f"{self.TIMELOCK_BLOCKS} blocks",
        }


# ---- SyntheticAsset
class SyntheticAsset:
    """A synthetic asset tracking a real-world asset price."""

    def __init__(self, synth_id: str, name: str,
                  tracked_asset: str,
                  oracle_key: str):
        self.synth_id      = synth_id
        self.name          = name
        self.tracked       = tracked_asset
        self.oracle_key    = oracle_key
        self.total_supply  = 0
        self.collateral:   Dict[str, int] = {}


# ---- SyntheticAssetProtocol
class SyntheticAssetProtocol:
    """
    Synthetic asset protocol for NEBULA.
    Mint synthetic stocks, commodities, and indices.
    """

    MIN_RATIO  = 1.50   # 150% collateral ratio
    ASSETS     = {
        "sTSLA":  ("Tesla",        "TSLA/USD"),
        "sAAPL":  ("Apple",        "AAPL/USD"),
        "sGOLD":  ("Gold",         "XAU/USD"),
        "sOIL":   ("Crude Oil",    "WTI/USD"),
        "sSP500": ("S&P 500 Index","SPX/USD"),
        "sBTC":   ("Synthetic BTC","BTC/USD"),
        "sETH":   ("Synthetic ETH","ETH/USD"),
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc       = blockchain
        self._oracle   = oracle
        self._synthetics: Dict[str, SyntheticAsset] = {}
        self._positions:  Dict[str, List[dict]]     = {}
        self._lock     = threading.RLock()
        self._init_assets()

    def _init_assets(self):
        for sid, (name, oracle_key) in self.ASSETS.items():
            self._synthetics[sid] = SyntheticAsset(
                sid, name, sid[1:], oracle_key)

    def mint(self, minter: str, synth_id: str,
              amount: float, collateral_nbl: float) -> Tuple[bool, str]:
        with self._lock:
            synth = self._synthetics.get(synth_id)
            if not synth:
                return False, f"Unknown synthetic: {synth_id}"
            # Check collateral ratio
            col_raw  = int(collateral_nbl * 10**DECIMALS)
            if self._bc.utxo.balance(minter) < col_raw:
                return False, "Insufficient collateral"
            synth_price = (self._oracle.price(synth.oracle_key)
                           if self._oracle else 1.0) or 1.0
            nbl_price   = (self._oracle.price("NBL/USD")
                           if self._oracle else 0.01) or 0.01
            col_usd     = collateral_nbl * nbl_price
            synth_usd   = amount * synth_price
            if col_usd < synth_usd * self.MIN_RATIO:
                return False, f"Need {synth_usd*self.MIN_RATIO:.2f} USD collateral"
            synth.total_supply += int(amount * 10**9)
            synth.collateral[minter] = (
                synth.collateral.get(minter, 0) + col_raw)
            return True, f"Minted {amount:.4f} {synth_id}"

    def synth_price(self, synth_id: str) -> float:
        synth = self._synthetics.get(synth_id)
        if not synth or not self._oracle:
            return 0.0
        return self._oracle.price(synth.oracle_key) or 0.0

    def protocol_stats(self) -> dict:
        total_supply = sum(
            s.total_supply / 10**9
            for s in self._synthetics.values()
        )
        return {
            "synthetic_assets": len(self._synthetics),
            "total_synth_supply": f"{total_supply:.4f}",
            "min_collateral_ratio": f"{self.MIN_RATIO*100:.0f}%",
        }


# ---- CrossChainGovernance
class CrossChainGovernance:
    """
    Cross-chain governance allowing multiple chains to vote
    on NEBULA protocol decisions.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc         = blockchain
        self._proposals: List[dict] = []
        self._chains:    Set[str]   = {"nebula"}
        self._votes:     Dict[str, Dict[str, float]] = {}
        self._lock       = threading.RLock()

    def add_chain(self, chain: str, weight: float = 1.0):
        with self._lock:
            self._chains.add(chain)

    def propose_xcgov(self, proposer: str, title: str,
                       description: str) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"XCGOV:{proposer}:{title}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._proposals.append({
                "id":          pid,
                "proposer":    proposer,
                "title":       title,
                "description": description,
                "status":      "active",
            })
            self._votes[pid] = {}
            return pid

    def submit_chain_vote(self, chain: str, proposal_id: str,
                           yes_tokens: float) -> bool:
        with self._lock:
            if chain not in self._chains:
                return False
            if proposal_id not in self._votes:
                return False
            self._votes[proposal_id][chain] = yes_tokens
            return True

    def tally_votes(self, proposal_id: str) -> dict:
        votes = self._votes.get(proposal_id, {})
        total = sum(votes.values())
        return {
            "proposal_id": proposal_id,
            "votes_by_chain": votes,
            "total_yes":  total,
            "chains":     len(votes),
        }

    def xcgov_stats(self) -> dict:
        return {
            "chains":     len(self._chains),
            "proposals":  len(self._proposals),
        }


# ---- SecurityCouncil
class SecurityCouncil:
    """
    NEBULA Security Council — emergency multisig.
    Can pause protocols and freeze addresses in emergencies.
    """

    REQUIRED_SIGNATURES = 4
    COUNCIL_SIZE        = 7

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._members: List[str]         = []
        self._paused:  Set[str]          = set()
        self._frozen:  Set[str]          = set()
        self._actions: List[dict]        = []
        self._sigs:    Dict[str, Set[str]] = {}
        self._lock     = threading.RLock()

    def add_member(self, address: str) -> bool:
        with self._lock:
            if len(self._members) >= self.COUNCIL_SIZE:
                return False
            if address not in self._members:
                self._members.append(address)
            return True

    def _propose_action(self, action_type: str,
                         target: str, data: dict = None) -> str:
        aid = hashlib.sha256(
            f"SEC:{action_type}:{target}:{time.time()}".encode()
        ).hexdigest()[:12]
        self._actions.append({
            "id":     aid,
            "type":   action_type,
            "target": target,
            "data":   data or {},
            "status": "pending",
        })
        self._sigs[aid] = set()
        return aid

    def propose_pause(self, member: str, protocol: str) -> str:
        return self._propose_action("pause", protocol)

    def propose_freeze(self, member: str, address: str) -> str:
        return self._propose_action("freeze_address", address)

    def sign(self, member: str, action_id: str) -> Tuple[bool, str]:
        with self._lock:
            if member not in self._members:
                return False, "Not a council member"
            action = next((a for a in self._actions
                           if a["id"] == action_id), None)
            if not action or action["status"] != "pending":
                return False, "Action not found"
            self._sigs[action_id].add(member)
            n = len(self._sigs[action_id])
            if n >= self.REQUIRED_SIGNATURES:
                if action["type"] == "pause":
                    self._paused.add(action["target"])
                elif action["type"] == "freeze_address":
                    self._frozen.add(action["target"])
                action["status"] = "executed"
                return True, f"Action executed ({n}/{self.REQUIRED_SIGNATURES})"
            return True, f"Signed ({n}/{self.REQUIRED_SIGNATURES})"

    def is_paused(self, protocol: str) -> bool:
        return protocol in self._paused

    def is_frozen(self, address: str) -> bool:
        return address in self._frozen

    def council_stats(self) -> dict:
        return {
            "members":   len(self._members),
            "required":  self.REQUIRED_SIGNATURES,
            "paused":    len(self._paused),
            "frozen":    len(self._frozen),
            "actions":   len(self._actions),
        }


# ---- EcosystemTracker
class EcosystemTracker:
    """
    Tracks the growth of the NEBULA ecosystem over time.
    DAU, new addresses, protocol usage, TVL trends.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._daily: Dict[str, dict] = {}

    def track_day(self) -> dict:
        key = time.strftime('%Y-%m-%d')
        bc  = self._bc
        day = {
            "date":      key,
            "height":    bc.height,
            "mempool":   bc.mempool.size(),
            "supply":    bc.utxo.total_supply() / 10**DECIMALS,
            "addresses": bc.utxo.size(),
        }
        self._daily[key] = day
        return day

    def growth_rate(self, metric: str,
                     days: int = 30) -> Optional[float]:
        keys = sorted(self._daily.keys())[-days:]
        if len(keys) < 2:
            return None
        first = self._daily[keys[0]].get(metric, 0)
        last  = self._daily[keys[-1]].get(metric, 0)
        return (last - first) / first * 100 if first > 0 else None

    def trajectory(self) -> dict:
        return {
            "tracked_days": len(self._daily),
            "address_growth": self.growth_rate("addresses"),
            "supply_growth":  self.growth_rate("supply"),
        }


# ---- InteroperabilityLayer
class InteroperabilityLayer:
    """
    NEBULA interoperability layer.
    Connects NEBULA to IBC, Polkadot XCM, LayerZero.
    """

    PROTOCOLS = {
        "IBC":       {"type": "cosmos", "chains": ["cosmos", "osmosis", "juno"]},
        "XCM":       {"type": "polkadot", "chains": ["polkadot", "acala"]},
        "LayerZero": {"type": "evm", "chains": ["ethereum", "polygon", "bnb"]},
        "Wormhole":  {"type": "bridge", "chains": ["solana", "ethereum", "terra"]},
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._active:  Dict[str, bool] = {p: False for p in self.PROTOCOLS}
        self._messages: List[dict]     = []
        self._lock     = threading.RLock()

    def enable_protocol(self, protocol: str) -> bool:
        with self._lock:
            if protocol not in self.PROTOCOLS:
                return False
            self._active[protocol] = True
            return True

    def send_message(self, protocol: str, dest_chain: str,
                      payload: dict) -> Tuple[bool, str]:
        with self._lock:
            if not self._active.get(protocol):
                return False, f"{protocol} not enabled"
            proto_info = self.PROTOCOLS.get(protocol, {})
            if dest_chain not in proto_info.get("chains", []):
                return False, f"{dest_chain} not supported by {protocol}"
            mid = hashlib.sha256(
                f"IOP:{protocol}:{dest_chain}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._messages.append({
                "id":        mid,
                "protocol":  protocol,
                "dest":      dest_chain,
                "payload":   payload,
                "status":    "sent",
                "ts":        time.time(),
            })
            return True, mid

    def interop_stats(self) -> dict:
        enabled = sum(1 for v in self._active.values() if v)
        return {
            "protocols":       len(self.PROTOCOLS),
            "enabled":         enabled,
            "messages_sent":   len(self._messages),
            "supported_chains": sum(
                len(p["chains"]) for p in self.PROTOCOLS.values()),
        }


# ---- ThresholdSignatureScheme
class ThresholdSignatureScheme:
    """
    t-of-n threshold signature scheme.
    Requires t out of n signers to produce valid signature.
    """

    def __init__(self, t: int, n: int):
        assert 1 <= t <= n
        self.t = t
        self.n = n
        self._shares:  Dict[int, bytes] = {}
        self._partial: Dict[str, Dict[int, bytes]] = {}

    def generate_shares(self, secret: bytes) -> Dict[int, bytes]:
        """Shamir's Secret Sharing simplified."""
        shares = {}
        for i in range(1, self.n + 1):
            share = hashlib.sha256(
                secret + i.to_bytes(4, 'big')
            ).digest()
            shares[i] = share
            self._shares[i] = share
        return shares

    def add_partial_sig(self, msg_hash: str,
                         signer_idx: int,
                         partial: bytes):
        if msg_hash not in self._partial:
            self._partial[msg_hash] = {}
        self._partial[msg_hash][signer_idx] = partial

    def combine_signatures(self, msg_hash: str) -> Optional[bytes]:
        partials = self._partial.get(msg_hash, {})
        if len(partials) < self.t:
            return None
        # Combine first t partial signatures
        combined = b"".join(list(partials.values())[:self.t])
        return hashlib.sha256(combined).digest()

    def threshold_info(self) -> dict:
        return {
            "t": self.t,
            "n": self.n,
            "threshold": f"{self.t}-of-{self.n}",
        }


# ---- KeyDerivationFunction
class KeyDerivationFunction:
    """HKDF key derivation function."""

    @staticmethod
    def hkdf(salt: bytes, ikm: bytes, info: bytes,
              length: int = 32) -> bytes:
        prk = hmac_sha256(salt, ikm)
        okm = b""
        t   = b""
        for i in range(1, (length // 32) + 2):
            t   = hmac_sha256(prk, t + info + bytes([i]))
            okm += t
        return okm[:length]

    @staticmethod
    def pbkdf2(password: bytes, salt: bytes,
               iterations: int = 2048,
               length: int = 64) -> bytes:
        import hashlib as _hl
        return _hl.pbkdf2_hmac('sha512', password, salt,
                                iterations, length)


# ---- NFTLoanOffer
class NFTLoanOffer:
    """A loan offer backed by NFT collateral."""

    def __init__(self, offer_id: str, lender: str,
                  collection_id: str, amount: int,
                  interest_rate: float, duration_blocks: int):
        self.offer_id    = offer_id
        self.lender      = lender
        self.collection_id = collection_id
        self.amount      = amount
        self.interest    = interest_rate
        self.duration    = duration_blocks
        self.duration_blocks = duration_blocks   # G51 FIX: NFTLending.accept_offer reads this name
        self.active      = True
        self.loan        = None


# ---- NFTLending
class NFTLending:
    """
    Peer-to-peer NFT lending protocol.
    Borrow NBL using NFTs as collateral.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  nft: 'NBL721Registry'):
        self._bc     = blockchain
        self._nft    = nft
        self._offers: Dict[str, NFTLoanOffer] = {}
        self._loans:  Dict[str, dict]         = {}
        self._lock    = threading.RLock()

    def create_offer(self, lender: str, collection_id: str,
                      amount_nbl: float, interest: float,
                      duration_days: int) -> str:
        with self._lock:
            oid = hashlib.sha256(
                f"NFTLEND:{lender}:{collection_id}:{time.time()}".encode()
            ).hexdigest()[:12]
            offer = NFTLoanOffer(
                offer_id       = oid,
                lender         = lender,
                collection_id  = collection_id,
                amount         = int(amount_nbl * 10**DECIMALS),
                interest_rate  = interest,
                duration_blocks = duration_days * 144,
            )
            self._offers[oid] = offer
            return oid

    def accept_offer(self, borrower: str, offer_id: str,
                      token_id: int) -> Tuple[bool, str]:
        with self._lock:
            offer = self._offers.get(offer_id)
            if not offer or not offer.active:
                return False, "Offer not available"
            owner = self._nft.owner_of(offer.collection_id, token_id)
            if owner != borrower:
                return False, "Not NFT owner"
            loan_id = hashlib.sha256(
                f"LOAN:{borrower}:{offer_id}:{token_id}".encode()
            ).hexdigest()[:12]
            repay_total = int(offer.amount * (1 + offer.interest))
            self._loans[loan_id] = {
                "loan_id":    loan_id,
                "borrower":   borrower,
                "lender":     offer.lender,
                "collection": offer.collection_id,
                "token_id":   token_id,
                "principal":  offer.amount,
                "repay":      repay_total,
                "due_block":  self._bc.height + offer.duration_blocks,
                "status":     "active",
            }
            offer.active = False
            return True, f"Loan {loan_id}: {offer.amount/10**DECIMALS:.3f} NBL borrowed"

    def repay(self, borrower: str, loan_id: str) -> Tuple[bool, str]:
        with self._lock:
            loan = self._loans.get(loan_id)
            if not loan or loan["borrower"] != borrower:
                return False, "Loan not found"
            if loan["status"] != "active":
                return False, "Not active"
            if self._bc.utxo.balance(borrower) < loan["repay"]:
                return False, "Insufficient balance"
            loan["status"] = "repaid"
            return True, f"Repaid {loan['repay']/10**DECIMALS:.6f} NBL"

    def nft_lending_stats(self) -> dict:
        with self._lock:
            active = sum(1 for l in self._loans.values()
                         if l["status"] == "active")
        return {
            "offers":       len(self._offers),
            "active_loans": active,
            "total_loans":  len(self._loans),
        }


# ---- DAOv2
class DAOv2:
    """
    DAO v2 — structured working groups and committee governance.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  treasury: 'NEBULATreasury' = None):
        self._bc       = blockchain
        self._treasury = treasury
        self._working_groups: Dict[str, dict] = {}
        self._members:        Dict[str, dict] = {}
        self._proposals:      List[dict]      = []
        self._lock     = threading.RLock()

    def create_working_group(self, name: str, lead: str,
                              budget_nbl: float) -> str:
        with self._lock:
            wgid = hashlib.sha256(
                f"WG:{name}:{lead}".encode()
            ).hexdigest()[:8]
            self._working_groups[wgid] = {
                "id":      wgid,
                "name":    name,
                "lead":    lead,
                "budget":  int(budget_nbl * 10**DECIMALS),
                "spent":   0,
                "members": [],
            }
            return wgid

    def join_dao(self, address: str, stake: int) -> bool:
        with self._lock:
            if address in self._members:
                return False
            self._members[address] = {
                "address":  address,
                "stake":    stake,
                "joined":   time.time(),
                "role":     "member",
            }
            return True

    def propose_funding(self, proposer: str, wg_id: str,
                         amount_nbl: float,
                         justification: str) -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"DAOV2:{proposer}:{wg_id}:{amount_nbl}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._proposals.append({
                "id":            pid,
                "proposer":      proposer,
                "wg_id":         wg_id,
                "amount":        amount_nbl,
                "justification": justification,
                "votes":         0.0,
                "status":        "voting",
            })
            return pid

    def vote_and_execute(self, voter: str, proposal_id: str,
                          weight: float = 1.0) -> Tuple[bool, str]:
        with self._lock:
            prop = next((p for p in self._proposals
                         if p["id"] == proposal_id), None)
            if not prop:
                return False, "Not found"
            prop["votes"] += weight
            if prop["votes"] >= 1000:
                wg = self._working_groups.get(prop["wg_id"])
                if wg:
                    amount = int(prop["amount"] * 10**DECIMALS)
                    if amount <= wg["budget"] - wg["spent"]:
                        wg["spent"] += amount
                        prop["status"] = "funded"
                        return True, f"Funded: {prop['amount']} NBL to {wg['name']}"
            return True, f"Vote recorded ({prop['votes']:.0f} total)"

    def dao_v2_stats(self) -> dict:
        return {
            "members":        len(self._members),
            "working_groups": len(self._working_groups),
            "proposals":      len(self._proposals),
        }


# ---- MultisigTreasury
class MultisigTreasury:
    """
    Multisig-controlled treasury for NEBULA.
    3-of-5 by default, configurable.
    """

    def __init__(self, signers: List[str],
                  required: int,
                  blockchain: 'NEBULABlockchain'):
        assert 1 <= required <= len(signers)
        self._signers  = signers
        self._required = required
        self._bc       = blockchain
        self._balance  = 0
        self._txs:     List[dict] = []
        self._sigs:    Dict[str, Set[str]] = {}
        self._lock     = threading.RLock()

    def deposit(self, amount: int):
        self._balance += amount

    def propose_spend(self, proposer: str, to: str,
                       amount: int, memo: str = "") -> Tuple[bool, str]:
        with self._lock:
            if proposer not in self._signers:
                return False, "Not a signer"
            if amount > self._balance:
                return False, "Insufficient treasury"
            txid = hashlib.sha256(
                f"MSTX:{proposer}:{to}:{amount}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._txs.append({
                "id":       txid,
                "to":       to,
                "amount":   amount,
                "memo":     memo,
                "status":   "pending",
            })
            self._sigs[txid] = {proposer}
            return True, txid

    def sign(self, signer: str, txid: str) -> Tuple[bool, str]:
        with self._lock:
            if signer not in self._signers:
                return False, "Not a signer"
            tx = next((t for t in self._txs if t["id"] == txid), None)
            if not tx or tx["status"] != "pending":
                return False, "Not found"
            self._sigs[txid].add(signer)
            n = len(self._sigs[txid])
            if n >= self._required:
                self._balance -= tx["amount"]
                tx["status"] = "executed"
                return True, f"Executed: {tx['amount']/10**DECIMALS:.3f} NBL to {tx['to']}"
            return True, f"Signed ({n}/{self._required})"

    def ms_treasury_stats(self) -> dict:
        return {
            "balance_nbl": f"{self._balance/10**DECIMALS:.3f}",
            "signers":     len(self._signers),
            "required":    self._required,
            "pending_txs": sum(1 for t in self._txs if t["status"] == "pending"),
        }


# ---- RecursiveZKProof
class RecursiveZKProof:
    """
    Recursive ZK proof system for NEBULA.
    Allows proofs to verify other proofs — enabling infinite scalability.
    """

    def __init__(self):
        self._proofs: Dict[str, dict] = {}
        self._lock   = threading.RLock()

    def create_proof(self, statement: str,
                      witness: bytes) -> dict:
        """Create a ZK proof for a statement."""
        proof_hash = hashlib.sha256(
            statement.encode() + witness
        ).hexdigest()
        proof = {
            "proof_id":  hashlib.sha256(proof_hash.encode()).hexdigest()[:12],
            "statement": statement,
            "hash":      proof_hash,
            "recursive": False,
            "ts":        time.time(),
        }
        with self._lock:
            self._proofs[proof["proof_id"]] = proof
        return proof

    def create_recursive_proof(self,
                                statement: str,
                                inner_proof_ids: List[str],
                                witness: bytes) -> dict:
        """Create a recursive proof that verifies multiple inner proofs."""
        with self._lock:
            inner_hashes = [
                self._proofs[pid]["hash"]
                for pid in inner_proof_ids
                if pid in self._proofs
            ]
        combined   = hashlib.sha256(
            statement.encode() +
            b"".join(h.encode() for h in inner_hashes) +
            witness
        ).hexdigest()
        proof = {
            "proof_id":    hashlib.sha256(combined.encode()).hexdigest()[:12],
            "statement":   statement,
            "hash":        combined,
            "recursive":   True,
            "verifies":    inner_proof_ids,
            "inner_count": len(inner_proof_ids),
            "ts":          time.time(),
        }
        with self._lock:
            self._proofs[proof["proof_id"]] = proof
        return proof

    def verify(self, proof_id: str) -> bool:
        """Verify a proof (simplified)."""
        return proof_id in self._proofs

    def proof_stats(self) -> dict:
        with self._lock:
            recursive = sum(1 for p in self._proofs.values()
                            if p.get("recursive"))
        return {
            "total_proofs":    len(self._proofs),
            "recursive_proofs": recursive,
            "simple_proofs":    len(self._proofs) - recursive,
        }
