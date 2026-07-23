# PROMPT FOR OPTIMAL RESILIENT AND CORRELATION-IMMUNE BOOLEAN FUNCTIONS

## Maximum nonlinearity of \((n,1,m)\)-resilient functions and existence for open parameter sets

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 13 of 50
**Area:** Boolean & cryptographic functions
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A resilient Boolean function is one whose output stays balanced and statistically independent of any \(m\) of its inputs - the property a combiner in a stream cipher needs so that no small set of tapped bits leaks the key. Resilience trades against nonlinearity and degree (the Siegenthaler and Sarkar–Maitra bounds), and the exact frontier - the maximum nonlinearity of an \(m\)-resilient function for given \((n,m)\), and the existence of resilient functions for specific parameter tuples - has open cases in the standard tables. The task fits certified search: resilience is an exact condition on the Walsh spectrum (\(W_f\) vanishes on all low-weight points), nonlinearity is exact, and the objects correspond to orthogonal arrays and to cosets of linear codes, giving a rich structure to search and to bound. The on-machine verifier is a Walsh transform confirming the resilience support condition plus the nonlinearity value; anything short of the Section 2 standard - a construction with no matching upper bound, an existence claim without a recomputed spectrum - is a partial result, never a resolution. The coding-theory link is used as a tool; the classical-codes classification territory belongs to the mathematics program and is not the object here.

## 1. Exact problem statement

Notation as in the Boolean-function conventions: \(f:\mathbb{F}_2^n\to\mathbb{F}_2\), truth table in \(\{0,1\}^{2^n}\), Walsh transform \(W_f(w)=\sum_x(-1)^{f(x)+\langle w,x\rangle}\), nonlinearity \(\mathrm{nl}(f)=2^{n-1}-\frac12\max_w|W_f(w)|\), algebraic degree \(\deg f\).

\(f\) is **correlation-immune of order \(m\)** (denoted \(\mathrm{CI}(m)\)) iff
\[
W_f(w)=0\quad\text{for all }w\text{ with }1\le \mathrm{wt}(w)\le m,
\]
where \(\mathrm{wt}(w)\) is the Hamming weight. \(f\) is **\(m\)-resilient** iff it is \(\mathrm{CI}(m)\) **and balanced**, equivalently
\[
W_f(w)=0\quad\text{for all }w\text{ with }0\le\mathrm{wt}(w)\le m.
\]
The standard label \((n,1,m,N)\) means an \(m\)-resilient function on \(n\) variables with nonlinearity \(N\) (the "\(1\)" records single-bit output; vectorial \((n,k,m)\) generalizes to \(k\) outputs). Write \(\mathrm{nl}_{\max}(n,m)\) for the maximum nonlinearity of an \(m\)-resilient \(n\)-variable function.

The **Xiao–Massey characterization** restates resilience spectrally: \(f\) is \(m\)-resilient iff its Walsh transform vanishes on the entire Hamming ball of radius \(m\) around the origin,
\[
W_f(w)=0\quad\text{for all }w\in\mathbb{F}_2^n,\ \mathrm{wt}(w)\le m,
\]
a set of \(\sum_{i=0}^{m}\binom{n}{i}\) exact linear conditions on the truth-table bits - which is why resilience is cheap to certify and natural to encode for SAT.

**Bounds fixing the regime.**
- **Siegenthaler bound:** an \(m\)-resilient function has \(\deg f\le n-m-1\) (for \(m\le n-2\)); resilience trades directly against algebraic degree.
- **Sarkar–Maitra divisibility:** for \(m\le n-2\), \(\mathrm{nl}_{\max}(n,m)\) is divisible by \(2^{m+1}\), and \(\mathrm{nl}_{\max}(n,m)\le 2^{n-1}-2^{m+1}\).
- The upper bound \(2^{n-1}-2^{m+1}\) is **attained** for \(m\) large relative to \(n\) (roughly \(m\ge 0.6n-0.4\)); for smaller \(m\) the exact maximum is often **open**.
- The divisibility means the open question in a cell is which *specific multiple of \(2^{m+1}\)* is the maximum, a discrete ladder of at most a few rungs.

