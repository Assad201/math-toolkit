"""
Linear algebra utilities built on NumPy.

Every function accepts plain nested lists or NumPy arrays so it can be
used directly from a Python shell without extra conversion steps.
"""

from __future__ import annotations

import numpy as np


def _as_array(matrix) -> np.ndarray:
    """Convert input to a float NumPy array, raising a clear error on bad shapes."""
    arr = np.array(matrix, dtype=float)
    if arr.ndim != 2:
        raise ValueError(f"Expected a 2D matrix, got array with shape {arr.shape}")
    return arr


def determinant(matrix) -> float:
    """Return the determinant of a square matrix."""
    arr = _as_array(matrix)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Determinant is only defined for square matrices")
    return float(np.linalg.det(arr))


def inverse(matrix) -> np.ndarray:
    """Return the inverse of a square, non-singular matrix."""
    arr = _as_array(matrix)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Inverse is only defined for square matrices")
    det = np.linalg.det(arr)
    if np.isclose(det, 0.0):
        raise np.linalg.LinAlgError("Matrix is singular (determinant is 0); no inverse exists")
    return np.linalg.inv(arr)


def rank(matrix) -> int:
    """Return the rank of a matrix."""
    arr = _as_array(matrix)
    return int(np.linalg.matrix_rank(arr))


def eigen(matrix) -> tuple[np.ndarray, np.ndarray]:
    """Return (eigenvalues, eigenvectors) of a square matrix.

    Each column of the eigenvectors array corresponds to the eigenvalue
    at the same index, matching NumPy's convention.
    """
    arr = _as_array(matrix)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Eigenvalues/eigenvectors are only defined for square matrices")
    values, vectors = np.linalg.eig(arr)
    return values, vectors


def solve_system(coefficients, constants) -> np.ndarray:
    """Solve the linear system A x = b.

    coefficients: the matrix A (n x n)
    constants: the vector b (length n)
    """
    a_matrix = _as_array(coefficients)
    b_vector = np.array(constants, dtype=float).flatten()
    if a_matrix.shape[0] != a_matrix.shape[1]:
        raise ValueError("Coefficient matrix must be square")
    if a_matrix.shape[0] != b_vector.shape[0]:
        raise ValueError("Coefficient matrix and constants vector have incompatible shapes")
    return np.linalg.solve(a_matrix, b_vector)


def is_diagonalizable(matrix, tol: float = 1e-8) -> bool:
    """Check whether a square matrix is diagonalizable.

    A matrix is diagonalizable if the geometric multiplicity of every
    eigenvalue equals its algebraic multiplicity. We approximate this by
    checking that the eigenvector matrix has full rank.
    """
    arr = _as_array(matrix)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Diagonalizability is only defined for square matrices")
    _, vectors = np.linalg.eig(arr)
    return np.linalg.matrix_rank(vectors, tol=tol) == arr.shape[0]
