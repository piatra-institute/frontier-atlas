# A distillation witness refuting Werner undistillability

**Refute:** the conjecture that certain NPT Werner states are n-undistillable for all n, by exhibiting an explicit distillation witness at some finite n.

## What counts as a win
A specific NPT Werner state W on C^d tensor C^d (from the parameter range conjectured undistillable) together with a vector |psi> of Schmidt rank at most 2 across the collective A^{tensor n} : B^{tensor n} cut such that <psi| (W^{tensor n})^{Gamma_B} |psi> < 0. That single vector certifies n-distillability and refutes undistillability for that state. One-sided: only the negative expectation counts.

## Checker
Form M = (W^{tensor n})^{Gamma_B} (partial transpose on the B side of n copies). Verify Schmidt rank of |psi> across the A:B cut is <= 2 (rank of its d^n x d^n coefficient matrix, exact). Then evaluate the real number <psi| M |psi> and confirm it is strictly negative. All exact rational/algebraic arithmetic. Runtime: seconds for small d and n=2,3.

## Search plan
For fixed d and n minimise <psi|M|psi> over Schmidt-rank-2 |psi> (biconvex / alternating optimisation), then rationalise any negative point. Start at the boundary of the known-distillable region and push into the conjectured-undistillable window; try n=3 where the 2-copy case is now settled.

## Prior art (verify)
NPT bound entanglement (existence of undistillable NPT states) is a central open problem (DiVincenzo-Shor-Smolin-Terhal-Thapliyal 2000; Dur-Cirac-Lewenstein-Bruss 2000; Open Quantum Problems, oqp.iqoqi.oeaw.ac.at). The 2-copy Werner case was recently claimed resolved (2026); the general n case is open.
