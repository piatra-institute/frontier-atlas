# PROMPT FOR EXTENDING AND CERTIFYING THE ERDŐS–MOSER EXCLUSION BOUND

## The Erdős–Moser equation: is 1 + 2 = 3 the only power-sum solution?

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 45 of 50  
**Area:** number theory & algebra  
**Modes:** `[search]` `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Erdős–Moser equation is \(1^k+2^k+\dots+(m-1)^k=m^k\); the only known solution is
\(1+2=3\) (\(k=1,\ m=3\)), and the conjecture is that there are no others. Moser (1953) proved no
further solution has \(m\) below an enormous bound, derived from congruences and the continued
fraction of \(\log 2\); the bound has since been pushed astronomically (Gallot–Moree–Zudilin and
others). This is a crisp Diophantine target with **machine-checkable arithmetic**: a putative
solution is pinned by exact congruences (`[sym]`, via Bernoulli numbers / von Staudt–Clausen) and
excluded up to a huge bound by a **certified** computation of the convergents of \(\log 2\) with
interval arithmetic (`[search]`). The certified deliverables are (i) an extension of the exclusion
bound with a replayable certificate, and (ii) new certified congruence obstructions. The resolution
standard in section 2 is the target; a heuristic bound, an uncertified continued-fraction computation,
or a numerical near-miss is reported as a partial result and never as resolving the conjecture.

## 1. Exact problem statement

For integers \(m\ge2\) and \(k\ge1\), consider
\[
S_k(m-1):=\sum_{j=1}^{m-1} j^{k}\;=\;m^{k}. \tag{EM}
\]
The pair \((m,k)=(3,1)\) solves (EM): \(1+2=3\). The **Erdős–Moser conjecture** is that (EM) has no
other solution in positive integers. A **nontrivial solution** is any \((m,k)\neq(3,1)\).

By von Staudt–Clausen and the Bernoulli expansion of power sums,
\(S_k(m-1)=\frac{1}{k+1}\sum_{j=0}^{k}\binom{k+1}{j}B_j\,m^{k+1-j}\), so (EM) imposes exact
congruences on \(m\) and \(k\) modulo primes \(p\) via the appearance of \(B_j\) and the primes \(p\)
with \((p-1)\mid k\). Established necessary conditions on any nontrivial solution include: \(k\) is
even; strong \(2\)-adic and modular congruences on \(m\) (e.g. \(m\equiv3\pmod 8\) - **verify** the
exact modulus and depth); constraints on the prime factors of \(m\), \(2m\pm1\), \(3m\pm1\); and the
near-integrality of \(\sum_{(p-1)\mid k}\tfrac1p\), which ties \(k\) to \(\log 2\). The last yields the
central mechanism: a nontrivial solution forces the continued fraction of \(\log 2\) to have a very
large partial quotient before a certain index, so that \(m\) exceeds a bound governed by the
**convergent denominators of \(\log 2\)**.

An **exclusion bound \(B\)** is a proof that (EM) has no nontrivial solution with \(m\le B\). The
conjecture is the statement that the exclusion holds for all \(B\).

## 2. Resolution standard

A **complete resolution** is **one** of:

- a proof that (EM) has no nontrivial solution (the conjecture), formalized to the standard below; or
- an explicit nontrivial solution \((m,k)\), certified - necessarily by a **structural** exact
  certificate (the numbers are astronomically large, so direct summation is impossible; the
  certificate must be the exact congruence/valuation data that pins \((m,k)\) and an exact check of
  (EM) via the Bernoulli identity in the relevant residue rings).

Because a full proof is a windfall, the certified deliverables at workstation scope are:

- a **certified extension of the exclusion bound** beyond the current record: a replayable proof that no
  nontrivial solution has \(m\le B\) for a new record \(B\); and/or
- **new certified congruence obstructions** on any nontrivial solution.

**Certified form.** (i) The exclusion bound rests on a **certified continued-fraction computation of
\(\log 2\)** - convergents \(p_i/q_i\) with **interval-arithmetic** enclosures (Arb/FLINT, directed
rounding) proving the required approximation inequality, which is the "exact Diophantine bound" tool
here. (ii) The congruence obstructions are **exact modular / Bernoulli** computations (von
Staudt–Clausen, Kummer congruences) over \(\mathbb Z/N\). (iii) The reduction "solution \(\Rightarrow\)
continued-fraction inequality \(+\) congruences" is a candidate for **Lean 4 + mathlib** formalization,
turning a certified convergent computation into a formal exclusion theorem.

**Not accepted as resolution.**
- A floating-point continued fraction of \(\log 2\) with no interval enclosure of the convergents.
- An exclusion bound quoted without the exact inequality and congruence certificate behind it.
- A single congruence re-derivation presented as new obstruction when it is Moser's.
- A "no solution found" from a bounded numerical scan presented as a proof (the real bound is
  astronomically beyond any scan).
- The bound for one structured sub-case presented as the general exclusion bound.
- Any convergent inequality checked only numerically at working precision without directed rounding.

## 3. Graded partial-result targets

**P1 - Reproduce the congruence skeleton.** Symbolically re-derive the necessary conditions on a
nontrivial solution (\(k\) even; the \(2\)-adic and modular congruences on \(m\); the prime-factor
constraints; the \(\sum1/p\) near-integrality) from the Bernoulli/von Staudt–Clausen identity, exactly.
*Certificate:* the exact derivations, checked by a second CAS; small-modulus verifications.

**P2 - Reproduce the known exclusion bound, certified.** Recompute the continued fraction of \(\log 2\)
with **certified** convergent enclosures and the exact congruence sieve, reproducing Moser's and then
Gallot–Moree–Zudilin's bounds (\(\sim10^{10^{6}}\), then \(\sim10^{10^{9}}\) - verify). *Certificate:*
Arb enclosures for the convergents, the exact inequality verification, and a replay.

**P3 - Extend the certified exclusion bound.** Push the record \(B\) further by computing more certified
convergents of \(\log 2\) and/or tightening the congruence obstruction. *Certificate:* the additional
certified convergents, the exact inequality at the new bound, a replayable log, and a **SHA-256
manifest**.

**P4 - New certified congruence obstructions.** Prove additional necessary conditions on any nontrivial
solution (new prime moduli, deeper \(2\)-adic conditions, factor constraints on \(2m\pm1\)). *Certificate:*
exact modular proofs, independently rechecked.

**P5 - Structural mining.** Study the arithmetic of \(m\pm1,\,2m\pm1\), links to irregular/Bernoulli
primes, and the distribution of admissible \(k\); form precise conjectures. *Certificate:* exact data
with an honest multiple-testing account; conjectures flagged as such.

**P6 - Formalize the reduction.** Lean 4 proof that a nontrivial solution implies the continued-fraction
inequality and the congruences, so a certified convergent computation yields a formal exclusion up to
\(B\). *Certificate:* the compiled development.

**P7 - Further exclusion for structured sub-cases.** Reach a larger bound under a restriction (\(m\)
prime; \(k\) in a fixed residue class) via a sharper certified argument. *Certificate:* the exact
sub-case argument and its bound.

## 4. Known results and prior art

- **Erdős** - posed the equation; **Moser (1953)** - "On the Diophantine equation
  \(1^n+2^n+\dots+(m-1)^n=m^n\)": no nontrivial solution with \(m<10^{10^{6}}\); \(k\) even and the core
  congruence conditions.
- **Krzysztofek (1966); Best, te Riele (1976)** - computational refinements (verify).
- **Moree, te Riele, Urbanowicz (1994)** - divisibility/congruence results on power sums and (EM)
  (verify).
- **Butske, Jaje, Mayernik (2000)** - Giuga/\(\sum1/p\)-type computations relevant to the near-integrality
  condition (verify).
- **Moree (survey, c. 2013)** - "A top hat for Moser's four mathemagical rabbits" (Amer. Math. Monthly):
  the standard readable account of the mechanism (verify venue/year).
- **Gallot, Moree, Zudilin (2011)** - "The Erdős–Moser equation … revisited using continued fractions":
  pushed the exclusion bound to roughly \(m>10^{10^{9}}\) and sharpened the structural conditions, via
  the continued fraction of \(\log 2\) (verify the exact record).
- **Kellner** - Bernoulli-number and power-sum identities relevant to the exact congruences (verify).

**Status as of mid-2026 - re-verify against the current literature before starting any session**
(the exclusion-bound record and the exact congruence conditions drift; check whether the bound has been
pushed since Gallot–Moree–Zudilin; several nearby problems fell in 2019–2024).

## 5. Attack plan

**`[sym]` exact congruences.** In **SageMath** / **Pari-GP**, compute Bernoulli numbers and the power-sum
expansion exactly; re-derive and verify the necessary conditions on \((m,k)\) via von Staudt–Clausen and
Kummer congruences (P1, P4). Work in \(\mathbb Z/N\) with exact arithmetic; validate each congruence
against small explicit \(k\).

**`[search]` certified continued fraction of \(\log 2\).** With **Arb/FLINT**, compute \(\log 2\) to very
high precision with a rigorous enclosure and extract convergents \(p_i/q_i\) with **certified** error
bounds (directed rounding), so each partial quotient and each convergent denominator is proved correct.
The exclusion bound is the largest \(B\) for which the Moser/GMZ inequality is certified to fail for all
\(m\le B\); more certified convergents push \(B\) (P2, P3).

**`[sym]` obstruction sieve.** Combine the congruences into a sieve that, together with the
continued-fraction inequality, excludes \(m\le B\); keep every step exact so the exclusion is a proof,
not a scan.

**`[cert]` formalization.** In **Lean 4 + mathlib**, formalize the reduction and the inequality (P6).

**One-workstation scope and failure modes.** The bound \(B\) is astronomically large and is *not*
reached by iterating over \(m\); it comes from the certified approximation quality of \(\log 2\), so the
work is high-precision certified real computation plus exact number theory, both workstation-feasible.
Failure modes: **uncertified** convergents (floating-point CF is worthless here - every convergent needs
a directed-rounding enclosure); a mis-stated congruence modulus (guard against it by small-\(k\)
validation and cross-checking Moree/GMZ); and over-claiming - an extended bound must state exactly which
inequality and which certified convergents deliver it.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every convergent of \(\log 2\) carries an Arb interval enclosure
   with directed rounding; every congruence is exact modular arithmetic; the exclusion inequality is
   verified rigorously, not at plain floating precision. Floating point is exploration only.
2. **Independent verification.** A standalone re-checker, written separately from the search, replays the
   certified continued fraction (independent high-precision \(\log 2\) enclosure) and re-verifies the
   inequality and every congruence in a second CAS; the reduction is checked in Lean where formalized.
3. **Reproducibility.** Working precisions, the number of certified convergents, congruence moduli, and
   tool versions are recorded; a **SHA-256 manifest** covers the convergent table and every certificate.
4. **Preservation.** The CF/interval driver, the congruence-sieve code, and the exact derivations are
   part of the record; anything not preserved is stated explicitly, not obscured (the Hadamard-668
   lost-source lesson).
5. **Honest reporting.** The report states up front the exact exclusion bound \(B\) certified and the
   precise congruence obstructions proved, and never presents an uncertified bound, a numerical scan, or
   a re-derivation of known conditions as a resolution of the Erdős–Moser conjecture.
