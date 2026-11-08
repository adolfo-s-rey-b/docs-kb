[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.median.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.median.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.median.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.median.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.median.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.median.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.median.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.median.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.median.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.median.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.median.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.median.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.median.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.median.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.median[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.median.html#pandas-api-typing-resampler-median "Link to this heading")

======================================================================================================================================================================================

final Resampler.median(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1450-L1498)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.median.html#pandas.api.typing.Resampler.median "Link to this definition")

Compute median of groups, excluding missing values.

For multiple groupings, the result index will be a MultiIndex

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Changed in version 2.0.0: numeric\_only no longer accepts `None` and defaults to False.

Returns:

Series or DataFrame

Median of values within each group.

See also

`Series.groupby`

Apply a function groupby to a Series.

`DataFrame.groupby`

Apply a function groupby to each row or column of a DataFrame.

Examples

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