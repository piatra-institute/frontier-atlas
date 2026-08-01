# Kissing configuration beating the record in a fixed dimension

**Find.** A set of unit vectors in R^d with pairwise angular separation at least 60 degrees, of size larger than the best published kissing-number lower bound, for a dimension d (e.g. 13, 14) where the kissing number is not known exactly.

**What counts as a win (one-sided).** One set of s unit vectors with all pairwise inner products <= 1/2, with s above the current record. A single larger configuration improves the lower bound; failure proves nothing.

**Checker (seconds).** For all pairs, assert (after clearing the common norm) the scaled inner product satisfies the >= 60-degree condition exactly. With vectors in a lattice or over a small number field, use exact arithmetic. O(s^2 d); seconds for the relevant s.

**Search plan.** Extract kissing configurations from record lattices (minimal vectors) and from non-lattice packings, then augment by local search / SDP-guided placement adding vectors that keep all angles >= 60 degrees; simulated annealing on the sphere with exact snapping to a lattice. Evolutionary recombination of near-configurations.

**Prior art (verify).** Kissing numbers are known exactly only in dimensions 1, 2, 3, 4, 8, 24; other small dimensions have gaps between best known lower and upper bounds, and lower bounds have improved recently (e.g. dimensions 11-14 in the 2020s). See Conway-Sloane, SPLAG, kissing-number tables, and recent lower-bound papers. Avoid dimensions already worked here; confirm the record (verify).
