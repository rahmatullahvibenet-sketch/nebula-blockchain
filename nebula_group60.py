"""NEBULA group60 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. IBCProtocol  (orig. lines 103050-103119)
   2. LiquidRestaking  (orig. lines 103126-103194)
   3. PerpetualV2  (orig. lines 103201-103322)
   4. OptionsVault  (orig. lines 103329-103394)
   5. IsolatedMarket  (orig. lines 103401-103471)
   6. LendingProtocolV3  (orig. lines 103474-103537)
   7. NFTMintPhase  (orig. lines 103544-103570)
   8. NFTLaunchpadV2  (orig. lines 103573-103669)
   9. VeTokenomics  (orig. lines 103676-103766)
  10. VestingScheduleV2  (orig. lines 103773-103830)
  11. TokenVestingManager  (orig. lines 103833-103885)
  12. RiskManagementSystem  (orig. lines 103892-103982)
  13. NEBULAEcosystemV2  (orig. lines 103989-104065)
  14. MultiSigDAO  (orig. lines 104073-104128)
  15. OnChainGrantsDAO  (orig. lines 104131-104216)
  16. ChainlinkStyleOracle  (orig. lines 104223-104286)
  17. SwapAggregatorV3  (orig. lines 104293-104382)
  18. PortfolioTrackerV2  (orig. lines 104389-104460)
  19. HardwareWalletSimulator  (orig. lines 104467-104500)
  20. NEBULAMemoryPool  (orig. lines 104507-104567)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): HDKey, IBCPacket
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

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- IBCProtocol
class IBCProtocol:
    """Full IBC protocol implementation for NEBULA."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._channels: dict = {}
        self._packets:  list = []
        self._acks:     dict = {}
        self._lock      = threading.RLock()

    def create_channel(self, port: str, counterparty_chain: str,
                        counterparty_port: str) -> str:
        with self._lock:
            ch_id = f"channel-{len(self._channels)}"
            self._channels[ch_id] = {
                "channel_id":          ch_id,
                "port":                port,
                "counterparty_chain":  counterparty_chain,
                "counterparty_port":   counterparty_port,
                "state":               "OPEN",
                "ordering":            "UNORDERED",
                "version":             "ics20-1",
                "sequence":            0,
            }
            return ch_id

    def send_packet(self, src_port: str, src_channel: str,
                     data: bytes, timeout_blocks: int = 100) -> dict:
        with self._lock:
            ch = next((c for c in self._channels.values()
                       if c["port"] == src_port and
                          f"channel-{len(self._channels)-1}" == src_channel), None)
            # Find channel
            ch = self._channels.get(src_channel)
            if not ch or ch["state"] != "OPEN":
                return {"ok": False, "error": "Channel not open"}
            ch["sequence"] += 1
            pkt = IBCPacket(
                sequence       = ch["sequence"],
                src_port       = src_port,
                src_channel    = src_channel,
                dst_port       = ch["counterparty_port"],
                dst_channel    = src_channel,
                data           = data,
                timeout_height = self._bc.height + timeout_blocks,
            )
            self._packets.append(pkt)
            return {"ok": True, "packet_id": pkt.packet_id,
                    "sequence": pkt.sequence}

    def acknowledge_packet(self, packet_id: str,
                            ack_data: bytes) -> bool:
        with self._lock:
            pkt = next((p for p in self._packets
                        if p.packet_id == packet_id), None)
            if not pkt:
                return False
            self._acks[packet_id] = {
                "ack":  ack_data.hex(),
                "block": self._bc.height,
            }
            return True

    def ibc_stats(self) -> dict:
        return {
            "channels": len(self._channels),
            "packets":  len(self._packets),
            "acks":     len(self._acks),
            "protocol": "IBC (Inter-Blockchain Communication)",
        }


