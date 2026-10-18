import {createRequire} from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.dirname(fileURLToPath(import.meta.url));
const original=fs.existsSync(path.join(root,'research/evidence/Workshop_Step_by_Step.html'))?path.join(root,'research/evidence'):path.resolve(root,'../agentic_grid_workflow_tutorial');
const out=path.join(root,'research/screenshots');fs.mkdirSync(out,{recursive:true});
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
const page=await browser.newPage({viewport:{width:1460,height:1000},deviceScaleFactor:2});
await page.route('https://**/*',route=>route.abort());
const log=[];
async function shot(name,locator,source,limit){
 await locator.evaluate(e=>e.scrollIntoView({block:'start'}));
 let box=await locator.boundingBox();
 const full={...box};
 if(limit)box.height=Math.min(box.height,limit);
 const file=path.join(out,name+'.png');
 await page.screenshot({path:file,clip:box});
 log.push({file:'research/screenshots/'+name+'.png',source_file:source,source_sha256:sha(path.join(original,source)),locator:await locator.evaluate(e=>e.tagName+' '+(e.querySelector('summary')?.textContent||e.querySelector('h2')?.textContent||'')),capture_viewport:{width:1460,height:1000,deviceScaleFactor:2},capture_region:box,element_region:full,cropped:box.height<full.height,source_text:await locator.textContent(),sha256:sha(file),transformation:'Browser screenshot of existing local HTML. Preformatted text enlarged to 18px, line height 1.45; contents unchanged. Selected element crop; no invented interface or result.'});
}
async function excerptShot(name,locator,source,start,end,cropWidth){
 await locator.evaluate(e=>e.scrollIntoView({block:'start'}));
 await locator.locator('pre').evaluate(e=>{e.style.fontSize='28px';e.style.lineHeight='1.45'});
 const region=await locator.locator('pre').evaluate((e,{start,end})=>{
  const n=e.firstChild,t=n.textContent,a=t.indexOf(start),b=t.indexOf(end,a);
  if(a<0||b<0)throw new Error('Missing excerpt boundary');
  const r=document.createRange();r.setStart(n,a);r.setEnd(n,b);
  const box=r.getBoundingClientRect(),pre=e.getBoundingClientRect();
  return {x:pre.x,y:box.y-8,width:pre.width,height:box.height+16,text:t.slice(a,b)};
 },{start,end});
 const file=path.join(out,name+'.png');const {text,...clip}=region;
 if(cropWidth)clip.width=Math.min(clip.width,cropWidth);
 await page.screenshot({path:file,clip});
 log.push({file:'research/screenshots/'+name+'.png',source_file:source,source_sha256:sha(path.join(original,source)),capture_region:clip,selected_original_text:text,sha256:sha(file),transformation:'Selected original preformatted output region; browser text enlarged to28px. Text and numbers unchanged.'});
}
await page.goto('file:///'+original+'/Workshop_Step_by_Step.html');
await page.addStyleTag({content:'pre{font-size:18px!important;line-height:1.45!important;max-height:none!important;overflow:visible!important}'});
const ds=await page.locator('details').evaluateAll(es=>es.map((e,i)=>({i,s:e.querySelector('summary')?.textContent,t:e.querySelector('pre')?.textContent})));
for(const [caseName,prefix] of [['restoration','rest'],['cyber','cyber']]){
 const input=ds.find(e=>e.s==='Awareness | PASS: exact response'&&e.t?.includes('"use_case": "'+caseName+'"'));
 if(!input)throw new Error('No input '+caseName);
 const specs=[['input',input.i,null],['route',input.i+1,360],['result',input.i+2,caseName==='cyber'?420:315],['review',input.i+6,null]];
 for(const [label,index,height]of specs){
  const d=page.locator('details').nth(index);await d.evaluate(e=>e.open=true);
  if(label==='result'){
   if(caseName==='restoration')await excerptShot(prefix+'_'+label,d,'Workshop_Step_by_Step.html','"objective"','"pickup"',610);
   else await excerptShot(prefix+'_'+label,d,'Workshop_Step_by_Step.html','"flexible_injection_pu"','-0.046197066897314544');
  }else await shot(prefix+'_'+label,d,'Workshop_Step_by_Step.html',height);
 }
}
await page.goto('file:///'+original+'/Workshop_Operator_Dashboard.html');
const options=await page.locator('#run option').evaluateAll(es=>es.map(e=>({value:e.value,text:e.textContent})));
const selected=options.find(e=>e.text.includes('opendss')&&e.text.includes('agentic'));
console.log('options',JSON.stringify(options));
if(!selected)throw new Error('No OpenDSS agentic dashboard');
await page.selectOption('#run',selected.value);
const request=page.locator('#request').locator('..');
await shot('voltage_result',request,'Workshop_Operator_Dashboard.html');
await page.addStyleTag({content:'.split,.trace{grid-template-columns:1fr!important}'});
const review=page.locator('#ack').locator('..');
await review.evaluate(e=>e.scrollIntoView({block:'start'}));
const a=await page.locator('#ack').boundingBox(),b=await page.locator('#review').boundingBox();
const clip={x:Math.min(a.x,b.x),y:Math.min(a.y,b.y)-8,width:Math.max(a.x+a.width,b.x+b.width)-Math.min(a.x,b.x),height:Math.max(a.y+a.height,b.y+b.height)-Math.min(a.y,b.y)+16};
const reviewFile=path.join(out,'voltage_review.png');await page.screenshot({path:reviewFile,clip});
log.push({file:'research/screenshots/voltage_review.png',source_file:'Workshop_Operator_Dashboard.html',source_sha256:sha(path.join(original,'Workshop_Operator_Dashboard.html')),capture_region:clip,sha256:sha(reviewFile),acknowledgment_disabled:await page.locator('#ack').isDisabled(),form_values_entered:false,transformation:'Unchanged real decision controls selected from the original local dashboard. No acknowledgment entered.'});
await page.addStyleTag({content:'pre{font-size:18px!important;line-height:1.45!important;max-height:none!important;overflow:visible!important}'});
const trace=await page.locator('#trace details').evaluateAll(es=>es.map((e,i)=>({i,s:e.querySelector('summary')?.textContent,t:e.querySelector('pre')?.textContent})));
console.log('voltage stages',JSON.stringify(trace.map(x=>({i:x.i,s:x.s,t:x.t?.slice(0,90)}))));
const input=page.locator('#trace details').nth(0);await input.evaluate(e=>e.open=true);
await shot('voltage_input',input,'Workshop_Operator_Dashboard.html',345);
const routing=trace.find(e=>e.s?.startsWith('Recovery'));
if(!routing)throw new Error('No routing stage');
const route=page.locator('#trace details').nth(routing.i);await route.evaluate(e=>e.open=true);
await shot('voltage_route',route,'Workshop_Operator_Dashboard.html');
fs.writeFileSync(path.join(out,'capture_manifest.json'),JSON.stringify({captured_utc:new Date().toISOString(),records:log},null,2));
await browser.close();console.log('Captured',log.length);
