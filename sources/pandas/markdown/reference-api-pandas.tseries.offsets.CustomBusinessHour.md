[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.CustomBusinessHour.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.CustomBusinessHour[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.html#pandas-tseries-offsets-custombusinesshour "Link to this heading")

===========================================================================================================================================================================================================

class pandas.tseries.offsets.CustomBusinessHour[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.html#pandas.tseries.offsets.CustomBusinessHour "Link to this definition")

DateOffset subclass representing possibly n custom business days.

In CustomBusinessHour we can use custom weekmask, holidays, and calendar.

Parameters:

**n**int, default 1

The number of hours represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**weekmask**str, Default ‘Mon Tue Wed Thu Fri’

Weekmask of valid business days, passed to `numpy.busdaycalendar`.

**holidays**list

List/array of dates to exclude from the set of valid business days, passed to `numpy.busdaycalendar`.

**calendar**np.busdaycalendar

Calendar to integrate.

**start**str, time, or list of str/time, default “09:00”

Start time of your custom business hour in 24h format.

**end**str, time, or list of str/time, default: “17:00”

End time of your custom business hour in 24h format.

**offset**timedelta, default timedelta(0)

Time offset to apply.

Attributes

|     |     |
| --- | --- |
| [`weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.weekmask.html#pandas.tseries.offsets.CustomBusinessHour.weekmask "pandas.tseries.offsets.CustomBusinessHour.weekmask") | Return the weekmask used for custom business day calculations. |
| [`holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.holidays.html#pandas.tseries.offsets.CustomBusinessHour.holidays "pandas.tseries.offsets.CustomBusinessHour.holidays") | Return the holidays used for custom business day calculations. |
| [`calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.calendar.html#pandas.tseries.offsets.CustomBusinessHour.calendar "pandas.tseries.offsets.CustomBusinessHour.calendar") | Return the calendar used for business day calculations. |
| [`start`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.start.html#pandas.tseries.offsets.CustomBusinessHour.start "pandas.tseries.offsets.CustomBusinessHour.start") | Return the start time(s) of the business hour. |
| [`end`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.end.html#pandas.tseries.offsets.CustomBusinessHour.end "pandas.tseries.offsets.CustomBusinessHour.end") | Return the end time(s) of the business hour. |
| [`offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessHour.offset.html#pandas.tseries.offsets.CustomBusinessHour.offset "pandas.tseries.offsets.CustomBusinessHour.offset") | Return the time offset applied to the business day. |

See also

[`BusinessHour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessHour.html#pandas.tseries.offsets.BusinessHour "pandas.tseries.offsets.BusinessHour")

DateOffset subclass representing possibly n business hours.

[`CustomBusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#pandas.tseries.offsets.CustomBusinessDay "pandas.tseries.offsets.CustomBusinessDay")

DateOffset subclass representing custom business days.

Examples

In the example below the default parameters give the next business hour.

\>>> ts \= pd.Timestamp(2022, 8, 5, 16)
\>>> ts + pd.offsets.CustomBusinessHour()
Timestamp('2022-08-08 09:00:00')

Copy to clipboard

We can also change the start and the end of business hours.

\>>> ts \= pd.Timestamp(2022, 8, 5, 16)
\>>> ts + pd.offsets.CustomBusinessHour(start\="11:00")
Timestamp('2022-08-08 11:00:00')

Copy to clipboard

\>>> from datetime import time as dt\_time
\>>> ts \= pd.Timestamp(2022, 8, 5, 16)
\>>> ts + pd.offsets.CustomBusinessHour(end\=dt\_time(19, 0))
Timestamp('2022-08-05 17:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 8, 5, 22)
\>>> ts + pd.offsets.CustomBusinessHour(end\=dt\_time(19, 0))
Timestamp('2022-08-08 10:00:00')

Copy to clipboard

You can divide your business day hours into several parts.

\>>> import datetime as dt
\>>> freq \= pd.offsets.CustomBusinessHour(start\=\["06:00", "10:00", "15:00"\],
...                                      end\=\["08:00", "12:00", "17:00"\])
\>>> pd.date\_range(dt.datetime(2022, 12, 9), dt.datetime(2022, 12, 13), freq\=freq)
DatetimeIndex(\['2022-12-09 06:00:00', '2022-12-09 07:00:00',\
               '2022-12-09 10:00:00', '2022-12-09 11:00:00',\
               '2022-12-09 15:00:00', '2022-12-09 16:00:00',\
               '2022-12-12 06:00:00', '2022-12-12 07:00:00',\
               '2022-12-12 10:00:00', '2022-12-12 11:00:00',\
               '2022-12-12 15:00:00', '2022-12-12 16:00:00'\],
               dtype='datetime64\[us\]', freq='cbh')

Copy to clipboard

Business days can be specified by `weekmask` parameter. To convert the returned datetime object to its string representation the function strftime() is used in the next example.

\>>> import datetime as dt
\>>> freq \= pd.offsets.CustomBusinessHour(weekmask\="Mon Wed Fri",
...                                      start\="10:00", end\="13:00")
\>>> pd.date\_range(dt.datetime(2022, 12, 10), dt.datetime(2022, 12, 18),
...               freq\=freq).strftime('%a %d %b %Y %H:%M')
Index(\['Mon 12 Dec 2022 10:00', 'Mon 12 Dec 2022 11:00',\
       'Mon 12 Dec 2022 12:00', 'Wed 14 Dec 2022 10:00',\
       'Wed 14 Dec 2022 11:00', 'Wed 14 Dec 2022 12:00',\
       'Fri 16 Dec 2022 10:00', 'Fri 16 Dec 2022 11:00',\
       'Fri 16 Dec 2022 12:00'\],
       dtype='str')

Copy to clipboard

Using NumPy business day calendar you can define custom holidays.

\>>> import datetime as dt
\>>> bdc \= np.busdaycalendar(holidays\=\['2022-12-12', '2022-12-14'\])
\>>> freq \= pd.offsets.CustomBusinessHour(calendar\=bdc, start\="10:00", end\="13:00")
\>>> pd.date\_range(dt.datetime(2022, 12, 10), dt.datetime(2022, 12, 18), freq\=freq)
DatetimeIndex(\['2022-12-13 10:00:00', '2022-12-13 11:00:00',\
               '2022-12-13 12:00:00', '2022-12-15 10:00:00',\
               '2022-12-15 11:00:00', '2022-12-15 12:00:00',\
               '2022-12-16 10:00:00', '2022-12-16 11:00:00',\
               '2022-12-16 12:00:00'\],
               dtype='datetime64\[us\]', freq='cbh')

Copy to clipboard

On this page