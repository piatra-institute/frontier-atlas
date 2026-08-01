# 24. A function with optimal algebraic immunity and record nonlinearity

**Find.** A balanced Boolean function f: F_2^n -> F_2 at a specified n that simultaneously achieves optimal (maximum) algebraic immunity ceil(n/2) and a nonlinearity above the best explicitly-known value for functions with that immunity. Jointly optimizing algebraic immunity, nonlinearity, and balancedness for stream-cipher design leaves open (n) cells where the achievable nonlinearity at maximum immunity is not pinned down (verify the target n).

**What counts as a win.** One explicit truth table that is balanced, has algebraic immunity exactly ceil(n/2), and nonlinearity strictly above the recorded best for max-immunity functions at that n. One-sided: an explicit function reaching the target settles achievability.

**Checker (seconds).** Algebraic immunity: solve for low-degree annihilators of f and of f+1 by Gaussian elimination over F_2 on the monomials of degree < d, increasing d until an annihilator appears; assert the minimal such d equals ceil(n/2). Nonlinearity from the Walsh transform. Balancedness from the weight. Exact over F_2; for n up to ~16 this is seconds.

**Search plan.** Structured: start from the Carlet-Feng / majority-function constructions known to reach optimal immunity, then apply nonlinearity-raising local swaps that preserve the annihilator structure; SAT/CP with immunity encoded as "no nonzero low-degree annihilator."

**Prior art (verify).** Courtois & Meier (2003, algebraic attacks); Carlet & Feng construction (2008); tables of best (nonlinearity, algebraic immunity) trade-offs (verify the open n). Achievable nonlinearity at maximum immunity is not fully determined.
