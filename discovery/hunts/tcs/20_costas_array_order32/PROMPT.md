# 20. A Costas array of order 32 (or 33)

**Find.** A Costas array of order 32, or of order 33. A Costas array of order n is a permutation of {1..n} (an n x n permutation matrix) in which the n(n-1)/2 displacement vectors between pairs of marks are all distinct. Every order n <= 29 has a known example (exhaustive), but n = 32 and n = 33 are the smallest orders for which *no* Costas array is known; existence is a long-standing open question.

**What counts as a win.** One permutation p: {1..n} -> {1..n} (n=32 or 33) satisfying the distinct-difference property. One-sided: a single array settles existence for that order. (Conjecture: they exist for all n.)

**Checker (seconds).** For the permutation, for each row-distance h in 1..n-1, collect the multiset { p(i+h) - p(i) : 1 <= i <= n-h } and assert no value repeats within that multiset (equivalently, all displacement vectors (h, p(i+h)-p(i)) are distinct). O(n^2), microseconds. Exact integer.

**Search plan.** The full exhaustive search at n=32 is infeasible, so target structure: near-Costas permutations from Welch/Lempel-Golomb generators of nearby orders modified locally; local search / backtracking with the distinct-difference constraint and strong pruning; SAT/CP encodings with all-different displacement constraints.

**Prior art (verify).** Drakakis, "Open problems in Costas arrays" (arXiv 1102.5727, 2011); Costas array enumeration up to order 29 (Drakakis et al.). Orders 32 and 33 remain the smallest with no known array.
