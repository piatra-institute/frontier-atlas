# A record success probability for generalized Hardy nonlocality

**Find:** a state and measurements achieving a Hardy-paradox success probability above the best-known value, for a multiparty or higher-setting Hardy configuration whose maximum is undetermined.

## What counts as a win
An explicit state and projective measurements satisfying the Hardy zero-probability constraints exactly, with the target "paradox" probability strictly above the current record. One-sided: any larger probability meeting all constraints is a new lower bound on the maximum.

## Checker
From rho and the projective measurements compute the relevant joint outcome probabilities by the Born rule (exact for algebraic entries). Verify every Hardy constraint probability is exactly 0 and that the designated success probability P exceeds the previous record. Pure linear algebra on small operators. Runtime: seconds.

## Search plan
Fix the configuration (number of parties, settings, local dimension); impose the zero constraints as exact algebraic equations on the measurement projectors and state, solve/optimise P subject to them (Lagrangian or elimination), and rationalise a record point. Certify with the exact checker.

## Prior art (verify)
Hardy (1993) nonlocality has an optimal two-qubit probability of (5 sqrt5 - 11)/2; generalized (multiparty, ladder, higher-dimensional) versions have improving records and, for several settings, no proven maximum (Chen et al.; Meng et al.; Rabelo et al.). Confirm the chosen configuration has an open maximum.
