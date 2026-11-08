[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legsub.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.legsub.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legsub.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.legsub.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.legsub.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.legsub.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.legsub.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.legsub.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.legsub.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.legsub[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legsub.html#numpy-polynomial-legendre-legsub "Link to this heading")

====================================================================================================================================================================================

polynomial.legendre.legsub(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L365-L406)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legsub.html#numpy.polynomial.legendre.legsub "Link to this definition")

Subtract one Legendre series from another.

Returns the difference of two Legendre series _c1_ - _c2_. The sequences of coefficients are from lowest order term to highest, i.e., \[1,2,3\] represents the series `P_0 + 2*P_1 + 3*P_2`.

Parameters:

**c1, c2**array\_like

1-D arrays of Legendre series coefficients ordered from low to high.

Returns:

**out**ndarray

Of Legendre series coefficients representing their difference.

See also

[`legadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legadd.html#numpy.polynomial.legendre.legadd "numpy.polynomial.legendre.legadd")
, [`legmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmulx.html#numpy.polynomial.legendre.legmulx "numpy.polynomial.legendre.legmulx")
, [`legmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmul.html#numpy.polynomial.legendre.legmul "numpy.polynomial.legendre.legmul")
, [`legdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legdiv.html#numpy.polynomial.legendre.legdiv "numpy.polynomial.legendre.legdiv")
, [`legpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legpow.html#numpy.polynomial.legendre.legpow "numpy.polynomial.legendre.legpow")

Notes

Unlike multiplication, division, etc., the difference of two Legendre series is a Legendre series (without having to “reproject” the result onto the basis set) so subtraction, just like that of “standard” polynomials, is simply “component-wise.”

Examples

Try it in your browser!

\>>> from numpy.polynomial import legendre as L
\>>> c1 \= (1,2,3)
\>>> c2 \= (3,2,1)
\>>> L.legsub(c1,c2)
array(\[-2.,  0.,  2.\])
\>>> L.legsub(c2,c1) \# -C.legsub(c1,c2)
array(\[ 2.,  0., -2.\])

Copy to clipboard

Go BackOpen In Tab

On this page