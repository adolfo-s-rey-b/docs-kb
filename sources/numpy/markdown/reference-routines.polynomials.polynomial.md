[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.polynomial.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.polynomial.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.polynomial.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.polynomial.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.polynomial.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.polynomial.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.polynomial.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.polynomial.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.polynomial.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.polynomial.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.polynomial.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.polynomial.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.polynomial.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.polynomial.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.polynomial.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.polynomial.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.polynomial.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.polynomial.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.polynomial.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.polynomial.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Power Series ([`numpy.polynomial.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#module-numpy.polynomial.polynomial "numpy.polynomial.polynomial")
)[#](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#power-series-numpy-polynomial-polynomial "Link to this heading")

==============================================================================================================================================================================================================================================================================================================================================

This module provides a number of objects (mostly functions) useful for dealing with polynomials, including a [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial")
 class that encapsulates the usual arithmetic operations. (General information on how this module represents and works with polynomial objects is in the docstring for its “parent” sub-package, [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
).

Classes[#](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#classes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial")<br>(coef\[, domain, window, symbol\]) | A power series class. |

Constants[#](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#constants "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`polydomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polydomain.html#numpy.polynomial.polynomial.polydomain "numpy.polynomial.polynomial.polydomain") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`polyzero`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyzero.html#numpy.polynomial.polynomial.polyzero "numpy.polynomial.polynomial.polyzero") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`polyone`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyone.html#numpy.polynomial.polynomial.polyone "numpy.polynomial.polynomial.polyone") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`polyx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyx.html#numpy.polynomial.polynomial.polyx "numpy.polynomial.polynomial.polyx") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |

Arithmetic[#](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#arithmetic "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`polyadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyadd.html#numpy.polynomial.polynomial.polyadd "numpy.polynomial.polynomial.polyadd")<br>(c1, c2) | Add one polynomial to another. |
| [`polysub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polysub.html#numpy.polynomial.polynomial.polysub "numpy.polynomial.polynomial.polysub")<br>(c1, c2) | Subtract one polynomial from another. |
| [`polymulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymulx.html#numpy.polynomial.polynomial.polymulx "numpy.polynomial.polynomial.polymulx")<br>(c) | Multiply a polynomial by x. |
| [`polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymul.html#numpy.polynomial.polynomial.polymul "numpy.polynomial.polynomial.polymul")<br>(c1, c2) | Multiply one polynomial by another. |
| [`polydiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polydiv.html#numpy.polynomial.polynomial.polydiv "numpy.polynomial.polynomial.polydiv")<br>(c1, c2) | Divide one polynomial by another. |
| [`polypow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polypow.html#numpy.polynomial.polynomial.polypow "numpy.polynomial.polynomial.polypow")<br>(c, pow\[, maxpower\]) | Raise a polynomial to a power. |
| [`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval.html#numpy.polynomial.polynomial.polyval "numpy.polynomial.polynomial.polyval")<br>(x, c\[, tensor\]) | Evaluate a polynomial at points x. |
| [`polyval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html#numpy.polynomial.polynomial.polyval2d "numpy.polynomial.polynomial.polyval2d")<br>(x, y, c) | Evaluate a 2-D polynomial at points (x, y). |
| [`polyval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval3d.html#numpy.polynomial.polynomial.polyval3d "numpy.polynomial.polynomial.polyval3d")<br>(x, y, z, c) | Evaluate a 3-D polynomial at points (x, y, z). |
| [`polyvalnd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvalnd.html#numpy.polynomial.polynomial.polyvalnd "numpy.polynomial.polynomial.polyvalnd")<br>(pts, c) | Evaluate an N-D polynomial at points. |
| [`polygrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polygrid2d.html#numpy.polynomial.polynomial.polygrid2d "numpy.polynomial.polynomial.polygrid2d")<br>(x, y, c) | Evaluate a 2-D polynomial on the Cartesian product of x and y. |
| [`polygrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polygrid3d.html#numpy.polynomial.polynomial.polygrid3d "numpy.polynomial.polynomial.polygrid3d")<br>(x, y, z, c) | Evaluate a 3-D polynomial on the Cartesian product of x, y and z. |

Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#calculus "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`polyder`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyder.html#numpy.polynomial.polynomial.polyder "numpy.polynomial.polynomial.polyder")<br>(c\[, m, scl, axis\]) | Differentiate a polynomial. |
| [`polyint`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyint.html#numpy.polynomial.polynomial.polyint "numpy.polynomial.polynomial.polyint")<br>(c\[, m, k, lbnd, scl, axis\]) | Integrate a polynomial. |

Misc Functions[#](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#misc-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`polyfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfromroots.html#numpy.polynomial.polynomial.polyfromroots "numpy.polynomial.polynomial.polyfromroots")<br>(roots) | Generate a monic polynomial with given roots. |
| [`polyroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyroots.html#numpy.polynomial.polynomial.polyroots "numpy.polynomial.polynomial.polyroots")<br>(c) | Compute the roots of a polynomial. |
| [`polyvalfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvalfromroots.html#numpy.polynomial.polynomial.polyvalfromroots "numpy.polynomial.polynomial.polyvalfromroots")<br>(x, r\[, tensor\]) | Evaluate a polynomial specified by its roots at points x. |
| [`polyvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html#numpy.polynomial.polynomial.polyvander "numpy.polynomial.polynomial.polyvander")<br>(x, deg) | Vandermonde matrix of given degree. |
| [`polyvander2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander2d.html#numpy.polynomial.polynomial.polyvander2d "numpy.polynomial.polynomial.polyvander2d")<br>(x, y, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`polyvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander3d.html#numpy.polynomial.polynomial.polyvander3d "numpy.polynomial.polynomial.polyvander3d")<br>(x, y, z, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`polycompanion`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polycompanion.html#numpy.polynomial.polynomial.polycompanion "numpy.polynomial.polynomial.polycompanion")<br>(c) | Return the companion matrix of c. |
| [`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfit.html#numpy.polynomial.polynomial.polyfit "numpy.polynomial.polynomial.polyfit")<br>(x, y, deg\[, rcond, full, w\]) | Least-squares fit of a polynomial to data. |
| [`polytrim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polytrim.html#numpy.polynomial.polynomial.polytrim "numpy.polynomial.polynomial.polytrim")<br>(c\[, tol\]) | Remove "small" "trailing" coefficients from a polynomial. |
| [`polyline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyline.html#numpy.polynomial.polynomial.polyline "numpy.polynomial.polynomial.polyline")<br>(off, scl) | Returns an array representing a linear polynomial. |

See Also[#](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#see-also "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

[`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")

On this page