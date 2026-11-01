"""nebula_group40_install.py - wiring layer for NEBULA group40 (20 formerly dead classes).

Design rules (same pattern as group5):
  * nebula_v10_11.py and nebula_group40.py are NOT edited. Everything lives here.
  * install(host) wraps NEBULAFullNode.__init__; the original __init__ always runs first.
  * A failure inside this layer never stops the node from starting and never rejects a
    block or a transaction: every callback is wrapped, errors are counted in layer.errors.
  * uninstall(host) restores the original __init__ completely.
  * Nothing here fabricates data. Where a class would otherwise run on made-up inputs
    (no price oracle, no NFT registry, no proof verifier) the layer refuses and says why.

Public entry points:
  install(host)            -> patch NEBULAFullNode.__init__
  uninstall(host)          -> undo it
  Layer40(node, host=None) -> the layer object, stored as node.group40
"""
from __future__ import annotations

import hashlib
import sys
import threading
import time
from collections import deque
from typing import Any, Callable, Dict, List, Optional, Tuple
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

HOST_MODULE = "nebula_v10_11"
GROUP_MODULE = "nebula_group40"
_ORIG_ATTR = "_g40_orig"
_ROUTES_ATTR = "_g40_routes_installed"

# Names the group needs from the host at RUN time (not just in annotations).
RUNTIME_DEPENDENCIES: Tuple[str, ...] = (
    "BlockTemplateEngine",   # NodeRESTAPI._block_template
    "BridgeDirection",       # UniversalTokenBridge / BridgeRequestV2
    "ContractEvent",         # base of ContractEventC (EventLog.emit)
    "ContractEventC",        # EventLog.emit (built here if the host lacks it)
    "ContractTemplate",      # ContractFactory.deploy (template.value)
    "DeployedContract",      # ContractFactory.deploy
    "LockStakingPool",       # AdvancedStakingPlatform.__init__
    "NEBULABlockchain",      # NodeManager / DeFiDashboard defaults
    "Transaction",           # NodeRESTAPI submit / decode
)

# Every name copied from the host into the group module on install, so that the
# classes the group uses are the SAME objects as in the running host.
_BIND_NAMES: Tuple[str, ...] = RUNTIME_DEPENDENCIES + ("StakingPool", "BridgeRequest")

DEFAULT_OPTIONS: Dict[str, Any] = {
    "auto_staking_rewards": True,    # call AdvancedStakingPlatform.process_rewards() per block
    "auto_liquidations": True,       # call MarginTradingEngine.check_liquidations() per block
    "event_log_soft_cap": 100_000,   # EventLog is RAM only; stats flag when exceeded
    "nft_proof_verifier": None,      # callable(collection_id, token_id, owner, source_chain, proof)->bool
}


class Group40Error(RuntimeError):
    """Raised when the layer cannot be built at all (missing hard dependency)."""


# --------------------------------------------------------------------------- loading

def _import_group(host=None):
    """Import nebula_group40 so that it shares the running host module.

    When the host is run as a script its module name is __main__; importing
    nebula_group40 would then import a SECOND copy of the host (slow, and with different
    class objects). Aliasing the running host under its real name avoids that.
    """
    if host is not None and HOST_MODULE not in sys.modules:
        if getattr(host, "__name__", "") in ("__main__", HOST_MODULE):
            sys.modules[HOST_MODULE] = host
    import importlib
    return importlib.import_module(GROUP_MODULE)


def bind_host(group, host) -> List[str]:
    """Copy dependency classes from the running host into the group module.

    Returns the list of RUNTIME_DEPENDENCIES that are still missing afterwards.
    """
    if host is not None:
        for name in _BIND_NAMES:
            if hasattr(host, name):
                setattr(group, name, getattr(host, name))
    # ContractEventC is a host-side compat subclass that the group file uses but does
    # not declare. Build it from ContractEvent with the group's own helper if needed.
    if not hasattr(group, "ContractEventC") and hasattr(group, "ContractEvent"):
        try:
            group.ContractEventC = group._make_compat(group.ContractEvent,
                                                      name="ContractEventC")
        except Exception:
            _NB_SWALLOW_LOG.debug("swallowed Exception in bind_host", exc_info=True)
    return [n for n in RUNTIME_DEPENDENCIES if not hasattr(group, n)]


