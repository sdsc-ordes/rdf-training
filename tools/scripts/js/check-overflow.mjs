// Flag slides whose content overflows or runs into the footer. Run after `npm run build`:
//   node tools/scripts/js/check-overflow.mjs [deck ...]   (default: every built deck)
import { createServer } from 'node:http'
import { readFile, readdir } from 'node:fs/promises'
import { extname, join } from 'node:path'
import { chromium } from 'playwright-chromium'

const root = new URL('../../../_site', import.meta.url).pathname
const base = process.env.SITE_BASE ?? '/rdf-training/'
const types = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.png': 'image/png', '.json': 'application/json' }

const server = createServer(async (req, res) => {
  let path = decodeURIComponent(new URL(req.url, 'http://x').pathname)
  if (path.startsWith(base)) path = `/${path.slice(base.length)}`
  if (path.endsWith('/')) path += 'index.html'
  try {
    const body = await readFile(join(root, path))
    res.writeHead(200, { 'content-type': types[extname(path)] ?? 'application/octet-stream' })
    res.end(body)
  } catch {
    res.writeHead(404)
    res.end()
  }
}).listen(0)

// Runs in the page: what is wrong with this slide? (v-click elements are hidden but keep their space)
function inspect(el) {
  const out = []
  const box = el.getBoundingClientRect()
  if (el.scrollHeight > el.clientHeight + 2) out.push('content taller than the slide')
  if (el.scrollWidth > el.clientWidth + 2) out.push('content wider than the slide')
  if ([...el.querySelectorAll('pre')].some(pre => pre.scrollWidth > pre.clientWidth + 2)) out.push('code line too long')
  if (!/\b(cover|intro|section)\b/.test(el.className)) {
    // measure content, not layout containers (two-column grids stretch to full height)
    const content = el.querySelectorAll('h1, h2, h3, p, li, pre, table, img, svg, blockquote, .spo, .sdsc-feature, .sdsc-takeaway, .legend, .slidev-vclick-target')
    const bottom = Math.max(0, ...[...content].map(c => c.getBoundingClientRect().bottom))
    if (bottom > box.bottom - box.height * 0.075) out.push('content reaches the footer')
  }
  return { title: el.querySelector('h1')?.textContent?.trim() ?? '', out }
}

const decks = process.argv.length > 2 ? process.argv.slice(2) : await readdir(join(root, 'decks'))
const browser = await chromium.launch({ executablePath: process.env.SLIDEV_CHROMIUM })
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } })
let problems = 0

for (const deck of decks) {
  await page.goto(`http://localhost:${server.address().port}${base}decks/${deck}/#/1`, { waitUntil: 'networkidle' })
  await page.waitForTimeout(2000) // fonts
  // only nearby slides are mounted, so read the total from the SDSC footer ("2 / 45") of an early content slide
  let total = 0
  for (let n = 2; !total && n <= 6; n++) {
    await page.evaluate((no) => { location.hash = `#/${no}` }, n)
    await page.waitForTimeout(300)
    const footer = await page.$('.sdsc-footer-page')
    if (footer) total = Number((await footer.textContent()).split('/')[1])
  }
  let issues = 0
  for (let n = 1; n <= total; n++) {
    await page.evaluate((no) => { location.hash = `#/${no}` }, n)
    const selector = `.slidev-page-${n}`
    await page.waitForFunction((s) => { const p = document.querySelector(s); return p && getComputedStyle(p).display !== 'none' }, selector)
    await page.waitForTimeout((await page.$(`${selector} .mermaid, ${selector} svg`)) ? 1200 : 250)
    const { title, out } = await page.$eval(`${selector} .slidev-layout`, inspect)
    for (const reason of out) console.log(`${deck} ${n} "${title}": ${reason}`)
    issues += out.length
  }
  console.log(`${deck}: ${total} slides, ${issues ? `${issues} issue(s)` : 'ok'}`)
  problems += issues
}

await browser.close()
server.close()
process.exit(problems ? 1 : 0)
