# PROMPT FOR THE ANALYTIC NATURE OF THE 2D ISING SUSCEPTIBILITY

## The zero-field magnetic susceptibility of the square-lattice Ising model

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 06 of 50 (Tier 1)
**Source:** top-50 list #21, category C (exactly solvable models and lattice statistics)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Onsager's 1944 solution gives the square-lattice Ising free energy in closed form, and the spontaneous magnetization is algebraic (Onsager–Yang), yet the zero-field susceptibility $\chi(T)$ has resisted closed form for eighty years. It is the best-instrumented open function in lattice statistics: a form-factor decomposition (Wu–McCoy–Tracy–Barouch 1976), series known to thousands of terms, and enormous exact Fuchsian ODEs for the components $\chi^{(n)}$, which are diagonals of rational functions. Nickel's singularity analysis suggests a natural boundary on the unit circle of the $\sinh 2K$ variable, which would make $\chi$ non-D-finite; whether $\chi$ is even differentially algebraic is open. The task is to settle the analytic nature of $\chi$ - D-finite, differentially algebraic, or neither, ideally with a natural-boundary proof - or, realistically, to produce new certified structure from the massive exact data. This is pure symbolic mining of exact objects: our best-matched `[sym]` problem. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Model and normalizations

Square lattice $\mathbb{Z}^2$, spins $\sigma_i\in\{\pm1\}$, isotropic nearest-neighbour energy $E=-J\sum_{\langle ij\rangle}\sigma_i\sigma_j$, coupling $K=J/k_BT>0$ (ferromagnetic). Finite boxes with free boundary conditions; all objects below are thermodynamic-limit quantities (existence is classical and may be cited). Define

\[
s=\sinh 2K,\qquad T=T_c\iff s=1,\qquad
w=\tfrac{1}{2}\,s/(1+s^{2}),
\]

$w$ being the standard variable of the $\chi^{(n)}$ ODE literature. A frozen conversion table between $s$, $w$, $v=\tanh K$, and the low-temperature variables used by the series literature is part of the session record.

### 1.2 Susceptibility

With the two-point function $\langle\sigma_{0}\sigma_{n}\rangle$ in the infinite-volume Gibbs state (the $+$ state for $T<T_c$) and spontaneous magnetization $M$ ($=0$ for $T>T_c$),

\[
k_BT\,\chi(T)\;=\;\tilde\chi(T)\;=\;\sum_{n\in\mathbb{Z}^2}\bigl(\langle\sigma_{0}\sigma_{n}\rangle-M^{2}\bigr).
\]

$\tilde\chi$ is the *reduced susceptibility*; all series objects below refer to $\tilde\chi$.

### 1.3 Form-factor decomposition

By Wu–McCoy–Tracy–Barouch (1976), there exist explicit $(n-1)$-fold integrals $\tilde\chi^{(n)}(s)$ - integrals of algebraic integrands over $[0,2\pi]^{n-1}$, arising from $n$-particle intermediate states of the diagonalized transfer matrix - such that

\[
\tilde\chi(T)=\sum_{n\ \mathrm{odd}}\tilde\chi^{(n)}(s)\quad(T>T_c),
\qquad
\tilde\chi(T)=\sum_{n\ \mathrm{even}}\tilde\chi^{(n)}(s)\quad(T<T_c),
\]

with $\tilde\chi^{(1)}$ and $\tilde\chi^{(2)}$ elementary. Adopt the integral representations exactly as printed in Nickel (1999) and in the Zenine–Boukraa–Hassani–Maillard papers; transcribing and re-verifying those formulas against series data is part of P1, and the transcription used must be frozen into the record. Key structural facts (to be used, and re-verified where cheap):

- each $\tilde\chi^{(n)}$ is D-finite, annihilated by an explicit Fuchsian operator (known exactly for $n\le4$, modulo primes for $n=5,6$);
- each $\tilde\chi^{(n)}$ is the diagonal of an explicit rational function, hence a globally bounded series, algebraic modulo every prime;
- the full $\tilde\chi$ is the infinite sum, and none of the per-$n$ finiteness properties automatically survive the sum - that gap is the problem.

### 1.4 Target properties

