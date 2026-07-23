# PROMPT FOR DERIVED CLOSED-FORM REACTIVITY LAWS

## Symbolic barrier/rate laws for reaction families, derived from computed transition states rather than fitted - Bell–Evans–Polanyi and linear-free-energy relations as discovered forms

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** A - closed-loop (on-machine verifier)
**Rank:** A04 of 21
**Source:** chem/bio top-50 list #49, section G (higher-order structure)
**Modes:** `[sym]` `[func]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Across a reaction family, activation barriers correlate with simple descriptors - the Bell–Evans–Polanyi (BEP) linear relation $E_a = \alpha\,\Delta H_{\text{rxn}} + \beta$, Hammett and Brønsted linear-free-energy relations, and Marcus theory's quadratic form. These are among the most useful compact laws in chemistry, but they are usually *fitted* to a chosen dataset. This prompt asks for such a law to be *derived* - recovered by symbolic regression as a short closed form - and, crucially, tested against ground truth the machine computes for itself. Activation barriers are computable on-machine: an automated transition-state search (autodE driving PySCF/ORCA) locates a first-order saddle, a frequency analysis confirms exactly one imaginary mode, and an intrinsic-reaction-coordinate (IRC) trace confirms the saddle connects the intended minima. That verified barrier is the **on-machine verifier**: symbolic laws are judged against DFT barriers the pipeline itself certifies, on held-out reactions and in extrapolation. The central discipline is distinguishing a genuine closed-form law (short, generalizing, theory-consistent) from an overfit regressor (long, memorizing, fragile). Anything short of the section-2 standard - a fit with no held-out test, or a formula that beats a linear baseline only in-sample - is a partial result, never a law.

## 1. Exact problem statement

**Reaction family $\mathcal{F}$.**

- A set of elementary reactions sharing a mechanistic motif with a varying substituent/substrate - e.g. gas-phase $\mathrm{S_N2}$ ($\mathrm{X^- + CH_3Y \to CH_3X + Y^-}$), E2 eliminations, hydrogen-atom transfers (HAT), or Diels–Alder cycloadditions.
- One family is fixed per study.
- Each reaction $i\in\mathcal{F}$ carries descriptors $\mathbf{x}_i$ - reaction energy $\Delta E_{\text{rxn},i}$, a substituent electronic parameter, a bond-dissociation energy, atomic charges - all computed by a fixed protocol.

**Reference method (the ground-truth generator).**

- A fixed DFT level: functional $+$ basis (state it, e.g. $\omega$B97X-D/def2-TZVP) with a fixed solvation treatment or gas phase - committed up front.
- For each reaction the pipeline locates a saddle; computes the Hessian and confirms **exactly one imaginary frequency** within a stated $|\nu|$ window; runs an **IRC** whose endpoints match the intended reactant and product by connectivity/RMSD tolerance; and reports the electronic activation barrier $\Delta E^{\ddagger}_i$ (and, where free energies are used, $\Delta G^{\ddagger}_i$ with thermal/entropic corrections at fixed $T$).
- A reaction with no verified saddle is excluded and logged, not guessed.

**A law.** A closed-form symbolic expression

\[
f_\theta:\ \mathbf{x}\ \longmapsto\ \widehat{\Delta E^{\ddagger}},
\]

drawn from a fixed operator set ($+,-,\times,\div$, powers, $\exp/\log$) with a bounded complexity (expression length / node count); a rate law follows via Eyring, $k = \tfrac{k_B T}{h}\exp(-\Delta G^{\ddagger}/RT)$. BEP is the length-3 form $\alpha\,\Delta E_{\text{rxn}} + \beta$; Marcus is the quadratic

\[
\Delta G^{\ddagger} \;=\; \frac{\lambda}{4}\Big(1 + \frac{\Delta G^{\circ}}{\lambda}\Big)^{2}.
\]

**Certified fit.**

- A train/test split is committed *before* fitting.
- The law is fitted on train and reported on a *held-out* test set - reactions, and (to prevent scaffold leakage) substrate scaffolds, disjoint from train.
- It is stress-tested by **extrapolation** to descriptor ranges outside train (new substituents / larger substrates), against freshly computed, verified barriers.

**Target.** For a family $\mathcal{F}$, discover a law $f_\theta$ with:

- held-out mean absolute error $\text{MAE}_{\text{hold}} \le T_{\text{hold}}$ (a committed threshold, e.g. $1$–$2\,\text{kcal}\,\text{mol}^{-1}$ relative to the DFT ground truth);
- complexity below a committed bound;
- extrapolation MAE $\le T_{\text{extrap}}$.

The positive control is to recover a known law (BEP linear / Marcus quadratic) with matching slope/curvature.

**Accuracy threshold.** Numeric and held-out: $T_{\text{hold}}$ and $T_{\text{extrap}}$ in $\text{kcal}\,\text{mol}^{-1}$ against verified DFT barriers, plus a complexity ceiling. In-sample fit quality alone is not a target.

## 2. Resolution standard

Full resolution is a discovered closed-form barrier/rate law for a non-trivial reaction family that:

1. meets $T_{\text{hold}}$ on a committed, scaffold-disjoint held-out set;
2. meets $T_{\text{extrap}}$ under genuine extrapolation to freshly computed verified barriers;
3. is below the complexity ceiling and beats - on held-out - a linear baseline, a nearest-neighbour baseline, and a random-feature baseline;
4. is theory-consistent or theory-illuminating (reduces to or refines BEP/Marcus, with interpretable parameters).

Every ground-truth barrier is TS-verified (one imaginary frequency, IRC-confirmed) and reproduced by a standalone recomputation.

**Not accepted as resolution:**

- A fit reported only in-sample, or with a random split that leaks scaffolds between train and test.
- A high-accuracy but high-complexity expression indistinguishable from a black-box regressor (an overfit dressed as a law).
- A law that beats baselines in-sample but not on held-out, or that collapses under extrapolation.
- Barriers taken from an unverified TS (wrong saddle, multiple imaginary modes, IRC not connecting the intended minima) or from a downloaded dataset whose TS verification cannot be reproduced.
- A law for one narrow substituent series generalized to a claim about the whole family.
- A claim of a "law of nature" when the ground truth is a single DFT level (see integrity clause).

**Benchmark-integrity clause.** The verifier is DFT, not nature: barrier errors versus CCSD(T)/experiment run $\sim 1$–$4\,\text{kcal}\,\text{mol}^{-1}$ depending on functional and system, so a discovered law is a law *for this level's barriers*. State the level explicitly and, where feasible, spot-check a handful of barriers against a higher reference (DLPNO-CCSD(T) or experiment) to bound the gap. The core guard against teaching-to-the-test is a trio: (i) a scaffold-disjoint held-out split committed before fitting; (ii) genuine **extrapolation** to descriptor ranges absent from train, evaluated on newly computed verified barriers, not resampled train; (iii) a **complexity/description-length** penalty, so a short generalizing form is preferred to a long memorizing one, with explicit baselines. A symbolic-regression "law" that survives none of these is confident-but-wrong and must be flagged as such.

## 3. Graded partial-result targets

- **P1 (verified pipeline reproduces a known BEP correlation).** For a family with an established BEP relation, compute barriers with the TS-verified pipeline and recover the linear $E_a$–$\Delta E_{\text{rxn}}$ correlation, with slope/intercept matching literature within uncertainty. *Certificate:* per-reaction TS validation logs (one imaginary frequency, IRC endpoints) + the regression + the literature comparison.
- **P2 (build the certified ground-truth dataset).** Produce a family dataset of $N$ reactions, each with a fully verified saddle and IRC and a converged barrier with a stated tolerance - the generator every later target consumes. *Certificate:* per-reaction imaginary-frequency count $=1$, IRC endpoint match, and energy convergence, all reproducible.
- **P3 (discover a symbolic law with held-out validation).** Run PySR / SymbolicRegression.jl on the P2 dataset with a frozen, scaffold-disjoint split committed beforehand; report the Pareto front of accuracy vs complexity, the chosen law, its held-out MAE, and the baseline comparison. *Certificate:* the split hash, the search log, the expression, and the held-out/baseline table.
- **P4 (Marcus-consistent form where curvature is expected).** For a family with expected curvature (electron/proton transfer, wide $\Delta G^{\circ}$ range), recover a quadratic Marcus-consistent law and show it beats the linear BEP on held-out. *Certificate:* the model comparison + held-out errors + the interpretation of $\lambda$.
- **P5 (extrapolation test).** The discovered law predicts barriers for substituents/substrates *outside* the training descriptor range; verify against freshly computed, TS-verified barriers. Meeting $T_{\text{extrap}}$ here is the strongest realistic result - a genuinely predictive law. *Certificate:* the prospective DFT TS computations + the prediction-vs-truth errors.

Full resolution (a P5-surviving, baseline-beating, theory-consistent law for a broad family) is unlikely in one session; P1–P3 are realistic and independently valuable, P4–P5 are the stretch.

## 4. Known results and prior art

- Bell 1936; Evans & Polanyi 1938 - the BEP principle relating activation energy to reaction enthalpy within a series.
- Brønsted & Pedersen 1924 - the catalysis linear-free-energy relation; Hammett 1937 - the $\sigma$/$\rho$ substituent scale.
- Marcus 1956, 1964 - Marcus theory of electron transfer and the quadratic barrier–driving-force relation (Nobel 1992).
- Nørskov, Bligaard and co-workers, ~2004–2011 - computational scaling relations and BEP lines in heterogeneous catalysis; the modern "descriptor + linear relation" paradigm.
- Young, Silcock, Sterling, Duarte 2021 (*Angew. Chem.*) - autodE, automated generation of reaction profiles / transition states with verification.
- Grambow, Pattanaik, Green 2020 (*Scientific Data*) - a dataset of ~12k elementary reactions with DFT transition states and barriers; Zhao & Savoie 2023 - RGD1 reaction dataset (verify size/level); RDB7 (verify).
- Jorner, Brinck and co-workers ~2021 (*Chem. Sci.*) - machine learning meeting mechanistic reactivity modelling (verify).
- Cranmer 2023 - PySR / SymbolicRegression.jl, high-performance symbolic regression.
- Udrescu & Tegmark 2020 (*Science Advances*) - AI-Feynman, symbolic regression rediscovering physical laws (methodological precedent for "discover, don't fit").
- Kozuch & Shaik 2011 - the energetic-span model (context for translating barriers to observable rates).

The individual laws (BEP, Marcus, Hammett) are long established; an *automated derive-and-validate* pipeline that produces new, extrapolating, theory-consistent reactivity laws with certified ground truth is not a settled capability. **Status as of mid-2026 - re-verify against current literature before starting any session.**

## 5. Attack plan

**[func] Ground-truth generation.** autodE orchestrates conformer search, TS location (double-ended / NEB or growing-string seeding, then eigenvector-following), and IRC; PySCF or ORCA is the electronic-structure engine (Psi4 as an alternative); Sella provides robust saddle optimization when autodE's default struggles. Every barrier passes the one-imaginary-frequency and IRC-endpoint tests before entering the dataset; failures are logged and excluded. The fixed DFT level is committed up front; a few barriers are spot-checked at DLPNO-CCSD(T) to bound the functional error.

**[sym] Law discovery.** PySR / SymbolicRegression.jl over the committed operator set and complexity ceiling, on the frozen train split; produce the accuracy-vs-complexity Pareto front and select by held-out performance, not in-sample. Baselines (linear, nearest-neighbour, random-feature ridge) are computed on the identical held-out split. Recovering BEP/Marcus is the positive control that the pipeline can find a known law before any novelty is claimed.

**One-workstation scope.** DFT TS searches for small reactants ($\lesssim 30$ heavy atoms) are feasible on a single multicore workstation (ORCA/PySCF are CPU-parallel; no GPU needed); a family of tens to low hundreds of reactions is a multi-day campaign. Symbolic regression is cheap by comparison. **Failure modes:** TS-search non-convergence or convergence to the wrong saddle (multiple imaginary modes); IRC failing to connect the intended minima; conformational complexity (many reactant/TS conformers) biasing barriers; DFT functional error setting an irreducible noise floor on the ground truth; symbolic-regression instability and overfitting; and descriptor leakage across the split - each guarded by the section-2 trio.

## 6. Verification and auditability requirements

1. **Certified ground truth and held-out numerics.** Every barrier is TS-verified (one imaginary frequency, IRC-confirmed, converged) with a stated tolerance; every reported law accuracy is a held-out (scaffold-disjoint) and extrapolation number, not an in-sample fit; the train/test split is committed and hashed before fitting.
2. **Independent verification.** The TS-verification checker is separate from the search that produced the geometries; headline barriers are recomputed by a standalone run; the symbolic law is re-evaluated on the frozen split by code separate from the regressor.
3. **Reproducibility.** DFT level, autodE/PySCF/ORCA versions, TS/IRC criteria, descriptor definitions, the operator set and complexity ceiling, seeds, and the split are recorded; a SHA-256 manifest covers every geometry, Hessian, IRC, barrier, and expression.
4. **Preservation.** TS-search inputs/outputs (including failed searches and excluded reactions), the symbolic-regression logs and full Pareto front, and the baselines are part of the record; anything discarded is listed as discarded.
5. **Honest reporting.** The report states the DFT level as the ground-truth caveat up front, reports held-out and extrapolation errors alongside baselines (not just in-sample fit), distinguishes a short theory-consistent law from an overfit regressor explicitly, and never presents a fitted correlation as a derived law of nature.
