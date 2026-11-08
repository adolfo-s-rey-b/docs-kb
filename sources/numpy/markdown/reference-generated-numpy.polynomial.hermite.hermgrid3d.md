[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid3d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.hermgrid3d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.hermgrid3d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid3d.html#numpy-polynomial-hermite-hermgrid3d "Link to this heading")

=============================================================================================================================================================================================

polynomial.hermite.hermgrid3d(_x_, _y_, _z_, _c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite.py#L1111-L1172)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid3d.html#numpy.polynomial.hermite.hermgrid3d "Link to this definition")

Evaluate a 3-D Hermite series on the Cartesian product of x, y, and z.

This function returns the values:

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

[`hermval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval.html#numpy.polynomial.hermite.hermval "numpy.polynomial.hermite.hermval")
, [`hermval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval2d.html#numpy.polynomial.hermite.hermval2d "numpy.polynomial.hermite.hermval2d")
, [`hermgrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid2d.html#numpy.polynomial.hermite.hermgrid2d "numpy.polynomial.hermite.hermgrid2d")
, [`hermval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval3d.html#numpy.polynomial.hermite.hermval3d "numpy.polynomial.hermite.hermval3d")

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite import hermgrid3d
\>>> x \= \[1, 2\]
\>>> y \= \[4, 5\]
\>>> z \= \[6, 7\]
\>>> c \= \[\[\[1, 2, 3\], \[4, 5, 6\]\], \[\[7, 8, 9\], \[10, 11, 12\]\]\]
\>>> hermgrid3d(x, y, z, c)
array(\[\[\[ 40077.,  54117.\],\
        \[ 49293.,  66561.\]\],\
       \[\[ 72375.,  97719.\],\
        \[ 88975., 120131.\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page