"""nebula_group37_install.py - additive wiring layer for NEBULA group37.

Wires ALL 20 group37 classes into the running chain WITHOUT editing
nebula_v10_11.py and WITHOUT editing nebula_group37.py (which stays verbatim).

Usage (same pattern as the earlier groups):

    import nebula_v10_11 as host
    import nebula_group37_install as g37
    g37.install(host)          # patch NEBULAFullNode.__init__ (+ optional hooks)
    node = host.NEBULAFullNode(...)
    node.group37.status()      # live counters, errors, discovered dependencies
    node.group37.wiring_report()   # per-class wiring map (all 20 classes)
    g37.uninstall(host)        # restore every patched method

Design rules (from the group37 guide):
  * The original host method ALWAYS runs first; our code runs after it.
  * The layer never rejects a block, a transaction or a peer message.
    Every callback is wrapped in try/except; failures are counted in
    layer.errors and the host continues exactly as before.
  * Observation first: nothing here changes consensus. Liquidations are
    report-only until you call layer.enable_liquidations(True).
  * Remote peers cannot mutate layer state: no state-changing P2P handler is
    registered by default (messages are unauthenticated).

What is NOT done here (cannot be done without editing the host file):
  * REST routes are not registered automatically. layer.rest_handlers()
    returns a {path: callable} map you can hand to the host's route system.
"""
from __future__ import annotations

import logging
import statistics
import threading
import time
from collections import defaultdict, deque
from typing import Any, Callable, Dict, List, Optional, Tuple

import nebula_group37 as g
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.group37")

_MISSING = object()
_LAYERS: List["Layer37"] = []
_LAYERS_LOCK = threading.RLock()
# (owner_class, attribute_name, original_or__MISSING) - used by uninstall()
_PATCHES: List[Tuple[Any, str, Any]] = []


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------
def _get(obj: Any, key: str, default: Any = None) -> Any:
    """Read a key from a dict or an attribute from an object."""
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _ensure_compat_names() -> None:
    """OracleV2.update_price() refers to the name OracleFeedC, which in the
    host is created at module level right after OracleFeed.  When group37 is
    imported without the host (or the host does not export it) that name is
    missing and update_price() on a NEW pair would raise NameError.

    We build it from the helper (_make_compat) that group37 already carries,
    and only if it is absent.  nebula_group37.py itself is not modified.
    """
    if hasattr(g, "OracleFeedC"):
        return
    g.OracleFeedC = g._make_compat(
        g.OracleFeed,
        aliases=None,
        extra_defaults={
            "feed_type": lambda: g.OracleFeedType.CUSTOM,
            "description": "",
        },
        post=g._v108_feed_post,
        name="OracleFeedC",
    )


def _find_instance(roots: List[Any], type_names: Tuple[str, ...]) -> Optional[Any]:
    """Find an attribute value whose class (or a base class) has one of the
    given names. Looks one level deep inside each root object."""
    seen = set()
    for root in roots:
        if root is None:
            continue
        for value in list(getattr(root, "__dict__", {}).values()):
            if id(value) in seen:
                continue
            seen.add(id(value))
            try:
                if any(c.__name__ in type_names for c in type(value).__mro__):
                    return value
            except Exception:
                continue
    return None


def _peer_endpoint(peer: Any) -> Optional[Tuple[str, int]]:
    """Best-effort (ip, port) extraction from a host peer object."""
    ip: Optional[str] = None
    port: Optional[int] = None
    for key in ("ip", "host", "address"):
        v = _get(peer, key)
        if isinstance(v, str) and v:
            ip = v
            break
    v = _get(peer, "port")
    if isinstance(v, int) and not isinstance(v, bool):
        port = v
    if ip is None:
        addr = _get(peer, "addr")
        if isinstance(addr, (tuple, list)) and len(addr) >= 2:
            ip, port = str(addr[0]), int(addr[1])
        elif isinstance(addr, str) and ":" in addr:
            host_part, _, port_part = addr.rpartition(":")
            if host_part and port_part.isdigit():
                ip, port = host_part, int(port_part)
    if ip and port is not None:
        return ip, port
    return None


