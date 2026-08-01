# 2n points, no three in line, at an open grid size

**Find.** A set of 2n points on the n x n integer grid with no three collinear, at a value of n for which no 2n-point solution is currently recorded.

**What counts as a win (one-sided).** One placement of 2n grid points, no three on a common line, for the target n. A single configuration settles that n; failure proves nothing.

**Checker (seconds).** For every triple of chosen points, assert they are not collinear (cross product of the two difference vectors nonzero). O((2n)^3) with exact integer arithmetic, or O((2n)^2) via a slopes-from-each-point hash. Seconds.

**Search plan.** Backtracking column by column placing two points per column with an incremental collinearity check; symmetry breaking under the grid's dihedral group and the known central-symmetry heuristics; SAT/CP with a forbidden-triple clause set (or lazily added collinear triples); simulated annealing repairing near-solutions. Seed from constructions that give 2n for nearby n.

**Prior art (verify).** The no-three-in-line problem asks for 2n points on the n x n grid with no three collinear; solutions are known for many small n but not all, and it is conjectured (Guy-Kelly) that 2n is unachievable for large n. See Achim Flammenkamp's no-three-in-line pages for the table of solved and open n. Confirm the target n is open (verify).
