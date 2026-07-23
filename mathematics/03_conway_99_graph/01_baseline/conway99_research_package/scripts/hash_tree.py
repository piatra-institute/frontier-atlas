#!/usr/bin/env python3
"""Write deterministic SHA-256 hashes for all package files."""

from __future__ import annotations

import hashlib
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    output = root / "results" / "SHA256SUMS"
    files = [
        path
        for path in root.rglob("*")
        if path.is_file()
        and path != output
        and "__pycache__" not in path.parts
        and ".pytest_cache" not in path.parts
    ]
    lines = [f"{digest(path)}  {path.relative_to(root).as_posix()}" for path in sorted(files)]
    output.write_text("\n".join(lines) + "\n", encoding="ascii")


if __name__ == "__main__":
    main()
