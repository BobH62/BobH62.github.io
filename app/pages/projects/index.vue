<script setup lang="ts">
const { data: projects } = await useAsyncData('projects', () =>
  queryCollection('projects').order('order', 'DESC').order('date', 'DESC').all()
)

function year(date: string) {
  return date.slice(0, 4)
}

function btnLabel(label: string): string {
  const l = label.toLowerCase()
  if (/arxiv/.test(l)) return 'arXiv'
  if (/code|github|dataset/.test(l)) return 'Code'
  if (/video|youtube/.test(l)) return 'Video'
  if (/pdf|paper|iass/.test(l)) return 'Paper'
  if (/page|website|roboticplus|archi-solutions|studio/.test(l)) return 'Website'
  return label
}

useSeoMeta({
  title: 'Projects — Haoming Huang',
  description:
    'Selected projects spanning world models, LiDAR–BIM registration, SLAM datasets, solar-house construction, and bending-active gridshells.',
})
</script>

<template>
  <div class="container">
    <h1>Projects</h1>
    <p class="section-lead">
      A trajectory from full-scale architectural construction to cross-modal robot
      perception and autonomous-driving world models.
    </p>

    <div class="cards">
      <article v-for="p in projects" :key="p.path" class="card">
        <NuxtLink :to="p.path" class="card-link">
          <div class="card-media">
            <NuxtImg
              v-if="p.cardImage || p.image"
              :src="p.cardImage || p.image"
              :alt="p.title"
              format="webp"
              width="640"
              class="card-img"
            />
            <div v-else class="card-img card-placeholder">
              <span>{{ p.nda ? 'NDA' : 'project' }}</span>
            </div>
            <span v-if="p.nda" class="nda-badge">Selected Industry Work · NDA</span>
          </div>
          <div class="card-body">
            <div class="card-meta">
              <span class="card-year">{{ year(p.date) }}</span>
              <span class="card-tags">
                <span v-for="t in p.tags.slice(0, 2)" :key="t" class="tag">{{ t }}</span>
              </span>
            </div>
            <h3 class="card-title">{{ p.title }}</h3>
            <p class="card-excerpt">{{ p.summary }}</p>
          </div>
        </NuxtLink>
        <div v-if="p.links?.length" class="card-actions">
          <a
            v-for="l in p.links"
            :key="l.url"
            :href="l.url"
            target="_blank"
            rel="noopener"
            class="card-btn"
            @click.stop
          >{{ btnLabel(l.label) }}</a>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
.section-lead { color: var(--text-muted); margin-top: -0.5rem; }
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  gap: 1.5rem;
  margin-top: 1.75rem;
}
.card {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--bg-elev);
  overflow: hidden;
  color: inherit;
  transition: border-color var(--transition), transform var(--transition);
}
.card:hover { border-color: var(--accent); transform: translateY(-2px); }
.card-link { display: flex; flex-direction: column; color: inherit; }
.card-media { position: relative; aspect-ratio: 16 / 10; overflow: hidden; background: var(--border); }
.card-img { width: 100%; height: 100%; object-fit: cover; display: block; filter: grayscale(1); transition: filter var(--transition); }
.card:hover .card-img { filter: grayscale(0); }
.card-placeholder {
  display: flex; align-items: center; justify-content: center;
  color: var(--text-faint); font-size: 0.85rem; background: var(--border);
}
.nda-badge {
  position: absolute; top: 0.5rem; left: 0.5rem;
  font-size: 0.7rem; color: var(--accent);
  background: var(--accent-soft); border-radius: 999px; padding: 0.15rem 0.5rem;
}
.card-body { padding: 0.9rem 1rem 1rem; }
.card-meta { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.4rem; }
.card-year { font-size: 0.78rem; color: var(--text-faint); font-variant-numeric: tabular-nums; }
.card-tags { display: flex; flex-wrap: wrap; gap: 0.3rem; }
.card-tags .tag { font-size: 0.68rem; padding: 0.05rem 0.5rem; }
.card-title { font-family: var(--font-body); font-size: 1.02rem; margin: 0 0 0.4rem; line-height: 1.3; }
.card-excerpt { font-size: 0.84rem; color: var(--text-muted); margin: 0; line-height: 1.5;
  display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }

.card-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding: 0 1rem 1rem;
  margin-top: auto;
}
.card-btn {
  font-size: 0.68rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 0.25rem 0.7rem;
  text-decoration: none;
  transition: color var(--transition), border-color var(--transition), background var(--transition);
}
.card-btn:hover {
  color: var(--accent);
  border-color: var(--accent);
  background: var(--accent-soft);
}
</style>
