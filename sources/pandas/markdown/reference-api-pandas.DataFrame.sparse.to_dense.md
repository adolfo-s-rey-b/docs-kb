[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_dense.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sparse.to\_dense[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_dense.html#pandas-dataframe-sparse-to-dense "Link to this heading")

=================================================================================================================================================================================

DataFrame.sparse.to\_dense()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/accessor.py#L381-L410)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_dense.html#pandas.DataFrame.sparse.to_dense "Link to this definition")

Convert a DataFrame with sparse values to dense.

This method converts all SparseArray columns in the DataFrame to regular NumPy arrays.

Returns:

DataFrame

A DataFrame with the same values stored as dense arrays.

See also

[`DataFrame.sparse.density`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.density.html#pandas.DataFrame.sparse.density "pandas.DataFrame.sparse.density")

Ratio of non-sparse points to total (dense) data points.

Examples

\>>> df \= pd.DataFrame({"A": pd.arrays.SparseArray(\[0, 1, 0\])})
\>>> df.sparse.to\_dense()
   A
0  0
1  1
2  0

Copy to clipboard

On this page