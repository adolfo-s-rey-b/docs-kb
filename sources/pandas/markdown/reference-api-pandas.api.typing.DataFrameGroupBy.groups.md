[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.groups[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html#pandas-api-typing-dataframegroupby-groups "Link to this heading")

===========================================================================================================================================================================================================

property DataFrameGroupBy.groups[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L226-L301)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html#pandas.api.typing.DataFrameGroupBy.groups "Link to this definition")

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