---
layout: two-cols-header
minutes: 4
---

# Demo · vegetarian and gluten-free

::left::

## Vector RAG

Retrieves recipe texts that mention "vegetarian" or "salad". The anchovy is only in the Worcestershire product sheet, which never matches the question.

::right::

## Knowledge graph

Query q09 returns **Fondue, Rösti, Chana masala**, and can say why the others drop out:

<Triple s="Caesar salad" p="has ingredient" o="Worcestershire sauce" />
<Triple s="Worcestershire sauce" p="contains" o="anchovy" />
<Triple s="Pad Thai" p="has ingredient" o="soy sauce" />
<Triple s="soy sauce" p="contains" o="wheat" />

<!--
Run the notebook demo (notebooks/03-graph-rag) in replay mode, or show q09 in Comunica.
The exclusion paths come from the property path rec:hasIngredient/rec:containsIngredient*.
-->

---
minutes: 3
---

# Demo · fact-check an LLM answer

"Pad Thai is vegan, gluten-free and Vietnamese, and quite spicy."

<table class="compact">
  <thead><tr><th>Claim</th><th>Checked against the KG</th><th>Result</th></tr></thead>
  <tbody>
    <tr><td>vegan</td><td>contains egg, and anchovy via fish sauce</td><td>contradicted</td></tr>
    <tr><td>gluten-free</td><td>soy sauce contains wheat</td><td>contradicted</td></tr>
    <tr><td>Vietnamese</td><td>cuisine is Thai</td><td>contradicted</td></tr>
    <tr><td>spicy</td><td>the graph says nothing about spiciness</td><td><b>unknown</b></td></tr>
  </tbody>
</table>

```sparql
ASK { recipe:pad-thai rec:hasIngredient/rec:containsIngredient*/rec:hasAllergen allergen:gluten }
```

<!--
Each claim becomes a triple pattern; an ASK query checks it. "Unknown" is not "false":
the graph is open world, absence of a fact proves nothing.
-->
