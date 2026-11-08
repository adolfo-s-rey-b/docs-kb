[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.period_range.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.period_range.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.period_range.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.period_range.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.period_range.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.period_range.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.period_range.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.period_range.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.period_range.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.period_range.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.period_range.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.period_range.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.period\_range[#](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas-period-range "Link to this heading")

==========================================================================================================================================

pandas.period\_range(_start\=None_, _end\=None_, _periods\=None_, _freq\=None_, _name\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L1159-L1238)
[#](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas.period_range "Link to this definition")

Return a fixed frequency PeriodIndex.

The day (calendar) is the default frequency.

Parameters:

**start**str, datetime, date, pandas.Timestamp, or period-like, default None

Left bound for generating periods.

**end**str, datetime, date, pandas.Timestamp, or period-like, default None

Right bound for generating periods.

**periods**int, default None

Number of periods to generate.

**freq**str or DateOffset, optional

Frequency alias. By default the freq is taken from start or end if those are Period objects. Otherwise, the default is `"D"` for daily frequency.

**name**str, default None

Name of the resulting PeriodIndex.

Returns:

PeriodIndex

A PeriodIndex of fixed frequency periods.

See also

[`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")

Returns a fixed frequency DatetimeIndex.

[`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")

Represents a period of time.

[`PeriodIndex`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.html#pandas.PeriodIndex "pandas.PeriodIndex")

Immutable ndarray holding ordinal values indicating regular periods in time.

Notes

Of the three parameters: `start`, `end`, and `periods`, exactly two must be specified.

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

Examples

\>>> pd.period\_range(start\="2017-01-01", end\="2018-01-01", freq\="M")
PeriodIndex(\['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',\
         '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',\
         '2018-01'\],
        dtype='period\[M\]')

Copy to clipboard

If `start` or `end` are `Period` objects, they will be used as anchor endpoints for a `PeriodIndex` with frequency matching that of the `period_range` constructor.

\>>> pd.period\_range(
...     start\=pd.Period("2017Q1", freq\="Q"),
...     end\=pd.Period("2017Q2", freq\="Q"),
...     freq\="M",
... )
PeriodIndex(\['2017-03', '2017-04', '2017-05', '2017-06'\],
            dtype='period\[M\]')

Copy to clipboard

On this page