# Batch sweep: refute conjectured properties of OEIS sequences

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit index n where a sequence's conjectured property first fails, or a set of properties that survive extended computation. A first-failure is a clean, exactly-checkable refutation.

**Family + panel.** OEIS sequences carrying an unproven "Conjecture:" comment or a conjectured formula. Properties to test: monotonicity, positivity of differences, log-concavity a(n)^2 ≥ a(n−1)a(n+1), unimodality, integrality of a claimed closed form, divisibility/congruence patterns ("a(n) ≡ r mod m"), and primality claims ("a(n) is prime for all n").

**Enumerate / source.** Harvest sequences programmatically from OEIS: those with keyword filters and free-text "Conjecture" comments, prioritizing sequences with a b-file (many known terms) and an explicit generating rule so terms can be recomputed far beyond the stored range. Cross-check the first stored terms against the b-file before trusting any recomputation.

**Conjecture generation.** For each harvested sequence, extract the exact conjectural claim from its comment/formula and turn it into a decidable predicate over n. The "generation" step is parsing many real conjectures, not inventing bounds; the value is testing each far past where the proposer checked.

**Adversarial refutation.** Recompute the sequence from its defining recurrence/formula to a much larger index than the b-file, then evaluate the predicate at every new index. Fragile conjectures (log-concavity, congruence, "always prime") often break just beyond the tabulated range.

**Checker (exact).** All arithmetic exact (big integers / exact rationals); a violation is a specific n with the computed a(n) contradicting the claim. Emit (A-number, claim, first-failing n, value).

**Verification discipline.** Generator is not verifier: recompute each sequence two independent ways (recurrence vs closed form, or two libraries) and require agreement on all stored terms first. No fabricated A-numbers or terms; every claim quoted verbatim from OEIS with access date. Report the denominator: sequences tested / broken / survived.
