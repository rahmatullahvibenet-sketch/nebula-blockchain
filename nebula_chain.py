"""NEBULA unified chain - ONE installer for every group (06 .. 63) plus the hardening pack.

This module replaces the three separate masters
(nebula_all_chain, nebula_all_groups_install, nebula_master_install).
It does NOT edit nebula_v10_11.py and it does NOT edit any nebula_groupNN file.

    import nebula_v10_11 as host
    import nebula_chain as chain

    print(chain.preflight(host))          # [] means every required piece is present
    report = chain.install_all(host)      # 06 -> 63 ascending, then hardening
    print(chain.summary(report))

    node = host.NEBULAFullNode(...)       # node.group06 ... node.group63 now exist
    chain.attach_hubs(node)               # group10 stack + group14 chain (need node.bc)
    print(chain.status(node))             # which layers are really attached, errors

    chain.uninstall_all(host)             # strict reverse order (hardening first)

Rules:
  * Install order is ascending, uninstall order is the exact reverse (LIFO). Several
    groups wrap NEBULAFullNode.__init__ / P2PNode._handle_message; a wrong unwind order
    would silently drop a later group's patch.
  * Every group is installed inside its own try/except. One failing group never stops
    the others and never stops the node from starting.
  * A group whose module file is not present is reported as "absent", never as an error.
  * Nothing here changes consensus rules or rejects blocks / transactions.
  * Nothing is verified against the real host unless YOU run it there.
"""
from __future__ import annotations

import importlib
import inspect
import logging
import threading
import time
import traceback
from typing import Any, Dict, List, Optional, Tuple
import logging as _nb_logging
_NB_SWALLOW_LOG = _nb_logging.getLogger("nebula.swallowed")

log = logging.getLogger("nebula.chain")

# --------------------------------------------------------------------------- #
# Group table: (group number, module exposing install()/uninstall())
# --------------------------------------------------------------------------- #
_LOW: List[int] = [6, 7, 8, 9, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26]

GROUPS: List[Tuple[int, str]] = (
    [(n, "nebula_group%02d_install" % n) for n in _LOW]
    + [
        (27, "nebula_group27_install"),
        (28, "nebula_group28_install"),
        (29, "nebula_group29_install"),
        (30, "nebula_group30_connected"),
        (31, "nebula_group31_wired"),
        (32, "nebula_group32_install"),
        (33, "nebula_group33_install"),
        (34, "nebula_group34_install"),
        (35, "nebula_group35_install"),
        (36, "nebula_group36_install"),
        (37, "nebula_group37_install"),
        (38, "nebula_group38_chain"),
        (39, "nebula_group39_install"),
        (40, "nebula_group40_install"),
        (41, "nebula_group41_install"),
        (42, "nebula_group42_install"),
        (43, "nebula_group43_install"),
        (44, "nebula_group44_install"),
        (45, "nebula_group45_install"),
    ]
    + [(n, "nebula_group%d_install" % n) for n in range(46, 64)]
)

# Groups that have no installer of their own.
NO_INSTALLER: Dict[int, str] = {
    10: "hub (Group10Stack) - use attach_hubs()",
    11: "classes only - no installer supplied",
    14: "hub (Group14Chain) - use attach_hubs()",
    24: "not supplied",
}

# Group 62 needs group 61's Bip9State, so 61 must be installed before 62.
REQUIRES: Dict[int, List[int]] = {62: [61]}

_LOCK = threading.RLock()
_INSTALLED: List[int] = []          # successful installs, in order
_MODULES: Dict[int, Any] = {}       # imported installer modules by group number
_HUBS: Dict[str, Any] = {}          # attached hubs (group10 / group14)
_HARDENING_APPLIED = False


def _short_tb() -> str:
    return traceback.format_exc(limit=3).strip().splitlines()[-1]


def _module_missing(exc: BaseException, modname: str) -> bool:
    """True when the installer file itself is not present (not a bug inside it)."""
    return isinstance(exc, ModuleNotFoundError) and getattr(exc, "name", None) == modname


def _call(fn: Any, host: Any, options: Optional[dict]) -> Any:
    """Call fn(host, **options) passing only the keywords fn really accepts."""
    options = dict(options or {})
    if options:
        try:
            params = inspect.signature(fn).parameters
            if not any(p.kind is inspect.Parameter.VAR_KEYWORD for p in params.values()):
                options = {k: v for k, v in options.items() if k in params}
        except (TypeError, ValueError):
            options = {}
    return fn(host, **options)


# --------------------------------------------------------------------------- #
# Shared names between groups (e.g. g19 needs g18.ProposalState)
# --------------------------------------------------------------------------- #
def bind_shared(host: Any) -> Dict[str, str]:
    """Expose classes defined by groups 06..26 on the host namespace so a group that
    needs a name from another group finds it. Never overwrites a name host already has."""
    added: Dict[str, str] = {}
    for n in _LOW:
        try:
            mod = importlib.import_module("nebula_group%02d" % n)
        except Exception:
            continue
        for k, v in vars(mod).items():
            if k.startswith("_") or not isinstance(v, type) or v.__module__ != mod.__name__:
                continue
            if not hasattr(host, k):
                setattr(host, k, v)
                added[k] = "group%02d" % n
    return added


