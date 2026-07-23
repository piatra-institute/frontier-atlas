# PROMPT FOR EXTENDING AND CERTIFYING MARKOV UNIQUENESS

## The Markov (Frobenius) uniqueness conjecture: a Markov number determines its triple

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 42 of 50  
**Area:** number theory & algebra  
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Markov equation \(x^2+y^2+z^2=3xyz\) has its positive-integer solutions organized in a
single tree under Vieta involutions; the largest coordinate of a solution is a **Markov number**.
The Frobenius uniqueness conjecture (open since 1913) states that every Markov number is the
maximum of exactly one Markov triple up to ordering - the max-coordinate map is injective. It is
proved for Markov numbers that are prime powers or twice prime powers (Baragar; Button; Zhang) and
verified computationally to large bounds. This is a `[proof]` problem with a sharp machine-checkable
edge: a counterexample would be two triples verified by exact integer arithmetic, and a positive
result for a new arithmetic class reduces to an exact congruence/Pell analysis formalizable in Lean.
**Honest calibration:** full resolution is hard and is not the expected product; the deliverables are
(i) certified verification of uniqueness to a larger bound with a replayable certificate, and (ii) a
certified proof for a new arithmetic class. Anything less than the section-2 standard is reported as
a partial result and never represented as resolving the conjecture.

## 1. Exact problem statement

A **Markov triple** is a solution \((x,y,z)\in\mathbb Z_{>0}^3\) of
\[
x^2+y^2+z^2=3xyz .
\]
The base solution is \((1,1,1)\); \((1,1,2)\) is the next. Fixing two coordinates, the equation is a
monic quadratic in the third, so from \((x,y,z)\) one obtains a neighbouring solution by the **Vieta
involution**
\[
(x,y,z)\ \longmapsto\ (x,\,y,\,3xy-z),
\]
and cyclically in each coordinate. Starting from \((1,1,1)\) these moves generate **every** Markov
triple exactly once on an (essentially) binary tree (Markov, 1879). Order a triple as \(x\le y\le z\);
the largest entry \(z\) is a **Markov number**. The Markov numbers are
\[
1,\,2,\,5,\,13,\,29,\,34,\,89,\,169,\,194,\,233,\,433,\,610,\,985,\dots
\]
(the OEIS Markov sequence).

**Uniqueness (Frobenius) conjecture.** For each Markov number \(m\), there is exactly one ordered
Markov triple \((x,y,z)\) with \(x\le y\le z=m\); equivalently the map \((x,y,z)\mapsto z\) is
injective on ordered triples. A **counterexample** is two ordered triples \((x_1,y_1,m)\neq(x_2,y_2,m)\)
both satisfying the equation.

**Reduction of a single \(m\).** Fixing \(z=m\), the triples with maximum \(m\) are the solutions
\((x,y)\) with \(0<x\le y<m\) of \(x^2+y^2+m^2=3mxy\). Along the tree, each such \((x,y)\) is tied to a
residue \(u\) with \(y\equiv u\,x\pmod m\) and \(u^2\equiv -1\pmod m\) (up to the standard
normalization - **verify** the exact congruence and modulus \(m\) vs \(3m\)); uniqueness for \(m\)
follows when the number of admissible residue classes is forced to one, which is what the arithmetic
of \(m\) controls.

A **certified verification to bound \(N\)** is a proof that every ordered Markov triple with \(z\le N\)
has a distinct maximum, i.e. the multiset of Markov numbers \(\le N\) has no repeats.

## 2. Resolution standard

A **complete resolution** is **one** of:

- a proof that the max-coordinate map is injective on all Markov triples (uniqueness), formalized to
  the standard below; or
- an explicit **counterexample**: integers \((x_1,y_1,m)\) and \((x_2,y_2,m)\), distinct as ordered
  triples, each **verified by exact big-integer arithmetic** to satisfy \(x^2+y^2+m^2=3mxy\) - a fully
  machine-checkable disproof.

