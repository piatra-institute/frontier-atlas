# Integer-distance point set beating the record for fixed n

**Find.** A set of n points in the plane, no three collinear and no four concyclic, with all pairwise distances integers, of smaller diameter than the best published such configuration for that n (an Erdos-type integral point set in general position).

**What counts as a win (one-sided).** One general-position integral point set of n points with diameter below the current record. A single smaller-diameter configuration beats the record; failure proves nothing.

**Checker (seconds).** For all pairs verify the squared distance is a perfect square (isqrt), so the distance is an integer; verify no three points are collinear (nonzero area determinant) and no four are concyclic (zero of the circumcircle determinant excluded); compute the diameter. Exact integer arithmetic.

**Search plan.** Build integral point sets from Heronian triangles glued along integer cevians / from rational points on circles scaled to clear denominators; extend a base set by adding a point at integer distance to all current points (a simultaneous Pell-like / Diophantine condition), searching a bounded region; local search minimizing diameter. Seed from the record configurations.

**Prior art (verify).** Erdos and Ulam asked about integral point sets in general position; minimum-diameter configurations for each n are tabulated as records and are not proven optimal for larger n. See Kreisel and Kurz on integral point sets, and Harborth's surveys. Confirm the record diameter for the target n (verify).
