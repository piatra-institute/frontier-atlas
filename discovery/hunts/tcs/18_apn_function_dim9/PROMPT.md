# 18. A new APN function in dimension 9 or 10

**Find.** An APN function F: F_2^n -> F_2^n for n = 9 or 10 that is not CCZ-equivalent to any function in the current known list (the Edel-Pott / Yu-Wang-Li switching families, the monomial/Gold/Kasami/Welch/Niho classes, and catalogued quadratics). New CCZ-classes of APN functions in these dimensions are still being discovered; the classification is far from complete.

**What counts as a win.** One explicit F (polynomial or table over F_2^n) with differential uniformity 2, together with a demonstration that it is CCZ-inequivalent to the known list (via a computed CCZ/EA invariant that differs). One-sided: a genuinely new class member is a result.

**Checker (seconds).** For n=9 (512 elements) or n=10 (1024): compute the difference distribution table and assert max = 2 (APN). Then compute a CCZ-invariant (e.g. the Gamma-rank / delta-rank of the code from the graph of F, or the extended-Walsh-spectrum multiset) and compare against precomputed invariants of the known classes. Seconds.

**Search plan.** Structured/algebraic: search quadratic APN via the QAM (quadratic APN matrix) formulation with orderly generation and isomorph rejection; apply switching/twisting to known functions and re-test the invariant. SAT for constrained coefficient patterns.

**Prior art (verify).** Edel & Pott, "A new almost perfect nonlinear function" (2009); Yu, Wang, Li QAM search; the APN function tables maintained by Kaleyski/Budaghyan et al. (verify current count of classes for n=9,10). Classification incomplete.
