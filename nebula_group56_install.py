"""nebula_group56_install.py - wiring layer for NEBULA group56 (20 formerly dead classes).

Design rules (from the group56 guide):
  * nebula_v10_11.py and nebula_group56.py are NEVER edited. Everything is attached from outside.
  * The layer never rejects a block, a transaction or a peer message. Every callback is wrapped
    in try/except; failures are counted in layer.errors / layer.error_log and the node keeps running.
  * The original method always runs first (Mempool.submit, P2PNode._handle_message).
  * Observation only: counters, statistics, bounded in-memory history. No consensus decisions.
  * install(host) / uninstall(host) are idempotent and fully reversible.

Usage:
    import nebula_v10_11 as host
    import nebula_group56_install as g56
    g56.install(host)                # before the node is created
    node = host.NEBULAFullNode(...)  # node.group56 is the layer
    print(node.group56.stats())
    g56.uninstall(host)              # restores everything
"""
from __future__ import annotations

import logging
import math
import threading
import time
from functools import wraps
from typing import Any, Callable, Dict, List, Optional

import nebula_group56 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group56")

PAIR = "NBL/USD"
HEADER_CAP = 10_000          # light-client headers kept in RAM
PROPAGATION_CAP = 5_000      # propagation records kept in RAM
PEER_CAP = 1_000             # peers tracked by PeerDiscoveryV2
SIG_CAP = 10_000             # signatures kept by AggregateSignatureScheme
ADDR_CAP_PER_BLOCK = 500     # output addresses checked per block (report-only)
ERROR_LOG_CAP = 50

_LAYERS: List["Layer56"] = []
_LAYERS_LOCK = threading.RLock()


# --------------------------------------------------------------------------------------
# RealizedVolatility fix (documented deviation - see README)
# --------------------------------------------------------------------------------------
class RealizedVolatilityFixed(g.RealizedVolatility):
    """The verbatim RealizedVolatility.record_price only appends a log-return when the
    return list is already non-empty, and the list starts empty, so it never fills and
    realized_vol() always returns None. This subclass keeps the same public API and fixes
    that, plus guards log() against non-positive prices. nebula_group56.py is untouched."""

    def record_price(self, pair: str, price: float):
        last_map = self.__dict__.setdefault("_g56_last", {})
        rets = self._log_returns.setdefault(pair, [])
        last = last_map.get(pair)
        if last is not None and last > 0 and price > 0:
            rets.append(math.log(price / last))
            if len(rets) > 1000:
                rets.pop(0)
        if price > 0:
            last_map[pair] = price


# --------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------
def _first(x):
    if isinstance(x, (list, tuple)):
        return x[0] if x else None
    return x


def _last(x):
    if isinstance(x, (list, tuple)):
        return x[-1] if x else None
    return x


def _iter_output_addresses(block):
    n = 0
    for tx in getattr(block, "transactions", None) or []:
        for out in getattr(tx, "outputs", None) or []:
            addr = getattr(out, "address", None)
            if addr is None and isinstance(out, dict):
                addr = out.get("address")
            if isinstance(addr, str):
                yield addr
                n += 1
                if n >= ADDR_CAP_PER_BLOCK:
                    return


def _peer_id(peer) -> str:
    for attr in ("id", "peer_id", "addr", "address", "host", "ip"):
        v = getattr(peer, attr, None)
        if v:
            return str(v)[:64]
    return repr(peer)[:64]


