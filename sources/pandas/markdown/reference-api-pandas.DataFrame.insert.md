[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.insert.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.insert.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.insert.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.insert.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.insert.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.insert.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.insert.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.insert.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.insert.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.insert.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.insert.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.insert.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.insert[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas-dataframe-insert "Link to this heading")

=====================================================================================================================================================

DataFrame.insert(_loc_, _column_, _value_, _allow\_duplicates\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L6186-L6271)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert "Link to this definition")

Insert column into DataFrame at specified location.

Raises a ValueError if column is already contained in the DataFrame, unless allow\_duplicates is set to True.

Parameters:

**loc**int

Insertion index. Must verify 0 <= loc <= len(columns).

**column**str, number, or hashable object

Label of the inserted column.

**value**Scalar, Series, or array-like

Content of the inserted column.

**allow\_duplicates**bool, default False

Allow duplicate column labels to be created.

See also

[`Index.insert`](https://pandas.pydata.org/docs/reference/api/pandas.Index.insert.html#pandas.Index.insert "pandas.Index.insert")

Insert new item by index.

Examples

\>>> df \= pd.DataFrame({"col1": \[1, 2\], "col2": \[3, 4\]})
\>>> df
   col1  col2
0     1     3
1     2     4
\>>> df.insert(1, "newcol", \[99, 99\])
\>>> df
   col1  newcol  col2
0     1      99     3
1     2      99     4
\>>> df.insert(0, "col1", \[100, 100\], allow\_duplicates\=True)
\>>> df
   col1  col1  newcol  col2
0   100     1      99     3
1   100     2      99     4

Copy to clipboard

Notice that pandas uses index alignment in case of value from type Series:

\>>> df.insert(0, "col0", pd.Series(\[5, 6\], index\=\[1, 2\]))
\>>> df
   col0  col1  col1  newcol  col2
0   NaN   100     1      99     3
1   5.0   100     2      99     4

Copy to clipboard

On this page