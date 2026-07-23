# PROMPT FOR PINNING THE SHORTEST SUPERPERMUTATION ON SIX SYMBOLS

## Certified upper and lower bounds on \(s(n)\), starting with the open value \(s(6)\)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 34 of 50  
**Area:** discrete dynamics & pattern search  
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A *superpermutation* on \(n\) symbols is a string over \(\{1,\dots,n\}\) that contains every one of the \(n!\) permutations as a contiguous substring; \(s(n)\) is the length of the shortest such string. The value is known exactly only for \(n\le5\) (with \(s(5)=153\)); for \(n\ge6\) it is **open**. The problem sits between a constructive upper bound and a combinatorial lower bound - the celebrated anonymous lower bound \(n!+(n-1)!+(n-2)!+n-3\), later written up by Houston, Pantone, Vatter and others, and constructive upper bounds that for \(n=6\) reach length 872 (Houston), below the once-conjectured \(\sum_{i\le n} i!=873\). The gap is small and machine-checkable: an upper bound is a *string* whose superpermutation property is verified by scanning all \(n!\) permutations, and a lower bound is a graph/SAT statement whose infeasibility is DRAT/LRAT-checkable. This matches AI search - exact construction plus certified infeasibility. The on-machine verifier that closes the loop is a substring-coverage checker (upper) and an independently checked UNSAT / optimality proof (lower). Anything short of Section 2 - an unverified string, an unchecked "no shorter exists" claim, a heuristic optimum - is a partial result, never a solution.

## 1. Exact problem statement

Fix \(n\ge1\) and alphabet \(\Sigma=\{1,\dots,n\}\). A string \(w\in\Sigma^{*}\) is a **superpermutation** on \(n\) symbols iff for every permutation \(\pi\) of \(\Sigma\) the length-\(n\) word \(\pi\) occurs as a contiguous substring of \(w\). Define

\[
s(n)=\min\{\,|w| : w\ \text{is a superpermutation on }n\ \text{symbols}\,\}.
\]

**Graph formulation.** Build the directed graph \(G_n\) on the \(n!\) permutation-vertices, with a weighted edge \(\pi\to\pi'\) whose cost is the least number of symbols appended to \(\pi\) to reach an occurrence of \(\pi'\); a superpermutation is a walk visiting every vertex, and

\[
|w| = n + \sum(\text{edge costs along the walk}),
\qquad
s(n)=n!+\min_{\text{covering walk}}\ \sum(\text{extra cost}).
\]

Consecutive permutations differing by "drop the first symbol, append one" incur cost 1 (a 1-overlap of \(n-1\) symbols); larger jumps cost more. Minimising \(|w|\) is a shortest covering-walk / asymmetric-TSP-type problem on \(G_n\).

**Known exact values.**

\[
s(1)=1,\quad s(2)=3,\quad s(3)=9,\quad s(4)=33,\quad s(5)=153,
\qquad s(n)=\textstyle\sum_{i=1}^{n} i!\ \ (n\le5).
\]

This "sum-of-factorials" pattern **fails** at \(n=6\) (see Section 4).

**Instance sizes.** The regime is right at the edge of exact methods:

\[
n=6:\ \ 6!=720\ \text{permutations},\quad \text{target length}\ \sim 872,\quad \text{alphabet } 6;
\qquad
n=7:\ \ 7!=5040,\quad \text{length}\ \gtrsim 5900 .
\]

For \(n=6\) a length-\(L\) SAT model has on the order of \(6L\) symbol variables plus the coverage constraints for all \(720\) permutations - large but plausibly within reach for the single decisive value \(L=871\); \(n=7\) exact optimality is out of scope.

**The open question.** Determine \(s(n)\) for \(n\ge6\), beginning with \(n=6\): either pin \(s(6)\) to an exact value with a certified matching upper and lower bound, or strictly narrow the certified bracket. All objects are finite strings and finite graphs; every claim is exactly decidable.

## 2. Resolution standard

Two certified halves, each independently checkable.

- **Upper bound (construction).** An explicit string \(w\) over \(\{1,\dots,n\}\) with a **coverage certificate**: a deterministic scan confirming

\[
\forall\, \pi\in \mathfrak S_n:\quad \pi\ \text{occurs as a length-}n\ \text{substring of } w,
\]

and \(|w|\) reported. This proves \(s(n)\le|w|\).
- **Lower bound (infeasibility).** A **certified no-shorter proof**: a DRAT/LRAT-checked UNSAT of the SAT/ILP encoding "a superpermutation of length \(\le L-1\) exists", or an exhaustive covering-walk search with a replayable completeness log, proving \(s(n)\ge L\).

