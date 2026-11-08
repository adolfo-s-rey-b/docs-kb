[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polyval.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polyval.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polyval.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polyval.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polyval.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polyval.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polyval.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polyval.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polyval.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polyval.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polyval.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polyval.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polyval.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polyval.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polyval.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polyval.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polyval.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polyval.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polyval.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polyval.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polyval[#](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy-polyval "Link to this heading")

===========================================================================================================================

numpy.polyval(_p_, _x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L713-L790)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "Link to this definition")

Evaluate a polynomial at specific values.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

If _p_ is of length N, this function returns the value:

p\[0\]\*x\*\*(N\-1) + p\[1\]\*x\*\*(N\-2) + ... + p\[N\-2\]\*x + p\[N\-1\]

Copy to clipboard

If _x_ is a sequence, then `p(x)` is returned for each element of `x`. If _x_ is another polynomial then the composite polynomial `p(x(t))` is returned.

Parameters:

**p**array\_like or poly1d object

1D array of polynomial coefficients (including coefficients equal to zero) from highest degree to the constant term, or an instance of poly1d.

**x**array\_like or poly1d object

A number, an array of numbers, or an instance of poly1d, at which to evaluate _p_.

Returns:

**values**ndarray or poly1d

If _x_ is a poly1d instance, the result is the composition of the two polynomials, i.e., _x_ is “substituted” in _p_ and the simplified result is returned. In addition, the type of _x_ - array\_like or poly1d - governs the type of the output: _x_ array\_like => _values_ array\_like, _x_ a poly1d object => _values_ is also.

See also

[`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")

A polynomial class.

Notes

Horner’s scheme [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#r138ee7027ddf-1)
 is used to evaluate the polynomial. Even so, for polynomials of high degree the values may be inaccurate due to rounding errors. Use carefully.

If _x_ is a subtype of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 the return value will be of the same type.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#id1)\
\]

I. N. Bronshtein, K. A. Semendyayev, and K. A. Hirsch (Eng. trans. Ed.), _Handbook of Mathematics_, New York, Van Nostrand Reinhold Co., 1985, pg. 720.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.polyval(\[3,0,1\], 5)  \# 3 \* 5\*\*2 + 0 \* 5\*\*1 + 1
76
\>>> np.polyval(\[3,0,1\], np.poly1d(5))
poly1d(\[76\])
\>>> np.polyval(np.poly1d(\[3,0,1\]), 5)
76
\>>> np.polyval(np.poly1d(\[3,0,1\]), np.poly1d(5))
poly1d(\[76\])

Copy to clipboard

Go BackOpen In Tab

On this page