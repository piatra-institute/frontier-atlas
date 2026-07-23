# PROMPT FOR CERTIFIED NO-THREE-IN-LINE RECORDS ON THE GRID

## The maximum number of grid points with no three collinear

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 27 of 50  
**Area:** discrete geometry  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

How many points can be placed on an \(n\times n\) integer grid with no three on a common line? At most \(2n\) (two per row), and \(2n\)-point configurations are known for \(n\) up to the mid-40s - but whether \(2n\) is always achievable, and what the true maximum is for large \(n\), are open. This is the cleanest finite-search problem in the discrete-geometry pack: collinearity is exact integer arithmetic, so the ground truth is machine-checkable and the objects are directly SAT/CP-encodable. The `[search]` deliverable is certified: a maximal (\(2n\)-point) configuration for an open \(n\), an exhaustive-search record (the exact maximum, or the exact count, for a new \(n\)), or a certified proof that no \(2n\)-point set exists for a specific \(n\). A good-looking configuration is worthless without either an exact optimality proof (exhaustive search / SAT UNSAT of the "one more point" instance) or, for a record, a certified exhaustive count.

## 1. Exact problem statement

Fix the grid \(G_n=\{0,1,\dots,n-1\}^2\subset\mathbb{Z}^2\), \(|G_n|=n^2\). A set \(S\subseteq G_n\) is **in general position** (no-three-in-line) if no line of the plane contains three distinct points of \(S\); equivalently, for all distinct \(a,b,c\in S\),

\[
(b-a)\times(c-a)\;=\;(b_x-a_x)(c_y-a_y)-(b_y-a_y)(c_x-a_x)\;\ne\;0 .
\]

This is an *exact* integer condition. Define the **no-three-in-line number**

\[
\tau(n)=\max\{\,|S| : S\subseteq G_n\text{ in general position}\,\}.
\]

Trivial bounds and the central question:

- Each row contains at most \(2\) points of \(S\) (three in a row are collinear), so \(\tau(n)\le 2n\); likewise for columns.
- The central existence question is: for which \(n\) is \(\tau(n)=2n\)?

Adopted conventions:

- Grid \(\{0,\dots,n-1\}^2\) (equivalently \(\{1,\dots,n\}^2\)).
- Lines are all lines of \(\mathbb{R}^2\), not just grid-aligned ones - the cross-product test captures every line, including diagonals of every rational slope.
- The dihedral group \(D_4\) of the square acts on \(G_n\); optima and counts are considered up to this action where stated.
- The cross-product test is slope-agnostic: it captures axis-aligned, diagonal, and arbitrary rational-slope lines uniformly, with no special-casing.
- The count \(\binom{n^2}{k}\) of candidate \(k\)-subsets is astronomical; the practical objects are SAT models and isomorph-free generators, never brute subset enumeration.
- "Open \(n\)" means an \(n\) for which \(\tau(n)\) is not yet determined by exhaustive search, or for which \(2n\)-point existence is unknown.

Two distinct frontiers, not to be conflated:

- The **\(2n\)-existence frontier** - the largest \(n\) for which some \(2n\)-point general-position set is *known* - advances by explicit construction and is far ahead.
- The **exhaustive-\(\tau\) frontier** - the largest \(n\) for which \(\tau(n)\) is *proven* (by complete search) - is much smaller, because proving \(\tau(n)<2n\) or enumerating all solutions is expensive.

No informal target is acceptable; deliverables are the certified statements of section 2.

## 2. Resolution standard

**(R1) Certified maximal configuration at an open \(n\).** For a named \(n\) currently lacking one, either

- (a) an explicit \(2n\)-point set \(S\subseteq G_n\) in general position (which, with \(\tau(n)\le 2n\), certifies \(\tau(n)=2n\)), or
- (b) a certified proof that no \(2n\)-point set exists together with the exact value \(\tau(n)=2n-k\).

Accepted certified form: for existence, an **exact-arithmetic verification** that all \(\binom{|S|}{3}\) triples are non-collinear; for nonexistence and for exact \(\tau(n)\), an **exhaustive search** - an isomorph-free enumeration, or a **SAT/CP proof** with a DRAT/LRAT-checked UNSAT certificate for the "\(m\) points exist" instance at \(m=\tau(n)+1\).

**(R2) Exhaustive-search record.** For a named \(n\) beyond the current exhaustive frontier, the exact value \(\tau(n)\), or the exact *number* of maximal configurations (up to \(D_4\)), established by a complete search. Certified form: a replayable exhaustive enumeration with isomorph rejection, or a model-counting / exhaustive-SAT certificate.

**Not accepted as resolution.**

- A \(2n\)-point configuration whose non-collinearity is only checked in floating point or only for grid-aligned lines - every triple must pass the exact integer cross-product test.
- A claim \(\tau(n)<2n\) resting on a heuristic search's failure to find \(2n\) points; a nonexistence claim requires an exhaustive / SAT-UNSAT proof.
- Matching a known record (reproducing a tabulated \(2n\)-set for an already-solved \(n\)) presented as new.
- An exhaustive count with no isomorph-free completeness argument or no independent replay.
- An asymptotic constant "confirmed" numerically without proof (the Guy–Kelly constant is a conjecture, not a certifiable target here).

