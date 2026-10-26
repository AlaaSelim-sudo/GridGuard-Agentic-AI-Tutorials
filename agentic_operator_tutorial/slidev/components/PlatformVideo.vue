<script setup>
import { ref, onUnmounted, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
const props = defineProps({ embedUrl: String, watchUrl: String, poster: String, title: String })
const playing = ref(false)
const { $nav, $page } = useSlideContext()
watch(() => $nav.value.currentSlideNo, current => { if (current !== $page.value) playing.value = false })
onUnmounted(() => { playing.value = false })
const base = import.meta.env.BASE_URL
</script>
<template>
  <div class="platform-video">
    <div class="player">
      <iframe v-if="playing" :src="embedUrl" :title="title" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin" />
      <button v-else type="button" @click="playing = true" :aria-label="`Play ${title}`">
        <img :src="base + 'images/' + poster" :alt="title + ' — official video thumbnail'" />
        <span class="play">▶ Play official video</span>
      </button>
    </div>
    <a :href="watchUrl" target="_blank" rel="noopener">Open official video in a new tab ↗</a>
  </div>
</template>
<style scoped>
.player{height:370px;background:#003b5c;position:relative;max-width:850px;margin:0 auto}
button,iframe{border:0;width:100%;height:100%;display:block;padding:0;background:#003b5c;cursor:pointer}
button img{height:100%;width:100%;object-fit:contain;display:block}
.play{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);padding:10px 24px;background:#00629b;color:white;font:bold 24px 'Latin Modern Roman',serif;white-space:nowrap;border:2px solid white}
button:focus-visible{outline:4px solid #00a6b2;outline-offset:4px}
a{display:block;text-align:center;font-size:18px;color:#00629b;margin-top:8px;text-decoration:underline}
</style>
