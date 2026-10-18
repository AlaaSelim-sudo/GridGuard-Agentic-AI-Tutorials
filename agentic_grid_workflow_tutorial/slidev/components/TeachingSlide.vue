<script setup>
import { computed } from 'vue'
import katex from 'katex'
import hljs from 'highlight.js/lib/core'
import python from 'highlight.js/lib/languages/python'
import lessons from '../content/lessons.json'
hljs.registerLanguage('python', python)
const props=defineProps({ index:Number, step:Number, complete:Boolean })
const s=computed(()=>lessons[props.index])
const reveal=computed(()=>props.complete ? 99 : props.step||0)
const asset=p=>`${import.meta.env.BASE_URL}${String(p).replace(/^\//,'')}`
const equation=computed(()=>s.value.equation ? katex.renderToString(s.value.equation,{displayMode:true,throwOnError:false,strict:false}) : '')
const symbol=x=>katex.renderToString(x,{throwOnError:false,strict:false})
const lines=computed(()=>s.value.code_text?.split('\n')||[])
const syntax=x=>hljs.highlight(x,{language:'python'}).value || '&nbsp;'
const show=(at)=>reveal.value>=at
const isFlow=computed(()=>s.value.kind==='flow'||s.value.nodes&&s.value.visual&&['dag','cycle','reactloop','route','roles','claims','state','checkpoint','stages','tools','control'].includes(s.value.visual))
const table=computed(()=>s.value.rows && (s.value.columns||s.value.headers))
</script>
<template>
 <article :class="['lesson','kind-'+s.kind,{'has-code':s.code_text,'has-image':s.image,'has-flow':isFlow,'is-dark':['cover','divider','question','lab'].includes(s.kind)}]" :data-lesson="s.id" :data-step="reveal">
  <header>
   <div class="eyebrow">{{ s.section }}<span v-if="s.code"> / {{ s.code.cell }}</span></div>
   <h1>{{ s.title }}</h1>
   <p v-if="s.kicker" class="kicker">{{ s.kicker }}</p>
  </header>
  <main :class="{'split':s.code_text || s.image}">
   <template v-if="s.code_text">
    <div class="code-pane">
     <div class="code-caption">{{ s.code.notebook }} · {{ s.code.cell }} · lines {{ s.code.start }}–{{ s.code.end }}</div>
     <pre :style="{fontSize:lines.length<=4?'17px':lines.length<=8?'15px':'13px'}"><code><span v-for="(line,i) in lines" :key="i" :class="['code-line',{focus:complete||reveal===0||reveal>=s.clicks||Math.floor(i/(lines.length/3))+1===Math.min(3,reveal)}]"><span class="line-no">{{ s.code.start+i }}</span><span v-html="syntax(line)" /></span></code></pre>
    </div>
    <div class="side-explanation">
     <p v-for="(item,i) in s.items" :key="i" :class="['reveal statement',{shown:show(i+1)}]"><span class="small-number">{{ i+1 }}</span>{{ item }}</p>
     <p v-if="s.prompt" class="prompt">{{ s.prompt }}</p>
     <p v-if="s.answer" :class="['answer','reveal',{shown:show(3)}]">{{ s.answer }}</p>
     <table v-if="table" :class="['comparison compact-table','reveal',{shown:show(3)}]"><thead><tr><th v-for="c in (s.columns||s.headers)" :key="String(c)">{{ c }}</th></tr></thead><tbody><tr v-for="(row,i) in s.rows" :key="i"><td v-for="(v,j) in row" :key="j">{{ v }}</td></tr></tbody></table>
    </div>
   </template>
   <template v-else-if="s.image">
    <figure><img :src="asset(s.image)" :alt="s.image_alt||s.title" /><figcaption v-if="s.image_caption">{{ s.image_caption }}</figcaption></figure>
    <div class="side-explanation"><p v-for="(item,i) in s.items" :key="i" :class="['reveal statement',{shown:show(i+1)}]">{{ item }}</p><p v-if="s.prompt" class="prompt">{{ s.prompt }}</p><p v-if="s.answer" :class="['answer','reveal',{shown:show(3)}]">{{ s.answer }}</p></div>
   </template>
   <template v-else-if="s.kind==='question'">
    <p class="question-prompt">{{ s.prompt || s.items?.[0] || s.takeaway }}</p>
    <div v-if="equation" class="equation compact" v-html="equation" />
    <div v-if="s.symbols" class="symbols question-symbols"><div v-for="(x,i) in s.symbols" :key="i" :class="['symbol','reveal',{shown:show(1)}]"><b v-html="symbol(x.symbol)"/><span>{{ x.meaning }}</span></div></div>
    <div :class="['answer-big','reveal',{shown:show(1)}]">{{ s.answer || s.items?.slice(1).join(' ') }}</div>
    <p v-for="(item,i) in s.items?.slice(s.prompt?0:1)" :key="i" :class="['reveal quiet-item',{shown:show(Math.min(3,i+2))}]">{{ item }}</p>
   </template>
   <template v-else-if="s.bars">
    <div class="bars"><div v-for="(bar,i) in s.bars" :key="i" class="bar-row"><span>{{ bar.label }}</span><div class="bar-track"><div class="bar-fill" :style="{width:show(i+1)?`${bar.value/35*100}%`:'0%'}" /></div><strong :class="['reveal',{shown:show(i+1)}]">{{ bar.value.toFixed(3) }} s</strong></div><p class="bar-axis">0<span>Elapsed seconds</span>35</p></div>
    <div class="flow-captions"><p v-for="(item,i) in s.items?.slice(-2)" :key="i" :class="['reveal',{shown:show(3)}]">{{ item }}</p></div>
   </template>
   <template v-else-if="equation && !isFlow || s.kind==='equation'">
    <div class="equation" v-html="equation" />
    <div class="symbols"><div v-for="(x,i) in s.symbols" :key="i" :class="['symbol','reveal',{shown:show(1)}]"><b v-html="symbol(x.symbol)"/><span>{{ x.meaning }}</span></div></div>
    <div class="equation-explain"><p v-for="(item,i) in s.items" :key="i" :class="['reveal',{shown:show(Math.min(3,i+2))}]">{{ item }}</p></div>
   </template>
   <template v-else-if="table">
    <table class="comparison"><thead><tr><th v-for="c in (s.columns||s.headers)" :key="String(c)">{{ c }}</th></tr></thead><tbody><tr v-for="(row,i) in s.rows" :key="i" :class="['reveal',{shown:show(Math.min(3,i+1))}]"><td v-for="(v,j) in (Array.isArray(row)?row:Object.values(row))" :key="j" :class="{'tick':String(v).includes('✓')}">{{ v }}</td></tr></tbody></table>
    <p v-if="s.prompt" class="prompt table-prompt">{{ s.prompt }}</p>
    <p v-if="s.answer" :class="['answer table-answer','reveal',{shown:show(3)}]">{{ s.answer }}</p>
    <template v-else><p class="table-key" v-for="(item,i) in s.items" :key="i">{{ item }}</p></template>
   </template>
   <template v-else-if="s.visual==='restoration' && s.id==='R01'">
    <RestorationViz :step="reveal" :complete="complete" />
    <div class="flow-captions"><p v-for="(item,i) in s.items" :key="i" :class="['reveal',{shown:show(i+1)}]">{{ item }}</p></div>
   </template>
   <template v-else-if="isFlow">
    <FlowViz :kind="s.visual" :nodes="s.nodes" :step="reveal" :complete="complete" />
    <div v-if="equation" class="equation compact" v-html="equation" />
    <div v-if="s.symbols" class="symbols flow-symbols"><div v-for="(x,i) in s.symbols" :key="i" :class="['symbol','reveal',{shown:show(1)}]"><b v-html="symbol(x.symbol)"/><span>{{ x.meaning }}</span></div></div>
    <div class="flow-captions"><p v-for="(item,i) in s.items" :key="i" :class="['reveal',{shown:show(i+1)}]">{{ item }}</p></div>
   </template>
   <template v-else-if="s.symbols">
    <div class="symbol-lesson"><div v-for="(x,i) in s.symbols" :key="i" :class="['reveal',{shown:show(i+1)}]"><b v-html="symbol(x.symbol)"/><p>{{ x.meaning }}</p></div></div>
    <div class="flow-captions"><p v-for="(item,i) in s.items" :key="i" :class="['reveal',{shown:show(Math.min(3,i+1))}]">{{ item }}</p></div>
   </template>
   <template v-else>
    <div class="concept-list"><div v-for="(item,i) in s.items" :key="i" :class="['concept-item','reveal',{shown:show(i+1)}]"><span class="concept-number">{{ String(i+1).padStart(2,'0') }}</span><p>{{ item }}</p></div></div>
    <p v-if="s.prompt" class="prompt">{{ s.prompt }}</p>
    <p v-if="s.answer" :class="['answer','reveal',{shown:show(3)}]">{{ s.answer }}</p>
   </template>
  </main>
  <div :class="['takeaway','reveal',{shown:show(3)}]">{{ s.takeaway }}</div>
  <footer><div class="references"><a v-for="(r,i) in s.refs" :key="i" :href="r.url" target="_blank" rel="noopener">{{ r.label }}</a></div><div class="foot-bottom"><span>{{ s.next ? `Next: ${s.next}` : 'Workshop complete' }}</span><span>{{ index+1 }} / {{ lessons.length }}</span></div></footer>
 </article>
</template>
