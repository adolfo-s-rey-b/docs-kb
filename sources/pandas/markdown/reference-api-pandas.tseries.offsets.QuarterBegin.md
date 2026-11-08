[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.QuarterBegin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.QuarterBegin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.QuarterBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.html#pandas-tseries-offsets-quarterbegin "Link to this heading")

=========================================================================================================================================================================================

class pandas.tseries.offsets.QuarterBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.html#pandas.tseries.offsets.QuarterBegin "Link to this definition")

DateOffset increments between Quarter start dates.

startingMonth = 1 corresponds to dates like 1/01/2007, 4/01/2007, … startingMonth = 2 corresponds to dates like 2/01/2007, 5/01/2007, … startingMonth = 3 corresponds to dates like 3/01/2007, 6/01/2007, …

Parameters:

**n**int, default 1

The number of quarters represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**startingMonth**int, default 3

The month of the year in which quarters start.

Attributes

|     |     |
| --- | --- |
| [`startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.QuarterBegin.startingMonth.html#pandas.tseries.offsets.QuarterBegin.startingMonth "pandas.tseries.offsets.QuarterBegin.startingMonth") | Return the month of the year that anchors the quarters. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.QuarterBegin()
Timestamp('2022-03-01 00:00:00')

Copy to clipboard

On this page