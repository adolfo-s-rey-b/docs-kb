[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.laguerre.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.laguerre.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.laguerre.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.laguerre.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.laguerre.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.laguerre.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.laguerre.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.laguerre.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.laguerre.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.laguerre.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.laguerre.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.laguerre.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.laguerre.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.laguerre.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.laguerre.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.laguerre.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.laguerre.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.laguerre.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.laguerre.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.laguerre.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Laguerre Series ([`numpy.polynomial.laguerre`](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#module-numpy.polynomial.laguerre "numpy.polynomial.laguerre")
)[#](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#laguerre-series-numpy-polynomial-laguerre "Link to this heading")

========================================================================================================================================================================================================================================================================================================================================

This module provides a number of objects (mostly functions) useful for dealing with Laguerre series, including a [`Laguerre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html#numpy.polynomial.laguerre.Laguerre "numpy.polynomial.laguerre.Laguerre")
 class that encapsulates the usual arithmetic operations. (General information on how this module represents and works with such polynomials is in the docstring for its “parent” sub-package, [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
).

Classes[#](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#classes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Laguerre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html#numpy.polynomial.laguerre.Laguerre "numpy.polynomial.laguerre.Laguerre")<br>(coef\[, domain, window, symbol\]) | A Laguerre series class. |

Constants[#](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#constants "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`lagdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagdomain.html#numpy.polynomial.laguerre.lagdomain "numpy.polynomial.laguerre.lagdomain") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`lagzero`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagzero.html#numpy.polynomial.laguerre.lagzero "numpy.polynomial.laguerre.lagzero") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`lagone`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagone.html#numpy.polynomial.laguerre.lagone "numpy.polynomial.laguerre.lagone") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`lagx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagx.html#numpy.polynomial.laguerre.lagx "numpy.polynomial.laguerre.lagx") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |

Arithmetic[#](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#arithmetic "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`lagadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagadd.html#numpy.polynomial.laguerre.lagadd "numpy.polynomial.laguerre.lagadd")<br>(c1, c2) | Add one Laguerre series to another. |
| [`lagsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagsub.html#numpy.polynomial.laguerre.lagsub "numpy.polynomial.laguerre.lagsub")<br>(c1, c2) | Subtract one Laguerre series from another. |
| [`lagmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagmulx.html#numpy.polynomial.laguerre.lagmulx "numpy.polynomial.laguerre.lagmulx")<br>(c) | Multiply a Laguerre series by x. |
| [`lagmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagmul.html#numpy.polynomial.laguerre.lagmul "numpy.polynomial.laguerre.lagmul")<br>(c1, c2) | Multiply one Laguerre series by another. |
| [`lagdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagdiv.html#numpy.polynomial.laguerre.lagdiv "numpy.polynomial.laguerre.lagdiv")<br>(c1, c2) | Divide one Laguerre series by another. |
| [`lagpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagpow.html#numpy.polynomial.laguerre.lagpow "numpy.polynomial.laguerre.lagpow")<br>(c, pow\[, maxpower\]) | Raise a Laguerre series to a power. |
| [`lagval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagval.html#numpy.polynomial.laguerre.lagval "numpy.polynomial.laguerre.lagval")<br>(x, c\[, tensor\]) | Evaluate a Laguerre series at points x. |
| [`lagval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagval2d.html#numpy.polynomial.laguerre.lagval2d "numpy.polynomial.laguerre.lagval2d")<br>(x, y, c) | Evaluate a 2-D Laguerre series at points (x, y). |
| [`lagval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagval3d.html#numpy.polynomial.laguerre.lagval3d "numpy.polynomial.laguerre.lagval3d")<br>(x, y, z, c) | Evaluate a 3-D Laguerre series at points (x, y, z). |
| [`lagvalnd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagvalnd.html#numpy.polynomial.laguerre.lagvalnd "numpy.polynomial.laguerre.lagvalnd")<br>(pts, c) | Evaluate an N-D Laguerre series at points. |
| [`laggrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.laggrid2d.html#numpy.polynomial.laguerre.laggrid2d "numpy.polynomial.laguerre.laggrid2d")<br>(x, y, c) | Evaluate a 2-D Laguerre series on the Cartesian product of x and y. |
| [`laggrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.laggrid3d.html#numpy.polynomial.laguerre.laggrid3d "numpy.polynomial.laguerre.laggrid3d")<br>(x, y, z, c) | Evaluate a 3-D Laguerre series on the Cartesian product of x, y, and z. |

Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#calculus "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`lagder`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagder.html#numpy.polynomial.laguerre.lagder "numpy.polynomial.laguerre.lagder")<br>(c\[, m, scl, axis\]) | Differentiate a Laguerre series. |
| [`lagint`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagint.html#numpy.polynomial.laguerre.lagint "numpy.polynomial.laguerre.lagint")<br>(c\[, m, k, lbnd, scl, axis\]) | Integrate a Laguerre series. |

Misc Functions[#](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#misc-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`lagfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagfromroots.html#numpy.polynomial.laguerre.lagfromroots "numpy.polynomial.laguerre.lagfromroots")<br>(roots) | Generate a Laguerre series with given roots. |
| [`lagroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagroots.html#numpy.polynomial.laguerre.lagroots "numpy.polynomial.laguerre.lagroots")<br>(c) | Compute the roots of a Laguerre series. |
| [`lagvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagvander.html#numpy.polynomial.laguerre.lagvander "numpy.polynomial.laguerre.lagvander")<br>(x, deg) | Pseudo-Vandermonde matrix of given degree. |
| [`lagvander2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagvander2d.html#numpy.polynomial.laguerre.lagvander2d "numpy.polynomial.laguerre.lagvander2d")<br>(x, y, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`lagvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagvander3d.html#numpy.polynomial.laguerre.lagvander3d "numpy.polynomial.laguerre.lagvander3d")<br>(x, y, z, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`laggauss`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.laggauss.html#numpy.polynomial.laguerre.laggauss "numpy.polynomial.laguerre.laggauss")<br>(deg) | Gauss-Laguerre quadrature. |
| [`lagweight`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagweight.html#numpy.polynomial.laguerre.lagweight "numpy.polynomial.laguerre.lagweight")<br>(x) | Weight function of the Laguerre polynomials. |
| [`lagcompanion`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagcompanion.html#numpy.polynomial.laguerre.lagcompanion "numpy.polynomial.laguerre.lagcompanion")<br>(c) | Return the companion matrix of c. |
| [`lagfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagfit.html#numpy.polynomial.laguerre.lagfit "numpy.polynomial.laguerre.lagfit")<br>(x, y, deg\[, rcond, full, w\]) | Least squares fit of Laguerre series to data. |
| [`lagtrim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagtrim.html#numpy.polynomial.laguerre.lagtrim "numpy.polynomial.laguerre.lagtrim")<br>(c\[, tol\]) | Remove "small" "trailing" coefficients from a polynomial. |
| [`lagline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagline.html#numpy.polynomial.laguerre.lagline "numpy.polynomial.laguerre.lagline")<br>(off, scl) | Laguerre series whose graph is a straight line. |
| [`lag2poly`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lag2poly.html#numpy.polynomial.laguerre.lag2poly "numpy.polynomial.laguerre.lag2poly")<br>(c) | Convert a Laguerre series to a polynomial. |
| [`poly2lag`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.poly2lag.html#numpy.polynomial.laguerre.poly2lag "numpy.polynomial.laguerre.poly2lag")<br>(pol) | Convert a polynomial to a Laguerre series. |

See also[#](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html#see-also "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

[`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")

On this page