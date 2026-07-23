# PROMPT FOR EXACT SEPARATIONS AMONG DETERMINISTIC, RANDOMIZED, AND QUANTUM QUERY COMPLEXITY

## Certified extremal separating functions and small-\(n\) query profiles for total Boolean functions

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 18 of 50
**Area:** complexity & communication
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

For total Boolean functions the deterministic, randomized, and quantum query (decision-tree) complexities \(D(f)\ge R(f)\ge Q(f)\) are all polynomially related, but the *exact exponents* of the largest possible gaps are open and have moved repeatedly over the last decade - pointer functions gave near-quadratic \(D\) vs \(R\) separations, cheat-sheet constructions broke the "\(R=O(Q^2)\)" folklore, and the current record \(R(f)=\tilde\Omega(Q(f)^{5/2})\) and beyond sits inside an unresolved gap between exponents \(3\) and \(4\). This is a domain where the certifiable product is concrete: the **exact** query complexities of explicit small separating functions, and the exact \((D,R_0,R,Q,\deg,\widetilde{\deg},bs)\) profile of every function up to some arity \(n\). The on-machine verifier is a decision-tree solver that computes \(D\), \(R_0\), \(R\) exactly by dynamic programming / LP and \(Q\) by the (tight, up to constants) general adversary SDP with exact rounding. Anything short of the section-2 standard - a separating family with only asymptotic bounds, a numerically-estimated \(Q\), a non-exhaustive sample called extremal - is a partial result.

## 1. Exact problem statement

Let \(f:\{0,1\}^n\to\{0,1\}\) be **total** (defined on all of \(\{0,1\}^n\)); partial functions \(f:\mathcal D\to\{0,1\}\), \(\mathcal D\subseteq\{0,1\}^n\), are considered only as gadget ingredients and are flagged as such.

- **Deterministic query** \(D(f)\): min depth of a deterministic decision tree computing \(f\) exactly.

- **Zero-error randomized** \(R_0(f)\): min over distributions on decision trees of the worst-case *expected* depth, always correct.

- **Bounded-error randomized** \(R(f)=R_{1/3}(f)\): min expected depth of a randomized decision tree correct with probability \(\ge 2/3\) on every input.

- **Bounded-error quantum** \(Q(f)=Q_{1/3}(f)\): min number of queries of a quantum query algorithm correct with probability \(\ge2/3\) on every input.

The companions are exact/deterministic degree \(\deg(f)\), approximate degree \(\widetilde{\deg}(f)\), block sensitivity \(bs(f)\), and certificate complexity \(C(f)\), ordered by

\[
Q(f)\ \le\ R(f)\ \le\ R_0(f)\ \le\ D(f),\qquad
\tfrac12\widetilde{\deg}(f)\ \le\ Q(f),\qquad
bs(f)\ \le\ C(f)\ \le\ D(f).
\]

The relevant known relations pinning the regime include

\[
D(f)=O\!\big(Q(f)^4\big),\qquad D(f)=O\!\big(bs(f)^3\big),\qquad Q(f)=\Theta\!\big(\mathrm{ADV}^{\pm}(f)\big),
\]

the last being Reichardt's tightness of the general adversary bound (verify the exact exponents).

**Adopted normalizations.** \(R\) and \(Q\) use error \(1/3\) unless stated; complexities are integers for \(D\) and rationals for \(R_0,R,Q\) lower/upper bounds. Cost is number of input-bit queries.

**Open questions (adopted here).**

1. **Largest \(D\) vs \(R\) exponent** \(\sup_f \log D(f)/\log R(f)\) for total \(f\) (pointer functions give \(\approx\) quadratic; the exact supremum is open).

2. **Largest \(R\) vs \(Q\) exponent** \(\sup_f \log R(f)/\log Q(f)\) (records climbed \(5/2\to8/3\to3\); the gap to \(4\) is open).

3. **Largest \(D\) vs \(Q\) exponent** (folklore \(4\); best separations lower it toward the truth).

4. **Small-\(n\) extremal separators:** for each \(n\), the functions maximizing each ratio, with exact values.

**Starting from the prompt alone.** A reader reconstructs \(f\) from a \(2^n\)-bit truth table and computes \(D\) (exact DP over subcubes), \(R_0,R\) (LP over decision-tree distributions, exact for small \(n\)), and \(Q\) (general adversary SDP, lower) - every measure is machine-derivable from the object.

## 2. Resolution standard

Full resolution of an exponent question is a **proof** valid for all total \(f\); full resolution of a small-\(n\) extremal value is a **certified exhaustive census**. Neither exponent proof is expected; the certified products are the census and the exact profiles of named separators. Named certified forms:

