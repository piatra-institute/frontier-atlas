# Smaller 5-chromatic unit-distance graph than the record

**Find.** A 5-chromatic unit-distance graph in the plane with fewer vertices than the smallest published such graph.

**What counts as a win (one-sided).** One unit-distance graph, non-4-colorable, with vertex count below the current record. A single smaller graph beats the record; failure proves nothing.

**Checker (seconds).** Verify each edge realizes exact distance 1 in the appropriate number field, then verify non-4-colorability with a SAT solver, exporting a DRAT/LRAT proof of unsatisfiability for the 4-coloring instance; check the proof with an independent proof checker. Also confirm 5-colorability (an explicit 5-coloring) to pin the chromatic number.

**Search plan.** Prune known small 5-chromatic graphs: remove vertices/edges and re-test 4-colorability with SAT; search unions of Moser spindles and rotated copies at rational-cosine angles for compact non-4-colorable cores; use unsatisfiable-core extraction to identify minimal subgraphs. Evolutionary trimming scored by vertex count subject to staying non-4-colorable.

**Prior art (verify).** After de Grey's original 1581-vertex 5-chromatic unit-distance graph (2018), the Polymath16 project reduced the vertex count substantially (to a few hundred). The minimum size is not settled and remains an active record. See de Grey (2018) and the Polymath16 project pages for the current smallest known graph (verify).
