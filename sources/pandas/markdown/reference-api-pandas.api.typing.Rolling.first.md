[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.first.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.first[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.first.html#pandas-api-typing-rolling-first "Link to this heading")

=============================================================================================================================================================================

Rolling.first(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L3076-L3112)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.first.html#pandas.api.typing.Rolling.first "Link to this definition")

Calculate the rolling First (left-most) element of the window.

Return the first observed value in each rolling window. This is useful for tracking the starting value of a window as it slides forward.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`GroupBy.first`

Similar method for GroupBy objects.

[`Rolling.last`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.last.html#pandas.api.typing.Rolling.last "pandas.api.typing.Rolling.last")

Method to get the last element in each window.

Examples

The example below will show a rolling calculation with a window size of three.

\>>> s \= pd.Series(range(5))
\>>> s.rolling(3).first()
0         NaN
1         NaN
2         0.0
3         1.0
4         2.0
dtype: float64

Copy to clipboard

On this page