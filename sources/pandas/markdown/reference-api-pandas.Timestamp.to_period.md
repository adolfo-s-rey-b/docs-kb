[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_period.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.to_period.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_period.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.to_period.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.to_period.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.to_period.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.to_period.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.to_period.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.to_period.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.to_period.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.to_period.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.to_period.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.to_period.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.to_period.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.to\_period[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_period.html#pandas-timestamp-to-period "Link to this heading")

===============================================================================================================================================================

Timestamp.to\_period(_freq\=None_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_period.html#pandas.Timestamp.to_period "Link to this definition")

Return a period of which this timestamp is an observation.

This method converts the given Timestamp to a Period object, which represents a span of time,such as a year, month, etc., based on the specified frequency.

Parameters:

**freq**str, optional

Frequency string for the period (e.g., ‘Y’, ‘M’, ‘W’). Defaults to None.

See also

[`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")

Represents a specific timestamp.

[`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")

Represents a span of time.

[`to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_period.html#pandas.Timestamp.to_period "pandas.Timestamp.to_period")

Converts an object to a Period.

Examples

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651')
\>>> \# Year end frequency
\>>> ts.to\_period(freq\='Y')
Period('2020', 'Y-DEC')

Copy to clipboard

\>>> \# Month end frequency
\>>> ts.to\_period(freq\='M')
Period('2020-03', 'M')

Copy to clipboard

\>>> \# Weekly frequency
\>>> ts.to\_period(freq\='W')
Period('2020-03-09/2020-03-15', 'W-SUN')

Copy to clipboard

\>>> \# Quarter end frequency
\>>> ts.to\_period(freq\='Q')
Period('2020Q1', 'Q-DEC')

Copy to clipboard

On this page