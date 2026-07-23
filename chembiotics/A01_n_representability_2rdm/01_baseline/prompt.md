# PROMPT FOR USABLE N-REPRESENTABILITY CONDITIONS ON THE 2-RDM

## Certified positivity hierarchies for the two-electron reduced density matrix

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-01 of 21
**Source:** chem/bio top-50 list #5, section A (electronic structure)
**Modes:** `[sym]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The ground-state energy of an $N$-electron system is an exact *linear* functional of the two-electron reduced density matrix (2-RDM). If the set of $N$-representable 2-RDMs could be characterized by tractable constraints, one would compute correlated ground-state energies by convex optimization, bypassing the exponentially large wavefunction entirely - decisive for strongly correlated matter.

The exact conditions are known to be formally characterizable (Coleman) but the decision problem is QMA-complete. The working substitutes are the $(2,q)$-positivity families D, Q, G, T1, T2 (Garrod–Percus; Erdahl; Zhao–Braams–Fukuda–Overton–Percus; Mazziotti), imposed as semidefinite constraints in a variational SDP that returns a *rigorous lower bound* to the ground-state energy.

This is the most algebraic, most certifiable Pack A item: an SDP optimum carries a dual certificate that, rounded to exact rational arithmetic, proves a bound no floating-point run can be argued away. The **on-machine verifier** is twofold:

- the exact full-CI energy on small systems, against which the 2-RDM lower bound is compared; and
- a rational dual-feasibility certificate that proves the lower bound independently of the SDP solver.

Anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

Fix a finite one-particle basis of $r$ spin-orbitals. Second-quantized creation/annihilation operators $a_p^\dagger, a_p$ obey the fermionic anticommutation relations. For an $N$-electron pure or ensemble state $\rho$ on the antisymmetric Fock sector, the (unnormalized) 2-RDM is

\[
{}^2D^{\,pq}_{st} = \operatorname{Tr}\!\big(\rho\, a_p^\dagger a_q^\dagger a_t a_s\big),
\qquad p,q,s,t \in \{1,\dots,r\},
\]

a Hermitian operator on the two-particle space, antisymmetric under $p\leftrightarrow q$ and $s\leftrightarrow t$, with trace $\operatorname{Tr}\,{}^2D = N(N-1)$.

For a spin-free non-relativistic Hamiltonian with one- and two-electron integrals $h_{ps}$ and $v_{pq,st}$, the electronic energy is the *exact linear functional*

\[
E[{}^2D] = \sum_{pq,st} {}^2K^{\,pq}_{st}\, {}^2D^{\,pq}_{st},
\]

where the reduced Hamiltonian ${}^2K$ folds the one-electron part into the two-particle space via the fixed $N$. No approximation enters $E[\cdot]$; the entire difficulty is the constraint set.

**Definition (ensemble $N$-representability).** A candidate ${}^2D$ is $N$-representable iff there exists an $N$-electron ensemble $\rho \succeq 0$, $\operatorname{Tr}\rho = 1$, whose contraction is ${}^2D$. Let $\mathcal{P}^2_N$ denote this convex set of Hermitian two-particle operators. The exact variational problem is

\[
E_0 = \min_{{}^2D \in \mathcal{P}^2_N} E[{}^2D],
\]

equal to the true ground-state energy. Relaxing $\mathcal{P}^2_N$ to any tractable convex superset $\mathcal{S} \supseteq \mathcal{P}^2_N$ yields a **rigorous lower bound**

\[
E_{\mathcal S} = \min_{{}^2D\in\mathcal S} E[{}^2D] \;\le\; E_0 .
\]

Two representability notions must be kept distinct. *Ensemble* $N$-representability (above) is the convex hull relevant to the variational lower bound and is the target here. *Pure-state* $N$-representability (${}^2D$ arising from a single antisymmetric $|\Psi\rangle$) is a strictly smaller, non-convex set and carries additional generalized Pauli constraints; it is not required for the energy lower bound and is not imposed. All conditions below are ensemble-necessary.

**The admissible relaxations.** The metric/positivity conditions are semidefinite constraints on linear images of ${}^2D$:

- **D:** ${}^2D \succeq 0$ (the 2-RDM itself PSD).
- **Q:** the two-hole matrix ${}^2Q$, a fixed affine image of ${}^2D$, satisfies ${}^2Q \succeq 0$.
- **G:** the particle–hole matrix ${}^2G \succeq 0$ (Garrod–Percus).
- **T1, T2:** three-body positivity conditions ${}^3T_1 \succeq 0$, ${}^3T_2 \succeq 0$ (Erdahl; Zhao et al.), affine images of the 2-RDM lifted with the appropriate contraction identities.

Standard hierarchies are **DQG** (the $(2,2)$-positivity conditions) and **DQGT1T2** (partial $(2,3)$-positivity). Linear constraints - Hermiticity, antisymmetry, trace, contraction ${}^2D \to {}^1D$, and the $(1,1)$-consistency ${}^1D + {}^1Q = I$ - are imposed exactly.

**Units and accuracy threshold.** Energies are in **Hartree** (atomic units). For a given system/basis, report the *certified gap*

\[
\Delta = E_0^{\text{FCI}} - E_{\mathcal S} \;\ge\; 0,
\]

where $E_{\mathcal S}$ is the certified lower bound. A target of "$1\,\mathrm{mHartree}$" or "chemical accuracy" is admissible only when written as a number: the claim must be a certified $\Delta$ with an explicit sign ($\Delta \ge 0$ always) and magnitude in Hartree, on a named system and basis.

## 2. Resolution standard

The full problem - a tractable exact characterization of $\mathcal{P}^2_N$ - is QMA-complete and will not be resolved. What *can* be resolved, and is the object of this pack, is one or both of the following.

1. A **certified SDP pipeline** that, for a named Hamiltonian $({}^2K)$ and relaxation $\mathcal S \in \{$DQG, DQGT1T2, $\dots\}$, outputs a lower bound $E_{\mathcal S}$ **together with an exact rational dual-feasible certificate** proving $E_{\mathcal S} \le E_0$ with no floating-point trust. The certificate is a rational dual point $(y, Z)$ with $Z \succeq 0$ (verified by exact/interval Cholesky or LDL$^\top$) satisfying dual feasibility exactly, giving $E_{\mathcal S} = b^\top y$.

2. Either (a) a **new necessary $N$-representability condition** - an operator inequality $M[{}^2D] \succeq 0$ valid for every $N$-representable ${}^2D$ - proved symbolically and shown by a certified separation example to be *not* implied by DQGT1T2; or (b) a **certified separation example**: an explicit ${}^2D$ satisfying a named relaxation yet provably non-$N$-representable (it violates a proved necessary condition), with both facts certified in exact arithmetic.

**Not accepted as resolution:**

- A floating-point SDP energy reported as a "lower bound" with no exact dual certificate - the solver's interior-point iterate is dual-*infeasible* by construction and the reported bound can be above $E_0$.
- A new condition demonstrated only to *tighten energies numerically* on a benchmark set, without a symbolic proof of necessity **and** a certified example proving it is not redundant with DQGT1T2.
- A claim of "solving strong correlation via 2-RDM" from agreement with FCI on one molecule or one basis.
- "Approximately $N$-representable" 2-RDMs (purified, or with small negative eigenvalues) presented as satisfying the conditions.
- Replacing the lower-bound guarantee with a *variational upper bound* from a purified wavefunction and calling the gap closed.

**Benchmark-integrity clause.** The verifier here is unusually clean (exact FCI energies; exact certificates) but has two known biases.

- *System-size bias.* DQG lower bounds are excellent for small, weakly correlated systems and loosen for larger active spaces and metallic/degenerate cases; reporting only small clean systems overstates method quality. Guard: a held-out panel that must include at least one strongly correlated, near-degenerate case (e.g. a stretched-bond or transition-metal-dimer active space) where the gap is expected to be large, and the gap must be reported there too.
- *Solver-precision bias.* A bound that looks tight in double precision may be an artifact of an unconverged duality gap. Guard: the rational certificate is mandatory and is re-checked by an independent exact-arithmetic verifier (section 6). A tight $\Delta$ without a passing certificate is reported as "unverified", not as a bound.

## 3. Graded partial-result targets

**P1 - Reproduce the DQG / DQGT1T2 frontier with a certified toolchain.** For a fixed panel (He, Be, LiH, H$_2$O, N$_2$ at equilibrium and stretched, in STO-3G / 6-31G active spaces small enough for FCI), compute DQG and DQGT1T2 lower bounds and reproduce published gaps to within solver tolerance. *Certificate:* rational dual point verified by exact LDL$^\top$; the certified $E_{\mathcal S}$ matched against exact FCI. Independently valuable as a trusted baseline.

**P2 - Certified rational lower bounds, not just floating-point.** Upgrade every P1 energy to a *proved* lower bound: round the dual solution to rationals, restore exact dual feasibility (a small correction / dual-facial reduction), and verify $Z \succeq 0$ exactly. *Certificate:* the exact dual triple plus an independent checker recomputing $b^\top y$ and the PSD test in Arb/FLINT.

**P3 - Certified separation examples.** Construct explicit 2-RDMs that lie in the DQG (resp. DQGT1T2) feasible set but are provably non-$N$-representable, via a proved necessary condition they violate; and conversely exhibit ${}^2D$ that pass DQG but fail T2 with an exact witness. *Certificate:* exact evaluation of all defining inequalities on the constructed matrix.

**P4 - A new necessary condition, symbolically proved.** Derive an operator inequality valid on $\mathcal P^2_N$ (e.g. from a positive polynomial in $a^\dagger,a$ not spanned by the D/Q/G/T lifts), prove necessity symbolically, and certify non-redundancy against DQGT1T2 by a separation example (P3 machinery). *Certificate:* a machine-checkable symbolic proof of the operator-positivity identity plus a certified separating ${}^2D$.

**P5 - Symbolic characterization of a new condition class.** Give a closed, parameterized family of necessary conditions (a $(2,q)$ subfamily, or a new class from a named positive-operator construction) with a proof schema and a demonstrated energy improvement, certified, on the P1 panel and on at least one strongly correlated held-out system. *Certificate:* the proof schema plus certified lower bounds showing strict improvement $E_{\text{new}} > E_{\text{DQGT1T2}}$ with rational certificates on both.

## 4. Known results and prior art

- Coleman (1963), *Structure of Fermion Density Matrices* - ensemble $N$-representability of the 1-RDM solved; the 2-RDM problem posed.
- Garrod & Percus (1964) - the Q and G conditions.
- Erdahl (1978) - the T1, T2 three-index conditions; Erdahl & Jin (2000s) - geometry of the representability cone (verify).
- Nakata, Nakatsuji, Ehara, Fukuda, K. Nakata, Fujisawa (2001) - first large-scale variational 2-RDM SDP for molecules.
- Zhao, Braams, Fukuda, Overton, Percus (2004) - DQGT1T2 SDP; near-FCI energies on small molecules.
- Mazziotti - an extensive program: a large-scale boundary-point/RRSDP solver (2011), the $(2,q)$ hierarchy, and *Structure of Fermionic Density Matrices: Complete N-Representability Conditions*, PRL (2012), giving a formally complete but intractable $(2,\infty)$ family. Book: *Reduced-Density-Matrix Mechanics*, Adv. Chem. Phys. (2007).
- Liu, Christandl, Verstraete (2007) - pure-state $N$-representability (and the 2-RDM decision problem) is QMA-complete: the hardness ceiling.
- Fukuda, Braams, Nakata, Overton, Percus, Yamashita, Zhao (2007) - SDP algorithms and codes (SDPARA) for the 2-RDM problem (verify exact author list).
- van Aggelen, Verstichel, Bultinck, Van Neck and co-workers - spin/point-group adaptation, subsystem constraints, and diatomic dissociation studies (verify years).
- SDP solvers: SDPA / SDPA-GMP (Nakata) - arbitrary-precision primal-dual; Yamashita et al. Boundary-point and matrix-completion methods exploit the large sparse block structure.

Typical reported behavior to reproduce and then improve on: DQG recovers most of the correlation energy but leaves gaps of order $10$–$50\,\mathrm{mHartree}$ for multiply-bonded and stretched systems; adding T1/T2 tightens this substantially (often to a few mHartree) at markedly higher cost. These magnitudes are the concrete target the certified pipeline must first match before any new-condition claim is credible.

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 5. Attack plan

**Reference layer (verifier).** Build the FCI reference with **PySCF** (`fci` module) for every panel system; extract the exact reduced Hamiltonian ${}^2K$ from PySCF's AO/MO integrals. This is the ground truth $E_0^{\text{FCI}}$ and the exact 2-RDM for sanity checks. It fits comfortably on one workstation up to $\sim 14$–$16$ spin-orbitals.

**SDP layer `[cert]`.** Assemble the DQG (then DQGT1T2) SDP: block-diagonal PSD variables ${}^2D, {}^2Q, {}^2G$ (and ${}^3T_1, {}^3T_2$), the linear maps between them, and the trace/contraction constraints. Solve first in double precision with **SDPA** or a boundary-point solver to obtain a warm start, then in **SDPA-GMP** (arbitrary precision) to drive the duality gap down. Spin- and point-group-adapt the blocks to shrink the problem.

**Certification layer `[cert]`.** Take the high-precision dual iterate and round $y$ to rationals; reconstruct an *exactly* dual-feasible $(y, Z)$ by forming $Z = C - \sum_i y_i A_i$ over $\mathbb{Q}$ and verifying $Z \succeq 0$ by exact LDL$^\top$ (or an interval Cholesky in **Arb/FLINT**). The certified bound is $b^\top y \in \mathbb Q$. Where exact feasibility fails at the boundary, apply a small rational dual perturbation / facial reduction and re-verify, accepting a slightly weaker but *proved* bound.

**Symbolic layer `[sym]`.** For P4/P5, represent candidate necessary conditions as positivity of $\langle \Psi | O^\dagger O | \Psi\rangle \ge 0$ for chosen two/three-body operators $O$; expand into the 2-RDM using anticommutators in **SymPy** or a Grassmann-algebra module; test linear independence from the D/Q/G/T lifts by exact rank over $\mathbb Q$. Separation examples come from solving the P3 feasibility SDP that maximizes violation of the new condition subject to DQGT1T2.

**Expected failure modes.**

- *Boundary/degeneracy.* The optimum sits on a low-rank face where interior-point solvers stall and rational feasibility is delicate - mitigate with facial reduction and accept a marginally looser certified bound.
- *Precision blow-up.* SDPA-GMP cost grows fast with precision and block size; cap active spaces at what a workstation certifies overnight.
- *Symbolic redundancy.* Many "new" conditions collapse into DQGT1T2 - the exact-rank test must be run before any energy claim.
- *Spin-symmetry contamination* inflating apparent gaps if adaptation is done wrong.
- *Rational-rounding failure.* Aggressive denominators make the exact PSD test intractable; balance denominator size against the tightness sacrificed by the dual perturbation.

## 6. Verification and auditability requirements

1. **Exact or certified numerics.** Every lower-bound claim carries an exact rational dual certificate $(y, Z)$ with $Z \succeq 0$ proved by exact LDL$^\top$ or interval Cholesky; floating-point SDP output is exploration only and is never reported as a bound. Symbolic-condition claims carry exact-arithmetic linear-independence proofs.
2. **Independent verification.** A standalone checker - written separately from the solver - reads $({}^2K, \text{constraints}, y, Z)$ and recomputes $b^\top y$, dual feasibility, and $Z \succeq 0$ in Arb/FLINT. Separation examples are re-evaluated by a second routine that tests each defining inequality exactly.
3. **Reproducibility.** All integrals, SDP data (in exact rational SDPA-sparse form), seeds, solver versions and precisions, spin/point-group adaptation, and train/held-out panel splits are recorded; a SHA-256 manifest covers every artifact; the strongly-correlated held-out system is fixed *before* any energy is reported.
4. **Preservation.** SDP-generation code, the GMP solver configuration, the certificate-rounding routine, and the symbolic derivations are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front whether P1–P5 were met, reports the certified gap $\Delta$ on the strongly correlated held-out system (not only the clean small ones), distinguishes "certified bound" from "unverified floating-point energy" for every number, and never presents agreement with FCI on one system as a characterization of $\mathcal P^2_N$.
