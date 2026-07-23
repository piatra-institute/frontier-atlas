# PROMPT FOR THE GROTHENDIECK CONSTANTS AND THE MAXIMAL I3322 QUANTUM VIOLATION

## Exact values and certified bounds for $K_G$, $K_G(3)$, and the $I_{3322}$ Tsirelson problem

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 18 of 50 (Tier 2)
**Source:** top-50 list #7, category A (quantum information and foundations)
**Modes:** `[bound]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The real Grothendieck constant $K_G$ - the universal ratio between vector-valued and $\pm 1$-valued bilinear optimization - satisfies roughly $1.676 < K_G < 1.7822$, with Krivine's classical upper bound proved non-optimal by Braverman–Makarychev–Makarychev–Naor, and its exact value has been open since 1953. Its order-3 restriction $K_G(3)$ *is* a physical constant: its reciprocal is the exact local-hidden-variable visibility threshold of two-qubit Werner states under projective measurements, so every improvement to its bounds is a theorem about quantum nonlocality. Alongside sits the stubbornly open maximal quantum violation of the $I_{3322}$ Bell inequality, conjectured from structured numerics to be $0.2509\ldots$ and believed attained only in infinite dimension. All three questions reduce to certifiable objects: Bell functionals with exactly computable classical bounds, local-model constructions with rigorously rounded geometry, and SDP/NPA relaxations admitting exact rational dual certificates. Full determination of $K_G$ is unlikely by these means, and we say so plainly; the graded certified-bounds program is the goal. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

For a real matrix $A = (a_{ij}) \in \mathbb{R}^{m \times n}$ define

\[
\mathrm{LOC}(A) \;=\; \max_{s_i,\, t_j \in \{-1, +1\}} \sum_{i,j} a_{ij}\, s_i t_j ,
\]

\[
\mathrm{SDP}_k(A) \;=\; \max_{u_i,\, v_j \in S^{k-1}} \sum_{i,j} a_{ij}\, \langle u_i, v_j \rangle ,
\]

with $S^{k-1} \subset \mathbb{R}^k$ the unit sphere, and $\mathrm{SDP}(A) = \sup_k \mathrm{SDP}_k(A)$. The **Grothendieck constants** are

\[
K_G(k) \;=\; \sup_{m, n,\ A \ne 0} \frac{\mathrm{SDP}_k(A)}{\mathrm{LOC}(A)}, \qquad K_G \;=\; \sup_{k} K_G(k),
\]

finite by Grothendieck's inequality (1953). We work exclusively with the *real* constants; the complex constants are a different problem, and every claim must say "real".

**Problems, in scope order:**

1. **$K_G(3)$:** determine, or improve the certified bounds on, $K_G(3)$. Physical dictionary (Acín–Gisin–Toner, ~2006), to be stated and used explicitly: the two-qubit Werner state $\rho_v = v\,|\phi^-\rangle\langle\phi^-| + (1-v)\,\mathbb{1}/4$ admits a local hidden variable model for all projective measurements iff $v \le v_c = 1/K_G(3)$. Every result is to be reported in both languages ($K_G(3)$ and $v_c$).
2. **$K_G$:** improve the certified interval $1.676\ldots \le K_G \le 1.7822\ldots$ at either end, knowing Krivine's bound $\pi/(2\ln(1+\sqrt2))$ is not tight.
3. **$Q_{3322}$:** determine the supremum of the quantum value of the $I_{3322}$ inequality in the Collins–Gisin normalization (local bound 0; the exact rational coefficient table is fixed once in the artifact repository and referenced everywhere), over all finite and infinite dimensions; conjectured $\approx 0.250875\ldots$ (Pál–Vértesi), believed attained only in the limit of infinite dimension.

Certification vocabulary, fixed here:

- a **certified lower bound on $K_G(k)$** is an explicit rational matrix $A$ with exact $\mathrm{LOC}(A)$ and a certified (exact or interval) lower bound on $\mathrm{SDP}_k(A)$;
- a **certified upper bound on $K_G(3)$** is a proof valid for *all* $A$ - operationally, a local-model construction certifying a visibility $v$, which gives $K_G(3) \le 1/v$;
- a **certified upper bound on $Q_{3322}$** is an NPA-type dual with exact rational certificate; a **certified lower bound** is an explicit quantum strategy with certified value.

## 2. Complete-resolution standard

Any one of the following, fully certified per section 6, resolves the corresponding subproblem; the prompt as a whole is resolved only if all three are:

1. **$K_G(3)$ exactly:** a closed-form or exactly characterized value, with a matching certified lower-bound witness sequence and a matching upper-bound proof (local-model or dual construction), the two provably converging to the same value.
2. **$K_G$ exactly:** likewise. (Calibration: no known technique approaches this; treat as aspirational context for the bounds program.)
3. **$Q_{3322}$ exactly:** a proof of the exact supremum, including whether it is attained in finite dimension, with certified matching upper bound (exact-arithmetic NPA dual or analytic argument) and lower bound (explicit strategy sequence with certified values and certified convergence).

**Not accepted as resolution:**

- Floating-point NPA or see-saw values, however converged, for any of the three quantities.
- Re-derivations of Krivine-type upper bounds, or numerics about the Krivine-scheme optimum, presented as progress on the true $K_G$.
- Heuristic local models (sampled spheres, unverified roundings) presented as upper bounds on $K_G(3)$; Monte Carlo estimates of $\mathrm{LOC}(A)$ (classical bounds must be exact - complete enumeration or exact branch-and-bound).
- Bounds on complex constants, on $K_G(k)$ for $k \ne 3$, or on other Bell scenarios presented as bounds on the named targets (log them as by-products if certified).
- The Pál–Vértesi number restated to more digits without a certificate; dimension-restricted $I_{3322}$ optima presented as $Q_{3322}$.
- Any claim whose exact rational certificate fails independent re-verification.

## 3. Graded partial-result targets

**P1 - Certified re-derivation of the classical anchors.**
*Task:* (a) Krivine's bound $K_G \le \pi/(2\ln(1+\sqrt2))$ as a verified symbolic derivation (SymPy/SageMath notebook, human-checked). (b) A certified lower bound $K_G \ge 1.67$-scale: implement a Davie/Reeds-type witness with exact rational data, exact $\mathrm{LOC}$, and interval-certified SDP value with rational dual gap. (c) Audit the published record bounds for $K_G(3)$ - lower bounds of Diviánszky–Bene–Vértesi type, upper bounds of the Hirsch–Quintino–Vértesi–Navascués line, and the recent Frank–Wolfe-era improvements - determining for each *how much is actually certified* (verify current records first).
*Certificate:* exact witness dossiers plus the audit table.
*Effort:* days to two weeks.

**P2 - Exact-arithmetic Bell-bound engine.**
*Task:* a reusable tool that, given rational $A$: computes $\mathrm{LOC}(A)$ *exactly* (C++ branch-and-bound over $\{\pm1\}^m$ with the inner maximization resolved exactly via $\mathrm{LOC}(A) = \max_s \sum_j |\sum_i a_{ij} s_i|$; complete-enumeration cross-check at small sizes; GMP rationals) and produces certified enclosures of $\mathrm{SDP}_3(A)$ and $\mathrm{SDP}(A)$ (high-precision SDP plus rational dual rounding).
*Certificate:* validation against published values; dual implementations compared.
*Value:* everything downstream uses this engine; it serves the institute's whole Bell-inequality program.

**P3 - Improved certified lower bound on $K_G(3)$.**
*Task:* search for matrices beating the current record ratio $\mathrm{SDP}_3(A)/\mathrm{LOC}(A)$ - Gilbert/Frank–Wolfe heuristics, column generation, symmetric ansätze from sphere point-sets - then certify winners with P2.
*Certificate:* exact witness dossier per section 1's vocabulary.
*Value:* every certified improvement narrows the proven Werner-state threshold window; realistic single-session headline.
*Effort:* search is cheap; the exact $\mathrm{LOC}$ of large witnesses is the budget item.

**P4 - Improved certified upper bound on $K_G(3)$.**
*Task:* implement the covering-based local-model construction methodology (Hirsch–Quintino line) entirely in certified arithmetic: finite measurement covers with certified radii, exact polytope-membership via rational LP, and a final certified visibility. Aim to push the certified visibility over the published record; even *matching* the record with a fully certified proof is valuable if the published constructions lean on unverified numerics (verify which do).
*Certificate:* cover data, rational LP certificates, and the visibility inequality chain.
*Effort:* weeks; geometrically fiddly, and the certification gap versus published numerics is the real question.

**P5 - $I_{3322}$ certified two-sided sandwich.**
*Task:* upper - NPA at the highest level solvable with high-precision SDP, rounded to an exact rational dual certificate. Lower - reproduce the Pál–Vértesi infinite-dimensional ansatz through certified finite truncations with a proved truncation-error lemma, yielding certified lower bounds converging toward $0.250875\ldots$.
*Certificate:* rational NPA dual; interval-certified strategy values; the truncation lemma.
*Value:* plausibly the first fully certified two-sided enclosure of $Q_{3322}$ at width $10^{-5}$ or better (verify no one has done this).

**P6 - Improved certified bounds on $K_G$ itself.**
*Task:* either end: a new certified lower bound above the verified Davie/Reeds-type value via large structured witnesses (P2 at scale); or an *effective, certified* version of the BMMN improvement - extracting an explicit $\varepsilon > 0$ with $K_G \le \pi/(2\ln(1+\sqrt2)) - \varepsilon$ (their argument is effective in principle; a certified explicit constant would be new - verify).
*Value:* strongest realistic outcome short of resolution.

**P7 - Full resolution** of any subproblem per section 2.

Honest calibration: exact $K_G$ and exact $Q_{3322}$ are long-shots; exact $K_G(3)$ is conceivable only if the true optimum has recognizable algebraic structure. P2–P5 are the expected products.

## 4. Known results and prior art

- Grothendieck's inequality: Grothendieck (1953, Résumé); modern SDP formulation standard since the 1970s–1990s.
- Upper bounds: Krivine (~1977–1979), $K_G \le \pi/(2\ln(1+\sqrt2)) \approx 1.7822$; strict non-optimality of Krivine's bound: Braverman–Makarychev–Makarychev–Naor (~2011, journal version ~2013), improvement explicit-in-principle but not numerically optimized (verify).
- Lower bounds: Davie (~1984) and Reeds (~1991), $K_G \gtrsim 1.676$–$1.677$; largely in unpublished notes - re-derive rather than cite blindly (verify best published account).
- Computability: Raghavendra–Steurer (~2009), $K_G$ is computable to any precision in principle; the algorithm is impractical.
- $K_G(3)$ and Werner states: Acín–Gisin–Toner (~2006). Lower bounds via large Bell functionals: Vértesi (~2008); Diviánszky–Bene–Vértesi (~2017), $K_G(3) \ge 1.4367$-scale. Upper bounds via local-model constructions: Hirsch–Quintino–Vértesi–Navascués–Brunner (~2016–2017), $K_G(3) \le 1.4644$-scale. Frank–Wolfe-based narrowing toward a $[1.45, 1.46]$-scale window: Designolle–Iommazzo–Besançon–Knebel–Gelß–Pokutta (~2023) and successors (verify the current record interval and how much of it is certified versus numerical).
- $I_{3322}$: Froissart (~1981); Collins–Gisin (~2004) normalization and study; Pál–Vértesi (~2010), infinite-dimensional numerics giving $0.250875\ldots$ with dimension-scaling evidence; NPA hierarchy (Navascués–Pironio–Acín, ~2007–2008) upper bounds consistent to many digits; finite-dimensional attainability believed to fail (open). Post-MIP*=RE Tsirelson-problem context is background, not a tool here.
- Exact-certification methodology: rational rounding of SDP duals as practiced in verified flag-algebra and sphere-packing computations (~2010s, standard).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

**Exact $\mathrm{LOC}$ engine (P2).**

- C++ branch-and-bound over $s \in \{\pm1\}^m$; inner maximization exact; GMP rational arithmetic throughout; symmetry pruning; complete enumeration cross-check for small $m$.
- Failure mode: witness matrices beyond exact-$\mathrm{LOC}$ reach - cap witness sizes accordingly and say so; a lower bound is only as strong as its exact classical value.

**SDP with exact duals (P2, P5).**

- SDPA-GMP-class high-precision solves; rational rounding with a strict-feasibility margin; exact PSD verification by $LDL^T$ over $\mathbb{Q}$ (SageMath/FLINT).
- NPA: generate moment matrices symbolically (SymPy/SageMath); exploit the symmetry group of $I_{3322}$ to block-diagonalize; expect memory to be the binding constraint at high levels - record the wall.

**Witness search (P3, P6).**

- Frank–Wolfe/Gilbert alternation on the ratio objective; seeds from sphere designs and known record matrices; anneal witness size against certifiability.
- All discovery in floating point; survivors re-instantiated over $\mathbb{Q}$ (rounding the matrix itself is allowed - only the certified ratio matters) and fed to P2.

**Local-model constructions (P4).**

- Interval arithmetic (Arb/MPFI) for cover radii and shrinking factors; exact rational LP for polytope membership; assemble the certified visibility chain.
- Failure mode: cover fineness explodes near the record - profile certified visibility versus cover size and report the certified plateau honestly.

**$I_{3322}$ lower bounds (P5).**

- Reimplement the Pál–Vértesi ansatz; interval linear algebra for finite-dimensional strategy values; prove the truncation-error lemma before extrapolating anything; report only certified finite values plus proved limits.

**Workstation budget.**

- P1–P4: single workstation.
- P5 NPA upper bound: the memory-heavy item; high levels may exceed a workstation - document the achievable level.
- Distributed restarts help the P3 search but are optional.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** $\mathrm{LOC}$ values exact-rational always; SDP-side claims only via exact rational dual certificates or directed-rounding intervals; every reported constant carries its certificate type inline (exact / rational-dual / interval).
2. **Independent verification.** Standalone checkers, independent of search and modeling code, in both Python and C++, for: rational PSD certificates; $\mathrm{LOC}$ values (independent implementation or full enumeration at reduced size); local-model polytope-membership certificates. Every published-record re-verification is logged pass/fail with artifacts.
3. **Reproducibility.** Seeds, solver versions, precision schedules, cover parameters, NPA level and monomial bases recorded; SHA-256 manifest over witnesses, duals, covers, models, and code; single-command replay per claim.
4. **Preservation.** The Bell-bound engine, all record and near-record witnesses, failed roundings, and the certified-versus-published comparison table are part of the record; unpreserved exploration is declared.
5. **Honest reporting.** The report opens with whether any subproblem met section 2 (expected: none); presents the certified intervals for $K_G$, $K_G(3)$, $v_c$, and $Q_{3322}$ side by side with the best published (possibly uncertified) values, clearly distinguishing the two; and never lets a numerical value appear without its certification status.
