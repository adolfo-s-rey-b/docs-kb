[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander3d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polyvander3d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyvander3d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander3d.html#numpy-polynomial-polynomial-polyvander3d "Link to this heading")

============================================================================================================================================================================================================

polynomial.polynomial.polyvander3d(_x_, _y_, _z_, _deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L1274-L1345)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander3d.html#numpy.polynomial.polynomial.polyvander3d "Link to this definition")

Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees _deg_ and sample points `(x, y, z)`. If _l_, _m_, _n_ are the given degrees in _x_, _y_, _z_, then The pseudo-Vandermonde matrix is defined by

\\\[V\[..., (m+1)(n+1)i + (n+1)j + k\] = x^i \* y^j \* z^k,\\\]

where `0 <= i <= l`, `0 <= j <= m`, and `0 <= j <= n`. The leading indices of _V_ index the points `(x, y, z)` and the last index encodes the powers of _x_, _y_, and _z_.

If `V = polyvander3d(x, y, z, [xdeg, ydeg, zdeg])`, then the columns of _V_ correspond to the elements of a 3-D coefficient array _c_ of shape (xdeg + 1, ydeg + 1, zdeg + 1) in the order

\\\[c\_{000}, c\_{001}, c\_{002},... , c\_{010}, c\_{011}, c\_{012},...\\\]

and `np.dot(V, c.flat)` and `polyval3d(x, y, z, c)` will be the same up to roundoff. This equivalence is useful both for least squares fitting and for the evaluation of a large number of 3-D polynomials of the same degrees and sample points.

Parameters:

**x, y, z**array\_like

Arrays of point coordinates, all of the same shape. The dtypes will be converted to either float64 or complex128 depending on whether any of the elements are complex. Scalars are converted to 1-D arrays.

**deg**list of ints

List of maximum degrees of the form \[x\_deg, y\_deg, z\_deg\].

Returns:

**vander3d**ndarray

The shape of the returned matrix is `x.shape + (order,)`, where \\(order = (deg\[0\]+1)\*(deg\[1\]+1)\*(deg\[2\]+1)\\). The dtype will be the same as the converted _x_, _y_, and _z_.

See also

[`polyvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html#numpy.polynomial.polynomial.polyvander "numpy.polynomial.polynomial.polyvander")
, [`polyvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander3d.html#numpy.polynomial.polynomial.polyvander3d "numpy.polynomial.polynomial.polyvander3d")
, [`polyval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html#numpy.polynomial.polynomial.polyval2d "numpy.polynomial.polynomial.polyval2d")
, [`polyval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval3d.html#numpy.polynomial.polynomial.polyval3d "numpy.polynomial.polynomial.polyval3d")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.polynomial import polynomial as P
\>>> x \= np.asarray(\[\-1, 2, 1\])
\>>> y \= np.asarray(\[1, \-2, \-3\])
\>>> z \= np.asarray(\[2, 2, 5\])
\>>> l, m, n \= \[2, 2, 1\]
\>>> deg \= \[l, m, n\]
\>>> V \= P.polyvander3d(x\=x, y\=y, z\=z, deg\=deg)
\>>> V
array(\[\[  1.,   2.,   1.,   2.,   1.,   2.,  -1.,  -2.,  -1.,\
         -2.,  -1.,  -2.,   1.,   2.,   1.,   2.,   1.,   2.\],\
       \[  1.,   2.,  -2.,  -4.,   4.,   8.,   2.,   4.,  -4.,\
         -8.,   8.,  16.,   4.,   8.,  -8., -16.,  16.,  32.\],\
       \[  1.,   5.,  -3., -15.,   9.,  45.,   1.,   5.,  -3.,\
        -15.,   9.,  45.,   1.,   5.,  -3., -15.,   9.,  45.\]\])

Copy to clipboard

We can verify the columns for any `0 <= i <= l`, `0 <= j <= m`, and `0 <= k <= n`

\>>> i, j, k \= 2, 1, 0
\>>> V\[:, (m+1)\*(n+1)\*i + (n+1)\*j + k\] \== x\*\*i \* y\*\*j \* z\*\*k
array(\[ True,  True,  True\])

Copy to clipboard

Go BackOpen In Tab

On this page