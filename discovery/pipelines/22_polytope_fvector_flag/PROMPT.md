# Batch sweep: refute polytope f-vector and flag conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit polytope violating a stated f-vector/flag inequality, or hardened survivors. Refutation is the clean win. (Lower yield: witnesses need a realizability certificate; note this honestly.)

**Family + panel.** Simplicial and general convex polytopes and lattice polytopes in low dimension; data: f-vector (face counts f_i), flag f-vector, h-vector, cd-index coefficients, and the h*-vector (Ehrhart δ-vector) of lattice polytopes. Anchor: Kalai's 3^d conjecture (a centrally symmetric d-polytope has ≥ 3^d nonempty faces; open) and h*-vector unimodality (open in general).

**Enumerate.** Combinatorial types of small polytopes: all d-polytopes with few vertices (d=3,4) from the enumerations of simplicial/general polytopes (e.g. via placing-triangulations or the polymake/plantri catalogues); lattice polytopes with few boundary/interior points. Cross-check 3-polytope counts against the Steinitz/plantri triangulation counts.

**Conjecture generation.** Test 3^d on centrally symmetric constructions; test flag-f nonnegativity (cd-index) and h*-unimodality across generated lattice polytopes; auto-fit inequalities among f_i and h_i. Many h*-unimodality claims fail for non-IDP (non-integrally-closed) polytopes — target those.

**Adversarial families.** Hansen/Hanner polytopes and cross-polytope variants (extremal for 3^d), free sums and products, dilated simplices with removed lattice points, and cyclic polytopes (extremal f-vectors).

**Checker (exact).** Compute the full face lattice exactly (double-description / convex hull with exact rational arithmetic); compute h*-vector by exact Ehrhart enumeration. A refutation is a polytope with a certified vertex description violating the inequality. Emit vertex coordinates.

**Verification discipline.** Generator is not verifier: recompute the face lattice with a second exact hull routine and confirm the polytope is realized by the given rational vertices; recompute h* by two Ehrhart methods. Cite each conjecture. Report candidates generated / broken / survived, with exact vertex data.