**Combinatorial correspondence (tool, not object).** An \(m\)-resilient function corresponds to a binary **orthogonal array** \(\mathrm{OA}(2^{n-1},n,2,m)\) (the support of \(f\)), and to a coset structure over a linear \([n,\,k]\) code via the Xiao–Massey / Maiorana–McFarland viewpoint. These are used to construct and bound; the classification of the underlying codes/arrays as objects in their own right is out of scope (owned by the mathematics program).

Every criterion here is decidable exactly and cheaply: balancedness and resilience from \(\sum_{i\le m}\binom{n}{i}\) low-weight Walsh coefficients, nonlinearity from the full spectrum, degree from the ANF. The verifier is entirely integer-valued, and the Sarkar–Maitra divisibility means a record is one of only a few admissible multiples of \(2^{m+1}\).

**The questions, adopted scope.** For specified small \(n\) with open table entries (primary \(n=9,10,11,12\)):
(i) the exact **\(\mathrm{nl}_{\max}(n,m)\)** for open \((n,m)\);
(ii) certified **existence/nonexistence** of \((n,1,m,N)\) functions for target \(N\) in open cells;
(iii) certified constructions attaining the Sarkar–Maitra bound where attainability is open. Cost: verified Walsh spectra (resilience + nonlinearity), DRAT/LRAT for nonexistence.

## 2. Resolution standard

A **full resolution** of a scoped instance is one of:

- **(Optimal value)** a proof that \(\mathrm{nl}_{\max}(n,m)=N\): an explicit \(m\)-resilient \(n\)-variable function with a recomputed Walsh spectrum proving resilience (\(W_f\) vanishes on \(\mathrm{wt}\le m\)) and \(\mathrm{nl}=N\), **plus** a matching machine-checkable bound (a DRAT/LRAT UNSAT proof, or a certified exhaustion within a complete class, that no \(m\)-resilient function reaches \(N+2^{m+1}\));
- **(Existence/nonexistence)** a certified witness, or a machine-checkable nonexistence proof, for a target \((n,1,m,N)\) in an open table cell.

Named certified forms:

- **(a) Explicit construction** with a recomputed Walsh spectrum (resilience + nonlinearity + degree).
- **(b) SAT-with-DRAT** for existence/nonexistence of an \((n,1,m,N)\) function.
- **(c) Exhaustive/canonical enumeration** of a symmetry class or a coset-code family via nauty/orbit counting, with completeness certified.
- **(d) Exact spectral/LP certificate** bounding \(\mathrm{nl}_{\max}(n,m)\) from above with rational arithmetic.

A one-sided result - a record lower bound in an open cell, or a certified upper bound - is a legitimate reportable increment and is labelled distinctly from a *determined* \(\mathrm{nl}_{\max}(n,m)\) (matched bounds).

**Not accepted as resolution.**

- A resilient function attaining nonlinearity \(N\) with **no** matching upper bound - a record lower bound (a genuine P-level partial result), not a determined \(\mathrm{nl}_{\max}\).
- A resilience claim whose Walsh spectrum is not independently recomputed (a single nonzero \(W_f(w)\) at low weight breaks it).
- An existence claim via a coset/OA construction whose resulting truth table is not verified to be resilient with the stated nonlinearity.
- A within-class maximum presented as the global \(\mathrm{nl}_{\max}(n,m)\) without a certified losslessness argument.
- A construction inheriting a family's resilience order but never recomputing the low-weight Walsh spectrum on the concrete instance.
- A record comparison that cites a table cell without the specific source and access date of the value being beaten.
- An unreplayable UNSAT, or a reference to the coding-theory literature standing in for an actual recomputed Boolean-function certificate.
- A nonlinearity value not divisible by \(2^{m+1}\) reported as an \(m\)-resilient record (it violates Sarkar–Maitra and signals a bug).
- A degree that violates the Siegenthaler bound \(\deg\le n-m-1\), reported without flagging the contradiction.
- A "resilient" function whose balancedness (\(W_f(0)=0\)) was not checked - correlation-immune-but-unbalanced is a different object.
- Asymptotic statements in place of the exact open small-\(n\) value.
- A vectorial \((n,k,m)\) claim where only *some* nonzero output combinations were checked \(m\)-resilient.
- A cell "resolved" by a construction that meets the target \(N\) but where no matching upper bound is offered - that improves the lower bound only.

