# PROMPT FOR BOOLEAN FUNCTIONS WITH OPTIMAL ALGEBRAIC IMMUNITY AND SIMULTANEOUS OPTIMALITY

## Maximum algebraic immunity \(\lceil n/2\rceil\) together with high nonlinearity and good behavior against fast algebraic attacks

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 12 of 50
**Area:** Boolean & cryptographic functions
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Algebraic immunity measures a Boolean function's resistance to algebraic attacks on stream ciphers: it is the least degree of a nonzero annihilator of \(f\) or of \(f+1\). Maximum algebraic immunity is \(\lceil n/2\rceil\), and the Carlet–Feng construction gives an infinite family attaining it while also achieving good nonlinearity - yet a filtering function must be *simultaneously* good along several axes (algebraic immunity, nonlinearity, algebraic degree, resistance to fast algebraic attacks, balancedness), and the exact frontier of what can be achieved together, and the complete classification/counts for small \(n\), remain **open**. The task fits certified search: algebraic immunity is decidable by an exact rank computation over \(\mathbb{F}_2\) (the Meier–Pasalic–Carlet linear-algebra test), nonlinearity is an exact Walsh computation, and the space of candidates in a symmetry class is finite-in-practice. The on-machine verifier is the annihilator-rank test plus a Walsh transform; anything short of the Section 2 standard - an optimal-AI function with unrecorded nonlinearity, a count without a certified completeness argument - is a partial result, never a resolution.

## 1. Exact problem statement

Notation as in the Boolean-function conventions: \(f:\mathbb{F}_2^n\to\mathbb{F}_2\) in \(\mathcal{B}_n\), truth table in \(\{0,1\}^{2^n}\), Walsh transform \(W_f(w)=\sum_x(-1)^{f(x)+\langle w,x\rangle}\), nonlinearity \(\mathrm{nl}(f)=2^{n-1}-\frac12\max_w|W_f(w)|\), algebraic normal form and algebraic degree \(\deg f\) as in problem 10.

An **annihilator** of \(f\) is a function \(g\in\mathcal{B}_n\), \(g\neq0\), with \(f\cdot g=0\) (pointwise product \(0\) everywhere \(f=1\)); the annihilators of \(f\) of degree \(\le d\) form an \(\mathbb{F}_2\)-vector space \(\mathrm{An}_d(f)\). The **algebraic immunity** is
\[
\mathrm{AI}(f)=\min\bigl\{\deg g : g\neq0,\ f g=0\ \text{ or }\ (f+1)g=0\bigr\}
=\min\bigl\{d:\ \mathrm{An}_d(f)\neq\{0\}\ \text{ or }\ \mathrm{An}_d(f+1)\neq\{0\}\bigr\}.
\]
For every \(f\in\mathcal{B}_n\), \(\mathrm{AI}(f)\le\lceil n/2\rceil\); \(f\) has **maximum (optimal) algebraic immunity** iff \(\mathrm{AI}(f)=\lceil n/2\rceil\). The bound follows from a dimension count: the space of functions of degree \(\le\lceil n/2\rceil\) has dimension \(\sum_{i\le\lceil n/2\rceil}\binom{n}{i}>2^{n-1}\ge\mathrm{wt}(f)\), forcing a nonzero annihilator. Deciding \(\mathrm{AI}(f)\le d\) is thus one \(\mathbb{F}_2\) rank computation on a \(\mathrm{wt}(f)\times\sum_{i\le d}\binom{n}{i}\) matrix (Meier–Pasalic–Carlet).

The nonlinearity of an optimal-\(\mathrm{AI}\) function obeys the **Lobanov bound**
\[
\mathrm{nl}(f)\ \ge\ 2\sum_{i=0}^{\lceil n/2\rceil-2}\binom{n-1}{i}\ =\ 2^{n-1}-\binom{n-1}{\lceil n/2\rceil-1}\quad(n\text{ even, adapt for odd}),
\]
so optimal \(\mathrm{AI}\) already forces fairly high nonlinearity; the open question is the *exact maximum* it allows.

**Resistance to fast algebraic attacks (FAA).** For integers \(e<d\), say \(f\) admits a relation of type \((e,d)\) if there is \(g\neq0\) with
\[
\deg g=e\quad\text{and}\quad \deg(f\cdot g)=d ,
\]
which a fast algebraic attack exploits with cost governed by \(e\) and \(e+d\). Optimal FAA-resistance requires that no low-\(e\), low-\((e+d)\) relations exist; the relevant profile is the set of achievable \((e,d)\). A function has **perfect algebraic immunity** if no \((e,d)\) with \(e<\lceil n/2\rceil\) and \(e+d<n\) occurs. This is a distinct, strictly stronger requirement than optimal \(\mathrm{AI}\), and is checked by a family of exact \(\mathbb{F}_2\) rank computations, one per candidate \((e,d)\).

