# PROMPT FOR CLOSED-FORM LYAPUNOV EXPONENTS OF RANDOM MATRIX PRODUCTS

## Viswanath's random Fibonacci constant, Anderson band-center anomalies, and the exactly solvable catalogue

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 22 of 50 (Tier 2)
**Source:** top-50 list #34, category D (stochastic)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Furstenberg theory guarantees that i.i.d. products of random matrices have a well-defined top Lyapunov exponent, positive under mild irreducibility hypotheses - yet exact values are almost never known. The flagship embarrassment is Viswanath's constant $1.13198824\ldots$, the almost-sure growth rate of random Fibonacci sequences, computed in 1999 through the Stern–Brocot structure of the stationary measure and still without a closed form; the same gap runs through 1D Anderson localization lengths (where the Kappus–Wegner band-center anomaly shows exact structure exists) and Bernoulli matrix products. The problem is matched to current AI methods because progress decomposes into certified computation and symbolic identity-hunting: interval Stern–Brocot pipelines, Pollicott-determinant methods with rigorous truncation error, systematic re-derivation and extension of the exactly solvable catalogue via invariant-measure ansätze and Dufresne-type integral identities, and disciplined PSLQ mining. The complete resolution defined in section 2 is the target; full resolution for the flagship constant is unlikely, and the graded targets of section 3 are the intended product. Anything less must be reported as a partial result, never as a solution.

## 1. Exact problem statement

### 1.1 Lyapunov exponents of i.i.d. matrix products

Let $\mu$ be a probability measure on $\mathrm{GL}_d(\mathbb{R})$ with $\int \log^+ \|A\|\, d\mu(A) < \infty$, and let $A_1, A_2, \ldots$ be i.i.d. with law $\mu$. The top Lyapunov exponent

\[
\lambda_1(\mu) \;=\; \lim_{n \to \infty} \frac{1}{n}\, \mathbb{E}\, \log \| A_n \cdots A_1 \|
\]

exists (Furstenberg–Kesten 1960) and equals the almost-sure limit of $\frac1n \log \|A_n \cdots A_1\|$. Furstenberg's formula expresses it against a stationary measure $\nu$ of the induced projective action:

\[
\lambda_1(\mu) \;=\; \int_{\mathrm{GL}_d} \int_{\mathbb{P}^{d-1}} \log \frac{\|A v\|}{\|v\|}\; d\nu(\bar v)\, d\mu(A).
\]

Positivity holds under non-compactness and strong irreducibility (Furstenberg 1963). The obstruction to exact evaluation is always the same: $\nu$ is not available in closed form.

### 1.2 Flagship instances (fixed normalizations)

1. **Random Fibonacci (Viswanath).** $t_1 = t_2 = 1$, $t_{n+1} = \pm t_n + t_{n-1}$ with i.i.d. fair signs; equivalently $d = 2$, $\mu = \frac12(\delta_{A_+} + \delta_{A_-})$ with

\[
A_\pm = \begin{pmatrix} \pm 1 & 1 \\ 1 & 0 \end{pmatrix}.
\]

Viswanath (1999): $|t_n|^{1/n} \to \sigma_V = 1.13198824\ldots$ almost surely; $\lambda_1 = \log \sigma_V$. No closed form known.

2. **1D Anderson at band center.** Transfer matrices

\[
T_n = \begin{pmatrix} E - V_n & -1 \\ 1 & 0 \end{pmatrix},
\]

$V_n$ i.i.d. with variance $\sigma^2$; $\gamma(E) = \lambda_1$. The naive weak-disorder formula $\gamma(E) \approx \sigma^2/(8 - 2E^2)$ fails at $E = 0$ (Kappus–Wegner 1981); the exact anomalous coefficient involves $\Gamma$-function values (Derrida–Gardner 1984). Exact perturbative structure exists even where no exact $\gamma$ does.

3. **Bernoulli $\mathrm{SL}_2$ products.** E.g. $\mu = \frac12(\delta_{B} + \delta_{B^{\top}})$ with $B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, and elliptic/hyperbolic Bernoulli mixtures: exponents positive, values unknown.

