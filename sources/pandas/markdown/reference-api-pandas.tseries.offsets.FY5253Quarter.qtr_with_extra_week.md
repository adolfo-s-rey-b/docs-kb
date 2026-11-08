[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253Quarter.qtr\_with\_extra\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html#pandas-tseries-offsets-fy5253quarter-qtr-with-extra-week "Link to this heading")

===========================================================================================================================================================================================================================================================

FY5253Quarter.qtr\_with\_extra\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html#pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week "Link to this definition")

Return the quarter number that has the leap or 14 week when needed.

In a 52-53 week fiscal year, when a year has 53 weeks, one quarter will have 14 weeks instead of the standard 13 weeks. This property indicates which quarter (1, 2, 3, or 4) receives the extra week.

Returns:

int

The quarter number (1, 2, 3, or 4) that contains the extra week in 53-week years.

See also

[`FY5253Quarter.get_weeks`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html#pandas.tseries.offsets.FY5253Quarter.get_weeks "pandas.tseries.offsets.FY5253Quarter.get_weeks")

Get the number of weeks in each quarter.

[`FY5253Quarter.year_has_extra_week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html#pandas.tseries.offsets.FY5253Quarter.year_has_extra_week "pandas.tseries.offsets.FY5253Quarter.year_has_extra_week")

Check if a given year has 53 weeks.

Examples

\>>> offset \= pd.offsets.FY5253Quarter(
...     weekday\=5, startingMonth\=12, qtr\_with\_extra\_week\=4
... )
\>>> offset.qtr\_with\_extra\_week
4

Copy to clipboard

On this page