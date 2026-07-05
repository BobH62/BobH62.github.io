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

const adlImages = [
  '/images/adl/adl-page-01.jpg',
  '/images/adl/adl-page-02.jpg',
  '/images/adl/adl-page-03.jpg',
  '/images/adl/adl-page-04.jpg',
  '/images/adl/adl-page-05.jpg',
  '/images/adl/adl-page-06.jpg',
  '/images/adl/adl-page-07.jpg',
  '/images/adl/adl-page-09.jpg',
  '/images/adl/adl-page-10.jpg',
  '/images/adl/adl-page-11.jpg',
  '/images/adl/adl-page-12.jpg',
  '/images/adl/adl-page-13.jpg',
  '/images/adl/adl-shell-series.jpg',
]

const adlCaptions = [
  'SCUT Arch. Digital Lab — title slide',
  'Timeline 2017–2021 and faculty across architecture, civil engineering, and applied mathematics',
  'Our interests — project thumbnails',
  'Our interests — Interaction Design, Digital Fabrication, Urban Design',
  'Exhibitions, lecture series and workshops',
  'Lab activities',
  'Selected works on digital fabrication, 2017–2022',
  'Project 2017 — Foam Shell (instructed by Guanqiu Zhong, Gang Song)',
  'Foam Shell — process and prototype',
  'Project 2019 — Concrete Shell (Bowen Miao et al., instructed by Lu Xiong)',
  'Concrete Shell — fabrication',
  'Concrete Shell — full-scale prototype',
  'Shell series — from digital form-finding and robotic fabrication to full-scale prototypes',
]

useSeoMeta({
  title: 'Haoming Huang — Architecture · Robotics · AI',
  description:
    'MPhil (HKUST) · World Model Algorithm Engineer at Zhuoyu (ex-DJI Automotive). Bridging architecture, robotics, and AI.',
})

