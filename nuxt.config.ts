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
        { property: 'og:image', content: 'https://bobh62.github.io/images/og-image.png' },
        { property: 'og:image:width', content: '1200' },
        { property: 'og:image:height', content: '630' },
        { property: 'og:site_name', content: 'Haoming Huang' },
        { property: 'og:locale', content: 'en_US' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: 'Haoming Huang — Architecture · Robotics · AI' },
        {
          name: 'twitter:description',
          content:
            'MPhil (HKUST) · World Model Algorithm Engineer. Bridging architecture, robotics, and AI.',
        },
        { name: 'twitter:image', content: 'https://bobh62.github.io/images/og-image.png' },
        { name: 'author', content: 'Haoming Huang' },
      ],
      link: [
        { rel: 'canonical', href: 'https://bobh62.github.io/' },
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
          type: 'application/ld+json',
          innerHTML: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'Person',
            name: 'Haoming Huang',
            alternateName: '黄浩明',
            url: 'https://bobh62.github.io/',
            jobTitle: 'World Model Algorithm Engineer',
            worksFor: {
              '@type': 'Organization',
              name: 'Zhuoyu (formerly DJI Automotive)',
              url: 'https://www.zyt.com/zh',
            },
            alumniOf: [
              {
                '@type': 'CollegeOrUniversity',
                name: 'Hong Kong University of Science and Technology',
                url: 'https://hkust.edu.hk/',
              },
              {
                '@type': 'CollegeOrUniversity',
                name: 'South China University of Technology',
                url: 'https://www.scut.edu.cn/en/',
              },
            ],
            sameAs: [
              'https://scholar.google.com/citations?user=NUaxRNcAAAAJ',
              'https://github.com/BobH62',
            ],
            email: 'mailto:hhuangce@connect.ust.hk',
          }),
          tagPosition: 'head',
        },
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
      routes: ['/', '/publications', '/projects', '/highlights', '/sitemap.xml'],
    },
  },

  compatibilityDate: '2024-04-03',
})
