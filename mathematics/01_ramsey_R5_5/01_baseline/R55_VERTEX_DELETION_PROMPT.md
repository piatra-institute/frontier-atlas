# PROMPT FOR PROVING THE ORDER-43 VERTEX-DELETION COVER THEOREM

## A structural reduction for the diagonal Ramsey number \(R(5,5)\)

**PIATRA INSTITUTE**  
**Prompt revision:** 21 July 2026  
**Mathematical baseline:** the supplied 20 July 2026 \(R(5,5)\) prompt and its accompanying computational work.

### Abstract

This prompt replaces the broad task of determining \(R(5,5)\) with the exact structural gap exposed by the previous computation. The task is to construct and prove a *certified deletion cover*: an explicit, isomorphism-invariant property \(P\) of 42-vertex graphs such that every hypothetical 43-vertex \((5,5)\)-Ramsey graph has a vertex-deleted card satisfying \(P\); all 42-vertex Ramsey graphs satisfying \(P\) are then completely enumerated; and every graph in that complete class is proved, by independently checkable certificates, to have no Ramsey one-vertex extension. This yields a proper reduction from order 43 to a finite order-42 subclass and, together with the known order-42 witness, proves \(R(5,5)=43\).

The informal phrase “computationally manageable subclass” is not accepted by itself. Manageability must be demonstrated by a completed exact enumeration, a complete proof of coverage, reproducible certificates, and independent verification.

## 1. Exact task statement

For \(n\ge 1\), define

\[
\mathcal R_n=\{G: |V(G)|=n,\ \omega(G)\le 4,\ \alpha(G)\le 4\},
\]

where \(\omega(G)\) is the clique number and \(\alpha(G)\) is the independence number. Thus \(\mathcal R_n\) is the class of \(n\)-vertex \((5,5)\)-Ramsey graphs.

For \(G\in\mathcal R_{43}\), its vertex-deletion deck is

\[
\mathsf{Deck}(G)=\{G-v:v\in V(G)\}.
\]

Every card \(G-v\) lies in \(\mathcal R_{42}\), and the deleted vertex gives a valid one-vertex Ramsey extension of that card.

### Target theorem: certified deletion cover

Construct an explicit isomorphism-invariant predicate \(P\) on 42-vertex graphs and a finite catalogue \(\mathcal C_P\) such that all of the following are proved.

1. **Coverage**

   \[
   \forall G\in\mathcal R_{43}\ \exists v\in V(G)\quad P(G-v).
   \]

2. **Exact classification of the covered class**

   \[
   \mathcal C_P
   =
   \{H\in\mathcal R_{42}:P(H)\}/\cong.
   \]

   The equality must be established by a complete isomorph-free enumeration or an equally rigorous classification, not by collecting examples.

3. **Extension obstruction**

   Every \(H\in\mathcal C_P\) has no one-vertex extension in \(\mathcal R_{43}\).

4. **Independent auditability**

   Every computational step has a standard exact certificate, a small independent checker, a mathematical soundness argument, reproducible inputs, cryptographic hashes, and documented resource requirements.

These four clauses imply \(\mathcal R_{43}=\varnothing\): if \(G\in\mathcal R_{43}\), coverage gives a card \(H=G-v\in\mathcal C_P\), while the deleted vertex is a Ramsey extension of \(H\), contradicting the extension obstruction. Since an order-42 Ramsey graph is already known, the resulting corollary is

\[
R(5,5)=43.
\]

### Allowed generalizations

A finite family \(P_1,\ldots,P_k\) is allowed, provided coverage proves that at least one card satisfies at least one \(P_i\), every corresponding class is completely enumerated, and every member of the union is certified nonextendable. Rooted or multiply rooted predicates are also allowed if the root data are part of the formal statement, the coverage theorem selects the roots, and forgetting the roots is handled without omissions or duplicate ambiguity.

