# PROMPT FOR THE HARD-SQUARES ENTROPY CONSTANT

## The growth rate of independent sets on the square grid

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 12 of 50 (Tier 2)
**Source:** top-50 list #23, category C (exactly solvable models and lattice statistics)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The hard-squares entropy constant $\kappa\approx1.5030480824753\ldots$ is the exponential growth rate of the number of independent sets on the $n\times n$ grid graph. Baxter solved the neighbouring hard-hexagon model exactly in 1980 - its growth constant is algebraic, with Rogers–Ramanujan structure - while hard squares, apparently just as natural, has no known closed form and no proof that none exists. The constant is computable to high precision (corner-transfer-matrix numerics), and the finite-width objects are exact integer linear algebra, so the problem is ideally matched to symbolic mining: certified interval enclosures from our own toolchain, integer-relation sweeps with honest multiple-testing accounting, and structure mining of transfer-matrix spectra. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution. Full resolution - a closed form, or proof machinery for its absence - is unlikely; the graded targets are the goal.

## 1. Exact problem statement

### 1.1 Objects

For $m,n\ge1$ let $G_{m,n}$ be the grid graph with vertex set $\{1,\dots,m\}\times\{1,\dots,n\}$ and edges between points at Euclidean distance 1 (free boundary conditions; no wraparound). Let $i(m,n)$ be the number of independent sets in $G_{m,n}$ - sets of vertices spanning no edge; the empty set counts. Equivalently, $i(m,n)$ counts configurations of the hard-square lattice gas at activity $z=1$.

### 1.2 The constant

By subadditivity (to be proved in-session as part of P1) the limit

\[
\kappa=\lim_{m,n\to\infty} i(m,n)^{1/(mn)}
\]

exists; numerically $\kappa=1.5030480824753322\ldots$ (corner-transfer-matrix value; verify digits). Write $h=\log\kappa$ for the entropy.

### 1.3 Transfer-matrix conventions (fixed)

For width $n$, let $S_n\subseteq\{0,1\}^n$ be the binary strings with no two adjacent 1s, so $|S_n|=F_{n+2}$ (Fibonacci). The transfer matrix $T_n$ is the $|S_n|\times|S_n|$ 0/1 matrix with

\[
T_n(u,v)=1\iff u\wedge v=0\quad(\text{componentwise product zero: rows }u,v\text{ may be vertically adjacent}),
\]

so that $i(m,n)=\mathbf{1}^{T}T_n^{\,m-1}\mathbf{1}$. $T_n$ is symmetric, nonnegative, primitive; let $\Lambda_n>0$ be its Perron eigenvalue. Standard facts, to be re-proved in-session before use (P1):

- $\lim_m i(m,n)^{1/m}=\Lambda_n$;
- $\Lambda_{n_1+n_2}\le\Lambda_{n_1}\Lambda_{n_2}$ (restriction of configurations to sub-strips);
- $\Lambda_{n_1+n_2+1}\ge\Lambda_{n_1}\Lambda_{n_2}$ (insert an empty separating column);
- consequently, for every $n$,

\[
\Lambda_n^{1/(n+1)}\;\le\;\kappa\;\le\;\Lambda_n^{1/n},
\qquad
\kappa=\lim_n\Lambda_n^{1/n}=\inf_n\Lambda_n^{1/n}.
\]

The faster-converging Calkin–Wilf eigenvalue-ratio sandwiches are to be re-derived and machine-verified before use. Cylinder (periodic) transfer matrices $T_n^{\mathrm{per}}$ - same definition with index $n$ on a cycle - may be used only with their own proved inequalities.

### 1.4 Related objects fixed out of scope

The activity generalization $Z_{m,n}(z)=\sum_{S\ \mathrm{independent}}z^{|S|}$ and its per-site free energy $f(z)$ are permitted *tools* (all transfer-matrix statements above hold with $z$-weighted matrices $T_n(z)$), but the target constant is $\kappa=\exp f(1)$ at $z=1$ only. The critical activity $z_c\approx3.796$ of the hard-square gas, the hard-hexagon constants, and cylinder-vs-free finite-size constants are distinct objects; claims about them must be labeled as such and do not count toward any target below.

### 1.5 The open question (adopted formulation)

Determine the exact nature of $\kappa$:

1. exhibit a closed form - an algebraic number, or an explicit expression in standard constants and values of standard functions, with proof; or
2. prove that no closed form exists within a precisely delimited class - e.g. $\kappa$ is transcendental, or not algebraic of degree $\le D$ and height $\le H$ for explicit large $D,H$; or
3. failing both, advance the certified numerical and structural frontier per section 3.

Calibration contrast: the hard-hexagon growth constant at $z=1$ is a known algebraic number (Baxter 1980, triangular-lattice analogue), so possibility 1 is not absurd on its face; but hard squares lacks the Yang–Baxter structure that made hard hexagons solvable, and no solvable manifold is known to pass through the square-lattice $z=1$ point.

## 2. Complete-resolution standard

