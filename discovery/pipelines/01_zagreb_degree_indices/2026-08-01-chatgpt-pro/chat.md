Worked for 50m 20s

> **Reframed objective:** exhaustively test published and automatically generated inequalities among degree-based graph indices on every connected unlabeled graph through $n=9$, push surviving candidates against adversarial graph families, independently verify all arithmetic, and return explicit graph6 witnesses with exact denominators.

# Result: explicit connected refutation obtained

The Hansen–Vukičević comparison

$$
\frac{M_1}{n}\leq \frac{M_2}{m}
$$

fails for the following connected bicyclic graph:

```
```
graph6: P]oCGGC@?G?_@?@??_?G?@??
```
```

## Exact witness data

| Quantity | Value |
| --- | --- |
| $n$ | 17 |
| $m$ | 18 |
| $\Delta$ | 11 |
| $\delta$ | 1 |
| Degree sequence | $11,4,3,2,2,2,2,1^{10}$ |
| $M_1$ | 172 |
| $M_2$ | 182 |
| $F$ | 1464 |
| Hyper-Zagreb $HM$ | 1828 |
| Albertson irregularity | 120 |
| Sigma index | 1100 |
| Tree | No |
| Chemical, $\Delta\leq4$ | No |
| Cyclomatic number | 2 |

The exact comparison is

$$
\frac{M_1}{n}=\frac{172}{17}, \qquad \frac{M_2}{m}=\frac{182}{18}=\frac{91}{9},
$$

and therefore

$$
\frac{M_1}{n}-\frac{M_2}{m} =\frac{172}{17}-\frac{91}{9} =\frac{1}{153}>0.
$$

Equivalently, without division,

$$
mM_1-nM_2 =18(172)-17(182) =3096-3094 =2>0.
$$

The small margin, only $1/153$, is why every comparison in the sweep used exact fractions or integer cross-products rather than floating point.

## Human-readable construction

Use vertices $0,\ldots,16$:

1.  Construct $K_{2,3}$ with parts $\{0,1\}$ and $\{2,3,4\}$.

2.  Construct a star with center $5$ and leaves $6,\ldots,16$.

3.  Add the bridge edge $0\text{--}6$.


