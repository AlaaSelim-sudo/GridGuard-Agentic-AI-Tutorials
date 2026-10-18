"""Numerical tools with one candidate schema; no LLM dependency.

MPC uses a finite-action nonlinear AC lookup over a three-step horizon.
It is deliberately small enough to inspect in a class, not a continuous OPF.
"""
from dataclasses import dataclass, asdict
from functools import lru_cache
from pathlib import Path
import hashlib, json, time, math
import numpy as np
from .power_tools import ROOT, DATA, simulate, verify_physics

CAPS = np.array([0, 10, 20, 30, 40, 60, 80, 100], dtype=float)
LOADS = np.array([.3, .5, .7, 1., 1.3])
HORIZON, GAMMA, SWITCH_COST = 3, .95, .15

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def provenance():
    return {'feeder': {p.name: digest(p) for p in sorted(DATA.glob('*.dss'))},
            'physics_code': digest(ROOT/'src/power_tools.py'),
            'control_code': digest(__file__), 'caps': CAPS.tolist(),
            'loads': LOADS.tolist(), 'horizon': HORIZON,
            'gamma': GAMMA, 'switch_cost': SWITCH_COST,
            'voltage_limits': [.95, 1.05], 'cache_schema': 2}

def ac_table(rebuild=False):
    """Regenerate whenever feeder, preparation, constraints or catalog changes."""
    path = ROOT/'results/ac_table.json'
    manifest = provenance()
    if path.exists() and not rebuild:
        saved = json.loads(path.read_text())
        if saved.get('manifest') == manifest:
            return saved['data']
    # Recreate syntax-adjusted copies even when files from an earlier run exist.
    from .power_tools import prepare
    prepare()
    start = time.perf_counter()
    data = [[simulate(load_mult=float(load), pv_cap=float(cap), details=True)
             for cap in CAPS] for load in LOADS]
    path.write_text(json.dumps({'manifest': manifest, 'data': data}))
    (ROOT/'results/table_cost.json').write_text(json.dumps(
        {'ac_solves': 40, 'seconds': time.perf_counter()-start}, indent=2))
    return data

@dataclass(frozen=True)
class Candidate:
    tool: str
    pv_cap: float
    tie: str = 'none'
    shed_fraction: float = 0.

@dataclass(frozen=True)
class Case:
    id: str
    task: str = 'voltage'
    forecast: tuple = (3, 2, 1)  # indices into LOADS; known forecasts in this lab
    previous: int = 2           # previous cap index, not an inferred safe fallback
    rating_fraction: float = 1.
    fault: bool = False
    capacity: float = 400.
    pv_available: bool = True
    long_available: bool = True

    @property
    def load(self):
        return float(LOADS[self.forecast[0]])

def case_failures(case):
    if not isinstance(case, Case):
        return ['invalid_case']
    finite = lambda x: not isinstance(x, bool) and isinstance(x, (int,float)) and math.isfinite(x)
    integer = lambda x: isinstance(x, int) and not isinstance(x, bool)
    if (not isinstance(case.id, str) or not case.id or case.task not in ('voltage','restoration')
        or not isinstance(case.forecast, (tuple,list)) or not case.forecast
        or any(not integer(i) or not 0 <= i < len(LOADS) for i in case.forecast)
        or not integer(case.previous) or not 0 <= case.previous < len(CAPS)
        or not finite(case.rating_fraction) or not 0 < case.rating_fraction <= 1
        or not finite(case.capacity) or case.capacity <= 0
        or any(type(v) is not bool for v in (case.fault,case.pv_available,case.long_available))):
        return ['invalid_case']
    return []

def compact(m, rating_fraction=1.):
    keys = ['converged', 'vmin', 'vmax', 'voltage_violations', 'served_kw',
            'unserved_kw', 'critical_served_kw', 'critical_total_kw', 'pv_kw',
            'losses_kw', 'mv_cycles', 'topology_hash', 'physical_load_disconnects']
    result = {k: m[k] for k in keys}
    result.update(max_line_pct=m['max_line_pct']/rating_fraction,
                  overloaded_lines=sum(r['loading_pct'] is not None and
                    r['loading_pct']/rating_fraction > 100+1e-4 for r in m['lines']))
    if m.get('tie_loading_pct') is not None:
        result['tie_loading_pct'] = m['tie_loading_pct']/rating_fraction
    return result

def utility(T, load_index, action_index, previous):
    return float(T[load_index][action_index]['pv_kw']/8000 -
                 SWITCH_COST*abs(CAPS[action_index]-CAPS[previous])/100)

def observation(case, remaining=1.):
    seq = list(case.forecast)
    future = [LOADS[seq[min(k, len(seq)-1)]]/1.3 for k in range(HORIZON)]
    return np.array(future+[CAPS[case.previous]/100, case.rating_fraction, remaining])

