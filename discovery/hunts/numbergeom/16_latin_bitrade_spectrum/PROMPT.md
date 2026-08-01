# Latin bitrade filling a spectrum gap

**Find.** A Latin bitrade (a pair of disjoint partial Latin squares T_1, T_2 occupying the same cells, with matching row and column symbol sets) of a size or shape reported as not known to exist, filling a gap in the tabulated spectrum of bitrade sizes / minimal defining sets.

**What counts as a win (one-sided).** One bitrade of the target size/shape satisfying the trade conditions. A single witness fills the gap; failure proves nothing.

**Checker (seconds).** Assert T_1 and T_2 occupy identical cells with disjoint entries per cell, and that in every row and every column the multiset of symbols used by T_1 equals that of T_2. Linear in the number of filled cells; exact.

**Search plan.** Construct from a genus / triangulation model of the bitrade, or from a small partial Latin square and its intercalate structure; backtracking that grows the trade cell by cell keeping row/column balance; SAT/CP with the row-column symbol-balance constraints. Evolutionary search over cell sets.

**Prior art (verify).** The spectrum of sizes and structures of Latin bitrades (and minimal defining sets / critical sets of Latin squares) has documented open or sporadic cases. See Nick Cavenagh, "The theory and application of Latin bitrades: a survey" (ca. 2008), and the critical-set literature (Keedwell, Donovan). Confirm a currently open size/shape before starting (verify).
