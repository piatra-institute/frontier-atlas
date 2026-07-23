# PROMPT FOR POSITIVE METRIC ENTROPY OF THE CHIRIKOV STANDARD MAP

## Sinai's question: Lyapunov exponents on positive Lebesgue measure for the standard family

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 50 of 50 (Tier 4)
**Source:** top-50 list #37, category E (dynamical systems and classical mechanics)
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Does the Chirikov standard map have positive Kolmogorov–Sinai entropy with respect to Lebesgue measure - equivalently, a positive-Lebesgue-measure set of points with nonzero Lyapunov exponent - for large, or indeed any, parameter $K$? Numerics scream yes ($h \approx \log(K/2)$ for large $K$); rigorously the question is fully open for every $K$, blocked by the coexistence obstruction: elliptic islands appear for a residual set of arbitrarily large parameters, and no known technique controls hyperbolicity on the complement of an unknown island union. This is a Tier 4 prompt: **no frontal assault**. The problem is background and opportunistic, on a decade scale; its value to the program is that it disciplines adjacent certified work - finite-time exponent statistics, horseshoe certificates, perturbed and randomized families where positivity is provable - and demands an exact map of the obstruction landscape. The complete resolution defined in section 2 is stated for reference only; the graded targets of section 3 are the entire realistic product, and none of them may ever be represented as resolving Sinai's question.

## 1. Exact problem statement

### 1.1 The map, the entropy, the exponents

On the torus $\mathbb{T}^2 = (\mathbb{R}/\mathbb{Z})^2$ define, for $K > 0$,

\[
f_K(x, y) \;=\; \Big( x + y + \tfrac{K}{2\pi} \sin(2\pi x), \;\; y + \tfrac{K}{2\pi} \sin(2\pi x) \Big) \pmod 1,
\]

an area-preserving real-analytic diffeomorphism (Lebesgue measure $\lambda$ invariant). The metric (Kolmogorov–Sinai) entropy with respect to $\lambda$ is

\[
h_\lambda(f_K) \;=\; \sup_{\mathcal{P}} \; \lim_{n \to \infty} \frac{1}{n}\, H_\lambda\!\Big( \bigvee_{i=0}^{n-1} f_K^{-i} \mathcal{P} \Big),
\]

the supremum over finite measurable partitions $\mathcal{P}$, with $H_\lambda$ the Shannon entropy of a partition. For $z \in \mathbb{T}^2$ let

\[
\chi^+(z) \;=\; \limsup_{n \to \infty} \frac{1}{n} \log \| D f_K^n(z) \|
\]

be the top Lyapunov exponent. By Pesin theory for $C^{1+\varepsilon}$ area-preserving surface diffeomorphisms (Pesin 1977; entropy formula),

\[
h_\lambda(f_K) \;=\; \int_{\mathbb{T}^2} \chi^+ \, d\lambda,
\qquad \text{so} \qquad
h_\lambda(f_K) > 0 \iff \lambda\{ z : \chi^+(z) > 0 \} > 0 .
\]

**Sinai's question (adopted formulation).** *Does there exist $K > 0$ - equivalently, is it true for all sufficiently large $K$ - with $h_\lambda(f_K) > 0$?*

Open for every single value of $K \ne 0$. No informal surrogate ("chaotic sea", "numerically hyperbolic region") is an acceptable target.

### 1.2 Calibration: what is known around the statement

