# PROMPT FOR EXACT COUNTS OF COMPLETE MAPPINGS AND ORTHOMORPHISMS

## Enumerating complete mappings / orthomorphisms of specific groups, with extra properties and MOLS consequences

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 15 of 50
**Area:** Boolean & cryptographic functions
**Modes:** `[search]` `[enum]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A complete mapping of a group is a permutation \(\theta\) for which \(x\mapsto x\cdot\theta(x)\) is again a permutation; its existence controls whether the group's Cayley table has an orthogonal mate, i.e. whether it yields a pair of mutually orthogonal Latin squares. **The existence question is settled:** the Hall–Paige conjecture - a finite group has a complete mapping iff its Sylow 2-subgroup is trivial or non-cyclic - was **proven** (Wilcox, Evans, and Bray, ~2009, using the classification of finite simple groups). This prompt therefore does **not** target existence. It targets the parts that remain open and are matched to certified counting and enumeration: **exact numbers** of complete mappings / orthomorphisms of specific groups, orthomorphisms carrying **extra structure** (strong complete mappings, complete mappings of prescribed cycle type, orthomorphism graphs), and the resulting **mutually-orthogonal-Latin-square** consequences. The on-machine verifier is a direct permutation-and-orthogonality check; anything short of the Section 2 standard - an uncertified count, an existence claim dressed as new - is a partial result, never a resolution. A literature gate is the mandatory first step.

## 1. Exact problem statement

Let \((G,\cdot)\) be a finite group of order \(v\), written multiplicatively (for abelian targets, additively as \((G,+)\)). A permutation \(\theta:G\to G\) is a **complete mapping** iff the map
\[
\eta:\ x\ \longmapsto\ x\cdot\theta(x)
\]
is also a permutation of \(G\). Equivalently \(\theta\) is a complete mapping iff \(\sigma(x)=x\cdot\theta(x)\) is bijective; \(\sigma\) is then called the **orthomorphism** associated with \(\theta\) (for abelian \(G\), \(\phi(x)=\theta(x)\) is an **orthomorphism** iff both \(\phi\) and \(x\mapsto x^{-1}\phi(x)\) - additively \(x\mapsto \phi(x)-x\) - are permutations; complete mappings and orthomorphisms are interchangeable via \(x\mapsto x^{-1}\)).

Refinements:
- A **strong complete mapping** is a permutation \(\theta\) such that \(\theta\), \(x\mapsto x\theta(x)\), **and** \(x\mapsto x^{-1}\theta(x)\) are all permutations.
- The **cycle type** of a complete mapping is the cycle type of \(\theta\) (or of \(\eta\)); prescribing it gives refined counting problems.
- The **orthomorphism graph** of \(G\) has orthomorphisms as vertices, adjacent when their "difference" is again an orthomorphism; cliques correspond to sets of MOLS.

**Symmetries of the count.** The set of complete mappings carries a natural action: pre- and post-composition by the holomorph \(\mathrm{Hol}(G)=G\rtimes\mathrm{Aut}(G)\) permutes complete mappings, and this action is what "up to equivalence" means when a reduced count is reported. Two functions \(\theta,\theta'\) are **equivalent** if \(\theta'=\alpha\circ\theta\circ\beta\) for suitable holomorph elements \(\alpha,\beta\) fixing the defining property; a certified reduced count must specify the exact acting group and quotient correctly.

**MOLS connection (a genuine consequence, kept computational, not the maths-program design classification).** A **Latin square** of order \(v\) is a \(v\times v\) array on \(v\) symbols with every symbol once per row and column; two are **orthogonal** if superimposing them yields all \(v^2\) ordered pairs. The Cayley table \(L_G\) of \(G\) is a Latin square; \(L_G\) has an orthogonal mate iff \(G\) has a complete mapping. A set of \(k\) pairwise-orthogonal orthomorphisms of \(G\) (a clique of size \(k\) in the orthomorphism graph, including the identity) yields \(k+1\) mutually orthogonal Latin squares (MOLS) of order \(v\) based on \(G\). The general MOLS existence question is a mathematics-program design problem; here only the *group-based* count and clique are in scope.

For an **abelian** group written additively, the definitions specialize cleanly: \(\theta\) is a complete mapping iff both
\[
\theta:\ x\mapsto\theta(x)\quad\text{and}\quad \eta:\ x\mapsto x+\theta(x)
\]
are permutations, and \(\phi\) is an orthomorphism iff \(\phi\) and \(x\mapsto\phi(x)-x\) are both permutations; the two notions correspond via \(\phi(x)=x+\theta(x)\). Both conditions are decided exactly by checking that a candidate map and one derived map are each bijections - two \(O(v)\) passes per candidate. This is why the problem is a pure exact-enumeration target with a trivial verifier and a hard search.

**The questions, adopted scope (existence excluded - see Hall–Paige).** For specified small groups \(G\) (cyclic \(\mathbb{Z}_v\) for odd \(v\), elementary-abelian \(\mathbb{Z}_p^k\), small non-abelian groups):
(i) the **exact number** of complete mappings / orthomorphisms of \(G\);
(ii) exact counts of **strong** complete mappings, or complete mappings of a **prescribed cycle type**;
(iii) the **maximum clique** in the orthomorphism graph (hence the largest MOLS set from \(G\)) and certified structure thereof. Cost: exact counts (certified enumeration), DRAT/LRAT or exhaustive-search certificates.

## 2. Resolution standard

**Literature gate (mandatory first step).** Before any search, produce a dated literature note establishing, for the target group(s), (a) that existence is settled by Hall–Paige and is *not* the object, (b) which exact counts / clique numbers are already published (Cayley–Rubin/McKay-style enumerations, OEIS sequences for orthomorphism counts of cyclic and elementary-abelian groups, the Evans monograph tables), and (c) precisely which count or structure this session will newly certify or independently confirm. A result already in the literature is a *reproduction* target (P1-level), and must be labelled as such.

This gate is the single most important instruction in the prompt: the existence question is closed, and the only defensible new results are exact counts, refined-structure counts, and clique numbers, each labelled as reproduction or novelty against the cited baseline.

A **full resolution** of a scoped instance is one of:

- **(Exact count)** the exact number \(N(G)\) of complete mappings (or orthomorphisms, or strong complete mappings, or of prescribed cycle type) of a specific \(G\), established by a certified exhaustive enumeration (isomorph-free where a symmetry quotient is claimed) whose completeness is machine-checkable, together with an independent recount;
- **(Clique/MOLS)** the exact maximum number of MOLS obtainable from \(G\) via orthomorphisms (the orthomorphism-graph clique number), with the extremal set exhibited and every pair's orthogonality recomputed, plus a certified optimality (no larger clique) proof.

Named certified forms:

- **(a) Exhaustive backtracking enumeration** with a replayable search tree / count certificate.
- **(b) SAT/#SAT or model-counting** with a certified count (DRAT for a decision sub-claim, a certified model counter for the total).
- **(c) Exhaustive/canonical enumeration** via **nauty** (on the Cayley/orthomorphism structure) or **GAP** orbit computation guaranteeing completeness of a symmetry-reduced count.
- **(d) Exact transfer-matrix / permanent-style computation** with exact integer arithmetic.

A reproduction of a published count is a P1-level validation, not a new result; a new certified count for a group whose value is not in the literature is the genuine contribution and is labelled distinctly, with the literature-gate note as evidence of novelty.

**Not accepted as resolution.**

- Any framing of **existence** as open or newly settled - Hall–Paige decides it; re-deriving existence is at most a P1 reproduction and must be labelled so.
- A "does group \(G\) have a complete mapping" investigation dressed as a research contribution - the Sylow-2 criterion answers it immediately.
- An exact-count claim from a single unreplayable search run, or a heuristic/statistical estimate (e.g. quoting the \((e^{-1/2}+o(1))|G^{\mathrm{ab}}|\,v!^2/v^v\) asymptotic) in place of the exact integer.
- A count "up to symmetry" whose symmetry quotient (isomorphisms, holomorph action) is not certified - an over- or under-count silently voids it.
- A MOLS/clique claim without recomputed pairwise orthogonality, or without a certified "no larger clique" proof.
- An orthomorphism or complete-mapping claim whose two permutation conditions are not both independently verified.
- Confusing complete mappings of \(G\) with the classification of Latin squares / MOLS as designs (mathematics-program territory) - the object here is the group-based count/structure.
- A count that does not state whether it counts raw complete mappings or equivalence classes under the holomorph action.
- A cycle-type or strong-complete-mapping count where the extra permutation condition was assumed rather than verified on each object.
- A clique claim that exhibits \(k+1\) MOLS but never certifies that \(k+2\) is impossible.
- A "new count" that on checking matches an existing OEIS term or Evans-table value - that is a reproduction, and must be labelled so, not presented as new.
- A count reported to fewer digits than the exact integer, or with the integer replaced by its floating-point/asymptotic approximation.

## 3. Graded partial-result targets

**P0 - Checker base case.** Validate the complete-mapping/orthomorphism checker on \(\mathbb{Z}_5\) (a hand-checkable case with 3 complete mappings) and confirm two independent implementations agree, before any counting at scale. *Certificate:* the enumerated complete mappings of \(\mathbb{Z}_5\) with cross-implementation agreement, matching the known value.

**P1 - Literature gate + reproduce known counts.** Deliver the dated literature note (Section 2), then independently reproduce published exact counts: the number of complete mappings/orthomorphisms of small cyclic groups \(\mathbb{Z}_v\) (odd \(v\)) and of \(\mathbb{Z}_2^k\), matching the known OEIS / Evans-monograph values. *Certificate:* certified enumeration matching published integers, with SHA-256 over the search output.

**P2 - Certified count for an open group.** Compute the exact number of complete mappings / orthomorphisms of a specific group whose count is not published (a larger cyclic \(\mathbb{Z}_v\), an elementary-abelian \(\mathbb{Z}_p^k\), or a small non-abelian group), by certified exhaustive enumeration with an independent recount. The single new exact integer, certified two ways, is the primary deliverable - a genuine addition to the OEIS/Evans record. *Certificate:* replayable search tree / model-count certificate + a second-method recount.

**P3 - Strong complete mappings / cycle type.** Exact counts of strong complete mappings, or of complete mappings of a prescribed cycle type, for a target group - refined enumerations exercising the extra permutation conditions. *Certificate:* certified enumeration with each extra condition independently verified.

**P4 - Orthomorphism-graph clique (MOLS).** Determine the clique number of the orthomorphism graph of a specific small group \(G\) (equivalently the largest MOLS family from \(G\)), exhibit the extremal set, recompute every pairwise orthogonality, and certify no larger clique exists. *Certificate:* explicit clique + a certified maximum-clique proof (exhaustive or DRAT/LRAT).

**P5 - Structure / symmetry-reduced totals.** Produce a certified count up to the natural symmetry (holomorph / automorphism action), with the quotient certified by GAP orbit computation, for a group where the raw count is otherwise infeasible. Report both the class count and, where derivable, the implied raw count via orbit sizes. *Certificate:* orbit-stabilizer bookkeeping + a Burnside cross-check.

**P6 - New MOLS or non-existence-of-larger consequence.** If a target group yields a MOLS set matching or exceeding a known bound for order \(v\), record it with full orthogonality certificates; or certify that the group-based route cannot exceed a stated count. *Certificate:* recomputed MOLS orthogonality + certified bound.

**P7 - Asymptotic sanity + exact confirmation.** For each new exact count, confirm it lands within the Eberhard–Manners–Mrazović asymptotic band as a coarse sanity check, and archive both the exact integer and the asymptotic estimate side by side (never substituting one for the other). *Certificate:* the exact count, the asymptotic value, and their ratio.

## 4. Known results and prior art

- **Existence - SETTLED.** Hall–Paige conjecture (Hall–Paige, ~1955): a finite group \(G\) has a complete mapping iff its Sylow 2-subgroup is trivial or non-cyclic. **Proven** by Wilcox, Evans, and Bray (~2009), using the classification of finite simple groups plus substantial computer algebra. *Do not target existence.* (verify the attribution and date.)
- **Asymptotic count (a bound, not the object):** the number of complete mappings of a group of order \(v\) satisfying the Hall–Paige condition is \((e^{-1/2}+o(1))\,|G^{\mathrm{ab}}|\,v!^2/v^v\) (Eberhard–Manners–Mrazović, ~2019–2022); this is asymptotic and does **not** give exact small-\(v\) integers (verify).
- **Cycle type:** the Friedlander–Gordon–Tannenbaum conjecture on the cycle type of complete mappings was proven (~2023, "Cycle type in Hall–Paige"), so which cycle types *occur* is settled; the *counts* per cycle type remain a finite exact-enumeration question (verify).
- **Sequenceable / R-sequenceable groups:** closely related structures (sequencings, harmonious groups) share the enumeration methodology and are catalogued alongside complete mappings in Evans's monograph (verify).
- **Random Hall–Paige** and further refinements (~2022–2025) (verify).
- **Exact small counts:** numbers of complete mappings / orthomorphisms of small cyclic and elementary-abelian groups are tabulated (McKay, and others; several OEIS sequences, e.g. counts of orthomorphisms of \(\mathbb{Z}_n\)) and in Evans's monograph *Orthogonal Latin Squares Based on Groups* (~2018) - the standard reference for orthomorphism graphs, counts, and MOLS-from-groups (verify sequence numbers and table values against the source).
- **MOLS link:** \(L_G\) has an orthogonal mate iff \(G\) has a complete mapping; MOLS-from-groups and the orthomorphism-graph clique problem are covered in Evans's monograph and the *Handbook of Combinatorial Designs* (verify).
- **Cyclic-group counts:** the number of complete mappings of \(\mathbb{Z}_n\) (odd \(n\)) is a well-studied sequence - small values are \(1\ (n=1)\), \(1\ (n=3)\), \(3\ (n=5)\), \(19\ (n=7)\), \(225\ (n=9)\), … - tabulated on OEIS (verify the exact sequence and its identifier).
- **Elementary-abelian and non-abelian:** counts for \(\mathbb{Z}_p^k\) and for small non-abelian groups (dihedral, quaternion where the Hall–Paige condition holds) are partially tabulated; many specific groups remain uncomputed (verify).
- **Orthomorphism-graph structure:** the clique numbers (largest MOLS from a group) are known for small orders and are the subject of the Evans monograph's tables; several are open (verify).
- **Random model:** the "random Hall–Paige" line (~2022–2025) gives distributional results, again asymptotic, not exact small-\(v\) counts (verify).

**Web-verify the headline record tables** - the exact orthomorphism/complete-mapping counts (OEIS, Evans's tables) and the post-2009 refinements (cycle type, asymptotics, random model) are actively updated; consult OEIS, Evans's monograph, and recent arXiv. **Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

`[search]` `[enum]` first computations on one workstation:

1. **Literature gate (P1).** Compile the dated note fixing existence as settled and enumerating which counts/cliques are already published (OEIS sequences, Evans's tables); state precisely the new target. This gate is a hard prerequisite - no search result is meaningful without it.
2. **Verified checkers (P1).** In **GAP** (native group support) and independently in **custom C++/SageMath**: given \(\theta\), verify it is a permutation and that \(x\mapsto x\theta(x)\) is a permutation (complete mapping), plus the extra maps for strong/cycle-type variants; verify pairwise orthomorphism-orthogonality for MOLS. Exact integer/permutation arithmetic throughout.
3. **Exhaustive enumeration (P2–P3).** Backtracking search over permutations \(\theta\) with the partial-orthogonality constraint pruned incrementally (a Latin-rectangle / list-coloring style backtrack); count exactly. For symmetry reduction quotient by the holomorph / automorphism action via **GAP**, and canonicalize the attached structure with **nauty** so a reduced count is certificate-backed.
4. **Model counting (P2).** Encode "complete mapping of \(G\)" as CNF (a permutation matrix for \(\theta\) plus a permutation matrix for \(\eta=x\theta(x)\), linked by the group multiplication table) and run an **exact model counter** (e.g. a certified #SAT tool) for the total; cross-check against the backtracking count. Use DRAT for any decision sub-claim.
5. **Clique search (P4).** Build the orthomorphism graph and run an exact **maximum-clique** solver (with a certified optimality proof); recompute every edge (pairwise orthogonality) independently.
6. **Cycle-type refinement (P3).** During enumeration tag each complete mapping by the cycle type of \(\theta\) and of \(\eta\), so a single exhaustive pass yields the full cycle-type distribution and the strong-complete-mapping subcount as byproducts.

Target groups to attack, roughly increasing difficulty:

- **Cyclic \(\mathbb{Z}_v\), odd \(v\)** - the classical sequence; reproduce small \(v\), then push \(v\) upward to the first unpublished value.
- **Elementary-abelian \(\mathbb{Z}_p^k\)** - rich automorphism group (\(\mathrm{GL}(k,p)\)) gives large symmetry reduction.
- **Small non-abelian groups** satisfying Hall–Paige (dihedral \(D_n\), etc.) - where counts are sparsely tabulated.
- **Groups near the feasibility edge** - where only a symmetry-reduced count (P5) is attainable.
- **Quaternion and dicyclic groups** (Hall–Paige-admissible cases) - under-tabulated non-abelian targets.

**One-workstation scope and failure modes.**

- *Factorial explosion:* raw enumeration is \(v!\)-scale - only aggressive incremental pruning and symmetry reduction make \(v\) into the low-to-mid tens feasible; scope the target order honestly.
- *Symmetry-quotient bugs:* an incorrect holomorph/automorphism action over- or under-counts - cross-check reduced counts by Burnside and against any unreduced small case.
- *Existence scope creep:* never present existence as a result; Hall–Paige owns it, and the literature gate must say so before any search.
- *Unverified counts:* a single search run is not a certificate - recount by a second method (backtrack vs. model counter).
- *MOLS-design drift:* stay on the group-based count/clique; do not slide into classifying Latin squares as designs (mathematics-program territory).
- *Asymptotic-for-exact substitution:* the \((e^{-1/2}+o(1))|G^{\mathrm{ab}}|\,v!^2/v^v\) formula is a check on the *order of magnitude* only; it never stands in for the exact integer.
- *Group-presentation errors:* a wrong multiplication table silently counts the wrong group - validate the table against GAP's library group before enumerating.
- *Clique-vs-count conflation:* the number of orthomorphisms and the orthomorphism-graph clique number are different quantities; report each with its own certificate.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every complete-mapping/orthomorphism claim is an exact permutation check on both required maps; every count is an exhaustive enumeration or a certified model count in exact integer arithmetic; every clique optimality is a certified maximum-clique proof. No floating point and no statistical estimate stands in for an exact integer.
2. **Independent verification.** Every exact count is recomputed by a second method (backtracking vs. certified #SAT); every checker is dual-implemented (GAP vs. C++/SageMath); every symmetry-reduced count is cross-checked by Burnside and against an unreduced sub-case; every MOLS edge is recomputed. A reproduced count must match the published integer to the last digit before any adjacent new count is trusted.
3. **Reproducibility.** Record the group presentation / multiplication table (validated against GAP's group library), the equivalence/symmetry action used, all encodings, and tool versions (GAP, nauty, SageMath, #SAT/clique solvers), with a SHA-256 manifest over every permutation list, CNF, count certificate, and clique. Cite the published baseline count or OEIS sequence being reproduced or extended (identifier, source, access date). State whether each count is raw or holomorph-reduced.
4. **Preservation.** All enumeration, checker, and clique-search source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson). The literature-gate note is archived as a dated artifact so the reproduction-vs-novelty judgment is auditable.
5. **Honest reporting.** The report states up front - after the literature gate - whether the result is a *reproduction* of a published count, a *new certified count/clique*, or a *refined-structure* count, and never presents existence (settled by Hall–Paige) as open or newly resolved. An uncertified or single-run count, or an asymptotic figure, is never represented as an exact enumeration.

Calibration for the session lead: the realistic product is the literature gate plus P1–P2 - reproduced small-group counts and one new certified exact count for a group whose value is unpublished - plus, with luck, a strong/cycle-type count (P3) or an orthomorphism-graph clique number (P4). This problem's single sharpest risk is misreporting the *existence* question, which Hall–Paige closed in 2009; the gate exists to make that impossible. The valuable, genuinely-open work is exact enumeration and clique structure, not existence.
