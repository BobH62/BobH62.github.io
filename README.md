# bobh62.github.io

Personal website for Haoming Huang — built with [Nuxt 4](https://nuxt.com), [@nuxt/content](https://content.nuxt.com), and [@nuxt/image](https://image.nuxt.com). Design inspired by [beyond-disciplines.com](https://beyond-disciplines.com) (minimal, single-column, Satoshi/Alpino typography, zinc palette with a restrained teal accent).

## Stack

- Nuxt 4 (Static Site Generation via `nuxt generate`)
- @nuxt/content v3 (Markdown projects + YAML publications)
- @nuxt/image (responsive WebP)
- GitHub Actions → GitHub Pages

## Develop

```bash
npm install
npm run dev          # http://localhost:3000
```

## Content

- `content/projects/*.md` — project pages (frontmatter: title, date, summary, image, tags, role, stack, links, gallery, nda)
- `content/publications/*.yml` — publication entries
- `app/pages/index.vue` — About / home
- `app/pages/highlights.vue` — trajectory timeline, awards, open source
- `public/images/` — site images (SDME gallery in `public/images/sdme/`)

## Build & preview

```bash
npm run generate     # outputs .output/public
npx serve .output/public
```

## Deploy

Push to `main` triggers `.github/workflows/deploy.yml`, which builds and deploys to GitHub Pages. In repo Settings → Pages, set Source to **GitHub Actions** (one-time).

The previous Jekyll site is preserved on the `backup/jekyll` branch and the `jekyll-final` tag.
