# PROMPT FOR THE RESIDUAL ENTROPY OF ICE Ih

## The Pauling entropy problem for three-dimensional ice lattices

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 14 of 50 (Tier 2)
**Source:** top-50 list #25, category C (exactly solvable models and lattice statistics)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Pauling estimated in 1935 that ice retains a residual entropy $k_B\log W$ per molecule with $W\approx3/2$, matching the Giauque–Stout calorimetry. Lieb proved in 1967 that two-dimensional square ice has exactly $W=(4/3)^{3/2}$ - a crown jewel of exact lattice statistics - but for real three-dimensional ice (hexagonal Ih, cubic Ic) only series and numerical estimates exist, near $W\approx1.5074$ (Nagle 1966 and successors). No exact value is known, and no rigorous two-sided enclosure of useful width appears to have been published: the rigorous state of the art is essentially Pauling's $3/2$ as a lower bound (via Schrijver's Eulerian-orientation theorem) plus weak counting upper bounds. The task is the exact value or proof machinery toward it; the realistic and genuinely valuable graded product is the first certified rigorous enclosure from our own verified transfer-matrix and interval pipeline - rarely attempted rigorously - together with structure mining aimed at the three-dimensional integrability obstruction (tetrahedron equation). Adjacent payoff: spin-ice materials realize the same counting problem. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Ice rule

Let $G$ be a finite 4-regular graph (vertices are oxygen sites; edges are hydrogen bonds). An *ice configuration* is an orientation of all edges with in-degree 2 and out-degree 2 at every vertex - an Eulerian orientation. Physically each O has two covalent (near) and two long (far) hydrogens (Bernal–Fowler rules). Write $Z(G)$ for the number of ice configurations.

### 1.2 Lattices (fixed conventions)

- *Square ice:* $\mathbb{Z}^2$ as a 4-regular lattice; solved (Lieb 1967) - calibration only.
- *Ice Ic:* oxygens at the vertices of the diamond lattice (two interpenetrating fcc sublattices; tetrahedral 4-coordination).
- *Ice Ih:* oxygens at the vertices of the hexagonal wurtzite-type lattice (tetrahedral coordination, hexagonal symmetry, bilayers stacked along the $c$-axis).

Finite samples are $N$-vertex tori (periodic in all directions) built from explicitly recorded primitive cells; free boundaries must be flagged wherever used.

### 1.3 The constants

For each lattice family,

\[
W=\lim_{N\to\infty}Z(G_N)^{1/N},
\qquad
S_0=k_B\log W\ \text{per molecule}.
\]

Existence of the limit and boundary-condition independence must be re-proved in-session for the exact graph sequences used (standard subadditivity; part of P1/P2).

### 1.4 Anchors

- **Exact (calibration):** Lieb (1967): $W_{\square}=(4/3)^{3/2}=1.53960\ldots$ for square ice (six-vertex model at $a=b=c$, Bethe-ansatz transfer matrix).
- **Pauling estimate:** each vertex admits 6 of $2^4=16$ arrow states; the mean-field count gives $W_{\mathrm{Pauling}}=2^{2}\cdot(6/16)=3/2$ - present this derivation exactly in the report.
- **Series/numerics:** Nagle (1966): $W(\mathrm{Ih})=1.50685\pm0.00015$; modern estimates cluster near $1.5074$, resolving a tiny Ih–Ic difference in the fifth decimal (verify current values and error bars).
- Note $W(\mathrm{Ih})$ is strikingly close to, but distinct from, $3/2$, and far from $W_\square$.

### 1.5 Transfer-matrix convention (fixed)

For a layered decomposition (Ic along a cubic axis of the diamond lattice; Ih in bilayers along the $c$-axis), the state on a cut is the arrow configuration on the cut bonds; the layer transfer matrix $T_n$ (cross-section of $n\times n$ cells, periodic in-plane) has entries

