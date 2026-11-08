[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.holiday.Holiday[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.html#pandas-tseries-holiday-holiday "Link to this heading")

==========================================================================================================================================================================

class pandas.tseries.holiday.Holiday(_name_, _year\=None_, _month\=None_, _day\=None_, _offset\=None_, _observance\=None_, _start\_date\=None_, _end\_date\=None_, _days\_of\_week\=None_, _exclude\_dates\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/tseries/holiday.py#L450-L753)
[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.html#pandas.tseries.holiday.Holiday "Link to this definition")

Class that defines a holiday with start/end dates and rules for observance.

A `Holiday` can either be defined by a fixed `year`/`month`/`day`, or, more commonly, by a recurring `month`/`day` combined with an `offset` or `observance` rule that adjusts the date in each year it is calculated for. Instances of `Holiday` are typically collected in the `rules` of an [`AbstractHolidayCalendar`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.AbstractHolidayCalendar.html#pandas.tseries.holiday.AbstractHolidayCalendar "pandas.tseries.holiday.AbstractHolidayCalendar")
.

Parameters:

**name**str

Name of the holiday, defaults to class name.

**year**int, default None

Year of the holiday.

**month**int, default None

Month of the holiday.

**day**int, default None

Day of the holiday.

**offset**DateOffset or list of DateOffset, default None

Computes offset from date. See `pandas.tseries.offsets` for the available offset classes.

**observance**function, default None

Computes when holiday is given a pandas Timestamp.

**start\_date**datetime-like, default None

First date the holiday is observed.

**end\_date**datetime-like, default None

Last date the holiday is observed.

**days\_of\_week**tuple of int or dateutil.relativedelta weekday strs, default None

Provide a tuple of days e.g (0,1,2,3,) for Monday through Thursday Monday=0,..,Sunday=6 Only instances of the holiday included in days\_of\_week will be computed.

**exclude\_dates**DatetimeIndex or default None

Specific dates to exclude e.g. skipping a specific year’s holiday.

See also

`tseries.holiday.AbstractHolidayCalendar`

Abstract interface to create holidays following certain rules.

`tseries.holiday.Holiday.dates`

Calculate holidays observed between start date and end date.

Examples

\>>> from dateutil.relativedelta import MO

Copy to clipboard

\>>> USMemorialDay \= pd.tseries.holiday.Holiday(
...     "Memorial Day", month\=5, day\=31, offset\=pd.DateOffset(weekday\=MO(\-1))
... )
\>>> USMemorialDay
Holiday: Memorial Day (month=5, day=31, offset=<DateOffset: weekday=MO(-1)>)

Copy to clipboard

\>>> USLaborDay \= pd.tseries.holiday.Holiday(
...     "Labor Day", month\=9, day\=1, offset\=pd.DateOffset(weekday\=MO(1))
... )
\>>> USLaborDay
Holiday: Labor Day (month=9, day=1, offset=<DateOffset: weekday=MO(+1)>)

Copy to clipboard

\>>> July3rd \= pd.tseries.holiday.Holiday("July 3rd", month\=7, day\=3)
\>>> July3rd
Holiday: July 3rd (month=7, day=3, )

Copy to clipboard

\>>> NewYears \= pd.tseries.holiday.Holiday(
...     "New Years Day",
...     month\=1,
...     day\=1,
...     observance\=pd.tseries.holiday.nearest\_workday,
... )
\>>> NewYears
Holiday: New Years Day (
    month=1, day=1, observance=<function nearest\_workday at 0x66545e9bc440>
)

Copy to clipboard

\>>> July3rd \= pd.tseries.holiday.Holiday(
...     "July 3rd", month\=7, day\=3, days\_of\_week\=(0, 1, 2, 3)
... )
\>>> July3rd
Holiday: July 3rd (month=7, day=3, )

Copy to clipboard

Attributes

Methods

|     |     |
| --- | --- |
| [`dates`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.holiday.Holiday.dates.html#pandas.tseries.holiday.Holiday.dates "pandas.tseries.holiday.Holiday.dates")<br>(start\_date, end\_date\[, return\_name\]) | Calculate holidays observed between start date and end date. |

On this page