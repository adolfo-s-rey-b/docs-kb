[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebvander2d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html#numpy-polynomial-chebyshev-chebvander2d "Link to this heading")

=========================================================================================================================================================================================================

polynomial.chebyshev.chebvander2d(_x_, _y_, _deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L1459-L1503)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html#numpy.polynomial.chebyshev.chebvander2d "Link to this definition")

Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees _deg_ and sample points `(x, y)`. The pseudo-Vandermonde matrix is defined by

\\\[V\[..., (deg\[1\] + 1)\*i + j\] = T\_i(x) \* T\_j(y),\\\]

where `0 <= i <= deg[0]` and `0 <= j <= deg[1]`. The leading indices of _V_ index the points `(x, y)` and the last index encodes the degrees of the Chebyshev polynomials.

If `V = chebvander2d(x, y, [xdeg, ydeg])`, then the columns of _V_ correspond to the elements of a 2-D coefficient array _c_ of shape (xdeg + 1, ydeg + 1) in the order

\\\[c\_{00}, c\_{01}, c\_{02}, ... , c\_{10}, c\_{11}, c\_{12}, ...\\\]

and `np.dot(V, c.flat)` and `chebval2d(x, y, c)` will be the same up to roundoff. This equivalence is useful both for least squares fitting and for the evaluation of a large number of 2-D Chebyshev series of the same degrees and sample points.

Parameters:

**x, y**array\_like

Arrays of point coordinates, all of the same shape. The dtypes will be converted to either float64 or complex128 depending on whether any of the elements are complex. Scalars are converted to 1-D arrays.

**deg**list of ints

List of maximum degrees of the form \[x\_deg, y\_deg\].

Returns:

**vander2d**ndarray

The shape of the returned matrix is `x.shape + (order,)`, where \\(order = (deg\[0\]+1)\*(deg\[1\]+1)\\). The dtype will be the same as the converted _x_ and _y_.

See also

[`chebvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander.html#numpy.polynomial.chebyshev.chebvander "numpy.polynomial.chebyshev.chebvander")
, [`chebvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander3d.html#numpy.polynomial.chebyshev.chebvander3d "numpy.polynomial.chebyshev.chebvander3d")
, [`chebval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval2d.html#numpy.polynomial.chebyshev.chebval2d "numpy.polynomial.chebyshev.chebval2d")
, [`chebval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval3d.html#numpy.polynomial.chebyshev.chebval3d "numpy.polynomial.chebyshev.chebval3d")

On this page