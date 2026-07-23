# Hadwiger-Nelson problem: exact partial result and research audit

**Date:** 22 July 2026  
**Target:** determine the unrestricted chromatic number of the Euclidean plane.  
**Outcome:** no complete determination was obtained. The rigorous interval remains

\[
5 \leq \chi(\mathbb{R}^2) \leq 7.
\]

This report does not present a restricted measurable, Borel, periodic, polygonal, or map-type result as the ordinary chromatic number. It records the strongest exact result obtained in this run, packages a direct certificate, and states the remaining gap precisely.

## 1. Executive result

Let `G510` be the graph specified by `data/510.vtx` and `data/510.edge`.
The exact verifier proves that:

1. the 510 coordinate expressions are distinct points in
   \(\mathbb{Q}(\sqrt3,\sqrt5,\sqrt{11})^2\);
2. the 2,504 listed edges are exactly all pairs at Euclidean distance 1;
3. there are 127,291 nonedges;
4. all 84 rows in `certificates/colorings_84.csv` are proper colorings with color set \(\{0,1,2,3,4\}\);
5. for every nonedge \(\{u,v\}\), at least one supplied coloring has \(c(u)=c(v)\), and at least one other supplied coloring has \(c(u)\ne c(v)\).

### Certified theorem: binary terminal flexibility of G510

For every nonedge \(\{u,v\}\) of `G510`, neither equality nor inequality of the two terminal colors is forced across all proper 5-colorings.

### Proof

The certificate contains 84 explicit color vectors. The verifier checks each vector directly against all 2,504 edges. It then checks each of the 127,291 nonedges and exhibits, by finite search through the certificate rows, both an equality witness and an inequality witness. This is a constructive finite proof; no probabilistic or floating-point step occurs in verification.

### Stronger corollary for subgraphs

No subgraph of `G510` can serve as a nontrivial two-terminal 5-color gadget using any nonedge terminal pair from `G510`. Indeed, the two full-graph witness colorings restrict to proper colorings of every subgraph while preserving the terminal relation.

This rules out the entire family of strategies that merely delete vertices or edges from `G510` and hope that a non-unit terminal pair becomes forced equal or forced different.

## 2. Exact golden-ratio geometry

Write

\[
\varphi=\frac{1+\sqrt5}{2}.
\]

The verifier finds exactly these terminal pairs at distance \(\varphi\):

- \((212,490)\)
- \((218,491)\)
- \((224,489)\)

It finds exactly these terminal pairs at distance \(1/\varphi\):

- \((212,491)\)
- \((218,489)\)
- \((224,490)\)

All six pairs are binary-flexible. For example, certificate row 1 colors every one of them differently, while rows listed in `certificates/special_pair_witness_rows.json` provide same-color witnesses.

## 3. Why the golden-ratio route was tested

Jaan Parts constructed a 31-vertex graph whose forbidden edge lengths are \(1\) and \(\varphi\), and whose chromatic number is at least 6. This gives the following exact conversion target.

### Unit-gadget conversion lemma

Suppose a finite unit-distance graph \(H\) has terminals \(x,y\) separated geometrically by \(\varphi\), and every proper 5-coloring of \(H\) satisfies \(c(x)\ne c(y)\). Replace every \(\varphi\)-edge of Parts' two-distance graph by a congruent copy of \(H\), identifying its terminals with the endpoints of that edge. Retain the original unit edges.

Then the geometric union is a finite unit-distance graph that is not 5-colorable.

### Proof

Any proper 5-coloring of the union restricts to a proper 5-coloring of each copy of \(H\), so each former \(\varphi\)-edge has differently colored endpoints. The retained unit edges also have differently colored endpoints. The restriction to the original terminal vertices would therefore be a proper 5-coloring of the 6-chromatic two-distance graph, a contradiction. Coincident nonterminal points or accidental additional unit distances can only add identifications or constraints; they do not invalidate the implication.

The same argument can be applied after scaling Parts' graph by \(1/\varphi\): a unit-distance gadget with terminals separated by \(1/\varphi\) and forced different would also yield a 6-chromatic unit-distance graph.

### Result of the test

`G510` contains exact pairs at both target separations, but the certificate proves that none is forced different. Therefore `G510`, and every subgraph obtained from it only by deletion, cannot supply this conversion gadget.

This is a genuine elimination of a concrete route, not a heuristic failure to find a coloring.

## 4. Upper-bound audit

