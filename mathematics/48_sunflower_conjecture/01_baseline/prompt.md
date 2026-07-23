# PROMPT FOR CERTIFYING SMALL-\(k\) SUNFLOWER-FREE BOUNDS AND EXTREMAL FAMILIES

## The Erdős–Rado sunflower conjecture: exact small cases and certified bounds

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 48 of 50
**Area:** order theory & extremal set systems
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A sunflower is a family of sets sharing a common core, with pairwise intersections all equal to that core and the remaining petals pairwise disjoint. The Erdős–Rado sunflower conjecture asserts that a family of more than \(c^k\) distinct \(k\)-element sets must contain a sunflower with three petals, for some absolute constant \(c\).

This is a proof problem, universal over all \(k\), and the exponent has not been closed: Erdős–Rado (1960) gave \(k!\,2^k\), and the 2019–2021 breakthrough of Alweiss–Lovett–Wu–Zhang, simplified by Rao and refined by Bell–Chueluecha–Warnke, reached roughly \((C\log k)^k\), still short of \(c^k\). Closing the exponent is not a realistic session product and this prompt says so plainly.

What is machine-checkable is the extremal function \(f(k,3)\) for small \(k\): its exact value is pinned by a construction plus a matching exhaustive or LP-duality upper bound, and the extremal sunflower-free families can be enumerated up to isomorphism. Those certified small-\(k\) facts, and certified numeric improvements to the finite lemmas inside the general bound, are the deliverable.

## 1. Exact problem statement

Fix a ground set and consider distinct sets over it.

A **sunflower with \(p\) petals** (a \(p\)-sunflower) is a family \(\{S_1,\dots,S_p\}\) of distinct sets together with a **core** \(Y\) such that
\[
S_i\cap S_j=Y\quad\text{for all }i\ne j,
\]
so the **petals** \(S_i\setminus Y\) are pairwise disjoint; the core \(Y\) may be empty (then the \(S_i\) are pairwise disjoint). A family is **\(p\)-sunflower-free** if it contains no \(p\)-sunflower.

For integers \(k\ge1,\ p\ge2\) define the extremal function
\[
f(k,p)\;=\;\max\bigl\{\,|\mathcal F|:\ \mathcal F\ \text{a family of distinct }k\text{-sets with no }p\text{-sunflower}\,\bigr\}.
\]
The principal case is \(p=3\).

**Sunflower lemma (Erdős–Rado 1960).**
\[
f(k,p)\ \le\ k!\,(p-1)^k;\qquad\text{in particular}\quad f(k,3)\ \le\ k!\,2^k.
\]

**Conjecture (Erdős–Rado).** For each \(p\) there is a constant \(c=c(p)\) with
\[
f(k,p)\ \le\ c(p)^{\,k}\qquad\text{for all }k,
\]
and in the main case an absolute \(c\) with \(f(k,3)\le c^k\).

**Degenerate small case.** For \(k=1\), any three distinct singletons are pairwise disjoint, hence a \(3\)-sunflower with empty core, so \(f(1,3)=2\). For \(k=2\), a \(3\)-sunflower of edges is either three pairwise-disjoint edges (a matching) or three edges through a common vertex (a star), so a \(3\)-sunflower-free family of pairs is a graph with no matching of size \(3\) and no vertex of degree \(3\) - an exactly finite extremal problem.

**ILP form of the extremal value.** With a Boolean variable \(z_S\in\{0,1\}\) for each \(k\)-set \(S\) over ground set \([m]\),
\[
f(k,3)\ =\ \max\ \sum_{S} z_S
\quad\text{s.t.}\quad
z_{S_1}+z_{S_2}+z_{S_3}\le 2\ \ \text{for every triple }\{S_1,S_2,S_3\}\ \text{forming a sunflower},
\]
for \(m\) large enough not to constrain the optimum. This is the object the SAT/ILP certificates in section 3 target.

The function \(f(k,3)\) is well-defined and finite for every \(k\); for fixed \(k\) it is an exact integer decided by finite search. No asymptotic paraphrase is an acceptable target; the objects are the exact values \(f(k,3)\), the certified upper/lower bounds, and the extremal families attaining them.

## 2. Resolution standard

A complete resolution is a **proof** of \(f(k,3)\le c^k\) for an absolute constant \(c\) and all \(k\) (or a proof it is impossible, i.e. a superexponential lower bound). This is infinitary and cannot be reached by search; the accepted certificate is a written proof, Lean-formalizable, whose finite lemmas are exact. **Closing the exponent is the conjecture itself and is not a session product.**

