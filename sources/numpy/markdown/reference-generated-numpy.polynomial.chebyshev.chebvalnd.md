[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebvalnd[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html#numpy-polynomial-chebyshev-chebvalnd "Link to this heading")

================================================================================================================================================================================================

polynomial.chebyshev.chebvalnd(_pts_, _c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L1305-L1353)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html#numpy.polynomial.chebyshev.chebvalnd "Link to this definition")

Evaluate an N-D Chebyshev series at points.

This function returns the values:

\\\[p(pts, c) = \\sum\_{i\_1, i\_2, \\dots, i\_n} c\_{i\_1, i\_2, \\dots, i\_n} \* T\_{i\_1}(x\_1) \* T\_{i\_2}(x\_2) \\dots T\_{i\_n}(x\_n)\\\]

where \\(x\_1, x\_2, \\dots, x\_n = pts\\). Note that _pts_ may also be an _(n, m)_ array.

The parameters in _pts_ are converted to arrays only if they are tuples or lists, otherwise they are treated as scalars and they must have the same shape after conversion. In either case, either the elements of _pts_ or their elements must support multiplication and addition both with themselves and with the elements of _c_.

If _c_ has fewer than N dimensions, ones are implicitly appended to its shape to make it N-D. The shape of the result will be c.shape\[N:\] + pts\[0\].shape.

Parameters:

**pts**tuple or list of array\_like, compatible objects

The N-dimensional series is evaluated at the points `(x_1, x_2, ..., x_n)` provided in the _pts_ iterable, where all elements must have the same shape. If any element is a list or tuple, it is first converted to an ndarray, otherwise it is left unchanged and if it isn’t an ndarray it is treated as a scalar.

**c**array\_like

Array of coefficients ordered so that the coefficient of the term of multi-degree i,j,k,… is contained in `c[i,j,k,...]`. If _c_ has dimension greater than N, the remaining indices enumerate multiple sets of coefficients.

Returns:

**values**ndarray, compatible object

The values of the multidimensional Chebyshev series on points formed with N-tuples of corresponding values from _pts_.

See also

[`chebval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval.html#numpy.polynomial.chebyshev.chebval "numpy.polynomial.chebyshev.chebval")
, [`chebval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval2d.html#numpy.polynomial.chebyshev.chebval2d "numpy.polynomial.chebyshev.chebval2d")
, [`chebval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval3d.html#numpy.polynomial.chebyshev.chebval3d "numpy.polynomial.chebyshev.chebval3d")

On this page