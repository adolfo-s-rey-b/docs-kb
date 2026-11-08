[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas-timestamp "Link to this heading")

================================================================================================================================

class pandas.Timestamp(_ts\_input\=<object object>_, _year\=None_, _month\=None_, _day\=None_, _hour\=None_, _minute\=None_, _second\=None_, _microsecond\=None_, _tzinfo\=None_, _\*_, _nanosecond\=None_, _tz\=<object object>_, _unit\=None_, _fold\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "Link to this definition")

Pandas replacement for python datetime.datetime object.

Timestamp is the pandas equivalent of python’s Datetime and is interchangeable with it in most cases. It’s the type used for the entries that make up a DatetimeIndex, and other timeseries oriented data structures in pandas.

Parameters:

**ts\_input**datetime-like, str, int, float

Value to be converted to Timestamp.

**year**int

Value of year.

**month**int

Value of month.

**day**int

Value of day.

**hour**int, optional, default 0

Value of hour.

**minute**int, optional, default 0

Value of minute.

**second**int, optional, default 0

Value of second.

**microsecond**int or datetime.tzinfo, optional, default 0

Value of microsecond. In the `datetime.datetime`\-like positional form this is instead `datetime.datetime`’s `tzinfo`; see Notes.

**tzinfo**datetime.tzinfo, optional, default None

Timezone info.

**nanosecond**int, optional, default 0

Value of nanosecond.

**tz**str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None

Time zone for time which Timestamp will have.

**unit**str

Unit used for conversion if ts\_input is of type int or float. The valid values are ‘W’, ‘D’, ‘h’, ‘m’, ‘s’, ‘ms’, ‘us’, and ‘ns’. For example, ‘s’ means seconds and ‘ms’ means milliseconds.

For float inputs, the result will be stored in nanoseconds, and the unit attribute will be set as `'ns'`.

**fold**{0, 1}, default None, keyword-only

Due to daylight saving time, one wall clock time can occur twice when shifting from summer to winter time; fold describes whether the datetime-like corresponds to the first (0) or the second time (1) the wall clock hits the ambiguous time.

See also

