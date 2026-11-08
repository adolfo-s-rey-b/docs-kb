[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisocalendar.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.fromisocalendar.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisocalendar.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.fromisocalendar.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.fromisocalendar.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.fromisocalendar.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.fromisocalendar.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.fromisocalendar.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.fromisocalendar.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.fromisocalendar.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.fromisocalendar.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.fromisocalendar.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.fromisocalendar.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.fromisocalendar.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.fromisocalendar[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisocalendar.html#pandas-timestamp-fromisocalendar "Link to this heading")

================================================================================================================================================================================

classmethod Timestamp.fromisocalendar(_year_, _week_, _day_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromisocalendar.html#pandas.Timestamp.fromisocalendar "Link to this definition")

Construct a Timestamp from an ISO year, week number, and weekday.

This is the inverse of [`Timestamp.isocalendar()`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas.Timestamp.isocalendar "pandas.Timestamp.isocalendar")
, constructing a Timestamp from the ISO 8601 year, week number, and weekday.

Parameters:

**year**int

ISO year.

**week**int

ISO week number, ranging from 1 to 52 or 53.

**day**int

ISO weekday, where Monday is 1 and Sunday is 7.

Returns:

Timestamp

A Timestamp object corresponding to the given ISO calendar date.

See also

[`Timestamp.isocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas.Timestamp.isocalendar "pandas.Timestamp.isocalendar")

Return a named tuple with ISO year, week, and weekday.

[`Timestamp.fromordinal`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.fromordinal.html#pandas.Timestamp.fromordinal "pandas.Timestamp.fromordinal")

Construct a Timestamp from a proleptic Gregorian ordinal.

Examples

\>>> pd.Timestamp.fromisocalendar(2023, 1, 1)
Timestamp('2023-01-02 00:00:00')

Copy to clipboard

On this page