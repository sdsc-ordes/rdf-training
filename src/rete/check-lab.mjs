// Drive docs/index.html in a browser, opened from disk: every worksheet query must return the rows of its
// snapshot, a broken query must be reported, and Turtle and JSON-LD must build into a graph that can be
// queried and downloaded. With --shots, also write the screenshots in docs/img/.
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
// Query KG and Validate KG run only when asked: the Run and Validate buttons, or Ctrl+Enter in the editor.
const pill = (id) => page.locator(`#${id} .pill`).innerText()
const notRun = (id) => page.waitForFunction((i) => document.querySelector(`#${i} .pill`).textContent === 'not run', id, { timeout: 10000 })
const runQuery = async (kind = 'ok') => { await page.locator('#q-run').click(); await settled('q-status', kind) }
const shown = (sel) => page.locator(sel).first().isVisible()
const graphLoaded = () => page.waitForFunction(() => document.querySelectorAll('#datasets li').length === 1, null, { timeout: 10000 })

await page.goto(pathToFileURL(join(root, 'docs/index.html')).href)
await graphLoaded()
check((await page.locator('#datasets li').count()) === 1, 'built-in recipe graph opens from the page itself')
check(await page.locator('#home').isVisible() && !(await page.locator('#q').isVisible()) && !(await page.locator('.side').isVisible()), 'the page opens on Welcome, without the sidebar')
check((await page.locator('#home a[href="https://github.com/caviri/rete"]').count()) >= 1 && (await page.locator('#ver2').innerText()) !== '', 'Welcome names the rete engine, its version and its repository')
await shot('lab-welcome')
await page.locator('#go-create').click()
check(await page.locator('#d').isVisible() && await page.locator('.side').isVisible(), 'Welcome leads to Create KG')
await page.locator('#mode-home').click()
await page.locator('#go-query').click()
check(await page.locator('#q').isVisible() && !(await page.locator('#home').isVisible()), 'and to Query KG')
check((await pill('q-status')) === 'not run' && (await page.locator('#out .empty').innerText()).includes('Press Run'), 'Query KG runs nothing until Run is pressed')
check(!(await shown('#add-example')) && !(await shown('#url')) && !(await shown('#csv')) && !(await shown('#share')) && !(await shown('#datasets .dl')) && await shown('#q-run') && await shown('#prefixes') && await shown('#examples'), 'beginners see the examples, + prefixes and Run, not the rarer tools')

