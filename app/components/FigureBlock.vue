<script setup lang="ts">
const props = defineProps<{
  src: string
  caption?: string
  n?: string | number
  maxw?: string
}>()

const open = ref(false)

function onKey(e: KeyboardEvent) {
  if (open.value && e.key === 'Escape') open.value = false
}
onMounted(() => window.addEventListener('keydown', onKey))
onBeforeUnmount(() => window.removeEventListener('keydown', onKey))
</script>

<template>
  <figure class="fig" :style="maxw ? `max-width: ${maxw}; margin-left:auto; margin-right:auto;` : ''">
    <button type="button" class="fig-btn" @click="open = true">
      <NuxtImg :src="src" :alt="caption || ''" format="webp" />
    </button>
    <figcaption>
      <span v-if="n !== undefined" class="figno">Fig. {{ n }}</span>
      <span v-if="caption" class="figcap">{{ caption }}</span>
    </figcaption>

    <Teleport to="body">
      <div v-if="open" class="lightbox" @click.self="open = false">
        <button class="lb-close" aria-label="Close" @click="open = false">&times;</button>
        <figure class="lb-figure" @click.stop>
          <img :src="src" :alt="caption || ''" />
          <figcaption v-if="caption">
            <span v-if="n !== undefined" class="figno">Fig. {{ n }}</span>
            <span>{{ caption }}</span>
          </figcaption>
        </figure>
      </div>
    </Teleport>
  </figure>
</template>

<style scoped>
.fig { margin: 1.75rem 0; }
.fig-btn {
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
.fig-btn:hover { border-color: var(--border-strong); }
.fig-btn :deep(img) { width: 100%; height: auto; display: block; }

figcaption {
  margin-top: 0.6rem;
  font-size: 0.85rem;
  line-height: 1.55;
  color: var(--text-faint);
  max-width: 52rem;
}
.figno {
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.04em;
  color: var(--text-muted);
  margin-right: 0.5rem;
}
.figcap { color: var(--text-faint); }

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
.lb-close {
  position: absolute;
  top: 1rem;
  right: 1.5rem;
  background: transparent;
  border: 0;
  color: #fff;
  font-size: 2rem;
  cursor: pointer;
  line-height: 1;
  opacity: 0.7;
}
.lb-close:hover { opacity: 1; }
</style>
