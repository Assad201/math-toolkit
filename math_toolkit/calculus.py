"""
Symbolic calculus utilities built on SymPy.

Expressions are passed as plain strings (e.g. "x**2 * sin(x)") so the
functions can be used quickly from a script, notebook, or the CLI
without importing SymPy symbols by hand.
"""

from __future__ import annotations

import sympy as sp


def _parse(expr_str: str) -> sp.Expr:
    """Parse a string into a SymPy expression, raising a clear error on failure."""
    try:
        return sp.sympify(expr_str)
    except (sp.SympifyError, SyntaxError) as exc:
        raise ValueError(f"Could not parse expression '{expr_str}': {exc}") from exc


def derivative(expr_str: str, var: str = "x", order: int = 1) -> str:
    """Return the order-th derivative of expr_str with respect to var, as a string."""
    symbol = sp.Symbol(var)
    expr = _parse(expr_str)
    result = sp.diff(expr, symbol, order)
    return str(sp.simplify(result))


def indefinite_integral(expr_str: str, var: str = "x") -> str:
    """Return the indefinite integral of expr_str with respect to var, as a string."""
    symbol = sp.Symbol(var)
    expr = _parse(expr_str)
    result = sp.integrate(expr, symbol)
    return f"{sp.simplify(result)} + C"


def definite_integral(expr_str: str, var: str, a, b) -> float:
    """Return the definite integral of expr_str with respect to var over [a, b]."""
    symbol = sp.Symbol(var)
    expr = _parse(expr_str)
    result = sp.integrate(expr, (symbol, a, b))
    return float(result.evalf())


def compute_limit(expr_str: str, var: str, point, direction: str = "+-") -> str:
    """Return the limit of expr_str as var approaches point.

    direction: '+' for right-hand limit, '-' for left-hand limit,
    '+-' (default) for the two-sided limit.
    """
    symbol = sp.Symbol(var)
    expr = _parse(expr_str)
    if direction == "+-":
        result = sp.limit(expr, symbol, point)
    else:
        result = sp.limit(expr, symbol, point, dir=direction)
    return str(result)


def taylor_series(expr_str: str, var: str = "x", point=0, order: int = 5) -> str:
    """Return the Taylor series of expr_str around `point` up to the given order."""
    symbol = sp.Symbol(var)
    expr = _parse(expr_str)
    series = sp.series(expr, symbol, point, order).removeO()
    return str(sp.simplify(series))


def partial_derivative(expr_str: str, var: str, other_vars: list[str] | None = None) -> str:
    """Return the partial derivative of a multivariable expression with respect to var.

    other_vars is optional and only used to make sure those symbols are
    recognized as free variables (useful if they don't already appear
    elsewhere in expr_str).
    """
    symbols = {var: sp.Symbol(var)}
    if other_vars:
        for name in other_vars:
            symbols[name] = sp.Symbol(name)
    expr = _parse(expr_str)
    result = sp.diff(expr, symbols[var])
    return str(sp.simplify(result))


def gradient(expr_str: str, vars_list: list[str]) -> dict[str, str]:
    """Return the gradient of a multivariable scalar function as a dict of partials."""
    expr = _parse(expr_str)
    grad = {}
    for name in vars_list:
        symbol = sp.Symbol(name)
        grad[name] = str(sp.simplify(sp.diff(expr, symbol)))
    return grad
