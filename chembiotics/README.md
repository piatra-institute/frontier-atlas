# Piatra Institute - Computational Chemistry & Biology Program

Fifty open problems in computational chemistry and biology, selected for tractability by SOTA models (LLM reasoning agents plus the specialized nets they orchestrate: AlphaFold-lineage, diffusion generators, learned functionals). No ill-posed flagships.

The list is split into two packs by where the verifier lives:

- **Pack A - closed-loop (21).** The machine verifies its own answer without leaving the machine: a proof, a CAS identity, a physics simulation the AI runs (QM / MD / GCMC), or synthetic data with a known answer. These carry a genuine resolution standard, like the physics program. Prompts follow `PROMPT_TEMPLATE_A.md`. Start here.
- **Pack B - reality-gated (29).** The real verifier is empirical: a wet-lab assay, or a frozen experimental corpus that is itself the bottleneck. Compute can advance these (certified method + held-out SOTA + falsifiable predictions) but cannot close them. Prompts follow `PROMPT_TEMPLATE_B.md`. Each item needs a wet-lab partner and a multi-year horizon.

Mode tags: `[func]` learn a functional/potential · `[gen]` generative design · `[sym]` closed-form/scaling-law discovery · `[algo]` algorithm/complexity · `[cert]` rigorous/certified result · `[struct]` structure/ensemble prediction · `[data]` corpus mining.

## Pack A - closed-loop (work in numeric order)

| # | Folder | Problem | Modes | Orig | Sec |
|---|--------|---------|-------|------|-----|
| A01 | `A01_n_representability_2rdm` | Usable N-representability constraints for the 2-RDM | sym, cert | 5 | A |
| A02 | `A02_retrosynthesis_verified_routes` | Retrosynthesis with guaranteed-feasible, cost-optimal routes | algo, gen | 28 | D |
| A03 | `A03_mof_target_isotherm` | MOF / porous materials for a target adsorption isotherm | gen, search | 32 | D |
| A04 | `A04_reactivity_scaling_laws` | Closed-form rate constants / activation energies (BEP done right) | sym, func | 49 | G |
| A05 | `A05_ml_force_field_ccsdt` | Universal transferable ML force field at CCSD(T) accuracy | func | 4 | A |
| A06 | `A06_basis_sets_ecps` | Optimal compact basis sets / ECPs by search | gen, search | 7 | A |
| A07 | `A07_solvation_pka` | Accurate implicit solvation and protein pKa | func | 13 | B |
| A08 | `A08_reaction_coordinate_discovery` | Automatic reaction-coordinate / collective-variable discovery | data, func | 11 | B |
| A09 | `A09_mechanism_discovery` | Automated reaction-mechanism discovery (TS-verified) | algo, sym | 50 | G |
| A10 | `A10_nonadiabatic_conical_intersections` | Nonadiabatic couplings and conical intersections | func | 8 | A |
| A11 | `A11_exact_dft_functional` | The exact DFT exchange-correlation functional | func | 1 | A |
| A12 | `A12_free_energy_sampling` | Boltzmann-weighted folding/binding free-energy sampling | struct, func | 9 | B |
| A13 | `A13_conformational_ensembles` | Conformational ensembles with correct Boltzmann weights | struct | 16 | C |
| A14 | `A14_binding_kinetics` | Binding kinetics: k_on/k_off and residence times | struct | 12 | B |
| A15 | `A15_absolute_binding_free_energy` | Absolute binding free energies below 1 kcal/mol | func, struct | 10 | B |
| A16 | `A16_multireference_blackbox` | A black-box multireference method (auto active space) | algo | 6 | A |
| A17 | `A17_markov_state_models` | Automated Markov State Model construction | algo, data | 14 | B |
| A18 | `A18_coarse_graining` | Coarse-graining preserving thermodynamics AND kinetics | func | 15 | B |
| A19 | `A19_cryoem_heterogeneity` | Cryo-EM heterogeneous reconstruction (recover the distribution) | struct, data | 41 | F |
| A20 | `A20_fermion_sign_problem` | The fermion sign problem for specific Hamiltonians | func, algo | 2 | A |
| A21 | `A21_hubbard_ground_state` | Ground state of the 2D Hubbard model | func | 3 | A |

## Pack B - reality-gated (portfolio; needs a wet-lab partner)

