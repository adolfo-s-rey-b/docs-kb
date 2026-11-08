[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.sparse.from_spmatrix.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sparse.from\_spmatrix[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html#pandas-dataframe-sparse-from-spmatrix "Link to this heading")

================================================================================================================================================================================================

classmethod DataFrame.sparse.from\_spmatrix(_data_, _index\=None_, _columns\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/accessor.py#L316-L379)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html#pandas.DataFrame.sparse.from_spmatrix "Link to this definition")

Create a new DataFrame from a scipy sparse matrix.

This method converts a scipy sparse matrix into a pandas DataFrame with sparse array columns for memory efficiency.

Parameters:

**data**scipy.sparse.spmatrix

Must be convertible to csc format.

**index, columns**Index, optional

Row and column labels to use for the resulting DataFrame. Defaults to a RangeIndex.

Returns:

DataFrame

Each column of the DataFrame is stored as a [`arrays.SparseArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html#pandas.arrays.SparseArray "pandas.arrays.SparseArray")
.

See also

[`DataFrame.sparse.to_coo`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_coo.html#pandas.DataFrame.sparse.to_coo "pandas.DataFrame.sparse.to_coo")

Return the contents of the frame as a sparse SciPy COO matrix.

Examples

\>>> import scipy.sparse
\>>> mat \= scipy.sparse.eye(3, dtype\=float)
\>>> pd.DataFrame.sparse.from\_spmatrix(mat)
     0    1    2
0  1.0  0.0  0.0
1  0.0  1.0  0.0
2  0.0  0.0  1.0

Copy to clipboard

On this page