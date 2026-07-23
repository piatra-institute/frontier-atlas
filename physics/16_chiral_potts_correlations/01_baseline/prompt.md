# PROMPT FOR CORRELATION FUNCTIONS OF THE INTEGRABLE CHIRAL POTTS MODEL

## Closing the correlation gap in the last great solved-free-energy lattice model, with the XYZ factorized-correlation program as scaffold

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 16 of 50 (Tier 2)
**Source:** top-50 list #28, category C (exactly solvable models and lattice statistics)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The integrable chiral Potts model is the outstanding case of a lattice model whose free energy (Baxter 1988–1990) and order parameters (Albertini–McCoy–Perk–Tang conjecture 1989, proven by Baxter 2005) are exactly known while its correlation functions have resisted every approach for over thirty-five years, despite a complete integrable structure - star–triangle relation, functional relations, Onsager algebra.

The obstruction is structural: the Boltzmann weights live on a rapidity curve of genus greater than one and lack the difference property underlying the vertex-operator and qKZ machinery that solved XXZ correlations (the Jimbo–Miwa tradition; the Boos–Jimbo–Miwa–Smirnov–Takeyama factorization). This prompt attacks the gap the way a symbolic-computation program can: build certified exact finite-lattice correlation data over cyclotomic number fields as ground truth, verify and extend the known form-factor conjectures, mine the exact data for closed forms with integer-relation methods, and test candidate determinant or integral representations against the data at every accessible size.

The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 The lattice model

