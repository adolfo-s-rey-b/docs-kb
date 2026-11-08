[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.rank.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Rolling.rank.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.rank.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Rolling.rank.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Rolling.rank.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Rolling.rank.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Rolling.rank.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Rolling.rank.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Rolling.rank.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Rolling.rank.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Rolling.rank.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Rolling.rank.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Rolling.rank.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Rolling.rank.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Rolling.rank[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.rank.html#pandas-api-typing-rolling-rank "Link to this heading")

==========================================================================================================================================================================

Rolling.rank(_method\='average'_, _ascending\=True_, _pct\=False_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/rolling.py#L3219-L3298)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.rank.html#pandas.api.typing.Rolling.rank "Link to this definition")

Calculate the rolling rank.

Compute the rank of each value within each rolling window. Ties are resolved using the `method` parameter.

Parameters:

**method**{‘average’, ‘min’, ‘max’}, default ‘average’

How to rank the group of records that have the same value (i.e. ties):

*   average: average rank of the group
    
*   min: lowest rank in the group
    
*   max: highest rank in the group
    

**ascending**bool, default True

Whether or not the elements should be ranked in ascending order.

**pct**bool, default False

Whether or not to display the returned rankings in percentile form.

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

`Series.rank`

Aggregating rank for Series.

`DataFrame.rank`

Aggregating rank for DataFrame.

Examples

\>>> s \= pd.Series(\[1, 4, 2, 3, 5, 3\])
\>>> s.rolling(3).rank()
0    NaN
1    NaN
2    2.0
3    2.0
4    3.0
5    1.5
dtype: float64

Copy to clipboard

\>>> s.rolling(3).rank(method\="max")
0    NaN
1    NaN
2    2.0
3    2.0
4    3.0
5    2.0
dtype: float64

Copy to clipboard

\>>> s.rolling(3).rank(method\="min")
0    NaN
1    NaN
2    2.0
3    2.0
4    3.0
5    1.0
dtype: float64

Copy to clipboard

On this page