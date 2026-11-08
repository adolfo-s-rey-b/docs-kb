[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite\_e.HermiteE.convert[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html#numpy-polynomial-hermite-e-hermitee-convert "Link to this heading")

======================================================================================================================================================================================================================

method

polynomial.hermite\_e.HermiteE.convert(_domain\=None_, _kind\=None_, _window\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L779-L814)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.HermiteE.convert.html#numpy.polynomial.hermite_e.HermiteE.convert "Link to this definition")

Convert series to a different kind and/or domain and/or window.

Parameters:

**domain**array\_like, optional

The domain of the converted series. If the value is None, the default domain of _kind_ is used.

**kind**class, optional

The polynomial series type class to which the current instance should be converted. If kind is None, then the class of the current instance is used.

**window**array\_like, optional

The window of the converted series. If the value is None, the default window of _kind_ is used.

Returns:

**new\_series**series

The returned class can be of different type than the current instance and/or have a different domain and/or different window.

Notes

Conversion between domains and class types can result in numerically ill defined series.

On this page