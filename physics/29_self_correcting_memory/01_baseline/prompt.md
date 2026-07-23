# PROMPT FOR DECIDING THE EXISTENCE OF A 3D SELF-CORRECTING QUANTUM MEMORY

## Finite-temperature topological order and passive quantum memories in three dimensions

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 29 of 50 (Tier 3)
**Source:** top-50 list #8, category A (quantum information)
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Does there exist a local Hamiltonian in three spatial dimensions whose ground space stores logical qubits that survive thermal noise for a time growing without bound in the system size, with no active error correction? The 4D toric code achieves this (Dennis–Kitaev–Landahl–Preskill 2002; rigorous thermal stability Alicki–Horodecki–Horodecki–Horodecki 2010), 2D stabilizer models provably cannot (Bravyi–Terhal 2009), and 3D is open: Haah's cubic code has an energy barrier growing only as $\log L$ and a memory time that improves with $L$ only up to a temperature-dependent cutoff (Bravyi–Haah 2011–2013).
The search space - translation-invariant 3D stabilizer and CSS codes, fracton models - is enumerable, with machine-checkable figures of merit (logical dimension, distance, energy-barrier bounds), which is why this problem is matched to current AI methods in `[search]` mode.
The complete resolution defined in section 2 is the target; anything less - including any energy-barrier result without a thermal memory-time statement - must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

**Hamiltonian class.** Fix a cubic lattice $\Lambda_L=(\mathbb{Z}/L\mathbb{Z})^3$ with $q$ qubits per site (Hilbert space $(\mathbb{C}^2)^{\otimes q|\Lambda_L|}$). A *local Hamiltonian family* is $H_L=-\sum_a h_a$ where each $h_a$ is supported on a ball of radius $r=O(1)$, $\|h_a\|\le 1$, with translation invariance assumed for the primary (search-mode) formulation. The *stabilizer subclass*: $h_a=P_a$ commuting Pauli projectors, i.e. $H_L$ is defined by a translation-invariant stabilizer group $\mathcal{S}_L$ with local generators; *CSS subclass*: generators are pure-$X$ or pure-$Z$. The code space $\mathcal{C}_L$ is the ground space; $k(L)=\log_2\dim\mathcal{C}_L$ logical qubits.

**Thermal dynamics.** Couple every qubit weakly to a thermal bath at inverse temperature $\beta$; evolve by the Davies generator (weak-coupling limit)

\[
\mathcal{L}_\beta(\rho)\;=\;-i[H_L,\rho]\;+\;\sum_{a,\,\omega} h(\omega)\Big(S_a(\omega)\,\rho\, S_a(\omega)^\dagger-\tfrac12\big\{S_a(\omega)^\dagger S_a(\omega),\rho\big\}\Big),
\qquad h(-\omega)=e^{-\beta\omega}h(\omega),
\]

where the $S_a(\omega)$ are the Bohr-frequency components of single-qubit Pauli couplings $S_a$, and $h$ is any admissible KMS spectral function with $h(\omega)>0$ on the Bohr spectrum.
The Davies semigroup is the adopted noise model; results for other local, detailed-balanced semigroups are acceptable if the substitution is stated as a hypothesis.

**Memory time.** Fix an encoding of $k$ logical qubits and a decoder $\mathcal{D}$ (any efficient map from the final state to the logical algebra; the decoder may depend on $L$ but acts once, at read-out - no mid-run intervention). Define

\[
\tau(L,\beta)\;=\;\sup_{\mathcal{D}}\ \inf_{\text{logical states }\psi}\ \sup\Big\{t:\ \big\|\mathcal{D}\big(e^{t\mathcal{L}_\beta}(\rho_\psi)\big)-\psi\big\|_1\le 1/3\Big\}.
\]

**Definition (self-correcting).** The family $\{H_L\}$ is a *self-correcting quantum memory* if there exists $\beta_0<\infty$ and $k(L)\ge1$ such that for all $\beta\ge\beta_0$,

\[
\tau(L,\beta)\;\ge\;c(\beta)\,L^{\alpha}\quad\text{for some }\alpha>0\text{ and all }L,
\]

i.e. $\tau(L,\beta)\to\infty$ at fixed temperature.
(Exponential growth is the expected profile, cf. 4D; unbounded polynomial growth at fixed $\beta$ already qualifies.)

