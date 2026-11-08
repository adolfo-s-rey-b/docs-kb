[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polyvander.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polyvander.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyvander[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html#numpy-polynomial-polynomial-polyvander "Link to this heading")

======================================================================================================================================================================================================

polynomial.polynomial.polyvander(_x_, _deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L1128-L1192)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html#numpy.polynomial.polynomial.polyvander "Link to this definition")

Vandermonde matrix of given degree.

Returns the Vandermonde matrix of degree _deg_ and sample points _x_. The Vandermonde matrix is defined by

\\\[V\[..., i\] = x^i,\\\]

where `0 <= i <= deg`. The leading indices of _V_ index the elements of _x_ and the last index is the power of _x_.

If _c_ is a 1-D array of coefficients of length `n + 1` and _V_ is the matrix `V = polyvander(x, n)`, then `np.dot(V, c)` and `polyval(x, c)` are the same up to roundoff. This equivalence is useful both for least squares fitting and for the evaluation of a large number of polynomials of the same degree and sample points.

Parameters:

**x**array\_like

Array of points. The dtype is converted to float64 or complex128 depending on whether any of the elements are complex. If _x_ is scalar it is converted to a 1-D array.

**deg**int

Degree of the resulting matrix.

Returns:

**vander**ndarray.

The Vandermonde matrix. The shape of the returned matrix is `x.shape + (deg + 1,)`, where the last index is the power of _x_. The dtype will be the same as the converted _x_.

See also

[`polyvander2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander2d.html#numpy.polynomial.polynomial.polyvander2d "numpy.polynomial.polynomial.polyvander2d")
, [`polyvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander3d.html#numpy.polynomial.polynomial.polyvander3d "numpy.polynomial.polynomial.polyvander3d")

Examples

Try it in your browser!

The Vandermonde matrix of degree `deg = 5` and sample points `x = [-1, 2, 3]` contains the element-wise powers of _x_ from 0 to 5 as its columns.

\>>> from numpy.polynomial import polynomial as P
\>>> x, deg \= \[\-1, 2, 3\], 5
\>>> P.polyvander(x\=x, deg\=deg)
array(\[\[  1.,  -1.,   1.,  -1.,   1.,  -1.\],\
       \[  1.,   2.,   4.,   8.,  16.,  32.\],\
       \[  1.,   3.,   9.,  27.,  81., 243.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page