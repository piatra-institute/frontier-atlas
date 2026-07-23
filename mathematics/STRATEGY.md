# Strategy - mathematics program

Intelligence-rich, resource-poor. We pick problems where a SOTA reasoning model plus a workstation plus disciplined verification produces a certified result no one else has. Every claim here is settled on-machine by a proof, an exact certificate, or an exhaustive search.

## Selection criteria

1. **Checkability** - every step certifiable (DRAT/LRAT SAT traces, exact/interval arithmetic, isomorph-free enumeration, Gröbner/Positivstellensatz certificates, Lean proofs). Dominant.
2. **Finiteness / algebraicity** - finite configurations, polynomial systems, and exact data beat open-ended analysis.
3. **Bounded scope** - a crisp target value, theorem, or counterexample, not a theory to build.
4. **Continuity with the original eleven** - Ramsey/extremal, finite geometry, packing, additive combinatorics, designs/codes, and one algebra strand.
5. **Crank distance** - obscure-but-precise, not the poisoned flagship genre.

## The original eleven as calibration

The 01-11 sprint set the house standard: certified partial results (a finite reduction, an exact obstruction, a verified construction, a near-miss with replay checkers) delivered with independent verifiers and SHA-256 manifests, and honest reports that state plainly when the headline problem was not resolved. Two lessons are in the template:

- **Preserve the search source** (Hadamard-668 lost its enumeration source; the audit record survived but was not reproducible).
- **Leave a `NEXT_STEPS.md`** at the frontier when pausing (the Moore-57 pattern).

## Operating rules

1. **Certified partial results are the product.** Full resolutions are windfalls. Every session ends with something independently checkable that did not exist before: a bound with a proof trace, an exact enumeration, an obstruction certificate, a verified extremal configuration.
2. **Re-verify before every session.** Bounds and records move, and adjacent problems fall: Erdős-Faber-Lovász (2021), the sensitivity conjecture (2019), Kaplansky's unit conjecture (disproved 2021), and Gerver's moving-sofa optimality (claimed 2024 - verify) all closed recently.
3. **Everything is auditable.** Exact/certified computation for claims, independent replay checkers, SHA-256 manifests, preserved source.
4. **Honest reporting is non-negotiable.** Reports state up front when the headline problem was not resolved; numerical or single-case results are never dressed as proofs.
5. **Promote and demote freely.** When a session shows a problem is softer or harder than expected, note it here; the tractability ordering is a prior, not a contract.

## Tractability tiers (a prior, not a schedule)

- **Tier 1 - machine-checkable ground truth, best starting points:** Schur S(6) (12), cap set n=7 (17), no-three-in-line (27), MOLS(10) (34), maximal determinant (38), SRG existence (28), Costas arrays (37), Tammes / circle packing (24, 26). SAT and exact-search shaped, like R(5,5).
- **Tier 2 - strong footholds, exact data or optimization structure:** the Ramsey/van der Waerden numbers (13-16), Heilbronn (22), Zarankiewicz/Guy crossing numbers (30, 31), optimal/covering codes (35, 36), Lehmer (40), Alon-Tarsi (43), Thomson (50).
- **Tier 3 - crisp but proof-heavy:** Erdős-Straus (18), Singmaster (21), Borsuk threshold (23), Reinhardt (25), second-neighbourhood (32), Casas-Alvero (41), Markov uniqueness (42), Rota basis (44), Erdős-Moser (45), 1/3-2/3 (46), Ryser-Brualdi-Stein (47), sunflower (48), and the labeling/design existence problems (33, 39, 29, 49).

## Escalation pattern per problem

1. Reproduce the known frontier exactly with our own verified toolchain (validates the pipeline cheaply).
2. Extend the certified frontier by the smallest nontrivial increment (one more value, one more case, a tighter bound with a proof trace).
3. Mine the extended data for structure (the [sym] step) and form a precise conjecture.
4. Attack the conjecture with certificates; only then attempt the headline result.