**Resolution of \(s(n)\)** is a matching pair,

\[
s(n)\le L\ (\text{upper string}) \quad\wedge\quad s(n)\ge L\ (\text{checked infeasibility}) \ \Longrightarrow\ s(n)=L .
\]

The named endpoint objects: an **overlap-certified superpermutation** (string plus coverage scan) and a **certified length lower bound** (checked infeasibility). **Bracket improvement** = a strict improvement to either certified side, with the other side cited by value, source, and access date.

**Not accepted as resolution.**

- A construction whose superpermutation property is asserted but not verified by an exhaustive permutation-coverage scan.
- A lower bound stated as a formula or "our search found nothing shorter" without a DRAT/LRAT UNSAT proof or a replayable exhaustive-search completeness argument.
- Presenting the anonymous/Houston lower-bound *formula* as if it settled \(s(6)\): for \(n=6\) it gives 867, which does **not** match the 872 upper bound - the value is not pinned by the formula.
- Repeating a community "\(s(6)=872\)" claim as established: the exactness of \(s(6)\) has been *claimed* but not, to date, independently certified; treat it as open until a checked no-length-871 proof exists.
- A heuristic/ILP optimum reported without an exact certificate (an ILP must yield an exact rational or DRAT-checked infeasibility certificate, not a solver "optimal" flag alone).
- A superpermutation on \(n\) symbols that silently uses a different alphabet size, allows non-contiguous "substrings", or requires each permutation only once *as a set* while double-counting - the definition (contiguous, all \(n!\), over exactly \(n\) symbols) must be held fixed.
- Any result whose construction or infeasibility proof cannot be regenerated deterministically from the recorded encoding and solver version.

## 3. Graded partial-result targets

- **P1 - Verifier + small-case reproduction.** Build the coverage checker and the graph model; re-derive \(s(n)\) for \(n\le5\) exactly (construction plus certified optimality), confirming \(s(5)=153\). *Certificate:* coverage scans and a checked optimality proof for \(n=5\).
- **P2 - \(n=6\) upper-bound reproduction.** Reproduce a length-872 superpermutation on 6 symbols and verify it with the coverage checker. *Certificate:* the string plus its exhaustive coverage scan; \(|w|=872\) confirmed.
- **P3 - \(n=6\) lower-bound certification.** Certify a lower bound for \(s(6)\): a DRAT/LRAT-checked proof that no superpermutation of length \(\le L-1\) exists, pushing \(L\) up from the formula value 867 toward 872. *Certificate:* encoding plus checked UNSAT trace at each \(L\).
- **P4 - Pin \(s(6)\).** Close the bracket: certified upper 872 (P2) and a checked lower proof that 871 is impossible,

\[
s(6)\le 872\ \wedge\ \bigl(\nexists\ \text{superpermutation of length } 871\bigr)\ \Longrightarrow\ s(6)=872,
\]

with an independent, replayable certificate. *Certificate:* the matching pair.
- **P5 - Improve \(n=7\) bounds.** Strictly improve the certified upper or lower bound for \(s(7)\), with the counterpart bound sourced. *Certificate:* coverage scan (upper) or checked infeasibility/partial lower bound.
- **P6 - Structural lower-bound tooling.** Turn the anonymous/Houston counting argument into a machine-checked lower-bound proof (formalised or DRAT-backed) reusable across \(n\). *Certificate:* the formal/checked proof artifact.
- **P7 - Palindromicity/structure audit of the 872 string.** Independently confirm structural claims made about the length-872 object (e.g. its overlap profile and any symmetry), as a check on the upper-bound artifact. *Certificate:* a machine-checked structural report tied to the verified string.

## 4. Known results and prior art

- **Exact small values.** \(s(n)=\sum_{i\le n} i!\) for \(n\le5\); in particular \(s(5)=153\). Aaron Williams, Nathaniel Johnston and others analysed the \(n\le5\) regime; the sum-of-factorials conjecture was believed to hold generally.
- **Upper bound falls at \(n=6\).** Robin Houston (2014) exhibited a superpermutation on 6 symbols of length **872**, one shorter than the conjectured \(873=\sum_{i\le6} i!\), disproving the conjecture. See "Tackling the Minimal Superpermutation Problem" (Houston and collaborators), arXiv:1408.5108 (2014, verify the author list). Greg Egan (2018) gave an improved general construction with upper bound

\[
s(n)\ \le\ n!+(n-1)!+(n-2)!+(n-3)!+n-3 \qquad (\text{verify}).
\]

