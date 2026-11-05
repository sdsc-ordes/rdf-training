# H1 · Model the recipe domain

Sketch the classes and properties a recipe knowledge graph needs to answer five questions.

## The questions

1. Which recipes take less than 30 minutes?
2. What can I cook for a vegetarian, gluten-free guest?
3. Which recipes use ingredients grown in Spain?
4. Which recipes contain fish?
5. Which cuisine has the most vegan recipes?

## Steps

1. **Alone, 5 min:** underline the nouns (candidate classes) and verbs (candidate properties).
2. **In groups, 15 min:** fill the canvas below. Look for terms to reuse on [schema.org/Recipe](https://schema.org/Recipe).
3. **Optional:** ask your LLM for a class and property table for the same questions. What did it get right?
4. **10 min:** compare with the reference model.

## Canvas

| Class | Example | Reused from |
|---|---|---|
| Recipe | Rösti | schema.org |
| | | |

| Property | From | To | Reused from |
|---|---|---|---|
| has ingredient | Recipe | Food | — |
| | | | |

::: details Reference model
<<< @/../data/vocab/recipes.ttl{turtle}
:::

::: tip Stretch
Write your model in Turtle, starting from the [starter file](https://github.com/sdsc-ordes/rdf-training/blob/main/src/hands-on/h1-model/starter.ttl).
:::
