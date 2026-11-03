---
minutes: 3
---

# Let the LLM fill JSON, let code write RDF

```json
{
  "@context": {
    "rec": "https://sdsc-ordes.github.io/rdf-training/vocab/recipes#",
    "food": "https://sdsc-ordes.github.io/rdf-training/id/food/",
    "hasIngredient": { "@id": "rec:hasIngredient", "@type": "@id" }
  },
  "@id": "https://sdsc-ordes.github.io/rdf-training/id/recipe/rosti",
  "hasIngredient": ["food:potato", "food:butter", "food:salt"]
}
```

- A JSON Schema constrains what the LLM may output (structured output)
- A JSON-LD `@context` turns plain JSON into triples
- Tools that do this: LinkML, OntoGPT (SPIRES)

<!--
Asking an LLM for Turtle directly works for a workshop; in production, structured JSON plus a
fixed context removes a whole class of syntax and prefix errors.
-->
