[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas-period "Link to this heading")

=======================================================================================================================

class pandas.Period(_value\=None_, _freq\=None_, _ordinal\=None_, _year\=None_, _month\=None_, _quarter\=None_, _day\=None_, _hour\=None_, _minute\=None_, _second\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "Link to this definition")

Represents a period of time.

A Period represents a specific time span rather than a point in time. Unlike Timestamp, which represents a single instant, a Period defines a duration, such as a month, quarter, or year. The exact representation is determined by the freq parameter.

Parameters:

**value**Period, str, datetime, date or pandas.Timestamp, default None

The time period represented (e.g., ‘4Q2005’). This represents neither the start or the end of the period, but rather the entire period itself.

**freq**str, default None

One of pandas period strings or corresponding objects. Accepted strings are listed in the [period alias section](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-period-aliases)
 in the user docs. If value is datetime, freq is required.

**ordinal**int, default None

The period offset from the proleptic Gregorian epoch.

**year**int, default None

Year value of the period.

**month**int, default 1

Month value of the period.

**quarter**int, default None

Quarter value of the period.

**day**int, default 1

Day value of the period.

**hour**int, default 0

Hour value of the period.

**minute**int, default 0

Minute value of the period.

**second**int, default 0

Second value of the period.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Pandas replacement for python datetime.datetime object.

[`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")

Return a fixed frequency DatetimeIndex.

[`timedelta_range`](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas.timedelta_range "pandas.timedelta_range")

Generates a fixed frequency range of timedeltas.

Examples

\>>> period \= pd.Period('2012-1-1', freq\='D')
\>>> period
Period('2012-01-01', 'D')

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| [`day`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day.html#pandas.Period.day "pandas.Period.day") | Get day of the month that a Period falls on. |
| [`day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_week.html#pandas.Period.day_of_week "pandas.Period.day_of_week") | Day of the week the period lies in, with Monday=0 and Sunday=6. |
| [`day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.day_of_year.html#pandas.Period.day_of_year "pandas.Period.day_of_year") | Return the day of the year. |
| [`dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofweek.html#pandas.Period.dayofweek "pandas.Period.dayofweek") | (DEPRECATED) Return day of the week. |
| [`dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.dayofyear.html#pandas.Period.dayofyear "pandas.Period.dayofyear") | (DEPRECATED) Return day of the year. |
| [`days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Period.days_in_month.html#pandas.Period.days_in_month "pandas.Period.days_in_month") | Get the total number of days in the month that this period falls on. |
| [`daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.Period.daysinmonth.html#pandas.Period.daysinmonth "pandas.Period.daysinmonth") | (DEPRECATED) Get the total number of days of the month that this period falls on. |
| [`end_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.end_time.html#pandas.Period.end_time "pandas.Period.end_time") | Get the Timestamp for the end of the period. |
| [`freq`](https://pandas.pydata.org/docs/reference/api/pandas.Period.freq.html#pandas.Period.freq "pandas.Period.freq") | Return the frequency object for this Period. |
| [`freqstr`](https://pandas.pydata.org/docs/reference/api/pandas.Period.freqstr.html#pandas.Period.freqstr "pandas.Period.freqstr") | Return a string representation of the frequency. |
| [`hour`](https://pandas.pydata.org/docs/reference/api/pandas.Period.hour.html#pandas.Period.hour "pandas.Period.hour") | Get the hour of the day component of the Period. |
| [`is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.is_leap_year.html#pandas.Period.is_leap_year "pandas.Period.is_leap_year") | Return True if the period's year is in a leap year. |
| [`minute`](https://pandas.pydata.org/docs/reference/api/pandas.Period.minute.html#pandas.Period.minute "pandas.Period.minute") | Get minute of the hour component of the Period. |
| [`month`](https://pandas.pydata.org/docs/reference/api/pandas.Period.month.html#pandas.Period.month "pandas.Period.month") | Return the month this Period falls on. |
| [`ordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Period.ordinal.html#pandas.Period.ordinal "pandas.Period.ordinal") | Return the integer ordinal for this Period. |
| [`quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Period.quarter.html#pandas.Period.quarter "pandas.Period.quarter") | Return the quarter this Period falls on. |
| [`qyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.qyear.html#pandas.Period.qyear "pandas.Period.qyear") | Fiscal year the Period lies in according to its starting-quarter. |
| [`second`](https://pandas.pydata.org/docs/reference/api/pandas.Period.second.html#pandas.Period.second "pandas.Period.second") | Get the second component of the Period. |
| [`start_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#pandas.Period.start_time "pandas.Period.start_time") | Get the Timestamp for the start of the period. |
| [`week`](https://pandas.pydata.org/docs/reference/api/pandas.Period.week.html#pandas.Period.week "pandas.Period.week") | Get the week of the year on the given Period. |
| [`weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekday.html#pandas.Period.weekday "pandas.Period.weekday") | Day of the week the period lies in, with Monday=0 and Sunday=6. |
| [`weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.weekofyear.html#pandas.Period.weekofyear "pandas.Period.weekofyear") | Get the week of the year on the given Period. |
| [`year`](https://pandas.pydata.org/docs/reference/api/pandas.Period.year.html#pandas.Period.year "pandas.Period.year") | Return the year this Period falls on. |

Methods

|     |     |
| --- | --- |
| [`asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#pandas.Period.asfreq "pandas.Period.asfreq")<br>(freq\[, how\]) | Convert Period to desired frequency, at the start or end of the interval. |
| [`now`](https://pandas.pydata.org/docs/reference/api/pandas.Period.now.html#pandas.Period.now "pandas.Period.now")<br>(freq) | Return the period of now's date. |
| [`strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#pandas.Period.strftime "pandas.Period.strftime")<br>(fmt) | (DEPRECATED) Returns a formatted string representation of the [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")<br>. |
| [`to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Period.to_timestamp.html#pandas.Period.to_timestamp "pandas.Period.to_timestamp")<br>(\[freq, how\]) | Return the Timestamp representation of the Period. |

On this page