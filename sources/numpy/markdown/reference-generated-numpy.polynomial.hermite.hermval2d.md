[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval2d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.hermval2d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval2d.html#numpy-polynomial-hermite-hermval2d "Link to this heading")

==========================================================================================================================================================================================

polynomial.hermite.hermval2d(_x_, _y_, _c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite.py#L892-L942)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval2d.html#numpy.polynomial.hermite.hermval2d "Link to this definition")

Evaluate a 2-D Hermite series at points (x, y).

This function returns the values:

\\\[p(x,y) = \\sum\_{i,j} c\_{i,j} \* H\_i(x) \* H\_j(y)\\\]

The parameters _x_ and _y_ are converted to arrays only if they are tuples or a lists, otherwise they are treated as a scalars and they must have the same shape after conversion. In either case, either _x_ and _y_ or their elements must support multiplication and addition both with themselves and with the elements of _c_.

If _c_ is a 1-D array a one is implicitly appended to its shape to make it 2-D. The shape of the result will be c.shape\[2:\] + x.shape.

Parameters:

**x, y**array\_like, compatible objects

The two dimensional series is evaluated at the points `(x, y)`, where _x_ and _y_ must have the same shape. If _x_ or _y_ is a list or tuple, it is first converted to an ndarray, otherwise it is left unchanged and if it isn’t an ndarray it is treated as a scalar.

**c**array\_like

Array of coefficients ordered so that the coefficient of the term of multi-degree i,j is contained in `c[i,j]`. If _c_ has dimension greater than two the remaining indices enumerate multiple sets of coefficients.

Returns:

**values**ndarray, compatible object

The values of the two dimensional polynomial at points formed with pairs of corresponding values from _x_ and _y_.

See also

[`hermval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval.html#numpy.polynomial.hermite.hermval "numpy.polynomial.hermite.hermval")
, [`hermgrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid2d.html#numpy.polynomial.hermite.hermgrid2d "numpy.polynomial.hermite.hermgrid2d")
, [`hermval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval3d.html#numpy.polynomial.hermite.hermval3d "numpy.polynomial.hermite.hermval3d")
, [`hermgrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid3d.html#numpy.polynomial.hermite.hermgrid3d "numpy.polynomial.hermite.hermgrid3d")

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite import hermval2d
\>>> x \= \[1, 2\]
\>>> y \= \[4, 5\]
\>>> c \= \[\[1, 2, 3\], \[4, 5, 6\]\]
\>>> hermval2d(x, y, c)
array(\[1035., 2883.\])

Copy to clipboard

Go BackOpen In Tab

On this page