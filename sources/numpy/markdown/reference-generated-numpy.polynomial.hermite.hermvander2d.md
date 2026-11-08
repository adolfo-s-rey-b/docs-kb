[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander2d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.hermvander2d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.hermvander2d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.hermvander2d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander2d.html#numpy-polynomial-hermite-hermvander2d "Link to this heading")

===================================================================================================================================================================================================

polynomial.hermite.hermvander2d(_x_, _y_, _deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite.py#L1237-L1293)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander2d.html#numpy.polynomial.hermite.hermvander2d "Link to this definition")

Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees _deg_ and sample points `(x, y)`. The pseudo-Vandermonde matrix is defined by

\\\[V\[..., (deg\[1\] + 1)\*i + j\] = H\_i(x) \* H\_j(y),\\\]

where `0 <= i <= deg[0]` and `0 <= j <= deg[1]`. The leading indices of _V_ index the points `(x, y)` and the last index encodes the degrees of the Hermite polynomials.

If `V = hermvander2d(x, y, [xdeg, ydeg])`, then the columns of _V_ correspond to the elements of a 2-D coefficient array _c_ of shape (xdeg + 1, ydeg + 1) in the order

\\\[c\_{00}, c\_{01}, c\_{02}, ... , c\_{10}, c\_{11}, c\_{12}, ...\\\]

and `np.dot(V, c.flat)` and `hermval2d(x, y, c)` will be the same up to roundoff. This equivalence is useful both for least squares fitting and for the evaluation of a large number of 2-D Hermite series of the same degrees and sample points.

Parameters:

**x, y**array\_like

Arrays of point coordinates, all of the same shape. The dtypes will be converted to either float64 or complex128 depending on whether any of the elements are complex. Scalars are converted to 1-D arrays.

**deg**list of ints

List of maximum degrees of the form \[x\_deg, y\_deg\].

Returns:

**vander2d**ndarray

The shape of the returned matrix is `x.shape + (order,)`, where \\(order = (deg\[0\]+1)\*(deg\[1\]+1)\\). The dtype will be the same as the converted _x_ and _y_.

See also

[`hermvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander.html#numpy.polynomial.hermite.hermvander "numpy.polynomial.hermite.hermvander")
, [`hermvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander3d.html#numpy.polynomial.hermite.hermvander3d "numpy.polynomial.hermite.hermvander3d")
, [`hermval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval2d.html#numpy.polynomial.hermite.hermval2d "numpy.polynomial.hermite.hermval2d")
, [`hermval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval3d.html#numpy.polynomial.hermite.hermval3d "numpy.polynomial.hermite.hermval3d")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.polynomial.hermite import hermvander2d
\>>> x \= np.array(\[\-1, 0, 1\])
\>>> y \= np.array(\[\-1, 0, 1\])
\>>> hermvander2d(x, y, \[2, 2\])
array(\[\[ 1., -2.,  2., -2.,  4., -4.,  2., -4.,  4.\],\
       \[ 1.,  0., -2.,  0.,  0., -0., -2., -0.,  4.\],\
       \[ 1.,  2.,  2.,  2.,  4.,  4.,  2.,  4.,  4.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page