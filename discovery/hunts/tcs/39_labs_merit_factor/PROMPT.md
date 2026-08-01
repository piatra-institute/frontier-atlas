# 39. A binary sequence beating the best known LABS merit factor

**Find.** A binary sequence s in {+1, -1}^L, for a length L in the currently-open range (beyond exhaustive proof, e.g. L in the ~70-120 band and specific larger L), whose low-autocorrelation "merit factor" exceeds the best value ever recorded at that length. The Low-Autocorrelation Binary Sequence (LABS) problem asks to minimize the sidelobe energy E(s) = sum_{k>=1} C_k(s)^2 where C_k are aperiodic autocorrelations; optimal sequences are known only for small L, and best-known records for larger L are periodically improved.

**What counts as a win.** One explicit sequence of the target length L whose merit factor F = L^2 / (2 E(s)) strictly exceeds the recorded best for that L. One-sided: a better sequence is a new record; global optimality need not be proven.

**Checker (seconds).** Compute the L-1 aperiodic autocorrelations C_k = sum_i s_i s_{i+k}, form E = sum C_k^2, then F = L^2/(2E); assert F beats the record. O(L^2) integer arithmetic, microseconds.

**Search plan.** Structured/evolutionary: self-avoiding-walk and memetic/tabu search (the state of the art for LABS), branch-and-bound for smaller L, and restarts from skew-symmetric sequences (which admit only odd L and halve the search); GPU-parallel random restarts.

**Prior art (verify).** Golay (merit factor); Mertens, "Exhaustive search for low-autocorrelation binary sequences" (1996) and later; Boskovic, Brglez, Zamuda memetic solvers; the LABS records tables (verify the best-known merit factor at the target L). Known NP-hard-in-practice; records genuinely move.