# --------------------------------------------------------------------------- #
# Preflight
# --------------------------------------------------------------------------- #
def preflight(host: Any) -> List[str]:
    """Return a list of problems that would prevent wiring. [] means OK.
    Absent optional groups (files not supplied) are NOT problems; see absent_groups()."""
    problems: List[str] = []
    cls = getattr(host, "NEBULAFullNode", None)
    if cls is None:
        problems.append("host has no NEBULAFullNode class")
    elif not callable(getattr(cls, "__init__", None)):
        problems.append("NEBULAFullNode has no callable __init__")
    for n, modname in GROUPS:
        try:
            mod = importlib.import_module(modname)
        except Exception as e:
            if _module_missing(e, modname):
                continue
            problems.append("group%d: cannot import %s (%s: %s)" % (n, modname, type(e).__name__, e))
            continue
        if not callable(getattr(mod, "install", None)):
            problems.append("group%d: %s has no install()" % (n, modname))
        if not callable(getattr(mod, "uninstall", None)):
            problems.append("group%d: %s has no uninstall()" % (n, modname))
    return problems


def absent_groups() -> List[int]:
    """Groups whose installer file is not in the folder."""
    out: List[int] = []
    for n, modname in GROUPS:
        try:
            importlib.import_module(modname)
        except Exception as e:
            if _module_missing(e, modname):
                out.append(n)
    return out


# --------------------------------------------------------------------------- #
# Install / uninstall
# --------------------------------------------------------------------------- #
def install_all(host: Any,
                only: Optional[List[int]] = None,
                skip: Optional[List[int]] = None,
                options: Optional[Dict[int, dict]] = None,
                harden: bool = True) -> Dict[Any, Dict[str, Any]]:
    """Install every group ascending. Never raises. Returns one record per group:
    {"state": "ok" | "already" | "failed" | "absent" | "skipped", "error": ..., ...}.

    only    - install just these group numbers
    skip    - leave these group numbers out
    options - per-group keyword arguments, e.g. {44: {"risk_every": 12}}
    harden  - apply nebula_hardening after the groups (default True)
    """
    global _HARDENING_APPLIED
    options = options or {}
    report: Dict[Any, Dict[str, Any]] = {}
    with _LOCK:
        try:
            bound = bind_shared(host)
        except Exception:
            bound = {}
        for n, modname in GROUPS:
            if only is not None and n not in only:
                continue
            rec: Dict[str, Any] = {"state": "failed", "module": modname, "error": None,
                                   "result": None, "seconds": 0.0}
            report[n] = rec
            if skip and n in skip:
                rec.update(state="skipped", error="skipped by caller")
                continue
            need = [r for r in REQUIRES.get(n, []) if r not in _INSTALLED]
            if need and (only is None or all(r in only for r in need)):
                rec.update(error="requires group(s) %s installed first" % need)
                continue
            t0 = time.time()
            try:
                mod = importlib.import_module(modname)
                if n in _INSTALLED:
                    rec["state"] = "already"
                else:
                    rec["result"] = _call(mod.install, host, options.get(n))
                    if rec["result"] is False:
                        # install() returns False when the layer was already present
                        rec["state"] = "already"
                    else:
                        rec["state"] = "ok"
                    _MODULES[n] = mod
                    _INSTALLED.append(n)
            except Exception as e:
                if _module_missing(e, modname):
                    rec.update(state="absent", error="installer file not supplied")
                else:
                    rec["error"] = "%s: %s (%s)" % (type(e).__name__, e, _short_tb())
                    log.warning("group %s failed to install: %s", n, rec["error"])
            rec["seconds"] = round(time.time() - t0, 4)
        for n, why in NO_INSTALLER.items():
            if only is None or n in only:
                report.setdefault(n, {"state": "skipped", "module": None, "error": why})
        if harden:
            report["hardening"] = _apply_hardening(host)
    return report


def _apply_hardening(host: Any) -> Dict[str, Any]:
    global _HARDENING_APPLIED
    try:
        hard = importlib.import_module("nebula_hardening")
        rep = hard.apply(host)
        _HARDENING_APPLIED = True
        return {"state": "ok", "error": None, "result": rep}
    except Exception as e:
        if _module_missing(e, "nebula_hardening"):
            return {"state": "absent", "error": "nebula_hardening.py not supplied"}
        return {"state": "failed", "error": "%s: %s" % (type(e).__name__, e)}


