<script setup lang="ts">
const { data: pubs } = await useAsyncData('publications', () =>
  queryCollection('publications').order('order', 'ASC').all()
)

function splitAuthors(authors: string) {
  return authors.split(',').map((a) => a.trim()).filter(Boolean)
}
function isSelf(name: string) {
  return name.includes('Haoming Huang')
}

useSeoMeta({
  title: 'Publications — Haoming Huang',
  description: 'Selected publications, posters, and workshop summaries by Haoming Huang.',
})
</script>

<template>
  <div class="container">
    <h1>Publications</h1>
    <p class="section-lead">
      Selected work on cross-modal LiDAR–BIM registration, SLAM-BIM datasets, and
      bending-active gridshells.
    </p>

    <ul class="pub-list">
      <li v-for="p in pubs" :key="p.order" class="pub-item">
        <NuxtImg
          v-if="p.image"
          :src="p.image"
          :alt="p.title"
          class="pub-thumb"
          width="220"
          format="webp"
        />
        <div class="pub-body">
          <div class="pub-type">{{ p.type === 'workshop' ? 'Workshop / Poster' : 'Paper' }}</div>
          <h3 class="pub-title">{{ p.title }}</h3>
          <div class="pub-authors">
            <template v-for="(a, i) in splitAuthors(p.authors)" :key="i">
              <span v-if="i > 0">, </span>
              <strong v-if="isSelf(a)">{{ a }}</strong>
              <span v-else>{{ a }}</span>
            </template>
          </div>
          <div class="pub-venue"><em>{{ p.venue }}</em></div>
          <div v-if="p.links?.length" class="pub-links">
            <a
              v-for="l in p.links"
              :key="l.label"
              :href="l.url"
              :target="l.url.startsWith('http') ? '_blank' : undefined"
              rel="noopener"
              class="link-underline"
            >{{ l.label }}</a>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.section-lead { color: var(--text-muted); margin-top: -0.5rem; }
.pub-list { list-style: none; padding: 0; margin: 1.5rem 0 0; }
.pub-item {
  display: flex;
  gap: 1.5rem;
  padding: 1.5rem 0;
  border-top: 1px solid var(--border);
  align-items: flex-start;
}
.pub-item:last-child { border-bottom: 1px solid var(--border); }
.pub-thumb {
  flex: 0 0 220px;
  width: 220px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--bg-elev);
}
.pub-body { flex: 1; min-width: 0; }
.pub-type {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-faint);
  margin-bottom: 0.25rem;
}
.pub-title { font-family: var(--font-body); font-size: 1.05rem; margin: 0 0 0.4rem; line-height: 1.35; }
.pub-authors { font-size: 0.92rem; color: var(--text); }
.pub-venue { font-size: 0.9rem; color: var(--text-muted); margin-top: 0.25rem; }
.pub-links { margin-top: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.85rem; font-size: 0.9rem; }
.pub-links a { border-bottom: 1px solid var(--border-strong); }

@media (max-width: 34rem) {
  .pub-item { flex-direction: column; gap: 0.85rem; }
  .pub-thumb { width: 100%; flex-basis: auto; }
}
</style>
