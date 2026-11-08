[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BaseOffset.freqstr[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html#pandas-tseries-offsets-baseoffset-freqstr "Link to this heading")

===========================================================================================================================================================================================================

BaseOffset.freqstr[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BaseOffset.freqstr.html#pandas.tseries.offsets.BaseOffset.freqstr "Link to this definition")

Return a string representing the frequency.

The string representation typically consists of the offset multiplier and a frequency alias (e.g., `'D'` for daily, `'h'` for hourly).

See also

`tseries.offsets.BusinessDay.freqstr`

Return a string representing an offset frequency in Business Days.

`tseries.offsets.BusinessHour.freqstr`

Return a string representing an offset frequency in Business Hours.

`tseries.offsets.Week.freqstr`

Return a string representing an offset frequency in Weeks.

`tseries.offsets.Hour.freqstr`

Return a string representing an offset frequency in Hours.

Examples

\>>> pd.DateOffset(5).freqstr
'<5 \* DateOffsets>'

Copy to clipboard

\>>> pd.offsets.BusinessHour(2).freqstr
'2bh'

Copy to clipboard

\>>> pd.offsets.Nano().freqstr
'ns'

Copy to clipboard

\>>> pd.offsets.Nano(\-3).freqstr
'-3ns'

Copy to clipboard

On this page