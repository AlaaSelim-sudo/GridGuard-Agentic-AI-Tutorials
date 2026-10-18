<script setup>
import { computed } from 'vue'
const props = defineProps({ kind: String, nodes: Array, step: Number, complete: Boolean })
const mode = computed(() => props.kind || 'stages')
const labels = computed(() => props.nodes?.length ? props.nodes :
  mode.value === 'dag' ? ['Evidence','MPC plan','SAC candidate','Compare','Review'] :
  mode.value === 'cycle' ? ['Propose','Simulate','Verify','Repair','Hold / review'] :
  mode.value === 'checkpoint' ? ['Run','Save state','Pause','Readback','Resume'] :
  mode.value === 'state' ? ['Request','Measurements','Candidate','Evidence','Decision'] :
  mode.value === 'tools' ? ['Intent','Typed request','Tool','Numeric result','Explanation'] :
  mode.value === 'control' ? ['Telemetry','Advisory service','Evidence gate','Operator','Approved process'] :
  ['Awareness','Planning','Simulation','Verification','LLM optimizer'])
const points = computed(() => {
  const n=labels.value.length
  if(mode.value==='reactloop') return [[160,75],[640,75],[640,235],[160,235]]
  if(mode.value==='dag' && n===4) return [[105,150],[380,65],[380,235],[690,150]]
  if(mode.value==='dag' && n===5) return [[105,150],[300,65],[300,235],[495,150],[690,150]]
  if(mode.value==='cycle' && n===4) return [[105,85],[380,85],[380,225],[690,85]]
  if(mode.value==='route') return [[95,150],[310,150],[650,40],[650,150],[650,260]]
  if(mode.value==='cycle' && n===5) return [[105,85],[300,85],[495,85],[495,225],[690,85]]
  return labels.value.map((x,i)=>[90+i*620/Math.max(1,n-1),145])
})
const edges = computed(() => {
  if(['roles','claims'].includes(mode.value)) return []
  if(mode.value==='reactloop') return [[0,1],[1,2],[2,3],[3,0]]
  if(mode.value==='dag' && labels.value.length===4) return [[0,1],[0,2],[1,3],[2,3]]
  if(mode.value==='dag' && labels.value.length===5) return [[0,1],[0,2],[1,3],[2,3],[3,4]]
  if(mode.value==='cycle' && labels.value.length===4) return [[0,1],[1,2],[2,0],[1,3]]
  if(mode.value==='route') return [[0,1],[1,2],[1,3],[1,4]]
  if(mode.value==='cycle' && labels.value.length===5) return [[0,1],[1,2],[2,3],[3,1],[2,4]]
  return labels.value.slice(1).map((_,i)=>[i,i+1])
})
function path(e){ const a=points.value[e[0]],b=points.value[e[1]],dx=b[0]-a[0],dy=b[1]-a[1];const t=Math.min(74/Math.max(1,Math.abs(dx)),38/Math.max(1,Math.abs(dy)));return `M ${a[0]+t*dx} ${a[1]+t*dy} L ${b[0]-t*dx} ${b[1]-t*dy}` }
function lines(label){ const words=String(label).split(' '); const l=[];for(const word of words){if(!l.length||l[l.length-1].length+word.length>15)l.push(word);else l[l.length-1]+=' '+word}return l.slice(0,3) }
const active = computed(()=>Math.min(labels.value.length-1,props.step||0))
const isActive=i=>props.complete||(mode.value==='dag'&&labels.value.length===4?((props.step||0)===1?[1,2].includes(i):i===((props.step||0)===0?0:3)):active.value===i)
const viewBox=computed(()=>['dag','cycle','route','reactloop'].includes(mode.value)?'0 0 800 300':mode.value==='stages'?'0 45 800 230':'0 45 800 180')
</script>
<template>
  <svg class="flow-viz" :viewBox="viewBox" role="img" :aria-label="`${mode} workflow diagram`">
    <defs><marker :id="'arrow-'+mode" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor" /></marker></defs>
    <g class="flow-edges"><path v-for="(e,i) in edges" :key="i" :d="path(e)" :marker-end="`url(#arrow-${mode})`" /></g>
    <g v-for="(label,i) in labels" :key="i" :transform="`translate(${points[i][0]},${points[i][1]})`" :class="['flow-node',{active:isActive(i),visited:complete||active>i}]">
      <rect x="-71" y="-35" width="142" height="70" rx="5" />
      <text text-anchor="middle"><tspan v-for="(line,j) in lines(label)" :key="j" x="0" :y="-(lines(label).length-1)*10+6+j*20">{{ line }}</tspan></text>
      <text class="flow-index" text-anchor="middle" y="-52">{{ String(i+1).padStart(2,'0') }}</text>
    </g>
    <text v-if="mode==='cycle'" class="diagram-caption" x="400" y="290" text-anchor="middle">Bounded repair budget • exhausted budget routes to HOLD</text>
    <text v-else-if="mode==='dag'" class="diagram-caption" x="400" y="290" text-anchor="middle">Dependencies determine which tools may run together</text>
    <g v-if="mode==='claims'"><text class="diagram-caption" x="245" y="145" text-anchor="middle">does not prove</text><text class="diagram-caption" x="555" y="145" text-anchor="middle">does not prove</text></g>
    <g v-if="labels[0]==='Awareness' && labels[4]==='LLM optimizer' && (complete||step>=4)" class="flow-edges"><path d="M 710 183 V 220 H 400 V 184" :marker-end="`url(#arrow-${mode})`"/><text class="diagram-caption" x="555" y="247" text-anchor="middle">New candidate: simulate and verify again</text></g>
  </svg>
</template>
