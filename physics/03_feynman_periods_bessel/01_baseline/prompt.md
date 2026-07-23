# PROMPT FOR PROVING THE OPEN BESSEL-MOMENT AND φ⁴-COACTION CONJECTURES

## Feynman periods: Broadhurst-type Bessel-moment identities and the Panzer–Schnetz coaction

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 03 of 50 (Tier 1)
**Source:** top-50 list #45, category G (QFT and mathematical particle theory)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

On-shell values of sunrise ("banana") Feynman diagrams in two dimensions reduce to moments of products of Bessel functions $I_0$ and $K_0$. Broadhurst, with Mellit and Roberts, conjectured a dense web of exact structure on these moments: closed-form evaluations as critical $L$-values of modular forms, determinant formulae, $\mathbb{Q}$-linear sum rules, and integrality/congruence statements. A substantial part of this web has since been proved (Zhou; Fresán–Sabbah–Yu), and a residue remains open. Separately, Panzer and Schnetz conjectured that the motivic Galois coaction closes on the space of $\phi^4$ periods; this is verified computationally on every period computed to date but is unproven. Both problems are identity-proving over concrete integrals with massive machine-checkable ground truth - thousands of certified digits, PSLQ rediscovery, creative-telescoping certificates - which makes this the program's best `[sym]` problem in QFT. The complete resolution defined in section 2 is the target. Anything less must be reported as a partial result against the graded targets of section 3, never represented as a solution.

## 1. Exact problem statement

### 1.1 Bessel moments

Let $I_0$ and $K_0$ be the modified Bessel functions, the solutions of $t\,f''(t) + f'(t) - t\,f(t) = 0$ normalized by

\[
I_0(t) = \sum_{k\ge 0} \frac{(t/2)^{2k}}{(k!)^2},
\qquad
K_0(t) = \int_0^\infty e^{-t\cosh u}\,du \quad (t>0).
\]

For integers $a \ge 0$, $b \ge 1$, $k \ge 0$ define the Bessel moments

\[
\mathrm{IKM}(a,b;k) \;=\; \int_0^\infty I_0(t)^a\, K_0(t)^b\, t^k\, dt ,
\]

convergent whenever $b > a$, and also for $b = a$ with $k < a - 1$ (since $I_0(t)K_0(t) \sim 1/(2t)$). Elementary anchors, to be reproduced as toolchain tests:

- $\mathrm{IKM}(0,1;0) = \pi/2$ and $\mathrm{IKM}(0,1;1) = 1$;
- $\mathrm{IKM}(0,2;0) = \pi^2/4$ and $\mathrm{IKM}(0,2;1) = 1/2$;
- the classical evaluation $\mathrm{IKM}(0,3;0) = 3\,\Gamma(1/3)^6 /(32\pi\cdot 2^{2/3})$ (verify normalization against Bailey–Borwein–Broadhurst–Glasser 2008).

Physics link (context, not needed for the mathematics): with $n = a+b$ Bessel factors, $\mathrm{IKM}(a,b;1)$ and its odd-$k$ companions are periods of the $(n-1)$-loop equal-mass banana graph in $D=2$ dimensions, with $a$ counting cut/on-shell Wick-rotated propagators.

### 1.2 Problem A - the open Broadhurst-type conjectures

For $n = 2h+1$ odd, form the $h\times h$ matrices of odd moments

\[
\mathbf{M}_h^{(n)} \;=\; \Bigl(\, \mathrm{IKM}(a,\, n-a;\, 2b-1) \,\Bigr)_{1\le a,b\le h},
\]

and analogously for even $n$ (Broadhurst–Mellit 2016; Broadhurst–Roberts 2018 for the dual/rectangular variants). The conjectural corpus comprises, schematically:

