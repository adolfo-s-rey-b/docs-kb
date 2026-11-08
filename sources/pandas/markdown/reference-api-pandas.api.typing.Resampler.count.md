[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.count.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.count.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.count.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.count.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.count.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.count.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.count.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.count.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.count.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.count.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.count.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.count.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.count.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.count.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.count[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.count.html#pandas-api-typing-resampler-count "Link to this heading")

===================================================================================================================================================================================

final Resampler.count()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1889-L1940)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.count.html#pandas.api.typing.Resampler.count "Link to this definition")

Compute count of group, excluding missing values.

This method returns the number of non-null values in each resampled time period.

Returns:

Series or DataFrame

Count of values within each group.

See also

`Series.groupby`

Apply a function groupby to a Series.

`DataFrame.groupby`

Apply a function groupby to each row or column of a DataFrame.

Examples

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
\>>> ser.resample("MS").count()
2023-01-01    2
2023-02-01    2
Freq: MS, dtype: int64

Copy to clipboard

On this page