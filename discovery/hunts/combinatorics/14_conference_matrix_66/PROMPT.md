# 14. Symmetric conference matrix of order 66

**Target.** Construct a symmetric conference matrix of order 66, or prove none exists. A conference matrix C of order n has zero diagonal, off-diagonal entries +/-1, and C*C^T = (n-1)*I. A symmetric order-66 conference matrix is equivalent to a strongly regular conference graph srg(65,32,15,16). The necessary condition (n-1 = 65 = 8^2 + 1^2 a sum of two squares) is met; existence is open.

**What counts as a win.** One explicit 66x66 symmetric conference matrix settles existence (one-sided YES) and simultaneously yields srg(65,32,15,16).

**Checker (seconds).** Read the 66x66 integer matrix C. Verify diag(C) = 0, all off-diagonal entries in {+1,-1}, C = C^T, and C*C^T = 65*I. O(n^3), milliseconds.

**Search plan.** Cyclotomic / Paley-type constructions fail because 65 is not a prime power (this is why the case is open), so try: two-block / Seidel-matrix constructions from regular two-graphs on 66 points; prescribed-automorphism SAT/ILP on the Seidel matrix; local search over symmetric +/-1 matrices minimizing the off-orthogonality residual.

**Prior art (verify).** Symmetric conference matrices exist for many orders n = 2 mod 4 but order 66 is a documented open case; see the conference-matrix and srg(65,...) entries in Colbourn-Dinitz "Handbook of Combinatorial Designs" and Brouwer's SRG notes. Re-verify openness.

**Openness:** verify. **Win-type:** existence.