- Positive *topological* entropy is essentially settled and is a different matter: the separatrices of the hyperbolic fixed point split transversally - exponentially small splitting, Lazutkin (1984) asymptotics, made rigorous by Gelfreich (~1999) for small $K$ - producing horseshoes and $h_{\mathrm{top}} > 0$; horseshoes at moderate $K$ are verifiable by interval methods. Horseshoes have Lebesgue measure zero, so this says nothing about $h_\lambda$.
- The obstruction: Duarte (1994) proved that for a residual set of arbitrarily large $K$ the standard map has infinitely many elliptic islands, dense in increasingly large regions. Uniform hyperbolicity fails persistently; any positive-entropy proof must coexist with KAM islands.
- Gorodetski (2012): the "stochastic sea" contains hyperbolic sets of full Hausdorff dimension accumulating on elliptic points - dimension, not positive measure.
- Berger–Turaev (~2019): Herman's positive-entropy conjecture - arbitrarily small $C^\infty$ conservative perturbations of the identity with positive metric entropy, in suitable families. A breakthrough in the area that does **not** apply to the standard family.
- Blumenthal–Xue–Young (~2017–18): positive Lyapunov exponents for the standard map *with i.i.d. random perturbations* at explicit noise scales. The randomized problem is solved; the deterministic one is not.
- (Verify all exact statements above before any dependence is built on them.)

## 2. Complete-resolution standard

Stated for reference; not a session target.

1. **Affirmative.** A proof, for an explicit $K$ (or an explicit set of $K$), that $h_\lambda(f_K) > 0$: exhibiting a measurable invariant set of positive Lebesgue measure with almost-everywhere nonzero Lyapunov exponent, or any equivalent route to the entropy statement of 1.1.
2. **Negative.** A proof that $h_\lambda(f_K) = 0$ for all $K$ - included only for logical completeness; it would overturn the universal expectation.

**Not accepted as resolution**

- Numerical Lyapunov exponents or numerical entropy, at any precision, over any orbit ensemble.
- Positive topological entropy, horseshoes, or transverse homoclinics (known; measure zero).
- Positive-exponent results for randomized, noisy, piecewise-linear, discontinuous, or generic-family variants represented as the standard map - including Blumenthal–Xue–Young (random noise) and Berger–Turaev (other families).
- Hausdorff-dimension or residual-genericity statements about chaotic sets (Gorodetski-type) represented as positive measure.
- "For almost every $K$" claims without an explicit $K$, unless the full-measure claim is itself proven.
- Finite-time exponent statistics, however certified, presented as asymptotic conclusions.
- Conditional results with unverified hypotheses presented as unconditional.

## 3. Graded partial-result targets

Tier 4 discipline: each target is adjacent, certifiable, and useful even though none resolves the question. Expected engagement: opportunistic, revisited across sessions over years - plan and report accordingly.

- **P1 - The obstruction dossier (theorem-level).**
  - *Task:* a precise, self-contained mathematical document reconstructing with full proofs: (i) Duarte's residual-islands theorem with explicit parameter and phase-space localization; (ii) why Pesin/cone-field/invariant-cone arguments fail on the island complement (the complement is not invariant-cone-friendly and the island union admits no computable upper bound); (iii) the exact logical gap between Blumenthal–Xue–Young's randomized result and the deterministic statement, and between Berger–Turaev's families and the standard family. Plus at least one new quantitative lemma - e.g., certified *lower* bounds on total island area at explicit $K$ via interval-verified Moser twist conditions on explicit islands. (Upper bounds over *all* islands are exactly what nobody can prove; state the asymmetry as a lemma, not a lament.)
  - *Certificate:* complete proofs; interval-verified island enclosures for the quantitative part.
  - *Value:* the field lacks a single rigorous map of why this problem is hard; producing one is genuine research output and the foundation for P4.
- **P2 - Certified finite-time exponent statistics.**
  - *Task:* interval-arithmetic propagation of the tangent cocycle over certified box covers of $\mathbb{T}^2$ at explicit $K$ (e.g., $K = 6, 10, 20$): rigorous enclosures of finite-time exponent distributions at horizons $n = 10^2$–$10^4$.
  - *Certificate:* box covers, cocycle enclosures, and a checker; the artifact text itself states the non-implication for $n \to \infty$.
  - *Value:* rigorous ground truth replacing folklore numerics, plus a reusable certified-cocycle library for the program.
