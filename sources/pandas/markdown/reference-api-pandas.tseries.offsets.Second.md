[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Second.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.Second.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Second.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.Second.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.Second.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.Second.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.Second.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.Second.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.Second.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.Second.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.Second.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.Second.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.Second.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.Second.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.Second[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Second.html#pandas-tseries-offsets-second "Link to this heading")

=======================================================================================================================================================================

class pandas.tseries.offsets.Second[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Second.html#pandas.tseries.offsets.Second "Link to this definition")

Offset `n` seconds.

Represents a fixed duration of `n` seconds for use in arithmetic with datetime-like objects. The smallest tick offset that does not involve fractional seconds.

Parameters:

**n**int, default 1

The number of seconds represented.

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

You can use the parameter `n` to represent a shift of n seconds.

\>>> from pandas.tseries.offsets import Second
\>>> ts \= pd.Timestamp(2022, 12, 9, 15)
\>>> ts
Timestamp('2022-12-09 15:00:00')

Copy to clipboard

\>>> ts + Second(n\=10)
Timestamp('2022-12-09 15:00:10')
\>>> ts \- Second(n\=10)
Timestamp('2022-12-09 14:59:50')

Copy to clipboard

\>>> ts + Second(n\=-10)
Timestamp('2022-12-09 14:59:50')

Copy to clipboard

On this page