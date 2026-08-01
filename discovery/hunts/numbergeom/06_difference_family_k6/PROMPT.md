# (v, k, 1) difference family at an open order

**Find.** A (v, k, 1)-difference family in Z_v for k = 6 or k = 7 at an order v listed as open: base blocks B_1, ..., B_t whose combined differences hit every nonzero element of Z_v exactly once.

**What counts as a win (one-sided).** One set of base blocks whose difference list is exactly Z_v \ {0}, each nonzero value once. A single valid family settles existence for that v; failure proves nothing.

**Checker (seconds).** For each base block compute all ordered differences mod v, concatenate, assert the multiset equals Z_v \ {0} with multiplicity one. O(t k^2). Exact modular arithmetic.

**Search plan.** Algebraic seeds from multiplier / orbit constructions (blocks fixed by a multiplier group of Z_v shrink the search); then backtracking that places blocks and prunes on already-used differences; SAT/CP with an exact-cover constraint over the difference set. Evolutionary repair of near-families.

**Prior art (verify).** Existence of (v, k, 1)-difference families (equivalently cyclic 2-(v, k, 1) designs) is resolved for k <= 5 with finitely many exceptions, but for k = 6, 7 the spectrum has open or sporadic cases. See Handbook of Combinatorial Designs (Colbourn and Dinitz), difference-family tables; Buratti's surveys on cyclic difference families. Specific orders remain undetermined (verify).
