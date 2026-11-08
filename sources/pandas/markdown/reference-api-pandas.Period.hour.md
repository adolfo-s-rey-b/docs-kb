[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.hour.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.hour.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.hour.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.hour.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.hour.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.hour.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.hour.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.hour.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.hour.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.hour.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.hour.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.hour.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.hour.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.hour.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.hour[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.hour.html#pandas-period-hour "Link to this heading")

======================================================================================================================================

Period.hour[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.hour.html#pandas.Period.hour "Link to this definition")

Get the hour of the day component of the Period.

For periods with a frequency shorter than a day, this returns the hour portion of the time. For longer frequencies, it returns 0.

Returns:

int

The hour as an integer, between 0 and 23.

See also

[`Period.second`](https://pandas.pydata.org/docs/reference/api/pandas.Period.second.html#pandas.Period.second "pandas.Period.second")

Get the second component of the Period.

[`Period.minute`](https://pandas.pydata.org/docs/reference/api/pandas.Period.minute.html#pandas.Period.minute "pandas.Period.minute")

Get the minute component of the Period.

Examples

\>>> p \= pd.Period("2018-03-11 13:03:12.050000")
\>>> p.hour
13

Copy to clipboard

Period longer than a day

\>>> p \= pd.Period("2018-03-11", freq\="M")
\>>> p.hour
0

Copy to clipboard

On this page