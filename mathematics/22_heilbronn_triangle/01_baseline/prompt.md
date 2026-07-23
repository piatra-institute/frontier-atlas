# PROMPT FOR A CERTIFIED HEILBRONN OPTIMUM OR A RIGOROUS BOUND IMPROVEMENT

## The Heilbronn triangle problem: maximizing the smallest triangle among \(n\) points in the unit square

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 22 of 50  
**Area:** discrete geometry  
**Modes:** `[opt]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Given \(n\) points in the unit square, the Heilbronn function \(H(n)\) is the largest possible value of the smallest triangle area over all placements. It is a canonical extremal-geometry quantity: a compact global-optimization problem over a fixed-dimensional configuration space, with a proven exact answer for only the smallest \(n\) and asymptotics that were still moving in 2023. This matches AI-assisted work in two disjoint modes: certified global optimization (an interval-arithmetic branch-and-bound that either proves a specific configuration optimal or brackets \(H(n)\) rigorously) and analytic bound improvement (a machine-mined, then hand-certified, packing/incidence argument). The resolution standard in section 2 is a *proof* - an optimality certificate for a named \(n\), or an inequality with a checkable derivation. A configuration with a good objective value, however carefully polished, is never by itself a resolution and is reported as a lower-bound witness only.

## 1. Exact problem statement

Fix the closed unit square \(Q=[0,1]^2\) with Lebesgue area normalized so \(\operatorname{area}(Q)=1\). A *configuration* is an ordered tuple \(P=(p_1,\dots,p_n)\in Q^n\), with \(p_i=(x_i,y_i)\). For an unordered triple \(\{i,j,k\}\) the triangle area is

\[
A_{ijk}(P)=\tfrac12\,\bigl|\det(p_j-p_i,\;p_k-p_i)\bigr|
=\tfrac12\,\bigl|(x_j-x_i)(y_k-y_i)-(x_k-x_i)(y_j-y_i)\bigr|.
\]

Define the *dispersion objective* and the Heilbronn function

\[
h(P)=\min_{1\le i<j<k\le n} A_{ijk}(P),
\qquad
H(n)=\max_{P\in Q^n} h(P).
\]

The configuration space \(Q^n\) is compact and \(P\mapsto h(P)\) is continuous (a minimum of finitely many continuous functions), so the maximum is attained: an *optimal configuration* exists for every \(n\ge 3\). It is generally not unique.

Symmetries and the reduced configuration space:

- The dihedral group \(D_4\) of the square (order 8) acts by isometries preserving \(h\).
- The symmetric group \(S_n\) acts by relabeling the points.
- The reduced search domain is \(Q^n/(D_4\times S_n)\); results are stated up to this action.

Adopted normalizations and scope, fixed once here:

- **Domain.** The unit *square*. The unit disk, the unit-area equilateral triangle, and the flat torus are inequivalent domains that change the constant (and, for the torus, the extremal structure). Every result must name the domain.
- **Areas.** Absolute (unsigned) areas; the determinant sign is handled by \(|\cdot|\) or by explicit orientation branches in an optimizer.
- **Primary object.** We work with \(H(n)\) itself, not the rescaled asymptotic quantity \(n^2 H(n)\); the latter is derived, not primary.

Degeneracies and well-posedness:

- A configuration with three collinear points has \(h(P)=0\); such configurations are never optimal for \(n\ge 3\), since any optimum has \(H(n)>0\) (a positive lower bound is achievable, e.g. by a grid or random placement).
- Coincident points are excluded implicitly (they force \(h=0\)); optimizers should nonetheless guard against near-coincidence.
- Attainment follows from compactness of \(Q^n\) and continuity of \(h\); there is no supremum-not-maximum subtlety.

Two questions are in scope; a session should commit to one:

1. **Small-\(n\) exact value.** Determine \(H(n)\) for a specific currently-open \(n\), together with the optimal configuration(s).
2. **Asymptotics.** Improve a rigorous upper or lower bound on \(H(n)\) as \(n\to\infty\).

No informal target ("a near-optimal placement", "essentially tight") is acceptable. The deliverable is a proof of one of the statements in section 2.

## 2. Resolution standard

A complete resolution is one of the following, in certified form.

**(R1) Exact small-\(n\) optimum.** For a named currently-open \(n\), a rational or algebraic configuration \(P^\star\) and a *certified proof* that \(H(n)=h(P^\star)\). The proof must establish the upper bound \(H(n)\le h(P^\star)\) rigorously - the hard direction. Accepted certified form: an **interval-arithmetic global-optimization proof** - a branch-and-bound over \(Q^n/\text{sym}\) whose leaves each carry a directed-rounding interval certificate that \(h(P)<h(P^\star)+\epsilon\) throughout the cell, with a machine-checkable exhaustive-cover argument. Equivalently, an exact semidefinite/Positivstellensatz certificate, or a symbolic KKT + resultant classification of critical configurations with interval-verified global comparison.

**(R2) Rigorous asymptotic bound.** An inequality of the form \(H(n)\le C\,n^{-8/7-\delta}\) or \(H(n)\ge c\,n^{-2}\log n\) (or better) that strictly improves the current record, with a fully written proof whose finite computational inputs, if any, are certified (exact or interval).

**Not accepted as resolution.**

- A configuration with a high objective value and no upper-bound proof - this is a *lower-bound witness*, never a determination of \(H(n)\).
- A floating-point local (or "global") optimizer output, however converged; nonlinear solvers do not certify global optimality.
- Matching a tabulated conjectural optimum (Goldberg/Yang-type tables) to more digits.
- An asymptotic bound proved only "up to constants believed to hold" or resting on an un-certified numerical lemma.
- A single symmetric candidate shown to be a local maximum.

State explicitly that for a geometric optimum, *numerical quality is not proof*: the entire difficulty is the universally-quantified upper bound over an uncountable domain.

## 3. Graded partial-result targets

Ordered milestones, each with its own certificate standard.

**P1 - Reproduce the certified frontier.** Re-derive, with our own interval toolchain, a rigorous optimality proof for a small already-solved \(n\) (e.g. \(n\in\{5,6,7\}\)).
*Certificate:* the branch-and-bound cover with per-leaf interval bounds, replayable by an independent checker, plus exact optimal coordinates as algebraic numbers.

**P2 - Best-known lower-bound witnesses, exactly.** For a band of open \(n\), certify the value \(h(P)\) of the best publicly tabulated configurations, giving verified lower bounds on \(H(n)\).
*Certificate:* exact evaluation of all \(\binom{n}{3}\) areas at the given (rationalized) coordinates.

**P3 - Improve a lower bound for one open \(n\).** A configuration with strictly larger certified \(h(P)\) than the best recorded value for some open \(n\), via global-optimization search then exact rationalization.
*Certificate:* exact \(\min\) area beating the record, plus the search log.

**P4 - Certified upper bound for one open \(n\).** Bracket \(H(n)\) from above by a rigorous branch-and-bound, narrowing the interval \([\,\underline H,\overline H\,]\) around \(H(n)\) even if not to closure.
*Certificate:* interval cover of \(Q^n/\text{sym}\) with a stated gap.

**P5 - Close one open \(n\) (this is R1).** Match P3 and P4 to a proof \(H(n)=h(P^\star)\).
*Certificate:* the combined lower witness and upper cover meeting at \(h(P^\star)\).

**P6 - Structure mining for asymptotics.** From certified small-\(n\) optima, extract and state a precise conjecture on extremal structure (boundary incidence, near-collinear triples).
*Certificate:* the data set of certified optima and the explicit conjecture derived from it.

**P7 - Rigorous asymptotic increment (this is R2).** A written, certificate-backed improvement to an upper or lower asymptotic bound.
*Certificate:* the full proof plus any exact/interval finite lemma it depends on.

## 4. Known results and prior art

- **Definition and first bounds.** Heilbronn asked (1940s) whether \(H(n)=O(1/n^{2})\). **Roth (1951)** gave the first nontrivial upper bound \(H(n)=O\!\bigl(n^{-1}(\log\log n)^{-1/2}\bigr)\) (verify), later improved by Roth and by **W. M. Schmidt (1972)**; the long-standing upper record was of order \(n^{-8/7-\epsilon}\)-type (verify the exponent).
- **Lower bound.** **Komlós, Pintz, and Szemerédi (1982)** proved \(H(n)=\Omega(\log n / n^{2})\), disproving Heilbronn's original \(\Theta(1/n^2)\) guess. This remained the best lower bound for decades (verify current status; there has been recent activity).
- **Recent upper bound.** **A. Cohen, C. Pohoata, and D. Zakharov (2023)** improved the upper bound below the Roth–Schmidt exponent (a gain of order \(n^{-1/2000}\)-scale in the exponent) (verify the precise statement and any 2024–2025 follow-ups on either side).
- **Small-\(n\) data.** **M. Goldberg (1972)** initiated the tabulation of optimal/near-optimal square configurations; later work by **Yang, Graham, Dress**, and others (approximately 1990s–2000s) extended conjectural optima to roughly \(n\le 16\) (verify how many are *proved* optimal versus best-known). Rigorous optimality proofs hold only for small \(n\); the exact frontier of *proven* values must be confirmed (verify - it is smaller than the tabulated frontier).
- **Structural observations.** For small \(n\), conjectured optima tend to place many points on the boundary of \(Q\) and to have several triples simultaneously attaining the minimum area (a rigidity typical of extremal packings); Yang, Dress, and collaborators tabulated the tight-triple structure (verify).
- **Domain variants.** Parallel tables exist for the disk and the unit-area triangle (Yang and others); analogous quantities are studied on the flat torus, where the extremal structure differs. Constants differ; asymptotics agree in order.
- **Related dispersion quantities.** The Heilbronn problem sits in a family with the "spreading points" / minimum-distance problem (problem 26) and higher-dimensional simplex-volume analogues; methods transfer but constants and extremal types do not.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** The upper-bound exponent moved in 2023 and the area is active; confirm the exact current upper and lower asymptotic records, and the precise set of \(n\) for which \(H(n)\) is *proven* (not merely conjectured), before claiming any increment.

## 5. Attack plan

**`[opt]` certified small-\(n\) (primary).**

- *Exploration (float, uncertified).* Multistart nonlinear optimization of \(h(P)\) via a smooth-max surrogate or the epigraph formulation - maximize \(t\) subject to \(A_{ijk}\ge t\) with sign branches on the determinants - in Julia (JuMP + Ipopt) or C++. Purpose: find candidate optima and their combinatorial type (which triples are tight).
- *Certification (rigorous).* Interval branch-and-bound over the reduced box \(Q^n/\text{sym}\), using **Arb/FLINT** or **kv**/**CAPD** interval arithmetic. Fix symmetry by ordering constraints (lexicographic point order, one point pinned to a corner/edge orbit) to shrink the domain. Each box is either discarded (interval upper bound on \(h\) below the incumbent) or subdivided; near the optimum, an interval Newton / Krawczyk test on the KKT system certifies a unique critical configuration per cell.
- *Exact coordinates.* Solve the tight-triple polynomial system symbolically (SageMath / `Singular`) for algebraic optimal coordinates, then interval-verify them as the global maximum.
- *Feasible scale.* One workstation realistically reaches certified proofs only for small \(n\); the box dimension \(2n\) and the \(\binom{n}{3}\) constraints make the branch-and-bound cost grow steeply. State the reached \(n\) honestly.

**`[opt]` cheap upper bounds.** Before the full branch-and-bound, obtain a rigorous (if weak) upper bound on \(H(n)\) from a relaxation - e.g. a covering / pigeonhole argument on a fixed sub-partition of \(Q\), or the epigraph SOCP dual - to bracket the target and prune the search. These are certified inputs, not resolutions.

**`[search]` records.** Global optimizers (simulated annealing, CMA-ES, then local polish) to push lower-bound witnesses for open \(n\); rationalize coordinates and certify the exact \(\min\) area. This is P3, not a resolution.

**`[opt]` asymptotic.** Reproduce the Komlós–Pintz–Szemerédi lower-bound argument and the Cohen–Pohoata–Zakharov upper-bound argument on paper; identify the certified-finite lemma (an incidence or packing count) where a machine search could tighten a constant, then attempt that single increment with an exact/interval certificate.

**First-session checklist (concrete).**

1. Multistart-optimize \(h(P)\) for \(n=6\) (float); read off the tight-triple graph of the candidate optimum.
2. Stand up the interval branch-and-bound and re-certify \(n=5\) end-to-end as a pipeline test.
3. Rationalize the \(n=6\) optimum and exact-check all \(\binom{6}{3}=20\) areas.
4. Fix the target open \(n\); run the global optimizer to a lower-bound witness and rationalize it (P3).
5. Begin the interval cover for that \(n\), reporting the first bracketing interval \([\underline H,\overline H\,]\) (P4).

**Failure modes.**

- Branch-and-bound blow-up - the honest outcome is a bracketing interval (P4), reported as such.
- Symmetry mishandling that double-counts or misses an orbit, invalidating the cover - the isomorph/orbit argument must itself be checked.
- Rationalizing a float optimum to a nearby configuration that is *not* optimal - the exact upper-bound proof, not the rationalization, is what certifies.
- Confusing a domain variant's constant with the square's.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All triangle areas at witness configurations are evaluated in exact rational/algebraic arithmetic. Every optimality or bracketing claim rests on interval arithmetic with directed rounding (Arb/kv/CAPD). The branch-and-bound cover is emitted as a machine-readable list of boxes with per-box interval bounds. Floating point is exploration only.
2. **Independent verification.** A standalone checker, written separately from the search, (a) re-evaluates all \(\binom{n}{3}\) areas at each witness to confirm the claimed \(h(P)\), and (b) replays the interval cover, re-deriving each box's bound and confirming the boxes tile the reduced domain. Where feasible a second interval library reproduces the leaf bounds.
3. **Reproducibility.** All seeds, solver versions, subdivision tolerances, symmetry-reduction constraints, and coordinates (as exact algebraic data) are recorded; a SHA-256 manifest covers every artifact (witness files, box lists, logs, checker output).
4. **Preservation.** The global-optimization search code, the interval branch-and-bound code, and the symbolic critical-point scripts are all part of the record. Anything not preserved is stated plainly (the Hadamard-668 lost-source lesson). A `NEXT_STEPS.md` records the current certified \([\underline H,\overline H\,]\) for the target \(n\) if not closed (the Moore-57 pattern).
5. **Honest reporting.** The report states up front whether an exact \(H(n)\) was *proved*, or whether the result is a certified lower-bound witness, a certified bracketing interval, or an asymptotic increment. A numerically excellent configuration is never presented as determining \(H(n)\); the domain (square) and the proved-versus-conjectured status of every quoted value are stated explicitly.
