[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.median.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.median.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.median.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.median[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.median.html#pandas-api-typing-seriesgroupby-median "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.median(_numeric\_only\=False_, _skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L2087-L2184)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.median.html#pandas.api.typing.SeriesGroupBy.median "Link to this definition")

Compute median of groups, excluding missing values.

For multiple groupings, the result index will be a MultiIndex

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Changed in version 2.0.0: numeric\_only no longer accepts `None` and defaults to False.

**skipna**bool, default True

Exclude NA/null values. If an entire group is NA, the result will be NA.

Added in version 3.0.0.

Returns:

Series or DataFrame

Median of values within each group.

See also

`Series.median`

Apply function median to a Series.

`DataFrame.median`

Apply function median to each row or column of a DataFrame.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "a", "b", "b", "b"\]
\>>> ser \= pd.Series(\[7, 2, 8, 4, 3, 3\], index\=lst)
\>>> ser
a     7
a     2
a     8
b     4
b     3
b     3
dtype: int64
\>>> ser.groupby(level\=0).median()
a    7.0
b    3.0
dtype: float64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= {"a": \[1, 3, 5, 7, 7, 8, 3\], "b": \[1, 4, 8, 4, 4, 2, 1\]}
\>>> df \= pd.DataFrame(
...     data, index\=\["dog", "dog", "dog", "mouse", "mouse", "mouse", "mouse"\]
... )
\>>> df
         a  b
  dog    1  1
  dog    3  4
  dog    5  8
mouse    7  4
mouse    7  4
mouse    8  2
mouse    3  1
\>>> df.groupby(level\=0).median()
         a    b
dog    3.0  4.0
mouse  7.0  3.0

Copy to clipboard

For Resampler:

\>>> ser \= pd.Series(
...     \[1, 2, 3, 3, 4, 5\],
...     index\=pd.DatetimeIndex(
...         \[\
...             "2023-01-01",\
...             "2023-01-10",\
...             "2023-01-15",\
...             "2023-02-01",\
...             "2023-02-10",\
...             "2023-02-15",\
...         \]
...     ),
... )
\>>> ser.resample("MS").median()
2023-01-01    2.0
2023-02-01    4.0
Freq: MS, dtype: float64

Copy to clipboard

On this page