[`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")

Represents a duration, the difference between two dates or times.

[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")

Python datetime.datetime object.

Notes

There are essentially three calling conventions for the constructor. In the primary form the only positional parameter is the value to convert, `ts_input`; `nanosecond`, `tz`, `unit` and `fold` are keyword-only.

The other two forms mimic the parameters from `datetime.datetime`. They can be passed by either position or keyword, but not both mixed together.

In the positional `datetime.datetime`\-like form each parameter stands in for the _next_ `datetime.datetime` field, so the eighth argument – whether passed positionally or as `microsecond=` – is `datetime.datetime`’s `tzinfo`. It is attached to the result as-is, just as `datetime.datetime` does, unlike the `tz` and `tzinfo` keywords which localize.

Mixing a value to convert with the by-component arguments raises `ValueError`, except in two cases that cannot be detected. An `int` first argument is indistinguishable from a `year`, so `Timestamp(2020, year=1, month=1)` is read as `Timestamp(2020, 1, 1)`; and a keyword filling the next free positional slot is indistinguishable from passing it positionally, so `Timestamp(2020, 12, 31, day=5)` is read as `Timestamp(2020, 12, 31, 5)`. Null-like input is exempt from the check altogether: `Timestamp(NaT, hour=5)` and friends give `NaT`.

`nanosecond` is outside the check: it is honored alongside a `datetime`/`Timestamp` value, rejected alongside a string, and silently ignored alongside a `date`, `numpy.datetime64`, `int` or `float`.

Examples

Using the primary calling convention:

This converts a datetime-like string

\>>> pd.Timestamp('2017-01-01T12')
Timestamp('2017-01-01 12:00:00')

Copy to clipboard

This converts a float representing a Unix epoch in units of seconds

\>>> pd.Timestamp(1513393355.5, unit\='s')
Timestamp('2017-12-16 03:02:35.500000')

Copy to clipboard

This converts an int representing a Unix-epoch in units of weeks

\>>> pd.Timestamp(1535, unit\='W')
Timestamp('1999-06-03 00:00:00')

Copy to clipboard

This converts an int representing a Unix-epoch in units of seconds and for a particular timezone

\>>> pd.Timestamp(1513393355, unit\='s', tz\='US/Pacific')
Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')

Copy to clipboard

Using the other two forms that mimic the API for `datetime.datetime`:

\>>> pd.Timestamp(2017, 1, 1, 12)
Timestamp('2017-01-01 12:00:00')

Copy to clipboard

\>>> pd.Timestamp(year\=2017, month\=1, day\=1, hour\=12)
Timestamp('2017-01-01 12:00:00')

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| [`asm8`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.asm8.html#pandas.Timestamp.asm8 "pandas.Timestamp.asm8") | Return numpy datetime64 format with same precision. |
| [`day`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day.html#pandas.Timestamp.day "pandas.Timestamp.day") | Return the day of the Timestamp. |
| [`day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_week.html#pandas.Timestamp.day_of_week "pandas.Timestamp.day_of_week") | Return day of the week. |
| [`day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_of_year.html#pandas.Timestamp.day_of_year "pandas.Timestamp.day_of_year") | Return the day of the year. |
| [`dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dayofweek.html#pandas.Timestamp.dayofweek "pandas.Timestamp.dayofweek") | (DEPRECATED) Return day of the week. |
| [`dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dayofyear.html#pandas.Timestamp.dayofyear "pandas.Timestamp.dayofyear") | (DEPRECATED) Return day of the year. |
| [`days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.days_in_month.html#pandas.Timestamp.days_in_month "pandas.Timestamp.days_in_month") | Return the number of days in the month. |
| [`daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.daysinmonth.html#pandas.Timestamp.daysinmonth "pandas.Timestamp.daysinmonth") | (DEPRECATED) Return the number of days in the month. |
| [`fold`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fold.html#pandas.Timestamp.fold "pandas.Timestamp.fold") | Return the fold value of the Timestamp. |
| [`hour`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.hour.html#pandas.Timestamp.hour "pandas.Timestamp.hour") | Return the hour of the Timestamp. |
| [`is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_leap_year.html#pandas.Timestamp.is_leap_year "pandas.Timestamp.is_leap_year") | Return True if year is a leap year. |
| [`is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_end.html#pandas.Timestamp.is_month_end "pandas.Timestamp.is_month_end") | Check if the date is the last day of the month. |
| [`is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_month_start.html#pandas.Timestamp.is_month_start "pandas.Timestamp.is_month_start") | Check if the date is the first day of the month. |
| [`is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_end.html#pandas.Timestamp.is_quarter_end "pandas.Timestamp.is_quarter_end") | Check if date is last day of the quarter. |
| [`is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_quarter_start.html#pandas.Timestamp.is_quarter_start "pandas.Timestamp.is_quarter_start") | Check if the date is the first day of the quarter. |
| [`is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_year_end.html#pandas.Timestamp.is_year_end "pandas.Timestamp.is_year_end") | Return True if date is last day of the year. |
| [`is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.is_year_start.html#pandas.Timestamp.is_year_start "pandas.Timestamp.is_year_start") | Return True if date is first day of the year. |
| [`max`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.max.html#pandas.Timestamp.max "pandas.Timestamp.max") |     |
| [`microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.microsecond.html#pandas.Timestamp.microsecond "pandas.Timestamp.microsecond") | Return the microsecond of the Timestamp. |
| [`min`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.min.html#pandas.Timestamp.min "pandas.Timestamp.min") |     |
| [`minute`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.minute.html#pandas.Timestamp.minute "pandas.Timestamp.minute") | Return the minute of the Timestamp. |
| [`month`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month.html#pandas.Timestamp.month "pandas.Timestamp.month") | Return the month of the Timestamp. |
| [`nanosecond`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.nanosecond.html#pandas.Timestamp.nanosecond "pandas.Timestamp.nanosecond") | Return the nanosecond of the Timestamp. |
| [`quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.quarter.html#pandas.Timestamp.quarter "pandas.Timestamp.quarter") | Return the quarter of the year for the Timestamp. |
| [`resolution`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.resolution.html#pandas.Timestamp.resolution "pandas.Timestamp.resolution") |     |
| [`second`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.second.html#pandas.Timestamp.second "pandas.Timestamp.second") | Return the second of the Timestamp. |
| [`tz`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz.html#pandas.Timestamp.tz "pandas.Timestamp.tz") | Alias for tzinfo. |
| [`tzinfo`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzinfo.html#pandas.Timestamp.tzinfo "pandas.Timestamp.tzinfo") | Returns the timezone info of the Timestamp. |
| [`unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.unit.html#pandas.Timestamp.unit "pandas.Timestamp.unit") | The abbreviation associated with self.\_creso. |
| [`value`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.value.html#pandas.Timestamp.value "pandas.Timestamp.value") | Return the value of the Timestamp. |
| [`week`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.week.html#pandas.Timestamp.week "pandas.Timestamp.week") | Return the week number of the year. |
| [`weekofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekofyear.html#pandas.Timestamp.weekofyear "pandas.Timestamp.weekofyear") | Return the week number of the year. |
| [`year`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.year.html#pandas.Timestamp.year "pandas.Timestamp.year") | Return the year of the Timestamp. |

Methods

|     |     |
| --- | --- |
| [`as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.as_unit.html#pandas.Timestamp.as_unit "pandas.Timestamp.as_unit")<br>(unit\[, round\_ok\]) | Convert the underlying int64 representation to the given unit. |
| [`astimezone`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.astimezone.html#pandas.Timestamp.astimezone "pandas.Timestamp.astimezone")<br>(tz) | Convert timezone-aware Timestamp to another time zone. |
| [`ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ceil.html#pandas.Timestamp.ceil "pandas.Timestamp.ceil")<br>(freq\[, ambiguous, nonexistent\]) | Return a new Timestamp ceiled to this resolution. |
| [`combine`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.combine.html#pandas.Timestamp.combine "pandas.Timestamp.combine")<br>(date, time) | Combine a date and time into a single Timestamp object. |
| [`ctime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ctime.html#pandas.Timestamp.ctime "pandas.Timestamp.ctime")<br>() | Return a ctime() style string representing the Timestamp. |
| [`date`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.date.html#pandas.Timestamp.date "pandas.Timestamp.date")<br>() | Returns datetime.date with the same year, month, and day. |
| [`day_name`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.day_name.html#pandas.Timestamp.day_name "pandas.Timestamp.day_name")<br>(\[locale\]) | Return the day name of the Timestamp with specified locale. |
| [`dst`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.dst.html#pandas.Timestamp.dst "pandas.Timestamp.dst")<br>() | Return the daylight saving time (DST) adjustment. |
| [`floor`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.floor.html#pandas.Timestamp.floor "pandas.Timestamp.floor")<br>(freq\[, ambiguous, nonexistent\]) | Return a new Timestamp floored to this resolution. |
| [`fromisocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisocalendar.html#pandas.Timestamp.fromisocalendar "pandas.Timestamp.fromisocalendar")<br>(year, week, day) | Construct a Timestamp from an ISO year, week number, and weekday. |
| [`fromisoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisoformat.html#pandas.Timestamp.fromisoformat "pandas.Timestamp.fromisoformat")<br>(date\_string) | Construct a Timestamp from a string in ISO 8601 format. |
| [`fromordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html#pandas.Timestamp.fromordinal "pandas.Timestamp.fromordinal")<br>(ordinal\[, tz\]) | Construct a timestamp from a proleptic Gregorian ordinal. |
| [`fromtimestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromtimestamp.html#pandas.Timestamp.fromtimestamp "pandas.Timestamp.fromtimestamp")<br>(ts\[, tz\]) | Create a Timestamp object from a POSIX timestamp. |
| [`isocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas.Timestamp.isocalendar "pandas.Timestamp.isocalendar")<br>() | Return a named tuple containing ISO year, week number, and weekday. |
| [`isoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html#pandas.Timestamp.isoformat "pandas.Timestamp.isoformat")<br>(\[sep, timespec\]) | Return the time formatted according to ISO 8601. |
| [`isoweekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoweekday.html#pandas.Timestamp.isoweekday "pandas.Timestamp.isoweekday")<br>() | Return the day of the week represented by the date. |
| [`month_name`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.month_name.html#pandas.Timestamp.month_name "pandas.Timestamp.month_name")<br>(\[locale\]) | Return the month name of the Timestamp with specified locale. |
| [`normalize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.normalize.html#pandas.Timestamp.normalize "pandas.Timestamp.normalize")<br>() | Normalize Timestamp to midnight, preserving tz information. |
| [`now`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.now.html#pandas.Timestamp.now "pandas.Timestamp.now")<br>(\[tz\]) | Return new Timestamp object representing current time local to tz. |
| [`replace`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.replace.html#pandas.Timestamp.replace "pandas.Timestamp.replace")<br>(\[year, month, day, hour, minute, ...\]) | Implements datetime.replace, handles nanoseconds. |
| [`round`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.round.html#pandas.Timestamp.round "pandas.Timestamp.round")<br>(freq\[, ambiguous, nonexistent\]) | Round the Timestamp to the specified resolution. |
| [`strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#pandas.Timestamp.strftime "pandas.Timestamp.strftime")<br>(format) | Return a formatted string of the Timestamp. |
| [`strptime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strptime.html#pandas.Timestamp.strptime "pandas.Timestamp.strptime")<br>(date\_string, format) | Convert string argument to datetime. |
| [`time`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.time.html#pandas.Timestamp.time "pandas.Timestamp.time")<br>() | Return time object with same time but with tzinfo=None. |
| [`timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#pandas.Timestamp.timestamp "pandas.Timestamp.timestamp")<br>() | Return POSIX timestamp as float. |
| [`timetuple`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetuple.html#pandas.Timestamp.timetuple "pandas.Timestamp.timetuple")<br>() | Return time tuple, compatible with time.localtime(). |
| [`timetz`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetz.html#pandas.Timestamp.timetz "pandas.Timestamp.timetz")<br>() | Return time object with same time and tzinfo. |
| [`to_datetime64`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html#pandas.Timestamp.to_datetime64 "pandas.Timestamp.to_datetime64")<br>() | Return a NumPy datetime64 object with same precision. |
| [`to_julian_date`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_julian_date.html#pandas.Timestamp.to_julian_date "pandas.Timestamp.to_julian_date")<br>() | Convert Timestamp to a Julian Date. |
| [`to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html#pandas.Timestamp.to_numpy "pandas.Timestamp.to_numpy")<br>(\[dtype, copy\]) | Convert the Timestamp to a NumPy datetime64. |
| [`to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_period.html#pandas.Timestamp.to_period "pandas.Timestamp.to_period")<br>(\[freq\]) | Return a period of which this timestamp is an observation. |
| [`to_pydatetime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html#pandas.Timestamp.to_pydatetime "pandas.Timestamp.to_pydatetime")<br>(\[warn\]) | Convert a Timestamp object to a native Python datetime object. |
| [`today`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.today.html#pandas.Timestamp.today "pandas.Timestamp.today")<br>(\[tz\]) | Return the current time in the local timezone. |
| [`toordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.toordinal.html#pandas.Timestamp.toordinal "pandas.Timestamp.toordinal")<br>() | Return proleptic Gregorian ordinal. |
| [`tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_convert.html#pandas.Timestamp.tz_convert "pandas.Timestamp.tz_convert")<br>(tz) | Convert timezone-aware Timestamp to another time zone. |
| [`tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tz_localize.html#pandas.Timestamp.tz_localize "pandas.Timestamp.tz_localize")<br>(tz\[, ambiguous, nonexistent\]) | Attach or detach a time zone on a Timestamp. |
| [`tzname`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.tzname.html#pandas.Timestamp.tzname "pandas.Timestamp.tzname")<br>() | Return time zone name. |
| [`utcfromtimestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcfromtimestamp.html#pandas.Timestamp.utcfromtimestamp "pandas.Timestamp.utcfromtimestamp")<br>(ts) | Construct a timezone-aware UTC datetime from a POSIX timestamp. |
| [`utcnow`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcnow.html#pandas.Timestamp.utcnow "pandas.Timestamp.utcnow")<br>() | (DEPRECATED) Return a new Timestamp representing UTC day and time. |
| [`utcoffset`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utcoffset.html#pandas.Timestamp.utcoffset "pandas.Timestamp.utcoffset")<br>() | Return utc offset. |
| [`utctimetuple`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utctimetuple.html#pandas.Timestamp.utctimetuple "pandas.Timestamp.utctimetuple")<br>() | Return UTC time tuple, compatible with time.localtime(). |
| [`weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.weekday.html#pandas.Timestamp.weekday "pandas.Timestamp.weekday")<br>() | Return the day of the week represented by the date. |

On this page