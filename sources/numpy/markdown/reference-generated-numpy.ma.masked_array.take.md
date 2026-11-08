[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.take.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.take.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.take.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.take.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.take.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.take.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.take.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.take.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.take.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.take.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.take.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.take.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.take.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.take.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.take.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.take.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.take.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.take.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.take.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.take.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.take.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.take.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.take[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.take.html#numpy-ma-masked-array-take "Link to this heading")

===================================================================================================================================================================

method

ma.masked\_array.take(_indices_, _axis\=None_, _out\=None_, _mode\='raise'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L6180-L6269)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.take.html#numpy.ma.masked_array.take "Link to this definition")

Take elements from a masked array along an axis.

This function does the same thing as “fancy” indexing (indexing arrays using arrays) for masked arrays. It can be easier to use if you need elements along a given axis.

Parameters:

**a**masked\_array

The source masked array.

**indices**array\_like

The indices of the values to extract. Also allow scalars for indices.

**axis**int, optional

The axis over which to select values. By default, the flattened input array is used.

**out**MaskedArray, optional

If provided, the result will be placed in this array. It should be of the appropriate shape and dtype. Note that _out_ is always buffered if _mode=’raise’_; use other modes for better performance.

**mode**{‘raise’, ‘wrap’, ‘clip’}, optional

Specifies how out-of-bounds indices will behave.

*   ‘raise’ – raise an error (default)
    
*   ‘wrap’ – wrap around
    
*   ‘clip’ – clip to the range
    

‘clip’ mode means that all indices that are too large are replaced by the index that addresses the last element along that axis. Note that this disables indexing with negative numbers.

Returns:

**out**MaskedArray

The returned array has the same type as _a_.

See also

[`numpy.take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")

Equivalent function for ndarrays.

[`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress")

Take elements using a boolean mask.

[`take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis")

Take elements by matching the array and the index arrays.

Notes

This function behaves similarly to [`numpy.take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take")
, but it handles masked values. The mask is retained in the output array, and masked values in the input array remain masked in the output.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[4, 3, 5, 7, 6, 8\], mask\=\[0, 0, 1, 0, 1, 0\])
\>>> indices \= \[0, 1, 4\]
\>>> np.ma.take(a, indices)
masked\_array(data=\[4, 3, --\],
            mask=\[False, False,  True\],
    fill\_value=999999)

Copy to clipboard

When [`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
 is not one-dimensional, the output also has these dimensions:

\>>> np.ma.take(a, \[\[0, 1\], \[2, 3\]\])
masked\_array(data=\[\[4, 3\],\
                \[--, 7\]\],
            mask=\[\[False, False\],\
                \[ True, False\]\],
    fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page