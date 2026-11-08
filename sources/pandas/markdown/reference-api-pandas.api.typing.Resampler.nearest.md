[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nearest.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.nearest.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nearest.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.nearest.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.nearest.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.nearest.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.nearest.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.nearest.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.nearest.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.nearest.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.nearest.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.nearest.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.nearest.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.nearest.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.nearest[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nearest.html#pandas-api-typing-resampler-nearest "Link to this heading")

=========================================================================================================================================================================================

final Resampler.nearest(_limit\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L690-L746)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nearest.html#pandas.api.typing.Resampler.nearest "Link to this definition")

Resample by using the nearest value.

When resampling data, missing values may appear (e.g., when the resampling frequency is higher than the original frequency). The nearest method will replace `NaN` values that appeared in the resampled data with the value from the nearest member of the sequence, based on the index value. Missing values that existed in the original data will not be modified. If limit is given, fill only this many values in each direction for each of the original values.

Parameters:

**limit**int, optional

Limit of how many values to fill.

Returns:

Series or DataFrame

An upsampled Series or DataFrame with `NaN` values filled with their nearest value.

See also

[`bfill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.bfill.html#pandas.api.typing.Resampler.bfill "pandas.api.typing.Resampler.bfill")

Backward fill the new missing values in the resampled data.

[`ffill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ffill.html#pandas.api.typing.Resampler.ffill "pandas.api.typing.Resampler.ffill")

Forward fill `NaN` values.

Examples

\>>> s \= pd.Series(\[1, 2\], index\=pd.date\_range("20180101", periods\=2, freq\="1h"))
\>>> s
2018-01-01 00:00:00    1
2018-01-01 01:00:00    2
Freq: h, dtype: int64

Copy to clipboard

\>>> s.resample("15min").nearest()
2018-01-01 00:00:00    1
2018-01-01 00:15:00    1
2018-01-01 00:30:00    2
2018-01-01 00:45:00    2
2018-01-01 01:00:00    2
Freq: 15min, dtype: int64

Copy to clipboard

Limit the number of upsampled values imputed by the nearest:

\>>> s.resample("15min").nearest(limit\=1)
2018-01-01 00:00:00    1.0
2018-01-01 00:15:00    1.0
2018-01-01 00:30:00    NaN
2018-01-01 00:45:00    2.0
2018-01-01 01:00:00    2.0
Freq: 15min, dtype: float64

Copy to clipboard

On this page