# PROMPT FOR THE EXACTNESS FRONTIER OF PERCOLATION CRITICAL POLYNOMIALS

## Scullard–Ziff–Jacobsen critical polynomials: proving a prediction exact, or delimiting the solvable class, and the closed-form question for the square-site threshold

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 04 of 50 (Tier 1)
**Source:** top-50 list #27, category C (exactly solvable models and lattice statistics)
**Modes:** `[sym]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The critical-polynomial method assigns to every finite torus-embedded basis $B$ of a periodic planar lattice an integer polynomial $P_B(p)$ whose root in $(0,1)$ reproduces, exactly and for every basis, all rigorously known bond thresholds (square $p_c=1/2$, Kesten 1980; triangular and honeycomb via star–triangle, Wierman 1981), and on unsolved lattices (kagome bond, $(4,8^2)$, square site, …) produces basis-dependent roots that converge to the numerically observed threshold astonishingly fast - Jacobsen's transfer-matrix implementations give 10+ digits.

No one has proved either that some such prediction on an unsolved lattice is exact, or a theorem explaining why exactness holds precisely on the self-dual/triangle-type class and cannot extend. This prompt targets both: (A) an exactness/dichotomy theorem, and (B) a closed form or a certified conditional-exclusion statement for the square-site threshold $p_c\approx0.59274605\ldots$

The problem is matched to current AI methods because every object involved is a finite, exactly computable polynomial, the rigorous toolkit (duality, star–triangle, substitution bounds) is crisp, and every intermediate claim is machine-certifiable in exact arithmetic. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Lattice and percolation conventions

- A *periodic planar lattice* $\mathcal L=(V,E)$ is an infinite, locally finite, connected graph embedded in $\mathbb R^2$, invariant under a rank-2 translation lattice $\Lambda\cong\mathbb Z^2$, with finite quotient.
- Bond percolation: on the probability space $(\{0,1\}^E,\mathcal F,\mathbb P_p)$ each edge is *open* independently with probability $p\in[0,1]$.
- $\theta(p)=\mathbb P_p(0\leftrightarrow\infty)$ (origin in an infinite open cluster; a vertex-transitive representative is fixed once per lattice). The threshold is
\[
p_c(\mathcal L)=\sup\{p:\theta(p)=0\}.
\]
- Site percolation is defined analogously on $\{0,1\}^V$, threshold $p_c^{\mathrm{site}}$.

### 1.2 Basis and critical polynomial

- A *basis* $B$ is the finite quotient graph of $\mathcal L$ by a finite-index sublattice $\Lambda'\le\Lambda$, embedded on the torus $\mathbb T^2=\mathbb R^2/\Lambda'$.
- For a bond configuration $\omega$ on $E(B)$, classify open clusters by homology on $\mathbb T^2$ and define
\[
E_2=\{\text{some open cluster wraps both fundamental cycles}\},\qquad
E_0=\{\text{no open cluster wraps either cycle}\}.
\]
- The *critical polynomial* of the basis is
\[
P_B(p)\;=\;\mathbb P_p(E_2)\;-\;\mathbb P_p(E_0),
\]
an integer-coefficient polynomial of degree $\le|E(B)|$ in $p$.
- An equivalent deletion–contraction definition is used by Jacobsen 2014 (verify equivalence); adopt one definition and prove agreement on every basis used.
- Empirically $P_B$ has a unique root $p_B\in(0,1)$; uniqueness must be certified per basis (Sturm sequences in exact arithmetic), never assumed.
- Site versions replace edge states by vertex states with the same homological classification.

### 1.3 What is known to be exact, and what is not

- Square lattice: every basis gives $P_B(1/2)=0$ by self-duality.
- Triangular/honeycomb: the roots of $p^3-3p+1$ (i.e. $p_c^{\triangle}=2\sin(\pi/18)$) and the complementary honeycomb value are exact for every basis.
- More generally, exactness holds for lattices decomposable into self-dual arrangements of triangle-type cells (Ziff–Scullard 2006; Wierman–Ziff ~2011 - verify scope).
- On lattices outside this class (kagome bond, $(4,8^2)$ bond, square site), $p_B$ depends on $B$: the root sequence is nonconstant, so at most one basis value can equal $p_c$.
- The convergence $p_B\to p_c$ as the basis grows is **unproven** on any unsolved lattice. It must never be assumed.

### 1.4 Question A (exactness dichotomy)

Prove one of:

- **A1.** For a specific unsolved lattice (kagome bond is the canonical target), $p_c$ equals the root in $(0,1)$ of an explicitly stated integer polynomial, with full proof.
- **A2.** A theorem characterizing exactly the class of periodic planar lattices for which $p_B$ is independent of the basis $B$, proving both inclusion and exclusion, together with a rigorous statement relating the basis-dependent root sequence to $p_c$ on excluded lattices - at minimum a proven inequality or error bound valid for all sufficiently large bases.

### 1.5 Question B (square-site closed form)

Reference value: $p_c^{\mathrm{site}}(\mathbb Z^2)=0.59274605079210(2)$ (Jacobsen 2015 - verify digits and error bar). Produce one of:

- **B1.** An exact closed form - an algebraic number with explicit minimal polynomial, or an explicit expression in standard constants - with a complete proof of equality.
- **B2.** A certified conditional exclusion: "if $p_c^{\mathrm{site}}(\mathbb Z^2)$ lies in the stated numerical interval $I$, then it is not a root of any integer polynomial of degree $\le D$ and height $\le H$", for explicit $(I,D,H)$, with LLL/PSLQ certificates.
- Note carefully: no rigorous high-precision enclosure of $p_c^{\mathrm{site}}(\mathbb Z^2)$ exists - the best rigorous interval is of order $[0.556,\,0.680]$ (van den Berg–Ermakov 1996 lower; Wierman 1995 upper; verify both). B2 is therefore intrinsically conditional on the numerical interval and must be labeled as such.

## 2. Complete-resolution standard

Complete resolution means at least one of the following, in full:

1. **A1 met:** an explicit $Q\in\mathbb Z[p]$, a certified unique root in the physical interval, and a proof that it equals $p_c$ of a named, not previously solved lattice, using only rigorous probabilistic/combinatorial arguments (duality, star–triangle/substitution couplings, sharp-threshold theorems); self-contained or citing only proven results.
2. **A2 met:** the two-sided characterization theorem for basis-independence, plus the rigorous root-vs-threshold statement on the excluded class, with definitions exactly as in section 1.
3. **B1 met:** the exact value of $p_c^{\mathrm{site}}(\mathbb Z^2)$ with proof. (A transcendence or non-algebraicity proof would also resolve B but is judged beyond current technology; say so if attempted.)

**Not accepted as resolution:**

- Numerical agreement of $p_B$ with a threshold to any number of digits, on any sequence of bases.
- The observation that the root sequence converges, or fitted convergence rates, without proof that the limit is $p_c$.
- Exactness arguments conditional on conformal invariance, universality, or unproven properties of the Potts critical manifold.
- A PSLQ/LLL null search represented as an impossibility theorem - only the conditional form B2, with explicit $(I,D,H)$, counts as a result.
- New unproven predictions for further lattices, however precise.
- Transfer of bond-duality arguments to site problems by analogy; site percolation has no proven star–triangle mechanism of the required kind, and any such claim needs full proof.
- Any argument that assumes $p_B\to p_c$; this convergence is itself open (targets A2/P7).

## 3. Graded partial-result targets

**P1 - verified toolchain on the known frontier.**
Implement critical polynomials in exact arithmetic and reproduce the rigorous cases: for at least three inequivalent bases each of square, triangular, and honeycomb bond ($\le24$ edges), certify that $P_B$ vanishes at the exact threshold - exact polynomial division at $p=1/2$; exact resultant/factor checks against $p^3-3p+1$ for the star–triangle pair.
*Certificate:* the polynomials, an independent brute-force $2^{|E|}$ evaluation in a second language, and the divisibility/resultant computations, all reproducible from a manifest.

**P2 - reproduce the unsolved-lattice frontier.**
Reproduce Jacobsen-scale critical polynomials for kagome bond, $(4,8^2)$ bond, and square site on growing bases; isolate roots with certified interval arithmetic (Arb) to $\ge30$ digits; tabulate against published values (Jacobsen 2014/2015 - verify).
*Certificate:* exact polynomial coefficients, certified root enclosures, dual-implementation agreement.

**P3 - nonconstancy theorems.**
Prove, by exact computation, that on kagome bond the roots for the computed basis family are pairwise distinct - "the critical-polynomial prediction is basis-dependent at all computed sizes" - hence at most one computed prediction can be exact. Extend the exact convergence table beyond published sizes if feasible.
*Certificate:* exact sign changes of $P_B(p_{B'})$ in rational arithmetic.

**P4 - rigorous threshold bounds.**
Implement the substitution method (Wierman; May–Wierman) with exact rational computation of the coupling inequalities; reproduce and, if possible, tighten the rigorous kagome bond interval (May–Wierman ~2005, roughly $[0.5209,0.5291]$ - verify) and the square-site interval. Any tightening of a published rigorous bound is publishable.
*Certificate:* exact inequalities plus an independent checker of the substitution partition computations.

**P5 - grow the rigorously solved class.**
Machine-generate and verify the catalogue of periodic lattices with $\le N$ edges per fundamental domain decomposable into self-dual triangle-type hypergraph arrangements (Ziff–Scullard 2006; Wierman–Ziff - verify), each entry yielding a rigorous exact threshold with proof; flag any lattice whose exact threshold has not appeared in the literature.
*Certificate:* per-lattice proof object - the decomposition plus the star–triangle identity verified in exact arithmetic.

**P6 - conditional exclusion for the square-site value.**
Run LLL/PSLQ against the best available digits of $p_c^{\mathrm{site}}(\mathbb Z^2)$; state the strongest supportable conditional exclusion in form B2. Honest calibration: with ~12–13 published digits the excluded $(D,H)$ region is small; report exactly what the input precision supports and no more.
*Certificate:* reduced-lattice certificates re-checkable by an independent LLL implementation.

**P7 - strongest short of resolution.**
A rigorous error bound $|p_B-p_c|\le f(B)\to0$, for any explicit $f$ and any lattice family - even a restricted one - would be the first convergence theorem for the method. Document all obstructions encountered; the expected obstruction (no route from finite-basis homology counts to $p_c$ without new probabilistic input) is itself part of the A2 delimitation.

Full resolution (A1/A2/B1) is genuinely unlikely in one session; P3–P5 are realistic and independently valuable, P7 is the stretch goal.

## 4. Known results and prior art

- Kesten 1980: $p_c(\mathbb Z^2,\text{bond})=1/2$. Wierman 1981: triangular/honeycomb bond via star–triangle, making the Sykes–Essam 1964 values rigorous.
- Scullard 2006 and Ziff 2006: triangle–triangle transformation, generalized cell/dual-cell method.
- Ziff–Scullard 2006–2010: predictions for kagome, $(4,8^2)$, $(3,12^2)$ and other Archimedean lattices.
- Wierman–Ziff ~2011: self-dual planar hypergraphs and exact bond thresholds (verify exact statement and scope).
- Wu 1979: conjectured kagome bond value $\approx0.52443$; refuted numerically (Scullard–Ziff; Feng–Deng–Blöte 2008).
- Scullard–Jacobsen 2012–2013: transfer-matrix critical polynomials.
- Jacobsen 2014: kagome bond $p_c=0.52440499916744$ (approximate - verify digits) and many other lattices.
- Jacobsen 2015: extension to site problems; square site $p_c=0.59274605079210(2)$ (verify).
- Grimmett–Manolescu 2013–2014: bond percolation on isoradial graphs via star–triangle couplings - the strongest rigorous star–triangle technology currently available.
- Rigorous bounds: Wierman substitution method (1990–2003); May–Wierman ~2005 kagome interval (verify); van den Berg–Ermakov 1996 square-site lower bound $\approx0.556$ (verify); Wierman 1995 square-site upper bound $\approx0.6795$ (verify).
- Riordan–Walters 2007: rigorous confidence-interval computations (Monte Carlo with rigorous error statements; distinct from deterministic bounds).
- Convergence of $p_B$ to $p_c$: empirically fast (roughly polynomial in inverse basis size with a large power - verify Jacobsen's stated rates); no rigorous convergence result is known.

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

### 5.1 `[sym]` Exact computation of $P_B$

- Custom C++ transfer matrix over torus-homology-tracked connectivity states (non-crossing partitions augmented with winding data); coefficients in $\mathbb Z[p]$ via FLINT `fmpz_poly`.
- Independent Python/SymPy brute force summing all $2^{|E|}$ configurations for $|E|\le26$ - the mandatory dual implementation.
- Feasibility: state-space growth is Catalan-like ($\sim4^w$ in basis width $w$); a single workstation handles widths ~14–20 sites and polynomial degrees to a few hundred.
- Expected failure modes: homology bookkeeping errors on the torus (caught by the brute-force cross-check); coefficient blowup (use FLINT, not naive bignums); non-uniqueness of the root in $(0,1)$ for pathological bases (certify with Sturm sequences).

### 5.2 `[sym]` Root isolation and closed-form search

- Arb for certified enclosures with directed rounding.
- Pari/GP `lindep` and mpmath PSLQ for Question B against published digits; never exceed input precision; log every candidate tested and the exclusion region achieved.

### 5.3 `[proof]` Rigorous track

- Substitution-method bounds as exact computations: the partition-lattice couplings reduce to finitely many exact rational inequalities; implement with exact arithmetic and an independent checker.
- Formalize the triangle-type exactness catalogue (P5): each entry is a finite star–triangle identity, verifiable by computer algebra (SymPy/SageMath polynomial identities).
- For P7, attempt to combine Grimmett–Manolescu isoradial couplings with finite-basis data. Expected failure mode: homology probabilities on a finite torus do not control infinite-volume crossing probabilities without an unproven RSW-type input - document exactly where the argument breaks; that delimitation feeds A2.

All heavy runs fit a single workstation ($\le64$ GB RAM); nothing requires clusters. Floating point is for exploration only.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Every polynomial coefficient in $\mathbb Z$; every root enclosure an Arb ball with stated radius; every inequality in P4/P5 over $\mathbb Q$. Floating-point output appears only in exploratory tables marked as such.
2. **Independent verification.** Brute-force $2^{|E|}$ Python checker for every basis with $|E|\le26$; C++ and Python/Sage dual implementations of the transfer matrix; an LLL-certificate re-checker independent of the search code. Checkers must be small enough to audit by hand.
3. **Reproducibility.** Manifest of all bases (adjacency plus embedding data), lattice definitions, and tool versions; SHA-256 manifest over every polynomial file, certificate, and script.
4. **Preservation.** Transfer-matrix source, brute-force checkers, substitution-method code, and all failed exactness attempts are part of the record; anything discarded must be listed as discarded, not silently dropped.
5. **Honest reporting.** The final report opens with an explicit statement of whether A1, A2, B1, or B2 was met (expected: none in full; P-targets only), and never presents numerical agreement, conditional exclusions, or convergence observations as resolution of the problem.
