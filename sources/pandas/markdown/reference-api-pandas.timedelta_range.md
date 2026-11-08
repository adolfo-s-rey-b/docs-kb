[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.timedelta_range.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.timedelta_range.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.timedelta_range.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.timedelta_range.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.timedelta_range.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.timedelta_range.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.timedelta_range.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.timedelta_range.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.timedelta_range.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.timedelta_range.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.timedelta_range.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.timedelta_range.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.timedelta\_range[#](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas-timedelta-range "Link to this heading")

===================================================================================================================================================

pandas.timedelta\_range(_start\=None_, _end\=None_, _periods\=None_, _freq\=None_, _name\=None_, _closed\=None_, _\*_, _unit\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/timedeltas.py#L936-L1079)
[#](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas.timedelta_range "Link to this definition")

Return a fixed frequency TimedeltaIndex with day as the default.

This function generates a sequence of evenly spaced timedelta values between the specified bounds, using day as the default frequency.

Parameters:

**start**str or timedelta-like, default None

Left bound for generating timedeltas.

**end**str or timedelta-like, default None

Right bound for generating timedeltas.

**periods**int, default None

Number of periods to generate.

**freq**str, Timedelta, datetime.timedelta, or DateOffset, default ‘D’

Frequency strings can have multiples, e.g. ‘5h’.

**name**Hashable, default None

Name of the resulting TimedeltaIndex.

**closed**str, default None

Make the interval closed with respect to the given frequency to the ‘left’, ‘right’, or both sides (None).

**unit**{‘s’, ‘ms’, ‘us’, ‘ns’, None}, default None

Specify the desired resolution of the result. If not specified, this is inferred from the ‘start’, ‘end’, and ‘freq’ using the same inference as [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
 taking the highest resolution of the three that are provided.

Added in version 2.0.0.

Returns:

TimedeltaIndex

Fixed frequency, with day as the default.

See also

[`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")

Return a fixed frequency DatetimeIndex.

[`period_range`](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas.period_range "pandas.period_range")

Return a fixed frequency PeriodIndex.

Notes

Of the four parameters `start`, `end`, `periods`, and `freq`, a maximum of three can be specified at once. Of the three parameters `start`, `end`, and `periods`, at least two must be specified. If `freq` is omitted, the resulting `DatetimeIndex` will have `periods` linearly spaced elements between `start` and `end` (closed on both sides).

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

Examples

\>>> pd.timedelta\_range(start\="1 day", periods\=4)
TimedeltaIndex(\['1 days', '2 days', '3 days', '4 days'\],
               dtype='timedelta64\[us\]', freq='D')

Copy to clipboard

The `closed` parameter specifies which endpoint is included. The default behavior is to include both endpoints.

\>>> pd.timedelta\_range(start\="1 day", periods\=4, closed\="right")
TimedeltaIndex(\['2 days', '3 days', '4 days'\],
               dtype='timedelta64\[us\]', freq='D')

Copy to clipboard

The `freq` parameter specifies the frequency of the TimedeltaIndex. Only fixed frequencies can be passed, non-fixed frequencies such as ‘M’ (month end) will raise.

\>>> pd.timedelta\_range(start\="1 day", end\="2 days", freq\="6h")
TimedeltaIndex(\['1 days 00:00:00', '1 days 06:00:00', '1 days 12:00:00',\
                '1 days 18:00:00', '2 days 00:00:00'\],
               dtype='timedelta64\[us\]', freq='6h')

Copy to clipboard

Specify `start`, `end`, and `periods`; the frequency is generated automatically (linearly spaced).

\>>> pd.timedelta\_range(start\="1 day", end\="5 days", periods\=4)
TimedeltaIndex(\['1 days 00:00:00', '2 days 08:00:00', '3 days 16:00:00',\
                '5 days 00:00:00'\],
               dtype='timedelta64\[us\]', freq=None)

Copy to clipboard

**Specify a unit**

\>>> pd.timedelta\_range("1 Day", periods\=3, freq\="100000D", unit\="s")
TimedeltaIndex(\['1 days', '100001 days', '200001 days'\],
               dtype='timedelta64\[s\]', freq='100000D')

Copy to clipboard

On this page