# 38. Denser girth-5 graph than the best-known extremal number

**Target.** Find a graph on n vertices with girth at least 5 (no triangles, no 4-cycles) and more edges than the best-known lower bound for ex(n; {C3,C4}), for a specific n where the extremal number is not determined. ex(n; {C3,C4}) is the maximum number of edges in an n-vertex graph of girth >= 5; it is known exactly only for scattered n.

**What counts as a win.** One explicit girth-5 graph on n vertices with more edges than the current best-known construction improves the lower bound for ex(n; {C3,C4}) at that n (one-sided). If it meets the known upper bound it determines the extremal number.

**Checker (seconds).** Read adjacency (graph6) on n vertices. Verify girth >= 5: no triangles (A^2 and A share no nonzero off-diagonal support giving a triangle; triangle count 0) and no 4-cycles (for every pair of non-adjacent vertices, at most one common neighbor; equivalently the number of length-2 walks between distinct vertices <= 1). Count edges. O(n^3).

**Search plan.** Incidence-graph and generalized-polygon truncations; Cayley graphs over small groups screened for girth 5; add edges greedily to known extremal graphs while preserving the "at most one common neighbor" property; local search / tabu maximizing edges under the girth-5 constraint.

**Prior art (verify).** Best-known values and constructions for ex(n; {C3,C4}) are tabulated in the extremal-girth-5 literature (Garnick, Kwong, Lazebnik; Exoo's cage-and-girth pages) and match Moore-bound-type limits at special n. Re-verify the current best for the chosen n; several small n remain undetermined.

**Openness:** documented-open (verify). **Win-type:** found-object.
