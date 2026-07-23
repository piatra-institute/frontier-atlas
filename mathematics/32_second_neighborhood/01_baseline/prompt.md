# PROMPT FOR SEYMOUR'S SECOND-NEIGHBOURHOOD CONJECTURE

## Certified verification and structural partial results on \(|N^{++}(v)|\ge|N^{+}(v)|\)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 32 of 50  
**Area:** graph theory  
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Seymour's second-neighbourhood conjecture asserts that every finite oriented graph has a vertex whose second out-neighbourhood is at least as large as its first out-neighbourhood - a "Seymour vertex". It is proven for tournaments (Fisher; Havet–Thomassé) and several other classes, but open in general, and a full proof is genuinely hard. This prompt is honest about that: the product is not a claimed general proof but a graded set of **certifiable** contributions - an exhaustive, replayable verification up to a vertex count; certified verification on new graph classes; and structural partial results (density constants, weightings, median-order arguments) with machine-checkable content. The finite verification is exactly matched to current AI methods (isomorph-free digraph generation plus a trivial per-graph check), and the constant-factor and class results are matched to exact optimization and computer-assisted proof. The resolution standard in section 2 (a complete proof of the conjecture) is stated as the ultimate target and is **not** expected in a session; every partial result is reported as such and never dressed up as the general theorem.

## 1. Exact problem statement

A **digraph** \(D=(V,A)\) is a finite set of vertices with a set of ordered pairs (arcs). An **oriented graph** is a digraph with no loops and no **digon** (no pair \(u\to v\) and \(v\to u\) simultaneously); equivalently, an orientation of a simple graph. For \(v\in V\):
\[
N^{+}(v)=\{u: v\to u\in A\},\qquad
N^{++}(v)=\Big(\bigcup_{u\in N^{+}(v)}N^{+}(u)\Big)\setminus\big(N^{+}(v)\cup\{v\}\big),
\]
the **first** and **second out-neighbourhoods**. A vertex \(v\) with \(|N^{++}(v)|\ge|N^{+}(v)|\) is a **Seymour vertex**.

**Seymour's second-neighbourhood conjecture (SNC).** Every finite oriented graph has at least one Seymour vertex.

Notes fixing the statement: the digon-free (oriented) hypothesis is essential - it fails for general digraphs (e.g. a directed 2-cycle-laden example); "second out-neighbourhood" excludes \(N^{+}(v)\) and \(v\) itself as written above; and vertices of out-degree 0 are trivially Seymour vertices, so only digraphs with all out-degrees positive are interesting. A convenient reformulation uses the closed out-neighbourhood and a "loss" function; another assigns each vertex \(v\) the deficiency \(\delta(v)=|N^{++}(v)|-|N^{+}(v)|\) and asks for \(\max_v\delta(v)\ge 0\).

**Task.** Produce certifiable contributions toward SNC: (i) an exhaustive replayable verification that every oriented graph on at most \(n\) vertices has a Seymour vertex, for the largest feasible \(n\); (ii) a certified proof of SNC for a new graph class; or (iii) a structural partial result (an improved density constant, a weighting or median-order argument, a reduction) with machine-checkable content. A full general proof (section 2) is the ultimate target but not the expected product.

## 2. Resolution standard

**Full resolution.** A correct proof that every finite oriented graph has a Seymour vertex, general over all orders. Because this is a statement about all finite oriented graphs, resolution is a **mathematical proof**, ideally formalized in Lean 4 + mathlib or an equivalent proof assistant so the logical core is machine-checked; any finite computation the proof invokes must carry its own certificate (isomorph-free enumeration replay or DRAT/LRAT).

**Named certified form.** For the general theorem: a formal proof (Lean/Isabelle/Coq) whose axioms and imports are auditable, with any computational lemma discharged by an independently replayable certificate. For finite/class results: an exhaustive isomorph-free digraph enumeration (nauty `directg`/orderly generation) with a per-graph Seymour-vertex check, replayable; or a formal proof for the class.

**Not accepted as resolution.**
- A proof for tournaments, or any already-covered class, presented as the general conjecture (tournaments are done - Fisher; Havet–Thomassé).
- A density result "some vertex has \(|N^{++}(v)|\ge c\,|N^{+}(v)|\)" with \(c<1\) presented as SNC (it is a partial result, however strong).
- A verification up to some \(n\) presented as a general proof (finite ranges never prove the universal statement).
- A probabilistic/heuristic argument that a random oriented graph has a Seymour vertex, offered as a proof.
- Any finite verification whose digraph enumeration is not proven complete and isomorph-free, or whose per-graph check is not independently replayable.

## 3. Graded partial-result targets

**P1 - Certified small-order verification.** Exhaustively verify that every oriented graph on \(\le n\) vertices has a Seymour vertex, pushing \(n\) as high as compute allows (the number of oriented graphs grows super-exponentially, so each additional \(n\) is a real gain). *Certificate:* a complete isomorph-free generation (nauty `directg` from all graphs, or a direct orientation enumeration) with per-graph deficiency computed exactly, a log recording the minimum \(\max_v\delta(v)\) observed, and an independent replay reproducing the graph counts (matching OEIS counts for oriented graphs). *This is the flagship finite product.*

**P2 - Reproduce the class theorems.** Independently re-verify SNC for tournaments (via the median-order / feed-vertex argument) and for other settled classes (out-degree \(\le 6\); tournaments with a small modification), with the argument written out and, where practical, formalized. *Certificate:* a written proof plus, for the computational parts, a replay; a partial Lean formalization is a strong plus.

