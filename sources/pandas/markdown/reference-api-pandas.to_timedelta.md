[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.to\_timedelta[#](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas-to-timedelta "Link to this heading")

==========================================================================================================================================

pandas.to\_timedelta(_arg_, _unit\=None_, _errors\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/tools/timedeltas.py#L77-L207)
[#](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "Link to this definition")

Convert argument to timedelta.

Timedeltas are absolute differences in times, expressed in difference units (e.g. days, hours, minutes, seconds). This method converts an argument from a recognized timedelta format / value into a Timedelta type.

Parameters:

**arg**str, timedelta, list-like or Series

The data to be converted to timedelta.

Changed in version 2.0: Strings with units ‘M’, ‘Y’ and ‘y’ do not represent unambiguous timedelta values and will raise an exception.

**unit**str, optional

Denotes the unit of the arg for numeric arg. Defaults to `"ns"`.

Possible values:

*   ‘W’
    
*   ‘D’ / ‘days’ / ‘day’
    
*   ‘hours’ / ‘hour’ / ‘hr’ / ‘h’
    
*   ‘m’ / ‘minute’ / ‘min’ / ‘minutes’
    
*   ‘s’ / ‘seconds’ / ‘sec’ / ‘second’
    
*   ‘ms’ / ‘milliseconds’ / ‘millisecond’ / ‘milli’ / ‘millis’
    
*   ‘us’ / ‘microseconds’ / ‘microsecond’ / ‘micro’ / ‘micros’
    
*   ‘ns’ / ‘nanoseconds’ / ‘nano’ / ‘nanos’ / ‘nanosecond’
    

Must not be specified when arg contains strings and `errors="raise"`.

**errors**{‘raise’, ‘coerce’}, default ‘raise’

*   If ‘raise’, then invalid parsing will raise an exception.
    
*   If ‘coerce’, then invalid parsing will be set as NaT.
    

Returns:

timedelta

If parsing succeeded. Return type depends on input:

*   list-like: TimedeltaIndex of timedelta64 dtype
    
*   Series: Series of timedelta64 dtype
    
*   scalar: Timedelta
    

See also

[`DataFrame.astype`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype "pandas.DataFrame.astype")

Cast argument to a specified dtype.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

`convert_dtypes`

Convert dtypes.

Notes

If the precision is higher than nanoseconds, the precision of the duration is truncated to nanoseconds for string inputs.

Examples

Parsing a single string to a Timedelta:

\>>> pd.to\_timedelta("1 days 06:05:01.00003")
Timedelta('1 days 06:05:01.000030')
\>>> pd.to\_timedelta("15.5us")
Timedelta('0 days 00:00:00.000015500')

Copy to clipboard

Parsing a list or array of strings:

\>>> pd.to\_timedelta(\["1 days 06:05:01.00003", "15.5us", "nan"\])
TimedeltaIndex(\['1 days 06:05:01.000030000', '0 days 00:00:00.000015500', NaT\],
               dtype='timedelta64\[ns\]', freq=None)

Copy to clipboard

Converting numbers by specifying the unit keyword argument:

\>>> pd.to\_timedelta(np.arange(5), unit\="s")
TimedeltaIndex(\['0 days 00:00:00', '0 days 00:00:01', '0 days 00:00:02',\
                '0 days 00:00:03', '0 days 00:00:04'\],
               dtype='timedelta64\[us\]', freq=None)
\>>> pd.to\_timedelta(np.arange(5), unit\="D")
TimedeltaIndex(\['0 days', '1 days', '2 days', '3 days', '4 days'\],
               dtype='timedelta64\[us\]', freq=None)

Copy to clipboard

On this page