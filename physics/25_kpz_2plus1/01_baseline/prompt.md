# PROMPT FOR EXACT STRUCTURE IN THE 2+1-DIMENSIONAL KPZ UNIVERSALITY CLASS

## Strong-coupling exponents of isotropic KPZ growth in two spatial dimensions: certified numerics, solvable-structure obstructions, and the hunt for a first rigorous inequality

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 25 of 50 (Tier 2)
**Source:** top-50 list #32, category D (nonequilibrium and stochastic)
**Modes:** `[sym]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

In 1+1 dimensions the KPZ class is exactly characterized: Tracy–Widom statistics (Baik–Deift–Johansson 1999; Johansson 2000), the KPZ fixed point (Matetski–Quastel–Remenik), the directed landscape (Dauvergne–Ortmann–Virág). In 2+1 dimensions - the physically dominant case for real film growth - nothing exact is known: the strong-coupling exponents are purely numerical ($\beta\approx0.2415$, $\alpha\approx0.39$ - verify current values and the unresolved spread between high-precision groups), no limiting distributions are analytically characterized, no solvable isotropic model exists, and not one nontrivial rigorous exponent inequality has been proven for a genuine 2+1 KPZ-class model.

This prompt is honest about scope: full resolution - the exact 2+1 fixed point - is beyond visible technology. The goal is exponent-structure mining with certified deliverables: reproducible high-precision exponent data under a disciplined statistical protocol; machine-checked obstruction theorems showing that candidate solvable structures in 2+1 collapse into the anisotropic (AKPZ / Edwards–Wilkinson) class; rigorous inequalities ported from first/last-passage percolation technology; and certified analysis of hierarchical analogs.

The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 The class, defined via models

- The KPZ equation $\partial_th=\nu\nabla^2h+\frac\lambda2|\nabla h|^2+\sqrt D\,\xi$ with space-time white noise $\xi$ in two spatial dimensions is scaling-critical for its noise and does not by itself define the strong-coupling class: the rigorous weak-coupling theory - Edwards–Wilkinson limits and the critical 2D stochastic heat flow (Caravenna–Sun–Zygouras 2017–2023) - describes a different regime by construction.
- The class studied here is therefore defined through discrete models, whose update rules are fixed as follows:
  1. RSOS deposition (Kim–Kosterlitz 1989) on $\mathbb Z^2$: integer heights with $|h(x)-h(y)|\le1$ for all nearest neighbors; pick a random site, deposit $h\to h+1$ if all constraints remain satisfied, else reject;
  2. the single-step / body-centered SOS model: checkerboard heights with $|h(x)-h(y)|=1$ across neighbors; deposition/evaporation rates $p,q$ with $p\ne q$ for KPZ nonlinearity;
  3. ballistic deposition: $h(x)\to\max\{h(x)+1,\max_{y\sim x}h(y)\}$ at a random site;
  4. directed polymers / zero-temperature last-passage percolation with paths in 2+1 dimensions (i.i.d. weights; law fixed per study, e.g. exponential).
- For a model on an $L\times L$ torus started flat, the interface width is
\[
W^2(L,t)=\frac1{L^2}\sum_x\big(h(x,t)-\bar h(t)\big)^2,
\]
with Family–Vicsek scaling: $W\sim t^\beta$ for $1\ll t\ll L^z$, saturation $W\sim L^\alpha$, $z=\alpha/\beta$.
- The relation $\alpha+z=2$ follows from Galilean/tilt symmetry heuristics; it is nonrigorous for any given discrete model and is a hypothesis to be tested, never assumed in a proof.
- **Isotropy requirement:** the nonlinearity's quadratic form must be definite. If $\lambda_x\lambda_y<0$ the model is anisotropic KPZ (AKPZ), which flows to logarithmic roughness (Wolf 1991) - realized rigorously in the solvable model of Borodin–Ferrari 2008 and in lozenge-dynamics results of Toninelli and coauthors (verify) - and is *not* the target class.

### 1.2 Proxy exponent conventions ($\chi$, $\xi$)

For the polymer/passage-time proxies used in P4, fix the standard conventions:
- $\chi$ = fluctuation exponent of the passage time / free energy: $\mathrm{Var}\,T(0,ne_1)\asymp n^{2\chi}$;
- $\xi$ = transversal wandering exponent: geodesics/polymers of length $n$ wander $\asymp n^{\xi}$;
- the growth-model dictionary is $\beta=\chi/z_{\mathrm{time}}$-type only after an explicit model-specific identification - state it, never assume it;
- the KPZ scaling relation $\chi=2\xi-1$ is proven for FPP under hypotheses (Chatterjee 2013); its applicability to any chosen 2+1 model must be argued, not cited.

### 1.3 Open problems, graded

1. **(Q1)** Exact values, or any rigorous nontrivial bounds, for $\alpha,\beta,z$ of isotropic 2+1 KPZ. Reference numerics: $\beta=0.2415(15)$ (Kelling–Ódor 2011, GPU); $\alpha=0.393(4)$ (Halpin-Healy 2012); but also $\alpha=0.3869(4)$ (Pagnani–Parisi 2015) - verify all three and note the unresolved tension. The Kim–Kosterlitz rational guess $\alpha=2/5$, $z=8/5$, $\beta=1/4$ is reported excluded by parts of this literature (verify).
2. **(Q2)** Existence of any exactly solvable isotropic 2+1 growth model - tetrahedron-equation or determinantal structure - or obstruction theorems explaining its absence.
3. **(Q3)** Analytic characterization of the 2+1 height-fluctuation distributions (numerically universal: Halpin-Healy 2012–2013; Oliveira–Alves–Ferreira 2013 - verify; no analytic form is known even conjecturally).

Any rigorous nontrivial exponent inequality for a concrete isotropic 2+1 model - e.g. a quantitative lower bound establishing growth of fluctuations in the $\beta$ sense, or a sub-diffusive upper bound strictly better than trivial - would be a notable first.

## 2. Complete-resolution standard

Complete resolution means: exact strong-coupling exponents for a concrete isotropic 2+1 model with proofs; or the construction and rigorous analysis of a solvable isotropic 2+1 model determining the class exponents; or a proven fixed-point characterization. This is stated for completeness; it is not the expected outcome, and the report must not shade partial progress toward it.

**Not accepted as resolution:**

- Numerical exponents at any precision, including new in-session values with tight error bars.
- Weak-coupling rigorous results (Edwards–Wilkinson limits in $d\ge2$; the critical 2D stochastic heat flow) presented as strong-coupling statements.
- AKPZ / anisotropic solvable results (Borodin–Ferrari lineage) presented as isotropic 2+1 KPZ results.
- Hierarchical-lattice or mean-field exponents presented as $\mathbb Z^2$-model exponents; they are labeled analogs (target P5).
- Scaling relations ($\alpha+z=2$; Krug–Meakin identities) assumed without proof inside any claimed theorem about a specific model.
- Uncontrolled field-theory outputs - mode-coupling, NPRG (e.g. Canet–Chaté–Delamotte–Wschebor ~2010–2011, verify) - presented as exact; they are prior-art heuristics.
- An "obstruction theorem" whose model family was gerrymandered after the search; the family must be declared and frozen before searching (see P3).

## 3. Graded partial-result targets

**P1 - certified data generation with our own toolchain.**
Simulate at least three distinct isotropic models (RSOS, single-step, ballistic deposition) on $L\le8192$ tori under a documented statistical protocol: counter-based RNG with logged seeds; batch-means error bars; finite-time and finite-size crossover analysis; effective-exponent flows rather than single fits. Deliver $\beta$ and $\alpha$ estimates with defensible uncertainties reproducing the literature band, plus raw data. Floating-point exploration by definition: labeled ground-truth *data*, never certification.
*Certificate:* seeds, code, raw traces, protocol document, SHA-256 manifest.

**P2 - exponent-candidate audit.**
Assemble every closed-form candidate in the literature - Kim–Kosterlitz $(2/5,8/5,1/4)$; Lässig's rational proposals (verify statements); anything newer found in the 2020s literature - and test each against P1 data and published high-precision values, with explicit statistical exclusion levels. Deliverable: a candidate-status table with sources. Do **not** run integer-relation searches on 3–4 significant digits; state plainly that PSLQ is meaningless at that precision.
*Certificate:* the table, its data lineage, and the exclusion computations.

**P3 - solvable-structure obstruction, machine-checked.**
Declare (and freeze, with hash and date) a finite family of local stochastic update rules in 2+1: stencil size, height-difference constraints, rate parametrization. Search symbolically for exact structure: Markov dualities ($HD=DH^{T}$ over small local spaces - finite exact linear algebra); determinantal/free-fermion signatures; tetrahedron-equation compatibility (Zamolodchikov 1980; Bazhanov–Baxter 1992; Bazhanov–Sergeev ~2005–2006 - verify relevance). Expected outcome, provable as a theorem about the declared family: every member with exact structure has AKPZ/EW signature ($\lambda_x\lambda_y\le0$ or vanishing nonlinearity) - no solvable isotropic member exists in the family.
*Certificate:* the frozen family definition; exact linear-algebra certificates (SymPy/SageMath); independent nullspace re-verification.

**P4 - rigorous inequalities on concrete 2+1 models.**
Port FPP/LPP fluctuation technology to a declared 2+1 model (exponential LPP with paths in $\mathbb Z^2\times\mathbb Z$, or 3D FPP as proxy). Reproduce with complete proofs, in order:
- the analog of Kesten's $\chi\le1/2$ (1993);
- Benjamini–Kalai–Schramm sublinear variance (2003);
- Licea–Newman–Piza transversal-exponent bounds ($\xi\ge1/(d+1)$ lineage, 1995–1996);
- Chatterjee's scaling relation $\chi=2\xi-1$ under stated hypotheses (2013).
Then push for any strict improvement in the 2+1 setting. A clean, complete port with explicit constants is already a useful artifact; a strict improvement is publishable.
*Certificate:* full proof text; any computer-assisted steps in exact arithmetic.

**P5 - hierarchical analogs, certified.**
Directed polymers on hierarchical lattices (Derrida–Griffiths 1989; Cook–Derrida 1989): compute the analog exponents by certified interval iteration of the exact RG recursion (Arb, directed rounding), with rigorous convergence statements for the hierarchical model itself. Labeled analog: no claim of transfer to $\mathbb Z^2$.
*Certificate:* interval-arithmetic proofs; independent reimplementation (mpmath).

**P6 - strongest short of resolution.**
One of: a rigorous nontrivial exponent inequality for a genuine isotropic 2+1 model beyond the P4 ports (e.g. strict positivity of a fluctuation exponent with a quantitative bound, or any bound separating 2+1 from both EW and 1+1 values); an extension of the P3 obstruction to a natural infinite family; or a rigorous unconditional consequence of tilt symmetry for one concrete model - a proof of $\alpha+z=2$ for any single 2+1 model would itself be notable (verify whether any such proof exists).

Honest calibration: this problem is exponent-structure mining. Q1–Q3 in full are far out of reach; the expected genuine products are P1–P3, with P4 the serious mathematical target.

## 4. Known results and prior art

- 1+1 rigorous canon (contrast and toolbox): Baik–Deift–Johansson 1999; Johansson 2000; Amir–Corwin–Quastel 2011; Matetski–Quastel–Remenik ~2016–2021 (KPZ fixed point); Dauvergne–Ortmann–Virág ~2018–2022 (directed landscape).
- Weak-coupling rigorous results, $d=2$: Caravenna–Sun–Zygouras 2017–2020 (Edwards–Wilkinson regime in the subcritical window); Caravenna–Sun–Zygouras ~2023 (critical 2D stochastic heat flow); related work by Gu, Chatterjee–Dunlap, Dunlap–Gu–Ryzhik–Zeitouni (verify).
- $d\ge3$ weak disorder: Gaussian limits (Magnen–Unterberger ~2018; the Comets school). Strong disorder at all temperatures for $d=2$ polymers: Lacoin 2010 (verify statement). None of these touch strong-coupling exponents.
- Anisotropic 2+1, rigorous and solvable: Borodin–Ferrari 2008 (determinantal 2+1 growth; GFF/logarithmic fluctuations); Wolf 1991 (AKPZ RG prediction); Toninelli and coauthors on AKPZ interface dynamics ~2015–2019 (verify). These delimit Q2: all known 2+1 solvable structures are anisotropic.
- Numerics: Kelling–Ódor 2011 ($\beta=0.2415(15)$); Halpin-Healy 2012–2013 (exponents; universal distributions); Oliveira–Alves–Ferreira 2013 (distributions); Pagnani–Parisi 2015 ($\alpha=0.3869(4)$); later GPU studies by Kelling–Ódor and others ~2016–2020 (verify current best values and whether the $\alpha$ discrepancy is resolved).
- Field-theoretic estimates: Lässig ~1998 (operator-product rational-exponent proposal - verify); mode-coupling; NPRG: Canet–Chaté–Delamotte–Wschebor ~2010–2011 (verify values). All nonrigorous.
- FPP/LPP rigorous toolbox: Kesten 1993; Licea–Newman–Piza 1995–1996; Newman–Piza 1995; Benjamini–Kalai–Schramm 2003; Chatterjee 2013 (scaling relation); Auffinger–Damron–Hanson survey ~2017.
- Hierarchical lattices: Derrida–Griffiths 1989; Cook–Derrida 1989.
- Tetrahedron equation: Zamolodchikov 1980; Bazhanov–Baxter 1992; Bazhanov–Sergeev ~2005–2006. No stochastic isotropic-KPZ-relevant solution known (verify - a 2020s discovery here would change this prompt's premises).
- Reviews: Halpin-Healy–Takeuchi ~2015 (KPZ universality review); Takeuchi ~2018 (survey of KPZ developments) - both cover the 2+1 numerical landscape (verify).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

### 5.1 `[sym]` Simulation layer (exploration)

- C++ with OpenMP (optionally CUDA) for RSOS/single-step on $L\le8192$; Philox counter-based RNG; measure $W^2(L,t)$, height-distribution cumulants, and tilt response.
- Isotropy check per model before any class claim: verify $\lambda_x\lambda_y>0$ numerically via tilt response; test invariance under 90° rotation.
- For Q3: accumulate height-fluctuation histograms in the growth regime and at saturation; report skewness and kurtosis flows with batch-means errors - the numerically universal 2+1 values are reference points (Halpin-Healy 2012 - verify) and remain unexplained analytically.
- Expected failure modes: crossover contamination of $\beta$ (mandate effective-exponent extrapolation with stated windows); anisotropy accidentally introduced by lattice or update order; RNG artifacts (dual RNG families, compared).

### 5.2 `[sym]` Structure search

- SymPy/SageMath exact linear algebra for duality and free-fermion conditions on the declared rule families; local state spaces of at most a few hundred dimensions - trivial as linear algebra, combinatorially heavy as a sweep; prune by symmetry.
- Every nullspace claim re-verified by evaluation at random rationals in a second system.
- Deliverable shape: exhaustive sweep table over the frozen family; the obstruction theorem of P3 falls out if the table is total.

### 5.3 `[proof]` Inequality layer

- Write out the P4 ports completely; the known proofs are dimension-generic to varying degrees - BKS variance bounds port cleanly; curvature-dependent steps do not. The expected failure point is exactly there; document it precisely.
- Fix the target model in advance (exponential LPP in 2+1) to prevent theorem-shopping.
- Proof artifacts are prose plus, where a lemma reduces to finite computation, an exact-arithmetic script whose output the lemma cites; each such lemma lists its script and hash.
- Cross-check every ported statement against its 1+1 specialization, where exact answers exist, before claiming the 2+1 version.

### 5.4 `[sym]` Hierarchical layer

- Arb interval iteration of the Derrida–Griffiths recursion with directed rounding; certify fixed-point locations and exponents for the hierarchical model; independent mpmath reimplementation.

### 5.5 Resource budget

- Everything fits a single workstation except long P1 runs (weeks of CPU/GPU, embarrassingly parallel; checkpoint and log continuously).

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All P3 structure certificates and P5 interval results in exact or ball arithmetic with directed rounding. P1/P2 are explicitly statistical and carry error protocols instead; the report must keep the two ledgers separate and labeled.
2. **Independent verification.** Dual implementations for simulations (two codes or two RNG families with statistical agreement tests); two CAS routes for every nullspace certificate; Arb plus mpmath for interval iterations; an independent checker script per certificate type.
3. **Reproducibility.** Seeds, lattice sizes, update rules, and the frozen rule-family declarations (with hash and date) recorded; tool versions pinned; SHA-256 manifest over raw data, certificates, and source.
4. **Preservation.** Simulation code, the declared rule families including every member that showed no structure, and failed inequality ports with the exact breaking step documented - all part of the record; unpreserved explorations must be declared.
5. **Honest reporting.** The final report opens by stating that no exact 2+1 result was obtained (unless the section-2 standard was actually met); every exponent value is tagged rigorous / analog / numerical; AKPZ, weak-coupling, and hierarchical results are never blended into isotropic strong-coupling claims; and the candidate-status table distinguishes statistical exclusion from disproof.