\[
T_n(u,v)=\#\{\text{ice-rule-consistent layer completions given boundary arrows }u,v\},
\]

a nonnegative integer matrix. $W$ is recovered from Perron eigenvalues per site through sandwich inequalities to be proved in P2 for the exact geometry used.

### 1.6 Scope exclusions

The following neighbouring objects are out of scope and must not be conflated with the targets: square ice and all 2D six-vertex results (calibration only); KDP- and F-model variants (weighted vertices); ice with Bjerrum or ionic defects (the physical entropy at finite temperature); antiferroelectric transitions of real ice. The targets are the two zero-temperature counting constants of section 1.3 exactly as defined.

### 1.7 The open question (adopted formulation)

Determine $W(\mathrm{Ih})$ and $W(\mathrm{Ic})$ exactly - closed form with proof - or produce proof machinery and certified rigorous enclosures. The two lattices are one problem with two instances; every claim must name its instance. A subsidiary precise question, open to our knowledge: prove $W(\mathrm{Ih})\neq W(\mathrm{Ic})$, or prove equality (the series and numerics suggest a difference of order $10^{-5}$ - verify).

## 2. Complete-resolution standard

A complete resolution is one of:

- **(A)** An exact closed form for $W(\mathrm{Ih})$ or $W(\mathrm{Ic})$ - an algebraic number or an explicit expression in standard constants - with complete proof, verified numerically against certified enclosures to $\ge20$ digits.
- **(B)** A proof that $W$ (either instance) lies outside an explicitly declared natural class (e.g. not algebraic of degree $\le D$ and height $\le H$), with the class declared before the attempt.
- **(C)** A rigorous exact-solution framework for a genuinely three-dimensional ice lattice - a solved 3D vertex model containing the ice point - with complete proofs.

**Not accepted as resolution:**

- Monte Carlo, tensor-network, or series estimates of any precision, presented as more than estimates.
- Pauling-type, Kikuchi/cluster-variation, or other approximations, however refined.
- Results for square ice, decorated 2D lattices, Bethe lattices, or Husimi trees presented as statements about Ih/Ic.
- A PSLQ hit - a pretty closed form matching 15 digits - without proof; report as conjecture with multiple-testing accounting.
- "The tetrahedron equation has solutions, hence 3D ice is solvable"-type arguments without an actual solution containing the ice point.
- Bounds whose underlying inequalities (sub/supermultiplicativity, boundary-condition comparisons) are asserted but not proved for the specific layered geometry used.

## 3. Graded partial-result targets

Full resolution is very unlikely; P2 is the headline realistic target and would likely be the first of its kind (verify).

- **P1 - Calibration on solved and classical ground.**
  - *Task:* (i) exact ice-configuration counts on small tori of all three lattices by brute force and independently by transfer matrix (dual code); (ii) reproduce Lieb's $W_\square=(4/3)^{3/2}$ numerically from our own square-ice transfer matrices, with measured convergence rates; (iii) reproduce Nagle's 1966 series methodology and value from scratch.
  - *Certificate:* exact count tables with dual-implementation agreement; convergence report; hashes.
- **P2 - First certified rigorous enclosure of $W(\mathrm{Ic})$, then $W(\mathrm{Ih})$.**
  - *Task:* prove the layered sandwich inequalities relating Perron eigenvalues of $T_n$ to $W$ (sub/supermultiplicativity in cross-section size and layer count for Eulerian-orientation counts, for the exact geometry used); compute certified Perron enclosures via Collatz–Wielandt ratios - for positive $v$, $\min_u(T_nv)_u/v_u\le\Lambda_n\le\max_u(T_nv)_u/v_u$ - in exact or directed-rounding arithmetic at the largest feasible $n$; output rigorous intervals.
  - *Success ladder:* width $10^{-2}$, then $10^{-3}$, then $10^{-4}$ around $1.5074$. Ic first (higher symmetry), Ih second.
  - *Certificate:* the proofs, the exact ratio checks, and an independent sparse-multiplication checker.
  - *Value:* even a rigorous $[1.50,1.52]$ would, to our knowledge, be the tightest certified enclosure ever published for real ice; a $10^{-4}$ window brackets the Nagle value rigorously for the first time.
