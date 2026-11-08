[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmulx.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.hermmulx.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.hermmulx.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.hermmulx[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmulx.html#numpy-polynomial-hermite-hermmulx "Link to this heading")

=======================================================================================================================================================================================

polynomial.hermite.hermmulx(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite.py#L393-L443)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmulx.html#numpy.polynomial.hermite.hermmulx "Link to this definition")

Multiply a Hermite series by x.

Multiply the Hermite series _c_ by x, where x is the independent variable.

Parameters:

**c**array\_like

1-D array of Hermite series coefficients ordered from low to high.

Returns:

**out**ndarray

Array representing the result of the multiplication.

See also

[`hermadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermadd.html#numpy.polynomial.hermite.hermadd "numpy.polynomial.hermite.hermadd")
, [`hermsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermsub.html#numpy.polynomial.hermite.hermsub "numpy.polynomial.hermite.hermsub")
, [`hermmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmul.html#numpy.polynomial.hermite.hermmul "numpy.polynomial.hermite.hermmul")
, [`hermdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermdiv.html#numpy.polynomial.hermite.hermdiv "numpy.polynomial.hermite.hermdiv")
, [`hermpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermpow.html#numpy.polynomial.hermite.hermpow "numpy.polynomial.hermite.hermpow")

Notes

The multiplication uses the recursion relationship for Hermite polynomials in the form

\\\[xP\_i(x) = (P\_{i + 1}(x)/2 + i\*P\_{i - 1}(x))\\\]

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite import hermmulx
\>>> hermmulx(\[1, 2, 3\])
array(\[2. , 6.5, 1. , 1.5\])

Copy to clipboard

Go BackOpen In Tab

On this page