import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { fileURLToPath } from 'node:url'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..')
const tutorial=path.dirname(root)
const read=p=>JSON.parse(fs.readFileSync(p,'utf8').replace(/^\uFEFF/,''))
const files=['foundations.json','cases.json','closing.json']
let lessons=files.flatMap(f=>read(path.join(root,'content',f)))
if(new Set(lessons.map(s=>s.id)).size!==lessons.length)throw Error('Duplicate slide IDs')
const breakAt=lessons.findIndex(s=>s.section==='Restoration')
lessons.splice(breakAt,0,{id:'BREAK',title:'Ten-minute break',section:'Pause',kind:'divider',kicker:'82–92 minutes',items:['Save the voltage experiment.','Return with one model-mismatch question.'],takeaway:'Next we change the decision from continuous inverter control to discrete restoration.',refs:[{label:'Classroom_Labs L2–L5',url:'./notebooks/Classroom_Labs.html'}],notes:'Take the scheduled ten-minute break. Participants should save their notebook and record whether the LinDistFlow candidate passed each model. At the restart, ask one participant to explain why the same physical action can pass an aggregated model and fail a more detailed model. This prepares the distinction between proposing a candidate and establishing its admissibility. The next chapter introduces discrete restoration decisions and a priority-weighted objective.',duration_seconds:600})
const manifest=read(path.join(root,'content','checkpoint_manifest.json'))
let mappings=[]
for(let i=0;i<lessons.length;i++){
 const s=lessons[i];s.next=lessons[i+1]?.title;s.order=i+1
 for(const r of s.refs||[]){if(r.url.startsWith('../')){
   const relative=r.url.slice(3),src=path.resolve(tutorial,relative)
   if(!src.startsWith(tutorial+path.sep))throw Error('Invalid local reference '+r.url)
   const dest=/^[^/]+\.(html|ipynb)$/.test(relative)?'notebooks/'+relative:'resources/'+relative
   const target=path.join(root,'public',dest);fs.mkdirSync(path.dirname(target),{recursive:true})
   // Keep copied reference documents usable in the portable workshop package.
   if(fs.existsSync(src))fs.copyFileSync(src,target)
   else if(!fs.existsSync(target))throw Error('Missing local reference '+r.url)
   r.url='./'+dest
 }}
 s.clicks=Math.max(3,Math.min(5,s.items?.length||3),s.nodes?.length-1||0)
 if(s.code){
  const m=manifest.find(m=>m.checkpoint===s.code.cell&&m.notebook===s.code.notebook)
  if(!m)throw Error('Unknown checkpoint '+JSON.stringify(s.code))
  const nb=read(path.join(tutorial,s.code.notebook));const source=nb.cells[m.cell_index].source;const full=Array.isArray(source)?source.join(''):source
  const lines=full.trimEnd().split(/\r?\n/);if(s.code.start<1||s.code.end>lines.length)throw Error('Code range '+s.id)
  s.code_text=lines.slice(s.code.start-1,s.code.end).join('\n')
  mappings.push({slide:i+1,id:s.id,...s.code,cell_index:m.cell_index,sha256:crypto.createHash('sha256').update(full).digest('hex'),excerpt_sha256:crypto.createHash('sha256').update(s.code_text).digest('hex')})
 }
}
fs.writeFileSync(path.join(root,'content','lessons.json'),JSON.stringify(lessons,null,2))
fs.writeFileSync(path.join(root,'content','notebook_map.json'),JSON.stringify(mappings,null,2))
const header=`---\ntheme: ./theme\nlayout: teaching\ntitle: Agentic AI for Grid Operators\ninfo: A three-hour scientific workshop with integrated notebook experiments\ncolorSchema: light\nfonts:\n  sans: Aptos\n  mono: Consolas\n  provider: none\ncanvasWidth: 1280\naspectRatio: 16/9\ntransition: fade-out\nclicks: ${lessons[0].clicks}\ndrawings:\n  persist: false\nmdc: true\nlineNumbers: false\nexportFilename: Agentic_Grid_Slides\ndownload: false\n---\n`
let md=header
for(let i=0;i<lessons.length;i++){
 const s=lessons[i]
 if(i)md+=`\n---\nlayout: teaching\ntitle: ${JSON.stringify(s.title)}\nclicks: ${s.clicks}\ntransition: ${['divider','lab'].includes(s.kind)?'slide-left':'fade-out'}\n---\n`
 md+=`\n<TeachingSlide :index="${i}" :step="$clicks" :complete="$nav.isPrintMode" />\n\n<!--\n${s.notes}\n\nClick sequence: ${s.animation||'Reveal the evidence in order, then discuss the takeaway.'}\n\nNext: ${s.next||'End of workshop'}\n-->\n`
}
fs.writeFileSync(path.join(root,'slides.md'),md)
const assetDir=path.join(root,'public','assets')
fs.mkdirSync(assetDir,{recursive:true})
for(const s of lessons){if(s.image && !s.image.includes('/papers/')){
 const name=path.basename(s.image),src=path.join(tutorial,'figures',name)
 if(!fs.existsSync(src))throw Error('Missing image '+src)
 fs.copyFileSync(src,path.join(assetDir,name))
}}
fs.mkdirSync(path.join(root,'public','notebooks'),{recursive:true})
for(const name of ['Graph_Workflow_Lab','Classroom_Labs'])for(const ext of ['html','ipynb'])fs.copyFileSync(path.join(tutorial,`${name}.${ext}`),path.join(root,'public','notebooks',`${name}.${ext}`))
console.log(JSON.stringify({slides:lessons.length,codeExcerpts:mappings.length,clickSteps:lessons.reduce((a,s)=>a+s.clicks,0)}))
