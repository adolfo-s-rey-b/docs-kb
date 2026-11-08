[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_timedelta64.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.to\_timedelta64[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_timedelta64.html#pandas-timedelta-to-timedelta64 "Link to this heading")

==============================================================================================================================================================================

Timedelta.to\_timedelta64()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_timedelta64.html#pandas.Timedelta.to_timedelta64 "Link to this definition")

Return a numpy.timedelta64 object with ‘ns’ precision.

Since NumPy uses `timedelta64` objects for its time operations, converting a pandas `Timedelta` into a NumPy `timedelta64` provides seamless integration between the two libraries, especially when working in environments that heavily rely on NumPy for array-based calculations.

See also

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to timedelta.

[`numpy.timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "(in NumPy v2.5)")

A NumPy object for time duration.

[`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")

Represents a duration, the difference between two dates or times.

Examples

\>>> td \= pd.Timedelta('3D')
\>>> td
Timedelta('3 days 00:00:00')
\>>> td.to\_timedelta64()
np.timedelta64(259200000000,'us')

Copy to clipboard

On this page