"""nebula_group44_install.py - wires NEBULA group44 (20 classes) into the chain.

Usage (host file nebula_v10_11.py and nebula_group44.py must be importable):

    import nebula_v10_11 as host
    import nebula_group44_install as g44
    g44.install(host)                 # every NEBULAFullNode created afterwards gets node.group44
    # ... or attach to an already running node:
    layer = g44.attach(node)
    layer.stats(); layer.coverage(); layer.self_check()
    g44.uninstall(host)               # restores everything exactly as before

Design rules (taken from the group44 guide):
  * nebula_v10_11.py and nebula_group44.py are NEVER edited.
  * The layer is a chain listener: bc.add_listener(layer) -> on_connect / on_reorg.
  * The layer NEVER rejects a block or a transaction. Every callback is wrapped in
    try/except; failures are counted in layer.errors and layer.error_log.
  * First phase is report-only: liquidation scan, risk score, supply check and
    mempool hook only record data. Nothing is liquidated, nothing is executed.
  * All growing buffers are capped.
"""
from __future__ import annotations

import collections
import functools
import hashlib
import hmac
import json
import threading
import time
from decimal import Decimal
from typing import Any, Callable, Deque, Dict, List, Optional, Tuple

import nebula_group44 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

__all__ = [
    "Layer44", "attach", "install", "uninstall", "DEFAULT_OPTIONS",
    "SafeProofOfReserves", "SafeIntegrationTestSuite", "CLASS_MAP",
]

# --------------------------------------------------------------------------- #
# Options                                                                      #
# --------------------------------------------------------------------------- #

DEFAULT_OPTIONS: Dict[str, Any] = {
    "compound_every":        6,      # blocks between PerpetualVaultRegistry.compound_all()
    "scan_every":            6,      # blocks between liquidation scans (report-only)
    "risk_every":            6,      # blocks between ProtocolRiskEngine scoring
    "supply_check_every":    144,    # blocks between supply-schedule vs UTXO comparison
    "dashboard_every":       6,      # blocks between ProtocolStatsDashboard snapshots
    "checkpoint_every":      144,    # blocks between AuditTrail checkpoints
    "supply_drift_alert_pct": 1.0,   # alert (report-only) when drift is above this percent
    "alerts_cap":            200,
    "error_log_cap":         100,
    "fee_history_cap":       2048,   # heights remembered for fee roll-back on reorg
    "hook_mempool":          True,   # count-only wrapper around Mempool.submit
}

# --------------------------------------------------------------------------- #
# Class map: where every one of the 20 classes lives in the wiring             #
# --------------------------------------------------------------------------- #
# (class name, attribute on layer, mode, role)
#   active  = driven by the chain listener
#   passive = live instance ready for on-demand calls (API / CLI / other layers)
#   linked  = no own instance; created and used by another wired class
#   ondemand= never run automatically (tests)

CLASS_MAP: List[Tuple[str, str, str, str]] = [
    ("PositionManager",           "position_manager",    "passive",  "utility"),
    ("LiquidationEngine",         "liquidation_engine",  "active",   "monitor (report-only scan)"),
    ("EVMBridge",                 "evm_bridge",          "passive",  "reads live height/balances from the chain"),
    ("StakedNBL",                 "staked_nbl",          "passive",  "utility (optional StakingEngine)"),
    ("ProtocolStatsDashboard",    "stats_dashboard",     "active",   "periodic snapshot"),
    ("IntegrationTestSuite",      "integration_suite",   "ondemand", "tests on separate chains only"),
    ("ProofOfReserves",           "proof_of_reserves",   "passive",  "utility (fixed verify)"),
    ("TreasuryBond",              "bond_market",         "linked",   "data type used by TreasuryBondMarket"),
    ("TreasuryBondMarket",        "bond_market",         "passive",  "contract/economy state"),
    ("RewardsDistributor",        "rewards_distributor", "passive",  "uses host MerkleTree"),
    ("FeeSharing",                "fee_sharing",         "active",   "fed with block fees, rolled back on reorg"),
    ("GovernanceForum",           "forum",               "passive",  "off-chain signalling"),
    ("PerpetualVault",            "vault_registry",      "linked",   "4 vaults created by the registry"),
    ("PerpetualVaultRegistry",    "vault_registry",      "active",   "compounded on a block cadence"),
    ("ChainGovernanceParameter",  "chain_governance",    "linked",   "5 parameters created by ChainGovernance"),
    ("ChainGovernance",           "chain_governance",    "passive",  "report-only (never applies to consensus)"),
    ("AuditTrail",                "audit_trail",         "active",   "checkpoints, reorgs, risk alerts"),
    ("RiskLevel",                 "risk_engine",         "linked",   "enum used by ProtocolRiskEngine"),
    ("ProtocolRiskEngine",        "risk_engine",         "active",   "periodic scoring"),
    ("SupplyScheduleEngine",      "supply_engine",       "active",   "periodic comparison with UTXO supply"),
]

