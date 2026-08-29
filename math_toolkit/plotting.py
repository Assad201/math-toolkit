"""
Plotting helpers built on Matplotlib and SymPy.

These functions render a symbolic expression (given as a string) over a
numeric range and either show the plot interactively or save it to a
file, which is convenient for generating figures for slides or handouts.
"""

from __future__ import annotations

import numpy as np
import sympy as sp
import matplotlib

matplotlib.use("Agg")  # safe default for headless/server environments
import matplotlib.pyplot as plt


def plot_function(
    expr_str: str,
    var: str = "x",
    x_range: tuple[float, float] = (-10, 10),
    num_points: int = 400,
    save_path: str | None = None,
    title: str | None = None,
):
    """Plot a single-variable function over x_range.

    If save_path is given, the figure is written to that path (e.g. 'plot.png')
    instead of being shown interactively.
    """
    symbol = sp.Symbol(var)
    expr = sp.sympify(expr_str)
    func = sp.lambdify(symbol, expr, modules=["numpy"])

    x_values = np.linspace(x_range[0], x_range[1], num_points)
    y_values = func(x_values)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x_values, y_values, linewidth=2)
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.set_xlabel(var)
    ax.set_ylabel(f"f({var})")
    ax.set_title(title or f"f({var}) = {expr_str}")
    ax.grid(True, linestyle="--", alpha=0.5)

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return save_path

    plt.show()
    return fig


def plot_surface(
    expr_str: str,
    vars_: tuple[str, str] = ("x", "y"),
    x_range: tuple[float, float] = (-5, 5),
    y_range: tuple[float, float] = (-5, 5),
    num_points: int = 60,
    save_path: str | None = None,
    title: str | None = None,
):
    """Plot a two-variable function z = f(x, y) as a 3D surface."""
    x_sym, y_sym = sp.symbols(vars_)
    expr = sp.sympify(expr_str)
    func = sp.lambdify((x_sym, y_sym), expr, modules=["numpy"])

    x_values = np.linspace(x_range[0], x_range[1], num_points)
    y_values = np.linspace(y_range[0], y_range[1], num_points)
    x_grid, y_grid = np.meshgrid(x_values, y_values)
    z_grid = func(x_grid, y_grid)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(projection="3d")
    surface = ax.plot_surface(x_grid, y_grid, z_grid, cmap="viridis", edgecolor="none")
    ax.set_xlabel(vars_[0])
    ax.set_ylabel(vars_[1])
    ax.set_zlabel(f"f({vars_[0]}, {vars_[1]})")
    ax.set_title(title or f"f({vars_[0]}, {vars_[1]}) = {expr_str}")
    fig.colorbar(surface, shrink=0.6, aspect=10)

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return save_path

    plt.show()
    return fig
