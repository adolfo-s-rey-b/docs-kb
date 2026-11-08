[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebint.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebint[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebint.html#numpy-polynomial-chebyshev-chebint "Link to this heading")

==========================================================================================================================================================================================

polynomial.chebyshev.chebint(_c_, _m\=1_, _k\=\[\]_, _lbnd\=0_, _scl\=1_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L963-L1085)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebint.html#numpy.polynomial.chebyshev.chebint "Link to this definition")

Integrate a Chebyshev series.

Returns the Chebyshev series coefficients _c_ integrated _m_ times from _lbnd_ along _axis_. At each iteration the resulting series is **multiplied** by _scl_ and an integration constant, _k_, is added. The scaling factor is for use in a linear change of variable. (“Buyer beware”: note that, depending on what one is doing, one may want _scl_ to be the reciprocal of what one might expect; for more information, see the Notes section below.) The argument _c_ is an array of coefficients from low to high degree along each axis, e.g., \[1,2,3\] represents the series `T_0 + 2*T_1 + 3*T_2` while \[\[1,2\],\[1,2\]\] represents `1*T_0(x)*T_0(y) + 1*T_1(x)*T_0(y) + 2*T_0(x)*T_1(y) + 2*T_1(x)*T_1(y)` if axis=0 is `x` and axis=1 is `y`.

Parameters:

**c**array\_like

Array of Chebyshev series coefficients. If c is multidimensional the different axis correspond to different variables with the degree in each axis given by the corresponding index.

**m**int, optional

Order of integration, must be positive. (Default: 1)

**k**{\[\], list, scalar}, optional

Integration constant(s). The value of the first integral at zero is the first value in the list, the value of the second integral at zero is the second value, etc. If `k == []` (the default), all constants are set to zero. If `m == 1`, a single scalar can be given instead of a list.

**lbnd**scalar, optional

The lower bound of the integral. (Default: 0)

**scl**scalar, optional

Following each integration the result is _multiplied_ by _scl_ before the integration constant is added. (Default: 1)

**axis**int, optional

Axis over which the integral is taken. (Default: 0).

Returns:

**S**ndarray

C-series coefficients of the integral.

Raises:

ValueError

If `m < 1`, `len(k) > m`, `np.ndim(lbnd) != 0`, or `np.ndim(scl) != 0`.

See also

[`chebder`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebder.html#numpy.polynomial.chebyshev.chebder "numpy.polynomial.chebyshev.chebder")

Notes

Note that the result of each integration is _multiplied_ by _scl_. Why is this important to note? Say one is making a linear change of variable \\(u = ax + b\\) in an integral relative to _x_. Then \\(dx = du/a\\), so one will need to set _scl_ equal to \\(1/a\\)\- perhaps not what one would have first thought.

Also note that, in general, the result of integrating a C-series needs to be “reprojected” onto the C-series basis set. Thus, typically, the result of this function is “unintuitive,” albeit correct; see Examples section below.

Examples

Try it in your browser!

\>>> from numpy.polynomial import chebyshev as C
\>>> c \= (1,2,3)
\>>> C.chebint(c)
array(\[ 0.5, -0.5,  0.5,  0.5\])
\>>> C.chebint(c,3)
array(\[ 0.03125   , -0.1875    ,  0.04166667, -0.05208333,  0.01041667, # may vary\
    0.00625   \])
\>>> C.chebint(c, k\=3)
array(\[ 3.5, -0.5,  0.5,  0.5\])
\>>> C.chebint(c,lbnd\=-2)
array(\[ 8.5, -0.5,  0.5,  0.5\])
\>>> C.chebint(c,scl\=-2)
array(\[-1.,  1., -1., -1.\])

Copy to clipboard

Go BackOpen In Tab

On this page