- **Exact query census.** For stated \(n\): exact \((D,R_0,R,Q,\deg,\widetilde{\deg},bs,C)\) for a canonical representative of every NPN class, with extremal ratios and witnesses. \(D\) is exact by DP; \(R,R_0\) exact by rational LP for small \(n\); \(Q\) bracketed by an **exact-rounded general-adversary SDP** lower bound and a matching explicit quantum algorithm or polynomial-method upper bound - reported as an exact value only when the bracket closes, otherwise as a certified interval \([Q_{\mathrm{lo}},Q_{\mathrm{hi}}]\).

- **Certified separator.** For a named separating function (pointer/cheat-sheet), the exact or two-sided-certified value of each measure entering the claimed ratio, at explicit finite size.

**Not accepted as resolution.**

- A separating **family** with only \(\tilde O/\tilde\Omega\) asymptotics reported as an *exact* separation at finite size.

- A **numerically** solved adversary SDP (floating point) presented as a \(Q\) value; the dual/primal must be rounded to an exact rational feasible point.

- \(R\) or \(R_0\) from a heuristic randomized tree rather than the exact LP optimum (small \(n\)) or a certified bound.

- A non-exhaustive sample over \(n\)-bit functions called an extremum.

- Conflating partial-function separations (Forrelation and friends, which can be exponential) with the **total**-function question - partial results bound total exponents only through an explicit lifting/cheat-sheet with its own certificate.

- \(D\) reported without the exact optimal decision tree, or \(Q\) without both an adversary lower bound and an algorithmic upper bound.

## 3. Graded partial-result targets

- **P1 - Verified query solver + tiny census.** Exact \(D,R_0,R\) and adversary-SDP \(Q\)-bounds for all NPN classes at \(n\le4\); reproduce known small values.
  *Certificate:* class count matches known NPN counts; optimal decision trees serialized; SDP lower bounds rounded exactly; independent re-evaluation.

- **P2 - Census to \(n=5\) (and \(n=6\) as compute allows).** Complete exact \(D,R_0,R\); \(Q\) as a certified interval \([Q_{\mathrm{lo}},Q_{\mathrm{hi}}]\) per class.
  *Certificate:* NPN class-count gate; extremal-ratio witnesses; resource log of where it closed.

- **P3 - Certified small pointer-function separator.** Instantiate the Göös–Pitassi–Watson / Ambainis-et-al. pointer construction at the smallest explicit sizes and certify \(D\) and \(R\) (or \(R_0\)) exactly, exhibiting the finite \(D\) vs \(R\) gap.
  *Certificate:* exact \(D\) (optimal tree), exact/two-sided \(R\); explicit truth table or oracle description.

- **P4 - Certified small cheat-sheet / \(R\)-vs-\(Q\) separator.** Instantiate a cheat-sheet-lifted function at explicit size; certify an \(R\) lower bound and a \(Q\) upper bound (algorithm) so the finite \(R/Q\) ratio is real.
  *Certificate:* adversary SDP for the \(Q\) side (exact-rounded) and an LP/adversary bound for \(R\); construction source.

- **P5 - Improved finite ratio.** Find, at some reachable \(n\), a function with a certified ratio \(D/R\), \(R/Q\), or \(D/Q\) strictly exceeding the best finite value in P3–P4.
  *Certificate:* two-sided certified measures; diff against the record with source.

- **P6 - \(Q\)-bracket closures.** Report the small functions (symmetric functions, thresholds, specific gadgets) for which the adversary SDP lower bound and an explicit algorithm meet, giving exact \(Q\).
  *Certificate:* exact-rounded SDP optimum equal to the algorithm's query count.

- **P7 - Approximate-degree small data.** Tabulate exact \(\widetilde{\deg}(f)\) across the census and the finite \(Q(f)/\widetilde{\deg}(f)\) and \(\widetilde{\deg}(f)/bs(f)\) ratios, contributing certified data on where the polynomial method is tight at small \(n\).
  *Certificate:* exact-rounded approximate-degree SDP/LP per class; ratio table with witnesses.

## 4. Known results and prior art

- **Polynomial relations.** Beals–Buhrman–Cleve–Mosca–de Wolf (\(\approx\)1998, verify): \(D(f)=O(Q(f)^6)\) via the polynomial method; \(D=O(bs^3)\), \(bs\le 2\widetilde{\deg}^2\), etc. Later \(D=O(Q^4)\)-type improvements (Aaronson–Ben-David–Kothari–Tal, verify).

- **Adversary tightness.** Reichardt (\(\approx\)2009–2011, "Span programs and quantum query complexity: the general adversary bound is nearly tight for every Boolean function," arXiv 0904.2759, verify): \(Q(f)=\Theta(\mathrm{ADV}^\pm(f))\), and \(\mathrm{ADV}^\pm\) is an SDP - the computational lever for exact \(Q\).

