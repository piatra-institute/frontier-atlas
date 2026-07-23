# PROMPT FOR DETERMINING THE RAMSEY NUMBER R(4,6)

## Narrowing one of the two smallest open two-colour Ramsey numbers

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 13 of 50  
**Area:** Ramsey/extremal  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

$R(4,6)$ is the least $N$ such that every red/blue edge-colouring of $K_N$ contains a red $K_4$ or a blue $K_6$. It sits, with $R(3,10)$, as one of the two smallest two-colour Ramsey numbers still unknown; the current interval is

\[
36\le R(4,6)\le 40 .
\]

For calibration, $R(4,5)=25$ (McKay–Radziszowski, 1995) remains the largest exactly determined nontrivial two-colour Ramsey number, and it was settled by exactly the isomorph-free graph-gluing methodology this prompt deploys. The lower side of $R(4,6)$ is a construction problem - exhibit a graph on many vertices with no $K_4$ and no independent $6$-set - and is trivially checkable. The upper side is an exhaustive-nonexistence problem - show no such graph exists on $U$ vertices - settled only by a certified enumeration or a certified SAT unsatisfiability proof. The task is to **narrow the $R(4,6)$ interval with certified artifacts on either side.** The resolution standard in section 2 (the exact value with a machine-checkable nonexistence proof) is the target; every lesser result is reported as a partial result and never represented as determining $R(4,6)$.

## 1. Exact problem statement

For integers $s,t\ge2$, the Ramsey number $R(s,t)$ is the least $N$ such that every graph $G$ on $N$ vertices contains a clique of size $s$ or an independent set of size $t$; equivalently every red/blue colouring of $E(K_N)$ has a red $K_s$ or a blue $K_t$ (red $=$ edges of $G$, blue $=$ non-edges).

**Definition.** A **$(s,t;N)$-graph** (a Ramsey graph) is a graph $G$ with

\[
|V(G)|=N,\qquad \omega(G)<s,\qquad \alpha(G)<t,
\]

where $\omega$ is the clique number and $\alpha$ the independence number. Its existence certifies $R(s,t)>N$, i.e. $R(s,t)\ge N+1$. Conversely $R(s,t)\le N$ means **no** $(s,t;N)$-graph exists.

Here $s=4$, $t=6$: a **$(4,6;N)$-graph** is a $K_4$-free graph on $N$ vertices with $\alpha(G)\le 5$. Write $\mathcal{R}(4,6;N)$ for the set of such graphs up to isomorphism, and

\[
e(4,6;N)=|\mathcal{R}(4,6;N)|
\]

for their count. The complement map $G\mapsto\overline{G}$ sends a $(4,6;N)$-graph to a $(6,4;N)$-graph, so the two orientations carry the same information.

*Context.* The classical recursion $R(s,t)\le R(s-1,t)+R(s,t-1)$ (with strict inequality when both summands are even) gives finiteness and a crude ceiling; for $R(4,6)$ it yields only $R(4,6)\le R(3,6)+R(4,5)=18+25=43$, weaker than the computational $\le40$. The gap between $43$ and the true value is exactly the room that isomorph-free enumeration and SAT must close.

*Local constraints.* In a $(4,6;N)$-graph $G$, the neighbourhood $N(v)$ of any vertex induces a $(3,6)$-graph (it is triangle-free - else a $K_4$ with $v$ - and has independence $\le5$), while the non-neighbourhood induces a $(4,5)$-graph. Hence

\[
\deg(v)\ \le\ R(3,6)-1=17,\qquad N-1-\deg(v)\ \le\ R(4,5)-1=24,
\]

so every vertex satisfies $N-25\le\deg(v)\le17$; at $N=40$ this pins $15\le\deg(v)\le17$. These local Ramsey constraints are what make the gluing enumeration tractable at all.

The open question: **determine $R(4,6)$**, i.e. the least $N$ with $\mathcal{R}(4,6;N)=\varnothing$; equivalently, the sharpest certified bracket

