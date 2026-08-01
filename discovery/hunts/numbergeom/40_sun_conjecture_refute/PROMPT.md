# Counterexample to a Zhi-Wei Sun conjecture

**Refute.** A specific conjecture from Zhi-Wei Sun's published lists of the form "for all n, P(n) holds" or "the only solutions are ...", chosen so that its stated verification bound is modest and its structure is machine-generated: exhibit an n violating P.

**What counts as a win (one-sided).** One explicit n at which the chosen conjecture fails. A single counterexample refutes it; failure proves nothing. Several such conjectures have already been disproved, so being false is plausible.

**Checker (seconds).** Recompute the conjecture's predicate at the witness n exactly (the predicates are typically representation counts, primality/monotonicity, or divisibility statements computable directly); assert it fails. Exact integer arithmetic; independent recomputation.

**Search plan.** Pick a conjecture with a low reported verification bound and a cheap per-n predicate. Extend the search well past the reported bound with an optimized direct evaluation; for "only solutions are ..." claims, sieve for additional solutions; for monotonicity/positivity claims, scan for the first violation. Batch over many candidate conjectures to raise the hit rate.

**Prior art (verify).** Zhi-Wei Sun has posted large collections of conjectures (arXiv preprints on conjectures in number theory and combinatorics, and many OEIS entries), a number of which carry only finite verification and some of which have been refuted by later computation. Select a currently standing conjecture with a modest bound and confirm it is open (verify against Sun's lists and OEIS).
