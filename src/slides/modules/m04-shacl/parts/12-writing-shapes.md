---
minutes: 2
---

# Tools for writing shapes

<table class="compact">
  <thead><tr><th>Need</th><th>Tools</th></tr></thead>
  <tbody>
    <tr><td>Model classes and shapes in a web editor</td><td>TopBraid EDG (now TQ Data Foundation), metaphactory · both commercial</td></tr>
    <tr><td>Write shapes in a spreadsheet</td><td>SHACL Play! Excel template, DCTAP with tap2shacl (beta)</td></tr>
    <tr><td>Generate from a YAML model</td><td>LinkML (<code>gen-shacl</code>)</td></tr>
    <tr><td>Generate from an OWL ontology</td><td>Astrea (research prototype), SHACL Play! conversion rules</td></tr>
    <tr><td>Derive from existing data</td><td>sheXer, QSE, SHACL Play!</td></tr>
    <tr><td>Document and draw shapes</td><td>SHACL Play!: documentation pages and UML diagrams</td></tr>
    <tr><td>Data entry forms from shapes</td><td>shacl-form</td></tr>
  </tbody>
</table>

<p class="fine">Sources: TopBraid EDG · metaphactory · SHACL Play! · DCTAP · LinkML · Cimmino et al. 2020 · Fernández-Álvarez et al. 2022 · Rabbani et al. 2023 · shacl-form</p>

<!--
Most shapes are written by hand in Turtle, as in this course. These tools help with a first draft, or when domain experts work in spreadsheets.
Generated shapes are a draft: shapes derived from data describe the data as it is, errors included. Review them before you validate with them.
TopBraid EDG is documented as TQ Data Foundation from version 9.2; every class you create there is also a node shape.
Astrea (ESWC 2020) has not changed since 2023. SHACL Play! ships rules that convert OWL to SHACL (open, semi-closed and closed variants).
DCTAP is a DCMI specification for application profiles in a spreadsheet, 12 columns; tap2shacl converts it and is still in beta.
QSE is built for very large graphs; SHACL Play!'s generator does not handle Wikidata-sized endpoints.
Also: the SHACL4Protégé plugin (edit and validate SHACL inside Protégé), the Mentor extension for VS Code. LLMs can draft shapes too (module 5).
-->