**Certified form (the session product).** For a fixed \(k\) (and \(p=3\)), a **certified sunflower-free extremal certificate** consists of two matching parts:

- **Lower bound:** an explicit family of \(k\)-sets, machine-verified to be \(3\)-sunflower-free (no triple forms a sunflower), of size \(f\).
- **Upper bound:** either an exhaustive isomorph-free search proving no \(3\)-sunflower-free family of \(k\)-sets has size \(f+1\), with a **DRAT/LRAT** UNSAT proof, or an exact rational **LP/ILP duality** certificate (a feasible dual solution) bounding \(f(k,3)\le f\).

When the two parts meet, \(f(k,3)=f\) is certified exactly.

**Not accepted as resolution.**

- Any asymptotic improvement to the general upper bound represented as "resolving the conjecture" - closing the exponent is the conjecture, not a partial result.
- A construction (lower bound) without a matching certified upper bound, presented as "the extremal number".
- A floating LP bound with no exact feasible dual; certification requires exact rational duality or an UNSAT proof.
- A single non-canonical extremal example presented as a classification of extremal families.
- Conflating the group-theoretic "sunflower-free set" notion (pairwise-intersection-equal triples in \([3]^n\), Naslund–Sawin) with the \(f(k,3)\) extremal function - they are different objects.

## 3. Graded partial-result targets

- **P1 - reproduce known small values.**
  Certify the exact \(f(k,3)\) for \(k=1,2,3\) (and any further literature values) with matching construction + exhaustive-search upper bound.
  *Certificate:* verified \(3\)-sunflower-free extremal family plus a DRAT UNSAT proof (or exact LP dual) for the \(+1\) infeasibility; cross-check against Abbott–Hanson–Sauer values.

- **P2 - a new certified exact value.**
  Establish \(f(k,3)\) for the smallest \(k\) currently open or only bounded (e.g. \(k=4\) or \(5\)) over a sufficiently large ground set: lower bound by verified construction, upper bound by SAT/ILP with DRAT or exact dual.
  *Certificate:* both parts, with a proof that the ground set is large enough not to constrain the maximum.

- **P3 - certified LP/SDP bounds across a range.**
  Exact rational LP (or SDP with rational rounding) upper bounds on \(f(k,3)\) for a band of \(k\), reported against \(c^k\).
  *Certificate:* exact feasible dual solutions, re-verified by a second solver/CAS.

