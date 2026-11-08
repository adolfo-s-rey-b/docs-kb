[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.identity.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.Legendre.identity.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.Legendre.identity[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.identity.html#numpy-polynomial-legendre-legendre-identity "Link to this heading")

=====================================================================================================================================================================================================================

method

_classmethod_ polynomial.legendre.Legendre.identity(_domain\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L1079-L1112)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.Legendre.identity.html#numpy.polynomial.legendre.Legendre.identity "Link to this definition")

Identity function.

If `p` is the returned series, then `p(x) == x` for all values of x.

Parameters:

**domain**{None, array\_like}, optional

If given, the array must be of the form `[beg, end]`, where `beg` and `end` are the endpoints of the domain. If None is given then the class domain is used. The default is None.

**window**{None, array\_like}, optional

If given, the resulting array must be if the form `[beg, end]`, where `beg` and `end` are the endpoints of the window. If None is given then the class window is used. The default is None.

**symbol**str, optional

Symbol representing the independent variable. Default is ‘x’.

Returns:

**new\_series**series

Series of representing the identity.

On this page