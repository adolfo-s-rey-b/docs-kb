[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.get_fill_value.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.get_fill_value.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.get\_fill\_value[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.get_fill_value.html#numpy-ma-maskedarray-get-fill-value "Link to this heading")

===============================================================================================================================================================================================

method

ma.MaskedArray.get\_fill\_value()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L3792-L3832)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.get_fill_value.html#numpy.ma.MaskedArray.get_fill_value "Link to this definition")

The filling value of the masked array is a scalar. When setting, None will set to a default based on the data type.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> for dt in \[np.int32, np.int64, np.float64, np.complex128\]:
...     np.ma.array(\[0, 1\], dtype\=dt).get\_fill\_value()
...
np.int64(999999)
np.int64(999999)
np.float64(1e+20)
np.complex128(1e+20+0j)

Copy to clipboard

\>>> x \= np.ma.array(\[0, 1.\], fill\_value\=-np.inf)
\>>> x.fill\_value
np.float64(-inf)
\>>> x.fill\_value \= np.pi
\>>> x.fill\_value
np.float64(3.1415926535897931)

Copy to clipboard

Reset to default:

\>>> x.fill\_value \= None
\>>> x.fill\_value
np.float64(1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page