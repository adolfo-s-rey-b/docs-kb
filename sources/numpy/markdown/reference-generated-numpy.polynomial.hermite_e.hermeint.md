[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeint.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.hermeint.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.hermeint.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.hermeint[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeint.html#numpy-polynomial-hermite-e-hermeint "Link to this heading")

==============================================================================================================================================================================================

polynomial.hermite\_e.hermeint(_c_, _m\=1_, _k\=\[\]_, _lbnd\=0_, _scl\=1_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L676-L793)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeint.html#numpy.polynomial.hermite_e.hermeint "Link to this definition")

Integrate a Hermite\_e series.

Returns the Hermite\_e series coefficients _c_ integrated _m_ times from _lbnd_ along _axis_. At each iteration the resulting series is **multiplied** by _scl_ and an integration constant, _k_, is added. The scaling factor is for use in a linear change of variable. (“Buyer beware”: note that, depending on what one is doing, one may want _scl_ to be the reciprocal of what one might expect; for more information, see the Notes section below.) The argument _c_ is an array of coefficients from low to high degree along each axis, e.g., \[1,2,3\] represents the series `H_0 + 2*H_1 + 3*H_2` while \[\[1,2\],\[1,2\]\] represents `1*H_0(x)*H_0(y) + 1*H_1(x)*H_0(y) + 2*H_0(x)*H_1(y) + 2*H_1(x)*H_1(y)` if axis=0 is `x` and axis=1 is `y`.

Parameters:

**c**array\_like

Array of Hermite\_e series coefficients. If c is multidimensional the different axis correspond to different variables with the degree in each axis given by the corresponding index.

**m**int, optional

Order of integration, must be positive. (Default: 1)

**k**{\[\], list, scalar}, optional

Integration constant(s). The value of the first integral at `lbnd` is the first value in the list, the value of the second integral at `lbnd` is the second value, etc. If `k == []` (the default), all constants are set to zero. If `m == 1`, a single scalar can be given instead of a list.

**lbnd**scalar, optional

The lower bound of the integral. (Default: 0)

**scl**scalar, optional

Following each integration the result is _multiplied_ by _scl_ before the integration constant is added. (Default: 1)

**axis**int, optional

Axis over which the integral is taken. (Default: 0).

Returns:

**S**ndarray

Hermite\_e series coefficients of the integral.

Raises:

ValueError

If `m < 0`, `len(k) > m`, `np.ndim(lbnd) != 0`, or `np.ndim(scl) != 0`.

See also

[`hermeder`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeder.html#numpy.polynomial.hermite_e.hermeder "numpy.polynomial.hermite_e.hermeder")

Notes

Note that the result of each integration is _multiplied_ by _scl_. Why is this important to note? Say one is making a linear change of variable in an integral relative to _x_. Then dx = du/a, so one will need to set _scl_ equal to 1/a - perhaps not what one would have first thought.

Also note that, in general, the result of integrating a C-series needs to be “reprojected” onto the C-series basis set. Thus, typically, the result of this function is “unintuitive,” albeit correct; see Examples section below.

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite\_e import hermeint
\>>> hermeint(\[1, 2, 3\]) \# integrate once, value 0 at 0.
array(\[1., 1., 1., 1.\])
\>>> hermeint(\[1, 2, 3\], m\=2) \# integrate twice, value & deriv 0 at 0
array(\[-0.25      ,  1.        ,  0.5       ,  0.33333333,  0.25      \]) # may vary
\>>> hermeint(\[1, 2, 3\], k\=1) \# integrate once, value 1 at 0.
array(\[2., 1., 1., 1.\])
\>>> hermeint(\[1, 2, 3\], lbnd\=-1) \# integrate once, value 0 at -1
array(\[-1.,  1.,  1.,  1.\])
\>>> hermeint(\[1, 2, 3\], m\=2, k\=\[1, 2\], lbnd\=-1)
array(\[ 1.83333333,  0.        ,  0.5       ,  0.33333333,  0.25      \]) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page