[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.count.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.count.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.count.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.count.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.count.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.count.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.count.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.count.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.count.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.count.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.count.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.count.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.count.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.count.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.count[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.count.html#pandas-api-typing-rolling-count "Link to this heading")

=============================================================================================================================================================================

Rolling.count(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L2126-L2172)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.count.html#pandas.api.typing.Rolling.count "Link to this definition")

Calculate the rolling count of non NaN observations.

This is useful for identifying windows with missing data, as it counts only non-NaN entries within each window.

Parameters:

**numeric\_only**bool, default False

Include only float, int, boolean columns.

Returns:

Series or DataFrame

Return type is the same as the original object with `np.float64` dtype.

See also

`Series.rolling`

Calling rolling with Series data.

`DataFrame.rolling`

Calling rolling with DataFrames.

`Series.count`

Aggregating count for Series.

`DataFrame.count`

Aggregating count for DataFrame.

Examples

\>>> s \= pd.Series(\[2, 3, np.nan, 10\])
\>>> s.rolling(2).count()
0    NaN
1    2.0
2    1.0
3    1.0
dtype: float64
\>>> s.rolling(3).count()
0    NaN
1    NaN
2    2.0
3    2.0
dtype: float64
\>>> s.rolling(4).count()
0    NaN
1    NaN
2    NaN
3    3.0
dtype: float64

Copy to clipboard

On this page