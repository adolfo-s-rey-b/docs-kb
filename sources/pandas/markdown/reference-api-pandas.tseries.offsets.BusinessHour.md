[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BusinessHour.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BusinessHour.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BusinessHour.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BusinessHour.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BusinessHour.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BusinessHour.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BusinessHour.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BusinessHour.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BusinessHour.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BusinessHour.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BusinessHour.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BusinessHour.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BusinessHour[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html#pandas-tseries-offsets-businesshour "Link to this heading")

=========================================================================================================================================================================================

class pandas.tseries.offsets.BusinessHour[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html#pandas.tseries.offsets.BusinessHour "Link to this definition")

DateOffset subclass representing possibly n business hours.

BusinessHour is a date offset that advances time by a number of business hours. By default, business hours are from 9:00 AM to 5:00 PM on weekdays. The `start` and `end` parameters can be used to customize the business hours window, and multiple intervals can be specified by passing lists.

Parameters:

**n**int, default 1

The number of hours represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**start**str, time, or list of str/time, default “09:00”

Start time of your custom business hour in 24h format.

**end**str, time, or list of str/time, default: “17:00”

End time of your custom business hour in 24h format.

**offset**timedelta, default timedelta(0)

Time offset to apply.

Attributes

|     |     |
| --- | --- |
| [`offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.offset.html#pandas.tseries.offsets.BusinessHour.offset "pandas.tseries.offsets.BusinessHour.offset") | Return the time offset applied to the business day. |
| [`holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.holidays.html#pandas.tseries.offsets.BusinessHour.holidays "pandas.tseries.offsets.BusinessHour.holidays") | Return the holidays used for custom business day calculations. |
| [`calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.calendar.html#pandas.tseries.offsets.BusinessHour.calendar "pandas.tseries.offsets.BusinessHour.calendar") | Return the calendar used for business day calculations. |
| [`weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.weekmask.html#pandas.tseries.offsets.BusinessHour.weekmask "pandas.tseries.offsets.BusinessHour.weekmask") | Return the weekmask used for custom business day calculations. |
| [`start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.start.html#pandas.tseries.offsets.BusinessHour.start "pandas.tseries.offsets.BusinessHour.start") | Return the start time(s) of the business hour. |
| [`end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.end.html#pandas.tseries.offsets.BusinessHour.end "pandas.tseries.offsets.BusinessHour.end") | Return the end time(s) of the business hour. |

See also

[`CustomBusinessHour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.html#pandas.tseries.offsets.CustomBusinessHour "pandas.tseries.offsets.CustomBusinessHour")

DateOffset subclass with custom weekmask and holidays.

[`BusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay "pandas.tseries.offsets.BusinessDay")

DateOffset subclass representing possibly n business days.

Examples

You can use the parameter `n` to represent a shift of n hours.

\>>> ts \= pd.Timestamp(2022, 12, 9, 8)
\>>> ts + pd.offsets.BusinessHour(n\=5)
Timestamp('2022-12-09 14:00:00')

Copy to clipboard

You can also change the start and the end of business hours.

\>>> ts \= pd.Timestamp(2022, 8, 5, 16)
\>>> ts + pd.offsets.BusinessHour(start\="11:00")
Timestamp('2022-08-08 11:00:00')

Copy to clipboard

\>>> from datetime import time as dt\_time
\>>> ts \= pd.Timestamp(2022, 8, 5, 22)
\>>> ts + pd.offsets.BusinessHour(end\=dt\_time(19, 0))
Timestamp('2022-08-08 10:00:00')

Copy to clipboard

Passing the parameter `normalize` equal to True, you shift the start of the next business hour to midnight.

\>>> ts \= pd.Timestamp(2022, 12, 9, 8)
\>>> ts + pd.offsets.BusinessHour(normalize\=True)
Timestamp('2022-12-09 00:00:00')

Copy to clipboard

You can divide your business day hours into several parts.

\>>> import datetime as dt
\>>> freq \= pd.offsets.BusinessHour(start\=\["06:00", "10:00", "15:00"\],
...                                end\=\["08:00", "12:00", "17:00"\])
\>>> pd.date\_range(dt.datetime(2022, 12, 9), dt.datetime(2022, 12, 13), freq\=freq)
DatetimeIndex(\['2022-12-09 06:00:00', '2022-12-09 07:00:00',\
               '2022-12-09 10:00:00', '2022-12-09 11:00:00',\
               '2022-12-09 15:00:00', '2022-12-09 16:00:00',\
               '2022-12-12 06:00:00', '2022-12-12 07:00:00',\
               '2022-12-12 10:00:00', '2022-12-12 11:00:00',\
               '2022-12-12 15:00:00', '2022-12-12 16:00:00'\],
               dtype='datetime64\[us\]', freq='bh')

Copy to clipboard

On this page