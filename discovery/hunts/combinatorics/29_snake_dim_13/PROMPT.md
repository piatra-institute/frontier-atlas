# 29. Longer snake-in-the-box in dimension 13

**Target.** Find an induced path (snake) in the 13-dimensional hypercube Q_13 longer than the current best-known record. Q_13 is far beyond the exactly-solved range (n <= 8), so any improvement to the best-known length is a new record for the dimension.

**What counts as a win.** One explicit snake in Q_13 whose length exceeds the current record improves the lower bound (one-sided). The large dimension means the search is wide open and records move.

**Checker (seconds).** Read the vertex sequence as 13-bit integers v_0,...,v_L. Verify all distinct; consecutive differ in exactly one bit (popcount(v_i XOR v_{i+1}) = 1); no two non-consecutive vertices adjacent (popcount(v_i XOR v_j) != 1 for |i-j| > 1). O(L^2).

**Search plan.** Evolutionary / genetic search and beam search with symmetry canonicalization (the methods behind most large-dimension records); prune-heavy DFS for local extension; transfer / lift long snakes from Q_12; parallel restart portfolios.

**Prior art (verify).** OEIS A099155 (snake maxima; exact only to n=8). For n=13 the Allison-Paulusma bound gave length >= 2687 (2016), with subsequent record improvements (e.g. T. Ace census, 2025-2026). Re-verify the current Q_13 record before claiming an improvement.

**Openness:** documented-open. **Win-type:** found-object.
