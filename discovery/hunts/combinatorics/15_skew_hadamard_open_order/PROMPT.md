# 15. Skew-Hadamard matrix at a small open order

**Target.** Construct a skew-Hadamard matrix of order n for the smallest n = 0 mod 4 at which none is currently known. A skew-Hadamard matrix H satisfies H*H^T = n*I and H + H^T = 2*I (so H - I is skew-symmetric with +/-1 off-diagonal). The skew-Hadamard conjecture asserts one exists for every n = 0 mod 4; a handful of small orders remain open.

**What counts as a win.** One explicit skew-Hadamard matrix at an open order settles that order (one-sided YES).

**Checker (seconds).** Read the n x n integer matrix H. Verify all entries in {+1,-1}, H + H^T = 2*I (skew condition on the off-diagonal part), and H*H^T = n*I. O(n^3), milliseconds.

**Search plan.** Goethals-Seidel and Williamson-type arrays built from four suitable +/-1 sequences (search the sequences, not the full matrix); amicable / disjoint difference families over Z_m; prescribed-automorphism SAT/ILP; local search on the four base sequences with the autocorrelation constraints as objective.

**Prior art (verify).** Skew-Hadamard matrices are known for all orders n <= 276 except a short list; consult the skew-Hadamard entry in Colbourn-Dinitz "Handbook of Combinatorial Designs," 2nd ed., and Seberry's Hadamard-matrix tables for the current smallest open order (it drifts as orders are resolved). Re-verify the chosen order is open.

**Openness:** verify. **Win-type:** existence.
