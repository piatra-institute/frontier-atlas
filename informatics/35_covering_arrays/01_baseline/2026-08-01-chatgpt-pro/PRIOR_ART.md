# Prior-art check

Access date: 2026-08-01.

## Exact benchmark

The value reproduced here is already known:

- C. J. Colbourn, G. Kéri, P. P. Rivas Soriano, and J.-C. Schlage-Puchta, *Covering and Radius-covering Arrays: Constructions and Classification*, preprint dated 3 December 2019. Theorem 5.2 states \(\mathrm{CAN}(2,8,3)=13\), using a 13-row construction and exhaustive nonexistence of \(\mathrm{CA}(12;2,8,3)\). The same classification reports a unique \(\mathrm{CA}(12;2,7,3)\).
- Janne I. Kokkala, Karen Meagher, Reza Naserasr, Kari J. Nurmela, Patric R. J. Östergård, and Brett Stevens, *On the Structure of Small Strength-2 Covering Arrays*, Journal of Combinatorial Designs 28(1), 5-24 (2020), DOI 10.1002/jcd.21671. The work and associated dataset study exact small strength-2 cases by computational enumeration.

## Table status

The original Colbourn tables were discontinued in 2025 after Charles Colbourn's retirement and an Arizona State University website redesign. Ulrike Grömping's 2026 technical report identifies a preserved November 2024 snapshot as the latest available status known to the author. These tables are empirical upper-bound trackers: a row size is backed by a known construction, but the array itself is often not directly supplied.

The preserved November 2024 entries relevant to the exploratory branch are:

- strength 2, alphabet 3: 13 rows support at least 9 columns;
- strength 3, alphabet 3: the listed upper bounds are 39 rows for 7 columns and 42 rows for 8 columns.

## Status of this package

This package is P2 under the supplied grading scheme: it independently regenerates a known exact optimum with both certified halves. It does not claim a new bound.

The exploratory \(\mathrm{CAN}(3,7,3)\) work is explicitly non-load-bearing. It regenerated a valid 39-row array and did not find a 38-row array within the recorded search budget.

## Source locations

- https://www.mathematik.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Covering_array.pdf
- https://doi.org/10.1002/jcd.21671
- https://arxiv.org/abs/1901.03594
- https://github.com/ugroempi/CAs/blob/main/ColbournTables.md
- https://www1.beuth-hochschule.de/FB_II/reports/Report-2026-001.pdf
