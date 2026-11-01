"""NEBULA group38 - chain wiring layer.

Connects the 20 classes of ``nebula_group38.py`` to each other in one ordered
chain, WITHOUT editing a single line of ``nebula_group38.py`` or of the host
file ``nebula_v10_11.py``.

Chain overview (see ``Layer38.LINKS`` for the machine-readable version):

    DevToolkit ──► PoSEngine ──► PoSValidator
    DigitalIdentityV2 (CredentialType, VerifiablePresentation)
        └─► ComplianceEngine (ComplianceCheckType, ComplianceRecord)
              └─► gates: SidechainBridge, TestnetFaucet, NFTMarketplaceV2,
                         NFTGamingEngine, TxBuilderV2, PoSEngine
    NFTGamingEngine (GameItem) ──► NFTMarketplaceV2 ──► WebSocketAPIServer
    TxBuilderV2 ──► ComplianceEngine ──► Mempool.submit hook ──► WebSocketAPIServer
    OrderBookManager ──► WebSocketAPIServer (dex_trade) ──► AnalyticsV2
    PoSEngine ──► AnalyticsV2 (TVL)      SidechainBridge ──► AnalyticsV2
    AnalyticsV2 (AnalyticsMetric) ◄── every service above

Design rules (same as the guide):
  * The layer NEVER rejects a block or a transaction. Every callback runs
    inside try/except; failures are counted in ``layer.errors``.
  * User-initiated operations (peg_in, buy, faucet ...) may be refused by the
    compliance gate, but only when ``enforce_compliance=True`` (default False:
    report-only).
  * Coin-minting helpers stay fail-closed through the host's
    ``_enable_dev_mode`` guard.
"""
from __future__ import annotations

import hashlib
import threading
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Deque, Dict, List, Optional, Tuple

import nebula_group38 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")


# ---------------------------------------------------------------------------
# Small helper types
# ---------------------------------------------------------------------------

@dataclass
class ChainEvent:
    """One entry of the layer's bounded event log."""
    seq:    int
    kind:   str
    height: Optional[int]
    detail: dict
    ts:     float = field(default_factory=time.time)


class _FallbackRNG:
    """Deterministic stand-in for the host's OnChainRNG.

    NFTGamingEngine only calls ``random_int(block_height, upper)``.
    Pass your own ``rng=`` to Layer38 to use the real OnChainRNG instead.
    """

    def random_int(self, block_height: int, upper: int) -> int:
        digest = hashlib.sha256(f"G38RNG:{block_height}:{time.time_ns()}".encode()).digest()
        return int.from_bytes(digest[:8], "big") % max(1, upper)


class _PoSStakingView:
    """Adapter so AnalyticsV2.tvl_estimate(staking=...) can read PoSEngine.

    tvl_estimate expects ``staking_stats()["total_staked_nbl"]`` as "<number> NBL".
    PoSEngine.pos_stats() exposes the same number under another key.
    """

    def __init__(self, pos: "g.PoSEngine"):
        self._pos = pos

    def staking_stats(self) -> dict:
        total = self._pos.pos_stats().get("total_stake_nbl", "0")
        return {"total_staked_nbl": f"{total} NBL"}


# ---------------------------------------------------------------------------
# The layer
# ---------------------------------------------------------------------------

