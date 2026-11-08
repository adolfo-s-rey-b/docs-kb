[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyint.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polyint.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyint.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polyint.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polyint.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polyint.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polyint.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polyint.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polyint.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyint[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyint.html#numpy-polynomial-polynomial-polyint "Link to this heading")

=============================================================================================================================================================================================

polynomial.polynomial.polyint(_c_, _m\=1_, _k\=\[\]_, _lbnd\=0_, _scl\=1_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L546-L660)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyint.html#numpy.polynomial.polynomial.polyint "Link to this definition")

Integrate a polynomial.

Returns the polynomial coefficients _c_ integrated _m_ times from _lbnd_ along _axis_. At each iteration the resulting series is **multiplied** by _scl_ and an integration constant, _k_, is added. The scaling factor is for use in a linear change of variable. (“Buyer beware”: note that, depending on what one is doing, one may want _scl_ to be the reciprocal of what one might expect; for more information, see the Notes section below.) The argument _c_ is an array of coefficients, from low to high degree along each axis, e.g., \[1,2,3\] represents the polynomial `1 + 2*x + 3*x**2` while \[\[1,2\],\[1,2\]\] represents `1 + 1*x + 2*y + 2*x*y` if axis=0 is `x` and axis=1 is `y`.

Parameters:

**c**array\_like

1-D array of polynomial coefficients, ordered from low to high.

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

Coefficient array of the integral.

Raises:

ValueError

If `m < 1`, `len(k) > m`, `np.ndim(lbnd) != 0`, or `np.ndim(scl) != 0`.

See also

[`polyder`](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html#numpy.polyder "numpy.polyder")

Notes

Note that the result of each integration is _multiplied_ by _scl_. Why is this important to note? Say one is making a linear change of variable \\(u = ax + b\\) in an integral relative to _x_. Then \\(dx = du/a\\), so one will need to set _scl_ equal to \\(1/a\\) - perhaps not what one would have first thought.

Examples

Try it in your browser!

\>>> from numpy.polynomial import polynomial as P
\>>> c \= (1, 2, 3)
\>>> P.polyint(c)  \# should return array(\[0, 1, 1, 1\])
array(\[0.,  1.,  1.,  1.\])
\>>> P.polyint(c, 3)  \# should return array(\[0, 0, 0, 1/6, 1/12, 1/20\])
 array(\[ 0.        ,  0.        ,  0.        ,  0.16666667,  0.08333333, # may vary\
         0.05      \])
\>>> P.polyint(c, k\=3)  \# should return array(\[3, 1, 1, 1\])
array(\[3.,  1.,  1.,  1.\])
\>>> P.polyint(c,lbnd\=-2)  \# should return array(\[6, 1, 1, 1\])
array(\[6.,  1.,  1.,  1.\])
\>>> P.polyint(c,scl\=-2)  \# should return array(\[0, -2, -2, -2\])
array(\[ 0., -2., -2., -2.\])

Copy to clipboard

Go BackOpen In Tab

On this page