"""Workflow failure-path tests. All mocked language/physics outputs are TEST ONLY.

No Ollama calls, no training, and no replacement of recorded experiments.
"""
import copy
import json
from pathlib import Path
import tempfile
import unittest
import shutil
import subprocess
from unittest.mock import patch
from src import continuous_control as cc
from src import continuous_workflow as cw
from src import workshop_review as review


class TestOnlyPlant:
    evaluations = []
    def __init__(self, backend):
        self.backend=backend
    def solve(self, control, load_mult=1., rating_fraction=1.):
        cc._control(control)
        self.evaluations.append(list(control))
        amps=1.1 if control[0]>.3 else .5
        return {'control':list(control),'voltages_pu':[.99,1.02], 'current_pu':[amps],
                'voltage_ids':['fixture_a.1','fixture_b.1'],'line_ids':['fixture_line'],
                'rating_fraction':rating_fraction,'load_mult':load_mult,'converged':True,
                'fresh_model_solve':True,'scope':'UNIT TEST synthetic physics','backend':self.backend,
                'max_device_p_mismatch_kw':0.,'max_device_q_mismatch_kvar':0.,
                'p_actual_kw':1000*control[0],'q_actual_kvar':1000*control[1],
                'p_requested_kw':1000*control[0],'q_requested_kvar':1000*control[1],
                'accepted':amps<=rating_fraction,'violations':{'line_current':int(amps>rating_fraction)},
                'vmin':.99,'vmax':1.02,'max_line_utilization_pct':100*amps,
                'max_allowed_current_pct':100*amps/rating_fraction}


class TestOnlyLlama:
    def __init__(self, overrides=None):
        self.calls=[];self.overrides=overrides or {}
    def ask(self, role, context, choices):
        self.calls.append({'role':role,'context':copy.deepcopy(context)})
        choice=self.overrides.get(role,choices[0])
        if choice=='SERVICE_ERROR':
            return {'choice':'REVIEW','reason':'UNIT TEST simulated service failure',
                    'source':'local_failure_fallback','error':'test-only service outage'}
        return {'choice':choice,'reason':'UNIT TEST ONLY response',
                'source':'explicit_unit_test_double','error':None}


def proposal(control=None,tool='SAC'):
    return {'status':'PROPOSE','candidate':{'tool':tool,'control':control or [.4,0.]}}


