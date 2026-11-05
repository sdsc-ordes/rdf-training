import { readFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { definePreparserSetup } from '@slidev/types'

const CITE = /<p class="fine">(Sources?: )(.+?)<\/p>/g
const attr = (s: string) => s.replaceAll('&', '&amp;').replaceAll('"', '&quot;')

// Link each label in a "Sources:" line to its URL. The labels and URLs come from
// src/slides/references.toml, written to references/urls.json by kgcourse.refs.
export default definePreparserSetup(({ filepath }) => {
  const urls: Record<string, string> = JSON.parse(readFileSync(join(dirname(filepath), 'references', 'urls.json'), 'utf-8'))
  const link = (label: string) => urls[label] ? `<a href="${attr(urls[label])}" target="_blank" rel="noopener">${label}</a>` : label
  return [{
    name: 'course:source-links',
    transformRawLines(lines) {
      lines.forEach((line, i) => {
        lines[i] = line.replace(CITE, (_, head, labels) => `<p class="fine">${head}${labels.split(' · ').map(link).join(' · ')}</p>`)
      })
    },
  }]
})
