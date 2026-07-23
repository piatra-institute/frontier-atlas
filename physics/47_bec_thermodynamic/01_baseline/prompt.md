# PROMPT FOR PROVING BOSE–EINSTEIN CONDENSATION IN THE THERMODYNAMIC LIMIT

## Off-diagonal long-range order for interacting bosons at fixed positive density

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 47 of 50 (Tier 4)
**Source:** top-50 list #16, category B (rigorous many-body and condensed matter)
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Bose–Einstein condensation - a macroscopic eigenvalue of the one-particle density matrix - has never been proven for any genuinely interacting continuum Bose gas in the true thermodynamic limit, at any density or temperature, including zero temperature.
What is proven lives elsewhere: the ideal gas; lattice hard-core bosons at half filling via reflection positivity (Dyson–Lieb–Simon 1978; Kennedy–Lieb–Shastry 1988); condensation in Gross–Pitaevskii and mean-field *scaling* limits (Lieb–Seiringer school, with optimal rates by Boccato–Brennecke–Cenatiempo–Schlein); and ground-state energy asymptotics through second (Lee–Huang–Yang) order (Yau–Yin 2009; Fournais–Solovej 2020–2023).
The gap between scaling limits and the thermodynamic limit is the whole problem.
This Tier 4 `[proof]` prompt is calibrated accordingly: full resolution is very unlikely; the graded targets - a precise formalization of the scaling-vs-thermodynamic gap, sharp theorems on where reflection positivity breaks off half filling, certified finite-size reduced-density-matrix ground truth, and conditional BEC theorems under checkable correlation-decay hypotheses - are the goal.
The complete resolution defined in section 2 is the target standard; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

**Continuum model.** $N$ spinless bosons on the torus $\Lambda_L=[0,L]^3$ (periodic boundary conditions),

\[
H_{N,L}\;=\;\sum_{i=1}^{N}-\Delta_{x_i}\;+\;\sum_{1\le i<j\le N} v(x_i-x_j)
\quad\text{on }L^2_{\mathrm{sym}}(\Lambda_L^N),
\]

with pair potential $v\ge0$, radial, of compact support (canonical instances: hard spheres of radius $a$; or $v\in C_c^\infty$, $v\ge0$, $v\not\equiv0$).
Thermodynamic limit: $N,L\to\infty$ with $\rho=N/L^3>0$ fixed.
States: ground state, or Gibbs state at inverse temperature $\beta$ (canonical or grand canonical at fixed density - state which; claims must survive the stated ensemble).

**Order parameter.** One-particle reduced density matrix $\gamma_{N,L}(x,y)=\langle a_y^\dagger a_x\rangle$, normalized $\operatorname{Tr}\gamma_{N,L}=N$. *BEC (adopted definition, Penrose–Onsager 1956):*

\[
n_0\;=\;\liminf_{\substack{N,L\to\infty\\ N/L^3=\rho}}\ \frac{1}{N}\,\big\|\gamma_{N,L}\big\|_{\mathrm{op}}\;>\;0 .
\]

On the torus with translation invariance this equals the fraction of particles in the zero mode, and is equivalent to off-diagonal long-range order:

\[
\gamma_{N,L}(x,y)=\gamma_{N,L}(x-y),
\qquad
\liminf_{\substack{N,L\to\infty}}\ \gamma_{N,L}(z)\Big|_{|z|\to\infty}\;=\;\rho_0\;>\;0
\]

(state and use the ODLRO/operator-norm equivalence precisely, with the order of limits fixed in writing).

**The open problem.** Prove BEC in the above sense for *some* (ideally any) $v$ as above at *some* fixed $(\rho,\beta)$ - including the ground state ($\beta=\infty$) at small $\rho a^3$, universally expected to condense. Open for every interacting continuum model. Adopted primary instance: hard spheres (or fixed smooth $v\ge0$) at small but fixed $\rho a^3$, ground state; positive-temperature claims graded strictly above.

**Scaling dictionary (fix these distinctions in every statement).** The rigorous BEC literature works in scaling regimes obtained by tying the interaction to $N$. On the unit torus, with $\beta_s\in[0,1]$,

\[
H^{(\beta_s)}_{N}\;=\;\sum_{i=1}^{N}-\Delta_{x_i}\;+\;\sum_{i<j} N^{3\beta_s-1}\,v\big(N^{\beta_s}(x_i-x_j)\big)
\quad\text{on }L^2_{\mathrm{sym}}\big(([0,1]^3)^N\big):
\]

