[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days_in_month.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dt.days_in_month.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days_in_month.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dt.days_in_month.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dt.days_in_month.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dt.days_in_month.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dt.days_in_month.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dt.days_in_month.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dt.days_in_month.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dt.days_in_month.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dt.days_in_month.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dt.days_in_month.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dt.days_in_month.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dt.days_in_month.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dt.days\_in\_month[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days_in_month.html#pandas-series-dt-days-in-month "Link to this heading")

============================================================================================================================================================================

Series.dt.days\_in\_month[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L108-L109)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days_in_month.html#pandas.Series.dt.days_in_month "Link to this definition")

The number of days in the month.

This attribute returns the total number of days in the month for each datetime value in the Series/Index. The value depends on the month and whether the year is a leap year (e.g., February has 29 days in a leap year).

See also

[`Series.dt.day`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day.html#pandas.Series.dt.day "pandas.Series.dt.day")

Return the day of the month.

[`Series.dt.is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_end.html#pandas.Series.dt.is_month_end "pandas.Series.dt.is_month_end")

Return a boolean indicating if the date is the last day of the month.

[`Series.dt.is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_start.html#pandas.Series.dt.is_month_start "pandas.Series.dt.is_month_start")

Return a boolean indicating if the date is the first day of the month.

[`Series.dt.month`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month.html#pandas.Series.dt.month "pandas.Series.dt.month")

Return the month as January=1 through December=12.

Examples

\>>> s \= pd.Series(\["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"\])
\>>> s \= pd.to\_datetime(s)
\>>> s
0   2020-01-01 10:00:00+00:00
1   2020-02-01 11:00:00+00:00
dtype: datetime64\[us, UTC\]
\>>> s.dt.days\_in\_month
0    31
1    29
dtype: int32

Copy to clipboard

On this page