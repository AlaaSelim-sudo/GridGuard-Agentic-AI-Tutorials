# -*- coding: utf-8 -*-
"""
GridGuard — Physics-Informed OPRO for Distribution Grid Operation
- OPRO-style meta-prompt loop (Optimization by PROmpting)
- LLM proposals evaluated by OpenDSS (external evaluator)
- Meta-prompt viewer (FEASIBLE_FRONTIER + REJECTED_RECENT)
- Teaching note grounded by measured before/after numbers (no hallucinated voltages)
- "Prefer utility devices first" toggle (taps/caps first; delay VAR-gen/PV/Load until stuck>=N)
- Physics pool is a delayed guardrail only (optional)
"""

import os
import sys
import json
import hashlib
import math
import time
import traceback
import subprocess
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, TypedDict

import numpy as np
import pandas as pd
import requests

# The physics/StateGraph engine is also used by a command-line runner.  Keep the
# desktop UI optional so headless execution does not require Qt or matplotlib.
_GUI_AVAILABLE = True
_GUI_IMPORT_ERROR_TEXT = ""
_GRIDGUARD_HEADLESS = os.environ.get("GRIDGUARD_HEADLESS", "").strip().lower() in {
    "1", "true", "yes", "on"
}

class _MissingGuiClass:
    def __init__(self, *args, **kwargs):
        raise RuntimeError(
            "The optional desktop UI requires PySide6 and matplotlib; use "
            "scripts/run_gridguard_headless.py for command-line execution."
        )

try:
    if _GRIDGUARD_HEADLESS:
        raise ImportError("desktop imports disabled by GRIDGUARD_HEADLESS")
    from PySide6.QtCore import Qt, QThread, Signal
    from PySide6.QtGui import QPalette, QColor
    from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget,
        QVBoxLayout, QHBoxLayout, QGridLayout,
        QLabel, QLineEdit, QPushButton, QPlainTextEdit,
        QTableWidget, QTableWidgetItem, QGroupBox, QMessageBox,
        QSplitter, QComboBox, QCheckBox
    )
except ImportError as exc:
    _GUI_AVAILABLE = False
    _GUI_IMPORT_ERROR_TEXT = str(exc)

    class _MissingQtNamespace:
        Horizontal = None
        ItemIsEditable = None

    Qt = _MissingQtNamespace()
    QThread = QApplication = QMainWindow = QWidget = _MissingGuiClass
    QVBoxLayout = QHBoxLayout = QGridLayout = _MissingGuiClass
    QLabel = QLineEdit = QPushButton = QPlainTextEdit = _MissingGuiClass
    QTableWidget = QTableWidgetItem = QGroupBox = QMessageBox = _MissingGuiClass
    QSplitter = QComboBox = QCheckBox = QPalette = QColor = _MissingGuiClass

    def Signal(*args, **kwargs):
        return None

if _GUI_AVAILABLE:
    try:
        import matplotlib
        matplotlib.use("QtAgg")
        from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
    except ImportError as exc:
        _GUI_AVAILABLE = False
        _GUI_IMPORT_ERROR_TEXT = str(exc)
        Figure = FigureCanvas = _MissingGuiClass
else:
    Figure = FigureCanvas = _MissingGuiClass

from opendssdirect import dss

try:
    from langgraph.graph import END, START, StateGraph
except ImportError:  # The GUI can still open and explain the missing runtime dependency.
    END = START = StateGraph = None


# =========================
# Defaults / folders
# =========================
DEFAULT_TESTCASES_ROOT = r"C:\Program Files\OpenDSS\IEEETestCases"
V_MIN_PU_DEFAULT = 0.95
V_MAX_PU_DEFAULT = 1.05

DOCS_DIR = Path.home() / "Documents"
RUN_DIR = Path(os.environ.get("GRIDGUARD_RUN_DIR", DOCS_DIR / "OpenDSS_OPRO"))
RUN_DIR.mkdir(parents=True, exist_ok=True)

_DSS_LLM_WINDOW = None


# =========================
# Dark mode
# =========================
def apply_dark_mode(app: QApplication):
    app.setStyle("Fusion")
    pal = QPalette()
    pal.setColor(QPalette.Window, QColor(28, 28, 30))
    pal.setColor(QPalette.WindowText, QColor(230, 230, 235))
    pal.setColor(QPalette.Base, QColor(18, 18, 20))
    pal.setColor(QPalette.AlternateBase, QColor(35, 35, 38))
    pal.setColor(QPalette.Text, QColor(230, 230, 235))
    pal.setColor(QPalette.Button, QColor(45, 45, 48))
    pal.setColor(QPalette.ButtonText, QColor(235, 235, 240))
    pal.setColor(QPalette.Highlight, QColor(90, 150, 255))
    pal.setColor(QPalette.HighlightedText, QColor(10, 10, 12))
    pal.setColor(QPalette.Disabled, QPalette.Text, QColor(140, 140, 145))
    pal.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(140, 140, 145))
    pal.setColor(QPalette.Disabled, QPalette.WindowText, QColor(140, 140, 145))
    app.setPalette(pal)

    app.setStyleSheet("""
        QGroupBox {
            border: 1px solid #3a3a3d;
            margin-top: 10px;
            border-radius: 6px;
            padding: 6px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 4px 0 4px;
        }
        QLineEdit, QPlainTextEdit, QComboBox {
            border: 1px solid #3a3a3d;
            border-radius: 6px;
            padding: 6px;
            background: #121214;
        }
        QPushButton {
            border: 1px solid #3a3a3d;
            border-radius: 8px;
            padding: 8px;
            background: #2d2d30;
        }
        QPushButton:hover { background: #3a3a3d; }
        QPushButton:pressed { background: #242427; }
        QTableWidget {
            border: 1px solid #3a3a3d;
            border-radius: 6px;
            gridline-color: #3a3a3d;
            background: #121214;
        }
        QHeaderView::section {
            background-color: #2d2d30;
            padding: 6px;
            border: 1px solid #3a3a3d;
        }
    """)


# =========================
# Fast testcase scanning
# =========================
def _find_main_dss_fast(folder: Path) -> Optional[str]:
    for name in ("Master.dss", "master.dss"):
        p = folder / name
        if p.exists():
            return str(p)
    direct = sorted(folder.glob("*.dss"))
    if direct:
        for f in direct:
            if "master" in f.name.lower():
                return str(f)
        return str(direct[0])
    second = sorted(folder.glob("*/*.dss"))
    if second:
        for f in second:
            if "master" in f.name.lower():
                return str(f)
        return str(second[0])
    return None


def scan_testcases_root_fast(root: str) -> List[Dict[str, str]]:
    root_p = Path(root)
    if not root_p.exists():
        return []
    cases = []
    with os.scandir(root) as it:
        for entry in it:
            if not entry.is_dir():
                continue
            folder = Path(entry.path)
            main_dss = _find_main_dss_fast(folder)
            if main_dss:
                cases.append({"label": entry.name, "folder": str(folder), "main_dss": main_dss})
    cases.sort(key=lambda x: x["label"].lower())
    return cases


# =========================
# OpenDSS helpers
# =========================
def _as_float_list(x) -> List[float]:
    if x is None:
        return []
    try:
        return [float(v) for v in x]
    except Exception:
        return []


def dss_query(cmd: str) -> str:
    try:
        dss.Text.Command(cmd)
        r = getattr(dss.Text, "Result", "")
        return r() if callable(r) else (r or "")
    except Exception as e:
        return f"(query_error) {e}"


def _circuit_all_element_names() -> List[str]:
    try:
        if hasattr(dss.Circuit, "AllElementNames"):
            return dss.Circuit.AllElementNames() or []
    except Exception:
        pass
    return []


def _element_names_by_class(cls: str) -> List[str]:
    cls = cls.lower().strip()
    prefix = cls + "."
    out = []
    for e in _circuit_all_element_names():
        e = (e or "").strip()
        if e.lower().startswith(prefix) and "." in e:
            out.append(e.split(".", 1)[1])
    seen = set()
    uniq = []
    for x in out:
        xl = x.lower()
        if xl not in seen:
            seen.add(xl)
            uniq.append(x)
    return uniq


def discover_devices() -> Dict[str, List[str]]:
    def allnames(iface_candidates: List[str], fallback_cls: str) -> List[str]:
        for nm in iface_candidates:
            if hasattr(dss, nm):
                iface = getattr(dss, nm)
                try:
                    return list(iface.AllNames() or [])
                except Exception:
                    pass
        return _element_names_by_class(fallback_cls)

    devices = {
        "regcontrols": allnames(["RegControls"], "regcontrol"),
        "capacitors": allnames(["Capacitors"], "capacitor"),
        "pvsystems": allnames(["PVsystems", "PVSystems"], "pvsystem"),
        "invcontrols": allnames(["InvControls", "InvControl"], "invcontrol"),
        "capcontrols": allnames(["CapControls", "CapControl"], "capcontrol"),
        "storages": allnames(["Storages", "Storage"], "storage"),
        "storagecontrollers": allnames(
            ["StorageControllers", "StorageController"], "storagecontroller"
        ),
        "generators": allnames(["Generators", "Generator"], "generator"),
        "loads": allnames(["Loads", "Load"], "load"),
        "lines": allnames(["Lines"], "line"),
        "transformers": allnames(["Transformers"], "transformer"),
    }
    switchable: List[str] = []
    if hasattr(dss, "Lines"):
        for name in devices["lines"]:
            try:
                dss.Lines.Name(name)
                is_switch = getattr(dss.Lines, "IsSwitch", None)
                if callable(is_switch) and bool(is_switch()):
                    switchable.append(name)
            except Exception:
                continue
    devices["switchable_lines"] = switchable
    return devices


def _topology_counter(name: str) -> int:
    """Read an OpenDSS Topology counter without depending on one API version."""
    try:
        member = getattr(dss.Topology, name, None)
        value = member() if callable(member) else member
        return max(0, int(value or 0))
    except Exception:
        return 0


def collect_topology_metrics(lines: List[str]) -> Dict[str, Any]:
    """Capture stable graph topology plus OpenDSS diagnostic counters.

    OpenDSS' topology iterator can change its internal traversal state after
    other API calls, so its loop/isolation counters are retained only as
    diagnostics.  Certification uses an independently constructed energized
    bus-branch graph from enabled, closed lines and enabled transformers.
    """
    status: List[Tuple[str, str]] = []
    active_edges: List[Tuple[str, str, str]] = []
    nodes: set[str] = set()

    def base_bus(value: Any) -> str:
        return str(value or "").split(".", 1)[0].strip().lower()

    def active_element_buses(element: str) -> List[str]:
        dss.Circuit.SetActiveElement(element)
        return [
            bus for bus in (
                base_bus(item)
                for item in (getattr(dss.CktElement, "BusNames", lambda: [])() or [])
            ) if bus
        ]

    for name in lines:
        try:
            buses = active_element_buses(f"Line.{name}")
            enabled_fn = getattr(dss.CktElement, "Enabled", None)
            enabled = bool(enabled_fn()) if callable(enabled_fn) else True
            nterms = max(1, int(getattr(dss.CktElement, "NumTerminals", lambda: 1)()))
            nconds = max(1, int(getattr(dss.CktElement, "NumConductors", lambda: 1)()))
            is_open = False
            open_fn = getattr(dss.CktElement, "IsOpen", None)
            if callable(open_fn):
                for terminal in range(1, nterms + 1):
                    for conductor in range(1, nconds + 1):
                        if bool(open_fn(terminal, conductor)):
                            is_open = True
                            break
                    if is_open:
                        break
            status.append((
                name.lower(), "disabled" if not enabled else ("open" if is_open else "closed")
            ))
            if enabled and not is_open and len(buses) >= 2:
                anchor = buses[0]
                for bus in buses[1:]:
                    nodes.update((anchor, bus))
                    active_edges.append((anchor, bus, f"line.{name.lower()}"))
        except Exception:
            status.append((name.lower(), "unknown"))

    transformer_names: List[str] = []
    try:
        transformer_names = list(dss.Transformers.AllNames() or [])
    except Exception:
        transformer_names = _element_names_by_class("transformer")
    transformer_status: List[Tuple[str, str]] = []
    for name in transformer_names:
        try:
            buses = active_element_buses(f"Transformer.{name}")
            enabled_fn = getattr(dss.CktElement, "Enabled", None)
            enabled = bool(enabled_fn()) if callable(enabled_fn) else True
            transformer_status.append((name.lower(), "enabled" if enabled else "disabled"))
            if enabled and len(buses) >= 2:
                anchor = buses[0]
                for bus in buses[1:]:
                    nodes.update((anchor, bus))
                    active_edges.append((anchor, bus, f"transformer.{name.lower()}"))
        except Exception:
            transformer_status.append((name.lower(), "unknown"))

    source_buses: set[str] = set()
    try:
        source_names = list(dss.Vsources.AllNames() or [])
    except Exception:
        source_names = _element_names_by_class("vsource")
    for name in source_names:
        try:
            buses = active_element_buses(f"Vsource.{name}")
            source_buses.update(buses)
            nodes.update(buses)
        except Exception:
            continue

    load_buses: List[str] = []
    try:
        load_names = list(dss.Loads.AllNames() or [])
    except Exception:
        load_names = _element_names_by_class("load")
    for name in load_names:
        try:
            buses = active_element_buses(f"Load.{name}")
            enabled_fn = getattr(dss.CktElement, "Enabled", None)
            enabled = bool(enabled_fn()) if callable(enabled_fn) else True
            if enabled and buses:
                load_buses.append(buses[0])
                nodes.add(buses[0])
        except Exception:
            continue

    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}

    def find(node: str) -> str:
        root = node
        while parent[root] != root:
            root = parent[root]
        while parent[node] != node:
            next_node = parent[node]
            parent[node] = root
            node = next_node
        return root

    def union(left: str, right: str) -> None:
        root_left, root_right = find(left), find(right)
        if root_left == root_right:
            return
        if rank[root_left] < rank[root_right]:
            root_left, root_right = root_right, root_left
        parent[root_right] = root_left
        if rank[root_left] == rank[root_right]:
            rank[root_left] += 1

    for left, right, _element in active_edges:
        union(left, right)
    component_roots = {find(node) for node in nodes} if nodes else set()
    source_roots = {find(bus) for bus in source_buses if bus in parent}
    disconnected_loads = sum(
        1 for bus in load_buses
        if bus not in parent or find(bus) not in source_roots
    )
    cycle_rank = max(0, len(active_edges) - len(nodes) + len(component_roots))

    encoded = json.dumps(
        {"lines": sorted(status), "transformers": sorted(transformer_status)},
        sort_keys=True, separators=(",", ":"),
    ).encode("utf-8")
    return {
        "topology_hash": hashlib.sha256(encoded).hexdigest()[:16],
        "network_nodes": len(nodes),
        "network_active_edges": len(active_edges),
        "network_components": len(component_roots),
        "network_cycle_rank": cycle_rank,
        "source_bus_count": len(source_buses),
        "source_disconnected_loads": disconnected_loads,
        "isolated_branches": _topology_counter("NumIsolatedBranches"),
        "isolated_loads": _topology_counter("NumIsolatedLoads"),
        "loops": _topology_counter("NumLoops"),
        "line_status": dict(status),
    }


def collect_load_service(energized_threshold_pu: float = 0.10) -> Dict[str, Any]:
    """Estimate served and unserved enabled load from solved bus voltage."""
    served_kw = 0.0
    unserved_kw = 0.0
    load_status_kw: Dict[str, Dict[str, Any]] = {}
    names: List[str] = []
    try:
        load_multiplier = float(dss.Solution.LoadMult())
    except Exception:
        load_multiplier = 1.0
    try:
        names = list(dss.Loads.AllNames() or [])
    except Exception:
        names = _element_names_by_class("load")

    for name in names:
        try:
            dss.Loads.Name(name)
            dss.Circuit.SetActiveElement(f"Load.{name}")
            enabled_fn = getattr(dss.CktElement, "Enabled", None)
            if callable(enabled_fn) and not bool(enabled_fn()):
                continue
            # OpenDSSDirect returns the unscaled load definition here. Apply
            # the active snapshot multiplier so restoration benefit reflects
            # the scenario actually being solved.
            kw = max(0.0, float(dss.Loads.kW()) * load_multiplier)
            buses = getattr(dss.CktElement, "BusNames", lambda: [])() or []
            bus = str(buses[0]).split(".", 1)[0] if buses else ""
            vmax = 0.0
            if bus:
                dss.Circuit.SetActiveBus(bus)
                pu = _as_float_list(dss.Bus.puVmagAngle()[0::2])
                vmax = max(pu) if pu else 0.0
            if vmax >= energized_threshold_pu:
                served_kw += kw
                load_status_kw[name] = {"kw": kw, "served": True}
            else:
                unserved_kw += kw
                load_status_kw[name] = {"kw": kw, "served": False}
        except Exception:
            continue
    return {
        "served_load_kw": served_kw,
        "unserved_load_kw": unserved_kw,
        "load_status_kw": load_status_kw,
        "load_multiplier": load_multiplier,
    }


def safe_bus_exists(bus: str) -> bool:
    try:
        return bus in (dss.Circuit.AllBusNames() or [])
    except Exception:
        return False


def bus_kv_infer(bus: str) -> Tuple[float, int]:
    """
    Robust kV inference for created PV/Gen/Load (prevents silly kV that can diverge).
    Returns (kV_LL, phases).
    """
    try:
        dss.Circuit.SetActiveBus(bus)
        pu = dss.Bus.puVmagAngle()
        vm = dss.Bus.VMagAngle()
        pu_m = _as_float_list(pu[0::2])
        vm_m = _as_float_list(vm[0::2])

        bases = []
        for v, p in zip(vm_m, pu_m):
            if p and p > 1e-6 and v and v > 1e-3:
                bases.append(v / p)

        kv_ln = None
        if bases:
            kv_ln = float(np.median(np.array(bases))) / 1000.0

        if kv_ln is None or kv_ln <= 0:
            kv_ln = float(dss.Bus.kVBase())
            if kv_ln <= 0:
                kv_ln = 4.16 / math.sqrt(3.0)

        nodes = int(dss.Bus.NumNodes())
        ph = max(1, min(3, nodes))
        kv = kv_ln * math.sqrt(3.0) if ph >= 2 else kv_ln
        if kv <= 0:
            kv = 4.16
        return kv, ph
    except Exception:
        return 4.16, 3


def collect_lines_loading(top_k: Optional[int] = None) -> pd.DataFrame:
    names = []
    if hasattr(dss, "Lines"):
        try:
            names = list(dss.Lines.AllNames() or [])
        except Exception:
            names = []
    if not names:
        names = _element_names_by_class("line")

    rows = []
    for nm in names:
        try:
            norm_amps = np.nan
            if hasattr(dss, "Lines"):
                try:
                    dss.Lines.Name(nm)
                    norm_amps = dss.Lines.NormAmps()
                except Exception:
                    norm_amps = np.nan

            dss.Circuit.SetActiveElement(f"Line.{nm}")
            buses = getattr(dss.CktElement, "BusNames", lambda: [])() or []
            bus1 = buses[0] if len(buses) > 0 else ""
            bus2 = buses[1] if len(buses) > 1 else ""

            ia = _as_float_list(getattr(dss.CktElement, "CurrentsMagAng", lambda: [])())
            mags = ia[0::2]
            imax = float(np.max(mags)) if mags else np.nan

            pct = (imax / norm_amps * 100.0) if (not np.isnan(imax) and not np.isnan(norm_amps) and norm_amps > 0) else np.nan
            rows.append({"line": nm, "bus1": bus1, "bus2": bus2, "imax_a": imax, "norm_amps": norm_amps, "%norm": pct})
        except Exception as e:
            rows.append({"line": nm, "error": str(e)})

    df = pd.DataFrame(rows)
    if "%norm" in df.columns:
        df = df.sort_values(["%norm", "line"], ascending=[False, True]).reset_index(drop=True)
    # Keep the complete population for certification metrics.  Truncating this
    # table before summarize_metrics() silently under-counted overloaded lines
    # on large SMART-DS cases; callers that only need a display subset can opt
    # in to a limit or use top_overloaded_lines().
    if top_k is not None:
        return df.head(max(0, int(top_k)))
    return df


# =========================
# RegControl -> Transformer mapping
# =========================
def _parse_transformer_from_regcontrol_help(txt: str) -> Optional[str]:
    if not isinstance(txt, str) or not txt:
        return None
    m = re.search(r"(Transformer\.[A-Za-z0-9_\-]+)", txt, flags=re.I)
    if m:
        return m.group(1).split(".", 1)[1]
    m = re.search(r"transformer\s*=\s*([A-Za-z0-9_\-]+)", txt, flags=re.I)
    if m:
        return m.group(1)
    return None


def _guess_transformer_name(reg: str, transformers: List[str]) -> Optional[str]:
    if not transformers:
        return None
    tr_set = {t.lower(): t for t in transformers}
    r = reg.strip()
    candidates = [r]
    if r.lower().startswith("c") and len(r) > 1:
        candidates.append(r[1:])
    if r.lower().startswith("creg"):
        candidates.append("reg" + r[4:])
    if not r.lower().startswith("reg"):
        candidates.append("reg" + r)
    if len(r) > 2 and r[-1].lower() in ("a", "b", "c"):
        candidates.append(r[:-1])
        if r.lower().startswith("c"):
            candidates.append(r[1:-1])
        if r.lower().startswith("creg"):
            candidates.append("reg" + r[4:-1])

    for c in candidates:
        if c.lower() in tr_set:
            return tr_set[c.lower()]

    rl = r.lower().lstrip("c")
    for t in transformers:
        if rl and rl in t.lower():
            return t
    return None


def get_regcontrol_controlled_transformer(reg_name: str, devs: Dict[str, List[str]]) -> Tuple[Optional[str], int, float, str]:
    wdg = 1
    tap_inc = 0.00625

    try:
        if hasattr(dss, "RegControls"):
            dss.RegControls.Name(reg_name)
            # OpenDSSDirect exposes the controlled transformer and both the
            # monitored/tap windings directly.  SMART-DS regulators control
            # winding 2, so the old winding-1 default produced wrong tap edits.
            if hasattr(dss.RegControls, "TapWinding"):
                try:
                    api_wdg = int(dss.RegControls.TapWinding())
                    if api_wdg > 0:
                        wdg = api_wdg
                except Exception:
                    pass
            if wdg == 1 and hasattr(dss.RegControls, "Winding"):
                try:
                    api_wdg = int(dss.RegControls.Winding())
                    if api_wdg > 0:
                        wdg = api_wdg
                except Exception:
                    pass
            if hasattr(dss.RegControls, "Transformer"):
                xf = dss.RegControls.Transformer()
                if isinstance(xf, str) and xf.strip():
                    xf = xf.split(".", 1)[-1].strip()
                    try:
                        dss.Transformers.Name(xf)
                        dss.Transformers.Wdg(wdg)
                        ntaps = int(dss.Transformers.NumTaps())
                        if ntaps > 0:
                            tap_inc = (
                                float(dss.Transformers.MaxTap())
                                - float(dss.Transformers.MinTap())
                            ) / ntaps
                    except Exception:
                        pass
                    return xf, wdg, tap_inc, "api.Transformer"
            if hasattr(dss.RegControls, "ControlledElement"):
                ce = dss.RegControls.ControlledElement()
                if isinstance(ce, str) and ce.lower().startswith("transformer.") and "." in ce:
                    return ce.split(".", 1)[1], wdg, tap_inc, "api.ControlledElement"
    except Exception:
        pass

    txt = dss_query(f"? RegControl.{reg_name}")
    xf = _parse_transformer_from_regcontrol_help(txt)
    if xf:
        return xf, wdg, tap_inc, "help.parse"

    xf = _guess_transformer_name(reg_name, devs.get("transformers", []) or [])
    if xf:
        return xf, wdg, tap_inc, "guess.name"

    return None, wdg, tap_inc, "none"


def read_transformer_tap(xfmr: str, wdg: int) -> Optional[float]:
    try:
        if hasattr(dss, "Transformers"):
            dss.Transformers.Name(xfmr)
            if hasattr(dss.Transformers, "Wdg"):
                try:
                    dss.Transformers.Wdg(wdg)
                except Exception:
                    pass
            if hasattr(dss.Transformers, "Tap"):
                return float(dss.Transformers.Tap())
    except Exception:
        pass
    return None


# =========================
# Snapshot
# =========================
@dataclass
class SnapshotResult:
    case_label: str
    case_folder: str
    compiled_file: str
    solved: bool
    total_losses_kw: float
    total_losses_kvar: float
    total_p_kw: float
    total_q_kvar: float
    bus_df: pd.DataFrame
    line_df: pd.DataFrame
    devices: Dict[str, List[str]]
    reg_map: Dict[str, Dict[str, Any]]
    served_load_kw: float
    unserved_load_kw: float
    load_status_kw: Dict[str, Dict[str, Any]]
    isolated_branches: int
    isolated_loads: int
    topology_loops: int
    topology_hash: str
    raw_notes: str
    line_status: Dict[str, str] = field(default_factory=dict)
    recovery_applied: bool = False
    load_multiplier: float = 1.0
    network_nodes: int = 0
    network_active_edges: int = 0
    network_components: int = 0
    network_cycle_rank: int = 0
    source_bus_count: int = 0
    source_disconnected_loads: int = 0


def build_reg_map(devs: Dict[str, List[str]]) -> Dict[str, Dict[str, Any]]:
    out = {}
    regs = devs.get("regcontrols", []) or []
    for r in regs:
        xfmr, wdg, tap_inc, src = get_regcontrol_controlled_transformer(r, devs)
        tap = None
        if xfmr:
            tap = read_transformer_tap(xfmr, wdg)
        out[r] = {"xfmr": xfmr, "wdg": wdg, "tap": tap, "tap_inc": tap_inc, "src": src}
    return out


def _try_recovery(notes: List[str]):
    for cmd in [
        "calcvoltagebases",
        "set maxiterations=300",
        "set maxcontroliter=300",
        "set controlmode=off",
        "set algorithm=newton",
        "set tolerance=0.0001",
    ]:
        try:
            dss.Text.Command(cmd)
            notes.append(f"> {cmd}")
        except Exception:
            pass


def compile_and_solve(case_label: str, case_folder: str, dss_path: str,
                      commands: List[str], vmin_limit: float, vmax_limit: float,
                      recover_on_failure: bool = True) -> SnapshotResult:
    notes = []
    dss.Basic.ClearAll()

    cmd = f"compile [{dss_path}]"
    dss.Text.Command(cmd)
    notes.append(f"> {cmd}")

    try:
        dss.Text.Command("calcvoltagebases")
        notes.append("> calcvoltagebases")
    except Exception:
        pass

    for c in commands:
        c = (c or "").strip()
        if c:
            if re.search(r"\bedit\s+vsource\.", c, flags=re.I):
                raise RuntimeError("Blocked: Edit Vsource.* is not allowed.")
            dss.Text.Command(c)
            notes.append(f"> {c}")

    dss.Solution.Mode(0)  # snapshot
    try:
        dss.Solution.Solve()
        solved = bool(dss.Solution.Converged())
    except Exception as exc:
        # Large SMART-DS cases can surface Max Control Iterations as an exception
        # rather than simply returning Converged=False. Route both forms through
        # the same deterministic recovery policy.
        solved = False
        notes.append(f"Initial solve error: {type(exc).__name__}: {exc}")

    recovery_applied = False
    if not solved and recover_on_failure:
        recovery_applied = True
        notes.append("Converged: False -> attempting recovery")
        _try_recovery(notes)
        try:
            dss.Solution.Solve()
            solved = bool(dss.Solution.Converged())
        except Exception as exc:
            solved = False
            notes.append(f"Recovery solve error: {type(exc).__name__}: {exc}")
    elif not solved:
        notes.append("Converged: False -> strict no-recovery policy retained")

    notes.append(f"Converged: {solved}")

    losses_w, losses_var = dss.Circuit.Losses()
    total_p_kw, total_q_kvar = dss.Circuit.TotalPower()

    rows = []
    for b in dss.Circuit.AllBusNames():
        try:
            dss.Circuit.SetActiveBus(b)
            pu = dss.Bus.puVmagAngle()
            mags = _as_float_list(pu[0::2])
            if mags:
                vmin = float(np.min(mags))
                vmax = float(np.max(mags))
                vavg = float(np.mean(mags))
            else:
                vmin = vmax = vavg = np.nan
            # A fully de-energized island is a restoration problem, not a
            # conventional ANSI-voltage violation.  Keep partially energized
            # or missing-phase buses in the voltage screen, but account for an
            # all-zero bus through the separate service/restoration metrics.
            energized = bool(not np.isnan(vmax) and vmax >= 0.10)
            viol = bool(energized and (
                (not np.isnan(vmin) and vmin < vmin_limit)
                or (not np.isnan(vmax) and vmax > vmax_limit)
            ))
            rows.append({
                "bus": b,
                "phases": getattr(dss.Bus, "NumNodes", lambda: np.nan)(),
                "vmin_pu": vmin, "vmax_pu": vmax, "vavg_pu": vavg,
                "energized": energized, "violation": viol
            })
        except Exception as e:
            rows.append({"bus": b, "error": str(e)})

    bus_df = pd.DataFrame(rows)
    if "violation" in bus_df.columns and "vavg_pu" in bus_df.columns:
        bus_df = bus_df.sort_values(["violation", "vavg_pu", "bus"], ascending=[False, True, True]).reset_index(drop=True)

    line_df = collect_lines_loading()
    devs = discover_devices()
    reg_map = build_reg_map(devs)
    service = collect_load_service()
    topology = collect_topology_metrics(devs.get("lines", []))

    return SnapshotResult(
        case_label=case_label, case_folder=case_folder, compiled_file=dss_path,
        solved=solved,
        total_losses_kw=float(losses_w / 1000.0),
        total_losses_kvar=float(losses_var / 1000.0),
        total_p_kw=float(total_p_kw),
        total_q_kvar=float(total_q_kvar),
        bus_df=bus_df,
        line_df=line_df,
        devices=devs,
        reg_map=reg_map,
        served_load_kw=float(service["served_load_kw"]),
        unserved_load_kw=float(service["unserved_load_kw"]),
        load_status_kw=dict(service["load_status_kw"]),
        isolated_branches=int(topology["isolated_branches"]),
        isolated_loads=int(topology["isolated_loads"]),
        topology_loops=int(topology["loops"]),
        topology_hash=str(topology["topology_hash"]),
        raw_notes="\n".join(notes),
        line_status=dict(topology.get("line_status", {})),
        recovery_applied=recovery_applied,
        load_multiplier=float(service.get("load_multiplier", 1.0)),
        network_nodes=int(topology.get("network_nodes", 0)),
        network_active_edges=int(topology.get("network_active_edges", 0)),
        network_components=int(topology.get("network_components", 0)),
        network_cycle_rank=int(topology.get("network_cycle_rank", 0)),
        source_bus_count=int(topology.get("source_bus_count", 0)),
        source_disconnected_loads=int(topology.get("source_disconnected_loads", 0)),
    )


