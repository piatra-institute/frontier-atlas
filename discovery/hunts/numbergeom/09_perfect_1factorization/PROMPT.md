# Perfect 1-factorization of K_{2n} at an open order

**Find.** A perfect 1-factorization of the complete graph K_{2n} at a smallest open order: a proper edge-coloring into 2n-1 perfect matchings such that the union of every pair of matchings is a single Hamiltonian cycle.

**What counts as a win (one-sided).** One factorization of K_{2n} passing the check at an order with none known. A single witness settles existence there; failure proves nothing.

**Checker (seconds).** Verify the 2n-1 color classes are perfect matchings partitioning the edges, then for each of the C(2n-1, 2) pairs verify the union is a single 2n-cycle (one connected 2-regular component). O(n^4) worst case, fast for the relevant sizes.

**Search plan.** Start from starter-based / GK-type constructions and repair; backtracking that extends a partial factorization while enforcing the Hamiltonicity of each pair; SAT with matching and cycle constraints; evolutionary recombination of near-perfect factorizations.

**Prior art (verify).** Kotzig conjectured every K_{2n} has a perfect 1-factorization. It is known for 2n = p+1 and 2n = 2p (p prime) and many sporadic orders, but infinitely many orders are open, with specific small orders undetermined. See Wallis's survey on one-factorizations and computational work (Wanless, Ihrig, and others). Confirm the smallest current open order before starting (verify).
