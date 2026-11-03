---
minutes: 2
---

# Words are ambiguous, IRIs are not

- **One word, many things:** "Fuji" is an apple variety, a mountain and a company: three IRIs
- **Many words, one thing:** rocket, arugula and Rucola: one IRI, several labels
- **Class or individual?** Is "Fuji" all Fuji apples, or one cultivar? Let your questions decide

```turtle
food:rocket a rec:Vegetable ;
    skos:prefLabel "rocket"@en ;
    skos:altLabel "arugula"@en, "Rucola"@de .
```

<!--
LLMs and string matching both trip over homonyms; this is where entity linking (module 5) comes in.
-->