A complete resolution is one of:

- **(A)** An exact closed form for $\kappa$ with complete proof - for instance an explicit algebraic equation, or an exact expression arising from a newly solved model - plus certified numerical verification of the identity to at least 50 significant digits with the section 5 toolchain.
- **(B)** A theorem giving proof machinery for non-solvability: a precise exclusion of $\kappa$ from an explicitly defined, defensibly natural class of constants, with full proof. The class must be declared *before* the proof is attempted; post-hoc class gerrymandering is not accepted.

**Not accepted as resolution:**

- High-precision numerics alone, at any number of digits, including new records.
- A PSLQ/LLL "hit" - an integer relation matching to working precision - without an exact proof of the identity. A hit is a conjecture and must be reported with its multiple-testing-adjusted significance.
- Irrationality or non-D-finiteness *conjectures* supported by series analysis.
- Statements about the hard-square gas at other activities $z\neq1$, about hard hexagons, or about other lattices or constants of similar name, presented as statements about $\kappa$.
- Adoption of any claimed closed form from the literature without independent proof and certified verification.

## 3. Graded partial-result targets

- **P1 - Reproduce the frontier with verified code.**
  - *Task:* prove the transfer-matrix facts and sandwich inequalities of section 1.3 (short rigorous write-up); implement $T_n$ and compute $i(m,n)$ exactly for small sizes, matching OEIS grid-independent-set data; re-derive the Calkin–Wilf ratio bounds with proofs.
  - *Certificate:* proofs in the report; dual-implementation agreement on exact counts; hashes of all data.
- **P2 - Certified interval enclosure of $\kappa$.**
  - *Task:* rigorous Perron enclosures for $T_n$ (and $T_n^{\mathrm{per}}$) at the largest feasible widths via Collatz–Wielandt: for any positive vector $v$,

\[
\min_{u\in S_n}\frac{(T_nv)_u}{v_u}\;\le\;\Lambda_n\;\le\;\max_{u\in S_n}\frac{(T_nv)_u}{v_u},
\]

  evaluated in exact rational or directed-rounding interval arithmetic; combine with the proved sandwich to output $[\underline\kappa,\overline\kappa]$. Target: fully rigorous width $\le10^{-12}$, then push.
  - *Certificate:* the vector $v$, the exact ratio checks, and an independent checker re-verifying both inequalities by sparse multiplication only.
- **P3 - Rigorous high-precision value via certified extrapolation.**
  - *Task:* prove an explicit convergence-rate theorem for a ratio sequence (e.g. $\Lambda_{n+1}/\Lambda_n$ or a cylinder analogue), with certified error constants (spectral-gap based; the gap itself enclosed rigorously, e.g. from exactly computed $\mathrm{tr}\,T_n^k$); reach an enclosure of width $\le10^{-30}$, stretch $10^{-40}$ - near CTM precision but rigorous, which is rarely attempted in the literature.
  - *Certificate:* the proved error bound plus interval evaluations, independently re-run.
- **P4 - Integer-relation sweeps with honest accounting.**
  - *Task:* using $\ge50$ certified digits (from P3; non-rigorous CTM digits only for labeled exploration): PSLQ/LLL tests of $\kappa$, $\log\kappa$, $\kappa^{\pm k}$ against a *pre-declared* basis census - algebraic-number tests to stated degree/height; monomials in $\pi$, $\log2$, $\log3$, Catalan's constant, $\Gamma$-values at rationals, Dirichlet $L$-values, Rogers–Ramanujan-type evaluations - with a multiple-testing analysis (expected number of spurious relations at working precision).
  - *Certificate:* the declared census, full PSLQ transcripts, and exclusion bounds derived from certified digits. A clean negative - "$\kappa$ satisfies no algebraic equation of degree $\le20$ with coefficient height $\le10^{40}$, to the confidence implied by 60 certified digits" - is the expected valuable outcome.
- **P5 - Structure mining of the exact finite-width objects.**
  - *Task:* characteristic polynomials of $T_n$ and $T_n^{\mathrm{per}}$ for all feasible $n$: factorization over $\mathbb{Q}$, symmetry (dihedral/cyclic) decompositions, interlacing patterns, growth of the algebraic degree of $\Lambda_n$; search for persistent factors or modular patterns that would signal hidden solvable structure.
  - *Certificate:* exact polynomial data files, dual-CAS verification.
- **P6 - Non-D-finiteness program for associated generating functions.**
  - *Task:* compute the (rational) fixed-width generating functions $\sum_m i(m,n)x^m$ exactly; then attack the diagonal object $\sum_n i(n,n)x^n$: exclusion certificates ("no ODE of order $\le r$, degree $\le d$ annihilates the series to depth $N$"), and any provable statement connecting the accumulating singularities of the width-$n$ rational functions to non-D-finiteness of the diagonal. A *proof* that $\sum_n i(n,n)x^n$ is not D-finite would be a strong publishable theorem.
  - *Certificate:* exact linear-algebra transcripts; complete proofs where claimed.

