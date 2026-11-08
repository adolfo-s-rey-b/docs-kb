[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253Quarter.year\_has\_extra\_week[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html#pandas-tseries-offsets-fy5253quarter-year-has-extra-week "Link to this heading")

===========================================================================================================================================================================================================================================================

FY5253Quarter.year\_has\_extra\_week(_dt_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.year_has_extra_week.html#pandas.tseries.offsets.FY5253Quarter.year_has_extra_week "Link to this definition")

Return whether the fiscal year containing the given date has 53 weeks.

In a 52-53 week fiscal year, most years have 52 weeks (4 quarters of 13 weeks each), but occasionally a year will have 53 weeks. When this occurs, one quarter will have 14 weeks instead of the standard 13 weeks. This method determines whether the fiscal year containing the given date is a 53-week year.

Parameters:

**dt**datetime

The date to check, which falls within some fiscal year.

Returns:

bool

True if the fiscal year containing dt has 53 weeks, False if it has 52 weeks.

See also

[`FY5253Quarter.get_weeks`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.get_weeks.html#pandas.tseries.offsets.FY5253Quarter.get_weeks "pandas.tseries.offsets.FY5253Quarter.get_weeks")

Get the number of weeks in each quarter.

[`FY5253Quarter.qtr_with_extra_week`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week.html#pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week "pandas.tseries.offsets.FY5253Quarter.qtr_with_extra_week")

Get the quarter number that receives the extra week in 53-week years.

Examples

\>>> offset \= pd.offsets.FY5253Quarter(
...     weekday\=5, startingMonth\=12, qtr\_with\_extra\_week\=1
... )
\>>> offset.year\_has\_extra\_week(pd.Timestamp("2014-04-02"))
True
\>>> offset.year\_has\_extra\_week(pd.Timestamp("2010-04-02"))
False

Copy to clipboard

On this page