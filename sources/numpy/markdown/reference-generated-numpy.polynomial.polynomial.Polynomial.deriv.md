[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.deriv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.Polynomial.deriv[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.deriv.html#numpy-polynomial-polynomial-polynomial-deriv "Link to this heading")

========================================================================================================================================================================================================================

method

polynomial.polynomial.Polynomial.deriv(_m\=1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L878-L898)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.deriv.html#numpy.polynomial.polynomial.Polynomial.deriv "Link to this definition")

Differentiate.

Return a series instance of that is the derivative of the current series.

Parameters:

**m**non-negative int

Find the derivative of order _m_.

Returns:

**new\_series**series

A new series representing the derivative. The domain is the same as the domain of the differentiated series.

On this page