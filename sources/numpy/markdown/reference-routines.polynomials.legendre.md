[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.legendre.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.legendre.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.legendre.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.legendre.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.legendre.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.legendre.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.legendre.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.legendre.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.legendre.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.legendre.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.legendre.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.legendre.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.legendre.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.legendre.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.legendre.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.legendre.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.legendre.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.legendre.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.legendre.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.legendre.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Legendre Series ([`numpy.polynomial.legendre`](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#module-numpy.polynomial.legendre "numpy.polynomial.legendre")
)[#](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#legendre-series-numpy-polynomial-legendre "Link to this heading")

========================================================================================================================================================================================================================================================================================================================================

This module provides a number of objects (mostly functions) useful for dealing with Legendre series, including a [`Legendre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html#numpy.polynomial.legendre.Legendre "numpy.polynomial.legendre.Legendre")
 class that encapsulates the usual arithmetic operations. (General information on how this module represents and works with such polynomials is in the docstring for its “parent” sub-package, [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
).

Classes[#](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#classes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Legendre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html#numpy.polynomial.legendre.Legendre "numpy.polynomial.legendre.Legendre")<br>(coef\[, domain, window, symbol\]) | A Legendre series class. |

Constants[#](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#constants "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`legdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legdomain.html#numpy.polynomial.legendre.legdomain "numpy.polynomial.legendre.legdomain") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`legzero`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legzero.html#numpy.polynomial.legendre.legzero "numpy.polynomial.legendre.legzero") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`legone`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legone.html#numpy.polynomial.legendre.legone "numpy.polynomial.legendre.legone") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`legx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legx.html#numpy.polynomial.legendre.legx "numpy.polynomial.legendre.legx") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |

Arithmetic[#](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#arithmetic "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`legadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legadd.html#numpy.polynomial.legendre.legadd "numpy.polynomial.legendre.legadd")<br>(c1, c2) | Add one Legendre series to another. |
| [`legsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legsub.html#numpy.polynomial.legendre.legsub "numpy.polynomial.legendre.legsub")<br>(c1, c2) | Subtract one Legendre series from another. |
| [`legmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmulx.html#numpy.polynomial.legendre.legmulx "numpy.polynomial.legendre.legmulx")<br>(c) | Multiply a Legendre series by x. |
| [`legmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmul.html#numpy.polynomial.legendre.legmul "numpy.polynomial.legendre.legmul")<br>(c1, c2) | Multiply one Legendre series by another. |
| [`legdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legdiv.html#numpy.polynomial.legendre.legdiv "numpy.polynomial.legendre.legdiv")<br>(c1, c2) | Divide one Legendre series by another. |
| [`legpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legpow.html#numpy.polynomial.legendre.legpow "numpy.polynomial.legendre.legpow")<br>(c, pow\[, maxpower\]) | Raise a Legendre series to a power. |
| [`legval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval.html#numpy.polynomial.legendre.legval "numpy.polynomial.legendre.legval")<br>(x, c\[, tensor\]) | Evaluate a Legendre series at points x. |
| [`legval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval2d.html#numpy.polynomial.legendre.legval2d "numpy.polynomial.legendre.legval2d")<br>(x, y, c) | Evaluate a 2-D Legendre series at points (x, y). |
| [`legval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval3d.html#numpy.polynomial.legendre.legval3d "numpy.polynomial.legendre.legval3d")<br>(x, y, z, c) | Evaluate a 3-D Legendre series at points (x, y, z). |
| [`legvalnd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legvalnd.html#numpy.polynomial.legendre.legvalnd "numpy.polynomial.legendre.legvalnd")<br>(pts, c) | Evaluate an N-D Legendre series at points. |
| [`leggrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid2d.html#numpy.polynomial.legendre.leggrid2d "numpy.polynomial.legendre.leggrid2d")<br>(x, y, c) | Evaluate a 2-D Legendre series on the Cartesian product of x and y. |
| [`leggrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggrid3d.html#numpy.polynomial.legendre.leggrid3d "numpy.polynomial.legendre.leggrid3d")<br>(x, y, z, c) | Evaluate a 3-D Legendre series on the Cartesian product of x, y, and z. |

Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#calculus "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`legder`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legder.html#numpy.polynomial.legendre.legder "numpy.polynomial.legendre.legder")<br>(c\[, m, scl, axis\]) | Differentiate a Legendre series. |
| [`legint`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legint.html#numpy.polynomial.legendre.legint "numpy.polynomial.legendre.legint")<br>(c\[, m, k, lbnd, scl, axis\]) | Integrate a Legendre series. |

Misc Functions[#](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#misc-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`legfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfromroots.html#numpy.polynomial.legendre.legfromroots "numpy.polynomial.legendre.legfromroots")<br>(roots) | Generate a Legendre series with given roots. |
| [`legroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legroots.html#numpy.polynomial.legendre.legroots "numpy.polynomial.legendre.legroots")<br>(c) | Compute the roots of a Legendre series. |
| [`legvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legvander.html#numpy.polynomial.legendre.legvander "numpy.polynomial.legendre.legvander")<br>(x, deg) | Pseudo-Vandermonde matrix of given degree. |
| [`legvander2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legvander2d.html#numpy.polynomial.legendre.legvander2d "numpy.polynomial.legendre.legvander2d")<br>(x, y, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`legvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legvander3d.html#numpy.polynomial.legendre.legvander3d "numpy.polynomial.legendre.legvander3d")<br>(x, y, z, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`leggauss`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggauss.html#numpy.polynomial.legendre.leggauss "numpy.polynomial.legendre.leggauss")<br>(deg) | Gauss-Legendre quadrature. |
| [`legweight`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legweight.html#numpy.polynomial.legendre.legweight "numpy.polynomial.legendre.legweight")<br>(x) | Weight function of the Legendre polynomials. |
| [`legcompanion`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legcompanion.html#numpy.polynomial.legendre.legcompanion "numpy.polynomial.legendre.legcompanion")<br>(c) | Return the scaled companion matrix of c. |
| [`legfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfit.html#numpy.polynomial.legendre.legfit "numpy.polynomial.legendre.legfit")<br>(x, y, deg\[, rcond, full, w\]) | Least squares fit of Legendre series to data. |
| [`legtrim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legtrim.html#numpy.polynomial.legendre.legtrim "numpy.polynomial.legendre.legtrim")<br>(c\[, tol\]) | Remove "small" "trailing" coefficients from a polynomial. |
| [`legline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legline.html#numpy.polynomial.legendre.legline "numpy.polynomial.legendre.legline")<br>(off, scl) | Legendre series whose graph is a straight line. |
| [`leg2poly`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leg2poly.html#numpy.polynomial.legendre.leg2poly "numpy.polynomial.legendre.leg2poly")<br>(c) | Convert a Legendre series to a polynomial. |
| [`poly2leg`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.poly2leg.html#numpy.polynomial.legendre.poly2leg "numpy.polynomial.legendre.poly2leg")<br>(pol) | Convert a polynomial to a Legendre series. |

See also[#](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html#see-also "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

numpy.polynomial

On this page