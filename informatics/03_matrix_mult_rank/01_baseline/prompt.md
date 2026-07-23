# PROMPT FOR PINNING THE TENSOR RANK OF SMALL MATRIX MULTIPLICATION

## The rank of \(\langle 3,3,3\rangle\) and small-format rank / border-rank brackets

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 03 of 50
**Area:** algorithms & bilinear complexity
**Modes:** `[sym]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The tensor rank \(R(\langle n,n,n\rangle)\) is the minimum number of scalar multiplications in any bilinear algorithm for multiplying two \(n\times n\) matrices; it is the exact-complexity heart of fast matrix multiplication. Strassen's \(R(\langle 2,2,2\rangle)=7\) is settled (optimality via Hopcroft–Kerr and Winograd), but the next case is wide open: \(R(\langle 3,3,3\rangle)\) is known only to lie in the bracket \([19,23]\) - upper bound \(23\) (Laderman, 1976) and lower bound \(19\) (Bläser). Progress is inherently certifiable: an upper bound is an explicit decomposition of the structure tensor into \(r\) rank-one triples whose correctness is a polynomial identity checkable exactly, and a lower bound is an algebraic or combinatorial argument (substitution method, Gröbner/rank obstructions, or SAT over a finite field) with a machine-checkable core. This matches current AI methods precisely: flip-graph search and SAT recently reshaped the field (new small-format and modular schemes, 2022–2024), and symbolic computation certifies each identity. The on-machine verifier that closes the loop is exact polynomial-identity checking of a claimed decomposition (over \(\mathbb{Q}\) or a fixed finite field) and a replayable lower-bound certificate. Any single decomposition without a matching lower bound, or a numerical-only scheme, is a partial result.

## 1. Exact problem statement

For positive integers \(m,n,p\), matrix multiplication \(\langle m,n,p\rangle\) is the bilinear map \(\mathbb{F}^{m\times n}\times\mathbb{F}^{n\times p}\to\mathbb{F}^{m\times p}\), \((A,B)\mapsto AB\). Its **structure tensor** \(T_{\langle m,n,p\rangle}\in\mathbb{F}^{mn}\otimes\mathbb{F}^{np}\otimes\mathbb{F}^{pm}\) has entries indexed so that \((AB)_{ik}=\sum_{j}A_{ij}B_{jk}\). A **rank-\(r\) decomposition** over \(\mathbb{F}\) is a set of triples \(\{(u_\ell,v_\ell,w_\ell)\}_{\ell=1}^{r}\) with

\[
T_{\langle m,n,p\rangle}=\sum_{\ell=1}^{r} u_\ell\otimes v_\ell\otimes w_\ell ,
\]

equivalently a bilinear algorithm computing each output via \(r\) products

\[
p_\ell=\Big(\textstyle\sum_{ij}u_\ell^{ij}A_{ij}\Big)\Big(\textstyle\sum_{jk}v_\ell^{jk}B_{jk}\Big),\qquad (AB)_{ik}=\sum_\ell w_\ell^{ik}\,p_\ell .
\]

The **tensor rank** is

\[
R(\langle m,n,p\rangle)=\min\{\,r:\ T \text{ has a rank-}r\text{ decomposition over }\mathbb{F}\,\},
\]

and the **border rank** \(\underline{R}\) allows entries in \(\mathbb{F}(\varepsilon)\) with the identity holding modulo \(O(\varepsilon)\) (approximate / degeneration rank).

**Conventions.**

- Both ranks are **field-dependent**; fix the field explicitly (default \(\mathbb{Q}\); modular results over \(\mathbb{F}_2\) or \(\mathbb{F}_p\) must say so).
- Rank is invariant under the \(\mathrm{GL}\times\mathrm{GL}\times\mathrm{GL}\) sandwiching symmetry and the cyclic/transpose symmetries of matrix multiplication; the search may exploit and must document any symmetry used.
- "Number of additions" (the linear cost of forming the \(u_\ell,v_\ell\) combinations and recombining) is a *separate* measure from rank; reducing additions at fixed rank does not change \(R\).

**Frontier adopted here.**

- Primary: \(R(\langle 3,3,3\rangle)\), bracket \([19,23]\) over \(\mathbb{Q}\).
- Secondary: rank or border-rank brackets of small formats \(\langle 2,2,n\rangle,\langle 2,3,3\rangle,\langle 3,3,3\rangle\) over specified fields, and modular ranks over \(\mathbb{F}_2\).

**Known values and brackets (to reproduce and re-verify).**

- \(R(\langle 2,2,2\rangle)=7\) and \(\underline{R}(\langle 2,2,2\rangle)=7\) (fully settled).
- \(R(\langle 2,2,3\rangle)=11\), \(R(\langle 2,3,3\rangle)\in[14,15]\) (open), \(R(\langle 3,3,3\rangle)\in[19,23]\) (open).
- Over \(\mathbb{Q}\), no rank-\(22\) scheme for \(\langle 3,3,3\rangle\) is known and none is ruled out; the whole bracket \([19,23]\) is live.

Re-verify all values against Section 4.

## 2. Resolution standard

A **resolution** of a rank value is an exact integer \(R\) (over the stated field) with **both** sides certified.

1. **Upper bound (decomposition).** An explicit list of \(r\) triples with rational (or fixed-field) entries and an **exact polynomial-identity check** that \(\sum_\ell u_\ell\otimes v_\ell\otimes w_\ell\) equals the structure tensor entrywise, performed in exact arithmetic by a checker written separately from the search.
   - *Preferred form:* the decomposition file plus a Macaulay2/SageMath verification script that expands both sides and confirms the zero difference.
2. **Lower bound (optimality).** A certificate that no rank-\((R-1)\) decomposition exists over the stated field. Accepted named forms:
   - (a) a **substitution-method / Alexeev–Bläser** argument reduced to a finite, checkable case analysis;
   - (b) a **Gröbner-basis infeasibility certificate** - the Macaulay2/Singular computation showing the rank-\((R-1)\) variety is empty, with the ideal and monomial order recorded;
   - (c) over a finite field, a **DRAT/LRAT UNSAT proof** for the SAT encoding "a rank-\((R-1)\) decomposition exists over \(\mathbb{F}_q\)".

**Not accepted as resolution.**

- A new decomposition (upper bound) with no matching lower bound - including a fewer-additions scheme at the same rank \(23\).
- A numerically found decomposition whose identity is only checked in floating point (must be exact / rational).
- A lower bound over one field claimed for another (e.g. an \(\mathbb{F}_2\) SAT bound reported as a \(\mathbb{Q}\) bound).
- A border-rank result reported as a (tensor) rank result, or conversely.
- An "AlphaTensor-style" scheme reported as improving \(R(\langle 3,3,3\rangle)\) when it merely re-attains \(23\) or applies to a different format/field.
- A rank bound derived from an unverified symmetry ansatz (assuming the decomposition inherits a group symmetry) without proof that optimum-preserving.

## 3. Graded partial-result targets

- **P1 - Reproduce the bracket.** Exactly verify Laderman's rank-\(23\) decomposition and Strassen's rank-\(7\); reproduce \(R(\langle 2,2,2\rangle)\ge 7\) and re-check (or re-derive) the standing \(R(\langle 3,3,3\rangle)\ge 19\) argument.
  - *Certificate:* exact identity checks and a replayable lower-bound log; SHA-256 manifest.
- **P2 - New certified decomposition.** A rank-\(23\) scheme for \(\langle 3,3,3\rangle\) with new structure (fewer additions, all-ternary coefficients, or a fresh symmetry), exactly verified - or a rank-\(r\) scheme with \(r<23\) if found (a genuine breakthrough).
  - *Certificate:* the decomposition and its exact check.
- **P3 - Improved lower bound (finite field).** A DRAT/LRAT UNSAT proof raising the \(\mathbb{F}_2\) (or \(\mathbb{F}_p\)) lower bound for \(\langle 3,3,3\rangle\) or a small rectangular format above the currently certified value.
  - *Certificate:* the certified UNSAT proof and the CNF encoding with its symmetry-breaking note.
- **P4 - Improved lower bound (\(\mathbb{Q}\)).** A Gröbner/substitution certificate raising \(R(\langle 3,3,3\rangle)\ge 20\) (or higher) over \(\mathbb{Q}\).
  - *Certificate:* the recorded ideal, monomial order, and infeasibility computation, independently re-run.
- **P5 - Close a small-format bracket.** Pin an open small-format rank exactly (e.g. \(\underline{R}\) or \(R\) of \(\langle 2,3,3\rangle\) over a stated field) meeting Section 2 on both sides.
  - *Certificate:* matching upper and lower certificates for that format.
- **P6 - Resolve \(\langle 3,3,3\rangle\).** Matching upper and lower bounds pinning \(R(\langle 3,3,3\rangle)\) over \(\mathbb{Q}\).
  - *Certificate:* the full two-sided package per Section 2.
- **P7 - Modular map.** A certified table of \(R_{\mathbb{F}_q}(\langle 3,3,3\rangle)\) for several small \(q\), documenting where the modular rank drops below the \(\mathbb{Q}\)-value.
  - *Certificate:* per-\(q\) decompositions and finite-field lower-bound certificates.

## 4. Known results and prior art

- **Settled base case.** Strassen (1969) - \(R(\langle 2,2,2\rangle)\le 7\); Hopcroft–Kerr (1971) and Winograd (1971) - optimality, \(R(\langle 2,2,2\rangle)=7\). Landsberg (2006) - border rank \(\underline{R}(\langle 2,2,2\rangle)=7\).
- **\(3\times3\) upper bound.** Laderman (1976) - rank \(23\) over \(\mathbb{Q}\) (98 additions originally). Additions have since been cut at rank \(23\): Schwartz–Vaknin (~61 via change of basis), Mårtensson–Wagner (~62), Stapleton (~60), and a 2025 flip-graph-derived scheme with **58 additions and all-ternary coefficients** (*verify*). None reduces the rank below \(23\).
- **\(3\times3\) lower bound.** Bläser (~1999/2003) - \(R(\langle 3,3,3\rangle)\ge 19\); Bläser's general bound \(R(\langle n,n,n\rangle)\ge 2.5n^2-3n\).
- **Border-rank bounds.** Landsberg–Ottaviani \(\underline{R}(\langle n,n,n\rangle)\ge 2n^2-n\), improved to \(2n^2-\log_2 n-1\) (Landsberg–Michałek), giving a small-\(n\) border-rank floor for \(\langle 3,3,3\rangle\) around \(15\text{–}17\) (*verify* the current exact value).
- **Flip-graph and machine search.** Kauers and Moosbauer (~2022–2023) - flip-graph search rediscovering and improving small-format schemes, including modular improvements to \(\langle 4,5,5\rangle,\langle 5,5,5\rangle\); Kauers–Wood, "meta flip graph" (~2025).
- **Reinforcement learning.** Fawzi et al. / DeepMind **AlphaTensor** (2022) - RL-found decompositions matching \(23\) for \(\langle 3,3,3\rangle\) and improving certain modular/rectangular formats (e.g. \(\langle 4,4,4\rangle\) mod 2); it did **not** break \(23\) over \(\mathbb{Q}\).
- **SAT / algebra tooling.** Heule et al. - SAT over finite fields ruling out low-rank decompositions with symmetries (~2024); Macaulay2/Singular Gröbner infeasibility for exact lower bounds; a 2026 preprint on automated finite-field lower bounds for small formats (*verify*).
- **Surveys.** Bürgisser–Clausen–Shokrollahi, *Algebraic Complexity Theory* (1997), and Landsberg, *Geometry and Complexity Theory* (2017) - the standard references for exact ranks, the substitution method, and border-rank geometry.
- **Modular subtlety.** Ranks can genuinely drop over small finite fields (AlphaTensor's mod-2 improvements); a modular result never implies the \(\mathbb{Q}\)-value and must be labelled by field.

**Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

**`[sym]` - upper bounds and exact certification.**

1. Represent the structure tensor and any candidate decomposition symbolically over the chosen field.
2. Run **flip-graph search** from a known rank-\(23\) scheme, applying flips and reductions over \(\mathbb{Q}\) and over \(\mathbb{F}_2\).
3. Export every candidate reaching lower rank or new structure to an independent exact identity verifier (Macaulay2/SageMath).
4. Canonicalize schemes under the sandwiching symmetry to detect genuine novelty.

**`[search]` - lower bounds.**

1. Finite field: encode "\(\exists\) rank-\(r\) decomposition over \(\mathbb{F}_q\)" as CNF (Boolean variables per coordinate of \(u_\ell,v_\ell,w_\ell\); the tensor identity as parity/XOR constraints).
2. Run CaDiCaL/kissat/CryptoMiniSat with DRAT/LRAT; symmetry-break with the group action and argue soundness.
3. Over \(\mathbb{Q}\): set up the rank-\(r\) decomposition variety as a polynomial system and test emptiness with a Gröbner-basis computation, or apply the substitution method to reduce to a finite checkable analysis.

**Tools.**

- Algebra: SageMath, Macaulay2, Singular (exact identity checks, Gröbner bases).
- Search: flip-graph code (Kauers–Moosbauer style, custom C++); FLINT for exact \(\mathbb{F}_q\) linear algebra.
- SAT: CaDiCaL, kissat, CryptoMiniSat with DRAT/LRAT and drat-trim/cake_lpr.

**First concrete session steps.**

1. Load the structure tensor for \(\langle 3,3,3\rangle\); verify Laderman's rank-\(23\) scheme with the independent checker (P1).
2. Reproduce a small flip-graph run over \(\mathbb{F}_2\) to confirm the search rediscovers known low-rank schemes.
3. Stand up the \(\mathbb{F}_2\) SAT lower-bound encoding at rank \(21\) and confirm it is quickly SAT (sanity), then probe the frontier rank.
4. Scope the \(\mathbb{Q}\) Gröbner lower bound on the smallest tractable format (\(\langle 2,2,2\rangle\) at rank \(6\)) before touching \(\langle 3,3,3\rangle\).
5. Decide the session's realistic aim (most sessions land at P2 or P3); commit the exact field and measure in the report header before any number is produced.

**One-workstation scope and failure modes.** Flip-graph upper-bound search and exact identity checking fit comfortably on one workstation and are the likeliest source of a concrete new artifact. Dominant risks:

- The \(\mathbb{Q}\) lower bound (Gröbner emptiness for rank \(22\)) is very likely infeasible at full \(3\times3\) scale - expect memory blow-up; scope to smaller formats or finite fields.
- SAT lower bounds over \(\mathbb{F}_2\) may not close for rank \(22\); UNSAT proofs can be enormous.
- Floating-point "decompositions" that fail exact checking; conflating field, rank vs border rank, or format; unsound symmetry breaking in the SAT encoding.

Report the exact field and measure with every number.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every decomposition is verified by exact rational (or exact finite-field) polynomial-identity checking; every lower bound is a Gröbner infeasibility certificate, a finite substitution-method case analysis, or a DRAT/LRAT UNSAT proof. Floating point is exploration only.
2. **Independent verification.** The identity checker is written separately from the search (e.g. a SageMath check of a flip-graph output); a second solver re-runs any SAT lower bound on a sub-instance; Gröbner results are re-run with a different monomial order or system (Macaulay2 vs Singular).
3. **Reproducibility.** The field, tensor indexing convention, symmetry-breaking group action, solver/CAS versions, and monomial orders are recorded; a SHA-256 manifest covers every decomposition, CNF, proof, and ideal file; the specific record improved (Laderman, a flip-graph scheme, or a lower bound) is cited with source and access date.
4. **Preservation.** Flip-graph search code, SAT encoders, CAS scripts, and all decompositions and certificates are part of the record; anything not preserved (a large UNSAT proof) is stated with its hash and regeneration command.
5. **Honest reporting.** The report states up front the field, whether tensor rank or border rank, and whether a bracket was narrowed or a value pinned; a fewer-additions scheme at rank \(23\) is reported as an addition-count improvement, not a rank improvement, and a numerical scheme is never represented as a certified decomposition.
