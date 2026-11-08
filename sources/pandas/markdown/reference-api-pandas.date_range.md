[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.date_range.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.date_range.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.date_range.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.date_range.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.date_range.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.date_range.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.date_range.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.date_range.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.date_range.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.date_range.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.date_range.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.date_range.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.date\_range[#](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas-date-range "Link to this heading")

====================================================================================================================================

pandas.date\_range(_start\=None_, _end\=None_, _periods\=None_, _freq\=None_, _tz\=None_, _normalize\=False_, _name\=None_, _inclusive\='both'_, _\*_, _unit\=None_, _ambiguous\='raise'_, _nonexistent\='raise'_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L2498-L2791)
[#](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "Link to this definition")

Return a fixed frequency DatetimeIndex.

Returns the range of equally spaced time points (where the difference between any two adjacent points is specified by the given frequency) such that they fall in the range \[start, end\] , where the first one and the last one are, resp., the first and last time points in that range that fall on the boundary of `freq` (if given as a frequency string) or that are valid for `freq` (if given as a [`pandas.tseries.offsets.DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")
). If `freq` is positive, the points satisfy start <\[=\] x <\[=\] end, and if `freq` is negative, the points satisfy end <\[=\] x <\[=\] start. (If exactly one of `start`, `end`, or `freq` is _not_ specified, this missing parameter can be computed given `periods`, the number of timesteps in the range. See the note below.)

Parameters:

**start**str or datetime-like, optional

Left bound for generating dates.

**end**str or datetime-like, optional

Right bound for generating dates.

**periods**int, optional

Number of periods to generate.

**freq**str, Timedelta, datetime.timedelta, or DateOffset, default ‘D’

Frequency strings can have multiples, e.g. ‘5h’. See [here](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
 for a list of frequency aliases.

**tz**str or tzinfo, optional

Time zone name for returning localized DatetimeIndex, for example ‘Asia/Hong\_Kong’. By default, the resulting DatetimeIndex is timezone-naive unless timezone-aware datetime-likes are passed.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**name**Hashable, default None

Name of the resulting DatetimeIndex.

**inclusive**{“both”, “neither”, “left”, “right”}, default “both”

Include boundaries; Whether to set each bound as closed or open.

**unit**{‘s’, ‘ms’, ‘us’, ‘ns’, None}, default None

Specify the desired resolution of the result. If not specified, this is inferred from the ‘start’, ‘end’, and ‘freq’ using the same inference as [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 taking the highest resolution of the three that are provided.

Added in version 2.0.0.

**ambiguous**‘infer’, bool-ndarray, ‘NaT’, default ‘raise’

When clocks moved backward due to DST, ambiguous times may arise. For example in Central European Time (UTC+01), when going from 03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC and at 01:30:00 UTC. In such a situation, the ambiguous parameter dictates how ambiguous times should be handled.

*   ‘infer’ will attempt to infer fall dst-transition hours based on order. Requires that the timestamps are monotonically increasing.
    
*   bool-ndarray where True signifies a DST time, False signifies a non-DST time (note that this flag is only applicable for ambiguous times)
    
*   ‘NaT’ will return NaT where there are ambiguous times
    
*   ‘raise’ will raise a ValueError if there are ambiguous times.
    

**nonexistent**‘shift\_forward’, ‘shift\_backward’, ‘NaT’, timedelta, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST.

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time
    
*   ‘NaT’ will return NaT where there are nonexistent times
    
*   timedelta objects will shift nonexistent times by the timedelta
    
*   ‘raise’ will raise a ValueError if there are nonexistent times.
    

**\*\*kwargs**

For compatibility. Has no effect on the result.

Returns:

DatetimeIndex

A DatetimeIndex object of the generated dates.

See also

[`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")

An immutable container for datetimes.

[`timedelta_range`](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas.timedelta_range "pandas.timedelta_range")

Return a fixed frequency TimedeltaIndex.

[`period_range`](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas.period_range "pandas.period_range")

Return a fixed frequency PeriodIndex.

[`interval_range`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")

Return a fixed frequency IntervalIndex.

Notes

Of the four parameters `start`, `end`, `periods`, and `freq`, a maximum of three can be specified at once. Of the three parameters `start`, `end`, and `periods`, at least two must be specified. If `freq` is omitted, the resulting `DatetimeIndex` will have `periods` linearly spaced elements between `start` and `end` (closed on both sides).

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

Examples

**Specifying the values**

The next four examples generate the same DatetimeIndex, but vary the combination of start, end and periods.

Specify start and end, with the default daily frequency.

\>>> pd.date\_range(start\="1/1/2018", end\="1/08/2018")
DatetimeIndex(\['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',\
               '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

Specify timezone-aware start and end, with the default daily frequency.

\>>> pd.date\_range(
...     start\=pd.to\_datetime("1/1/2018").tz\_localize("Europe/Berlin"),
...     end\=pd.to\_datetime("1/08/2018").tz\_localize("Europe/Berlin"),
... )
DatetimeIndex(\['2018-01-01 00:00:00+01:00', '2018-01-02 00:00:00+01:00',\
               '2018-01-03 00:00:00+01:00', '2018-01-04 00:00:00+01:00',\
               '2018-01-05 00:00:00+01:00', '2018-01-06 00:00:00+01:00',\
               '2018-01-07 00:00:00+01:00', '2018-01-08 00:00:00+01:00'\],
              dtype='datetime64\[us, Europe/Berlin\]', freq='D')

Copy to clipboard

Specify start and periods, the number of periods (days).

\>>> pd.date\_range(start\="1/1/2018", periods\=8)
DatetimeIndex(\['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',\
               '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

Specify end and periods, the number of periods (days).

\>>> pd.date\_range(end\="1/1/2018", periods\=8)
DatetimeIndex(\['2017-12-25', '2017-12-26', '2017-12-27', '2017-12-28',\
               '2017-12-29', '2017-12-30', '2017-12-31', '2018-01-01'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

Specify start, end, and periods; the frequency is generated automatically (linearly spaced).

\>>> pd.date\_range(start\="2018-04-24", end\="2018-04-27", periods\=3)
DatetimeIndex(\['2018-04-24 00:00:00', '2018-04-25 12:00:00',\
               '2018-04-27 00:00:00'\],
              dtype='datetime64\[us\]', freq=None)

Copy to clipboard

**Other Parameters**

Changed the freq (frequency) to `'ME'` (month end frequency).

\>>> pd.date\_range(start\="1/1/2018", periods\=5, freq\="ME")
DatetimeIndex(\['2018-01-31', '2018-02-28', '2018-03-31', '2018-04-30',\
               '2018-05-31'\],
              dtype='datetime64\[us\]', freq='ME')

Copy to clipboard

Multiples are allowed

\>>> pd.date\_range(start\="1/1/2018", periods\=5, freq\="3ME")
DatetimeIndex(\['2018-01-31', '2018-04-30', '2018-07-31', '2018-10-31',\
               '2019-01-31'\],
              dtype='datetime64\[us\]', freq='3ME')

Copy to clipboard

freq can also be specified as an Offset object.

\>>> pd.date\_range(start\="1/1/2018", periods\=5, freq\=pd.offsets.MonthEnd(3))
DatetimeIndex(\['2018-01-31', '2018-04-30', '2018-07-31', '2018-10-31',\
               '2019-01-31'\],
              dtype='datetime64\[us\]', freq='3ME')

Copy to clipboard

Use [`pandas.DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.DateOffset")
 for calendar steps that are not anchored to the start or end of a period.

\>>> pd.date\_range(end\="2017-03-12", periods\=3, freq\=pd.DateOffset(years\=1))
DatetimeIndex(\['2015-03-12', '2016-03-12', '2017-03-12'\],
              dtype='datetime64\[us\]', freq='<DateOffset: years=1>')

Copy to clipboard

Specify tz to set the timezone.

\>>> pd.date\_range(start\="1/1/2018", periods\=5, tz\="Asia/Tokyo")
DatetimeIndex(\['2018-01-01 00:00:00+09:00', '2018-01-02 00:00:00+09:00',\
               '2018-01-03 00:00:00+09:00', '2018-01-04 00:00:00+09:00',\
               '2018-01-05 00:00:00+09:00'\],
              dtype='datetime64\[us, Asia/Tokyo\]', freq='D')

Copy to clipboard

inclusive controls whether to include start and end that are on the boundary. The default, “both”, includes boundary points on either end.

\>>> pd.date\_range(start\="2017-01-01", end\="2017-01-04", inclusive\="both")
DatetimeIndex(\['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

Use `inclusive='left'` to exclude end if it falls on the boundary.

\>>> pd.date\_range(start\="2017-01-01", end\="2017-01-04", inclusive\="left")
DatetimeIndex(\['2017-01-01', '2017-01-02', '2017-01-03'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

Use `inclusive='right'` to exclude start if it falls on the boundary, and similarly `inclusive='neither'` will exclude both start and end.

\>>> pd.date\_range(start\="2017-01-01", end\="2017-01-04", inclusive\="right")
DatetimeIndex(\['2017-01-02', '2017-01-03', '2017-01-04'\],
              dtype='datetime64\[us\]', freq='D')

Copy to clipboard

**Specify a unit**

\>>> pd.date\_range(start\="2017-01-01", periods\=10, freq\="100YS", unit\="s")
DatetimeIndex(\['2017-01-01', '2117-01-01', '2217-01-01', '2317-01-01',\
               '2417-01-01', '2517-01-01', '2617-01-01', '2717-01-01',\
               '2817-01-01', '2917-01-01'\],
              dtype='datetime64\[s\]', freq='100YS-JAN')

Copy to clipboard

On this page