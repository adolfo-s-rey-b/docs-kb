[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BusinessDay[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas-tseries-offsets-businessday "Link to this heading")

======================================================================================================================================================================================

class pandas.tseries.offsets.BusinessDay(_n\=1_, _normalize\=False_, _offset\=datetime.timedelta(0)_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay "Link to this definition")

DateOffset subclass representing possibly n business days.

BusinessDay, also known as BDay, is a date offset representing a single business day or a number of business days. Business days exclude weekends (Saturday and Sunday) by default.

Parameters:

**n**int, default 1

The number of days represented.

**normalize**bool, default False

Normalize start/end dates to midnight.

**offset**timedelta, default timedelta(0)

Additional time offset applied after the business day calculation.

Attributes

|     |     |
| --- | --- |
| [`offset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.offset.html#pandas.tseries.offsets.BusinessDay.offset "pandas.tseries.offsets.BusinessDay.offset") | Return the time offset applied to the business day. |
| [`holidays`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.holidays.html#pandas.tseries.offsets.BusinessDay.holidays "pandas.tseries.offsets.BusinessDay.holidays") | Return the holidays used for custom business day calculations. |
| [`calendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.calendar.html#pandas.tseries.offsets.BusinessDay.calendar "pandas.tseries.offsets.BusinessDay.calendar") | Return the calendar used for business day calculations. |
| [`weekmask`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.weekmask.html#pandas.tseries.offsets.BusinessDay.weekmask "pandas.tseries.offsets.BusinessDay.weekmask") | Return the weekmask used for custom business day calculations. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

You can use the parameter `n` to represent a shift of n business days.

\>>> ts \= pd.Timestamp(2022, 12, 9, 15)
\>>> ts.strftime('%a %d %b %Y %H:%M')
'Fri 09 Dec 2022 15:00'
\>>> (ts + pd.offsets.BusinessDay(n\=5)).strftime('%a %d %b %Y %H:%M')
'Fri 16 Dec 2022 15:00'

Copy to clipboard

Passing the parameter `normalize` equal to True, you shift the start of the next business day to midnight.

\>>> ts \= pd.Timestamp(2022, 12, 9, 15)
\>>> ts + pd.offsets.BusinessDay(normalize\=True)
Timestamp('2022-12-12 00:00:00')

Copy to clipboard

On this page