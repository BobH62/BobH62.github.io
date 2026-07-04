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
    <button
      v-for="(img, i) in images"
      :key="img"
      type="button"
      class="gallery-cell"
      @click="open = i"
    >
      <NuxtImg :src="img" :alt="captions?.[i] || ''" format="webp" />
    </button>

    <Teleport to="body">
      <div v-if="open !== null" class="lightbox" @click.self="close">
        <button class="lb-close" aria-label="Close" @click="close">&times;</button>
        <button class="lb-nav lb-prev" aria-label="Previous" @click="prev">&lsaquo;</button>
        <figure class="lb-figure" @click.stop>
          <img :src="images[open]" :alt="captions?.[open] || ''" />
          <figcaption v-if="captions?.[open]">{{ captions[open] }}</figcaption>
        </figure>
        <button class="lb-nav lb-next" aria-label="Next" @click="next">&rsaquo;</button>
      </div>
    </Teleport>
  </div>
</template>

<style scoped>
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 0.5rem;
  margin: 1.5rem 0;
}
.gallery-cell {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  padding: 0;
  background: var(--bg-elev);
  cursor: zoom-in;
  transition: transform var(--transition);
}
.gallery-cell:hover { transform: scale(1.01); }
.gallery-cell :deep(img) { width: 100%; display: block; }

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
.lb-figure figcaption { color: #d4d4d8; font-size: 0.875rem; margin-top: 0.5rem; }
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