A formal power series $f\in\mathbb{Q}[[x]]$ is *D-finite* (holonomic) if it satisfies a nonzero linear ODE with polynomial coefficients; *differentially algebraic* (DA) if $P(x,f,f',\dots,f^{(r)})=0$ for some nonzero polynomial $P$; *hypertranscendental* otherwise. A function has a *natural boundary* on a curve if it is analytic on one side and admits analytic continuation across no arc of the curve.

### 1.5 The open question (adopted formulation)

Determine the analytic nature of $\tilde\chi$ as a function of $s$ (equivalently of $w$ or the standard series variables): prove or disprove

1. $\tilde\chi$ is D-finite - conjecturally false;
2. the unit circle $|s|=1$ is a natural boundary for $\tilde\chi$ - Nickel's conjecture; it implies 1 is false;
3. $\tilde\chi$ is differentially algebraic - open in both directions.

A complete resolution settles 2, or otherwise settles 1 and 3, with proofs. Numerical evidence, however extensive, settles none of these.

## 2. Complete-resolution standard

A complete resolution is a proof, in refereeable form with machine-verified supporting computations, of one of:

- **(A)** the unit circle $|s|=1$ is a natural boundary of $\tilde\chi$ (hence non-D-finiteness), with an explicit statement of what remains open about differential algebraicity; or
- **(B)** non-D-finiteness of $\tilde\chi$ by other means; or
- **(C)** a proof that $\tilde\chi$ is, or is not, differentially algebraic - with the annihilating algebraic differential equation exhibited exactly in the positive case; or
- **(D)** (revolution scenario) an exact closed form or complete constructive characterization of $\tilde\chi$, verified symbolically against the known ODE, series, and singularity data to full available depth.

Every supporting computation (series, operators, exponents) must carry certificates per section 6.

**Not accepted as resolution:**

- Numerical or series-based "evidence" of a natural boundary: accumulating singularities of the partial sums $\tilde\chi^{(n)}$ do not preclude cancellation in the full sum - this gap is the whole problem, and glossing it voids the claim.
- Non-D-finiteness claims about individual $\tilde\chi^{(n)}$ (each is in fact D-finite; confusion here voids the report).
- "No ODE of order $\le r$, degree $\le d$ fits $N$ coefficients" presented as non-D-finiteness: it is a valuable exclusion certificate (P4), not a resolution.
- Scaling-limit statements (Painlevé structure of the scaled susceptibility) presented as statements about the lattice function $\tilde\chi$.
- Results modulo primes presented as characteristic-0 conclusions.
- Restatements of the Guttmann–Enting or Nickel conjectures with new numerology.

## 3. Graded partial-result targets

Full resolution is unlikely in a session; the graded targets are the goal, and each of P1–P5 produces a durable certified artifact.

- **P1 - Reproduce the series frontier with our own verified code.**
  - *Task:* implement the quadratic difference equations for Ising correlations (Perk 1980; the engine behind Orrick–Nickel–Guttmann–Perk) in exact arithmetic; recompute high- and low-temperature expansions of $\tilde\chi$ to several hundred terms at minimum; match published coefficients exactly wherever available.
  - *Certificate:* dual-implementation agreement (SymPy reference vs C++/FLINT production), coefficient-level match against published data, SHA-256 of coefficient files.
- **P2 - Certified re-derivation of the $\tilde\chi^{(3)}$ and $\tilde\chi^{(4)}$ Fuchsian ODEs.**
  - *Task:* generate long series for $\tilde\chi^{(3)},\tilde\chi^{(4)}$ from their integral/diagonal representations; guess minimal operators with ore_algebra; *prove* them via creative telescoping / Picard–Fuchs computation on the diagonal representation (Bostan–Boukraa–Christol–Hassani–Maillard program).
  - *Certificate:* telescoper identity verified by independent substitution; operator annihilates the series to full depth; comparison against the published operators.
- **P3 - Certified singularity atlas.**
  - *Task:* for $\tilde\chi^{(n)}$, $n\le6$ (published operators may be imported for $n=5,6$, clearly labeled): exact singularity locations as roots of explicit polynomials; local exponents from certified indicial equations; verified confirmation of the Nickel singularities on $|s|=1$ and their accumulation pattern in $n$.
  - *Certificate:* exact algebra (indicial polynomials, factorizations) re-verified in a second CAS; Arb-certified connection data wherever analytic continuation is invoked.
- **P4 - Rigorous exclusion certificates for the full $\tilde\chi$.**
  - *Task:* from $N$ certified series coefficients, prove: no linear ODE with order $\le r$ and coefficient degree $\le d$ annihilates the series to depth $N$, for all $(r,d)$ in an explicit region; and no algebraic differential equation of order $\le2$ and total degree $\le d'$ (small $d'$) does either. Exact linear algebra over $\mathbb{Q}$, or over several primes with lifting.
  - *Certificate:* the rank computations themselves, reproducible and independently re-run; a precise statement of what the certificates do and do not imply.
