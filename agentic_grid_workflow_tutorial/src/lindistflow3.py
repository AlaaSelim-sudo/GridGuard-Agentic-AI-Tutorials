"""Independent three-phase LinDistFlow for this feeder's MV primary network.

The solver imports only NumPy and the standard library. ``export_network`` is a
separate, optional OpenDSS adapter that exports static equipment parameters; it
does not fit to AC voltages or cache AC solutions. The exported network includes
all load/PV/storage names, mapped through declared ideal service transformers.

For positive downstream consumption S (VA), phase reference beta=(1,a,a^2),
a=exp(-j*2*pi/3), and full phase impedance Z (ohm), each radial branch obeys

    S_ij = s_j + sum_k S_jk,
    w_j = w_i - 2*Re[conj(beta) * (Z @ (beta * conj(S_ij)))].

Here w=|V|^2 in V^2, and products outside @ are elementwise. These are the
diagonal squared-voltage form of Gan and Low (2014), Section V, equations (12).
Mutual impedance terms are retained. Branch currents are reconstructed at a
fixed balanced 1.03-pu reference; losses are diagnostic, not fed into balance.

Scope: MV phases and MV line currents ONLY. Service transformers are ideal and
lossless; secondary voltage drop, transformer losses/thermal constraints, and
protection are not modeled. A linear-screen pass is not a whole-feeder AC pass.
The optional OpenDSS audit remains a separate higher-fidelity comparison.

References:
https://arxiv.org/abs/1406.3054 (Gan and Low, 2014, Section V)
https://dss-extensions.org/dss-format/Line.html (phase impedance units)
https://dss-extensions.org/dss-format/PVSystem.html (PF and inverter priorities)
"""
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_NETWORK = ROOT/'data/lindistflow3_network.json'
SOURCE = 'udt8894-uhs20_1247x'
FAULT = 'l(r:udt8894-uhs20_1247)'
TAIL = 'udt8894-uhs20_1247x_b1_1'
MODEL_SCOPE = 'MV primary phases; ideal lossless aggregation of LV devices'
BETA = np.exp(-2j*np.pi*np.arange(3)/3)
REFERENCES = [
    {'title': 'Gan and Low (2014), multiphase LPF, Section V, equations (12)',
     'url': 'https://arxiv.org/abs/1406.3054'},
    {'title': 'DSS-Extensions Line property reference',
     'url': 'https://dss-extensions.org/dss-format/Line.html'},
    {'title': 'DSS-Extensions PVSystem property reference',
     'url': 'https://dss-extensions.org/dss-format/PVSystem.html'},
]
APPROXIMATIONS = [
    'Radial lossless active/reactive branch-power balance; fixed nearly balanced phase-angle ratios.',
    'Actual MV phase impedance matrices, including mutual coupling; no single-phase equivalent.',
    'All secondary devices aggregated to actual primary phase(s) through ideal lossless unity-tap wye transformers.',
    'No LV voltages, LV line currents, transformer thermal limits, transformer core/copper losses or protection.',
    'Constant-PQ loads and PV setpoints; no voltage-dependent low/high-voltage fallback or inverter dynamics.',
    'Fixed capacitor and line-pi-shunt powers evaluated at nominal voltage; controls remain off.',
    'Storage remains idle: nominal standby consumption is included; no energy-state dynamics.',
    'Branch current uses fixed source-reference phasors; I^H R I losses are diagnostic and not fed back.',
    'MV mesh/parallel energized paths, phase swaps, ambiguous transformer mappings and unsupported controls are rejected.',
]


class UnsupportedModel(ValueError):
    """The input requires a device or topology outside the declared linear model."""


def _hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def _base(bus):
    return bus.lower().split('.')[0]


def _finite(value):
    return type(value) in (int, float) and math.isfinite(value)


