[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sem.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.sem.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.sem[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sem.html#pandas-api-typing-seriesgroupby-sem "Link to this heading")

=========================================================================================================================================================================================

SeriesGroupBy.sem(_ddof\=1_, _numeric\_only\=False_, _skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L2545-L2649)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sem.html#pandas.api.typing.SeriesGroupBy.sem "Link to this definition")

Compute standard error of the mean of groups, excluding missing values.

For multiple groupings, the result index will be a MultiIndex.

Parameters:

**ddof**int, default 1

Degrees of freedom.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: numeric\_only now defaults to `False`.

**skipna**bool, default True

Exclude NA/null values. If an entire group is NA, the result will be NA.

Added in version 3.0.0.

Returns:

Series or DataFrame

Standard error of the mean of values within each group.

See also

`DataFrame.sem`

Return unbiased standard error of the mean over requested axis.

`Series.sem`

Return unbiased standard error of the mean over requested axis.

Examples

For SeriesGroupBy:

\>>> lst \= \["a", "a", "b", "b"\]
\>>> ser \= pd.Series(\[5, 10, 8, 14\], index\=lst)
\>>> ser
a     5
a    10
b     8
b    14
dtype: int64
\>>> ser.groupby(level\=0).sem()
a    2.5
b    3.0
dtype: float64

Copy to clipboard

For DataFrameGroupBy:

\>>> data \= \[\[1, 12, 11\], \[1, 15, 2\], \[2, 5, 8\], \[2, 6, 12\]\]
\>>> df \= pd.DataFrame(
...     data,
...     columns\=\["a", "b", "c"\],
...     index\=\["tuna", "salmon", "catfish", "goldfish"\],
... )
\>>> df
           a   b   c
    tuna   1  12  11
  salmon   1  15   2
 catfish   2   5   8
goldfish   2   6  12
\>>> df.groupby("a").sem()
      b  c
a
1    1.5  4.5
2    0.5  2.0

Copy to clipboard

For Resampler:

\>>> ser \= pd.Series(
...     \[1, 3, 2, 4, 3, 8\],
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
\>>> ser.resample("MS").sem()
2023-01-01    0.577350
2023-02-01    1.527525
Freq: MS, dtype: float64

Copy to clipboard

On this page