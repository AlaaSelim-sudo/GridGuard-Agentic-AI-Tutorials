"""Analytic, topology, provenance and independence tests for the MV linear model.

Run ``python appendix/test_lindistflow3.py``. The optional final integration test
uses OpenDSS if installed; all other tests need only NumPy and the static JSON.
"""
import copy
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src import lindistflow3 as linear


def two_bus(phases=(1,), mutual=False):
    n = len(phases)
    r = np.eye(n)*.2
    x = np.eye(n)*.3
    if mutual:
        r += (np.ones((n, n))-np.eye(n))*.04
        x += (np.ones((n, n))-np.eye(n))*.08
    return {
        'network_sha256': 'analytic-unit-fixture', 'source': {'bus': 'root', 'phases': [1, 2, 3], 'pu': 1.},
        'nodes': {'root': {'base_kv': 1., 'phases': [1, 2, 3]},
                  'leaf': {'base_kv': 1., 'phases': list(phases)}},
        'frequency_hz': 60.,
        'branches': [{'line': 'analytic_line', 'from_bus': 'root', 'to_bus': 'leaf',
                      'phases': list(phases), 'r_ohm': r.tolist(), 'x_ohm': x.tolist(),
                      'c_nf': np.zeros((n, n)).tolist(), 'normal_amps': 100., 'overlay': False}],
        'loads': [{'name': 'demand', 'primary_bus': 'leaf', 'primary_phases': [1],
                   'phase_weights': [1.], 'kw': 10., 'kvar': 4., 'critical': True}],
        'pvs': [], 'storage': [], 'capacitors': [], 'transformer_interfaces': [],
    }


class LinDistFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.network = linear.load_network()

    def test_export_is_actual_multiphase_network_with_complete_device_mapping(self):
        net = self.network
        self.assertEqual(len(net['nodes']), 453)
        self.assertEqual(sum(not b['overlay'] for b in net['branches']), 452)
        self.assertEqual(len(net['transformer_interfaces']), 258)
        self.assertEqual(len(net['loads']), 2173)
        self.assertEqual(len(net['pvs']), 930)
        self.assertEqual(len(net['storage']), 436)
        self.assertFalse(net['export']['fitted_to_ac_results'])
        self.assertEqual(net['source']['bus'], linear.SOURCE)
        self.assertTrue(any(len(b['phases']) == 1 for b in net['branches']))
        self.assertTrue(any(len(b['phases']) == 3 and abs(b['r_ohm'][0][1]) > 0
                            for b in net['branches'] if not b['overlay']))
        for group in ('loads', 'pvs', 'storage', 'capacitors'):
            for device in net[group]:
                self.assertIn(device['primary_bus'], net['nodes'])
                self.assertAlmostEqual(sum(device['phase_weights']), 1.)

    def test_one_phase_analytic_squared_voltage_and_lossless_balance(self):
        result = linear.simulate(network=two_bus())
        self.assertEqual(result['status'], 'SOLVED')
        leaf = next(row for row in result['node_phase_voltages'] if row['bus'] == 'leaf')
        expected_w = 1000.**2-2*(.2*10000+.3*4000)
        self.assertAlmostEqual(leaf['voltage_squared_v2'], expected_w, places=7)
        self.assertAlmostEqual(leaf['v_pu'], math.sqrt(expected_w)/1000, places=12)
        self.assertAlmostEqual(result['lines'][0]['max_current_amps'], math.hypot(10, 4), places=10)
        self.assertEqual(result['source_p_kw_phase'], [10., 0., 0.])
        self.assertEqual(result['source_q_kvar_phase'], [4., 0., 0.])
        self.assertAlmostEqual(result['losses_kw'], .2*(10**2+4**2)/1000, places=12)
        # The diagnostic loss must not be silently added to the linear balance.
        self.assertAlmostEqual(sum(result['source_p_kw_phase']), result['served_kw'], places=12)

    def test_mutual_impedance_changes_unloaded_phase_voltages(self):
        net = two_bus((1, 2, 3), mutual=True)
        net['loads'][0]['kvar'] = 0.
        result = linear.simulate(network=net)
        phases = {row['phase']: row['voltage_squared_v2'] for row in result['node_phase_voltages']
                  if row['bus'] == 'leaf'}
        # Analytic cross-phase terms for a phase-A-only unity-PF load.
        expected_b = 1e6-2*10000*(-.04/2-.08*math.sqrt(3)/2)
        expected_c = 1e6-2*10000*(-.04/2+.08*math.sqrt(3)/2)
        self.assertAlmostEqual(phases[2], expected_b, places=7)
        self.assertAlmostEqual(phases[3], expected_c, places=7)
        self.assertGreater(phases[2], 1e6)
        self.assertLess(phases[3], 1e6)

    def test_unserved_phase_and_mesh_are_rejected(self):
        net = two_bus()
        net['loads'][0]['primary_phases'] = [2]
        self.assertEqual(linear.simulate(network=net)['status'], 'UNSUPPORTED')
        for options in ({'fault': True, 'tie': 'both'}, {'fault': False, 'tie': 'short'}):
            answer = linear.simulate(network=self.network, **options)
            self.assertEqual(answer['status'], 'UNSUPPORTED')
            self.assertIn('energized_MV_cycle', answer['unsupported_reasons'])
            self.assertTrue(linear.verify_linear(answer))

    def test_fault_isolation_restoration_and_shedding_use_real_mappings(self):
        outage = linear.simulate(network=self.network, fault=True, pv_cap=0.)
        self.assertEqual(outage['served_kw'], 0.)
        self.assertEqual(outage['pv_kw'], 0.)
        self.assertIn('load_service', linear.verify_linear(outage))
        full = linear.simulate(network=self.network, fault=True, tie='short', pv_cap=20.)
        self.assertAlmostEqual(full['served_kw'], full['nominal_kw'])
        self.assertAlmostEqual(full['critical_served_kw'], full['critical_total_kw'])
        self.assertEqual(linear.verify_linear(full), [])
        constrained = linear.simulate(network=self.network, fault=True, tie='short',
                                      capacity=100., pv_cap=0., shed_fraction=.75)
        self.assertAlmostEqual(constrained['served_kw'], 1843.61355, places=6)
        self.assertAlmostEqual(constrained['critical_served_kw'], constrained['critical_total_kw'])
        self.assertLess(constrained['served_kw'], constrained['nominal_kw'])
        self.assertEqual(linear.verify_linear(constrained, allow_unserved=True), [])
        self.assertEqual(linear.simulate(network=self.network, fault=True, tie='fault')['status'], 'UNSUPPORTED')

    def test_pv_var_priority_and_standby_consumption(self):
        pv = {'pmpp_kw': 10., 'irradiance': 1., 'kva': 10., 'pf': -.8,
              'kvar_max': 10., 'kvar_max_abs': 10., 'cutin_pct': .1}
        p, q = linear.pv_dispatch(pv, 100.)
        self.assertAlmostEqual(q, -7.5, places=10)
        self.assertAlmostEqual(p, math.sqrt(100-7.5**2), places=10)
        self.assertEqual(linear.pv_dispatch(pv, 0.), (0., -0.))
        result = linear.simulate(network=self.network, pv_cap=20.)
        self.assertAlmostEqual(result['pv_kw'], 1765., places=7)
        self.assertAlmostEqual(result['storage_standby_kw'], 34.88, places=7)

    def test_invalid_numeric_inputs_and_evidence_fail_closed(self):
        for kwargs in ({'pv_cap': float('nan')}, {'load_mult': True}, {'capacity': -1.},
                       {'shed_fraction': 1.1}, {'fault': 'false'}, {'tie': 'external_command'}):
            self.assertEqual(linear.simulate(network=self.network, **kwargs)['status'], 'UNSUPPORTED')
        valid = linear.simulate(network=self.network, pv_cap=30.)
        for field in ('vmin', 'vmax', 'max_line_pct', 'served_kw'):
            self.assertTrue(linear.verify_linear(dict(valid, **{field: float('nan')})))
        self.assertTrue(linear.verify_linear(dict(valid, model_scope='full feeder')))
        damaged = copy.deepcopy(valid)
        damaged['lines'][0]['loading_pct'] += 1.
        self.assertIn('inconsistent_line_evidence', linear.verify_linear(damaged))

    def test_static_export_integrity(self):
        damaged = copy.deepcopy(self.network)
        damaged['source']['pu'] = 1.04
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'changed.json'
            path.write_text(json.dumps(damaged), encoding='utf-8')
            with self.assertRaises(ValueError):
                linear.load_network(path)

    def test_fresh_python_process_solves_with_all_dss_imports_blocked(self):
        script = r'''
import importlib.abc, sys
class NoDSS(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.startswith(('opendssdirect', 'dss')) or fullname == 'src.power_tools':
            raise ImportError('DSS import forbidden by independence regression')
sys.meta_path.insert(0, NoDSS())
from src.lindistflow3 import simulate
m = simulate(pv_cap=30.)
assert m['status'] == 'SOLVED'
assert 'opendssdirect' not in sys.modules
assert 'src.power_tools' not in sys.modules
print('Independent MV solve passed')
'''
        run = subprocess.run([sys.executable, '-c', script], cwd=linear.ROOT,
                             text=True, capture_output=True, timeout=30)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn('Independent MV solve passed', run.stdout)

    @unittest.skipUnless(importlib.util.find_spec('opendssdirect'), 'Optional OpenDSS integration check')
    def test_selected_fresh_ac_snapshots_compare_only_common_mv_voltages(self):
        from src.power_tools import simulate as ac_simulate
        for cap in (0., 30., 100.):
            with self.subTest(cap=cap):
                approx = linear.simulate(network=self.network, pv_cap=cap)
                ac = ac_simulate(pv_cap=cap, details=True)
                self.assertAlmostEqual(approx['pv_kw'], ac['pv_kw'], places=6)
                self.assertAlmostEqual(approx['served_kw'], ac['served_kw'], places=6)
                ac_buses = {b['bus']: b for b in ac['buses']}
                maximum_error = max(abs(row[k]-ac_buses[row['bus']][k])
                                    for row in approx['buses'] for k in ('vmin', 'vmax'))
                self.assertLess(maximum_error, .01)
                self.assertFalse(approx['coverage']['LV_voltage_checks'])
                if cap == 100.:
                    self.assertEqual(linear.verify_linear(approx), [])
                    self.assertGreater(ac['overloaded_lines'], 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
