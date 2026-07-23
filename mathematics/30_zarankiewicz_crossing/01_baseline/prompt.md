# PROMPT FOR CERTIFYING A CROSSING NUMBER OF A COMPLETE BIPARTITE GRAPH

## The Zarankiewicz conjecture at the \(K_{7,n}\) frontier

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 30 of 50  
**Area:** graph theory  
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Zarankiewicz's crossing-number conjecture asserts that the crossing number of the complete bipartite graph \(K_{m,n}\) equals \(Z(m,n)=\lfloor m/2\rfloor\lfloor(m-1)/2\rfloor\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor\). The value \(Z(m,n)\) is achieved by an explicit rectilinear drawing, so the upper bound is settled for all \(m,n\); the difficulty is the matching lower bound. Kleitman proved the conjecture whenever \(\min(m,n)\le 6\), leaving the frontier at \(\min(m,n)=7\), where the truth is known for the smallest cases (by a 1990s computer search whose certificate does not meet modern replay standards) and open beyond them. This is a finite optimization over a discrete space of drawings/rotation systems, and lower bounds are exactly the kind of statement SAT/UNSAT, flag-algebra, and exhaustive rotation-system arguments can certify - which is why it is matched to current AI methods. The resolution standard in section 2 is a certified crossing number \(\mathrm{cr}(K_{7,n})\) for a specific \(n\), or a certified improved lower bound toward the conjecture; anything numerical-only or non-replayable is reported as a partial result.

## 1. Exact problem statement

A **drawing** of a graph \(G\) in the plane maps vertices to distinct points and edges to simple curves joining their endpoints, with no edge passing through a non-incident vertex, no three edges crossing at a common point, and any two edges meeting in finitely many points. A **crossing** is a transversal intersection of two edges at a non-vertex point. The **crossing number** \(\mathrm{cr}(G)\) is the minimum number of crossings over all drawings; the **rectilinear crossing number** \(\overline{\mathrm{cr}}(G)\) restricts edges to straight segments, and \(\mathrm{cr}(G)\le\overline{\mathrm{cr}}(G)\).

For the complete bipartite graph \(K_{m,n}\), define the **Zarankiewicz number**
\[
Z(m,n)=\left\lfloor\tfrac{m}{2}\right\rfloor\left\lfloor\tfrac{m-1}{2}\right\rfloor\left\lfloor\tfrac{n}{2}\right\rfloor\left\lfloor\tfrac{n-1}{2}\right\rfloor.
\]
Zarankiewicz's drawing places the \(m\) vertices of one class on the vertical axis (\(\lceil m/2\rceil\) above the origin, \(\lfloor m/2\rfloor\) below) and the \(n\) vertices of the other on the horizontal axis (split likewise), joining all pairs by straight segments; a direct count of the crossings gives exactly \(Z(m,n)\). Hence
\[
\mathrm{cr}(K_{m,n})\le \overline{\mathrm{cr}}(K_{m,n})\le Z(m,n),
\]
so the upper bound is settled for every \(m,n\) and only the lower bound is at issue.
The **Zarankiewicz conjecture** is \(\mathrm{cr}(K_{m,n})=Z(m,n)\) for all \(m,n\ge 1\). Relevant values at the frontier:
\[
Z(7,7)=3\cdot3\cdot3\cdot3=81,\qquad Z(7,n)=9\left\lfloor\tfrac{n}{2}\right\rfloor\left\lfloor\tfrac{n-1}{2}\right\rfloor,\qquad Z(6,7)=3\cdot2\cdot3\cdot3=54.
\]

Because the upper bound is settled, the open content is entirely the **lower bound** \(\mathrm{cr}(K_{7,n})\ge Z(7,n)\).

