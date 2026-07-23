#!/usr/bin/env python3
"""Thin wrapper around conway99.opb for reproducible case generation."""

from conway99.cli import main

if __name__ == "__main__":
    raise SystemExit(main(["generate-opb", *__import__("sys").argv[1:]]))
