// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ['@nuxt/content', '@nuxt/image'],

  devtools: { enabled: true },

  ssr: true,

  site: {
    url: 'https://bobh62.github.io',
    name: 'Haoming Huang',
  },

  app: {
    baseURL: '/',
    head: {
      htmlAttrs: { lang: 'en' },
      title: 'Haoming Huang — Architecture · Robotics · AI',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            'Haoming Huang — MPhil (HKUST), World Model Algorithm Engineer. Bridging architecture, robotics, and AI through cross-modal registration, SLAM, and digital fabrication.',
        },
        { name: 'theme-color', content: '#fafafa' },
        { property: 'og:type', content: 'website' },
        { property: 'og:title', content: 'Haoming Huang — Architecture · Robotics · AI' },
        {
          property: 'og:description',
          content:
            'MPhil (HKUST) · World Model Algorithm Engineer. Bridging architecture, robotics, and AI.',
        },
        { property: 'og:url', content: 'https://bobh62.github.io' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/images/favicon-16x16.png' },
        { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/images/favicon-32x32.png' },
        { rel: 'apple-touch-icon', sizes: '180x180', href: '/images/apple-touch-icon.png' },
        {
          rel: 'stylesheet',
          href: 'https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&f[]=alpino@400,500,700&display=swap',
        },
      ],
      script: [
        {
          innerHTML:
            "(function(){try{var t=localStorage.getItem('theme');var d=t==='dark'||(!t&&window.matchMedia('(prefers-color-scheme:dark)').matches);if(d){document.documentElement.classList.add('dark');document.documentElement.style.colorScheme='dark';}}catch(e){}})();",
          tagPosition: 'head',
        },
      ],
    },
  },

  css: ['~/assets/css/main.css'],

  content: {
    build: {
      markdown: {
        highlight: {
          theme: {
            default: 'github-light',
          },
        },
      },
    },
  },

  image: {
    quality: 80,
    format: ['webp'],
  },

  nitro: {
    preset: 'static',
    prerender: {
      crawlLinks: true,
      routes: ['/', '/publications', '/projects', '/highlights'],
    },
  },

  compatibilityDate: '2024-04-03',
})
