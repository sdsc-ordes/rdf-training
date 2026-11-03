---
minutes: 3
---

# Linking names to IRIs

1. **Find candidates:** Wikidata search, OpenRefine reconciliation, or your own label index
2. **Let the LLM choose,** using the surrounding text
3. **A person confirms** the uncertain ones

- "Fuji": apple variety, mountain or company?
- "Rocket": salad or spacecraft?

<div class="sdsc-takeaway">Never accept an identifier an LLM writes from memory: look it up.</div>

<!--
LLMs produce plausible but wrong Wikidata Q-IDs. This course checks every Wikidata ID it uses
against the Wikidata API.
-->
