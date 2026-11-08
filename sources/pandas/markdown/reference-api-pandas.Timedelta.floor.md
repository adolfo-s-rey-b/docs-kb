[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.floor.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.floor[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.floor.html#pandas-timedelta-floor "Link to this heading")

==================================================================================================================================================

Timedelta.floor(_freq_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.floor.html#pandas.Timedelta.floor "Link to this definition")

Return a new Timedelta floored to this resolution.

Truncates the Timedelta to the nearest multiple of the given frequency, rounding toward negative infinity.

Parameters:

**freq**str or timedelta

Frequency string or timedelta value indicating the flooring resolution. It uses the same units as class constructor [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
.

Returns:

Timedelta

A new Timedelta object floored to the specified resolution.

See also

[`Timedelta.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.ceil.html#pandas.Timedelta.ceil "pandas.Timedelta.ceil")

Ceil the Timedelta to the specified resolution.

[`Timedelta.round`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html#pandas.Timedelta.round "pandas.Timedelta.round")

Round the Timedelta to the specified resolution.

[`Timestamp.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.floor.html#pandas.Timestamp.floor "pandas.Timestamp.floor")

Similar method for Timestamp objects.

Examples

\>>> td \= pd.Timedelta('1001ms')
\>>> td
Timedelta('0 days 00:00:01.001000')
\>>> td.floor('s')
Timedelta('0 days 00:00:01')

Copy to clipboard

`freq` can also be a timedelta value:

\>>> td.floor(freq\=pd.Timedelta('1s'))
Timedelta('0 days 00:00:01')

Copy to clipboard

On this page