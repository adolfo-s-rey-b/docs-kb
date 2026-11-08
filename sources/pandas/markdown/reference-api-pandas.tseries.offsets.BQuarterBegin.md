[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BQuarterBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.html#pandas-tseries-offsets-bquarterbegin "Link to this heading")

============================================================================================================================================================================================

class pandas.tseries.offsets.BQuarterBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.html#pandas.tseries.offsets.BQuarterBegin "Link to this definition")

DateOffset increments between the first business day of each Quarter.

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
| [`startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html#pandas.tseries.offsets.BQuarterBegin.startingMonth "pandas.tseries.offsets.BQuarterBegin.startingMonth") | Return the month of the year that anchors the quarters. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> from pandas.tseries.offsets import BQuarterBegin
\>>> ts \= pd.Timestamp('2020-05-24 05:01:15')
\>>> ts + BQuarterBegin()
Timestamp('2020-06-01 05:01:15')
\>>> ts + BQuarterBegin(2)
Timestamp('2020-09-01 05:01:15')
\>>> ts + BQuarterBegin(startingMonth\=2)
Timestamp('2020-08-03 05:01:15')
\>>> ts + BQuarterBegin(\-1)
Timestamp('2020-03-02 05:01:15')

Copy to clipboard

On this page