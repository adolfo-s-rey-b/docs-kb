[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.CustomBusinessMonthBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html#pandas-tseries-offsets-custombusinessmonthbegin "Link to this heading")

=============================================================================================================================================================================================================================

class pandas.tseries.offsets.CustomBusinessMonthBegin(_n\=1_, _normalize\=False_, _weekmask\='Mon Tue Wed Thu Fri'_, _holidays\=None_, _calendar\=None_, _offset\=datetime.timedelta(0)_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.html#pandas.tseries.offsets.CustomBusinessMonthBegin "Link to this definition")

DateOffset subclass representing custom business month(s).

Increments between beginning of month dates.

Parameters:

**n**int, default 1

The number of months represented.

**normalize**bool, default False

Normalize start dates to midnight before generating date range.

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
| [`m_offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset.html#pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset "pandas.tseries.offsets.CustomBusinessMonthBegin.m_offset") | Return a MonthBegin or MonthEnd offset. |
| [`weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.weekmask.html#pandas.tseries.offsets.CustomBusinessMonthBegin.weekmask "pandas.tseries.offsets.CustomBusinessMonthBegin.weekmask") | Return the weekmask used for custom business day calculations. |
| [`holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.holidays.html#pandas.tseries.offsets.CustomBusinessMonthBegin.holidays "pandas.tseries.offsets.CustomBusinessMonthBegin.holidays") | Return the holidays used for custom business day calculations. |
| [`calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.calendar.html#pandas.tseries.offsets.CustomBusinessMonthBegin.calendar "pandas.tseries.offsets.CustomBusinessMonthBegin.calendar") | Return the calendar used for business day calculations. |
| [`offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessMonthBegin.offset.html#pandas.tseries.offsets.CustomBusinessMonthBegin.offset "pandas.tseries.offsets.CustomBusinessMonthBegin.offset") | Return the time offset applied to the business day. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

In the example below we use the default parameters.

\>>> ts \= pd.Timestamp(2022, 8, 5)
\>>> ts + pd.offsets.CustomBusinessMonthBegin()
Timestamp('2022-09-01 00:00:00')

Copy to clipboard

Custom business month start can be specified by `weekmask` parameter. To convert the returned datetime object to its string representation the function strftime() is used in the next example.

\>>> import datetime as dt
\>>> freq \= pd.offsets.CustomBusinessMonthBegin(weekmask\="Wed Thu")
\>>> pd.date\_range(dt.datetime(2022, 7, 10), dt.datetime(2022, 12, 18),
...               freq\=freq).strftime('%a %d %b %Y %H:%M')
Index(\['Wed 03 Aug 2022 00:00', 'Thu 01 Sep 2022 00:00',\
       'Wed 05 Oct 2022 00:00', 'Wed 02 Nov 2022 00:00',\
       'Thu 01 Dec 2022 00:00'\],
       dtype='str')

Copy to clipboard

Using NumPy business day calendar you can define custom holidays.

\>>> import datetime as dt
\>>> bdc \= np.busdaycalendar(holidays\=\['2022-08-01', '2022-09-30',\
...                                   '2022-10-31', '2022-11-01'\])
\>>> freq \= pd.offsets.CustomBusinessMonthBegin(calendar\=bdc)
\>>> pd.date\_range(dt.datetime(2022, 7, 10), dt.datetime(2022, 11, 10), freq\=freq)
DatetimeIndex(\['2022-08-02', '2022-09-01', '2022-10-03', '2022-11-02'\],
               dtype='datetime64\[us\]', freq='CBMS')

Copy to clipboard

On this page