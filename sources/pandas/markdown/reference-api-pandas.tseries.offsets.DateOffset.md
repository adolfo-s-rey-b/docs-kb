[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.DateOffset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas-tseries-offsets-dateoffset "Link to this heading")

===================================================================================================================================================================================

class pandas.tseries.offsets.DateOffset[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "Link to this definition")

Standard kind of date increment used for a date range.

Works exactly like the keyword argument form of relativedelta. Note that the positional argument form of relativedelta is not supported. Use of the keyword n is discouraged– you would be better off specifying n in the keywords you use, but regardless it is there for you. n is needed for DateOffset subclasses.

DateOffset works as follows. Each offset specify a set of dates that conform to the DateOffset. For example, Bday defines this set to be the set of dates that are weekdays (M-F). To test if a date is in the set of a DateOffset dateOffset we can use the is\_on\_offset method: dateOffset.is\_on\_offset(date).

If a date is not on a valid date, the rollback and rollforward methods can be used to roll the date to the nearest valid date before/after the date.

DateOffsets can be created to move dates forward a given number of valid dates. For example, Bday(2) can be added to a date to move it two business days forward. If the date does not start on a valid date, it is first rolled forward to the next valid date, and that roll counts as the first of the n increments. For example, 2014-08-31 is a Sunday, so `Timestamp("2014-08-31") + BDay(1)` only rolls forward to Monday 2014-09-01, and adding `BDay(2)` gives Tuesday 2014-09-02. Equivalently, the date is first rolled back to the previous valid date, then moved n valid dates forward. Thus pseudo code is:

def \_\_add\_\_(date):
  date \= rollback(date) \# does nothing if date is valid
  return date + <n number of periods\>

Copy to clipboard

When a date offset is created for a negative number of periods, the roll is symmetric: rolling back to the previous valid date counts as the first decrement; equivalently, the date is first rolled forward, then moved `abs(n)` valid dates backward. The pseudo code is:

def \_\_add\_\_(date):
  date \= rollforward(date) \# does nothing if date is valid
  return date + <n number of periods\>

Copy to clipboard

Zero presents a problem. Should it roll forward or back? We arbitrarily have it rollforward:

date + BDay(0) == BDay.rollforward(date)

Since 0 is a bit weird, we suggest avoiding its use. Because the roll counts as an increment, `date + BDay(0)` and `date + BDay(1)` give the same result when date is not a business day.

Besides, adding a DateOffsets specified by the singular form of the date component can be used to replace certain component of the timestamp.

Parameters:

**n**int, default 1

The number of time periods the offset represents. If specified without a temporal pattern, defaults to n days.

**normalize**bool, default False

Whether to round the result of a DateOffset addition down to the previous midnight.

**weekday**int {0, 1, …, 6}, default 0

A specific integer for the day of the week.

*   0 is Monday
    
*   1 is Tuesday
    
*   2 is Wednesday
    
*   3 is Thursday
    
*   4 is Friday
    
*   5 is Saturday
    
*   6 is Sunday
    

Instead Weekday type from dateutil.relativedelta can be used.

*   MO is Monday
    
*   TU is Tuesday
    
*   WE is Wednesday
    
*   TH is Thursday
    
*   FR is Friday
    
*   SA is Saturday
    
*   SU is Sunday.
    

**\*\*kwds**

Temporal parameter that add to or replace the offset value.

Parameters that **add** to the offset (like Timedelta):

*   years
    
*   months
    
*   weeks
    
*   days
    
*   hours
    
*   minutes
    
*   seconds
    
*   milliseconds
    
*   microseconds
    
*   nanoseconds
    

Parameters that **replace** the offset value:

*   year
    
*   month
    
*   day
    
*   weekday
    
*   hour
    
*   minute
    
*   second
    
*   microsecond
    
*   nanosecond.
    

See also

[`BaseOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.html#pandas.tseries.offsets.BaseOffset "pandas.tseries.offsets.BaseOffset")

Base class of all offset types.

[`dateutil.relativedelta.relativedelta`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.relativedelta "(in Matplotlib v3.11.2)")

The relativedelta type is designed to be applied to an existing datetime and can replace specific components of that datetime, or represents an interval of time.

Notes

When added to a `DatetimeIndex` or datetime `Series`, a `DateOffset` is applied to each entry independently. Calendar components such as `months` and `years` do not represent a fixed duration, so evenly spaced input dates are not guaranteed to remain evenly spaced: dates that would fall on a nonexistent day are clamped to the end of the month. For example, adding `DateOffset(months=1)` to both `2018-01-30` and `2018-01-31` yields `2018-02-28` in each case.

Examples

\>>> from pandas.tseries.offsets import DateOffset
\>>> ts \= pd.Timestamp('2017-01-01 09:10:11')
\>>> ts + DateOffset(months\=3)
Timestamp('2017-04-01 09:10:11')

Copy to clipboard

\>>> ts \= pd.Timestamp('2017-01-01 09:10:11')
\>>> ts + DateOffset(months\=2)
Timestamp('2017-03-01 09:10:11')
\>>> ts + DateOffset(day\=31)
Timestamp('2017-01-31 09:10:11')

Copy to clipboard

\>>> ts + pd.DateOffset(hour\=8)
Timestamp('2017-01-01 08:10:11')

Copy to clipboard

On this page