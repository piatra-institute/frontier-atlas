"""Command-line interface for verification, case generation, and OPB output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .opb import write_metadata, write_opb
from .orbits import build_case_records
from .projector import G_to_B, verify_G
from .verify import load_matrix, verify_A, verify_B


def _partition(value: str) -> tuple[int, ...]:
    try:
        parts = tuple(int(item) for item in value.replace("+", ",").split(",") if item)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("partition must look like 3+2+1") from exc
    if not parts or any(part <= 0 for part in parts):
        raise argparse.ArgumentTypeError("partition parts must be positive")
    return parts


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="conway99")
    sub = parser.add_subparsers(dest="command", required=True)

    verify_b = sub.add_parser("verify-b", help="verify a reduced B matrix")
    verify_b.add_argument("matrix")
    verify_b.add_argument("--m", type=int, default=7)

    verify_a = sub.add_parser("verify-a", help="verify a full adjacency matrix")
    verify_a.add_argument("matrix")
    verify_a.add_argument("--m", type=int, default=7)

    verify_g = sub.add_parser("verify-g", help="verify an integral-projector G matrix")
    verify_g.add_argument("matrix")

    opb = sub.add_parser("generate-opb", help="generate an exact OPB encoding")
    opb.add_argument("output")
    opb.add_argument("--m", type=int, default=7)
    opb.add_argument("--partition", type=_partition)
    opb.add_argument("--metadata")

    cases = sub.add_parser("cases", help="write the normalized case manifest")
    cases.add_argument("output")
    cases.add_argument("--m", type=int, default=7)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "verify-b":
        report = verify_B(load_matrix(args.matrix), m=args.m)
    elif args.command == "verify-a":
        report = verify_A(load_matrix(args.matrix), m=args.m)
    elif args.command == "verify-g":
        report = verify_G(load_matrix(args.matrix))
    elif args.command == "generate-opb":
        counts = write_opb(
            args.output,
            m=args.m,
            partition=args.partition,
        )
        if args.metadata:
            write_metadata(args.metadata, counts, partition=args.partition)
        print(json.dumps(counts.to_dict(), indent=2, sort_keys=True))
        return 0
    elif args.command == "cases":
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        payload = {"m": args.m, "cases": build_case_records(m=args.m)}
        output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(output)
        return 0
    else:  # pragma: no cover
        raise AssertionError(args.command)

    print(json.dumps(report.to_dict(), indent=2, sort_keys=True))
    return 0 if report.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
