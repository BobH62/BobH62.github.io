<script setup lang="ts">
const interests = [
  'World Models',
  'Spatial Intelligence',
  'Robotic Perception',
  'Localization & Mapping (SLAM)',
  'Computational Design',
]

const education = [
  {
    degree: 'MPhil, Individualized Interdisciplinary Program (EMIA)',
    school: 'The Hong Kong University of Technology',
    years: '2023 – 2025',
    note: 'Academy of Interdisciplinary Studies / Cheng Kar-Shun Robotics Institute (CKSRI)',
  },
  {
    degree: 'B.Arch., Architecture',
    school: 'South China University of Technology',
    years: '2017 – 2022',
    note: 'Department of Architecture — GPA 3.83 / 4.0',
  },
]

useSeoMeta({
  title: 'Haoming Huang — Architecture · Robotics · AI',
  description:
    'MPhil (HKUST) · World-Model Algorithm Engineer at Zhuoyu (ex-DJI Automotive). Bridging architecture, robotics, and AI.',
})
</script>

<template>
  <div class="container about">
    <section class="profile">
      <NuxtImg
        src="/images/portrait.jpg"
        alt="Haoming Huang"
        class="portrait"
        width="190"
        height="190"
        format="webp"
      />
      <div class="intro">
        <h1>Haoming Huang <span class="name-cn">黄浩明</span></h1>
        <p class="tagline">
          Bridging the digital and the physical — from architecture to robotics to AI.
        </p>
        <p class="lead">
          I recently completed my MPhil at the
          <a href="https://ri.hkust.edu.hk/" target="_blank" rel="noopener">Cheng Kar-Shun Robotics Institute (CKSRI)</a>, HKUST,
          advised by Prof.
          <a href="https://seng.hkust.edu.hk/about/people/faculty/yi-kuen-lee" target="_blank" rel="noopener">Yi-Kuen Lee</a>
          and Prof.
          <a href="https://huanyin94.github.io/" target="_blank" rel="noopener">Huan Yin</a>,
          where I worked closely with
          <a href="https://qiaozhijian.github.io/" target="_blank" rel="noopener">Zhijian Qiao</a>
          from the
          <a href="https://uav.hkust.edu.hk/" target="_blank" rel="noopener">Aerial Robotics Group</a>.
          I am deeply grateful to Prof.
          <a href="https://seng.hkust.edu.hk/about/people/faculty/zexiang-li" target="_blank" rel="noopener">Zexiang Li</a>
          for his mentorship and support throughout my career.
          I am now a World-Model Algorithm Engineer at
          <a href="https://www.zyt.com/zh" target="_blank" rel="noopener">Zhuoyu</a>
          (formerly DJI Automotive), working on world models for autonomous driving.
        </p>
        <p>
          My path is deliberately cross-disciplinary. I hold a Bachelor of Architecture from
          South China University of Technology (2017–2022), where I spent four years between
          digital design, robotic fabrication, and full-scale construction — including a
          student-led solar house for the Solar Decathlon, the "Olympics" of international
          architecture student competitions. That hands-on, "design-to-physical" mindset
          carried into my robotics MPhil: cross-modal LiDAR–BIM registration, SLAM, and 3D
          perception, and now into foundation models and world models for autonomous driving.
        </p>
        <p>
          I am broadly interested in <strong>world models</strong>,
          <strong>spatial intelligence</strong>,
          <strong>robotic perception</strong>, and
          <strong>localization &amp; mapping (SLAM)</strong> — and in how ideas migrate across
          design, robotics, and AI.
        </p>
      </div>
      <aside class="contact-col">
        <h2>Contact</h2>
        <div class="contact-name">Haoming Huang</div>
        <div class="contact-line">MPhil, HKUST</div>
        <div class="contact-line">Cheng Kar-Shun Robotics Institute</div>
        <div class="contact-line">Hong Kong SAR, China</div>
        <a class="contact-mail" href="mailto:hhuangce@connect.ust.hk">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true">
            <rect x="3" y="5" width="18" height="14" rx="2" />
            <path d="m3 7 9 6 9-6" />
          </svg>
          <span>hhuangce@connect.ust.hk</span>
        </a>
      </aside>
    </section>

    <section>
      <h2>Interest</h2>
      <div class="tags">
        <span v-for="i in interests" :key="i" class="tag tag-accent">{{ i }}</span>
      </div>
    </section>

    <section>
      <h2>Education</h2>
      <ul class="edu">
        <li v-for="e in education" :key="e.degree">
          <div class="edu-row">
            <span class="edu-degree">{{ e.degree }}</span>
            <span class="edu-years">{{ e.years }}</span>
          </div>
          <div class="edu-school">{{ e.school }}</div>
          <div class="edu-note">{{ e.note }}</div>
        </li>
      </ul>
    </section>

    <section>
      <h2>Selected Honors</h2>
      <ul class="honors">
        <li>
          <strong>Overall Champion</strong>, Solar Decathlon Middle East 2021 (Dubai, Expo 2020) —
          a student-led full-size solar house, from design to construction
          (<a href="https://solarchitecture.ch/sdme-2021-team-x-house/" target="_blank" rel="noopener">link</a>)
        </li>
        <li>
          <strong>First Winner</strong>, Ice &amp; Snow Structure International Invitational Competition 2022 —
          <em>The Arctic Olympic Venues</em> with multistable grid-shell formworks
        </li>
        <li><strong>Graduation Project with Distinction</strong>, 2022, SCUT</li>
        <li>
          <strong>Runner-up</strong>, National Competition for College Students in Industrialized
          Building &amp; Intelligent Construction, 2022
          (<a href="https://civil.cqu.edu.cn/ibic/" target="_blank" rel="noopener">link</a>)
        </li>
      </ul>
    </section>

    <section>
      <h2>Community Service</h2>
      <ul>
        <li>Teaching assistant: EMIA 2020 Cross-disciplinary Design Thinking, HKUST, 2024 Autumn</li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.about { padding-top: 1rem; max-width: 72rem; }