# ---- LiquidRestaking
class LiquidRestaking:
    """
    Liquid restaking protocol — restake stNBL to earn additional yield.
    Based on EigenLayer restaking concept.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  stnbl: 'StakedNBL'):
        self._bc      = blockchain
        self._stnbl   = stnbl
        self._restaked: dict = {}
        self._avs_list: list = []
        self._rewards:  dict = {}
        self._lock     = threading.RLock()

    def register_avs(self, name: str, operator: str,
                      apy: float, slashing_risk: float) -> str:
        """Register an Actively Validated Service."""
        avs_id = hashlib.sha256(f"AVS:{name}:{operator}".encode()).hexdigest()[:12]
        self._avs_list.append({
            "avs_id":   avs_id,
            "name":     name,
            "operator": operator,
            "apy":      apy,
            "risk":     slashing_risk,
            "stakers":  {},
        })
        return avs_id

    def restake(self, staker: str, avs_id: str,
                 stnbl_amount: int) -> dict:
        with self._lock:
            if self._stnbl.stnbl_balance(staker) < stnbl_amount:
                return {"ok": False, "error": "Insufficient stNBL"}
            avs = next((a for a in self._avs_list if a["avs_id"] == avs_id), None)
            if not avs:
                return {"ok": False, "error": "AVS not found"}
            avs["stakers"][staker] = avs["stakers"].get(staker, 0) + stnbl_amount
            key = f"{staker}:{avs_id}"
            self._restaked[key] = self._restaked.get(key, 0) + stnbl_amount
            return {
                "ok":      True,
                "avs":     avs["name"],
                "amount":  f"{stnbl_amount/10**DECIMALS:.6f} stNBL",
                "extra_apy": f"{avs['apy']*100:.2f}%",
            }

    def accrue_restaking_rewards(self) -> dict:
        total_accrued = 0
        with self._lock:
            for avs in self._avs_list:
                for staker, amount in avs["stakers"].items():
                    reward = int(amount * avs["apy"] / (365 * 144))
                    self._rewards[staker] = self._rewards.get(staker, 0) + reward
                    total_accrued += reward
        return {"accrued_nbl": f"{total_accrued/10**DECIMALS:.6f}"}

    def claim_restaking_rewards(self, staker: str) -> int:
        with self._lock:
            amount = self._rewards.pop(staker, 0)
            return amount

    def restaking_stats(self) -> dict:
        total = sum(sum(a["stakers"].values()) for a in self._avs_list)
        return {
            "avs_count":        len(self._avs_list),
            "total_restaked":   f"{total/10**DECIMALS:.3f} stNBL",
            "pending_rewards":  f"{sum(self._rewards.values())/10**DECIMALS:.6f}",
        }


# ---- PerpetualV2
class PerpetualV2:
    """
    Advanced perpetual futures v2 with funding rate,
    mark price, insurance fund.
    """

    FUNDING_INTERVAL = 28800   # 8 hours in seconds
    MAX_LEVERAGE     = 100     # 100x max

    def __init__(self, pair: str, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self.pair         = pair
        self._bc          = blockchain
        self._oracle      = oracle
        self._positions:  dict = {}
        self._insurance:  int  = 0
        self._last_funding = time.time()
        self._cumulative_funding = 0.0
        self._lock        = threading.RLock()

    def mark_price(self) -> float:
        return (self._oracle.price(self.pair) if self._oracle else 0.01) or 0.01

    def funding_rate(self) -> float:
        """Calculate funding rate based on premium/discount."""
        mark  = self.mark_price()
        index = mark   # simplified
        premium = (mark - index) / index if index > 0 else 0
        return max(-0.001, min(0.001, premium / 24))   # clamp ±0.1% per 8h

    def open_position(self, trader: str, side: str,
                       size_nbl: float, leverage: int) -> dict:
        with self._lock:
            if leverage > self.MAX_LEVERAGE:
                return {"ok": False, "error": f"Max leverage: {self.MAX_LEVERAGE}x"}
            margin  = size_nbl / leverage
            bal     = self._bc.utxo.balance(trader) / 10**DECIMALS
            if bal < margin:
                return {"ok": False, "error": f"Need {margin:.4f} NBL margin"}
            pos_id  = hashlib.sha256(
                f"PERP:{trader}:{side}:{time.time()}".encode()
            ).hexdigest()[:12]
            entry   = self.mark_price()
            self._positions[pos_id] = {
                "pos_id":   pos_id,
                "trader":   trader,
                "side":     side,
                "size":     size_nbl,
                "leverage": leverage,
                "margin":   margin,
                "entry":    entry,
                "liq_price": entry * (1 - 0.9/leverage) if side == "long"
                              else entry * (1 + 0.9/leverage),
                "funding_paid": 0.0,
                "open":     True,
            }
            return {
                "ok":       True,
                "pos_id":   pos_id,
                "side":     side,
                "size":     f"{size_nbl:.4f} NBL",
                "leverage": f"{leverage}x",
                "entry":    f"${entry:.6f}",
                "margin":   f"{margin:.6f} NBL",
                "liq_price": f"${self._positions[pos_id]['liq_price']:.6f}",
            }

    def close_position(self, trader: str, pos_id: str) -> dict:
        with self._lock:
            pos = self._positions.get(pos_id)
            if not pos or pos["trader"] != trader or not pos["open"]:
                return {"ok": False, "error": "Position not found"}
            exit_price = self.mark_price()
            if pos["side"] == "long":
                pnl = (exit_price - pos["entry"]) / pos["entry"] * pos["size"]
            else:
                pnl = (pos["entry"] - exit_price) / pos["entry"] * pos["size"]
            pos["open"] = False
            return {
                "ok":        True,
                "pnl_nbl":   f"{pnl:+.6f}",
                "exit":      f"${exit_price:.6f}",
                "entry":     f"${pos['entry']:.6f}",
                "result":    "profit" if pnl > 0 else "loss",
            }

    def apply_funding(self) -> dict:
        now  = time.time()
        if now - self._last_funding < self.FUNDING_INTERVAL:
            return {"applied": False}
        rate = self.funding_rate()
        with self._lock:
            total_paid = 0
            for pos in self._positions.values():
                if not pos["open"]:
                    continue
                payment = pos["size"] * abs(rate)
                if (rate > 0 and pos["side"] == "long") or \
                   (rate < 0 and pos["side"] == "short"):
                    pos["funding_paid"] += payment
                    self._insurance     += int(payment * 10**DECIMALS)
                else:
                    pos["funding_paid"] -= payment
                total_paid += payment
        self._last_funding      = now
        self._cumulative_funding += rate
        return {
            "applied":          True,
            "rate":             f"{rate*100:.4f}%",
            "total_paid":       f"{total_paid:.6f} NBL",
            "insurance_fund":   f"{self._insurance/10**DECIMALS:.3f} NBL",
        }

    def perp_v2_stats(self) -> dict:
        open_pos = sum(1 for p in self._positions.values() if p["open"])
        return {
            "pair":         self.pair,
            "open_pos":     open_pos,
            "mark_price":   f"${self.mark_price():.6f}",
            "funding_rate": f"{self.funding_rate()*100:.4f}%",
            "insurance":    f"{self._insurance/10**DECIMALS:.3f} NBL",
        }


# ---- OptionsVault
class OptionsVault:
    """Automated options vault for covered calls & cash-secured puts."""

    def __init__(self, asset: str, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self.asset     = asset
        self._bc       = blockchain
        self._oracle   = oracle
        self._deposits: dict = {}
        self._written:  list = []
        self._premium:  int  = 0
        self._lock     = threading.RLock()

    def deposit(self, depositor: str, amount: int) -> bool:
        with self._lock:
            if self._bc.utxo.balance(depositor) < amount:
                return False
            self._deposits[depositor] = (
                self._deposits.get(depositor, 0) + amount)
            return True

    def write_covered_call(self, strike_pct_above: float = 0.10,
                            expiry_days: int = 30) -> dict:
        """Write covered call at X% above current price."""
        spot   = (self._oracle.price(f"{self.asset}/USD")
                  if self._oracle else 0.01) or 0.01
        strike = spot * (1 + strike_pct_above)
        total  = sum(self._deposits.values())
        if total == 0:
            return {"ok": False, "error": "No deposits"}
        # Simplified premium: 2-5% of notional
        premium_usd = total / 10**DECIMALS * spot * 0.03
        self._premium += int(premium_usd * 10**DECIMALS / spot)
        option = {
            "type":    "covered_call",
            "asset":   self.asset,
            "strike":  strike,
            "expiry":  expiry_days,
            "premium": f"${premium_usd:.4f}",
            "written": time.time(),
        }
        self._written.append(option)
        return {"ok": True, **option}

    def distribute_premium(self) -> dict:
        total = sum(self._deposits.values()) or 1
        dist  = {}
        for dep, amount in self._deposits.items():
            share = int(self._premium * amount / total)
            dist[dep] = share
        premium_paid   = self._premium
        self._premium  = 0
        return {
            "distributed": f"{premium_paid/10**DECIMALS:.6f} NBL",
            "depositors":  len(dist),
        }

    def vault_stats(self) -> dict:
        total = sum(self._deposits.values())
        return {
            "asset":        self.asset,
            "tvl_nbl":      f"{total/10**DECIMALS:.3f}",
            "depositors":   len(self._deposits),
            "options_written": len(self._written),
            "pending_premium": f"{self._premium/10**DECIMALS:.6f}",
        }


# ---- IsolatedMarket
class IsolatedMarket:
    """Isolated lending market — separate risk per asset pair."""

    def __init__(self, collateral_asset: str, borrow_asset: str,
                  ltv: float, liquidation_threshold: float,
                  blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self.collateral   = collateral_asset
        self.borrow       = borrow_asset
        self.ltv          = ltv
        self.liq_thresh   = liquidation_threshold
        self._bc          = blockchain
        self._oracle      = oracle
        self._positions:  dict = {}
        self._supply:     int  = 0
        self._borrows:    int  = 0
        self._lock        = threading.RLock()

    def supply(self, lender: str, amount: int) -> bool:
        with self._lock:
            self._supply += amount
            return True

    def borrow(self, borrower: str, collateral: int,
                borrow_amount: int) -> dict:
        with self._lock:
            col_price  = (self._oracle.price(f"{self.collateral}/USD")
                          if self._oracle else 1.0) or 1.0
            bor_price  = (self._oracle.price(f"{self.borrow}/USD")
                          if self._oracle else 1.0) or 1.0
            col_usd    = collateral / 10**DECIMALS * col_price
            max_borrow = col_usd * self.ltv / bor_price * 10**DECIMALS
            if borrow_amount > max_borrow:
                return {"ok": False,
                        "error": f"Max borrow: {max_borrow/10**DECIMALS:.4f}"}
            if borrow_amount > self._supply - self._borrows:
                return {"ok": False, "error": "Insufficient liquidity"}
            self._positions[borrower] = {
                "collateral": collateral,
                "borrowed":   borrow_amount,
                "col_asset":  self.collateral,
                "bor_asset":  self.borrow,
            }
            self._borrows += borrow_amount
            return {
                "ok":      True,
                "borrowed": f"{borrow_amount/10**DECIMALS:.4f} {self.borrow}",
                "ltv":      f"{self.ltv*100:.0f}%",
            }

    def health_factor(self, borrower: str) -> float:
        pos = self._positions.get(borrower)
        if not pos or pos["borrowed"] == 0:
            return float('inf')
        col_price = (self._oracle.price(f"{self.collateral}/USD")
                     if self._oracle else 1.0) or 1.0
        bor_price = (self._oracle.price(f"{self.borrow}/USD")
                     if self._oracle else 1.0) or 1.0
        col_usd   = pos["collateral"] / 10**DECIMALS * col_price
        bor_usd   = pos["borrowed"]   / 10**DECIMALS * bor_price
        return col_usd * self.liq_thresh / bor_usd if bor_usd > 0 else float('inf')

    def market_stats(self) -> dict:
        util = self._borrows / self._supply if self._supply > 0 else 0
        return {
            "pair":        f"{self.collateral}/{self.borrow}",
            "supplied":    f"{self._supply/10**DECIMALS:.3f}",
            "borrowed":    f"{self._borrows/10**DECIMALS:.3f}",
            "utilization": f"{util*100:.1f}%",
            "ltv":         f"{self.ltv*100:.0f}%",
        }


# ---- LendingProtocolV3
class LendingProtocolV3:
    """Lending v3 with isolated markets, e-mode, and flash loans."""

    EMODE_CATEGORIES = {
        "stablecoins": {"ltv": 0.97, "liq_thresh": 0.98, "bonus": 0.01},
        "eth_corr":    {"ltv": 0.90, "liq_thresh": 0.93, "bonus": 0.02},
        "btc_corr":    {"ltv": 0.85, "liq_thresh": 0.90, "bonus": 0.03},
    }

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._markets: dict = {}
        self._user_emode: dict = {}
        self._lock    = threading.RLock()

    def create_market(self, collateral: str, borrow: str,
                       ltv: float = 0.75,
                       liq_thresh: float = 0.80) -> str:
        with self._lock:
            mid = f"{collateral}/{borrow}"
            self._markets[mid] = IsolatedMarket(
                collateral, borrow, ltv, liq_thresh,
                self._bc, self._oracle)
            return mid

    def enable_emode(self, user: str, category: str) -> dict:
        if category not in self.EMODE_CATEGORIES:
            return {"ok": False, "error": "Unknown e-mode category"}
        self._user_emode[user] = category
        params = self.EMODE_CATEGORIES[category]
        return {
            "ok":       True,
            "category": category,
            "ltv":      f"{params['ltv']*100:.0f}%",
            "bonus":    f"{params['bonus']*100:.0f}% extra",
            "note":     "E-Mode only works within same asset category",
        }

    def flash_loan_v3(self, borrower: str, market_id: str,
                       amount: int, callback_data: bytes = b"") -> dict:
        market = self._markets.get(market_id)
        if not market:
            return {"ok": False, "error": "Market not found"}
        fee = int(amount * 0.0009)   # 0.09% fee
        return {
            "ok":       True,
            "amount":   f"{amount/10**DECIMALS:.6f}",
            "fee":      f"{fee/10**DECIMALS:.6f}",
            "market":   market_id,
            "note":     "Must repay within same transaction",
        }

    def protocol_v3_stats(self) -> dict:
        total_supply  = sum(m._supply for m in self._markets.values())
        total_borrows = sum(m._borrows for m in self._markets.values())
        return {
            "markets":        len(self._markets),
            "total_supply":   f"{total_supply/10**DECIMALS:.3f}",
            "total_borrows":  f"{total_borrows/10**DECIMALS:.3f}",
            "emode_users":    len(self._user_emode),
            "version":        "Lending v3 (Aave v3 style)",
        }


# ---- NFTMintPhase
class NFTMintPhase:
    """A single mint phase (whitelist, public, etc)."""

    def __init__(self, name: str, start_block: int,
                  end_block: int, price_nbl: float,
                  max_per_wallet: int, allowlist: list = None):
        self.name           = name
        self.start_block    = start_block
        self.end_block      = end_block
        self.price          = int(price_nbl * 10**DECIMALS)
        self.max_per_wallet = max_per_wallet
        self.allowlist      = set(allowlist or [])
        self.minted:        dict = {}

    def can_mint(self, minter: str, cur_block: int) -> Tuple[bool, str]:
        if cur_block < self.start_block:
            return False, f"Phase not started (starts block {self.start_block})"
        if cur_block > self.end_block:
            return False, "Phase ended"
        if self.allowlist and minter not in self.allowlist:
            return False, "Not on allowlist for this phase"
        if self.minted.get(minter, 0) >= self.max_per_wallet:
            return False, f"Max {self.max_per_wallet} per wallet"
        return True, "OK"

    def record_mint(self, minter: str, count: int = 1):
        self.minted[minter] = self.minted.get(minter, 0) + count


# ---- NFTLaunchpadV2
class NFTLaunchpadV2:
    """Full NFT launchpad with multi-phase minting."""

    def __init__(self, nft: 'NBL721Registry',
                  blockchain: 'NEBULABlockchain'):
        self._nft    = nft
        self._bc     = blockchain
        self._projects: dict = {}
        self._lock   = threading.RLock()

    def create_project(self, creator: str, name: str,
                        symbol: str, max_supply: int,
                        royalty: float = 0.05,
                        base_uri: str = "") -> str:
        with self._lock:
            col_id = self._nft.create_collection(
                creator, name, symbol,
                f"NEBULA NFT: {name}", max_supply, royalty)
            self._projects[col_id] = {
                "col_id":   col_id,
                "creator":  creator,
                "name":     name,
                "symbol":   symbol,
                "max":      max_supply,
                "base_uri": base_uri or f"ipfs://nebula/{col_id}/",
                "phases":   [],
                "minted":   0,
                "revenue":  0,
            }
            return col_id

    def add_phase(self, col_id: str, name: str,
                   start_block: int, end_block: int,
                   price_nbl: float, max_per_wallet: int,
                   allowlist: list = None) -> int:
        with self._lock:
            proj = self._projects.get(col_id)
            if not proj:
                return -1
            phase = NFTMintPhase(name, start_block, end_block,
                                  price_nbl, max_per_wallet, allowlist)
            proj["phases"].append(phase)
            return len(proj["phases"]) - 1

    def mint(self, minter: str, col_id: str,
              quantity: int = 1) -> dict:
        with self._lock:
            proj = self._projects.get(col_id)
            if not proj:
                return {"ok": False, "error": "Project not found"}
            if proj["minted"] + quantity > proj["max"]:
                return {"ok": False, "error": "Max supply reached"}
            # Find active phase
            cur = self._bc.height
            active = next((p for p in proj["phases"]
                           if p.start_block <= cur <= p.end_block), None)
            if not active:
                return {"ok": False, "error": "No active mint phase"}
            can, msg = active.can_mint(minter, cur)
            if not can:
                return {"ok": False, "error": msg}
            total_cost = active.price * quantity
            if self._bc.utxo.balance(minter) < total_cost:
                return {"ok": False, "error": "Insufficient NBL"}
            token_ids = []
            for _ in range(quantity):
                proj["minted"] += 1
                tid = proj["minted"]
                self._nft._collections[col_id]["tokens"][tid] = {
                    "owner": minter,
                    "uri":   f"{proj['base_uri']}{tid}.json",
                    "meta":  {"name": f"{proj['name']} #{tid}"},
                    "approved": None,
                }
                token_ids.append(tid)
            active.record_mint(minter, quantity)
            proj["revenue"] += total_cost
            return {
                "ok":       True,
                "minted":   quantity,
                "token_ids": token_ids,
                "cost":     f"{total_cost/10**DECIMALS:.4f} NBL",
                "phase":    active.name,
            }

    def project_stats(self, col_id: str) -> dict:
        proj = self._projects.get(col_id)
        if not proj:
            return {}
        return {
            "name":     proj["name"],
            "minted":   proj["minted"],
            "max":      proj["max"],
            "sold_pct": f"{proj['minted']/max(1,proj['max'])*100:.1f}%",
            "revenue":  f"{proj['revenue']/10**DECIMALS:.3f} NBL",
            "phases":   len(proj["phases"]),
        }


# ---- VeTokenomics
class VeTokenomics:
    """
    Full veToken (vote-escrowed) economics model.
    Lock NBL → receive veNBL → earn fees + governance power.
    """

    MAX_LOCK_WEEKS = 208   # 4 years
    BOOST_MAX      = 2.5   # 2.5x max boost

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc     = blockchain
        self._locks: dict = {}   # address -> {amount, end_block, power}
        self._weekly_fees: list = []
        self._lock   = threading.RLock()

    def lock(self, address: str, amount: int,
              weeks: int) -> dict:
        with self._lock:
            if weeks > self.MAX_LOCK_WEEKS:
                return {"ok": False, "error": f"Max {self.MAX_LOCK_WEEKS} weeks"}
            if self._bc.utxo.balance(address) < amount:
                return {"ok": False, "error": "Insufficient balance"}
            existing = self._locks.get(address, {})
            new_end  = self._bc.height + weeks * 144 * 7
            end_block = max(existing.get("end_block", 0), new_end)
            new_amount = existing.get("amount", 0) + amount
            # veNBL power = amount * remaining_weeks / max_weeks
            remaining_weeks = (end_block - self._bc.height) / (144 * 7)
            ve_power = int(new_amount * remaining_weeks / self.MAX_LOCK_WEEKS)
            self._locks[address] = {
                "amount":    new_amount,
                "end_block": end_block,
                "ve_power":  ve_power,
                "locked_at": self._bc.height,
            }
            return {
                "ok":       True,
                "locked":   f"{amount/10**DECIMALS:.3f} NBL",
                "total":    f"{new_amount/10**DECIMALS:.3f} NBL",
                "ve_power": f"{ve_power/10**DECIMALS:.3f} veNBL",
                "weeks":    weeks,
                "unlocks":  end_block,
            }

    def ve_balance(self, address: str) -> int:
        lock = self._locks.get(address)
        if not lock or self._bc.height >= lock["end_block"]:
            return 0
        remaining = lock["end_block"] - self._bc.height
        total_lock = self.MAX_LOCK_WEEKS * 144 * 7
        return int(lock["amount"] * remaining / total_lock)

    def boost(self, address: str, base_reward: int) -> int:
        """Calculate boosted reward based on veNBL."""
        ve   = self.ve_balance(address)
        total_ve = sum(self.ve_balance(a) for a in self._locks)
        if total_ve == 0:
            return base_reward
        boost_factor = min(self.BOOST_MAX,
                           1 + 1.5 * (ve / total_ve) ** 0.5)
        return int(base_reward * boost_factor)

    def distribute_fees(self, total_fees: int) -> dict:
        """Distribute protocol fees to veNBL holders."""
        total_ve = sum(self.ve_balance(a) for a in self._locks)
        if total_ve == 0:
            return {"distributed": 0}
        dist = {}
        for addr in self._locks:
            ve    = self.ve_balance(addr)
            share = int(total_fees * ve / total_ve)
            dist[addr] = share
        week_record = {
            "total_fees": total_fees,
            "recipients": len(dist),
            "block":      self._bc.height,
        }
        self._weekly_fees.append(week_record)
        return {"distributed": f"{total_fees/10**DECIMALS:.6f}", "dist": dist}

    def ve_stats(self) -> dict:
        total_locked = sum(l["amount"] for l in self._locks.values())
        total_ve     = sum(self.ve_balance(a) for a in self._locks)
        return {
            "total_locked_nbl":  f"{total_locked/10**DECIMALS:.3f}",
            "total_ve_power":    f"{total_ve/10**DECIMALS:.3f}",
            "lockers":           len(self._locks),
            "max_lock_weeks":    self.MAX_LOCK_WEEKS,
            "max_boost":         f"{self.BOOST_MAX}x",
            "fee_epochs":        len(self._weekly_fees),
        }


# ---- VestingScheduleV2
class VestingScheduleV2:
    """Advanced token vesting with cliff, linear, and milestone-based."""

    def __init__(self, beneficiary: str, total: int,
                  cliff_blocks: int, vesting_blocks: int,
                  blockchain: 'NEBULABlockchain',
                  schedule_type: str = "linear"):
        self.beneficiary    = beneficiary
        self.total          = total
        self.cliff          = cliff_blocks
        self.vesting        = vesting_blocks
        self._bc            = blockchain
        self.schedule_type  = schedule_type
        self.created_block  = blockchain.height
        self.claimed        = 0
        self.milestones:    list = []

    def add_milestone(self, block: int, pct: float, description: str):
        """For milestone-based vesting."""
        self.milestones.append({
            "block": block, "pct": pct,
            "desc": description, "claimed": False})

    def vested_amount(self) -> int:
        cur = self._bc.height
        if cur < self.created_block + self.cliff:
            return 0   # Still in cliff period
        if self.schedule_type == "milestone":
            return sum(
                int(self.total * m["pct"])
                for m in self.milestones
                if cur >= m["block"] and not m["claimed"]
            )
        elapsed  = cur - self.created_block - self.cliff
        fraction = min(1.0, elapsed / max(1, self.vesting))
        return int(self.total * fraction)

    def claimable(self) -> int:
        return max(0, self.vested_amount() - self.claimed)

    def claim(self) -> int:
        amount = self.claimable()
        self.claimed += amount
        return amount

    def vesting_info(self) -> dict:
        cur   = self._bc.height
        cliff_end = self.created_block + self.cliff
        return {
            "beneficiary":  self.beneficiary,
            "total_nbl":    f"{self.total/10**DECIMALS:.3f}",
            "claimed_nbl":  f"{self.claimed/10**DECIMALS:.3f}",
            "claimable":    f"{self.claimable()/10**DECIMALS:.3f}",
            "cliff_ends":   cliff_end,
            "cliff_done":   cur >= cliff_end,
            "type":         self.schedule_type,
            "pct_vested":   f"{min(100, self.vested_amount()/max(1,self.total)*100):.1f}%",
        }


# ---- TokenVestingManager
class TokenVestingManager:
    """Manages vesting schedules for team, investors, ecosystem."""

    CATEGORIES = {
        "team":       {"cliff_months": 12, "vesting_months": 48},
        "investors":  {"cliff_months": 6,  "vesting_months": 24},
        "advisors":   {"cliff_months": 3,  "vesting_months": 18},
        "ecosystem":  {"cliff_months": 0,  "vesting_months": 36},
        "foundation": {"cliff_months": 0,  "vesting_months": 60},
        "community":  {"cliff_months": 0,  "vesting_months": 24},
    }

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._schedules: list = []
        self._lock     = threading.RLock()

    def create_vesting(self, beneficiary: str, amount_nbl: float,
                        category: str = "team") -> dict:
        with self._lock:
            params = self.CATEGORIES.get(category, self.CATEGORIES["team"])
            cliff_b   = params["cliff_months"] * 30 * 144
            vesting_b = params["vesting_months"] * 30 * 144
            schedule  = VestingScheduleV2(
                beneficiary, int(amount_nbl * 10**DECIMALS),
                cliff_b, vesting_b, self._bc)
            self._schedules.append(schedule)
            return {
                "ok":          True,
                "beneficiary": beneficiary,
                "amount_nbl":  amount_nbl,
                "category":    category,
                "cliff_months": params["cliff_months"],
                "vesting_months": params["vesting_months"],
                "starts":      self._bc.height + cliff_b,
            }

    def claim_all(self, beneficiary: str) -> int:
        total = 0
        for s in self._schedules:
            if s.beneficiary == beneficiary:
                total += s.claim()
        return total

    def vesting_stats(self) -> dict:
        total_locked  = sum(s.total for s in self._schedules)
        total_claimed = sum(s.claimed for s in self._schedules)
        return {
            "schedules":      len(self._schedules),
            "total_locked":   f"{total_locked/10**DECIMALS:.3f} NBL",
            "total_claimed":  f"{total_claimed/10**DECIMALS:.3f} NBL",
            "beneficiaries":  len(set(s.beneficiary for s in self._schedules)),
        }


# ---- RiskManagementSystem
class RiskManagementSystem:
    """
    Comprehensive risk management for NEBULA DeFi protocols.
    Monitors positions, sets limits, triggers emergency actions.
    """

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc     = blockchain
        self._oracle = oracle
        self._limits: dict = {}
        self._alerts: list = []
        self._paused: set  = set()
        self._lock   = threading.RLock()

    def set_protocol_limit(self, protocol: str,
                            tvl_cap_nbl: float,
                            single_tx_cap: float = 0,
                            daily_vol_cap: float = 0):
        with self._lock:
            self._limits[protocol] = {
                "tvl_cap":    int(tvl_cap_nbl * 10**DECIMALS),
                "tx_cap":     int(single_tx_cap * 10**DECIMALS),
                "daily_cap":  int(daily_vol_cap * 10**DECIMALS),
                "daily_vol":  0,
                "reset_block": self._bc.height + 144,
            }

    def check_tx(self, protocol: str, amount: int) -> Tuple[bool, str]:
        with self._lock:
            if protocol in self._paused:
                return False, f"{protocol} is paused"
            limits = self._limits.get(protocol)
            if not limits:
                return True, "OK"
            if limits["tx_cap"] > 0 and amount > limits["tx_cap"]:
                return False, f"Exceeds single-tx cap: {limits['tx_cap']/10**DECIMALS:.0f} NBL"
            if self._bc.height > limits["reset_block"]:
                limits["daily_vol"]   = 0
                limits["reset_block"] = self._bc.height + 144
            if limits["daily_cap"] > 0:
                if limits["daily_vol"] + amount > limits["daily_cap"]:
                    return False, "Daily volume cap reached"
            limits["daily_vol"] += amount
            return True, "OK"

    def pause_protocol(self, protocol: str, reason: str):
        with self._lock:
            self._paused.add(protocol)
            self._alerts.append({
                "type":     "PAUSE",
                "protocol": protocol,
                "reason":   reason,
                "block":    self._bc.height,
                "ts":       time.time(),
            })

    def resume_protocol(self, protocol: str):
        with self._lock:
            self._paused.discard(protocol)

    def global_risk_score(self) -> dict:
        price   = (self._oracle.price("NBL/USD")
                   if self._oracle else 0.001) or 0.001
        supply  = self._bc.utxo.total_supply() / 10**DECIMALS
        mem_size = self._bc.mempool.size()
        score   = 100
        risks   = []
        if mem_size > 10000:
            score -= 15
            risks.append(f"High mempool congestion: {mem_size} txs")
        if len(self._paused) > 0:
            score -= 20
            risks.append(f"{len(self._paused)} protocol(s) paused")
        if price < 0.0001:
            score -= 10
            risks.append("NBL price extremely low")
        return {
            "score":     score,
            "level":     "LOW" if score >= 80 else "MEDIUM" if score >= 60 else "HIGH",
            "risks":     risks,
            "paused":    list(self._paused),
            "alerts":    len(self._alerts),
        }

    def risk_stats(self) -> dict:
        return {
            "monitored_protocols": len(self._limits),
            "paused_protocols":    len(self._paused),
            "total_alerts":        len(self._alerts),
        }


# ---- NEBULAEcosystemV2
class NEBULAEcosystemV2:
    """Comprehensive NEBULA ecosystem hub v2."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc = blockchain
        self._dapps: list = []
        self._partnerships: list = []
        self._metrics_log: list = []
        self._lock = threading.RLock()

    def register_dapp(self, name: str, category: str,
                       url: str, developer: str,
                       description: str = "") -> str:
        with self._lock:
            dapp_id = hashlib.sha256(
                f"DAPP:{name}:{developer}".encode()
            ).hexdigest()[:10]
            self._dapps.append({
                "dapp_id":     dapp_id,
                "name":        name,
                "category":    category,
                "url":         url,
                "developer":   developer,
                "description": description,
                "users":       0,
                "volume_nbl":  0.0,
                "listed":      time.time(),
                "verified":    False,
            })
            return dapp_id

    def verify_dapp(self, dapp_id: str) -> bool:
        with self._lock:
            dapp = next((d for d in self._dapps
                         if d["dapp_id"] == dapp_id), None)
            if dapp:
                dapp["verified"] = True
                return True
            return False

    def add_partnership(self, partner: str, category: str,
                         description: str,
                         deal_type: str = "integration") -> str:
        with self._lock:
            pid = hashlib.sha256(
                f"PARTNER:{partner}:{time.time()}".encode()
            ).hexdigest()[:10]
            self._partnerships.append({
                "partner_id":  pid,
                "name":        partner,
                "category":    category,
                "description": description,
                "deal_type":   deal_type,
                "announced":   time.time(),
            })
            return pid

    def ecosystem_snapshot(self) -> dict:
        with self._lock:
            verified_dapps = sum(1 for d in self._dapps if d["verified"])
        snap = {
            "block":             self._bc.height,
            "total_dapps":       len(self._dapps),
            "verified_dapps":    verified_dapps,
            "partnerships":      len(self._partnerships),
            "supply_nbl":        f"{self._bc.utxo.total_supply()/10**DECIMALS:.3f}",
            "ts":                time.time(),
        }
        self._metrics_log.append(snap)
        return snap

    def ecosystem_v2_stats(self) -> dict:
        return {
            "dapps":        len(self._dapps),
            "partnerships": len(self._partnerships),
            "snapshots":    len(self._metrics_log),
        }