# --------------------------------------------------------------------------- safe ERC20

_SAFE_ERC20_CACHE: Dict[int, type] = {}

_AMOUNT_FUNCS = ("transfer", "approve", "transferFrom", "mint", "burn")
_REQUIRED_ARGS = {
    "transfer": ("to",),
    "transferFrom": ("owner", "to"),
    "approve": ("spender",),
}


def safe_erc20_class(group) -> type:
    """ERC20Contract with input validation and all-or-nothing calls.

    Fixes found while reading group40 (the original class is left untouched):
      * negative or non-integer amounts were accepted (a negative `transfer` moves
        funds the wrong way, a negative `burn` mints);
      * a missing `to` / `spender` silently credited the empty address;
      * transferFrom lowered the allowance before checking the balance, so a failed
        call left the allowance changed. Any exception now rolls the state back.
    """
    key = id(group)
    cached = _SAFE_ERC20_CACHE.get(key)
    if cached is not None:
        return cached

    base = group.ERC20Contract

    class SafeERC20Contract(base):  # type: ignore[misc, valid-type]
        def __init__(self, *a, **k):
            super().__init__(*a, **k)
            self._call_lock = threading.RLock()

        def call(self, caller, fn_name, args=None, value=0):
            if not isinstance(caller, str) or not caller:
                raise ValueError("caller must be a non-empty string")
            args = dict(args or {})
            if fn_name in _AMOUNT_FUNCS:
                amt = args.get("amount", 0)
                if isinstance(amt, bool) or not isinstance(amt, int) or amt < 0:
                    raise ValueError("amount must be a non-negative integer (base units)")
            for k in _REQUIRED_ARGS.get(fn_name, ()):
                v = args.get(k)
                if not isinstance(v, str) or not v:
                    raise ValueError(f"'{k}' is required and must be a non-empty string")
            for k in ("to", "spender", "owner", "account"):
                if k in args and (not isinstance(args[k], str) or not args[k]):
                    raise ValueError(f"'{k}' must be a non-empty string")
            with self._call_lock:
                storage_before = dict(self.state._storage)
                events_before = len(self.state._events)
                try:
                    return super().call(caller, fn_name, args, value)
                except Exception:
                    self.state._storage = storage_before
                    del self.state._events[events_before:]
                    raise

    _SAFE_ERC20_CACHE[key] = SafeERC20Contract
    return SafeERC20Contract


# --------------------------------------------------------------------------- bound manager

def bound_manager_class(group) -> type:
    """NodeManager that adopts the running node's blockchain.

    The original NodeManager.__init__ builds a brand-new NEBULABlockchain(), i.e. a
    second, unrelated chain next to the real one. This subclass takes the real one.
    """
    class BoundNodeManager(group.NodeManager):
        def __init__(self, blockchain, config=None):
            self.config = config or group.NodeConfig.from_env()
            self.blockchain = blockchain
            self.running = False
            self._threads = []
            self._start_time = 0.0

    return BoundNodeManager


# --------------------------------------------------------------------------- helpers

def _find_attr(obj, names: Tuple[str, ...], needs: Tuple[str, ...] = ()):
    """First attribute of `obj` among `names` that has every method in `needs`."""
    for n in names:
        cand = getattr(obj, n, None)
        if cand is not None and all(callable(getattr(cand, m, None)) for m in needs):
            return cand
    return None


def _ok(data) -> Tuple[int, dict]:
    return 200, {"success": True, "data": data}


def _fail(code: int, msg: str) -> Tuple[int, dict]:
    return code, {"success": False, "error": msg}


# --------------------------------------------------------------------------- the layer

