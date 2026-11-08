[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.api.guess_datetime_format.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.api.guess_datetime_format.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.api.guess_datetime_format.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.api.guess_datetime_format.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.api.guess_datetime_format.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.api.guess_datetime_format.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.api.guess_datetime_format.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.api.guess_datetime_format.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.api.guess_datetime_format.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.api.guess_datetime_format.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.api.guess_datetime_format.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.api.guess_datetime_format.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.api.guess_datetime_format.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.api.guess_datetime_format.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.api.guess\_datetime\_format[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.api.guess_datetime_format.html#pandas-tseries-api-guess-datetime-format "Link to this heading")

==========================================================================================================================================================================================================

pandas.tseries.api.guess\_datetime\_format(_dt\_str_, _dayfirst\=False_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.api.guess_datetime_format.html#pandas.tseries.api.guess_datetime_format "Link to this definition")

Guess the datetime format of a given datetime string.

This function attempts to deduce the format of a given datetime string. It is useful for situations where the datetime format is unknown and needs to be determined for proper parsing. The function is not guaranteed to return a format.

Parameters:

**dt\_str**str

Datetime string to guess the format of.

**dayfirst**bool, default False

If True parses dates with the day first, eg 20/01/2005

Warning

dayfirst=True is not strict, but will prefer to parse with day first (this is a known bug).

Returns:

**str or None**ret

datetime format string (for strftime or strptime), or None if it can’t be guessed.

See also

`to_datetime`

Convert argument to datetime.

`Timestamp`

Pandas replacement for python datetime.datetime object.

`DatetimeIndex`

Immutable ndarray-like of datetime64 data.

Examples

\>>> from pandas.tseries.api import guess\_datetime\_format
\>>> guess\_datetime\_format('09/13/2023')
'%m/%d/%Y'

Copy to clipboard

\>>> guess\_datetime\_format('2023|September|13')

Copy to clipboard

On this page