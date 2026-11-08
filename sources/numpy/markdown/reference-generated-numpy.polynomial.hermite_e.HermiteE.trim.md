[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.trim.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.HermiteE.trim[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.trim.html#numpy-polynomial-hermite-e-hermitee-trim "Link to this heading")

=============================================================================================================================================================================================================

method

polynomial.hermite\_e.HermiteE.trim(_tol\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L727-L748)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.trim.html#numpy.polynomial.hermite_e.HermiteE.trim "Link to this definition")

Remove trailing coefficients

Remove trailing coefficients until a coefficient is reached whose absolute value greater than _tol_ or the beginning of the series is reached. If all the coefficients would be removed the series is set to `[0]`. A new series instance is returned with the new coefficients. The current instance remains unchanged.

Parameters:

**tol**non-negative number.

All trailing coefficients less than _tol_ will be removed.

Returns:

**new\_series**series

New instance of series with trimmed coefficients.

On this page