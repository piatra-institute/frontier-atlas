# PROMPT FOR PROVING NÉEL ORDER IN THE SPIN-1/2 SQUARE-LATTICE HEISENBERG ANTIFERROMAGNET

## Ground-state long-range order at $S=1/2$: closing the infrared-bound constant gap

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 32 of 50 (Tier 3)
**Source:** top-50 list #10, category B (rigorous many-body and condensed matter)
**Modes:** `[cert]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The ground state of the spin-1/2 nearest-neighbor Heisenberg antiferromagnet on the square lattice is ordered: quantum Monte Carlo pins the staggered magnetization at $m_s \approx 0.307$ with no serious dissent. Yet no proof exists. The reflection-positivity/infrared-bound program (Dyson–Lieb–Simon 1978; ground-state versions by Neves–Perez 1986 and Kennedy–Lieb–Shastry 1988) proves Néel order for all $S \ge 1$ on the square lattice and for $S = 1/2$ in three dimensions - and fails at $S = 1/2$ in two dimensions by a small quantitative margin in the final constant inequality. The obstruction is arithmetic, not conceptual: sharpen a chain of explicitly computable constants (Watson-type lattice integrals, sum rules, double-commutator bounds, finite-cluster inputs) until the inequality closes. This is exceptionally well matched to certified computation: every constant in the chain can be enclosed with interval arithmetic, and every proposed sharpening is falsifiable by a machine-checked number. The complete resolution defined in section 2 is the target, and anything less must be reported as a partial result, never represented as a solution. The margin has resisted since 1988; the graded targets of section 3 are the session's realistic goal.

## 1. Exact problem statement

Let $\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^2$ be the $L\times L$ torus, $L$ even. On $\mathcal{H}_L = \bigotimes_{x\in\Lambda_L}\mathbb{C}^2$ define the spin-1/2 Heisenberg antiferromagnet

\[
H_L \;=\; \sum_{\langle x,y\rangle} \mathbf{S}_x\cdot\mathbf{S}_y ,
\qquad \mathbf{S} = \tfrac{1}{2}\,(\sigma^x, \sigma^y, \sigma^z),
\]

the sum over nearest-neighbor pairs, coupling $J = 1$. Work in the $S^z_{\mathrm{tot}} = 0$ sector, where the finite-volume ground state is unique (Marshall; Lieb–Mattis); let $\langle\cdot\rangle_L$ denote its expectation. With the sublattice sign $(-1)^{|x|} = (-1)^{x_1 + x_2}$ and Néel vector $Q = (\pi, \pi)$, define the staggered magnetization squared

\[
m_s^2 \;=\; \liminf_{L\to\infty}\; \frac{1}{|\Lambda_L|^2} \sum_{x,y\in\Lambda_L} (-1)^{|x-y|}\, \big\langle \mathbf{S}_x\cdot\mathbf{S}_y \big\rangle_L .
\]

**Target theorem (Néel order).**

\[
m_s^2 \;>\; 0 .
\]

Equivalently: infinite-volume ground states exhibit long-range staggered correlations, $\liminf_{|x-y|\to\infty} (-1)^{|x-y|}\langle \mathbf{S}_x\cdot\mathbf{S}_y\rangle > 0$, and the $SU(2)$ symmetry is broken in the thermodynamic limit. Reference value (not part of the theorem): $m_s = 0.3070(3)$ (Sandvik, QMC, 1997; verify digits).

The machinery to beat, stated to fix notation. Let $\gamma(k) = \tfrac12(\cos k_1 + \cos k_2)$ and let $\widehat{S^z_k}$ be the Fourier transform of $S^z_x$ on the torus. The $T=0$ infrared bound of Neves–Perez / Kennedy–Lieb–Shastry (via reflection positivity and Gaussian domination on the torus) gives, for $k \ne Q$ (up to normalization conventions to be fixed in-session and used consistently),

\[
\big\langle \widehat{S^z_{-k}}\, \widehat{S^z_k} \big\rangle \;\le\; \frac{1}{2}\sqrt{\frac{C_k}{E_k}},
\qquad
C_k = \big\langle\, [\,\widehat{S^z_{-k}}, [H, \widehat{S^z_k}]\,] \,\big\rangle,
\]

with $E_k$ the reflection-positivity dispersion (proportional to $1 + \gamma(k)$ in the standard convention). The double commutator evaluates against the bond energy, so $C_k$ is bounded through the ground-state energy density $e_0$; combined with the sum rule

\[
\frac{1}{|\Lambda_L|}\sum_k \big\langle \widehat{\mathbf{S}_{-k}}\cdot\widehat{\mathbf{S}_k} \big\rangle \;=\; S(S+1) \;=\; \tfrac34,
\]

one obtains a lower bound of the schematic form

\[
m_s^2 \;\ge\; S(S+1) \;-\; 3\int_{[-\pi,\pi]^2} \frac{d^2k}{(2\pi)^2}\; \frac{1}{2}\sqrt{\frac{C(k)}{E(k)}}\; .
\]

For $S \ge 1$ the right-hand side is positive; at $S = 1/2$ the integral exceeds $3/4$ by a small margin - the literature puts the deficit at the few-percent level (re-derive and certify the exact margin; do not quote it from memory). The problem adopted here is the isotropic model above; anisotropic (XXZ) versions appear only as graded targets.

Conventions to fix once and use everywhere (the derivation is convention-fragile):

- Fourier normalization: $\widehat{S^z_k} = |\Lambda_L|^{-1/2}\sum_x e^{-ik\cdot x} S^z_x$, $k \in \frac{2\pi}{L}\mathbb{Z}^2 \cap (-\pi,\pi]^2$.
- The infrared bound holds for the two-point function at $k \ne Q$ only; the $k = Q$ mode carries the order parameter and is excluded from the integral by construction - the finite-$L$ bookkeeping of the excluded modes must be explicit.
- All statements at finite $L$ first, thermodynamic limits taken last with proved monotonicity or subsequence arguments; no formal interchange of limit and integral without proof.

## 2. Complete-resolution standard

A complete resolution is a proof of $m_s^2 > 0$ for the isotropic spin-1/2 square-lattice Heisenberg antiferromagnet as normalized above, with:

- every analytic inequality fully proved;
- every numerical constant in the proof enclosed by certified interval arithmetic with an independent checker;
- no unproved spectral or correlation inputs (QMC values may motivate, never justify).

The proof may combine reflection positivity, sum rules, finite-cluster spectral data, or entirely new methods.

**Not accepted as resolution:**

- QMC, DMRG, series-expansion, or spin-wave evidence of order, at any precision, including the universally believed $m_s \approx 0.307$.
- A proof for $S \ge 1$, for $d \ge 3$, for the XY model, or for XXZ anisotropy $\Delta_a \ne 1$, represented as covering the isotropic $S = 1/2$ 2D case (these are the known frontier; section 4).
- Positive-temperature claims: there is no order at $T > 0$ in 2D (Mermin–Wagner); any claimed finite-$T$ route to this theorem is simply wrong.
- Order for modified interactions (added second-neighbor couplings, staggered fields, decorated lattices) passed off as the physical model.
- An improved constant chain that still fails to close the inequality, represented as anything other than a quantitative partial result (a legitimate P2 outcome, not a resolution).
- Interval evaluations without preserved code and independent checkers.

## 3. Graded partial-result targets

**P1 - The DLS/NP/KLS constant chain, re-derived and certified.**
- Task: reproduce the full $T=0$ infrared-bound argument self-contained: Gaussian domination on the torus, the infrared bound, the double-commutator evaluation, the sum rule, the final inequality. Enclose every constant - in particular the 2D Watson-type integral $\int \frac{d^2k}{(2\pi)^2}\sqrt{C(k)/E(k)}$ with the standard choices of $C, E$ - in certified interval arithmetic (Arb). State the exact certified deficit at $S = 1/2$ and the certified surplus at $S = 1$ (control case).
- Certificate: the complete proof-chain document plus an interval manifest; independent re-integration with a second quadrature implementation.
- Value: the community lacks a single certified statement of "how much is missing"; this is the baseline for everything below.

**P2 - Certified sharpening of individual links.**
- Task: attack each inequality in the chain separately for slack: (a) better upper bounds on $C(k)$ via improved certified enclosures of the energy density $e_0$; (b) sharper sum-rule usage (full vector sum rule and $SU(2)$ invariance versus single-component accounting); (c) $k$-region splitting - different bounds near and far from $Q$, where the generic bound is loosest.
- Certificate: each sharpened link is a lemma with proof plus certified numerics; report the new total deficit after each.
- Value: any strict certified reduction of the P1 deficit is a standalone result; the deficit trajectory tells the field whether this road can ever close.

**P3 - Hybrid finite-cluster + infrared-bound schemes.**
- Task: Kennedy–Lieb–Shastry-style improvements inject exact small-cluster data into the reflection-positivity framework via chessboard estimates. Redo this with modern certified diagonalization: tori up to $2^{24}$–$2^{26}$ Hilbert dimension before symmetry reduction (e.g. $4\times4$ exactly, $6\times4$ and tilted $\sqrt{20}$/$\sqrt{26}$ clusters as stretch), with interval-certified ground-state correlations entering as rigorous inputs through a fully proved transfer theorem.
- Certificate: the transfer theorem proved in full; certified cluster data with independent checkers.
- Value: state precisely how the deficit shrinks with cluster size, and whether the *certified* scheme (not numerics) closes at a computable size - if yes, that is the path to full resolution and must be stated as an explicit finite computation with a resource estimate.

**P4 - XXZ interpolation with certified thresholds.**
- Task: for $H(\Delta_a) = \sum_{\langle xy\rangle}\big[S^x_xS^x_y + S^y_xS^y_y + \Delta_a S^z_xS^z_y\big]$: Kennedy–Lieb–Shastry (1988) proved ground-state order at the XY point ($\Delta_a = 0$) for $S = 1/2$, $d \ge 2$; Kubo–Kishi (1988) proved order windows in $\Delta_a$ (verify the exact proven intervals on both the planar and Ising sides, and the width of the unproven window containing $\Delta_a = 1$). Recompute all thresholds with certified constants and sharpen them.
- Certificate: theorems plus interval manifests; the deliverable is the largest certified ordered region $[0, \Delta_a^-] \cup [\Delta_a^+, \infty)$ and the exact residual window.
- Value: each certified narrowing of the window around the isotropic point is independently publishable.

**P5 - Necessary-condition ledger and no-go mapping.**
- Task: determine whether the obstruction is slack in the inequalities or a genuine limitation of Gaussian domination at $S = 1/2$: formulate the optimization over the admissible class of bounds of the given functional form, with rigorously bounded inputs ($e_0$, structure-factor constraints), and resolve it with certified arithmetic - does the *optimal* bound of this shape close or provably fail?
- Certificate: a clean optimization statement and its certified resolution.
- Value: tells every future attacker where not to dig; a proved "this functional form cannot close" is a significant negative theorem.

**P6 - Conditional resolution with an explicit finite certificate.**
- Task: strongest short of resolution - a proved theorem "if the certified cluster quantity $X_C$ on cluster $C$ satisfies $X_C < t$, then $m_s^2 > 0$", where non-certified numerics indicate $X_C < t$ plausibly holds for a cluster within present or near-future reach.
- Certificate: the theorem; the exact computation, its dimension, and certification cost stated.
- Value: reduces a 38-year-old open problem to a named finite computation.

## 4. Known results and prior art

- Marshall (1955); Lieb–Mattis (1962): sign structure; total-spin-0, in-sector-unique ground state on bipartite lattices.
- Mermin–Wagner (1966): no order at $T > 0$ in 2D - forces the ground-state formulation.
- Fröhlich–Simon–Spencer (1976): infrared bounds, classical case.
- Dyson–Lieb–Simon (1978): reflection positivity and infrared bounds for quantum spin systems; order at $T > 0$ in $d \ge 3$ (spin thresholds per case - verify).
- Neves–Perez (1986): $T = 0$ infrared bound; Néel order for the square lattice at $S \ge 1$.
- Kennedy–Lieb–Shastry (1988, J. Stat. Phys.): Néel order for $S = 1/2$ on the cubic lattice; 2D constant refinements. Kennedy–Lieb–Shastry (1988, PRL): ground-state order for the XY model, $S = 1/2$, $d \ge 2$.
- Kubo–Kishi (1988): order windows for the $S = 1/2$ XXZ model in 2D near the XY and deep-Ising regimes (verify exact anisotropy ranges).
- Ozeki–Nishimori and successors (late 1980s–1990s): incremental constant improvements (verify which are the current record - this matters directly for P1's baseline).
- Tasaki, *Physics and Mathematics of Quantum Many-Body Systems* (2020): the modern pedagogical account of the chain; recommended P1 baseline text.
- Sandvik (1997): stochastic-series-expansion QMC, $m_s = 0.3070(3)$ (verify digits); later QMC only tightens it. No numerical work disputes ordering.
- Post-2020 literature: search explicitly for any sharpening of infrared-bound constants or new RP-adjacent methods - an overlooked improvement would live exactly there.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

Modes `[cert]` `[proof]`. Single-workstation first computations.

1. **Certified Watson-type integrals (Arb).** Implement $\int_{[-\pi,\pi]^2}\sqrt{C(k)/E(k)}\,d^2k$ with rigorous quadrature. The integrand has inverse-square-root singularities at $k = Q$ (and $k = 0$): substitute $k = Q + r\omega$, certify the local expansion by hand-proved bounds, and apply Arb-certified quadrature on the regular remainder. Expected failure mode: naive global interval quadrature stalls at the singularity - the local analysis must be proved, not patched.
2. **Certified $e_0$ enclosures.** Upper bound: exact-rational Rayleigh quotients of explicit variational states (small-bond-dimension tensor states or Huse–Elser-type wavefunctions with rational parameters) on tori, transferred to infinite volume by proved subadditivity. Lower bound: Anderson-type cluster bounds from certified diagonalization; more ambitiously, an SDP lower bound on the energy density via the plaquette marginal problem, solved with SDPA-GMP and certified by exact-rational dual feasibility (a rigorous lower bound regardless of solver status).
3. **Cluster diagonalization for P3.** Sparse Lanczos in C++/Julia with $S^z$, momentum, and point-group reduction; interval-certified ground-state energy and correlations via residual-plus-separation bounds. Checker: independent Python re-verification of residuals and of the chessboard-transfer inequalities.
4. **Symbolic bookkeeping.** The chain of inequalities is riddled with convention traps (factors of 2, sublattice vs. full-lattice sums, component vs. vector sum rules). Maintain the entire derivation in a CAS worksheet (SymPy or Mathematica) with numbered steps; the interval code consumes constants only from that worksheet. Expected failure mode: silent convention mismatch between literature sources - the worksheet is the defense, and cross-checking $S = 1$ (where the result is known true) is the unit test.
5. **Formalization seed (`[proof]`, optional).** Reflection positivity and Gaussian domination on a finite torus are finite-dimensional statements; a Lean 4 formalization of Gaussian domination is a reusable artifact even if the full chain stays on paper. Expected failure mode: Mathlib gaps in tensor-product operator algebra; timebox.
6. **Order of battle.** P1 fully before P2; P5's optimization only after P2 has exposed where slack lives; P3 clusters scale with available memory, and the $4\times4$/$6\times4$ pair suffices for a first certified data point.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All final constants as certified intervals (Arb, directed rounding, precision recorded); variational energies in exact rational arithmetic; SDP lower bounds certified by exact-rational dual feasibility, never by solver status codes. Floating point is exploratory only.
2. **Independent verification.** Two independent quadrature implementations (different algorithms and libraries) for every integral entering a theorem; standalone checkers for eigenvalue and correlation certificates; the inequality chain re-derived in a separate session from the CAS worksheet before any release.
3. **Reproducibility.** Worksheet, code, solver versions, precisions, cluster geometries, and all parameters recorded; SHA-256 manifest over every artifact including SDP problem and solution files.
4. **Preservation.** All code - including failed sharpening attempts in P2 and the optimization scaffolding of P5 - is part of the record; unpreserved exploration must be declared explicitly rather than obscured.
5. **Honest reporting.** The report opens by stating whether $m_s^2 > 0$ was proved for the isotropic $S = 1/2$ model (expected: no), then gives the certified deficit before and after this session's improvements, the certified XXZ window, and a precise statement of the remaining obstruction. QMC values are context, never evidence.
