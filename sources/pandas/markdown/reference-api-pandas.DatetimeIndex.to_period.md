[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_period.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.to\_period[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_period.html#pandas-datetimeindex-to-period "Link to this heading")

===========================================================================================================================================================================

DatetimeIndex.to\_period(_freq\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L1732-L1803)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_period.html#pandas.DatetimeIndex.to_period "Link to this definition")

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