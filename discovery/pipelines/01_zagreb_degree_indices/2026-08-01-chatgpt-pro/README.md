# Exact batch sweep of degree-based topological-index inequalities

## Result in one line

A connected 17-vertex bicyclic graph refutes the Hansen-Vukičević comparison

\[
\frac{M_1}{n}\le \frac{M_2}{m}.
\]

Its graph6 string is:

```text
P]oCGGC@?G?_@?@??_?G?@??
```

It has

```text
n = 17, m = 18
sorted degrees = 11,4,3,2,2,2,2,1,1,1,1,1,1,1,1,1,1
M1 = 172
M2 = 182
M1/n = 172/17
M2/m = 91/9
M1/n - M2/m = 1/153 > 0
m*M1 - n*M2 = 2 > 0
```

This is an explicit member of the published counterexample family formed from `K_{2,nu+1}` and a star `S_{p+1}`, joined by an edge from one star leaf to a vertex in the size-2 part. Here `nu=2` and `p=11`.

The exhaustive part of this run rules out a counterexample only through `n=9`. Orders 10 through 16 were not exhaustively enumerated, so this package does **not** certify global minimality of the 17-vertex witness.

## Human-readable construction of the 17-vertex witness

Use vertices `0,...,16`.

- Make `K_{2,3}` with parts `{0,1}` and `{2,3,4}`.
- Make a star centered at `5`, with leaves `6,...,16`.
- Add the bridge edge `{0,6}`.

Edge list:

```text
0 2
0 3
0 4
0 6
1 2
1 3
1 4
5 6
5 7
5 8
5 9
5 10
5 11
5 12
5 13
5 14
5 15
5 16
```

The edge-degree types are `4 x (4,2)`, `3 x (3,2)`, `1 x (11,2)`, and `10 x (11,1)`. Hence

\[
M_2=4(4\cdot2)+3(3\cdot2)+(11\cdot2)+10(11\cdot1)=182.
\]

The degree multiplicities give

\[
M_1=11^2+4^2+3^2+4\cdot2^2+10\cdot1^2=172.
\]

Therefore

\[
\frac{172}{17}-\frac{182}{18}=\frac{1}{153}>0.
\]

## Exhaustive census

The bundled files are Brendan McKay's official connected graph6 catalogues, equivalent as a graph set to running `geng -c n`. The run checked every connected unlabeled graph through `n=9`.

| n | connected | A001349 check | trees | A000055 check | chemical connected, Delta<=4 | chemical trees |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | 2 | 2 | 1 | 1 | 2 | 1 |
| 4 | 6 | 6 | 2 | 2 | 6 | 2 |
| 5 | 21 | 21 | 3 | 3 | 21 | 3 |
| 6 | 112 | 112 | 6 | 6 | 78 | 5 |
| 7 | 853 | 853 | 11 | 11 | 353 | 9 |
| 8 | 11,117 | 11,117 | 23 | 23 | 1,929 | 18 |
| 9 | 261,080 | 261,080 | 47 | 47 | 12,207 | 35 |

Totals used in inequalities with `m>0`:

- connected graphs: **273,192**
- trees: **94**
- chemical connected graphs: **14,597**
- chemical trees: **74**
- connected unicyclic graphs: **383**

The official `n=10` connected count is 11,716,571. It was not enumerated in this run.

## Index panel and exact identities

For each graph the sweep computed

\[
M_1=\sum_v d(v)^2,\qquad
M_2=\sum_{uv\in E}d(u)d(v),\qquad
F=\sum_v d(v)^3,
\]

\[
HM=\sum_{uv\in E}(d(u)+d(v))^2,
\]

\[
\operatorname{irr}=\sum_{uv\in E}|d(u)-d(v)|,
\qquad
\sigma=\sum_{uv\in E}(d(u)-d(v))^2.
\]

The implementation computes every quantity directly and checks, for every graph,

\[
\sum_v d(v)=2m,
\]

