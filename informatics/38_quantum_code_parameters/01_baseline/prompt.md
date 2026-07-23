# PROMPT FOR IMPROVING THE PARAMETERS OF A QUANTUM ERROR-CORRECTING CODE

## Best \(((n,K,d))\) for a specific length and distance - the quantum analog of \(A(n,d)\)

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 38 of 50
**Area:** quantum computation & codes
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Fault-tolerant quantum computing rests on error-correcting codes, and the same optimization that drives classical coding theory - for length \(n\) and distance \(d\), how large a code can exist - has a quantum analog with its own tables of best-known bounds. Grassl's `codetables.de` tracks, for each \((n,d)\), the best lower bound (an explicit code) and the best upper bound (typically a linear-programming argument), and many entries remain open, with a gap between the two. The task is to move one such entry: either construct a code beating the recorded lower bound, or prove a tighter upper bound than the recorded one. Both directions close on the machine. A construction is verified by checking the stabilizer/CWS conditions and the exact minimum distance; an upper bound is a quantum linear-programming (LP) bound - an optimization over Shor–Laflamme weight enumerators with the quantum MacWilliams identities and the shadow inequalities - whose optimum, to count as a certified integer bound, must be produced with exact rational arithmetic and correct rounding. The verifier that closes the loop is exact: a distance recomputation for a construction, and an exact-rational LP dual (Farkas) certificate for a bound. This is kept strictly distinct from the mathematics program's **classical** codes (problem 35 there). Anything short of the section-2 standard - a numeric LP value, a code whose distance is only sampled, an asymptotic estimate - is a partial result, never a solution.

## 1. Exact problem statement

A **quantum code** on \(n\) qubits is a subspace \(Q \subseteq (\mathbb{C}^2)^{\otimes n}\) of dimension \(K\), with projector \(P\). It has **distance** \(d\) if it detects all Pauli errors of weight \(< d\); equivalently the Knill–Laflamme condition holds:

\[
P\, E\, P \;=\; c(E)\, P
\qquad\text{for every Pauli } E \text{ with } \mathrm{wt}(E) \le d-1 .
\]

Such a code is written \(((n,K,d))\); when \(K = 2^k\) and the code is a stabilizer code it is written \([[n,k,d]]\). A stabilizer code is fixed by an abelian subgroup \(S\) of the \(n\)-qubit Pauli group with \(-I \notin S\); via the symplectic representation \(S\) is a self-orthogonal \(\mathbb{F}_2\)-code in \(\mathbb{F}_2^{2n}\) (equivalently additive over \(\mathrm{GF}(4)\), CRSS), and

\[
d \;=\; \min\{\,\mathrm{wt}(P) : P \in N(S)\setminus S\,\}
\]

(the pure/impure distinction: the code is pure if this minimum equals \(\min\{\mathrm{wt}(P) : P \in N(S), P \ne I\}\)).

The **Shor–Laflamme weight enumerators** of a code with projector \(P\) (dimension \(K\)) are

\[
A_j = \frac{1}{K^2}\sum_{\mathrm{wt}(E)=j} \big|\mathrm{Tr}(E P)\big|^2,
\qquad
B_j = \frac{1}{K}\sum_{\mathrm{wt}(E)=j} \mathrm{Tr}(E P E P),
\]

summed over Paulis \(E\) of weight \(j\). They satisfy the **quantum MacWilliams identity**

\[
B(x,y) \;=\; A\!\left(\tfrac{x+3y}{2},\ \tfrac{x-y}{2}\right),
\]

together with \(A_0 = B_0 = 1\), the inequalities \(0 \le A_j \le B_j\), Rains' **shadow** inequalities, and - for a distance-\(d\) code - \(A_j = B_j\) for \(j < d\), with \(B_d > A_d\) in the impure case. The **shadow enumerator** \(S_j\), obtained from \(A\) by the substitution

\[
S(x,y) \;=\; A\!\left(\tfrac{-x+3y}{2},\ \tfrac{x+y}{2}\right),
\qquad
S_j \ge 0 \ \ \forall j,
\]

supplies the extra linear inequalities that make the quantum LP substantially stronger than the classical MacWilliams LP. The upper-bound optimization is then

\[
\max\ K \quad\text{subject to}\quad
\{A_j, B_j, S_j \ge 0\},\ \ B = \mathrm{MacW}(A),\ \ S = \mathrm{Shad}(A),\ \ A_j = B_j\ (j<d),
\]

