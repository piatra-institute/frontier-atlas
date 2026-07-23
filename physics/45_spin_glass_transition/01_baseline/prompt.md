# PROMPT FOR PROVING A FINITE-TEMPERATURE PHASE TRANSITION IN THE 3D EDWARDS–ANDERSON SPIN GLASS

## Existence of spin-glass order at positive temperature in short-range disordered Ising models

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 45 of 50 (Tier 4)
**Source:** top-50 list #17, category B (rigorous many-body and condensed matter)
**Modes:** `[proof]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Four decades of numerics agree that the three-dimensional Edwards–Anderson spin glass orders at a finite temperature ($T_c\approx1.1$ for $\pm J$ couplings, $T_c\approx0.95$ for Gaussian - note the common misattribution of $0.95$ to $\pm J$), yet there is no rigorous proof that $T_c>0$ in any finite dimension for any short-range spin-glass model.
The mean-field Sherrington–Kirkpatrick model is completely solved (Parisi formula: Guerra 2003, Talagrand 2006, Panchenko 2013), which makes the short-range existence question the sharpest embarrassment in mathematical statistical mechanics: before replica-symmetry-breaking versus droplets can even be posed rigorously, mere existence of the transition is open.
The standard machines all fail - no FKG, no reflection positivity, no infrared bound.
This Tier 4 prompt targets the graded ladder: certified high-temperature uniqueness frontiers, exact small-volume ground truth (interface free energies, stiffness), rigorous series with certified remainders, and - the strategic heart - design of a finite-volume, machine-checkable criterion that provably implies spin-glass order, in the spirit of what Peierls and infrared bounds do for ordered systems.
The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

**Model.** On $\Lambda_L=\{-L,\dots,L\}^3\subset\mathbb{Z}^3$ with Ising spins $\sigma:\Lambda_L\to\{\pm1\}$ and i.i.d. couplings $J=(J_{xy})$ on nearest-neighbor edges,

\[
H_{\Lambda_L}^{J}(\sigma)\;=\;-\sum_{\langle xy\rangle\subset\Lambda_L} J_{xy}\,\sigma_x\sigma_y ,
\]

with either $\mathbb{P}(J_{xy}=\pm1)=\tfrac12$ ($\pm J$ model) or $J_{xy}\sim\mathcal{N}(0,1)$ (Gaussian model).
Quenched Gibbs states $\langle\cdot\rangle_{\beta,\Lambda_L}^{J}$ at inverse temperature $\beta$, with stated boundary conditions (free/periodic unless specified).
Quenched free energy density $f(\beta)=-\lim_{L\to\infty}(\beta|\Lambda_L|)^{-1}\,\mathbb{E}\log Z^J_{\beta,\Lambda_L}$ exists and is self-averaging (Guerra–Toninelli 2002).

**Order parameters.** Two-replica overlap correlations: for the same disorder, two independent Gibbs copies $\sigma,\tau$;

\[
q_x=\sigma_x\tau_x,
\qquad
C(x)\;=\;\mathbb{E}\big[\langle\sigma_0\sigma_x\rangle^2\big],
\qquad
\chi_{\mathrm{SG}}(\beta)\;=\;\sum_{x\in\mathbb{Z}^3} C(x)
\]

(infinite-volume limits along stated boundary conditions/subsequences).

**Adopted formulation of the open problem.** Prove that for the 3D EA model ($\pm J$ or Gaussian - either is acceptable; state which) there exists $\beta<\infty$ such that spin-glass order holds, in at least one of the following precise senses, each acceptable and to be named explicitly in any claim:

- **(T1)** $\limsup_{|x|\to\infty} C(x)>0$ (nonvanishing Edwards–Anderson-type order parameter);
- **(T2)** $\chi_{\mathrm{SG}}(\beta)=\infty$ at some finite $\beta$ (divergent spin-glass susceptibility);
- **(T3)** $f$ is non-analytic at some $\beta_c\in(0,\infty)$.

(T1)$\Rightarrow$(T2); (T3) is the weakest and still open. A proof of any of (T1)–(T3) resolves the problem at its level; the headline question is (T1)/(T2).

**Finite-volume observables (used throughout section 3).** For a disorder sample $J$ on the $L^3$ torus, the interface (domain-wall) free energy is

\[
\Delta F_J(L)\;=\;-\beta^{-1}\Big(\log Z^{J,\mathrm{AP}}_{\beta,L}-\log Z^{J,\mathrm{P}}_{\beta,L}\Big),
\]

with periodic (P) versus antiperiodic (AP) boundary conditions in one coordinate direction; the stiffness exponent $\theta$ is defined through the $L$-scaling of the sample median of $|\Delta F_J(L)|$ (droplet-theory diagnostic: $\theta>0$ expected in 3D, $\theta<0$ in 2D - non-rigorous).
At $\beta=\infty$ the same quantity is the ground-state energy difference, an exactly computable integer ($\pm J$) or algebraic sum (Gaussian).

**Contrast facts to keep straight.** In $d=2$ the transition is believed absent ($T_c=0$) but a full rigorous proof of uniqueness/analyticity for all $T>0$ is *also* open (verify current status - partial results only). On the Nishimori line, and for the weakly disordered random-bond Ising model, *ferromagnetic* order at low temperature is provable - but ferromagnetic order under weak disorder is a different phenomenon and does not touch (T1)–(T3) at zero mean coupling.

## 2. Complete-resolution standard

A complete resolution is a proof, for the 3D EA model with zero-mean i.i.d. couplings ($\pm J$ or Gaussian, stated), that at some explicit finite $\beta$ one of (T1)/(T2) holds (or (T3), constituting resolution of the weakest form, and labeled as such).
All computer-assisted steps must be certified per section 6; if the proof is conditional on a finite computation (the intended breakthrough path of P4 below), that computation must be completed and certified, not estimated.

**Not accepted as resolution:**

- Numerical evidence of any quality (Monte Carlo, finite-size scaling, series extrapolation) for $T_c>0$.
- Results for the SK model, Bethe lattices/random graphs, hierarchical models, or $d\ge d_0$ with $d_0$ large and unspecified reach to $d=3$ (each valuable; none is 3D EA).
- Transitions in modified short-range models (correlated disorder, vector spins with special couplings, models engineered for reflection positivity) - this is target P5, explicitly partial.
- Zero-temperature statements (ground-state degeneracy, disorder chaos, stiffness numerics) presented as finite-$T$ transitions.
- Non-analyticity of dynamical or metastable quantities; aging results.
- "Transition of the overlap distribution" in finite volume without an infinite-volume theorem.

## 3. Graded partial-result targets

Calibration: a full proof would be a once-a-decade event; P1–P3 are solid deliverables, P4 is the strategic bet, P5–P6 are stretch.

- **P1 - Certified high-temperature frontier.**
  Produce the best certified $\beta_0$ such that for all $\beta<\beta_0$ the 3D EA model ($\pm J$ and Gaussian) has a unique Gibbs state with exponentially decaying $C(x)$, via Dobrushin-uniqueness or cluster-expansion conditions with all constants enclosed in interval arithmetic (for Gaussian couplings the disorder average of the Dobrushin coefficient is an explicit integral - certify it with Arb quadrature).
  Compare against the literature's uniqueness region (verify current best).
  *Certificate:* the finite condition (matrix norm / expansion convergence inequality) evaluated in interval arithmetic with an independent checker.
- **P2 - Exact small-volume ground truth.**
  (a) Exact quenched averages on small tori: for $\pm J$ on $L^3$, $L\le4$ cross-sections via transfer matrices with polynomial (exact rational in $\tanh\beta$) entries; full disorder enumeration where feasible (strips/small tori), exactly sampled disorder with recorded seeds otherwise - labeled as sampled.
  (b) Certified interface free energies: $\Delta F(L)=F_{\mathrm{AP}}-F_{\mathrm{P}}$ (periodic vs. antiperiodic) computed exactly per disorder sample at $L\le6$ (exact partition functions via transfer matrix; ground-state versions via exact branch-and-cut or MaxSAT with certificates), giving certified stiffness data confronting $\theta_{3D}\approx0.2$ vs. $\theta_{2D}<0$ (non-certified literature values - verify).
  Deliverable: a public table of exact $(L,\beta)$ interface data with the disorder-set definition (enumerated or seeded) attached to every row.
  *Certificate:* exact rational outputs; MaxSAT optimality certificates checked independently.
- **P3 - Rigorous high-temperature series with certified remainder.**
  Recompute the quenched series for $\chi_{\mathrm{SG}}$ in $w=\tanh^2\beta$ ($\pm J$: coefficients are exact rationals via free-graph counting) to the current known order and beyond if feasible (literature reaches high order - verify, cf. Singh–Chakravarty 1986 tradition); prove a certified lower bound on the radius of convergence, yielding a rigorous analyticity region (complements P1).
  State plainly: series analysis (Dlog-Padé estimates of $T_c$) is exploration, never certification.
  *Certificate:* exact coefficient tables with two independent graph-counting implementations; remainder bounds proved, constants in interval arithmetic.
- **P4 - A machine-checkable finite-volume criterion (strategic heart).**
  Formulate and prove a theorem of the form: *if* an explicit, finite, quenched inequality at scale $L_0$ holds (e.g. a certified lower bound on a renormalization-style overlap-coupling quantity, a coarse-grained Peierls-type contour estimate for the two-replica system, or a finite-size condition in the style of Lieb–Simon/rigorous-RG for disordered systems), *then* (T1) or (T2) holds at some $\beta$.
  Then attempt to verify the hypothesis by certified computation at reachable $L_0$.
  The two-replica representation (order parameter $q_x=\sigma_x\tau_x$, whose interactions are still disordered but ferromagnetic-in-$q$ correlations are the object) is the suggested arena.
  Honest calibration: no such criterion is known; even a criterion whose hypothesis is *false* at reachable sizes, or whose verification cost is proven astronomical, is a publishable structural result.
  *Certificate:* the theorem (human proof, formalizable core), plus the certified computation transcript for the hypothesis test - whichever way it comes out.
- **P5 - Transition in an honest modified model.**
  Prove (T1)-type order for a 3D short-range disordered model as close to EA as achievable - e.g. a reflection-positive disordered variant, or zero-mean couplings with special correlation structure. Every deviation from i.i.d. zero-mean nearest-neighbor EA must be listed in the statement. *Certificate:* complete proof.
- **P6 - Sharpened structural theorems for EA.**
  Extend what is provable unconditionally: Ghirlanda–Guerra identities and stochastic stability consequences specialized to 3D with quantitative content; correlation inequalities for two-replica observables (find any nontrivial one - none is known; a single proven FKG-substitute for the $q$-field would be significant).
  *Certificate:* proofs; machine verification of finite-lattice instances of any conjectured inequality before proof attempts (a certified counterexample kills a false conjecture cheaply - also valuable).

## 4. Known results and prior art

- Edwards–Anderson 1975: the model. Sherrington–Kirkpatrick 1975: mean-field version.
- Mean-field solved: Guerra 2003 (bound), Talagrand 2006 (Parisi formula), Panchenko 2013 (ultrametricity; book) - methods do not transfer to short range.
- Guerra–Toninelli 2002: existence/self-averaging of the EA free energy; Guerra–Toninelli ~2004: interpolation comparisons between short-range and mean-field free energies (verify direction and scope).
- Fröhlich–Simon–Spencer 1976 / Dyson–Lieb–Simon 1978: the infrared-bound machinery that proves transitions for ordered systems - cited here as the template P4 tries to imitate, and which fails verbatim for EA (no reflection positivity in the disordered case).
- Ghirlanda–Guerra 1998; Aizenman–Contucci 1998: identities/stochastic stability valid for EA; Newman–Stein 1990s–2000s (metastates), Newman–Stein book 2013; Contucci–Giardinà book 2013; Talagrand's two-volume treatise 2011.
- Nishimori 1981: gauge identities on the Nishimori line - exact internal energy, correlation identities; a rare island of exactness for EA-type models.
- Droplet/scaling phenomenology: Bray–Moore ~1984; Fisher–Huse 1986–1988 - the non-rigorous framework the stiffness data of P2 confronts.
- Fröhlich–Zegarliński ~1987: high-temperature regime results for short-range spin glasses (verify exact scope).
- Zero temperature, 2D: Arguin–Damron–Newman–Stein 2010s–2020s ground-state structure results; Chatterjee ~2023: disorder chaos / zero-temperature EA results (verify precise statements). None yields finite-$T$ 3D order.
- We know of *no* "Ding–Sly-type" existence result for EA order (the attribution circulating in some problem lists did not survive our check - verify independently; Ding–Sly concern other models).
- Numerics: Katzgraber–Körner–Young 2006 ($T_c\approx0.95$, Gaussian); Hasenbusch–Pelissetto–Vicari 2008 and Janus collaboration (Baity-Jesi et al. 2013) ($T_c\approx1.10$, $\pm J$) (verify values).
- High-temperature series: Singh–Chakravarty 1986 and successors (verify current highest order).
- 2D nonexistence: believed, with strong numerics and droplet arguments; full rigorous uniqueness for all $T>0$ in 2D EA remains open to our knowledge (verify - do not cite 2D as "proven absent").

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

`[proof]`+`[cert]`; all computations single-workstation.

1. **Dobrushin/cluster-expansion certifier (P1).**
   Interval evaluation (Arb) of Dobrushin influence coefficients - for $\pm J$ a finite maximization over local coupling patterns (exact); for Gaussian, certified quadrature over the coupling density.
   Independent check: cluster expansion (Kotecký–Preskill-style condition) as a second, independent route to a (possibly different) $\beta_0$; report both.
- *Failure mode:* worst-case-over-disorder Dobrushin bounds collapse to the ferromagnetic bound and waste the zero-mean structure - quantify exactly how much is lost; that gap is itself informative for P4.
2. **Exact transfer-matrix stack (P2, P3).**
   C++ with FLINT `fmpq_poly` entries: transfer matrices over $4\times4\times L$ tori ($2^{16}$ states) with polynomial arithmetic in $\tanh\beta$; disorder handling: full enumeration only on strips/small cells (the $2^{\#\mathrm{bonds}}$ wall is real - never claim quenched exactness beyond enumerated sets); elsewhere seeded sampling, labeled.
3. **Ground states and interfaces (P2b).** Exact ground states via MaxSAT (EvalMaxSAT/UWrMaxSat) with optimality certificates, or ILP with exact rational duals; P/AP boundary-condition pairs per sample.
- *Failure mode:* 3D ground states are NP-hard - sizes cap near $6^3$–$8^3$ per sample at certificate quality; do not trade certificates for size.
4. **Series engine (P3).** Free-graph/star-graph expansion with exact rational bookkeeping; two independent implementations (Python/SymPy prototype vs. C++/FLINT) must agree to the last coefficient before any coefficient is published.
- *Failure mode:* embedding-count bugs are the classic silent killer - the dual-implementation rule is mandatory, not advisory.
5. **Criterion design loop (P4).** Work in the two-replica ($q$-field) representation; prototype candidate finite-volume inequalities; *test each candidate numerically on small exact data from P2 before attempting proofs* - most candidates die in minutes this way, which is the point of having certified ground truth.
6. **Optional Lean 4 target:** formalize the Ghirlanda–Guerra derivation for finite systems (finite probability + algebra; feasible) as a seed for machine-checked spin-glass theory.
- *Failure mode across all steps:* silently averaging over too few disorder samples and reporting the result as quenched - every table must carry its exact disorder-set definition (enumerated or seeded-sampled) in the same artifact.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** Series coefficients and transfer-matrix outputs exact rational; Dobrushin/cluster constants and Gaussian disorder integrals in Arb intervals with directed rounding; MaxSAT/ILP results carry optimality certificates.
   Monte Carlo appears nowhere in a certified claim.
2. **Independent verification.** Dual implementations for series and transfer matrices; standalone checkers for Dobrushin condition evaluation and for MaxSAT certificates; any P4 criterion's hypothesis test re-run from the theorem statement alone by a checker that never imports the search code.
3. **Reproducibility.** Disorder samples: seeds and generator versions recorded; enumerated disorder sets defined exactly; SHA-256 manifest over coefficient tables, certificates, samples, and code.
4. **Preservation.** The P4 graveyard - candidate criteria and the small-volume data that killed them - is a primary deliverable; preserve every candidate with its refutation.
5. **Honest reporting.** The final report opens by stating that $T_c>0$ for 3D EA remains unproven unless section 2 was met (expected); every statement names its sense (T1)/(T2)/(T3), its coupling distribution, and its boundary conditions; sampled-disorder results are never phrased as quenched theorems; series-extrapolation numbers are never phrased as bounds.
