[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.to_pydatetime.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.to_pydatetime.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.to_pydatetime.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.to_pydatetime.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.to_pydatetime.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.to_pydatetime.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.to_pydatetime.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.to_pydatetime.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.to_pydatetime.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.to_pydatetime.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.to_pydatetime.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.to_pydatetime.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.to\_pydatetime[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html#pandas-timestamp-to-pydatetime "Link to this heading")

===========================================================================================================================================================================

Timestamp.to\_pydatetime(_warn\=True_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_pydatetime.html#pandas.Timestamp.to_pydatetime "Link to this definition")

Convert a Timestamp object to a native Python datetime object.

This method is useful for when you need to utilize a pandas Timestamp object in contexts where native Python datetime objects are expected or required. The conversion discards the nanoseconds component, and a warning can be issued in such cases if desired.

Parameters:

**warn**bool, default True

If True, issues a warning when the timestamp includes nonzero nanoseconds, as these will be discarded during the conversion.

Returns:

datetime.datetime or NaT

Returns a datetime.datetime object representing the timestamp, with year, month, day, hour, minute, second, and microsecond components. If the timestamp is NaT (Not a Time), returns NaT.

See also

[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")

The standard Python datetime class that this method returns.

[`Timestamp.timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.timestamp.html#pandas.Timestamp.timestamp "pandas.Timestamp.timestamp")

Convert a Timestamp object to POSIX timestamp.

[`Timestamp.to_datetime64`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html#pandas.Timestamp.to_datetime64 "pandas.Timestamp.to_datetime64")

Convert a Timestamp object to numpy.datetime64.

Examples

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548')
\>>> ts.to\_pydatetime()
datetime.datetime(2020, 3, 14, 15, 32, 52, 192548)

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.to\_pydatetime()
NaT

Copy to clipboard

On this page