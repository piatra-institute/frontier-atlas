# 36. Improve the lower bound for R(5,6)

**Target.** Find a K5-free graph on N vertices with independence number at most 5, for N at least the current best-known lower bound of R(5,6). Such a graph proves R(5,6) >= N+1. The interval for R(5,6) is very wide (best-known bounds span dozens of vertices), so the lower bound is under-tested.

**What counts as a win.** One explicit K5-free graph on N vertices with no independent set of size 6, where N+1 beats the current tabulated lower bound, improves the lower bound for R(5,6) (one-sided).

**Checker (seconds).** Read adjacency (graph6). Verify clique number <= 4 (K5-free) via exact max-clique. Verify independence number <= 5 via max-clique on the complement. Both exact; fast for N up to ~80.

**Search plan.** Cyclic / circulant graphs over Z_N (search connection sets screening clique and independence numbers, the standard source of Ramsey lower bounds); prescribed-automorphism SAT with symmetry breaking; evolutionary search on adjacency; blow-ups and Cayley graphs over small groups of order N.

**Prior art (verify).** S. Radziszowski, "Small Ramsey Numbers," EJC dynamic survey DS1, tabulates the current bounds for R(5,6). Re-verify the current lower bound before claiming; the wide gap reflects how little the exact value is pinned down, making the lower bound a realistic target.

**Openness:** documented-open. **Win-type:** found-object.
