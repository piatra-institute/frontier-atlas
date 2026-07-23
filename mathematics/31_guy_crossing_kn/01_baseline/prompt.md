# PROMPT FOR CERTIFYING THE CROSSING NUMBER OF A COMPLETE GRAPH

## Guy's conjecture at the first open case \(\mathrm{cr}(K_{13})\)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 31 of 50  
**Area:** graph theory  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Guy's conjecture gives a closed form for the crossing number of the complete graph, \(\mathrm{cr}(K_n)=\frac{1}{4}\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor\lfloor(n-2)/2\rfloor\lfloor(n-3)/2\rfloor\), matched by an explicit cylindrical drawing. The value is proven for all \(n\le 12\); by a parity argument the odd cases drive the even ones, so the first open case is \(n=13\), where the conjectured value 225 is bracketed by a best-known lower bound in the low 220s and the upper bound 225 - a gap of only a few crossings. This is a finite, certifiable optimization: the upper bound is an explicit drawing whose crossings are counted exactly, and the lower bound is a counting/SAT/exhaustive statement over combinatorial drawings of a fixed small graph. It is well matched to current AI methods for that reason. The resolution standard in section 2 - a certified exact \(\mathrm{cr}(K_{13})\) (or the next open \(n\)), or a certified improved lower bound - is the target; a heuristic drawing hitting the conjectured value, or a floating-point bound, is reported only as a partial result.

## 1. Exact problem statement

Drawings, crossings, and the crossing number \(\mathrm{cr}(G)\) are as in the standard topological sense: vertices to distinct points, edges to simple curves, no edge through a non-incident vertex, no three edges through one point, finitely many pairwise intersections; a crossing is a transversal meeting of two edges at a non-vertex point; \(\mathrm{cr}(G)\) is the minimum number of crossings over all drawings. The **rectilinear** crossing number \(\overline{\mathrm{cr}}(G)\) restricts to straight edges and satisfies \(\mathrm{cr}(G)\le\overline{\mathrm{cr}}(G)\); for \(K_n\) the two differ for \(n\ge 8\), so results must state which is meant.

Define the **Guy number**
\[
Z(n)=\frac{1}{4}\left\lfloor\tfrac{n}{2}\right\rfloor\left\lfloor\tfrac{n-1}{2}\right\rfloor\left\lfloor\tfrac{n-2}{2}\right\rfloor\left\lfloor\tfrac{n-3}{2}\right\rfloor.
\]
A **cylindrical** (or "tin-can") drawing places \(\lceil n/2\rceil\) vertices on one circle and \(\lfloor n/2\rfloor\) on a concentric circle, drawing intra-circle edges as arcs and inter-circle edges across the annulus; a direct count of the three crossing types (top–top, bottom–bottom, top–bottom) totals exactly \(Z(n)\), so
\[
\mathrm{cr}(K_n)\le Z(n).
\]
The same value \(Z(n)\) is achieved by a **2-page** (book) drawing, which is the form most amenable to combinatorial verification.
**Guy's conjecture** is \(\mathrm{cr}(K_n)=Z(n)\) for all \(n\). Relevant values:
\[
Z(11)=\tfrac{1}{4}\cdot5\cdot5\cdot4\cdot4=100,
\]
\[
Z(12)=\tfrac{1}{4}\cdot6\cdot5\cdot5\cdot4=150,
\]
\[
Z(13)=\tfrac{1}{4}\cdot6\cdot6\cdot5\cdot5=225.
\]

A key structural fact: a counting/parity argument gives \(\mathrm{cr}(K_{2k})\) from \(\mathrm{cr}(K_{2k-1})\), so proving the conjecture for odd \(n\) yields the next even \(n\). Concretely, in any drawing of \(K_{2k}\) the \(2k\) sub-drawings obtained by deleting one vertex are drawings of \(K_{2k-1}\), and a counting identity relates their total crossing count to that of \(K_{2k}\); combined with a parity constraint this forces \(\mathrm{cr}(K_{2k})=Z(2k)\) once \(\mathrm{cr}(K_{2k-1})=Z(2k-1)\) is known. Hence the frontier is at odd \(n\): with \(n\le 12\) settled, the first open case is \(n=13\), and settling \(K_{13}\) also settles \(K_{14}\).

Conventions fixed here: "drawing" and "crossing" are topological as above; the crossing number is the ordinary one unless the rectilinear \(\overline{\mathrm{cr}}\) is named; a good drawing satisfies the standard normalizations (adjacent edges do not cross, two edges cross at most once, no self-crossings), which do not increase the minimum. Every 4-subset of vertices induces a \(K_4\) that contributes 0 or 1 crossings, so the crossing number of a drawing is \(\sum_{4\text{-subsets}} [\text{the four points are in "convex" position in the drawing}]\).

