# 28. Longer snake-in-the-box in dimension 11

**Target.** Find an induced path (a "snake") in the 11-dimensional hypercube Q_11 longer than the current best-known record. A snake is a chordless (induced) path: a sequence of distinct vertices, each differing from the next in one bit, with no two non-consecutive vertices adjacent in Q_11. Exact maxima are known only through dimension 8; dimensions >= 9 hold only records that keep improving.

**What counts as a win.** One explicit snake in Q_11 with length (edge count) strictly above the current record improves the lower bound for that dimension (one-sided). Records here have advanced repeatedly, including in 2025-2026.

**Checker (seconds).** Read the vertex sequence as 11-bit integers v_0,...,v_L. Verify all distinct; consecutive vertices differ in exactly one bit (popcount(v_i XOR v_{i+1}) = 1); and for all non-consecutive i,j, popcount(v_i XOR v_j) != 1 (induced). O(L^2), fast.

**Search plan.** Prune-heavy depth-first / branch-and-bound with canonical (symmetry) reduction under the hyperoctahedral group; evolutionary and beam search (the historical record-setters); SAT / constraint models for local extension; stitch known long sub-snakes.

**Prior art (verify).** Snake-in-the-box maxima: OEIS A099155 (exact to n=8: 1,2,4,7,13,26,50,98). For n=11 the Allison-Paulusma bound gave length >= 712 (2016), improved by later record searches (e.g. T. Ace, 2025). Re-verify the current record length for Q_11 before claiming.

**Openness:** documented-open. **Win-type:** found-object.
