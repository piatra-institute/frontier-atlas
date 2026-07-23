# PROMPT FOR SETTLING THE EXISTENCE OF AN APN PERMUTATION IN DIMENSION EIGHT

## The "big APN problem" - an almost-perfect-nonlinear permutation of \(\mathbb{F}_2^8\)

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 08 of 50
**Area:** Boolean & cryptographic functions
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An almost perfect nonlinear (APN) function offers the best possible resistance to differential cryptanalysis; an APN *permutation* is what an ideal S-box would be. For odd \(n\) many APN permutations of \(\mathbb{F}_2^n\) are known; for even \(n\) the situation is a scandal of the field. None exists for \(n=4\) (an exhaustive fact), exactly one CCZ-equivalence class is known for \(n=6\) (the Dillon "Kim function" permutation, 2009), and for \(n=8\) and every even \(n\ge 8\) the existence question is **open**. This is "the big APN problem". The task is matched to certified search because the objects are finite, the defining property is a decidable counting condition on \(2^n\) field elements, and the only known route to an even-dimension APN permutation - start from a quadratic APN function and hunt its CCZ-equivalence class for a graph that is the graph of a permutation - is exactly the kind of structured, symmetry-reduced, SAT-and-linear-algebra search a machine closes. The on-machine verifier is a direct recomputation of the difference distribution table (DDT) together with a bijectivity check; anything short of the Section 2 standard - a heuristic near-miss, an unreplayable solver run, an equivalence claim without a certified transformation - is a partial result, never a solution. The value of even a *restricted* certified negative (no permutation in a completely enumerated family) is high precisely because it narrows where an APN permutation, if one exists, must hide.

## 1. Exact problem statement

Let \(\mathbb{F}_2=\{0,1\}\) and \(\mathbb{F}_2^n\) the \(n\)-dimensional vector space over it; fix an isomorphism \(\mathbb{F}_2^n\cong\mathbb{F}_{2^n}\) as needed (a chosen primitive polynomial), so that a vectorial Boolean function \(F:\mathbb{F}_2^n\to\mathbb{F}_2^n\) may be given either as a lookup table of \(2^n\) values or as a univariate polynomial \(\sum_{i=0}^{2^n-1} c_i x^i\) over \(\mathbb{F}_{2^n}\).

For \(a,b\in\mathbb{F}_2^n\) the *difference distribution table* entry is
\[
\delta_F(a,b)=\bigl|\{x\in\mathbb{F}_2^n : F(x+a)+F(x)=b\}\bigr|,
\]
and the *differential uniformity* is
\[
\delta(F)=\max_{a\neq 0,\ b}\ \delta_F(a,b).
\]
Because \(x\) and \(x+a\) are paired, every nonzero-\(a\) count is even, so \(\delta(F)\ge 2\). \(F\) is **almost perfect nonlinear (APN)** iff \(\delta(F)=2\). Equivalently, writing the DDT-row constraint explicitly,
\[
\forall a\neq 0:\qquad \sum_{b\in\mathbb{F}_2^n}\delta_F(a,b)=2^n,\quad \delta_F(a,b)\in 2\mathbb{Z}_{\ge0},\quad \max_b\delta_F(a,b)=2,
\]
so APN says every nonzero-\(a\) row of the DDT is a \(\{0,2\}\)-vector. A univariate polynomial \(F(x)=\sum_i c_i x^i\) over \(\mathbb{F}_{2^n}\) is **quadratic** iff every exponent \(i\) with \(c_i\neq0\) has binary weight \(\le 2\); quadratic APN functions are the workhorses of the search because their ortho-derivative gives a strong, cheap invariant.

