"""
Command-line interface for math_toolkit.

Examples:
    python -m math_toolkit.cli derivative "x**2 * sin(x)" --var x --order 2
    python -m math_toolkit.cli integral "1/x" --var x
    python -m math_toolkit.cli limit "sin(x)/x" --var x --point 0
    python -m math_toolkit.cli plot "sin(x) + x/4" --save plot.png
    python -m math_toolkit.cli det "[[1,2],[3,4]]"
"""

from __future__ import annotations

import argparse
import ast
import sys

from . import calculus, linear_algebra, plotting


def _parse_matrix(text: str):
    try:
        return ast.literal_eval(text)
    except (ValueError, SyntaxError) as exc:
        raise ValueError(f"Could not parse matrix literal '{text}': {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="math_toolkit", description="Small math CLI toolkit.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_diff = subparsers.add_parser("derivative", help="Differentiate an expression")
    p_diff.add_argument("expr")
    p_diff.add_argument("--var", default="x")
    p_diff.add_argument("--order", type=int, default=1)

    p_int = subparsers.add_parser("integral", help="Integrate an expression indefinitely")
    p_int.add_argument("expr")
    p_int.add_argument("--var", default="x")

    p_dint = subparsers.add_parser("definite-integral", help="Integrate over [a, b]")
    p_dint.add_argument("expr")
    p_dint.add_argument("--var", default="x")
    p_dint.add_argument("--a", type=float, required=True)
    p_dint.add_argument("--b", type=float, required=True)

    p_lim = subparsers.add_parser("limit", help="Compute a limit")
    p_lim.add_argument("expr")
    p_lim.add_argument("--var", default="x")
    p_lim.add_argument("--point", required=True)
    p_lim.add_argument("--direction", default="+-", choices=["+", "-", "+-"])

    p_series = subparsers.add_parser("series", help="Compute a Taylor series")
    p_series.add_argument("expr")
    p_series.add_argument("--var", default="x")
    p_series.add_argument("--point", type=float, default=0)
    p_series.add_argument("--order", type=int, default=5)

    p_plot = subparsers.add_parser("plot", help="Plot a single-variable function")
    p_plot.add_argument("expr")
    p_plot.add_argument("--var", default="x")
    p_plot.add_argument("--save", default=None, help="Path to save the figure instead of showing it")

    p_det = subparsers.add_parser("det", help="Compute a matrix determinant")
    p_det.add_argument("matrix", help="Matrix as a Python literal, e.g. '[[1,2],[3,4]]'")

    p_inv = subparsers.add_parser("inverse", help="Compute a matrix inverse")
    p_inv.add_argument("matrix", help="Matrix as a Python literal, e.g. '[[1,2],[3,4]]'")

    p_solve = subparsers.add_parser("solve", help="Solve A x = b")
    p_solve.add_argument("matrix", help="Coefficient matrix A as a Python literal")
    p_solve.add_argument("vector", help="Constants vector b as a Python literal, e.g. '[1,2]'")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "derivative":
            print(calculus.derivative(args.expr, args.var, args.order))
        elif args.command == "integral":
            print(calculus.indefinite_integral(args.expr, args.var))
        elif args.command == "definite-integral":
            print(calculus.definite_integral(args.expr, args.var, args.a, args.b))
        elif args.command == "limit":
            point = args.point
            try:
                point = float(point)
            except ValueError:
                pass  # allow symbolic points like 'oo'
            print(calculus.compute_limit(args.expr, args.var, point, args.direction))
        elif args.command == "series":
            print(calculus.taylor_series(args.expr, args.var, args.point, args.order))
        elif args.command == "plot":
            result = plotting.plot_function(args.expr, args.var, save_path=args.save)
            if args.save:
                print(f"Saved plot to {result}")
        elif args.command == "det":
            print(linear_algebra.determinant(_parse_matrix(args.matrix)))
        elif args.command == "inverse":
            print(linear_algebra.inverse(_parse_matrix(args.matrix)))
        elif args.command == "solve":
            print(linear_algebra.solve_system(_parse_matrix(args.matrix), _parse_matrix(args.vector)))
    except Exception as exc:  # noqa: BLE001 - CLI top-level error boundary
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
