# PROMPT FOR THE MAXIMUM NONLINEARITY OF NINE-VARIABLE BOOLEAN FUNCTIONS

## The covering radius of the first-order Reed–Muller code \(\mathrm{RM}(1,9)\)

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 09 of 50
**Area:** Boolean & cryptographic functions
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The nonlinearity of a Boolean function - its Hamming distance to the nearest affine function - is the single most cited measure of resistance to linear cryptanalysis, and its maximum over all \(n\)-variable functions is exactly the covering radius of the first-order Reed–Muller code \(\mathrm{RM}(1,n)\). For even \(n\), bent functions attain the tight bound \(2^{n-1}-2^{n/2-1}\). For odd \(n\) the truth is stranger: the "bent-concatenation" value \(2^{n-1}-2^{(n-1)/2}\) was long believed maximal, until Patterson and Wiedemann (1983) exceeded it at \(n=15\). The exact maximum is settled only for \(n\le 7\); for \(n=9,11,13\) it is **open**. For \(n=9\) the record lower bound is \(242\) and the covering radius is pinned to \(\{242,244\}\). The task fits certified search and bound optimization precisely: the object is a length-\(512\) bit vector, nonlinearity is an exact Walsh-transform computation, and the frontier has repeatedly moved through symmetry-restricted search (rotation-symmetric and idempotent classes). The on-machine verifier is a fast Walsh–Hadamard transform giving nonlinearity exactly; anything short of the Section 2 standard - a construction with no matching upper bound, an unverified heuristic optimum - is a partial result, never the value.

## 1. Exact problem statement

A **Boolean function** in \(n\) variables is a map \(f:\mathbb{F}_2^n\to\mathbb{F}_2\); the space of all such is written \(\mathcal{B}_n\), with \(|\mathcal{B}_n|=2^{2^n}\). Represent \(f\) by its truth table, a vector in \(\{0,1\}^{2^n}\). Its \(\pm1\) **sign function** is \(\hat f(x)=(-1)^{f(x)}\). The **Walsh–Hadamard transform** at \(w\in\mathbb{F}_2^n\) is
\[
W_f(w)=\sum_{x\in\mathbb{F}_2^n}(-1)^{f(x)+\langle w,x\rangle},
\qquad \langle w,x\rangle=\textstyle\sum_i w_i x_i \bmod 2 .
\]
The **nonlinearity** of \(f\) is its minimum Hamming distance to the set of affine functions \(\langle w,x\rangle+c\):
\[
\mathrm{nl}(f)=2^{n-1}-\tfrac12\max_{w\in\mathbb{F}_2^n}\bigl|W_f(w)\bigr|.
\]

Here \(\mathrm{wt}(u)\) is the Hamming weight of \(u\in\mathbb{F}_2^{2^n}\) and \(d(u,u')=\mathrm{wt}(u+u')\) the Hamming distance; the **affine functions** are the \(2^{n+1}\) maps \(x\mapsto\langle w,x\rangle+c\). The **algebraic normal form** writes \(f(x)=\bigoplus_{S\subseteq[n]}a_S\prod_{i\in S}x_i\) and the **algebraic degree** \(\deg f\) is the largest \(|S|\) with \(a_S=1\). Two useful identities constrain the spectrum: **Parseval**,
\[
\sum_{w\in\mathbb{F}_2^n}W_f(w)^2=2^{2n},
\]
which forces \(\max_w|W_f(w)|\ge 2^{n/2}\) (bent functions meet it with equality), and the **autocorrelation / Wiener–Khinchin** relation \(\sum_w W_f(w)^2(-1)^{\langle w,a\rangle}=2^n\sum_x(-1)^{f(x)+f(x+a)}\).

The **first-order Reed–Muller code** \(\mathrm{RM}(1,n)\) is the set of truth tables of all affine functions, a \([2^n,\,n+1]\) binary linear code. Its **covering radius** \(\rho(1,n)=\max_{f\in\mathcal{B}_n}\min_{a\in\mathrm{RM}(1,n)} d(f,a)\) equals \(\max_{f}\mathrm{nl}(f)\); this quantity is denoted \(N_{\max}(n)\).

