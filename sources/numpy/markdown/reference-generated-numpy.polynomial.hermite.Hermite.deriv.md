[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.Hermite.deriv[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html#numpy-polynomial-hermite-hermite-deriv "Link to this heading")

======================================================================================================================================================================================================

method

polynomial.hermite.Hermite.deriv(_m\=1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L878-L898)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.deriv.html#numpy.polynomial.hermite.Hermite.deriv "Link to this definition")

Differentiate.

Return a series instance of that is the derivative of the current series.

Parameters:

**m**non-negative int

Find the derivative of order _m_.

Returns:

**new\_series**series

A new series representing the derivative. The domain is the same as the domain of the differentiated series.

On this page