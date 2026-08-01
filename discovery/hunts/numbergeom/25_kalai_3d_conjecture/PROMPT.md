# Centrally symmetric polytope with fewer than 3^d faces

**Refute.** Kalai's 3^d conjecture: find a centrally symmetric convex d-polytope (given by an explicit vertex list, symmetric under x -> -x) whose total number of nonempty faces (all dimensions, including the polytope itself) is strictly less than 3^d.

**What counts as a win (one-sided).** One centrally symmetric d-polytope with total face count below 3^d. A single witness refutes the conjecture; failure proves nothing.

**Checker (seconds).** Verify central symmetry of the vertex set, compute the full face lattice exactly (rational arithmetic), and count nonempty faces of every dimension; assert the total is < 3^d. Feasible and exact for small d; independent recount via a second face-enumeration routine.

**Search plan.** Search centrally symmetric vertex configurations in small d (d = 5, 6, 7): perturb Hanner / Hansen / cross-polytope-like examples that are known to be tight at exactly 3^d; local moves on symmetric vertex sets scored by face count; test near-tight candidates first. Exact face enumeration only on finalists.

**Prior art (verify).** Kalai's 3^d conjecture asserts every centrally symmetric d-polytope has at least 3^d nonempty faces, with equality for Hanner polytopes. It is proven in low dimensions and for special classes but open in general. See Gil Kalai's 3^d conjecture and Sanyal-Werner-Ziegler on the equality cases. Open (verify).