# --------------------------------------------------------------------------------------
# the layer
# --------------------------------------------------------------------------------------
class Layer56:
    """Holds the 20 group56 services for one node and feeds them with real data."""

    def __init__(self, node, vrf_privkey: Optional[int] = None, sample_every: int = 10):
        self.node = node
        self.bc = getattr(node, "bc", None)
        self.p2p = self._find(node, ("p2p", "network", "p2p_node", "net"))
        self.oracle = self._find(node, ("oracle", "oracle_v2", "price_oracle"))
        self.sample_every = max(1, int(sample_every))

        self.errors = 0
        self.last_error: Optional[str] = None
        self.error_log: List[str] = []
        self.build_errors: Dict[str, str] = {}
        self._clock = threading.Lock()
        self.counters: Dict[str, int] = {
            "blocks_seen": 0, "reorgs_seen": 0, "reorgs_skipped": 0,
            "submit_seen": 0, "submit_ok": 0, "p2p_messages": 0,
            "addr_checked": 0, "addr_invalid": 0,
        }
        self.last_block_summary: Optional[str] = None
        self.last_quantum_risk: Optional[dict] = None
        self.last_selection: Optional[dict] = None

        self._mempool = None
        self._mempool_had_attr = False
        self._mempool_orig = None
        self.mempool_hooked = False
        self.attached = False

        b = self._build
        # --- services that need no host objects
        self.aggregate_sigs = b("AggregateSignatureScheme", g.AggregateSignatureScheme)
        self.pq_prep = b("PostQuantumPrep", g.PostQuantumPrep)
        self.light_client = b("NEBULALightClient", g.NEBULALightClient)
        self.address_validator = b("AddressValidator", g.AddressValidator)
        self.block_serializer = b("BlockSerializer", g.BlockSerializer)
        self.gov_token = b("NBLGovernanceToken", g.NBLGovernanceToken)
        self.vol_calc = b("VolatilityCalculator", g.VolatilityCalculator)
        self.realized_vol = b("RealizedVolatility", RealizedVolatilityFixed)
        self.interest = b("InterestRateCalculator", g.InterestRateCalculator)
        self.twap = b("TwapOracle", lambda: g.TwapOracle(PAIR))
        # --- services that need the blockchain
        bc = self.bc
        self.fork_manager = b("ForkManager", lambda: g.ForkManager(bc), need=bc)
        self.tx_prioritizer = b("TxPrioritizer", lambda: g.TxPrioritizer(bc), need=bc)
        self.block_propagation = b("BlockPropagationManager", lambda: g.BlockPropagationManager(bc), need=bc)
        self.tx_broadcaster = b("TransactionBroadcaster", lambda: g.TransactionBroadcaster(bc), need=bc)
        self.wrapped_nbl = b("WrappedNBL", lambda: g.WrappedNBL(bc), need=bc)
        self.amortized_fees = b("AmortizedFeeCalculator", lambda: g.AmortizedFeeCalculator(bc), need=bc)
        orc = self.oracle
        self.fair_value = b("FairValueEstimator", lambda: g.FairValueEstimator(bc, orc), need=bc)
        # --- services that need other host objects
        p2p = self.p2p
        self.peer_discovery = b("PeerDiscoveryV2", lambda: g.PeerDiscoveryV2(p2p), need=p2p)
        self.price3 = b("PriceOracle3in1", lambda: g.PriceOracle3in1(PAIR, orc), need=orc)
        # --- VRFv2 needs a private key supplied by the operator (never invented here)
        self.vrf = None
        if vrf_privkey is not None:
            self.vrf = b("VRFv2", lambda: g.VRFv2(int(vrf_privkey)))

    # ---------------- construction helpers
    @staticmethod
    def _find(node, names):
        for n in names:
            v = getattr(node, n, None)
            if v is not None:
                return v
        return None

    def _build(self, name: str, factory: Callable[[], Any], need: Any = True):
        if need is None:
            self.build_errors[name] = "required host object not found on node"
            return None
        try:
            return factory()
        except Exception as e:  # one failing class must not break the others
            self.build_errors[name] = f"{type(e).__name__}: {e}"
            log.warning("group56: could not build %s: %s", name, e)
            return None

    # ---------------- bookkeeping
    def _bump(self, key: str, n: int = 1):
        with self._clock:
            self.counters[key] = self.counters.get(key, 0) + n

    def _err(self, where: str, exc: BaseException):
        msg = f"{where}: {type(exc).__name__}: {exc}"
        with self._clock:
            self.errors += 1
            self.last_error = msg
            self.error_log.append(msg)
            if len(self.error_log) > ERROR_LOG_CAP:
                del self.error_log[0]
        log.debug("group56 %s", msg)

    def _step(self, name: str, fn: Callable, *a):
        """Run one sub-step; failure is counted and never propagates."""
        try:
            return fn(*a)
        except Exception as e:
            self._err(name, e)
            return None

    # ---------------- attach / detach
    def attach(self):
        if self.attached:
            return
        self.bc.add_listener(self)
        self.attached = True
        self._hook_mempool()

    def detach(self):
        try:
            self.bc._listeners.remove(self)
        except Exception:
            rm = getattr(self.bc, "remove_listener", None)
            if callable(rm):
                try:
                    rm(self)
                except Exception:
                    _NB_SWALLOW_LOG.debug("swallowed Exception in Layer56.detach", exc_info=True)
        self._unhook_mempool()
        self.attached = False

    def _hook_mempool(self):
        mp = getattr(self.bc, "mempool", None)
        submit = getattr(mp, "submit", None)
        if mp is None or not callable(submit) or getattr(mp, "_g56_hooked", False):
            return
        layer = self

        def wrapped(tx, *a, **k):
            result = submit(tx, *a, **k)          # original ALWAYS runs first
            try:
                layer._after_submit(tx, result)
            except Exception as e:
                layer._err("mempool.submit", e)
            return result                          # result is never altered

        try:
            self._mempool_had_attr = "submit" in getattr(mp, "__dict__", {})
            self._mempool_orig = submit
            mp.submit = wrapped
            mp._g56_hooked = True
            self._mempool = mp
            self.mempool_hooked = True
        except Exception as e:                     # e.g. __slots__
            self._err("mempool hook", e)

    def _unhook_mempool(self):
        mp = self._mempool
        if mp is None:
            return
        try:
            if self._mempool_had_attr:
                mp.submit = self._mempool_orig
            else:
                del mp.submit
            del mp._g56_hooked
        except Exception as e:
            self._err("mempool unhook", e)
        self._mempool = None
        self.mempool_hooked = False

    # ---------------- chain listener API (confirmed in host: add_listener/_notify_connect/_notify_reorg)
    def on_connect(self, block):
        try:
            self._bump("blocks_seen")
            n = self.counters["blocks_seen"]
            self._step("light_client", self._feed_light_client, block)
            self._step("propagation", self._feed_propagation, block)
            self._step("serializer", self._feed_serializer, block)
            self._step("addresses", self._feed_addresses, block)
            if n % self.sample_every == 0:
                self._step("tx_prioritizer", self._sample_prioritizer)
                self._step("quantum_risk", self._sample_quantum, block)
                self._step("prices", self._sample_prices)
        except Exception as e:
            self._err("on_connect", e)

    def on_reorg(self, old, new, ancestor_height):
        try:
            fm = self.fork_manager
            if fm is None:
                return
            fork_block = _first(old) or _first(new)
            tip = _last(new)
            tip_hash = getattr(tip, "hash", None)
            if fork_block is None or getattr(fork_block, "hash", None) is None or tip_hash is None:
                self._bump("reorgs_skipped")
                return
            fm.record_fork(fork_block, str(tip_hash))
            fm.resolve_fork(str(tip_hash))         # host already finished the reorg when it notifies
            self._bump("reorgs_seen")
        except Exception as e:
            self._err("on_reorg", e)

    # ---------------- per-block feeders
    def _feed_light_client(self, block):
        lc = self.light_client
        if lc is None:
            return
        h = block.header
        lc.add_header(block.height, block.hash, h.prev_hash, h.bits, h.timestamp)
        hdrs = lc._headers
        if len(hdrs) > HEADER_CAP + 500:           # batch prune, oldest heights first
            for k in sorted(hdrs)[: len(hdrs) - HEADER_CAP]:
                hdrs.pop(k, None)

    def _feed_propagation(self, block):
        bp = self.block_propagation
        if bp is None:
            return
        peers = 0
        try:
            peers = len(getattr(self.p2p, "peers", ()) or ())
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Layer56._feed_propagation", exc_info=True)
        bp.broadcast(block, peers=peers)           # records only; sends nothing
        with bp._lock:
            while len(bp._propagated) > PROPAGATION_CAP:
                bp._propagated.pop(next(iter(bp._propagated)))

    def _feed_serializer(self, block):
        if self.block_serializer is not None:
            self.last_block_summary = self.block_serializer.block_summary(block)

    def _feed_addresses(self, block):             # report-only: never rejects anything
        av = self.address_validator
        if av is None:
            return
        for addr in _iter_output_addresses(block):
            self._bump("addr_checked")
            if not av.is_valid(addr):
                self._bump("addr_invalid")

    # ---------------- periodic samplers
    def _sample_prioritizer(self):
        tp = self.tx_prioritizer
        if tp is None:
            return
        sel = tp.select_for_block()
        self.last_selection = {"txs": len(sel), "bytes": sum(t.byte_size() for t in sel)}

    def _sample_quantum(self, block):
        if self.pq_prep is not None:
            self.last_quantum_risk = self.pq_prep.assess_quantum_risk(block.height)

    def _sample_prices(self):
        orc = self.oracle
        if orc is None:
            return
        price = orc.price(PAIR)
        if not price or price <= 0:
            return
        self.twap.update(price)
        self.vol_calc.record(PAIR, price)
        self.realized_vol.record_price(PAIR, price)
        if self.price3 is not None:
            self.price3.get_all_prices()

    # ---------------- mempool / p2p observers
    def _after_submit(self, tx, result):
        self._bump("submit_seen")
        ok = result[0] if isinstance(result, tuple) and result else bool(result)
        if not ok:
            return
        self._bump("submit_ok")
        if self.amortized_fees is not None:
            self.amortized_fees.record_fee(int(tx.fee(self.bc.utxo)))

    def on_p2p_message(self, peer, msg):
        self._bump("p2p_messages")
        pd = self.peer_discovery
        if pd is None:
            return
        pid = _peer_id(peer)
        with pd._lock:
            known = pid in pd._latency
            full = len(pd._latency) >= PEER_CAP
        if not known and not full:
            ip = str(getattr(peer, "ip", None) or getattr(peer, "host", None) or "")
            # region/latency are not provided by the host: 'unknown' / 9999 ms sentinel (see README)
            pd.register(pid, ip, "unknown", 9999.0)

    # ---------------- operator helpers
    def record_signature(self, pubkey: bytes, sig: bytes, msg_hash: bytes):
        agg = self.aggregate_sigs
        if agg is None:
            return False
        agg.add_signature(pubkey, sig, msg_hash)
        if len(agg._sigs) > SIG_CAP:
            del agg._sigs[0]
        return True

    def stats(self) -> dict:
        def safe(fn):
            try:
                return fn()
            except Exception as e:
                return {"error": f"{type(e).__name__}: {e}"}

        s: Dict[str, Any] = {
            "errors": self.errors, "last_error": self.last_error,
            "build_errors": dict(self.build_errors),
            "counters": dict(self.counters),
            "mempool_hooked": self.mempool_hooked,
            "last_block": self.last_block_summary,
            "last_selection": self.last_selection,
            "quantum": self.last_quantum_risk,
        }
        if self.light_client:
            s["light_client"] = safe(self.light_client.light_client_info)
        if self.fork_manager:
            s["forks"] = safe(self.fork_manager.fork_stats)
        if self.block_propagation:
            s["propagation"] = safe(self.block_propagation.propagation_stats)
        if self.amortized_fees:
            s["fees"] = safe(self.amortized_fees.fee_report)
        if self.tx_broadcaster:
            s["broadcaster"] = safe(self.tx_broadcaster.broadcaster_stats)
        if self.wrapped_nbl:
            s["wnbl"] = safe(self.wrapped_nbl.wnbl_stats)
        if self.gov_token:
            s["governance_token"] = safe(self.gov_token.info)
        if self.twap:
            s["twap"] = safe(self.twap.twap_info)
        if self.vol_calc:
            s["volatility"] = safe(lambda: self.vol_calc.vol_info(PAIR))
        if self.realized_vol:
            s["realized_vol"] = safe(lambda: self.realized_vol.realized_vol(PAIR))
        if self.fair_value:
            s["fair_value"] = safe(self.fair_value.fair_value_estimate)
        if self.peer_discovery:
            s["peers"] = safe(lambda: self.peer_discovery.best_peers(5))
        if self.aggregate_sigs:
            s["aggregate_sigs"] = safe(self.aggregate_sigs.agg_info)
        if self.pq_prep:
            s["pqc"] = safe(self.pq_prep.pqc_info)
        return s