# --------------------------------------------------------------------------- #
# Fixed subclasses (original group44 file stays untouched)                    #
# --------------------------------------------------------------------------- #

class SafeProofOfReserves(g.ProofOfReserves):
    """ProofOfReserves with a verify_proof that actually works.

    Original bug: generate_proof hashes the raw integers, but verify_proof hashes the
    formatted strings ("1.000000000 NBL"), so verification was always False.
    Fix: the proof additionally carries raw integers; the hash formula is unchanged,
    so proofs stay compatible with the original generate_proof.
    """

    def generate_proof(self, custodian: str, liabilities: Dict[str, int]) -> dict:
        total_liab = int(sum(liabilities.values()))
        total_assets = int(self._bc.utxo.balance(custodian))
        height = self._bc.height
        proof_hash = hashlib.sha256(
            json.dumps({"custodian": custodian, "liabilities": total_liab,
                        "assets": total_assets, "block": height},
                       sort_keys=True).encode()
        ).hexdigest()
        proof = {
            "custodian":        custodian,
            "total_assets":     f"{total_assets / 10**g.DECIMALS:.9f} NBL",
            "total_liab":       f"{total_liab / 10**g.DECIMALS:.9f} NBL",
            "total_assets_raw": total_assets,
            "total_liab_raw":   total_liab,
            "solvent":          total_assets >= total_liab,
            "surplus_nbl":      f"{max(0, total_assets - total_liab) / 10**g.DECIMALS:.9f}",
            "block_height":     height,
            "proof_hash":       proof_hash,
            "timestamp":        time.time(),
        }
        with self._lock:
            self._snapshots.append(proof)
        return proof

    @staticmethod
    def _parse_nbl(text: str) -> int:
        return int(Decimal(str(text).split()[0]) * (10 ** g.DECIMALS))

    def verify_proof(self, proof: dict) -> bool:
        try:
            assets = proof.get("total_assets_raw")
            liab = proof.get("total_liab_raw")
            if assets is None:
                assets = self._parse_nbl(proof["total_assets"])
            if liab is None:
                liab = self._parse_nbl(proof["total_liab"])
            expected = hashlib.sha256(
                json.dumps({"custodian": proof["custodian"], "liabilities": int(liab),
                            "assets": int(assets), "block": proof["block_height"]},
                           sort_keys=True).encode()
            ).hexdigest()
            if not hmac.compare_digest(expected, str(proof.get("proof_hash", ""))):
                return False
            return bool(proof.get("solvent")) == (int(assets) >= int(liab))
        except Exception:
            return False


