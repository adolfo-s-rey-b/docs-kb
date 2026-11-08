[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.freq.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.freq[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.freq.html#pandas-period-freq "Link to this heading")

======================================================================================================================================

Period.freq[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.freq.html#pandas.Period.freq "Link to this definition")

Return the frequency object for this Period.

The frequency object represents the span of time that this Period covers. It is a DateOffset that defines the interval type (e.g., daily, monthly).

See also

[`Period.freqstr`](https://pandas.pydata.org/docs/reference/api/pandas.Period.freqstr.html#pandas.Period.freqstr "pandas.Period.freqstr")

Return a string representation of the frequency.

[`Period.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#pandas.Period.asfreq "pandas.Period.asfreq")

Convert Period to desired frequency.

Examples

\>>> period \= pd.Period('2020-01', freq\='M')
\>>> period.freq
<MonthEnd>

Copy to clipboard

On this page