"""Portable review screen for the continuous-control classroom records."""
from datetime import datetime, timezone
from pathlib import Path
import json
import math
from .continuous_workflow import ROOT, fingerprint, recommendation_payload, candidate_failures

SCHEMA = 'continuous_workshop_v1'


def run_record_failures(run, backend, method):
    """Consistency screening of an advisory record, not a power-flow replay."""
    failures = []
    try:
        if run['backend'] != backend or run['method'] != method:
            failures.append('record_model_or_method_mismatch')
        if run['recommendation_id'] != fingerprint(recommendation_payload(run)):
            failures.append('stale_recommendation_identity')
        contract = run['contract']
        if contract['backend'] != backend or fingerprint(contract['case']) != fingerprint(run['case_definition']):
            failures.append('request_binding_mismatch')
        allowance = contract['allowed_current_percent_of_nominal']
        if (type(allowance) not in (int, float) or not math.isfinite(allowance) or
                not 0 < allowance <= 100 or abs(allowance-100*run['case_definition']['rating_fraction']) > 1e-9 or
                contract['voltage_limits_pu'] != [.95, 1.05]):
            failures.append('invalid_record_limits')
        if run['status'] not in ('MODEL_RECOMMEND', 'REVIEW') or run['equipment_operated'] is not False:
            failures.append('invalid_record_disposition')
        cards = [t['response']['operator_card'] for t in run['trace'] if t['stage'] == 'Explanation']
        if len(cards) != 1 or any(cards[0][key] != run[key] for key in ('status', 'candidate', 'metrics', 'reasons', 'model_scope', 'equipment_operated')):
            failures.append('stale_operator_card')
        acknowledgments = [t['response'] for t in run['trace'] if t['stage'] == 'Operator acknowledgment']
        if (len(acknowledgments) != 1 or acknowledgments[0]['recommendation_id'] != run['recommendation_id'] or
                acknowledgments[0]['acknowledged'] is not False or acknowledgments[0]['dispatch_authorized'] is not False):
            failures.append('invalid_acknowledgment_binding')
        if run['status'] == 'REVIEW':
            if run['candidate'] is not None or run['metrics'] is not None:
                failures.append('review_contains_final_recommendation')
        else:
            candidate, point, last = run['candidate'], run['metrics'], run['attempts'][-1]
            if candidate_failures(candidate, 'SAC' if candidate['tool'] == 'SAC' else 'CONTINUOUS_MPC'):
                failures.append('invalid_record_candidate')
            if (last['candidate'] != candidate or last['point'] != point or last['failures'] != [] or
                    point['control'] != candidate['control'] or run['reasons'] != []):
                failures.append('final_attempt_mismatch')
            values = [point[key] for key in ('vmin', 'vmax', 'max_line_utilization_pct', 'max_allowed_current_pct', 'p_actual_kw', 'q_actual_kvar')]
            if (any(type(v) not in (int, float) or not math.isfinite(v) for v in values) or
                    point['accepted'] is not True or any(point['violations'].values()) or
                    point['converged'] is not True or point['fresh_model_solve'] is not True or point['backend'] != backend or
                    not .95-1e-7 <= point['vmin'] <= point['vmax'] <= 1.05+1e-7 or
                    not 0 <= point['max_allowed_current_pct'] <= 100+1e-5 or
                    abs(point['max_allowed_current_pct']-point['max_line_utilization_pct']*100/allowance) > 1e-6):
                failures.append('failed_or_inconsistent_metric_card')
    except (KeyError, TypeError, ValueError, IndexError, AttributeError, OverflowError):
        failures.append('malformed_record')
    return sorted(set(failures))


def validate_record(record):
    if (not isinstance(record, dict) or record.get('schema') != SCHEMA or
            record.get('backend') not in ('lindistflow3', 'opendss')):
        raise ValueError('Unknown workshop record schema or model')
    json.dumps(record, allow_nan=False)
    for method in ('fixed', 'agentic'):
        failures = run_record_failures(record.get(method, {}), record['backend'], method)
        if failures:
            raise ValueError('Invalid ' + method + ' advisory record: ' + ', '.join(failures))
    return record


def workshop_runs(current=None):
    records = {}
    for backend in ('lindistflow3', 'opendss'):
        path = ROOT / 'results' / ('workshop_run_' + backend + '.json')
        if path.exists():
            record = json.loads(path.read_text(encoding='utf-8'))
            if record.get('schema') == SCHEMA:
                validate_record(record)
                records[backend] = record
    if current is not None:
        validate_record(current)
        records[current['backend']] = current
    return [records[key] for key in ('lindistflow3', 'opendss') if key in records]


