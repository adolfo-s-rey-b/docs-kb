[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.hermeval3d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html#numpy-polynomial-hermite-e-hermeval3d "Link to this heading")

====================================================================================================================================================================================================

polynomial.hermite\_e.hermeval3d(_x_, _y_, _z_, _c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L979-L1021)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html#numpy.polynomial.hermite_e.hermeval3d "Link to this definition")

Evaluate a 3-D Hermite\_e series at points (x, y, z).

This function returns the values:

\\\[p(x,y,z) = \\sum\_{i,j,k} c\_{i,j,k} \* He\_i(x) \* He\_j(y) \* He\_k(z)\\\]

The parameters _x_, _y_, and _z_ are converted to arrays only if they are tuples or a lists, otherwise they are treated as a scalars and they must have the same shape after conversion. In either case, either _x_, _y_, and _z_ or their elements must support multiplication and addition both with themselves and with the elements of _c_.

If _c_ has fewer than 3 dimensions, ones are implicitly appended to its shape to make it 3-D. The shape of the result will be c.shape\[3:\] + x.shape.

Parameters:

**x, y, z**array\_like, compatible object

The three dimensional series is evaluated at the points _(x, y, z)_, where _x_, _y_, and _z_ must have the same shape. If any of _x_, _y_, or _z_ is a list or tuple, it is first converted to an ndarray, otherwise it is left unchanged and if it isn’t an ndarray it is treated as a scalar.

**c**array\_like

Array of coefficients ordered so that the coefficient of the term of multi-degree i,j,k is contained in `c[i,j,k]`. If _c_ has dimension greater than 3 the remaining indices enumerate multiple sets of coefficients.

Returns:

**values**ndarray, compatible object

The values of the multidimensional polynomial on points formed with triples of corresponding values from _x_, _y_, and _z_.

See also

[`hermeval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval.html#numpy.polynomial.hermite_e.hermeval "numpy.polynomial.hermite_e.hermeval")
, [`hermeval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval2d.html#numpy.polynomial.hermite_e.hermeval2d "numpy.polynomial.hermite_e.hermeval2d")
, [`hermegrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermegrid2d.html#numpy.polynomial.hermite_e.hermegrid2d "numpy.polynomial.hermite_e.hermegrid2d")
, [`hermegrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermegrid3d.html#numpy.polynomial.hermite_e.hermegrid3d "numpy.polynomial.hermite_e.hermegrid3d")

On this page