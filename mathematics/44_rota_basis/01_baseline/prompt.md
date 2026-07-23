# PROMPT FOR CERTIFIED VERIFICATION OF ROTA'S BASIS CONJECTURE AT AN OPEN ORDER

## Rota's basis conjecture: arranging n bases into an n×n grid of rows-and-columns bases

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 44 of 50  
**Area:** number theory & algebra  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Rota's basis conjecture states that given \(n\) bases \(B_1,\dots,B_n\) of an \(n\)-dimensional
vector space (more generally, \(n\) disjoint bases of a rank-\(n\) matroid), the \(n^2\) vectors can be
arranged in an \(n\times n\) array so that row \(i\) is exactly \(B_i\) and **every column is also a
basis**. It is proved for small \(n\), for paving matroids (Geelen–Humphries), for strongly
base-orderable matroids, for \(n=p\pm1\) over characteristic \(0\) via the Alon–Tarsi conjecture (#43,
Huang–Rota/Onn), and asymptotically to half the rows (Bucić–Kwan–Pokrovskiy–Sudakov). This is a
`[search]` problem: for a fixed order, a fixed field or matroid class, the statement is a finite family
of constraint-satisfaction instances, each solved by SAT/backtracking with an explicit arrangement
certificate, and the family made complete by isomorph-free (\(GL_n\)-orbit / matroid-isomorphism)
enumeration. The resolution standard in section 2 is the target for a specified open order and class;
verifying random configurations, or a single case, or omitting the completeness argument, is reported
as a partial result and never as resolving the conjecture.

## 1. Exact problem statement

Let \(V\) be an \(n\)-dimensional vector space over a field \(K\), and let \(B_1,\dots,B_n\) be bases
of \(V\), each \(B_i=\{b_{i,1},\dots,b_{i,n}\}\). A **Rota arrangement** is an \(n\times n\) array
\(A=(A_{i,c})\) of vectors such that:

1. **row condition:** \(\{A_{i,1},\dots,A_{i,n}\}=B_i\) as a set (row \(i\) is a permutation of \(B_i\));
2. **column condition:** for every \(c\), \(\{A_{1,c},\dots,A_{n,c}\}\) is a basis of \(V\).

**Rota's basis conjecture (vector-space form).** For every \(K\), every \(n\), and every choice of
bases \(B_1,\dots,B_n\), a Rota arrangement exists.

**Matroid form (Huang–Rota).** For a matroid \(M\) of rank \(n\) and \(n\) pairwise disjoint bases
\(B_1,\dots,B_n\), the \(n^2\) elements can be arranged in an \(n\times n\) array with row \(i\) equal
to \(B_i\) and every column a basis of \(M\).

Choosing coordinates, \(B_i\) is an invertible \(n\times n\) matrix over \(K\); "column \(c\) is a
basis" means the matrix formed by the \(c\)-th chosen vector of each row is invertible
(\(\det\neq0\) over \(K\), or nonzero rank over the matroid). A **counterexample at order \(n\)** is
bases \(B_1,\dots,B_n\) for which **no** arrangement satisfies the column condition - a finite,
exactly checkable object. Over a finite field \(\mathbb F_q\) the set of base-tuples is finite, so
the conjecture at fixed \(n,q\) is a finite (large) statement; over infinite fields one reduces to
finitely many matroid/genericity types.

