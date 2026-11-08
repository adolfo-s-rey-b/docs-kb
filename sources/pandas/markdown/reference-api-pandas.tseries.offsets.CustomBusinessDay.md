[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.CustomBusinessDay[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#pandas-tseries-offsets-custombusinessday "Link to this heading")

========================================================================================================================================================================================================

class pandas.tseries.offsets.CustomBusinessDay(_n\=1_, _normalize\=False_, _weekmask\='Mon Tue Wed Thu Fri'_, _holidays\=None_, _calendar\=None_, _offset\=datetime.timedelta(0)_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html#pandas.tseries.offsets.CustomBusinessDay "Link to this definition")

DateOffset subclass representing possibly n custom business days.

In CustomBusinessDay we can use custom weekmask, holidays, and calendar.

Parameters:

**n**int, default 1

The number of days represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**weekmask**str, Default ‘Mon Tue Wed Thu Fri’

Weekmask of valid business days, passed to `numpy.busdaycalendar`.

**holidays**list

List/array of dates to exclude from the set of valid business days, passed to `numpy.busdaycalendar`.

**calendar**np.busdaycalendar

Calendar to integrate.

**offset**timedelta, default timedelta(0)

Time offset to apply.

Attributes

|     |     |
| --- | --- |
| [`weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.weekmask.html#pandas.tseries.offsets.CustomBusinessDay.weekmask "pandas.tseries.offsets.CustomBusinessDay.weekmask") | Return the weekmask used for custom business day calculations. |
| [`holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.holidays.html#pandas.tseries.offsets.CustomBusinessDay.holidays "pandas.tseries.offsets.CustomBusinessDay.holidays") | Return the holidays used for custom business day calculations. |
| [`calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.calendar.html#pandas.tseries.offsets.CustomBusinessDay.calendar "pandas.tseries.offsets.CustomBusinessDay.calendar") | Return the calendar used for business day calculations. |
| [`offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.offset.html#pandas.tseries.offsets.CustomBusinessDay.offset "pandas.tseries.offsets.CustomBusinessDay.offset") | Return the time offset applied to the business day. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

In the example below the default parameters give the next business day.

\>>> ts \= pd.Timestamp(2022, 8, 5, 16)
\>>> ts + pd.offsets.CustomBusinessDay()
Timestamp('2022-08-08 16:00:00')

Copy to clipboard

Business days can be specified by `weekmask` parameter. To convert the returned datetime object to its string representation the function strftime() is used in the next example.

\>>> import datetime as dt
\>>> freq \= pd.offsets.CustomBusinessDay(weekmask\="Mon Wed Fri")
\>>> pd.date\_range(dt.datetime(2022, 12, 10), dt.datetime(2022, 12, 21),
...               freq\=freq).strftime('%a %d %b %Y %H:%M')
Index(\['Mon 12 Dec 2022 00:00', 'Wed 14 Dec 2022 00:00',\
       'Fri 16 Dec 2022 00:00', 'Mon 19 Dec 2022 00:00',\
       'Wed 21 Dec 2022 00:00'\],
       dtype='str')

Copy to clipboard

Using NumPy business day calendar you can define custom holidays.

\>>> import datetime as dt
\>>> bdc \= np.busdaycalendar(holidays\=\['2022-12-12', '2022-12-14'\])
\>>> freq \= pd.offsets.CustomBusinessDay(calendar\=bdc)
\>>> pd.date\_range(dt.datetime(2022, 12, 10), dt.datetime(2022, 12, 25), freq\=freq)
DatetimeIndex(\['2022-12-13', '2022-12-15', '2022-12-16', '2022-12-19',\
               '2022-12-20', '2022-12-21', '2022-12-22', '2022-12-23'\],
               dtype='datetime64\[us\]', freq='C')

Copy to clipboard

If you want to shift the result on n day you can use the parameter `offset`.

\>>> pd.Timestamp(2022, 8, 5, 16) + pd.offsets.CustomBusinessDay(1)
Timestamp('2022-08-08 16:00:00')

Copy to clipboard

\>>> import datetime as dt
\>>> ts \= pd.Timestamp(2022, 8, 5, 16)
\>>> ts + pd.offsets.CustomBusinessDay(1, offset\=dt.timedelta(days\=1))
Timestamp('2022-08-09 16:00:00')

Copy to clipboard

On this page