class Layer40:
    """Owns every group40 service and reacts to chain events (listener protocol)."""

    def __init__(self, node, host=None, group=None, options: Optional[dict] = None):
        self.node = node
        self.host = host
        self.g = group or _import_group(host)
        self.options = {**DEFAULT_OPTIONS, **(options or {})}
        self.errors = 0
        self.error_log: deque = deque(maxlen=50)
        self.failed: Dict[str, str] = {}
        self.stats_: Dict[str, Any] = {
            "blocks_seen": 0, "reorgs_seen": 0, "last_height": None,
            "reward_runs": 0, "liquidations": 0, "contract_calls": 0,
            "events_forwarded": 0,
        }
        self._lock = threading.RLock()
        self.contracts: Dict[str, Any] = {}

        missing = bind_host(self.g, host)
        if missing:
            raise Group40Error("missing host classes: " + ", ".join(missing))

        self.bc = _find_attr(node, ("bc", "blockchain"), ("add_listener",))
        if self.bc is None:
            raise Group40Error("node has no blockchain with add_listener (expected node.bc)")

        self.oracle = (_find_attr(node, ("oracle", "price_oracle", "oracle_v2"), ("price",))
                       or _find_attr(self.bc, ("oracle", "price_oracle"), ("price",)))
        self.nft_registry = _find_attr(node, ("nft", "nbl721", "nft_registry"), ("owner_of",))
        self.token_registry = _find_attr(node, ("nbl20", "nbl20_registry", "tokens"), ())

        self._build()

    # ---- construction -------------------------------------------------------

    def _make(self, attr: str, factory: Callable[[], Any]):
        try:
            obj = factory()
        except Exception as e:  # a broken service must not stop the node
            obj = None
            self.failed[attr] = f"{type(e).__name__}: {e}"
        setattr(self, attr, obj)
        return obj

    def _build(self) -> None:
        g, bc = self.g, self.bc
        self._make("events", lambda: g.EventLog(bc))
        self._make("factory", lambda: g.ContractFactory(bc))
        self._make("nft_bridge", lambda: g.CrossChainNFTBridge(bc, self.nft_registry))
        self._make("staking", lambda: g.AdvancedStakingPlatform(bc))
        self._make("portfolio", lambda: g.PortfolioTracker(bc, self.oracle))
        self._make("rest", lambda: g.NodeRESTAPI(bc))
        self._make("token_bridge", lambda: g.UniversalTokenBridge(bc, self.token_registry))
        self._make("margin", lambda: g.MarginTradingEngine(bc, self.oracle))
        self._make("config", lambda: g.NodeConfig.from_env())
        self._make("manager", lambda: bound_manager_class(g)(bc, self.config))
        # DeFiDashboard calls node.staking / nft / dex / governance / bridge / social.
        # Hand it the node only if every one of those exists, else chain-only mode.
        full = self.node if self._node_has_defi_parts() else None
        self._make("dashboard", lambda: g.DeFiDashboard(full_node=full, blockchain=bc))
        self.dashboard_mode = "full_node" if full is not None else "chain_only"

    def _node_has_defi_parts(self) -> bool:
        need = {"staking": ("get_stake", "staking_stats"), "nft": ("tokens_of", "nft_stats"),
                "dex": ("dex_stats",), "governance": ("votes_by", "governance_stats"),
                "bridge": ("bridge_stats",), "social": ("social_stats",)}
        return all(_find_attr(self.node, (n,), m) is not None for n, m in need.items())

    # ---- listener protocol (bc.add_listener(layer)) --------------------------

    def _record_error(self, where: str, exc: Exception) -> None:
        with self._lock:
            self.errors += 1
            self.error_log.append(f"{time.strftime('%H:%M:%S')} {where}: {type(exc).__name__}: {exc}")

    def on_connect(self, block) -> None:
        with self._lock:
            self.stats_["blocks_seen"] += 1
            self.stats_["last_height"] = getattr(block, "height", None)
        if self.options["auto_staking_rewards"] and self.staking is not None:
            try:
                self.staking.process_rewards()
                with self._lock:
                    self.stats_["reward_runs"] += 1
            except Exception as e:
                self._record_error("process_rewards", e)
        if self.options["auto_liquidations"] and self.margin is not None and self.oracle is not None:
            try:
                n = len(self.margin.check_liquidations())
                with self._lock:
                    self.stats_["liquidations"] += n
            except Exception as e:
                self._record_error("check_liquidations", e)

    def on_reorg(self, old, new, ancestor_height) -> None:
        try:
            with self._lock:
                self.stats_["reorgs_seen"] += 1
            # Reward accrual is height based. After a reorg to a shorter chain the
            # "last rewarded height" would otherwise sit above the tip and stall rewards.
            if self.staking is not None:
                tip = self.bc.height
                if self.staking._last_reward_block > tip:
                    self.staking._last_reward_block = tip
        except Exception as e:
            self._record_error("on_reorg", e)

    def detach(self) -> None:
        try:
            self.bc._listeners.remove(self)
        except (ValueError, AttributeError):
            remover = getattr(self.bc, "remove_listener", None)
            if callable(remover):
                try:
                    remover(self)
                except Exception:
                    _NB_SWALLOW_LOG.debug("swallowed Exception in Layer40.detach", exc_info=True)

    # ---- balances ----------------------------------------------------------------

    def reserved_balance(self, address: str) -> int:
        """Raw units already committed by this layer's services for `address`.

        The group classes only CHECK the UTXO balance, they never lock it, so the same
        coins could back a stake, a margin position and a bridge request at once. This
        soft ledger counts what the layer has already accepted. It does not move UTXOs.
        """
        dec = 10 ** self.g.DECIMALS
        total = 0
        if self.staking is not None:
            for pool in self.staking._pools.values():
                info = pool.stakers.get(address)
                if info:
                    total += int(info["amount"])
        if self.margin is not None:
            for p in self.margin._positions.values():
                if p.open and p.trader == address:
                    total += int(p.collateral * dec)
        if self.token_bridge is not None:
            for r in self.token_bridge._requests.values():
                if r.sender == address and r.asset == "NBL" and r.status in ("pending", "approved"):
                    total += int(r.amount)
        return total

    def available_balance(self, address: str) -> int:
        return max(0, int(self.bc.utxo.balance(address)) - self.reserved_balance(address))

    # ---- services with guards ----------------------------------------------------

    def stake(self, address: str, pool_id: str, amount_nbl: float) -> Tuple[bool, str]:
        if self.staking is None:
            return False, "staking platform unavailable"
        if not isinstance(amount_nbl, (int, float)) or isinstance(amount_nbl, bool) or amount_nbl <= 0:
            return False, "amount must be a positive number"
        need = int(amount_nbl * 10 ** self.g.DECIMALS)
        if self.available_balance(address) < need:
            return False, "Insufficient available balance (some coins are already committed)"
        return self.staking.stake(address, pool_id, amount_nbl)

    def margin_open(self, trader: str, pair: str, side: str,
                    size_nbl: float, leverage: float) -> Tuple[bool, str]:
        if self.margin is None:
            return False, "margin engine unavailable"
        if self.oracle is None:
            return False, "No price oracle connected: refusing to open a position at a made-up price"
        if not isinstance(size_nbl, (int, float)) or isinstance(size_nbl, bool) or size_nbl <= 0:
            return False, "size must be a positive number"
        if not isinstance(leverage, (int, float)) or isinstance(leverage, bool) or leverage < 1:
            return False, "leverage must be >= 1"
        if self.oracle.price(pair) in (None, 0):
            return False, f"Oracle has no price for {pair}"
        need = int((size_nbl / leverage) * 10 ** self.g.DECIMALS)
        if self.available_balance(trader) < need:
            return False, "Insufficient available collateral (some coins are already committed)"
        return self.margin.open_position(trader, pair, side, size_nbl, leverage)

    def portfolio_value(self, owner: str) -> dict:
        out = self.portfolio.portfolio_value(owner)
        out["price_source"] = "oracle" if self.oracle is not None else "none (no oracle: NBL=0.01, others=1.0 are placeholders)"
        return out

    def nft_bridge_out(self, collection_id, token_id, owner, dest_chain, dest_address):
        if self.nft_bridge is None:
            return False, "NFT bridge unavailable"
        if self.nft_registry is None:
            return False, "No NFT registry connected: ownership cannot be verified"
        return self.nft_bridge.bridge_out(collection_id, token_id, owner, dest_chain, dest_address)

    def nft_bridge_in(self, collection_id, token_id, owner, source_chain, proof=""):
        if self.nft_bridge is None:
            return False, "NFT bridge unavailable"
        verifier = self.options.get("nft_proof_verifier")
        if not callable(verifier):
            return False, "No proof verifier configured: refusing to mint without proof"
        try:
            valid = bool(verifier(collection_id, token_id, owner, source_chain, proof))
        except Exception as e:
            self._record_error("nft_proof_verifier", e)
            return False, "proof verification failed"
        if not valid:
            return False, "invalid proof"
        return self.nft_bridge.bridge_in(collection_id, token_id, owner, source_chain, proof)

    def token_bridge_submit(self, sender, asset, amount_raw, receiver, dst_chain):
        if self.token_bridge is None:
            return False, "token bridge unavailable"
        if isinstance(amount_raw, bool) or not isinstance(amount_raw, int) or amount_raw <= 0:
            return False, "amount_raw must be a positive integer"
        if asset == "NBL" and self.available_balance(sender) < amount_raw:
            return False, "Insufficient available balance"
        return self.token_bridge.submit_bridge_request(sender, asset, amount_raw, receiver, dst_chain)

    # ---- contracts -> events ---------------------------------------------------------

    def deploy_erc20(self, deployer: str, name: str, symbol: str,
                     decimals: int, total_supply: float) -> Tuple[bool, str]:
        if not (isinstance(deployer, str) and deployer):
            return False, "deployer required"
        if isinstance(decimals, bool) or not isinstance(decimals, int) or not 0 <= decimals <= 36:
            return False, "decimals must be an integer 0..36"
        if not isinstance(total_supply, (int, float)) or isinstance(total_supply, bool) or total_supply < 0:
            return False, "total_supply must be >= 0"
        if not (isinstance(name, str) and name and isinstance(symbol, str) and symbol):
            return False, "name and symbol required"
        cid = hashlib.sha256(
            f"ERC20:{deployer}:{symbol}:{self.bc.height}:{time.time()}".encode()).hexdigest()[:20]
        cls = safe_erc20_class(self.g)
        try:
            contract = cls(cid, deployer, self.bc, name, symbol, decimals, total_supply)
        except Exception as e:
            return False, f"deploy failed: {e}"
        with self._lock:
            self.contracts[cid] = contract
        self._forward_events(cid, [{"event": "Deployed", "data": {
            "owner": deployer, "name": name, "symbol": symbol}}])
        return True, cid

    def call_contract(self, contract_id: str, caller: str, fn_name: str,
                      args: Optional[dict] = None, value: int = 0) -> dict:
        contract = self.contracts.get(contract_id)
        if contract is None:
            return {"ok": False, "error": "contract not found"}
        try:
            result, events = contract.call(caller, fn_name, args, value)
        except Exception as e:
            return {"ok": False, "error": str(e)}
        with self._lock:
            self.stats_["contract_calls"] += 1
        self._forward_events(contract_id, events)
        return {"ok": True, "result": result, "events": events}

    def _forward_events(self, contract_id: str, events: List[dict]) -> None:
        """Copy contract events into the chain-wide EventLog (searchable by topic)."""
        if self.events is None:
            return
        for ev in events:
            data = dict(ev.get("data", {}))
            topics = [str(ev["event"])] + [str(data[k]) for k in ("from", "to", "owner", "spender")
                                           if k in data]
            try:
                self.events.emit(contract_id, ev["event"], topics, data)
                with self._lock:
                    self.stats_["events_forwarded"] += 1
            except Exception as e:
                self._record_error("event_log.emit", e)

    def deploy_template(self, deployer: str, template_name: str, params: dict) -> Tuple[bool, str]:
        """ContractFactory.deploy with the template given by enum name or value."""
        if self.factory is None:
            return False, "factory unavailable"
        tpl_cls = self.g.ContractTemplate
        template = None
        for member in tpl_cls:
            if template_name in (member.name, member.value):
                template = member
                break
        if template is None:
            return False, "unknown template: " + str(template_name)
        return self.factory.deploy(deployer, template, params)

    # ---- real yield data (replaces the dashboard's hard-coded table) -------------------

    def yield_opportunities(self) -> List[dict]:
        """Yields computed from the live staking pools. Nothing is invented."""
        if self.staking is None:
            return []
        dec = 10 ** self.g.DECIMALS
        out = []
        for pool in self.staking._pools.values():
            out.append({
                "protocol": f"NEBULA Staking ({pool.name})",
                "apy_pct": round(pool.apy * 100, 4),
                "lock_days": getattr(pool, "lock_days", None),
                "tvl_nbl": pool.total_staked / dec,
                "stakers": len(pool.stakers),
            })
        return out

    # ---- status -----------------------------------------------------------------------

    def status(self) -> dict:
        soft_cap = self.options["event_log_soft_cap"]
        n_events = len(self.events._logs) if self.events is not None else 0
        with self._lock:
            return {
                "group": 40,
                "errors": self.errors,
                "recent_errors": list(self.error_log)[-5:],
                "failed_components": dict(self.failed),
                "oracle_connected": self.oracle is not None,
                "nft_registry_connected": self.nft_registry is not None,
                "dashboard_mode": self.dashboard_mode,
                "contracts": len(self.contracts),
                "event_log_size": n_events,
                "event_log_over_soft_cap": n_events > soft_cap,
                **self.stats_,
            }


