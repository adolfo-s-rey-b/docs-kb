[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterEnd.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BQuarterEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterEnd.html#pandas-tseries-offsets-bquarterend "Link to this heading")

======================================================================================================================================================================================

class pandas.tseries.offsets.BQuarterEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterEnd.html#pandas.tseries.offsets.BQuarterEnd "Link to this definition")

DateOffset increments between the last business day of each Quarter.

startingMonth = 1 corresponds to dates like 1/31/2007, 4/30/2007, … startingMonth = 2 corresponds to dates like 2/28/2007, 5/31/2007, … startingMonth = 3 corresponds to dates like 3/30/2007, 6/29/2007, …

Parameters:

**n**int, default 1

The number of quarters represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**startingMonth**int, default 3

The month of the year in which quarters end.

Attributes

|     |     |
| --- | --- |
| [`startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterEnd.startingMonth.html#pandas.tseries.offsets.BQuarterEnd.startingMonth "pandas.tseries.offsets.BQuarterEnd.startingMonth") | Return the month of the year that anchors the quarters. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> from pandas.tseries.offsets import BQuarterEnd
\>>> ts \= pd.Timestamp('2020-05-24 05:01:15')
\>>> ts + BQuarterEnd()
Timestamp('2020-06-30 05:01:15')
\>>> ts + BQuarterEnd(2)
Timestamp('2020-09-30 05:01:15')
\>>> ts + BQuarterEnd(1, startingMonth\=2)
Timestamp('2020-05-29 05:01:15')
\>>> ts + BQuarterEnd(startingMonth\=2)
Timestamp('2020-05-29 05:01:15')

Copy to clipboard

On this page