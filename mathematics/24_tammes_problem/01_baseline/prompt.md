# PROMPT FOR A CERTIFIED TAMMES OPTIMUM AT AN OPEN N

## The Tammes problem: the best-separated N points on the sphere \(S^2\)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 24 of 50  
**Area:** discrete geometry  
**Modes:** `[cert]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Tammes problem asks for the placement of \(N\) points on the unit sphere that maximizes the minimum pairwise distance - the packing of \(N\) equal spherical caps. Despite a century of attention it is *rigorously* solved only for \(N\le 14\) and \(N=24\); every other \(N\) (starting at \(N=15\)) is open. The modern proofs (Musin–Tarasov) are computer-assisted and structural: enumerate the finitely many combinatorial types of contact graph that an optimum could have, then eliminate all but one by rigorous local analysis. This is a `[cert]`/`[opt]` target with a real, reproducible proof architecture and an exact verifier - adjacent to kissing numbers (problem 06) and the Thomson problem (problem 50). The resolution standard is a certified proof that a named configuration is optimal for a specific open \(N\). A numerically superb configuration, even one matching every published digit, is a *lower-bound witness* only, never a proof of optimality.

## 1. Exact problem statement

Let \(S^2=\{x\in\mathbb{R}^3:\lVert x\rVert_2=1\}\). For \(X=(x_1,\dots,x_N)\in(S^2)^N\) define the **separation**

\[
\psi(X)=\min_{1\le i<j\le N}\theta(x_i,x_j),
\qquad \theta(x_i,x_j)=\arccos\langle x_i,x_j\rangle\in[0,\pi],
\]

the least geodesic angle between distinct points. The **Tammes value** is

\[
\Theta_N=\max_{X\in(S^2)^N}\psi(X).
\]

Metric equivalence and normalization:

- With chordal distance \(d(x_i,x_j)=\lVert x_i-x_j\rVert_2=2\sin(\theta/2)\), maximizing \(\min_{i<j}d\) yields the *same* optimizers, since \(\theta\mapsto 2\sin(\theta/2)\) is increasing on \([0,\pi]\).
- \(\Theta_N\) may be reported as an angle, as the chord \(d_N=2\sin(\Theta_N/2)\), or as \(N\) spherical caps of angular radius \(\Theta_N/2\); reports must state which.
- The unit sphere has radius 1.

The maximum is attained by compactness of \((S^2)^N\) and continuity of \(\psi\). Optima are determined only up to the isometry group \(O(3)\) and relabeling \(S_N\); the reduced space is \((S^2)^N/(O(3)\times S_N)\).

**Contact graph.** For an optimal (or candidate) \(X\), the **contact graph** \(\Gamma(X)\) has vertex set \(\{1,\dots,N\}\) and an edge \(ij\) iff \(\theta(x_i,x_j)=\psi(X)\) (a "touching" pair).

- \(\Gamma(X)\) embeds as a planar graph on the sphere; its combinatorial type is the object the Musin–Tarasov method enumerates.
- An optimum is *irreducible*: no local move increases \(\psi\), which constrains \(\Gamma\) - minimum-degree bounds, no separating structure, rigidity-type conditions, and Euler/face-count relations.

Degeneracies and well-posedness:

- For \(N\ge 2\) the optimum has \(\Theta_N>0\); antipodal or coincident points never occur at an optimum for \(N\ge 3\) beyond the forced structure.
- The problem is invariant under a global rotation/reflection, so any reported \(X^\star\) is one representative of an \(O(3)\)-orbit; gauge must be fixed before interval certification (e.g. pin one point to the north pole and one great-circle direction).
- Optima may have continuous families (rare) or isolated points; the contact graph distinguishes the cases.

Adopted conventions:

- Geodesic metric primary; chordal equivalent stated alongside.
- "Open \(N\)" means \(N\notin\{2,\dots,14\}\cup\{24\}\) (verify this proven set - section 4); the flagship target is the smallest open case, \(N=15\).

No informal target ("a very even spread") is acceptable - the deliverable is a proof per section 2.

## 2. Resolution standard

**(R1) Certified optimum at an open \(N\).** For a named open \(N\), an explicit configuration \(X^\star\) (coordinates as algebraic numbers or interval enclosures) and a *certified proof* that \(\Theta_N=\psi(X^\star)\). The accepted certified form is a **Musin–Tarasov-style proof**:

1. a complete, isomorph-free enumeration of the candidate contact graphs consistent with the necessary conditions for an optimum at \(N\);
2. for each candidate graph, a rigorous bound - via **interval arithmetic** on the associated system of angle constraints (an interval-Newton / branch-and-bound certifying either infeasibility above \(\psi(X^\star)\), or that the graph's best value is \(\le\psi(X^\star)\));
3. identification of the unique maximizing type, with \(X^\star\) its exact solution and the global upper bound \(\Theta_N\le\psi(X^\star)\) certified.

An alternative accepted form is a direct interval-arithmetic global optimization over \((S^2)^N/\text{sym}\) proving \(\Theta_N\le\psi(X^\star)\), if it can be pushed to closure.

**Not accepted as resolution.**

- A configuration from a spherical-optimization code with a high \(\psi\) value and no upper-bound proof - a *lower-bound witness*, not a determination of \(\Theta_N\).
- Matching a published conjectural optimum to more digits, or reproducing a known table.
- An enumeration of contact graphs that is not proved *complete* (missing the isomorph-free completeness argument), even if every listed graph is analyzed.
- A single candidate graph solved rigorously while others are dismissed numerically.
- Local optimality / rigidity of one configuration presented as global optimality.

Emphasize: the whole difficulty is the universally-quantified upper bound \(\Theta_N\le\psi(X^\star)\) over an uncountable configuration space. Numerical excellence of \(X^\star\) contributes nothing to that direction.

## 3. Graded partial-result targets

**P1 - Reproduce a solved case end-to-end.** Re-prove \(N=13\) or \(N=14\) (or a smaller case) with our own toolchain: enumerate candidate contact graphs, interval-certify the elimination, and produce exact optimal coordinates.
*Certificate:* the complete candidate-graph list with an isomorph-free completeness argument, per-graph interval certificates, and exact \(X^\star\).

**P2 - Certified lower-bound witnesses for open \(N\).** For a band of open \(N\) (e.g. \(15\le N\le 20\)), certify the \(\psi\) value of best-known configurations, giving verified lower bounds \(\Theta_N\ge\psi(X)\).
*Certificate:* interval evaluation of the minimum angle at rigorously enclosed coordinates.

**P3 - Complete candidate-graph enumeration for one open \(N\).** For the target \(N\) (e.g. 15), produce the certified-complete list of contact graphs satisfying the necessary optimality conditions.
*Certificate:* enumeration replay plus an independent isomorph check (nauty/Traces).

**P4 - Eliminate a subset of candidate types.** For the target \(N\), interval-certify that a proper subset of candidate graphs cannot exceed the incumbent \(\psi(X^\star)\).
*Certificate:* per-graph interval infeasibility proofs.

**P5 - Close one open \(N\) (this is R1).** All candidate types resolved; unique optimum identified; \(\Theta_N\) certified.
*Certificate:* the union of P3 (completeness) and P4 (all-but-one eliminated) plus exact \(X^\star\).

**P6 - Structure / adjacency note.** Relate the certified \(N\) to kissing (06) and Thomson (50): record whether the Tammes optimum coincides with or differs from the Thomson (energy) optimum for that \(N\).
*Certificate:* exact/interval comparison of the two configurations and their separation values.

## 4. Known results and prior art

- **Origin.** Tammes (1930), from the distribution of pores on pollen grains.
- **Classically solved small \(N\).** \(N=3,4,6,12\) (regular figures, L. Fejes Tóth and earlier). **Schütte and van der Waerden (1951)** proved \(N=5,7,8,9\). **Danzer** (dissertation ~1963, published 1986) proved \(N=10,11\). These use spherical-geometry case analysis (verify attributions).
- **Computer-assisted modern cases.** **O. Musin and A. Tarasov** proved \(N=13\) (~2012) and \(N=14\) (~2015) via exhaustive enumeration of irreducible contact graphs plus rigorous (interval / linear-programming) elimination. **Robinson (1961)** established \(N=24\), the configuration related to the snub cube (verify).
- **Proven set.** Rigorously: \(N\le 14\) and \(N=24\). Everything else, from \(N=15\) up (except 24), is open (verify this exact list before starting - it is the crux of the target).
- **Difficulty scaling.** The number of irreducible contact graphs to analyze grows quickly with \(N\); \(N=13\) and \(N=14\) each required a substantial machine-assisted case analysis, which is why \(N=15\) is hard despite being the immediate next value (verify the case counts).
- **Uniqueness.** For several solved \(N\) the optimum is unique up to isometry; for others there are finitely many optima; whether the \(N=15\) optimum is unique is itself part of the open question (verify).
- **Best-known configurations.** For open \(N\), high-quality conjectural optima are tabulated (Sloane's spherical-codes tables; work of Hardin, Sloane, and others) but are *not* proofs. Kottwitz and others catalogued conjectured contact graphs.
- **Universal upper bounds.** L. Fejes Tóth's inequality bounds \(\Theta_N\) from above for all \(N\) (the "Fejes Tóth bound"), and the linear-programming bounds of Delsarte–Goethals–Seidel and Bachoc–Vallentin give further rigorous ceilings; these feed the elimination step (verify the exact statements).
- **Contact-graph catalogues.** Conjectured optimal contact graphs for open \(N\) have been catalogued (Kottwitz ~1991 and later web tabulations); useful as candidate targets but not as proofs (verify).
- **Adjacent.** Kissing number in \(\mathbb{R}^3\) (Tammes-type with a fixed cap radius; problem 06 is the \(\mathbb{R}^{11}\) sibling); the Thomson minimal-energy problem (problem 50) has near-but-not-identical optimizers.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the exact set of proven \(N\) (whether any case beyond \(\{2,\dots,14,24\}\) has since been closed), the precise Musin–Tarasov method and its published cases, and the current best-known configurations for the target \(N\).

## 5. Attack plan

**`[opt]` exploration (uncertified).** Multistart spherical optimization to recover the candidate optimum and read off its contact graph \(\Gamma\):

- maximize a smooth surrogate of \(\min_{i<j}\theta\) - a soft-min of angles, or the epigraph form maximizing \(t\) subject to \(\langle x_i,x_j\rangle\le\cos t\) under \(\lVert x_i\rVert=1\);
- solve via projected gradient / SLSQP / a Riemannian optimizer (Julia `Manopt`, or C++);
- run many random restarts, since spurious local optima are common on the sphere;
- cross-check the recovered separation against the best-known tabulated value for the target \(N\).

**`[cert]` Musin–Tarasov pipeline (primary).**

- *Enumerate candidate contact graphs.* Using the necessary conditions for an irreducible optimum (planarity on the sphere, minimum-degree bounds, edge/face counts from Euler's formula, no "flexible" vertices), generate all combinatorial types for the target \(N\); reject isomorphs with **nauty/Traces**; keep an explicit completeness argument.
- *Gauge fixing.* Before any interval work, remove the \(O(3)\) freedom (pin one vertex to the north pole and fix one adjacent great-circle direction) so the constraint systems are locally rigid and interval-Newton can certify isolated solutions.
- *Certify each type.* For each graph, set up the system \(\langle x_i,x_j\rangle=\cos\psi\) on edges, \(\langle x_i,x_j\rangle\le\cos\psi\) elsewhere, \(\lVert x_i\rVert=1\); use **interval arithmetic** (Arb/FLINT, **kv**, or **CAPD**) with interval-Newton / Krawczyk and branch-and-bound to certify either infeasibility for \(\psi>\psi^\star\) or an upper bound \(\le\psi^\star\).
- *Pre-prune.* SDP/LP relaxations (Bachoc–Vallentin-style linear-programming bounds) can eliminate types before the interval step.
- *Identify the optimum.* The unique surviving type gives \(X^\star\); solve its polynomial system symbolically (**SageMath** / `Singular` resultants or Gröbner) for algebraic coordinates, then interval-verify global optimality.

**One-workstation scope.** \(N=15\) is the natural first open target: the contact-graph enumeration is finite and modest, and the per-graph interval certification is workstation-feasible. Larger \(N\) grows the enumeration combinatorially and is likely out of reach; state the reached \(N\) honestly.

**First-session checklist (concrete).**

1. Recover the conjectured \(N=15\) optimum by Riemannian multistart; read off and record its contact graph \(\Gamma\).
2. Re-run the contact-graph enumeration and interval elimination for \(N=13\) as a pipeline test against the published result (P1).
3. Interval-certify the \(\psi\) value of the best-known \(N=15\) configuration as a lower bound \(\Theta_{15}\ge\psi(X)\) (P2).
4. Enumerate the candidate contact graphs for \(N=15\) with isomorph rejection and record the completeness argument (P3).
5. Interval-certify the first batch of eliminations, pre-pruned by the LP bound (P4).

**Failure modes.**

- Incomplete graph enumeration - the fatal error; the completeness / isomorph-free argument must itself be verified.
- Interval branch-and-bound non-termination on a near-degenerate type (flat directions from continuous symmetries or floppy modes) - mitigate by fixing gauge and detecting infinitesimal flexes.
- Rationalizing a float optimum to a configuration that is not the true maximizer.
- Confusing chordal and geodesic values in reported numbers.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Optimal coordinates are algebraic numbers or certified interval enclosures; the minimum angle at any witness is evaluated in interval arithmetic with directed rounding. Every elimination of a candidate contact graph is an interval certificate (or an exact LP/SDP dual). Floating point is exploration only.
2. **Independent verification.** A standalone checker, independent of the search: (a) re-reads \(X^\star\), recomputes all pairwise angles, and confirms \(\psi(X^\star)\); (b) replays the contact-graph enumeration and re-checks isomorph-free completeness with an independent nauty run; (c) re-verifies each per-graph interval certificate, ideally with a second interval library. Exact optimal coordinates are re-derived by a second CAS.
3. **Reproducibility.** Enumeration parameters, the necessary-condition set used, interval tolerances, solver/library versions, seeds, and coordinates are recorded; a SHA-256 manifest over graph lists, certificate files, coordinate data, and logs.
4. **Preservation.** The optimizer, the contact-graph generator, the interval-certification code, and the symbolic solver scripts are all part of the record; anything not preserved is stated (the Hadamard-668 lost-source lesson). A `NEXT_STEPS.md` records which candidate types remain if \(N\) is not closed (the Moore-57 pattern).
5. **Honest reporting.** The report states up front whether \(\Theta_N\) was *proved* for an open \(N\), or whether the result is a certified lower-bound witness, a complete candidate enumeration, or a partial elimination. A numerically excellent configuration is never presented as an optimality proof; the proven-versus-conjectured status and the metric (geodesic vs chordal) of every quoted value are stated explicitly.
