Worked for 93m 8s

# Certified result

$$
\boxed{\mathrm{CAN}(2,8,3)=13}
$$

I completed a **P2 certified reproduction of a known exact value**:

$$
\mathrm{CA}(13;2,8,3)\text{ exists}, \qquad \mathrm{CA}(12;2,8,3)\text{ does not exist}.
$$

This is not a new covering-array number. Colbourn, Kéri, Rivas Soriano, and Schlage-Puchta previously established the same value as Theorem 5.2 through construction and exhaustive classification; later work by Kokkala and collaborators also studied these small strength-2 arrays computationally. [![](https://www.google.com/s2/favicons?domain=https://www.mathematik.uni-rostock.de&sz=128)University of Rostock Mathematics+1](https://www.mathematik.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Covering_array.pdf)

## What was independently established

| Certificate half | Result | Verification |
| --- | --- | --- |
| Upper bound | $\mathrm{CAN}(2,8,3)\le13$ | Explicit $13\times8$ ternary array |
| Column pairs checked | $28$ | All $\binom82$ pairs |
| Required interactions | $252$ | $28\times9$ ordered symbol pairs |
| Observed multiplicities | $1$ to $3$ | No interaction missing |
| Lower bound | $\mathrm{CAN}(2,8,3)\ge13$ | Complete normalized enumeration |
| Initial multiplicity matrices | $165$ | All positive $3\times3$ matrices summing to $12$ |
| Symmetry orbits | $7$ | Under two symbol permutations and transposition |
| Canonical candidate columns | $4{,}008$ total | Independently regenerated |
| Compatibility edges | $164{,}043$ total | Independently regenerated |
| Largest possible additional-column clique | $5$ | Six are required |
| Final status | **Exact optimum** | Both halves pass |

## Lower-bound argument

For any hypothetical $\mathrm{CA}(12;2,8,3)$, fix two columns $c_0,c_1$. Their ordered-pair multiplicity matrix $M=(m_{ij})$ satisfies

$$
m_{ij}\ge1,\qquad \sum_{i,j}m_{ij}=12.
$$

Therefore $M$ is the all-one $3\times3$ matrix plus three distributed units. There are exactly

$$
\binom{11}{8}=165
$$

such labelled matrices, reducing to seven canonical symmetry cases.

For each case, every possible additional ternary column was exhaustively generated and retained when it covered all nine pairs with both $c_0$ and $c_1$. A compatibility graph was then constructed:

-   vertices are admissible additional columns;

-   two vertices are adjacent when their columns jointly realize all nine ordered symbol pairs.


An eight-column array would require six additional columns beyond $c_0,c_1$, hence a $K_6$ in one of these graphs. Exact exhaustive clique enumeration gave:

$$
\omega(G_0),\ldots,\omega(G_6) = 2,3,3,3,3,4,5.
$$

No $K_6$ exists, so no $\mathrm{CA}(12;2,8,3)$ exists.

## Independent-check architecture

The generator and verifier do not repeat the same implementation:

-   **C++ generator:** recursive restricted-growth generation, bitset graphs, fixed-size clique enumeration.

-   **Python verifier:** decodes all $3^{12}=531{,}441$ ternary words, independently canonicalizes them, reconstructs every graph, and uses Bron–Kerbosch maximal-clique enumeration.

-   **Coverage scanner 1:** Python tuple-set implementation.

-   **Coverage scanner 2:** separately written C++ 9-bit-mask implementation.


The complete replay ended with:

```
```
lower_bound=CAN(2,8,3)>=13
result=PASS
ALL_CHECKS_PASS
```
```

No floating-point result is load-bearing. The construction search used simulated annealing, but the resulting array is accepted solely because both exhaustive coverage scanners pass.

The lower half is a **completed symmetry-normalized exhaustive enumeration**, not a DRAT/LRAT trace and not a global classification of all isomorphism classes. Any remaining duplicate representations only enlarge the search and cannot produce a false nonexistence result.

## Exploratory frontier attempt

I also tested the neighboring cell $\mathrm{CAN}(3,7,3)$. The preserved November 2024 Colbourn-table snapshot lists a 39-row upper bound for seven ternary columns. The original Colbourn tables were discontinued in 2025, with the November 2024 snapshot identified in a 2026 technical report as the latest available status known to its author. [![](https://www.google.com/s2/favicons?domain=https://www.data2intelligence.de&sz=128)data2intelligence.de+2![](https://www.google.com/s2/favicons?domain=https://www1.beuth-hochschule.de&sz=128)www1.beuth-hochschule.de+2](https://www.data2intelligence.de/ColbournTables/t3v3.html)

The new search implementation:

-   regenerated a valid $\mathrm{CA}(39;3,7,3)$ in $0.607$ seconds;

-   ran six recorded $N=38$ attempts;

-   reached states with only five uncovered interactions;

-   did **not** find a valid 38-row array.


No $N=38$ bound claim is made.

## Artifacts

Download the complete certified package

Download the SHA-256 sidecar

```
```
c4584ffc28f86bd61f324abd866cef6aecbce6af52bf7d7267d3b6db0bdb0cd2
```
```

Direct audit surfaces:

-   CLAIM.md

-   PROOF\_NOTE.md

-   array\_CA\_13\_2\_8\_3.csv

-   lower\_bound\_summary.json

-   Immutable artifact manifest


Reverification requires:

```
Bash

```
unzip CAN_2_8_3_certified_reproduction.zip
cd covering_array_CAN_2_8_3_certified
./verify_all.sh
```
```

Full regeneration from source:

```
Bash

```
./reproduce.sh
```
```

CLAIM.mdDocumentOpen file

PROOF\_NOTE.mdDocumentOpen file

array\_CA\_13\_2\_8\_3.csvSpreadsheetOpen file

lower\_bound\_summary.jsonCodeOpen file

Show less

![](https://www.google.com/s2/favicons?domain=https://www.data2intelligence.de&sz=32)

![](https://www.google.com/s2/favicons?domain=https://research.aalto.fi&sz=32)

![](https://www.google.com/s2/favicons?domain=https://www.mathematik.uni-rostock.de&sz=32)

Sources
