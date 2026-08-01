# Counterexample to an open real-rootedness conjecture

**Refute.** A specific open conjecture that a combinatorially defined polynomial family is real-rooted: exhibit a member with a non-real root. Candidate families include certain independence, chromatic-adjacent, local h-, or descent-type polynomials for which real-rootedness is conjectured but unproven.

**What counts as a win (one-sided).** One instance polynomial (explicit integer coefficients from the combinatorial data) that has a non-real root. A single instance refutes the family conjecture; failure proves nothing.

**Checker (seconds).** Compute the number of real roots exactly via a Sturm sequence (or sign of the discriminant for small degree) over Q; assert it is less than the degree. Exact rational/integer arithmetic; no floating point in the certificate.

**Search plan.** Generate the polynomials over a batch of combinatorial inputs (graphs, posets, permutations, simplicial complexes) of increasing size; screen each with a fast numerical root count, then certify the first apparent counterexample exactly with Sturm. Evolutionary search over the combinatorial inputs scored by the numerical imaginary-part magnitude.

**Prior art (verify).** Several real-rootedness conjectures in algebraic combinatorics are open, and some once-believed ones fell (the Neggers-Stanley conjecture was disproved by Braenden and by Stembridge with small examples). See Petter Braenden, survey "Unimodality, log-concavity, real-rootedness and beyond" (ca. 2015). Pick a currently open family and confirm status (verify).