\[
M_1=\sum_{uv\in E}(d(u)+d(v)),
\qquad
F=\sum_{uv\in E}(d(u)^2+d(v)^2),
\]

\[
HM=F+2M_2,
\qquad
\sigma=F-2M_2.
\]

All five identities passed on all **273,193** graphs including `K1`.

## Independent verification discipline

Each graph is processed twice.

1. `indices_primary` manually decodes graph6, stores adjacency as integer bitsets, and evaluates all sums directly.
2. `indices_secondary` uses NetworkX's independent graph6 parser and graph representation, then recomputes the same values with separately written loops.

The two complete records must agree exactly. All inequality checks use integer cross-products or `fractions.Fraction`. No tolerance or floating-point comparison decides a result. This matters for the 17-vertex witness because its normalized gap is only `1/153`.

## Literature-bound results

The exact denominators and witnesses are in `results/literature_bounds.csv`.

| ID | Scope | Census tested | Census broken | Adversarial tested | Adversarial broken | First witness |
|---|---|---:|---:|---:|---:|---|
| HV_general | connected | 273,192 | 0 | 8,931 | 513 | 17 vertices, graph6 above |
| HV_trees | trees | 94 | 0 | 1,931 | 0 | none |
| HV_chemical | Delta<=4 | 14,597 | 0 | 397 | 0 | none |
| HV_unicyclic | unicyclic | 383 | 0 | 173 | 0 | none |
| FG_lower_1 | connected | 273,192 | 0 | 8,931 | 0 | none |
| FG_lower_2 | connected | 273,192 | 0 | 8,931 | 0 | none |
| FG_upper_corrected | connected | 273,192 | 0 | 8,931 | 0 | none |
| FG_upper_literal_printed | connected | 273,192 | 21,209 | 8,931 | 4,603 | `CF` = `K1,3` |
| CheChen_lower_irr_M2 | connected | 273,192 | 0 | 8,931 | 0 | none |
| CheChen_lower_irr_M1 | connected | 273,192 | 0 | 8,931 | 0 | none |
| CheChen_upper_Delta_delta | connected | 273,192 | 0 | 8,931 | 0 | none |
| M1_upper_Delta_delta | connected | 273,192 | 0 | 8,931 | 0 | none |
| M1_common_lower | connected | 273,192 | 0 | 8,931 | 0 | none |
| M2_common_lower | connected | 273,192 | 0 | 8,931 | 0 | none |
| M2_common_upper | connected | 273,192 | 0 | 8,931 | 0 | none |

### The literal Furtula-Gutman print error

Che and Chen explicitly document that the 2015 upper bound was printed with a missing square. Testing the printed text literally gives

\[
F\le 2M_2+m(n-2),
\]

which first fails at `K_{1,3}`, graph6 `CF`:

```text
n=4, m=3, M2=9, F=30
literal RHS = 2*9 + 3*(4-2) = 24
corrected RHS = 2*9 + 3*(4-2)^2 = 30
```

Thus `30 <= 24` is false, while the corrected theorem holds with equality. This is a verified typographical failure, not a substantive refutation of the corrected bound.

## Auto-fit and push stage

The script forms all 28 unordered pairs from

```text
M1, M2, F, HM, irr, sigma, M1/n, M2/m
```

and fits the exact minimum and maximum homogeneous ratio on all 995 connected graphs with `2<=n<=7`. This gives 56 candidate inequalities of the form

\[
c_{\min}Y\le X\le c_{\max}Y.
\]

Results:

```text
candidate bounds generated:                         56
broken by the exhaustive n=8,9 push:                26
survived every n=8,9 graph:                         30
survived n=8,9 but broken by adversarial families:   1
remaining computationally hardened survivors:      29
```

The single candidate that survived every graph through `n=9` but broke in the adversarial sweep is exactly

\[
\frac{M_1/n}{M_2/m}\le1,
\]

