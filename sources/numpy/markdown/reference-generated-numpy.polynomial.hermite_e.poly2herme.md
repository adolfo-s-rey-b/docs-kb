[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.poly2herme.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.poly2herme.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.poly2herme[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.poly2herme.html#numpy-polynomial-hermite-e-poly2herme "Link to this heading")

====================================================================================================================================================================================================

polynomial.hermite\_e.poly2herme(_pol_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L96-L140)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.poly2herme.html#numpy.polynomial.hermite_e.poly2herme "Link to this definition")

Convert a polynomial to a Hermite series.

Convert an array representing the coefficients of a polynomial (relative to the “standard” basis) ordered from lowest degree to highest, to an array of the coefficients of the equivalent Hermite series, ordered from lowest to highest degree.

Parameters:

**pol**array\_like

1-D array containing the polynomial coefficients

Returns:

**c**ndarray

1-D array containing the coefficients of the equivalent Hermite series.

See also

[`herme2poly`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.herme2poly.html#numpy.polynomial.hermite_e.herme2poly "numpy.polynomial.hermite_e.herme2poly")

Notes

The easy way to do conversions between polynomial basis sets is to use the convert method of a class instance.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.polynomial.hermite\_e import poly2herme
\>>> poly2herme(np.arange(4))
array(\[  2.,  10.,   2.,   3.\])

Copy to clipboard

Go BackOpen In Tab

On this page