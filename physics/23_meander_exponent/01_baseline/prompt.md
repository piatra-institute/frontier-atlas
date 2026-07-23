# PROMPT FOR THE MEANDER EXPONENT AND THE MEANDRIC GROWTH CONSTANT

## Meandric numbers: rigorous asymptotics against the Di Francesco–Golinelli–Guitter prediction $\alpha=(29+\sqrt{145})/12$, certified enumeration, and bounds on the growth rate

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 23 of 50 (Tier 2)
**Source:** top-50 list #33, category D (nonequilibrium and stochastic / physics-method combinatorics)
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The meandric number $M_n$ counts closed self-avoiding loops crossing an infinite line at exactly $2n$ points, up to homeomorphism of the plane - equivalently, pairs of noncrossing perfect matchings of $2n$ points whose union is a single cycle. Di Francesco, Golinelli and Guitter (~2000) predicted, via a two-flavor fully packed loop model coupled to two-dimensional quantum gravity through the KPZ relation, the asymptotic form $M_n\sim C\,R^{2n}n^{-\alpha}$ with the striking irrational exponent $\alpha=(29+\sqrt{145})/12\approx3.42013$.

Nothing here is rigorous: not the exponent, not the power-law form, not even the value of the growth constant $R\approx3.50$ - only crude rigorous bounds exist (Albert–Paterson lineage - verify). Meanders are matched to current AI methods because the enumeration is a clean transfer-matrix problem in exact integer arithmetic, growth-rate bounds reduce to certifiable finite computations, and the D-finiteness question is attackable through exact rank certificates on the known series.

The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Objects and conventions

- A *closed meander* of order $n$: a closed curve in the plane, transverse to a fixed oriented line $\ell$, meeting $\ell$ in exactly $2n$ points, considered up to orientation-preserving homeomorphisms of the plane fixing $\ell$ setwise.
- Working definition (adopted): an *arch pair* $(U,L)$, where $U$ and $L$ are noncrossing perfect matchings ("arch systems") of $\{1,\dots,2n\}$ drawn above and below $\ell$ respectively, such that $U\cup L$ is a single cycle on $\{1,\dots,2n\}$. $M_n$ is the number of such pairs.
- Ground-truth initial values (to be re-derived in-session, not assumed):
\[
M_1=1,\;M_2=2,\;M_3=8,\;M_4=42,\;M_5=262,\;M_6=1828,\;M_7=13820,\;M_8=110954
\]
(OEIS A005315 - re-derive independently; continuation $M_9=933458$, $M_{10}=8152860$ - verify).
- Equivalent formulations, admissible as working coordinates:
  - *meandric permutations*: the permutation of $\{1,\dots,2n\}$ obtained by reading the loop's visit order along $\ell$; the single-cycle condition becomes a condition on the product of the two matching involutions;
  - pairs of complete arch systems in the Temperley–Lieb diagram algebra $TL_{2n}$, with $M_n$ the number of pairs whose closure has exactly one loop.
- Trivially $M_n\le C_n^2$ ($C_n$ = Catalan), so $\limsup M_n^{1/n}\le16$.
- Concatenation gives supermultiplicativity $M_{m+n}\ge M_mM_n$ (prove the splice as a first exercise; attribution of the existence argument: folklore / Lando–Zvonkin ~1993 - verify). By Fekete,
\[
\rho:=\lim_{n\to\infty}M_n^{1/n}=R^2\ \text{exists},\qquad R:=\rho^{1/2}.
\]
- Numerically $R^2\approx12.26$, $R\approx3.502$ (Jensen; Jensen–Guttmann ~2000 - verify values and error bars).

### 1.2 The conjecture (Di Francesco–Golinelli–Guitter ~2000)

With central charge $c=-4$ (two fully packed loop flavors), the KPZ/string-susceptibility dressing
\[
\gamma=\frac{c-1-\sqrt{(1-c)(25-c)}}{12}=\frac{-5-\sqrt{145}}{12}
\]
yields the configuration-exponent prediction
\[
M_n\;\sim\;C\,\frac{R^{2n}}{n^{\alpha}},\qquad\alpha\;=\;2-\gamma\;=\;\frac{29+\sqrt{145}}{12}.
\]
A companion prediction exists for semi-meanders (one free end; OEIS A000682) - verify the exact conjectured value before using it, and never transplant the closed-meander exponent to semi-meanders or vice versa.

### 1.3 Open questions, in decreasing strength

