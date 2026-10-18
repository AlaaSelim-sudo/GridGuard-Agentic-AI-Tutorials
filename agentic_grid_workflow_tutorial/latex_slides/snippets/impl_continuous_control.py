"""Continuous fleet P/Q control: SAC proposals, horizon optimization, fresh checks.

The saved SAC is reward-trained in a declared response-surface environment.
Neither optimizer actions nor labels enter its replay buffer. Its deterministic
actor can run with NumPy alone; training uses Stable-Baselines3/PyTorch lazily.
Fresh evaluation uses the unchanged OpenDSS or coupled MV LinDistFlow backend.
No result is a field safety or global AC-optimality certificate.
"""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from copy import deepcopy
import argparse
import hashlib
import json
import math
import time
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, minimize
from .standard_formulations import PQBackend, capability_polygon

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / 'models' / 'continuous_sac'
RESULT_DIR = ROOT / 'results'
GAMMA = .98
MOVEMENT_WEIGHT = .05
Q_LIMIT = .44
REFERENCE = {
    'algorithm': 'https://arxiv.org/abs/1801.01290',
    'algorithm_update': 'https://arxiv.org/abs/1812.05905',
    'implementation': 'https://stable-baselines3.readthedocs.io/en/master/modules/sac.html',
    'equations': 'https://spinningup.openai.com/en/latest/algorithms/sac.html',
}


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _json(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(type(value).__name__)


def _write(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=_json, allow_nan=False), encoding='utf-8')


@dataclass(frozen=True)
class ContinuousCase:
    id: str
    forecast_loads: tuple = (1., 1., 1.)
    rating_fraction: float = 1.
    previous: tuple = (.25, 0.)


def validate_case(case):
    if not isinstance(case, ContinuousCase) or not isinstance(case.id, str) or not case.id:
        raise ValueError('A named ContinuousCase is required')
    if not 1 <= len(case.forecast_loads) <= 3:
        raise ValueError('Forecast horizon must contain one to three loads')
    finite = lambda x: type(x) in (int, float) and math.isfinite(x)
    if any(not finite(x) or not .5 <= x <= 1.5 for x in case.forecast_loads):
        raise ValueError('Loads must be finite multipliers within the declared 0.5--1.5 evaluation domain')
    if not finite(case.rating_fraction) or not 0 < case.rating_fraction <= 1:
        raise ValueError('Current allowance must lie in (0,1]')
    _control(case.previous)


def cases():
    """Authored, fixed before training; unseen sequences, not an unseen feeder."""
    return [ContinuousCase('P1_nominal', (1., 1., 1.)),
            ContinuousCase('P2_load_change', (.78, 1.08, .93), previous=(.50, -.10)),
            ContinuousCase('P3_current_reserve', (1., .94, 1.06), rating_fraction=.8)]


def _control(control):
    if not isinstance(control, (tuple, list, np.ndarray)) or len(control) != 2:
        raise ValueError('Control must contain exactly [a,b]')
    if any(isinstance(x, (bool, np.bool_)) for x in control):
        raise ValueError('Boolean controls are invalid')
    x = np.asarray(control, float)
    if not np.isfinite(x).all() or not 0 <= x[0] <= 1 or abs(x[1]) > Q_LIMIT + 1e-12:
        raise ValueError('Control violates finite active/reactive participation bounds')
    if float(x @ x) > 1 + 1e-9:
        raise ValueError('Control violates the inverter capability circle')
    return x


def map_action(normalized_action):
    """Two continuous latent commands -> inverter-feasible fleet participation.

    SAC's entropy is defined in its normalized Box action coordinates. This
    nonlinear engineering map is part of the environment, not post-hoc rounding.
    It is the same actuator domain used by the continuous optimizer.
    """
    z = np.asarray(normalized_action, float)
    if z.shape != (2,) or not np.isfinite(z).all() or np.any(np.abs(z) > 1 + 1e-6):
        raise ValueError('SAC action must be a finite pair in [-1,1]')
    z = np.clip(z, -1., 1.)
    a = .5 * (z[0] + 1)
    b = z[1] * min(Q_LIMIT, math.sqrt(max(0., 1 - a*a)))
    return [float(a), float(b)]


