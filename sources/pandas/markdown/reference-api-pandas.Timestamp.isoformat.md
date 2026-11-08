[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.isoformat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.isoformat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.isoformat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.isoformat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.isoformat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.isoformat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.isoformat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.isoformat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.isoformat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.isoformat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.isoformat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.isoformat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.isoformat[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html#pandas-timestamp-isoformat "Link to this heading")

==============================================================================================================================================================

Timestamp.isoformat(_sep\='T'_, _timespec\='auto'_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isoformat.html#pandas.Timestamp.isoformat "Link to this definition")

Return the time formatted according to ISO 8601.

The full format looks like ‘YYYY-MM-DD HH:MM:SS.mmmmmmnnn’. By default, the fractional part is omitted if self.microsecond == 0 and self.\_nanosecond == 0.

If self.tzinfo is not None, the UTC offset is also attached, giving a full format of ‘YYYY-MM-DD HH:MM:SS.mmmmmmnnn+HH:MM\[:SS\[.ffffff\]\]’. The ‘:SS’ is present only if the offset is not a whole number of minutes, as for a timezone in its pre-standardization era.

Parameters:

**sep**str, default ‘T’

String used as the separator between the date and time.

**timespec**str, default ‘auto’

Specifies the number of additional terms of the time to include. The valid values are ‘auto’, ‘hours’, ‘minutes’, ‘seconds’, ‘milliseconds’, ‘microseconds’, and ‘nanoseconds’.

Returns:

str

See also

[`Timestamp.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#pandas.Timestamp.strftime "pandas.Timestamp.strftime")

Return a formatted string.

[`Timestamp.isocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.isocalendar.html#pandas.Timestamp.isocalendar "pandas.Timestamp.isocalendar")

Return a tuple containing ISO year, week number and weekday.

Examples

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651')
\>>> ts.isoformat()
'2020-03-14T15:32:52.192548651'
\>>> ts.isoformat(timespec\='microseconds')
'2020-03-14T15:32:52.192548'

Copy to clipboard

On this page