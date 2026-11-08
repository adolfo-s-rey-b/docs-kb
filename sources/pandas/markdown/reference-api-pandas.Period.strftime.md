[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.strftime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.strftime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.strftime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.strftime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.strftime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.strftime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.strftime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.strftime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.strftime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.strftime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.strftime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.strftime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.strftime[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#pandas-period-strftime "Link to this heading")

==================================================================================================================================================

Period.strftime(_fmt_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#pandas.Period.strftime "Link to this definition")

Returns a formatted string representation of the [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
.

Deprecated since version 3.1.0: The `%n` directive for nanoseconds is deprecated; use `%N` instead. `%n` conflicts with the POSIX standard meaning of a newline character.

`fmt` must be `None` or a string containing one or several directives. When `None`, the format will be determined from the frequency of the Period. The method recognizes the same directives as the [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.15)")
 function of the standard Python distribution, as well as the specific additional directives `%f`, `%F`, `%q`, `%l`, `%u`, `%N`. (formatting & docs originally from scikits.timeries).

| Directive | Meaning | Notes |
| --- | --- | --- |
| `%a` | Locale’s abbreviated weekday name. |     |
| `%A` | Locale’s full weekday name. |     |
| `%b` | Locale’s abbreviated month name. |     |
| `%B` | Locale’s full month name. |     |
| `%c` | Locale’s appropriate date and time representation. |     |
| `%d` | Day of the month as a decimal number \[01,31\]. |     |
| `%f` | ‘Fiscal’ year without a century as a decimal number \[00,99\] | (1) |
| `%F` | ‘Fiscal’ year with a century as a decimal number | (2) |
| `%H` | Hour (24-hour clock) as a decimal number \[00,23\]. |     |
| `%I` | Hour (12-hour clock) as a decimal number \[01,12\]. |     |
| `%j` | Day of the year as a decimal number \[001,366\]. |     |
| `%m` | Month as a decimal number \[01,12\]. |     |
| `%M` | Minute as a decimal number \[00,59\]. |     |
| `%p` | Locale’s equivalent of either AM or PM. | (3) |
| `%q` | Quarter as a decimal number \[1,4\] |     |
| `%S` | Second as a decimal number \[00,61\]. | (4) |
| `%l` | Millisecond as a decimal number \[000,999\]. |     |
| `%u` | Microsecond as a decimal number \[000000,999999\]. |     |
| `%N` | Nanosecond as a decimal number \[000000000,999999999\]. |     |
| `%n` | Nanosecond as a decimal number \[000000000,999999999\]. | (6) |
| `%U` | Week number of the year (Sunday as the first day of the week) as a decimal number \[00,53\]. All days in a new year preceding the first Sunday are considered to be in week 0. | (5) |
| `%w` | Weekday as a decimal number \[0(Sunday),6\]. |     |
| `%W` | Week number of the year (Monday as the first day of the week) as a decimal number \[00,53\]. All days in a new year preceding the first Monday are considered to be in week 0. | (5) |
| `%x` | Locale’s appropriate date representation. |     |
| `%X` | Locale’s appropriate time representation. |     |
| `%y` | Year without century as a decimal number \[00,99\]. |     |
| `%Y` | Year with century as a decimal number. |     |
| `%Z` | Time zone name (no characters if no time zone exists). |     |
| `%%` | A literal `'%'` character. |     |

The strftime method provides a way to represent a [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")
 object as a string in a specified format. This is particularly useful when displaying date and time data in different locales or customized formats, suitable for reports or user interfaces. It extends the standard Python string formatting capabilities with additional directives specific to pandas, accommodating features like fiscal years and precise sub-second components.

Parameters:

**fmt**str or None

String containing the desired format directives. If `None`, the format is determined based on the Period’s frequency.

See also

[`Timestamp.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#pandas.Timestamp.strftime "pandas.Timestamp.strftime")

Return a formatted string of the Timestamp.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

[`time.strftime`](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.15)")

Format a time object as a string according to a specified format string in the standard Python library.

Notes

1.  The `%f` directive is the same as `%y` if the frequency is not quarterly. Otherwise, it corresponds to the ‘fiscal’ year, as defined by the [`qyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.qyear.html#pandas.Period.qyear "pandas.Period.qyear")
     attribute.
    
2.  The `%F` directive is the same as `%Y` if the frequency is not quarterly. Otherwise, it corresponds to the ‘fiscal’ year, as defined by the [`qyear`](https://pandas.pydata.org/docs/reference/api/pandas.Period.qyear.html#pandas.Period.qyear "pandas.Period.qyear")
     attribute.
    
3.  The `%p` directive only affects the output hour field if the `%I` directive is used to parse the hour.
    
4.  The range really is `0` to `61`; this accounts for leap seconds and the (very rare) double leap seconds.
    
5.  The `%U` and `%W` directives are only used in calculations when the day of the week and the year are specified.
    
6.  The `%n` directive is deprecated since pandas 3.1.0; use `%N` instead. `%n` is a newline directive in C `strftime` (and Python’s `time.strftime` / `datetime.strftime`).
    

Examples

\>>> from pandas import Period
\>>> a \= Period(freq\='Q-JUL', year\=2006, quarter\=1)
\>>> a.strftime('%F\-Q%q')
'2006-Q1'
\>>> \# Output the last month in the quarter of this date
\>>> a.strftime('%b-%Y')
'Oct-2005'
\>>>
\>>> a \= Period(freq\='D', year\=2001, month\=1, day\=1)
\>>> a.strftime('%d\-%b-%Y')
'01-Jan-2001'
\>>> a.strftime('%b. %d, %Y was a %A')
'Jan. 01, 2001 was a Monday'

Copy to clipboard

On this page