def export_network(path=DEFAULT_NETWORK, overwrite=False):
    """One-time static export; OpenDSS is needed ONLY for this adapter.

    An existing artifact is retained unless overwrite=True is explicit. The
    returned object has a content hash and source hashes. No AC operating-point
    voltages, solved powers, currents, or fitted sensitivities enter the export.
    """
    path = Path(path)
    if path.exists() and not overwrite:
        return load_network(path)
    # Deliberately local imports: normal solve/load paths do not require DSS.
    from . import power_tools
    dss = power_tools.dss
    power_tools.reset(load_mult=1., pv_cap=100.)
    all_buses = {}
    for name in dss.Circuit.AllBusNames():
        dss.Circuit.SetActiveBus(name)
        all_buses[name.lower()] = {
            'base_kv': float(dss.Bus.kVBase()),
            'phases': [int(p) for p in dss.Bus.Nodes() if p in (1, 2, 3)],
        }
    nodes = {name: data for name, data in all_buses.items() if data['base_kv'] > 1}
    if SOURCE not in nodes or nodes[SOURCE]['phases'] != [1, 2, 3]:
        raise UnsupportedModel('Expected a three-phase MV source bus.')
    branches, lv_edges, excluded = [], [], []
    for name in dss.Lines.AllNames():
        dss.Lines.Name(name)
        if name.startswith('tutorial_'):
            continue  # The same explicitly declared teaching ties are added below.
        buses = dss.CktElement.BusNames()
        a, b = map(_base, buses)
        if not dss.CktElement.Enabled():
            excluded.append({'line': name, 'reason': 'disabled in source model'})
            continue
        n = int(dss.CktElement.NumPhases())
        nc = int(dss.CktElement.NumConductors())
        order = list(map(int, dss.CktElement.NodeOrder()))
        if any(dss.CktElement.IsOpen(t, c) for t in (1, 2) for c in range(1, nc+1)):
            raise UnsupportedModel(f'Partially/open-ended line requires explicit export handling: {name}')
        if a in nodes and b in nodes:
            pa, pb = order[:n], order[nc:nc+n]
            if n not in (1, 2, 3) or nc != n or pa != pb or any(p not in (1, 2, 3) for p in pa):
                raise UnsupportedModel(f'Unsupported neutral or phase-swap line: {name}')
            length = float(dss.Lines.Length())
            def matrix(values):
                return (np.array(values, dtype=float).reshape(n, n)*length).tolist()
            branches.append({
                'line': name, 'from_bus': a, 'to_bus': b, 'phases': pa,
                'r_ohm': matrix(dss.Lines.RMatrix()), 'x_ohm': matrix(dss.Lines.XMatrix()),
                'c_nf': matrix(dss.Lines.CMatrix()), 'normal_amps': float(dss.CktElement.NormalAmps()),
                'length': length, 'length_unit_code': int(dss.Lines.Units()),
                'overlay': False,
            })
        elif a not in nodes and b not in nodes:
            lv_edges.append((a, b))
        else:
            raise UnsupportedModel(f'A line crosses nominal voltage levels: {name}')
    # Components below service transformers can contain parallel LV wiring; they
    # are not solved here. Multiple primaries feeding one component are rejected.
    parent = {name: name for name in all_buses if name not in nodes}
    def find(name):
        while parent[name] != name:
            parent[name] = parent[parent[name]]
            name = parent[name]
        return name
    for a, b in lv_edges:
        parent[find(a)] = find(b)
    interfaces, component_interfaces = [], defaultdict(list)
    for name in dss.Transformers.AllNames():
        dss.Transformers.Name(name)
        if not dss.CktElement.Enabled():
            continue
        buses = dss.CktElement.BusNames()
        primary = _base(buses[0])
        n = int(dss.CktElement.NumPhases())
        nc = int(dss.CktElement.NumConductors())
        phase_order = list(map(int, dss.CktElement.NodeOrder()))[:nc]
        phases = [p for p in phase_order if p in (1, 2, 3)]
        windings = []
        for w in range(1, dss.Transformers.NumWindings()+1):
            dss.Transformers.Wdg(w)
            windings.append({'bus': buses[w-1].lower(), 'delta': bool(dss.Transformers.IsDelta()),
                             'tap': float(dss.Transformers.Tap()), 'kv': float(dss.Transformers.kV()),
                             'kva': float(dss.Transformers.kVA())})
        if (primary not in nodes or any(_base(b) in nodes for b in buses[1:])
            or n not in (1, 3) or len(phases) != n
            or any(w['delta'] or abs(w['tap']-1.) > 1e-12 for w in windings)):
            raise UnsupportedModel(f'Transformer is outside ideal unity-tap wye service scope: {name}')
        interface = {'transformer': name, 'primary_bus': primary, 'primary_phases': phases,
                     'secondary_buses': sorted(set(map(_base, buses[1:]))),
                     'windings': windings, 'model': 'ideal lossless power aggregation'}
        interfaces.append(interface)
        for component in {find(b) for b in interface['secondary_buses']}:
            component_interfaces[component].append(interface)
    if any(len(items) != 1 for items in component_interfaces.values()):
        raise UnsupportedModel('At least one secondary component has ambiguous transformer primaries.')

    def mapping():
        buses = dss.CktElement.BusNames()
        bus = _base(buses[0])
        n = int(dss.CktElement.NumPhases())
        original_phases = [int(p) for p in dss.CktElement.NodeOrder()[:n]]
        if bus in nodes:
            mapped_bus, phases, transformer = bus, original_phases, None
            if n == 1 and len([p for p in dss.CktElement.NodeOrder() if p]) > 1:
                raise UnsupportedModel('Direct MV line-to-line single-phase injection is unsupported.')
        else:
            choices = component_interfaces.get(find(bus), [])
            if len(choices) != 1:
                raise UnsupportedModel(f'No unique service transformer for device at {bus}.')
            interface = choices[0]
            mapped_bus, transformer = interface['primary_bus'], interface['transformer']
            if len(interface['primary_phases']) == 1:
                phases = interface['primary_phases']
            else:
                if any(p not in interface['primary_phases'] for p in original_phases):
                    raise UnsupportedModel(f'Unknown phase transfer at transformer {transformer}.')
                phases = original_phases
                if n == 1 and len([p for p in dss.CktElement.NodeOrder() if p]) > 1:
                    raise UnsupportedModel('Single-phase line-to-line device on a three-phase service is unsupported.')
        if not phases or any(p not in nodes[mapped_bus]['phases'] for p in phases):
            raise UnsupportedModel(f'Device phases missing at primary bus {mapped_bus}.')
        return {'original_bus': bus, 'original_phases': original_phases,
                'primary_bus': mapped_bus, 'primary_phases': phases,
                'phase_weights': [1./len(phases)]*len(phases), 'transformer': transformer}

    loads, pvs, storage, capacitors = [], [], [], []
    critical = set(sorted(dss.Loads.AllNames())[::10])
    for name in dss.Loads.AllNames():
        dss.Loads.Name(name)
        if dss.Loads.Model() != 1 or dss.Loads.IsDelta():
            raise UnsupportedModel(f'Only constant-PQ wye load export is implemented: {name}')
        loads.append(dict(mapping(), name=name, kw=float(dss.Loads.kW()), kvar=float(dss.Loads.kvar()),
                          critical=name in critical))
    def prop(name):
        return dss.Properties.Value(name)
    for name in dss.PVsystems.AllNames():
        dss.PVsystems.Name(name)
        unsupported = (prop('EffCurve') or prop('P-TCurve') or int(prop('Model')) != 1
                       or prop('WattPriority').lower() != 'no' or prop('PFPriority').lower() != 'no'
                       or float(prop('%PMinNoVars')) != 0 or float(prop('%PMinkvarMax')) != 0)
        if unsupported:
            raise UnsupportedModel(f'PV requires a model not implemented by this exporter: {name}')
        pf = float(prop('pf'))
        if not 0 < abs(pf) <= 1:
            raise UnsupportedModel(f'Unsupported PV power factor: {name}')
        pvs.append(dict(mapping(), name=name, pmpp_kw=float(prop('Pmpp')), kva=float(prop('kVA')),
                        irradiance=float(prop('Irradiance')), pf=pf,
                        kvar_max=float(prop('kvarMax')), kvar_max_abs=float(prop('kvarMaxAbs')),
                        cutin_pct=float(prop('%CutIn')), cutout_pct=float(prop('%CutOut')),
                        model='constant PF, unity efficiency, var priority'))
    for name in dss.Storages.AllNames():
        dss.Storages.Name(name)
        if abs(float(prop('kvar'))) > 1e-12:
            raise UnsupportedModel(f'Nonzero idle storage var setpoint is unsupported: {name}')
        storage.append(dict(mapping(), name=name,
                            standby_kw=float(prop('kWrated'))*float(prop('%IdlingkW'))/100))
    for name in dss.Capacitors.AllNames():
        if name.lower() == 'none':
            continue
        dss.Capacitors.Name(name)
        if dss.Capacitors.IsDelta() or dss.Capacitors.NumSteps() != 1 or dss.Capacitors.States() != [1]:
            raise UnsupportedModel(f'Only fixed one-step wye capacitors are supported: {name}')
        capacitors.append(dict(mapping(), name=name, kvar=float(dss.Capacitors.kvar())))
    # Same synthetic bypasses as the original teaching model, not utility assets.
    for name, length in [('short', .25), ('long', 2.)]:
        r = np.full((3, 3), (.5-.2)/3); np.fill_diagonal(r, (.5+2*.2)/3)
        x = np.full((3, 3), (.6-.3)/3); np.fill_diagonal(x, (.6+2*.3)/3)
        branches.append({'line': f'tutorial_{name}', 'from_bus': SOURCE, 'to_bus': TAIL,
                         'phases': [1, 2, 3], 'r_ohm': (r*length).tolist(),
                         'x_ohm': (x*length).tolist(), 'c_nf': np.zeros((3, 3)).tolist(),
                         'normal_amps': 400., 'length': length, 'length_unit_code': 3,
                         'overlay': True})
    dss.Vsources.First()
    source = {'bus': SOURCE, 'phases': [1, 2, 3], 'pu': float(dss.Vsources.PU()),
              'base_kv': nodes[SOURCE]['base_kv'], 'phase_angles_deg': [0., -120., 120.]}
    payload = {
        'schema': 1, 'model_scope': MODEL_SCOPE, 'source': source, 'frequency_hz': float(dss.Solution.Frequency()),
        'nodes': nodes, 'branches': branches, 'transformer_interfaces': interfaces,
        'loads': loads, 'pvs': pvs, 'storage': storage, 'capacitors': capacitors,
        'approximations': APPROXIMATIONS, 'references': REFERENCES,
        'export': {'utc': datetime.now(timezone.utc).isoformat(), 'engine': dss.Basic.Version(),
                   'exporter_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                     for p in sorted(power_tools.DATA.glob('*.dss'))},
                   'fitted_to_ac_results': False, 'excluded_disabled_lines': excluded,
                   'excluded_LV_or_unenergized_line_count': len(lv_edges),
                   'unmapped_secondary_components_without_devices': sum(
                       component not in component_interfaces for component in {find(n) for n in parent})},
    }
    payload['network_sha256'] = _hash(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, allow_nan=False), encoding='utf-8')
    return payload


