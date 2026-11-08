[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.SemiMonthEnd.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.SemiMonthEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.html#pandas-tseries-offsets-semimonthend "Link to this heading")

=========================================================================================================================================================================================

class pandas.tseries.offsets.SemiMonthEnd[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.html#pandas.tseries.offsets.SemiMonthEnd "Link to this definition")

Two DateOffset’s per month repeating on the last day of the month & day\_of\_month.

This offset allows for flexibility in generating date ranges or adjusting dates to the end of a month or a specific day in the month, such as the 15th or the last day of the month. It is useful for financial or scheduling applications where events occur bi-monthly.

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
| [`day_of_month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.SemiMonthEnd.day_of_month.html#pandas.tseries.offsets.SemiMonthEnd.day_of_month "pandas.tseries.offsets.SemiMonthEnd.day_of_month") | Return the day of the month for the semi-monthly offset. |

See also

`tseries.offsets.SemiMonthBegin`

Offset for semi-monthly frequencies, starting at the beginning of the month.

`tseries.offsets.MonthEnd`

Offset to the last calendar day of the month.

`tseries.offsets.MonthBegin`

Offset to the first calendar day of the month.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 14)
\>>> ts + pd.offsets.SemiMonthEnd()
Timestamp('2022-01-15 00:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 1, 15)
\>>> ts + pd.offsets.SemiMonthEnd()
Timestamp('2022-01-31 00:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 1, 31)
\>>> ts + pd.offsets.SemiMonthEnd()
Timestamp('2022-02-15 00:00:00')

Copy to clipboard

If you want to get the result for the current month:

\>>> ts \= pd.Timestamp(2022, 1, 15)
\>>> pd.offsets.SemiMonthEnd().rollforward(ts)
Timestamp('2022-01-15 00:00:00')

Copy to clipboard

On this page