**P3 - New graph class.** Prove SNC for a class not previously covered (e.g. a structurally defined family - certain circulant orientations, orientations with bounded independence number, near-tournaments, or graphs with a prescribed dominant vertex), with a complete proof. *Certificate:* a written proof; formalize the core if feasible; any computational case analysis carries a replay.

**P4 - Density constant.** Improve, or independently re-certify, the constant \(c\) in "every oriented graph has a vertex with \(|N^{++}(v)|\ge c\,|N^{+}(v)|\)" beyond the known \(c\approx 0.657\) (root of \(2x^3+x^2-1\)), or give an exact-arithmetic re-derivation of it. *Certificate:* an exact proof of the constant (the bound argument reduced to a certified inequality / small optimization), independently checked.

**P5 - Structural reduction.** A theorem that reduces SNC to a restricted class (e.g. reduce to strongly connected oriented graphs, to a minimal-counterexample structure, or to a local density condition), with a rigorous proof. *Certificate:* a written (ideally formalized) proof; if it enables a finite check, discharge that check with a replay.

**P6 - Weighting / median-order framework.** Formalize a general weighting or median-order framework (in the spirit of Havet–Thomassé) and prove it captures a strictly larger class than currently known, or prove a sharp two-Seymour-vertex statement for a class. *Certificate:* proof plus any computational validation replayed.

Targets P1–P4 are realistic session products; P5–P6 are ambitious; full resolution (section 2) is not expected.

## 4. Known results and prior art

- **Origin.** The conjecture is due to Paul Seymour; the tournament special case is often attributed to Dean.
- **Tournaments.** Fisher (~1996) proved the tournament case (Dean's conjecture) using a probabilistic/Farkas argument; Havet and Thomassé (~2000) gave a short combinatorial proof via **median orders** and additionally characterized when a tournament has exactly one Seymour vertex (verify).
- **Bounded out-degree.** Kaneko and Locke (early 2000s) proved SNC when the minimum out-degree is at most 6 (verify the exact bound).
- **Density constant.** Chen, Shen and Yuster (~2003) proved every digraph has a vertex with \(|N^{++}(v)|\ge \gamma\,|N^{+}(v)|\), where \(\gamma=0.657298\ldots\) is the unique real root of \(2x^3+x^2-1=0\) (verify). This is the best known general constant and is the natural target for P4.
- **Other classes / partial work.** Results are known for tournaments plus a few arcs, for graphs with a vertex of small out-degree, and for various structured families; Cohn, Godbole and collaborators studied random settings; further class results appear scattered across the literature (verify specific classes and authors before citing).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** SNC has attracted steady work; new classes and improved constants appear periodically, and the exhaustive-verification frontier (largest \(n\) checked) may have moved. Confirm the current best density constant, the settled classes, and the verification frontier before committing compute - and confirm the conjecture itself remains open in general.

## 5. Attack plan

**Finite verification (`[proof]`, computational core).** Generate all oriented graphs up to isomorphism per order with nauty: enumerate simple graphs (`geng`) and all orientations (`directg`), or use a direct isomorph-free orientation generator; for each digraph compute \(N^{+}(v)\) and \(N^{++}(v)\) exactly (bitset adjacency) and record \(\max_v\delta(v)\). The check per graph is trivial; the cost is the enumeration. Restrict soundly to the interesting cases (all out-degrees positive; up to converse/complement symmetry) with justified reductions, and log the graph counts for cross-checking against known oriented-graph counts.

**Class proofs and median orders (`[proof]`).** Reconstruct the median-order argument for tournaments and probe its reach: a median order of a digraph yields a "feed vertex" whose deficiency is controllable; identify classes where the argument or a weighting extends. Convert each promising heuristic into a stated lemma with an explicit proof obligation, and attempt a Lean 4 formalization of the tournament case as a base for extensions.

**Density constant (`[opt]`+`[proof]`).** Re-derive the \(\gamma\)-bound as a small optimization / inequality and attempt to sharpen it; any numerical optimum must be converted to an exact certified inequality (rational Positivstellensatz or an exact case analysis).

**One-workstation scope and failure modes.** A single workstation can: exhaustively verify SNC to a modest \(n\) (the super-exponential growth of oriented graphs is the hard wall - each additional vertex multiplies the count by a large factor); prove and formalize class results; and run exact small optimizations for the constant. It **cannot** verify large \(n\) by brute force, and it cannot prove the general conjecture by search. Expect: enumeration that is correct but hits the count wall quickly (careful symmetry reduction buys perhaps one or two more \(n\)); median-order arguments that extend tantalizingly but resist a clean class boundary; and constant-improvement attempts that produce numerically better but not-yet-certified bounds. Report the verification frontier \(n\) and the certified constant precisely.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All deficiency computations in exact integer arithmetic; any density constant backed by an exact certified inequality; any finite verification backed by a complete isomorph-free enumeration. Floating point is exploratory only.
2. **Independent verification.** The per-graph Seymour-vertex check is re-run by a second, independently written checker on the enumerated digraphs; the enumeration is replayed to reproduce the graph counts (matched against published oriented-graph counts); formal proofs are checked by the proof assistant's kernel.
3. **Reproducibility.** All generation commands, symmetry reductions, solver/CAS versions, seeds, and environment recorded; SHA-256 manifest over enumeration logs, certificates, and proof scripts.
4. **Preservation.** Enumeration and checking source code, and any proof scripts, are part of the record; every soundness-reducing assumption (restriction to strongly connected, to positive out-degree, symmetry quotient) is stated explicitly - the Hadamard-668 lost-source lesson.
5. **Honest reporting.** The report states up front that SNC remains open in general, reports the exact verification frontier \(n\), the classes proved, and the certified density constant, and never represents a finite verification, a class result, or a constant \(c<1\) as a proof of the conjecture.