```
```
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
```

This is the $\nu=2,p=11$ member of the published $K_{2,\nu+1}$\-plus-star bridge family. Caporossi, Hansen, and Vukičević displayed the 17-vertex bicyclic example and derived the corresponding infinite family. Thus, the witness is a verified reconstruction, not a claim of a previously unknown counterexample. [![](https://www.google.com/s2/favicons?domain=https://match.pmf.kg.ac.rs&sz=128)match.pmf.kg.ac.rs+1](https://match.pmf.kg.ac.rs/electronic_versions/Match63/n2/match63n2_441-451.pdf)

The original 2007 paper formulated the comparison for connected graphs, reported that it fails in general, and proved it for chemical graphs with maximum degree at most four. [![](https://www.google.com/s2/favicons?domain=https://www.gerad.ca&sz=128)GERAD](https://www.gerad.ca/fr/papers/G-2006-51.pdf)

# Exhaustive census through $n=9$

The enumeration used Brendan McKay’s official connected graph6 catalogues. These contain the same graph sets as `geng -c n` and are bundled in the package for reproducibility. The connected counts exactly match the requested A001349 values. [![](https://www.google.com/s2/favicons?domain=https://users.cecs.anu.edu.au&sz=128)ANU CECS Users+1](https://users.cecs.anu.edu.au/~bdm/data/graphs.html)

| $n$ | Connected | Trees | Chemical connected | Chemical trees |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 | 1 |
| 3 | 2 | 1 | 2 | 1 |
| 4 | 6 | 2 | 6 | 2 |
| 5 | 21 | 3 | 21 | 3 |
| 6 | 112 | 6 | 78 | 5 |
| 7 | 853 | 11 | 353 | 9 |
| 8 | 11,117 | 23 | 1,929 | 18 |
| 9 | 261,080 | 47 | 12,207 | 35 |

Totals for nontrivial graphs, $n\geq2$:

| Scope | Candidates |
| --- | --- |
| All connected graphs | 273,192 |
| Trees | 94 |
| Chemical connected graphs | 14,597 |
| Chemical trees | 74 |
| Connected unicyclic graphs | 383 |

No connected graph with $n\leq9$ violates the Hansen–Vukičević comparison. Consequently:

$$
\text{smallest counterexample order}>9.
$$

The run does **not** prove that 17 is globally minimal because orders $10,\ldots,16$ were not exhaustively enumerated. The official $n=10$ connected census alone contains 11,716,571 graphs, so it was left outside this batch. [![](https://www.google.com/s2/favicons?domain=https://users.cecs.anu.edu.au&sz=128)ANU CECS Users](https://users.cecs.anu.edu.au/~bdm/data/graphs.html)

# Literature-bound results

| Bound or scope | Census tested | Census broken | Adversarial tested | Adversarial broken |
| --- | --- | --- | --- | --- |
| $M_1/n\leq M_2/m$, general connected | 273,192 | 0 | 8,931 | **513** |
| Same, trees | 94 | 0 | 1,931 | 0 |
| Same, chemical graphs | 14,597 | 0 | 397 | 0 |
| Same, unicyclic graphs | 383 | 0 | 173 | 0 |
| Furtula–Gutman lower bound 1 | 273,192 | 0 | 8,931 | 0 |
| Furtula–Gutman lower bound 2 | 273,192 | 0 | 8,931 | 0 |
| Corrected Furtula–Gutman upper bound | 273,192 | 0 | 8,931 | 0 |
| Literal printed Furtula–Gutman formula | 273,192 | **21,209** | 8,931 | **4,603** |
| Che–Chen irregularity lower bounds | 273,192 each | 0 | 8,931 each | 0 |
| Che–Chen $\Delta,\delta$ upper bound | 273,192 | 0 | 8,931 | 0 |
| Common $M_1,M_2$ lower/upper bounds | 273,192 each | 0 | 8,931 each | 0 |

All **13 corrected or scope-restricted literature statements** tested survived both the exhaustive census and the adversarial family sweep. The common Zagreb bounds tested include

$$
M_1\geq\frac{4m^2}{n},\qquad M_2\geq\frac{4m^3}{n^2},\qquad 2M_2\leq \Delta M_1,
$$

as developed in the Zagreb-comparison literature. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/pdf/1104.4262)

The 1972 Gutman–Trinajstić work was retained as historical provenance for the degree-power expressions, but no standalone “1972 inequality” was placed in the checker without a precisely verified theorem statement.

## Literal forgotten-index print failure

The printed formula

$$
F\leq 2M_2+m(n-2)
$$

already fails at the star $K_{1,3}$:

```
```
graph6: CF
```
```

For this graph,

$$
n=4,\quad m=3,\quad M_2=9,\quad F=30,
$$

so the printed right-hand side is

$$
2(9)+3(4-2)=24,
$$

giving the false statement

$$
30\leq24.
$$

The corrected formula is

$$
F\leq2M_2+m(n-2)^2,
$$

which gives $30\leq30$. Che and Chen explicitly identify the absent square as a typographical error. This is therefore a literal published-formula counterexample, but not a substantive refutation of the corrected theorem. [![](https://www.google.com/s2/favicons?domain=https://match.pmf.kg.ac.rs&sz=128)match.pmf.kg.ac.rs+1](https://match.pmf.kg.ac.rs/electronic_versions/Match76/n3/match76n3_635-648.pdf)

# Auto-fit and adversarial push

The training stage used all 995 connected graphs with $2\leq n\leq7$. For the panel

$$
M_1,\ M_2,\ F,\ HM,\ \operatorname{irr},\ \sigma,\ M_1/n,\ M_2/m,
$$

all 28 unordered index pairs were considered. Exact minimum and maximum homogeneous ratios produced 56 one-sided candidate inequalities.

| Stage | Result |
| --- | --- |
| Candidate inequalities generated | 56 |
| Broken by all connected graphs at $n=8,9$ | 26 |
| Survived the $n=8,9$ push | 30 |
| Survived through $n=9$, then broke adversarially | 1 |
| Computationally hardened survivors | 29 |

The unique bound that survived every connected graph through $n=9$ but failed in the adversarial sweep was exactly

$$
\frac{M_1/n}{M_2/m}\leq1.
$$

For the 17-vertex witness, its observed ratio is

$$
\frac{M_1/n}{M_2/m}=\frac{1548}{1547}>1.
$$

The remaining 29 inequalities are labelled **computational survivors**, not theorems. Some are elementary consequences of nonnegativity or exact index identities.

## Adversarial-family outcome

A total of 8,931 parameter instances through order 60 were tested. They were intentionally not isomorphism-deduplicated.

| Group | Instances | Hansen–Vukičević failures |
| --- | --- | --- |
| $K_{2,\nu+1}$\-plus-star bridge family | 855 | 372 |
| Star plus triangle-chain family | 350 | 141 |
| Complete bipartite, stars, double-stars, brooms, kites, Turán, barbells, subdivided stars, dense-plus-pendant | 7,726 | 0 |
| **Total** | **8,931** | **513** |

# Independent verification

Every graph was evaluated twice:

1.  A manually written graph6 decoder using integer adjacency bitsets.

2.  NetworkX’s independent graph6 parser, followed by separately written index loops.


All 273,193 graphs, including $K_1$, passed exact agreement and the identities

$$
\sum_v d(v)=2m,
$$

$$
M_1=\sum_{uv\in E}(d(u)+d(v)),
$$

$$
F=\sum_{uv\in E}\bigl(d(u)^2+d(v)^2\bigr),
$$

$$
HM=F+2M_2, \qquad \sigma=F-2M_2.
$$

No floating-point tolerance determines any reported result.

# Reproducible files

**Complete package:**

Download the degree-index inequality sweep ZIP

SHA-256:

```
```
1f5c24b9c34813a64b04a0b0524655389c5c00949d1f43acdeabd107ed8578bc
```
```

Principal files:

-   README.md

-   REPORT.md

-   literature\_bounds.csv

-   autofit\_hardened\_survivors.csv

-   17-vertex graph6 witness

-   17-vertex edge list

-   sweep.py


## Takeaways

1.  **Explicit connected refutation:** graph6 `P]oCGGC@?G?_@?@??_?G?@??`, with exact gap $1/153$.

2.  **Exhaustive lower-order exclusion:** no connected counterexample through $n=9$.

3.  **No new corrected-theorem failure:** all 13 corrected or properly restricted literature bounds survived the census and adversarial sweep.

4.  **Literal print error:** the missing-square forgotten-index formula fails first at $K_{1,3}$.

5.  **Auto-fit warning:** a candidate may survive more than 273,000 exhaustive small graphs and still fail immediately under a targeted structural family.


README.mdDocumentOpen file

REPORT.mdDocumentOpen file

literature\_bounds.csvSpreadsheetOpen file

autofit\_hardened\_survivors.csvSpreadsheetOpen file

sweep.pyCodeOpen file

Show less

![](https://www.google.com/s2/favicons?domain=https://users.cecs.anu.edu.au&sz=32)

![](https://www.google.com/s2/favicons?domain=https://www.gerad.ca&sz=32)

![](https://www.google.com/s2/favicons?domain=https://match.pmf.kg.ac.rs&sz=32)

Sources