# --------------------------------------------------------------------------
# PeerBook - gives DiscoveredPeer a live home (fed by the P2P hook)
# --------------------------------------------------------------------------
class PeerBook:
    """Bounded table of DiscoveredPeer records, fed from P2P traffic."""

    MAX_PEERS = 2048

    def __init__(self) -> None:
        self._peers: Dict[Tuple[str, int], g.DiscoveredPeer] = {}
        self._lock = threading.RLock()

    def observe(self, ip: str, port: int, height: int = 0,
                version: Optional[int] = None, user_agent: str = "",
                discovery: str = "p2p") -> g.DiscoveredPeer:
        now = time.time()
        key = (ip, port)
        with self._lock:
            p = self._peers.get(key)
            if p is None:
                if len(self._peers) >= self.MAX_PEERS:
                    worst = min(self._peers, key=lambda k: self._peers[k].score())
                    del self._peers[worst]
                p = g.DiscoveredPeer(ip=ip, port=port, last_seen=now,
                                     discovery=discovery)
                self._peers[key] = p
            p.last_seen = now
            if isinstance(height, int) and height > 0:
                p.height = height
            if isinstance(version, int) and version > 0:
                p.version = version
            if user_agent:
                p.user_agent = str(user_agent)[:128]
            return p

    def count(self) -> int:
        with self._lock:
            return len(self._peers)

    def best(self, n: int = 10) -> List[dict]:
        with self._lock:
            ranked = sorted(self._peers.values(), key=lambda p: p.score(),
                            reverse=True)
            return [p.to_dict() for p in ranked[:n]]


# --------------------------------------------------------------------------
# NFTListingBook - gives NFTListing / NFTAuctionType a live home
# --------------------------------------------------------------------------
class NFTListingBook:
    """RECORD-ONLY order book for NFTListing objects.

    No NBL or NFT ownership is moved here (the group has no settlement
    code); sales are only recorded so a marketplace layer can read them.
    """

    MAX_LISTINGS = 10_000

    def __init__(self, chain_height: Callable[[], int]) -> None:
        self._height = chain_height
        self._listings: Dict[str, g.NFTListing] = {}
        self._start_blocks: Dict[str, int] = {}
        self._lock = threading.RLock()
        self._seq = 0

    @staticmethod
    def _coerce_type(t: Any) -> Optional[g.NFTAuctionType]:
        if isinstance(t, g.NFTAuctionType):
            return t
        try:
            return g.NFTAuctionType(str(t))
        except ValueError:
            return None

    def create_listing(self, seller: str, collection_id: str, token_id: int,
                       auction_type: Any, start_price: int, reserve: int = 0,
                       end_block: int = 0, dutch_end_price: int = 0,
                       dutch_blocks: int = 0) -> Tuple[bool, str]:
        atype = self._coerce_type(auction_type)
        if atype is None:
            return False, "Unknown auction type"
        if start_price <= 0:
            return False, "start_price must be positive"
        if atype is g.NFTAuctionType.DUTCH and not (
                0 <= dutch_end_price < start_price and dutch_blocks > 0):
            return False, "Dutch auction needs dutch_end_price < start_price and dutch_blocks > 0"
        with self._lock:
            if len(self._listings) >= self.MAX_LISTINGS:
                return False, "Listing book full"
            for l in self._listings.values():
                if (not l.sold and l.collection_id == collection_id
                        and l.token_id == token_id):
                    return False, "Token already listed"
            self._seq += 1
            lid = f"NFTL-{self._seq:08d}"
            self._listings[lid] = g.NFTListing(
                listing_id=lid, collection_id=collection_id,
                token_id=token_id, seller=seller, auction_type=atype,
                start_price=start_price, reserve=reserve, end_block=end_block,
                dutch_end_price=dutch_end_price, dutch_blocks=dutch_blocks)
            self._start_blocks[lid] = self._height()
            return True, lid

    def current_price(self, listing_id: str) -> Optional[int]:
        with self._lock:
            l = self._listings.get(listing_id)
            if l is None:
                return None
            return l.current_dutch_price(self._height(),
                                         self._start_blocks[listing_id])

    def place_bid(self, listing_id: str, bidder: str,
                  amount: int) -> Tuple[bool, str]:
        with self._lock:
            l = self._listings.get(listing_id)
            if l is None or l.sold:
                return False, "Listing unavailable"
            if l.auction_type not in (g.NFTAuctionType.ENGLISH,
                                      g.NFTAuctionType.SEALED_BID):
                return False, "Not a bid-based listing"
            if bidder == l.seller:
                return False, "Seller cannot bid"
            if l.end_block and self._height() >= l.end_block:
                return False, "Auction ended"
            if amount < l.start_price or amount <= l.highest_bid:
                return False, "Bid too low"
            l.bids.append({"bidder": bidder, "amount": amount,
                           "block": self._height()})
            l.highest_bid, l.highest_bidder = amount, bidder
            return True, f"Bid recorded ({amount})"

    def buy(self, listing_id: str, buyer: str) -> Tuple[bool, str]:
        with self._lock:
            l = self._listings.get(listing_id)
            if l is None or l.sold:
                return False, "Listing unavailable"
            if l.auction_type not in (g.NFTAuctionType.FIXED_PRICE,
                                      g.NFTAuctionType.DUTCH):
                return False, "Not a buy-now listing"
            if buyer == l.seller:
                return False, "Seller cannot buy"
            price = l.current_dutch_price(self._height(),
                                          self._start_blocks[listing_id])
            l.sold, l.highest_bid, l.highest_bidder = True, price, buyer
            return True, f"Sale recorded at {price}"

    def finalize(self, listing_id: str) -> Tuple[bool, str]:
        with self._lock:
            l = self._listings.get(listing_id)
            if l is None or l.sold:
                return False, "Listing unavailable"
            if l.auction_type not in (g.NFTAuctionType.ENGLISH,
                                      g.NFTAuctionType.SEALED_BID):
                return False, "Not a bid-based listing"
            if not l.end_block or self._height() < l.end_block:
                return False, "Auction not ended yet"
            if l.highest_bid <= 0 or l.highest_bid < l.reserve:
                return False, "Reserve not met / no bids"
            l.sold = True
            return True, f"Sold to {l.highest_bidder} at {l.highest_bid}"

    def get(self, listing_id: str) -> Optional[dict]:
        with self._lock:
            l = self._listings.get(listing_id)
            return l.to_dict() if l else None

    def count(self) -> int:
        with self._lock:
            return len(self._listings)

    def stats(self) -> dict:
        with self._lock:
            sold = sum(1 for l in self._listings.values() if l.sold)
            return {"listings": len(self._listings), "sold": sold,
                    "active": len(self._listings) - sold}