The **bent-concatenation** construction takes \(f\in\mathcal{B}_{n-1}\) bent (\(n-1\) even) and forms \(g(x_1,\dots,x_n)=f(x_1,\dots,x_{n-1})\oplus (x_n\cdot h)\)-style concatenations to reach \(\mathrm{nl}(g)=2^{n-1}-2^{(n-1)/2}\) for odd \(n\); the whole point of the odd-\(n\) problem is whether one can do strictly better.

**Coding-theory reading.** Since \(\mathrm{RM}(1,n)\) has \(2^{n+1}\) codewords, computing \(\min_{a}d(f,a)\) for a fixed \(f\) is one Walsh transform; the covering radius asks for the \(f\) maximizing this. The general Helleseth–Kløve–Mykkeltveit lower bound and the sphere-covering upper bound sandwich \(\rho(1,n)\), and for \(n=9\) they leave exactly the gap \(\{242,244\}\) after the constructive improvements below.

**Facts fixing the regime.** For **even** \(n\), \(N_{\max}(n)=2^{n-1}-2^{n/2-1}\), attained exactly by **bent** functions (those with \(|W_f(w)|=2^{n/2}\) for all \(w\)). For **odd** \(n\), the **bent-concatenation lower bound** is \(N_{\max}(n)\ge 2^{n-1}-2^{(n-1)/2}\); the general upper bound is \(N_{\max}(n)\le 2^{n-1}-2^{(n-1)/2}\) *only* for \(n\le 7\) (where it is tight), and for \(n\ge 9\) it can be exceeded. Every attainable nonlinearity is an even integer.

The exactly known values of \(N_{\max}(n)\) (equivalently \(\rho(1,n)\)) for small odd \(n\) are
\[
N_{\max}(1)=0,\quad N_{\max}(3)=2,\quad N_{\max}(5)=12,\quad N_{\max}(7)=56,
\]
each equal to the bent-concatenation value \(2^{n-1}-2^{(n-1)/2}\); the first \(n\) where that value is *not* known to be optimal is \(n=9\), and the first where it is provably *not* optimal is \(n=15\).

**The question, adopted scope.** Determine \(N_{\max}(9)=\rho(1,9)\). The bent-concatenation value at \(n=9\) is \(2^8-2^4=240\); the record lower bound is \(\mathbf{242}\), and the covering radius is known to lie in \(\{242,244\}\). Cost is measured in exactly verified nonlinearities (Walsh spectra) for lower bounds, and in DRAT/LRAT-certified UNSAT (or an exact LP/SDP/parity argument) for any upper-bound improvement.

## 2. Resolution standard

A **full resolution** for \(n=9\) is a proof that \(N_{\max}(9)=v\) for a specific even \(v\in\{242,244\}\), consisting of:

- a **lower bound** \(N_{\max}(9)\ge v\): an explicit \(512\)-bit truth table \(f\) with a recomputed full Walsh spectrum showing \(\max_w|W_f(w)|=2^9-2v\), hence \(\mathrm{nl}(f)=v\); and
- a **matching upper bound** \(N_{\max}(9)\le v\): a machine-checkable proof that no \(9\)-variable function has nonlinearity \(>v\) - a DRAT/LRAT UNSAT certificate for the SAT encoding of "\(\exists f:\ \mathrm{nl}(f)\ge v+2\)", or an exact combinatorial/LP argument on the Walsh spectrum with rational certificate.

Named certified forms:

- **(a) Explicit construction** with a recomputed full Walsh spectrum (lower bounds).
- **(b) SAT-with-DRAT** for existence/nonexistence of a function of given nonlinearity, possibly within a symmetry class whose orbit structure is certified.
- **(c) Exhaustive/canonical enumeration** of a symmetry-restricted class (rotation-symmetric, idempotent, or bent-concatenation-plus-perturbation), with completeness certified via nauty/orbit counting.
- **(d) Exact LP/spectral certificate:** a rational feasibility/infeasibility certificate over the Walsh coefficients that bounds \(N_{\max}(9)\) from above.