the Hansen-Vukičević comparison. The first adversarial break is the 17-vertex graph above, where the ratio is `1548/1547`.

The 29 remaining rows are **computational survivors**, not claimed theorems. Several are trivial nonnegativity bounds or consequences of elementary identities. See:

- `results/autofit_ratio_bounds.csv`
- `results/autofit_hardened_survivors.csv`
- `results/autofit_broken_candidates.csv`

## Adversarial family bag

The run tested 8,931 parameter instances through order 60:

| Family | Instances | HV violations |
|---|---:|---:|
| `HV_K2nu_star_bridge` | 855 | 372 |
| barbells | 2,530 | 0 |
| brooms | 931 | 0 |
| complete bipartite | 900 | 0 |
| dense-plus-pendant | 1,058 | 0 |
| double-stars | 841 | 0 |
| kites | 873 | 0 |
| stars | 59 | 0 |
| star plus triangle chain | 350 | 141 |
| subdivided stars | 40 | 0 |
| Turan graphs | 494 | 0 |

These are parameter instances, not a non-isomorphic census. Family overlap is intentionally retained because the purpose is adversarial stress testing, not counting graph isomorphism classes.

## Source verification status

- Hansen and Vukičević, *Comparing the Zagreb Indices*, Croatica Chemica Acta 80 (2007): conjecture, chemical-graph theorem, and general counterexamples verified from the paper/preprint.
- Caporossi, Hansen, and Vukičević, *Comparing Zagreb Indices of Cyclic Graphs*, MATCH 63 (2010): 17-vertex cyclic counterexample and infinite bridge family verified through the paper and a published survey.
- Furtula and Gutman, *A forgotten topological index* (2015): lower and upper formulas checked through Che and Chen's 2016 paper, which also explicitly records the missing-square typo.
- Che and Chen, *Lower and Upper Bounds of the Forgotten Topological Index*, MATCH 76 (2016): Propositions 3.1, 3.3, 4.2, and 4.3 checked from the paper.
- Ilić and Stevanović, *On Comparing Zagreb Indices*, MATCH 62 (2009): common lower and upper Zagreb bounds checked through the original paper/survey record.
- Gutman and Trinajstić (1972) is used as historical provenance for the degree-power expressions. No standalone 1972 inequality was added to the checker without a precisely verified statement.

## Reproduce

Python 3.11 or newer is recommended.

```bash
python -m pip install -r requirements.txt
python sweep.py --data-dir data --output-dir results
python verify_witnesses.py
```

The full run should reproduce the graph counts, all CSV files, the 17-vertex graph6 witness, and the exact `1/153` gap.

## File map

```text
README.md
sweep.py
verify_witnesses.py
requirements.txt
run_all.sh
data/graph2c.g6 ... graph9c.g6
witnesses/hv17.g6
witnesses/hv17.edgelist
witnesses/hv17.dot
witnesses/fg_literal_typo_K1_3.g6
witnesses/fg_literal_typo_K1_3.edgelist
results/summary.json
results/counts.csv
results/literature_bounds.csv
results/autofit_ratio_bounds.csv
results/autofit_hardened_survivors.csv
results/autofit_broken_candidates.csv
results/adversarial_families.csv
results/key_witnesses.json
results/key_witnesses.csv
results/violations_by_order.csv
```

## External data and literature locations

- McKay graph catalogues: `https://users.cecs.anu.edu.au/~bdm/data/graphs.html`
- nauty/Traces: `https://pallini.di.uniroma1.it/`
- Hansen-Vukičević article record: `https://hrcak.srce.hr/12846`
- GERAD preprint: `https://www.gerad.ca/fr/papers/G-2006-51.pdf`
- Zagreb-comparison survey: `https://match.pmf.kg.ac.rs/electronic_versions/Match65/n3/match65n3_581-593.pdf`
- Che-Chen forgotten-index bounds: `https://match.pmf.kg.ac.rs/electronic_versions/Match76/n3/match76n3_635-648.pdf`
