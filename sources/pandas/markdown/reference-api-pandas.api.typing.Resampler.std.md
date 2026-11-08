[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.std.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.std[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.std.html#pandas-api-typing-resampler-std "Link to this heading")

=============================================================================================================================================================================

final Resampler.std(_ddof\=1_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1557-L1619)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.std.html#pandas.api.typing.Resampler.std "Link to this definition")

Compute standard deviation of groups, excluding missing values.

This method calculates the sample standard deviation of values within each resampled time period.

Parameters:

**ddof**int, default 1

Degrees of freedom.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 2.0.0: numeric\_only now defaults to `False`.

Returns:

DataFrame or Series

Standard deviation of values within each group.

See also

`core.resample.Resampler.mean`

Compute mean of groups, excluding missing values.

`core.resample.Resampler.median`

Compute median of groups, excluding missing values.

`core.resample.Resampler.var`

Compute variance of groups, excluding missing values.

Notes

To use the same divisor as `numpy.std`, use `ddof=0` instead of the default `ddof=1`.

Examples

\>>> ser \= pd.Series(
...     \[1, 3, 2, 4, 3, 8\],
...     index\=pd.DatetimeIndex(
...         \[\
...             "2023-01-01",\
...             "2023-01-10",\
...             "2023-01-15",\
...             "2023-02-01",\
...             "2023-02-10",\
...             "2023-02-15",\
...         \]
...     ),
... )
\>>> ser.resample("MS").std()
2023-01-01    1.000000
2023-02-01    2.645751
Freq: MS, dtype: float64

Copy to clipboard

On this page