def observation(case, step=0, previous=None):
    validate_case(case)
    if type(step) is not int or not 0 <= step < len(case.forecast_loads):
        raise ValueError('Invalid prediction step')
    previous = case.previous if previous is None else previous
    _control(previous)
    tail = list(case.forecast_loads[step:])
    tail += [tail[-1]] * (3-len(tail))
    return np.array(tail + list(previous) + [case.rating_fraction,
                    (len(case.forecast_loads)-step)/3], dtype=np.float32)


class ContinuousPlant:
    """New adapter; the original frozen P/Q module is never modified.

    For LinDistFlow, scale only the exported physical loads before invoking the
    original adapter at load_mult=1. This leaves commanded PV kvar, capacitors,
    shunts, and idle storage outside the demand multiplier, as in OpenDSS.
    """
    def __init__(self, backend='opendss'):
        if backend not in ('opendss', 'lindistflow3'):
            raise ValueError('Use opendss or lindistflow3')
        self.backend = backend
        self.scope = 'full supplied MV/LV feeder' if backend == 'opendss' else 'MV phases only; ideal LV aggregation'
        self.solves = 0
        self.seconds = 0.
        self._plants = {}

    def solve(self, control, load_mult=1., rating_fraction=1.):
        x = _control(control)
        if (isinstance(load_mult, bool) or not math.isfinite(float(load_mult)) or
                not .5 <= float(load_mult) <= 1.5):
            raise ValueError('Invalid demand multiplier')
        if (isinstance(rating_fraction, bool) or not math.isfinite(float(rating_fraction)) or
                not 0 < float(rating_fraction) <= 1):
            raise ValueError('Invalid current allowance')
        load = float(load_mult)
        if load not in self._plants:
            plant = PQBackend(self.backend, load if self.backend == 'opendss' else 1.)
            if self.backend == 'lindistflow3':
                plant.network = deepcopy(plant.network)
                for row in plant.network['loads']:
                    row['kw'] *= load
                    row['kvar'] *= load
            self._plants[load] = plant
        plant = self._plants[load]
        started = time.perf_counter()
        # Resolve sub-femtoscale differences between exported 0.44 and the
        # minimum per-device ratio without changing the engineering command.
        actual_x = x.copy()
        actual_x[1] = np.clip(actual_x[1], *plant.q_bounds)
        point = plant.solve(actual_x)
        self.solves += 1
        elapsed = time.perf_counter()-started
        self.seconds += elapsed
        point.update(backend=self.backend, scope=self.scope, load_mult=load,
                     rating_fraction=float(rating_fraction), fresh_model_solve=True,
                     model_solve_seconds=elapsed)
        current = np.asarray(point['current_pu']) / rating_fraction
        point['allowed_current_pu'] = current.tolist()
        point['max_allowed_current_pct'] = float(100*current.max())
        point['violations']['line_current'] = int(np.sum(current > 1+1e-7))
        point['accepted'] = bool(point['converged'] and not any(point['violations'].values()))
        point['verification_limits'] = {'voltage_pu': [.95, 1.05],
            'allowed_current_fraction': float(rating_fraction),
            'fleet_inverter_circle': 'a^2+b^2<=1', 'reactive_participation': [-Q_LIMIT, Q_LIMIT]}
        return point