An order \(n\) is **open** here when it is neither settled by direct computation (small \(n\); the
literature reaches \(n\le4\) - **verify**) nor by a structural theorem (paving / strongly-base-orderable
matroids; \(n=p\pm1\) over characteristic \(0\)). Concrete `[search]` targets: \(n\in\{5,6,7\}\) over
\(\mathbb F_2,\mathbb F_3\) and over the small-matroid catalogue; over characteristic \(0\) the first
order not covered by Alon–Tarsi is \(n=26\) (mirroring #43).

## 2. Resolution standard

A **complete resolution** is a proof of Rota's basis conjecture for all \(n\) and all
fields/matroids (formalized to the standard below), **or** an explicit **counterexample**: bases
\(B_1,\dots,B_n\) with a machine-checkable proof that no arrangement makes every column a basis
(exhaustive over the \((n!)^{n}\) row-permutation choices, each column tested by exact determinant).

Because a full proof is a windfall, the certified deliverable is a **certified exhaustive verification
for a specified open order \(n\) and class**: a proof that **every** configuration in that class admits
a Rota arrangement, consisting of (a) a per-configuration arrangement certificate and (b) a
**completeness argument** that the enumerated configurations exhaust the class up to isomorphism.

**Certified form.** (i) "Is a basis" is decided by **exact determinant/rank** over \(K\) (\(\mathbb Q\)
or \(\mathbb F_q\)), never floating point. (ii) Each configuration's arrangement-existence instance is
solved by **SAT with a DRAT/LRAT proof** (UNSAT of "no arrangement" ⇒ arrangement, or a model directly
giving the arrangement) or by exhaustive backtracking with a **replayable** log; the produced
arrangement is re-verified independently. (iii) Completeness of the configuration set is an
**isomorph-free enumeration** - \(GL_n(\mathbb F_q)\)-orbit representatives of base-tuples, or the
catalogue of rank-\(n\) matroids on the relevant ground set - with the orbit/canonical-form argument
recorded. (iv) Small-\(n\) and structural cases are candidates for **Lean 4 + mathlib**.

**Not accepted as resolution.**
- Verifying randomly sampled configurations without a completeness argument.
- A single configuration's arrangement presented as verifying order \(n\).
- Floating-point rank/determinant tests.
- "No counterexample found" from an incomplete search presented as a proof.
- A result for one field presented as holding over all fields.
- The Alon–Tarsi implication (\(n=p\pm1\), characteristic \(0\)) re-stated as new for a genuinely open order.

## 3. Graded partial-result targets

**P1 - Reproduce the settled frontier.** Certified exhaustive verification for \(n\le4\) (or the current
proven bound) over \(\mathbb F_2,\mathbb F_3\), and a certified derivation of the Alon–Tarsi \(\Rightarrow\)
Rota implication for \(n=p\pm1\) over \(\mathbb Q\) (tie to #43). *Certificate:* per-orbit arrangement
certificates + complete \(GL_n\)-orbit enumeration; the AT-linked argument written out.

**P2 - Certified verification at the smallest open order over a small field.** For \(n\in\{5,6,7\}\)
over \(\mathbb F_2\) (then \(\mathbb F_3\)): enumerate \(GL_n\)-orbit representatives of base-tuples and
certify each admits an arrangement. *Certificate:* per-configuration DRAT/replay + exact-determinant
column checks, plus the orbit-completeness argument and a **SHA-256 manifest**.

**P3 - Matroid version over the small-matroid catalogue.** Verify the matroid form for all rank-\(n\)
matroids on a bounded ground set (small-\(n\) catalogue), with per-instance arrangement certificates.
*Certificate:* the matroid list (with isomorphism-completeness), per-matroid arrangements, exact rank
checks.

**P4 - Counterexample search at larger \(n\)/field.** SAT-encode arrangement existence for a specified
\(n\) over \(\mathbb F_q\) and search for an unsatisfiable configuration (a counterexample), with DRAT
proofs certifying satisfiability where found. *Certificate:* the encoding, the per-instance proofs, and
the search scope.

**P5 - Structure mining.** Identify the hardest configurations (fewest valid arrangements), the role of
the Latin-square/Alon–Tarsi structure, and degrees of freedom; form a precise conjecture. *Certificate:*
exact data with an honest multiple-testing account.

**P6 - Formalize a case.** Lean 4 proof of a small-\(n\) case or of the paving / strongly-base-orderable
theorem, giving the search a formal anchor. *Certificate:* the compiled development.

**P7 - A new certified class.** Prove Rota for a matroid family beyond the known classes via structured
search + a certified reduction. *Certificate:* the class definition, the reduction proof, and a
verified smallest instance.

## 4. Known results and prior art

- **Rota (c. 1989)** - posed the conjecture (transmitted via Huang); part of Rota's "colorful"/algebraic
  program.
- **Huang, Rota (1994)** - the matroid generalization and the link to the Alon–Tarsi conjecture (#43)
  through the supersymmetric bracket algebra; \(\mathrm{AT}(n)\neq0\) implies Rota over characteristic
  \(0\) for order \(n\).
- **Chan (c. 1995)** - verification of small orders (up to \(n=4\) - verify).
- **Onn (1997)** - a colorful reformulation.
- **Geelen, Humphries (2006)** - Rota's basis conjecture for paving matroids.
- **Strongly base-orderable matroids** - the conjecture holds (folklore/verify attribution).
- **Wild; Cheung; Dong–Geelen** - small cases and structural partials (verify).
- **Bucić, Kwan, Pokrovskiy, Sudakov (2020)** - "Halfway to Rota's basis conjecture": one can fill
  \((\tfrac12-o(1))n\) rows with disjoint transversal bases (possible later improvements - verify).
- Over characteristic \(0\), Rota holds for \(n=p\pm1\) via Drisko/Glynn on Alon–Tarsi; the first
  characteristic-\(0\) order not so covered is \(n=26\) (verify).

**Status as of mid-2026 - re-verify against the current literature before starting any session**
(the proven small-order bound, the structural classes, and the asymptotic fraction all drift; several
nearby problems fell in 2019–2024).

## 5. Attack plan

**`[search]` exact linear algebra core.** In **SageMath** / **Pari-GP**, represent bases as invertible
matrices over \(\mathbb F_q\) or \(\mathbb Q\); the column condition is an exact determinant test.
Build a per-configuration arrangement-existence checker (exhaustive over row permutations for tiny
\(n\); SAT for larger).

**`[search]` SAT encoding.** Encode "row \(i\) uses permutation \(\pi_i\in S_n\); every column is a
basis" with Boolean variables for the per-row permutation and clauses forbidding column dependence
(precompute, over \(\mathbb F_q\), which column vector-sets are dependent - an exact determinant scan).
Solve with **CaDiCaL/kissat/CryptoMiniSat**, emitting **DRAT/LRAT**; a model yields the arrangement,
which is re-verified by exact determinants.

**`[enum]` completeness.** Enumerate configurations up to isomorphism: \(GL_n(\mathbb F_q)\)-orbit
representatives of base-tuples (canonical form / orbit stabilizer), or the small-matroid catalogue with
**nauty**-style canonical labeling. Record the orbit argument so "all configurations" is provable, not
assumed.

**`[cert]` formalization.** In **Lean 4 + mathlib**, formalize a small-\(n\) case or a structural class
(P6), and the AT \(\Rightarrow\) Rota implication (with #43).

**One-workstation scope and failure modes.** The configuration space explodes with \(n\) and \(q\):
even \(GL_n(\mathbb F_2)\)-orbit enumeration is heavy by \(n=6,7\), so report the exact \((n,q)\) range
certified and the completeness argument for it, never an extrapolation. SAT instances are individually
easy but there are enormously many; the bottleneck is *complete* orbit coverage, not any single solve.
Over infinite fields, exact verification requires a matroid/genericity reduction - do not silently
conflate "verified over \(\mathbb F_q\)" with "verified over all \(K\)".

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every basis test is an exact determinant/rank over \(K\); every
   per-configuration solve carries a DRAT/LRAT proof or a replayable exhaustion; no floating point
   enters a certified claim.
2. **Independent verification.** A standalone checker, written separately from the search, re-verifies
   each produced arrangement (exact column determinants) and replays the orbit enumeration; DRAT proofs
   are checked by an independent DRAT checker.
3. **Reproducibility.** Field, order, SAT encoding, solver versions, orbit/canonical-form method, and
   seeds are recorded; a **SHA-256 manifest** covers configurations, proofs, and arrangements.
4. **Preservation.** The encoder, solver drivers, orbit enumerator, and arrangement checker are part of
   the record; anything not preserved is stated explicitly, not obscured (the Hadamard-668 lost-source
   lesson).
5. **Honest reporting.** The report states up front the exact order \(n\), field/matroid class, and
   completeness scope certified, and never presents a random-sample verification, a single configuration,
   or an incomplete search as a resolution of Rota's basis conjecture.
