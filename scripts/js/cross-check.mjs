// Check that the engines behind the browser tools agree with the Python harness:
// rdf-validate-shacl (Zazuko SHACL Playground) and Comunica (Comunica web client).
import { readFileSync, readdirSync } from 'node:fs'
import { join } from 'node:path'
import rdf from '@zazuko/env-node'
import SHACLValidator from 'rdf-validate-shacl'
import { QueryEngine } from '@comunica/query-sparql'
import { Parser, Store } from 'n3'

const root = new URL('../..', import.meta.url).pathname
const p = (...parts) => join(root, ...parts)
const ttlIn = (dir) => readdirSync(p(dir)).filter((f) => f.endsWith('.ttl')).sort().map((f) => p(dir, f))
const context = [...ttlIn('data/vocab'), ...ttlIn('data/concepts'), p('data/golden/foods.ttl'), p('data/golden/people.ttl')]
const recipes = p('data/golden/recipes.ttl')
const h2 = p('hands-on/h2-validate')
const h3 = p('hands-on/h3-query')

const prefixes = {}
new Parser().parse(readFileSync(p('data/prefixes.ttl'), 'utf8'), null, (prefix, iri) => { prefixes[prefix] = iri.value })
const expand = (curie) => (curie ? prefixes[curie.split(':')[0]] + curie.slice(curie.indexOf(':') + 1) : '')

let failures = 0
const check = (ok, label, detail = '') => {
  console.log(`${ok ? 'ok  ' : 'FAIL'} ${label}${ok ? '' : `\n     ${detail}`}`)
  if (!ok) failures++
}

// --- SHACL ------------------------------------------------------------------
const dataset = async (files) => {
  const ds = rdf.dataset()
  for (const f of files) await ds.import(rdf.fromFile(f))
  return ds
}
const validator = new SHACLValidator(await dataset([p('data/shapes/recipes.shapes.ttl')]), { factory: rdf })
const results = async (files) => {
  const report = await validator.validate(await dataset(files))
  const rows = report.results.map((r) => [r.focusNode, r.path, r.sourceShape, r.sourceConstraintComponent, r.severity]
    .map((t) => (t && t.termType === 'NamedNode' ? t.value : '')).join(' | '))
  return [...new Set(rows)].sort() // compare as sets, like the Python harness
}

const golden = await results([...context, recipes])
check(golden.length === 0, 'golden data has no SHACL results', golden.join('\n     '))

const expected = {}
for (const line of readFileSync(join(h2, 'expected.tsv'), 'utf8').trim().split('\n').slice(1)) {
  const [file, , focus, path, shape, component, severity] = line.split('\t')
  ;(expected[file] ??= []).push([focus, path, shape, component, severity].map(expand).join(' | '))
}
for (const [file, want] of Object.entries(expected)) {
  const got = await results([...context, join(h2, 'buggy', file)])
  check(JSON.stringify(got) === JSON.stringify(want.sort()), `shacl ${file}`,
    `got:\n       ${got.join('\n       ')}\n     want:\n       ${want.join('\n       ')}`)
}

// --- SPARQL -----------------------------------------------------------------
const store = new Store()
for (const f of [...context, recipes]) store.addQuads(new Parser({ baseIRI: 'file://' + f }).parse(readFileSync(f, 'utf8')))
const engine = new QueryEngine()

const XSD_INTEGER = 'http://www.w3.org/2001/XMLSchema#integer'
const XSD_STRING = 'http://www.w3.org/2001/XMLSchema#string'
const term = (t) => {
  if (!t) return ''
  if (t.termType === 'NamedNode') return `<${t.value}>`
  if (t.termType === 'BlankNode') return `_:${t.value}`
  if (t.datatype?.value === XSD_INTEGER && /^-?\d+$/.test(t.value)) return t.value
  const v = `"${t.value.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n').replace(/\t/g, '\\t')}"`
  if (t.language) return `${v}@${t.language}`
  return t.datatype?.value === XSD_STRING ? v : `${v}^^<${t.datatype.value}>`
}

for (const file of readdirSync(join(h3, 'queries')).filter((f) => f.endsWith('.rq')).sort()) {
  const query = readFileSync(join(h3, 'queries', file), 'utf8')
  if (query.includes('# online: true')) continue
  const result = await engine.query(query, { sources: [store] })
  let tsv
  if (result.resultType === 'boolean') {
    tsv = `${await result.execute()}\n`
  } else {
    const vars = (await result.metadata()).variables.map((v) => v.variable ?? v)
    const rows = await (await result.execute()).toArray()
    tsv = [vars.map((v) => `?${v.value}`).join('\t'), ...rows.map((b) => vars.map((v) => term(b.get(v))).join('\t'))].join('\n') + '\n'
  }
  const want = readFileSync(join(h3, 'expected', file.replace('.rq', '.tsv')), 'utf8')
  check(tsv === want, `sparql ${file}`, `got:\n${tsv}\n     want:\n${want}`)
}

process.exit(failures ? 1 : 0)
