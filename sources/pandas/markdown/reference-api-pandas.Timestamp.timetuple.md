[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetuple.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.timetuple.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetuple.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.timetuple.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.timetuple.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.timetuple.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.timetuple.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.timetuple.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.timetuple.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.timetuple.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.timetuple.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.timetuple.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.timetuple.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.timetuple.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.timetuple[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetuple.html#pandas-timestamp-timetuple "Link to this heading")

==============================================================================================================================================================

Timestamp.timetuple()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timetuple.html#pandas.Timestamp.timetuple "Link to this definition")

Return time tuple, compatible with time.localtime().

This method converts the Timestamp into a time tuple, which is compatible with functions like time.localtime(). The time tuple is a named tuple with attributes such as year, month, day, hour, minute, second, weekday, day of the year, and daylight savings indicator.

See also

[`time.localtime`](https://docs.python.org/3/library/time.html#time.localtime "(in Python v3.15)")

Converts a POSIX timestamp into a time tuple.

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

The Timestamp that represents a specific point in time.

[`datetime.datetime.timetuple`](https://docs.python.org/3/library/datetime.html#datetime.datetime.timetuple "(in Python v3.15)")

Equivalent method in the datetime module.

Examples

\>>> ts \= pd.Timestamp('2023-01-01 10:00:00')
\>>> ts
Timestamp('2023-01-01 10:00:00')
\>>> ts.timetuple()
time.struct\_time(tm\_year=2023, tm\_mon=1, tm\_mday=1,
tm\_hour=10, tm\_min=0, tm\_sec=0, tm\_wday=6, tm\_yday=1, tm\_isdst=-1)

Copy to clipboard

On this page