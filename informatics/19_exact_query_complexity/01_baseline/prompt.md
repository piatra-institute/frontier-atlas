# PROMPT FOR EXACT RANDOMIZED AND QUANTUM QUERY COMPLEXITY OF SPECIFIC SMALL FUNCTIONS

## Certified exact \(R(f)\) and \(Q(f)\) via exact-rounded adversary/polynomial SDPs and exhaustive small-\(n\) search

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 19 of 50
**Area:** complexity & communication
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Separations ask for the *largest gaps*; this prompt asks for the complementary, and equally hard, object: the **exact value** of the randomized and quantum query complexity of *specific, named* functions - small symmetric functions, small cases of \(k\)-distinctness and element distinctness, thresholds, and specific total functions whose exact \(Q\) or \(R\) is not pinned. Exact query complexity is a well-posed optimization: the bounded-error quantum query complexity is characterized up to constants by the general adversary bound, itself a semidefinite program, and the exact adversary value can be certified by rounding an SDP optimum to an exact rational feasible point; the randomized complexity is a linear program over decision-tree distributions; both admit exhaustive computation at small \(n\). The certifiable product is a table of exact (or tightly two-sided-certified) \((R,Q)\) values for a curated list of functions, each with an SDP/LP certificate and a matching algorithm. The on-machine verifier is an exact SDP-feasibility checker plus a decision-tree/algorithm replayer. A floating-point SDP optimum, a heuristic algorithm without a matching lower bound, or an asymptotic estimate where an exact value is asked, is a partial result.

## 1. Exact problem statement

For \(f:\mathcal D\to\{0,1,\dots\}\) with \(\mathcal D\subseteq\Sigma^n\) (Boolean \(\Sigma=\{0,1\}\), or a larger alphabet for distinctness problems):

- **Bounded-error randomized query** \(R_\varepsilon(f)\): min over distributions on deterministic decision trees of worst-case expected number of queries, error \(\le\varepsilon\) on every input; default \(\varepsilon=1/3\).

- **Bounded-error quantum query** \(Q_\varepsilon(f)\): min queries of a quantum query algorithm with error \(\le\varepsilon\); default \(\varepsilon=1/3\). Also **exact quantum** \(Q_E(f)\) (zero error) where relevant.

- **General adversary bound** \(\mathrm{ADV}^\pm(f)\): the value of the standard adversary SDP, satisfying

\[
Q_{1/3}(f)=\Theta\!\big(\mathrm{ADV}^\pm(f)\big),\qquad
c_1\,\mathrm{ADV}^\pm(f)\ \le\ Q(f)\ \le\ c_2\,\mathrm{ADV}^\pm(f),
\]

with explicit constants \(c_1,c_2\) (Reichardt).

- **Approximate degree** \(\widetilde{\deg}_\varepsilon(f)\): min degree of a real polynomial \(\varepsilon\)-approximating \(f\), giving \(Q_\varepsilon(f)\ge\tfrac12\widetilde{\deg}_{2\varepsilon}(f)\).

The measures are ordered by

\[
\tfrac12\widetilde{\deg}(f)\ \le\ Q(f)\ \le\ Q_E(f),\qquad
Q(f)\ \le\ R(f)\ \le\ D(f)\ \le\ n,
\]

so an exact \(\widetilde{\deg}\) and an exact \(\mathrm{ADV}^\pm\) together bracket \(Q\) from both sides.

**Named target functions.**

1. **Symmetric** \(f:\{0,1\}^n\to\{0,1\}\) (value depends only on Hamming weight) for small \(n\): thresholds \(\mathrm{TH}_k\), exact-\(k\), parity, majority, `MOD`\(_m\).

2. **Element distinctness / \(k\)-distinctness** on small domains: input \(x\in[m]^n\), decide whether some value repeats \(k\) times; small \((n,m,k)\).

3. **Specific total Boolean functions** whose exact \(R\) or \(Q\) is unsettled (small pointer/gadget functions, sorting-type predicates).

**Adopted normalizations.** Cost is number of oracle queries; error \(1/3\) unless a function is studied at exact/zero error; complexities are integers where the model forces integrality (\(D\), \(Q_E\)) and certified rationals otherwise.

**Open questions (adopted here).** The exact values \(R_{1/3}(f)\) and \(Q_{1/3}(f)\) (and \(Q_E\) where natural) for each named function at each small size - most are known only up to constants or asymptotically (e.g. \(k\)-distinctness quantum complexity has matching bounds only for small \(k\) asymptotically; small-\(n\) exact values are unrecorded).

**Starting from the prompt alone.** Each function is defined by an explicit rule; a reader builds its truth table (or transition relation for larger alphabets), forms the adversary SDP and the randomized-tree LP, and reads off certified bounds - no external data required.

## 2. Resolution standard

An exact value is resolved when the lower and upper bounds meet in **certified form**:

