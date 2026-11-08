[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.filled.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.filled.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.filled.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.filled.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.filled.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.filled.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.filled.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.filled.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.filled.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.filled.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.filled.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.filled.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.filled.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.filled.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.filled.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.filled.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.filled.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.filled.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.filled.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.filled.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.filled.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.filled.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.filled[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.filled.html#numpy-ma-filled "Link to this heading")

=================================================================================================================================

ma.filled(_a_, _fill\_value\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L631-L690)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.filled.html#numpy.ma.filled "Link to this definition")

Return input as an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, with masked values replaced by _fill\_value_.

If _a_ is not a [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, _a_ itself is returned. If _a_ is a [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 with no masked values, then `a.data` is returned. If _a_ is a [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 and _fill\_value_ is None, _fill\_value_ is set to `a.fill_value`.

Parameters:

**a**MaskedArray or array\_like

An input object.

**fill\_value**array\_like, optional.

Can be scalar or non-scalar. If non-scalar, the resulting filled array should be broadcastable over input array. Default is None.

Returns:

**a**ndarray

The filled array.

See also

[`compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html#numpy.ma.compressed "numpy.ma.compressed")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= ma.array(np.arange(9).reshape(3, 3), mask\=\[\[1, 0, 0\],\
...                                                \[1, 0, 0\],\
...                                                \[0, 0, 0\]\])
\>>> x.filled()
array(\[\[999999,      1,      2\],\
       \[999999,      4,      5\],\
       \[     6,      7,      8\]\])
\>>> x.filled(fill\_value\=333)
array(\[\[333,   1,   2\],\
       \[333,   4,   5\],\
       \[  6,   7,   8\]\])
\>>> x.filled(fill\_value\=np.arange(3))
array(\[\[0, 1, 2\],\
       \[0, 4, 5\],\
       \[6, 7, 8\]\])

Copy to clipboard

Go BackOpen In Tab

On this page