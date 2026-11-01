"""NEBULA group51 - full wiring layer (installer).

Wires all 20 group51 classes to a running NEBULAFullNode WITHOUT editing nebula_v10_11.py.

Design rules (from the guide):
  * REPORT-ONLY: nothing here ever rejects a block, a transaction or a peer message.
  * Every callback runs inside try/except; failures are counted in layer.errors.
  * The original host method ALWAYS runs first; our code runs after it.
  * install(host) is idempotent; uninstall(host) restores every patched method.
  * A class that fails to build does not stop the others (see layer.build_errors).

Usage:
    import nebula_v10_11 as host
    import nebula_group51_install as g51
    g51.install(host)                       # before the node is created
    node = host.NEBULAFullNode(...)         # node.group51 is now available
    print(node.group51.status())
    g51.uninstall(host)                     # back to the original behaviour

Optional configuration (nothing fake is created when you leave it out):
    g51.install(host, config={
        "council_members":    ["addr1", ... up to 7],
        "guardians":          ["addrA", ...],
        "multisig_signers":   ["addr1", "addr2", "addr3"],
        "multisig_required":  2,
        "tss":                (3, 5),
        "feed_cap":           1000,
        "report_cap":         1000,
        "max_txs_per_block":  500,
    })
"""
from __future__ import annotations

import threading
import time
import traceback
from collections import defaultdict, deque
from typing import Any, Callable, Dict, List, Optional

import nebula_group51 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

__all__ = ["Layer51", "install", "uninstall", "active_layers"]

# --------------------------------------------------------------------------
# registry of live layers (the Mempool / P2P wrappers do not know the node)
# --------------------------------------------------------------------------
_ACTIVE: List["Layer51"] = []
_ACTIVE_LOCK = threading.RLock()

_DEFAULTS: Dict[str, Any] = {
    "council_members": [],
    "guardians": [],
    "multisig_signers": [],
    "multisig_required": 0,
    "tss": (3, 5),
    "feed_cap": 1000,
    "report_cap": 1000,
    "max_txs_per_block": 500,
}

# names under which the host may already keep shared services (all optional)
_HOST_NAMES = {
    "oracle":   ("oracle", "oracle_v2", "oraclev2"),
    "venbl":    ("venbl", "ve_nbl", "vote_escrow", "vote_escrowed_nbl"),
    "treasury": ("treasury", "nebula_treasury"),
    "nft":      ("nft", "nft_registry", "nbl721", "nbl721_registry"),
}


def active_layers() -> List["Layer51"]:
    with _ACTIVE_LOCK:
        return list(_ACTIVE)


