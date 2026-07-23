#!/usr/bin/env python3
"""Run deterministic mathematical audits and write machine-readable results."""

from __future__ import annotations

import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from conway99.model import build_model, validate_model_identities
from conway99.opb import encoding_counts
from conway99.orbits import build_case_records, signature_counts
from conway99.projector import baseline_G, baseline_G_from_line_graph_polynomial
from conway99.small_instances import m2_unique_solution, spectral_feasibility
from conway99.verify import reconstruct_A, verify_A, verify_B


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    results = root / "results"
    results.mkdir(parents=True, exist_ok=True)

    model = build_model(7)
    B2 = m2_unique_solution()
    A2 = reconstruct_A(B2, m=2)
    case_records = build_case_records(7)
    counts = signature_counts(7)
    projector_agrees = np.array_equal(
        baseline_G(), baseline_G_from_line_graph_polynomial()
    )

    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "software": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "resolution_status": "UNRESOLVED",
        "statement": "No srg(99,14,1,2) adjacency matrix or complete nonexistence certificate is included.",
        "conway_model": {
            "base_vertices": model.base_vertex_count,
            "second_layer_vertices": model.second_layer_count,
            "full_vertices": model.full_vertex_count,
            "degree": model.degree,
            "identities": validate_model_identities(model),
        },
        "small_instance_audit": {
            "m2_B": verify_B(B2, m=2).to_dict(),
            "m2_A": verify_A(A2, m=2).to_dict(),
            "m2_spectral": spectral_feasibility(2),
            "m3_spectral": spectral_feasibility(3),
            "m7_spectral": spectral_feasibility(7),
        },
        "normalization_audit": {
            "case_count": len(case_records),
            "labeled_matching_count": sum(counts.values()),
            "signature_counts": {
                "+".join(map(str, signature)): count
                for signature, count in sorted(counts.items(), reverse=True)
            },
            "cases": case_records,
        },
        "projector_audit": {
            "relation_construction_equals_line_graph_polynomial": projector_agrees,
            "baseline_diagonal": sorted(set(np.diag(baseline_G()).tolist())),
        },
        "full_case_encoding_counts": encoding_counts(7, with_case=True).to_dict(),
    }

    (results / "audit.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "Conway-99 reconstructed research package audit",
        "===============================================",
        f"Resolution status: {payload['resolution_status']}",
        payload["statement"],
        "",
        f"Fixed-vertex model identities all pass: {all(payload['conway_model']['identities'].values())}",
        f"m=2 reduced/full verifier pass: {payload['small_instance_audit']['m2_B']['valid']} / {payload['small_instance_audit']['m2_A']['valid']}",
        f"11-case matching cover total: {payload['normalization_audit']['labeled_matching_count']}",
        f"Projector baseline independent constructions agree: {projector_agrees}",
        f"Full normalized OPB variables: {payload['full_case_encoding_counts']['total_variables']}",
        f"Full normalized OPB constraints: {payload['full_case_encoding_counts']['total_constraints']}",
    ]
    (results / "audit.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