class SafeIntegrationTestSuite(g.IntegrationTestSuite):
    """IntegrationTestSuite with the undefined-name bug fixed.

    Original bug: test_complete_defi_journey used `stk.stake(...)` but `stk` was never
    defined (NameError, always recorded as FAIL). Fix: create a StakedNBL for the
    separate test chain. The tests only ever use their own NEBULABlockchain instances,
    never the live chain.
    """

    def test_complete_defi_journey(self):
        print("\n\U0001F3E6 Complete DeFi Journey")
        try:
            bc = g.NEBULABlockchain()
            bc._dev_mode = True
            bc.fund_address(g.FOUNDATION_ADDRESS, 100_000)
            stk = g.StakedNBL(bc)
            ok, m = stk.stake(g.FOUNDATION_ADDRESS, 1_000 * 10**g.DECIMALS)
            assert ok, m
            self._ok("Stake NBL", m)
            gov = g.GovernanceEngine(bc)
            ok2, pid = gov.propose(g.FOUNDATION_ADDRESS, g.ProposalType.TEXT,
                                   "Test", "Integration test", {})
            assert ok2, pid
            self._ok("Create governance proposal", pid)
            ok3, m3 = gov.cast_vote(g.FOUNDATION_ADDRESS, pid, "yes")
            assert ok3, m3
            self._ok("Cast governance vote", m3)
            dex = g.NEBULADex(bc)
            pid2 = dex.create_pool("NBL", "USDT", fee_bps=30)
            assert pid2
            self._ok("Create DEX pool", pid2)
        except Exception as e:
            self._fail("DeFi journey", str(e))


# --------------------------------------------------------------------------- #
# The layer                                                                    #
# --------------------------------------------------------------------------- #

