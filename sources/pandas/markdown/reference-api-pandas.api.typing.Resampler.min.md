[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.min.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.min[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.min.html#pandas-api-typing-resampler-min "Link to this heading")

=============================================================================================================================================================================

final Resampler.min(_numeric\_only\=False_, _min\_count\=0_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1224-L1279)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.min.html#pandas.api.typing.Resampler.min "Link to this definition")

Compute min value of group.

This method returns the minimum value within each resampled time period.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Changed in version 2.0.0: numeric\_only no longer accepts `None`.

**min\_count**int, default 0

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

Returns:

Series or DataFrame

Compute the minimum value in the given Series or DataFrame.

See also

`core.resample.Resampler.max`

Compute max value of group.

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
\>>> ser.resample("MS").min()
2023-01-01    1
2023-02-01    3
Freq: MS, dtype: int64

Copy to clipboard

On this page