def verify_control(point, case=None):
    """Fail-closed engineering gate; reconstruct findings from finite evidence."""
    if not isinstance(point, dict):
        return ['missing_evidence']
    failures = []
    try:
        control = _control(point['control'])
        v = np.asarray(point['voltages_pu'], float)
        amps = np.asarray(point['current_pu'], float)
        rho = float(point['rating_fraction'])
        if (v.ndim != 1 or amps.ndim != 1 or not len(v) or not len(amps) or
                not np.isfinite(v).all() or not np.isfinite(amps).all() or
                np.any(v <= 0) or np.any(amps < 0) or not 0 < rho <= 1):
            return ['invalid_or_empty_evidence']
        if len(point['voltage_ids']) != len(v) or len(point['line_ids']) != len(amps):
            return ['unidentified_evidence']
        if len(set(point['voltage_ids'])) != len(v) or len(set(point['line_ids'])) != len(amps):
            return ['duplicate_evidence_identity']
        if point.get('converged') is not True or point.get('fresh_model_solve') is not True:
            failures.append('fresh_converged_model_required')
        if not point.get('scope') or point.get('backend') not in ('opendss', 'lindistflow3'):
            failures.append('model_scope_required')
        if case is not None:
            validate_case(case)
            if abs(rho-case.rating_fraction)>1e-12 or abs(point['load_mult']-case.forecast_loads[0])>1e-12:
                failures.append('case_evidence_mismatch')
        if np.any(v < .95-1e-7) or np.any(v > 1.05+1e-7):
            failures.append('voltage')
        if np.any(amps/rho > 1+1e-7):
            failures.append('thermal')
        for key in ('max_device_p_mismatch_kw', 'max_device_q_mismatch_kvar'):
            if not math.isfinite(point[key]) or point[key] < 0 or point[key] > 1e-5:
                failures.append('dispatch_tracking'); break
        for key in ('p_actual_kw', 'q_actual_kvar', 'p_requested_kw', 'q_requested_kvar'):
            if not math.isfinite(point[key]):
                failures.append('invalid_dispatch'); break
    except (KeyError, TypeError, ValueError, OverflowError):
        return ['invalid_or_missing_evidence']
    return sorted(set(failures))


def stage_cost(control, voltages_pu, previous):
    x, previous = np.asarray(control), np.asarray(previous)
    return float((1-x[0])**2 + .05*x[1]**2 +
                 10*np.mean((np.asarray(voltages_pu)-1.01)**2) +
                 MOVEMENT_WEIGHT*np.sum((x-previous)**2))


def compact(point):
    keys = ('control', 'p_actual_kw', 'q_actual_kvar', 'vmin', 'vmax',
            'max_line_utilization_pct', 'max_allowed_current_pct', 'accepted',
            'violations', 'scope', 'backend', 'load_mult', 'rating_fraction')
    return {k: point[k] for k in keys if k in point}


