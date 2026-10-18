"""Executable standard-formulation companions; no LLM and no frozen-study edits.

1. Continuous two-control inverter P/Q participation OPF: local convex sensitivity
   QPs, conservative capability polygon, fresh selected-backend validation.
2. Small active-power restoration MILP: load pickup, energized topology, commodity
   connectivity, radiality and branch capacities; independent exhaustive check.
3. Identifiable linear WLS, chi-square and normalized residuals, a stealth Hc
   negative control, and constrained redispatch from protected toy measurements.

These are declared reduced teaching problems, not general full AC-OPF, field
switching, or attack-proof state estimation. Run: python -m src.standard_formulations
"""
from copy import deepcopy
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
import math
import time
import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, milp, minimize
from scipy.stats import chi2

ROOT = Path(__file__).resolve().parents[1]


def _json(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(type(value).__name__)


class PQBackend:
    """Separate P/Q adapter; existing solver files and network export stay intact.

    p_i=a*S_i, q_i=b*S_i because all supplied available inverter P equals kVA.
    The model verifies this condition. The control represents a common fleet
    participation signal, not 930 independent setpoint decisions.
    """
    def __init__(self, name, load_mult=1.):
        from . import lindistflow3 as linear
        if name not in ('opendss', 'lindistflow3'):
            raise ValueError('Unsupported backend')
        self.name, self.load_mult, self.linear = name, float(load_mult), linear
        if not math.isfinite(self.load_mult) or self.load_mult <= 0:
            raise ValueError('Demand multiplier must be positive and finite')
        if name == 'lindistflow3' and self.load_mult != 1.:
            raise ValueError('Linear P/Q demonstration currently uses nominal demand only')
        self.network = linear.load_network()
        self.pvs = self.network['pvs']
        self.s_total = sum(p['kva'] for p in self.pvs)
        if any(abs(min(p['pmpp_kw'] * p['irradiance'], p['kva']) - p['kva']) > 1e-8 for p in self.pvs):
            raise ValueError('This participation example assumes available P equals each inverter kVA')
        self.q_bounds = (-min(p['kvar_max_abs'] / p['kva'] for p in self.pvs),
                         min(p['kvar_max'] / p['kva'] for p in self.pvs))
        self.solves = 0

    def solve(self, x):
        a, b = map(float, x)
        if not np.isfinite([a, b]).all() or not 0 <= a <= 1 or not self.q_bounds[0] <= b <= self.q_bounds[1]:
            raise ValueError('P/Q control outside declared participation bounds')
        self.solves += 1
        if self.name == 'lindistflow3':
            net = deepcopy(self.network)
            # An ideal controlled reactive injection is algebraically a negative
            # reactive load. Preserve each original primary phase mapping.
            for pv in net['pvs']:
                net['loads'].append({**pv, 'name': 'pq_control_' + pv['name'],
                                     'kw': 0., 'kvar': -b * pv['kva'], 'critical': False})
                pv.update(pmpp_kw=a * pv['kva'], irradiance=1., pf=1., cutin_pct=0., cutout_pct=0.)
            m = self.linear.simulate(load_mult=self.load_mult, pv_cap=100., network=net, details=True)
            if not m.get('converged'):
                raise RuntimeError(m.get('unsupported_reasons', 'Linear solve failed'))
            # Load scaling must not scale the controllable kvar command.
            # The shipped example uses load_mult=1; reject other scaling here
            # until the adapter gives separate load/control participation.
            if self.load_mult != 1.:
                raise ValueError('Linear P/Q demonstration currently uses nominal demand only')
            phase = m['node_phase_voltages']
            if isinstance(phase, dict):
                ids, voltages = list(phase), list(phase.values())
            else:
                ids = [r.get('node', r.get('bus', '') + '.' + str(r.get('phase'))) for r in phase]
                voltages = [r.get('pu', r.get('voltage_pu')) for r in phase]
            lines = m['lines']
            p_actual, q_actual = m['pv_kw'], b * self.s_total
            max_p_error, max_q_error = 0., 0.
            converged = bool(m['converged'])
        else:
            from . import power_tools as power
            _, _, _, reachable, _, _, _ = power.reset(load_mult=self.load_mult, pv_cap=100.)
            dss = power.dss
            for pv in self.pvs:
                cap = 100 * a * pv['kva'] / pv['pmpp_kw']
                dss.Text.Command(f"edit PVSystem.{pv['name']} %Pmpp={cap:.12g} kvar={b * pv['kva']:.12g}")
            dss.Solution.Solve()
            converged = bool(dss.Solution.Converged())
            ids, voltages = [], []
            for name, value in zip(dss.Circuit.AllNodeNames(), dss.Circuit.AllBusMagPu()):
                if name.rsplit('.', 1)[-1] in ('1', '2', '3') and name.rsplit('.', 1)[0].lower() in reachable:
                    ids.append(name.lower()); voltages.append(float(value))
            lines = []
            for name in dss.Lines.AllNames():
                dss.Lines.Name(name)
                if not dss.CktElement.Enabled():
                    continue
                amps = max(dss.CktElement.CurrentsMagAng()[::2])
                rating = float(dss.CktElement.NormalAmps())
                if rating <= 0:
                    raise ValueError('Missing line rating')
                lines.append({'line': name, 'loading_pct': 100 * amps / rating})
            p_actual = q_actual = max_p_error = max_q_error = 0.
            rating_by_name = {pv['name'].lower(): pv['kva'] for pv in self.pvs}
            for name in dss.PVsystems.AllNames():
                dss.PVsystems.Name(name)
                p_value, q_value = float(dss.PVsystems.kW()), float(dss.PVsystems.kvar())
                p_actual += p_value
                q_actual += q_value
                rating = rating_by_name[name.lower()]
                max_p_error = max(max_p_error, abs(p_value - a * rating))
                max_q_error = max(max_q_error, abs(q_value - b * rating))
        v = np.asarray(voltages, float)
        current = np.array([r['loading_pct'] / 100 for r in lines], float)
        if (not len(v) or not len(current) or not np.isfinite(v).all() or not np.isfinite(current).all()
                or not np.isfinite([p_actual, q_actual, max_p_error, max_q_error]).all()):
            raise ValueError('Missing or invalid physical evidence')
        violations = {'voltage_low': int(np.sum(v < .95 - 1e-7)),
                      'voltage_high': int(np.sum(v > 1.05 + 1e-7)),
                      'line_current': int(np.sum(current > 1 + 1e-7)),
                      'inverter_capability': int(a * a + b * b > 1 + 1e-9),
                      'dispatch_tracking': int(max_p_error > 1e-5 or max_q_error > 1e-5)}
        return {'control': [a, b], 'p_requested_kw': a * self.s_total,
                'q_requested_kvar': b * self.s_total, 'p_actual_kw': p_actual,
                'q_actual_kvar': q_actual, 'vmin': float(v.min()), 'vmax': float(v.max()),
                'dispatch_mismatch_kw': float(p_actual - a * self.s_total),
                'dispatch_mismatch_kvar': float(q_actual - b * self.s_total),
                'max_device_p_mismatch_kw': max_p_error, 'max_device_q_mismatch_kvar': max_q_error,
                'max_line_utilization_pct': float(current.max() * 100),
                'converged': converged, 'violations': violations,
                'accepted': converged and not any(violations.values()),
                'voltage_ids': ids, 'voltages_pu': v.tolist(),
                'line_ids': [r['line'] for r in lines], 'current_pu': current.tolist()}


def capability_polygon(sides=32):
    """Inscribed regular polygon: vertices, rather than facets, touch the circle."""
    angles = 2 * np.pi * (np.arange(sides) + .5) / sides
    return np.c_[np.cos(angles), np.sin(angles)], np.full(sides, np.cos(np.pi / sides))


def run_voltvar(backend='opendss', load_mult=1., max_iterations=10):
    started = time.perf_counter()
    physical = PQBackend(backend, load_mult)
    baseline = physical.solve([1., 0.])
    x = np.array([.25, 0.])
    current = physical.solve(x)
    if not current['accepted']:
        raise RuntimeError('Declared initial P/Q point is not feasible; no optimizer result claimed')
    polygon, polygon_rhs = capability_polygon()
    trace = []
    trust = .3
    # Convex objective: retain solar P, discourage large reactive use, and
    # discourage modeled voltage deviation. Normalization is stated, not tuned
    # after observing one backend's result.
    def cost(point, voltages):
        return float((1 - point[0]) ** 2 + .05 * point[1] ** 2 +
                     10 * np.mean((np.asarray(voltages) - 1.01) ** 2))
    for iteration in range(max_iterations):
        v0, i0 = np.asarray(current['voltages_pu']), np.asarray(current['current_pu'])
        jv, ji = np.zeros((len(v0), 2)), np.zeros((len(i0), 2))
        h = .001
        for k in range(2):
            lo, hi = x.copy(), x.copy()
            lo[k] = max(0. if k == 0 else physical.q_bounds[0], x[k] - h)
            hi[k] = min(1. if k == 0 else physical.q_bounds[1], x[k] + h)
            left, right = physical.solve(lo), physical.solve(hi)
            if (left['voltage_ids'] != right['voltage_ids'] or left['line_ids'] != right['line_ids'] or
                    current['voltage_ids'] != left['voltage_ids'] or current['line_ids'] != left['line_ids']):
                raise ValueError('Sensitivity rows are not aligned')
            jv[:, k] = (np.array(right['voltages_pu']) - left['voltages_pu']) / (hi[k] - lo[k])
            ji[:, k] = (np.array(right['current_pu']) - left['current_pu']) / (hi[k] - lo[k])
        matrix = np.vstack([jv, ji, polygon])
        lower = np.r_[np.full(len(v0), .9502) - v0 + jv @ x,
                      np.full(len(i0), -np.inf), np.full(len(polygon), -np.inf)]
        upper = np.r_[np.full(len(v0), 1.0498) - v0 + jv @ x,
                      np.full(len(i0), .995) - i0 + ji @ x, polygon_rhs]
        def objective(y):
            return cost(y, v0 + jv @ (y - x))
        def gradient(y):
            predicted = v0 + jv @ (y - x)
            return np.array([-2 * (1 - y[0]), .1 * y[1]]) + 20 * jv.T @ (predicted - 1.01) / len(v0)
        result = minimize(objective, x, jac=gradient, method='SLSQP',
                          bounds=Bounds(np.maximum([0., physical.q_bounds[0]], x - trust),
                                        np.minimum([1., physical.q_bounds[1]], x + trust)),
                          constraints=[LinearConstraint(matrix, lower, upper)],
                          options={'ftol': 1e-11, 'maxiter': 150})
        qp_violation = max(float(np.max(np.maximum(lower - matrix @ result.x, 0))),
                           float(np.max(np.maximum(matrix @ result.x - upper, 0))))
        entry = {'iteration': iteration + 1, 'linearization_control': x.tolist(),
                 'qp_success': bool(result.success), 'qp_message': result.message,
                 'qp_control': result.x.tolist(), 'qp_constraint_violation': qp_violation,
                 'objective_before': cost(x, v0)}
        if not result.success or qp_violation > 1e-6:
            entry['disposition'] = 'retain_last_verified_feasible_point'; trace.append(entry); break
        chosen = None
        for fraction in (1., .5, .25, .125, .0625):
            trial_x = np.clip(x + fraction * (result.x - x), [0., physical.q_bounds[0]], [1., physical.q_bounds[1]])
            trial = physical.solve(trial_x)
            if trial['accepted'] and cost(trial_x, trial['voltages_pu']) <= entry['objective_before'] + 1e-9:
                chosen = (trial_x, trial, fraction); break
        if chosen is None:
            entry['disposition'] = 'no_verified_improving_step'; trace.append(entry); break
        new_x, new_point, fraction = chosen
        entry.update(disposition='accepted_fresh_backend_solve', line_search_fraction=fraction,
                     control=new_x.tolist(), objective_after=cost(new_x, new_point['voltages_pu']),
                     validation=new_point['violations'])
        trace.append(entry)
        delta = np.linalg.norm(new_x - x, ord=np.inf)
        x, current = new_x, new_point
        if delta < 1e-5:
            break
    optimized = physical.solve(x)
    optimized['objective'] = cost(x, optimized['voltages_pu'])
    baseline['objective'] = cost([1., 0.], baseline['voltages_pu'])
    optimized['curtailed_available_kw'] = physical.s_total - optimized['p_actual_kw']
    return {'backend': backend, 'scope': 'full supplied feeder' if backend == 'opendss' else 'MV phases only',
            'formulation': {'kind': 'continuous one-step P/Q participation OPF via local convex sensitivity QPs',
                            'variables': 'a in [0,1], b in common inverter kvar/kVA bounds; p_i=a*S_i, q_i=b*S_i',
                            'objective': '(1-a)^2 + 0.05*b^2 + 10*mean((v_pred-1.01)^2)',
                            'inverter_capability': '32-side inscribed polygon within a^2+b^2<=1',
                            'linear_constraints': '0.9502<=v_pred<=1.0498; I_pred/I_rating<=0.995',
                            'physical_checks': '0.95<=v<=1.05; actual I/I_rating<=1; inverter circle',
                            'solver': 'SciPy SLSQP solving quadratic objective with linear constraints',
                            'finite_difference_step': .001, 'trust_radius': trust,
                            'available_p_kw': physical.s_total, 'inverter_count': len(physical.pvs)},
            'baseline': baseline, 'optimized': optimized, 'solver_trace': trace,
            'validation': {'fresh_backend_accepted': optimized['accepted'], 'backend_solves': physical.solves},
            'seconds': time.perf_counter() - started,
            'limits': ['Two shared participation controls, not independent inverter OPF.',
                       'Local sensitivity/sequential-QP solution, not a global nonlinear AC optimum.',
                       'Fixed nominal demand; no forecast horizon, energy states, or robust guarantees.',
                       'Linear reactive injections use ideal primary aggregation; full AC uses PV kvar commands.',
                       'Voltage/current model coverage differs between backends.']}


def restoration_graph(capacity_kw=220.):
    if not math.isfinite(capacity_kw) or capacity_kw < 0:
        raise ValueError('Synthetic tie active-power capacity must be finite and nonnegative')
    return {'nodes': list(range(6)), 'source': 0, 'demand_kw': [0., 40., 60., 70., 50., 30.],
            'priority': [0., 1., 10., 1., 1., 10.],
            'edges': [{'name': 'source_healthy', 'u': 0, 'v': 1, 'capacity_kw': 300., 'available': True},
                      {'name': 'faulted_segment', 'u': 1, 'v': 2, 'capacity_kw': 250., 'available': False},
                      {'name': 'section_23', 'u': 2, 'v': 3, 'capacity_kw': 250., 'available': True},
                      {'name': 'section_34', 'u': 3, 'v': 4, 'capacity_kw': 250., 'available': True},
                      {'name': 'section_25', 'u': 2, 'v': 5, 'capacity_kw': 250., 'available': True},
                      {'name': 'tie_04', 'u': 0, 'v': 4, 'capacity_kw': float(capacity_kw), 'available': True},
                      {'name': 'tie_15', 'u': 1, 'v': 5, 'capacity_kw': 100., 'available': True}]}


def _enumerate_restoration(graph):
    edges, n = graph['edges'], len(graph['nodes'])
    demand, weight = np.array(graph['demand_kw']), np.array(graph['priority'])
    best, best_row, examined = -np.inf, None, 0
    for bits in product((0, 1), repeat=len(edges)):
        if any(bit and not edge['available'] for bit, edge in zip(bits, edges)):
            continue
        adj = {i: [] for i in range(n)}
        for e, (bit, edge) in enumerate(zip(bits, edges)):
            if bit:
                adj[edge['u']].append((edge['v'], e)); adj[edge['v']].append((edge['u'], e))
        parent, order, parent_edge = {0: None}, [0], {}
        for node in order:
            for other, e in adj[node]:
                if other not in parent:
                    parent[other], parent_edge[other] = node, e; order.append(other)
        if sum(bits) != len(order) - 1 or any(bits[e] and (edge['u'] not in parent or edge['v'] not in parent)
                                            for e, edge in enumerate(edges)):
            continue
        for pickup in product((0, 1), repeat=n - 1):
            served = np.array([0, *pickup])
            if any(served[i] and i not in parent for i in range(n)):
                continue
            examined += 1
            flow, accumulated = np.zeros(len(edges)), demand * served
            for node in order[:0:-1]:
                flow[parent_edge[node]] = accumulated[node]
                accumulated[parent[node]] += accumulated[node]
            if any(flow[e] > edge['capacity_kw'] + 1e-8 for e, edge in enumerate(edges)):
                continue
            value = float(np.dot(demand * weight, served))
            if value > best:
                best, best_row = value, {'pickup': served.tolist(), 'closed_edges': [e['name'] for b, e in zip(bits, edges) if b]}
    return {'objective': best, 'solution': best_row, 'enumerated_tree_load_combinations': examined}


def solve_restoration_milp(capacity_kw=220.):
    graph = restoration_graph(capacity_kw)
    n, m = len(graph['nodes']), len(graph['edges'])
    # x=[energized(n),pickup(n),closed(m),commodity(m),active_flow(m)].
    ze, zl, ye, fc, fp = 0, n, 2 * n, 2 * n + m, 2 * n + 2 * m
    nv = 2 * n + 3 * m
    lower, upper = np.zeros(nv), np.ones(nv)
    lower[0] = upper[0] = 1; upper[n] = 0
    lower[fc:fc + m], upper[fc:fc + m] = -(n - 1), n - 1
    caps = np.array([e['capacity_kw'] for e in graph['edges']])
    lower[fp:], upper[fp:] = -caps, caps
    integrality = np.zeros(nv); integrality[:fc] = 1
    rows, lows, highs = [], [], []
    def add(coeffs, lo=-np.inf, hi=np.inf):
        row = np.zeros(nv)
        for index, value in coeffs.items(): row[index] = value
        rows.append(row); lows.append(lo); highs.append(hi)
    for i in range(1, n): add({zl + i: 1, ze + i: -1}, hi=0)
    incidence = np.zeros((n, m))  # positive arrival at v, negative departure at u
    for e, edge in enumerate(graph['edges']):
        u, v = edge['u'], edge['v']
        incidence[u, e], incidence[v, e] = -1, 1
        if not edge['available']: upper[ye + e] = 0
        for endpoint in (u, v): add({ye + e: 1, ze + endpoint: -1}, hi=0)
        for offset, cap in ((fc, n - 1), (fp, caps[e])):
            add({offset + e: 1, ye + e: -cap}, hi=0)
            add({offset + e: -1, ye + e: -cap}, hi=0)
    for i in range(1, n):
        add({**{fc + e: incidence[i, e] for e in range(m)}, ze + i: -1}, lo=0, hi=0)
        add({**{fp + e: incidence[i, e] for e in range(m)}, zl + i: -graph['demand_kw'][i]}, lo=0, hi=0)
    add({**{fc + e: incidence[0, e] for e in range(m)}, **{ze + i: 1 for i in range(1, n)}}, lo=0, hi=0)
    add({**{ye + e: 1 for e in range(m)}, **{ze + i: -1 for i in range(1, n)}}, lo=0, hi=0)
    reward = np.array(graph['demand_kw']) * graph['priority']
    objective = np.zeros(nv); objective[zl:zl + n] = -reward
    constraint = LinearConstraint(np.array(rows), lows, highs)
    started = time.perf_counter()
    solved = milp(objective, integrality=integrality, bounds=Bounds(lower, upper), constraints=constraint,
                  options={'mip_rel_gap': 0.})
    if not solved.success: raise RuntimeError(solved.message)
    optimum = -float(solved.fun)
    # Explicit lexicographic second stage: preserve service, then minimize
    # energized branches. This is not switch operations from a prior topology.
    add({zl + i: reward[i] for i in range(n)}, lo=optimum - 1e-7)
    secondary = np.zeros(nv); secondary[ye:ye + m] = 1 + .001 * np.arange(m)
    final = milp(secondary, integrality=integrality, bounds=Bounds(lower, upper),
                 constraints=LinearConstraint(np.array(rows), lows, highs), options={'mip_rel_gap': 0.})
    if not final.success: raise RuntimeError(final.message)
    x = final.x; pickup = np.rint(x[zl:zl + n]).astype(int)
    exhaustive = _enumerate_restoration(graph)
    row = {'objective': float(reward @ pickup), 'served_kw': float(np.dot(graph['demand_kw'], pickup)),
           'critical_served_kw': float(sum(graph['demand_kw'][i] * pickup[i] for i in range(n) if graph['priority'][i] == 10)),
           'pickup': pickup.tolist(), 'energized': np.rint(x[:n]).astype(int).tolist(),
           'closed_edges': [edge['name'] for e, edge in enumerate(graph['edges']) if x[ye + e] > .5],
           'branch_flows_kw': {edge['name']: float(x[fp + e]) for e, edge in enumerate(graph['edges'])},
           'solver': 'SciPy milp / HiGHS', 'success': True, 'message': final.message,
           'mip_gap': float(final.mip_gap), 'seconds': time.perf_counter() - started}
    return {'graph': graph, 'milp': row, 'enumeration': exhaustive,
            'agreement': abs(row['objective'] - exhaustive['objective']) < 1e-6,
            'secondary_objective': 'Preserve maximum weighted pickup, then minimize energized branch count with 0.001*edge-index tie-break; not switching operations.',
            'formulation': 'binary pickup/energization/switches; single-commodity connectivity; radial edge count; signed active-power balances and capacities',
            'limits': ['Six-node explicitly synthetic sectional graph, not an extracted Greensboro switching model.',
                       'Active-power transport capacities; no AC voltages, reactive power or protection sequencing.',
                       'Commodity flow enforces source connectivity; edge count alone is not the radiality method.',
                       'Discrete load pickup; only the given graph and catalog of switches are represented.']}


def weighted_least_squares(H, z, sigma, alpha=.01):
    H, z, sigma = np.asarray(H, float), np.asarray(z, float), np.asarray(sigma, float)
    if H.ndim != 2 or z.shape != (len(H),) or sigma.shape != z.shape or not np.isfinite(H).all() or not np.isfinite(z).all() or not np.isfinite(sigma).all() or np.any(sigma <= 0):
        raise ValueError('Invalid measurement model')
    if not math.isfinite(alpha) or not 0 < alpha < 1:
        raise ValueError('Significance alpha must be between zero and one')
    rank = int(np.linalg.matrix_rank(H))
    if rank != H.shape[1]: raise ValueError('State is not observable: H is rank deficient')
    weighted_H, weighted_z = H / sigma[:, None], z / sigma
    covariance = np.linalg.solve(weighted_H.T @ weighted_H, np.eye(H.shape[1]))
    estimate = np.linalg.lstsq(weighted_H, weighted_z, rcond=None)[0]
    residual = z - H @ estimate
    omega = np.diag(sigma ** 2) - H @ covariance @ H.T
    diagonal = np.diag(omega)
    valid = diagonal > 1e-10 * sigma ** 2
    normalized = np.full(len(z), np.nan)
    normalized[valid] = np.abs(residual[valid]) / np.sqrt(diagonal[valid])
    dof = len(z) - rank
    statistic = float(np.sum((residual / sigma) ** 2))
    threshold = float(chi2.ppf(1 - alpha, dof)) if dof > 0 else None
    return {'estimate': estimate.tolist(), 'covariance': covariance.tolist(), 'rank': rank,
            'residual': residual.tolist(), 'normalized_residuals': [float(v) if math.isfinite(v) else None for v in normalized],
            'undefined_normalized_residual_indices': np.flatnonzero(~valid).tolist(),
            'chi_square': {'statistic': statistic, 'degrees_of_freedom': dof, 'alpha': alpha,
                           'threshold': threshold, 'alarm': statistic > threshold if threshold is not None else None},
            'largest_normalized_residual': int(np.nanargmax(normalized)) if valid.any() else None}


def _redispatch(estimate, true_state, F, B):
    # One flexible injection at non-slack node 2, balanced by the slack source.
    direction = np.array([0., 1., 0.])
    sensitivity = F @ np.linalg.solve(B, direction)
    forecast_flow = F @ np.asarray(estimate)
    limits = np.array([.35, .18, .35, .35]); margin = .01
    answer = minimize(lambda u: .5 * float(u[0] ** 2), [0.], jac=lambda u: np.array([u[0]]),
                      bounds=Bounds([0.], [.5]),
                      constraints=[LinearConstraint(sensitivity[:, None], -limits + margin - forecast_flow,
                                                    limits - margin - forecast_flow)], method='SLSQP',
                      options={'ftol': 1e-12})
    if not answer.success: return {'status': 'HOLD', 'reason': answer.message}
    actual = F @ np.asarray(true_state) + sensitivity * answer.x[0]
    predicted = forecast_flow + sensitivity * answer.x[0]
    if (not np.isfinite(answer.x).all() or not np.isfinite(predicted).all() or
            not np.isfinite(actual).all() or not -1e-8 <= answer.x[0] <= .5 + 1e-8 or
            np.any(np.abs(predicted) > limits - margin + 1e-8)):
        return {'status': 'HOLD', 'reason': 'Independent post-solve constraint check failed'}
    return {'status': 'PROPOSE', 'flexible_injection_pu': float(answer.x[0]),
            'predicted_flows_pu': predicted.tolist(), 'actual_toy_model_flows_pu': actual.tolist(),
            'line_limits_pu': limits.tolist(), 'planning_margin_pu': margin,
            'actual_violation_count': int(np.sum(np.abs(actual) > limits + 1e-8)),
            'objective': float(answer.fun), 'model': 'Three-state DC network, not the distribution-feeder AC model'}


def run_wls_demo():
    incidence = np.array([[-1., 0, 0], [1., -1., 0], [0, 1., -1.], [0, 0, -1.]])
    F = np.diag([10., 8., 10., 5.]) @ incidence
    B = incidence.T @ F
    H = np.vstack([F, B, [1., 0., 0.]])
    sigma = np.array([.004] * 4 + [.006] * 3 + [.0005])
    truth = np.array([-.02, -.05, -.04])
    noise = np.random.default_rng(11).normal(size=len(H)) * sigma
    clean = H @ truth + noise
    isolated = clean.copy(); isolated[1] += .08
    shift = np.array([.01, .025, 0.])
    stealth = clean + H @ shift
    cases = []
    for name, measurements in [('nominal_noise', clean), ('isolated_corruption', isolated), ('stealth_Hc', stealth)]:
        fit = weighted_least_squares(H, measurements, sigma)
        control = ({'status': 'HOLD', 'reason': 'Residual alarm blocks redispatch from untrusted estimate'}
                   if fit['chi_square']['alarm'] else _redispatch(fit['estimate'], truth, F, B))
        cases.append({'name': name, 'measurements': measurements.tolist(), **fit,
                      'state_error_norm': float(np.linalg.norm(np.array(fit['estimate']) - truth)), 'control': control})
    suspect = cases[1]['largest_normalized_residual']
    keep = np.arange(len(H)) != suspect
    removal = weighted_least_squares(H[keep], isolated[keep], sigma[keep])
    protected_sigma = np.full(3, .00005)
    protected = truth + np.random.default_rng(21).normal(size=3) * protected_sigma
    recovery = weighted_least_squares(np.eye(3), protected, protected_sigma)
    recovery['control'] = _redispatch(recovery['estimate'], truth, F, B)
    return {'measurement_model': {'H': H.tolist(), 'sigma': sigma.tolist(), 'true_state': truth.tolist(),
                                  'state': 'three non-slack DC voltage angles in radians',
                                  'measurements': ['flow01', 'flow12', 'flow23', 'flow03', 'injection1', 'injection2', 'injection3', 'angle1'],
                                  'noise_seed': 11, 'attack_sensor_index': 1, 'isolated_bias': .08,
                                  'stealth_shift': shift.tolist(), 'stealth_attack': (H @ shift).tolist()},
            'cases': cases, 'isolated_removal': {'removed_index': suspect, **removal},
            'trusted_recovery': {'protected_H': np.eye(3).tolist(), 'protected_measurements': protected.tolist(),
                                 'protected_sigma': protected_sigma.tolist(), 'noise_seed': 21, **recovery},
            'limitations': ['Identifiable four-bus DC example, not feeder-wide distribution state estimation.',
                            'Chi-square calibration assumes the stated independent Gaussian noise and correct linear model.',
                            'Largest normalized residual is a localization heuristic, not a guaranteed attacker identifier.',
                            'Stealth attack assumes knowledge of H and control of all unprotected measurement channels.',
                            'Protected recovery assumes three independent trustworthy angle measurements; authentication is not implemented.',
                            'Exactly determined trusted recovery has zero residual degrees of freedom and no chi-square detection claim.',
                            'Redispatch is a scalar DC constrained-control demonstration with a stated engineering margin, not AC cyber resilience.']}


def make_plots(data):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    folder = ROOT / 'figures'; folder.mkdir(exist_ok=True)
    fig, axes = plt.subplots(1, len(data['voltvar']), figsize=(12, 4), squeeze=False)
    for ax, (backend, row) in zip(axes[0], data['voltvar'].items()):
        for key, color in [('baseline', '#c77630'), ('optimized', '#007f83')]:
            point = row[key]
            ax.plot(np.sort(point['voltages_pu']), label=key, color=color, lw=1.7)
        ax.axhline(1.05, ls='--', color='#a7353d', lw=1); ax.axhline(.95, ls='--', color='#a7353d', lw=1)
        ax.set(title=backend + (' · full feeder' if backend == 'opendss' else ' · MV only'),
               xlabel='Sorted phase-voltage sample', ylabel='Voltage (p.u.)'); ax.legend()
    fig.suptitle('Continuous P/Q OPF: compare within each model scope'); fig.tight_layout()
    fig.savefig(folder / 'standard_voltvar.png', dpi=180); plt.close(fig)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    labels = ['Normal tie', 'Limited tie']
    served = [data['restoration'][k]['milp']['served_kw'] for k in ('normal', 'limited')]
    critical = [data['restoration'][k]['milp']['critical_served_kw'] for k in ('normal', 'limited')]
    axes[0].bar(labels, served, color='#b6d9d8', label='All connected demand')
    axes[0].bar(labels, critical, color='#007f83', label='Critical portion')
    axes[0].set(title='MILP: weighted load restoration', ylabel='Nominal demand (kW)'); axes[0].legend()
    rows = data['cyber']['cases']
    axes[1].bar(['Noise', 'Isolated error', 'Stealth Hc'], [r['chi_square']['statistic'] for r in rows], color=['#007f83', '#c77630', '#a7353d'])
    axes[1].axhline(rows[0]['chi_square']['threshold'], ls='--', color='black', label='1% chi-square threshold')
    axes[1].set(title='WLS residual test: stealth negative control', ylabel='Weighted residual statistic'); axes[1].legend()
    fig.tight_layout(); fig.savefig(folder / 'standard_restoration_wls.png', dpi=180); plt.close(fig)


def run_all(backends=('opendss', 'lindistflow3'), plots=True):
    data = {'metadata': {'created_utc': datetime.now(timezone.utc).isoformat(), 'scipy_version': scipy.__version__,
                         'numpy_version': np.__version__, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                         'scope': 'New standard-formulation teaching companions; separate from all frozen workflow/request studies.'},
            'voltvar': {}, 'restoration': {}, 'cyber': None}
    for backend in backends:
        print('Continuous P/Q OPF:', backend, flush=True)
        data['voltvar'][backend] = run_voltvar(backend)
    if 'opendss' in backends and 'lindistflow3' in backends:
        audit = PQBackend('opendss').solve(data['voltvar']['lindistflow3']['optimized']['control'])
        data['voltvar']['lindistflow3']['reference_full_ac_audit'] = audit
    for label, capacity in [('normal', 220.), ('limited', 100.)]:
        data['restoration'][label] = solve_restoration_milp(capacity)
    data['cyber'] = run_wls_demo()
    target = ROOT / 'results/standard_formulations.json'
    target.write_text(json.dumps(data, indent=2, default=_json, allow_nan=False), encoding='utf-8')
    if plots: make_plots(data)
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--backend', choices=('both', 'opendss', 'lindistflow3'), default='both')
    parser.add_argument('--no-plots', action='store_true')
    args = parser.parse_args()
    run_all(('opendss', 'lindistflow3') if args.backend == 'both' else (args.backend,), not args.no_plots)