**Simultaneous optimality target.** Fix \(n\). Seek \(f\) that is **balanced** (\(\mathrm{wt}(f)=2^{n-1}\)), has **optimal \(\mathrm{AI}=\lceil n/2\rceil\)**, has **optimal or near-optimal FAA-resistance**, achieves **algebraic degree** \(n-1\) (the maximum for a balanced function), and has **nonlinearity** as high as possible (the Lobanov bound gives \(\mathrm{nl}(f)\ge 2^{n-1}-\binom{n-1}{\lceil n/2\rceil-1}\) for optimal-\(\mathrm{AI}\) functions; the question is how much higher one can go).

All five axes are decidable exactly: balancedness by a weight count, \(\mathrm{AI}\) and the FAA \((e,d)\)-profile by \(\mathbb{F}_2\) ranks, degree from the ANF, nonlinearity from the Walsh spectrum. There is no numerical approximation anywhere in the verifier - the entire profile of a candidate is an exact integer tuple.

**The questions, adopted scope.** For specified small \(n\) (primary \(n=8,9,10\)):
(i) the **maximum nonlinearity** achievable by a balanced function with optimal \(\mathrm{AI}\) (and, separately, with optimal \(\mathrm{AI}\) + optimal FAA-resistance);
(ii) certified **classification or counts** of optimal-\(\mathrm{AI}\) functions within a symmetry class;
(iii) certified existence/nonexistence of functions meeting a full simultaneous-optimality profile. Cost: exact annihilator-rank tests, Walsh spectra, FAA-relation degree tests; DRAT/LRAT for nonexistence.

## 2. Resolution standard

A **full resolution** of a scoped instance is one of:

- **(Optimal value)** a proof that the maximum nonlinearity of balanced optimal-\(\mathrm{AI}\) functions in \(n\) variables equals \(N\): a function attaining \(N\) with a recomputed annihilator-rank test (\(\mathrm{AI}=\lceil n/2\rceil\)), a recomputed Walsh spectrum (\(\mathrm{nl}=N\)), and a balancedness/degree check, **plus** a matching machine-checkable bound (a DRAT/LRAT UNSAT proof, or an isomorph-free exhaustion within a certified-complete class, that nothing does better);
- **(Existence/classification)** a certified construction, or an isomorph-free classification/count within a delimited class, of functions meeting a stated simultaneous-optimality profile, with a completeness certificate.

Named certified forms:

- **(a) Explicit construction** with recomputed \(\mathrm{AI}\) (annihilator rank), Walsh spectrum, degree, and FAA profile.
- **(b) SAT-with-DRAT** for existence/nonexistence of a function with prescribed \((\mathrm{AI},\mathrm{nl},\deg,\text{FAA})\).
- **(c) Exhaustive/canonical enumeration** of a symmetry class (rotation-symmetric, etc.) via nauty/orbit counting, with completeness certified.
- **(d) Exact rank certificate:** the annihilator matrix and its certified \(\mathbb{F}_2\)-rank, so \(\mathrm{AI}\) is auditable independently of the search code.

A one-sided record improvement (a higher-nonlinearity optimal-\(\mathrm{AI}\)-and-FAA function) is a legitimate reportable increment; a *determined maximum* additionally requires the matching bound and is labelled distinctly.

**Not accepted as resolution.**

- An optimal-\(\mathrm{AI}\) function with **no** recorded nonlinearity, FAA profile, or degree - the whole point is the simultaneous profile.
- A high-nonlinearity function whose \(\mathrm{AI}\) is asserted but not verified by an exact annihilator-rank computation.
- An improvement claim that does not name the exact baseline function and its full profile for comparison.
- A within-class maximum presented as the global optimum without a certified losslessness argument.
- A count of optimal-\(\mathrm{AI}\) functions from string comparison without a certified canonical/equivalence form.
- An FAA-resistance claim not backed by an exact test of achievable \((e,d)\) relations.
- An unreplayable UNSAT, or an asymptotic statement in place of the exact small-\(n\) value.
- A nonlinearity comparison that omits whether the competing functions were balanced (balancedness materially shifts the record).
- An FAA claim of the form "optimal \(\mathrm{AI}\) implies FAA-resistant" - it does not; FAA is a separate profile that must be measured.
- A count of optimal-\(\mathrm{AI}\) functions that conflates functions with equivalence classes, or omits the equivalence used.
- A nonlinearity record that silently drops the balancedness or degree-\(n-1\) requirement to inflate the value.
- An \(\mathrm{AI}\) asserted from a partial annihilator search that did not certify the *absence* of lower-degree annihilators (both \(f\) and \(f+1\)).

