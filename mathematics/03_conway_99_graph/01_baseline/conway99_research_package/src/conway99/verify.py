"""Independent exact verifiers for reduced and full adjacency matrices."""

from __future__ import annotations

import csv
import hashlib
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import numpy as np
from numpy.typing import NDArray

from .model import ModelData, build_model

IntMatrix = NDArray[np.int64]


@dataclass(frozen=True)
class VerificationReport:
    """Machine-readable verification result."""

    valid: bool
    checks: dict[str, bool]
    metadata: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _as_int_matrix(matrix: Any) -> IntMatrix:
    arr = np.asarray(matrix)
    if arr.ndim != 2:
        raise ValueError("matrix must be two-dimensional")
    if not np.issubdtype(arr.dtype, np.integer):
        # Permit exactly integral floating-point input, but reject silent rounding.
        if not np.all(np.isfinite(arr)) or not np.all(arr == np.rint(arr)):
            raise ValueError("matrix entries must be exact integers")
    return arr.astype(np.int64, copy=False)


def matrix_sha256(matrix: Any) -> str:
    """Hash a matrix using a stable shape + little-endian int64 representation."""

    arr = _as_int_matrix(matrix)
    header = f"{arr.shape[0]}x{arr.shape[1]}\n".encode("ascii")
    payload = np.asarray(arr, dtype="<i8", order="C").tobytes(order="C")
    return hashlib.sha256(header + payload).hexdigest()


def reconstruct_A(B: Any, m: int = 7) -> IntMatrix:
    """Reconstruct the full adjacency matrix from a reduced matrix ``B``."""

    model = build_model(m)
    B_arr = _as_int_matrix(B)
    q = model.second_layer_count
    if B_arr.shape != (q, q):
        raise ValueError(f"B must have shape {(q, q)}, got {B_arr.shape}")

    v = model.full_vertex_count
    n = model.base_vertex_count
    A = np.zeros((v, v), dtype=np.int64)

    # Vertex order: fixed vertex x; its n neighbors; the q distance-two vertices.
    A[0, 1 : 1 + n] = 1
    A[1 : 1 + n, 0] = 1
    A[1 : 1 + n, 1 : 1 + n] = model.L
    A[1 : 1 + n, 1 + n :] = model.M.T
    A[1 + n :, 1 : 1 + n] = model.M
    A[1 + n :, 1 + n :] = B_arr
    return A


def verify_A(A: Any, m: int = 7) -> VerificationReport:
    """Verify all strongly-regular conditions in exact integer arithmetic."""

    model = build_model(m)
    expected_shape = (model.full_vertex_count, model.full_vertex_count)

    try:
        arr = _as_int_matrix(A)
    except ValueError:
        return VerificationReport(False, {"integer_matrix": False}, {"expected_shape": expected_shape})

    checks: dict[str, bool] = {
        "shape": arr.shape == expected_shape,
    }
    if not checks["shape"]:
        return VerificationReport(False, checks, {"expected_shape": expected_shape, "actual_shape": arr.shape})

    checks.update(
        {
            "binary": bool(np.all((arr == 0) | (arr == 1))),
            "symmetric": bool(np.array_equal(arr, arr.T)),
            "zero_diagonal": bool(np.all(np.diag(arr) == 0)),
            "row_sums": bool(np.all(arr.sum(axis=1) == model.degree)),
        }
    )

    eye = np.eye(model.full_vertex_count, dtype=np.int64)
    ones = np.ones(expected_shape, dtype=np.int64)
    rhs = (model.degree - 2) * eye - arr + 2 * ones
    square = arr @ arr
    checks["srg_matrix_equation"] = bool(np.array_equal(square, rhs))

    # Redundant entrywise audit, deliberately separate from the matrix equality.
    off_diagonal = ~np.eye(model.full_vertex_count, dtype=bool)
    adjacent = (arr == 1) & off_diagonal
    nonadjacent = (arr == 0) & off_diagonal
    checks["adjacent_common_neighbors_1"] = bool(np.all(square[adjacent] == 1))
    checks["nonadjacent_common_neighbors_2"] = bool(np.all(square[nonadjacent] == 2))

    return VerificationReport(
        valid=all(checks.values()),
        checks=checks,
        metadata={
            "m": m,
            "parameters": [model.full_vertex_count, model.degree, 1, 2],
            "sha256": matrix_sha256(arr),
        },
    )