# --------------------------------------------------------------------------------------
# P2P class-level wrapper (original method always first)
# --------------------------------------------------------------------------------------
def _dispatch_p2p(p2p_obj, peer, msg):
    with _LAYERS_LOCK:
        layers = list(_LAYERS)
    for L in layers:
        if L.p2p is p2p_obj:
            try:
                L.on_p2p_message(peer, msg)
            except Exception as e:
                L._err("p2p", e)


def _patch_p2p(host) -> List[str]:
    patched_names = []
    for cname in ("P2PNode", "P2PNetwork"):
        cls = getattr(host, cname, None)
        orig = getattr(cls, "_handle_message", None) if cls is not None else None
        if orig is None or getattr(cls, "_g56_hm_orig", None) is not None:
            continue

        def make(orig):
            @wraps(orig)
            def patched(self, peer, msg, *a, **k):
                result = orig(self, peer, msg, *a, **k)   # original first; its exceptions propagate unchanged
                _dispatch_p2p(self, peer, msg)
                return result
            return patched

        cls._g56_hm_orig = orig
        cls._handle_message = make(orig)
        patched_names.append(cname)
    return patched_names


def _unpatch_p2p(host):
    for cname in ("P2PNode", "P2PNetwork"):
        cls = getattr(host, cname, None)
        orig = getattr(cls, "_g56_hm_orig", None) if cls is not None else None
        if orig is not None:
            cls._handle_message = orig
            del cls._g56_hm_orig


