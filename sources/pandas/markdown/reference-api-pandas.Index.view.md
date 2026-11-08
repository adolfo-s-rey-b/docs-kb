[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.view.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.view.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.view.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.view.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.view.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.view.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.view.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.view.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.view.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.view.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.view.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.view.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.view.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.view.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.view[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.view.html#pandas-index-view "Link to this heading")

===================================================================================================================================

Index.view(_cls\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1071-L1147)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.view.html#pandas.Index.view "Link to this definition")

Return a view of the Index with the specified dtype or a new Index instance.

This method returns a view of the calling Index object if no arguments are provided. If a dtype is specified through the cls argument, it attempts to return a view of the Index with the specified dtype. Note that viewing the Index as a different dtype reinterprets the underlying data, which can lead to unexpected results for non-numeric or incompatible dtype conversions.

Parameters:

**cls**data-type or ndarray sub-class, optional

Data-type descriptor of the returned view, e.g., float32 or int16. Omitting it results in the view having the same data-type as self. This argument can also be specified as an ndarray sub-class, e.g., np.int64 or np.float32 which then specifies the type of the returned object.

Returns:

Index or ndarray

A view of the Index. If cls is None, the returned object is an Index view with the same dtype as the calling object. If a numeric cls is specified an ndarray view with the new dtype is returned.

Raises:

ValueError

If attempting to change to a dtype in a way that is not compatible with the original dtype’s memory layout, for example, viewing an ‘int64’ Index as ‘str’.

See also

[`Index.copy`](https://pandas.pydata.org/docs/reference/api/pandas.Index.copy.html#pandas.Index.copy "pandas.Index.copy")

Returns a copy of the Index.

[`numpy.ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "(in NumPy v2.5)")

Returns a new view of array with the same data.

Examples

\>>> idx \= pd.Index(\[\-1, 0, 1\])
\>>> idx.view()
Index(\[-1, 0, 1\], dtype='int64')

Copy to clipboard

\>>> idx.view(np.uint64)
array(\[18446744073709551615,                    0,                    1\],
  dtype=uint64)

Copy to clipboard

Viewing as ‘int32’ or ‘float32’ reinterprets the memory, which may lead to unexpected behavior:

\>>> idx.view("float32")
array(\[   nan,    nan, 0.e+00, 0.e+00, 1.e-45, 0.e+00\], dtype=float32)

Copy to clipboard

On this page