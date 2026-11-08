[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.infer_objects.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Index.infer_objects.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Index.infer_objects.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Index.infer_objects.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Index.infer_objects.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Index.infer_objects.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Index.infer_objects.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Index.infer_objects.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Index.infer_objects.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Index.infer_objects.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Index.infer_objects.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Index.infer_objects.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Index.infer_objects.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Index.infer_objects.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.infer\_objects[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.infer_objects.html#pandas-index-infer-objects "Link to this heading")

===============================================================================================================================================================

final Index.infer\_objects(_copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L7630-L7680)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.infer_objects.html#pandas.Index.infer_objects "Link to this definition")

If we have an object dtype, try to infer a non-object dtype.

For an Index with `object` dtype, this attempts to determine a more specific dtype (e.g., `int64` or `float64`) from the values.

Parameters:

**copy**bool, default True

Whether to make a copy in cases where no inference occurs.

Returns:

Index

An Index with a new dtype if the dtype was inferred or a shallow copy if the dtype could not be inferred.

See also

[`Index.inferred_type`](https://pandas.pydata.org/docs/reference/api/pandas.Index.inferred_type.html#pandas.Index.inferred_type "pandas.Index.inferred_type")

Return a string of the type inferred from the values.

Examples

\>>> pd.Index(\["a", 1\]).infer\_objects()
Index(\['a', 1\], dtype='object')
\>>> pd.Index(\[1, 2\], dtype\="object").infer\_objects()
Index(\[1, 2\], dtype='int64')

Copy to clipboard

On this page