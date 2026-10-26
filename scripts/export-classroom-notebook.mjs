// Export the learner notebook using the Markdown renderer already pinned by Slidev.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const packages=path.join(root,'agentic_operator_cases_tutorial/slidev/node_modules/.pnpm');
const version=fs.readdirSync(packages).filter(n=>/^markdown-it@\d/.test(n)).sort().at(-1);
if(!version)throw Error('Install the pinned Slidev dependencies first.');
const MarkdownIt=createRequire(import.meta.url)(path.join(packages,version,'node_modules/markdown-it'));
const md=new MarkdownIt({html:true,linkify:true});
const lab=path.join(root,'agentic_grid_workflow_tutorial');
const file=path.join(lab,'Classroom_Labs.ipynb');
const nb=JSON.parse(fs.readFileSync(file,'utf8'));
const join=v=>Array.isArray(v)?v.join(''):v||'';
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const prior=fs.readFileSync(path.join(lab,'Classroom_Labs.html'),'utf8');
const css=prior.match(/<style>([\s\S]*?)<\/style>/)?.[1]||'';
function render(text){
 const math=[];
 const prepared=text.replace(/\\\[[\s\S]*?\\\]|\$\$[\s\S]*?\$\$|\$[^$\n]+?\$/g,m=>{math.push(m);return 'MATHSLOT'+(math.length-1)+'END';});
 return md.render(prepared).replace(/MATHSLOT(\d+)END/g,(_,n)=>esc(math[Number(n)]));
}
const chapters=nb.cells.filter(c=>c.cell_type==='markdown'&&/^##?\s/m.test(join(c.source)));
const nav=chapters.map(c=>{const heading=join(c.source).match(/^##?\s+(.+)/m)[1];return '<a href="#'+esc(c.id)+'">'+esc(heading)+'</a>';}).join('');
let out='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Classroom Labs: three operator cases</title><style>'+css+'</style><script>window.MathJax={tex:{inlineMath:[["$","$"]],displayMath:[["\\\\[","\\\\]"]]},options:{skipHtmlTags:["script","noscript","style","textarea","pre","code"]}};</script><script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script></head><body><nav><strong>CLASSROOM LABS</strong>'+nav+'</nav><main><div class="notice">Read the instructions here, then <a href="https://colab.research.google.com/github/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials/blob/main/agentic_grid_workflow_tutorial/Classroom_Labs.ipynb">run the notebook in Colab</a>. Python calculates new results. Llama replies are separately labeled saved records.</div>';
for(const cell of nb.cells){
 out+='<section id="'+esc(cell.id)+'">';
 if(cell.cell_type==='markdown')out+=render(join(cell.source));
 else{
  out+='<details class="code"><summary>Code: '+esc(cell.id)+'</summary><pre><code>'+esc(join(cell.source))+'</code></pre></details>';
  for(const o of cell.outputs||[]){const d=o.data||{};if(d['image/png'])out+='<figure><img alt="Notebook plot" src="data:image/png;base64,'+join(d['image/png'])+'"></figure>';else if(d['text/html'])out+='<div class="table-wrap">'+join(d['text/html'])+'</div>';else if(o.text||d['text/plain'])out+='<pre>'+esc(join(o.text||d['text/plain']))+'</pre>';}
 }
 out+='</section>';
}
out+='<p class="footer">Synthetic and reduced teaching models. Saved model replies keep their original case inputs. No equipment commands.</p></main></body></html>';
fs.writeFileSync(path.join(lab,'Classroom_Labs.html'),out);
for(const ext of ['ipynb','html'])fs.copyFileSync(path.join(lab,'Classroom_Labs.'+ext),path.join(lab,'slidev/public/notebooks/Classroom_Labs.'+ext));
console.log(JSON.stringify({cells:nb.cells.length,codeCells:nb.cells.filter(c=>c.cell_type==='code').length,html:'Classroom_Labs.html'}));
