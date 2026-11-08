[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utctimetuple.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.utctimetuple[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utctimetuple.html#pandas-timestamp-utctimetuple "Link to this heading")

=======================================================================================================================================================================

Timestamp.utctimetuple()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.utctimetuple.html#pandas.Timestamp.utctimetuple "Link to this definition")

Return UTC time tuple, compatible with time.localtime().

This method converts the Timestamp to UTC and returns a time tuple containing 9 components: year, month, day, hour, minute, second, weekday, day of year, and DST flag. This is particularly useful for converting a Timestamp to a format compatible with time module functions.

Returns:

time.struct\_time

A time.struct\_time object representing the UTC time.

See also

[`datetime.datetime.utctimetuple`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utctimetuple "(in Python v3.15)")

Return UTC time tuple, compatible with time.localtime().

[`Timestamp.timetuple`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetuple.html#pandas.Timestamp.timetuple "pandas.Timestamp.timetuple")

Return time tuple of local time.

[`time.struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "(in Python v3.15)")

Time tuple structure used by time functions.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00', tz\='Europe/Brussels')
\>>> ts
Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
\>>> ts.utctimetuple()
time.struct\_time(tm\_year=2023, tm\_mon=1, tm\_mday=1, tm\_hour=9,
tm\_min=0, tm\_sec=0, tm\_wday=6, tm\_yday=1, tm\_isdst=0)

Copy to clipboard

On this page