For \(u\in\mathbb{F}_2^n\), \(\mathrm{wt}(u)\) is the Hamming weight, \(d(u,u')=\mathrm{wt}(u+u')\) the Hamming distance, and \(\langle w,x\rangle=\sum_i w_i x_i\bmod 2\) the standard inner product. For \(v\in\mathbb{F}_2^n\setminus\{0\}\) the **component function** \(f_v=\langle v,F\rangle\) is Boolean, with Walsh transform
\[
W_F(v,w)=\sum_{x\in\mathbb{F}_2^n}(-1)^{\langle v,F(x)\rangle+\langle w,x\rangle}.
\]
The multiset \(\{W_F(v,w):v\neq0,\,w\}\) is the **extended Walsh spectrum**, and the vectorial nonlinearity is \(\mathrm{nl}(F)=2^{n-1}-\tfrac12\max_{v\neq0,w}|W_F(v,w)|\); both are CCZ-invariant. \(F\) is a **permutation** iff its image multiset is exactly \(\mathbb{F}_2^n\), equivalently iff \(W_F(v,0)=0\) for all \(v\neq0\).

For a quadratic \(F\), write \(B_F(a,x)=F(x+a)+F(x)+F(a)+F(0)\) for the associated symmetric bilinear map. The **ortho-derivative** \(\pi_F\) assigns to each nonzero \(a\) the (generically unique up to scalar) nonzero \(\pi_F(a)\) with \(\langle\pi_F(a),\,B_F(a,x)\rangle=0\) for all \(x\); the differential and Walsh spectra of \(\pi_F\) form the sharpest known practical CCZ-invariant for quadratic APN functions and are the primary class separator used below.

Two functions \(F,G:\mathbb{F}_2^n\to\mathbb{F}_2^n\) are **CCZ-equivalent** (Carlet–Charpin–Zinoviev, 1998) if their graphs
\[
\mathcal{G}_F=\{(x,F(x)):x\in\mathbb{F}_2^n\}\subseteq\mathbb{F}_2^{2n}
\]
are mapped onto one another by an affine permutation \(\mathcal{L}\) of \(\mathbb{F}_2^{2n}\); i.e. \(\mathcal{L}(\mathcal{G}_F)=\mathcal{G}_G\). **Extended-affine (EA) equivalence** is the special case \(G=A_1\circ F\circ A_2+A\) with \(A_1,A_2\) affine permutations and \(A\) affine; EA-equivalence plus taking inverses of permutations generates CCZ-equivalence. CCZ-equivalence preserves the multiset \(\{\delta_F(a,b)\}\) (hence APN-ness) and the extended Walsh spectrum, but it does **not** preserve the property of being a permutation.

**Permutation-existence criterion (the search surface).** Attach to \(F\) the linear code \(\mathcal{C}_F\subseteq\mathbb{F}_2^{2n+1}\) generated by the rows \((1,\,x,\,F(x))\); a **Walsh-zero space** of \(F\) is an \(n\)-dimensional subspace \(V\le\mathbb{F}_2^{2n}\) on which the Walsh transform of the graph indicator vanishes. Then:
\[
\text{the CCZ-class of }F\text{ contains a permutation}\iff \exists\ \text{Walsh-zero spaces } V_1,V_2\text{ with } V_1\cap V_2=\{0\}.
\]
Searching for such transversal pairs is a structured linear-algebra problem over \(\mathbb{F}_2^{2n}\), not a blind sweep of \(\mathrm{GL}(2n,\mathbb{F}_2)\); this is what makes P3 finite-in-practice.

**The question.** Does there exist a permutation \(F\) of \(\mathbb{F}_2^8\) with \(\delta(F)=2\)? More generally, for which even \(n\) does an APN permutation of \(\mathbb{F}_2^n\) exist?

Adopted scope for a session: \(n=8\). Cost is measured in verified DDT recomputations, certified CCZ-transformation matrices, certified Walsh-zero-space enumerations, and (for nonexistence within a family) DRAT clauses.

## 2. Resolution standard

A **full resolution** is either of:

- **(Existence)** an explicit permutation \(F:\mathbb{F}_2^8\to\mathbb{F}_2^8\), given as a table or univariate polynomial, together with (i) a recomputed full DDT proving \(\delta(F)=2\), and (ii) a bijectivity certificate (the sorted image multiset equals \(\mathbb{F}_2^8\)); or

- **(Nonexistence, restricted or full)** a machine-checkable proof that no APN permutation of \(\mathbb{F}_2^8\) exists - either overall, or within a precisely delimited class (e.g. all quadratic functions up to CCZ-equivalence, all functions in a stated univariate family) - carried by an isomorph-free exhaustive enumeration and/or a DRAT/LRAT UNSAT certificate for the encoded search.