def load_network(path=DEFAULT_NETWORK):
    """Load and integrity-check the portable static export; no OpenDSS import."""
    payload = json.loads(Path(path).read_text(encoding='utf-8'))
    expected = payload.get('network_sha256')
    if not expected or expected != _hash({k: v for k, v in payload.items() if k != 'network_sha256'}):
        raise ValueError('LinDistFlow network integrity hash mismatch.')
    if payload.get('schema') != 1 or payload.get('model_scope') != MODEL_SCOPE:
        raise UnsupportedModel('Unsupported exported network schema or scope.')
    return payload


def pv_dispatch(pv, cap_percent):
    """Declared snapshot constant-PF/var-priority converter algebra, in kW/kvar."""
    available = pv['pmpp_kw']*pv['irradiance']
    if available < pv['kva']*pv['cutin_pct']/100:
        return 0., 0.
    p = min(available, pv['pmpp_kw']*cap_percent/100)
    q = p*math.sqrt(1/pv['pf']**2-1)*(1 if pv['pf'] > 0 else -1)
    q = max(-min(pv['kvar_max_abs'], pv['kva']), min(pv['kvar_max'], pv['kva'], q))
    if p*p+q*q > pv['kva']**2:
        p = math.sqrt(max(0., pv['kva']**2-q*q))
    return p, q