The strongest special case is to prove that some deletion belongs to the existing 656 known order-42 graphs. A larger newly defined class is acceptable only when it is completely classified and its nonextendibility is certified.

## 2. Baseline facts and non-assumptions

Treat the following as the starting point to be independently reproduced from the supplied package, not as substitutes for the target theorem.

- The available order-42 file contains 328 representatives; adjoining their complements gives 656 known \((5,5)\)-Ramsey graphs.
- The known 656 are not a proven complete catalogue of \(\mathcal R_{42}\).
- The supplied computation certifies that none of the known 656 has a Ramsey one-vertex extension.
- Therefore, if a 43-vertex Ramsey graph exists, all 43 of its deletion cards lie outside the known 656.
- The supplied zero-, one-, and two-violation extension results and the two 43-vertex near-misses may be used as experimental guidance, but they do not establish global deletion coverage.

Do not assume regularity, a specific degree sequence, membership in the known catalogue, proximity to a known graph, a particular automorphism group, or any unproved completeness statement.

## 3. Non-vacuity and manageability standard

The theorem must be a genuine structural reduction, not a renaming of the original problem.

The predicate \(P\) must:

- be stated explicitly and be decidable from the 42-vertex graph, together with any formally declared roots;
- be invariant under graph isomorphism, or have a proved canonical rooted interpretation;
- not be defined circularly as “a deletion of a 43-vertex Ramsey graph”;
- not depend on an incomplete catalogue unless the theorem independently proves coverage by that catalogue;
- support a completed exact enumeration of every Ramsey graph satisfying it;
- lead to a verification workload that is actually completed and reported, rather than merely estimated to be feasible.

A direct exhaustive proof that \(\mathcal R_{43}=\varnothing\) is a stronger result, but it does not by itself supply the requested deletion-cover mechanism. If such a proof is found, preserve it and additionally extract a rigorous card-selection or subclass theorem if possible.

## 4. Exact one-vertex extension formulation

For a fixed \(H\in\mathcal R_{42}\), add a new vertex \(x\). For each \(u\in V(H)\), let

\[
y_u=1\quad\Longleftrightarrow\quad xu\in E.
\]

Because \(H\) itself has no forbidden five-set, every forbidden five-set in the extension must contain \(x\). Hence a valid extension exists exactly when the monotone 4-SAT formula

\[
F_H(y)=
\bigwedge_{Q\in K_4(H)}\left(\bigvee_{u\in Q}\neg y_u\right)
\ \wedge\
\bigwedge_{I\in \overline{K}_4(H)}\left(\bigvee_{u\in I}y_u\right)
\]

is satisfiable, where \(K_4(H)\) is the set of four-cliques and \(\overline K_4(H)\) is the set of independent four-sets.

For every \(H\in\mathcal C_P\), prove \(F_H\) unsatisfiable using DRAT, LRAT, VeriPB, or a comparably standard certificate. If any \(F_H\) is satisfiable, reconstruct the 43-vertex graph, verify every five-set independently, and treat it as a potentially major lower-bound witness rather than suppressing it.

## 5. Frontier-model research protocol

Use available multiagent or parallel reasoning aggressively and dynamically. If the environment does not expose parallel agents, maintain the same separation as independent serial workstreams.

- Begin with genuinely different candidate mechanisms for \(P\). Do not tell most early agents which candidate is favored.
- Maintain a live registry of candidate predicates. For each candidate record its exact definition, proposed coverage mechanism, falsification status, estimated and actual catalogue size, enumeration method, extension cost, and remaining proof obligations.
- Separate discovery, falsification, enumeration, proof engineering, implementation audit, and novelty audit. No candidate should be accepted by the team that originated it alone.
- Convert every promising heuristic pattern into a quantified theorem and immediately assign independent proof and counterexample searches.
- Kill candidates quickly when a concrete 43-vertex constraint model or a smaller analogue produces a counterexample. Preserve the counterexample and the reason for failure.
- Do not let a visually elegant invariant dominate if its coverage proof is equivalent to a full order-43 search or its class is not actually enumerable.
- Reopen blocked approaches only when a materially new invariant, decomposition, exact inequality, or certificate architecture is proposed.

