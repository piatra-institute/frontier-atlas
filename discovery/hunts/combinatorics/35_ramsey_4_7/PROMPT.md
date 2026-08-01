# 35. Improve the lower bound for R(4,7)

**Target.** Find a K4-free graph on N vertices with independence number at most 6, for N at least the current best-known lower bound of R(4,7). Such a graph proves R(4,7) >= N+1. The interval for R(4,7) is wide (roughly 49 <= R(4,7) <= 58, verify), so the lower bound is under-tested and improvable.

**What counts as a win.** One explicit K4-free graph on N vertices with no independent set of size 7, where N+1 exceeds the current tabulated lower bound, improves the lower bound for R(4,7) (one-sided).

**Checker (seconds).** Read adjacency (graph6). Verify K4-free (no 4 mutually adjacent vertices; exact clique check, clique number <= 3). Verify independence number <= 6 (max clique on the complement <= 6). Both exact and fast for N in the tens of vertices.

**Search plan.** Cyclic / circulant graphs (search connection sets over Z_N screening clique and independence numbers); prescribed-automorphism SAT; genetic / tabu search on graphs with the two Ramsey constraints as penalties; lift or blow up smaller good Ramsey graphs.

**Prior art (verify).** S. Radziszowski, "Small Ramsey Numbers," EJC dynamic survey DS1, tabulates the current bounds for R(4,7) (upper bounds for R(4,l) from Angeltveit-McKay). Re-verify the current lower bound before claiming; many R(4,l) lower bounds come from decades-old cyclic constructions and are candidates for improvement.

**Openness:** documented-open. **Win-type:** found-object.
