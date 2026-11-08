[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.hermite.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.hermite.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.hermite.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.hermite.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.hermite.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.hermite.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.hermite.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.hermite.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.hermite.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.hermite.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.hermite.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.hermite.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.hermite.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.hermite.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.hermite.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.hermite.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.hermite.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.hermite.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.hermite.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.hermite.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Hermite Series, “Physicists” ([`numpy.polynomial.hermite`](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#module-numpy.polynomial.hermite "numpy.polynomial.hermite")
)[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#hermite-series-physicists-numpy-polynomial-hermite "Link to this heading")

=========================================================================================================================================================================================================================================================================================================================================================

This module provides a number of objects (mostly functions) useful for dealing with Hermite series, including a [`Hermite`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#numpy.polynomial.hermite.Hermite "numpy.polynomial.hermite.Hermite")
 class that encapsulates the usual arithmetic operations. (General information on how this module represents and works with such polynomials is in the docstring for its “parent” sub-package, [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
).

Classes[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#classes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Hermite`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#numpy.polynomial.hermite.Hermite "numpy.polynomial.hermite.Hermite")<br>(coef\[, domain, window, symbol\]) | A Hermite series class. |

Constants[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#constants "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hermdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermdomain.html#numpy.polynomial.hermite.hermdomain "numpy.polynomial.hermite.hermdomain") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`hermzero`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermzero.html#numpy.polynomial.hermite.hermzero "numpy.polynomial.hermite.hermzero") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`hermone`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermone.html#numpy.polynomial.hermite.hermone "numpy.polynomial.hermite.hermone") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`hermx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermx.html#numpy.polynomial.hermite.hermx "numpy.polynomial.hermite.hermx") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |

Arithmetic[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#arithmetic "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hermadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermadd.html#numpy.polynomial.hermite.hermadd "numpy.polynomial.hermite.hermadd")<br>(c1, c2) | Add one Hermite series to another. |
| [`hermsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermsub.html#numpy.polynomial.hermite.hermsub "numpy.polynomial.hermite.hermsub")<br>(c1, c2) | Subtract one Hermite series from another. |
| [`hermmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmulx.html#numpy.polynomial.hermite.hermmulx "numpy.polynomial.hermite.hermmulx")<br>(c) | Multiply a Hermite series by x. |
| [`hermmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmul.html#numpy.polynomial.hermite.hermmul "numpy.polynomial.hermite.hermmul")<br>(c1, c2) | Multiply one Hermite series by another. |
| [`hermdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermdiv.html#numpy.polynomial.hermite.hermdiv "numpy.polynomial.hermite.hermdiv")<br>(c1, c2) | Divide one Hermite series by another. |
| [`hermpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermpow.html#numpy.polynomial.hermite.hermpow "numpy.polynomial.hermite.hermpow")<br>(c, pow\[, maxpower\]) | Raise a Hermite series to a power. |
| [`hermval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval.html#numpy.polynomial.hermite.hermval "numpy.polynomial.hermite.hermval")<br>(x, c\[, tensor\]) | Evaluate a Hermite series at points x. |
| [`hermval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval2d.html#numpy.polynomial.hermite.hermval2d "numpy.polynomial.hermite.hermval2d")<br>(x, y, c) | Evaluate a 2-D Hermite series at points (x, y). |
| [`hermval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermval3d.html#numpy.polynomial.hermite.hermval3d "numpy.polynomial.hermite.hermval3d")<br>(x, y, z, c) | Evaluate a 3-D Hermite series at points (x, y, z). |
| [`hermvalnd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvalnd.html#numpy.polynomial.hermite.hermvalnd "numpy.polynomial.hermite.hermvalnd")<br>(pts, c) | Evaluate an N-D Hermite series at points. |
| [`hermgrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid2d.html#numpy.polynomial.hermite.hermgrid2d "numpy.polynomial.hermite.hermgrid2d")<br>(x, y, c) | Evaluate a 2-D Hermite series on the Cartesian product of x and y. |
| [`hermgrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgrid3d.html#numpy.polynomial.hermite.hermgrid3d "numpy.polynomial.hermite.hermgrid3d")<br>(x, y, z, c) | Evaluate a 3-D Hermite series on the Cartesian product of x, y, and z. |

Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#calculus "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hermder`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermder.html#numpy.polynomial.hermite.hermder "numpy.polynomial.hermite.hermder")<br>(c\[, m, scl, axis\]) | Differentiate a Hermite series. |
| [`hermint`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermint.html#numpy.polynomial.hermite.hermint "numpy.polynomial.hermite.hermint")<br>(c\[, m, k, lbnd, scl, axis\]) | Integrate a Hermite series. |

Misc Functions[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#misc-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hermfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermfromroots.html#numpy.polynomial.hermite.hermfromroots "numpy.polynomial.hermite.hermfromroots")<br>(roots) | Generate a Hermite series with given roots. |
| [`hermroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermroots.html#numpy.polynomial.hermite.hermroots "numpy.polynomial.hermite.hermroots")<br>(c) | Compute the roots of a Hermite series. |
| [`hermvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander.html#numpy.polynomial.hermite.hermvander "numpy.polynomial.hermite.hermvander")<br>(x, deg) | Pseudo-Vandermonde matrix of given degree. |
| [`hermvander2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander2d.html#numpy.polynomial.hermite.hermvander2d "numpy.polynomial.hermite.hermvander2d")<br>(x, y, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`hermvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermvander3d.html#numpy.polynomial.hermite.hermvander3d "numpy.polynomial.hermite.hermvander3d")<br>(x, y, z, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`hermgauss`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermgauss.html#numpy.polynomial.hermite.hermgauss "numpy.polynomial.hermite.hermgauss")<br>(deg) | Gauss-Hermite quadrature. |
| [`hermweight`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermweight.html#numpy.polynomial.hermite.hermweight "numpy.polynomial.hermite.hermweight")<br>(x) | Weight function of the Hermite polynomials. |
| [`hermcompanion`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermcompanion.html#numpy.polynomial.hermite.hermcompanion "numpy.polynomial.hermite.hermcompanion")<br>(c) | Return the scaled companion matrix of c. |
| [`hermfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermfit.html#numpy.polynomial.hermite.hermfit "numpy.polynomial.hermite.hermfit")<br>(x, y, deg\[, rcond, full, w\]) | Least squares fit of Hermite series to data. |
| [`hermtrim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermtrim.html#numpy.polynomial.hermite.hermtrim "numpy.polynomial.hermite.hermtrim")<br>(c\[, tol\]) | Remove "small" "trailing" coefficients from a polynomial. |
| [`hermline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermline.html#numpy.polynomial.hermite.hermline "numpy.polynomial.hermite.hermline")<br>(off, scl) | Hermite series whose graph is a straight line. |
| [`herm2poly`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.herm2poly.html#numpy.polynomial.hermite.herm2poly "numpy.polynomial.hermite.herm2poly")<br>(c) | Convert a Hermite series to a polynomial. |
| [`poly2herm`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.poly2herm.html#numpy.polynomial.hermite.poly2herm "numpy.polynomial.hermite.poly2herm")<br>(pol) | Convert a polynomial to a Hermite series. |

See also[#](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html#see-also "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

[`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")

On this page