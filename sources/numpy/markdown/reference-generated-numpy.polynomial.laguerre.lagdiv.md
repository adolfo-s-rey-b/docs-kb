[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagdiv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.laguerre.lagdiv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.laguerre.lagdiv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.laguerre.lagdiv[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagdiv.html#numpy-polynomial-laguerre-lagdiv "Link to this heading")

====================================================================================================================================================================================

polynomial.laguerre.lagdiv(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/laguerre.py#L508-L551)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagdiv.html#numpy.polynomial.laguerre.lagdiv "Link to this definition")

Divide one Laguerre series by another.

Returns the quotient-with-remainder of two Laguerre series _c1_ / _c2_. The arguments are sequences of coefficients from lowest order “term” to highest, e.g., \[1,2,3\] represents the series `P_0 + 2*P_1 + 3*P_2`.

Parameters:

**c1, c2**array\_like

1-D arrays of Laguerre series coefficients ordered from low to high.

Returns:

**\[quo, rem\]**ndarrays

Of Laguerre series coefficients representing the quotient and remainder.

See also

[`lagadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagadd.html#numpy.polynomial.laguerre.lagadd "numpy.polynomial.laguerre.lagadd")
, [`lagsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagsub.html#numpy.polynomial.laguerre.lagsub "numpy.polynomial.laguerre.lagsub")
, [`lagmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagmulx.html#numpy.polynomial.laguerre.lagmulx "numpy.polynomial.laguerre.lagmulx")
, [`lagmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagmul.html#numpy.polynomial.laguerre.lagmul "numpy.polynomial.laguerre.lagmul")
, [`lagpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagpow.html#numpy.polynomial.laguerre.lagpow "numpy.polynomial.laguerre.lagpow")

Notes

In general, the (polynomial) division of one Laguerre series by another results in quotient and remainder terms that are not in the Laguerre polynomial basis set. Thus, to express these results as a Laguerre series, it is necessary to “reproject” the results onto the Laguerre basis set, which may produce “unintuitive” (but correct) results; see Examples section below.

Examples

Try it in your browser!

\>>> from numpy.polynomial.laguerre import lagdiv
\>>> lagdiv(\[  8., \-13.,  38., \-51.,  36.\], \[0, 1, 2\])
(array(\[1., 2., 3.\]), array(\[0.\]))
\>>> lagdiv(\[  9., \-12.,  38., \-51.,  36.\], \[0, 1, 2\])
(array(\[1., 2., 3.\]), array(\[1., 1.\]))

Copy to clipboard

Go BackOpen In Tab

On this page