# --------------------------------------------------------------------------------------
# optional read-only REST endpoints (opt-in: install(host, rest=True))
# --------------------------------------------------------------------------------------
def _layer_from_args(args) -> Optional[Layer56]:
    for x in args:
        L = getattr(x, "group56", None)
        if isinstance(L, Layer56):
            return L
    with _LAYERS_LOCK:
        return _LAYERS[-1] if _LAYERS else None


def _register_rest(host) -> bool:
    route = getattr(host, "route", None)
    if not callable(route) or getattr(host, "_g56_rest", False):
        return False

    def stats_handler(*a, **k):
        L = _layer_from_args(a)
        if L is None:
            return 503, {"success": False, "error": "group56 layer not active"}
        return 200, {"success": True, "data": L.stats()}

    def interest_handler(*a, **k):
        L = _layer_from_args(a)
        if L is None or L.interest is None:
            return 503, {"success": False, "error": "group56 layer not active"}
        util = k.get("utilization")
        for x in a:
            if isinstance(x, dict) and "utilization" in x:
                util = x["utilization"]
        if isinstance(util, (list, tuple)):
            util = util[0] if util else None
        try:
            if util is None:
                return 200, {"success": True, "data": L.interest.simulate()}
            u = float(util)
            if not 0.0 <= u <= 1.0:
                return 400, {"success": False, "error": "utilization must be between 0 and 1"}
            return 200, {"success": True, "data": {"utilization": u, "rate": L.interest.rate(u)}}
        except (TypeError, ValueError):
            return 400, {"success": False, "error": "utilization must be a number"}

    route("/api/group56/stats")(stats_handler)
    route("/api/group56/interest")(interest_handler)
    host._g56_rest = True
    return True


