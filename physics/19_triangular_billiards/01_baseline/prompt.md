# PROMPT FOR THE EXISTENCE OF A PERIODIC ORBIT IN EVERY TRIANGULAR BILLIARD

## The obtuse-triangle periodic-orbit problem and the certified angle-space frontier

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 19 of 50 (Tier 2)
**Source:** top-50 list #36, category E (dynamical systems and classical mechanics)
**Modes:** `[cert]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Does every triangle admit a periodic billiard trajectory? The question is elementary to state, is classical (the acute case is Fagnano's orbit, 1775), and is open precisely for irrational obtuse triangles with largest angle beyond the current certified frontier (approximately $112.3^\circ$; verify). It matters as the simplest hard instance of polygonal billiard dynamics and as a model problem for certified computation over parameter space: existence on an open set of triangles is witnessed by a finite combinatorial word plus a finite set of trigonometric inequalities, checkable by interval arithmetic - exactly the `[cert]`+`[search]` modes. The complete resolution defined in section 2 is the target; the realistic session product is the graded ladder of section 3, centered on rebuilding a verified unfolding-search pipeline and extending the certified region of angle space by positive measure. Anything less than section 2 must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Billiards and periodic orbits

Let $T \subset \mathbb{R}^2$ be a compact triangle with interior angles $\alpha \le \beta \le \gamma$, $\alpha + \beta + \gamma = \pi$. The billiard flow moves a point at unit speed along straight segments in $T$, reflecting off the open edges by specular reflection; the flow is undefined at the three vertices. A **periodic orbit** is a closed billiard trajectory with finitely many reflection points, none at a vertex.

Parameterize triangle shapes, up to similarity, by the open shape simplex

\[
\mathcal{T} \;=\; \{(\alpha,\beta) \in \mathbb{R}_{>0}^2 : \alpha \le \beta \le \pi - \alpha - \beta \}.
\]

A triangle is **rational** if $\alpha, \beta \in \pi\mathbb{Q}$, and **obtuse** if $\gamma = \pi - \alpha - \beta > \pi/2$.

**Adopted question.** *Does every $(\alpha,\beta) \in \mathcal{T}$ admit at least one periodic billiard orbit?*

Known affirmative territory:

- all acute triangles (Fagnano's orthic orbit, 1775);
- all right triangles (explicit constructions; the orbits are unstable in the sense of 1.2);
- all rational triangles (translation-surface theory);
- all obtuse triangles with $\gamma$ up to the certified frontier: $100^\circ$ (Schwartz 2009), extended to $\approx 112.3^\circ$ (Tokarsky–Garber–Marinov–Moore, ~2018 - verify the current value).

Open: irrational obtuse triangles with $\gamma$ beyond the frontier. No informal surrogate ("almost every triangle", "all triangles tested") is an acceptable target.

### 1.2 Unfolding formalism (the certification substrate)

Label the edges $1,2,3$. For a word $w = w_1 w_2 \cdots w_{2k}$ over $\{1,2,3\}$ with $w_i \ne w_{i+1}$ (indices cyclic), define the unfolding: $T_0 = T$ placed in the plane, and $T_i$ the reflection of $T_{i-1}$ across the edge of $T_{i-1}$ labeled $w_i$. Let $g_w$ be the composed isometry taking $T_0$ to $T_{2k}$ and $H(w) \in \mathrm{O}(2)$ its linear part. Since every edge line of every $T_i$ makes an angle in $\mathbb{Z}\alpha + \mathbb{Z}\beta + \mathbb{Z}\pi$ with the horizontal, the rotation angle of $H(w)$ has the form

\[
\theta_w(\alpha, \beta) \;=\; 2(a\alpha + b\beta) \bmod 2\pi, \qquad a, b \in \mathbb{Z} \ \text{determined combinatorially by } w .
\]

- $w$ is a **translation word** at $(\alpha,\beta)$ if $H(w) = \mathrm{Id}$, so $g_w$ is a translation by some $V(w) \ne 0$.
- A periodic orbit with reflection sequence $w$ exists at $(\alpha,\beta)$ iff $w$ is a translation word and there is a segment $S$ from a point $p$ to $p + V(w)$ crossing, in order and through their interiors, the common edges $T_0 \cap T_1,\ T_1 \cap T_2,\ \dots,\ T_{2k-1} \cap T_{2k}$. This **corridor condition** is a finite conjunction of strict linear inequalities in the unfolded vertex coordinates, which are finite trigonometric expressions in $\alpha, \beta$.
- $w$ is **stable** if its rotation form vanishes identically ($a = b = 0$), so $H(w) = \mathrm{Id}$ for *all* $(\alpha,\beta)$. For stable $w$, the **orbit tile** $O(w) \subset \mathcal{T}$ is the open set where the corridor condition holds: existence on $O(w)$ is witnessed by finitely many strict inequalities - the natural object of interval certification.
- Unstable translation words exist only on the codimension-one set $\{a\alpha + b\beta \in \pi\mathbb{Z}\}$. Right triangles carry only unstable periodic words (Hooper), which is why *pointwise* coverage - not merely full-measure coverage - is the standard adopted here.

## 2. Complete-resolution standard

Either of:

1. **Affirmative.** A proof that every triangle in $\mathcal{T}$ has a periodic billiard orbit. If the proof is a tiling of $\mathcal{T}$ by orbit tiles, it must:
   - exhibit an explicit (finite, or explicitly enumerated infinite) family of stable words whose tiles cover every irrational obtuse shape point;
   - handle the unstable loci (right, isosceles, and rational-degenerate lines) by separate proof;
   - be pointwise: every single $(\alpha,\beta)$ is covered by a proved tile or a proved special case, with all tile claims certified per section 6.
2. **Negative.** An explicit triangle $(\alpha,\beta)$ together with a proof that it admits *no* periodic orbit. This requires excluding every word and hence genuinely new theory; no such mechanism is currently known.

**Not accepted as resolution**

- Numerically found orbits (floating point) without interval or exact-arithmetic certificates, for any triangle.
- Coverage of $\mathcal{T}$ up to a set of measure zero, or "almost every triangle", represented as the full statement - the open problem lives exactly at the uncovered points.
- Frontier claims ("all $\gamma \le \Gamma$") without machine-checkable tile certificates covering the closed region claimed, including tile-boundary bookkeeping in exact arithmetic.
- Tiles certified only at sample points of a grid rather than uniformly over boxes - sampling is search, not certification.
- Existence of approximate or limit-periodic behavior, orbits in a Hausdorff-limit sense, or orbits through a vertex.
- Results restricted to rational or near-rational triangles (known territory).
- Density statements (immediate from the rational case).

## 3. Graded partial-result targets

- **P1 - Verified unfolding pipeline, reproducing classical tiles.**
  - *Task:* independent implementation of the unfolding, the stability criterion ($(a,b)$ computed exactly from $w$ as integers), and tile certification: for a stable word $w$ and a box $B \subset \mathcal{T}$ with rational endpoints (angles in units of $\pi$), an interval-arithmetic proof with directed rounding that the corridor inequalities hold with strict margin on all of $B$. Deliver a certified Fagnano tile on an explicit acute box plus at least one classical obtuse tile.
  - *Certificate:* $(w, B)$ pairs with per-box interval transcripts, re-checked by a standalone independent checker.
  - *Value:* the toolchain gate; nothing downstream is claimable without it.
- **P2 - Reproduce a published tile region.**
  - *Task:* re-certify, with our own pipeline and words (re-searched, or taken from published McBilliards/Schwartz data), an explicit sub-rectangle of the Schwartz $\gamma \le 100^\circ$ region.
  - *Certificate:* as P1, plus exact bookkeeping showing the claimed sub-rectangle is fully covered.
  - *Value:* calibrates our search against the known frontier machinery and validates the checker on nontrivial words.
- **P3 - Independent re-certification of the current frontier band.**
  - *Task:* a positive-area subregion with $\gamma$ between $100^\circ$ and the published frontier ($\approx 112.3^\circ$), fully covered by our own certified tiles.
  - *Certificate:* word list, boxes, transcripts, exact coverage union.
  - *Value:* first output with independent audit value - the frontier currently rests on one software lineage.
- **P4 - Extend the certified frontier by positive measure.**
  - *Task:* any new certified tile union covering a positive-area region of $\mathcal{T}$ with $\gamma$ beyond the published frontier, or closing an uncovered pocket below it.
  - *Certificate:* word list, boxes, per-box interval transcripts, plus exact-arithmetic (rational or CGAL-exact) bookkeeping of the covered union and its area.
  - *Value:* every positive extension, however small, is publishable; this is the headline target of the prompt.
- **P5 - Structural theorems on stable orbit words.**
  - *Task:* proved statements organizing the tile zoo: explicit infinite families of stable words whose tiles accumulate on a specified boundary segment or limit line (in the spirit of Schwartz–Hooper near-isosceles analyses); certified coverage of an entire one-parameter family of shapes; or proved bounds on the minimal orbit word length as $\gamma$ approaches frontier values (empirically, required word lengths grow sharply - a theorem here would explain the difficulty).
  - *Certificate:* complete proofs; any parameterized interval computations to the P1 standard.
  - *Value:* converts the search from enumeration to structure; the plausible route to any future full resolution.
- **P6 - Coverage program for a new angle bound.**
  - *Task:* a theorem scheme reducing "every triangle with $\gamma \le \Gamma$ has a periodic orbit" to a finite certified tile set plus proofs for the unstable loci, executed for some $\Gamma$ strictly beyond the current frontier.
  - *Certificate:* the full tile database, exact coverage proof, and the unstable-locus arguments.
  - *Value:* the strongest realistic result short of full resolution.

## 4. Known results and prior art

- Fagnano (1775): the orthic-triangle orbit in every acute triangle.
- Right triangles: periodic orbits by explicit constructions (1990s; attributions include Cipra–Hanson–Kolan ~1995 and the survey literature - verify). Hooper (~2007): periodic billiard paths in right triangles are unstable.
- Rational polygons: Masur (1986) - existence and density of periodic directions on the associated translation surfaces; Boshernitzan–Galperin–Krüger–Troubetzkoy (1998) - density of periodic orbits in rational billiards.
- Vorobets–Galperin–Stepin (1992): survey fixing the unfolding formalism and the stability notion.
- Schwartz (2006): obtuse triangles near the $(2,3,6)$ shape. Schwartz (2009): every obtuse triangle with $\gamma \le 100^\circ$ has a periodic orbit - computer-assisted via McBilliards (with Hooper); the direct template for this prompt.
- Hooper–Schwartz (~2009): billiards in nearly isosceles triangles (perpetual orbit families near the isosceles locus).
- Tokarsky–Garber–Marinov–Moore (~2018): extension of the certified frontier to approximately $112.3^\circ$. Verify: the exact bound, publication status, and whether machine-checkable artifacts are available; also check for any post-2018 extensions. The current frontier value is the single most important fact to re-verify.
- McBilliards (Schwartz–Hooper, mid-2000s): the original search software; check current availability of code and tile data before rebuilding from scratch (verify).
- Specific irrational obtuse families with proved orbits (isosceles subfamilies etc.): scattered results (verify).
- Gutkin (1996, 2003 surveys of polygonal billiards): fix the problem's status and terminology; useful as the canonical statement source (verify editions).
- Negative direction: no published mechanism for proving a given triangle has no periodic orbit.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

1. **`[search]` Word enumeration.** Enumerate even words over $\{1,2,3\}$ without immediate repeats, up to cyclic rotation, reversal, and relabeling; compute the rotation form $(a,b)$ exactly (integer arithmetic) and keep only stable words. Prune by fast floating-point corridor feasibility on a grid of $(\alpha,\beta)$ samples in the target region; a word surviving at a sample becomes a tile candidate there. Priority queue ordered by (word length, float corridor margin).
2. **`[cert]` Tile certification.** For each candidate $(w, B)$: evaluate the unfolded vertex coordinates as interval trigonometric expressions in $(\alpha,\beta) \in B$ - interval $\sin/\cos$ with directed rounding via the kv library, MPFI, or custom C++ with `fesetround` - and verify all corridor inequalities with strictly positive margin; on failure, adaptively bisect $B$; store proven boxes. Work in units of $\pi$ with rational box endpoints so all region bookkeeping is exact.
3. **Coverage bookkeeping.** Maintain the certified union as exact rational rectangle unions (or CGAL exact-kernel polygon booleans); report covered area and the exact uncovered residue. Coverage claims are only as strong as this bookkeeping - it must itself be exact, not floating point.
4. **Structure mining for P5.** Cluster proven words by combinatorial pattern; fit family schemas (e.g., $w_k$ with a syllable repeated $k$ times); prove tile containment for the schema by hand or by symbolic interval computation parameterized by $k$.

**First computations (session day one).**

1. Verify $(a,b) = (0,0)$ for the doubled Fagnano word $123123$ and compute its tile; certify a central sub-box of the acute region.
2. Certify one known obtuse tile (word from published Schwartz data if available, else re-searched) on an explicit rational box.
3. Run the float search at word length $\le 30$ on a coarse grid in the $100^\circ$–$105^\circ$ band; certify the three largest candidate tiles found.
4. Stand up the exact coverage bookkeeping and the independent checker; run the checker on every tile from steps 1–3 and reconcile discrepancies to zero.

**Workstation feasibility.**

- Words to length a few hundred and tile databases of a few GB: single-workstation scale (the Schwartz-era search ran on commodity hardware; modern cores and pruning give real margin).
- Frontier-band certification: words of length $10^2$–$10^3$ and deep subdivision; days-to-weeks per band, embarrassingly parallel over boxes.

**Expected failure modes.**

- Sliver tiles: near tile boundaries the corridor margin tends to zero and subdivision explodes; cap the depth and record the residue honestly rather than forcing coverage.
- The needed word length may genuinely diverge along interior limit lines (believed to be why the frontier is hard); a pocket resisting all words up to the length cap is a reportable empirical finding, not a failure to hide.
- The unstable loci (right and isosceles lines) are cracks between tiles; pointwise claims crossing them need the separate classical arguments wired explicitly into the coverage proof.
- Vertex-grazing corridors produce float-feasible but interval-infeasible words; never promote a candidate without the certificate.
- Relabeling/orientation bugs in the unfolding are the classic silent killer; the independent checker must recompute unfoldings from scratch, not reuse the search code's geometry.
- Tile databases without canonical word forms accumulate duplicates that corrupt coverage statistics; canonicalize (cyclic rotation, reversal, relabeling) on insertion and re-canonicalize in the checker.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Box endpoints and all region bookkeeping in exact rationals (angles as rational multiples of $\pi$); all tile proofs in interval arithmetic with directed rounding; the stability data $(a,b)$ of every used word computed in exact integer arithmetic. Floating point only in the exploratory search layer, never in a certificate.
2. **Independent verification.** A standalone tile checker - independent code path for unfolding, trig enclosures, and corridor inequalities - consuming only $(w, B)$ and re-deriving the certificate. Dual implementations (Python/mpmath-interval and C++/MPFI) run on the full certified tile set; any disagreement is treated as a failed certificate.
3. **Reproducibility.** Search parameters (length caps, sample grids, margins, subdivision limits), tool versions, and random seeds recorded; SHA-256 manifest over the word database, tile database, and checker outputs.
4. **Preservation.** The search code, the rejected-candidate log (words that float-passed but failed certification), and the uncovered-residue description are part of the record; unpreserved intermediates must be declared explicitly.
5. **Honest reporting.** The report opens by stating whether the section 2 standard was met (it will not be, absent a breakthrough) and states the exact certified region: which boxes, which $\gamma$ range, pointwise versus measure-theoretic coverage, and the precise relationship to the published frontier value as re-verified at session start.