- **P3 - Certified entropy positivity for cousin systems.**
  - *Task (a):* piecewise-linear standard-like maps (sawtooth, linked-twist regimes) where hyperbolicity on positive measure is finitely checkable - full certified proofs in exact rational arithmetic.
  - *Task (b):* a quantitative, explicit-constants version of the randomized result: positive exponents for the standard map with declared noise level $\varepsilon(K)$, every constant traced.
  - *Task (c):* covering-relation horseshoe certificates (CAPD-style) for the deterministic $f_K$ at explicit $K$, yielding certified lower bounds on $h_{\mathrm{top}}$ - labeled clearly as topological, not metric.
  - *Certificate:* per-item proofs and interval/rational certificates with independent checkers.
  - *Value:* maps the exact boundary of what current technology certifies, from three directions at once.
- **P4 - The conditional program.**
  - *Task:* formulate and prove theorems of the form: *if* an explicitly checkable finite-computation hypothesis $H(K, n, \delta)$ holds - e.g., cone-field invariance with margin $\delta$ outside a certified open set of measure $< m_0$, checked at resolution $n$ - *then* $h_\lambda(f_K) > 0$. Then determine precisely which component of $H$ is uncheckable today (invariance of the exceptional set is the expected sticking point), and honestly test the checkable fragments at small resolution.
  - *Certificate:* the implication proven in full; the fragment tests with interval certificates; a precise statement of the uncheckable residue.
  - *Value:* a sharp conditional theorem that localizes the entire difficulty into one verifiable-in-principle hypothesis is the most valuable purely mathematical product this prompt can realistically yield.
- **P5 - Transfer probes (strongest realistic).**
  - *Task:* attempt Berger–Turaev-style entropy mechanisms inside conservative families that limit on the standard family, or standard-map-adjacent analytic families with a provable positive-measure hyperbolic block; quantify the distance to $f_K$ explicitly in every statement.
  - *Certificate:* complete proofs; explicit distance quantification.
  - *Value:* any unconditional positive-metric-entropy theorem for a family containing $f_K$ in its closure would be a major publication. Decade-scale; log partial progress honestly and stop when the opportunistic budget is spent.

## 4. Known results and prior art

- Chirikov (1979, Phys. Rep.): the map, the numerics, the $h \approx \log(K/2)$ heuristic for large $K$. The entropy question is associated with Sinai and appears in Herman's ICM 1998 problem list (verify the attribution phrasing before quoting).
- Pesin (1977): entropy formula framework. Katok (1980): entropy and horseshoes for surface diffeomorphisms.
- Duarte (1994, Ann. IHP Analyse Non Linéaire): plenty of elliptic islands for the standard family - the obstruction theorem.
- Lazutkin (1984, asymptotics) and Gelfreich (~1999, rigorous): exponentially small separatrix splitting for small $K$; transverse homoclinics, hence horseshoes and positive topological entropy (verify the exact $K$-ranges covered by rigorous statements).
- Mather (1984): no rotational invariant circles for $|K| > 4/3$. MacKay–Percival (1985): $|K| \ge 63/64$. Global transport, but no measure-positive hyperbolicity.
- Gorodetski (2012, Comm. Math. Phys.): stochastic sea of full Hausdorff dimension accumulating on elliptic islands.
- Berger–Turaev (~2019): Herman's positive-entropy conjecture for arbitrarily small conservative perturbations of the identity (verify venue and the exact perturbation class; not the standard family).
- Blumenthal–Xue–Young (~2017–18): positive Lyapunov exponents for random perturbations of the standard map, with quantitative noise thresholds (verify exact noise scaling and publication data).
- Coexistence literature (Przytycki, Liverani, and others on elliptic islands in chaotic seas): verify each specific statement before citing any.
- No positive result on $h_\lambda(f_K) > 0$ for any deterministic $K$ exists (verify - any such paper would re-scope this prompt entirely).

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

Mode `[proof]`: the primary product is precise mathematics; computation is in support, never in front.

