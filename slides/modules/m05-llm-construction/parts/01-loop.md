---
minutes: 3
---

# Generate, validate, repair

```mermaid
graph LR
  P[Prompt with<br/>schema card] --> L[LLM writes Turtle]
  L --> V{Valid?<br/>SHACL}
  V -- "no · max 3 rounds" --> R[Send the report back]
  R --> L
  V -- yes --> H[Human review]
  H --> K[(Knowledge graph)]
```

<div class="sdsc-takeaway">LLMs draft, SHACL checks, humans decide.</div>

<!--
The same loop works for ontology drafting, entity extraction from text and synthetic test data.
Cap the retries; if it still fails, a person looks at it. Label synthetic data as synthetic.
-->