Because a full proof is a windfall, the certified deliverables at workstation scope are:

- a **certified verification to a bound \(N\)**: a replayable certificate that all Markov numbers
  \(\le N\) are distinct - the sorted list of Markov numbers \(\le N\) with an exact deduplication
  proof **and** a completeness argument that the tree BFS reached every triple with \(z\le N\); and/or
- a **certified proof for a new arithmetic class** \(\mathcal A\) of Markov numbers (a factorization or
  congruence family not covered by prime-power / twice-prime-power results), via an exact
  Diophantine/congruence argument, ideally checked in **Lean 4 + mathlib**.

**Certified form.** All triple checks are exact integer arithmetic; the verification-to-\(N\) is an
exhaustive tree enumeration with big-integer arithmetic plus a proof that the pruning (stop when
\(z>N\)) loses no triple with \(z\le N\); a new-class theorem is an **exact Diophantine bound / congruence
count** with a written proof, targeted for Lean formalization.

**Not accepted as resolution.**
- A floating-point or bounded-precision tree search (Markov numbers grow super-exponentially; only
  exact big integers are valid).
- Verification to some bound presented as a proof of the full conjecture.
- A restatement of a known class (prime power, \(2p^k\)) presented as a new class.
- A structural conjecture from data mining presented as a theorem.
- A "no near-collision found" observation presented as uniqueness.
- Any new-class argument whose congruence count is only checked numerically for small \(m\).

## 3. Graded partial-result targets

**P1 - Reproduce the tree, certified.** Generate the Markov tree with exact big integers, list Markov
numbers to a modest bound, and certify uniqueness there with an exact dedup + completeness argument.
*Certificate:* the sorted list, the BFS-completeness proof (every \(z\le N\) reached), independent
replay.

**P2 - Extend the certified verification bound.** Push certified uniqueness to the largest \(N\)
feasible on one workstation, using the tree's structure (each move strictly increases the max, so BFS
by max is complete). *Certificate:* the enumeration driver, the pruning-soundness proof, the sorted
Markov-number list with no repeats, and a **SHA-256 manifest**; an independent enumerator replays it.

**P3 - Certify a known class result.** Give a fully exact (ideally Lean) proof of uniqueness for
Markov numbers that are prime powers, reproducing Baragar/Button. *Certificate:* the written proof and,
where formalized, the compiled Lean development.

**P4 - Prove a new arithmetic class.** Prove uniqueness for a family \(\mathcal A\) not previously
covered (e.g. specified two-prime-factor shapes, or \(m\) with a prescribed residue structure) via the
congruence-count reduction. *Certificate:* the exact Diophantine argument; Lean formalization where
feasible; the class defined precisely and checked disjoint from prior results.

**P5 - Mine the verified data.** Study the distribution, near-collisions (pairs of Markov numbers of
nearly equal size), and the residue statistics, forming a precise conjecture. *Certificate:* the exact
data tables with an honest multiple-testing account; conjectures flagged as conjectures.

**P6 - Formalize the framework.** Lean 4 proofs that the Vieta tree enumerates all triples once, and
that uniqueness of \(m\) is equivalent to the admissible-residue count being one. *Certificate:* the
compiled development, giving P2–P4 a formal backbone.

**P7 - Certified exclusion of special-shape counterexamples.** Prove no counterexample exists among
triples of a special form (bounded ratio \(y/x\), or one coordinate in a fixed congruence class).
*Certificate:* the exact argument, independently checked.

## 4. Known results and prior art

- **Markov (1879, 1880)** - the equation, the tree of solutions, and the connection to minima of
  indefinite binary quadratic forms.
- **Frobenius (1913)** - stated the uniqueness conjecture.
- **Zagier (1982)** - the counting asymptotic: the number of Markov numbers below \(x\) is
  \(\sim C(\log x)^2\); efficient tree generation.