The named certified forms permitted are:

- **(a) Direct construction** with a recomputed full DDT and an exact bijectivity check.
- **(b) CCZ/EA-equivalence-complete search:** every candidate quadratic APN representative is enumerated up to equivalence (via a canonical invariant and a certified equivalence test), and its entire CCZ-class is exhausted for permutation graphs by certified linear algebra over \(\mathbb{F}_2\).
- **(c) SAT/DRAT:** an encoding of "there is a permutation with \(\delta\le 2\) satisfying stated structural constraints", with a replayable UNSAT proof for nonexistence or an exhibited model for existence.
- **(d) Canonical enumeration via nauty** of the combinatorial object (the graph/design attached to a CCZ-class) to guarantee completeness of a case split.

A **restricted nonexistence** (form (b), (c), or (d) over a delimited class) is a legitimate and valuable result, but its scope must be stated exactly - which family, up to which equivalence, with which completeness certificate - and it must never be paraphrased as "no APN permutation of \(\mathbb{F}_2^8\) exists". The global existence question is resolved only by an explicit permutation or by a nonexistence proof whose scope is genuinely all of \(\mathbb{F}_2^8\).

**Not accepted as resolution.**

- A permutation with \(\delta(F)=4\) (or any \(\delta>2\)), however high its nonlinearity - that is problem 11, not this one.
- A quadratic APN *function* (non-permutation) in dimension 8, even a newly discovered CCZ-inequivalent one; millions are already known and none has yet yielded a permutation.
- A CCZ-equivalence assertion between two functions without an explicit, independently multipliable affine transformation matrix over \(\mathbb{F}_2^{2n}\).
- A solver run reporting UNSAT with no DRAT/LRAT proof, or a proof that no independent checker replays.
- An enumeration claimed "up to equivalence" whose canonicity or completeness is not certified (a missed class silently voids a nonexistence claim).
- Asymptotic or heuristic arguments ("APN permutations are expected to be rare/absent for large even \(n\)") in place of the decided \(n=8\) instance.
- An existence claim resting on a permutation whose components were only *sampled* for the APN condition rather than exhaustively counted across all \((a,b)\).
- A statistical "we searched \(N\) random candidates and found none" report presented as a nonexistence result.
- A near-miss permutation with a small number of DDT entries equal to 4, described as "almost APN".
- A Walsh-zero-space pair claimed to yield a permutation without the reconstructed permutation's DDT and bijectivity being recomputed from scratch.
- A completeness claim over "all quadratic APN in dimension 8" that silently relies on the inventory being exhaustive - the quadratic APN classification for \(n=8\) is *not* known to be complete, so a class-wide negative must state its scope as "all known/enumerated classes", not "all".

## 3. Graded partial-result targets

**P1 - Reproduce the frontier.** Rebuild the known landscape with an independent toolchain: recompute the DDT of the \(n=6\) Kim-function APN permutation and confirm \(\delta=2\) and bijectivity; recompute \(\delta\) for a corpus of known quadratic APN functions in dimension 8 and confirm APN-ness; and re-derive the Kim permutation itself from the Kim quadratic via the Walsh-zero-space criterion, validating the whole pipeline on the one even-dimension permutation that is known to exist. *Certificate:* recomputed DDTs, bijectivity checks, and the reconstructed \(n=6\) permutation, with SHA-256 over inputs and outputs, matching published invariants.

**P2 - Certified equivalence infrastructure.** Implement and validate a certified CCZ/EA-equivalence test for \(n=8\): given \(F,G\), either output an affine \(\mathcal{L}\) with \(\mathcal{L}(\mathcal{G}_F)=\mathcal{G}_G\) (which a checker multiplies out) or a certified non-equivalence via a complete CCZ-invariant (e.g. the ortho-derivative / Walsh-spectrum-based invariant), cross-checked against a canonical form computed by nauty on the attached graph. Two functions with different ortho-derivative differential spectra are certainly inequivalent; a matching invariant triggers the explicit-transformation search. *Certificate:* transformation matrices and/or invariant tables, replayed by a separate checker.

