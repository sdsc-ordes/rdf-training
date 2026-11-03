---
class: code-small
minutes: 2
---

# Asking another graph: federation

<<< @/../hands-on/h3-query/queries/q11-country-codes.rq sparql {11|all}

- `SERVICE` sends part of the query to another endpoint, here Wikidata
- Powerful and fragile: you depend on someone else's speed and uptime
- The Wikidata Query Service is moving from Blazegraph to QLever (2026)

<!--
Try Wikidata-scale queries at qlever.dev. Check the endpoint URL before each course: the migration may change it.
This is query q11; it runs in the Comunica web client from hands-on 3.
-->
