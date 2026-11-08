[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.density.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.sparse.density.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.density.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.sparse.density.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.sparse.density.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.sparse.density.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.sparse.density.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.sparse.density.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.sparse.density.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.sparse.density.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.sparse.density.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.sparse.density.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.sparse.density.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.sparse.density.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sparse.density[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.density.html#pandas-dataframe-sparse-density "Link to this heading")

=============================================================================================================================================================================

DataFrame.sparse.density[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/accessor.py#L475-L498)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.density.html#pandas.DataFrame.sparse.density "Link to this definition")

Ratio of non-sparse points to total (dense) data points.

This property returns the proportion of the data that is not sparse (i.e., not equal to the fill value), as a value between 0 and 1. An empty DataFrame has no density and returns `nan`.

See also

[`DataFrame.sparse.from_spmatrix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html#pandas.DataFrame.sparse.from_spmatrix "pandas.DataFrame.sparse.from_spmatrix")

Create a new DataFrame from a scipy sparse matrix.

Examples

\>>> df \= pd.DataFrame({"A": pd.arrays.SparseArray(\[0, 1, 0, 1\])})
\>>> df.sparse.density
np.float64(0.5)

Copy to clipboard

On this page