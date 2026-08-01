# Postage-stamp basis beating a tabulated record

**Find.** A k-element set A of positive integers containing 0 (or 1) whose h-fold sumset covers a longer initial run [1, N] than the best published n(h, k), for an open (h, k) cell.

**What counts as a win (one-sided).** One k-set whose h-fold sums cover 1..N with N strictly above the current record n(h, k). A single better basis improves the lower bound; failure proves nothing.

**Checker (seconds).** Enumerate all sums of at most h elements (with repetition), mark covered integers, assert 1..N all covered and N+1 not forced. O(k^h) small for the relevant sizes; exact integer arithmetic.

**Search plan.** Exhaustive / branch-and-bound with Kohonen-style pruning for small k; for larger k use simulated annealing or evolutionary search on the mark set, scoring by the first uncovered integer; ILP for the covering feasibility at a target N. Seed from the extremal bases in the tables and mutate the top marks.

**Prior art (verify).** The postage-stamp (h-range basis) problem n(h, k) is tabulated but only partially known; records improve irregularly. See Stohr; Challis and Robinson, "Some extremal postage stamp bases" (ca. 2010); Kohonen, pruning methods for the postage-stamp problem; OEIS A001212, A001208. Several (h, k) cells are open or only lower-bounded (verify).
