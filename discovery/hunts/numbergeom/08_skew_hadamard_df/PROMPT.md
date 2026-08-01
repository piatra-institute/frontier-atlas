# Skew Hadamard difference set at an open order

**Find.** A skew Hadamard difference set of order v not of Paley type: a (v, (v-1)/2, (v-3)/4) difference set D in an abelian group with the skew property D and -D partition the nonzero elements, at an order where no inequivalent example is catalogued.

**What counts as a win (one-sided).** One skew Hadamard difference set inequivalent to the Paley construction at that order, or one at an order with none known. A single witness settles it; failure proves nothing.

**Checker (seconds).** Verify the difference multiset covers each nonzero element lambda times, and verify the skew condition (D, -D, {0} partition the group). O(v^2). For inequivalence, compare invariants (e.g., the associated code / multiplier group) against the Paley example.

**Search plan.** Search cyclotomic and index-2 / index-4 constructions over small fields; genetic search over multiplier-invariant candidate sets; CP with the skew and constant-difference constraints. Focus on orders where the classification is incomplete.

**Prior art (verify).** The long-standing belief that all skew Hadamard difference sets are Paley type was disproved (Ding and Yuan, ca. 2006), and further inequivalent families followed (Feng, Xiang, and others). Classification remains incomplete; several orders have no known non-Paley example or are undetermined. See Ding-Yuan and subsequent skew-Hadamard papers (verify current tables).
