[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.filled.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.filled.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.filled.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.filled.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.filled.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.filled.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.filled.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.filled.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.filled.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.filled[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.filled.html#numpy-ma-maskedarray-filled "Link to this heading")

=====================================================================================================================================================================

method

ma.MaskedArray.filled(_fill\_value\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L3857-L3936)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.filled.html#numpy.ma.MaskedArray.filled "Link to this definition")

Return a copy of self, with masked values filled with a given value. **However**, if there are no masked values to fill, self will be returned instead as an ndarray.

Parameters:

**fill\_value**array\_like, optional

The value to use for invalid entries. Can be scalar or non-scalar. If non-scalar, the resulting ndarray must be broadcastable over input array. Default is None, in which case, the [`fill_value`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "numpy.ma.MaskedArray.fill_value")
 attribute of the array is used instead.

Returns:

**filled\_array**ndarray

A copy of `self` with invalid entries replaced by _fill\_value_ (be it the function argument or the attribute of `self`), or `self` itself as an ndarray if there are no invalid entries to be replaced.

Notes

The result is **not** a MaskedArray!

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[1,2,3,4,5\], mask\=\[0,0,1,0,1\], fill\_value\=-999)
\>>> x.filled()
array(\[   1,    2, -999,    4, -999\])
\>>> x.filled(fill\_value\=1000)
array(\[   1,    2, 1000,    4, 1000\])
\>>> type(x.filled())
<class 'numpy.ndarray'>

Copy to clipboard

Subclassing is preserved. This means that if, e.g., the data part of the masked array is a recarray, [`filled`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.filled.html#numpy.ma.MaskedArray.filled "numpy.ma.MaskedArray.filled")
 returns a recarray:

\>>> x \= np.array(\[(\-1, 2), (\-3, 4)\], dtype\='i8,i8').view(np.recarray)
\>>> m \= np.ma.array(x, mask\=\[(True, False), (False, True)\])
\>>> m.filled()
rec.array(\[(999999,      2), (    -3, 999999)\],
          dtype=\[('f0', '<i8'), ('f1', '<i8')\])

Copy to clipboard

Go BackOpen In Tab

On this page