def verify_B(B: Any, m: int = 7, verify_full: bool = True) -> VerificationReport:
    """Verify the reduced equations and, optionally, the reconstructed graph."""

    model = build_model(m)
    q = model.second_layer_count
    expected_shape = (q, q)

    try:
        arr = _as_int_matrix(B)
    except ValueError:
        return VerificationReport(False, {"integer_matrix": False}, {"expected_shape": expected_shape})

    checks: dict[str, bool] = {"shape": arr.shape == expected_shape}
    if not checks["shape"]:
        return VerificationReport(False, checks, {"expected_shape": expected_shape, "actual_shape": arr.shape})

    checks.update(
        {
            "binary": bool(np.all((arr == 0) | (arr == 1))),
            "symmetric": bool(np.array_equal(arr, arr.T)),
            "zero_diagonal": bool(np.all(np.diag(arr) == 0)),
            "row_sums": bool(np.all(arr.sum(axis=1) == model.b_degree)),
            "BM_equals_MT": bool(np.array_equal(arr @ model.M, model.M @ model.T)),
        }
    )

    eye = np.eye(q, dtype=np.int64)
    ones = np.ones((q, q), dtype=np.int64)
    rhs_b2 = model.b_degree * eye - arr - model.M @ model.M.T + 2 * ones
    checks["B_quadratic_equation"] = bool(np.array_equal(arr @ arr, rhs_b2))

    full_report: VerificationReport | None = None
    if verify_full:
        full_report = verify_A(reconstruct_A(arr, m=m), m=m)
        checks["reconstructed_A_valid"] = full_report.valid

    metadata: dict[str, Any] = {
        "m": m,
        "shape": list(arr.shape),
        "sha256": matrix_sha256(arr),
    }
    if full_report is not None:
        metadata["reconstructed_A"] = full_report.to_dict()

    return VerificationReport(all(checks.values()), checks, metadata)


def load_matrix(path: str | Path) -> IntMatrix:
    """Load a matrix from .npy, CSV, or whitespace-delimited text."""

    file_path = Path(path)
    suffix = file_path.suffix.lower()
    if suffix == ".npy":
        return _as_int_matrix(np.load(file_path, allow_pickle=False))
    if suffix == ".csv":
        return _as_int_matrix(np.loadtxt(file_path, delimiter=",", dtype=np.int64))
    return _as_int_matrix(np.loadtxt(file_path, dtype=np.int64))


def save_matrix_csv(matrix: Any, path: str | Path) -> None:
    """Write an integer matrix as deterministic comma-separated rows."""

    arr = _as_int_matrix(matrix)
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerows(arr.tolist())


def rank_mod_p(matrix: Any, p: int) -> int:
    """Compute matrix rank over the prime field F_p by exact elimination."""

    if p < 2:
        raise ValueError("p must be at least 2")
    # This routine assumes p is prime; primality is intentionally not hidden.
    A = np.mod(_as_int_matrix(matrix), p).astype(object)
    rows, cols = A.shape
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if int(A[r, col]) % p), None)
        if pivot is None:
            continue
        if pivot != rank:
            A[[rank, pivot]] = A[[pivot, rank]]
        inv = pow(int(A[rank, col]) % p, -1, p)
        A[rank, :] = [(int(value) * inv) % p for value in A[rank, :]]
        for r in range(rows):
            if r == rank:
                continue
            factor = int(A[r, col]) % p
            if factor:
                A[r, :] = [
                    (int(A[r, c]) - factor * int(A[rank, c])) % p
                    for c in range(cols)
                ]
        rank += 1
        if rank == rows:
            break
    return rank
