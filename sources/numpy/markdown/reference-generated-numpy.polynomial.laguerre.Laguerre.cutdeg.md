[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.laguerre.Laguerre.cutdeg[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html#numpy-polynomial-laguerre-laguerre-cutdeg "Link to this heading")

===============================================================================================================================================================================================================

method

polynomial.laguerre.Laguerre.cutdeg(_deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L704-L725)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.Laguerre.cutdeg.html#numpy.polynomial.laguerre.Laguerre.cutdeg "Link to this definition")

Truncate series to the given degree.

Reduce the degree of the series to _deg_ by discarding the high order terms. If _deg_ is greater than the current degree a copy of the current series is returned. This can be useful in least squares where the coefficients of the high degree terms may be very small.

Parameters:

**deg**non-negative int

The series is reduced to degree _deg_ by discarding the high order terms. The value of _deg_ must be a non-negative integer.

Returns:

**new\_series**series

New instance of series with reduced degree.

On this page