class Layer51:
    """Holds all 20 group51 classes and feeds them real chain data (report-only)."""

    # build order = guide step 4 (data types first, then dependents)
    BUILD_ORDER = (
        "data_types", "security_council", "compliance_rule", "compliance",
        "data_feeds", "perps", "options", "treasury_yield", "gov_v3",
        "synth", "xcgov", "ecosystem", "interop", "tss", "kdf",
        "nft_lending", "dao", "multisig", "zk",
    )

    def __init__(self, node: Any, config: Optional[dict] = None):
        self.node = node
        self.bc = getattr(node, "bc", None)
        self.cfg = dict(_DEFAULTS)
        self.cfg.update(config or {})
        self.errors = 0
        self.last_error: Optional[str] = None
        self.build_errors: Dict[str, str] = {}
        self.skipped: Dict[str, str] = {}
        self.counters: Dict[str, int] = defaultdict(int)
        self.recent_findings: deque = deque(maxlen=200)
        self.lock = threading.RLock()
        self.attached = False

        # host services (None when the host does not expose them)
        self.oracle = self._find("oracle")
        self.venbl = self._find("venbl")
        self.host_treasury = self._find("treasury")
        self.host_nft = self._find("nft")

        # the 20 classes
        self.compliance_rule: Optional[g.ComplianceRuleV2] = None
        self.compliance: Optional[g.ComplianceV2] = None
        self.data_feeds: Optional[g.DataFeedRegistry] = None
        self.perps: Optional[g.PerpetualProtocol] = None
        self.options: Optional[g.OptionsProtocolV2] = None
        self.treasury_yield: Optional[g.TreasuryYieldStrategy] = None
        self.gov_v3: Optional[g.GovernanceV3] = None
        self.synth: Optional[g.SyntheticAssetProtocol] = None
        self.xcgov: Optional[g.CrossChainGovernance] = None
        self.council: Optional[g.SecurityCouncil] = None
        self.ecosystem: Optional[g.EcosystemTracker] = None
        self.interop: Optional[g.InteroperabilityLayer] = None
        self.tss: Optional[g.ThresholdSignatureScheme] = None
        self.kdf: Optional[g.KeyDerivationFunction] = None
        self.nft_lending: Optional[g.NFTLending] = None
        self.dao: Optional[g.DAOv2] = None
        self.multisig: Optional[g.MultisigTreasury] = None
        self.zk: Optional[g.RecursiveZKProof] = None

        self._build_all()

    # ------------------------------------------------------------------ helpers
    def _find(self, kind: str) -> Any:
        for name in _HOST_NAMES[kind]:
            obj = getattr(self.node, name, None)
            if obj is None and self.bc is not None:
                obj = getattr(self.bc, name, None)
            if obj is not None:
                return obj
        return None

    def _fail(self, where: str, exc: BaseException) -> None:
        with self.lock:
            self.errors += 1
            self.last_error = f"{where}: {type(exc).__name__}: {exc}"

    def _guard(self, where: str, fn: Callable, *a, **k) -> Any:
        try:
            return fn(*a, **k)
        except Exception as e:                       # never propagate into the host
            self._fail(where, e)
            return None

    def _count(self, key: str, n: int = 1) -> None:
        with self.lock:
            self.counters[key] += n

    # ------------------------------------------------------------------ build
    def _build_all(self) -> None:
        for step in self.BUILD_ORDER:
            try:
                getattr(self, "_build_" + step)()
            except Exception as e:
                self.build_errors[step] = f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=2)}"

    def _build_data_types(self) -> None:
        # SyntheticAsset and NFTLoanOffer are plain data types. They are used by
        # SyntheticAssetProtocol / NFTLending; here we only prove they are importable.
        assert g.SyntheticAsset and g.NFTLoanOffer

    def _build_security_council(self) -> None:
        self.council = g.SecurityCouncil(self.bc)
        for m in self.cfg["council_members"]:
            self.council.add_member(m)

    def _build_compliance_rule(self) -> None:
        council = self.council

        def frozen_check(address: str, ctx: dict):
            if council is not None and council.is_frozen(address):
                return False, "Address frozen by Security Council"
            return True, "OK"

        self.compliance_rule = g.ComplianceRuleV2(
            "council_freeze", "Security Council freeze list", frozen_check, "critical")

    def _build_compliance(self) -> None:
        self.compliance = g.ComplianceV2(self.bc)
        r = self.compliance_rule
        if r is not None:
            self.compliance.add_rule(r.rule_id, r.name, r.check_fn, r.severity)

    def _build_data_feeds(self) -> None:
        self.data_feeds = g.DataFeedRegistry(self.bc)
        for fid, desc in (
            ("chain.height", "Height of the best chain"),
            ("chain.block_txs", "Transactions per connected block"),
            ("chain.reorg_depth", "Blocks removed by the last reorg"),
            ("mempool.submitted", "Cumulative Mempool.submit calls seen"),
            ("p2p.messages", "Cumulative P2P messages seen"),
        ):
            self.data_feeds.register_feed(fid, desc, "int", "group51")

    def _build_perps(self) -> None:
        self.perps = g.PerpetualProtocol(self.bc, self.oracle)

    def _build_options(self) -> None:
        self.options = g.OptionsProtocolV2(self.bc, self.oracle)

    def _build_treasury_yield(self) -> None:
        if self.host_treasury is None:
            self.skipped["treasury_yield"] = "host treasury object not found on node"
            return
        self.treasury_yield = g.TreasuryYieldStrategy(self.host_treasury, self.bc)

    def _build_gov_v3(self) -> None:
        self.gov_v3 = g.GovernanceV3(self.bc, self.venbl)
        for guardian in self.cfg["guardians"]:
            self.gov_v3.add_guardian(guardian)

    def _build_synth(self) -> None:
        self.synth = g.SyntheticAssetProtocol(self.bc, self.oracle)

    def _build_xcgov(self) -> None:
        self.xcgov = g.CrossChainGovernance(self.bc)

    def _build_ecosystem(self) -> None:
        self.ecosystem = g.EcosystemTracker(self.bc)

    def _build_interop(self) -> None:
        # protocols stay DISABLED: nothing is ever sent to another chain automatically
        self.interop = g.InteroperabilityLayer(self.bc)

    def _build_tss(self) -> None:
        t, n = self.cfg["tss"]
        self.tss = g.ThresholdSignatureScheme(int(t), int(n))

    def _build_kdf(self) -> None:
        self.kdf = g.KeyDerivationFunction()

    def _build_nft_lending(self) -> None:
        if self.host_nft is None:
            self.skipped["nft_lending"] = "host NFT registry (NBL721Registry) not found on node"
            return
        self.nft_lending = g.NFTLending(self.bc, self.host_nft)

    def _build_dao(self) -> None:
        self.dao = g.DAOv2(self.bc, self.host_treasury)

    def _build_multisig(self) -> None:
        signers = list(self.cfg["multisig_signers"])
        required = int(self.cfg["multisig_required"])
        if not signers or required < 1:
            self.skipped["multisig"] = "needs config: multisig_signers + multisig_required"
            return
        self.multisig = g.MultisigTreasury(signers, required, self.bc)

    def _build_zk(self) -> None:
        self.zk = g.RecursiveZKProof()

    # --------------------------------------------------------- chain listener
    def on_connect(self, block: Any) -> None:
        try:
            self._handle_block(block)
        except Exception as e:
            self._fail("on_connect", e)

    def on_reorg(self, old: Any = None, new: Any = None, ancestor_height: Any = None) -> None:
        try:
            self._count("reorgs")
            depth = len(old) if old is not None and hasattr(old, "__len__") else 0
            if self.data_feeds:
                self.data_feeds.update_feed("chain.reorg_depth", depth, "group51")
        except Exception as e:
            self._fail("on_reorg", e)

    def _handle_block(self, block: Any) -> None:
        self._count("blocks_seen")
        txs = getattr(block, "transactions", None)
        if txs is None:
            txs = getattr(block, "txs", None)
        txs = list(txs or [])
        cap = int(self.cfg["max_txs_per_block"])

        if self.data_feeds:
            h = getattr(block, "height", None)
            if h is None:
                h = getattr(self.bc, "height", 0)
            self.data_feeds.update_feed("chain.height", h, "group51")
            self.data_feeds.update_feed("chain.block_txs", len(txs), "group51")
            self._trim_feeds()

        if self.ecosystem:
            self._guard("ecosystem.track_day", self.ecosystem.track_day)

        if self.compliance:
            for tx in txs[:cap]:
                self._check_tx(tx)
            self._trim_reports()

    def _trim_feeds(self) -> None:
        cap = int(self.cfg["feed_cap"])
        reg = self.data_feeds
        with reg._lock:
            for f in reg._feeds.values():
                if len(f["rounds"]) > cap:
                    del f["rounds"][: len(f["rounds"]) - cap]

    def _trim_reports(self) -> None:
        cap = int(self.cfg["report_cap"])
        c = self.compliance
        with c._lock:
            if len(c._reports) > cap:
                del c._reports[: len(c._reports) - cap]

    # ------------------------------------------------------- tx -> compliance
    @staticmethod
    def _outputs(tx: Any):
        outs = getattr(tx, "outputs", None)
        if outs is None and isinstance(tx, dict):
            outs = tx.get("outputs")
        for o in outs or []:
            if isinstance(o, dict):
                addr, amt = o.get("address"), o.get("amount", 0)
            else:
                addr, amt = getattr(o, "address", None), getattr(o, "amount", 0)
            if isinstance(addr, str):
                yield addr, int(amt or 0)

    def _check_tx(self, tx: Any) -> None:
        for addr, amount in self._outputs(tx):
            report = self._guard("compliance.check_address",
                                 self.compliance.check_address, addr, {"amount": amount})
            if not report:
                continue
            self._count("compliance_checked")
            if not report["compliant"]:
                self._count("compliance_flagged")
                bad = [r["rule"] for r in report["rules"] if not r["passed"]]
                self.recent_findings.append(
                    {"ts": time.time(), "address": addr, "amount": amount, "rules": bad})
            if self.council and self._guard("council.is_frozen", self.council.is_frozen, addr):
                self._count("frozen_address_seen")

    # -------------------------------------------- Mempool / P2P observations
    def observe_submit(self, result: Any) -> None:
        try:
            self._count("mempool_submitted")
            ok_flag = result[0] if isinstance(result, tuple) and result else bool(result)
            self._count("mempool_accepted" if ok_flag else "mempool_refused_by_host")
            if self.data_feeds:
                self.data_feeds.update_feed(
                    "mempool.submitted", self.counters["mempool_submitted"], "group51")
        except Exception as e:
            self._fail("observe_submit", e)

    def observe_p2p(self, peer: Any, msg: Any) -> None:
        try:
            self._count("p2p_messages")
            kind = None
            if isinstance(msg, dict):
                kind = msg.get("type") or msg.get("cmd")
            else:
                kind = getattr(msg, "type", None) or getattr(msg, "cmd", None)
            self._count("p2p_msg_" + str(kind or "unknown"))
            if self.data_feeds and self.counters["p2p_messages"] % 50 == 0:
                self.data_feeds.update_feed(
                    "p2p.messages", self.counters["p2p_messages"], "group51")
        except Exception as e:
            self._fail("observe_p2p", e)

    # --------------------------------------------------------------- status
    def stats(self) -> Dict[str, Any]:
        calls = {
            "compliance_v2": (self.compliance, "compliance_v2_stats"),
            "data_feeds": (self.data_feeds, "feed_registry_stats"),
            "perpetuals": (self.perps, "perp_protocol_stats"),
            "options_v2": (self.options, "options_v2_stats"),
            "treasury_yield": (self.treasury_yield, "treasury_yield_stats"),
            "governance_v3": (self.gov_v3, "gov_v3_stats"),
            "synthetics": (self.synth, "protocol_stats"),
            "cross_chain_gov": (self.xcgov, "xcgov_stats"),
            "security_council": (self.council, "council_stats"),
            "ecosystem": (self.ecosystem, "trajectory"),
            "interop": (self.interop, "interop_stats"),
            "threshold_sig": (self.tss, "threshold_info"),
            "nft_lending": (self.nft_lending, "nft_lending_stats"),
            "dao_v2": (self.dao, "dao_v2_stats"),
            "multisig_treasury": (self.multisig, "ms_treasury_stats"),
            "recursive_zk": (self.zk, "proof_stats"),
        }
        out: Dict[str, Any] = {}
        for name, (obj, meth) in calls.items():
            if obj is None:
                out[name] = {"status": "not_built", "reason": self.skipped.get(
                    {"treasury_yield": "treasury_yield", "nft_lending": "nft_lending",
                     "multisig_treasury": "multisig"}.get(name, name), "build error")}
                continue
            out[name] = self._guard("stats." + name, getattr(obj, meth))
        out["kdf"] = {"status": "ready"} if self.kdf else {"status": "not_built"}
        return out

    def status(self) -> Dict[str, Any]:
        with self.lock:
            counters = dict(self.counters)
        return {
            "attached": self.attached,
            "errors": self.errors,
            "last_error": self.last_error,
            "build_errors": dict(self.build_errors),
            "skipped": dict(self.skipped),
            "counters": counters,
            "host_services": {
                "oracle": self.oracle is not None, "venbl": self.venbl is not None,
                "treasury": self.host_treasury is not None, "nft": self.host_nft is not None,
            },
            "classes_built": sum(1 for o in (
                self.compliance_rule, self.compliance, self.data_feeds, self.perps,
                self.options, self.treasury_yield, self.gov_v3, self.synth, self.xcgov,
                self.council, self.ecosystem, self.interop, self.tss, self.kdf,
                self.nft_lending, self.dao, self.multisig, self.zk) if o is not None) + 2,
            "stats": self.stats(),
        }

    # ------------------------------------------------------------- lifecycle
    def attach(self) -> None:
        if self.bc is not None and hasattr(self.bc, "add_listener"):
            self.bc.add_listener(self)
            self.attached = True
        with _ACTIVE_LOCK:
            if self not in _ACTIVE:
                _ACTIVE.append(self)

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer51.detach", exc_info=True)
        self.attached = False
        with _ACTIVE_LOCK:
            if self in _ACTIVE:
                _ACTIVE.remove(self)