**Task.** Certify \(\mathrm{cr}(K_{13})\) exactly (prove \(\mathrm{cr}(K_{13})=225\), or determine a different exact value), or certify an improved lower bound \(\mathrm{cr}(K_{13})\ge L\) beyond the best previously certified \(L\). If \(K_{13}\) is settled before a session, target the next open \(n\). Work with the ordinary crossing number unless a result is explicitly for the rectilinear variant. This problem is linked by counting arguments to the Zarankiewicz conjecture for \(K_{m,n}\) (problem 30).

## 2. Resolution standard

**Exact resolution for \(n\).** A proof that \(\mathrm{cr}(K_n)\) equals a specific integer, combining:
- an **upper bound** \(\mathrm{cr}(K_n)\le U\) from an explicit drawing - a rotation system / combinatorial good drawing whose crossing count is verified exactly by an independent checker (the cylindrical drawing gives \(U=Z(n)\)); and
- a **matching lower bound** \(\mathrm{cr}(K_n)\ge U\), in a certified form below.

**Lower-bound certified forms.**
- A **DRAT/LRAT-certified UNSAT** proof that no good drawing of \(K_n\) has fewer than \(U\) crossings - encoded over realizable rotation systems / good-drawing axioms with justified symmetry-breaking - checked by an independent verifier.
- An **exhaustive isomorph-free enumeration** of the relevant combinatorial drawings (rotation systems up to symmetry) with exact per-drawing crossing counts, minimum \(=U\).
- A **counting reduction** to already-certified smaller cases (e.g. \(\mathrm{cr}(K_{n})\ge\binom{n}{n-4}^{-1}\)-type responsibility counting from \(\mathrm{cr}(K_{n-1})\) or \(K_{5}\)-subgraph counting), carried out in exact arithmetic, possibly combined with the above.
- An **insertion analysis** over a completely classified set of optimal (or sub-\(U\)) drawings of \(K_{n-1}\), bounding the crossings any added vertex must create.

**Named certified form.** Upper bound: an explicit rotation system plus an independent exact crossing counter. Lower bound: a DRAT/LRAT UNSAT certificate over the good-drawing encoding, an isomorph-free rotation-system enumeration replay, or an exact-arithmetic counting certificate reducing to certified smaller cases.

**Not accepted as resolution.**
- The cylindrical upper bound \(Z(n)\) alone (the hard direction is the lower bound).
- A heuristic or randomized drawing achieving \(Z(n)\) crossings offered as proof of optimality.
- A lower bound proved only for the **rectilinear** crossing number and presented as settling the ordinary one.
- A floating-point SDP/flag-algebra bound without an exact rational certificate.
- Reproducing the known bracket \(223\le\mathrm{cr}(K_{13})\le 225\) (or whatever the current interval is) without strictly improving it or closing it.
- An asymptotic constant presented as an exact value.
- A lower bound that silently restricts to cylindrical, 2-page, or rectilinear drawings and is presented as a bound over all topological drawings.
- A crossing count obtained from floating-point coordinates rather than exact combinatorial evaluation.

## 3. Graded partial-result targets

Ordered from reproducing the settled frontier to full resolution of the first open case. Each target names the specific \(n\), the baseline it improves, and the crossing-number variant.

**P1 - Reproduce the settled frontier.** Independently re-certify \(\mathrm{cr}(K_n)\) for the largest settled cases (\(\mathrm{cr}(K_{11})=100\), \(\mathrm{cr}(K_{12})=150\)) with your own exact crossing counter and a replayable lower-bound artifact, matching the full sequence \(1,3,9,18,36,60,100,150\) for \(n=5,\dots,12\). *Certificate:* exact drawing evaluation plus a machine-checkable lower bound; SHA-256 manifest.

**P2 - Certified evaluator and encoder.** Build and validate an exact rotation-system crossing counter and a good-drawing SAT/CP encoding, validated on \(K_{10}\)/\(K_{11}\) by reproducing \(Z(10)=60\), \(Z(11)=100\). *Certificate:* round-trip on settled cases with independent replay.

**P3 - Reproduce and tighten the \(K_{13}\) lower bound.** Re-derive the current best certified lower bound for \(\mathrm{cr}(K_{13})\) (reported in the low 220s) in exact arithmetic via responsibility/\(K_5\)-counting from \(\mathrm{cr}(K_{12})\), and report the exact remaining gap to 225. *Certificate:* exact counting derivation with independent recomputation.