### 1.3 The adopted question

*Produce proven closed forms - explicit finite expressions over a declared class (elementary functions; $\Gamma$; hypergeometric and Bessel functions at algebraic arguments; evaluated one-dimensional integrals of elementary functions) - for the Lyapunov exponents of natural nontrivial instances, with the random Fibonacci constant $\log \sigma_V$ as the flagship; or prove that a flagship exponent lies in no such class; and systematically extend the rigorously solvable catalogue.*

## 2. Complete-resolution standard

Resolution of the flagship is either:

1. **Closed form for $\sigma_V$** (equivalently $\lambda_1$ of instance 1.2.1) over the declared class, with complete proof - the invariant measure identified exactly and Furstenberg's integral evaluated rigorously, or an equivalent route (thermodynamic determinant with exactly located zero, exactly summed cycle expansion) - plus certified numerical concordance of the closed form with a certified enclosure of $\sigma_V$ to margin far beyond coincidence.
2. **Class-nonexistence theorem:** a proof that $\log \sigma_V$ (or $\sigma_V$) does not belong to a precisely defined infinite closed-form class.

An equally canonical instance (Anderson band-center $\gamma(0)$ for a standard disorder law; symmetric Bernoulli $\mathrm{SL}_2$ families) may substitute for the flagship if its canonicity is argued explicitly in the report.

**Not accepted as resolution**

- Numerical values of any precision, certified or not.
- Formal invariant-measure ansätze whose stationarity is checked only numerically, or termwise without a convergence proof.
- Closed forms for *reducible* families - triangular, commuting, normal, or scalar-multiple matrices, or any case where the projective action has a finite invariant set - presented as answering the flagship question.
- Weak-disorder or other asymptotic series presented as exact values.
- Restatements of Furstenberg's integral with an unevaluated stationary measure ("closed form up to $\nu$").
- Moment exponents $\lim \frac1n \log \mathbb{E}\|A_n \cdots A_1\|$ - computable via the spectral radius of a finite-dimensional or transfer operator and sometimes algebraic - conflated with the almost-sure exponent $\lambda_1$. This confusion is endemic in the literature; the two differ already for random Fibonacci. Flag it everywhere.

## 3. Graded partial-result targets

- **P1 - Certified recomputation of Viswanath's constant, two independent methods.**
  - *Task (a):* interval Stern–Brocot pipeline - rigorous enclosure of the stationary measure on Stern–Brocot intervals to depth $N$, a proved geometric tail bound, directed rounding throughout.
  - *Task (b):* Pollicott-style Fredholm-determinant/cycle expansion for the two-map projective system, with rigorous truncation error, coefficients in Arb ball arithmetic.
  - *Certificate:* two independently produced enclosures that agree; standalone checkers for both; any digit-level discrepancy is a stop-the-line event.
  - *Value:* certified tens of digits - beating the original eight - and a validated substrate for P5. Re-verify the current published precision record first (post-1999 improvements have been claimed; verify).
- **P2 - Certified Anderson band-center package.**
  - *Task:* symbolic re-derivation, with proof, of the Kappus–Wegner/Derrida–Gardner band-center anomaly coefficient for a declared disorder law; cross-check via a certified numerical $\gamma(0)$ at small $\sigma$ (interval transfer-operator or certified quadrature of the stationary density where one exists).
  - *Certificate:* the symbolic derivation script re-run in a second CAS; interval numerics with checker.
  - *Value:* welds the exact-perturbative corner of the field to a certified numerical baseline.
- **P3 - The solvable catalogue, consolidated and certified.**
  - *Task:* machine-verified re-derivations of the known exact cases: Cohen–Newman Gaussian ensembles; Forrester-type Ginibre-product formulas; Marklof–Tourigny–Wolowski explicit invariant measures; the Comtet–Texier–Tourigny 1D-disorder solvable family; Chassaing–Letac–Mora-type examples (verify each attribution).
  - *Certificate:* per-entry proof scripts (SageMath/Mathematica) plus certified numerical concordance to $\ge 50$ digits.
  - *Value:* the catalogue is currently scattered across three decades at uneven rigor; expect to find and document gaps - each documented gap is a result.
