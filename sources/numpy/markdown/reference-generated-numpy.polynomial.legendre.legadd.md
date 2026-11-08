[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legadd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.legadd.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legadd.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.legadd.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.legadd.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.legadd.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.legadd.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.legadd.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.legadd.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.legadd[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legadd.html#numpy-polynomial-legendre-legadd "Link to this heading")

====================================================================================================================================================================================

polynomial.legendre.legadd(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L323-L362)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legadd.html#numpy.polynomial.legendre.legadd "Link to this definition")

Add one Legendre series to another.

Returns the sum of two Legendre series _c1_ + _c2_. The arguments are sequences of coefficients ordered from lowest order term to highest, i.e., \[1,2,3\] represents the series `P_0 + 2*P_1 + 3*P_2`.

Parameters:

**c1, c2**array\_like

1-D arrays of Legendre series coefficients ordered from low to high.

Returns:

**out**ndarray

Array representing the Legendre series of their sum.

See also

[`legsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legsub.html#numpy.polynomial.legendre.legsub "numpy.polynomial.legendre.legsub")
, [`legmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmulx.html#numpy.polynomial.legendre.legmulx "numpy.polynomial.legendre.legmulx")
, [`legmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmul.html#numpy.polynomial.legendre.legmul "numpy.polynomial.legendre.legmul")
, [`legdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legdiv.html#numpy.polynomial.legendre.legdiv "numpy.polynomial.legendre.legdiv")
, [`legpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legpow.html#numpy.polynomial.legendre.legpow "numpy.polynomial.legendre.legpow")

Notes

Unlike multiplication, division, etc., the sum of two Legendre series is a Legendre series (without having to “reproject” the result onto the basis set) so addition, just like that of “standard” polynomials, is simply “component-wise.”

Examples

Try it in your browser!

\>>> from numpy.polynomial import legendre as L
\>>> c1 \= (1,2,3)
\>>> c2 \= (3,2,1)
\>>> L.legadd(c1,c2)
array(\[4.,  4.,  4.\])

Copy to clipboard

Go BackOpen In Tab

On this page