# ---- MultiSigDAO
class MultiSigDAO:
    """Multi-signature DAO with proposal lifecycle."""

    def __init__(self, members: list, threshold: int,
                  blockchain: 'NEBULABlockchain'):
        self._members   = list(members)
        self._threshold = threshold
        self._bc        = blockchain
        self._proposals: list = []
        self._sigs:     dict = {}
        self._lock      = threading.RLock()

    def propose(self, proposer: str, action: str,
                 params: dict, description: str) -> str:
        if proposer not in self._members:
            return ""
        with self._lock:
            pid = hashlib.sha256(
                f"MSDAO:{proposer}:{action}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._proposals.append({
                "pid":        pid,
                "proposer":   proposer,
                "action":     action,
                "params":     params,
                "description": description,
                "status":     "pending",
                "created":    self._bc.height,
            })
            self._sigs[pid] = {proposer}
            return pid

    def sign(self, signer: str, pid: str) -> dict:
        if signer not in self._members:
            return {"ok": False, "error": "Not a member"}
        with self._lock:
            p = next((p for p in self._proposals if p["pid"] == pid), None)
            if not p or p["status"] != "pending":
                return {"ok": False, "error": "Not found/pending"}
            self._sigs[pid].add(signer)
            n = len(self._sigs[pid])
            if n >= self._threshold:
                p["status"] = "executed"
                return {"ok": True, "executed": True,
                        "sigs": f"{n}/{len(self._members)}"}
            return {"ok": True, "executed": False,
                    "sigs": f"{n}/{self._threshold} needed"}

    def dao_stats(self) -> dict:
        executed = sum(1 for p in self._proposals if p["status"] == "executed")
        return {
            "members":    len(self._members),
            "threshold":  self._threshold,
            "proposals":  len(self._proposals),
            "executed":   executed,
        }