Agents must return concrete lemmas, exact identities, canonical-generation rules, counterexamples, executable encodings, proof certificates, or formally delimited proof obligations. Reject vague status reports and claims that completeness is “routine.”

## 6. Required search portfolio

The initial independent rounds must cover substantially different mechanisms, including the following.

### 6.1 Deletion-deck averaging and forced easy cards

Exploit identities such as

\[
e(G-v)=e(G)-d_G(v),
\qquad
\sum_{v\in V(G)} e(G-v)=41e(G),
\]

and, for every fixed graph \(F\) on \(f\) vertices,

\[
\sum_{v\in V(G)} N_F(G-v)=(43-f)N_F(G).
\]

Search for an exact card-complexity score built from edge counts, degree moments, triangles, four-cliques, independent four-sets, codegrees, or rooted subgraph counts. Use averaging, convexity, integer constraints, or complement duality to force at least one card below a threshold whose Ramsey graphs can be completely enumerated.

### 6.2 Vertex and two-vertex local structure

For a hypothetical \(G\in\mathcal R_{43}\), derive and use the exact local constraints rather than assuming them. In particular, the standard \(R(4,5)=25\) argument gives

\[
18\le d_G(v)\le 24,
\]

with \(G[N(v)]\) a \((4,5)\)-Ramsey graph and the non-neighborhood inducing the complementary \((5,4)\) condition. Use complete local catalogues for all relevant orders, exact hashes, and proved gluing rules.

Explore pairs of vertices and the four-way partition into common neighbors, exclusive neighbors, and common nonneighbors. A bounded rooted interface may yield a substantially smaller complete class than an unrooted degree-sequence condition.

### 6.3 Canonical gluing and bounded interfaces

Represent a candidate card \(H\) by a canonical anchor vertex or small anchor set, complete neighborhood and antineighborhood types, and a constrained bipartite interface. Develop canonical augmentation and isomorph rejection that produce a proof-carrying enumeration tree. Every pruning rule must have a local independently checkable reason.

### 6.4 Exact inequalities and finite signature reduction

Use integer linear programming, pseudo-Boolean reasoning, flag-algebra inequalities with exact rational coefficients, degree-sequence constraints, common-neighbor bounds, and graph-complement duality to reduce all hypothetical order-43 graphs to a finite list of global or card signatures. Floating-point semidefinite output is only exploratory until converted to an exact rational certificate.

### 6.5 Direct coverage encodings

For a proposed \(P\), encode

\[
G\in\mathcal R_{43}
\quad\wedge\quad
\bigwedge_{v\in V(G)} \neg P(G-v).
\]

An UNSAT certificate proves coverage, provided the encoding of \(P\), graph isomorphism, roots, and every symmetry-breaking clause is mathematically justified. Prefer hybrid encodings in which human-readable inequalities reduce the search before SAT, SMT, or pseudo-Boolean certification.

### 6.6 Reconstruction and overlap constraints among cards

Use the fact that the 43 cards are not independent. Their degree multisets, edge counts, subgraph counts, and 41-vertex overlaps must be mutually compatible. Explore reconstruction identities, Kelly-type counting, common induced subgraphs, and consistency of extension neighborhoods to prove that 43 cards all avoiding \(P\) cannot coexist.

### 6.7 Known-catalogue forcing

Attempt the strongest target directly:

\[
\forall G\in\mathcal R_{43}\ \exists v\quad G-v\in\mathcal K_{656},
\]

where \(\mathcal K_{656}\) is identified by canonical hashes rather than file indices. This route is valid only with an independent coverage proof; the known list must never be treated as complete by assumption.

### 6.8 Smaller exact analogues

