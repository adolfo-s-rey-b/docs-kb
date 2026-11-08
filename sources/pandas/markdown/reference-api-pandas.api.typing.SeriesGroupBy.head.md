[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.head.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.head.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.head.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.head[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.head.html#pandas-api-typing-seriesgroupby-head "Link to this heading")

============================================================================================================================================================================================

SeriesGroupBy.head(_n\=5_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L5480-L5518)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.head.html#pandas.api.typing.SeriesGroupBy.head "Link to this definition")

Return first n rows of each group.

Similar to `.apply(lambda x: x.head(n))`, but it returns a subset of rows from the original DataFrame with original index and order preserved (`as_index` flag is ignored).

Parameters:

**n**int

If positive: number of entries to include from start of each group. If negative: number of entries to exclude from end of each group.

Returns:

Series or DataFrame

Subset of original Series or DataFrame as determined by n.

See also

`Series.head`

Apply function head to a Series.

`DataFrame.head`

Apply function head to each row or column of a DataFrame.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[1, 4\], \[5, 6\]\], columns\=\["A", "B"\])
\>>> df.groupby("A").head(1)
   A  B
0  1  2
2  5  6
\>>> df.groupby("A").head(\-1)
   A  B
0  1  2

Copy to clipboard

On this page