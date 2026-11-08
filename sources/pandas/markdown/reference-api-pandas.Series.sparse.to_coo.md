[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.to_coo.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sparse.to_coo.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.to_coo.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sparse.to_coo.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sparse.to_coo.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sparse.to_coo.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sparse.to_coo.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sparse.to_coo.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sparse.to_coo.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sparse.to_coo.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sparse.to_coo.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sparse.to_coo.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sparse.to_coo.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sparse.to_coo.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sparse.to\_coo[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.to_coo.html#pandas-series-sparse-to-coo "Link to this heading")

==================================================================================================================================================================

Series.sparse.to\_coo(_row\_levels\=(0,)_, _column\_levels\=(1,)_, _sort\_labels\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/sparse/accessor.py#L158-L250)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.to_coo.html#pandas.Series.sparse.to_coo "Link to this definition")

Create a scipy.sparse.coo\_matrix from a Series with MultiIndex.

Use row\_levels and column\_levels to determine the row and column coordinates respectively. row\_levels and column\_levels are the names (labels) or numbers of the levels. {row\_levels, column\_levels} must be a partition of the MultiIndex level names (or numbers).

Parameters:

**row\_levels**tuple/list

MultiIndex levels to use for row coordinates, specified by name or index.

**column\_levels**tuple/list

MultiIndex levels to use for column coordinates, specified by name or index.

**sort\_labels**bool, default False

Sort the row and column labels before forming the sparse matrix. When row\_levels and/or column\_levels refer to a single level, set to True for a faster execution.

Returns:

**y**scipy.sparse.coo\_matrix

The sparse matrix in coordinate format.

**rows**list (row labels)

Labels corresponding to the row coordinates.

**columns**list (column labels)

Labels corresponding to the column coordinates.

See also

[`Series.sparse.from_coo`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.from_coo.html#pandas.Series.sparse.from_coo "pandas.Series.sparse.from_coo")

Create a Series with sparse values from a scipy.sparse.coo\_matrix.

Examples

\>>> s \= pd.Series(\[3.0, np.nan, 1.0, 3.0, np.nan, np.nan\])
\>>> s.index \= pd.MultiIndex.from\_tuples(
...     \[\
...         (1, 2, "a", 0),\
...         (1, 2, "a", 1),\
...         (1, 1, "b", 0),\
...         (1, 1, "b", 1),\
...         (2, 1, "b", 0),\
...         (2, 1, "b", 1),\
...     \],
...     names\=\["A", "B", "C", "D"\],
... )
\>>> s
A  B  C  D
1  2  a  0    3.0
         1    NaN
   1  b  0    1.0
         1    3.0
2  1  b  0    NaN
         1    NaN
dtype: float64

Copy to clipboard

\>>> ss \= s.astype("Sparse")
\>>> ss
A  B  C  D
1  2  a  0    3.0
         1    NaN
   1  b  0    1.0
         1    3.0
2  1  b  0    NaN
         1    NaN
dtype: Sparse\[float64, nan\]

Copy to clipboard

\>>> A, rows, columns \= ss.sparse.to\_coo(
...     row\_levels\=\["A", "B"\], column\_levels\=\["C", "D"\], sort\_labels\=True
... )
\>>> A
<COOrdinate sparse matrix of dtype 'float64'
    with 3 stored elements and shape (3, 4)>
\>>> A.todense()
matrix(\[\[0., 0., 1., 3.\],\
\[3., 0., 0., 0.\],\
\[0., 0., 0., 0.\]\])

Copy to clipboard

\>>> rows
\[(1, 1), (1, 2), (2, 1)\]
\>>> columns
\[('a', 0), ('a', 1), ('b', 0), ('b', 1)\]

Copy to clipboard

On this page