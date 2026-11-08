[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.days.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.days.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.days.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.days.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.days.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.days.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.days.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.days.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.days.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.days.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.days.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.days.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.days.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.days.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.days[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.days.html#pandas-timedelta-days "Link to this heading")

===============================================================================================================================================

Timedelta.days[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.days.html#pandas.Timedelta.days "Link to this definition")

Returns the days of the timedelta.

The days attribute of a pandas.Timedelta object provides the number of days represented by the Timedelta. This is useful for extracting the day component from a Timedelta that may also include hours, minutes, seconds, and smaller time units. This attribute simplifies the process of working with durations where only the day component is of interest.

Returns:

int

See also

[`Timedelta.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.seconds.html#pandas.Timedelta.seconds "pandas.Timedelta.seconds")

Returns the seconds component of the timedelta.

[`Timedelta.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.microseconds.html#pandas.Timedelta.microseconds "pandas.Timedelta.microseconds")

Returns the microseconds component of the timedelta.

[`Timedelta.total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#pandas.Timedelta.total_seconds "pandas.Timedelta.total_seconds")

Returns the total duration in seconds.

Examples

\>>> td \= pd.Timedelta(1, "D")
\>>> td.days
1

Copy to clipboard

\>>> td \= pd.Timedelta('4 min 3 us 42 ns')
\>>> td.days
0

Copy to clipboard

On this page