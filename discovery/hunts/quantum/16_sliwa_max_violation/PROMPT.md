# A record violation of a Sliwa tripartite Bell inequality

**Find:** a state and measurements exceeding the best-known quantum value of a Sliwa (3-party, 2-setting, 2-outcome) Bell inequality whose maximal quantum violation is not settled.

## What counts as a win
Explicit tripartite state rho on C^d tensor C^d tensor C^d and dichotomic measurements per party giving a value above the current numerical record for a chosen Sliwa functional with an open maximum. One-sided: a higher value is a new lower bound on that maximum.

## Checker
Assemble the tripartite Bell operator M as the signed sum of A_x tensor B_y tensor C_z with the Sliwa coefficients; verify each observable squares to I. Evaluate Tr(rho M) and report the top eigenvalue of M. Exact over algebraic entries, otherwise certified interval arithmetic. Runtime: seconds.

## Search plan
Seesaw / gradient optimisation over the three parties' measurements and the state at small d; compare against the NPA-hierarchy upper bound to target functionals with an open gap. Certify any record point exactly.

## Prior art (verify)
Sliwa (2003) enumerated the 46 tripartite (2,2,2) Bell inequality classes; for several the exact maximal quantum violation is undetermined, with only numerical lower bounds and NPA upper bounds (Vertesi-Bene and later studies). Confirm which functionals still have an open maximum.