def summarize_metrics(res: SnapshotResult, vmin: float, vmax: float) -> Dict[str, Any]:
    df = res.bus_df.copy()
    viols = int(df["violation"].sum()) if "violation" in df.columns else 0

    bus_measurement_count = 0
    if "vmin_pu" in df.columns and "vmax_pu" in df.columns:
        bus_measurement_count = int(
            (pd.to_numeric(df["vmin_pu"], errors="coerce").notna()
             & pd.to_numeric(df["vmax_pu"], errors="coerce").notna()).sum()
        )
    bus_voltage_coverage_rate = bus_measurement_count / max(1, len(df))

    operating_df = df[df["energized"] == True] if "energized" in df.columns else df
    deenergized_buses = int((df["energized"] == False).sum()) if "energized" in df.columns else 0
    vmin_arr = operating_df.get("vmin_pu", pd.Series([], dtype=float)).fillna(1e9).to_numpy(dtype=float)
    vmax_arr = operating_df.get("vmax_pu", pd.Series([], dtype=float)).fillna(-1e9).to_numpy(dtype=float)
    under = np.maximum(0.0, vmin - vmin_arr)
    over = np.maximum(0.0, vmax_arr - vmax)
    v_sev = float(np.sum(under + over))

    over_lines = 0
    max_pct = np.nan
    thermal_severity_pct_sum = 0.0
    line_loading_p95_pct = np.nan
    line_rating_count = 0
    total_line_count = len(res.line_df) if res.line_df is not None else 0
    if res.line_df is not None and not res.line_df.empty and "%norm" in res.line_df.columns:
        pct = res.line_df["%norm"].dropna().to_numpy(dtype=float)
        line_rating_count = len(pct)
        if len(pct) > 0:
            max_pct = float(np.max(pct))
            over_lines = int(np.sum(pct > 100.0))
            thermal_severity_pct_sum = float(np.sum(np.maximum(0.0, pct - 100.0)))
            line_loading_p95_pct = float(np.percentile(pct, 95.0))

    has_under = bool(np.any(vmin_arr < vmin - 1e-9))
    has_over = bool(np.any(vmax_arr > vmax + 1e-9))
    if has_under and has_over:
        viol_type = "mixed"
    elif has_under:
        viol_type = "undervoltage"
    elif has_over:
        viol_type = "overvoltage"
    else:
        viol_type = "none"

    return {
        "converged": bool(res.solved),
        "viol_buses": viols,
        "viol_type": viol_type,
        "deenergized_buses": deenergized_buses,
        "bus_measurement_count": bus_measurement_count,
        "bus_voltage_coverage_rate": float(bus_voltage_coverage_rate),
        "v_severity": v_sev,
        "losses_kw": float(res.total_losses_kw),
        "max_line_pct": max_pct,
        "line_loading_p95_pct": line_loading_p95_pct,
        "line_rating_count": int(line_rating_count),
        "line_loading_coverage_rate": float(line_rating_count / max(1, total_line_count)),
        "over_lines": over_lines,
        "thermal_severity_pct_sum": thermal_severity_pct_sum,
        "served_load_kw": float(res.served_load_kw),
        "unserved_load_kw": float(res.unserved_load_kw),
        "load_multiplier": float(res.load_multiplier),
        "isolated_branches": int(res.isolated_branches),
        "isolated_loads": int(res.isolated_loads),
        "topology_loops": int(res.topology_loops),
        "topology_hash": str(res.topology_hash),
        "network_nodes": int(res.network_nodes),
        "network_active_edges": int(res.network_active_edges),
        "network_components": int(res.network_components),
        "network_cycle_rank": int(res.network_cycle_rank),
        "source_bus_count": int(res.source_bus_count),
        "source_disconnected_loads": int(res.source_disconnected_loads),
        "recovery_applied": bool(res.recovery_applied),
    }


def objective(m: Dict[str, Any]) -> float:
    pen = 1e8 if not bool(m.get("converged", True)) else 0.0
    return (
        pen
        + 1e5 * float(m.get("unserved_load_kw", 0.0))
        + 1e6 * float(m.get("v_severity", 0.0))
        + 1e4 * float(m.get("viol_buses", 0))
        + 1e3 * float(m.get("over_lines", 0))
        + 1e2 * float(m.get("thermal_severity_pct_sum", 0.0))
        + 1e3 * float(m.get("network_cycle_rank", 0))
        + float(m.get("losses_kw", 0.0))
        + 100.0 * float(m.get("switching_effort", 0.0))
        + 100.0 * float(m.get("cumulative_control_effort", 0.0))
        + 5.0 * float(m.get("cumulative_device_action_count", 0.0))
    )


def operating_goal_satisfied(metrics: Dict[str, Any]) -> bool:
    """Absolute electrical/service terminal condition.

    Topology validity is enforced as a declared reference-state invariant in
    the certificate.  A universal ``loops == 0`` rule is inappropriate for
    supplied SMART-DS cases whose validated reference model contains parallel
    paths reported by OpenDSS as loops.
    """
    return bool(
        metrics.get("converged")
        and int(metrics.get("viol_buses", 0)) == 0
        and int(metrics.get("over_lines", 0)) == 0
        and float(metrics.get("unserved_load_kw", 0.0)) <= 1e-6
        and float(metrics.get("bus_voltage_coverage_rate", 0.0)) >= 0.999
        and float(metrics.get("line_loading_coverage_rate", 0.0)) >= 0.95
    )


def action_burden(actions_any: Any) -> Dict[str, float]:
    """Return transparent, unit-normalized control-burden components.

    This is deliberately a modest regularizer rather than a surrogate power-
    system cost.  It lets equal-budget studies distinguish two candidates with
    similar electrical benefit while preserving the violation-first objective.
    """
    actions = sanitize_actions(actions_any)
    pv_curtailment = 0.0
    storage_dispatch = 0.0
    tap_motion = 0.0
    discrete_ops = 0.0
    for action in actions:
        typ = _normalize_type(action.get("type", ""))
        if typ == "der_setpoint" and action.get("pct_pmpp") is not None:
            pv_curtailment += max(0.0, 100.0 - float(action["pct_pmpp"])) / 100.0
        elif typ == "storage_setpoint" and action.get("pct_kw") is not None:
            storage_dispatch += abs(float(action["pct_kw"])) / 100.0
        elif typ == "tap_step":
            tap_motion += abs(float(action.get("step", 0.0))) / 16.0
        elif typ in {"cap_state", "switch_line", "create_var_gen", "create_pv", "create_load"}:
            discrete_ops += 1.0
    return {
        "cumulative_device_action_count": float(len(actions)),
        "pv_curtailment_command_fraction_sum": pv_curtailment,
        "storage_dispatch_command_fraction_sum": storage_dispatch,
        "cumulative_tap_motion_normalized": tap_motion,
        "cumulative_discrete_operation_count": discrete_ops,
        "cumulative_control_effort": pv_curtailment + storage_dispatch + tap_motion + discrete_ops,
    }


def worst_buses_list(res: SnapshotResult, vmin: float, vmax: float, k: int = 5) -> List[Dict[str, Any]]:
    df = res.bus_df
    if df is None or df.empty or "violation" not in df.columns:
        return []
    viols = df[df["violation"] == True].copy()
    if viols.empty:
        return []
    vmin_arr = viols["vmin_pu"].fillna(1e9).to_numpy(dtype=float)
    vmax_arr = viols["vmax_pu"].fillna(-1e9).to_numpy(dtype=float)
    under = np.maximum(0.0, vmin - vmin_arr)
    over = np.maximum(0.0, vmax_arr - vmax)
    sev = under + over
    viols["sev"] = sev
    viols = viols.sort_values("sev", ascending=False).head(k)
    out = []
    for _, r in viols.iterrows():
        out.append({
            "bus": str(r.get("bus", "")),
            "vmin": float(r.get("vmin_pu")) if not pd.isna(r.get("vmin_pu")) else None,
            "vmax": float(r.get("vmax_pu")) if not pd.isna(r.get("vmax_pu")) else None,
            "sev": float(r.get("sev", 0.0)),
        })
    return out


def top_overloaded_lines(res: SnapshotResult, k: int = 5) -> List[Dict[str, Any]]:
    df = res.line_df
    if df is None or df.empty or "%norm" not in df.columns:
        return []
    d2 = df.dropna(subset=["%norm"]).copy()
    if d2.empty:
        return []
    d2 = d2.sort_values("%norm", ascending=False).head(k)
    out = []
    for _, r in d2.iterrows():
        out.append({
            "line": str(r.get("line", "")),
            "%norm": float(r.get("%norm")) if not pd.isna(r.get("%norm")) else None,
            "bus1": str(r.get("bus1", "")),
            "bus2": str(r.get("bus2", "")),
        })
    return out


def bus_minmax_pu(bus: str) -> Tuple[Optional[float], Optional[float]]:
    """
    Measured values from the *current* compiled/solved DSS state (no hallucinations).
    """
    try:
        dss.Circuit.SetActiveBus(bus)
        pu = dss.Bus.puVmagAngle()
        mags = _as_float_list(pu[0::2])
        if not mags:
            return None, None
        return float(np.min(mags)), float(np.max(mags))
    except Exception:
        return None, None


# =========================
# Merge commands (cumulative)
# =========================
RE_EDIT = re.compile(r"^\s*edit\s+([A-Za-z]+)\.([^\s]+)\s+.+$", re.I)
RE_SWITCH = re.compile(r"^\s*(open|close)\s+line\.([^\s]+)\s*$", re.I)
RE_NEW = re.compile(r"^\s*new\s+([A-Za-z]+)\.([^\s]+)\s+.+$", re.I)


def merge_state_cmds(state_cmds: List[str], new_cmds: List[str]) -> List[str]:
    latest = {}
    news = {}
    others = []

    def key_for(cmd: str) -> Optional[Tuple[str, str]]:
        m = RE_EDIT.match(cmd)
        if m:
            return ("edit", f"{m.group(1).lower()}.{m.group(2).lower()}")
        m = RE_SWITCH.match(cmd)
        if m:
            return ("sw", f"line.{m.group(2).lower()}")
        m = RE_NEW.match(cmd)
        if m:
            return ("new", f"{m.group(1).lower()}.{m.group(2).lower()}")
        return None

    for c in state_cmds:
        k = key_for(c)
        if k is None:
            others.append(c)
            continue
        typ, name = k
        if typ == "new":
            news[name] = c
        else:
            latest[(typ, name)] = c

    for c in new_cmds:
        k = key_for(c)
        if k is None:
            others.append(c)
            continue
        typ, name = k
        if typ == "new":
            news[name] = c
        else:
            latest[(typ, name)] = c

    merged = []
    merged += others
    merged += list(news.values())
    merged += list(latest.values())
    return merged


