# PROMPT FOR THE CRYSTALLIZATION CONJECTURE

## Periodicity of classical ground states for generic pair potentials

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 39 of 50 (Tier 4)
**Source:** top-50 list #19, category B (geometry of matter)
**Modes:** `[proof]` `[bound]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The crystallization conjecture asserts that ground states of classical particle systems with generic short-range pair potentials are periodic - that crystals form for a reason provable from the interaction alone. It is solved in dimension 1 (Ventevogel–Nijboer tradition), solved in dimension 2 for specific potential classes (Theil 2006 and the discrete-geometry school), and entirely open in dimension 3, where even face-centered-cubic universal optimality remains unproven despite the $E_8$/Leech breakthroughs. The problem is matched to current AI methods on two fronts: the published 2D proofs are long chains of explicit elementary inequalities begging for machine verification and machine-driven extension of their potential classes, and finite-$N$ ground states plus linear-programming energy bounds are exactly certifiable computations (interval global optimization, SDP with exact rounding). This is a Tier 4 problem: the complete resolution defined in section 2 is far out of reach; the graded targets in section 3 are the honest goal, and no partial, restricted, or numerical result may be represented as a solution.

## 1. Exact problem statement

### 1.1 Configurations, energy, thermodynamic limit

For a finite configuration $X=\{x_1,\dots,x_N\}\subset\mathbb R^d$ (with $d\in\{1,2,3\}$; the target is $d=3$) and a pair potential $v:(0,\infty)\to\mathbb R\cup\{+\infty\}$, define
\[
E_v(X)=\sum_{1\le i<j\le N}v(|x_i-x_j|),
\qquad
e_N(v)=\frac1N\inf_{X\subset\mathbb R^d,\ |X|=N}E_v(X).
\]
**Admissible potential class $\mathcal V_d$:**

- $v$ lower semicontinuous;
- repulsive core: $v(r)\ge c_1 r^{-d-\delta_0}$ near $0$ (strong enough to force a minimal interparticle distance in minimizers);
- tempered decay: $|v(r)|\le c_2 r^{-d-\delta_0}$ for large $r$;
- normalized well: $\min v=v(1)=-1$.

Under these hypotheses the thermodynamic limit
\[
e_\infty(v)=\lim_{N\to\infty}e_N(v)
\]
exists by subadditivity - prove or cite this precisely in-session; it is part of the formal record.

**Ground states.** A locally finite configuration $\omega\subset\mathbb R^d$ is a ground state if no perturbation of finitely many points decreases the energy (finite local energy differences are well-defined under the decay hypothesis). A configuration is **periodic** if it is invariant under a full-rank lattice $L\subset\mathbb R^d$ with finitely many orbits per fundamental domain.

### 1.2 The conjecture (adopted formulations)

- **(C-energy)** For $v$ in an explicitly described subclass $\mathcal G\subset\mathcal V_3$ - open in a declared topology, or "generic" in a declared Baire/prevalence sense -
  \[
  e_\infty(v)=\inf\{\,e(\omega,v):\ \omega\ \text{periodic}\,\},
  \]
  with the infimum attained by a periodic configuration of uniformly bounded fundamental domain.
- **(C-geometric)** For $v\in\mathcal G$, every ground state is periodic up to rigid motion, or lies within uniformly bounded distance of a periodic configuration, with the bound explicit.

Both statements, with $\mathcal G$ explicit, constitute the conjecture here; (C-geometric) is strictly stronger. Genericity is essential: potentials engineered to frustrate periodicity (quasicrystalline constructions in the Radin tradition) show the conjecture is false for *all* of $\mathcal V_3$. Zero temperature only; positive-temperature freezing (the hard-sphere transition) is adjacent context, not the target.

### 1.3 Benchmark potentials

- Lennard-Jones family: $v_{m,n}(r)=\frac{n}{m-n}r^{-m}-\frac{m}{m-n}r^{-n}$, $m>n>d$, rational exponents;
- Morse family with rational stiffness;
- Theil-class narrow-well potentials (parameters explicit).

All computational targets below must state their potential exactly, with rational parameters.

### 1.4 Normalization for periodic energies

For a periodic configuration $\omega$ with lattice $L$ and orbit representatives $y_1,\dots,y_m$ in a fundamental domain of volume $|L|$, the energy per particle is
\[
e(\omega,v)=\frac{1}{2m}\sum_{j=1}^{m}\ \sum_{\substack{(\ell,k)\in L\times\{1..m\}\\ (\ell,k)\neq(0,j)}} v\bigl(|y_j-y_k-\ell|\bigr),
\]
with absolute convergence guaranteed by the decay hypothesis. Density is *not* fixed: minimization over the lattice scale is part of every upper-bound computation, and certified periodic energies must optimize (or bracket) the density with enclosures. When comparing to LP lower bounds at fixed density, state the density convention explicitly on both sides - mismatched density conventions are a recurring silent error in this literature.

## 2. Complete-resolution standard

A complete resolution is a proof of **(C-energy) and (C-geometric) in $d=3$** for an explicitly described class $\mathcal G$ that contains a benchmark potential - for instance an open neighborhood of a Lennard-Jones potential in a declared topology - identifying the optimal periodic structure(s) (e.g., the fcc/hcp family), with all constants explicit and every computer-assisted step certified to the standard of section 6.

**Not accepted as resolution:**

- Minimization restricted to Bravais lattices or to any parametric family of periodic structures (Bétermin/theta-function results) presented as crystallization: the competitor class must be all configurations.
- Finite-$N$ numerics (Cambridge Cluster Database putative minima and the like), or even certified finite-$N$ global optima, presented as thermodynamic-limit statements.
- Results in $d=1,2$ presented as answering $d=3$.
- Potentials with built-in angular or three-body terms rewarding the target lattice (Flatley–Theil-type) presented as the generic pair-potential theorem; they are valuable partials and must be labeled as such.
- LP/SDP lower bounds with a nonzero gap to the periodic upper bound presented as proofs of optimality.
- "Generic" claims without a declared topology or measure-theoretic notion of genericity.
- Zero-temperature results presented as freezing-transition (positive-temperature) results, or vice versa.
- Energy-level statements (C-energy) presented as geometric statements (C-geometric), or conversely.

## 3. Graded partial-result targets

- **P1 - Dimension 1 reproduced with certified parameter regions.**
  - Deliverable: machine-checked reproduction of the Ventevogel–Nijboer convexity argument; then, for the two-parameter Lennard-Jones family $v_{m,n}$, a certified (interval-arithmetic) description of the region of $(m,n)$ for which the 1D ground state is the equidistant lattice, with certified lattice-spacing enclosures.
  - Certificate: inequality-chain scripts plus a standalone interval checker.
- **P2 - Finite-$N$ certified ground states (machine-checkable ground truth).**
  - Deliverable: interval branch-and-bound global optimization for $N$-clusters in $d=3$ at a fixed rational LJ potential - certified enclosure of the global minimum energy and of the minimizer geometry up to symmetry, for as large an $N$ as feasible.
  - Honest calibration: rigorous global optimality is currently known only for very small $N$; deterministic non-interval claims exist around $N\le7$ (Maranas–Floudas tradition - verify). Every newly certified $N$ is a record-grade artifact.
  - Target: certificates for all $N\le N_{\max}$ achieved, aiming $N_{\max}\ge8$, cross-checked against Cambridge Cluster Database putative minima; agreement and refutation are both reportable results.
- **P3 - Theil chain audited and constants improved.**
  - Deliverable: a full constant-explicit re-derivation of Theil's 2006 2D crystallization theorem (triangular lattice, narrow-well class): every lemma constant extracted, machine-verified, and the admissible well-width/decay parameters *widened* wherever the chain has slack, with certified inequalities.
  - Certificate: a literate audit document plus a verified constants file; any strict widening of the potential class is a publishable partial.
- **P4 - LP/SDP energy lower bounds with certified solves.**
  - Deliverable: Cohn–Elkies-type linear-programming lower bounds adapted to energy minimization at fixed density (auxiliary functions with sign-constrained Fourier transforms), solved numerically, then certified by exact rational rounding plus interval verification of all sign conditions.
  - Comparison side: certified periodic upper bounds - fcc/hcp/bcc energies via Epstein-zeta/theta summation with rigorous tails in Arb.
  - Product: certified two-sided brackets on $e_\infty(v)$ for benchmark potentials in $d=2,3$, duality gap reported honestly. A gap under $1\%$ for LJ in $d=3$ would be a significant landmark; a zero gap is not expected (fcc universal optimality is open).
- **P5 - Dimension 2 beyond Theil.**
  - Deliverable: a new certified crystallization theorem in $d=2$ for an explicitly parameterized class strictly outside existing results - e.g., certified robustness: every potential within an explicit $C^2$-distance $\rho>0$ of a reference Theil-class potential crystallizes, with $\rho$ certified via the P3 constants.
  - Certificate: proof document plus machine-verified constant chain.
- **P6 - Any rigorous 3D statement (strongest short of resolution).** One of:
  - (a) an extension of the Flatley–Theil fcc result (three-body-augmented) with a machine-verified constant chain and a strictly weaker angular term than published, quantified;
  - (b) a proof of (C-energy) in $d=3$ against a restricted-but-infinite competitor class strictly larger than lattices (e.g., all periodic configurations with $\le k$ orbits, plus certified defect bounds);
  - (c) a certified LP bound matching a certified periodic upper bound for *some* explicitly constructed $v\in\mathcal V_3$ - a "designer potential" with provable crystallization, new if achieved for a genuine pair potential.

## 4. Known results and prior art

- $d=1$: Ventevogel (1978); Ventevogel–Nijboer (1979) - convex-well potentials crystallize; Gardner–Radin (1979) - one-dimensional Lennard-Jones ground states.
- $d=2$: Heitmann–Radin (1980) - sticky-disk triangular crystallization; Radin (1981) - perfect-crystal ground states; Theil (2006, Comm. Math. Phys.) - triangular lattice for a class of narrow-well smooth potentials in the thermodynamic limit; E–Li (~2009) (verify scope); Mainini–Stefanelli (~2014) and Mainini–Piovano–Stefanelli - discrete crystallization for graphene-type and ionic models; Davoli–Piovano–Stefanelli and the De Luca–Friesecke school - $N^{3/4}$ fluctuation laws for sticky-disk minimizers (verify attributions).
- $d=3$: no crystallization theorem for any pure pair potential (verify - this is the central gap). Flatley–Theil (~2015) - fcc crystallization with an added three-body angular term.
- Lattice-restricted minimization: Montgomery (1988) - triangular theta-function optimality in 2D; Bétermin (~2016–2021) - lattice energy landscapes among Bravais lattices.
- Adjacent landmarks: Hales (1998/2005; Flyspeck 2017) - Kepler conjecture; Viazovska (2016) - $E_8$ sphere packing; Cohn–Kumar–Miller–Radchenko–Viazovska (2017; universal optimality ~2019, published ~2022) - $E_8$ and Leech universal optimality; universal optimality in $\mathbb R^3$ is **open**; Cohn–Elkies (2003) - LP bounds; Cohn–Kumar (2007) - universal optimality on spheres.
- 2D Coulomb/Riesz route: Sandier–Serfaty (~2012) - renormalized energy; the Abrikosov triangular conjecture (conditional results only).
- Hard spheres and positive temperature (context): Richthammer (2007) - no translational symmetry breaking in 2D; the 3D freezing transition has no rigorous proof (verify).
- Surveys: Blanc–Lewin (2015), "The crystallization conjecture: a review"; Friesecke–Theil (2002) on Cauchy–Born validity.
- Numerical ground-truth sources (exploration only): Wales–Doye basin-hopping; the Cambridge Cluster Database; Northby (1987).
- Deterministic (non-interval) global optimization for microclusters: Maranas–Floudas (~1994) and successors (verify which $N$ are covered and at what rigor level).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

Single-workstation program throughout:

1. **`[bound]` Certified cluster optimization (P2).** Custom C++ interval branch-and-bound over $(\mathbb R^3)^N$ quotiented by isometries (fix $x_1=0$, orient $x_2$, $x_3$):
   - interval Newton/Krawczyk contraction on first-order conditions;
   - box pruning by interval Hessian and pair-distance lower bounds (Arb/MPFI arithmetic);
   - symmetry pruning via canonical ordering constraints;
   - certified lower bounds per box from interval pair-energy enclosures.
   Expect combinatorial explosion beyond $N\approx8$–$10$; report the certified frontier honestly. Failure mode: near-degenerate flat basins stalling contraction - switch to enclosure-of-minimum rather than enclosure-of-minimizer where needed.
2. **`[bound]` LP/SDP layer (P4).** Auxiliary-function search in a radial basis (Laguerre/Hermite functions, rational parameters); float exploration with Mosek/SDPB; exact rational rounding; sign conditions re-verified by interval evaluation plus symbolically proved tail lemmas. Concretely:
   - the sign conditions ($f\le v$ pointwise beyond the core; $\hat f\ge0$) are each a one-dimensional interval-verification problem plus an analytic tail lemma - prove the tail lemmas once, symbolically;
   - periodic upper bounds: Epstein zeta and theta series for fcc/hcp/bcc in Arb with rigorous incomplete-gamma tail bounds, density-optimized with enclosures; SageMath cross-check;
   - failure mode: LP bounds in $d=3$ landing far below fcc - expected; the certified gap is itself the result, and a three-point/SDP strengthening (Cohn–Kumar-style) is the documented escalation path.
3. **`[proof]` Theil audit (P3, P5).** Transcribe the 2006 proof into a lemma DAG; every constant into a machine-readable ledger; verify each elementary inequality in SymPy/interval arithmetic; run automated slack analysis (which lemma constants bind?) to widen the potential class. Document-heavy, compute-light - ideal session work.
4. **Dimension-1 layer (P1).** Symbolic convexity conditions; interval verification over the $(m,n)$ rectangle; hours of compute at most.
5. **Pipeline order.** P1 first (validates the interval toolchain on a solved problem); P2 and P4 in parallel (independent codebases); P3 alongside as the document track; P5/P6 only from the audited P3 ledger - attempting them from the published prose alone wastes the session.
6. **Cross-cutting failure modes.**
   - Conflating "certified for this $v$" with "generic $v$".
   - Float exploration leaking into certificates.
   - Truncated lattice sums without tail enclosures in the periodic upper bounds - use energy per particle with explicit summation-tail bounds, never bare truncations.
   - Silent competitor-class restriction (lattice-only comparisons) contaminating conjecture-level claims.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Potentials fixed with rational parameters; all certified energies as Arb balls or rational bounds with directed rounding; LP/SDP certificates as exact rational objects whose feasibility is re-verified symbolically or in interval arithmetic. Basin-hopping and solver floats are exploration only.
2. **Independent verification.** For each P2 certificate: a standalone checker that re-verifies the box-elimination proof and the final enclosure from the certificate file alone, written independently of the branch-and-bound code; Python and C++ implementations for headline $N$. For P4: an independent sign-condition checker per auxiliary function.
3. **Reproducibility.** All potential parameters, box-subdivision traces, solver versions, basis choices, and seeds recorded; SHA-256 manifest over certificates, ledgers, and environment lockfiles.
4. **Preservation.** The full lemma-constant ledger for P3, all failed widening attempts, and all pruned-search statistics are part of the record; negative results (e.g., "the LP gap cannot close below $x\%$ in this basis") must be stated, not omitted.
5. **Honest reporting.** The report opens with: section 2 standard met or not met - expected **not met**. Every claim is tagged by dimension, potential class, competitor class (all configurations vs. restricted), and $N$-range; putative (uncertified) minima are always visually separated from certified enclosures.
