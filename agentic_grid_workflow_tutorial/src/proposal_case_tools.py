"""Numerical adapters for the complete five-stage proposal demonstration.

These tools propose, simulate, independently check, and score bounded actions.
They do not call an LLM, dispatch equipment, modify the older studies, or imply
that a language model improves an already optimal numerical solution.  Both
supervisors receive these same tools and the same candidate-evaluation budget.
"""
from copy import deepcopy
import hashlib
import json
import math
import time

import numpy as np


def _json(value):
    """Return ordinary JSON values and reject non-finite evidence."""
    def convert(item):
        if isinstance(item, np.ndarray):
            return item.tolist()
        if isinstance(item, np.generic):
            return item.item()
        raise TypeError(type(item).__name__)
    return json.loads(json.dumps(value, default=convert, allow_nan=False))


def _digest(value):
    return hashlib.sha256(json.dumps(_json(value), sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def _finite(value):
    return type(value) in (int, float) and math.isfinite(value)


def _best(history):
    valid = [row for row in history if not row.get('failures')
             and _finite(row.get('score'))]
    return min(valid, key=lambda row: row['score']) if valid else None


def _unused(candidate, history):
    """Ignore labels when deciding whether a physical command was tested."""
    def physical(row):
        return {key: value for key, value in row.items()
                if key not in ('tool', 'operation', 'description', 'id')}
    return all(_digest(physical(candidate)) != _digest(physical(row['candidate']))
               for row in history)


class VoltageAdapter:
    """SAC + finite-horizon model-based planning, then bounded local trials."""
    def __init__(self, backend):
        from .continuous_control import ContinuousCase, ContinuousPlant
        self.backend = backend
        self.case = ContinuousCase('proposal_voltage', (1., .94, 1.06),
                                   rating_fraction=.8, previous=(.25, 0.))
        self.plant = ContinuousPlant(backend)
        self.scope = self.plant.scope + '; current first action only at final gate'
        self.objective = ('Minimize current-step J=(1-a)^2+0.05*b^2+'
                          '10*mean((V-1.01)^2)+0.05*||[a,b]-previous||^2; '
                          'MPC supplies a horizon-informed first action.')
        self.setup, self.setup_seconds = {}, 0.
        self.mpc, self.sac = None, None

    def awareness(self):
        from .continuous_control import compact, verify_control
        point = self.plant.solve(self.case.previous, self.case.forecast_loads[0],
                                 self.case.rating_fraction)
        return _json({'method': 'Fresh model snapshot and structured operating contract',
            'measurements': compact(point), 'alarms': verify_control(point, self.case),
            'topology': {'operation': 'unchanged supplied radial feeder',
                         'switching_authorized': False},
            'der': {'availability': '930 supplied inverters; common fleet a,b',
                    'P_fraction_bounds': [0., 1.], 'Q_fraction_bounds': [-.44, .44],
                    'capability': 'a^2+b^2 <= 1'},
            'forecast_load_multipliers': list(self.case.forecast_loads),
            'current_allowance_fraction': self.case.rating_fraction,
            'scope': self.scope, 'fresh_model_solve': True,
            'operational_limit': 'Forecast supplied, not learned; no telemetry ingestion or hardware execution.'})

    def plan(self):
        from .continuous_control import optimize_mpc, sac_proposal
        from .continuous_workflow import plan_failures
        started = time.perf_counter()
        self.sac = sac_proposal(self.case)
        self.mpc = optimize_mpc(self.case, self.backend)
        self.setup_seconds = time.perf_counter() - started
        self.setup = _json({'method': 'Saved SAC actor plus fresh H=3 local sensitivity MPC',
            'seconds': self.setup_seconds, 'mpc_seconds': self.mpc['seconds'],
            'mpc_model_solves': self.mpc['model_solves'],
            'sac_inference_seconds': self.sac['seconds'],
            'mpc_plan_failures': plan_failures(self.mpc, self.case, self.backend),
            'mpc_horizon_plan': self.mpc,
            'training': 'Previously trained SAC; training time excluded and no retraining occurs.'})
        return _json([{**self.sac['candidate'], 'operation': 'INITIAL_SAC'},
            {'tool': 'CONSERVATIVE_SEED', 'control': [.25, 0.],
             'operation': 'INITIAL_CONSERVATIVE'}])

    def simulate(self, candidate):
        self._validate(candidate)
        point = self.plant.solve(candidate['control'], self.case.forecast_loads[0],
                                 self.case.rating_fraction)
        point['candidate_sha256'] = _digest(candidate)
        return _json(point)

    def _validate(self, candidate):
        from .continuous_control import _control
        if not isinstance(candidate, dict) or candidate.get('tool') not in (
                'SAC', 'CONSERVATIVE_SEED', 'CONTINUOUS_MPC', 'BOUNDED_LOCAL_SEARCH'):
            raise ValueError('Unauthorized voltage proposal tool')
        _control(candidate.get('control'))

    def verify(self, candidate, evidence):
        from .continuous_control import verify_control
        try:
            self._validate(candidate)
            failures = verify_control(evidence, self.case)
            if evidence.get('backend') != self.backend:
                failures.append('backend_mismatch')
            if (evidence.get('candidate_sha256') != _digest(candidate) or
                    evidence.get('control') != candidate['control']):
                failures.append('candidate_evidence_mismatch')
            return sorted(set(failures))
        except (ValueError, TypeError, KeyError, OverflowError, AttributeError):
            return ['invalid_candidate_or_evidence']

    def score(self, candidate, evidence):
        from .continuous_control import stage_cost
        if self.verify(candidate, evidence):
            raise ValueError('Only verified candidates may be ranked')
        score = stage_cost(candidate['control'], evidence['voltages_pu'], self.case.previous)
        if not _finite(score):
            raise ValueError('Non-finite objective')
        return score

    def _candidate(self, operation, history):
        if operation == 'USE_MPC_PLAN':
            if self.mpc is None or self.setup['mpc_plan_failures']:
                raise ValueError('A verified MPC plan is unavailable')
            return {**deepcopy(self.mpc['candidate']), 'operation': operation}
        best = _best(history)
        if best is None:
            raise ValueError('A feasible anchor is required for local refinement')
        a, b = best['candidate']['control']
        if operation == 'INCREASE_PV_0025':
            a = min(1., a + .0025)
        elif operation == 'RELAX_Q_10_PERCENT':
            b *= .9
        else:
            raise ValueError('Unauthorized refinement operation')
        return {'tool': 'BOUNDED_LOCAL_SEARCH', 'control': [float(a), float(b)],
                'operation': operation}

    def operations(self, history):
        descriptions = {
            'USE_MPC_PLAN': 'Test the first action from the freshly computed, feasible H=3 MPC plan.',
            'INCREASE_PV_0025': 'Increase a by 0.0025 from the best feasible action; keep b fixed; recheck.',
            'RELAX_Q_10_PERCENT': 'Reduce |b| by 10% from the best feasible action; keep a fixed; recheck.'}
        available = {}
        for operation, description in descriptions.items():
            try:
                candidate = self._candidate(operation, history)
                self._validate(candidate)
                if _unused(candidate, history):
                    available[operation] = description
            except (ValueError, KeyError, TypeError):
                pass
        return available

    def propose(self, operation, history):
        if operation not in self.operations(history):
            raise ValueError('Unavailable or duplicate refinement')
        return _json(self._candidate(operation, history))

    def fixed_choice(self, history, options):
        return next((key for key in ('USE_MPC_PLAN', 'INCREASE_PV_0025',
                                    'RELAX_Q_10_PERCENT') if key in options), None)

    def summary(self, candidate, evidence):
        from .continuous_control import compact
        return _json({**compact(evidence), 'control': candidate['control'],
                      'first_step_only': True, 'objective': self.objective})


class RestorationAdapter:
    """Feeder catalog refinement; the six-node MILP remains a separate lesson."""
    def __init__(self, backend):
        from .stage_workflow import StageCase, ElectricalModel
        from .lindistflow3 import load_network
        self.backend = backend
        self.case = StageCase('proposal_restoration', task='restoration',
            forecast=(3, 3, 3), fault=True, capacity=100., pv_available=False,
            long_available=False)
        self.model = ElectricalModel(backend)
        self.mv_nodes = set(load_network()['nodes'])
        self.scope = ('full supplied MV/LV feeder' if backend == 'opendss' else
                      'MV phases only; ideal LV aggregation')
        self.scope += '; synthetic bypass catalog, no physical switching sequence'
        self.objective = 'Minimize -(served nominal kW + 9*critical served nominal kW).'
        self.setup, self.setup_seconds = {}, 0.

    @staticmethod
    def _candidate(fraction, operation):
        return {'tool': 'RESTORATION_CATALOG', 'pv_cap': 0., 'tie': 'short',
                'shed_fraction': float(fraction), 'operation': operation}

    def awareness(self):
        from .stage_workflow import compact, model_failures
        baseline = {'pv_cap': 0., 'tie': 'none', 'shed_fraction': 0.}
        point = self.model.solve(self.case, baseline)
        return _json({'method': 'Fresh fault-isolated feeder snapshot and equipment permissions',
            'measurements': compact(point, self.case),
            'alarms': model_failures(point, self.case),
            'topology': {'faulted_segment_isolated': True, 'short_bypass_km': .25,
                         'short_bypass_limit_A': 100., 'long_bypass_permitted': False},
            'der': {'PV_permitted': False, 'storage': 'idle; no battery dispatch'},
            'forecast_load_multipliers': [1., 1., 1.], 'scope': self.scope,
            'priority': 'Every tenth sorted load is an artificial critical-priority object.',
            'fresh_model_solve': True,
            'operational_limit': 'Snapshots only; no relay/interlock, phase-level switching or crew sequence model.'})

    def plan(self):
        self.setup = {'method': 'Two bounded catalog seeds, with two additional fractions available',
                      'seconds': 0., 'numerical_setup_model_solves': 0}
        return [self._candidate(.5, 'INITIAL_HIGH_PICKUP'),
                self._candidate(.9, 'INITIAL_CONSERVATIVE')]

    def simulate(self, candidate):
        self._validate(candidate)
        point = self.model.solve(self.case, candidate)
        point.update(candidate_sha256=_digest(candidate), fresh_model_solve=True)
        return _json(point)

    def _validate(self, candidate):
        from .stage_workflow import scope_failures
        if (not isinstance(candidate, dict) or candidate.get('tool') != 'RESTORATION_CATALOG'
                or scope_failures(self.case, candidate)
                or candidate.get('tie') != 'short'
                or candidate.get('shed_fraction') not in (.5, .65, .75, .9)):
            raise ValueError('Candidate outside the authorized restoration catalog')

    def _topology_failures(self, evidence):
        from .lindistflow3 import SOURCE, FAULT
        endpoints = evidence.get('line_endpoints')
        if not isinstance(endpoints, list) or not endpoints:
            return ['missing_topology_evidence']
        parent, adjacency, names = {}, {}, []
        def find(node):
            parent.setdefault(node, node)
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        cycles = 0
        for row in endpoints:
            if not isinstance(row, (list, tuple)) or len(row) != 3:
                return ['invalid_topology_evidence']
            name, a, b = row
            if not all(isinstance(v, str) and v for v in row):
                return ['invalid_topology_evidence']
            names.append(name.lower())
            if a in self.mv_nodes and b in self.mv_nodes:
                pa, pb = find(a), find(b)
                if pa == pb:
                    cycles += 1
                else:
                    parent[pa] = pb
                adjacency.setdefault(a, set()).add(b)
                adjacency.setdefault(b, set()).add(a)
        failures = []
        if len(names) != len(set(names)):
            failures.append('duplicate_line_identity')
        if FAULT.lower() in names or 'tutorial_long' in names or names.count('tutorial_short') != 1:
            failures.append('unauthorized_switch_status')
        if cycles:
            failures.append('independent_MV_radiality')
        seen, queue = {SOURCE}, [SOURCE]
        for node in queue:
            for neighbor in adjacency.get(node, set()) - seen:
                seen.add(neighbor); queue.append(neighbor)
        if not adjacency or any(node not in seen for node in adjacency):
            failures.append('disconnected_MV_energized_branch')
        return failures

    def verify(self, candidate, evidence):
        from .stage_workflow import model_failures
        try:
            self._validate(candidate)
            failures = model_failures(evidence, self.case)
            if (evidence.get('candidate_sha256') != _digest(candidate) or
                    evidence.get('fresh_model_solve') is not True or
                    evidence.get('backend') != self.backend or
                    any(evidence.get(key) != candidate[key] for key in
                        ('pv_cap', 'tie', 'shed_fraction')) or
                    evidence.get('load_mult') != self.case.load):
                failures.append('candidate_evidence_mismatch')
            failures.extend(self._topology_failures(evidence))
            short = [line for line in evidence.get('lines', [])
                     if line.get('line', '').lower() == 'tutorial_short']
            if len(short) != 1 or short[0].get('normal_amps') != 100.:
                failures.append('short_tie_rating_mismatch')
            if (not _finite(evidence.get('critical_served_kw')) or
                    not _finite(evidence.get('critical_total_kw')) or
                    abs(evidence['critical_served_kw']-evidence['critical_total_kw']) > .1):
                failures.append('critical_service_priority')
            if not _finite(evidence.get('pv_kw')) or abs(evidence['pv_kw']) > 1e-5:
                failures.append('PV_off_policy')
            return sorted(set(failures))
        except (ValueError, KeyError, TypeError, OverflowError, AttributeError):
            return ['invalid_candidate_or_evidence']

    def score(self, candidate, evidence):
        if self.verify(candidate, evidence):
            raise ValueError('Only verified candidates may be ranked')
        score = float(-(evidence['served_kw'] + 9*evidence['critical_served_kw']))
        if not _finite(score):
            raise ValueError('Non-finite objective')
        return score

    def operations(self, history):
        options = {'SHED_065': 'Test 65% disconnection of the ordered noncritical load objects.',
                   'SHED_075': 'Test 75% disconnection of the ordered noncritical load objects.'}
        return {key: text for key, text in options.items()
                if _unused(self._candidate(.65 if key == 'SHED_065' else .75, key), history)}

    def propose(self, operation, history):
        if operation not in self.operations(history):
            raise ValueError('Unavailable or duplicate restoration refinement')
        return self._candidate(.65 if operation == 'SHED_065' else .75, operation)

    def fixed_choice(self, history, options):
        # Coarse-to-fine pickup search, using the same two unused catalog values.
        return next((key for key in ('SHED_075', 'SHED_065') if key in options), None)

    def summary(self, candidate, evidence):
        from .stage_workflow import compact
        return _json({**compact(evidence, self.case), 'tie': candidate['tie'],
            'shed_fraction_of_noncritical_objects': candidate['shed_fraction'],
            'tie_loading_pct': evidence.get('tie_loading_pct'),
            'switching_sequence_verified': False,
            'objective': self.objective})


class CyberAdapter:
    """Observable DC fixture, protected-measurement WLS and constrained control."""
    def __init__(self, case):
        self.case, self.backend = case, 'dc'
        self.scope = ('Four-bus DC teaching network; three protected additional angle '
                      'measurements assumed trustworthy; authentication not implemented')
        self.objective = 'Minimize 0.5*u^2 for one flexible injection u in [0,0.5] pu.'
        self.setup, self.setup_seconds = {}, 0.
        self.fixture, self.fit, self.trusted = None, None, None
        self.F, self.B, self.sensitivity = None, None, None
        self.limits = np.array([.35, .18, .35, .35])
        self.margin = .01

    def awareness(self):
        from .standard_formulations import run_wls_demo
        started = time.perf_counter()
        self.fixture = run_wls_demo()
        name = 'isolated_corruption' if self.case == 'cyber_isolated' else 'stealth_Hc'
        self.fit = next(row for row in self.fixture['cases'] if row['name'] == name)
        self.trusted = self.fixture['trusted_recovery']
        incidence = np.array([[-1., 0, 0], [1., -1., 0], [0, 1., -1.], [0, 0, -1.]])
        self.F = np.diag([10., 8., 10., 5.]) @ incidence
        self.B = incidence.T @ self.F
        self.sensitivity = self.F @ np.linalg.solve(self.B, [0., 1., 0.])
        covariance = np.asarray(self.fit['covariance']) + np.asarray(self.trusted['covariance'])
        disagreement = np.abs(np.asarray(self.fit['estimate'])-self.trusted['estimate'])
        sigma_units = disagreement / np.sqrt(np.diag(covariance))
        alarms = []
        if self.fit['chi_square']['alarm']:
            alarms.append('unprotected_WLS_residual_alarm')
        if np.max(sigma_units) > 5:
            alarms.append('unprotected_vs_protected_angle_disagreement_5sigma')
        return _json({'method': 'WLS + chi-square residual + protected-channel consistency check',
            'attack_fixture': name, 'measurements': self.fit['measurements'],
            'state_estimate_unprotected_rad': self.fit['estimate'],
            'residual_test': self.fit['chi_square'],
            'protected_state_estimate_rad': self.trusted['estimate'],
            'protected_disagreement_sigma_units': sigma_units.tolist(),
            'alarms': alarms, 'topology': {'buses': 4, 'state_dimension': 3, 'branches': 4},
            'der': {'flexible_injection_bus': 2, 'bounds_pu': [0., .5],
                    'balancing': 'slack bus'},
            'forecast': 'single DC snapshot; no stochastic forecast or temporal dynamics',
            'scope': self.scope, 'fresh_numerical_analysis': True,
            'awareness_numerical_seconds': time.perf_counter()-started,
            'protected_channel_note': 'I3 gives three additional angle channels, not a subset of the original eight measurements.',
            'detector_limit': 'Stealth Hc can evade the unprotected residual test; trusted-channel availability is assumed.'})

    def _ensure_awareness(self):
        if self.fixture is None:
            raise ValueError('Execute awareness before planning or simulation')

    def plan(self):
        from .standard_formulations import _redispatch
        self._ensure_awareness()
        started = time.perf_counter()
        self.qp = _redispatch(self.trusted['estimate'],
            self.fixture['measurement_model']['true_state'], self.F, self.B)
        self.setup_seconds = time.perf_counter()-started
        self.setup = _json({'method': 'Constrained scalar DC redispatch QP from protected WLS',
            'seconds': self.setup_seconds, 'QP': self.qp,
            'audit_note': 'true_state appears only in offline audit; it is not used in the QP objective/constraints.'})
        return [{'tool': 'UNPROTECTED_WLS_BASELINE', 'u': 0.,
                 'basis': 'unprotected', 'operation': 'INITIAL_UNPROTECTED'},
                {'tool': 'TRUSTED_CONSERVATIVE_SEED', 'u': .3,
                 'basis': 'protected', 'operation': 'INITIAL_CONSERVATIVE'}]

    def _validate(self, candidate):
        self._ensure_awareness()
        if (not isinstance(candidate, dict) or not _finite(candidate.get('u')) or
                not 0 <= candidate['u'] <= .5 or candidate.get('basis') not in ('protected', 'unprotected')
                or candidate.get('tool') not in ('UNPROTECTED_WLS_BASELINE',
                    'TRUSTED_CONSERVATIVE_SEED', 'TRUSTED_QP', 'TRUSTED_MARGIN_TRIAL')):
            raise ValueError('Unauthorized DC control candidate')
        expected = 'unprotected' if candidate['tool'] == 'UNPROTECTED_WLS_BASELINE' else 'protected'
        if candidate['basis'] != expected:
            raise ValueError('Candidate tool and measurement basis disagree')

    def simulate(self, candidate):
        self._validate(candidate)
        started = time.perf_counter()
        basis = self.trusted if candidate['basis'] == 'protected' else self.fit
        predicted = self.F @ np.asarray(basis['estimate']) + self.sensitivity * candidate['u']
        # An explicitly separate truth oracle is available only in this authored toy experiment.
        truth = np.asarray(self.fixture['measurement_model']['true_state'])
        actual = self.F @ truth + self.sensitivity * candidate['u']
        return _json({'candidate_sha256': _digest(candidate), 'backend': 'dc',
            'fresh_model_solve': True, 'scope': self.scope, 'u': candidate['u'],
            'measurement_basis': candidate['basis'],
            'measurement_sha256': _digest(basis['estimate']),
            'predicted_flows_pu': predicted.tolist(),
            'line_limits_pu': self.limits.tolist(), 'planning_margin_pu': self.margin,
            'offline_truth_audit': {'actual_toy_flows_pu': actual.tolist(),
                'actual_violation_count': int(np.sum(np.abs(actual) > self.limits+1e-8)),
                'not_used_by_verifier': True},
            'numerical_seconds': time.perf_counter()-started})

    def verify(self, candidate, evidence):
        try:
            self._validate(candidate)
            if not isinstance(evidence, dict):
                return ['missing_evidence']
            failures = []
            if (evidence.get('candidate_sha256') != _digest(candidate) or
                    evidence.get('backend') != 'dc' or evidence.get('fresh_model_solve') is not True or
                    evidence.get('u') != candidate['u'] or
                    evidence.get('measurement_basis') != candidate['basis']):
                failures.append('candidate_evidence_mismatch')
            basis = self.trusted if candidate['basis'] == 'protected' else self.fit
            if (evidence.get('measurement_sha256') != _digest(basis['estimate']) or
                    candidate['basis'] != 'protected'):
                failures.append('trusted_measurement_provenance_required')
            predicted = np.asarray(evidence['predicted_flows_pu'], float)
            recomputed = self.F @ np.asarray(basis['estimate']) + self.sensitivity*candidate['u']
            if (predicted.shape != (4,) or not np.isfinite(predicted).all() or
                    not np.allclose(predicted, recomputed, rtol=0., atol=1e-12)):
                failures.append('inconsistent_DC_flow_evidence')
            if (evidence.get('line_limits_pu') != self.limits.tolist() or
                    evidence.get('planning_margin_pu') != self.margin):
                failures.append('limits_mismatch')
            if np.any(np.abs(recomputed) > self.limits-self.margin+1e-8):
                failures.append('DC_flow_margin')
            if basis['rank'] != 3:
                failures.append('state_unobservable')
            return sorted(set(failures))
        except (ValueError, TypeError, KeyError, OverflowError, AttributeError):
            return ['invalid_candidate_or_evidence']

    def score(self, candidate, evidence):
        if self.verify(candidate, evidence):
            raise ValueError('Only verified candidates may be ranked')
        return .5*float(candidate['u']**2)

    def _candidate(self, operation):
        if not getattr(self, 'qp', None) or self.qp.get('status') != 'PROPOSE':
            raise ValueError('Verified QP proposal unavailable')
        u = self.qp['flexible_injection_pu']
        if operation == 'TRUSTED_QP':
            tool = 'TRUSTED_QP'
        elif operation == 'EXTRA_MARGIN_001':
            u, tool = min(.5, u+.01), 'TRUSTED_MARGIN_TRIAL'
        else:
            raise ValueError('Unauthorized DC refinement')
        return {'tool': tool, 'u': float(u), 'basis': 'protected', 'operation': operation}

    def operations(self, history):
        available = {}
        for operation, text in {
                'TRUSTED_QP': 'Test the minimum-control quadratic-program action from protected WLS.',
                'EXTRA_MARGIN_001': 'Test QP injection plus 0.01 pu; verify every DC branch again.'}.items():
            try:
                candidate = self._candidate(operation)
                if _unused(candidate, history):
                    available[operation] = text
            except ValueError:
                pass
        return available

    def propose(self, operation, history):
        if operation not in self.operations(history):
            raise ValueError('Unavailable or duplicate DC refinement')
        return self._candidate(operation)

    def fixed_choice(self, history, options):
        return next((key for key in ('TRUSTED_QP', 'EXTRA_MARGIN_001') if key in options), None)

    def summary(self, candidate, evidence):
        return _json({'u_pu': candidate['u'], 'measurement_basis': candidate['basis'],
            'predicted_flows_pu': evidence['predicted_flows_pu'],
            'line_limits_pu': self.limits.tolist(), 'planning_margin_pu': self.margin,
            'offline_truth_audit': evidence['offline_truth_audit'],
            'objective': self.objective, 'scope': self.scope})


def make_adapter(case, backend):
    """Factory: voltage/restoration use either feeder model; cyber uses DC."""
    if case in ('voltage', 'restoration') and backend in ('opendss', 'lindistflow3'):
        return VoltageAdapter(backend) if case == 'voltage' else RestorationAdapter(backend)
    if case in ('cyber_isolated', 'cyber_stealth') and backend == 'dc':
        return CyberAdapter(case)
    raise ValueError('Use voltage/restoration with opendss/lindistflow3, or cyber_isolated/cyber_stealth with dc')
