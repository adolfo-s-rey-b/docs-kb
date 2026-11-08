[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.Week.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.Week.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.Week.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.Week.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.Week.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.Week.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.Week.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.Week.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.Week.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.Week.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.Week.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.Week.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.Week[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.html#pandas-tseries-offsets-week "Link to this heading")

=================================================================================================================================================================

class pandas.tseries.offsets.Week[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.html#pandas.tseries.offsets.Week "Link to this definition")

Weekly offset.

This offset represents a duration of one or more weeks. It can optionally be anchored to a specific day of the week, which represents the last day of the weekly period. For example, `W-MON` produces weekly periods that end on Monday (and start on Tuesday).

Parameters:

**n**int, default 1

The number of weeks represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**weekday**int or None, default None

Always generate specific day of week. 0 for Monday and 6 for Sunday.

Attributes

|     |     |
| --- | --- |
| [`weekday`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Week.weekday.html#pandas.tseries.offsets.Week.weekday "pandas.tseries.offsets.Week.weekday") | Return the day of the week on which the offset is applied. |

See also

`pd.tseries.offsets.WeekOfMonth`

Describes monthly dates like, the Tuesday of the 2nd week of each month.

Examples

\>>> date\_object \= pd.Timestamp("2023-01-13")
\>>> date\_object
Timestamp('2023-01-13 00:00:00')

Copy to clipboard

\>>> date\_plus\_one\_week \= date\_object + pd.tseries.offsets.Week(n\=1)
\>>> date\_plus\_one\_week
Timestamp('2023-01-20 00:00:00')

Copy to clipboard

\>>> date\_next\_monday \= date\_object + pd.tseries.offsets.Week(weekday\=0)
\>>> date\_next\_monday
Timestamp('2023-01-16 00:00:00')

Copy to clipboard

\>>> date\_next\_sunday \= date\_object + pd.tseries.offsets.Week(weekday\=6)
\>>> date\_next\_sunday
Timestamp('2023-01-15 00:00:00')

Copy to clipboard

On this page