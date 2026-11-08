[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.hermevander3d[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html#numpy-polynomial-hermite-e-hermevander3d "Link to this heading")

=============================================================================================================================================================================================================

polynomial.hermite\_e.hermevander3d(_x_, _y_, _z_, _deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L1233-L1278)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html#numpy.polynomial.hermite_e.hermevander3d "Link to this definition")

Pseudo-Vandermonde matrix of given degrees.

Returns the pseudo-Vandermonde matrix of degrees _deg_ and sample points `(x, y, z)`. If _l_, _m_, _n_ are the given degrees in _x_, _y_, _z_, then Hehe pseudo-Vandermonde matrix is defined by

where `0 <= i <= l`, `0 <= j <= m`, and `0 <= j <= n`. The leading indices of _V_ index the points `(x, y, z)` and the last index encodes the degrees of the HermiteE polynomials.

If `V = hermevander3d(x, y, z, [xdeg, ydeg, zdeg])`, then the columns of _V_ correspond to the elements of a 3-D coefficient array _c_ of shape (xdeg + 1, ydeg + 1, zdeg + 1) in the order

c\_{000}, c\_{001}, c\_{002},... , c\_{010}, c\_{011}, c\_{012},...

and `np.dot(V, c.flat)` and `hermeval3d(x, y, z, c)` will be the same up to roundoff. This equivalence is useful both for least squares fitting and for the evaluation of a large number of 3-D HermiteE series of the same degrees and sample points.

Parameters:

**x, y, z**array\_like

Arrays of point coordinates, all of the same shape. The dtypes will be converted to either float64 or complex128 depending on whether any of the elements are complex. Scalars are converted to 1-D arrays.

**deg**list of ints

List of maximum degrees of the form \[x\_deg, y\_deg, z\_deg\].

Returns:

**vander3d**ndarray

The shape of the returned matrix is `x.shape + (order,)`, where order = (deg\[0\]+1)\*(deg\[1\]+1)\*(deg\[2\]+1). The dtype will be the same as the converted _x_, _y_, and _z_.

See also

[`hermevander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander.html#numpy.polynomial.hermite_e.hermevander "numpy.polynomial.hermite_e.hermevander")
, [`hermevander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html#numpy.polynomial.hermite_e.hermevander3d "numpy.polynomial.hermite_e.hermevander3d")
, [`hermeval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval2d.html#numpy.polynomial.hermite_e.hermeval2d "numpy.polynomial.hermite_e.hermeval2d")
, [`hermeval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html#numpy.polynomial.hermite_e.hermeval3d "numpy.polynomial.hermite_e.hermeval3d")

On this page