# PROMPT FOR LOWERING (OR CERTIFYING A FLOOR ON) THE BORSUK THRESHOLD DIMENSION

## The smallest dimension in which Borsuk's partition conjecture fails

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 23 of 50  
**Area:** discrete geometry  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Borsuk conjectured that every bounded set in \(\mathbb{R}^d\) splits into \(d+1\) pieces of strictly smaller diameter. It is true for \(d\le 3\) and false for large \(d\) (Kahn–Kalai, 1993); the smallest dimension where it fails is unknown, pinned only to the interval \(4\le d\le 64\). All known counterexamples are *finite point sets* - typically two-distance sets drawn from strongly regular graphs - for which the Borsuk number equals the chromatic number of the diameter graph. That reduction turns the search into a machine-checkable object: construct a finite set whose diameter graph needs more than \(d+1\) colours, or certify that no set of a given combinatorial type does so below some \(d\). This is a `[search]` problem with an exact verifier and a direct link to problem 28 (strongly regular graph existence). The resolution standard is a *proof*: an exact-arithmetic counterexample in a new low dimension, or a certified nonexistence within a delimited class. A promising point cloud with a numerically small diameter spread is not a resolution.

## 1. Exact problem statement

For a bounded set \(S\subset\mathbb{R}^d\) let the diameter be

\[
\operatorname{diam}(S)=\sup_{x,y\in S}\lVert x-y\rVert_2 .
\]

The *Borsuk number* \(b(S)\) is the least \(m\) such that \(S=\bigcup_{i=1}^m S_i\) with \(\operatorname{diam}(S_i)<\operatorname{diam}(S)\) for all \(i\). Define

\[
f(d)=\sup\{\,b(S):S\subset\mathbb{R}^d\text{ bounded}\,\}.
\]

**Borsuk's conjecture** is \(f(d)=d+1\) (the lower bound \(f(d)\ge d+1\) is classical, from a regular \(d\)-simplex or a ball). Define the **threshold**

\[
d_\star=\min\{\,d: f(d)>d+1\,\},
\]

the smallest dimension in which the conjecture *fails*. Known facts:

- \(f(d)=d+1\) for \(d\le 3\).
- \(f(d)>d+1\) for \(d\ge 64\).
- Hence \(4\le d_\star\le 64\), and \(d_\star\) is open.