# --------------------------------------------------------------------------------------
# install / uninstall
# --------------------------------------------------------------------------------------
def install(host, *, rest: bool = False, vrf_privkey: Optional[int] = None, sample_every: int = 10) -> dict:
    """Patch NEBULAFullNode.__init__ so every new node gets node.group56. Idempotent."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g56_orig", None) is not None:
        return {"already_installed": True}
    orig = cls.__init__

    @wraps(orig)
    def patched(self, *a, **k):
        orig(self, *a, **k)
        try:
            layer = Layer56(self, vrf_privkey=vrf_privkey, sample_every=sample_every)
            layer.attach()
            self.group56 = layer
            with _LAYERS_LOCK:
                _LAYERS.append(layer)
        except Exception as e:                      # the node must still start
            self.group56_error = e
            log.warning("group56 layer failed to attach: %s", e)

    cls._g56_orig = orig
    cls.__init__ = patched
    info = {"already_installed": False, "p2p_patched": _patch_p2p(host), "rest": False}
    if rest:
        try:
            info["rest"] = _register_rest(host)
        except Exception as e:
            info["rest_error"] = f"{type(e).__name__}: {e}"
    return info


def uninstall(host):
    """Restore everything: constructor, P2P handler, listeners, mempool hooks."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g56_orig", None)
    if orig is not None:
        cls.__init__ = orig
        del cls._g56_orig
    _unpatch_p2p(host)
    with _LAYERS_LOCK:
        layers = list(_LAYERS)
        _LAYERS.clear()
    for L in layers:
        L.detach()