$\beta_s=0$ is mean-field; $\beta_s=1$ is Gross–Pitaevskii, where the scattering length scales as $a_N\sim a/N$ and the gas parameter $\rho a_N^3\sim N^{-2}\to0$.
In every such regime the interaction range or strength is sent to a degenerate limit with $N$; the thermodynamic limit - $v$ fixed, $N/L^3=\rho$ fixed, $\rho a^3$ fixed - is precisely the regime these theorems avoid.
No value of $\beta_s$ (nor any "beyond-GP" exponent) reproduces it; conflating the two is the canonical error this prompt forbids.

**Lattice benchmark (for contrast and for P2).** Hard-core bosons on $\mathbb{Z}^3$ ($\equiv$ spin-$\tfrac12$ XY model): BEC/ODLRO is *proven* at half filling - ground state (Kennedy–Lieb–Shastry 1988) and $T>0$ (Dyson–Lieb–Simon 1978 framework via reflection positivity + infrared bounds; verify attribution details). Off half filling (fixed density $\neq\tfrac12$), even the lattice problem is open - the sharpest known boundary of the RP method.

## 2. Complete-resolution standard

A complete resolution is a proof of BEC as defined above - $n_0>0$ in the thermodynamic limit at fixed density - for an explicitly stated interacting continuum model ($v\ge0$, $v\not\equiv0$, compactly supported or hard-sphere) at explicitly stated $(\rho,\beta)$, ground state accepted, with all computer-assisted steps certified per section 6.
A proof for the lattice hard-core gas at some fixed filling $\neq\tfrac12$ at $T>0$ would be accepted as resolution of the lattice form and must be labeled as such (it is the decisive methodological barrier, though not the continuum headline).

**Not accepted as resolution:**

- BEC in any scaling limit - Gross–Pitaevskii ($Na/L\to\mathrm{const}$ with $N\to\infty$ in a fixed-size box after rescaling), mean-field, or "beyond-GP" exponent regimes - however sharp the rate.
  These limits decouple the interaction range from the interparticle distance; the thermodynamic limit is precisely what they avoid.
- Energy asymptotics (LHY order or beyond) without an order-parameter statement.
- Quasi-averages/symmetry-breaking formulations without control of the $\liminf$ above; superfluid-density or one-mode-dominance statements that do not imply $n_0>0$.
- Path-integral/cycle-percolation numerics (PIMC) or any uncertified computation as evidence.
- The ideal gas, or models with $v\le0$ pathologies, or infinite-range/mean-field interactions in disguise.
- Variational trial-state computations: an upper bound on the energy bounds no eigenvalue of $\gamma$ and says nothing about $n_0$.
- Re-derivations of the lattice half-filling results, however streamlined, presented as new territory.
- 2D/1D statements (BEC is absent at $T>0$ in 2D - Hohenberg 1967; the interesting 2D ground-state question is out of scope here).

## 3. Graded partial-result targets

- **P1 - The gap, formalized.** (a) A precise statement-and-proof document (theorem-grade, no prose hand-waving) delineating exactly what GP/mean-field/beyond-GP theorems assert versus the fixed-density thermodynamic limit: the scaling dictionary, the order of limits, and proven non-implications where obtainable.
  (b) Lean 4 formalization seed: Penrose–Onsager equivalences (operator-norm vs. ODLRO on the torus) and BEC for the 3D ideal gas at $\rho<\rho_c(\beta)$.
  *Certificate:* compiling Lean artifact for (b); for (a), a reviewed theorem file with complete proofs.
- **P2 - The reflection-positivity boundary, sharpened into theorems.**
  Determine precisely which steps of the DLS/KLS chain (RP with respect to a reflection, Gaussian domination, infrared bound, sum rules) survive off half filling and which fail, as proven statements:
  - (i) a theorem listing the exact particle-hole/staggered symmetry used, and a proof that Gaussian domination fails (or survives) for stated perturbations off half filling;
  - (ii) at minimum one new positive extension - e.g. LRO for a perturbed-but-symmetric family (anisotropy, next-nearest structure, soft-core constraints) not in the literature.
  Machine-support: RP and Gaussian-domination conditions on small tori are finite matrix positivity statements - verify candidates by exact/interval computation before proof attempts.
  *Certificate:* proofs; exact-arithmetic positivity transcripts for the finite checks.