A standard **counting (deletion) bound** already gives a nontrivial lower bound. Deleting one vertex from the size-\(n\) side of a drawing of \(K_{7,n}\) yields a drawing of \(K_{7,n-1}\); each crossing of the full drawing survives in a fixed fraction of the \(n\) sub-drawings, giving a recursion of the shape
\[
\mathrm{cr}(K_{7,n})\ \ge\ \left\lceil \frac{n}{\,n-2\,}\,\mathrm{cr}(K_{7,n-1})\right\rceil,
\]
and, seeded by Kleitman's exact \(\mathrm{cr}(K_{6,n})=Z(6,n)\) through a colour-class deletion, a bound of the form \(\mathrm{cr}(K_{7,7})\ge \lceil \tfrac{7}{5}\,\mathrm{cr}(K_{6,7})\rceil\) (verify the exact constant and resulting integer). These recursions typically leave a small additive gap below \(Z(7,n)\) - closing that gap for a specific \(n\) is the concrete objective.

**Task.** For a specific \(n\ge 7\), certify \(\mathrm{cr}(K_{7,n})\) exactly (prove \(\mathrm{cr}(K_{7,n})=Z(7,n)\), or determine a different exact value), or certify an improved lower bound \(\mathrm{cr}(K_{7,n})\ge L\) with \(L\) exceeding the best previously certified bound. Work with the ordinary (topological) crossing number unless a result is explicitly stated for the rectilinear variant. This problem is a sibling of Guy's conjecture for \(\mathrm{cr}(K_n)\) (problem 31), which it feeds via counting arguments.

Conventions fixed here: "drawing" means a good drawing in the plane (equivalently the sphere) in the topological sense above; the crossing number is the ordinary (topological) one unless the rectilinear variant \(\overline{\mathrm{cr}}\) is named explicitly; and \(m\le n\) is assumed without loss of generality by symmetry \(K_{m,n}\cong K_{n,m}\). A "good drawing" additionally satisfies the usual normalizations (adjacent edges do not cross, no two edges cross more than once, no edge crosses itself), which are known not to increase the minimum crossing count.

## 2. Resolution standard

Fix a specific \(n\ge 7\). The upper bound is not the difficulty (the Zarankiewicz drawing gives it for free); a resolution is judged almost entirely on the lower-bound certificate, which must be exact and independently replayable.

**Exact resolution.** A proof that \(\mathrm{cr}(K_{7,n})\) equals a specific integer, combining:
- an **upper bound** \(\mathrm{cr}(K_{7,n})\le U\) via an explicit drawing (a rotation system / combinatorial drawing whose crossing count is verified exactly by an independent checker), typically the Zarankiewicz drawing giving \(U=Z(7,n)\); and
- a **matching lower bound** \(\mathrm{cr}(K_{7,n})\ge U\), certified in one of the forms below.

**Lower-bound certified forms.**
- A **DRAT/LRAT-certified UNSAT** proof that no good drawing of \(K_{7,n}\) has fewer than \(U\) crossings - encoded via realizable rotation systems / the "good drawing" axioms as Boolean constraints - with all symmetry-breaking justified; checked by an independent verifier.
- An **exhaustive isomorph-free enumeration** of the relevant combinatorial drawings (rotation systems up to the natural symmetries), each evaluated exactly, terminating with a minimum of \(U\).
- A **flag-algebra / semidefinite** lower bound whose floating-point SDP solution is rounded to an **exact rational certificate** (a Positivstellensatz-style nonnegativity witness verified exactly), yielding \(\ge L\).

**Named certified form.** Upper bound: an explicit rotation system plus an independent exact crossing counter. Lower bound: a DRAT/LRAT UNSAT certificate over the good-drawing encoding, an isomorph-free rotation-system enumeration replay, or an exact-rational flag-algebra certificate.

A **different exact value** (should some \(\mathrm{cr}(K_{7,n})\) turn out to be strictly less than \(Z(7,n)\)) would refute the conjecture and is an extraordinary claim: it requires both an explicit sub-\(Z\) drawing and a certificate that it is optimal, held to the strongest standard.

