// Drive docs/lab.html in a browser, opened from disk: every worksheet query must return the rows of its
// snapshot, a broken query must be reported, and Turtle and JSON-LD must build into a graph that can be
// queried and downloaded. With --shots, also write the screenshots used in docs/index.html.
import { createServer } from 'node:http'
import { existsSync, readFileSync, readdirSync } from 'node:fs'
import { join } from 'node:path'
import { pathToFileURL } from 'node:url'
import { chromium } from 'playwright-chromium'

const root = new URL('../..', import.meta.url).pathname
const shots = process.argv.includes('--shots')
const expectedDir = join(root, 'src/hands-on/h3-query/expected')

let failures = 0
const check = (ok, label, detail = '') => {
  console.log(`${ok ? 'ok  ' : 'FAIL'} ${label}${ok ? '' : `\n     ${detail}`}`)
  if (!ok) failures++
}

// docs/ over HTTP with CORS, to open a .rete by URL from the page on disk.
const server = createServer((req, res) => {
  const file = join(root, 'docs', decodeURIComponent(req.url.split('?')[0]))
  if (!existsSync(file)) return res.writeHead(404).end()
  res.writeHead(200, { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/octet-stream' }).end(readFileSync(file))
})
await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve))
const reteUrl = `http://127.0.0.1:${server.address().port}/data/recipes.rete`

const executablePath = process.env.SLIDEV_CHROMIUM || undefined
const browser = await chromium.launch({ executablePath }).catch(() => chromium.launch({ channel: 'chrome' }))
const page = await browser.newPage({ viewport: { width: 1440, height: 860 }, acceptDownloads: true })
const errors = []
page.on('pageerror', (e) => errors.push(String(e)))
const shot = async (name) => {
  await page.locator('.side').evaluate((side) => side.scrollTo(0, 0))
  await page.mouse.move(700, 600)
  if (shots) await page.screenshot({ path: join(root, 'docs/img', `${name}.png`) })
}
const status = (id) => page.locator(`#${id}`).innerText()
const settled = (id, kind) => page.waitForFunction(([i, k]) => document.getElementById(i).classList.contains(k), [id, kind], { timeout: 10000 })

await page.goto(pathToFileURL(join(root, 'docs/lab.html')).href)
await settled('q-status', 'ok')
check((await page.locator('#datasets li').count()) === 1, 'built-in recipe graph opens from the page itself')

// --- worksheet queries ------------------------------------------------------
for (const file of readdirSync(expectedDir).sort()) {
  const id = file.slice(0, 3)
  const tsv = readFileSync(join(expectedDir, file), 'utf8').trim().split('\n')
  await page.locator(`#examples button[data-id=${id}]`).click()
  await settled('q-status', 'ok')
  const text = await status('q-status')
  if (tsv[0] === 'ASK' || /^(true|false)$/.test(tsv[tsv.length - 1])) {
    const want = tsv[tsv.length - 1]
    check((await page.locator('#out .bool').innerText()) === want, `${id} answers ${want}`, text)
  } else {
    const rows = await page.locator('#out').evaluate((out) => out.querySelectorAll('tbody tr, .card, circle').length)
    check(rows === tsv.length - 1, `${id} returns ${tsv.length - 1} rows`, `got ${rows}: ${text}`)
  }
}

// --- views ------------------------------------------------------------------
await page.locator('#examples button[data-id=q04]').click()
await page.locator('#views [data-view=table]').click()
await settled('q-status', 'ok')
await shot('lab-table')

await page.locator('#q').fill(`${await page.locator('#q').inputValue()}\n}`)
await settled('q-status', 'err')
check((await status('q-status')).includes('not valid'), 'a broken query is reported while typing')
check(await page.locator('#out.stale').count() === 1, 'the last good result stays on screen, dimmed')
await shot('lab-error')

await page.locator('#examples button[data-id=q07]').click()
await page.locator('#views [data-view=cards]').click()
await settled('q-status', 'ok')
check((await page.locator('#out .card').count()) > 0, 'cards view shows one card per row')
await shot('lab-cards')

await page.locator('#examples button[data-id=q20]').click()
await settled('q-status', 'ok')
check((await page.locator('#out svg circle').count()) === 6, 'map view places the six countries')
await shot('lab-map')
await page.locator('#examples button[data-id=q01]').click()
await page.locator('#views [data-view=map]').click()
check((await page.locator('#out .empty').innerText()).includes('?lat'), 'map view explains what it needs when there are no coordinates')
await page.locator('#views [data-view=table]').click()

