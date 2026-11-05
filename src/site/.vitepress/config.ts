import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Knowledge Graphs',
  description: 'RDF knowledge graph course: slides, hands-on and reference',
  base: process.env.SITE_BASE ?? '/rdf-training/',
  outDir: '../_site',
  vite: { publicDir: '../slides/public' },
  themeConfig: {
    logo: { light: '/SDSC_Logo_RGB.png', dark: '/SDSC_Logo_White.png' },
    siteTitle: false,
    nav: [{ text: 'Hands-on', link: '/hands-on/h1-model' }],
    sidebar: [
      {
        text: 'Hands-on',
        items: [
          { text: 'H1 · Model', link: '/hands-on/h1-model' },
          { text: 'H2 · Generate and validate', link: '/hands-on/h2-validate' },
          { text: 'H3 · Query', link: '/hands-on/h3-query' },
        ],
      },
    ],
    socialLinks: [{ icon: 'github', link: 'https://github.com/sdsc-ordes/rdf-training' }],
  },
})