def optimize_mpc(case, backend='opendss', max_iterations=7):
    """H<=3 continuous local sensitivity MPC, with fresh horizon feasibility.

    A fixed feasible initialization is tested, never assumed. All forecast
    steps must pass. Retaining a feasible prior iterate is explicit. This is a
    locally improved feasible horizon plan, not a certified local optimum,
    global AC-OPF optimum, or robust MPC guarantee.
    """
    validate_case(case)
    started = time.perf_counter()
    plant, h = ContinuousPlant(backend), len(case.forecast_loads)
    x = np.tile([.25, 0.], (h, 1))
    points = [plant.solve(u, load, case.rating_fraction) for u, load in zip(x, case.forecast_loads)]
    if any(verify_control(p) for p in points):
        return {'status': 'REVIEW', 'candidate': None, 'control_sequence': None,
                'objective': None, 'fresh_checks': [compact(p) for p in points],
                'reason': 'No verified feasible initialization; no infeasibility proof claimed',
                'model_solves': plant.solves, 'seconds': time.perf_counter()-started}
    polygon, polygon_rhs = capability_polygon()
    discounts = GAMMA**np.arange(h)
    def objective(z, predictions):
        z = np.reshape(z, (h, 2))
        return sum(discounts[k]*stage_cost(z[k], predictions[k], case.previous if k==0 else z[k-1]) for k in range(h))
    trace = []
    for iteration in range(max_iterations):
        v0, i0, jv, ji = [], [], [], []
        for k, (u, load, point) in enumerate(zip(x, case.forecast_loads, points)):
            v0.append(np.array(point['voltages_pu'])); i0.append(np.array(point['current_pu'])/case.rating_fraction)
            jvk, jik = np.zeros((len(v0[-1]), 2)), np.zeros((len(i0[-1]), 2))
            for axis in range(2):
                # Use a feasible backward difference close to circle/bounds.
                delta = .001 if axis == 0 and u[0] < .85 else -.001
                if axis == 1:
                    delta = -.001 if u[1] >= 0 else .001
                trial = u.copy(); trial[axis] += delta
                if trial[0] < 0: trial[0]=u[0]+.001; delta=.001
                p = plant.solve(trial, load, case.rating_fraction)
                if p['voltage_ids'] != point['voltage_ids'] or p['line_ids'] != point['line_ids']:
                    raise ValueError('Sensitivity identities changed')
                jvk[:,axis]=(np.array(p['voltages_pu'])-v0[-1])/delta
                jik[:,axis]=(np.array(p['current_pu'])/case.rating_fraction-i0[-1])/delta
            jv.append(jvk); ji.append(jik)
        matrices, lower, upper = [], [], []
        for k in range(h):
            block=np.vstack((jv[k],ji[k],polygon)); matrix=np.zeros((len(block),2*h)); matrix[:,2*k:2*k+2]=block
            matrices.append(matrix)
            lower.extend(np.r_[np.full(len(v0[k]),.9502)-v0[k]+jv[k]@x[k],
                               np.full(len(i0[k])+len(polygon),-np.inf)])
            upper.extend(np.r_[np.full(len(v0[k]),1.0498)-v0[k]+jv[k]@x[k],
                               np.full(len(i0[k]),.995)-i0[k]+ji[k]@x[k],polygon_rhs])
        matrix=np.vstack(matrices); lower=np.asarray(lower); upper=np.asarray(upper)
        def predicted(z):
            y=np.reshape(z,(h,2)); return [v0[k]+jv[k]@(y[k]-x[k]) for k in range(h)]
        def fun(z): return objective(z,predicted(z))
        bound_lo=np.maximum(np.tile([0.,-Q_LIMIT],h),x.ravel()-.25)
        bound_hi=np.minimum(np.tile([1.,Q_LIMIT],h),x.ravel()+.25)
        answer=minimize(fun,x.ravel(),method='SLSQP',bounds=Bounds(bound_lo,bound_hi),
                        constraints=[LinearConstraint(matrix,lower,upper)],
                        options={'ftol':1e-10,'maxiter':100})
        violation=max(float(np.maximum(lower-matrix@answer.x,0).max()),
                      float(np.maximum(matrix@answer.x-upper,0).max()))
        entry={'iteration':iteration+1,'qp_success':bool(answer.success),'qp_message':answer.message,
               'qp_constraint_violation':violation,'objective_before':objective(x,v0)}
        if not answer.success or violation>1e-6:
            entry['disposition']='retain_last_verified_horizon';trace.append(entry);break
        found=None
        for fraction in (1.,.5,.25,.125,.0625):
            y=x+fraction*(answer.x.reshape(h,2)-x)
            evaluated=[plant.solve(u,load,case.rating_fraction) for u,load in zip(y,case.forecast_loads)]
            cost=objective(y,[p['voltages_pu'] for p in evaluated])
            if all(not verify_control(p) for p in evaluated) and cost<=entry['objective_before']+1e-9:
                found=(y,evaluated,cost,fraction);break
        if found is None:
            entry['disposition']='retain_last_verified_horizon';trace.append(entry);break
        y,points,cost,fraction=found
        entry.update(disposition='accepted_fresh_horizon',objective_after=cost,step_fraction=fraction)
        trace.append(entry);delta=float(np.max(abs(y-x)));x=y
        if delta<2e-5:break
    points=[plant.solve(u,load,case.rating_fraction) for u,load in zip(x,case.forecast_loads)]
    ok=all(not verify_control(p) for p in points)
    return {'status':'PLAN' if ok else 'REVIEW','candidate':{'tool':'CONTINUOUS_MPC','control':x[0].tolist()} if ok else None,
            'control_sequence':x.tolist(),'objective':objective(x,[p['voltages_pu'] for p in points]),
            'fresh_checks':[compact(p) for p in points],'horizon_feasible':ok,'solver_trace':trace,
            'model_solves':plant.solves,'seconds':time.perf_counter()-started,'backend':backend,
            'scope':plant.scope,'method':'continuous local sensitivity QPs, fresh checks at every H step',
            'limits':'Local horizon solution; known forecasts, no uncertainty/terminal stability certificate.'}


def _features(load, a, b):
    """Cubic response surface, openly approximate and never a final verifier."""
    x=np.array([load,a,b],float)
    return np.array([1.,*x,*(x*x),x[0]*x[1],x[0]*x[2],x[1]*x[2],
                     *(x*x*x),x[0]**2*x[1],x[0]**2*x[2],x[1]**2*x[0],
                     x[1]**2*x[2],x[2]**2*x[0],x[2]**2*x[1],np.prod(x)])


