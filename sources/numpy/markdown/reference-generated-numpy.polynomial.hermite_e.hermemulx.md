[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemulx.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.hermemulx.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.hermemulx[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemulx.html#numpy-polynomial-hermite-e-hermemulx "Link to this heading")

=================================================================================================================================================================================================

polynomial.hermite\_e.hermemulx(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite_e.py#L393-L443)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemulx.html#numpy.polynomial.hermite_e.hermemulx "Link to this definition")

Multiply a Hermite series by x.

Multiply the Hermite series _c_ by x, where x is the independent variable.

Parameters:

**c**array\_like

1-D array of Hermite series coefficients ordered from low to high.

Returns:

**out**ndarray

Array representing the result of the multiplication.

See also

[`hermeadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermeadd.html#numpy.polynomial.hermite_e.hermeadd "numpy.polynomial.hermite_e.hermeadd")
, [`hermesub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermesub.html#numpy.polynomial.hermite_e.hermesub "numpy.polynomial.hermite_e.hermesub")
, [`hermemul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermemul.html#numpy.polynomial.hermite_e.hermemul "numpy.polynomial.hermite_e.hermemul")
, [`hermediv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermediv.html#numpy.polynomial.hermite_e.hermediv "numpy.polynomial.hermite_e.hermediv")
, [`hermepow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermepow.html#numpy.polynomial.hermite_e.hermepow "numpy.polynomial.hermite_e.hermepow")

Notes

The multiplication uses the recursion relationship for Hermite polynomials in the form

\\\[xP\_i(x) = (P\_{i + 1}(x) + iP\_{i - 1}(x)))\\\]

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite\_e import hermemulx
\>>> hermemulx(\[1, 2, 3\])
array(\[2.,  7.,  2.,  3.\])

Copy to clipboard

Go BackOpen In Tab

On this page