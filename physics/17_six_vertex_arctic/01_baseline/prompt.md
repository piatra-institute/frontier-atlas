# PROMPT FOR SIX-VERTEX ARCTIC CURVES AT GENERAL Δ AND A DIRECT ASM–DPP BIJECTION

## Domain-wall six-vertex model: rigorous Colomo–Pronko arctic curves, and an explicit structure-revealing bijection between alternating sign matrices and descending plane partitions

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 17 of 50 (Tier 2)
**Source:** top-50 list #29, category C (exactly solvable models and lattice statistics)
**Modes:** `[proof]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Two crisp open targets sit at the junction of the six-vertex model and enumerative combinatorics. (a) For the six-vertex model with domain-wall boundary conditions, Colomo and Pronko derived (2008–2010, nonrigorously) explicit arctic curves separating frozen from temperate regions at general anisotropy $\Delta$; rigorous proofs exist at the free-fermion point $\Delta=0$ and, via Aggarwal's work at the ice point, in select cases (verify exact scope) - general $\Delta$ is open. (b) The equality $|\mathrm{ASM}_n|=|\mathrm{DPP}_n|$ is a theorem (Andrews 1979 counted DPPs; Zeilberger 1996 and Kuperberg 1996 counted ASMs), yet after forty years no direct, statistic-preserving, structure-revealing bijection is known; the Fischer–Konvalinka bijective proofs work through signed sets and compositions of recursions (verify current status).

Both targets decompose into machine-certifiable pieces: exact partition-function and refined-enumeration data via the Izergin–Korepin determinant in rational arithmetic; tangent-method steps with explicitly audited rigor; and bijection existence/nonexistence within constrained families as finite search problems with certificates.

The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Model and conventions

- On the $n\times n$ grid, orient every edge so that each vertex has two arrows in and two out (ice rule).
- Domain-wall boundary conditions (DWBC): all arrows on the left and right boundaries point inward, all on top and bottom point outward.
- The six vertex types carry weights $a,a,b,b,c,c$ (standard pairing as in Korepin 1982). The type table, fixed here:
  - types 1,2 (weight $a$): horizontal arrows continue through, vertical arrows continue through (both-right/both-up and both-left/both-down);
  - types 3,4 (weight $b$): horizontal continues, vertical continues, with opposite relative orientation to the $a$ types;
  - types 5,6 (weight $c$): arrows turn - sources and sinks of horizontal flux.
  Any session must draw the six configurations explicitly and verify its table against $Z_2$ and $Z_3$ brute force before use.
- Define
\[
\Delta=\frac{a^2+b^2-c^2}{2ab},
\qquad
a=\sin(\lambda-\eta),\quad b=\sin(\lambda+\eta),\quad c=\sin2\eta,\quad\Delta=\cos2\eta,
\]
in the disordered regime $|\Delta|<1$.
- Partition function $Z_n=\sum_{\text{configs}}\prod_vw(v)$. The inhomogeneous $Z_n$ is the Izergin–Korepin determinant (Izergin 1987); adopt one explicit convention and verify it reproduces $Z_1,Z_2,Z_3$ by brute force before any other use.
- The height function $h$ and the four frozen corner regions are defined in the standard way.

### 1.2 Arctic curve, defined

For $(x,y)\in[0,1]^2$, the *arctic curve* is a curve $\Gamma_\Delta$ such that for every $\varepsilon>0$, as $n\to\infty$:
- at rescaled distance $\ge\varepsilon$ outside $\Gamma_\Delta$, the configuration is frozen with probability $\to1$;
- at rescaled distance $\ge\varepsilon$ inside, it is unfrozen with probability $\to1$.

Convergence in probability; this definition is part of the problem statement and must be used verbatim in any claimed theorem - existence of $\Gamma_\Delta$ is part of what must be proven, not assumed.

### 1.3 Target (a): arctic curves at general $\Delta$

Prove that for the DWBC six-vertex model at given $\Delta\in(-1,1)$ the arctic curve exists and equals the explicit Colomo–Pronko curve (their parametric formulas at general $\Delta$; at the ice point $a=b=c$, $\Delta=1/2$, the curve is the known inscribed ellipse - verify the formulas from Colomo–Pronko 2010 before use). Full target: all $\Delta\in(-1,1)$. A positive-measure interval of $\Delta$, or any new $\Delta$ value beyond the currently proven set, is graded under section 3.

### 1.4 Target (b): a direct ASM–DPP bijection

- An $n\times n$ *alternating sign matrix* (ASM) has entries in $\{0,\pm1\}$, each row and column summing to $1$, nonzero entries alternating in sign along each row and column.
- A *descending plane partition* (DPP) of order $n$ is an array $(d_{i,j})$, $1\le i\le r$, $i\le j\le\mu_i$, of positive integers $\le n$, weakly decreasing along rows, strictly decreasing down columns, in which the first entry of each row strictly exceeds its own row length and is at most the length of the preceding row (Andrews's conditions - verify against a standard reference and freeze).
- Statistics dictionary (Mills–Robbins–Rumsey; proven in refined form by Behrend–Di Francesco–Zinn-Justin 2012–2013 - verify the exact statistic conventions):
  - number of $-1$'s in the ASM $\leftrightarrow$ number of *special parts* ($d_{i,j}\le j-i$) of the DPP;
  - position of the $1$ in the top row $\leftrightarrow$ number of parts equal to $n$;
  - plus the third statistic of the triply refined version.
- Common counts, to be re-derived: $|\mathrm{ASM}_n|=|\mathrm{DPP}_n|=1,2,7,42,429,7436,218348$ for $n=1,\dots,7$, with the product formula $\prod_{j=0}^{n-1}\frac{(3j+1)!}{(n+j)!}$.
- Target: an explicit bijection $\Phi:\mathrm{ASM}_n\to\mathrm{DPP}_n$ carrying these statistics. *Explicit/direct* means: $\Phi$ and $\Phi^{-1}$ are defined by local or structural rules computable in polynomial time from the individual object, without evaluating determinants, generating functions, or recursions ranging over the whole family.
- Monotone-triangle and order-ideal encodings of ASMs, and the standard lozenge/cyclically-symmetric encodings of DPPs, are all admissible working coordinates; the bijection itself must still satisfy the directness clause above in whichever coordinates are chosen.

## 2. Complete-resolution standard

- **(a):** a theorem, fully rigorous under the section-1.2 definition, establishing the Colomo–Pronko curves for all $\Delta\in(-1,1)$ with DWBC - existence of the limit shape included, not assumed.
- **(b):** the map $\Phi$, proofs of bijectivity and of the statistics correspondence for all $n$, plus a demonstration of structure revealed: an explicit dictionary of at least the three refined statistics.
- Either (a) or (b) alone is a complete resolution of its half of the prompt.

**Not accepted as resolution:**

- (a) Tangent-method derivations that assume unproven one-point boundary asymptotics or the condensation hypothesis - these reproduce Colomo–Pronko, they do not prove it; each unproven analytic step must be named.
- (a) Results only at $\Delta=0$ (known), or simulation evidence for the curves at any precision.
- (a) Limit-shape statements controlling only the mean height, without control of the frozen-boundary fluctuation.
- (b) Equinumerosity re-proofs of any kind; determinant identities; signed bijections with cancellation. (Fischer–Konvalinka is celebrated prior art, not the target - verify whether their program has since produced an unsigned direct map, which would close (b).)
- (b) A map verified computationally for small $n$ without an all-$n$ proof; or a "bijection" that invokes global recursions or constant-term identities in its definition.
- Either half: conflating ice-point ($\Delta=1/2$) results with general $\Delta$.

## 3. Graded partial-result targets

**P1 - certified data with our own toolchain.**
Exact rational computation of $Z_n$, refined and boundary-refined versions, via the Izergin–Korepin determinant and the Korepin recursion at exactly representable weight points (ice point via cyclotomics; rational $(a,b,c)$ points); direct enumeration cross-check for $n\le6$ against ASM counts $1,2,7,42,429,7436$. Exact emptiness-formation-probability (EFP) and boundary one-point tables for $n\le40$–$60$.
*Certificate:* exact values; dual implementations (FLINT/Pari-GP determinants vs. SageMath recursion); SHA-256 manifest.

**P2 - tangent-method audit at $\Delta=0$.**
Implement the tangent method fully at the free-fermion point, where every step can be made rigorous; produce a document classifying each step as proven/unproven at general $\Delta$, with the asymptotic steps carried out in certified (Arb) arithmetic. The exact location of the analytic gap is a genuine deliverable.
*Certificate:* the annotated derivation plus certified asymptotics.

**P3 - new rigorous boundary results.**
Extend the proven set: a rigorous one-point or boundary-segment asymptotic at a new $\Delta$ value - leveraging Aggarwal's ice-point techniques and the Bleher–Fokin / Bleher–Liechty Riemann–Hilbert asymptotics (verify the scope of both) - or a proof of existence of the limit shape at some $\Delta\ne0$ without identifying the curve. Each increment is publishable.
*Certificate:* complete proof text plus supporting certified computations.

**P4 - bijection search as finite certifiable problems.**
For $n\le5$ (and $6$ where feasible): compute the full triple-statistic refined classes on both sides exactly. Then, for declared families of candidate maps (local growth rules; statistic-monotone maps; matchings constrained by a chosen partial order), decide existence of a statistics-preserving bijection within the family by SAT/CP with proof logging - DRAT for nonexistence, the explicit map for existence. Nonexistence within a natural family is a theorem about that family and steers the search.
*Certificate:* encodings, solver logs, DRAT proofs checked by `drat-trim`, or the explicit verified map.

**P5 - subclass bijections, proof-grade.**
An explicit proven bijection on a nontrivial subfamily - e.g. ASMs with exactly one $-1$ versus DPPs with exactly one special part (check the literature for partial correspondences, e.g. Lalonde - verify), or the permutation-matrix / no-special-part case extended one level.
*Certificate:* proof plus exhaustive machine verification for $n\le8$.

**P6 - strongest short of resolution.**
Either the arctic curve at one new $\Delta$ in full (curve identified), or a direct statistic-preserving bijection for one refined statistic on all of $\mathrm{ASM}_n$ with the remaining statistics conjecturally aligned and machine-verified for $n\le7$.

Honest calibration: (a) at general $\Delta$ and (b) in full are decades-old targets; expect P1–P4 as the session's genuine products, P5 as a strong outcome.

## 4. Known results and prior art

- Korepin 1982 (DWBC, recursion); Izergin 1987 (determinant).
- Rigorous DWBC free energy in all regimes: Bleher–Fokin 2006 (disordered); Bleher–Liechty 2009–2011 (other regimes; verify the split).
- Arctic phenomena at free fermion: Jockusch–Propp–Shor 1998 (arctic circle, dominos); Cohn–Elkies–Propp 1996; variational/frozen-boundary theory for dimers: Cohn–Kenyon–Propp 2001; Kenyon–Okounkov ~2005–2007.
- Colomo–Pronko 2008–2010: arctic curves for DWBC six-vertex at general $\Delta$ via EFP/condensation (nonrigorous); Colomo–Pronko–Zinn-Justin 2010 (extensions).
- Tangent method: Colomo–Sportiello 2016; applications by Di Francesco–Guitter and coauthors 2018–2019 (nonrigorous in general; verify which instances have been rigorized).
- Aggarwal: rigorous arctic-boundary results for the ice model / ASM point (~2020, Inventiones-level - verify the precise theorem, the domains covered, and any post-2020 extensions toward general $\Delta$; verify also the rigorous limit-shape results for the *stochastic* six-vertex model and whether they transfer to DWBC).
- ASM counting: Mills–Robbins–Rumsey 1982–1983 (conjectures); Andrews 1979 (DPP count); Zeilberger 1996 (ASM proof); Kuperberg 1996 (Izergin–Korepin proof).
- Refined ASM–DPP equivalences: Behrend–Di Francesco–Zinn-Justin 2012 (doubly refined), 2013 (triply refined - verify).
- Bijective front: Fischer–Konvalinka ~2019–2022, bijective proof of the ASM theorem via signed sets (verify exact status and any newer unsigned results); Krattenthaler's plane-partition surveys; Striker's poset-theoretic unification ~2011 (verify).
- Six-vertex limit shapes at general $\Delta$: variational/PDE approaches (Palamarchuk–Reshetikhin ~2010; later integrability-of-limit-shape-PDE work by Reshetikhin and coauthors - verify) remain nonrigorous for DWBC arctic curves.

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

### 5.1 `[search]`/`[sym]` Data layer

- Pari/GP and FLINT exact determinant evaluation of Izergin–Korepin at rational/cyclotomic weight points; $n\le60$ workstation-feasible; entries blow up - use CRT plus rational reconstruction.
- Korepin recursion in SageMath as the independent implementation.
- Brute-force ASM/DPP enumerators in C++ with per-object statistics ($n\le7$: 218348 objects, trivial; $n=8$: 10850216, minutes).
- ore_algebra guessing on refined generating sequences as a conjecture generator; all guesses labeled as guesses.

### 5.2 `[search]` Bijection machinery

- Encode candidate-map families as constraint problems: variables = image assignments within refined classes; constraints = statistics preservation plus declared structural rules (locality in a monotone-triangle coordinate; row-by-row growth; equivariance under the known symmetries).
- Solvers: CaDiCaL/kissat with DRAT logging; exact matching via LEMON/OR-tools for pure-matching questions.
- Expected failure modes: a family too rich (search trivially succeeds with unstructured matchings - worthless; always quotient by symmetries and demand canonicity) or too poor (immediate UNSAT - informative only with the DRAT certificate retained).
- Iterate family definitions; preserve every definition tried, including dead ones.

### 5.3 `[proof]` Arctic layer

- At $\Delta=0$: full rigorous pipeline (P2) using determinantal/LGV structure with Arb-certified steepest-descent bounds.
- At $\Delta\ne0$: attack one-point boundary asymptotics via the Bleher–Liechty Riemann–Hilbert framework (verify applicability).
- Expected failure mode: loss of rigor exactly at the EFP condensation step - document it precisely; the delimitation feeds P2's audit.
- A single workstation suffices throughout; nothing needs clusters.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All partition functions, refined counts, and statistic tables in exact rationals/cyclotomics; asymptotic constants via Arb with directed rounding; floating point only in exploratory plots, so labeled.
2. **Independent verification.** Dual determinant/recursion implementations agreeing exactly; brute-force enumeration cross-checks at $n\le6$; DRAT proofs re-checked with `drat-trim`; any claimed bijection re-verified by an independently written verifier applying $\Phi$ and $\Phi^{-1}$ to every object for $n\le7$.
3. **Reproducibility.** Solver seeds, encodings, weight points, and precision settings recorded; SHA-256 manifest over all data, encodings, proofs, and scripts.
4. **Preservation.** Every candidate-map family (including failures), every UNSAT certificate, and the tangent-method audit document are part of the record; discarded searches must be listed as discarded.
5. **Honest reporting.** The final report states first whether (a) or (b) was completely resolved (expected: neither); tangent-method outputs are never called proofs; family-restricted nonexistence and small-$n$ verifications are never represented as the bijection or its impossibility.
