[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rowcols.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.mask\_rowcols[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rowcols.html#numpy-ma-mask-rowcols "Link to this heading")

====================================================================================================================================================

ma.mask\_rowcols(_a_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L1035-L1121)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rowcols.html#numpy.ma.mask_rowcols "Link to this definition")

Mask rows and/or columns of a 2D array that contain masked values.

Mask whole rows and/or columns of a 2D array that contain masked values. The masking behavior is selected using the _axis_ parameter.

> *   If _axis_ is None, rows _and_ columns are masked.
>     
> *   If _axis_ is 0, only rows are masked.
>     
> *   If _axis_ is 1 or -1, only columns are masked.
>     

Parameters:

**a**array\_like, MaskedArray

The array to mask. If not a MaskedArray instance (or if no array elements are masked), the result is a MaskedArray with _mask_ set to [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 (False). Must be a 2D array.

**axis**int, optional

Axis along which to perform the operation. If None, applies to a flattened version of the array.

Returns:

**a**MaskedArray

A modified version of the input array, masked depending on the value of the _axis_ parameter.

Raises:

NotImplementedError

If input array _a_ is not 2D.

See also

[`mask_rows`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_rows.html#numpy.ma.mask_rows "numpy.ma.mask_rows")

Mask rows of a 2D array that contain masked values.

[`mask_cols`](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_cols.html#numpy.ma.mask_cols "numpy.ma.mask_cols")

Mask cols of a 2D array that contain masked values.

[`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")

Mask where a condition is met.

Notes

The input array’s mask is modified by this function.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.zeros((3, 3), dtype\=np.int\_)
\>>> a\[1, 1\] \= 1
\>>> a
array(\[\[0, 0, 0\],\
       \[0, 1, 0\],\
       \[0, 0, 0\]\])
\>>> a \= np.ma.masked\_equal(a, 1)
\>>> a
masked\_array(
  data=\[\[0, 0, 0\],\
        \[0, --, 0\],\
        \[0, 0, 0\]\],
  mask=\[\[False, False, False\],\
        \[False,  True, False\],\
        \[False, False, False\]\],
  fill\_value=1)
\>>> np.ma.mask\_rowcols(a)
masked\_array(
  data=\[\[0, --, 0\],\
        \[--, --, --\],\
        \[0, --, 0\]\],
  mask=\[\[False,  True, False\],\
        \[ True,  True,  True\],\
        \[False,  True, False\]\],
  fill\_value=1)

Copy to clipboard

Go BackOpen In Tab

On this page