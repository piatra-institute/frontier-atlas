"""Exact structural tools for Conway's putative srg(99, 14, 1, 2)."""

from .model import ModelData, build_model
from .verify import reconstruct_A, verify_A, verify_B

__all__ = [
    "ModelData",
    "build_model",
    "reconstruct_A",
    "verify_A",
    "verify_B",
]

__version__ = "0.1.0"
