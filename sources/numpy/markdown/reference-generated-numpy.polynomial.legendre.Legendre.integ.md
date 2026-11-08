[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.integ.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.Legendre.integ[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.integ.html#numpy-polynomial-legendre-legendre-integ "Link to this heading")

============================================================================================================================================================================================================

method

polynomial.legendre.Legendre.integ(_m\=1_, _k\=\[\]_, _lbnd\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L845-L876)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.integ.html#numpy.polynomial.legendre.Legendre.integ "Link to this definition")

Integrate.

Return a series instance that is the definite integral of the current series.

Parameters:

**m**non-negative int

The number of integrations to perform.

**k**array\_like

Integration constants. The first constant is applied to the first integration, the second to the second, and so on. The list of values must less than or equal to _m_ in length and any missing values are set to zero.

**lbnd**Scalar

The lower bound of the definite integral.

Returns:

**new\_series**series

A new series representing the integral. The domain is the same as the domain of the integrated series.

On this page