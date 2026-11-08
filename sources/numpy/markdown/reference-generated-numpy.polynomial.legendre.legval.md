[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.legval.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.legval.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.legval.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.legval.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.legval.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.legval.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.legval.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.legval.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.legval.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.legval.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.legval.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.legval.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.legval.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.legval.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.legval.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.legval.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.legval.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.legval.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.legval.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.legval.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.legval[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval.html#numpy-polynomial-legendre-legval "Link to this heading")

====================================================================================================================================================================================

polynomial.legendre.legval(_x_, _c_, _tensor\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L829-L909)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval.html#numpy.polynomial.legendre.legval "Link to this definition")

Evaluate a Legendre series at points x.

If _c_ is of length `n + 1`, this function returns the value:

\\\[p(x) = c\_0 \* L\_0(x) + c\_1 \* L\_1(x) + ... + c\_n \* L\_n(x)\\\]

The parameter _x_ is converted to an array only if it is a tuple or a list, otherwise it is treated as a scalar. In either case, either _x_ or its elements must support multiplication and addition both with themselves and with the elements of _c_.

If _c_ is a 1-D array, then `p(x)` will have the same shape as _x_. If _c_ is multidimensional, then the shape of the result depends on the value of _tensor_. If _tensor_ is true the shape will be c.shape\[1:\] + x.shape. If _tensor_ is false the shape will be c.shape\[1:\]. Note that scalars have shape (,).

Trailing zeros in the coefficients will be used in the evaluation, so they should be avoided if efficiency is a concern.

Parameters:

**x**array\_like, compatible object

If _x_ is a list or tuple, it is converted to an ndarray, otherwise it is left unchanged and treated as a scalar. In either case, _x_ or its elements must support addition and multiplication with themselves and with the elements of _c_.

**c**array\_like

Array of coefficients ordered so that the coefficients for terms of degree n are contained in c\[n\]. If _c_ is multidimensional the remaining indices enumerate multiple polynomials. In the two dimensional case the coefficients may be thought of as stored in the columns of _c_.

**tensor**boolean, optional

If True, the shape of the coefficient array is extended with ones on the right, one for each dimension of _x_. Scalars have dimension 0 for this action. The result is that every column of coefficients in _c_ is evaluated for every element of _x_. If False, _x_ is broadcast over the columns of _c_ for the evaluation. This keyword is useful when _c_ is multidimensional. The default value is True.

Returns:

**values**ndarray, algebra\_like

The shape of the return value is described above.

See also

[`legval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval2d.html#numpy.polynomial.legendre.legval2d "numpy.polynomial.legendre.legval2d")
, [`leggrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid2d.html#numpy.polynomial.legendre.leggrid2d "numpy.polynomial.legendre.leggrid2d")
, [`legval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval3d.html#numpy.polynomial.legendre.legval3d "numpy.polynomial.legendre.legval3d")
, [`leggrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid3d.html#numpy.polynomial.legendre.leggrid3d "numpy.polynomial.legendre.leggrid3d")

Notes

The evaluation uses Clenshaw recursion, aka synthetic division.

On this page