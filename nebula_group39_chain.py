"""NEBULA group39 - chain wiring hub.

This module wires the 20 classes of ``nebula_group39.py`` into ONE ordered chain.
It does NOT edit ``nebula_group39.py`` or ``nebula_v10_11.py``.

Chain layout (build order = dependency order)
---------------------------------------------
Level 0  value types (no dependencies)
         NodeType, BridgeProtocol, TreasuryProposalType,
         SlashingCondition, ContractTemplate
Level 1  data types (depend on level 0)
         NodeInfo, BridgeTransfer, TreasuryProposal, DeployedContract
Level 2  stateless utilities
         ContractStdLib, AddressFormatter, TaprootScript
Level 3  chain-aware services (take the blockchain)
         StateProof, SupplyAnalytics, NodeRegistry, PrivacyMixerManager
         (-> 4 x CoinMixPool), TokenBridgeV2, SlashingConditionsEngine
Level 4  services that need a level-3 / host object
         TreasuryGovernanceV2 (needs the host treasury)
Level 5  glue
         ContractRegistry (DeployedContract + ContractTemplate + TaprootScript)

Cross links created here
------------------------
* AddressFormatter + ContractStdLib validate every address that enters
  NodeRegistry, the mixer, the bridge, the treasury and the contract registry.
* TokenBridgeV2.initiate  -> StateProof.prove_balance  (balance receipt)
* TokenBridgeV2 fee quote -> ContractStdLib.percentage
* SlashingConditionsEngine -> NodeRegistry (score penalty on slashed operator)
* TreasuryGovernanceV2 quorum preview -> SupplyAnalytics + ContractStdLib
* ContractRegistry -> TaprootScript (MAST root = bytecode hash, taproot address)
* Block listener (on_connect / on_reorg) -> StateProof commitments,
  tracked-address proofs, NodeRegistry pings, SupplyAnalytics snapshots,
  and a stats report from every service.

Safety rules (from the group39 guide)
-------------------------------------
* Nothing here ever rejects a block or a transaction.
* Every stage / facade call is wrapped; failures are counted, never raised.
* ``report_only=True`` (default): evidence is stored but NOT processed while a
  real PoS engine is attached, so no real stake is slashed until you decide.
"""
from __future__ import annotations

import hashlib
import json
import threading
import time
from collections import deque
from typing import Any, Deque, Dict, List, Optional, Tuple
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

try:
    import nebula_group39 as g
except NameError as exc:  # host classes (AddressType, MerkleTree, ...) missing
    raise ImportError(
        "nebula_group39 could not be imported: put nebula_v10_11.py in the same "
        "folder so the cross-group names (AddressType, KeyBlinding, MerkleTree, "
        "SlashingEvidence) can be resolved. Original error: %s" % exc
    ) from exc


# --------------------------------------------------------------------------
# Static description of the chain (used by wiring_report and by the tests)
# --------------------------------------------------------------------------
BUILD_ORDER: Tuple[Tuple[int, str, str], ...] = (
    # (level, class name, role)
    (0, "NodeType",                 "value type: kind of network node"),
    (0, "BridgeProtocol",           "value type: bridge protocol"),
    (0, "TreasuryProposalType",     "value type: treasury proposal kind"),
    (0, "SlashingCondition",        "value type: slashing reason"),
    (0, "ContractTemplate",         "value type: contract template"),
    (1, "NodeInfo",                 "data: one registered node"),
    (1, "BridgeTransfer",           "data: one bridge transfer"),
    (1, "TreasuryProposal",         "data: one treasury proposal"),
    (1, "DeployedContract",         "data: one deployed contract"),
    (2, "ContractStdLib",           "utility: safe math / address checks"),
    (2, "AddressFormatter",         "utility: address encode / decode / validate"),
    (2, "TaprootScript",            "utility: MAST script commitments"),
    (3, "StateProof",               "service: light-client state proofs"),
    (3, "SupplyAnalytics",          "service: supply / rich list / gini"),
    (3, "NodeRegistry",             "service: on-chain node registry"),
    (3, "CoinMixPool",              "service: one mixing pool (built by the manager)"),
    (3, "PrivacyMixerManager",      "service: owns one CoinMixPool per denomination"),
    (3, "TokenBridgeV2",            "service: multi-chain bridge"),
    (3, "SlashingConditionsEngine", "service: slashing evidence engine"),
    (4, "TreasuryGovernanceV2",     "service: token-weighted treasury votes"),
)

