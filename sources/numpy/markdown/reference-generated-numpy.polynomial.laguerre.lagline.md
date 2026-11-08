[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagline.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.laguerre.lagline.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagline.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.laguerre.lagline.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.laguerre.lagline.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.laguerre.lagline.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.laguerre.lagline.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.laguerre.lagline.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.laguerre.lagline.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.laguerre.lagline[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagline.html#numpy-polynomial-laguerre-lagline "Link to this heading")

=======================================================================================================================================================================================

polynomial.laguerre.lagline(_off_, _scl_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/laguerre.py#L214-L249)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagline.html#numpy.polynomial.laguerre.lagline "Link to this definition")

Laguerre series whose graph is a straight line.

Parameters:

**off, scl**scalars

The specified line is given by `off + scl*x`.

Returns:

**y**ndarray

This module’s representation of the Laguerre series for `off + scl*x`.

See also

[`numpy.polynomial.polynomial.polyline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyline.html#numpy.polynomial.polynomial.polyline "numpy.polynomial.polynomial.polyline")

[`numpy.polynomial.chebyshev.chebline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebline.html#numpy.polynomial.chebyshev.chebline "numpy.polynomial.chebyshev.chebline")

[`numpy.polynomial.legendre.legline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legline.html#numpy.polynomial.legendre.legline "numpy.polynomial.legendre.legline")

[`numpy.polynomial.hermite.hermline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermline.html#numpy.polynomial.hermite.hermline "numpy.polynomial.hermite.hermline")

[`numpy.polynomial.hermite_e.hermeline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeline.html#numpy.polynomial.hermite_e.hermeline "numpy.polynomial.hermite_e.hermeline")

Examples

Try it in your browser!

\>>> from numpy.polynomial.laguerre import lagline, lagval
\>>> lagval(0,lagline(3, 2))
3.0
\>>> lagval(1,lagline(3, 2))
5.0

Copy to clipboard

Go BackOpen In Tab

On this page