# Strategy - informatics program

Intelligence-rich, resource-poor. We pick problems where a SOTA reasoning model plus a workstation plus disciplined verification produces a certified result no one else has. Most open problems in theoretical CS come with a crisp cost measure and an on-machine verifier; SAT solvers, exact enumeration, and machine-checked proof are its own instruments.

## Selection criteria

1. **Checkability** - every step certifiable (DRAT/LRAT SAT traces, exhaustive/canonical enumeration, exact LP/SDP certificates, formal proofs). Dominant.
2. **Crisp cost measure** - comparators, gates, multiplications, states, T-count, code distance: an integer to pin down, not an asymptotic to argue.
3. **Bounded scope** - a specific optimal value, record, or existence question, not a theory to build.
4. **Distinct from mathematics** - complexity, algorithms, automated reasoning, and quantum computation; not the combinatorics/designs/classical-codes territory the maths program owns.
5. **Crank distance** - obscure-but-precise, with an active record-tracking community rather than a poisoned flagship.

## The record-drift warning (sharper here than anywhere)

CS records move faster than any other field in the atlas. In 2023-2025 alone: BB(5) was settled (47,176,870; Coq-verified, 2024), matrix-multiplication decompositions shifted (AlphaTensor and flip-graph methods found new small-format schemes), sorting-network bounds advanced, and Conway's Life reached omniperiodicity and new spaceship results. Treat every prior-art figure in a prompt as stale until re-checked against the current literature and the community record trackers before a session begins.

## Operating rules

1. **Certified partial results are the product.** Full resolutions are windfalls. Every session ends with something independently checkable that did not exist before: a strictly improved record with a proof trace, an exact optimal value, a matching lower bound, a verified construction, an exhaustive nonexistence result.
2. **Re-verify before every session** (see the drift warning).
3. **Everything is auditable.** Exact/certified computation for claims, independent replay checkers, SHA-256 manifests, preserved source.
4. **Honest reporting is non-negotiable.** State up front whether the standard was met, whether a record was strictly improved, and in which model of computation. A heuristic-looking optimum or an unreplayable solver run is never presented as certified.
5. **Cite the baseline you beat.** Record its value, source, and access date so the claimed gain is unambiguous.

## Tractability tiers (a prior, not a schedule)

- **Tier 1 - machine-checkable ground truth, best starting points:** sorting networks (01), APN permutation (08), busy beaver (23), superpermutations (34), T-count synthesis (36), Černý reset words (49), covering arrays (35). SAT / exact-search shaped with live record trackers.
- **Tier 2 - strong footholds, exact-search or algebraic structure:** matrix-multiplication rank (03), addition chains (04), bent/low-uniformity functions (10, 11), state complexity (29), Wang tiles (25), quantum code parameters (38), selection networks (46), octal games (48).
- **Tier 3 - crisp but proof-heavy:** the complexity separations and lower-bound problems (16-22), matrix rigidity (07), universal machines (24), rewriting termination (28), Life constructions (31-33), magic-state distillation (40), stabilizer rank (41), pattern avoidance (50).

## Escalation pattern per problem

1. Reproduce the current record/frontier exactly with our own verified toolchain (validates the pipeline and the baseline).
2. Extend the certified frontier by the smallest nontrivial increment (one more comparator saved, one more value, a tighter lower bound with a proof trace).
3. Mine the extended data for structure (the [sym] step) and form a precise conjecture.
4. Attack the conjecture with certificates; only then attempt the headline result.