A complete answer \(\chi(\mathbb{R}^2)=6\) would also require a coloring of every point of the plane with six colors, including a rigorous convention for all boundaries and exceptional points. No such coloring was obtained.

Recent work proving that seven colors are necessary for broad classes of map-type or polygonal colorings does not establish the unrestricted lower bound \(\chi(\mathbb{R}^2)\ge 7\). An arbitrary coloring need not have polygonal regions, locally finite boundaries, or any regularity at all.

Likewise, a 2026 result showing that the fractional chromatic number of the plane is strictly greater than 4 still implies only the integer lower bound 5, not 6.

## 5. Exact remaining alternatives

| Candidate value | What would still have to be proved |
|---|---|
| \(5\) | An explicit unrestricted 5-coloring of all of \(\mathbb{R}^2\). |
| \(6\) | A finite 6-chromatic unit-distance graph or equivalent lower-bound proof, and an unrestricted 6-coloring of the entire plane. |
| \(7\) | An unrestricted lower bound of 7, for example a finite 7-chromatic unit-distance graph. The classical 7-color upper bound is already available. |

The exact interval is therefore unchanged.

## 6. Most defensible next research step

The binary-gadget route inside `G510` is exhausted by theorem, not merely by sampling. The next useful search object is a relation on at least three terminals. A multi-terminal relation can remain nontrivial even when every projected pair is flexible.

A preliminary screen sampled all five equality patterns on independent triples:

- `AAA`: all three colors equal;
- `AAB`, `ABA`, `ABB`: exactly one unequal terminal in each position;
- `ABC`: all three colors different.

The sampling found many apparently missing patterns, but targeted contraction and inequality tests quickly produced explicit 5-colorings for hundreds of early candidates. No exact ternary obstruction survived. This exploratory stage is deliberately not stated as a theorem; the package includes the scanner and sample output only as a search record.

A serious continuation should therefore do one of the following:

1. exact SAT enumeration of three- and four-terminal color-partition relations in known 5-chromatic witnesses;
2. compositional search over those relations, rather than over isolated terminal pairs;
3. simultaneous geometric embedding and relation composition, with exact algebraic coordinates;
4. an independent upper-bound program that searches non-polygonal hierarchical or highly discontinuous six-color rules and verifies all displacement classes exactly.

## 7. Reproduction

From the package root:

```bash
python -m pip install -r requirements.txt
python verify_all.py
```

Expected output:

```text
VERIFIED
  vertices: 510; exact unit pairs/edges: 2504
  exact phi pairs: [(212, 490), (218, 491), (224, 489)]
  exact 1/phi pairs: [(212, 491), (218, 489), (224, 490)]
  certificate colorings: 84
  conclusion: every one of the 127291 nonedges is same-colored in at least one proper 5-coloring and differently colored in at least one other.
```

A second, independently implemented checker verifies the graph-coloring and pair-coverage portion:

```bash
g++ -O2 -std=c++17 verify_coloring.cpp -o verify_coloring
./verify_coloring data/510.edge certificates/colorings_84.csv
```

The Python verifier is the authoritative exact geometry checker. It uses rational arithmetic in the eight-dimensional basis

\[
1,\sqrt3,\sqrt5,\sqrt{15},\sqrt{11},\sqrt{33},\sqrt{55},\sqrt{165}.
\]

## 8. Scope and novelty

This package does **not** determine the Hadwiger-Nelson number and does **not** improve the interval \(5\le\chi(\mathbb{R}^2)\le7\).

The binary-flexibility theorem was derived and machine-certified in this run. No claim is made that it is absent from unpublished computations or the wider literature. Its value here is exact route elimination and a reusable certificate.

The certificate also does not independently prove that `G510` is non-4-colorable. That known role of the graph is separate from the theorem proved here. The present proof needs only the exact unit-distance realization and the supplied proper 5-colorings.

## 9. Sources and provenance

- The problem specification is preserved as `source_prompt.pdf`.
- `data/510.vtx` and `data/510.edge` were obtained from Marijn Heule's public `CNP-SAT` repository, directories `vtx/` and `edge/`.
- J. Parts, *A small 6-chromatic two-distance graph in the plane*, arXiv:2010.12656.
- G. Sokolov and V. Voronov, *On the chromatic number of the plane for map-type colorings*, arXiv:2502.01958.
- A. Dúcz and D. Varga, *A unit-distance graph in the plane with independence ratio below 1/4*, arXiv:2606.28157.