const adlOpen = ref<number | null>(null)
function adlClose() { adlOpen.value = null }
function adlPrev() {
  if (adlOpen.value === null) return
  adlOpen.value = (adlOpen.value - 1 + adlImages.length) % adlImages.length
}
function adlNext() {
  if (adlOpen.value === null) return
  adlOpen.value = (adlOpen.value + 1) % adlImages.length
}
function adlKey(e: KeyboardEvent) {
  if (adlOpen.value === null) return
  if (e.key === 'Escape') adlClose()
  if (e.key === 'ArrowLeft') adlPrev()
  if (e.key === 'ArrowRight') adlNext()
}
onMounted(() => window.addEventListener('keydown', adlKey))
onBeforeUnmount(() => window.removeEventListener('keydown', adlKey))
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
        <p class="tagline tagline-cn">
          Verum, sine mendacio, certum et verissimum:<br />
          Quod est inferius est sicut quod est superius, et quod est superius est sicut quod est inferius, ad perpetranda miracula rei unius.
        </p>
        <p class="tagline-attr">— Tabula Smaragdina</p>
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
          I am now a World Model Algorithm Engineer at
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
      <h2>Leadership &amp; Community</h2>
      <div class="adl">
        <div class="adl-meta">
          <div class="adl-title">SCUT Architectural Digital Lab (ADL)</div>
          <div class="adl-role">Member → Rotating Chair · 2017–2022</div>
        </div>
        <p class="adl-desc">
          I joined SCUT's Architectural Digital Lab in its early days and grew from an
          ordinary member into a rotating chair, helping build and run a cross-disciplinary
          student community spanning <strong>digital fabrication</strong>,
          <strong>interaction design</strong>, and <strong>urban design</strong>. I
          co-organized workshops, lecture series, and exhibitions, and contributed to
          research outputs including the
          <NuxtLink to="/projects/gridshell">cable-driven grid shell</NuxtLink>
          (IASS 2022).
        </p>
        <p class="adl-desc">
          The lab also brought me together with many inspiring peers — for instance,
          Xiaofan Gao, now an AI chip engineer at Huawei;
          <a href="https://uk.linkedin.com/in/bowen-miao-7a0376158" target="_blank" rel="noopener">Bowen Miao</a>,
          now an architect at
          <a href="https://www.zha.com/" target="_blank" rel="noopener">ZHA</a>
          (Zaha Hadid Architects;
          <a href="https://pr2021.aaschool.ac.uk/students/bowen-miao" target="_blank" rel="noopener">selected works</a>),
          <a href="https://cn.linkedin.com/in/songlun-he-92b964166" target="_blank" rel="noopener">Songlun He</a>,
          now an urban design researcher, and
          <a href="https://ca.linkedin.com/in/maria-razzhivina" target="_blank" rel="noopener">Maria Razzhivina</a>,
          now an ML engineer.
        </p>
        <div class="adl-scroll">
          <figure v-for="(img, i) in adlImages" :key="img" class="adl-card">
            <button type="button" class="adl-btn" @click="adlOpen = i" :aria-label="`Open Fig. ${i + 1}`">
              <NuxtImg :src="img" :alt="adlCaptions[i]" width="560" height="315" format="webp" />
            </button>
            <figcaption>
              <span class="figno">Fig. {{ i + 1 }}</span>{{ adlCaptions[i] }}
            </figcaption>
          </figure>
        </div>
      </div>
      <ul class="community-other">
        <li>Teaching assistant: EMIA 2020 Cross-disciplinary Design Thinking, HKUST, 2024 Autumn</li>
      </ul>
    </section>

    <Teleport to="body">
      <div v-if="adlOpen !== null" class="adl-lightbox" @click.self="adlClose">
        <button class="adl-lb-close" aria-label="Close" @click="adlClose">&times;</button>
        <button class="adl-lb-nav adl-lb-prev" aria-label="Previous" @click="adlPrev">&lsaquo;</button>
        <figure class="adl-lb-figure" @click.stop>
          <img :src="adlImages[adlOpen]" :alt="adlCaptions[adlOpen]" />
          <figcaption>
            <span class="figno">Fig. {{ adlOpen + 1 }}</span>{{ adlCaptions[adlOpen] }}
          </figcaption>
        </figure>
        <button class="adl-lb-nav adl-lb-next" aria-label="Next" @click="adlNext">&rsaquo;</button>
      </div>
    </Teleport>
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
.tagline-cn {
  font-style: italic;
  font-size: 0.82rem;
  color: var(--text-faint);
  letter-spacing: 0.04em;
}
.tagline-attr {
  font-size: 0.7rem;
  color: var(--text-faint);
  opacity: 0.7;
  margin: -0.5rem 0 1.25rem;
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

.adl { margin: 1rem 0; }
.adl-meta {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 0.5rem;
}
.adl-title { font-weight: 600; }
.adl-role { color: var(--text-faint); font-size: 0.9rem; white-space: nowrap; }
.adl-desc { max-width: 52rem; }
.adl-scroll {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  overflow-y: hidden;
  scroll-snap-type: x mandatory;
  margin: 1.25rem 0 0;
  padding: 0.25rem 0 1.25rem;
  -webkit-overflow-scrolling: touch;
}
.adl-card {
  flex: 0 0 auto;
  width: 30rem;
  margin: 0;
  scroll-snap-align: start;
}
.adl-btn {
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
.adl-btn:hover { border-color: var(--border-strong); }
.adl-btn :deep(img) { width: 100%; height: auto; display: block; }
.adl-card figcaption {
  font-size: 0.8rem;
  color: var(--text-faint);
  margin-top: 0.4rem;
  line-height: 1.45;
}
.figno {
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.04em;
  color: var(--text-muted);
  margin-right: 0.4rem;
}
.adl-scroll::-webkit-scrollbar { height: 8px; }
.adl-scroll::-webkit-scrollbar-track { background: transparent; }
.adl-scroll::-webkit-scrollbar-thumb {
  background: var(--border-strong);
  border-radius: 999px;
}
.adl-scroll::-webkit-scrollbar-thumb:hover { background: var(--text-faint); }
.community-other { padding-left: 1.25rem; margin-top: 1rem; }

.adl-lightbox {
  position: fixed;
  inset: 0;
  z-index: 100;
  background: rgba(0, 0, 0, 0.88);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
.adl-lb-figure { margin: 0; max-width: 90vw; max-height: 88vh; text-align: center; }
.adl-lb-figure img { max-width: 90vw; max-height: 80vh; object-fit: contain; display: block; margin: 0 auto; }
.adl-lb-figure figcaption { color: #d4d4d8; font-size: 0.875rem; margin-top: 0.75rem; }
.adl-lb-figure figcaption .figno { color: #fafafa; }
.adl-lb-close, .adl-lb-nav {
  position: absolute;
  background: transparent;
  border: 0;
  color: #fff;
  font-size: 2rem;
  cursor: pointer;
  line-height: 1;
  opacity: 0.7;
}
.adl-lb-close:hover, .adl-lb-nav:hover { opacity: 1; }
.adl-lb-close { top: 1rem; right: 1.5rem; }
.adl-lb-nav { top: 50%; transform: translateY(-50%); }
.adl-lb-prev { left: 1rem; }
.adl-lb-next { right: 1rem; }
.community-other li { margin: 0.5rem 0; }

@media (max-width: 48rem) {
  .profile { grid-template-columns: 160px 1fr; }
  .contact-col { grid-column: 1 / -1; }
}
@media (max-width: 34rem) {
  .profile { grid-template-columns: 1fr; gap: 1.25rem; }
  .portrait { width: 130px; height: 130px; }
  .adl-card { width: 20rem; }
}
</style>
