[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.skew.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.skew.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.skew.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.skew.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.skew.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.skew.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.skew.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.skew.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.skew.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.skew.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.skew.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.skew.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.skew.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.skew.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.skew[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.skew.html#pandas-api-typing-rolling-skew "Link to this heading")

==========================================================================================================================================================================

Rolling.skew(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L2932-L2974)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.skew.html#pandas.api.typing.Rolling.skew "Link to this definition")

Calculate the rolling unbiased skewness.

This is equivalent to applying `scipy.stats.skew` over each rolling window. A minimum of three periods is required.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`scipy.stats.skew`

Third moment of a probability density.

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.skew`

Aggregating skew for Series.

`DataFrame.skew`

Aggregating skew for DataFrame.

Notes

A minimum of three periods is required for the rolling calculation.

Examples

\>>> ser \= pd.Series(\[1, 5, 2, 7, 15, 6\])
\>>> ser.rolling(3).skew().round(6)
0         NaN
1         NaN
2    1.293343
3   -0.585583
4    0.670284
5    1.652317
dtype: float64

Copy to clipboard

On this page