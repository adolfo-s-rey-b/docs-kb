[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander2d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyvander2d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander2d.html#numpy-polynomial-polynomial-polyvander2d "Link to this heading")

============================================================================================================================================================================================================

polynomial.polynomial.polyvander2d(_x_, _y_, _deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L1195-L1271)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander2d.html#numpy.polynomial.polynomial.polyvander2d "Link to this definition")

Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees _deg_ and sample points `(x, y)`. The pseudo-Vandermonde matrix is defined by

\\\[V\[..., (deg\[1\] + 1)\*i + j\] = x^i \* y^j,\\\]

where `0 <= i <= deg[0]` and `0 <= j <= deg[1]`. The leading indices of _V_ index the points `(x, y)` and the last index encodes the powers of _x_ and _y_.

If `V = polyvander2d(x, y, [xdeg, ydeg])`, then the columns of _V_ correspond to the elements of a 2-D coefficient array _c_ of shape (xdeg + 1, ydeg + 1) in the order

\\\[c\_{00}, c\_{01}, c\_{02}, ... , c\_{10}, c\_{11}, c\_{12}, ...\\\]

and `np.dot(V, c.flat)` and `polyval2d(x, y, c)` will be the same up to roundoff. This equivalence is useful both for least squares fitting and for the evaluation of a large number of 2-D polynomials of the same degrees and sample points.

Parameters:

**x, y**array\_like

Arrays of point coordinates, all of the same shape. The dtypes will be converted to either float64 or complex128 depending on whether any of the elements are complex. Scalars are converted to 1-D arrays.

**deg**list of ints

List of maximum degrees of the form \[x\_deg, y\_deg\].

Returns:

**vander2d**ndarray

The shape of the returned matrix is `x.shape + (order,)`, where \\(order = (deg\[0\]+1)\*(deg\[1\]+1)\\). The dtype will be the same as the converted _x_ and _y_.

See also

[`polyvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html#numpy.polynomial.polynomial.polyvander "numpy.polynomial.polynomial.polyvander")
, [`polyvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander3d.html#numpy.polynomial.polynomial.polyvander3d "numpy.polynomial.polynomial.polyvander3d")
, [`polyval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html#numpy.polynomial.polynomial.polyval2d "numpy.polynomial.polynomial.polyval2d")
, [`polyval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval3d.html#numpy.polynomial.polynomial.polyval3d "numpy.polynomial.polynomial.polyval3d")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

The 2-D pseudo-Vandermonde matrix of degree `[1, 2]` and sample points `x = [-1, 2]` and `y = [1, 3]` is as follows:

\>>> from numpy.polynomial import polynomial as P
\>>> x \= np.array(\[\-1, 2\])
\>>> y \= np.array(\[1, 3\])
\>>> m, n \= 1, 2
\>>> deg \= np.array(\[m, n\])
\>>> V \= P.polyvander2d(x\=x, y\=y, deg\=deg)
\>>> V
array(\[\[ 1.,  1.,  1., -1., -1., -1.\],\
       \[ 1.,  3.,  9.,  2.,  6., 18.\]\])

Copy to clipboard

We can verify the columns for any `0 <= i <= m` and `0 <= j <= n`:

\>>> i, j \= 0, 1
\>>> V\[:, (deg\[1\]+1)\*i + j\] \== x\*\*i \* y\*\*j
array(\[ True,  True\])

Copy to clipboard

The (1D) Vandermonde matrix of sample points `x` and degree `m` is a special case of the (2D) pseudo-Vandermonde matrix with `y` points all zero and degree `[m, 0]`.

\>>> P.polyvander2d(x\=x, y\=0\*x, deg\=(m, 0)) \== P.polyvander(x\=x, deg\=m)
array(\[\[ True,  True\],\
       \[ True,  True\]\])

Copy to clipboard

Go BackOpen In Tab

On this page