- Fix $N\ge2$, $\omega=e^{2\pi i/N}$. Spins $\sigma_x\in\mathbb Z_N$ on the sites of the square lattice.
- Rapidities $p=(a_p,b_p,c_p,d_p)$ lie on the curve
\[
a_p^N+k'b_p^N=k\,d_p^N,\qquad k'a_p^N+b_p^N=k\,c_p^N,\qquad k^2+k'^2=1,
\]
with $0<k'<1$ in the ordered regime.
- Edge weights (conventions of Baxter–Perk–Au-Yang 1988; fix once, use everywhere):
\[
\frac{W_{pq}(n)}{W_{pq}(0)}=\prod_{j=1}^{n}\frac{d_pb_q-a_pc_q\,\omega^j}{b_pd_q-c_pa_q\,\omega^j},
\qquad
\frac{\overline W_{pq}(n)}{\overline W_{pq}(0)}=\prod_{j=1}^{n}\frac{\omega a_pd_q-d_pa_q\,\omega^j}{c_pb_q-b_pc_q\,\omega^j},
\]
$n\in\mathbb Z_N$, horizontal and vertical edges respectively; these satisfy the star–triangle relation.
- Known exactly: the partition function per site (Baxter 1988–1990) and the order parameters
\[
\langle\sigma_x^n\rangle=(1-k'^2)^{\,n(N-n)/(2N^2)},\qquad1\le n\le N-1
\]
(conjectured Albertini–McCoy–Perk–Tang 1989; proven Baxter 2005).

### 1.2 The quantum chain

The superintegrable $\mathbb Z_N$ chiral Potts chain on $L$ sites (von Gehlen–Rittenberg 1985):
\[
H(\lambda)=-\sum_{j=1}^{L}\sum_{n=1}^{N-1}\frac{1}{1-\omega^{-n}}\Big(X_j^{\,n}+\lambda\,(Z_jZ_{j+1}^{\dagger})^{n}\Big),
\]
with $Z|s\rangle=\omega^s|s\rangle$, $X|s\rangle=|s+1\bmod N\rangle$; boundary condition (periodic or open) fixed explicitly per computation. For $\lambda\in\mathbb Q$ all matrix entries lie in the cyclotomic field $\mathbb Q(\omega)$.

### 1.3 The open problem

Determine the correlation functions. Primary target objects, fixed here:

1. The lattice two-point function $G_n(r)=\langle\sigma_0^{\,n}\sigma_r^{-n}\rangle$ in the infinite-volume ordered regime, $r$ along a lattice axis, general $N\ge3$: exact values at finite $r$, and large-$r$ asymptotics beyond the known limit $G_n(\infty)=\langle\sigma^n\rangle\langle\sigma^{-n}\rangle$.
2. Chain ground-state correlators $\langle Z_1^{\,n}Z_{1+r}^{-n}\rangle$ of $H(\lambda)$ on the superintegrable line, both phases.

No exact formula - multiple integral, determinant, or convergent form-factor series - is known for either object at $N\ge3$, for any $r\ge2$, anywhere in parameter space off the Ising reduction $N=2$.

The XYZ/eight-vertex chain is carried as scaffold: its correlation program (qKZ, vertex operators, factorization) is the most developed near-analog and is itself incomplete; progress there transfers machinery here.

## 2. Complete-resolution standard

Complete resolution requires all of:

1. An exact representation of $G_n(r)$ (or the chain correlator), valid for all $r$ on a parameter region of nonzero measure and general $N\ge3$ - a determinant, a multiple integral with explicit contours, or a form-factor series with proven convergence.
2. A derivation from the integrable structure in which every step is either proven or reduced to an explicitly stated, independently checkable identity. (Integrable-physics rigor is acceptable under mode `[sym]`, but every unproven step must be isolated and labeled as such.)
3. Verification against the certified exact finite-lattice data of P1 at every accessible size, with exact or 100+-digit agreement.
4. Correct degenerations: $N=2$ reduces to the known Ising correlations; $r\to\infty$ reproduces Baxter's order parameters; free-fermion/decoupling limits check out.

**Not accepted as resolution:**

- $N=2$ results - Ising is solved and serves only as calibration.
- Reproduction of superintegrable ground-state form factors / spin matrix elements already in the literature (Au-Yang–Perk ~2008–2011; Iorgov–Shadura–Tykhyy and Lisovyy ~2009–2012 - verify): prior art and target P2, not resolution.
- Order-parameter or free-energy rederivations, however elegant.
- Conjectural integral formulas checked only at $r=1$, or only numerically at low precision.
- Correlations of the associated $\tau_2$ / six-vertex descendant model presented as chiral Potts correlations without an exact proven dictionary.
- Large-$r$ asymptotic forms without exact finite-$r$ content, or vice versa, presented as the full answer.

## 3. Graded partial-result targets

**P1 - certified exact ground truth.**
Exact diagonalization of $H(\lambda)$ for $N=3$: minimal polynomials and exact eigenvectors over $\mathbb Q(\omega)$ in symmetry sectors ($\mathbb Z_N$ charge plus translation) for $L\le8$; certified ball-arithmetic (Arb) ground states with rigorous eigenpair enclosures for $L\le14$–$16$. Deliver tables of $\langle Z_1^{\,n}Z_{1+r}^{-n}\rangle$: exact algebraic numbers where feasible, certified 100-digit enclosures otherwise.
*Certificate:* exact residual checks $(H-E)v=0$ in $\mathbb Q(\omega)$, or Arb enclosures with stated radii; dual implementations.

**P2 - verify the known frontier.**
Test Baxter's order-parameter formula by certified finite-size extrapolation; verify the published superintegrable form-factor/matrix-element formulas (verify the literature first: Au-Yang–Perk; Iorgov–Lisovyy et al.) against P1 data. Any confirmed discrepancy is itself a significant result.
*Certificate:* scripted side-by-side exact/enclosure comparisons.

**P3 - symbolic mining of exact data.**
For $r=1,2,3$, hunt closed forms with PSLQ/LLL over $\mathbb Q(\omega)$-spanned candidate bases - products of Gamma values at rationals, hypergeometric constants, powers of $(1-k'^2)$ - guided by the Ising analog, where diagonal correlations are polynomial in the elliptic integrals $E,K$.
*Certificate:* any hit stated as a conjecture with $\ge100$-digit agreement, the exact candidate, and a re-verification script; misses reported with the searched basis and height bounds.

**P4 - a new representation, checked.**
A determinant or integral representation for at least one correlation family (e.g. an emptiness-formation-probability analog, or the nearest-neighbor family) on the superintegrable line, checked against P1 at all accessible $L$ and $r$. A representation passing all checks but lacking derivation is a strong partial, to be labeled conjectural.
*Certificate:* the formula, the check scripts, and the labeled derivation status.

**P5 - the XYZ scaffold.**
Calibrate on solved ground: implement the XXZ factorized correlations (Boos–Jimbo–Miwa–Smirnov–Takeyama 2006–2009) and reproduce known short-distance values exactly. Then produce exact finite-$L$ XYZ correlation tables ($L\le14$) and test the special-point structures (supersymmetric point $\eta=\pi/3$; Bazhanov–Mangazeev Painlevé VI structures ~2005–2010) against them. Progress on XYZ factorization transfers directly to the chiral Potts program.
*Certificate:* exact tables plus published-formula agreement.

**P6 - strongest short of resolution.**
A general-$N$ conjectural exact formula for $G_n(1),G_n(2),\dots$ or the chain correlators, passing every certified check in P1–P5 including the $N=2$ reduction and the order-parameter asymptotics, with the derivation gap stated precisely.

Honest calibration: full resolution would close a 35-year-old program that defeated its creators. The realistic session products are P1–P3, with P4/P5 as strong outcomes. The certified data set of P1 is of lasting value to the field on its own.

## 4. Known results and prior art

- Model discovery and star–triangle: Au-Yang–McCoy–Perk–Tang–Yan 1987; Baxter–Perk–Au-Yang 1988.
- Six-vertex descendant structure: Bazhanov–Stroganov 1990; Baxter 1990.
- Free energy: Baxter 1988–1990 (functional relations; later simplified derivations by Baxter).
- Order parameters: Albertini–McCoy–Perk–Tang 1989 (conjecture); Baxter 2005 (proof).
- Superintegrable chain: Howes–Kadanoff–den Nijs 1983 ($N=3$ precursor); von Gehlen–Rittenberg 1985; Onsager-algebra structure: Davies 1990.
- Form factors / spin matrix elements on the superintegrable line: Au-Yang–Perk ~2008–2011; Iorgov, Shadura, Tykhyy; Lisovyy ~2009–2012 (verify exact scope - matrix elements, not full correlation functions).
- XXZ correlation program: Jimbo–Miwa (vertex operators, multiple integrals; 1992–1995 book); Kitanine–Maillet–Terras 1999–2005 (algebraic Bethe ansatz multiple integrals); factorization/fermionic basis: Boos–Jimbo–Miwa–Smirnov–Takeyama 2006–2009; parallel factorization line: Boos–Göhmann–Klümper–Suzuki ~2006–2012 (verify).
- Eight-vertex/XYZ: Lashkevich–Pugai 1998 (free-field integral formulas - verify the status of their verification); Bazhanov–Mangazeev ~2005–2010 (eight-vertex ground state and Painlevé VI); Rosengren ~2015 and Zinn-Justin on the XYZ combinatorial point and three-color model (verify).
- No completed XYZ factorized-correlation program, and no published exact chiral Potts two-point function for $N\ge3$ at any $r\ge2$, as of last knowledge (verify - this absence *is* the problem; a literature scan for 2024–2026 preprints is mandatory before starting).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

### 5.1 `[sym]` Exact linear algebra over cyclotomic fields

- $N=3$, $L=8$: dimension $3^8=6561$; charge+translation sectors of size $\lesssim250$ - minimal polynomials and exact eigenvectors are workstation-feasible with FLINT/antic (via SageMath or e-antic).
- $L=10$ ($3^{10}=59049$; sectors $\sim1650$) is the exact-arithmetic stretch goal; use CRT/fraction-free methods against entry blowup.
- Beyond that: Arb ball arithmetic - double-precision Krylov to locate the ground state, then interval Rayleigh/residual certification of the eigenpair.
- Expected failure modes: intermediate-entry blowup in exact elimination; eigenvalue near-degeneracies defeating certification near phase boundaries - work at generic $\lambda\in\mathbb Q$ (e.g. $\lambda=1/2$, $\lambda=2$) and handle critical $\lambda=1$ separately.

### 5.2 Parameter discipline

- Off the superintegrable line the weights require high-degree algebraic extensions of the rapidity curve.
- Restrict exact work to superintegrable/vertical-rapidity points where entries stay in $\mathbb Q(\omega)$ (verify the parametrization before computing); document the choice and its loss of generality.

### 5.3 `[sym]` Transfer-matrix lattice data

- Row-to-row transfer matrices for widths $W\le8$ at exactly representable rapidity points.
- Correlations from dominant-eigenvector sandwiches, with the same exact/certified discipline as 5.1.

### 5.4 `[sym]` Mining and structure detection

- mpmath PSLQ / Pari-GP `lindep` at 100–300 digits from Arb data; candidate bases assembled from the Ising and order-parameter constants; every run logged with basis, precision, and outcome.
- ore_algebra guessing on sequences in $r$ and $L$ to detect D-finite structure; any found recurrence is a conjecture to be re-verified exactly at new points before being reported.

### 5.5 Calibration gate

Run the full pipeline first on $N=2$ (Ising) and on XXZ, where every answer is known. A pipeline that cannot reproduce the Ising diagonal correlations exactly is not admissible for chiral Potts claims. This gate is mandatory and its results are part of the record.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All $L\le8$ ($N=3$) spectra and correlators as exact elements of stated extensions of $\mathbb Q(\omega)$ with minimal polynomials given; all larger-$L$ data as Arb balls of radius $\le10^{-100}$; floating point only for eigenvalue location, never for reported values.
2. **Independent verification.** Dual implementations of the Hamiltonian/transfer matrix (SageMath and C++/FLINT); an independent checker that re-verifies residuals $(H-E)v$ and enclosures from serialized data without rerunning the search; PSLQ hits re-verified by an LLL implementation from a different library.
3. **Reproducibility.** Every table records $(N,L,\lambda,\text{boundary},\text{sector},\text{precision})$, code versions, and any seeds; SHA-256 manifest over all data files, certificates, and scripts.
4. **Preservation.** Diagonalization code, mining logs including all failed PSLQ bases, and rejected candidate representations are part of the record; unpreserved explorations must be declared.
5. **Honest reporting.** The final report opens by stating whether the section-2 standard was met (expected: no); every formula is labeled proven / derived-modulo-stated-identities / conjectural-data-backed; and no matrix-element reproduction, small-$r$ closed form, or XYZ-side progress is represented as the chiral Potts correlation solution.