1. **P1 dossier.** Close reading and reconstruction of Duarte, Gorodetski, Berger–Turaev, and Blumenthal–Xue–Young; write the gap analysis as numbered lemmas with full proofs. Computational support: interval verification of specific elliptic islands - locate the periodic point, verify Moser twist-theorem hypotheses via interval normal-form coefficients (CAPD or the kv library; workstation-hours per island).
2. **P2 statistics.** Custom C++ with directed rounding (or CAPD `IMap`) for the tangent cocycle over adaptive box covers; report distributions with rigorous enclosure bars; horizon and resolution schedules fixed in advance to avoid garden-of-forking-paths reporting.
3. **P3 cousins.** (a) Sawtooth/piecewise-linear: hyperbolicity is linear algebra on polytopes - exact rational arithmetic proofs, no rounding at all. (b) Explicit-constants randomized theorem: pencil-and-paper with certified numerical constants. (c) Covering-relation horseshoes at $K = 6, 10$: standard CAPD technology, workstation-days, yielding certified statements of the form $h_{\mathrm{top}}(f_K) \ge \log 2 / p$ for explicit period $p$.
4. **P4 conditional theorems.** Draft $H(K, n, \delta)$ around interval-checkable cone invariance outside certified island enclosures; prove the implication with Pesin-block bookkeeping; then test $H$'s checkable fragments at small resolution to locate exactly where, and why, verification fails today.

**First computations (session day one).**

1. Locate and interval-verify one explicit elliptic island at a large $K$ (e.g., an accelerator-mode island near $K = 2\pi$): periodic point enclosure, multiplier on the unit circle, twist coefficient bounded away from zero.
2. A coarse certified P2 run at $K = 10$, horizon $n = 100$, on a $256^2$ box cover; checker pass on the output.
3. One CAPD covering-relation horseshoe at $K = 6$; extract the certified $h_{\mathrm{top}}$ lower bound.
4. Draft the P1 dossier skeleton: the numbered list of external statements to verify against primary sources, before any writing.

**Workstation feasibility.**

- Everything listed is single-workstation; nothing here is compute-bound. The binding constraint is proof labor, which is why this prompt is Tier 4 and opportunistic.

**Expected failure modes.**

- The perennial one: topological/metric conflation. Every artifact carries its category label; every draft is checked against the section 2 exclusion list before circulation.
- Island-area *upper* bounds are not obtainable by finite computation (the island count is unknown); any draft assuming one is unsound and must be withdrawn, not patched.
- Finite-time exponent enthusiasm: P2 outputs will look overwhelmingly hyperbolic and prove nothing asymptotic; the artifact text must lead with that sentence.
- Cousin-family results drifting into overclaim by informal "closeness" to the standard map; distances must be quantified or the comparison dropped.
- Misremembered literature (Berger–Turaev's exact class; Blumenthal–Xue–Young's noise scaling) silently corrupting the dossier; re-verify against the primary sources before any dependence is built.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All island enclosures, cone verifications, cocycle statistics, and horseshoe certificates in interval arithmetic with directed rounding, or exact rational arithmetic in the piecewise-linear cases; floating point only for exploration and figures, never inside a certificate. All P1/P4 mathematics as complete, human-checkable proofs.
2. **Independent verification.** Standalone checkers for every computational certificate: box-cover cocycle re-verification, covering-relation re-checks (independent of CAPD where CAPD produced them - dual C++/Python implementations), island normal-form condition re-evaluation. Proof documents are verified against the primary sources cited, with the verification of each external statement logged item by item.
3. **Reproducibility.** Box schedules, horizons, precisions, tool versions (CAPD, kv, compilers), and a SHA-256 manifest over all covers, certificates, and dossier sources.
4. **Preservation.** All code and all failed attempts - in particular failed conditional-hypothesis formulations in P4, which are the real research record on a Tier 4 problem. Anything not preserved is stated explicitly rather than obscured.
5. **Honest reporting.** Every report on this prompt opens with: "Sinai's question remains open; nothing below resolves it." Each result carries its exact category - topological vs metric; deterministic vs randomized; standard map vs cousin family; conditional vs unconditional - and the decade-scale, opportunistic framing is restated so that no session output can be mistaken for frontier resolution.
