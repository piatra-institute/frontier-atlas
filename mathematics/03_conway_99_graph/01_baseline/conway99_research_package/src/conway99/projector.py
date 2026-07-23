"""Integral-projector reformulation of the Conway-99 reduced problem.

For m=7, a valid reduced adjacency matrix B determines

    G = G0 + 15 B = 105 P,

where P is a rank-40 orthogonal projector supported in the fixed 70-dimensional
(-2)-eigenspace of the line graph L(K_{2,2,2,2,2,2,2}).  The fixed matrix G0
has diagonal 50 and five possible off-diagonal values determined only by the
relationship between the corresponding base edges.

Novelty warning: this formulation was reconstructed during the investigation,
but no claim of publication-level originality is made by this package.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
from numpy.typing import NDArray

from .model import BaseEdge, build_model, mate, part
from .verify import VerificationReport, matrix_sha256

IntMatrix = NDArray[np.int64]
RelationType = Literal[
    "overlap_mates",
    "overlap_distinct_parts",
    "disjoint_2_parts",
    "disjoint_3_parts",
    "disjoint_4_parts",
]

BASELINE_VALUES: dict[RelationType, int] = {
    "overlap_mates": -5,
    "overlap_distinct_parts": -6,
    "disjoint_2_parts": 0,
    "disjoint_3_parts": -1,
    "disjoint_4_parts": -2,
}


def relation_type(e: BaseEdge, f: BaseEdge) -> RelationType:
    """Classify a pair of distinct edges of K_{2,2,...,2}."""

    if e == f:
        raise ValueError("relation_type expects two distinct edges")
    intersection = set(e).intersection(f)
    if len(intersection) == 1:
        shared = next(iter(intersection))
        other_e = e[0] if e[1] == shared else e[1]
        other_f = f[0] if f[1] == shared else f[1]
        if mate(other_e) == other_f:
            return "overlap_mates"
        return "overlap_distinct_parts"
    if intersection:
        raise ValueError("base edges are malformed")

    part_count = len({part(vertex) for vertex in (*e, *f)})
    if part_count == 2:
        return "disjoint_2_parts"
    if part_count == 3:
        return "disjoint_3_parts"
    if part_count == 4:
        return "disjoint_4_parts"
    raise ValueError(f"unexpected part count {part_count}")


def baseline_G() -> IntMatrix:
    """Return the fixed integral matrix G0 for m=7."""

    model = build_model(7)
    q = model.second_layer_count
    G0 = np.zeros((q, q), dtype=np.int64)
    np.fill_diagonal(G0, 50)
    for i, e in enumerate(model.base_edges):
        for j in range(i + 1, q):
            f = model.base_edges[j]
            value = BASELINE_VALUES[relation_type(e, f)]
            G0[i, j] = value
            G0[j, i] = value
    return G0


def baseline_G_from_line_graph_polynomial() -> IntMatrix:
    """Independently construct G0 from the exact polynomial in the line graph.

    If R is the adjacency matrix of L(K_{2,2,...,2}), then

        G0 = (R - 10I)(R^2 - 30R - 184I) / 24.

    Exact divisibility by 24 is checked entrywise.
    """

    model = build_model(7)
    q = model.second_layer_count
    eye = np.eye(q, dtype=np.int64)
    R = model.M @ model.M.T - 2 * eye
    numerator = (R - 10 * eye) @ (R @ R - 30 * R - 184 * eye)
    if np.any(numerator % 24 != 0):
        raise ArithmeticError("line-graph polynomial was not integrally divisible by 24")
    return numerator // 24


def B_to_G(B: Any) -> IntMatrix:
    """Map a binary reduced adjacency matrix to its integral-projector matrix."""

    arr = np.asarray(B)
    if arr.shape != (84, 84):
        raise ValueError(f"B must have shape (84, 84), got {arr.shape}")
    if not np.issubdtype(arr.dtype, np.integer):
        if not np.all(np.isfinite(arr)) or not np.all(arr == np.rint(arr)):
            raise ValueError("B must be integral")
    return baseline_G() + 15 * arr.astype(np.int64, copy=False)


def G_to_B(G: Any) -> IntMatrix:
    """Recover B from G, rejecting entries outside the two-lift alphabet."""

    arr = np.asarray(G)
    if arr.shape != (84, 84):
        raise ValueError(f"G must have shape (84, 84), got {arr.shape}")
    if not np.issubdtype(arr.dtype, np.integer):
        if not np.all(np.isfinite(arr)) or not np.all(arr == np.rint(arr)):
            raise ValueError("G must be integral")
    delta = arr.astype(np.int64, copy=False) - baseline_G()
    if np.any(delta % 15 != 0):
        raise ValueError("G does not lie in the required residue class modulo 15")
    B = delta // 15
    if not np.all((B == 0) | (B == 1)):
        raise ValueError("G uses a lift outside {baseline, baseline+15}")
    return B


def verify_G(G: Any, verify_recovered_B: bool = True) -> VerificationReport:
    """Verify the exact integral-projector identities."""

    arr = np.asarray(G)
    checks: dict[str, bool] = {"shape": arr.shape == (84, 84)}
    if not checks["shape"]:
        return VerificationReport(False, checks, {"expected_shape": [84, 84]})
    if not np.issubdtype(arr.dtype, np.integer):
        checks["integer"] = bool(np.all(np.isfinite(arr)) and np.all(arr == np.rint(arr)))
        if not checks["integer"]:
            return VerificationReport(False, checks, {})
    arr = arr.astype(np.int64, copy=False)

    checks.update(
        {
            "symmetric": bool(np.array_equal(arr, arr.T)),
            "diagonal_50": bool(np.all(np.diag(arr) == 50)),
            "row_sums_0": bool(np.all(arr.sum(axis=1) == 0)),
            "projector_polynomial": bool(np.array_equal(arr @ arr, 105 * arr)),
            "trace_4200": int(np.trace(arr)) == 4200,
        }
    )

    recovered = None
    try:
        recovered = G_to_B(arr)
        checks["valid_entry_alphabet"] = True
    except ValueError:
        checks["valid_entry_alphabet"] = False

    if verify_recovered_B and recovered is not None:
        from .verify import verify_B

        checks["recovered_B_valid"] = verify_B(recovered, m=7, verify_full=True).valid

    metadata = {
        "sha256": matrix_sha256(arr),
        "implied_rank": 40 if checks["projector_polynomial"] and checks["trace_4200"] else None,
    }
    return VerificationReport(all(checks.values()), checks, metadata)