def uninstall_all(host: Any) -> Dict[Any, Dict[str, Any]]:
    """Undo install_all() in strict reverse order. Never raises."""
    global _HARDENING_APPLIED
    report: Dict[Any, Dict[str, Any]] = {}
    with _LOCK:
        for key, hub in list(_HUBS.items()):
            try:
                hub.detach()
            except Exception:
                _NB_SWALLOW_LOG.debug("swallowed Exception in uninstall_all", exc_info=True)
        _HUBS.clear()
        if _HARDENING_APPLIED:
            try:
                report["hardening"] = {"ok": True,
                                       "reverted": importlib.import_module("nebula_hardening").revert()}
            except Exception as e:
                report["hardening"] = {"ok": False, "error": "%s: %s" % (type(e).__name__, e)}
            _HARDENING_APPLIED = False
        for n in reversed(list(_INSTALLED)):
            rec: Dict[str, Any] = {"ok": False, "error": None}
            try:
                mod = _MODULES.get(n)
                if mod is None:
                    raise RuntimeError("module not loaded")
                mod.uninstall(host)
                rec["ok"] = True
            except Exception as e:
                rec["error"] = "%s: %s" % (type(e).__name__, e)
            report[n] = rec
        _INSTALLED.clear()
        _MODULES.clear()
    return report


def installed_groups() -> List[int]:
    with _LOCK:
        return list(_INSTALLED)


# --------------------------------------------------------------------------- #
# Hubs (group10 stack, group14 chain) - need a live blockchain object
# --------------------------------------------------------------------------- #
def attach_hubs(node: Any, **kw: Any) -> Dict[str, str]:
    out: Dict[str, str] = {}
    bc = getattr(node, "bc", None)
    if bc is None:
        return {"group10": "FAILED: node has no .bc", "group14": "FAILED: node has no .bc"}
    builders = (
        ("group10", "nebula_group10_stack",
         lambda m: m.Group10Stack(blockchain=bc, node=getattr(node, "p2p", None), **kw.get("g10", {}))),
        ("group14", "nebula_group14_chain",
         lambda m: m.Group14Chain(bc, **kw.get("g14", {}))),
    )
    with _LOCK:
        for key, modname, build in builders:
            try:
                hub = build(importlib.import_module(modname))
                if key == "group10":
                    hub.attach(bc)
                else:
                    hub.attach()
                _HUBS[key] = hub
                setattr(node, key, hub)
                out[key] = "ok"
            except Exception as e:
                if _module_missing(e, modname):
                    out[key] = "absent: %s not supplied" % modname
                else:
                    out[key] = "FAILED: %s: %s" % (type(e).__name__, e)
    return out


# --------------------------------------------------------------------------- #
# Status / summary
# --------------------------------------------------------------------------- #
def _layer(node: Any, n: int) -> Any:
    return getattr(node, "group%02d" % n, None) if n < 10 else getattr(node, "group%d" % n, None)


def status(node: Any) -> Dict[str, Any]:
    """Read-only: which group layers are really attached to a started node."""
    layers: Dict[int, Dict[str, Any]] = {}
    for n, _ in GROUPS:
        layer = _layer(node, n)
        if layer is None and n < 10:
            layer = getattr(node, "group%d" % n, None)
        err = getattr(node, "group%d_error" % n, None)
        entry: Dict[str, Any] = {"attached": layer is not None,
                                 "init_error": None if err is None else repr(err)}
        if layer is not None:
            errs = getattr(layer, "errors", None)
            if callable(errs):
                try:
                    errs = errs()
                except Exception:
                    errs = None
            if isinstance(errs, int):
                entry["errors"] = errs
            elif isinstance(errs, (list, tuple, dict)):
                entry["errors"] = len(errs)
            last = getattr(layer, "last_error", None)
            if last:
                entry["last_error"] = str(last)
        layers[n] = entry
    for hub in ("group10", "group14"):
        layers[int(hub[5:])] = {"attached": getattr(node, hub, None) is not None, "init_error": None}
    attached = sorted(n for n, e in layers.items() if e["attached"])
    expected = [n for n in installed_groups()] + [int(h[5:]) for h in _HUBS]
    missing = sorted(n for n in set(expected) if not layers.get(n, {}).get("attached"))
    return {"attached": attached, "missing_after_install": missing,
            "not_installed": sorted(n for n in layers if n not in attached and n not in expected),
            "total_layer_errors": sum(e.get("errors", 0) for e in layers.values()),
            "all_installed_attached": not missing, "layers": layers}


def summary(report: Dict[Any, Dict[str, Any]]) -> str:
    """Short human-readable text of an install_all() report."""
    def ids(state: str) -> List[Any]:
        return [n for n, r in report.items() if n != "hardening" and r.get("state") == state]
    lines = ["installed OK : %s" % (ids("ok") or "none"),
             "already      : %s" % (ids("already") or "none"),
             "absent files : %s" % (ids("absent") or "none"),
             "skipped      : %s" % (ids("skipped") or "none")]
    for n in ids("failed"):
        lines.append("group%s FAILED: %s" % (n, report[n].get("error")))
    h = report.get("hardening")
    if h is not None:
        lines.append("hardening    : %s%s" % (h.get("state"), "" if not h.get("error") else " (%s)" % h["error"]))
    return "\n".join(lines)


if __name__ == "__main__":
    try:
        import nebula_v10_11 as _host
    except Exception as exc:
        raise SystemExit("cannot import nebula_v10_11: %s" % exc)
    _problems = preflight(_host)
    print("preflight:", _problems or "OK")
    print(summary(install_all(_host)))
