# PROMPT FOR PROVING THE SPECTRAL GAP OF THE SPIN-1 ANTIFERROMAGNETIC HEISENBERG CHAIN

## Haldane's conjecture at the Heisenberg point: a rigorous thermodynamic gap

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 30 of 50 (Tier 3)
**Source:** top-50 list #9, category B (rigorous many-body and condensed matter)
**Modes:** `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Haldane (1983) predicted that the integer-spin antiferromagnetic Heisenberg chain has a nonzero spectral gap above its ground state in the thermodynamic limit; for spin 1 the gap is numerically $\Delta \approx 0.4105\,J$ (White–Huse DMRG, 1993 - verify current best digits). Forty years on, no proof exists at the Heisenberg point. The proven cousin is the AKLT model (Affleck–Kennedy–Lieb–Tasaki, 1987–88), and since 2020 entire families of 2D AKLT-type models have fallen to a now-standard pipeline: a finite-size criterion (Knabe 1988; Gosset–Mozgunov 2016; Lemm-school refinements) converts a rigorous thermodynamic gap statement into a certified finite-cluster spectral computation. The missing piece is a criterion weak enough - in particular, one not requiring frustration-freeness - to bite at the Heisenberg point. This matches current AI methods because every layer is certifiable: interval Lanczos with directed rounding gives machine-checkable finite-cluster gap bounds, and the criteria themselves are short combinatorial-operator inequalities suitable for formalization. The complete resolution defined in section 2 is the target, and anything less must be reported as a partial result, never represented as a solution. Full resolution in one session is unlikely; the graded targets of section 3 are the realistic product.

## 1. Exact problem statement

Fix the on-site Hilbert space $\mathfrak{h} = \mathbb{C}^3$ carrying the spin-1 representation of $\mathfrak{su}(2)$: Hermitian operators $S^x, S^y, S^z$ with

\[
[S^x, S^y] = i S^z \ \text{(and cyclic)}, \qquad \mathbf{S}^2 = S(S+1)\,\mathbb{1} = 2\,\mathbb{1}.
\]

For a finite chain of $n$ sites, $\mathcal{H}_n = \bigotimes_{i=1}^{n} \mathbb{C}^3$. Define the Hamiltonian with open boundary conditions (OBC)

\[
H_n^{\mathrm{obc}} \;=\; \sum_{i=1}^{n-1} \mathbf{S}_i \cdot \mathbf{S}_{i+1},
\qquad
\mathbf{S}_i \cdot \mathbf{S}_{i+1} = S_i^x S_{i+1}^x + S_i^y S_{i+1}^y + S_i^z S_{i+1}^z,
\]

and with periodic boundary conditions (PBC)

\[
H_n^{\mathrm{pbc}} \;=\; H_n^{\mathrm{obc}} + \mathbf{S}_n\cdot\mathbf{S}_1 .
\]

The coupling $J$ is set to $1$; all gaps are in units of $J$. No anisotropy, no biquadratic term, no external field: this normalization is the adopted formulation, and results for modified Hamiltonians are not results about this one.

Let $E_0(H) \le E_1(H) \le \dots$ be the eigenvalues of a Hermitian $H$ counted with multiplicity, and define the finite-volume gap

\[
\gamma(H) \;=\; E_1(H) - E_0(H).
\]

For OBC spin-1 chains the ground state is asymptotically fourfold quasi-degenerate (Kennedy edge-spin-1/2 tower); the physically meaningful OBC gap is from that tower to the first bulk state above it, and any claim must state exactly which gap is bounded.

**Target theorem (Haldane gap).** There exists $\Delta > 0$ such that

\[
\liminf_{n\to\infty} \gamma\!\left(H_n^{\mathrm{pbc}}\right) \;\ge\; \Delta \;>\; 0 .
\]

Equivalently (and to be proved equivalent if used): the GNS Hamiltonian of the unique infinite-volume ground state of the spin-1 chain has spectrum $\{0\} \cup [\Delta', \infty)$ for some $\Delta' > 0$. A proof of a uniform-in-$n$ OBC gap above the edge-state tower is accepted if accompanied by the standard argument transferring it to the thermodynamic-limit statement.

Reference numerical value (not part of the theorem): $\Delta = 0.41050(2)$ from White–Huse (1993); later tensor-network work refines the fifth digit (verify current best value before citing digits). The theorem requires only $\Delta > 0$ with an explicit certified constant.

The working coordinate system is the bilinear–biquadratic deformation family

\[
H_n(\beta) \;=\; \sum_{i} \left[\, \mathbf{S}_i\cdot\mathbf{S}_{i+1} \;+\; \beta \,(\mathbf{S}_i\cdot\mathbf{S}_{i+1})^2 \,\right],
\]

with $\beta = 1/3$ the AKLT point and $\beta = 0$ the Heisenberg point. At $\beta = 1/3$ each local term is, up to affine normalization, the projector $P^{(2)}_{i,i+1}$ onto total pair spin 2, and the model is frustration-free; at every other $\beta$ on the path it is not. "Gap proven on $[\beta_0, 1/3]$" always means a certified lower bound $\Delta(\beta) > 0$, uniform on the closed interval.

## 2. Complete-resolution standard

A complete resolution is a proof, written in full mathematical detail, of the Target theorem with an explicit certified constant $\Delta > 0$ (any positive value; matching $0.4105$ is not required). If the proof is computer-assisted:

- every computational ingredient must be a certificate in exact or interval arithmetic with an independent checker;
- the reduction from the thermodynamic statement to the finite computation must be a fully proved theorem (Knabe-type or otherwise), not a plausibility argument;
- the finite computation must actually be completed and preserved, not estimated to be feasible.

**Not accepted as resolution:**

- Numerical gap estimates at any system size or by any method (DMRG, VMC, uncertified exact diagonalization), including extrapolations with error bars.
- A gap proof for the AKLT point or any $\beta \ne 0$, represented as covering the Heisenberg point.
- A gap proof for an anisotropic, dimerized, decorated, or boundary-modified Hamiltonian passed off as the physical model.
- Finite-size criteria proved as theorems but never successfully instantiated at $\beta = 0$ ("the criterion would apply if the finite gap exceeded $t$" without the certified computation showing that it does).
- Stability-theory arguments (Bravyi–Hastings–Michalakis style) applied outside their hypotheses - the perturbation from AKLT to Heisenberg is extensive and of order 1 per site, not small.
- Field-theory arguments (nonlinear sigma model, $\theta$-term) at any level of rigor short of complete proof.
- Conditional results whose hypothesis is itself an unproved spectral statement of comparable difficulty, unless labeled as a conditional partial result under section 3 (P6).

## 3. Graded partial-result targets

Ordered from most accessible to strongest short of resolution. Each stands alone.

**P1 - Certified finite-chain gaps for AKLT and Heisenberg, own toolchain.**
- Task: rigorous two-sided enclosures of the lowest two (PBC) and lowest five (OBC) eigenvalues of $H_n(\beta)$ for $\beta \in \{1/3, 0\}$, all $n$ up to the workstation limit (expect $n \approx 14$–$18$ with $S^z$/momentum/$SU(2)$ symmetry reduction).
- Certificate: interval-arithmetic residual-plus-separation bounds (Temple–Lehmann, or block Rayleigh–Ritz with certified separation), checkable by an independent verifier that only multiplies sparse exact matrices by interval vectors.
- Value: reproduces the known frontier (the finite-size gaps behind Knabe-type instantiations) under our own verified toolchain; the ground truth for everything below.

**P2 - Knabe and Gosset–Mozgunov thresholds, machine-checked and instantiated.**
- Task: reformalize the finite-size criteria for frustration-free translation-invariant chains - Knabe (1988): subchain gap $\epsilon_m > 1/(m-1)$ implies a thermodynamic gap with explicit constant; Gosset–Mozgunov (2016): improved threshold of order $6/(m(m+1))$ - with complete proofs. Instantiate at the AKLT point with the P1 enclosures.
- Certificate: gold standard is a Lean 4 formalization of the operator inequality; minimum is a fully detailed human proof plus the interval computation manifest. Output: an unconditional, independently checkable AKLT gap with explicit constant.
- Value: the pipeline's foundation, verified end to end for the first time in our infrastructure.

**P3 - Certified gap interval around AKLT in $\beta$.**
- Task: combine P2 with quantitative perturbation bounds. Since $\|(\mathbf{S}_i\cdot\mathbf{S}_{i+1})^2\| \le 4$ per bond, a certified AKLT-side gap plus norm-relative bounds proves $\gamma > 0$ on $\beta \in [1/3 - \delta,\, 1/3 + \delta]$. Knabe (1988) proved a small such interval; maximize the certified $\delta$ by optimizing criterion length $m$, the finite-size enclosures, and the perturbation decomposition (parts relatively bounded by $H(1/3)$ rather than by $\mathbb{1}$).
- Certificate: a theorem with all constants explicit plus the interval computation.
- Value: report the certified interval honestly against the distance $1/3$ to the Heisenberg point; any strict improvement over the published record is a result.

**P4 - Finite-size criteria for frustrated chains, as standalone theorems.**
- Task: the Heisenberg point is not frustration-free, and this is the true obstruction. Prove a Knabe-type theorem whose hypothesis is a certified finite-volume quantity of a *frustrated* chain. Candidate routes: subtract the exact local ground energy $e_0(\beta)\mathbb{1}$ per bond and control the non-commuting remainder; coarse-grain into blocks of $b$ sites so the blocked chain on $\mathbb{C}^{3^b}$ is frustration-free after certified truncation; martingale-method conditions (Nachtergaele 1996) with checkable finite-volume inputs.
- Certificate: complete proof; if the hypothesis is computable, the exact statement of the finite computation that would discharge it, with a resource estimate.
- Value: independently valuable even if the hypothesis is currently too strong to verify at $\beta = 0$; this is the missing piece named in the Abstract.

**P5 - Maximal certified gap interval toward the Heisenberg point.**
- Task: instantiate P4 (or an interpolation/quasi-adiabatic scheme with certified path bounds) to push the proven-gap interval from the AKLT side toward $\beta = 0$: prove $\gamma(\beta) \ge \Delta(\beta) > 0$ for all $\beta \in [\beta_0, 1/3]$ with the smallest achievable certified $\beta_0$.
- Certificate: theorem plus complete interval-arithmetic manifest.
- Value: each strict extension of the rigorously gapped interval is reportable; $\beta_0 = 0$ is full resolution.

**P6 - Conditional Haldane gap with an explicit finite certificate gap.**
- Task: strongest short of resolution - a fully proved theorem "if the certified quantity $Q_m$ (a specific finite-cluster spectral quantity at $\beta = 0$, cluster size $m$) satisfies $Q_m > t_m$, then the Haldane gap holds with $\Delta \ge f(Q_m, m)$", together with non-certified numerics indicating $Q_m > t_m$ plausibly holds at reachable $m$, and a precise account of the remaining certified computation.
- Certificate: the theorem; the numerics clearly firewalled as exploration.
- Value: discharging it at reachable $m$ would be the full resolution; even undischargeable, it pins the exact shape of the missing criterion.

## 4. Known results and prior art

- Haldane (1983): the conjecture, via large-$S$ mapping to the $O(3)$ nonlinear sigma model with $\theta = 2\pi S$; integer $S$ gapped, half-integer gapless.
- Lieb–Schultz–Mattis (1961); Affleck–Lieb (1986): half-integer chains have no gap above a unique ground state - the complementary rigorous statement, explaining why any proof must use integer-spin structure.
- Affleck–Kennedy–Lieb–Tasaki (1987 PRL; 1988 CMP): the AKLT model has a unique infinite-volume ground state, exponential decay, and a spectral gap, via the valence-bond-solid structure.
- Knabe (1988): finite-size criterion for frustration-free chains; clean AKLT gap proof and a gap on a small bilinear–biquadratic interval around the AKLT point.
- Nachtergaele (1996): martingale method - gaps from finite-volume conditions for a broad class including AKLT-type models.
- Gosset–Mozgunov (2016): improved 1D finite-size threshold of order $1/m^2$, qualitatively optimal.
- Lemm–Mozgunov (2019) and subsequent Lemm-school refinements: finite-size criteria for 2D lattices and decorated versions (verify exact scope of each paper).
- Lemm–Sandvik–Wang (2020); Pomata–Wei (2020): spectral gaps of spin-3/2 AKLT models on hexagonal and related trivalent/decorated 2D lattices via finite-size criteria discharged by large finite-cluster computations (verify the certification level - floating-point vs. certified - claimed by each paper).
- Bravyi–Hastings–Michalakis (2010); Michalakis–Zwolak (2013): gap stability for frustration-free Hamiltonians under weak local perturbations; hypotheses do not cover the AKLT→Heisenberg path at order-1 strength, but the technology informs P4.
- White–Huse (1993): DMRG, $\Delta = 0.41050(2)$, correlation length $\xi \approx 6.03$; modern tensor-network and QMC work agrees (verify current best digits).
- Interval-arithmetic eigenvalue certification is standard technology (Rump's INTLAB tradition; Arb); confirm which gap papers, if any, already used certified rather than floating-point Lanczos.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

Mode `[cert]`. Concrete first computations, all single-workstation.

1. **Sparse exact diagonalization core (C++ or Julia).** Build $H_n(\beta)$ in the $S^z_{\mathrm{tot}}$ basis with momentum (PBC) and, where worthwhile, full $SU(2)$ reduction. Dimensions: $3^{14} \approx 4.8\times 10^6$ raw; symmetry sectors bring $n = 16$–$18$ into Lanczos reach. Matrix entries are exact rationals (half-integers), so the Hamiltonian is exactly representable.
2. **Certification layer.** Floating-point Lanczos proposes eigenpairs; certification computes interval residuals $\|Hv - \theta v\|$ with directed rounding (Arb/FLINT via Arblib.jl or Nemo.jl, or MPFI in C++) and applies Temple–Lehmann/Kato bounds with a certified spectral-separation input from a second interval computation. The checker is a separate short program (Python, different interval library) that re-verifies residual and separation inequalities from stored vectors. Expected failure mode: separation certification near the OBC Kennedy tower - certify the four-state block jointly (block Rayleigh–Ritz) rather than state by state.
3. **Threshold instantiation.** Implement Knabe and Gosset–Mozgunov thresholds as exact rational inequalities; feed certified AKLT subchain gaps; emit the rigorous thermodynamic gap constant; optimize criterion length $m$ against certification cost.
4. **Perturbation ledger for P3.** Symbolically decompose $(\mathbf{S}\cdot\mathbf{S})^2$ in the pair-spin projector basis $\{P^{(0)}, P^{(1)}, P^{(2)}\}$; compute exact operator norms of the perturbation pieces relative to the AKLT projectors; produce the certified $\delta$-interval by rational-arithmetic optimization.
5. **Formalization target (Lean 4).** The Knabe combinatorial lemma - an inequality of the form $H^2 \ge c \sum (\text{subchain terms})$ for sums of projectors - is a finite-dimensional operator inequality with a short proof; formalize over an abstract finite-dimensional inner-product space using Mathlib's positive-semidefinite API. Expected failure mode: Mathlib friction on operator inequalities and spectral-theorem plumbing; timebox, and fall back to a fully explicit paper proof plus certified arithmetic.
6. **Exploratory probe for P6 (firewalled).** DMRG (ITensor) scans of candidate frustrated-criterion quantities $Q_m$ along $\beta \in [0, 1/3]$ to select which P4 criterion design has a fighting chance at $\beta = 0$ before investing proof effort. Never cited as evidence.
7. **Expected global failure modes.** Certified $n$ too small for any criterion to bite even at AKLT (mitigate: sharper separation bounds, larger $m$ via OBC subchains); P4 remainder terms uncontrollable at $\beta$ near 0 (report the boundary of controllability precisely - that boundary is itself a P5 deliverable).

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Hamiltonians stored with exact rational entries; every claimed eigenvalue bound is an interval statement with directed rounding (Arb/MPFI); Knabe-type thresholds evaluated in exact rational arithmetic. Floating-point Lanczos output is exploration only and never cited as evidence.
2. **Independent verification.** For each certified gap: a standalone checker (independent codebase, different language or at minimum different interval library) that loads stored candidate vectors and re-proves the residual and separation inequalities. Dual implementation (Julia + Python/C++) required for any bound entering a theorem statement.
3. **Reproducibility.** Record chain length, boundary conditions, symmetry-sector labels, $\beta$ as an exact rational, solver settings, library versions, and hardware; SHA-256 manifest over Hamiltonian generators, eigenvector files, interval logs, and checker outputs.
4. **Preservation.** All search code - ED, DMRG probes, threshold optimizers, and the failed criterion designs of P4 - enters the record; negative design knowledge is part of the deliverable. Anything not preserved must be stated explicitly rather than obscured.
5. **Honest reporting.** The final report opens with a single sentence stating whether the Target theorem of section 1 was proved (expected answer: no), then lists exactly which of P1–P6 were completed to certificate standard, which interval of $\beta$ is now rigorously gapped, and what stands between the strongest result and the Heisenberg point. DMRG numbers are always labeled non-rigorous.
