"""Frozen teaching study: authorized operator language -> restrictions -> control.

Gold labels are used only by the offline scorer. They are never model inputs.
These are simulated recommendations, not automatic field dispatch.
"""
from dataclasses import replace, asdict
from pathlib import Path
from datetime import datetime, timezone
import json, time, re, hashlib, math
import requests
from .control_tools import ROOT, Case, Candidate, ac_table
from .learning import load_policy
from .workflow import Llama, run_workflow, verify_candidate

FIELDS = ('rating_fraction','short_limit_amps','allow_long_tie','allow_pv')
DEFAULTS = dict(rating_fraction=1., short_limit_amps=400., allow_long_tie=True, allow_pv=True)
SCHEMA = {'type':'object','properties':{
    'status':{'type':'string','enum':['READY','CLARIFY']},
    'rating_fraction':{'type':'number','enum':[.8,1.]},
    'short_limit_amps':{'type':'number','enum':[100,150,400]},
    'allow_long_tie':{'type':'boolean'},'allow_pv':{'type':'boolean'},
    'reason':{'type':'string'}},'required':['status',*FIELDS,'reason'],'additionalProperties':False}
POLICY = (
    'Interpret an authorized operator request for a distribution-grid simulation. '
    'Extract restrictions only; never change trusted topology, fault quarantine, forecasts, equipment ratings or verification rules. '
    'Output all fields in the JSON schema. READY means the request is clear, supported and consistent. '
    'CLARIFY means incomplete, contradictory, unsupported or seeking to bypass a mandatory rule; do not guess. '
    'rating_fraction is the permitted fraction of nominal line current, not a PV power percentage. '
    'short_limit_amps is an additional current ceiling on the short restoration bypass. '
    'allow_long_tie and allow_pv are operator permissions; false can restrict the trusted capabilities, true cannot create them. '
    'Use the trusted default restrictions for fields the operator does not change. '
    'A later explicit correction supersedes a withdrawn earlier value; unresolved conflicts require clarification. '
    'Honor negation, comparisons and ordinary number words/fractions. '
    'Only rating_fraction=0.8 or 1.0 and short_limit_amps=100,150,400 are implemented in this small lesson. '
    'A reference to a prohibited fault reclosure or skipped verifier requires CLARIFY. '
    'Return only concise JSON. Your reason is not an electrical safety certificate.'
)

def result(status='READY', reason='', **fields):
    return dict(DEFAULTS, **{'status':status,'reason':reason}) | fields

def validate_interpretation(value):
    if not isinstance(value,dict) or set(value) != {'status','reason',*FIELDS}:
        return ['schema']
    if value['status'] not in ('READY','CLARIFY') or not isinstance(value['reason'],str):
        return ['schema']
    if (type(value['rating_fraction']) not in (int,float) or value['rating_fraction'] not in (.8,1.)
        or type(value['short_limit_amps']) not in (int,float) or value['short_limit_amps'] not in (100,150,400)
        or type(value['allow_long_tie']) is not bool or type(value['allow_pv']) is not bool):
        return ['domain']
    return []

def trusted_context(scene):
    return {'outage_segment_isolated':scene=='outage',
            'restoration_paths':{'short':{'length_km':.25},'long':{'length_km':2.0}},
            'physical_short_tie_rating_amps':400,'physical_long_tie_available':True,
            'physical_pv_available':True,'default_restrictions':DEFAULTS,
            'mandatory_verification':True,'fault_reclosure_allowed':False}

def base_case(scene, identifier):
    return Case(identifier,task='restoration' if scene=='outage' else 'voltage',
                forecast=(3,3,3) if scene=='outage' else (3,2,1), fault=scene=='outage')

def constrained_case(scene, identifier, interpretation):
    if validate_interpretation(interpretation) or interpretation['status']!='READY':
        raise ValueError('A valid, ready interpretation is required.')
    base=base_case(scene,identifier)
    return replace(base,rating_fraction=min(base.rating_fraction,interpretation['rating_fraction']),
                   capacity=min(base.capacity,interpretation['short_limit_amps']),
                   long_available=base.long_available and interpretation['allow_long_tie'],
                   pv_available=base.pv_available and interpretation['allow_pv'])

