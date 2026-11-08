[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.T.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.T.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.T.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.T.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.T.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.T.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.T.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.T.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.T.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.T.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.T.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.T.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.T[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html#pandas-dataframe-t "Link to this heading")

======================================================================================================================================

property DataFrame.T[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L4204-L4234)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html#pandas.DataFrame.T "Link to this definition")

The transpose of the DataFrame.

This property returns a DataFrame with rows and columns interchanged, reflecting the data across the main diagonal.

Returns:

DataFrame

The transposed DataFrame.

See also

[`DataFrame.transpose`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose "pandas.DataFrame.transpose")

Transpose index and columns.

Examples

\>>> df \= pd.DataFrame({"col1": \[1, 2\], "col2": \[3, 4\]})
\>>> df
   col1  col2
0     1     3
1     2     4

Copy to clipboard

\>>> df.T
      0  1
col1  1  2
col2  3  4

Copy to clipboard

On this page