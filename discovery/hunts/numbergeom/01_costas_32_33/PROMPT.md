# Costas array of order 32 or 33

**Find.** A Costas array of order 32 (or 33): a permutation p of {1..n} whose n(n-1)/2 displacement vectors (i-j, p(i)-p(j)), i<j, are all distinct.

**What counts as a win (one-sided).** One explicit permutation of order 32 or 33 passing the check. Existence is settled by a single witness; failure to find proves nothing.

**Checker (seconds).** Form all pairwise displacement vectors, assert the multiset has no repeat. O(n^2), microseconds. Independent re-check from the raw permutation.

**Search plan.** Algebraic seeds first: Welch (order p-1) and Lempel-Golomb (order q-2) miss 32, 33 (33, 34, 35 are not prime / prime-power), which is why these orders are hard. Then heuristic repair over permutations: tabu / simulated annealing minimizing displacement collisions; backtracking with distinct-difference pruning; SAT/CP with an all-different constraint on displacements. Evolutionary crossover of near-Costas permutations.

**Prior art (verify).** Costas arrays are enumerated exhaustively through order 29 (Drakakis, Rickard, Beard, Iorio, et al., enumeration of orders 27-29, ca. 2008-2011). No Costas array is known for orders 32 and 33; the standard constructions do not reach them. See Costas-array surveys (Drakakis) and OEIS A008404. Open as of mid-2026 (verify).