## 3. Graded partial-result targets

**P0 - Resilience-test base case.** Validate the resilience checker on known objects: a bent-based 1-resilient function, the parity function (\(\mathrm{CI}(n-1)\), unbalanced), and a simple Maiorana–McFarland instance, confirming the low-weight Walsh conditions and balancedness are computed identically by two implementations. *Certificate:* recomputed low-weight spectra with cross-implementation agreement.

**P1 - Reproduce the frontier.** Independently verify landmark table entries: the \((7,1,2,56)\) function (max nonlinearity for 7-variable 2-resilient, attaining \(2^{6}-2^{3}=56\)) and the \((10,1,4,480)\) function; recompute their Walsh spectra to confirm resilience and nonlinearity. *Certificate:* recomputed spectra with SHA-256, matching published values.

**P2 - Certified small-\(n\) table.** Reconstruct, with a certified pipeline, the exact \(\mathrm{nl}_{\max}(n,m)\) for all \((n,m)\) with \(n\le 8\) (a mix of attained-bound cells and known exact values), including any DRAT-certified upper bounds. *Certificate:* enumeration/SAT replays matching the standard tables.

**P3 - Attain a bound where attainability is open.** For an open cell, construct an \(m\)-resilient function attaining the Sarkar–Maitra bound \(2^{n-1}-2^{m+1}\) (or improving the best-known nonlinearity), via a coset/Maiorana–McFarland construction verified as a Boolean function. Since the record moves in steps of \(2^{m+1}\), even a single-rung improvement is a clean, citable increment. *Certificate:* recomputed Walsh spectrum proving resilience + nonlinearity + degree.

**P4 - Existence in an open parameter set.** Settle a specific open \((n,1,m,N)\) existence question - a witness with recomputed spectrum, or a certified nonexistence proof. *Certificate:* explicit function, or a DRAT/LRAT / certified-exhaustion nonexistence.

**P5 - Certified upper bound.** Produce a machine-checkable proof that \(\mathrm{nl}_{\max}(n,m)\le N\) for an open cell (which, with a matching construction, resolves the cell): a DRAT/LRAT UNSAT for "\(\exists\) \(m\)-resilient \(f\) with \(\mathrm{nl}\ge N+2^{m+1}\)", or an exact spectral/LP argument. *Certificate:* CNF + replayed proof, or exact rational certificate.

**P6 - Vectorial extension.** Extend a resolved single-output cell to a certified \((n,k,m)\)-resilient vectorial function (all nonzero output combinations \(m\)-resilient) with high nonlinearity. *Certificate:* recomputed Walsh spectra over all nonzero linear combinations.

**P7 - Degree-optimal resilient functions.** For an open cell, find or certify a function meeting *both* the Siegenthaler degree bound \(\deg=n-m-1\) and the maximum nonlinearity - the simultaneously degree- and nonlinearity-optimal resilient function, which is not always known to exist. *Certificate:* recomputed spectrum, degree from the ANF, and a matching bound where claimed optimal.

## 4. Known results and prior art

