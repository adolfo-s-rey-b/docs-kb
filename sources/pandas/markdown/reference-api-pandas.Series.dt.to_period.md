[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.to_period.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.to_period.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.to_period.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.to_period.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.to_period.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.to_period.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.to_period.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.to_period.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.to_period.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.to_period.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.to_period.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.to_period.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.to\_period[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html#pandas-series-dt-to-period "Link to this heading")

===============================================================================================================================================================

Series.dt.to\_period(_freq\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/datetimes.py#L1208-L1284)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html#pandas.Series.dt.to_period "Link to this definition")

Cast to PeriodArray/PeriodIndex at a particular frequency.

Converts DatetimeArray/Index to PeriodArray/PeriodIndex.

Parameters:

**freq**str, optional

One of pandas’ [period aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-period-aliases)
. Will be inferred by default.

Returns:

PeriodArray/PeriodIndex

Immutable ndarray holding ordinal values at a particular frequency.

Raises:

ValueError

When converting a DatetimeArray/Index with non-regular values, so that a frequency cannot be inferred.

See also

[`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")

Immutable ndarray holding ordinal values.

[`DatetimeIndex.to_pydatetime`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_pydatetime.html#pandas.DatetimeIndex.to_pydatetime "pandas.DatetimeIndex.to_pydatetime")

Return DatetimeIndex as object.

Examples

\>>> df \= pd.DataFrame(
...     {"y": \[1, 2, 3\]},
...     index\=pd.to\_datetime(
...         \[\
...             "2000-03-31 00:00:00",\
...             "2000-05-31 00:00:00",\
...             "2000-08-31 00:00:00",\
...         \]
...     ),
... )
\>>> df.index.to\_period("M")
PeriodIndex(\['2000-03', '2000-05', '2000-08'\],
            dtype='period\[M\]')

Copy to clipboard

Infer the daily frequency

\>>> idx \= pd.date\_range("2017-01-01", periods\=2)
\>>> idx.to\_period()
PeriodIndex(\['2017-01-01', '2017-01-02'\],
            dtype='period\[D\]')

Copy to clipboard

On this page