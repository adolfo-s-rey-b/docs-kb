[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.std.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Window.std.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.std.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Window.std.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Window.std.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Window.std.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Window.std.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Window.std.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Window.std.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Window.std.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Window.std.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Window.std.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Window.std.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Window.std.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Window.std[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.std.html#pandas-api-typing-window-std "Link to this heading")

====================================================================================================================================================================

Window.std(_ddof\=1_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L1487-L1542)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.std.html#pandas.api.typing.Window.std "Link to this definition")

Calculate the rolling weighted window standard deviation.

The window type is determined by the `win_type` parameter specified in `DataFrame.rolling()` or `Series.rolling()`. Additional keyword arguments are passed to the SciPy window function.

Parameters:

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.

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

`Series.std`

Aggregating std for Series.

`DataFrame.std`

Aggregating std for DataFrame.

Examples

\>>> ser \= pd.Series(\[0, 1, 5, 2, 8\])

Copy to clipboard

To get an instance of `Window` we need to pass the parameter win\_type.

\>>> type(ser.rolling(2, win\_type\="gaussian"))
<class 'pandas.api.typing.Window'>

Copy to clipboard

In order to use the SciPy Gaussian window we need to provide the parameters M and std. The parameter M corresponds to 2 in our example. We pass the second parameter std as a parameter of the following method:

\>>> ser.rolling(2, win\_type\="gaussian").std(std\=3)
0         NaN
1    0.707107
2    2.828427
3    2.121320
4    4.242641
dtype: float64

Copy to clipboard

On this page