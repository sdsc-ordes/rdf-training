# RETE lab

Sources of the lab published from `docs/`: a self-contained HTML page that runs SPARQL over
[rete](https://github.com/caviri/rete) files in the browser.

| File | Role |
|---|---|
| `build-rete.sh` | builds `docs/data/recipes.rete` from `src/data/` with the rete CLI, then calls `build-lab.mjs` |
| `build-lab.mjs` | inlines the engine, the graph, the worksheet queries, the course shapes, the broken H2 files and a world outline into `lab.html` → `docs/lab.html` |
| `lab.html` | the page template: Welcome, Create KG (Turtle/JSON-LD, graph preview, dataset card), Validate KG (SHACL) and Query KG (SPARQL; table, cards, map) |
| `check-lab.mjs` | browser checks of `docs/lab.html`; `--shots` rewrites `docs/img/` |

```sh
just rete         # bash src/rete/build-rete.sh
just check-rete   # node src/rete/check-lab.mjs
```

`RETE_VERSION` in `build-rete.sh` and `rete-graph` in `package.json` must be the same version.
Exercises and the AI disclosure are in `docs/index.html`.
