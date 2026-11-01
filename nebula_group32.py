"""NEBULA group32 - 20 dead classes, extracted VERBATIM from nebula_v10_11.py (original order).

Classes:
   1. MultisigVault  (orig. lines 54288-54313)
   2. MultisigVaultManager  (orig. lines 54315-54439)
   3. AuditSeverity  (orig. lines 54449-54453)
   4. AuditEvent  (orig. lines 54455-54477)
   5. AuditLogger  (orig. lines 54479-54619)
   6. MicroPaymentNetwork  (orig. lines 54634-54764)
   7. VMError  (orig. lines 54775-54776)
   8. VMGasExhausted  (orig. lines 54778-54779)
   9. GasCosts  (orig. lines 54781-54794)
  10. VMState  (orig. lines 54796-54804)
  11. NEBULASmartContractVM  (orig. lines 54806-55046)
  12. DeFiRouter  (orig. lines 55086-55200)
  13. Subscription  (orig. lines 55214-55237)
  14. SubscriptionProtocol  (orig. lines 55239-55297)
  15. EscrowContract  (orig. lines 55307-55330)
  16. EscrowService  (orig. lines 55332-55416)
  17. SocialProfile  (orig. lines 55426-55449)
  18. SocialPost  (orig. lines 55451-55471)
  19. NEBULASocial  (orig. lines 55473-55610)
  20. InsurancePolicy  (orig. lines 55620-55643)

Helpers/constants copied from the host (module-level) are in the section below the imports.
Depends on classes of OTHER groups (not copied here): ChannelUpdate, DecentralizedOracle, MicroChannel, MicroChannelUpdate, NEBULADex, PaymentChannel
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

_routes: Dict[str, Dict[str, Callable]] = {}

def route(path: str, methods: List[str] = None):
    """Decorator to register an API endpoint."""
    def decorator(fn: Callable) -> Callable:
        for method in (methods or ["GET"]):
            _routes.setdefault(method.upper(), {})[path] = fn
        return fn
    return decorator

MAX_STACK_DEPTH     = 1024

# ===== optional: other host classes (only needed for cross-group references; own definitions below override) =====
try:
    import nebula_v10_11 as _host
    for _k, _v in vars(_host).items():
        if not _k.startswith("__") and _k not in globals():
            globals()[_k] = _v
except Exception:
    _NB_SWALLOW_LOG.debug("swallowed Exception in <module>", exc_info=True)

# ===== the 20 classes =====


# ---- MultisigVault
@dataclass
class MultisigVault:
    """
    Advanced multi-signature vault.
    Time-locked, with rotating signers and spending limits.
    """
    vault_id:       str
    owners:         List[str]       # NBL addresses
    required:       int             # m of n
    spending_limit: int             # max per-tx without full approval
    timelock:       int             # blocks delay for large txs
    created_at:     float
    balance:        int = 0
    pending_txs:    List[dict] = field(default_factory=list)
    nonce:          int = 0

    def to_dict(self) -> dict:
        return {
            "vault_id":       self.vault_id,
            "owners":         self.owners,
            "required":       f"{self.required}/{len(self.owners)}",
            "spending_limit_nbl": f"{self.spending_limit/10**DECIMALS:.3f}",
            "timelock_blocks": self.timelock,
            "balance_nbl":    f"{self.balance/10**DECIMALS:.9f}",
            "pending_txs":    len(self.pending_txs),
        }


# ---- MultisigVaultManager
class MultisigVaultManager:
    """Manages multiple multisig vaults for teams and DAOs."""

    def __init__(self):
        self._vaults:  Dict[str, MultisigVault]   = {}
        self._pending: Dict[str, dict]             = {}  # proposal -> sigs
        self._lock     = threading.RLock()

    def create_vault(self, owners: List[str], required: int,
                      spending_limit_nbl: float = 1000,
                      timelock: int = 144) -> str:
        """Create a new multisig vault."""
        with self._lock:
            if required > len(owners) or required < 1:
                raise ValueError(f"Invalid m-of-n: {required}/{len(owners)}")
            vid = hashlib.sha256(
                f"VAULT:{''.join(sorted(owners))}:{required}:{time.time()}".encode()
            ).hexdigest()[:20]
            self._vaults[vid] = MultisigVault(
                vault_id       = vid,
                owners         = owners,
                required       = required,
                spending_limit = int(spending_limit_nbl * 10**DECIMALS),
                timelock       = timelock,
                created_at     = time.time(),
            )
            return vid

    def propose_transaction(self, vault_id: str, proposer: str,
                             to: str, amount: int,
                             note: str = "") -> Tuple[bool, str]:
        """Propose a transaction from a vault."""
        with self._lock:
            vault = self._vaults.get(vault_id)
            if not vault:
                return False, "Vault not found"
            if proposer not in vault.owners:
                return False, "Not a vault owner"
            if amount > vault.balance:
                return False, f"Insufficient balance: {vault.balance}"

            pid = hashlib.sha256(
                f"{vault_id}{to}{amount}{vault.nonce}{time.time()}".encode()
            ).hexdigest()[:16]
            vault.nonce += 1

            proposal = {
                "proposal_id": pid,
                "vault_id":    vault_id,
                "to":          to,
                "amount":      amount,
                "note":        note,
                "proposer":    proposer,
                "signatures":  {proposer: True},   # proposer auto-signs
                "status":      "pending",
                "created_at":  time.time(),
                "needs_timelock": amount > vault.spending_limit,
                "execute_after":  0,
            }
            self._pending[pid] = proposal
            vault.pending_txs.append(pid)
            return True, pid

    def sign(self, proposal_id: str, signer: str) -> Tuple[bool, str]:
        """Sign a pending proposal."""
        with self._lock:
            p = self._pending.get(proposal_id)
            if not p:
                return False, "Not found"
            vault = self._vaults.get(p["vault_id"])
            if signer not in vault.owners:
                return False, "Not an owner"
            if signer in p["signatures"]:
                return False, "Already signed"
            p["signatures"][signer] = True

            if len(p["signatures"]) >= vault.required:
                if p["needs_timelock"] and p["execute_after"] == 0:
                    p["execute_after"] = int(time.time()) + vault.timelock * 600
                    p["status"] = "timelock"
                    return True, f"Approved — timelock until block +{vault.timelock}"
                p["status"] = "approved"
            return True, f"Signed ({len(p['signatures'])}/{vault.required})"

    def execute(self, proposal_id: str,
                 executor: str) -> Tuple[bool, str]:
        """Execute an approved proposal."""
        with self._lock:
            p = self._pending.get(proposal_id)
            if not p:
                return False, "Not found"
            vault = self._vaults.get(p["vault_id"])
            if executor not in vault.owners:
                return False, "Not owner"
            if p["status"] not in ("approved", "timelock"):
                return False, f"Not approved: {p['status']}"
            if p["status"] == "timelock":
                if time.time() < p["execute_after"]:
                    remaining = p["execute_after"] - time.time()
                    return False, f"Timelock active: {remaining:.0f}s remaining"
            if len(p["signatures"]) < vault.required:
                return False, f"Need {vault.required} sigs, have {len(p['signatures'])}"

            vault.balance -= p["amount"]
            p["status"]    = "executed"
            vault.pending_txs = [x for x in vault.pending_txs
                                  if x != proposal_id]
            return True, (f"Executed: sent {p['amount']/10**DECIMALS:.3f} NBL "
                          f"to {p['to']}")

    def deposit(self, vault_id: str, amount: int) -> Tuple[bool, str]:
        with self._lock:
            vault = self._vaults.get(vault_id)
            if not vault:
                return False, "Not found"
            vault.balance += amount
            return True, f"Deposited {amount/10**DECIMALS:.3f} NBL"

    def vault_info(self, vault_id: str) -> Optional[dict]:
        v = self._vaults.get(vault_id)
        return v.to_dict() if v else None

    def pending_proposals(self, vault_id: str) -> List[dict]:
        return [p for p in self._pending.values()
                if p["vault_id"] == vault_id and p["status"] != "executed"]


# ---- AuditSeverity
class AuditSeverity(_enum.Enum):
    INFO     = "INFO"
    WARNING  = "WARNING"
    CRITICAL = "CRITICAL"
    ALERT    = "ALERT"


# ---- AuditEvent
@dataclass
class AuditEvent:
    event_id:   str
    timestamp:  float
    severity:   AuditSeverity
    category:   str
    actor:      str
    action:     str
    details:    dict
    block_height: int
    tx_hash:    str = ""

    def to_dict(self) -> dict:
        return {
            "event_id":    self.event_id,
            "timestamp":   self.timestamp,
            "severity":    self.severity.value,
            "category":    self.category,
            "actor":       self.actor,
            "action":      self.action,
            "details":     self.details,
            "block_height": self.block_height,
        }


# ---- AuditLogger
class AuditLogger:
    """
    Immutable audit log for NEBULA.
    All events are hash-chained to prevent tampering.
    """

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc      = blockchain
        self._events: List[AuditEvent] = []
        self._chain_hash = "0" * 64
        self._lock    = threading.RLock()
        self._alerts: List[dict] = []
        self._rules:  List[dict] = []
        self._setup_default_rules()

    def _setup_default_rules(self):
        """Default anomaly detection rules."""
        self._rules = [
            {
                "name": "large_transfer",
                "condition": lambda e: (
                    e.category == "transaction" and
                    e.details.get("amount", 0) > 100_000 * 10**DECIMALS
                ),
                "severity": AuditSeverity.ALERT,
                "message": "Large transfer detected",
            },
            {
                "name": "rapid_tx",
                "condition": lambda e: (
                    e.category == "transaction" and
                    e.details.get("count_1min", 0) > 100
                ),
                "severity": AuditSeverity.WARNING,
                "message": "Rapid transaction rate",
            },
            {
                "name": "governance_vote",
                "condition": lambda e: e.category == "governance",
                "severity": AuditSeverity.INFO,
                "message": "Governance action recorded",
            },
            {
                "name": "slash_event",
                "condition": lambda e: e.category == "staking" and "slash" in e.action,
                "severity": AuditSeverity.CRITICAL,
                "message": "Validator slashed",
            },
        ]

    def log(self, severity: AuditSeverity, category: str,
            actor: str, action: str,
            details: dict = None, tx_hash: str = "") -> str:
        """Record an audit event."""
        with self._lock:
            eid = hashlib.sha256(
                f"{self._chain_hash}{time.time()}{actor}{action}".encode()
            ).hexdigest()[:16]

            event = AuditEvent(
                event_id     = eid,
                timestamp    = time.time(),
                severity     = severity,
                category     = category,
                actor        = actor,
                action       = action,
                details      = details or {},
                block_height = self._bc.height,
                tx_hash      = tx_hash,
            )

            # Chain hash for integrity
            self._chain_hash = hashlib.sha256(
                f"{self._chain_hash}{eid}".encode()
            ).hexdigest()

            self._events.append(event)
            self._check_rules(event)
            return eid

    def _check_rules(self, event: AuditEvent):
        """Check anomaly detection rules."""
        for rule in self._rules:
            try:
                if rule["condition"](event):
                    alert = {
                        "alert_id":  secrets.token_hex(8),
                        "rule":      rule["name"],
                        "severity":  rule["severity"].value,
                        "message":   rule["message"],
                        "event_id":  event.event_id,
                        "timestamp": time.time(),
                    }
                    self._alerts.append(alert)
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in AuditLogger._check_rules", exc_info=True)

    def query(self, category: str = None, actor: str = None,
               severity: str = None, limit: int = 100) -> List[dict]:
        """Query audit log."""
        with self._lock:
            events = list(self._events)
        if category:
            events = [e for e in events if e.category == category]
        if actor:
            events = [e for e in events if e.actor == actor]
        if severity:
            events = [e for e in events if e.severity.value == severity]
        return [e.to_dict() for e in events[-limit:]]

    def verify_integrity(self) -> Tuple[bool, str]:
        """Verify audit log has not been tampered with."""
        with self._lock:
            events = list(self._events)
        chain = "0" * 64
        for e in events:
            chain = hashlib.sha256(f"{chain}{e.event_id}".encode()).hexdigest()
        if chain == self._chain_hash:
            return True, f"Integrity verified ({len(events)} events)"
        return False, "INTEGRITY VIOLATION: audit log has been tampered"

    def compliance_report(self, days: int = 30) -> dict:
        cutoff = time.time() - days * 86400
        with self._lock:
            recent = [e for e in self._events if e.timestamp >= cutoff]
        by_severity = {}
        by_category = {}
        for e in recent:
            by_severity[e.severity.value] = by_severity.get(e.severity.value, 0) + 1
            by_category[e.category]       = by_category.get(e.category, 0) + 1
        return {
            "period_days":   days,
            "total_events":  len(recent),
            "by_severity":   by_severity,
            "by_category":   by_category,
            "alerts_raised": len(self._alerts),
            "integrity":     self.verify_integrity()[1],
        }

    def active_alerts(self) -> List[dict]:
        return list(self._alerts[-50:])


# ---- MicroPaymentNetwork
@dataclass
@dataclass
class MicroPaymentNetwork:
    """
    NEBULA off-chain micropayment network.
    Inspired by Lightning Network.
    """

    CHANNEL_RESERVE = 1_000   # minimum balance each side must keep

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._channels: Dict[str, PaymentChannel]     = {}
        self._updates:  Dict[str, List[ChannelUpdate]] = {}
        self._lock      = threading.RLock()
        self._routing_table: Dict[str, List[str]]     = {}

    def open_channel(self, party_a: str, party_b: str,
                      amount_a: int,
                      amount_b: int = 0) -> Tuple[bool, str]:
        """Open a payment channel between two parties."""
        with self._lock:
            capacity = amount_a + amount_b
            if capacity < self.CHANNEL_RESERVE * 2:
                return False, f"Minimum capacity: {self.CHANNEL_RESERVE*2} Neb"
            cid = hashlib.sha256(
                f"CH:{party_a}:{party_b}:{time.time()}".encode()
            ).hexdigest()[:16]
            ch = MicroChannel(
                channel_id  = cid,
                party_a     = party_a,
                party_b     = party_b,
                capacity    = capacity,
                balance_a   = amount_a,
                balance_b   = amount_b,
                opened_at   = time.time(),
            )
            self._channels[cid]  = ch
            self._updates[cid]   = []
            self._update_routing(party_a, party_b, cid)
            return True, cid

    def _update_routing(self, a: str, b: str, cid: str):
        if a not in self._routing_table:
            self._routing_table[a] = []
        if b not in self._routing_table:
            self._routing_table[b] = []
        if cid not in self._routing_table[a]:
            self._routing_table[a].append(cid)
        if cid not in self._routing_table[b]:
            self._routing_table[b].append(cid)

    def pay(self, channel_id: str, from_party: str,
             amount: int) -> Tuple[bool, str]:
        """Make an instant off-chain payment."""
        with self._lock:
            ch = self._channels.get(channel_id)
            if not ch or ch.state != "open":
                return False, "Channel not found or not open"

            if from_party == ch.party_a:
                if ch.balance_a - amount < self.CHANNEL_RESERVE:
                    return False, f"Insufficient balance (need reserve {self.CHANNEL_RESERVE})"
                ch.balance_a -= amount
                ch.balance_b += amount
            elif from_party == ch.party_b:
                if ch.balance_b - amount < self.CHANNEL_RESERVE:
                    return False, "Insufficient balance"
                ch.balance_b -= amount
                ch.balance_a += amount
            else:
                return False, "Not a channel participant"

            ch.sequence      += 1
            ch.total_payments += 1
            ch.total_volume  += amount

            update = MicroChannelUpdate(
                channel_id = channel_id,
                sequence   = ch.sequence,
                balance_a  = ch.balance_a,
                balance_b  = ch.balance_b,
            )
            self._updates[channel_id].append(update)
            return True, (f"Payment: {amount/10**DECIMALS:.9f} NBL | "
                          f"seq={ch.sequence}")

    def cooperative_close(self, channel_id: str) -> Tuple[bool, str]:
        """Both parties agree to close the channel."""
        with self._lock:
            ch = self._channels.get(channel_id)
            if not ch or ch.state != "open":
                return False, "Not found or not open"
            ch.state     = "closed"
            ch.closed_at = time.time()
            return True, (f"Channel closed. Final balances: "
                          f"A={ch.balance_a/10**DECIMALS:.9f} NBL, "
                          f"B={ch.balance_b/10**DECIMALS:.9f} NBL")

    def find_route(self, from_addr: str,
                    to_addr: str) -> Optional[List[str]]:
        """Simple BFS route finding through channel network."""
        visited = {from_addr}
        queue   = [(from_addr, [from_addr])]
        while queue:
            current, path = queue.pop(0)
            for cid in self._routing_table.get(current, []):
                ch = self._channels.get(cid)
                if not ch or ch.state != "open":
                    continue
                next_addr = ch.party_b if ch.party_a == current else ch.party_a
                if next_addr == to_addr:
                    return path + [next_addr]
                if next_addr not in visited:
                    visited.add(next_addr)
                    queue.append((next_addr, path + [next_addr]))
        return None

    def channel_stats(self) -> dict:
        with self._lock:
            total    = len(self._channels)
            open_ch  = sum(1 for c in self._channels.values() if c.state == "open")
            total_cap = sum(c.capacity for c in self._channels.values() if c.state == "open")
            total_pay = sum(c.total_payments for c in self._channels.values())
        return {
            "total_channels":   total,
            "open_channels":    open_ch,
            "total_capacity_nbl": f"{total_cap/10**DECIMALS:.3f}",
            "total_payments":   total_pay,
            "network_nodes":    len(self._routing_table),
        }


# ---- VMError
class VMError(Exception):
    pass


# ---- VMGasExhausted
class VMGasExhausted(VMError):
    pass


# ---- GasCosts
class GasCosts:
    """Gas costs for VM operations."""
    BASE          = 1
    STORAGE_READ  = 200
    STORAGE_WRITE = 5000
    SHA256        = 60
    SIGNATURE     = 3000
    CALL          = 700
    LOG           = 375
    PUSH          = 3
    ARITHMETIC    = 5
    COMPARISON    = 3
    JUMP          = 8
    MEMORY        = 3


# ---- VMState
@dataclass
class VMState:
    """Snapshot of VM state for debugging/rollback."""
    stack:    List
    memory:   Dict
    storage:  Dict
    gas_used: int
    pc:       int
    events:   List


# ---- NEBULASmartContractVM
class NEBULASmartContractVM:
    """
    NEBULA Smart Contract Virtual Machine.
    Stack-based, similar to EVM but simpler and safer.
    Full gas metering, deterministic execution.
    """

    MAX_STACK_DEPTH  = 1024
    MAX_MEMORY_ITEMS = 4096
    MAX_CALL_DEPTH   = 16

    def __init__(self, gas_limit: int = 1_000_000):
        self.gas_limit   = gas_limit
        self.gas_used    = 0
        self._halted     = False
        self.stack:      List[Any]        = []
        self.memory:     Dict[str, Any]   = {}
        self.storage:    Dict[str, Any]   = {}
        self.events:     List[dict]       = []
        self.call_depth  = 0
        self.pc          = 0
        self.returndata: Any = None
        self._snapshots: List[VMState]    = []

    def _gas(self, cost: int):
        self.gas_used += cost
        if self.gas_used > self.gas_limit:
            raise VMGasExhausted(f"Gas limit {self.gas_limit} exceeded")

    def _push(self, value: Any):
        if len(self.stack) >= self.MAX_STACK_DEPTH:
            raise VMError("Stack overflow")
        self._gas(GasCosts.PUSH)
        self.stack.append(value)

    def _pop(self) -> Any:
        if not self.stack:
            raise VMError("Stack underflow")
        return self.stack.pop()

    def snapshot(self) -> VMState:
        return VMState(
            stack   = list(self.stack),
            memory  = dict(self.memory),
            storage = dict(self.storage),
            gas_used = self.gas_used,
            pc      = self.pc,
            events  = list(self.events),
        )

    def restore(self, snap: VMState):
        self.stack    = snap.stack
        self.memory   = snap.memory
        self.storage  = snap.storage
        self.gas_used = snap.gas_used
        self.pc       = snap.pc
        self.events   = snap.events

    def execute_bytecode(self, bytecode: List[Tuple[str, Any]],
                          context: dict = None) -> Any:
        """
        Execute VM bytecode.
        bytecode = list of (opcode, operand) tuples.
        context = {"caller", "value", "block_height", "timestamp"}
        """
        ctx = context or {}
        self.pc = 0

        self._halted = False
        while self.pc < len(bytecode) and not self._halted:
            op, operand = bytecode[self.pc]
            self.pc += 1
            self._gas(GasCosts.BASE)
            self._exec_op(op, operand, ctx)

        return self.returndata

    def _exec_op(self, op: str, operand: Any, ctx: dict):
        """Execute a single VM instruction."""

        if op == "PUSH":
            self._push(operand)

        elif op == "POP":
            self._pop()

        elif op == "DUP":
            v = self._pop(); self._push(v); self._push(v)

        elif op == "SWAP":
            a = self._pop(); b = self._pop()
            self._push(a); self._push(b)

        elif op == "ADD":
            self._gas(GasCosts.ARITHMETIC)
            b = self._pop(); a = self._pop()
            self._push(a + b)

        elif op == "SUB":
            self._gas(GasCosts.ARITHMETIC)
            b = self._pop(); a = self._pop()
            self._push(a - b)

        elif op == "MUL":
            self._gas(GasCosts.ARITHMETIC)
            b = self._pop(); a = self._pop()
            self._push(a * b)

        elif op == "DIV":
            self._gas(GasCosts.ARITHMETIC)
            b = self._pop(); a = self._pop()
            if b == 0:
                raise VMError("Division by zero")
            self._push(a // b)

        elif op == "MOD":
            self._gas(GasCosts.ARITHMETIC)
            b = self._pop(); a = self._pop()
            if b == 0:
                raise VMError("Modulo by zero")
            self._push(a % b)

        elif op == "EQ":
            self._gas(GasCosts.COMPARISON)
            b = self._pop(); a = self._pop()
            self._push(1 if a == b else 0)

        elif op == "LT":
            self._gas(GasCosts.COMPARISON)
            b = self._pop(); a = self._pop()
            self._push(1 if a < b else 0)

        elif op == "GT":
            self._gas(GasCosts.COMPARISON)
            b = self._pop(); a = self._pop()
            self._push(1 if a > b else 0)

        elif op == "AND":
            b = self._pop(); a = self._pop()
            self._push(a & b)

        elif op == "OR":
            b = self._pop(); a = self._pop()
            self._push(a | b)

        elif op == "NOT":
            a = self._pop()
            self._push(1 if a == 0 else 0)

        elif op == "JUMP":
            self.pc = self._pop()
            self._gas(GasCosts.JUMP)

        elif op == "JUMPI":
            self._gas(GasCosts.JUMP)
            cond = self._pop(); dest = self._pop()
            if cond != 0:
                self.pc = dest

        elif op == "MLOAD":
            self._gas(GasCosts.STORAGE_READ)
            key = self._pop()
            self._push(self.memory.get(str(key), 0))

        elif op == "MSTORE":
            self._gas(GasCosts.STORAGE_WRITE)
            if len(self.memory) >= self.MAX_MEMORY_ITEMS:
                raise VMError("Memory limit reached")
            val = self._pop(); key = self._pop()
            self.memory[str(key)] = val

        elif op == "SLOAD":
            self._gas(GasCosts.STORAGE_READ)
            key = self._pop()
            self._push(self.storage.get(str(key), 0))

        elif op == "SSTORE":
            self._gas(GasCosts.STORAGE_WRITE)
            val = self._pop(); key = self._pop()
            self.storage[str(key)] = val

        elif op == "CALLER":
            self._push(ctx.get("caller", ""))

        elif op == "VALUE":
            self._push(ctx.get("value", 0))

        elif op == "HEIGHT":
            self._push(ctx.get("block_height", 0))

        elif op == "TIMESTAMP":
            self._push(ctx.get("timestamp", int(time.time())))

        elif op == "SHA256":
            self._gas(GasCosts.SHA256)
            data = self._pop()
            if isinstance(data, str):
                data = data.encode()
            elif isinstance(data, int):
                data = data.to_bytes(32, 'big')
            self._push(hashlib.sha256(data).hexdigest())

        elif op == "LOG":
            self._gas(GasCosts.LOG)
            data  = self._pop()
            topic = self._pop()
            self.events.append({
                "topic":   topic,
                "data":    data,
                "pc":      self.pc,
                "height":  ctx.get("block_height", 0),
            })

        elif op == "RETURN":
            self.returndata = self._pop()
            self._halted = True   # cleanly stop execution loop

        elif op == "REVERT":
            msg = self._pop()
            raise VMError(f"Contract reverted: {msg}")

        elif op == "ASSERT":
            cond = self._pop()
            if not cond:
                raise VMError("Assertion failed")

        elif op == "NOP":
            pass

        else:
            raise VMError(f"Unknown opcode: {op}")

    def gas_report(self) -> dict:
        remaining = self.gas_limit - self.gas_used
        return {
            "gas_limit":   self.gas_limit,
            "gas_used":    self.gas_used,
            "gas_remaining": remaining,
            "pct_used":    f"{self.gas_used/self.gas_limit*100:.2f}%",
            "events_emitted": len(self.events),
        }


# ---- DeFiRouter
class DeFiRouter:
    """
    NEBULA DeFi aggregator router.
    Finds the best swap route across all AMM pools and order books.
    """

    MAX_HOPS     = 3
    DEFAULT_SLIPPAGE = 0.005    # 0.5%

    def __init__(self, dex: NEBULADex,
                 oracle: DecentralizedOracle = None):
        self._dex    = dex
        self._oracle = oracle

    def get_best_quote(self, token_in: str, token_out: str,
                        amount_in: int) -> dict:
        """Find best swap quote across all routes."""
        direct = self._quote_direct(token_in, token_out, amount_in)
        results = [direct] if direct["amount_out"] > 0 else []

        # Try multi-hop routes (up to 3 hops)
        intermediates = self._find_intermediates(token_in, token_out)
        for mid in intermediates:
            hop1 = self._quote_direct(token_in, mid, amount_in)
            if hop1["amount_out"] > 0:
                hop2 = self._quote_direct(mid, token_out, hop1["amount_out"])
                if hop2["amount_out"] > 0:
                    results.append({
                        "route":       [token_in, mid, token_out],
                        "amount_out":  hop2["amount_out"],
                        "hops":        2,
                        "price_impact": max(hop1.get("price_impact", 0),
                                           hop2.get("price_impact", 0)),
                    })

        if not results:
            return {"route": [], "amount_out": 0, "error": "No liquidity"}

        best = max(results, key=lambda r: r["amount_out"])
        best["min_out_with_slippage"] = int(
            best["amount_out"] * (1 - self.DEFAULT_SLIPPAGE))
        return best

    def _quote_direct(self, token_in: str, token_out: str,
                       amount_in: int) -> dict:
        pid      = self._dex._pair_id(token_in, token_out)
        rev_pid  = self._dex._pair_id(token_out, token_in)
        amm      = self._dex._amms.get(pid) or self._dex._amms.get(rev_pid)
        if not amm:
            return {"route": [token_in, token_out], "amount_out": 0}
        is_a_to_b = pid in self._dex._amms
        out       = amm.get_amount_out(amount_in, is_a_to_b)
        impact    = amm.price_impact(amount_in, is_a_to_b)
        return {
            "route":        [token_in, token_out],
            "amount_out":   out,
            "hops":         1,
            "price_impact": impact,
        }

    def _find_intermediates(self, from_: str, to_: str) -> List[str]:
        """Find tokens that could serve as intermediaries."""
        intermediates = set()
        for pid in self._dex._pools:
            parts = pid.split(":")
            if len(parts) == 2:
                a, b = parts
                if a in (from_, to_) or b in (from_, to_):
                    intermediates.add(a)
                    intermediates.add(b)
        intermediates.discard(from_)
        intermediates.discard(to_)
        return list(intermediates)[:5]

    def execute_swap(self, trader: str, token_in: str,
                     token_out: str, amount_in: int,
                     max_slippage: float = None) -> Tuple[bool, str, int]:
        """Execute swap using best route."""
        slippage = max_slippage or self.DEFAULT_SLIPPAGE
        quote    = self.get_best_quote(token_in, token_out, amount_in)

        if quote.get("amount_out", 0) == 0:
            return False, "No liquidity found", 0

        if quote.get("price_impact", 0) > 0.15:
            return False, f"Price impact too high: {quote['price_impact']*100:.1f}%", 0

        min_out = int(quote["amount_out"] * (1 - slippage))
        route   = quote.get("route", [token_in, token_out])

        if len(route) == 2:
            return self._dex.swap_amm(trader, token_in, token_out,
                                       amount_in, min_out)
        elif len(route) == 3:
            # Multi-hop
            ok1, msg1, mid_out = self._dex.swap_amm(
                trader, route[0], route[1], amount_in, 0)
            if not ok1:
                return False, f"Hop 1 failed: {msg1}", 0
            ok2, msg2, final_out = self._dex.swap_amm(
                trader, route[1], route[2], mid_out, min_out)
            if not ok2:
                return False, f"Hop 2 failed: {msg2}", 0
            return True, f"Multi-hop swap via {route[1]}", final_out

        return False, "Invalid route", 0

    def router_stats(self) -> dict:
        pools = self._dex.list_pools()
        return {
            "available_pools": len(pools),
            "max_hops":        self.MAX_HOPS,
            "default_slippage": f"{self.DEFAULT_SLIPPAGE*100:.1f}%",
            "pools":           pools,
        }


# ---- Subscription
@dataclass
class Subscription:
    sub_id:        str
    subscriber:    str
    provider:      str
    amount_per_period: int
    period_blocks: int    # e.g. 4320 = ~30 days
    next_payment:  int    # block height
    active:        bool = True
    total_paid:    int  = 0
    payments_made: int  = 0

    def to_dict(self) -> dict:
        return {
            "sub_id":        self.sub_id,
            "subscriber":    self.subscriber,
            "provider":      self.provider,
            "amount_nbl":    f"{self.amount_per_period/10**DECIMALS:.9f}",
            "period_blocks": self.period_blocks,
            "next_payment":  self.next_payment,
            "active":        self.active,
            "total_paid_nbl": f"{self.total_paid/10**DECIMALS:.9f}",
            "payments_made": self.payments_made,
        }


# ---- SubscriptionProtocol
class SubscriptionProtocol:
    """Recurring payment subscriptions on NEBULA."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc   = blockchain
        self._subs: Dict[str, Subscription] = {}
        self._lock = threading.RLock()

    def subscribe(self, subscriber: str, provider: str,
                  amount_nbl: float, period_days: int = 30) -> Tuple[bool, str]:
        period_blocks = int(period_days * 24 * 6)   # 6 blocks/hour
        amount        = int(amount_nbl * 10**DECIMALS)
        with self._lock:
            sid = hashlib.sha256(
                f"SUB:{subscriber}:{provider}:{time.time()}".encode()
            ).hexdigest()[:16]
            sub = Subscription(
                sub_id             = sid,
                subscriber         = subscriber,
                provider           = provider,
                amount_per_period  = amount,
                period_blocks      = period_blocks,
                next_payment       = self._bc.height + period_blocks,
            )
            self._subs[sid] = sub
            return True, sid

    def cancel(self, sub_id: str, caller: str) -> Tuple[bool, str]:
        with self._lock:
            sub = self._subs.get(sub_id)
            if not sub or sub.subscriber != caller:
                return False, "Not found or not subscriber"
            sub.active = False
            return True, f"Subscription {sub_id} cancelled"

    def process_due(self) -> List[str]:
        """Process all subscriptions due at current height."""
        cur = self._bc.height
        processed = []
        with self._lock:
            for sid, sub in self._subs.items():
                if not sub.active or cur < sub.next_payment:
                    continue
                bal = self._bc.utxo.balance(sub.subscriber)
                if bal >= sub.amount_per_period:
                    sub.total_paid    += sub.amount_per_period
                    sub.payments_made += 1
                    sub.next_payment  += sub.period_blocks
                    processed.append(sid)
                else:
                    sub.active = False   # auto-cancel on insufficient funds
        return processed

    def subscriptions_for(self, address: str,
                           as_subscriber: bool = True) -> List[dict]:
        with self._lock:
            subs = [s for s in self._subs.values()
                    if (s.subscriber if as_subscriber else s.provider) == address]
        return [s.to_dict() for s in subs]