A one-sided result - a certified new lower bound, or a certified upper bound over a delimited degree/symmetry class - is a legitimate reportable increment and must be labelled as such, never as the determined value \(N_{\max}(9)\).

**Not accepted as resolution.**

- A construction achieving \(242\) (or more) with **no** matching upper-bound argument - that improves the record lower bound (a genuine partial result, P-level) but does not determine \(N_{\max}(9)\).
- An upper-bound claim from an unreplayable solver run, or from a numerical SDP without an exact rational certificate.
- A function reported at nonlinearity \(v\) whose Walsh spectrum is not recomputed by an independent transform.
- A result inside a symmetry class ("best rotation-symmetric \(9\)-variable function has \(\mathrm{nl}=v\)") presented as the *global* maximum, unless the restriction is proved lossless.
- Asymptotic statements about \(\rho(1,n)\) growth in place of the exact \(n=9\) value.
- Confusing \(\rho(1,9)\) with the covering radius of higher-order Reed–Muller codes (e.g. \(\mathrm{RM}(2,n)\)) or with related but distinct records.
- A nonlinearity value between \(242\) and \(244\) reported without checking it against the spectrum-divisibility constraints (an "impossible" value indicates a bug).
- A heuristic-search optimum quoted without the exact truth table archived and re-evaluated.
- A bound derived only for balanced functions but reported as a bound on the unrestricted \(N_{\max}(9)\) (or vice versa) - the two records differ.
- A claim that \(N_{\max}(9)=242\) on the strength of "no known construction beats it" - absence of a construction is not an upper-bound proof.

## 3. Graded partial-result targets

**P1 - Reproduce the frontier.** Independently recompute, via a verified fast Walsh–Hadamard transform, the nonlinearity of published \(n=9\) record functions: the \(\mathrm{nl}=241\) rotation-symmetric functions (Kavut–Maitra–Yücel) and the \(\mathrm{nl}=242\) functions (Kavut–Yücel), confirming they beat the bent-concatenation bound \(240\). *Certificate:* recomputed full Walsh spectra with SHA-256 over the truth tables and outputs.

**P2 - Certified small-\(n\) calibration.** Reconfirm \(N_{\max}(n)\) for \(n\le 7\) end-to-end with the pipeline: exhaustive/orbit enumeration for the lower bounds and a DRAT-certified upper bound at \(n=7\) (\(N_{\max}(7)=56\)). This validates that the SAT-upper-bound encoding is sound before it is trusted at \(n=9\), where its verdict is not independently known. *Certificate:* enumeration replays and a replayed DRAT/LRAT proof, matching the values \(N_{\max}(3)=2\), \(N_{\max}(5)=12\), \(N_{\max}(7)=56\).

**P3 - Symmetry-class exhaustion.** Perform a certified, isomorph-free exhaustive search over a well-defined symmetry class at \(n=9\) - rotation-symmetric Boolean functions (RSBFs), the \(k\)-rotation-symmetric or idempotent classes - reporting the exact maximum nonlinearity attained in that class and whether \(242\) is exceeded. A certified within-class maximum (even if it equals \(242\)) is a genuine result: it pins the best that a whole structured family can do. *Certificate:* orbit-enumeration completeness (nauty/cyclic-group orbit counts) plus recomputed spectra of the optima.

**P4 - Improve the lower bound.** Exhibit a \(9\)-variable function with \(\mathrm{nl}=244\) (which would close the interval from below and force \(N_{\max}(9)=244\)), or certify that \(244\) is unattainable in the searched class. *Method:* idempotent/RSBF search seeded from the \(242\)-functions, with local perturbation and exact re-evaluation. *Certificate:* recomputed Walsh spectrum, or a class-restricted DRAT UNSAT.

