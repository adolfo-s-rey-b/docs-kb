[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Polynomials[#](https://numpy.org/doc/stable/reference/routines.polynomials.html#polynomials "Link to this heading")

====================================================================================================================

Polynomials in NumPy can be _created_, _manipulated_, and even _fitted_ using the [convenience classes](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html)
 of the [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 package, introduced in NumPy 1.4.

Prior to NumPy 1.4, [`numpy.poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
 was the class of choice and it is still available in order to maintain backward compatibility. However, the newer [`polynomial package`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is more complete and its _convenience classes_ provide a more consistent, better-behaved interface for working with polynomial expressions. Therefore [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is recommended for new coding.

Note

**Terminology**

The term _polynomial module_ refers to the old API defined in `numpy.lib.polynomial`, which includes the [`numpy.poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
 class and the polynomial functions prefixed with _poly_ accessible from the [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "numpy")
 namespace (e.g. [`numpy.polyadd`](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy.polyadd "numpy.polyadd")
, [`numpy.polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")
, [`numpy.polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
, etc.).

The term _polynomial package_ refers to the new API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
, which includes the convenience classes for the different kinds of polynomials ([`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial")
, [`Chebyshev`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.html#numpy.polynomial.chebyshev.Chebyshev "numpy.polynomial.chebyshev.Chebyshev")
, etc.).

Transitioning from [`numpy.poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
 to [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
[#](https://numpy.org/doc/stable/reference/routines.polynomials.html#transitioning-from-numpy-poly1d-to-numpy-polynomial "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As noted above, the [`poly1d class`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
 and associated functions defined in `numpy.lib.polynomial`, such as [`numpy.polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
 and [`numpy.poly`](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#numpy.poly "numpy.poly")
, are considered legacy and should **not** be used in new code. Since NumPy version 1.4, the [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 package is preferred for working with polynomials.

### Quick Reference[#](https://numpy.org/doc/stable/reference/routines.polynomials.html#quick-reference "Link to this heading")

The following table highlights some of the main differences between the legacy polynomial module and the polynomial package for common tasks. The [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial")
 class is imported for brevity:

from numpy.polynomial import Polynomial

Copy to clipboard

|     |     |     |
| --- | --- | --- |
| **How to…** | Legacy ([`numpy.poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")<br>) | [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial") |
| Create a polynomial object from coefficients [\[1\]](https://numpy.org/doc/stable/reference/routines.polynomials.html#id3) | `p = np.poly1d([1, 2, 3])` | `p = Polynomial([3, 2, 1])` |
| Create a polynomial object from roots | `r = np.poly([-1, 1])` `p = np.poly1d(r)` | `p = Polynomial.fromroots([-1, 1])` |
| Fit a polynomial of degree `deg` to data | `np.polyfit(x, y, deg)` | `Polynomial.fit(x, y, deg)` |
| Evaluate a polynomial at a point [\[2\]](https://numpy.org/doc/stable/reference/routines.polynomials.html#id4) | `p(2.0)` or `np.polyval([1, 2, 3], 2.0)` | `p(2.0)` or `polyval(2.0, p.coef)` (use `p.convert().coef` after fit) |

### Transition Guide[#](https://numpy.org/doc/stable/reference/routines.polynomials.html#transition-guide "Link to this heading")

There are significant differences between `numpy.lib.polynomial` and [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
. The most significant difference is the ordering of the coefficients for the polynomial expressions. The various routines in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 all deal with series whose coefficients go from degree zero upward, which is the _reverse order_ of the poly1d convention. The easy way to remember this is that indices correspond to degree, i.e., `coef[i]` is the coefficient of the term of degree _i_.

Though the difference in convention may be confusing, it is straightforward to convert from the legacy polynomial API to the new. For example, the following demonstrates how you would convert a [`numpy.poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
 instance representing the expression \\(x^{2} + 2x + 3\\) to a [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial "numpy.polynomial.polynomial.Polynomial")
 instance representing the same expression:

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> p1d \= np.poly1d(\[1, 2, 3\])
\>>> p \= np.polynomial.Polynomial(p1d.coef\[::\-1\])

Copy to clipboard

In addition to the `coef` attribute, polynomials from the polynomial package also have `domain` and `window` attributes. These attributes are most relevant when fitting polynomials to data, though it should be noted that polynomials with different `domain` and `window` attributes are not considered equal, and can’t be mixed in arithmetic:

\>>> p1 \= np.polynomial.Polynomial(\[1, 2, 3\])
\>>> p1
Polynomial(\[1., 2., 3.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p2 \= np.polynomial.Polynomial(\[1, 2, 3\], domain\=\[\-2, 2\])
\>>> p1 \== p2
False
\>>> p1 + p2
Traceback (most recent call last):
    ...
TypeError: Domains differ

Copy to clipboard

Go BackOpen In Tab

See the documentation for the [convenience classes](https://numpy.org/doc/stable/reference/routines.polynomials.classes)
 for further details on the `domain` and `window` attributes.

Another major difference between the legacy polynomial module and the polynomial package is polynomial fitting. In the old module, fitting was done via the [`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
 function. In the polynomial package, the [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#numpy.polynomial.polynomial.Polynomial.fit "numpy.polynomial.polynomial.Polynomial.fit")
 class method is preferred. For example, consider a simple linear fit to the following data:

In \[1\]: rng \= np.random.default\_rng()

In \[2\]: x \= np.arange(10)

In \[3\]: y \= np.arange(10) + rng.standard\_normal(10)

Copy to clipboard

With the legacy polynomial module, a linear fit (i.e. polynomial of degree 1) could be applied to these data with [`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
:

In \[4\]: np.polyfit(x, y, deg\=1)
Out\[4\]: array(\[ 1.02069771, -0.33004794\])

Copy to clipboard

With the new polynomial API, the [`fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#numpy.polynomial.polynomial.Polynomial.fit "numpy.polynomial.polynomial.Polynomial.fit")
 class method is preferred:

In \[5\]: p\_fitted \= np.polynomial.Polynomial.fit(x, y, deg\=1)

In \[6\]: p\_fitted
Out\[6\]: Polynomial(\[4.26309174, 4.59313969\], domain=\[0., 9.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Note that the coefficients are given _in the scaled domain_ defined by the linear mapping between the `window` and `domain`. [`convert`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.convert.html#numpy.polynomial.polynomial.Polynomial.convert "numpy.polynomial.polynomial.Polynomial.convert")
 can be used to get the coefficients in the unscaled data domain.

In \[7\]: p\_fitted.convert()
Out\[7\]: Polynomial(\[-0.33004794,  1.02069771\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')

Copy to clipboard

Documentation for the [`polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 package[#](https://numpy.org/doc/stable/reference/routines.polynomials.html#documentation-for-the-polynomial-package "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to standard power series polynomials, the polynomial package provides several additional kinds of polynomials including Chebyshev, Hermite (two subtypes), Laguerre, and Legendre polynomials. Each of these has an associated _convenience class_ available from the [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 namespace that provides a consistent interface for working with polynomials regardless of their type.

*   [Using the convenience classes](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html)
    

Documentation pertaining to specific functions defined for each kind of polynomial individually can be found in the corresponding module documentation:

*   [Power Series (`numpy.polynomial.polynomial`)](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html)
    
*   [Chebyshev Series (`numpy.polynomial.chebyshev`)](https://numpy.org/doc/stable/reference/routines.polynomials.chebyshev.html)
    
*   [Hermite Series, “Physicists” (`numpy.polynomial.hermite`)](https://numpy.org/doc/stable/reference/routines.polynomials.hermite.html)
    
*   [HermiteE Series, “Probabilists” (`numpy.polynomial.hermite_e`)](https://numpy.org/doc/stable/reference/routines.polynomials.hermite_e.html)
    
*   [Laguerre Series (`numpy.polynomial.laguerre`)](https://numpy.org/doc/stable/reference/routines.polynomials.laguerre.html)
    
*   [Legendre Series (`numpy.polynomial.legendre`)](https://numpy.org/doc/stable/reference/routines.polynomials.legendre.html)
    
*   [Polyutils](https://numpy.org/doc/stable/reference/routines.polynomials.polyutils.html)
    

Documentation for legacy polynomials[#](https://numpy.org/doc/stable/reference/routines.polynomials.html#documentation-for-legacy-polynomials "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Poly1d](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html)
    *   [Basics](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#basics)
        
    *   [Fitting](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#fitting)
        
    *   [Calculus](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#calculus)
        
    *   [Arithmetic](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#arithmetic)
        

On this page