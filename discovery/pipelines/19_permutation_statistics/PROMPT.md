# Batch sweep: refute permutation-statistic and pattern conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit statistic/pattern pair whose claimed equidistribution or Wilf-equivalence fails, or hardened survivors. Refutation is the clean win. Precedent: several Noonan-Zeilberger-style pattern conjectures were later refuted.

**Family + panel.** Permutations of [n]; statistics: inversions (maj/inv Mahonian pair), descents (Eulerian), excedances, major index, number of occurrences of a fixed pattern, longest increasing subsequence, and stack-sorting depth. Also: sizes of pattern-avoidance classes |Av_n(σ)|.

**Enumerate.** All permutations of [n] for n≤10 (n! = 3628800 at n=10, exhaustive), n≤11 by streaming. Sanity-check |Av_n(123)| = Catalan numbers 1,1,2,5,14,42,132,429,1430,4862 and |Av_n(σ)| for length-3 σ all equal (a known equidistribution — use as a self-check).

**Conjecture generation.** Test three families: (1) Wilf-equivalence — do two patterns give equal |Av_n| for all n≤10? (2) equidistribution — do two statistics have the same distribution over S_n or over an avoidance class? (3) unimodality/log-concavity of a statistic's distribution. Harvest candidate claims from the permutation-patterns literature and the Database of Permutation Pattern Avoidance (Tenner). Auto-generate pattern pairs to test.

**Adversarial families.** Longer patterns (length 4-5, where Wilf classes are subtler), pairs of patterns, mesh/vincular patterns, and statistic pairs that agree on S_n but may split on avoidance classes.

**Checker (exact).** Count exactly by full enumeration; two distributions match only if their entire generating polynomials are identical (exact integer coefficients). Emit any n where a claimed equality first fails, with counts.

**Verification discipline.** Generator is not verifier: recompute each statistic and each avoidance count with a second independent routine; verify Catalan/known equidistributions as audits. Cite each claim's source or mark "could not verify." Report candidates generated / broken / survived, with the first failing n.
