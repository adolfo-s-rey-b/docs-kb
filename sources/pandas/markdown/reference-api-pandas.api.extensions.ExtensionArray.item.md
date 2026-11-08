[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.item.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.item[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.item.html#pandas-api-extensions-extensionarray-item "Link to this heading")

===========================================================================================================================================================================================================

ExtensionArray.item(_index\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L634-L685)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.item.html#pandas.api.extensions.ExtensionArray.item "Link to this definition")

Return the array element at the specified position as a Python scalar.

Analogous to [`numpy.ndarray.item()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "(in NumPy v2.5)")
, this converts a single element to a native Python object.

Parameters:

**index**int, optional

Position of the element. If not provided, the array must contain exactly one element.

Returns:

scalar

The element at the specified position.

Raises:

ValueError

If no index is provided and the array does not have exactly one element.

IndexError

If the specified position is out of bounds.

See also

[`numpy.ndarray.item`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "(in NumPy v2.5)")

Return the item of an array as a scalar.

Examples

\>>> arr \= pd.array(\[1\], dtype\="Int64")
\>>> arr.item()
np.int64(1)

Copy to clipboard

\>>> arr \= pd.array(\[1, 2, 3\], dtype\="Int64")
\>>> arr.item(0)
np.int64(1)
\>>> arr.item(2)
np.int64(3)

Copy to clipboard

On this page