class Layer44:
    """Chain listener that owns every group44 service for one node."""

    def __init__(self, node: Any, **options: Any):
        unknown = set(options) - set(DEFAULT_OPTIONS)
        if unknown:
            raise TypeError(f"Unknown Layer44 option(s): {sorted(unknown)}")
        self.node = node
        self.bc = node.bc
        self.opts: Dict[str, Any] = {**DEFAULT_OPTIONS, **options}

        self._lock = threading.RLock()
        self.errors = 0
        self.step_errors: Dict[str, int] = collections.defaultdict(int)
        self.error_log: Deque[Tuple[float, str, str]] = collections.deque(
            maxlen=self.opts["error_log_cap"])
        self.alerts: Deque[dict] = collections.deque(maxlen=self.opts["alerts_cap"])

        self.blocks_seen = 0
        self.reorgs = 0
        self.last_height: Optional[int] = None
        self.last_block_id: Optional[str] = None
        self.latest: Dict[str, Any] = {}
        self.mempool_stats = {"submitted": 0, "accepted": 0, "rejected": 0, "unknown": 0}

        self._last_run: Dict[str, int] = {}
        self._fees_by_height: "collections.OrderedDict[int, int]" = collections.OrderedDict()
        self._last_risk_level: Optional[str] = None
        self.detached = False

        self.services: Dict[str, Any] = {}
        self.build_errors: Dict[str, str] = {}
        self._build_services()

        self._periodic: List[Tuple[str, str, Callable[[int], None]]] = [
            ("compound",         "compound_every",     self._step_compound),
            ("liquidation_scan", "scan_every",         self._step_liquidation_scan),
            ("risk",             "risk_every",         self._step_risk),
            ("supply_check",     "supply_check_every", self._step_supply_check),
            ("dashboard",        "dashboard_every",    self._step_dashboard),
            ("checkpoint",       "checkpoint_every",   self._step_checkpoint),
        ]

    # ----- construction ---------------------------------------------------- #

    def _build_services(self) -> None:
        bc = self.bc
        oracle = getattr(self.node, "oracle", None) or getattr(bc, "oracle", None)
        staking = (getattr(self.node, "staking", None)
                   or getattr(self.node, "staking_engine", None))
        factories: List[Tuple[str, Callable[[], Any]]] = [
            ("audit_trail",         lambda: g.AuditTrail(bc)),
            ("position_manager",    lambda: g.PositionManager(bc, oracle)),
            ("liquidation_engine",  lambda: g.LiquidationEngine(bc, oracle)),
            ("evm_bridge",          lambda: g.EVMBridge(bc)),
            ("staked_nbl",          lambda: g.StakedNBL(bc, staking)),
            ("stats_dashboard",     lambda: g.ProtocolStatsDashboard(bc)),
            ("proof_of_reserves",   lambda: SafeProofOfReserves(bc)),
            ("bond_market",         lambda: g.TreasuryBondMarket(bc)),
            ("rewards_distributor", lambda: g.RewardsDistributor(bc)),
            ("fee_sharing",         lambda: g.FeeSharing(bc)),
            ("forum",               lambda: g.GovernanceForum(bc)),
            ("vault_registry",      lambda: g.PerpetualVaultRegistry(bc)),
            ("chain_governance",    lambda: g.ChainGovernance(bc)),
            ("risk_engine",         lambda: g.ProtocolRiskEngine(bc)),
            ("supply_engine",       lambda: g.SupplyScheduleEngine(bc)),
            ("integration_suite",   lambda: SafeIntegrationTestSuite()),
        ]
        for name, factory in factories:
            try:
                self.services[name] = factory()
            except Exception as e:  # one failing class must never block the others
                self.build_errors[name] = repr(e)
                self._record_error(f"build:{name}", e)

    def __getattr__(self, name: str) -> Any:
        # layer.fee_sharing, layer.risk_engine, ... -> the live service object
        services = self.__dict__.get("services")
        if services is not None and name in services:
            return services[name]
        raise AttributeError(name)

    # ----- error handling -------------------------------------------------- #

    def _record_error(self, step: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.step_errors[step] += 1
            self.error_log.append((time.time(), step, repr(exc)))

    def _run(self, step: str, fn: Callable[..., Any], *a: Any, **k: Any) -> Any:
        try:
            return fn(*a, **k)
        except Exception as e:
            self._record_error(step, e)
            return None

    def _alert(self, kind: str, **data: Any) -> None:
        with self._lock:
            self.alerts.append({"t": time.time(), "kind": kind,
                                "height": self.last_height, **data})

    # ----- chain listener interface --------------------------------------- #

    def on_connect(self, block: Any) -> None:
        if self.detached:
            return
        try:
            with self._lock:
                height = int(self.bc.height)
                self.blocks_seen += 1
                self.last_height = height
                self.last_block_id = self._block_id(block)
                self._run("fees", self._track_fees, block, height)
                self._run_periodic(height, force=False)
        except Exception as e:  # last line of defence: never leak into the chain
            self._record_error("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        if self.detached:
            return
        try:
            with self._lock:
                self.reorgs += 1
                self._run("reorg_fees", self._rollback_fees, ancestor_height)
                self._run("reorg_vaults", self._clamp_vault_clocks)
                self._run("reorg_audit", self._audit_reorg, old, new, ancestor_height)
                # cadence clocks above the ancestor are stale
                for k, v in list(self._last_run.items()):
                    if v > ancestor_height:
                        self._last_run[k] = ancestor_height
                self.last_height = int(self.bc.height)
        except Exception as e:
            self._record_error("on_reorg", e)

    def detach(self) -> None:
        self.detached = True
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer44.detach", exc_info=True)
        _MEMPOOL_LAYERS.pop(id(getattr(self.bc, "mempool", None)), None)

    # ----- periodic work --------------------------------------------------- #

    def refresh(self) -> None:
        """Run every periodic step once now (also used right after attach)."""
        with self._lock:
            height = int(self.bc.height)
            self.last_height = height
            self._run_periodic(height, force=True)

    def _due(self, name: str, every: int, height: int) -> bool:
        last = self._last_run.get(name)
        return last is None or height < last or height - last >= max(1, int(every))

    def _run_periodic(self, height: int, force: bool) -> None:
        for name, opt, fn in self._periodic:
            if force or self._due(name, self.opts[opt], height):
                self._last_run[name] = height
                self._run(name, fn, height)

    def _step_compound(self, height: int) -> None:
        reg = self.services.get("vault_registry")
        if reg is not None:
            self.latest["vault_compound"] = reg.compound_all()

    def _step_liquidation_scan(self, height: int) -> None:
        eng = self.services.get("liquidation_engine")
        if eng is None:
            return
        under = eng.scan_for_liquidations()          # report-only: never liquidate
        self.latest["underwater_positions"] = under
        if under:
            self._alert("underwater_positions", count=len(under))

    def _step_risk(self, height: int) -> None:
        eng = self.services.get("risk_engine")
        if eng is None:
            return
        report = eng.overall_risk_score()
        self.latest["risk"] = report
        level = report.get("risk_level")
        if level != self._last_risk_level:
            previous, self._last_risk_level = self._last_risk_level, level
            if level in ("high", "critical"):
                self._alert("risk_level", level=level, previous=previous,
                            score=report.get("overall_score"))
                self._audit("risk_alert", "risk_engine", f"level={level}",
                            {"score": report.get("overall_score"), "previous": previous})

    def _step_supply_check(self, height: int) -> None:
        eng = self.services.get("supply_engine")
        if eng is None:
            return
        expected = int(eng.supply_at_block(height))
        actual = int(self.bc.utxo.total_supply())
        drift = actual - expected
        pct = (abs(drift) / expected * 100.0) if expected else 0.0
        self.latest["supply_check"] = {
            "height": height, "expected": expected, "actual": actual,
            "drift": drift, "drift_pct": round(pct, 6),
        }
        if pct > float(self.opts["supply_drift_alert_pct"]):
            self._alert("supply_drift", drift=drift, drift_pct=round(pct, 6))

    def _step_dashboard(self, height: int) -> None:
        dash = self.services.get("stats_dashboard")
        if dash is not None:
            self.latest["dashboard"] = dash.full_stats()

    def _step_checkpoint(self, height: int) -> None:
        self._audit("chain_checkpoint", "layer44", "checkpoint",
                    {"height": height, "block": self.last_block_id})

    # ----- helpers --------------------------------------------------------- #

    def _audit(self, event_type: str, actor: str, action: str, details: dict) -> None:
        trail = self.services.get("audit_trail")
        if trail is not None:
            self._run("audit", trail.log, event_type, actor, action, details)

    def _audit_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        def size(x: Any) -> Optional[int]:
            try:
                return len(x)
            except TypeError:
                return None
        self._audit("chain_reorg", "layer44", "reorg",
                    {"ancestor_height": ancestor_height,
                     "old_blocks": size(old), "new_blocks": size(new)})

    @staticmethod
    def _block_id(block: Any) -> Optional[str]:
        for attr in ("hash", "block_hash", "id"):
            v = getattr(block, attr, None)
            if callable(v):
                try:
                    v = v()
                except Exception:
                    v = None
            if v:
                return v.hex() if isinstance(v, (bytes, bytearray)) else str(v)
        return None

    @staticmethod
    def _block_fees(block: Any) -> int:
        txs = getattr(block, "txs", None)
        if txs is None:
            txs = getattr(block, "transactions", None)
        total = 0
        for tx in txs or []:
            try:
                total += int(getattr(tx, "fee", 0) or 0)
            except (TypeError, ValueError):
                continue
        return total

    def _track_fees(self, block: Any, height: int) -> None:
        fees = self._block_fees(block)
        fs = self.services.get("fee_sharing")
        if fs is None:
            return
        if fees > 0:
            fs.accumulate(fees)
        self._fees_by_height[height] = fees
        while len(self._fees_by_height) > int(self.opts["fee_history_cap"]):
            self._fees_by_height.popitem(last=False)

    def _rollback_fees(self, ancestor_height: int) -> None:
        fs = self.services.get("fee_sharing")
        if fs is None:
            return
        for h in [h for h in self._fees_by_height if h > ancestor_height]:
            fees = self._fees_by_height.pop(h)
            if fees:
                fs.accumulate(-fees)

    def _clamp_vault_clocks(self) -> None:
        reg = self.services.get("vault_registry")
        if reg is None:
            return
        height = int(self.bc.height)
        for vault in reg._vaults.values():
            if vault._last_compound > height:
                vault._last_compound = height

    def _on_mempool_submit(self, result: Any) -> None:
        with self._lock:
            self.mempool_stats["submitted"] += 1
            if isinstance(result, (tuple, list)) and result:
                self.mempool_stats["accepted" if result[0] else "rejected"] += 1
            else:
                self.mempool_stats["unknown"] += 1

    # ----- public reporting ------------------------------------------------ #

    def coverage(self) -> dict:
        """Where each of the 20 classes is wired, with proof that a live object exists."""
        rows = []
        for cls_name, attr, mode, role in CLASS_MAP:
            svc = self.services.get(attr)
            live = svc is not None
            if cls_name == "PerpetualVault" and live:
                live = any(isinstance(v, g.PerpetualVault) for v in svc._vaults.values())
            elif cls_name == "ChainGovernanceParameter" and live:
                live = any(isinstance(v, g.ChainGovernanceParameter)
                           for v in svc._params.values())
            elif cls_name == "TreasuryBond":
                live = svc is not None and hasattr(g, "TreasuryBond")
            elif cls_name == "RiskLevel":
                live = svc is not None and hasattr(g, "RiskLevel")
            rows.append({"class": cls_name, "attr": attr, "mode": mode,
                         "role": role, "wired": bool(live)})
        return {"all_wired": all(r["wired"] for r in rows),
                "wired": sum(r["wired"] for r in rows),
                "total": len(rows), "classes": rows,
                "build_errors": dict(self.build_errors)}

    def self_check(self) -> dict:
        """Read-only smoke test of every service against the live chain."""
        s = self.services
        checks: List[Tuple[str, Callable[[], Any]]] = [
            ("PositionManager",       lambda: s["position_manager"].portfolio_overview("__selfcheck__")),
            ("LiquidationEngine",     lambda: s["liquidation_engine"].liquidation_stats()),
            ("EVMBridge",             lambda: (s["evm_bridge"].eth_block_number(), s["evm_bridge"].evm_stats())),
            ("StakedNBL",             lambda: s["staked_nbl"].stnbl_stats()),
            ("ProtocolStatsDashboard", lambda: s["stats_dashboard"].summary()),
            ("ProofOfReserves",       lambda: s["proof_of_reserves"].history()),
            ("TreasuryBondMarket",    lambda: s["bond_market"].bond_market_stats()),
            ("RewardsDistributor",    lambda: s["rewards_distributor"].distributor_stats()),
            ("FeeSharing",            lambda: s["fee_sharing"].fee_sharing_stats()),
            ("GovernanceForum",       lambda: s["forum"].forum_stats()),
            ("PerpetualVaultRegistry", lambda: s["vault_registry"].all_vaults()),
            ("ChainGovernance",       lambda: s["chain_governance"].get_params()),
            ("AuditTrail",            lambda: s["audit_trail"].audit_stats()),
            ("ProtocolRiskEngine",    lambda: s["risk_engine"].overall_risk_score()),
            ("SupplyScheduleEngine",  lambda: s["supply_engine"].supply_stats()),
        ]
        results: Dict[str, str] = {}
        for name, fn in checks:
            try:
                fn()
                results[name] = "ok"
            except Exception as e:
                results[name] = f"FAIL: {e!r}"
        return {"ok": all(v == "ok" for v in results.values()), "results": results}

    def stats(self) -> dict:
        s = self.services
        def safe(step: str, fn: Callable[[], Any]) -> Any:
            return self._run(step, fn)
        with self._lock:
            return {
                "layer": {
                    "errors": self.errors,
                    "blocks_seen": self.blocks_seen,
                    "reorgs": self.reorgs,
                    "last_height": self.last_height,
                    "last_block_id": self.last_block_id,
                    "alerts": len(self.alerts),
                    "mempool": dict(self.mempool_stats),
                    "detached": self.detached,
                },
                "latest": dict(self.latest),
                "liquidation": safe("stats:liq", s["liquidation_engine"].liquidation_stats) if "liquidation_engine" in s else None,
                "evm": safe("stats:evm", s["evm_bridge"].evm_stats) if "evm_bridge" in s else None,
                "staking": safe("stats:stnbl", s["staked_nbl"].stnbl_stats) if "staked_nbl" in s else None,
                "bonds": safe("stats:bonds", s["bond_market"].bond_market_stats) if "bond_market" in s else None,
                "rewards": safe("stats:rewards", s["rewards_distributor"].distributor_stats) if "rewards_distributor" in s else None,
                "fee_sharing": safe("stats:fees", s["fee_sharing"].fee_sharing_stats) if "fee_sharing" in s else None,
                "forum": safe("stats:forum", s["forum"].forum_stats) if "forum" in s else None,
                "vaults": safe("stats:vaults", s["vault_registry"].all_vaults) if "vault_registry" in s else None,
                "governance_params": safe("stats:gov", s["chain_governance"].get_params) if "chain_governance" in s else None,
                "audit": safe("stats:audit", s["audit_trail"].audit_stats) if "audit_trail" in s else None,
                "supply": safe("stats:supply", s["supply_engine"].supply_stats) if "supply_engine" in s else None,
            }

    def run_integration_tests(self) -> dict:
        """On demand only. Uses separate NEBULABlockchain instances, never the live chain."""
        suite = SafeIntegrationTestSuite()
        return suite.run_all()


# --------------------------------------------------------------------------- #
# install / uninstall                                                          #
# --------------------------------------------------------------------------- #

_MEMPOOL_LAYERS: Dict[int, Layer44] = {}
_LIVE_LAYERS: List[Layer44] = []
_INSTALL_OPTIONS: Dict[str, Any] = {}


def attach(node: Any, **options: Any) -> Layer44:
    """Create the layer for `node`, register it as a chain listener, return it.
    Safe to call twice: the second call returns the existing layer."""
    existing = getattr(node, "group44", None)
    if isinstance(existing, Layer44) and not existing.detached:
        return existing
    layer = Layer44(node, **{**_INSTALL_OPTIONS, **options})
    node.bc.add_listener(layer)
    node.group44 = layer
    _LIVE_LAYERS.append(layer)
    if layer.opts["hook_mempool"]:
        mp = getattr(node.bc, "mempool", None)
        if mp is not None:
            _MEMPOOL_LAYERS[id(mp)] = layer
    layer.refresh()
    return layer


def _patch_mempool(host: Any) -> bool:
    cls = getattr(host, "Mempool", None)
    if cls is None or getattr(cls, "_g44_submit_orig", None) is not None:
        return False
    orig = cls.submit

    @functools.wraps(orig)
    def patched(self: Any, *a: Any, **k: Any) -> Any:
        result = orig(self, *a, **k)          # exceptions/results exactly as before
        try:
            layer = _MEMPOOL_LAYERS.get(id(self))
            if layer is not None:
                layer._on_mempool_submit(result)
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in _patch_mempool.patched", exc_info=True)
        return result

    cls._g44_submit_orig = orig
    cls.submit = patched
    return True


def install(host: Any, **options: Any) -> None:
    """Wrap NEBULAFullNode.__init__ so every new node gets node.group44."""
    unknown = set(options) - set(DEFAULT_OPTIONS)
    if unknown:
        raise TypeError(f"Unknown Layer44 option(s): {sorted(unknown)}")
    cls = host.NEBULAFullNode
    if getattr(cls, "_g44_orig", None):
        return
    _INSTALL_OPTIONS.clear()
    _INSTALL_OPTIONS.update(options)
    orig = cls.__init__

    @functools.wraps(orig)
    def patched(self: Any, *a: Any, **k: Any) -> None:
        orig(self, *a, **k)
        try:
            attach(self)
        except Exception as e:                 # the node must still start
            self.group44_error = e

    cls._g44_orig = orig
    cls.__init__ = patched
    if DEFAULT_OPTIONS["hook_mempool"] and options.get("hook_mempool", True):
        _patch_mempool(host)


def uninstall(host: Any) -> None:
    """Undo install(): restore __init__ and Mempool.submit, detach every live layer."""
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g44_orig", None)
    if orig:
        cls.__init__ = orig
        del cls._g44_orig
    mp_cls = getattr(host, "Mempool", None)
    mp_orig = getattr(mp_cls, "_g44_submit_orig", None) if mp_cls else None
    if mp_orig:
        mp_cls.submit = mp_orig
        del mp_cls._g44_submit_orig
    for layer in list(_LIVE_LAYERS):
        layer.detach()
        node_layer = getattr(layer.node, "group44", None)
        if node_layer is layer:
            try:
                del layer.node.group44
            except AttributeError:
                _NB_SWALLOW_LOG.debug("swallowed AttributeError in uninstall", exc_info=True)
    _LIVE_LAYERS.clear()
    _MEMPOOL_LAYERS.clear()
    _INSTALL_OPTIONS.clear()
