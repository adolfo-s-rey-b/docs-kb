[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebgrid3d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html#numpy-polynomial-chebyshev-chebgrid3d "Link to this heading")

===================================================================================================================================================================================================

polynomial.chebyshev.chebgrid3d(_x_, _y_, _z_, _c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L1356-L1403)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html#numpy.polynomial.chebyshev.chebgrid3d "Link to this definition")

Evaluate a 3-D Chebyshev series on the Cartesian product of x, y, and z.

This function returns the values:

\\\[p(a,b,c) = \\sum\_{i,j,k} c\_{i,j,k} \* T\_i(a) \* T\_j(b) \* T\_k(c)\\\]

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

[`chebval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval.html#numpy.polynomial.chebyshev.chebval "numpy.polynomial.chebyshev.chebval")
, [`chebval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval2d.html#numpy.polynomial.chebyshev.chebval2d "numpy.polynomial.chebyshev.chebval2d")
, [`chebgrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgrid2d.html#numpy.polynomial.chebyshev.chebgrid2d "numpy.polynomial.chebyshev.chebgrid2d")
, [`chebval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval3d.html#numpy.polynomial.chebyshev.chebval3d "numpy.polynomial.chebyshev.chebval3d")

On this page