- **Foundations:** correlation immunity (Siegenthaler, ~1984) and resilience (Chor–Goldreich–Håstad–Friedman–Rudich–Smolensky, ~1985) as the combiner-security criteria for stream ciphers (verify).
- **Siegenthaler bound (~1984):** \(\deg\le n-m-1\); resilience trades against degree.
- **Sarkar–Maitra bound and divisibility (~2000):** \(\mathrm{nl}_{\max}(n,m)\le 2^{n-1}-2^{m+1}\) and divisibility by \(2^{m+1}\); independently Tarannikov, and Zheng–Zhang gave related bounds (~2000) (verify).
- **Attainment regime:** the bound \(2^{n-1}-2^{m+1}\) is met for \(m\ge 0.6n-0.4\) (Tarannikov's construction and refinements); the maximum-nonlinearity problem for 7-variable functions of any resiliency order was closed by an explicit \((7,1,2,56)\) function (Maitra–Pasalic / Kavut–Yücel-type search; ~2002) (verify).
- **Construction toolbox:** Maiorana–McFarland and its modifications, the Xiao–Massey spectral characterization, direct-sum and concatenation constructions, and the orthogonal-array / linear-code correspondence (Camion–Carlet–Charpin–Sendrier; Chee–Seberry–Zhang; ~1990s) (verify).
- **Open cells:** for smaller \(m\) relative to \(n\) - e.g. low-order resiliency in \(n=9,\dots,12\) - the exact \(\mathrm{nl}_{\max}(n,m)\) and some existence questions remain open, tracked in resiliency/nonlinearity tables (Sarkar–Maitra; Tarannikov; Pasalic; and the Boolean-functions community pages) (verify current open cells).
- **Correlation immunity of unbalanced functions:** best correlation immunity of unbalanced functions is a separate active line (Krotov and others, ~2019) (verify) - distinct from the resilient (balanced) target here.
- **Higher-order and vectorial:** \((n,k,m)\)-resilient functions and their nonlinearity bounds (Zhang–Zheng; Gupta–Sarkar; ~2000s) extend the single-output theory; the SCV-type bound governs vectorial nonlinearity here too (verify).
- **Degree-optimality:** the simultaneous attainment of the Siegenthaler degree bound and maximum nonlinearity is delicate; several small cells are settled, others open (Pasalic–Maitra–Johansson–Sarkar; ~2000s) (verify).
- **Tables and trackers:** the resiliency–nonlinearity tables in Sarkar–Maitra and the Boolean-functions community pages are the live record of open cells; treat them as the baseline to cite and beat (verify).

**Web-verify the headline record tables** - the \(\mathrm{nl}_{\max}(n,m)\) tables and open existence cells move; consult the Boolean-functions community pages and recent journals. **Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

`[search]` first computations on one workstation:

1. **Verified resilience test (P1).** Fast Walsh–Hadamard transform in **SageMath** and independently in **custom C++**; \(f\) is \(m\)-resilient iff \(W_f(w)=0\) for all \(\mathrm{wt}(w)\le m\) - an exact integer check over the \(\sum_{i\le m}\binom{n}{i}\) low-weight points, together with balancedness (\(W_f(0)=0\)). Cross-implement to gate integrity.
2. **Ground truth (P1–P2).** Verify the landmark \((7,1,2,56)\), \((10,1,4,480)\) and the \(n\le 8\) table cells; reproduce any published DRAT upper bounds. Confirm each reproduced value against both its lower-bound construction and its upper-bound proof, so the pipeline is exercised in both directions before an open cell is attempted.
3. **Coset/OA constructions (P3, P6).** Implement Maiorana–McFarland and Tarannikov-style constructions parameterized by a linear \([n,k]\) code / permutation; instantiate for open cells and verify the resulting Boolean function's spectrum. Use **GAP**/**SageMath** for the code/coset bookkeeping.
4. **Symmetry-restricted search (P3–P4).** Restrict to rotation-symmetric or code-coset-structured functions to make the space finite-in-practice; enumerate representatives with **nauty**/orbit counting, run the resilience + nonlinearity battery, canonicalize survivors. Heuristic search (annealing) as explorer, every hit re-verified.
5. **SAT existence/nonexistence (P4–P5).** Encode "\(\exists f\): \(W_f(w)=0\) for \(\mathrm{wt}(w)\le m\) and \(\mathrm{nl}\ge N\)" - the resilience conditions are linear equalities on the truth-table bits (each \(W_f(w)\) is a signed sum), the nonlinearity a bound on the remaining coefficients - and run **CaDiCaL**/**kissat**/**CryptoMiniSat** with proof logging; replay UNSAT with `drat-trim`/`lrat-check`. Exact ILP/LP (SCIP, QSopt_ex) for spectral upper bounds.
6. **Divisibility filter.** Restrict every target and every upper-bound question to multiples of \(2^{m+1}\) (Sarkar–Maitra); this collapses the candidate values in a cell to a short ladder and sharpens both search and bound.

Construction families to instantiate for open cells, each verified as a Boolean function:

- **Maiorana–McFarland** \(f(x,y)=\langle x,\phi(y)\rangle+g(y)\) with \(\phi\) into codewords of a good linear code - the workhorse resilient construction.
- **Tarannikov's construction** - meets the \(2^{n-1}-2^{m+1}\) bound in its regime; the recursive elevator between dimensions.
- **Direct sum / concatenation** - combine known resilient functions to raise \(n\) or \(m\).
- **Rotation-symmetric resilient** - the finite-in-practice search class for smaller cells.

**One-workstation scope and failure modes.**

- *Test cheap, search vast:* only symmetry/coset restriction or SAT makes the space finite-in-practice; global-optimum claims must justify completeness.
- *Silent resilience breakage:* one nonzero low-weight Walsh coefficient voids resilience - recompute the full low-weight spectrum, never trust a construction's promise.
- *Coding-theory scope drift:* the OA/code correspondence is a tool; do not slide into classifying the codes themselves (mathematics-program territory).
- *Unverified solver output:* UNSAT unproven until replayed by a separate DRAT/LRAT checker.
- *Bound rigor:* floating-point LP bounds are exploratory until made exact-rational.
- *Divisibility slips:* forgetting the \(2^{m+1}\) divisibility either wastes search on impossible values or misreads a bug as a record.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every resilience claim is an exact "\(W_f=0\) on \(\mathrm{wt}\le m\)" check from a recomputed Walsh spectrum; every nonlinearity is exact; every nonexistence is a DRAT/LRAT proof or a certified exhaustion. No floating point in a load-bearing step.
2. **Independent verification.** Two independently written Walsh transforms agree on every load-bearing spectrum; every DRAT/LRAT proof is replayed by a separate checker; every coset/OA construction's output truth table is independently re-tested; every symmetry-class orbit count is confirmed two ways. Every reported nonlinearity is checked for \(2^{m+1}\)-divisibility and every degree against the Siegenthaler bound as automatic sanity gates.
3. **Reproducibility.** Record the variable ordering, construction parameters (code, permutation), class definition, all encodings, and tool versions (SageMath, GAP, nauty, solvers), with a SHA-256 manifest over every truth table, Walsh spectrum, CNF, and proof. Cite the exact table cell / record being matched or beaten (value, authors, source, access date). Archive the full truth table of every record-level function, not just its \((n,m,N,\deg)\) label.
4. **Preservation.** All search, construction, and enumeration source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front whether an *optimal \(\mathrm{nl}_{\max}(n,m)\)* was determined (with a matching bound), a *record lower bound improved*, or an *existence cell settled*, and in which class any completeness claim holds. A within-class maximum is never presented as the global \(\mathrm{nl}_{\max}(n,m)\), and a coding-theory reference is never substituted for a recomputed Boolean-function certificate.

Calibration for the session lead: the realistic product is P1–P3 - a validated resilience/nonlinearity toolchain, a reproduced table, and a bound attained or a record lower bound improved in an open cell - plus, with luck, a settled existence cell (P4) or a certified upper bound (P5). Determining \(\mathrm{nl}_{\max}(n,m)\) exactly in an open cell (matched bounds) is the headline; a one-sided improvement is the common, still-valuable outcome and is labelled as such. The task is deliberately kept distinct from the mathematics program's classification of the underlying orthogonal arrays and codes.
