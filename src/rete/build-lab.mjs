// Assemble docs/lab.html: the template src/rete/lab.html with the rete engine, the recipe graph,
// the course queries and a world outline inlined, so the page works from any host or from disk.
import { readFileSync, readdirSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { feature } from 'topojson-client'

const root = new URL('../..', import.meta.url).pathname
const read = (...parts) => readFileSync(join(root, ...parts), 'utf8')
const mod = (...parts) => readFileSync(join(root, 'node_modules', ...parts), 'utf8')

const engine = mod('rete-graph/dist/rete-graph.min.js')
const { version } = JSON.parse(mod('rete-graph/package.json'))

const prefixes = Object.fromEntries([...read('src/data/prefixes.ttl').matchAll(/@prefix (\w+):\s*<([^>]+)>/g)].map((m) => [m[1], m[2]]))

// The worksheet queries, minus the ones that need the network; q20 opens on the map.
const dir = 'src/hands-on/h3-query/queries'
const examples = readdirSync(join(root, dir)).filter((f) => f.endsWith('.rq')).sort().flatMap((file) => {
  const text = read(dir, file)
  if (/^# online: true/m.test(text)) return []
  const [first, ...rest] = text.split('\n')
  const query = rest.filter((line) => !/^# #(end)?region/.test(line)).join('\n').trim()
  const id = file.slice(0, 3)
  return [{ id, title: first.replace(/^# q\d+ · /, ''), query: `${first}\n${query}\n`, ...(id === 'q20' ? { view: 'map' } : {}) }]
})
const mapExample = examples.find((e) => e.id === 'q20').query

// Land outline as one SVG path in an equirectangular projection: x = longitude, y = -latitude.
const topology = JSON.parse(mod('world-atlas/land-110m.json'))
const land = feature(topology, topology.objects.land)
// A ring that crosses the antimeridian is cut there, so that closing each piece runs along the map edge
// instead of across the map; the one ring around the pole (Antarctica) is closed along the bottom edge.
const pieces = (ring) => {
  const pts = ring.slice(0, -1) // drop the repeated closing point
  const jumps = pts.map((p, i) => i).filter((i) => Math.abs(pts[i][0] - pts[(i + pts.length - 1) % pts.length][0]) > 180)
  if (!jumps.length) return [pts]
  const turned = [...pts.slice(jumps[0]), ...pts.slice(0, jumps[0])]
  if (jumps.length === 1) {
    const pole = turned[0][1] < 0 ? -90 : 90
    return [[...turned, [turned.at(-1)[0], pole], [turned[0][0], pole]]]
  }
  const out = [[]]
  turned.forEach((p, i) => {
    if (i && Math.abs(p[0] - turned[i - 1][0]) > 180) out.push([])
    out.at(-1).push(p)
  })
  return out
}
const world = land.features.flatMap((f) => (f.geometry.type === 'Polygon' ? [f.geometry.coordinates] : f.geometry.coordinates))
  .flat()
  .flatMap(pieces)
  .map((pts) => `M${pts.map(([lon, lat]) => `${+lon.toFixed(1)},${+(-lat).toFixed(1)}`).join('L')}Z`)
  .join('')

const starterTurtle = `@prefix schema: <https://schema.org/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix rec:    <${prefixes.rec}> .
@prefix recipe: <${prefixes.recipe}> .
@prefix food:   <${prefixes.food}> .
@prefix cuisine: <${prefixes.cuisine}> .
@prefix course: <${prefixes.course}> .

# Your own recipe. Edit it: the graph is rebuilt as you type.
recipe:tomato-salad a schema:Recipe ;
    schema:name "Tomato salad"@en, "Tomatensalat"@de ;
    schema:totalTime "PT10M"^^xsd:dayTimeDuration ;
    rec:cuisine cuisine:italian ;
    rec:course course:starter ;
    schema:suitableForDiet schema:VeganDiet ;
    rec:hasIngredient food:tomato, food:olive-oil, food:basil, food:salt .
`
const starterJsonld = `${JSON.stringify({
  '@context': {
    schema: 'https://schema.org/',
    rec: prefixes.rec,
    food: prefixes.food,
    name: { '@id': 'schema:name', '@language': 'en' },
    totalTime: { '@id': 'schema:totalTime', '@type': 'http://www.w3.org/2001/XMLSchema#dayTimeDuration' },
    ingredients: { '@id': 'rec:hasIngredient', '@type': '@id' },
  },
  '@id': `${prefixes.recipe}tomato-salad`,
  '@type': 'schema:Recipe',
  name: 'Tomato salad',
  totalTime: 'PT10M',
  ingredients: ['food:tomato', 'food:olive-oil', 'food:basil', 'food:salt'],
}, null, 2)}\n`

const data = {
  version,
  prefixes,
  examples,
  mapExample,
  world,
  starterTurtle,
  starterJsonld,
  kgName: 'Recipes',
  kg: readFileSync(join(root, 'docs/data/recipes.rete')).toString('base64'),
}

// Function replacements: the engine and the data contain `$` sequences that String.replace would expand.
const html = read('src/rete/lab.html')
  .replace('__LAB_DATA__', () => JSON.stringify(data).replace(/</g, '\\u003c'))
  .replace('__RETE_ENGINE__', () => engine.replace(/<\/script/gi, '<\\/script'))
writeFileSync(join(root, 'docs/lab.html'), html)
console.log(`docs/lab.html: ${(html.length / 1048576).toFixed(1)} MB, rete-graph ${version}, ${examples.length} queries, world outline ${(world.length / 1024).toFixed(0)} KB`)