def comparison_rows(current=None):
    rows = []
    for record in workshop_runs(current):
        for method in ('fixed', 'agentic'):
            run = record[method]
            metrics = run.get('metrics') or {}
            rows.append({'backend': record['backend'], 'supervisor': method,
                'case': run['case'], 'status': run['status'],
                'tool': (run.get('candidate') or {}).get('tool'),
                'control_a_b': (run.get('candidate') or {}).get('control'),
                'P_kW': metrics.get('p_actual_kw'), 'Q_kvar': metrics.get('q_actual_kvar'),
                'max_current_pct_of_allowance': metrics.get('max_allowed_current_pct'),
                'rejected_attempts': run['gate_rejections'], 'llama_calls': run['llm_calls'],
                'model_scope': run['model_scope'], 'record_created_utc': record.get('created_utc'),
                'source': 'current in-memory run' if current is record else 'saved classroom run'})
    return rows


def save_workshop_run(record):
    validate_record(record)
    encoded = json.dumps(record, indent=2, allow_nan=False)
    backend = record['backend']
    path = ROOT / 'results' / ('workshop_run_' + backend + '.json')
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    journal = ROOT / 'results' / ('continuous_classroom_' + stamp + '_' + backend + '.json')
    journal.write_text(encoded, encoding='utf-8')
    path.write_text(encoded, encoding='utf-8')
    write_dashboard()
    return path


def write_dashboard():
    records = workshop_runs()
    data = [{'backend': record['backend'], 'created_utc': record.get('created_utc'),
             'run': record[method]} for record in records for method in ('fixed', 'agentic')]
    payload = json.dumps(data, allow_nan=False).replace('<', '\\u003c')
    text = TEMPLATE.replace('__RECORDS__', payload)
    path = ROOT / 'Workshop_Operator_Dashboard.html'
    path.write_text(text, encoding='utf-8')
    (ROOT / 'results/continuous_workflow_comparison.json').write_text(json.dumps({
        'schema': SCHEMA, 'rows': comparison_rows(), 'comparison_scope':
        'Same saved SAC policy and approved request; selected model coverage differs. These are classroom advisory records.'
    }, indent=2, allow_nan=False), encoding='utf-8')
    return path


