import { defineEventHandler, setHeader } from 'h3'
import { queryCollection } from '@nuxt/content/server'

const SITE = 'https://bobh62.github.io'

export default defineEventHandler(async (event) => {
  const staticPaths = ['/', '/publications', '/projects', '/highlights']

  const projects = await queryCollection(event, 'projects')
    .select('path')
    .all()

  const urls = [
    ...staticPaths.map((p) => ({ loc: p, priority: p === '/' ? '1.0' : '0.8' })),
    ...projects.map((p) => ({ loc: p.path, priority: '0.7' })),
  ]

  const lastmod = new Date().toISOString().slice(0, 10)

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map(
    (u) =>
      `  <url>\n    <loc>${SITE}${u.loc}</loc>\n    <lastmod>${lastmod}</lastmod>\n    <priority>${u.priority}</priority>\n  </url>`
  )
  .join('\n')}
</urlset>`

  setHeader(event, 'Content-Type', 'application/xml; charset=utf-8')
  return body
})
