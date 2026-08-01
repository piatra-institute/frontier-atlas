# 44. A shorter perfect / sparse ruler at an open length

**Find.** A sparse ruler (a.k.a. complete or perfect difference ruler) with m marks that measures every integer distance from 1 up to a length L exceeding the best known for that mark count, at a parameter where the optimum is unproven. A length-L sparse ruler with marks 0 = x_1 < ... < x_m = L is "complete" if every integer in [1, L] equals some x_j - x_i. The maximal length achievable with m marks (equivalently the minimal marks for length L) has open values (OEIS A046693 and related); records are improved by search.

**What counts as a win.** One explicit mark set achieving a length L with m marks that beats the recorded best (more length per mark, or fewer marks per length), at an open cell. One-sided: a better ruler is a new record; matching optimality proof not required.

**Checker (seconds).** Form the set D = { x_j - x_i : i < j }; assert D contains every integer in [1, L] (completeness) and record (m, L). O(m^2) to build D, then a range scan. Exact integer, microseconds.

**Search plan.** Structured: extend known optimal/near-optimal rulers by appending marks and testing completeness; branch-and-bound / SAT with "every distance covered" constraints; use the perfect-difference-set and Wichmann-ruler constructions as scaffolds and search the residual.

**Prior art (verify).** OEIS A046693 (minimal number of marks) and A103294 (sparse rulers); Wichmann rulers; the sparse-ruler records maintained by the OEIS/ruler community (verify the open cell and current record before starting).
