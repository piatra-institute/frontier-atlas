#!/usr/bin/env python3
"""Structural and integrity validator for the frozen Stage-0 scout package."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
CARDS = sorted((ROOT / "discovery" / "targets").glob("*.md"))
REQUIRED = [
    "id", "result_class", "statement", "source", "baseline", "witness",
    "search_edge", "budget", "stop_rules", "publication_path", "aliases",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    assert len(CARDS) == 17, f"expected 17 cards, got {len(CARDS)}"
    labels: list[str] = []
    ids: set[str] = set()

    for path in CARDS:
        text = path.read_text(encoding="utf-8")
        assert text.startswith("---\n"), path
        _, front, body = text.split("---", 2)
        data = yaml.safe_load(front)

        missing = [key for key in REQUIRED if key not in data]
        assert not missing, (path, missing)
        assert data["id"] == path.stem, (path, data["id"])
        assert data["id"] not in ids, data["id"]
        ids.add(data["id"])
        assert data["result_class"] in {"B1", "B2", "B3"}, path

        nested = {
            "source": ["primary_locator", "access_date", "status_evidence"],
            "baseline": ["current_value_or_range", "replay_command"],
            "witness": ["format", "checker_command", "checker_hash", "calibration_cases"],
            "budget": ["model", "wall_clock", "cpu_gpu", "memory"],
        }
        for parent, children in nested.items():
            assert isinstance(data[parent], dict), (path, parent)
            assert all(key in data[parent] for key in children), (path, parent)

        label_match = re.search(r"\*\*Admission label:\*\* `([^`]+)`", body)
        assert label_match, (path, "label")
        label = label_match.group(1)
        labels.append(label)
        assert label in {"ready", "needs-status", "needs-edge"}, path

        gate_rows = re.findall(
            r"^\| ([1-9]) \| [^|]+ \| (GREEN|RED) \|", body, re.MULTILINE
        )
        assert [number for number, _ in gate_rows] == list("123456789"), (path, gate_rows)
        green = sum(state == "GREEN" for _, state in gate_rows)
        count_match = re.search(r"\*\*Gate count:\*\* (\d+)/9", body)
        assert count_match and int(count_match.group(1)) == green, (path, green)
        if label == "ready":
            assert green == 9, (path, "ready but not all gates green")
        else:
            assert green < 9, (path, "non-ready but all gates green")
        if label == "needs-status":
            assert any(number in {"1", "2", "3"} and state == "RED" for number, state in gate_rows), path

        vector = re.search(r"`\[([0-5](?:, ?[0-5]){7})\]`", body)
        assert vector, (path, "missing/invalid eight-dimensional score vector")
        assert "Priority vector" in body, path

        command = str(data["witness"]["checker_command"])
        checker_match = re.search(r"(?:^|\s)(checkers/[A-Za-z0-9_.-]+\.py)(?:\s|$)", command)
        assert checker_match, (path, command)
        checker = ROOT / checker_match.group(1)
        assert checker.is_file(), (path, checker)
        declared_hash = str(data["witness"]["checker_hash"])
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", declared_hash), (path, declared_hash)
        assert declared_hash == f"sha256:{sha256(checker)}", (path, checker, declared_hash)

        assert not re.search(r"\b(TODO|TBD|PLACEHOLDER)\b", text, re.IGNORECASE), path

    assert labels.count("ready") == 1, labels
    assert labels.count("needs-status") == 3, labels
    assert labels.count("needs-edge") == 13, labels

    required_files = [
        "README.md", "BREAKTHROUGH_STRATEGY.md", "TARGET_CARD_TEMPLATE.md",
        "SHORTLIST.md", "STATUS_AUDIT.md", "SCREENING_LOG.md",
        "CALIBRATION_REPORT.md", "run_calibrations.sh", "requirements.txt",
    ]
    for name in required_files:
        assert (ROOT / name).is_file(), name

    print(
        "PASS: 17 cards; labels ready=1 needs-status=3 needs-edge=13; "
        "schema, gates, vectors, and checker hashes valid"
    )


if __name__ == "__main__":
    main()
