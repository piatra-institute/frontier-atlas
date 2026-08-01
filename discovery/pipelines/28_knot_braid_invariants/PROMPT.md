# Batch sweep: refute knot-invariant relation conjectures on tabulated knots

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit tabulated knot violating a stated invariant inequality/relation, or hardened survivors. Refutation is a named-knot witness. (Lower yield: recomputing some invariants is nontrivial, though still seconds per knot; note this.)

**Family + panel.** Prime knots from the standard tables; invariants: crossing number, signature σ, determinant, genus (Seifert and slice), unknotting number, braid index, Alexander/Jones/HOMFLY polynomials, Rasmussen s-invariant, and the Ozsvath-Szabo tau. Anchor questions: does the Jones polynomial detect the unknot (open — verify no nontrivial tabulated knot has trivial Jones), and slice-ribbon for small slice knots (open).

**Enumerate / source.** The KnotInfo database (Livingston-Moore), which tabulates these invariants for prime knots to 12+ crossings (counts per crossing number: 3:1, 4:1, 5:2, 6:3, 7:7, 8:21, 9:49, 10:165, 11:552, 12:2176 — cross-check on load). Read invariants as columns; recompute the ones with algorithmic definitions.

**Conjecture generation.** Test relation conjectures across columns: bounds between σ, genus, s, tau, determinant, and braid index (e.g. |σ|/2 ≤ genus, |s| ≤ 2·genus, tau vs s equalities); flag any tabulated knot violating a claimed inequality. Also scan for a nontrivial knot with trivial Jones (a Jones-unknot-detection counterexample).

**Adversarial families.** Torus knots, twist and pretzel knots, cables and connected sums (predictable invariants, good for cross-checks), and the historically tricky knots (e.g. 8_19, mutant pairs).

**Checker (exact).** Recompute algorithmically-defined invariants (Alexander/Jones from a braid word or PD code, signature from the Seifert form) with SnapPy/Sage, exact where the invariant is integer/polynomial. A refutation is a KnotInfo knot certified against a stated relation.

**Verification discipline.** Generator is not verifier: recompute each hit's invariants from the diagram independently of the tabulated value and require agreement. Cite KnotInfo (with access date) and each relation's source or mark "could not verify." Report candidates generated / broken / survived, with knot names.
