---
minutes: 4
---

# Your turn: sentences to triples

> Robin is a data engineer who loves apples, especially Fuji.
>
> Fuji apples are grown in Spain and France, both countries in Europe.
>
> Robin teaches an RDF course in Zurich on 12 March 2025.

<div class="exercise-meta">
  <span><b>Pairs · 4 min</b> · one triple per sticky note</span>
</div>

<!--
Debrief questions: Is "Fuji" a thing or a value? Is "loves" the same relation as "favourite"?
How do you write the date so a computer can compare it? Who is the subject of "teaches"?
-->

---

# One possible answer

```turtle
@prefix ex: <http://example.org/> .

person:robin a schema:Person ;
    schema:jobTitle "Data engineer"@en ;
    ex:likes food:apple, food:fuji-apple .

food:fuji-apple rec:grownIn wd:Q29, wd:Q142 .    # Spain, France
wd:Q29 schema:containedInPlace wd:Q46 .          # Spain is in Europe
wd:Q142 schema:containedInPlace wd:Q46 .

ex:rdf-course a schema:Course ;
    schema:instructor person:robin ;
    schema:location wd:Q72 ;                      # Zurich
    schema:startDate "2025-03-12"^^xsd:date .
```

<!--
No single right answer. Note what we reused (schema.org, Wikidata) and what we invented (ex:likes).
-->