# --------------------------------------------------------------------------- REST (read only)

_ACTIVE: List[Layer40] = []   # most recently installed layer serves the routes


def _layer() -> Optional[Layer40]:
    return _ACTIVE[-1] if _ACTIVE else None


def _guard(fn):
    def handler(path, query, body):
        lay = _layer()
        if lay is None:
            return _fail(503, "group40 layer not installed")
        try:
            return _ok(fn(lay, query or {}))
        except Exception as e:
            lay._record_error("route " + str(path), e)
            return _fail(500, str(e))
    return handler


def _q(query: dict, key: str, default=None):
    v = query.get(key, default)
    if isinstance(v, list):
        v = v[0] if v else default
    return v


def _r_status(lay, q):      return lay.status()
def _r_staking(lay, q):     return lay.staking.staking_platform_stats()
def _r_yields(lay, q):      return lay.yield_opportunities()
def _r_margin(lay, q):      return lay.margin.margin_stats()
def _r_portfolio(lay, q):   return lay.portfolio.global_stats()
def _r_token_bridge(lay, q): return lay.token_bridge.bridge_stats()
def _r_nft_bridge(lay, q):  return lay.nft_bridge.bridge_stats()
def _r_factory(lay, q):     return lay.factory.factory_stats()
def _r_events(lay, q):      return lay.events.event_log_stats()
def _r_node(lay, q):        return lay.manager.node_info()
def _r_rest_stats(lay, q):  return lay.rest.api_stats()
def _r_risk(lay, q):        return lay.dashboard.risk_metrics()