def mpc(T, case):
    """Bellman recursion, with -infinity propagated through infeasible futures."""
    started = time.perf_counter()
    if case_failures(case):
        return {'status': 'ESCALATE', 'candidate': None, 'reason': 'invalid_case', 'fresh_ac_solves': 0}
    forecast = tuple(case.forecast[:HORIZON])
    feasible = {(k, a): not verify_physics(T[li][a], rating_fraction=case.rating_fraction)
                for k, li in enumerate(forecast) for a in range(len(CAPS))}
    @lru_cache(None)
    def value(k, previous):
        if k == len(forecast):
            return 0., ()
        best = (-math.inf, ())
        for a in range(len(CAPS)):
            if not feasible[k, a]:
                continue
            tail_value, tail = value(k+1, a)
            if not math.isfinite(tail_value):
                continue
            score = utility(T, forecast[k], a, previous)+GAMMA*tail_value
            if score > best[0]:
                best = score, (a,)+tail
        return best
    score, actions = value(0, case.previous)
    return {'status': 'PROPOSE' if actions else 'ESCALATE',
            'candidate': asdict(Candidate('MPC', float(CAPS[actions[0]]))) if actions else None,
            'reason': 'finite_action_horizon_optimum' if actions else 'no_feasible_horizon',
            'plan_caps': [float(CAPS[a]) for a in actions],
            'objective': score if actions else None,
            'seconds': time.perf_counter()-started, 'fresh_ac_solves': 0}

def drl(net, case):
    started = time.perf_counter()
    q = net.forward(observation(case)[None])[0][0]
    a = int(q.argmax())
    return {'status': 'PROPOSE', 'candidate': asdict(Candidate('DRL', float(CAPS[a]))),
            'reason': 'greedy_DQN_value', 'q_values': q.tolist(),
            'seconds': time.perf_counter()-started, 'fresh_ac_solves': 0}

def simulate_candidate(case, candidate):
    return simulate(load_mult=case.load, pv_cap=candidate.pv_cap,
                    fault=case.fault, tie=candidate.tie, capacity=case.capacity,
                    shed_fraction=candidate.shed_fraction, details=True)

def action_failures(case, candidate):
    if case_failures(case):
        return ['invalid_case']
    if not isinstance(candidate, Candidate):
        return ['invalid_candidate']
    failures = []
    if candidate.tool not in ('MPC', 'DRL', 'RESTORATION_SEARCH'):
        failures.append('unknown_tool')
    if isinstance(candidate.pv_cap, bool) or not isinstance(candidate.pv_cap, (float, int)) or not math.isfinite(candidate.pv_cap) or candidate.pv_cap not in CAPS:
        failures.append('invalid_pv_cap')
    if isinstance(candidate.shed_fraction, bool) or not isinstance(candidate.shed_fraction, (float, int)) or not math.isfinite(candidate.shed_fraction) or not 0 <= candidate.shed_fraction <= 1:
        failures.append('invalid_shedding')
    if candidate.tie not in ('none', 'short', 'long', 'both', 'fault'):
        failures.append('unknown_switch')
    if case.fault and candidate.tie == 'fault':
        failures.append('fault_quarantine')
    if not case.long_available and candidate.tie in ('long', 'both'):
        failures.append('unavailable_tie')
    if not case.pv_available and candidate.pv_cap != 0:
        failures.append('unavailable_pv')
    if case.task == 'voltage' and (candidate.tie != 'none' or candidate.shed_fraction != 0):
        failures.append('wrong_control_scope')
    return failures

def restoration_search(case):
    """Enumerate a small teaching catalog, maximize weighted connected demand."""
    start = time.perf_counter()
    cap = 20. if case.pv_available else 0.
    choices = [Candidate('RESTORATION_SEARCH', cap, 'short', f)
               for f in [0., .25, .5, .65, .75, .9]]
    if case.long_available:
        choices.append(Candidate('RESTORATION_SEARCH', cap, 'long'))
    rows = []
    for c in choices:
        m = simulate_candidate(case, c)
        failures = action_failures(case, c)+verify_physics(m, allow_unserved=True, rating_fraction=case.rating_fraction)
        if m['served_kw'] <= .1:
            failures.append('no_service_restored')
        rows.append({'candidate': asdict(c), 'failures': failures,
                     'metrics': compact(m, case.rating_fraction),
                     'objective': m['served_kw']+9*m['critical_served_kw']})
    passing = [r for r in rows if not r['failures']]
    best = max(passing, key=lambda r: (r['objective'], -r['metrics']['losses_kw'])) if passing else None
    return {'status': 'PROPOSE' if best else 'ESCALATE',
            'candidate': best['candidate'] if best else None,
            'reason': 'best_in_catalog' if best else 'no_feasible_restoration',
            'catalog': rows, 'seconds': time.perf_counter()-start,
            'fresh_ac_solves': len(rows)}
