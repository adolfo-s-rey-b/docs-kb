[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas-timedelta "Link to this heading")

================================================================================================================================

class pandas.Timedelta(_value\=<object object>_, _unit\=None_, _\*\*kwargs_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "Link to this definition")

Represents a duration, the difference between two dates or times.

Timedelta is the pandas equivalent of python’s `datetime.timedelta` and is interchangeable with it in most cases.

Parameters:

**value**Timedelta, timedelta, np.timedelta64, str, int or float

Input value.

**unit**str, default ‘ns’

If input is an integer, denote the unit of the input. If input is a float, denote the unit of the integer parts. The decimal parts with resolution lower than 1 nanosecond are ignored.

Possible values:

*   ‘W’, or ‘D’
    
*   ‘days’, or ‘day’
    
*   ‘hours’, ‘hour’, ‘hr’, or ‘h’
    
*   ‘minutes’, ‘minute’, ‘min’, or ‘m’
    
*   ‘seconds’, ‘second’, ‘sec’, or ‘s’
    
*   ‘milliseconds’, ‘millisecond’, ‘millis’, ‘milli’, or ‘ms’
    
*   ‘microseconds’, ‘microsecond’, ‘micros’, ‘micro’, or ‘us’
    
*   ‘nanoseconds’, ‘nanosecond’, ‘nanos’, ‘nano’, or ‘ns’.
    

Deprecated since version 3.0.0: Allowing the values w, d, MIN, MS, US and NS to denote units are deprecated in favour of the values W, D, min, ms, us and ns.

**\*\*kwargs**

Available kwargs: {days, seconds, microseconds, milliseconds, minutes, nanoseconds, hours, weeks}. Values for construction in compat with datetime.timedelta. Numpy ints and floats will be coerced to python ints and floats.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a single timestamp in time.

[`TimedeltaIndex`](https://pandas.pydata.org/docs/reference/api/pandas.TimedeltaIndex.html#pandas.TimedeltaIndex "pandas.TimedeltaIndex")

Immutable Index of timedelta64 data.

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.DateOffset")

Standard kind of date increment used for a date range.

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta.

[`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")

Represents a duration in the datetime module.

[`numpy.timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "(in NumPy v2.5)")

Represents a duration compatible with NumPy.

Notes

The constructor may take in either both values of value and unit or kwargs as above. Either one of them must be used during initialization

The `.value` attribute is always in ns.

If the precision is higher than nanoseconds, the precision of the duration is truncated to nanoseconds.

Examples

Here we initialize Timedelta object with both value and unit

\>>> td \= pd.Timedelta(1, "D")
\>>> td
Timedelta('1 days 00:00:00')

Copy to clipboard

Here we initialize the Timedelta object with kwargs

\>>> td2 \= pd.Timedelta(days\=1)
\>>> td2
Timedelta('1 days 00:00:00')

Copy to clipboard

We see that either way we get the same result

Attributes

|     |     |
| --- | --- |
| [`asm8`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.asm8.html#pandas.Timedelta.asm8 "pandas.Timedelta.asm8") | Return a numpy timedelta64 array scalar view. |
| [`components`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas.Timedelta.components "pandas.Timedelta.components") | Return a components namedtuple-like. |
| [`days`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.days.html#pandas.Timedelta.days "pandas.Timedelta.days") | Returns the days of the timedelta. |
| [`max`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.max.html#pandas.Timedelta.max "pandas.Timedelta.max") |     |
| [`microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.microseconds.html#pandas.Timedelta.microseconds "pandas.Timedelta.microseconds") | Return the number of microseconds (n), where 0 <= n < 1 millisecond. |
| [`min`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.min.html#pandas.Timedelta.min "pandas.Timedelta.min") |     |
| [`nanoseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.nanoseconds.html#pandas.Timedelta.nanoseconds "pandas.Timedelta.nanoseconds") | Return the number of nanoseconds (n), where 0 <= n < 1 microsecond. |
| [`resolution`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.resolution.html#pandas.Timedelta.resolution "pandas.Timedelta.resolution") |     |
| [`resolution_string`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.resolution_string.html#pandas.Timedelta.resolution_string "pandas.Timedelta.resolution_string") | Return a string representing the lowest timedelta resolution. |
| [`seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.seconds.html#pandas.Timedelta.seconds "pandas.Timedelta.seconds") | Return the total hours, minutes, and seconds of the timedelta as seconds. |
| [`unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.unit.html#pandas.Timedelta.unit "pandas.Timedelta.unit") | Return the unit of Timedelta object. |
| [`value`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.value.html#pandas.Timedelta.value "pandas.Timedelta.value") | Return the value of Timedelta object in nanoseconds. |

Methods

|     |     |
| --- | --- |
| [`as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.as_unit.html#pandas.Timedelta.as_unit "pandas.Timedelta.as_unit")<br>(unit\[, round\_ok\]) | Convert the underlying int64 representation to the given unit. |
| [`ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.ceil.html#pandas.Timedelta.ceil "pandas.Timedelta.ceil")<br>(freq) | Return a new Timedelta ceiled to this resolution. |
| [`floor`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.floor.html#pandas.Timedelta.floor "pandas.Timedelta.floor")<br>(freq) | Return a new Timedelta floored to this resolution. |
| [`isoformat`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.isoformat.html#pandas.Timedelta.isoformat "pandas.Timedelta.isoformat")<br>() | Format the Timedelta as ISO 8601 Duration. |
| [`round`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html#pandas.Timedelta.round "pandas.Timedelta.round")<br>(freq) | Round the Timedelta to the specified resolution. |
| [`to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_numpy.html#pandas.Timedelta.to_numpy "pandas.Timedelta.to_numpy")<br>(\[dtype, copy\]) | Convert the Timedelta to a NumPy timedelta64. |
| [`to_pytimedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_pytimedelta.html#pandas.Timedelta.to_pytimedelta "pandas.Timedelta.to_pytimedelta")<br>() | Convert a pandas Timedelta object into a python `datetime.timedelta` object. |
| [`to_timedelta64`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_timedelta64.html#pandas.Timedelta.to_timedelta64 "pandas.Timedelta.to_timedelta64")<br>() | Return a numpy.timedelta64 object with 'ns' precision. |
| [`total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#pandas.Timedelta.total_seconds "pandas.Timedelta.total_seconds")<br>() | Total seconds in the duration. |
| [`view`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.view.html#pandas.Timedelta.view "pandas.Timedelta.view")<br>(dtype) | Array view compatibility. |

On this page