[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.last.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.last.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.last.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.last.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.last.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.last.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.last.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.last.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.last.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.last.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.last.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.last.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.last.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.last.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.last[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.last.html#pandas-api-typing-rolling-last "Link to this heading")

==========================================================================================================================================================================

Rolling.last(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L3114-L3150)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.last.html#pandas.api.typing.Rolling.last "Link to this definition")

Calculate the rolling Last (right-most) element of the window.

Return the last observed value in each rolling window. This is useful for tracking the most recent value of a window as it slides forward.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`GroupBy.last`

Similar method for GroupBy objects.

[`Rolling.first`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.first.html#pandas.api.typing.Rolling.first "pandas.api.typing.Rolling.first")

Method to get the first element in each window.

Examples

The example below will show a rolling calculation with a window size of three.

\>>> s \= pd.Series(range(5))
\>>> s.rolling(3).last()
0         NaN
1         NaN
2         2.0
3         3.0
4         4.0
dtype: float64

Copy to clipboard

On this page