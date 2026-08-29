import unittest

from math_toolkit import calculus


class TestCalculus(unittest.TestCase):
    def test_derivative_polynomial(self):
        self.assertEqual(calculus.derivative("x**3", "x"), "3*x**2")

    def test_derivative_second_order(self):
        self.assertEqual(calculus.derivative("x**3", "x", order=2), "6*x")

    def test_indefinite_integral(self):
        self.assertEqual(calculus.indefinite_integral("2*x", "x"), "x**2 + C")

    def test_definite_integral(self):
        result = calculus.definite_integral("x**2", "x", 0, 3)
        self.assertAlmostEqual(result, 9.0)

    def test_limit_removable_singularity(self):
        result = calculus.compute_limit("sin(x)/x", "x", 0)
        self.assertEqual(result, "1")

    def test_limit_one_sided(self):
        result = calculus.compute_limit("1/x", "x", 0, direction="+")
        self.assertEqual(result, "oo")

    def test_taylor_series(self):
        result = calculus.taylor_series("exp(x)", "x", 0, 4)
        # 1 + x + x^2/2 + x^3/6 (some ordering of terms)
        self.assertIn("x**3/6", result)
        self.assertIn("x**2/2", result)

    def test_partial_derivative(self):
        result = calculus.partial_derivative("x**2 * y + y**3", "x", other_vars=["y"])
        self.assertEqual(result, "2*x*y")

    def test_gradient(self):
        grad = calculus.gradient("x**2 + y**2", ["x", "y"])
        self.assertEqual(grad["x"], "2*x")
        self.assertEqual(grad["y"], "2*y")

    def test_invalid_expression_raises(self):
        with self.assertRaises(ValueError):
            calculus.derivative("x**", "x")


if __name__ == "__main__":
    unittest.main()
