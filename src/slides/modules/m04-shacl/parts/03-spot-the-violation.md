---
class: code-small no-prefixes
minutes: 3
---

# Spot the violations

An LLM wrote this recipe. What will the validator say?

<<< @/../hands-on/h2-validate/buggy/b11-llm-first-attempt.ttl#pizza turtle

<div v-click>

<p class="code-label">The shapes it is checked against, one constraint each (from recipes.shapes.ttl):</p>

```turtle
recsh:Recipe-name      sh:path schema:name ;       sh:datatype rdf:langString .
recsh:Recipe-totalTime sh:path schema:totalTime ;  sh:datatype xsd:dayTimeDuration .
recsh:Recipe-cuisine   sh:path rec:cuisine ;       sh:minCount 1 .
```

</div>

<div class="flex gap-10 text-sm">
  <div v-click>① The name has no language tag</div>
  <div v-click>② <code>"25 min"</code> is text, not a duration</div>
  <div v-click>③ There is no <code>rec:cuisine</code></div>
</div>

<!--
First click: the property shapes behind the three results, cut down to the constraint that fails. Let the room compare each line with the data.
The full shapes also set counts, allowed languages and messages (src/data/shapes/recipes.shapes.ttl). Prefix lines are hidden on this slide so both listings fit.
Give the room a minute. Then reveal one by one. These are the exact results from the real validator.
-->
