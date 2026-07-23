# PROMPT FOR GLYCAN AND GLYCOPROTEIN 3D STRUCTURE PREDICTION

## The flexible, branched, water-mediated blind spot - an ensemble target, not one structure

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Pack:** B - reality-gated (empirical verifier)
**Rank:** B-16 of 29
**Source:** chem/bio top-50 list #23, section C (beyond static structure)
**Modes:** `[struct]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Glycans coat most cell-surface and secreted proteins and mediate immunity, trafficking, and recognition, yet their 3D structure is a genuine blind spot for prediction. Unlike a folded protein domain, a glycan is **branched, highly flexible, and stabilized by water- and ion-mediated contacts**, and it is drastically underrepresented in the PDB - where glycans, when present at all, are frequently disordered and only partially resolved. The consequential target is therefore not a single conformation but a **conformational ensemble**: the population of glycosidic-torsion states a glycan samples, and how that ensemble shields or presents the underlying protein surface. Static single-structure predictors (AlphaFold-lineage) place the fold and stub glycans but do not deliver correct Boltzmann-weighted glycan ensembles; force-field and grafting approaches (GLYCAM, GlycoSHIELD, GlycoShape) give ensembles but inherit force-field and sampling limits. This is **reality-gated**: the ground truth is an experimentally measured ensemble (NMR couplings/NOEs, crystallographic density, ion-mobility populations, MD validated against these), and that measurement is the bottleneck. Compute can advance ensemble prediction and shielding estimates; it cannot certify a glycan's solution ensemble without new physical experiment. This item connects directly to Boltzmann-weighted ensemble prediction - the deliverable is an ensemble, scored as an ensemble.

## 1. Exact problem statement

**Input.** A glycoprotein: the protein sequence/structure plus the covalently attached glycan(s) specified as a linkage graph (monosaccharide identities and glycosidic linkages, e.g. an N-glycan at a given Asn), and declared solution conditions (ions, pH). Free-glycan and protein-attached tracks are scored separately.

**Output.** A predicted **conformational ensemble** - a set of full-atom conformers with Boltzmann-like weights (or the equivalent torsion-angle distributions and conformer populations) for each glycosidic linkage and for the whole glycan - plus derived observables: per-linkage torsion distributions $p(\phi,\psi,\omega)$, conformer-cluster populations, and the glycan's **shielding map** over the protein surface.

**Metrics.** Because the target is an ensemble, single-structure RMSD is inadequate. Score by **distributional agreement** with the reference ensemble:
- Glycosidic-torsion distribution divergence (Jensen–Shannon / earth-mover distance) per linkage,
$$D_{\mathrm{JS}}\big(p_{\text{pred}}(\phi,\psi)\,\|\,p_{\text{ref}}(\phi,\psi)\big),$$
- conformer-population error (predicted vs. reference cluster weights),
- **back-computed experimental observables**: agreement of ensemble-averaged NMR ³J-couplings, NOEs/residual dipolar couplings, and ion-mobility collision cross-sections with measured values (RMSE / $\chi^2$),
- shielding-map agreement (per-residue accessibility reduction) where a reference exists.

**Population.** N-glycans, O-glycans, and glycosaminoglycans reported separately; stratified by branching complexity and by flexibility class. Because the corpus is small and biased, per-glycan-type tables accompany any aggregate.

**Compute-tractable sub-question.** On a frozen split, predict glycan torsion distributions / conformer populations that match a reference ensemble (NMR-validated MD or experimental) better than a named baseline, and back-compute measured observables within experimental error, with calibrated uncertainty on the populations.

**Empirically-gated whole.** The actual solution-state ensemble of a specific glycan on a specific protein - verifiable only by NMR / crystallography / ion-mobility-MS / glycomics, never by simulation alone.

## 2. Verifier and data

**Ground-truth source.**
- **PDB / PDBe** - glycoprotein structures with resolved glycans (with the caveat that glycan density is often partial/disordered; the *resolved* portion and B-factors are the usable truth), and the PDBe/GlyGen glyco-annotations.
- **Glycan repositories:** **GlyTouCan** (glycan accession/structure registry), **GlyCosmos / GlyConnect / GlyGen**, and **CSDB** (Carbohydrate Structure Database) - sequence/linkage truth and cross-links to structures (verify coverage).
- **Ensemble references:** **GlycoShape** (Fadda et al.; verify) and **GLYCAM-Web** (Woods lab) - glycan conformer ensembles from validated MD; **GlycoSHIELD** (Sikora, Hanus et al.; verify) - grafted glycan-ensemble shielding. These are *MD/grafting* references, trusted only where validated against experiment.
- **Experimental observables:** **BMRB** and primary NMR literature (³J-couplings, NOEs, RDCs) for solution ensembles; **ion-mobility-MS** collision-cross-section datasets for conformer populations; **mass-spec glycomics** for composition/sequence.

**Frozen split (leakage-safe).** The test set is fixed before modeling by **glycan-type / linkage-motif clustering** (no test glycan sharing its full branch topology and attachment context with training) intersected with a **time split** where structure/annotation dates allow. For protein-attached glycans, the underlying protein is also cluster-separated to avoid learning the site rather than the glycan. MD-derived ensembles used as references are held out as *references only*, never as training labels for the same glycan they score. All split, cluster, and reference-provenance manifests are committed and hashed before any evaluation.

**Wet-lab gate (mandatory).** A glycan's true solution ensemble **cannot be established by computation**. It requires experimental measurement: solution NMR (³J-couplings, NOEs, RDCs - the primary ensemble probe, with limited chemical-shift dispersion making assignment laborious), X-ray/cryo-EM density (which frequently fails to resolve flexible glycans), ion-mobility mass spectrometry (conformer-population fingerprints), and mass-spec glycomics (to even establish the glycan sequence/heterogeneity present). Producing and characterizing a defined glycoform is itself hard (glycan microheterogeneity; synthesis or enzymatic remodeling), and a full ensemble characterization is many months and, in effort terms, roughly \$80k–\$300k per system. An MD trajectory or a grafted ensemble is a hypothesis, not a verifier; a carbohydrate force field is not the solution state. This gate is not softenable.

## 3. Standard of a genuine advance

A genuine advance is one of:
1. A **certified method contribution** - an ensemble-prediction method that, on the frozen split, matches experimentally validated reference ensembles (torsion distributions, conformer populations) and back-computes measured NMR/ion-mobility observables significantly better than a named baseline (GLYCAM/GlycoShape MD, or an AF3 static output), with calibrated uncertainty on populations.
2. A **falsifiable, ranked ensemble/shielding prediction set** - for glycoproteins under active NMR/ion-mobility/crystallographic study, predicted ensembles and shielding maps with calibrated conformer populations, registered before results, ready for a glyco-structural partner.

**Not accepted as resolution:**
- A **single "the structure" of a flexible glycan** - reporting one conformer (or an RMSD to one) misrepresents an ensemble target; this is the defining error here.
- A **leaderboard/distributional number treated as a guarantee** of the real solution ensemble.
- **In-silico "validation"** - agreement with an *unvalidated* MD force field, or between two simulation methods, is not experimental confirmation; matching a reference ensemble that was itself never validated against experiment proves nothing.
- A **corpus-overfit metric** - accuracy driven by the few well-studied N-glycan cores and by memorizing common linkage motifs, that collapses on rare branches, O-glycans, or glycosaminoglycans.

## 4. Graded targets

**P1 - Reproduce baselines.** Reproduce GLYCAM/GlycoShape reference ensembles and AF3's static glycan placement on the frozen split; back-compute NMR/ion-mobility observables with an independent tool and quantify each baseline's ensemble error. *Evidence:* committed split hashes, standalone observable back-calculators, per-glycan-type tables.

**P2 - Calibrated ensemble uncertainty.** Predict conformer populations with calibrated uncertainty; validate that predicted population uncertainty tracks realized error on held-out glycans. *Evidence:* reliability curves on population weights, expected calibration error.

**P3 - Certified method contribution.** A method - a learned generative ensemble model, an enhanced-sampling or reweighting scheme, or a physics+ML hybrid - that significantly improves distributional agreement and observable back-calculation over P1 on held-out glycans, including harder strata (branched, O-glycan, GAG). *Evidence:* paired per-glycan deltas with confidence intervals, ablations, no test-set tuning.

**P4 - New held-out SOTA.** Best-in-class ensemble/observable agreement on the committed split across glycan types, at one-GPU-feasible inference. *Evidence:* full distributional comparisons, split manifests, independent reproduction.

**P5 - Wet-lab-ready ensemble predictions.** A ranked, calibrated set of ensemble + shielding predictions for glycoproteins under active NMR/ion-mobility/crystallographic study, registered before results, with pre-committed falsifiable claims (e.g. predicted ³J-couplings / CCS within stated tolerance) and honest post-hoc scoring including misses. The machine's ceiling; the spectrometer closes the loop.

## 5. Known results and prior art

- **GLYCAM / GLYCAM-Web** - Woods and collaborators - the carbohydrate force field and modeling tools underlying much glycan MD; the ensemble-generation workhorse and baseline.
- **GlycoShape / Re-Glyco** - Fadda and collaborators (~2023–2024; verify) - a database of glycan conformer ensembles from validated MD and a tool to graft them onto protein structures; the ensemble reference resource.
- **GlycoSHIELD** - Sikora, Hanus and collaborators (~2023; verify) - grafts precomputed glycan conformer ensembles onto static protein structures to estimate surface shielding; the shielding reference.
- **AlphaFold3** - Abramson et al. (2024, Nature) - added covalent-modification/glycan support; places glycans but does not deliver validated Boltzmann-weighted glycan *ensembles* - **re-verify the ensemble quality on our split.**
- **Glycan databases** - GlyTouCan / GlyCosmos / GlyConnect / GlyGen (community glycan registries and annotations) and CSDB (Carbohydrate Structure Database); the sequence/linkage truth (verify coverage of 3D links).
- **Experimental ensemble methods** - solution NMR of glycans (³J, NOE, RDC; e.g. work by Fontana, Almond, Woods and others; verify), ion-mobility MS for conformer populations, and MD-vs-NMR reweighting - the validation backbone.
- **Glycosaminoglycans** - heparin/heparan-sulfate and chondroitin modeling - an especially data-poor, highly charged, ion-dependent sub-case.

*Status as of mid-2026 - re-verify against current literature before starting any session.* Check whether AF3-class or generative models now produce experimentally validated glycan *ensembles* (not single conformers) on a leakage-safe split; as of writing, the flexible-ensemble target is open.

## 6. Attack plan

**Data.** Assemble glycoprotein structures with resolved glycans from PDBe; pull GlyTouCan/GlyCosmos linkage truth; collect validated reference ensembles (GlycoShape/GLYCAM) and experimental observables (BMRB NMR, ion-mobility CCS). Cluster by branch topology and (for attached glycans) protein; commit a linkage-motif ∩ time split with reference provenance recorded. Freeze and hash before modeling.

**Baselines.** GLYCAM/GlycoShape MD ensembles, AF3 static placement, GlycoSHIELD shielding. Back-compute NMR ³J/NOE/RDC and ion-mobility CCS with an independent tool for scoring.

**Model.** Candidate contributions: (i) a **generative ensemble model** over glycosidic torsions conditioned on the linkage graph and ions; (ii) **enhanced-sampling / reweighting** to correct force-field population bias against experimental observables; (iii) a **shielding predictor** validated where reference exists; (iv) explicit **ion/water-mediated** contact modeling for GAGs. Output populations, not single structures.

**Calibration.** Validate predicted conformer-population uncertainty against realized error on held-out glycans; report expected calibration error on populations.

**Compute.** Generative-ensemble inference and grafting are one-GPU feasible; short validated MD is affordable; long atomistic MD of large branched glycans is the expensive tail and is optional. The bottleneck is experimentally validated reference data, not compute.

**Failure modes.** (i) **Data scarcity / disorder** - glycans are under-resolved in the PDB; few experimentally validated ensembles exist. (ii) **Verifier trap** - matching an *unvalidated* MD reference proves nothing; only experiment-validated references and back-computed observables count. (iii) **Ensemble misframing** - collapsing to one conformer is the standard error. (iv) **Distribution shift / leakage** - dominance of common N-glycan cores; motif leakage; strict linkage-motif separation required. (v) **Microheterogeneity** - the physical sample is a mixture of glycoforms, complicating any experimental comparison.

## 7. Verification and auditability requirements

1. **Leakage-safe evaluation.** Linkage-motif clustering (and protein clustering for attached glycans) plus a time axis, committed and hashed before evaluation; MD-derived references held out as references only, never as labels for the glycan they score; no test-set tuning; per-glycan-type reporting.
2. **Calibrated uncertainty.** Every predicted ensemble carries calibrated conformer-population uncertainty; calibration is reported on held-out glycans.
3. **Independent reproduction.** Torsion-distribution divergences, population errors, and back-computed NMR/ion-mobility observables are recomputed by standalone tools separate from the generator, from committed splits and predicted ensembles.
4. **Cryptographic manifest.** A SHA-256 manifest covers split and linkage-motif definitions, reference-ensemble provenance, data version hashes, model code, weights, and every predicted ensemble and derived observable.
5. **Preservation.** Generative/sampling code, weights, force-field and reweighting configuration, and dataset version hashes are part of the record; anything not preserved is stated explicitly.
6. **Prospective-prediction registry.** Any ensemble/shielding prediction handed to a partner (P5) is timestamped and registered with its predicted observables, population weights, and pre-committed tolerance before results, and scored afterward including misses.
7. **Honest reporting.** The report states up front that glycan 3D structure is reality-gated, is an **ensemble** target, and is **not resolved**; separates in-silico/MD agreement from experimental confirmation; labels every predicted ensemble a wet-lab-pending hypothesis; never reports a single conformer as "the structure"; and never presents a distributional metric as a guarantee of the real solution ensemble.
