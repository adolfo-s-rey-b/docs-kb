[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.bfill.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.bfill.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.bfill.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.bfill.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.bfill.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.bfill.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.bfill.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.bfill.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.bfill.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.bfill.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.bfill.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.bfill.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.bfill.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.bfill.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.bfill[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.bfill.html#pandas-api-typing-resampler-bfill "Link to this heading")

===================================================================================================================================================================================

final Resampler.bfill(_limit\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L748-L848)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.bfill.html#pandas.api.typing.Resampler.bfill "Link to this definition")

Backward fill the new missing values in the resampled data.

In statistics, imputation is the process of replacing missing data with substituted values [\[1\]](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.bfill.html#rc40a2f8d886c-1)
. When resampling data, missing values may appear (e.g., when the resampling frequency is higher than the original frequency). The backward fill will replace NaN values that appeared in the resampled data with the next value in the original sequence. Missing values that existed in the original data will not be modified.

Parameters:

**limit**int, optional

Limit of how many values to fill.

Returns:

Series, DataFrame

An upsampled Series or DataFrame with backward filled NaN values.

See also

[`nearest`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nearest.html#pandas.api.typing.Resampler.nearest "pandas.api.typing.Resampler.nearest")

Fill NaN values with nearest neighbor starting from center.

[`ffill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ffill.html#pandas.api.typing.Resampler.ffill "pandas.api.typing.Resampler.ffill")

Forward fill NaN values.

`Series.fillna`

Fill NaN values in the Series using the specified method, which can be ‘backfill’.

`DataFrame.fillna`

Fill NaN values in the DataFrame using the specified method, which can be ‘backfill’.

References

\[[1](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.bfill.html#id1)\
\]

[https://en.wikipedia.org/wiki/Imputation\_%28statistics%29](https://en.wikipedia.org/wiki/Imputation_%28statistics%29)

Examples

Resampling a Series:

\>>> s \= pd.Series(
...     \[1, 2, 3\], index\=pd.date\_range("20180101", periods\=3, freq\="h")
... )
\>>> s
2018-01-01 00:00:00    1
2018-01-01 01:00:00    2
2018-01-01 02:00:00    3
Freq: h, dtype: int64

Copy to clipboard

\>>> s.resample("30min").bfill()
2018-01-01 00:00:00    1
2018-01-01 00:30:00    2
2018-01-01 01:00:00    2
2018-01-01 01:30:00    3
2018-01-01 02:00:00    3
Freq: 30min, dtype: int64

Copy to clipboard

\>>> s.resample("15min").bfill(limit\=2)
2018-01-01 00:00:00    1.0
2018-01-01 00:15:00    NaN
2018-01-01 00:30:00    2.0
2018-01-01 00:45:00    2.0
2018-01-01 01:00:00    2.0
2018-01-01 01:15:00    NaN
2018-01-01 01:30:00    3.0
2018-01-01 01:45:00    3.0
2018-01-01 02:00:00    3.0
Freq: 15min, dtype: float64

Copy to clipboard

Resampling a DataFrame that has missing values:

\>>> df \= pd.DataFrame(
...     {"a": \[2, np.nan, 6\], "b": \[1, 3, 5\]},
...     index\=pd.date\_range("20180101", periods\=3, freq\="h"),
... )
\>>> df
                       a  b
2018-01-01 00:00:00  2.0  1
2018-01-01 01:00:00  NaN  3
2018-01-01 02:00:00  6.0  5

Copy to clipboard

\>>> df.resample("30min").bfill()
                       a  b
2018-01-01 00:00:00  2.0  1
2018-01-01 00:30:00  NaN  3
2018-01-01 01:00:00  NaN  3
2018-01-01 01:30:00  6.0  5
2018-01-01 02:00:00  6.0  5

Copy to clipboard

\>>> df.resample("15min").bfill(limit\=2)
                       a    b
2018-01-01 00:00:00  2.0  1.0
2018-01-01 00:15:00  NaN  NaN
2018-01-01 00:30:00  NaN  3.0
2018-01-01 00:45:00  NaN  3.0
2018-01-01 01:00:00  NaN  3.0
2018-01-01 01:15:00  NaN  NaN
2018-01-01 01:30:00  6.0  5.0
2018-01-01 01:45:00  6.0  5.0
2018-01-01 02:00:00  6.0  5.0

Copy to clipboard

On this page