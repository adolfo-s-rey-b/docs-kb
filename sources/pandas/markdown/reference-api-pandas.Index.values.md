[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.values.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.values.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.values.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.values.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.values.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.values.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.values.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.values.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.values.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.values.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.values.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.values.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.values[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#pandas-index-values "Link to this heading")

=========================================================================================================================================

property Index.values[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L5211-L5282)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#pandas.Index.values "Link to this definition")

Return an array representing the data in the Index.

Warning

We recommend using [`Index.array`](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas.Index.array "pandas.Index.array")
 or [`Index.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_numpy.html#pandas.Index.to_numpy "pandas.Index.to_numpy")
, depending on whether you need a reference to the underlying data or a NumPy array. The return type of `.values` depends on the dtype: it is a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 for some dtypes (for example `int64` or `float64`) and an [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
 for others (for example `interval`, `category`, or nullable `Int64`), which makes it harder to write code that works across dtypes. [`Index.array`](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas.Index.array "pandas.Index.array")
 always returns the underlying array as an [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
, and [`Index.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_numpy.html#pandas.Index.to_numpy "pandas.Index.to_numpy")
 always returns a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 and accepts `dtype`, `copy`, and `na_value` arguments to control the conversion.

Changed in version 3.0.0: The returned array is read-only.

Returns:

array: numpy.ndarray or ExtensionArray

See also

[`Index.array`](https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas.Index.array "pandas.Index.array")

Reference to the underlying data.

[`Index.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_numpy.html#pandas.Index.to_numpy "pandas.Index.to_numpy")

A NumPy array representing the underlying data.

Examples

For an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 backed by a NumPy dtype such as `int64`, `.values` returns a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
:

\>>> idx \= pd.Index(\[1, 2, 3\])
\>>> idx
Index(\[1, 2, 3\], dtype='int64')
\>>> idx.values
array(\[1, 2, 3\])

Copy to clipboard

For an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 backed by an extension dtype such as `interval`, `.values` returns an [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
 instead, while [`Index.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.to_numpy.html#pandas.Index.to_numpy "pandas.Index.to_numpy")
 always returns a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
:

\>>> idx \= pd.interval\_range(start\=0, end\=5)
\>>> idx.values
<IntervalArray>
\[(0, 1\], (1, 2\], (2, 3\], (3, 4\], (4, 5\]\]
Length: 5, dtype: interval\[int64, right\]
\>>> idx.to\_numpy()
array(\[Interval(0, 1, closed='right'), Interval(1, 2, closed='right'),\
       Interval(2, 3, closed='right'), Interval(3, 4, closed='right'),\
       Interval(4, 5, closed='right')\], dtype=object)

Copy to clipboard

On this page