1. Prove or refute $M_n=C\,R^{2n}n^{-\alpha}(1+o(1))$ with $\alpha=(29+\sqrt{145})/12$.
2. Prove the power-law form itself: existence of $\alpha:=\lim_n\big(2n\log R-\log M_n\big)/\log n$, any value.
3. Determine $R$ exactly, or improve the rigorous interval for $R^2$.
4. Decide whether $\mathcal M(t)=\sum_nM_nt^n$ is D-finite. Conjecturally it is **not**. Note: irrationality of $\alpha$ alone does not decide this - indicial exponents of D-finite equations need only be algebraic, and $(29+\sqrt{145})/12$ is a quadratic irrational. Any impossibility argument must do real work.

## 2. Complete-resolution standard

Complete resolution means a proof of question 1 - both the asymptotic form and the exponent value, including existence of all limits involved - or a refutation identifying the true asymptotic behavior to the same standard. Partial closure of questions 2–4 counts under section 3, not as resolution.

**Not accepted as resolution:**

- Numerical exponent estimates from differential approximants or ratio methods, at any precision, including new ones produced in-session.
- Rederivations of the DGG prediction through KPZ/Liouville heuristics, matrix models, or conformal field theory, however carefully done.
- Results conditional on unproven conjectures (e.g. convergence of the meandric permuton to a specific LQG/SLE object) presented as unconditional; conditional theorems are valuable partials and must be labeled conditional.
- Bounds on $R$ or on subexponential factors presented as determinations.
- Semi-meander results presented as closed-meander results, or vice versa.
- A "non-D-finiteness proof" that only exhibits failure of guessing on finitely many terms - that is a finite rank certificate (target P3), not a theorem about $\mathcal M$.

## 3. Graded partial-result targets

**P1 - certified enumeration with our own toolchain.**
Reimplement the arch-configuration transfer matrix (Jensen ~2000 lineage) with exact big-integer arithmetic; re-derive $M_n$ for all published $n$ (record: $n=24$ - verify) with a second, independent implementation: brute force over matching pairs with single-cycle check for $n\le10$, plus an independent recomputation at larger $n$.
*Certificate:* full integer table, dual-implementation agreement, SHA-256 manifest.

**P2 - frontier extension.**
Extend beyond the published record if memory allows. Honest feasibility: the state space (pairs of open-arch boundary states with connectivity tracking) grows exponentially; Jensen's $n=24$ consumed large 2000-era resources; a modern 256–512 GB workstation plausibly reaches $n=25$–$28$. Treat as a stretch goal and report the exact wall.
*Certificate:* new terms; resource log; independent internal-consistency checks (supermultiplicativity, parity, cross-section identities).

**P3 - finite non-D-finiteness certificates.**
Exact statement: "no P-recurrence with order $\le r$ and coefficient degree $\le d$, for all $(r,d)$ with $(r+1)(d+1)\le B$, is satisfied by $(M_n)_{n\le N}$," via certified nullspace-empty computations over $\mathbb Q$ (ore_algebra guessing, then exact rank re-verification in FLINT). A found recurrence would be sensational and must be tested predictively on held-out terms before any claim.
*Certificate:* exact rank computations, reproducible from the manifest.

**P4 - rigorous bounds on $R^2$.**
Reproduce the best published rigorous interval (Albert–Paterson ~2005; roughly $11.38\le R^2\le12.90$ - verify statement and numbers) with certified arithmetic; then improve both ends:
- upper bounds via certified Perron-root bounds on truncated/quotiented transfer operators (exact rational vector $v>0$ with $vA\le\lambda v$), with the domination argument proven, not assumed;
- lower bounds via Fekete applied to the largest exactly enumerated blocks ($R^2\ge M_k^{1/k}$ - compute the floor $M_{24}^{1/24}$ explicitly) and via concatenable positive-density subfamilies.
Any certified improvement of either end is publishable.
*Certificate:* the inequality chain and Perron certificates in $\mathbb Q$, plus an independent checker.

**P5 - structure theorems.**
Rigorous qualitative results: log-convexity/log-concavity statements for $(M_n)$ (test on data first; prove only what the data supports); subexponential-factor bounds $cR^{2n}n^{-A}\le M_n\le CR^{2n}n^{-a}$ with explicit $A,a$ bracketing the conjectured $\alpha$; or exclusion of specific asymptotic forms. The exact Temperley–Lieb Gram-determinant structure (Di Francesco ~1996–1997 meander determinants) is admissible input when used rigorously.
*Certificate:* proofs plus exact-arithmetic verification of every computational step.

**P6 - strongest short of resolution.**
One of: existence of the power-law exponent (question 2) in any rigorous formulation (e.g. regular variation of $M_nR^{-2n}$); a genuine non-D-finiteness theorem for $\mathcal M(t)$; or an unconditional theorem transferring one piece of the KPZ dictionary to meanders - the meandric-permuton program (Borga–Gwynne–Sun ~2022–2023) is the current route (verify status), noting in any writeup that permuton convergence does not by itself yield $\alpha$.

