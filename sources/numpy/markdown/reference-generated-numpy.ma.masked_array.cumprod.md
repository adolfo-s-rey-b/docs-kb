[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.cumprod.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.cumprod[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.cumprod.html#numpy-ma-masked-array-cumprod "Link to this heading")

============================================================================================================================================================================

method

ma.masked\_array.cumprod(_axis\=None_, _dtype\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5345-L5374)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.cumprod.html#numpy.ma.masked_array.cumprod "Link to this definition")

Return the cumulative product of the array elements over the given axis.

Masked values are set to 1 internally during the computation. However, their position is saved, and the result will be masked at the same locations.

Refer to [`numpy.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod")
 for full documentation.

See also

[`numpy.ndarray.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumprod.html#numpy.ndarray.cumprod "numpy.ndarray.cumprod")

corresponding function for ndarrays

[`numpy.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod")

equivalent function

Notes

The mask is lost if _out_ is not a valid MaskedArray !

Arithmetic is modular when using integer types, and no error is raised on overflow.

On this page