[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.sum.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Window.sum[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.sum.html#pandas-api-typing-window-sum "Link to this heading")

====================================================================================================================================================================

Window.sum(_numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L1307-L1367)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.sum.html#pandas.api.typing.Window.sum "Link to this definition")

Calculate the rolling weighted window sum.

The window type is determined by the `win_type` parameter specified in `DataFrame.rolling()` or `Series.rolling()`. Additional keyword arguments are passed to the SciPy window function.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**\*\*kwargs**

Keyword arguments to configure the `SciPy` weighted window type.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.sum`

Aggregating sum for Series.

`DataFrame.sum`

Aggregating sum for DataFrame.

Examples

\>>> ser \= pd.Series(\[0, 1, 5, 2, 8\])

Copy to clipboard

To get an instance of `Window` we need to pass the parameter win\_type.

\>>> type(ser.rolling(2, win\_type\="gaussian"))
<class 'pandas.api.typing.Window'>

Copy to clipboard

In order to use the SciPy Gaussian window we need to provide the parameters M and std. The parameter M corresponds to 2 in our example. We pass the second parameter std as a parameter of the following method (sum in this case):

\>>> ser.rolling(2, win\_type\="gaussian").sum(std\=3)
0         NaN
1    0.986207
2    5.917243
3    6.903450
4    9.862071
dtype: float64

Copy to clipboard

On this page