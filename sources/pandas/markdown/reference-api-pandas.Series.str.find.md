[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.find.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.find.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.find.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.find.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.find.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.find.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.find.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.find.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.find.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.find.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.find.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.find.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.find[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html#pandas-series-str-find "Link to this heading")

==================================================================================================================================================

Series.str.find(_sub_, _start\=0_, _end\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3610-L3664)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html#pandas.Series.str.find "Link to this definition")

Return lowest indexes in each strings in the Series/Index.

Each of returned indexes corresponds to the position where the substring is fully contained between \[start:end\]. Return -1 on failure. Equivalent to standard [`str.find()`](https://docs.python.org/3/builtins/stdtypes.html#str.find "(in Python v3.15)")
.

Parameters:

**sub**str

Substring being searched.

**start**int

Left edge index.

**end**int

Right edge index.

Returns:

Series or Index of int.

A Series (if the input is a Series) or an Index (if the input is an Index) of the lowest indexes corresponding to the positions where the substring is found in each string of the input.

See also

[`rfind`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rfind.html#pandas.Series.str.rfind "pandas.Series.str.rfind")

Return highest indexes in each strings.

Examples

For Series.str.find:

\>>> ser \= pd.Series(\["\_cow\_", "duck\_", "do\_v\_e"\])
\>>> ser.str.find("\_")
0   0
1   4
2   2
dtype: int64

Copy to clipboard

For Series.str.rfind:

\>>> ser \= pd.Series(\["\_cow\_", "duck\_", "do\_v\_e"\])
\>>> ser.str.rfind("\_")
0   4
1   4
2   4
dtype: int64

Copy to clipboard

On this page