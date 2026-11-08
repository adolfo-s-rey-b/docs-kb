[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Period.freqstr.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Period.freqstr.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Period.freqstr.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Period.freqstr.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Period.freqstr.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Period.freqstr.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Period.freqstr.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Period.freqstr.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Period.freqstr.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Period.freqstr.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Period.freqstr.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Period.freqstr.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Period.freqstr.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Period.freqstr.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Period.freqstr[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.freqstr.html#pandas-period-freqstr "Link to this heading")

===============================================================================================================================================

Period.freqstr[#](https://pandas.pydata.org/docs/reference/api/pandas.Period.freqstr.html#pandas.Period.freqstr "Link to this definition")

Return a string representation of the frequency.

This property provides the frequency string associated with the Period object. The frequency string describes the granularity of the time span represented by the Period. Common frequency strings include ‘D’ for daily, ‘M’ for monthly, ‘Y’ for yearly, etc.

See also

[`Period.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.Period.asfreq.html#pandas.Period.asfreq "pandas.Period.asfreq")

Convert Period to desired frequency, at the start or end of the interval.

[`period_range`](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas.period_range "pandas.period_range")

Return a fixed frequency PeriodIndex.

Examples

\>>> pd.Period('2020-01', 'D').freqstr
'D'

Copy to clipboard

On this page