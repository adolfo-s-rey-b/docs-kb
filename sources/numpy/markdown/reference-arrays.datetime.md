[Skip to main content](https://numpy.org/doc/stable/reference/arrays.datetime.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/arrays.datetime.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/arrays.datetime.html)
[2.4](https://numpy.org/doc/2.4/reference/arrays.datetime.html)
[2.3](https://numpy.org/doc/2.3/reference/arrays.datetime.html)
[2.2](https://numpy.org/doc/2.2/reference/arrays.datetime.html)
[2.1](https://numpy.org/doc/2.1/reference/arrays.datetime.html)
[2.0](https://numpy.org/doc/2.0/reference/arrays.datetime.html)
[1.26](https://numpy.org/doc/1.26/reference/arrays.datetime.html)
[1.25](https://numpy.org/doc/1.25/reference/arrays.datetime.html)
[1.24](https://numpy.org/doc/1.24/reference/arrays.datetime.html)
[1.23](https://numpy.org/doc/1.23/reference/arrays.datetime.html)
[1.22](https://numpy.org/doc/1.22/reference/arrays.datetime.html)
[1.21](https://numpy.org/doc/1.21/reference/arrays.datetime.html)
[1.20](https://numpy.org/doc/1.20/reference/arrays.datetime.html)
[1.19](https://numpy.org/doc/1.19/reference/arrays.datetime.html)
[1.18](https://numpy.org/doc/1.18/reference/arrays.datetime.html)
[1.17](https://numpy.org/doc/1.17/reference/arrays.datetime.html)
[1.16](https://numpy.org/doc/1.16/reference/arrays.datetime.html)
[1.15](https://numpy.org/doc/1.15/reference/arrays.datetime.html)
[1.14](https://numpy.org/doc/1.14/reference/arrays.datetime.html)
[1.13](https://numpy.org/doc/1.13/reference/arrays.datetime.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Datetimes and timedeltas[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetimes-and-timedeltas "Link to this heading")

=========================================================================================================================================

Starting in NumPy 1.7, there are core array data types which natively support datetime functionality. The data type is called [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
, so named because [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 is already taken by the Python standard library.

Datetime64 conventions and assumptions[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime64-conventions-and-assumptions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Similar to the Python [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)")
 class, dates are expressed in the current Gregorian Calendar, indefinitely extended both in the future and in the past. [\[1\]](https://numpy.org/doc/stable/reference/arrays.datetime.html#id3)
 Contrary to Python [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)")
, which supports only years in the 1 AD — 9999 AD range, [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 allows also for dates BC; years BC follow the [Astronomical year numbering](https://en.wikipedia.org/wiki/Astronomical_year_numbering)
 convention, i.e. year 2 BC is numbered −1, year 1 BC is numbered 0, year 1 AD is numbered 1.

Time instants, say 16:23:32.234, are represented counting hours, minutes, seconds and fractions from midnight: i.e. 00:00:00.000 is midnight, 12:00:00.000 is noon, etc. Each calendar day has exactly 86400 seconds. This is a “naive” time, with no explicit notion of timezones or specific time scales (UT1, UTC, TAI, etc.). [\[2\]](https://numpy.org/doc/stable/reference/arrays.datetime.html#id4)

Basic datetimes[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#basic-datetimes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

The most basic way to create datetimes is from strings in ISO 8601 date or datetime format. It is also possible to create datetimes from an integer by offset relative to the Unix epoch (00:00:00 UTC on 1 January 1970). The unit for internal storage is automatically selected from the form of the string, and can be either a [date unit](https://numpy.org/doc/stable/reference/arrays.datetime.html#arrays-dtypes-dateunits)
 or a [time unit](https://numpy.org/doc/stable/reference/arrays.datetime.html#arrays-dtypes-timeunits)
. The date units are years (‘Y’), months (‘M’), weeks (‘W’), and days (‘D’), while the time units are hours (‘h’), minutes (‘m’), seconds (‘s’), milliseconds (‘ms’), and some additional SI-prefix seconds-based units. The [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 data type also accepts the string “NAT”, in any combination of lowercase/uppercase letters, for a “Not A Time” value. The string “now” is also supported and returns the current UTC time. By default, it uses second (‘s’) precision, but you can specify a different unit (e.g., ‘M’, ‘D’, ‘h’) to truncate the result to that precision. Units finer than seconds (such as ‘ms’ or ‘ns’) are supported but will show fractional parts as zeros, effectively truncating to whole seconds. The string “today” is also supported and returns the current UTC date with day precision. It also supports the same precision specifiers as `now`.

Example

Try it in your browser!

A simple ISO date:

\>>> import numpy as np

Copy to clipboard

\>>> np.datetime64('2005-02-25')
np.datetime64('2005-02-25')

Copy to clipboard

From an integer and a date unit, 1 year since the UNIX epoch:

\>>> np.datetime64(1, 'Y')
np.datetime64('1971')

Copy to clipboard

Using months for the unit:

\>>> np.datetime64('2005-02')
np.datetime64('2005-02')

Copy to clipboard

Specifying just the month, but forcing a ‘days’ unit:

\>>> np.datetime64('2005-02', 'D')
np.datetime64('2005-02-01')

Copy to clipboard

From a date and time:

\>>> np.datetime64('2005-02-25T03:30')
np.datetime64('2005-02-25T03:30')

Copy to clipboard

NAT (not a time):

\>>> np.datetime64('nat', 'D')
np.datetime64('NaT', 'D')

Copy to clipboard

The current time (UTC, default second precision):

\>>> np.datetime64('now')
np.datetime64('2025-08-05T02:22:14')  # result will depend on the current time

Copy to clipboard

\>>> np.datetime64('now', 'D')
np.datetime64('2025-08-05')

Copy to clipboard

\>>> np.datetime64('now', 'ms')
np.datetime64('2025-08-05T02:22:14.000')

Copy to clipboard

The current date:

\>>> np.datetime64('today')
np.datetime64('2025-08-05')  # result will depend on the current date

Copy to clipboard

Go BackOpen In Tab

When creating an array of datetimes from a string, it is still possible to automatically select the unit from the inputs, by using the datetime type with generic units.

Deprecated since version 2.5: The generic units of [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 were deprecated in NumPy 2.5 and will raise an error in the future. With this change, `NaT` in [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 is now required to have an explicit time unit.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.array(\['2007-07-13', '2006-01-13', '2010-08-13'\], dtype\=np.datetime64)
array(\['2007-07-13', '2006-01-13', '2010-08-13'\], dtype='datetime64\[D\]')

Copy to clipboard

\>>> np.array(\['2001-01-01T12:00', '2002-02-03T13:56:03.172'\], dtype\=np.datetime64)
array(\['2001-01-01T12:00:00.000', '2002-02-03T13:56:03.172'\],
      dtype='datetime64\[ms\]')

Copy to clipboard

Go BackOpen In Tab

An array of datetimes can be constructed from integers representing POSIX timestamps with the given unit.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.array(\[0, 1577836800\], dtype\='datetime64\[s\]')
array(\['1970-01-01T00:00:00', '2020-01-01T00:00:00'\],
      dtype='datetime64\[s\]')

Copy to clipboard

\>>> np.array(\[0, 1577836800000\]).astype('datetime64\[ms\]')
array(\['1970-01-01T00:00:00.000', '2020-01-01T00:00:00.000'\],
      dtype='datetime64\[ms\]')

Copy to clipboard

Go BackOpen In Tab

The datetime type works with many common NumPy functions, for example [`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
 can be used to generate ranges of dates.

Example

Try it in your browser!

All the dates for one month:

\>>> import numpy as np

Copy to clipboard

\>>> np.arange('2005-02', '2005-03', dtype\='datetime64\[D\]')
array(\['2005-02-01', '2005-02-02', '2005-02-03', '2005-02-04',\
       '2005-02-05', '2005-02-06', '2005-02-07', '2005-02-08',\
       '2005-02-09', '2005-02-10', '2005-02-11', '2005-02-12',\
       '2005-02-13', '2005-02-14', '2005-02-15', '2005-02-16',\
       '2005-02-17', '2005-02-18', '2005-02-19', '2005-02-20',\
       '2005-02-21', '2005-02-22', '2005-02-23', '2005-02-24',\
       '2005-02-25', '2005-02-26', '2005-02-27', '2005-02-28'\],
      dtype='datetime64\[D\]')

Copy to clipboard

Go BackOpen In Tab

The datetime object represents a single moment in time. If two datetimes have different units, they may still be representing the same moment of time, and converting from a bigger unit like months to a smaller unit like days is considered a ‘safe’ cast because the moment of time is still being represented exactly.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.datetime64('2005') \== np.datetime64('2005-01-01')
True

Copy to clipboard

\>>> np.datetime64('2010-03-14T15') \== np.datetime64('2010-03-14T15:00:00.00')
True

Copy to clipboard

Go BackOpen In Tab

Deprecated since version 1.11.0: NumPy does not store timezone information. For backwards compatibility, datetime64 still parses timezone offsets, which it handles by converting to UTC±00:00 (Zulu time). This behaviour is deprecated and will raise an error in the future.

Datetime and timedelta arithmetic[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime-and-timedelta-arithmetic "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy allows the subtraction of two datetime values, an operation which produces a number with a time unit. Because NumPy doesn’t have a physical quantities system in its core, the [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 data type was created to complement [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
. The arguments for [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 are a number, to represent the number of units, and a date/time unit, such as (D)ay, (M)onth, (Y)ear, (h)ours, (m)inutes, or (s)econds. The [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 data type also accepts the string “NAT” in place of the number for a “Not A Time” value.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.timedelta64(1, 'D')
np.timedelta64(1,'D')

Copy to clipboard

\>>> np.timedelta64(4, 'h')
np.timedelta64(4,'h')

Copy to clipboard

\>>> np.timedelta64('nAt', 'D')
np.timedelta64('NaT', 'D')

Copy to clipboard

Go BackOpen In Tab

Datetimes and Timedeltas work together to provide ways for simple datetime calculations.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.datetime64('2009-01-01') \- np.datetime64('2008-01-01')
np.timedelta64(366,'D')

Copy to clipboard

\>>> np.datetime64('2009') + np.timedelta64(20, 'D')
np.datetime64('2009-01-21')

Copy to clipboard

\>>> np.datetime64('2011-06-15T00:00') + np.timedelta64(12, 'h')
np.datetime64('2011-06-15T12:00')

Copy to clipboard

\>>> np.timedelta64(1,'W') / np.timedelta64(1,'D')
7.0

Copy to clipboard

\>>> np.timedelta64(1,'W') % np.timedelta64(10,'D')
np.timedelta64(7,'D')

Copy to clipboard

\>>> np.datetime64('nat', 'D') \- np.datetime64('2009-01-01')
np.timedelta64('NaT','D')

Copy to clipboard

\>>> np.datetime64('2009-01-01') + np.timedelta64('nat', 'D')
np.datetime64('NaT', 'D')

Copy to clipboard

Go BackOpen In Tab

There are two Timedelta units (‘Y’, years and ‘M’, months) which are treated specially, because how much time they represent changes depending on when they are used. While a timedelta day unit is equivalent to 24 hours, month and year units cannot be converted directly into days without using ‘unsafe’ casting.

The [`numpy.ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype")
 method can be used for unsafe conversion of months/years to days. The conversion follows calculating the averaged values from the 400 year leap-year cycle.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> a \= np.timedelta64(1, 'Y')

Copy to clipboard

\>>> np.timedelta64(a, 'M')
numpy.timedelta64(12,'M')

Copy to clipboard

\>>> np.timedelta64(a, 'D')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Cannot cast NumPy timedelta64 scalar from metadata \[Y\] to \[D\] according to the rule 'same\_kind'

Copy to clipboard

Go BackOpen In Tab

Datetime units[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime-units "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

The Datetime and Timedelta data types support a large number of time units, as well as generic units which can be coerced into any of the other units based on input data. The generic units are deprecated since NumPy 2.5 and will raise an error in the future. Migration guidance is provided in the [migration guide for deprecation of generic units](https://numpy.org/doc/stable/reference/arrays.datetime.html#migration-guide-for-deprecation-of-generic-units)
 section below.

Datetimes are always stored with an epoch of 1970-01-01T00:00. This means the supported dates are always a symmetric interval around the epoch, called “time span” in the table below.

The length of the span is the range of a 64-bit integer times the length of the date or unit. For example, the time span for ‘W’ (week) is exactly 7 times longer than the time span for ‘D’ (day), and the time span for ‘D’ (day) is exactly 24 times longer than the time span for ‘h’ (hour).

Here are the date units:

| Code | Meaning | Time span (relative) | Time span (absolute) |
| --- | --- | --- | --- |
| Y   | year | +/- 9.2e18 years | \[9.2e18 BC, 9.2e18 AD\] |
| M   | month | +/- 7.6e17 years | \[7.6e17 BC, 7.6e17 AD\] |
| W   | week | +/- 1.7e17 years | \[1.7e17 BC, 1.7e17 AD\] |
| D   | day | +/- 2.5e16 years | \[2.5e16 BC, 2.5e16 AD\] |

And here are the time units:

| Code | Meaning | Time span (relative) | Time span (absolute) |
| --- | --- | --- | --- |
| h   | hour | +/- 1.0e15 years | \[1.0e15 BC, 1.0e15 AD\] |
| m   | minute | +/- 1.7e13 years | \[1.7e13 BC, 1.7e13 AD\] |
| s   | second | +/- 2.9e11 years | \[2.9e11 BC, 2.9e11 AD\] |
| ms  | millisecond | +/- 2.9e8 years | \[ 2.9e8 BC, 2.9e8 AD\] |
| us / μs | microsecond | +/- 2.9e5 years | \[290301 BC, 294241 AD\] |
| ns  | nanosecond | +/- 292 years | \[ 1678 AD, 2262 AD\] |
| ps  | picosecond | +/- 106 days | \[ 1969 AD, 1970 AD\] |
| fs  | femtosecond | +/- 2.6 hours | \[ 1969 AD, 1970 AD\] |
| as  | attosecond | +/- 9.2 seconds | \[ 1969 AD, 1970 AD\] |

Converting datetime and timedelta to Python Object[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#converting-datetime-and-timedelta-to-python-object "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy follows a strict protocol when converting [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 and/or [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 to Python Objects (e.g., `tuple`, `list`, [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
).

The protocol is described in the following table:

| Input Type | for [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64") | for [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64") |
| --- | --- | --- |
| `NaT` | `None` | `None` |
| ns/ps/fs/as | `int` | `int` |
| μs/ms/s/m/h | [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)") |
| D/W (Linear units) | [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)") | [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)") |
| Y/M (Non-linear units) | [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)") | `int` |
| Generic units | [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.14)") | `int` |

Deprecated since version 2.5: The generic units of [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 are deprecated in NumPy 2.5 and will raise an error in the future.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> type(np.datetime64('NaT', 'D').item())
<class 'NoneType'>

Copy to clipboard

\>>> type(np.timedelta64('NaT', 'D').item())
<class 'NoneType'>

Copy to clipboard

\>>> type(np.timedelta64(123, 'ns').item())
<class 'int'>

Copy to clipboard

\>>> type(np.datetime64('2025-01-01T12:00:00.123456').item())
<class 'datetime.datetime'>

Copy to clipboard

\>>> type(np.timedelta64(10, 'D').item())
<class 'datetime.timedelta'>

Copy to clipboard

Go BackOpen In Tab

In the case where conversion of [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 and/or [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 is done against Python types like `int`, `float`, and `str` the corresponding return types will be `np.str_`, `np.int64` and `np.float64`.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> type(np.timedelta64(1, 'D').astype(int))
<class 'numpy.int64'>

Copy to clipboard

\>>> type(np.datetime64('2025-01-01T12:00:00.123456').astype(float))
<class 'numpy.float64'>

Copy to clipboard

\>>> type(np.timedelta64(123, 'ns').astype(str))
<class 'numpy.str\_'>

Copy to clipboard

Go BackOpen In Tab

Business day functionality[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#business-day-functionality "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

To allow the datetime to be used in contexts where only certain days of the week are valid, NumPy includes a set of “busday” (business day) functions.

The default for busday functions is that the only valid days are Monday through Friday (the usual business days). The implementation is based on a “weekmask” containing 7 Boolean flags to indicate valid days; custom weekmasks are possible that specify other sets of valid days.

The “busday” functions can additionally check a list of “holiday” dates, specific dates that are not valid days.

The function [`busday_offset`](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html#numpy.busday_offset "numpy.busday_offset")
 allows you to apply offsets specified in business days to datetimes with a unit of ‘D’ (day).

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.busday\_offset('2011-06-23', 1)
np.datetime64('2011-06-24')

Copy to clipboard

\>>> np.busday\_offset('2011-06-23', 2)
np.datetime64('2011-06-27')

Copy to clipboard

Go BackOpen In Tab

When an input date falls on the weekend or a holiday, [`busday_offset`](https://numpy.org/doc/stable/reference/generated/numpy.busday_offset.html#numpy.busday_offset "numpy.busday_offset")
 first applies a rule to roll the date to a valid business day, then applies the offset. The default rule is ‘raise’, which simply raises an exception. The rules most typically used are ‘forward’ and ‘backward’.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.busday\_offset('2011-06-25', 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Non-business day date in busday\_offset

Copy to clipboard

\>>> np.busday\_offset('2011-06-25', 0, roll\='forward')
np.datetime64('2011-06-27')

Copy to clipboard

\>>> np.busday\_offset('2011-06-25', 2, roll\='forward')
np.datetime64('2011-06-29')

Copy to clipboard

\>>> np.busday\_offset('2011-06-25', 0, roll\='backward')
np.datetime64('2011-06-24')

Copy to clipboard

\>>> np.busday\_offset('2011-06-25', 2, roll\='backward')
np.datetime64('2011-06-28')

Copy to clipboard

Go BackOpen In Tab

In some cases, an appropriate use of the roll and the offset is necessary to get a desired answer.

Example

Try it in your browser!

The first business day on or after a date:

\>>> import numpy as np

Copy to clipboard

\>>> np.busday\_offset('2011-03-20', 0, roll\='forward')
np.datetime64('2011-03-21')
\>>> np.busday\_offset('2011-03-22', 0, roll\='forward')
np.datetime64('2011-03-22')

Copy to clipboard

The first business day strictly after a date:

\>>> np.busday\_offset('2011-03-20', 1, roll\='backward')
np.datetime64('2011-03-21')
\>>> np.busday\_offset('2011-03-22', 1, roll\='backward')
np.datetime64('2011-03-23')

Copy to clipboard

Go BackOpen In Tab

The function is also useful for computing some kinds of days like holidays. In Canada and the U.S., Mother’s day is on the second Sunday in May, which can be computed with a custom weekmask.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.busday\_offset('2012-05', 1, roll\='forward', weekmask\='Sun')
np.datetime64('2012-05-13')

Copy to clipboard

Go BackOpen In Tab

When performance is important for manipulating many business dates with one particular choice of weekmask and holidays, there is an object [`busdaycalendar`](https://numpy.org/doc/stable/reference/generated/numpy.busdaycalendar.html#numpy.busdaycalendar "numpy.busdaycalendar")
 which stores the data necessary in an optimized form.

### np.is\_busday():[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#np-is-busday "Link to this heading")

To test a [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 value to see if it is a valid day, use [`is_busday`](https://numpy.org/doc/stable/reference/generated/numpy.is_busday.html#numpy.is_busday "numpy.is_busday")
.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.is\_busday(np.datetime64('2011-07-15'))  \# a Friday
True
\>>> np.is\_busday(np.datetime64('2011-07-16')) \# a Saturday
False
\>>> np.is\_busday(np.datetime64('2011-07-16'), weekmask\="Sat Sun")
True
\>>> a \= np.arange(np.datetime64('2011-07-11'), np.datetime64('2011-07-18'))
\>>> np.is\_busday(a)
array(\[ True,  True,  True,  True,  True, False, False\])

Copy to clipboard

Go BackOpen In Tab

### np.busday\_count():[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#np-busday-count "Link to this heading")

To find how many valid days there are in a specified range of datetime64 dates, use [`busday_count`](https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html#numpy.busday_count "numpy.busday_count")
:

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.busday\_count(np.datetime64('2011-07-11'), np.datetime64('2011-07-18'))
5
\>>> np.busday\_count(np.datetime64('2011-07-18'), np.datetime64('2011-07-11'))
\-5

Copy to clipboard

Go BackOpen In Tab

If you have an array of datetime64 day values, and you want a count of how many of them are valid dates, you can do this:

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> a \= np.arange(np.datetime64('2011-07-11'), np.datetime64('2011-07-18'))
\>>> np.count\_nonzero(np.is\_busday(a))
5

Copy to clipboard

Go BackOpen In Tab

### Custom weekmasks[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#custom-weekmasks "Link to this heading")

Here are several examples of custom weekmask values. These examples specify the “busday” default of Monday through Friday being valid days.

Some examples:

\# Positional sequences; positions are Monday through Sunday.
\# Length of the sequence must be exactly 7.
weekmask \= \[1, 1, 1, 1, 1, 0, 0\]
\# list or other sequence; 0 == invalid day, 1 == valid day
weekmask \= "1111100"
\# string '0' == invalid day, '1' == valid day

\# string abbreviations from this list: Mon Tue Wed Thu Fri Sat Sun
weekmask \= "Mon Tue Wed Thu Fri"
\# any amount of whitespace is allowed; abbreviations are case-sensitive.
weekmask \= "MonTue Wed  Thu\\tFri"

Copy to clipboard

Datetime64 shortcomings[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime64-shortcomings "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

The assumption that all days are exactly 86400 seconds long makes [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 largely compatible with Python [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "(in Python v3.14)")
 and “POSIX time” semantics; therefore they all share the same well known shortcomings with respect to the UTC timescale and historical time determination. A brief non exhaustive summary is given below.

*   It is impossible to parse valid UTC timestamps occurring during a positive leap second.
    
    Example
    
    “2016-12-31 23:59:60 UTC” was a leap second, therefore “2016-12-31 23:59:60.450 UTC” is a valid timestamp which is not parseable by [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
    :
    
    Try it in your browser!
    
    \>>> import numpy as np
    
    Copy to clipboard
    
    \>>> np.datetime64("2016-12-31 23:59:60.450")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Seconds out of range in datetime string "2016-12-31 23:59:60.450"
    
    Copy to clipboard
    
    Go BackOpen In Tab
    
*   Timedelta64 computations between two UTC dates can be wrong by an integer number of SI seconds.
    
    Example
    
    Compute the number of SI seconds between “2021-01-01 12:56:23.423 UTC” and “2001-01-01 00:00:00.000 UTC”:
    
    Try it in your browser!
    
    \>>> import numpy as np
    
    Copy to clipboard
    
    \>>> (
    ...   np.datetime64("2021-01-01 12:56:23.423")
    ...   \- np.datetime64("2001-01-01")
    ... ) / np.timedelta64(1, "s")
    631198583.423
    
    Copy to clipboard
    
    However, the correct answer is _631198588.423_ SI seconds, because there were 5 leap seconds between 2001 and 2021.
    
    Go BackOpen In Tab
    
*   Timedelta64 computations for dates in the past do not return SI seconds, as one would expect.
    
    Example
    
    > Compute the number of seconds between “000-01-01 UT” and “1600-01-01 UT”, where UT is [universal time](https://en.wikipedia.org/wiki/Universal_Time)
    > :
    
    Try it in your browser!
    
    \>>> import numpy as np
    
    Copy to clipboard
    
    \>>> a \= np.datetime64("0000-01-01", "us")
    \>>> b \= np.datetime64("1600-01-01", "us")
    \>>> b \- a
    numpy.timedelta64(50491123200000000,'us')
    
    Copy to clipboard
    
    The computed results, _50491123200_ seconds, are obtained as the elapsed number of days (_584388_) times _86400_ seconds; this is the number of seconds of a clock in sync with the Earth’s rotation. The exact value in SI seconds can only be estimated, e.g., using data published in [Measurement of the Earth’s rotation: 720 BC to AD 2015, 2016, Royal Society’s Proceedings A 472, by Stephenson et.al.](https://doi.org/10.1098/rspa.2016.0404)
    . A sensible estimate is _50491112870 ± 90_ seconds, with a difference of 10330 seconds.
    
    Go BackOpen In Tab
    

Migration guide for deprecation of generic units[#](https://numpy.org/doc/stable/reference/arrays.datetime.html#migration-guide-for-deprecation-of-generic-units "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The generic units of [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 are deprecated since NumPy 2.5 and will raise an error in the future. This section provides guidance on how to update code that uses generic units of [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 and [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 to avoid future errors.

The straight forward way is to replace the generic unit with a specific time unit such as ‘D’ (day), ‘h’ (hour), ‘m’ (minute), ‘s’ (second), etc. The choice of the specific time unit will depend on the context of your code and the level of precision you require.

Example

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> \# Old code using generic units of timedelta64
\>>> np.timedelta64(5, "s") + 1
DeprecationWarning: The 'generic' unit for NumPy timedelta is deprecated, and will raise an error in the future. This includes implicit conversion of bare integers (e.g. \`+ 1\`).Please use a specific unit instead.

Copy to clipboard

\>>> \# Updated code using a specific time unit
\>>> np.timedelta64(5, "s") + np.timedelta64(1, "s")
np.timedelta64(6,'s')

Copy to clipboard

When comparing [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 objects, make sure to use the same specific time unit for both operands even if they are representing `0`.

\>>> np.timedelta64(0, "s") \== 0
DeprecationWarning: The 'generic' unit for NumPy timedelta is deprecated, and will raise an error in the future. This includes implicit conversion of bare integers (e.g. \`== 0\`).Please use a specific unit instead.
np.True\_

Copy to clipboard

\>>> np.timedelta64(0, "s") \== np.timedelta64(0, "s")
np.True\_

Copy to clipboard

When using `numpy.testing.assert_allclose` to compare [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 objects, ensure to set a specific time unit to `atol` parameter as well.

\>>> arr \= np.ones(5, dtype\='m8\[s\]')
\>>> np.testing.assert\_allclose(arr, np.timedelta64(1, "s"), atol\=np.timedelta64(0, "s"))

Copy to clipboard

Previously, [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
 allowed _NaT_ without specifying a time unit. With the deprecation of generic units, _NaT_ is now required to have an explicit time unit for consistency with other datetime and timedelta operations.

\>>> np.datetime64("NAT")
DeprecationWarning: The 'generic' unit for NumPy timedelta is deprecated, and will raise an error in the future. This includes implicit conversion of bare integers (e.g. \`+ 1\`).Please use a specific unit instead.

Copy to clipboard

\>>> np.datetime64("NAT", "D")
np.datetime64('NaT', 'D')

Copy to clipboard

Go BackOpen In Tab

On this page