# --------------------------------------------------------------------------
# Layer37 - holds all 20 classes' live instances
# --------------------------------------------------------------------------
class Layer37:
    """Chain listener + service holder for group37.

    Chain listener API expected by the host (confirmed in the guide):
        bc.add_listener(layer) -> layer.on_connect(block)
                                  layer.on_reorg(old, new, ancestor_height)
    """

    LIQ_CHECK_EVERY = 10        # blocks between at-risk CDP scans
    GAS_SAMPLES = 50            # recent fee-rate samples kept for GAS_PRICE

    def __init__(self, node: Any, host: Any = None) -> None:
        self.node = node
        self.host = host
        self.bc = node.bc
        self.errors = 0
        self.last_error = ""
        self.counters: Dict[str, int] = defaultdict(int)
        self.auto_liquidations = False
        self.at_risk_cdps: List[str] = []
        self.stablecoin_mechanism = g.StablecoinMechanism.COLLATERAL
        self._lock = threading.RLock()
        self._gas: deque = deque(maxlen=self.GAS_SAMPLES)
        self._handlers: Dict[str, Callable[[Any, Any], None]] = {}

        _ensure_compat_names()

        self.oracle = self._build("oracle", lambda: g.OracleV2(self.bc))
        self.stablecoin = self._build(
            "stablecoin",
            lambda: g.StablecoinProtocol(self.bc, self.oracle)
            if self.oracle is not None else None)
        self.lightning = self._build("lightning",
                                     lambda: g.LightningNetworkV2(self.bc))
        self.governance = self._build("governance",
                                      lambda: g.GovernanceV2(self.bc))
        self.multisig = self._build("multisig",
                                    lambda: g.MultisigManagerV2(self.bc))

        roots = [node, self.bc] + [
            v for v in list(getattr(node, "__dict__", {}).values())
            if hasattr(v, "__dict__") and not isinstance(v, (type, Layer37))
        ]
        self.dex = _find_instance(roots, ("NEBULADex",))
        self.tx_index = _find_instance(roots, ("TransactionIndex",))
        self.analytics = _find_instance(roots, ("ChainAnalytics",))

        self.aggregator = None
        if self.dex is not None:
            self.aggregator = self._build(
                "aggregator", lambda: g.DeFiAggregatorV2(self.dex, self.bc))
        self.explorer = self._build(
            "explorer",
            lambda: g.BlockExplorerBackend(self.bc, self.tx_index,
                                           self.analytics))
        self.peers = PeerBook()
        self.nfts = NFTListingBook(lambda: int(getattr(self.bc, "height", 0)))

    # ---- construction helper -------------------------------------------
    def _build(self, name: str, factory: Callable[[], Any]) -> Any:
        try:
            return factory()
        except Exception as e:                       # never stop node start-up
            self._fail(f"build:{name}", e)
            return None

    def _fail(self, where: str, exc: BaseException) -> None:
        with self._lock:
            self.errors += 1
            self.last_error = f"{where}: {type(exc).__name__}: {exc}"
        log.warning("group37 %s failed: %s", where, exc)

    def _count(self, key: str, n: int = 1) -> None:
        with self._lock:
            self.counters[key] += n

    # ---- late binding ---------------------------------------------------
    def attach_dex(self, dex: Any) -> bool:
        """Bind the DEX later if it was not discoverable on the node."""
        self.dex = dex
        self.aggregator = self._build(
            "aggregator", lambda: g.DeFiAggregatorV2(dex, self.bc))
        return self.aggregator is not None

    def enable_liquidations(self, flag: bool = True) -> None:
        """Default is report-only. When enabled, check_liquidations() runs
        (it flags CDPs inside StablecoinProtocol only; no chain effect)."""
        self.auto_liquidations = bool(flag)

    def register_message_handler(self, msg_type: str,
                                 fn: Callable[[Any, Any], None]) -> None:
        """Optional P2P dispatch table (runs AFTER the host handler)."""
        self._handlers[str(msg_type)] = fn

    # ---- chain listener -------------------------------------------------
    def on_connect(self, block: Any) -> None:
        try:
            self._count("blocks_seen")
            self.counters["last_height"] = int(_get(block, "height", 0) or 0)
            n = self.counters["blocks_seen"]
            if self.stablecoin is not None and n % self.LIQ_CHECK_EVERY == 0:
                self.at_risk_cdps = self.cdps_at_risk()
                self.counters["cdps_at_risk"] = len(self.at_risk_cdps)
                if self.auto_liquidations and self.at_risk_cdps:
                    done = self.stablecoin.check_liquidations()
                    self._count("cdps_liquidated", len(done))
        except Exception as e:
            self._fail("on_connect", e)

    def on_reorg(self, old: Any, new: Any, ancestor_height: Any) -> None:
        # All group37 state is off-chain / in-memory and is not derived from
        # block contents, so there is nothing to rewind; just record it.
        try:
            self._count("reorgs_seen")
            self.counters["last_reorg_ancestor"] = int(ancestor_height or 0)
        except Exception as e:
            self._fail("on_reorg", e)

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            _NB_SWALLOW_LOG.debug("swallowed (ValueError, AttributeError) in Layer37.detach", exc_info=True)
        with _LAYERS_LOCK:
            if self in _LAYERS:
                _LAYERS.remove(self)

    # ---- P2P hook (runs after the original _handle_message) -------------
    def on_p2p_message(self, peer: Any, msg: Any) -> None:
        try:
            self._count("p2p_messages")
            ep = _peer_endpoint(peer)
            if ep is None:
                self._count("p2p_peer_unparsed")
            else:
                payload = _get(msg, "payload")
                src = payload if isinstance(payload, dict) else msg
                height = _get(src, "height", 0)
                version = _get(src, "version")
                agent = _get(src, "user_agent", "") or ""
                self.peers.observe(
                    ep[0], ep[1],
                    height=height if isinstance(height, int) else 0,
                    version=version if isinstance(version, int) else None,
                    user_agent=agent if isinstance(agent, str) else "")
            mtype = (_get(msg, "type") or _get(msg, "command")
                     or _get(msg, "cmd"))
            fn = self._handlers.get(str(mtype)) if mtype is not None else None
            if fn is not None:
                fn(peer, msg)
        except Exception as e:
            self._fail("on_p2p_message", e)

    # ---- Mempool hook (runs after the original submit) -------------------
    def on_mempool_submit(self, tx: Any, result: Any) -> None:
        """Observation only: the host's (ok, reason) result is never changed.
        Accepted transactions feed the oracle's GAS_PRICE feed with the
        median recent fee rate (fee per byte)."""
        try:
            ok = bool(result[0]) if isinstance(result, tuple) and result else bool(result)
            if not ok:
                self._count("mempool_rejected")
                return
            self._count("mempool_accepted")
            fee = tx.fee(self.bc.utxo)
            size = tx.byte_size()
            if size and fee is not None and self.oracle is not None:
                with self._lock:
                    self._gas.append(float(fee) / float(size))
                    med = statistics.median(self._gas)
                self.oracle.update_price("GAS_PRICE", float(med))
        except Exception as e:
            self._fail("on_mempool_submit", e)

    # ---- read-only helpers ---------------------------------------------
    def cdps_at_risk(self) -> List[str]:
        """CDP ids whose ratio is under LIQUIDATION_RATIO (does not mutate)."""
        sc = self.stablecoin
        if sc is None:
            return []
        with sc._lock:
            return [cid for cid, c in sc._cdps.items()
                    if not c["liquidated"] and c["debt"] > 0
                    and sc.get_collateral_ratio(cid) < sc.LIQUIDATION_RATIO]

    def wallet_positions(self, address: str) -> dict:
        """What this address holds in group37 services (wallet-side view)."""
        out: dict = {"address": address, "cdps": [], "multisig_wallets": []}
        try:
            sc = self.stablecoin
            if sc is not None:
                with sc._lock:
                    for cid, c in sc._cdps.items():
                        if c["owner"] == address:
                            ratio = sc.get_collateral_ratio(cid)
                            out["cdps"].append({
                                "cdp_id": cid,
                                "collateral_nbl": c["collateral"] / 10 ** g.DECIMALS,
                                "debt_nbusd": c["debt"] / 10 ** g.DECIMALS,
                                "ratio": None if ratio == float("inf") else ratio,
                                "liquidated": c["liquidated"],
                            })
            ms = self.multisig
            if ms is not None:
                with ms._lock:
                    out["multisig_wallets"] = [
                        w.to_dict() for w in ms._wallets.values()
                        if address in w.signers]
        except Exception as e:
            self._fail("wallet_positions", e)
        return out

    def rest_handlers(self) -> Dict[str, Callable[..., Any]]:
        """Map of read-only API handlers. NOT auto-registered (the host's
        router is not touched); pass them to the host's route system."""
        ex, ag = self.explorer, self.aggregator
        handlers: Dict[str, Callable[..., Any]] = {}
        if ex is not None:
            handlers.update({
                "/api/g37/explorer/stats": ex.explorer_stats,
                "/api/g37/explorer/block": ex.get_block,
                "/api/g37/explorer/tx": ex.get_transaction,
                "/api/g37/explorer/address": ex.get_address,
                "/api/g37/explorer/latest": ex.latest_blocks,
                "/api/g37/explorer/mempool": ex.mempool_snapshot,
                "/api/g37/explorer/search": ex.search,
            })
        if ag is not None:
            handlers["/api/g37/swap/quote"] = ag.quote
        if self.oracle is not None:
            handlers["/api/g37/oracle/stats"] = self.oracle.oracle_stats
        if self.stablecoin is not None:
            handlers["/api/g37/stablecoin/stats"] = self.stablecoin.stablecoin_stats
        if self.governance is not None:
            handlers["/api/g37/governance/stats"] = self.governance.governance_v2_stats
        if self.lightning is not None:
            handlers["/api/g37/lightning/stats"] = self.lightning.network_stats
        return handlers

    # ---- reporting -------------------------------------------------------
    def status(self) -> dict:
        def safe(fn: Optional[Callable[[], Any]]) -> Any:
            try:
                return fn() if fn else None
            except Exception as e:
                return f"error: {e}"
        with self._lock:
            counters = dict(self.counters)
        return {
            "errors": self.errors,
            "last_error": self.last_error,
            "counters": counters,
            "auto_liquidations": self.auto_liquidations,
            "stablecoin_mechanism": self.stablecoin_mechanism.value,
            "discovered": {
                "dex": self.dex is not None,
                "tx_index": self.tx_index is not None,
                "analytics": self.analytics is not None,
            },
            "services": {
                "oracle": safe(self.oracle.oracle_stats if self.oracle else None),
                "stablecoin": safe(self.stablecoin.stablecoin_stats if self.stablecoin else None),
                "lightning": safe(self.lightning.network_stats if self.lightning else None),
                "governance": safe(self.governance.governance_v2_stats if self.governance else None),
                "multisig": safe(self.multisig.multisig_stats if self.multisig else None),
                "aggregator": safe(self.aggregator.aggregator_stats if self.aggregator else None),
                "explorer": safe(self.explorer.explorer_stats if self.explorer else None),
                "peers": self.peers.count(),
                "nft_book": self.nfts.stats(),
            },
        }

    def wiring_report(self) -> List[dict]:
        """One row per group37 class: how it is wired and how many live
        instances exist right now (0 is normal until the feature is used)."""
        def n(fn: Callable[[], int]) -> int:
            try:
                return int(fn())
            except Exception:
                return -1
        lt, gv, orc = self.lightning, self.governance, self.oracle
        ms, ag = self.multisig, self.aggregator
        rows = [
            ("DiscoveredPeer", "data", "PeerBook <- P2PNode._handle_message hook",
             n(self.peers.count)),
            ("LightningChannel", "data", "LightningNetworkV2._channels",
             n(lambda: len(lt._channels))),
            ("LightningNetworkV2", "service", "node.group37.lightning",
             1 if lt else 0),
            ("VotingMechanism", "enum", "GovernanceV2.PROPOSAL_TEMPLATES",
             n(lambda: sum(1 for t in gv.PROPOSAL_TEMPLATES.values()
                           if isinstance(t["mechanism"], g.VotingMechanism)))),
            ("Delegation", "data", "GovernanceV2._delegations",
             n(lambda: len(gv._delegations))),
            ("GovernanceV2", "service", "node.group37.governance",
             1 if gv else 0),
            ("OracleFeedType", "enum", "OracleFeed.feed_type",
             n(lambda: sum(1 for f in orc._feeds.values()
                           if isinstance(f.feed_type, g.OracleFeedType)))),
            ("OracleReport", "data", "OracleFeed.reports",
             n(lambda: sum(len(f.reports) for f in orc._feeds.values()))),
            ("OracleFeed", "data", "OracleV2._feeds",
             n(lambda: len(orc._feeds))),
            ("OracleV2", "service",
             "node.group37.oracle <- Mempool.submit hook (GAS_PRICE)",
             1 if orc else 0),
            ("StablecoinMechanism", "enum", "Layer37.stablecoin_mechanism (COLLATERAL)",
             1),
            ("StablecoinProtocol", "service",
             "node.group37.stablecoin (+ wallet_positions, chain listener scan)",
             1 if self.stablecoin else 0),
            ("MultisigPolicy", "enum", "MultisigWalletV2.policy",
             n(lambda: sum(1 for w in ms._wallets.values()
                           if isinstance(w.policy, g.MultisigPolicy)))),
            ("MultisigWalletV2", "data", "MultisigManagerV2._wallets",
             n(lambda: len(ms._wallets))),
            ("MultisigManagerV2", "service",
             "node.group37.multisig (+ wallet_positions)", 1 if ms else 0),
            ("SwapRoute", "data", "built per quote/swap by DeFiAggregatorV2",
             0),
            ("DeFiAggregatorV2", "service",
             "node.group37.aggregator (needs host NEBULADex)", 1 if ag else 0),
            ("BlockExplorerBackend", "service",
             "node.group37.explorer (+ rest_handlers)", 1 if self.explorer else 0),
            ("NFTAuctionType", "enum", "NFTListingBook / NFTListing.auction_type",
             n(lambda: sum(1 for l in self.nfts._listings.values()
                           if isinstance(l.auction_type, g.NFTAuctionType)))),
            ("NFTListing", "data", "NFTListingBook (record-only)",
             n(self.nfts.count)),
        ]
        return [{"class": c, "kind": k, "wired_to": w, "live_instances": i}
                for c, k, w, i in rows]