Stress: existence of a good configuration is easy to *verify* but a *maximum* or a *nonexistence* is a universally-quantified statement requiring exhaustiveness. The certificate - exact triple-check plus, for optimality, a machine-checkable UNSAT / enumeration - is the entire content.

## 3. Graded partial-result targets

**P1 - Reproduce the exhaustive frontier.** Re-derive \(\tau(n)\) and exact solution counts for small \(n\) (up to the current exhaustive limit) with our own isomorph-free search and an independent SAT encoding; confirm agreement with tabulated values (OEIS).
*Certificate:* enumeration replay plus DRAT for the \(m=\tau(n)+1\) UNSAT instance.

**P2 - Certified \(2n\)-sets across a band.** For a band of \(n\) up to and past the recorded existence frontier, produce and exactly certify \(2n\)-point general-position sets.
*Certificate:* exact triple-check over all \(\binom{2n}{3}\) triples per configuration.

**P3 - Push the \(2n\)-existence frontier by one.** A certified \(2n\)-point set for an \(n\) beyond the largest previously recorded.
*Certificate:* exact triple-check; construction / search log preserved.

**P4 - Extend the exact-\(\tau(n)\) frontier by one (R2 for one \(n\)).** The exact maximum for a new \(n\) via exhaustive search with a DRAT-checked optimality certificate.
*Certificate:* SAT-UNSAT for \(m=\tau(n)+1\) plus a witness at \(m=\tau(n)\).

**P5 - Certified nonexistence of a \(2n\)-set (part of R1).** For a specific \(n\), a DRAT-checked proof that no \(2n\)-point general-position set exists, with the exact \(\tau(n)\).
*Certificate:* UNSAT proof for the \(2n\)-point instance plus a witness at \(\tau(n)\).

**P6 - Exact solution counts / structure mining.** For a new \(n\), the exact number of maximal solutions up to \(D_4\), and a structural note (symmetry classes, modular/parabola constructions) toward a precise conjecture.
*Certificate:* model-count with isomorph rejection, independently replayed.

**P7 - Independent cross-check of a published record.** Re-derive an existing \(2n\)-existence or exhaustive-\(\tau\) claim from scratch and confirm agreement (or flag a discrepancy).
*Certificate:* independent exact triple-check for existence, or independent DRAT replay for an optimality claim.

## 4. Known results and prior art

- **Origin and upper bound.** Dudeney posed the \(n=8\) case (1917); the row bound gives \(\tau(n)\le 2n\).
- **Constructions.** Erdős observed (via **Roth**, 1951) that points on a parabola modulo a prime \(p\) give \(\sim p\) points in general position on a \(p\times p\) grid, so \(\tau(n)\ge(1-o(1))n\). **Hall, Jackson, Sudbery, and Wild (1975)** gave modular-hyperbola constructions achieving \(\approx\tfrac{3}{2}n\) points for infinitely many \(n\) (verify the constant and range).
- **Full \(2n\) configurations.** Explicit \(2n\)-point solutions are known for all small \(n\); **A. Flammenkamp** (approximately 1992 and 1998) found \(2n\)-point solutions for \(n\) up to the mid-40s (commonly cited as \(n\le 46\); verify the exact upper \(n\) and any later extension) and computed solution counts.
- **Exhaustive data.** Exact values of \(\tau(n)\) and the number of solutions are tabulated for small \(n\) (OEIS **A000769** counts general-position placements of \(2n\) points; related sequences for \(\tau(n)\); verify the current exhaustive limit).
- **Asymptotics (conjectural).** **Guy and Kelly (1968)** conjectured that for large \(n\) one *cannot* place \(2n\) points and that \(\tau(n)\sim c\,n\) with \(c=(2\pi^2/3)^{1/3}\approx 1.874\) (later commentary revised the heuristic; verify). This is a conjecture, not settled, and is *not* a certifiable target - it frames the significance of the finite records.
- **Symmetric solutions.** Many \(2n\)-point solutions carry nontrivial symmetry (central or dihedral); symmetry-restricted searches find constructions faster but must not be mistaken for exhaustive results. Symmetric-solution counts are tabulated separately in OEIS (verify the sequence numbers).
- **No known gap below the frontier.** For every \(n\) up to the recorded frontier a \(2n\)-point solution is known, so no failure of \(2n\)-achievability has yet been observed; whether \(2n\) holds for *all* \(n\) in that range is nonetheless not a closed theorem (verify).
- **SAT/CP records.** Modern exhaustive and record work uses SAT and constraint solvers; confirm the current computational frontier and whether any DRAT-certified optimality/nonexistence results have been published (verify).
- **Related.** The general-position and "no-\(\ell\)-in-line" variants, and cap-set-style density questions (adjacent to problem 17).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the current largest \(n\) with a known \(2n\)-point solution, the largest \(n\) with exhaustively-determined \(\tau(n)\), the relevant OEIS values, and any recent SAT-based records before claiming an increment.

