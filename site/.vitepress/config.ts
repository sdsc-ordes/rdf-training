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
    socialLinks: [{ icon: 'github', link: 'https://github.com/sdsc-ordes/rdf-training' }],
  },
})
