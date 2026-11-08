[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.Legendre.linspace[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html#numpy-polynomial-legendre-legendre-linspace "Link to this heading")

=====================================================================================================================================================================================================================

method

polynomial.legendre.Legendre.linspace(_n\=100_, _domain\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L915-L943)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.linspace.html#numpy.polynomial.legendre.Legendre.linspace "Link to this definition")

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