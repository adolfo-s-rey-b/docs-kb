[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermediv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.hermediv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.hermediv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.hermediv[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermediv.html#numpy-polynomial-hermite-e-hermediv "Link to this heading")

==============================================================================================================================================================================================

polynomial.hermite\_e.hermediv(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L512-L555)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermediv.html#numpy.polynomial.hermite_e.hermediv "Link to this definition")

Divide one Hermite series by another.

Returns the quotient-with-remainder of two Hermite series _c1_ / _c2_. The arguments are sequences of coefficients from lowest order “term” to highest, e.g., \[1,2,3\] represents the series `P_0 + 2*P_1 + 3*P_2`.

Parameters:

**c1, c2**array\_like

1-D arrays of Hermite series coefficients ordered from low to high.

Returns:

**\[quo, rem\]**ndarrays

Of Hermite series coefficients representing the quotient and remainder.

See also

[`hermeadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeadd.html#numpy.polynomial.hermite_e.hermeadd "numpy.polynomial.hermite_e.hermeadd")
, [`hermesub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermesub.html#numpy.polynomial.hermite_e.hermesub "numpy.polynomial.hermite_e.hermesub")
, [`hermemulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemulx.html#numpy.polynomial.hermite_e.hermemulx "numpy.polynomial.hermite_e.hermemulx")
, [`hermemul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemul.html#numpy.polynomial.hermite_e.hermemul "numpy.polynomial.hermite_e.hermemul")
, [`hermepow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermepow.html#numpy.polynomial.hermite_e.hermepow "numpy.polynomial.hermite_e.hermepow")

Notes

In general, the (polynomial) division of one Hermite series by another results in quotient and remainder terms that are not in the Hermite polynomial basis set. Thus, to express these results as a Hermite series, it is necessary to “reproject” the results onto the Hermite basis set, which may produce “unintuitive” (but correct) results; see Examples section below.

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite\_e import hermediv
\>>> hermediv(\[ 14.,  15.,  28.,   7.,   6.\], \[0, 1, 2\])
(array(\[1., 2., 3.\]), array(\[0.\]))
\>>> hermediv(\[ 15.,  17.,  28.,   7.,   6.\], \[0, 1, 2\])
(array(\[1., 2., 3.\]), array(\[1., 2.\]))

Copy to clipboard

Go BackOpen In Tab

On this page