**P3 - Exhaust one CCZ-class for a permutation.** Take one quadratic APN function \(F\) on \(\mathbb{F}_2^8\) and search its full CCZ-class for a permutation graph via the Walsh-zero-space transversal criterion. Report either a permutation (⇒ existence, a full resolution) or a certified "no permutation in this class", with the enumerated Walsh-zero-space count as an auditable byproduct. *Certificate:* the enumeration of Walsh-zero spaces and admissible transversal pairs, with a replayable exhaustiveness argument.

**P4 - Class-wide certified negative.** Extend P3 to a certified, isomorph-free complete list of known dimension-8 quadratic APN classes, proving none of them contains a permutation. *Certificate:* per-class exhaustiveness certificates plus a nauty-checked completeness statement for the class list used.

**P5 - Structured-family SAT nonexistence.** Fix a symmetry-reduced ansatz (e.g. permutations invariant under a prescribed subgroup, or with a fixed univariate shape) and produce a DRAT/LRAT UNSAT proof that no APN permutation of that shape exists on \(\mathbb{F}_2^8\). The encoding carries: \(2^8\) output words as Boolean variables; a permutation constraint (each value used once, via an at-most-one/at-least-one encoding); and the APN constraint that for every \((a,b)\), \(a\neq0\), at most two \(x\) satisfy \(F(x+a)+F(x)=b\). *Certificate:* the CNF, solver version, and a replayed DRAT/LRAT proof, plus the group action used for symmetry breaking.

**P6 - New quadratic APN with permutation-favorable structure.** If existence resists, produce a genuinely new CCZ-inequivalent quadratic APN function on \(\mathbb{F}_2^8\) whose ortho-derivative or graph invariant is closer than any known class to admitting a permutation, with the invariant tabulated. *Certificate:* recomputed DDT, certified CCZ-inequivalence to the catalogued classes, invariant table.

**P7 - Full resolution of \(n=8\).** Either an explicit APN permutation of \(\mathbb{F}_2^8\) (P1-style certificate) or a global machine-checkable nonexistence proof. This is a windfall, not the expected product; the graded targets P1–P6 are the realistic session output and each is independently valuable.

## 4. Known results and prior art

- **Odd \(n\):** APN permutations are plentiful (the Gold, Kasami, Welch, Niho, inverse, and Dobbertin power maps), so the difficulty is entirely a parity phenomenon of even \(n\).
- **\(n=2\):** no APN permutation (immediate). **\(n=4\):** no APN permutation exists - a small exhaustive result, folklore/confirmed by classification of 4-bit optimal S-boxes (Leander–Poschmann on 4-bit S-boxes, ~2007) (verify).
- **\(n=6\):** exactly one known APN permutation up to CCZ-equivalence, obtained by Dillon and coauthors (Browning, Dillon, McQuistan, Wolfe, ~2009–2010) as a CCZ-image of the quadratic "Kim function" \(\kappa(x)=x^3+x^{10}+u\,x^{24}\) over \(\mathbb{F}_{2^6}\) (verify constants). Whether other CCZ-classes yield an \(n=6\) permutation was subsequently studied (verify).
- **\(n=8\) and even \(n\ge 8\):** existence **open** - "the big APN problem". No APN permutation is known in any even dimension other than \(6\).
- **Nonexistence obstructions:** several partial no-go results are known - e.g. an APN permutation of \(\mathbb{F}_2^n\) (even \(n\)) cannot be a monomial \(x^d\), and various structured families have been ruled out - but none extends to a full even-\(n\) nonexistence (Hou; Nyberg; and others) (verify).
- **Quadratic APN inventory, dimension 8:** the count of known CCZ-inequivalent quadratic APN functions has grown rapidly - on the order of tens of thousands classically known (~32,900) and, in 2024–2025 work, millions of inequivalent quadratic APN functions in eight variables were constructed (with total estimated near six million); crucially, none found so far is CCZ-equivalent to a permutation (verify counts and the "none is a permutation" status against the latest papers).
- **Method lineage:** CCZ-equivalence (Carlet–Charpin–Zinoviev, 1998); the "switching" and matrix/QAM (quadratic APN matrix) construction methods (Yu–Wang–Li, Edel–Pott, ~2009–2014) (verify); Walsh-zero-space characterizations of when a CCZ-class contains a permutation (Kaleyski, Budaghyan, and coauthors, ~2021) (verify); 2-to-1 APN function algorithms bearing on the big APN problem (~2019) (verify); Gröbner-basis / self-equivalence-subspace searches for quadratic APN in dimension 8 (2025–2026) (verify).
- **Invariants:** the ortho-derivative invariant is currently the sharpest practical CCZ-invariant for quadratic APN functions (Canteaut–Perrin and coauthors, ~2019) (verify); earlier separators used the Walsh spectrum, the differential spectrum, and the \(\Gamma\)-rank / \(\Delta\)-rank of the associated code/design (Edel–Pott) (verify).
- **Permutation criterion:** a CCZ-class contains a permutation iff its graph admits two complementary "Walsh-zero" subspaces of dimension \(n\) meeting only in \(0\); the systematic Walsh-zero-space (WZ) search over dimension-6 classes recovered the Kim permutation and, for dimension 8, has so far returned no permutation over the classes examined (Kaleyski, Budaghyan, Kölsch, and coauthors, ~2021) (verify).
- **Constructions of quadratic APN:** the QAM (quadratic APN matrix) representation, the "switching"/subspace method, and matrix/Gröbner searches over self-equivalence subspaces are the engines behind the growing dimension-8 inventory (Yu–Wang–Li; Edel–Pott; ~2009–2026) (verify).
- **Lower dimensions for calibration:** APN functions are completely classified up to CCZ-equivalence for \(n\le 5\), and the quadratic APN classification is known for \(n\le 7\) (Brinkmann–Leander; Edel–Pott; Yu–Wang–Li) (verify) - useful ground truth for the toolchain.

