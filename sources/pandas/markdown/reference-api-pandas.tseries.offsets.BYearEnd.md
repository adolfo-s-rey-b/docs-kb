[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BYearEnd.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BYearEnd.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BYearEnd.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BYearEnd.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BYearEnd.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BYearEnd.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BYearEnd.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BYearEnd.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BYearEnd.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BYearEnd.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BYearEnd.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BYearEnd.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BYearEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.html#pandas-tseries-offsets-byearend "Link to this heading")

=============================================================================================================================================================================

class pandas.tseries.offsets.BYearEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.html#pandas.tseries.offsets.BYearEnd "Link to this definition")

DateOffset increments between the last business day of the year.

This offset moves dates to the last business day of the specified month (default December), skipping weekends.

Parameters:

**n**int, default 1

The number of years represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**month**int, default 12

A specific integer for the month of the year.

Attributes

|     |     |
| --- | --- |
| [`month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BYearEnd.month.html#pandas.tseries.offsets.BYearEnd.month "pandas.tseries.offsets.BYearEnd.month") | Return the month of the year on which this offset applies. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> from pandas.tseries.offsets import BYearEnd
\>>> ts \= pd.Timestamp('2020-05-24 05:01:15')
\>>> ts \- BYearEnd()
Timestamp('2019-12-31 05:01:15')
\>>> ts + BYearEnd()
Timestamp('2020-12-31 05:01:15')
\>>> ts + BYearEnd(3)
Timestamp('2022-12-30 05:01:15')
\>>> ts + BYearEnd(\-3)
Timestamp('2017-12-29 05:01:15')
\>>> ts + BYearEnd(month\=11)
Timestamp('2020-11-30 05:01:15')

Copy to clipboard

On this page