| # | Folder | Problem | Modes | Orig | Sec |
|---|--------|---------|-------|------|-----|
| B01 | `B01_variant_effect_noncoding` | Variant-effect prediction, non-coding & structural | data | 36 | E |
| B02 | `B02_ddg_stability_dms` | Point-mutation ΔΔG stability/function at DMS scale | func, data | 21 | C |
| B03 | `B03_splicing_code` | The splicing code, including cryptic sites | data | 35 | E |
| B04 | `B04_regulatory_genome` | The regulatory / non-coding genome code | data | 34 | E |
| B05 | `B05_rna_3d_structure` | De novo RNA 3D structure prediction | struct | 18 | C |
| B06 | `B06_dark_proteome_annotation` | Function annotation for the dark proteome | data | 38 | E |
| B07 | `B07_protein_protein_complexes` | Protein-protein complexes & interaction networks | struct, data | 19 | C |
| B08 | `B08_fold_switching_proteins` | Fold-switching / metamorphic proteins | struct | 17 | C |
| B09 | `B09_condensate_phase_separation` | Phase-separation / condensate propensity from sequence | data, struct | 43 | F |
| B10 | `B10_tcr_pmhc_binding` | TCR:pMHC binding and immunogenicity | data, struct | 47 | G |
| B11 | `B11_antibody_codesign` | Antibody structure + developability + affinity co-prediction | struct, gen | 46 | G |
| B12 | `B12_crispr_outcomes` | CRISPR guide, off-target, and repair-outcome prediction | data, func | 39 | E |
| B13 | `B13_mrna_codon_optimization` | mRNA / codon optimization (expression, stability, immunogenicity) | gen, data | 40 | E |
| B14 | `B14_membrane_protein_structure` | Membrane proteins in native lipid environments | struct | 20 | C |
| B15 | `B15_idr_function_grammar` | Grammar of intrinsically disordered region function | data | 22 | C |
| B16 | `B16_glycan_structure` | Glycan and glycoprotein 3D structure | struct | 23 | C |
| B17 | `B17_subcellular_localization` | Subcellular localization and trafficking signals | data | 42 | F |
| B18 | `B18_genotype_phenotype_polygenic` | Genotype-to-phenotype for complex/polygenic traits | data | 37 | E |
| B19 | `B19_microbiome_function` | Microbiome community-function from metagenomes | data | 48 | G |
| B20 | `B20_de_novo_enzymes` | De novo enzymes at natural k_cat/K_M | gen | 24 | D |
| B21 | `B21_undruggable_binders` | De novo protein binders against flat/undruggable interfaces | gen | 27 | D |
| B22 | `B22_small_molecule_binders` | Programmable small-molecule binders and sensors | gen | 26 | D |
| B23 | `B23_allostery_design` | Design for a target conformational ensemble / allostery | gen | 25 | D |
| B24 | `B24_inverse_design_admet` | Inverse molecular design under synthesizability + ADMET | gen | 30 | D |
| B25 | `B25_stereoselective_catalysts` | Stereoselective organocatalysts / ligands for asymmetric catalysis | gen, func | 31 | D |
| B26 | `B26_reaction_yield_prediction` | Reaction-yield and condition prediction | data, func | 29 | D |
| B27 | `B27_solid_state_electrolytes` | Solid-state electrolytes / battery materials (stability + conductivity) | gen, search | 33 | D |
| B28 | `B28_whole_cell_model` | Whole-cell models with predictive (not fitted) kinetics | algo | 44 | F |
| B29 | `B29_metabolic_flux_prediction` | Metabolic-flux prediction beyond FBA | algo, func | 45 | F |

Sections (from the source list): A electronic structure · B free energy, dynamics, sampling · C beyond static structure prediction · D design · E genomics, sequence, systems · F cells, structures, images · G higher-order / adjacent. Every one of the 50 source entries appears exactly once (see the Orig column).

## Working protocol

Every session runs under the atlas `SOLVER.md` (agency, compute, adversarial self-verification).
Same protocol as the sister programs, with the pack distinction enforced:

1. **Pick** the lowest-numbered unstarted problem in Pack A first. Open a Pack B item only with a wet-lab collaborator lined up, or to build the in-silico half (baseline + falsifiable predictions) ahead of one.
2. **Re-verify** current status first. Start from `STATUS_AUDIT_2026-07.md`, which flags the problems whose SOTA baseline moved in 2025 (AlphaGenome for B01/B04, 2025 NQS for A21, RFdiffusion2 enzymes for B20, and more); re-baseline against those before claiming any contribution.
3. **Seed** a SOTA session with the attempt's `prompt.md` (template A or B as marked).
4. **Preserve** the transcript as `chat.md`.
5. **Require** a self-contained package: report (md + pdf), all code, certificates or frozen data-splits, independent verifier, SHA-256 manifest. Training/search code is part of the record.
6. **Report honestly:** Pack A states whether the resolution standard was met and reports held-out metrics; Pack B states up front that the problem is reality-gated and labels every design/prediction as a wet-lab-pending hypothesis.
7. **Update** the Status column and leave a `NEXT_STEPS.md` when pausing a line.

## Beware the verifier

A closed-loop verifier that is systematically biased (a force field, a docking score, a computed benchmark) turns "solved" into confident-but-wrong. Pack A prompts carry a mandatory benchmark-integrity clause; honor it. The pack boundary drifts: a Pack B problem migrates to Pack A once a trusted simulator or a dense-enough frozen corpus can act as verifier.
