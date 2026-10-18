"""One live classroom request, saved separately from frozen study records."""
import json,time,uuid
import requests
from .control_tools import ROOT,ac_table
from .learning import load_policy
from .request_study import POLICY,SCHEMA,rule_parser,trusted_context,validate_interpretation,result,constrained_case
from .workflow import Llama,run_workflow

def demonstrate(text,scene='outage',model='llama3.1:8b'):
    identifier='demo_'+uuid.uuid4().hex[:10]
    parser=rule_parser(text,scene);interpretation=parser;intake_call=None
    if parser['status']!='READY':
        payload={'model':model,'messages':[
            {'role':'system','content':POLICY+' Your role is Interpreter. Interpret the request.'},
            {'role':'user','content':json.dumps({'operator_request':text,'trusted_context':trusted_context(scene)})}],
            'format':SCHEMA,'stream':False,'keep_alive':'30m',
            'options':{'temperature':0,'seed':11,'num_predict':230,'num_ctx':8192}}
        started=time.perf_counter();intake_call={'payload':payload}
        try:
            response=requests.post('http://localhost:11434/api/chat',json=payload,timeout=120)
            response.raise_for_status();raw=response.json();intake_call['raw_response']=raw
            interpretation=json.loads(raw['message']['content'])
            if validate_interpretation(interpretation):raise ValueError('Schema/domain error')
        except Exception as exc:
            intake_call['error']=str(exc);interpretation=result('CLARIFY','Model/schema error; request human review.')
        intake_call.update(response=interpretation,seconds=time.perf_counter()-started)
    workflow=None
    if interpretation['status']=='READY':
        llama=Llama(model,log_path=ROOT/f'results/{identifier}_planner.json')
        workflow=run_workflow(constrained_case(scene,identifier,interpretation),ac_table(),load_policy(),
                              method='agentic',llama=llama)
    record={'request':text,'scene':scene,'parser':parser,'interpretation':interpretation,
            'intake_call':intake_call,'workflow':workflow,
            'interpretation_notice':'Check the extracted restrictions against the operator request. The electrical gate does not establish semantic correctness; this classroom example is not independently gold-graded.'}
    (ROOT/f'results/{identifier}.json').write_text(json.dumps(record,indent=2))
    return record
