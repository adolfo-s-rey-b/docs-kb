[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.FY5253.get\_year\_end[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html#pandas-tseries-offsets-fy5253-get-year-end "Link to this heading")

================================================================================================================================================================================================================

FY5253.get\_year\_end(_dt_)[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.get_year_end.html#pandas.tseries.offsets.FY5253.get_year_end "Link to this definition")

Get the fiscal year end date for the given datetime.

This method calculates the fiscal year end date based on the offset’s weekday, starting month, and variation parameters. The fiscal year end is determined as either the last occurrence of the specified weekday in the starting month, or the occurrence of the specified weekday nearest to the last day of the starting month.

Parameters:

**dt**datetime

A timezone-naive datetime for which to determine the fiscal year end. The year component of this datetime is used to determine which fiscal year end to calculate.

Returns:

datetime

The fiscal year end datetime for the year specified in the input.

See also

[`FY5253`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.FY5253.html#pandas.tseries.offsets.FY5253 "pandas.tseries.offsets.FY5253")

Describes 52-53 week fiscal year.

`FY5253.is_on_offset`

Check if a date is on the offset.

Examples

\>>> from datetime import datetime
\>>> offset \= pd.offsets.FY5253(weekday\=4, startingMonth\=12, variation\="last")
\>>> offset.get\_year\_end(datetime(2022, 6, 15))
datetime.datetime(2022, 12, 30, 0, 0)

Copy to clipboard

\>>> offset \= pd.offsets.FY5253(weekday\=0, startingMonth\=1, variation\="nearest")
\>>> offset.get\_year\_end(datetime(2022, 6, 15))
datetime.datetime(2022, 1, 31, 0, 0)

Copy to clipboard

On this page