class Layer38:
    """Owns one instance of every group38 service and wires them together.

    Usable in two ways:
      * as a chain listener (``bc.add_listener(layer)``) through ``install(host)``;
      * standalone: ``Layer38(blockchain=bc)`` and call its methods directly.
    """

    DEFAULT_SIDECHAIN = "nebula-sidechain-1"
    MAX_EVENTS        = 500
    MAX_ERRORS        = 100
    MAX_PROPOSER_LOG  = 1000
    MAX_DAILY_ADDRS   = 100_000

    # name of each of the 20 classes -> how this layer wires it
    COVERAGE: Dict[str, str] = {
        "PoSValidator":          "created by PoSEngine.register; stake summed into AnalyticsV2 TVL",
        "PoSEngine":             "proposer log per connected block; fed by DevToolkit wallets; gated by compliance",
        "DevToolkit":            "wallet source for validators; guarded test-block mining",
        "TxBuilderV2":           "build -> compliance.transaction_check -> Mempool.submit hook",
        "WebSocketSubscription": "created by WebSocketAPIServer.subscribe",
        "WebSocketAPIServer":    "receives blocks, txs, mempool, nft_sale, dex_trade, activity events",
        "NFTGamingEngine":       "mints items; items are listed and sold through NFTMarketplaceV2",
        "GameItem":              "created by NFTGamingEngine.mint_item; ownership moved on sale",
        "NFTMarketplaceV2":      "fixed-price game items + auctions auto-finalized on each block",
        "OrderBookManager":      "volume delta -> ws dex_trade; DEX_VOLUME metric",
        "SidechainBridge":       "compliance gate -> peg_in/peg_out -> ws + BRIDGE_VOLUME metric",
        "TestnetFaucet":         "dev-mode only; compliance gate -> request -> ws activity",
        "CredentialType":        "KYC credentials drive ComplianceEngine KYC level",
        "VerifiablePresentation": "create_kyc_presentation()/verify_kyc_presentation() round trip",
        "DigitalIdentityV2":     "issues/revokes KYC credentials bound to addresses",
        "ComplianceCheckType":   "enum values used as the record.checks keys",
        "ComplianceRecord":      "produced by ComplianceEngine; KYC level re-applied after every AML check",
        "ComplianceEngine":      "gate for bridge/faucet/market/gaming/validators + per-block tx scan",
        "AnalyticsMetric":       "keys of Layer38.metrics()",
        "AnalyticsV2":           "daily snapshot per block; TVL from PoSEngine through an adapter",
    }

    # ordered chain: (step, source, target, mechanism)
    LINKS: List[Tuple[int, str, str, str]] = [
        (1,  "DevToolkit",        "PoSEngine",          "bootstrap_test_validators()"),
        (2,  "PoSEngine",         "PoSValidator",       "register()"),
        (3,  "DigitalIdentityV2", "ComplianceEngine",   "issue_kyc() -> kyc level on ComplianceRecord"),
        (4,  "ComplianceEngine",  "SidechainBridge",    "peg_in()/peg_out() gate"),
        (5,  "ComplianceEngine",  "TestnetFaucet",      "faucet_request() gate"),
        (6,  "ComplianceEngine",  "NFTGamingEngine",    "mint_game_item() gate"),
        (7,  "NFTGamingEngine",   "NFTMarketplaceV2",   "list_game_item()/buy_game_item()"),
        (8,  "NFTMarketplaceV2",  "WebSocketAPIServer", "nft_sale broadcast"),
        (9,  "TxBuilderV2",       "ComplianceEngine",   "build_transfer() transaction_check"),
        (10, "TxBuilderV2",       "WebSocketAPIServer", "Mempool.submit hook -> mempool_update"),
        (11, "OrderBookManager",  "WebSocketAPIServer", "dex_trade broadcast on volume change"),
        (12, "WebSocketAPIServer", "AnalyticsV2",       "block/tx activity counters"),
        (13, "PoSEngine",         "AnalyticsV2",        "TVL through _PoSStakingView"),
        (14, "SidechainBridge",   "AnalyticsV2",        "BRIDGE_VOLUME metric"),
        (15, "AnalyticsV2",       "AnalyticsMetric",    "metrics() keyed by AnalyticsMetric values"),
    ]

    def __init__(self, node: Any = None, *, blockchain: Any = None, rng: Any = None,
                 sidechain_name: str = DEFAULT_SIDECHAIN,
                 enforce_compliance: bool = False,
                 pos_accounting: bool = False,
                 snapshot_every: int = 1):
        bc = blockchain if blockchain is not None else getattr(node, "bc", None)
        if bc is None:
            raise ValueError("Layer38 needs a blockchain (node.bc or blockchain=...)")
        self.node               = node
        self.bc                 = bc
        self.enforce_compliance = bool(enforce_compliance)
        self.pos_accounting     = bool(pos_accounting)
        self.snapshot_every     = max(1, int(snapshot_every))
        self.sidechain_name     = sidechain_name
        self._rng               = rng if rng is not None else _FallbackRNG()

        self._lock = threading.RLock()
        self.errors      = 0
        self.error_log: Deque[Tuple[float, str, str]] = deque(maxlen=self.MAX_ERRORS)
        self.events: Deque[ChainEvent]               = deque(maxlen=self.MAX_EVENTS)
        self._seq        = 0

        self.blocks_seen     = 0
        self.reorgs          = 0
        self.txs_seen        = 0
        self.flagged_txs     = 0
        self.ws_deliveries   = 0
        self.mempool_ok      = 0
        self.mempool_rejected = 0
        self.desyncs         = 0
        self.proposer_log: Deque[Tuple[int, Optional[str]]] = deque(maxlen=self.MAX_PROPOSER_LOG)

        self._daily: Dict[str, dict] = {}
        self._kyc_creds: Dict[str, dict] = {}      # cred_id -> {holder, address, level, expires, revoked}
        self._did_address: Dict[str, str] = {}     # did -> address
        self._listings: Dict[str, dict] = {}       # listing_id -> metadata
        self._bridge_volume = 0.0
        self._last_dex_volume = 0.0

        self._mp_target: Any = None
        self._mp_had_instance_attr = False
        self._mp_prev: Any = None
        self._mp_hook: Any = None

        self.build_errors: Dict[str, str] = {}
        self._build_services()

    # ------------------------------------------------------------------
    # Construction (dependency order, each service isolated)
    # ------------------------------------------------------------------

    def _build(self, name: str, factory):
        try:
            return factory()
        except Exception as exc:                       # node must still start
            self.build_errors[name] = f"{type(exc).__name__}: {exc}"
            return None

    def _build_services(self) -> None:
        bc = self.bc
        self.ws         = self._build("WebSocketAPIServer", lambda: g.WebSocketAPIServer(bc))
        self.compliance = self._build("ComplianceEngine",   lambda: g.ComplianceEngine(bc))
        self.identity   = self._build("DigitalIdentityV2",  lambda: g.DigitalIdentityV2())
        self.pos        = self._build("PoSEngine",          lambda: g.PoSEngine(bc))
        self.txb        = self._build("TxBuilderV2",        lambda: g.TxBuilderV2(bc))
        self.bridge     = self._build("SidechainBridge",
                                      lambda: g.SidechainBridge(self.sidechain_name, bc))
        self.market     = self._build("NFTMarketplaceV2",   lambda: g.NFTMarketplaceV2(bc))
        self.gaming     = self._build("NFTGamingEngine",    lambda: g.NFTGamingEngine(bc, self._rng))
        self.books      = self._build("OrderBookManager",   lambda: g.OrderBookManager())
        self.analytics  = self._build("AnalyticsV2",        lambda: g.AnalyticsV2(bc))
        self.faucet     = self._build("TestnetFaucet",      lambda: g.TestnetFaucet(bc))
        self.dev        = self._build("DevToolkit",         lambda: g.DevToolkit(bc))

    @property
    def services(self) -> Dict[str, Any]:
        return {
            "WebSocketAPIServer": self.ws, "ComplianceEngine": self.compliance,
            "DigitalIdentityV2": self.identity, "PoSEngine": self.pos,
            "TxBuilderV2": self.txb, "SidechainBridge": self.bridge,
            "NFTMarketplaceV2": self.market, "NFTGamingEngine": self.gaming,
            "OrderBookManager": self.books, "AnalyticsV2": self.analytics,
            "TestnetFaucet": self.faucet, "DevToolkit": self.dev,
        }

    # ------------------------------------------------------------------
    # Internal utilities
    # ------------------------------------------------------------------

    def _record_error(self, label: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.error_log.append((time.time(), label, f"{type(exc).__name__}: {exc}"))

    def _safe(self, label: str, fn, *args, default=None, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as exc:
            self._record_error(label, exc)
            return default

    def _emit(self, kind: str, height: Optional[int] = None, **detail) -> None:
        with self._lock:
            self._seq += 1
            self.events.append(ChainEvent(self._seq, kind, height, detail))

    def _broadcast(self, event_type: str, data: dict) -> int:
        if self.ws is None:
            return 0
        sent = self._safe(f"ws.broadcast:{event_type}", self.ws.broadcast_event,
                          event_type, data, default=0) or 0
        with self._lock:
            self.ws_deliveries += sent
        return sent

    def _daily_bucket(self) -> dict:
        day = time.strftime("%Y-%m-%d")
        bucket = self._daily.get(day)
        if bucket is None:
            bucket = {"txs": 0, "addresses": set()}
            self._daily[day] = bucket
            for old in sorted(self._daily)[:-7]:
                del self._daily[old]
        return bucket

    @staticmethod
    def _block_miner(block: Any) -> Optional[str]:
        """Best-effort miner address; None when it cannot be determined."""
        miner = getattr(block, "miner", None)
        if isinstance(miner, str) and miner:
            return miner
        try:
            coinbase = block.transactions[0]
            addr = getattr(coinbase.outputs[0], "address", "")
            return addr or None
        except Exception:
            return None

    def _tx_check(self, tx: Any) -> Tuple[bool, str]:
        """ComplianceEngine.transaction_check that never raises."""
        if self.compliance is None:
            return True, "UNCHECKED: compliance unavailable"
        try:
            return self.compliance.transaction_check(tx)
        except AttributeError as exc:                  # e.g. output without .address
            return True, f"UNCHECKED: {exc}"

    # ------------------------------------------------------------------
    # Compliance gate + KYC (DigitalIdentityV2 -> ComplianceEngine)
    # ------------------------------------------------------------------

    def _effective_kyc(self, address: str) -> int:
        now = time.time()
        level = 0
        for cred in self._kyc_creds.values():
            if cred["address"] == address and not cred["revoked"] and cred["expires"] > now:
                level = max(level, cred["level"])
        return level

    def _aml(self, address: str):
        """Run the AML check and re-apply the layer's KYC state to the record.

        ComplianceEngine.run_aml_check builds a fresh record every time, which
        would otherwise reset kyc_level to 0.
        """
        record = self.compliance.run_aml_check(address)
        level = self._effective_kyc(address)
        record.kyc_level = level
        record.checks[g.ComplianceCheckType.KYC.value] = level > 0
        return record

    def _gate(self, address: str, action: str) -> Tuple[bool, str]:
        if self.compliance is None:
            return True, "compliance unavailable"
        record = self._safe("compliance.aml", self._aml, address)
        if record is None:
            return True, "compliance check failed (not enforced)"
        allowed = (record.checks.get(g.ComplianceCheckType.AML.value, True)
                   and record.checks.get("blacklist", True))
        if allowed:
            return True, "OK"
        self._emit("compliance_block" if self.enforce_compliance else "compliance_warning",
                   address=address, action=action, flags=list(record.flags))
        if self.enforce_compliance:
            return False, f"Compliance: {action} blocked for {address} ({', '.join(record.flags)})"
        return True, f"WARNING: {address} flagged ({', '.join(record.flags)})"

    def register_kyc_issuer(self, did: str, name: str) -> bool:
        if self.identity is None:
            return False
        return self.identity.register_issuer(did, name, [g.CredentialType.KYC])

    def bind_identity(self, did: str, address: str) -> None:
        with self._lock:
            self._did_address[did] = address

    def issue_kyc(self, issuer_did: str, holder_did: str, claims: Optional[dict] = None,
                  level: int = 1, expiry_days: int = 365) -> Tuple[bool, str]:
        """Issue a KYC credential and lift the holder address' KYC level."""
        if self.identity is None or self.compliance is None:
            return False, "identity/compliance unavailable"
        address = self._did_address.get(holder_did)
        if address is None:
            return False, "Holder DID is not bound to an address (bind_identity first)"
        try:
            cid = self.identity.issue_credential(
                issuer_did, holder_did, g.CredentialType.KYC,
                claims or {}, expiry_days=expiry_days)
        except ValueError as exc:
            return False, str(exc)
        with self._lock:
            self._kyc_creds[cid] = {
                "holder": holder_did, "address": address, "level": int(level),
                "expires": time.time() + expiry_days * 86400, "revoked": False,
                "issuer": issuer_did,
            }
        self._safe("compliance.aml", self._aml, address)
        self._emit("kyc_issued", address=address, credential=cid, level=level)
        return True, cid

    def revoke_kyc(self, cred_id: str, issuer_did: str) -> Tuple[bool, str]:
        if self.identity is None:
            return False, "identity unavailable"
        ok, msg = self.identity.revoke_credential(cred_id, issuer_did)
        if ok:
            with self._lock:
                cred = self._kyc_creds.get(cred_id)
                if cred:
                    cred["revoked"] = True
            if cred:
                self._safe("compliance.aml", self._aml, cred["address"])
            self._emit("kyc_revoked", credential=cred_id)
        return ok, msg

    def kyc_level(self, address: str) -> int:
        return self._effective_kyc(address)

    def create_kyc_presentation(self, holder_did: str, credential_ids: List[str], purpose: str,
                                challenge: str, privkey: int,
                                selective_claims: Optional[Dict[str, List[str]]] = None
                                ) -> Tuple[bool, str]:
        """DigitalIdentityV2.create_presentation without raising (returns (ok, vp_id|reason))."""
        if self.identity is None:
            return False, "identity unavailable"
        try:
            vp_id = self.identity.create_presentation(holder_did, credential_ids, purpose,
                                                      challenge, privkey, selective_claims)
        except ValueError as exc:
            return False, str(exc)
        self._emit("presentation_created", holder=holder_did, vp=vp_id)
        return True, vp_id

    def verify_kyc_presentation(self, vp_id: str, challenge: str) -> Tuple[bool, str]:
        if self.identity is None:
            return False, "identity unavailable"
        return self.identity.verify_presentation(vp_id, challenge)

    # ------------------------------------------------------------------
    # DevToolkit -> PoSEngine -> PoSValidator
    # ------------------------------------------------------------------

    def bootstrap_test_validators(self, n: int = 4, stake: Optional[int] = None,
                                  commission: float = 0.05) -> List[Tuple[str, bool, str]]:
        """Create n throw-away wallets and register them as validators.

        Mnemonics are NOT kept: only addresses are used and returned.
        """
        if self.dev is None or self.pos is None:
            return []
        stake = stake if stake is not None else self.pos.MIN_STAKE
        results = []
        for wallet in self.dev.generate_test_wallets(n):
            address = wallet["address"]
            ok, msg = self.register_validator(address, stake, commission)
            results.append((address, ok, msg))
        return results

    def register_validator(self, address: str, stake: int,
                           commission: float) -> Tuple[bool, str]:
        if self.pos is None:
            return False, "PoSEngine unavailable"
        allowed, why = self._gate(address, "register_validator")
        if not allowed:
            return False, why
        return self.pos.register(address, stake, commission)

    def mine_test_blocks(self, n: int = 10, miner: Optional[str] = None) -> int:
        """Guarded wrapper: only runs on a chain whose dev mode is already on."""
        if self.dev is None:
            return 0
        g._enable_dev_mode(self.bc, "Layer38.mine_test_blocks")
        return self.dev.mine_test_blocks(n, miner)

    # ------------------------------------------------------------------
    # TxBuilderV2 -> ComplianceEngine -> Mempool.submit -> WebSocketAPIServer
    # ------------------------------------------------------------------

    def build_transfer(self, sender: str, recipient: str, amount_nbl: float,
                       fee_rate: Optional[int] = None, memo: str = "") -> Tuple[bool, Any, str]:
        if self.txb is None:
            return False, None, "TxBuilderV2 unavailable"
        for who in (sender, recipient):
            allowed, why = self._gate(who, "build_transfer")
            if not allowed:
                return False, None, why
        ok, tx, msg = self.txb.build_transfer(sender, recipient, amount_nbl, fee_rate, memo)
        if not ok:
            return ok, tx, msg
        passed, note = self._tx_check(tx)
        if not passed:
            self._emit("tx_blocked" if self.enforce_compliance else "tx_warning", note=note)
            if self.enforce_compliance:
                return False, None, note
        return True, tx, msg if note in ("PASS",) else f"{msg} [{note}]"

    def submit_prepared(self, tx: Any) -> Tuple[bool, str]:
        """Forward a prepared tx to the node's Mempool.submit (hook counts it)."""
        mempool = getattr(self.bc, "mempool", None)
        if mempool is None or not hasattr(mempool, "submit"):
            return False, "mempool unavailable"
        result = mempool.submit(tx)
        if isinstance(result, tuple) and len(result) >= 2:
            return bool(result[0]), str(result[1])
        return bool(result), ""

    def attach_mempool_hook(self, mempool: Any = None) -> bool:
        """Wrap Mempool.submit so successful/failed submits reach the layer.

        The original return value and exceptions are passed through untouched.
        """
        mp = mempool if mempool is not None else getattr(self.bc, "mempool", None)
        if mp is None or not hasattr(mp, "submit") or self._mp_hook is not None:
            return False
        layer = self
        original = mp.submit

        def hooked(tx, *args, **kwargs):
            result = original(tx, *args, **kwargs)
            try:
                layer._on_mempool_result(tx, result)
            except Exception as exc:
                layer._record_error("mempool_hook", exc)
            return result

        try:
            self._mp_had_instance_attr = "submit" in getattr(mp, "__dict__", {})
            self._mp_prev = mp.__dict__.get("submit") if self._mp_had_instance_attr else None
            mp.submit = hooked
        except Exception as exc:
            self._record_error("mempool_attach", exc)
            return False
        self._mp_target, self._mp_hook = mp, hooked
        return True

    def detach_mempool_hook(self) -> None:
        mp = self._mp_target
        if mp is None:
            return
        try:
            if self._mp_had_instance_attr:
                mp.submit = self._mp_prev
            else:
                del mp.submit
        except Exception as exc:
            self._record_error("mempool_detach", exc)
        self._mp_target = self._mp_hook = self._mp_prev = None
        self._mp_had_instance_attr = False

    def _on_mempool_result(self, tx: Any, result: Any) -> None:
        ok = bool(result[0]) if isinstance(result, tuple) and result else bool(result)
        with self._lock:
            if ok:
                self.mempool_ok += 1
            else:
                self.mempool_rejected += 1
        self._emit("mempool_submit", ok=ok, txid=getattr(tx, "txid", None))
        self._broadcast("mempool_update", {"txid": getattr(tx, "txid", None), "accepted": ok})
        if ok and self.ws is not None:
            self.ws_deliveries += self._safe("ws.on_new_tx", self.ws.on_new_tx, tx, default=0) or 0

    # ------------------------------------------------------------------
    # SidechainBridge / TestnetFaucet (compliance gate -> service -> ws)
    # ------------------------------------------------------------------

    def peg_in(self, address: str, amount_nbl: float) -> Tuple[bool, str]:
        if self.bridge is None:
            return False, "SidechainBridge unavailable"
        allowed, why = self._gate(address, "peg_in")
        if not allowed:
            return False, why
        ok, msg = self.bridge.peg_in(address, amount_nbl)
        if ok:
            with self._lock:
                self._bridge_volume += float(amount_nbl)
            self._emit("peg_in", address=address, amount=amount_nbl)
            self._broadcast("address_activity", {"address": address, "action": "peg_in"})
        return ok, msg

    def peg_out(self, address: str, amount_nbl: float, proof: str = "") -> Tuple[bool, str]:
        if self.bridge is None:
            return False, "SidechainBridge unavailable"
        allowed, why = self._gate(address, "peg_out")
        if not allowed:
            return False, why
        ok, msg = self.bridge.peg_out(address, amount_nbl, proof)
        if ok:
            with self._lock:
                self._bridge_volume += float(amount_nbl)
            self._emit("peg_out", address=address, amount=amount_nbl)
            self._broadcast("address_activity", {"address": address, "action": "peg_out"})
        return ok, msg

    def faucet_request(self, address: str) -> Tuple[bool, str]:
        if self.faucet is None:
            return False, "TestnetFaucet unavailable (dev mode is off on this chain)"
        allowed, why = self._gate(address, "faucet_request")
        if not allowed:
            return False, why
        ok, msg = self.faucet.request(address)
        if ok:
            self._emit("faucet", address=address)
            self._broadcast("address_activity", {"address": address, "action": "faucet"})
        return ok, msg

    # ------------------------------------------------------------------
    # NFTGamingEngine -> NFTMarketplaceV2 -> WebSocketAPIServer
    # ------------------------------------------------------------------

    def register_game(self, game_id: str, name: str, developer: str,
                      item_types: List[str]) -> bool:
        return bool(self.gaming and self.gaming.register_game(game_id, name, developer, item_types))

    def mint_game_item(self, game_id: str, owner: str, item_type: str) -> Tuple[bool, str]:
        if self.gaming is None:
            return False, "NFTGamingEngine unavailable"
        allowed, why = self._gate(owner, "mint_game_item")
        if not allowed:
            return False, why
        return self.gaming.mint_item(game_id, owner, item_type, block_height=self.bc.height)

    def _find_item(self, owner: str, item_id: str) -> Optional[dict]:
        for item in self.gaming.player_items(owner):
            if item["item_id"] == item_id:
                return item
        return None

    @staticmethod
    def _token_id(item_id: str) -> int:
        try:
            return int(item_id, 16)
        except ValueError:
            return int.from_bytes(hashlib.sha256(item_id.encode()).digest()[:8], "big")

    def list_game_item(self, item_id: str, seller: str, price_nbl: float) -> Tuple[bool, str]:
        if self.gaming is None or self.market is None:
            return False, "gaming/marketplace unavailable"
        with self._lock:
            item = self._find_item(seller, item_id)
            if item is None:
                return False, "Item not found or not owned by seller"
            if not item["tradeable"]:
                return False, "Item is not tradeable"
            for meta in self._listings.values():
                if meta["kind"] == "game_item" and meta["item_id"] == item_id and not meta["sold"]:
                    return False, "Item is already listed"
            lid = self.market.list_fixed(item["game_id"], self._token_id(item_id), seller, price_nbl)
            self._listings[lid] = {"kind": "game_item", "item_id": item_id, "seller": seller,
                                   "game_id": item["game_id"], "sold": False}
        self._emit("game_item_listed", listing=lid, item=item_id, seller=seller)
        return True, lid

    def buy_game_item(self, listing_id: str, buyer: str) -> Tuple[bool, str]:
        if self.gaming is None or self.market is None:
            return False, "gaming/marketplace unavailable"
        with self._lock:
            meta = self._listings.get(listing_id)
            if meta is None or meta["kind"] != "game_item":
                return False, "Not a game-item listing of this layer"
            if meta["sold"]:
                return False, "Already sold"
            allowed, why = self._gate(buyer, "buy_game_item")
            if not allowed:
                return False, why
            item = self._find_item(meta["seller"], meta["item_id"])
            if item is None or not item["tradeable"]:
                return False, "Seller no longer owns a tradeable copy of this item"
            ok, msg = self.market.buy_now(listing_id, buyer)
            if not ok:
                return False, msg
            meta["sold"] = True
            moved, why_moved = self.gaming.transfer_item(meta["item_id"], meta["seller"], buyer)
            if not moved:
                self.desyncs += 1
                self._emit("market_gaming_desync", listing=listing_id, reason=why_moved)
                return False, f"Marketplace sold the listing but item transfer failed: {why_moved}"
        self._emit("nft_sale", listing=listing_id, item=meta["item_id"], buyer=buyer)
        self._broadcast("nft_sale", {"listing_id": listing_id, "item_id": meta["item_id"],
                                     "buyer": buyer})
        return True, msg

    def list_nft_auction(self, collection_id: str, token_id: int, seller: str,
                         start_price: float, reserve: float = 0,
                         duration_blocks: int = 1000, auction_type: Any = None) -> str:
        if self.market is None:
            raise RuntimeError("NFTMarketplaceV2 unavailable")
        kwargs = {}
        if auction_type is not None:
            kwargs["auction_type"] = auction_type
        with self._lock:
            lid = self.market.list_auction(collection_id, token_id, seller, start_price,
                                           reserve, duration_blocks, **kwargs)
            self._listings[lid] = {"kind": "auction", "seller": seller,
                                   "end_block": self.bc.height + duration_blocks,
                                   "attempted": False, "sold": False}
        self._emit("auction_listed", listing=lid, seller=seller)
        return lid

    def place_nft_bid(self, listing_id: str, bidder: str, amount: float) -> Tuple[bool, str]:
        if self.market is None:
            return False, "NFTMarketplaceV2 unavailable"
        allowed, why = self._gate(bidder, "place_nft_bid")
        if not allowed:
            return False, why
        return self.market.place_bid(listing_id, bidder, amount)

    # ------------------------------------------------------------------
    # Order books
    # ------------------------------------------------------------------

    def ensure_pair(self, pair: str):
        return self.books.add_pair(pair) if self.books is not None else None

    # ------------------------------------------------------------------
    # Chain listener interface (bc.add_listener(layer))
    # ------------------------------------------------------------------

    def on_connect(self, block: Any) -> None:
        try:
            height = getattr(block, "height", None)
            with self._lock:
                self.blocks_seen += 1
            self._emit("block_connected", height, hash=getattr(block, "hash", None))
            txs = list(getattr(block, "transactions", None) or [])
            self._safe("link.ws", self._link_ws, block, txs)
            self._safe("link.compliance", self._link_compliance, txs, height)
            self._safe("link.pos", self._link_pos, block, height)
            self._safe("link.market", self._link_market)
            self._safe("link.orderbook", self._link_orderbook)
            self._safe("link.analytics", self._link_analytics)
        except Exception as exc:                       # never propagate into the chain
            self._record_error("on_connect", exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        try:
            with self._lock:
                self.reorgs += 1
                kept = [(h, p) for h, p in self.proposer_log if h <= ancestor_height]
                self.proposer_log.clear()
                self.proposer_log.extend(kept)
            self._emit("reorg", ancestor_height, old=len(old or []), new=len(new or []))
        except Exception as exc:
            self._record_error("on_reorg", exc)

    def detach(self) -> None:
        self.detach_mempool_hook()
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer38.detach", exc_info=True)

    # --- links executed for every connected block ---------------------

    def _link_ws(self, block: Any, txs: list) -> None:
        bucket = self._daily_bucket()
        if self.ws is not None:
            self.ws_deliveries += self.ws.on_new_block(block)
        for tx in txs:
            if self.ws is not None:
                self.ws_deliveries += self.ws.on_new_tx(tx)
            with self._lock:
                self.txs_seen += 1
                bucket["txs"] += 1
                for out in getattr(tx, "outputs", None) or []:
                    addr = getattr(out, "address", "")
                    if addr and len(bucket["addresses"]) < self.MAX_DAILY_ADDRS:
                        bucket["addresses"].add(addr)

    def _link_compliance(self, txs: list, height: Optional[int]) -> None:
        for tx in txs:
            passed, note = self._tx_check(tx)
            if not passed or note.startswith("FLAGGED"):
                with self._lock:
                    self.flagged_txs += 1
                self._emit("compliance_flag", height, txid=getattr(tx, "txid", None), note=note)
                self._broadcast("address_activity", {"flag": note, "txid": getattr(tx, "txid", None)})

    def _link_pos(self, block: Any, height: Optional[int]) -> None:
        if self.pos is None or height is None:
            return
        expected = self.pos.select_proposer(height)
        with self._lock:
            self.proposer_log.append((height, expected))
        if self.pos_accounting and expected is not None:
            miner = self._block_miner(block)
            if miner is not None:                      # unknown miner -> never penalize anyone
                self.pos.record_proposal(expected, proposed=(miner == expected))

    def _link_market(self) -> None:
        if self.market is None:
            return
        for lid, meta in list(self._listings.items()):
            if meta["kind"] != "auction" or meta["attempted"] or meta["sold"]:
                continue
            if self.bc.height <= meta["end_block"]:
                continue
            meta["attempted"] = True
            ok, msg = self.market.finalize_auction(lid)
            self._emit("auction_finalize", listing=lid, ok=ok, note=msg)
            if ok:
                meta["sold"] = True
                self._broadcast("nft_sale", {"listing_id": lid, "note": msg})

    def _link_orderbook(self) -> None:
        if self.books is None:
            return
        volume = float(self.books.market_summary()["total_vol_24h"])
        delta = volume - self._last_dex_volume
        self._last_dex_volume = volume
        if delta > 0:
            self._broadcast("dex_trade", {"volume_delta": delta, "volume_24h": volume})

    def _link_analytics(self) -> None:
        if self.analytics is not None and self.blocks_seen % self.snapshot_every == 0:
            self.analytics.record_daily_snapshot()

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    @staticmethod
    def _first_number(text: Any) -> Optional[float]:
        try:
            return float(str(text).replace(",", "").replace("$", "").split()[0])
        except (ValueError, IndexError):
            return None

    def metrics(self) -> Dict[str, Optional[float]]:
        """One value per AnalyticsMetric; None where this layer has no real source."""
        M = g.AnalyticsMetric
        out: Dict[str, Optional[float]] = {m.value: None for m in M}
        bucket = self._daily.get(time.strftime("%Y-%m-%d"))
        if bucket is not None:
            out[M.DAILY_TXS.value]    = float(bucket["txs"])
            out[M.DAILY_ACTIVE.value] = float(len(bucket["addresses"]))
        if self.analytics is not None and self.pos is not None:
            tvl = self._safe("metrics.tvl", self.analytics.tvl_estimate,
                             _PoSStakingView(self.pos))
            if tvl:
                out[M.TVL.value] = self._first_number(tvl["total_nbl"])
        if self.bridge is not None:
            out[M.BRIDGE_VOLUME.value] = self._bridge_volume
        if self.books is not None:
            out[M.DEX_VOLUME.value] = self._first_number(
                self.books.market_summary()["total_vol_24h"])
        if self.market is not None:
            out[M.NFT_VOLUME.value] = self._first_number(
                self.market.marketplace_stats()["volume_nbl"])
        return out                                     # FEES_24H / GAS_USED stay None

    def stats(self) -> dict:
        sources = {
            "ws": (self.ws, "ws_stats"), "pos": (self.pos, "pos_stats"),
            "market": (self.market, "marketplace_stats"), "bridge": (self.bridge, "bridge_stats"),
            "faucet": (self.faucet, "faucet_stats"), "gaming": (self.gaming, "gaming_stats"),
            "identity": (self.identity, "identity_stats"),
            "compliance": (self.compliance, "compliance_stats"),
            "orderbooks": (self.books, "market_summary"),
            "health": (self.analytics, "protocol_health"),
        }
        services = {name: self._safe(f"stats.{name}", getattr(obj, method))
                    for name, (obj, method) in sources.items() if obj is not None}
        return {
            "hub": {
                "blocks_seen": self.blocks_seen, "reorgs": self.reorgs, "txs_seen": self.txs_seen,
                "flagged_txs": self.flagged_txs, "ws_deliveries": self.ws_deliveries,
                "mempool_ok": self.mempool_ok, "mempool_rejected": self.mempool_rejected,
                "desyncs": self.desyncs, "errors": self.errors,
                "enforce_compliance": self.enforce_compliance,
                "pos_accounting": self.pos_accounting,
            },
            "services": services,
            "metrics": self.metrics(),
            "build_errors": dict(self.build_errors),
        }


# ---------------------------------------------------------------------------
# install / uninstall (same pattern as the guide / group 5)
# ---------------------------------------------------------------------------

def install(host: Any, **options: Any) -> None:
    """Patch NEBULAFullNode.__init__ so every new node gets ``node.group38``."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g38_orig", None):
        return
    original = cls.__init__

    def patched(self, *args, **kwargs):
        original(self, *args, **kwargs)
        try:
            layer = Layer38(self, **options)
            self.group38 = layer
            self.bc.add_listener(layer)
            layer.attach_mempool_hook()
        except Exception as exc:                       # the node must still start
            self.group38_error = exc

    cls._g38_orig = original
    cls.__init__ = patched


def uninstall(host: Any) -> None:
    """Restore the original NEBULAFullNode.__init__ (existing nodes: call node.group38.detach())."""
    cls = host.NEBULAFullNode
    original = getattr(cls, "_g38_orig", None)
    if original:
        cls.__init__ = original
        del cls._g38_orig