**P4 - Improved certified lower bound for \(K_{13}\).** Push \(\mathrm{cr}(K_{13})\ge L\) above the best previously certified \(L\) (i.e. beyond the current low-220s bound), via SAT/UNSAT over the good-drawing encoding or an exhaustive rotation-system argument on a reduced sub-space. *Certificate:* DRAT/LRAT or enumeration replay. Concretely, this may take one of three forms:
- a SAT UNSAT that no good drawing has \(<L\) crossings, checked by an independent verifier;
- a sharpened responsibility-counting weighting, re-derived independently, that provably yields \(\ge L\);
- an insertion analysis over a classified optimal-\(K_{12}\) set showing every extension exceeds \(L-1\) crossings.

**P5 - Exact resolution of \(K_{13}\).** Prove \(\mathrm{cr}(K_{13})=225\) with matching certified bounds; by the parity argument this also yields \(\mathrm{cr}(K_{14})=Z(14)\). The deliverable is three certificates:
- the upper bound: an explicit \(K_{13}\) drawing (cylindrical or 2-page) with \(225\) crossings, exactly counted;
- the lower bound: \(\mathrm{cr}(K_{13})\ge 225\), in one of the section-2 certified forms;
- the parity step: an exact (ideally formalized) certificate deriving \(\mathrm{cr}(K_{14})=Z(14)\) from the \(K_{13}\) value. (Full resolution for \(n=13,14\).)

**P6 - Structural / formal reduction.** A machine-checkable reduction of the conjecture for a range of \(n\) to finitely many certified base cases, or a Lean/Isabelle formalization of the parity step and the exact counting bounds. *Certificate:* formalized proof plus certificates for base cases.

Targets P1–P4 are realistic session products; P5 is a full resolution of the first open case (and, via parity, the next even case); P6 is the most ambitious short of the general conjecture. A result that leaves the bracket \([L,225]\) unchanged is reported at its true grade, not promoted.

## 4. Known results and prior art

- **Origin.** R. K. Guy proposed the conjecture (~1960) and computed small values; the cylindrical drawing giving \(Z(n)\) is classical (Guy; also attributed to the "two concentric circles" construction). Guy also observed the \(Z(2k-1)\Rightarrow Z(2k)\) parity reduction, which localizes the problem to odd \(n\).
- **Exact small values.** \(\mathrm{cr}(K_n)\) is known for \(n\le 12\): \(1,3,9,18,36,60,100,150\) for \(n=5,\dots,12\), matching \(Z(n)\). The values through \(n=10\) were settled by the 1970s–1990s; \(n=11,12\) by Pan–Richter (verify).
- **Small exact values.** \(\mathrm{cr}(K_n)=Z(n)\) is established for all \(n\le 12\): the low cases by hand/early computation; \(\mathrm{cr}(K_{11})=100\) and \(\mathrm{cr}(K_{12})=150\) by Pan and Richter (~2007), using the fact that \(\mathrm{cr}(K_{11})=100\) implies \(\mathrm{cr}(K_{12})=150\) via the parity/counting step (verify).
- **\(K_{13}\) bounds.** The conjectured value is 225. The best certified lower bound is in the low 220s - reported as \(\mathrm{cr}(K_{13})\ge 223\) via responsibility-counting refinements (McQuillan, Pan, Richter and related work, mid-2010s) (verify current record; earlier bounds were 217, 219, 221 before being improved). The upper bound is \(225\) from the cylindrical drawing. So \(223\le\mathrm{cr}(K_{13})\le 225\) (verify), a gap of at most two crossings - one of the smallest open gaps in the crossing-number literature.
- **2-page and rectilinear variants.** Ábrego, Fernández-Merchant, Salazar and collaborators established that the **2-page** (book) crossing number of \(K_n\) equals \(Z(n)\), strong evidence for the conjecture (verify). The **rectilinear** crossing number of \(K_n\) is strictly larger than \(Z(n)\) for \(n\ge 8\) and is a separate, actively studied quantity (Ábrego–Fernández-Merchant, Aichholzer et al.) - do not conflate it with the ordinary crossing number.
- **Asymptotics.** de Klerk, Pasechnik and collaborators gave SDP-based lower bounds on \(\lim \mathrm{cr}(K_n)/Z(n)\) (around \(0.85\)–\(0.86\)) (verify); numerical/asymptotic, not exact single-\(n\) certificates.
- **Method of Pan–Richter.** Their \(n=11\) proof combined an exhaustive analysis of optimal drawings of \(K_{10}\) (via the "flag" / rotation-system classification of good drawings) with the counting step to \(K_{12}\); the same style of argument, scaled to \(K_{12}\to K_{13}\), is the natural template, but the number of drawings to classify grows steeply (verify the exact method and its cost).
- **Rectilinear crossing number.** The rectilinear \(\overline{\mathrm{cr}}(K_n)\) is a distinct, larger quantity studied via order types and the "\(k\)-set" / allowable-sequence machinery (Ábrego–Fernández-Merchant, Aichholzer, and the order-type database); a rectilinear bound does not settle \(\mathrm{cr}(K_n)\) and must be labelled. The rectilinear values are known exactly for a somewhat different range of \(n\) (verify).
- **Cross-reference.** The bipartite Zarankiewicz conjecture (problem 30) and Guy's conjecture are linked: counting arguments pass bounds between \(\mathrm{cr}(K_n)\), \(\mathrm{cr}(K_{m,n})\), and the crossing number of \(K_{m,n}\) plus an internal drawing; techniques transfer between the two.
- **Enumeration feasibility.** Complete isomorph-free enumeration of good drawings of \(K_n\) has been carried out for small \(n\) (the number grows very fast; the \(K_{13}\) count is far beyond direct enumeration), which is why lower-bound progress at \(K_{13}\) depends on counting reductions and classified-drawing insertion rather than raw enumeration (verify the largest \(n\) fully enumerated).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** The exact best lower bound for \(\mathrm{cr}(K_{13})\) has been sharpened repeatedly; confirm whether \(K_{13}\) has been fully settled (which would move the frontier to \(K_{15}\)) and confirm the current bracket before committing compute.

