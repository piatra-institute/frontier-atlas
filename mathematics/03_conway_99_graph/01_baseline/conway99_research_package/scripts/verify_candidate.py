#!/usr/bin/env python3
"""Verify a candidate B, A, or integral-projector G matrix."""

from __future__ import annotations

import argparse
import json

from conway99.projector import verify_G
from conway99.verify import load_matrix, verify_A, verify_B


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("A", "B", "G"))
    parser.add_argument("matrix")
    parser.add_argument("--m", type=int, default=7)
    args = parser.parse_args()

    matrix = load_matrix(args.matrix)
    if args.kind == "A":
        report = verify_A(matrix, m=args.m)
    elif args.kind == "B":
        report = verify_B(matrix, m=args.m)
    else:
        report = verify_G(matrix)
    print(json.dumps(report.to_dict(), indent=2, sort_keys=True))
    return 0 if report.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
