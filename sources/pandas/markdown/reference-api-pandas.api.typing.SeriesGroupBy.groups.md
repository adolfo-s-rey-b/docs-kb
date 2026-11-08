[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.groups.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.groups[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.groups.html#pandas-api-typing-seriesgroupby-groups "Link to this heading")

==================================================================================================================================================================================================

property SeriesGroupBy.groups[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L226-L301)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.groups.html#pandas.api.typing.SeriesGroupBy.groups "Link to this definition")

Dict {group name -> group labels}.

This property provides a dictionary representation of the groupings formed during a groupby operation, where each key represents a unique group value from the specified column(s), and each value is a list of index labels that belong to that group.

See also

`core.groupby.DataFrameGroupBy.get_group`

Retrieve group from a `DataFrameGroupBy` object with provided name.

`core.groupby.SeriesGroupBy.get_group`

Retrieve group from a `SeriesGroupBy` object with provided name.

`core.resample.Resampler.get_group`

Retrieve group from a `Resampler` object with provided name.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[1, 2, 3\], index\=lst)
\>>> ser
a    1
a    2
b    3
dtype: int64
\>>> ser.groupby(level\=0).groups
{'a': \['a', 'a'\], 'b': \['b'\]}

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 2, 3\], \[1, 5, 6\], \[7, 8, 9\]\]
\>>> df \= pd.DataFrame(data, columns\=\["a", "b", "c"\])
\>>> df
   a  b  c
0  1  2  3
1  1  5  6
2  7  8  9
\>>> df.groupby(by\="a").groups
{1: \[0, 1\], 7: \[2\]}

Copy to clipboard

For Resampler:

\>>> ser \= pd.Series(
...     \[1, 2, 3, 4\],
...     index\=pd.DatetimeIndex(
...         \["2023-01-01", "2023-01-15", "2023-02-01", "2023-02-15"\]
...     ),
... )
\>>> ser
2023-01-01    1
2023-01-15    2
2023-02-01    3
2023-02-15    4
dtype: int64
\>>> ser.resample("MS").groups
{Timestamp('2023-01-01 00:00:00'): np.int64(2),
 Timestamp('2023-02-01 00:00:00'): np.int64(4)}

Copy to clipboard

On this page