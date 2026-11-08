[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.hermevander.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.hermevander.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.hermevander[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander.html#numpy-polynomial-hermite-e-hermevander "Link to this heading")

=======================================================================================================================================================================================================

polynomial.hermite\_e.hermevander(_x_, _deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L1125-L1183)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander.html#numpy.polynomial.hermite_e.hermevander "Link to this definition")

Pseudo-Vandermonde matrix of given degree.

Returns the pseudo-Vandermonde matrix of degree _deg_ and sample points _x_. The pseudo-Vandermonde matrix is defined by

where `0 <= i <= deg`. The leading indices of _V_ index the elements of _x_ and the last index is the degree of the HermiteE polynomial.

If _c_ is a 1-D array of coefficients of length `n + 1` and _V_ is the array `V = hermevander(x, n)`, then `np.dot(V, c)` and `hermeval(x, c)` are the same up to roundoff. This equivalence is useful both for least squares fitting and for the evaluation of a large number of HermiteE series of the same degree and sample points.

Parameters:

**x**array\_like

Array of points. The dtype is converted to float64 or complex128 depending on whether any of the elements are complex. If _x_ is scalar it is converted to a 1-D array.

**deg**int

Degree of the resulting matrix.

Returns:

**vander**ndarray

The pseudo-Vandermonde matrix. The shape of the returned matrix is `x.shape + (deg + 1,)`, where The last index is the degree of the corresponding HermiteE polynomial. The dtype will be the same as the converted _x_.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.polynomial.hermite\_e import hermevander
\>>> x \= np.array(\[\-1, 0, 1\])
\>>> hermevander(x, 3)
array(\[\[ 1., -1.,  0.,  2.\],\
       \[ 1.,  0., -1., -0.\],\
       \[ 1.,  1.,  0., -2.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page