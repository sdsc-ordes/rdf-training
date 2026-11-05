import { defineShikiSetup } from '@slidev/types'
import type { Element, ElementContent } from 'hast'
import { PREFIXES } from './prefixes'

const USED = /(?<![\w:/#.-])([A-Za-z][\w-]*):(?=[\w-])/g
const DECLARED = /^\s*(?:@prefix|PREFIX)\s+([\w-]*):/gim
const PREFIX_LINE = /^\s*(?:@prefix|PREFIX|@base|BASE)\b/i
const text = (value: string): ElementContent => ({ type: 'text', value })

// Turtle and SPARQL blocks: grey out prefix lines, and show (greyed, linked) the
// declarations of prefixes the snippet uses but doesn't declare. The added lines
// sit outside <code>, so line numbers and click-through highlights are unchanged.
const prefixes = {
  name: 'course:prefixes',
  line(node: Element, line: number) {
    if (!['turtle', 'sparql'].includes(this.options.lang)) return
    if (PREFIX_LINE.test(this.source.split('\n')[line - 1] ?? '')) this.addClassToHast(node, 'prefix-line')
  },
  pre(node: Element) {
    const lang = this.options.lang
    if (lang !== 'turtle' && lang !== 'sparql') return
    const declared = new Set([...this.source.matchAll(DECLARED)].map(m => m[1]))
    const missing = [...new Set([...this.source.matchAll(USED)].map(m => m[1]))]
      .filter(p => p in PREFIXES && !declared.has(p))
      .sort()
    if (!missing.length) return
    const [keyword, end] = lang === 'turtle' ? ['@prefix', ' .'] : ['PREFIX', '']
    node.children.unshift({
      type: 'element',
      tagName: 'div',
      properties: { class: 'code-prefixes' },
      children: missing.map(p => ({
        type: 'element',
        tagName: 'div',
        properties: {},
        children: [
          text(`${keyword} ${p}: `),
          { type: 'element', tagName: 'a', properties: { href: PREFIXES[p], title: PREFIXES[p], target: '_blank', rel: 'noopener' }, children: [text(`<${PREFIXES[p]}>`)] },
          text(end),
        ],
      })),
    })
  },
}

export default defineShikiSetup(() => ({ transformers: [prefixes] }))