- **Baragar (1996)** - uniqueness when \(m\) is prime, \(2p\), or \(p^2\) (verify exact list).
- **Button (1998, 2001)** - uniqueness via unique factorization in real quadratic orders; classes
  including prime powers and twice prime powers (verify).
- **Schmutz; Lang–Tan** - related uniqueness/structure results (verify).
- **Zhang (2007)** - further arithmetic classes (verify).
- **Aigner (2013)** - *Markov's theorem and 100 years of the uniqueness conjecture*: the standard
  monograph, with the fine sub-conjectures and reductions.
- **Cluster-algebra / snake-graph approaches (2010s–2020s)** - Propp; Rabideau–Schiffler; Lee–Li–…;
  Gyoda and collaborators - new proofs of cases and structural results via continued fractions and
  cluster algebras (verify authorship and which cases).
- **Computational verification** - uniqueness confirmed for all Markov numbers up to a large bound;
  the exact current record must be **verified** (it has been pushed well beyond naive ranges using the
  tree's structure).

**Status as of mid-2026 - re-verify against the current literature before starting any session**
(the proved arithmetic classes, the computational record, and the recent cluster-algebra progress all
drift; several nearby problems fell in 2019–2024).

## 5. Attack plan

**`[proof]` / exact enumeration.** In **Python (gmpy2)** / **Pari-GP** / **SageMath**, generate the
Markov tree by Vieta moves with exact big integers; since each descent strictly increases the maximum,
a BFS pruned at \(z>N\) provably reaches every triple with \(z\le N\) - write and check this
pruning-soundness lemma explicitly. Collect maxima, sort, and prove no duplicates (P1, P2).

**`[proof]` congruence reduction.** For fixed \(m\), enumerate solutions of \(x^2+y^2+m^2=3mxy\) with
\(0<x\le y<m\) via the admissible residues \(u\) with \(u^2\equiv-1\pmod m\) (verify the modulus and
normalization); relate the count to the factorization of \(m\). Use this to reproduce known classes
(P3) and to design a new class \(\mathcal A\) whose residue count is provably one (P4).

**`[sym]` data mining.** With **SageMath**, tabulate near-collisions and residue statistics on the
verified range; any pattern is a conjecture pending proof, reported with its multiple-testing budget
(many candidate patterns → spurious ones expected).

**`[cert]` formalization.** In **Lean 4 + mathlib**, formalize the tree-enumeration completeness and
the uniqueness-⇔-residue-count equivalence (P6), then a new-class proof (P4).

**One-workstation scope and failure modes.** Markov numbers grow super-exponentially, so P2 is bounded
by big-integer memory/time, not by tree depth alone - report the exact \(N\) reached and the
pruning-soundness proof, never a bound "extrapolated". The congruence reduction's exact modulus is a
known pitfall (\(m\) vs \(3m\), sign of \(-1\)); pin it down against Aigner before claiming a class.
Data mining will surface many coincidences; discipline is mandatory.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every triple identity and every Markov number is computed in
   exact big-integer arithmetic; the verification-to-\(N\) carries an explicit pruning-soundness proof.
   No floating point enters any certified claim.
2. **Independent verification.** A second, independently written enumerator replays the tree and the
   dedup; a new-class proof is re-derived by hand and/or checked in Lean; a counterexample (if ever
   found) is re-verified by a standalone exact-arithmetic checker.
3. **Reproducibility.** The enumeration order, bound \(N\), big-integer library and versions, and all
   congruence normalizations are recorded; a **SHA-256 manifest** covers the Markov-number list and
   every proof artifact.
4. **Preservation.** The tree generator, the dedup/completeness checker, and any class-proof scripts
   are part of the record; anything not preserved is stated explicitly, not obscured (the Hadamard-668
   lost-source lesson).
5. **Honest reporting.** The report states up front that the conjecture was **not** resolved (unless it
   truly was), gives the exact certified bound \(N\) and the precise definition of any new class proved,
   and never presents verification-to-\(N\), a known-class restatement, or a data-mined pattern as a
   resolution of the Frobenius conjecture.