\[
L+1\le R(4,6)\le U
\]

where a $(4,6;L)$-graph exists and no $(4,6;U)$-graph does. Convention: simple undirected graphs, no loops or multi-edges; "clique" / "independent set" refer to vertex subsets inducing complete / empty subgraphs.

## 2. Resolution standard

A **complete resolution** fixes $R(4,6)=V$ and supplies:

1. **Lower certificate.** An explicit $(4,6;V-1)$-graph as a canonical adjacency object (a graph6 string or adjacency matrix), with a verified check that $\omega\le3$ (enumerate all $4$-subsets, none a clique) and $\alpha\le5$ (enumerate all $6$-subsets, none independent), or an equivalent certified clique / independence solver.
2. **Upper certificate.** A proof that $\mathcal{R}(4,6;V)=\varnothing$, in one of two certified forms:
   - (a) an **exhaustive isomorph-free enumeration** showing no $(4,6;V)$-graph survives, produced by a canonical-augmentation / gluing pipeline (nauty/Traces lineage) with a replayable generation record and an independent recount; or
   - (b) a **SAT unsatisfiability proof** (DRAT/LRAT) for a CNF encoding "$\exists$ a $(4,6;V)$-graph", checked by an independent proof checker, with an encoding-fidelity argument.

**Not accepted as resolution.**

- A record $(4,6)$-graph alone (bounds only the lower side).
- An upper bound asserted from a solver's UNSAT print with no preserved, independently checked DRAT/LRAT trace.
- An enumeration whose isomorph-rejection completeness is not argued and independently reconstructed (partial catalogues are not nonexistence proofs).
- A bound imported from the survey or a "personal communication" figure without reproducing a certificate at our standard.
- A probabilistic, semidefinite, or flag-algebra *numerical* bound reported as the exact value (such bounds are legitimate partial results - see P5 - but are not $R(4,6)$).
- A nonexistence proved only for a restricted graph class (circulants, regular graphs) presented as the unrestricted $\mathcal{R}(4,6;V)=\varnothing$.
- Matching an OEIS / survey number without an on-machine artifact.

Honest calibration: full determination of $R(4,6)$ is **unlikely** on one workstation. The nonexistence side at the true value defeated the McKay–Radziszowski machinery for decades; $R(4,5)=25$ took a landmark effort. The realistic product is a certified lower-bound reproduction / improvement and certified enumeration data at accessible orders.

## 3. Graded partial-result targets

**P1 - Reproduce the frontier.** Re-derive $R(4,5)=25$ with our toolchain:

- verify a $(4,5;24)$-graph (a Ramsey graph on $24$ vertices, $\omega\le3$, $\alpha\le4$);
- reproduce the nonexistence $\mathcal{R}(4,5;25)=\varnothing$ (or a documented partial re-enumeration if the full run is out of budget), matching published counts $e(4,5;N)$ where available.

*Certificate:* verified $(4,5;24)$-graph; enumeration / recount record with SHA-256 manifest. Validates the pipeline against a known answer.

