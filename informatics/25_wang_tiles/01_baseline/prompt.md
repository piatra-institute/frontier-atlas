# PROMPT FOR MINIMAL APERIODIC TILE SETS IN OPEN VARIANT MODELS

## Smallest aperiodic sets beyond the settled Wang-tile case - other tile models, forced structures, and the monotile line

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 25 of 50  
**Area:** computation models & automated reasoning  
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An **aperiodic** tile set admits a tiling of the plane but **no periodic** tiling. The question "what is the smallest aperiodic set of Wang tiles?" is **SOLVED and out of scope**: Jeandel and Rao (2015/2021) proved the minimum is **11 tiles over 4 colors**, by an exhaustive computer search establishing that every set of \(\le 10\) Wang tiles either fails to tile the plane or admits a periodic tiling, together with an aperiodicity proof for one 11-tile candidate. Do **not** target that number. This prompt re-scopes to the genuinely open neighbourhood: minimal aperiodic sets in **other tile models** (edge-to-edge polygon protosets, Wang cubes / higher dimensions, tiles with colored corners or rotations allowed, sofic/SFT-forced constraints), aperiodic sets that **force a specific structure** (a given subshift, a given hierarchical substitution, a fixed slope), and minimality/forcing questions along the **2023 hat/spectre monotile line** (a single tile that tiles only aperiodically). These are exhaustive-search-and-certify problems with machine-checkable ground truth: a small aperiodic set is proved aperiodic by a certified hierarchical/substitution argument, and a minimality claim is proved by an exhaustive isomorph-free enumeration that no smaller set works. Anything short - an aperiodic set with no minimality proof, or a minimality claim from an unreplayable search - is a partial result.

## 1. Exact problem statement

**Wang tiles (the settled reference, not the target).** A Wang tile is a unit square with a color from a finite palette on each edge; a tile is \((n,e,s,w)\in C^4\) over a color set \(C\). A *Wang set* \(T\subseteq C^4\) tiles the plane if there is a map \(\phi:\mathbb Z^2\to T\) with matching colors across every shared edge:
\[
\mathrm{east}(\phi(i,j))=\mathrm{west}(\phi(i{+}1,j)),\qquad \mathrm{north}(\phi(i,j))=\mathrm{south}(\phi(i,j{+}1)).
\]
The set of all valid \(\phi\) is a subshift of finite type \(X_T\subseteq T^{\mathbb Z^2}\). \(T\) is **aperiodic** if \(X_T\neq\varnothing\) but contains no \(\phi\) invariant under a nonzero translation \(v\in\mathbb Z^2\) (\(\phi\circ\sigma_v=\phi\)). The size measure is \((|T|,|C|)\). Jeandel–Rao settled the minimum: **11 tiles, 4 colors**, both parameters minimal.

**In-scope variant models (pick one and fix it precisely).**
1. **Other geometric protosets.** Edge-to-edge polygon tiles with matching rules, allowing prescribed symmetry operations (translation only / translation+rotation / full isometry incl. reflection). Size measure: number of prototiles (and number of colors/markings). Open: minimum protoset size for aperiodicity under each symmetry regime and shape family.
2. **Higher dimension / Wang cubes.** Unit cubes with colored faces tiling \(\mathbb Z^3\); minimum tile count for aperiodicity, and minimal sets forcing a given 3D structure.
3. **Corner/vertex-colored, or partial-matching, tiles.** Alternative local rules (corner colors, "ribbon" constraints); minimal aperiodic sets under these rules.
4. **Structure-forcing sets.** The smallest tile set whose tilings all belong to a prescribed subshift \(X\) (e.g. all tilings encode a fixed substitution / a fixed irrational slope / a specified Sturmian-like structure). Recent work builds aperiodic Wang sets tied to each quadratic irrational; minimality within such families is open.
5. **Monotile-line questions (hat/spectre).** For the aperiodic monotile family (the "hat", the chiral "spectre", 2023), open minimality/forcing questions: minimal matching-rule decorations, minimal marked-tile analogues, the smallest *combinatorial* (Wang-encoded) representation of the hat's forcing, and whether smaller monotiles exist under stated shape/adjacency constraints. Note that a single-tile "aperiodicity" is a forcing statement about one protoshape and its allowed isometries, not a protoset-cardinality minimum, and the two must not be conflated.

