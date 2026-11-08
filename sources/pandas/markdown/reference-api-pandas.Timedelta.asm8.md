[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.asm8.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.asm8[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.asm8.html#pandas-timedelta-asm8 "Link to this heading")

===============================================================================================================================================

Timedelta.asm8[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.asm8.html#pandas.Timedelta.asm8 "Link to this definition")

Return a numpy timedelta64 array scalar view.

Provides access to the array scalar view (i.e. a combination of the value and the units) associated with the numpy.timedelta64().view(), including a 64-bit integer representation of the timedelta in nanoseconds (Python int compatible).

Returns:

numpy timedelta64 array scalar view

Array scalar view of the timedelta in nanoseconds.

See also

[`Timedelta.total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#pandas.Timedelta.total_seconds "pandas.Timedelta.total_seconds")

Return the total seconds in the duration.

[`Timedelta.components`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas.Timedelta.components "pandas.Timedelta.components")

Return a namedtuple of the Timedelta’s components.

[`Timedelta.to_timedelta64`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_timedelta64.html#pandas.Timedelta.to_timedelta64 "pandas.Timedelta.to_timedelta64")

Convert the Timedelta to a numpy.timedelta64.

Examples

\>>> td \= pd.Timedelta('1 days 2 min 3 us 42 ns')
\>>> td.asm8
np.timedelta64(86520000003042,'ns')

Copy to clipboard

\>>> td \= pd.Timedelta('2 min 3 s')
\>>> td.asm8
np.timedelta64(123000000,'us')

Copy to clipboard

\>>> td \= pd.Timedelta('3 ms 5 us')
\>>> td.asm8
np.timedelta64(3005,'us')

Copy to clipboard

\>>> td \= pd.Timedelta(42, unit\='ns')
\>>> td.asm8
np.timedelta64(42,'ns')

Copy to clipboard

On this page