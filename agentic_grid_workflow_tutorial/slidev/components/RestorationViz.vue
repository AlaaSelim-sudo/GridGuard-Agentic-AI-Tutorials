<script setup>
defineProps({step:Number,complete:Boolean})
const nodes=[{id:0,x:90,y:70,load:'Source'},{id:1,x:300,y:70,load:'40 kW'},{id:2,x:510,y:70,load:'60 kW · critical'},{id:3,x:730,y:70,load:'70 kW'},{id:4,x:730,y:240,load:'50 kW'},{id:5,x:510,y:240,load:'30 kW · critical'}]
</script>
<template>
 <svg class="restoration-viz" viewBox="0 0 850 355" role="img" aria-label="Exact six-node restoration teaching graph with faulted 1–2 line and two candidate ties">
  <g fill="none" stroke="currentColor" stroke-width="3"><path d="M90 70H300"/><path d="M510 70H730V240M510 70V240"/></g>
  <path d="M300 70H510" stroke="#db776c" stroke-width="3" stroke-dasharray="7 6"/><text x="405" y="45" text-anchor="middle" fill="#eea397">FAULT 1–2</text><path d="M395 60L415 80M395 80L415 60" stroke="#db776c" stroke-width="3"/>
  <g :opacity="complete||step>=2?1:.18" class="network-option"><path d="M300 90V240H485" stroke="#80dae1" stroke-width="3" stroke-dasharray="7 5" fill="none"/><text x="390" y="218" text-anchor="middle" fill="#80dae1">Tie 1–5 · 100 kW</text></g>
  <g :opacity="complete||step>=3?1:.18" class="network-option"><path d="M90 90V320H730V265" stroke="#e3a743" stroke-width="3" stroke-dasharray="7 5" fill="none"/><text x="360" y="310" text-anchor="middle" fill="#e3a743">Tie 0–4 · sweep 40–120 kW</text></g>
  <g v-for="n in nodes" :key="n.id"><circle :cx="n.x" :cy="n.y" r="21" :fill="[2,5].includes(n.id)?'#e3a743':'#eff5f3'"/><text :x="n.x" :y="n.y+7" text-anchor="middle" fill="#102e39" font-weight="700">{{n.id}}</text><text :x="n.id===4?805:n.x" :y="n.y===70?22:n.id===4?245:n.y+43" text-anchor="middle" fill="currentColor">{{n.load}}</text></g>
  <text class="network-caption" x="425" y="350" text-anchor="middle" fill="#acc5cd">Available network options, not a solved switching plan · kW transport model</text>
 </svg>
</template>