## 5. Attack plan

First confirm the current status (whether \(K_{13}\) remains open, and the exact current best lower bound) and record it as the baseline. Then split into a lower-bound workstream (the hard direction) and a verification workstream (reproduce the settled frontier and validate tooling).

**Combinatorial drawings (`[search]`).** Work with rotation systems and good-drawing axioms; the ordinary crossing number of \(K_n\) is a minimum over realizable rotation systems, and each crossing count is computed exactly by combinatorial rules (every 4-subset contributes 0 or 1 crossing depending on the induced rotation). Build and validate an exact counter on \(n\le 12\) first, checking it against the known exact values \(\mathrm{cr}(K_5)=1,\ \mathrm{cr}(K_6)=3,\ \mathrm{cr}(K_7)=9,\dots,\mathrm{cr}(K_{12})=150\).

**Responsibility / \(K_5\)-counting lower bounds.** Every drawing of \(K_n\) restricts to \(\binom{n}{5}\) drawings of \(K_5\) (each with \(\ge 1\) crossing) and \(\binom{n}{k}\) drawings of \(K_k\); exact counting relations (each crossing is "responsible" in a fixed number of sub-drawings) yield lower bounds from certified smaller cases. The basic bound chained upward from small \(k\), and its refinements weighting sub-drawings by their exact crossing distribution, are what push the \(K_{13}\) lower bound into the low 220s. Implement these in exact arithmetic to reproduce the current record and then attempt to sharpen the weighting.

**Optimal-drawing classification.** Following Pan–Richter, classify the optimal (or near-optimal) drawings of \(K_{12}\) up to rotation-system isomorphism, then bound how a 13th vertex can be inserted; the crossing contribution of the new vertex against every 4-subset is exactly countable, turning the lower bound into a finite case analysis over a classified set. Feasibility hinges on the size of the optimal-\(K_{12}\) class, which must be measured before committing.

**SAT / pseudo-Boolean UNSAT (`[search]`).** Encode "a good drawing of \(K_{13}\) with \(<U\) crossings exists" over crossing indicators constrained by the realizability axioms and parity, with sound symmetry-breaking (relabelings, reflections); run CaDiCaL / kissat / CryptoMiniSat, emit DRAT, convert to LRAT, check independently. Reducing to sub-spaces (fixing a sub-drawing type) may make the smallest gap closable.

**Parity-step certification.** The step \(\mathrm{cr}(K_{2k-1})=Z(2k-1)\Rightarrow\mathrm{cr}(K_{2k})=Z(2k)\) is a finite counting/parity argument; certify it exactly (and ideally formalize it in Lean) so that resolving \(K_{13}\) automatically and auditably yields \(K_{14}\). This is cheap relative to the \(K_{13}\) lower bound and should be done regardless, since it doubles the payoff of a full resolution.

