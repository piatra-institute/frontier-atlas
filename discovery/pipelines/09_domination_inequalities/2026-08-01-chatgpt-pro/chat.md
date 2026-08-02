Worked for 96m 26s

# Reframed task

> Audit the current status of TxGraffiti’s domination-related conjectures; test every genuinely unresolved statement using exact methods on all connected unlabeled graphs through order $9$; extend the search to adversarial graph families; independently verify every candidate counterexample; and report either certified graph6 violators or quantitatively hardened survivors.

# Result

**No independently verified counterexample was found to a TxGraffiti conjecture that I could confirm as currently unresolved.**

The strongest live target I found,

$$
\gamma_t(G\square H)\ge \gamma(G\times H),
$$

survived **10,153 exhaustive factor pairs** and **102 additional structured-family pairs**.

The regular-graph conjecture

$$
i(G)\le \mu^*(G)
$$

also survived all searches here, including 5,000 constructed cubic graphs of order $60$. However, a late-July 2026 public post claims a counterexample exists. Because that post did not expose a graph6 witness or independently checkable certificate to this session, its status is best recorded as **“claimed refuted; independently unverified,” not “confirmed open.”**

The secondary synthetic generator did produce clean refutations: **37 of 59 fitted inequalities broke**, including two particularly simple order-$8$ tree witnesses given below.

---

## 1\. TxGraffiti status audit

The four conjectures advertised as open in the 2025 *In Reverie Together* paper are no longer a reliable live-open list as of 2 August 2026. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/html/2507.17780v1?utm_source=chatgpt.com)

### Product domination conjecture — apparently open

For connected $G,H$, both of order at least two,

$$
\boxed{\gamma_t(G\square H)\ge \gamma(G\times H)}.
$$

