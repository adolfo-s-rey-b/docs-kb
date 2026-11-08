[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.asm8.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.asm8.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.asm8.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.asm8.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.asm8.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.asm8.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.asm8.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.asm8.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.asm8.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.asm8.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.asm8.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.asm8.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.asm8.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.asm8.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.asm8[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.asm8.html#pandas-timestamp-asm8 "Link to this heading")

===============================================================================================================================================

Timestamp.asm8[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.asm8.html#pandas.Timestamp.asm8 "Link to this definition")

Return numpy datetime64 format with same precision.

This property provides interoperability with NumPy datetime operations.

See also

[`numpy.datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")

Numpy datatype for dates and times with high precision.

[`Timestamp.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html#pandas.Timestamp.to_numpy "pandas.Timestamp.to_numpy")

Convert the Timestamp to a NumPy datetime64.

[`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")

Convert argument to datetime.

Examples

\>>> ts \= pd.Timestamp(2020, 3, 14, 15)
\>>> ts.asm8
np.datetime64('2020-03-14T15:00:00.000000')

Copy to clipboard

On this page