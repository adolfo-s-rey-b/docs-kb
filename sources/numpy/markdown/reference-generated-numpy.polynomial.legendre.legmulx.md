[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmulx.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.legmulx.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmulx.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.legmulx.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.legmulx.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.legmulx.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.legmulx.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.legmulx.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.legmulx.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.legmulx[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmulx.html#numpy-polynomial-legendre-legmulx "Link to this heading")

=======================================================================================================================================================================================

polynomial.legendre.legmulx(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L409-L462)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmulx.html#numpy.polynomial.legendre.legmulx "Link to this definition")

Multiply a Legendre series by x.

Multiply the Legendre series _c_ by x, where x is the independent variable.

Parameters:

**c**array\_like

1-D array of Legendre series coefficients ordered from low to high.

Returns:

**out**ndarray

Array representing the result of the multiplication.

See also

[`legadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legadd.html#numpy.polynomial.legendre.legadd "numpy.polynomial.legendre.legadd")
, [`legsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legsub.html#numpy.polynomial.legendre.legsub "numpy.polynomial.legendre.legsub")
, [`legmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legmul.html#numpy.polynomial.legendre.legmul "numpy.polynomial.legendre.legmul")
, [`legdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legdiv.html#numpy.polynomial.legendre.legdiv "numpy.polynomial.legendre.legdiv")
, [`legpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legpow.html#numpy.polynomial.legendre.legpow "numpy.polynomial.legendre.legpow")

Notes

The multiplication uses the recursion relationship for Legendre polynomials in the form

\\\[xP\_i(x) = ((i + 1)\*P\_{i + 1}(x) + i\*P\_{i - 1}(x))/(2i + 1)\\\]

Examples

Try it in your browser!

\>>> from numpy.polynomial import legendre as L
\>>> L.legmulx(\[1,2,3\])
array(\[ 0.66666667, 2.2, 1.33333333, 1.8\]) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page