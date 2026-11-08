[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.asfreq.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.asfreq.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.asfreq.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.asfreq.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.asfreq.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.asfreq.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.asfreq.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.asfreq.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.asfreq.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.asfreq.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.asfreq.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.asfreq.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.asfreq.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.asfreq.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.asfreq[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.asfreq.html#pandas-api-typing-resampler-asfreq "Link to this heading")

======================================================================================================================================================================================

final Resampler.asfreq(_fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1060-L1104)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.asfreq.html#pandas.api.typing.Resampler.asfreq "Link to this definition")

Return the values at the new freq, essentially a reindex.

This method selects data at the specified frequency without aggregation, useful for upsampling to a higher frequency or selecting specific time points.

Parameters:

**fill\_value**scalar, optional

Value to use for missing values, applied during upsampling (note this does not fill NaNs that already were present).

Returns:

DataFrame or Series

Values at the specified freq.

See also

`Series.asfreq`

Convert TimeSeries to specified frequency.

`DataFrame.asfreq`

Convert TimeSeries to specified frequency.

Examples

\>>> ser \= pd.Series(
...     \[1, 2, 3, 4\],
...     index\=pd.DatetimeIndex(
...         \["2023-01-01", "2023-01-31", "2023-02-01", "2023-02-28"\]
...     ),
... )
\>>> ser
2023-01-01    1
2023-01-31    2
2023-02-01    3
2023-02-28    4
dtype: int64
\>>> ser.resample("MS").asfreq()
2023-01-01    1
2023-02-01    3
Freq: MS, dtype: int64

Copy to clipboard

On this page