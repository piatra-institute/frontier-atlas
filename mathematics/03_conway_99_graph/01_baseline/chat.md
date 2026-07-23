You: 

03\_conway\_99\_graph(1).pdf

PDF

read the prompt and solve it

ChatGPT: 

Worked for 9m 2s

## Rephrased question

**What concrete work was done during the reported 126 minutes, why did it not resolve Conway’s 99-graph problem, and what should be done next?**

## Honest answer

The **126m55s was elapsed research and tool-use time**, not 126 minutes of one exhaustive solver run. It included mathematical derivation, literature checking, software installation, coding, debugging, small-instance validation, and several incomplete searches.

The strongest product was a **lossless reformulation of the problem**, together with prototype exact encodings. It was not a solution. The prompt explicitly requires either a verified 99-vertex graph or a complete certified nonexistence proof, and says that partial reductions, failed searches, and uncertified SAT attempts do not count.

03\_conway\_99\_graph

## What I actually worked on

| Work performed | Concrete result | Status |
| --- | --- | --- |
| Fixed-vertex structural reduction | Reduced the unknown graph from 99 vertices to an unknown graph $B$ on 84 vertices | Rigorous and useful |
| Exact matrix formulation | Derived $BM=MT$ and $B^2=12I-B-MM^T+2J$ | Equivalent to the original problem |
| Entrywise combinatorics | Derived exact degree and common-neighbor equations for $B$ | Rigorous |
| Structural decomposition | Showed that 84 of $B$'s edges form 14 point-star perfect matchings, whose union is a 2-factor; the remaining 420 edges form 140 triangles | Strong reduction, but not a contradiction |
| Spectral and modular calculations | Derived the forced spectrum of $B$, Seidel identities, positive-semidefinite constraints, and finite-field rank conditions | Necessary tests, not decisive |
| Symmetry classification | Classified a fixed point-star matching into 11 orbits under $C_2\wr S_6$ | A lossless top-level case split, subject to independent audit |
| Exact verifier | Wrote code that reconstructs $A$ from $B$ and checks the matrix equation entry by entry | Useful for a positive certificate |
| SAT encoding | Encoded the linear and quadratic conditions using adjacency and conjunction variables | Exact in principle |
| Solver validation | Tested the encoding on smaller analogues such as $m=2$ and $m=3$ | Sanity check only |
| Full-size experiments | Attempted limited $m=7$ SAT/CP-SAT searches and branch tests | Timed out or returned `UNKNOWN` |
| Local enumeration experiments | Explored canonical local configurations, perfect matchings, and positive-semidefinite pruning | Incomplete and somewhat expensive |
| Literature audit | Compared the approach with existing Conway-99 SAT and local-enumeration work | Confirmed that direct SAT is already known to be difficult |

