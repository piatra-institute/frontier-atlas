# PROMPT FOR CERTIFYING A GLOBAL THOMSON MINIMUM AT AN OPEN \(N\)

## The Thomson problem: rigorous energy minimization of point charges on the sphere

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 50 of 50
**Area:** order theory & extremal set systems (discrete geometry / optimization)
**Modes:** `[opt]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Thomson problem asks for the arrangement of \(N\) points on the unit sphere \(S^2\) minimizing the Coulomb energy \(\sum_{i<j}1/|x_i-x_j|\). Physically it is the classical electrostatic minimum-energy configuration; mathematically it is a continuous global-optimization problem whose optima are, for most \(N\), known only as conjectures from extensive numerics.

Rigorous global optimality is proved for a short list - \(N\in\{2,3,4,5,6,12\}\) - with \(N=5\) requiring a computer-assisted proof (Schwartz) and \(N\in\{4,6,12\}\) following from universal optimality of sharp configurations (Cohn–Kumar). The problem is matched to certified optimization: interval arithmetic can rigorously enclose energies and certify critical points, and linear/semidefinite programming (Delsarte–Yudin, three-point SDP) yields rigorous lower bounds when the dual is made exact.

The target is a **certified global minimum for one open \(N\)** - a rigorously enclosed upper bound from a construction meeting a certified LP/SDP lower bound - or, short of that, certified bounds that tighten the gap. A numerical minimum, however well-converged, is never represented as a proof.

## 1. Exact problem statement

For \(N\ge2\), a configuration is a set \(\omega=\{x_1,\dots,x_N\}\subset S^2=\{x\in\mathbb R^3:|x|=1\}\) of distinct points. The **Coulomb (Riesz \(s=1\)) energy** is
\[
E(\omega)\;=\;\sum_{1\le i<j\le N}\frac{1}{|x_i-x_j|}.
\]
The **Thomson problem** is to determine the minimum energy and the minimizing configuration(s) up to isometry of \(S^2\):
\[
U(N)\;=\;\min_{\omega\subset S^2,\ |\omega|=N}\ E(\omega).
\]
It is the \(s=1\) member of the Riesz family \(E_s(\omega)=\sum_{i<j}|x_i-x_j|^{-s}\) (with \(s=0\) the logarithmic / Whyte problem and \(s\to\infty\) the Tammes packing problem, #24). This prompt fixes \(s=1\); Target P6 may perturb \(s\) around \(1\).

In inner-product coordinates \(t_{ij}=\langle x_i,x_j\rangle\in[-1,1)\), each squared distance is \(|x_i-x_j|^2=2-2t_{ij}\), so
\[
E(\omega)=\sum_{i<j}\frac{1}{\sqrt{2-2t_{ij}}},
\]
the form on which the Delsarte–Yudin linear-programming lower bounds of section 5 operate.
Existence of a minimizer follows from compactness; the difficulty is *global* optimality - the energy landscape has a number of distinct local minima that grows rapidly, empirically like \(e^{\,cN}\), in \(N\).

**Critical-point (force-balance) condition.** A configuration is a critical point of \(E\) on \((S^2)^N\) iff the net Coulomb force on each point is normal to the sphere, i.e. its tangential component vanishes:
\[
\Bigl(I-x_ix_i^{\!\top}\Bigr)\sum_{j\ne i}\frac{x_i-x_j}{|x_i-x_j|^{3}}=0\qquad\text{for all }i,
\]
where \(I-x_ix_i^{\!\top}\) projects onto the tangent plane at \(x_i\). A certified optimum must certify this equation (interval enclosure of the left side containing \(0\)) and local minimality of the tangential Hessian.

Rigorous global optima are known only for \(N\in\{2,3,4,5,6,12\}\) (verify): the antipodal pair, equilateral triangle, regular tetrahedron, triangular bipyramid (\(N=5\)), octahedron (\(N=6\)), and icosahedron (\(N=12\)). The first three have clean closed forms,
\[
U(2)=\tfrac12,\qquad U(3)=\sqrt3,\qquad U(4)=\tfrac{3\sqrt6}{2},
\]
from the great-circle diameter, the inscribed equilateral triangle, and the regular tetrahedron respectively. For all other \(N\) the optimum is conjectural, from numerical databases.

No informal target is admissible. A claimed optimum requires (i) a specific configuration with a rigorously enclosed energy and (ii) a rigorous lower bound on \(U(N)\); optimality holds only when the two meet:
\[
\underline u\ \le\ U(N)\ \le\ \overline u,\qquad \text{optimum certified when}\ \ \overline u=\underline u\ \ (\text{within the stated interval}).
\]

## 2. Resolution standard

For a target open \(N\), a complete resolution is a **certified global minimum**: a configuration \(\omega^\*\) with a rigorously enclosed energy \(E(\omega^\*)\in[\underline u,\overline u]\), and a rigorous lower bound \(L\le U(N)\) with \(L=\underline u\) (equivalently, the enclosure certifies \(E(\omega^\*)=U(N)\) up to the stated interval). Accepted certificate forms:

- **Upper bound:** an interval-arithmetic (Arb/FLINT) enclosure of \(E(\omega^\*)\) with directed rounding, from exact or interval-certified coordinates.
- **Lower bound:** a **Delsarte–Yudin linear-programming** bound with an **exact rational feasible dual** (a nonnegative-combination / SOS certificate checked by CAS), or a **three-point / SDP** bound (Bachoc–Vallentin style) with the SDP solution **rationally rounded** and re-verified exactly, or - for very small \(N\) - an interval **branch-and-bound** over the symmetry-reduced configuration space with verified enclosures.

A **certified Thomson optimum for \(N\)** is a matching interval upper bound and exact lower bound. Short of matching, the honest deliverable is the certified gap
\[
\Delta(N)\;=\;\overline u-L\;\ge\;0,
\]
reported as a rigorous enclosure of \(U(N)\in[L,\overline u]\); a session that only narrows \(\Delta(N)\) has produced a partial result, not a resolution.

**Not accepted as resolution.**

- A minimum from gradient descent / simulated annealing / L-BFGS, at any number of restarts, presented as proven - it certifies nothing about global optimality.
- A floating SDP or LP bound without an exact/interval-certified dual.
- An upper bound (configuration energy) with no matching rigorous lower bound.
- Conflating a deep local minimum with the global one, or citing agreement across numerical codes as proof.
- A claim of a "new proven \(N\)" without both certified bounds meeting.
- A certified critical point mistaken for a certified minimizer when the tangential Hessian positive-definiteness has not been verified (a saddle passes the force-balance test too).

## 3. Graded partial-result targets

- **P1 - reproduce the certified list.**
  Independently verify the known rigorous optima for \(N\le6\) and \(N=12\): re-enclose the energies in interval arithmetic, replay (or independently re-derive) Schwartz's \(N=5\) computer-assisted certificate, and verify the Cohn–Kumar sharp-configuration argument for \(N\in\{4,6,12\}\).
  *Certificate:* Arb enclosures plus the replayed/reconstructed optimality arguments.

- **P2 - certified upper bound at an open \(N\).**
  For a chosen open \(N\), take the conjectured optimum, certify it is a critical point (gradient enclosure contains \(0\)) and a local minimum (interval Hessian positive-definite on the tangent space), and report \(E(\omega^\*)\) as a validated interval.
  *Certificate:* Arb enclosures of energy, gradient, and Hessian, with interval-Newton local-uniqueness.

- **P3 - Delsarte–Yudin lower bound.**
  For the target \(N\), an exact rational LP lower bound on \(U(N)\) via an admissible potential (Gegenbauer-positive), with an exact feasible dual / SOS certificate.
  *Certificate:* the exact polynomial and its certified nonnegativity, re-checked by CAS.

- **P4 - SDP / three-point lower bound.**
  A Bachoc–Vallentin three-point SDP lower bound with the solution rationally rounded and re-verified exactly, tightening the gap to the conjectured optimum for the target \(N\).
  *Certificate:* the rounded exact dual and its verification.

- **P5 - a new certified global optimum (strongest short of the full landscape).**
  For one small open \(N\) (e.g. \(N=7\) or \(8\)), matching interval upper bound (P2) and exact lower bound (P3/P4, or symmetry-reduced interval branch-and-bound) that close the gap - the first Thomson value certified beyond the classical list.
  *Certificate:* both bounds meeting, fully independent.

- **P6 - rigidity / uniqueness or a Riesz-\(s\) neighborhood.**
  A certified local-uniqueness (rigidity) statement for the target configuration, or extension of a certified bound to a range of Riesz exponents \(s\) around \(s=1\).
  *Certificate:* interval-Newton uniqueness or the parametrized bound with certificates.

## 4. Known results and prior art

- **Origin.** J. J. Thomson (1904), the "plum-pudding" atomic model.
- **Rigorous optima.** \(N=2,3,4\) elementary; \(N=6\) (octahedron) and \(N=12\) (icosahedron) via **Cohn–Kumar (2007, JAMS)** universal optimality of sharp configurations; \(N=5\) (triangular bipyramid) via **Schwartz** (arXiv 1001.3702, 2010; *Experimental Mathematics* 2013), a computer-assisted proof also covering the \(s=2\) potential. Verify this list is still exactly \(\{2,3,4,5,6,12\}\).
- **Universal optimality.** Cohn–Kumar proved *sharp* configurations are universally optimal: a spherical \((2m-1)\)-design attaining exactly \(m\) distinct inner products among distinct points. On \(S^2\) the tetrahedron (a \(2\)-design), octahedron (\(3\)-design), and icosahedron (\(5\)-design) qualify,
\[
N=4,6,12\ \Longrightarrow\ \text{universally optimal}\ \Longrightarrow\ \text{Thomson-optimal},
\]
but no such coincidence exists for, e.g., \(N=7,8,9,10,11\), so those must be attacked per-\(N\). This is exactly why the rigorous list is short.
- **Lower-bound machinery.** Delsarte–Goethals–Seidel LP; Yudin and Kolushov–Yudin energy bounds; Cohn–Kumar LP framework; Bachoc–Vallentin (2008) three-point SDP. Recent exact-SDP optimality proofs for spherical codes (arXiv 2403.16874, 2024) illustrate the rational-rounding methodology (verify).
- **Numerics.** Extensive conjectured Thomson minima are tabulated (Womersley; Wales and co-workers; the Cambridge energy databases), with putative optima and their symmetry groups recorded for \(N\) into the thousands. These give candidate configurations and warm starts, not proofs, and the conjectured minimizer occasionally changes as searches deepen - so the candidate for a target \(N\) must be re-confirmed before it is certified.
- **Adjacent.** Kissing number in dimension 11 (#06) and the Tammes problem (#24) - the same sphere-optimization toolbox, distance maximization rather than energy minimization.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the exact list of rigorously solved \(N\), the current best SDP lower-bound techniques, and any newly certified values before choosing a target; spherical-optimization methods advanced through the early 2020s. No fabricated arXiv IDs, DOIs, or page numbers are to be introduced.

## 5. Attack plan

- **`[cert]` interval arithmetic.** Arb/FLINT enclosures of energy, gradient, and tangent-space Hessian; interval-Newton to certify critical points and local minimality; exact or algebraic coordinates for symmetric candidates. The Krawczyk operator on the tangential gradient map \(F\),
\[
K(\mathbf X)=\check{\mathbf x}-Y F(\check{\mathbf x})+\bigl(I-Y F'(\mathbf X)\bigr)(\mathbf X-\check{\mathbf x})\subseteq\operatorname{int}\mathbf X,
\]
certifies a unique critical point in the box \(\mathbf X\); a verified positive-definite tangential Hessian there certifies a strict local minimum. Exploit the conjectured symmetry group (dihedral / polyhedral) to reduce the effective dimension \(2N-3\).
- **`[opt]` LP/SDP lower bounds.** The Delsarte–Yudin bound: if \(h(t)=\sum_k \hat h_k\,C_k^{(1/2)}(t)\) satisfies \(\hat h_k\ge0\) for \(k\ge1\) and \(h(t)\le 1/\sqrt{2-2t}\) for \(t\in[-1,1)\), then
\[
U(N)\ \ge\ \tfrac12 N^2\,\hat h_0-\tfrac12 N\,h(1),
\]
so any Gegenbauer-nonnegative admissible \(h\) yields a rigorous lower bound; optimize over \(h\) by LP and certify the dual exactly (Sage exact LP / rational simplex). SOS certificates via SumOfSquares + SDPA-GMP, then rational rounding re-verified by CAS (Positivstellensatz). Three-point SDP (Bachoc–Vallentin) with rigorous rounding tightens further.
- **Global optimization.** After quotienting by the isometry group \(O(3)\) (dimension \(3\)), the reduced configuration space has dimension
\[
2N-3,
\]
so a full interval branch-and-bound is realistic only for the smallest \(N\); at \(N=7\) the space is already \(11\)-dimensional and strong symmetry reduction (fixing the conjectured stabilizer) is essential. Beyond small \(N\), B&B is infeasible on a workstation.
- **One-workstation scope.** Interval verification of a fixed configuration is cheap and reliable; LP/SDP bounds are feasible for a broad range of \(N\) but the gap to the conjectured optimum usually stays positive; certified global optimality by B&B is realistic only for the smallest open \(N\) with heavy symmetry use.
- **Failure modes.** Curse of dimensionality in global search; SDP ill-conditioning and rounding failure; interval blow-up if coordinates are not tight; a "verified critical point" that is only a saddle if the Hessian test is skipped; floating SDP that resists exact certification.

## 6. Verification and auditability requirements

1. **Exact/certified computation.** Every energy bound is an interval enclosure with directed rounding or an exact rational LP/SDP value; lower bounds carry exact/SOS-certified duals. Floating point is for exploration and warm-starting only, never for a certificate.
2. **Independent verification.** A standalone checker, independent of the optimizer, re-encloses the configuration's energy and re-verifies each LP/SDP dual by exact evaluation; a second interval library or CAS confirms the enclosures.
3. **Reproducibility.** Coordinates, symmetry reductions, LP/SDP formulations, solver versions, rounding procedures, and seeds recorded; SHA-256 manifest over every configuration, certificate, and bound.
4. **Preservation.** Optimizer, interval-verification, and SDP-rounding source is part of the record (the Hadamard-668 lost-source lesson). A gap that does not close is reported as bounds \([L,\overline u]\), not as a solved value.
5. **Honest reporting.** The report states plainly whether upper and lower bounds meet. A well-converged numerical configuration is reported as a certified **upper** bound at best; only matching certified bounds may be called a proven optimum, and the classical list is never claimed extended without both.

### Honest calibration

For most \(N\) the certified lower bound will sit strictly below the conjectured optimum, and the honest product is a pair of rigorous bounds
\[
L\ \le\ U(N)\ \le\ \overline u,\qquad \Delta(N)=\overline u-L>0,
\]
that tighten the gap - genuinely useful, not a proof. A single new certified global optimum (e.g. \(N=7\), where \(\Delta(N)\) is driven to \(0\)) would be a landmark on the scale of Schwartz's \(N=5\) and should be treated as ambitious; the classical rigorous list is short precisely because closing these gaps is hard.
