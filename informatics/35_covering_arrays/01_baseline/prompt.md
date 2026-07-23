# PROMPT FOR A CERTIFIED-OPTIMAL COVERING ARRAY OR AN IMPROVED BOUND

## Exact values of the covering array number \(\mathrm{CAN}(t,k,v)\) for specific parameters

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 35 of 50  
**Area:** discrete dynamics & pattern search  
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A covering array \(\mathrm{CA}(N;t,k,v)\) is an \(N\times k\) array over a \(v\)-symbol alphabet such that every choice of \(t\) columns contains, among its \(N\) rows, all \(v^{t}\) possible \(t\)-tuples. The **covering array number** \(\mathrm{CAN}(t,k,v)\) is the least \(N\) for which one exists. These arrays are the backbone of combinatorial interaction testing - every \(t\)-way combination of \(k\) parameters is exercised in \(N\) tests - and many exact values remain open even for strength \(t=2,3\). The problem is squarely machine-checkable: an *upper bound* is an explicit array whose coverage is verified by scanning all \(\binom{k}{t}\) column-sets, and a *lower bound* is the infeasibility of "a \(\mathrm{CA}(N-1;t,k,v)\) exists", provable by SAT with a DRAT/LRAT trace or by exhaustive isomorph-free enumeration. This matches AI methods - certified construction plus certified infeasibility / exhaustive classification. The on-machine verifier that closes the loop is a coverage checker (upper) and an independently checked UNSAT proof or completed enumeration (lower). This problem is kept deliberately distinct from *covering codes* (owned by the mathematics program). Anything short of Section 2 - a heuristic array with no matching lower bound, an unchecked solver run - is a partial result, never a solution.

## 1. Exact problem statement

Fix strength \(t\ge2\), number of columns (factors) \(k\ge t\), and alphabet size \(v\ge2\). An \(N\times k\) array \(A\) over \(\{0,\dots,v-1\}\) is a **covering array** \(\mathrm{CA}(N;t,k,v)\) iff

\[
\forall\, C\in\binom{[k]}{t}\ \ \forall\, \tau\in\{0,\dots,v-1\}^{t}\ \ \exists\, \text{row } r:\quad A[r,C]=\tau .
\]

That is, every \(t\)-subset of columns, restricted to the \(N\) rows, realises all \(v^{t}\) tuples (index 1: each covered at least once). Define

\[
\mathrm{CAN}(t,k,v)=\min\{\,N : \text{a } \mathrm{CA}(N;t,k,v)\ \text{exists}\,\}.
\]

**Basic bounds.**

\[
\mathrm{CAN}(t,k,v)\ge v^{t},
\qquad
\mathrm{CAN}(t,k,v)\ge v\cdot \mathrm{CAN}(t-1,k-1,v),
\qquad
\mathrm{CAN}(t,k,v)\le \mathrm{CAN}(t,k+1,v).
\]

If a suitable **orthogonal array** \(\mathrm{OA}(v^{t};t,k,v)\) exists then \(\mathrm{CAN}=v^{t}\) exactly. The binary strength-2 case is solved (Section 4); most higher-\(v\) or higher-\(t\) cases are not.

**The open question.** For a specified \((t,k,v)\), determine \(\mathrm{CAN}(t,k,v)\) exactly - a construction meeting a matching lower bound - or strictly improve a standing bound. Every array, coverage check, and infeasibility claim is finite and exactly decidable. The most tractable open cells are ternary strength two and small ternary/quaternary strength three,

\[
\mathrm{CAN}(2,k,3),\quad \mathrm{CAN}(3,k,3),\quad \mathrm{CAN}(3,k,4)\qquad (\text{small } k),
\]

where the SAT/enumeration window is still within one workstation and table gaps or uncertified "best-known" entries remain.

**Coverage budget.** An \(N\times k\) array over \(v\) symbols offers, per column-\(t\)-set, \(N\) rows to realise \(v^{t}\) required tuples, so a necessary counting condition is that redundancy be non-negative:

\[
\text{each } C\in\binom{[k]}{t}\ \text{needs all } v^{t}\ \text{tuples among } N\ \text{rows}\ \Rightarrow\ N\ge v^{t},
\]

and interaction-testing utility comes precisely from \(N\) being far below the naive \(v^{k}\) exhaustive test suite. The optimisation is: cover all \(\binom{k}{t}v^{t}\) required interactions with as few rows as possible.

**Model fixings.** Index 1 (each tuple at least once), uniform alphabet size \(v\) across columns (no mixed-level / variable-strength arrays unless separately declared), strength exactly \(t\). Changing any of these changes the object and must be stated.

## 2. Resolution standard

Two certified halves.

