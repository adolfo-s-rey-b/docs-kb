[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.strftime.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.strftime[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.strftime.html#pandas-datetimeindex-strftime "Link to this heading")

=======================================================================================================================================================================

DatetimeIndex.strftime(_date\_format_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimes.py#L1023-L1067)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.strftime.html#pandas.DatetimeIndex.strftime "Link to this definition")

Convert to Index using specified date\_format.

Return an Index of formatted strings specified by date\_format, which supports the same string format as the python standard library. Details of the string format can be found in [python string format doc](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
.

Formats supported by the C strftime API but not by the python string format doc (such as “%R”, “%r”) are not officially supported and should be preferably replaced with their supported equivalents (such as “%H:%M”, “%I:%M:%S %p”). Note that PeriodIndex support additional directives, detailed in Period.strftime.

Parameters:

**date\_format**str

Date format string (e.g. “%Y-%m-%d”).

Returns:

ndarray\[object\]

NumPy ndarray of formatted strings.

See also

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert the given argument to datetime.

[`DatetimeIndex.normalize`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.normalize.html#pandas.DatetimeIndex.normalize "pandas.DatetimeIndex.normalize")

Return DatetimeIndex with times to midnight.

[`DatetimeIndex.round`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.round.html#pandas.DatetimeIndex.round "pandas.DatetimeIndex.round")

Round the DatetimeIndex to the specified freq.

[`DatetimeIndex.floor`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.floor.html#pandas.DatetimeIndex.floor "pandas.DatetimeIndex.floor")

Floor the DatetimeIndex to the specified freq.

[`Timestamp.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html#pandas.Timestamp.strftime "pandas.Timestamp.strftime")

Format a single Timestamp.

[`Period.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html#pandas.Period.strftime "pandas.Period.strftime")

Format a single Period.

Examples

\>>> rng \= pd.date\_range(pd.Timestamp("2018-03-10 09:00"), periods\=3, freq\="s")
\>>> rng.strftime("%B %d, %Y, %r")
Index(\['March 10, 2018, 09:00:00 AM', 'March 10, 2018, 09:00:01 AM',\
       'March 10, 2018, 09:00:02 AM'\],
            dtype='str')

Copy to clipboard

On this page