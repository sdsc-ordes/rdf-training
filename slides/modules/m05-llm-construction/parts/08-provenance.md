---
minutes: 2
---

# Keep track of what the LLM made

```turtle
@prefix ex: <http://example.org/> .

ex:batch-17 a prov:Entity ;
    prov:wasGeneratedBy ex:run-17 .
ex:run-17 a prov:Activity ;
    prov:used ex:prompt-v3 ;
    prov:wasAssociatedWith ex:some-llm ;
    prov:endedAtTime "2026-11-03T10:15:00Z"^^xsd:dateTime .
```

- One named graph per batch, so you can find and remove it
- Review new classes, uncertain links and a sample of facts
- Keep confidential data out of consumer chat tools

<!--
PROV-O is the W3C provenance vocabulary. Record the model, the prompt version and the date.
-->
