#!/usr/bin/env python3
"""Rebuild the 84-row CSV from the supplied source arrays."""
from pathlib import Path
import csv, json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
samples = np.load(ROOT / "data" / "510_kempe_samples_3001.npy")
targeted = np.load(ROOT / "data" / "510_targeted_same_20.npy")
rows = np.vstack([samples, targeted])
selected = json.loads(
    (ROOT / "certificates" / "selected_source_rows.json").read_text()
)["selected_indices"]
certificate = rows[selected]
assert certificate.shape == (84, 510)
with (ROOT / "certificates" / "colorings_84.csv").open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["coloring_id"] + [f"v{i}" for i in range(1, 511)])
    for row_id, row in enumerate(certificate, start=1):
        writer.writerow([row_id] + [int(value) for value in row])
print("rebuilt certificates/colorings_84.csv")