def build_surrogate(seed=2301, samples=240, validation_samples=48):
    """Fit only physical responses; separate fit-validation is not RL evaluation."""
    MODEL_DIR.mkdir(parents=True,exist_ok=True)
    rng=np.random.default_rng(seed);plant=ContinuousPlant('opendss')
    inputs=[];outputs=[]
    for index in range(samples+validation_samples):
        load=float(rng.uniform(.7,1.2));control=map_action(rng.uniform(-1,1,2))
        p=plant.solve(control,load)
        inputs.append([load,*control]);outputs.append([p['vmin'],p['vmax'],p['max_line_utilization_pct']/100,
                                                      float(np.mean((np.array(p['voltages_pu'])-1.01)**2))])
        if (index+1)%60==0:
            print(f'Physical response-surface preparation: {index+1}/{samples+validation_samples} fresh AC solves',flush=True)
    inputs=np.array(inputs);outputs=np.array(outputs)
    design=np.array([_features(*row) for row in inputs])
    coef=np.linalg.lstsq(design[:samples],outputs[:samples],rcond=None)[0]
    error=design[samples:]@coef-outputs[samples:]
    np.savez(MODEL_DIR/'response_surface.npz',coefficients=coef,inputs=inputs,outputs=outputs)
    record={'kind':'degree-three least-squares physical response surface; not a power-flow solver',
            'backend':'opendss','scope':'full supplied feeder summary responses','seed':seed,
            'fit_samples':samples,'validation_samples':validation_samples,'actual_ac_solves':plant.solves,
            'training_input_range':{'load_mult':[.7,1.2],'a':[0,1],'b':[-Q_LIMIT,Q_LIMIT]},
            'outputs':['vmin_pu','vmax_pu','max_rated_current_fraction','mean_squared_voltage_deviation'],
            'validation_mae':np.mean(abs(error),axis=0).tolist(),
            'validation_max_abs_error':np.max(abs(error),axis=0).tolist(),
            'surface_sha256':_sha(MODEL_DIR/'response_surface.npz'),
            'source_hashes':{'continuous_control':_sha(__file__),
                             'standard_formulations':_sha(ROOT/'src/standard_formulations.py'),
                             'power_tools':_sha(ROOT/'src/power_tools.py'),
                             'network':_sha(ROOT/'data/lindistflow3_network.json')},
            'seconds':plant.seconds,'no_optimizer_labels':True}
    _write(MODEL_DIR/'response_surface.json',record)
    return record


class ResponseSurface:
    def __init__(self):
        self.coefficients=np.load(MODEL_DIR/'response_surface.npz')['coefficients']
    def predict(self, load, control):
        y=_features(load,*control)@self.coefficients
        y[2:]=np.maximum(y[2:],0)
        return y