The classical lower bound \(f(d)\ge d+1\) is witnessed by two canonical bodies: the regular \(d\)-simplex (each pair of a smaller-diameter part must separate two of its \(d+1\) vertices, forcing \(d+1\) parts) and the Euclidean ball (Borsuk's own antipodal argument). So a counterexample must *exceed* this \(d+1\), not merely meet it.

**Finite reduction (the certified handle).** For a *finite* set \(S\), define its **diameter graph** \(G_S\) on vertex set \(S\), with an edge between \(x,y\) iff \(\lVert x-y\rVert=\operatorname{diam}(S)\). A partition of \(S\) into parts of strictly smaller diameter is exactly a proper vertex colouring of \(G_S\) - each part omits every diametral pair. Therefore

\[
b(S)=\chi(G_S)\qquad(S\text{ finite}),
\]

and a counterexample in dimension \(d\) is a finite \(S\subset\mathbb{R}^d\) with \(\chi(G_S)>d+1\).

Special structure that makes the search tractable:

- A **two-distance set** has all pairwise distances in \(\{a,b\}\), \(a<b\); taking \(b=\operatorname{diam}\), \(G_S\) is the graph of the larger distance.
- Such sets on a sphere arise from **strongly regular graphs**, association schemes, and spherical designs - the source of every record construction.
- A diametral **clique** of size \(d+2\) already certifies \(\chi(G_S)\ge d+2>d+1\).

Adopted conventions:

- Euclidean norm; "smaller diameter" is strict.
- The primary search is restricted to finite sets (sufficient for a counterexample; a bounded-set counterexample can be finitized to its diameter-graph-relevant points).
- Dimension \(d\) is the dimension of the affine hull of \(S\).

No informal target ("a set that is hard to partition") is acceptable.

## 2. Resolution standard

**(R1) New low-dimensional counterexample.** A finite set \(S\subset\mathbb{R}^{d}\) with \(4\le d<64\) and a *certified proof* that \(\chi(G_S)>d+1\), i.e. \(b(S)>d+1\). Certified form:

- **exact-arithmetic diameter determination** - all pairwise squared distances in exact rational or algebraic arithmetic, so the diameter and hence the edge set of \(G_S\) are exact and unambiguous; together with
- a **certified chromatic-number lower bound** - a DRAT/LRAT-checked proof that the \((d+1)\)-colouring SAT instance for \(G_S\) is unsatisfiable, or an exhibited diametral \((d+2)\)-clique.

This lowers the record on \(d_\star\).

**(R2) Certified structural floor.** For a delimited combinatorial class \(\mathcal{C}\) (e.g. two-distance sets of \(\le M\) points, or diameter graphs arising from strongly regular graphs with parameters in a stated feasible list), an exhaustive certified proof that no member yields \(\chi(G_S)>d+1\) for \(d\) below some \(d_0\). Certified form: an **exhaustive isomorph-free enumeration** of the class with a certified colouring (upper bound) for each member.

**Not accepted as resolution.**

- A point set with a numerically computed diameter graph and a numerically estimated chromatic number - floating-point distances can misclassify diametral pairs, and greedy/heuristic colourings do not certify \(\chi\).
- A colouring failure by one algorithm presented as \(\chi>d+1\); a lower bound on \(\chi\) requires exhaustiveness (SAT UNSAT with proof), not a heuristic's inability to colour.
- Reproducing a known counterexample (\(d\ge 64\)) at higher precision, or matching Bondarenko/Jenrich data without lowering \(d\).
- A construction whose diameter is realized only in a limiting/approximate sense (distances equal "to \(10^{-9}\)").

A diametral clique of size \(d+2\), with its distances verified exactly, *is* accepted as a certified lower bound. Stress: the entire content is the *exact* edge set of \(G_S\) and a *certified* colouring bound; a configuration that "looks" hard to partition proves nothing.

## 3. Graded partial-result targets

**P1 - Certified reproduction of the record.** Rebuild Bondarenko's \(d=65\) and the Jenrich–Brouwer \(d=64\) counterexamples with exact-arithmetic distances and a certified \(\chi\) lower bound.
*Certificate:* exact coordinate/Gram data, exact diameter, and a DRAT proof or an exhibited \((d+2)\)-clique.

**P2 - Exact catalogue of candidate diameter graphs.** For strongly regular / two-distance families with vertex counts up to a stated bound, compute exact Gram matrices, realize them in the minimal Euclidean dimension, and record \(d\), \(|S|\), and clique lower bounds on \(\chi(G_S)\).
*Certificate:* exact linear algebra (rank, eigenvalues via exact characteristic polynomial); reproducible catalogue.

**P3 - Certified upper bounds \(f(d)\le d+1\) for small \(d\) within a class.** For \(d\in\{4,5,6\}\) and a bounded combinatorial class, certify that no member forces more than \(d+1\) parts.
*Certificate:* certified colourings for each member plus the enumeration-completeness argument.

**P4 - A near-miss below 64.** A finite set in some \(d<64\) with \(\chi(G_S)=d+1\) exactly (tight but not a counterexample), or with \(\chi(G_S)>d\) improving structural understanding.
*Certificate:* exact diameter graph plus certified \(\chi\).

**P5 - A new counterexample \(4\le d<64\) (this is R1).** Lower the record on \(d_\star\).
*Certificate:* exact diameter graph plus DRAT-checked \((d+1)\)-colouring UNSAT (or a \((d+2)\)-clique).

**P6 - Certified nonexistence floor (this is R2).** For a delimited class, an exhaustive certified proof of no counterexample below a stated \(d_0\).
*Certificate:* isomorph-free enumeration replay plus per-member certified colourings.

## 4. Known results and prior art

- **Truth for small \(d\).** \(d=2\): Borsuk (1932). \(d=3\): Perkal (1947), Eggleston (1955), with later short proofs (Grünbaum, Heppes, ~1957). No counterexample for \(d\le 3\).
- **Failure for large \(d\).** **Kahn and Kalai (1993)** disproved the conjecture, first counterexample near \(d=1325\) (verify), using \(\{0,1\}\)-vectors and the Frankl–Wilson theorem.
- **Dimension reductions.** **Nilli/Alon (1994)** \(d\approx 946\); **Raigorodskii (1997)** \(d\approx 561\); **Weißbach**; **Hinrichs (2002)** \(d\approx 323\); **Pikhurko**; **Hinrichs–Richter (2003)** \(d\approx 298\) (verify each dimension).
- **Current record.** **A. Bondarenko (2013/2014)** gave a counterexample in \(d=65\) from a two-distance set of 416 points on \(S^{64}\) associated with a strongly regular graph; **T. Jenrich and A. E. Brouwer (2014)** reduced this to \(d=64\) via a 352-point subset. So \(d_\star\le 64\) (verify the precise vertex counts and the SRG involved).
- **Piece-count growth.** Beyond the threshold, Kahn–Kalai showed the number of required pieces grows like \((1.2\dots)^{\sqrt d}\), far above \(d+1\); the *threshold* question (smallest failing \(d\)) is nonetheless separate from the *growth-rate* question and is the target here.
- **Ball-free counterexamples.** All known counterexamples are finite point sets, not smooth bodies; this is why the diameter-graph / chromatic-number reduction captures them exactly.
- **Reduction and method.** For finite sets \(b(S)=\chi(G_S)\); two-distance sets and spherical designs are the productive source. Raigorodskii's surveys (2000s–2010s) collect the state of the art. The gap \(4\le d_\star\le 63\) has been essentially untouched from below - no counterexample under dimension 64 is known.
- **Link.** The constructions ride on strongly regular graph existence (problem 28); feasible-parameter SRGs are the raw material.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the current record dimension (whether it is still 64), the exact Bondarenko / Jenrich–Brouwer parameters, and any post-2014 improvement from either direction before claiming an increment.

## 5. Attack plan

**`[search]` counterexample hunt (primary).**

- *Build candidate diameter graphs.* Take strongly regular graphs / association schemes with feasible parameters; form the exact Gram matrix \(G=I+\alpha A+\beta(J-I-A)\) tuned so the larger distance is the diameter; realize \(S\) in \(\mathbb{R}^d\) with \(d=\operatorname{rank}\) of the appropriate centered Gram matrix, via exact eigenvalue/rank computations in **SageMath**.
- *Extract and test.* From each candidate, extract \(G_S\) exactly and (a) search for a \((d+2)\)-clique of diametral pairs (an immediate certified lower bound), and (b) encode \((d+1)\)-colourability as SAT, running **CaDiCaL/kissat/CryptoMiniSat** with DRAT output; UNSAT with a checked proof certifies \(\chi>d+1\).
- *Push down in dimension.* Prioritize families known to be extremal (the \(G_2(4)\)-related and other rank-3 graphs behind Bondarenko), then take subsets and quotients while re-checking the exact diameter, aiming at a lower realizing dimension.

**`[search]`/`[enum]` nonexistence within a class.** For small \(d\) and bounded \(|S|\), enumerate two-distance sets isomorph-free (nauty/Traces on the diameter graph) and certify a \((d+1)\)-colouring for each; completeness of the enumeration plus per-instance colourings yields a certified floor.

**One-workstation scope.** Exact Gram-matrix algebra and SAT colouring for graphs up to a few hundred vertices are workstation-feasible. The bottleneck is not the SAT check but the *combinatorial supply* of low-dimensional two-distance sets; the search is idea-limited, not compute-limited - exactly the institute's profile.

**First-session checklist (concrete).**

1. Rebuild the Jenrich–Brouwer \(d=64\) point set with an exact Gram matrix; confirm the exact diameter and edge set of \(G_S\).
2. Encode \((d+1)=65\)-colourability as SAT and reproduce UNSAT with a checked DRAT proof, or exhibit a \((d+2)\)-clique (P1).
3. Enumerate strongly regular / two-distance families with small realizing dimension and tabulate \((d,|S|)\) exactly (P2).
4. For each candidate, extract \(G_S\) and test for a diametral \((d+2)\)-clique - the cheapest certified lower bound.
5. For the most promising low-\(d\) candidate, run the \((d+1)\)-colouring SAT with DRAT output.

**Failure modes.**

- Floating-point diameter misclassification flipping edges of \(G_S\) - fatal; distances must be exact.
- Realizing a Gram matrix in the wrong (too high) dimension by not centering/reducing correctly, discarding a genuinely low-\(d\) set.
- Treating a heuristic colouring failure as a lower bound on \(\chi\).
- A counterexample whose diameter is achieved only approximately, so \(G_S\) is ill-defined.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All pairwise squared distances, the diameter, the edge set of \(G_S\), and the realizing dimension are computed in exact rational/algebraic arithmetic. The chromatic lower bound is certified: an exhibited diametral clique (exact) or a DRAT/LRAT-checked SAT-UNSAT proof of \((d+1)\)-colourability. Floating point is exploration only.
2. **Independent verification.** A standalone checker, independent of the construction code, re-reads the point set (or Gram matrix), recomputes all distances exactly, rebuilds \(G_S\), verifies the affine-hull dimension, and independently checks the colouring certificate (DRAT checker, or clique verification). A second CAS reproduces the exact eigenvalues/rank.
3. **Reproducibility.** The SRG/association-scheme source, the Gram-matrix parameters, the realization procedure, SAT encodings, solver versions, and seeds are recorded; a SHA-256 manifest covers coordinate files, DIMACS instances, DRAT proofs, and checker logs.
4. **Preservation.** Construction scripts, the SAT-encoding generator, and the enumeration code are part of the record; anything not preserved is stated (the Hadamard-668 lost-source lesson). A `NEXT_STEPS.md` records the current lowest certified counterexample dimension and the classes still to enumerate (the Moore-57 pattern).
5. **Honest reporting.** The report states plainly whether a genuine counterexample in a *new* dimension \(d<64\) was proved (with the certified \(\chi\) bound), or whether the result is a certified reproduction, a tight near-miss, or a delimited nonexistence floor. The exact edge set of \(G_S\) and the certified nature of every \(\chi\) bound are the load-bearing facts, reported as such - never a numerically suggestive point cloud.
