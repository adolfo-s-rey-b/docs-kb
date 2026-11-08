[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.indices.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.indices.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.indices[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.indices.html#pandas-api-typing-seriesgroupby-indices "Link to this heading")

=====================================================================================================================================================================================================

property SeriesGroupBy.indices[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L308-L377)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.indices.html#pandas.api.typing.SeriesGroupBy.indices "Link to this definition")

Dict {group name -> group indices}.

The dictionary keys represent the group labels (e.g., timestamps for a time-based resampling operation), and the values are arrays of integer positions indicating where the elements of each group are located in the original data. This property is particularly useful when working with resampled data, as it provides insight into how the original time-series data has been grouped.

See also

`core.groupby.DataFrameGroupBy.indices`

Provides a mapping of group rows to positions of the elements.

`core.groupby.SeriesGroupBy.indices`

Provides a mapping of group rows to positions of the elements.

`core.resample.Resampler.indices`

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
\>>> ser.groupby(level\=0).indices
{'a': array(\[0, 1\]), 'b': array(\[2\])}

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
\>>> df.groupby(by\=\["a"\]).indices
{np.int64(1): array(\[0, 1\]), np.int64(7): array(\[2\])}

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
\>>> ser.resample("MS").indices
defaultdict(<class 'list'>, {Timestamp('2023-01-01 00:00:00'): \[0, 1\],
Timestamp('2023-02-01 00:00:00'): \[2, 3\]})

Copy to clipboard

On this page