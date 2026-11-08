[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebder.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebder.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebder.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebder[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebder.html#numpy-polynomial-chebyshev-chebder "Link to this heading")

==========================================================================================================================================================================================

polynomial.chebyshev.chebder(_c_, _m\=1_, _scl\=1_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L873-L960)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebder.html#numpy.polynomial.chebyshev.chebder "Link to this definition")

Differentiate a Chebyshev series.

Returns the Chebyshev series coefficients _c_ differentiated _m_ times along _axis_. At each iteration the result is multiplied by _scl_ (the scaling factor is for use in a linear change of variable). The argument _c_ is an array of coefficients from low to high degree along each axis, e.g., \[1,2,3\] represents the series `1*T_0 + 2*T_1 + 3*T_2` while \[\[1,2\],\[1,2\]\] represents `1*T_0(x)*T_0(y) + 1*T_1(x)*T_0(y) + 2*T_0(x)*T_1(y) + 2*T_1(x)*T_1(y)` if axis=0 is `x` and axis=1 is `y`.

Parameters:

**c**array\_like

Array of Chebyshev series coefficients. If c is multidimensional the different axis correspond to different variables with the degree in each axis given by the corresponding index.

**m**int, optional

Number of derivatives taken, must be non-negative. (Default: 1)

**scl**scalar, optional

Each differentiation is multiplied by _scl_. The end result is multiplication by `scl**m`. This is for use in a linear change of variable. (Default: 1)

**axis**int, optional

Axis over which the derivative is taken. (Default: 0).

Returns:

**der**ndarray

Chebyshev series of the derivative.

See also

[`chebint`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebint.html#numpy.polynomial.chebyshev.chebint "numpy.polynomial.chebyshev.chebint")

Notes

In general, the result of differentiating a C-series needs to be “reprojected” onto the C-series basis set. Thus, typically, the result of this function is “unintuitive,” albeit correct; see Examples section below.

Examples

Try it in your browser!

\>>> from numpy.polynomial import chebyshev as C
\>>> c \= (1,2,3,4)
\>>> C.chebder(c)
array(\[14., 12., 24.\])
\>>> C.chebder(c,3)
array(\[96.\])
\>>> C.chebder(c,scl\=-1)
array(\[-14., -12., -24.\])
\>>> C.chebder(c,2,\-1)
array(\[12.,  96.\])

Copy to clipboard

Go BackOpen In Tab

On this page