# --------------------------------------------------------------------------
# install / uninstall
# --------------------------------------------------------------------------
def _layers_snapshot() -> List[Layer37]:
    with _LAYERS_LOCK:
        return list(_LAYERS)


def _layer_for_mempool(mp: Any) -> Optional[Layer37]:
    for L in _layers_snapshot():
        if getattr(L.bc, "mempool", None) is mp:
            return L
    return None


def _layer_for_p2p(p2p: Any) -> Optional[Layer37]:
    layers = _layers_snapshot()
    for L in layers:
        if (getattr(L.node, "p2p", None) is p2p
                or getattr(L.node, "net", None) is p2p
                or getattr(p2p, "node", None) is L.node
                or getattr(p2p, "bc", None) is L.bc
                or getattr(p2p, "blockchain", None) is L.bc):
            return L
    return layers[0] if len(layers) == 1 else None


def _patch(owner: Any, name: str, new: Any) -> None:
    _PATCHES.append((owner, name, owner.__dict__.get(name, _MISSING)))
    setattr(owner, name, new)


def install(host: Any) -> bool:
    """Patch the host additively. Returns False if already installed."""
    cls = getattr(host, "NEBULAFullNode", None)
    if cls is None:
        raise AttributeError("host has no NEBULAFullNode")
    if getattr(cls, "_g37_orig", None):
        return False
    _ensure_compat_names()

    orig_init = cls.__init__

    def patched_init(self, *a, **k):
        orig_init(self, *a, **k)               # host always first
        try:
            layer = Layer37(self, host)
            self.group37 = layer
            self.bc.add_listener(layer)
            with _LAYERS_LOCK:
                _LAYERS.append(layer)
        except Exception as e:                  # node must still start
            self.group37_error = e
            log.warning("group37 install failed on node: %s", e)

    cls._g37_orig = orig_init
    cls.__init__ = patched_init

    # --- Mempool.submit(tx) -> (ok, reason): original first -----------------
    mp_cls = getattr(host, "Mempool", None)
    if mp_cls is not None and hasattr(mp_cls, "submit"):
        orig_submit = mp_cls.submit

        def patched_submit(self, *a, **k):
            result = orig_submit(self, *a, **k)
            L = _layer_for_mempool(self)
            if L is not None and a:
                L.on_mempool_submit(a[0], result)
            return result
        _patch(mp_cls, "submit", patched_submit)

    # --- P2PNode._handle_message(peer, msg): original first -----------------
    p2p_cls = getattr(host, "P2PNode", None)
    if p2p_cls is not None and hasattr(p2p_cls, "_handle_message"):
        orig_handle = p2p_cls._handle_message

        def patched_handle(self, *a, **k):
            result = orig_handle(self, *a, **k)
            L = _layer_for_p2p(self)
            if L is not None and len(a) >= 2:
                L.on_p2p_message(a[0], a[1])
            return result
        _patch(p2p_cls, "_handle_message", patched_handle)

    # --- NEBULAWallet: read-only helper, added only if the name is free -----
    w_cls = getattr(host, "NEBULAWallet", None)
    if w_cls is not None and not hasattr(w_cls, "g37_positions"):
        def g37_positions(self, address: Optional[str] = None) -> dict:
            addr = address or getattr(self, "address", None)
            layers = _layers_snapshot()
            if not addr or not layers:
                return {"address": addr, "cdps": [], "multisig_wallets": []}
            return layers[-1].wallet_positions(addr)
        _patch(w_cls, "g37_positions", g37_positions)

    return True


def uninstall(host: Any) -> None:
    """Restore every patched method and detach all layers."""
    for L in _layers_snapshot():
        L.detach()
    while _PATCHES:
        owner, name, original = _PATCHES.pop()
        if original is _MISSING:
            try:
                delattr(owner, name)
            except AttributeError:
                _NB_SWALLOW_LOG.debug("swallowed AttributeError in uninstall", exc_info=True)
        else:
            setattr(owner, name, original)
    cls = getattr(host, "NEBULAFullNode", None)
    orig = getattr(cls, "_g37_orig", None) if cls else None
    if orig:
        cls.__init__ = orig
        del cls._g37_orig