# ---- OnChainGrantsDAO
class OnChainGrantsDAO:
    """Fully on-chain grants DAO with milestone-based disbursements."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  treasury_nbl: float = 1_000_000):
        self._bc       = blockchain
        self._treasury = int(treasury_nbl * 10**DECIMALS)
        self._grants:  list = []
        self._milestones: dict = {}
        self._lock     = threading.RLock()

    def submit_grant(self, applicant: str, title: str,
                      amount_nbl: float, milestones: list,
                      category: str = "development") -> str:
        with self._lock:
            gid = hashlib.sha256(
                f"GRANT:{applicant}:{title}:{time.time()}".encode()
            ).hexdigest()[:12]
            total_pct = sum(m.get("pct", 0) for m in milestones)
            if abs(total_pct - 1.0) > 0.01:
                return ""
            self._grants.append({
                "gid":        gid,
                "applicant":  applicant,
                "title":      title,
                "amount":     int(amount_nbl * 10**DECIMALS),
                "milestones": milestones,
                "category":   category,
                "status":     "reviewing",
                "votes_yes":  0.0,
                "votes_no":   0.0,
                "disbursed":  0,
            })
            self._milestones[gid] = [
                {**m, "completed": False, "paid": False}
                for m in milestones
            ]
            return gid

    def vote_grant(self, voter: str, gid: str,
                    support: bool) -> bool:
        with self._lock:
            g = next((g for g in self._grants if g["gid"] == gid), None)
            if not g or g["status"] != "reviewing":
                return False
            weight = self._bc.utxo.balance(voter) / 10**DECIMALS
            if support:
                g["votes_yes"] += weight
            else:
                g["votes_no"]  += weight
            total = g["votes_yes"] + g["votes_no"]
            if total >= 10_000 and g["votes_yes"] / total >= 0.60:
                g["status"] = "approved"
            return True

    def complete_milestone(self, gid: str, milestone_idx: int) -> dict:
        with self._lock:
            g = next((g for g in self._grants if g["gid"] == gid), None)
            if not g or g["status"] != "approved":
                return {"ok": False, "error": "Grant not approved"}
            ms = self._milestones.get(gid, [])
            if milestone_idx >= len(ms):
                return {"ok": False, "error": "Invalid milestone"}
            m = ms[milestone_idx]
            if m["completed"]:
                return {"ok": False, "error": "Already completed"}
            m["completed"] = True
            m["paid"]      = True
            payout = int(g["amount"] * m["pct"])
            g["disbursed"] += payout
            self._treasury -= payout
            return {
                "ok":      True,
                "payout":  f"{payout/10**DECIMALS:.3f} NBL",
                "milestone": m.get("name", f"Milestone {milestone_idx+1}"),
            }

    def grants_stats(self) -> dict:
        approved = sum(1 for g in self._grants if g["status"] == "approved")
        total_disbursed = sum(g["disbursed"] for g in self._grants)
        return {
            "treasury_nbl":    f"{self._treasury/10**DECIMALS:.3f}",
            "total_grants":    len(self._grants),
            "approved":        approved,
            "total_disbursed": f"{total_disbursed/10**DECIMALS:.3f}",
        }


# ---- ChainlinkStyleOracle
class ChainlinkStyleOracle:
    """Chainlink-style oracle aggregator for NEBULA."""

    def __init__(self):
        self._feeds:    dict = {}
        self._lock      = threading.RLock()

    def create_feed(self, pair: str, decimals: int = 8,
                     description: str = "") -> str:
        with self._lock:
            feed_id = hashlib.sha256(pair.encode()).hexdigest()[:12]
            self._feeds[pair] = {
                "feed_id":      feed_id,
                "pair":         pair,
                "decimals":     decimals,
                "description":  description,
                "answers":      [],   # (round, answer, ts, reporter)
                "latest_round": 0,
            }
            return feed_id

    def transmit(self, pair: str, answer: int,
                  reporter: str) -> int:
        """Transmit a new answer (like Chainlink transmit)."""
        with self._lock:
            feed = self._feeds.get(pair)
            if not feed:
                return -1
            feed["latest_round"] += 1
            rnd = feed["latest_round"]
            feed["answers"].append({
                "round":    rnd,
                "answer":   answer,
                "ts":       time.time(),
                "reporter": reporter,
            })
            if len(feed["answers"]) > 1000:
                feed["answers"].pop(0)
            return rnd

    def latest_answer(self, pair: str) -> Optional[int]:
        feed = self._feeds.get(pair)
        if not feed or not feed["answers"]:
            return None
        return feed["answers"][-1]["answer"]

    def latest_round_data(self, pair: str) -> Optional[dict]:
        feed = self._feeds.get(pair)
        if not feed or not feed["answers"]:
            return None
        a = feed["answers"][-1]
        return {
            "round_id":   a["round"],
            "answer":     a["answer"],
            "started_at": a["ts"],
            "updated_at": a["ts"],
            "answered_in": a["round"],
        }

    def oracle_stats(self) -> dict:
        return {
            "feeds":         len(self._feeds),
            "total_rounds":  sum(len(f["answers"]) for f in self._feeds.values()),
        }


# ---- SwapAggregatorV3
class SwapAggregatorV3:
    """
    DEX aggregator v3 — splits orders across multiple pools
    for best execution price.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc    = blockchain
        self._pools: list = []
        self._routes: list = []
        self._lock  = threading.RLock()

    def add_pool(self, pool_type: str, pool_id: str,
                  token_a: str, token_b: str,
                  reserve_a: float, reserve_b: float,
                  fee: float):
        with self._lock:
            self._pools.append({
                "type":     pool_type,
                "pool_id":  pool_id,
                "token_a":  token_a,
                "token_b":  token_b,
                "reserve_a": reserve_a,
                "reserve_b": reserve_b,
                "fee":      fee,
            })

    def get_quote(self, token_in: str, token_out: str,
                   amount_in: float) -> dict:
        """Get best single-hop quote."""
        best_out = 0.0
        best_pool = None
        for p in self._pools:
            if p["token_a"] == token_in and p["token_b"] == token_out:
                fee_adjusted = amount_in * (1 - p["fee"])
                out = fee_adjusted * p["reserve_b"] / (p["reserve_a"] + fee_adjusted)
            elif p["token_b"] == token_in and p["token_a"] == token_out:
                fee_adjusted = amount_in * (1 - p["fee"])
                out = fee_adjusted * p["reserve_a"] / (p["reserve_b"] + fee_adjusted)
            else:
                continue
            if out > best_out:
                best_out  = out
                best_pool = p
        if not best_pool:
            return {"ok": False, "error": "No liquidity found"}
        return {
            "ok":       True,
            "out":      best_out,
            "pool":     best_pool["pool_id"],
            "price":    best_out / amount_in if amount_in > 0 else 0,
            "fee":      best_pool["fee"],
        }

    def split_order(self, token_in: str, token_out: str,
                     amount_in: float, splits: int = 3) -> dict:
        """Split order across multiple pools for better execution."""
        part_size = amount_in / splits
        total_out = 0.0
        routes    = []
        for _ in range(splits):
            q = self.get_quote(token_in, token_out, part_size)
            if q.get("ok"):
                total_out += q["out"]
                routes.append({
                    "pool":   q["pool"],
                    "amount": part_size,
                    "out":    q["out"],
                })
        self._routes.append({
            "token_in":  token_in,
            "token_out": token_out,
            "amount_in": amount_in,
            "total_out": total_out,
            "routes":    routes,
        })
        return {
            "ok":        True,
            "total_out": total_out,
            "avg_price": total_out / amount_in if amount_in > 0 else 0,
            "splits":    len(routes),
            "routes":    routes,
        }

    def agg_stats(self) -> dict:
        return {
            "pools":   len(self._pools),
            "routes":  len(self._routes),
            "version": "Aggregator v3",
        }


