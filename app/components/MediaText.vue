<script setup lang="ts">
const props = defineProps<{
  src: string
  caption?: string
  n?: string | number
  side?: 'left' | 'right'
  mediaWidth?: string
}>()

const open = ref(false)
const side = props.side ?? 'left'
const mediaWidth = props.mediaWidth ?? '26rem'

function onKey(e: KeyboardEvent) {
  if (open.value && e.key === 'Escape') open.value = false
}
onMounted(() => window.addEventListener('keydown', onKey))
onBeforeUnmount(() => window.removeEventListener('keydown', onKey))
</script>

<template>
  <div class="mt" :class="side">
    <figure class="mt-media">
      <button type="button" class="mt-btn" @click="open = true">
        <NuxtImg :src="src" :alt="caption || ''" format="webp" />
      </button>
      <figcaption>
        <span v-if="n !== undefined" class="figno">Fig. {{ n }}</span>
        <span v-if="caption" class="figcap">{{ caption }}</span>
      </figcaption>
    </figure>
    <div class="mt-text">
      <slot />
    </div>

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
  </div>
</template>

<style scoped>
.mt {
  display: grid;
  grid-template-columns: v-bind(mediaWidth) 1fr;
  gap: 2rem;
  align-items: start;
  margin: 1.75rem 0;
}
.mt.right { grid-template-columns: 1fr v-bind(mediaWidth); }
.mt.right .mt-media { order: 2; }
.mt.right .mt-text { order: 1; }

.mt-media { margin: 0; }
.mt-btn {
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
.mt-btn:hover { border-color: var(--border-strong); }
.mt-btn :deep(img) { width: 100%; height: auto; display: block; }

.mt-media figcaption {
  margin-top: 0.6rem;
  font-size: 0.85rem;
  line-height: 1.55;
  color: var(--text-faint);
}
.figno {
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.04em;
  color: var(--text-muted);
  margin-right: 0.5rem;
}
.figcap { color: var(--text-faint); }

.mt-text { line-height: 1.7; }
.mt-text :deep(p:first-child) { margin-top: 0; }
.mt-text :deep(p:last-child) { margin-bottom: 0; }

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

@media (max-width: 44rem) {
  .mt, .mt.right {
    grid-template-columns: 1fr;
  }
  .mt.right .mt-media,
  .mt.right .mt-text { order: initial; }
  .mt-media { max-width: 24rem; margin: 0 auto; }
}
</style>
