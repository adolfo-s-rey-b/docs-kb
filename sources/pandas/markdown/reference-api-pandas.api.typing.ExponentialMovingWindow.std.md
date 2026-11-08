[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.ExponentialMovingWindow.std[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html#pandas-api-typing-exponentialmovingwindow-std "Link to this heading")

=======================================================================================================================================================================================================================

ExponentialMovingWindow.std(_bias\=False_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/ewm.py#L716-L764)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html#pandas.api.typing.ExponentialMovingWindow.std "Link to this definition")

Calculate the ewm (exponential weighted moment) standard deviation.

The weighting is controlled by the `com`, `span`, `halflife`, or `alpha` parameter specified when calling `DataFrame.ewm()` or `Series.ewm()`.

Parameters:

**bias**bool, default False

Use a standard estimation bias correction.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`Series.ewm`

Calling ewm with Series data.

`DataFrame.ewm`

Calling ewm with DataFrames.

`Series.std`

Aggregating std for Series.

`DataFrame.std`

Aggregating std for DataFrame.

Examples

\>>> ser \= pd.Series(\[1, 2, 3, 4\])
\>>> ser.ewm(alpha\=0.2).std()
0         NaN
1    0.707107
2    0.995893
3    1.277320
dtype: float64

Copy to clipboard

On this page