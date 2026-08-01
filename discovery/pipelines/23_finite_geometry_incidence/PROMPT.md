# Batch sweep: refute finite-geometry incidence conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit point/line configuration beating a stated incidence bound or realizing a claimed-impossible structure, or hardened survivors. Refutation is the clean win. (Cap sets in AG(n,3) are explicitly excluded as a hardened record; this pipeline targets other, under-tested incidence questions.)

**Family + panel.** Point sets in the real/rational plane and in projective planes PG(2,q); quantities: number of ordinary lines (exactly-2-point lines), number of 3-point lines t3 (orchard problem), configuration types n_k, blocking-set sizes, and arc/cap sizes in PG(2,q).

**Enumerate.** Exhaustive small configurations: all n_3 configurations for small n via the Betten-Brinkmann-Pisanski style enumeration; all point sets of size ≤ ~12 in small grids for the orchard count; arcs in PG(2,q) for small prime-power q by exhaustive/backtracking search. Cross-check known orchard values (max t3 for small n) before sweeping.

**Conjecture generation.** Test the orchard maximum t3(n) against constructions; test the Green-Tao ordinary-lines bound on small sets; sweep arc/blocking-set sizes against the known extremal values in PG(2,q) for small q (where a beating configuration would be a genuine surprise). Auto-generate candidate configurations by perturbing extremal ones.

**Adversarial families.** Cubic-curve point sets (the orchard-optimal families), Hesse configuration and its relatives, conics and their secants in PG(2,q), and Sylvester-type near-pencils.

**Checker (exact).** Compute all collinearities exactly (rational or finite-field determinants = 0), count lines by multiplicity, and verify arc/blocking properties combinatorially. A refutation is a configuration certified to beat a stated count. Emit exact coordinates.

**Verification discipline.** Generator is not verifier: recompute all incidences with exact arithmetic in a second routine; confirm no three-point-line miscount from float. Cite each bound (orchard tables, Green-Tao, PG(2,q) arc records) or mark "could not verify." Report candidates generated / broken / survived, with coordinates.
