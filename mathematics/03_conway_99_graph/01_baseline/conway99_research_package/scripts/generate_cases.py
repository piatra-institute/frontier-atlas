#!/usr/bin/env python3
"""Generate the 11 normalized Conway-99 case files."""

from __future__ import annotations

import json
from pathlib import Path

from conway99.orbits import build_case_records


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    cases_dir = root / "cases"
    cases_dir.mkdir(parents=True, exist_ok=True)
    records = build_case_records(7)
    manifest = {
        "problem": "srg(99,14,1,2)",
        "normalization": "perfect matching on S_0 modulo C2 wr S6",
        "case_count": len(records),
        "total_labeled_matchings": sum(int(record["orbit_size"]) for record in records),
        "cases": records,
    }
    (cases_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    for record in records:
        partition = "_".join(str(part) for part in record["partition"])
        filename = f"case_{int(record['case']):02d}_{partition}.json"
        (cases_dir / filename).write_text(
            json.dumps(record, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