def _r_snapshot(lay, q):
    return lay.dashboard.ecosystem_snapshot()


def _r_contracts(lay, q):
    return [c.contract_info() for c in lay.contracts.values()]


def _r_logs(lay, q):
    limit = min(int(_q(q, "limit", 100)), 1000)
    return lay.events.get_logs(contract_id=_q(q, "contract"), event_name=_q(q, "event"),
                               topic=_q(q, "topic"), limit=limit)


def _r_address(lay, q):
    addr = _q(q, "address")
    if not addr:
        raise ValueError("address query parameter required")
    return {
        "address": addr,
        "balance_raw": lay.bc.utxo.balance(addr),
        "reserved_raw": lay.reserved_balance(addr),
        "available_raw": lay.available_balance(addr),
        "staking_positions": lay.staking.user_positions(addr),
        "margin_positions": lay.margin.trader_positions(addr),
        "portfolio": lay.portfolio_value(addr),
    }


def _r_node_proxy(lay, q):
    """GET-only pass-through to NodeRESTAPI.handle (POST /tx is deliberately unreachable)."""
    path = _q(q, "path", "/status")
    res = lay.rest.handle("GET", path, {})
    if not res.get("ok"):
        raise ValueError(res.get("error", "request failed"))
    return res["result"]


ENDPOINTS: Dict[str, Callable] = {
    "/api/g40/status": _r_status,
    "/api/g40/staking": _r_staking,
    "/api/g40/yields": _r_yields,
    "/api/g40/margin": _r_margin,
    "/api/g40/portfolio": _r_portfolio,
    "/api/g40/bridge/tokens": _r_token_bridge,
    "/api/g40/bridge/nft": _r_nft_bridge,
    "/api/g40/factory": _r_factory,
    "/api/g40/contracts": _r_contracts,
    "/api/g40/events": _r_events,
    "/api/g40/logs": _r_logs,
    "/api/g40/node": _r_node,
    "/api/g40/rest-stats": _r_rest_stats,
    "/api/g40/risk": _r_risk,
    "/api/g40/snapshot": _r_snapshot,
    "/api/g40/address": _r_address,
    "/api/g40/rest": _r_node_proxy,
}


