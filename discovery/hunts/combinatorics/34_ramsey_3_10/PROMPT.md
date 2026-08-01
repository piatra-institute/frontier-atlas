# 34. Settle R(3,10) = 41 with a triangle-free witness

**Target.** Find a triangle-free graph on 40 vertices whose independence number is at most 9. The Ramsey number R(3,10) is known to satisfy 40 <= R(3,10) <= 41; such a graph proves R(3,10) >= 41, hence R(3,10) = 41, closing the interval.

**What counts as a win.** One explicit 40-vertex graph with no triangle and no independent set of size 10 determines R(3,10) = 41 (one-sided: a single witness settles the exact value given the known upper bound 41).

**Checker (seconds).** Read adjacency (graph6) on 40 vertices. Verify triangle-free (no i<j<k mutually adjacent; A^2 elementwise vs A, or triangle count = 0). Verify independence number <= 9: assert no independent set of size 10 exists (exact via a clique solver on the complement, or ILP; 40 vertices is fast). O(v^3) for triangle-freeness; independence check via a max-clique routine on the complement.

**Search plan.** Cyclic / circulant graphs on Z_40 (search connection sets that are sum-free-like, screening triangle count and independence); prescribed-automorphism SAT; local search / tabu on triangle-free graphs maximizing girth-independence tradeoff; extend known R(3,10) >= 40 constructions by one vertex.

**Prior art (verify).** S. Radziszowski, "Small Ramsey Numbers," EJC dynamic survey DS1, gives 40 <= R(3,10) <= 41 (upper bound 41 by Goedgebeur et al., 2024; lower bound 40 by explicit construction). Re-verify the current interval; if the upper bound has moved, adjust the target.

**Openness:** documented-open. **Win-type:** found-object.
