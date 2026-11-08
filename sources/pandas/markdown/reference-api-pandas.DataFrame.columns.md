[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.columns[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas-dataframe-columns "Link to this heading")

========================================================================================================================================================

DataFrame.columns[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "Link to this definition")

The column labels of the DataFrame.

This property holds the column names as a pandas `Index` object. It provides an immutable sequence of column labels that can be used for data selection, renaming, and alignment in DataFrame operations.

Returns:

pandas.Index

The column labels of the DataFrame.

See also

[`DataFrame.index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "pandas.DataFrame.index")

The index (row labels) of the DataFrame.

[`DataFrame.axes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.axes.html#pandas.DataFrame.axes "pandas.DataFrame.axes")

Return a list representing the axes of the DataFrame.

Examples

\>>> df \= pd.DataFrame({'A': \[1, 2\], 'B': \[3, 4\]})
\>>> df
        A  B
0    1  3
1    2  4
\>>> df.columns
Index(\['A', 'B'\], dtype='str')

Copy to clipboard

On this page