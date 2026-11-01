"""NEBULA group42 wiring layer.

Connects the 20 classes of ``nebula_group42.py`` to the live node WITHOUT editing
``nebula_v10_11.py``:

* ``Layer42``  - one object per node (``node.group42``) that owns every service,
  receives chain events (``on_connect`` / ``on_reorg``) and exposes validated,
  read-mostly facade methods.
* ``install(host)`` / ``uninstall(host)`` - wrap ``NEBULAFullNode.__init__`` so every
  node gets a ``Layer42`` automatically; the node still starts if the layer fails.

Design rules (same as the earlier groups):
* The layer NEVER rejects a block or a transaction. Every callback is wrapped in
  try/except and failures are counted in ``layer.errors`` / ``layer.error_log``.
* Chain-event handling is read-only with respect to consensus state.
* The 20 original classes are used unmodified; safeguards the originals lack live
  in the facade methods of this file.

Honest scope notes (see CHANGES_v10_42.txt for the full list):
* Several original classes keep their own in-memory books and do not move real UTXOs
  (vault deposits, lending, privacy pool, name-service fees, burn ledger). The layer
  validates inputs and balances, but it does not create on-chain transactions.
* State is in memory only; it is rebuilt/empty after a restart (the indexer re-syncs).
"""
from __future__ import annotations

import math
import re
import threading
import time
from collections import OrderedDict, deque
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group42 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

# Names of the 20 classes this layer wires (order = guide order).
GROUP42_CLASSES: Tuple[str, ...] = (
    "NBLDomain", "YieldOptimizer", "DollarCostAverager", "ConfidentialTransaction",
    "PrivacyPoolV2", "NEBULANameService", "EcosystemHub", "VoteEscrowedNBL",
    "MEVProtector", "CrossMarginAccount", "CrossMarginEngine", "InterestRateModel",
    "LendingPoolV2", "LendingProtocolV2", "VaultStrategy", "VaultManager",
    "FractionalNFTDex", "TokenomicsEngine", "SybilResistanceScore", "BlockchainIndexer",
)

ECOSYSTEM_CATEGORIES: Tuple[str, ...] = (
    "defi", "nft", "gaming", "social", "identity",
    "governance", "bridge", "data_market", "insurance", "analytics",
)

_LABEL_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$")   # 3..63 chars, no dots
_UNIT = 10 ** g.DECIMALS


# --------------------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------------------
@dataclass
class Layer42Config:
    enable_indexer: bool = True
    index_catchup_batch: int = 500          # max blocks indexed per callback while catching up
    enable_hub_events: bool = True
    hub_event_limit: int = 1000             # EcosystemHub keeps only the newest N events
    enable_mev_scan: bool = True
    enable_dca: bool = True                 # needs a price_provider, otherwise it is skipped
    margin_check_interval: int = 10         # blocks between cross-margin scans (0 = off)
    vault_harvest_interval: int = 0         # 0 = never. VaultManager.harvest_all is SIMULATED yield
    confidential_registry_limit: int = 10_000
    error_log_size: int = 100


# --------------------------------------------------------------------------------------
# Small validation helpers
# --------------------------------------------------------------------------------------
def _is_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _pos_number(x: Any) -> bool:
    return _is_number(x) and x > 0


def _pos_int(x: Any) -> bool:
    return isinstance(x, int) and not isinstance(x, bool) and x > 0


def _nonempty_str(x: Any, max_len: int = 256) -> bool:
    return isinstance(x, str) and 0 < len(x.strip()) and len(x) <= max_len


