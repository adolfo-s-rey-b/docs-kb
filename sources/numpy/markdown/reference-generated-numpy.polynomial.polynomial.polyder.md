[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyder.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polyder.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyder.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polyder.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polyder.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polyder.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polyder.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polyder.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polyder.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyder[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyder.html#numpy-polynomial-polynomial-polyder "Link to this heading")

=============================================================================================================================================================================================

polynomial.polynomial.polyder(_c_, _m\=1_, _scl\=1_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L466-L543)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyder.html#numpy.polynomial.polynomial.polyder "Link to this definition")

Differentiate a polynomial.

Returns the polynomial coefficients _c_ differentiated _m_ times along _axis_. At each iteration the result is multiplied by _scl_ (the scaling factor is for use in a linear change of variable). The argument _c_ is an array of coefficients from low to high degree along each axis, e.g., \[1,2,3\] represents the polynomial `1 + 2*x + 3*x**2` while \[\[1,2\],\[1,2\]\] represents `1 + 1*x + 2*y + 2*x*y` if axis=0 is `x` and axis=1 is `y`.

Parameters:

**c**array\_like

Array of polynomial coefficients. If c is multidimensional the different axis correspond to different variables with the degree in each axis given by the corresponding index.

**m**int, optional

Number of derivatives taken, must be non-negative. (Default: 1)

**scl**scalar, optional

Each differentiation is multiplied by _scl_. The end result is multiplication by `scl**m`. This is for use in a linear change of variable. (Default: 1)

**axis**int, optional

Axis over which the derivative is taken. (Default: 0).

Returns:

**der**ndarray

Polynomial coefficients of the derivative.

See also

[`polyint`](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html#numpy.polyint "numpy.polyint")

Examples

Try it in your browser!

\>>> from numpy.polynomial import polynomial as P
\>>> c \= (1, 2, 3, 4)
\>>> P.polyder(c)  \# (d/dx)(c)
array(\[  2.,   6.,  12.\])
\>>> P.polyder(c, 3)  \# (d\*\*3/dx\*\*3)(c)
array(\[24.\])
\>>> P.polyder(c, scl\=-1)  \# (d/d(-x))(c)
array(\[ -2.,  -6., -12.\])
\>>> P.polyder(c, 2, \-1)  \# (d\*\*2/d(-x)\*\*2)(c)
array(\[  6.,  24.\])

Copy to clipboard

Go BackOpen In Tab

On this page