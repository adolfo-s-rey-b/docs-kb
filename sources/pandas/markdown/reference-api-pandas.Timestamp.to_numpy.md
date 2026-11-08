[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Timestamp.to_numpy.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Timestamp.to_numpy.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Timestamp.to_numpy.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Timestamp.to_numpy.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Timestamp.to_numpy.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Timestamp.to_numpy.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Timestamp.to_numpy.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Timestamp.to_numpy.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Timestamp.to_numpy.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Timestamp.to_numpy.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Timestamp.to_numpy.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Timestamp.to_numpy.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Timestamp.to\_numpy[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html#pandas-timestamp-to-numpy "Link to this heading")

============================================================================================================================================================

Timestamp.to\_numpy(_dtype\=None_, _copy\=False_)[#](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.to_numpy.html#pandas.Timestamp.to_numpy "Link to this definition")

Convert the Timestamp to a NumPy datetime64.

This is an alias method for Timestamp.to\_datetime64(). The dtype and copy parameters are available here only for compatibility. Their values will not affect the return value.

Parameters:

**dtype**dtype, optional

Data type of the output, ignored in this method as the return type is always numpy.datetime64.

**copy**bool, default False

Whether to ensure that the returned value is a new object. This parameter is also ignored as the method does not support copying.

Returns:

numpy.datetime64

See also

`DatetimeIndex.to_numpy`

Similar method for DatetimeIndex.

Examples

\>>> ts \= pd.Timestamp('2020-03-14T15:32:52.192548651')
\>>> ts.to\_numpy()
np.datetime64('2020-03-14T15:32:52.192548651')

Copy to clipboard

Analogous for `pd.NaT`:

\>>> pd.NaT.to\_numpy()
np.datetime64('NaT','ns')

Copy to clipboard

On this page