- **P3 - Exact series extension.**
  - *Task:* extend Nagle-type series (or an equivalent cumulant/moment expansion for Eulerian-orientation entropy) beyond the classical order with exact rational coefficients, derived twice independently; certified resummation with a stated non-rigorous error model, kept strictly separate from P2 rigor.
  - *Certificate:* coefficient files, dual derivations, hashes.
- **P4 - Relation hunting on certified digits.**
  - *Task:* PSLQ/LLL on the best available digits (rigorous where possible, labeled otherwise) against a pre-declared census: algebraic numbers of bounded degree/height, Lieb-type expressions $p^aq^b$ in small rationals, values from solvable vertex models, $\Gamma$-value monomials; multiple-testing accounting throughout.
  - *Certificate:* the census, full transcripts, and exclusion statements phrased with exact logical content (e.g. "no relation of the declared form exists unless digits beyond our certified enclosure conspire").
- **P5 - Integrability-obstruction mining.**
  - *Task:* (i) spectral structure of the layer transfer matrices: exact characteristic polynomials for small $n$, degeneracy patterns, comparison with the rich solvable structure of the 2D case; (ii) bounded-search certificates of the form "within an explicitly parametrized class of local weight deformations, no nontrivial commuting partner of $T_n$ - and no tetrahedron-equation-compatible local structure - exists through the ice point", as exact linear-algebra results on finite systems with their finite scope stated in the claim.
  - *Certificate:* exact polynomial data; kernel computations reproducible and independently re-checked.
- **P6 - Strongest short of resolution.**
  - *Task:* any proved structural theorem - a monotone sequence of upper bounds with explicit convergence rate; a proved inequality separating $W(\mathrm{Ih})$ from $W(\mathrm{Ic})$, or a proof of their equality (their relationship is itself open; verify the current numerical separation first); or a solvable 3D vertex model rigorously bounding ice.
  - *Certificate:* complete proofs, with every computational step certified per section 6.

## 4. Known results and prior art

- J. D. Bernal, R. H. Fowler (1933): ice rules. L. Pauling (1935): the $3/2$ estimate. W. F. Giauque, J. W. Stout (1936): calorimetric residual entropy of ice.
- E. H. Lieb (1967): exact solution of square ice; the six-vertex tradition (Sutherland, Yang–Yang era).
- J. F. Nagle (1966): series method for ice Ih/Ic; $W(\mathrm{Ih})=1.50685(15)$.
- A. Schrijver (1983): lower bound on the number of Eulerian orientations of 4-regular graphs, yielding $W\ge3/2$ rigorously for ice lattices (verify the exact form and constants of the theorem before use).
- Modern numerics: multicanonical Monte Carlo (B. Berg and collaborators, ~2007); high-precision estimates by J. Kolafa (~2014), $W(\mathrm{Ih})\approx1.50738$ with an Ih/Ic distinction (verify values); tensor-network computations of 3D residual entropies (L. Vanderstraeten and collaborators, ~2018) (verify).
- Spin ice: A. Ramirez and collaborators (1999): Pauling entropy measured in Dy$_2$Ti$_2$O$_7$; S. Bramwell, M. Gingras (2001) review - the materials payoff channel.
- 3D integrability frontier: A. B. Zamolodchikov (1980–81): tetrahedron equation; R. J. Baxter (1983): verification of the Zamolodchikov model's free energy; V. Bazhanov, S. Sergeev (2005 onward): quantum-geometry solutions. None contains real ice.
- We know of no published rigorous two-sided enclosure of $W(\mathrm{Ih})$ of width better than $\sim10^{-1}$ (verify - this gap is precisely the P2 opportunity; search also the mathematics literature on Eulerian-orientation entropy of vertex-transitive graphs).

