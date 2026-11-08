[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leg2poly.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.leg2poly.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.leg2poly.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.leg2poly[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leg2poly.html#numpy-polynomial-legendre-leg2poly "Link to this heading")

==========================================================================================================================================================================================

polynomial.legendre.leg2poly(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L148-L207)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leg2poly.html#numpy.polynomial.legendre.leg2poly "Link to this definition")

Convert a Legendre series to a polynomial.

Convert an array representing the coefficients of a Legendre series, ordered from lowest degree to highest, to an array of the coefficients of the equivalent polynomial (relative to the “standard” basis) ordered from lowest to highest degree.

Parameters:

**c**array\_like

1-D array containing the Legendre series coefficients, ordered from lowest order term to highest.

Returns:

**pol**ndarray

1-D array containing the coefficients of the equivalent polynomial (relative to the “standard” basis) ordered from lowest order term to highest.

See also

[`poly2leg`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.poly2leg.html#numpy.polynomial.legendre.poly2leg "numpy.polynomial.legendre.poly2leg")

Notes

The easy way to do conversions between polynomial basis sets is to use the convert method of a class instance.

Examples

Try it in your browser!

\>>> from numpy import polynomial as P
\>>> c \= P.Legendre(range(4))
\>>> c
Legendre(\[0., 1., 2., 3.\], domain=\[-1.,  1.\], window=\[-1.,  1.\], symbol='x')
\>>> p \= c.convert(kind\=P.Polynomial)
\>>> p
Polynomial(\[-1. , -3.5,  3. ,  7.5\], domain=\[-1.,  1.\], window=\[-1., ...\
\>>> P.legendre.leg2poly(range(4))\
array(\[-1. , -3.5,  3. ,  7.5\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page