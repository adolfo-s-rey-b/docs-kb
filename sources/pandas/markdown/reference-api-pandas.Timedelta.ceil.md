[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.ceil.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.ceil[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.ceil.html#pandas-timedelta-ceil "Link to this heading")

===============================================================================================================================================

Timedelta.ceil(_freq_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.ceil.html#pandas.Timedelta.ceil "Link to this definition")

Return a new Timedelta ceiled to this resolution.

Rounds the Timedelta up to the nearest multiple of the given frequency, rounding toward positive infinity.

Parameters:

**freq**str or timedelta

Frequency string or timedelta value indicating the ceiling resolution. Must be a fixed frequency like ‘s’ (second) not ‘ME’ (month end). See [frequency aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
 for a list of possible freq values.

Returns:

Timedelta

A new Timedelta object ceiled to the specified resolution.

See also

[`Timedelta.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.floor.html#pandas.Timedelta.floor "pandas.Timedelta.floor")

Floor the Timedelta to the specified resolution.

[`Timedelta.round`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html#pandas.Timedelta.round "pandas.Timedelta.round")

Round the Timedelta to the specified resolution.

[`Timestamp.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.ceil.html#pandas.Timestamp.ceil "pandas.Timestamp.ceil")

Similar method for Timestamp objects.

Examples

\>>> td \= pd.Timedelta('1001ms')
\>>> td
Timedelta('0 days 00:00:01.001000')
\>>> td.ceil('s')
Timedelta('0 days 00:00:02')

Copy to clipboard

`freq` can also be a timedelta value:

\>>> td.ceil(freq\=pd.Timedelta('1s'))
Timedelta('0 days 00:00:02')

Copy to clipboard

On this page