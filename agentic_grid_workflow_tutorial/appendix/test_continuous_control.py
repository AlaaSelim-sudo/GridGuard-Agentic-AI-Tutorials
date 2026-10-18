"""Bounded tests for continuous control; synthetic plants are test fixtures only.

python -m unittest discover -s appendix -p test_continuous_control.py
Heavy training libraries are optional; stored NumPy-policy tests need no Torch.
"""
import copy
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch
import numpy as np
from src import continuous_control as cc


def fixture_point(control=(.25,0.), load=1., rho=1., current=.5):
    return {'control':list(control),'voltages_pu':[.99,1.02], 'current_pu':[current],
            'voltage_ids':['test_a.1','test_b.1'],'line_ids':['test_line'],
            'rating_fraction':rho,'load_mult':load,'converged':True,
            'fresh_model_solve':True,'scope':'unit-test synthetic model','backend':'opendss',
            'max_device_p_mismatch_kw':0.,'max_device_q_mismatch_kvar':0.,
            'p_actual_kw':250.,'q_actual_kvar':0.,'p_requested_kw':250.,'q_requested_kvar':0.,
            'accepted':True,'violations':{},'vmin':.99,'vmax':1.02,
            'max_line_utilization_pct':100*current,'max_allowed_current_pct':100*current/rho}


class ContinuousMappingTests(unittest.TestCase):
    def test_continuous_map_is_capability_feasible(self):
        points=[cc.map_action([a,b]) for a in np.linspace(-1,1,31) for b in np.linspace(-1,1,29)]
        for a,b in points:
            self.assertGreaterEqual(a,0);self.assertLessEqual(a,1)
            self.assertLessEqual(abs(b),.44+1e-12)
            self.assertLessEqual(a*a+b*b,1+1e-12)
        # This is not the previous eight-action PV catalog.
        a,b=cc.map_action([.123456,-.234567])
        self.assertAlmostEqual(a,.561728)
        self.assertNotIn(round(a*100,6),(0,10,20,30,40,60,80,100))
        self.assertNotEqual(b,0)

    def test_invalid_or_nonfinite_action_rejected(self):
        for value in ([np.nan,0.],[0.,np.inf],[1.1,0.],[0.],[[0.,0.]]):
            with self.assertRaises((ValueError,TypeError)):
                cc.map_action(value)
        for value in ([True,0.],[1.,.1],[-.1,0.],[.5,.5]):
            with self.assertRaises(ValueError):
                cc._control(value)

    def test_forecast_observation_retains_prior_and_terminal_position(self):
        case=cc.ContinuousCase('test',(.8,1.,1.1),.8,(.4,-.1))
        np.testing.assert_allclose(cc.observation(case),[.8,1.,1.1,.4,-.1,.8,1.],rtol=1e-6)
        np.testing.assert_allclose(cc.observation(case,2,[.3,.1]),[1.1,1.1,1.1,.3,.1,.8,1/3],rtol=1e-6)


class FreshGateTests(unittest.TestCase):
    def test_valid_independent_evidence(self):
        self.assertEqual(cc.verify_control(fixture_point()),[])

    def test_missing_empty_nonfinite_and_duplicate_evidence_fail_closed(self):
        for key in ['control','voltages_pu','current_pu','rating_fraction','line_ids','p_actual_kw']:
            p=fixture_point();p.pop(key)
            self.assertTrue(cc.verify_control(p),key)
        for key,value in [('voltages_pu',[]),('current_pu',[]),('voltages_pu',[np.nan,1.]),
                          ('current_pu',[np.inf]),('voltage_ids',['same','same']),
                          ('max_device_p_mismatch_kw',np.nan),('rating_fraction',0.)]:
            p=fixture_point();p[key]=value
            self.assertTrue(cc.verify_control(p),(key,value))

    def test_array_evidence_overrides_claimed_pass_and_summary(self):
        p=fixture_point(current=.85,rho=.8)
        p['accepted']=True;p['violations']={};p['max_allowed_current_pct']=10.
        self.assertIn('thermal',cc.verify_control(p))
        p=fixture_point();p['voltages_pu'][1]=1.06
        self.assertIn('voltage',cc.verify_control(p))

    def test_bound_to_actual_case(self):
        case=cc.ContinuousCase('case',(1.,1.,1.),.8)
        self.assertIn('case_evidence_mismatch',cc.verify_control(fixture_point(),case))


class HorizonTests(unittest.TestCase):
    def test_future_without_verified_initialization_cannot_return_action(self):
        class TestOnlyPlant:
            def __init__(self,backend):self.solves=0;self.scope='unit test'
            def solve(self,u,load,rho):
                self.solves+=1
                return fixture_point(u,load,rho,current=2. if load>1.4 else .5)
        with patch.object(cc,'ContinuousPlant',TestOnlyPlant):
            result=cc.optimize_mpc(cc.ContinuousCase('future',(1.,1.45,1.)))
        self.assertEqual(result['status'],'REVIEW')
        self.assertIsNone(result['candidate'])
        self.assertIn('No verified feasible initialization',result['reason'])


class SavedPolicyTests(unittest.TestCase):
    @unittest.skipUnless((cc.MODEL_DIR/'training.json').exists(),'Run training preparation first')
    def test_actual_reward_training_and_export_provenance(self):
        record=json.loads((cc.MODEL_DIR/'training.json').read_text(encoding='utf-8'))
        self.assertGreater(record['updates'],0)
        self.assertGreater(record['actor_parameter_change_l2'],0)
        self.assertGreater(record['unique_continuous_replay_actions'],1000)
        self.assertEqual(record['terminal_transitions'],record['configuration']['steps']//3)
        self.assertLess(record['numpy_export_max_abs_error'],2e-6)
        policy=cc.load_policy()
        for case in cc.cases():
            proposal=cc.sac_proposal(case,policy)
            self.assertEqual(proposal['candidate']['tool'],'SAC')
            cc._control(proposal['candidate']['control'])

    @unittest.skipUnless((cc.RESULT_DIR/'continuous_control.json').exists(),'Run heldout evaluation first')
    def test_saved_matched_cases_keep_raw_and_fallback_distinct(self):
        result=json.loads((cc.RESULT_DIR/'continuous_control.json').read_text(encoding='utf-8'))
        self.assertEqual(len(result['runs']),6)
        for row in result['runs']:
            self.assertEqual(len(row['raw_sac_rollout']),3)
            self.assertEqual(len(row['mpc']['fresh_checks']),3)
            if row['fallback_used']:
                self.assertTrue(row['raw_sac_failures'])
                self.assertEqual(row['checked_candidate']['tool'],'CONTINUOUS_MPC')
            if row['checked_candidate']:
                self.assertFalse(row['checked_failures'])


class LinearAdapterTests(unittest.TestCase):
    def test_load_variation_does_not_scale_commanded_reactive_power(self):
        plant=cc.ContinuousPlant('lindistflow3')
        lower=plant.solve([.25,.1],.78)
        higher=plant.solve([.25,.1],1.08)
        self.assertAlmostEqual(lower['q_requested_kvar'],higher['q_requested_kvar'],places=6)
        self.assertAlmostEqual(lower['q_actual_kvar'],higher['q_actual_kvar'],places=6)
        self.assertAlmostEqual(lower['p_actual_kw'],higher['p_actual_kw'],places=6)
        self.assertNotAlmostEqual(lower['vmin'],higher['vmin'],places=4)


if __name__=='__main__':
    unittest.main(verbosity=2)