**The open question (adopted formulation).** Does a 3D self-correcting quantum memory exist within the class of local, bounded-strength, translation-invariant Hamiltonian families with local Davies dynamics? Two graded sub-questions:

- **(Q-stab)** within commuting Pauli (stabilizer) families - the enumerable class;
- **(Q-gen)** within general local Hamiltonians (including non-commuting and subsystem/gauge models).

A negative answer to (Q-stab) with a complete proof, or a positive answer to either, resolves the problem at the corresponding level.

**Energy barrier (auxiliary figure of merit).** For a stabilizer family, define

\[
\Delta(L)\;=\;\min_{\ell\,\text{nontrivial logical}}\ \ \min_{\substack{P_0=I,\,P_T=\ell\\ P_{t+1}=P_t\cdot(\text{one single-qubit Pauli})}}\ \ \max_{0\le t\le T}\ \big(\langle g|P_t^\dagger H_L P_t|g\rangle-E_0\big),
\]

the minimax energy along single-Pauli walks from the identity to a nontrivial logical operator, started in a ground state $|g\rangle$.
For fixed $L$ and integer energies this is a finite combinatorial quantity - exactly the machine-checkable object of P1–P5.
Barrier growth is a proxy, not the definition: the resolution standard is stated in terms of $\tau(L,\beta)$ only.

## 2. Complete-resolution standard

One of the following, with complete proofs:

1. **Existence.** An explicit 3D family $\{H_L\}$ in the class above, an explicit decoder, and a rigorous lower bound $\tau(L,\beta)\ge c(\beta)L^{\alpha}\to\infty$ for all $\beta\ge\beta_0$, proved for the Davies dynamics (not merely for a phenomenological stochastic model, unless accompanied by a reduction theorem).
2. **Nonexistence for (Q-stab).** A theorem: every translation-invariant 3D commuting-Pauli family with $k(L)\ge1$ has $\tau(L,\beta)\le C(\beta)\,f(L)$ with $f$ bounded (or growing slower than any positive power, stated precisely) - covering the cubic code's actual behavior as a consistency check.
3. **Nonexistence for (Q-gen)** - same, for all local Hamiltonians; this would be a landmark and is not expected.

**Not accepted as resolution:**