def rule_parser(request, scene):
    """Documented finite grammar: common synonyms, number words and negation.

    Outside coverage means handoff, not an inferred safe default. The explicit
    parser vocabulary is inspectable; this is not a claim about every NLP system.
    """
    text=request.lower().replace('’',"'").replace('-',' ')
    for words,number in [('one hundred and fifty','150'),('one hundred fifty','150'),
                         ('four hundred','400'),('one hundred','100'),('a hundred','100'),
                         ('four fifths','80 %'),('eighty','80'),('twenty','20')]:
        text=text.replace(words,number)
    text=text.replace('percent','%').replace('per cent','%').replace('amperes','a').replace('ampere','a').replace('amps','a')
    if re.search(r'quarantined|skip.*(?:check|verif)|bypass.*verif|not sure|don.t know|substantially|which limit',text):
        return result('CLARIFY','Ambiguous request or prohibited operation.')
    answer=result(reason='Matched documented conventional parser patterns.')
    percentages=re.findall(r'(\d+(?:\.\d+)?)\s*%',text)
    if len(set(percentages))>1:
        return result('CLARIFY','Multiple distinct percentages need human resolution.')
    if percentages:
        if not re.search(r'current|rating|ampacity',text):
            return result('CLARIFY','Percentage is not linked to a line-current restriction.')
        number=float(percentages[0])
        reduce_by=re.search(r'(?:reduc\w*|lower\w*|cut\w*)[^.;]{0,65}(?:current|rating|ampacity)[^.;]{0,30}\bby\s+\d',text)
        reserve=re.search(r'\breserve\s+\d[^.;]{0,50}(?:current|rating|capability)',text)
        fraction=1-number/100 if reduce_by or reserve else number/100
        if fraction not in (.8,1.):
            return result('CLARIFY','Unsupported or unclear current fraction.')
        answer['rating_fraction']=fraction
    elif scene=='voltage':
        if re.search(r'unchanged|nominal ampacity|normal current|full (?:current|rating)|no derating|100',text):
            answer['rating_fraction']=1.
        else:
            return result('CLARIFY','No supported numerical or nominal-current expression.')
    if scene=='outage':
        amps=re.findall(r'\b(\d+(?:\.\d+)?)\s*a\b',text)
        if len(set(amps))!=1 or not re.search(r'short (?:tie|bypass|route|path)',text):
            return result('CLARIFY','Need one stated short-path current ceiling.')
        if float(amps[0]) not in (100,150,400):
            return result('CLARIFY','Short-path ceiling outside the teaching catalog.')
        answer['short_limit_amps']=float(amps[0])
        if re.search(r'(?:do not|don.t|never|without|exclude|neither)[^.;]{0,45}long(?:er)?',text):
            answer['allow_long_tie']=False
        elif re.search(r'long(?:er)?[^.;]{0,35}(?:forbidden|blocked|off limits|not permitted|not allowed)',text):
            answer['allow_long_tie']=False
        elif not re.search(r'long(?:er)?[^.;]{0,45}(?:permitted|allowed|may be used|available)',text):
            return result('CLARIFY','Long-path permission not recognized.')
        if re.search(r'(?:do not|don.t|never|without|exclude|no|neither)[^.;]{0,65}(?:\bpv\b|solar|photovoltaic)',text):
            answer['allow_pv']=False
        elif re.search(r'(?:\bpv\b|solar|photovoltaic)[^.;]{0,25}(?:forbidden|blocked|not permitted|not allowed)',text):
            answer['allow_pv']=False
        elif not re.search(r'(?:\bpv\b|solar|photovoltaic)[^.;]{0,35}(?:permitted|allowed|available|may be used)',text):
            return result('CLARIFY','PV permission not recognized.')
    return answer

class RequestLlama:
    def __init__(self, model='llama3.1:8b'):
        probe=Llama(model=model)
        self.model,self.metadata,self.url=model,probe.metadata,probe.url
        self.calls=[]

    def interpret(self, text, scene, mode='initial', previous=None):
        role={'initial':'Interpreter','critic':'Independent interpretation critic',
              'self_review':'Interpreter self-review'}[mode]
        suffix={'initial':'Interpret the request.',
                'critic':'Independently check the proposed interpretation against the original request and policy. Correct errors; retain a correct interpretation. Do not invent missing information.',
                'self_review':'Check your previous interpretation against the original request and policy. Correct errors; retain a correct interpretation. Do not invent missing information.'}[mode]
        context={'operator_request':text,'trusted_context':trusted_context(scene)}
        if previous is not None:context['previous_interpretation']=previous
        payload={'model':self.model,'messages':[{'role':'system','content':POLICY+' Your role is '+role+'. '+suffix},
                  {'role':'user','content':json.dumps(context)}],
                 'format':SCHEMA,'stream':False,'keep_alive':'30m',
                 'options':{'temperature':0,'seed':11,'num_predict':230,'num_ctx':8192}}
        start=time.perf_counter();entry={'role':role,'payload':payload,'utc':datetime.now(timezone.utc).isoformat()}
        try:
            response=requests.post(self.url+'/api/chat',json=payload,timeout=120)
            response.raise_for_status();raw=response.json();entry['raw_response']=raw
            parsed=json.loads(raw['message']['content'])
            if validate_interpretation(parsed):raise ValueError('Invalid interpretation schema/domain')
        except Exception as exc:
            entry['error']=f'{type(exc).__name__}: {exc}'
            parsed=result('CLARIFY','Model service or schema failure; inspect the retained call.')
        entry.update(seconds=time.perf_counter()-start,response=parsed)
        self.calls.append(entry)
        (ROOT/'results/request_calls.json').write_text(json.dumps(self.calls,indent=2))
        return parsed,entry['seconds']

