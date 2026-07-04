<script setup lang="ts">
const trajectory = [
  { year: '2017', label: 'B.Arch, SCUT', desc: 'Architecture — digital design & robotic fabrication', to: '' },
  { year: '2021', label: 'Point-Cloud Registration', desc: 'First bridge from architecture into robotics', to: '/projects/pc-registration' },
  { year: '2021', label: 'Solar Decathlon ME', desc: 'Overall Champion — full-size solar house, Dubai', to: '/projects/sdme' },
  { year: '2022', label: 'Gridshell Research', desc: 'Active-bending & multistable formworks — Ice & Snow First Winner', to: '/projects/gridshell' },
  { year: '2023', label: 'MPhil, HKUST', desc: 'Cross-modal LiDAR–BIM registration & SLAM', to: '' },
  { year: '2025', label: 'LiDAR2BIM / SLABIM', desc: 'T-ASE paper & ICRA dataset, open-sourced', to: '/projects/lidar2bim' },
  { year: '2026', label: 'Zhuoyu World Model', desc: 'LLM / world-model engineer for autonomous driving', to: '/projects/world-model' },
]

const awards = [
  {
    title: 'Overall Champion',
    event: 'Solar Decathlon Middle East 2021',
    place: 'Dubai · Expo 2020',
    icon: '🏆',
  },
  {
    title: 'First Winner',
    event: 'Ice & Snow Structure International Invitational Competition 2022',
    place: 'The Arctic Olympic Venues',
    icon: '❄️',
  },
]

const oss = [
  {
    name: 'SLABIM',
    desc: 'A SLAM-BIM coupled dataset (164K+ LiDAR scans, 3,900+ RGB images) with benchmarks.',
    venue: 'ICRA 2025',
    url: 'https://github.com/HKUST-Aerial-Robotics/SLABIM',
  },
  {
    name: 'LiDAR2BIM-Registration',
    desc: 'Global LiDAR–BIM registration via Pose Hough Transform — cross-modal, no pose prior.',
    venue: 'IEEE T-ASE',
    url: 'https://github.com/HKUST-Aerial-Robotics/LiDAR2BIM-Registration',
  },
]

useSeoMeta({
  title: 'Highlights — Haoming Huang',
  description:
    'Awards, cross-disciplinary trajectory, and open-source releases by Haoming Huang.',
})
</script>

<template>
  <div class="container">
    <h1>Highlights</h1>

    <section class="awards">
      <div v-for="a in awards" :key="a.event" class="award">
        <div class="award-icon">{{ a.icon }}</div>
        <div class="award-text">
          <div class="award-title">{{ a.title }}</div>
          <div class="award-event">{{ a.event }}</div>
          <div class="award-place">{{ a.place }}</div>
        </div>
      </div>
    </section>

    <section>
      <h2>Trajectory — From Architecture to Robotics to AGI</h2>
      <p class="section-lead">
        A deliberately cross-disciplinary path: digital design and full-scale construction
        feeding into cross-modal robot perception, and now into world models for autonomous
        driving.
      </p>
      <ol class="timeline">
        <li v-for="(t, i) in trajectory" :key="i" class="tl-item">
          <div class="tl-dot" />
          <div class="tl-year">{{ t.year }}</div>
          <div class="tl-body">
            <component
              :is="t.to ? 'NuxtLink' : 'div'"
              :to="t.to || undefined"
              :class="t.to ? 'tl-link' : 'tl-label'"
            >
              <span class="tl-label-text">{{ t.label }}</span>
            </component>
            <div class="tl-desc">{{ t.desc }}</div>
          </div>
        </li>
      </ol>
    </section>

    <section>
      <h2>Open-source releases</h2>
      <ul class="oss-list">
        <li v-for="o in oss" :key="o.name" class="oss-item">
          <a :href="o.url" target="_blank" rel="noopener" class="oss-name link-underline">{{ o.name }}</a>
          <span class="oss-venue">{{ o.venue }}</span>
          <p class="oss-desc">{{ o.desc }}</p>
        </li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.section-lead { color: var(--text-muted); margin-top: -0.5rem; }

.awards { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin: 1.25rem 0 0.5rem; }
.award { display: flex; gap: 0.85rem; align-items: flex-start; border: 1px solid var(--border); border-radius: var(--radius); padding: 1rem 1.1rem; background: var(--bg-elev); }
.award-icon { font-size: 1.5rem; line-height: 1; }
.award-title { font-weight: 700; color: var(--accent); }
.award-event { font-size: 0.92rem; }
.award-place { font-size: 0.82rem; color: var(--text-faint); }

.timeline { list-style: none; padding: 0; margin: 1.25rem 0 0; position: relative; }
.timeline::before {
  content: ''; position: absolute; left: 4.5rem; top: 0.4rem; bottom: 0.4rem; width: 1px; background: var(--border);
}
.tl-item { display: grid; grid-template-columns: 4rem 1fr; gap: 1rem; padding: 0.6rem 0; position: relative; align-items: baseline; }
.tl-year { font-variant-numeric: tabular-nums; color: var(--text-faint); font-size: 0.85rem; text-align: right; }
.tl-dot { position: absolute; left: 4.4rem; top: 1rem; width: 9px; height: 9px; border-radius: 50%; background: var(--accent); border: 2px solid var(--bg); }
.tl-label-text { font-weight: 600; }
.tl-link .tl-label-text { color: var(--text); border-bottom: 1px solid var(--border-strong); }
.tl-link:hover .tl-label-text { color: var(--accent); border-bottom-color: var(--accent); }
.tl-desc { font-size: 0.85rem; color: var(--text-muted); margin-top: 0.1rem; }

.oss-list { list-style: none; padding: 0; margin: 1rem 0 0; }
.oss-item { padding: 0.85rem 0; border-top: 1px solid var(--border); }
.oss-item:last-child { border-bottom: 1px solid var(--border); }
.oss-name { font-weight: 600; }
.oss-venue { margin-left: 0.6rem; font-size: 0.75rem; color: var(--text-faint); border: 1px solid var(--border); border-radius: 999px; padding: 0.05rem 0.5rem; }
.oss-desc { margin: 0.3rem 0 0; color: var(--text-muted); font-size: 0.9rem; }

@media (max-width: 32rem) {
  .timeline::before { left: 0.5rem; }
  .tl-item { grid-template-columns: 1fr; gap: 0.1rem; padding-left: 1.4rem; }
  .tl-year { text-align: left; font-size: 0.78rem; }
  .tl-dot { left: 0.05rem; top: 0.5rem; }
}
</style>