- **P4 - New certified-solvable families.**
  - *Task:* engineer measures $\mu$ whose projective stationary measure lies in a closed family: Möbius-stable densities, hypergeometric ansätze, and Dufresne-type identities for exponential functionals (the continuous-disorder route of Comtet–Texier–Tourigny) pushed to new discrete or matrix instances.
  - *Certificate:* stationarity proven symbolically; positivity/irreducibility hypotheses checked; closed form vs certified numerics concordance.
  - *Value:* even one genuinely new family - irreducible, non-compact, proven closed-form $\lambda_1$ - is a publishable extension of the catalogue.
- **P5 - Pre-registered relation mining on flagship digits.**
  - *Task:* PSLQ/LLL on certified digits of $\log \sigma_V$, $\sigma_V$, and Anderson band-center constants from P1/P2, against a pre-registered basis ($\log$s of algebraic numbers, $\pi$, $\Gamma$-values at rationals, $\zeta$ values, golden-ratio combinations - the plausible suspects given the Stern–Brocot structure), with declared budgets and multiple-testing discipline.
  - *Certificate:* mining logs; exclusion certificates (norm lower bounds for any integer relation) for all negatives.
  - *Value:* converts folklore "no known closed form" into bounded, citable exclusion statements.
- **P6 - Flagship theorem.**
  - *Task:* closed form or defined-class exclusion for $\sigma_V$, or for band-center $\gamma(0)$ - the section 2 standard.
  - *Certificate:* complete proof plus concordance check.
  - *Value:* strongest target; not expected in-session, and the report must not pretend otherwise.

## 4. Known results and prior art

- Furstenberg–Kesten (1960); Furstenberg (1963): existence, positivity, the projective-measure formula. Bougerol–Lacroix (1985): the standard monograph.
- Viswanath (1999/2000, Math. Comp.): $\sigma_V = 1.13198824\ldots$ via the Stern–Brocot decomposition of the stationary measure, with rigorous floating-point error analysis. Subsequent precision improvements and error-analysis refinements: verify the current record before P1.
- Embree–Trefethen (1999): growth/decay transition for generalized random Fibonacci $t_{n+1} = \pm \beta t_n + t_{n-1}$. Janvresse–Rittaud–de la Rue (~2008–2010): rigorous growth rates for biased random Fibonacci via continued-fraction/measure techniques (verify the exact scope of their formulas).
- Pollicott (2010, Inventiones): superexponentially convergent determinant algorithm for $\lambda_1$ of positive-matrix products with computable error bounds - the backbone of P1(b); refinements by Jurga–Morris and others (verify).
- Anderson 1D: Thouless formula; Kappus–Wegner (1981): band-center anomaly; Derrida–Gardner (1984): exact anomalous coefficients ($\Gamma$-value expressions - verify the constant before re-deriving); Comtet–Texier–Tourigny (2010s, incl. a J. Phys. A review ~2013): solvable continuous-disorder models via exponential functionals and Dufresne (1990) identities; Sadel–Schulz-Baldes school for perturbative exponents (verify).
- Exact ensembles: Cohen–Newman (1984, Ann. Probab.): exact $\lambda_1$ for i.i.d. Gaussian-entry matrices; Newman (1986); Forrester (~2013): exact Lyapunov spectra for products of complex Ginibre matrices; Akemann–Burda–Kieburg product-ensemble exact results (2010s); Marklof–Tourigny–Wolowski (~2008, Trans. AMS): explicit invariant measures for classes of random Möbius products; Chassaing–Letac–Mora (1984): early explicit examples (verify).
- Arithmetic nature: no closed form and no irrationality/transcendence result is known for $\sigma_V$ (verify - a literature surprise here would re-scope the session).

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

All under `[sym]`, with certified numerics as substrate.