def train_sac(seed=23, steps=12000):
    """Actual off-policy, entropy-regularized reward training; lazy heavy imports."""
    import gymnasium as gym
    from gymnasium import spaces
    import torch
    import stable_baselines3
    from stable_baselines3 import SAC
    torch.set_num_threads(1)
    class Environment(gym.Env):
        def __init__(self):
            self.action_space=spaces.Box(-1.,1.,(2,),dtype=np.float32)
            self.observation_space=spaces.Box(np.array([.5,.5,.5,0.,-Q_LIMIT,0.,0.],np.float32),
                                            np.array([1.5,1.5,1.5,1.,Q_LIMIT,1.,1.],np.float32))
            self.surface=ResponseSurface();self.episode_rewards=[];self.episode_violations=[]
        def reset(self,seed=None,options=None):
            super().reset(seed=seed)
            self.case=ContinuousCase('training',tuple(float(x) for x in self.np_random.uniform(.7,1.2,3)),
                                     1.,tuple(map_action(self.np_random.uniform(-.5,.5,2))))
            self.previous=np.array(self.case.previous);self.k=0;self.total=0.;self.violations=0
            return observation(self.case),{}
        def step(self,z):
            u=np.array(map_action(z));vmin,vmax,current,vmse=self.surface.predict(self.case.forecast_loads[self.k],u)
            base=(1-u[0])**2+.05*u[1]**2+10*vmse+MOVEMENT_WEIGHT*np.sum((u-self.previous)**2)
            vbad=max(.95-vmin,0.)+max(vmax-1.05,0.);ibad=max(current-1.,0.)
            violation=vbad>0 or ibad>0
            reward=-float(base+40*(vbad/.05)**2+10*ibad**2+2*violation)
            self.total+=reward;self.violations+=int(violation);self.previous=u;self.k+=1
            done=self.k==3
            obs=observation(self.case,min(self.k,2),u)
            if done:
                self.episode_rewards.append(self.total);self.episode_violations.append(self.violations)
            return obs,reward,done,False,{'surrogate_violation':bool(violation)}
    env=Environment()
    configuration={'algorithm':'Stable-Baselines3 SAC','seed':seed,'steps':steps,'gamma':GAMMA,
                   'learning_rate':.0003,'batch_size':128,'buffer_size':30000,'learning_starts':600,
                   'tau':.005,'ent_coef':.005,'net_arch':[64,64],
                   'training':'continuous physical-response surrogate; reward only, no MPC labels',
                   'train_load_range':[.7,1.2],'train_current_allowance':1.,'episode_length':3,
                   'reward':'-stage_cost -40*(voltage_excess/0.05)^2 -10*current_excess^2 -2*any_violation',
                   'base_cost':'(1-a)^2 +0.05*b^2 +10*mean((v-1.01)^2) +0.05*||u-u_previous||²',
                   'action_space':'continuous normalized Box[-1,1]^2 mapped into fleet inverter capability',
                   'heldout_cases':[asdict(c) for c in cases()],
                   'freeze_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':_sha(__file__),
                   'surface_sha256':_sha(MODEL_DIR/'response_surface.npz')}
    _write(MODEL_DIR/'training_protocol.json',configuration)
    model=SAC('MlpPolicy',env,seed=seed,gamma=GAMMA,learning_rate=.0003,batch_size=128,
              buffer_size=30000,learning_starts=600,tau=.005,ent_coef=.005,
              policy_kwargs={'net_arch':[64,64]},device='cpu',verbose=0)
    initial={k:v.detach().cpu().numpy().copy() for k,v in model.actor.state_dict().items()}
    print(f'Training actual SAC: {steps} reward-based interactions, seed {seed}',flush=True)
    started=time.perf_counter();model.learn(total_timesteps=steps,progress_bar=False)
    model.save(str(MODEL_DIR/'sac_training_checkpoint'))
    weights={k:v.detach().cpu().numpy() for k,v in model.actor.state_dict().items()}
    np.savez(MODEL_DIR/'actor_numpy.npz',**weights)
    probe=np.stack([observation(c) for c in cases()])
    reference=model.predict(probe,deterministic=True)[0]
    actor=NumPyPolicy(MODEL_DIR/'actor_numpy.npz')
    exported=np.stack([actor.predict(o) for o in probe])
    discrepancy=float(np.max(abs(reference-exported)))
    if discrepancy>2e-6:raise RuntimeError('NumPy actor export does not match trained actor')
    trace={'configuration':configuration,'seconds':time.perf_counter()-started,
           'versions':{'torch':torch.__version__,'stable_baselines3':stable_baselines3.__version__,'gymnasium':gym.__version__},
           'episode_rewards':env.episode_rewards,'episode_surrogate_violations':env.episode_violations,
           'updates':int(model._n_updates),'actor_parameter_change_l2':float(np.sqrt(sum(np.sum((weights[k]-initial[k])**2) for k in weights))),
           'replay_transitions':int(model.replay_buffer.pos),
           'terminal_transitions':int(model.replay_buffer.dones[:model.replay_buffer.pos].sum()),
           'unique_continuous_replay_actions':int(len(np.unique(model.replay_buffer.actions[:model.replay_buffer.pos].reshape(-1,2),axis=0))),
           'actor_sha256':_sha(MODEL_DIR/'actor_numpy.npz'),'checkpoint_sha256':_sha(MODEL_DIR/'sac_training_checkpoint.zip'),
           'numpy_export_max_abs_error':discrepancy,'references':REFERENCE,
           'evaluation_note':'Fixed seed/final checkpoint. No checkpoint selection using heldout performance.'}
    _write(MODEL_DIR/'training.json',trace)
    print(f'SAC training complete: {trace["updates"]} gradient updates in {trace["seconds"]:.1f} s',flush=True)
    return trace


