#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo '[1/3] Verifying bundle-wide SHA-256 manifest'
sha256sum -c MANIFEST.sha256

echo '[2/3] Verifying regenerated research-package manifest'
(
  cd research_package
  sha256sum -c MANIFEST.sha256
)

echo '[3/3] Verifying extension hashes from portable metadata'
python3 - <<'PY'
import hashlib, json
from pathlib import Path
root = Path('extension_instances')
data = json.loads((root / 'metadata_portable.json').read_text())
for item in data:
    path = root / item['path']
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != item['sha256']:
        raise SystemExit(f"FAIL {path}: expected {item['sha256']}, got {actual}")
    print(f"{path}: OK")
PY

echo 'All bundle checks passed.'