def _unsupported(reason, network=None, cycles=0):
    return {'status': 'UNSUPPORTED', 'converged': False, 'model_scope': MODEL_SCOPE,
            'unsupported_reasons': [reason], 'mv_cycles': cycles,
            'network_sha256': network.get('network_sha256') if network else None,
            'approximations': APPROXIMATIONS}


def simulate(load_mult=1., pv_cap=100., fault=False, tie='none', capacity=400.,
             shed_fraction=0., details=True, network_path=DEFAULT_NETWORK, network=None):
    """Solve the exported MV model independently; return common metrics + scope.

    Valid ties are none/short/long/both/fault. Energized cycles are rejected;
    tie='fault' with fault=True is rejected as a quarantined operation. If the
    entire feeder is disconnected, only the source is energized and served load
    is zero. Metric vmin/vmax/line maxima refer ONLY to modeled MV quantities.
    """
    started = time.perf_counter()
    if (not _finite(load_mult) or load_mult <= 0 or not _finite(pv_cap) or not 0 <= pv_cap <= 100
        or type(fault) is not bool or tie not in ('none', 'short', 'long', 'both', 'fault')
        or not _finite(capacity) or capacity <= 0
        or not _finite(shed_fraction) or not 0 <= shed_fraction <= 1):
        return _unsupported('invalid_input')
    net = load_network(network_path) if network is None else network
    if fault and tie == 'fault':
        return _unsupported('fault_quarantine', net)
    try:
        answer = _solve(net, load_mult, pv_cap, fault, tie, capacity, shed_fraction, details)
    except UnsupportedModel as exc:
        return _unsupported(str(exc), net, cycles=1 if str(exc) == 'energized_MV_cycle' else 0)
    answer['elapsed_s'] = time.perf_counter()-started
    return answer


