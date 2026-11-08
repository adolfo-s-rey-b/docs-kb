[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.density.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sparse.density.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.density.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sparse.density.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sparse.density.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sparse.density.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sparse.density.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sparse.density.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sparse.density.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sparse.density.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sparse.density.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sparse.density.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sparse.density.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sparse.density.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sparse.density[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.density.html#pandas-series-sparse-density "Link to this heading")

====================================================================================================================================================================

Series.sparse.density[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.density.html#pandas.Series.sparse.density "Link to this definition")

The percent of non- `fill_value` points, as decimal.

This is calculated as the number of non-fill-value points divided by the total length of the array. A density of 1.0 means no values are the fill value, while 0.0 means all values are the fill value. An empty array has no density and returns `nan`.

See also

[`DataFrame.sparse.from_spmatrix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html#pandas.DataFrame.sparse.from_spmatrix "pandas.DataFrame.sparse.from_spmatrix")

Create a new DataFrame from a scipy sparse matrix.

Examples

\>>> from pandas.arrays import SparseArray
\>>> s \= SparseArray(\[0, 0, 1, 1, 1\], fill\_value\=0)
\>>> s.density
0.6

Copy to clipboard

On this page