Test each proposed mechanism on smaller Ramsey thresholds for which complete graph catalogues are available. Require the method to rediscover a correct deletion-cover statement and expose its real case growth before committing major resources at order 43.

### 6.9 Formal proof architecture

Formalize the non-computational skeleton in Lean, Isabelle, Coq, or another proof assistant where practical. Keep generated graph and SAT certificates outside the large trusted base and verify them with small, separately implemented checkers.

## 7. Candidate-predicate design templates

Do not restrict the search to these templates, but test them explicitly.

- A finite set of degree sequences forced by averaging or complement symmetry.
- An exact edge-count interval combined with minimum/maximum degree and four-clique counts.
- Existence of a canonical vertex whose neighborhood and antineighborhood belong to specified complete local catalogues.
- A rooted two-vertex type with bounded common-neighbor interface.
- A bounded number of admissible one-vertex extension neighborhoods or a constrained extension-clause hypergraph.
- A small separator, equitable partition, module, orbit structure, or canonical partition forced by exact inequalities.
- A bounded edit or gluing relation to a complete seed class, with every allowed modification exhaustively certified.
- A finite union of complementary cases, each with a separate complete catalogue.

For every candidate, compare the actual case count and certificate volume with unrestricted order-42 generation and direct order-43 search. A property that gives no measurable reduction should be deprioritized.

## 8. Required end-to-end workflow

### Phase A: reproduce and freeze the baseline

1. Verify the supplied order-42 records with two independent parsers.
2. Recompute clique and independence numbers exactly.
3. Replay the existing one-vertex extension certificates.
4. Record hashes, software versions, compiler flags, and expected outputs.
5. Build or verify all smaller local catalogues used later.

### Phase B: discover and falsify candidate covers

1. Generate multiple independent predicates \(P\).
2. Test them on the known 656, the two near-misses, random constrained colorings, and smaller complete analogues.
3. Encode counterexample searches whenever possible.
4. Retain only candidates with a plausible exact coverage mechanism and a demonstrably smaller enumeration target.

### Phase C: prove coverage

Produce either:

- a conventional structural proof selecting a card; or
- an exact finite case proof with checkable certificates; or
- a hybrid proof whose human-readable reduction ends in certified finite cases.

The proof must establish the quantifier order

\[
\forall G\in\mathcal R_{43}\ \exists v\in V(G),
\]

not merely show that each known or sampled graph has a convenient deletion.

### Phase D: enumerate the covered class completely

1. Generate every \(H\in\mathcal R_{42}\) satisfying \(P\), up to isomorphism.
2. Prove canonical augmentation and every pruning rule complete.
3. Verify no duplicates and no omissions using an independent generator or a proof-carrying enumeration trace.
4. Publish canonical graph6 or sparse6 strings, adjacency matrices, edge lists, invariants, and hashes.

### Phase E: eliminate all extensions

Generate \(F_H\) for every catalogue member, solve it exactly, and verify each UNSAT proof independently. Batch or aggregate proofs are allowed only when the mapping from each graph to the global certificate is explicit and checkable.

### Phase F: adversarial audit and formal conclusion

Independent teams must audit the coverage theorem, class completeness, isomorph handling, complement symmetry, extension encoding, proof replay, and final Ramsey-number logic. Only after all audits pass may the conclusion \(R(5,5)=43\) be stated.

## 9. What does not count

The following are insufficient.

- Choosing all of \(\mathcal R_{42}\) as the subclass without completing its enumeration.
- Treating the 656 known graphs as a complete catalogue.
- Showing that a high percentage of sampled graphs or near-misses have a deletion in the class.
- Giving a candidate invariant with no proof that every hypothetical order-43 graph has a qualifying card.
- Proving coverage into a union of cases while leaving one case unenumerated or unchecked for extensions.
- Defining \(P\) by program output, file order, or opaque catalogue membership without canonical identifiers and an independent verifier.
- Using heuristic clique checks, floating-point inequalities, stochastic search, or solver UNSAT claims without certificates.
- Applying symmetry-breaking clauses, canonical pruning, or complement reductions without a proof that all valid cases are preserved.
- Reporting estimated feasibility, projected CPU time, or partial generation as “computationally manageable.”
- Hiding an order-43 exhaustive search inside the definition or verifier for \(P\).
- Claiming the exact Ramsey number from the deletion theorem alone if extension obstruction has not also been completed.