This appears as Conjecture 3 in the May 2026 TxGraffiti software paper. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+1](https://arxiv.org/pdf/2409.19379)

I found no later proof or counterexample in exact-phrase and arXiv searches. That is evidence of apparent openness, not a formal guarantee that no resolution exists.

### Regular independent-domination conjecture — status disputed

For every nontrivial regular graph,

$$
\boxed{i(G)\le \mu^*(G)},
$$

where $\mu^*(G)$ is the saturation number, the minimum size of a maximal matching. This is explicitly stated as TxGraffiti Conjecture 1. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+1](https://arxiv.org/pdf/1909.09093)

A public post now claims a connected cubic counterexample of order $60$ and girth $5$, with $i(G)>\mu^*(G)$. [![](https://www.google.com/s2/favicons?domain=https://x.com&sz=128)X (formerly Twitter)](https://x.com/PolygonWindow1/status/2080473679641837821?utm_source=chatgpt.com) The post did not yield an accessible graph encoding or certificate here, so I could neither reproduce nor refute that claim.

### Targets removed before testing

-   The annihilation–residue inequality

    $$
    \Delta(G)\alpha(G)\ge a(G)+R(G)
    $$

    has been proved for connected graphs with $\Delta\ge2$; $K_2$ is the exception to the original unrestricted wording. It was therefore not treated as open. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+1](https://arxiv.org/abs/2606.29553?utm_source=chatgpt.com)

-   The saturation–harmonic inequality

    $$
    \mu^*(G)\le H(G)
    $$

    is false. The friendship graph $F_4$ is a smallest counterexample:

    $$
    \mu^*(F_4)=4>\frac{18}{5}=H(F_4).
    $$

    The ratio can be made arbitrarily large. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+1](https://arxiv.org/pdf/2606.15761)

-   The zero-forcing conjecture $Z(G)\le\alpha(G)+1$ for subcubic/cubic graphs was refuted in July 2026. It is also outside the requested invariant panel. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/abs/2607.23664)


---

# 2\. Exact enumeration and invariant panel

## Exhaustive corpus

All **273,193 connected unlabeled graphs** through $n=9$ were processed:

| $n$ | Graphs |
| --- | --- |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 6 |
| 5 | 21 |
| 6 | 112 |
| 7 | 853 |
| 8 | 11,117 |
| 9 | 261,080 |

For every graph, the primary solver computed:

$$
\gamma,\quad \gamma_t,\quad i,\quad \gamma_c,\quad \gamma_R,\quad \gamma_{\mathrm{paired}},\quad \alpha,\quad \tau,\quad \mu^*,
$$

along with $n,m,\Delta,\delta$, tree/regular predicates, and optimal witnesses. Total and paired domination were evaluated only where their definitions apply; $K_1$ was retained for the ordinary invariants.

The optimized C++ sweep took **2.21 seconds** on the session hardware.

### Independent audit

A definition-by-definition second implementation recomputed every invariant on:

-   all 996 connected graphs through $n=7$;

-   100 deterministic graphs of order $8$;

-   100 deterministic graphs of order $9$.


Thus, **1,196 full-panel graphs** received a second-method audit. Results:

-   value mismatches: **0**;

-   invalid stored certificates: **0**;

-   Roman domination used explicit ternary label enumeration;

-   $\mu^*$ used a separate binary edge ILP;

-   all other invariants used direct cardinality-ordered subset searches.


The full $n=8,9$ corpus did not receive this second-method recomputation; every reported extremal candidate and counterexample did.

As the one classical engine sanity check, Ore’s bound

$$
\gamma(G)\le \frac n2
$$

for connected $n\ge2$ produced no violation and attained equality.

---

# 3\. Priority conjecture results

## 3.1 Product domination: hardened survivor

The exact sweep used every connected factor graph of orders $2$ through $6$:

-   factors: **142**;

-   unordered pairs: **10,153**;

-   largest product order: $36$;

-   violations: **0**;

-   equalities: **766**;

-   minimum slack:

    $$
    \gamma_t(G\square H)-\gamma(G\times H)=0;
    $$

-   maximum observed slack: $6$.


Slack distribution:

| Slack | Pairs |
| --- | --- |
| 0 | 766 |
| 1 | 1,494 |
| 2 | 4,488 |
| 3 | 1,933 |
| 4 | 1,427 |
| 5 | 21 |
| 6 | 24 |

The primary method was a cardinality-ordered exact set-cover branch-and-bound solver. It establishes optimality by proving infeasibility at every smaller cardinality.

A binary ILP independently recomputed **765 pairs**:

-   all 465 pairs whose factors have order at most $5$;

-   300 deterministic pairs involving an order-$6$ factor.


Agreements: **765/765**.

### Structured-factor extension

An additional curated battery used 34 factors from all requested adversarial classes and three small connected core factors:

-   factor–core pairs: **102**;

-   product order: at most $54$;

-   violations: **0**;

-   equalities: **58**;

-   minimum slack: $0$;

-   independent ILP cross-checks: **45/45 agreed**.


This included coronas, spiders, complete multipartite graphs, generalized Petersen graphs, Kneser graphs, grids, tori, random cubic graphs, and caterpillars.

**Conclusion:** the conjecture is substantially hardened through factor order $6$, but this is not a proof.

---

## 3.2 Regular $i(G)\le\mu^*(G)$: no recovered counterexample

The following exact tests found no violation:

| Corpus | Graphs tested | Result |
| --- | --- | --- |
| All nontrivial connected regular graphs through $n=9$ | 54 | No violation |
| Graph6-distinct regular members of the family battery | 157 | No violation |
| Constructed connected cubic, girth-$5$, order-$60$ instances | 5,000 generated | No violation |

For the first two corpora, $i$ and $\mu^*$ were independently recomputed by separate ILPs:

-   $i$: binary vertex model enforcing independence and domination;

-   $\mu^*$: binary edge model enforcing matching and maximality.


Agreements: **211/211**; certificate failures: **0**.

### Order-$60$ structured search

Every generated graph had a certified maximal matching of size $18$. For a cubic graph of order $n$, a maximal matching of size $k$ satisfies

$$
3(n-2k)\le4k,
$$

because unmatched vertices form an independent set. Hence

$$
k\ge\left\lceil\frac{3n}{10}\right\rceil.
$$

At $n=60$, this gives $\mu^*\ge18$. The constructed matching proves $\mu^*=18$.

Observed independent domination numbers:

| $i(G)$ | Instances |
| --- | --- |
| 16 | 2,122 |
| 17 | 2,878 |
| $\ge18$ | 0 |

The strongest instance had

$$
i(G)=17,\qquad \mu^*(G)=18.
$$

An independent branch-and-bound verifier proved that no independent dominating set of size $16$ exists and returned the following size-$17$ optimum:

$$
\{0,11,13,14,17,18,19,22,28,29,30,32,34,39,43,48,51\}.
$$

This search covers a deliberately extremal structured subclass; it is **not** an enumeration of all cubic order-$60$, girth-$5$ graphs. Consequently, it does not settle the public counterexample claim.

---

## 3.3 Subquartic harmonic refinement

After refuting the unrestricted harmonic-index conjecture, the same paper proposed:

$$
\boxed{\Delta(G)\le4\quad\Longrightarrow\quad\mu^*(G)\le H(G)}.
$$

This is a new human refinement rather than one of the original machine targets. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+1](https://arxiv.org/pdf/2606.15761)

Exact rational-arithmetic tests found:

-   connected graphs through $n=9$ with $\Delta\le4$: **14,597**;

-   structured family graphs through order $18$ with $\Delta\le4$: **766**;

-   violations: **0**;

-   minimum slack: $0$.


The paper itself reports a broader unrestricted enumeration through order $11$; the value added here is integration with the independent exact checker and the structured-family battery.

---

# 4\. Adversarial family battery

The generator produced **4,044 raw constructions**, deduplicated by graph6 to **3,456 connected graphs** of orders $2$ through $18$.

Membership counts overlap because some graphs belong to several families:

| Family | Memberships |
| --- | --- |
| Coronas $G\circ K_1$ | 142 |
| Spiders | 1,122 |
| Complete multipartite | 1,578 |
| Generalized Petersen | 14 |
| Kneser | 2 |
| Grid products | 13 |
| Torus products | 5 |
| Random cubic | 108 |
| Caterpillars | 622 |

The full domination panel was computed exactly on every deduplicated graph.

Observed ratio extremes included

$$
\max\frac{\gamma_t}{\gamma}=2,\qquad \max\frac{i}{\gamma}=4.5.
$$

---

# 5\. Synthetic generator: explicit refutations

The generator fitted affine $\gamma$\-versus-invariant inequalities and the ratios $\gamma_t/\gamma$ and $i/\gamma$ on the 995 nontrivial connected graphs through $n=7$.

Results:

| Outcome | Candidates |
| --- | --- |
| Raw fitted candidates | 59 |
| Affine candidates | 57 |
| Ratio candidates | 2 |
| Broken on $n=8,9$ | 33 |
| Survived $n=8,9$, broken by families | 4 |
| Raw survivors | 22 |
| Rediscovered classical candidate removed | 1 |
| Remaining unclassified survivors | 21 |

The remaining 21 are **not claimed to be novel**: comprehensive literature de-duplication was not completed.

## Counterexample A: affine domination bound

Fitted candidate:

$$
\boxed{3\gamma(G)\le n(G)+\Delta(G)}.
$$

Graph6:

```
```
G?`DE_
```
```

Decoded graph:

$$
n=8,\quad m=7,\quad \Delta=3,
$$

with edges

$$
\{(0,4),(0,6),(0,7),(1,5),(1,7),(2,6),(3,7)\}.
$$

It is a tree. An optimal dominating set is

$$
D=\{0,1,2,3\}, \qquad \gamma(G)=4.
$$

Therefore,

$$
3\gamma(G)=12>11=n+\Delta.
$$

The independent verifier exhaustively rejected every subset of size at most $3$.

## Counterexample B: independent-domination ratio

Fitted candidate:

$$
\boxed{2i(G)\le3\gamma(G)}.
$$

Graph6:

```
```
G??F?{
```
```

This is the balanced double star with edges

$$
\{(0,6),(1,6),(2,6),(3,7),(4,7),(5,7),(6,7)\}.
$$

Exact values and witnesses:

$$
\gamma(G)=2,\qquad D=\{6,7\},
$$

and

$$
i(G)=4,\qquad I=\{0,1,2,7\}.
$$

Thus,

$$
2i(G)=8>6=3\gamma(G).
$$

The verifier independently checked that $I$ is independent and dominating and proved that no independent dominating set of size at most $3$ exists.

All vertex sets above use zero-based labels in the decoded graph6 order.

---

# 6\. Verification discipline

The computations used the following separation of roles:

1.  **Generator/primary solver**

    -   optimized bit-mask enumeration for the full small-graph panel;

    -   exact set-cover branch-and-bound for products;

    -   cardinality-ordered searches, so optimality includes explicit infeasibility below the reported optimum.

2.  **Independent verifier**

    -   binary vertex or edge ILPs using separate formulations;

    -   direct combination searches for small graphs;

    -   explicit ternary Roman labels;

    -   an independently written C++ branch-and-bound verifier for the order-$60$ independent-domination certificate.

3.  **Witness validation**

    -   every displayed set was checked directly against the decoded graph;

    -   every displayed optimum was recomputed independently;

    -   every displayed counterexample includes a “no smaller feasible set” certificate.


---

# 7\. Incomplete scope

-   **Order $10$ was not enumerated.** The connected corpus contains 11,716,571 graphs. [![](https://www.google.com/s2/favicons?domain=https://users.cecs.anu.edu.au&sz=128)ANU CECS Users](https://users.cecs.anu.edu.au/~bdm/data/graphs.html) The exact engine remained fast at order $9$, but the sandbox did not contain `geng`, and the order-$10$ corpus could not be downloaded into the code environment during the run. Thus, this was an input-generation limitation rather than a demonstrated solver limit.

-   The claimed order-$60$ regular counterexample was not independently recovered because no machine-readable graph was accessible.

-   The product conjecture’s “apparently open” status is based on a literature search, not an authoritative continuously updated registry.

-   Mixed zero-forcing/domination conjectures were not implemented because zero forcing was outside the requested invariant panel.

-   The full $n=8,9$ corpus used one exhaustive engine plus sampled second-method auditing. Every actual witness or extremal candidate received the requested independent recomputation.


---

# 8\. Reproducible artifacts

| Artifact | Contents |
| --- | --- |
| panel.csv | All 273,193 graphs and complete invariant panel |
| exhaustive\_summary.json | Counts, timings, validation result |
| sweep.cpp | Exact bit-mask panel implementation |
| panel\_second\_method\_crosscheck\_summary.json | 1,196-graph independent audit |
| panel\_second\_method\_crosscheck.csv | Per-graph comparison |
| family\_panel.csv | Exact invariants for 3,456 family graphs |
| family\_summary.json | Family counts and extrema |
| family\_metadata.csv | Construction names and graph6 encodings |
| product\_txgraffiti\_n6\_summary.json | Complete factor-order-$6$ result |
| product\_txgraffiti\_n6\_complete.csv | All 10,153 product pairs and witnesses |
| product\_ilp\_crosscheck.csv | 765 independent recomputations |
| product\_structured\_families\_summary.json | Adversarial-family product battery |
| regular\_ilp\_crosscheck.csv | Exact $i$ and $\mu^*$ verification |
| Order-60 survivor graph6 | Best structured regular instance |
| structured60\_certificate.json | Graph checks, $i=17$, $\mu^*=18$, witnesses |
| structured60\_best\_bb\_k16.txt | Independent lower certificate for $i$ |
| structured60\_best\_bb\_k17.txt | Independent optimum witness |
| subquartic\_harmonic\_test.csv | Exact rational harmonic-index checks |
| synthetic\_candidates.csv | All 59 fitted candidates and outcomes |
| synthetic\_witness\_certificates.json | Independent verification details |
| Affine counterexample graph6 | Witness for $3\gamma\le n+\Delta$ |
| Ratio counterexample graph6 | Witness for $2i\le3\gamma$ |

## Essential takeaways

1.  **No independently certified real-open TxGraffiti refutation emerged.**

2.  **The product domination conjecture survived 10,255 exact product tests**, including exhaustive factors through order $6$.

3.  **The regular independent-domination target survived every reproducible test**, but a public counterexample claim prevents confidently labeling it open.

4.  **The synthetic phase produced 37 refuted fits**, with two minimal, independently certified order-$8$ tree witnesses.

5.  **Order $10$ remains the principal missing exhaustive layer.**


panel.csvSpreadsheetOpen file

exhaustive\_summary.jsonCodeOpen file

sweep.cppCodeOpen file

panel\_second\_method\_crosscheck\_summary.jsonCodeOpen file

panel\_second\_method\_crosscheck.csvSpreadsheetOpen file

family\_panel.csvSpreadsheetOpen file

family\_summary.jsonCodeOpen file

family\_metadata.csvSpreadsheetOpen file

product\_txgraffiti\_n6\_summary.jsonCodeOpen file

product\_txgraffiti\_n6\_complete.csvSpreadsheetOpen file

product\_ilp\_crosscheck.csvSpreadsheetOpen file

product\_structured\_families\_summary.jsonCodeOpen file

regular\_ilp\_crosscheck.csvSpreadsheetOpen file

structured60\_certificate.jsonCodeOpen file

structured60\_best\_bb\_k16.txtDocumentOpen file

structured60\_best\_bb\_k17.txtDocumentOpen file

subquartic\_harmonic\_test.csvSpreadsheetOpen file

synthetic\_candidates.csvSpreadsheetOpen file

synthetic\_witness\_certificates.jsonCodeOpen file

Show less

![](https://www.google.com/s2/favicons?domain=https://users.cecs.anu.edu.au&sz=32)

![](https://www.google.com/s2/favicons?domain=https://x.com&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

Sources