- **Exact \(Q\):** an **exact-rounded general-adversary SDP** feasible point proving \(Q(f)\ge \ell\), together with an explicit quantum query algorithm (span program, or a construction from the SDP dual) using \(\le\ell\) queries with error \(\le1/3\) - the bracket closing at a certified value. Where only the adversary value is pinned exactly, report \(\mathrm{ADV}^\pm(f)\) exactly and the resulting constant-factor bracket on \(Q\).

- **Exact \(R\):** the exact **rational LP** optimum over decision-tree distributions (small \(n\)) - a primal distribution (upper) and a dual (lower) certifying the same value - or, at larger \(n\), a certified two-sided bracket (Yao-principle hard distribution + explicit randomized tree).

- **Approximate degree** where used: exact via an LP/SDP with rational rounding.

**Not accepted as resolution.**

- A **floating-point** SDP optimum reported as \(\mathrm{ADV}^\pm\) or \(Q\); the certificate must be an exact rational feasible point (primal for upper, dual for lower) checked by re-substitution.

- An algorithm (upper bound) with no matching lower bound, or vice versa - that is a bracket, not an exact value, and must be labelled a bracket.

- A heuristic randomized decision tree presented as \(R\) without the matching Yao/LP-dual lower bound.

- Asymptotic \(\Theta\)/\(\tilde O\) claims where an exact small-\(n\) value is requested.

- Using \(\mathrm{ADV}^\pm(f)\) as if it *equals* \(Q(f)\) (it is tight only up to a fixed constant); the constant must be tracked and the residual bracket stated.

- An unreplayable solver run or an SDP whose dimension/feasibility the independent checker cannot reconstruct.

## 3. Graded partial-result targets

- **P1 - Verified adversary-SDP + LP pipeline, tiny check.** Build the general-adversary SDP and the randomized-tree LP; reproduce known exact values for parity, OR, AND, majority at small \(n\).
  *Certificate:* exact-rounded SDP feasible points and LP primal/dual, independently re-substituted.

- **P2 - Symmetric-function exact table.** For all symmetric \(f:\{0,1\}^n\to\{0,1\}\) with \(n\le 6\) (each determined by a weight-pattern in \(\{0,1\}^{n+1}\)), tabulate exact \(\mathrm{ADV}^\pm\), the \(Q\) bracket, and exact \(R\).
  *Certificate:* per-function SDP/LP certificates; comparison against the known symmetric-function formulas (e.g. \(\Theta(\sqrt{n(n-k+1)})\)-type) as a sanity gate.

- **P3 - Element distinctness small cases.** Exact \(\mathrm{ADV}^\pm\) and \(Q\) bracket for element distinctness on small \((n,m)\) (e.g. \(n\le5\), \(m\le6\)).
  *Certificate:* exact-rounded SDP; matching algorithm where the bracket closes.

- **P4 - \(k\)-distinctness small cases.** Exact adversary value and \(Q\) bracket for \(3\)-distinctness and \(4\)-distinctness at the smallest nontrivial sizes, contributing exact data where only asymptotics are known.
  *Certificate:* SDP certificate + resource log; explicit statement of open bracket width.

- **P5 - Specific total functions.** Pin exact \(R\) and \(Q\) (or tight brackets) for a curated shortlist of small total functions whose exact query complexity is unrecorded.
  *Certificate:* two-sided certificates per function; a shortlist manifest with definitions.

- **P6 - Exact quantum \(Q_E\) small cases.** For functions where zero-error quantum query complexity is natural (e.g. small symmetric functions), certify \(Q_E\) exactly via the exact-error adversary/polynomial method.
  *Certificate:* exact SDP/polynomial certificate + matching exact algorithm.

- **P7 - Exact approximate degree of the targets.** Compute \(\widetilde{\deg}_{1/3}(f)\) exactly (rational LP/SDP with rounding) for the symmetric and distinctness targets, and report where it meets the adversary \(Q\)-bound (polynomial method tight) versus where a gap remains.
  *Certificate:* exact-rounded approximate-degree certificate per function; the \(\widetilde{\deg}\)-vs-\(\mathrm{ADV}^\pm\) comparison.

## 4. Known results and prior art

- **Adversary characterizes \(Q\).** Reichardt (\(\approx\)2009–2011, arXiv 0904.2759, verify): \(Q_{1/3}(f)=\Theta(\mathrm{ADV}^\pm(f))\); the negative-weight adversary is an SDP (Høyer–Lee–Špalek, \(\approx\)2007, verify). Barnum–Saks–Szegedy (\(\approx\)2003, verify): the SDP formulation of the spectral adversary.

- **Polynomial method.** Beals–Buhrman–Cleve–Mosca–de Wolf (\(\approx\)1998, verify): \(Q_\varepsilon(f)\ge\tfrac12\widetilde{\deg}_{2\varepsilon}(f)\); exact and approximate degree of symmetric functions (Paturi, \(\approx\)1992, verify).

