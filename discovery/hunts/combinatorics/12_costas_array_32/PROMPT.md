# 12. Costas array of order 32

**Target.** Find a Costas array of order 32 (or order 33), or a certified exhaustive nonexistence. A Costas array of order n is an n x n permutation matrix in which the C(n,2) displacement vectors between pairs of the n marked cells are all distinct. Orders 32 and 33 are the smallest for which no Costas array is known.

**What counts as a win.** A single order-32 permutation with the distinct-displacement property settles existence for n = 32 (one-sided YES). It would be the first known Costas array of that order.

**Checker (seconds).** Read a permutation p[0..31] (p a bijection on {0..31}). For all pairs i<j collect the vector (j - i, p[j] - p[i]); assert all C(32,2) = 496 vectors are pairwise distinct (hash into a set, check size). O(n^2), microseconds.

**Search plan.** The known algebraic families (Welch and Lempel-Golomb constructions from primitive roots) do not yield 32 or 33, which is why they are open; so run backtracking with the distinct-difference constraint and strong pruning, plus tabu / evolutionary search and orbit reduction under the dihedral symmetry group of the array. Restart-heavy stochastic search has historically found sporadic Costas arrays.

**Prior art (verify).** Costas arrays are known for all n <= 29; existence for n = 32 and n = 33 is the standing open question (Costas, Golomb-Taylor; see the Costas-array enumeration literature and databases, e.g. Drakakis et al.). Re-verify these orders are still open before starting.

**Openness:** documented-open (verify). **Win-type:** existence.
