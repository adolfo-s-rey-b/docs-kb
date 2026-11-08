[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.YearBegin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.YearBegin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.YearBegin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.YearBegin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.YearBegin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.YearBegin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.YearBegin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.YearBegin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.YearBegin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.YearBegin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.YearBegin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.YearBegin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.YearBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.html#pandas-tseries-offsets-yearbegin "Link to this heading")

================================================================================================================================================================================

class pandas.tseries.offsets.YearBegin[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.html#pandas.tseries.offsets.YearBegin "Link to this definition")

DateOffset increments between calendar year begin dates.

YearBegin goes to the next date which is the start of the year.

Parameters:

**n**int, default 1

The number of years represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**month**int, default 1

A specific integer for the month of the year.

Attributes

|     |     |
| --- | --- |
| [`month`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.YearBegin.month.html#pandas.tseries.offsets.YearBegin.month "pandas.tseries.offsets.YearBegin.month") | Return the month of the year on which this offset applies. |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> ts \= pd.Timestamp(2022, 12, 1)
\>>> ts + pd.offsets.YearBegin()
Timestamp('2023-01-01 00:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2023, 1, 1)
\>>> ts + pd.offsets.YearBegin()
Timestamp('2024-01-01 00:00:00')

Copy to clipboard

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.YearBegin(month\=2)
Timestamp('2022-02-01 00:00:00')

Copy to clipboard

If you want to get the start of the current year:

\>>> ts \= pd.Timestamp(2023, 1, 1)
\>>> pd.offsets.YearBegin().rollback(ts)
Timestamp('2023-01-01 00:00:00')

Copy to clipboard

On this page