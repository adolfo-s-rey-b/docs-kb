[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.mean.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.mean.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.mean.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.mean.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.mean.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.mean.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.mean.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.mean.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.mean.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.mean.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.mean.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.mean.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.mean.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.mean.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.mean[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.mean.html#pandas-api-typing-resampler-mean "Link to this heading")

================================================================================================================================================================================

final Resampler.mean(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1500-L1555)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.mean.html#pandas.api.typing.Resampler.mean "Link to this definition")

Compute mean of groups, excluding missing values.

This method calculates the arithmetic mean of values within each resampled time period.

Parameters:

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: numeric\_only now defaults to `False`.

Returns:

DataFrame or Series

Mean of values within each group.

See also

`core.resample.Resampler.median`

Compute median of groups, excluding missing values.

`core.resample.Resampler.sum`

Compute sum of groups, excluding missing values.

`core.resample.Resampler.std`

Compute standard deviation of groups, excluding missing values.

`core.resample.Resampler.var`

Compute variance of groups, excluding missing values.

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
\>>> ser.resample("MS").mean()
2023-01-01    1.5
2023-02-01    3.5
Freq: MS, dtype: float64

Copy to clipboard

On this page