// --- worksheet queries ------------------------------------------------------
for (const file of readdirSync(expectedDir).sort()) {
  const id = file.slice(0, 3)
  const tsv = readFileSync(join(expectedDir, file), 'utf8').trim().split('\n')
  await page.locator(`#examples button[data-id=${id}]`).click()
  await runQuery()
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
await runQuery()
await shot('lab-table')

const answer = await page.locator('#out').innerText()
await page.locator('#q').fill(`${await page.locator('#q').inputValue()}\n}`)
check((await pill('q-status')) === 'not run' && (await page.locator('#out').innerText()) === answer && await page.locator('#out.stale').count() === 1, 'typing does not run the query: the last answer stays, dimmed')
await runQuery('err')
check((await status('q-status')).includes('not valid'), 'a broken query is reported when it is run')
check(await page.locator('#out.stale').count() === 1, 'the last good result stays on screen, dimmed')
await shot('lab-error')

await page.locator('#examples button[data-id=q07]').click()
check((await pill('q-status')) === 'not run' && (await page.locator('#q').inputValue()).includes('q07'), 'picking an example loads it without running it')
await page.locator('#views [data-view=cards]').click()
await runQuery()
check((await page.locator('#out .card').count()) > 0, 'cards view shows one card per row')
await shot('lab-cards')

await page.locator('#examples button[data-id=q20]').click()
await runQuery()
check((await page.locator('#out svg circle').count()) === 6, 'map view places the six countries')
await shot('lab-map')
await page.locator('#examples button[data-id=q01]').click()
await runQuery()
await page.locator('#views [data-view=map]').click()
check((await page.locator('#out .empty').innerText()).includes('?lat'), 'map view explains what it needs when there are no coordinates')
await page.locator('#views [data-view=table]').click()

// --- editor: colours, line numbers, collapsible examples ---------------------
await page.locator('#examples button[data-id=q04]').click()
await runQuery()
const lines = (await page.locator('#q').inputValue()).split('\n').length
check((await page.locator('#q-ed .gutter div').count()) === lines, `the query editor numbers its ${lines} lines`)
const kinds = await page.locator('#q-ed pre').evaluate((pre) => [...new Set([...pre.querySelectorAll('span')].map((s) => s.className))].join(' '))
check(['t-kw', 't-var', 't-iri', 't-str', 't-pn', 't-com'].every((k) => kinds.includes(k)), 'the query is coloured: keywords, variables, IRIs, strings, prefixed names, comments', kinds)
check(await page.locator('#q-ed pre').evaluate((pre) => pre.textContent === `${document.getElementById('q').value}\n`), 'the coloured text is the text being edited')
const box = (sel) => page.locator(sel).evaluate((e) => { const r = document.createRange(); r.selectNodeContents(e); const b = r.getClientRects()[0]; return [Math.round(b.left), Math.round(b.top)] })
const first = await box('#q-ed pre'), caret = await page.locator('#q').evaluate((ta) => { const b = ta.getBoundingClientRect(), c = getComputedStyle(ta); return [Math.round(b.left + parseFloat(c.paddingLeft)), Math.round(b.top + parseFloat(c.paddingTop))] })
check(Math.abs(first[0] - caret[0]) <= 1 && Math.abs(first[1] - caret[1]) <= 3, 'the coloured text sits exactly under the caret', `${first} vs ${caret}`)
await page.locator('#q').fill(`${await page.locator('#q').inputValue()}\n}`)
await page.locator('#q').press('Control+Enter')
await settled('q-status', 'err')
check((await page.locator('#q-ed .gutter .bad').count()) === 1, 'Ctrl+Enter runs the query, and the line of a parse error is marked in the gutter')
await page.locator('#ex-box summary').click()
check(!(await page.locator('#examples').isVisible()), 'the example queries collapse')
await page.locator('#ex-box summary').click()
check(await page.locator('#examples').isVisible(), 'and expand again')

// --- Create KG: write data, preview it, describe it, download it ---------------------
await page.locator('#mode-create').click()
await settled('d-status', 'ok')
check((await status('d-status')).includes('valid Turtle'), 'starter Turtle builds into a .rete in memory', await status('d-status'))
check(await page.locator('#side-create').isVisible() && !(await page.locator('#examples').isVisible()), 'Create KG has its own sidebar, without the query list')
check((await page.locator('#out svg g.n').count()) > 5 && (await page.locator('#out svg line').count()) === 11, 'Create KG draws the graph: one link per triple')
check((await page.locator('#d-ed pre .t-pn').count()) > 5, 'the Turtle is coloured too')
await shot('lab-create')
check(!(await shown('#d-card')) && !(await shown('#d-download')) && !(await shown('#d-example')) && !(await shown('#fmt')) && !(await shown('#my-name')) && await shown('#d-example-ttl') && await shown('#combine') && await shown('#d-query'), 'Create KG shows beginners the example, Combine with and Query this graph, not the rarer tools')
await page.locator('#all-opts').check()
check(await shown('#d-card') && await shown('#d-download') && await shown('#fmt') && await shown('#csv'), 'All options shows the rest')
await page.locator('#views [data-view=table]').click()
check((await page.locator('#out tbody tr').count()) === 11, 'and lists its triples')
await page.locator('#views [data-view=classes]').click()
const byClass = await page.locator('#out .byclass section').evaluateAll((all) => all.map((sec) => ({ name: sec.querySelector('h3').textContent, rows: sec.querySelectorAll('tbody tr').length, cols: sec.querySelectorAll('thead th').length })))
check(byClass.length === 1 && byClass[0].name.startsWith('schema:Recipe') && byClass[0].rows === 1 && byClass[0].cols === 7, 'By class groups the rows by class, one column per property', JSON.stringify(byClass))
await shot('lab-by-class')
await page.locator('#views [data-view=graph]').click()

await page.locator('#d').fill('@prefix ex: <http://example.org/> .\nex:a ex:b')
await settled('d-status', 'err')
check((await status('d-status')).includes('not valid Turtle'), 'broken Turtle is reported while typing')

await page.locator('#d-example-ttl').click()
await settled('d-status', 'ok')
check((await status('d-status')).includes('valid Turtle'), 'the Turtle example loads from the sidebar')
await page.locator('#d-example').click()
await page.waitForFunction(() => document.querySelector('#d-status .pill').textContent.includes('JSON-LD'))
check((await status('d-status')).includes('valid JSON-LD'), 'JSON-LD example builds into a .rete in memory', await status('d-status'))

// dataset card
await page.locator('#d-card').click()
check((await page.locator('#card-fields [data-field]').count()) === 19, 'the card dialog offers the 18 curated fields of a rete card, and the example queries')
const field = (key) => page.locator(`#card-fields [data-field=${key}]`)
await field('title').locator('input').fill('Family recipes')
await page.keyboard.press('Enter')
check(await page.locator('#card-dlg').isVisible(), 'Enter in a field does not close the dialog')
await field('description').locator('textarea').fill('Recipes written in the course, with the course graph.')
await field('license').locator('input').fill('https://creativecommons.org/licenses/by/4.0/')
await field('creators').getByText('+ Add creator').click()
await field('creators').locator('input[name=name]').fill('Ada Lovelace')
await field('creators').locator('input[name=id]').fill('https://orcid.org/0000-0002-1825-0097')
await field('creators').getByText('+ Add creator').click()
await field('creators').locator('input[name=name]').nth(1).fill('Charles Babbage')
for (const [n, name] of ['Swiss Data Science Center', 'EPFL'].entries()) {
  await field('publisher').getByText('+ Add organization').click()
  await field('publisher').locator('input[name=name]').nth(n).fill(name)
}
for (const word of ['recipes', 'course']) {
  await field('keywords').locator('input').fill(word)
  await page.keyboard.press('Enter')
}
check((await field('keywords').locator('.chip').allInnerTexts()).map((t) => t.replace('✕', '').trim()).join() === 'recipes,course', 'a keyword is added with Enter and shown below the field')
await field('theme').locator('input').fill('not an IRI')
await page.keyboard.press('Enter')
const seen = await page.locator('#card-preview').innerText()
check(['Family recipes', 'Ada Lovelace', 'Charles Babbage', 'ORCID', 'Organizations', 'EPFL', 'recipes', 'creativecommons.org/licenses/by/4.0'].every((t) => seen.includes(t)), 'the preview on the right shows the card as it is filled', seen.replace(/\n+/g, ' / ').slice(0, 300))
await page.locator('#card-save').click()
check((await page.locator('#card-err').innerText()).includes('theme'), 'the engine checks the card: a theme that is not an IRI is refused', await page.locator('#card-err').innerText())
await field('theme').locator('.chip button').click()
await field('theme').locator('input').fill('http://publications.europa.eu/resource/authority/data-theme/AGRI')
await page.keyboard.press('Enter')
// a query written in the form
await field('example_queries').locator('[name=ex-new]').click()
await field('example_queries').locator('[name=ex-title]').fill('All recipes')
await field('example_queries').locator('[name=ex-query]').fill('SELECT ?r WHERE { ?r a <https://schema.org/Recipe> }')
await field('example_queries').locator('[name=ex-add]').click()
check((await field('example_queries').locator('.eq li').count()) === 1 && (await page.locator('#card-preview .qs').innerText()).includes('All recipes'), 'a SPARQL query can be added in the form')
check(!(await page.locator('#card-fields').innerText()).includes('null') && await page.locator('#card-preview .cv').evaluate((cv) => cv.scrollWidth <= cv.clientWidth + 1), 'the form and the preview keep their shape')
await page.locator('#card-fields').evaluate((f) => f.scrollTo(0, 0))
await shot('lab-card')
// the same card as YAML, in step with the form in both directions
await page.locator('#card-tab-yaml').click()
const yaml = await page.locator('#card-yaml').inputValue()
check(yaml.includes('title: Family recipes') && /creators:\n  - name: Ada Lovelace\n    orcid: https:\/\/orcid\.org/.test(yaml) && /keywords:\n  - recipes\n  - course/.test(yaml) && /publisher:\n  name: Swiss Data Science Center/.test(yaml) && /extra:\n  organizations:\n    - name: EPFL/.test(yaml), 'the card dialog shows the form as YAML', yaml.split('\n').slice(2, 14).join(' / '))
await shot('lab-card-yaml')
await page.locator('#card-yaml').fill(`${yaml}version: "2.0"\nkeywords: [recipes, course, playground]\n`)
await page.locator('#card-tab-form').click()
check((await page.locator('#card-err').innerText()).includes('keywords is given twice'), 'a YAML mistake is reported with its line and keeps you on the YAML tab', await page.locator('#card-err').innerText())
await page.locator('#card-yaml').fill(yaml.replace(/keywords:\n  - recipes\n  - course/, 'keywords: [recipes, course, playground]') + 'version: "2.0"\n')
check((await page.locator('#card-preview .cv-head .tags').innerText()).includes('v2.0'), 'the preview follows the YAML as it is typed')
await page.locator('#card-tab-form').click()
check((await field('version').locator('input').inputValue()) === '2.0' && (await field('keywords').locator('.chip').count()) === 3 && (await field('creators').locator('input[name=id]').first().inputValue()).includes('orcid.org') && (await field('publisher').locator('input[name=name]').count()) === 2, 'and what is typed in YAML fills the form')
await field('version').locator('input').fill('')
await field('keywords').locator('.chip button').nth(2).click()
await field('example_queries').locator('.eq li button').click()
await page.locator('#card-save').click()
await page.waitForFunction(() => document.getElementById('my-name').textContent === 'Family recipes')
check(!(await page.locator('#card-dlg').isVisible()) && (await page.locator('#card-meta').innerText()).startsWith('8 of 18'), 'a saved card names the graph', await page.locator('#card-meta').innerText())

await page.locator('#combine').selectOption('builtin')
await page.waitForFunction(() => document.querySelector('#d-status .txt').textContent.includes('from Recipes'))
const [download] = await Promise.all([page.waitForEvent('download'), page.locator('#d-download').click()])
const file = readFileSync(await download.path())
check(file.subarray(0, 4).toString('latin1') === 'RETE', 'the graph in memory downloads as a .rete file')
const card = await page.evaluate(async (b64) => (await rete.open(Uint8Array.from(atob(b64), (c) => c.charCodeAt(0)))).card(), file.toString('base64'))
check(card.title === 'Family recipes' && card.creators.length === 2 && card.creators[0].orcid.includes('orcid.org') && card.publisher.name === 'Swiss Data Science Center' && card.extra.organizations[0].name === 'EPFL' && card.keywords.length === 2 && card.triple_count === 814, 'the downloaded .rete carries the card', JSON.stringify(card).slice(0, 200))
// The text downloads must hold the same graph: rebuild each one in the page and count its triples.
const rebuilt = async (button, format) => {
  const [text_file] = await Promise.all([page.waitForEvent('download'), page.locator(button).click()])
  const text = readFileSync(await text_file.path(), 'utf8')
  const quads = await page.evaluate(async ([t, f]) => (await rete.open(await rete.build(t, f))).info().quads, [text, format]).catch((e) => String(e))
  return { name: text_file.suggestedFilename(), quads, text }
}
const ttl = await rebuilt('#d-ttl', 'ttl')
check(ttl.name.endsWith('.ttl') && ttl.quads === 814 && ttl.text.includes('@prefix schema:'), 'the graph downloads as Turtle with all 814 triples', `${ttl.name}: ${ttl.quads}`)
const jsonld = await rebuilt('#d-jsonld', 'jsonld')
check(jsonld.name.endsWith('.jsonld') && jsonld.quads === 814, 'and as JSON-LD with all 814 triples', `${jsonld.name}: ${jsonld.quads}`)
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
await runQuery()
await page.waitForFunction(() => document.querySelectorAll('#out tbody tr').length === 4, null, { timeout: 10000 }).catch(() => {})
check((await page.locator('#out tbody tr').count()) === 4, 'the written recipe joins the course graph: 4 labelled ingredients', await status('q-status'))

// keep the query as an example: sidebar and card
await page.locator('#add-example').click()
await page.locator('#ex-title').fill('Ingredients of my salad')
await page.locator('#ex-save').click()
check((await page.locator('#examples .mine-ex').count()) === 1, 'a query can be kept as an example in the sidebar')
await shot('lab-own-recipe')
await page.waitForTimeout(600) // the graph is rebuilt with the new card
await page.locator('#datasets li.on .dl [data-as=card]').click()
const shownCard = await page.locator('#info-body').innerText()
check(shownCard.includes('Family recipes') && shownCard.includes('Ingredients of my salad') && shownCard.includes('EPFL'), 'and it is written into the card of the graph', shownCard.slice(0, 200))
await page.locator('#info-dlg button').click()
await page.locator('#mode-create').click()
await page.locator('#d-card').click()
await page.locator('#card-tab-yaml').click()
const withQuery = await page.locator('#card-yaml').inputValue()
check(/example_queries:\n  - \|-?\n    # Ingredients of my salad\n    PREFIX schema:/.test(withQuery), 'the YAML lists the example query as a block of text', withQuery.split('\n').slice(-12, -6).join(' / '))
await page.locator('#card-tab-form').click()
await page.locator('#card-dlg button[value=cancel]').click()
await page.locator('#mode-query').click()
const side = await rebuilt('#datasets li:first-child .dl [data-as=ttl]', 'ttl')
check(side.name === 'recipes.ttl' && side.quads === 807, 'any graph in the sidebar downloads as Turtle too', `${side.name}: ${side.quads}`)

await page.locator('#mode-create').click()
await page.locator('#d-new').click()
check(await page.locator('#confirm-dlg').isVisible(), 'New empty graph asks before clearing the text and the card')
await page.locator('#confirm-ok').click()
await page.waitForFunction(() => document.getElementById('my-meta').textContent.startsWith('Not built'))
check((await page.locator('#d').inputValue()) === '' && await page.locator('#d-query').isDisabled() && (await page.locator('#my-name').innerText()) === 'My graph', 'and then starts from nothing')

// --- Validate KG: SHACL shapes against a graph ------------------------------------
await page.locator('#mode-validate').click()
check((await pill('s-status')) === 'not run' && (await page.locator('#out .empty').innerText()).includes('Press Validate'), 'Validate KG checks nothing until Validate is pressed')
await page.locator('#s-run').click()
await settled('s-status', 'ok')
check(await page.locator('#side-validate').isVisible() && (await page.locator('#out .verdict').innerText()).includes('Conforms'), 'Validate KG: the recipe graph conforms to the course shapes', await status('s-status'))
check((await page.locator('#s-ed pre .t-kw').count()) > 5 && (await page.locator('#s-ed .gutter div').count()) === (await page.locator('#s').inputValue()).split('\n').length, 'the shapes editor has colours and line numbers')
check(!(await page.locator('#buggy').isVisible()), 'the broken files start collapsed')
await page.locator('#bug-box summary').click()
for (const bug of await page.locator('#buggy button').all()) {
  const id = await bug.getAttribute('data-id'), want = Number(/: (\d+) expected/.exec(await bug.getAttribute('title'))[1])
  await bug.click()
  await notRun('s-status')
  await page.locator('#s-run').click()
  await page.waitForFunction((i) => document.getElementById('on-label').textContent.includes(`report on ${i} `), id)
  const got = await page.locator('#out tbody tr').count()
  check(got === want, `${id} gives the ${want} expected SHACL result${want === 1 ? '' : 's'}`, `got ${got}: ${await status('s-status')}`)
}
// the last one, b11, breaks several shapes: each is highlighted, and the cursor is on the first
const pointed = await page.evaluate(() => {
  const ta = document.getElementById('s'), line = ta.value.slice(0, ta.selectionStart).split('\n').length
  const hits = [...document.querySelectorAll('#s-ed .gutter .hit')].map((d) => Number(d.textContent))
  return { line, hits, text: ta.value.split('\n')[line - 1], focused: document.activeElement === ta, bands: document.querySelectorAll('#s-ed pre .band').length, visible: ta.scrollTop < (line - 1) * 20.15 }
})
check(pointed.bands > 1 && pointed.hits[0] === pointed.line && /^recsh:\S+ a sh:/.test(pointed.text) && pointed.focused && pointed.visible, 'picking a broken file highlights the shapes it breaks and puts the cursor on the first', JSON.stringify(pointed))
await shot('lab-validate')
const layers = await page.evaluate(() => ({ band: getComputedStyle(document.querySelector('#s-ed pre .band')).zIndex, shown: document.elementFromPoint(...(() => { const b = document.querySelector('#s-ed pre .band').getBoundingClientRect(); return [b.left + 60, b.top + 8] })()).id }))
check(layers.band === '-1' && layers.shown === 's', 'the highlight sits behind the text', JSON.stringify(layers))

// layout: scrollbars above and below a wide table, a divider to drag, a sidebar to hide
const bars = await page.evaluate(() => { const hs = document.getElementById('hscroll'), out = document.getElementById('out'); hs.scrollLeft = 120; return new Promise((done) => setTimeout(() => done({ shown: !hs.hidden, wide: out.scrollWidth > out.clientWidth, follows: out.scrollLeft }), 100)) })
check(bars.shown && bars.wide && bars.follows === 120, 'a wide table has a scrollbar above it that moves the table', JSON.stringify(bars))
await page.evaluate(() => { document.getElementById('out').scrollLeft = 0 })
const width = () => page.locator('.pane.edit').evaluate((e) => Math.round(e.getBoundingClientRect().width))
const before = await width(), handle = await page.locator('#split').boundingBox()
await page.mouse.move(handle.x + 4, handle.y + 300)
await page.mouse.down()
await page.mouse.move(handle.x + 4 - 150, handle.y + 300, { steps: 5 })
await page.mouse.up()
check(Math.abs((await width()) - (before - 150)) <= 3, 'the divider between editor and results can be dragged', `${before} -> ${await width()}`)
await page.locator('#split').focus()
await page.keyboard.press('ArrowRight')
check(Math.abs((await width()) - (before - 118)) <= 3, 'and moved with the arrow keys')
await page.locator('#split').dblclick()
check(Math.abs((await width()) - before) <= 3, 'a double-click puts it back')
await page.locator('#side-toggle').click()
check(!(await page.locator('.side').isVisible()) && (await width()) > before + 100, 'the sidebar collapses and gives its room to the panes')
await page.locator('#side-toggle').click()
check(await page.locator('.side').isVisible() && Math.abs((await width()) - before) <= 3, 'and comes back')

await page.locator('#out tbody tr').nth(1).click()
const one = await page.evaluate(() => ({ bands: document.querySelectorAll('#s-ed pre .band').length, text: document.getElementById('s').value.split('\n')[Number(document.querySelector('#s-ed .gutter .hit').textContent) - 1] }))
check(one.bands === 1 && one.text.startsWith('recsh:'), 'clicking a result points at its shape', JSON.stringify(one))
await page.locator('#views [data-view=cards]').click()
check((await page.locator('#out .card').count()) === 9, 'the report reads as cards too')
await page.locator('#views [data-view=table]').click()
const [reportFile] = await Promise.all([page.waitForEvent('download'), page.locator('#csv').click()])
const reportCsv = readFileSync(await reportFile.path(), 'utf8')
check(reportCsv.startsWith('severity,focus,message,path,value,shape,constraint\n') && reportCsv.includes('gazpacho'), 'the report downloads as CSV', reportCsv.slice(0, 120))
const shapes = await page.locator('#s').inputValue()
await page.locator('#s').fill(`${shapes}\nrecsh:Broken a sh:NodeShape ; sh:targetClass`)
check((await pill('s-status')) === 'not run' && await page.locator('#out.stale').count() === 1, 'typing does not validate: the last report stays, dimmed')
await page.locator('#s').press('Control+Enter')
await settled('s-status', 'err')
await page.waitForFunction(() => document.querySelector('#s-status .pill').textContent.includes('shapes not valid'))
check((await page.locator('#s-ed .gutter .bad').count()) === 1 && await page.locator('#out.stale').count() === 1, 'shapes that do not parse are reported with their line')
await page.locator('#s-minimal').click()
await page.locator('#s-run').click()
await page.waitForFunction(() => /result|conforms/.test(document.querySelector('#s-status .pill').textContent))
check((await page.locator('#s').inputValue()).includes('ex:RecipeShape') && (await page.locator('#out tbody tr').count()) > 0, 'a small example shape finds the missing fields of the broken file', await status('s-status'))

// --- open a .rete by URL ----------------------------------------------------------
await page.locator('#mode-query').click()
await page.locator('#url').fill(reteUrl)
await page.locator('#url-form button').click()
await page.waitForFunction(() => (document.querySelector('#datasets li.on small') || {}).textContent?.includes('URL'), null, { timeout: 10000 }).catch(() => {})
check((await page.locator('#datasets li.on small').innerText()).includes('URL'), 'a .rete file opens from a URL and becomes the queried graph', await page.locator('#add-msg').innerText())

// with All options on, every sidebar fits its width and scrolls only vertically
const sides = []
for (const mode of ['create', 'validate', 'query']) {
  await page.locator(`#mode-${mode}`).click()
  sides.push(await page.locator('.side').evaluate((s, m) => ({ m, fits: s.scrollWidth <= s.clientWidth, x: getComputedStyle(s).overflowX, w: `${s.scrollWidth}/${s.clientWidth}` }), mode))
}
check(sides.every((s) => s.fits && s.x === 'hidden'), 'every sidebar fits its width, with no horizontal scrolling', JSON.stringify(sides))

await page.goto('about:blank')
await page.goto(`${pathToFileURL(join(root, 'docs/index.html')).href}#view=cards&q=${encodeURIComponent('ASK { ?s ?p ?o }')}`)
await graphLoaded()
check((await page.locator('#q').inputValue()) === 'ASK { ?s ?p ?o }' && (await pill('q-status')) === 'not run', 'a link restores the query without running it')
check(await page.locator('#all-opts').isChecked() && await shown('#share'), 'All options stays on after a reload')
await runQuery()
check((await page.locator('#out .bool').innerText()) === 'true', 'and Run answers it')

await page.locator('#mode-guide').click()
check(await page.locator('#guide').isVisible() && !(await page.locator('.side').isVisible()) && (await page.locator('#guide h3').count()) === 5 && (await page.locator('#guide #ai').count()) === 1, 'the Guide tab holds the five exercises and the AI disclosure, in the same file')
await shot('lab-guide')
await page.locator('#guide [data-go=validate]').click()
check(await page.locator('#s').isVisible(), 'an exercise leads to its tab')
await page.goto('about:blank')
await page.goto(`${pathToFileURL(join(root, 'docs/index.html')).href}#tab=guide`)
await page.waitForFunction(() => !document.getElementById('guide').hidden)
check(await page.locator('#guide').isVisible(), 'a link can open the Guide')
check(await page.evaluate(() => [...document.querySelectorAll('img, link[href], script[src]')].length) === 0, 'the page loads no other file')

check(errors.length === 0, 'no uncaught errors in the page', errors.join('\n     '))
await browser.close()
server.close()
if (failures) {
  console.error(`${failures} check(s) failed`)
  process.exit(1)
}
