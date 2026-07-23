# PROMPT FOR A SMALLER GARDEN OF EDEN OR A CERTIFIED-MINIMAL ORPHAN

## The smallest predecessor-free configuration in Conway's Life, via SAT with DRAT nonexistence proofs

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 33 of 50  
**Area:** discrete dynamics & pattern search  
**Modes:** `[search]` `[enum]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A *Garden of Eden* in Conway's Life (\(\mathrm{B3/S23}\) on \(\mathbb Z^2\)) is a configuration with no predecessor: no state maps to it under the Life transition. The finite witness of this is an **orphan** - a finite patch of specified cells that cannot be the image of any assignment to its neighbourhood. Existence is classical (the Moore–Myhill Garden-of-Eden theorem, ~1962–63). The living frontier is *minimisation*: the smallest orphan by bounding box and by cell count, pushed by SAT-based predecessor search, whose records have shrunk repeatedly. The problem is exactly matched to certified search because "\(P\) has no predecessor" is a single SAT instance over the neighbourhood, and its unsatisfiability is a DRAT/LRAT-checkable proof; minimality is an exhaustive or SAT argument over a bounded box. The on-machine verifier that closes the loop is a SAT solver with an independently checked UNSAT proof, plus (for minimality) an exhaustive enumeration. Anything short of Section 2 - a "probable" orphan, an unchecked solver run, a record without a sourced baseline - is a partial result, never a solution.

## 1. Exact problem statement

**The rule and predecessors.** With \(n(c,x)\) the live Moore-neighbour count, the Life map is

\[
(Tc)(x)=\mathbf 1\!\left[\,n(c,x)=3\ \lor\ \bigl(c(x)=1\land n(c,x)=2\bigr)\,\right].
\]

A **predecessor** of a target \(g\) is any \(f\) with \(T(f)=g\). Because \(T\) has Moore radius 1, whether a finite target patch \(g\) restricted to a region \(R\) has a predecessor depends only on the assignment to the dilated region

\[
R^{+}=\{\,y : \mathcal N(y)\cap R\ne\varnothing\,\}=R\oplus \mathcal N .
\]

**Orphan.** A finite pattern \(g\) on \(R\) (a fixed on/off specification, exterior unconstrained) is an **orphan** when the Boolean formula over predecessor variables \(f(y),\ y\in R^{+}\),

\[
\Phi_g \;=\; \bigwedge_{x\in R}\Bigl[\ \mathrm{Life}\bigl(f;x\bigr)=g(x)\ \Bigr],
\]

is **unsatisfiable**. Here each conjunct is the totalistic constraint, for \(s=\sum_{y\in\mathcal N(x)} f(y)\),

\[
\mathrm{Life}(f;x)=g(x)\ \Longleftrightarrow\
\begin{cases}
s=3\ \lor\ (f(x)=1\land s=2) & \text{if } g(x)=1,\\
s\notin\{3\}\ \land\ \lnot(f(x)=1\land s=2) & \text{if } g(x)=0,
\end{cases}
\]

which is encoded to CNF with a cardinality/sorting-network sub-circuit on the eight neighbours. An orphan certifies that every configuration (finite or infinite) containing \(g\) is a Garden of Eden, because the no-predecessor property is local to \(R^{+}\) and unaffected by the exterior.

**Size measures.** Two must be distinguished and reported separately:

\[
\#\mathrm{spec}(g)=\bigl|\{x\in R: g(x)\ \text{constrained}\}\bigr|,
\qquad
\#\mathrm{live}(g)=\bigl|\{x\in R: g(x)=1\}\bigr|,
\qquad
\mathrm{box}(g)=\text{area of the bounding rectangle of } R .
\]

An orphan may leave many interior cells as don't-cares, so \(\#\mathrm{spec}\) and \(\#\mathrm{live}\) genuinely differ; a "cell count" record is meaningless without saying which.

**Orphan vs Garden of Eden.** A *Garden of Eden* is any (possibly infinite) unreachable configuration; an *orphan* is a finite certificate of one. Every Garden of Eden contains an orphan, and every superpattern of an orphan is a Garden of Eden, so the extremal question is entirely about finite orphans. Minimising over orphans is well-posed because, for a fixed box, there are finitely many specifications:

\[
\bigl|\{\text{on/off/dc specifications on } R\}\bigr| = 3^{|R|},
\]

each testable by a single SAT call, so \(\mathrm{minbox}\) and the minimal cell counts are computable in principle and the task is to push the box and the counts down with certificates.

**The open question.** Determine, or improve the bounds on, the minimal orphan by cell count and by bounding box: exhibit a smaller orphan than the record, or prove a given orphan minimal within a stated box via exhaustive/SAT search. Both directions are finite and decidable.

## 2. Resolution standard

Produce a **certified orphan** and, for a minimality claim, a **certified-minimality artifact**.

- **Orphan certificate.** An explicit pattern \(g\) on region \(R\) (RLE plus an explicit on/off/don't-care map) and a **DRAT/LRAT-checked UNSAT proof** of \(\Phi_g\), establishing that \(g\) has no predecessor. Report \(\#\mathrm{spec}\), \(\#\mathrm{live}\), and \(\mathrm{box}\).
- **Record form.** The orphan is strictly smaller than the standing record in the stated measure, i.e.

\[
\mu(g) < \mu_{\mathrm{record}} \quad\text{for } \mu\in\{\#\mathrm{spec},\ \#\mathrm{live},\ \mathrm{box}\},
\]

cited by value, source, and access date.
- **Minimality form.** A certified statement that no orphan exists below a stated size in a stated window - an exhaustive isomorph-free enumeration, or a SAT proof (with DRAT/LRAT) of the correct quantifier order

\[
\forall\, g'\ \text{in the window with (measure)} < m:\quad \Phi_{g'}\ \text{is satisfiable (a predecessor exists),}
\]

so the exhibited orphan of measure \(m\) is minimal there.

**Not accepted as resolution.**

- A "probable" or solver-only orphan whose \(\Phi_g\)-UNSAT is asserted without an independently checked DRAT/LRAT proof.
- Confusing measures: a bounding-box record reported as a cell-count record, or \(\#\mathrm{live}\) conflated with \(\#\mathrm{spec}\).
- A minimality claim without a completed exhaustive enumeration or a SAT proof of the correct \(\forall\exists\) statement over the whole window - one satisfying predecessor for one nearby pattern proves nothing about minimality.
- A pattern claimed to be an orphan but whose don't-care/boundary handling is wrong, so a predecessor actually exists just outside \(R\).
- An "orphan" that is really only a Garden-of-Eden *density* or symmetry claim with no explicit finite unsatisfiable patch.
- An orphan whose UNSAT holds only for the exact region \(R^{+}\) but fails when the predecessor region is enlarged by one ring - a boundary artifact rather than a true orphan (see the boundary audit in Section 5).
- Any result whose SAT instance or enumeration cannot be regenerated deterministically from the recorded encoding and solver version.

## 3. Graded partial-result targets

- **P1 - Encoding reproduction.** Build the predecessor-SAT encoding and reproduce a *known* orphan: recover its UNSAT with a checked DRAT/LRAT proof. *Certificate:* the encoding, the UNSAT trace, and a standalone checker log; \(\#\mathrm{spec}\), \(\#\mathrm{live}\), \(\mathrm{box}\) tabulated.
- **P2 - Record-table reproduction.** Reproduce the standing smallest-known orphan by bounding box and by cell count. *Certificate:* certified orphans plus a sourced record table with access dates.
- **P3 - Small-box existence census.** For a fixed small box \(B\), determine whether an orphan exists at all, and if so

\[
m^{*}(B)=\min\{\#\mathrm{spec}(g): R\subseteq B,\ \Phi_g\ \text{UNSAT}\},
\]

by exhaustive enumeration or an optimising SAT sweep. *Certificate:* enumeration log or SAT proof, with checked traces.
- **P4 - New size record.** Exhibit an orphan strictly smaller than the record in bounding box or cell count. *Certificate:* orphan certificate (checked UNSAT) plus sourced record comparison.
- **P5 - Certified local minimality.** Prove a given orphan minimal within a stated box/cell-count window: no smaller orphan exists there. *Certificate:* exhaustive isomorph-free enumeration or a DRAT/LRAT-backed \(\forall\exists\) SAT proof over the window.
- **P6 - Symmetry-restricted optima.** Certified smallest orphan under a declared symmetry (as in symmetry-focused Garden-of-Eden searches). *Certificate:* the machine-checkable symmetry predicate plus the minimality artifact.
- **P7 - Low-height frontier.** Push the minimal *height* at which orphans exist (Eker's height-5 result opened this), or certify the minimum cell count at a fixed small height. *Certificate:* orphan certificate at the stated height plus, for a minimality claim, an enumeration/UNSAT over the height-restricted window.

## 4. Known results and prior art

- **Existence (classical).** The Garden-of-Eden theorem: a cellular automaton has a Garden of Eden iff it is not injective on finite configurations ("twins"). Edward F. Moore (1962) proved existence for Life-type CA; John Myhill (1963) proved the converse - hence *Moore–Myhill*. Life has Gardens of Eden.
- **First explicit orphans.** Early explicit Life Gardens of Eden were large (hundreds of cells) found by hand and by the early Life groups (J. Hardouin-Duparc and others, ~1970s, verify); records then shrank steadily.
- **SAT-era records.** SAT-based predecessor search drove the modern records. "Symmetry in Gardens of Eden" (Christiaan Hartman, Marijn Heule, and collaborators, Electronic Journal of Combinatorics, 2013, verify exact authorship and the volume v20i3p16) reported an orphan with a \(10\times10\) bounding box and on the order of ninety-odd specified cells. Steven Eker (2016) found height-5 orphans (a \(5\times83\) bounding box, ~96 live cells in a \(5\times45\) region), notable because low-height orphans were long doubted to exist (verify).
- **Recent enumerations.** As of ~2022, exhaustive searches in small boxes (\(10\times10\), \(11\times11\)) turned up many orphans, with the smallest known by live-cell count around the mid-40s (verify the current holder and exact value).
- **Method lineage.** Incremental / assumption-based SAT (checking many candidate patches per second), symmetry reductions, and DRAT proof logging are the standard machinery; solvers such as CaDiCaL / kissat / CryptoMiniSat with `drat-trim` / `lrat-check` close the loop.
- **Two independent records.** The smallest orphan by bounding box and the smallest by cell count are held by different objects and have moved on different timelines; a session must state which record it is contesting and never present an improvement in one metric as an improvement in the other.
- **Reachability context.** The density of Gardens of Eden (fraction of configurations that are unreachable) grows with region size; this is context, not a substitute for an explicit finite orphan, which is the only accepted witness here.

Never cite a discoverer, date, record value, or bounding box you have not re-checked; the "(verify)" markers above are exactly the items to confirm. Life records move fast - web-verify every claim and record value. **Status as of mid-2026 - re-verify against the current literature and record trackers (LifeWiki, the ConwayLife forums, and the SAT-Life literature) before starting any session.**

## 5. Attack plan

`[search]` `[enum]` - concrete first computations on one workstation.

1. **Predecessor encoding.** Encode \(\Phi_g\) over the dilated region \(R^{+}\), with careful boundary/don't-care semantics: cells in \(R\) are constrained to \(g\); the predecessor lives on \(R^{+}\); the exterior is unconstrained. Get the boundary right - most false orphans are boundary bugs.
2. **Search direction.** To *find* a smaller orphan, search over candidate patches - fix a box, minimise the target measure - and test each for UNSAT,

\[
\text{orphan found} \iff \exists\, g\ \text{in box with}\ \Phi_g\ \text{UNSAT and } \mu(g)\ \text{below the target,}
\]

using assumption-based/incremental SAT (CaDiCaL, CryptoMiniSat) to reuse solver state across candidates.
3. **Proof logging.** For every claimed orphan, produce and check a DRAT/LRAT UNSAT proof (`drat-trim`, `lrat-check`); an unchecked UNSAT is not a result.
4. **Minimality.** For P5, either exhaustively enumerate all patches below the target size in the box (with isomorph rejection under the box's symmetry group), SAT-testing each, or encode the \(\forall\exists\) "every smaller patch has a predecessor" statement and certify it.
5. **Symmetry.** Add symmetry constraints (as in the symmetry-focused searches) to shrink the search and target P6; each symmetry reduction must have a proof it preserves all cases.
6. **Boundary audit.** Before trusting any UNSAT, re-test the same \(g\) with the predecessor region enlarged by one ring; if the enlarged instance becomes satisfiable, the original "orphan" was a boundary artifact. Only patches that stay UNSAT under enlargement are reported.

One-workstation scope: single-patch UNSAT proofs and small-box enumerations are feasible; full minimality over large boxes is the hard part - bound and report the window. **Failure modes:** boundary/don't-care mis-encoding (spurious orphans); measure confusion (\(\#\mathrm{spec}\) vs \(\#\mathrm{live}\); box vs count); unverified UNSAT; enumeration non-canonicity (double counting or gaps); SAT blow-up as the box grows.

## 6. Verification and auditability requirements

1. **Exact/certified computation.** Every orphan claim rests on a DRAT/LRAT-checked UNSAT proof; every minimality claim on a completed enumeration or a checked \(\forall\exists\) proof. Solver output alone is never load-bearing; floating point plays no role.
2. **Independent verification.** Each UNSAT proof is checked by a standalone checker written separately from the search (`drat-trim` / `lrat-check`), and for headline orphans re-derived with a second solver; each enumeration is replayed by an independent generator.
3. **Reproducibility.** The full encoding (region \(R\), dilation \(R^{+}\), boundary semantics), solver and checker versions, seeds, and the measure conventions (\(\#\mathrm{spec}\), \(\#\mathrm{live}\), box) are recorded; SHA-256 manifest over every artifact; each record being beaten is cited with source and access date.
4. **Preservation.** Encoder, search, and enumeration source plus all proof traces are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting.** The report states up front whether a strict size record, a certified local minimality, or only an encoding reproduction was achieved, and in which measure. A probable orphan, an unchecked UNSAT, or a measure-confused "record" is never represented as a certified result.
