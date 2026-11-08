[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.rank.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Expanding.rank.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.rank.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Expanding.rank.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Expanding.rank.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Expanding.rank.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Expanding.rank.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Expanding.rank.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Expanding.rank.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Expanding.rank.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Expanding.rank.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Expanding.rank.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Expanding.rank.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Expanding.rank.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Expanding.rank[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.rank.html#pandas-api-typing-expanding-rank "Link to this heading")

================================================================================================================================================================================

Expanding.rank(_method\='average'_, _ascending\=True_, _pct\=False_, _numeric\_only\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/window/expanding.py#L1185-L1262)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.rank.html#pandas.api.typing.Expanding.rank "Link to this definition")

Calculate the expanding rank.

Each value is ranked relative to all prior observations, with configurable tie-breaking and optional percentile normalization.

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

`Series.expanding`

Calling expanding with Series data.

`DataFrame.expanding`

Calling expanding with DataFrames.

`Series.rank`

Aggregating rank for Series.

`DataFrame.rank`

Aggregating rank for DataFrame.

Examples

\>>> s \= pd.Series(\[1, 4, 2, 3, 5, 3\])
\>>> s.expanding().rank()
0    1.0
1    2.0
2    2.0
3    3.0
4    5.0
5    3.5
dtype: float64

Copy to clipboard

\>>> s.expanding().rank(method\="max")
0    1.0
1    2.0
2    2.0
3    3.0
4    5.0
5    4.0
dtype: float64

Copy to clipboard

\>>> s.expanding().rank(method\="min")
0    1.0
1    2.0
2    2.0
3    3.0
4    5.0
5    3.0
dtype: float64

Copy to clipboard

On this page