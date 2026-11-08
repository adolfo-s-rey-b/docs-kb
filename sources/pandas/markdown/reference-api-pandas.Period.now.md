[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.now.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.now.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.now.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.now.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.now.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.now.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.now.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.now.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.now.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.now.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.now.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.now.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.now.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.now.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.now[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.now.html#pandas-period-now "Link to this heading")

===================================================================================================================================

classmethod Period.now(_freq_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.now.html#pandas.Period.now "Link to this definition")

Return the period of now’s date.

The now method provides a convenient way to generate a period object for the current date and time. This can be particularly useful in financial and economic analysis, where data is often collected and analyzed in regular intervals (e.g., hourly, daily, monthly). By specifying the frequency, users can create periods that match the granularity of their data.

Parameters:

**freq**str, DateOffset

Frequency to use for the returned period.

See also

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

[`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")

Represents a period of time.

[`Period.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Period.to_timestamp.html#pandas.Period.to_timestamp "pandas.Period.to_timestamp")

Return the Timestamp representation of the Period.

Examples

\>>> pd.Period.now('h')
Period('2023-06-12 11:00', 'h')

Copy to clipboard

On this page