- **Upper bound (construction).** An explicit \(N\times k\) array with a **coverage certificate**: a deterministic scan over all \(\binom{k}{t}\) column-subsets confirming every one of the \(v^{t}\) tuples appears. This proves \(\mathrm{CAN}(t,k,v)\le N\).
- **Lower bound (infeasibility).** A certificate that no \(\mathrm{CA}(N-1;t,k,v)\) exists: a **DRAT/LRAT-checked UNSAT** of the SAT encoding of existence, or a **completed isomorph-free exhaustive enumeration** with a replayable completeness log. This proves \(\mathrm{CAN}(t,k,v)\ge N\).

**Resolution of \(\mathrm{CAN}(t,k,v)\)** is a matching pair,

\[
\mathrm{CA}(N;t,k,v)\ \text{exists (coverage-certified)} \ \wedge\ \mathrm{CA}(N-1;t,k,v)\ \text{infeasible (checked)}
\ \Longrightarrow\ \mathrm{CAN}(t,k,v)=N .
\]

Named endpoint objects: a **coverage-certified covering array** and a **certified optimality proof** (checked infeasibility of \(N-1\)). **Bound improvement** = a strict improvement to one certified side, the other cited by value, source (e.g. the Colbourn tables), and access date.

**Not accepted as resolution.**

- A metaheuristic/simulated-annealing array reported as "optimal" with no matching lower bound (a good construction alone never settles \(\mathrm{CAN}\)).
- An array whose coverage is asserted but not verified by the exhaustive column-set/tuple scan.
- A lower bound stated by a formula or "our search found nothing smaller" without a DRAT/LRAT UNSAT proof or a completed isomorph-free enumeration with a completeness argument.
- A solver "UNSAT" or ILP "optimal" flag without an exact certificate.
- Silently changing the definition (higher index \(\lambda>1\), mixed/variable-strength, or "don't-care" coverage) while claiming a result for the standard index-1 \(\mathrm{CAN}\).
- Conflating this with covering *codes* / covering radius (a different object owned by the mathematics program).
- A composite array from a recursive construction whose coverage is inferred from the construction lemma but not re-verified by a full column-set/tuple scan (the scan is cheap and catches lemma-application errors).
- Any result whose array, encoding, or proof cannot be regenerated deterministically from the recorded inputs and solver version.

## 3. Graded partial-result targets

- **P1 - Verifier + table reproduction.** Build the coverage checker; reproduce known exact \(\mathrm{CAN}\) values from the Colbourn tables (e.g. small binary strength-2, small \(v=3\) strength-2 cases) with coverage-certified arrays. *Certificate:* coverage scans plus a sourced table comparison with access date.
- **P2 - Optimality for a small case.** For a small \((t,k,v)\) whose exact value \(N\) is known, produce the matching lower bound yourself,

\[
\mathrm{CA}(N;t,k,v)\ \text{exists}\ \wedge\ \mathrm{CA}(N-1;t,k,v)\ \text{UNSAT (checked)},
\]

by a DRAT/LRAT UNSAT of \(N-1\) or a completed enumeration. *Certificate:* the array plus the checked infeasibility/enumeration.
- **P3 - New optimal value.** For a \((t,k,v)\) with a gap in the tables, close it: a coverage-certified array meeting a checked lower bound. *Certificate:* the matching pair.
- **P4 - Improved upper bound.** A smaller coverage-certified array than the standing best-known for some \((t,k,v)\). *Certificate:* coverage scan plus sourced table comparison.
- **P5 - Improved lower bound.** A checked infeasibility pushing \(\mathrm{CAN}(t,k,v)\) above the previous certified lower bound. *Certificate:* DRAT/LRAT UNSAT or completed enumeration with completeness log.
- **P6 - Classification.** For a small \((t,k,v)\), an isomorph-free classification of *all* optimal (or minimum-plus-one) covering arrays, not just one witness. *Certificate:* the enumeration, its canonical-form generator, and an independent replay.
- **P7 - Bound-propagation.** Use a newly certified small value to certify a family via the recursive inequalities (e.g. \(\mathrm{CAN}(t,k,v)\ge v\,\mathrm{CAN}(t-1,k-1,v)\) or a product upper bound), each derived value checked end-to-end. *Certificate:* the seed certificate plus a machine-checked derivation for every propagated entry.

## 4. Known results and prior art

- **Binary strength 2 (solved).** \(\mathrm{CAN}(2,k,2)\) is known exactly for all \(k\): it equals the least \(N\) with

\[
k\le \binom{N-1}{\lceil N/2\rceil},
\]

