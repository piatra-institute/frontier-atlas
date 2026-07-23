# PROMPT FOR CERTIFIED-FEASIBLE, COST-OPTIMAL RETROSYNTHETIC ROUTES

## Retrosynthesis that produces guaranteed-valid, cost-optimal routes under a formal on-machine route-checker

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A02 of 21
**Source:** chem/bio top-50 list #28, section D (design)
**Modes:** `[algo]` `[gen]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Modern retrosynthesis planners (Monte-Carlo tree search over neural template scores) return routes that *look* plausible but carry no guarantee: a step may correspond to no real reaction template, atoms may not balance, a claimed building block may not be purchasable, and the "best" route by a learned score need not minimize any explicit cost. This prompt replaces "plausible route" with a formal object - a synthesis route is a proof-carrying artifact that a **formally-specified, deterministic route-checker** accepts. Every step is a valid application of a template in a fixed library with a consistent atom mapping; every leaf is in a frozen building-block stock; the route's cost is accounted under an explicit numeric cost model. That checker is the **on-machine verifier** that closes the loop. The strong targets go further: a route that is *cost-optimal* under the fixed cost model, with a machine-checkable optimality certificate (an admissible AND/OR search that has closed, or an exhaustive enumeration of the bounded route space). This is a search/optimization problem with a formal verifier, which is exactly what makes it a Pack A item rather than a demo. Anything short of the section-2 standard - a route that passes only the planner's own scoring, or an "optimal" route without a matching lower bound - is reported as a partial result, never as a solution.

## 1. Exact problem statement

**Molecules.** A molecule is a labelled molecular graph with stereochemistry, identified by its RDKit canonical SMILES (isomeric, fixed RDKit version). Equality of molecules is equality of canonical SMILES strings. All canonicalization uses one pinned RDKit version, recorded in the manifest.

**Building-block stock $\mathcal{S}$.**

- A finite, explicitly frozen set of purchasable molecules, each a canonical SMILES string.
- Each block $b\in\mathcal{S}$ carries a price $\mathrm{price}(b)\in\mathbb{Q}_{\ge 0}$ in fixed cost units.
- $\mathcal{S}$ is a committed file (a snapshot of a vendor catalogue - eMolecules / Enamine building blocks - or a defined subset), hashed before any planning begins.
- The target $M$ satisfies $M\notin\mathcal{S}$, so no route is trivial.

**Template library $\mathcal{T}$.**

- A finite set of reaction templates, each a SMARTS reaction transform with explicit atom maps.
- Extracted from a fixed reaction corpus (USPTO grants text-mined by Lowe; USPTO-50k / USPTO-full) by a fixed procedure (RDChiral).
- Each template $t$ has a *forward* reading (reactants $\to$ product) and a *retro* reading applied to a product to yield precursor sets.

**Route.** A synthesis route for $M$ is a finite bipartite AND/OR directed acyclic graph:

- molecule (OR) nodes and reaction (AND) nodes;
- the root is $M$;
- each non-leaf molecule node is expanded by exactly one reaction node;
- a reaction node applies one template $t\in\mathcal{T}$ and has as children the precursor molecules produced by the retro application;
- every leaf molecule node is a member of $\mathcal{S}$.

**Route-validity predicate $V$ (the checker).** $V(R)=\texttt{true}$ iff all four hold, each independently re-computed by the checker (never trusting the planner):

1. **Template validity.** Every reaction node's stored template $t\in\mathcal{T}$, and running $t$'s *forward* transform on the node's precursors reproduces exactly the node's product (canonical-SMILES equality) - i.e. the retro step is invertible as claimed.
2. **Atom mapping / balance.** The reaction is atom-balanced under $t$'s atom map: every heavy atom of the product maps to a unique reactant atom, leaving groups and reagents are exactly those the template declares, and no atom is unaccounted.
3. **Stock membership.** Every leaf molecule's canonical SMILES lies in $\mathcal{S}$.
4. **Acyclicity / finiteness.** The graph is a finite DAG with no molecule reachable from itself.

**Cost model $C$ (fixed, numeric).** For a valid route $R$,

\[
C(R)\;=\;\alpha\cdot\big(\text{number of reaction nodes in }R\big)\;+\;\sum_{\text{leaf }b\in R}\mathrm{price}(b),
\]

with a fixed step penalty $\alpha\in\mathbb{Q}_{>0}$ (a per-step reagent+labour proxy). Convergent routes are rewarded implicitly, since shared subtrees are counted once. This model is deliberately simple and *committed before planning*. Alternatives (template-specific step costs, yield-discounted cost) are allowed only if written down and hashed as $C$ up front.

**Targets.** Given $(M,\mathcal{T},\mathcal{S},C)$:

- **Feasibility.** Produce a route $R$ with $V(R)=\texttt{true}$.
- **Optimality.** Produce $R^\star$ with $V(R^\star)=\texttt{true}$ and

  \[
  C(R^\star)\;=\;\min\{\,C(R)\;:\;V(R)=\texttt{true}\,\},
  \]

  together with an optimality certificate: a lower bound $L$ with $L=C(R^\star)$, established by an admissible AND/OR shortest-route search that has closed, or by an exhaustive enumeration of the bounded route space.

**Accuracy threshold.** Exact and Boolean: the checker $V$ accepts with zero violations, and for optimality targets $C(R^\star)$ equals the certified minimum exactly (rational arithmetic on $C$). There is no "approximately valid" route.

## 2. Resolution standard

Full resolution is a system that, for a *committed target set* $\{M_j\}$ under a *committed* $(\mathcal{T},\mathcal{S},C)$, returns for each $M_j$ a route $R^\star_j$ with $V(R^\star_j)=\texttt{true}$ and a machine-checkable certificate that $C(R^\star_j)$ is the exact minimum over all valid routes in the defined space. The certificate is re-checkable by a standalone verifier written separately from the planner. At the strongest target, the route-validity predicate $V$ and the optimality argument are formalized in Lean 4, so acceptance is a proof rather than a script's say-so.

**Not accepted as resolution:**

- A route accepted only by the planner's own model score, a learned feasibility classifier, or an "SCScore"-style heuristic - anything other than the standalone $V$.
- A route whose steps are chemically suggestive but fail template invertibility or atom balance (the two most common silent failures of neural planners).
- An "optimal" route with no lower-bound certificate, or optimality asserted from a search with an inadmissible/learned heuristic that can prune the true optimum.
- Optimality within an *implicitly* truncated space (an undisclosed depth cap, silently dropped templates) presented as optimality over the defined space.
- Success on the specific literature targets whose own published routes seeded $\mathcal{T}$ (leakage): a route reconstructed because its exact template chain was memorized.
- Single-target success generalized to a claim about arbitrary targets.

**Benchmark-integrity clause.** The verifier $V$ is exact *with respect to the model space* $(\mathcal{T},\mathcal{S},C)$ - and that space is not the wet lab. Template validity is not experimental feasibility: templates ignore chemoselectivity, competing reactive sites, protecting-group strategy, stoichiometry, conditions, and yield; a route can be $V$-optimal and still fail at the bench. State this bias explicitly. Two guards are mandatory. (i) **Leakage control:** freeze a held-out target set whose literature routes were excluded from template extraction, and report performance there separately. (ii) **Round-trip / prospective feasibility check:** every proposed step is additionally passed through an *independent* forward-reaction predictor (a Molecular-Transformer-style model) and must reproduce the recorded product from the proposed precursors; disagreement is reported, not hidden. A checker-win with a leaked or lab-blind verifier is confident-but-wrong and must be flagged as such.

## 3. Graded partial-result targets

- **P1 (verified toolchain reproduces a known route).** For a named literature target, take its published synthetic route, encode it as a route object, and have the standalone checker $V$ confirm every step: template validity, atom balance, leaves in $\mathcal{S}$. *Certificate:* the machine-readable route + the checker transcript + the RDChiral template applications, reproducible from a manifest.
- **P2 (planner route, independently re-verified).** Run AiZynthFinder and ASKCOS on a small committed target set; take each returned route and re-verify with $V$ written *separately* from the planner. Report the fraction that pass unmodified and the specific failure mode of those that do not. *Certificate:* planner outputs + independent-checker logs + a failure taxonomy.
- **P3 (certified cost-optimal route, bounded space).** For a single target under committed $(\mathcal{T},\mathcal{S},C)$ and an explicit depth bound $d$, produce $R^\star$ and prove $C(R^\star)$ minimal via an admissible AND/OR search (Retro\*/AO\*-style, with a provably admissible cost lower bound) that has closed. *Certificate:* the optimum route + the closed search's lower-bound frontier, re-checkable independently.
- **P4 (provably-exhaustive enumeration).** For a target with a deliberately small $(\mathcal{T},\mathcal{S})$ and depth bound $d$, enumerate *all* valid routes and certify completeness: at every molecule node, every applicable template in $\mathcal{T}$ was tried and the recursion closed at stock or depth. *Certificate:* the full enumeration transcript + an independent replay reproducing the same route set as a canonical hash.
- **P5 (optimality certificates at target-set scale).** Extend P3 to a committed target library, reporting the certified optimum per target and the search resources. Where the admissible search cannot close, report the best route together with the standing lower bound (an explicit optimality gap), never a bare "best found". *Certificate:* a per-target optimum-or-gap table + independent re-check.
- **P6 (formally verified checker).** Formalize $V$ and the AND/OR optimality argument in Lean 4, so that "route valid" and "route optimal in the bounded space" are machine-checked proofs. *Certificate:* the Lean development + a bridge mapping a route object to the formal statement.

Full resolution (P5/P6 across a nontrivial target set with lab-relevant $\mathcal{T},\mathcal{S}$) is unlikely in one session; P1–P4 are realistic and independently valuable.

## 4. Known results and prior art

- Corey - LHASA, the first retrosynthesis program (from the late 1960s); Corey's disconnection logic underlies all template methods.
- Lowe 2012 - text-mined USPTO reaction dataset (Daniel Lowe, PhD thesis); the standard public template/reaction source (USPTO-50k, USPTO-full).
- Segler, Preuss, Waller 2018 (*Nature*) - 3N-MCTS: neural template scoring with Monte-Carlo tree search; the demonstration that learned retrosynthesis reaches expert-competitive routes in a double-blind test.
- Coley, Green, Jensen and co-workers - ASKCOS (MIT): template-relevance networks, SCScore (Coley et al. 2018), and RDChiral for template extraction/application (Coley et al. 2019); forward-prediction consistency checks.
- Genheden, Thakkar, Bjerrum et al. 2020 - AiZynthFinder (AstraZeneca), open-source MCTS planner (*J. Cheminformatics*).
- Binghong Chen, Li, Dai, Song 2020 - Retro\*: neural-guided A\* over AND/OR graphs (*ICML*); the closest prior work to certified optimal-cost search.
- Schwaller et al. 2019 - Molecular Transformer for forward reaction prediction (*ACS Cent. Sci.*); Schwaller et al. 2021 - RXNMapper, attention-based atom mapping.
- Genheden & Bjerrum 2022 - PaRoutes, a benchmark set of literature routes for evaluating multi-step planners (verify exact scope).
- Maziarz et al. 2023–2024 (Microsoft Research) - Syntheseus, a unified, reproducible search library for retrosynthesis benchmarking (verify).
- Thakkar, Kogej, Reymond, Engkvist, Bjerrum 2020 - data-quality and route-feasibility studies.

No published system returns routes with a formal feasibility guarantee *and* a cost-optimality certificate; "feasibility" today means a learned score, and "optimal" means best-found under search. That gap is the point of this prompt. **Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

**[algo] The checker first.** Implement $V$ as a standalone module: RDKit for canonical SMILES and molecule equality; RDChiral to apply each template's forward transform and confirm it reproduces the recorded product; an atom-balance routine over the template's atom map; a stock-membership lookup against the hashed $\mathcal{S}$; and a DAG/acyclicity check. This module is written and tested *before* any planner is trusted, and is the sole authority on validity. Where warranted, a second implementation of atom balance in a different library cross-checks it.

**[algo] Search with certificates.** For P3/P5, build the retrosynthesis space as an AND/OR graph and run AO\*/Retro\*-style search with a *provably admissible* cost lower bound under $C$ - for example, $\alpha\cdot(\text{remaining-depth lower bound}) + (\text{cheapest-stock bound})$. Optimality holds only if the heuristic is admissible, so the admissibility proof is part of the deliverable. For P4, depth-bounded exhaustive enumeration with memoized subproblems and a canonical route-set hash for independent replay.

**[gen] Planners as proposers.** ASKCOS and AiZynthFinder generate candidate routes and single-step expansions; a generative single-step model (template-based or template-free) proposes precursors. These are *untrusted proposers*: nothing they emit is accepted until $V$ - and, for the integrity guard, an independent forward predictor - re-checks it. USPTO templates via RDChiral; stock from a frozen catalogue file.

**[algo] Formalization.** For P6, encode molecules-as-graphs, template application, and the AND/OR optimality argument in Lean 4; keep the formal statement close to the executable checker via a small trusted bridge.

**One-workstation scope.**

- AiZynthFinder/ASKCOS single-target planning runs on one CPU workstation (a single GPU accelerates the neural scorers) in seconds to minutes; the checker is CPU-cheap.
- Exhaustive/admissible search over a bounded $(\mathcal{T},\mathcal{S},d)$ is the cost driver and must be kept in scope by bounding the depth $d$ and the template count $|\mathcal{T}|$.
- The Lean formalization (P6) is developer time, not compute; it fits on the same workstation.

**Failure modes.**

- Template-application explosion - combinatorial precursor sets from permissive SMARTS; contained by bounding branching and depth.
- Atom-mapping ambiguity and stereochemistry loss; mitigated with RXNMapper cross-checks and strict isomeric-SMILES equality.
- Canonicalization mismatches causing false stock misses; guarded by pinning the RDKit version and canonicalizing $\mathcal{S}$ by the identical routine.
- Search non-termination; guarded by a hard depth bound and memoization.
- Heuristic inadmissibility silently breaking the optimality proof; guarded by an independent recomputation of the lower bound.

## 6. Verification and auditability requirements

1. **Exact/Boolean acceptance.** Validity is the standalone $V$'s Boolean verdict with zero tolerated violations; cost comparisons are exact rational arithmetic on $C$; optimality requires a lower bound *equal* to the achieved cost, never a floating-point near-tie.
2. **Independent verification.** The checker is implemented separately from every planner and, where warranted, twice (a second atom-balance/template-application implementation); the forward-prediction round-trip is a third, independent feasibility signal.
3. **Reproducibility.** $\mathcal{T}$, $\mathcal{S}$, $C$ (including $\alpha$), RDKit/RDChiral versions, the template-extraction corpus and procedure, seeds, and depth bounds are recorded; a SHA-256 manifest covers every template file, the stock file, every route object, and every certificate; the leakage-controlled held-out target set is committed before evaluation.
4. **Preservation.** Planner configurations, search transcripts, the checker, the Lean development (if any), and *failed or rejected* routes are part of the record; anything discarded is listed as discarded.
5. **Honest reporting.** The report states up front whether feasibility-only or certified-optimality was achieved and over which committed space; reports held-out (leakage-controlled) performance and the forward-prediction round-trip agreement, not only the tuned in-space numbers; and never presents a planner-scored route, a lab-blind checker win, or a best-found route as a solved-and-optimal synthesis.
