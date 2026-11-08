[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid3d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.leggrid3d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid3d.html#numpy-polynomial-legendre-leggrid3d "Link to this heading")

=============================================================================================================================================================================================

polynomial.legendre.leggrid3d(_x_, _y_, _z_, _c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L1098-L1145)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid3d.html#numpy.polynomial.legendre.leggrid3d "Link to this definition")

Evaluate a 3-D Legendre series on the Cartesian product of x, y, and z.

This function returns the values:

\\\[p(a,b,c) = \\sum\_{i,j,k} c\_{i,j,k} \* L\_i(a) \* L\_j(b) \* L\_k(c)\\\]

where the points `(a, b, c)` consist of all triples formed by taking _a_ from _x_, _b_ from _y_, and _c_ from _z_. The resulting points form a grid with _x_ in the first dimension, _y_ in the second, and _z_ in the third.

The parameters _x_, _y_, and _z_ are converted to arrays only if they are tuples or a lists, otherwise they are treated as a scalars. In either case, either _x_, _y_, and _z_ or their elements must support multiplication and addition both with themselves and with the elements of _c_.

If _c_ has fewer than three dimensions, ones are implicitly appended to its shape to make it 3-D. The shape of the result will be c.shape\[3:\] + x.shape + y.shape + z.shape.

Parameters:

**x, y, z**array\_like, compatible objects

The three dimensional series is evaluated at the points in the Cartesian product of _x_, _y_, and _z_. If _x_, _y_, or _z_ is a list or tuple, it is first converted to an ndarray, otherwise it is left unchanged and, if it isn’t an ndarray, it is treated as a scalar.

**c**array\_like

Array of coefficients ordered so that the coefficients for terms of degree i,j are contained in `c[i,j]`. If _c_ has dimension greater than two the remaining indices enumerate multiple sets of coefficients.

Returns:

**values**ndarray, compatible object

The values of the two dimensional polynomial at points in the Cartesian product of _x_ and _y_.

See also

[`legval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval.html#numpy.polynomial.legendre.legval "numpy.polynomial.legendre.legval")
, [`legval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval2d.html#numpy.polynomial.legendre.legval2d "numpy.polynomial.legendre.legval2d")
, [`leggrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid2d.html#numpy.polynomial.legendre.leggrid2d "numpy.polynomial.legendre.leggrid2d")
, [`legval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval3d.html#numpy.polynomial.legendre.legval3d "numpy.polynomial.legendre.legval3d")

On this page