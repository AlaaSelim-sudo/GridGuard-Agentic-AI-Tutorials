import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {completeEvidenceLinks} from './complete-evidence-links.mjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const args=process.argv.slice(2);
const value=(flag,fallback)=>args.includes(flag)?args[args.indexOf(flag)+1]:fallback;
const base=value('--base','/GridGuard-Agentic-AI-Tutorials/');
if(!/^\/(?:[A-Za-z0-9_-]+\/)*$/.test(base))throw new Error('Base must be an absolute directory URL ending in /.');
const out=path.join(root,'_site');
fs.mkdirSync(out,{recursive:true});
const repo='https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials';
const decks=[
  {slug:'foundations',folder:'agentic_operator_tutorial',slides:80,pdf:'latex/main.pdf'},
  {slug:'operator-cases',folder:'agentic_operator_cases_tutorial',pdf:'Three_Operator_Cases.pdf'},
];
const walk=dir=>fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);
const copy=(from,to)=>{fs.mkdirSync(path.dirname(to),{recursive:true});fs.copyFileSync(from,to);};
const report={base,decks:[],downloads:[]};

for(const deck of decks){
  if(!deck.slides)deck.slides=JSON.parse(fs.readFileSync(path.join(root,deck.folder,'lesson_content.json'),'utf8')).length;
  const project=path.join(root,deck.folder,'slidev');
  const target=path.join(out,deck.slug);
  const cli=path.join(project,'node_modules/@slidev/cli/bin/slidev.mjs');
  if(!fs.existsSync(cli))throw new Error('Install the pinned dependencies in '+project+' first.');
  const built=spawnSync(process.execPath,[cli,'build','slides.md','--base',base+deck.slug+'/','--out',target,'--router-mode','hash'],{cwd:project,stdio:'inherit',env:process.env});
  if(built.status!==0)throw new Error('Slidev build failed for '+deck.slug);
  let rewritten=0;
  // Vite rebases images and styles. Ordinary source-guide anchors need the same prefix.
  for(const file of walk(target).filter(p=>p.endsWith('.js')||p.endsWith('.css')||path.dirname(p)===target&&p.endsWith('.html'))){
    const original=fs.readFileSync(file,'utf8');
    const prefix=base+deck.slug+'/';
    const text=original
      .replace(/(\bhref\s*[:=]\s*)(["'`])\/(research\/|Full_Reading_Guide(?:\.html|\.pdf)|Code_and_Record_Guide\.html|Exercises\.html)/g,(_,a,q,tail)=>{rewritten++;return a+q+prefix+tail;});
    if(text!==original)fs.writeFileSync(file,text);
  }
  const evidence=await completeEvidenceLinks(root,target);
  copy(path.join(root,deck.folder,deck.pdf),path.join(out,'downloads',deck.slug+'.pdf'));
  report.downloads.push('downloads/'+deck.slug+'.pdf');
  report.decks.push({slug:deck.slug,slides:deck.slides,base:base+deck.slug+'/',router:'hash',sourceAnchorsRebased:rewritten,evidence});
}
for(const [from,to] of [
  ['agentic_operator_tutorial/Full_Reading_Guide.pdf','foundations-reading-guide.pdf'],
  ['agentic_operator_cases_tutorial/Teaching_and_Source_Guide.pdf','operator-cases-teaching-guide.pdf'],
  ...['Classroom_Labs','Graph_Workflow_Lab','Agent_Trace_and_Latency'].map(n=>['agentic_grid_workflow_tutorial/'+n+'.ipynb',n+'.ipynb']),
]){copy(path.join(root,from),path.join(out,'downloads',to));report.downloads.push('downloads/'+to);}
fs.cpSync(path.join(root,'web/assets'),path.join(out,'assets'),{recursive:true});
fs.cpSync(path.join(root,'third_party'),path.join(out,'third_party'),{recursive:true});
const notices=fs.readdirSync(path.join(out,'third_party/notices')).filter(n=>n.endsWith('.txt'));
fs.writeFileSync(path.join(out,'third_party/notices/index.html'),'<!doctype html><meta charset="utf-8"><title>Dependency notices</title><main style="font:18px/1.6 Arial;max-width:900px;margin:45px auto;padding:25px"><p><a href="'+base+'">GridGuard tutorials</a></p><h1>Dependency notices</h1><ul>'+notices.map(n=>'<li><a href="'+n+'">'+n+'</a></li>').join('')+'</ul></main>');
let landing=fs.readFileSync(path.join(root,'web/index.html'),'utf8').replaceAll('{{BASE}}',base).replaceAll('{{REPO}}',repo);
fs.writeFileSync(path.join(out,'index.html'),landing);
fs.writeFileSync(path.join(out,'.nojekyll'),'');
fs.writeFileSync(path.join(out,'404.html'),'<!doctype html><meta charset="utf-8"><title>GridGuard tutorials</title><main style="font:22px/1.6 Arial;max-width:800px;margin:80px auto;padding:25px"><h1>Find the tutorial</h1><p>This address is unavailable. Open a presentation from the tutorial home page.</p><p><a href="'+base+'">Go to the GridGuard tutorials</a></p></main>');
fs.writeFileSync(path.join(out,'site-manifest.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({site:out,decks:report.decks.map(d=>({slug:d.slug,slides:d.slides,sourceAnchorsRebased:d.sourceAnchorsRebased,evidence:d.evidence})),downloads:report.downloads},null,2));