- **P5 - Mod-$p$ and globally bounded structure.**
  - *Task:* certify algebraicity modulo small primes of $\tilde\chi^{(n)}$ (diagonal ⇒ algebraic mod $p$) with explicit annihilating polynomials; investigate and certify the analogous structure for the *full* $\tilde\chi$ modulo 2 and small primes (published claims exist - verify), including how degrees grow with $p$. Any proved statement of the form "$\tilde\chi \bmod p$ is algebraic for all $p$ in an explicit family, with degree pattern X" is a new structural theorem.
  - *Certificate:* polynomial identities verified by exact substitution to full series depth, dual implementations.
- **P6 - A theorem about the boundary.**
  - *Task:* the strongest realistic advance - a proof that singularities of the partial sums survive on a dense subset of $|s|=1$ in the full $\tilde\chi$ (e.g. via positivity or monotonicity of form-factor contributions in suitable variables), or a proof of (A)/(B) outright.
  - *Certificate:* mathematics in refereeable form; every computational ingredient certified per section 6.

## 4. Known results and prior art

- L. Onsager (1944): free energy. C. N. Yang (1952): spontaneous magnetization (algebraic).
- T. T. Wu, B. McCoy, C. Tracy, E. Barouch (1976): form-factor expansion of $\tilde\chi$; scaling functions and the Painlevé III connection (McCoy–Tracy–Wu tradition).
- J. H. H. Perk (1980): quadratic difference equations for Ising correlations - the engine behind fast exact series. M. Jimbo, T. Miwa (1980): diagonal correlations and Painlevé VI.
- B. Nickel (1999, 2000): singularities of $\tilde\chi^{(2n+1)}$ on $|s|=1$, becoming dense as $n\to\infty$; the natural-boundary conjecture.
- W. Orrick, B. Nickel, A. J. Guttmann, J. H. H. Perk (~2001): susceptibility series to several hundred terms; scaling analysis. Y. Chan, A. J. Guttmann, B. Nickel, J. H. H. Perk (~2011): extension to on the order of two thousand terms (verify exact counts and variables).
- A. J. Guttmann, I. Enting (1996): the D-finiteness test philosophy; conjecture that $\tilde\chi$ is not D-finite.
- N. Zenine, S. Boukraa, S. Hassani, J.-M. Maillard (2004–2005): Fuchsian ODEs for $\tilde\chi^{(3)}$ (order 7) and $\tilde\chi^{(4)}$ (order 10). The same group with I. Jensen and collaborators (~2009–2011): $\tilde\chi^{(5)},\tilde\chi^{(6)}$ operators modulo primes, minimal orders in the tens (verify exact orders); global nilpotence and factorization studies.
- A. Bostan, S. Boukraa, G. Christol, S. Hassani, J.-M. Maillard (~2012–2013): $\tilde\chi^{(n)}$ as diagonals of rational functions; globally bounded series; algebraicity modulo primes.
- A. Bostan, P. Lairez, B. Salvy (~2013–2017): algorithms for diagonals and binomial sums; P. Lairez (~2016): periods of rational integrals - the proof engines for P2.
- Studies of the full $\tilde\chi$ modulo 2 and small primes (Maillard school and/or Guttmann collaborations - verify the precise published statements before relying on them).
- To our knowledge: no proof of the natural boundary, of non-D-finiteness, or of (non-)differential-algebraicity of the full $\tilde\chi$.