.profile {
  display: grid;
  grid-template-columns: 190px 1fr 200px;
  gap: 3rem;
  align-items: start;
  margin-bottom: 1.5rem;
}
.portrait {
  width: 190px;
  height: 190px;
  object-fit: cover;
  border-radius: 50%;
  border: 1px solid var(--border);
  background: var(--bg-elev);
}
.intro { min-width: 0; }
.name-cn {
  font-family: var(--font-body);
  font-weight: 400;
  font-size: 1rem;
  color: var(--text-faint);
}
.tagline {
  font-family: var(--font-display);
  color: var(--text-muted);
  font-size: 1.05rem;
  margin: 0 0 1.25rem;
  line-height: 1.5;
}
.lead { font-size: 1.02rem; }

.contact-col {
  font-size: 0.9rem;
  line-height: 1.5;
}
.contact-col h2 {
  font-family: var(--font-body);
  font-size: 1rem;
  font-weight: 700;
  margin: 0 0 0.5rem;
}
.contact-name { font-weight: 600; color: var(--text); }
.contact-line { color: var(--text-muted); }
.contact-mail {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  margin-top: 0.75rem;
  color: var(--accent);
  border-bottom: 1px solid var(--border-strong);
  transition: border-color var(--transition);
}
.contact-mail:hover { border-bottom-color: var(--accent); }

.tags { display: flex; flex-wrap: wrap; }

.edu { list-style: none; padding: 0; }
.edu li { margin: 0.75rem 0; }
.edu-row {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.edu-degree { font-weight: 500; }
.edu-years { color: var(--text-faint); font-size: 0.9rem; white-space: nowrap; }
.edu-school { color: var(--text-muted); }
.edu-note { color: var(--text-faint); font-size: 0.875rem; }

.honors { padding-left: 1.25rem; }
.honors li { margin: 0.5rem 0; }

@media (max-width: 48rem) {
  .profile { grid-template-columns: 160px 1fr; }
  .contact-col { grid-column: 1 / -1; }
}
@media (max-width: 34rem) {
  .profile { grid-template-columns: 1fr; gap: 1.25rem; }
  .portrait { width: 130px; height: 130px; }
}
</style>
