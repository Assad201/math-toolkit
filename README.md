# Math Toolkit

A small Python library and CLI for the linear algebra and calculus
operations that come up constantly when teaching or studying **Linear
Algebra** and **Calculus 3**: matrix operations, symbolic
differentiation/integration, limits, Taylor series, multivariable
derivatives, and quick plotting of functions and surfaces.

## Features

- **Linear algebra** (`math_toolkit.linear_algebra`): determinant,
  inverse, rank, eigenvalues/eigenvectors, solving linear systems,
  diagonalizability check.
- **Calculus** (`math_toolkit.calculus`): symbolic derivatives (any
  order), indefinite/definite integrals, limits (one- and two-sided),
  Taylor series, partial derivatives, gradients.
- **Plotting** (`math_toolkit.plotting`): 2D function plots and 3D
  surface plots for two-variable functions, either shown interactively
  or saved to a file.
- **CLI** (`math_toolkit.cli`): every operation above is also available
  from the command line.

## Installation

```bash
git clone <repo-url>
cd math-toolkit
pip install -r requirements.txt
```

## Usage as a library

```python
from math_toolkit import linear_algebra as la
from math_toolkit import calculus

# Linear algebra
la.determinant([[1, 2], [3, 4]])          # -2.0
la.solve_system([[1, 1], [1, -1]], [3, 1])  # [2.0, 1.0]

# Calculus
calculus.derivative("x**2 * sin(x)", "x")        # 'x*(x*cos(x) + 2*sin(x))'
calculus.definite_integral("x**2", "x", 0, 3)    # 9.0
calculus.compute_limit("sin(x)/x", "x", 0)       # '1'
```

## Usage from the CLI

```bash
python -m math_toolkit.cli derivative "x**2 * sin(x)" --var x --order 1
python -m math_toolkit.cli integral "1/x" --var x
python -m math_toolkit.cli limit "sin(x)/x" --var x --point 0
python -m math_toolkit.cli series "exp(x)" --var x --point 0 --order 5
python -m math_toolkit.cli plot "sin(x) + x/4" --save plot.png
python -m math_toolkit.cli det "[[1,2],[3,4]]"
python -m math_toolkit.cli solve "[[1,1],[1,-1]]" "[3,1]"
```

## Running the tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```
math-toolkit/
├── math_toolkit/
│   ├── __init__.py
│   ├── linear_algebra.py
│   ├── calculus.py
│   ├── plotting.py
│   └── cli.py
├── tests/
│   ├── test_linear_algebra.py
│   └── test_calculus.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Notes

Symbolic operations are powered by [SymPy](https://www.sympy.org/) and
numeric linear algebra by [NumPy](https://numpy.org/), so results for
calculus functions come back as exact symbolic expressions rather than
floating-point approximations wherever possible.