## 3. Graded partial-result targets

**P0 - Annihilator-test base case.** Validate the annihilator-rank engine on functions of known \(\mathrm{AI}\) (the majority function; a random function; a low-degree function), confirming exact agreement between two independent implementations before any record work. *Certificate:* the annihilator matrices, their \(\mathbb{F}_2\)-ranks, and cross-implementation agreement.

**P1 - Reproduce the frontier.** Independently verify the Carlet–Feng function for \(n=8,9,10\): recompute \(\mathrm{AI}=\lceil n/2\rceil\) by annihilator rank, the Walsh spectrum and nonlinearity, the algebraic degree, and the FAA profile; confirm the published values. *Certificate:* recomputed rank tables, Walsh spectra, and FAA-relation tests with SHA-256.

**P2 - Certified small-\(n\) landscape.** For \(n=6,7\), compute the exact maximum nonlinearity of balanced optimal-\(\mathrm{AI}\) functions by a certified exhaustion within a symmetry class (or full exhaustion where feasible), and compare to the Lobanov lower bound. This calibrates how far above the Lobanov floor real optima sit, informing the \(n=8,9,10\) targets. *Certificate:* isomorph-free enumeration completeness plus recomputed profiles.

**P3 - Improve or match a record.** For \(n=8,9,10\), search (symmetry-restricted or heuristic-then-verified) for a balanced optimal-\(\mathrm{AI}\) function with nonlinearity exceeding the best-known Carlet–Feng-type value while preserving optimal \(\mathrm{AI}\), degree \(n-1\), and FAA-resistance, or certify no improvement in the searched class. Any nonlinearity gain must be shown not to cost an axis. *Certificate:* recomputed full profile of any improvement, or a class-restricted DRAT UNSAT.

**P4 - Full simultaneous-optimality witness.** Exhibit, for a specific \(n\), a balanced function with optimal \(\mathrm{AI}\), optimal FAA-resistance, degree \(n-1\), and the highest nonlinearity you can certify - the complete filtering-function profile. *Certificate:* recomputed \(\mathrm{AI}\), Walsh spectrum, degree, and full FAA \((e,d)\) table.

**P5 - Classification/count within a class.** Produce a certified isomorph-free count or classification of optimal-\(\mathrm{AI}\) functions (or optimal-\(\mathrm{AI}\)-plus-optimal-FAA functions) within a delimited class in a small \(n\). A certified count of the optimal-\(\mathrm{AI}\)-and-optimal-FAA functions in a fixed symmetry class would be especially informative, since the intersection of both criteria is poorly mapped. *Certificate:* canonical-generation completeness with nauty-checked distinctness.

**P6 - Certified optimality bound.** A machine-checkable proof that no balanced optimal-\(\mathrm{AI}\) function in \(n\) variables (in a stated broad family) exceeds nonlinearity \(N\): a DRAT/LRAT UNSAT certificate or an exact combinatorial bound. *Certificate:* CNF + replayed proof, or exact rational certificate.

**P7 - Small-\(n\) exact count.** For a small \(n\) (say \(n=6\)), determine the exact number of optimal-\(\mathrm{AI}\) functions, or of balanced optimal-\(\mathrm{AI}\) functions attaining the maximum nonlinearity, up to affine equivalence - an exact enumeration the literature does not fully tabulate. *Certificate:* isomorph-free canonical generation with a Burnside cross-check.

## 4. Known results and prior art