def plan(backend='opendss'):
    evidence = {'control':[.25,0.], 'backend':backend, 'accepted':True,
                'violations':{'line_current':0}, 'load_mult':1., 'rating_fraction':.8,
                'vmin':.99, 'vmax':1.02, 'max_allowed_current_pct':62.5}
    return {'status':'PLAN','candidate':{'tool':'CONTINUOUS_MPC','control':[.25,0.]},
            'control_sequence':[[.25,0.]]*3,'objective':1.,'fresh_checks':[copy.deepcopy(evidence) for _ in range(3)],
            'horizon_feasible':True,'backend':backend}


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.case=cc.ContinuousCase('unit', (1.,1.,1.), .8)
        TestOnlyPlant.evaluations=[]
        self.patcher=patch.object(cc,'ContinuousPlant',TestOnlyPlant)
        self.patcher.start();self.addCleanup(self.patcher.stop)

    def run_workflow(self,method='fixed',p=None,m=None,llama=None):
        return cw.run_continuous_workflow(self.case,'opendss',method=method,llama=llama,
                                         proposal=p or proposal(),plan=m or plan())

    def test_rejected_policy_then_freshly_checked_mpc(self):
        result=self.run_workflow()
        self.assertEqual(result['status'],'MODEL_RECOMMEND')
        self.assertEqual(result['candidate']['tool'],'CONTINUOUS_MPC')
        self.assertEqual(TestOnlyPlant.evaluations,[[.4,0.],[.25,0.]])
        self.assertEqual(result['gate_rejections'],1)
        self.assertEqual(result['attempts'][0]['failures'],['thermal'])
        self.assertEqual(result['attempts'][1]['failures'],[])
        self.assertEqual(result['metrics']['max_allowed_current_pct'],62.5)
        self.assertFalse(result['equipment_operated'])
        self.assertFalse(result['trace'][-1]['response']['dispatch_authorized'])

    def test_critic_receives_failed_current_and_exact_replacement(self):
        llama=TestOnlyLlama()
        result=self.run_workflow('agentic',llama=llama)
        recovery=next(call for call in llama.calls if call['role']=='Recovery')
        self.assertEqual(recovery['context']['failed_checks'],['thermal'])
        self.assertEqual(recovery['context']['failed_candidate']['control'],[.4,0.])
        self.assertEqual(recovery['context']['replacement_plan']['candidate']['control'],[.25,0.])
        self.assertEqual(result['candidate']['control'],[.25,0.])

    def test_tool_contract_distinguishes_requesting_check_from_approval(self):
        llama=TestOnlyLlama()
        result=self.run_workflow('agentic',llama=llama)
        planner=next(call['context'] for call in llama.calls if call['role']=='Planner')
        self.assertEqual(planner['named_role'],'Planner')
        self.assertEqual(planner['tool_interface_version'],'1.1')
        self.assertEqual(planner['sac_proposal'],proposal())
        self.assertEqual(set(planner['allowed_actions']),{'VERIFY_SAC_FIRST','REVIEW'})
        self.assertIn('Launch a fresh numerical simulation',planner['allowed_actions']['VERIFY_SAC_FIRST'])
        self.assertIn('neither approves',planner['allowed_actions']['VERIFY_SAC_FIRST'])
        self.assertIn('Escalate for human review',planner['allowed_actions']['REVIEW'])
        recovery=next(call['context'] for call in llama.calls if call['role']=='Recovery')
        self.assertEqual(recovery['named_role'],'Recovery')
        self.assertEqual(set(recovery['allowed_actions']),{'USE_MPC_PLAN','REVIEW'})
        self.assertIn('does not apply an unchecked action',recovery['allowed_actions']['USE_MPC_PLAN'])
        self.assertEqual(result['contract']['tool_interface_version'],'1.1')

    def test_planner_review_produces_no_numerical_attempt(self):
        result=self.run_workflow('agentic',llama=TestOnlyLlama({'Planner':'REVIEW'}))
        self.assertEqual(result['status'],'REVIEW')
        self.assertIsNone(result['candidate'])
        self.assertEqual(TestOnlyPlant.evaluations,[])

    def test_recovery_review_cannot_be_overridden_by_explanation(self):
        result=self.run_workflow('agentic',llama=TestOnlyLlama({'Recovery':'REVIEW'}))
        self.assertEqual(result['status'],'REVIEW')
        self.assertIsNone(result['candidate'])
        self.assertEqual(len(result['attempts']),1)

    def test_explanation_error_card_and_final_status_agree(self):
        result=self.run_workflow('agentic',llama=TestOnlyLlama({'Explanation':'SERVICE_ERROR'}))
        self.assertEqual(result['status'],'REVIEW')
        card=next(t['response']['operator_card'] for t in result['trace'] if t['stage']=='Explanation')
        self.assertEqual(card['status'],result['status'])
        self.assertIsNone(result['candidate'])
        self.assertIsNone(result['metrics'])
        self.assertEqual(review.run_record_failures(result,'opendss','agentic'),[])

    def test_unknown_tool_is_rejected_before_model_evaluation(self):
        result=self.run_workflow(p=proposal([.25,0.],tool='UNAUTHORIZED_TOOL'))
        unknown=[a for a in result['attempts'] if a['candidate']['tool']=='UNAUTHORIZED_TOOL']
        self.assertTrue(not unknown or unknown[0]['failures'])
        # An unknown label must never become an accepted candidate identity.
        self.assertNotEqual((result['candidate'] or {}).get('tool'),'UNAUTHORIZED_TOOL')

    def test_review_plan_cannot_supply_a_fallback(self):
        p=plan();p['status']='REVIEW'
        result=self.run_workflow(m=p)
        self.assertEqual(result['status'],'REVIEW')
        self.assertIsNone(result['candidate'])
        self.assertEqual(len(result['attempts']),1)

    def test_infeasible_horizon_cannot_supply_a_fallback(self):
        p=plan();p['horizon_feasible']=False
        result=self.run_workflow(m=p)
        self.assertEqual(result['status'],'REVIEW')
        self.assertIsNone(result['candidate'])

    def test_other_model_plan_not_presented_as_same_model_horizon(self):
        result=self.run_workflow(m=plan('lindistflow3'))
        self.assertEqual(result['status'],'REVIEW')
        self.assertIsNone(result['candidate'])

    def test_boolean_command_is_not_a_numeric_action(self):
        result=self.run_workflow(p=proposal([True,0.]))
        self.assertTrue(result['attempts'][0]['failures'])
        self.assertNotIn([True,0.],TestOnlyPlant.evaluations)

    def test_horizon_check_must_match_forecast_and_candidate(self):
        for key,value in [('load_mult',1.3),('control',[.2,0.]),('vmax',1.2)]:
            with self.subTest(key=key):
                p=plan();p['fresh_checks'][2][key]=value
                result=self.run_workflow(m=p)
                self.assertEqual(result['status'],'REVIEW')
                self.assertEqual(len(result['attempts']),1)

    def test_stale_identity_or_operator_card_rejected(self):
        good=self.run_workflow()
        self.assertEqual(review.run_record_failures(good,'opendss','fixed'),[])
        stale=copy.deepcopy(good);stale['contract']['allowed_current_percent_of_nominal']=100
        self.assertIn('stale_recommendation_identity',review.run_record_failures(stale,'opendss','fixed'))
        stale=copy.deepcopy(good)
        next(t for t in stale['trace'] if t['stage']=='Explanation')['response']['operator_card']['status']='REVIEW'
        self.assertIn('stale_operator_card',review.run_record_failures(stale,'opendss','fixed'))

    def test_fresh_point_must_match_requested_model_and_command(self):
        original=TestOnlyPlant.solve
        for key,value in [('backend','lindistflow3'),('control',[.2,0.])]:
            def wrong(plant,*args,**kwargs):
                point=original(plant,*args,**kwargs);point[key]=value;return point
            with self.subTest(key=key),patch.object(TestOnlyPlant,'solve',wrong):
                result=self.run_workflow(p=proposal([.25,0.]))
                self.assertEqual(result['status'],'REVIEW')
                self.assertIsNone(result['candidate'])

    @unittest.skipUnless(shutil.which('node'),'Node.js is needed to exercise the shipped pure JavaScript gate')
    def test_actual_javascript_readback_gate_fails_closed(self):
        good=self.run_workflow()
        values={'p':'250.00','q':'0.00','limit':'80','scope':True,'limits':True,'operator':'TEST ONLY'}
        cases=[{'name':'matching','run':good,'values':values,'expected':True}]
        for name,edit in [
            ('review_status',lambda r:r.update(status='REVIEW')),
            ('claimed_pass_with_reject',lambda r:r['metrics'].update(accepted=False)),
            ('current_violation',lambda r:r['metrics'].update(max_allowed_current_pct=101.)),
            ('wrong_current_denominator',lambda r:r['metrics'].update(max_allowed_current_pct=50.)),
            ('voltage_violation',lambda r:r['metrics'].update(vmax=1.1)),
            ('wrong_candidate',lambda r:r['candidate'].update(control=[.2,0.])),
            ('missing_evidence',lambda r:r.update(metrics=None)),
            ('missing_attempts',lambda r:r.update(attempts=[])),
            ('stale_identity',lambda r:r.update(recommendation_id='stale')),
        ]:
            row=copy.deepcopy(good);edit(row)
            cases.append({'name':name,'run':row,'values':values,'expected':False})
        cases += [{'name':'absent','run':None,'values':values,'expected':False},
                  {'name':'missing_inputs','run':good,'values':{},'expected':False}]
        # Test each malformed record even when it is the initial UI snapshot;
        # separately verify that a later content mutation loses its binding.
        function=review.TEMPLATE.split('function readbackValid',1)[1].split('function values',1)[0]
        script=('const cases='+json.dumps(cases)+'; let reviewBindings; const fn = '+
                'function readbackValid'+function.strip().rstrip(';')+';\n'+
                "for(const c of cases){reviewBindings=new Map(c.run?[[c.run.recommendation_id,JSON.stringify(c.run)]]:[]); const answer=fn(c.run,c.values); if(answer!==c.expected)throw Error(c.name+' got '+answer);}\n"+
                'const r=cases[0].run;reviewBindings=new Map([[r.recommendation_id,JSON.stringify(r)]]);r.contract.allowed_current_percent_of_nominal=100;if(fn(r,cases[0].values))throw Error("stale binding");')
        result=subprocess.run([shutil.which('node')],input=script,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)


class ReviewRecordTests(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root=Path(self.directory.name);(self.root/'results').mkdir()
        self.patcher=patch.object(review,'ROOT',self.root)
        self.patcher.start();self.addCleanup(self.patcher.stop)

    def test_legacy_records_are_not_imported_into_continuous_review(self):
        (self.root/'results/workshop_run_opendss.json').write_text(json.dumps({'backend':'opendss','schema':'legacy'}))
        self.assertEqual(review.workshop_runs(),[])

    def test_nonfinite_records_cannot_be_saved(self):
        row={'schema':review.SCHEMA,'backend':'opendss','unknown':float('nan')}
        with self.assertRaises(ValueError):review.save_workshop_run(row)
        self.assertEqual(list((self.root/'results').iterdir()),[])

    def test_unknown_backend_rejected_before_any_file_write(self):
        row={'schema':review.SCHEMA,'backend':'unrecognized'}
        with self.assertRaises(ValueError):review.save_workshop_run(row)
        self.assertEqual(list((self.root/'results').iterdir()),[])


if __name__=='__main__':
    unittest.main(verbosity=2)