## 4. Known results and prior art

- R. J. Baxter (1980): exact solution of hard hexagons; algebraic growth constants; Rogers–Ramanujan identities central. (Contrast object, not this problem.)
- R. J. Baxter, I. Enting, S. Tsang (~1980): hard-square lattice-gas studies; corner-transfer-matrix methodology (Baxter, from 1968; book 1982).
- N. Calkin, H. Wilf (1998): "The number of independent sets in a grid graph" - existence of $\kappa$ and rigorous transfer-matrix bounds; the standard starting point.
- R. J. Baxter (1999): "Planar lattice gases with nearest-neighbour exclusion" - CTM computation of the hard-square entropy constant to roughly 40 digits (verify digit count).
- Subsequent refinements of bounds and digits in the combinatorics literature (Engel-type bounds; Friedland and collaborators on entropy monotonicity; further CTM/tensor pushes) - verify the current records, rigorous and non-rigorous, before starting.
- The sequence $i(n,n)$, the fixed-width sequences, and the constant itself appear in the OEIS - use as cross-checks; verify entry numbers in-session rather than citing from memory.
- To our knowledge: no closed form, no algebraicity proof, and no transcendence proof for $\kappa$.

**Status as of mid-2026 - re-verify against current literature before starting the session.** In particular check: current record digits (rigorous and non-rigorous), any claimed closed form, and recent work on D-finiteness questions for grid independent-set sequences.

## 5. Attack plan

All single-workstation; the width frontier is memory-limited ($|S_n|=F_{n+2}$; width 30 gives dimension ≈ 2.2M - sparse matrix–vector products only, never dense storage).

1. **Exact counting layer (P1).**
   - Python/SymPy reference implementation of $T_n$ and $i(m,n)$; independent C++ (64-bit and GMP) implementation; exact comparison for $m,n\le12$ and against OEIS.
   - Failure mode: indexing/orientation mismatches between the two implementations masking as agreement - compare against a third, brute-force enumeration for $m,n\le6$.
2. **Rigorous eigenvalue layer (P2).**
   - Floating-point power iteration for an approximate Perron vector $v$ (sparse operator, widths to ~30); round $v$ to a positive dyadic/rational vector; evaluate the Collatz–Wielandt ratios exactly - GMP rationals at moderate widths, Arb directed rounding at large widths. The certificate is independent of how $v$ was found.
   - Failure mode: ratio spread stagnating from a too-coarse $v$ - increase the precision of $v$, not of the check.
3. **Extrapolation layer (P3).**
   - Prove the geometric-convergence lemma for the chosen ratio sequence; enclose the spectral gap rigorously (exact $\mathrm{tr}\,T_n^k$ for small $k$, or a second Collatz–Wielandt-style certificate on a deflated operator); assemble final intervals in Pari/GP or Arb.
   - Failure mode: provable error constants too pessimistic - report the honest rigorous interval and, separately and clearly labeled, the non-rigorous CTM-style estimate; never merge them.
4. **Relation-hunting layer (P4).**
   - Pari/GP `lindep`/PSLQ and fplll-based LLL; the test census is a version-controlled file declared before any run; every hit re-tested at ≥2× precision before being reported even as a conjecture.
5. **Structure layer (P5, P6).**
   - FLINT/Pari for exact characteristic polynomials to width ~20 (dimension ≈ 17k: Krylov/Berlekamp–Massey modulo primes + CRT reconstruction).
   - Sage ore_algebra for exclusion certificates on $\sum_n i(n,n)x^n$; diagonal terms from profile dynamic programming, feasible to roughly $n\approx25$–$30$ - this small $N$ limits the exclusion envelope; state the reached $(r,d,N)$ exactly.
   - Failure mode: reading structure into floating-point factorization artifacts - all polynomial work exact, two CAS.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All counts exact integers; all eigenvalue enclosures via exact rational Collatz–Wielandt checks or Arb directed rounding; floating-point Perron vectors are exploration inputs whose certificates are exact; no floating-point digit ever enters a reported enclosure.
2. **Independent verification.** Dual implementations (SymPy/Python vs C++/GMP) for counting; a standalone checker (~100 lines, no linear-algebra library) re-verifying each Collatz–Wielandt certificate by sparse multiply-and-compare; PSLQ hits re-verified in a second system (mpmath vs Pari/GP).
3. **Reproducibility.** All widths, precisions, seeds, and the declared PSLQ census recorded; environment (compiler, FLINT/Arb/Pari versions) frozen; SHA-256 manifest over vectors, certificates, polynomial data, and logs.
4. **Preservation.** Approximate eigenvectors, failed extrapolation ansätze, and all negative PSLQ sweeps preserved - negative sweeps are a primary deliverable, not a byproduct.
5. **Honest reporting.** The report states up front that no closed form for $\kappa$ was established (unless (A) was actually proved); rigorous and non-rigorous precision appear in separate, clearly labeled intervals; every PSLQ conjecture carries its multiple-testing accounting.