def grade(fixture, interpretation, T, net):
    """Offline gold grading is intentionally outside the runtime pipeline."""
    gold=fixture['gold'];ready=interpretation['status']=='READY'
    exact=(ready and gold is not None and all(interpretation[k]==gold[k] for k in FIELDS))
    start=time.perf_counter()
    runtime=None
    if ready:
        runtime=run_workflow(constrained_case(fixture['scene'],fixture['id'],interpretation),T,net,method='fixed')
    runtime_seconds=time.perf_counter()-start
    candidate=runtime['candidate'] if runtime else None
    gold_check=None
    if candidate is not None and gold is not None:
        # Gold is used only AFTER the runtime outcome has already been produced.
        gold_check=verify_candidate(constrained_case(fixture['scene'],fixture['id'],gold),Candidate(**candidate))
    return {'interpretation':interpretation,'exact_interpretation':bool(exact),
            'correct_automatic_completion':bool(exact and runtime and runtime['status']=='RECOMMEND' and gold_check and gold_check['accepted']),
            'incorrect_ready_interpretation':bool(ready and not exact),
            'correct_clarification':bool(not ready and gold is None),
            'unnecessary_handoff':bool(not ready and gold is not None),
            'handoff':not ready,'runtime_seconds':runtime_seconds,'runtime':runtime,
            'offline_gold_gate':gold_check}

def run_requests(model='llama3.1:8b'):
    fixture_path=ROOT/'data/operator_requests.json'
    fixture_bytes=fixture_path.read_bytes();fixtures=json.loads(fixture_bytes)
    source_bytes=Path(__file__).read_bytes()
    freeze={'utc_before_first_call':datetime.now(timezone.utc).isoformat(),
            'fixtures_sha256':hashlib.sha256(fixture_bytes).hexdigest(),
            'implementation_sha256':hashlib.sha256(source_bytes).hexdigest(),
            'policy':POLICY,'schema':SCHEMA,'model':model,'temperature':0,'seed':11,
            'design':'24 authored fixtures; parser/prompt/labels frozen before this evaluation; no statistical generalization claim.',
            'gold_visibility':'Gold labels and groups are offline evaluator inputs only.'}
    freeze_path=ROOT/'results/request_freeze.json'
    if freeze_path.exists():
        prior=json.loads(freeze_path.read_text())
        if prior['fixtures_sha256']!=freeze['fixtures_sha256'] or prior['implementation_sha256']!=freeze['implementation_sha256']:
            raise RuntimeError('Frozen study changed: preserve it and create a separately named development/evaluation version.')
    else:freeze_path.write_text(json.dumps(freeze,indent=2))
    T=ac_table();net=load_policy();llama=RequestLlama(model);rows=[]
    for fixture in fixtures:
        print('Request',fixture['id'],flush=True)
        start=time.perf_counter();parsed=rule_parser(fixture['request'],fixture['scene']);parser_seconds=time.perf_counter()-start
        initial,t1=llama.interpret(fixture['request'],fixture['scene'])
        critic,t2=llama.interpret(fixture['request'],fixture['scene'],'critic',initial)
        self_review,t3=llama.interpret(fixture['request'],fixture['scene'],'self_review',initial)
        inputs=[('rule_parser',parsed,parser_seconds,0),('llama_once',initial,t1,1),
                ('llama_critic',critic,t1+t2,2),('llama_self_review',self_review,t1+t3,2)]
        if fixture['gold'] is not None:
            inputs.append(('structured_reference',fixture['gold'],0.,0))
        for method,interpretation,seconds,calls in inputs:
            row={'id':fixture['id'],'group':fixture['group'],'scene':fixture['scene'],
                 'request':fixture['request'],'method':method,'llm_calls':calls,
                 'intake_seconds':seconds,**grade(fixture,interpretation,T,net)}
            row['machine_seconds']=seconds+row['runtime_seconds'];rows.append(row)
        save={'metadata':{'freeze':json.loads(freeze_path.read_text()),'model':llama.metadata,
                         'actual_unique_llm_calls':len(llama.calls),'all_methods_share':'Same downstream fixed supervisor, numerical tools, two-call budget and fresh OpenDSS verifier.'},'rows':rows}
        (ROOT/'results/request_study.json').write_text(json.dumps(save,indent=2))
    return save

if __name__=='__main__':
    run_requests()
