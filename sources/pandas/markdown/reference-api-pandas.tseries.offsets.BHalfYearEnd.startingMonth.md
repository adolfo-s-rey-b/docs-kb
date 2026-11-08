[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.BHalfYearEnd.startingMonth[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html#pandas-tseries-offsets-bhalfyearend-startingmonth "Link to this heading")

===================================================================================================================================================================================================================================

BHalfYearEnd.startingMonth[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BHalfYearEnd.startingMonth.html#pandas.tseries.offsets.BHalfYearEnd.startingMonth "Link to this definition")

Return the month of the year that anchors the half-years.

For the `*Begin` offsets this is a month in which a half-year starts, so `startingMonth=1` anchors on January 1 and July 1. For the `*End` offsets it is a month in which a half-year _ends_, so `startingMonth=1` anchors on January 31 and July 31.

See also

`HalfYearOffset.rule_code`

Return the rule code for the half-year offset.

`QuarterOffset.startingMonth`

Similar property for quarter-based offsets.

Examples

A `*Begin` offset starts its half-years in `startingMonth`:

\>>> pd.offsets.HalfYearBegin(startingMonth\=2).startingMonth
2

Copy to clipboard

\>>> pd.Timestamp("2022-01-15") + pd.offsets.HalfYearBegin(startingMonth\=2)
Timestamp('2022-02-01 00:00:00')

Copy to clipboard

An `*End` offset ends its half-years in `startingMonth`:

\>>> pd.offsets.HalfYearEnd(startingMonth\=2).startingMonth
2

Copy to clipboard

\>>> pd.Timestamp("2022-01-15") + pd.offsets.HalfYearEnd(startingMonth\=2)
Timestamp('2022-02-28 00:00:00')

Copy to clipboard

On this page