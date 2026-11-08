[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.last.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.last.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.last.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.last.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.last.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.last.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.last.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.last.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.last.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.last.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.last.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.last.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.last.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.last.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.last[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.last.html#pandas-api-typing-resampler-last "Link to this heading")

================================================================================================================================================================================

final Resampler.last(_numeric\_only\=False_, _min\_count\=0_, _skipna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1394-L1448)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.last.html#pandas.api.typing.Resampler.last "Link to this definition")

Compute the last non-null entry of each column.

This method returns the last value encountered in each resampled time period, skipping missing values by default.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**min\_count**int, default 0

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

**skipna**bool, default True

Exclude NA/null values. If an entire group is NA, the result will be NA.

Returns:

Series or DataFrame

Last of values within each group.

See also

`core.resample.Resampler.first`

Compute the first non-null value in each group.

`core.resample.Resampler.mean`

Compute mean of groups, excluding missing values.

Examples

\>>> s \= pd.Series(
...     \[1, 2, 3, 4\],
...     index\=pd.DatetimeIndex(
...         \["2023-01-01", "2023-01-15", "2023-02-01", "2023-02-15"\]
...     ),
... )
\>>> s
2023-01-01    1
2023-01-15    2
2023-02-01    3
2023-02-15    4
dtype: int64
\>>> s.resample("MS").last()
2023-01-01    2
2023-02-01    4
Freq: MS, dtype: int64

Copy to clipboard

On this page