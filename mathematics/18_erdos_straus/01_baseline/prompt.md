# PROMPT FOR ADVANCING THE ERDŐS–STRAUS CONJECTURE ON \(4/n\)

## Three-term unit-fraction representations \(4/n=1/a+1/b+1/c\)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 18 of 50  
**Area:** additive & combinatorial number theory  
**Modes:** `[search]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Erdős–Straus conjecture asserts that for every integer \(n\ge 2\) the equation

\[
\frac4n=\frac1a+\frac1b+\frac1c
\]

has a solution in positive integers. It has been verified computationally to very large bounds - past \(10^{17}\), and by 2025 work to \(10^{18}\) (verify the current record) - and reduces, via multiplicativity and Mordell's identities, to prime \(n\) lying in six specific residue classes modulo \(840\). The problem is matched to certified search (a replayable per-\(n\) witness log extending verification) and to symbolic / covering-system methods (machine discovery and certificate-checking of parametric identities that eliminate residue classes).

**Full resolution is a famous hard problem and is not the expected product.** The expected product is the graded partial results of section 3, each carrying an independent certificate. The resolution standard in section 2 is the target, and anything short of it - a verification bound, an eliminated residue class, a proof for one family - is reported as a partial result and never represented as proving the conjecture.

## 1. Exact problem statement

For an integer \(n\ge 2\), the **Erdős–Straus equation** is

\[
\frac{4}{n}=\frac1a+\frac1b+\frac1c,\qquad a,b,c\in\mathbb{Z}_{>0},
\]

with \(a,b,c\) **not required distinct**. Let \(E\) denote the statement "a solution exists for every \(n\ge 2\)."

**Reduction to primes.** If \(4/n\) is solvable, so is \(4/(mn)\) for every \(m\ge 1\), by multiplying each denominator by \(m\):

\[
\frac{4}{mn}=\frac1{ma}+\frac1{mb}+\frac1{mc}.
\]

Hence \(E\) holds if and only if \(4/p\) is solvable for every prime \(p\). The cases \(p=2,3\) are immediate, so the content is \(p\ge 5\).

**Reduction modulo \(840\).** Writing \(840=2^3\cdot3\cdot5\cdot7\), Mordell's polynomial identities solve \(4/n\) for all \(n\) except those in the residue classes

\[
n\equiv 1,\ 11^2,\ 13^2,\ 17^2,\ 19^2,\ 23^2 \pmod{840},
\]

that is,

\[
n\equiv 1,\ 121,\ 169,\ 289,\ 361,\ 529 \pmod{840},
\]

the squares of the totatives of \(840\). Call this set \(R_{840}\subseteq(\mathbb{Z}/840\mathbb{Z})^\times\). Only primes \(p\) with \(p\bmod 840\in R_{840}\) can be problematic.

**Solution types.** A representation is of **Type I** if exactly one denominator is a multiple of \(n\) after normalization, and **Type II** otherwise. A standard Type I ansatz writes, for a divisor pattern of \(n\),

\[
\frac4n=\frac1{n}\cdot\frac{4d}{d}=\frac1a+\frac1b+\frac1c\quad\text{with } a=\Big\lceil\tfrac n4\Big\rceil\text{-scale, } n\mid b\ \text{or}\ n\mid c,
\]

so that solvability reduces to finding a divisor of a linear form in \(n\) in a prescribed residue class. The hard residues \(R_{840}\) are precisely those where every such Type I pattern can fail and a genuine Type II solution (two denominators sharing factors with \(n\)) is required.

**Adopted formulation and admissible advances.** The determination is a proof of \(E\). Admissible partial advances are:
- (a) a certified extension of computational verification to a new bound \(N\) with a replayable witness certificate;
- (b) a covering-system elimination of one or more residue classes modulo \(840\), or a refinement modulus \(840m\), by parametric identities;
- (c) a proof of \(E\) for a new infinite family of \(n\).

No informal target is accepted.

## 2. Resolution standard

A complete resolution is a proof of \(E\) for **all** \(n\ge 2\), in one of these certified forms.

- A **covering-identity certificate**: a finite family of parametric identities

\[
\frac4n=\frac1{f_i(n)}+\frac1{g_i(n)}+\frac1{h_i(n)},\qquad i=1,\dots,r,
\]

with \(f_i,g_i,h_i\) piecewise-polynomial (or divisor-conditioned) integer-valued maps, each valid and positive on an explicit residue class \(C_i\pmod{M}\), such that \(\bigcup_i C_i\) covers all residues coprime to the modulus (verified by exhaustive residue check / CRT).

- A **Lean 4 + mathlib** formal proof of \(E\).

**Named certified form for the search side.** A **replayable verification certificate** to bound \(N\): a deterministic solver that, for each \(n\le N\) (equivalently each prime \(p\le N\) in \(R_{840}\)), emits a witness \((a,b,c)\); a compact, hash-manifested log; and a standalone checker that re-derives \(4/n=1/a+1/b+1/c\) in exact arithmetic for a stated coverage of \(n\).

**Not accepted as resolution.**
- Verification to any finite bound \(N\), however large, presented as a proof of \(E\).
- A density / analytic estimate (e.g. a Vaughan-type bound on the exceptional set, or "almost all \(n\)") presented as full resolution.
- A covering that leaves any residue class or any infinite family unresolved, presented as complete.
- A "solution" using negative, zero, rational, or non-integer denominators, or fewer / more than three unit fractions.

## 3. Graded partial-result targets

- **\(P_1\) - reproduce the reduction and a modest verification.** Independently re-derive Mordell's six-class reduction with a verified identity table, and verify \(E\) to \(n\le 10^{9}\) with a replayable witness log.
  - *Certificate:* identity table checked symbolically + per-\(n\) witness checker. Validates the pipeline.

- **\(P_2\) - extend certified verification.** Push verification past the current published record (targeting a new bound beyond \(10^{18}\)) with a fast sieve over the hard residues and a replayable, hash-manifested certificate.
  - *Certificate:* solver source + witness log + independent recheck of a sampled dense subset and of all near-failures.

- **\(P_3\) - eliminate a residue class by covering.** Machine-discover parametric identities eliminating at least one class of \(R_{840}\), or a subclass modulo \(840m\) - a Mordell-style partial result.
  - *Certificate:* identity + validity / positivity proof on the class + CRT coverage check.

- **\(P_4\) - prove \(E\) for a new infinite family.** A closed-form identity certificate resolving all \(n\) in a specified residue class or factorization type (e.g. \(n\) with a prime factor in a good class).
  - *Certificate:* parametric identity + range of validity + formal or symbolic proof.

- **\(P_5\) - minimize the hard classes.** A certified covering leaving the fewest residue classes unresolved, quantifying the reduction versus the six-class baseline.
  - *Certificate:* the covering system + a proof of exactly which residues remain.

- **\(P_6\) - strongest short of resolution.** A Lean-formalized proof of the best partial theorem (e.g. the reduction plus \(P_4\)), or a certified "all \(n\) outside an explicit density-zero set" statement with the exceptional set named. The full proof of \(E\) is a windfall.

## 4. Known results and prior art

- Erdős and Straus posed the conjecture (~1948).
- Mordell (*Diophantine Equations*, 1969) gave the identities reducing to the six residue classes \(R_{840}\); Rosati (1954) and Yamamoto (1965) gave further identities and computations.
- Vaughan (1970) bounded the exceptional set: the number of \(n\le N\) for which \(4/n\) is not (Type I) representable is \(\ll N\exp(-c(\log N)^{2/3})\).
- Elsholtz (2001) and **Elsholtz–Tao (2013)**, *Counting the number of solutions to the Erdős–Straus equation on unit fractions*, gave average and pointwise results on the solution-count and connections to primes in arithmetic progressions (Bombieri–Vinogradov).
- Computational verification: **Salez (2014)**, *New modular equations and checking up to \(N=10^{17}\)* - a seven-equation modular sieve in C++; extended by 2025 work to \(10^{18}\) with empirical study of the solution-count \(f(p)\); a 2024 "complete congruence system" preprint (verify).
- OEIS **A073101** records the number of solutions to \(4/n\); related sequences track the exceptional residues.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the exact current verification record and whether any new residue class or infinite family has been resolved; several nearby number-theory records moved in 2024–2025.

## 5. Attack plan

`[search]` and `[proof]` on a single workstation.

**Verification sieve `[search]`.** Restrict to primes \(p\le N\) with \(p\bmod 840\in R_{840}\) - the only hard cases. For each, search Type I solutions: with \(4/p=1/a+1/b+1/c\), \(a\le b\le c\), the smallest denominator satisfies

\[
\Big\lceil \tfrac p4\Big\rceil+1\ \le\ a\ \le\ \Big\lfloor \tfrac{3p}4\Big\rfloor,
\]

after which \(1/b+1/c=4/p-1/a\) is solved by divisor enumeration of the resulting fraction. Use exact integer arithmetic via **Pari/GP** or **FLINT/GMP**, with a tight C++ inner loop mirroring Salez's approach. Emit a witness per \(n\) and a hash-manifested log.

**Covering-system search `[sym]`.** Encode candidate identities as parametric denominator maps conditioned on \(n\bmod M\) and on divisibility of small linear forms in \(n\). Search over moduli \(M\mid 840m\) and residue classes, verifying:
- validity - \(1/f+1/g+1/h=4/n\) as a polynomial identity on the class;
- positivity - each denominator is a positive integer on the class.

Frame "does a finite covering by identities of bounded degree cover class \(C\)?" as a constraint / SAT problem over residues, and confirm any covering by exhaustive CRT.

**Formalization `[proof]`.** Lean 4 + mathlib for the multiplicative reduction, the Mordell identities, and any new family identity (\(P_4\)); these are finite algebraic verifications well suited to a proof assistant.

**Scope and failure modes.** Verification to \(\sim10^{18}\)–\(10^{19}\) is feasible on one workstation with a good sieve; the hard residues are sparse, so most work touches only \(\sim 6N/(\phi(840)\log N)\) primes. Covering-system searches for moderate moduli are feasible. **Honest barrier:** it is expected - and partly understood - that *no* finite covering by polynomial identities of the simplest shape resolves every prime; the residue \(n\equiv1\) family resists uniform Type I identities, so \(P_3\)/\(P_5\) reduce but very likely cannot eliminate all classes. State this rather than promising a covering proof of \(E\). Type II solutions for the hardest residues require large \(a,b,c\), inflating search cost; document any \(n\) needing atypically large denominators.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every witness \((a,b,c)\) is rechecked by exact rational arithmetic; every identity is a verified polynomial / CRT identity, not a numerical coincidence. Floating point is never used for certification.
2. **Independent verification.** A standalone checker, written separately from the sieve, re-validates witnesses and covering identities; for a formal target, the Lean kernel is the independent checker. Recheck all near-failures and a dense random sample of the verified range with a second implementation.
3. **Reproducibility.** Sieve parameters, residue enumeration order, solver versions, and the exact range covered are recorded; a SHA-256 manifest spans the witness logs, identity tables, and code.
4. **Preservation.** The verification and covering-search source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front that the conjecture was not proved (unless it genuinely was), and reports a verification bound, an eliminated residue class, or a family proof as exactly that - never as a proof of \(E\).
