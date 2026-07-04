import { defineContentConfig, defineCollection, z } from '@nuxt/content'

export default defineContentConfig({
  collections: {
    pages: defineCollection({
      type: 'page',
      source: '*.md',
    }),

    projects: defineCollection({
      type: 'page',
      source: 'projects/**/*.md',
      schema: z.object({
        title: z.string(),
        date: z.string(),
        excerpt: z.string(),
        image: z.string().optional(),
        tags: z.array(z.string()).default([]),
        role: z.string().optional(),
        stack: z.array(z.string()).default([]),
        links: z
          .array(z.object({ label: z.string(), url: z.string() }))
          .default([]),
        gallery: z.array(z.string()).default([]),
        nda: z.boolean().default(false),
        category: z.string().default('project'),
      }),
    }),

    publications: defineCollection({
      type: 'data',
      source: 'publications/*.yml',
      schema: z.object({
        title: z.string(),
        authors: z.string(),
        venue: z.string(),
        year: z.number(),
        image: z.string().optional(),
        type: z.string().default('paper'),
        order: z.number().default(0),
        links: z
          .array(z.object({ label: z.string(), url: z.string() }))
          .default([]),
      }),
    }),
  },
})
