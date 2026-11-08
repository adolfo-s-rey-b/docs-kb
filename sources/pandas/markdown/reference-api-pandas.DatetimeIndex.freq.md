[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.freq.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DatetimeIndex.freq[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.freq.html#pandas-datetimeindex-freq "Link to this heading")

===========================================================================================================================================================

property DatetimeIndex.freq[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/datetimelike.py#L698-L726)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.freq.html#pandas.DatetimeIndex.freq "Link to this definition")

Return the frequency object if it is set, otherwise None.

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

See also

[`DatetimeIndex.freq`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.freq.html#pandas.DatetimeIndex.freq "pandas.DatetimeIndex.freq")

Return the frequency object if it is set, otherwise None.

[`PeriodIndex.freq`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodIndex.freq.html#pandas.PeriodIndex.freq "pandas.PeriodIndex.freq")

Return the frequency object if it is set, otherwise None.

Examples

\>>> datetimeindex \= pd.date\_range(
...     "2022-02-22 02:22:22", periods\=10, tz\="America/Chicago", freq\="h"
... )
\>>> datetimeindex
DatetimeIndex(\['2022-02-22 02:22:22-06:00', '2022-02-22 03:22:22-06:00',\
               '2022-02-22 04:22:22-06:00', '2022-02-22 05:22:22-06:00',\
               '2022-02-22 06:22:22-06:00', '2022-02-22 07:22:22-06:00',\
               '2022-02-22 08:22:22-06:00', '2022-02-22 09:22:22-06:00',\
               '2022-02-22 10:22:22-06:00', '2022-02-22 11:22:22-06:00'\],
              dtype='datetime64\[us, America/Chicago\]', freq='h')
\>>> datetimeindex.freq
<Hour>

Copy to clipboard

On this page