- **P3 - Certified finite-size ground truth for condensate fractions.**
  Sparse exact diagonalization of hard-core and Bose–Hubbard gases on tori up to the feasible edge (e.g. hard-core on $3\times3\times3$ at various fillings; dimensions $\binom{27}{n}\lesssim2\times10^7$ - Lanczos with *certified* eigenvalue and eigenvector-residual enclosures, so that $\|\gamma\|_{\mathrm{op}}/N$ carries rigorous error bars), plus continuum few-boson benchmarks via explicitly correlated Gaussians under directed rounding.
  Deliverable: a certified dataset of $n_0(N,L)$ against which finite-size scaling conjectures can be tested honestly.
  *Certificate:* interval enclosures from residual bounds (Weyl/Temple/Kato), independent checker recomputing the bounds from stored vectors.
- **P4 - Conditional BEC theorems.** Prove implications of the form: explicit, in-principle-checkable hypotheses $\Rightarrow$ $n_0>0$.
  Candidate hypotheses to make precise and minimal:
  - uniform-in-volume off-diagonal lower bounds on $\gamma_{N,L}$ at finite range;
  - a quantitative uniform spectral gap plus correlation-clustering assumption;
  - cycle-percolation criteria (Sütő-style) upgraded from the ideal gas to conditional interacting statements.
  The value is the exact isolation of the missing estimate - the analogue of what an infrared bound would deliver.
  *Certificate:* complete proofs; each hypothesis accompanied by its certified finite-size status from P3 (holds/fails/unknown at reachable sizes).
- **P5 - Push a scaling exponent or a structured continuum model.**
  Either (a) extend the proven BEC range in interpolating regimes toward the thermodynamic limit (beyond-GP exponents - Adhikari–Brennecke–Schlein ~2021, Fournais ~2021 (verify current frontier); any certified-constant extension of the exponent range is frontier movement), or (b) prove $T>0$ or ground-state BEC for a continuum model engineered to admit reflection positivity, with every structural concession stated.
  Strongest realistic target short of resolution.

## 4. Known results and prior art

- Bogoliubov 1947: the heuristic theory whose predictions (LHY constants, quasiparticle spectrum) the rigorous program has been confirming order by order.
- Penrose–Onsager 1956: the ODLRO/largest-eigenvalue criterion; Lee–Huang–Yang 1957: the second-order energy prediction.
- Ideal gas: classical (Bose 1924, Einstein 1925; rigorous treatments standard); 2D absence at $T>0$: Hohenberg 1967 (Bogoliubov-inequality argument); Mermin–Wagner 1966 for lattice analogues.
- Lieb–Liniger 1963: 1D exactly solvable Bose gas - solvable benchmark without BEC; useful contrast, not progress on 3D.
- Dyson–Lieb–Simon 1978: reflection positivity + infrared bounds for quantum lattice models; Kennedy–Lieb–Shastry 1988: ODLRO for the XY model / hard-core bosons at half filling (ground state, $d\ge2$); the $T>0$ half-filling statement lives in this RP circle (verify exact attributions before citing).
- Ground-state energy: Dyson 1957 (hard-sphere upper bound); Lieb–Yngvason 1998 (leading-order lower bound $4\pi a\rho$ per particle); LHY second order: Yau–Yin 2009 (upper), Fournais–Solovej 2020 (lower, Annals) and ~2023 (general $v$ incl. hard core); upper bound for hard spheres at LHY order: Basti–Cenatiempo–Schlein ~2021 (verify).
- Scaling-limit BEC: Lieb–Seiringer 2002 (GP ground state); Lieb–Seiringer–Yngvason 2000s program; optimal-rate GP BEC: Boccato–Brennecke–Cenatiempo–Schlein 2018–2020; positive-temperature GP: Deuchert–Seiringer ~2020 (verify); trapped free energy: Deuchert–Seiringer–Yngvason ~2019 (verify).
- Beyond-GP scaling exponents: Adhikari–Brennecke–Schlein ~2021; Fournais ~2021 ("length scales" - verify precise exponent reach).
- Positive-temperature dilute free energy: Seiringer 2008 (lower), Yin ~2010 (upper); LHY-order free energy: Haberberger–Hainzl–Nam–Seiringer–Triay ~2023–2025 (verify).
- c-number substitution made rigorous: Lieb–Seiringer–Yngvason 2005 - but Bogoliubov's argument still does not yield thermodynamic-limit BEC.
- Cycle representation: Sütő 1993, 2002 (ideal-gas BEC $\Leftrightarrow$ infinite cycles); Ueltschi 2000s - conjectural bridge for interacting gases.
- Optical-lattice BEC as a quantum phase transition: Aizenman–Lieb–Seiringer–Solovej–Yngvason 2004 (still RP-anchored, half-filling-type symmetry).
- No proof of interacting continuum thermodynamic-limit BEC exists to our knowledge, at any density or temperature; nor any nontrivial no-go.

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