# ---- PortfolioTrackerV2
class PortfolioTrackerV2:
    """Advanced portfolio tracker with P&L, yield, and rebalancing."""

    def __init__(self, blockchain: 'NEBULABlockchain',
                  oracle: 'OracleV2' = None):
        self._bc      = blockchain
        self._oracle  = oracle
        self._portfolios: dict = {}
        self._snapshots:  list = []
        self._lock    = threading.RLock()

    def create_portfolio(self, owner: str,
                          name: str = "My Portfolio") -> str:
        with self._lock:
            pfid = hashlib.sha256(
                f"PF:{owner}:{name}:{time.time()}".encode()
            ).hexdigest()[:12]
            self._portfolios[pfid] = {
                "pfid":      pfid,
                "owner":     owner,
                "name":      name,
                "positions": [],
                "created":   time.time(),
            }
            return pfid

    def add_position(self, pfid: str, protocol: str,
                      asset: str, amount: float,
                      cost_basis: float, apy: float = 0) -> bool:
        with self._lock:
            pf = self._portfolios.get(pfid)
            if not pf:
                return False
            price = (self._oracle.price(f"{asset}/USD")
                     if self._oracle else 0.01) or 0.01
            pf["positions"].append({
                "protocol":    protocol,
                "asset":       asset,
                "amount":      amount,
                "cost_basis":  cost_basis,
                "current_price": price,
                "value_usd":   amount * price,
                "unrealized_pnl": (price - cost_basis) * amount,
                "apy":         apy,
                "added":       time.time(),
            })
            return True

    def portfolio_summary(self, pfid: str) -> dict:
        pf = self._portfolios.get(pfid)
        if not pf:
            return {}
        total_value    = sum(p["value_usd"] for p in pf["positions"])
        total_cost     = sum(p["cost_basis"] * p["amount"] for p in pf["positions"])
        total_pnl      = total_value - total_cost
        annual_yield   = sum(p["value_usd"] * p["apy"] for p in pf["positions"])
        return {
            "name":          pf["name"],
            "positions":     len(pf["positions"]),
            "total_value":   f"${total_value:,.2f}",
            "total_cost":    f"${total_cost:,.2f}",
            "unrealized_pnl": f"${total_pnl:+,.2f}",
            "pnl_pct":       f"{total_pnl/max(0.01,total_cost)*100:+.2f}%",
            "annual_yield":  f"${annual_yield:,.2f}",
            "blended_apy":   f"{annual_yield/max(0.01,total_value)*100:.2f}%",
        }

    def tracker_stats(self) -> dict:
        return {
            "portfolios": len(self._portfolios),
            "snapshots":  len(self._snapshots),
        }


