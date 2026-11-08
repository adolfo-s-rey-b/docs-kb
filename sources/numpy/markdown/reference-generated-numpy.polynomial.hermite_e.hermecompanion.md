[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermecompanion.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.hermecompanion[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermecompanion.html#numpy-polynomial-hermite-e-hermecompanion "Link to this heading")

================================================================================================================================================================================================================

polynomial.hermite\_e.hermecompanion(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L1415-L1452)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermecompanion.html#numpy.polynomial.hermite_e.hermecompanion "Link to this definition")

Return the scaled companion matrix of c.

The basis polynomials are scaled so that the companion matrix is symmetric when _c_ is a HermiteE basis polynomial. This provides better eigenvalue estimates than the unscaled case and for basis polynomials the eigenvalues are guaranteed to be real if [`numpy.linalg.eigvalsh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#numpy.linalg.eigvalsh "numpy.linalg.eigvalsh")
 is used to obtain them.

Parameters:

**c**array\_like

1-D array of HermiteE series coefficients ordered from low to high degree.

Returns:

**mat**ndarray

Scaled companion matrix of dimensions (deg, deg).

On this page