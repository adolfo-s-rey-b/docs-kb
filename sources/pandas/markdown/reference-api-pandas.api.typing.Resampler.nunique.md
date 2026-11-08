[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nunique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.nunique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nunique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.nunique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.nunique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.nunique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.nunique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.nunique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.nunique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.nunique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.nunique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.nunique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.nunique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.nunique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.nunique[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nunique.html#pandas-api-typing-resampler-nunique "Link to this heading")

=========================================================================================================================================================================================

final Resampler.nunique()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1799-L1835)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nunique.html#pandas.api.typing.Resampler.nunique "Link to this definition")

Return number of unique elements in the group.

This method counts the number of distinct values within each resampled time period.

Returns:

Series

Number of unique values within each group.

See also

`core.groupby.SeriesGroupBy.nunique`

Method nunique for SeriesGroupBy.

Examples

\>>> ser \= pd.Series(
...     \[1, 2, 3, 3\],
...     index\=pd.DatetimeIndex(
...         \["2023-01-01", "2023-01-15", "2023-02-01", "2023-02-15"\]
...     ),
... )
\>>> ser
2023-01-01    1
2023-01-15    2
2023-02-01    3
2023-02-15    3
dtype: int64
\>>> ser.resample("MS").nunique()
2023-01-01    2
2023-02-01    1
Freq: MS, dtype: int64

Copy to clipboard

On this page