# =========================
# LLM client + parsing
# =========================
class LLMClient:
    def __init__(self, seed: Optional[int] = None):
        self.ollama_url = os.environ.get("OLLAMA_URL", "http://localhost:11434")
        self.model = os.environ.get("OLLAMA_MODEL", "llama3.1:latest")
        self.candidate_source = "LLM"
        self.actor_type = "llm"
        self.session = requests.Session()
        env_seed = os.environ.get("OLLAMA_SEED", "").strip()
        self.seed = int(env_seed) if seed is None and env_seed else seed
        self.call_index = 0
        self.seed_stream_indices: Dict[str, int] = {
            "planner": 0, "critic": 0, "explanation": 0,
        }
        self.call_records: List[Dict[str, Any]] = []

    def list_models(self) -> List[str]:
        try:
            out = subprocess.check_output(["ollama", "list"], text=True, stderr=subprocess.STDOUT, timeout=6)
            lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
            if lines and lines[0].lower().startswith("name"):
                lines = lines[1:]
            return [ln.split()[0] for ln in lines if ln.split()]
        except Exception:
            return []

    def chat(self, system: str, user_text: str, temperature: float, num_predict: int,
             timeout_s: int = 240, response_format: Optional[Any] = None) -> str:
        """Send a chat request, optionally asking Ollama for structured output.

        ``response_format="json"`` maps to Ollama's ``format`` request field. A
        dict may also be supplied for Ollama versions that accept a JSON schema.
        Older servers can reject the field, so a 400/422 response is retried once
        without it. Calls that do not request a format retain the old behavior.
        """
        url = f"{self.ollama_url.rstrip('/')}/api/chat"
        started = time.perf_counter()
        call_index = self.call_index
        if "Constraint Critic Agent" in system:
            seed_stream = "critic"
        elif "planning node" in system or "OPRO" in system:
            seed_stream = "planner"
        else:
            seed_stream = "explanation"
        stream_index = self.seed_stream_indices[seed_stream]
        self.seed_stream_indices[seed_stream] = stream_index + 1
        options = {"temperature": float(temperature), "num_predict": int(num_predict)}
        if self.seed is not None:
            # Independent streams ensure an ablation that adds a critic does
            # not silently change the later planner samples.  Stream offsets
            # are intentionally far apart and recorded with every call.
            stream_offset = {"planner": 0, "critic": 100_000, "explanation": 200_000}[seed_stream]
            options["seed"] = int(self.seed) + stream_offset + stream_index
        self.call_index += 1
        payload = {
            "model": self.model,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user_text}],
            "stream": False,
            "options": options,
        }
        if response_format is not None:
            payload["format"] = response_format
        r = self.session.post(url, json=payload, timeout=timeout_s)
        format_fallback = False
        if response_format is not None and r.status_code in {400, 422}:
            # ``format`` was introduced after the basic /api/chat contract. Keep
            # local installations on an older Ollama release usable.
            fallback_payload = dict(payload)
            fallback_payload.pop("format", None)
            r = self.session.post(url, json=fallback_payload, timeout=timeout_s)
            format_fallback = True
        if r.status_code != 200:
            content = f"(LLM error) HTTP {r.status_code}: {r.text[:300]}"
            self.call_records.append({
                "call_index": call_index,
                "seed_stream": seed_stream,
                "seed_stream_index": stream_index,
                "seed": options.get("seed"),
                "temperature": float(temperature),
                "num_predict": int(num_predict),
                "status_code": r.status_code,
                "format_fallback": format_fallback,
                "latency_ms": round((time.perf_counter() - started) * 1000.0, 1),
                "prompt_sha256": hashlib.sha256(user_text.encode("utf-8")).hexdigest(),
                "response_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            })
            return content
        data = r.json()
        content = data.get("message", {}).get("content", "").strip() or ""
        self.call_records.append({
            "call_index": call_index,
            "seed_stream": seed_stream,
            "seed_stream_index": stream_index,
            "seed": options.get("seed"),
            "temperature": float(temperature),
            "num_predict": int(num_predict),
            "status_code": r.status_code,
            "format_fallback": format_fallback,
            "latency_ms": round((time.perf_counter() - started) * 1000.0, 1),
            "prompt_eval_count": data.get("prompt_eval_count"),
            "eval_count": data.get("eval_count"),
            "total_duration_ns": data.get("total_duration"),
            "load_duration_ns": data.get("load_duration"),
            "prompt_sha256": hashlib.sha256(user_text.encode("utf-8")).hexdigest(),
            "response_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        })
        return content


def parse_llm_json(text: Any) -> Optional[Dict[str, Any]]:
    # Structured-output clients and mocked/test clients may return the decoded
    # object directly. Copy it so downstream normalization cannot mutate the
    # caller's response object.
    if isinstance(text, dict):
        return dict(text)
    if not isinstance(text, str):
        return None
    t = (text or "").strip()
    # allow <JSON> ... </JSON>
    m = re.search(r"<JSON>(.*?)</JSON>", t, flags=re.S | re.I)
    if m:
        t = m.group(1).strip()
    # allow ```json ... ```
    m2 = re.search(r"```json\s*(.*?)```", t, flags=re.S | re.I)
    if m2:
        t = m2.group(1).strip()
    # fallback: clip outermost { }
    if not t.startswith("{"):
        i = t.find("{")
        j = t.rfind("}")
        if i >= 0 and j > i:
            t = t[i:j+1]
    # quick trailing comma repair
    t = re.sub(r",\s*}", "}", t)
    t = re.sub(r",\s*]", "]", t)
    try:
        return json.loads(t)
    except Exception:
        return None


# =========================
# Actions: sanitize/normalize/dedup
# =========================
ALLOWED_TYPES = {
    "tap_step", "cap_state", "switch_line",
    "der_setpoint", "storage_setpoint", "storage_fleet_setpoint",
    "create_var_gen", "create_pv", "create_load"
}

TYPE_ALIASES = {
    # tap
    "tap": "tap_step",
    "xfmr_tap": "tap_step",
    "transformer_tap": "tap_step",
    "reg_tap": "tap_step",
    "tapchange": "tap_step",
    # cap
    "cap": "cap_state",
    "capacitor": "cap_state",
    "cap_switch": "cap_state",
    "cap_toggle": "cap_state",
    # switching
    "switch": "switch_line",
    "line_switch": "switch_line",
    # existing distributed energy resources
    "der": "der_setpoint",
    "set_der": "der_setpoint",
    "pv_setpoint": "der_setpoint",
    "generator_setpoint": "der_setpoint",
    # storage
    "storage": "storage_setpoint",
    "battery": "storage_setpoint",
    "bess": "storage_setpoint",
    "battery_setpoint": "storage_setpoint",
    "storage_fleet": "storage_fleet_setpoint",
    "battery_fleet": "storage_fleet_setpoint",
    # var gen
    "var_gen": "create_var_gen",
    "q_gen": "create_var_gen",
    "q_injection": "create_var_gen",
    "varonly_gen": "create_var_gen",
    "generator_var": "create_var_gen",
    # pv/load
    "pv": "create_pv",
    "pvsystem": "create_pv",
    "load": "create_load",
    "new_load": "create_load",
}

def _safe_int(x: Any, default: int = 0) -> int:
    try:
        if isinstance(x, bool):
            return int(x)
        if isinstance(x, (int, np.integer)):
            return int(x)
        if isinstance(x, float):
            return int(round(x))
        s = str(x).strip()
        return int(float(s))
    except Exception:
        return default


def _normalize_type(t: Any) -> str:
    s = str(t or "").strip().lower()
    if s in TYPE_ALIASES:
        s = TYPE_ALIASES[s]
    return s


def sanitize_actions(actions_any: Any) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    if not isinstance(actions_any, list):
        return out
    for a in actions_any:
        if isinstance(a, dict):
            out.append(a)
            continue
        if isinstance(a, str):
            s = a.strip()
            if s.startswith("{") and s.endswith("}"):
                try:
                    obj = json.loads(s)
                    if isinstance(obj, dict):
                        out.append(obj)
                except Exception:
                    pass
    # normalize per action
    normed: List[Dict[str, Any]] = []
    for a in out:
        aa = dict(a)
        aa["type"] = _normalize_type(aa.get("type", ""))
        normed.append(aa)
    return normed


def first_family(actions: List[Dict[str, Any]]) -> str:
    if not actions:
        return "none"
    return _normalize_type(actions[0].get("type", ""))


def _dedup_number(value: Any) -> Any:
    """Normalize numeric setpoints without collapsing distinct invalid values."""
    if value is None:
        return None
    try:
        number = float(value)
        if math.isfinite(number):
            return round(number, 9)
    except Exception:
        pass
    return str(value).strip().lower()


def _action_dedup_key(action: Dict[str, Any]) -> Tuple[Any, ...]:
    """Return the complete control identity used to de-duplicate candidates."""
    typ = _normalize_type(action.get("type", ""))
    if typ == "tap_step":
        return (typ, str(action.get("regcontrol", "")).lower(), _safe_int(action.get("step", 0), 0))
    if typ == "cap_state":
        return (typ, str(action.get("cap", "")).lower(), str(action.get("state", "")).strip())
    if typ == "switch_line":
        return (typ, str(action.get("op", "")).lower(), str(action.get("line", "")).lower())
    if typ == "der_setpoint":
        return (
            typ,
            str(action.get("device", "")).lower(),
            _dedup_number(action.get("kw")),
            _dedup_number(action.get("kvar")),
            _dedup_number(action.get("pct_pmpp")),
        )
    if typ == "storage_setpoint":
        return (
            typ,
            str(action.get("storage", "")).lower(),
            str(action.get("state", "")).strip().upper(),
            _dedup_number(action.get("pct_kw")),
            _dedup_number(action.get("kvar")),
        )
    if typ == "storage_fleet_setpoint":
        return (
            typ,
            str(action.get("fleet", "")).lower(),
            str(action.get("state", "")).strip().upper(),
            _dedup_number(action.get("pct_kw")),
            _dedup_number(action.get("kvar")),
        )
    if typ == "create_var_gen":
        return (
            typ, str(action.get("bus", "")).lower(), str(action.get("name", "")).lower(),
            _dedup_number(action.get("kvar")),
        )
    if typ == "create_pv":
        return (
            typ, str(action.get("bus", "")).lower(), str(action.get("name", "")).lower(),
            _dedup_number(action.get("phases")), _dedup_number(action.get("kva")),
            _dedup_number(action.get("pmpp")), _dedup_number(action.get("kvar")),
        )
    if typ == "create_load":
        return (
            typ, str(action.get("bus", "")).lower(), str(action.get("name", "")).lower(),
            _dedup_number(action.get("phases")), _dedup_number(action.get("kw")),
            _dedup_number(action.get("kvar")), _dedup_number(action.get("model")),
        )
    # Preserve every supplied field for unknown action types so malformed
    # candidates do not accidentally hide one another before validation.
    return (typ, json.dumps(action, sort_keys=True, separators=(",", ":"), default=str))


_ORDER_INDEPENDENT_SETPOINT_TYPES = {
    "tap_step", "cap_state", "der_setpoint", "storage_setpoint",
}


def _setpoint_target(action: Dict[str, Any]) -> str:
    """Return a stable target identity for commutative setpoint actions."""
    typ = _normalize_type(action.get("type", ""))
    field = {
        "tap_step": "regcontrol",
        "cap_state": "cap",
        "der_setpoint": "device",
        "storage_setpoint": "storage",
    }.get(typ)
    if not field:
        return ""
    value = str(action.get(field, "")).strip().lower()
    return f"{typ}:{value}" if value else ""


def candidate_bundle_fingerprint(actions_or_candidate: Any) -> str:
    """Hash a candidate bundle, ignoring order for distinct-target setpoints.

    Absolute/independent setpoints on different devices commute in OpenDSS, so
    an LLM cannot evade replay detection merely by reordering them. Ordered
    semantics are retained for repeated targets, switching, and create actions.
    """
    raw_actions = (
        actions_or_candidate.get("actions", [])
        if isinstance(actions_or_candidate, dict)
        else actions_or_candidate
    )
    actions = sanitize_actions(raw_actions)
    action_keys = [_action_dedup_key(action) for action in actions]
    targets = [_setpoint_target(action) for action in actions]
    commutative = bool(actions) and all(
        _normalize_type(action.get("type", "")) in _ORDER_INDEPENDENT_SETPOINT_TYPES
        for action in actions
    ) and all(targets) and len(set(targets)) == len(targets)
    if commutative:
        action_keys = sorted(
            action_keys,
            key=lambda item: json.dumps(item, sort_keys=True, separators=(",", ":"), default=str),
        )
    canonical = {
        "ordering": "distinct_target_set" if commutative else "sequence",
        "actions": action_keys,
    }
    encoded = json.dumps(
        canonical, sort_keys=True, separators=(",", ":"), default=str
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def operating_state_fingerprint(state_cmds: List[str]) -> str:
    """Identify the accepted operating point for replay filtering."""
    commands = [str(command).strip() for command in (state_cmds or []) if str(command).strip()]
    encoded = json.dumps(commands, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def evaluated_fingerprint_key(operating_state_id: str, bundle_fingerprint: str) -> str:
    return f"{operating_state_id}:{bundle_fingerprint}"


def filter_previously_evaluated_candidates(
    candidates: List[Dict[str, Any]],
    evaluated_fingerprints: Dict[str, Dict[str, Any]],
    operating_state_id: str,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Remove bundles already evaluated at this exact accepted operating point."""
    novel: List[Dict[str, Any]] = []
    repeated: List[Dict[str, Any]] = []
    known = evaluated_fingerprints or {}
    for candidate in candidates:
        actions = sanitize_actions(candidate.get("actions", []))
        if not actions:
            continue
        fingerprint = candidate_bundle_fingerprint(actions)
        item = dict(candidate)
        item["actions"] = actions
        item["fingerprint"] = fingerprint
        key = evaluated_fingerprint_key(operating_state_id, fingerprint)
        if key in known:
            repeated.append(item)
        else:
            novel.append(item)
    return novel, repeated


def dedup_candidates(cands: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    out = []
    for c in cands:
        acts = sanitize_actions(c.get("actions", []))
        if not acts:
            continue
        # Every action and value participates. Distinct-target setpoints are
        # canonicalized as a set because their execution order is immaterial.
        key = candidate_bundle_fingerprint(acts)
        if key in seen:
            continue
        seen.add(key)
        cc = dict(c)
        cc["actions"] = acts
        cc["fingerprint"] = key
        out.append(cc)
    return out


def pick_diverse_subset(cands: List[Dict[str, Any]], k: int) -> List[Dict[str, Any]]:
    buckets: Dict[str, List[Dict[str, Any]]] = {}
    for c in cands:
        acts = sanitize_actions(c.get("actions", []))
        fam = first_family(acts)
        buckets.setdefault(fam, []).append(c)

    out: List[Dict[str, Any]] = []
    families = sorted(buckets.keys())
    idx = {f: 0 for f in families}
    while len(out) < k and families:
        progressed = False
        for f in families:
            if len(out) >= k:
                break
            j = idx[f]
            if j < len(buckets[f]):
                out.append(buckets[f][j])
                idx[f] = j + 1
                progressed = True
        if not progressed:
            break
    return out[:k]


def repair_candidate_buses(cands: List[Dict[str, Any]], worst_list: List[Dict[str, Any]]):
    valid_buses = [w.get("bus") for w in worst_list if w.get("bus")]
    fallback = valid_buses[0] if valid_buses else None
    if not fallback:
        return cands

    for c in cands:
        acts = sanitize_actions(c.get("actions", []))
        for a in acts:
            t = _normalize_type(a.get("type", ""))
            if t in ("create_var_gen", "create_pv", "create_load"):
                b = str(a.get("bus", "")).strip()
                if (not b) or (not safe_bus_exists(b)):
                    a["bus"] = fallback
        c["actions"] = acts
    return cands


def prioritize_names_for_buses(names: List[str], worst_list: List[Dict[str, Any]]) -> List[str]:
    """Put controls whose canonical names reference a measured worst bus first."""
    tokens = [str(item.get("bus", "")).lower() for item in worst_list if item.get("bus")]
    indexed = list(enumerate(names))

    def rank(item: Tuple[int, str]) -> Tuple[int, int]:
        index, name = item
        lowered = str(name).lower()
        if any(
            lowered in {token, f"pv_load_{token}", f"storage_{token}", f"storage_load_{token}"}
            for token in tokens
        ):
            return 0, index
        if any(token and token in lowered for token in tokens):
            return 1, index
        return 2, index

    return [name for _index, name in sorted(indexed, key=rank)]


# =========================
# Translator
# =========================
class ActionTranslator:
    def __init__(self):
        self.pv_idx = 1
        self.load_idx = 1
        self.var_idx = 1

    def next_pv_name(self) -> str:
        n = f"AUTOPV{self.pv_idx}"
        self.pv_idx += 1
        return n

    def next_load_name(self) -> str:
        n = f"AUTOLOAD{self.load_idx}"
        self.load_idx += 1
        return n

    def next_vargen_name(self) -> str:
        n = f"VARGEN{self.var_idx}"
        self.var_idx += 1
        return n

    def actions_to_cmds(
        self,
        res: SnapshotResult,
        actions_any: Any,
        allow_switch: bool,
        allow_pv: bool,
        allow_load: bool,
        allow_var_gen: bool,
        max_actions: int,
    ) -> Tuple[List[str], List[str]]:
        notes: List[str] = []
        cmds: List[str] = []

        actions = sanitize_actions(actions_any)[:max_actions]
        if not actions:
            return [], ["no_valid_actions"]

        lines_exist = set([x.lower() for x in (res.devices.get("lines") or [])])

        for a in actions:
            typ = _normalize_type(a.get("type", ""))

            if typ not in ALLOWED_TYPES:
                notes.append(f"unknown_action:{typ}")
                continue

            if typ == "tap_step":
                reg = str(a.get("regcontrol", "")).strip()
                step = _safe_int(a.get("step", 1), default=1)
                step = max(-4, min(4, step))

                rm = res.reg_map.get(reg, {})
                xf = rm.get("xfmr", None)
                wdg = int(rm.get("wdg", 1) or 1)
                inc = float(rm.get("tap_inc", 0.00625) or 0.00625)
                cur = rm.get("tap", None)

                if xf is None:
                    notes.append(f"tap_blocked_no_xfmr:{reg}")
                    continue
                if cur is None:
                    cur = 1.0
                new_tap = float(cur + step * inc)
                new_tap = max(0.90, min(1.10, new_tap))
                cmds.append(f"Edit Transformer.{xf} wdg={wdg} tap={new_tap:.6f}")
                continue

            if typ == "cap_state":
                cap = str(a.get("cap", "")).strip()
                state = str(a.get("state", "(1)")).strip()
                if state not in ("(0)", "(1)"):
                    state = "(1)"
                cmds.append(f"Edit Capacitor.{cap} states={state}")
                continue

            if typ == "switch_line":
                if not allow_switch:
                    notes.append("switch_blocked")
                    continue
                op = str(a.get("op", "")).strip().lower()
                line = str(a.get("line", "")).strip()
                if op not in ("open", "close"):
                    notes.append(f"bad_switch_op:{op}")
                    continue
                if line.lower() not in lines_exist:
                    notes.append(f"bad_line:{line}")
                    continue
                prior_status = str(res.line_status.get(line.lower(), "unknown"))
                if op == "close" and prior_status == "disabled":
                    # SMART-DS represents normally-open boundary ties as
                    # disabled switch lines. Enabling such a line closes its
                    # default terminal state; a bare Close command is a no-op.
                    cmds.append(f"Edit Line.{line} enabled=yes")
                else:
                    cmds.append(f"{op.capitalize()} Line.{line}")
                continue

            if typ == "der_setpoint":
                device = str(a.get("device", "")).strip()
                if "." not in device:
                    notes.append(f"bad_der:{device}")
                    continue
                cls, name = device.split(".", 1)
                cls_norm = cls.lower()
                if cls_norm == "pvsystem":
                    exists = name in (res.devices.get("pvsystems") or [])
                    target = f"PVSystem.{name}"
                elif cls_norm == "generator":
                    exists = name in (res.devices.get("generators") or [])
                    target = f"Generator.{name}"
                else:
                    exists = False
                    target = device
                if not exists:
                    notes.append(f"bad_der:{device}")
                    continue
                settings = []
                if cls_norm == "generator" and a.get("kw") is not None:
                    settings.append(f"kW={float(a['kw']):.3f}")
                if cls_norm == "pvsystem" and a.get("pct_pmpp") is not None:
                    settings.append(f"%Pmpp={float(a['pct_pmpp']):.3f}")
                if a.get("kvar") is not None:
                    settings.append(f"kvar={float(a['kvar']):.3f}")
                if not settings:
                    notes.append(f"empty_der_setpoint:{device}")
                    continue
                cmds.append(f"Edit {target} {' '.join(settings)}")
                continue

            if typ == "storage_setpoint":
                name = str(a.get("storage", "")).strip()
                if name not in (res.devices.get("storages") or []):
                    notes.append(f"bad_storage:{name}")
                    continue
                state_name = str(a.get("state", "IDLING")).strip().upper()
                if state_name not in ("CHARGING", "DISCHARGING", "IDLING"):
                    notes.append(f"bad_storage_state:{state_name}")
                    continue
                settings = ["DispMode=EXTERNAL", f"State={state_name}"]
                if state_name != "IDLING":
                    pct_kw = max(0.0, min(100.0, float(a.get("pct_kw", 50.0))))
                    prop = "%Charge" if state_name == "CHARGING" else "%Discharge"
                    settings.append(f"{prop}={pct_kw:.3f}")
                if a.get("kvar") is not None:
                    settings.append(f"kvar={float(a['kvar']):.3f}")
                cmds.append(f"Edit Storage.{name} {' '.join(settings)}")
                continue

            if typ == "create_var_gen":
                if not allow_var_gen:
                    notes.append("var_gen_blocked")
                    continue
                bus = str(a.get("bus", "")).strip()
                kvar = float(a.get("kvar", 0.0) or 0.0)
                kvar = max(-1500.0, min(1500.0, kvar))
                if not bus or not safe_bus_exists(bus):
                    notes.append(f"bad_bus:{bus}")
                    continue
                name = str(a.get("name", "")).strip() or self.next_vargen_name()
                kv, ph = bus_kv_infer(bus)
                cmds.append(f"New Generator.{name} bus1={bus} phases={ph} kV={kv:.4f} kW=0 kvar={kvar:.3f} model=1")
                continue

            if typ == "create_pv":
                if not allow_pv:
                    notes.append("pv_blocked")
                    continue
                bus = str(a.get("bus", "")).strip()
                if not bus or not safe_bus_exists(bus):
                    notes.append(f"bad_bus:{bus}")
                    continue
                name = str(a.get("name", "")).strip() or self.next_pv_name()
                kva = float(a.get("kva", 800.0) or 800.0)
                pmpp = float(a.get("pmpp", 600.0) or 600.0)
                kvar = float(a.get("kvar", 0.0) or 0.0)
                kva = max(10.0, min(8000.0, kva))
                pmpp = max(1.0, min(kva, pmpp))
                kvar = max(-5000.0, min(5000.0, kvar))
                kv, ph = bus_kv_infer(bus)
                cmds.append(f"New PVSystem.{name} bus1={bus} phases={ph} kV={kv:.4f} kVA={kva:.3f} Pmpp={pmpp:.3f} kvar={kvar:.3f}")
                continue

            if typ == "create_load":
                if not allow_load:
                    notes.append("load_blocked")
                    continue
                bus = str(a.get("bus", "")).strip()
                if not bus or not safe_bus_exists(bus):
                    notes.append(f"bad_bus:{bus}")
                    continue
                name = str(a.get("name", "")).strip() or self.next_load_name()
                kw = float(a.get("kw", 400.0) or 400.0)
                kvar = float(a.get("kvar", 150.0) or 150.0)
                kw = max(0.0, min(15000.0, kw))
                kvar = max(-10000.0, min(10000.0, kvar))
                kv, ph = bus_kv_infer(bus)
                cmds.append(f"New Load.{name} bus1={bus} phases={ph} conn=wye model=1 kV={kv:.4f} kW={kw:.3f} kvar={kvar:.3f}")
                continue

        for c in cmds:
            if re.search(r"\bedit\s+vsource\.", c, flags=re.I):
                raise RuntimeError("Blocked: Edit Vsource.* is not allowed.")
        return cmds, notes


# =========================
# Physics pool (guardrail fallback)
# =========================
def _base_bus_name(value: Any) -> str:
    """Strip OpenDSS node suffixes while preserving the canonical bus token."""
    return str(value or "").strip().split(".", 1)[0].lower()


def _catalog_pvs_at_buses(
    pv_names: List[str], bus_items: List[Tuple[str, str]]
) -> List[Tuple[str, str, str]]:
    """Resolve bus targets to existing PV names; never synthesize a device name."""
    # Index every exact name and delimiter-bounded suffix once.  SMART-DS has
    # tens of thousands of PVs, so rescanning the full catalog for each target
    # bus made planner preparation scale as targets x devices.  Lists retain
    # catalog order, preserving the former first-catalog-match behavior.
    by_bus_key: Dict[str, List[str]] = {}
    for raw_name in pv_names:
        original = str(raw_name)
        lowered = original.lower()
        keys = {lowered}
        for delimiter in ("_", "-"):
            start = 0
            while True:
                position = lowered.find(delimiter, start)
                if position < 0:
                    break
                suffix = lowered[position + 1:]
                if suffix:
                    keys.add(suffix)
                start = position + 1
        for key in keys:
            by_bus_key.setdefault(key, []).append(original)

    selected: List[Tuple[str, str, str]] = []
    used: set[str] = set()
    for bus_value, role in bus_items:
        bus = _base_bus_name(bus_value)
        if not bus:
            continue
        for name in by_bus_key.get(bus, []):
            lowered = name.lower()
            if lowered not in used:
                selected.append((name, bus, role))
                used.add(lowered)
                break
    return selected


def exact_evidence_pv_seed_candidates(
    res: SnapshotResult,
    vmin: float,
    vmax: float,
    max_actions: int,
) -> List[Dict[str, Any]]:
    """Build reproducible SMART-DS PV seeds from the current solved snapshot.

    The mapping deliberately requires the exact catalog name ``pv_load_<bus>``.
    Voltage targets are ordered by measured violation severity and take precedence
    over overloaded-line endpoints when a PV appears in both sets. The action
    budget is applied only after each evidence scope has been assembled and
    de-duplicated, matching the independently measured portfolio study.
    """
    action_budget = max(0, int(max_actions))
    if action_budget < 2:
        return []

    pv_lookup = {
        str(name).lower(): str(name)
        for name in (res.devices.get("pvsystems") or [])
    }
    if not pv_lookup:
        return []

    bus_count = len(res.bus_df) if res.bus_df is not None else 0
    ranked_buses = worst_buses_list(res, vmin, vmax, k=max(1, bus_count))
    voltage_targets: List[Tuple[str, str, float]] = []
    for item in ranked_buses:
        bus = _base_bus_name(item.get("bus"))
        pv = pv_lookup.get(f"pv_load_{bus}")
        if not pv:
            continue
        vmin_value = item.get("vmin")
        vmax_value = item.get("vmax")
        under = (
            max(0.0, float(vmin) - float(vmin_value))
            if vmin_value is not None and not pd.isna(vmin_value)
            else 0.0
        )
        over = (
            max(0.0, float(vmax_value) - float(vmax))
            if vmax_value is not None and not pd.isna(vmax_value)
            else 0.0
        )
        voltage_targets.append((pv, bus, 0.0 if over >= under else 100.0))

    overloaded_count = 0
    if res.line_df is not None and "%norm" in res.line_df.columns:
        overloaded_count = int((res.line_df["%norm"] > 100.0).sum())
    ranked_lines = (
        top_overloaded_lines(res, k=overloaded_count)
        if overloaded_count > 0
        else []
    )
    thermal_targets: List[Tuple[str, str, float]] = []
    seen_thermal: set[str] = set()
    for item in ranked_lines:
        loading = item.get("%norm")
        if loading is None or float(loading) <= 100.0:
            continue
        for endpoint in ("bus1", "bus2"):
            bus = _base_bus_name(item.get(endpoint))
            pv = pv_lookup.get(f"pv_load_{bus}")
            if not pv or pv.lower() in seen_thermal:
                continue
            seen_thermal.add(pv.lower())
            thermal_targets.append((pv, bus, 75.0))

    def build_seed(
        label: str,
        selected_voltage: List[Tuple[str, str, float]],
        selected_thermal: List[Tuple[str, str, float]],
    ) -> Optional[Dict[str, Any]]:
        union: List[Tuple[str, str, float, str]] = []
        used: set[str] = set()
        for role, targets in (
            ("voltage", selected_voltage),
            ("thermal_endpoint", selected_thermal),
        ):
            for pv, bus, pct_pmpp in targets:
                lowered = pv.lower()
                if lowered in used:
                    continue
                used.add(lowered)
                union.append((pv, bus, pct_pmpp, role))

        # Truncate only after the voltage-first exact-name union is complete.
        applied = union[:action_budget]
        if len(applied) < 2:
            return None
        voltage_count = sum(role == "voltage" for _, _, _, role in applied)
        thermal_count = sum(role == "thermal_endpoint" for _, _, _, role in applied)
        thermal_setpoints = sorted({
            pct_pmpp
            for _, _, pct_pmpp, role in applied
            if role == "thermal_endpoint"
        })
        actions = [
            {
                "type": "der_setpoint",
                "device": f"PVSystem.{pv}",
                "pct_pmpp": pct_pmpp,
            }
            for pv, _bus, pct_pmpp, _role in applied
        ]
        return {
            "name": f"PHY_pv_{label}_{len(actions)}",
            "source": "PHYS_SEED",
            "actions": actions,
            "reasoning": (
                "Current-snapshot, exact-catalog physics seed with voltage-first de-duplication: "
                f"{voltage_count} violation-bus PV controls and {thermal_count} additional "
                f"overloaded-line endpoint PV controls at %Pmpp={thermal_setpoints}; "
                "every action is independently screened "
                "by OpenDSS and the GridGuard certificate gates."
            ),
        }

    aggressive_thermal_targets = [
        (pv, bus, 0.0) for pv, bus, _pct_pmpp in thermal_targets
    ]
    scopes = (
        ("exact_all_matching_aggressive", voltage_targets, aggressive_thermal_targets),
        ("exact_top1000_plus_thermal25", voltage_targets[:1000], thermal_targets[:25]),
    )
    seeds = [build_seed(label, voltage, thermal) for label, voltage, thermal in scopes]
    return dedup_candidates([seed for seed in seeds if seed is not None])


def pv_portfolio_candidates(
    res: SnapshotResult,
    vmin: float,
    vmax: float,
    max_actions: int,
) -> List[Dict[str, Any]]:
    """Build deterministic multi-PV bundles grounded in measured problem locations.

    The portfolio interleaves PVs at several worst-voltage buses and endpoints of
    the most overloaded lines.  Every referenced device is resolved from the
    OpenDSS discovery catalog; a missing bus/device match is skipped.
    """
    action_budget = max(0, int(max_actions))
    if action_budget < 2:
        return []

    evidence_seeds = exact_evidence_pv_seed_candidates(
        res, vmin, vmax, action_budget
    )

    worst = worst_buses_list(res, vmin, vmax, k=max(5, action_budget))
    top_lines = top_overloaded_lines(res, k=max(5, action_budget))
    worst_bus_items = [(str(item.get("bus", "")), "voltage") for item in worst]
    line_bus_items: List[Tuple[str, str]] = []
    for item in top_lines:
        line_bus_items.extend([
            (str(item.get("bus1", "")), "thermal"),
            (str(item.get("bus2", "")), "thermal"),
        ])

    pv_catalog = list(res.devices.get("pvsystems") or [])
    voltage_targets = _catalog_pvs_at_buses(pv_catalog, worst_bus_items)
    thermal_targets = _catalog_pvs_at_buses(pv_catalog, line_bus_items)
    if not voltage_targets and not thermal_targets:
        return evidence_seeds

    # Interleave security axes so a small max_actions budget still represents
    # voltage and thermal evidence when both are available.
    selected: List[Tuple[str, str, str]] = []
    used: set[str] = set()
    for index in range(max(len(voltage_targets), len(thermal_targets))):
        for group in (voltage_targets, thermal_targets):
            if index >= len(group):
                continue
            item = group[index]
            if item[0].lower() in used:
                continue
            selected.append(item)
            used.add(item[0].lower())
            if len(selected) >= action_budget:
                break
        if len(selected) >= action_budget:
            break
    if len(selected) < 2:
        return []

    worst_by_bus = {_base_bus_name(item.get("bus")): item for item in worst}
    profiles = (
        ("balanced", 50.0, 90.0),
        ("strong", 0.0, 75.0),
        ("conservative", 75.0, 95.0),
    )
    candidates: List[Dict[str, Any]] = []
    for label, overvoltage_pct, thermal_pct in profiles:
        actions: List[Dict[str, Any]] = []
        voltage_count = 0
        thermal_count = 0
        for pv, bus, role in selected:
            if role == "voltage":
                voltage_count += 1
                bus_record = worst_by_bus.get(bus, {})
                is_overvoltage = float(bus_record.get("vmax") or 0.0) > vmax
                # Curtail for overvoltage; release curtailment for undervoltage.
                pct_pmpp = overvoltage_pct if is_overvoltage else 100.0
            else:
                thermal_count += 1
                pct_pmpp = thermal_pct
            actions.append({
                "type": "der_setpoint",
                "device": f"PVSystem.{pv}",
                "pct_pmpp": pct_pmpp,
            })
        candidates.append({
            "name": f"PHY_pv_portfolio_{label}_{len(actions)}",
            "source": "PHYS",
            "actions": actions,
            "reasoning": (
                f"Catalog-grounded coordinated PV portfolio: {voltage_count} voltage-target and "
                f"{thermal_count} overloaded-line endpoint controls, jointly screened by OpenDSS."
            ),
        })
    return dedup_candidates(evidence_seeds + candidates)


def physics_candidates(res: SnapshotResult, vmin: float, vmax: float,
                       allow_var_gen: bool, allow_pv: bool, allow_load: bool,
                       max_actions: int) -> List[Dict[str, Any]]:
    worst_list = worst_buses_list(res, vmin, vmax, k=max(5, int(max_actions)))
    worst_bus = worst_list[0]["bus"] if worst_list else "none"

    regs = (res.devices.get("regcontrols") or [])[:10]
    caps = (res.devices.get("capacitors") or [])[:10]

    cands = []
    for r in regs:
        if res.reg_map.get(r, {}).get("xfmr") is None:
            continue
        for s in (-2, -1, +1, +2):
            cands.append({
                "name": f"PHY_tap_{r}_{s:+d}",
                "source": "PHYS",
                "actions": [{"type": "tap_step", "regcontrol": r, "step": s}][:max_actions],
                "reasoning": "Transformer ratio changes downstream voltage magnitude; test both directions near the current point."
            })

    for c in caps:
        cands.append({"name": f"PHY_cap_{c}_on", "source": "PHYS",
                      "actions": [{"type": "cap_state", "cap": c, "state": "(1)"}][:max_actions],
                      "reasoning": "Capacitor injects VARs; can reduce undervoltage locally."})
        cands.append({"name": f"PHY_cap_{c}_off", "source": "PHYS",
                      "actions": [{"type": "cap_state", "cap": c, "state": "(0)"}][:max_actions],
                      "reasoning": "Turning off VAR injection can reduce overvoltage in lightly loaded areas."})

    # Multi-action portfolios come first within the DER family, ahead of the
    # original single-device probes. This preserves the low-cost guardrails but
    # gives larger SMART-DS runs a coordinated fallback when max_actions > 1.
    cands.extend(pv_portfolio_candidates(res, vmin, vmax, max_actions))
    ranked_pvs = prioritize_names_for_buses(res.devices.get("pvsystems") or [], worst_list)
    for pv in ranked_pvs[:10]:
        for pct_pmpp in (50.0, 75.0, 90.0):
            cands.append({
                "name": f"PHY_pv_{pv}_{pct_pmpp:.0f}pct", "source": "PHYS",
                "actions": [{
                    "type": "der_setpoint", "device": f"PVSystem.{pv}",
                    "pct_pmpp": pct_pmpp,
                }][:max_actions],
                "reasoning": "Test bounded real-power curtailment on an existing PV at a measured worst bus.",
            })

    ranked_storages = prioritize_names_for_buses(res.devices.get("storages") or [], worst_list)
    overvoltage = bool(worst_list and float(worst_list[0].get("vmax") or 0.0) > vmax)
    storage_state = "CHARGING" if overvoltage else "DISCHARGING"
    for storage in ranked_storages[:10]:
        for pct_kw in (50.0, 100.0):
            cands.append({
                "name": f"PHY_storage_{storage}_{storage_state.lower()}_{pct_kw:.0f}",
                "source": "PHYS",
                "actions": [{
                    "type": "storage_setpoint", "storage": storage,
                    "state": storage_state, "pct_kw": pct_kw,
                }][:max_actions],
                "reasoning": (
                    "Charge near an overvoltage bus to absorb real power."
                    if overvoltage
                    else "Discharge near an undervoltage bus to supply local real power."
                ),
            })

    for generator in (res.devices.get("generators") or [])[:10]:
        for kvar in (-300.0, 0.0, 300.0):
            cands.append({
                "name": f"PHY_gen_{generator}_{kvar:+.0f}", "source": "PHYS",
                "actions": [{"type": "der_setpoint", "device": f"Generator.{generator}", "kvar": kvar}][:max_actions],
                "reasoning": "Test a bounded reactive-power setpoint on an existing generator.",
            })

    if allow_var_gen and worst_bus != "none":
        for kvar in (+200.0, +300.0, +400.0, -200.0, -300.0, -400.0):
            cands.append({"name": f"PHY_varGen_{kvar:+.0f}", "source": "PHYS",
                          "actions": [{"type": "create_var_gen", "bus": worst_bus, "kvar": kvar}][:max_actions],
                          "reasoning": "Local Q injection/absorption shifts voltage via Q-V sensitivity."})

    if allow_pv and worst_bus != "none":
        cands.append({"name": "PHY_addPV", "source": "PHYS",
                      "actions": [{"type": "create_pv", "bus": worst_bus, "kva": 1200, "pmpp": 900, "kvar": 0.0}][:max_actions],
                      "reasoning": "Local P support can reduce upstream drop (network-dependent)."})

    if allow_load and worst_bus != "none":
        cands.append({"name": "PHY_addLoad", "source": "PHYS",
                      "actions": [{"type": "create_load", "bus": worst_bus, "kw": 800, "kvar": 200}][:max_actions],
                      "reasoning": "Adding local absorption can pull voltage down (useful if overvoltage dominates)."})

    return cands[:80]


def restoration_seed_candidates(
    res: SnapshotResult,
    config: "GridGuardConfig",
) -> List[Dict[str, Any]]:
    """Generate blind-tie and one coarse fleet-response probe.

    The initial portfolio deliberately does not contain a hand-tuned passing
    setpoint. If these probes fail, the repair node can infer a new setpoint
    from their independently simulated watch-line responses.
    """
    if config.max_actions < 1 or not config.restoration_ties:
        return []
    line_lookup = {str(name).lower(): str(name) for name in res.devices.get("lines", [])}
    candidates: List[Dict[str, Any]] = []
    for configured_tie in config.restoration_ties:
        tie = line_lookup.get(str(configured_tie).lower())
        if tie is None:
            continue
        candidates.append({
            "name": f"RESTORE_blind_{tie}"[:80],
            "source": "RESTORE_SEED",
            "actions": [{"type": "switch_line", "line": tie, "op": "close"}],
            "reasoning": "Screen topology-only service restoration before commit.",
        })
        if config.max_actions < 2:
            continue
        for fleet_id in config.storage_fleets:
            pct_kw = float(config.restoration_probe_pct_kw)
            candidates.append({
                "name": f"RESTORE_PROBE_{tie}_{fleet_id}_charge{pct_kw:g}"[:80],
                "source": "RESTORE_PROBE",
                "actions": [
                    {"type": "switch_line", "line": tie, "op": "close"},
                    {
                        "type": "storage_fleet_setpoint", "fleet": fleet_id,
                        "state": "CHARGING", "pct_kw": pct_kw,
                    },
                ],
                "reasoning": "Measure a coarse tie-pickup versus fleet-charging response.",
            })
    return dedup_candidates(candidates)


def _line_loading_evidence(
    trial: SnapshotResult,
    reference: SnapshotResult,
    watched_lines: List[str],
) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Return exact, bounded watch-line measurements for a candidate solve."""
    trial_lookup: Dict[str, Tuple[str, float]] = {}
    reference_lookup: Dict[str, Tuple[str, float]] = {}
    for frame, target in (
        (trial.line_df, trial_lookup),
        (reference.line_df, reference_lookup),
    ):
        if frame is None or frame.empty:
            continue
        for _, row in frame.iterrows():
            name = str(row.get("line", ""))
            loading = row.get("%norm")
            if name and _finite_number(loading):
                target[name.lower()] = (name, float(loading))

    evidence: List[Dict[str, Any]] = []
    missing: List[str] = []
    for configured in list(dict.fromkeys(str(name) for name in watched_lines))[:20]:
        key = configured.lower()
        trial_value = trial_lookup.get(key)
        reference_value = reference_lookup.get(key)
        if trial_value is None or reference_value is None:
            missing.append(configured)
            continue
        evidence.append({
            "line": trial_value[0],
            "loading_pct": trial_value[1],
            "reference_loading_pct": reference_value[1],
        })
    return evidence, missing


def _restoration_response_point(
    record: Dict[str, Any],
    tie: str,
    fleet_id: str,
) -> Optional[float]:
    """Extract one exact tie-plus-fleet charging response coordinate."""
    raw_actions = record.get("supervisory_actions")
    if raw_actions is None:
        raw_actions = record.get("actions", [])
    actions = sanitize_actions(raw_actions)
    switches = [
        action for action in actions
        if _normalize_type(action.get("type")) == "switch_line"
    ]
    fleet_actions = [
        action for action in actions
        if _normalize_type(action.get("type")) == "storage_fleet_setpoint"
    ]
    if len(switches) != 1 or len(actions) not in {1, 2}:
        return None
    switch = switches[0]
    if (
        str(switch.get("line", "")).lower() != tie.lower()
        or str(switch.get("op", "")).strip().lower() != "close"
    ):
        return None
    if len(actions) == 1:
        return 0.0
    if len(fleet_actions) != 1:
        return None
    fleet_action = fleet_actions[0]
    if (
        str(fleet_action.get("fleet", "")).lower() != fleet_id.lower()
        or str(fleet_action.get("state", "")).strip().upper() != "CHARGING"
        or not _finite_number(fleet_action.get("pct_kw"))
    ):
        return None
    pct_kw = float(fleet_action["pct_kw"])
    return pct_kw if 0.0 <= pct_kw <= 100.0 else None


def derive_restoration_secant_candidates(
    recent_evals: List[Dict[str, Any]],
    config: "GridGuardConfig",
    operating_state_id: str,
) -> List[Dict[str, Any]]:
    """Derive bounded fleet repairs from prior same-state OpenDSS responses.

    The helper performs no simulation. It requires two or more converged,
    one-dimensional response points with a finite negative slope and returns
    at most one normally budgeted proposal per configured tie/fleet pair.
    """
    if (
        config.max_actions < 2
        or not config.restoration_ties
        or not config.storage_fleets
        or not config.restoration_watch_lines
    ):
        return []
    target_loading = float(config.restoration_target_loading_pct)
    quantum = 0.1
    min_slope = 0.05
    max_extrapolation = 30.0
    candidates: List[Dict[str, Any]] = []

    for tie in config.restoration_ties:
        for fleet_id in config.storage_fleets:
            points_by_line: Dict[str, Dict[float, Dict[str, Any]]] = {
                str(line).lower(): {} for line in config.restoration_watch_lines
            }
            canonical_line_names = {
                str(line).lower(): str(line) for line in config.restoration_watch_lines
            }
            evaluated_pct: set[float] = set()
            for record in recent_evals:
                if not isinstance(record, dict) or not record.get("simulated"):
                    continue
                if str(record.get("operating_state_id", "")) != str(operating_state_id):
                    continue
                metrics = record.get("metrics") or {}
                if not bool(metrics.get("converged", False)):
                    continue
                pct_kw = _restoration_response_point(record, str(tie), str(fleet_id))
                if pct_kw is None:
                    continue
                evaluated_pct.add(round(float(pct_kw), 9))
                for item in record.get("line_loading_evidence", []) or []:
                    if not isinstance(item, dict):
                        continue
                    key = str(item.get("line", "")).lower()
                    loading = item.get("loading_pct")
                    if key in points_by_line and _finite_number(loading):
                        canonical_line_names[key] = str(item.get("line"))
                        points_by_line[key][round(float(pct_kw), 9)] = {
                            "pct_kw": float(pct_kw),
                            "loading_pct": float(loading),
                            "candidate": str(record.get("name", "candidate"))[:80],
                            "fingerprint": str(record.get("fingerprint", ""))[:80],
                        }

            predictions: List[Dict[str, Any]] = []
            for line_key, point_map in points_by_line.items():
                points = sorted(point_map.values(), key=lambda item: item["pct_kw"])
                if len(points) < 2:
                    continue
                valid_pairs: List[Tuple[float, float, Dict[str, Any], Dict[str, Any]]] = []
                for left_index in range(len(points) - 1):
                    for right_index in range(left_index + 1, len(points)):
                        left = points[left_index]
                        right = points[right_index]
                        dx = right["pct_kw"] - left["pct_kw"]
                        if dx <= 0.0:
                            continue
                        slope = (right["loading_pct"] - left["loading_pct"]) / dx
                        if not math.isfinite(slope) or slope >= -min_slope:
                            continue
                        predicted = left["pct_kw"] + (
                            target_loading - left["loading_pct"]
                        ) / slope
                        if math.isfinite(predicted):
                            pair_rank = max(
                                abs(left["loading_pct"] - target_loading),
                                abs(right["loading_pct"] - target_loading),
                            )
                            valid_pairs.append((pair_rank, predicted, left, right))
                if not valid_pairs:
                    continue
                _, predicted, left, right = min(valid_pairs, key=lambda item: item[0])
                predictions.append({
                    "line": canonical_line_names[line_key],
                    "predicted_pct_kw": float(predicted),
                    "slope_loading_per_pct_kw": (
                        right["loading_pct"] - left["loading_pct"]
                    ) / (right["pct_kw"] - left["pct_kw"]),
                    "points": [left, right],
                })

            if not predictions:
                continue
            raw_pct = max(item["predicted_pct_kw"] for item in predictions)
            max_observed = max(evaluated_pct)
            upper = min(100.0, max_observed + max_extrapolation)
            clipped_pct = min(upper, max(0.0, raw_pct))
            # The required negative response means greater charging lowers the
            # watched loading, so one-sided upward rounding preserves margin.
            proposed_pct = min(
                100.0, math.ceil((clipped_pct - 1e-12) / quantum) * quantum
            )
            proposed_pct = round(proposed_pct, 1)
            if any(abs(proposed_pct - value) < quantum / 2.0 for value in evaluated_pct):
                if proposed_pct + quantum <= upper + 1e-12:
                    proposed_pct = round(proposed_pct + quantum, 1)
                else:
                    continue
            if not 0.0 < proposed_pct <= 100.0:
                continue
            derivation = {
                "method": "secant_watch_line_repair",
                "operating_state_id": str(operating_state_id),
                "watch_line_target_pct": target_loading,
                "proposed_pct_kw": proposed_pct,
                "raw_secant_pct_kw": raw_pct,
                "extrapolation_clipped": abs(clipped_pct - raw_pct) > 1e-9,
                "constraints": predictions,
            }
            repair_tag = hashlib.sha256(
                f"{tie}|{fleet_id}".lower().encode("utf-8")
            ).hexdigest()[:8]
            pct_tag = f"{proposed_pct:g}".replace(".", "p")
            candidates.append({
                "name": f"RESTORE_REPAIR_secant_charge{pct_tag}pct_{repair_tag}",
                "source": "PHYS_REPAIR",
                "actions": [
                    {"type": "switch_line", "line": str(tie), "op": "close"},
                    {
                        "type": "storage_fleet_setpoint", "fleet": str(fleet_id),
                        "state": "CHARGING", "pct_kw": proposed_pct,
                    },
                ],
                "reasoning": (
                    f"Secant repair targets {target_loading:g}% on monitored line evidence."
                ),
                "repair_derivation": derivation,
            })
    return dedup_candidates(candidates)


# =========================
# OPRO meta-prompt builder
# =========================
_PROMPT_METRIC_FIELDS = (
    "converged", "viol_buses", "v_severity", "over_lines", "max_line_pct",
    "thermal_severity_pct_sum", "line_loading_p95_pct",
    "losses_kw", "served_load_kw", "unserved_load_kw", "isolated_loads",
    "isolated_branches", "network_cycle_rank", "switching_effort",
    "bus_voltage_coverage_rate", "line_loading_coverage_rate",
    "cumulative_device_action_count", "cumulative_control_effort",
    "pv_curtailment_command_fraction_sum", "storage_dispatch_command_fraction_sum",
)


def _compact_prompt_metrics(metrics: Any) -> Dict[str, Any]:
    if not isinstance(metrics, dict):
        return {}
    compact: Dict[str, Any] = {}
    for field in _PROMPT_METRIC_FIELDS:
        if field not in metrics:
            continue
        value = metrics[field]
        if isinstance(value, bool) or value is None:
            compact[field] = value
        elif isinstance(value, (int, float)) and math.isfinite(float(value)):
            compact[field] = round(float(value), 8)
        elif isinstance(value, str):
            compact[field] = value[:120]
    return compact


def _compact_prompt_action(action: Dict[str, Any]) -> Dict[str, Any]:
    """Keep only bounded action-schema fields in model-facing memory."""
    fields = (
        "type", "regcontrol", "step", "cap", "state", "op", "line",
        "device", "kw", "kvar", "pct_pmpp", "storage", "fleet", "pct_kw", "bus",
        "name", "phases", "kva", "pmpp", "model",
    )
    compact: Dict[str, Any] = {}
    for field in fields:
        if field not in action:
            continue
        value = action[field]
        if isinstance(value, (str, int, float, bool)) or value is None:
            compact[field] = value[:120] if isinstance(value, str) else value
    return compact


def _prompt_record_actions(record: Dict[str, Any]) -> List[Dict[str, Any]]:
    solution = record.get("solution", {}) if isinstance(record.get("solution"), dict) else {}
    raw_actions = record.get("actions")
    if raw_actions is None:
        raw_actions = solution.get("delta_actions", [])
    return sanitize_actions(raw_actions)


def _prompt_record_source(record: Dict[str, Any]) -> str:
    solution = record.get("solution", {}) if isinstance(record.get("solution"), dict) else {}
    return str(record.get("source") or solution.get("source") or "UNKNOWN")[:40]


def _prompt_record_name(record: Dict[str, Any]) -> str:
    solution = record.get("solution", {}) if isinstance(record.get("solution"), dict) else {}
    return str(record.get("name") or solution.get("name") or "candidate")[:80]


def _prompt_record_is_baseline(record: Dict[str, Any]) -> bool:
    return _prompt_record_source(record).upper() == "BASE" or _prompt_record_name(record).upper() == "BASELINE"


def _prompt_record_is_certified(record: Dict[str, Any]) -> bool:
    solution = record.get("solution", {}) if isinstance(record.get("solution"), dict) else {}
    status = str(record.get("status", "")).strip().lower()
    return _prompt_record_is_baseline(record) or status == "certified" or bool(
        record.get("certified") or solution.get("certified")
    )


def _compact_prompt_record(record: Dict[str, Any], status: str) -> Dict[str, Any]:
    actions = _prompt_record_actions(record)
    fingerprint = str(record.get("fingerprint") or "")
    if not fingerprint:
        fingerprint = "baseline" if _prompt_record_is_baseline(record) else candidate_bundle_fingerprint(actions)
    compact: Dict[str, Any] = {
        "name": _prompt_record_name(record),
        "source": _prompt_record_source(record),
        "status": status,
        "action_count": len(actions),
        "fingerprint": fingerprint[:80],
        "metrics": _compact_prompt_metrics(record.get("metrics", {})),
        "representative_actions": [_compact_prompt_action(action) for action in actions[:3]],
    }
    score = record.get("obj", record.get("objective"))
    if _finite_number(score):
        compact["objective"] = float(score)
    failures = record.get("failure_modes", [])
    if isinstance(failures, list) and failures:
        compact["failure_modes"] = [str(item)[:180] for item in failures[:6]]
    return compact


def _evaluated_memory_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """Store bounded replay evidence without retaining solver snapshots."""
    status = "certified" if bool(record.get("certified")) else "rejected"
    compact = _compact_prompt_record(record, status)
    compact.update({
        "iteration": int(record.get("iteration", 0)),
        "certified": bool(record.get("certified")),
    })
    return compact


def _compact_verification_feedback(feedback: Any) -> Dict[str, Any]:
    if not isinstance(feedback, dict):
        return {}
    compact: Dict[str, Any] = {}
    if "iteration" in feedback:
        compact["iteration"] = feedback["iteration"]
    for field, limit in (("summary", 600), ("repair_instruction", 800)):
        if feedback.get(field):
            compact[field] = str(feedback[field])[:limit]
    counts = feedback.get("failure_counts", {})
    if isinstance(counts, dict):
        compact["failure_counts"] = {
            str(key)[:80]: value for key, value in list(counts.items())[:12]
            if isinstance(value, (int, float))
        }
    examples = feedback.get("examples", [])
    if isinstance(examples, list):
        compact["examples"] = [
            {
                "candidate": str(item.get("candidate", item.get("name", "candidate")))[:80],
                "source": str(item.get("source", ""))[:40],
                "representative_actions": [
                    _compact_prompt_action(action)
                    for action in (item.get("actions") or [])[:3]
                    if isinstance(action, dict)
                ],
                "failure_modes": [
                    str(mode)[:180]
                    for mode in (item.get("failure_modes") or item.get("failures") or [])[:4]
                ],
                "metrics": _compact_prompt_metrics(item.get("metrics") or {}),
                "line_loading_evidence": [
                    {
                        "line": str(evidence.get("line", ""))[:160],
                        "loading_pct": evidence.get("loading_pct"),
                        "reference_loading_pct": evidence.get("reference_loading_pct"),
                    }
                    for evidence in (item.get("line_loading_evidence") or [])[:6]
                    if isinstance(evidence, dict)
                ],
            }
            for item in examples[-5:] if isinstance(item, dict)
        ]
    derived = feedback.get("derived_repair_candidates", [])
    if isinstance(derived, list):
        compact["derived_repair_candidates"] = [
            {
                "name": str(item.get("name", ""))[:80],
                "actions": [
                    _compact_prompt_action(action)
                    for action in (item.get("actions") or [])[:3]
                    if isinstance(action, dict)
                ],
                "repair_derivation": item.get("repair_derivation"),
            }
            for item in derived[:3] if isinstance(item, dict)
        ]
    critic = feedback.get("critic_agent", {})
    if isinstance(critic, dict) and critic:
        compact["critic_agent"] = {
            "diagnosis": str(critic.get("diagnosis", ""))[:500],
            "avoid": [str(item)[:120] for item in critic.get("avoid", [])[:6]],
            "next_focus": [str(item)[:80] for item in critic.get("next_focus", [])[:6]],
            "repair_instruction": str(critic.get("repair_instruction", ""))[:500],
        }
    return compact


def build_meta_prompt(task: str,
                      constraints: List[str],
                      state_summary: Dict[str, Any],
                      best_so_far: List[Dict[str, Any]],
                      recent_evals: List[Dict[str, Any]],
                      stuck: int,
                      forbidden_first: List[str],
                      prefer_utility_first: bool,
                      allow_var_gen_now: bool,
                      allow_pv_now: bool,
                      allow_load_now: bool,
                      k_candidates: int,
                      max_actions: int,
                      verification_feedback: Optional[Dict[str, Any]] = None) -> str:
    feasible_frontier = [
        _compact_prompt_record(record, "baseline" if _prompt_record_is_baseline(record) else "certified")
        for record in best_so_far
        if isinstance(record, dict) and _prompt_record_is_certified(record)
    ][:10]
    rejected_recent: List[Dict[str, Any]] = []
    for record in recent_evals:
        if (
            not isinstance(record, dict)
            or _prompt_record_is_baseline(record)
            or _prompt_record_is_certified(record)
        ):
            continue
        compact_record = _compact_prompt_record(record, "rejected")
        rejected_recent.append({
            "fingerprint": compact_record.get("fingerprint"),
            "objective": compact_record.get("objective"),
            "metrics": compact_record.get("metrics", {}),
            "failure_modes": compact_record.get("failure_modes", []),
        })
    rejected_recent = rejected_recent[-12:]
    banned_exact_actions: List[Dict[str, Any]] = []
    for record in recent_evals[-20:]:
        if not isinstance(record, dict):
            continue
        # Retain enough exact action-level evidence to keep the planner from
        # walking straight back into a rejected large portfolio.  The global
        # cap below keeps the prompt bounded across many prior candidates.
        for action in _prompt_record_actions(record)[:24]:
            compact_action = _compact_prompt_action(action)
            if compact_action not in banned_exact_actions:
                banned_exact_actions.append(compact_action)
    banned_exact_actions = banned_exact_actions[:24]
    compact_feedback = _compact_verification_feedback(verification_feedback)
    # Large deterministic portfolios are useful for feeder-scale fallback
    # search, but asking a small local model to emit dozens of actions makes
    # malformed or truncated JSON much more likely. This cap applies only to
    # the LLM prompt; deterministic portfolios still use max_actions directly.
    llm_action_cap = max(1, min(int(max_actions), 8))

    # Build schema examples from this feeder's actual allowlist. Static examples with
    # fictional device names teach the model to hallucinate otherwise-invalid actions.
    devices = state_summary.get("available_devices", {}) or {}
    regcontrols = list(devices.get("regcontrols") or [])
    capacitors = list(devices.get("capacitors") or [])
    switchable_lines = list(devices.get("switchable_lines") or [])
    open_switches = list(devices.get("open_switches") or [])
    pvsystems = list(devices.get("pvsystems") or [])
    storages = list(devices.get("storages") or [])
    storage_fleets_raw = dict(devices.get("storage_fleets") or {})
    storage_fleets = {
        str(fleet_id): (
            int(value) if isinstance(value, (int, float)) else len(value or [])
        )
        for fleet_id, value in storage_fleets_raw.items()
    }
    generators = list(devices.get("generators") or [])
    worst_buses = list(state_summary.get("WORST_BUSES") or [])
    worst_bus = str(worst_buses[0].get("bus")) if worst_buses else ""
    allowed_actions_desc: List[Dict[str, Any]] = []
    if regcontrols:
        allowed_actions_desc.append({"type": "tap_step", "regcontrol": regcontrols[0], "step": -1})
    if capacitors:
        allowed_actions_desc.append({"type": "cap_state", "cap": capacitors[0], "state": "(1)"})
    if state_summary.get("allow_switch") and switchable_lines:
        switch_name = open_switches[0] if open_switches else switchable_lines[0]
        allowed_actions_desc.append({
            "type": "switch_line",
            "op": "close" if open_switches else "open",
            "line": switch_name,
        })
    if pvsystems:
        allowed_actions_desc.append({
            "type": "der_setpoint", "device": f"PVSystem.{pvsystems[0]}", "pct_pmpp": 75,
        })
    elif generators:
        allowed_actions_desc.append({
            "type": "der_setpoint", "device": f"Generator.{generators[0]}", "kw": 500, "kvar": 150,
        })
    if storages:
        allowed_actions_desc.append({
            "type": "storage_setpoint", "storage": storages[0],
            "state": "CHARGING", "pct_kw": 50,
        })
    if storage_fleets:
        first_fleet = next(iter(storage_fleets))
        allowed_actions_desc.append({
            "type": "storage_fleet_setpoint", "fleet": first_fleet,
            "state": "CHARGING", "pct_kw": 40,
        })
    if allow_var_gen_now and worst_bus:
        allowed_actions_desc.append({"type": "create_var_gen", "bus": worst_bus, "kvar": 300})
    if allow_pv_now and worst_bus:
        allowed_actions_desc.append({
            "type": "create_pv", "bus": worst_bus, "kva": 1200, "pmpp": 900, "kvar": 0,
        })
    if allow_load_now and worst_bus:
        allowed_actions_desc.append({"type": "create_load", "bus": worst_bus, "kw": 800, "kvar": 200})
    if not prefer_utility_first:
        family_priority = {
            "storage_fleet_setpoint": 0, "der_setpoint": 1,
            "storage_setpoint": 2, "tap_step": 3, "cap_state": 4,
        }
        allowed_actions_desc = sorted(
            allowed_actions_desc,
            key=lambda action: family_priority.get(str(action.get("type", "")), 4),
        )

    # Critic guidance may deliberately revisit a family with a different device or
    # increment. In that case it supersedes the coarse novelty ban, eliminating a
    # contradictory prompt (forbid tap_step while requiring a regulator candidate).
    critic_focus_raw = ((verification_feedback or {}).get("critic_agent") or {}).get("next_focus") or []
    if isinstance(critic_focus_raw, str):
        critic_focus = [critic_focus_raw]
    elif isinstance(critic_focus_raw, list):
        critic_focus = critic_focus_raw
    else:
        critic_focus = []
    focus_families: set[str] = set()
    for focus in critic_focus:
        if focus in {"tap_step", "regcontrols"} or focus in regcontrols:
            focus_families.add("tap_step")
        elif focus in {"cap_state", "capacitors"} or focus in capacitors:
            focus_families.add("cap_state")
        elif focus in {"switch_line", "switchable_lines"} or focus in switchable_lines:
            focus_families.add("switch_line")
        elif focus in {"der_setpoint", "pvsystems", "generators"} or focus in pvsystems or focus in generators:
            focus_families.add("der_setpoint")
        elif focus in {"storage_setpoint", "storages"} or focus in storages:
            focus_families.add("storage_setpoint")
        elif focus in {"storage_fleet_setpoint", "storage_fleets"} or focus in storage_fleets:
            focus_families.add("storage_fleet_setpoint")
        elif focus in {"create_var_gen", "create_pv", "create_load"}:
            focus_families.add(focus)
    effective_forbidden = [family for family in forbidden_first if family not in focus_families]
    enabled_types: List[str] = []
    if regcontrols:
        enabled_types.append("tap_step")
    if capacitors:
        enabled_types.append("cap_state")
    if state_summary.get("allow_switch") and switchable_lines:
        enabled_types.append("switch_line")
    if pvsystems or generators:
        enabled_types.append("der_setpoint")
    if storages:
        enabled_types.append("storage_setpoint")
    if storage_fleets:
        enabled_types.append("storage_fleet_setpoint")
    if allow_var_gen_now and worst_bus:
        enabled_types.append("create_var_gen")
    if allow_pv_now and worst_bus:
        enabled_types.append("create_pv")
    if allow_load_now and worst_bus:
        enabled_types.append("create_load")

    # Hard gating: when prefer_utility_first, explicitly forbid var/pv/load until allowed_now True
    gating_note = []
    if prefer_utility_first:
        gating_note.append("PREFER_UTILITY_FIRST is TRUE: focus on tap_step and cap_state first.")
        if not allow_var_gen_now:
            gating_note.append("DO NOT propose create_var_gen yet (wait until stuck_counter reaches threshold).")
        if not allow_pv_now:
            gating_note.append("DO NOT propose create_pv yet (wait until stuck_counter reaches threshold).")
        if not allow_load_now:
            gating_note.append("DO NOT propose create_load yet (wait until stuck_counter reaches threshold).")
    else:
        gating_note.append(
            "PREFER_UTILITY_FIRST is FALSE: choose the action family best supported by measured evidence."
        )

    payload = {
        "task": task,
        "objective": (
            "Minimize: 1e8*(not_converged) + 1e5*unserved_load_kw + "
            "1e6*v_severity + 1e4*viol_buses + 1e3*over_lines + "
            "1e2*thermal_severity_pct_sum + 1e3*network_cycle_rank + losses_kw + "
            "100*switching_effort + 100*cumulative_control_effort + "
            "5*cumulative_device_action_count"
        ),
        "constraints": constraints,
        "STATE": state_summary,
        # Put repair evidence before optimization memory so a local model sees
        # the binding failure information before candidate examples.
        "VERIFICATION_FEEDBACK": compact_feedback,
        "FEASIBLE_FRONTIER": feasible_frontier,
        "REJECTED_RECENT": rejected_recent,
        "stuck_counter": stuck,
        "FORBIDDEN_FIRST_ACTION_FAMILIES": effective_forbidden,
        "ACTION_SCHEMA": {
            "allowed_types": enabled_types,
            "examples": allowed_actions_desc
        },
        "EXACT_TARGET_POOLS": {
            "pvsystems": pvsystems[:20],
            "storages": storages[:20],
            "storage_fleets": [
                {"fleet": fleet_id, "device_count": device_count}
                for fleet_id, device_count in list(storage_fleets.items())[:20]
            ],
            "regcontrols": regcontrols[:20],
            "capacitors": capacitors[:20],
            "open_switches": open_switches[:20],
            "voltage_priority_pvs": list(state_summary.get("VOLTAGE_PRIORITY_PVS") or [])[:20],
            "thermal_priority_pvs": list(state_summary.get("THERMAL_PRIORITY_PVS") or [])[:20],
        },
        "BANNED_EXACT_ACTIONS": banned_exact_actions,
        "SETPOINT_MENU": {
            "pv_pct_pmpp": [0, 20, 40, 60, 75, 90],
            "storage_pct_kw": [20, 40, 60, 80, 100],
            "tap_step": [-4, -2, -1, 1, 2, 4],
        },
        "UTILITY_FIRST_GUIDANCE": gating_note,
        "TAP_RULE": (
            "tap_step is optional, never mandatory. Use it only when regcontrols is non-empty, it is not "
            "forbidden, and measured evidence supports it."
        ),
        "EXTRA_INSTRUCTION": state_summary.get("extra_instruction", ""),
        "DIVERSITY_RULE": (
            "Diversify across exact targets and setpoint magnitudes within ACTION_SCHEMA.allowed_types. "
            "A failed setpoint does not forbid its whole family: if it improved some metrics, repair it "
            "by changing device, direction, magnitude, or bundle composition."
        ),
        "NOVELTY_RULE_WHEN_STUCK": (
            "If stuck_counter>=1: do NOT repeat first-action family patterns listed in FORBIDDEN_FIRST_ACTION_FAMILIES. "
            "Use a different device name or different worst bus."
        ),
        "instruction": (
            f"Propose {k_candidates} NEW candidates. Each must have "
            f"1..{llm_action_cap} actions. Use at most 12 words in reasoning."
        ),
        "IMPORTANT": [
            "Return ONLY one valid JSON object. No tags or markdown.",
            "Each candidate MUST include >=1 action.",
            "Actions MUST be JSON objects, NOT strings.",
            "Every candidate must use the key actions; never copy evidence fields such as representative_actions, metrics, status, or fingerprint into the output.",
            "Use exact device names in STATE.available_devices.",
            "For PV real-power control use pct_pmpp in [0,100], not kW.",
            "For batteries use storage_setpoint with CHARGING, DISCHARGING, or IDLING.",
            "Do NOT output placeholder values like 'string'.",
            "Do not copy example setpoint values unless current measurements justify them.",
            "Do not repeat a fingerprint shown in FEASIBLE_FRONTIER or REJECTED_RECENT.",
            "Never reproduce an action in BANNED_EXACT_ACTIONS; change both target or setpoint as needed.",
            "Use different exact targets or setpoints across candidates and iterations.",
            "If a candidate reduced voltage burden but worsened the worst line, keep its useful direction and move control toward TOP_LINES endpoint buses.",
            "Do NOT propose Edit Vsource.*",
            "Do NOT invent device names.",
            "When restoring service, close only a listed open switch and never a quarantined faulted line.",
        ],
        "OUTPUT_FORMAT": {"candidates": [{
            "name": "...",
            "actions": [allowed_actions_desc[0]] if allowed_actions_desc else [],
            "reasoning": "...",
        }]}
    }

    binding_instruction = str(state_summary.get("extra_instruction", "")).strip()
    binding_tail = (
        "\nBINDING EXTRA INSTRUCTION (apply exactly unless it violates the JSON schema):\n"
        + binding_instruction
        if binding_instruction
        else ""
    )
    novelty_tail = (
        "\nBINDING NOVELTY RULE: none of the following exact actions may be repeated; "
        "choose different exact targets or setpoints:\n"
        + json.dumps(banned_exact_actions)
        if banned_exact_actions else ""
    )
    return (
        "Read the following JSON planning context.\n"
        "<JSON>" + json.dumps(payload) + "</JSON>\n"
        + binding_tail + novelty_tail + "\n"
        "Now output ONLY:\n"
        "{\"candidates\": [...]}"
    )


# =========================
# GridGuard typed LangGraph workflow
# =========================
class GridGuardState(TypedDict, total=False):
    """Shared state carried through the GridGuard StateGraph."""

    case: Dict[str, str]
    base_cmds: List[str]
    state_cmds: List[str]
    operating_state_id: str
    evaluated_fingerprints: Dict[str, Dict[str, Any]]
    vmin: float
    vmax: float
    feeder_model: Dict[str, Any]
    telemetry: Dict[str, Any]
    admissible_controls: Dict[str, Any]
    candidate_actions: List[Dict[str, Any]]
    repair_candidates: List[Dict[str, Any]]
    simulation_outputs: List[Dict[str, Any]]
    violation_summaries: List[Dict[str, Any]]
    feedback_history: List[Dict[str, Any]]
    meta_prompt_snapshots: List[Dict[str, Any]]
    agent_trace: List[Dict[str, Any]]
    verification_results: List[Dict[str, Any]]
    evaluation_history: List[Dict[str, Any]]
    current_snapshot: SnapshotResult
    baseline_snapshot: SnapshotResult
    current_metrics: Dict[str, Any]
    baseline_metrics: Dict[str, Any]
    security_reference_metrics: Dict[str, Any]
    security_reference_snapshot: SnapshotResult
    best_so_far: List[Dict[str, Any]]
    recent_evals: List[Dict[str, Any]]
    pending_accept: Dict[str, Any]
    history: List[Dict[str, Any]]
    iteration: int
    stuck: int
    total_candidates: int
    candidate_slots_allocated: int
    llm_candidate_objects_returned: int
    llm_parse_valid_candidates: int
    historical_duplicates_filtered: int
    certified_candidates: int
    invalid_candidates: int
    rejected_candidates: int
    switching_effort: int
    first_certified_iteration: Optional[int]
    route: str
    final_metrics: Dict[str, Any]
    run_path: str


@dataclass(frozen=True)
class GridGuardConfig:
    steps: int
    k_candidates: int
    max_actions: int
    llm_samples: int
    explore_temp: float
    guardrail_start_stuck: int
    max_stuck: int
    allow_switch: bool
    allow_pv: bool
    allow_load: bool
    allow_var_gen: bool
    prefer_utility_first: bool
    vargen_after_stuck: int
    pv_after_stuck: int
    load_after_stuck: int
    fast_llm: bool
    show_meta_prompt: bool
    teaching_notes: bool
    extra_instruction: str
    # Research ablations. Defaults preserve the interactive application's
    # original hybrid behavior; the TII benchmark switches them explicitly.
    enable_llm_candidates: bool = True
    enable_physics_fallback: bool = True
    enable_portfolio_seeds: bool = True
    enable_scored_memory: bool = True
    enable_verifier_feedback: bool = True
    enable_critic: bool = True
    allow_recovered_solve: bool = True
    certificate_mode: str = "relative_safe_improvement"
    voltage_severity_tolerance_pu: float = 1e-8
    max_line_loading_tolerance_pct: float = 1e-8
    thermal_severity_tolerance_pct_sum: float = 1e-8
    restoration_tolerance_kw: float = 1e-6
    max_physical_actions: int = 5000
    storage_fleets: Dict[str, List[str]] = field(default_factory=dict)
    restoration_ties: List[str] = field(default_factory=list)
    restoration_watch_lines: List[str] = field(default_factory=list)
    restoration_probe_pct_kw: float = 40.0
    restoration_target_loading_pct: float = 99.5


SAFE_DSS_NAME = re.compile(r"^[A-Za-z0-9_.-]+$")


def _finite_number(value: Any) -> bool:
    try:
        return math.isfinite(float(value))
    except Exception:
        return False


def _action_target(action: Dict[str, Any]) -> str:
    typ = _normalize_type(action.get("type", ""))
    if typ == "tap_step":
        return f"regcontrol.{action.get('regcontrol', '')}".lower()
    if typ == "cap_state":
        return f"capacitor.{action.get('cap', '')}".lower()
    if typ == "switch_line":
        return f"line.{action.get('line', '')}".lower()
    if typ == "der_setpoint":
        return str(action.get("device", "")).lower()
    if typ == "storage_setpoint":
        return f"storage.{action.get('storage', '')}".lower()
    if typ == "storage_fleet_setpoint":
        return f"storage_fleet.{action.get('fleet', '')}".lower()
    if typ in ("create_var_gen", "create_pv", "create_load"):
        return f"{typ}.{action.get('bus', '')}".lower()
    return typ


def ground_supervisory_actions(
    state: GridGuardState,
    actions_any: Any,
    config: GridGuardConfig,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[str]]:
    """Expand approved fleet macro-actions into exact device commands.

    The LLM sees and budgets supervisory actions.  Only this deterministic
    function may expand an allowlisted fleet ID to physical storage devices;
    arbitrary prefixes or invented membership are never accepted.
    """
    supervisory = sanitize_actions(actions_any)
    grounded: List[Dict[str, Any]] = []
    expansions: List[Dict[str, Any]] = []
    errors: List[str] = []
    discovered = {
        str(name).lower(): str(name)
        for name in (
            state.get("current_snapshot").devices.get("storages", [])
            if state.get("current_snapshot") is not None else []
        )
    }
    fleet_lookup = {
        str(fleet_id).lower(): (str(fleet_id), list(members))
        for fleet_id, members in (config.storage_fleets or {}).items()
    }
    for index, action in enumerate(supervisory):
        typ = _normalize_type(action.get("type", ""))
        if typ != "storage_fleet_setpoint":
            grounded.append(dict(action))
            continue
        fleet_key = str(action.get("fleet", "")).strip().lower()
        if fleet_key not in fleet_lookup:
            errors.append(f"action[{index}]:inadmissible_storage_fleet:{fleet_key}")
            continue
        fleet_id, members = fleet_lookup[fleet_key]
        canonical_members: List[str] = []
        missing: List[str] = []
        for member in members:
            canonical = discovered.get(str(member).lower())
            if canonical is None:
                missing.append(str(member))
            else:
                canonical_members.append(canonical)
        if missing:
            errors.append(
                f"action[{index}]:storage_fleet_members_missing:{fleet_id}:{len(missing)}"
            )
            continue
        for storage in canonical_members:
            physical = {
                "type": "storage_setpoint",
                "storage": storage,
                "state": action.get("state"),
            }
            if action.get("pct_kw") is not None:
                physical["pct_kw"] = action.get("pct_kw")
            if action.get("kvar") is not None:
                physical["kvar"] = action.get("kvar")
            grounded.append(physical)
        membership_hash = hashlib.sha256(
            json.dumps(sorted(name.lower() for name in canonical_members)).encode("utf-8")
        ).hexdigest()
        expansions.append({
            "supervisory_action_index": index,
            "type": typ,
            "fleet": fleet_id,
            "physical_device_count": len(canonical_members),
            "membership_sha256": membership_hash,
        })
    if len(grounded) > config.max_physical_actions:
        errors.append(
            f"grounding:physical_action_budget_exceeded:{len(grounded)}>{config.max_physical_actions}"
        )
    return grounded[:config.max_physical_actions], expansions, errors


def prepare_telemetry_validation_batch(
    telemetry_any: Any,
    validation_time: Optional[datetime] = None,
) -> Tuple[Dict[str, Any], datetime]:
    """Freeze one telemetry time reference for a complete candidate batch.

    A generated offline OpenDSS snapshot is refreshed at the batch boundary,
    because candidate simulations are counterfactual evaluations of that same
    snapshot rather than elapsed real-world telemetry. User-supplied/external
    timestamps remain untouched and are still subject to the configured age gate.
    """
    now = validation_time or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    telemetry = dict(telemetry_any or {})
    if telemetry.get("timestamp_mode") == "offline_batch":
        telemetry["timestamp_utc"] = now.isoformat()
        telemetry["batch_refreshed_utc"] = now.isoformat()
    telemetry["validation_batch_utc"] = now.isoformat()
    return telemetry, now


def validate_candidate_actions(
    state: GridGuardState,
    actions_any: Any,
    config: GridGuardConfig,
    allow_var_gen_now: bool,
    allow_pv_now: bool,
    allow_load_now: bool,
    validation_time: Optional[datetime] = None,
    action_limit: Optional[int] = None,
) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Reject malformed, inadmissible, stale, or conflicting control requests."""
    actions = sanitize_actions(actions_any)
    effective_limit = int(action_limit if action_limit is not None else config.max_actions)
    errors: List[str] = []
    if not actions:
        return [], ["schema:no_actions"]
    if len(actions) > effective_limit:
        errors.append(f"schema:too_many_actions:{len(actions)}")

    res = state["current_snapshot"]
    devices = res.devices
    quarantined = {
        str(item).lower() for item in state.get("telemetry", {}).get("quarantined_devices", [])
    }
    expected_hash = str(state.get("telemetry", {}).get("expected_topology_hash", ""))
    if expected_hash and expected_hash != res.topology_hash:
        errors.append("cyber:topology_mismatch")
    if not bool(state.get("telemetry", {}).get("trusted", True)):
        errors.append("cyber:telemetry_untrusted")

    timestamp = state.get("telemetry", {}).get("timestamp_utc")
    max_age_s = float(state.get("telemetry", {}).get("max_age_s", 300.0))
    if timestamp:
        try:
            observed = datetime.fromisoformat(str(timestamp).replace("Z", "+00:00"))
            if observed.tzinfo is None:
                observed = observed.replace(tzinfo=timezone.utc)
            reference_time = validation_time or datetime.now(timezone.utc)
            if reference_time.tzinfo is None:
                reference_time = reference_time.replace(tzinfo=timezone.utc)
            age_s = (reference_time - observed).total_seconds()
            if age_s > max_age_s:
                errors.append(f"cyber:stale_telemetry:{age_s:.0f}s")
        except Exception:
            errors.append("cyber:bad_telemetry_timestamp")

    targets: set[str] = set()
    regcontrols = set(devices.get("regcontrols") or [])
    capacitors = set(devices.get("capacitors") or [])
    lines = set(devices.get("lines") or [])
    switchable = set(devices.get("switchable_lines") or [])
    pvs = set(devices.get("pvsystems") or [])
    storages = set(devices.get("storages") or [])
    generators = set(devices.get("generators") or [])

    for index, action in enumerate(actions[:effective_limit]):
        typ = _normalize_type(action.get("type", ""))
        prefix = f"action[{index}]"
        if typ not in ALLOWED_TYPES:
            errors.append(f"{prefix}:unknown_type:{typ}")
            continue

        target = _action_target(action)
        if target in targets:
            errors.append(f"{prefix}:conflicting_target:{target}")
        targets.add(target)
        if target in quarantined:
            errors.append(f"{prefix}:cyber_quarantined:{target}")

        if typ == "tap_step":
            name = str(action.get("regcontrol", ""))
            step = _safe_int(action.get("step", 0), 0)
            if name not in regcontrols or res.reg_map.get(name, {}).get("xfmr") is None:
                errors.append(f"{prefix}:inadmissible_regcontrol:{name}")
            if step == 0 or step < -4 or step > 4:
                errors.append(f"{prefix}:tap_step_out_of_range:{step}")
        elif typ == "cap_state":
            name = str(action.get("cap", ""))
            if name not in capacitors:
                errors.append(f"{prefix}:inadmissible_capacitor:{name}")
            if str(action.get("state", "")) not in ("(0)", "(1)"):
                errors.append(f"{prefix}:bad_cap_state")
        elif typ == "switch_line":
            name = str(action.get("line", ""))
            if not config.allow_switch:
                errors.append(f"{prefix}:switching_disabled")
            if name not in lines:
                errors.append(f"{prefix}:unknown_line:{name}")
            if not switchable:
                errors.append(f"{prefix}:no_designated_switch_allowlist")
            elif name not in switchable:
                errors.append(f"{prefix}:line_not_designated_switch:{name}")
            if str(action.get("op", "")).lower() not in ("open", "close"):
                errors.append(f"{prefix}:bad_switch_operation")
        elif typ == "der_setpoint":
            device = str(action.get("device", ""))
            is_pv = device.startswith("PVSystem.") and device.split(".", 1)[1] in pvs
            is_generator = (
                device.startswith("Generator.") and device.split(".", 1)[1] in generators
            )
            valid = is_pv or is_generator
            if not valid:
                errors.append(f"{prefix}:unknown_der:{device}")
            if (
                action.get("kw") is None
                and action.get("kvar") is None
                and action.get("pct_pmpp") is None
            ):
                errors.append(f"{prefix}:empty_der_setpoint")
            if is_pv and action.get("kw") is not None:
                errors.append(f"{prefix}:pv_kw_not_writable_use_pct_pmpp")
            if is_generator and action.get("pct_pmpp") is not None:
                errors.append(f"{prefix}:pct_pmpp_only_valid_for_pv")
            if action.get("kw") is not None and (
                not _finite_number(action.get("kw")) or abs(float(action["kw"])) > 15000.0
            ):
                errors.append(f"{prefix}:der_kw_out_of_range")
            if action.get("kvar") is not None and (
                not _finite_number(action.get("kvar")) or abs(float(action["kvar"])) > 10000.0
            ):
                errors.append(f"{prefix}:der_kvar_out_of_range")
            if action.get("pct_pmpp") is not None and (
                not _finite_number(action.get("pct_pmpp"))
                or not 0.0 <= float(action["pct_pmpp"]) <= 100.0
            ):
                errors.append(f"{prefix}:pv_pct_pmpp_out_of_range")
        elif typ == "storage_setpoint":
            name = str(action.get("storage", ""))
            state_name = str(action.get("state", "")).upper()
            if name not in storages:
                errors.append(f"{prefix}:unknown_storage:{name}")
            if state_name not in ("CHARGING", "DISCHARGING", "IDLING"):
                errors.append(f"{prefix}:bad_storage_state:{state_name}")
            if state_name != "IDLING" and action.get("pct_kw") is None:
                errors.append(f"{prefix}:missing_storage_pct_kw")
            if action.get("pct_kw") is not None and (
                not _finite_number(action.get("pct_kw"))
                or not 0.0 <= float(action["pct_kw"]) <= 100.0
            ):
                errors.append(f"{prefix}:storage_pct_kw_out_of_range")
            if action.get("kvar") is not None and (
                not _finite_number(action.get("kvar"))
                or abs(float(action["kvar"])) > 10000.0
            ):
                errors.append(f"{prefix}:storage_kvar_out_of_range")
        else:
            bus = str(action.get("bus", ""))
            if not bus or not SAFE_DSS_NAME.fullmatch(bus) or not safe_bus_exists(bus):
                errors.append(f"{prefix}:unknown_bus:{bus}")
            if typ == "create_var_gen" and not allow_var_gen_now:
                errors.append(f"{prefix}:var_gen_not_admissible_now")
            if typ == "create_pv" and not allow_pv_now:
                errors.append(f"{prefix}:pv_not_admissible_now")
            if typ == "create_load" and not allow_load_now:
                errors.append(f"{prefix}:load_not_admissible_now")

        for value in action.values():
            if isinstance(value, str) and len(value) > 160:
                errors.append(f"{prefix}:oversized_value")
                break
        # Existing-device identifiers are already checked by exact membership
        # in the discovered catalog above. SMART-DS legitimately uses names
        # containing parentheses and colons, so a generic identifier regex
        # would reject valid switches. Only user-created object names require
        # the restricted grammar.
        created_name = action.get("name")
        if created_name and not SAFE_DSS_NAME.fullmatch(str(created_name)):
            errors.append(f"{prefix}:unsafe_identifier")

    return actions[:effective_limit], list(dict.fromkeys(errors))


def _read_active_dss_property(element: str, property_names: List[str]) -> Tuple[Any, str]:
    """Read an element property without treating an absent API as a value.

    OpenDSSDirect versions differ in which class-specific properties they
    expose.  The generic active-element property interface is the preferred
    path, with a text query as a compatibility fallback.
    """
    try:
        activated = dss.Circuit.SetActiveElement(element)
        if activated is False or activated == 0:
            return None, "element_not_found"
    except Exception as exc:
        return None, f"activation_error:{type(exc).__name__}"

    properties = getattr(dss, "Properties", None)
    value_fn = getattr(properties, "Value", None) if properties is not None else None
    if callable(value_fn):
        for prop in property_names:
            try:
                value = value_fn(prop)
                if value is not None and str(value).strip() != "":
                    return value, f"api.Properties.Value({prop})"
            except Exception:
                continue

    for prop in property_names:
        value = dss_query(f"? {element}.{prop}")
        text_value = str(value).strip()
        unavailable_markers = (
            "(query_error)", "error", "unknown", "invalid", "not found", "not recognized"
        )
        if text_value and not any(
            marker in text_value.lower() for marker in unavailable_markers
        ):
            return value, f"query:{prop}"
    return None, "property_unavailable"


def _readback_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    match = re.search(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][-+]?\d+)?", str(value))
    if not match:
        return None
    try:
        parsed = float(match.group(0))
        return parsed if math.isfinite(parsed) else None
    except Exception:
        return None


def _normalized_cap_states(value: Any) -> Optional[Tuple[int, ...]]:
    if isinstance(value, (list, tuple, np.ndarray)):
        raw = list(value)
    else:
        raw = re.findall(r"[-+]?\d+", str(value or ""))
    try:
        states = tuple(int(float(item)) for item in raw)
    except Exception:
        return None
    return states or None


def _reg_map_entry(snapshot: SnapshotResult, name: str) -> Dict[str, Any]:
    direct = snapshot.reg_map.get(name)
    if direct is not None:
        return direct
    lowered = name.lower()
    for key, value in snapshot.reg_map.items():
        if str(key).lower() == lowered:
            return value
    return {}


def verify_post_solve_actuation(
    actions_any: Any,
    before_snapshot: SnapshotResult,
    numeric_tolerance: float = 1e-3,
) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Compare requested controls with deterministic post-solve readback.

    Supported existing-device actions fail closed: a mismatch *or* unavailable
    readback is a cyber/actuation certification failure.  Creation actions keep
    their existing compile/discovery/physics checks and are reported as outside
    this focused state-readback gate.
    """
    records: List[Dict[str, Any]] = []
    errors: List[str] = []

    def finish(
        index: int,
        typ: str,
        target: str,
        requested: Any,
        observed: Any,
        source: str,
        status: str,
    ) -> None:
        record = {
            "action_index": index,
            "type": typ,
            "target": target,
            "requested": requested,
            "observed": observed,
            "source": source,
            "status": status,
        }
        records.append(record)
        if status in {"mismatch", "unavailable"}:
            errors.append(
                f"cyber:actuation_{status}:action[{index}]:{target.lower()}"
            )

    for index, action in enumerate(sanitize_actions(actions_any)):
        typ = _normalize_type(action.get("type", ""))
        target = _action_target(action)

        if typ == "der_setpoint":
            device = str(action.get("device", "")).strip()
            checks: List[Tuple[str, Any, List[str]]] = []
            if action.get("pct_pmpp") is not None:
                checks.append(("pct_pmpp", float(action["pct_pmpp"]), ["%Pmpp", "pctPmpp"]))
            if action.get("kw") is not None:
                checks.append(("kw", float(action["kw"]), ["kW", "kw"]))
            if action.get("kvar") is not None:
                checks.append(("kvar", float(action["kvar"]), ["kvar", "kVAr"]))
            for field, requested, property_names in checks:
                value, source = _read_active_dss_property(device, property_names)
                observed = _readback_float(value)
                field_target = f"{device}.{field}"
                if observed is None:
                    finish(index, typ, field_target, requested, None, source, "unavailable")
                elif math.isclose(observed, requested, rel_tol=0.0, abs_tol=numeric_tolerance):
                    finish(index, typ, field_target, requested, observed, source, "verified")
                else:
                    finish(index, typ, field_target, requested, observed, source, "mismatch")
            continue

        if typ == "storage_setpoint":
            name = str(action.get("storage", "")).strip()
            element = f"Storage.{name}"
            requested_state = str(action.get("state", "")).strip().upper()
            state_value, state_source = _read_active_dss_property(element, ["State", "state"])
            observed_state: Optional[str] = None
            if state_value is not None:
                raw_state = str(state_value).strip().upper()
                enum_states = {"-1": "CHARGING", "0": "IDLING", "1": "DISCHARGING"}
                observed_state = enum_states.get(raw_state, raw_state)
            state_target = f"{element}.state"
            if not observed_state:
                finish(index, typ, state_target, requested_state, None, state_source, "unavailable")
            elif observed_state == requested_state:
                finish(index, typ, state_target, requested_state, observed_state, state_source, "verified")
            else:
                finish(index, typ, state_target, requested_state, observed_state, state_source, "mismatch")

            if requested_state != "IDLING" and action.get("pct_kw") is not None:
                prop = "%Charge" if requested_state == "CHARGING" else "%Discharge"
                requested_pct = float(action["pct_kw"])
                pct_value, pct_source = _read_active_dss_property(element, [prop])
                observed_pct = _readback_float(pct_value)
                pct_target = f"{element}.{prop}"
                if observed_pct is None:
                    finish(index, typ, pct_target, requested_pct, None, pct_source, "unavailable")
                elif math.isclose(observed_pct, requested_pct, rel_tol=0.0, abs_tol=numeric_tolerance):
                    finish(index, typ, pct_target, requested_pct, observed_pct, pct_source, "verified")
                else:
                    finish(index, typ, pct_target, requested_pct, observed_pct, pct_source, "mismatch")
            if action.get("kvar") is not None:
                requested_kvar = float(action["kvar"])
                kvar_value, kvar_source = _read_active_dss_property(element, ["kvar", "kVAr"])
                observed_kvar = _readback_float(kvar_value)
                kvar_target = f"{element}.kvar"
                if observed_kvar is None:
                    finish(index, typ, kvar_target, requested_kvar, None, kvar_source, "unavailable")
                elif math.isclose(observed_kvar, requested_kvar, rel_tol=0.0, abs_tol=numeric_tolerance):
                    finish(index, typ, kvar_target, requested_kvar, observed_kvar, kvar_source, "verified")
                else:
                    finish(index, typ, kvar_target, requested_kvar, observed_kvar, kvar_source, "mismatch")
            continue

        if typ == "switch_line":
            line = str(action.get("line", "")).strip()
            element = f"Line.{line}"
            requested = str(action.get("op", "")).strip().lower()
            try:
                activated = dss.Circuit.SetActiveElement(element)
                if activated is False or activated == 0:
                    raise LookupError("element_not_found")
                enabled_fn = getattr(dss.CktElement, "Enabled", None)
                enabled = bool(enabled_fn()) if callable(enabled_fn) else True
                terminals = max(1, int(getattr(dss.CktElement, "NumTerminals")()))
                conductors = max(1, int(getattr(dss.CktElement, "NumConductors")()))
                is_open = getattr(dss.CktElement, "IsOpen", None)
                if not callable(is_open):
                    raise AttributeError("IsOpen")
                terminal_states = [
                    all(bool(is_open(terminal, conductor)) for conductor in range(1, conductors + 1))
                    for terminal in range(1, terminals + 1)
                ]
                any_open = any(
                    bool(is_open(terminal, conductor))
                    for terminal in range(1, terminals + 1)
                    for conductor in range(1, conductors + 1)
                )
                observed = (
                    "disabled" if not enabled
                    else "open" if any(terminal_states)
                    else ("partial" if any_open else "close")
                )
                if requested == "open" and observed == "disabled":
                    observed = "open"
                status = "verified" if observed == requested else "mismatch"
                finish(
                    index, typ, element, requested, observed,
                    "api.CktElement.Enabled+IsOpen", status,
                )
            except Exception as exc:
                finish(index, typ, element, requested, None, f"read_error:{type(exc).__name__}", "unavailable")
            continue

        if typ == "cap_state":
            cap = str(action.get("cap", "")).strip()
            element = f"Capacitor.{cap}"
            requested = _normalized_cap_states(action.get("state"))
            observed = None
            source = "property_unavailable"
            try:
                capacitors = getattr(dss, "Capacitors", None)
                name_fn = getattr(capacitors, "Name", None)
                states_fn = getattr(capacitors, "States", None)
                if callable(name_fn) and callable(states_fn):
                    name_fn(cap)
                    observed = _normalized_cap_states(states_fn())
                    source = "api.Capacitors.States"
            except Exception as exc:
                source = f"read_error:{type(exc).__name__}"
            if observed is None:
                value, property_source = _read_active_dss_property(element, ["states", "States"])
                observed = _normalized_cap_states(value)
                source = property_source
            if observed is None:
                finish(index, typ, element, requested, None, source, "unavailable")
            elif observed == requested:
                finish(index, typ, element, requested, observed, source, "verified")
            else:
                finish(index, typ, element, requested, observed, source, "mismatch")
            continue

        if typ == "tap_step":
            reg = str(action.get("regcontrol", "")).strip()
            mapping = _reg_map_entry(before_snapshot, reg)
            xfmr = mapping.get("xfmr")
            before_tap = mapping.get("tap")
            wdg = int(mapping.get("wdg", 1) or 1)
            tap_inc = float(mapping.get("tap_inc", 0.00625) or 0.00625)
            element = f"RegControl.{reg}.tap"
            if xfmr is None or before_tap is None:
                finish(index, typ, element, "relative_step", None, "reg_map_unavailable", "unavailable")
                continue
            requested = max(
                0.90,
                min(1.10, float(before_tap) + _safe_int(action.get("step", 0), 0) * tap_inc),
            )
            observed = read_transformer_tap(str(xfmr), wdg)
            tolerance = max(numeric_tolerance, abs(tap_inc) * 0.10)
            if observed is None:
                finish(index, typ, element, requested, None, "api.Transformers.Tap", "unavailable")
            elif math.isclose(float(observed), requested, rel_tol=0.0, abs_tol=tolerance):
                finish(index, typ, element, requested, float(observed), "api.Transformers.Tap", "verified")
            else:
                finish(index, typ, element, requested, float(observed), "api.Transformers.Tap", "mismatch")
            continue

        # New-element actions do not have a stable target name in the action
        # schema. Preserve their existing validation path, but make their scope
        # outside this focused existing-device gate visible in the certificate.
        finish(index, typ, target, action, None, "creation_action", "not_applicable")

    return records, list(dict.fromkeys(errors))


class GridGuardEngine:
    """LangGraph implementation of plan, verify, repair, and accept cycles."""

    def __init__(
        self,
        llm: LLMClient,
        translator: ActionTranslator,
        config: GridGuardConfig,
        progress: Optional[Callable[[str], None]] = None,
        meta_prompt_updated: Optional[Callable[[str], None]] = None,
        step_done: Optional[Callable[[Dict[str, Any]], None]] = None,
    ):
        self.llm = llm
        self.translator = translator
        self.config = config
        if config.certificate_mode not in {"relative_safe_improvement", "absolute_feasible"}:
            raise ValueError(
                "certificate_mode must be 'relative_safe_improvement' or 'absolute_feasible'"
            )
        if config.max_physical_actions < config.max_actions:
            raise ValueError("max_physical_actions must be at least max_actions")
        known_storages = {
            str(name).lower()
            for names in (config.storage_fleets or {}).values()
            for name in names
        }
        if len(known_storages) != sum(len(names) for names in (config.storage_fleets or {}).values()):
            raise ValueError("storage_fleets must not reuse a storage device across fleet IDs")
        if not 0.0 < float(config.restoration_probe_pct_kw) <= 100.0:
            raise ValueError("restoration_probe_pct_kw must be in (0, 100]")
        if not 0.0 < float(config.restoration_target_loading_pct) < 100.0:
            raise ValueError("restoration_target_loading_pct must be in (0, 100)")
        if len(config.restoration_watch_lines) > 20:
            raise ValueError("restoration_watch_lines supports at most 20 exact line names")
        self.progress = progress or (lambda _text: None)
        self.meta_prompt_updated = meta_prompt_updated or (lambda _text: None)
        self.step_done = step_done or (lambda _record: None)

    def build(self):
        if StateGraph is None:
            raise RuntimeError(
                "GridGuard requires LangGraph. Install the dependencies in requirements.txt, then restart the app."
            )
        graph = StateGraph(GridGuardState)
        graph.add_node("initialize", self.initialize_node)
        graph.add_node("plan", self.planner_node)
        graph.add_node("verify", self.verification_node)
        graph.add_node("repair", self.repair_node)
        graph.add_node("critic", self.critic_node)
        graph.add_node("accept", self.accept_node)
        graph.add_node("finalize", self.finalize_node)
        graph.add_edge(START, "initialize")
        graph.add_conditional_edges(
            "initialize", lambda state: state["route"], {"plan": "plan", "finalize": "finalize"}
        )
        graph.add_edge("plan", "verify")
        graph.add_conditional_edges(
            "verify", lambda state: state["route"], {"accept": "accept", "repair": "repair"}
        )
        graph.add_conditional_edges(
            "accept", lambda state: state["route"], {"plan": "plan", "finalize": "finalize"}
        )
        graph.add_conditional_edges(
            "repair", lambda state: state["route"],
            {"critic": "critic", "plan": "plan", "finalize": "finalize"}
        )
        graph.add_edge("critic", "plan")
        graph.add_edge("finalize", END)
        return graph.compile()

    def initialize_node(self, state: GridGuardState) -> Dict[str, Any]:
        case = state["case"]
        res = compile_and_solve(
            case["label"], case["folder"], case["main_dss"],
            state.get("base_cmds", []), state["vmin"], state["vmax"],
            recover_on_failure=self.config.allow_recovered_solve,
        )
        if res.recovery_applied and not self.config.allow_recovered_solve:
            raise RuntimeError(
                "Baseline required the automatic recovery policy; strict experiment mode "
                "requires one declared solver policy for every candidate."
            )
        metrics = summarize_metrics(res, state["vmin"], state["vmax"])
        metrics["switching_effort"] = 0
        metrics.update(action_burden([]))
        score = objective(metrics)
        now = datetime.now(timezone.utc).isoformat()
        telemetry = dict(state.get("telemetry", {}))
        supplied_timestamp = bool(telemetry.get("timestamp_utc"))
        telemetry.setdefault("source", "OpenDSS snapshot")
        telemetry.setdefault("timestamp_utc", now)
        telemetry.setdefault(
            "timestamp_mode", "external" if supplied_timestamp else "offline_batch"
        )
        telemetry.setdefault("max_age_s", 300.0)
        telemetry.setdefault("trusted", True)
        telemetry.setdefault("quarantined_devices", [])
        telemetry.setdefault("expected_topology_hash", res.topology_hash)
        history = [{
            "step": -1, "picked": "BASELINE", "source": "BASE", "applied_cmds": [],
            "before": metrics, "after": metrics, "obj": score, "teaching": "", "certified": False,
        }]
        self.progress(f"[GridGuard] Baseline score={score:.3e} metrics={metrics}")
        solved = operating_goal_satisfied(metrics)
        return {
            "state_cmds": [],
            "operating_state_id": operating_state_fingerprint([]),
            "evaluated_fingerprints": {},
            "feeder_model": {"label": res.case_label, "path": res.compiled_file},
            "telemetry": telemetry,
            "admissible_controls": res.devices,
            "candidate_actions": [],
            "repair_candidates": [],
            "simulation_outputs": [{"iteration": -1, "metrics": metrics, "score": score}],
            "violation_summaries": [metrics],
            "feedback_history": [],
            "meta_prompt_snapshots": [],
            "agent_trace": [{
                "iteration": -1,
                "node": "initialize",
                "role": "State and Telemetry Agent",
                "actor_type": "deterministic",
                "outputs": {"violating_buses": metrics.get("viol_buses"), "objective": score},
                "route": "finalize" if solved else "plan",
                "timestamp_utc": now,
            }],
            "verification_results": [],
            "evaluation_history": [],
            "current_snapshot": res,
            "baseline_snapshot": res,
            "current_metrics": metrics,
            "baseline_metrics": dict(metrics),
            "best_so_far": [{
                "obj": score, "metrics": metrics, "certified": True,
                "status": "baseline", "fingerprint": "baseline",
                "solution": {
                    "name": "BASELINE", "delta_cmds": [], "delta_actions": [],
                    "source": "BASE", "certified": True,
                },
            }],
            "recent_evals": [],
            "history": history,
            "iteration": 0,
            "stuck": 0,
            "total_candidates": 0,
            "candidate_slots_allocated": 0,
            "llm_candidate_objects_returned": 0,
            "llm_parse_valid_candidates": 0,
            "historical_duplicates_filtered": 0,
            "certified_candidates": 0,
            "invalid_candidates": 0,
            "rejected_candidates": 0,
            "switching_effort": 0,
            "first_certified_iteration": None,
            "route": "finalize" if solved else "plan",
        }

    def _gates(self, state: GridGuardState) -> Tuple[bool, bool, bool]:
        stuck = int(state.get("stuck", 0))
        cfg = self.config
        var_now = cfg.allow_var_gen and (not cfg.prefer_utility_first or stuck >= cfg.vargen_after_stuck)
        pv_now = cfg.allow_pv and (not cfg.prefer_utility_first or stuck >= cfg.pv_after_stuck)
        load_now = cfg.allow_load and (not cfg.prefer_utility_first or stuck >= cfg.load_after_stuck)
        return var_now, pv_now, load_now

    def planner_node(self, state: GridGuardState) -> Dict[str, Any]:
        started = time.perf_counter()
        cfg = self.config
        res = state["current_snapshot"]
        met = state["current_metrics"]
        stuck = int(state.get("stuck", 0))
        var_now, pv_now, load_now = self._gates(state)
        worst = worst_buses_list(res, state["vmin"], state["vmax"], k=5)
        top_lines = top_overloaded_lines(res, k=5)
        priority_buses = list(worst)
        thermal_priority_buses: List[Dict[str, Any]] = []
        for line in top_lines:
            for key in ("bus1", "bus2"):
                bus = str(line.get(key, "")).split(".", 1)[0]
                if bus:
                    priority_buses.append({"bus": bus})
                    thermal_priority_buses.append({"bus": bus})
        voltage_priority_pvs = prioritize_names_for_buses(
            res.devices.get("pvsystems") or [], worst
        )
        thermal_priority_pvs = prioritize_names_for_buses(
            res.devices.get("pvsystems") or [], thermal_priority_buses
        )
        planner_offset = max(0, int(state.get("iteration", 0))) * max(1, int(cfg.k_candidates))

        def rotate(items: List[str], offset: int) -> List[str]:
            if not items:
                return []
            pivot = offset % len(items)
            return items[pivot:] + items[:pivot]

        available_pvs = rotate(
            prioritize_names_for_buses(res.devices.get("pvsystems") or [], priority_buses),
            planner_offset,
        )
        available_storages = rotate(
            prioritize_names_for_buses(res.devices.get("storages") or [], priority_buses),
            planner_offset,
        )
        recent = state.get("recent_evals", [])
        forbidden_first = []
        if stuck and cfg.enable_scored_memory:
            # Do not ban an entire control family merely because one setpoint
            # caused a physical regression. OPRO must be able to repair within
            # the same family by changing the target, direction, or magnitude.
            # Reserve family-level bans for schema/admissibility/cyber failures.
            structurally_failed = []
            for item in recent[-10:]:
                failures = [str(mode) for mode in item.get("failure_modes", [])]
                if any(
                    mode.startswith(("schema:", "admissibility:", "cyber:", "action["))
                    for mode in failures
                ):
                    structurally_failed.append(
                        first_family(sanitize_actions(item.get("actions", [])))
                    )
            forbidden_first = [
                name for name in dict.fromkeys(structurally_failed) if name != "none"
            ][:10]
        switchable_all = list(res.devices.get("switchable_lines") or [])
        switch_lookup = {str(name).lower(): str(name) for name in switchable_all}
        configured_ties = [
            switch_lookup[str(name).lower()]
            for name in cfg.restoration_ties
            if str(name).lower() in switch_lookup
        ]
        prioritized_switches = configured_ties + [
            name for name in switchable_all if name not in configured_ties
        ]
        state_summary = {
            "feeder": res.case_label,
            "limits": [state["vmin"], state["vmax"]],
            "current_metrics": met,
            "current_obj": objective(met),
            "security_reference_metrics": state.get("security_reference_metrics") or met,
            "restoration_watch_lines": list(cfg.restoration_watch_lines),
            "restoration_target_loading_pct": cfg.restoration_target_loading_pct,
            "WORST_BUSES": worst,
            "TOP_LINES": top_lines,
            "VOLTAGE_PRIORITY_PVS": voltage_priority_pvs[:20],
            "THERMAL_PRIORITY_PVS": thermal_priority_pvs[:20],
            "telemetry": state.get("telemetry", {}),
            "allow_switch": cfg.allow_switch,
            "allow_var_gen_now": var_now,
            "allow_pv_now": pv_now,
            "allow_load_now": load_now,
            "available_devices": {
                "regcontrols": (res.devices.get("regcontrols") or [])[:40],
                "capacitors": (res.devices.get("capacitors") or [])[:40],
                "switchable_lines": (
                    prioritized_switches or res.devices.get("lines") or []
                )[:60],
                "pvsystems": prioritize_names_for_buses(
                    available_pvs, []
                )[:60],
                "storages": prioritize_names_for_buses(
                    available_storages, []
                )[:60],
                "storage_fleets": {
                    fleet_id: len(members)
                    for fleet_id, members in (cfg.storage_fleets or {}).items()
                },
                "generators": (res.devices.get("generators") or [])[:60],
                "open_switches": [
                    name for name in prioritized_switches
                    if res.line_status.get(str(name).lower()) in {"open", "disabled"}
                ][:60],
                "closed_switches": [
                    name for name in (res.devices.get("switchable_lines") or [])
                    if res.line_status.get(str(name).lower()) == "closed"
                ][:60],
            },
            "reg_map_hint": {key: value for key, value in list(res.reg_map.items())[:24]},
        }
        if cfg.extra_instruction:
            state_summary["extra_instruction"] = cfg.extra_instruction
        prompt = build_meta_prompt(
            task=(
                "Propose switching actions and DER or utility-device setpoints that reduce operating-limit "
                "violations and restore load without weakening topology or cyber-physical consistency."
            ),
            constraints=[
                "Never edit Vsource.*",
                "Use only exact device and bus names from STATE",
                "Do not target quarantined devices",
                "Do not increase source-disconnected load, component count, or cycle rank beyond the declared security reference",
                "Each candidate must contain at least one action",
            ],
            state_summary=state_summary,
            best_so_far=(
                sorted(state.get("best_so_far", []), key=lambda item: item["obj"])[:25]
                if cfg.enable_scored_memory else []
            ),
            recent_evals=(recent if cfg.enable_scored_memory else []),
            stuck=stuck,
            forbidden_first=forbidden_first,
            prefer_utility_first=cfg.prefer_utility_first,
            allow_var_gen_now=var_now,
            allow_pv_now=pv_now,
            allow_load_now=load_now,
            k_candidates=cfg.k_candidates,
            max_actions=cfg.max_actions,
            verification_feedback=(
                (state.get("feedback_history") or [{}])[-1]
                if cfg.enable_verifier_feedback else None
            ),
        )
        if cfg.show_meta_prompt:
            self.meta_prompt_updated(prompt[:12000])
        base_temp = min(0.82, 0.22 + 0.12 * stuck)
        explore = max(0.30, min(0.95, cfg.explore_temp))
        temperatures = [base_temp]
        if cfg.llm_samples > 1:
            temperatures.append(explore)
        temperatures.extend([min(0.95, explore + 0.10)] * max(0, cfg.llm_samples - 2))
        candidates: List[Dict[str, Any]] = []
        response_samples: List[Dict[str, Any]] = []
        llm_candidate_objects_returned = 0
        llm_parse_valid_candidates = 0
        llm_temperatures = temperatures if cfg.enable_llm_candidates else []
        for sample, temperature in enumerate(llm_temperatures):
            raw = self.llm.chat(
                system=(
                    "You are the planning node in GridGuard, an OPRO derivative-free optimizer. "
                    "Return one strict JSON object and no surrounding text. "
                    "Treat verification feedback as binding evidence."
                ),
                user_text=prompt,
                temperature=temperature,
                num_predict=(
                    min(1400, 320 + 220 * max(1, int(cfg.k_candidates)))
                    if cfg.fast_llm else 1600
                ),
                response_format="json",
            )
            response_samples.append({
                "sample": sample,
                "temperature": temperature,
                "response_excerpt": raw[:4000],
            })
            parsed = parse_llm_json(raw) or {}
            parsed_candidates = (
                parsed.get("candidates", [])
                if isinstance(parsed.get("candidates", []), list) else []
            )
            llm_candidate_objects_returned += len(parsed_candidates)
            for candidate_index, candidate in enumerate(parsed_candidates):
                if not isinstance(candidate, dict):
                    continue
                actions = sanitize_actions(candidate.get("actions", []))
                if not actions:
                    continue
                llm_parse_valid_candidates += 1
                candidate = dict(candidate)
                candidate_name = str(candidate.get("name") or "").strip()
                if candidate_name.lower() in {"", "...", "candidate", "string", "name"}:
                    candidate_name = (
                        f"{getattr(self.llm, 'candidate_source', 'LLM')}_"
                        f"{state['iteration']}_{sample}_{candidate_index}"
                    )
                candidate["name"] = candidate_name[:80]
                candidate["source"] = getattr(self.llm, "candidate_source", "LLM")
                candidate["actions"] = actions
                candidate["reasoning"] = str(candidate.get("reasoning", ""))[:400]
                candidates.append(candidate)
        # Respect the configured simulation budget.  The previous minimum of
        # twelve candidates made one SMART-DS iteration unexpectedly require
        # dozens of full 154k-bus recompiles even when k_candidates was small.
        candidate_budget = max(1, min(60, int(cfg.k_candidates)))
        allocated_slots = (
            candidate_budget
            if cfg.enable_llm_candidates or cfg.enable_physics_fallback or cfg.enable_portfolio_seeds
            else 0
        )
        candidates = pick_diverse_subset(dedup_candidates(candidates), candidate_budget)
        portfolio_pool = (
            dedup_candidates(pv_portfolio_candidates(
                res, state["vmin"], state["vmax"], cfg.max_actions
            ))
            if cfg.enable_portfolio_seeds else []
        )
        repair_pool = (
            dedup_candidates(list(state.get("repair_candidates", [])))
            if cfg.enable_physics_fallback else []
        )
        restoration_pool = (
            dedup_candidates(repair_pool + restoration_seed_candidates(res, cfg))
            if cfg.enable_physics_fallback and cfg.restoration_ties else []
        )
        use_physics = cfg.enable_physics_fallback and (
            stuck >= cfg.guardrail_start_stuck or not candidates
        )
        expanded_pool = list(candidates)
        if use_physics:
            expanded_pool.extend(restoration_pool)
            expanded_pool.extend(physics_candidates(
                res, state["vmin"], state["vmax"], cfg.allow_var_gen, cfg.allow_pv,
                cfg.allow_load, cfg.max_actions
            ))
        # Reserve one configured simulation slot for a broad, catalog-grounded
        # PV bundle whenever the budget permits. A budget of at least three
        # reserves the two evidence-ranked exact-catalog seeds, leaving at least
        # one slot for the LLM. With k=1, switch to a bundle after the first
        # rejected iteration instead of repeatedly simulating an LLM singleton.
        # max_actions=1 retains the original behavior.
        portfolio_supplemented = False
        restoration_supplemented = False
        if restoration_pool:
            reserve_count = min(
                len(restoration_pool),
                candidate_budget if not candidates else max(1, candidate_budget - 1),
            )
            # A repair candidate is a response to the preceding verifier
            # batch, so give it first access to a normal candidate slot. It is
            # not simulated outside or in addition to the configured budget.
            start = (
                0 if repair_pool
                else int(state.get("iteration", 0)) % len(restoration_pool)
            )
            restores = [
                restoration_pool[(start + offset) % len(restoration_pool)]
                for offset in range(reserve_count)
            ]
            restore_keys = {
                candidate_bundle_fingerprint(candidate) for candidate in restores
            }
            remaining = [
                candidate for candidate in dedup_candidates(expanded_pool)
                if candidate_bundle_fingerprint(candidate) not in restore_keys
            ]
            candidates = restores + pick_diverse_subset(
                remaining, max(0, candidate_budget - len(restores))
            )
            restoration_supplemented = True
        elif portfolio_pool and (candidate_budget > 1 or stuck > 0 or not candidates):
            reserve_count = min(
                len(portfolio_pool), 2 if candidate_budget >= 3 else 1
            )
            start = int(state.get("iteration", 0)) % len(portfolio_pool)
            portfolios = [
                portfolio_pool[(start + offset) % len(portfolio_pool)]
                for offset in range(reserve_count)
            ]
            portfolio_keys = {
                tuple(_action_dedup_key(action) for action in portfolio["actions"])
                for portfolio in portfolios
            }
            remaining = [
                candidate for candidate in dedup_candidates(expanded_pool)
                if tuple(
                    _action_dedup_key(action)
                    for action in sanitize_actions(candidate.get("actions", []))
                ) not in portfolio_keys
            ]
            candidates = portfolios + pick_diverse_subset(
                remaining, max(0, candidate_budget - len(portfolios))
            )
            portfolio_supplemented = True
        else:
            candidates = pick_diverse_subset(
                dedup_candidates(expanded_pool), candidate_budget
            )
        operating_state_id = str(
            state.get("operating_state_id")
            or operating_state_fingerprint(state.get("state_cmds", []))
        )
        candidates, historical_duplicates = filter_previously_evaluated_candidates(
            candidates,
            state.get("evaluated_fingerprints", {}),
            operating_state_id,
        )
        # Filtering happens after the reservation policy, then backfills from
        # the already-built pools so old bundles cannot consume simulation
        # slots or starve unseen physics/LLM alternatives.
        if len(candidates) < candidate_budget:
            selected_fingerprints = {
                candidate_bundle_fingerprint(candidate) for candidate in candidates
            }
            refill_pool = [
                candidate for candidate in dedup_candidates(
                    restoration_pool + portfolio_pool + expanded_pool
                )
                if candidate_bundle_fingerprint(candidate) not in selected_fingerprints
            ]
            novel_refill, repeated_refill = filter_previously_evaluated_candidates(
                refill_pool,
                state.get("evaluated_fingerprints", {}),
                operating_state_id,
            )
            candidates.extend(pick_diverse_subset(
                novel_refill, candidate_budget - len(candidates)
            ))
            duplicate_by_fingerprint = {
                item["fingerprint"]: item
                for item in historical_duplicates + repeated_refill
            }
            historical_duplicates = list(duplicate_by_fingerprint.values())
        self.progress(
            f"[GridGuard] Iteration {state['iteration']}: planner proposed {len(candidates)} candidates "
            f"after filtering {len(historical_duplicates)} prior bundles "
            f"(physics fallback={use_physics}, PV portfolio={portfolio_supplemented}, "
            f"restoration portfolio={restoration_supplemented})."
        )
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        prompt_snapshot = {
            "iteration": state["iteration"],
            "role": "OPRO Planner Agent",
            "model": self.llm.model,
            "prompt_sha256": prompt_hash,
            "prompt_excerpt": prompt[:16000],
            "response_samples": response_samples,
            "candidate_count": len(candidates),
            "historical_duplicates_filtered": len(historical_duplicates),
            "physics_fallback_used": use_physics,
            "physics_portfolio_supplemented": portfolio_supplemented,
            "restoration_portfolio_supplemented": restoration_supplemented,
            "adaptive_restoration_repairs": len(repair_pool),
            "ablation": {
                "llm_candidates": cfg.enable_llm_candidates,
                "physics_fallback": cfg.enable_physics_fallback,
                "portfolio_seeds": cfg.enable_portfolio_seeds,
                "scored_memory": cfg.enable_scored_memory,
                "verifier_feedback": cfg.enable_verifier_feedback,
                "critic": cfg.enable_critic,
            },
        }
        trace = list(state.get("agent_trace", [])) + [{
            "iteration": state["iteration"],
            "node": "plan",
            "role": "OPRO Planner Agent",
            "actor_type": getattr(self.llm, "actor_type", "llm"),
            "model": self.llm.model,
            "prompt_sha256": prompt_hash,
            "input_memory_items": len(state.get("best_so_far", [])) + len(recent),
            "output_candidates": len(candidates),
            "historical_duplicates_filtered": len(historical_duplicates),
            "physics_fallback_used": use_physics,
            "physics_portfolio_supplemented": portfolio_supplemented,
            "restoration_portfolio_supplemented": restoration_supplemented,
            "adaptive_restoration_repairs": len(repair_pool),
            "latency_ms": round((time.perf_counter() - started) * 1000.0, 1),
            "route": "verify",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        }]
        return {
            "candidate_actions": candidates,
            "repair_candidates": [],
            "candidate_slots_allocated": int(state.get("candidate_slots_allocated", 0)) + allocated_slots,
            "llm_candidate_objects_returned": int(
                state.get("llm_candidate_objects_returned", 0)
            ) + llm_candidate_objects_returned,
            "llm_parse_valid_candidates": int(
                state.get("llm_parse_valid_candidates", 0)
            ) + llm_parse_valid_candidates,
            "historical_duplicates_filtered": int(
                state.get("historical_duplicates_filtered", 0)
            ) + len(historical_duplicates),
            "meta_prompt_snapshots": state.get("meta_prompt_snapshots", []) + [prompt_snapshot],
            "agent_trace": trace,
        }

    def verification_node(self, state: GridGuardState) -> Dict[str, Any]:
        started = time.perf_counter()
        cfg = self.config
        telemetry, validation_time = prepare_telemetry_validation_batch(
            state.get("telemetry", {})
        )
        validation_state = dict(state)
        validation_state["telemetry"] = telemetry
        res = state["current_snapshot"]
        current = state["current_metrics"]
        security_reference = state.get("security_reference_metrics") or current
        security_reference_snapshot = state.get("security_reference_snapshot") or res
        current_score = objective(current)
        var_now, pv_now, load_now = self._gates(state)
        results: List[Dict[str, Any]] = []
        recent = list(state.get("recent_evals", []))
        outputs = list(state.get("simulation_outputs", []))
        best_archive = list(state.get("best_so_far", []))
        invalid_count = 0
        certified_count = 0
        operating_state_id = str(
            state.get("operating_state_id")
            or operating_state_fingerprint(state.get("state_cmds", []))
        )
        evaluated_fingerprints = dict(state.get("evaluated_fingerprints", {}))

        for candidate in state.get("candidate_actions", [])[:max(1, min(60, int(cfg.k_candidates)))]:
            candidate_started = time.perf_counter()
            name = str(candidate.get("name", "candidate"))[:80]
            proposed_actions = sanitize_actions(candidate.get("actions", []))
            bundle_fingerprint = candidate_bundle_fingerprint(proposed_actions)
            memory_key = evaluated_fingerprint_key(operating_state_id, bundle_fingerprint)
            if memory_key in evaluated_fingerprints:
                record = {
                    "iteration": state["iteration"], "name": name,
                    "operating_state_id": operating_state_id,
                    "source": str(candidate.get("source", "LLM")),
                    "actions": proposed_actions, "fingerprint": bundle_fingerprint,
                    "reasoning": str(candidate.get("reasoning", ""))[:400],
                    "failure_modes": ["planner:historical_duplicate_filtered"],
                    "certified": False, "obj": 1e30, "simulated": False,
                }
                record["evaluation_latency_ms"] = round(
                    (time.perf_counter() - candidate_started) * 1000.0, 3
                )
                invalid_count += 1
                recent.append(record)
                results.append(record)
                continue
            grounding_errors: List[str] = []
            if len(proposed_actions) > cfg.max_actions:
                grounding_errors.append(
                    f"schema:supervisory_action_budget_exceeded:{len(proposed_actions)}>{cfg.max_actions}"
                )
            grounded_actions, grounding_records, expansion_errors = ground_supervisory_actions(
                validation_state, proposed_actions, cfg
            )
            grounding_errors.extend(expansion_errors)
            actions, validation_errors = validate_candidate_actions(
                validation_state, grounded_actions, cfg, var_now, pv_now, load_now,
                validation_time=validation_time,
                action_limit=cfg.max_physical_actions,
            )
            errors = grounding_errors + validation_errors
            record: Dict[str, Any] = {
                "iteration": state["iteration"], "name": name,
                "operating_state_id": operating_state_id,
                "source": str(candidate.get("source", "LLM")), "actions": actions,
                "supervisory_actions": proposed_actions,
                "repair_derivation": candidate.get("repair_derivation"),
                "grounding_expansions": grounding_records,
                "supervisory_action_count": len(proposed_actions),
                "physical_action_count": len(actions),
                "fingerprint": bundle_fingerprint,
                "reasoning": str(candidate.get("reasoning", ""))[:400],
                "failure_modes": list(errors), "certified": False, "obj": 1e30,
                "simulated": False,
            }
            if errors:
                record["evaluation_latency_ms"] = round(
                    (time.perf_counter() - candidate_started) * 1000.0, 3
                )
                invalid_count += 1
                evaluated_fingerprints[memory_key] = _evaluated_memory_record(record)
                recent.append({key: value for key, value in record.items() if key != "snapshot"})
                results.append(record)
                continue

            commands, notes = self.translator.actions_to_cmds(
                res, actions, cfg.allow_switch, cfg.allow_pv, cfg.allow_load,
                cfg.allow_var_gen, cfg.max_physical_actions
            )
            if notes or len(commands) != len(actions):
                record["failure_modes"].extend([f"admissibility:{note}" for note in notes] or ["admissibility:partial_translation"])
                record["evaluation_latency_ms"] = round(
                    (time.perf_counter() - candidate_started) * 1000.0, 3
                )
                invalid_count += 1
                evaluated_fingerprints[memory_key] = _evaluated_memory_record(record)
                recent.append({key: value for key, value in record.items() if key != "snapshot"})
                results.append(record)
                continue

            merged = merge_state_cmds(state.get("state_cmds", []), commands)
            simulation_started = time.perf_counter()
            try:
                trial = compile_and_solve(
                    state["case"]["label"], state["case"]["folder"], state["case"]["main_dss"],
                    state.get("base_cmds", []) + merged, state["vmin"], state["vmax"],
                    recover_on_failure=cfg.allow_recovered_solve,
                )
                actuation_readback, actuation_errors = verify_post_solve_actuation(
                    actions, res
                )
                record["actuation_readback"] = actuation_readback
                record["failure_modes"].extend(actuation_errors)
                metrics = summarize_metrics(trial, state["vmin"], state["vmax"])
                burden = action_burden(actions)
                for field, delta in burden.items():
                    metrics[field] = float(current.get(field, 0.0)) + float(delta)
                switch_count = sum(_normalize_type(action.get("type")) == "switch_line" for action in actions)
                metrics["switching_effort"] = int(state.get("switching_effort", 0)) + switch_count
                record["simulated"] = True
                record["simulation_latency_ms"] = round(
                    (time.perf_counter() - simulation_started) * 1000.0, 3
                )
                score = objective(metrics)
                reference_voltage_violations = {
                    str(row.get("bus", "")).lower()
                    for _, row in security_reference_snapshot.bus_df.iterrows()
                    if bool(row.get("violation", False))
                }
                trial_voltage_violations = {
                    str(row.get("bus", "")).lower()
                    for _, row in trial.bus_df.iterrows()
                    if bool(row.get("violation", False))
                }
                new_voltage_violations = sorted(
                    trial_voltage_violations - reference_voltage_violations
                )
                reference_line_loading = {
                    str(row.get("line", "")).lower(): float(row.get("%norm"))
                    for _, row in security_reference_snapshot.line_df.iterrows()
                    if _finite_number(row.get("%norm"))
                }
                new_line_overloads: List[str] = []
                for _, row in trial.line_df.iterrows():
                    name_key = str(row.get("line", "")).lower()
                    loading = row.get("%norm")
                    if not _finite_number(loading):
                        continue
                    reference_loading = reference_line_loading.get(name_key)
                    if (
                        reference_loading is not None
                        and reference_loading <= 100.0 + cfg.max_line_loading_tolerance_pct
                        and float(loading) > 100.0 + cfg.max_line_loading_tolerance_pct
                    ):
                        new_line_overloads.append(str(row.get("line", "")))
                line_loading_evidence, missing_watch_lines = _line_loading_evidence(
                    trial, security_reference_snapshot, cfg.restoration_watch_lines
                )
                topology_ok = (
                    metrics["source_disconnected_loads"]
                    <= security_reference.get("source_disconnected_loads", 0)
                    and metrics["network_components"]
                    <= security_reference.get("network_components", 0)
                    and metrics["network_cycle_rank"]
                    <= security_reference.get("network_cycle_rank", 0)
                )
                restoration_target = max(
                    float(current.get("served_load_kw", 0.0)),
                    float(security_reference.get("served_load_kw", 0.0)),
                )
                restoration_ok = bool(
                    metrics["served_load_kw"] + cfg.restoration_tolerance_kw
                    >= restoration_target
                )
                voltage_ok = (
                    metrics["viol_buses"] <= security_reference.get("viol_buses", 0)
                    and metrics["v_severity"]
                    <= security_reference.get("v_severity", 0.0)
                    + cfg.voltage_severity_tolerance_pu
                    and not new_voltage_violations
                )
                thermal_ceiling = max(
                    100.0, float(security_reference.get("max_line_pct") or 0.0)
                )
                trial_loading = float(metrics.get("max_line_pct") or 0.0)
                thermal_ok = bool(
                    metrics["over_lines"] <= security_reference.get("over_lines", 0)
                    and trial_loading
                    <= thermal_ceiling + cfg.max_line_loading_tolerance_pct
                    and float(metrics.get("thermal_severity_pct_sum", 0.0))
                    <= float(security_reference.get("thermal_severity_pct_sum", 0.0))
                    + cfg.thermal_severity_tolerance_pct_sum
                    and not new_line_overloads
                )
                coverage_ok = bool(
                    float(metrics.get("bus_voltage_coverage_rate", 0.0)) + 1e-12
                    >= float(security_reference.get("bus_voltage_coverage_rate", 0.0))
                    and float(metrics.get("line_loading_coverage_rate", 0.0)) + 1e-12
                    >= float(security_reference.get("line_loading_coverage_rate", 0.0))
                )
                if not metrics["converged"]:
                    record["failure_modes"].append("physics:power_flow_not_converged")
                if trial.recovery_applied and not cfg.allow_recovered_solve:
                    record["failure_modes"].append("physics:undeclared_solver_recovery")
                if not topology_ok:
                    record["failure_modes"].append("topology:islanding_or_loop_regression")
                if not restoration_ok:
                    record["failure_modes"].append("restoration:served_load_decreased")
                if not voltage_ok:
                    record["failure_modes"].append("security:voltage_regression")
                if not thermal_ok:
                    record["failure_modes"].append("security:thermal_regression")
                if not coverage_ok:
                    record["failure_modes"].append("observability:measurement_coverage_regression")
                if missing_watch_lines:
                    record["failure_modes"].append(
                        "observability:watched_line_loading_unavailable:"
                        + ",".join(missing_watch_lines[:6])
                    )
                if score >= current_score - 1e-6:
                    record["failure_modes"].append("objective:no_improvement")
                relative_safe_improvement = not record["failure_modes"]
                absolute_operating_limits_satisfied = operating_goal_satisfied(metrics)
                absolute_feasible = bool(
                    absolute_operating_limits_satisfied and topology_ok and coverage_ok
                )
                if cfg.certificate_mode == "absolute_feasible" and not absolute_feasible:
                    record["failure_modes"].append("certificate:absolute_constraints_unsatisfied")
                record.update({
                    "commands": commands, "merged_commands": merged, "metrics": metrics,
                    "obj": float(score), "snapshot": trial,
                    "certificate_mode": cfg.certificate_mode,
                    "security_reference": (
                        "declared_precontingency_envelope"
                        if state.get("security_reference_metrics") else "current_operating_state"
                    ),
                    "relative_safe_improvement": relative_safe_improvement,
                    "absolute_operating_limits_satisfied": absolute_operating_limits_satisfied,
                    "topology_reference_preserved": topology_ok,
                    "measurement_coverage_preserved": coverage_ok,
                    "new_voltage_violation_count": len(new_voltage_violations),
                    "new_voltage_violations": new_voltage_violations[:30],
                    "new_line_overload_count": len(new_line_overloads),
                    "new_line_overloads": new_line_overloads[:30],
                    "line_loading_evidence": line_loading_evidence,
                    "missing_restoration_watch_lines": missing_watch_lines,
                    "absolute_feasible": absolute_feasible,
                    "certified": not record["failure_modes"],
                })
                if record["certified"]:
                    certified_count += 1
                outputs.append({
                    "iteration": state["iteration"], "candidate": name,
                    "metrics": metrics, "score": float(score), "certified": record["certified"],
                })
                best_archive.append({
                    "obj": float(score), "metrics": metrics,
                    "certified": bool(record["certified"]),
                    "status": "certified" if record["certified"] else "rejected",
                    "failure_modes": list(record["failure_modes"]),
                    "fingerprint": bundle_fingerprint,
                    "solution": {
                        "name": name, "source": record["source"],
                        "delta_cmds": commands, "delta_actions": actions,
                        "certified": bool(record["certified"]),
                    },
                })
            except Exception as exc:
                record["failure_modes"].append(f"physics:apply_error:{str(exc)[:160]}")
                record["simulation_latency_ms"] = round(
                    (time.perf_counter() - simulation_started) * 1000.0, 3
                )
            record["evaluation_latency_ms"] = round(
                (time.perf_counter() - candidate_started) * 1000.0, 3
            )
            evaluated_fingerprints[memory_key] = _evaluated_memory_record(record)
            recent.append({key: value for key, value in record.items() if key not in {"snapshot", "merged_commands"}})
            results.append(record)

        recent = recent[-100:]
        best_archive = sorted(best_archive, key=lambda item: item["obj"])[:30]
        certified = [record for record in results if record.get("certified")]
        pending = min(certified, key=lambda item: item["obj"]) if certified else {}
        rejected = len(results) - len(certified)
        self.progress(
            f"[GridGuard] Verification: {len(certified)}/{len(results)} candidates certified; "
            f"{invalid_count} rejected before simulation."
        )
        route = "accept" if pending else "repair"
        trace = list(state.get("agent_trace", [])) + [{
            "iteration": state["iteration"],
            "node": "verify",
            "role": "Physics and Certificate Team",
            "actor_type": "deterministic",
            "input_candidates": len(results),
            "simulated_candidates": len(results) - invalid_count,
            "certified_candidates": len(certified),
            "rejected_candidates": rejected,
            "invalid_before_simulation": invalid_count,
            "latency_ms": round((time.perf_counter() - started) * 1000.0, 1),
            "route": route,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        }]
        public_batch = [
            {key: value for key, value in item.items() if key not in {"snapshot", "merged_commands"}}
            for item in results
        ]
        return {
            "telemetry": telemetry,
            "verification_results": results,
            "evaluation_history": state.get("evaluation_history", []) + public_batch,
            "pending_accept": pending,
            "recent_evals": recent,
            "simulation_outputs": outputs,
            "best_so_far": best_archive,
            "operating_state_id": operating_state_id,
            "evaluated_fingerprints": evaluated_fingerprints,
            "total_candidates": int(state.get("total_candidates", 0)) + len(results),
            "certified_candidates": int(state.get("certified_candidates", 0)) + certified_count,
            "invalid_candidates": int(state.get("invalid_candidates", 0)) + invalid_count,
            "rejected_candidates": int(state.get("rejected_candidates", 0)) + rejected,
            "agent_trace": trace,
            "route": route,
        }

    def repair_node(self, state: GridGuardState) -> Dict[str, Any]:
        counts: Dict[str, int] = {}
        for result in state.get("verification_results", []):
            for mode in result.get("failure_modes", []):
                parts = str(mode).split(":")
                family = parts[0]
                if family.startswith("action[") and len(parts) > 1:
                    detail = parts[1]
                    if any(token in detail for token in ("inadmissible", "not_admissible", "unknown_")):
                        family = "admissibility"
                    elif any(token in detail for token in ("bad_", "out_of_range", "unsafe_", "conflicting_")):
                        family = "schema"
                    else:
                        family = "action"
                counts[family] = counts.get(family, 0) + 1
        if not state.get("verification_results"):
            counts["planner_output"] = 1
        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        derived_repairs = derive_restoration_secant_candidates(
            list(state.get("recent_evals", [])),
            self.config,
            str(
                state.get("operating_state_id")
                or operating_state_fingerprint(state.get("state_cmds", []))
            ),
        )
        feedback = {
            "iteration": state["iteration"],
            "summary": (
                "Planner returned no novel parseable candidate. Rotate to unused exact targets and setpoints."
                if not state.get("verification_results")
                else "Verifier evidence produced a bounded watch-line secant repair."
                if derived_repairs
                else "No candidate passed every certification gate."
            ),
            "failure_counts": dict(ranked),
            "repair_instruction": (
                "Allocate a normal candidate slot to the recorded secant repair, then verify every gate."
                if derived_repairs
                else "Change the failed device or action family and address the listed gate. "
                "Use measured state values and exact admissible names."
            ),
            "derived_repair_candidates": derived_repairs,
            "examples": [
                {
                    "candidate": item.get("name"),
                    "source": item.get("source"),
                    "actions": (
                        item.get("supervisory_actions")
                        or item.get("actions") or []
                    )[:4],
                    "failures": item.get("failure_modes", [])[:4],
                    "line_loading_evidence": (
                        item.get("line_loading_evidence") or []
                    )[:6],
                    "metrics": {
                        key: (item.get("metrics") or {}).get(key)
                        for key in (
                            "viol_buses", "v_severity", "over_lines", "max_line_pct",
                            "thermal_severity_pct_sum", "losses_kw", "cumulative_control_effort",
                        )
                    },
                }
                for item in state.get("verification_results", [])[:5]
            ],
        }
        iteration = int(state.get("iteration", 0)) + 1
        stuck = int(state.get("stuck", 0)) + 1
        self.progress(f"[GridGuard] Repair/reflection feedback: {feedback['failure_counts']}")
        should_stop = iteration >= self.config.steps or stuck >= self.config.max_stuck
        next_route = (
            "finalize" if should_stop
            else "critic" if self.config.enable_critic
            else "plan"
        )
        trace = list(state.get("agent_trace", [])) + [{
            "iteration": state["iteration"],
            "node": "repair",
            "role": "Failure Taxonomy Agent",
            "actor_type": "deterministic",
            "failure_counts": feedback["failure_counts"],
            "derived_repair_candidates": len(derived_repairs),
            "derivation_methods": sorted({
                str((item.get("repair_derivation") or {}).get("method", ""))
                for item in derived_repairs
                if item.get("repair_derivation")
            }),
            "route": next_route,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        }]
        return {
            "feedback_history": state.get("feedback_history", []) + [feedback],
            "repair_candidates": derived_repairs,
            "agent_trace": trace,
            "iteration": iteration,
            "stuck": stuck,
            "route": next_route,
        }

    def critic_node(self, state: GridGuardState) -> Dict[str, Any]:
        """Use a separate, non-authoritative LLM role to turn failures into repair guidance."""
        started = time.perf_counter()
        feedback_history = list(state.get("feedback_history", []))
        if not feedback_history:
            return {"agent_trace": state.get("agent_trace", [])}
        base_feedback = dict(feedback_history[-1])
        current = state.get("current_metrics", {})
        payload = {
            "current_metrics": {
                "violating_buses": current.get("viol_buses"),
                "voltage_severity": current.get("v_severity"),
                "overloaded_lines": current.get("over_lines"),
                "served_load_kw": current.get("served_load_kw"),
                "isolated_loads": current.get("isolated_loads"),
                "network_cycle_rank": current.get("network_cycle_rank"),
            },
            "failure_summary": {
                "failure_counts": base_feedback.get("failure_counts", {}),
                "examples": base_feedback.get("examples", [])[:3],
                "derived_repair_candidates": base_feedback.get(
                    "derived_repair_candidates", []
                )[:3],
            },
            "available_devices": {
                "regcontrols": (state.get("admissible_controls", {}).get("regcontrols") or [])[:30],
                "capacitors": (state.get("admissible_controls", {}).get("capacitors") or [])[:30],
                "switchable_lines": (state.get("admissible_controls", {}).get("switchable_lines") or [])[:30],
                "pvsystems": (state.get("admissible_controls", {}).get("pvsystems") or [])[:30],
                "storages": (state.get("admissible_controls", {}).get("storages") or [])[:30],
                "storage_fleets": [
                    {"fleet": fleet_id, "device_count": len(members)}
                    for fleet_id, members in list((self.config.storage_fleets or {}).items())[:20]
                ],
                "generators": (state.get("admissible_controls", {}).get("generators") or [])[:30],
            },
            "allowed_focus_families": [
                "tap_step", "cap_state", "switch_line", "der_setpoint",
                "storage_setpoint", "create_var_gen", "create_pv", "create_load",
            ],
            "instruction": (
                "Diagnose the binding failures and recommend the next device or action family to explore. "
                "Preserve directions that improved some metrics, but change exact target, magnitude, or bundle "
                "to correct the failed gate. Do not certify, apply, or invent an action. Keep every string under 30 words."
            ),
            "output_format": {
                "diagnosis": "short evidence-grounded statement",
                "avoid": ["failed pattern"],
                "next_focus": ["admissible family or exact device"],
                "repair_instruction": "one binding instruction for the planner",
            },
        }
        raw = self.llm.chat(
            system=(
                "You are the GridGuard Constraint Critic Agent. You analyze verifier evidence but have no "
                "authority to approve or apply grid actions. Use only supplied values and exact device names. "
                "Return one strict JSON object and no surrounding text, using at most 120 words total."
            ),
            user_text="<JSON>" + json.dumps(payload) + "</JSON>",
            temperature=0.05,
            num_predict=420 if self.config.fast_llm else 700,
            response_format="json",
        )
        parsed = parse_llm_json(raw) or {}
        controls = state.get("admissible_controls", {}) or {}
        regcontrols = list(controls.get("regcontrols") or [])
        capacitors = list(controls.get("capacitors") or [])
        switchable_lines = list(controls.get("switchable_lines") or [])
        pvsystems = list(controls.get("pvsystems") or [])
        storages = list(controls.get("storages") or [])
        generators = list(controls.get("generators") or [])
        allowed_focus: set[str] = set()
        if regcontrols:
            allowed_focus.update({"tap_step", "regcontrols", *regcontrols})
        if capacitors:
            allowed_focus.update({"cap_state", "capacitors", *capacitors})
        if self.config.allow_switch and switchable_lines:
            allowed_focus.update({"switch_line", "switchable_lines", *switchable_lines})
        if pvsystems or generators:
            allowed_focus.update({"der_setpoint", "pvsystems", "generators", *pvsystems, *generators})
        if storages:
            allowed_focus.update({"storage_setpoint", "storages", *storages})
        if self.config.storage_fleets:
            allowed_focus.update({
                "storage_fleet_setpoint", "storage_fleets",
                *self.config.storage_fleets.keys(),
            })
        stuck = int(state.get("stuck", 0))
        if self.config.allow_var_gen and (not self.config.prefer_utility_first or stuck >= self.config.vargen_after_stuck):
            allowed_focus.add("create_var_gen")
        if self.config.allow_pv and (not self.config.prefer_utility_first or stuck >= self.config.pv_after_stuck):
            allowed_focus.add("create_pv")
        if self.config.allow_load and (not self.config.prefer_utility_first or stuck >= self.config.load_after_stuck):
            allowed_focus.add("create_load")
        focus_raw = parsed.get("next_focus", [])
        if isinstance(focus_raw, str):
            focus_raw = [focus_raw]
        elif not isinstance(focus_raw, list):
            focus_raw = []
        canonical_focus = {str(item).lower(): str(item) for item in allowed_focus}
        next_focus: List[str] = []
        for item in focus_raw:
            if not isinstance(item, str):
                continue
            raw_item = item.strip()
            lowered = raw_item.lower()
            match = canonical_focus.get(lowered)
            if match is None:
                # Small local models often wrap an exact token in phrases such
                # as "storage_setpoint on storage_x". Recover only tokens that
                # are already in the deterministic allowlist; invented names
                # remain discarded.
                matches = [
                    canonical for token, canonical in canonical_focus.items()
                    if token and re.search(rf"(?<![A-Za-z0-9_.-]){re.escape(token)}(?![A-Za-z0-9_.-])", lowered)
                ]
                if matches:
                    match = max(matches, key=len)
            if match is not None and match not in next_focus:
                next_focus.append(match[:80])
            if len(next_focus) >= 6:
                break
        parsed_json_valid = bool(parsed)
        repair_text = str(parsed.get("repair_instruction", ""))[:500]
        guidance_promoted = bool(repair_text and next_focus)
        critic_record = {
            "role": "Constraint Critic Agent",
            "model": self.llm.model,
            "diagnosis": str(parsed.get("diagnosis", ""))[:500],
            "avoid": [str(item)[:120] for item in parsed.get("avoid", []) if isinstance(item, str)][:6],
            "next_focus": next_focus,
            "repair_instruction": repair_text,
            "raw_response_excerpt": raw[:2400],
            "parsed_json_valid": parsed_json_valid,
            "guidance_promoted": guidance_promoted,
            "authority": "advisory_only",
        }
        if guidance_promoted:
            base_feedback["repair_instruction"] = critic_record["repair_instruction"]
        base_feedback["critic_agent"] = critic_record
        feedback_history[-1] = base_feedback
        self.progress(
            f"[GridGuard] Critic agent returned parsed_json_valid={parsed_json_valid} "
            f"next_focus={critic_record['next_focus']}"
        )
        trace = list(state.get("agent_trace", [])) + [{
            "iteration": state["iteration"],
            "node": "critic",
            "role": "Constraint Critic Agent",
            "actor_type": "llm",
            "model": self.llm.model,
            "parsed_json_valid": parsed_json_valid,
            "guidance_promoted": guidance_promoted,
            "latency_ms": round((time.perf_counter() - started) * 1000.0, 1),
            "route": "plan",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        }]
        return {"feedback_history": feedback_history, "agent_trace": trace, "route": "plan"}

    def accept_node(self, state: GridGuardState) -> Dict[str, Any]:
        chosen = state["pending_accept"]
        before = state["current_metrics"]
        after = dict(chosen["metrics"])
        actions = chosen.get("actions", [])
        switch_count = sum(_normalize_type(action.get("type")) == "switch_line" for action in actions)
        iteration = int(state.get("iteration", 0)) + 1
        teaching = ""
        if self.config.teaching_notes:
            teaching = self.llm.chat(
                system=(
                    "Explain a certified distribution-grid control action to an operator. "
                    "Use only the supplied actions, checks, and measurements. Do not invent values."
                ),
                user_text=json.dumps({
                    "candidate": chosen["name"], "actions": actions,
                    "before": before, "after": after,
                    "passed_checks": [
                        "device admissibility", "telemetry consistency", "post-solve actuation readback",
                        "power-flow convergence",
                        "topology preservation", "restoration preservation", "operating-limit non-regression",
                        "objective improvement",
                    ],
                }),
                temperature=0.20,
                num_predict=300,
            )
        record = {
            "step": state["iteration"], "picked": chosen["name"], "source": chosen["source"],
            "applied_cmds": chosen["commands"], "actions": actions, "before": before, "after": after,
            "supervisory_actions": chosen.get("supervisory_actions", []),
            "repair_derivation": chosen.get("repair_derivation"),
            "line_loading_evidence": chosen.get("line_loading_evidence", []),
            "obj": chosen["obj"], "certified": True,
            "certificate": {
                "device_admissible": True, "cyber_consistent": True,
                "post_solve_actuation_verified": True,
                "actuation_readback": chosen.get("actuation_readback", []),
                "power_flow_converged": True,
                "topology_preserved": True, "restoration_preserved": True,
                "voltage_not_worse": True, "thermal_not_worse": True, "objective_improved": True,
            },
            "teaching": teaching,
        }
        self.step_done(record)
        self.progress(
            f"[GridGuard] Accepted certified candidate {chosen['name']} at iteration {state['iteration']} "
            f"with score {chosen['obj']:.3e}."
        )
        telemetry = dict(state.get("telemetry", {}))
        telemetry["expected_topology_hash"] = chosen["snapshot"].topology_hash
        telemetry["timestamp_utc"] = datetime.now(timezone.utc).isoformat()
        violations = state.get("violation_summaries", []) + [after]
        goal = operating_goal_satisfied(after)
        should_stop = goal or iteration >= self.config.steps
        trace = list(state.get("agent_trace", []))
        if self.config.teaching_notes:
            trace.append({
                "iteration": state["iteration"],
                "node": "explain",
                "role": "Operator Explanation Agent",
                "actor_type": "llm",
                "model": self.llm.model,
                "authority": "explanation_only",
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            })
        trace.append({
            "iteration": state["iteration"],
            "node": "accept",
            "role": "Certificate Commit Agent",
            "actor_type": "deterministic",
            "candidate": chosen["name"],
            "certificate": record["certificate"],
            "route": "finalize" if should_stop else "plan",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        })
        return {
            "state_cmds": chosen["merged_commands"],
            "operating_state_id": operating_state_fingerprint(chosen["merged_commands"]),
            "current_snapshot": chosen["snapshot"],
            "current_metrics": after,
            "telemetry": telemetry,
            "admissible_controls": chosen["snapshot"].devices,
            "violation_summaries": violations,
            "history": state.get("history", []) + [record],
            "iteration": iteration,
            "stuck": 0,
            "switching_effort": int(state.get("switching_effort", 0)) + switch_count,
            "first_certified_iteration": state.get("first_certified_iteration") or iteration,
            "agent_trace": trace,
            "route": "finalize" if should_stop else "plan",
        }

    def finalize_node(self, state: GridGuardState) -> Dict[str, Any]:
        baseline = state["baseline_metrics"]
        final = state["current_metrics"]
        security_reference = state.get("security_reference_metrics") or baseline
        baseline_snapshot = state["baseline_snapshot"]
        final_snapshot = state["current_snapshot"]
        restored_load_kw = 0.0
        for name, base_status in baseline_snapshot.load_status_kw.items():
            final_status = final_snapshot.load_status_kw.get(name, {})
            if not bool(base_status.get("served")) and bool(final_status.get("served")):
                restored_load_kw += float(base_status.get("kw", 0.0))
        total = max(1, int(state.get("total_candidates", 0)))
        invalid = int(state.get("invalid_candidates", 0))
        evaluations = list(state.get("evaluation_history", []))
        source_counts: Dict[str, int] = {}
        certified_source_counts: Dict[str, int] = {}
        rejection_taxonomy: Dict[str, int] = {}
        action_count = 0
        supervisory_action_count = 0
        readbacks: List[Dict[str, Any]] = []
        for item in evaluations:
            source = str(item.get("source", "unknown"))
            source_counts[source] = source_counts.get(source, 0) + 1
            if item.get("certified"):
                certified_source_counts[source] = certified_source_counts.get(source, 0) + 1
            else:
                families = {
                    str(mode).split(":", 1)[0]
                    for mode in (item.get("failure_modes") or [])
                }
                for family in families:
                    rejection_taxonomy[family] = rejection_taxonomy.get(family, 0) + 1
            action_count += len(item.get("actions") or [])
            supervisory_action_count += int(
                item.get("supervisory_action_count", len(item.get("actions") or []))
            )
            readbacks.extend(item.get("actuation_readback") or [])
        verified_readbacks = sum(item.get("status") == "verified" for item in readbacks)
        candidate_simulation_latencies = [
            float(item["simulation_latency_ms"])
            for item in evaluations if item.get("simulation_latency_ms") is not None
        ]
        candidate_evaluation_latencies = [
            float(item["evaluation_latency_ms"])
            for item in evaluations if item.get("evaluation_latency_ms") is not None
        ]
        llm_calls = list(getattr(self.llm, "call_records", []) or [])
        llm_prompt_tokens = sum(int(item.get("prompt_eval_count") or 0) for item in llm_calls)
        llm_output_tokens = sum(int(item.get("eval_count") or 0) for item in llm_calls)
        llm_total_duration_ms = sum(
            float(item.get("total_duration_ns") or 0.0) / 1_000_000.0
            for item in llm_calls
        )
        llm_load_duration_ms = sum(
            float(item.get("load_duration_ns") or 0.0) / 1_000_000.0
            for item in llm_calls
        )
        llm_calls_by_stream: Dict[str, int] = {}
        for item in llm_calls:
            stream = str(item.get("seed_stream", "unknown"))
            llm_calls_by_stream[stream] = llm_calls_by_stream.get(stream, 0) + 1
        stage_latency_ms: Dict[str, float] = {}
        for item in state.get("agent_trace", []):
            if item.get("latency_ms") is None:
                continue
            node = str(item.get("node", "unknown"))
            stage_latency_ms[node] = stage_latency_ms.get(node, 0.0) + float(item["latency_ms"])
        certified_rate = float(state.get("certified_candidates", 0)) / total
        allocated_slots = int(state.get("candidate_slots_allocated", 0))
        simulated_candidates = int(state.get("total_candidates", 0)) - invalid
        topology_reference_preserved = bool(
            int(final.get("source_disconnected_loads", 0))
            <= int(security_reference.get("source_disconnected_loads", 0))
            and int(final.get("network_components", 0))
            <= int(security_reference.get("network_components", 0))
            and int(final.get("network_cycle_rank", 0))
            <= int(security_reference.get("network_cycle_rank", 0))
        )
        absolute_limits_final = operating_goal_satisfied(final)
        absolute_final = bool(absolute_limits_final and topology_reference_preserved)
        research_metrics = {
            "certified_candidate_rate": certified_rate,
            "certified_action_rate": certified_rate,
            "metric_note": (
                "certified_action_rate is retained for backward compatibility; "
                "its denominator is candidate bundles, not individual device actions."
            ),
            "candidate_bundles_proposed": int(state.get("total_candidates", 0)),
            "candidate_slots_allocated": allocated_slots,
            "llm_candidate_objects_returned": int(
                state.get("llm_candidate_objects_returned", 0)
            ),
            "llm_parse_valid_candidates": int(state.get("llm_parse_valid_candidates", 0)),
            "historical_duplicates_filtered": int(
                state.get("historical_duplicates_filtered", 0)
            ),
            "verifier_input_candidates": int(state.get("total_candidates", 0)),
            "candidate_bundles_simulated": simulated_candidates,
            "certified_candidates": int(state.get("certified_candidates", 0)),
            "certified_per_allocated_slot": (
                float(state.get("certified_candidates", 0)) / allocated_slots
                if allocated_slots else None
            ),
            "simulated_per_allocated_slot": (
                simulated_candidates / allocated_slots if allocated_slots else None
            ),
            "device_actions_proposed": action_count,
            "supervisory_actions_proposed": supervisory_action_count,
            "candidate_source_counts": source_counts,
            "certified_source_counts": certified_source_counts,
            "rejection_taxonomy": rejection_taxonomy,
            "post_solve_readback_checks": len(readbacks),
            "post_solve_readback_verified": verified_readbacks,
            "post_solve_readback_rate": (
                verified_readbacks / len(readbacks) if readbacks else None
            ),
            "operating_limit_relief": {
                "voltage_severity_reduction_pu": float(baseline.get("v_severity", 0.0) - final.get("v_severity", 0.0)),
                "voltage_violation_bus_reduction": int(baseline.get("viol_buses", 0) - final.get("viol_buses", 0)),
                "overloaded_line_reduction": int(baseline.get("over_lines", 0) - final.get("over_lines", 0)),
                "thermal_severity_reduction_pct_sum": float(
                    baseline.get("thermal_severity_pct_sum", 0.0)
                    - final.get("thermal_severity_pct_sum", 0.0)
                ),
            },
            "restored_load_kw": restored_load_kw,
            "switching_effort": int(state.get("switching_effort", 0)),
            "invalid_action_rejection_count": invalid,
            "invalid_action_rejection_rate": invalid / total,
            "pre_simulation_rejection_count": invalid,
            "pre_simulation_rejection_rate": invalid / total,
            "iterations_executed": int(state.get("iteration", 0)),
            "iterations_to_first_certified_action": state.get("first_certified_iteration"),
            "relative_physics_verified_recommendation": bool(
                state.get("history") and any(item.get("certified") for item in state["history"])
            ),
            "physics_certified_recommendation": bool(
                state.get("history") and any(item.get("certified") for item in state["history"])
            ),
            "unsafe_commit_count": sum(
                1 for item in state.get("history", [])[1:] if not item.get("certified")
            ),
            "absolute_feasible_final_state": absolute_final,
            "absolute_operating_limits_satisfied": absolute_limits_final,
            "topology_reference_preserved": topology_reference_preserved,
            "operating_goal_satisfied": absolute_final,
            "objective_reduction": float(objective(baseline) - objective(final)),
            "cumulative_accepted_device_actions": float(
                final.get("cumulative_device_action_count", 0.0)
            ),
            "cumulative_accepted_control_effort": float(
                final.get("cumulative_control_effort", 0.0)
            ),
            "pv_curtailment_command_fraction_sum": float(
                final.get("pv_curtailment_command_fraction_sum", 0.0)
            ),
            "storage_dispatch_command_fraction_sum": float(
                final.get("storage_dispatch_command_fraction_sum", 0.0)
            ),
            "candidate_simulation_latency_ms": candidate_simulation_latencies,
            "candidate_evaluation_latency_ms": candidate_evaluation_latencies,
            "stage_latency_ms": stage_latency_ms,
            "llm_call_count": len(llm_calls),
            "llm_calls_by_stream": llm_calls_by_stream,
            "llm_prompt_tokens": llm_prompt_tokens,
            "llm_output_tokens": llm_output_tokens,
            "llm_total_duration_ms": llm_total_duration_ms,
            "llm_load_duration_ms": llm_load_duration_ms,
        }
        stamp = time.strftime("%Y%m%d_%H%M%S")
        out_path = RUN_DIR / f"gridguard_run_{state['case']['label']}_{stamp}.json"
        public_evals = list(state.get("evaluation_history", []))
        try:
            with open(out_path, "w", encoding="utf-8") as handle:
                json.dump({
                    "framework": "GridGuard", "case": state["case"], "baseline": baseline,
                    "security_reference": security_reference,
                    "history": state.get("history", []), "final": final,
                    "research_metrics": research_metrics, "feedback_history": state.get("feedback_history", []),
                    "meta_prompt_snapshots": state.get("meta_prompt_snapshots", []),
                    "agent_trace": state.get("agent_trace", []),
                    "candidate_evaluation_ledger": public_evals,
                    "last_verification_results": [
                        {key: value for key, value in item.items() if key not in {"snapshot", "merged_commands"}}
                        for item in state.get("verification_results", [])
                    ],
                    "configuration": {
                        name: getattr(self.config, name)
                        for name in self.config.__dataclass_fields__
                    },
                    "llm": {
                        "model": getattr(self.llm, "model", "unknown"),
                        "seed": getattr(self.llm, "seed", None),
                        "calls": llm_calls,
                    },
                }, handle, indent=2)
            self.progress(f"[GridGuard] Saved certified run record: {out_path}")
        except Exception as exc:
            self.progress(f"[GridGuard] Run record could not be saved: {exc}")
        return {"final_metrics": research_metrics, "run_path": str(out_path), "route": "done"}

    def run(self, initial_state: GridGuardState) -> GridGuardState:
        app = self.build()
        return app.invoke(
            initial_state,
            config={"recursion_limit": max(50, self.config.steps * 5 + 10)},
        )


# =========================
# Worker: LangGraph execution behind the desktop UI
# =========================
class OPROMetaWorker(QThread):
    progress = Signal(str)
    meta_prompt_updated = Signal(str)
    step_done = Signal(object)
    finished_ok = Signal(object)
    finished_err = Signal(str)

    def __init__(self, llm: LLMClient, translator: ActionTranslator,
                 case: Dict[str, str], base_cmds: List[str],
                 vmin: float, vmax: float,
                 steps: int, k_candidates: int, max_actions: int,
                 llm_samples: int, explore_temp: float,
                 guardrail_start_stuck: int, max_stuck: int,
                 allow_switch: bool, allow_pv: bool, allow_load: bool, allow_var_gen: bool,
                 prefer_utility_first: bool,
                 vargen_after_stuck: int,
                 pv_after_stuck: int,
                 load_after_stuck: int,
                 fast_llm: bool,
                 show_meta_prompt: bool,
                 teaching_notes: bool,
                 extra_instruction: str):
        super().__init__()
        self.llm = llm
        self.translator = translator
        self.case = case
        self.base_cmds = base_cmds
        self.vmin = vmin
        self.vmax = vmax

        self.steps = max(1, int(steps))
        self.k_candidates = max(3, int(k_candidates))
        self.max_actions = max(1, int(max_actions))
        self.llm_samples = max(1, int(llm_samples))
        self.explore_temp = float(explore_temp)

        self.guardrail_start_stuck = max(0, int(guardrail_start_stuck))
        self.max_stuck = max(3, int(max_stuck))

        self.allow_switch = allow_switch
        self.allow_pv = allow_pv
        self.allow_load = allow_load
        self.allow_var_gen = allow_var_gen

        self.prefer_utility_first = bool(prefer_utility_first)
        self.vargen_after_stuck = max(0, int(vargen_after_stuck))
        self.pv_after_stuck = max(0, int(pv_after_stuck))
        self.load_after_stuck = max(0, int(load_after_stuck))

        self.fast_llm = bool(fast_llm)
        self.show_meta_prompt = bool(show_meta_prompt)
        self.teaching_notes = bool(teaching_notes)
        self.extra_instruction = (extra_instruction or "").strip()

    def _run_legacy(self):
        try:
            state_cmds: List[str] = []

            res = compile_and_solve(self.case["label"], self.case["folder"], self.case["main_dss"],
                                    self.base_cmds, self.vmin, self.vmax)
            met = summarize_metrics(res, self.vmin, self.vmax)
            cur_obj = objective(met)
            baseline_met = dict(met)

            history: List[Dict[str, Any]] = [{
                "step": -1, "picked": "BASELINE", "source": "BASE",
                "applied_cmds": [], "before": met, "after": met, "obj": float(cur_obj),
                "teaching": ""
            }]

            self.progress.emit(f"[OPRO] Baseline: obj={cur_obj:.3e} metrics={met}")

            best_so_far: List[Dict[str, Any]] = [{
                "obj": float(cur_obj),
                "metrics": met,
                "solution": {"name": "BASELINE", "delta_cmds": [], "delta_actions": [], "source": "BASE"}
            }]

            recent_evals: List[Dict[str, Any]] = []
            stuck = 0

            task = "Use OpenDSS controllable devices to reduce voltage violations and overloads while keeping the power-flow converged."
            constraints = [
                "DO NOT edit Vsource.*",
                "Switching only if allow_switch=true AND line exists",
                "Only use exact device names listed in STATE.available_devices",
                "Each candidate must have >=1 action",
            ]

            base_temp = 0.22
            explore_temp = max(0.30, min(0.95, self.explore_temp))
            num_predict = 520 if self.fast_llm else 1600
            teach_predict = 300

            for step in range(self.steps):
                if met.get("viol_buses", 0) == 0 and met.get("over_lines", 0) == 0:
                    self.progress.emit(f"[OPRO] Stop: solved at step {step}.")
                    break

                devs = res.devices
                worst_list = worst_buses_list(res, self.vmin, self.vmax, k=5)
                top_lines = top_overloaded_lines(res, k=5)

                forbidden_first = []
                if stuck >= 1:
                    for e in recent_evals[-10:]:
                        acts = sanitize_actions(e.get("actions", []))
                        fam = first_family(acts)
                        if fam and fam != "none":
                            forbidden_first.append(fam)
                    forbidden_first = list(dict.fromkeys(forbidden_first))[:10]

                # Utility-first gating (for LLM)
                allow_var_gen_now = self.allow_var_gen and ((not self.prefer_utility_first) or (stuck >= self.vargen_after_stuck))
                allow_pv_now = self.allow_pv and ((not self.prefer_utility_first) or (stuck >= self.pv_after_stuck))
                allow_load_now = self.allow_load and ((not self.prefer_utility_first) or (stuck >= self.load_after_stuck))

                state_summary = {
                    "feeder": res.case_label,
                    "limits": [self.vmin, self.vmax],
                    "current_metrics": met,
                    "current_obj": float(cur_obj),
                    "WORST_BUSES": worst_list,
                    "TOP_LINES": top_lines,
                    "allow_switch": self.allow_switch,
                    "allow_var_gen_now": allow_var_gen_now,
                    "allow_pv_now": allow_pv_now,
                    "allow_load_now": allow_load_now,
                    "available_devices": {
                        "regcontrols": (devs.get("regcontrols") or [])[:30],
                        "capacitors": (devs.get("capacitors") or [])[:30],
                        "lines": (devs.get("lines") or [])[:25],
                    },
                    "reg_map_hint": {k: v for k, v in list(res.reg_map.items())[:18]},
                }
                if self.extra_instruction:
                    state_summary["extra_instruction"] = self.extra_instruction

                best_so_far = sorted(best_so_far, key=lambda x: x["obj"])[:25]

                system = (
                    "You are OPRO (Optimization by PROmpting): a derivative-free optimizer.\n"
                    "Return strict JSON only inside <JSON>...</JSON>.\n"
                    "Actions MUST be JSON objects, not strings.\n"
                    "Never propose Vsource edits.\n"
                )

                meta_prompt = build_meta_prompt(
                    task=task,
                    constraints=constraints,
                    state_summary=state_summary,
                    best_so_far=best_so_far,
                    recent_evals=recent_evals,
                    stuck=stuck,
                    forbidden_first=forbidden_first,
                    prefer_utility_first=self.prefer_utility_first,
                    allow_var_gen_now=allow_var_gen_now,
                    allow_pv_now=allow_pv_now,
                    allow_load_now=allow_load_now,
                    k_candidates=self.k_candidates,
                    max_actions=self.max_actions
                )

                if self.show_meta_prompt:
                    self.meta_prompt_updated.emit(meta_prompt[:9000])

                temps = []
                if self.llm_samples == 1:
                    temps = [base_temp]
                elif self.llm_samples == 2:
                    temps = [base_temp, explore_temp]
                else:
                    temps = [base_temp, explore_temp] + [min(0.95, explore_temp + 0.10)] * (self.llm_samples - 2)

                llm_pool: List[Dict[str, Any]] = []
                for si, T in enumerate(temps):
                    raw = self.llm.chat(
                        system=system, user_text=meta_prompt, temperature=T,
                        num_predict=num_predict, response_format="json",
                    )
                    obj_llm = parse_llm_json(raw) or {}
                    cands = obj_llm.get("candidates", [])
                    if isinstance(cands, list):
                        for c in cands:
                            if not isinstance(c, dict):
                                continue
                            acts = sanitize_actions(c.get("actions", []))
                            if not acts:
                                continue
                            nm = str(c.get("name", "")).strip()
                            if (not nm) or (nm.lower() == "string"):
                                nm = f"LLM_step{step}_s{si}"
                            c2 = dict(c)
                            c2["name"] = nm[:80]
                            c2["source"] = "LLM"
                            c2["actions"] = acts[:self.max_actions]
                            c2["reasoning"] = str(c.get("reasoning", ""))[:320]
                            llm_pool.append(c2)

                llm_pool = dedup_candidates(llm_pool)
                llm_pool = repair_candidate_buses(llm_pool, worst_list)
                llm_pool = pick_diverse_subset(llm_pool, k=min(22, max(self.k_candidates, 12)))

                # Evaluate LLM pool first (your requirement)
                pool = list(llm_pool)

                # Guardrail physics only after stuck threshold OR no LLM candidates
                use_phys = (stuck >= self.guardrail_start_stuck) or (len(llm_pool) == 0)
                if use_phys:
                    pool += physics_candidates(
                        res, self.vmin, self.vmax,
                        allow_var_gen=self.allow_var_gen,
                        allow_pv=self.allow_pv,
                        allow_load=self.allow_load,
                        max_actions=self.max_actions
                    )

                pool = dedup_candidates(pool)
                if not pool:
                    stuck += 1
                    self.progress.emit(f"[OPRO] Step {step}: no usable candidates. stuck={stuck}")
                    if stuck >= self.max_stuck:
                        self.progress.emit(f"[OPRO] Stuck for {self.max_stuck} steps. Stopping.")
                        break
                    continue

                table = []
                best_step = None
                best_step_obj = float("inf")

                for cand in pool[:60]:
                    name = str(cand.get("name", "cand"))[:70]
                    src = str(cand.get("source", "LLM"))
                    actions_any = cand.get("actions", [])
                    reasoning = str(cand.get("reasoning", ""))[:220]

                    # Enforce utility-first gating at evaluator too (not just prompt)
                    fam = first_family(sanitize_actions(actions_any))
                    if self.prefer_utility_first:
                        if (not allow_var_gen_now) and fam == "create_var_gen":
                            continue
                        if (not allow_pv_now) and fam == "create_pv":
                            continue
                        if (not allow_load_now) and fam == "create_load":
                            continue

                    cmds, notes = self.translator.actions_to_cmds(
                        res, actions_any,
                        allow_switch=self.allow_switch,
                        allow_pv=self.allow_pv,
                        allow_load=self.allow_load,
                        allow_var_gen=self.allow_var_gen,
                        max_actions=self.max_actions
                    )

                    if not cmds:
                        msg = "no_cmds"
                        if notes:
                            msg += f" notes={notes[:3]}"
                        table.append((src, name, 1e30, False, 0, msg))
                        recent_evals.append({
                            "step": step, "name": name, "source": src,
                            "obj": 1e30, "ok": False,
                            "actions": sanitize_actions(actions_any)[:self.max_actions],
                            "notes": notes[:6],
                            "reasoning": reasoning
                        })
                        continue

                    merged = merge_state_cmds(state_cmds, cmds)
                    full_cmds = self.base_cmds + merged

                    try:
                        res_try = compile_and_solve(self.case["label"], self.case["folder"], self.case["main_dss"],
                                                    full_cmds, self.vmin, self.vmax)
                        met_try = summarize_metrics(res_try, self.vmin, self.vmax)
                        obj_try = objective(met_try)
                        ok = bool(met_try.get("converged", True))
                    except Exception as e:
                        met_try = {"converged": False, "viol_buses": 999, "v_severity": 999, "losses_kw": 1e9, "over_lines": 999, "max_line_pct": np.nan, "viol_type": "apply_error"}
                        obj_try = 1e30
                        ok = False
                        notes = notes + [f"apply_error:{str(e)[:120]}"]

                    table.append((src, name, obj_try, ok, len(cmds), f"viol={met_try.get('viol_buses')} vsev={met_try.get('v_severity'):.4f}"))
                    recent_evals.append({
                        "step": step, "name": name, "source": src,
                        "obj": float(obj_try), "ok": ok,
                        "metrics": met_try,
                        "delta_cmds": cmds,
                        "actions": sanitize_actions(actions_any)[:self.max_actions],
                        "notes": notes[:6],
                        "reasoning": reasoning
                    })
                    recent_evals = recent_evals[-80:]

                    best_so_far.append({
                        "obj": float(obj_try),
                        "metrics": met_try,
                        "solution": {"name": name, "source": src, "delta_cmds": cmds, "delta_actions": sanitize_actions(actions_any)[:self.max_actions]}
                    })
                    best_so_far = sorted(best_so_far, key=lambda x: x["obj"])[:25]

                    if obj_try < best_step_obj:
                        best_step_obj = float(obj_try)
                        best_step = {"name": name, "source": src, "cmds": cmds, "obj": obj_try, "reasoning": reasoning}

                table = sorted(table, key=lambda x: x[2])
                lines = [f"[OPRO] Step {step} candidates (LLM_pool={len(llm_pool)} use_phys={use_phys} stuck={stuck}):"]
                for src, nm, ob, ok, ncmd, extra in table[:14]:
                    lines.append(f"- SRC={src:4s} {nm:30s} {'OK' if ok else 'BAD'} obj={ob:.3e} cmds={ncmd} {extra}")
                self.progress.emit("\n".join(lines))

                if best_step is None:
                    stuck += 1
                    self.progress.emit(f"[OPRO] Step {step}: no valid candidate. stuck={stuck}")
                    if stuck >= self.max_stuck:
                        self.progress.emit(f"[OPRO] Stuck for {self.max_stuck} steps. Stopping.")
                        break
                    continue

                # Accept only improvement
                if best_step["obj"] < cur_obj - 1e-6:
                    before = met

                    # Grounded teaching: compute worst bus before min/max
                    worst_bus = worst_list[0]["bus"] if worst_list else ""
                    b_vmin0, b_vmax0 = (None, None)
                    if worst_bus:
                        # current "res" is still before the accepted step, so bus_minmax_pu reads before-values
                        b_vmin0, b_vmax0 = bus_minmax_pu(worst_bus)

                    state_cmds = merge_state_cmds(state_cmds, best_step["cmds"])
                    res = compile_and_solve(self.case["label"], self.case["folder"], self.case["main_dss"],
                                            self.base_cmds + state_cmds, self.vmin, self.vmax)
                    met = summarize_metrics(res, self.vmin, self.vmax)
                    cur_obj = objective(met)

                    # Grounded teaching: worst bus after min/max (now DSS state includes accepted cmds)
                    b_vmin1, b_vmax1 = (None, None)
                    if worst_bus:
                        b_vmin1, b_vmax1 = bus_minmax_pu(worst_bus)

                    teach = ""
                    if self.teaching_notes:
                        teach_sys = (
                            "You are a distribution operator teaching a trainee.\n"
                            "Use ONLY the provided numbers. If a value is None, say 'not available'.\n"
                            "Do NOT invent voltages or line loadings.\n"
                            "Explain in 8–12 lines why the chosen action should help.\n"
                            "End with 2 next actions to try if a violation remains."
                        )
                        teach_user = (
                            f"Feeder={res.case_label}\n"
                            f"Chosen source={best_step['source']} name={best_step['name']}\n"
                            f"Candidate reasoning={best_step.get('reasoning','')}\n"
                            f"Commands:\n- " + "\n- ".join(best_step["cmds"]) + "\n\n"
                            f"Before metrics={before}\nAfter metrics={met}\n"
                            f"Worst_bus={worst_bus} vmin_before={b_vmin0} vmax_before={b_vmax0} vmin_after={b_vmin1} vmax_after={b_vmax1}\n"
                            f"Worst_buses_list={worst_list}\nTop_lines={top_lines}\n"
                        )
                        teach = self.llm.chat(teach_sys, teach_user, temperature=0.25, num_predict=teach_predict)

                    rec = {
                        "step": step,
                        "picked": best_step["name"],
                        "source": best_step["source"],
                        "applied_cmds": best_step["cmds"],
                        "before": before,
                        "after": met,
                        "obj": float(cur_obj),
                        "teaching": teach
                    }
                    history.append(rec)
                    self.step_done.emit(rec)

                    top3 = sorted(best_so_far, key=lambda x: x["obj"])[:3]
                    top3_txt = " | ".join([f"{t['solution']['source']}:{t['solution']['name']} obj={t['obj']:.2e}" for t in top3])
                    self.progress.emit(f"[OPRO] Meta-prompt updated: BEST_SO_FAR top3 => {top3_txt}")
                    self.progress.emit(f"[OPRO] Accepted step {step}: source={rec['source']} picked={rec['picked']} -> obj={cur_obj:.3e} viol={met['viol_buses']}")
                    stuck = 0
                else:
                    stuck += 1
                    self.progress.emit(f"[OPRO] Step {step}: no improvement (best={best_step['obj']:.3e} vs current={cur_obj:.3e}). stuck={stuck}")
                    if stuck >= self.max_stuck:
                        self.progress.emit(f"[OPRO] Stuck for {self.max_stuck} steps. Stopping.")
                        break

            # save run
            stamp = time.strftime("%Y%m%d_%H%M%S")
            out_path = RUN_DIR / f"opro_run_{self.case['label']}_{stamp}.json"
            try:
                with open(out_path, "w", encoding="utf-8") as f:
                    json.dump({
                        "case": self.case,
                        "baseline": baseline_met,
                        "history": history,
                        "final": met,
                    }, f, indent=2)
                self.progress.emit(f"[OPRO] Saved run log: {str(out_path)}")
            except Exception:
                pass

            self.finished_ok.emit({"final": res, "history": history, "baseline": baseline_met, "best_archive": best_so_far})

        except Exception:
            self.finished_err.emit(traceback.format_exc())

    def run(self):
        """Execute the typed GridGuard graph and adapt its result to the existing UI."""
        try:
            config = GridGuardConfig(
                steps=self.steps,
                k_candidates=self.k_candidates,
                max_actions=self.max_actions,
                llm_samples=self.llm_samples,
                explore_temp=self.explore_temp,
                guardrail_start_stuck=self.guardrail_start_stuck,
                max_stuck=self.max_stuck,
                allow_switch=self.allow_switch,
                allow_pv=self.allow_pv,
                allow_load=self.allow_load,
                allow_var_gen=self.allow_var_gen,
                prefer_utility_first=self.prefer_utility_first,
                vargen_after_stuck=self.vargen_after_stuck,
                pv_after_stuck=self.pv_after_stuck,
                load_after_stuck=self.load_after_stuck,
                fast_llm=self.fast_llm,
                show_meta_prompt=self.show_meta_prompt,
                teaching_notes=self.teaching_notes,
                extra_instruction=self.extra_instruction,
            )
            engine = GridGuardEngine(
                llm=self.llm,
                translator=self.translator,
                config=config,
                progress=self.progress.emit,
                meta_prompt_updated=self.meta_prompt_updated.emit,
                step_done=self.step_done.emit,
            )
            final_state = engine.run({
                "case": self.case,
                "base_cmds": self.base_cmds,
                "vmin": self.vmin,
                "vmax": self.vmax,
            })
            self.finished_ok.emit({
                "final": final_state["current_snapshot"],
                "history": final_state.get("history", []),
                "baseline": final_state.get("baseline_metrics", {}),
                "best_archive": final_state.get("best_so_far", []),
                "research_metrics": final_state.get("final_metrics", {}),
                "run_path": final_state.get("run_path", ""),
            })
        except Exception:
            self.finished_err.emit(traceback.format_exc())


# =========================
# Plot canvas
# =========================
class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.fig.patch.set_facecolor("#121214")
        self.ax.set_facecolor("#121214")

    def _restyle(self):
        self.fig.patch.set_facecolor("#121214")
        self.ax.set_facecolor("#121214")
        self.ax.tick_params(colors="#e6e6eb")
        for s in self.ax.spines.values():
            s.set_color("#3a3a3d")
        self.ax.title.set_color("#e6e6eb")
        self.ax.xaxis.label.set_color("#e6e6eb")
        self.ax.yaxis.label.set_color("#e6e6eb")

    def plot_bus_vavg(self, bus_df: pd.DataFrame, vmin_pu: float, vmax_pu: float):
        self.ax.clear()
        self._restyle()
        if bus_df is None or bus_df.empty or "vavg_pu" not in bus_df.columns:
            self.ax.set_title("No bus results")
            self.draw()
            return
        x = np.arange(len(bus_df))
        y = bus_df["vavg_pu"].to_numpy(dtype=float)
        self.ax.plot(x, y, marker="o", linewidth=1)
        self.ax.axhline(vmin_pu, linestyle="--", linewidth=1)
        self.ax.axhline(vmax_pu, linestyle="--", linewidth=1)
        self.ax.set_title("Bus Vavg (pu)")
        self.ax.grid(True, alpha=0.25)
        self.fig.tight_layout()
        self.draw()

    def plot_progress(self, history: List[Dict[str, Any]]):
        self.ax.clear()
        self._restyle()
        steps, obj, viols = [], [], []
        for h in history:
            if h.get("step", -1) < 0:
                continue
            a = h.get("after", {})
            steps.append(int(h["step"]))
            obj.append(float(h.get("obj", 0.0)))
            viols.append(float(a.get("viol_buses", 0.0)))
        if not steps:
            self.ax.set_title("No progress data")
            self.draw()
            return
        self.ax.plot(steps, obj, marker="o", linewidth=1, label="objective")
        self.ax.plot(steps, viols, marker="o", linewidth=1, label="viol_buses")
        self.ax.set_title("Progress vs baseline")
        self.ax.set_xlabel("Step")
        self.ax.grid(True, alpha=0.25)
        self.ax.legend()
        self.fig.tight_layout()
        self.draw()


# =========================
# UI
# =========================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GridGuard — Physics-Informed LLM Optimization")
        self.resize(1950, 1080)

        self.llm = LLMClient()
        self.translator = ActionTranslator()

        self.cases: List[Dict[str, str]] = []
        self.current_case: Optional[Dict[str, str]] = None
        self.current_result: Optional[SnapshotResult] = None
        self.history: List[Dict[str, Any]] = []

        # Left: cases + baseline
        self.root_edit = QLineEdit(DEFAULT_TESTCASES_ROOT)
        self.btn_scan = QPushButton("Scan cases (fast)")
        self.case_combo = QComboBox()
        self.folder_edit = QLineEdit("")
        self.folder_edit.setReadOnly(True)
        self.dss_edit = QLineEdit("")
        self.dss_edit.setReadOnly(True)

        self.vmin_edit = QLineEdit(str(V_MIN_PU_DEFAULT))
        self.vmax_edit = QLineEdit(str(V_MAX_PU_DEFAULT))
        self.base_cmds = QPlainTextEdit()
        self.base_cmds.setPlaceholderText("Base commands (one per line)")
        self.btn_solve = QPushButton("Solve baseline")
        self.summary = QPlainTextEdit()
        self.summary.setReadOnly(True)
        self.log = QPlainTextEdit()
        self.log.setReadOnly(True)

        # Center: plots + table
        self.canvas = MplCanvas()
        self.plot_mode = QComboBox()
        self.plot_mode.addItems(["Bus Vavg", "Progress"])
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(["Bus", "Phases", "Vmin", "Vmax", "Vavg", "Violation"])
        self.table.horizontalHeader().setStretchLastSection(True)

        # Right: LLM/OPRO settings
        self.model_combo = QComboBox()
        self.btn_models = QPushButton("Refresh models")
        self.cb_fast = QCheckBox("Fast LLM")
        self.cb_fast.setChecked(True)

        self.cb_switch = QCheckBox("Allow switching (Open/Close lines)")
        self.cb_switch.setChecked(False)
        self.cb_pv = QCheckBox("Allow PV creation")
        self.cb_pv.setChecked(False)
        self.cb_load = QCheckBox("Allow Load creation")
        self.cb_load.setChecked(False)
        self.cb_vargen = QCheckBox("Allow VAR-only Generator")
        self.cb_vargen.setChecked(True)

        self.cb_util_first = QCheckBox("Prefer utility devices first (taps/caps before gen/PV/load)")
        self.cb_util_first.setChecked(True)

        self.vargen_after_edit = QLineEdit("1")
        self.pv_after_edit = QLineEdit("2")
        self.load_after_edit = QLineEdit("2")

        self.cb_teach = QCheckBox("Teaching note per accepted step (grounded)")
        self.cb_teach.setChecked(True)
        self.cb_show_prompt = QCheckBox("Show meta-prompt viewer")
        self.cb_show_prompt.setChecked(True)

        self.steps_edit = QLineEdit("10")
        self.kcand_edit = QLineEdit("10")
        self.max_actions_edit = QLineEdit("3")
        self.llm_samples_edit = QLineEdit("3")
        self.explore_temp_edit = QLineEdit("0.70")

        # IMPORTANT: physics should be delayed (your request)
        self.guardrail_edit = QLineEdit("4")
        self.max_stuck_edit = QLineEdit("8")

        self.extra_instruction = QPlainTextEdit()
        self.extra_instruction.setPlaceholderText(
            "Extra instruction (optional).\n"
            "Example: 'Try creg1a and creg1c taps both directions before any var gen.'"
        )

        self.btn_run = QPushButton("Run GridGuard certification graph")
        self.chat = QPlainTextEdit()
        self.chat.setReadOnly(True)

        self.meta_box = QPlainTextEdit()
        self.meta_box.setReadOnly(True)
        self.meta_box.setPlaceholderText("Meta-prompt will appear here (truncated).")

        self._load_models()

        # Layout
        left = QWidget()
        L = QVBoxLayout(left)

        gb_cases = QGroupBox("TestCases")
        gl = QGridLayout(gb_cases)
        gl.addWidget(QLabel("Root:"), 0, 0)
        gl.addWidget(self.root_edit, 0, 1, 1, 2)
        gl.addWidget(self.btn_scan, 0, 3)
        gl.addWidget(QLabel("Case:"), 1, 0)
        gl.addWidget(self.case_combo, 1, 1, 1, 3)
        gl.addWidget(QLabel("Folder:"), 2, 0)
        gl.addWidget(self.folder_edit, 2, 1, 1, 3)
        gl.addWidget(QLabel("Main .dss:"), 3, 0)
        gl.addWidget(self.dss_edit, 3, 1, 1, 3)
        L.addWidget(gb_cases)

        gb_base = QGroupBox("Baseline")
        gb = QGridLayout(gb_base)
        gb.addWidget(QLabel("Vmin:"), 0, 0)
        gb.addWidget(self.vmin_edit, 0, 1)
        gb.addWidget(QLabel("Vmax:"), 0, 2)
        gb.addWidget(self.vmax_edit, 0, 3)
        gb.addWidget(self.base_cmds, 1, 0, 1, 4)
        gb.addWidget(self.btn_solve, 2, 0, 1, 4)
        gb.addWidget(QLabel("Summary:"), 3, 0, 1, 4)
        gb.addWidget(self.summary, 4, 0, 1, 4)
        L.addWidget(gb_base)

        L.addWidget(QLabel("Log:"))
        L.addWidget(self.log, stretch=1)

        center = QWidget()
        C = QVBoxLayout(center)
        rowp = QHBoxLayout()
        rowp.addWidget(QLabel("Plot:"))
        rowp.addWidget(self.plot_mode)
        C.addLayout(rowp)
        C.addWidget(self.canvas, stretch=2)
        C.addWidget(self.table, stretch=3)

        right = QWidget()
        R = QVBoxLayout(right)

        gb_model = QGroupBox("Ollama")
        hm = QHBoxLayout(gb_model)
        hm.addWidget(QLabel("Model:"))
        hm.addWidget(self.model_combo)
        hm.addWidget(self.btn_models)
        R.addWidget(gb_model)

        R.addWidget(self.cb_fast)
        R.addWidget(self.cb_switch)
        R.addWidget(self.cb_vargen)
        R.addWidget(self.cb_pv)
        R.addWidget(self.cb_load)
        R.addWidget(self.cb_util_first)

        gb_gate = QGroupBox("Utility-first gating (stuck threshold)")
        gg = QGridLayout(gb_gate)
        gg.addWidget(QLabel("Allow VAR-gen after stuck ≥"), 0, 0)
        gg.addWidget(self.vargen_after_edit, 0, 1)
        gg.addWidget(QLabel("Allow PV after stuck ≥"), 1, 0)
        gg.addWidget(self.pv_after_edit, 1, 1)
        gg.addWidget(QLabel("Allow Load after stuck ≥"), 2, 0)
        gg.addWidget(self.load_after_edit, 2, 1)
        R.addWidget(gb_gate)

        R.addWidget(self.cb_teach)
        R.addWidget(self.cb_show_prompt)

        gb_cfg = QGroupBox("GridGuard / OPRO settings")
        g = QGridLayout(gb_cfg)
        g.addWidget(QLabel("steps"), 0, 0); g.addWidget(self.steps_edit, 0, 1)
        g.addWidget(QLabel("k_candidates"), 1, 0); g.addWidget(self.kcand_edit, 1, 1)
        g.addWidget(QLabel("max_actions"), 2, 0); g.addWidget(self.max_actions_edit, 2, 1)
        g.addWidget(QLabel("LLM samples/step"), 3, 0); g.addWidget(self.llm_samples_edit, 3, 1)
        g.addWidget(QLabel("explore temp"), 4, 0); g.addWidget(self.explore_temp_edit, 4, 1)
        g.addWidget(QLabel("physics after stuck ≥"), 5, 0); g.addWidget(self.guardrail_edit, 5, 1)
        g.addWidget(QLabel("stop after stuck ≥"), 6, 0); g.addWidget(self.max_stuck_edit, 6, 1)
        R.addWidget(gb_cfg)

        R.addWidget(self.extra_instruction, stretch=1)
        R.addWidget(self.btn_run)

        R.addWidget(QLabel("Run log:"))
        R.addWidget(self.chat, stretch=2)
        R.addWidget(QLabel("Meta-prompt viewer:"))
        R.addWidget(self.meta_box, stretch=2)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left)
        splitter.addWidget(center)
        splitter.addWidget(right)
        splitter.setSizes([600, 720, 620])

        root = QWidget()
        root_layout = QVBoxLayout(root)
        root_layout.addWidget(splitter)
        self.setCentralWidget(root)

        # signals
        self.btn_scan.clicked.connect(self.on_scan)
        self.case_combo.currentIndexChanged.connect(self.on_case_changed)
        self.btn_solve.clicked.connect(self.on_solve)
        self.plot_mode.currentTextChanged.connect(self.refresh_plot)
        self.btn_models.clicked.connect(self._load_models)
        self.btn_run.clicked.connect(self.on_run)
        self.cb_show_prompt.stateChanged.connect(self._toggle_prompt)

        self.on_scan()
        self._toggle_prompt()

    def _toggle_prompt(self):
        self.meta_box.setVisible(bool(self.cb_show_prompt.isChecked()))

    def _load_models(self):
        current = self.model_combo.currentText().strip()
        self.model_combo.clear()
        models = self.llm.list_models()
        if not models:
            models = [self.llm.model]
        self.model_combo.addItems(models)
        if current:
            idx = self.model_combo.findText(current)
            if idx >= 0:
                self.model_combo.setCurrentIndex(idx)

    def _append_log(self, s: str):
        self.log.appendPlainText(s)

    def _get_limits(self) -> Tuple[float, float]:
        try:
            vmin = float(self.vmin_edit.text().strip())
        except Exception:
            vmin = V_MIN_PU_DEFAULT
        try:
            vmax = float(self.vmax_edit.text().strip())
        except Exception:
            vmax = V_MAX_PU_DEFAULT
        return vmin, vmax

    def _get_base_cmds(self) -> List[str]:
        return [ln.strip() for ln in self.base_cmds.toPlainText().splitlines() if ln.strip()]

    def on_scan(self):
        root = self.root_edit.text().strip()
        self.cases = scan_testcases_root_fast(root)
        self.case_combo.blockSignals(True)
        self.case_combo.clear()
        self.case_combo.addItems([c["label"] for c in self.cases] if self.cases else ["(no cases found)"])
        self.case_combo.blockSignals(False)
        self._append_log(f"Found {len(self.cases)} cases.")
        if self.cases:
            self.case_combo.setCurrentIndex(0)
            self.on_case_changed(0)

    def on_case_changed(self, idx: int):
        if idx < 0 or idx >= len(self.cases):
            self.current_case = None
            self.folder_edit.setText("")
            self.dss_edit.setText("")
            return
        self.current_case = self.cases[idx]
        self.folder_edit.setText(self.current_case["folder"])
        self.dss_edit.setText(self.current_case["main_dss"])
        self.chat.appendPlainText(f"\n[Selected] {self.current_case['label']}\n")

    def on_solve(self):
        if not self.current_case:
            return
        vmin, vmax = self._get_limits()
        cmds = self._get_base_cmds()
        try:
            res = compile_and_solve(self.current_case["label"], self.current_case["folder"], self.current_case["main_dss"],
                                    cmds, vmin, vmax)
            self.current_result = res
            met = summarize_metrics(res, vmin, vmax)
            self.summary.setPlainText(str(met))
            self._fill_table(res.bus_df)
            self.history = [{"step": -1, "after": met, "obj": objective(met), "source": "BASE"}]
            self.plot_mode.setCurrentText("Bus Vavg")
            self.refresh_plot()
        except Exception:
            tb = traceback.format_exc()
            QMessageBox.critical(self, "Solve failed", tb)
            self._append_log(tb)

    def _fill_table(self, df: pd.DataFrame):
        if df is None or df.empty:
            self.table.setRowCount(0)
            return
        self.table.setRowCount(len(df))
        for i, row in df.iterrows():
            bus = str(row.get("bus", ""))
            phases = row.get("phases", np.nan)
            vmin = row.get("vmin_pu", np.nan)
            vmax = row.get("vmax_pu", np.nan)
            vavg = row.get("vavg_pu", np.nan)
            viol = bool(row.get("violation", False))
            items = [
                QTableWidgetItem(bus),
                QTableWidgetItem("" if pd.isna(phases) else str(int(phases))),
                QTableWidgetItem("" if pd.isna(vmin) else f"{float(vmin):.4f}"),
                QTableWidgetItem("" if pd.isna(vmax) else f"{float(vmax):.4f}"),
                QTableWidgetItem("" if pd.isna(vavg) else f"{float(vavg):.4f}"),
                QTableWidgetItem("YES" if viol else "no"),
            ]
            for j, it in enumerate(items):
                it.setFlags(it.flags() ^ Qt.ItemIsEditable)
                if j == 5 and viol:
                    it.setBackground(QColor(200, 170, 30))
                self.table.setItem(i, j, it)

    def refresh_plot(self):
        if self.plot_mode.currentText() == "Progress":
            self.canvas.plot_progress(self.history)
            return
        if self.current_result is None:
            return
        vmin, vmax = self._get_limits()
        self.canvas.plot_bus_vavg(self.current_result.bus_df, vmin, vmax)

    def on_run(self):
        if not self.current_case:
            return

        self.llm.model = self.model_combo.currentText().strip() or self.llm.model
        vmin, vmax = self._get_limits()
        base_cmds = self._get_base_cmds()

        def _iget(le: QLineEdit, default: int) -> int:
            try:
                return int(le.text().strip())
            except Exception:
                return default

        def _fget(le: QLineEdit, default: float) -> float:
            try:
                return float(le.text().strip())
            except Exception:
                return default

        steps = _iget(self.steps_edit, 10)
        kcand = _iget(self.kcand_edit, 10)
        max_actions = _iget(self.max_actions_edit, 3)
        llm_samples = _iget(self.llm_samples_edit, 3)
        explore_temp = _fget(self.explore_temp_edit, 0.70)
        guardrail_start = _iget(self.guardrail_edit, 4)
        max_stuck = _iget(self.max_stuck_edit, 8)

        prefer_utility_first = bool(self.cb_util_first.isChecked())
        vargen_after = _iget(self.vargen_after_edit, 1)
        pv_after = _iget(self.pv_after_edit, 2)
        load_after = _iget(self.load_after_edit, 2)

        self.btn_run.setEnabled(False)
        self.chat.appendPlainText("\n[Run] GridGuard StateGraph starting...\n")

        worker = OPROMetaWorker(
            llm=self.llm,
            translator=self.translator,
            case=self.current_case,
            base_cmds=base_cmds,
            vmin=vmin, vmax=vmax,
            steps=steps, k_candidates=kcand, max_actions=max_actions,
            llm_samples=llm_samples, explore_temp=explore_temp,
            guardrail_start_stuck=guardrail_start, max_stuck=max_stuck,
            allow_switch=bool(self.cb_switch.isChecked()),
            allow_pv=bool(self.cb_pv.isChecked()),
            allow_load=bool(self.cb_load.isChecked()),
            allow_var_gen=bool(self.cb_vargen.isChecked()),
            prefer_utility_first=prefer_utility_first,
            vargen_after_stuck=vargen_after,
            pv_after_stuck=pv_after,
            load_after_stuck=load_after,
            fast_llm=bool(self.cb_fast.isChecked()),
            show_meta_prompt=bool(self.cb_show_prompt.isChecked()),
            teaching_notes=bool(self.cb_teach.isChecked()),
            extra_instruction=self.extra_instruction.toPlainText()
        )

        def on_progress(s: str):
            self.chat.appendPlainText(s)

        def on_meta(p: str):
            if self.cb_show_prompt.isChecked():
                self.meta_box.setPlainText(p)

        def on_step(rec: Dict[str, Any]):
            self.chat.appendPlainText(
                f"\n[Step {rec['step']}] source={rec.get('source')} picked={rec['picked']} obj={rec.get('obj',0):.3e}\n"
                f"Commands:\n- " + "\n- ".join(rec["applied_cmds"]) + "\n"
                f"Before: {rec['before']}\nAfter:  {rec['after']}\n"
            )
            if rec.get("teaching"):
                self.chat.appendPlainText("\nTeaching note (grounded):\n" + rec["teaching"] + "\n")
            self.history.append({"step": rec["step"], "after": rec["after"], "obj": rec.get("obj", 0.0), "source": rec.get("source")})

        def on_done(payload: Dict[str, Any]):
            self.btn_run.setEnabled(True)
            self.current_result = payload["final"]
            self.history = []
            for h in payload["history"]:
                self.history.append({"step": h.get("step", -1), "after": h.get("after", {}), "obj": h.get("obj", 0.0), "source": h.get("source", "")})
            met2 = summarize_metrics(self.current_result, vmin, vmax)
            research = payload.get("research_metrics", {})
            self.summary.setPlainText(str(met2) + ("\n\nCertification metrics:\n" + json.dumps(research, indent=2) if research else ""))
            self._fill_table(self.current_result.bus_df)
            self.plot_mode.setCurrentText("Progress")
            self.refresh_plot()
            self.chat.appendPlainText(f"\n[Finished] {met2}\nCertification metrics: {research}\n")

        def on_err(tb: str):
            self.btn_run.setEnabled(True)
            QMessageBox.critical(self, "OPRO failed", tb)
            self._append_log(tb)

        worker.progress.connect(on_progress)
        worker.meta_prompt_updated.connect(on_meta)
        worker.step_done.connect(on_step)
        worker.finished_ok.connect(on_done)
        worker.finished_err.connect(on_err)
        self._worker = worker
        worker.start()


# =========================
# main() (Spyder safe)
# =========================
def main():
    if not _GUI_AVAILABLE:
        raise RuntimeError(
            "The GridGuard desktop UI requires PySide6. "
            "Run scripts/run_gridguard_headless.py for headless execution. "
            f"Original import error: {_GUI_IMPORT_ERROR_TEXT}"
        )
    app = QApplication.instance()
    created = False
    if app is None:
        app = QApplication(sys.argv)
        created = True

    apply_dark_mode(app)

    global _DSS_LLM_WINDOW
    try:
        if _DSS_LLM_WINDOW is not None:
            _DSS_LLM_WINDOW.close()
    except Exception:
        pass

    _DSS_LLM_WINDOW = MainWindow()
    _DSS_LLM_WINDOW.show()

    if created:
        sys.exit(app.exec())

    return _DSS_LLM_WINDOW


if __name__ == "__main__":
    main()
