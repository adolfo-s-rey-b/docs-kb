[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legweight.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.legweight.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legweight.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.legweight.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.legweight.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.legweight.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.legweight.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.legweight.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.legweight.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.legweight[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legweight.html#numpy-polynomial-legendre-legweight "Link to this heading")

=============================================================================================================================================================================================

polynomial.legendre.legweight(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L1587-L1606)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legweight.html#numpy.polynomial.legendre.legweight "Link to this definition")

Weight function of the Legendre polynomials.

The weight function is and the interval of integration is \[-1, 1\]. The Legendre polynomials are orthogonal, but not normalized, with respect to this weight function.

Parameters:

**x**array\_like

Values at which the weight function will be computed.

Returns:

**w**ndarray

The weight function at _x_.

On this page