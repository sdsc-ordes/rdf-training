import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../../', import.meta.url))
const read = (path: string) => readFileSync(root + path, 'utf8')

const context = ['data/ontology/ontology.ttl', 'data/ontology/enumerations.ttl', 'data/golden/countries.ttl',
  'data/golden/units.ttl', 'data/golden/foods.ttl', 'data/golden/people.ttl']
  .map(read).join('\n')
const shapes = read('data/ontology/shapes.ttl')
const marker = '\n# ---- paste your recipes below this line ----\n\n'

const zazuko = (data: string) => 'https://shacl-playground.zazuko.com/#' + [
  ['page', '0'], ['shapesGraph', shapes], ['shapesGraphFormat', 'text/turtle'],
  ['dataGraph', data], ['dataGraphFormat', 'text/turtle'],
].map(([k, v]) => `${k}=${encodeURIComponent(v)}`).join('&')

const iris = (file: string, prefix: string, type: string) =>
  [...read(file).matchAll(new RegExp(`^(${prefix}:[\\w-]+) +a ${type}[ ;]`, 'gm'))].map((m) => m[1]).join(', ')

const prompt = read('hands-on/h2-validate/prompt-generate.md')
  .replace('{{cuisines}}', iris('data/ontology/enumerations.ttl', 'cuisine', 'skos:Concept'))
  .replace('{{courses}}', iris('data/ontology/enumerations.ttl', 'course', 'skos:Concept'))
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
