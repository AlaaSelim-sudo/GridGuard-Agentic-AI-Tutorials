// Render official documentation diagrams in the browser without changing content.
import {createRequire} from 'node:module';
import fs from 'node:fs';
import crypto from 'node:crypto';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root='C:/Users/f00863x/OPRO/output/agentic_operator_tutorial';
const manifestPath=root+'/images/power_real_framework_manifest.json';
const manifest=JSON.parse(fs.readFileSync(manifestPath,'utf8'));
const specs=[
 {stem:'mcp_architecture',url:'https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture',index:0,refs:['T08'],slides:[73],title:'Official MCP participants and connections',locator:'Core concepts: Participants diagram',caption:'The official MCP diagram separates the host, its clients and connected servers. MCP supplies a communication interface; a power solver still performs the numerical study.',limit:'A protocol architecture does not prove numerical correctness or that a utility uses this implementation.'},
 {stem:'mcp_proxy_boundary',url:'https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices',index:4,refs:['T09'],slides:[74],title:'Official MCP proxy security boundary example',locator:'stdio Transport Security in Proxy Scenarios: attack sequence diagram',caption:'The MCP security guide shows how a malicious server can exploit a vulnerable client/proxy boundary. This is a separate example of why received content must not grant new authority.',limit:'This particular attack requires a proxy architecture and compromised client context. It is not a diagram of retrieved-document prompt injection and does not apply to every direct stdio connection.'},
];
const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
try{
 const page=await browser.newPage({viewport:{width:1600,height:1000},deviceScaleFactor:2,colorScheme:'light'});
 for(const s of specs){
  await page.goto(s.url,{waitUntil:'domcontentloaded',timeout:45000});
  await page.waitForTimeout(2000);
  const svg=page.locator('main svg[id^="mermaid-"],article svg[id^="mermaid-"]').nth(s.index);
  await svg.waitFor({state:'visible'});
  await svg.scrollIntoViewIfNeeded();
  const file='real_framework_'+s.stem+'.png';
  await svg.screenshot({path:root+'/images/'+file,animations:'disabled'});
  const dimensions=await svg.boundingBox();
  const text=await svg.evaluate(e=>{const c=e.cloneNode(true);c.querySelectorAll('style').forEach(s=>s.remove());return c.textContent;});
  const raw=fs.readFileSync(root+'/images/'+file);
  const item={id:'real_framework_'+s.stem,title:s.title,file,path:'images/'+file,width:Math.round(dimensions.width*2),height:Math.round(dimensions.height*2),bytes:raw.length,sha256:crypto.createHash('sha256').update(raw).digest('hex'),source_page_url:s.url,direct_image_url:s.url,source_url:s.url,original_image_url:s.url,source_locator:s.locator,source_refs:s.refs,proposed_slides:s.slides,credit:'Source: Model Context Protocol, official documentation revision July 28, 2026. Screenshot captured October 18, 2026.',caption:s.caption,evidence_limit:s.limit,assumptions:s.limit,transformation:'Native browser screenshot of the original rendered source diagram only. Page navigation and surrounding prose excluded; diagram content unchanged.',license_or_permission_status:'Publisher attribution supplied. No separate permission or unrestricted reuse license claimed.',recommended:true,source_diagram_text:text,visual_qa:'Pending full-size inspection.'};
  manifest.images=manifest.images.filter(x=>x.id!==item.id);manifest.images.push(item);
  console.log(item.id,item.width,item.height,text);
 }
 fs.writeFileSync(manifestPath,JSON.stringify(manifest,null,2));
}finally{await browser.close();}
