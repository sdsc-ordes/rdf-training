<script setup>
import { data } from './h2.data.ts'
</script>

# H2 · Generate, validate, repair

Let an LLM write recipes for the knowledge graph, then make them pass validation.

## 1. Generate · 8 min

Copy the prompt into your LLM chat and replace `CUISINE` with your group's cuisine.

<div class="language-text prompt"><button title="Copy" class="copy"></button><span class="lang">prompt</span><pre><code>{{ data.prompt }}</code></pre></div>

## 2. Validate · 8 min

<a :href="data.validate" target="_blank" rel="noopener">Open the validator ↗</a>
with the shapes and vocabulary filled in. Paste the LLM's Turtle at the end of the **Data Graph**.
The report updates as you type.

No LLM? <a :href="data.fallback" target="_blank" rel="noopener">Open an LLM's first attempt ↗</a> instead.

## 3. Repair · 10 min

Send the errors back to the LLM with this prompt. Stop after three rounds.

<div class="language-text prompt"><button title="Copy" class="copy"></button><span class="lang">prompt</span><pre><code>{{ data.fixPrompt }}</code></pre></div>

Note each type of error and how many rounds you needed.

## 4. Share

Paste your valid Turtle into the shared pad.

::: tip Stretch
- Remove the vocabulary from the data graph. Why does the vegan rule stop working?
- Validate the SHACL-SPARQL version of the rule (`data/shapes/recipes.shapes-sparql.ttl`) in the [EU ITB validator](https://www.itb.ec.europa.eu/shacl/any/upload).
:::