# ---- HardwareWalletSimulator
class HardwareWalletSimulator:
    """Simulates hardware wallet signing (for testing)."""

    def __init__(self, seed: bytes):
        self._master = HDKey.from_seed(seed)
        self._signed: list = []

    def sign_transaction(self, tx_hash: str,
                          derivation_path: str) -> dict:
        """Sign a transaction hash using the hardware wallet."""
        node     = self._master.derive_path(derivation_path)
        # Simulate signing
        sig_hash = hashlib.sha256(
            bytes.fromhex(tx_hash) + node.private_key.to_bytes(32, 'big')
        ).hexdigest()
        self._signed.append({
            "tx_hash":  tx_hash,
            "path":     derivation_path,
            "sig":      sig_hash,
            "ts":       time.time(),
        })
        return {
            "signed":    True,
            "signature": sig_hash,
            "device":    "NEBULA HW Simulator",
            "path":      derivation_path,
        }

    def get_public_key(self, path: str) -> str:
        node = self._master.derive_path(path)
        return node.public_key.hex() if hasattr(node.public_key, 'hex') else str(node.public_key)

    def hw_stats(self) -> dict:
        return {"signed_txs": len(self._signed)}


# ---- NEBULAMemoryPool
class NEBULAMemoryPool:
    """Advanced mempool with RBF, CPFP, and fee bumping."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._pool:   dict = {}
        self._rbf:    dict = {}   # txid -> replacement txid
        self._lock    = threading.RLock()

    def submit_tx(self, tx: 'Transaction', fee_rate: int,
                   utxo: 'UTXOSet') -> Tuple[bool, str]:
        with self._lock:
            if tx.txid in self._pool:
                return False, "Already in mempool"
            self._pool[tx.txid] = {
                "tx":       tx,
                "fee_rate": fee_rate,
                "added":    self._bc.height,
            }
            return True, "Accepted"

    def rbf_replace(self, old_txid: str, new_tx: 'Transaction',
                     new_fee_rate: int, utxo: 'UTXOSet') -> Tuple[bool, str]:
        with self._lock:
            old = self._pool.get(old_txid)
            if not old:
                return False, "Original tx not found"
            if new_fee_rate <= old["fee_rate"] * 1.10:
                return False, "New fee must be ≥110% of original"
            del self._pool[old_txid]
            self._pool[new_tx.txid] = {
                "tx": new_tx, "fee_rate": new_fee_rate,
                "added": self._bc.height,
            }
            self._rbf[old_txid] = new_tx.txid
            return True, f"Replaced {old_txid[:8]} with {new_tx.txid[:8]}"

    def select_for_block(self, max_size: int = 1_000_000) -> list:
        with self._lock:
            sorted_txs = sorted(
                self._pool.values(),
                key=lambda x: -x["fee_rate"]
            )
        selected = []
        size     = 0
        for entry in sorted_txs:
            tx_size = entry["tx"].byte_size()
            if size + tx_size <= max_size:
                selected.append(entry["tx"])
                size += tx_size
        return selected

    def mempool_stats(self) -> dict:
        with self._lock:
            total_fees = sum(e["fee_rate"] * e["tx"].byte_size()
                             for e in self._pool.values())
        return {
            "size":        len(self._pool),
            "total_fees":  f"{total_fees/10**DECIMALS:.6f}",
            "rbf_count":   len(self._rbf),
        }
