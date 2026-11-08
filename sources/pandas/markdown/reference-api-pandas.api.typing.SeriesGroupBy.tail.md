[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.tail.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.tail.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.tail[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.tail.html#pandas-api-typing-seriesgroupby-tail "Link to this heading")

============================================================================================================================================================================================

SeriesGroupBy.tail(_n\=5_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L5520-L5565)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.tail.html#pandas.api.typing.SeriesGroupBy.tail "Link to this definition")

Return last n rows of each group.

Similar to `.apply(lambda x: x.tail(n))`, but it returns a subset of rows from the original DataFrame with original index and order preserved (`as_index` flag is ignored).

Parameters:

**n**int

If positive: number of entries to include from end of each group. If negative: number of entries to exclude from start of each group.

Returns:

Series or DataFrame

Subset of original Series or DataFrame as determined by n.

See also

`Series.tail`

Apply function tail to a Series.

`DataFrame.tail`

Apply function tail to each row or column of a DataFrame.

Examples

\>>> df \= pd.DataFrame(
...     \[\["a", 1\], \["a", 2\], \["b", 1\], \["b", 2\]\], columns\=\["A", "B"\]
... )
\>>> df.groupby("A").tail(1)
   A  B
1  a  2
3  b  2
\>>> df.groupby("A").tail(\-1)
   A  B
1  a  2
3  b  2

Copy to clipboard

On this page