- **Community resources:** the "Boolean functions" wiki (Bergen), the sboxU toolkit (Perrin), and public APN/quadratic-APN databases collate representatives and invariants; use them for ground-truth cross-checks rather than as the trusted base (verify current URLs and contents).

**Web-verify the headline record tables** - the dimension-8 quadratic APN inventory and the "no permutation yet" status are actively moving; consult the Boolean-functions community pages and the most recent arXiv/ePrint papers. **Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

`[search]` first computations on one workstation:

1. **Ground truth (P1).** In SageMath, load the \(n=6\) Kim permutation and known \(n=8\) quadratic APN representatives; compute full DDTs (a \(2^n\times2^n\) tally, \(O(2^{2n})\) - trivial for \(n=6\), seconds for \(n=8\)) and bijectivity checks. Cross-implement the DDT in a small standalone C++ program for the independent check.
2. **Equivalence engine (P2).** Custom C++ for Boolean-function search: implement the ortho-derivative invariant and a certified CCZ/EA-equivalence test; build the graph/design attached to each class and canonicalize with **nauty/Traces** (or **bliss**) so class identity is certificate-backed, not string-compared. Validate against published equivalence facts.
3. **Class exhaustion (P3–P4).** For a quadratic APN \(F\), enumerate affine transformations \(\mathcal{L}\) of \(\mathbb{F}_2^{16}\) that make \(\mathcal{L}(\mathcal{G}_F)\) a function graph, then test bijectivity - the Walsh-zero-space / linear-algebra criterion makes this a structured \(\mathbb{F}_2\) linear-algebra sweep rather than brute force over \(16\times16\) matrices. Use **GAP** for the affine/matrix group bookkeeping and orbit enumeration.
   The two workhorses here are Gaussian elimination over \(\mathbb{F}_2\) (to enumerate Walsh-zero spaces) and orbit-stabilizer counting under the automorphism group of the class (to avoid re-testing symmetric transversals); both are exact and cheap per class, with the class count the only real budget question.
