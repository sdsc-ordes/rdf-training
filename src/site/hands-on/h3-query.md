<script setup>
import { data } from './h3.data.ts'
</script>

# H3 · Query the recipe graph

Each query runs in the Comunica web client on the course KG. Predict the answer before you run it, then change the query.

**Fallback:** open the [AtomGraph SPARQL Playground](https://atomgraph.github.io/SPARQL-Playground/), paste [kg.ttl](/files/kg.ttl){target="_self"} as data, then paste the query.

## q01 · All recipes

<a :href="data.q01" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q01-recipes.rq{sparql}

## q02 · Names in Italian, else English

<a :href="data.q02" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q02-italian-names.rq{sparql}

## q03 · Claimed diets

<a :href="data.q03" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q03-diets.rq{sparql}

## q04 · Under 30 minutes <Badge text="core" />

<a :href="data.q04" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q04-quick.rq{sparql}

## q05 · Hidden dairy

<a :href="data.q05" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q05-dairy.rq{sparql}

## q06 · Grown in Spain

<a :href="data.q06" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q06-grown-in-spain.rq{sparql}

## q07 · Recipes per cuisine

<a :href="data.q07" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q07-per-cuisine.rq{sparql}

## q08 · Many allergens

<a :href="data.q08" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q08-many-allergens.rq{sparql}

## q09 · Vegetarian and gluten-free <Badge text="core" />

<a :href="data.q09" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q09-vegetarian-gluten-free.rq{sparql}

## q10 · Any peanuts?

<a :href="data.q10" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q10-peanuts.rq{sparql}

## q11 · Ask Wikidata

<a :href="data.q11" target="_blank" rel="noopener">Run ↗</a>

<<< @/../hands-on/h3-query/queries/q11-country-codes.rq{sparql}