the Rényi / Kleitman–Spencer / Katona result (~1971–1973). This is the model of a fully certified case.
- **Strength 3, \(v=2\).** Exact values are known for all \(k\) in the binary strength-3 case (verify the precise reference and statement).
- **Orthogonal-array meetpoints.** Whenever an \(\mathrm{OA}(v^{t};t,k,v)\) exists (e.g. from MDS codes / finite-field constructions), \(\mathrm{CAN}(t,k,v)=v^{t}\) exactly; these anchor many table entries.
- **Tables and trackers.** Charles J. Colbourn maintains the covering array tables (best-known upper bounds; a November 2024 status covers \(2\le v\le25\), \(2\le t\le6\), \(t\le k\le10000\)). NIST's covering-array tables (D. Richard Kuhn, Raghu Kacker, and collaborators) track best-known sizes for interaction testing. Treat every entry as a live, re-verifiable best-known, not a proven optimum unless flagged as such.
- **Constructions and search.** Orderly/canonical exhaustive algorithms for optimal small arrays (Colbourn, Nayeri, Konjevod, and others, ~2010s, verify); metaheuristics (José Torres-Jiménez and collaborators) for best-known upper bounds; SAT and constraint-programming existence tests (Hnich, Prestwich, and others; Kari Kokkala and Patric Östergård for classification-style exact results, verify). "New covering array numbers" and related papers report exact-value improvements (verify specific parameters and years).
- **SAT/CP for exact small values.** Existence of \(\mathrm{CA}(N;t,k,v)\) is a natural SAT/CP decision problem, and modern solvers with symmetry-breaking have certified several exact values and non-existence results; DRAT proof logging is what turns a solver "UNSAT" into an auditable lower bound (verify which specific \((t,k,v)\) have certified optima).
- **Open frontier.** Many exact values are open even at \(t=2\) with \(v\ge3\) and at \(t=3\); the gap between best-known upper bounds and certified lower bounds is where the work is.

Never cite an author, date, table entry, or exact value you have not re-checked; the "(verify)" markers are exactly the items to confirm. Combinatorial-design records move fast. **Status as of mid-2026 - re-verify against the current literature and the Colbourn/NIST tables before starting any session, recording the table version and access date.**

## 5. Attack plan

`[search]` `[opt]` - concrete first computations on one workstation.

1. **Coverage checker first.** Implement the exhaustive column-set/tuple scan; cheap and load-bearing for every upper bound.
2. **Existence as SAT.** Encode "a \(\mathrm{CA}(N;t,k,v)\) exists": a Boolean per cell (one-hot over \(v\) symbols) plus a covering clause per (column-set, tuple),

\[
\bigvee_{r=1}^{N}\ \bigl[\,A[r,C]=\tau\,\bigr]
\qquad \text{for every } C\in\binom{[k]}{t},\ \tau\in\{0,\dots,v-1\}^{t},
\]

with row/column/symbol symmetry-breaking. Solve with CaDiCaL/kissat; SAT gives a construction, UNSAT (with logged DRAT) gives \(\mathrm{CAN}>N\).
3. **Optimality sweep.** For fixed \((t,k,v)\), decrement \(N\) until infeasibility,

\[
N^{*}=\min\{N:\ \mathrm{CA}(N;t,k,v)\ \text{SAT}\},\qquad \mathrm{CAN}=N^{*}\ \text{once } N^{*}-1\ \text{is a checked UNSAT},
\]

so the largest UNSAT plus a coverage-certified array at \(N^{*}\) pins the value.
4. **Exhaustive classification.** For the smallest cases, run orderly/canonical generation (isomorph rejection under the row/column/symbol symmetry group) to classify all optimal arrays (P6).
5. **ILP alternative.** Model as a set-cover ILP (SCIP with exact rational / infeasibility certificates) as an independent second route for both bounds.
6. **Recursive constructions.** Use the product / Roux-type and column-augmentation constructions to build large-\(k\) upper bounds from small certified seeds; verify the composite array by full coverage scan, never by trusting the construction lemma alone.

One-workstation scope: SAT/ILP optimality is feasible for small \(k\) and modest \(N\); it blows up quickly with \(k\), \(t\), and \(v\) - bound and report the parameter window. **Failure modes:** SAT blow-up and weak symmetry-breaking; solver flags without exact certificates; coverage-checker errors on the column-subset enumeration; definition drift (index, mixed strength); non-canonical enumeration (double counting or omissions).

## 6. Verification and auditability requirements

1. **Exact/certified computation.** Every upper bound rests on an exhaustive coverage scan; every lower bound on a DRAT/LRAT UNSAT proof or a completed isomorph-free enumeration. Solver status flags alone are never load-bearing; heuristic optima are exploration only.
2. **Independent verification.** Each coverage certificate is re-checked by a second, separately written scanner; each UNSAT/optimality proof is checked by a standalone checker (`drat-trim` / `lrat-check`, or an exact ILP certificate verifier) and, for headline claims, re-derived with a second solver or a second independent enumeration.
3. **Reproducibility.** The full encoding (variables, covering clauses, symmetry-breaking), solver and checker versions, seeds, the array itself, and the exact \((t,k,v,N)\) are recorded; SHA-256 manifest over every artifact; each bound being improved is cited with value, source (Colbourn/NIST table version), and access date.
4. **Preservation.** Construction/search source, encoders, and all proof traces are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front whether an exact \(\mathrm{CAN}\) value was certified, a bound was strictly improved (and on which side), or only reproduction was achieved, and in which model (standard index-1 \(\mathrm{CAN}\)). A heuristic array without a matching lower bound, an unchecked UNSAT, or a covering-codes conflation is never represented as a certified covering-array result.
