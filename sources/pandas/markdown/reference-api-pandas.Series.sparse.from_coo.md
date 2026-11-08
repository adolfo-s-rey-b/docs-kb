[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.from_coo.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sparse.from_coo.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.from_coo.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sparse.from_coo.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sparse.from_coo.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sparse.from_coo.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sparse.from_coo.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sparse.from_coo.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sparse.from_coo.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sparse.from_coo.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sparse.from_coo.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sparse.from_coo.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sparse.from_coo.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sparse.from_coo.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sparse.from\_coo[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.from_coo.html#pandas-series-sparse-from-coo "Link to this heading")

========================================================================================================================================================================

classmethod Series.sparse.from\_coo(_A_, _dense\_index\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/accessor.py#L94-L156)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.from_coo.html#pandas.Series.sparse.from_coo "Link to this definition")

Create a Series with sparse values from a scipy.sparse.coo\_matrix.

This method takes a `scipy.sparse.coo_matrix` (coordinate format) as input and returns a pandas `Series` where the non-zero elements are represented as sparse values. The index of the Series can either include only the coordinates of non-zero elements (default behavior) or the full sorted set of coordinates from the matrix if `dense_index` is set to True.

Parameters:

**A**scipy.sparse.coo\_matrix

The sparse matrix in coordinate format from which the sparse Series will be created.

**dense\_index**bool, default False

If False (default), the index consists of only the coords of the non-null entries of the original coo\_matrix. If True, the index consists of the full sorted (row, col) coordinates of the coo\_matrix.

Returns:

**s**Series

A Series with sparse values.

See also

[`DataFrame.sparse.from_spmatrix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html#pandas.DataFrame.sparse.from_spmatrix "pandas.DataFrame.sparse.from_spmatrix")

Create a new DataFrame from a scipy sparse matrix.

`scipy.sparse.coo_matrix`

A sparse matrix in COOrdinate format.

Examples

\>>> from scipy import sparse

Copy to clipboard

\>>> A \= sparse.coo\_matrix(
...     (\[3.0, 1.0, 2.0\], (\[1, 0, 0\], \[0, 2, 3\])), shape\=(3, 4)
... )
\>>> A
<COOrdinate sparse matrix of dtype 'float64'
    with 3 stored elements and shape (3, 4)>

Copy to clipboard

\>>> A.todense()
matrix(\[\[0., 0., 1., 2.\],\
\[3., 0., 0., 0.\],\
\[0., 0., 0., 0.\]\])

Copy to clipboard

\>>> ss \= pd.Series.sparse.from\_coo(A)
\>>> ss
0  2    1.0
   3    2.0
1  0    3.0
dtype: Sparse\[float64, nan\]

Copy to clipboard

On this page