**P5 - Improve the upper bound.** Produce a machine-checkable proof that \(N_{\max}(9)\le 242\) (which, with P1, would resolve \(N_{\max}(9)=242\)): a DRAT/LRAT UNSAT certificate for "\(\exists f:\mathrm{nl}(f)\ge 244\)", or an exact spectral/LP argument. This is the hard direction - the unrestricted instance is at the edge of one-workstation feasibility, so a *partial* upper bound (e.g. "no function of degree \(\le d\) reaches \(244\)") is itself a reportable increment. *Certificate:* the CNF, solver version, and replayed proof, or an exact rational LP certificate.

**P6 - Full resolution.** \(N_{\max}(9)=v\) with matched, independently checked lower and upper bounds. Optionally, transfer the toolchain toward \(n=11\) with any certified bound improvement.

**P7 - Reproduce Patterson–Wiedemann at \(n=15\).** As a stress test and a source of structural intuition, independently reconstruct a Patterson–Wiedemann-type \(n=15\) function exceeding the bent-concatenation bound and recompute its nonlinearity exactly. *Certificate:* recomputed Walsh spectrum over \(2^{15}\) points with SHA-256, matching the published record value. (This is a reproduction, not a new result, and is labelled as such.)

## 4. Known results and prior art

- **Covering-radius framing:** \(N_{\max}(n)=\rho(1,n)\), the covering radius of the first-order Reed–Muller code; the small exact values and the general bounds are catalogued in the covering-codes literature (Cohen–Honkala–Litsyn–Lobstein, ~1997) (verify).
- **Even \(n\):** \(N_{\max}(n)=2^{n-1}-2^{n/2-1}\), bent (Rothaus, ~1976).
- **Odd \(n\le 7\):** \(N_{\max}=2^{n-1}-2^{(n-1)/2}\), tight; \(N_{\max}(7)=56\). The tightness at \(n\le 7\) was established via covering-radius work on \(\mathrm{RM}(1,n)\) (Helleseth, Kløve, Mykkeltveit and others, ~1970s–1980s) (verify).
- **\(n=9\), lower bound history:** bent-concatenation \(240\) → \(241\) (Kavut–Maitra–Yücel, ~2006) → \(242\) (Kavut–Yücel, ~2007) - each step a certified explicit function, none yet matched by an upper bound below \(244\) (verify).
- **\(n=15\):** Patterson and Wiedemann (~1983) constructed functions of nonlinearity \(16276>16256=2^{14}-2^7\), the first exceedance of the bent-concatenation bound, using idempotent/cyclic-orbit structure over \(\mathbb{F}_{2^{15}}\) (verify exact value). This showed the bent-concatenation bound is not tight for odd \(n\) in general, and reframed \(n=9,11,13\) as genuinely open rather than "obviously \(240,\dots\)".
- **\(n=9\):** bent-concatenation bound \(240\). Kavut, Maitra and Yücel (~2006) found rotation-symmetric functions with \(\mathrm{nl}=241>240\); Kavut and Yücel (~2007, journal ~2010) improved to \(\mathrm{nl}=242\) in a generalized rotation-symmetric class. The covering radius \(\rho(1,9)\) is thereby pinned to \(\{242,244\}\); the upper bound \(244\) is the standard one for \(\rho(1,9)\) (verify against current sources). The exact value remains **open**.
- **Improvements at \(n=15\):** the Patterson–Wiedemann value was revisited and the surrounding covering-radius bounds tightened by later authors (Kavut–Yücel, and others), and the \(n=13\) landscape studied similarly (verify current records and any exact resolutions).
- **\(n=11,13\):** likewise open, with record lower bounds above the bent-concatenation value from rotation-symmetric / heuristic search (verify current records).
- **Divisibility / parity constraints:** attainable nonlinearities of \(n\)-variable functions are constrained by divisibility results on the Walsh spectrum (McEliece-type \(2\)-divisibility, and refinements for low-degree functions), which limit which values between \(242\) and \(244\) are even possible (verify).
- **Methods:** rotation-symmetric Boolean functions and steepest-descent/annealing search (Maitra, Kavut, Yücel, Sarkar; ~2006–2011); idempotents over \(\mathbb{F}_{2^n}\); algebraic constructions extending Patterson–Wiedemann; the general theory of the covering radius of \(\mathrm{RM}(1,n)\) (Helleseth–Kløve–Mykkeltveit; Cohen–Honkala–Litsyn–Lobstein covering-codes monograph) (verify).