// --- editor: colours, line numbers, collapsible examples ---------------------
await page.locator('#examples button[data-id=q04]').click()
await settled('q-status', 'ok')
const lines = (await page.locator('#q').inputValue()).split('\n').length
check((await page.locator('#q-ed .gutter div').count()) === lines, `the query editor numbers its ${lines} lines`)
const kinds = await page.locator('#q-ed pre').evaluate((pre) => [...new Set([...pre.querySelectorAll('span')].map((s) => s.className))].join(' '))
check(['t-kw', 't-var', 't-iri', 't-str', 't-pn', 't-com'].every((k) => kinds.includes(k)), 'the query is coloured: keywords, variables, IRIs, strings, prefixed names, comments', kinds)
check(await page.locator('#q-ed pre').evaluate((pre) => pre.textContent === `${document.getElementById('q').value}\n`), 'the coloured text is the text being edited')
const box = (sel) => page.locator(sel).evaluate((e) => { const r = document.createRange(); r.selectNodeContents(e); const b = r.getClientRects()[0]; return [Math.round(b.left), Math.round(b.top)] })
const first = await box('#q-ed pre'), caret = await page.locator('#q').evaluate((ta) => { const b = ta.getBoundingClientRect(), c = getComputedStyle(ta); return [Math.round(b.left + parseFloat(c.paddingLeft)), Math.round(b.top + parseFloat(c.paddingTop))] })
check(Math.abs(first[0] - caret[0]) <= 1 && Math.abs(first[1] - caret[1]) <= 3, 'the coloured text sits exactly under the caret', `${first} vs ${caret}`)
await page.locator('#q').fill(`${await page.locator('#q').inputValue()}\n}`)
await settled('q-status', 'err')
check((await page.locator('#q-ed .gutter .bad').count()) === 1, 'the line of a parse error is marked in the gutter')
await page.locator('#ex-box summary').click()
check(!(await page.locator('#examples').isVisible()), 'the example queries collapse')
await page.locator('#ex-box summary').click()
check(await page.locator('#examples').isVisible(), 'and expand again')

// --- write data, keep it in memory, query it, download it -----------------------
await page.locator('#mode-create').click()
await settled('d-status', 'ok')
check((await status('d-status')).includes('valid Turtle'), 'starter Turtle builds into a .rete in memory', await status('d-status'))
check((await page.locator('#out tbody tr').count()) > 5, 'Create KG shows the triples of the data being written')
check((await page.locator('#d-ed pre .t-pn').count()) > 5, 'the Turtle is coloured too')
await shot('lab-create')

await page.locator('#d').fill('@prefix ex: <http://example.org/> .\nex:a ex:b')
await settled('d-status', 'err')
check((await status('d-status')).includes('not valid Turtle'), 'broken Turtle is reported while typing')

await page.locator('#d-example').click()
await settled('d-status', 'ok')
check((await status('d-status')).includes('valid JSON-LD'), 'JSON-LD example builds into a .rete in memory', await status('d-status'))

await page.locator('#combine').selectOption('builtin')
await page.waitForFunction(() => document.querySelector('#d-status .txt').textContent.includes('from Recipes'))
const [download] = await Promise.all([page.waitForEvent('download'), page.locator('#d-download').click()])
const magic = readFileSync(await download.path()).subarray(0, 4).toString('latin1')
check(magic === 'RETE', 'the graph in memory downloads as a .rete file', `magic ${magic}`)
await shot('lab-data')

await page.locator('#d-query').click()
await page.locator('#q').fill(`PREFIX schema: <https://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rec: <https://sdsc-ordes.github.io/rdf-training/vocab/recipes#>
PREFIX recipe: <https://sdsc-ordes.github.io/rdf-training/id/recipe/>
SELECT ?name ?ingredient WHERE {
  recipe:tomato-salad schema:name ?name ; rec:hasIngredient/rdfs:label ?ingredient .
  FILTER(lang(?ingredient) = "en")
}`)
await page.waitForFunction(() => document.querySelectorAll('#out tbody tr').length === 4, null, { timeout: 10000 }).catch(() => {})
check((await page.locator('#out tbody tr').count()) === 4, 'the written recipe joins the course graph: 4 labelled ingredients', await status('q-status'))
await shot('lab-own-recipe')

// --- open a .rete by URL ----------------------------------------------------------
await page.locator('#url').fill(reteUrl)
await page.locator('#url-form button').click()
await page.waitForFunction(() => document.querySelectorAll('#datasets li').length === 3, null, { timeout: 10000 }).catch(() => {})
check((await page.locator('#datasets li.on small').innerText()).includes('URL'), 'a .rete file opens from a URL and becomes the queried graph', await page.locator('#add-msg').innerText())

await page.goto('about:blank')
await page.goto(`${pathToFileURL(join(root, 'docs/lab.html')).href}#view=cards&q=${encodeURIComponent('ASK { ?s ?p ?o }')}`)
await settled('q-status', 'ok')
check((await page.locator('#out .bool').innerText()) === 'true', 'a link restores the query')

check(errors.length === 0, 'no uncaught errors in the page', errors.join('\n     '))
await browser.close()
server.close()
if (failures) {
  console.error(`${failures} check(s) failed`)
  process.exit(1)
}
