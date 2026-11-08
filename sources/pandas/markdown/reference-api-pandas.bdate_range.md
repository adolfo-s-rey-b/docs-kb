[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.bdate_range.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.bdate_range.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.bdate_range.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.bdate_range.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.bdate_range.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.bdate_range.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.bdate_range.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.bdate_range.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.bdate_range.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.bdate_range.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.bdate_range.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.bdate_range.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.bdate\_range[#](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html#pandas-bdate-range "Link to this heading")

=======================================================================================================================================

pandas.bdate\_range(_start\=None_, _end\=None_, _periods\=None_, _freq\='B'_, _tz\=None_, _normalize\=True_, _name\=None_, _weekmask\=None_, _holidays\=None_, _inclusive\='both'_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L2794-L2907)
[#](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html#pandas.bdate_range "Link to this definition")

Return a fixed frequency DatetimeIndex with business day as the default.

This function generates a DatetimeIndex using business day frequency by default, skipping weekends. Custom business day calendars can be specified via `weekmask` and `holidays`.

Parameters:

**start**str or datetime-like, default None

Left bound for generating dates.

**end**str or datetime-like, default None

Right bound for generating dates.

**periods**int, default None

Number of periods to generate.

**freq**str, Timedelta, datetime.timedelta, or DateOffset, default ‘B’

Frequency strings can have multiples, e.g. ‘5h’. The default is business daily (‘B’).

**tz**str or None

Time zone name for returning localized DatetimeIndex, for example Asia/Beijing.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**name**Hashable, default None

Name of the resulting DatetimeIndex.

**weekmask**str or None, default None

Weekmask of valid business days, passed to `numpy.busdaycalendar`, only used when custom frequency strings are passed. The default value None is equivalent to ‘Mon Tue Wed Thu Fri’.

**holidays**list-like or None, default None

Dates to exclude from the set of valid business days, passed to `numpy.busdaycalendar`, only used when custom frequency strings are passed.

**inclusive**{“both”, “neither”, “left”, “right”}, default “both”

Include boundaries; Whether to set each bound as closed or open.

**\*\*kwargs**

For compatibility. Has no effect on the result.

Returns:

DatetimeIndex

Fixed frequency DatetimeIndex.

See also

[`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")

Return a fixed frequency DatetimeIndex.

[`period_range`](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas.period_range "pandas.period_range")

Return a fixed frequency PeriodIndex.

[`timedelta_range`](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas.timedelta_range "pandas.timedelta_range")

Return a fixed frequency TimedeltaIndex.

Notes

Of the four parameters: `start`, `end`, `periods`, and `freq`, exactly three must be specified. Specifying `freq` is a requirement for `bdate_range`. Use `date_range` if specifying `freq` is not desired.

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

Examples

Note how the two weekend days are skipped in the result.

\>>> pd.bdate\_range(start\="1/1/2018", end\="1/08/2018")
DatetimeIndex(\['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',\
           '2018-01-05', '2018-01-08'\],
          dtype='datetime64\[us\]', freq='B')

Copy to clipboard

On this page