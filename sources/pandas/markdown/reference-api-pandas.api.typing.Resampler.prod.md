[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.prod.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.prod.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.prod.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.prod.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.prod.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.prod.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.prod.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.prod.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.prod.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.prod.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.prod.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.prod.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.prod.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.prod.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.prod[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.prod.html#pandas-api-typing-resampler-prod "Link to this heading")

================================================================================================================================================================================

final Resampler.prod(_numeric\_only\=False_, _min\_count\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1166-L1222)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.prod.html#pandas.api.typing.Resampler.prod "Link to this definition")

Compute prod of group values.

This method calculates the product of all values within each resampled time period.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Changed in version 2.0.0: numeric\_only no longer accepts `None`.

**min\_count**int, default 0

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

Returns:

Series or DataFrame

Computed prod of values within each group.

See also

`core.resample.Resampler.sum`

Compute sum of groups, excluding missing values.

`core.resample.Resampler.mean`

Compute mean of groups, excluding missing values.

`core.resample.Resampler.median`

Compute median of groups, excluding missing values.

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
\>>> ser.resample("MS").prod()
2023-01-01    2
2023-02-01   12
Freq: MS, dtype: int64

Copy to clipboard

On this page