- **Element / \(k\)-distinctness.** Ambainis (\(\approx\)2004, verify): quantum walk algorithm, \(Q(\text{element distinctness})=\Theta(n^{2/3})\); \(k\)-distinctness upper bounds \(O(n^{k/(k+1)})\) and Belovs' learning-graph improvements (\(\approx\)2012, arXiv 1205.1534, verify); matching lower bounds known only in limited regimes - exact small-\(n\) values are unrecorded.

- **Adversary lower bounds for structured problems.** Belovs and collaborators, "Applications of the adversary method" (\(\approx\)2014, arXiv 1402.3858, verify); adversary lower bound for the orthogonal-array / \(k\)-sum problems (arXiv 1304.0845, verify).

- **Symmetric functions, closed forms.** Exact and approximate degree of symmetric functions have known closed forms (Paturi, \(\approx\)1992, verify), and their quantum query complexity is \(\Theta(\sqrt{n(n-\Gamma(f)+1)})\)-type where \(\Gamma\) measures the flat interval (verify) - a sanity gate for the P2 table, not a substitute for the exact per-\(n\) census.

- **Small-\(n\) SDP practice.** Adversary/polynomial SDPs have been solved for all Boolean functions up to \(n=4\) and for symmetric functions up to \(n=6\) in the literature (verify); "On exact quantum query complexity" (verify) tabulates exact-quantum small cases. A certified exact-rounded table across P2–P6 is the deliverable.

**Status as of mid-2026 - re-verify against the current literature before starting any session.**

## 5. Attack plan

**`[search]` - the SDP lower bound with exact rounding.** Assemble the general-adversary SDP for each target from its input/output relation; solve with `SDPA-GMP` / `SDPA-DD` (arbitrary / double-double precision). **Round the optimal dual (for lower bounds) to an exact rational feasible point** by the following pipeline, each step re-checked in exact arithmetic:

1. solve to high precision and read off the near-optimal dual matrix;

2. perturb the objective value slightly below the numerical optimum to leave slack toward strict feasibility;

3. rationalize the matrix entries with continued fractions at a controlled denominator bound;

4. re-verify the linear-matrix-inequality by an exact eigenvalue / `LDL^T` sign check (`SageMath`/`FLINT`).

The exact feasible value that survives step 4 is the certificate. For symmetric functions, exploit the representation-theoretic block-diagonalization to shrink the SDP before solving.

**`[search]` - the randomized LP.** For small \(n\), solve the min-max value of randomized decision trees as an exact rational LP (`QSopt_ex`/`SoPlex` exact) with a hard input distribution (Yao) as the dual; for larger \(n\) build a certified bracket.

**`[search]` - matching upper bounds.** Construct explicit quantum algorithms from the adversary dual / span programs (Reichardt's dual-to-algorithm route) or by hand for structured cases; construct explicit randomized trees for \(R\). Close the bracket where the two meet.

**Tools.** `SDPA-GMP`/`SDPA-DD`, `SageMath`/`FLINT` for exact rounding and LMI verification, `QSopt_ex`/`SoPlex`/`SCIP` exact for LP, custom C++ for building relations and decision trees.

**One-workstation scope.** Symmetric \(n\le6\) SDPs after symmetry reduction: feasible; element distinctness / \(k\)-distinctness small \((n,m,k)\): the SDP grows fast with alphabet - expect only the smallest instances.

**Failure modes.** The rounding step is where rigor is won or lost - an unrounded SDP optimum is *not* a certificate; near-degenerate LMIs resist rationalization (report as a bracket, not an exact value); alphabet size \(m^n\) explodes distinctness SDPs; forgetting the Reichardt constant turns \(\mathrm{ADV}^\pm\) into a false exact \(Q\).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every \(Q\) lower bound is an exact rational adversary-SDP feasible point with the LMI re-verified by exact arithmetic; every \(R\) value is an exact LP primal/dual pair or a stated certified bracket; approximate/exact degrees via exact LP/SDP. Raw floating-point solver output is never load-bearing.

2. **Independent verification.** A standalone LMI-feasibility checker (separate from the solver) re-substitutes each rounded certificate; a decision-tree/algorithm replayer confirms each upper-bound construction's query count and error; a second solver re-solves each LP. Symmetric-function values are cross-checked against closed-form formulas.

3. **Reproducibility.** Function definitions, SDP/LP encodings, solver versions and precision settings, rounding procedure, and symmetry reductions recorded; SHA-256 manifest over every SDP/LP certificate, algorithm, and table entry; any prior exact value or bracket being tightened cited with source and access date.

4. **Preservation.** SDP/LP encodings, rounding scripts, algorithms, and checkers are part of the record; anything not preserved is stated explicitly.

5. **Honest reporting.** The report distinguishes, per function, an *exact* value (bracket closed) from a *certified bracket* (bounds not yet meeting), states the Reichardt constant wherever \(\mathrm{ADV}^\pm\) stands in for \(Q\), and never presents a rounded-away-from-feasible SDP optimum or a one-sided bound as an exact query complexity.
