[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.size.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.size.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.size[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.size.html#pandas-api-typing-dataframegroupby-size "Link to this heading")

=====================================================================================================================================================================================================

DataFrameGroupBy.size()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L2651-L2744)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.size.html#pandas.api.typing.DataFrameGroupBy.size "Link to this definition")

Compute group sizes.

Returns the number of rows in each group. This is useful for understanding the distribution of data across groups.

Returns:

DataFrame or Series

Number of rows in each group as a Series if as\_index is True or a DataFrame if as\_index is False.

See also

`Series.size`

Apply function size to a Series.

`DataFrame.size`

Apply function size to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b"\]
\>>> ser \= pd.Series(\[1, 2, 3\], index\=lst)
\>>> ser
a     1
a     2
b     3
dtype: int64
\>>> ser.groupby(level\=0).size()
a    2
b    1
dtype: int64

Copy to clipboard

\>>> data \= \[\[1, 2, 3\], \[1, 5, 6\], \[7, 8, 9\]\]
\>>> df \= pd.DataFrame(
...     data, columns\=\["a", "b", "c"\], index\=\["owl", "toucan", "eagle"\]
... )
\>>> df
        a  b  c
owl     1  2  3
toucan  1  5  6
eagle   7  8  9
\>>> df.groupby("a").size()
a
1    2
7    1
dtype: int64

Copy to clipboard

For Resampler:

\>>> ser \= pd.Series(
...     \[1, 2, 3\],
...     index\=pd.DatetimeIndex(\["2023-01-01", "2023-01-15", "2023-02-01"\]),
... )
\>>> ser
2023-01-01    1
2023-01-15    2
2023-02-01    3
dtype: int64
\>>> ser.resample("MS").size()
2023-01-01    2
2023-02-01    1
Freq: MS, dtype: int64

Copy to clipboard

On this page