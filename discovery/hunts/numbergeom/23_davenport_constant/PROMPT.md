# Zero-sum-free sequence beating the Davenport lower bound

**Find.** A zero-sum-free sequence over a finite abelian group G (rank >= 3, e.g. C_n^3 or a mixed group) longer than the best published lower bound for the Davenport constant D(G): a sequence of group elements with no nonempty subsequence summing to the identity.

**What counts as a win (one-sided).** One zero-sum-free sequence of length exceeding the current lower bound for D(G). A single longer sequence improves the bound; failure proves nothing.

**Checker (seconds).** Verify no nonempty subsequence sums to zero. For length L up to the relevant range, use meet-in-the-middle over the group (split the sequence, tabulate partial sums of each half, test for a matching pair covering a nonempty subset). 2^{L/2} group operations; seconds for the target lengths.

**Search plan.** Construct from known extremal patterns (repeated generators, box constructions) and extend; local search adding/swapping elements while keeping zero-sum-freeness; CP over the group with the subset-sum constraint. Focus on rank-3 and higher groups where D(G) is not determined.

**Prior art (verify).** The Davenport constant D(G) is known for p-groups of rank <= 2 and cyclic groups, but is open for most groups of rank >= 3, with only lower and upper bounds tabulated. See Gao and Geroldinger, "Zero-sum problems in finite abelian groups: a survey" (ca. 2006). Improving a lower bound for a rank >= 3 group is a genuine open target (verify current bounds).
