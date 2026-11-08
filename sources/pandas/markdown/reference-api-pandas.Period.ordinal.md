[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.ordinal.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.ordinal.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.ordinal.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.ordinal.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.ordinal.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.ordinal.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.ordinal.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.ordinal.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.ordinal.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.ordinal.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.ordinal.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.ordinal.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.ordinal.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.ordinal.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.ordinal[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.ordinal.html#pandas-period-ordinal "Link to this heading")

===============================================================================================================================================

Period.ordinal[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.ordinal.html#pandas.Period.ordinal "Link to this definition")

Return the integer ordinal for this Period.

The ordinal is the internal integer representation of the Period, representing its position in the sequence of periods of the given frequency. It counts from an epoch (e.g., for daily frequency, ordinal 0 corresponds to January 1, 1970).

See also

[`Period.freq`](https://pandas.pydata.org/docs/reference/api/pandas.Period.freq.html#pandas.Period.freq "pandas.Period.freq")

Return the frequency of the Period.

[`Period.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.Period.start_time.html#pandas.Period.start_time "pandas.Period.start_time")

Return the start time of the Period.

Examples

\>>> period \= pd.Period('2020-01', freq\='M')
\>>> period.ordinal
600

Copy to clipboard

\>>> period \= pd.Period('2020-01-01', freq\='D')
\>>> period.ordinal
18262

Copy to clipboard

On this page