4. **SAT route (P5).** Encode "permutation of \(\mathbb{F}_2^8\) with \(\delta\le 2\) and structural constraints \(S\)" as CNF; run **CaDiCaL**/**kissat**/**CryptoMiniSat** with proof logging; on UNSAT, replay the **DRAT/LRAT** proof with `drat-trim`/`lrat-check`. Symmetry-break aggressively (fix images of a basis, quotient by the ansatz group) or the raw instance is hopeless.
5. **Walsh-zero enumeration (P3–P4).** For each target class, enumerate the \(n\)-dimensional Walsh-zero spaces via exact \(\mathbb{F}_2\) linear algebra, then test all transversal pairs \((V_1,V_2)\) with \(V_1\cap V_2=\{0\}\); a surviving pair reconstructs a candidate permutation whose DDT and bijectivity are recomputed from scratch. Record the count of Walsh-zero spaces per class as an auditable intermediate.
6. **Structure mining (P6).** Tabulate ortho-derivative and Walsh-spectrum invariants across the known dimension-8 classes; rank by proximity to permutation-admissibility criteria (number and intersection pattern of Walsh-zero spaces) to steer where new quadratic APN construction (QAM/switching, Gröbner over a self-equivalence subspace in SageMath/Singular) is worth the compute.
7. **Small-analogue calibration.** Rehearse the entire pipeline on \(n=6\) (where the Kim permutation is the ground-truth positive) and on \(n=4\) (ground-truth negative), confirming the Walsh-zero enumeration and the SAT nonexistence route each reproduce the known answer before committing compute at \(n=8\).

**One-workstation scope and failure modes.** DDT and bijectivity checks for \(n=8\) are cheap; the hazards are elsewhere.

- *Search blow-up:* the raw CCZ-transformation space is astronomically large - only the Walsh-zero-space structure makes P3 finite-in-practice; an unstructured sweep will not terminate.
- *Canonicity bugs:* a faulty CCZ-invariant or a mis-set nauty canonical form silently merges or splits classes, voiding any completeness claim - dual-implement the invariant.
- *Unverified solver output:* treat every UNSAT as unproven until a separately built DRAT/LRAT checker replays it.
- *Completeness of the class list:* a nonexistence-within-known-classes claim is only as strong as the certified completeness of "the known classes"; state precisely which list, with hashes.
- *Memory and I/O:* the full million-entry class inventory may not fit in RAM - stream, hash, and checkpoint rather than materialize.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every APN claim rests on an exactly recomputed DDT over \(\mathbb{F}_2^n\) and every permutation claim on an exact bijectivity check; every CCZ-equivalence claim on an explicit affine matrix over \(\mathbb{F}_2^{2n}\) that a checker multiplies out; every nonexistence on an isomorph-free enumeration or a DRAT/LRAT proof. No floating point enters a load-bearing step.
2. **Independent verification.** For each certificate a small standalone checker, written separately from the search code: a DDT/bijectivity re-evaluator in a second language, a CCZ-transformation replayer, a Walsh-zero-space transversal re-checker, a DRAT/LRAT checker (`drat-trim`, `lrat-check`), and a nauty-based recanonicalization of any class list. Dual-implement the ortho-derivative invariant, since it is the load-bearing class separator.
3. **Reproducibility.** Record the field representation (primitive polynomial), all encodings, solver and nauty/GAP/SageMath versions, seeds, and a SHA-256 manifest over every function table, matrix, CNF, and proof. Cite the exact baseline inventory of known dimension-8 quadratic APN classes being used, with source and access date, so any "new class" or "none is a permutation" claim is unambiguous.
4. **Preservation.** All search and construction source - the equivalence engine, the SAT encoders, the enumeration drivers - is part of the record; anything not preserved is stated explicitly (heed the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front whether the Section 2 standard was met: an explicit permutation, a certified restricted nonexistence (naming the class and its certified completeness), or neither. A new quadratic APN function, a permutation-*favorable* invariant, or a heuristic near-miss is reported as exactly that and never represented as settling the big APN problem for \(n=8\).

A closing calibration for the session lead: the realistic product of a first session is P1–P4 - a validated toolchain, a certified equivalence engine, and one or more classes proved permutation-free - not the headline. The headline (an explicit \(n=8\) APN permutation, or a global nonexistence proof) would be a genuine breakthrough; treat any apparent hit with maximal suspicion and re-verify from scratch with an independently written checker before making any claim.