- An energy-barrier growth result alone, even $\Delta(L)=\Omega(L)$: the welded code (Michnicki 2014) shows polynomial barriers coexist with poor memory time via entropic effects. Barrier results are P-targets.
- Memory times that grow with $L$ only for $L\le L^*(\beta)$ (the cubic-code profile, Bravyi–Haah): "partial self-correction" is a partial result by definition.
- Numerical simulation of decay times (Monte Carlo of the Davies or kinetic dynamics) without proof.
- Self-correction under symmetry-restricted noise (e.g. Roberts–Bartlett-type symmetry-protected results) or with engineered dissipation/active feedback - different problem.
- No-go theorems for subclasses narrower than (Q-stab) - e.g. only scale-invariant codes (Yoshida's class) or only $k=O(1)$ - unless the subclass restriction is proven removable.
- 4D or higher-dimensional constructions, or 3D models with unbounded-strength or unbounded-range terms.

## 3. Graded partial-result targets

Full resolution of (Q-gen) is very unlikely in a session; (Q-stab) no-go is plausible-but-hard. The graded targets are the goal.

- **P1 - Verified reproduction of the cubic-code frontier.**
  Implement Haah's $\mathbb{F}_2[x^{\pm},y^{\pm},z^{\pm}]$-module formalism independently.
  For Haah's code (and 2–3 other cubic codes from his 2011 list): verify commutation, compute $k(L)$ exactly for $L\le 64$ via Smith normal form / Gröbner bases over $\mathbb{F}_2$, verify the no-strings property algorithmically, and reproduce the $\Omega(\log L)$ barrier lower bound as a certified finite statement for a ladder of $L$.
  *Certificate:* exact-arithmetic linear algebra transcripts; for finite-$L$ barrier statements, SAT encodings ("exists a path with max energy $<b$") whose UNSAT results carry DRAT proofs checked by `drat-trim`.
  This is the known frontier under our own verified toolchain.
- **P2 - Certified systematic search over code families.**
  Enumerate translation-invariant 3D CSS codes with small unit cells ($q\le 2$ qubits/site, stencil radius $\le 2$), the commutation condition solved as a syzygy computation over $\mathbb{F}_2[x,y,z]$.
  For each candidate compute, exactly:
  - $k(L)$ growth class (Smith normal form over the group algebra quotient);
  - distance bounds for small $L$ (SAT/ILP, exact);
  - string-operator detection (Haah's algorithm) and topological-order checks;
  - certified finite-$L$ barrier lower bounds (UNSAT certificates as in P1).
  Deliverable: a reproducible atlas with machine-checkable figures of merit - the `[search]` core.
  *Certificate:* per-code artifact bundle; independent re-checker for a random 5% sample.
- **P3 - Barrier upper bounds and entropic analysis for the atlas.**
  For every P2 candidate with promising lower bounds: explicit low-barrier paths (SAT satisfying assignments - self-certifying), and free-energy barrier estimates separating "barrier grows" from "memory survives" (rigorous where possible, labeled heuristic otherwise). Kills false positives cheaply.
- **P4 - Sharpened no-go theorems.** Extend the Bravyi–Terhal / Yoshida / Haah toolkit: e.g. prove an $O(\log L)$ barrier upper bound for a class strictly containing all known fracton codes (all translation-invariant CSS codes with $k(L)$ bounded on a cofinal set of $L$? - formulate and prove), or close the gap in Yoshida's scale-invariance hypothesis.
  *Certificate:* proof, plus machine verification of the combinatorial lemmas on finite instances.
- **P5 - A candidate beating $\log L$.** A translation-invariant 3D stabilizer family with certified barrier $\omega(\log L)$: finite-$L$ UNSAT certificates for a growing ladder plus a proven asymptotic lower bound (induction on structure, as Bravyi–Haah did for $\log L$).
  This would be a headline result even without a memory-time theorem, and must still be reported as partial (see section 2).
- **P6 - Thermal statement for a candidate.**
  For the best available candidate (from P5 or the literature): a rigorous Davies-dynamics result - either an Arrhenius-type upper bound sharpening (extending Bravyi–Haah's analysis) or a lower bound on autocorrelation/memory time via spectral-gap or Poincaré-inequality machinery.
  Strongest realistic step short of resolution.

## 4. Known results and prior art

- Dennis–Kitaev–Landahl–Preskill 2002: 4D toric code as a self-correcting memory (statistical-mechanics argument); Alicki–Horodecki–Horodecki–Horodecki 2010: rigorous 4D thermal stability under Davies dynamics.
- Kitaev 2003: toric code; Alicki–Fannes–Horodecki 2009: the 2D toric code is *not* self-correcting under Davies dynamics.
- Bravyi–Terhal 2009: 2D stabilizer no-go - string-like logical operators force $O(1)$ barriers.
- Haah 2011: cubic codes, the no-strings rule; Haah 2013: commutative-algebra (module) framework for translation-invariant Pauli codes.
- Bravyi–Haah 2011: $\Omega(\log L)$ energy barrier for cubic code 1; Bravyi–Haah 2013: memory time $\tau\sim L^{c\beta}$ for $L\lesssim e^{\beta/3}$, then decreasing - partial self-correction, with the entropic ceiling made quantitative.
- Yoshida 2011: no-go within scale- and translation-invariant 3D stabilizer codes (verify exact hypotheses - the class is narrower than all of (Q-stab)).
- Landon-Cardinal–Poulin 2013: local commuting-projector codes in 2D lack thermal protection beyond stabilizers (marginal-strengthening of 2D no-go).
- Michnicki 2014: welded toric code - polynomial energy barrier, yet memory time bounded in $L$ at fixed $\beta$ (entropy beats energy); the standing counterexample to "barrier $\Rightarrow$ memory".
- Chesi–Röthlisberger–Loss 2010: self-correction with long-range interactions (outside our class); Brown–Loss–Pachos–Self–Wootton 2016 (Rev. Mod. Phys.): the definitive survey of quantum memories at finite temperature.
- Bombín 2015: single-shot error correction in 3D gauge color codes - adjacent but active-correction, not self-correction; Kubica–Vasmer 2022: single-shot 3D toric code (verify) - same caveat.
- Chamon 2005: the first fracton-type model (verify attribution details); Castelnovo–Chamon 2008: thermal fragility of topological order at $T>0$ (verify) - conceptual backdrop for why 3D is hard.
- Fracton reviews: Nandkishore–Hermele 2019; Pretko–Chen–You 2020 - taxonomy of the search space.
- Terhal 2015 (Rev. Mod. Phys.): quantum error correction for quantum memories - standard reference for the decoder/memory-time definitions adopted here.
- Post-2023 activity on Lindbladian/dissipative stabilization and measurement-based memories exists but changes the problem statement; check whether any 2024–2026 work claims a passive 3D result (none known to us as of this revision - verify).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

`[search]` mode; all core computations fit a single workstation.

1. **Module toolchain.** SageMath or Macaulay2 for $\mathbb{F}_2[x^{\pm},y^{\pm},z^{\pm}]$ syzygies and Gröbner bases; custom exact Smith-normal-form code (C++ with bitset rows, or FLINT nmod matrices) for $k(L)$ on $\Lambda_L$, $L\le 64$ (matrix dimensions $\sim 10^6$ over $\mathbb{F}_2$ - minutes with bit-packed elimination).
   Cross-check $k(L)$ against Haah's published values.
- **Failure mode:** Laurent-ring vs. quotient-ring subtleties at finite $L$ (periodic boundary resonances make $k(L)$ oscillate in $L$); always report $k(L)$ as a function, never a single number.
2. **Barrier certificates via SAT.** Encode "there is a Pauli path implementing logical $\ell$ with all intermediate energies $<b$" as SAT (path length polynomially bounded via a proven normal form - establish the bound first, it is a lemma, not an assumption).
   Kissat/CaDiCaL with DRAT output; `drat-trim` as independent checker.
   Feasible for $L\le 8$–$12$ and small $b$; that suffices for ladder evidence, with asymptotics done by proof (P4/P5).
- **Failure mode:** unproven path-length normal form silently weakens the UNSAT claim to "no short path" - state the normal-form lemma explicitly or downgrade the claim.
3. **Search loop.** Random + structured enumeration of stencil pairs satisfying the CSS syzygy condition; filter: nontrivial $k(L)$ growth, no string operators, distance growth; promote survivors to SAT barrier ladders.
   Log every candidate (including failures) to the atlas.
- **Failure mode:** figure-of-merit gaming - codes optimizing finite-$L$ barrier ladders while asymptotically string-degenerate; require the no-strings check and structural proofs before promotion.
4. **Thermal analysis (P6).** Davies-generator spectral computations by sparse exact diagonalization for toy sizes ($\le 4^3$ sites) as ground truth; rigorous bounds via canonical-paths/Poincaré methods on the classical energy landscape.
- **Failure mode:** conflating the classical kinetic (Metropolis) landscape with the quantum Davies generator - the reduction must be stated as a theorem or the result labeled model-dependent.
5. **Lean 4 (optional, timeboxed):** formalize the Bravyi–Terhal 2D no-go core lemma (string cleaning) - a self-contained combinatorial statement.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All code parameters ($k(L)$, distances, commutation, syzygies) in exact $\mathbb{F}_2$/integer arithmetic; energies are integers, so barrier statements are exact combinatorics; no floating point anywhere in a certified claim (Davies spectral toys excepted, and labeled exploratory).
2. **Independent verification.** DRAT proofs checked by `drat-trim` (independent of the SAT solver); $k(L)$ recomputed by two implementations (Sage/M2 and custom C++); a standalone Python checker re-verifies stabilizer commutation and no-strings for every atlas entry.
3. **Reproducibility.** Every atlas entry: stencil polynomials (exact), $L$-ladder, solver versions, seeds for randomized search, SHA-256 manifest over stencils, CNF files, DRAT proofs, and result tables.
4. **Preservation.** The full search log - including rejected candidates and the rejection reason - is part of the record; a "we searched $N$ families" claim without the log is not accepted internally.
5. **Honest reporting.** The final report states up front that the existence question (Q-stab)/(Q-gen) remains open unless section-2 standards were met; barrier results are always reported with the Michnicki caveat attached; finite-$L$ certificates are never described as asymptotic theorems.
