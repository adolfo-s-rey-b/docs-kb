[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.Chebyshev.cast[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html#numpy-polynomial-chebyshev-chebyshev-cast "Link to this heading")

===============================================================================================================================================================================================================

method

_classmethod_ polynomial.chebyshev.Chebyshev.cast(_series_, _domain\=None_, _window\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L1153-L1191)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.cast.html#numpy.polynomial.chebyshev.Chebyshev.cast "Link to this definition")

Convert series to series of this class.

The _series_ is expected to be an instance of some polynomial series of one of the types supported by by the numpy.polynomial module, but could be some other class that supports the convert method.

Parameters:

**series**series

The series instance to be converted.

**domain**{None, array\_like}, optional

If given, the array must be of the form `[beg, end]`, where `beg` and `end` are the endpoints of the domain. If None is given then the class domain is used. The default is None.

**window**{None, array\_like}, optional

If given, the resulting array must be if the form `[beg, end]`, where `beg` and `end` are the endpoints of the window. If None is given then the class window is used. The default is None.

Returns:

**new\_series**series

A series of the same kind as the calling class and equal to _series_ when evaluated.

See also

[`convert`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.Chebyshev.convert.html#numpy.polynomial.chebyshev.Chebyshev.convert "numpy.polynomial.chebyshev.Chebyshev.convert")

similar instance method

On this page