"""Prospective confirmation of parser-first, Llama-on-handoff request intake.

This policy was selected after the original pilot. The separate confirmation
requests were authored and frozen before any calls for this follow-up study.
"""
import hashlib,json,time
from pathlib import Path
from datetime import datetime,timezone
import requests
from .control_tools import ROOT,ac_table
from .learning import load_policy
from .workflow import Llama
from .request_study import POLICY,SCHEMA,result,trusted_context,validate_interpretation,rule_parser,grade

class ConfirmationLlama:
    def __init__(self,model='llama3.1:8b'):
        probe=Llama(model);self.model,self.metadata,self.url=model,probe.metadata,probe.url;self.calls=[]
    def interpret(self,text,scene):
        # Exactly the original study's initial interpreter prompt and settings.
        payload={'model':self.model,'messages':[
            {'role':'system','content':POLICY+' Your role is Interpreter. Interpret the request.'},
            {'role':'user','content':json.dumps({'operator_request':text,'trusted_context':trusted_context(scene)})}],
            'format':SCHEMA,'stream':False,'keep_alive':'30m',
            'options':{'temperature':0,'seed':11,'num_predict':230,'num_ctx':8192}}
        start=time.perf_counter();entry={'payload':payload,'utc':datetime.now(timezone.utc).isoformat()}
        try:
            response=requests.post(self.url+'/api/chat',json=payload,timeout=120);response.raise_for_status()
            raw=response.json();entry['raw_response']=raw;parsed=json.loads(raw['message']['content'])
            if validate_interpretation(parsed):raise ValueError('Invalid schema/domain')
        except Exception as exc:
            entry['error']=f'{type(exc).__name__}: {exc}'
            parsed=result('CLARIFY','Model service or schema failure; inspect the retained call.')
        entry.update(response=parsed,seconds=time.perf_counter()-start);self.calls.append(entry)
        (ROOT/'results/confirmation_calls.json').write_text(json.dumps(self.calls,indent=2))
        return parsed,entry['seconds'],bool(entry.get('error'))

def run_confirmation(model='llama3.1:8b'):
    path=ROOT/'data/operator_requests_confirmation.json'
    fixtures=json.loads(path.read_text())
    sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    freeze={'fixture_sha256':sha(path),'hybrid_source_sha256':sha(__file__),
            'unchanged_interpreter_and_parser_sha256':sha(ROOT/'src/request_study.py'),
            'model':model,'policy':'Use parser READY outputs. Otherwise ask the original Llama interpreter once. Never change the engineering tools or verifier.',
            'selection':'Exploratory pilot motivated the hybrid policy; this distinct authored confirmation set is prospective, not a field sample.',
            'utc_before_first_confirmation_call':datetime.now(timezone.utc).isoformat()}
    frozen_path=ROOT/'results/confirmation_freeze.json'
    if frozen_path.exists():
        prior=json.loads(frozen_path.read_text())
        for key in ('fixture_sha256','hybrid_source_sha256','unchanged_interpreter_and_parser_sha256','model'):
            if prior[key]!=freeze[key]:raise RuntimeError('Confirmation inputs changed; create a separate study version.')
    else:frozen_path.write_text(json.dumps(freeze,indent=2))
    T=ac_table();net=load_policy();llama=ConfirmationLlama(model);rows=[]
    for f in fixtures:
        print('Confirmation',f['id'],flush=True)
        start=time.perf_counter();parsed=rule_parser(f['request'],f['scene']);parser_s=time.perf_counter()-start
        if parsed['status']=='READY':
            hybrid=parsed;llm_seconds=0.;error=False;calls=0
        else:
            hybrid,llm_seconds,error=llama.interpret(f['request'],f['scene']);calls=1
        for method,interpretation,seconds,ncalls in [
            ('rule_parser',parsed,parser_s,0),('hybrid',hybrid,parser_s+llm_seconds,calls)]:
            row={'id':f['id'],'group':f['group'],'scene':f['scene'],'request':f['request'],
                 'method':method,'intake_seconds':seconds,'llm_calls':ncalls,
                 'final_response_error':error if method=='hybrid' else False,**grade(f,interpretation,T,net)}
            row['correct_semantic_clarification']=row['correct_clarification'] and not row['final_response_error']
            row['machine_seconds']=seconds+row['runtime_seconds'];rows.append(row)
        saved={'metadata':{'freeze':json.loads(frozen_path.read_text()),'model':llama.metadata,
                           'actual_llm_calls':len(llama.calls),'complete':len(rows)==2*len(fixtures)},'rows':rows}
        (ROOT/'results/confirmation.json').write_text(json.dumps(saved,indent=2))
    return saved

if __name__=='__main__':run_confirmation()