def _register_routes(host) -> int:
    """Register the read-only endpoints in the host's route table (GET only)."""
    if getattr(host, _ROUTES_ATTR, False):
        return 0
    deco = getattr(host, "route", None)
    if not callable(deco):
        return 0
    for path, fn in ENDPOINTS.items():
        deco(path)(_guard(fn))
    setattr(host, _ROUTES_ATTR, True)
    return len(ENDPOINTS)


def _unregister_routes(host) -> None:
    table = getattr(host, "_routes", None)
    if isinstance(table, dict):
        for path in ENDPOINTS:
            table.get("GET", {}).pop(path, None)
    if hasattr(host, _ROUTES_ATTR):
        delattr(host, _ROUTES_ATTR)


# --------------------------------------------------------------------------- install / uninstall

def install(host, options: Optional[dict] = None) -> None:
    """Attach Layer40 to every NEBULAFullNode created from now on."""
    cls = host.NEBULAFullNode
    if getattr(cls, _ORIG_ATTR, None):
        return
    group = _import_group(host)
    missing = bind_host(group, host)
    if missing:
        raise Group40Error("cannot install, missing host classes: " + ", ".join(missing))
    orig = cls.__init__

    def patched(self, *a, **k):
        orig(self, *a, **k)            # the original node always starts first
        try:
            layer = Layer40(self, host=host, group=group, options=options)
            layer.bc.add_listener(layer)
            self.group40 = layer           # attached only after the listener is registered
            _ACTIVE.append(layer)
        except Exception as e:         # never stop the node
            self.group40_error = e

    cls._g40_orig = orig
    cls.__init__ = patched
    _register_routes(host)


def uninstall(host) -> None:
    cls = host.NEBULAFullNode
    orig = getattr(cls, _ORIG_ATTR, None)
    for lay in list(_ACTIVE):
        lay.detach()
    _ACTIVE.clear()
    if orig:
        cls.__init__ = orig
        delattr(cls, _ORIG_ATTR)
    _unregister_routes(host)
