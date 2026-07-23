#!/usr/bin/env python3
"""Generate independently verifiable small-instance examples."""

from __future__ import annotations

import json
from pathlib import Path

from conway99.opb import write_metadata, write_opb
from conway99.small_instances import m2_unique_solution
from conway99.verify import reconstruct_A, save_matrix_csv, verify_A, verify_B


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    examples = root / "examples"
    examples.mkdir(parents=True, exist_ok=True)

    B = m2_unique_solution()
    A = reconstruct_A(B, m=2)
    save_matrix_csv(B, examples / "m2_solution_B.csv")
    save_matrix_csv(A, examples / "m2_solution_A.csv")

    counts = write_opb(examples / "m2_case_1.opb", m=2, partition=(1,))
    write_metadata(examples / "m2_case_1.metadata.json", counts, partition=(1,))

    verification = {
        "B": verify_B(B, m=2).to_dict(),
        "A": verify_A(A, m=2).to_dict(),
    }
    (examples / "m2_verification.json").write_text(
        json.dumps(verification, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
