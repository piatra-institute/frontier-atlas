# PROMPT FOR CERTIFYING A MAHLER-MEASURE GAP BELOW LEHMER'S NUMBER

## Lehmer's problem: is the Mahler measure of a non-cyclotomic integer polynomial bounded away from 1?

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 40 of 50  
**Area:** number theory & algebra  
**Modes:** `[opt]` `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Lehmer's problem asks whether there is a constant \(c>1\) such that every non-cyclotomic
polynomial \(P\in\mathbb Z[x]\) has Mahler measure \(M(P)\ge c\). The smallest known value
exceeding \(1\) is **Lehmer's number** \(\lambda\approx 1.17628081\ldots\), the Mahler measure
of Lehmer's degree-10 polynomial, and Lehmer's conjecture asserts \(\lambda\) (or some fixed
\(c>1\)) is a universal lower bound. The problem is matched to current AI methods on two
fronts: an **exact, interval-certified exhaustive search** that no integer polynomial of
bounded degree realizes a measure in the open gap \((1,\lambda)\); and **bound optimization**
producing certified lower bounds for structured subclasses via auxiliary-function / integer
transfinite-diameter certificates that reduce to exact rational linear algebra. The resolution
standard in section 2 is the target - a proof of the gap, a genuine counterexample, or a
certified degree-bounded exhaustion; anything less (a numerical minimum, a single class, a
heuristic frontier) is reported as a partial result and never represented as solving Lehmer's
problem.

## 1. Exact problem statement

For a polynomial \(P(x)=a_d\prod_{i=1}^{d}(x-\alpha_i)\in\mathbb Z[x]\) with \(a_d\ne 0\), the
**Mahler measure** is
\[
M(P)=|a_d|\prod_{i=1}^{d}\max(1,|\alpha_i|)
     =\exp\!\left(\int_0^1\log\bigl|P(e^{2\pi i t})\bigr|\,dt\right),
\]
the second equality being Jensen's formula. Write \(m(P)=\log M(P)\) for the logarithmic
measure. The measure is multiplicative: \(M(PQ)=M(P)M(Q)\), and \(M(P)\ge 1\) for every nonzero
\(P\in\mathbb Z[x]\).

**Kronecker's theorem.** For monic \(P\in\mathbb Z[x]\), \(M(P)=1\) if and only if every root is
either \(0\) or a root of unity; equivalently \(P(x)=x^{k}\prod_j\Phi_{n_j}(x)\) up to sign,
a product of a monomial and cyclotomic polynomials \(\Phi_n\). Call such \(P\) **cyclotomic**.
All measure lives on the non-cyclotomic polynomials.

**Lehmer's polynomial** is
\[
L(x)=x^{10}+x^{9}-x^{7}-x^{6}-x^{5}-x^{4}-x^{3}+x+1,
\]
whose largest real root is a Salem number \(\lambda\approx 1.17628081825991\), with
\(M(L)=\lambda\).

**Lehmer's problem (the open question).** Does
\[
\mu_\ast:=\inf\{\,M(P):P\in\mathbb Z[x],\ M(P)>1\,\}
\]
satisfy \(\mu_\ast>1\)? Lehmer's conjecture is the sharper assertion \(\mu_\ast=\lambda\), i.e.
no non-cyclotomic integer polynomial has \(1<M(P)<\lambda\). Because \(M\) is multiplicative and
invariant under \(x\mapsto\pm x\), \(x\mapsto x^{-1}\cdot x^{\deg}\) (reciprocal) and removal of
cyclotomic factors, the infimum is attained (if at all) on irreducible non-cyclotomic minimal
polynomials of algebraic integers, and - by Smyth's theorem below - the search reduces to
**reciprocal** polynomials \(x^dP(1/x)=P(x)\). We adopt this reduced formulation: normalize to
\(P\) monic, irreducible, reciprocal, non-cyclotomic, with \(\deg P=d\).

An **exhaustive gap-exclusion for degree \(D\)** is the statement: no \(P\in\mathbb Z[x]\) with
\(\deg P\le D\) satisfies \(1<M(P)<\lambda\). A **structured lower bound** for a class
\(\mathcal K\subseteq\mathbb Z[x]\) is a constant \(c_{\mathcal K}>1\) with \(M(P)\ge c_{\mathcal K}\)
for all non-cyclotomic \(P\in\mathcal K\).

## 2. Resolution standard

A complete resolution of Lehmer's problem is **one** of:

- a proof that \(\mu_\ast>1\) (Lehmer's problem), or the sharp \(\mu_\ast=\lambda\) (Lehmer's
  conjecture), formalized to the standard below; or
- an explicit \(P\in\mathbb Z[x]\) with a **certified** value \(1<M(P)<\lambda\) - a genuine
  counterexample to Lehmer's conjecture - the certificate being an interval enclosure of
  \(M(P)\) with directed rounding that lies strictly inside \((1,\lambda)\), together with an
  exact proof that \(P\) is non-cyclotomic.

Because a full proof is a windfall, the certified deliverable at the scope of one workstation is
a **certified exhaustive gap-exclusion** for the largest attainable degree \(D\): a machine-checkable
proof that every reciprocal non-cyclotomic \(P\) with \(\deg P\le D\) has \(M(P)\ge\lambda\), or a
**certified structured lower bound** \(c_{\mathcal K}>1\) for a named class.

**Certified form.** (i) Every Mahler-measure comparison is an **interval-arithmetic** enclosure
(Arb/FLINT, directed rounding) proving \(M(P)>\lambda\) or locating \(M(P)\) inside \((1,\lambda)\);
root counts inside/on/outside the unit circle are settled by exact **resultant/Sturm**
computations, never by floating point. (ii) A finite **coefficient search** is reduced by exact
inequalities (bounds on coefficients from \(M(P)<\lambda\), e.g. via Newton's inequalities and the
house-of-\(\alpha\) bound) to a certified finite box, then exhausted with an isomorph/symmetry
rejection argument that is itself replayable. (iii) A structured lower bound is delivered as an
**auxiliary-function / integer-transfinite-diameter certificate**: an exact rational (or algebraic)
linear combination \(\sum_j c_j\log|Q_j|\) dominating \(\log|x|\) on the unit circle, whose validity
is a finite set of exact polynomial-nonnegativity checks (a Positivstellensatz/SOS certificate over
\(\mathbb Q\)). (iv) Reduction lemmas (Kronecker, Smyth's reciprocal reduction, multiplicativity)
are candidates for a **Lean 4 + mathlib** formalization.

**Not accepted as resolution.**
- A floating-point table of smallest measures with no interval certificate.
- A single new small Salem number, however small, that is not \(<\lambda\) (it does not touch the gap).
- A lower bound of the Dobrowolski form \(1+c(\log\log d/\log d)^3\) presented as "settling" the
  problem - it tends to \(1\) and is not a fixed \(c>1\).
- Gap-exclusion for one degree presented as gap-exclusion for all degrees.
- An auxiliary-function bound whose nonnegativity is only checked numerically.
- Any claim \(\mu_\ast=\lambda\) inferred from finite search alone.

## 3. Graded partial-result targets

**P1 - Reproduce the numerical frontier, certified.** Recompute the smallest Mahler measures for
reciprocal non-cyclotomic \(P\) of degree \(\le 20\) with **interval-certified** measures, and
certify that \(\lambda\) is the unique minimum in \((1,\lambda]\) over that range. *Certificate:* Arb
enclosures for each candidate + an exact finite-box exhaustion log; independent replay recomputes
every enclosure.

**P2 - Extend certified gap-exclusion by degree.** Push the certified statement "no reciprocal
non-cyclotomic \(P\) of degree \(\le D\) has \(M(P)\in(1,\lambda)\)" to the largest \(D\) reachable on
one workstation (target the mid-40s if the pruned box permits). *Certificate:* the exact
coefficient-bound derivation defining the finite box, plus a replayable exhaustion trace with
per-branch interval certificates.

**P3 - Certify Smyth's non-reciprocal bound.** Produce an exact auxiliary-function certificate that
every **non-reciprocal** \(P\in\mathbb Z[x]\) has \(M(P)\ge\theta_0=1.324717\ldots\) (the smallest Pisot
number, root of \(x^3-x-1\)). *Certificate:* rational coefficients \(c_j\) and the finite exact
nonnegativity checks; independent CAS re-derivation.

**P4 - Certified structured lower bound.** For a named class (all-odd-coefficient polynomials;
polynomials with \(\le t\) nonzero terms; prescribed trace/height), prove \(M(P)\ge c_{\mathcal K}>1\)
with an exact certificate. *Certificate:* SOS/transfinite-diameter LP solved in exact rational
arithmetic with a verified feasibility witness.

**P5 - Certified Salem enumeration.** Enumerate, with certified minimal polynomials, all Salem
numbers below a fixed bound of degree \(\le D\), matching or extending the standard tables.
*Certificate:* exact minimal polynomial for each (reconstructed via LLL, **verified** by exact
resultant/factorization), plus interval enclosure of the Salem root.

**P6 - Improve a class constant.** Strictly improve a published lower bound for a structured class,
with a fully exact certificate. *Certificate:* the new auxiliary function + exact checks; comparison
to the prior constant.

**P7 - Formalize the reductions.** Lean 4 proofs of Kronecker's theorem and Smyth's reciprocal
reduction, so that any later search inherits a formal foundation. *Certificate:* the compiled Lean
development.

## 4. Known results and prior art

- **Lehmer (1933)** posed the problem and exhibited \(L(x)\) with \(M(L)=\lambda\); still the record.
- **Kronecker (1857)** - measure-one classification.
- **Smyth (1971)** - every non-reciprocal \(P\in\mathbb Z[x]\) has \(M(P)\ge\theta_0\approx1.3247\),
  the smallest Pisot number; this reduces Lehmer's problem to reciprocal polynomials.
- **Dobrowolski (1979)** - for non-cyclotomic \(P\) of degree \(d\),
  \(M(P)\ge 1+c\!\left(\tfrac{\log\log d}{\log d}\right)^{3}\); **Voutier (1996)** made the constant
  explicit (\(c=\tfrac14\) for \(d\ge2\)) (verify). Best general unconditional bound; it tends to \(1\).
- **Amoroso–Dvornicich (2000)** - \(M(P)\ge 5^{1/12}\) when the splitting field is abelian (verify).
- **Borwein–Dobrowolski–Mossinghoff (2007)** - non-cyclotomic all-odd-coefficient \(P\) satisfy
  \(M(P)\ge 5^{1/4}\) (verify).
- **Breusch (1951)** - an early bound predating Smyth for a related class (verify).
- **Mossinghoff (1998); Mossinghoff–Rhin–Wu (2008)** - exhaustive searches computing the smallest
  Mahler measures; the search reached degree in the low-to-mid 40s (the exact bound and whether it is
  \(40\), \(44\), or higher must be **verified**), confirming \(\lambda\) is the smallest known and no
  smaller value appears up to that degree.
- **Rhin–Wu; Wu** - integer transfinite diameter / auxiliary-function LP methods giving certified
  lower bounds for restricted classes and small Salem/Pisot enumerations (verify specific constants).
- **Boyd (1977–1989)** - conjectures on small Salem numbers; the "Salem–Lehmer" heuristics and the
  list of small Salem numbers (Mossinghoff's tables) with \(\lambda\) the smallest known.
- **Smyth (2008 survey)** - "The Mahler measure of algebraic numbers: a survey"; the standard entry
  point (verify edition/venue).

**Status as of mid-2026 - re-verify against the current literature before starting any session**
(the record \(\lambda\), the exhaustive degree bound, and the best class constants all drift; several
nearby problems fell in 2019–2024).

## 5. Attack plan

**`[sym]` exact polynomial infrastructure.** In **SageMath** / **Pari-GP**, generate reciprocal
non-cyclotomic candidates degree-by-degree; strip cyclotomic factors by exact GCD with
\(\prod\Phi_n\); count roots off the unit circle by **Sturm sequences / resultants** (never
floating point). Reconstruct minimal polynomials of Salem candidates with **LLL/PSLQ**, then
**verify exactly** by resultant and irreducibility test - treat every integer relation as a
hypothesis to be confirmed, and record the multiple-testing budget (many candidates → spurious
"relations" are expected; only exact confirmation counts).

**`[opt]` certified measures.** Use **Arb/FLINT** for ball-arithmetic enclosures of all roots and of
\(M(P)=|a_d|\prod\max(1,|\alpha_i|)\) with directed rounding; a candidate enters the gap only if its
enclosure lies strictly inside \((1,\lambda)\), and is excluded when the enclosure proves
\(M(P)>\lambda\). The finite search box per degree comes from exact coefficient bounds implied by
\(M(P)<\lambda\) (house-of-\(\alpha\), Newton/Gauss inequalities); derive and record these bounds
symbolically so the box is provably complete.

**`[opt]` structured lower bounds.** Formulate the auxiliary-function / integer transfinite-diameter
problem as a **linear program** over rational coefficients of \(\sum_j c_j\log|Q_j|\); solve in exact
rational arithmetic and export an SOS/Positivstellensatz **feasibility witness** whose validity is a
finite set of exact polynomial-nonnegativity checks. This is the route to P3, P4, P6.

**`[cert]` formalization.** Target **Lean 4 + mathlib** for Kronecker and Smyth's reduction (P7),
giving later searches a formal base.

**One-workstation scope and failure modes.** The coefficient box grows fast with degree - P2 is
gated by pruning quality, and the honest outcome may be "gap-exclusion certified to degree \(D\), box
provably complete, larger \(D\) infeasible here." LLL can return **false relations**; only exact
resultant confirmation is accepted. Exact LP/SOS solving can blow up in bit-size; cap the number of
auxiliary factors and report infeasibility honestly. Interval widths near \(M(P)\approx\lambda\)
require high precision - increase Arb precision adaptively and log the working precision per branch.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every measure comparison is an Arb interval enclosure with
   directed rounding; every "off the unit circle" root count is an exact resultant/Sturm result;
   every finite box is provably complete from symbolically derived coefficient bounds. Floating point
   is exploration only.
2. **Independent verification.** A standalone re-checker, written separately from the search, replays
   each interval enclosure and each exhaustion branch; minimal polynomials from LLL are re-verified
   by an independent exact factorization; auxiliary-function certificates are re-checked by a second
   CAS evaluating the finite nonnegativity conditions.
3. **Reproducibility.** All coefficient-box derivations, seeds, Arb precisions, LP inputs and exact
   solutions, and tool versions are recorded; a **SHA-256 manifest** covers every artifact.
4. **Preservation.** The full search and certificate-generation source is part of the record; if any
   component (e.g. an ad hoc pruning script) is not preserved, that is stated explicitly, not obscured
   (the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front whether the resolution standard was met, gives the
   exact degree \(D\) of any certified gap-exclusion and the exact constant of any structured bound,
   and never presents a finite-degree exhaustion or a single-class bound as a resolution of Lehmer's
   problem.
