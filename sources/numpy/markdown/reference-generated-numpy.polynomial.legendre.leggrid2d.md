[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid2d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.leggrid2d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.leggrid2d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.leggrid2d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid2d.html#numpy-polynomial-legendre-leggrid2d "Link to this heading")

=============================================================================================================================================================================================

polynomial.legendre.leggrid2d(_x_, _y_, _c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L955-L999)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid2d.html#numpy.polynomial.legendre.leggrid2d "Link to this definition")

Evaluate a 2-D Legendre series on the Cartesian product of x and y.

This function returns the values:

\\\[p(a,b) = \\sum\_{i,j} c\_{i,j} \* L\_i(a) \* L\_j(b)\\\]

where the points `(a, b)` consist of all pairs formed by taking _a_ from _x_ and _b_ from _y_. The resulting points form a grid with _x_ in the first dimension and _y_ in the second.

The parameters _x_ and _y_ are converted to arrays only if they are tuples or a lists, otherwise they are treated as a scalars. In either case, either _x_ and _y_ or their elements must support multiplication and addition both with themselves and with the elements of _c_.

If _c_ has fewer than two dimensions, ones are implicitly appended to its shape to make it 2-D. The shape of the result will be c.shape\[2:\] + x.shape + y.shape.

Parameters:

**x, y**array\_like, compatible objects

The two dimensional series is evaluated at the points in the Cartesian product of _x_ and _y_. If _x_ or _y_ is a list or tuple, it is first converted to an ndarray, otherwise it is left unchanged and, if it isn’t an ndarray, it is treated as a scalar.

**c**array\_like

Array of coefficients ordered so that the coefficient of the term of multi-degree i,j is contained in `c[i,j]`. If _c_ has dimension greater than two the remaining indices enumerate multiple sets of coefficients.

Returns:

**values**ndarray, compatible object

The values of the two dimensional Chebyshev series at points in the Cartesian product of _x_ and _y_.

See also

[`legval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval.html#numpy.polynomial.legendre.legval "numpy.polynomial.legendre.legval")
, [`legval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval2d.html#numpy.polynomial.legendre.legval2d "numpy.polynomial.legendre.legval2d")
, [`legval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval3d.html#numpy.polynomial.legendre.legval3d "numpy.polynomial.legendre.legval3d")
, [`leggrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid3d.html#numpy.polynomial.legendre.leggrid3d "numpy.polynomial.legendre.leggrid3d")

On this page