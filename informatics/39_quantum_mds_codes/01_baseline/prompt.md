# PROMPT FOR CERTIFIED QUANTUM MDS CODES AT SPECIFIC PARAMETERS

## Existence, construction, or nonexistence of a \(q\)-ary quantum MDS code meeting the quantum Singleton bound

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 39 of 50
**Area:** quantum computation & codes
**Modes:** `[search]` `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A quantum code is **MDS** when it meets the quantum Singleton bound with equality - the optimal trade-off between length, dimension, and distance, the quantum analog of Reed–Solomon optimality. Beyond the trade-off itself sits a sharp length question: for a fixed alphabet \(q\) and dimension, how long can a quantum MDS code be? The quantum MDS conjecture predicts a ceiling near \(q^2 + 1\) (with a known family of exceptions), tied to the classical MDS conjecture, and many specific parameter cases - a given \((q, k, d)\) or a given length - remain open, awaiting either a construction or a nonexistence proof. Both directions are certifiable on the machine and lean on algebra: MDS codes come from constacyclic, generalized Reed–Solomon, and monomial-Cartesian families whose defining conditions are combinatorial and checkable exactly, while nonexistence for small parameters follows from the quantum LP / weight-enumerator method or from finite exhaustion of Hermitian/Euclidean self-orthogonal generators. The verifier is exact: a construction is confirmed by verifying self-orthogonality and the exact distance (the code is MDS iff \(k = n - 2d + 2\) at equality); a nonexistence is a checked LP infeasibility with an exact dual, or an exhaustive symbolic search with a completeness argument. Anything short of the section-2 standard - a numeric distance, an incomplete family search, an asymptotic claim - is a partial result, never a solution.

## 1. Exact problem statement

Fix a prime power \(q\). A quantum code \([[n,k,d]]_q\) on \(n\) qudits of dimension \(q\) satisfies the **quantum Singleton bound**

\[
k \;\le\; n - 2d + 2
\]

(Knill–Laflamme; Rains). It is **quantum MDS (QMDS)** when equality holds:

\[
k \;=\; n - 2d + 2,
\qquad\text{equivalently}\qquad
d \;=\; \frac{n - k}{2} + 1 .
\]

Thus a QMDS code extracts the maximum possible distance from its length-and-dimension budget, exactly as a classical Reed–Solomon code does.

Stabilizer QMDS codes are constructed most often from classical MDS codes via the Hermitian or Euclidean self-orthogonality route.

- **Hermitian construction.** A classical \([n,k',d']_{q^2}\) code \(C\) that is Hermitian dual-containing, \(C^{\perp_H} \subseteq C\), yields a stabilizer code

  \[
  [[\,n,\ 2k' - n,\ \ge d'\,]]_q ;
  \]

  if \(C\) is MDS the quantum code is QMDS.

- **Euclidean / CSS construction.** A nested pair \(C_2 \subseteq C_1\) of classical codes over \(\mathbb{F}_q\) with \(C_1, C_2\) MDS gives a QMDS code with parameters read off from \((n, \dim C_1, \dim C_2)\); explicitly, for \(C_2 \subseteq C_1\) with \(C_1 = [n,k_1,d_1]\), \(C_2 = [n,k_2,d_2]\),

  \[
  [[\,n,\ k_1 - k_2,\ \min(d_1, d_2^{\perp})\,]]_q ,
  \]

  which is QMDS when both classical codes are MDS. The workhorse family is the **generalized Reed–Solomon** code: for distinct evaluation points \(a_1,\dots,a_n \in \mathbb{F}_q\) and nonzero multipliers \(v_1,\dots,v_n\),

  \[
  \mathrm{GRS}_k(\mathbf a, \mathbf v) \;=\; \big\{\,\big(v_1 f(a_1),\dots,v_n f(a_n)\big) : \deg f < k \,\big\},
  \]

  an \([n,k,n-k+1]_q\) MDS code; the self-orthogonality condition (Euclidean or Hermitian) becomes an explicit polynomial condition on \((\mathbf a, \mathbf v)\).

The **QMDS length problem:** for fixed \(q\) and distance \(d\) (or dimension \(k\)), determine the maximum length \(n\) for which a \([[n,k,d]]_q\) QMDS code exists. The **QMDS conjecture** asserts that, apart from a known exceptional family (of the form \([[q^2+2,\,q^2-4,\,4]]_q\) for \(q = 2^m\), verify), every stabilizer QMDS code with \(d \ge 3\) satisfies

\[
n \;\le\; q^2 + 1 ;
\]

the case \(d = 3\) is settled, larger \(d\) is open (verify). This ceiling is inherited from the classical MDS conjecture, which asserts that a classical \([n,k]_q\) MDS code with \(2 \le k \le q-1\) has

\[
n \;\le\; q + 1
\]

(with the two known exceptions at \(q = 2^m\), \(k \in \{3, q-1\}\)); the quantum length bound is its image under the Hermitian/CSS constructions.

The open problem, per instance: **for a specific \((q, k, d)\) or a specific target length \(n\), certify a QMDS code (construction) or prove no QMDS code with those parameters exists (nonexistence).** The cost measures are \(n\), \(k\), \(d\), \(q\); the alphabet is a qudit of prime-power dimension \(q\) unless otherwise declared. Start from this prompt alone - the Singleton bound, the MDS equality, and the two standard constructions are fixed above.

## 2. Resolution standard

Fix a specific \((q, k, d)\) (or \((q, n, d)\)). Resolution is **one** of:

1. **Construction.** An explicit \([[n,k,d]]_q\) code with \(k = n - 2d + 2\), self-orthogonality and exact distance certified; or

2. **Nonexistence.** A proof that no \([[n,k,d]]_q\) code with those parameters exists.

**Named certified form.** One of:

- **Certified construction.** The defining data (the constacyclic defining set, the GRS evaluation points and column multipliers, or the monomial-Cartesian twist vector) given exactly; the Hermitian/Euclidean self-orthogonality condition checked symbolically over \(\mathbb{F}_q\) / \(\mathbb{F}_{q^2}\); the exact minimum distance verified (MDS equality confirmed via the classical MDS property plus the quantum distance formula, or by an exact minimum-weight computation).

- **LP nonexistence with exact rounding.** The Shor–Laflamme quantum LP (weight enumerators, the MacWilliams identity, shadow inequalities, plus the MDS-equality constraints) shown infeasible, certified by an exact-rational dual (Farkas) certificate, with any fractional value rounded and justified in exact arithmetic.

- **Exhaustive symbolic nonexistence.** For small \(q, n\), a complete search over candidate Hermitian/Euclidean self-orthogonal generator matrices (up to the appropriate equivalence) showing none yields the target, with a stated and checked completeness / canonicity argument.

**Not accepted as resolution.**

- A code presented as MDS whose distance is only **sampled** or asserted from the template without the MDS equality checked exactly.

- A **floating-point** LP infeasibility with no exact dual certificate.

- A construction that violates the self-orthogonality condition (an invalid stabilizer code).

- An **incomplete** family search reported as nonexistence (a canonicity / coverage gap).

- An asymptotic length statement where a specific parameter case is asked.

- Restating the QMDS conjecture as if a specific case were resolved by analogy.

## 3. Graded partial-result targets

- **P1 - Reproduce known QMDS families.** Rebuild a documented QMDS construction (a constacyclic or GRS family) at small \(q\) and verify MDS equality exactly with our own toolchain. Certificate: symbolic self-orthogonality + exact distance.

- **P2 - Exact LP for MDS parameters.** Implement the quantum LP with MDS-equality constraints and reproduce known nonexistence/existence boundaries for small \(q, n\). Certificate: exact-rational duals across a band.

- **P3 - A settled small open case.** For one open \((q,k,d)\) at small \(q\), decide it: construct or prove nonexistent by exhaustion or LP. Certificate: exact construction or exact dual / complete search.

- **P4 - A new construction.** Produce a QMDS code at a length or distance not previously tabulated (a new constacyclic defining set, a new GRS multiplier choice), MDS equality certified. Certificate: defining data + exact distance proof.

- **P5 - A certified nonexistence.** Prove no QMDS code exists at a specific open \((q,k,d)\), fully certified (exact LP dual or exhaustive symbolic search with completeness), citing the open status it resolves. Certificate: complete manifest; independently re-checked.

- **P6 - Reusable QMDS harness.** An audited tool that, given \((q,k,d)\), runs the standard constructions and the exact LP and reports certified existence/nonexistence, validated against P1–P2. Certificate: source + second-backend agreement.

## 4. Known results and prior art

- **Bounds.** Quantum Singleton bound (Knill–Laflamme; Rains, quantum weight enumerators, late 1990s, verify). The QMDS conjecture and its exceptional family; the \(d = 3\) case bounding \(n \le q^2 + 1\) (verify), larger \(d\) open.

- **Constructions.** Grassl, Beth, Rötteler, *On optimal quantum codes* / quantum MDS from classical MDS (~2004, verify); constacyclic-code constructions (Kai, Zhu, Li; Chen, Ling, and others, ~2014, verify); generalized Reed–Solomon constructions (Jin, Xing; Zhang, Ge; and others, verify); Hermitian and Euclidean self-orthogonal MDS families; monomial-Cartesian and generalized-monomial-Cartesian constructions (Springer QIP, ~2024, verify).

- **Highly entangled / non-stabilizer.** QMDS codes and highly entangled subspaces (Huber, Grassl, ~2020, verify) - non-stabilizer QMDS existence can differ from the stabilizer conjecture.

- **Tables.** `codetables.de` and the survey literature track achieved QMDS lengths per \(q\); the baseline for any claim.

- **Entanglement-assisted.** EA-QMDS codes have their own Singleton-type bound and constructions (verify) - keep distinct unless explicitly targeted.

Status as of mid-2026 - re-verify against the current literature and tables before starting any session.

## 5. Attack plan

`[search]` `[sym]`. One workstation.

1. **Symbolic algebra core.** Work in \(\mathbb{F}_q\) and \(\mathbb{F}_{q^2}\) exactly (SageMath / GAP / Magma-if-available). Implement the Hermitian and Euclidean self-orthogonality tests and the GRS / constacyclic defining-set machinery symbolically; verify on a known family before trusting.

2. **Reproduce known families (P1).** Rebuild a documented QMDS construction and confirm MDS equality via the classical MDS property plus the quantum distance formula, cross-checked by an exact minimum-weight computation on small instances.

3. **Construction search (P3–P4).** Sweep constacyclic defining sets and GRS evaluation-point-and-multiplier choices for the target \((q,k,d)\); each candidate's self-orthogonality is checked symbolically and MDS equality certified exactly.

4. **Exact LP (P2, P5).** Reuse the Shor–Laflamme exact-rational quantum LP (problem 38's core) with MDS-equality constraints; solve in QSopt_ex / exact SoPlex; emit Farkas duals for nonexistence.

5. **Exhaustive symbolic nonexistence (P5).** For small \(q, n\), enumerate candidate self-orthogonal generators up to monomial/equivalence with a stated canonicity rule; certify completeness.

6. **Failure modes.** Field-arithmetic and equivalence-reduction bugs (guard with cross-implementation checks); asserting MDS from a template without the exact distance/equality check; incomplete family sweeps masquerading as nonexistence; floating-point LP values with no exact dual; qudit-alphabet and stabilizer-vs-nonstabilizer slips. Keep the baseline pinned to dated tables.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Self-orthogonality and minimum distance are checked symbolically / by proven-optimal minimum-weight computation; nonexistence carries an exact-rational LP dual or a complete, canonical exhaustion. Floating point is screening only.

2. **Independent verification.** A standalone checker, separate from the search, that (a) re-verifies self-orthogonality and MDS equality of a construction, and (b) re-checks the LP dual or replays the enumeration. A second algebra backend where available.

3. **Reproducibility.** Every defining set, generator matrix, LP file, solver/CAS name+version, and equivalence rule recorded; SHA-256 manifest over codes, LP files, and certificates; the exact table entry or open-case reference being addressed cited with access date.

4. **Preservation.** All construction, search, and LP source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).

5. **Honest reporting.** The report states up front, per \((q,k,d)\), whether the outcome is a certified construction, a certified nonexistence, or neither, in which model (stabilizer vs non-stabilizer, EA or not), and which open case or table entry it resolves - never presenting a template-asserted distance or a floating-point LP value as certified, and never restating the conjecture as a proof.