- **P4 - certified extremal families.**
  Enumerate, up to isomorphism, all extremal \(3\)-sunflower-free families for small \(k\), and characterize their structure (relation to Deza's theorem, near-pencils, sunflower-free designs).
  *Certificate:* isomorph-free enumeration with completeness argument and verified sunflower-freeness.

- **P5 - bounded-universe and \(p>3\) cases.**
  Exact \(f(k,p)\) over a bounded ground set \([m]\) for small \(m,k,p\), by exhaustive search with certificate; and small-\(k\) values for \(p=4\).
  *Certificate:* exhaustive log with DRAT for the tight upper bound.

- **P6 - certified numeric improvement inside the general bound (strongest short of full).**
  For a specific structured regime, a checkable improvement to the constant in the Alweiss–Lovett–Wu–Zhang / Rao "robust sunflower" machinery, with the finite density base cases certified by exact arithmetic - an honest numeric gain, **not** a change of exponent.
  *Certificate:* the improved lemma with its finite computations certified and independently replayed.

## 4. Known results and prior art

- **Erdős–Rado (1960).** \(f(k,p)\le k!\,(p-1)^k\); Erdős offered \$1000 for the \(p=3\) exponent. Small refinements to constants followed (Kostochka, 1990s, verify).
- **Alweiss–Lovett–Wu–Zhang (2019; Annals of Mathematics 2021).** A bound of the form
\[
f(k,p)\ \le\ \bigl(C\,p\log k\bigr)^{k}\ \ \text{(roughly }(\log k)^{k(1+o(1))}\ \text{for fixed }p),
\]
via "robust sunflowers" / spread families.
- **Rao (2020).** A shorter proof, \(f(k,p)\le(Cp\log(pk))^{k}\) (verify constant form).
- **Bell–Chueluecha–Warnke (2021).** Further constant refinements (verify). Tao's blog gives an exposition; Bloom's notes track the current record.
- **The gap in one line.** The current knowledge ladder for \(p=3\) is
\[
c^{\,k}\ \le\ f(k,3)\ \le\ \bigl(C\log k\bigr)^{k}\ \ll\ k!\,2^k,
\]
where the left inequality is the (easy) exponential lower construction, the middle is Alweiss–Lovett–Wu–Zhang / Rao, and the conjecture asserts the middle can be brought down to \(c^k\).
- **Small exact values.** Abbott–Hanson (early 1970s) and Abbott–Hanson–Sauer computed \(f(k,3)\) for small \(k\); Deza's theorem characterizes maximal \(k\)-uniform families with all pairwise intersections of the same size (relevant to extremal structure). Confirm the exact small-\(k\) table before claiming any value as the frontier.
- **Related (distinct notion).** Naslund–Sawin (2017) bounded "sunflower-free" families in \([3]^n\) by a cap-set-style slice-rank argument - a different extremal object, listed to avoid conflation.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** The general upper bound has moved repeatedly since 2019; confirm the current record form and the small-\(k\) exact values before scoping targets. No fabricated arXiv IDs, DOIs, or page numbers are to be introduced.

## 5. Attack plan

- **`[proof]` with computational support.** The mode is proof, but small cases are decided by exhaustive computation. Over a ground set \([m]\), enumerate families of \(k\)-sets; reject isomorphs with a `nauty`/`Traces` canonical form on the set-system's bipartite incidence (or hypergraph) representation.
- **SAT/ILP.** A Boolean variable per candidate \(k\)-set; for each triple that would form a sunflower, a clause forbidding all three chosen; maximize the count (MaxSAT) or decide a size threshold (SAT), emitting **DRAT** for the tight-upper-bound UNSAT. The fractional relaxation
\[
f^\*(k,3)=\max\Bigl\{\textstyle\sum_S y_S:\ 0\le y_S\le1,\ y_{S_1}+y_{S_2}+y_{S_3}\le2\ \text{on sunflower triples}\Bigr\}\ \ge\ f(k,3)
\]
gives an LP upper bound whose exact rational optimal dual is a certificate; a second solver re-checks it.
- **CAS.** SageMath / Python for construction, canonical forms, and exact LP; SOS/Positivstellensatz via SDPA-GMP with rational rounding for any P6 lemma.
- **Ground-set adequacy.** A finite search is only valid if the ground set \([m]\) is large enough that no larger optimum lives on more points. Since a \(3\)-sunflower-free family has at most \(k!\,2^k\) sets by Erdős–Rado, its support satisfies
\[
m\ \le\ k\cdot f(k,3)\ \le\ k\cdot k!\,2^k,
\]
giving an explicit (crude) adequacy bound; sharper problem-specific bounds must accompany any claimed exact \(f(k,3)\).
- **One-workstation scope.** Ground set up to \(m\approx12\text{–}15\) and \(k\le5\) keeps \(\binom{m}{k}\) and the sunflower-triple constraint set within SAT range; beyond that the encoding explodes. The exponent-closing question is beyond any finite computation and is stated as such.
- **Failure modes.** Combinatorial explosion in \(m,k\); MaxSAT scaling on the optimization form; ground set chosen too small (an artificial cap masquerading as \(f(k,3)\)); no finite result can close the exponent - the honest boundary of the mode.

## 6. Verification and auditability requirements

1. **Exact/certified computation.** Sunflower-freeness of a family is checked exactly over all triples; upper bounds rest on DRAT UNSAT proofs or exact rational LP duals; floating point is exploration only.
2. **Independent verification.** A standalone checker, independent of the search, re-verifies sunflower-freeness of every claimed family and runs a DRAT checker on each UNSAT proof; LP duals are re-checked by a second solver/CAS.
3. **Reproducibility.** Ground-set sizes, encodings, canonical-form definitions, solver versions, and seeds recorded; SHA-256 manifest over every family file, certificate, and proof trace.
4. **Preservation.** Enumeration and encoding source is part of the record (the Hadamard-668 lost-source lesson). A value established only over a bounded universe is stated as such, with the ground-set-adequacy argument attached or its absence flagged.
5. **Honest reporting.** The report states up front that the exponent is not closed and that the results are exact small-\(k\) values, certified bounds, and extremal families. No asymptotic improvement is ever represented as resolving the conjecture.

### Honest calibration

Closing the exponent from \((\log k)^k\) to \(c^k\) is one of the hard open problems in extremal set theory and will not fall in a session - this prompt does not pretend otherwise. The product is exact: one or two new certified values of \(f(k,3)\), a clean enumeration of small extremal families, and honest LP/SDP bounds. P6 (a certified numeric improvement inside the general machinery) is a real stretch and, even if achieved, is a constant gain, never an exponent.
