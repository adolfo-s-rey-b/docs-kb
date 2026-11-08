[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polycompanion.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polycompanion.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polycompanion.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polycompanion[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polycompanion.html#numpy-polynomial-polynomial-polycompanion "Link to this heading")

===============================================================================================================================================================================================================

polynomial.polynomial.polycompanion(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L1502-L1542)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polycompanion.html#numpy.polynomial.polynomial.polycompanion "Link to this definition")

Return the companion matrix of c.

The companion matrix for power series cannot be made symmetric by scaling the basis, so this function differs from those for the orthogonal polynomials.

Parameters:

**c**array\_like

1-D array of polynomial coefficients ordered from low to high degree.

Returns:

**mat**ndarray

Companion matrix of dimensions (deg, deg).

Examples

Try it in your browser!

\>>> from numpy.polynomial import polynomial as P
\>>> c \= (1, 2, 3)
\>>> P.polycompanion(c)
array(\[\[ 0.        , -0.33333333\],\
       \[ 1.        , -0.66666667\]\])

Copy to clipboard

Go BackOpen In Tab

On this page