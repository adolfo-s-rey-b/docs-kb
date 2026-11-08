[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.linspace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.Chebyshev.linspace[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.linspace.html#numpy-polynomial-chebyshev-chebyshev-linspace "Link to this heading")

===========================================================================================================================================================================================================================

method

polynomial.chebyshev.Chebyshev.linspace(_n\=100_, _domain\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L915-L943)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.linspace.html#numpy.polynomial.chebyshev.Chebyshev.linspace "Link to this definition")

Return x, y values at equally spaced points in domain.

Returns the x, y values at _n_ linearly spaced points across the domain. Here y is the value of the polynomial at the points x. By default the domain is the same as that of the series instance. This method is intended mostly as a plotting aid.

Parameters:

**n**int, optional

Number of point pairs to return. The default value is 100.

**domain**{None, array\_like}, optional

If not None, the specified domain is used instead of that of the calling instance. It should be of the form `[beg,end]`. The default is None which case the class domain is used.

Returns:

**x, y**ndarray

x is equal to linspace(self.domain\[0\], self.domain\[1\], n) and y is the series evaluated at element of x.

On this page