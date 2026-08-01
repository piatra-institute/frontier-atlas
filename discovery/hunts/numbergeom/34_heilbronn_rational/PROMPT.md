# Heilbronn configuration beating the record for fixed n

**Find.** A placement of n points in the unit square (rational coordinates) whose minimum triangle area over all triples exceeds the best published Heilbronn value h(n) for that n.

**What counts as a win (one-sided).** One n-point set whose smallest triangle area is strictly above the current record. A single better configuration improves the lower bound; failure proves nothing. (This is a record-improvement target, but the witness is exactly checkable.)

**Checker (seconds).** For every triple compute twice the signed area exactly (integer determinant after clearing denominators), take the minimum absolute value, divide by the common denominator scale; assert it exceeds the record. O(n^3) exact rational arithmetic.

**Search plan.** Local optimization in floating point maximizing the minimum triangle area (move points off the smallest triangles), then snap to nearby rationals and re-certify exactly; multi-start / simulated annealing; seed from the published record configurations and perturb. Optionally rescale to an integer grid and search there so all areas are integers.

**Prior art (verify).** The Heilbronn triangle problem seeks the placement of n points in the unit square maximizing the minimum triangle area; exact optima are known only for very small n, and larger n are best-known configurations (Goldberg; Yang; Comellas-Yebra; Dress-Yang; Cantrell). Confirm the current record for the target n before starting (verify).
