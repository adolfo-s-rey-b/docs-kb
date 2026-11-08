[Skip to main content](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.polynomials.poly1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.polynomials.poly1d.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.polynomials.poly1d.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.polynomials.poly1d.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.polynomials.poly1d.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.polynomials.poly1d.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.polynomials.poly1d.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.polynomials.poly1d.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.polynomials.poly1d.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.polynomials.poly1d.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.polynomials.poly1d.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.polynomials.poly1d.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.polynomials.poly1d.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.polynomials.poly1d.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.polynomials.poly1d.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.polynomials.poly1d.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.polynomials.poly1d.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.polynomials.poly1d.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.polynomials.poly1d.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.polynomials.poly1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Poly1d[#](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#poly1d "Link to this heading")

=================================================================================================================

Basics[#](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#basics "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")<br>(c\_or\_r\[, r, variable\]) | A one-dimensional polynomial class. |
| [`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")<br>(p, x) | Evaluate a polynomial at specific values. |
| [`poly`](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#numpy.poly "numpy.poly")<br>(seq\_of\_zeros) | Find the coefficients of a polynomial with the given sequence of roots. |
| [`roots`](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#numpy.roots "numpy.roots")<br>(p) | Return the roots of a polynomial with coefficients given in p. |

Fitting[#](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#fitting "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")<br>(x, y, deg\[, rcond, full, w, cov\]) | Least squares polynomial fit. |

Calculus[#](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#calculus "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`polyder`](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html#numpy.polyder "numpy.polyder")<br>(p\[, m\]) | Return the derivative of the specified order of a polynomial. |
| [`polyint`](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html#numpy.polyint "numpy.polyint")<br>(p\[, m, k\]) | Return an antiderivative (indefinite integral) of a polynomial. |

Arithmetic[#](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html#arithmetic "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`polyadd`](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy.polyadd "numpy.polyadd")<br>(a1, a2) | Find the sum of two polynomials. |
| [`polydiv`](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html#numpy.polydiv "numpy.polydiv")<br>(u, v) | Returns the quotient and remainder of polynomial division. |
| [`polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")<br>(a1, a2) | Find the product of two polynomials. |
| [`polysub`](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html#numpy.polysub "numpy.polysub")<br>(a1, a2) | Difference (subtraction) of two polynomials. |

On this page