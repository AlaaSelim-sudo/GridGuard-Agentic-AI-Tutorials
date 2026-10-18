"""Portable regression: the complete fixed workflow needs no OpenDSS or Llama.

This is a numerical integration test, not an experimental supervisor result.
It uses the real exported network, all 40 table solves and saved DQN weights.
"""
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


class LinearStandaloneTests(unittest.TestCase):
    def test_voltage_and_restoration_workflows_without_dss_or_network(self):
        script = r'''
import importlib.abc
import json
import socket
import sys

blocked_attempts = []
class NoDSS(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if (fullname.split('.')[0] in ('opendssdirect', 'dss')
                or fullname == 'src.power_tools'):
            blocked_attempts.append(fullname)
            raise ImportError('DSS import forbidden by standalone workflow regression')
sys.meta_path.insert(0, NoDSS())

def no_network(*args, **kwargs):
    raise AssertionError('Network access forbidden by standalone workflow regression')
socket.create_connection = no_network
socket.socket.connect = no_network

from src.stage_workflow import ElectricalModel, cases, run_stages

model = ElectricalModel('lindistflow3')
table = model.table()
assert model.solves == 40, model.solves
assert len(table) == 5 and all(len(row) == 8 for row in table)
assert all(m['converged'] for row in table for m in row)
table_solves = model.solves
results = []
for case in (c for c in cases() if c.id in ('V2', 'R2')):
    row = run_stages(case, model, table, method='fixed')
    assert row['status'] == 'MODEL_RECOMMEND', (case.id, row['reasons'])
    assert row['model_scope'] == 'medium_voltage_only'
    assert row['llm_calls'] == 0
    assert row['model_solves'] > 0
    assert row['prediction']['coverage']['LV_voltage_checks'] is False
    stages = row['trace']
    assert {s['stage'] for s in stages} == {
        'Awareness', 'Planning', 'Execution', 'Simulation', 'Verification',
        'Recovery', 'Explanation', 'Operator acknowledgment'}
    assert any(s['stage'] == 'Verification' and s['status'] == 'PASS' for s in stages)
    assert stages[-1]['response']['state'] == 'PENDING'
    explanation = next(s for s in stages if s['stage'] == 'Explanation')
    assert explanation['response']['operator_card']['equipment_operated'] is False
    if case.id == 'V2':
        execution = [s for s in stages if s['stage'] == 'Execution']
        assert execution[0]['response']['candidate']['tool'] == 'DRL'
        assert len(execution[0]['response']['q_values']) == 8
        assert any(s['stage'] == 'Recovery' and s['status'] == 'REPAIR' for s in stages)
        assert row['gate_rejections'] >= 1
        assert row['candidate']['tool'] == 'MPC'
    else:
        assert row['candidate']['tie'] == 'short'
        assert 0 < row['candidate']['shed_fraction'] < 1
        assert row['candidate']['pv_cap'] == 0
        p = row['prediction']
        assert abs(p['critical_served_kw'] - p['critical_total_kw']) < 1e-6
        assert 0 < p['served_kw'] < p['nominal_kw']
    results.append({k: row[k] for k in ('case', 'status', 'candidate', 'model_solves', 'llm_calls')})

assert not blocked_attempts, blocked_attempts
assert not any(name.split('.')[0] in ('opendssdirect', 'dss')
               or name == 'src.power_tools' for name in sys.modules)
print(json.dumps({'table_solves': table_solves, 'runs': results, 'dss_import_attempts': blocked_attempts}))
'''
        run = subprocess.run([sys.executable, '-c', script], cwd=ROOT,
                             capture_output=True, text=True, timeout=90)
        self.assertEqual(run.returncode, 0, run.stderr or run.stdout)
        report = json.loads(run.stdout)
        self.assertEqual(report['table_solves'], 40)
        self.assertEqual([r['case'] for r in report['runs']], ['V2', 'R2'])
        self.assertEqual(report['dss_import_attempts'], [])
        self.assertTrue(all(r['llm_calls'] == 0 for r in report['runs']))


if __name__ == '__main__':
    unittest.main(verbosity=2)
