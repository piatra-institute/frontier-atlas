# Strategy - why this ordering, and how we spend effort

Resource-poor, intelligence-rich. We do not out-compute big labs; we pick problems where a SOTA reasoning model plus a workstation plus disciplined verification produces a result no one else has. The strongest predictor of AI success on open problems is machine-checkable ground truth, so the ranking optimizes for it.

## Ranking criteria

1. **Checkability** - can every claimed step be certified (SAT/DRAT traces, exact arithmetic, interval bounds, CAS identities)? Dominant.
2. **Finiteness/algebraicity** - finite configurations, polynomial systems, and exact series data beat open-ended analysis.
3. **Bounded scope** - a crisp target theorem or constant, not a field to develop.
4. **Payoff** - practical utility (QKD, fusion, materials) or Jacobian-style foundational weight.
5. **Crank distance** - obscure enough that head-on assaults are not a crowded, poisoned genre.

## Tiers

- **Tier 1 (01-10):** certified search and symbolic mining on finite or algebraic structures; serious partial result plausible in weeks, breakthrough in months. Worked first, in order.
- **Tier 2 (11-25):** exact data or optimization structure exists (series coefficients, integrable machinery, variational formulations), but the gap to a theorem is wider. Worked as Tier 1 lines block or saturate.
- **Tier 3 (26-37):** certificate pipeline defined (spectral bounds, bootstrap/optimization, computer-assisted proofs) but heavy; chosen when a Tier 1-2 result suggests a transferable technique.
- **Tier 4 (38-50):** deep proof problems kept for opportunistic strikes; a new lemma elsewhere, a literature shift, or a model-capability jump can promote one. No frontal assaults.

## Operating rules

1. **Certified partial results are the product.** Full resolutions are windfalls. Every session ends with something independently checkable that did not exist before: a certificate, an exact reduction, an obstruction, a verified table entry.
2. **Re-verify before every session.** Open status drifts monthly. Prompts state prior art "as of mid-2026"; treat as stale until confirmed.
3. **Everything is auditable.** Exact arithmetic for claims, independent dual verifiers, SHA-256 manifests, preserved source.
4. **Honest reporting is non-negotiable.** Reports state up front when the problem was NOT resolved. Restricted/numerical results are never dressed as solutions.
5. **Leave a trail.** A paused attack gets a `NEXT_STEPS.md` with the exact remaining obligations (the Moore-57 pattern).
6. **Promote and demote freely.** The ranking is a prior, not a contract. When a session reveals a problem is softer or harder than ranked, renumber the priority in `README.md` (folders keep their names) and note why here.

## Escalation pattern per problem

1. Reproduce the known frontier exactly (validates the toolchain).
2. Extend the certified frontier by the smallest nontrivial increment (new bound, new table entry, one more case).
3. Mine the extended data for structure (the [sym] step) and formulate a precise conjecture.
4. Attack the conjecture with certificates; only then attempt the headline theorem.
