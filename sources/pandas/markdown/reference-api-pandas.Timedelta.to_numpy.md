[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_numpy.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.to\_numpy[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_numpy.html#pandas-timedelta-to-numpy "Link to this heading")

============================================================================================================================================================

Timedelta.to\_numpy(_dtype\=None_, _copy\=False_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_numpy.html#pandas.Timedelta.to_numpy "Link to this definition")

Convert the Timedelta to a NumPy timedelta64.

This is an alias method for Timedelta.to\_timedelta64().

Parameters:

**dtype**NoneType

It is available here only for compatibility. Its value will not affect the return value.

**copy**bool, default False

It is available here only for compatibility. Its value will not affect the return value.

Returns:

numpy.timedelta64

See also

[`Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")

Similar method for Series.

Examples

\>>> td \= pd.Timedelta('3D')
\>>> td
Timedelta('3 days 00:00:00')
\>>> td.to\_numpy()
np.timedelta64(259200000000,'us')

Copy to clipboard

On this page