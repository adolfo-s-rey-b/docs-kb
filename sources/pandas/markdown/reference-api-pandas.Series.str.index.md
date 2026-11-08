[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.index[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.index.html#pandas-series-str-index "Link to this heading")

=====================================================================================================================================================

Series.str.index(_sub_, _start\=0_, _end\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L3762-L3817)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.index.html#pandas.Series.str.index "Link to this definition")

Return lowest indexes in each string in Series/Index.

Each of the returned indexes corresponds to the position where the substring is fully contained between \[start:end\]. This is the same as `str.find` except instead of returning -1, it raises a ValueError when the substring is not found. Equivalent to standard `str.index`.

Parameters:

**sub**str

Substring being searched.

**start**int

Left edge index.

**end**int

Right edge index.

Returns:

Series or Index of object

Returns a Series or an Index of the lowest indexes in each string of the input.

See also

[`rindex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rindex.html#pandas.Series.str.rindex "pandas.Series.str.rindex")

Return highest indexes in each strings.

Examples

For Series.str.index:

\>>> ser \= pd.Series(\["horse", "eagle", "donkey"\])
\>>> ser.str.index("e")
0   4
1   0
2   4
dtype: int64

Copy to clipboard

For Series.str.rindex:

\>>> ser \= pd.Series(\["Deer", "eagle", "Sheep"\])
\>>> ser.str.rindex("e")
0   2
1   4
2   3
dtype: int64

Copy to clipboard

On this page