# Verification log

All checks below completed successfully on 20 July 2026.

## Exact one-vertex extensions

Independent Python DRUP replay, four ranges:

```text
[0,82):    VERIFIED, 82 graphs,  9,548 additions
[82,164):  VERIFIED, 82 graphs,  9,779 additions
[164,246): VERIFIED, 82 graphs,  9,383 additions
[246,328): VERIFIED, 82 graphs,  9,003 additions
TOTAL:     VERIFIED, 328 graphs, 37,713 additions
```

A separate custom exhaustive DPLL implementation also returned UNSAT for every instance:

```text
DPLL nodes:        441,990
Unit propagations: 2,464,913
Extensions found:  0
```

## Extensions with at most one bad K5

Independent C++ DRUP replay:

```text
[0,164):   VERIFIED, 164 graphs, 278,864 additions
[164,328): VERIFIED, 164 graphs, 275,747 additions
TOTAL:     VERIFIED, 328 graphs, 554,611 additions
```

## Extensions with at most two bad K5s

Indices 41 and 255 are SAT and have direct two-violation witnesses. All other representatives are UNSAT.

Independent C++ DRUP replay:

```text
[0,82):    VERIFIED, 81 UNSAT graphs, 417,553 additions
[82,164):  VERIFIED, 82 UNSAT graphs, 407,880 additions
[164,246): VERIFIED, 82 UNSAT graphs, 423,287 additions
[246,328): VERIFIED, 81 UNSAT graphs, 435,311 additions
TOTAL:     VERIFIED, 326 UNSAT graphs, 1,684,031 additions
```

The four projected SAT extensions, two from each base representative, were exhaustively blocked and reduced by exact graph isomorphism to two unlabeled classes.

## Hamming-radius exclusion around near-miss Graph 1

Independent C++ DRUP replay:

```text
radius 1: VERIFIED,     21 additions,     16,478 base clauses
radius 2: VERIFIED,    257 additions,     85,576 base clauses
radius 3: VERIFIED,  1,210 additions,    299,290 base clauses
radius 4: VERIFIED,  8,039 additions,    715,454 base clauses
radius 5: VERIFIED, 30,366 additions,  1,227,766 base clauses
```

The radius-5 proof was replayed in seven composable ranges because the execution harness limits individual processes. Every range passed; prior verified additions were retained when checking later ranges.

## Input integrity

```text
r55_42some.g6 SHA-256:
067902e853d87b49bcef0d1d4c0e3bbadd238ee18bc65341b079a3ca4780eccb

input_prompt.pdf SHA-256:
2a9397490f0285362cfbd32d220465ad2afa3d3212a11866261ef3b3d24ebed4
```