a finite linear program in the enumerator coefficients once \(n\) and \(d\) are fixed.

Define, for fixed \(n\) and \(d\),

\[
K^{*}(n,d) \;=\; \max\{\,K : \text{an } ((n,K,d)) \text{ code exists}\,\}
\]

(or, restricted to stabilizer codes, the maximum \(k\)). The open problem, per entry: **for a specific \((n,d)\), close or narrow the gap between the best lower and upper bounds on \(K^{*}(n,d)\).** The cost measures are the dimension \(K\) (or \(k\)) and the distance \(d\); everything is over qubits unless a qudit alphabet \(q\) is explicitly declared. Start from this prompt alone - the code parameters, the Knill–Laflamme condition, the enumerators, and the MacWilliams/shadow constraints are all fixed above.

## 2. Resolution standard

Fix a specific \((n,d)\) (and alphabet). Resolution is **one** of:

1. **Improved lower bound (construction).** An explicit code with \(K > K_{\text{recorded}}\) (or \(k > k_{\text{recorded}}\)), with its exact minimum distance \(\ge d\) verified; or

2. **Improved upper bound.** A proof that \(K^{*}(n,d) < K_{\text{recorded}}\) via a quantum LP bound with an exact-rational certificate.

**Named certified form.** One of:

- **Explicit stabilizer construction with a checked distance.** The stabilizer generators (or the GF(4)-additive generator matrix) given exactly; self-orthogonality checked; the minimum weight of \(N(S)\setminus S\) computed exactly (coset-leader / minimum-weight search or an exact ILP), certifying \(d\). A CWS or non-stabilizer construction is admissible if the Knill–Laflamme conditions are verified exactly.

- **Quantum LP bound with exact rounding.** The Shor–Laflamme LP (variables \(A_j, B_j\); constraints: the MacWilliams identity, \(0 \le A_j \le B_j\), \(A_j = B_j\) for \(j < d\), the shadow inequalities, normalization) is infeasible for the recorded \(K\), certified by an **exact rational dual (Farkas) certificate**; any fractional optimum is rounded down with the rounding step written out and justified. The solve is done in exact arithmetic (QSopt_ex / exact SoPlex / SCIP with rational data), never floating point alone.

**Not accepted as resolution.**

- A construction whose distance is only **sampled** or checked against low-weight errors up to some cutoff below \(d\).

- A **floating-point** LP optimum reported as an integer bound without an exact dual certificate and an explicit rounding argument.

- A code beating the lower bound but violating self-orthogonality / Knill–Laflamme (an invalid code).

- An asymptotic \(A_q(n,d)\)-style estimate where an exact per-entry bound is asked.

- Improving a bound **already** superseded on the current `codetables.de` (the baseline must be the live table with an access date).

- Anything conflating this quantum table with the classical codes of the mathematics program.

## 3. Graded partial-result targets

- **P1 - Reproduce a table row.** For a chosen \((n,d)\), independently reproduce both the recorded lower bound (rebuild the code, recompute \(d\) exactly) and the recorded quantum LP upper bound (re-solve with an exact dual). Certificate: exact distance + exact Farkas certificate matching the table.

- **P2 - Exact LP frontier.** Implement the full Shor–Laflamme LP with shadow inequalities and reproduce the LP bound for a band of \((n,d)\) at small \(n\) (say \(n \le 12\)). Certificate: exact-rational duals across the band.

- **P3 - A narrowed gap.** For one open \((n,d)\), improve *either* bound by hand-plus-search (a better construction, or a strengthened LP with additional valid inequalities). Certificate: exact construction or exact dual, plus the cited superseded baseline.

- **P4 - A new explicit code.** Construct a code meeting or beating the recorded lower bound for an open entry (via GF(4)-additive search, cyclic/quasi-cyclic families, or CWS search), distance certified exactly. Certificate: generator data + exact minimum-weight proof.

- **P5 - A strictly improved table entry.** Move the best-known lower or upper bound on `codetables.de` for a specific \((n,d)\), fully certified in both the construction/bound and the baseline it beats. Certificate: complete manifest; independent recomputation of distance or dual.

