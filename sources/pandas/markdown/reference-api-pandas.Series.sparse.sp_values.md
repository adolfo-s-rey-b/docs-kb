[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.sp_values.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sparse.sp\_values[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.sp_values.html#pandas-series-sparse-sp-values "Link to this heading")

===========================================================================================================================================================================

Series.sparse.sp\_values[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.sp_values.html#pandas.Series.sparse.sp_values "Link to this definition")

An ndarray containing the non- `fill_value` values.

This property returns the actual data values stored in the sparse representation, excluding the values that are equal to the `fill_value`. The result is an ndarray of the underlying values, preserving the sparse structure by omitting the default `fill_value` entries.

See also

`Series.sparse.to_dense`

Convert a Series from sparse values to dense.

[`Series.sparse.fill_value`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.fill_value.html#pandas.Series.sparse.fill_value "pandas.Series.sparse.fill_value")

Elements in data that are fill\_value are not stored.

[`Series.sparse.density`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.density.html#pandas.Series.sparse.density "pandas.Series.sparse.density")

The percent of non- `fill_value` points, as decimal.

Examples

\>>> from pandas.arrays import SparseArray
\>>> s \= SparseArray(\[0, 0, 1, 0, 2\], fill\_value\=0)
\>>> s.sp\_values
array(\[1, 2\])

Copy to clipboard

On this page