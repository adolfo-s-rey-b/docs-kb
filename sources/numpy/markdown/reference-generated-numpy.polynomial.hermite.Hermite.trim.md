[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.trim.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.Hermite.trim.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.Hermite.trim[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.trim.html#numpy-polynomial-hermite-hermite-trim "Link to this heading")

===================================================================================================================================================================================================

method

polynomial.hermite.Hermite.trim(_tol\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L727-L748)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.Hermite.trim.html#numpy.polynomial.hermite.Hermite.trim "Link to this definition")

Remove trailing coefficients

Remove trailing coefficients until a coefficient is reached whose absolute value greater than _tol_ or the beginning of the series is reached. If all the coefficients would be removed the series is set to `[0]`. A new series instance is returned with the new coefficients. The current instance remains unchanged.

Parameters:

**tol**non-negative number.

All trailing coefficients less than _tol_ will be removed.

Returns:

**new\_series**series

New instance of series with trimmed coefficients.

On this page