1. **Stern–Brocot pipeline (P1a).** Implement Viswanath's measure recursion on the Stern–Brocot tree in interval arithmetic (C++ with directed rounding or the kv library; MPFR intervals at depth): enclose the measure of each depth-$N$ interval, sum the $\log$-norm integrand against interval bounds, and control the tail by the proved geometric contraction of branch measures. Depth cost is $O(2^N)$ with pruning; expect roughly 10–15 digits at workstation scale from this method alone - its role is ground truth for (b).
2. **Determinant pipeline (P1b).** Cast $\lambda_1$ as the derivative of the pressure (leading eigenvalue) of a weighted transfer operator for the two projective Möbius maps; compute via Pollicott's determinant truncations with explicit nuclear-norm tail bounds, all coefficients in Arb. Superexponential convergence should deliver 30+ certified digits cheaply *if* the contraction hypotheses can be verified on an explicit disk. Verifying them for the random Fibonacci pair - one map is not a uniform contraction on the natural domain - is a genuine subtask: induce/accelerate and document the domain surgery, since the tail bounds must follow it.
3. **Symbolic layer (P2–P4).** SageMath/Mathematica for stationary-density ansätze (solve the stationarity integral equation within hypergeometric families), Dufresne-identity manipulation, and Mellin-transform bookkeeping; every candidate identity numerically screened at 50+ certified digits before proof investment. Singular/Macaulay2 only where algebraic-measure ansätze reduce to polynomial systems.
4. **Mining (P5).** PARI/GP `lindep` and fplll per the pre-registered protocol; every run logged.

**First computations (session day one).**

1. Float implementation of the Stern–Brocot recursion to depth 25; reproduce Viswanath's $1.13198824$ (sanity gate for the encoding).
2. Interval version at depth 20 with the proved tail bound; confirm the certified enclosure contains the float value.
3. Pollicott-determinant prototype in floats for a *known-hyperbolic* toy pair first (uniform contractions), then attempt the random Fibonacci pair and document exactly where uniform contraction fails - this failure map drives the P1b domain surgery.
4. Symbolic re-derivation of one easy catalogue entry (Cohen–Newman $2\times 2$ Gaussian case) end-to-end with a 50-digit concordance check.

**Workstation feasibility.**

- P1a to depth ~40 with pruning: days. P1b: hours once the operator domain is validated.
- P2–P4: symbolic-labor-bound, not compute-bound. Everything fits on one workstation.

**Expected failure modes.**

- The random Fibonacci stationary measure is singular (fractal-supported): density-based ansätze fail structurally - work with measures, not densities, in P1a; this is also why naive quadrature lies.
- Transfer-operator certification fails on the natural projective domain (non-uniform contraction); requires induced/accelerated maps, with tail bounds re-derived after the surgery, not inherited.
- Moment exponents masquerading as $\lambda_1$ (section 2): keep the distinction in every artifact and table.
- Literature "exact" results at physics rigor that do not survive re-derivation: document the gap rather than silently repairing it - the documentation is a deliverable.
- PSLQ false positives against $\Gamma$-rich bases with too few digits; enforce the $2\times$ margin rule and higher-precision re-tests.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Every claimed digit of every constant from interval/ball arithmetic with directed rounding; symbolic identities verified by exact simplification or resultant/Gröbner reduction, never by float agreement alone.
2. **Independent verification.** Standalone checkers re-verifying (a) Stern–Brocot measure enclosures and tail bounds from stored tree data, and (b) determinant truncation errors from stored operator coefficients. Dual implementations (Python/mpmath-interval and C++/MPFR) for both. P3/P4 proof scripts re-run in a second CAS where feasible.
3. **Reproducibility.** Tree depths, operator domains, truncation orders, precisions, pre-registration timestamps for P5, tool versions (Arb/FLINT, kv, PARI, fplll, SageMath), and a SHA-256 manifest over enclosures, proof scripts, and mining logs.
4. **Preservation.** All pipeline code; failed ansätze and failed domain choices (scientifically informative); the complete mining log including negatives. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report opens by stating whether any section 2 standard was met (expected: no). Every catalogue entry carries its hypotheses and rigor level; every numerical value carries its certification status; the moment-exponent vs almost-sure-exponent distinction is restated wherever a value appears.
