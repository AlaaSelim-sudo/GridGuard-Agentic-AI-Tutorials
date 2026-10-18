"""Build a portable operator review dashboard from recorded workflow evidence."""
import json
from .stage_workflow import ROOT


def build_dashboard(data=None):
    data = data or json.loads((ROOT / 'results/model_workflow_reviewed.json').read_text())
    records = []
    for row in data['runs']:
        record = {k: v for k, v in row.items() if k not in ('prediction', 'ac_audit')}
        if row.get('ac_audit'):
            record['ac_audit'] = {k: v for k, v in row['ac_audit'].items() if k not in ('lines', 'node_phase_voltages')}
        records.append(record)
    payload = json.dumps({'metadata': data['metadata'], 'runs': records}, separators=(',', ':')).replace('<', '\\u003c')
    page = TEMPLATE.replace('__WORKFLOW_DATA__', payload)
    target = ROOT / 'Operator_Dashboard.html'
    target.write_text(page, encoding='utf-8')
    return target


TEMPLATE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Operator review | Agentic grid workflow</title>
<style>
:root{--ink:#193d4b;--muted:#60747e;--teal:#007f83;--soft:#e9f3f3;--amber:#b95d17;--line:#dbe5e8;--red:#a7353d}
*{box-sizing:border-box}body{margin:0;background:#f2f5f6;color:var(--ink);font:15px/1.5 system-ui,Segoe UI,Arial,sans-serif}
header{background:#193d4b;color:white;padding:24px 5vw 20px}header .eyebrow{font-size:12px;letter-spacing:2px;color:#92d9d6;text-transform:uppercase}
h1{font-size:28px;margin:3px 0 7px;letter-spacing:-.5px}header p{color:#d5e2e6;margin:0;max-width:1000px}
main{max-width:1440px;padding:24px;margin:auto}h2{font-size:20px;margin:0 0 14px}h3{font-size:16px;margin:0 0 8px}p{margin:5px 0 12px}
.toolbar{display:flex;align-items:end;gap:16px;flex-wrap:wrap;padding:18px;background:white;border:1px solid var(--line);border-radius:10px}
label{font-weight:600;font-size:13px}select,input[type=text]{display:block;margin-top:5px;border:1px solid #a9bec5;border-radius:6px;padding:10px 12px;color:var(--ink);background:white;font-size:14px;min-height:42px}
select{min-width:195px}input[type=text]{width:100%}.toolbar .subtle{margin-left:auto;max-width:320px;font-size:12px;color:var(--muted)}
.ribbon{margin:18px 0;padding:16px 20px;border-radius:9px;background:var(--soft);border-left:5px solid var(--teal)}.ribbon.warning{background:#fff2e5;border-color:var(--amber)}
.ribbon strong{display:block;font-size:19px}.muted{color:var(--muted)}.small{font-size:12px}.grid{display:grid;grid-template-columns:1fr 370px;gap:22px}.card{background:white;border:1px solid var(--line);border-radius:10px;padding:22px;margin-bottom:20px}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:18px 0}.metric{background:white;border:1px solid var(--line);padding:15px;border-radius:8px}.metric .number{display:block;font-size:25px;font-weight:650;letter-spacing:-.5px}.metric .label{font-size:12px;color:var(--muted)}
.pill{display:inline-block;border-radius:20px;background:var(--soft);color:#086c6b;font-size:11px;padding:3px 8px;font-weight:700;white-space:nowrap}.pill.warn{background:#fff0df;color:#94490d}.pill.fail{background:#fce9ea;color:var(--red)}
table{width:100%;border-collapse:collapse;font-size:13px}th,td{text-align:left;padding:9px 8px;border-bottom:1px solid var(--line);vertical-align:top}th{font-size:11px;text-transform:uppercase;letter-spacing:.6px;color:var(--muted)}
.stage{border-left:2px solid #cae1e2;padding:0 0 20px 20px;position:relative}.stage:last-child{padding-bottom:0}.stage:before{content:'';position:absolute;left:-6px;top:6px;background:var(--teal);height:10px;width:10px;border-radius:50%}.stage-top{display:flex;gap:10px;align-items:center;justify-content:space-between}.method{font-size:13px;color:var(--muted);margin:3px 0 8px}.response{font-size:13px;background:#f4f8f9;padding:10px 12px;border-radius:5px;overflow-wrap:anywhere}.quote{border-left:3px solid #8bc7c5;padding:7px 12px;margin-top:9px;font-size:13px}details{margin-top:7px}summary{cursor:pointer;font-size:12px;color:#006a74}pre{font:11px/1.45 Consolas,monospace;white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f7f8;padding:12px;max-height:370px;overflow:auto}
.checks label{display:flex;align-items:start;gap:10px;font-size:13px;font-weight:400;margin:13px 0}.checks input{margin-top:4px;accent-color:var(--teal)}button{border:0;background:var(--teal);color:white;border-radius:6px;font:600 14px system-ui;padding:12px 16px;cursor:pointer}button:disabled{background:#afc3c7;cursor:not-allowed}.secondary{background:#eaf1f3;color:var(--ink);margin-top:8px}.ackstate{padding:12px;background:#f2f7f7;border:1px solid var(--line);border-radius:6px;font-size:13px;margin-top:14px;overflow-wrap:anywhere}.warningtext{color:#925017}.reading{font-size:12px;color:var(--muted);margin:10px 0}.wide{grid-column:1/-1}footer{color:var(--muted);font-size:12px;padding:10px 0 20px}.tablewrap{overflow-x:auto}a{color:#006f7b}.numbers{font-variant-numeric:tabular-nums}.action{font-size:20px;font-weight:650}.plain-list{padding-left:18px;margin:6px 0}
@media(max-width:1050px){.grid{grid-template-columns:1fr}.metrics{grid-template-columns:repeat(2,1fr)}.toolbar .subtle{margin:0}}@media(max-width:600px){main{padding:12px}.card{padding:16px}header{padding:20px}.toolbar label,select{width:100%}h1{font-size:24px}.metric .number{font-size:21px}}
</style></head><body>
<header><div class="eyebrow">Greensboro feeder · teaching simulator</div><h1>Operator review desk</h1><p>Review the proposed action, inspect every agent response, compare model evidence, and acknowledge what you have reviewed.</p></header>
<main><p class="reading"><strong>Three use cases:</strong> Voltage support, Restoration, and Cyber-attack response. This dashboard retains the recorded finite-catalog workflow. The <a href="Standard_Formulations.html">OPF, MILP and WLS laboratory</a> introduces the general formulations and separate conventional-method experiments.</p><div class="toolbar">
<label>Scenario<select id="case"><optgroup label="1. Voltage support"><option value="V1" selected>V1 · Normal voltage support</option><option value="V2">V2 · Reduced current allowance</option><option value="V3">V3 · Infeasible forecast</option></optgroup><optgroup label="2. Restoration"><option value="R1">R1 · Restoration, two routes</option><option value="R2">R2 · Restoration, limited capacity</option></optgroup><optgroup label="3. Cyber-attack response"><option value="C1">C1 · Stale measurements</option><option value="C2">C2 · Biased measurements</option><option value="C3">C3 · Untrusted instruction</option></optgroup></select></label>
<label>Prediction model<select id="backend"><option value="opendss">OpenDSS · full feeder</option><option value="lindistflow3">LinDistFlow · MV phases</option></select></label>
<label>Supervisor<select id="method"><option value="agentic">Agentic · local Llama</option><option value="fixed">Conventional · adaptive rules</option></select></label>
<div class="subtle">Recorded experiments, with actual local model responses. Changing a selection displays a saved run; it does not make a new model call.</div></div>
<div id="ribbon" class="ribbon" aria-live="polite"></div><div id="metrics" class="metrics numbers"></div>
<div class="grid"><section><div class="card"><h2>Recommendation and model evidence</h2><div id="action"></div><div class="tablewrap" id="comparison"></div><div id="scope" class="reading"></div></div>
<div class="card"><h2>Agent responses, in execution order</h2><p class="muted small">Each stage names its numerical method and exposes its actual output. Llama wording is unverified: compare it with the numerical evidence and selected model scope.</p><div id="trace"></div></div></section>
<aside><div class="card"><h2>Operator acknowledgment</h2><p class="small">This records a local review of the displayed result. It sends no dispatch command and does not certify grid safety.</p>
<div id="ackcontext" class="reading"></div><label>Your name or training identifier<input id="operator" type="text" maxlength="80" autocomplete="off" placeholder="Enter your identifier"></label>
<div class="checks"><label><input id="check-action" type="checkbox">I have read the proposed action or stop decision and the permitted current limit.</label><label><input id="check-scope" type="checkbox">I understand which model produced this result and what its checks do not cover.</label><label><input id="check-risk" type="checkbox">I have reviewed the failures, reference audit, and remaining uncertainties.</label></div>
<button id="acknowledge" disabled>Acknowledge review</button><div id="ackstate" class="ackstate" aria-live="polite">PENDING · operator acknowledgment required.</div>
<details id="receipt-preview" hidden><summary>Inspect this review record</summary><pre id="receipt-json"></pre></details>
<button id="download" class="secondary" disabled>Download review record</button><button id="reset" class="secondary">Clear this local acknowledgment</button>
<p class="reading">Saved in this browser for this exact review ID. A different recommendation or audit requires a separate acknowledgment. This is a teaching record, not authenticated identity or a tamper-proof log.</p></div>
<div class="card"><h3>What the operator should verify</h3><ul class="plain-list small"><li>Correct scenario and present equipment state.</li><li>PV cap, restoration route and disconnected demand.</li><li>Current allowance and the model’s voltage limits.</li><li>Any disagreement between the linear prediction and AC check.</li><li>Separate authorization and operational procedures before real execution.</li></ul></div>
<div class="card"><h3>Run evidence</h3><div id="provenance" class="small muted"></div><p class="small"><a href="Grid_Operator_Workflow.html">Return to the full tutorial</a></p></div></aside></div>
<footer>One synthetic Greensboro feeder. Nominal connected demand is not measured delivered power. MV linear losses and full-feeder AC losses have different coverage. Protection, switching transients and transformer thermal limits are outside this lesson.</footer>
</main><script type="application/json" id="study-data">__WORKFLOW_DATA__</script><script>
'use strict';
const study=JSON.parse(document.getElementById('study-data').textContent), el=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=(n,d=2)=>n===null||n===undefined?'—':Number(n).toFixed(d);
let current, acknowledgment=null;
function loadAck(){try{return JSON.parse(localStorage.getItem('grid-review-'+current.review_id)||'null')}catch{return null}}
function actionText(r){if(!r.candidate)return 'No action recommended';const c=r.candidate;return `PV cap ${c.pv_cap}% · ${c.tie==='none'?'original radial topology':c.tie+' restoration route'} · shed ${Math.round(c.shed_fraction*100)}% of the ordered noncritical load objects`;}
function stageSummary(s){const r=s.response;if(s.stage==='Awareness')return `${s.status}: voltage residual ${fmt(r.max_voltage_residual_pu,4)} pu; ${r.failures.length?r.failures.join(', '):'freshness and topology checks passed'}.`;
if(s.stage==='Planning'&&r.numerical_plan){const p=r.numerical_plan;return `Numerical status: ${p.status}. ${p.plan_caps?'MPC horizon caps: '+p.plan_caps.join(' → ')+'%. ':''}Effective strategy: ${r.effective_strategy}. ${r.declared_intervention||''}`;}
if(s.stage==='Execution'&&r.candidate)return `${r.candidate.tool} proposed PV=${r.candidate.pv_cap}%, route=${r.candidate.tie}, shedding=${r.candidate.shed_fraction}. Simulation proposal only.`;
if(s.stage==='Simulation'&&r.vmin!==undefined)return `Voltage ${fmt(r.vmin,4)}–${fmt(r.vmax,4)} pu; allowed-current utilization ${fmt(r.allowed_current_utilization_pct,1)}%; connected demand ${fmt(r.served_kw,1)} kW.`;
if(s.stage==='Verification'&&r.failures)return `${r.accepted_in_model_scope?'PASS within declared model scope':'REJECT: '+r.failures.join(', ')}. MPC value gap: ${fmt(r.value_gap,4)}. ${r.scope_warning||''}`;
if(s.stage==='Recovery'&&r.decision)return `${r.decision}: ${r.reason}`;
if(s.stage==='Explanation'&&r.operator_card)return `${r.operator_card.status}. ${r.operator_card.operator_requirement}`;
if(s.stage==='Operator acknowledgment')return 'PENDING when this run was recorded. Your local readback is shown in the panel at right.';
return r.reason||s.status;}
function render(){current=study.runs.find(r=>r.case===el('case').value&&r.backend===el('backend').value&&r.method===el('method').value);if(!current){el('ribbon').textContent='This combination was not run.';return}
const r=current,a=r.ac_audit,m=r.metrics,good=r.final_review_status==='AC_CHECK_PASSED',domain=a?.failure_scope?.voltage_current_failure_scope,lvOnly=domain==='LV_ONLY';el('ribbon').className='ribbon'+(good?'':' warning');
el('ribbon').innerHTML=`<strong>${good?'Ready for operator review':r.candidate?(lvOnly?'AC coverage gap · review required':'AC reference disagreement · review required'):'Stopped · review the evidence'}</strong>${good?'Recommendation passed the stated full-feeder AC reference checks.':r.candidate?(lvOnly?'The separate AC audit found violations only in LV circuits outside the linear model’s coverage. This is not evidence of a poor MV approximation.':'The selected model accepted an action that failed the separate AC check. Inspect the failure domains below.'):'The workflow produced no accepted recommendation.'} Operator acknowledgment is still pending unless recorded below.`;
el('metrics').innerHTML=[['PV cap',r.candidate?fmt(r.candidate.pv_cap,0)+'%':'—'],['Connected demand',m?fmt(m.served_kw/1000,2)+' MW':'—'],['Allowed current use',m?fmt(m.allowed_current_utilization_pct,1)+'%':'—'],['Live Llama calls in run',r.llm_calls]].map(([label,number])=>`<div class="metric"><span class="label">${label}</span><span class="number">${number}</span></div>`).join('');
el('action').innerHTML=`<p class="action">${esc(actionText(r))}</p><p class="small">Permitted line-current fraction: <strong>${fmt(r.case_definition.rating_fraction*100,0)}%</strong>; short-route ceiling: <strong>${fmt(r.case_definition.capacity,0)} A</strong>. ${esc(r.reasons.join(', '))}</p>`;
const other=study.runs.find(x=>x.case===r.case&&x.method===r.method&&x.backend!==r.backend);
el('comparison').innerHTML='<table><thead><tr><th>Evidence</th><th>Selected prediction</th><th>Same action: AC audit</th></tr></thead><tbody>'+[
['Coverage',r.model_scope==='full_feeder'?'Full feeder':'MV only','Full feeder'],
['Voltage (pu)',m?fmt(m.vmin,4)+'–'+fmt(m.vmax,4):'—',a?fmt(a.metrics.vmin,4)+'–'+fmt(a.metrics.vmax,4):'—'],
['Allowed current (%)',m?fmt(m.allowed_current_utilization_pct,1):'—',a?fmt(a.metrics.allowed_current_utilization_pct,1):'—'],
['Result',r.status,a?(a.accepted?'AC check passed':a.failures.join(', ')):'No candidate to audit'],
['AC failure domain','—',domain||'—']].map(v=>'<tr>'+v.map(x=>'<td>'+esc(x)+'</td>').join('')+'</tr>').join('')+'</tbody></table>';
el('scope').innerHTML=`${r.backend==='lindistflow3'?'LinDistFlow includes coupled MV phases and aggregates secondaries at ideal transformer primaries. It does not predict LV voltages or transformer loading.':'OpenDSS represents the original feeder and secondary circuits. The verifier still omits protection and transformer thermal constraints.'}<br>${other?'Other model’s proposed action: '+esc(actionText(other)):''}<br>Common MV maximum voltage error: ${fmt(r.common_domain_error?.voltage_max_abs_error_pu,5)} pu. Workflow ${fmt(r.seconds)} s; separate AC audit ${fmt(a?.seconds)} s.`;
el('trace').innerHTML=r.trace.map((s,i)=>{const lang=s.response.language_response||(s.response.call_id?s.response:null);const warn=['REJECT','REVIEW','FAILED'].includes(s.status);return `<div class="stage"><div class="stage-top"><h3>${i+1}. ${esc(s.stage)}</h3><span class="pill ${warn?'fail':s.status==='PENDING'?'warn':''}">${esc(s.status)}</span></div><div class="method">${esc(s.method)}</div><div class="response">${esc(stageSummary(s))}</div>${lang?`<div class="quote"><strong>${lang.error?'Local failure fallback':'Actual Llama response'} · call ${lang.call_id}</strong><br>${esc(lang.reason)}</div>`:''}<details><summary>Inspect exact inputs and response</summary><pre>${esc(JSON.stringify(s,null,2))}</pre></details></div>`}).join('');
el('ackcontext').textContent='Review ID: '+r.review_id.slice(0,16)+'…';el('provenance').innerHTML=`Run: ${esc(study.metadata.run_id)}<br>Model: ${esc(study.metadata.llama?.name||'No Llama')}<br>Method: ${esc(r.method)}<br>Model solves: ${r.model_solves}<br>Rejected proposals: ${r.gate_rejections}<br>All values are recorded simulation results.`;
for(const id of ['check-action','check-scope','check-risk'])el(id).checked=false;el('operator').value='';acknowledgment=loadAck();renderAck();}
function renderAck(){el('ackstate').textContent=acknowledgment?`ACKNOWLEDGED by ${acknowledgment.operator_id} at ${acknowledgment.acknowledged_utc}. Local review only; no command sent.`:'PENDING · operator acknowledgment required.';el('download').disabled=!acknowledgment;el('receipt-preview').hidden=!acknowledgment;el('receipt-json').textContent=acknowledgment?JSON.stringify(acknowledgment,null,2):'';updateButton();}
function updateButton(){el('acknowledge').disabled=!!acknowledgment||el('operator').value.trim().length<2||!['check-action','check-scope','check-risk'].every(id=>el(id).checked);}
for(const id of ['case','backend','method'])el(id).addEventListener('change',render);for(const id of ['operator','check-action','check-scope','check-risk'])el(id).addEventListener('input',updateButton);
el('acknowledge').addEventListener('click',()=>{if(el('acknowledge').disabled)return;acknowledgment={schema:'operator_review.v1',review_id:current.review_id,recommendation_id:current.recommendation_id,case:current.case,backend:current.backend,supervisor:current.method,review_status:current.final_review_status,operator_id:el('operator').value.trim(),acknowledged_utc:new Date().toISOString(),readbacks:{action_and_current_limit:true,model_scope:true,remaining_risks:true},effect:'local_review_only',dispatch_authorized:false,equipment_operated:false};try{localStorage.setItem('grid-review-'+current.review_id,JSON.stringify(acknowledgment))}catch{}renderAck();});
el('download').addEventListener('click',()=>{if(!acknowledgment)return;const url=URL.createObjectURL(new Blob([JSON.stringify(acknowledgment,null,2)],{type:'application/json'}));const link=document.createElement('a');link.href=url;link.download='operator_review_'+current.case+'_'+current.review_id.slice(0,8)+'.json';link.click();URL.revokeObjectURL(url);});
el('reset').addEventListener('click',()=>{try{localStorage.removeItem('grid-review-'+current.review_id)}catch{}acknowledgment=null;for(const id of ['check-action','check-scope','check-risk'])el(id).checked=false;el('operator').value='';renderAck();});render();
</script></body></html>'''


if __name__ == '__main__':
    print(build_dashboard())
