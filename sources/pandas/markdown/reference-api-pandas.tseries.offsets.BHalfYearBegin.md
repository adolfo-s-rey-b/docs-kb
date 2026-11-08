[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearBegin.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BHalfYearBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearBegin.html#pandas-tseries-offsets-bhalfyearbegin "Link to this heading")

===============================================================================================================================================================================================

class pandas.tseries.offsets.BHalfYearBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearBegin.html#pandas.tseries.offsets.BHalfYearBegin "Link to this definition")

DateOffset increments between the first business day of each half-year.

startingMonth = 1 corresponds to dates like 1/01/2007, 7/01/2007, … startingMonth = 2 corresponds to dates like 2/01/2007, 8/01/2007, … startingMonth = 3 corresponds to dates like 3/01/2007, 9/01/2007, …

Parameters:

**n**int, default 1

The number of half-years represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**startingMonth**int, default 1

The month of the year in which half-years start.

Attributes

|     |     |
| --- | --- |
| [`startingMonth`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearBegin.startingMonth.html#pandas.tseries.offsets.BHalfYearBegin.startingMonth "pandas.tseries.offsets.BHalfYearBegin.startingMonth") | Return the month of the year that anchors the half-years. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> from pandas.tseries.offsets import BHalfYearBegin
\>>> ts \= pd.Timestamp('2020-05-24 05:01:15')
\>>> ts + BHalfYearBegin()
Timestamp('2020-07-01 05:01:15')
\>>> ts + BHalfYearBegin(2)
Timestamp('2021-01-01 05:01:15')
\>>> ts + BHalfYearBegin(startingMonth\=2)
Timestamp('2020-08-03 05:01:15')
\>>> ts + BHalfYearBegin(\-1)
Timestamp('2020-01-01 05:01:15')

Copy to clipboard

On this page