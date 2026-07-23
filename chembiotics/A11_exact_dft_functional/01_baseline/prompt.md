# PROMPT FOR THE EXACT EXCHANGE–CORRELATION FUNCTIONAL OF DENSITY FUNCTIONAL THEORY

## Constraint-satisfying learned functionals toward the exact $E_{xc}[\rho]$, with graded targets as the product

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A-11 of 21
**Source:** chem/bio top-50 list #1, section A (electronic structure)
**Modes:** `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Density functional theory reduces the many-electron problem to a functional of the electron density. Hohenberg–Kohn guarantees an exact universal exchange–correlation functional $E_{xc}[\rho]$ exists; its form is unknown, and every practical DFT calculation uses an approximation. This is the single highest-leverage target in computational chemistry - the exact functional would upgrade essentially every downstream calculation at Kohn–Sham cost. It is also very hard, and **this prompt states plainly up front: a fully exact, universal functional is not a realistic single-session outcome.** The realistic and valuable products are the graded targets: functionals that provably satisfy the known exact constraints, that improve on a held-out reaction class under an honest benchmark-integrity guard, or that form a systematically convergent hierarchy. DM21 (Kirkpatrick, Cohen and co-workers at DeepMind, 2021) showed the template - a neural functional trained partly on fractional-charge and fractional-spin constraints beat hand-built functionals on hard cases. The **on-machine verifier** is exact/near-exact reference data the session computes itself: full-CI densities and energies for small systems, quantum Monte Carlo for larger ones, and the *exact mathematical constraints* $E_{xc}$ must obey (Lieb–Oxford bound, uniform coordinate scaling, the derivative discontinuity, size-consistency), which are checkable directly. Anything short of the section-2 standard is reported as a partial result, never as a solution.

## 1. Exact problem statement

**The object.** In Kohn–Sham DFT the total energy is

\[
E[\rho] = T_s[\rho] + \int v_{\text{ext}}(\mathbf r)\rho(\mathbf r)\,d\mathbf r + J[\rho] + E_{xc}[\rho],
\]

with $T_s$ the non-interacting kinetic energy, $J$ the Hartree energy, and $E_{xc}[\rho]$ the exchange–correlation functional - the only unknown. The exact $E_{xc}$ is universal (independent of $v_{\text{ext}}$) and, evaluated at the true ground-state density, makes $E[\rho]$ equal the exact ground-state energy for every system.

**Reference method (ground truth).** For small systems the reference is **full configuration interaction (FCI)** total energies and densities in a converged basis (approaching CBS), giving exact $E_0$ and $\rho_0$; for larger systems, **diffusion / auxiliary-field quantum Monte Carlo** total energies with quantified statistical + systematic (fixed-node / constrained-path) error. Exact Kohn–Sham potentials/densities for benchmark systems (from inversion of accurate densities) provide the exact $E_{xc}$ behavior to match locally.

**Exact constraints (checkable directly).** The admissible functional must respect the known exact conditions, among them:
- **Lieb–Oxford bound:** $E_{xc}[\rho] \ge -C_{\text{LO}}\int \rho^{4/3}\,d\mathbf r$ with the best proven constant.
- **Uniform coordinate scaling:** the exact scaling relations for $E_x$ (homogeneity degree 1 under $\rho_\lambda(\mathbf r)=\lambda^3\rho(\lambda\mathbf r)$) and the correlation scaling inequalities.
- **Derivative discontinuity / piecewise-linearity:** the exact energy is piecewise linear in fractional electron number $N$; the functional must reproduce this (delocalization-error-free).
- **Constancy of $E_{xc}$ under fractional spin** for degenerate ground states (static-correlation error-free).
- **Size-consistency / size-extensivity**, correct uniform-electron-gas limit, spin-scaling, and the Lieb–Oxford tightening at low density.

**Admissible class.** A functional of the density and its semilocal ingredients (LDA/GGA/meta-GGA ingredients: $\rho$, $\nabla\rho$, $\tau$, $\nabla^2\rho$) and optionally exact-exchange / nonlocal ingredients, expressed analytically or as a neural network, evaluated self-consistently in Kohn–Sham. The rung (Jacob's ladder level) and the ingredient set are declared.

**Accuracy threshold (numeric).** For energetics, the target is **$1\,\mathrm{kcal/mol}$ ($\approx 1.6\,\mathrm{mHartree}$)** MAE on relative energies (atomization, reaction, barrier) vs the exact/near-exact reference on a held-out set, *and* satisfaction of every declared exact constraint to a stated numeric tolerance. "Chemical accuracy" appears only as this number plus the constraint tolerances.

## 2. Resolution standard

**Full resolution (not a realistic session outcome, stated for completeness):** a single universal functional that, evaluated self-consistently, reproduces exact energies within $1\,\mathrm{kcal/mol}$ for *arbitrary* systems (weak and strong correlation, metals and molecules, all fillings) while provably satisfying all known exact constraints. This is not expected; graded targets are the product.

**Deliverable for the graded targets:** a functional (weights/parameters + evaluation code), the reference data the session computed, machine-checkable proofs/tests of constraint satisfaction, and a held-out benchmark with an honest integrity guard.

**Not accepted as resolution:**
- A functional with low MAE on a benchmark set but that *violates* a known exact constraint (e.g. the Lieb–Oxford bound, or piecewise-linearity) - benchmark accuracy does not substitute for the exact conditions.
- Improvement on the *training* reaction classes only, without a held-out class.
- A functional tuned to reproduce a *higher approximate* method (e.g. a hybrid or CCSD(T)) rather than the exact reference, presented as "toward exact".
- Good total energies from cancellation of exchange and correlation errors that break under fractional charge/spin (delocalization or static-correlation error hidden by the test set).
- A single-system or single-reaction-class success presented as a universal functional.

**Benchmark-integrity clause.** The verifier combines *exact references* (clean) with *benchmark reaction sets* (biased). Named biases: (i) *Training-set thermochemistry bias* - public DFT benchmarks (e.g. GMTKN55) overlap the data functionals are trained on; a win there can be memorization. Guard: a prospective held-out reaction class, whose reference energies are computed by the session after the functional is frozen, drawn from a chemistry deliberately outside training (e.g. if trained on main-group thermochemistry, tested on a transition-metal reaction or a noncovalent set). (ii) *Constraint-vs-accuracy tension* - a functional can be pushed to a benchmark at the cost of a subtle constraint violation. Guard: constraint satisfaction is tested independently and reported alongside every accuracy number; a benchmark win with a constraint violation is flagged as confident-but-wrong. (iii) *Reference error* - FCI/QMC references have their own (small, quantified) error, which must be smaller than the claimed accuracy.

## 3. Graded partial-result targets

**P1 - Reproduce DM21-style constrained training on a verified small-system corpus.** Rebuild a neural functional trained on fractional-charge/fractional-spin systems plus a small molecular set, using an *own-computed* FCI reference corpus, and reproduce the qualitative DM21 result: reduced delocalization and static-correlation error vs a standard hybrid on the same hard cases. *Certificate:* the FCI corpus (verified), the trained functional, and error comparisons on the hard cases; self-consistent evaluation, not post-hoc on fixed densities only.

**P2 - Certified satisfaction of exact constraints.** For a functional (new or existing), *prove/test* satisfaction of a named set of exact constraints to a numeric tolerance: the Lieb–Oxford bound (checked as an inequality over a broad density sample and, where the form allows, symbolically), uniform scaling relations (symbolic where analytic), piecewise-linearity in $N$ (computed on fractional-charge systems), fractional-spin constancy. *Certificate:* per-constraint tests with tolerances; symbolic proofs where the functional form permits (exact-exchange scaling, LO for a bounded enhancement factor).

**P3 - Improved functional on a held-out reaction class with an honest guard.** Produce a functional that beats a strong baseline (e.g. a well-regarded meta-GGA or hybrid) on a *prospective* held-out reaction class, with constraint satisfaction maintained. *Certificate:* frozen-functional hash predating the held-out reference computation; error distribution vs baseline; constraint report.

**P4 - Systematically convergent hierarchy.** Construct a family (a ladder rung sequence, or a controlled-order expansion) with a demonstrated monotone error decrease toward the exact reference as the level increases, on a held-out set - i.e. a functional with a *convergence handle*, not a one-off fit. *Certificate:* the family, the monotone held-out error curve, and the convergence rationale.

**P5 - Exact-behavior functional for a restricted domain.** For a narrow but exactly solvable domain (e.g. one/two-electron systems, or a model Hamiltonian where the exact $E_{xc}$ is known by inversion), produce a functional that is exact-to-tolerance on that domain and analyze what it reveals about the general form. *Certificate:* near-exact match on the domain against inverted-density references.

## 4. Known results and prior art

- Hohenberg & Kohn (1964); Kohn & Sham (1965) - existence of the universal functional and the KS scheme.
- Levy (1979); Lieb (1983) - constrained-search formulation and rigorous functional foundations; Lieb & Oxford (1981) - the Lieb–Oxford bound.
- Perdew, Burke, Ernzerhof (1996) - PBE (constraint-based GGA). Tao, Perdew, Staroverov, Scuseria (2003) - TPSS meta-GGA. Sun, Ruzsinszky, Perdew (2015) - SCAN (satisfies 17 known constraints). Becke; Lee–Yang–Parr; the B3LYP hybrid.
- Perdew, Parr, Levy, Balduz (1982) - piecewise-linearity and the derivative discontinuity; Cohen, Mori-Sánchez, Yang (2008–2012) - delocalization and static-correlation errors; fractional charge/spin analysis.
- Kirkpatrick, McMorrow, Turban, Gaunt, Spencer, Cohen et al. (DeepMind, 2021) - DM21: a neural functional trained with fractional-charge/spin constraints, published in *Science*.
- Nagai, Akashi, Sugino (2020) - machine-learned functionals from small datasets; Dick & Fernandez-Serra (2020–2021) - NeuralXC; Bogojeski, Vogt-Maranto, Tuckerman, Müller (2020) - ML corrections to DFT toward CCSD(T).
- Exact-density / inversion references: Wagner, Baker, Burke and co-workers on exact KS potentials and the exact functional for model systems (verify).

*Status as of mid-2026 - re-verify against current literature before starting any session.*

## 5. Attack plan

**Reference/verifier layer.** Compute the exact corpus with **PySCF** FCI for small atoms/molecules (energies and densities), fractional-charge and fractional-spin systems (ensemble densities), and - where needed - DMC/AFQMC (e.g. **QMCPACK**) for larger references with quantified stochastic + systematic error. Generate exact KS potentials by density inversion for benchmark densities. A single workstation covers FCI up to $\sim 12$–$16$ orbitals and the full fractional-charge/spin small-system corpus; QMC references are the expensive extension.

**Functional/model layer `[func]`.** Implement the functional as a neural enhancement factor over declared ingredients (LDA/GGA/meta-GGA, optionally exact exchange) in **PyTorch**, coupled to PySCF for self-consistent Kohn–Sham evaluation (differentiable through the SCF where feasible, or via the DM21-style local-energy training). Enforce constraints two ways: (i) *by construction* - bound the enhancement factor to respect Lieb–Oxford and the correct limits; (ii) *by training* - include fractional-charge/spin data so piecewise-linearity and fractional-spin constancy are learned.

**Constraint-certification layer `[func]`/`[sym]`.** Test each exact constraint numerically over a broad density sample; where the enhancement factor is analytic, prove Lieb–Oxford and scaling *symbolically* (SymPy) over the ingredient domain. Compute piecewise-linearity error on fractional-$N$ systems directly.

**Held-out evaluation.** Freeze the functional (hash), then compute the prospective held-out reaction-class references and evaluate self-consistently. Report error distribution and the constraint report together.

**Expected failure modes.** (i) Great post-hoc energies on fixed exact densities but poor *self-consistent* behavior - always evaluate self-consistently. (ii) Benchmark win hiding a constraint violation - test constraints independently. (iii) Error cancellation masking delocalization/static-correlation error - the fractional-charge/spin tests expose it. (iv) Overfitting to the small FCI corpus; the held-out class controls it. (v) QMC systematic error mistaken for functional error - quantify the reference error first.

## 6. Verification and auditability requirements

1. **Exact or certified numerics.** Energetic claims are held-out MAEs vs FCI/QMC references whose own error is quantified and smaller than the claim; constraint satisfaction is a set of explicit numeric tests (and symbolic proofs where the form allows), reported to stated tolerances. Self-consistent evaluation is mandatory; fixed-density post-hoc numbers are labeled as such.
2. **Independent verification.** A standalone checker - separate from training - evaluates the frozen functional self-consistently in PySCF, recomputes held-out errors, and re-runs every constraint test; a subset of FCI references is recomputed with a second code, and QMC references cross-checked between methods.
3. **Reproducibility.** The reference corpus and its error bars, ingredient set/rung, training data and splits, the prospective held-out class (frozen before evaluation), seeds, hyperparameters, functional version/hash, and SCF thresholds are recorded; SHA-256 manifest over all artifacts; frozen-functional hash timestamped before held-out references.
4. **Preservation.** Training code, functional weights, reference-generation inputs, and constraint-test scripts are part of the record. Anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front - and prominently - that the full exact universal functional was *not* achieved (graded targets are the deliverable), reports the prospective held-out error and the full constraint report side by side, flags any benchmark win that coexists with a constraint violation, and never presents a training-set or single-domain result as the exact functional.