# class -> (fed by, feeds)
LINKS: Dict[str, Tuple[Tuple[str, ...], Tuple[str, ...]]] = {
    "NodeType":                 ((), ("NodeInfo", "NodeRegistry")),
    "BridgeProtocol":           ((), ("BridgeTransfer", "TokenBridgeV2")),
    "TreasuryProposalType":     ((), ("TreasuryProposal", "TreasuryGovernanceV2")),
    "SlashingCondition":        ((), ("SlashingConditionsEngine",)),
    "ContractTemplate":         ((), ("DeployedContract", "ContractRegistry")),
    "NodeInfo":                 (("NodeType",), ("NodeRegistry",)),
    "BridgeTransfer":           (("BridgeProtocol",), ("TokenBridgeV2",)),
    "TreasuryProposal":         (("TreasuryProposalType",), ("TreasuryGovernanceV2",)),
    "DeployedContract":         (("ContractTemplate",), ("ContractRegistry",)),
    "ContractStdLib":           ((), ("AddressValidation", "TokenBridgeV2", "TreasuryGovernanceV2", "ContractRegistry")),
    "AddressFormatter":         ((), ("AddressValidation",)),
    "TaprootScript":            ((), ("ContractRegistry",)),
    "StateProof":               (("block listener",), ("TokenBridgeV2 receipts", "tracked addresses")),
    "SupplyAnalytics":          (("block listener",), ("TreasuryGovernanceV2 quorum preview",)),
    "NodeRegistry":             (("NodeType", "NodeInfo", "AddressValidation", "SlashingConditionsEngine"), ("block listener ping",)),
    "CoinMixPool":              (("PrivacyMixerManager",), ("mix history",)),
    "PrivacyMixerManager":      (("AddressValidation",), ("CoinMixPool",)),
    "TokenBridgeV2":            (("BridgeProtocol", "BridgeTransfer", "AddressValidation"), ("StateProof receipt",)),
    "SlashingConditionsEngine": (("SlashingCondition",), ("NodeRegistry score penalty",)),
    "TreasuryGovernanceV2":     (("TreasuryProposalType", "TreasuryProposal", "AddressValidation"), ("treasury log",)),
}


class _NullTreasury:
    """Used only when the host node exposes no treasury object.

    Every proposal is rejected ("Amount exceeds treasury balance") until a real
    treasury is attached with ``Group39Chain.attach_treasury``.
    """

    def balance(self) -> int:
        return 0


