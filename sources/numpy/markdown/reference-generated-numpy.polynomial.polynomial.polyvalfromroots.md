[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyvalfromroots[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html#numpy-polynomial-polynomial-polyvalfromroots "Link to this heading")

========================================================================================================================================================================================================================

polynomial.polynomial.polyvalfromroots(_x_, _r_, _tensor\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L762-L846)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html#numpy.polynomial.polynomial.polyvalfromroots "Link to this definition")

Evaluate a polynomial specified by its roots at points x.

If _r_ is of length `N`, this function returns the value

\\\[p(x) = \\prod\_{n=1}^{N} (x - r\_n)\\\]

The parameter _x_ is converted to an array only if it is a tuple or a list, otherwise it is treated as a scalar. In either case, either _x_ or its elements must support multiplication and addition both with themselves and with the elements of _r_.

If _r_ is a 1-D array, then `p(x)` will have the same shape as _x_. If _r_ is multidimensional, then the shape of the result depends on the value of _tensor_. If _tensor_ is `True` the shape will be r.shape\[1:\] + x.shape; that is, each polynomial is evaluated at every value of _x_. If _tensor_ is `False`, the shape will be r.shape\[1:\]; that is, each polynomial is evaluated only for the corresponding broadcast value of _x_. Note that scalars have shape (,).

Parameters:

**x**array\_like, compatible object

If _x_ is a list or tuple, it is converted to an ndarray, otherwise it is left unchanged and treated as a scalar. In either case, _x_ or its elements must support addition and multiplication with with themselves and with the elements of _r_.

**r**array\_like

Array of roots. If _r_ is multidimensional the first index is the root index, while the remaining indices enumerate multiple polynomials. For instance, in the two dimensional case the roots of each polynomial may be thought of as stored in the columns of _r_.

**tensor**boolean, optional

If True, the shape of the roots array is extended with ones on the right, one for each dimension of _x_. Scalars have dimension 0 for this action. The result is that every column of coefficients in _r_ is evaluated for every element of _x_. If False, _x_ is broadcast over the columns of _r_ for the evaluation. This keyword is useful when _r_ is multidimensional. The default value is True.

Returns:

**values**ndarray, compatible object

The shape of the returned array is described above.

See also

[`polyroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyroots.html#numpy.polynomial.polynomial.polyroots "numpy.polynomial.polynomial.polyroots")
, [`polyfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfromroots.html#numpy.polynomial.polynomial.polyfromroots "numpy.polynomial.polynomial.polyfromroots")
, [`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")

Examples

Try it in your browser!

\>>> from numpy.polynomial.polynomial import polyvalfromroots
\>>> polyvalfromroots(1, \[1, 2, 3\])
0.0
\>>> a \= np.arange(4).reshape(2, 2)
\>>> a
array(\[\[0, 1\],\
       \[2, 3\]\])
\>>> polyvalfromroots(a, \[\-1, 0, 1\])
array(\[\[-0.,   0.\],\
       \[ 6.,  24.\]\])
\>>> r \= np.arange(\-2, 2).reshape(2,2)  \# multidimensional coefficients
\>>> r \# each column of r defines one polynomial
array(\[\[-2, -1\],\
       \[ 0,  1\]\])
\>>> b \= \[\-2, 1\]
\>>> polyvalfromroots(b, r, tensor\=True)
array(\[\[-0.,  3.\],\
       \[ 3., 0.\]\])
\>>> polyvalfromroots(b, r, tensor\=False)
array(\[-0.,  0.\])

Copy to clipboard

Go BackOpen In Tab

On this page