[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermdiv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.hermdiv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.hermdiv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.hermdiv[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermdiv.html#numpy-polynomial-hermite-hermdiv "Link to this heading")

====================================================================================================================================================================================

polynomial.hermite.hermdiv(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite.py#L512-L557)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermdiv.html#numpy.polynomial.hermite.hermdiv "Link to this definition")

Divide one Hermite series by another.

Returns the quotient-with-remainder of two Hermite series _c1_ / _c2_. The arguments are sequences of coefficients from lowest order “term” to highest, e.g., \[1,2,3\] represents the series `P_0 + 2*P_1 + 3*P_2`.

Parameters:

**c1, c2**array\_like

1-D arrays of Hermite series coefficients ordered from low to high.

Returns:

**\[quo, rem\]**ndarrays

Of Hermite series coefficients representing the quotient and remainder.

See also

[`hermadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermadd.html#numpy.polynomial.hermite.hermadd "numpy.polynomial.hermite.hermadd")
, [`hermsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermsub.html#numpy.polynomial.hermite.hermsub "numpy.polynomial.hermite.hermsub")
, [`hermmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmulx.html#numpy.polynomial.hermite.hermmulx "numpy.polynomial.hermite.hermmulx")
, [`hermmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmul.html#numpy.polynomial.hermite.hermmul "numpy.polynomial.hermite.hermmul")
, [`hermpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermpow.html#numpy.polynomial.hermite.hermpow "numpy.polynomial.hermite.hermpow")

Notes

In general, the (polynomial) division of one Hermite series by another results in quotient and remainder terms that are not in the Hermite polynomial basis set. Thus, to express these results as a Hermite series, it is necessary to “reproject” the results onto the Hermite basis set, which may produce “unintuitive” (but correct) results; see Examples section below.

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite import hermdiv
\>>> hermdiv(\[ 52.,  29.,  52.,   7.,   6.\], \[0, 1, 2\])
(array(\[1., 2., 3.\]), array(\[0.\]))
\>>> hermdiv(\[ 54.,  31.,  52.,   7.,   6.\], \[0, 1, 2\])
(array(\[1., 2., 3.\]), array(\[2., 2.\]))
\>>> hermdiv(\[ 53.,  30.,  52.,   7.,   6.\], \[0, 1, 2\])
(array(\[1., 2., 3.\]), array(\[1., 1.\]))

Copy to clipboard

Go BackOpen In Tab

On this page