[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.nunique.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.nunique.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.nunique.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.nunique.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.nunique.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.nunique.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.nunique.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.nunique.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.nunique.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.nunique.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.nunique.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.nunique.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.nunique.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.nunique.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.nunique[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.nunique.html#pandas-api-typing-rolling-nunique "Link to this heading")

===================================================================================================================================================================================

Rolling.nunique(_numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L3300-L3342)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.nunique.html#pandas.api.typing.Rolling.nunique "Link to this definition")

Calculate the rolling nunique.

Added in version 3.0.0.

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

`Series.nunique`

Aggregating nunique for Series.

`DataFrame.nunique`

Aggregating nunique for DataFrame.

Examples

\>>> s \= pd.Series(\[1, 4, 2, np.nan, 3, 3, 4, 5\])
\>>> s.rolling(3).nunique()
0    NaN
1    NaN
2    3.0
3    NaN
4    NaN
5    NaN
6    2.0
7    3.0
dtype: float64

Copy to clipboard

On this page