# PROMPT FOR A CERTIFIED OPTIMAL PACKING OF N CIRCLES IN A SQUARE

## Spreading N points in the unit square to maximize the minimum pairwise distance

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 26 of 50  
**Area:** discrete geometry  
**Modes:** `[opt]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Pack \(N\) equal circles into a unit square as tightly as possible - equivalently, spread \(N\) points to maximize the smallest pairwise distance. Best-known configurations are tabulated into the hundreds, but *proven* optimality is known for only a small set of \(N\), with gaps. The proofs are computer-assisted: interval-arithmetic branch-and-bound over the point configuration space, exactly the certified global optimization at which AI-assisted methods excel (Markót–Csendes proved \(N=28,29,30\) this way). This is the planar sibling of the Tammes problem (24) and shares the packing character of kissing (06) and Kelvin (11). The resolution standard is a *certified* optimality proof for a currently-open \(N\), or a certified improved bound. A configuration with a record minimum distance, however finely tuned, is a *lower-bound witness* only - never, by itself, a proof of optimality.

## 1. Exact problem statement

Fix the closed unit square \(Q=[0,1]^2\). For \(P=(p_1,\dots,p_N)\in Q^N\) define the **separation**

\[
s(P)=\min_{1\le i<j\le N}\lVert p_i-p_j\rVert_2,
\qquad
d_N=\max_{P\in Q^N} s(P).
\]

The maximum is attained (compact domain, continuous objective); an **optimal spreading** exists. Optima are determined up to the dihedral symmetry \(D_4\) of the square and relabeling \(S_N\); the reduced space is \(Q^N/(D_4\times S_N)\).

**Equivalent circle-packing normalization.** Packing \(N\) non-overlapping equal circles of radius \(r\) inside \(Q\) (centers in \([r,1-r]^2\), pairwise center distance \(\ge 2r\)) is equivalent to the point problem by an affine rescaling of the inner square. The maximal radius \(r_N\) satisfies

\[
r_N=\frac{d_N}{2\,(1+d_N)},\qquad\text{equivalently}\qquad d_N=\frac{2r_N}{1-2r_N}.
\]

Conventions fixed once here:

- We adopt the **point / max-min-distance** formulation as primary and report \(r_N\) via the identity above.
- A third common convention packs \(N\) unit circles into the smallest square; it is the same problem rescaled.
- Euclidean distance; unit square domain \(Q=[0,1]^2\).
- Collinear / boundary degeneracies are allowed - optima frequently place points on the boundary and edges.
- The three normalizations (point separation \(d_N\), in-square radius \(r_N\), unit-circle square side) each appear in the literature; every reported number must name its normalization to avoid silent factor-of-two or offset errors.

Degeneracies and well-posedness:

- The optimum has \(d_N>0\) for all \(N\); coincident points force \(s(P)=0\) and are excluded.
- Optima are frequently *not unique* and often have "rattlers" - points free to move without lowering \(s(P)\) - which create continuous families and flat directions the certification must handle (fix them by pinning or by treating the rattler's admissible region explicitly).
- Points on the boundary and at corners are common in optima and are fully admissible.

"Open \(N\)" means an \(N\) for which \(d_N\) is not yet *proven* (as opposed to conjectured from best-known configurations - section 4). No informal target ("a very good packing") is acceptable; the deliverable is a proof per section 2.

## 2. Resolution standard

**(R1) Certified optimum at an open \(N\).** For a named currently-open \(N\), an explicit configuration \(P^\star\) (algebraic coordinates or certified interval enclosures) and a *certified proof* that \(d_N=s(P^\star)\). The hard direction is the uniform upper bound \(d_N\le s(P^\star)\). Accepted certified form: an **interval-arithmetic global-optimization proof** -

- a branch-and-bound over \(Q^N/\text{sym}\) whose every discarded box carries a directed-rounding interval certificate that \(s(P)\le s(P^\star)\) on that box (or that the box is infeasible);
- the boxes provably tiling the reduced domain, the whole cover machine-checkable;
- interval-Newton / Krawczyk certification of the finitely many critical configurations near the optimum.

Equivalently, an exact KKT + resultant classification with interval-verified global comparison.

The proof therefore has two halves that must both be delivered:

- a **lower half** - the witness \(P^\star\) with its exactly-evaluated separation \(s(P^\star)\), giving \(d_N\ge s(P^\star)\);
- an **upper half** - the certified branch-and-bound giving \(d_N\le s(P^\star)\); this is the hard, universally-quantified direction, and its absence reduces the claim to a lower bound.

**(R2) Certified improved bound.** For an open \(N\), a rigorous upper bound \(d_N\le U\) (certified branch-and-bound bracketing) strictly better than any previously certified, and/or a certified lower bound \(d_N\ge L\) from an exactly-evaluated configuration. A narrowed certified interval \([L,U]\) around \(d_N\) is a genuine result.

**Not accepted as resolution.**

- A configuration with a record \(s(P)\) and no upper-bound proof - a *lower-bound witness*, not a determination of \(d_N\).
- Output of a floating-point optimizer (billiard/pushing algorithms, simulated annealing) presented as optimal; these do not certify the universal upper bound.
- Matching a best-known value from Packomania / Nurmela–Östergård tables to more digits.
- A branch-and-bound whose box cover is not proved to tile the domain, or whose interval bounds use non-directed rounding.
- Optimality asserted from an unbroken local-optimality / rigidity check on one configuration.

Stress: for a geometric optimum the difficulty is entirely the universally-quantified upper bound over an uncountable domain. A numerically excellent packing proves only a lower bound.

## 3. Graded partial-result targets

**P1 - Reproduce a certified case.** Re-prove optimality for a small already-proven \(N\) (e.g. \(N\le 9\), or a Markót–Csendes case \(N\in\{28,29,30\}\)) with our own interval branch-and-bound.
*Certificate:* the box cover with per-box interval bounds and a tiling argument, replayable independently, plus exact \(P^\star\).

**P2 - Certified best-known values, exactly.** For a band of open \(N\), certify the \(s(P)\) of the best publicly tabulated configurations, yielding verified lower bounds \(d_N\ge s(P)\) and the corresponding \(r_N\).
*Certificate:* exact/interval evaluation of the minimum pairwise distance at rationalized coordinates.

**P3 - Improve a lower bound for one open \(N\).** A configuration with certified \(s(P)\) strictly above the best recorded value for some open \(N\).
*Certificate:* exact minimum distance beating the record, plus the search log.

**P4 - Certified upper bound for one open \(N\).** Bracket \(d_N\) from above by a rigorous branch-and-bound, narrowing \([L,U]\) even without closure.
*Certificate:* the interval box cover with the stated gap.

**P5 - Close one open \(N\) (this is R1).** P3 and P4 matched to a certified proof \(d_N=s(P^\star)\).
*Certificate:* the combined witness and cover meeting at \(s(P^\star)\).

**P6 - Sibling comparison.** For a certified \(N\), record the relationship to the Tammes optimum (24) at the same \(N\) (planar-square vs spherical domain) and the shared packing character with kissing (06) / Kelvin (11).
*Certificate:* exact/interval comparison of the separation values.

## 4. Known results and prior art

- **Formulations.** The point max-min-distance problem, the equal-circle-in-square packing, and the "unit circles in smallest square" problem are equivalent by rescaling.
- **Early exact results.** Small cases were settled by hand / geometry: **Schaer** and **Schaer–Meir** (1960s) for the first several \(N\); optimality is classically established for small \(N\) (roughly \(N\le 9\); verify the exact list).
- **Perfect-square cases.** For some square \(N=k^2\) the \(k\times k\) grid is optimal and for others it is not; the pattern is subtle and the proven cases must be checked individually (verify).
- **Rattler prevalence.** Many best-known packings contain rattlers, so the optimizer's raw output is often a continuum rather than a point; this must be resolved before an interval optimality proof can close (verify per \(N\)).
- **Best-known configurations.** Extensive tables of *best-known* (mostly conjectural) packings: **Graham and Lubachevsky** (1990s, "billiards" algorithm), **Nurmela and Östergård (1997)**, **Melissen** (thesis, 1997), **Peikert**, **de Groot–Peikert–Würtz**, and **E. Specht's Packomania** collection (into the hundreds). These are records, not proofs.
- **Certified optimality (the target's method).** **M. C. Markót and T. Csendes** (approximately 2005) used rigorous **interval-arithmetic** branch-and-bound to *prove* optimality for \(N=28,29,30\) (verify), extending earlier certified cases. This is the model the resolution standard adopts.
- **Global-optimization framing.** **Locatelli and Raber** (approximately 2002) and others formulated the packing as a rigorous global-optimization problem with convex relaxations and branch-and-bound; **Nurmela–Östergård** and **de Groot–Peikert–Würtz** contributed the computational best-known frontier. The rattler / continuous-family phenomenon complicates certification for larger \(N\) (verify attributions and dates).
- **Proven set.** Rigorously proven optimal \(d_N\) exists for small \(N\) plus scattered larger cases (including certain grid-like \(N\) and the interval-arithmetic cases); the exact proven set has gaps and must be confirmed before choosing an open \(N\) (verify).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the exact set of \(N\) with *proven* optimality (versus best-known), the current Packomania records for the target \(N\), and any interval-arithmetic optimality proofs published since Markót–Csendes, before claiming an increment.

## 5. Attack plan

**`[opt]` exploration (uncertified).** Recover candidate optima with the standard heuristics:

- Lubachevsky–Graham billiards / "pushing" dynamics;
- simulated annealing with restarts;
- multistart nonlinear optimization of the epigraph LP/SOCP - maximize \(t\) subject to \(\lVert p_i-p_j\rVert^2\ge t^2\), \(p_i\in Q\) - in Julia (JuMP) or C++;
- Locatelli–Raber-style convex relaxation to seed the branch-and-bound with a valid upper bound.

Read off the contact structure (which pairs and which boundary constraints are tight), and detect rattlers before certification so their flat directions can be handled explicitly.

**`[cert]` interval branch-and-bound (primary).**

- Certify optimality with an interval branch-and-bound over the reduced box \(Q^N/\text{sym}\), using **Arb/FLINT**, **kv**, or **CAPD**. Fix symmetry by ordering constraints (lexicographic point order, pin a point to a corner/edge orbit) to shrink the domain and kill the \(D_4\times S_N\) redundancy.
- Each box: compute an interval upper bound on \(s(P)\); discard if below the incumbent \(s(P^\star)\); otherwise subdivide. Near the optimum, apply an interval-Newton / Krawczyk test to the KKT system (stationarity of \(t\) with active distance and boundary constraints) to certify a unique critical configuration per remaining cell.
- Exact optimal coordinates via symbolic solution of the active-constraint polynomial system (**SageMath** / `Singular`), then interval-verified as the global maximum.

**One-workstation scope.** The box dimension is \(2N\) and the constraint count \(\binom{N}{2}\) plus boundary; certified proofs are workstation-feasible up to a moderate \(N\) (the published interval frontier is around \(N=30\)). Target one open \(N\) near or just past that frontier, or a smaller stubborn open case. State the reached \(N\) honestly; a bracketing interval (P4) is the honest fallback.

**First-session checklist (concrete).**

1. Recover the \(N\le 9\) optima by billiards / multistart; exact-check all pairwise distances and confirm known \(d_N\).
2. Re-certify one small already-proven case via the interval branch-and-bound as a pipeline test (P1).
3. Certify the best-known \(s(P)\) for a band of open \(N\) as lower bounds \(d_N\ge s(P)\), reporting \(r_N\) via the identity (P2).
4. Fix one open \(N\) near the interval frontier; run the search to a lower-bound witness (P3) and read off the contact structure.
5. Begin the interval cover for that \(N\) with symmetry fixed, reporting the first bracketing interval \([L,U]\) (P4).

**Failure modes.**

- Branch-and-bound blow-up - report a certified bracketing interval, not a claimed optimum.
- Incorrect symmetry reduction that fails to cover an orbit, invalidating the tiling - the cover-completeness argument must be checked.
- Non-directed rounding silently invalidating interval bounds.
- Rationalizing a float optimum to a nearby non-optimal configuration; the exact upper-bound proof, not the rationalization, certifies.
- Confusing the point-distance value \(d_N\) with the circle radius \(r_N\) (use the identity).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All pairwise distances at witness configurations are evaluated exactly (rational/algebraic) or in interval arithmetic; every optimality or bracketing claim rests on interval arithmetic with directed rounding (Arb/kv/CAPD). The branch-and-bound cover is emitted as a machine-readable list of boxes with per-box interval bounds. Floating point is exploration only.
2. **Independent verification.** A standalone checker, independent of the search: (a) recomputes all \(\binom{N}{2}\) distances at each witness to confirm \(s(P)\) and \(r_N\); (b) replays the interval box cover, re-deriving each box bound and confirming the boxes tile the reduced domain. A second interval library reproduces the leaf bounds where feasible.
3. **Reproducibility.** Seeds, solver and interval-library versions, subdivision tolerances, symmetry-reduction constraints, and coordinates (as exact algebraic data) are recorded; a SHA-256 manifest over witness files, box lists, logs, and checker output.
4. **Preservation.** The heuristic packing code, the interval branch-and-bound code, and the symbolic active-set scripts are all part of the record; anything not preserved is stated (the Hadamard-668 lost-source lesson). A `NEXT_STEPS.md` records the current certified \([L,U]\) for the target \(N\) if not closed (the Moore-57 pattern).
5. **Honest reporting.** The report states up front whether \(d_N\) was *proved* for an open \(N\), or whether the result is a certified lower-bound witness, a certified bracketing interval, or a certified value-check of best-known data. A record-setting packing is never presented as an optimality proof; the proven-versus-conjectured status and the normalization (point distance \(d_N\) vs radius \(r_N\)) of every quoted value are stated explicitly.
