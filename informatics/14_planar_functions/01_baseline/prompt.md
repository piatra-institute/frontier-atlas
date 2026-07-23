# PROMPT FOR PLANAR (PERFECT-NONLINEAR) FUNCTIONS AND COMMUTATIVE SEMIFIELDS

## Existence and classification of planar functions \(\mathbb{F}_{p^n}\to\mathbb{F}_{p^n}\) for odd \(p\), and their semifields

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 14 of 50
**Area:** Boolean & cryptographic functions
**Modes:** `[search]` `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A planar (perfect-nonlinear) function over a field of odd characteristic is the sharpest possible object against differential attacks in the odd-prime world: every nonzero directional derivative is a bijection. Planar functions are equivalent to commutative (pre)semifields via the Dembowski–Ostrom correspondence and to a rich family of finite projective planes and skew-Hadamard difference sets - a place where cryptography, finite geometry, and algebra coincide. Classification is complete only in small cases (all commutative semifields of order \(3^5\), planar functions in characteristic 3 up to a degree, monomial planar functions), and existence/classification for many specific \((p,n,\text{degree})\) is **open**. The task fits symbolic-algebraic computation and certified search: planarity is an exact 2-to-1 condition on the derivative map over \(p^n\) elements, equivalence is governed by CCZ/isotopism and by nauty canonical forms on the attached semifield/plane, and the productive families (Dembowski–Ostrom polynomials) are algebraic enough to enumerate and to test. The on-machine verifier is a direct check that every nonzero derivative is bijective; anything short of the Section 2 standard - a family with no certified completeness, an equivalence claim without a certificate - is a partial result, never a classification.

## 1. Exact problem statement

Let \(p\) be an odd prime and \(q=p^n\); \(\mathbb{F}_q\) the finite field, \(\mathbb{F}_q^\ast\) its multiplicative group. For \(F:\mathbb{F}_q\to\mathbb{F}_q\) and \(a\in\mathbb{F}_q^\ast\), the **directional derivative** is \(D_aF(x)=F(x+a)-F(x)\). \(F\) is **planar** (equivalently **perfect nonlinear, PN**) iff
\[
D_aF:\ x\mapsto F(x+a)-F(x)\ \text{ is a bijection of }\mathbb{F}_q\quad\text{for every }a\in\mathbb{F}_q^\ast,
\]
equivalently the equation \(F(x+a)-F(x)=b\) has exactly one solution \(x\) for every \(a\neq0\) and every \(b\). (No planar function exists in characteristic 2; the analog there is the almost-bent / APN world - cross-reference problems 08 and 10.)

A **Dembowski–Ostrom (DO) polynomial** is \(F(x)=\sum_{i,j} a_{ij}\,x^{p^i+p^j}\) (all monomial exponents have \(p\)-weight \(2\)), plus possibly an additive/linear term; a planar DO polynomial is exactly one whose associated symmetric bilinear form \(B(x,y)=F(x+y)-F(x)-F(y)\) is nondegenerate. The **multiplication** \(x\ast y=B(x,y)\) (suitably normalized) makes \((\mathbb{F}_q,+,\ast)\) a **commutative presemifield**; conversely every commutative presemifield of odd order yields a planar DO polynomial. Two planar DO polynomials give **isotopic** semifields iff they are related by the appropriate equivalence (**CCZ-equivalence** coincides with **isotopism** for planar DO functions, up to the standard caveats - Budaghyan–Helleseth).

A **presemifield** is a structure \((\mathbb{F}_q,+,\ast)\) with two-sided distributivity and no zero divisors (a unit is not required; adjoining one gives a **semifield**); it is **commutative** when \(\ast\) is. **Isotopism** is the equivalence \((\mathbb{F}_q,+,\ast)\sim(\mathbb{F}_q,+,\star)\) when there are additive bijections \(L,M,N\) with \(N(x\ast y)=L(x)\star M(y)\); it is exactly the relation under which two presemifields coordinatize the same projective plane. For planar DO functions, CCZ-equivalence coincides with isotopism (Budaghyan–Helleseth), so the enumeration counts isotopism classes. Every commutative semifield yields a projective plane of Lenz–Barlotti type V.1, and non-isotopic semifields can still give isomorphic planes, so plane-isomorphism is a coarser invariant that must be tracked separately.

The bilinear form \(B(x,y)=F(x+y)-F(x)-F(y)\) is **nondegenerate** iff \(B(x,y)=0\ \forall y\Rightarrow x=0\); planarity of a DO \(F\) is exactly this nondegeneracy, checkable as an \(\mathbb{F}_p\)-rank condition. In characteristic 2 the form \(B\) is alternating, forcing degeneracy, which is why no planar functions exist there - the analog is the bent/APN/AB world (cross-reference problems 08, 10).

Non-DO planar functions also exist (the Coulter–Matthews planar monomial \(x^{(3^k+1)/2}\) over \(\mathbb{F}_{3^n}\), \(k\) odd, \(\gcd(k,n)=1\), is planar but not DO, and its plane is not a translation plane); these are of separate interest.

The planarity test is exact and cheap at the target orders: for each of the \(p^n-1\) nonzero \(a\), the derivative \(x\mapsto F(x+a)-F(x)\) is tabulated and checked bijective, an \(O(p^{2n})\) integer computation. For a DO \(F\) the whole test reduces to one \(\mathbb{F}_p\)-rank check on the bilinear form \(B\). The verifier is entirely arithmetic over \(\mathbb{F}_{p^n}\); no numerical approximation appears.

**The questions, adopted scope.** For specified \((p,n)\) with open cells (primary \(p=3\), \(n=6,7,8\); secondary small \(p=5,7\)):
(i) certified **classification** of planar functions (or planar DO polynomials / commutative semifields) up to CCZ-equivalence/isotopism within a fixed degree or family;
(ii) certified **existence/nonexistence** of new (in)equivalent planar functions for target parameters;
(iii) the **almost-bent characteristic-2 analog** where relevant (existence of AB functions in a fixed odd \(n\), cross-referenced to problem 10). Cost: exact planarity checks, certified isotopism/CCZ tests, nauty canonical forms on the attached semifield/plane.

## 2. Resolution standard

A **full resolution** of a scoped instance is one of:

- **(Classification)** a certified isomorph-free list (or count) of the planar functions / commutative semifields for the target \((p,n,\text{class})\) up to isotopism/CCZ-equivalence, with a machine-checkable **completeness certificate** (exhaustive canonical generation over the coefficient space, or a certified reduction to a finite orbit problem);
- **(Existence/nonexistence)** an explicit new planar function with a recomputed planarity check and a certified inequivalence to all catalogued ones, or a machine-checkable nonexistence proof for a target family.

Named certified forms:

- **(a) Explicit construction** with a recomputed planarity check (every nonzero derivative bijective).
- **(b) CCZ/isotopism-equivalence-complete search** over a coefficient family, with certified equivalence tests and **nauty** canonicalization of the attached semifield multiplication table / projective plane.
- **(c) Exhaustive/canonical enumeration** via nauty or **GAP** orbit computation guaranteeing a case split is complete.
- **(d) Gröbner-basis / algebraic elimination** (Singular/Macaulay2) certifying that a parameterized planarity system has exactly the claimed solution set.

A classification within a delimited family, or a certified lower bound on the isotopism-class number at an open order, is a legitimate reportable increment; a *complete* classification for \((p,n)\) additionally requires that non-DO functions and the full coefficient space are covered, and is labelled distinctly.

**Not accepted as resolution.**

- A new planar function with **no** certified inequivalence to the known catalogue - a candidate, not a new object.
- A planarity assertion whose derivative-bijectivity is not independently recomputed over all \(a\neq0\).
- An isotopism/CCZ-equivalence claim without an explicit transformation (or a certified complete invariant) a checker can verify.
- A semifield presented without its nuclei orders, which are the cheapest isotopism invariants and are expected in any report.
- A relative-difference-set or plane claim not reconciled with the underlying planar function's recomputed derivative table.
- A within-family classification presented as a classification of *all* planar functions for \((p,n)\) without a certified completeness argument.
- A planarity claim for a *non-DO* function reduced to the DO bilinear-form test (the reduction is only valid for DO polynomials).
- An isotopism-class count that omits whether non-DO planar functions in the order were considered.
- A count of semifields from string-comparing multiplication tables without a certified canonical form (nauty).
- An unreplayable Gröbner/solver run, or a heuristic "these seem to be all" in place of a completeness certificate.
- A count of *semifields* conflated with a count of *planes* - non-isotopic semifields can coordinatize isomorphic planes; state which is counted.
- A "new semifield" whose nuclei / order invariants were not computed to distinguish it from known families.
- A characteristic-2 object described as "planar" - planarity requires odd \(p\); the char-2 analog is AB/APN and belongs to problems 08, 10.
- An isotopism claim tested only up to field automorphisms rather than the full additive-bijection triple \((L,M,N)\).
- A Gröbner "solution set" reported without the certificate that the ideal computation terminated over the exact base field.

## 3. Graded partial-result targets

**P0 - Planarity-test base case.** Validate the planarity checker on \(x^2\) over small \(\mathbb{F}_{p^n}\) (always planar) and on a deliberately non-planar DO polynomial (degenerate \(B\)), confirming two independent implementations agree on the all-derivatives-bijective verdict. Also confirm the char-2 guard: the checker must reject any even-characteristic input as ill-posed. *Certificate:* recomputed derivative tables with cross-implementation agreement.

**P1 - Reproduce the frontier.** Independently verify canonical planar functions: the DO planar monomials \(x^2\) and \(x^{p^k+1}\) (with \(\gcd\) conditions), and the Coulter–Matthews monomial \(x^{(3^k+1)/2}\) over \(\mathbb{F}_{3^n}\); recompute planarity (all nonzero derivatives bijective) and, for DO cases, the semifield multiplication table. *Certificate:* recomputed derivative-bijectivity tables with SHA-256, matching known families.

**P2 - Equivalence & semifield infrastructure.** Implement a certified isotopism/CCZ-equivalence test for planar DO functions, build the attached commutative-semifield multiplication table and (where useful) the projective plane, and canonicalize with **nauty**; validate against the known classification of small semifields (e.g. order \(3^4,3^5\)). The isotopism test searches the additive-bijection triple \((L,M,N)\); the nuclei invariants prune it drastically. *Certificate:* transformation data / canonical labels replayed by a separate checker.

**P3 - Reproduce a small classification.** Reproduce, with a certified completeness argument, the classification of all commutative semifields (equivalently planar DO polynomials up to isotopism) of a small order, e.g. \(3^5\) or \(5^3\). Recompute the isotopism-class count two ways (canonical-list length and GAP orbit count) and match the published total. *Certificate:* isomorph-free enumeration completeness plus recomputed planarity and nuclei invariants for each representative.

**P4 - Classify a fixed family at an open order.** For an open \((p,n)\), classify the planar DO polynomials within a delimited coefficient family (e.g. planar binomials \(x^{p^i+1}+cx^{p^j+1}\), or a fixed nucleus structure) up to isotopism, with a completeness certificate. The binomial family is small enough that Gröbner elimination can certify the exact planar locus and the isotopism quotient can be computed in full. *Certificate:* canonical-generation completeness + nauty-checked distinctness + Gröbner certificate for the planar locus.

**P5 - New planar function / semifield.** Exhibit a planar function (or commutative semifield) for a target \((p,n)\) that is certified inequivalent to all catalogued ones, or certify that a targeted family yields nothing new. Inequivalence must be witnessed by a computed invariant (nuclei orders differ) or by an exhaustive isotopism search returning no transformation. *Certificate:* recomputed planarity + certified inequivalence, or a certified-exhaustion negative.

**P5b - Improve a class-number bound.** For an open order, prove a certified lower bound on the number of isotopism classes of commutative semifields by exhibiting that many pairwise-inequivalent representatives with distinguishing invariants. *Certificate:* the representatives, their invariants, and pairwise-inequivalence proofs.

**P6 - Characteristic-2 companion.** Produce a certified classification/enumeration of almost-bent functions in a fixed odd \(n\) (the characteristic-2 analog), up to CCZ/affine equivalence, cross-referenced to the APN inventory (problem 08) and bent-companion work (problem 10). *Certificate:* recomputed Walsh spectra \(\{0,\pm2^{(n+1)/2}\}\) + certified equivalence classes.

**P7 - Nucleus-refined invariants.** For a family of known and candidate semifields at a target order, compute and tabulate the full invariant set (nuclei orders, center, plane collineation group, autotopism group) and use it to certify the exact number of isotopism classes present. *Certificate:* invariant tables plus a nauty-backed distinctness proof.

## 4. Known results and prior art

- **Correspondence:** commutative presemifields of odd order \(\leftrightarrow\) planar DO polynomials (Dembowski–Ostrom, ~1968; Coulter–Henderson; Budaghyan–Helleseth) - for planar DO functions, CCZ-equivalence \(=\) isotopism of the associated semifields (verify).
- **Planarity and finite planes:** a planar function of order \(q\) yields an affine plane of order \(q\); Dembowski–Ostrom conjectured the associated planes are translation planes, which holds for DO functions but fails for Coulter–Matthews (verify).
- **Monomial planar functions:** classified - the planar power functions over \(\mathbb{F}_{p^n}\) are essentially \(x^2\), the Gold-type \(x^{p^k+1}\) with \(n/\gcd(n,k)\) odd, and the Coulter–Matthews \(x^{(3^k+1)/2}\) over characteristic 3 (Coulter–Matthews, ~1997; Zieve and others) (verify).
- **Non-monomial families:** new commutative semifields / planar DO multinomials over \(\mathbb{F}_{p^{2k}}\) (Zha–Kyureghyan–Wang; Bierbrauer; Budaghyan–Helleseth; Pott–Zhou; ~2008–2013), many giving new semifields for \(k\) odd, \(p\neq3\) (verify).
- **Small-order classifications:** all commutative semifields of order \(3^5\) are classified; classifications in characteristic 3 up to a fixed degree, and of certain semifield orders (e.g. \(3^4=81\), \(5^3=125\)) are known (verify exact orders classified). The number of commutative-semifield isotopism classes is \(1\) for the prime-order and prime-square-order cases and grows from the first genuinely non-field order; the exact small-order counts are the ground-truth for a reproduction (verify the specific figures).
- **Kloosterman/Weil-bound tools** and the connection to skew-Hadamard difference sets and relative difference sets (Weng–Zeng; Ding–Yuan; ~2007) (verify).
- **Relative difference sets:** a planar function of order \(q\) is equivalent to a \((q,q,q,1)\) relative difference set in \(\mathbb{F}_q\times\mathbb{F}_q\), giving a design-theoretic route to invariants and canonicalization (verify).
- **Characteristic-2 analog:** almost-bent (AB) functions meet the odd-dimension nonlinearity bound and are APN; the Gold/Kasami/Welch/Niho families are the classical AB monomials (cross-reference problems 08, 10) (verify).
- **Semifield taxonomy:** the known commutative semifields include Albert's generalized twisted fields, Dickson semifields, and the Coulter–Matthews, Zha–Kyureghyan–Wang, Bierbrauer, and Budaghyan–Helleseth families; the standard references are Knuth's semifield work (~1965) and Lavrauw–Polverino's survey (~2011) (verify).
- **Plane vs semifield counts:** the number of commutative semifields of a given order and the number of the planes they coordinatize differ; small-order tables (orders \(16,32,64,81,243,\ldots\)) are catalogued (Rúa–Combarro–Ranilla for order \(64\); ~2009) (verify - order \(64\) is char 2, use for methodology only).
- **Bounds on class numbers:** the number of isotopism classes grows with the order; exact counts are known only for small orders, and improving a count or exhibiting a new class at an open order is the live frontier (verify).
- **Biprojective and \((q,q)\)-families:** recent classifications of biprojective and \((q,q)\)-biprojective APN/planar functions give structured families amenable to certified search (Göloğlu; Kaspers–Zhou; ~2021–2022) (verify).
- **Isotopism vs strong isotopism:** the finer "strong isotopism" and the "principal isotopism" notions matter when relating semifields to their planes; fix which is used (verify).
- **Community resources:** finite-geometry semifield databases and the "Boolean functions" wiki's planar/PN pages collate representatives and invariants; use for cross-checks, not as the trusted base (verify current URLs).
- **Cross-reference:** the characteristic-2 companion (AB/APN) shares the CCZ-equivalence engine of problem 08 and the almost-bent target of problem 10; reuse that infrastructure for P6.

**Web-verify the headline record tables** - the semifield/planar-function classification status and the newest multinomial families move; consult the finite-geometry / Boolean-functions community pages, semifield catalogues, and recent journals/ePrint. **Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

`[search]` `[sym]` first computations on one workstation:

1. **Verified planarity test (P0–P1).** In **SageMath**/**GAP**, over \(\mathbb{F}_{p^n}\): for each \(a\neq0\) form the map \(x\mapsto F(x+a)-F(x)\) and check bijectivity (image multiset \(=\mathbb{F}_q\)); \(F\) is planar iff all \(p^n-1\) derivatives pass - an exact \(O(p^{2n})\) check, cheap for the target orders. For DO \(F\), also verify via the single \(\mathbb{F}_p\)-rank test on \(B\), and confirm the two verdicts agree. Cross-implement in **custom C++** for the independent check.
2. **Semifield / equivalence engine (P2).** Build the associated commutative-semifield multiplication and the isotopism/CCZ-equivalence test; canonicalize the multiplication table (or the attached plane / difference set) with **nauty/Traces**; use **GAP** for the isotopism group orbits and the finite-field algebra. Validate on small classified orders.
3. **Algebraic elimination (P4).** Parameterize a DO coefficient family and encode planarity (nondegeneracy of the bilinear form \(B\)) as a polynomial system over \(\mathbb{F}_p\); use **Gröbner bases** in **Singular**/**Macaulay2** to certify the exact solution set, then quotient by isotopism. The nondegeneracy condition is a determinant non-vanishing, so the "planar in this family" locus is a constructible set whose defining ideal the Gröbner computation makes explicit.
4. **Canonical enumeration (P3, P5).** For a fixed order, enumerate DO coefficient tuples up to isotopism by orderly generation + nauty canonical forms; planarity-test survivors; count classes two ways (canonical-list length and a GAP orbit count). Seed the enumeration with the known families (twisted fields, Dickson, Zha–Kyureghyan–Wang) so the reproduction target is exercised before novelty is claimed.
5. **Nucleus/invariant computation (P2, P5).** For each semifield representative compute the left/middle/right nuclei and center (their orders are isotopism invariants) and the plane's collineation-group order; these separate isotopism classes cheaply and flag genuinely new objects.
6. **Companion AB search (P6).** Reuse the CCZ/affine-equivalence engine (problem 08) to enumerate almost-bent candidates in a fixed odd \(n\) and verify their Walsh spectra.

Target orders to attack first, smallest planarity-check cost first:

- \(5^3=125\), \(7^3=343\) - small odd-characteristic base cases for the engine.
- \(3^5=243\) - a fully classified order; the primary validation target.
- \(3^6=729\), \(3^7=2187\), \(3^8=6561\) - the open characteristic-3 frontier.
- \(5^4=625\), \(7^4=2401\) - even-exponent orders where multinomial families for \(p\neq3\) live.
- \(3^9,3^{10}\) - larger characteristic-3 orders, feasible only with heavy nucleus/symmetry pruning.

**One-workstation scope and failure modes.**

- *Planarity check cheap for small orders* but the *coefficient space* of DO families grows fast - restrict by nucleus/symmetry to stay finite-in-practice.
- *Canonicity bugs* on the semifield multiplication table silently merge or split isotopism classes - validate on classified small orders and cross-check counts.
- *Isotopism vs CCZ vs plane-isomorphism:* fix and state the equivalence; the DO caveat (isotopism \(=\) CCZ) must be respected, and plane-isomorphism is coarser than isotopism.
- *Gröbner blow-up:* elimination over large families may not terminate on one workstation - scope honestly.
- *Characteristic confusion:* planar functions require odd \(p\); the char-2 companion is a different object (AB/APN) and must not be conflated.
- *Isotopism-search cost:* the \((L,M,N)\) triple search is expensive without invariant pruning; compute nuclei first and only run the full search on invariant-matching pairs.
- *Non-DO blind spots:* a DO-only enumeration says nothing about non-DO planar functions at the order - state the scope, and treat non-DO existence as a separate question.
- *Memory on multiplication tables:* a full \(q\times q\) semifield table for the larger target orders is sizeable - stream and hash rather than hold all candidates in RAM.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every planarity claim is an exact all-derivatives-bijective check over \(\mathbb{F}_{p^n}\) (or the equivalent \(\mathbb{F}_p\)-rank test for DO functions); every isotopism/CCZ-equivalence a certified transformation or complete invariant; every classification an isomorph-free enumeration or a Gröbner-certified solution set; every count a nauty-backed canonical total. No floating point in a load-bearing step.
2. **Independent verification.** Two independently written planarity testers agree on every function; every equivalence transformation is replayed by a checker; every semifield multiplication table is recanonicalized by a separate nauty run; every class total is confirmed two ways (canonical list vs. GAP orbit count); every nucleus/plane invariant is recomputed by a second routine to certify inequivalence claims.
3. **Reproducibility.** Record the field representation, DO coefficient parameterization, equivalence notion (isotopism/CCZ/plane-isomorphism), all encodings, and tool versions (SageMath, GAP, nauty, Singular/Macaulay2), with a SHA-256 manifest over every function, multiplication table, canonical label, and Gröbner certificate. Cite the semifield/planar-function catalogue baseline (source, access date). State whether counts are of functions, isotopism classes, or planes.
4. **Preservation.** All planarity-test, equivalence, enumeration, and algebra source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson). Every semifield multiplication table and every Gröbner certificate is archived in full, not summarized.
5. **Honest reporting.** The report states up front the exact \((p,n,\text{class})\) for which completeness is certified, whether a *classification/count*, a *new inequivalent object*, or only a *construction* was produced, and under which equivalence. A within-family classification is never presented as covering all planar functions for \((p,n)\), and a candidate lacking a certified inequivalence is never presented as a new semifield.

Calibration for the session lead: the realistic product is P1–P3 - a validated planarity/isotopism engine and a reproduced small-order classification (e.g. \(3^5\)) - plus, with luck, a certified classification of a fixed DO family at an open order (P4) or a new certified-inequivalent semifield (P5). A complete classification of *all* planar functions at an open order is generally out of reach; the value is in exact, certified statements about well-delimited coefficient families and in rigorously new isotopism classes with computed invariants.
