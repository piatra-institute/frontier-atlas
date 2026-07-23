# PROMPT FOR A CERTIFIED MINIMAL ARITHMETIC CIRCUIT

## The minimum number of operations to compute a specific linear map or transform, with a checked certificate

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 47 of 50  
**Area:** search, sequences & games  
**Modes:** `[sym]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A straight-line program (SLP) computes a fixed function by a branch-free sequence of ring operations; its cost is the number of gates. For linear maps the natural gates are additions/subtractions and scalar multiplications, and the questions are exact and stubborn: what is the minimum number of *additions* to compute the \(n\)-point discrete Fourier transform (open even asymptotically in the unrestricted model), the minimum number of gates to compute a fixed \((0,1)\)-matrix–vector product (the "Boolean sum" / ensemble-computation SLP problem, NP-hard in general), or the minimum operations to evaluate a small fixed polynomial? Small instances are decidable by exact search, and every claim is machine-checkable: an SLP is verified by exact symbolic re-evaluation (over \(\mathbb Q\) or a large prime field), and optimality is a finite enumeration or a SAT/ILP refutation. The verifier that closes the loop is a symbolic SLP evaluator (the program computes the target map identically, checked in exact arithmetic) plus a lower-bound certificate (an exhaustive smaller-SLP enumeration, a DRAT-checked UNSAT, or a gate-elimination proof). Anything short of a matched construction and lower bound for a specified map - a good circuit with no lower bound, or an asymptotic operation count offered as the exact minimum - is a partial result, never a solution.

## 1. Exact problem statement

Fix a field \(\mathbb F\) (typically \(\mathbb Q\), \(\mathbb C\), or \(\mathrm{GF}(2)\)) and a target **linear map** \(A\in\mathbb F^{m\times n}\); the goal is to compute \(x\mapsto Ax\).

**Linear straight-line program.** A sequence of instructions \(g_1,\dots,g_C\); each \(g_k\) is either an input \(x_i\), or \(\alpha\, g_a + \beta\, g_b\) for previously computed \(g_a,g_b\) and scalars \(\alpha,\beta\in\mathbb F\). The program computes \(A\) if \(m\) designated gates equal the rows of \(Ax\) as formal linear forms in \(x\).

**Cost measures.**
- **Additive complexity** \(L_+(A)\): the minimum number of \(\pm\) gates when only additions/subtractions are allowed (the natural measure for a \((0,1)\)-matrix \(A\), where no scalar multiplication is needed).
- **Total linear complexity** \(L(A)\): minimum additions plus scalar multiplications, scalars unrestricted.
- **Bounded-coefficient complexity** \(L_{c}(A)\): as above but every scalar has \(|\alpha|\le c\) (the model in which the DFT has a proven \(\Omega(n\log n)\) bound).

**Transforms.** The \(n\)-point DFT is the linear map with matrix

\[
F_n=\bigl(\omega^{jk}\bigr)_{0\le j,k<n},\qquad \omega=e^{2\pi i/n},
\]

realized over the reals as a \(2n\times 2n\) map on real/imaginary parts. The open targets are the exact minimum number of real additions and the exact total operation count. In the bounded-coefficient model the standing lower bound is

\[
L_{1}(F_n)\ \ge\ \tfrac12\, n\log_2 n,
\]

while in the unrestricted model no superlinear lower bound is known for any explicit linear map. For a fixed \((0,1)\)-matrix the target is \(L_+(A)\); for a fixed small polynomial \(p\), the minimum multiplications/additions to evaluate it.

**Target.** Fix one concrete map - a specific small DFT size, a specific \((0,1)\)-matrix, or a specific polynomial - and certify the exact minimal circuit, or a verified lower bound. The cost measure (which gates are counted, and any coefficient restriction) is fixed and stated; a value in one model never transfers to another.

**Polynomial-evaluation companion.** For a univariate polynomial of degree \(d\), the minimum multiplications (with preconditioning) is governed by the Motzkin–Belaga bound

\[
\left\lfloor \tfrac{d}{2}\right\rfloor+1 \ \ \text{multiplications},\qquad d\ \text{additions},
\]

for a generic polynomial; specific small polynomials may need fewer, and certifying the exact figure for a named polynomial is a valid target.

**Decision form used by the search.** The optimum is located by the monotone family

\[
\mathrm{SLP}(A,\text{model},C):\quad \text{does a } C\text{-gate program in the fixed model compute } A?
\]

satisfiable for \(C\ge L_\bullet(A)\), unsatisfiable below; certifying \(L_\bullet(A)=C\) means a witness program for \(\mathrm{SLP}(A,\cdot,C)\) and a checked refutation of \(\mathrm{SLP}(A,\cdot,C-1)\).

A reader starting from this prompt alone has the SLP model, the three cost measures, the DFT and \((0,1)\)-matrix targets, the decision form, and the polynomial-evaluation companion.

## 2. Resolution standard

**Named certified form: exhaustive search or SAT/ILP with a checked optimality certificate.** A resolution of "\(L_\bullet(A)=C\)" for a fixed map and fixed model consists of two independently checkable artifacts.

1. **Upper bound (an SLP).** An explicit straight-line program of \(C\) gates, with a symbolic evaluator that substitutes formal variables, expands each gate, and confirms the designated outputs equal the rows of \(Ax\) as identical linear forms - in exact arithmetic over \(\mathbb Q\) (or by evaluating on the standard basis \(e_1,\dots,e_n\) and comparing the resulting matrix to \(A\) entrywise). The program plus the evaluator's accept is the certificate.
2. **Lower bound.** A machine-checked proof that no \(C-1\)-gate program in the fixed model computes \(A\), delivered as either
   - (a) an exhaustive isomorph-free enumeration of all \((C-1)\)-gate SLPs (up to the model's symmetries) whose completeness log an independent driver replays; or
   - (b) a DRAT/LRAT UNSAT proof of a SAT/ILP encoding "a \((C-1)\)-gate program computes \(A\)", checked by drat-trim / an exact ILP dual; or
   - (c) a gate-elimination / substitution argument reduced to a checkable inequality.

Both parts are mandatory: the exact value is proven only when the two meet, and verification is exact (never floating point).

Exactness is the crux. For \(\mathbb C\)-valued transforms, "computes \(A\)" is a statement about identical linear forms with algebraic-number coefficients; verify it symbolically over the cyclotomic field \(\mathbb Q(\omega)\), or by evaluation at the standard basis with exact arithmetic in \(\mathbb Q(\omega)\). A residual numerical check to machine precision is evidence only, never a certificate.

**Not accepted as resolution.**

- A circuit whose correctness is checked only numerically (floating point), rather than by exact symbolic equality or exact basis evaluation.
- An operation count from a named algorithm (split-radix, Winograd) presented as the *minimum* without a matching lower bound.
- A bounded-coefficient lower bound quoted as an unrestricted lower bound, or a multiplicative-complexity result quoted as an additive one.
- An SLP with no lower bound, an asymptotic bound where an exact integer is asked, or an enumeration/UNSAT that cannot be independently replayed.
- A lower bound whose scalar set was silently restricted (e.g. "assume coefficients in \(\{-1,0,1\}\)") without a proof that the restriction is without loss of generality for the target map.

## 3. Graded partial-result targets

Ordered from reproducing the known frontier to the strongest result short of a new general bound. Each names its certificate.

**P1 - Reproduce a known optimum.** For a small map with a settled minimum (a tiny DFT, a small \((0,1)\)-matrix, a named polynomial), recompute it: explicit SLP plus a checked lower bound (enumeration or DRAT UNSAT).
*Certificate:* symbolic-evaluator accept; replayable enumeration or checked UNSAT at \(C-1\).

**P2 - Verify a published construction.** Independently re-verify a record FFT or transform circuit (e.g. the split-radix or modified-split-radix operation count for a specific \(n\)) by exact symbolic evaluation, certifying its exact gate count as an upper bound.
*Certificate:* exact operation tally and symbolic-equality accept.

**P3 - Exact minimum for an open small map.** Certify \(L_\bullet(A)\) for one map beyond the known frontier by matched construction and lower bound.
*Certificate:* both artifacts of §2 under a SHA-256 manifest.

**P4 - Certified lower bound for a transform.** For a specific DFT size (or \((0,1)\)-matrix), certify the largest lower bound on the additive complexity the search budget reaches - a checked UNSAT at \(C-1\) or an exhaustive infeasibility.
*Certificate:* checked lower-bound proof; the gap to the best construction reported exactly, and the model (which gates counted, coefficient restriction) stated with it.

**P5 - GF(2) / XOR-count optimum.** For a fixed \(\mathrm{GF}(2)\) matrix (an MDS-matrix layer, a small linear map), certify the minimum XOR-gate count via SAT with DRAT.
*Certificate:* explicit XOR circuit re-evaluated over \(\mathrm{GF}(2)\); checked UNSAT lower bound.

**P6 - Polynomial-evaluation optimum.** For a named small polynomial, certify the exact minimum multiplications and additions, matching or beating the Motzkin–Belaga generic figure.
*Certificate:* explicit scheme plus a checked lower bound.

**P7 - Structure mining ([sym]).** From certified optimal circuits, extract a reusable identity or lower-bound lemma and state it as a precise conjecture with certified supporting data.
*Certificate:* the data table plus the conjecture, each datum individually certified.

## 4. Known results and prior art

- Bounded-coefficient lower bound: J. Morgenstern (~1973, *J. ACM*) proved that any linear algorithm computing the \(n\)-point DFT with coefficients of modulus \(\le 1\) uses at least \(\tfrac12 n\log_2 n\) operations; refined by Chazelle and by Ailon in terms of singular values / non-rigidity (verify).
- In the **unrestricted** model no superlinear lower bound is known for any explicit linear map - the exact additive complexity of the DFT is open, and even a general \(\omega(n)\) bound would be a breakthrough (Valiant's log-depth program; matrix rigidity, rank 07).
- FFT operation-count records: the split-radix algorithm uses \(4n\log_2 n-6n+8\) real operations (Yavne ~1968; Duhamel–Hollmann ~1984); Van Buskirk, and Johnson–Frigo, "A Modified Split-Radix FFT With Fewer Arithmetic Operations," *IEEE T. Signal Process.* (~2007), lowered this to \((34/9)n\log_2 n+O(n)\); the "tangent FFT" (Bernstein) reframes it (verify). These are upper bounds, not proven minima.
- Multiplicative complexity of the DFT: S. Winograd gave exact minimal-multiplication algorithms for several \(n\) (verify the settled sizes).
- \((0,1)\)-matrix / "ensemble computation" SLPs: for \(A\in\{0,1\}^{m\times n}\) the target is the fewest additions to compute all \(m\) subset-sums

  \[
  (Ax)_r=\sum_{i:\,A_{r,i}=1} x_i,\qquad r=1,\dots,m,
  \]

  which is NP-complete in general (the Ensemble Computation problem, Garey–Johnson, verify); gate-elimination gives lower bounds for explicit families.
- Polynomial evaluation: Motzkin and Belaga (generic bounds \(\lfloor d/2\rfloor+1\) multiplications, \(d\) additions), Paterson–Stockmeyer, Ostrowski (verify).
- GF(2) linear-circuit / XOR-count minimization is an active SAT-based area (minimizing the XOR cost of MDS matrices and linear layers; Kranz–Leander and others, verify).
- Caveat on models: the additive complexity \(L_+\), the total complexity \(L\), the bounded-coefficient complexity, and the multiplicative complexity are four different measures with four different literatures; a record in one is silent about the others, and prompts frequently conflate them.

**Status as of mid-2026 - re-verify against the current literature (and record trackers) before starting any session.**

## 5. Attack plan

`[sym]` `[search]` - first computations on one workstation. The [sym] mode owns exact verification and structure mining; the [search] mode owns the exhaustive/SAT optimality proofs.

- **Symbolic evaluator first.** Implement exact SLP evaluation in a CAS (SageMath / SymPy / FLINT): each gate carries the exact linear form

  \[
  g_k=\sum_{i=1}^{n} c_{k,i}\,x_i,\qquad c_{k,i}\in\mathbb F,
  \]

  built by combining operands; the program computes \(A\) iff the \(m\) output gates' coefficient vectors equal the rows of \(A\). Validate on textbook circuits (a \(2\)- or \(4\)-point DFT).
- **Reproduce records (P1, P2).** Re-encode the split-radix / modified-split-radix circuit for a small \(n\) and re-count its exact operations; re-verify a small Winograd DFT. This validates the tallying and the evaluator against published figures before any new search is trusted.
- **Exhaustive SLP search (P3, P6).** A custom C++/Sage generator enumerates SLPs gate-by-gate over a restricted scalar set (for \((0,1)\)-matrices, scalars \(\in\{-1,0,1\}\)) with canonical-form pruning: dedupe gates that compute the same linear form, order by a canonical key.
- **Search discipline.** Iterative deepening on \(C\); represent each gate's value as an exact linear form (a vector over \(\mathbb Q\) or \(\mathbb Q(\omega)\)) so equality tests are exact; the completeness log records the pruned frontier at each backtrack for independent replay.
- **SAT/ILP encoding (P4, P5).** Encode "a \(C\)-gate program computes \(A\)" with per-gate operand and coefficient variables and linear-form propagation; over \(\mathrm{GF}(2)\) the propagation is XOR constraints, and the model is exact and finite.
- **Solve and prove.** Run CaDiCaL / kissat → DRAT (checked by drat-trim/cake\_lpr) for the lower bound; SCIP with exact rational duals for ILP formulations. Every SAT witness is re-decoded to an SLP and re-evaluated symbolically before its gate count is accepted as an upper bound.
- **Lower-bound cross-checks.** Require the exhaustive enumeration and the SAT UNSAT to agree on every borderline instance; a gate-elimination bound, where available, is a third independent check.
- **Scalar-set control.** For rational-coefficient targets, restrict the search to a documented finite scalar set and prove separately that no scalar outside it can help (a common source of unsoundness); over \(\mathbb Q(\omega)\) fix an explicit integral basis.
- **One-workstation scope.** The SLP search space explodes combinatorially in \(C\) and in the scalar set; even modest maps are hard, so the certified frontier is small. Prefer \((0,1)\)-matrix and \(\mathrm{GF}(2)\) targets, where the scalar set is trivial, for the first closed values.
- **Failure modes.** Expect (i) infeasible exhaustive search beyond a small gate budget - report the certified inequality; (ii) numeric verification masquerading as exact (forbidden - use symbolic/exact only); (iii) model confusion (additive vs total vs bounded-coefficient, multiplicative vs additive); (iv) unverified UNSAT trusted on the solver's word. Record the largest map actually closed and in which model.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every upper bound is verified by exact symbolic equality or exact basis evaluation over \(\mathbb Q\)/\(\mathrm{GF}(2)\); every lower bound is a replayable exhaustive enumeration, a drat-trim/cake\_lpr-checked UNSAT, or an exact ILP dual. Floating point is for exploration only.
2. **Independent verification.** The symbolic evaluator, the search/encoder, and the operation-tally are separate programs; each lower bound is confirmed by at least two of {enumeration, SAT UNSAT, gate-elimination}; every SAT/ILP witness is re-decoded and re-evaluated symbolically.
3. **Reproducibility.** The target matrix \(A\), the model and scalar restrictions, encodings, canonicalization, solver/CAS names and versions, and seeds are recorded; a SHA-256 manifest covers every circuit, proof, and log. Any reproduced or extended record is cited with source and access date.
4. **Preservation.** Evaluator, generator, encoder, and checker source are part of the record. Any discarded run or lost proof is stated explicitly.
5. **Honest reporting.** The report states up front, per map, whether both bounds were certified (hence the exact minimum), in which model (additive / total / bounded-coefficient / GF(2)), or only one side (an inequality). An algorithm's operation count is reported as an upper bound, never as the proven minimum.
