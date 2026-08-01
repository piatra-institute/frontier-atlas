# B_2[g] set beating a tabulated size

**Find.** A B_2[g] set in [1, n] (every integer has at most g representations as an unordered pair sum a_i + a_j) that is larger than the best published size for that (g, n), with g = 2 or g = 3.

**What counts as a win (one-sided).** One set of size s in [1, n] whose every pairwise sum multiplicity is at most g, with s above the current record. A single larger set improves the lower bound; failure proves nothing.

**Checker (seconds).** Tally multiplicities of all pair sums a_i + a_j (i <= j), assert max multiplicity <= g. O(s^2) with a hash of sums; exact integer arithmetic, sub-second.

**Search plan.** Local search / simulated annealing over the set, penalizing sums that exceed multiplicity g; incremental update of the sum histogram on swaps; CP with per-sum count constraints. Seed from known extremal B_2[g] sets and dilations of Sidon sets.

**Prior art (verify).** Maximum sizes of B_2[g] sets in [1, n] are only partially known; tables give lower bounds that are not proven optimal. See Kohonen, meet-in-the-middle enumeration of restricted additive sets (ca. 2014-2016); O'Bryant's Sidon survey (DS11) for the B_h[g] background. Specific (g, n) cells are open or improvable (verify).
