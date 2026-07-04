<script setup lang="ts">
const route = useRoute()
const { data: project } = await useAsyncData(`project-${route.path}`, () =>
  queryCollection('projects').path(route.path).first()
)

if (!project.value) {
  throw createError({ statusCode: 404, statusMessage: 'Project not found', fatal: true })
}

useSeoMeta({
  title: () => `${project.value?.title} — Haoming Huang`,
  description: () => project.value?.excerpt || '',
})

function year(date: string) {
  return date.slice(0, 4)
}
</script>

<template>
  <div v-if="project" class="container project">
    <NuxtLink to="/projects" class="back link-underline">&larr; All projects</NuxtLink>

    <header class="project-head">
      <div class="project-head-text">
        <div class="project-meta">
          <span class="card-year">{{ year(project.date) }}</span>
          <span v-for="t in project.tags" :key="t" class="tag">{{ t }}</span>
          <span v-if="project.nda" class="tag tag-accent">NDA</span>
        </div>
        <h1>{{ project.title }}</h1>
        <p class="excerpt">{{ project.excerpt }}</p>
        <dl class="meta-grid">
          <div v-if="project.role"><dt>Role</dt><dd>{{ project.role }}</dd></div>
          <div v-if="project.stack?.length"><dt>Stack</dt><dd>{{ project.stack.join(', ') }}</dd></div>
          <div v-if="project.links?.length"><dt>Links</dt>
            <dd>
              <a v-for="l in project.links" :key="l.label" :href="l.url" target="_blank" rel="noopener" class="link-underline">{{ l.label }}</a>
            </dd>
          </div>
        </dl>
      </div>
      <div v-if="project.image" class="project-hero">
        <NuxtImg :src="project.image" :alt="project.title" format="webp" width="900" />
      </div>
    </header>

    <article class="project-body">
      <ContentRenderer :value="project" />
    </article>

    <nav class="project-foot">
      <NuxtLink to="/projects">&larr; Back to projects</NuxtLink>
    </nav>
  </div>
</template>

<style scoped>
.back { font-size: 0.85rem; color: var(--text-muted); }
.project { padding-top: 1rem; }
.project-head {
  display: grid;
  grid-template-columns: 1fr 1.4fr;
  gap: 2rem;
  align-items: start;
  margin: 1.25rem 0 1.5rem;
}
.project-meta { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4rem; margin-bottom: 0.5rem; }
.card-year { font-size: 0.8rem; color: var(--text-faint); }
.excerpt { color: var(--text-muted); margin-top: 0; }
.meta-grid { margin: 1rem 0 0; }
.meta-grid > div { display: grid; grid-template-columns: 5rem 1fr; gap: 0.5rem; margin: 0.35rem 0; font-size: 0.9rem; }
.meta-grid dt { color: var(--text-faint); margin: 0; }
.meta-grid dd { margin: 0; color: var(--text); }
.meta-grid dd a { margin-right: 0.75rem; }

.project-hero :deep(img) {
  width: 100%; border: 1px solid var(--border); border-radius: var(--radius); display: block;
}

.project-body { line-height: 1.7; }
.project-body :deep(h2) { margin-top: 2rem; }
.project-body :deep(ul) { padding-left: 1.25rem; }
.project-body :deep(img) { border-radius: var(--radius); border: 1px solid var(--border); }

.project-foot { margin-top: 2.5rem; padding-top: 1.25rem; border-top: 1px solid var(--border); font-size: 0.9rem; }

@media (max-width: 40rem) {
  .project-head { grid-template-columns: 1fr; }
}
</style>
