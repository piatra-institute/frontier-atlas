# Three mutually orthogonal Latin squares of order 10

**Find.** Three Latin squares of order 10 that are pairwise orthogonal (every ordered pair of symbols occurs exactly once across each pair of squares).

**What counts as a win (one-sided).** One triple of pairwise-orthogonal order-10 Latin squares. A single witness settles the famous question N(10) >= 3; failure proves nothing. (This is a hardened target: decades of search have found only pairs. Flag the long-shot status honestly.)

**Checker (seconds).** Assert each of the three arrays is a Latin square, then for each of the three pairs assert the 100 symbol-pairs are all distinct. O(1) at order 10; exact.

**Search plan.** Fix one square (or a prolongation of a known pair) and search for a third orthogonal mate via exact-cover / SAT over the orthogonality constraints; use the transversal / orthogonal-mate formulation; restrict to squares with prescribed autotopism groups to shrink the space. Evolutionary repair of near-orthogonal triples.

**Prior art (verify).** Two MOLS of order 10 exist (Bose, Shrikhande, Parker, disproving Euler), but whether three exist is a long-standing open problem; extensive computation has not produced a triple nor ruled one out. See the Handbook of Combinatorial Designs, N(n) tables, and the MOLS(10) literature. Open (verify).
