# PROMPT FOR THE EXACT QUANTUM QUERY COMPLEXITY OF A SPECIFIC FUNCTION

## Certified value of \(Q(f)\) via the general adversary bound computed as an SDP with exact rounding

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 42 of 50
**Area:** quantum computation & codes
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The quantum query (decision-tree) model measures how many oracle queries a quantum algorithm needs to compute a function \(f\) - the setting of Grover, Deutsch–Jozsa, and the polynomial and adversary lower-bound methods. A landmark result makes the model unusually tractable: the **general (negative-weight) adversary bound** \(\mathrm{ADV}^\pm(f)\) characterizes the bounded-error quantum query complexity \(Q(f)\) up to a constant factor, and \(\mathrm{ADV}^\pm(f)\) is itself the optimum of a **semidefinite program**. So for a specific small function, \(Q(f)\) (up to constants) is computable - and the tightness of the polynomial method or the positive-weight adversary against it is checkable - by solving an SDP. The task is to compute the general adversary value of a specific function exactly and to pin down \(Q(f)\) as tightly as the theory allows, with a certificate. The catch is that "compute an SDP" is not automatically rigorous: a floating-point interior-point optimum is not a proof. The verifier that closes the loop is exact: an SDP optimum certified by a **primal-dual pair rounded to exact rationals** whose feasibility and objective are checked in exact arithmetic, together with matching feasible witnesses (a valid adversary matrix for the lower bound, a dual/algorithmic witness for the upper bound). This is kept distinct from the query-**separation** problem: here the object of interest is the **exact value** of \(Q\) (or \(\mathrm{ADV}^\pm\), or \(Q_E\)) for a named function, not a gap between two measures. Anything short of the section-2 standard - a floating-point SDP value, an asymptotic bound where an exact value is asked, an unverified solver output - is a partial result, never a solution.

## 1. Exact problem statement

A function \(f : D \to \{0,1\}\) with \(D \subseteq \{0,1\}^N\) (or \(\Sigma^N\)) is computed with **bounded error** by a quantum query algorithm making queries to the oracle

\[
O_x : |i\rangle|b\rangle \;\mapsto\; |i\rangle|b \oplus x_i\rangle .
\]

Then \(Q(f)\) (also \(Q_2(f)\)) is the minimum number of queries to output \(f(x)\) with error \(\le 1/3\) for all \(x \in D\); formally, over query algorithms \(\mathcal{A}\) making \(t\) oracle calls,

\[
Q(f) \;=\; \min\Big\{\, t \;:\; \exists\,\mathcal{A}_t\ \text{with}\ \Pr[\mathcal{A}_t(x) = f(x)] \ge \tfrac{2}{3}\ \forall x \in D \,\Big\}.
\]

The **exact** version \(Q_E(f)\) demands zero error (\(\Pr = 1\)).

**Adversary matrices.** For a symmetric matrix \(\Gamma\) indexed by inputs, with \(\Gamma[x,y] = 0\) whenever \(f(x) = f(y)\), let \(\Gamma_i\) be \(\Gamma\) with entries zeroed unless \(x_i \ne y_i\). The **general (negative-weight) adversary bound** is

\[
\mathrm{ADV}^\pm(f) \;=\; \max_{\Gamma \ne 0}\ \frac{\|\Gamma\|}{\max_i \|\Gamma_i\|},
\]

maximized over all symmetric \(\Gamma\) (entries of any sign) with the zero pattern above; the **positive-weight** bound \(\mathrm{ADV}(f)\) restricts to \(\Gamma \ge 0\). Both are SDPs. The characterization (Reichardt; Lee–Mittal–Reichardt–Špalek–Szegedy) states

\[
Q(f) \;=\; \Theta\!\big(\mathrm{ADV}^\pm(f)\big),
\]

so \(\mathrm{ADV}^\pm\) determines \(Q\) up to a universal constant; for total Boolean functions \(\mathrm{ADV}^\pm(f) \le Q(f) \le O(\mathrm{ADV}^\pm(f))\) with small explicit constants.

In semidefinite form the maximization is written, after normalizing \(\max_i \|\Gamma_i\| \le 1\),

\[
\mathrm{ADV}^\pm(f) \;=\; \max\ \|\Gamma\|
\quad\text{s.t.}\quad
\Gamma[x,y] = 0\ \text{when}\ f(x)=f(y),
\quad
\Big\| \textstyle\sum_{i:\, x_i \ne y_i}\!\Gamma[x,y]\, |x\rangle\langle y| \Big\| \le 1\ \ \forall i,
\]

which is a genuine SDP: its feasible set is spectrahedral and its optimum is attained at a rational (or low-degree algebraic) point whenever \(f\) is rational, so exact certification is possible in principle. The exact version \(Q_E(f)\) is bounded below by \(\mathrm{ADV}^\pm(f)\) as well and, for many small functions, equals a small integer determined by an explicit exact algorithm.

