[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.get_group.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.get_group.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.get_group.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.get_group.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.get_group.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.get_group.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.get_group.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.get_group.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.get_group.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.get_group.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.get_group.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.get_group.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.get_group.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.get_group.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.get\_group[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.get_group.html#pandas-api-typing-resampler-get-group "Link to this heading")

================================================================================================================================================================================================

Resampler.get\_group(_name_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L548-L644)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.get_group.html#pandas.api.typing.Resampler.get_group "Link to this definition")

Construct DataFrame from group with provided name.

This method retrieves all rows belonging to a specific group identified by the given name.

Parameters:

**name**object

The name of the group to get as a DataFrame.

Returns:

Series or DataFrame

Get the respective Series or DataFrame corresponding to the group provided.

See also

[`DataFrameGroupBy.groups`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html#pandas.api.typing.DataFrameGroupBy.groups "pandas.api.typing.DataFrameGroupBy.groups")

Dictionary representation of the groupings formed during a groupby operation.

[`DataFrameGroupBy.indices`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.indices.html#pandas.api.typing.DataFrameGroupBy.indices "pandas.api.typing.DataFrameGroupBy.indices")

Provides a mapping of group rows to positions of the elements.

[`SeriesGroupBy.groups`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.groups.html#pandas.api.typing.SeriesGroupBy.groups "pandas.api.typing.SeriesGroupBy.groups")

Dictionary representation of the groupings formed during a groupby operation.

[`SeriesGroupBy.indices`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.indices.html#pandas.api.typing.SeriesGroupBy.indices "pandas.api.typing.SeriesGroupBy.indices")

Provides a mapping of group rows to positions of the elements.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[1, 2, 3\], index\=lst)
\>>> ser
a    1
a    2
b    3
dtype: int64
\>>> ser.groupby(level\=0).get\_group("a")
a    1
a    2
dtype: int64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 2, 3\], \[1, 5, 6\], \[7, 8, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["owl", "toucan", "eagle"\]
... )
\>>> df
        a  b  c
owl     1  2  3
toucan  1  5  6
eagle   7  8  9
\>>> df.groupby(by\=\["a"\]).get\_group((1,))
        a  b  c
owl     1  2  3
toucan  1  5  6

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
\>>> ser.resample("MS").get\_group("2023-01-01")
2023-01-01    1
2023-01-15    2
dtype: int64

Copy to clipboard

On this page