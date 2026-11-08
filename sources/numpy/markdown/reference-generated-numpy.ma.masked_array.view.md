[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.view.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.view[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.view.html#numpy-ma-masked-array-view "Link to this heading")

===================================================================================================================================================================

method

ma.masked\_array.view(_dtype\=None_, _type\=None_, _fill\_value\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L3203-L3275)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.view.html#numpy.ma.masked_array.view "Link to this definition")

Return a view of the MaskedArray data.

Parameters:

**dtype**data-type or ndarray sub-class, optional

Data-type descriptor of the returned view, e.g., float32 or int16. The default, None, results in the view having the same data-type as _a_. As with `ndarray.view`, dtype can also be specified as an ndarray sub-class, which then specifies the type of the returned object (this is equivalent to setting the `type` parameter).

**type**Python type, optional

Type of the returned view, either ndarray or a subclass. The default None results in type preservation.

**fill\_value**scalar, optional

The value to use for invalid entries (None by default). If None, then this argument is inferred from the passed [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, or in its absence the original array, as discussed in the notes below.

See also

[`numpy.ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")

Equivalent method on ndarray object.

Notes

`a.view()` is used two different ways:

`a.view(some_dtype)` or `a.view(dtype=some_dtype)` constructs a view of the array’s memory with a different data-type. This can cause a reinterpretation of the bytes of memory.

`a.view(ndarray_subclass)` or `a.view(type=ndarray_subclass)` just returns an instance of _ndarray\_subclass_ that looks at the same array (same shape, dtype, etc.) This does not cause a reinterpretation of the memory.

If [`fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill_value.html#numpy.ma.masked_array.fill_value "numpy.ma.masked_array.fill_value")
 is not specified, but [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is specified (and is not an ndarray sub-class), the [`fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill_value.html#numpy.ma.masked_array.fill_value "numpy.ma.masked_array.fill_value")
 of the MaskedArray will be reset. If neither [`fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill_value.html#numpy.ma.masked_array.fill_value "numpy.ma.masked_array.fill_value")
 nor [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 are specified (or if [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is an ndarray sub-class), then the fill value is preserved. Finally, if [`fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill_value.html#numpy.ma.masked_array.fill_value "numpy.ma.masked_array.fill_value")
 is specified, but [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is not, the fill value is set to the specified value.

For `a.view(some_dtype)`, if `some_dtype` has a different number of bytes per entry than the previous dtype (for example, converting a regular array to a structured array), then the behavior of the view cannot be predicted just from the superficial appearance of `a` (shown by `print(a)`). It also depends on exactly how `a` is stored in memory. Therefore if `a` is C-ordered versus fortran-ordered, versus defined as a slice or transpose, etc., the view may give different results.

On this page