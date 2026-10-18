"""Support for the small real-LangGraph runtime lesson, without grid physics."""
from hashlib import sha256
import json
import math


def initial_state(command=.25, limit=.8, max_repairs=2):
    """TypedDict annotations do not validate values; validate this boundary."""
    for name, value, low, high in [('command', command, 0., 1.), ('limit', limit, 0., 2.)]:
        if type(value) not in (int, float) or not math.isfinite(value) or not low <= value <= high:
            raise ValueError(f'{name} must be a finite number in [{low}, {high}]')
    if type(max_repairs) is not int or not 0 <= max_repairs <= 5:
        raise ValueError('max_repairs must be an integer in [0,5]')
    return {'command': float(command), 'limit': float(limit), 'attempts': 0,
            'max_repairs': max_repairs, 'current': 0., 'passed': False,
            'status': 'TOY_NEW', 'acknowledged': False, 'trace': []}


def recommendation_id(state):
    """Bind this simulated readback to the current toy result; not authentication."""
    evidence = {key: state[key] for key in ('command', 'limit', 'current', 'attempts', 'passed')}
    return sha256(json.dumps(evidence, sort_keys=True, allow_nan=False).encode()).hexdigest()[:16]


def summary(state):
    return {key: state[key] for key in ('command', 'current', 'limit', 'attempts',
                                       'status', 'acknowledged', 'trace')}


def fixed_baseline(seed, simulate, verify, repair, route, ready, hold):
    """The identical rule/controller functions orchestrated by a Python loop."""
    state = dict(seed)
    state['trace'] = list(seed['trace'])
    def apply(function):
        update = function(state)
        entries = update.pop('trace', [])
        state.update(update)
        state['trace'] = state['trace'] + entries
    for _ in range(state['max_repairs'] + 1):
        apply(simulate)
        apply(verify)
        branch = route(state)
        if branch == 'repair':
            apply(repair)
        else:
            apply(ready if branch == 'report' else hold)
            return state
    raise RuntimeError('Rule/repair budget inconsistency in the direct-loop baseline')
