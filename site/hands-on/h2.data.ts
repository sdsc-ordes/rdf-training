import { readFileSync, readdirSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../../', import.meta.url))
const read = (path: string) => readFileSync(root + path, 'utf8')
const ttlIn = (dir: string) => readdirSync(root + dir).filter((f) => f.endsWith('.ttl')).sort().map((f) => `${dir}/${f}`)

const context = [...ttlIn('data/vocab'), ...ttlIn('data/concepts'), 'data/golden/foods.ttl', 'data/golden/people.ttl']
  .map(read).join('\n')
const shapes = read('data/shapes/recipes.shapes.ttl')
const marker = '\n# ---- paste your recipes below this line ----\n\n'

const zazuko = (data: string) => 'https://shacl-playground.zazuko.com/#' + [
  ['page', '0'], ['shapesGraph', shapes], ['shapesGraphFormat', 'text/turtle'],
  ['dataGraph', data], ['dataGraphFormat', 'text/turtle'],
].map(([k, v]) => `${k}=${encodeURIComponent(v)}`).join('&')

const iris = (file: string, prefix: string, type: string) =>
  [...read(file).matchAll(new RegExp(`^(${prefix}:[\\w-]+) +a ${type}[ ;]`, 'gm'))].map((m) => m[1]).join(', ')

const prompt = read('hands-on/h2-validate/prompt-generate.md')
  .replace('{{cuisines}}', iris('data/concepts/cuisines.ttl', 'cuisine', 'skos:Concept'))
  .replace('{{courses}}', iris('data/concepts/courses.ttl', 'course', 'skos:Concept'))
  .replace('{{people}}', iris('data/golden/people.ttl', 'person', 'schema:Person'))
  .replace('{{foods}}', iris('data/golden/foods.ttl', 'food', 'rec:\\w+'))

export default {
  watch: ['../../data/**/*.ttl', '../../hands-on/h2-validate/**/*'],
  load: () => ({
    prompt,
    fixPrompt: read('hands-on/h2-validate/prompt-fix.md'),
    validate: zazuko(context + marker),
    fallback: zazuko(context + marker + read('hands-on/h2-validate/buggy/b11-llm-first-attempt.ttl')),
  }),
}
