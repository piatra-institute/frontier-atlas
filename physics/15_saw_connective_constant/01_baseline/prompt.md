# PROMPT FOR THE SQUARE-LATTICE CONNECTIVE CONSTANT AND ITS PARAFERMIONIC OBSERVABLE PROBLEM

## Self-avoiding walks on $\mathbb Z^2$: an exact observable in the Duminil-Copin–Smirnov style, a proof that none exists in a defined class, or certified progress on bounds and enumeration

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 15 of 50 (Tier 2)
**Source:** top-50 list #26, category C (exactly solvable models and lattice statistics)
**Modes:** `[proof]` `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The connective constant of self-avoiding walks on the square lattice, $\mu\approx2.63815853032\ldots$, has no known closed form and no proof that one exists or cannot exist. On the honeycomb lattice the analogous constant $\sqrt{2+\sqrt2}$ was proven by Duminil-Copin and Smirnov (2012) using a discretely holomorphic parafermionic observable whose contour sums vanish exactly at criticality.

The square-lattice question is therefore sharply structured: either an analogous observable with exact local vanishing exists on $\mathbb Z^2$ - determining $\mu$ - or it does not, and the non-existence is itself a finite, machine-checkable statement class by class, because for a fixed locality class the vanishing conditions form a finite exact linear system. This prompt targets that dichotomy, plus the certifiable substance around it: exact enumeration with an independent toolchain, rigorous upper bounds (Pönitz–Tittmann automaton method) and lower bounds (Kesten bridge decomposition) with exact-arithmetic certificates.

The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Walks and the constant

- A self-avoiding walk (SAW) of length $n$ on $\mathbb Z^2$ (nearest-neighbour edges) is a sequence $\gamma=(\gamma_0,\dots,\gamma_n)$ with $\gamma_0=0$, $\|\gamma_{i+1}-\gamma_i\|_1=1$, all $\gamma_i$ distinct.
- $c_n$ = number of such walks: $c_0=1$, $c_1=4$, $c_2=12$, $c_3=36$, $c_4=100$ (OEIS A001411; re-derive, do not import).
- Submultiplicativity $c_{n+m}\le c_nc_m$ (Hammersley–Morton 1954) gives
\[
\mu=\lim_{n\to\infty}c_n^{1/n}=\inf_n c_n^{1/n}.
\]
- Reference numerical value: $\mu=2.63815853032790(3)$ (Jacobsen–Scullard–Guttmann 2016 - verify).
- A *bridge* is a SAW with $\gamma_0\cdot e_1<\gamma_i\cdot e_1\le\gamma_n\cdot e_1$ for all $i\ge1$ (first-coordinate convention fixed here). Bridge counts satisfy $b_{n+m}\ge b_nb_m$ and $\lim b_n^{1/n}=\mu$ (Kesten 1963), so **every** $b_n^{1/n}$ is a rigorous lower bound for $\mu$.

### 1.2 The honeycomb mechanism (calibration case)

On the honeycomb lattice, for a mid-edge domain $\Omega$ with boundary mid-edge $a$, the parafermionic observable
\[
F(z)=\sum_{\gamma\subset\Omega:\,a\to z}x^{\ell(\gamma)}\,e^{-i\sigma W_\gamma(a,z)},\qquad\sigma=\tfrac58,
\]
with $W_\gamma$ the total winding, satisfies at $x_c=(2+\sqrt2)^{-1/2}$, for every interior vertex $v$ with adjacent mid-edges $p,q,r$,
\[
(p-v)F(p)+(q-v)F(q)+(r-v)F(r)=0,
\]
and this exact local vanishing telescopes over domains, yielding $\mu_{\mathrm{hex}}=\sqrt{2+\sqrt2}$ (Duminil-Copin–Smirnov 2012).

### 1.3 Observable classes on $\mathbb Z^2$

- Fix a locality radius $K\ge1$ and a finite set $S$ of unimodular *turn weights*. The class $\mathcal C_K$ consists of observables
\[
F(z)=\sum_{\gamma:\,a\to z}x^{\ell(\gamma)}\prod_{\text{turns }t\in\gamma}\lambda_t,\qquad\lambda_t\in S,
\]
together with candidate local identities: linear combinations, with coefficients depending only on the local geometry within radius $K$, of values of $F$ at mid-edges around a vertex or plaquette, required to vanish identically over all finite walk configurations.
- Because walk contributions through a window factor through finitely many boundary-connectivity classes (Temperley–Lieb-type link states with a marked endpoint), the vanishing requirement for fixed $K$ is a **finite linear system over $\mathbb Q(x,\lambda)$**.
- This finiteness claim must be proven as part of the work, with the state space made explicit; it is the hinge that makes the problem machine-checkable.

### 1.4 The problem

Prove one of:

- **(A)** There exist $K$, weights, and a local identity in $\mathcal C_K$ whose exact telescoping determines $x_c=1/\mu$ for square-lattice SAW, with a complete proof yielding a closed form for $\mu$.
- **(B)** For each $K\le K_0$ (finite computation), or for all $K$ (theorem), the only solutions of the vanishing system are trivial - identically zero, or degenerate solutions that fail to pin a nontrivial $x_c$. That is: no honeycomb-style observable exists on $\mathbb Z^2$ within $\mathcal C_K$.

### 1.5 Closed-form candidates and the standing trap

- The biquadratic candidate $13\mu^4-7\mu^2-581=0$ (circulated since the 1980s–90s; attribution uncertain - verify) is reported inconsistent with the Jacobsen–Scullard–Guttmann precision estimate (verify current status before repeating the claim).
- **Trap warning:** $1+\sqrt2$ is the proven critical *surface adsorption fugacity* on the honeycomb lattice (Beaton–Bousquet-Mélou–de Gier–Duminil-Copin–Guttmann 2014). It is not, and never was, a candidate for the square-lattice $\mu$. Do not conflate the two; any session output doing so is defective.

## 2. Complete-resolution standard

Complete resolution is one of:

1. **(A) met:** an explicit observable and local identity; proof of exact vanishing in exact algebra over $\mathbb Q(x,\lambda)$ or a number field; the telescoping argument on arbitrary simply-connected domains; and the derivation of a closed form for $\mu$ with full rigor, consistent with the numerical value.
2. **(B) met in theorem form:** a proof that for *all* $K$ the class $\mathcal C_K$ - with the definition frozen before the search - contains no observable with exact local vanishing pinning a nontrivial $x_c$, together with a precise statement of what the class does and does not include.
3. A proof that $\mu$ is algebraic with explicit minimal polynomial, or a proof that it is not algebraic, by any rigorous route.

**Not accepted as resolution:**

- Numerical estimates of $\mu$ to any precision, including new series/enumeration records.
- Observables whose local identities hold only approximately, only numerically, or only for walks up to a finite length.
- Finite-$K$ non-existence ($K\le K_0$) represented as the full class-(B) theorem - that is target P4/P5, a partial result.
- Adopting the integrable dilute O($n{=}0$) square-lattice loop model (Nienhuis 1990; Batchelor–Nienhuis–Warnaar early 1990s) as "SAW on $\mathbb Z^2$": it has exact structure but different microscopic weights (vacancies/vertex weights); results there do not resolve pure SAW unless an exact equivalence is proven.
- Asserting the biquadratic or the $1+\sqrt2$ value without proof; both are excluded or irrelevant (verify).
- PSLQ null searches presented as impossibility of a closed form.

## 3. Graded partial-result targets

**P1 - certified enumeration with our own toolchain.**
Reproduce $c_n$ with two independent implementations: C++ backtracking with symmetry pruning for $n\le36$; finite-lattice/transfer-matrix method with exact big-integer arithmetic for $n\lesssim50$–$60$ on a workstation. Cross-check against published tables (Jensen 2004 to $n=71$; later extension to $n=79$ - verify).
*Certificate:* full integer tables, dual-implementation agreement, SHA-256 manifest.

**P2 - rigorous lower bound via bridges.**
Enumerate bridges $b_n$ exactly; report the best certified bound $\mu\ge b_n^{1/n}$ attainable; improve via irreducible-bridge renewal inequalities (Kesten). Compare against the published record ($\approx2.62$ - verify value and attribution).
*Certificate:* exact $b_n$ integers plus the inequality chain in rational arithmetic.

**P3 - rigorous upper bound via automata.**
Reimplement the Pönitz–Tittmann (2000) bound $\mu\le2.6792$: SAWs inject into a regular language; the bound is the Perron root of a transfer automaton, certified by an exact rational vector $v>0$ with $Av\le\lambda v$ entrywise. Push the memory parameter as far as a workstation allows; any certified improvement on 2.6792 is publishable.
*Certificate:* the automaton, $v$, $\lambda\in\mathbb Q$, and an independent checker that only multiplies and compares rationals.

**P4 - observable search over finite classes.**
Implement the connectivity-class reduction for $\mathcal C_K$; for $K=1,2,3$ compute the exact nullspace of the vanishing system over $\mathbb Q(x,\lambda)$. Either outcome is valuable: a nontrivial solution escalates toward (A); an empty nullspace is a theorem - "no observable in $\mathcal C_K$ for $K\le3$."
*Certificate:* the linear systems and nullspace computations in exact arithmetic, with dual implementations (SageMath plus independent fraction-free elimination).

**P5 - structural no-go.**
Extend P4 to a proof scheme covering all $K$ for a natural subclass (e.g. pure winding-weight observables $\lambda^W$), plausibly via the discrete-holomorphicity classification of Ikhlef–Cardy 2009: local vanishing forces integrable weights, and pure SAW weights sit off the integrable manifold - turn this into a theorem for the subclass. This is the strongest realistic proof-mode outcome.
*Certificate:* proof text; all weight equations verified in exact arithmetic.

**P6 - negative D-finiteness certificates.**
From all available $c_n$, produce the exact statement "no linear recurrence with polynomial coefficients within the stated (order, degree) box fits the series," via ore_algebra guessing converted into certified exact rank computations. Supports, but does not prove, the expected non-D-finiteness of the SAW generating function.
*Certificate:* exact nullspace-empty proof over $\mathbb Q$, reproducible.

**P7 - frontier extension.**
Extend the enumeration record for $c_n$ or $b_n$ beyond the published frontier if hardware allows; otherwise report the exact resource wall encountered.

Honest calibration: (A) is unlikely - the honeycomb proof leans on degree-3 vertices, and the $\mathbb Z^2$ vanishing system is over-determined. The expected genuine products are P2–P5.

## 4. Known results and prior art

- Hammersley–Morton 1954 (submultiplicativity); Hammersley–Welsh 1962 ($c_n\le\mu^ne^{O(\sqrt n)}$); Kesten 1963 (bridges, pattern theorem).
- Nienhuis 1982: Coulomb-gas predictions; honeycomb $\mu=\sqrt{2+\sqrt2}$; exponent $\gamma=43/32$.
- Duminil-Copin–Smirnov 2012 (Annals of Mathematics): honeycomb connective constant via the parafermionic observable.
- Beaton–Bousquet-Mélou–de Gier–Duminil-Copin–Guttmann 2014: honeycomb critical surface fugacity $1+\sqrt2$ - the value *not* to conflate with square-lattice $\mu$.
- Duminil-Copin–Hammond 2013: SAW is sub-ballistic.
- Grimmett–Li, 2014 onward: general theory of connective constants; strict inequalities; bounds for lattice families.
- Enumeration: Jensen 2004 ($n=71$); Jensen ~2013 extension to $n=79$ (verify); series analysis Jensen–Guttmann 1999.
- Growth-constant estimate $\mu=2.63815853032790(3)$: Jacobsen–Scullard–Guttmann 2016 (verify).
- Bounds: Alm 1993 upper bound $\approx2.696$; Pönitz–Tittmann 2000 upper bound $2.6792$; best lower bound $\approx2.62$ via bridge enumeration (Jensen - verify current records on both sides).
- Discrete holomorphicity: Ikhlef–Cardy 2009; Cardy's subsequent reviews.
- Integrable dilute O($n$) model on the square lattice: Nienhuis 1990; Batchelor–Nienhuis–Warnaar early 1990s.
- Biquadratic candidate $13\mu^4-7\mu^2-581=0$: folklore, attribution uncertain (verify); reported excluded by modern precision (verify).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

### 5.1 `[sym]` Enumeration and series

- C++ finite-lattice/transfer-matrix code (Conway–Enting lineage) with GMP integers; boundary-state growth $\sim3^w$ bounds workstation reach at $n\lesssim55$ for $c_n$, further for $b_n$.
- Python brute force to $n\approx30$ as the independent check.
- ore_algebra (SageMath) for P6 guessing sweeps, then exact rank certification in FLINT.
- mpmath / Pari-GP PSLQ against the $\mu$ digits for closed-form exploration: with ~15 digits only small-height candidates are even testable; log every candidate and state exclusions honestly.

### 5.2 `[sym]` Observable linear algebra

- Enumerate local walk-connectivity classes through a $K$-window exactly; build the vanishing system with entries in $\mathbb Q(x,\lambda)$.
- Fraction-free Gaussian elimination (SymPy/SageMath) plus an independent evaluation-at-random-rationals rank check.
- Expected failure modes: state-space blowup at $K=3$–$4$ (quotient by lattice symmetries); spurious "solutions" valid only at special $x$ (detect by exact substitution and reject).

### 5.3 `[proof]` Bounds and no-go theorems

- The automaton upper bound and bridge lower bound are fully certifiable on a workstation; main risk in P3 is automaton-construction bugs - mitigate with an independent language-membership checker run on random walks.
- P5 theorem shape: "exact local vanishing in subclass $X$ implies weight equations $E$; $E$ has no solution at SAW weights." The equations come out of the P4 systems as finitely many polynomial identities, machine-verifiable.
- Calibrate everything on the honeycomb lattice first: the pipeline must re-derive the Duminil-Copin–Smirnov identity before its square-lattice output is admissible.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All enumeration in exact integers; all bound certificates ($v$, $\lambda$, inequality chains) in $\mathbb Q$; all observable nullspace results over $\mathbb Q(x,\lambda)$ or exact number fields. Floating point only in exploratory series analysis, so labeled.
2. **Independent verification.** Dual implementations for enumeration (C++/Python), for the Perron-certificate checker, and for the linear-algebra ranks (SageMath plus independent elimination); every certificate re-verifiable in minutes by code disjoint from the search code.
3. **Reproducibility.** Every table and certificate carries its generating command, tool versions, and SHA-256 hashes; automaton definitions serialized in a documented format sufficient for reimplementation from the report alone.
4. **Preservation.** All observable-class searches - including classes yielding empty nullspaces - are part of the record; a class searched but not preserved must be declared and its claimed result withdrawn.
5. **Honest reporting.** The final report states up front whether (A), (B), or the algebraicity question was resolved (expected: no), lists which P-targets were certified, and never represents finite-$K$ no-go results, bound improvements, or enumeration records as a determination of $\mu$.