**Not accepted as resolution.**
- The known upper bound \(Z(7,n)\) alone (the conjecture's hard direction is the lower bound).
- A numerical SDP lower bound reported in floating point without an exact rational certificate.
- A lower bound proved only for the **rectilinear** crossing number and presented as settling the ordinary crossing number (they may differ; state which).
- A heuristic drawing that happens to hit \(Z(7,n)\) crossings offered as a "proof" of optimality.
- Reproducing a previously known exact value without a modern, independently replayable certificate, if the claim is that the value is newly settled.
- An asymptotic ratio bound presented as an exact crossing number.
- A lower bound that relies on an unjustified restriction of the drawing space (e.g. to cylindrical or 2-page drawings) presented as a bound over all drawings.
- A SAT UNSAT whose realizability axioms are over-restrictive (excluding valid drawings), which produces an unsound lower bound.
- A crossing count computed in floating-point geometry rather than by exact combinatorial rules.

## 3. Graded partial-result targets

Ordered from reproducing the frontier to an exact single-\(n\) resolution. Each target names the specific \(n\) and the baseline it improves, and states whether the result is for the ordinary or the rectilinear crossing number.

**P1 - Reproduce the settled frontier with a modern certificate.** Independently re-derive the exact crossing number for the smallest settled \(K_{7,n}\) cases (those attributed to Woodall's 1990s computation) with a **replayable** certificate (exact crossing counter for the drawing, plus an independent lower-bound argument or enumeration). *Certificate:* exact drawing evaluation plus a machine-checkable lower-bound artifact; SHA-256 manifest. This is valuable precisely because the original certificates predate modern replay standards.

**P2 - Certified drawing evaluator and encoder.** Build and validate an exact rotation-system crossing counter and a "good drawing" SAT/CP encoding, validated end-to-end on \(K_{6,n}\) (settled by Kleitman) by reproducing \(Z(6,n)\) as both an upper bound (drawing) and a lower bound (encoding UNSAT below \(Z(6,n)\)). *Certificate:* round-trip on a solved case with independent replay.

**P3 - Counting lower bounds, made exact.** Certify the standard counting/deletion lower bounds \(\mathrm{cr}(K_{7,n})\ge \frac{n}{n-2}\,\mathrm{cr}(K_{7,n-1})\)-type recursions and the \(K_{6,\cdot}\)-based bounds in exact arithmetic, reporting the exact gap to \(Z(7,n)\). *Certificate:* an exact derivation with an independent recomputation of every rounded quantity. (This typically leaves a small gap, e.g. a handful of crossings for \(K_{7,7}\); closing it is the point.)

**P4 - Improved certified lower bound for one \(n\).** Push \(\mathrm{cr}(K_{7,n})\ge L\) above the best previously certified \(L\) for a specific \(n\), via SAT/UNSAT over the good-drawing encoding or an exact flag-algebra certificate. *Certificate:* DRAT/LRAT or exact-rational SDP witness, independently checked.

**P5 - Exact resolution for one \(n\).** Prove \(\mathrm{cr}(K_{7,n})=Z(7,n)\) for a specific \(n\) with matching certified bounds. *Certificate:* upper (drawing) + lower (certified) as in section 2. (Full resolution for that \(n\); the smallest genuinely open \(n\) is the natural target.)

**P6 - Structural reduction.** A certified reduction showing the conjecture for all \(K_{7,n}\) follows from finitely many base cases (in the spirit of the parity/counting reductions), each of which is then certified. *Certificate:* the reduction proof (formalized where practical) plus certificates for the base cases.

Targets P1–P4 are realistic session products; P5 is a full single-\(n\) resolution attainable only for the smallest open case; P6 is the most ambitious short of the general conjecture.

## 4. Known results and prior art

- **Origin.** Zarankiewicz (1954) proposed the drawing and an argument later found to be incomplete; the equality is now the standing conjecture. The upper bound \(\mathrm{cr}(K_{m,n})\le Z(m,n)\) is his (correct) contribution.
- **Kleitman (1970).** Proved \(\mathrm{cr}(K_{m,n})=Z(m,n)\) for \(\min(m,n)\le 6\), together with parity results on the crossing number that drive later reductions. The proof combines a counting argument with a parity constraint on the number of crossings among the edges at a vertex; reproducing it in exact arithmetic is a sound P2/P3 warm-up.
- **Guy, Beineke, Harary and early workers.** Established the small exact values and the conjecture's equivalent formulations; a modern survey of graphs with known or bounded crossing numbers collects the state of the art (verify the exact survey authors, title and year before citing).
- **Woodall (~1993).** "Cyclic-order graphs and Zarankiewicz's crossing-number conjecture" - a computer-assisted verification extending the conjecture to certain \(K_{7,n}\) and \(K_{8,n}\) cases (reported to include \(K_{7,7}\), \(K_{7,8}\), \(K_{7,9}\), \(K_{7,10}\), and some \(K_{8,\cdot}\)) (verify exactly which pairs, and note the certificate is 1990s-vintage and not in a modern replayable format). **This means \(K_{7,7}\) may already be settled; the smallest genuinely open \(K_{7,n}\) is likely larger - verify before choosing \(n\).**
- **de Klerk, Maharry, Pasechnik, Richter, Salazar (~2006).** Semidefinite-programming lower bounds on \(\mathrm{cr}(K_{m,n})/Z(m,n)\) and asymptotic constants; later refined by Norin, Zwols and others toward a limiting ratio around \(0.85\)–\(0.86\) (verify constant and attribution). These are numerical/asymptotic, not exact single-\(n\) certificates.
- **Best certified single-\(n\) lower bounds.** For the smallest cases beyond Kleitman's range, the strongest exact lower bounds come from the counting recursion seeded at \(K_{6,\cdot}\) together with case analysis; the exact current-best value for each open \(n\) (e.g. how close \(\mathrm{cr}(K_{7,n})\) is provably to \(Z(7,n)\)) must be read from the current literature (verify), since it has been sharpened over time.
- **Identifying the smallest open case.** With Kleitman (\(\min\le 6\)) and Woodall's \(K_{7,\cdot}\) cases both settled, the smallest genuinely open bipartite complete graph is likely a \(K_{7,n}\) with larger \(n\), or a \(K_{9,9}\)-type odd–odd case; determine it explicitly before choosing a target (verify).
- **Reductions.** It is classical that the conjecture for all \(m,n\) reduces to \(m,n\) both odd (and via counting to finitely many base cases per row): if \(\mathrm{cr}(K_{2a+1,2b+1})=Z(2a+1,2b+1)\), the even cases \(K_{2a+1,2b+2}\), \(K_{2a+2,2b+2}\) follow by counting/parity. Hence certifying the odd frontier cases \(K_{7,7}, K_{7,9}, K_{7,11},\dots\) is the load-bearing work.
- **Rectilinear variant.** For the *rectilinear* crossing number of \(K_{m,n}\) the Zarankiewicz value is also the conjectured answer and the drawing is straight-line, but rectilinear lower bounds use order-type / allowable-sequence machinery distinct from the topological rotation-system approach; a rectilinear result does not settle the ordinary crossing number and must be labelled accordingly.
- **Do not confuse with the Zarankiewicz *problem*.** The Kővári–Sós–Turán "Zarankiewicz problem" (maximum edges in a bipartite graph with no \(K_{s,t}\)) shares the name but is a different question; only the crossing-number conjecture is in scope here.
- **2-page / book bounds.** Techniques that pin the 2-page (book) crossing number provide strong evidence and sometimes matching bounds for bipartite complete graphs; treat any 2-page result as a related but distinct quantity unless it is shown to equal the ordinary crossing number for the case at hand.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** The exact set of settled \(K_{7,n}\) cases and the best certified lower bounds have moved over time; crossing-number lower bounds have been sharpened repeatedly since 2005. Confirm which \(K_{7,n}\) are already exact (Kleitman's range plus Woodall's cases) and pick the smallest genuinely open \(n\), or target a modern replayable re-certification of a case whose only proof is the 1990s computation.

## 5. Attack plan

First fix the target \(n\) after confirming its status (Kleitman settles \(\min\le 6\); Woodall's cases must be checked), and record the current best certified lower bound as the baseline to beat. Decide up front whether the session pursues a modern re-certification of an unpreserved case (P1) or an attack on the smallest confirmed-open case (P4/P5); the two use the same toolchain but different targets.

**Combinatorial drawings, not geometry (`[search]`).** Work with **rotation systems** (the cyclic order of edges around each vertex) and the good-drawing axioms rather than coordinates; the ordinary crossing number is determined by the realizable rotation systems, and the crossing count of a rotation system is computed exactly by combinatorial rules. Build an exact crossing counter first and validate it on Kleitman's settled cases.

**Realizability is the crux.** Not every abstract rotation system is realizable by a good drawing, and not every good drawing minimises crossings within its "independent odd crossing" class; encoding realizability soundly is the single hardest and most error-prone step. Use the established Hanani–Tutte / independent-odd-crossing framework where it applies, and validate the encoding by round-tripping known optimal drawings of \(K_{6,n}\) and small \(K_{7,n}\) before trusting any UNSAT.

**Rotation-system enumeration (`[search]`).** For the smallest \(n\), enumerate combinatorial drawings up to the natural symmetry group (permutations within each colour class, reflection, sphere homeomorphism) with canonical-form rejection, evaluating each exactly; the minimum over a provably complete enumeration is a lower bound. This is the most transparent certificate but the count grows fast, so it is feasible only at the frontier's smallest open case.

**SAT / pseudo-Boolean lower bounds (`[opt]`).** Encode "there is a good drawing of \(K_{7,n}\) with \(< U\) crossings" as a Boolean/pseudo-Boolean formula over crossing indicator variables constrained by the realizability axioms and parity constraints; run CaDiCaL / kissat / CryptoMiniSat, emit DRAT, convert to LRAT, and check independently. Sound symmetry-breaking (vertex-class permutations, reflections) is essential and must be justified - an unsound break silently converts a true SAT into a false UNSAT.

**Flag algebras / SDP, made exact (`[opt]`).** Reproduce the de Klerk–style SDP lower bound, then convert a floating-point optimum to an exact rational Positivstellensatz certificate (rationalize the SDP solution and verify nonnegativity exactly in a CAS). Only the exact certificate counts. For a single small \(n\), a finite flag-algebra relaxation truncated at the right level may already exceed the counting bound; the exactness of the rounding, not the SDP objective, is what makes it a certificate.

**Small solved analogues.** Validate the whole pipeline on cases Kleitman settled - reproduce \(\mathrm{cr}(K_{5,n})\) and \(\mathrm{cr}(K_{6,n})\) exactly (upper via the Zarankiewicz drawing, lower via the same encoding) - before trusting any tool at \(K_{7,n}\). A crossing counter or an UNSAT encoding that cannot reproduce a Kleitman value is not trusted at the open case.

**Counting recursions.** Implement the deletion/counting lower bounds in exact arithmetic to pin the current provable lower bound and the exact gap to \(Z(7,n)\); this frames how much a SAT/flag-algebra argument must close. Chain the recursion from Kleitman's exact \(K_{6,\cdot}\) values and from any newly certified \(K_{7,n-1}\) value to propagate an improvement across a whole row of \(n\).

**Cube-and-conquer for the hard case.** For the smallest open \(n\), a monolithic SAT call is likely to stall; split the search with cube-and-conquer (partition on a well-chosen set of crossing indicators or on a sub-drawing type), solve the cubes in parallel on one workstation, and concatenate the DRAT proofs into a single independently checkable certificate.

**Propagating a single result across a row.** Because the counting recursion links \(K_{7,n}\) to \(K_{7,n-1}\) and the parity reductions link odd to even, one certified odd case can lift the certified lower bound for an entire family of \(n\); implement the propagation exactly so a single hard win is leveraged fully.

**Concrete toolchain on one workstation.**
- nauty/Traces for canonical forms in the rotation-system enumeration;
- CaDiCaL / kissat / CryptoMiniSat for SAT, with `drat-trim` / `cake_lpr` for independent DRAT/LRAT checking;
- a bespoke C++ exact crossing counter over rotation systems (the performance-critical inner loop);
- an SDP solver (e.g. SDPA-GMP or a high-precision interior-point code) for flag-algebra relaxations, with a CAS (SageMath / Macaulay2) for exact rationalization;
- exact integer/rational arithmetic (FLINT/Arb) throughout the counting recursions;
- a proof assistant (Lean 4 + mathlib) for the non-computational skeleton of any structural reduction (P6), keeping generated certificates outside the trusted base.

**One-workstation scope and failure modes.** A single workstation can: evaluate and enumerate rotation systems for small \(K_{7,n}\); run SAT/UNSAT on the smallest open case with good symmetry-breaking; and rationalize small SDPs. It **cannot** brute-force rotation systems for large \(n\) (the count explodes), and SAT encodings of the good-drawing axioms grow quickly - expect the smallest open \(n\) to be the only feasible exact target, with larger \(n\) reachable only via reductions or asymptotic bounds. Expect: realizability axioms that are subtle to encode soundly (an over-permissive encoding gives a false lower bound; an over-restrictive one gives an unsound UNSAT); SAT calls that stall without cube-and-conquer; and SDP solutions that resist clean rationalization. Report the rectilinear-vs-ordinary distinction explicitly in every bound.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every crossing count computed by exact combinatorial rules; every lower bound backed by DRAT/LRAT, an enumeration replay, or an exact-rational flag-algebra certificate. Floating-point SDP output is exploratory only.
2. **Independent verification.** An exact crossing counter written separately from the search validates every claimed drawing. UNSAT proofs are checked by an independent DRAT/LRAT verifier; enumeration lower bounds are re-run independently; SDP certificates are re-verified in a second CAS.
3. **Reproducibility.** All encodings, symmetry-breaking clauses, solver versions, SDP inputs, rounding procedures, seeds, and environment recorded; SHA-256 manifest over every artifact. The baseline value being improved (which \(n\), which prior bound, from which source and access date) is recorded so the claimed improvement is unambiguous.
4. **Preservation.** Encoder, drawing evaluator, and SDP-rationalization source code is part of the record. Any symmetry assumption or restriction to a drawing class is stated explicitly - the Hadamard-668 lost-source lesson (and directly relevant here, since the 1990s \(K_{7,\cdot}\) certificates are effectively unpreserved).

   A specific consequence: if the session produces a modern replayable certificate for a case previously known only through Woodall's computation, that certificate - not merely the restated value - is the deliverable, and it is archived with the same rigour as a new result.
5. **Honest reporting.** The report states up front whether an exact \(\mathrm{cr}(K_{7,n})\) was certified for a specific \(n\), whether a lower bound was strictly improved, and whether each result is for the ordinary or rectilinear crossing number. A numerical SDP value or a known upper bound is never represented as resolving the conjecture.

### Calibration

The full conjecture is a hard, long-standing problem; a single session will most realistically deliver P1–P4 - a modern replayable certificate for an already-settled small case, an exact-arithmetic counting bound with the precise gap to \(Z(7,n)\), or a strict lower-bound improvement for one \(n\). An exact resolution (P5) is plausible only for the smallest genuinely open \(n\), and only if the realizability encoding is sound and the cube-and-conquer split is tractable on one workstation. Because \(K_{7,7}\) may already be settled by Woodall's 1990s computation, the most defensible framings are (a) a modern replayable re-certification of a case whose only proof is unpreserved, or (b) an attack on the smallest \(n\) confirmed open. State which framing is taken and why.
