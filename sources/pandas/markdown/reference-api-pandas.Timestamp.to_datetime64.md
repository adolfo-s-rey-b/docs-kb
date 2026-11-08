[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.to_datetime64.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.to_datetime64.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.to_datetime64.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.to_datetime64.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.to_datetime64.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.to_datetime64.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.to_datetime64.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.to_datetime64.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.to_datetime64.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.to_datetime64.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.to_datetime64.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.to_datetime64.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.to\_datetime64[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html#pandas-timestamp-to-datetime64 "Link to this heading")

===========================================================================================================================================================================

Timestamp.to\_datetime64()[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_datetime64.html#pandas.Timestamp.to_datetime64 "Link to this definition")

Return a NumPy datetime64 object with same precision.

This method returns a numpy.datetime64 object with the same date and time information and precision as the pd.Timestamp object.

See also

[`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")

Class to represent dates and times with high precision.

[`Timestamp.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html#pandas.Timestamp.to_numpy "pandas.Timestamp.to_numpy")

Alias for this method.

[`Timestamp.asm8`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.asm8.html#pandas.Timestamp.asm8 "pandas.Timestamp.asm8")

Alias for this method.

`pd.to_datetime`

Convert argument to datetime.

Examples

\>>> ts \= pd.Timestamp(year\=2023, month\=1, day\=1,
...                   hour\=10, second\=15)
\>>> ts
Timestamp('2023-01-01 10:00:15')
\>>> ts.to\_datetime64()
np.datetime64('2023-01-01T10:00:15.000000')

Copy to clipboard

On this page