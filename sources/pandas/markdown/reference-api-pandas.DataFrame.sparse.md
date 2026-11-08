[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.sparse.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.sparse.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.sparse.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.sparse.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.sparse.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.sparse.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.sparse.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.sparse.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.sparse.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.sparse.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.sparse.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.sparse.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sparse[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.html#pandas-dataframe-sparse "Link to this heading")

=====================================================================================================================================================

DataFrame.sparse()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/accessor.py#L286-L521)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.html#pandas.DataFrame.sparse "Link to this definition")

DataFrame accessor for sparse data.

It allows users to interact with a DataFrame that contains sparse data types (SparseDtype). It provides methods and attributes to efficiently work with sparse storage, reducing memory usage while maintaining compatibility with standard pandas operations.

Parameters:

**data**scipy.sparse.spmatrix

Must be convertible to csc format.

See also

[`DataFrame.sparse.density`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.density.html#pandas.DataFrame.sparse.density "pandas.DataFrame.sparse.density")

Ratio of non-sparse points to total (dense) data points.

Examples

\>>> df \= pd.DataFrame({"a": \[1, 2, 0, 0\], "b": \[3, 0, 0, 4\]}, dtype\="Sparse\[int\]")
\>>> df.sparse.density
np.float64(0.5)

Copy to clipboard

On this page