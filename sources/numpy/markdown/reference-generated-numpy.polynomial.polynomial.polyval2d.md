[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polyval2d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polyval2d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyval2d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html#numpy-polynomial-polynomial-polyval2d "Link to this heading")

===================================================================================================================================================================================================

polynomial.polynomial.polyval2d(_x_, _y_, _c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L854-L904)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html#numpy.polynomial.polynomial.polyval2d "Link to this definition")

Evaluate a 2-D polynomial at points (x, y).

This function returns the value

\\\[p(x,y) = \\sum\_{i,j} c\_{i,j} \* x^i \* y^j\\\]

The parameters _x_ and _y_ are converted to arrays only if they are tuples or a lists, otherwise they are treated as a scalars and they must have the same shape after conversion. In either case, either _x_ and _y_ or their elements must support multiplication and addition both with themselves and with the elements of _c_.

If _c_ has fewer than two dimensions, ones are implicitly appended to its shape to make it 2-D. The shape of the result will be c.shape\[2:\] + x.shape.

Parameters:

**x, y**array\_like, compatible objects

The two dimensional series is evaluated at the points `(x, y)`, where _x_ and _y_ must have the same shape. If _x_ or _y_ is a list or tuple, it is first converted to an ndarray, otherwise it is left unchanged and, if it isn’t an ndarray, it is treated as a scalar.

**c**array\_like

Array of coefficients ordered so that the coefficient of the term of multi-degree i,j is contained in `c[i,j]`. If _c_ has dimension greater than two the remaining indices enumerate multiple sets of coefficients.

Returns:

**values**ndarray, compatible object

The values of the two dimensional polynomial at points formed with pairs of corresponding values from _x_ and _y_.

See also

[`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")
, [`polygrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polygrid2d.html#numpy.polynomial.polynomial.polygrid2d "numpy.polynomial.polynomial.polygrid2d")
, [`polyval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval3d.html#numpy.polynomial.polynomial.polyval3d "numpy.polynomial.polynomial.polyval3d")
, [`polygrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polygrid3d.html#numpy.polynomial.polynomial.polygrid3d "numpy.polynomial.polynomial.polygrid3d")

Examples

Try it in your browser!

\>>> from numpy.polynomial import polynomial as P
\>>> c \= ((1, 2, 3), (4, 5, 6))
\>>> P.polyval2d(1, 1, c)
21.0

Copy to clipboard

Go BackOpen In Tab

On this page