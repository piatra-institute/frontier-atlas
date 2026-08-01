# 17. An APN permutation in dimension 8 (the Big APN problem)

**Find.** A bijective almost-perfect-nonlinear (APN) function F: F_2^8 -> F_2^8, i.e. a permutation for which every equation F(x+a)+F(x)=b (a != 0) has at most 2 solutions. Whether an APN permutation exists in any even dimension n >= 8 is the "Big APN problem." The only known even-dimension APN permutation is Dillon et al.'s dimension-6 example (2009); n=8 is wide open.

**What counts as a win.** One explicit permutation (a lookup table of 256 values, or a polynomial over F_2^8) that is a bijection with differential uniformity exactly 2. One-sided: a single witness resolves existence for n=8.

**Checker (seconds).** Build the 256-entry table; verify it is a bijection; compute the full difference distribution table: for each a != 0, tally F(x+a)+F(x) over all x and assert every count is 0 or 2 (max = 2). That is 255 x 256 evaluations, milliseconds. Optionally confirm APN-ness via the Walsh/autocorrelation criterion independently.

**Search plan.** SAT/CP over the 256-cell table with bijectivity + differential constraints (huge but structured; use symmetry/self-equivalence subspaces). Algebraic: search quadratic/CCZ classes and self-equivalence-constrained Groebner bases (the 2026 dim-8 approach); switch/twist known APN functions toward bijectivity.

**Prior art (verify).** Browning, Dillon, McQuistan, Wolfe, "An APN permutation in dimension six" (2009/2010); Carlet's Boolean-functions book; the recent dim-8 quadratic-APN Groebner searches (2026, arXiv, verify). Existence for even n >= 8 remains open.
