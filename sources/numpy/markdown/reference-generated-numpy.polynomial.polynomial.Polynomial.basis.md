[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.basis.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.Polynomial.basis[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.basis.html#numpy-polynomial-polynomial-polynomial-basis "Link to this heading")

========================================================================================================================================================================================================================

method

_classmethod_ polynomial.polynomial.Polynomial.basis(_deg_, _domain\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L1114-L1151)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.basis.html#numpy.polynomial.polynomial.Polynomial.basis "Link to this definition")

Series basis polynomial of degree _deg_.

Returns the series representing the basis polynomial of degree _deg_.

Parameters:

**deg**int

Degree of the basis polynomial for the series. Must be >= 0.

**domain**{None, array\_like}, optional

If given, the array must be of the form `[beg, end]`, where `beg` and `end` are the endpoints of the domain. If None is given then the class domain is used. The default is None.

**window**{None, array\_like}, optional

If given, the resulting array must be if the form `[beg, end]`, where `beg` and `end` are the endpoints of the window. If None is given then the class window is used. The default is None.

**symbol**str, optional

Symbol representing the independent variable. Default is ‘x’.

Returns:

**new\_series**series

A series with the coefficient of the _deg_ term set to one and all others zero.

On this page