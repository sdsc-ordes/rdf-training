import { readFileSync, readdirSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

const dir = fileURLToPath(new URL('../../hands-on/h3-query/queries/', import.meta.url))
const site = process.env.SITE_URL ?? 'https://sdsc-ordes.github.io/rdf-training/'
const kg = `${site}files/kg.ttl`

export default {
  watch: ['../../hands-on/h3-query/queries/*.rq'],
  load: () => Object.fromEntries(readdirSync(dir).filter((f) => f.endsWith('.rq')).sort().map((f) => {
    const query = readFileSync(dir + f, 'utf8')
    return [f.slice(0, 3), `https://query.comunica.dev/#datasources=${encodeURIComponent(kg)}&query=${encodeURIComponent(query)}`]
  })),
}
