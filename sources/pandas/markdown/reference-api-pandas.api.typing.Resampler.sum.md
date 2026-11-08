[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.sum.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.sum[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.sum.html#pandas-api-typing-resampler-sum "Link to this heading")

=============================================================================================================================================================================

final Resampler.sum(_numeric\_only\=False_, _min\_count\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1106-L1164)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.sum.html#pandas.api.typing.Resampler.sum "Link to this definition")

Compute sum of group values.

This method provides a simple way to compute the sum of values within each resampled group, particularly useful for aggregating time-based data into daily, monthly, or yearly sums.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Changed in version 2.0.0: numeric\_only no longer accepts `None`.

**min\_count**int, default 0

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

Returns:

Series or DataFrame

Computed sum of values within each group.

See also

`core.resample.Resampler.mean`

Compute mean of groups, excluding missing values.

`core.resample.Resampler.count`

Compute count of group, excluding missing values.

`DataFrame.resample`

Resample time-series data.

`Series.sum`

Return the sum of the values over the requested axis.

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
\>>> ser.resample("MS").sum()
2023-01-01    3
2023-02-01    7
Freq: MS, dtype: int64

Copy to clipboard

On this page