**P2 - Certify the record lower bound.** Reproduce and independently verify an explicit $(4,6;35)$-graph, giving $R(4,6)\ge36$ (Exoo's construction; see section 4). *Certificate:* the graph in graph6, a standalone checker confirming $\omega\le3$ and $\alpha\le5$ by exhaustive subset scan, plus the isomorphism-class hash.

**P3 - Improve the lower bound.** Search for a $(4,6;36)$-graph (would give $R(4,6)\ge37$). Restrict to structured families first, then broaden:

- circulant and Cayley graphs on $\mathbb{Z}_{36}$ and small groups;
- cyclic colourings and vertex-transitive constructions;
- local-search (simulated annealing / tabu) perturbations of the record graph.

*Certificate:* a verified $(4,6;36)$-graph (as in P2) with the search source preserved; a *negative* result on a restricted family is itself recorded as a certified partial (e.g. "no circulant $(4,6;36)$-graph on $\mathbb{Z}_{36}$", with the enumeration).

**P4 - Certified enumeration data toward the upper bound.** Produce complete isomorph-free catalogues $\mathcal{R}(4,6;N)$ and counts $e(4,6;N)$ for the largest $N$ reachable, by canonical-augmentation gluing of $K_4$-free graphs with bounded independence. *Certificate:* the catalogue with generation record and an independent recount (a second canonical form, e.g. Traces vs. nauty); counts cross-checked against any published $e(4,6;N)$.

**P5 - Upper-bound progress.** Either

- (a) a certified $\mathcal{R}(4,6;39)=\varnothing$ (would give $R(4,6)\le39$) via gluing or SAT with a checked proof - the hard research target; or
- (b) an improved *analytic / SDP / flag-algebra* upper bound with a machine-verified numerical core, reported as a bound (not the exact value).

*Certificate:* enumeration nonexistence record or checked DRAT/LRAT trace for (a); a verified rational SDP certificate / flag-algebra dual for (b).

**P6 - Strongest result short of resolution.** A certified bracket narrower than $36\le R(4,6)\le40$ - an improved lower bound with a verified graph, or an improved upper bound with a certified nonexistence - or a full determination meeting section 2 (windfall). *Certificate:* both directional certificates at the section-2 standard for the claimed bracket.

## 4. Known results and prior art

- **Calibration value.** $R(4,5)=25$ - **McKay and Radziszowski** (1995), by isomorph-free extension and gluing; the largest exactly known nontrivial two-colour Ramsey number.
- **Lower bound.** $R(4,6)\ge36$, from a $(4,6;35)$-graph found by **Geoffrey Exoo** (c. 2012), who exhibited multiple $(4,6;35)$-graphs (verify the exact record and count). Earlier lower bounds (Exoo and others) climbed through the low $30$s over prior decades.
- **Upper bound.** $R(4,6)\le40$ - **Angeltveit and McKay** (c. 2019–2024), improving the long-standing $R(4,6)\le41$ (McKay–Radziszowski era). Reported via the *Small Ramsey Numbers* dynamic survey and personal communication; re-verify the current figure and its documentation.
- **Status of the case.** $R(4,6)$ and $R(3,10)$ are the two smallest two-colour Ramsey numbers not yet determined - a well-known statement in the survey.
- **Survey and methods.** **Radziszowski**, *Small Ramsey Numbers* (Electron. J. Combin. Dynamic Survey DS1; latest revision 2024, verify) is the authoritative table of bounds and constructions. The core method is McKay's canonical-augmentation isomorph-free generation, implemented in **nauty/Traces** (McKay–Piperno); SAT and SDP / flag-algebra provide alternative upper-bound routes.
- **Data cross-checks.** McKay's public Ramsey-graph data pages list representatives and counts $e(4,t;N)$ for many classes; these are the external ground truth for the P1/P2 reproductions and for validating any new $e(4,6;N)$.
- **Sibling context.** $R(4,6)$ shares its calibration case $R(4,5)=25$ and its entire gluing / SAT toolchain with $R(3,10)$ (problem 14) and the multicolour numbers (problem 15); progress on any one sharpens the pipeline for the others.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Re-check the exact lower-bound record (is it still $\ge36$?), the upper bound (still $\le40$? any 2024–2026 improvement?), and whether new enumeration counts $e(4,6;N)$ have been published.

## 5. Attack plan

**Isomorph-free enumeration and gluing (`[search]`).** Use **nauty/Traces**: `geng` with degree / edge constraints to generate $K_4$-free graphs; canonical-augmentation gluing (à la McKay–Radziszowski) to extend $(4,6;N)$-graphs to order $N+1$, rejecting isomorphs by canonical form. Track $e(4,6;N)$ and cross-check with a second canonical labeler. This is the P1 / P4 workhorse.

**SAT nonexistence (`[search]`).** Encode "$\exists$ a $(4,6;N)$-graph" as CNF: a Boolean edge variable $x_{ij}$ per pair $\{i,j\}$; for every $4$-subset $Q$ a clause forbidding a clique, and for every $6$-subset $S$ a clause forbidding an independent set:

\[
\bigvee_{\{i,j\}\subseteq Q}\lnot x_{ij}\quad(\text{no }K_4),\qquad
\bigvee_{\{i,j\}\subseteq S} x_{ij}\quad(\text{no independent }6\text{-set}).
\]

Break symmetry with a canonical / lex-leader predicate (proved satisfiability-preserving). Solve with **CaDiCaL** / **kissat**, log **DRAT**, convert to **LRAT**, check with `drat-trim` / `dpr-trim`. Feasible for modest $N$; the true $U$ is likely out of direct reach - pivot to restricted / conditional lemmas. At order $N=40$ the flat model has $\binom{40}{2}=780$ edge variables and

\[
\binom{40}{4}=91{,}390\ \text{(no-}K_4\text{)},\qquad \binom{40}{6}=3{,}838{,}380\ \text{(no-independent-}6\text{)}
\]

clauses; the independent-set clauses dominate, so lazy / incremental independence constraints or a neighbourhood-decomposition (gluing) hybrid usually beats the flat CNF.

**Constructions for lower bounds (`[search]`).** Circulant and Cayley graphs on $\mathbb{Z}_N$ and small groups; cyclic colourings; local search (simulated annealing / tabu) over adjacency matrices minimizing $(K_4,\overline{K_6})$ violations; seed from Exoo's $(4,6;35)$-graph. Verify every candidate exactly.

**CAS support.** **SageMath** for clique / independence certification, automorphism groups, and structure mining of good graphs; a standalone C++ / Python checker (exhaustive $4$- and $6$-subset scan, or a certified clique solver) is the load-bearing verifier and is independent of the search code.

**One-workstation scope.** Feasible: exact verification of any candidate graph on tens of vertices (sub-second); circulant / Cayley searches at $N=36$–$40$; enumeration of $\mathcal{R}(4,6;N)$ for small $N$; SAT nonexistence for small $N$ and restricted lemmas. **Out of scope:** a full unconditional nonexistence at $N=39$ or $40$ is very likely beyond one machine. **Failure modes:** combinatorial explosion in gluing (bound the search by degree / neighbourhood structure, checkpoint); SAT timeouts on large $N$ (restrict to structured subclasses, report conditionally); local-search plateaus (diversify seeds, use the record graph as a base); isomorph-rejection bugs (dual canonical forms and recount catch them).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Lower bounds are graphs checked by exhaustive $4$-/$6$-subset scans (or certified clique / independence solvers); upper bounds are either isomorph-free enumerations with a completeness argument or DRAT/LRAT proofs checked by an independent checker. Floating point (in any SDP route) is admitted only through a rational / interval certificate; solver "UNSAT" prints are never certification by themselves.
2. **Independent verification.** The graph checker is written independently of the search / encoder. Enumeration completeness is re-established by an independent recount and a second canonical labeler (nauty vs. Traces); SAT traces are checked by a checker not derived from the solver. Encoding-fidelity arguments accompany every CNF.
3. **Reproducibility.** All generators, gluing scripts, CNF encoders, solver / nauty versions and flags, seeds, and environment are recorded; a SHA-256 manifest covers every graph, catalogue, CNF, proof trace, and log.
4. **Preservation.** All search and enumeration source is part of the record (the Hadamard-668 lost-source lesson). Any artifact too large to store (e.g. a giant enumeration stream) is named with a documented protocol to regenerate and spot-check it, never silently dropped.
5. **Honest reporting.** The report states up front whether $R(4,6)$ was determined (very likely not) and reports each result at its true strength - "certified $R(4,6)\ge36$", "complete enumeration $e(4,6;N)=\dots$", "flag-algebra upper bound" - never presenting a record graph, a restricted enumeration, or a numerical bound as the value of $R(4,6)$.
