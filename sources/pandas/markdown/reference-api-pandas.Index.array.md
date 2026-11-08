[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.array.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.array.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.array.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.array.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.array.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.array.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.array.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.array.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.array.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.array.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.array.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.array.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.array[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas-index-array "Link to this heading")

======================================================================================================================================

Index.array[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L5284-L5366)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas.Index.array "Link to this definition")

The ExtensionArray of the data backing this Index.

This property provides direct access to the underlying array data of an Index without requiring conversion to a NumPy array. It returns an ExtensionArray, which is the native storage format for pandas extension dtypes.

Changed in version 3.1.0: The returned array is read-only, since an Index is immutable.

Returns:

ExtensionArray

An ExtensionArray of the values stored within. For extension types, this is the actual array. For NumPy native types, this is a thin (no copy) wrapper around [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
.

`.array` differs from `.values`, which may require converting the data to a different form.

See also

[`Index.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_numpy.html#pandas.Index.to_numpy "pandas.Index.to_numpy")

Similar method that always returns a NumPy array.

[`Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")

Similar method that always returns a NumPy array.

Notes

This table lays out the different array types for each extension dtype within pandas.

| dtype | array type |
| --- | --- |
| category | Categorical |
| period | PeriodArray |
| interval | IntervalArray |
| IntegerNA | IntegerArray |
| string | StringArray |
| boolean | BooleanArray |
| datetime64\[ns, tz\] | DatetimeArray |

For any 3rd-party extension types, the array type will be an ExtensionArray.

For all remaining dtypes `.array` will be a [`arrays.NumpyExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.NumpyExtensionArray.html#pandas.arrays.NumpyExtensionArray "pandas.arrays.NumpyExtensionArray")
 wrapping the actual ndarray stored within. If you absolutely need a NumPy array (possibly with copying / coercing data), then use [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
 instead.

Examples

For regular NumPy types like int, and float, a NumpyExtensionArray is returned.

\>>> pd.Index(\[1, 2, 3\]).array
<NumpyExtensionArray>
\[1, 2, 3\]
Length: 3, dtype: int64

Copy to clipboard

For extension types, like Categorical, the actual ExtensionArray is returned

\>>> idx \= pd.Index(pd.Categorical(\["a", "b", "a"\]))
\>>> idx.array
\['a', 'b', 'a'\]
Categories (2, str): \['a', 'b'\]

Copy to clipboard

On this page