A second, independent lower-bound handle is the **polynomial method**: writing \(\widetilde{\deg}(f)\) for the least degree of a real polynomial approximating \(f\) to \(\pm 1/3\) on \(D\), and \(\deg(f)\) for the exact representing degree,

\[
Q(f) \;\ge\; \tfrac{1}{2}\,\widetilde{\deg}(f),
\qquad
Q_E(f) \;\ge\; \tfrac{1}{2}\,\deg(f),
\]

and \(\widetilde{\deg}(f)\) is itself the optimum of an exact LP over polynomial coefficients. Comparing \(\widetilde{\deg}\) with \(\mathrm{ADV}^\pm\) decides, per function, whether the polynomial method is tight.

The cost measures are the exact real number \(\mathrm{ADV}^\pm(f)\) (and \(\mathrm{ADV}(f)\)), and the integer / near-integer \(Q(f)\) or \(Q_E(f)\) it bounds. The function \(f\) is declared explicitly - a named small function: a specific 3–5 bit Boolean function, a graph property on few vertices, \(\mathrm{EXACT}_k\), \(\mathrm{THRESHOLD}\), or a small \(\mathrm{AND}\text{-}\mathrm{OR}\) tree. The open problem, per function: **compute \(\mathrm{ADV}^\pm(f)\) exactly, thereby pinning \(Q(f)\) as tightly as the constants allow, and determine whether the polynomial method / positive adversary matches it.** Start from this prompt alone - the model, the oracle, and the adversary SDP are all fixed above.

## 2. Resolution standard

Fix a named function \(f\). Resolution is:

1. the **exact** value of \(\mathrm{ADV}^\pm(f)\) (a rational or algebraic number), certified by a primal-dual SDP pair; and

2. the resulting statement about \(Q(f)\) (or \(Q_E(f)\)) - either an exact value (when a matching algorithm and lower bound coincide) or the tightest interval the known constants permit - with each side certified.

**Named certified form.** One of:

- **SDP optimum with exact rounding.** An interior-point solve of the adversary SDP followed by **exact rationalization**: a feasible primal \(\Gamma\) (a valid adversary matrix, feasibility checked exactly) giving a lower bound, and a feasible dual giving a matching upper bound, both rounded to exact rationals whose feasibility and objective values are verified in exact arithmetic; the two objectives equal (or bracket the exact optimum with a proven zero gap after rounding).

- **Exact algebraic optimum (small \(f\)).** For a small function, the SDP optimum computed symbolically (the optimal \(\Gamma\) and its spectral norm as algebraic numbers) with all steps exact.

- **Matching algorithm + lower bound (for \(Q\) or \(Q_E\)).** An explicit query algorithm attaining \(t\) queries (verified) together with a certified lower bound of \(t\) (from the adversary SDP or the polynomial method), giving the exact integer.

**Not accepted as resolution.**

- A **floating-point** SDP optimum reported as the exact value with no exact primal-dual rounding.

- A lower bound from a **hand-chosen** \(\Gamma\) presented as \(\mathrm{ADV}^\pm\) without a matching dual (a valid lower bound, not the optimum).

- An **asymptotic** \(\Theta(\cdot)\) statement where an exact value or exact constant is asked.

- An **unverified** solver run (no exact feasibility check of the rounded certificate).

- Conflating \(Q\), \(Q_E\), \(\mathrm{ADV}\), and \(\mathrm{ADV}^\pm\), or dropping the error model.

- A query **separation** result (which belongs to the separations track) dressed up as an exact-value result.

## 3. Graded partial-result targets

- **P1 - Reproduce textbook values.** Certify \(\mathrm{ADV}^\pm\) and \(Q\) for functions with known exact answers (\(\mathrm{OR}_N\): \(\mathrm{ADV}^\pm = \sqrt N\); small parity; small threshold) via the SDP with exact rounding. Certificate: exact primal-dual pair matching the known value.

- **P2 - Exact SDP-with-rounding pipeline.** Build the adversary SDP generator and an exact-rationalization / verification step; validate on P1. Certificate: exact feasibility + objective checks, second-solver agreement.

- **P3 - A specific small function, exact \(\mathrm{ADV}^\pm\).** Compute the exact general adversary value of a named 3–5 bit function not tabulated, with a certified primal-dual pair. Certificate: exact primal and dual, equal objectives.

- **P4 - Tightness of the polynomial method.** For a chosen small \(f\), compute the exact approximate / exact polynomial degree and compare to \(\mathrm{ADV}^\pm(f)\), certifying whether they match (both exactly). Certificate: exact degree LP/SDP + exact adversary value.

- **P5 - A new exact \(Q\) or \(Q_E\).** Pin the exact integer \(Q(f)\) or \(Q_E(f)\) for a named small function via a matching certified algorithm and lower bound, or narrow a published interval. Certificate: verified algorithm + certified lower bound, full manifest.