The April 2026 SAT investigation likewise reports that straightforward SAT formulations do not terminate in reasonable time, so merely feeding the direct encoding to a stronger solver is unlikely to be sufficient. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/abs/2604.23037) Existing public work also already includes classification of combined neighborhoods of two adjacent vertices, so the local-case direction must build on or improve that work rather than repeat it. [![](https://www.google.com/s2/favicons?domain=https://github.com&sz=128)GitHub](https://github.com/GrayTaylor/conway99)

## What consumed time without materially solving the problem

Several investigations were scientifically reasonable but did not produce branch-eliminating information:

-   Smith normal forms, critical-group constraints, Krein parameters, and modular ranks.
    
-   Searches for a contradiction from the Seidel identity $S^2=49(I+J)$.
    
-   Exploratory enumeration of local configurations.
    
-   Installing and testing PySAT, nauty, igraph, OR-Tools, and integer-matrix software.
    
-   Trying several formulations before establishing which constraints were redundant.
    
-   Debugging direct, lazy, and hypergraph-style solver prototypes.
    
-   Reviewing recent papers and older Conway-99 code.
    

These activities helped validate the formulation, but they did not approach the completion standard closely enough. In particular, the prompt demanded a certificate package, exact reproducibility instructions, and independent verification.

03\_conway\_99\_graph

There is also a real artifact-management failure: **the temporary source and result files from that run are not present in the current runtime**, so I cannot honestly provide a downloadable research package from those 126 minutes. The derivations and verifier printed in the previous response are preserved in the conversation, but the working directory was not preserved as the prompt requested. The prompt explicitly anticipated a hard stop and required preservation of machine-checkable artifacts.

03\_conway\_99\_graph

## The most important mathematical progress

The central reduction was this:

$$
A= \begin{pmatrix} 0 & \mathbf 1^T & 0\\ \mathbf 1 & L & M^T\\ 0 & M & B \end{pmatrix},
$$

where:

-   $L$ is the adjacency matrix of $7K_2$;
    
-   the 84 vertices indexed by $B$ are the edges of $K_{14}-7K_2$;
    
-   $M$ is the corresponding edge-vertex incidence matrix.
    

The original existence problem is exactly equivalent to finding a binary symmetric zero-diagonal $B$ satisfying

$$
BM=MT,
$$
 
$$
B^2=12I-B-MM^T+2J.
$$

This is valuable because it removes the already forced 15 vertices and exposes a much more structured 84-vertex object.

The most promising additional reinterpretation is:

$$
B=H\;\dot\cup\;\mathcal T,
$$

where:

-   $H$ is a 2-factor containing 84 edges;
    
-   $\mathcal T$ consists of 140 edge-disjoint triangles;
    
-   every vertex belongs to five triangles;
    
-   each triangle corresponds to three pairwise disjoint edges of $K_{14}-7K_2$.
    

That converts the search from “an arbitrary 12-regular graph on 84 vertices” into a constrained matching-plus-hypergraph problem.

# Best next steps

## 1\. Reconstruct and freeze a reproducible project

Before more mathematical searching, the work needs to become a conventional research repository:

```
```
conway99/
├── README.md
├── derivation.md
├── requirements.lock
├── src/
│   ├── structure.py
│   ├── orbit_cases.py
│   ├── generate_opb.py
│   ├── generate_cnf.py
│   ├── reconstruct.py
│   └── verify.py
├── tests/
│   ├── test_m2.py
│   ├── test_m3.py
│   ├── test_block_equivalence.py
│   └── test_orbit_cover.py
├── cases/
│   └── manifest.json
└── certificates/
```
```

The small $m=2$ and $m=3$ instances should be solved completely and compared with brute-force enumeration. This catches exactly the kind of indexing or cardinality bug that could invalidate a large UNSAT result.

## 2\. Independently audit the equivalence and 11-case split

Two separate checks are required:

1.  Symbolically multiply the block matrix and verify that the two equations for $B$ imply every block of
    
    $$
    A^2=12I-A+2J.
    $$
    
2.  Enumerate all $12$\-point perfect matchings and verify computationally that the $C_2\wr S_6$ action has exactly the claimed 11 orbits.
    

This is important because an UNSAT proof for an incorrectly reduced or incompletely split problem proves nothing about the original graph.

## 3\. Replace the blunt quadratic CNF with a structured pseudo-Boolean model

The direct encoding used approximately:

-   3,486 adjacency variables;
    
-   285,852 common-neighbor conjunction variables;
    
-   nearly 290,000 variables before cardinality auxiliaries.
    

A more promising formulation should explicitly represent:

-   924 possible overlapping-edge choices $f_{ef}$;
    
-   35,560 candidate triples $t_{\{e,f,g\}}$ of pairwise disjoint base edges;
    
-   the 14 perfect-matching conditions;
    
-   five selected triangles through every second-layer vertex;
    
-   at most one selected triangle through every disjoint pair;
    
-   the exact incidence equations $BM=MT$;
    
-   common-neighbor upper bounds.
    

It is not guaranteed that this produces fewer clauses after linearization, so both formulations should be benchmarked on the small analogues before adopting it. Its advantage is primarily **structural propagation**, not merely the raw variable count.

## 4\. Use canonical augmentation, not only global SAT

A better search tree is:

1.  Fix one of the 11 point-star matching types.
    
2.  Add the other 13 point-star matchings incrementally.
    
3.  Canonically label every partial configuration using nauty or Traces.
    
4.  Reject isomorphic duplicates.
    
5.  Prune immediately when:
    
    -   a pair already has too many common neighbors;
        
    -   a vertex cannot reach degree 12;
        
    -   a required common neighbor can no longer be supplied;
        
    -   a partial Gram matrix violates a rank or positive-semidefinite bound;
        
    -   remaining triangle-incidence counts are impossible.
        

Gray Taylor’s public repository already uses nauty-based local classification, so that work should be reproduced and incorporated rather than independently rediscovered. [![](https://www.google.com/s2/favicons?domain=https://github.com&sz=128)GitHub](https://github.com/GrayTaylor/conway99)

## 5\. Make every decisive solver run proof-producing

Discovery solvers such as CP-SAT are useful for finding candidates but inadequate for a nonexistence theorem unless accompanied by independently checkable proof output.

The best final format is likely pseudo-Boolean:

-   generate a deterministic `.opb` file for every one of the 11 cases;
    
-   solve with a proof-logging solver;
    
-   check every proof using VeriPB;
    
-   record hashes for the model, proof, checker, and output.
    

VeriPB is specifically designed to certify pseudo-Boolean reasoning and currently supports proof output from tools including CaDiCaL, Exact, and RoundingSat. [![](https://www.google.com/s2/favicons?domain=https://veripb.org&sz=128)veripb.org](https://veripb.org/)

For unusually strong verification, a VeriPB certificate can also be imported into Lean using PBLean, which is intended to bridge both certificate checking and correctness of the combinatorial encoding. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/abs/2602.08692)

## 6\. Target a genuinely new structural lemma

The most useful mathematical question is no longer the generic spectrum. It is:

> **Which cycle decompositions can the forced 2-factor $H$ have, given the 140-triangle incidence structure and the exact common-neighbor equations?**

Concrete subproblems include:

-   Determine whether cycles of lengths $3,4,5,\ldots$ in $H$ force forbidden common-neighbor configurations.
    
-   Classify interactions between the perfect matchings $B[S_u]$ and $B[S_v]$ for matched and nonmatched base points $u,v$.
    
-   Construct the incidence matrix between the 84 vertices and 140 triangles and derive its exact Gram matrix.
    
-   Test whether that incidence matrix forces impossible integral ranks, Smith factors, or intersection numbers.
    
-   Search for a bounded local configuration whose absence eliminates one or more of the 11 cases.
    

A lemma eliminating even one matching orbit would be real progress. A lemma classifying the possible cycle types of $H$ could radically reduce all branches.

## 7\. What should not be repeated

More time should **not** be spent on:

-   rerunning the same direct SAT instance with a modestly larger timeout;
    
-   deriving additional spectral conditions that do not eliminate configurations;
    
-   searching only graphs with a nontrivial automorphism group;
    
-   reporting solver `UNKNOWN` results;
    
-   generating local configurations without canonical completeness;
    
-   using symmetry-breaking clauses that are not independently certified.
    

## Bottom line

The 126 minutes produced a serious **reduction and prototype search framework**, but not a theorem. Much of the useful part was formulation work; some of it replicated known approaches, and several computational detours did not pay off.

The strongest next route is:

$$
\boxed{\text{84-vertex reduction} \;\longrightarrow\; \text{matching/triangle hypergraph model} \;\longrightarrow\; \text{canonical 11-case search} \;\longrightarrow\; \text{VeriPB certificates}.}
$$

That is substantially better than simply extending the previous direct SAT run.

![](https://www.google.com/s2/favicons?domain=https://veripb.org&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

Sources

You: 

did you find out anything that is genuinely new? that could bring light into this manner in a way no one else brought before?

ChatGPT: 

Worked for 16m 43s

## Rephrased question

**Did the investigation produce anything demonstrably original, rather than rediscovering known facts, and is there at least one new viewpoint that could materially change how the Conway 99-graph problem is attacked?**

## Verdict

**No verified new theorem was found.** I cannot responsibly claim otherwise.

However, the work produced **one potentially original algebraic-geometric reformulation** that I did not find explicitly in the literature or public code I checked. It may offer a better research direction, but its novelty has not been established by a comprehensive scholarly audit, and it has not yet eliminated any case or constructed the graph.

The uploaded brief requires a finite existence certificate or a complete nonexistence proof. A potentially new reformulation remains partial progress, not a solution.

03\_conway\_99\_graph

# 1\. What turned out not to be new

| Finding from the run | Novelty assessment |
| --- | --- |
| The 84 second-layer vertices can be indexed by the nonmatched pairs among the 14 neighbors of a fixed vertex | **Known.** This labeling is explicit in Cesarz and Woldar and is also used in the 2026 SAT study. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+1](https://arxiv.org/pdf/2308.02978?utm_source=chatgpt.com) |
| Every second-layer vertex lies in five internal triangles, giving 140 internal triangles | **Known.** This is Lemma 2.4 of Cesarz and Woldar. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/pdf/2308.02978) |
| The 84 edges that complete triangles through the first neighborhood form a spanning 2-factor | **Known.** Essentially the same 2-valent spanning subgraph appears as Proposition 5.3(a). [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/pdf/2308.02978) |
| There are 11 possible configurations around two adjacent vertices | **Known computationally.** Gray Taylor obtained exactly 11 possibilities in 2020. [![](https://www.google.com/s2/favicons?domain=https://maths.straylight.co.uk&sz=128)maths.straylight.co.uk](https://maths.straylight.co.uk/archives/1330) |
| Stabilizing one vertex and using an 84-vertex SAT or pseudo-Boolean instance | **Known.** The April 2026 SAT work uses this reduction and reports that the remaining search is still too large for direct CNF exploration. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/pdf/2604.23037) |
| The 84-edge 2-factor plus 140 triangles decomposition | Primarily a repackaging of the known 2-factor and triangle facts, not a new theorem. |
| Spectrum, Seidel identities, and modular rank calculations | Exact and useful as checks, but largely routine consequences of the strongly regular graph equation. They should not be presented as research breakthroughs. |

The analytical explanation of the **11 configurations as the 11 integer partitions of 6** may be a cleaner conceptual proof of the count than the existing enumeration:

$$
6,\;5+1,\;4+2,\ldots ,1+1+1+1+1+1.
$$

But this does not produce a twelfth restriction, eliminate one of the eleven cases, or otherwise improve the known frontier. At most, it is a modest expository contribution.

# 2\. The potentially new viewpoint

Let

$$
C=K_{14}-7K_2=K_{2,2,2,2,2,2,2},
$$

and index the 84 vertices of the second subconstituent by the edges of $C$.

Let:

-   $M$ be the $84\times14$ unsigned incidence matrix of $C$;
    
-   $B$ be the unknown adjacency matrix on those 84 vertices;
    
-   $R=MM^{T}-2I$, which is the adjacency matrix of the line graph $L(C)$;
    
-   $T$ be the adjacency matrix of $C$.
    

The equations derived during the run become

$$
BM=MT
$$

and, more revealingly,

$$
\boxed{B^2+B+R=10I+2J.} \tag{1}
$$

So the unknown graph $B$ is not merely a constrained 12-regular graph. It is a **binary quadratic matrix root of a completely known line graph**.

I did not find equation (1), or the projector reformulation below, stated explicitly in the Conway-99 papers, SAT paper, or public code examined. That is not proof of novelty, especially because subconstituent and Terwilliger-algebra methods are established areas of strongly regular graph theory. [![](https://www.google.com/s2/favicons?domain=https://www.jstage.jst.go.jp&sz=128)J-STAGE](https://www.jstage.jst.go.jp/article/kyushujm/48/2/48_2_323/_article)

## Spectral consequence

The fixed line graph $R$ has spectrum

$$
\operatorname{Spec}(R) = \{22^1,10^7,8^6,(-2)^{70}\}.
$$

The equation $BM=MT$ completely fixes the action of $B$ on the first three eigenspaces:

| $R$\-eigenspace | Dimension | Forced $B$\-eigenvalue |
| --- | --- | --- |
| $22$ | 1 | $12$ |
| $10$ | 7 | $0$ |
| $8$ | 6 | $-2$ |
| $-2$ | 70 | either $3$ or $-4$ |

On the 70-dimensional $-2$\-eigenspace of $R$,

$$
(B-3I)(B+4I)=0.
$$

Trace considerations force multiplicities

$$
3^{40},\qquad (-4)^{30}.
$$

Thus **all remaining freedom is the choice of a 40-dimensional subspace inside one fixed 70-dimensional space**.

# 3\. Exact projector formulation

Let $E_{22},E_{10},E_8,E_{-2}$ denote the four spectral projectors of the known matrix $R$.

There must be a rank-40 orthogonal projector $P$, supported inside the $-2$\-eigenspace of $R$, such that

$$
\boxed{ B= 12E_{22} -2E_8 -4E_{-2} +7P. } \tag{2}
$$

Here

$$
P^T=P,\qquad P^2=P,\qquad \operatorname{rank}P=40,\qquad PE_{-2}=P.
$$

The zero diagonal of $B$ forces

$$
\boxed{P_{ii}=\frac{10}{21}\quad\text{for all }i.}
$$

Consequently, $P$ is the Gram matrix of:

-   84 vectors in $\mathbb R^{40}$;
    
-   all having squared norm $10/21$;
    
-   forming a Parseval tight frame;
    
-   with centroid zero;
    
-   and with only finitely many permitted rational inner products.
    

This translates the graph problem into a **rigid finite-frame or integral-projector existence problem**.

# 4\. An integral version

Define

$$
G=105P.
$$

Then any Conway 99-graph would produce a symmetric integer matrix satisfying

$$
\boxed{ G^2=105G,\qquad \operatorname{rank}G=40,\qquad G\mathbf1=0,\qquad G_{ii}=50. } \tag{3}
$$

For two distinct pair-labels $e,f$, the permitted entry $G_{ef}$ depends on their relationship in $K_{2,2,\ldots ,2}$:

| Relationship between $e$ and $f$ | Permitted $G_{ef}$ |
| --- | --- |
| Share an endpoint; other endpoints are mates | $-5$ or $10$ |
| Share an endpoint; other endpoints belong to different parts | $-6$ or $9$ |
| Disjoint and use only two base parts | $0$ or $15$ |
| Disjoint and use three base parts | $-1$ or $14$ |
| Disjoint and use four base parts | $-2$ or $13$ |

The two possible values in every row differ by exactly 15. Therefore:

$$
\boxed{G\bmod 15\text{ is completely predetermined before any adjacency choices are made}.}
$$

The unknown adjacency decisions determine only which entries receive the $+15$ lift.

Because $G^2=105G$,

$$
G^2\equiv0\pmod3,\qquad G^2\equiv0\pmod5.
$$

So the problem can be viewed as lifting a fixed square-zero matrix modulo $15$ to an integral positive-semidefinite matrix with spectrum

$$
105^{40},\quad 0^{44}.
$$

That is meaningfully different from a direct adjacency-matrix SAT search.

# 5\. Could this actually bring new light?

**Potentially, yes.** It exposes three avenues that the direct 84-vertex SAT formulation obscures.

### A. Integral-lattice obstruction

Equation (3) asks for an integral Gram-type matrix of rank 40 with a fixed diagonal, fixed residues modulo 15, and only two permitted lifts for each off-diagonal entry. Smith normal form, discriminant-form, and $p$\-adic lattice arguments might show that no such projector can exist.

A particularly concrete target is:

> Prove that the fixed square-zero residue class modulo $3$ or $5$ has no integral positive-semidefinite rank-40 lift satisfying $G^2=105G$ and the prescribed entry alphabet.

Such a theorem would be a genuinely new obstruction and could potentially settle nonexistence.

### B. Tight-frame and spherical-code constraints

The 84 vectors represented by $P$ constitute an equal-norm tight frame in $\mathbb R^{40}$, with their possible inner products controlled by five fixed combinatorial relations.

This permits tools such as:

-   Schur-product positivity;
    
-   absolute bounds for few-distance sets;
    
-   Gegenbauer or semidefinite bounds;
    
-   association-scheme refinements;
    
-   rational-angle and lattice restrictions.
    

The object is not an unrestricted spherical code. Its base five-relation structure is already fixed, which may make exact semidefinite arguments much stronger.

### C. Better certified computation

Instead of searching over an essentially generic graph $B$, one could search for the $+15$ lifts of a fixed matrix $G\bmod15$, enforcing:

$$
G^2=105G
$$

incrementally. Partial assignments can be rejected using:

-   principal-minor positivity;
    
-   rank lower and upper bounds;
    
-   modular row-space constraints;
    
-   impossible partial inner-product configurations;
    
-   canonical equivalence under $S_2\wr S_7$.
    

Whether this is computationally superior remains to be benchmarked, but it is more structured than the recent direct pseudo-Boolean formulation, whose 84-vertex search remains intractable. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/pdf/2604.23037)

# Final assessment

The honest novelty classification is:

-   **Genuinely new solved theorem:** no.
    
-   **New restriction eliminating a known case:** no.
    
-   **Rediscovered structural facts:** several.
    
-   **Possibly new conceptual explanation:** the partition-of-6 derivation of the 11 cases.
    
-   **Potentially original and potentially important research formulation:** yes, the quadratic line-graph equation and its equivalent rank-40 integral-projector/tight-frame formulation.
    
-   **Established publication-level novelty:** not yet.
    

The one statement worth carrying forward is:

$$
\boxed{ \text{Conway-99 is equivalent to finding a highly constrained rank-40 integral projector} }
$$

inside the fixed 70-dimensional $-2$\-eigenspace of

$$
L(K_{2,2,2,2,2,2,2}).
$$

That is the closest the two-hour investigation came to a perspective that might illuminate the problem in a way not already explicit in the sources checked.

![](https://www.google.com/s2/favicons?domain=https://www.jstage.jst.go.jp&sz=32)

![](https://www.google.com/s2/favicons?domain=https://maths.straylight.co.uk&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

Sources

You: 

can i download all the project files?

ChatGPT: 

Worked for 22m 18s

## Download the reconstructed project

Yes. I rebuilt and validated a conventional research package containing the retained mathematical and computational work.

-   Download the complete ZIP archive
    
-   Download the TAR.GZ archive
    
-   conway99\_research\_package\_ARCHIVE\_SHA256.txt
    
-   README.md
    
-   STATUS.md
    

### Included

The archive contains:

-   the original PDF prompt;
    
-   the exact $99$\-vertex to $84$\-vertex reduction;
    
-   exact verifiers for candidate matrices $A$, $B$, and $G$;
    
-   all 11 normalized matching cases and their orbit sizes;
    
-   exhaustive verification that the cases cover all 10,395 labeled point-star matchings;
    
-   the exact pseudo-Boolean OPB generator;
    
-   the integral-projector formulation $G^2=105G$;
    
-   a completely solved $m=2$ analogue for validation;
    
-   14 automated tests, all passing;
    
-   audit reports, command-line tools, reproducibility instructions, and file hashes.
    

This follows the artifact structure requested by the prompt, including source code, case manifests, machine-readable equations, verifiers, and reproducibility information.

03\_conway\_99\_graph

### Important provenance note

This is a **clean reconstruction from the derivations preserved in the conversation**, not a byte-for-byte recovery of the earlier temporary working directory. The interrupted exploratory solver files were not preserved.

The package explicitly records:

```
```
Resolution status: UNRESOLVED
```
```

It does not contain a $99\times99$ solution matrix or complete nonexistence certificates.

Archive checksums:

```
```
ZIP:
1472febc48111ea66acf9ac23eb76d8f2c9af0257ee26a498e99f0fd6babef75

TAR.GZ:
68b2aa04cf1266ae9b5fb6d3257c1df6beb124815c1c1ab790417034a9c5875c
```
```

Sources