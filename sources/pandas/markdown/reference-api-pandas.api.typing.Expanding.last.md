[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.last.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.last.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.last.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.last.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.last.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.last.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.last.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.last.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.last.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.last.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.last.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.last.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.last.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.last.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.last[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.last.html#pandas-api-typing-expanding-last "Link to this heading")

================================================================================================================================================================================

Expanding.last(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L1085-L1121)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.last.html#pandas.api.typing.Expanding.last "Link to this definition")

Calculate the expanding Last (right-most) element of the window.

At each point in time, returns the last value in the expanding window, which is the most recent observation in the data.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`GroupBy.last`

Similar method for GroupBy objects.

[`Expanding.first`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.first.html#pandas.api.typing.Expanding.first "pandas.api.typing.Expanding.first")

Method to get the first element in each window.

Examples

The example below will show an expanding calculation with a window size of three.

\>>> s \= pd.Series(range(5))
\>>> s.expanding(3).last()
0         NaN
1         NaN
2         2.0
3         3.0
4         4.0
dtype: float64

Copy to clipboard

On this page