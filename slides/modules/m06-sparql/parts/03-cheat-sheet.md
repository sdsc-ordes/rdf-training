---
layout: two-cols-header
minutes: 3
---

# SPARQL cheat sheet

::left::

## Patterns

- `?x` is a variable
- `.` `;` `,` and `a` work as in Turtle
- `PREFIX` defines shorthands
- `#` starts a comment
- `SELECT *` returns every variable

::right::

## Keywords

<table class="compact">
  <tbody>
    <tr><td><code>OPTIONAL</code></td><td>keep rows without a match</td></tr>
    <tr><td><code>FILTER</code>, <code>NOT EXISTS</code></td><td>keep or drop rows</td></tr>
    <tr><td><code>UNION</code>, <code>MINUS</code></td><td>combine or subtract patterns</td></tr>
    <tr><td><code>/</code> <code>*</code> <code>+</code> <code>^</code></td><td>property paths</td></tr>
    <tr><td><code>GROUP BY</code>, <code>COUNT</code>, <code>HAVING</code></td><td>aggregate</td></tr>
    <tr><td><code>BIND</code>, <code>VALUES</code>, <code>COALESCE</code></td><td>compute and fill in</td></tr>
    <tr><td><code>ORDER BY</code>, <code>LIMIT</code></td><td>sort and cut</td></tr>
  </tbody>
</table>

<!--
Only the triple patterns borrow Turtle syntax; a SPARQL query as a whole is not valid Turtle.
-->