class NumPyPolicy:
    def __init__(self,path):
        self.weights={k:v for k,v in np.load(path).items()}
    def predict(self,obs):
        x=np.asarray(obs,dtype=np.float32)
        if x.shape!=(7,) or not np.isfinite(x).all():raise ValueError('Expected seven finite observations')
        for name in ('latent_pi.0','latent_pi.2'):
            x=np.maximum(x@self.weights[name+'.weight'].T+self.weights[name+'.bias'],0)
        return np.tanh(x@self.weights['mu.weight'].T+self.weights['mu.bias'])


def load_policy():
    record=json.loads((MODEL_DIR/'training.json').read_text(encoding='utf-8'))
    if _sha(MODEL_DIR/'actor_numpy.npz')!=record['actor_sha256']:
        raise ValueError('Saved SAC actor hash mismatch')
    return NumPyPolicy(MODEL_DIR/'actor_numpy.npz')


def sac_proposal(case, policy=None):
    validate_case(case);policy=load_policy() if policy is None else policy
    started=time.perf_counter();obs=observation(case);z=policy.predict(obs);u=map_action(z)
    return {'status':'PROPOSE','candidate':{'tool':'SAC','control':u},'observation':obs.tolist(),
            'raw_normalized_action':z.tolist(),'seconds':time.perf_counter()-started,
            'training_scope':'One nominal-current OpenDSS response-surface SAC; same weights on both backends.',
            'verification':'Proposal only; no feasibility certificate until a fresh selected-model check.'}


def prepare_study(train=False, steps=12000):
    if train:
        build_surrogate();train_sac(steps=steps)
    policy=load_policy();rows=[]
    for backend in ('opendss','lindistflow3'):
        for case in cases():
            print('Fresh heldout evaluation:',backend,case.id,flush=True)
            proposal=sac_proposal(case,policy);plant=ContinuousPlant(backend)
            raw=plant.solve(proposal['candidate']['control'],case.forecast_loads[0],case.rating_fraction)
            failures=verify_control(raw,case)
            rollout=[compact(raw)];prior=np.array(raw['control'])
            rollout_cost=stage_cost(prior,raw['voltages_pu'],case.previous)
            for k in range(1,len(case.forecast_loads)):
                command=map_action(policy.predict(observation(case,k,prior)))
                evaluated=plant.solve(command,case.forecast_loads[k],case.rating_fraction)
                rollout.append(compact(evaluated))
                rollout_cost+=GAMMA**k*stage_cost(command,evaluated['voltages_pu'],prior)
                prior=np.array(command)
            plan=optimize_mpc(case,backend)
            chosen=proposal['candidate'] if not failures else plan['candidate']
            checked=None if chosen is None else plant.solve(chosen['control'],case.forecast_loads[0],case.rating_fraction)
            rows.append({'case':asdict(case),'backend':backend,'sac':proposal,'raw_sac':compact(raw),
                         'raw_sac_failures':failures,'mpc':plan,'checked_candidate':chosen,
                         'raw_sac_rollout':rollout,'raw_sac_horizon_cost':rollout_cost,
                         'raw_sac_horizon_feasible':all(r['accepted'] for r in rollout),
                         'checked_metrics':compact(checked) if checked else None,
                         'checked_failures':verify_control(checked,case),
                         'fallback_used':bool(failures and chosen is not None),
                         'raw_sac_stage_cost':stage_cost(raw['control'],raw['voltages_pu'],case.previous),
                         'extra_verifier_solves':plant.solves})
    study={'created_utc':datetime.now(timezone.utc).isoformat(),'method':'continuous SAC and continuous local horizon MPC',
           'cases':[asdict(c) for c in cases()],'training':json.loads((MODEL_DIR/'training.json').read_text()),
           'surrogate':json.loads((MODEL_DIR/'response_surface.json').read_text()),'runs':rows,
           'scope_notes':['SAC training surrogate is approximate; heldout actions receive fresh backend solves.',
                          'Same SAC checkpoint transfers from nominal AC-surrogate training to MV-only linear evaluation.',
                          'Heldout authored trajectories, same feeder and domain; 80% current allowance is a training shift.',
                          'Checked/fallback performance is distinct from raw SAC. No human or physical operation.',
                          'Continuous MPC is a local H=3 planning result, not global AC optimality or closed-loop guarantee.'],
           'source_sha256':_sha(__file__),'references':REFERENCE}
    _write(RESULT_DIR/'continuous_control.json',study);make_plots(study)
    return study


