# 30. Longer coil-in-the-box in dimension 11 or 12

**Target.** Find an induced cycle (a "coil") in the hypercube Q_n (n = 11 or 12) longer than the current best-known record. A coil is a chordless cycle: a cyclic sequence of distinct vertices, each differing from the next in one bit, first and last adjacent, and no other pair of vertices adjacent in Q_n. Exact coil maxima are known only through dimension 7; higher dimensions hold improving records.

**What counts as a win.** One explicit coil in Q_n of length above the current record improves the lower bound for that dimension (one-sided).

**Checker (seconds).** Read the cyclic vertex sequence as n-bit integers v_0,...,v_{L-1}. Verify all distinct; each consecutive pair (cyclically, including v_{L-1}-v_0) differs in one bit; and for every non-adjacent pair in the cycle, popcount(v_i XOR v_j) != 1 (induced cycle). O(L^2).

**Search plan.** Evolutionary / beam search with hyperoctahedral symmetry reduction; branch-and-bound DFS for extension; adapt long snakes into closed coils; parallel restarts. Coils are cycles so the closure constraint makes them slightly rarer than snakes of the same length.

**Prior art (verify).** OEIS A000937 (coil-in-the-box maxima; exact only to n=7). Best-known coil records for n=11,12 come from record searches (Allison-Paulusma 2016 and later, e.g. T. Ace, 2025). Re-verify the current record for the chosen dimension before claiming.

**Openness:** documented-open. **Win-type:** found-object.