- **Algebraic attacks:** the threat model - Courtois–Meier (~2003) showed low-degree annihilators break filter/combiner stream ciphers, motivating the \(\mathrm{AI}\) criterion (verify).
- **Maximum AI is \(\lceil n/2\rceil\):** established via the annihilator linear-algebra bound (Courtois–Meier, ~2003; Meier–Pasalic–Carlet, ~2004) (verify).
- **Carlet–Feng construction (~2008):** an infinite class of balanced functions with optimal \(\mathrm{AI}\), good resistance to fast algebraic attacks, algebraic degree \(n-1\), and good nonlinearity - roughly \(\mathrm{nl}\approx 2^{n-1}-2^{n/2}\cdot(\ln 2)\,n/\pi\)-type behavior; for concrete small \(n\) the Carlet–Feng nonlinearity is the standard benchmark (verify exact values per \(n\)).
- **Lobanov bound (~2005):** any \(f\) with optimal \(\mathrm{AI}\) satisfies \(\mathrm{nl}(f)\ge 2^{n-1}-\binom{n-1}{\lceil n/2\rceil-1}\); a matching-ish upper structure is understood but the *achievable* maximum for balanced optimal-\(\mathrm{AI}\) functions is not pinned for all small \(n\) (verify).
- **Other constructions:** Tu–Deng functions (optimal \(\mathrm{AI}\), high nonlinearity, from a combinatorial conjecture on modular addition; ~2011), Tang–Carlet–Tang functions, and hidden-weight/majority-based constructions; extensions of Carlet–Feng improving nonlinearity via univariate/hill-climbing methods (~2011–2018) (verify).
- **Perfect algebraic immunity and FAA:** the exact conditions and the tension between optimal FAA-resistance and high nonlinearity are actively studied (Liu–Feng–Zhang; Carlet; ~2010s) (verify).
- **Small-\(n\) classification/counts:** exact counts of optimal-\(\mathrm{AI}\) functions and the exact max nonlinearity under the full profile are known only in low dimensions / restricted classes (verify).
- **Bent-based and majority functions:** the majority function has optimal \(\mathrm{AI}\) but poor nonlinearity/balancedness; it is the cautionary base case showing \(\mathrm{AI}\) alone is insufficient (verify).
- **Fast-algebraic-attack theory:** Courtois's fast algebraic attacks (~2003) and the \((e,d)\)-relation framework (Hawkes–Rose; Armknecht) set the FAA-resistance criterion that Carlet–Feng was designed to meet (verify).
- **Univariate/hill-climbing improvements:** genetic and Walsh-spectrum-based local search raised the nonlinearity of Carlet–Feng-class functions without degrading \(\mathrm{AI}\)/FAA in several small \(n\) (~2013–2018) - the natural explorer to reuse (verify).
- **Resources:** Carlet's monograph (~2021) and the "Boolean functions" wiki collate the \(\mathrm{AI}\)/FAA landscape and per-\(n\) records (verify).
- **Cross-reference:** the exact-enumeration methodology overlaps problems 10 and 13 (canonical generation under affine equivalence, Burnside cross-checks); reuse that infrastructure rather than rebuilding it.

**Web-verify the headline record tables** - the best-known nonlinearity for optimal-\(\mathrm{AI}\) (and optimal-\(\mathrm{AI}\)+FAA) functions per \(n\) moves; consult the Boolean-functions community pages and recent journals/ePrint. **Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

`[search]` first computations on one workstation:

