[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BQuarterBegin.startingMonth[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html#pandas-tseries-offsets-bquarterbegin-startingmonth "Link to this heading")

======================================================================================================================================================================================================================================

BQuarterBegin.startingMonth[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BQuarterBegin.startingMonth.html#pandas.tseries.offsets.BQuarterBegin.startingMonth "Link to this definition")

Return the month of the year that anchors the quarters.

For the `*Begin` offsets this is a month in which a quarter starts, so `startingMonth=1` anchors on January 1, April 1, July 1 and October 1. For the `*End` offsets it is a month in which a quarter _ends_, so `startingMonth=1` anchors on January 31, April 30, July 31 and October 31.

See also

`QuarterOffset.rule_code`

Return the rule code for the quarter offset.

`HalfYearOffset.startingMonth`

Similar property for half-year-based offsets.

Examples

A `*Begin` offset starts its quarters in `startingMonth`:

\>>> pd.offsets.QuarterBegin(startingMonth\=2).startingMonth
2

Copy to clipboard

\>>> pd.Timestamp("2022-01-15") + pd.offsets.QuarterBegin(startingMonth\=2)
Timestamp('2022-02-01 00:00:00')

Copy to clipboard

An `*End` offset ends its quarters in `startingMonth`:

\>>> pd.offsets.QuarterEnd(startingMonth\=2).startingMonth
2

Copy to clipboard

\>>> pd.Timestamp("2022-01-15") + pd.offsets.QuarterEnd(startingMonth\=2)
Timestamp('2022-02-28 00:00:00')

Copy to clipboard

On this page