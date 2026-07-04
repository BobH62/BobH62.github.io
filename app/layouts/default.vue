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
      <div class="header-inner">
        <NuxtLink to="/" class="brand">Haoming Huang</NuxtLink>
        <div class="nav-wrap">
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
          <span class="nav-divider" aria-hidden="true" />
          <div class="icon-row">
            <a href="https://scholar.google.com/citations?user=NUaxRNcAAAAJ&hl=en" target="_blank" rel="noopener" title="Google Scholar" class="icon-link" aria-label="Google Scholar">
              <svg viewBox="0 0 384 512" width="16" height="21" fill="currentColor" aria-hidden="true">
                <path d="M343.759 106.662V79.43L363.524 64h-213.89L20.476 176.274h85.656a82 82 0 0 0-.219 6.225c0 20.845 7.22 38.087 21.672 51.861c14.453 13.797 32.252 20.648 53.327 20.648c4.923 0 9.75-.368 14.438-1.024c-2.907 6.5-4.374 12.523-4.374 18.142c0 9.875 4.499 20.43 13.467 31.642c-39.234 2.67-68.061 9.732-86.437 21.163c-10.531 6.5-19 14.704-25.39 24.531c-6.391 9.9-9.578 20.515-9.578 31.962c0 9.648 2.062 18.336 6.219 26.062c4.156 7.726 9.578 14.07 16.312 18.984c6.718 4.968 14.469 9.101 23.219 12.469c8.734 3.344 17.406 5.718 26.061 7.062A167 167 0 0 0 180.555 448c13.469 0 26.953-1.734 40.547-5.187c13.562-3.485 26.28-8.642 38.171-15.493c11.86-6.805 21.515-16.086 28.922-27.718c7.39-11.68 11.094-24.805 11.094-39.336c0-11.016-2.25-21.039-6.75-30.14c-4.468-9.073-9.938-16.542-16.452-22.345c-6.501-5.813-13-11.155-19.516-15.968c-6.5-4.845-12-9.75-16.468-14.813c-4.485-5.046-6.735-10.054-6.735-14.984c0-4.921 1.734-9.672 5.216-14.265c3.455-4.61 7.674-9.048 12.61-13.306c4.937-4.25 9.875-8.968 14.796-14.133c4.922-5.147 9.141-11.827 12.61-20.008c3.485-8.18 5.203-17.445 5.203-27.757c0-13.453-2.547-24.46-7.547-33.314c-.594-1.022-1.218-1.803-1.875-3.022l56.907-46.672v17.119c-7.393.93-6.624 5.345-6.624 10.635V245.96c0 5.958 4.875 10.834 10.834 10.834h3.989c5.958 0 10.833-4.875 10.833-10.834V117.293c0-5.277.778-9.688-6.561-10.63m-107.36 222.48c1.14.75 3.704 2.78 7.718 6.038c4.05 3.243 6.797 5.695 8.266 7.414a444 444 0 0 1 6.376 7.547c2.813 3.375 4.718 6.304 5.718 8.734q1.5 3.717 3.047 8.946a38.3 38.3 0 0 1 1.485 10.562c0 17.048-6.564 29.68-19.656 37.859c-13.125 8.18-28.767 12.274-46.938 12.274c-9.187 0-18.203-1.093-27.063-3.196c-8.843-2.116-17.311-5.336-25.39-9.601c-8.078-4.258-14.577-10.204-19.5-17.797c-4.938-7.64-7.407-16.415-7.407-26.25c0-10.32 2.797-19.29 8.422-26.906c5.594-7.625 12.938-13.391 22.032-17.315c9.063-3.946 18.25-6.742 27.562-8.398a158 158 0 0 1 28.438-2.555c4.47 0 7.936.25 10.405.696c.455.219 3.032 2.07 7.735 5.563c4.704 3.462 7.625 5.595 8.75 6.384zm-3.359-100.579c-7.406 8.86-17.734 13.288-30.953 13.288c-11.86 0-22.298-4.764-31.266-14.312c-9-9.523-15.422-20.328-19.344-32.43c-3.937-12.109-5.906-23.984-5.906-35.648q.002-20.54 10.781-34.976c7.187-9.65 17.5-14.485 30.938-14.485c11.875 0 22.374 5.038 31.437 15.157c9.094 10.085 15.61 21.413 19.517 33.968c3.922 12.54 5.873 24.53 5.873 35.984c0 13.446-3.702 24.61-11.076 33.454z"/>
              </svg>
            </a>
            <a href="https://github.com/BobH62" target="_blank" rel="noopener" title="GitHub" class="icon-link" aria-label="GitHub">
              <svg viewBox="0 0 24 24" width="17" height="17" fill="currentColor" aria-hidden="true">
                <path d="M12 .5C5.4.5 0 5.9 0 12.5c0 5.3 3.4 9.8 8.2 11.4.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17 5 18 5.3 18 5.3c.6 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 24 12.5C24 5.9 18.6.5 12 .5z"/>
              </svg>
            </a>
            <a href="mailto:hhuangce@connect.ust.hk" title="Email" class="icon-link" aria-label="Email">
              <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true">
                <rect x="3" y="5" width="18" height="14" rx="2" />
                <path d="m3 7 9 6 9-6" />
              </svg>
            </a>
            <ThemeToggle />
          </div>
        </div>
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
          <a href="https://github.com/BobH62" target="_blank" rel="noopener">github</a>
          <a href="https://scholar.google.com/citations?user=NUaxRNcAAAAJ&hl=en" target="_blank" rel="noopener">scholar</a>
        </span>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.site {
  position: relative;
  z-index: 1;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  background: var(--header-bg);
  backdrop-filter: saturate(180%) blur(8px);
  border-bottom: 1px solid var(--border);
}
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 3rem;
  padding: 0 2rem;
  max-width: 100%;
}
.brand {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1rem;
  color: var(--text);
}
.brand:hover { color: var(--accent); }

.nav-wrap { display: flex; align-items: center; gap: 1.25rem; }
.nav { display: flex; gap: 1.1rem; }
.nav-link {
  font-size: 0.9rem;
  color: var(--text-muted);
  border-bottom: 2px solid transparent;
  padding-bottom: 0.15rem;
  transition: color var(--transition), border-color var(--transition);
}
.nav-link:hover { color: var(--text); }
.nav-link.active { color: var(--accent); border-bottom-color: var(--accent); }

.nav-divider { width: 1px; height: 1rem; background: var(--border); }
.icon-row { display: flex; align-items: center; gap: 0.5rem; }
.icon-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.75rem;
  height: 1.75rem;
  border-radius: 999px;
  color: var(--text-muted);
  transition: color var(--transition), background var(--transition);
}
.icon-link:hover { color: var(--text); background: var(--border); }

.site-main { flex: 1; position: relative; z-index: 1; padding: 2.5rem 0 3rem; }
.site-footer {
  position: relative;
  z-index: 1;
  border-top: 1px solid var(--border);
  padding: 1.5rem 0;
  font-size: 0.825rem;
  color: var(--text-faint);
}
.footer-inner { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem; }
.footer-links { display: flex; gap: 1rem; }
.footer-links a { color: var(--text-faint); }
.footer-links a:hover { color: var(--accent); }

@media (max-width: 34rem) {
  .header-inner { padding: 0 1.25rem; height: 2.75rem; }
  .nav { gap: 0.7rem; }
  .nav-link { font-size: 0.82rem; }
  .nav-divider { display: none; }
}
@media (max-width: 26rem) {
  .nav-wrap { gap: 0.6rem; }
}
</style>
