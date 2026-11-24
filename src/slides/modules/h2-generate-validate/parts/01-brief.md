---
minutes: 17
---

# Hands-on 2 · Generate, validate, repair

Start from your two competency questions and the classes and properties from hands-on 1.

1. **Generate · 6 min:** ask an LLM for instance data and a SHACL shapes graph, both in Turtle
2. **Validate · 5 min:** paste the shapes and the data into [shacl-playground.zazuko.com](https://shacl-playground.zazuko.com)
3. **Repair · 6 min:** send the errors back to the LLM, at most 3 rounds. Was the data wrong, or the shape?

```text
My competency questions: ...   My classes and properties: ...
Write Turtle instance data for a few recipes that answer these questions,
and a SHACL shapes graph that checks the data. Output only Turtle.
```

<div class="exercise-meta">
  <span><b>Pairs · 17 min</b> · No LLM? Write two recipes and one shape by hand.</span>
</div>

<!--
Pairs keep their hands-on 1 model, so every pair validates a different graph.
If the LLM writes shapes that accept everything, ask for sh:minCount and sh:datatype on each property.
A failing result means bad data or a bad shape; both happen, and deciding which is the point of step 3.
Count rounds per pair on the board. Toy data only: fine for any chat tool.
-->
