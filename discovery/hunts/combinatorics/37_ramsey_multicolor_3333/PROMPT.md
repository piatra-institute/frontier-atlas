# 37. Improve the lower bound for the 4-color triangle Ramsey number

**Target.** Find a 4-coloring of the edges of the complete graph K_N with no monochromatic triangle, for N at least the current best-known lower bound of R(3,3,3,3) (the 4-color Ramsey number for triangles). Such a coloring proves R(3,3,3,3) >= N+1. The best-known bounds have a wide gap (roughly 51 <= R(3,3,3,3) <= 62, verify), and the lower bound is under-tested.

**What counts as a win.** One explicit 4-edge-coloring of K_N with every color class triangle-free, where N+1 exceeds the current tabulated lower bound, improves the lower bound (one-sided). Equivalently: N vertices partitioned into 4 triangle-free graphs whose union is K_N.

**Checker (seconds).** Read the edge coloring (an N x N symmetric matrix of colors 1..4). Verify it colors every edge, and each of the 4 color classes is triangle-free (triangle count 0 per class). O(N^3).

**Search plan.** Cyclic / cyclotomic colorings over Z_N (partition nonzero residues into 4 sum-free-ish classes); Cayley colorings over small groups; SAT with symmetry breaking (variables = color per edge, clauses forbidding monochromatic triangles); local search minimizing monochromatic triangles; product / blow-up of smaller good colorings.

**Prior art (verify).** S. Radziszowski, "Small Ramsey Numbers," EJC dynamic survey DS1, tabulates multicolor Ramsey bounds including R(3,3,3,3). Re-verify the current lower bound before claiming; multicolor lower bounds have improved recently via SAT and cyclotomic constructions.

**Openness:** documented-open. **Win-type:** found-object.
