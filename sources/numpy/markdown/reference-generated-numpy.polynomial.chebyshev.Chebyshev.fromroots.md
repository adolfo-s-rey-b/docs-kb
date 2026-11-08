[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.Chebyshev.fromroots[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html#numpy-polynomial-chebyshev-chebyshev-fromroots "Link to this heading")

==============================================================================================================================================================================================================================

method

_classmethod_ polynomial.chebyshev.Chebyshev.fromroots(_roots_, _domain\=\[\]_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L1036-L1077)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.fromroots.html#numpy.polynomial.chebyshev.Chebyshev.fromroots "Link to this definition")

Return series instance that has the specified roots.

Returns a series representing the product `(x - r[0])*(x - r[1])*...*(x - r[n-1])`, where `r` is a list of roots.

Parameters:

**roots**array\_like

List of roots.

**domain**{\[\], None, array\_like}, optional

Domain for the resulting series. If None the domain is the interval from the smallest root to the largest. If \[\] the domain is the class domain. The default is \[\].

**window**{None, array\_like}, optional

Window for the returned series. If None the class window is used. The default is None.

**symbol**str, optional

Symbol representing the independent variable. Default is ‘x’.

Returns:

**new\_series**series

Series with the specified roots.

On this page