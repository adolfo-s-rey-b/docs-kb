[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.view.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.view.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.view.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.view.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.view.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.view.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.view.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.view.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.view.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.view.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.view.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.view.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.view.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.view.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.view[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.view.html#pandas-timedelta-view "Link to this heading")

===============================================================================================================================================

Timedelta.view(_dtype_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.view.html#pandas.Timedelta.view "Link to this definition")

Array view compatibility.

This method allows you to reinterpret the underlying data of a Timedelta object as a different dtype. The view method provides a way to reinterpret the internal representation of the Timedelta object without modifying its data. This is particularly useful when you need to work with the underlying data directly, such as for performance optimizations or interfacing with low-level APIs. The returned value is typically the number of nanoseconds since the epoch, represented as an integer or another specified dtype.

Parameters:

**dtype**str or dtype

The dtype to view the underlying data as.

See also

[`Timedelta.asm8`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.asm8.html#pandas.Timedelta.asm8 "pandas.Timedelta.asm8")

Return a numpy timedelta64 array scalar view.

[`numpy.ndarray.view`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "(in NumPy v2.5)")

Returns a view of an array with the same data.

[`Timedelta.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_numpy.html#pandas.Timedelta.to_numpy "pandas.Timedelta.to_numpy")

Converts the Timedelta to a NumPy timedelta64.

[`Timedelta.total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.total_seconds.html#pandas.Timedelta.total_seconds "pandas.Timedelta.total_seconds")

Returns the total duration of the Timedelta object in seconds.

Examples

\>>> td \= pd.Timedelta('3D')
\>>> td
Timedelta('3 days 00:00:00')
\>>> td.view(int)
np.int64(259200000000)

Copy to clipboard

On this page