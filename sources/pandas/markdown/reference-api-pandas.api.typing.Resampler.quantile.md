[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.quantile.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.quantile.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.quantile.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.quantile.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.quantile.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.quantile.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.quantile.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.quantile.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.quantile.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.quantile.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.quantile.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.quantile.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.quantile.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.quantile.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.quantile[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.quantile.html#pandas-api-typing-resampler-quantile "Link to this heading")

============================================================================================================================================================================================

final Resampler.quantile(_q\=0.5_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L1942-L1998)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.quantile.html#pandas.api.typing.Resampler.quantile "Link to this definition")

Return value at the given quantile.

Computes the quantile of values within each resampled group.

Parameters:

**q**float or array-like, default 0.5 (50% quantile)

Value between 0 <= q <= 1, the quantile(s) to compute.

**\*\*kwargs**

Additional keyword arguments to be passed to the function.

Returns:

DataFrame or Series

Quantile of values within each group.

See also

`Series.quantile`

Return a series, where the index is q and the values are the quantiles.

`DataFrame.quantile`

Return a DataFrame, where the columns are the columns of self, and the values are the quantiles.

[`DataFrameGroupBy.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.quantile.html#pandas.api.typing.DataFrameGroupBy.quantile "pandas.api.typing.DataFrameGroupBy.quantile")

Return a DataFrame, where the columns are groupby columns, and the values are its quantiles.

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
\>>> ser.resample("MS").quantile()
2023-01-01    2.0
2023-02-01    4.0
Freq: MS, dtype: float64

Copy to clipboard

\>>> ser.resample("MS").quantile(0.25)
2023-01-01    1.5
2023-02-01    3.5
Freq: MS, dtype: float64

Copy to clipboard

On this page