def make_plots(study):
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,2,figsize=(10,3.5))
    rewards=np.array(study['training']['episode_rewards']);window=min(100,len(rewards))
    axes[0].plot(np.arange(window,len(rewards)+1),np.convolve(rewards,np.ones(window)/window,'valid'))
    axes[0].set(xlabel='Training episode',ylabel='Mean return (100 episodes)',title='Actual SAC training on the response surface')
    failures=np.array(study['training']['episode_surrogate_violations'])
    axes[1].plot(np.arange(window,len(failures)+1),np.convolve(failures/3,np.ones(window)/window,'valid'))
    axes[1].set(xlabel='Training episode',ylabel='Surrogate violation fraction',title='Training evidence; not fresh AC validation')
    fig.tight_layout();fig.savefig(ROOT/'figures/continuous_training.png',dpi=180);plt.close(fig)
    fig,axes=plt.subplots(1,2,figsize=(11,4))
    for backend,ax in zip(('opendss','lindistflow3'),axes):
        rows=[r for r in study['runs'] if r['backend']==backend]
        for idx,r in enumerate(rows):
            u=r['sac']['candidate']['control'];v=r['mpc']['candidate']['control'] if r['mpc']['candidate'] else [np.nan,np.nan]
            ax.scatter(*u,marker='x',s=90,color='#b56624',label='Raw SAC' if idx==0 else None)
            ax.scatter(*v,marker='o',s=50,color='#007f83',label='Continuous MPC' if idx==0 else None)
            chosen=r['checked_candidate']
            if chosen:
                ax.scatter(*chosen['control'],marker='s',s=110,facecolors='none',edgecolors='#222222',
                           label='Checked/fallback action' if idx==0 else None)
            ax.annotate(r['case']['id']+(' reject' if r['raw_sac_failures'] else ' pass'),u,xytext=(4,4),textcoords='offset points',fontsize=8)
        ax.set(xlabel='Active participation a',ylabel='Reactive participation b',title=backend);ax.legend()
    fig.tight_layout();fig.savefig(ROOT/'figures/continuous_comparison.png',dpi=180);plt.close(fig)
    for backend in ('opendss','lindistflow3'):
        row=next(r for r in study['runs'] if r['backend']==backend and r['case']['id']=='P2_load_change')
        raw=row['raw_sac_rollout'];mpc=row['mpc']['fresh_checks'];steps=np.arange(1,len(raw)+1)
        fig,axes=plt.subplots(1,3,figsize=(12,3.4))
        for label,points,color in [('Raw SAC rollout',raw,'#b56624'),('Continuous MPC plan',mpc,'#007f83')]:
            axes[0].plot(steps,[p['control'][0] for p in points],'o-',label=label,color=color)
            axes[1].plot(steps,[p['control'][1] for p in points],'o-',color=color)
            axes[2].plot(steps,[p['max_allowed_current_pct'] for p in points],'o-',color=color)
        axes[2].axhline(100,color='#a7353d',ls='--')
        for ax,title,ylabel in zip(axes,['Active setting','Reactive setting','Fresh current check'],['a','b','Allowed-current use (%)']):
            ax.set(xlabel='Forecast step',title=title,ylabel=ylabel,xticks=steps)
        axes[0].legend(fontsize=8);fig.suptitle(backend+' | heldout P2; same controls, forecasts and limits')
        fig.tight_layout();fig.savefig(ROOT/f'figures/continuous_horizon_{backend}.png',dpi=180);plt.close(fig)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--train',action='store_true');parser.add_argument('--steps',type=int,default=12000)
    args=parser.parse_args();data=prepare_study(train=args.train,steps=args.steps)
    for row in data['runs']:
        print(row['backend'],row['case']['id'],'SAC',row['sac']['candidate']['control'],row['raw_sac_failures'],
              'MPC',row['mpc']['status'],row['mpc']['candidate'])
