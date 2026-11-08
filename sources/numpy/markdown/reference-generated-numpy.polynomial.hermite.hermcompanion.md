[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermcompanion.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.hermcompanion.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.hermcompanion.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.hermcompanion[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermcompanion.html#numpy-polynomial-hermite-hermcompanion "Link to this heading")

======================================================================================================================================================================================================

polynomial.hermite.hermcompanion(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite.py#L1490-L1534)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermcompanion.html#numpy.polynomial.hermite.hermcompanion "Link to this definition")

Return the scaled companion matrix of c.

The basis polynomials are scaled so that the companion matrix is symmetric when _c_ is a Hermite basis polynomial. This provides better eigenvalue estimates than the unscaled case and for basis polynomials the eigenvalues are guaranteed to be real if [`numpy.linalg.eigvalsh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#numpy.linalg.eigvalsh "numpy.linalg.eigvalsh")
 is used to obtain them.

Parameters:

**c**array\_like

1-D array of Hermite series coefficients ordered from low to high degree.

Returns:

**mat**ndarray

Scaled companion matrix of dimensions (deg, deg).

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite import hermcompanion
\>>> hermcompanion(\[1, 0, 1\])
array(\[\[0.        , 0.35355339\],\
       \[0.70710678, 0.        \]\])

Copy to clipboard

Go BackOpen In Tab

On this page