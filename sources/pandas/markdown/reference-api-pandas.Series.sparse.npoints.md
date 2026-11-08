[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.npoints.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sparse.npoints.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.npoints.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sparse.npoints.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sparse.npoints.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sparse.npoints.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sparse.npoints.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sparse.npoints.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sparse.npoints.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sparse.npoints.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sparse.npoints.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sparse.npoints.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sparse.npoints.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sparse.npoints.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sparse.npoints[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.npoints.html#pandas-series-sparse-npoints "Link to this heading")

====================================================================================================================================================================

Series.sparse.npoints[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.npoints.html#pandas.Series.sparse.npoints "Link to this definition")

The number of non- `fill_value` points.

This property returns the number of elements in the sparse series that are not equal to the `fill_value`. Sparse data structures store only the non-`fill_value` elements, reducing memory usage when the majority of values are the same.

See also

`Series.sparse.to_dense`

Convert a Series from sparse values to dense.

[`Series.sparse.fill_value`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.fill_value.html#pandas.Series.sparse.fill_value "pandas.Series.sparse.fill_value")

Elements in `data` that are `fill_value` are not stored.

[`Series.sparse.density`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.density.html#pandas.Series.sparse.density "pandas.Series.sparse.density")

The percent of non- `fill_value` points, as decimal.

Examples

\>>> from pandas.arrays import SparseArray
\>>> s \= SparseArray(\[0, 0, 1, 1, 1\], fill\_value\=0)
\>>> s.npoints
3

Copy to clipboard

On this page