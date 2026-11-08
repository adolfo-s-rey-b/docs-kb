[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.chebyshev.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.chebyshev.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.chebyshev.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.chebyshev.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.chebyshev.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.chebyshev.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.chebyshev.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.chebyshev.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.chebyshev.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.chebyshev.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.chebyshev.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.chebyshev.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.chebyshev.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.chebyshev.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.chebyshev.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.chebyshev.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.chebyshev.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.chebyshev.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.chebyshev.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.chebyshev.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Chebyshev Series ([`numpy.polynomial.chebyshev`](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#module-numpy.polynomial.chebyshev "numpy.polynomial.chebyshev")
)[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#chebyshev-series-numpy-polynomial-chebyshev "Link to this heading")

================================================================================================================================================================================================================================================================================================================================================

This module provides a number of objects (mostly functions) useful for dealing with Chebyshev series, including a [`Chebyshev`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy.polynomial.chebyshev.Chebyshev "numpy.polynomial.chebyshev.Chebyshev")
 class that encapsulates the usual arithmetic operations. (General information on how this module represents and works with such polynomials is in the docstring for its “parent” sub-package, [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
).

Classes[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#classes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Chebyshev`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy.polynomial.chebyshev.Chebyshev "numpy.polynomial.chebyshev.Chebyshev")<br>(coef\[, domain, window, symbol\]) | A Chebyshev series class. |

Constants[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#constants "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`chebdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebdomain.html#numpy.polynomial.chebyshev.chebdomain "numpy.polynomial.chebyshev.chebdomain") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`chebzero`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebzero.html#numpy.polynomial.chebyshev.chebzero "numpy.polynomial.chebyshev.chebzero") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`chebone`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebone.html#numpy.polynomial.chebyshev.chebone "numpy.polynomial.chebyshev.chebone") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |
| [`chebx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebx.html#numpy.polynomial.chebyshev.chebx "numpy.polynomial.chebyshev.chebx") | ndarray(shape, dtype=None, buffer=None, offset=0, strides=None, order=None) |

Arithmetic[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#arithmetic "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`chebadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebadd.html#numpy.polynomial.chebyshev.chebadd "numpy.polynomial.chebyshev.chebadd")<br>(c1, c2) | Add one Chebyshev series to another. |
| [`chebsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebsub.html#numpy.polynomial.chebyshev.chebsub "numpy.polynomial.chebyshev.chebsub")<br>(c1, c2) | Subtract one Chebyshev series from another. |
| [`chebmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmulx.html#numpy.polynomial.chebyshev.chebmulx "numpy.polynomial.chebyshev.chebmulx")<br>(c) | Multiply a Chebyshev series by x. |
| [`chebmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmul.html#numpy.polynomial.chebyshev.chebmul "numpy.polynomial.chebyshev.chebmul")<br>(c1, c2) | Multiply one Chebyshev series by another. |
| [`chebdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebdiv.html#numpy.polynomial.chebyshev.chebdiv "numpy.polynomial.chebyshev.chebdiv")<br>(c1, c2) | Divide one Chebyshev series by another. |
| [`chebpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpow.html#numpy.polynomial.chebyshev.chebpow "numpy.polynomial.chebyshev.chebpow")<br>(c, pow\[, maxpower\]) | Raise a Chebyshev series to a power. |
| [`chebval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval.html#numpy.polynomial.chebyshev.chebval "numpy.polynomial.chebyshev.chebval")<br>(x, c\[, tensor\]) | Evaluate a Chebyshev series at points x. |
| [`chebval2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval2d.html#numpy.polynomial.chebyshev.chebval2d "numpy.polynomial.chebyshev.chebval2d")<br>(x, y, c) | Evaluate a 2-D Chebyshev series at points (x, y). |
| [`chebval3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebval3d.html#numpy.polynomial.chebyshev.chebval3d "numpy.polynomial.chebyshev.chebval3d")<br>(x, y, z, c) | Evaluate a 3-D Chebyshev series at points (x, y, z). |
| [`chebvalnd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvalnd.html#numpy.polynomial.chebyshev.chebvalnd "numpy.polynomial.chebyshev.chebvalnd")<br>(pts, c) | Evaluate an N-D Chebyshev series at points. |
| [`chebgrid2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgrid2d.html#numpy.polynomial.chebyshev.chebgrid2d "numpy.polynomial.chebyshev.chebgrid2d")<br>(x, y, c) | Evaluate a 2-D Chebyshev series on the Cartesian product of x and y. |
| [`chebgrid3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgrid3d.html#numpy.polynomial.chebyshev.chebgrid3d "numpy.polynomial.chebyshev.chebgrid3d")<br>(x, y, z, c) | Evaluate a 3-D Chebyshev series on the Cartesian product of x, y, and z. |

Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#calculus "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`chebder`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebder.html#numpy.polynomial.chebyshev.chebder "numpy.polynomial.chebyshev.chebder")<br>(c\[, m, scl, axis\]) | Differentiate a Chebyshev series. |
| [`chebint`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebint.html#numpy.polynomial.chebyshev.chebint "numpy.polynomial.chebyshev.chebint")<br>(c\[, m, k, lbnd, scl, axis\]) | Integrate a Chebyshev series. |

Misc Functions[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#misc-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`chebfromroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebfromroots.html#numpy.polynomial.chebyshev.chebfromroots "numpy.polynomial.chebyshev.chebfromroots")<br>(roots) | Generate a Chebyshev series with given roots. |
| [`chebroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebroots.html#numpy.polynomial.chebyshev.chebroots "numpy.polynomial.chebyshev.chebroots")<br>(c) | Compute the roots of a Chebyshev series. |
| [`chebvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander.html#numpy.polynomial.chebyshev.chebvander "numpy.polynomial.chebyshev.chebvander")<br>(x, deg) | Pseudo-Vandermonde matrix of given degree. |
| [`chebvander2d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander2d.html#numpy.polynomial.chebyshev.chebvander2d "numpy.polynomial.chebyshev.chebvander2d")<br>(x, y, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`chebvander3d`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebvander3d.html#numpy.polynomial.chebyshev.chebvander3d "numpy.polynomial.chebyshev.chebvander3d")<br>(x, y, z, deg) | Pseudo-Vandermonde matrix of given degrees. |
| [`chebgauss`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgauss.html#numpy.polynomial.chebyshev.chebgauss "numpy.polynomial.chebyshev.chebgauss")<br>(deg) | Gauss-Chebyshev quadrature. |
| [`chebweight`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebweight.html#numpy.polynomial.chebyshev.chebweight "numpy.polynomial.chebyshev.chebweight")<br>(x) | The weight function of the Chebyshev polynomials. |
| [`chebcompanion`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebcompanion.html#numpy.polynomial.chebyshev.chebcompanion "numpy.polynomial.chebyshev.chebcompanion")<br>(c) | Return the scaled companion matrix of c. |
| [`chebfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebfit.html#numpy.polynomial.chebyshev.chebfit "numpy.polynomial.chebyshev.chebfit")<br>(x, y, deg\[, rcond, full, w\]) | Least squares fit of Chebyshev series to data. |
| [`chebpts1`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpts1.html#numpy.polynomial.chebyshev.chebpts1 "numpy.polynomial.chebyshev.chebpts1")<br>(npts) | Chebyshev points of the first kind. |
| [`chebpts2`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpts2.html#numpy.polynomial.chebyshev.chebpts2 "numpy.polynomial.chebyshev.chebpts2")<br>(npts) | Chebyshev points of the second kind. |
| [`chebtrim`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebtrim.html#numpy.polynomial.chebyshev.chebtrim "numpy.polynomial.chebyshev.chebtrim")<br>(c\[, tol\]) | Remove "small" "trailing" coefficients from a polynomial. |
| [`chebline`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebline.html#numpy.polynomial.chebyshev.chebline "numpy.polynomial.chebyshev.chebline")<br>(off, scl) | Chebyshev series whose graph is a straight line. |
| [`cheb2poly`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.cheb2poly.html#numpy.polynomial.chebyshev.cheb2poly "numpy.polynomial.chebyshev.cheb2poly")<br>(c) | Convert a Chebyshev series to a polynomial. |
| [`poly2cheb`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.poly2cheb.html#numpy.polynomial.chebyshev.poly2cheb "numpy.polynomial.chebyshev.poly2cheb")<br>(pol) | Convert a polynomial to a Chebyshev series. |
| [`chebinterpolate`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html#numpy.polynomial.chebyshev.chebinterpolate "numpy.polynomial.chebyshev.chebinterpolate")<br>(func, deg\[, args\]) | Interpolate a function at the Chebyshev points of the first kind. |

See also[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#see-also "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

[`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")

Notes[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#notes "Link to this heading")

------------------------------------------------------------------------------------------------------------------

The implementations of multiplication, division, integration, and differentiation use the algebraic identities [\[1\]](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#r3f3efff98d00-1)
:

where

x = \\frac{z + z^{-1}}{2}.

These identities allow a Chebyshev series to be expressed as a finite, symmetric Laurent series. In this module, this sort of Laurent series is referred to as a “z-series.”

References[#](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#references "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

\[[1](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#id1)\
\]

A. T. Benjamin, et al., “Combinatorial Trigonometry with Chebyshev Polynomials,” _Journal of Statistical Planning and Inference 14_, 2008 ([https://web.archive.org/web/20080221202153/https://www.math.hmc.edu/~benjamin/papers/CombTrig.pdf](https://web.archive.org/web/20080221202153/https://www.math.hmc.edu/~benjamin/papers/CombTrig.pdf)
, pg. 4)

On this page