`[proof]` mode with certified-computation support; single-workstation scale.

1. **RP finite checks first (P2).** Symbolic/exact verification of reflection positivity and Gaussian domination for candidate Hamiltonian families on $2\times2\times2$ and $4^3$ tori: matrix positivity over exact rationals (FLINT/`fmpq_mat` Cholesky with rational pivots; interval fallback in Arb).
   A candidate family that fails the finite check is dead before proof effort - the cheap kill is the method.
- *Failure mode:* checking RP in the wrong inner product/reflection plane; fix the reflection structure in writing before computing.
2. **Certified Lanczos stack (P3).** C++ sparse matvec (bit-packed occupation bases), ARPACK/Lanczos in floating point for candidate vectors, then *certification pass*: interval evaluation of residuals $\|Hv-\lambda v\|$ and Temple/Kato bounds in Arb; store vectors; recompute $\gamma$ and its top eigenvalue with interval arithmetic.
- *Failure mode:* reachable sizes ($\lesssim30$ sites) make thermodynamic extrapolation scientifically tempting and rigorously empty - the dataset is ground truth for hypotheses, never evidence of the limit.
3. **Conditional-theorem workshop (P4).** Draft hypothesis–conclusion pairs; for each, attempt (i) proof of the implication, (ii) P3-based finite-size status of the hypothesis, (iii) consistency with the scaling-limit literature. Iterate toward the minimal hypothesis.
   Keep a graveyard of failed candidate hypotheses with refutations.
4. **Lean 4 (P1b).** Ideal-gas BEC: needs Bose functions, geometric sums over momentum lattice, and elementary trace-class manipulation - genuinely feasible; Penrose–Onsager equivalence on the torus is finite-dimensional-flavored functional analysis.
   Timebox; report the exact formalization frontier reached.
- *Failure mode:* scope creep into general Fock-space theory; resist - torus-specific statements suffice.
5. **Scaling-frontier bookkeeping (P5a).** Before any attempt on exponents, produce a one-page exact map of the currently proven $(\beta_s$, rate$)$ frontier from the literature (with (verify) flags), so that any claimed extension is measured against a written baseline rather than memory.
- *Failure mode:* the beyond-GP literature moves fast; an "extension" that merely re-proves a 2024–2026 result is wasted effort - the baseline map is mandatory before work starts.
6. **Do not attempt** direct continuum thermodynamic-limit analysis by brute computation (no finite computation addresses it), and do not burn the session re-proving scaling-limit results that are already sharp.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** RP/positivity checks in exact rational arithmetic; all P3 enclosures in Arb interval arithmetic with directed rounding; floating-point Lanczos output is exploratory until the certification pass converts it; no uncertified number enters any claim.
2. **Independent verification.** A standalone checker recomputes every P3 enclosure from stored vectors and matrices without the search/diagonalization code; dual implementations for the RP positivity checks (SymPy rational vs. FLINT); Lean artifacts kernel-checked with `#print axioms`.
3. **Reproducibility.** Basis orderings, lattice geometries, fillings, and truncation/precision parameters recorded exactly; SHA-256 manifest over Hamiltonian definitions, stored eigenvectors, certificates, theorem files, and Lean sources.
4. **Preservation.** The P2/P4 graveyards - families failing finite RP checks, hypotheses refuted at finite size - are primary deliverables and are preserved with their refutation data; the boundary of the RP method is the scientific product.
5. **Honest reporting.** The final report opens by stating that thermodynamic-limit BEC for an interacting gas remains unproven unless section 2 was met (expected); every positive statement names its ensemble, filling, and model class; scaling-limit results are never described in thermodynamic-limit language; conditional theorems always appear with their unverified hypotheses in the same sentence.
