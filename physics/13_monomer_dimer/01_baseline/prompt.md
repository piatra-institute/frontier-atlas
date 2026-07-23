# PROMPT FOR THE MONOMER–DIMER CONSTANTS

## Monomer–dimer entropy on $\mathbb{Z}^2$ at finite monomer density, and the 3D pure-dimer constant

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 13 of 50 (Tier 2)
**Source:** top-50 list #24, category C (exactly solvable models and lattice statistics)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Kasteleyn and Temperley–Fisher solved the pure dimer model on $\mathbb{Z}^2$ in 1961: the perfect-matching entropy is $G/\pi$ with $G$ Catalan's constant. Admit monomers and exactness collapses: the monomer–dimer free energy $f_2(x)$ and fixed-density entropy $h_2(p)$ have no closed form at any interior density, and the model is not known to be integrable - only isolated exact islands survive (a single monomer on the boundary; the Temperley and Tzeng–Wu tradition). In three dimensions even the pure dimer constant $h_3$ is unknown, boxed between Schrijver-type lower bounds and transfer-matrix upper bounds. Both constants sit on mountains of exact finite data - matching polynomials, real-rooted by Heilmann–Lieb - which makes them natural `[sym]` targets: certified bound improvements with interval transfer matrices, series mining for differential-algebraic structure, and precise statements about the monomer-density expansion. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution. Full resolution of either constant is unlikely; the graded targets are the goal.

## 1. Exact problem statement

### 1.1 Matchings and generating polynomials

For a finite graph $G$, a $k$-matching is a set of $k$ pairwise disjoint edges; $m_k(G)$ counts them, $m_0=1$. Matched vertices carry dimers, unmatched vertices monomers. The matching generating polynomial with dimer activity $x>0$ is

\[
Z_G(x)=\sum_{k\ge0}m_k(G)\,x^{k}.
\]

### 1.2 Lattices and limits

Boxes $\Lambda_{m,n}\subset\mathbb{Z}^2$ and $\Lambda_{l,m,n}\subset\mathbb{Z}^3$ are grid graphs with free boundary conditions; periodic variants must be flagged wherever used. Standard limits (existence re-proved in-session where used):

\[
f_d(x)=\lim_{\Lambda\uparrow\mathbb{Z}^d}\frac{1}{|\Lambda|}\log Z_\Lambda(x),
\qquad
h_d(p)=\lim_{\Lambda\uparrow\mathbb{Z}^d}\frac{1}{|\Lambda|}\log m_{\lfloor p|\Lambda|/2\rfloor}(\Lambda),
\]

for dimer density $p\in[0,1]$ (fraction of vertices covered); monomer density is $1-p$. The two are Legendre-dual:

\[
h_d(p)=f_d(x)-\tfrac{p}{2}\log x
\quad\text{at}\quad
p=p(x)=2x\,f_d'(x).
\]

### 1.3 Constant (a): 2D monomer–dimer entropy

The function $h_2(p)$ for $0<p<1$, equivalently $f_2(x)$ for $0<x<\infty$. Exactly known anchors:

\[
h_2(0)=0,\qquad
h_2(1)=\frac{G}{\pi}=0.29156090\ldots,\quad
G=\sum_{j\ge0}\frac{(-1)^j}{(2j+1)^2}
\quad\text{(Kasteleyn 1961; Temperley–Fisher 1961)} .
\]

A standard benchmark is the $x=1$ constant $\exp f_2(1)=1.9402\ldots$ (Baxter 1968 numerics; rigorous digits in the Friedland–Peled tradition - verify). **Open question (a):** exact evaluation of $h_2(p)$ (equivalently $f_2(x)$) at any interior point, or a proof-grade determination of its analytic nature.

### 1.4 Constant (b): 3D pure-dimer constant

For even boxes, with $\mathrm{PM}$ the number of perfect matchings,

\[
h_3=\lim_{n\to\infty}\frac{1}{(2n)^3}\log\mathrm{PM}(\Lambda_{2n,2n,2n}).
\]