# ---- EscrowContract
@dataclass
class EscrowContract:
    escrow_id:   str
    buyer:       str
    seller:      str
    arbiter:     str       # optional dispute resolver
    amount:      int
    description: str
    state:       str = "funded"    # funded/released/disputed/refunded/resolved
    funded_at:   float = 0.0
    deadline:    int = 0           # block height
    dispute_reason: str = ""

    def to_dict(self) -> dict:
        return {
            "escrow_id":    self.escrow_id,
            "buyer":        self.buyer,
            "seller":       self.seller,
            "arbiter":      self.arbiter,
            "amount_nbl":   f"{self.amount/10**DECIMALS:.9f}",
            "description":  self.description,
            "state":        self.state,
            "deadline":     self.deadline,
        }


# ---- EscrowService
class EscrowService:
    """Trustless escrow for NEBULA transactions."""

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc       = blockchain
        self._escrows: Dict[str, EscrowContract] = {}
        self._lock     = threading.RLock()

    def create(self, buyer: str, seller: str, amount_nbl: float,
               description: str, arbiter: str = "",
               deadline_days: int = 30) -> Tuple[bool, str]:
        with self._lock:
            amount   = int(amount_nbl * 10**DECIMALS)
            deadline = self._bc.height + deadline_days * 144
            eid = hashlib.sha256(
                f"ESC:{buyer}:{seller}:{amount}:{time.time()}".encode()
            ).hexdigest()[:16]
            esc = EscrowContract(
                escrow_id   = eid,
                buyer       = buyer,
                seller      = seller,
                arbiter     = arbiter,
                amount      = amount,
                description = description,
                funded_at   = time.time(),
                deadline    = deadline,
            )
            self._escrows[eid] = esc
            return True, eid

    def release(self, escrow_id: str, caller: str) -> Tuple[bool, str]:
        """Buyer releases payment to seller."""
        with self._lock:
            esc = self._escrows.get(escrow_id)
            if not esc or esc.state != "funded":
                return False, "Not found or wrong state"
            if caller != esc.buyer:
                return False, "Only buyer can release"
            esc.state = "released"
            return True, f"Released {esc.amount/10**DECIMALS:.3f} NBL to {esc.seller}"

    def dispute(self, escrow_id: str, caller: str,
                reason: str) -> Tuple[bool, str]:
        """Raise a dispute."""
        with self._lock:
            esc = self._escrows.get(escrow_id)
            if not esc or esc.state != "funded":
                return False, "Cannot dispute"
            if caller not in (esc.buyer, esc.seller):
                return False, "Not a party"
            esc.state          = "disputed"
            esc.dispute_reason = reason
            return True, f"Dispute raised. Arbiter: {esc.arbiter or 'none'}"

    def resolve(self, escrow_id: str, arbiter: str,
                release_to: str) -> Tuple[bool, str]:
        """Arbiter resolves dispute."""
        with self._lock:
            esc = self._escrows.get(escrow_id)
            if not esc or esc.state != "disputed":
                return False, "Not in dispute"
            if arbiter != esc.arbiter:
                return False, "Not the arbiter"
            if release_to not in (esc.buyer, esc.seller):
                return False, "Invalid recipient"
            esc.state = "resolved"
            return True, (f"Resolved: {esc.amount/10**DECIMALS:.3f} NBL "
                          f"released to {release_to}")

    def refund(self, escrow_id: str, caller: str) -> Tuple[bool, str]:
        """Refund to buyer after deadline."""
        with self._lock:
            esc = self._escrows.get(escrow_id)
            if not esc:
                return False, "Not found"
            if esc.state not in ("funded", "disputed"):
                return False, f"Cannot refund: {esc.state}"
            if self._bc.height < esc.deadline and caller != esc.seller:
                return False, "Deadline not reached"
            esc.state = "refunded"
            return True, f"Refunded {esc.amount/10**DECIMALS:.3f} NBL to {esc.buyer}"

    def escrow_info(self, escrow_id: str) -> Optional[dict]:
        e = self._escrows.get(escrow_id)
        return e.to_dict() if e else None