# --------------------------------------------------------------------------------------
# The layer
# --------------------------------------------------------------------------------------
class Layer42:
    """Owns and drives every group42 service for one node."""

    def __init__(self, node: Any,
                 config: Optional[Layer42Config] = None,
                 price_provider: Optional[Callable[[], Optional[float]]] = None,
                 identity_verifier: Optional[Callable[[str, str], bool]] = None):
        self.node = node
        self.bc = node.bc
        self.cfg = config or Layer42Config()
        self.price_provider = price_provider          # () -> float USD price of 1 NBL, or None
        self.identity_verifier = identity_verifier    # (address, did_proof) -> bool

        self._lock = threading.RLock()
        self._detached = False
        self.errors = 0
        self.error_log: deque = deque(maxlen=self.cfg.error_log_size)
        self.unavailable: Dict[str, str] = {}
        self.blocks_seen = 0
        self.reorgs_seen = 0
        self.last_height = -1
        self.dca_skipped_no_price = 0
        self.mev_scan_errors = 0
        self.mev_flagged: deque = deque(maxlen=200)
        self.margin_calls_last: List[str] = []
        self.last_harvest: Dict[str, int] = {}
        self._confidential: "OrderedDict[str, Any]" = OrderedDict()

        # ---- build services (each one isolated: one failure never blocks the others) ----
        self.irm = self._build("InterestRateModel", lambda: g.InterestRateModel())
        self.lending = self._build("LendingProtocolV2", lambda: g.LendingProtocolV2(self.bc))
        self.vaults = self._build("VaultManager", lambda: g.VaultManager(self.bc))
        self.nns = self._build("NEBULANameService", lambda: g.NEBULANameService(self.bc))
        self.venbl = self._build("VoteEscrowedNBL", lambda: g.VoteEscrowedNBL(self.bc))
        self.privacy = self._build("PrivacyPoolV2", lambda: g.PrivacyPoolV2(self.bc))
        self.cross_margin = self._build(
            "CrossMarginEngine",
            lambda: g.CrossMarginEngine(self.bc, oracle=getattr(node, "oracle", None)))
        self.mev = self._build("MEVProtector", lambda: g.MEVProtector(self.bc.mempool, self.bc))
        self.tokenomics = self._build("TokenomicsEngine", lambda: g.TokenomicsEngine(self.bc))
        self.sybil = self._build("SybilResistanceScore", lambda: g.SybilResistanceScore(self.bc))
        self.indexer = self._build("BlockchainIndexer", lambda: g.BlockchainIndexer(self.bc))
        self.hub = self._build("EcosystemHub", lambda: g.EcosystemHub(self.bc))
        self.yield_optimizer = self._build("YieldOptimizer", lambda: g.YieldOptimizer())
        self.dca = self._build("DollarCostAverager", self._make_dca)
        self.nft_dex = self._build("FractionalNFTDex", self._make_nft_dex)

        # Classes that are created on demand by the services above or by facade methods.
        self._check_dependency("NBLDomain", self.nns, "created by NEBULANameService.register")
        self._check_dependency("CrossMarginAccount", self.cross_margin,
                               "created by CrossMarginEngine.open_account")
        self._check_dependency("LendingPoolV2", self.lending,
                               "created by LendingProtocolV2.create_pool")
        self._check_dependency("VaultStrategy", self.vaults,
                               "created by VaultManager.__init__ (4 default vaults)")
        if not all(hasattr(getattr(g, "PedersenCommitment", None), a) for a in ("commit", "add")):
            self.unavailable["ConfidentialTransaction"] = \
                "PedersenCommitment (group22) with commit/add is not available"

    # ------------------------------------------------------------------ build helpers
    def _build(self, name: str, factory: Callable[[], Any]) -> Any:
        try:
            return factory()
        except Exception as exc:                      # node must keep starting
            self.unavailable[name] = f"{type(exc).__name__}: {exc}"
            self._log_error(f"build:{name}", exc)
            return None

    def _make_dca(self) -> Any:
        dca = g.DollarCostAverager()
        if not hasattr(dca, "executions"):
            raise RuntimeError("DeFiStrategy base class has no 'executions' attribute")
        return dca

    def _make_nft_dex(self) -> Any:
        """FractionalNFTDex needs an NFTFractionalizer from another group."""
        frac = getattr(self.node, "nft_fractionalizer", None) or getattr(self.node, "fractionalizer", None)
        if frac is None:
            cls = getattr(g, "NFTFractionalizer", None)
            if cls is None:
                raise RuntimeError("NFTFractionalizer is not available (other group not loaded)")
            frac = cls()          # v10.19 fix: NFTFractionalizer.__init__ takes no arguments
        return g.FractionalNFTDex(frac, self.bc)

    def _check_dependency(self, name: str, owner: Any, via: str) -> None:
        if owner is None and name not in self.unavailable:
            self.unavailable[name] = f"owner service unavailable ({via})"

    def _log_error(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.error_log.append({"where": where, "error": f"{type(exc).__name__}: {exc}",
                                   "ts": time.time()})

    def _safe(self, where: str, fn: Callable[..., Any], *args: Any) -> Any:
        try:
            return fn(*args)
        except Exception as exc:
            self._log_error(where, exc)
            return None

    # ------------------------------------------------------------------ wiring report
    def wiring_report(self) -> Dict[str, dict]:
        """Status of all 20 classes: live or unavailable, and how each one is reached."""
        via = {
            "NBLDomain": "node.group42.nns (records of NEBULANameService)",
            "YieldOptimizer": "node.group42.yield_optimizer",
            "DollarCostAverager": "node.group42.dca (driven by on_connect + price_provider)",
            "ConfidentialTransaction": "node.group42.confidential_create()",
            "PrivacyPoolV2": "node.group42.privacy",
            "NEBULANameService": "node.group42.nns",
            "EcosystemHub": "node.group42.hub (fed by on_connect / on_reorg)",
            "VoteEscrowedNBL": "node.group42.venbl",
            "MEVProtector": "node.group42.mev (block scan, commit/reveal facade)",
            "CrossMarginAccount": "node.group42.cross_margin (accounts)",
            "CrossMarginEngine": "node.group42.cross_margin",
            "InterestRateModel": "node.group42.irm (shared by every lending pool)",
            "LendingPoolV2": "node.group42.lending (pools)",
            "LendingProtocolV2": "node.group42.lending",
            "VaultStrategy": "node.group42.vaults (vaults)",
            "VaultManager": "node.group42.vaults",
            "FractionalNFTDex": "node.group42.nft_dex",
            "TokenomicsEngine": "node.group42.tokenomics",
            "SybilResistanceScore": "node.group42.sybil",
            "BlockchainIndexer": "node.group42.indexer (fed by on_connect / on_reorg)",
        }
        report: Dict[str, dict] = {}
        for name in GROUP42_CLASSES:
            reason = self.unavailable.get(name)
            report[name] = {"status": "unavailable" if reason else "live",
                            "via": via[name], "reason": reason}
        return report

    # ------------------------------------------------------------------ chain listener
    def on_connect(self, block: Any) -> None:
        """Called by the chain for every connected block. Never raises."""
        if self._detached:
            return
        try:
            height = self._block_height(block)
            with self._lock:
                self.blocks_seen += 1
                self.last_height = height
            if self.cfg.enable_indexer and self.indexer is not None:
                self._safe("indexer.connect", self._index_connect, block, height)
            if self.cfg.enable_hub_events and self.hub is not None:
                self._safe("hub.block_event", self._hub_block_event, block, height)
            if self.cfg.enable_mev_scan and self.mev is not None:
                self._safe("mev.scan", self._mev_scan_block, block)
            if self.cfg.enable_dca and self.dca is not None:
                self._safe("dca.step", self._dca_step, height)
            if self.cfg.margin_check_interval > 0 and self.cross_margin is not None \
                    and height % self.cfg.margin_check_interval == 0:
                self._safe("margin.scan", self._margin_scan)
            if self.cfg.vault_harvest_interval > 0 and self.vaults is not None \
                    and height % self.cfg.vault_harvest_interval == 0:
                self._safe("vault.harvest", self._vault_harvest, height)
        except Exception as exc:
            self._log_error("on_connect", exc)

    def on_reorg(self, old: Any, new: Any, ancestor_height: int) -> None:
        """Called on a chain reorganisation. Never raises."""
        if self._detached:
            return
        try:
            with self._lock:
                self.reorgs_seen += 1
            if self.indexer is not None:
                self._safe("indexer.rollback", self._rollback_indexer, int(ancestor_height))
            if self.cfg.enable_hub_events and self.hub is not None:
                self._safe("hub.reorg_event", self._hub_event, "reorg",
                           f"Reorg above height {ancestor_height}",
                           {"ancestor_height": int(ancestor_height),
                            "old_len": self._safe_len(old), "new_len": self._safe_len(new)})
        except Exception as exc:
            self._log_error("on_reorg", exc)

    def detach(self) -> None:
        self._detached = True
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer42.detach", exc_info=True)

    # ------------------------------------------------------------------ listener internals
    def _block_height(self, block: Any) -> int:
        h = getattr(block, "height", None)
        return int(h) if isinstance(h, int) else int(self.bc.height)

    @staticmethod
    def _safe_len(x: Any) -> int:
        try:
            return len(x)
        except Exception:
            return -1

    def _index_connect(self, block: Any, height: int) -> None:
        ix = self.indexer
        last = ix._last_indexed
        if height <= last:
            # A block at or below the indexed tip means the chain replaced blocks: drop stale data.
            self._rollback_indexer(height - 1)
            last = ix._last_indexed
        self.index_catch_up(upto=height, tip_block=block)

    def index_catch_up(self, upto: Optional[int] = None, tip_block: Any = None) -> int:
        """Index sequentially from last_indexed+1, at most ``index_catchup_batch`` blocks per call."""
        ix = self.indexer
        if ix is None:
            return 0
        upto = self.bc.height if upto is None else upto
        start = ix._last_indexed + 1
        end = min(upto, ix._last_indexed + max(1, self.cfg.index_catchup_batch))
        done = 0
        for h in range(start, end + 1):
            blk = tip_block if (tip_block is not None and h == upto) else self.bc.get_block(h)
            if blk is None:
                break                                   # keep the index strictly sequential
            ix.index_block(blk)
            done += 1
        return done

    def _rollback_indexer(self, ancestor_height: int) -> None:
        """Remove every indexed block/tx above ``ancestor_height`` (BlockchainIndexer has no undo)."""
        ix = self.indexer
        with ix._lock:
            for h in [h for h in ix._block_index if h > ancestor_height]:
                del ix._block_index[h]
            dead = {t for t, info in ix._tx_index.items() if info["block"] > ancestor_height}
            for t in dead:
                del ix._tx_index[t]
            if dead:
                for addr in list(ix._addr_index):
                    kept = [t for t in ix._addr_index[addr] if t not in dead]
                    if kept:
                        ix._addr_index[addr] = kept
                    else:
                        del ix._addr_index[addr]
            ix._last_indexed = min(ix._last_indexed, ancestor_height)

    def _hub_event(self, kind: str, title: str, data: dict) -> None:
        with self._lock:
            self.hub.emit_ecosystem_event(kind, title, data)
            over = len(self.hub._events) - self.cfg.hub_event_limit
            if over > 0:
                del self.hub._events[:over]

    def _hub_block_event(self, block: Any, height: int) -> None:
        self._hub_event("block", f"Block {height} connected",
                        {"height": height, "hash": str(getattr(block, "hash", ""))})

    @staticmethod
    def _is_coinbase(tx: Any, index: int) -> bool:
        flag = getattr(tx, "is_coinbase", None)
        if callable(flag):
            return bool(flag())
        if flag is not None:
            return bool(flag)
        return index == 0

    def _mev_scan_block(self, block: Any) -> None:
        for i, tx in enumerate(getattr(block, "transactions", []) or []):
            if self._is_coinbase(tx, i):
                continue
            try:
                if self.mev.detect_sandwich(tx):
                    self.mev_flagged.append(str(getattr(tx, "txid", "")))
            except Exception:
                with self._lock:
                    self.mev_scan_errors += 1           # counted separately, not fatal, not spammy

    def _dca_step(self, height: int) -> None:
        if self.price_provider is None:
            with self._lock:
                self.dca_skipped_no_price += 1
            return
        price = self.price_provider()
        if not _pos_number(price):
            with self._lock:
                self.dca_skipped_no_price += 1
            return
        if self.dca.should_execute(height):
            self.dca.record_execution(height, float(price))

    def _margin_scan(self) -> None:
        self.margin_calls_last = list(self.cross_margin.check_margin_calls())

    def _vault_harvest(self, height: int) -> None:
        self.last_harvest = dict(self.vaults.harvest_all())

    # ======================================================================================
    # Facade methods (validated entry points for RPC / REST / other modules)
    # ======================================================================================
    # ---------------------------------------------------------------- name service + domain
    def nns_register(self, label: str, owner: str, years: int = 1) -> Tuple[bool, str]:
        if self.nns is None:
            return False, "Name service unavailable"
        if not isinstance(label, str) or not _LABEL_RE.match(label.lower()):
            return False, "Invalid label: use 3-63 chars of a-z, 0-9 and '-', no dots"
        if not _nonempty_str(owner) or not (isinstance(years, int) and 1 <= years <= 10):
            return False, "Invalid owner or years (1..10)"
        return self.nns.register(label, owner, years)

    def nns_set_subdomain(self, parent: str, label: str, owner: str, resolver: str) -> Tuple[bool, str]:
        if self.nns is None:
            return False, "Name service unavailable"
        if not isinstance(label, str) or not _LABEL_RE.match(label.lower()):
            return False, "Invalid subdomain label"
        if not (_nonempty_str(parent) and _nonempty_str(owner) and _nonempty_str(resolver)):
            return False, "Invalid arguments"
        parent_d = self.nns._domains.get(parent.lower())
        if parent_d is not None and parent_d.is_expired:
            return False, "Parent domain expired"
        return self.nns.set_subdomain(parent, label.lower(), owner, resolver)

    # ---------------------------------------------------------------- lending
    def lending_create_pool(self, asset: str) -> Tuple[bool, str]:
        if self.lending is None:
            return False, "Lending unavailable"
        if not _nonempty_str(asset, 32):
            return False, "Invalid asset"
        with self.lending._lock:
            if asset in self.lending._pools:
                return False, "Pool already exists"     # original create_pool would overwrite it
            self.lending.create_pool(asset)
            if self.irm is not None:
                self.lending._pools[asset].irm = self.irm   # one shared rate model
        return True, asset

    def lending_deposit(self, address: str, asset: str, amount_nbl: float) -> Tuple[bool, str]:
        if self.lending is None:
            return False, "Lending unavailable"
        if not (_nonempty_str(address) and _pos_number(amount_nbl)):
            return False, "Invalid arguments"
        if self.bc.utxo.balance(address) < int(amount_nbl * _UNIT):
            return False, "Insufficient balance"
        return self.lending.deposit(address, asset, amount_nbl)

    def lending_borrow(self, address: str, asset: str, amount_nbl: float,
                       collateral_nbl: float) -> Tuple[bool, str]:
        if self.lending is None:
            return False, "Lending unavailable"
        if not (_nonempty_str(address) and _pos_number(amount_nbl) and _pos_number(collateral_nbl)):
            return False, "Invalid arguments"
        pool = self.lending._pools.get(asset)
        if pool is None:
            return False, "Pool not found"
        if address in pool._loans:
            return False, "Existing loan on this pool (the original code would overwrite the debt)"
        if self.bc.utxo.balance(address) < int(collateral_nbl * _UNIT):
            return False, "Insufficient collateral balance"
        return self.lending.borrow(address, asset, amount_nbl, collateral_nbl)

    # ---------------------------------------------------------------- vaults
    def vault_deposit(self, vault_id: str, depositor: str, amount_nbl: float) -> Tuple[bool, int]:
        if self.vaults is None or not (_nonempty_str(depositor) and _pos_number(amount_nbl)):
            return False, 0
        vault = self.vaults._vaults.get(vault_id)
        if vault is None:
            return False, 0
        amount = int(amount_nbl * _UNIT)
        if amount <= 0:
            return False, 0
        if vault.total_shares and vault.total_assets and \
                amount * vault.total_shares // vault.total_assets == 0:
            return False, 0                             # would mint 0 shares and lose the deposit
        return self.vaults.deposit(vault_id, depositor, amount_nbl)

    def vault_withdraw(self, vault_id: str, depositor: str, shares: int) -> Tuple[bool, int]:
        if self.vaults is None or not (_nonempty_str(depositor) and _pos_int(shares)):
            return False, 0
        return self.vaults.withdraw(vault_id, depositor, shares)

    def vault_harvest_now(self) -> dict:
        """Explicit call only. NOTE: harvest_all credits SIMULATED yield (0.01% of assets)."""
        return self.vaults.harvest_all() if self.vaults is not None else {}

    # ---------------------------------------------------------------- veNBL
    def venbl_lock(self, address: str, amount: int, lock_blocks: int) -> Tuple[bool, str]:
        if self.venbl is None:
            return False, "veNBL unavailable"
        if not (_nonempty_str(address) and _pos_int(amount) and _pos_int(lock_blocks)):
            return False, "Invalid arguments"
        already = self.venbl._locks.get(address, {}).get("amount", 0)
        if self.bc.utxo.balance(address) < already + amount:
            return False, "Insufficient unlocked balance (existing lock counts)"
        return self.venbl.lock(address, amount, lock_blocks)

    # ---------------------------------------------------------------- privacy pool
    def privacy_deposit(self, sender: str, denomination: int, nullifier: str) -> Tuple[bool, str]:
        if self.privacy is None:
            return False, "Privacy pool unavailable"
        if not (_nonempty_str(sender) and isinstance(nullifier, str) and 16 <= len(nullifier) <= 128):
            return False, "Invalid sender or nullifier (16..128 chars)"
        return self.privacy.deposit(sender, denomination, nullifier)

    def privacy_withdraw(self, recipient: str, denomination: int, nullifier: str,
                         proof: str) -> Tuple[bool, str]:
        if self.privacy is None:
            return False, "Privacy pool unavailable"
        if not (_nonempty_str(recipient) and isinstance(nullifier, str) and 16 <= len(nullifier) <= 128):
            return False, "Invalid recipient or nullifier"
        return self.privacy.withdraw(recipient, denomination, nullifier, proof)

    # ---------------------------------------------------------------- confidential tx
    def confidential_create(self, sender: str, recipient: str, amount: int,
                            blinding_factor: int) -> Tuple[bool, Any]:
        if "ConfidentialTransaction" in self.unavailable:
            return False, self.unavailable["ConfidentialTransaction"]
        if not (_nonempty_str(sender) and _nonempty_str(recipient)):
            return False, "Invalid sender/recipient"
        if not (isinstance(amount, int) and not isinstance(amount, bool) and amount >= 0
                and _pos_int(blinding_factor)):
            return False, "amount must be int >= 0 and blinding_factor int > 0"
        try:
            ctx = g.ConfidentialTransaction(sender, recipient, amount, blinding_factor)
        except Exception as exc:
            self._log_error("confidential.create", exc)
            return False, f"{type(exc).__name__}: {exc}"
        with self._lock:
            self._confidential[ctx.tx_id] = ctx
            while len(self._confidential) > self.cfg.confidential_registry_limit:
                self._confidential.popitem(last=False)
        return True, ctx.to_dict()

    def confidential_verify_sum(self, tx_id_a: str, tx_id_b: str) -> Tuple[bool, str]:
        a, b = self._confidential.get(tx_id_a), self._confidential.get(tx_id_b)
        if a is None or b is None:
            return False, "Unknown confidential transaction"
        try:
            return bool(a.verify_sum(b)), "ok"
        except Exception as exc:
            self._log_error("confidential.verify_sum", exc)
            return False, f"{type(exc).__name__}: {exc}"

    # ---------------------------------------------------------------- cross margin
    def margin_open_account(self, address: str, collateral_nbl: float) -> Tuple[bool, str]:
        if self.cross_margin is None or not (_nonempty_str(address) and _pos_number(collateral_nbl)):
            return False, "Invalid arguments or engine unavailable"
        return self.cross_margin.open_account(address, collateral_nbl)

    def margin_deposit(self, address: str, amount_nbl: float) -> Tuple[bool, str]:
        if self.cross_margin is None or not (_nonempty_str(address) and _pos_number(amount_nbl)):
            return False, "Invalid arguments or engine unavailable"
        return self.cross_margin.deposit_collateral(address, amount_nbl)

    def margin_liquidate(self, address: str) -> Tuple[bool, str]:
        """Explicit call only; the layer itself never liquidates automatically."""
        if self.cross_margin is None or not _nonempty_str(address):
            return False, "Invalid arguments or engine unavailable"
        return self.cross_margin.liquidate_account(address)

    # ---------------------------------------------------------------- MEV commit/reveal
    def mev_commit(self, tx_hash_hex: str, secret_hex: str) -> Tuple[bool, str]:
        if self.mev is None:
            return False, "MEV protector unavailable"
        try:
            tx_hash, secret = bytes.fromhex(tx_hash_hex), bytes.fromhex(secret_hex)
        except (ValueError, TypeError):
            return False, "tx_hash and secret must be hex strings"
        if len(secret) < 16:
            return False, "secret must be at least 16 bytes"
        return True, self.mev.commit(tx_hash, secret)

    def mev_reveal(self, commitment: str, tx: Any, secret_hex: str) -> Tuple[bool, str]:
        if self.mev is None:
            return False, "MEV protector unavailable"
        try:
            secret = bytes.fromhex(secret_hex)
        except (ValueError, TypeError):
            return False, "secret must be a hex string"
        return self.mev.reveal(commitment, tx, secret)

    # ---------------------------------------------------------------- sybil score
    def sybil_score(self, address: str) -> Optional[dict]:
        if self.sybil is None or not _nonempty_str(address):
            return None
        return self.sybil.compute(address)

    def sybil_verify(self, address: str, did_proof: str = "") -> bool:
        """SybilResistanceScore.verify_identity accepts anything, so it is gated here:
        without a configured ``identity_verifier`` the call is refused."""
        if self.sybil is None or self.identity_verifier is None or not _nonempty_str(address):
            return False
        try:
            if not self.identity_verifier(address, did_proof):
                return False
        except Exception as exc:
            self._log_error("sybil.verifier", exc)
            return False
        return bool(self.sybil.verify_identity(address, did_proof))

    # ---------------------------------------------------------------- tokenomics
    def record_burn(self, amount: int, reason: str = "") -> bool:
        """Ledger entry only (TokenomicsEngine.burn_tokens does not touch the UTXO set)."""
        if self.tokenomics is None or not _pos_int(amount):
            return False
        if amount > self.tokenomics.effective_supply():
            return False
        return self.tokenomics.burn_tokens(amount, str(reason)[:200])

    # ---------------------------------------------------------------- ecosystem hub
    def hub_register_dapp(self, name: str, url: str, category: str, description: str = "") -> Optional[str]:
        if self.hub is None or not _nonempty_str(name, 64):
            return None
        if not (isinstance(url, str) and re.match(r"^https?://[^\s]{3,200}$", url)):
            return None
        if category not in ECOSYSTEM_CATEGORIES:
            return None
        with self._lock:
            return self.hub.register_dapp(name.strip(), url, category, str(description)[:500])

    # ---------------------------------------------------------------- NFT DEX
    def nft_list(self, vault_id: str, seller: str, amount: int, price: float) -> Tuple[bool, str]:
        if self.nft_dex is None:
            return False, self.unavailable.get("FractionalNFTDex", "NFT DEX unavailable")
        if not (_nonempty_str(vault_id) and _nonempty_str(seller) and _pos_int(amount) and _pos_number(price)):
            return False, "Invalid arguments"
        return self.nft_dex.list_fractions(vault_id, seller, amount, price)

    def nft_buy(self, buyer: str, listing_id: str, amount: int) -> Tuple[bool, str]:
        if self.nft_dex is None:
            return False, self.unavailable.get("FractionalNFTDex", "NFT DEX unavailable")
        if not (_nonempty_str(buyer) and _nonempty_str(listing_id) and _pos_int(amount)):
            return False, "Invalid arguments"
        return self.nft_dex.buy_fractions(buyer, listing_id, amount)

    # ======================================================================================
    # Read-only status / API
    # ======================================================================================
    def strategies_report(self) -> dict:
        out: dict = {}
        if self.yield_optimizer is not None:
            out["yield_options"] = self.yield_optimizer.find_best_yield()
            out["yield_low_risk"] = self.yield_optimizer.risk_adjusted_yield("low")
        if self.dca is not None:
            out["dca"] = self.dca.dca_stats()
            out["dca_skipped_no_price"] = self.dca_skipped_no_price
        return out

    def status(self) -> dict:
        def part(fn: Optional[Callable[[], Any]]) -> Any:
            if fn is None:
                return None
            try:
                return fn()
            except Exception as exc:
                self._log_error("status", exc)
                return {"error": f"{type(exc).__name__}: {exc}"}
        return {
            "layer": {
                "blocks_seen": self.blocks_seen, "reorgs_seen": self.reorgs_seen,
                "last_height": self.last_height, "errors": self.errors,
                "unavailable": dict(self.unavailable),
                "mev_flagged": len(self.mev_flagged), "mev_scan_errors": self.mev_scan_errors,
                "margin_calls_pending": len(self.margin_calls_last),
                "index_lag": (self.bc.height - self.indexer._last_indexed) if self.indexer else None,
            },
            "indexer": part(self.indexer.index_stats if self.indexer else None),
            "tokenomics": part(self.tokenomics.tokenomics_report if self.tokenomics else None),
            "nns": part(self.nns.nns_stats if self.nns else None),
            "lending": part(self.lending.protocol_stats_v2 if self.lending else None),
            "vaults": part(self.vaults.all_vaults if self.vaults else None),
            "venbl": part(self.venbl.venbl_stats if self.venbl else None),
            "privacy_pool": part(self.privacy.pool_stats if self.privacy else None),
            "cross_margin": part(self.cross_margin.cross_margin_stats if self.cross_margin else None),
            "mev": part(self.mev.mev_stats if self.mev else None),
            "hub": part(self.hub.full_ecosystem_stats if self.hub else None),
            "strategies": part(self.strategies_report),
        }

    def api_get(self, path: str) -> Tuple[int, dict]:
        """Read-only dispatcher, independent of the host's @route decorator.
        Example: layer.api_get('/api/g42/index/block/10') -> (200, {...})."""
        try:
            p = path.split("?", 1)[0].rstrip("/")
            parts = [x for x in p.split("/") if x]
            if parts[:2] != ["api", "g42"] or len(parts) < 3:
                return 404, {"error": "unknown path"}
            head, rest = parts[2], parts[3:]
            simple = {
                "status": self.status,
                "wiring": self.wiring_report,
                "tokenomics": lambda: self.tokenomics.tokenomics_report(),
                "halving": lambda: self.tokenomics.halving_schedule(),
                "vaults": lambda: self.vaults.all_vaults(),
                "lending": lambda: self.lending.protocol_stats_v2(),
                "venbl": lambda: self.venbl.venbl_stats(),
                "privacy": lambda: self.privacy.pool_stats(),
                "crossmargin": lambda: self.cross_margin.cross_margin_stats(),
                "mev": lambda: self.mev.mev_stats(),
                "hub": lambda: self.hub.full_ecosystem_stats(),
                "strategies": self.strategies_report,
            }
            if head in simple and not rest:
                return 200, {"success": True, "data": simple[head]()}
            if head == "nns" and rest == ["stats"]:
                return 200, {"success": True, "data": self.nns.nns_stats()}
            if head == "nns" and len(rest) == 2 and rest[0] == "resolve":
                addr = self.nns.resolve(rest[1])
                return (200, {"success": True, "data": {"name": rest[1], "address": addr}}) if addr \
                    else (404, {"error": "not found"})
            if head == "index" and len(rest) == 2:
                kind, key = rest
                if kind == "block" and key.isdigit():
                    d = self.indexer.query_block(int(key))
                elif kind == "tx":
                    d = self.indexer.query_tx(key)
                elif kind == "address":
                    d = self.indexer.query_address(key)
                else:
                    return 404, {"error": "unknown index query"}
                return (200, {"success": True, "data": d}) if d else (404, {"error": "not found"})
            if head == "sybil" and len(rest) == 1:
                return 200, {"success": True, "data": self.sybil.compute(rest[0])}
            return 404, {"error": "unknown path"}
        except Exception as exc:
            self._log_error("api_get", exc)
            return 500, {"error": "internal error"}


# --------------------------------------------------------------------------------------
# install / uninstall (wraps NEBULAFullNode.__init__, same pattern as group 5)
# --------------------------------------------------------------------------------------
def install(host: Any, **layer_kwargs: Any) -> None:
    """Attach a Layer42 to every NEBULAFullNode created after this call.
    ``layer_kwargs`` are forwarded to Layer42 (config, price_provider, identity_verifier)."""
    cls = host.NEBULAFullNode
    if getattr(cls, "_g42_orig", None):
        return
    orig = cls.__init__

    def patched(self: Any, *a: Any, **k: Any) -> None:
        orig(self, *a, **k)
        try:
            layer = Layer42(self, **layer_kwargs)
            self.group42 = layer
            self.bc.add_listener(layer)
        except Exception as exc:                        # the node must still start
            self.group42_error = exc

    cls._g42_orig = orig
    cls.__init__ = patched


def uninstall(host: Any) -> None:
    cls = host.NEBULAFullNode
    orig = getattr(cls, "_g42_orig", None)
    if orig:
        cls.__init__ = orig
        del cls._g42_orig
