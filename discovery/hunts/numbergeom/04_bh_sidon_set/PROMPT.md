# B_h Sidon set beating a tabulated size

**Find.** A B_h set in [1, n] (a set whose h-fold sums are all distinct, equivalently every integer has at most one representation as an unordered h-term sum) that is larger than the best published B_h set for that n, with h = 3 or h = 4.

**What counts as a win (one-sided).** One set of size s in [1, n] with the B_h property, where s exceeds the current tabulated lower bound. A single larger set beats the record; failure proves nothing.

**Checker (seconds).** Sort all multiset h-sums of the set, assert no collision. For s ~ 20-40 and h = 3, 4 the sum list is small; exact integer arithmetic, sub-second.

**Search plan.** Greedy plus local swap; simulated annealing on the set scored by number of colliding h-sums; meet-in-the-middle to test the B_h property fast during search; CP with an all-distinct constraint on h-sums. Seed from projective / Singer-type B_h constructions and extend near the top of [1, n].

**Prior art (verify).** Largest known B_h sets in [1, n] are tabulated but not tight for most h >= 3. See Kevin O'Bryant, dynamic survey on Sidon sequences (Electronic J. Combinatorics, DS11); Kohonen, computational tables of B_h sets. Lower bounds in these tables are improvable in specific (h, n) cells (verify).
