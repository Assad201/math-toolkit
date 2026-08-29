"""
Math Toolkit
============

A small Python library for the kinds of linear algebra and calculus
operations that come up when teaching or studying Linear Algebra and
Calculus 3: matrix operations, symbolic differentiation/integration,
limits, and quick plotting of functions and surfaces.
"""

from .linear_algebra import (
    determinant,
    inverse,
    rank,
    eigen,
    solve_system,
    is_diagonalizable,
)
from .calculus import (
    derivative,
    indefinite_integral,
    definite_integral,
    compute_limit,
    taylor_series,
    partial_derivative,
    gradient,
)

__all__ = [
    "determinant",
    "inverse",
    "rank",
    "eigen",
    "solve_system",
    "is_diagonalizable",
    "derivative",
    "indefinite_integral",
    "definite_integral",
    "compute_limit",
    "taylor_series",
    "partial_derivative",
    "gradient",
]

__version__ = "0.1.0"
