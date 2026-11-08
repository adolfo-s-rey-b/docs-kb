[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.DataError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.DataError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.DataError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.DataError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.DataError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.DataError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.DataError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.DataError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.DataError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.DataError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.DataError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.DataError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.DataError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.DataError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.DataError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.DataError.html#pandas-errors-dataerror "Link to this heading")

=====================================================================================================================================================

exception pandas.errors.DataError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L635-L653)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.DataError.html#pandas.errors.DataError "Link to this definition")

Exception raised when performing an operation on non-numerical data.

For example, calling `ohlc` on a non-numerical column or a function on a rolling window.

See also

`Series.rolling`

Provide rolling window calculations on Series object.

`DataFrame.rolling`

Provide rolling window calculations on DataFrame object.

Examples

\>>> ser \= pd.Series(\["a", "b", "c"\])
\>>> ser.rolling(2).sum()
Traceback (most recent call last):
DataError: No numeric types to aggregate

Copy to clipboard

On this page