1. **Determinant formulae:** $\det \mathbf{M}_h^{(n)}$ equals an explicit rational multiple of a specific power of $\pi$ times an explicit algebraic number (exact shapes as in Broadhurst–Mellit; verify exponents there).
2. **$L$-value evaluations:** individual moments at $n = 5, 6$ evaluate in terms of critical values of the $L$-functions of the level-6 eta-quotient newforms $f_{4,6}$ (weight 4) and $f_{6,6}$ (weight 6); for $n \ge 7$, in terms of $L$-functions attached to symmetric-power moments of Kloosterman sums.
3. **Sum rules:** explicit $\mathbb{Q}$-linear relations among $\{\mathrm{IKM}(a, n-a; k)\}$ at fixed $n$.
4. **Integrality and congruence conjectures** for the associated local data (Broadhurst's Kloosterman-moment congruences).

Much of items 1–3 is now proved (section 4). **Problem A** is: (Step 0, mandatory) produce a certified audit of exactly which conjectures in this corpus remain unproven at session date, item by item, with sources; then (Step 1) prove the remaining open items unconditionally.

### 1.3 Problem B - the Panzer–Schnetz coaction conjecture

A $\phi^4$ graph is a connected graph with vertex degree $\le 4$; a log-divergent graph $G$ with $h_G$ loops and $N_G = 2h_G$ edges is *primitive* if every proper subgraph $\gamma$ satisfies $N_\gamma > 2h_\gamma$. Its period is

\[
P(G) \;=\; \int_{x_e \ge 0} \frac{\delta(x_{N} - 1)\, \prod_{e} dx_e}{\Psi_G(x)^2} \;<\; \infty ,
\]

with $\Psi_G$ the Kirchhoff (first Symanzik) polynomial. Each $P(G)$ carries a canonical motivic lift $P^{\mathfrak m}(G)$, on which the motivic Galois group acts; write $\Delta$ for the resulting coaction on motivic periods (conventions of Panzer–Schnetz 2016 and Brown's motivic-period formalism). Let $\mathcal P_{\phi^4}$ denote the $\mathbb{Q}$-vector space spanned by the $P^{\mathfrak m}(G)$ over all primitive $\phi^4$ graphs, together with the powers of the Lefschetz period, in the precise form fixed by Panzer–Schnetz.

**Conjecture (coaction closure).** $\Delta\, \mathcal P_{\phi^4} \subseteq \mathcal A \otimes \mathcal P_{\phi^4}$: all Galois conjugates of $\phi^4$ periods are again (combinations of) $\phi^4$ periods. The formulation adopted here is exactly that of Panzer–Schnetz, "The Galois coaction on $\phi^4$ periods" (2016), including their treatment of weight drops and the adjoined constants. **Problem B** is to prove this conjecture at all loop orders. No informal surrogate ("the numbers look motivically stable") is an acceptable target.

## 2. Complete-resolution standard

Complete resolution means both of:

1. **Problem A:** unconditional proofs of every item on the Step-0 certified open-list - each proof either fully classical or resting on machine-verifiable certificates (creative-telescoping certificate pairs, Wronskian identities, exact CAS-checkable reductions), all certificates independently re-checked per section 6.
2. **Problem B:** a proof of coaction closure valid at all loop orders, with the space $\mathcal P_{\phi^4}$ and the coaction exactly as fixed in section 1.3.

**Not accepted as resolution:**

- Numerical verification of any identity to any number of digits, including PSLQ matches at 10,000 digits.
- Re-proofs of theorems already established by Zhou or Fresán–Sabbah–Yu, presented as new results (these are calibration targets only, cf. P3).
- Coaction verification at finitely many loop orders, however far beyond the current frontier.
- Proofs conditional on the period conjecture, Grothendieck's standard conjectures, or Galois-descent hypotheses, unless the conditionality is flagged in the first paragraph of the report - and even then such results meet only partial-result standard.
- Evaluations "up to an undetermined rational factor".
- Heuristic weight/motivic-depth arguments without a theorem.

## 3. Graded partial-result targets

### P1 - Audit plus certified numerical frontier

- Task (i): the Step-0 open-conjecture dossier - every Broadhurst-type conjecture classified proved/open, with source trail and exact statement in section-1 notation.
- Task (ii): Arb-certified enclosures, $\ge 1000$ digits, of all $\mathrm{IKM}(a,b;k)$ with $a+b\le 8$, $k \le 9$, each computed by two independent methods (rigorous quadrature vs holonomic continuation) with overlapping balls.
- Task (iii): all known closed forms and $L$-value identities re-verified against the enclosures.
- *Certificate:* dossier with citations; ball outputs plus both code paths; SHA-256 manifest.

### P2 - Telescoping ground truth

- Derive and certify the holonomic ODEs satisfied by the Bessel-moment integrands and moment sequences (Borwein–Salvy 2007; Vanhove's banana operators), via creative telescoping with explicit certificates.
- Use the operators to prove the classical sum rules that admit telescoping proofs.
- *Certificate:* telescoper/certificate pairs whose verification is a pure polynomial-arithmetic identity, checked in two independent CAS (ore_algebra and HolonomicFunctions).

### P3 - Calibration re-proof

- Re-derive one already-proved Broadhurst–Mellit determinant formula end-to-end with our own toolchain (Zhou's Wronskian route: Vanhove operators, Wronskian evaluation, connection constants), every computational step machine-checked.
- This is calibration: it validates the pipeline against a known theorem before it is aimed at an open one.
- *Certificate:* the full identity chain in executable form.

### P4 - One new identity (publishable theorem)

- Prove at least one currently-open item from the P1 dossier - recommended: an open $n=8$ moment/$L$-value relation or an open congruence family - by telescoping certificates plus Eichler-integral/Wronskian reduction.
- *Certificate:* proof document plus machine-checkable reduction chain.

### P5 - Coaction: independent re-verification and extension

- Recompute the $\phi^4$ periods and their $f$-alphabet coaction data through 7 loops with independent code paths: HyperInt and HyperLogProcedures cross-validated against each other and against an in-house $f$-alphabet coaction checker.
- Extend the published verification frontier by at least one new period.
- *Certificate:* period/coaction database, independent checker source, manifest.

### P6 - Structural theorem

- Prove coaction closure for an infinite subfamily - e.g. the zigzag family, whose periods are known in closed form (Brown–Schnetz zigzag theorem, ~2012) - or prove that the $\mathbb{Q}$-span of all Bessel moments at fixed $n$ is stable under $\Delta$.
- *Certificate:* theorem with machine-checked identity content.

### P7 - Strongest short of resolution

- Either all determinant-type conjectures proved for all $n$, or coaction closure proved in bounded coradical degree at all loop orders.
- *Certificate:* as P4/P6, at scale.

## 4. Known results and prior art

- Bailey–Borwein–Broadhurst–Glasser 2008: systematic evaluations of low-$n$ Bessel moments; elliptic-integral and $\Gamma$-value closed forms.
- Borwein–Salvy ~2007–2008: holonomic recurrences/ODEs for the moments $c_{n,k}$.
- Broadhurst 2016 ("Feynman integrals, $L$-series and Kloosterman moments") and Broadhurst–Mellit 2016: the $L$-value and determinant conjectures at $n = 5,6$ and beyond.
- Broadhurst–Roberts 2018: quadratic relations between Bessel moments; dual determinant conjectures.
- Zhou Yajun 2017–2019: proofs of a large part of the corpus - the $n=5,6$ $L$-value evaluations (Wick-rotation/Eichler-integral method), the Broadhurst–Mellit determinant formulae (Wronskian factorization), and several sum-rule families. The exact residual open set must be established in Step 0 (verify).
- Fresán–Sabbah–Yu ~2020–2023: Hodge-theoretic/motivic proofs of the Broadhurst–Roberts quadratic relations; Kloosterman-connection framework identifying the relevant motives for $n \ge 7$ (verify which special-value statements remain open).
- Vanhove 2014: differential operators for banana integrals; Bloch–Kerr–Vanhove 2015–2017: the sunrise/banana motives.
- Schnetz 2010: census of $\phi^4$ transcendentals; Brown ~2015–2017: motivic periods, the coaction, and the small-graphs principle; Panzer–Schnetz 2016: the coaction conjecture, with computational verification on all periods then known. The assignment sheet's "verified to loop order ~11" is treated here as unverified; the published complete knowledge is through 7 loops with substantial partial data beyond (verify the current frontier and Schnetz's post-2019 extensions).
- Tools literature: Panzer 2014 (HyperInt); Schnetz, HyperLogProcedures (maintained through the 2020s); Koutschan ~2010 (HolonomicFunctions); Mezzarobba ~2016+ (rigorous holonomic continuation in ore_algebra).

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

All modes here are `[sym]`: exact identities with certificate-bearing derivations, numerics only as scaffolding.

1. **Step 0 (audit).** Read the primary sources above; produce the open-list with, for each item, the exact statement in section-1.2 notation. Nothing downstream may cite "Broadhurst's conjecture" without resolving which one.
2. **Certified numerics (P1).** Arb via python-flint:
   - split at $t = T$; ball-evaluated Bessel functions with rigorous Gauss–Legendre or double-exponential quadrature on $(0, T]$;
   - explicit tail bounds from $K_0(t) \le e^{-t}\sqrt{\pi/2t}$ and $I_0(t)K_0(t) \le 1/(2t)$;
   - target 1000–5000 digits; cross-path via holonomic ODE continuation with rigorous transition matrices (ore_algebra, Mezzarobba-style).
   - Single workstation: minutes-to-hours per moment at 1000 digits.
3. **Telescoping (P2, P4).** HolonomicFunctions (Mathematica) and/or reduction-based telescoping; certificates re-verified by a standalone SageMath script performing only exact polynomial arithmetic over $\mathbb{Q}$; finite-field prefiltering to control ansatz sizes.
4. **$L$-values.** Pari/GP `lfunmf`/`lfun` for $L(f_{4,6}, s)$, $L(f_{6,6}, s)$ and Kloosterman-motive $L$-functions where constructible, to precision matching P1; PSLQ via mpmath at $\ge 2000$ digits, always re-run at doubled precision and with a decoy basis element to expose false positives.
5. **$\phi^4$ pipeline (P5).**
   - HyperInt (Maple) for primitive graphs through 7 loops - feasible on a 64–256 GB workstation for most graphs; expect memory blow-up on the hardest 8-loop primitives (known failure mode; record and skip).
   - HyperLogProcedures for $f$-alphabet decompositions and coaction data.
   - In-house Python implementation of the coproduct on the $f$-alphabet as the independent checker.
6. **Formal layer (optional).** Lean 4 formalization of the elementary moment recursions and the $n \le 2$ evaluations, as a probe of formalization cost only.

Expected failure modes: PSLQ misidentification at insufficient precision; trusting Maple's non-rigorous `int`/`evalf` for anything labeled certified; certificate size blow-up at $n \ge 8$; and the motivic/numerical conflation - all coaction statements live on motivic lifts, and the report must say so, since the numerical periods alone cannot even express the conjecture.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Every certified digit is an Arb ball with directed rounding; every identity proof reduces to exact polynomial or algebraic arithmetic over $\mathbb{Q}$; floating point appears only in exploration and is labeled as such.
2. **Independent verification.** Each telescoping certificate is re-checked by a standalone SageMath checker sharing no code with the system that produced it; numerical moments are double-computed by quadrature and holonomic continuation; the coaction data is re-checked by the in-house $f$-alphabet checker independent of HyperLogProcedures.
3. **Reproducibility.** Pinned versions of FLINT/Arb, Pari/GP, SageMath, Maple, Mathematica; all scripts, precisions, and seeds in the repository; SHA-256 manifest over every database (moment enclosures, period tables, $f$-alphabet data, certificates).
4. **Preservation.** All search code, failed PSLQ runs, and abandoned ansätze are preserved and indexed; anything discarded is listed as discarded.
5. **Honest reporting.** The final report opens with the Step-0 audit and a statement of whether the section-2 standard was met; every claim is labeled proved / conditionally proved (with hypotheses) / numerically verified - and no numerical match, at any precision, is reported as an identity.
