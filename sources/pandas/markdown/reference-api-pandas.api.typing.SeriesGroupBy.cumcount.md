[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumcount.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.cumcount[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumcount.html#pandas-api-typing-seriesgroupby-cumcount "Link to this heading")

========================================================================================================================================================================================================

SeriesGroupBy.cumcount(_ascending\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L4633-L4688)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumcount.html#pandas.api.typing.SeriesGroupBy.cumcount "Link to this definition")

Number each item in each group from 0 to the length of that group - 1.

Essentially this is equivalent to

self.apply(lambda x: pd.Series(np.arange(len(x)), x.index))

Copy to clipboard

Parameters:

**ascending**bool, default True

If False, number in reverse, from length of group - 1 to 0.

Returns:

Series

Sequence number of each element within each group.

See also

[`ngroup`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ngroup.html#pandas.api.typing.SeriesGroupBy.ngroup "pandas.api.typing.SeriesGroupBy.ngroup")

Number the groups themselves.

Examples

\>>> df \= pd.DataFrame(\[\["a"\], \["a"\], \["a"\], \["b"\], \["b"\], \["a"\]\], columns\=\["A"\])
\>>> df
   A
0  a
1  a
2  a
3  b
4  b
5  a
\>>> df.groupby("A").cumcount()
0    0
1    1
2    2
3    0
4    1
5    3
dtype: int64
\>>> df.groupby("A").cumcount(ascending\=False)
0    3
1    2
2    1
3    1
4    0
5    0
dtype: int64

Copy to clipboard

On this page