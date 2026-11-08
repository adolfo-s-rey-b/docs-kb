[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.filled.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.filled[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.filled.html#numpy-ma-masked-array-filled "Link to this heading")

=========================================================================================================================================================================

method

ma.masked\_array.filled(_fill\_value\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L3857-L3936)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.filled.html#numpy.ma.masked_array.filled "Link to this definition")

Return a copy of self, with masked values filled with a given value. **However**, if there are no masked values to fill, self will be returned instead as an ndarray.

Parameters:

**fill\_value**array\_like, optional

The value to use for invalid entries. Can be scalar or non-scalar. If non-scalar, the resulting ndarray must be broadcastable over input array. Default is None, in which case, the [`fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill_value.html#numpy.ma.masked_array.fill_value "numpy.ma.masked_array.fill_value")
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

Subclassing is preserved. This means that if, e.g., the data part of the masked array is a recarray, [`filled`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.filled.html#numpy.ma.masked_array.filled "numpy.ma.masked_array.filled")
 returns a recarray:

\>>> x \= np.array(\[(\-1, 2), (\-3, 4)\], dtype\='i8,i8').view(np.recarray)
\>>> m \= np.ma.array(x, mask\=\[(True, False), (False, True)\])
\>>> m.filled()
rec.array(\[(999999,      2), (    -3, 999999)\],
          dtype=\[('f0', '<i8'), ('f1', '<i8')\])

Copy to clipboard

Go BackOpen In Tab

On this page