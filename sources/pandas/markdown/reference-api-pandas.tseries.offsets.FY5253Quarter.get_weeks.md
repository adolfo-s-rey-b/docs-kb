[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253Quarter.get\_weeks[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html#pandas-tseries-offsets-fy5253quarter-get-weeks "Link to this heading")

===========================================================================================================================================================================================================================

FY5253Quarter.get\_weeks(_dt_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html#pandas.tseries.offsets.FY5253Quarter.get_weeks "Link to this definition")

Get the number of weeks in each quarter for the fiscal year containing dt.

In a 52-53 week fiscal year, most years have 52 weeks (13 weeks per quarter). In years with 53 weeks, one quarter will have 14 weeks as determined by the qtr\_with\_extra\_week attribute.

Parameters:

**dt**datetime

The date within the fiscal year to determine quarter week counts.

Returns:

list of int

A list of 4 integers representing the number of weeks in each quarter (Q1, Q2, Q3, Q4). Values are typically \[13, 13, 13, 13\] for 52-week years, with one value being 14 in 53-week years.

See also

[`FY5253Quarter.qtr_with_extra_week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html#pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week "pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week")

The quarter that receives the extra week.

[`FY5253Quarter.year_has_extra_week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html#pandas.tseries.offsets.FY5253Quarter.year_has_extra_week "pandas.tseries.offsets.FY5253Quarter.year_has_extra_week")

Check if a given year has 53 weeks.

Examples

\>>> offset \= pd.offsets.FY5253Quarter(
...     weekday\=5, startingMonth\=12, qtr\_with\_extra\_week\=4
... )
\>>> dt \= pd.Timestamp("2024-01-15")
\>>> offset.get\_weeks(dt)
\[13, 13, 13, 13\]

Copy to clipboard

On this page