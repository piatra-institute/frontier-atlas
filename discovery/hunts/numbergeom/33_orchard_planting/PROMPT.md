# Orchard configuration with more 3-point lines than the record

**Find.** A set of n points in the plane with more lines containing exactly three of the points (3-rich lines) than the best published orchard-problem value t_3(n), for an n where the maximum is unknown.

**What counts as a win (one-sided).** One n-point configuration whose count of exactly-3-point lines exceeds the current record. A single better configuration improves the lower bound; failure proves nothing.

**Checker (seconds).** Group the points by line (for every pair, the line through it; canonicalize by exact rational or integer coordinates), count lines with exactly three incident points; assert no line has more than three if the strict orchard variant is used. Exact arithmetic; O(n^3) or O(n^2 log n).

**Search plan.** Build from cubic-curve constructions (points on an elliptic curve with the group law forcing collinear triples), then perturb / augment; local search adding points that create many new 3-lines without 4-lines; use rational point sets so incidences certify exactly. Evolutionary search over point sets scored by t_3.

**Prior art (verify).** The orchard-planting problem asks for the maximum number of 3-point lines among n points; the asymptotic maximum is now known (Green-Tao), but exact values and best constructions for specific small and moderate n are open and tabulated. See Burr-Gruenbaum-Sloane and the Green-Tao orchard paper. Confirm the record for the target n (verify).