## 5. Attack plan

**`[search]` SAT/CP (primary, for records and nonexistence).**

- *Encoding - variables.* A Boolean variable \(x_{ij}\) for "grid point \((i,j)\in S\)".
- *Encoding - collinearity.* For every collinear triple \((a,b,c)\) in \(G_n\) (enumerated once by the exact cross-product test), the clause \(\neg x_a\vee\neg x_b\vee\neg x_c\).
- *Encoding - cardinality.* The constraint \(\sum x_{ij}\ge m\) via a sequential / totalizer encoding.
- *Queries.* \(m=2n\) for existence (SAT gives a \(2n\)-set) and \(m=\tau(n)+1\) for optimality (UNSAT certifies the maximum).
- *Solvers.* **CaDiCaL**, **kissat**, **CryptoMiniSat** with **DRAT/LRAT** proof output; check UNSAT proofs with **drat-trim** / **cake_lpr**.
- *Symmetry breaking.* Use the \(D_4\) action (lex-leader constraints) to shrink the search, with care that broken symmetry does not invalidate the UNSAT semantics.
- *Triple generation.* Enumerate collinear triples exactly (rational-slope lines through each pair, extended within the grid); this precomputation is exact integer arithmetic and itself independently checkable.

**`[enum]` isomorph-free enumeration (for exact counts).** For exact solution counts and a completeness argument (P6):

- orderly generation / augmentation, adding points row by row and pruning any partial set that already contains a collinear triple;
- isomorph rejection under \(D_4\) with **nauty/Traces**;
- independent recount by a second method (e.g. exhaustive SAT model-counting) to cross-check the total.

**`[search]` heuristic construction (for pushing \(2n\)-existence).** Local search / SAT with random restarts to *find* \(2n\)-point sets for new \(n\) (P3); every found set is then exact-triple-certified.

**One-workstation scope.** The exact optimality / nonexistence searches (P4/P5) are the compute-heavy ones and grow fast with \(n\); a workstation can realistically extend the exhaustive frontier by a small increment and certify individual \(2n\)-existence far higher. State the reached \(n\) honestly.

**First-session checklist (concrete).**

1. Generate the exact collinear-triple set for a target \(n\) and independently verify it against a second implementation.
2. Reproduce \(\tau(n)\) for small \(n\) via SAT (existence at \(m=2n\), UNSAT at \(m=\tau(n)+1\)) with checked DRAT proofs (P1).
3. Certify \(2n\)-point sets across a band by exact triple-check over all \(\binom{2n}{3}\) triples (P2).
4. Attempt one new \(2n\)-existence \(n\) beyond the recorded frontier (P3), exact-certifying any set found.
5. Attempt one exhaustive extension of the exact-\(\tau\) frontier with a DRAT-checked optimality certificate (P4).

**Failure modes.**

- Missing collinear triples (e.g. only checking small slopes) - fatal false positives; the triple set must be exact and complete.
- Symmetry-breaking clauses that accidentally exclude solutions, corrupting an UNSAT claim - verify the lex-leader encoding preserves satisfiability.
- Trusting a solver's UNSAT without a checked DRAT proof.
- Overflow in cross-product arithmetic for large grids (use exact / bignum integers).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Non-collinearity of every configuration is verified by the exact integer cross-product over *all* \(\binom{|S|}{3}\) triples (equivalently, by confirming no line holds three points). Every maximality / nonexistence claim rests on a DRAT/LRAT-checked SAT-UNSAT proof or a complete isomorph-free enumeration. Floating point is never used for collinearity.
2. **Independent verification.** A standalone checker, independent of the search, re-reads each configuration and re-runs the exact triple test; for optimality / nonexistence it independently checks the DRAT proof with a second checker (drat-trim and cake_lpr), and for counts replays the enumeration with an independent isomorph filter (independent nauty invocation).
3. **Reproducibility.** The grid size, exact collinear-triple set, DIMACS encodings, symmetry-breaking scheme, solver versions and seeds, and all configurations are recorded; a SHA-256 manifest over DIMACS files, DRAT proofs, configuration lists, and checker logs.
4. **Preservation.** The triple generator, the SAT encoder, the enumeration code, and the heuristic constructor are all part of the record; anything not preserved is stated (the Hadamard-668 lost-source lesson). A `NEXT_STEPS.md` records the current certified frontier (largest \(2n\)-existence \(n\), largest exact-\(\tau\) \(n\)) when pausing (the Moore-57 pattern).
5. **Honest reporting.** The report states up front exactly what was certified - a \(2n\)-set (hence \(\tau(n)=2n\)) for an open \(n\), an exact \(\tau(n)\) or solution count for a new \(n\), or a certified nonexistence - and never presents a heuristically-found configuration as an optimum, nor a solver's unchecked UNSAT as a proof. The Guy–Kelly asymptotic is reported as the open conjecture it is, not as a result.