- **Search technology:** the record functions were found by steepest-descent and simulated-annealing over rotation-symmetric and generalized-RSBF classes; the wins came from *shrinking the space by symmetry*, not from raw solver power - the lesson to carry into any new attempt (verify).
- **Balanced variant:** for cryptographic use one often wants the maximum nonlinearity among *balanced* \(9\)-variable functions, which is a separate (also open) record slightly below the unrestricted \(N_{\max}(9)\) - keep the two questions distinct (verify current balanced record).
- **Community resources:** the "Boolean functions" wiki and the covering-codes / covering-radius tables in the Cohen–Honkala–Litsyn–Lobstein monograph are the standard cross-checks; use them for ground truth, not as the trusted base (verify).

**Web-verify the headline record tables** - the odd-\(n\) nonlinearity records and the \(\rho(1,9)\in\{242,244\}\) status are exactly the kind of figure that moves; consult the Boolean-functions community record pages and recent journals. **Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

`[search]` `[opt]` first computations on one workstation:

1. **Verified transform (P1–P2).** Implement a fast Walsh–Hadamard transform in **SageMath** and, independently, in **custom C++ for Boolean-function search**; agreement on every spectrum is the primary integrity gate. Nonlinearity of a length-\(512\) function is microseconds; the bottleneck is the number of candidates, not evaluation.
2. **Symmetry reduction (P3).** Restrict to rotation-symmetric functions: representatives are indexed by orbits of the cyclic group \(\langle x\mapsto x\ll 1\rangle\) on \(\mathbb{F}_2^n\); the number of RSBF variables is the number of such orbits (far smaller than \(2^n\)). Enumerate orbit representatives with **GAP**/**nauty** orbit counting so class completeness is certificate-backed, then sweep with the fast transform. Extend to idempotent constructions over \(\mathbb{F}_{2^9}\).
3. **Bound optimization (P4).** Cast "maximize \(\mathrm{nl}\) in class \(C\)" as combinatorial optimization; use steepest-descent / simulated annealing over the class as an *explorer* (any hit is then exactly verified), and an exact ILP/LP relaxation on the Walsh spectrum (SCIP with exact certificates, QSopt_ex/SoPlex) to bound how high the class can reach.
4. **SAT upper bounds (P5).** Encode "\(\exists f\in\mathcal{B}_9:\ \forall w,\ |W_f(w)|\le 2^9-2(v+2)\)" - a constraint over the \(512\) truth-table bits with linear Walsh-coefficient bounds (via sequential-counter / totalizer encodings) - and run **CaDiCaL**/**kissat**/**CryptoMiniSat** with proof logging; replay UNSAT with `drat-trim`/`lrat-check`. The full unrestricted instance is very hard; begin with symmetry-restricted or partially-fixed encodings and report exactly what was decided.
5. **Idempotent / trace search (P4).** Work inside the idempotent subspace of \(\mathcal{B}_9\) (functions fixed by \(x\mapsto x^2\) over \(\mathbb{F}_{2^9}\)), the setting of Patterson–Wiedemann; enumerate cyclic-orbit-constant functions and evaluate nonlinearity via the transform, which is where \(242\) and any push toward \(244\) most plausibly live.
6. **Divisibility filter.** Precompute which nonlinearity values in \([242,244]\) are admissible under the spectrum-divisibility constraints for the degree range being searched, and use it to prune both the search and the upper-bound target.
7. **Structure mining.** Tabulate Walsh spectra and autocorrelation of the record functions; look for algebraic regularities (trace/idempotent forms) that generalize to \(n=11,13\), and hand any clean pattern to a certified re-derivation.
8. **Cross-check against covering-code tables.** Reconcile every reproduced value with the covering-radius tables for \(\mathrm{RM}(1,n)\); a discrepancy is a bug in the transform or the bit ordering, caught before any new claim is made.

Complementary encodings worth trying in parallel, each with its own certificate:

- **Truth-table encoding:** \(2^n\) Boolean variables, Walsh coefficients as linear pseudo-Boolean constraints via totalizer/sequential-counter encodings; general but heavy.
- **ANF (degree-bounded) encoding:** variables are the ANF coefficients up to a degree cap \(d\); shrinks the space dramatically and exploits that near-optimal odd-\(n\) functions have moderate degree.
- **Orbit-variable encoding:** for a symmetry class, one variable per orbit; the smallest instances, at the cost of a certified losslessness argument.
- **Fixed-partial encoding:** freeze a bent sub-block and search the perturbation, targeting the concatenation gap directly.

**One-workstation scope and failure modes.** Evaluation is free; the enemy is combinatorial explosion.

- *Unrestricted search is hopeless* - \(2^{512}\) functions; only symmetry restriction or SAT makes the space finite-in-practice, and any *global* claim must then justify losslessness.
- *Solver blow-up:* the unrestricted upper-bound SAT instance may not close on one workstation - scope honestly to what the DRAT proof actually covers.
- *SDP illusions:* a floating-point LP/SDP upper bound is exploratory only until converted to an exact rational certificate; a "244 is impossible" claim without exact arithmetic is void.
- *Class-vs-global confusion:* the maximum within RSBFs is not the global maximum unless proven so.
- *Orbit-count bugs:* a miscounted symmetry orbit silently drops candidates - cross-check counts two ways.
- *Bit-ordering drift:* a mismatched variable-to-bit convention between the two transforms fakes agreement or fakes a discrepancy - fix and document one convention up front.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every nonlinearity is an exact integer from a recomputed Walsh–Hadamard transform; every upper bound is a DRAT/LRAT UNSAT proof or an exact rational LP/spectral certificate. Floating-point annealing/SDP is exploration only - every reported optimum is re-verified exactly.
2. **Independent verification.** Two independently written Walsh transforms (e.g. SageMath and C++) must agree on every load-bearing spectrum; every DRAT/LRAT proof is replayed by a separate checker; every symmetry-class orbit count is recomputed by a second method (nauty vs. hand-rolled cyclic enumeration). A record-matching value that only one implementation produces is treated as unconfirmed until the second agrees.
3. **Reproducibility.** Record the variable/bit ordering, symmetry-class definition, all encodings, solver/SageMath/GAP/nauty versions, seeds, and a SHA-256 manifest over every truth table, Walsh spectrum, CNF, and proof. Cite the exact record lower bound being matched or beaten (value, authors, source, access date). Archive the full \(512\)-bit truth table of every record-level function, not just its nonlinearity, so the claim is independently re-checkable forever.
4. **Preservation.** All search, enumeration, and encoding source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson). The annealing/steepest-descent drivers count as source even though their output is re-verified exactly.
5. **Honest reporting.** The report states up front whether \(N_{\max}(9)\) was *determined* (matched bounds) or only a *lower bound improved* / *upper bound improved*, and in exactly which class any restricted claim holds. A heuristic optimum, an unverified spectrum, or a within-class maximum is never represented as the global covering radius \(\rho(1,9)\).

Calibration for the session lead: the realistic product is P1–P3 - a validated transform, a reproduced record, and a certified within-class maximum - plus, with luck, a lower-bound improvement (P4) or a class-restricted upper bound (P5). Determining \(N_{\max}(9)\) outright (P6) requires *both* an explicit \(244\)-function and a machine-checked "\(\ge 244\) impossible" (or matched \(242\) bounds), a substantial result; do not overstate a one-sided bound as the covering radius. The same toolchain, once trusted, is the natural launch point for \(n=11,13\).