- **P6 - Reusable exact-adversary harness.** An audited tool that, given \(f\)'s truth table, builds and solves the adversary SDP and emits an exact primal-dual certificate, validated against P1. Certificate: source + agreement with a second SDP backend on shared instances.

## 4. Known results and prior art

- **Adversary method.** Ambainis, *Quantum lower bounds by quantum arguments* (2000) - the positive-weight adversary; Høyer, Lee, Špalek, *Negative weights make adversaries stronger*, STOC (2007) - the general (negative-weight) adversary.

- **Characterization.** Reichardt, *Span programs and quantum query complexity: the general adversary bound is nearly tight for every Boolean function*, FOCS (2009) (arXiv 0904.2759) - \(Q(f) = \Theta(\mathrm{ADV}^\pm(f))\); Lee, Mittal, Reichardt, Špalek, Szegedy, *Quantum query complexity of state conversion* (2011) - extension to non-Boolean / state conversion; the adversary bound as an SDP with composition properties.

- **Polynomial method.** Beals, Buhrman, Cleve, Mosca, de Wolf, *Quantum lower bounds by polynomials*, JACM (2001) - \(Q(f) \ge \deg_{1/3}(f)/2\); the method and its (in)tightness vs the adversary.

- **Exact quantum query.** Montanaro, Jozsa, Mitchison and others on \(Q_E\) of small functions; Ambainis and collaborators on exact quantum algorithms beating classical (~2013–2016, verify).

- **SDP practice.** The adversary bound is routinely computed numerically for small functions; exact / rational certification is the gap this prompt targets.

Status as of mid-2026 - re-verify against the current literature before starting any session.

## 5. Attack plan

`[search]`. One workstation.

1. **SDP generator.** From \(f\)'s truth table build the adversary SDP: the variable matrix \(\Gamma\) with the enforced zero pattern, objective \(\|\Gamma\|\) normalized by \(\max_i \|\Gamma_i\|\) (in the standard SDP formulation with the \(\Gamma_i\) constraints). Exploit the automorphism group of \(f\) to symmetry-reduce (block-diagonalize) the SDP - essential for exact certification.

2. **Numerical solve, then rationalize.** Solve with an interior-point SDP solver (SDPA, MOSEK-if-available, SCS) for a candidate optimum; then round the primal \(\Gamma\) and the dual to exact rationals near the numeric optimum and check feasibility and objectives in exact arithmetic (SageMath / FLINT). The exact primal gives a certified lower bound, the exact dual a certified upper bound.

3. **Symbolic optimum for tiny \(f\).** For very small functions, solve the (symmetry-reduced) SDP symbolically so the optimum is an exact algebraic number.

4. **Polynomial-method side.** Compute \(\widetilde{\deg}(f)\) and \(\deg(f)\) via an exact LP/SDP for approximate degree; compare to \(\mathrm{ADV}^\pm\) for tightness (P4).

5. **Upper bounds for \(Q\) / \(Q_E\).** Construct explicit small query algorithms (span-program / dual-adversary-derived, or ad hoc) and verify their query count and correctness exactly.

6. **Failure modes.** The SDP grows fast with the input count \(|D|\), so exact certification needs aggressive symmetry reduction; naive rounding of a near-degenerate optimum can be infeasible (re-solve or perturb toward strict feasibility); the \(\Theta\) constant means \(\mathrm{ADV}^\pm\) pins \(Q\) only up to constants unless a matching algorithm is built; conflating error models. Declare \(Q\) vs \(Q_E\) vs \(\mathrm{ADV}^\pm\) in every claim.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** SDP optima are certified by exact-rational (or algebraic) primal-dual pairs whose feasibility and objective are checked in exact arithmetic; algorithm query counts and correctness are verified exactly. Floating point is used only to locate the optimum before rationalization.

2. **Independent verification.** A standalone checker, separate from the solver, that (a) verifies the rounded primal \(\Gamma\) satisfies the adversary constraints and computes its objective exactly, and (b) verifies the dual and that the objectives match. A second SDP backend for the numeric stage.

3. **Reproducibility.** Every truth table, SDP data file, symmetry reduction, solver name+version, and rounding decision recorded; SHA-256 manifest over instances, certificates, and any algorithms; any baseline value matched or improved cited with source and access date.

4. **Preservation.** All generator, solver-driver, rounding, and checker source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).

5. **Honest reporting.** The report states up front, per function, whether \(\mathrm{ADV}^\pm\) was certified exactly, what that implies for \(Q\) / \(Q_E\) (an exact value or an interval, with the constants named), whether the polynomial method was shown (non)tight, and whether any published value was improved - never presenting a floating-point SDP value as exact, and never blurring the line with the separations track.
