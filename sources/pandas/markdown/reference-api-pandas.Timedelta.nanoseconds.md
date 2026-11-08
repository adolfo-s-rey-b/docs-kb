[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.nanoseconds.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timedelta.nanoseconds.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.nanoseconds.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timedelta.nanoseconds.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timedelta.nanoseconds.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timedelta.nanoseconds.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timedelta.nanoseconds.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timedelta.nanoseconds.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timedelta.nanoseconds.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timedelta.nanoseconds.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timedelta.nanoseconds.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timedelta.nanoseconds.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timedelta.nanoseconds.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timedelta.nanoseconds.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timedelta.nanoseconds[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.nanoseconds.html#pandas-timedelta-nanoseconds "Link to this heading")

====================================================================================================================================================================

Timedelta.nanoseconds[#](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.nanoseconds.html#pandas.Timedelta.nanoseconds "Link to this definition")

Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.

This is the nanoseconds component of the Timedelta, which represents the residual nanoseconds that are not captured by higher-order components such as days, seconds, or microseconds. The value is always in the range \[0, 999\].

Returns:

int

Number of nanoseconds.

See also

[`Timedelta.components`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.components.html#pandas.Timedelta.components "pandas.Timedelta.components")

Return all attributes with assigned values (i.e. days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds).

Examples

**Using string input**

\>>> td \= pd.Timedelta('1 days 2 min 3 us 42 ns')

Copy to clipboard

\>>> td.nanoseconds
42

Copy to clipboard

**Using integer input**

\>>> td \= pd.Timedelta(42, unit\='ns')
\>>> td.nanoseconds
42

Copy to clipboard

On this page