def _solve(net, load_mult, cap, fault, tie, capacity, shed_fraction, details):
    source = net['source']['bus']
    nodes = net['nodes']
    active = []
    for branch in net['branches']:
        name = branch['line']
        if fault and name == FAULT:
            continue
        if branch['overlay'] and not (tie == 'both' or name == f'tutorial_{tie}'):
            continue
        active.append(branch)
    adjacency = defaultdict(list)
    for edge in active:
        adjacency[edge['from_bus']].append((edge['to_bus'], edge))
        adjacency[edge['to_bus']].append((edge['from_bus'], edge))
    parent, order, phases = {source: None}, [source], {source: set(net['source']['phases'])}
    parent_edge = {}
    for bus in order:
        for other, edge in adjacency[bus]:
            if parent_edge.get(bus) is edge:
                continue
            if other in parent:
                raise UnsupportedModel('energized_MV_cycle')
            parent[other], parent_edge[other] = bus, edge
            phases[other] = phases[bus] & set(edge['phases'])
            if not phases[other]:
                raise UnsupportedModel('energized_bus_without_supplied_phase')
            order.append(other)
    # Nominal fixed source-reference phasors reconstruct currents. The beta
    # ratios in the voltage drop are independent of the reference magnitude.
    reference = {b: nodes[b]['base_kv']*1000*net['source']['pu']*BETA for b in order}
    injections = {b: np.zeros(3, complex) for b in order}
    def add(device, power):
        bus = device['primary_bus']
        if bus not in parent:
            return False
        if not set(device['primary_phases']) <= phases[bus]:
            raise UnsupportedModel('partially_supplied_multiphase_device')
        for phase, weight in zip(device['primary_phases'], device['phase_weights']):
            injections[bus][phase-1] += power*1000*weight
        return True
    noncritical = sorted(d['name'] for d in net['loads'] if not d['critical'])
    shed = set(noncritical[:round(len(noncritical)*shed_fraction)])
    nominal = served = critical_total = critical_served = pv_kw = pv_kvar = idle_kw = 0.
    for device in net['loads']:
        kw, kvar = device['kw']*load_mult, device['kvar']*load_mult
        nominal += kw
        if device['critical']:
            critical_total += kw
        if device['name'] not in shed and add(device, complex(kw, kvar)):
            served += kw
            if device['critical']:
                critical_served += kw
    for device in net['pvs']:
        p, q = pv_dispatch(device, cap)
        if add(device, -complex(p, q)):
            pv_kw += p
            pv_kvar += q
    for device in net['storage']:
        if add(device, complex(device['standby_kw'], 0.)):
            idle_kw += device['standby_kw']
    for device in net['capacitors']:
        add(device, -1j*device['kvar'])
    # Fixed nominal-voltage pi-shunt powers: half at each energized endpoint.
    shunts = {}
    for child in order[1:]:
        edge = parent_edge[child]
        indices = np.array(edge['phases'])-1
        z = np.array(edge['r_ohm'])+1j*np.array(edge['x_ohm'])
        c = np.array(edge['c_nf'])*1e-9
        if z.shape != (len(indices), len(indices)) or not np.isfinite(z).all():
            raise UnsupportedModel('invalid_phase_impedance_matrix')
        if set(edge['phases']) != phases[child]:
            raise UnsupportedModel('branch_requires_unsupplied_phase')
        if abs(nodes[child]['base_kv']-nodes[parent[child]]['base_kv']) > 1e-8:
            raise UnsupportedModel('MV_line_crosses_voltage_bases')
        nominal_v = nodes[child]['base_kv']*1000*BETA[indices]
        power = nominal_v*np.conj(1j*2*np.pi*net['frequency_hz']*(c @ nominal_v))/2
        shunts[edge['line']] = power
        injections[child][indices] += power
        injections[parent[child]][indices] += power
    flows = {b: values.copy() for b, values in injections.items()}
    for bus in reversed(order[1:]):
        flows[parent[bus]] += flows[bus]
    source_voltage = nodes[source]['base_kv']*1000*net['source']['pu']
    squared = {source: np.full(3, source_voltage**2)}
    lines, losses_kw = [], 0.
    for child in order[1:]:
        edge = parent_edge[child]
        indices = np.array(edge['phases'])-1
        z = np.array(edge['r_ohm'])+1j*np.array(edge['x_ohm'])
        beta = BETA[indices]
        power = flows[child][indices]
        drop = 2*np.real(np.conj(beta)*(z @ (beta*np.conj(power))))
        squared[child] = np.full(3, np.nan)
        squared[child][indices] = squared[parent[child]][indices]-drop
        if np.any(squared[child][indices] <= 0) or not np.isfinite(squared[child][indices]).all():
            raise UnsupportedModel('nonpositive_or_nonfinite_squared_voltage')
        vref = reference[parent[child]][indices]
        series_current = np.conj(power/vref)
        shunt_current = np.conj(shunts[edge['line']]/vref)
        current_from = series_current+shunt_current
        current_to = -series_current+shunt_current
        maximum = float(max(np.abs(current_from).max(), np.abs(current_to).max()))
        rating = capacity if edge['line'] == 'tutorial_short' else edge['normal_amps']
        if not _finite(rating) or rating <= 0:
            raise UnsupportedModel('missing_or_invalid_MV_line_rating')
        loss = float(np.real(np.vdot(series_current, np.array(edge['r_ohm']) @ series_current))/1000)
        losses_kw += loss
        lines.append({'line': edge['line'], 'from_bus': parent[child], 'to_bus': child,
                      'phases': edge['phases'], 'normal_amps': rating, 'max_current_amps': maximum,
                      'loading_pct': 100*maximum/rating,
                      'p_kw_phase': (power.real/1000).tolist(), 'q_kvar_phase': (power.imag/1000).tolist(),
                      'current_amps_phase': np.abs(series_current).tolist(),
                      'current_from_amps_phase': np.abs(current_from).tolist(),
                      'current_to_amps_phase': np.abs(current_to).tolist(),
                      'diagnostic_loss_kw': loss})
    buses, node_phases = [], []
    for bus in order:
        indices = np.array(sorted(phases[bus]))-1
        voltage = np.sqrt(squared[bus][indices])/(nodes[bus]['base_kv']*1000)
        buses.append({'bus': bus, 'vmin': float(voltage.min()), 'vmax': float(voltage.max()),
                      'phases': (indices+1).tolist()})
        node_phases.extend({'bus': bus, 'phase': int(p+1), 'v_pu': float(v),
                            'voltage_pu': float(v),
                            'voltage_squared_v2': float(squared[bus][p])}
                           for p, v in zip(indices, voltage))
    vmax = max(b['vmax'] for b in buses)
    vmin = min(b['vmin'] for b in buses)
    topology = _hash({'energized_lines': sorted(row['line'] for row in lines),
                      'phase_sets': {b: sorted(phases[b]) for b in order}, 'capacity': capacity})
    result = {
        'status': 'SOLVED', 'converged': True, 'model_scope': MODEL_SCOPE,
        'network_sha256': net['network_sha256'], 'unsupported_reasons': [],
        'vmin': vmin, 'vmax': vmax,
        'voltage_violations': sum(b['vmin'] < .95-1e-6 or b['vmax'] > 1.05+1e-6 for b in buses),
        'voltage_severity': sum(max(0., .95-b['vmin'])+max(0., b['vmax']-1.05) for b in buses),
        'max_line_pct': max((row['loading_pct'] for row in lines), default=0.),
        'overloaded_lines': sum(row['loading_pct'] > 100+1e-4 for row in lines),
        'missing_line_ratings': 0, 'invalid_measurements': 0, 'mv_cycles': 0,
        'topology_hash': topology, 'energized_bus_count': len(buses), 'evaluated_line_count': len(lines),
        'nominal_kw': nominal, 'served_kw': served, 'unserved_kw': max(0., nominal-served),
        'critical_total_kw': critical_total, 'critical_served_kw': critical_served,
        'pv_kw': pv_kw, 'pv_kvar': pv_kvar, 'storage_standby_kw': idle_kw,
        'losses_kw': losses_kw, 'losses_scope': 'MV-only I^H R I diagnostic; omitted from power balance',
        'source_p_kw_phase': (flows[source].real/1000).tolist(),
        'source_q_kvar_phase': (flows[source].imag/1000).tolist(),
        'load_mult': load_mult, 'pv_cap': cap, 'tie': tie, 'shed_fraction': shed_fraction,
        'physical_load_disconnects': len(shed),
        'tie_loading_pct': next((r['loading_pct'] for r in lines if r['line'] == f'tutorial_{tie}'), None),
        'coverage': {'modeled_MV_bus_phases': len(node_phases), 'energized_MV_lines': len(lines),
                     'exported_service_transformers': len(net['transformer_interfaces']),
                     'mapped_loads': len(net['loads']), 'mapped_PV': len(net['pvs']),
                     'LV_voltage_checks': False, 'transformer_thermal_checks': False},
        'validity_diagnostics': {
            'maximum_MV_departure_from_source_pu': max(abs(vmin-net['source']['pu']), abs(vmax-net['source']['pu'])),
            'maximum_MV_within_bus_magnitude_spread_pu': max(b['vmax']-b['vmin'] for b in buses),
            'nominal_angle_ratios_assumed_not_estimated': True,
            'small_loss_assumption_not_a_certified_error_bound': True,
        },
        'approximations': APPROXIMATIONS,
    }
    if details:
        result.update(buses=buses, lines=lines, node_phase_voltages=node_phases,
                      line_endpoints=[(r['line'], r['from_bus'], r['to_bus']) for r in lines])
    return result


