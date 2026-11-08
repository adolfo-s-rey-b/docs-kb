[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.polyutils.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.polyutils.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.polyutils.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.polyutils.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.polyutils.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.polyutils.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.polyutils.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.polyutils.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.polyutils.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.polyutils.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.polyutils.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.polyutils.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.polyutils.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.polyutils.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.polyutils.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.polyutils.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.polyutils.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.polyutils.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.polyutils.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.polyutils.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.polyutils.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.polyutils.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Polyutils[#](https://numpy.org/doc/stable/reference/routines.polynomials.polyutils.html#module-numpy.polynomial.polyutils "Link to this heading")

==================================================================================================================================================

Utility classes and functions for the polynomial modules.

This module provides: error and warning objects; a polynomial base class; and some routines used in both the _polynomial_ and _chebyshev_ modules.

Functions[#](https://numpy.org/doc/stable/reference/routines.polynomials.polyutils.html#functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`as_series`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.as_series.html#numpy.polynomial.polyutils.as_series "numpy.polynomial.polyutils.as_series")<br>(alist\[, trim\]) | Return argument as a list of 1-d arrays. |
| [`trimseq`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.trimseq.html#numpy.polynomial.polyutils.trimseq "numpy.polynomial.polyutils.trimseq")<br>(seq) | Remove small Poly series coefficients. |
| [`trimcoef`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.trimcoef.html#numpy.polynomial.polyutils.trimcoef "numpy.polynomial.polyutils.trimcoef")<br>(c\[, tol\]) | Remove "small" "trailing" coefficients from a polynomial. |
| [`getdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.getdomain.html#numpy.polynomial.polyutils.getdomain "numpy.polynomial.polyutils.getdomain")<br>(x) | Return a domain suitable for given abscissae. |
| [`mapdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapdomain.html#numpy.polynomial.polyutils.mapdomain "numpy.polynomial.polyutils.mapdomain")<br>(x, old, new) | Apply linear map to input points. |
| [`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapparms.html#numpy.polynomial.polyutils.mapparms "numpy.polynomial.polyutils.mapparms")<br>(old, new) | Linear map parameters between domains. |

On this page