- **Pointer functions.** Göös–Pitassi–Watson (\(\approx\)2015, verify) and Ambainis–Balodis–Belovs–Lee–Santha–Smotrovs (\(\approx\)2016, "Separations in query complexity based on pointer functions," verify): near-quadratic \(D\) vs \(R_0\) / \(R\) and related separations.

- **Cheat sheets.** Aaronson–Ben-David–Kothari (\(\approx\)2016, "Separations in query complexity using cheat sheets," arXiv 1511.01937, verify): a power-\(2.5\) \(R\) vs \(Q\) separation and the lifting framework turning partial-function gaps into total ones.

- **Breaking \(R=O(Q^2)\).** Shalev Ben-David (\(\approx\)2016, verify): total \(f\) with \(R(f)=\tilde\Omega(Q(f)^{5/2})\); subsequent works pushed the \(R\) vs \(Q\) record toward exponents \(8/3\) and \(3\) (Sherstov / Aaronson–Ben-David–Kothari–Tal line, verify), leaving a gap up to \(4\).

- **Partial-function extremes (gadget source, not total).** Aaronson–Ambainis Forrelation and \(k\)-fold Forrelation; optimal quantum-vs-randomized separations for partial functions by Bansal–Sinha and Sherstov–Storozhenko–Wu (\(\approx\)2021, verify). The total-function status is strictly weaker.

- **Classical adversary methods.** "All classical adversary methods are equivalent for total functions" (arXiv 1709.08985, verify): the classical analogues of the adversary bound coincide for total \(f\), constraining what the \(R\)-side lower bounds can certify.

- **Small-\(n\) SDP practice.** Adversary/polynomial SDPs have been run for all functions up to \(n=4\) and symmetric functions to \(n=6\) in the literature (verify); a certified exact-rounded census with extremal witnesses is the P1–P2 product.

**Status as of mid-2026 - re-verify against the current literature before starting any session.**

## 5. Attack plan

**`[search]` - exact classical measures.** Custom C++/`SageMath`:

- \(D(f)\) by memoized DP over restrictions (partial assignments), emitting the optimal decision tree;

- \(R_0(f)\) and \(R(f)\) for small \(n\) by an exact rational LP over the (exponentially many but small-\(n\)-tractable) deterministic trees, or by the standard min-max LP with column generation - solved exactly (`QSopt_ex`/`SoPlex` exact).

**`[search]` - quantum via adversary SDP.** Formulate the general adversary bound \(\mathrm{ADV}^\pm(f)\) as an SDP; solve with `SDPA-GMP` (arbitrary precision) and **round the optimal dual to an exact rational feasible point** to certify \(Q\ge\lceil\mathrm{ADV}^\pm\rceil\)-type lower bounds; obtain matching upper bounds from explicit span-program/algorithmic constructions or the polynomial method, closing the bracket where possible.

**Enumeration.** NPN canonical generation with the class count gated against known NPN counts; extremal-ratio extraction across the census.

**Named separators.** Encode the pointer and cheat-sheet functions at their smallest instantiations; verify their measures with the same solvers.

**Tools.** `SDPA-GMP`/`SDPA-DD` for adversary SDPs with exact rounding; `SCIP`/`SoPlex` exact and `QSopt_ex` for LP; custom C++ for DP/decision trees; `SageMath`/`FLINT` for exact degree and NPN.

**One-workstation scope.** \(n\le4\) full (SDP + LP): comfortable; \(n=5\): heavy but feasible with canonical dedup; \(n=6\): symmetric/structured subclasses only.

**Failure modes.** Floating-point SDP optima are not certificates (must round exactly); the randomized-tree LP has exponentially many columns (needs generation/pruning); \(D\)-DP blows up past \(n\approx14\) even for a single function; conflating partial and total functions silently inflates claimed total-function separations.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** \(D,R_0,R\) via exact DP/LP; \(Q\) via exact-rounded adversary SDP plus an explicit matching algorithm; degrees via exact Fourier. Floating point (including raw SDP solver output) is exploratory only.

2. **Independent verification.** A separate decision-tree replayer confirms each emitted \(D\)-optimal tree; a separate SDP-feasibility checker validates the rounded adversary certificate; a second solver re-solves each small LP. Class counts gate the enumeration.

3. **Reproducibility.** Truth-table and NPN conventions, SDP/LP solver versions and precision/exact flags, seeds, and construction parameters recorded; SHA-256 manifest over every representative, tree, SDP certificate, and separator instance; the prior finite separation ratio being improved cited with source and access date.

4. **Preservation.** Solvers' input encodings, decision trees, SDP certificates, and enumeration source are part of the record; anything not preserved is stated explicitly.

5. **Honest reporting.** The report states which \(n\) the census closed for, which \(Q\) brackets closed to exact values, whether any finite \(D/R\), \(R/Q\), or \(D/Q\) ratio was strictly improved, and it never presents a partial-function (Forrelation-type) exponential gap as a total-function result, nor an asymptotic family as a certified finite separation.
