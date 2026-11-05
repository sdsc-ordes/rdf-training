---
minutes: 2
---

# The graph as a tool for agents

- An agent decides itself when to query the graph, and how often
- **MCP** (Model Context Protocol) servers expose a SPARQL endpoint as tools: list classes, run a query
- Shapes make good tool documentation: they say what exists and how it connects

<p class="fine">Sources: Anthropic 2024 · Graphwise GraphDB 11</p>

<!--
Triplestore vendors (e.g. GraphDB 11) and open-source projects offer SPARQL MCP servers;
2026 research evaluates agents that discover endpoints, explore schemas and write federated queries.
Use read-only access, timeouts and rate limits.
-->
