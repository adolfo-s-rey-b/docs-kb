[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Easter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.tseries.offsets.Easter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Easter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.tseries.offsets.Easter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.tseries.offsets.Easter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.tseries.offsets.Easter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.tseries.offsets.Easter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.tseries.offsets.Easter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.tseries.offsets.Easter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.tseries.offsets.Easter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.tseries.offsets.Easter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.tseries.offsets.Easter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.tseries.offsets.Easter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.tseries.offsets.Easter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.tseries.offsets.Easter[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Easter.html#pandas-tseries-offsets-easter "Link to this heading")

=======================================================================================================================================================================

class pandas.tseries.offsets.Easter[#](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.Easter.html#pandas.tseries.offsets.Easter "Link to this definition")

DateOffset for the Easter holiday using logic defined in dateutil.

Right now uses the revised method which is valid in years 1583-4099.

Parameters:

**n**int, default 1

The number of years represented.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**method**int, default 3

The method used to calculate the date of Easter. Valid options are: - 1 (EASTER\_JULIAN): Original calculation in Julian calendar - 2 (EASTER\_ORTHODOX): Original method, date converted to Gregorian calendar - 3 (EASTER\_WESTERN): Revised method, in Gregorian calendar These constants are defined in the dateutil.easter module.

Attributes

|     |     |
| --- | --- |
| **method** |     |

See also

[`DateOffset`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.DateOffset.html#pandas.tseries.offsets.DateOffset "pandas.tseries.offsets.DateOffset")

Standard kind of date increment.

Examples

\>>> ts \= pd.Timestamp(2022, 1, 1)
\>>> ts + pd.offsets.Easter()
Timestamp('2022-04-17 00:00:00')

Copy to clipboard

On this page