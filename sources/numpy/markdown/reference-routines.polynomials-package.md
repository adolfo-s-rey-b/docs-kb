[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials-package.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials-package.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials-package.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials-package.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials-package.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials-package.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials-package.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials-package.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials-package.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials-package.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials-package.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials-package.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials-package.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials-package.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials-package.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials-package.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials-package.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials-package.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials-package.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials-package.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials-package.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

[`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "Link to this heading")

=======================================================================================================================================================================================================================================================================

A sub-package for efficiently dealing with polynomials.

Within the documentation for this sub-package, a “finite power series,” i.e., a polynomial (also referred to simply as a “series”) is represented by a 1-D numpy array of the polynomial’s coefficients, ordered from lowest order term to highest. For example, array(\[1,2,3\]) represents `P_0 + 2*P_1 + 3*P_2`, where P\_n is the n-th order basis polynomial applicable to the specific module in question, e.g., [`polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html#module-numpy.polynomial.polynomial "numpy.polynomial.polynomial")
 (which “wraps” the “standard” basis) or [`chebyshev`](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html#module-numpy.polynomial.chebyshev "numpy.polynomial.chebyshev")
. For optimal performance, all operations on polynomials, including evaluation at an argument, are implemented as operations on the coefficients. Additional (module-specific) information can be found in the docstring for the module of interest.

This package provides _convenience classes_ for each of six different kinds of polynomials:

| **Name** | **Provides** |
| --- | --- |
| [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial") | Power series |
| [`Chebyshev`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy.polynomial.chebyshev.Chebyshev "numpy.polynomial.chebyshev.Chebyshev") | Chebyshev series |
| [`Legendre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.html#numpy.polynomial.legendre.Legendre "numpy.polynomial.legendre.Legendre") | Legendre series |
| [`Laguerre`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.html#numpy.polynomial.laguerre.Laguerre "numpy.polynomial.laguerre.Laguerre") | Laguerre series |
| [`Hermite`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#numpy.polynomial.hermite.Hermite "numpy.polynomial.hermite.Hermite") | Hermite series |
| [`HermiteE`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.html#numpy.polynomial.hermite_e.HermiteE "numpy.polynomial.hermite_e.HermiteE") | HermiteE series |

These _convenience classes_ provide a consistent interface for creating, manipulating, and fitting data with polynomials of different bases. The convenience classes are the preferred interface for the [`polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 package, and are available from the `numpy.polynomial` namespace. This eliminates the need to navigate to the corresponding submodules, e.g. `np.polynomial.Polynomial` or `np.polynomial.Chebyshev` instead of `np.polynomial.polynomial.Polynomial` or `np.polynomial.chebyshev.Chebyshev`, respectively. The classes provide a more consistent and concise interface than the type-specific functions defined in the submodules for each type of polynomial. For example, to fit a Chebyshev polynomial with degree `1` to data given by arrays `xdata` and `ydata`, the [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fit.html#numpy.polynomial.chebyshev.Chebyshev.fit "numpy.polynomial.chebyshev.Chebyshev.fit")
 class method:

\>>> from numpy.polynomial import Chebyshev
\>>> xdata \= \[1, 2, 3, 4\]
\>>> ydata \= \[1, 4, 9, 16\]
\>>> c \= Chebyshev.fit(xdata, ydata, deg\=1)

Copy to clipboard

is preferred over the [`chebyshev.chebfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebfit.html#numpy.polynomial.chebyshev.chebfit "numpy.polynomial.chebyshev.chebfit")
 function from the `np.polynomial.chebyshev` module:

\>>> from numpy.polynomial.chebyshev import chebfit
\>>> c \= chebfit(xdata, ydata, deg\=1)

Copy to clipboard

See [Using the convenience classes](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html)
 for more details.

Convenience Classes[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#convenience-classes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

The following lists the various constants and methods common to all of the classes representing the various kinds of polynomials. In the following, the term `Poly` represents any one of the convenience classes (e.g. [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial")
, [`Chebyshev`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy.polynomial.chebyshev.Chebyshev "numpy.polynomial.chebyshev.Chebyshev")
, [`Hermite`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.html#numpy.polynomial.hermite.Hermite "numpy.polynomial.hermite.Hermite")
, etc.) while the lowercase `p` represents an **instance** of a polynomial class.

### Constants[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#constants "Link to this heading")

*   `Poly.domain` – Default domain
    
*   `Poly.window` – Default window
    
*   `Poly.basis_name` – String used to represent the basis
    
*   `Poly.maxpower` – Maximum value `n` such that `p**n` is allowed
    

### Creation[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#creation "Link to this heading")

Methods for creating polynomial instances.

*   `Poly.basis(degree)` – Basis polynomial of given degree
    
*   `Poly.identity()` – `p` where `p(x) = x` for all `x`
    
*   `Poly.fit(x, y, deg)` – `p` of degree `deg` with coefficients determined by the least-squares fit to the data `x`, `y`
    
*   `Poly.fromroots(roots)` – `p` with specified roots
    
*   `p.copy()` – Create a copy of `p`
    

### Conversion[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#conversion "Link to this heading")

Methods for converting a polynomial instance of one kind to another.

*   `p.cast(Poly)` – Convert `p` to instance of kind `Poly`
    
*   `p.convert(Poly)` – Convert `p` to instance of kind `Poly` or map between `domain` and `window`
    

### Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#calculus "Link to this heading")

*   `p.deriv()` – Take the derivative of `p`
    
*   `p.integ()` – Integrate `p`
    

### Validation[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#validation "Link to this heading")

*   `Poly.has_samecoef(p1, p2)` – Check if coefficients match
    
*   `Poly.has_samedomain(p1, p2)` – Check if domains match
    
*   `Poly.has_sametype(p1, p2)` – Check if types match
    
*   `Poly.has_samewindow(p1, p2)` – Check if windows match
    

### Misc[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#misc "Link to this heading")

*   `p.linspace()` – Return `x, p(x)` at equally-spaced points in `domain`
    
*   `p.mapparms()` – Return the parameters for the linear mapping between `domain` and `window`.
    
*   `p.roots()` – Return the roots of `p`.
    
*   `p.trim()` – Remove trailing coefficients.
    
*   `p.cutdeg(degree)` – Truncate `p` to given degree
    
*   `p.truncate(size)` – Truncate `p` to given size
    

Configuration[#](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#configuration "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`numpy.polynomial.set_default_printstyle`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.set_default_printstyle.html#numpy.polynomial.set_default_printstyle "numpy.polynomial.set_default_printstyle")<br>(style) | Set the default format for the string representation of polynomials. |

On this page