**The open question, generically.** Fix a model \(\mathcal M\) and a symmetry regime \(G\) (which isometries may map a tile to a placed copy). Determine
\[
\mu(\mathcal M,G)=\min\{\,|T| : T\ \text{a protoset in}\ \mathcal M,\ X_T^{G}\neq\varnothing,\ X_T^{G}\ \text{has no periodic point}\,\},
\]
or, for a fixed target structure \(X\), the minimum size of a protoset whose tiling space equals (or forces) \(X\). A resolution supplies both a witness at the claimed size **and** an exhaustive proof that nothing smaller works.

## 2. Resolution standard

A result resolves a variant only in certified form.

- **Minimal aperiodic set in a variant.** A protoset \(T\) of size \(s\) in the fixed model, with **(a)** a certified aperiodicity proof - a machine-checkable hierarchical/substitution argument (a proved substitution system whose tilings are exactly the tilings of \(T\), forcing non-periodicity), and **(b)** a certified minimality proof - an **exhaustive isomorph-free enumeration** of all protosets of size \(<s\) (up to the model's symmetries and color renaming) showing each either does not tile the plane or admits a periodic tiling. Both halves are required; either alone is a partial result.
- **Structure-forcing set.** A protoset \(T\) with a certified proof that its tiling space equals (or forces) the prescribed subshift \(X\), plus, if minimality is claimed, the exhaustive enumeration ruling out smaller sets.
Formally, a minimality certificate for size \(s\) is a machine-checked disjunction over the canonical enumeration:
\[
\forall T\ \text{with}\ |T|<s:\quad X_T=\varnothing\ \ \vee\ \ \exists v\neq 0\ \exists \phi\in X_T:\ \phi\circ\sigma_v=\phi,
\]
each disjunct discharged by an explicit certificate (a non-tiling proof or an exhibited periodic tiling); the aperiodicity of the witness is the negation of the same predicate, proved via a substitution.

- **Named certified form.** One of: an **exhaustive machine-enumeration certificate** (canonical, isomorph-free, replayable) establishing minimality/nonexistence, together with a **certified aperiodicity construction** for the witness (a checked substitution or a formally verified aperiodicity proof). SAT/transducer-based emptiness-of-periodic-tiling checks must emit replayable certificates.

**Not accepted as resolution.**
- Re-deriving or "improving" the 11-tile 4-color Wang minimum - it is settled (Jeandel–Rao) and gated out.
- An aperiodic set in a variant with **no minimality proof** (a construction alone does not establish the minimum).
- A minimality claim from a search whose completeness is asserted but not certified (no canonical enumeration, no replay).
- A size reduction achieved by silently enlarging the color/marking alphabet while comparing tile counts (both parameters are part of the size).
- Aperiodicity argued only from finite patches ("no periodic tiling found up to size \(N\)") rather than a proved substitution/hierarchical or transducer argument.
- Silent symmetry-regime changes (allowing rotations to shrink a set while comparing against a translation-only record).
- Conflating "tiles only non-periodically" (monotile) with "aperiodic protoset" without fixing the model.
- Claiming completeness over a candidate class that includes instances where neither a tiling nor a non-tiling certificate was obtained (the undecidability shadow).
- A forcing claim ("all tilings encode structure \(X\)") supported only by sampled patches rather than a proved invariant.

## 3. Graded partial-result targets

**P1 - Reproduce the gate.** Independently re-verify the Jeandel–Rao result:
- certify that specific \(\le 10\)-tile candidate families admit a periodic tiling or fail to tile;
- re-check the aperiodicity of the 11-tile witness via its known substitutive structure;
- confirm the color-minimality side (no aperiodic Wang set over \(<4\) colors) on the relevant candidates.

*Certificate:* a replayable transducer/SAT proof for the \(\le 10\) side on sampled candidates, and a checked substitution argument for the witness. Validates the pipeline and the gate.

**P2 - Certified aperiodicity of a variant witness.** For a fixed variant model, take a known or newly built aperiodic protoset and produce a machine-checked substitution/hierarchical proof of its aperiodicity:
- exhibit a substitution \(\rho\) mapping each tile to a finite super-tile block;
- prove \(X_T\) equals the substitutive subshift generated by \(\rho\) (the tiling-space equality lemma);
- prove the substitutive subshift is non-periodic (recognizability / unique-composition property).

*Certificate:* the substitution system with the tiling-space equality lemma, checked in a proof assistant or by a replayable structural checker.

**P3 - Exhaustive small-case nonexistence.** In a fixed variant, prove by exhaustive isomorph-free enumeration that no aperiodic protoset of size \(\le s_0\) exists (for the largest \(s_0\) you can complete):
- generate every protoset up to \(G\) and color/marking renaming;
- certify each as periodic-tiling (exhibit \(\phi\) with a nonzero period) or non-tiling (DRAT);
- publish the exact per-size candidate counts.

*Certificate:* canonical-generation code, per-candidate verdict, and a replay harness; a SHA-256 manifest over the candidate list.

**P4 - A new minimal aperiodic set in a variant.** Combine P2 and P3: a witness of size \(s\) with certified aperiodicity, plus exhaustive proof that size \(s-1\) is impossible in the model. This requires:
- the certified substitution proof for the witness (aperiodicity);
- the certified isomorph-free enumeration at size \(s-1\) with a verdict for every candidate;
- an explicit statement of the symmetry regime (translation-only / +rotation / +reflection) and size measure.

*Certificate:* both halves, with the regime and measure stated in the theorem, and any prior claim cited with source and access date.

**P5 - Structure-forcing minimality.** For a prescribed target structure (a fixed quadratic-irrational slope, a fixed substitution), determine the minimum protoset that forces it:
- prove the tiling space forces the target (every tiling encodes the prescribed slope/substitution);
- prove minimality by exhaustive enumeration below the claimed size within the model.

*Certificate:* forcing proof + isomorph-free enumeration, with the target structure precisely specified.

**P6 - Monotile-line result.** A certified minimality/forcing statement in the hat/spectre family:
- the minimal matching-rule decoration that forces aperiodicity of a single tile;
- a certified combinatorial (Wang-encoded) representation of the monotile's forcing hierarchy;
- an exhaustive nonexistence for a smaller monotile under stated shape/adjacency constraints.

*Certificate:* checked forcing proof (the substitution/hierarchy underlying the hat or spectre) and, for any minimality claim, an exhaustive enumeration over the constrained shape family.

## 4. Known results and prior art

**This area moved a lot recently - web-verify every attribution below before a session.**

- **Jeandel–Rao (2015 preprint; 2021 in Advances in Combinatorics)** - the smallest aperiodic Wang set is **11 tiles, 4 colors**, and both parameters are minimal; established by exhaustive search over sets of \(\le 11\) tiles (all \(\le 10\)-tile sets tile periodically or not at all) plus an aperiodicity proof for one 11-tile candidate. **This is the gate: do not target it.** (verify)
- **Historical Wang aperiodic sets** - Berger (1966, ~20426 then 104), Knuth, Läuchli, Robinson (1971, 6 tiles / 56 in various encodings), Culik–Kari (1996, 13 tiles), Kari (rational-based) - all superseded by Jeandel–Rao for the minimum. (verify counts)
- **Hat monotile (Smith, Myers, Kaplan, Goodman-Strauss, March 2023, arXiv 2303.10798)** - the first aperiodic *monotile* ("einstein") for the plane, using reflections; a 13-sided polykite. (verify)
- **Spectre (same team, May 2023, arXiv 2305.17743)** - a chiral aperiodic monotile requiring no reflected copies. (verify)
- **Metallic-mean / quadratic-irrational Wang sets** - recent constructions (e.g. Labbé and collaborators, ~2023–2026) giving aperiodic Wang sets realizing each quadratic irrational; the substitutive structure of the Jeandel–Rao tilings is now understood. (verify)
- **Minimality methods** - the transducer / automata approach to deciding whether a Wang set admits a periodic tiling, and SAT-based finite-patch obstructions, are the workhorses of the exhaustive side. (verify)
- **Undecidability backdrop** - the general "does this Wang set tile the plane?" problem is undecidable (Berger), which is *why* aperiodic sets exist and why exhaustive minimality must combine a periodic-tiling decider with a tiling/non-tiling decider that can fail on some candidates. (verify)
- **Kari–Culik line** - Kari's construction from Beatty sequences / rational multiplication (13 tiles) and Culik's 13-tile set are the pre-Jeandel–Rao small sets, and the substitutive method descends from Robinson. (verify counts)

Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session. In particular re-confirm the gate (Jeandel–Rao minimality) and the current state of monotile-family minimality results.

## 5. Attack plan

`[search]` for the enumeration side, `[cert]` for aperiodicity/forcing proofs. One workstation suffices for small variant sizes; blow-up is the main risk.

1. **Fix the model on paper first.** Pin the tile model, allowed symmetries, size measure, and (if forcing) the target structure. Ambiguity here invalidates any minimality claim.
2. **Reproduce the gate (P1).** Implement the transducer test for "admits a periodic tiling" and a finite-window SAT/CSP test for "tiles at all"; reproduce the \(\le 10\)-tile verdicts on sampled Jeandel–Rao candidates. Golly/lifelib-style pattern tooling and a custom C++/Rust CSP harness are the tools; use CaDiCaL/kissat with DRAT logging for the SAT obstructions, and a matrix/transducer library for the periodic-tiling decider.
3. **Canonical enumeration (P3).** Generate protosets up to the model's symmetry group and color/marking renaming with orderly generation:
   - quotient by color permutations and the model's geometric symmetries (nauty/Traces for the symmetry quotient);
   - for each candidate, run the periodic-tiling transducer test and the finite-window tiling CSP;
   - emit a certificate per verdict (an exhibited periodic tiling, or a DRAT non-tiling proof);
   - record exact candidate counts and SHA-256 hashes so exhaustiveness is auditable.
4. **Aperiodicity by substitution (P2).** For a witness:
   - search for a substitution \(\rho\) by fusing recurring super-tiles observed in large valid patches;
   - prove the unique-composition / recognizability property so every tiling decomposes uniquely under \(\rho\);
   - prove \(X_T\) equals the substitutive subshift and is non-periodic;
   - formalize the hierarchical argument, or write a replayable structural checker - this is what makes aperiodicity a proof rather than an observation.
5. **Monotile / forcing (P5/P6).** For the monotile line:
   - encode the hat/spectre matching/forcing combinatorially (as a marked-tile or Wang-style system) and study minimal decorations;
   - for quadratic-irrational forcing, tie the protoset to the known substitutive structure and prove the tiling-space equality;
   - keep the symmetry regime explicit - the hat needs reflections, the spectre is chiral - since it changes what "monotile" means.

**Failure modes.** (a) Targeting the gated Wang minimum - automatic non-result. (b) Enumeration blow-up - protoset counts explode with size; canonical reduction and early periodic-tiling pruning are essential. (c) Aperiodicity from finite patches - never a proof; a periodic tiling can appear only at large period, so patch evidence is necessary but never sufficient. (d) Undecidability shadow - the general "does this set tile?" problem is undecidable, so some candidates resist both a tiling and a non-tiling certificate; segregate these and do not claim completeness over them. (e) Symmetry-regime drift - comparing sets under different allowed symmetries. (f) Unreplayable SAT - always log DRAT/LRAT.

## 6. Verification and auditability requirements

1. **Exact or certified computation:** every "no smaller set works" claim rests on a canonical, isomorph-free enumeration with a per-candidate certificate (a DRAT/LRAT-checked non-tiling proof or an explicit periodic tiling); every aperiodicity/forcing claim rests on a checked substitution/hierarchical proof; finite-patch evidence is exploration only.
2. **Independent verification:** each certificate re-checked by a small standalone replay written apart from the search:
   - a DRAT/LRAT checker for every non-tiling proof;
   - a tiling re-validator that re-checks color matches across a large patch of any exhibited periodic tiling;
   - a substitution re-expander that regenerates patches and confirms they lie in \(X_T\);
   - dual implementations of the transducer periodic-tiling test where warranted.
3. **Reproducibility:** model, symmetry regime, size measure, canonical-form conventions, solver and enumerator versions recorded; SHA-256 manifest over candidate lists, certificates, and witnesses; the Jeandel–Rao gate and any variant baseline cited with source and access date. The exact candidate count at each size is published so an auditor can independently confirm exhaustiveness.
4. **Preservation:** enumeration source, substitution proofs, and checkers are part of the record; anything not preserved is stated explicitly. The witness protoset and its substitution are stored in a machine-readable form that the re-expander can consume directly.
5. **Honest reporting:** state up front the model and symmetry regime, whether both aperiodicity **and** minimality were certified (a construction without a minimality proof is labeled as such), and explicitly that the settled 11/4 Wang minimum is the gate, not the target. Undecidable-shadow candidates left unresolved are named, never hidden, and the report says plainly whether the claimed minimum is unconditional or conditional on unresolved candidates.