**Independent re-derivation of counting identities.** Every responsibility-counting coefficient (how many sub-drawings each crossing is counted in, for each \(k\)) is re-derived by a second, independently written routine; a single off-by-one in these coefficients silently corrupts the whole lower bound.

**Reduced sub-space strategy.** The unrestricted \(K_{13}\) drawing space is intractable, but fixing the rotation at one vertex, or the induced drawing on a well-chosen sub-clique, partitions the space into cases; each case is a smaller SAT/enumeration problem, and their union is provably exhaustive if the case split is a genuine partition. The certificate is the disjunction: a completeness argument for the split plus a per-case UNSAT/enumeration, each independently checkable.

**Concrete toolchain on one workstation.**
- a bespoke C++ exact crossing counter over rotation systems, and nauty/Traces for canonical forms in any drawing classification;
- CaDiCaL / kissat / CryptoMiniSat with cube-and-conquer for the reduced \(K_{13}\) UNSAT attempts, and `drat-trim` / `cake_lpr` for independent proof checking;
- exact integer/rational arithmetic (FLINT/Arb) for the responsibility-counting bounds, with an independent second implementation of every counting identity;
- an SDP solver plus a CAS (SageMath / Macaulay2) if a flag-algebra bound is rationalized;
- Lean 4 + mathlib for formalizing the parity step and the counting skeleton (P6), certificates kept outside the trusted base.

**Small solved analogues.** Reproduce \(\mathrm{cr}(K_{10})=60\) and \(\mathrm{cr}(K_{11})=100\) end to end (drawing + certified lower bound) before trusting any tool at \(K_{13}\); a counter or encoding that cannot recover a settled value is not trusted at the open case.

**One-workstation scope and failure modes.** A single workstation can: evaluate/enumerate rotation systems for \(n\le 12\) fully, run the counting bounds exactly, and attempt SAT/UNSAT on carefully reduced \(K_{13}\) sub-spaces. It **cannot** enumerate all good drawings of \(K_{13}\) unrestricted (the space is far too large), so lower-bound progress relies on counting reductions and symmetry, not brute force. Expect: subtlety in encoding realizability soundly (over-permissive → false bound; over-restrictive → unsound UNSAT); counting bounds that stall a couple of crossings short of 225; SAT calls that stall without cube-and-conquer; and rectilinear/ordinary confusion - state the variant on every claim.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every crossing count computed by exact combinatorial rules; every lower bound backed by DRAT/LRAT, an enumeration replay, or an exact-arithmetic counting certificate. Floating point is exploratory only.
2. **Independent verification.** An exact crossing counter written separately from the search validates every drawing, cross-checked against the known values \(\mathrm{cr}(K_5),\dots,\mathrm{cr}(K_{12})\). UNSAT proofs are checked by an independent DRAT/LRAT verifier; counting bounds are recomputed by a second implementation of every coefficient; any SDP certificate is re-verified in a second CAS.
3. **Reproducibility.** All rotation-system encodings, symmetry-breaking clauses, counting derivations, case-split definitions, solver versions, seeds, and environment recorded; SHA-256 manifest over every artifact. The baseline lower bound being improved (value, source, access date) is recorded so the claimed gain is unambiguous.
4. **Preservation.** Encoder, evaluator, and counting-derivation source code is part of the record; any restriction to a drawing sub-class or symmetry assumption is stated explicitly as a scope limit - the Hadamard-668 lost-source lesson. If an optimal-\(K_{12}\) classification is produced, the classified set (canonical rotation systems) is archived so the insertion analysis is independently replayable.
5. **Honest reporting.** The report states up front whether an exact \(\mathrm{cr}(K_n)\) was certified, whether the \(K_{13}\) lower bound was strictly improved, and whether each result is ordinary or rectilinear. A cylindrical upper bound or a heuristic optimal-looking drawing is never represented as resolving the conjecture.

### Calibration

The \(K_{13}\) gap is small (at most two crossings above the current lower bound), which makes this one of the more attackable open crossing-number problems - but "small gap" has been true for years without closure, so honest expectations matter. A single session most realistically delivers P1–P4: a reproduced frontier, an exact-arithmetic responsibility bound recovering the current record, or a strict lower-bound improvement of \(K_{13}\) by one crossing. Full resolution (P5) would settle both \(K_{13}\) and \(K_{14}\) and is a genuine research result, plausible only if the optimal-\(K_{12}\) classification is small enough for the insertion analysis or a reduced UNSAT closes the last crossing. Report the exact bracket achieved, and never present the cylindrical \(Z(13)=225\) upper bound as the answer.
