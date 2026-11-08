[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sparse.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sparse.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sparse.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sparse.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sparse.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sparse.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sparse.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sparse.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sparse.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sparse.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sparse.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sparse.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sparse[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.html#pandas-series-sparse "Link to this heading")

============================================================================================================================================

Series.sparse()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/accessor.py#L46-L283)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.html#pandas.Series.sparse "Link to this definition")

Accessor for SparseArray from other sparse matrix data types.

Provides methods and properties to work with the underlying sparse data in a Series or DataFrame. It allows accessing sparse-specific attributes such as fill value, density, and stored non-fill values, as well as converting to and from scipy sparse matrices.

Parameters:

**data**Series or DataFrame

The Series or DataFrame to which the SparseAccessor is attached.

See also

[`Series.sparse.to_coo`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.to_coo.html#pandas.Series.sparse.to_coo "pandas.Series.sparse.to_coo")

Create a scipy.sparse.coo\_matrix from a Series with MultiIndex.

[`Series.sparse.from_coo`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.from_coo.html#pandas.Series.sparse.from_coo "pandas.Series.sparse.from_coo")

Create a Series with sparse values from a scipy.sparse.coo\_matrix.

Examples

\>>> ser \= pd.Series(\[0, 0, 2, 2, 2\], dtype\="Sparse\[int\]")
\>>> ser.sparse.density
0.6
\>>> ser.sparse.sp\_values
array(\[2, 2, 2\])

Copy to clipboard

On this page