# ---- SocialProfile
@dataclass
class SocialProfile:
    address:     str
    username:    str
    bio:         str = ""
    avatar_hash: str = ""
    followers:   int = 0
    following:   int = 0
    posts:       int = 0
    tips_received: int = 0
    verified:    bool = False
    created_at:  float = 0.0

    def to_dict(self) -> dict:
        return {
            "address":      self.address,
            "username":     self.username,
            "bio":          self.bio,
            "followers":    self.followers,
            "following":    self.following,
            "posts":        self.posts,
            "tips_nbl":     f"{self.tips_received/10**DECIMALS:.3f}",
            "verified":     self.verified,
        }


# ---- SocialPost
@dataclass
class SocialPost:
    post_id:    str
    author:     str
    content:    str
    timestamp:  float
    likes:      int = 0
    tips:       int = 0
    parent_id:  str = ""    # for replies
    content_hash: str = ""

    def to_dict(self) -> dict:
        return {
            "post_id":    self.post_id,
            "author":     self.author,
            "content":    self.content[:280],  # Twitter-like limit
            "timestamp":  self.timestamp,
            "likes":      self.likes,
            "tips_nbl":   f"{self.tips/10**DECIMALS:.3f}",
            "is_reply":   bool(self.parent_id),
        }


# ---- NEBULASocial
class NEBULASocial:
    """
    On-chain social network for NEBULA.
    All data stored on-chain or as content hashes.
    NBL micropayments for tipping creators.
    """

    MAX_POST_LENGTH = 560

    def __init__(self, blockchain: 'NEBULABlockchain'):
        self._bc        = blockchain
        self._profiles: Dict[str, SocialProfile] = {}
        self._posts:    Dict[str, SocialPost]     = {}
        self._follows:  Dict[str, Set[str]]       = {}  # follower -> {following}
        self._likes:    Dict[str, Set[str]]       = {}  # post_id -> {liker}
        self._lock      = threading.RLock()

    def create_profile(self, address: str, username: str,
                        bio: str = "") -> Tuple[bool, str]:
        with self._lock:
            if address in self._profiles:
                return False, "Profile exists"
            if any(p.username == username for p in self._profiles.values()):
                return False, f"Username '{username}' taken"
            self._profiles[address] = SocialProfile(
                address    = address,
                username   = username,
                bio        = bio,
                created_at = time.time(),
            )
            return True, f"Profile @{username} created"

    def post(self, author: str, content: str,
             parent_id: str = "") -> Tuple[bool, str]:
        with self._lock:
            if author not in self._profiles:
                return False, "No profile"
            if len(content) > self.MAX_POST_LENGTH:
                return False, f"Too long (max {self.MAX_POST_LENGTH})"
            pid = hashlib.sha256(
                f"{author}{content}{time.time()}".encode()
            ).hexdigest()[:16]
            self._posts[pid] = SocialPost(
                post_id      = pid,
                author       = author,
                content      = content,
                timestamp    = time.time(),
                parent_id    = parent_id,
                content_hash = hashlib.sha256(content.encode()).hexdigest(),
            )
            self._profiles[author].posts += 1
            return True, pid

    def follow(self, follower: str, target: str) -> Tuple[bool, str]:
        with self._lock:
            if follower == target:
                return False, "Cannot follow yourself"
            if follower not in self._follows:
                self._follows[follower] = set()
            if target in self._follows[follower]:
                return False, "Already following"
            self._follows[follower].add(target)
            if follower in self._profiles:
                self._profiles[follower].following += 1
            if target in self._profiles:
                self._profiles[target].followers += 1
            return True, f"Now following {target}"

    def unfollow(self, follower: str, target: str) -> Tuple[bool, str]:
        with self._lock:
            if self._follows.get(follower) and target in self._follows[follower]:
                self._follows[follower].remove(target)
                if follower in self._profiles:
                    self._profiles[follower].following -= 1
                if target in self._profiles:
                    self._profiles[target].followers -= 1
                return True, "Unfollowed"
            return False, "Not following"

    def like(self, liker: str, post_id: str) -> Tuple[bool, str]:
        with self._lock:
            if post_id not in self._posts:
                return False, "Post not found"
            if post_id not in self._likes:
                self._likes[post_id] = set()
            if liker in self._likes[post_id]:
                self._likes[post_id].remove(liker)
                self._posts[post_id].likes -= 1
                return True, "Unliked"
            self._likes[post_id].add(liker)
            self._posts[post_id].likes += 1
            return True, "Liked"

    def tip(self, tipper: str, post_id: str,
             amount_nbl: float) -> Tuple[bool, str]:
        """Tip a post author with NBL."""
        with self._lock:
            post = self._posts.get(post_id)
            if not post:
                return False, "Post not found"
            amount = int(amount_nbl * 10**DECIMALS)
            post.tips += amount
            if post.author in self._profiles:
                self._profiles[post.author].tips_received += amount
            return True, f"Tipped {amount_nbl} NBL to @{post.author}"

    def feed(self, address: str, limit: int = 20) -> List[dict]:
        """Get feed of posts from followed accounts."""
        following = self._follows.get(address, set()) | {address}
        with self._lock:
            posts = [p for p in self._posts.values()
                     if p.author in following]
        posts.sort(key=lambda p: p.timestamp, reverse=True)
        return [p.to_dict() for p in posts[:limit]]

    def trending(self, limit: int = 10) -> List[dict]:
        """Get trending posts by engagement."""
        with self._lock:
            posts = list(self._posts.values())
        posts.sort(key=lambda p: p.likes + p.tips // 10**DECIMALS, reverse=True)
        return [p.to_dict() for p in posts[:limit]]

    def profile(self, address: str) -> Optional[dict]:
        p = self._profiles.get(address)
        return p.to_dict() if p else None

    def social_stats(self) -> dict:
        with self._lock:
            total_profiles = len(self._profiles)
            total_posts    = len(self._posts)
            total_follows  = sum(len(f) for f in self._follows.values())
            total_tips     = sum(p.tips for p in self._posts.values())
        return {
            "total_profiles": total_profiles,
            "total_posts":    total_posts,
            "total_follows":  total_follows,
            "total_tips_nbl": f"{total_tips/10**DECIMALS:.3f}",
        }


# ---- InsurancePolicy
@dataclass
class InsurancePolicy:
    policy_id:    str
    holder:       str
    coverage_type: str    # "smart_contract", "bridge", "depeg", "hack"
    covered_protocol: str
    coverage_amount: int
    premium_paid: int
    valid_until:  int    # block height
    active:       bool = True
    claimed:      bool = False

    def to_dict(self) -> dict:
        return {
            "policy_id":     self.policy_id,
            "holder":        self.holder,
            "type":          self.coverage_type,
            "protocol":      self.covered_protocol,
            "coverage_nbl":  f"{self.coverage_amount/10**DECIMALS:.3f}",
            "premium_nbl":   f"{self.premium_paid/10**DECIMALS:.6f}",
            "valid_until":   self.valid_until,
            "active":        self.active,
            "claimed":       self.claimed,
        }
