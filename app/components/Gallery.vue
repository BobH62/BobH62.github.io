<script setup lang="ts">
const props = defineProps<{
  images: string[]
  captions?: string[]
}>()

const open = ref<number | null>(null)

function close() {
  open.value = null
}
function prev() {
  if (open.value === null) return
  open.value = (open.value - 1 + props.images.length) % props.images.length
}
function next() {
  if (open.value === null) return
  open.value = (open.value + 1) % props.images.length
}

function onKey(e: KeyboardEvent) {
  if (open.value === null) return
  if (e.key === 'Escape') close()
  if (e.key === 'ArrowLeft') prev()
  if (e.key === 'ArrowRight') next()
}
onMounted(() => window.addEventListener('keydown', onKey))
onBeforeUnmount(() => window.removeEventListener('keydown', onKey))
</script>

<template>
  <div class="gallery">
    <figure v-for="(img, i) in images" :key="img" class="gfig">
      <button type="button" class="gfig-btn" @click="open = i">
        <NuxtImg :src="img" :alt="captions?.[i] || ''" format="webp" />
      </button>
      <figcaption>
        <span class="figno">Fig. {{ i + 1 }}</span>
        <span v-if="captions?.[i]" class="figcap">{{ captions[i] }}</span>
      </figcaption>
    </figure>

    <Teleport to="body">
      <div v-if="open !== null" class="lightbox" @click.self="close">
        <button class="lb-close" aria-label="Close" @click="close">&times;</button>
        <button class="lb-nav lb-prev" aria-label="Previous" @click="prev">&lsaquo;</button>
        <figure class="lb-figure" @click.stop>
          <img :src="images[open]" :alt="captions?.[open] || ''" />
          <figcaption v-if="captions?.[open]">
            <span class="figno">Fig. {{ open + 1 }}</span>
            <span>{{ captions[open] }}</span>
          </figcaption>
        </figure>
        <button class="lb-nav lb-next" aria-label="Next" @click="next">&rsaquo;</button>
      </div>
    </Teleport>
  </div>
</template>

<style scoped>
.gallery {
  column-count: 2;
  column-gap: 1rem;
  margin: 2.5rem 0;
}
.gfig {
  margin: 0 0 1rem;
  break-inside: avoid;
  page-break-inside: avoid;
}
.gfig-btn {
  display: block;
  width: 100%;
  padding: 0;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--bg-elev);
  cursor: zoom-in;
  transition: border-color var(--transition);
}
.gfig-btn:hover { border-color: var(--border-strong); }
.gfig-btn :deep(img) { width: 100%; height: auto; display: block; }

figcaption {
  margin-top: 0.6rem;
  font-size: 0.82rem;
  line-height: 1.5;
  color: var(--text-faint);
}
.figno {
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.04em;
  color: var(--text-muted);
  margin-right: 0.4rem;
}
.figcap { color: var(--text-faint); }

@media (max-width: 40rem) {
  .gallery { column-count: 1; }
}

.lightbox {
  position: fixed;
  inset: 0;
  z-index: 100;
  background: rgba(0,0,0,0.88);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
.lb-figure { margin: 0; max-width: 90vw; max-height: 88vh; text-align: center; }
.lb-figure img { max-width: 90vw; max-height: 80vh; object-fit: contain; }
.lb-figure figcaption { color: #d4d4d8; font-size: 0.875rem; margin-top: 0.75rem; }
.lb-figure figcaption .figno { color: #fafafa; }
.lb-close, .lb-nav {
  position: absolute;
  background: transparent;
  border: 0;
  color: #fff;
  font-size: 2rem;
  cursor: pointer;
  line-height: 1;
  opacity: 0.7;
}
.lb-close:hover, .lb-nav:hover { opacity: 1; }
.lb-close { top: 1rem; right: 1.5rem; }
.lb-nav { top: 50%; transform: translateY(-50%); }
.lb-prev { left: 1rem; }
.lb-next { right: 1rem; }
</style>
