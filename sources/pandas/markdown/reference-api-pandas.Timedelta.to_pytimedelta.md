[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_pytimedelta.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.to_pytimedelta.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_pytimedelta.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.to_pytimedelta.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.to_pytimedelta.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.to_pytimedelta.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.to_pytimedelta.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.to_pytimedelta.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.to_pytimedelta.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.to_pytimedelta.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.to_pytimedelta.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.to_pytimedelta.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.to_pytimedelta.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.to_pytimedelta.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.to\_pytimedelta[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_pytimedelta.html#pandas-timedelta-to-pytimedelta "Link to this heading")

==============================================================================================================================================================================

Timedelta.to\_pytimedelta()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.to_pytimedelta.html#pandas.Timedelta.to_pytimedelta "Link to this definition")

Convert a pandas Timedelta object into a python `datetime.timedelta` object.

Timedelta objects are internally saved as numpy datetime64\[ns\] dtype. Use to\_pytimedelta() to convert to object dtype.

Returns:

datetime.timedelta or numpy.array of datetime.timedelta

See also

[`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")

Convert argument to Timedelta type.

Notes

Any nanosecond resolution will be lost.

Examples

\>>> td \= pd.Timedelta('3D')
\>>> td
Timedelta('3 days 00:00:00')
\>>> td.to\_pytimedelta()
datetime.timedelta(days=3)

Copy to clipboard

On this page