**Status as of mid-2026 - re-verify against current literature before starting the session.** In particular check for: any natural-boundary proof, new series extensions, new results on differential algebraicity of diagonals or of $\tilde\chi$ itself, and characteristic-0 proofs of the $\tilde\chi^{(5,6)}$ operators.

## 5. Attack plan

Single-workstation throughout (≤ 64 GB RAM); the heaviest published objects (the $\tilde\chi^{(5,6)}$ operators) are imported, not recomputed.

1. **Series engine (P1).**
   - C++ with FLINT/GMP implementing Perk's quadratic recurrences for $\langle\sigma_{0,0}\sigma_{M,N}\rangle$ as exact rationals in the chosen expansion variable; assemble the $\tilde\chi$ lattice sums with rigorous truncation bookkeeping (which shells contribute at which series order - prove the bound used).
   - SymPy prototype validated on the first ~50 published terms before scaling up.
   - Failure mode: silent misnormalization across $s$, $w$, $v$ conventions - mitigate with the frozen conversion table, verified symbolically.
2. **Guess-and-prove (P2).**
   - Sage + ore_algebra: Hermite–Padé guessing of operators, run modulo several 31-bit primes first, then rational reconstruction.
   - Proof route: represent $\tilde\chi^{(3)},\tilde\chi^{(4)}$ as diagonals/multiple binomial sums; creative telescoping via ore_algebra (Zeilberger/Chyzak-style) or Lairez's period algorithm.
   - Failure mode: telescoper size explosion - fall back to "operator annihilates the series to depth $N\gg$ (order)(degree)" statements, clearly labeled guessed-plus-strongly-checked, never "proved".
3. **Singularity atlas (P3).**
   - Exact indicial computations in Sage/SymPy; Arb (via python-flint) for certified analytic continuation along explicit paths, to determine which formal singularities of the operators are actual singularities of the analytic objects.
   - Failure mode: precision exhaustion near dense singularity clusters - report enclosure failures explicitly rather than downgrading rigor.
4. **Exclusion linear algebra (P4).**
   - Dense linear algebra over $\mathbb{F}_p$ (FLINT `nmod_mat` or custom C++) on Hermite–Padé matrices of dimension up to ~$10^4$; several primes; exact rank certificates.
   - Failure mode: undersized $N$ relative to the $(r,d)$ region - the certificate must state the exact inequality used to size the matrix, and the region must be shrunk to match.
5. **Mod-$p$ mining (P5).**
   - Series mod $p$ to depth $10^5$–$10^6$ via the P1 engine reduced mod $p$; algebraicity guessing by Hermite–Padé over $\mathbb{F}_p[x]$; verification by exact substitution of the annihilating polynomial to full depth.
   - Failure mode: mistaking high-degree algebraicity for its absence - always report the searched degree bound alongside any negative.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All series coefficients exact rationals/integers; all operators over $\mathbb{Q}[x]$ (or mod $p$, labeled); Arb ball arithmetic with directed rounding for every analytic-continuation claim; floating point only in exploratory singularity scans, never in certificates.
2. **Independent verification.** Dual series engines (SymPy reference vs C++/FLINT) compared coefficient-by-coefficient; every guessed operator re-applied to the series by an independent naive-polynomial-arithmetic checker; every mod-$p$ algebraicity certificate re-verified by a standalone script in a different language from the discovery code.
3. **Reproducibility.** Versions of FLINT, Arb, Sage, ore_algebra recorded; all primes, truncation orders, and variable conventions in a frozen `conventions.md`; SHA-256 manifest over series files, operators, certificates, and checker logs.
4. **Preservation.** All search code, including failed telescoping attempts and undersized exclusion runs, preserved; imported published data (long series, $\tilde\chi^{(5,6)}$ operators) archived with provenance and hashes, and clearly separated from recomputed data.
5. **Honest reporting.** The report opens by stating whether any of (A)–(D) was achieved (expected: no); exclusion certificates (P4) and mod-$p$ structure (P5) are reported with their exact logical strength and never as "evidence that settles" the conjectures; every imported object is flagged as imported at each point of use.