# --------------------------------------------------------------------------
# install / uninstall (idempotent, fully reversible)
# --------------------------------------------------------------------------
def _wrap_after(cls: Any, name: str, marker: str, observer: Callable) -> None:
    orig = getattr(cls, name, None)
    if orig is None or getattr(cls, marker, None) is not None:
        return

    def wrapper(self, *a, **k):
        result = orig(self, *a, **k)                 # original ALWAYS first
        for layer in active_layers():
            try:
                observer(layer, a, k, result)
            except Exception as e:
                layer._fail("wrapper." + name, e)
        return result

    wrapper.__wrapped__ = orig
    setattr(cls, marker, orig)
    setattr(cls, name, wrapper)


def _unwrap(cls: Any, name: str, marker: str) -> None:
    orig = getattr(cls, marker, None)
    if orig is not None:
        setattr(cls, name, orig)
        delattr(cls, marker)


def install(host: Any, config: Optional[dict] = None) -> bool:
    """Patch host classes. Returns False if already installed."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g51_orig", None) is not None:
        return False
    orig_init = cls.__init__
    cfg = dict(config or {})

    def patched(self, *a, **k):
        orig_init(self, *a, **k)                     # node must start exactly as before
        try:
            layer = Layer51(self, cfg)
            layer.attach()
            self.group51 = layer
        except Exception as e:                       # node still runs
            self.group51_error = e

    patched.__wrapped__ = orig_init
    cls._g51_orig = orig_init
    cls.__init__ = patched

    mp = getattr(host, "Mempool", None)
    if mp is not None:
        _wrap_after(mp, "submit", "_g51_orig_submit",
                    lambda layer, a, k, r: layer.observe_submit(r))
    p2p = getattr(host, "P2PNode", None)
    if p2p is not None:
        _wrap_after(p2p, "_handle_message", "_g51_orig_hm",
                    lambda layer, a, k, r: layer.observe_p2p(a[0] if a else None,
                                                             a[1] if len(a) > 1 else None))
    return True


def uninstall(host: Any) -> bool:
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g51_orig", None)
    if orig is None:
        return False
    cls.__init__ = orig
    del cls._g51_orig
    mp = getattr(host, "Mempool", None)
    if mp is not None:
        _unwrap(mp, "submit", "_g51_orig_submit")
    p2p = getattr(host, "P2PNode", None)
    if p2p is not None:
        _unwrap(p2p, "_handle_message", "_g51_orig_hm")
    for layer in active_layers():
        layer.detach()
    return True
