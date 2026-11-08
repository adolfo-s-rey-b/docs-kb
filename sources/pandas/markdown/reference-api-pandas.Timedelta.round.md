[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.round.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.round.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.round.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.round.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.round.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.round.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.round.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.round.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.round.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.round.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.round.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.round.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.round[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html#pandas-timedelta-round "Link to this heading")

==================================================================================================================================================

Timedelta.round(_freq_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.round.html#pandas.Timedelta.round "Link to this definition")

Round the Timedelta to the specified resolution.

Rounds the Timedelta value to the nearest multiple of the given frequency using half-even rounding.

Parameters:

**freq**str or timedelta

Frequency string or timedelta value indicating the rounding resolution. It uses the same units as class constructor [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
.

Returns:

a new Timedelta rounded to the given resolution of freq

Raises:

ValueError if the freq cannot be converted

See also

[`Timedelta.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.floor.html#pandas.Timedelta.floor "pandas.Timedelta.floor")

Floor the Timedelta to the specified resolution.

[`Timedelta.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.ceil.html#pandas.Timedelta.ceil "pandas.Timedelta.ceil")

Ceil the Timedelta to the specified resolution.

[`Timestamp.round`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.round.html#pandas.Timestamp.round "pandas.Timestamp.round")

Similar method for Timestamp objects.

Examples

\>>> td \= pd.Timedelta('1001ms')
\>>> td
Timedelta('0 days 00:00:01.001000')
\>>> td.round('s')
Timedelta('0 days 00:00:01')

Copy to clipboard

`freq` can also be a timedelta value:

\>>> td.round(freq\=pd.Timedelta('1s'))
Timedelta('0 days 00:00:01')

Copy to clipboard

On this page