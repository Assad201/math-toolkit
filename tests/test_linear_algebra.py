import unittest

import numpy as np

from math_toolkit import linear_algebra as la


class TestLinearAlgebra(unittest.TestCase):
    def test_determinant(self):
        self.assertAlmostEqual(la.determinant([[1, 2], [3, 4]]), -2.0)

    def test_determinant_identity(self):
        self.assertAlmostEqual(la.determinant([[1, 0], [0, 1]]), 1.0)

    def test_inverse(self):
        result = la.inverse([[1, 2], [3, 4]])
        expected = np.array([[-2.0, 1.0], [1.5, -0.5]])
        np.testing.assert_allclose(result, expected)

    def test_inverse_singular_raises(self):
        with self.assertRaises(np.linalg.LinAlgError):
            la.inverse([[1, 2], [2, 4]])

    def test_rank(self):
        self.assertEqual(la.rank([[1, 2], [2, 4]]), 1)
        self.assertEqual(la.rank([[1, 0], [0, 1]]), 2)

    def test_solve_system(self):
        # x + y = 3, x - y = 1  ->  x = 2, y = 1
        result = la.solve_system([[1, 1], [1, -1]], [3, 1])
        np.testing.assert_allclose(result, [2.0, 1.0])

    def test_eigen_diagonal_matrix(self):
        values, _ = la.eigen([[2, 0], [0, 3]])
        np.testing.assert_allclose(sorted(values), [2.0, 3.0])

    def test_is_diagonalizable_identity(self):
        self.assertTrue(la.is_diagonalizable([[1, 0], [0, 1]]))

    def test_non_square_raises(self):
        with self.assertRaises(ValueError):
            la.determinant([[1, 2, 3], [4, 5, 6]])


if __name__ == "__main__":
    unittest.main()
