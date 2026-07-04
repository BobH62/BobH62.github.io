<script setup lang="ts">
const nav = [
  { title: 'Home', to: '/' },
  { title: 'Publications', to: '/publications' },
  { title: 'Projects', to: '/projects' },
  { title: 'Highlights', to: '/highlights' },
]

const route = useRoute()
const year = new Date().getFullYear()
</script>

<template>
  <div class="site">
    <header class="site-header">
      <div class="container header-inner">
        <NuxtLink to="/" class="brand">Haoming Huang</NuxtLink>
        <nav class="nav">
          <NuxtLink
            v-for="item in nav"
            :key="item.to"
            :to="item.to"
            class="nav-link"
            :class="{ active: route.path === item.to }"
          >
            {{ item.title }}
          </NuxtLink>
        </nav>
      </div>
    </header>

    <main class="site-main">
      <slot />
    </main>

    <footer class="site-footer">
      <div class="container footer-inner">
        <span>&copy; {{ year }} Haoming Huang</span>
        <span class="footer-links">
          <a href="mailto:hhuangce@connect.ust.hk">email</a>
          <a href="https://github.com/HKUST-Aerial-Robotics" target="_blank" rel="noopener">github</a>
          <a href="https://scholar.google.com/" target="_blank" rel="noopener">scholar</a>
        </span>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.site {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  background: rgba(250, 250, 250, 0.85);
  backdrop-filter: saturate(180%) blur(8px);
  border-bottom: 1px solid var(--border);
}
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 3.5rem;
}
.brand {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1rem;
  color: var(--text);
}
.brand:hover { color: var(--accent); }
.nav {
  display: flex;
  gap: 1.25rem;
}
.nav-link {
  font-size: 0.9rem;
  color: var(--text-muted);
  border-bottom: 2px solid transparent;
  padding-bottom: 0.15rem;
  transition: color var(--transition), border-color var(--transition);
}
.nav-link:hover { color: var(--text); }
.nav-link.active {
  color: var(--accent);
  border-bottom-color: var(--accent);
}
.site-main {
  flex: 1;
  padding: 2.5rem 0 3rem;
}
.site-footer {
  border-top: 1px solid var(--border);
  padding: 1.5rem 0;
  font-size: 0.825rem;
  color: var(--text-faint);
}
.footer-inner {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.75rem;
}
.footer-links { display: flex; gap: 1rem; }
.footer-links a { color: var(--text-faint); }
.footer-links a:hover { color: var(--accent); }

@media (max-width: 30rem) {
  .nav { gap: 0.85rem; }
  .nav-link { font-size: 0.85rem; }
}
</style>
