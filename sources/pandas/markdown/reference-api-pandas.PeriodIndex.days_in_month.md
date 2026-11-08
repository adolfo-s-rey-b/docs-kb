[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.days_in_month.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.PeriodIndex.days_in_month.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.days_in_month.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.PeriodIndex.days_in_month.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.PeriodIndex.days_in_month.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.PeriodIndex.days_in_month.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.PeriodIndex.days_in_month.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.PeriodIndex.days_in_month.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.PeriodIndex.days_in_month.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.PeriodIndex.days_in_month.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.PeriodIndex.days_in_month.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.PeriodIndex.days_in_month.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.PeriodIndex.days_in_month.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.PeriodIndex.days_in_month.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.PeriodIndex.days\_in\_month[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.days_in_month.html#pandas-periodindex-days-in-month "Link to this heading")

==================================================================================================================================================================================

property PeriodIndex.days\_in\_month[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/period.py#L687-L706)
[#](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.days_in_month.html#pandas.PeriodIndex.days_in_month "Link to this definition")

The number of days in the month.

Returns the total number of days in the month of each period, accounting for leap years.

See also

[`PeriodIndex.day`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.day.html#pandas.PeriodIndex.day "pandas.PeriodIndex.day")

The days of the period.

[`PeriodIndex.month`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.month.html#pandas.PeriodIndex.month "pandas.PeriodIndex.month")

The month as January=1, December=12.

Examples

\>>> idx \= pd.PeriodIndex(\["2023-01", "2023-02", "2023-03"\], freq\="M")
\>>> idx.days\_in\_month
Index(\[31, 28, 31\], dtype='int64')

Copy to clipboard

On this page