Superadditivity of $\log\mathrm{PM}$ under disjoint gluing of even boxes (one-line proof to be included: a matching of $A$ union a matching of $B$ is a matching of $A\cup B$, and adding the interface edges only increases the count) gives $h_3=\sup_n$; hence every exact finite count is a rigorous lower bound, and upper bounds come from slab transfer matrices. **Open question (b):** the exact value of $h_3$, or improved certified bounds.

### 1.5 Transfer matrices and structural input

Width-$n$ strips (2D) and $n\times k$-cross-section slabs (3D): states are matching profiles on a cut (the subset of cut vertices already matched forward); the transfer matrix adds one layer with weight $x^{\#\text{dimers added}}$ ($x=1$ for (b)). Every bound-grade eigenvalue statement uses nonnegativity/primitivity and must state its boundary conditions exactly.

**Heilmann–Lieb (1972), assumed and re-verifiable:** all roots of $Z_G(x)$ are real and negative for every graph; hence $f_d$ is analytic on $\mathbb{C}\setminus(-\infty,0]$, there is no phase transition at any $x>0$, and $h_d(p)$ is analytic on $(0,1)$. The singularities live on the negative real $x$-axis and at the close-packing endpoint $p=1$.

## 2. Complete-resolution standard

Complete resolution of **(a)**: an exact closed form for $f_2(x)$ on an interval, or for $h_2(p)$ at some interior $p$, with complete proof and certified numerical verification to $\ge30$ digits; or a proof excluding $f_2$ from an explicit natural class of functions/constants, with the class declared before the proof is attempted.

Complete resolution of **(b)**: an exact closed form for $h_3$ with proof; or a rigorous enclosure precise enough to separate $h_3$ from every previously conjectured closed form, together with that exclusion analysis.

**Not accepted as resolution:**

- New digits for $\exp f_2(1)$, $h_2(p)$, or $h_3$ without proofs, represented as more than precision records.
- The exactly solvable islands - pure dimers, a single boundary/corner monomer, 1D chains, Bethe/tree lattices - presented as progress on interior-density $\mathbb{Z}^2$ or on $\mathbb{Z}^3$.
- Mean-field, Bethe-approximation, or truncated-series evaluations presented as values of the constants.
- A PSLQ hit without exact proof (report as conjecture, with multiple-testing accounting).
- Non-rigorous transfer-matrix or CTM extrapolations ("converged to 12 digits") presented as bounds; a bound requires a proved inequality plus exact/interval arithmetic.
- Complexity-theoretic remarks (#P-hardness of finite monomer–dimer counting) offered as resolving, or bearing on, the analytic question.

## 3. Graded partial-result targets

- **P1 - Reproduce the exact frontier with verified code.**
  - *Task:* (i) Kasteleyn Pfaffian evaluation of $\mathrm{PM}(\Lambda_{2m,2n})$ in exact integer arithmetic, matched against the product formula and OEIS; (ii) matching polynomials $Z_{\Lambda_{m,n}}(x)$ by profile transfer matrix, checked against direct enumeration for small sizes and published tables (Kong tradition - verify); (iii) in-session proofs of the limit-existence and Legendre-duality statements of section 1.2.
  - *Certificate:* dual implementations agreeing; hashes; short proofs in the report.
- **P2 - Certified improvement of the rigorous upper bound on $h_3$.**
  - *Task:* re-derive with full proofs the slab-subadditivity inequalities (Friedland–Peled tradition) converting a slab transfer-matrix Perron eigenvalue into an upper bound on $h_3$; compute certified Perron enclosures (Collatz–Wielandt ratios in exact/interval arithmetic) for the thickest feasible slabs, with cross-section symmetry reduction.
  - *Certificate:* the proved inequality, the exact-arithmetic eigenvalue certificate, and an independent checker.
  - *Value:* any certified improvement over the published record (order of $0.4575$ - verify) is publishable; even matching the record with a machine-checkable certificate is new, since published bounds rarely ship with certificates.
- **P3 - Certified two-sided enclosures for $f_2(x)$ and $h_2(p)$.**
  - *Task:* prove strip sandwich inequalities for the strip Perron values $\Lambda_n(x)$ at fixed rational $x>0$ (sub/supermultiplicativity in the width); certified Perron enclosures on wide strips; rigorous intervals for $f_2(x)$ on a grid of rational $x$; transport to $h_2(p)$ by certified convexity/Legendre analysis in interval arithmetic. Target rigorous width $\le10^{-10}$; compare Baxter's 1968 values.
  - *Certificate:* proofs + interval transcripts + independent checker.
- **P4 - Exact thermodynamic series and their analytic nature.**
  - *Task:* exact rational coefficients of the low-activity expansion $f_2(x)=\sum_{k\ge1}c_kx^k$ to high order via the finite-lattice method (Enting tradition), and of $f_3(x)$ to feasible order. Then: (i) certified location and type of the dominant negative-axis singularity; (ii) D-finiteness exclusion certificates ("no ODE of order $\le r$, degree $\le d$ annihilates the series to depth $N$"); (iii) tests of the Federbush–Butera–Pernici structural claims for the $h_d(p)$ expansion (verify the claims first).
  - *Certificate:* exact coefficient files, two independent derivations, linear-algebra transcripts.
- **P5 - The close-packing expansion of $h_2(p)$.**
  - *Task:* establish with certificates - and proofs where possible - the structure of $h_2(p)$ as $p\to1^-$, including the $(1-p)\log(1-p)$ non-analyticity and subsequent terms; certified extraction of coefficients from P3/P4 data; comparison with the exactly known boundary-monomer islands (Tzeng–Wu).
  - *Certificate:* interval-certified coefficient enclosures with stated error model; proofs where claimed.
- **P6 - Relation hunting and new exact islands (strongest realistic).**
  - *Task:* PSLQ/LLL sweeps on certified digits of $\exp f_2(1)$, $h_2(p)$ at symmetric points (e.g. $p=\tfrac12$), and $h_3$, against a pre-declared basis (Catalan family, $\pi$, logarithms, $\Gamma$-values, lattice Green-function constants), with multiple-testing accounting. In parallel: attempts to extend the boundary-monomer islands (one bulk monomer, two boundary monomers) to new proved product formulas via exact Pfaffian perturbation theory.
  - *Certificate:* declared census + transcripts; complete proofs for any claimed new island.

## 4. Known results and prior art

- R. H. Fowler, G. S. Rushbrooke (1937): origin of the monomer–dimer problem.
- P. W. Kasteleyn (1961); H. N. V. Temperley, M. E. Fisher (1961): pure-dimer solution on planar lattices; $h_2(1)=G/\pi$.
- M. E. Fisher, J. Stephenson (1963): monomer–monomer correlations in the dimer background ($r^{-1/2}$ decay) - the classic exact island beyond the free energy.
- R. J. Baxter (1968): "Dimers on a rectangular lattice" - variational/CTM computation of the monomer–dimer free energy at finite density; still reference numerics (verify precision).
- D. S. Gaunt (1969): monomer–dimer series for square and cubic lattices.
- O. J. Heilmann, E. H. Lieb (1972): real-rootedness of matching polynomials; no phase transition; analyticity.
- H. N. V. Temperley (1974): defect–spanning-tree bijection tradition. W.-J. Tzeng, F. Y. Wu (~2003): closed form for a single monomer on the boundary; F. Y. Wu and collaborators (~2006–2011): further boundary-monomer Pfaffian results, with some published corrections in that literature - verify carefully before use.
- A. Schrijver (1998): permanent lower bound for regular bipartite graphs; applied to $\mathbb{Z}^3$ it gives $h_3\ge\tfrac12\log(3125/1296)\approx0.44008$ (re-derive the application, including the limiting argument, in-session). P. Csikvári (~2014–2017): lower-matching-conjecture strengthenings via graph limits (verify exact consequences for $h_3$ and $h_3(p)$).
- S. Friedland, U. N. Peled (~2005): computability theory of matching entropies; rigorous 3D bounds (upper bound near $0.4575$ - verify the current record). S. Friedland, E. Krop, P. H. Lundow, K. Markström (~2008): asymptotic matching conjectures and validations.
- I. Beichl, F. Sullivan (~1999): importance-sampling estimate $h_3\approx0.4466$ (verify the best current non-rigorous value; likely refined since).
- P. Butera, P. Federbush, M. Pernici (~2011–2013): expansions for $h_d(p)$ and structural conjectures on the monomer-density expansion (verify statements).
- To our knowledge: no closed form for interior $h_2(p)$, none for $h_3$; no Yang–Baxter or commuting-transfer-matrix structure known (or expected) for monomer–dimer on $\mathbb{Z}^2$.

**Status as of mid-2026 - re-verify against current literature before starting the session.** In particular: current rigorous bounds on $h_3$ (both sides), best non-rigorous $h_3$ and monomer–dimer numerics, the corrected status of the boundary-monomer exact results, and any tensor-network rigorous-bound papers.

## 5. Attack plan

Single workstation throughout; state-space growth is the binding constraint.

1. **Exact engines (P1, P4).**
   - Python/SymPy reference plus C++/GMP production code for: exact Pfaffians (fraction-free or multi-prime CRT), profile transfer matrices over $\mathbb{Z}[x]$ for strips (widths to ~14 with polynomial entries; wider at fixed rational $x$), finite-lattice-method series assembly.
   - Cross-checks: OEIS matching counts, the Kasteleyn product formula, brute force on small graphs.
2. **Interval Perron layer (P2, P3).**
   - Approximate Perron vectors by floating-point power iteration; certificates by Collatz–Wielandt ratios in exact rational or Arb directed-rounding arithmetic (the certificate is independent of how the vector was found).
   - 3D slabs: dihedral symmetry reduction of the cross-section; expected reachable cross-sections around $4\times k$, $5\times k$, possibly $6\times6$ with implicit sparse products - measure, do not promise.
   - Failure mode: the published record already sits at an unreachable thickness - then reproduce the record rigorously with our independent certified pipeline and say so plainly; that is still a contribution.
3. **Series analysis (P4, P5).**
   - Sage ore_algebra for guessing and exclusion on $\{c_k\}$; Pari/GP for high-precision evaluation; differential-approximant analysis for the negative-axis singularity with Arb-certified refinement of any claimed enclosure.
   - Failure mode: finite-lattice-method order ceiling (2D perhaps order 30–40 in $x$; 3D much lower) - report the exact $(r,d,N)$ exclusion envelope actually achieved, no extrapolated claims.
4. **Relation hunting and islands (P6).**
   - Pari/GP `lindep` + fplll; pre-declared, version-controlled census; every hit re-tested at doubled precision.
   - Pfaffian perturbation for new islands: SymPy symbolic minors of the Kasteleyn matrix with defect rows/columns, seeking determinantal product structure; failure mode: expression swell without structure - cap the effort and record the negative outcome.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All matching counts and series coefficients exact; every claimed bound flows through a proved inequality evaluated in rational or Arb directed-rounding arithmetic; floating point only inside clearly quarantined exploration.
2. **Independent verification.** Dual implementations for every counting engine; a standalone Collatz–Wielandt checker (no eigenvalue library) re-verifying every Perron certificate; series coefficients re-derived by a second method (transfer matrix vs finite-lattice method) wherever both reach.
3. **Reproducibility.** Boundary conditions, activities, cross-section geometries, precisions, and the PSLQ census in version-controlled configuration; environment versions frozen; SHA-256 manifest over data files, certificates, and logs.
4. **Preservation.** Approximate eigenvectors, failed island ansätze, and negative PSLQ sweeps preserved; imported published data (series, bounds) archived with provenance, kept distinct from recomputed data.
5. **Honest reporting.** The report opens with the status of both constants (expected: unresolved); rigorous intervals listed separately from non-rigorous estimates; the report states whether any published bound was actually improved or only independently certified; exact islands are reported as islands, never as a solution of the monomer–dimer problem.