- **P6 - Reusable exact-LP tool.** An audited, exact-rational quantum-LP solver (with shadow inequalities and rounding) that emits Farkas certificates, validated against P1–P2. Certificate: source + agreement with a second exact solver on shared instances.

## 4. Known results and prior art

- **Foundations.** Knill, Laflamme error-correction conditions (~1997); Calderbank, Rains, Shor, Sloane (CRSS), *Quantum error correction via codes over GF(4)*, IEEE Trans. Inf. Theory (1998) - stabilizer = additive GF(4) self-orthogonal code.

- **Weight enumerators & LP bound.** Shor, Laflamme, quantum MacWilliams identities / weight enumerators (1997); Rains, *Quantum weight enumerators*, *Shadow enumerators*, and the quantum Singleton / Rains bounds (late 1990s–2000, verify) - the shadow inequalities and the LP method; Ashikhmin–Litsyn LP bounds.

- **Tables.** M. Grassl, `codetables.de` - the live tracker of best-known lower/upper bounds on quantum (and classical) code parameters; the baseline for any claim.

- **Small optimal codes.** \([[5,1,3]]\) (perfect), \([[7,1,3]]\) Steane, \([[8,3,3]]\), \([[15,1,3]]\) Reed–Muller; many small entries are proven-optimal, many larger ones are open.

- **Bounds & existence.** Quantum Singleton bound \(k \le n - 2d + 2\); quantum Gilbert–Varshamov existence bounds; Feng–Ma finite GV bound for pure stabilizer codes (verify). Entanglement-assisted variants have their own split-weight-enumerator LP (Lai–Ashikhmin, ~2016, verify).

Status as of mid-2026 - re-verify against the current `codetables.de` and literature before starting any session.

## 5. Attack plan

`[search]` `[opt]`. One workstation.

1. **Exact LP core.** Build the Shor–Laflamme LP symbolically: \(A_j, B_j\) variables, the MacWilliams transform as an exact rational matrix, \(0 \le A_j \le B_j\), \(A_j = B_j\) for \(j < d\), and the Rains shadow inequalities. Solve with QSopt_ex / exact SoPlex / SCIP(rational). Emit and store the dual (Farkas) certificate; round down explicitly.

2. **Reproduce before improving.** Match a handful of `codetables.de` upper-bound entries exactly (P1–P2) so the encoder is trusted, and re-solve with a second exact backend.

3. **Construction search.** GF(4)-additive / stabilizer search in SageMath/GAP (cyclic, quasi-cyclic, CSS from classical pairs \(C_2^{\perp} \subseteq C_1\)); CWS-code search for non-additive candidates. Screen many candidates, then certify the best.

4. **Exact distance.** For each candidate compute the true minimum weight of \(N(S)\setminus S\) exactly - a minimum-weight coset search or an exact ILP (SCIP) - never a sampled estimate.

5. **Strengthen the LP.** Add valid inequalities beyond the standard shadow set (Rains' additional constraints; split enumerators if entanglement-assisted) and re-certify.

6. **Failure modes.** The LP grows with \(n\) but stays workstation-scale up to \(n\) a few tens; the trap is a floating-point optimum with no exact dual (never report it as a bound); exact minimum-distance computation is the real bottleneck (NP-hard in general) - use ILP with proven optimality, not a truncated search; self-orthogonality/normalizer bugs produce invalid "codes"; alphabet (qubit vs qudit) slips. Keep the baseline pinned to the dated table.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Distances are computed exactly (proven-optimal minimum-weight search / ILP); LP bounds carry exact-rational dual certificates with the rounding step written out. Floating point is screening only.

2. **Independent verification.** A standalone checker, separate from the search, that (a) re-verifies self-orthogonality and recomputes the minimum distance of a construction, and (b) re-checks the LP dual certificate (dual feasibility, sign, and the rounding). A second exact LP backend on the same instance.

3. **Reproducibility.** Every generator matrix, LP data file, solver name+version, and rounding decision recorded; SHA-256 manifest over codes, LP files, and certificates; the exact `codetables.de` entry being matched or beaten cited with its access date.

4. **Preservation.** All construction and LP source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).

5. **Honest reporting.** The report states up front, per \((n,d)\), whether a bound was strictly improved and in which direction (lower vs upper), whether the code/bound is fully certified, and against which dated table entry - never presenting a floating-point LP value or a sampled distance as a certified bound, and never conflating this with the classical-code program.