class ContractRegistry:
    """Glue: DeployedContract + ContractTemplate + TaprootScript + ContractStdLib.

    The contract bytecode hash is the MAST root of two script leaves
    (the code blob and a metadata leaf), so every deployed contract can later be
    verified with a Merkle spend proof produced by TaprootScript.
    """

    def __init__(self, blockchain, taproot, stdlib):
        self._bc = blockchain
        self._taproot = taproot
        self._std = stdlib
        self._contracts: Dict[str, Any] = {}
        self._trees: Dict[str, str] = {}      # contract_id -> taproot tree id
        self._tapkeys: Dict[str, str] = {}    # contract_id -> taproot key
        self._lock = threading.RLock()

    def deploy(self, template, deployer: str, params: dict,
               code: bytes = b"") -> Tuple[bool, Any]:
        with self._lock:
            params = dict(params or {})
            blob = json.dumps(
                {"template": template.value, "params": params},
                sort_keys=True, default=str).encode()
            leaves = [b"CODE:" + (code or blob),
                      b"META:" + template.value.encode() + b":" + deployer.encode()]
            root, tapkey = self._taproot.build_mast(leaves)
            height = int(self._bc.height)
            contract_id = self._std.keccak256(
                f"{template.value}|{deployer}|{height}|{root}".encode()
            ).hex()[:40]
            if contract_id in self._contracts:
                return False, "Contract already deployed"
            contract = g.DeployedContract(
                contract_id=contract_id,
                template=template,
                deployer=deployer,
                params=params,
                deployed_at=time.time(),
                block_height=height,
                bytecode_hash=root,
            )
            self._contracts[contract_id] = contract
            self._trees[contract_id] = tapkey[:16]
            self._tapkeys[contract_id] = tapkey
            return True, contract

    def verify(self, contract_id: str) -> Tuple[bool, str]:
        with self._lock:
            contract = self._contracts.get(contract_id)
            if contract is None:
                return False, "Unknown contract"
            proof = self._taproot.create_spend_proof(self._trees[contract_id], 0)
            if not proof or proof.get("root") != contract.bytecode_hash:
                return False, "Bytecode commitment mismatch"
            if not self._taproot.verify_spend_proof(proof):
                return False, "Spend proof failed"
            contract.verified = True
            return True, "verified"

    def address(self, contract_id: str) -> Optional[str]:
        with self._lock:
            contract = self._contracts.get(contract_id)
            if contract is None:
                return None
            internal_key = hashlib.sha256(contract_id.encode()).digest()
            return self._taproot.taproot_address(internal_key, contract.bytecode_hash)

    def get(self, contract_id: str):
        with self._lock:
            return self._contracts.get(contract_id)

    def list(self) -> List[dict]:
        with self._lock:
            return [c.to_dict() for c in self._contracts.values()]

    def stats(self) -> dict:
        with self._lock:
            by_template: Dict[str, int] = {}
            for c in self._contracts.values():
                by_template[c.template.value] = by_template.get(c.template.value, 0) + 1
            return {
                "total_contracts": len(self._contracts),
                "verified": sum(1 for c in self._contracts.values() if c.verified),
                "by_template": by_template,
            }


