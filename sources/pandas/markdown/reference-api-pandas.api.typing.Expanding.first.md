[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.first.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.first[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.first.html#pandas-api-typing-expanding-first "Link to this heading")

===================================================================================================================================================================================

Expanding.first(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L1047-L1083)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.first.html#pandas.api.typing.Expanding.first "Link to this definition")

Calculate the expanding First (left-most) element of the window.

At each point in time, returns the first value in the expanding window, which is the earliest observation in the data.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`GroupBy.first`

Similar method for GroupBy objects.

[`Expanding.last`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.last.html#pandas.api.typing.Expanding.last "pandas.api.typing.Expanding.last")

Method to get the last element in each window.

Examples

The example below will show an expanding calculation with a window size of three.

\>>> s \= pd.Series(range(5))
\>>> s.expanding(3).first()
0         NaN
1         NaN
2         0.0
3         0.0
4         0.0
dtype: float64

Copy to clipboard

On this page