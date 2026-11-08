[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.take.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.take.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.take.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.take[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.take.html#pandas-api-extensions-extensionarray-take "Link to this heading")

===========================================================================================================================================================================================================

ExtensionArray.take(_indices_, _\*_, _allow\_fill\=False_, _fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1972-L2074)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.take.html#pandas.api.extensions.ExtensionArray.take "Link to this definition")

Take elements from an array.

This method selects elements from the array at the specified indices, optionally handling negative indices as missing values when `allow_fill=True`.

Parameters:

**indices**sequence of int or one-dimensional np.ndarray of int

Indices to be taken.

**allow\_fill**bool, default False

How to handle negative values in indices.

*   False: negative values in indices indicate positional indices from the right (the default). This is similar to [`numpy.take()`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "(in NumPy v2.5)")
    .
    
*   True: negative values in indices indicate missing values. These values are set to fill\_value. Any other other negative values raise a `ValueError`.
    

**fill\_value**any, optional

Fill value to use for NA-indices when allow\_fill is True. This may be `None`, in which case the default NA value for the type, `self.dtype.na_value`, is used.

For many ExtensionArrays, there will be two representations of fill\_value: a user-facing “boxed” scalar, and a low-level physical NA value. fill\_value should be the user-facing version, and the implementation should handle translating that to the physical version for processing the take if necessary.

Returns:

ExtensionArray

An array formed with selected indices.

Raises:

IndexError

When the indices are out of bounds for the array.

ValueError

When indices contains negative values other than `-1` and allow\_fill is True.

See also

[`numpy.take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "(in NumPy v2.5)")

Take elements from an array along an axis.

`api.extensions.take`

Take elements from an array.

Notes

ExtensionArray.take is called by `Series.__getitem__`, `.loc`, `iloc`, when indices is a sequence of values. Additionally, it’s called by `Series.reindex()`, or any other method that causes realignment, with a fill\_value.

Scalar values for indices are not supported. If needed, use a list-like wrapping a single element (e.g. `[index]`).

Examples

Here’s an example implementation, which relies on casting the extension array to object dtype. This uses the helper method `pandas.api.extensions.take()`.

def take(self, indices, allow\_fill\=False, fill\_value\=None):
    from pandas.api.extensions import take

    \# If the ExtensionArray is backed by an ndarray, then
    \# just pass that here instead of coercing to object.
    data \= self.astype(object)

    if allow\_fill and fill\_value is None:
        fill\_value \= self.dtype.na\_value

    \# fill value should always be translated from the scalar
    \# type for the array, to the physical storage type for
    \# the data, before passing to take.

    result \= take(
        data, indices, fill\_value\=fill\_value, allow\_fill\=allow\_fill
    )
    return self.\_from\_sequence(result, dtype\=self.dtype)

Copy to clipboard

On this page