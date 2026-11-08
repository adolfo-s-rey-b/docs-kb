[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.var.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.ExponentialMovingWindow.var[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.var.html#pandas-api-typing-exponentialmovingwindow-var "Link to this heading")

=======================================================================================================================================================================================================================

ExponentialMovingWindow.var(_bias\=False_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/ewm.py#L766-L817)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.var.html#pandas.api.typing.ExponentialMovingWindow.var "Link to this definition")

Calculate the ewm (exponential weighted moment) variance.

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

`Series.var`

Aggregating var for Series.

`DataFrame.var`

Aggregating var for DataFrame.

Examples

\>>> ser \= pd.Series(\[1, 2, 3, 4\])
\>>> ser.ewm(alpha\=0.2).var()
0         NaN
1    0.500000
2    0.991803
3    1.631547
dtype: float64

Copy to clipboard

On this page