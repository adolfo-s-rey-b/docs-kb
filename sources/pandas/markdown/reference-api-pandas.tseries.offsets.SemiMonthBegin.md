[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.SemiMonthBegin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.SemiMonthBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.html#pandas-tseries-offsets-semimonthbegin "Link to this heading")

===============================================================================================================================================================================================

class pandas.tseries.offsets.SemiMonthBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.html#pandas.tseries.offsets.SemiMonthBegin "Link to this definition")

Two DateOffset’s per month repeating on the first day of the month & day\_of\_month.

This offset moves dates to the first day of the month and an additional specified day (typically the 15th by default), useful in scenarios where bi-monthly processing occurs on set days.

Parameters:

**n**int, default 1

The number of months represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**day\_of\_month**int, {1, 3,…,27}, default 15

A specific integer for the day of the month.

Attributes

|     |     |
| --- | --- |
| [`day_of_month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthBegin.day_of_month.html#pandas.tseries.offsets.SemiMonthBegin.day_of_month "pandas.tseries.offsets.SemiMonthBegin.day_of_month") | Return the day of the month for the semi-monthly offset. |

See also

`tseries.offsets.SemiMonthEnd`

Two DateOffset’s per month repeating on the last day of the month & day\_of\_month.

`tseries.offsets.MonthEnd`

Offset to the last calendar day of the month.

`tseries.offsets.MonthBegin`

Offset to the first calendar day of the month.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.SemiMonthBegin()
Timestamp('2022-01-15 00:00:00')

Copy to clipboard

On this page