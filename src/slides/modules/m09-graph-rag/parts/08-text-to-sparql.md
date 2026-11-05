---
minutes: 3
---

# Family B: the LLM writes the query

```mermaid {scale: 0.68}
graph LR
  Q[Question] --> P[Prompt:<br/>schema card + prefixes<br/>+ example queries]
  P --> L[LLM writes SPARQL]
  L --> R{Runs?<br/>Results?}
  R -- "error or empty" --> L
  R -- yes --> A[Answer citing IRIs]
```

- The schema card can be generated from your SHACL shapes
- Answers are exact and traceable: every fact is a triple you can show
- Fragile when the LLM guesses IRIs or prefixes: give examples, and retry

<p class="fine">Sources: Emonet et al. 2024</p>

<!--
Our q01–q11 queries double as examples for few-shot prompting.
SIB's federated assistant (arXiv 2410.06062) checks generated queries against dataset descriptions before running them.
-->
