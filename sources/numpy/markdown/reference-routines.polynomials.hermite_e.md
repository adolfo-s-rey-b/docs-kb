[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.hermite_e.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.hermite_e.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.hermite_e.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.hermite_e.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.hermite_e.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.hermite_e.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.hermite_e.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.hermite_e.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.hermite_e.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.hermite_e.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.hermite_e.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.hermite_e.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.hermite_e.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.hermite_e.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.hermite_e.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.hermite_e.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.hermite_e.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.hermite_e.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.hermite_e.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.hermite_e.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

HermiteE Series, “Probabilists” ([`numpy.polynomial.hermite_e`](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#module-numpy.polynomial.hermite_e "numpy.polynomial.hermite_e")
)[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#hermitee-series-probabilists-numpy-polynomial-hermite-e "Link to this heading")

===========================================================================================================================================================================================================================================================================================================================================================================

This module provides a number of objects (mostly functions) useful for dealing with Hermite\_e series, including a [`HermiteE`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html#numpy.polynomial.hermite_e.HermiteE "numpy.polynomial.hermite_e.HermiteE")
 class that encapsulates the usual arithmetic operations. (General information on how this module represents and works with such polynomials is in the docstring for its “parent” sub-package, [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
).

Classes[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#classes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`HermiteE`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html#numpy.polynomial.hermite_e.HermiteE "numpy.polynomial.hermite_e.HermiteE")<br>(coef\[, domain, window, symbol\]) | A HermiteE series class. |

Constants[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#constants "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hermedomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermedomain.html#numpy.polynomial.hermite_e.hermedomain "numpy.polynomial.hermite_e.hermedomain") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`hermezero`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermezero.html#numpy.polynomial.hermite_e.hermezero "numpy.polynomial.hermite_e.hermezero") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`hermeone`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeone.html#numpy.polynomial.hermite_e.hermeone "numpy.polynomial.hermite_e.hermeone") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`hermex`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermex.html#numpy.polynomial.hermite_e.hermex "numpy.polynomial.hermite_e.hermex") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |

Arithmetic[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#arithmetic "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hermeadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeadd.html#numpy.polynomial.hermite_e.hermeadd "numpy.polynomial.hermite_e.hermeadd")<br>(c1, c2) | Add one Hermite series to another. |
| [`hermesub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermesub.html#numpy.polynomial.hermite_e.hermesub "numpy.polynomial.hermite_e.hermesub")<br>(c1, c2) | Subtract one Hermite series from another. |
| [`hermemulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemulx.html#numpy.polynomial.hermite_e.hermemulx "numpy.polynomial.hermite_e.hermemulx")<br>(c) | Multiply a Hermite series by x. |
| [`hermemul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemul.html#numpy.polynomial.hermite_e.hermemul "numpy.polynomial.hermite_e.hermemul")<br>(c1, c2) | Multiply one Hermite series by another. |
| [`hermediv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermediv.html#numpy.polynomial.hermite_e.hermediv "numpy.polynomial.hermite_e.hermediv")<br>(c1, c2) | Divide one Hermite series by another. |
| [`hermepow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermepow.html#numpy.polynomial.hermite_e.hermepow "numpy.polynomial.hermite_e.hermepow")<br>(c, pow\[, maxpower\]) | Raise a Hermite series to a power. |
| [`hermeval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval.html#numpy.polynomial.hermite_e.hermeval "numpy.polynomial.hermite_e.hermeval")<br>(x, c\[, tensor\]) | Evaluate a HermiteE series at points x. |
| [`hermeval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval2d.html#numpy.polynomial.hermite_e.hermeval2d "numpy.polynomial.hermite_e.hermeval2d")<br>(x, y, c) | Evaluate a 2-D HermiteE series at points (x, y). |
| [`hermeval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeval3d.html#numpy.polynomial.hermite_e.hermeval3d "numpy.polynomial.hermite_e.hermeval3d")<br>(x, y, z, c) | Evaluate a 3-D Hermite\_e series at points (x, y, z). |
| [`hermevalnd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevalnd.html#numpy.polynomial.hermite_e.hermevalnd "numpy.polynomial.hermite_e.hermevalnd")<br>(pts, c) | Evaluate an N-D Hermite\_e series at points. |
| [`hermegrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermegrid2d.html#numpy.polynomial.hermite_e.hermegrid2d "numpy.polynomial.hermite_e.hermegrid2d")<br>(x, y, c) | Evaluate a 2-D HermiteE series on the Cartesian product of x and y. |
| [`hermegrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermegrid3d.html#numpy.polynomial.hermite_e.hermegrid3d "numpy.polynomial.hermite_e.hermegrid3d")<br>(x, y, z, c) | Evaluate a 3-D HermiteE series on the Cartesian product of x, y, and z. |

Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#calculus "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hermeder`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeder.html#numpy.polynomial.hermite_e.hermeder "numpy.polynomial.hermite_e.hermeder")<br>(c\[, m, scl, axis\]) | Differentiate a Hermite\_e series. |
| [`hermeint`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeint.html#numpy.polynomial.hermite_e.hermeint "numpy.polynomial.hermite_e.hermeint")<br>(c\[, m, k, lbnd, scl, axis\]) | Integrate a Hermite\_e series. |

Misc Functions[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#misc-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hermefromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermefromroots.html#numpy.polynomial.hermite_e.hermefromroots "numpy.polynomial.hermite_e.hermefromroots")<br>(roots) | Generate a HermiteE series with given roots. |
| [`hermeroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeroots.html#numpy.polynomial.hermite_e.hermeroots "numpy.polynomial.hermite_e.hermeroots")<br>(c) | Compute the roots of a HermiteE series. |
| [`hermevander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander.html#numpy.polynomial.hermite_e.hermevander "numpy.polynomial.hermite_e.hermevander")<br>(x, deg) | Pseudo-Vandermonde matrix of given degree. |
| [`hermevander2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander2d.html#numpy.polynomial.hermite_e.hermevander2d "numpy.polynomial.hermite_e.hermevander2d")<br>(x, y, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`hermevander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermevander3d.html#numpy.polynomial.hermite_e.hermevander3d "numpy.polynomial.hermite_e.hermevander3d")<br>(x, y, z, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`hermegauss`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermegauss.html#numpy.polynomial.hermite_e.hermegauss "numpy.polynomial.hermite_e.hermegauss")<br>(deg) | Gauss-HermiteE quadrature. |
| [`hermeweight`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeweight.html#numpy.polynomial.hermite_e.hermeweight "numpy.polynomial.hermite_e.hermeweight")<br>(x) | Weight function of the Hermite\_e polynomials. |
| [`hermecompanion`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermecompanion.html#numpy.polynomial.hermite_e.hermecompanion "numpy.polynomial.hermite_e.hermecompanion")<br>(c) | Return the scaled companion matrix of c. |
| [`hermefit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermefit.html#numpy.polynomial.hermite_e.hermefit "numpy.polynomial.hermite_e.hermefit")<br>(x, y, deg\[, rcond, full, w\]) | Least squares fit of Hermite series to data. |
| [`hermetrim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermetrim.html#numpy.polynomial.hermite_e.hermetrim "numpy.polynomial.hermite_e.hermetrim")<br>(c\[, tol\]) | Remove "small" "trailing" coefficients from a polynomial. |
| [`hermeline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeline.html#numpy.polynomial.hermite_e.hermeline "numpy.polynomial.hermite_e.hermeline")<br>(off, scl) | Hermite series whose graph is a straight line. |
| [`herme2poly`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.herme2poly.html#numpy.polynomial.hermite_e.herme2poly "numpy.polynomial.hermite_e.herme2poly")<br>(c) | Convert a Hermite series to a polynomial. |
| [`poly2herme`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.poly2herme.html#numpy.polynomial.hermite_e.poly2herme "numpy.polynomial.hermite_e.poly2herme")<br>(pol) | Convert a polynomial to a Hermite series. |

See also[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html#see-also "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

[`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")

On this page