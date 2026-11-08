[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmul.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.legmul.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmul.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.legmul.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.legmul.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.legmul.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.legmul.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.legmul.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.legmul.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.legmul[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmul.html#numpy-polynomial-legendre-legmul "Link to this heading")

====================================================================================================================================================================================

polynomial.legendre.legmul(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L465-L530)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmul.html#numpy.polynomial.legendre.legmul "Link to this definition")

Multiply one Legendre series by another.

Returns the product of two Legendre series _c1_ \* _c2_. The arguments are sequences of coefficients, from lowest order “term” to highest, e.g., \[1,2,3\] represents the series `P_0 + 2*P_1 + 3*P_2`.

Parameters:

**c1, c2**array\_like

1-D arrays of Legendre series coefficients ordered from low to high.

Returns:

**out**ndarray

Of Legendre series coefficients representing their product.

See also

[`legadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legadd.html#numpy.polynomial.legendre.legadd "numpy.polynomial.legendre.legadd")
, [`legsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legsub.html#numpy.polynomial.legendre.legsub "numpy.polynomial.legendre.legsub")
, [`legmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmulx.html#numpy.polynomial.legendre.legmulx "numpy.polynomial.legendre.legmulx")
, [`legdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legdiv.html#numpy.polynomial.legendre.legdiv "numpy.polynomial.legendre.legdiv")
, [`legpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legpow.html#numpy.polynomial.legendre.legpow "numpy.polynomial.legendre.legpow")

Notes

In general, the (polynomial) product of two C-series results in terms that are not in the Legendre polynomial basis set. Thus, to express the product as a Legendre series, it is necessary to “reproject” the product onto said basis set, which may produce “unintuitive” (but correct) results; see Examples section below.

Examples

Try it in your browser!

\>>> from numpy.polynomial import legendre as L
\>>> c1 \= (1,2,3)
\>>> c2 \= (3,2)
\>>> L.legmul(c1,c2) \# multiplication requires "reprojection"
array(\[  4.33333333,  10.4       ,  11.66666667,   3.6       \]) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page