1. **Verified AI test (P1).** Implement the Meier–Pasalic–Carlet annihilator test: \(\mathrm{AI}(f)\le d\) iff the \(\mathbb{F}_2\) linear system "\(g\) of degree \(\le d\) with \(fg=0\)" (or \((f+1)g=0\)) has a nonzero solution - an exact Gaussian elimination / rank computation over \(\mathbb{F}_2\) on a \(\mathrm{wt}(f)\times\binom{\le d}{}\) matrix. Implement in **SageMath** and independently in **custom C++**; agreement gates integrity. Add an exact FAA \((e,d)\)-relation degree tester and a fast Walsh transform.
2. **Ground truth (P1–P2).** Verify Carlet–Feng and Tu–Deng functions for \(n=6,\dots,10\); tabulate \((\mathrm{AI},\mathrm{nl},\deg,\text{FAA})\).
3. **Symmetry-restricted search (P3, P5).** Restrict to rotation-symmetric or idempotent classes to make the space finite-in-practice; enumerate representatives with **GAP**/**nauty** orbit counting, run the AI + Walsh + FAA battery, and canonicalize survivors. Use hill-climbing / simulated annealing as an *explorer* (every hit exactly re-verified).
4. **SAT existence/nonexistence (P4, P6).** Encode "\(\exists f\): balanced, \(\mathrm{AI}\ge\lceil n/2\rceil\), \(\mathrm{nl}\ge N\), degree \(n-1\), FAA constraints" - with the annihilator conditions as linear constraints over the truth-table bits - and run **CaDiCaL**/**kissat**/**CryptoMiniSat** with proof logging; replay UNSAT with `drat-trim`/`lrat-check`. Symmetry-break aggressively. Note the \(\mathrm{AI}\ge\lceil n/2\rceil\) constraint is "no low-degree annihilator of \(f\) or \(f+1\)", a family of linear-independence conditions that must be encoded for both \(f\) and its complement.
5. **Bounds.** Exact ILP/LP (SCIP, QSopt_ex) for spectral upper bounds on nonlinearity under the optimal-\(\mathrm{AI}\) constraint.
6. **Profile battery.** Fix one reusable pipeline that, given any truth table, outputs the certified tuple \((\mathrm{AI},\mathrm{nl},\deg,\text{FAA-profile},\text{balancedness})\) with all sub-certificates; every candidate passes through it so no axis is ever left unreported.

Construction families to seed the search, each verified end-to-end:

- **Carlet–Feng** - the benchmark: support is a union of a coset structure over \(\mathbb{F}_{2^n}^\ast\); optimal \(\mathrm{AI}\), degree \(n-1\), good FAA.
- **Tu–Deng** - high nonlinearity via a modular-addition combinatorial property.
- **Tang–Carlet–Tang** - a further high-nonlinearity, optimal-\(\mathrm{AI}\) family.
- **Rotation-symmetric / idempotent optimal-\(\mathrm{AI}\)** - the finite-in-practice search classes.

**One-workstation scope and failure modes.**

- *AI test cost:* the annihilator matrix has \(\sim\binom{n}{\le\lceil n/2\rceil}\) columns and \(2^{n-1}\) rows - for \(n=10\) that is hundreds by thousands, exact and fast; for larger \(n\) it grows and must be watched.
- *Search explosion:* only symmetry restriction or SAT makes the function space finite-in-practice; a global-optimum claim must justify completeness.
- *Profile omission:* reporting \(\mathrm{AI}\) without FAA/degree/nonlinearity defeats the purpose - always report the full profile.
- *Unverified solver output:* UNSAT unproven until replayed by a separate DRAT/LRAT checker.
- *Bound rigor:* floating-point LP bounds are exploratory until made exact-rational.
- *FAA subtlety:* fast-algebraic-attack resistance is a stronger, separate condition than optimal \(\mathrm{AI}\); a function optimal in \(\mathrm{AI}\) can be weak against FAA - test the \((e,d)\) profile explicitly, never infer it.
- *Rank-mod-2 pitfalls:* \(\mathbb{F}_2\) rank must be computed exactly (no floating-point Gaussian elimination); a near-singular real matrix says nothing about the \(\mathbb{F}_2\) rank.
- *Weight assumptions:* the annihilator-matrix row count is \(\mathrm{wt}(f)\), which changes if balancedness is dropped - keep the balancedness constraint explicit in the encoding.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every \(\mathrm{AI}\) is from an exact \(\mathbb{F}_2\) rank computation; every nonlinearity from a recomputed Walsh spectrum; every FAA profile from exact degree tests; every nonexistence from a DRAT/LRAT proof or certified exhaustion. No floating point in a load-bearing step.
2. **Independent verification.** Two independently written annihilator-rank testers agree on every \(\mathrm{AI}\); two Walsh transforms agree on every spectrum; every DRAT/LRAT proof is replayed by a separate checker; every symmetry-class orbit count is confirmed two ways; every FAA \((e,d)\) verdict is recomputed by a second rank routine.
3. **Reproducibility.** Record the variable/monomial ordering, class definition, all encodings, and tool versions (SageMath, GAP, nauty, solvers), with a SHA-256 manifest over every truth table, annihilator matrix, Walsh spectrum, CNF, and proof. Cite the baseline (Carlet–Feng / Tu–Deng) values being matched or beaten (value, authors, source, access date). Archive the full truth table and the full FAA \((e,d)\) table of every record-level function.
4. **Preservation.** All AI-test, search, enumeration, and FAA-profile source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson). The heuristic explorers count as source even though their output is exactly re-verified.
5. **Honest reporting.** The report states up front the full profile \((\mathrm{AI},\mathrm{nl},\deg,\text{FAA})\) of any exhibited function, whether an *optimal value* was determined (with a matching bound) or only a *record improved*, and in which class any completeness claim holds. An optimal-\(\mathrm{AI}\) function with an unrecorded or weak FAA/nonlinearity profile is never presented as a simultaneously-optimal filtering function.

Calibration for the session lead: the realistic product is P1–P3 - a validated annihilator-rank and FAA toolchain, a reproduced Carlet–Feng/Tu–Deng profile, and a certified within-class maximum or improvement - plus, with luck, a full-profile witness (P4) or a small-\(n\) exact optimum. Determining the exact maximum nonlinearity of balanced optimal-\(\mathrm{AI}\) functions for a given \(n\) (with a matching bound) is a hard, publishable result; a one-sided record improvement is the common, still-valuable outcome and is labelled as such.