class Group39Chain:
    """Builds and connects all 20 group39 classes. See module docstring."""

    SNAPSHOT_INTERVAL = 100      # blocks between supply snapshots
    HISTORY_CAP = 2048           # cap for every in-RAM history list
    TRACKED_CAP = 64             # max tracked addresses

    STAGES = ("state", "registry", "supply", "bridge",
              "treasury", "slashing", "mixer", "contracts")

    def __init__(self, blockchain, pos_engine=None, treasury=None,
                 report_only: bool = True, strict_addresses: bool = True):
        self.bc = blockchain
        self.pos_engine = pos_engine
        self.report_only = bool(report_only)
        self.strict_addresses = bool(strict_addresses)

        self.errors = 0
        self.last_error: Optional[str] = None
        self.stage_errors: Dict[str, int] = {s: 0 for s in self.STAGES}
        self.reorgs = 0
        self.blocks_seen = 0
        self._lock = threading.RLock()

        self._ensure_slashing_evidence_class()

        # ---- Level 0 / 1: types (resolved and verified, not instantiated) ----
        self.NodeType = g.NodeType
        self.NodeInfo = g.NodeInfo
        self.BridgeProtocol = g.BridgeProtocol
        self.BridgeTransfer = g.BridgeTransfer
        self.TreasuryProposalType = g.TreasuryProposalType
        self.TreasuryProposal = g.TreasuryProposal
        self.SlashingCondition = g.SlashingCondition
        self.ContractTemplate = g.ContractTemplate
        self.DeployedContract = g.DeployedContract

        # ---- Level 2: stateless utilities ----
        self.stdlib = g.ContractStdLib()
        self.address_formatter = g.AddressFormatter()
        self.taproot = g.TaprootScript()

        # ---- Level 3: chain-aware services ----
        self.state_proof = g.StateProof(blockchain)
        self.supply = g.SupplyAnalytics(blockchain)
        self.registry = g.NodeRegistry(blockchain)
        self.mixer = g.PrivacyMixerManager(blockchain)
        self.bridge = g.TokenBridgeV2(blockchain)
        self.slashing = g.SlashingConditionsEngine(pos_engine, blockchain)

        # ---- Level 4: governance (needs the host treasury) ----
        self.treasury = treasury if treasury is not None else _NullTreasury()
        self.has_real_treasury = treasury is not None
        self.governance = g.TreasuryGovernanceV2(blockchain, self.treasury)

        # ---- Level 5: glue ----
        self.contracts = ContractRegistry(blockchain, self.taproot, self.stdlib)

        # ---- bounded histories filled by the listener and the facades ----
        self.commitments: Deque[dict] = deque(maxlen=self.HISTORY_CAP)
        self.supply_snapshots: Deque[dict] = deque(maxlen=self.HISTORY_CAP)
        self.mix_history: Deque[dict] = deque(maxlen=self.HISTORY_CAP)
        self.bridge_receipts: Dict[str, dict] = {}
        self.treasury_log: Deque[dict] = deque(maxlen=self.HISTORY_CAP)
        self.slash_log: Deque[dict] = deque(maxlen=self.HISTORY_CAP)
        self.tracked: Dict[str, Optional[dict]] = {}
        self.local_node_ids: List[str] = []
        self.last_report: Dict[str, Any] = {}

    # ------------------------------------------------------------------
    # internal helpers
    # ------------------------------------------------------------------
    @staticmethod
    def _ensure_slashing_evidence_class() -> None:
        """SlashingConditionsEngine.submit_evidence uses ``SlashingEvidenceC``.

        The host normally provides it. If it is missing, build it from the
        helpers that were copied verbatim into nebula_group39.py.
        """
        if getattr(g, "SlashingEvidenceC", None) is not None:
            return
        g.SlashingEvidenceC = g._make_compat(
            g.SlashingEvidence,
            aliases={"condition": "evidence_type"},
            post=g._v108_slash_post,
            name="SlashingEvidenceC",
        )

    def _fail(self, stage: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.stage_errors[stage] = self.stage_errors.get(stage, 0) + 1
            self.last_error = f"{stage}: {type(exc).__name__}: {exc}"

    def _call(self, stage: str, fn, *args, **kwargs) -> Tuple[bool, Any]:
        """Run a facade call; never raise. Returns (ok, payload_or_message)."""
        try:
            return fn(*args, **kwargs)
        except Exception as exc:  # noqa: BLE001 - layer must never break the node
            self._fail(stage, exc)
            return False, f"{type(exc).__name__}: {exc}"

    @staticmethod
    def _coerce_enum(enum_cls, value):
        if isinstance(value, enum_cls):
            return value
        if isinstance(value, str):
            try:
                return enum_cls(value.lower())
            except ValueError:
                _NB_SWALLOW_LOG.debug("swallowed ValueError in Group39Chain._coerce_enum", exc_info=True)
            try:
                return enum_cls[value.upper()]
            except KeyError:
                _NB_SWALLOW_LOG.debug("swallowed KeyError in Group39Chain._coerce_enum", exc_info=True)
        raise ValueError(f"Invalid {enum_cls.__name__}: {value!r}")

    def is_valid_address(self, address: Any) -> bool:
        """AddressFormatter OR ContractStdLib accepts the address."""
        if not isinstance(address, str) or not address:
            return False
        if not self.strict_addresses:
            return True
        try:
            if self.address_formatter.is_valid(address):
                return True
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in Group39Chain.is_valid_address", exc_info=True)
        try:
            return bool(self.stdlib.address_valid(address))
        except Exception:
            return False

    def _need_address(self, label: str, address: Any) -> Optional[str]:
        if self.is_valid_address(address):
            return None
        return f"Invalid {label} address"

    def attach_treasury(self, treasury) -> None:
        """Replace the placeholder treasury and rebuild governance on top of it."""
        with self._lock:
            self.treasury = treasury
            self.has_real_treasury = True
            self.governance = g.TreasuryGovernanceV2(self.bc, treasury)

    # ------------------------------------------------------------------
    # Facade: node registry  (NodeType -> NodeInfo -> NodeRegistry)
    # ------------------------------------------------------------------
    def register_node(self, operator: str, node_type, ip: str, port: int,
                      version: str, services: List[str],
                      local: bool = False) -> Tuple[bool, str]:
        def run():
            bad = self._need_address("operator", operator)
            if bad:
                return False, bad
            ntype = self._coerce_enum(self.NodeType, node_type)
            ok, result = self.registry.register(
                operator, ntype, ip, int(port), version, list(services or []))
            if ok and local and result not in self.local_node_ids:
                self.local_node_ids.append(result)
            return ok, result
        return self._call("registry", run)

    def ping_node(self, node_id: str) -> bool:
        ok, _ = self._call("registry", lambda: (
            self.registry.ping(node_id, int(self.bc.height)), None))
        return bool(ok)

    def deregister_node(self, node_id: str, operator: str) -> bool:
        ok, _ = self._call("registry", lambda: (
            self.registry.deregister(node_id, operator), None))
        return bool(ok)

    def active_nodes(self, node_type=None, max_age_secs: int = 3600) -> List[dict]:
        ok, res = self._call("registry", lambda: (True, self.registry.get_active_nodes(
            self._coerce_enum(self.NodeType, node_type) if node_type else None,
            max_age_secs)))
        return res if ok else []

    # ------------------------------------------------------------------
    # Facade: mixer  (AddressValidation -> PrivacyMixerManager -> CoinMixPool)
    # ------------------------------------------------------------------
    def mix(self, sender: str, amount_nbl: float, output_address: str,
            auto_execute: bool = True) -> Tuple[bool, Any]:
        def run():
            for label, addr in (("sender", sender), ("output", output_address)):
                bad = self._need_address(label, addr)
                if bad:
                    return False, bad
            ok, msg = self.mixer.join_mix(sender, amount_nbl, output_address)
            if not ok:
                return False, msg
            payload: Dict[str, Any] = {"joined": msg, "executed": None}
            denomination = int(amount_nbl * 10 ** g.DECIMALS)
            pool = self.mixer._pools.get(denomination)
            if auto_execute and pool is not None \
                    and pool.pool_info().get("status") == "ready":
                done, result = pool.execute_mix()
                if done:
                    payload["executed"] = result
                    self.mix_history.append(dict(result, executed_at=time.time()))
            return True, payload
        return self._call("mixer", run)

    # ------------------------------------------------------------------
    # Facade: bridge  (BridgeProtocol -> BridgeTransfer -> TokenBridgeV2 -> StateProof)
    # ------------------------------------------------------------------
    def quote_bridge_fee(self, amount_nbl: float) -> int:
        amount = int(amount_nbl * 10 ** g.DECIMALS)
        return self.stdlib.percentage(amount, self.bridge.BRIDGE_FEE_BPS)

    def bridge_out(self, sender: str, dest_chain: str, recipient: str,
                   amount_nbl: float, token: str = "NBL",
                   protocol=None) -> Tuple[bool, Any]:
        def run():
            bad = self._need_address("sender", sender)
            if bad:
                return False, bad
            proto = self._coerce_enum(
                self.BridgeProtocol, protocol or self.BridgeProtocol.LOCK_MINT)
            ok, tid = self.bridge.initiate(
                sender, dest_chain, recipient, amount_nbl, token, proto)
            if not ok:
                return False, tid
            receipt = self.state_proof.prove_balance(sender, int(self.bc.height))
            self.bridge_receipts[tid] = receipt
            return True, {"transfer_id": tid, "receipt": receipt,
                          "fee": self.quote_bridge_fee(amount_nbl)}
        return self._call("bridge", run)

    def bridge_complete(self, transfer_id: str, relay_proof: str) -> Tuple[bool, str]:
        return self._call("bridge", lambda: self.bridge.complete(transfer_id, relay_proof))

    def bridge_add_liquidity(self, chain: str, amount: int) -> bool:
        ok, _ = self._call("bridge", lambda: (
            self.bridge.add_liquidity(chain, int(amount)) is None, None))
        return bool(ok)

    # ------------------------------------------------------------------
    # Facade: treasury  (TreasuryProposalType -> TreasuryProposal -> Governance)
    # ------------------------------------------------------------------
    def propose_treasury(self, proposer: str, ptype, amount_nbl: float,
                         recipient: str, description: str) -> Tuple[bool, str]:
        def run():
            for label, addr in (("proposer", proposer), ("recipient", recipient)):
                bad = self._need_address(label, addr)
                if bad:
                    return False, bad
            kind = self._coerce_enum(self.TreasuryProposalType, ptype)
            return self.governance.propose(
                proposer, kind, amount_nbl, recipient, description)
        return self._call("treasury", run)

    def vote_treasury(self, voter: str, proposal_id: str,
                      support: bool) -> Tuple[bool, str]:
        def run():
            bad = self._need_address("voter", voter)
            if bad:
                return False, bad
            return self.governance.vote(voter, proposal_id, support)
        return self._call("treasury", run)

    def execute_treasury(self, proposal_id: str) -> Tuple[bool, str]:
        def run():
            ok, msg = self.governance.execute(proposal_id)
            if ok:
                prop = self.governance._proposals.get(proposal_id)
                self.treasury_log.append({
                    "proposal_id": proposal_id,
                    "type": prop.ptype.value if prop else None,
                    "amount": prop.amount if prop else 0,
                    "recipient": prop.recipient if prop else None,
                    "executed_at": time.time(),
                    "report_only": True,   # no funds are moved by this layer
                })
            return ok, msg
        return self._call("treasury", run)

    def proposal_status(self, proposal_id: str) -> Optional[dict]:
        """Proposal data plus the quorum still required (SupplyAnalytics + StdLib)."""
        def run():
            prop = self.governance._proposals.get(proposal_id)
            if prop is None:
                return False, "Unknown proposal"
            total_supply = self.bc.utxo.total_supply()
            quorum_bps = int(self.governance.QUORUM_PCT * 10_000)
            need = self.stdlib.percentage(total_supply, quorum_bps) / 10 ** g.DECIMALS
            have = prop.votes_for + prop.votes_against
            data = prop.to_dict()
            data.update({
                "quorum_required": need,
                "votes_cast": have,
                "quorum_met": have >= need,
                "circulating_supply": self.supply.circulating_supply() / 10 ** g.DECIMALS,
            })
            return True, data
        ok, res = self._call("treasury", run)
        return res if ok else None

    # ------------------------------------------------------------------
    # Facade: slashing  (SlashingCondition -> Engine -> NodeRegistry)
    # ------------------------------------------------------------------
    def report_slashing(self, reporter: str, validator: str, condition,
                        evidence_data: Optional[dict] = None,
                        process: bool = True) -> Tuple[bool, Any]:
        def run():
            for label, addr in (("reporter", reporter), ("validator", validator)):
                bad = self._need_address(label, addr)
                if bad:
                    return False, bad
            cond = self._coerce_enum(self.SlashingCondition, condition)
            ok, eid = self.slashing.submit_evidence(
                reporter, validator, cond, dict(evidence_data or {}))
            if not ok:
                return False, eid
            result = {"evidence_id": eid, "processed": False, "message": "stored",
                      "penalised_nodes": []}
            # report-only: never touch a real PoS engine until the owner decides
            may_process = process and (not self.report_only or self.slashing._pos is None)
            if may_process:
                done, msg = self.slashing.process_evidence(eid)
                result["processed"] = bool(done)
                result["message"] = msg
                if done:
                    rate = self.slashing.SLASH_RATES.get(cond, 0.01)
                    result["penalised_nodes"] = self._penalise_operator(validator, rate)
            self.slash_log.append(dict(result, validator=validator,
                                       condition=cond.value, at=time.time()))
            return True, result
        return self._call("slashing", run)

    def _penalise_operator(self, operator: str, rate: float) -> List[str]:
        """Lower the registry score of every node owned by a slashed operator."""
        hit: List[str] = []
        with self.registry._lock:
            for nid, node in self.registry._nodes.items():
                if node.operator == operator:
                    node.score = max(0.0, node.score * (1.0 - rate))
                    hit.append(nid)
        return hit

    # ------------------------------------------------------------------
    # Facade: contracts  (ContractTemplate -> DeployedContract -> ContractRegistry)
    # ------------------------------------------------------------------
    def deploy_contract(self, template, deployer: str, params: Optional[dict] = None,
                        code: bytes = b"") -> Tuple[bool, Any]:
        def run():
            bad = self._need_address("deployer", deployer)
            if bad:
                return False, bad
            tpl = self._coerce_enum(self.ContractTemplate, template)
            return self.contracts.deploy(tpl, deployer, params or {}, code)
        return self._call("contracts", run)

    def verify_contract(self, contract_id: str) -> Tuple[bool, str]:
        return self._call("contracts", lambda: self.contracts.verify(contract_id))

    def contract_address(self, contract_id: str) -> Optional[str]:
        ok, res = self._call("contracts", lambda: (True, self.contracts.address(contract_id)))
        return res if ok else None

    # ------------------------------------------------------------------
    # Facade: proofs, supply, addresses
    # ------------------------------------------------------------------
    def prove_state(self, address: str, height: Optional[int] = None) -> Optional[dict]:
        h = int(self.bc.height if height is None else height)
        ok, res = self._call("state", lambda: (True, self.state_proof.prove_balance(address, h)))
        return res if ok else None

    def prove_tx(self, txid: str, height: int) -> Optional[dict]:
        ok, res = self._call("state", lambda: (True, self.state_proof.prove_transaction(txid, int(height))))
        return res if ok else None

    def verify_tx(self, proof: dict) -> bool:
        ok, res = self._call("state", lambda: (True, self.state_proof.verify_tx_proof(proof)))
        return bool(res) if ok else False

    def supply_report(self) -> dict:
        def run():
            data = dict(self.supply.supply_distribution())
            data["inflation_pct"] = self.supply.inflation_rate()
            return True, data
        ok, res = self._call("supply", run)
        return res if ok else {}

    def address_formats(self, pubkey: bytes) -> dict:
        ok, res = self._call("registry", lambda: (True, self.address_formatter.pubkey_to_all_formats(pubkey)))
        return res if ok else {}

    def track_address(self, address: str) -> bool:
        """Follow an address: its balance proof is refreshed on every block."""
        if not self.is_valid_address(address):
            return False
        with self._lock:
            if address not in self.tracked and len(self.tracked) >= self.TRACKED_CAP:
                return False
            self.tracked.setdefault(address, None)
        return True

    def untrack_address(self, address: str) -> None:
        with self._lock:
            self.tracked.pop(address, None)

    # ------------------------------------------------------------------
    # Block pipeline (called by the Layer39 listener)
    # ------------------------------------------------------------------
    def _block_height(self, block) -> int:
        h = getattr(block, "height", None)
        if h is None:
            h = getattr(getattr(block, "header", None), "height", None)
        return int(h if h is not None else self.bc.height)

    def on_block_connected(self, block) -> Dict[str, Any]:
        """Run every stage in fixed order. Never raises."""
        report: Dict[str, Any] = {}
        try:
            height = self._block_height(block)
        except Exception as exc:  # noqa: BLE001
            self._fail("state", exc)
            return report
        self.blocks_seen += 1
        stages = (
            ("state",     self._stage_state),
            ("registry",  self._stage_registry),
            ("supply",    self._stage_supply),
            ("bridge",    self._stage_bridge),
            ("treasury",  self._stage_treasury),
            ("slashing",  self._stage_slashing),
            ("mixer",     self._stage_mixer),
            ("contracts", self._stage_contracts),
        )
        for name, fn in stages:
            try:
                report[name] = fn(block, height)
            except Exception as exc:  # noqa: BLE001
                self._fail(name, exc)
        self.last_report = report
        return report

    def on_block_reorged(self, old, new, ancestor_height: int) -> None:
        """Drop everything that was recorded above the common ancestor."""
        try:
            with self._lock:
                self.reorgs += 1
                while self.commitments and self.commitments[-1]["height"] > ancestor_height:
                    self.commitments.pop()
                while self.supply_snapshots and self.supply_snapshots[-1]["height"] > ancestor_height:
                    self.supply_snapshots.pop()
                for addr in self.tracked:
                    self.tracked[addr] = None   # recomputed on the next block
        except Exception as exc:  # noqa: BLE001
            self._fail("state", exc)

    # ---- stages (read-only on chain state) ----
    def _stage_state(self, block, height: int) -> dict:
        header = getattr(block, "header", None)
        txs = getattr(block, "transactions", None) or []
        commitment = {
            "height": height,
            "hash": getattr(block, "hash", None),
            "merkle_root": getattr(header, "merkle_root", None),
            "tx_count": len(txs),
        }
        with self._lock:
            self.commitments.append(commitment)
            addrs = list(self.tracked)
        for addr in addrs:
            proof = self.state_proof.prove_balance(addr, height)
            with self._lock:
                if addr in self.tracked:
                    self.tracked[addr] = {"balance": proof["balance"],
                                          "height": height,
                                          "proof_hash": proof["proof_hash"]}
        return {"commitments": len(self.commitments), "tracked": len(addrs)}

    def _stage_registry(self, block, height: int) -> dict:
        for nid in list(self.local_node_ids):
            self.registry.ping(nid, height)
        return self.registry.registry_stats()

    def _stage_supply(self, block, height: int) -> dict:
        if self.SNAPSHOT_INTERVAL > 0 and height % self.SNAPSHOT_INTERVAL == 0:
            snap = dict(self.supply.supply_distribution())
            snap["height"] = height
            with self._lock:
                self.supply_snapshots.append(snap)
            return {"snapshot": True, "snapshots": len(self.supply_snapshots)}
        return {"snapshot": False}

    def _stage_bridge(self, block, height: int) -> dict:
        return self.bridge.bridge_stats()

    def _stage_treasury(self, block, height: int) -> dict:
        return self.governance.treasury_governance_stats()

    def _stage_slashing(self, block, height: int) -> dict:
        return self.slashing.slashing_stats()

    def _stage_mixer(self, block, height: int) -> dict:
        return {"pools": self.mixer.mixer_stats()}

    def _stage_contracts(self, block, height: int) -> dict:
        return self.contracts.stats()

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------
    def wiring_report(self) -> List[dict]:
        """One row per class, in build order, proving each class is resolved."""
        instances = {
            "ContractStdLib": self.stdlib,
            "AddressFormatter": self.address_formatter,
            "TaprootScript": self.taproot,
            "StateProof": self.state_proof,
            "SupplyAnalytics": self.supply,
            "NodeRegistry": self.registry,
            "PrivacyMixerManager": self.mixer,
            "TokenBridgeV2": self.bridge,
            "SlashingConditionsEngine": self.slashing,
            "TreasuryGovernanceV2": self.governance,
        }
        rows = []
        for level, name, role in BUILD_ORDER:
            cls = getattr(g, name, None)
            if name == "CoinMixPool":
                pools = list(self.mixer._pools.values())
                resolved = bool(pools) and all(isinstance(p, cls) for p in pools)
                kind = f"{len(pools)} pool instances"
            elif name in instances:
                resolved = isinstance(instances[name], cls)
                kind = "instance"
            else:
                resolved = cls is not None
                kind = "type"
            fed_by, feeds = LINKS[name]
            rows.append({"level": level, "class": name, "role": role,
                         "kind": kind, "resolved": bool(resolved),
                         "fed_by": list(fed_by), "feeds": list(feeds)})
        return rows

    def stats(self) -> dict:
        return {
            "blocks_seen": self.blocks_seen,
            "reorgs": self.reorgs,
            "errors": self.errors,
            "stage_errors": dict(self.stage_errors),
            "last_error": self.last_error,
            "report_only": self.report_only,
            "has_real_treasury": self.has_real_treasury,
            "commitments": len(self.commitments),
            "supply_snapshots": len(self.supply_snapshots),
            "tracked_addresses": len(self.tracked),
            "local_nodes": len(self.local_node_ids),
            "registry": self.registry.registry_stats(),
            "bridge": self.bridge.bridge_stats(),
            "treasury": self.governance.treasury_governance_stats(),
            "slashing": self.slashing.slashing_stats(),
            "mixer": self.mixer.mixer_stats(),
            "contracts": self.contracts.stats(),
        }