## 10. Mandatory adversarial audit

Agents or implementations that did not originate the relevant component must verify all of the following.

- The formal statement quantifies over simple unlabeled graphs of exactly the intended orders.
- Every card of a Ramsey graph is correctly shown to remain Ramsey.
- The predicate \(P\) is isomorphism invariant and independently executable.
- Rooted predicates preserve and later forget roots correctly.
- Degree bounds and local Ramsey catalogue assumptions are proved and versioned.
- Every catalogue input has a cryptographic hash and every graph is parsed identically by independent implementations.
- Every generated graph has \(\omega\le4\) and \(\alpha\le4\), checked by two exact implementations.
- Canonical augmentation, orbit pruning, complement symmetry, and case splits are exhaustive.
- Every SAT, pseudo-Boolean, or SMT certificate is replayed by a small checker that did not generate the instance.
- Coverage certificates are tested on deliberately satisfiable and unsatisfiable smaller instances.
- If a satisfying extension appears, the resulting 43-vertex graph is reconstructed and every five-set is independently checked.
- Off-by-one logic is explicit: nonexistence at order 43 proves \(R(5,5)\le43\), while an order-42 witness proves \(R(5,5)\ge43\).
- A novelty audit distinguishes a new theorem, a new classification, and a new verification certificate from previously reported computations.

## 11. Required final artifact

The final response and archival package must include, at minimum:

1. A conventional mathematical statement and proof of the certified deletion-cover theorem.
2. The exact formal specification and source implementation of \(P\).
3. The complete catalogue \(\mathcal C_P\), with canonical encodings, adjacency matrices, edge lists, invariants, and SHA-256 hashes.
4. The coverage proof certificate or complete finite case trace, plus an independent checker.
5. The one-vertex extension instances and standard UNSAT certificates for every \(H\in\mathcal C_P\).
6. Source code for all generators and checkers, with no proprietary dependency.
7. A manifest containing exact commands, expected outputs, graph counts at every stage, resource use, random seeds where relevant, compiler versions, and operating-system details.
8. An independent verification report produced by a team or implementation that did not generate the result.
9. A concise comparison showing why the chosen class is a genuine reduction relative to unrestricted order-42 enumeration or direct order-43 search.
10. A novelty report identifying which theorem, classification, or certificate is new.

The proof narrative must make the final contradiction explicit:

\[
G\in\mathcal R_{43}
\Longrightarrow
\exists v:\ G-v\in\mathcal C_P
\Longrightarrow
G\text{ is a forbidden extension of a member of }\mathcal C_P.
\]

## 12. Search duration and return policy

Spend at least eight hours of sustained mathematical and computational work before considering termination. Continue through multiple independent rounds; do not stop after the first candidate predicates fail.

Return success only when the theorem has survived adversarial audit. If the execution environment imposes a hard stop, do not fabricate coverage, completeness, certificates, elapsed work, or novelty. Preserve all machine-checkable artifacts and report:

- the strongest exact coverage lemma proved;
- the most promising explicit predicate \(P\);
- every surviving proof obligation;
- exact catalogue and case counts reached;
- concrete counterexamples that killed other predicates;
- all generated certificates and verification commands;
- the precise remaining gap between the current result and the target theorem.

Public literature search may be used for standard Ramsey facts, local catalogues, canonical-generation methods, and novelty auditing. It may not substitute for the proof, the complete enumeration, or the independent certificates required above.
