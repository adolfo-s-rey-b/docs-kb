[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.keys.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.keys.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.keys.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.keys.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.keys.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.keys.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.keys.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.keys.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.keys.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.keys.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.keys.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.keys.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.keys.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.keys.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.keys[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.keys.html#pandas-dataframe-keys "Link to this heading")

===============================================================================================================================================

DataFrame.keys()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L1853-L1882)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.keys.html#pandas.DataFrame.keys "Link to this definition")

Get the ‘info axis’ (see Indexing for more).

This is index for Series, columns for DataFrame.

Returns:

Index

Info axis.

See also

[`DataFrame.index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "pandas.DataFrame.index")

The index (row labels) of the DataFrame.

[`DataFrame.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "pandas.DataFrame.columns")

The column labels of the DataFrame.

Examples

\>>> d \= pd.DataFrame(
...     data\={"A": \[1, 2, 3\], "B": \[0, 4, 8\]}, index\=\["a", "b", "c"\]
... )
\>>> d
   A  B
a  1  0
b  2  4
c  3  8
\>>> d.keys()
Index(\['A', 'B'\], dtype='str')

Copy to clipboard

On this page