Honest calibration: full resolution is far beyond current technology - the exponent sits on the KPZ relation at $c=-4$, where no rigorous LQG dictionary exists. P1–P4 are realistic; P5–P6 are stretch.

## 4. Known results and prior art

- Origins and enumeration history: Touchard 1950; Lando–Zvonkin ~1992–1993 (growth-rate framework - verify).
- Di Francesco–Golinelli–Guitter 1995–1997: meander polynomials; Temperley–Lieb Gram-determinant evaluations (~1996–1997).
- The exponent prediction: Di Francesco–Golinelli–Guitter ~1999–2000 ("exact meander asymptotics" line of papers - verify titles/venues): $\alpha=(29+\sqrt{145})/12$ for closed meanders, companion semi-meander predictions (verify values).
- Numerical support: Jensen ~2000; Jensen–Guttmann ~2000 - transfer-matrix enumeration to $n=24$ and estimates $R^2\approx12.26$ (verify).
- Rigorous bounds: Albert–Paterson ~2005 on the meandric growth rate (verify exact interval; earlier related bounds by the same authors in the 1990s for stamp-folding/meander quantities).
- Adjacent rigorous structure: Temperley–Lieb Gram determinants (Di Francesco ~1997; related determinants Ko–Smolinsky 1991 - verify); meanders as intersections of two Catalan structures.
- KPZ side: Duplantier–Sheffield 2011 (rigorous KPZ relation in Liouville quantum gravity); Borga–Gwynne–Sun ~2022–2023: the meandric permuton and its conjectural LQG/SLE description, with partial rigorous results (verify precise statements). No rigorous consequence for $\alpha$ is known.
- D-finiteness: no proof either way; the series shows no small recurrence (community folklore from guessing on 24 terms - re-derive in-session rather than cite).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

### 5.1 Enumeration engine

- C++ transfer matrix scanning the line left to right; states = pairs (upper, lower) of open-arch configurations with the pairing/connectivity data needed to enforce the single-cycle condition at closure; counts in GMP integers; canonical state encodings with hashing.
- Memory is the binding constraint; measure and report the empirical state-count growth.
- Independent implementation: Python/SageMath brute force over pairs of noncrossing matchings with cycle check for $n\le10$ ($C_{10}^2\approx2.7\times10^8$ pairs - prune by early cycle-closure detection).
- Expected failure modes: connectivity-bookkeeping bugs (the single-cycle constraint is exactly where independent implementations disagree - the $n\le10$ brute force is the arbiter); silent overflow (excluded by GMP throughout).

### 5.2 Series analysis (exploration only)

- mpmath differential approximants for $\alpha$ and $R^2$ estimates with stated uncertainties.
- Clearly labeled nonrigorous; used to sanity-check the P4 interval, never cited as results.

### 5.3 Bound certificates

- Upper: build an exact truncated transfer operator on a finite state class provably dominating meander growth (the monotone-embedding lemma must be proven); certify its Perron root from above by an exact positive vector $v$ with $vA\le\lambda v$; FLINT rationals.
- Lower: Fekete floors from exact $M_k$; renewal improvements if a provable irreducible-component decomposition is found.
- All certificates re-checkable in minutes by an independent rational-arithmetic checker.

### 5.4 D-finiteness sweeps

- ore_algebra (SageMath) guessing sweeps over the full $(r,d)$ box; convert every failed sweep into the exact P3 rank statement via FLINT `fmpq_mat` rank.

### 5.5 Workstation budget

- Everything except the P2 stretch fits in 64 GB.
- P2 wants 256–512 GB and weeks; plan checkpointing and partial-result flushes from the start.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All $M_n$, all bound certificates, and all rank computations in exact integers/rationals; floating point confined to labeled exploratory series analysis (section 5.2).
2. **Independent verification.** Dual enumeration implementations with the brute-force arbiter at $n\le10$; Perron certificates verified by an independent checker that only multiplies and compares rationals; rank certificates re-run in a second CAS.
3. **Reproducibility.** State-encoding documentation sufficient to reimplement from the report alone; all parameters, versions, and memory/time logs recorded; SHA-256 manifest over tables, certificates, and source.
4. **Preservation.** Transfer-matrix source, brute-force source, failed bound constructions, and all guessing logs are part of the record; anything unpreserved must be declared as such.
5. **Honest reporting.** The final report states first that the DGG exponent remains unproven (unless question 1 was actually resolved); estimates are labeled estimates; conditional and family-restricted results are labeled as such; and no bound, certificate, or series extension is represented as a determination of $R$ or $\alpha$.