TEMPLATE = r'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Continuous-control operator review</title>
<style>
:root{--green:#006b47;--ink:#203b33;--muted:#5b6c66;--border:#d6e1dc;--pale:#f3f7f5}*{box-sizing:border-box}body{margin:0;background:var(--pale);font:16px/1.5 system-ui,Arial;color:var(--ink)}header{background:var(--green);color:white;padding:30px 5vw}h1{font-size:30px;margin:6px 0}header p{max-width:900px;margin:4px 0}.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:11px}main{max-width:1300px;margin:auto;padding:26px}section,.card{background:white;border:1px solid var(--border);border-radius:8px;padding:23px;margin:0 0 20px}h2{font-size:19px;margin:0 0 12px}h3{font-size:16px;margin:0 0 8px}.toolbar{display:flex;align-items:center;gap:16px;flex-wrap:wrap}select,input,button{font:inherit;padding:10px;border:1px solid #aebfb6;border-radius:5px}select{min-width:340px;max-width:100%}.muted{color:var(--muted);font-size:13px}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.metric{border-left:3px solid var(--green);padding:9px 12px;background:var(--pale)}.metric strong{display:block;font-size:23px}.metric span{font-size:12px}.split{display:grid;grid-template-columns:1.4fr 1fr;gap:22px}.status{padding:14px;border-left:5px solid var(--green);background:#e8f3ed;margin:15px 0}.review{border-color:#b57525;background:#fff5e6}.detail{overflow-wrap:anywhere}.trace{display:grid;grid-template-columns:1fr 1fr;gap:12px}details{border:1px solid var(--border);border-radius:5px;padding:11px}summary{cursor:pointer;font-weight:600;font-size:14px}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f6f8f7;padding:10px;max-height:310px;overflow:auto;font:12px/1.55 Consolas,monospace}.small{font-size:13px}label{display:block;margin:14px 0 5px}.readback{display:grid;grid-template-columns:1fr 1fr;gap:12px}.readback input{width:100%}.check{display:flex;align-items:start;gap:9px;font-size:14px}.check input{margin-top:5px}button{cursor:pointer;background:var(--green);color:white;border:0;margin:14px 9px 0 0}button.secondary{background:#e9eeeb;color:var(--ink)}button:disabled{opacity:.4;cursor:not-allowed}#feedback{min-height:30px;font-size:14px;font-weight:600}a{color:var(--green)}footer{padding:0 26px 30px;max-width:1300px;margin:auto}.scope{font-size:14px;margin-top:15px}table{width:100%;border-collapse:collapse;font-size:13px}th,td{text-align:left;padding:9px;border-bottom:1px solid var(--border)}@media(max-width:850px){.split,.trace{grid-template-columns:1fr}.metrics{grid-template-columns:1fr 1fr}.toolbar{display:block}select{min-width:0;width:100%}}
</style></head><body><header><div class="eyebrow">Greensboro synthetic feeder · classroom advisory console</div>
<h1>Review a continuous P/Q recommendation</h1><p>Follow the request, the numerical proposal, each check, and the operator decision. This screen creates a local review record and issues no equipment commands.</p></header>
<main><section class="toolbar"><label for="run" style="margin:0">Stored classroom result</label><select id="run"></select><span id="stamp" class="muted"></span></section>
<div class="split"><div><section><h2>Request and proposed action</h2><p id="request"></p><div id="status" class="status"></div><div class="metrics"><div class="metric"><span>Active output</span><strong id="p"></strong><span>kW</span></div><div class="metric"><span>Reactive output</span><strong id="q"></strong><span>kvar</span></div><div class="metric"><span>Current use</span><strong id="current"></strong><span>% of allowed rating</span></div><div class="metric"><span>Rejected proposals</span><strong id="rejections"></strong><span>before this outcome</span></div></div><p id="scope" class="scope"></p><p id="identity" class="muted detail"></p></section>
<section><h2>What happened to each proposal?</h2><table><thead><tr><th>Tool</th><th>Control [a, b]</th><th>Verification</th></tr></thead><tbody id="attempts"></tbody></table></section></div>
<section><h2>Operator review</h2><p class="small">Read back the displayed P/Q and the requested current allowance. Confirm the model scope and remaining questions before recording your review.</p>
<div class="readback"><div><label for="read-p">P (kW, two decimals)</label><input id="read-p" type="number" step="0.01"></div><div><label for="read-q">Q (kvar, two decimals)</label><input id="read-q" type="number" step="0.01"></div></div>
<label for="read-limit">Allowed current (% of nominal rating)</label><input id="read-limit" type="number" step="0.01">
<label class="check"><input id="scope-check" type="checkbox"><span>I reviewed the model coverage and each failed check.</span></label>
<label class="check"><input id="limits-check" type="checkbox"><span>I understand the measurement assumptions and that this is a simulation recommendation.</span></label>
<label for="operator">Reviewer label (local exercise)</label><input id="operator" maxlength="60" placeholder="Initials or classroom alias">
<button id="ack">Record acknowledgment</button><button id="review" class="secondary">Request further review</button><p id="feedback" role="status" aria-live="polite"></p>
<p class="muted">This local record is unauthenticated. Operational deployment would require the utility's separate authorized operating process, interfaces and validation.</p></section></div>
<section><h2>Agent stages and exact responses</h2><p class="muted">Open a stage to inspect its method and returned evidence. Language-model responses and deterministic calculations retain their labels.</p><div id="trace" class="trace"></div></section></main>
<footer class="muted"><a href="Workshop_Step_by_Step.html">Back to the tutorial</a> · <a href="latex_slides/Agentic_Grid_Workshop_Handout.pdf">Completed-slide handout</a><p>Human-automation roles: <a href="https://doi.org/10.1109/3468.844354">Parasuraman et al. (2000)</a>. Deployment testing context: <a href="https://www.nlr.gov/docs/fy19osti/73705.pdf">Pratt et al. (2019), ADMS test bed</a>. These references do not establish deployment or human-performance gains for this demonstration.</p></footer>
<script>
const records=__RECORDS__;
// These local bindings detect stale UI records; they are not authentication.
const reviewBindings=new Map(records.map(x=>[x.run.recommendation_id,JSON.stringify(x.run)]));
const $=id=>document.getElementById(id);let row;
const num=x=>Number.isFinite(x)?x.toFixed(2):'—';
function readbackValid(r,v){try{
 if(!r||!v||!(/^[0-9a-f]{64}$/).test(r.recommendation_id)||reviewBindings.get(r.recommendation_id)!==JSON.stringify(r))return false;
 const m=r.metrics,c=r.candidate,limit=r.contract.allowed_current_percent_of_nominal;
 if(r.status!=='MODEL_RECOMMEND'||r.equipment_operated!==false||!m||!c||!['SAC','CONTINUOUS_MPC'].includes(c.tool)||!Array.isArray(c.control)||c.control.length!==2||!c.control.every(Number.isFinite))return false;
 const [a,b]=c.control;
 if(a<0||a>1||Math.abs(b)>.44+1e-9||a*a+b*b>1+1e-9)return false;
 if(!Number.isFinite(limit)||limit<=0||limit>100||!Array.isArray(r.attempts)||!r.attempts.length||!Array.isArray(r.reasons)||r.reasons.length)return false;
 const last=r.attempts.at(-1);
 if(!Array.isArray(last.failures)||last.failures.length||JSON.stringify(last.candidate)!==JSON.stringify(c)||JSON.stringify(last.point)!==JSON.stringify(m)||JSON.stringify(m.control)!==JSON.stringify(c.control))return false;
 if(m.accepted!==true||m.converged!==true||m.fresh_model_solve!==true||m.backend!==r.backend||r.contract.backend!==r.backend||!['opendss','lindistflow3'].includes(r.backend)||!m.violations||Object.values(m.violations).some(x=>!Number.isFinite(x)||x!==0))return false;
 if(![m.p_actual_kw,m.q_actual_kvar,m.vmin,m.vmax,m.max_line_utilization_pct,m.max_allowed_current_pct].every(Number.isFinite)||m.vmin<.95-1e-7||m.vmax>1.05+1e-7||m.vmin>m.vmax||m.max_allowed_current_pct<0||m.max_allowed_current_pct>100+1e-5||Math.abs(m.max_allowed_current_pct-m.max_line_utilization_pct*100/limit)>1e-6)return false;
 if(!['p','q','limit','operator'].every(k=>typeof v[k]==='string'&&v[k].trim()!==''))return false;
 return Number(v.p)===Number(m.p_actual_kw.toFixed(2))&&Number(v.q)===Number(m.q_actual_kvar.toFixed(2))&&Number(v.limit)===limit&&v.scope===true&&v.limits===true;
 }catch{return false;}}
function values(){return{p:$('read-p').value,q:$('read-q').value,limit:$('read-limit').value,scope:$('scope-check').checked,limits:$('limits-check').checked,operator:$('operator').value};}
function updateButton(){$('ack').disabled=!row||!readbackValid(row,values());}
function render(){const selected=records[Number($('run').value)];if(!selected)return;row=selected.run;
 $('stamp').textContent='Recorded '+selected.created_utc;
 $('request').textContent='Keep modeled voltage in 0.95–1.05 p.u.; allow '+row.contract.allowed_current_percent_of_nominal+'% of nominal line current. Use continuous shared inverter settings p=aS and q=bS.';
 $('status').textContent=row.status==='MODEL_RECOMMEND'?'Model checks passed · awaiting human review':'Further review required · no accepted recommendation';$('status').className='status'+(row.status==='MODEL_RECOMMEND'?'':' review');
 $('p').textContent=num(row.metrics?.p_actual_kw);$('q').textContent=num(row.metrics?.q_actual_kvar);$('current').textContent=num(row.metrics?.max_allowed_current_pct);$('rejections').textContent=row.gate_rejections;
 $('scope').textContent='Model coverage: '+row.model_scope;$('identity').textContent='Recommendation identity: '+row.recommendation_id;
 $('attempts').replaceChildren();for(const attempt of row.attempts){const tr=document.createElement('tr');for(const text of [attempt.candidate.tool,attempt.candidate.control.map(x=>x.toFixed(5)).join(', '),attempt.failures.length?attempt.failures.join(', '):'PASS in selected model']){const td=document.createElement('td');td.textContent=text;tr.append(td);}$('attempts').append(tr);}
 $('trace').replaceChildren();for(const stage of row.trace){const d=document.createElement('details'),s=document.createElement('summary'),p=document.createElement('p'),pre=document.createElement('pre');s.textContent=stage.stage+' · '+stage.status;p.textContent=stage.method+' | '+stage.response_source;p.className='small';pre.textContent=JSON.stringify(stage.response,null,2);d.append(s,p,pre);$('trace').append(d);}
 for(const id of ['read-p','read-q','read-limit','operator'])$(id).value='';for(const id of ['scope-check','limits-check'])$(id).checked=false;
 $('feedback').textContent='';try{const prior=JSON.parse(localStorage.getItem('continuous-review:'+row.recommendation_id)||'null');if(prior)$('feedback').textContent='Local record: '+prior.decision+' at '+prior.utc;}catch{}updateButton();}
 function record(decision){if(!row||(decision==='ACKNOWLEDGED'&&!readbackValid(row,values())))return;const entry={recommendation_id:row.recommendation_id,decision,readback:values(),utc:new Date().toISOString(),dispatch_authorized:false};try{localStorage.setItem('continuous-review:'+row.recommendation_id,JSON.stringify(entry));$('feedback').textContent='Recorded locally: '+decision+'. No equipment command was sent.';}catch{$('feedback').textContent='Browser storage unavailable; no review record was saved.';}}
 for(let i=0;i<records.length;i++){const option=document.createElement('option');option.value=i;option.textContent=records[i].backend+' · '+records[i].run.method+' · '+records[i].run.case;$('run').append(option);}
 $('run').addEventListener('change',render);for(const id of ['read-p','read-q','read-limit','operator','scope-check','limits-check'])$(id).addEventListener('input',updateButton);
 $('ack').addEventListener('click',()=>record('ACKNOWLEDGED'));$('review').addEventListener('click',()=>record('FURTHER_REVIEW_REQUESTED'));render();
</script></body></html>'''
