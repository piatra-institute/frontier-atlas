# PROMPT FOR RIGOROUS AVALANCHE EXPONENTS AND THE IDENTITY SCALING LIMIT OF THE 2D ABELIAN SANDPILE

## The Bak–Tang–Wiesenfeld sandpile on $\mathbb Z^2$: exact algebraic structure versus the unproven avalanche exponent, and the fractal identity element of the sandpile group

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 24 of 50 (Tier 2)
**Source:** top-50 list #31, category C (exactly solvable models and lattice statistics)
**Modes:** `[proof]` `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Abelian sandpile is the rare critical model whose algebra is completely exact - Dhar's operator formalism (1990), the burning bijection to spanning trees, determinant formulas for the group order - while its headline observable, the avalanche-size exponent $\tau$, has no rigorous value and arguably no proven existence: numerics place area-exponent values near $1.25$–$1.27$ under conventions that vary across papers, with persistent claims of multifractal violations of simple scaling.

In parallel, the identity element of the sandpile group on $n\times n$ squares displays a striking, unexplained fractal architecture. Scaling-limit technology exists for the *single-source* sandpile (Pegden–Smart; Levine–Pegden–Smart Apollonian structure - note that work concerns the sandpile PDE on $\mathbb Z^2$, not the identity), but the identity's limit is open. Height probabilities are the success story - Majumdar–Dhar and Priezzhev, made rigorous through Kenyon–Wilson and Poghosyan–Priezzhev–Ruelle - proof that exact-to-rigorous conversion is possible in this model. This prompt drives at certified identity computations at scale, exact height-correlation extensions with integer-relation mining, exactly stationary avalanche sampling via Wilson's algorithm, and rigorous exponent inequalities.

The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Model and conventions (fixed for the whole project)

- Domain $\Lambda_n=\{1,\dots,n\}^2\subset\mathbb Z^2$; toppling matrix $\Delta$ = graph Laplacian: $\Delta_{xx}=4$, $\Delta_{xy}=-1$ for nearest neighbors $x\sim y$ in $\Lambda_n$; grains falling off the boundary go to a sink (wired boundary).
- Configurations $\eta:\Lambda_n\to\mathbb Z_{\ge0}$; *stable* means $\eta\le3$ pointwise. **Heights take values in $\{0,1,2,3\}$** - this convention, not $\{1,\dots,4\}$, is fixed here.
- Toppling at $x$: $\eta\mapsto\eta-\Delta e_x$, legal when $\eta(x)\ge4$; stabilization $\eta^\circ$ is well defined and order-independent (Dhar 1990).
- Addition operators $a_x\eta=(\eta+e_x)^\circ$ commute on recurrent states; the recurrent set $\mathcal R_n$ (Dhar's burning test) satisfies $|\mathcal R_n|=\det\Delta$ and forms the abelian sandpile group $G_n$, with identity $e_n\in\mathcal R_n$.
- Burning test, stated: a stable $\eta$ is recurrent iff the following burns every site - repeatedly delete ("burn") any site whose height strictly exceeds its number of unburnt neighbors, starting from the sink; the burning order defines the spanning-tree edge choices of the Majumdar–Dhar bijection. Both the test and the bijection must be re-proven in the session report before use.
- The stationary measure $\mu_n$ of the add-at-random-site chain is uniform on $\mathcal R_n$; via the burning bijection (Majumdar–Dhar 1992) it maps to uniform spanning trees; $\mu_n\to\mu$ weakly on $\mathbb Z^2$ (Athreya–Járai 2004).
- The identity $e_n$ is the unique recurrent configuration with $e_n\oplus\eta=\eta$ for all recurrent $\eta$, where $\oplus$ is pointwise addition followed by stabilization. Its height field exhibits the unexplained fractal pattern structure targeted by Q2.

### 1.2 Avalanches and exponent conventions

- Sample $\eta\sim\mu_n$, add one grain at the center $o$, stabilize. Record: $S$ = number of topplings with multiplicity; $A$ = number of distinct toppled sites; $R$ = radius of the toppled set.
- Convention fixed here: *density* exponents, $\mathbb P(A=a)\asymp a^{-\tau_A}$ and $\mathbb P(S=s)\asymp s^{-\tau_S}$ in the limit $n\to\infty$ first, then $a,s\to\infty$ - if such laws exist.
- Any comparison with literature values must first translate conventions (cumulative vs density; $\{0..3\}$ vs $\{1..4\}$; grain at center vs uniform). Convention drift is a documented source of contradictory published numbers; every reported exponent in the session carries its convention tag.

### 1.3 Open problems

1. **(Q1) Avalanche exponents.** Prove existence of $\tau_A$ (or $\tau_S$) on $\mathbb Z^2$ and determine its value - or prove that no simple power law holds (multifractal scaling, cf. De Menech–Stella–Tebaldi 1998 claims - verify).
2. **(Q2) Identity scaling limit.** Prove that $e_n$, viewed as $\bar e_n(x)=e_n(\lceil nx\rceil)$ on $[0,1]^2$, converges as $n\to\infty$ in the local-pattern/weak-$*$ sense - convergence of pattern-frequency measures on every open set; this topology is fixed as part of the statement - and characterize the limit's piecewise-periodic structure.

### 1.4 Wave decomposition (fixed terminology)

- An avalanche started at $o$ decomposes into *waves*: repeatedly topple $o$ once and let the rest of the lattice relax without re-toppling $o$; the $k$-th relaxation is the $k$-th wave (Ivashkevich–Ktitarev–Priezzhev ~1994).
- Each wave topples a set of sites exactly once; waves are the objects behind the LERW-based exponent predictions (the last-wave $11/8$ claim).
- Sessions must keep wave statistics and avalanche statistics in separate ledgers; conflating wave exponents with avalanche exponents is a known failure mode of the literature.

### 1.5 Exact inputs (to be re-derived, never assumed)

- Expected topplings: $\mathbb E_{\mu_n}[S]$ for a grain at $x$ is given exactly by Green-function sums (Dhar 1990) and diverges logarithmically - any claimed $\tau_S$ must be consistent with the exact moment identities.
- Height probabilities under $\mu$: closed forms in $1/\pi$, e.g.
\[
\mathbb P(\eta(o)=0)=\frac{2}{\pi^2}-\frac{4}{\pi^3}
\]
(Majumdar–Dhar 1991); all four heights now rigorous (Kenyon–Wilson ~2011–2015; Poghosyan–Priezzhev–Ruelle 2011 - verify the attribution split).

## 2. Complete-resolution standard

- **Q1 resolved:** a theorem for the infinite-volume stationary sandpile on $\mathbb Z^2$ establishing either a power law $\mathbb P(A=a)=a^{-\tau_A+o(1)}$ with exact or rigorously characterized $\tau_A$, or a proven violation of simple scaling - with all limits (infinite volume, tail) handled explicitly, never interchanged silently.
- **Q2 resolved:** existence of the identity's scaling limit in the fixed topology plus an explicit characterization of the limit object (e.g. via the Levine–Pegden–Smart superharmonic-matrix pattern classification).
- Either alone resolves its half of the prompt.

**Not accepted as resolution:**

- Numerical exponent estimates at any lattice size, including in-session ones; finite-size collapse plots.
- Wave-decomposition or LERW-based heuristics for $\tau$ (Ivashkevich–Ktitarev–Priezzhev lineage) without full proof; conditional statements must be labeled conditional.
- Mean-field or high-dimensional results presented as $d=2$ results (verify the current high-$d$ rigorous scope; none of it transfers).
- Single-source scaling-limit results (Pegden–Smart; Levine–Pegden–Smart) represented as the identity limit or as avalanche statements: that technology's scope is the sandpile PDE for point sources, and the gap must be stated, not blurred.
- Pattern catalogs of $e_n$ at finite $n$, however large, presented as a limit theorem.
- Any exponent claim that omits its convention translation table.

## 3. Graded partial-result targets

**P1 - certified identity computations at scale.**
Compute $e_n$ exactly for $n$ up to $\ge2048$ (stretch: 4096) via a stated group-theoretic algorithm (e.g. stabilizing suitable multiples of the maximal configuration) proven correct from Dhar's axioms in the report. Certify $e_n\oplus e_n=e_n$ and burning-test recurrence by machine check; independent Python recomputation for $n\le256$. Deliver raw arrays plus pattern-region statistics - area fractions of each periodic pattern, matched against the Levine–Pegden–Smart pattern library (verify applicability).
*Certificate:* arrays, idempotence/recurrence checks, dual implementation, SHA-256 manifest.

**P2 - exact height statistics, extended.**
Re-derive the four height probabilities on finite grids by exact rational linear algebra (Green-function minors via Matrix-Tree / Kenyon–Wilson local-event calculus; FLINT exact LU for $n\le64$), extrapolating against the known $1/\pi$ closed forms. Then extend: exact two-site joint height correlations at distances $r\le8$, with PSLQ/LLL mining of closed forms in the known structure class $\mathbb Q[1/\pi]$, verified to 100+ digits with Arb. New proven or certificate-backed correlation formulas are publishable.
*Certificate:* exact rationals; mined identities with precision statements; re-verification scripts.

**P3 - exactly stationary avalanche data.**
Sample $\eta\sim\mu_n$ *exactly*: Wilson's algorithm on the spanning-tree side plus the burning bijection (prove the bijection chain used) - no equilibration error, a decisive methodological point. Generate avalanche ensembles at $n\in\{512,\dots,8192\}$ with $\ge10^8$ avalanches at moderate sizes; publish $S,A,R$ histograms under a documented statistical protocol; moment checks against the exact $\mathbb E[S]$ identities; explicit tests of simple scaling versus multifractality (moment-ratio flows across scales, not collapse plots alone). Record wave counts per avalanche separately, per section 1.4. Ground-truth data, labeled nonrigorous as to exponents.
*Certificate:* seeds, code, raw histograms, protocol document.

**P4 - rigorous moment and tail inequalities.**
Convert exact identities into theorems: from $\mathbb E[S]\asymp\log n$ (rigorous via Green functions) derive, under explicitly stated tail hypotheses, constraints linking $\tau_S$ to cutoff exponents; reproduce, then attempt to sharpen, the known rigorous tail bounds for $\mathbb Z^2$ avalanches (Bhupatiraju–Hanson–Járai ~2017 - verify exact statements). Any new unconditional inequality for $\mathbb P(A\ge a)$ or $\mathbb P(S\ge s)$ on $\mathbb Z^2$ is publishable.
*Certificate:* complete proofs; any computation-assisted step in exact arithmetic with an independent checker.

**P5 - rigorous identity structure.**
Prove any nontrivial structural statement about $e_n$ as $n\to\infty$: existence of the observed central region with asymptotically full-density periodic pattern; convergence along subsequences via compactness plus Pegden–Smart-type odometer arguments; or rigorous consequences of the harmonic-dynamics picture (Lang–Shkolnikov 2019 - verify what it yields for the identity specifically).
*Certificate:* proof text plus supporting exact computations.

**P6 - strongest short of resolution.**
Existence of $\tau_A$ along a subsequence with rigorous nontrivial bounds $1<\tau_A^-\le\tau_A\le\tau_A^+<2$; or the identity scaling limit for a one-parameter subfamily of domains.

Honest calibration: Q1 in full is a major open problem entangled with LERW exponents and the non-locality of avalanches; Q2 in full likely needs new PDE-style technology beyond the single-source theory. P1–P3 are certain deliverables; P4–P5 are where a genuine advance is plausible.

## 4. Known results and prior art

- Foundations: Bak–Tang–Wiesenfeld 1987; Dhar 1990 (abelian property, burning test, $\det\Delta$, exact expected topplings); Majumdar–Dhar 1991 (height-0 probability), 1992 (burning bijection).
- Height probabilities: Priezzhev 1994 (remaining heights, physics-exact); Jeng–Piroux–Ruelle 2006 (reduction to one unknown constant); Poghosyan–Priezzhev–Ruelle 2011 (the constant); Kenyon–Wilson ~2011–2015 (rigorous local-event calculus via trees/groves); Caracciolo–Sportiello contributions (verify).
- Field-theoretic / logarithmic-CFT correlation predictions: Ruelle and school, 2000s–2010s (verify which pieces are rigorous).
- Rigorous field-convergence results adjacent to Q1: scaling limits of the height-one field and related local fields (Dürre ~2009; later work by Kassel–Wilson-adjacent authors - verify precise statements before use).
- Infinite volume and rigor: Athreya–Járai 2004 (stationary measure limit); Járai–Redig ~2008 (avalanches in higher $d$); Járai's survey ~2018; rigorous tail inequalities on $\mathbb Z^d$ including partial $d=2$ results: Bhupatiraju–Hanson–Járai ~2017 (verify scope); high-dimensional/mean-field literature (verify current state - no transfer to $d=2$).
- Avalanche phenomenology: wave decomposition, Ivashkevich–Ktitarev–Priezzhev ~1994–1996; last-wave/LERW connection and the $11/8$ prediction via LERW dimension $5/4$ - rigorous LERW anchors: Kenyon 2000; Lawler–Schramm–Werner 2004 (SLE$_2$).
- Multifractal-scaling claims: De Menech–Stella–Tebaldi 1998; Tebaldi–De Menech–Stella 1999 (verify); reported area exponents cluster in $1.25$–$1.27$ with convention caveats - verify each source's convention before quoting any number.
- Patterns and limits: Ostojic 2003 (single-source patterns, heuristic); Pegden–Smart 2013 (single-source scaling limit via viscosity solutions); Levine–Pegden–Smart ~2016–2017 (Apollonian structure, integer superharmonic matrices - scope: the sandpile PDE on $\mathbb Z^2$).
- Identity structure: Le Borgne–Rossin ~2002 (partial characterizations - verify); Caracciolo–Paoletti–Sportiello ~2008–2012 (strings and patterns); Lang–Shkolnikov 2019 (harmonic dynamics of sandpiles, PNAS).
- Surveys and general theory: Holroyd–Levine–Mészáros–Peres–Propp–Wilson 2008 (chip-firing and rotor-routing); Levine–Propp 2010 (AMS Notices survey); Redig's lecture notes ~2005 (verify).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

### 5.1 `[sym]` Identity engine

- C++ stabilization: `uint8` height grid, FIFO toppling queue, 64-bit toppling counters; identity via a proven group-theoretic recipe (state and prove it from the axioms - no folklore shortcuts).
- Cost scales super-linearly (total topplings for $e_n$ empirically grows like a power of $n$ above cubic in wall-clock-relevant terms - measure and report); checkpoint long runs.
- Independent Python/NumPy implementation to $n=256$.
- Expected failure mode: correctness-by-folklore of identity algorithms - every recipe used must be derived in the report.

### 5.2 `[sym]` Exact tree calculus

- FLINT `fmpq_mat` for exact Green minors on grids up to $n=64$ (the $n^2\times n^2$ exact LU is hours, not days).
- Implement the Kenyon–Wilson determinant rules for local height/correlation events; verify against the four known probabilities; then extend to pair correlations at $r\le8$.
- Arb plus mpmath PSLQ for closed-form mining in the $\mathbb Q[1/\pi]$ class; every mined identity re-verified at doubled precision before being reported.

### 5.3 `[sym]` Exactly stationary sampling

- Wilson's algorithm (loop-erased walks) for exact UST samples; burning bijection to recurrent configurations; Philox counter-based RNG with logged seeds; avalanche driver shared with the P1 engine.
- Expected failure mode: finite-size and logarithmic corrections contaminating exponent readouts - mandate multi-scale effective-exponent analysis and report stability, never a single fitted number.

### 5.4 `[proof]` Inequalities

- Start from the exact moment identities (Dhar) and tail arguments on the spanning-tree side (FKG-type, Markov-type); target shapes: "polynomial lower bound on $\mathbb P(A\ge a)$" and "nontrivial upper bound with explicit exponent."
- Expected failure mode: avalanche non-locality defeats naive tree-surgery arguments - document precisely where; that delimitation is itself a deliverable on Q1's difficulty.

### 5.5 Resource budget

- All computations fit a single workstation: 64 GB suffices for P1/P2/P4; P3 wants weeks of CPU and is embarrassingly parallel across seeds.
- Checkpoint every long stabilization; identity runs at $n=4096$ are restartable from odometer snapshots.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Identity arrays are exact integers; height/correlation computations exact rationals; mined closed forms carried with Arb enclosures and stated precision; simulation outputs are statistical data, clearly separated and never presented as certification.
2. **Independent verification.** Dual implementations (C++/Python) of stabilization and the burning test; an independent checker verifying $e_n\oplus e_n=e_n$ and recurrence from stored arrays alone; exact-linear-algebra results re-derived in SageMath at $n\le32$.
3. **Reproducibility.** All seeds, lattice sizes, conventions (the $\{0..3\}$/density-exponent table from section 1.2), and tool versions recorded; SHA-256 manifest over arrays, histograms, certificates, and source.
4. **Preservation.** Engines, checkers, mining logs (including failed PSLQ bases), and abandoned P4/P5 proof attempts are part of the record; unpreserved work must be declared.
5. **Honest reporting.** The final report opens by stating that Q1 and Q2 remain open (unless actually resolved to the section-2 standard); every exponent number carries its convention and status tag (rigorous / conditional / numerical); and no pattern catalog, data set, or single-source-theory citation is represented as resolving the identity limit or the avalanche exponent.
