[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.total_seconds.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.total_seconds.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.total_seconds.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.total_seconds.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.total_seconds.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.total_seconds.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.total_seconds.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.total_seconds.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.total_seconds.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.total_seconds.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.total_seconds.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.total_seconds.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.total\_seconds[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#pandas-timedelta-total-seconds "Link to this heading")

===========================================================================================================================================================================

Timedelta.total\_seconds()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#pandas.Timedelta.total_seconds "Link to this definition")

Total seconds in the duration.

This method calculates the total duration in seconds by combining the days, seconds, microseconds, and nanoseconds of the Timedelta object.

See also

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta.

[`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")

Represents a duration, the difference between two dates or times.

[`Timedelta.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.seconds.html#pandas.Timedelta.seconds "pandas.Timedelta.seconds")

Returns the seconds component of the timedelta.

[`Timedelta.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.microseconds.html#pandas.Timedelta.microseconds "pandas.Timedelta.microseconds")

Returns the microseconds component of the timedelta.

Examples

\>>> td \= pd.Timedelta('1min')
\>>> td
Timedelta('0 days 00:01:00')
\>>> td.total\_seconds()
60.0

Copy to clipboard

On this page