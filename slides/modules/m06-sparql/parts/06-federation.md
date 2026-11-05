---
class: code-small
minutes: 2
---

# Asking another graph: federation

<<< @/../hands-on/h3-query/queries/q11-country-codes.rq sparql {11|all}

- `SERVICE` sends part of the query to another endpoint, here Wikidata
- Your query then depends on the other endpoint's speed and uptime
- The Wikidata Query Service is moving from Blazegraph to QLever (2026)

<p class="fine">Sources: W3C SPARQL 1.1 · Wikidata WDQS 2026 · Bast & Buchhold 2017</p>

<!--
Try Wikidata-scale queries at qlever.dev. Check the endpoint URL before each course: the migration may change it.
This is query q11; it runs in the Comunica web client from hands-on 3.
-->
