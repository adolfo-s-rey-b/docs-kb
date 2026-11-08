[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ffill.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.ffill[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ffill.html#pandas-api-typing-resampler-ffill "Link to this heading")

===================================================================================================================================================================================

final Resampler.ffill(_limit\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L611-L688)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ffill.html#pandas.api.typing.Resampler.ffill "Link to this definition")

Forward fill the values.

This method fills missing values by propagating the last valid observation forward, up to the next valid observation. It is commonly used in time series analysis when resampling data to a higher frequency (upsampling) and filling gaps in the resampled output.

Parameters:

**limit**int, optional

Limit of how many values to fill.

Returns:

Series

The resampled data with missing values filled forward.

See also

`Series.fillna`

Fill NA/NaN values using the specified method.

`DataFrame.fillna`

Fill NA/NaN values using the specified method.

Examples

Here we only create a `Series`.

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

Copy to clipboard

Example for `ffill` with downsampling (we have fewer dates after resampling):

\>>> ser.resample("MS").ffill()
2023-01-01    1
2023-02-01    3
Freq: MS, dtype: int64

Copy to clipboard

Example for `ffill` with upsampling (fill the new dates with the previous value):

\>>> ser.resample("W").ffill()
2023-01-01    1
2023-01-08    1
2023-01-15    2
2023-01-22    2
2023-01-29    2
2023-02-05    3
2023-02-12    3
2023-02-19    4
Freq: W-SUN, dtype: int64

Copy to clipboard

With upsampling and limiting (only fill the first new date with the previous value):

\>>> ser.resample("W").ffill(limit\=1)
2023-01-01    1.0
2023-01-08    1.0
2023-01-15    2.0
2023-01-22    2.0
2023-01-29    NaN
2023-02-05    3.0
2023-02-12    NaN
2023-02-19    4.0
Freq: W-SUN, dtype: float64

Copy to clipboard

On this page