def verify_linear(metrics, allow_unserved=False, rating_fraction=1.):
    """MV-only provisional screen. Empty reasons NEVER certify secondary safety."""
    if not isinstance(metrics, dict) or metrics.get('status') != 'SOLVED' or metrics.get('converged') is not True:
        return ['linear_model_unsupported_or_failed']
    if metrics.get('model_scope') != MODEL_SCOPE:
        return ['unknown_model_scope']
    if not _finite(rating_fraction) or not 0 < rating_fraction <= 1:
        return ['invalid_rating_fraction']
    required = ['vmin', 'vmax', 'max_line_pct', 'served_kw', 'unserved_kw', 'nominal_kw',
                'critical_total_kw', 'critical_served_kw', 'pv_kw']
    if any(not _finite(metrics.get(key)) for key in required):
        return ['missing_or_invalid_linear_evidence']
    if metrics['vmin'] <= 0 or metrics['vmax'] < metrics['vmin'] or any(metrics[k] < 0 for k in required):
        return ['invalid_linear_evidence_domain']
    counts = ['voltage_violations', 'overloaded_lines', 'mv_cycles', 'missing_line_ratings',
              'invalid_measurements', 'energized_bus_count', 'evaluated_line_count']
    if any(not _finite(metrics.get(k)) or metrics[k] < 0 or int(metrics[k]) != metrics[k] for k in counts):
        return ['missing_or_invalid_linear_evidence']
    reasons = []
    if metrics['invalid_measurements'] or metrics['missing_line_ratings']:
        reasons.append('missing_or_invalid_linear_evidence')
    if metrics['energized_bus_count'] < 1:
        reasons.append('empty_voltage_evidence')
    if metrics['vmin'] < .95-1e-6 or metrics['vmax'] > 1.05+1e-6:
        reasons.append('MV_voltage')
    if metrics['max_line_pct']/rating_fraction > 100+1e-4:
        reasons.append('MV_thermal')
    if metrics.get('mv_cycles') != 0:
        reasons.append('MV_radiality')
    if not allow_unserved and metrics['unserved_kw'] > .1:
        reasons.append('load_service')
    if abs(metrics['served_kw']+metrics['unserved_kw']-metrics['nominal_kw']) > .1:
        reasons.append('inconsistent_service_evidence')
    if (metrics['critical_served_kw'] > metrics['critical_total_kw']+.1
        or metrics['critical_total_kw'] > metrics['nominal_kw']+.1
        or metrics['critical_served_kw'] > metrics['served_kw']+.1):
        reasons.append('inconsistent_service_evidence')
    if 'lines' in metrics:
        lines = metrics['lines']
        if not isinstance(lines, list) or len(lines) != metrics['evaluated_line_count']:
            reasons.append('inconsistent_line_evidence')
        else:
            values = []
            for line in lines:
                if (not isinstance(line, dict) or not _finite(line.get('normal_amps'))
                    or line['normal_amps'] <= 0 or not _finite(line.get('max_current_amps'))
                    or line['max_current_amps'] < 0 or not _finite(line.get('loading_pct'))):
                    reasons.append('invalid_line_evidence')
                    continue
                value = 100*line['max_current_amps']/line['normal_amps']
                values.append(value)
                if abs(value-line['loading_pct']) > 1e-8:
                    reasons.append('inconsistent_line_evidence')
            if any(v/rating_fraction > 100+1e-4 for v in values):
                reasons.append('MV_thermal')
            if len(values) == len(lines) and abs(max(values, default=0.)-metrics['max_line_pct']) > 1e-8:
                reasons.append('inconsistent_line_evidence')
    return list(dict.fromkeys(reasons))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--export', action='store_true', help='Create the static export; needs OpenDSS.')
    parser.add_argument('--overwrite', action='store_true', help='Explicitly replace an existing export.')
    parser.add_argument('--pv-cap', type=float, default=30.)
    args = parser.parse_args()
    if args.export:
        exported = export_network(overwrite=args.overwrite)
        print(json.dumps({'network_sha256': exported['network_sha256'], 'nodes': len(exported['nodes']),
                          'branches_including_two_teaching_ties': len(exported['branches'])}, indent=2))
    else:
        answer = simulate(pv_cap=args.pv_cap)
        print(json.dumps({k: v for k, v in answer.items() if k not in ('buses', 'lines', 'node_phase_voltages', 'line_endpoints')}, indent=2))
