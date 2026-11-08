[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Tick.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.Tick.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Tick.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.Tick.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.Tick.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.Tick.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.Tick.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.Tick.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.Tick.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.Tick.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.Tick.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.Tick.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.Tick.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.Tick.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.Tick[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Tick.html#pandas-tseries-offsets-tick "Link to this heading")

=================================================================================================================================================================

class pandas.tseries.offsets.Tick[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Tick.html#pandas.tseries.offsets.Tick "Link to this definition")

Base class for fixed frequency offsets (Milli, Micro, Second, Minute, Hour).

This class should not be instantiated directly. Use one of the specific Tick subclasses for a concrete offset.

Parameters:

**n**int, default 1

The number of units (hours, minutes, etc.) the offset represents.

See also

[`Hour`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Hour.html#pandas.tseries.offsets.Hour "pandas.tseries.offsets.Hour")

Offset `n` hours.

[`Minute`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Minute.html#pandas.tseries.offsets.Minute "pandas.tseries.offsets.Minute")

Offset `n` minutes.

[`Second`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Second.html#pandas.tseries.offsets.Second "pandas.tseries.offsets.Second")

Offset `n` seconds.

[`Milli`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Milli.html#pandas.tseries.offsets.Milli "pandas.tseries.offsets.Milli")

Offset `n` milliseconds.

[`Micro`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Micro.html#pandas.tseries.offsets.Micro "pandas.tseries.offsets.Micro")

Offset `n` microseconds.

[`Nano`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Nano.html#pandas.tseries.offsets.Nano "pandas.tseries.offsets.Nano")

Offset `n` nanoseconds.

Examples

\>>> from pandas.tseries.offsets import Hour, Minute
\>>> ts \= pd.Timestamp(2022, 12, 9, 15)
\>>> ts
Timestamp('2022-12-09 15:00:00')

Copy to clipboard

\>>> ts + Hour(1)
Timestamp('2022-12-09 16:00:00')

Copy to clipboard

\>>> ts + Minute(30)
Timestamp('2022-12-09 15:30:00')

Copy to clipboard

On this page