- **Lower bound.** The famous anonymous "4chan" lower bound, later formalised and published (Houston, Jay Pantone, Vince Vatter, and others, ~2018–2019, verify), gives

\[
s(n)\ \ge\ n!+(n-1)!+(n-2)!+n-3 .
\]

- **\(n=6\) bracket.** For \(n=6\) the lower-bound formula is \(720+120+24+6-3=867\), and Houston's construction gives \(872\), so

\[
867\ \le\ s(6)\ \le\ 872 .
\]

A stronger claim - that \(s(6)=872\) exactly (no length-871 superpermutation) - was **claimed** by Cole Fritsch (~February 2021) via a computer search reporting no length-871 result plus a lower-bound write-up, but that write-up is provisional and, as of this prompt, not independently certified. Treat \(s(6)\) as open pending a checked no-871 proof (verify the current status).
- **Context.** The problem is a large asymmetric-TSP / shortest-covering-walk instance on the permutation overlap graph; OEIS A180632 tracks the sequence; Numberphile popularised the anonymous lower bound.

Never cite an author, date, arXiv identifier, or record you have not re-checked; the "(verify)" markers are exactly the items to confirm. CS records move fast. **Status as of mid-2026 - re-verify against the current literature (arXiv, OEIS A180632, the superpermutators mailing list) before starting any session; in particular re-check whether \(s(6)\) has been independently pinned.**

## 5. Attack plan

`[search]` `[opt]` - concrete first computations on one workstation.

1. **Coverage checker first.** Implement the exhaustive substring-coverage verifier - a rolling scan marking each of the \(n!\) permutations seen. Cheap and load-bearing for every upper bound.
2. **Graph/covering-walk model.** Build \(G_n\); the shortest superpermutation is a minimum-cost covering walk. For \(n\le6\) the vertex count (\(720\)) is tractable; encode as ILP (SCIP with exact rational certificates / QSopt\_ex) or as length-bounded SAT.
3. **Upper bounds.** Reconstruct Houston's 872 string and Egan's construction; verify by coverage scan. Explore improved constructions for \(n=7\).
4. **Lower bounds.** Encode "superpermutation of length \(\le L\) exists" as SAT and solve with CaDiCaL/kissat, logging DRAT for UNSAT; sweep \(L\) upward toward the construction length,

\[
L = 867,\ 868,\ \dots,\ 871 \quad (\text{each UNSAT tightens } s(6)\ge L+1),
\]

with exact ILP infeasibility certificates (SCIP / SoPlex exact) as the independent alternative. The no-871 instance for \(n=6\) is the headline target.
5. **Structural argument.** Reimplement the anonymous/Houston counting lower bound and, where feasible, formalise it (Lean 4) or reduce it to a checkable finite computation, to reuse across \(n\).
6. **Symmetry.** Fix the first permutation to the identity (a superpermutation can be relabelled), pruning the \(n!\) symmetry of the alphabet; every symmetry break used in a lower-bound encoding must be proved to preserve satisfiability.

One-workstation scope: \(n\le6\) upper-bound verification is trivial; the \(n=6\) length-871 UNSAT is the ambitious but plausibly feasible target; \(n\ge7\) exact optimality is out of reach - pursue bounds. **Failure modes:** SAT/ILP blow-up as \(L\) grows; solver "optimal"/"UNSAT" flags without exact certificates; coverage-checker off-by-one at string boundaries; conflating the lower-bound *formula* with a proof of exactness.

## 6. Verification and auditability requirements

1. **Exact/certified computation.** Every upper bound rests on an exhaustive coverage scan; every lower bound on a DRAT/LRAT UNSAT proof or an exact ILP infeasibility certificate. Solver status flags alone are never load-bearing.
2. **Independent verification.** Each coverage certificate is re-checked by a second, separately written scanner; each UNSAT/infeasibility proof is checked by a standalone checker (`drat-trim` / `lrat-check`, or an exact LP certificate verifier) and, for headline claims, re-derived with a second solver.
3. **Reproducibility.** The full encoding (graph construction, length bound, symmetry-breaking), solver and checker versions, seeds, and the exact string are recorded; SHA-256 manifest over every artifact; each bound being improved is cited with value, source, and access date.
4. **Preservation.** Construction code, encoders, search source, and all proof traces are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front whether \(s(6)\) was pinned, a bracket was strictly narrowed, or only reproduction was achieved, and on which side (upper vs lower). It does not represent the lower-bound formula, a community claim, or an uncertified solver run as a settled value.