**Status as of mid-2026 - re-verify against current literature before starting the session.** In particular: current best $W(\mathrm{Ih})$, $W(\mathrm{Ic})$ values and error bars; any rigorous-bound papers from combinatorics; any tetrahedron-equation advances touching ice-type weights.

## 5. Attack plan

Single workstation; the cross-section size is the binding constraint (states are arrow configurations on cut bonds: $2^{\#\mathrm{cut\ bonds}}$ before symmetry reduction).

1. **Exact counting layer (P1).**
   - Python brute force on tiny tori of all three lattices (up to ~24 vertices) as ground truth.
   - C++ layer builder for Ic along a cubic axis: enumerate layer completions by DFS with ice-rule pruning; verify row sums and small powers of $T_n$ against brute force.
   - Failure mode: geometry errors in the layered decomposition of diamond/wurtzite - mitigate with an independent lattice-generation script and automated isomorphism checks on small samples.
   - Failure mode: torus periodicities that are too small distorting the count (ice configurations wrap) - use at least two incommensurate cell sizes per lattice in all validation runs.
2. **Rigorous enclosure layer (P2).**
   - Prove the sandwich lemmas *first*; a session that computes before proving the inequalities produces nothing certifiable.
   - Floating-point power iteration for approximate Perron vectors on the sparse implicit operator; certificates via Collatz–Wielandt ratios in GMP rationals or Arb directed rounding.
   - Feasibility: cross-sections with $2^{n^2}$-scale state counts; realistically $n\le5$, possibly 6 with in-plane symmetry reduction - measure, do not promise.
   - Failure mode: slow convergence of the sandwich in $n$ stalls the rigorous window near $10^{-2}$–$10^{-3}$ - report the measured rate and the honest window.
3. **Series layer (P3).**
   - SymPy/Sage exact-rational reimplementation of Nagle's moment/cumulant corrections to Pauling counting; independent second derivation via programmatically generated weighted-graph embeddings.
   - Failure mode: embedding-count explosion - cap the order and record exactly where.
4. **Mining layer (P4, P5).**
   - Pari/GP `lindep` with a pre-declared census; FLINT + Berlekamp–Massey modulo primes with CRT for exact characteristic polynomials of $T_n$ at small $n$; exact nullspace computations over $\mathbb{Q}$ for commuting-partner searches within declared ansatz classes.
   - Failure mode: ansatz classes too small to mean anything - the scope of every obstruction certificate is declared inside the claim itself.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All configuration counts exact integers; every claimed bound flows through a proved inequality evaluated in exact rational or directed-rounding interval arithmetic; Monte Carlo or tensor-network numbers, if produced at all, are quarantined as non-rigorous context.
2. **Independent verification.** Dual lattice generators and dual counting engines compared on all small instances; a standalone Collatz–Wielandt checker re-verifying every eigenvalue certificate by sparse multiplication only; series coefficients derived twice by different methods.
3. **Reproducibility.** Exact lattice conventions (primitive cells, periodic identifications, layer orientation) frozen in a `conventions.md`; all cross-section sizes, precisions, seeds, and the PSLQ census version-controlled; SHA-256 manifest over count tables, Perron vectors, certificates, and logs.
4. **Preservation.** Approximate eigenvectors, geometry-validation artifacts, failed commuting-partner searches, and negative PSLQ sweeps preserved; imported numerical values (Kolafa-type) archived with provenance and never mixed into rigorous intervals.
5. **Honest reporting.** The report opens by stating that no exact value of $W(\mathrm{Ih})$ or $W(\mathrm{Ic})$ was obtained (unless (A)–(C) actually happened); rigorous enclosures and non-rigorous estimates appear in separate tables; the finite scope of every obstruction certificate (P5) is stated in the theorem-like claim itself, not in a footnote.
