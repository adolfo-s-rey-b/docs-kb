[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyroots.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polyroots.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polyroots.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyroots[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyroots.html#numpy-polynomial-polynomial-polyroots "Link to this heading")

===================================================================================================================================================================================================

polynomial.polynomial.polyroots(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L1545-L1608)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyroots.html#numpy.polynomial.polynomial.polyroots "Link to this definition")

Compute the roots of a polynomial.

Return the roots (a.k.a. “zeros”) of the polynomial

\\\[p(x) = \\sum\_i c\[i\] \* x^i.\\\]

Parameters:

**c**1-D array\_like

1-D array of polynomial coefficients.

Returns:

**out**ndarray

Array of the roots of the polynomial. If all the roots are real, then _out_ is also real, otherwise it is complex.

See also

[`numpy.polynomial.chebyshev.chebroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebroots.html#numpy.polynomial.chebyshev.chebroots "numpy.polynomial.chebyshev.chebroots")

[`numpy.polynomial.legendre.legroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legroots.html#numpy.polynomial.legendre.legroots "numpy.polynomial.legendre.legroots")

[`numpy.polynomial.laguerre.lagroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagroots.html#numpy.polynomial.laguerre.lagroots "numpy.polynomial.laguerre.lagroots")

[`numpy.polynomial.hermite.hermroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermroots.html#numpy.polynomial.hermite.hermroots "numpy.polynomial.hermite.hermroots")

[`numpy.polynomial.hermite_e.hermeroots`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeroots.html#numpy.polynomial.hermite_e.hermeroots "numpy.polynomial.hermite_e.hermeroots")

Notes

The root estimates are obtained as the eigenvalues of the companion matrix, Roots far from the origin of the complex plane may have large errors due to the numerical instability of the power series for such values. Roots with multiplicity greater than 1 will also show larger errors as the value of the series near such points is relatively insensitive to errors in the roots. Isolated roots near the origin can be improved by a few iterations of Newton’s method.

Examples

Try it in your browser!

\>>> import numpy.polynomial.polynomial as poly
\>>> poly.polyroots(poly.polyfromroots((\-1,0,1)))
array(\[-1.,  0.,  1.\])
\>>> poly.polyroots(poly.polyfromroots((\-1,0,1))).dtype
dtype('float64')
\>>> j \= complex(0,1)
\>>> poly.polyroots(poly.polyfromroots((\-j,0,j)))
array(\[  0.00000000e+00+0.j,   0.00000000e+00+1.j,   2.77555756e-17-1.j\])  # may vary

Copy to clipboard

Go BackOpen In Tab

On this page