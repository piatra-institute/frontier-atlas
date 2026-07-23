# PROMPT FOR CERTIFIED BOUNDS ON THE REINHARDT PACKING MINIMUM

## The Reinhardt conjecture: is the smoothed octagon the worst-packing symmetric convex body?

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 25 of 50  
**Area:** discrete geometry  
**Modes:** `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Among all centrally symmetric convex bodies in the plane, which one is *hardest* to pack - has the lowest maximum packing density? Reinhardt conjectured (1934) that it is the "smoothed octagon", a regular octagon with corners rounded by hyperbolic arcs, packing to density \(\approx 0.902414\), below the disk's \(\pi/\sqrt{12}\approx0.9069\). The conjecture is open. Unlike the finite problems in this program it is a genuine infinite-dimensional variational problem - recently recast by Hales and collaborators as an optimal-control problem with a bang-bang solution. Honesty up front: full resolution is out of scope for a single workstation. The realistic, valuable product is *certified partial structure* - a rigorous lower bound on the worst-case density, a certified re-proof of the smoothed octagon's local optimality, or the certified exclusion of classes of competitors. The resolution standard names the full conjecture; everything short of it is reported as the certified partial result it is.

## 1. Exact problem statement

A **centrally symmetric convex body** is a compact convex set \(K\subset\mathbb{R}^2\) with nonempty interior and \(K=-K\). Its **packing density** is

\[
\delta(K)=\sup\Bigl\{\text{upper density of }\mathcal{P}\ :\ \mathcal{P}\text{ a packing of the plane by congruent copies of }K\Bigr\}\in(0,1].
\]

Structural reductions that make \(\delta(K)\) computable:

- For centrally symmetric convex bodies the supremum is achieved by a **lattice packing** (Rogers 1951; L. Fejes Tóth), so \(\delta(K)\) equals the lattice packing density.
- The lattice density equals \(\operatorname{area}(K)\) divided by the area of the smallest centrally symmetric hexagon circumscribing \(K\) (the Reinhardt / Fejes-Tóth reduction).
- \(\delta(K)\) is affine-invariant, so \(K\) is taken modulo \(GL_2(\mathbb{R})\).

Define the **Reinhardt minimum**

\[
\delta_\star=\inf_{K=-K\text{ convex}}\delta(K).
\]

**Reinhardt's conjecture:** the infimum is attained by the **smoothed octagon** \(O_s\), with

\[
\delta(O_s)=\frac{8-4\sqrt{2}-\ln 2}{2\sqrt{2}-1}\approx 0.902414,
\]

a regular octagon whose corners are replaced by arcs of the hyperbola \(xy=\text{const}\) tangent to the adjacent edges. For comparison, the disk gives \(\pi/\sqrt{12}\approx0.9069\) and the regular octagon \(\approx0.906\); the smoothing *lowers* the density.

Configuration space and formulation:

- Parametrize \(K\) by its support function \(h:\mathbb{R}/2\pi\mathbb{Z}\to\mathbb{R}\), even (\(h(\theta)=h(\theta+\pi)\), central symmetry), with the convexity constraint \(h+h''\ge 0\) (as a measure).
- For each \(K\), \(\delta(K)\) is the lattice packing density, an optimization over admissible lattices (equivalently the minimal circumscribing centrally-symmetric hexagon).
- The problem \(\min_K\delta(K)\) is thus an optimization over the infinite-dimensional cone of even support functions, modulo affine maps.
- **Optimal-control reformulation (Hales).** The Euler–Lagrange structure admits a Pontryagin formulation whose extremal is bang-bang, the switches producing the octagon's straight/curved alternation. We adopt \(\delta_\star=\inf_K\delta(K)\) as primary and treat the control formulation as the analytic tool.

Well-posedness and scope notes:

- The infimum \(\delta_\star\) is attained (the space of centrally symmetric convex bodies modulo affine maps is compact in the Banach–Mazur / Hausdorff topology, and \(\delta\) is continuous), so "minimizer" is meaningful - the open question is *which* body, not whether one exists.
- Smooth bodies and polygons are both admissible; the conjectured optimum is neither purely smooth nor polygonal but a hybrid (straight edges joined by curved corners), which is why finite polygon/smooth families never contain it and a discretized search cannot reach it.
- The candidate value \(\delta(O_s)\approx0.902414\) is below every "nice" competitor (disk \(\approx0.9069\), regular octagon \(\approx0.906\)); the difficulty is proving nothing does better.

Adopted conventions: the plane \(\mathbb{R}^2\); density affine-invariant; "smaller density = harder to pack." No informal target is acceptable; deliverables are the certified statements of section 2.

## 2. Resolution standard

**(R1) Full conjecture.** A proof that \(\delta_\star=\delta(O_s)\) and that \(O_s\) is (up to affine equivalence) the unique minimizer. Certified form: a complete variational proof; any finite computational input (a certified interval enclosure of a critical value, a certified exclusion region in a reduced parameter space, a Positivstellensatz certificate for a polynomial inequality) must be exact or interval-verified.

**(R2) Certified global lower bound.** A rigorous inequality \(\delta(K)\ge L\) for *all* centrally symmetric convex \(K\), with \(L\) as large as possible (the target is \(L\to\delta(O_s)\)). Certified form: an **interval-arithmetic / certified-optimization proof** valid uniformly over the (reduced) body space, e.g. a certified lower bound on the density functional via a verified relaxation. Any improvement over the best previously *certified* uniform lower bound is a genuine result.

**(R3) Certified local optimality.** A rigorous proof that \(O_s\) is a strict local minimum of \(\delta\) in the body space (a certified re-proof and, ideally, a quantified neighborhood), via interval-verified second-variation / control-theoretic conditions.

**Not accepted as resolution.**

- A numerical minimization over a finite-dimensional family of bodies that "lands on" the smoothed octagon - a discretized search is not a proof over the infinite-dimensional cone.
- Verifying \(\delta(O_s)\approx0.902414\) to more digits; the value of the *candidate* is not in question, its *minimality* is.
- Local optimality presented as global optimality.
- Ruling out one competitor family and calling the conjecture settled.
- A control-theoretic derivation whose transversality / second-order conditions are asserted numerically rather than certified.

Stress: over an infinite-dimensional configuration space, a finite numerical search establishes *nothing* about the global minimum. The product is a rigorous inequality or a certified structural statement.

## 3. Graded partial-result targets

**P1 - Certify the candidate value.** Establish \(\delta(O_s)=(8-4\sqrt2-\ln2)/(2\sqrt2-1)\) rigorously, deriving the hyperbolic-arc geometry and the lattice density.
*Certificate:* symbolic derivation plus an interval enclosure of the closed form.

**P2 - Certified density for finite families.** For explicit finite-parameter families interpolating disk \(\to\) regular octagon \(\to\) smoothed octagon (and other symmetric bodies), certify \(\delta(K)\) as interval enclosures and confirm \(O_s\) is the family minimum.
*Certificate:* per-body interval density with a certified circumscribing-hexagon computation.

**P3 - Certified uniform lower bound (weak).** A rigorous \(\delta(K)\ge L_0\) for all \(K=-K\) convex, with \(L_0\) below \(\delta(O_s)\) but as high as a workstation-certified argument allows.
*Certificate:* an interval-verified relaxation valid over the reduced body cone.

**P4 - Certified exclusion of a competitor class.** Prove no body in a stated structured class (e.g. polygons with \(\le m\) sides, or bodies with a given symmetry) beats \(O_s\).
*Certificate:* interval global optimization over that finite-dimensional subfamily proving \(\delta\ge\delta(O_s)\) on it.

**P5 - Certified local optimality (this is R3).** Interval-verified strict local minimality of \(O_s\), with a quantified neighborhood if possible.
*Certificate:* an interval-verified second-variation positivity proof with gauge directions quotiented out.

**P6 - Certified lower bound approaching \(\delta(O_s)\) (toward R2).** Push \(L\) upward with a certified uniform argument; report the certified gap \(\delta(O_s)-L\).
*Certificate:* the improved relaxation plus its exact/interval optimal value.

**P7 - Control-formulation reproduction.** Independently reproduce the Hales optimal-control reduction and certify the extremal's switching structure.
*Certificate:* symbolic/interval verification of the Pontryagin conditions and switch points.

## 4. Known results and prior art

- **Origin and candidate.** K. Reinhardt (1934) introduced the smoothed octagon and conjectured its packing density is the minimum among centrally symmetric convex bodies; the density \(\approx0.902414\) (verify the closed form).
- **Reduction to lattices.** For centrally symmetric convex bodies the densest packing is a lattice packing (Rogers 1951; L. Fejes Tóth), reducing \(\delta(K)\) to a computable lattice / circumscribing-hexagon quantity.
- **Local optimality.** **F. Nazarov (1988)** proved the smoothed octagon is a *local* minimum of the packing density among centrally symmetric convex bodies (verify) - a landmark partial result; global minimality remains open.
- **Related bounds and bodies.** Mahler, Ennola, and Tammela studied extremal lattice-packing questions and local minima (approximate mid-20th century; verify). **Y. Kallus (2015)** studied "pessimal packing" shapes and the smoothed-octagon phenomenon in related settings (verify).
- **Three-dimensional analogue.** The analogous "worst-packing convex body in \(\mathbb{R}^3\)" is wide open and even the candidate is unclear; the planar Reinhardt problem is the tractable entry point (verify).
- **Circle comparison.** That the disk (\(\pi/\sqrt{12}\approx0.9069\)) is not the worst packer was itself once surprising; the smoothed octagon beats it, and Reinhardt asserts nothing beats the octagon.
- **Optimal-control formulation.** **T. Hales** and collaborators (with W. Kusner, K. Vajjha; approximately 2011–2022) recast the Reinhardt problem as an optimal-control / Pontryagin problem, showing the conjectured optimizer is a bang-bang extremal (verify the exact papers and claims).
- **Status.** The conjecture is open. No global proof; Nazarov's local result and the control-theoretic program are the state of the art.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the smoothed-octagon closed-form density, the precise statement of Nazarov's local-optimality theorem, and the current state of the Hales optimal-control program (including any partial global results) before claiming any increment.

## 5. Attack plan

**`[opt]` value and family certification (entry point).**

- Derive \(O_s\)'s geometry (hyperbolic corner arcs tangent to octagon edges) symbolically (**SageMath** / SymPy), compute its densest lattice via the minimal circumscribing centrally-symmetric hexagon, and enclose \(\delta(O_s)\) in interval arithmetic (**Arb/FLINT**). This validates the pipeline and P1.
- For finite-parameter body families, compute \(\delta(K)\) as a certified min-area circumscribing-hexagon problem, interval-verified over the parameter range (**kv** / **CAPD**), giving P2/P4.

**`[opt]` uniform lower bounds and local optimality.**

- Reproduce the Hales optimal-control reduction on paper; identify the density functional's second variation at \(O_s\) and attempt an interval-verified positivity certificate (P5, R3).
- For a certified uniform lower bound (P3/R2), formulate a relaxation of \(\min_K\delta(K)\) - via the circumscribing-hexagon dual, or moment/SOS relaxations of the finite-dimensional reductions - and certify its optimal value with exact SDP duals or interval arithmetic.

**Tools.**

- Arb/FLINT and kv/CAPD for interval enclosures of \(\delta(O_s)\) and family densities;
- SageMath / Singular / Macaulay2 for the symbolic geometry and any Positivstellensatz / SOS certificates;
- a custom C++ / Julia global optimizer for the finite-dimensional competitor subfamilies, with interval post-certification;
- an SDP solver (with exact rational rounding of the dual) for the moment/SOS relaxations behind any uniform lower bound.

**One-workstation scope and honesty.** This is a Tier-3, proof-heavy problem: the infinite-dimensional minimization is not going to fall to a workstation search. Realistic deliverables are P1–P5. Do not represent a discretized numerical minimum as evidence for the conjecture; the value of the candidate is not in doubt, only its global minimality.

**First-session checklist (concrete).**

1. Derive the smoothed-octagon geometry symbolically and enclose \(\delta(O_s)\) in interval arithmetic; confirm \(\approx0.902414\) (P1).
2. Build the disk \(\to\) regular octagon \(\to\) smoothed octagon family and certify \(\delta(K)\) across it, confirming \(O_s\) is the family minimum (P2).
3. Reproduce the Hales optimal-control reduction on paper and identify the switching structure (P7).
4. Set up the second variation of \(\delta\) at \(O_s\), quotient the affine/rotation gauge, and attempt an interval positivity certificate (P5).
5. Pick one competitor class (polygons with \(\le m\) sides) and interval-optimize \(\delta\) over it to attempt exclusion (P4).

**Failure modes.**

- Discretizing the body space and mistaking a finite-dimensional minimum for a global result - the central trap.
- An interval second-variation computation that fails to close because of the continuous affine/rotation symmetries (gauge directions must be quotiented out).
- Errors in the lattice-density reduction (using the wrong circumscribing polygon).
- Treating the control-formulation's optimality conditions as proved when they rest on un-certified numerics.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** The candidate density \(\delta(O_s)\), all finite-family densities, any uniform lower bound, and any second-variation positivity claim are computed with interval arithmetic and directed rounding (Arb/kv/CAPD) or exact symbolic / SOS certificates. Floating point is exploration only; a discretized numerical minimum is never a certificate.
2. **Independent verification.** A standalone checker, independent of the derivation: (a) re-encloses \(\delta(O_s)\) from the geometric definition; (b) re-verifies each finite-family interval density and any exclusion-region computation; (c) independently checks any SOS / Positivstellensatz certificate (a second SDP solve with exact rational rounding of the dual). A second CAS reproduces the symbolic geometry.
3. **Reproducibility.** Body parametrizations, the lattice-density reduction used, interval tolerances, SDP/SOS formulations and solver versions, and all parameter ranges are recorded; a SHA-256 manifest over derivations, certificate files, and logs.
4. **Preservation.** The symbolic-geometry scripts, the interval-certification code, the competitor-subfamily optimizer, and any SOS pipelines are part of the record; anything not preserved is stated (the Hadamard-668 lost-source lesson). A `NEXT_STEPS.md` records the current certified lower bound and the remaining gap (the Moore-57 pattern).
5. **Honest reporting.** The report states up front that the full conjecture was (almost certainly) not resolved, and names precisely which certified partial result was obtained - the value of \(O_s\), a certified uniform lower bound with its gap to \(\delta(O_s)\), a certified local optimality, or a certified competitor-class exclusion. A finite numerical search is never presented as evidence for global minimality.
